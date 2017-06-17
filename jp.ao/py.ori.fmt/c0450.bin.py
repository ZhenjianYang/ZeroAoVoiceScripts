from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付カイル",             # 1
        "ドリス",                 # 2
        "アーロン",               # 3
        "レティシア支配人",       # 4
        "ミンネス",               # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "市民",                   # 8
        "女の子",                 # 9
        "市民",                   # 10
        "市民",                   # 11
        "観光客",                 # 12
        "市民",                   # 13
        "市民",                   # 14
        "市民",                   # 15
        "デリック",               # 16
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
        "Function_9_989",          # 09, 9
        "Function_10_B23",         # 0A, 10
        "Function_11_B27",         # 0B, 11
        "Function_12_1F34",        # 0C, 12
        "Function_13_1F38",        # 0D, 13
        "Function_14_3052",        # 0E, 14
        "Function_15_3E46",        # 0F, 15
        "Function_16_4873",        # 10, 16
        "Function_17_4985",        # 11, 17
        "Function_18_4A94",        # 12, 18
        "Function_19_4B20",        # 13, 19
        "Function_20_4B93",        # 14, 20
        "Function_21_4BC0",        # 15, 21
        "Function_22_4BE5",        # 16, 22
        "Function_23_4D32",        # 17, 23
        "Function_24_4DDB",        # 18, 24
        "Function_25_4E46",        # 19, 25
        "Function_26_4E71",        # 1A, 26
        "Function_27_4EA6",        # 1B, 27
        "Function_28_4ED8",        # 1C, 28
        "Function_29_5B19",        # 1D, 29
        "Function_30_7861",        # 1E, 30
        "Function_31_78AC",        # 1F, 31
        "Function_32_78F0",        # 20, 32
        "Function_33_793B",        # 21, 33
        "Function_34_7986",        # 22, 34
        "Function_35_79D1",        # 23, 35
        "Function_36_7A1C",        # 24, 36
        "Function_37_7A67",        # 25, 37
        "Function_38_7AB2",        # 26, 38
        "Function_39_7AFD",        # 27, 39
        "Function_40_7B48",        # 28, 40
        "Function_41_7B93",        # 29, 41
        "Function_42_7BDE",        # 2A, 42
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
            "『おいしい鍋料理　圧力鍋編』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_985")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_985")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『満腹寄せ鍋』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_985")

    TalkEnd(0xFF)
    Return()

    # Function_8_8DA end

    def Function_9_989(): pass

    label("Function_9_989")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C")

    #C0003
    ChrTalk(
        0xC,
        (
            "おや、皆様……\x01",
            "まだ私に何か御用ですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xC,
        (
            "我がクインシー社とアルモリカ村の\x01",
            "『アルモリカ・ハニーカンパニー』計画は\x01",
            "徐々に進行しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xC,
        (
            "今後の展望を、皆様も\x01",
            "楽しみにしてくださると幸いですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B1F")

    label("loc_A7C")


    #C0006
    ChrTalk(
        0xC,
        (
            "我がクインシー社とアルモリカ村の\x01",
            "『アルモリカ・ハニーカンパニー』計画は\x01",
            "徐々に進行しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xC,
        (
            "今後の展望を、皆様も\x01",
            "楽しみにしてくださると幸いですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1F")

    TalkEnd(0xFE)
    Return()

    # Function_9_989 end

    def Function_10_B23(): pass

    label("Function_10_B23")

    Call(0, 11)
    Return()

    # Function_10_B23 end

    def Function_11_B27(): pass

    label("Function_11_B27")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAE")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0008
    ChrTalk(
        0xB,
        "あら、皆様は警察の……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00000Fええ、こちらの状況を\x01",
            "聞かせてもらっていいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "はい、当ホテルでは只今\x01",
            "元からの宿泊客を含め、\x01",
            "避難者を多数受け入れております。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "備蓄食料もございますので、\x01",
            "１ヶ月程度は凌げる見込みですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "とにかく、詳しい情報が\x01",
            "入らないことが皆様の不安に\x01",
            "つながっているという状態ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "現状、最小限の混乱で済んでいますが\x01",
            "これが続くとなると……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#00104Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00001F俺たちは、これからすぐに\x01",
            "事態収束のため行動を開始します。\x02\x03",

            "なので、しばらくの間\x01",
            "このまま様子を見て頂けますか。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "ええ、かしこまりました。\x01",
            "皆様もお気を付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 6)

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3B")

    #C0017
    ChrTalk(
        0xB,
        "《ホテル・ミレニアム》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "うふふ、当ホテルでは\x01",
            "お客様の様々なニーズに\x01",
            "お応えしておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "何かご所望がございましたら、\x01",
            "いつでも仰ってくださいませ。\x02",
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
            "ホテルや宿酒場に宿泊すると\x01",
            "ＣＰを回復する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通常の宿酒場ではＣＰ１００、\x01",
            "高級ホテルではＣＰ２００が回復します。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F38")
    SetScenarioFlags(0x0, 0)

    label("loc_F38")

    SetScenarioFlags(0x136, 5)

    label("loc_F3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F30")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_FA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC1")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F2B")

    label("loc_FC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD5")
    Jump("loc_1F2B")

    label("loc_FD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1100")

    #C0022
    ChrTalk(
        0xB,
        (
            "大統領拘束の一報を受け、\x01",
            "避難者の方々もそれぞれ\x01",
            "ご自宅に戻られましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        (
            "大樹については詳細不明ですが……\x01",
            "とりあえずモヤが晴れたことで\x01",
            "街もそれなりに落ち着いた印象です。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "とにかく、私たちは\x01",
            "今の内に各種出来る準備を\x01",
            "進めておかなければいけません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123C")

    #C0025
    ChrTalk(
        0xB,
        (
            "戒厳令と外出禁止令の通告を受け、\x01",
            "当ホテルでは避難者の受け入れを\x01",
            "すぐに検討したのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "流石に、あのモヤと\x01",
            "人形兵士の出現は想定外でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "どうやら、皆さんの大統領への不満も\x01",
            "極限まで高まっているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "今はどちらかというと、\x01",
            "不安の方が大きいという印象ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12C6")

    label("loc_123C")


    #C0029
    ChrTalk(
        0xB,
        (
            "どうやら、皆さんの大統領への不満も\x01",
            "極限まで高まっているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "今はどちらかというと、\x01",
            "不安の方が大きいという印象ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C6")

    Jump("loc_1F2B")

    label("loc_12CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_145F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A7")

    #C0031
    ChrTalk(
        0xB,
        (
            "演説の様子は\x01",
            "ホテルの導力ネットを通じて\x01",
            "拝見しましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "流石に外国からいらした\x01",
            "お客様の動揺には\x01",
            "凄まじいものがありました。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xB,
        (
            "何とか皆さん、本国まで\x01",
            "辿り着けるとよいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_145A")

    label("loc_13A7")


    #C0034
    ChrTalk(
        0xB,
        (
            "導力鉄道は本日をもって\x01",
            "運行を停止するそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xB,
        (
            "とにかく、お客様方が\x01",
            "帰路につけないのでは話になりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        (
            "飛行船の運航状況を含め、\x01",
            "徹底的に情報を集めませんと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145A")

    Jump("loc_1F2B")

    label("loc_145F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1519")

    #C0037
    ChrTalk(
        0xB,
        (
            "夕暮れと炎の色に染まる歓楽街……\x01",
            "あの日の光景は、まさに\x01",
            "悪夢としか言い様がありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "……ともかく、一刻も早く\x01",
            "日常を取り戻せるよう\x01",
            "出来ることを尽くしませんと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_15A2")

    #C0039
    ChrTalk(
        0xB,
        (
            "マインツ方面では\x01",
            "今も警備隊の皆さんが\x01",
            "奮戦されているそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "本当に警備隊の皆さんは\x01",
            "私たち市民の誇りですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_15A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D4")

    #C0041
    ChrTalk(
        0xB,
        (
            "昨日は列車事故の影響で、\x01",
            "鉄道のダイヤが大きく乱れたため……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "結局、クロスベル滞在を\x01",
            "一日延長した人もいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "とはいえ、何とか今朝までに\x01",
            "完全に復旧できて幸いでしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "足止めされるになった\x01",
            "お客様も、今朝には全員\x01",
            "無事に送り出すことができましたので。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_175D")

    label("loc_16D4")


    #C0045
    ChrTalk(
        0xB,
        (
            "足止めされることになった\x01",
            "お客様も、今朝には全員\x01",
            "無事に送り出すことができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "これも全ては、\x01",
            "警備隊の皆様のおかげですわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175D")

    Jump("loc_1F2B")

    label("loc_1762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1813")

    #C0047
    ChrTalk(
        0xB,
        (
            "何でも西クロスベル街道方面で\x01",
            "列車事故が起きたそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "今日これから帰路につく\x01",
            "お客様がたを混乱させないためにも\x01",
            "まずは情報を集めないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_19CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1916")

    #C0049
    ChrTalk(
        0xB,
        (
            "導力ネットによる予約サービスも\x01",
            "おかげ様で好評を頂いておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "現状まだまだ利用される方が\x01",
            "少ないのも確かではありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "更なるネットワーク拡充の折には、\x01",
            "通信器によるご予約件数を\x01",
            "必ず上回ると確信しておりますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19CA")

    label("loc_1916")


    #C0052
    ChrTalk(
        0xB,
        (
            "導力ネットの素晴らしい点は\x01",
            "たとえ受付時間外であっても\x01",
            "予約を頂ける所にありますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "通信器と違って、導力メールは\x01",
            "２４時間いつでも送受信することが\x01",
            "可能でございますからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CA")

    Jump("loc_1F2B")

    label("loc_19CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A61")

    #C0054
    ChrTalk(
        0xB,
        "国家独立の是非、でございますか……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "大変難しい問題ではありますが、\x01",
            "それを市民に問う事は\x01",
            "非常に意義のある事だと思いますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1ACB")

    #C0056
    ChrTalk(
        0xB,
        (
            "うふふ、ついに\x01",
            "本会議が始まりますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "ディーター市長には\x01",
            "頑張って頂きませんと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BA3")

    #C0058
    ChrTalk(
        0xB,
        (
            "私が支配人に就く以前から、\x01",
            "当ホテルには過去に様々な要人の方を\x01",
            "ご招待させて頂いた実績がございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        (
            "今回は話がなく残念でしたが、\x01",
            "各国首脳の皆様にもいつかの折には\x01",
            "ご宿泊して頂きたいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C5D")

    #C0060
    ChrTalk(
        0xB,
        (
            "ホテル業に携わるものとして\x01",
            "明日からの通商会議は\x01",
            "いやでも注目してしまいますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "結ばれる協定の内容によっては\x01",
            "今後の観光客の数などに\x01",
            "影響も出て来るでしょうからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D19")

    #C0062
    ChrTalk(
        0xB,
        "今日は雨でございますわね。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "当ホテルでは、雨の日でも\x01",
            "お楽しみ頂ける観光スポットを\x01",
            "ご紹介致しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "ぜひ、お気軽に\x01",
            "お問い合わせくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB9")

    label("loc_1D19")


    #C0065
    ChrTalk(
        0xB,
        (
            "基本的に、この歓楽街は\x01",
            "雨の日でもお楽しみ頂ける\x01",
            "場所がほとんどですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "それでも外出が億劫な方には、\x01",
            "当ホテルの各種ルームサービスも\x01",
            "オススメですわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB9")

    Jump("loc_1F2B")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E88")

    #C0067
    ChrTalk(
        0xB,
        "《ホテル・ミレニアム》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "うふふ、当ホテルでは\x01",
            "お客様の様々なニーズに\x01",
            "お応えしておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "何かご要望がございましたら、\x01",
            "いつでも仰ってくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F2B")

    label("loc_1E88")


    #C0070
    ChrTalk(
        0xB,
        (
            "エステや食事のルームサービス、\x01",
            "各種ブッキングサービスに\x01",
            "導力ネットを用いたご予約サービス……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        (
            "当ホテルでは、お客様の様々な\x01",
            "ニーズにお応えしておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2B")

    Jump("loc_F45")

    label("loc_1F30")

    TalkEnd(0xB)
    Return()

    # Function_11_B27 end

    def Function_12_1F34(): pass

    label("Function_12_1F34")

    Call(0, 13)
    Return()

    # Function_12_1F34 end

    def Function_13_1F38(): pass

    label("Function_13_1F38")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A9")

    #C0072
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ホテル・ミレニアム》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "当フロントでは当日の宿泊予約も\x01",
            "受け付けておりますので、\x01",
            "どうぞお気軽にお申し付け下さいませ。\x02",
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
            "ホテルや宿酒場に宿泊すると\x01",
            "ＣＰを回復する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通常の宿酒場ではＣＰ１００、\x01",
            "高級ホテルではＣＰ２００が回復します。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x136, 5)

    label("loc_20A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_304E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_210F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212F")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3049")

    label("loc_212F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2143")
    Jump("loc_3049")

    label("loc_2143")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3049")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_227C")

    #C0076
    ChrTalk(
        0x8,
        (
            "支配人の指示で、有事のための\x01",
            "備えをこれまで以上に\x01",
            "強化することになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "ただし、各種物資に関しては\x01",
            "自治州内の限りある商品を無闇に\x01",
            "買い占めるワケにもいきませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "政府への相談も視野に入れ、\x01",
            "外国方面から買い集める手段を\x01",
            "さっそく探り始めている所です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_227C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2379")

    #C0079
    ChrTalk(
        0x8,
        (
            "モヤの出現と同時にここへ\x01",
            "駆け込んだ方々の様子は、\x01",
            "それはもうパニック状態でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "人形の兵士が市民を襲う事は\x01",
            "一応ないと分かってからは、\x01",
            "少しは落ち着きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "とにかく、一刻も早くこの状況を\x01",
            "何とかして頂きたいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_247B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F0")

    #C0082
    ChrTalk(
        0x8,
        (
            "……今朝の演説には\x01",
            "本当に驚かされました。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "大統領の主張、\x01",
            "理解はできるのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2476")

    label("loc_23F0")


    #C0084
    ChrTalk(
        0x8,
        (
            "……ふむ、とりあえず\x01",
            "余計な事は口に出すべきでは\x01",
            "ありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "何はともあれ……\x01",
            "しばらくは成り行きを\x01",
            "見守るしかありません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2476")

    Jump("loc_3049")

    label("loc_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_254D")

    #C0086
    ChrTalk(
        0x8,
        (
            "襲撃の日、当ホテルには幸いにも\x01",
            "大した被害はありませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "アルカンシェルは……\x01",
            "本当に酷いものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "何が目的かは知りませんが……\x01",
            "このような所業、\x01",
            "許されるはずがありません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_254D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2600")

    #C0089
    ChrTalk(
        0x8,
        (
            "マインツで起こっている事件は\x01",
            "帝国の陰謀ではないかと\x01",
            "考えておられる方も多いみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "それがもし本当だとしたら……\x01",
            "不戦条約は一体何だったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_2600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26B2")

    #C0091
    ChrTalk(
        0x8,
        (
            "昨日は事故の影響で\x01",
            "宿泊をキャンセルしたいという\x01",
            "連絡を多く受けたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "大陸横断鉄道はまさに\x01",
            "我々にとっても生命線……\x01",
            "被害が最小限で済んで一安心ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_26B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_272A")

    #C0093
    ChrTalk(
        0x8,
        "ふむ、列車事故ですか……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "クロスベルでは\x01",
            "比較的珍しいことですが……\x01",
            "一体原因は何なんでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_272A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_287B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FC")

    #C0095
    ChrTalk(
        0x8,
        (
            "最近ドリスさんの仕事ぶりが\x01",
            "めきめき良くなっているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "掃除の手際はもちろん、\x01",
            "お客様からの評判も上々でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "これも教育係を務める\x01",
            "アーロンさんの指導の賜物ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2876")

    label("loc_27FC")


    #C0098
    ChrTalk(
        0x8,
        (
            "最近ドリスさんの仕事ぶりが\x01",
            "めきめき良くなっているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "これも教育係を務める\x01",
            "アーロンさんの指導の賜物ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2876")

    Jump("loc_3049")

    label("loc_287B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297B")

    #C0100
    ChrTalk(
        0x8,
        (
            "私はクロスベル人ですが、\x01",
            "以前は帝国のホテルに\x01",
            "勤めていた事があるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "こう言っては何ですが、\x01",
            "帝国にいた頃は貴族の方々に\x01",
            "神経をすり減らす日々でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "こちらに来てからは、伸び伸び\x01",
            "仕事をさせて頂いておりますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A1A")

    label("loc_297B")


    #C0103
    ChrTalk(
        0x8,
        (
            "帝国のホテルはサービス技術を\x01",
            "学ぶには良い環境でしたが、\x01",
            "その分気疲れも相当なものでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "こちらに来てからは、伸び伸び\x01",
            "仕事をさせて頂いておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1A")

    Jump("loc_3049")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    #C0105
    ChrTalk(
        0x8,
        (
            "昨日、仕事帰りに\x01",
            "遠目ながらオルキスタワーを\x01",
            "拝見させて頂いたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "いやはや、あの迫力たるや\x01",
            "話に聞いていた以上でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "今度はぜひとも近くに行って、\x01",
            "ビルを見上げてみたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B88")

    label("loc_2B04")


    #C0108
    ChrTalk(
        0x8,
        (
            "遠目ながら、オルキルタワーの\x01",
            "迫力には本当に圧倒されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "今度はぜひとも近くに行って、\x01",
            "ビルを見上げてみたいものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B88")

    Jump("loc_3049")

    label("loc_2B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C57")

    #C0110
    ChrTalk(
        0x8,
        (
            "お客様は除幕式の様子を\x01",
            "ご見学されましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "何でも花火も打ち上げられ、\x01",
            "大変見応えのある式典だったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "オルキスタワーの威容……\x01",
            "私も早く拝見したいものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CD9")

    label("loc_2C57")


    #C0113
    ChrTalk(
        0x8,
        (
            "除幕式では花火も打ち上げられ、\x01",
            "大変見応えがあったと聞きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "オルキスタワーの威容……\x01",
            "私も早く拝見したいものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD9")

    Jump("loc_3049")

    label("loc_2CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD2")

    #C0115
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "本日も良い天気でございますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "街は警察による警戒体制が\x01",
            "敷かれておりますが、\x01",
            "観光日和には違いありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "どこか良いスポットを\x01",
            "お探しでしたら、目的に合わせて\x01",
            "ご案内させて頂きますよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E5B")

    label("loc_2DD2")


    #C0118
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "本日も良い天気でございますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "どこか良いスポットを\x01",
            "お探しでしたら、目的に合わせて\x01",
            "ご案内させて頂きますよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5B")

    Jump("loc_3049")

    label("loc_2E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2A")

    #C0120
    ChrTalk(
        0x8,
        (
            "おはようございます。\x01",
            "本日もようこそいらっしゃいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "雨天時のお出掛けの際は\x01",
            "仰っていただければ、\x01",
            "傘のご提供もさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        "どうぞお気軽にお申し付け下さい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F9E")

    label("loc_2F2A")


    #C0123
    ChrTalk(
        0x8,
        (
            "雨天時のお出掛けの際は\x01",
            "仰っていただければ、\x01",
            "傘のご提供もさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        "どうぞお気軽にお申し付け下さい。\x02",
    )

    CloseMessageWindow()

    label("loc_2F9E")

    Jump("loc_3049")

    label("loc_2FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3049")

    #C0125
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ホテル・ミレニアム》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "当フロントでは当日の宿泊予約も\x01",
            "受け付けておりますので、\x01",
            "どうぞお気軽にお申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3049")

    Jump("loc_20B3")

    label("loc_304E")

    TalkEnd(0x8)
    Return()

    # Function_13_1F38 end

    def Function_14_3052(): pass

    label("Function_14_3052")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312D")

    #C0127
    ChrTalk(
        0xFE,
        (
            "先ほどレティシア支配人から\x01",
            "当分は利益度外視で営業を行うとの\x01",
            "意思表明がございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "今はクロスベル全体が困難にある時……\x01",
            "私もこれまでの経験を全て活かすつもりで\x01",
            "全力で支配人を支える所存です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_312D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_31E6")

    #C0129
    ChrTalk(
        0xFE,
        (
            "この度のホテルの無償提供で、\x01",
            "支配人がミラではなく人を大切される\x01",
            "方であることがよく分かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "そんな方の元で仕事が出来るのは\x01",
            "本当に幸せなことだと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_31E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32AE")

    #C0131
    ChrTalk(
        0xFE,
        (
            "独立宣言以降、お客様の数は\x01",
            "日に日に減ってはいたのですが……\x01",
            "今朝の演説は決定的ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "こういう時にする話でもありませんが……\x01",
            "当ホテルも経営方針を見直さざるを\x01",
            "得ないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_32AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338D")

    #C0133
    ChrTalk(
        0xFE,
        (
            "襲撃事件が街に残した爪痕は\x01",
            "余りに大きいと言う他ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "警備隊の被害は甚大、\x01",
            "それにあのイリア嬢まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "このようなことは\x01",
            "二度と起こってはならない……\x01",
            "ただ、そう思うばかりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3410")

    label("loc_338D")


    #C0136
    ChrTalk(
        0xFE,
        (
            "警備隊の被害は甚大、\x01",
            "それにあのイリア嬢まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "このようなことは\x01",
            "二度と起こってはならない……\x01",
            "ただ、そう思うばかりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3410")

    Jump("loc_3E42")

    label("loc_3415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_34A6")

    #C0138
    ChrTalk(
        0xFE,
        (
            "昨日起こった襲撃事件……\x01",
            "まだまだ事態は収束に\x01",
            "向かってくれないようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "マインツの住民の\x01",
            "皆様のことが本当に心配です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_34A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_354D")

    #C0140
    ChrTalk(
        0xFE,
        (
            "脱線事故は不可思議な\x01",
            "魔獣の仕業と聞きましたが……\x01",
            "何とも不気味な話でございますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "何か不吉なことの前触れ、\x01",
            "などとは考えたくないものですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_354D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_360A")

    #C0142
    ChrTalk(
        0xFE,
        (
            "そろそろチェックインのお客様が\x01",
            "見え出す時間なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "どうやら列車事故の影響が\x01",
            "さっそく出ているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "皆さん、無事に\x01",
            "到着して頂けるとよいのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_360A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_36B4")

    #C0145
    ChrTalk(
        0xFE,
        (
            "今の時期、デラックスルームが\x01",
            "空室になることは\x01",
            "そう珍しいことではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "つまり、確実に\x01",
            "ご宿泊になられたい方には\x01",
            "今が狙い目ということですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_36B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_389A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DB")

    #C0147
    ChrTalk(
        0xFE,
        (
            "国家独立の是非……\x01",
            "基本的に賛成意見が多いものの\x01",
            "様々な意見があるようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "私のような年寄りは、\x01",
            "どうしても２大国の脅威について\x01",
            "ばかり考えてしまいますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "当ホテルがそうであったように、\x01",
            "クロスベル自治州も今こそ変化が\x01",
            "必要な時期なのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3895")

    label("loc_37DB")


    #C0150
    ChrTalk(
        0xFE,
        (
            "私のような年寄りは、\x01",
            "どうしても２大国の脅威について\x01",
            "ばかり考えてしまいますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "当ホテルがそうであったように、\x01",
            "クロスベル自治州も今こそ変化が\x01",
            "必要な時期なのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3895")

    Jump("loc_3E42")

    label("loc_389A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3929")

    #C0152
    ChrTalk(
        0xFE,
        (
            "いよいよ通商会議の\x01",
            "本会議が始まるわけですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "いやはや、ディーター市長と\x01",
            "マクダエル議長には\x01",
            "期待せずにはおれませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_3929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39C7")

    #C0154
    ChrTalk(
        0xFE,
        (
            "オルキスタワーには全てのフロアに\x01",
            "導力ネットが引かれているそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ふふ、当ホテルの導力ネット予約も\x01",
            "ますます盛況になりそうですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_39C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA4")

    #C0156
    ChrTalk(
        0xFE,
        (
            "少し前まで頼りない所もあった\x01",
            "ドリスさんですが、なかなかどうして\x01",
            "最近は安心して見ていられますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "後進の成長を肌で感じられる……\x01",
            "教育係を任された者として\x01",
            "これ以上の喜びはありませんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B3B")

    label("loc_3AA4")


    #C0158
    ChrTalk(
        0xFE,
        (
            "ドリスさんが成長してくれて\x01",
            "本当に嬉しく思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "後進の成長を肌で感じられる……\x01",
            "教育係を任された者として\x01",
            "これ以上の喜びはありませんからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3B")

    Jump("loc_3E42")

    label("loc_3B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C37")

    #C0160
    ChrTalk(
        0xFE,
        (
            "記念祭ほどの盛況さはないものの、\x01",
            "当ホテルの客足は\x01",
            "順調に推移してございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "支配人肝いりの導力ネットによる\x01",
            "予約システムも反響は上々ですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "いやはや、《ホテル・ミレニアム》の\x01",
            "未来は明るうございますな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CE5")

    label("loc_3C37")


    #C0163
    ChrTalk(
        0xFE,
        (
            "伝統と革新の融合……\x01",
            "それがレティシア支配人の目指す\x01",
            "当ホテルのあり方でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "私も最初は戸惑いもしましたが、\x01",
            "今では支配人のことを\x01",
            "全面的に信頼しておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE5")

    Jump("loc_3E42")

    label("loc_3CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DBF")

    #C0165
    ChrTalk(
        0xFE,
        (
            "当ホテルは今年で開業６０周年……\x01",
            "ちなみに私がここで働き始めて\x01",
            "早３０年以上の歳月が経ちました。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "気づけば一番の古株ですよ。\x01",
            "いやはや、時代の流れというのは\x01",
            "本当に早いものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E42")

    label("loc_3DBF")


    #C0167
    ChrTalk(
        0xFE,
        (
            "このホテルで働き始めて\x01",
            "早３０年以上……\x01",
            "気づけば一番の古株ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "いやはや、時代の流れというのは\x01",
            "本当に早いものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E42")

    TalkEnd(0xFE)
    Return()

    # Function_14_3052 end

    def Function_15_3E46(): pass

    label("Function_15_3E46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EEE")

    #C0169
    ChrTalk(
        0xFE,
        (
            "ようやく、避難者の方々を一通り\x01",
            "お見送りすることができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "こんな状況ですが……\x01",
            "皆さんから、お礼の言葉をいただけて\x01",
            "本当に嬉しかったです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_3EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F95")

    #C0171
    ChrTalk(
        0xFE,
        (
            "状況がどうあれ……\x01",
            "ホテルがここまで忙しくなるのは\x01",
            "ずいぶん久しぶりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "ホテル・ミレニアムの一員として、\x01",
            "全力でサービスに努めさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_3F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403F")

    #C0173
    ChrTalk(
        0xFE,
        (
            "私にはうまく事態を\x01",
            "飲み込めないのですが……\x01",
            "今は複雑な気持ちで一杯です。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "確かに私たちは投票によって、\x01",
            "独立に賛成したわけですけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_409E")

    label("loc_403F")


    #C0175
    ChrTalk(
        0xFE,
        (
            "……手を止めると、何だか\x01",
            "色々考えちゃってダメですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "さてと……仕事に励みませんと。\x02",
    )

    CloseMessageWindow()

    label("loc_409E")

    Jump("loc_486F")

    label("loc_40A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4184")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40D5")
    Call(0, 42)
    Return()

    label("loc_40D5")


    #C0177
    ChrTalk(
        0xFE,
        (
            "魔獣の咆哮に銃撃の音、\x01",
            "それに警官隊の方々の怒号に悲鳴……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "……襲撃の日のことを思い出すと、\x01",
            "今でも震えが止まりません……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "どうして、この街でこんなことが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_4184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_41ED")

    #C0180
    ChrTalk(
        0xFE,
        (
            "マインツの事件……\x01",
            "本当にとんでもない話ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "一刻も早く解決して欲しいです……\x02",
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_41ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_42A5")

    #C0182
    ChrTalk(
        0xFE,
        (
            "昨日の列車事故では\x01",
            "多くの怪我人が出たそうですが、\x01",
            "幸い死者は出なかったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "でも中にはかなり\x01",
            "重傷の方もいたとか……\x01",
            "とにかく、早く良くなって欲しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_42A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4306")

    #C0184
    ChrTalk(
        0xFE,
        (
            "列車の事故だなんて……\x01",
            "本当に恐ろしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        "……乗客の方々が心配です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_4306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438C")

    #C0186
    ChrTalk(
        0xFE,
        "さてと、今日も頑張ってお仕事です。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "あっと、お客様への笑顔も\x01",
            "忘れないようにしませんと。（ニコリ）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_440F")

    label("loc_438C")


    #C0188
    ChrTalk(
        0xFE,
        (
            "誰かのために汗を掻くのって\x01",
            "本当に気持ち良いですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "何ていうか、\x01",
            "自分って必要とされてるんだな、\x01",
            "って実感できるんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_440F")

    Jump("loc_486F")

    label("loc_4414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44B8")

    #C0190
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの\x01",
            "リニューアル公演の日が\x01",
            "いよいよ近づいて来ましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "流石にチケットは\x01",
            "取れませんでしたけど、\x01",
            "どんな舞台になるか楽しみです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_44B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4580")

    #C0192
    ChrTalk(
        0xFE,
        (
            "お客様、タイムズ百貨店の\x01",
            "屋上へはもう行かれましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "何でもオルキスタワーを観る\x01",
            "絶景スポットだそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "もしまだでしたら、\x01",
            "行ってみてはいかがでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45FF")

    label("loc_4580")


    #C0195
    ChrTalk(
        0xFE,
        (
            "タイムズ百貨店の屋上は\x01",
            "オルキスタワーを観る\x01",
            "絶景スポットだそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "お客様もぜひ、\x01",
            "行ってみてはいかがでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45FF")

    Jump("loc_486F")

    label("loc_4604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_46BE")

    #C0197
    ChrTalk(
        0xFE,
        (
            "ＶＩＰの方々は除幕式の後、\x01",
            "それぞれ色々な場所を\x01",
            "ご訪問されるご予定だそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "どこかで拝見できたりすると\x01",
            "嬉しいんですけど……\x01",
            "ガードが固いから難しいですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_46BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_474C")

    #C0199
    ChrTalk(
        0xFE,
        (
            "最近アーロンさんに叱られることが\x01",
            "少なくなって来たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "私、成長してるんでしょうか？\x01",
            "ふふ、だとしたら嬉しいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_474C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47F8")

    #C0201
    ChrTalk(
        0xFE,
        (
            "雨の日はどうしても\x01",
            "泥汚れが付いてしまうので、\x01",
            "カーペット掃除が大変なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "でも綺麗になって行く所が\x01",
            "目に見えるのって、\x01",
            "けっこう快感なんですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_47F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_486F")

    #C0203
    ChrTalk(
        0xFE,
        (
            "おはようございます。\x01",
            "ご宿泊のお客様でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "外出の際は、お部屋の鍵を\x01",
            "忘れずにお掛けくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486F")

    TalkEnd(0xFE)
    Return()

    # Function_15_3E46 end

    def Function_16_4873(): pass

    label("Function_16_4873")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48FC")

    #C0205
    ChrTalk(
        0xFE,
        "ふむ、今日は何をして過ごそうか。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "支配人の言う通り、ホテルの\x01",
            "サービスを味わい尽くすというのも\x01",
            "案外いいかもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4981")

    label("loc_48FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4981")

    #C0207
    ChrTalk(
        0xFE,
        (
            "このホテル、部屋はもちろん\x01",
            "サービスも一流だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "ふむ、今後もクロスベル旅行の際は\x01",
            "ぜひここを利用するようにしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4981")

    TalkEnd(0xFE)
    Return()

    # Function_16_4873 end

    def Function_17_4985(): pass

    label("Function_17_4985")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4A00")

    #C0209
    ChrTalk(
        0xFE,
        (
            "ふふ、確かにホテルで\x01",
            "過ごすのも悪くなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "私としては、カジノに\x01",
            "入り浸りたいところだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A90")

    label("loc_4A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4A90")

    #C0211
    ChrTalk(
        0xFE,
        (
            "ふふ、今回は導力鉄道で\x01",
            "来たのだけど、移動の疲れが\x01",
            "すっかり取れたわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "少し値段は張るけど、\x01",
            "値段以上の価値があるのは確かね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A90")

    TalkEnd(0xFE)
    Return()

    # Function_17_4985 end

    def Function_18_4A94(): pass

    label("Function_18_4A94")

    TalkBegin(0xFE)

    #C0213
    ChrTalk(
        0xFE,
        (
            "僕と妹は家に帰ってる途中、\x01",
            "突然モヤに巻き込まれて\x01",
            "このホテルに避難してきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "……ホント、\x01",
            "命からがらって気分だったよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4A94 end

    def Function_19_4B20(): pass

    label("Function_19_4B20")

    TalkBegin(0xFE)

    #C0215
    ChrTalk(
        0xFE,
        (
            "お兄ちゃん、モヤが出た時\x01",
            "私のことをおんぶして\x01",
            "走り回ってくれたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "えへへ、かっこよかったな㈱\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_4B20 end

    def Function_20_4B93(): pass

    label("Function_20_4B93")

    TalkBegin(0xFE)

    #C0217
    ChrTalk(
        0xFE,
        "今頃みんな心配してるだろうな……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4B93 end

    def Function_21_4BC0(): pass

    label("Function_21_4BC0")

    TalkBegin(0xFE)

    #C0218
    ChrTalk(
        0xFE,
        "早くお家に帰りたいわ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4BC0 end

    def Function_22_4BE5(): pass

    label("Function_22_4BE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CCA")

    #C0219
    ChrTalk(
        0xFE,
        (
            "街を守っていた結界は\x01",
            "一体どこへ行ったんだ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "それに、あの気味の悪い\x01",
            "化物は一体なんなんだ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "大統領演説の日に故郷#4Rく　に#に\x01",
            "帰り損ねただけでこの仕打ち……\x01",
            "もういい加減にしてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D2E")

    label("loc_4CCA")


    #C0222
    ChrTalk(
        0xFE,
        (
            "大統領演説の日に故郷#4Rく　に#に\x01",
            "帰り損ねただけでこの仕打ち……\x01",
            "もういい加減にしてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D2E")

    TalkEnd(0xFE)
    Return()

    # Function_22_4BE5 end

    def Function_23_4D32(): pass

    label("Function_23_4D32")

    TalkBegin(0xFE)

    #C0223
    ChrTalk(
        0xFE,
        (
            "こんな状況になると\x01",
            "分かっていれば、すぐに\x01",
            "家に帰っていたんだがなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "まあただ、こんないい部屋に\x01",
            "無償で通してくれたことは\x01",
            "すごくラッキーだったけどね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_4D32 end

    def Function_24_4DDB(): pass

    label("Function_24_4DDB")

    TalkBegin(0xFE)

    #C0225
    ChrTalk(
        0xFE,
        (
            "ホテルに避難できたのは\x01",
            "ほんと不幸中の幸いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "でもこの状況……\x01",
            "一体いつまで続くのかしら？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4DDB end

    def Function_25_4E46(): pass

    label("Function_25_4E46")

    TalkBegin(0xFE)

    #C0227
    ChrTalk(
        0xFE,
        "えへへ、このお部屋おっきーね♪\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_4E46 end

    def Function_26_4E71(): pass

    label("Function_26_4E71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 6)), scpexpr(EXPR_END)), "loc_4EA2")
    Call(0, 29)
    Jump("loc_4EA5")

    label("loc_4EA2")

    Call(0, 28)

    label("loc_4EA5")

    Return()

    # Function_26_4E71 end

    def Function_27_4EA6(): pass

    label("Function_27_4EA6")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_27_4EA6 end

    def Function_28_4ED8(): pass

    label("Function_28_4ED8")

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
            "──ええ、それではまた明日。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x17,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今後ともよろしくお願いします。\x02",
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

    def lambda_50CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_50CD)

    def lambda_50DE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF79A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_50DE)
    WaitChrThread(0x17, 1)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sound(104, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0231
    ChrTalk(
        0x17,
        "おや……あんたたちは。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00000Fえっと、すみません。\x02\x03",

            "アルモリカ村の\x01",
            "デリックさんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x17,
        (
            "ああ、その通りだが……\x01",
            "俺に何か用なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#00000F申し遅れました……\x01",
            "警察の特務支援課の者です。\x02\x03",

            "少し話をお聞かせ願えませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x17)

    #C0235
    ChrTalk(
        0x17,
        "……なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x17,
        (
            "あんたたちは村長……\x01",
            "親父の差し金だな？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x17,
        (
            "警察まで呼ぶなんて……\x01",
            "フン、ご苦労なことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        "#00105Fえ、えっとあの……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x17,
        (
            "……大体見当はついてる。\x01",
            "俺の最近の行動を\x01",
            "洗おうって言うんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x17,
        (
            "別に後ろ暗いことを\x01",
            "しているわけじゃないんだ、\x01",
            "なんでも聞いてみろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x105,
        "#10303F（ふむ……意外な反応だね。）\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00003F……では、単刀直入に聞きます。\x02\x03",

            "#00001Fここ数日、あなたは\x01",
            "ミンネスさんという方と\x01",
            "付き合いがあるそうですが……\x02\x03",

            "一体、どういう目的が？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x17,
        (
            "……まあ、いいだろう。\x01",
            "いまさら知ったところで\x01",
            "親父にはどうにもできまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x17,
        (
            "少し前から、ミンネスさんには\x01",
            "あることについて世話になっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x17,
        "主に、村の改革についてな。\x02",
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
        "#10105Fむ、村の改革ですか……？\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00005Fそ、そんな大事なことを\x01",
            "村長さんに黙って\x01",
            "進めているんですか？\x02\x03",

            "#00006Fいくらなんでも、\x01",
            "それはよくないような……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x17,
        (
            "村長……親父には\x01",
            "今まで何度も話したさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x17,
        (
            "だが、返す言葉は決まって\x01",
            "『あるべき姿を見失うな』だの\x01",
            "『急激な変化はよくない』だの……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x17,
        (
            "だが、現状を維持しても\x01",
            "あんな田舎の村に\x01",
            "未来があるとは思えない。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x17,
        (
            "村を存続させるには、\x01",
            "改革が絶対に必要なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x17,
        (
            "親父はそこのところを、\x01",
            "分かってないんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#00203Fなるほど……\x01",
            "そんな中、そのミンネスという\x01",
            "人物に出会ったわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x17,
        (
            "……彼は、親父と違って\x01",
            "俺の相談に乗ってくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x17,
        (
            "そして、アルモリカ村の\x01",
            "養蜂業に大きな可能性を\x01",
            "見出してくれたらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x17,
        (
            "近々、彼と協力して\x01",
            "大きな事業を立ち上げる\x01",
            "計画もあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        (
            "#00306Fな、なんつーか\x01",
            "途方もねえ話だなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x17,
        (
            "フン……\x01",
            "俺が話せるのはこの位だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x17,
        (
            "もういいだろう？\x01",
            "そろそろ村に帰らせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58B1():
        OP_95(0xFE, 74620, 0, 5690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_58B1)
    Sleep(2000)

    def lambda_58CE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58CE)
    Sleep(50)

    def lambda_58DE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58DE)
    Sleep(50)

    def lambda_58EE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58EE)
    Sleep(50)

    def lambda_58FE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58FE)
    Sleep(50)

    def lambda_590E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_590E)
    Sleep(50)

    def lambda_591E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_591E)
    WaitChrThread(0x17, 1)
    SetChrFlags(0x17, 0x80)
    OP_0D()

    #C0260
    ChrTalk(
        0x102,
        "#00105Fあっ……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        "#10106F行ってしまいましたね……\x02",
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
            "#00003Fとにかく……\x01",
            "折角ここまできたんだ。\x02\x03",

            "#00000Fここは一つ、\x01",
            "ミンネスという男に、\x01",
            "直接会ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A07():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A07)
    Sleep(50)

    def lambda_5A17():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A17)
    Sleep(50)

    def lambda_5A27():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A27)
    Sleep(50)

    def lambda_5A37():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A37)
    Sleep(50)

    def lambda_5A47():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A47)

    #C0263
    ChrTalk(
        0x104,
        (
            "#00303Fなるほど……\x01",
            "色々と分かるかも知れねえな。\x02\x03",

            "#00300Fよっしゃ、そんじゃ\x01",
            "早速突入してみるとするか。\x02",
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

    # Function_28_4ED8 end

    def Function_29_5B19(): pass

    label("Function_29_5B19")

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
            "#00001Fそれじゃあ……\x01",
            "早速入ってみるぞ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)
    Sound(808, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("中年の声")

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おや……\x01",
            "どちらさまですかな？\x02\x03",

            "ルームサービスを\x01",
            "頼んだ覚えはありませぬが……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00000Fミンネスさん……ですね？\x02\x03",

            "#00004F突然すみません、\x01",
            "クロスベル警察・\x01",
            "特務支援課の者です。\x02\x03",

            "#00000F２、３、お聞きしたいことが\x01",
            "あるのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年の声")

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おやおや、\x01",
            "警察の方がわざわざ……\x02\x03",

            "そういうことなら\x01",
            "どうぞ、お入りください。\x01",
            "鍵は開いておりますゆえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        (
            "#00305F（な、なんだかえらくあっさり\x01",
            "  入れてくれるんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#00003F（俺たちが考えている以上の\x01",
            "  やり手なのかもしれないな……）\x02\x03",

            "#00005Fえっと……\x01",
            "それでは、失礼します。\x02",
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
            "#11Pお初にお目にかかります。\x01",
            "私がミンネスにございますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xC,
        (
            "#11P本日はどういった\x01",
            "ご用件でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#00003F先ほども言った通り……\x01",
            "いくつか質問をさせて\x01",
            "いただこうと思います。\x02\x03",

            "#00001Fご協力いただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xC,
        (
            "#11Pもちろんですとも。\x01",
            "私に協力できることなら何なりと……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "#11Pなにか、この辺りで\x01",
            "事件でも起こりましたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        (
            "#00003Fいえ……\x01",
            "聞きたいことというのは\x01",
            "あなたについてです。\x02\x03",

            "あなたがどういった人物なのか、\x01",
            "アルモリカ村でなにをしようと\x01",
            "しているのか……\x02\x03",

            "#00001F一通り、お聞かせ願いたいのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        "#11Pほう……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0277
    ChrTalk(
        0xC,
        (
            "#11Pまあいいでしょう。\x01",
            "それくらいは詮無きことです。\x02",
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
            "#11Pコホン……私はある会社で役員を\x01",
            "させてもらっている者でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "#11P仕事内容は、商品開発から\x01",
            "営業まで幅広くしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        (
            "#11Pアルモリカ村へは、わが社……\x01",
            "『クインシー社』の重要な取引きのため\x01",
            "訪問させていただいた次第です。\x02",
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
            "#00105Fえ……ええっ！\x01",
            "あのクインシー社ですか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6361():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6361)
    Sleep(50)

    def lambda_6371():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6371)
    Sleep(50)

    def lambda_6381():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6381)
    Sleep(50)

    def lambda_6391():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6391)
    Sleep(300)

    #C0282
    ChrTalk(
        0x104,
        (
            "#00305F初めて聞く名前だが……\x01",
            "お嬢は知ってるのかよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x102,
        (
            "#00105Fえっと……クインシー社というのは、\x01",
            "外国の有名なお菓子メーカーなの。\x02\x03",

            "#00104F製菓業界でもかなりの大企業で、\x01",
            "確か、クロスベルにも\x01",
            "商品が輸入されてたと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00005Fああ、そういえば子供の頃、\x01",
            "そんなメーカーのチョコレートを\x01",
            "よく買って食べてたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#00303Fうーん、メーカーなんぞ\x01",
            "あまり意識して見ないからなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "#11Pふふ、それもまた\x01",
            "仕方のないことでありましょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_656C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_656C)
    Sleep(50)

    def lambda_657C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_657C)
    Sleep(50)

    def lambda_658C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_658C)
    Sleep(50)

    def lambda_659C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_659C)
    Sleep(50)

    def lambda_65AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65AC)
    Sleep(300)

    #C0287
    ChrTalk(
        0xC,
        (
            "#11P私自身、この立場にはいますが\x01",
            "甘い物は苦手でしてねぇ。\x01",
            "昔は本当に疎いものでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        (
            "#11P長年営業方面で活躍したおかげで\x01",
            "力を認められ、今の地位に\x01",
            "つかせてもらったわけですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        (
            "#11P……おっと、\x01",
            "話が逸れてしまいましたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#00005Fあ……い、いえ。\x01",
            "こちらこそ失礼しました。\x02\x03",

            "#00003F……コホン。\x01",
            "先ほど、アルモリカ村で\x01",
            "『取引き』と仰いましたね。\x02\x03",

            "#00001Fその『取引き』とは……\x01",
            "村長の息子、デリックさんに\x01",
            "関係のあることなんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#00100F何でも、村の発展に\x01",
            "関係のあることのようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "#11Pおや……\x01",
            "そこまで知っておいででしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xC,
        (
            "#11Pふむ、デリックさん自ら\x01",
            "情報を解禁したというのなら、\x01",
            "隠す意味はありませんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xC,
        (
            "#11Pふふ、彼とは友好的な関係を\x01",
            "築かせていただいております。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x103,
        "#00203Fやはり……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#00001F詳しく聞かせていただけますか？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        "#11Pふふ、いいでしょう。\x02",
    )

    CloseMessageWindow()
    OP_68(167980, 1500, 3640, 3000)

    def lambda_68F2():
        OP_95(0xFE, 164960, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_68F2)
    Sleep(500)

    def lambda_690F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_690F)
    Sleep(50)

    def lambda_691F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_691F)
    Sleep(50)

    def lambda_692F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_692F)
    Sleep(50)

    def lambda_693F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_693F)
    Sleep(50)

    def lambda_694F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_694F)
    Sleep(50)

    def lambda_695F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_695F)
    WaitChrThread(0xC, 1)
    OP_6F(0x1)

    #C0298
    ChrTalk(
        0xC,
        (
            "#5P我がクインシー社は、\x01",
            "製菓業界の未来の為、\x01",
            "日々、研鑽を重ねています。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        (
            "#5Pそんな中、私は本社より\x01",
            "ある使命を賜って参りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xC,
        (
            "#5Pそれは、このクロスベルへの\x01",
            "クインシー社の進出、\x01",
            "その足がかりを模索することです。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#00105Fつまり……\x01",
            "クインシー社の子会社を\x01",
            "クロスベルに？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xC,
        "#5Pふふ、その通りです。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xC,
        (
            "#5Pそして、手始めに市内の百貨店に\x01",
            "ヒントを探しに行った所で……\x01",
            "私は出会ったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xC,
        (
            "#5Pかのアルモリカ村で作られるという、\x01",
            "大変質のよい『蜂蜜』をね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x109,
        (
            "#10100F蜂蜜……アルモリカの\x01",
            "レンゲ畑で作られるアレですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00003Fハロルドさんもその質は\x01",
            "保証していたっけ……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(169610, 1500, 3430, 3000)

    def lambda_6BD6():
        OP_95(0xFE, 168410, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6BD6)
    Sleep(500)

    def lambda_6BF3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BF3)
    Sleep(50)

    def lambda_6C03():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C03)
    Sleep(50)

    def lambda_6C13():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C13)
    Sleep(50)

    def lambda_6C23():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C23)
    Sleep(50)

    def lambda_6C33():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C33)
    Sleep(50)

    def lambda_6C43():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C43)
    WaitChrThread(0xC, 1)

    def lambda_6C54():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6C54)
    OP_6F(0x1)
    Sleep(300)

    #C0307
    ChrTalk(
        0xC,
        (
            "#11P豊かな自然のもと\x01",
            "代々受け継がれてきた\x01",
            "レンゲ畑によって生まれる蜂蜜。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "#11Pそれを見たとき、天啓の如く\x01",
            "新たな製菓ブランドを立ち上げる\x01",
            "一つの計画が生まれたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "#11Pその計画名こそ……\x01",
            "『アルモリカ・ハニーカンパニー』。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        "#10105Fアルモリカ・ハニーカンパニー……\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x104,
        "#00306Fな、なにやら凄そうな響きだな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0312
    ChrTalk(
        0xC,
        (
            "#11Pつまりは、アルモリカ村の蜂蜜を\x01",
            "ふんだんに使用したお菓子を\x01",
            "提供していくわけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xC,
        (
            "#11Pしかし、そのためには現地の、\x01",
            "アルモリカ村の方々の協力が\x01",
            "必要不可欠でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xC,
        (
            "#11Pそこで私は、アルモリカ村の\x01",
            "次期村長であるデリックさんに、\x01",
            "この話を持ちかけたのでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "#11P製菓工場の建造、そして\x01",
            "この新会社の経営をしてみないか、とね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00005Fデリックさんに\x01",
            "クインシー社の子会社を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        (
            "#11P無論、そのノウハウや販売ラインは\x01",
            "我が社で用意し、以降、レンゲ畑は\x01",
            "こちらのスタッフで管理する……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xC,
        (
            "#11P一切のお手を煩わせない、\x01",
            "そして村人たちの苦労を減らすという\x01",
            "条件を提示させていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        (
            "#00105Fでも、工場なんて……\x01",
            "いったいどこに建設する\x01",
            "おつもりなのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        (
            "#11Pそれに関しては今までの取引きで、\x01",
            "村の私有地を貸していただけることに\x01",
            "相成りましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "#11Pもともと物置程度にしか\x01",
            "使っておられなかったそうなので、\x01",
            "快諾していただきました次第です。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x105,
        (
            "#10304F確かにその条件なら、\x01",
            "話に乗ってくれる可能性は\x01",
            "かなり高いだろうね。\x02\x03",

            "村の改革を願うデリック君ならば\x01",
            "なおさら……\x02\x03",

            "#10302Fまさにあなたにとっても、\x01",
            "デリック君にとっても\x01",
            "悪い話じゃなかったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xC,
        "#11Pフフ、その通り。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xC,
        (
            "#11P実際、彼の才能と強い責任感は\x01",
            "それに値するものと感じましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "#11P……ふふ、私の話はこんなところです。\x01",
            "ご理解いただけましたかな？\x02",
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
            "#00003F……お話を聞かせていただき\x01",
            "ありがとうございます。\x02\x03",

            "#00000Fおかげさまで色々と\x01",
            "分からなかった部分に\x01",
            "答えが見出せそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        "#11Pおや、もう話はいいのですかな？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#00000Fええ、お時間をとらせて\x01",
            "申し訳ありませんでした。\x02\x03",

            "自分たちはこれで\x01",
            "失礼させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xC,
        (
            "#11Pいえいえ、何のこれしき。\x01",
            "またいつでも\x01",
            "いらっしゃってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "#11Pどうかお気をつけて\x01",
            "帰られますよう。\x02",
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
            "#00106Fふう……\x01",
            "なんていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、なんだか凄い話を\x01",
            "聞かされてしまったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        (
            "#00203Fあのミンネスという男……\x01",
            "予想以上の凄腕だったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x104,
        (
            "#00306F話は小難しかったが、\x01",
            "確かに儲かりそうな話だったし……\x02\x03",

            "#00301Fしかし、ありゃあ……\x02",
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
            "#10101F……でも、これで一通りの情報は\x01",
            "手に入れられましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#00003Fああ……\x01",
            "一旦アルモリカ村に戻ろう。\x02\x03",

            "#00001Fトルタ村長に報告しなきゃな。\x02",
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

    # Function_29_5B19 end

    def Function_30_7861(): pass

    label("Function_30_7861")


    def lambda_7866():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7866)

    def lambda_7877():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7877)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 167730, 0, 2860, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_30_7861 end

    def Function_31_78AC(): pass

    label("Function_31_78AC")


    def lambda_78B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_78B1)

    def lambda_78C2():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_78C2)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 169150, 0, 2870, 2000, 0x0)
    Return()

    # Function_31_78AC end

    def Function_32_78F0(): pass

    label("Function_32_78F0")


    def lambda_78F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_78F5)

    def lambda_7906():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7906)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 170230, 0, 1900, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_32_78F0 end

    def Function_33_793B(): pass

    label("Function_33_793B")


    def lambda_7940():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7940)

    def lambda_7951():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7951)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 167400, 0, 1860, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_33_793B end

    def Function_34_7986(): pass

    label("Function_34_7986")


    def lambda_798B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_798B)

    def lambda_799C():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_799C)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 168250, 0, 1200, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_34_7986 end

    def Function_35_79D1(): pass

    label("Function_35_79D1")


    def lambda_79D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_79D6)

    def lambda_79E7():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_79E7)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 169670, 0, 1220, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_35_79D1 end

    def Function_36_7A1C(): pass

    label("Function_36_7A1C")


    def lambda_7A21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A21)

    def lambda_7A32():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A32)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 68440, 0, 10210, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_36_7A1C end

    def Function_37_7A67(): pass

    label("Function_37_7A67")


    def lambda_7A6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A6C)

    def lambda_7A7D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A7D)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 67120, 0, 8910, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_37_7A67 end

    def Function_38_7AB2(): pass

    label("Function_38_7AB2")


    def lambda_7AB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7AB7)

    def lambda_7AC8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7AC8)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 70510, 0, 9150, 2000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_38_7AB2 end

    def Function_39_7AFD(): pass

    label("Function_39_7AFD")


    def lambda_7B02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7B02)

    def lambda_7B13():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7B13)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 67540, 0, 7130, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_39_7AFD end

    def Function_40_7B48(): pass

    label("Function_40_7B48")


    def lambda_7B4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7B4D)

    def lambda_7B5E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B5E)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 69250, 0, 6220, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_40_7B48 end

    def Function_41_7B93(): pass

    label("Function_41_7B93")


    def lambda_7B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7B98)

    def lambda_7BA9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BA9)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 70730, 0, 7540, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_41_7B93 end

    def Function_42_7BDE(): pass

    label("Function_42_7BDE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D75")

    #C0337
    ChrTalk(
        0x9,
        "さて、お掃除お掃除っと……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00003F（彼女なら『メイド』枠で\x01",
            "  ミスコンに出場できそうだな。）\x02\x03",

            "#00000Fあの、すみません。\x01",
            "ちょっと相談なのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0339
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

    #C0340
    ChrTalk(
        0x9,
        "ミ、ミスコン……ですか？\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x9,
        (
            "あ、あの、すみません……\x01",
            "お気持ちはうれしいのですが\x01",
            "仕事を抜けられないもので……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#00003Fそうですか……\x01",
            "いえ、失礼しました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 7)
    Jump("loc_7DD9")

    label("loc_7D75")


    #C0343
    ChrTalk(
        0x9,
        (
            "ミスコンへのお誘いは\x01",
            "ちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x9,
        (
            "お気持ちはうれしいのですが\x01",
            "仕事を抜けられないもので……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD9")

    TalkEnd(0x9)
    Return()

    # Function_42_7BDE end

    SaveToFile()

Try(main)
