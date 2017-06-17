from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1010.bin",                # FileName
        "c1010",                    # MapName
        "c1010",                    # Location
        0x0013,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1010",                  # 0
        "受付ミシェル",           # 1
        "遊撃士スコット",         # 2
        "遊撃士ヴェンツェル",     # 3
        "遊撃士リン",             # 4
        "遊撃士エオリア",         # 5
        "キーア",                 # 6
        "シズク",                 # 7
        "ツァイト",               # 8
        "アリオス",               # 9
        "キリカ",                 # 10
        "イス",                   # 11
        "イス",                   # 12
        "イス",                   # 13
        "イス",                   # 14
        "イス",                   # 15
        "イス",                   # 16
        "イス",                   # 17
        "イス",                   # 18
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch27200.itc",                   # 01
        "chr/ch27300.itc",                   # 02
        "chr/ch32000.itc",                   # 03
        "chr/ch32100.itc",                   # 04
        "chr/ch08202.itc",                   # 05
        "chr/ch08702.itc",                   # 06
        "chr/ch27202.itc",                   # 07
        "chr/ch27302.itc",                   # 08
        "chr/ch32102.itc",                   # 09
        "chr/ch02708.itc",                   # 0A
        "chr/ch08200.itc",                   # 0B
        "chr/ch08700.itc",                   # 0C
        "chr/ch02400.itc",                   # 0D
        "chr/ch07300.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
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

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-500,    0,       43900,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-500,    0,       45099,   180,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   13,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(114040,  0,       5860,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)
    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  14, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  15, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  15, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  15, 0x0000)

    ChipFrameInfo(1096, 0)                                       # 0

    ScpFunction((
        "Function_0_448",          # 00, 0
        "Function_1_4F8",          # 01, 1
        "Function_2_8EC",          # 02, 2
        "Function_3_98F",          # 03, 3
        "Function_4_993",          # 04, 4
        "Function_5_4645",         # 05, 5
        "Function_6_4E3E",         # 06, 6
        "Function_7_5141",         # 07, 7
        "Function_8_52B0",         # 08, 8
        "Function_9_5B31",         # 09, 9
        "Function_10_61AE",        # 0A, 10
        "Function_11_69D7",        # 0B, 11
        "Function_12_6F24",        # 0C, 12
        "Function_13_6F9D",        # 0D, 13
        "Function_14_708F",        # 0E, 14
        "Function_15_7DC4",        # 0F, 15
        "Function_16_7E97",        # 10, 16
        "Function_17_8334",        # 11, 17
        "Function_18_851E",        # 12, 18
        "Function_19_87E0",        # 13, 19
        "Function_20_87E7",        # 14, 20
        "Function_21_91E6",        # 15, 21
        "Function_22_95F9",        # 16, 22
        "Function_23_9F62",        # 17, 23
        "Function_24_A84A",        # 18, 24
        "Function_25_B4FD",        # 19, 25
        "Function_26_BA2B",        # 1A, 26
        "Function_27_BA75",        # 1B, 27
        "Function_28_D6CB",        # 1C, 28
        "Function_29_E16C",        # 1D, 29
        "Function_30_E8D6",        # 1E, 30
        "Function_31_10F5F",       # 1F, 31
        "Function_32_111D0",       # 20, 32
        "Function_33_128C4",       # 21, 33
        "Function_34_13558",       # 22, 34
        "Function_35_1403C",       # 23, 35
    ))


    def Function_0_448(): pass

    label("Function_0_448")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_480"),
        (1, "loc_48C"),
        (2, "loc_498"),
        (3, "loc_4A4"),
        (4, "loc_4B0"),
        (5, "loc_4BC"),
        (6, "loc_4C8"),
        (SWITCH_DEFAULT, "loc_4D4"),
    )


    label("loc_480")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_48C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_498")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4F7")

    Return()

    # Function_0_448 end

    def Function_1_4F8(): pass

    label("Function_1_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_546")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -540, 0, 43820, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -540, 0, 45260, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x11, 0x10)

    label("loc_541")

    Jump("loc_86B")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B9")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2760, 0, 10330, 315)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1800, 0, 10320, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -960, 0, 10340, 45)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1960, 0, 10340, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B4")
    Event(0, 24)

    label("loc_5B4")

    Jump("loc_86B")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_64E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 2220, 0, 4610, 90)
    SetChrPos(0xA, 3840, 0, 4540, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD")
    SetChrFlags(0xB, 0x10)

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60C")
    SetChrFlags(0xA, 0x10)

    label("loc_60C")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -6000, 150, 43030, 180)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -5030, 0, 52190, 0)
    Jump("loc_86B")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65C")
    Jump("loc_86B")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6C7")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 2760, 0, 10330, 315)
    SetChrPos(0xC, 1800, 0, 10320, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 600, 0, 39580, 90)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1400, 0, 40910, 135)
    Jump("loc_86B")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D5")
    Jump("loc_86B")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6E3")
    Jump("loc_86B")

    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F1")
    Jump("loc_86B")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6FF")
    Jump("loc_86B")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_73E")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -5030, 0, 52190, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 600, 0, 39580, 90)
    SetChrFlags(0xA, 0x10)
    Jump("loc_86B")

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_785")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1000, 0, 10310, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_785")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_785")

    Jump("loc_86B")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B1")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_7B1")

    Jump("loc_86B")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_829")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -6000, 150, 43030, 180)
    SetChrPos(0x9, -6000, 150, 40820, 0)
    SetChrChipByIndex(0xA, 0x8)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_824")
    Event(0, 20)

    label("loc_824")

    Jump("loc_86B")

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_86B")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, -540, 0, 45260, 180)
    SetChrPos(0xC, -540, 0, 43420, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B")
    Event(0, 20)

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_87F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)
    Jump("loc_8A8")

    label("loc_87F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_899")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 29)
    Jump("loc_8A8")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_8A8")
    ClearScenarioFlags(0x22, 2)
    Event(0, 31)

    label("loc_8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B9")
    Event(0, 30)

    label("loc_8B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EB")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_8EB")

    Return()

    # Function_1_4F8 end

    def Function_2_8EC(): pass

    label("Function_2_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_901")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)

    label("loc_901")

    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_936")
    OP_24(0x80)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_967")

    label("loc_936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_967")
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98E")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)

    label("loc_98E")

    Return()

    # Function_2_8EC end

    def Function_3_98F(): pass

    label("Function_3_98F")

    Call(0, 4)
    Return()

    # Function_3_98F end

    def Function_4_993(): pass

    label("Function_4_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AA")
    Call(0, 25)
    Return()

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BC")
    Call(0, 28)
    Return()

    label("loc_9BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DD")
    Jump("loc_AEE")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F0")
    Jump("loc_AEE")

    label("loc_9F0")

    TalkBegin(0x8)

    #C0001
    ChrTalk(
        0x8,
        (
            "#04000Fそうそう、実はこの間から\x01",
            "『ポムっと！』って導力ゲームを\x01",
            "始めたところなのよね。\x02\x03",

            "#04011Fあなたたちもやってるんでしょ？\x01",
            "フフ、ヒマができたら\x01",
            "アタシとも対戦しましょ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ミシェルのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 5)
    OP_E4(0x3)
    TalkEnd(0x8)
    Return()

    label("loc_AEE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D95")

    #C0003
    ChrTalk(
        0x8,
        "#04001Fそう……アリオスを倒したのね。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00008F……はい、何とか。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00306Fさすがにトンでもねえ\x01",
            "強さだったけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#04003F……アリオスは“理”に通じる\x01",
            "正真正銘の達人よ。\x02\x03",

            "それも、単なる才能だけでは\x01",
            "決して辿り着けない……\x01",
            "並々ならぬ鍛錬があればこその強さ。\x02\x03",

            "#04011Fフフ、それを乗り越えてしまうなんて\x01",
            "あなたたちも強くなったじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#00204F正直、運もあったとは思います。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#00100F厳しい戦いでしたけど……\x01",
            "ようやく乗り越える事が出来ました。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#04004Fフフ、それじゃああとは\x01",
            "あのキーアってコだけね。\x02\x03",

            "#04000F待っているシズクちゃんのためにも、\x01",
            "アリオスと一緒に何としても\x01",
            "連れ帰ってきてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00000Fええ、必ず……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 6)
    Jump("loc_F2D")

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E94")

    #C0011
    ChrTalk(
        0x8,
        (
            "#04003Fアリオスは“理”に通じる\x01",
            "正真正銘の達人よ。\x02\x03",

            "#04011Fフフ、それを乗り越えてしまうなんて\x01",
            "あなたたちも強くなったじゃない。\x02\x03",

            "#04000F待っているシズクちゃんのためにも、\x01",
            "あのキーアってコと一緒に\x01",
            "何としても連れ帰ってきてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F2D")

    label("loc_E94")


    #C0012
    ChrTalk(
        0x8,
        (
            "#04004Fフフ、あとはキーアってコを\x01",
            "取り戻すだけね。\x02\x03",

            "#04000F待っているシズクちゃんのためにも、\x01",
            "アリオスと一緒に何としても\x01",
            "連れ帰ってきてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2D")

    Jump("loc_4641")

    label("loc_F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_165F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1443")

    #C0013
    ChrTalk(
        0x8,
        (
            "#04000Fあなたたち……\x01",
            "大統領の拘束、お疲れだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000Fギルドの皆さんも、\x01",
            "ご協力ありがとうございました。\x02\x03",

            "皆さんの協力が無くては、\x01",
            "決して成し遂げられなかったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#04011Fウフフ、いいって事よ。\x02\x03",

            "#04004F街の状況を何とかしたかった\x01",
            "アタシたちにとっても、\x01",
            "渡りに船だったんだから。\x02\x03",

            "#04000Fおかげでギルドの活動も\x01",
            "再開出来るようになったしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#00105Fそういえば、ギルドの皆さんは……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#04000Fええ、結界が解除されたから\x01",
            "手分けして市外に行っているわ。\x02\x03",

            "#04003Fしばらく街から出られなかったから\x01",
            "各所で問題が起こってるらしくて、\x01",
            "依頼が一気に押し寄せたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        "#00200Fそれは……大変そうですね。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#00303F俺たちも手伝えれば\x01",
            "良かったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#04004Fまあ、こちらは任せておきなさい。\x02\x03",

            "#04001F代わりに、湿地帯に現れた\x01",
            "得体の知れない《大樹》……\x01",
            "あれはあなた達に任せるわ。\x02\x03",

            "アナタたちの今の役割は、\x01",
            "まさにそれなんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003Fええ……そうですね。\x02\x03",

            "あそこにはキーア……\x01",
            "そしてアリオスさんもいます。\x02\x03",

            "#00001F俺たちの手で、何としても\x01",
            "連れ帰ってみせる……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1353")

    #C0022
    ChrTalk(
        0x10A,
        "#00603F……当然だ。\x02",
    )

    CloseMessageWindow()

    label("loc_1353")


    #C0023
    ChrTalk(
        0x8,
        (
            "#04004Fウフフ、それでこそアナタたちね。\x02\x03",

            "#04001F……アリオスの力は、正直言って\x01",
            "ケタ違いと言っていいと思う。\x02\x03",

            "それは一緒に仕事していた\x01",
            "アタシたちが一番よく分かってるわ。\x02\x03",

            "#04011F気張りなさいよ、特務支援課！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00001Fはい！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 5)
    Jump("loc_165A")

    label("loc_1443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1593")

    #C0025
    ChrTalk(
        0x8,
        (
            "#04003F……アリオスの力は、正直言って\x01",
            "ケタ違いと言っていいと思う。\x02\x03",

            "#04001Fそれは一緒に仕事していた\x01",
            "アタシたちが一番よく分かってるわ。\x02\x03",

            "厳しい戦いが待っているハズだけど、\x01",
            "あのキーアってコと一緒に、\x01",
            "何としても連れ帰ってきてちょうだい。\x02\x03",

            "#04011Fフフ、自分勝手に辞表なんか出した\x01",
            "バツとして、お説教してあげなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_165A")

    label("loc_1593")


    #C0026
    ChrTalk(
        0x8,
        (
            "#04003F厳しい戦いが待っているハズだけど、\x01",
            "あのキーアってコと一緒に、アリオスを\x01",
            "何としても連れ帰ってきてちょうだい。\x02\x03",

            "#04011Fフフ、自分勝手に辞表なんか出した\x01",
            "バツとして、お説教してあげなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165A")

    Jump("loc_4641")

    label("loc_165F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1851")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D4")

    #C0027
    ChrTalk(
        0x8,
        (
            "#04006F独立宣言以来、アタシたちも\x01",
            "自由に動けなかったのよ。\x02\x03",

            "いくらギルドが中立と言っても、\x01",
            "独立国として成立している秩序を\x01",
            "無視した行動はできないのよね。\x02\x03",

            "#04001Fでも、今回ばかりは違う。\x01",
            "民間人が危険に晒されている以上、\x01",
            "ギルドも放ってはおけないわ。\x02\x03",

            "#04003Fオルキスタワーへの突入と\x01",
            "大統領の逮捕……アタシたちも\x01",
            "改めて、手伝わせてもらうわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_184C")

    label("loc_17D4")


    #C0028
    ChrTalk(
        0x8,
        (
            "#04003F作戦を開始するときは、\x01",
            "改めて連絡をちょうだい。\x02\x03",

            "#04001Fアタシたちもその時までに\x01",
            "しっかり準備しておくから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184C")

    Jump("loc_4641")

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1958")

    #C0029
    ChrTalk(
        0x8,
        (
            "#04006Fフウ、まさかアリオスが\x01",
            "スケジュールを誤魔化してまで\x01",
            "市長……大統領と会ってたなんて。\x02\x03",

            "不自然と思いつつも気づけなかった、\x01",
            "完全にアタシのミスだわ。\x02\x03",

            "#04008Fやっぱりシズクちゃんの事故の件が、\x01",
            "ずっと引っかかっていたのかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F0")

    label("loc_1958")


    #C0030
    ChrTalk(
        0x8,
        (
            "#04003Fともかく……独立宣言を出した以上、\x01",
            "中立の立場であるギルドとしては\x01",
            "今後の対応を考えないといけないわ。\x02\x03",

            "#04008F総本部にも連絡してみないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F0")

    Jump("loc_4641")

    label("loc_19F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_20A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_1C7F")

    #C0031
    ChrTalk(
        0x8,
        (
            "#04005Fああ、アナタたち……\x01",
            "アリオスは見かけたかしら？\x02\x03",

            "#04006Fフウ、まだ帰ってこないのよね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00005Fアリオスさんなら\x01",
            "さっき墓地で会いましたよ。\x02\x03",

            "ミシェルさんが探していたことを\x01",
            "伝えたんですが……\x01",
            "まだ戻ってないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04003Fええ、まだ戻ってないけど……\x01",
            "なるほど、墓地に行ってたのね。\x02\x03",

            "#04000F……まあ、サヤさんのお墓参りに\x01",
            "行くのなんて珍しい事でもないし、\x01",
            "そのうち戻ってくるでしょう。\x02\x03",

            "#04011Fお手数かけてしまったわね。\x01",
            "あとはもう大丈夫だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00012Fそ、そうですか。\x01",
            "それでは、失礼します。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF7")

    label("loc_1C7F")


    #C0035
    ChrTalk(
        0x8,
        (
            "#04005Fああ、アナタたち……\x01",
            "ちょっと聞きたいんだけど。\x02\x03",

            "#04001Fどこかでアリオスを見なかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00005Fえっ……？\x01",
            "アリオスさんなら、さっき\x01",
            "墓地で会いましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#00105F奥様のお墓参りを\x01",
            "していたみたいですけど……\x01",
            "何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#04000Fええ、今後のギルドの対応を\x01",
            "市長と協議するために、\x01",
            "オルキスタワーに行ってたんだけど……\x02\x03",

            "#04006Fアリオスはこの間の襲撃事件の時に\x01",
            "エニグマⅡを壊しちゃってね。\x02\x03",

            "あの事件から何かと忙しくて、\x01",
            "スペアの準備も出来てないから、\x01",
            "連絡がとりづらくて困ってるのよ。\x02\x03",

            "#04008Fそろそろ話も終わった頃でしょうし、\x01",
            "いい加減帰ってきて欲しいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00300Fはあ、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#04003Fでも、なるほど……\x01",
            "アリオスは墓地に行ってたのね。\x02\x03",

            "#04000Fまあ、サヤさんのお墓参りに\x01",
            "行くのなんて珍しい事でもないし、\x01",
            "そのうち戻ってくるでしょう。\x02\x03",

            "#04011F呼び止めて悪かったわね。\x01",
            "あとはもう大丈夫だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00012Fそ、そうですか。\x01",
            "それでは、失礼します。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF7")

    SetScenarioFlags(0x18E, 0)
    Jump("loc_20A4")

    label("loc_1FFF")


    #C0042
    ChrTalk(
        0x8,
        (
            "#04008Fクロスベルがこんな状況だから、\x01",
            "湿地帯のプレロマ草や《結社》にも\x01",
            "手を回す余裕がないのよね。\x02\x03",

            "#04006Fはあ、やっぱり総本部に増援を\x01",
            "要請した方がいいかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A4")

    Jump("loc_4641")

    label("loc_20A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238F")

    #C0043
    ChrTalk(
        0x8,
        (
            "#04005Fああ、アナタたち……\x01",
            "ちょっと聞きたいんだけど。\x02\x03",

            "#04001Fどこかでアリオスを見なかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#00005Fいえ、今日は見てませんけど。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00105Fアリオスさんが\x01",
            "どうかしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#04000Fええ、今後のギルドの対応を\x01",
            "市長と協議するために、\x01",
            "オルキスタワーに行ってるんだけど……\x02\x03",

            "#04006Fアリオスはこの間の襲撃事件の時に\x01",
            "エニグマⅡを壊しちゃってね。\x02\x03",

            "あの事件から何かと忙しくて、\x01",
            "スペアの準備も出来てないから、\x01",
            "連絡がとりづらくて困ってるのよ。\x02\x03",

            "#04008Fそろそろ話も終わった頃でしょうし、\x01",
            "いい加減帰ってきて欲しいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#00303Fん～、どっかで寄り道してんのか？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00000F分かりました、\x01",
            "アリオスさんを見かけたら\x01",
            "声をかけておきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#04000Fええ、そうしてくれると助かるわ。\x01",
            "よろしく頼むわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 7)
    Jump("loc_2531")

    label("loc_238F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248C")

    #C0050
    ChrTalk(
        0x8,
        (
            "#04003Fクロスベルがこんな状況だから、\x01",
            "ギルドも今は大忙しなのよね。\x02\x03",

            "#04008F湿地帯に咲き乱れるプレロマ草や、\x01",
            "クロスベルに介入した《結社》にも\x01",
            "手を回す余裕がなくって……\x02\x03",

            "#04006Fはあ、やっぱり総本部に増援を\x01",
            "要請した方がいいかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2531")

    label("loc_248C")


    #C0051
    ChrTalk(
        0x8,
        (
            "#04008Fクロスベルがこんな状況だから、\x01",
            "湿地帯のプレロマ草や《結社》にも\x01",
            "手を回す余裕がないのよね。\x02\x03",

            "#04006Fはあ、やっぱり総本部に増援を\x01",
            "要請した方がいいかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2531")

    Jump("loc_4641")

    label("loc_2536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2555")
    TalkEnd(0x8)
    Call(0, 23)
    Return()

    label("loc_2555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267C")

    #C0052
    ChrTalk(
        0x8,
        (
            "#04001Fこの状況が長く続くなら、\x01",
            "ギルドも動かざるを得なくなるでしょう。\x02\x03",

            "#04003Fでもそれは、以前から警備隊の\x01",
            "治安維持能力を槍玉にあげる２大国に、\x01",
            "更なる攻撃材料を与えてしまうはずよ。\x02\x03",

            "#04001F出来る事なら最後の手段にしたいけど……\x01",
            "民間人の安全を考えたら長くは待てないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2722")

    label("loc_267C")


    #C0053
    ChrTalk(
        0x8,
        (
            "#04001Fこの状況が長く続くなら、\x01",
            "ギルドも動かざるを得なくなるでしょう。\x02\x03",

            "#04006F出来る事なら最後の手段にしたいけど……\x01",
            "民間人の安全を考えたら長くは待てないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2722")

    Jump("loc_4641")

    label("loc_2727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_28AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2811")

    #C0054
    ChrTalk(
        0x8,
        (
            "#04003Fリンにしてもエオリアにしても\x01",
            "Ａ級に迫る凄腕の遊撃士よ。\x02\x03",

            "#04008Fその２人が連絡も入れずに\x01",
            "揃って湿地帯なんかに\x01",
            "足止めされているなんて……\x02\x03",

            "#04001F何があるか判らないわ。\x01",
            "くれぐれも気をつけなさい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28A6")

    label("loc_2811")


    #C0055
    ChrTalk(
        0x8,
        (
            "#04008Fリンとエオリアが連絡も入れずに\x01",
            "揃って湿地帯なんかに\x01",
            "足止めされているなんて……\x02\x03",

            "#04001F何があるか判らないわ。\x01",
            "くれぐれも気をつけなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A6")

    Jump("loc_4641")

    label("loc_28AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_END)), "loc_2A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A03")

    #C0056
    ChrTalk(
        0x8,
        (
            "#04005Fああ、あなたたち……\x01",
            "リンとエオリアの居場所が\x01",
            "わかったのかしら？\x02\x03",

            "エニグマⅡのアラート機能を\x01",
            "利用すると言う話だったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#00200F多少手続きを踏む必要がありますが\x01",
            "なんとかなりそうです。\x02\x03",

            "結果は追ってお伝えしますので、\x01",
            "もう少し待っててください。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#04011Fええ、分かったわ。\x01",
            "よろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A49")

    label("loc_2A03")


    #C0059
    ChrTalk(
        0x8,
        (
            "#04011Fリンとエオリアの居場所、\x01",
            "なんとか見つけ出してちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A49")

    Jump("loc_4641")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AD9")

    #C0060
    ChrTalk(
        0x8,
        (
            "#04003Fリンたちについて、\x01",
            "何か分かったらこちらにも\x01",
            "連絡をちょうだい。\x02\x03",

            "#04001F場合によっては\x01",
            "アリオスたちを呼び戻すわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4641")

    label("loc_2AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C48")

    #C0061
    ChrTalk(
        0x8,
        (
            "#04007Fついさっき連絡が来たけど……\x01",
            "列車事故が起きたんですって！？\x02\x03",

            "#04006Fううん、困ったわね。\x01",
            "アリオスたちは今、幻獣の調査で\x01",
            "すぐには戻ってこれないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00003Fいえ、調査も大事ですし……\x01",
            "こちらは任せてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#04006Fう～……仕方ないわね。\x02\x03",

            "#04000F分かった、脱線事故の方は任せるわ。\x01",
            "何かあったらすぐ知らせてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CD6")

    label("loc_2C48")


    #C0064
    ChrTalk(
        0x8,
        (
            "#04006Fアリオスたちは今、幻獣の調査で\x01",
            "すぐには戻ってこれないわ。\x02\x03",

            "#04000F脱線事故の方は任せるから、\x01",
            "何かあったらすぐ知らせてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD6")

    Jump("loc_4641")

    label("loc_2CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303F")

    #C0065
    ChrTalk(
        0x8,
        (
            "#04003Fアナタ達からの報告書にあった\x01",
            "『プレロマ草』という花……\x01",
            "まさか教会の聖典絡みとはね。\x02\x03",

            "#04001F念のため、スコットやリンたちにも\x01",
            "確認を取ってもらったけど……\x02\x03",

            "今まで幻獣が現れた地点の近くでも、\x01",
            "その蒼い花が咲いていたらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00203F蒼い花が咲く原因自体は\x01",
            "今のところ不明ですけど……\x02\x03",

            "#00200F状況と照らし合わせれば、\x01",
            "幻獣の出現に何らかの因果関係が\x01",
            "あるとみてよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば、ギルドでの調査状況は\x01",
            "どういった感じですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#04011F一応、昨日のうちに出ていた\x01",
            "幻獣３体のうち、２体は退治できたわ。\x02\x03",

            "#04000F今日は残りの幻獣の退治と、\x01",
            "今までの幻獣の出現地点の再調査を\x01",
            "手分けしてやってるってところね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00102Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#00300Fまあ、またいきなり\x01",
            "幻獣が現れないとも限らねえ。\x01",
            "充分注意してくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#04004Fええ、もちろん。\x02\x03",

            "#04000F何か分かったら連絡するから、\x01",
            "引き続きそちらも調査をお願いね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 3)
    Jump("loc_30D1")

    label("loc_303F")


    #C0072
    ChrTalk(
        0x8,
        (
            "#04000F今日はアリオスも復帰してるし、\x01",
            "こちらの調査は任せてちょうだい。\x02\x03",

            "#04011F何か分かったら連絡するから、\x01",
            "引き続きそちらも調査をお願いね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D1")

    Jump("loc_4641")

    label("loc_30D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_332B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32AC")

    #C0073
    ChrTalk(
        0x8,
        (
            "#04000Fアナタたち、《幻獣》の件は\x01",
            "よろしく頼むわね。\x02\x03",

            "#04006Fアリオスが動けない今の状況じゃ\x01",
            "アタシたちだけじゃ\x01",
            "どうしたって手が足りないもの。\x02\x03",

            "#04000Fスコットたちと、なんとか\x01",
            "分担して当たってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00000Fええ、任せてください。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00106Fシズクちゃんのことで\x01",
            "アリオスさんが動けないのは\x01",
            "仕方のないことですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#04003Fそう言ってもらえると助かるわ。\x02\x03",

            "#04000Fあなた達はあなた達で、\x01",
            "出来る限り調査を\x01",
            "進めてみてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3326")

    label("loc_32AC")


    #C0077
    ChrTalk(
        0x8,
        (
            "#04000Fアナタたち、《幻獣》の件は\x01",
            "よろしく頼むわね。\x02\x03",

            "あなた達はあなた達で、\x01",
            "出来る限り調査を\x01",
            "進めてみてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3326")

    Jump("loc_4641")

    label("loc_332B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3631")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3564")

    #C0078
    ChrTalk(
        0x8,
        (
            "#04000F今日はアリオスが本会議中の\x01",
            "警備をする予定になってるわ。\x02\x03",

            "各国首脳への配慮を踏まえても、\x01",
            "これ以上ない警備体制になるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00000Fこういう場合、中立の立場である\x01",
            "遊撃士の存在は心強いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#00104Fええ、ただ強いってだけじゃ\x01",
            "そこまでの大任は\x01",
            "任せてもらえないでしょうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#04003Fとはいえ、いくらアリオスでも\x01",
            "たった一人でテロリストから\x01",
            "首脳たちを守る事はできないわ。\x02\x03",

            "#04000F警察や警備隊との協力は\x01",
            "絶対に必要になるでしょう。\x01",
            "しっかりサポートしてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00000Fええ、気を抜かずに\x01",
            "警戒していこうと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_362C")

    label("loc_3564")


    #C0083
    ChrTalk(
        0x8,
        (
            "#04005Fああそうそう、そういえば……\x01",
            "ティオちゃんが帰ってきたって聞いて、\x01",
            "エオリアが凄く喜んでたわよ。\x02\x03",

            "#04011Fフフ、出先で会ったら\x01",
            "挨拶してあげてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#00206F……まあ、気が向いたら。\x02",
    )

    CloseMessageWindow()

    label("loc_362C")

    Jump("loc_4641")

    label("loc_3631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A2D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_37A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3665")
    Call(0, 13)
    Jump("loc_370F")

    label("loc_3665")


    #C0085
    ChrTalk(
        0x8,
        (
            "#04000F事情はアリオスから聞いたわ。\x02\x03",

            "クロスベルのギルドは\x01",
            "外国ともつながりがあるから\x01",
            "それなりの物資は揃ってるの。\x02\x03",

            "まあ、きっと大丈夫だから\x01",
            "心配しないでちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_370F")

    Jump("loc_37A1")

    label("loc_3714")


    #C0086
    ChrTalk(
        0x8,
        (
            "#04000Fさっき、アリオスのほうから\x01",
            "連絡があったわ。\x01",
            "患者さん、助かったみたいね。\x02\x03",

            "フフ、あなたたちも\x01",
            "大公に認められて\x01",
            "よかったじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A1")

    TalkEnd(0x8)
    Return()

    label("loc_37A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3996")

    #C0087
    ChrTalk(
        0x8,
        (
            "#04000Fさて、いよいよ\x01",
            "通商会議が始まったわね。\x02\x03",

            "#04003Fアタシたちは、警戒を兼ねて\x01",
            "各地の依頼を片付けているわ。\x02\x03",

            "#04000F何か起こった場合、\x01",
            "即座に近くにいる遊撃士が\x01",
            "駆けつけられるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#00100Fとても助かります。\x02\x03",

            "#00103F《赤い星座》や《黒月》の\x01",
            "出方が分からない以上、\x01",
            "油断は禁物ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#04003Fええ、相手が相手だし、\x01",
            "特に注意を払っておく\x01",
            "必要があるでしょうね。\x02\x03",

            "#04000Fとにかく、何か分かり次第\x01",
            "あなた達にも連絡するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00000Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3A28")

    label("loc_3996")


    #C0091
    ChrTalk(
        0x8,
        (
            "#04000Fアタシたちは、警戒を兼ねて\x01",
            "各地の依頼を片付けているわ。\x02\x03",

            "赤い星座や黒月については\x01",
            "何か分かり次第、あなた達にも\x01",
            "連絡させてもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A28")

    Jump("loc_4641")

    label("loc_3A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3FB1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AC4")

    #C0092
    ChrTalk(
        0x8,
        (
            "#04006Fふぅ、それにしても\x01",
            "この子が黒月長老の孫とはねえ。\x02\x03",

            "#04000Fなんていうか、ホント末恐ろしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAC")

    label("loc_3AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3B5B")

    #C0093
    ChrTalk(
        0x8,
        (
            "#04000Fキーアちゃんなら今も２階で\x01",
            "シズクちゃんと遊んでるわよ。\x02\x03",

            "#04011F２人の面倒はちゃんとアタシが\x01",
            "見ておくから心配しないでね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAC")

    label("loc_3B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F07")

    #C0094
    ChrTalk(
        0x8,
        (
            "#04000Fああ、アナタたち。\x01",
            "キーアちゃんなら２階で\x01",
            "シズクちゃんと遊んでるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00004Fすみません、お世話をかけます。\x01",
            "ギルドも忙しいでしょうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#04000Fううん、大歓迎よ。\x01",
            "賑やかになってウチにとっても\x01",
            "いい気分転換になるし。\x02\x03",

            "#04009Fそれにあの子達を見てると、\x01",
            "娘が２人もできたみたいで\x01",
            "母性本能がくすぐられるのよね～㈱\x02",
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
    Sleep(1200)

    #C0097
    ChrTalk(
        0x104,
        "#00306Fぼ、母性本能ッスか……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#04001F……なによ、文句でもあるワケ？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00109Fえ、ええっと……\x01",
            "そういえば、アリオスさんは？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "#04000Fああ、シズクちゃんを\x01",
            "病院から連れてきた後、\x01",
            "すぐ共和国方面に向かったわ。\x02\x03",

            "#04004F通商会議前の依頼を片付けつつ、\x01",
            "共和国方面の不安要素を\x01",
            "一通り洗い出してもらってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        "#10106Fはあ、さすがですね……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x105,
        (
            "#10302Fひとまずギルドの方は、\x01",
            "明日の準備は万端みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#04011Fフフ、あなたたちも\x01",
            "今日のうちにできる限りの\x01",
            "準備をしておくことね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 5)
    Jump("loc_3FAC")

    label("loc_3F07")


    #C0104
    ChrTalk(
        0x8,
        (
            "#04000Fキーアちゃんなら２階で\x01",
            "シズクちゃんと遊んでるわよ。\x02\x03",

            "#04011Fあの子達の事は任せてちょうだい。\x01",
            "アリオスが共和国から戻るまで\x01",
            "アタシがしっかり面倒を見るわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FAC")

    Jump("loc_4641")

    label("loc_3FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410D")

    #C0105
    ChrTalk(
        0x8,
        (
            "#04000F最近は、導力ネットを使っての依頼も\x01",
            "段々と増えてきているのよね。\x02\x03",

            "こういう雨の日なんかは、\x01",
            "特に端末越しの依頼が多いわよ。\x02\x03",

            "#04006Fただ、アタシたちも忙しいから\x01",
            "優先度の低そうな仕事は\x01",
            "お断りさせてもらってるのよね。\x02\x03",

            "#04000Fそういう依頼が支援課のほうに\x01",
            "回ることもあると思うけど……\x01",
            "何とかさばいてみてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_41DB")

    label("loc_410D")


    #C0106
    ChrTalk(
        0x8,
        (
            "#04006Fアタシたちも依頼はできるだけ\x01",
            "解決してあげたいけど、忙しいから\x01",
            "どうしても選別せざるを得ないのよ。\x02\x03",

            "#04000Fこぼれた依頼が支援課のほうに\x01",
            "回ることもあると思うけど……\x01",
            "何とかさばいてみてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41DB")

    Jump("loc_4641")

    label("loc_41E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A8")

    #C0107
    ChrTalk(
        0x8,
        (
            "#04000Fちなみにアリオスは、\x01",
            "アルタイルから戻ってすぐに\x01",
            "レミフェリアに出かけたわ。\x02\x03",

            "月末の通商会議でクロスベルに\x01",
            "大公がいらっしゃるから、\x01",
            "その準備を手伝っているそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00000Fアリオスさんも\x01",
            "相当忙しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#04006Fまあ、アリオスに\x01",
            "限ったことじゃないけど……\x02\x03",

            "#04000F通商会議が開かれる関係で\x01",
            "どこも忙しくなってるのは確かね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x109,
        (
            "#10100Fええ、警備隊のほうでも\x01",
            "人事異動やリハビリ訓練などもあって\x01",
            "かなり忙しかったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、ギルドについては\x01",
            "やっぱり人手不足が\x01",
            "切実ってところなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "#04006Fうーん、実際エステルとヨシュアが\x01",
            "抜けた穴が大きかったのよねえ。\x02\x03",

            "#04008F仕事は増える一方だし、\x01",
            "いくらアリオスやスコットたちが\x01",
            "優秀だと言っても、限度はあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        "#00103F確かに……それは言えてますね。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#04000Fまあ、これから更に忙しくなれば、\x01",
            "こっちの仕事を回すことも\x01",
            "大いにあり得るかもしれないわ。\x02\x03",

            "#04011Fフフ、色々とよろしく頼むわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00000Fええ、こちらこそ。\x01",
            "お互い頑張っていきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 5)
    Jump("loc_4641")

    label("loc_45A8")


    #C0116
    ChrTalk(
        0x8,
        (
            "#04003F月末の通商会議に向けて\x01",
            "これから忙しくなるでしょう。\x02\x03",

            "#04011Fこっちの仕事を回すことも\x01",
            "大いにあり得るかもしれないわ。\x01",
            "色々とよろしく頼むわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4641")

    TalkEnd(0x8)
    Return()

    # Function_4_993 end

    def Function_5_4645(): pass

    label("Function_5_4645")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4663")
    Call(0, 6)
    Jump("loc_471D")

    label("loc_4663")


    #C0117
    ChrTalk(
        0xFE,
        (
            "憧れていたキリカさんと\x01",
            "背中を合わせて戦えたこと……\x01",
            "私にとって何よりの経験だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "このクロスベルをこれからも\x01",
            "守っていくためにも、これからも\x01",
            "私自身の《泰斗》を磨かなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471D")

    Jump("loc_4E3A")

    label("loc_4722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_488E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4800")

    #C0119
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "逃げ遅れた人がいないか\x01",
            "市内を回っていたとき……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "なんだか見知った気配を\x01",
            "感じたような気がするんだ。\x01",
            "あれはもしかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "……そんなはずはないか。\x01",
            "すまない、忘れてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4889")

    label("loc_4800")


    #C0122
    ChrTalk(
        0xFE,
        (
            "市内で、なんだか見知った気配を\x01",
            "感じたような気がするんだ。\x01",
            "あれはもしかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "……そんなはずはないか。\x01",
            "すまない、忘れてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4889")

    Jump("loc_4E3A")

    label("loc_488E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A9")
    Call(0, 7)
    Jump("loc_492F")

    label("loc_48A9")


    #C0124
    ChrTalk(
        0xFE,
        (
            "アンタたち……\x01",
            "厳しそうなら助太刀するから\x01",
            "遠慮なく言ってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "私たちもギルドとして、\x01",
            "出来る限りのことを\x01",
            "させてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492F")

    Jump("loc_4E3A")

    label("loc_4934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4942")
    Jump("loc_4E3A")

    label("loc_4942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_49F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4961")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_4961")


    #C0126
    ChrTalk(
        0xFE,
        (
            "私たちも、しばらくは\x01",
            "ギルドに待機して様子を見るつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "ただ、状況は決して良いとは言えない……\x01",
            "出撃の準備はしておいた方がいいかもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E3A")

    label("loc_49F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A06")
    Jump("loc_4E3A")

    label("loc_4A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4A14")
    Jump("loc_4E3A")

    label("loc_4A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A22")
    Jump("loc_4E3A")

    label("loc_4A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A30")
    Jump("loc_4E3A")

    label("loc_4A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C05")

    #C0128
    ChrTalk(
        0xFE,
        (
            "キリカ先輩は、大統領のお付きとして\x01",
            "オルキスタワーに行ったようだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00000Fそういえばリンさんも、\x01",
            "キリカさんとお知り合いなんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "ああ、彼女は『泰斗流』の使い手でね。\x01",
            "私にとっては兄弟子にあたるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "数年前にお父上がお亡くなりになって、\x01",
            "しばらくはリベール王国で\x01",
            "ギルドの受付をしていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "まさか、大統領直属の\x01",
            "諜報機関に入っていたなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "正直、底が見えないお人だ。\x01",
            "気にかけておいた方がいいかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 7)
    Jump("loc_4C89")

    label("loc_4C05")


    #C0134
    ChrTalk(
        0xFE,
        (
            "キリカ先輩は、今回の通商会議でも\x01",
            "色々と動いていたようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "正直、底が見えないお人だ。\x01",
            "気にかけておいた方がいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C89")

    Jump("loc_4E3A")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C9C")
    Jump("loc_4E3A")

    label("loc_4C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4CAA")
    Jump("loc_4E3A")

    label("loc_4CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4CB8")
    Jump("loc_4E3A")

    label("loc_4CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD7")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCC")

    #C0136
    ChrTalk(
        0xFE,
        (
            "最初に会ったときは、\x01",
            "ただただヘッポコな奴らだと\x01",
            "思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "今のアンタらは充分に\x01",
            "一人前になったと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "これからは甘やかさずに\x01",
            "厳しくいくからそのつもりでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#00012Fはは……お手柔らかにお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E3A")

    label("loc_4DCC")


    #C0140
    ChrTalk(
        0xFE,
        (
            "今のアンタらは充分に\x01",
            "一人前になったと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "これからは甘やかさずに\x01",
            "厳しくいくからそのつもりでね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3A")

    TalkEnd(0xFE)
    Return()

    # Function_5_4645 end

    def Function_6_4E3E(): pass

    label("Function_6_4E3E")

    OP_4B(0x11, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0142
    ChrTalk(
        0xB,
        "キリカさん、お疲れ様でした！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xB,
        (
            "泰斗流《飛燕#4R ひ えん#紅児#4Rこう じ #》……\x01",
            "その真髄を間近で見れて、\x01",
            "とても勉強になりました！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x11,
        (
            "#03404F実戦は久しぶりだったけど\x01",
            "意外となんとかなってしまったわね。\x02\x03",

            "#03400F……それにしてもリン、\x01",
            "あなたも相当な鍛錬を積んだようね。\x02\x03",

            "８年前の交流試合で仕合った時とは\x01",
            "まるで見違えていて驚いたわ。\x01",
            "フフ、頼もしくなったじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        "はは、私なんてまだまだですよ。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "キリカさんやジンさんのような\x01",
            "達人の域に、少しでも近づけたなら\x01",
            "嬉しいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x11,
        (
            "#03400Fフフ、精進するといいわ。\x02\x03",

            "#03404Fそうね、もう１、２年経てば\x01",
            "ジンくらいには勝てるように\x01",
            "なるんじゃないかしら。\x02\x03",

            "#03402Fいまだに妙齢の女性に弱い性質は\x01",
            "克服できていないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "はは、キリカさんに言わせると\x01",
            "Ａ級遊撃士も形無しですね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1BB, 3)
    Return()

    # Function_6_4E3E end

    def Function_7_5141(): pass

    label("Function_7_5141")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0149
    ChrTalk(
        0xA,
        (
            "正直、あんな演説をされて\x01",
            "帝国が黙ってるとは思えない。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "必ず何らかのアクションを\x01",
            "取ってくる……あるいは、\x01",
            "もう取っているのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            "アランドールからのコンタクトも、\x01",
            "恐らくその一環に違いあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "ああ、それに関しては共和国側にも\x01",
            "同じ事が言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "教会の反応も気になるし……\x01",
            "とにかく万全を期さないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_7_5141 end

    def Function_8_52B0(): pass

    label("Function_8_52B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_52C1")
    Jump("loc_5B2D")

    label("loc_52C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_52CF")
    Jump("loc_5B2D")

    label("loc_52CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_54B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5425")

    #C0154
    ChrTalk(
        0xFE,
        (
            "マクダエル議長の無効宣言から\x01",
            "規制がさらに強化されて、\x01",
            "救急車での輸送もかなり制限されたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "病院に連れていけない患者は\x01",
            "何とか市に備蓄された薬で\x01",
            "対応していたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "やっぱり、街や教会で出来る\x01",
            "処置にも限界がある。\x01",
            "住民達に病院は絶対に必要なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "クロスベル市の解放……\x01",
            "絶対に成功させなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_54B2")

    label("loc_5425")


    #C0158
    ChrTalk(
        0xFE,
        (
            "やっぱり、街や教会で出来る\x01",
            "処置にも限界がある。\x01",
            "住民達に病院は絶対に必要なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "クロスベル市の解放……\x01",
            "絶対に成功させなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B2")

    Jump("loc_5B2D")

    label("loc_54B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55D1")

    #C0160
    ChrTalk(
        0xFE,
        (
            "今回の独立宣言、\x01",
            "故郷のレミフェリアでは\x01",
            "どういった対応をとるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "アルバート大公は聡明なお方だから、\x01",
            "公国民のことを第一に考えて\x01",
            "慎重にご判断されるでしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院方面にも連絡をとりつつ、\x01",
            "ギルドでも対応を考えていかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_566B")

    label("loc_55D1")


    #C0163
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院方面にも連絡をとりつつ、\x01",
            "ギルドでも対応を考えていかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "あなたたちには湖畔での借りもあるし、\x01",
            "困ったら何でも言ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566B")

    Jump("loc_5B2D")

    label("loc_5670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_567E")
    Jump("loc_5B2D")

    label("loc_567E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_585B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_569D")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_569D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_579C")

    #C0165
    ChrTalk(
        0xFE,
        (
            "猟兵団に人質に取られている\x01",
            "という異常事態……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "直接傷つけられてなくても、\x01",
            "相当な精神的負荷が\x01",
            "掛かってるに違いないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "この状態が長引けば、\x01",
            "身体に不調をきたす事も\x01",
            "充分に考えられると思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "一刻も早くなんとかしないと……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5856")

    label("loc_579C")


    #C0169
    ChrTalk(
        0xFE,
        (
            "猟兵団に人質に取られたことで、\x01",
            "マインツの人たちには相当な\x01",
            "精神的負荷が掛かってるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "この状態が長引けば、\x01",
            "身体に不調をきたす事も考えられる。\x01",
            "一刻も早くなんとかしないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5856")

    Jump("loc_5B2D")

    label("loc_585B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5869")
    Jump("loc_5B2D")

    label("loc_5869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5877")
    Jump("loc_5B2D")

    label("loc_5877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5885")
    Jump("loc_5B2D")

    label("loc_5885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5893")
    Jump("loc_5B2D")

    label("loc_5893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58A1")
    Jump("loc_5B2D")

    label("loc_58A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_58AF")
    Jump("loc_5B2D")

    label("loc_58AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_58BD")
    Jump("loc_5B2D")

    label("loc_58BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_58CB")
    Jump("loc_5B2D")

    label("loc_58CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58EA")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_58EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ABD")
    OP_4B(0xB, 0xFF)

    #C0171
    ChrTalk(
        0xC,
        (
            "そういえば……\x01",
            "ティオちゃんにも\x01",
            "しばらく会ってないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "確か、今はレマン自治州の方に\x01",
            "行っているんだったわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#00100Fええ、もうしばらくは\x01",
            "あちらにいるみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "……はっ、そうだわ。\x01",
            "レマンにはギルドの総本部もあるし、\x01",
            "私もしばらくそっちに出向して……！\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "……そんな余裕はないし、\x01",
            "ミシェルも許可しないと思うぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    #C0176
    ChrTalk(
        0xC,
        "ですよねー……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#00012F（はは……この人も相変わらずだな。）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_5B2D")

    label("loc_5ABD")


    #C0178
    ChrTalk(
        0xFE,
        (
            "ああ、久しぶりにティオちゃんを\x01",
            "ハグハグしたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "……帰ってきたらすぐ教えてね、\x01",
            "私、飛んでくから！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B2D")

    TalkEnd(0xFE)
    Return()

    # Function_8_52B0 end

    def Function_9_5B31(): pass

    label("Function_9_5B31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5B42")
    Jump("loc_61AA")

    label("loc_5B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B50")
    Jump("loc_61AA")

    label("loc_5B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA8")

    #C0180
    ChrTalk(
        0xFE,
        (
            "逃げ送れた人たちなんかは\x01",
            "手早く屋内に避難させたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "さすがに建物の中までは\x01",
            "確認できなかったけど、\x01",
            "百貨店のパールも無事だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "……こんな手をとるなんて、\x01",
            "大統領サイドもなりふり構って\x01",
            "られなくなってるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "これから先、奴らがどんな手段を\x01",
            "使ってきてもおかしくない。\x01",
            "君達も十分に注意するんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5D5E")

    label("loc_5CA8")


    #C0184
    ChrTalk(
        0xFE,
        (
            "……こんな手をとるなんて、\x01",
            "大統領サイドもなりふり構って\x01",
            "られなくなってるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "これから先、奴らがどんなを手段を\x01",
            "使ってきてもおかしくない。\x01",
            "君達も十分に注意するんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D5E")

    Jump("loc_61AA")

    label("loc_5D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E6E")

    #C0186
    ChrTalk(
        0xFE,
        (
            "同じクロスベル出身として、\x01",
            "アリオスさんの気持ちは\x01",
            "なんだか分かる気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "しかし、だからと言って\x01",
            "こんな風にギルドを\x01",
            "抜けてしまうなんてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "……考えていても仕方ないか。\x01",
            "今は遊撃士として、出来ることを\x01",
            "やっていかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5EDE")

    label("loc_5E6E")


    #C0189
    ChrTalk(
        0xFE,
        (
            "アリオスさんの事はこの際\x01",
            "考えていても仕方ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "今は遊撃士として、出来ることを\x01",
            "やっていかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EDE")

    Jump("loc_61AA")

    label("loc_5EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5EF1")
    Jump("loc_61AA")

    label("loc_5EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5F8A")
    OP_4B(0xFE, 0xFF)

    #C0191
    ChrTalk(
        0xFE,
        (
            "……そうですか、\x01",
            "アルモリカ方面は無事なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "ええ……はい……\x01",
            "念のため村の皆さんには\x01",
            "注意を呼びかけておいて下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    Jump("loc_61AA")

    label("loc_5F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F98")
    Jump("loc_61AA")

    label("loc_5F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5FA6")
    Jump("loc_61AA")

    label("loc_5FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5FB4")
    Jump("loc_61AA")

    label("loc_5FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5FC2")
    Jump("loc_61AA")

    label("loc_5FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5FD0")
    Jump("loc_61AA")

    label("loc_5FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5FDE")
    Jump("loc_61AA")

    label("loc_5FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FEC")
    Jump("loc_61AA")

    label("loc_5FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_61A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_600B")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_600B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_609C")
    Jump("loc_60E6")

    label("loc_609C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60E6")

    label("loc_60BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60DC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60E6")

    label("loc_60DC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60E6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0193
    ChrTalk(
        0xFE,
        (
            "最初に会った頃と比べると\x01",
            "随分と頼もしくなったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "今後、助け合っていける事も\x01",
            "多いと思うし、お互い\x01",
            "頑張っていこうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_61AA")

    label("loc_61A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_61AA")

    label("loc_61AA")

    TalkEnd(0xFE)
    Return()

    # Function_9_5B31 end

    def Function_10_61AE(): pass

    label("Function_10_61AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_61BF")
    Jump("loc_69D3")

    label("loc_61BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_61CD")
    Jump("loc_69D3")

    label("loc_61CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F9")

    #C0195
    ChrTalk(
        0xFE,
        (
            "魔導のゴーレムか……\x01",
            "厄介な物を持ち出してきたものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "解放作戦の際には、\x01",
            "市民に被害が及ばないよう\x01",
            "最大限の配慮が必要だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "……街中にあんなものを\x01",
            "徘徊させるとは、\x01",
            "断じて許せるものではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ギルドの名に懸けて、\x01",
            "必ず大統領の罪を\x01",
            "処断せねばなるまいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6383")

    label("loc_62F9")


    #C0199
    ChrTalk(
        0xFE,
        (
            "……街中にあんなものを\x01",
            "徘徊させるとは、\x01",
            "断じて許せるものではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "ギルドの名に懸けて、\x01",
            "必ず大統領の罪を\x01",
            "処断せねばなるまいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6383")

    Jump("loc_69D3")

    label("loc_6388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A3")
    Call(0, 7)
    Jump("loc_645F")

    label("loc_63A3")


    #C0201
    ChrTalk(
        0xFE,
        (
            "情報局のアランドール……\x01",
            "その名前は帝国ギルドにいた頃に\x01",
            "何度か耳にした事がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "既に会っているお前たちなら\x01",
            "分かっているだろうが、厄介な相手だ。\x01",
            "……充分に気をつけて行くがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_645F")

    Jump("loc_69D3")

    label("loc_6464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6472")
    Jump("loc_69D3")

    label("loc_6472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65AF")

    #C0203
    ChrTalk(
        0xFE,
        (
            "スコットが確認をとっているが……\x01",
            "アルモリカ村や病院などには\x01",
            "何も起こっていないようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "だが、山道の地形を利用し\x01",
            "地の利を得ている猟兵どもを\x01",
            "退けるのは至難の業だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "この状況が長引けば、\x01",
            "マインツの住民たちに\x01",
            "どんな危険があるか分からん。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "やはり、我々が動くしかないのか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6623")

    label("loc_65AF")


    #C0207
    ChrTalk(
        0xFE,
        (
            "この状況が長引けば、\x01",
            "マインツの住民たちに\x01",
            "どんな危険があるか分からん。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "やはり、我々が動くしかないのか……\x02",
    )

    CloseMessageWindow()

    label("loc_6623")

    Jump("loc_69D3")

    label("loc_6628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6636")
    Jump("loc_69D3")

    label("loc_6636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6644")
    Jump("loc_69D3")

    label("loc_6644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6652")
    Jump("loc_69D3")

    label("loc_6652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6660")
    Jump("loc_69D3")

    label("loc_6660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67D7")
    OP_4B(0xFE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6756")

    #C0209
    ChrTalk(
        0xFE,
        (
            "……ああ……ああ……\x01",
            "……そうか、やはり帝国の方で\x01",
            "テロリストどもに動きが……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……ああ、もちろんだ。\x01",
            "こちらの方でも警戒を強めよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00003F（どうやら帝国のギルドとも\x01",
            "  連絡をとりあってるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_67CE")

    label("loc_6756")


    #C0212
    ChrTalk(
        0xFE,
        (
            "……そうか、やはり帝国の方で\x01",
            "テロリストどもに動きが……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "……ああ、もちろんだ。\x01",
            "こちらの方でも警戒を強めよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CE")

    OP_4C(0xFE, 0xFF)
    Jump("loc_69D3")

    label("loc_67D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_67E5")
    Jump("loc_69D3")

    label("loc_67E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_67F3")
    Jump("loc_69D3")

    label("loc_67F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_69CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6812")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_6812")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68A3")
    Jump("loc_68ED")

    label("loc_68A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68C3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68ED")

    label("loc_68C3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68E3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68ED")

    label("loc_68E3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68ED")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0214
    ChrTalk(
        0xFE,
        (
            "アルタイル市での活躍は聞いている。\x01",
            "お前たちにしてはよくやったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "日頃の血の滲むような努力こそが\x01",
            "良き結果へと繋がる道標となる。\x01",
            "……この調子で精進するといい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_69D3")

    label("loc_69CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_69D3")

    label("loc_69D3")

    TalkEnd(0xFE)
    Return()

    # Function_10_61AE end

    def Function_11_69D7(): pass

    label("Function_11_69D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69EC")
    Call(0, 6)
    Jump("loc_6F20")

    label("loc_69EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D6C")

    #C0216
    ChrTalk(
        0x11,
        (
            "#03400Fあなたたちも……\x01",
            "お疲れ様だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00000Fキリカさんも、\x01",
            "ご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        "#00309Fやー、本当に助かったッスよ！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x11,
        (
            "#03402Fフフ、私はちょっとした\x01",
            "手伝いをしたというだけだけど。\x02\x03",

            "#03403Fそれよりも……\x01",
            "あの《大樹》の出現には\x01",
            "さすがに驚きを隠せないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#00205F共和国の方では\x01",
            "どういった対応を？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x11,
        (
            "#03403Fアルタイル市からも見える\x01",
            "あの《大樹》の出現には\x01",
            "さすがに面食らってるようね。\x02\x03",

            "どういう事態が起こるかも\x01",
            "分からないから、ひとまずは\x01",
            "様子見の体制をとるでしょう。\x02\x03",

            "#03400Fこれ以上詳しく話すことは\x01",
            "出来ないけど、そんな所かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        "#00103Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x11,
        (
            "#03400F私も顛末を見届けるまでは\x01",
            "ここに留まるつもりよ。\x02\x03",

            "#03403Fクロスベルがどのような道を辿るか、\x01",
            "もはや誰にも分からない……\x01",
            "全てはあなたたちに懸かっている。\x02\x03",

            "#03402F決して後悔することのないよう、\x01",
            "あなたたちの信じた道を進みなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#00000Fはい……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 7)
    Jump("loc_6F20")

    label("loc_6D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E6B")

    #C0225
    ChrTalk(
        0x11,
        (
            "#03400F私も顛末を見届けるまでは\x01",
            "ここに留まるつもりよ。\x02\x03",

            "#03403Fクロスベルがどのような道を辿るか、\x01",
            "もはや誰にも分からない……\x01",
            "全てはあなたたちに懸かっている。\x02\x03",

            "#03402F決して後悔することのないよう、\x01",
            "あなたたちの信じた道を進みなさい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F20")

    label("loc_6E6B")


    #C0226
    ChrTalk(
        0x11,
        (
            "#03403Fクロスベルがどのような道を辿るか、\x01",
            "もはや誰にも分からない……\x01",
            "全てはあなたたちに懸かっている。\x02\x03",

            "#03400F決して後悔することのないよう、\x01",
            "あなたたちの信じた道を進みなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F20")

    TalkEnd(0xFE)
    Return()

    # Function_11_69D7 end

    def Function_12_6F24(): pass

    label("Function_12_6F24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F39")
    Call(0, 13)
    Jump("loc_6F99")

    label("loc_6F39")


    #C0227
    ChrTalk(
        0x10,
        (
            "#01400F……こちらは任せてくれていい。\x02\x03",

            "お前たちはウルスラ間道で\x01",
            "『ナデリア茸』を探すんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F99")

    TalkEnd(0xFE)
    Return()

    # Function_12_6F24 end

    def Function_13_6F9D(): pass

    label("Function_13_6F9D")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0228
    ChrTalk(
        0x10,
        (
            "#01400F……ああ、さっき連絡したとおりだ。\x01",
            "すまないが、急ぎで探してみてくれ。\x02\x03",

            "確か、奥に備蓄があったはずだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#04000Fそうね……どこだったかしら。\x02\x03",

            "エオリアのほうにも\x01",
            "あたってみたほうがいいかしらね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_13_6F9D end

    def Function_14_708F(): pass

    label("Function_14_708F")

    TalkBegin(0xFF)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士たちのシフト表が貼り付けられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_71C1")
    SetChrName("")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　　　 －\x01",
            " 　スコット　：　アルモリカ村\x01",
            " ヴェンツェル： 鉱山街マインツ\x01",
            " 　　リン　　：　 《待機中》\x01",
            " 　エオリア　：　ウルスラ病院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_71C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_72A2")
    SetChrName("")

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　　　 －\x01",
            " 　スコット　：　 《待機中》\x01",
            " ヴェンツェル：　 《待機中》\x01",
            " 　　リン　　：　 《待機中》\x01",
            " 　エオリア　：　 《待機中》\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_72A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7383")
    SetChrName("")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　　　 －\x01",
            " 　スコット　：　 《待機中》\x01",
            " ヴェンツェル：　 《待機中》\x01",
            " 　　リン　　：　 《待機中》\x01",
            " 　エオリア　：　 《待機中》\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7470")
    SetChrName("")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　： オルキスタワー\x01",
            " 　スコット　：　ベルガード門\x01",
            " ヴェンツェル：　ベルガード門\x01",
            " 　　リン　　： 鉱山町マインツ\x01",
            " 　エオリア　： 鉱山町マインツ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7557")
    SetChrName("")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　： オルキスタワー\x01",
            " 　スコット　：　 《待機中》\x01",
            " ヴェンツェル：　 《待機中》\x01",
            " 　　リン　　：　 《待機中》\x01",
            " 　エオリア　：　 《待機中》\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7655")
    SetChrName("")

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：リン・エオリアの捜索\x01",
            " 　スコット　：リン・エオリアの捜索\x01",
            " ヴェンツェル：リン・エオリアの捜索\x01",
            " 　　リン　　：　　　 ※不明\x01",
            " 　エオリア　：　　　 ※不明\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_773F")
    SetChrName("")

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　《幻獣退治》\x01",
            " 　スコット　：　タングラム門\x01",
            " ヴェンツェル：　タングラム門\x01",
            " 　　リン　　：　ウルスラ病院\x01",
            " 　エオリア　：　ウルスラ病院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_773F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_782B")
    SetChrName("")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：幻獣退治及び調査\x01",
            " 　スコット　：　タングラム門\x01",
            " ヴェンツェル：　タングラム門\x01",
            " 　　リン　　：　ウルスラ病院\x01",
            " 　エオリア　：　ウルスラ病院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_782B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7919")
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　　※休暇\x01",
            " 　スコット　：幻獣退治及び調査\x01",
            " ヴェンツェル：幻獣退治及び調査\x01",
            " 　　リン　　：幻獣退治及び調査\x01",
            " 　エオリア　：幻獣退治及び調査\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7A02")
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　： オルキスタワー\x01",
            " 　スコット　：　アルモリカ村\x01",
            " ヴェンツェル：　 《待機中》\x01",
            " 　　リン　　：　 《待機中》\x01",
            " 　エオリア　：　ウルスラ病院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7AEC")
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　ウルスラ病院\x01",
            " 　スコット　：　※依頼対応中\x01",
            " ヴェンツェル：　※依頼対応中\x01",
            " 　　リン　　：　アルモリカ村\x01",
            " 　エオリア　：　アルモリカ村\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7BDB")
    SetChrName("")

    #A0242
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：カルバード共和国\x01",
            " 　スコット　： 鉱山町マインツ\x01",
            " ヴェンツェル：　ベルガード門\x01",
            " 　　リン　　：　※依頼対応中\x01",
            " 　エオリア　：　※依頼対応中　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7CC7")
    SetChrName("")

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：レミフェリア公国\x01",
            " 　スコット　：　 《待機中》\x01",
            " ヴェンツェル：　 《待機中》\x01",
            " 　　リン　　：　ウルスラ病院\x01",
            " 　エオリア　：　ウルスラ病院　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7DAD")
    SetChrName("")

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　氏　名　　　　　行き先\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：レミフェリア公国\x01",
            " 　スコット　：　アルモリカ村\x01",
            " ヴェンツェル： エレボニア帝国\x01",
            " 　　リン　　：　 《待機中》\x01",
            " 　エオリア　：　 《待機中》\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7DAD")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_708F end

    def Function_15_7DC4(): pass

    label("Function_15_7DC4")

    TalkBegin(0xFF)
    SetChrName("")

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士協会に対する依頼が\x01",
            "数多く張り出されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E93")

    #C0246
    ChrTalk(
        0x101,
        (
            "#00000F相変わらず、すごい量の依頼が\x01",
            "寄せられているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x109,
        (
            "#10103Fう～ん、あたしたちも\x01",
            "負けていられませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_7E93")

    TalkEnd(0xFF)
    Return()

    # Function_15_7DC4 end

    def Function_16_7E97(): pass

    label("Function_16_7E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EBC")
    Call(0, 33)
    Return()

    label("loc_7EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ECF")
    Call(0, 34)
    Return()

    label("loc_7ECF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_7EE0")
    Jump("loc_8330")

    label("loc_7EE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F02")
    Call(0, 17)
    Jump("loc_7F2D")

    label("loc_7F02")


    #C0248
    ChrTalk(
        0xD,
        "#01109Fシズク、あとで支援課に行こっ。\x02",
    )

    CloseMessageWindow()

    label("loc_7F2D")

    Jump("loc_8330")

    label("loc_7F32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F51")
    Jump("loc_82D4")

    label("loc_7F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823E")
    TurnDirection(0xD, 0x1A2, 0)

    #C0249
    ChrTalk(
        0xD,
        (
            "#01100Fねえねえ、シンっていったよね？\x02\x03",

            "クロスベルのコじゃないみたいだけど\x01",
            "いつまでいるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1A2,
        (
            "ボクか？\x01",
            "いちおう明後日までだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xD,
        (
            "#01105Fあ、じゃあ明日のタワーの\x01",
            "おひろめはどこでみるの～？\x02\x03",

            "#01102Fキーアたち、デパートの屋上で\x01",
            "見るつもりだけどいっしょにどう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0252
    ChrTalk(
        0x1A2,
        "い、いいのか……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0253
    ChrTalk(
        0xD,
        (
            "#01105Fいいって、どうしてー？\x02\x03",

            "#01109Fリュウとかアンリとか、\x01",
            "他のコもいっぱい来るし\x01",
            "たのしいと思うよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x1A2,
        "そ、そうか……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x1A2,
        (
            "……そこまで言うなら\x01",
            "参加してやってもいいぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x1A2,
        "たしか明日の１１時だったな！？\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xD,
        "#01109Fうんー、待ってるねー。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#00009F（はは……\x01",
            "  何だか嬉しそうだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        (
            "#00102F（そうね、あまり他の子供と\x01",
            "  遊ぶ機会がないのかも……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 2)
    TurnDirection(0xD, 0xE, 0)
    Jump("loc_82D4")

    label("loc_823E")

    TurnDirection(0xD, 0x1A2, 0)

    #C0260
    ChrTalk(
        0xD,
        (
            "#01100Fそれじゃ、明日の１１時に\x01",
            "デパートの屋上でねー。\x02\x03",

            "#01109Fみんなで待ってるからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x1A2,
        (
            "あ、ああ……\x01",
            "それじゃあ、また明日な。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 0)

    label("loc_82D4")

    Jump("loc_8330")

    label("loc_82D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F1")
    Jump("loc_8330")

    label("loc_82F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8303")
    Call(0, 17)
    Jump("loc_8330")

    label("loc_8303")


    #C0262
    ChrTalk(
        0xD,
        "#01109Fそれじゃあシズクも一緒に行こー！\x02",
    )

    CloseMessageWindow()

    label("loc_8330")

    TalkEnd(0xFE)
    Return()

    # Function_16_7E97 end

    def Function_17_8334(): pass

    label("Function_17_8334")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8455")

    #C0263
    ChrTalk(
        0xD,
        (
            "#01104Fシズクー、シンも行っちゃったし\x01",
            "どこか外に遊びにいこっかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xE,
        (
            "#06005Fあ、うん、そうだね。\x02\x03",

            "#06000Fでも、子供ふたりで行っても\x01",
            "大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xD,
        "#01111Fんー……確かにそっかー。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0266
    ChrTalk(
        0xD,
        "#01110Fあっ、それならいい考えがあるかもー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8512")

    label("loc_8455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8512")

    #C0267
    ChrTalk(
        0xD,
        (
            "#01109Fでねー、今は青いシートが\x01",
            "かかってるけど……\x01",
            "すっごく大っきいんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xE,
        (
            "#06002Fいいなあ……\x01",
            "ふふっ、私も見てみたいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xD,
        "#01109Fそれじゃあシズクも一緒に行こー！\x02",
    )

    CloseMessageWindow()

    label("loc_8512")

    SetScenarioFlags(0x1, 1)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_17_8334 end

    def Function_18_851E(): pass

    label("Function_18_851E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8543")
    Call(0, 33)
    Return()

    label("loc_8543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8556")
    Call(0, 34)
    Return()

    label("loc_8556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_8567")
    Jump("loc_87DC")

    label("loc_8567")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8589")
    Call(0, 17)
    Jump("loc_85E2")

    label("loc_8589")


    #C0270
    ChrTalk(
        0xE,
        (
            "#06005Fうん、いいけど……\x01",
            "いい考えってなんなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        "#01104Fえへへ、まだヒミツー。\x02",
    )

    CloseMessageWindow()

    label("loc_85E2")

    Jump("loc_87DC")

    label("loc_85E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8606")
    Jump("loc_877B")

    label("loc_8606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86E4")
    TurnDirection(0xE, 0x1A2, 0)

    #C0272
    ChrTalk(
        0xE,
        (
            "#06002Fふふっ、シン君は\x01",
            "とってもいい子なんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x1A2,
        (
            "い、いやっ……\x01",
            "そ、そんなことはないぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1A2,
        (
            "なんたってボクは、\x01",
            "将来《黒月》を背負うオトコ\x01",
            "なんだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xE,
        "#06002Fクスクス……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    TurnDirection(0xE, 0xD, 0)
    Jump("loc_877B")

    label("loc_86E4")

    TurnDirection(0xE, 0x1A2, 0)

    #C0276
    ChrTalk(
        0xE,
        (
            "#06002Fクスクス……\x01",
            "よくわからないけど、\x01",
            "シン君はいい子だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x1A2,
        (
            "（む、むう……\x01",
            "  ボクはそんなんじゃ\x01",
            "  ないんだけどなあ。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 0)

    label("loc_877B")

    Jump("loc_87DC")

    label("loc_8780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_87DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8798")
    Jump("loc_87DC")

    label("loc_8798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87AA")
    Call(0, 17)
    Jump("loc_87DC")

    label("loc_87AA")


    #C0278
    ChrTalk(
        0xE,
        (
            "#06002Fふふ、分かった。\x01",
            "一緒に見に行こうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87DC")

    TalkEnd(0xFE)
    Return()

    # Function_18_851E end

    def Function_19_87E0(): pass

    label("Function_19_87E0")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_19_87E0 end

    def Function_20_87E7(): pass

    label("Function_20_87E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2000, 1000, 2000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20740, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04000.itp")
    SetChrPos(0x101, -2000, 0, -1000, 0)
    SetChrPos(0x102, -2000, 0, -1000, 0)
    SetChrPos(0x109, -2000, 0, -1000, 0)
    SetChrPos(0x105, -2000, 0, -1000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_88CF():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88CF)

    def lambda_88E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88E9)
    Sleep(250)

    def lambda_88FD():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88FD)

    def lambda_8917():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8917)
    Sleep(600)

    def lambda_892B():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_892B)

    def lambda_8945():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8945)
    Sleep(250)

    def lambda_8959():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8959)

    def lambda_8973():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8973)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    OP_68(1000, 1100, 11300, 3000)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0279
    ChrTalk(
        0x8,
        "#04005Fあら、あなたたち……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#00000Fミシェルさん……\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0x102, -500, 0, 3000, 0)
    SetChrPos(0x105, 0, 0, 1900, 0)
    SetChrPos(0x109, -1000, 0, 1900, 0)

    def lambda_8A54():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A54)
    Sleep(100)

    def lambda_8A71():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A71)
    Sleep(150)

    def lambda_8A8E():
        OP_96(0xFE, 0x7D0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A8E)
    Sleep(100)

    def lambda_8AAB():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8AAB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x105, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B6A")

    #A0281
    AnonymousTalk(
        0x8,
        (
            "フフ、久しぶりじゃない。\x02\x03",

            "アルタイル市での捕り物、\x01",
            "本当にご苦労だったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8BCD")

    label("loc_8B6A")


    #A0282
    AnonymousTalk(
        0x8,
        (
            "フフ、久しぶりじゃない。\x02\x03",

            "遅くなったけど\x01",
            "アルタイル市での捕り物、\x01",
            "本当にご苦労だったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8BCD")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0283
    ChrTalk(
        0x101,
        (
            "#12P#00000Fありがとうございます。\x01",
            "こちらこそ、アリオスさんたちの\x01",
            "協力があって助かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、\x01",
            "ミシェルさんもお元気そうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#04011Fフフン、もちろん絶好調よ♪\x02\x03",

            "#04006Fま、エステルとヨシュアが\x01",
            "いなくなったおかげで\x01",
            "忙しさは増しちゃったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#12P#00003Fやはり、そうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x109,
        (
            "#12P#10100Fでも、アリオスさんや\x01",
            "他の遊撃士の方々で\x01",
            "上手く回しているみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#04004Fま、手が足りないのには\x01",
            "慣れているしね。\x02\x03",

            "#04000Fなんとか切り盛りさせて\x01",
            "もらっているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x105,
        (
            "#12P#10304Fまあ、そこは\x01",
            "民間人の味方たる遊撃士……\x02\x03",

            "#10300Fどんなに多忙を極めても\x01",
            "泣き言は言ってられない\x01",
            "だろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#04004Fその通り、\x01",
            "よく分かってるじゃない。\x02\x03",

            "#04009Fアナタたち警察も\x01",
            "認められてきたようだけど、\x01",
            "だからこそ私たちも──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x8,
        (
            "#04005Fって、もしかして\x01",
            "この子たち……？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#12P#00000Fええ、支援課の新メンバーです。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x109,
        (
            "#12P#10100Fこのたび、警備隊より出向した\x01",
            "ノエル・シーカーです！\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        (
            "#12P#10302Fワジ・ヘミスフィア……\x01",
            "とだけ名乗れば\x01",
            "分かってもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "#04000Fへえ……\x01",
            "なかなか面白い子達が\x01",
            "集まったみたいじゃないの。\x02\x03",

            "#04004F現役警備隊員は言わずもがな、\x01",
            "あの《テスタメンツ》の頭#2Rヘッド#まで\x01",
            "いるなんてね。\x02\x03",

            "#04000F何にせよ、支援課の再開は\x01",
            "こちらにとっても大助かりよ。\x02\x03",

            "いざというときは\x01",
            "頼りにしちゃっていいのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、もちろんです。\x02\x03",

            "立場は違いますけど\x01",
            "互いに力を合わせていきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "#04004Fフフ、最初に会った頃より\x01",
            "いい顔になってきたわね。\x02\x03",

            "#04011Fそれじゃ、改めて……\x01",
            "これからよろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x139, 0)
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_87E7 end

    def Function_21_91E6(): pass

    label("Function_21_91E6")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Fade(500)
    OP_68(-2140, 1300, 44740, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19620, 0)
    SetChrPos(0x101, -2140, 0, 45000, 90)
    SetChrPos(0x102, -2240, 0, 43520, 90)
    SetChrPos(0x109, -3420, 0, 43420, 90)
    SetChrPos(0x105, -3320, 0, 45300, 90)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_0D()

    #C0298
    ChrTalk(
        0xB,
        "よう、特務支援課の。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        "あら、お久しぶりね。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#00000Fお久しぶりです、\x01",
            "リンさんにエオリアさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#00100Fギルドの皆さんは\x01",
            "お変わりありませんか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    #C0302
    ChrTalk(
        0xB,
        (
            "ああ、相変わらず\x01",
            "忙しくさせてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    #C0303
    ChrTalk(
        0xB,
        (
            "えっと、そっちにいるのは\x01",
            "新入り君たちかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x105,
        "#6P#10300Fま、そんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x109,
        (
            "#6P#10100F遊撃士の方々ですよね、\x01",
            "よろしくおねがいします！\x02\x03",

            "#10109Fそういえば、あなた方が\x01",
            "共和国に向かうのを何度か\x01",
            "お見かけした事があります。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x109, 500)

    #C0306
    ChrTalk(
        0xB,
        (
            "ああ、君は警備隊員の……\x01",
            "そういえばタングラム門で\x01",
            "何度か見かけた気がするな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    #C0307
    ChrTalk(
        0xC,
        (
            "ふふ、アルタイル市での作戦では\x01",
            "なかなか活躍したんですってね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0308
    ChrTalk(
        0xC,
        (
            "あの教団事件を乗り越えて、\x01",
            "あなたたちもそろそろ一人前に\x01",
            "なってきたんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#00012Fはは、まだまだな部分は\x01",
            "かなり多いと思いますけど……\x02\x03",

            "#00000Fこれからも力の限り\x01",
            "頑張らせてもらうつもりです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0310
    ChrTalk(
        0xB,
        "はは、その意気だ。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xC, 0x0, 0x0)
    SetScenarioFlags(0x138, 6)
    EventEnd(0x5)
    Return()

    # Function_21_91E6 end

    def Function_22_95F9(): pass

    label("Function_22_95F9")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4470, 1300, 42260, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21800, 0)
    SetChrPos(0x101, -3700, 0, 41400, 270)
    SetChrPos(0x102, -3600, 0, 42800, 270)
    SetChrPos(0x109, -2500, 0, 41000, 270)
    SetChrPos(0x105, -2400, 0, 43000, 270)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9703")
    Jump("loc_974D")

    label("loc_9703")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9723")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_974D")

    label("loc_9723")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9743")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_974D")

    label("loc_9743")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_974D")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9803")
    Jump("loc_984D")

    label("loc_9803")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9823")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_984D")

    label("loc_9823")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9843")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_984D")

    label("loc_9843")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_984D")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_0D()

    #C0311
    ChrTalk(
        0x9,
        "#6Pおや、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xA,
        (
            "……特務支援課か。\x01",
            "ふむ、久しぶりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#11P#00000Fスコットさん、ヴェンツェルさん、\x01",
            "おつかれさまです。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x105,
        (
            "#11P#10300F遊撃士の人たちか。\x01",
            "フフ、どうやらけっこう\x01",
            "腕が立つみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x105, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99DF")
    Jump("loc_9A29")

    label("loc_99DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99FF")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A29")

    label("loc_99FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A1F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A29")

    label("loc_9A1F")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A29")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    #C0315
    ChrTalk(
        0x9,
        (
            "#6Pそういう君は、\x01",
            "旧市街の不良グループの……\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x109, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B14")
    Jump("loc_9B5E")

    label("loc_9B14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B34")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B5E")

    label("loc_9B34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B54")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B5E")

    label("loc_9B54")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B5E")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    #C0316
    ChrTalk(
        0x9,
        (
            "#6Pそれとそっちの子は\x01",
            "どうやら警備隊員みたいだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C4F")
    Jump("loc_9C99")

    label("loc_9C4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9C6F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C8F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C8F")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C99")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    #C0317
    ChrTalk(
        0x9,
        (
            "#6Pはは、なかなか面白い\x01",
            "新入りたちが入ったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#11P#10105Fワ、ワジ君はまだしも……\x01",
            "見ただけで分かるものですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x105, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DD0")
    Jump("loc_9E1A")

    label("loc_9DD0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9DF0")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E1A")

    label("loc_9DF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E10")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E1A")

    label("loc_9E10")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E1A")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Sleep(150)

    #C0319
    ChrTalk(
        0xA,
        (
            "普通の警察官とは佇まいが\x01",
            "明らかに違うようだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xA,
        (
            "遊撃士と似たような仕事を\x01",
            "している以上、お前たちも\x01",
            "観察眼を鍛えておくことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        "#11P#00100Fふふ、ご忠告ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x9,
        (
            "#6P今後、助け合っていける事も\x01",
            "多いと思うし、お互い\x01",
            "頑張っていこうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x138, 7)
    EventEnd(0x5)
    Return()

    # Function_22_95F9 end

    def Function_23_9F62(): pass

    label("Function_23_9F62")

    EventBegin(0x0)
    Fade(500)
    OP_68(1480, 1200, 9530, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21690, 0)
    SetChrPos(0x101, 500, 0, 8300, 0)
    SetChrPos(0x102, 1500, 0, 8200, 0)
    SetChrPos(0x103, 1000, 0, 7000, 0)
    SetChrPos(0x109, 0, 0, 6800, 0)
    SetChrPos(0x105, 2000, 0, 6900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    OP_0D()

    #C0323
    ChrTalk(
        0x8,
        "#5P#04000Fああ、アナタたち。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        "やあ、昨日は助かったよ。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#12P#00005Fリンさん、エオリアさん……\x01",
            "もう大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "ええ、なんとかね。\x01",
            "これもあなたたちのおかげよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 500)
    Sleep(500)

    #C0327
    ChrTalk(
        0xC,
        (
            "ティオちゃん、あとでお礼に\x01",
            "よしよしってしてあげるわね㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xC, 500)

    #C0328
    ChrTalk(
        0x103,
        (
            "#12P#00203F……謹んでお断りします。\x02\x03",

            "#00200Fでも、その調子なら\x01",
            "本当に大丈夫そうですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    #C0329
    ChrTalk(
        0xB,
        (
            "ああ、そこまでの無理は\x01",
            "まだできないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)

    #C0330
    ChrTalk(
        0xB,
        (
            "あれ、そういえば……\x01",
            "あの赤毛はどうしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xB,
        (
            "いつもならこの辺りで\x01",
            "『じゃあ俺が代わりに……』とか\x01",
            "言ってるタイミングだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x105)
    OP_64(0x109)
    OP_64(0x103)

    #C0332
    ChrTalk(
        0x8,
        (
            "#5P#04001F……何かあったみたいね。\x01",
            "よかったら話してもらえる？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        "#12P#00000F……ええ、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちはランディが\x01",
            "失踪した事を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0335
    ChrTalk(
        0x8,
        (
            "#5P#04003F……なるほどね。\x02\x03",

            "#04001F今回のマインツの占領事件……\x01",
            "《赤い星座》が絡んでいる以上、\x01",
            "どこか予想はしていたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#12P#00101F……ギルドは、今回の事件に\x01",
            "どう対応されるんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)
    Sleep(500)

    #C0337
    ChrTalk(
        0xB,
        (
            "……警備隊が事件の解決に\x01",
            "全力で当たっている現状、\x01",
            "今のところは様子見だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "でも、この状況が長く続くなら、\x01",
            "私たちも動かざるを得ないだろう。\x01",
            "……そうだな、ミシェル？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)
    Sleep(50)
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    #C0339
    ChrTalk(
        0x8,
        (
            "#5P#04003Fええ……\x02\x03",

            "#04001F場合によっては、周辺国から\x01",
            "Ａ級以上の遊撃士たちを呼んで、\x01",
            "介入する必要があるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0340
    ChrTalk(
        0x101,
        "#12P#00011Fそ、そこまで……！？\x02",
    )

    CloseMessageWindow()

    def lambda_A621():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A621)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0341
    ChrTalk(
        0xC,
        "あくまで最悪の場合の話だけどね。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xC,
        (
            "今、アリオスさんが市長の所へ\x01",
            "その交渉をしに行っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "もし、警備隊にこの事件を\x01",
            "解決する展望がないなら……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x109,
        "#12P#10108F……っ……\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x105,
        (
            "#12P#10303Fまあ、民間人の安全を第一とする\x01",
            "ギルドとしては当然の対応だろうけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    #C0346
    ChrTalk(
        0x8,
        (
            "#5P#04003F……とにかく、\x01",
            "あの赤毛の坊やの事は\x01",
            "こちらでも気にかけておくわ。\x02\x03",

            "#04001F何が起こるかわからない状況だし、\x01",
            "アナタたちも気をつけてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#12P#00001F……ええ、分かりました。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x16F, 2)
    EventEnd(0x5)
    Return()

    # Function_23_9F62 end

    def Function_24_A84A(): pass

    label("Function_24_A84A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_68(-1120, 1100, 7400, 0)
    MoveCamera(31, 10, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24030, 0)
    SetChrPos(0x101, -1750, 0, 2730, 0)
    SetChrPos(0x102, -2950, 0, 2530, 0)
    SetChrPos(0x103, -1750, 0, 1730, 0)
    SetChrPos(0x104, -2950, 0, 1530, 0)
    SetChrPos(0xF4, -1750, 0, 730, 0)
    SetChrPos(0xF5, -2950, 0, 530, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0348
    ChrTalk(
        0x8,
        "#5P#04005Fああっ……アナタたち！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A9AF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A9AF)
    Sleep(50)

    def lambda_A9BF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A9BF)
    Sleep(50)

    def lambda_A9CF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A9CF)
    TurnDirection(0xB, 0x101, 500)

    #C0349
    ChrTalk(
        0xA,
        (
            "独立宣言以来、\x01",
            "音沙汰が無かったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x9,
        "ハハ、元気そうでなによりだ。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#12P#00000Fミシェルさん、皆さん……\x01",
            "お久しぶりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        "#12P#00202Fふふ、ご無事でなによりです。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xB,
        "ふふ、君達のほうこそ。\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xC,
        (
            "ティオちゃん……\x01",
            "本当に良かったわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x8,
        (
            "#5P#04006F……って、悠長に挨拶を交わしてる\x01",
            "状況でもないわね。\x02\x03",

            "#04001F再会してすぐで悪いけど、\x01",
            "情報交換をしてもらえない？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#12P#00000Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(40, 1300, 9740, 0)
    MoveCamera(29, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22940, 0)
    SetChrPos(0x101, 300, 0, 8000, 0)
    SetChrPos(0x102, -1000, 0, 8200, 0)
    SetChrPos(0x103, 1500, 0, 8100, 0)
    SetChrPos(0x104, 0, 0, 6600, 0)
    SetChrPos(0xF4, -1300, 0, 7000, 0)
    SetChrPos(0xF5, 1600, 0, 6900, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    #C0357
    ChrTalk(
        0xA,
        (
            "……なるほど、\x01",
            "そんなことになってたとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xB,
        (
            "正直、ワケが分からない\x01",
            "状態だったけど\x01",
            "ようやく合点がいったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x9,
        (
            "しかし、西口に\x01",
            "赤い《神機》が現れたって聞いて、\x01",
            "何事かと思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x9,
        "まさか、エステルたちだったとはな。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xC,
        (
            "東口や北口では\x01",
            "黒月や警備隊のレジスタンスも\x01",
            "手伝ってくれてるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "ふふ、これもあなたたちの\x01",
            "人脈ってところかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        "#12P#00300Fハハ、まあそんなとこッス。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x102,
        (
            "#6P#00105Fそういえば……\x01",
            "市内に《魔導兵》が現れて、\x01",
            "人的な被害は出ていないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xC,
        "ええ、今のところはね。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x9,
        (
            "逃げ遅れた人たちがいないか、\x01",
            "俺たちも警戒しつつ\x01",
            "この近辺を回ってみたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x9,
        (
            "どうやら《魔導兵》どもは、\x01",
            "クロスベル市民には絶対に\x01",
            "手を出さないみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF57")

    #C0368
    ChrTalk(
        0x105,
        (
            "#12P#10403Fふむ……大統領側が上手く\x01",
            "コントロールしてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B012")

    label("loc_AF57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFB4")

    #C0369
    ChrTalk(
        0x10A,
        (
            "#12P#00603Fふむ……大統領側が上手く\x01",
            "コントロールしているようだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B012")

    label("loc_AFB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B012")

    #C0370
    ChrTalk(
        0x109,
        (
            "#12P#10101Fどうやら、大統領側が上手く\x01",
            "コントロールしているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B012")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B05D")

    #C0371
    ChrTalk(
        0x106,
        (
            "#12P#10705Fある意味、安心して\x01",
            "いいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0E8")

    label("loc_B05D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0A8")

    #C0372
    ChrTalk(
        0x109,
        (
            "#12P#10105Fある意味、安心して\x01",
            "いいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0E8")

    label("loc_B0A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0E8")

    #C0373
    ChrTalk(
        0x105,
        (
            "#12P#10304Fある意味、安心して\x01",
            "いいのかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0E8")


    #C0374
    ChrTalk(
        0x101,
        (
            "#12P#00001Fそれでも……\x01",
            "不安に思っている人は\x01",
            "かなり多いはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        (
            "#6P#00103Fそうね……この状態が長く続けば、\x01",
            "巻き込まれて怪我したりする人が\x01",
            "出ないとも限らないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        (
            "#5P#04003Fええ、罪もない民間人が\x01",
            "危険に晒されている以上、\x01",
            "ギルドも放ってはおけないわ。\x02\x03",

            "#04011Fオルキスタワーへの突入と\x01",
            "大統領の逮捕……アタシたちも\x01",
            "改めて、手伝わせてもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        (
            "#12P#00204Fありがとうございます。\x01",
            "……とても心強いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        (
            "#5P#04003Fただし……\x01",
            "恐らくオルキスタワーには\x01",
            "アリオスがいるわ。\x02\x03",

            "あのマリアベルお嬢さんや、\x01",
            "《戦鬼》なんかも\x01",
            "待ち構えているでしょう。\x02\x03",

            "#04001Fきっと一筋縄ではいかないはず……\x01",
            "それは分かっているわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x104,
        "#12P#00303F……百も承知だ。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        (
            "#12P#00001Fどんな《壁》があろうと……\x01",
            "俺たちは突き進むのみですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#5P#04004Fフフ、心の準備は\x01",
            "出来ているみたいね。\x02\x03",

            "#04001F──作戦を開始するときは、\x01",
            "改めて連絡をちょうだい。\x02\x03",

            "アタシたちもその時までに\x01",
            "しっかり準備しておくから。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#12P#00000Fええ……では、後ほど。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 300, 0, 8000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0x9, 0x2D, 0x0)
    OP_93(0xA, 0x2D, 0x0)
    SetScenarioFlags(0x1BB, 0)
    EventEnd(0x5)
    Return()

    # Function_24_A84A end

    def Function_25_B4FD(): pass

    label("Function_25_B4FD")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04000.itp")
    Fade(500)
    OP_68(1000, 1000, 11300, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 900, 0, 10000, 0)
    SetChrPos(0x102, 1500, 0, 9400, 0)
    SetChrPos(0x104, 300, 0, 8700, 0)
    SetChrPos(0x109, -300, 0, 9300, 0)
    SetChrPos(0x105, -1400, 0, 9350, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0383
    AnonymousTalk(
        0x8,
        (
            "あら、よく来たわね。\x02\x03",

            "まだアリオスは戻ってないけど\x01",
            "よかったら２階で待っている？\x02\x03",

            "何だったら用事を済ませてから\x01",
            "来てくれてもいいけど。\x02",
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

    #C0384
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあ、そうなんですか。\x02\x03",

            "#00008F（そろそろ夕方だし……\x01",
            "  他にやっておく事はあったかな？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",          # 0
            "【アリオスが戻るのを待つ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B798"),
        (1, "loc_B825"),
        (SWITCH_DEFAULT, "loc_BA2A"),
    )


    label("loc_B798")


    #C0385
    ChrTalk(
        0x8,
        (
            "#5P#04011Fそ、なら用が済んだら\x01",
            "こちらに来てちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        "#12P#00012Fええ、また来ます。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_BA2A")

    label("loc_B825")


    #C0387
    ChrTalk(
        0x8,
        (
            "#5P#04011Fそれじゃあ２階に上がって\x01",
            "適当にくつろいでてちょうだい。\x02\x03",

            "お茶とコーヒーの用意があるから\x01",
            "勝手に淹れちゃっていいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        "#12P#00012Fはは、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x102,
        "#12P#00102Fそれではお邪魔します。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 4500)

    def lambda_B903():

        label("loc_B903")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B903")

    QueueWorkItem2(0x8, 2, lambda_B903)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 26)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x2)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    StopBGM(0xBB8)
    WaitBGM()
    SetChrName("")

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ほどなくして\x01",
            "アリオスがギルドに戻ってきた。\x02\x03",

            "ロイドたちは改めて、通商会議及び、\x01",
            "《黒月》や《赤い星座》についての\x01",
            "情報交換を行うことにした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0x8, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_BA2A")

    label("loc_BA2A")

    Return()

    # Function_25_B4FD end

    def Function_26_BA2B(): pass

    label("Function_26_BA2B")

    OP_92(0xFE, 0x1F40, 0x2AF8, 0x1F4)

    def lambda_BA3D():
        OP_95(0xFE, 8000, 0, 11000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA3D)
    WaitChrThread(0xFE, 1)

    def lambda_BA5B():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA5B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_BA2B end

    def Function_27_BA75(): pass

    label("Function_27_BA75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    SoundLoad(4049)
    SoundLoad(4050)
    LoadChrToIndex("chr/ch09102.itc", 0x1E)
    LoadChrToIndex("chr/ch02402.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch02902.itc", 0x23)
    LoadChrToIndex("chr/ch03002.itc", 0x24)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -9300, 100, 46800, 0)
    SetChrPos(0x102, -7500, 100, 46800, 0)
    SetChrPos(0x104, -5700, 100, 46800, 0)
    SetChrPos(0x109, -11100, 100, 49400, 180)
    SetChrPos(0x105, -11100, 100, 46800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrFlags(0x8, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -7500, 100, 49400, 180)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    EndChrThread(0x10, 0xFF)
    SetChrPos(0x10, -9300, 100, 49400, 180)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    SetMapObjFrame(0xFF, "chair", 0x0, 0x1)
    SetMapObjFrame(0xFF, "chair_shadow", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x0, 0x12)
    OP_78(0x1, 0x13)
    OP_78(0x2, 0x14)
    OP_78(0x3, 0x15)
    OP_78(0x4, 0x16)
    OP_78(0x5, 0x17)
    OP_78(0x6, 0x18)
    OP_78(0x7, 0x19)
    OP_49()
    SetChrPos(0x12, -11100, 0, 46600, 0)
    OP_D5(0x12, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x13, -9300, 0, 46600, 0)
    OP_D5(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x14, -7500, 0, 46600, 0)
    OP_D5(0x14, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x15, -5700, 0, 46600, 0)
    OP_D5(0x15, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x16, -11100, 0, 49600, 0)
    OP_D5(0x16, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x17, -9300, 0, 49600, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x18, -7500, 0, 49600, 0)
    OP_D5(0x18, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x19, -5700, 0, 49600, 0)
    OP_D5(0x19, 0x0, 0x0, 0x0, 0x0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(-8200, 900, 48300, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0391
    AnonymousTalk(
        0x10,
        (
            "#4049V#30W──なるほどな。\x02\x03",

            "#4050V《クリムゾン商会》というのに\x01",
            "そんな裏があったとは……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD2)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0392
    ChrTalk(
        0x8,
        (
            "#04006F最近、帝都方面の情報が\x01",
            "入りにくくなってたものねぇ。\x02\x03",

            "#04000Fありがと、おかげで助かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#12P#00004Fいえ、お役に立てたら幸いです。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x105,
        (
            "#6P#10306Fしかし《赤い星座》の情報は\x01",
            "そっちの方でも掴んでないわけ？\x02\x03",

            "#10300Fギルドって、猟兵団と小競り合いを\x01",
            "することが多いって聞くけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "#5P#01403F確かに多いが、\x01",
            "《赤い星座》クラスの大物と\x01",
            "事を構える機会は滅多にない。\x02\x03",

            "#01400F……下手をすればお互い\x01",
            "全面戦争になりかねないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        "#12P#00101Fそこまで……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x109,
        (
            "#10108Fちょっとした小国の\x01",
            "軍隊レベルみたいですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#04003F──数ある猟兵団の中でも\x01",
            "《赤い星座》は別格といえるわね。\x02\x03",

            "大陸全土にコネクションを持ち、\x01",
            "紛争の兆しあらば即座に介入して\x01",
            "自分たちを高く売り込む……\x02\x03",

            "#04001F同じ猟兵団で匹敵しそうなのは\x01",
            "《西風の旅団》くらいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x105,
        (
            "#6P#10305Fたしか、ルバーチェの若頭の\x01",
            "古巣だった場所だったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x104,
        (
            "#00301F……あっちもあっちで\x01",
            "歴戦の猛者どもが集まる猟兵団だ。\x02\x03",

            "特に《猟兵王》と呼ばれたトップは\x01",
            "化物みたいなヤツだったが……\x02\x03",

            "#00303F半年前に《闘神》──\x01",
            "俺の親父と相討ちになったらしい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0401
    ChrTalk(
        0x102,
        "#6P#00108Fランディ……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#6P#00008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x10,
        "#5P#01405Fふむ、色々あるみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x8,
        (
            "#04003F一応、その情報については\x01",
            "ギルドの方でも把握しているわ。\x02\x03",

            "#04001Fちなみに現在、《西風の旅団》は\x01",
            "活動を休止しているそうだけど……\x02\x03",

            "《赤い星座》の方は相変わらず\x01",
            "精力的に活動しているみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x104,
        (
            "#00306F叔父貴が残っているからな。\x02\x03",

            "#00303F──赤い星座の副団長、\x01",
            "《赤の戦鬼#8Rオーガ・ロッソ#》シグムント。\x02\x03",

            "#00301F《闘神》と《猟兵王》に\x01",
            "匹敵するほどの化物だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x10,
        (
            "#5P#01400Fその３人は特に有名だろう。\x02\x03",

            "#01403F──話を聞く限りでは、\x01",
            "俺ですら太刀打ちできるかどうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0407
    ChrTalk(
        0x101,
        "#12P#00011Fそ、そんな……！\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x102,
        (
            "#12P#00105F《風の剣聖》が\x01",
            "太刀打ちできない……？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x8,
        (
            "#04006Fうーん、アタシの見る限りじゃ\x01",
            "五分五分くらいかしら？\x02\x03",

            "#04000F剣士と猟兵じゃ、戦闘スタイルも\x01",
            "得意とする間合いも違ってくるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x104,
        (
            "#00303F……だな。\x02\x03",

            "#00301Fアンタは確かに強いが\x01",
            "叔父貴も正真正銘の化物だ。\x02\x03",

            "やり合えばお互い、\x01",
            "タダじゃすまねえだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x10,
        (
            "#5P#01403Fああ、分かっている。\x02\x03",

            "#01400F──だが必要とあらば\x01",
            "敵対することも有り得るだろう。\x02\x03",

            "問題は彼らが何の目的で\x01",
            "クロスベル入りをしたかだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    Sleep(500)

    #C0412
    ChrTalk(
        0x109,
        "#10106F結局そこですよね……\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x105,
        (
            "#6P#10306Fこれだけ情報を集めても\x01",
            "そこが分からないんじゃねぇ。\x02\x03",

            "#10300F手がかりは帝国政府が\x01",
            "絡んでいるってことくらい？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    #C0414
    ChrTalk(
        0x8,
        (
            "#04001Fそれなんだけど……\x01",
            "一つ、気になる情報があるのよ。\x02\x03",

            "共和国方面でアリオスが\x01",
            "掴んできてくれたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        "#12P#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        "#12P#00101Fどんな情報ですか？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x10,
        (
            "#5P#01403Fああ──《黒月#4Rヘイユエ#》についてだ。\x02\x03",

            "#01401Fどうやら現在、共和国政府が\x01",
            "《黒月》の長老たちと\x01",
            "何かの取引を行っているらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0418
    ChrTalk(
        0x101,
        "#12P#00007F本当ですか……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_CAE2")

    #C0419
    ChrTalk(
        0x102,
        (
            "#12P#00108F《黒月》の長老というと\x01",
            "シン君のおじいさまもそうね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB2C")

    label("loc_CAE2")


    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#00108F《黒月》の長老ということは\x01",
            "より中枢の人物たちですよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB2C")


    #C0421
    ChrTalk(
        0x8,
        (
            "#04006F……それでね。\x01",
            "もう一つのポイントなんだけど。\x02\x03",

            "#04001Fその取引を主導したのが\x01",
            "キリカ・ロウランって女性なの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0422
    ChrTalk(
        0x101,
        "#12P#00011Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        (
            "#12P#00107Fそれって……\x01",
            "まさか、あのキリカさん！？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x105,
        (
            "#6P#10302Fへえ、競売会の時に\x01",
            "見かけた黒髪のお姉さんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10,
        (
            "#5P#01403F実は、彼女は遊撃士協会とも\x01",
            "縁がある人物でな……\x02\x03",

            "リベールのツァイス支部で\x01",
            "受付をしていた経験もある。\x02\x03",

            "#01400Fだが、１年ほど前に引退し、\x01",
            "カルバードの情報機関に移籍した。\x02\x03",

            "その情報機関の名前を\x01",
            "《ロックスミス機関》という。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        "#12P#00006Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x109,
        (
            "#10108Fロックスミス……\x01",
            "共和国の大統領の名前ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#12P#00106F大統領主導で、新たな情報機関が\x01",
            "設立された話は聞きましたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0429
    ChrTalk(
        0x102,
        (
            "#12P#00101Fちょ、ちょっと待ってください！\x02\x03",

            "《赤い星座》と《黒月》は\x01",
            "以前抗争しているんですよね！？\x02\x03",

            "その２つに、ニ大国の諜報関係者が\x01",
            "それぞれ接触しているという事は……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、見事な対立構図が\x01",
            "出来上がりつつあるというわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        "#12P#00013Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x109,
        (
            "#10101Fま、まさかクロスベルの地で\x01",
            "帝国と共和国の代理戦争を……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x8,
        (
            "#04003F当然、その可能性も考えられるわね。\x02\x03",

            "#04001F特に明日からの通商会議では\x01",
            "エレボニアからは宰相に皇子、\x01",
            "カルバードからは大統領が来るわ。\x02\x03",

            "お互い機に乗じて、相手のトップを\x01",
            "抹殺するつもりかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x10,
        (
            "#5P#01403Fだが、それにしてはお互い、\x01",
            "接触を隠していないのは不自然だ。\x02\x03",

            "仮に《黒月》や《赤い星座》が動けば\x01",
            "そうした背景が明るみに出て\x01",
            "国際社会の非難を招き寄せるだろう。\x02\x03",

            "#01400F帝国にしても共和国にしても\x01",
            "それだけのリスクを負うとは思えん。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x109,
        "#10106Fう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x102,
        (
            "#12P#00103F……確かに、短絡的な攻撃を\x01",
            "仕掛ける状況ではありませんね。\x02\x03",

            "#00108Fでも、それならどうして……？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x104,
        (
            "#00306Fクソ、叔父貴ども、\x01",
            "一体何を考えてやがるんだ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0438
    ChrTalk(
        0x101,
        (
            "#12P#00003F──いずれにせよ、\x01",
            "現在出来つつある構図には\x01",
            "何らかの意味があるはずです。\x02\x03",

            "#00008F多分、俺たちが手に入れていない\x01",
            "“欠けたピース”があるはず……\x02\x03",

            "#00001Fそれを掴む必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    #C0439
    ChrTalk(
        0x102,
        "#12P#00105Fあ……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x105,
        "#6P#10302Fフフ、なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x8,
        (
            "#04011Fウフフ、さすがロイド君。\x01",
            "先回りされちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x10,
        (
            "#5P#01404F実は、我々も同じ見解でな。\x02\x03",

            "#01402Fその“欠けたピース”については\x01",
            "ギルドの情報網を駆使して\x01",
            "現在当たりを付けている最中だ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)

    #C0443
    ChrTalk(
        0x101,
        "#12P#00002Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x104,
        (
            "#00300Fそんじゃ、何か判ったら\x01",
            "こっちにも教えてくれんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x8,
        (
            "#04000Fええ、新たな事実が判明しだい、\x01",
            "警察本部にも連絡するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x10,
        (
            "#5P#01402Fお前たちの方でも\x01",
            "何か掴んだら知らせてくれ。\x02\x03",

            "明日からの３日間を\x01",
            "何事もなく乗り切るためにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x101,
        "#12P#00000F了解しました……！\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        (
            "#12P#00102F何か判明したら\x01",
            "すぐにお知らせします。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    #A0449
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ツァイトと共に\x01",
            "キーアとシズクがギルドに戻って来た。\x02\x03",

            "ロイドたちは、父娘水入らずで\x01",
            "夕食に行くというアリオスたちに\x01",
            "別れを告げて支援課に戻る事にした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_BA75 end

    def Function_28_D6CB(): pass

    label("Function_28_D6CB")

    EventBegin(0x0)
    Fade(500)
    OP_68(1000, 1000, 11300, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 900, 0, 10000, 0)
    SetChrPos(0x102, 1500, 0, 9400, 0)
    SetChrPos(0x103, -300, 0, 9300, 0)
    SetChrPos(0x104, -1400, 0, 9350, 45)
    SetChrPos(0x109, 300, 0, 8700, 0)
    SetChrPos(0x105, 900, 0, 8100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x8,
        "#5P#04005Fあら、アナタたち……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        (
            "#12P#00012Fはは……\x01",
            "どうもミシェルさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        (
            "#12P#00106Fその、話を聞いて\x01",
            "ちょっと気になりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x8,
        (
            "#5P#04006Fフウ、イヤね。\x01",
            "催促した形になっちゃって。\x02\x03",

            "#04011Fでもアリガト。\x01",
            "わざわざ来てくれて嬉しいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x104,
        (
            "#6P#00305Fってことは、\x01",
            "まだエオリアさんたちと\x01",
            "連絡が取れてねぇのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x8,
        (
            "#5P#04003Fええ、アリオスたちが\x01",
            "手分けして当たってるけど……\x02\x03",

            "#04008F……本当にもう。\x01",
            "一体何をやってるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x109,
        "#12P#10108Fさすがに心配ですね……\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x105,
        (
            "#12P#10301Fふむ……\x01",
            "エニグマが通じないって事は\x01",
            "自治州外に出ているのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x8,
        (
            "#5P#04006Fアタシもそう思ったんだけど、\x01",
            "駅や空港を利用した記録が\x01",
            "無いみたいなのよねぇ。\x02\x03",

            "#04001Fベルガード門とタングラム門にも\x01",
            "通行記録はないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#12P#00001Fそれは……\x01",
            "さすがにおかしいですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0460
    ChrTalk(
        0x103,
        (
            "#12P#00203F……もし、リンさんたちが\x01",
            "自治州内にいるのであれば……\x02\x03",

            "#00200F何とか居場所を\x01",
            "特定できるかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DBA0():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DBA0)
    Sleep(50)

    def lambda_DBB0():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DBB0)
    Sleep(50)

    def lambda_DBC0():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DBC0)
    Sleep(50)

    def lambda_DBD0():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DBD0)
    Sleep(50)

    def lambda_DBE0():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DBE0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    #C0461
    ChrTalk(
        0x101,
        "#11P#00005F本当か……！？\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        "#5P#04005Fなになに、どういう方法！？\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#12P#00203F確か、エニグマⅡには研究段階の\x01",
            "機能が搭載されていた筈です。\x02\x03",

            "#00200Fその一つが緊急時に\x01",
            "アラート信号を発信する機能です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0464
    ChrTalk(
        0x109,
        "#12P#10105Fええっ？\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x102,
        "#00105Fそ、そうなの？\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x103,
        (
            "#12P#00206Fオーブメント内の予備導力で\x01",
            "一定間隔ごとに特定周波数の\x01",
            "導力波を発信する仕組みですが……\x02\x03",

            "あまりにも弱い導力波なため\x01",
            "実用には至っていないと聞きます。\x02\x03",

            "#00201Fただ、機能そのものは\x01",
            "カットされずに残っているかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x109,
        (
            "#12P#10101Fじゃあ、その微弱な導力波を\x01",
            "何とかキャッチできれば……！\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "#5P#04001Fリンとエオリアの居場所も\x01",
            "特定できるってわけね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x103,
        (
            "#12P#00204F試してみる価値はあるかと。\x02\x03",

            "#00202Fこの機能については\x01",
            "ロバーツ主任が詳しいので\x01",
            "ＩＢＣに行ってみましょう。\x02\x03",

            "たぶん力になってくれる筈です。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#11P#00000F分かった、行ってみよう。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#5P#04006F……済まないわね。\x01",
            "本当に助かっちゃうわ。\x02\x03",

            "#04000F何か分かったら\x01",
            "こちらにも連絡をちょうだい。\x02\x03",

            "場合によったら\x01",
            "アリオスたちを呼び戻すから。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E06A():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E06A)
    Sleep(50)

    def lambda_E07A():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E07A)
    Sleep(50)

    def lambda_E08A():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E08A)
    Sleep(50)

    def lambda_E09A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E09A)
    Sleep(50)

    def lambda_E0AA():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E0AA)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    #C0472
    ChrTalk(
        0x102,
        "#12P#00100F了解しました。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x105,
        (
            "#12P#10302Fさて、それじゃあ\x01",
            "ＩＢＣに行ってみようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 1)
    OP_29(0xA8, 0x4, 0x10)
    OP_29(0xA9, 0x4, 0x2)
    OP_29(0xA9, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_28_D6CB end

    def Function_29_E16C(): pass

    label("Function_29_E16C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(128)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    OP_68(1000, 1000, 11300, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x7)
    SetChrPos(0x101, 900, 0, 10000, 180)
    SetChrPos(0x102, 1500, 0, 9400, 0)
    SetChrPos(0x103, -300, 0, 9300, 0)
    SetChrPos(0x104, -1400, 0, 9350, 45)
    SetChrPos(0x109, 300, 0, 8700, 0)
    SetChrPos(0x105, 900, 0, 8100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_E27C():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E27C)
    Sleep(0)

    def lambda_E28C():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E28C)
    Sleep(0)

    def lambda_E29C():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E29C)
    Sleep(0)

    def lambda_E2AC():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E2AC)
    Sleep(0)

    def lambda_E2BC():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E2BC)
    Sleep(0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_4B(0x8, 0xFF)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0474
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──はい、導力ボートの方は\x01",
            "港湾区の波止場に手配しました。\x02\x03",

            "すぐに乗る事ができると思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0475
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006Fそうか、ありがとう。\x02\x03",

            "#00001Fゴメンな、フラン。\x01",
            "いきなり無理なことを頼んで。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0476
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いえいえ、こういう時こその\x01",
            "皆さんのサポートですから～。\x02\x03",

            "でも、南の湿地帯ですか……\x01",
            "くれぐれも気を付けてくださいね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0477
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000Fああ、肝に銘じるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(128, 1, 50, 0)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0478
    ChrTalk(
        0x109,
        (
            "#12P#10101F何とかボートを\x01",
            "確保できたみたいですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0479
    ChrTalk(
        0x101,
        (
            "#5P#00002Fああ、フランが素早く\x01",
            "手配してくれて助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#5P#04006F──ふう、今回に関しては\x01",
            "頼りきりになっちゃったわね。\x02\x03",

            "#04001Fでも、本当にいいの？\x02\x03",

            "１時間もすればアリオスたちが\x01",
            "戻ってくると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E630():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E630)
    Sleep(50)

    def lambda_E640():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E640)
    Sleep(50)

    def lambda_E650():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E650)
    Sleep(50)

    def lambda_E660():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E660)
    Sleep(50)

    def lambda_E670():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E670)
    Sleep(50)

    def lambda_E680():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E680)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    #C0481
    ChrTalk(
        0x104,
        (
            "#6P#00303Fいや、それだったら\x01",
            "俺たちが先行した方がいいだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x102,
        (
            "#12P#00108Fそうですね……\x01",
            "どんな状況かも判りませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、彼らが戻ってきたら\x01",
            "追いかけるように言っといてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "#5P#04000F……分かったわ。\x02\x03",

            "#04003Fリンにしてもエオリアにしても\x01",
            "Ａ級に迫る凄腕の遊撃士よ。\x02\x03",

            "その２人が連絡も入れずに\x01",
            "揃って足止めされている事実……\x02\x03",

            "#04001F何があるか判らないわ。\x01",
            "くれぐれも気をつけなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#12P#00013Fはい……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    #C0486
    ChrTalk(
        0x103,
        (
            "#6P#00201F準備を整えたら\x01",
            "波止場に行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x165, 0)
    OP_29(0xA9, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_29_E16C end

    def Function_30_E8D6(): pass

    label("Function_30_E8D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(1000, 1000, 10800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -2000, 0, -1500, 0)
    SetChrPos(0x102, -2000, 0, -1500, 0)
    SetChrPos(0x103, -2000, 0, -1500, 0)
    SetChrPos(0x104, -2000, 0, -1500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 2000, 0, 8800, 315)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 1900, 0, 10200, 270)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, -200, 0, 10200, 90)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, -300, 0, 8800, 45)
    OP_4B(0xC, 0xFF)
    StopBGM(0xFA0)
    SetCameraDistance(20500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(300)

    #C0487
    ChrTalk(
        0x101,
        "#00001Fごめんください。\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x102,
        "#00103F失礼します。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7251", 0)
    OP_68(-2000, 1000, 3000, 2000)
    MoveCamera(49, 23, 0, 2000)
    SetCameraDistance(21000, 2000)

    def lambda_EB5C():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_EB5C)
    Sleep(50)

    def lambda_EB6C():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_EB6C)
    Sleep(50)

    def lambda_EB7C():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_EB7C)
    Sleep(50)

    def lambda_EB8C():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_EB8C)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    Sleep(1000)

    def lambda_EBAF():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EBAF)

    def lambda_EBC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EBC9)
    Sleep(600)

    def lambda_EBDD():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EBDD)

    def lambda_EBF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EBF7)
    Sleep(900)

    def lambda_EC0B():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EC0B)

    def lambda_EC25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EC25)
    Sleep(600)

    def lambda_EC39():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EC39)

    def lambda_EC53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EC53)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0489
    ChrTalk(
        0x8,
        "#04005F#6Pアナタ達……\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x9,
        "#6Pやあ、ロイドたちか……\x02",
    )

    CloseMessageWindow()

    def lambda_ECB1():

        label("loc_ECB1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_ECB1")

    QueueWorkItem2(0x9, 2, lambda_ECB1)

    def lambda_ECC3():

        label("loc_ECC3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_ECC3")

    QueueWorkItem2(0xA, 2, lambda_ECC3)

    def lambda_ECD5():

        label("loc_ECD5")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_ECD5")

    QueueWorkItem2(0xC, 2, lambda_ECD5)

    def lambda_ECE7():
        OP_96(0xFE, 0x384, 0x0, 0x206C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECE7)
    Sleep(200)

    def lambda_ED04():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x1E78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED04)
    Sleep(100)

    def lambda_ED21():
        OP_96(0xFE, 0x578, 0x0, 0x1C84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ED21)
    Sleep(100)

    def lambda_ED3E():
        OP_96(0xFE, 0xC8, 0x0, 0x1A90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ED3E)
    Sleep(1500)
    Fade(500)
    OP_68(1000, 1100, 9900, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)

    def lambda_ED8E():
        OP_96(0xFE, 0xA8C, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ED8E)
    Sleep(100)

    def lambda_EDAB():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EDAB)
    WaitChrThread(0x103, 1)
    EndChrThread(0xC, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    #C0491
    ChrTalk(
        0x104,
        (
            "#00306F#12Pやれやれ、揃いも揃って\x01",
            "シケたツラ並べてんな？\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xA,
        (
            "#5P余計なお世話だ……\x01",
            "と言いたいところだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xA,
        "#5P……まあ、否定はせん。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xB,
        (
            "#5Pよりにもよって\x01",
            "何でアリオスさんが……\x02\x03",

            "はあ……寝耳に水すぎるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xC,
        (
            "#5P本当に、そんな気配は\x01",
            "ぜんぜん無かったものね……\x02\x03",

            "強いて言うなら\x01",
            "オルキスタワーを訪れることが\x01",
            "最近多かったくらいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x8,
        (
            "#5P#04006Fそうね……\x01",
            "あくまで今後のギルドの対応を\x01",
            "協議しに行ってたはずだけど。\x02\x03",

            "#04008Fまさかこんな段取りを\x01",
            "話し合っていたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x101,
        (
            "#12P#00006F……実はそのあたりを\x01",
            "お聞きしたくて来たんです。\x02\x03",

            "#00001Fアリオスさんはまだ、\x01",
            "ギルドに所属してるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x8,
        (
            "#5P#04001F……昨夜、いきなり辞表を出して\x01",
            "遊撃士のエンブレムを返してきたわ。\x02\x03",

            "#04006F持っていた仕事は全部片付けて、\x01",
            "今後の対応策も出してくれたのは\x01",
            "いかにも彼らしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x102,
        "#12P#00108Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x103,
        (
            "#12P#00206F確かにアリオスさんらしい\x01",
            "几帳面さですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xA,
        (
            "#5P……だが、このように唐突に\x01",
            "辞めるのはさすがに問題だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xA,
        (
            "#5Pしかも『クロスベル独立国』の\x01",
            "『国防軍』の長官などと……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        (
            "#5P……こう言っては何だけど\x01",
            "エレボニアの反応が恐いわね。\x02\x03",

            "#5P資産凍結なんていう脅迫すら\x01",
            "してしまっている状態だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xB,
        (
            "#5P……そうだね……\x01",
            "共和国の反応も恐いな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C0505
    ChrTalk(
        0x9,
        (
            "#11P……だが……\x01",
            "アリオスさんの気持ちも\x01",
            "理解できないわけじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1800, 1100, 9580, 1000)
    MoveCamera(41, 17, 0, 1000)

    def lambda_F37E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F37E)
    Sleep(50)

    def lambda_F38E():
        TurnDirection(0xB, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_F38E)
    Sleep(50)

    def lambda_F39E():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_F39E)
    Sleep(50)

    def lambda_F3AE():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F3AE)
    Sleep(50)

    def lambda_F3BE():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F3BE)
    Sleep(50)

    def lambda_F3CE():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F3CE)
    Sleep(50)

    def lambda_F3DE():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F3DE)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    OP_6F(0x79)

    #C0506
    ChrTalk(
        0xA,
        "#5Pスコット……？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xB,
        "#5Pどういうこと？\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x9,
        (
            "#11P俺もアリオスさんと同じ\x01",
            "クロスベル市の出身だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x9,
        (
            "#11P確かに、演説にもあったような\x01",
            "原因不明の不可解な事故は\x01",
            "年に１、２回は起きていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x9,
        (
            "#11P本当の事は判らないけど……\x01",
            "皆、帝国か共和国がらみで\x01",
            "起きた事だとは薄々感じていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xA,
        "#5P…………それは……………\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xB,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x9,
        (
            "#11Pまあ、ここ最近は\x01",
            "そうした事故は起きてないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x9,
        (
            "#11P５年前、アリオスさんの奥さんと\x01",
            "シズクちゃんが巻き込まれた事故が\x01",
            "最後と言えるかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0515
    ChrTalk(
        0x101,
        "#6P#00011Fあ……\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xC,
        "#5Pひょっとして……\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "#5P#04003F……５年前に表通りで起きた\x01",
            "運搬車の爆発・炎上事故……\x02\x03",

            "#04008F当初は導力機関#8Rオーバルエンジン#の暴走と\x01",
            "可燃性の積荷が原因とされたけど……\x01",
            "確かに不審な点は多すぎたわ。\x02\x03",

            "#04001Fそして、その事故に巻き込まれて\x01",
            "奥さんのサヤさんは亡くなり……\x01",
            "シズクちゃんは光を失った。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x104,
        "#12P#00301Fそういう顛末だったのかよ……\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x103,
        (
            "#6P#00208F……断片的な情報は\x01",
            "ある程度は聞いていましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x102,
        (
            "#6P#00106Fそれでアリオスさんは\x01",
            "警察を辞めてギルドに移って……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "#5P#04006Fアタシもアリオスとは\x01",
            "その後からの付き合いだけど……\x02\x03",

            "彼、一言も言わなかったけど\x01",
            "ずっと引っかかってたんでしょうね。\x02\x03",

            "#04008F……そう考えると\x01",
            "今回の大役を引き受けたのも\x01",
            "ようやく腑に落ちた気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        "#6P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_68(1000, 1100, 9900, 1000)
    MoveCamera(41, 17, 0, 1000)
    TurnDirection(0x101, 0x8, 500)
    OP_6F(0x79)

    #C0523
    ChrTalk(
        0x101,
        (
            "#12P#00003F──ミシェルさん。\x02\x03",

            "#00001F失礼は承知で尋ねますが……\x01",
            "アリオスさんのスケジュールで\x01",
            "不審な点はありませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA6C():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_FA6C)
    Sleep(50)

    def lambda_FA7C():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_FA7C)
    Sleep(50)

    def lambda_FA8C():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_FA8C)
    Sleep(50)

    def lambda_FA9C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FA9C)
    Sleep(50)

    def lambda_FAAC():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FAAC)
    Sleep(50)

    def lambda_FABC():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FABC)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0524
    ChrTalk(
        0x8,
        "#5P#04005Fえ。\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xC,
        "#5Pロイド君、どういうこと？\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        (
            "#12P#00006F『国防軍』の司令長官……\x02\x03",

            "いきなり引き受けるには\x01",
            "あまりに重過ぎる役目だと思います。\x02\x03",

            "#00001F多分、ディーター市長……\x01",
            "いや大統領との間で根回しが\x01",
            "されていたんじゃないですか？\x02\x03",

            "それも最近#4R㈲　㈲#ではなく、しばらく前#10R㈲　㈲　㈲　㈲　㈲#から。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        "#5P#04008F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_FC42():
        TurnDirection(0xB, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_FC42)
    Sleep(50)

    def lambda_FC52():
        TurnDirection(0xA, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_FC52)
    Sleep(50)

    def lambda_FC62():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_FC62)
    Sleep(50)

    def lambda_FC72():
        TurnDirection(0xC, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_FC72)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    def lambda_FC92():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FC92)

    def lambda_FC9F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FC9F)

    def lambda_FCAC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FCAC)

    #C0528
    ChrTalk(
        0xB,
        "#12Pミシェル……？\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xA,
        "まさか……本当なのか？\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x8,
        (
            "#5P#04006F……確かに、行き先など、\x01",
            "報告と食い違っていることは\x01",
            "たまにあったわ。\x02\x03",

            "#04008Fあれだけ仕事を抱えてたら\x01",
            "当然だとは思ってたけど……\x02\x03",

            "#04001F……考えてみれば、\x01",
            "アリオスが報告を間違うなんて\x01",
            "不自然極まりないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x9,
        (
            "それじゃあ、そうした時間に\x01",
            "ディーター市長とコンタクトを？\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x8,
        (
            "#5P#04003F……その可能性は\x01",
            "考えられるかもしれない。\x02\x03",

            "#04001Fロイド君、さすがね。\x01",
            "恐いくらいの洞察力だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        (
            "#12P#00006Fいえ……\x01",
            "失礼な事を言ってすみません。\x02\x03",

            "#00003Fその、失礼ついでに\x01",
            "お聞きしますけど……\x02\x03",

            "#00008Fそうしたアリオスさんの行き先や\x01",
            "スケジュールの食い違い──\x02\x03",

            "#00013F半年以上前#10R㈲　㈲　㈲　㈲　㈲#で\x01",
            "覚えはありませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_FFF8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FFF8)

    def lambda_10005():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10005)
    Sleep(50)

    def lambda_10015():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_10015)
    Sleep(50)

    def lambda_10025():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10025)
    Sleep(50)

    def lambda_10035():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_10035)
    Sleep(50)

    def lambda_10045():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10045)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x104, 0)

    #C0534
    ChrTalk(
        0x102,
        "#6P#00105F半年以上前って……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#12P#00200F……まだディーターさんが\x01",
            "市長にもなっていませんが？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x8,
        (
            "#5P#04006Fう、うーん……\x01",
            "そこまで前だとさすがに\x01",
            "覚えてないんだけど……\x02\x03",

            "#04005Fあ、でもあれがあったか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1013C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1013C)
    Sleep(50)

    def lambda_1014C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1014C)

    def lambda_10159():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10159)

    #C0537
    ChrTalk(
        0x101,
        "#12P#00005Fあれ……？\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x8,
        (
            "#5P#04004F創立記念祭の最終日よ。\x02\x03",

            "#04000F彼、仕事でレミフェリアに\x01",
            "出張する事になってたんだけど……\x02\x03",

            "それを急遽#4Rきゅうきょ#、キャンセルしたのを\x01",
            "報告し損なってたのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0539
    ChrTalk(
        0x101,
        "#12P#00011Fえ……\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x8,
        (
            "#5P#04005F後で気付いて聞いてみたら\x01",
            "忙しくて報告し損なってたって\x01",
            "言ってたけど……\x02\x03",

            "#04001F……なに、何か気になるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xB,
        (
            "#5Pまあ、あの記念祭は\x01",
            "殺人的な忙しさだったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xA,
        (
            "#5P報告に齟齬があったとしても\x01",
            "無理もないと思うが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x101,
        "#11P#00008F#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        "#6P#00108F……記念祭の最終日……\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x103,
        (
            "#12P#00201F最終日といえば\x01",
            "“あれ”がありましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#00301F#12Pそれがどう繋がるってんだ？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#11P#00006F……分からない。\x01",
            "でも何か繋がりそうな気がする。\x02\x03",

            "#00008F今まで俺たちが、忙しさのあまり、\x01",
            "見過ごしていた点と点が……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_104FE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_104FE)
    Sleep(50)

    def lambda_1050E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1050E)

    #C0548
    ChrTalk(
        0x101,
        "#12P#00011Fすみません、失礼します。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0549
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001Fはい、こちらクロスベル警察、\x01",
            "特務支援課で──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0550
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "んー？\x01",
            "『クロスベル国防軍、特務支援課』の\x01",
            "間違いじゃないのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0551
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F……あなたは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0552
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフフ……\x01",
            "サテワタシハダレデショウ？\x02\x03",

            "セイカイサレタカタニハ\x01",
            "モレナクゴウカケイヒンヲ──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0553
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006F……下らないクイズは結構です。\x02\x03",

            "#00010F一体どのツラをさげて……\x01",
            "クロスベルにやって来たんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0554
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やれやれ、嫌われたモンだなァ。\x02\x03",

            "派手な事になってるみたいだが\x01",
            "ちょっと会って話せないか？\x02\x03",

            "ま、損はさせないと思うぜぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0555
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F…………………………………\x02\x03",

            "#00006F……分かりました。\x01",
            "どこに行けばいいんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0556
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《クリムゾン商会》……\x01",
            "いや元《ルバーチェ商会》と\x01",
            "言った方がいいか。\x02\x03",

            "あそこの会長室にするか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0557
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00008F地下のあそこですか……\x01",
            "分かりました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そんじゃ待ってるぜ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0559
    ChrTalk(
        0x102,
        (
            "#6P#00101Fもしかして……\x01",
            "行方不明のツァオ氏とか？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x103,
        (
            "#12P#00200Fそういえばこの前、\x01",
            "ランディさんが居なくなった時、\x01",
            "連絡をもらいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x104,
        "#00305Fそうだったのか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    #C0562
    ChrTalk(
        0x101,
        (
            "#5P#00003F──いや、違う。\x02\x03",

            "#00013F帝国軍のレクター大尉だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0563
    ChrTalk(
        0x102,
        "#6P#00107Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#12P#00211Fあの人……またクロスベルに\x01",
            "来ていたんですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x104,
        (
            "#00301F#12P……確かに\x01",
            "どのツラ下げてって感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x101,
        (
            "#5P#00006Fどうやら旧ルバーチェ商会で\x01",
            "話があるみたいだ。\x02\x03",

            "#00001F《赤い星座》との繋がりを考えると\x01",
            "とても油断はできないけど……\x01",
            "行くだけ行ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x104,
        "#00306F#12Pだな……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x103,
        "#12P#00201F虎穴に入らずんば、ですね。\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x102,
        (
            "#6P#00103F……準備だけは\x01",
            "万全にした方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x8,
        "#5P#04006Fアナタ達も大変そうねぇ……\x02",
    )

    CloseMessageWindow()

    def lambda_10CF1():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10CF1)
    Sleep(50)

    def lambda_10D01():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10D01)
    Sleep(50)

    def lambda_10D11():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10D11)
    Sleep(50)

    def lambda_10D21():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10D21)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0571
    ChrTalk(
        0x9,
        (
            "#11Pどうやら面倒な相手と\x01",
            "やり合うみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "#5P情報局のアランドールか……\x01",
            "恐ろしく厄介な若造らしいが。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xB,
        (
            "#5P厳しそうなら助太刀するから\x01",
            "遠慮なく言ってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xC,
        (
            "#5Pそうね。\x01",
            "湿地帯での借りもあるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x102,
        "#12P#00102Fありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x103,
        (
            "#12P#00204F手に負えなさそうだったら\x01",
            "是非、力を貸してください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2220, 0, 4610, 90)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, 3840, 0, 4540, 270)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xC, -6000, 150, 43030, 180)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0x9, -5030, 0, 52190, 0)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x40)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 1000, 0, 9000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 2)
    OP_29(0xAD, 0x1, 0x1)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_30_E8D6 end

    def Function_31_10F5F(): pass

    label("Function_31_10F5F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 3800, 0, 13900, 90)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 2900, 0, 15300, 135)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 1600, 0, 14900, 135)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, 2200, 0, 13700, 90)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, 2400, 0, 12600, 90)
    OP_4B(0xC, 0xFF)
    OP_68(4600, 1000, 13900, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(4600, 1000, 13900, 10000)
    MoveCamera(41, 23, 0, 10000)
    SetCameraDistance(18500, 10000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(180, 20, -1, -1)
    SetChrName("マクダエル議長")

    #A0577
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W──ならば独立の意志を問う、\x01",
            "住民投票が根拠となるでしょうか？\x02\x03",

            "いいえ、かの住民投票は\x01",
            "“決意表明”を行うかどうかを\x01",
            "問うものでしかなかった筈です。\x02\x03",

            "国防軍やクロスベル独立国……\x02\x03",

            "まして大統領制などの正当性に\x01",
            "結びつくものでは決してありません！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_10F5F end

    def Function_32_111D0(): pass

    label("Function_32_111D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3020, 1700, 4270, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22460, 0)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11351")
    SetChrPos(0x101, -2740, 0, -2360, 0)
    SetChrPos(0x104, -1610, 0, -2360, 0)
    SetChrPos(0x1A2, -2510, 0, -2560, 0)
    SetChrPos(0x102, -1940, 0, -2360, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1129C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1129C)

    def lambda_112AD():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_112AD)
    Sleep(50)

    def lambda_112CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_112CA)

    def lambda_112DB():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_112DB)
    Sleep(700)

    def lambda_112F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_112F8)

    def lambda_11309():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11309)
    Sleep(50)

    def lambda_11326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_11326)

    def lambda_11337():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_11337)
    Jump("loc_115D2")

    label("loc_11351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11494")
    SetChrPos(0x101, -2740, 0, -2360, 0)
    SetChrPos(0x109, -1610, 0, -2360, 0)
    SetChrPos(0x1A2, -2510, 0, -2560, 0)
    SetChrPos(0x102, -1940, 0, -2360, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_113DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_113DF)

    def lambda_113F0():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113F0)
    Sleep(50)

    def lambda_1140D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1140D)

    def lambda_1141E():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1141E)
    Sleep(700)

    def lambda_1143B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1143B)

    def lambda_1144C():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1144C)
    Sleep(50)

    def lambda_11469():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_11469)

    def lambda_1147A():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1147A)
    Jump("loc_115D2")

    label("loc_11494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_115D2")
    SetChrPos(0x101, -2740, 0, -2360, 0)
    SetChrPos(0x105, -1610, 0, -2360, 0)
    SetChrPos(0x1A2, -2510, 0, -2560, 0)
    SetChrPos(0x102, -1940, 0, -2360, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_11522():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11522)

    def lambda_11533():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11533)
    Sleep(50)

    def lambda_11550():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11550)

    def lambda_11561():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11561)
    Sleep(700)

    def lambda_1157E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1157E)

    def lambda_1158F():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1158F)
    Sleep(50)

    def lambda_115AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_115AC)

    def lambda_115BD():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_115BD)

    label("loc_115D2")

    OP_68(-2140, 1300, 5160, 3000)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    #C0578
    ChrTalk(
        0x1A2,
        (
            "#12Pここが遊撃士協会・\x01",
            "クロスベル支部……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0579
    ChrTalk(
        0x101,
        (
            "#5P#00005F……シン？\x01",
            "影に隠れてどうしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11683")

    def lambda_11663():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11663)
    Sleep(50)

    def lambda_11673():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11673)
    Sleep(300)
    Jump("loc_116DA")

    label("loc_11683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_116B1")

    def lambda_11691():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11691)
    Sleep(50)

    def lambda_116A1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_116A1)
    Sleep(300)
    Jump("loc_116DA")

    label("loc_116B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_116DA")

    def lambda_116BF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_116BF)
    Sleep(50)

    def lambda_116CF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_116CF)
    Sleep(300)

    label("loc_116DA")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0580
    ChrTalk(
        0x1A2,
        "#12Pう、うるさい、別にいいだろ……！\x02",
    )

    CloseMessageWindow()
    OP_64(0x1A2)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    #C0581
    ChrTalk(
        0x8,
        (
            "#5P#N#04005Fあら、あなたたち……\x01",
            "可愛いボウヤを連れてどうしたの？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_117C1")

    def lambda_11791():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11791)
    Sleep(50)

    def lambda_117A1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117A1)
    Sleep(50)

    def lambda_117B1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_117B1)
    Sleep(300)
    Jump("loc_11838")

    label("loc_117C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_117FF")

    def lambda_117CF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_117CF)
    Sleep(50)

    def lambda_117DF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117DF)
    Sleep(50)

    def lambda_117EF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_117EF)
    Sleep(300)
    Jump("loc_11838")

    label("loc_117FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11838")

    def lambda_1180D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1180D)
    Sleep(50)

    def lambda_1181D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1181D)
    Sleep(50)

    def lambda_1182D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1182D)
    Sleep(300)

    label("loc_11838")


    #C0582
    ChrTalk(
        0x8,
        (
            "#5P#N#04000Fそんな所じゃ邪魔になるから\x01",
            "こちらにいらっしゃいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0583
    ChrTalk(
        0x102,
        "#12P#00105Fは、はい……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(330, 1300, 10820, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21390, 0)
    OP_93(0x8, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11999")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x104, 1640, 0, 8800, 0)

    def lambda_11928():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_11928)
    Sleep(50)

    def lambda_11945():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11945)
    Sleep(50)

    def lambda_11962():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11962)
    Sleep(50)

    def lambda_1197F():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1197F)
    Jump("loc_11B1A")

    label("loc_11999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11A5C")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x109, 1640, 0, 8800, 0)

    def lambda_119EB():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_119EB)
    Sleep(50)

    def lambda_11A08():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11A08)
    Sleep(50)

    def lambda_11A25():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A25)
    Sleep(50)

    def lambda_11A42():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11A42)
    Jump("loc_11B1A")

    label("loc_11A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11B1A")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x105, 1640, 0, 8800, 0)

    def lambda_11AAE():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_11AAE)
    Sleep(50)

    def lambda_11ACB():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11ACB)
    Sleep(50)

    def lambda_11AE8():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11AE8)
    Sleep(50)

    def lambda_11B05():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11B05)

    label("loc_11B1A")

    OP_0D()
    WaitChrThread(0x101, 1)

    #C0584
    ChrTalk(
        0x8,
        (
            "#04000F#5Pで、そのボウヤは\x01",
            "いったい誰なのかしら？\x02\x03",

            "#04005Fもしかして、\x01",
            "迷子の親探しでもしてた？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        "#12P#00012Fえっと、なんていうか……\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x1A2,
        (
            "#12Pお、おい、お前！\x01",
            "《風の剣聖》は今いるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x8,
        (
            "#04004F#5Pあら、お前とは随分な言い方ねえ。\x02\x03",

            "#04000Fまあ、アリオスなら留守にしてるけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x1A2,
        "#12Pそ、そうか……ほっ。\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x8,
        (
            "#04005F#5Pなんで、安心してるのよ。\x02\x03",

            "#04003Fふむ、その言動にその身なり……\x02\x03",

            "#04000Fなるほど――\x01",
            "このボウヤは《黒月》の関係者ね。\x01",
            "それも長老の孫かしら。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11D6A")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_11E47")

    label("loc_11D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11DDB")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_11E47")

    label("loc_11DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11E47")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_11E47")


    #C0590
    ChrTalk(
        0x102,
        "#12P#00105Fど、どうしてそれを……？\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x8,
        (
            "#04011F#5Pうふふ、カマかけが\x01",
            "見事に当たったみたいね。\x02\x03",

            "#04001Fあ、ちなみにオカマが\x01",
            "カマかけたなんて思っちゃダメよ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11F5A")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_12037")

    label("loc_11F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11FCB")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_12037")

    label("loc_11FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12037")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_12037")


    #C0592
    ChrTalk(
        0x101,
        "#12P#00012Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x1A2,
        (
            "#12Pくっ、こいつ見た目も中身も\x01",
            "タダモノじゃないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x1A2,
        (
            "#12Pこれだから\x01",
            "遊撃士協会ってヤツは……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x8,
        (
            "#04006F#5Pう～ん、さっきから失礼が\x01",
            "過ぎるのはおいといて。\x01",
            "この子も立派に《黒月》なのねえ。\x02\x03",

            "#04008F何だか末恐ろしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12166")

    #C0596
    ChrTalk(
        0x104,
        "#12P#00303Fああ、同感だぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_121BF")

    label("loc_12166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12195")

    #C0597
    ChrTalk(
        0x109,
        "#12P#10106Fええ、同感です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_121BF")

    label("loc_12195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_121BF")

    #C0598
    ChrTalk(
        0x105,
        "#12P#10304Fフフ、同感だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_121BF")


    #C0599
    ChrTalk(
        0x8,
        (
            "#04000F#5Pそれにしても、どうして\x01",
            "アリオスのことを\x01",
            "そこまで警戒するのかしら？\x02\x03",

            "別に私たちも、はっきり《黒月》と\x01",
            "敵対しているわけじゃないんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x1A2,
        (
            "#12Pフ、フン……\x01",
            "これまでにおじいさまたちの\x01",
            "邪魔を何度もしておいてよく言うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x1A2,
        (
            "#12P《風の剣聖》やら《不動》やらのせいで\x01",
            "ウチがどれだけソンシツを被ったか――\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        "#6P#00005F《不動》……？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x8,
        (
            "#04004F#5Pええ、《不動》のジン――\x02\x03",

            "#04000F共和国のＡ級遊撃士で\x01",
            "《泰斗流》という古武術の達人なのよ。\x02\x03",

            "最近はめっきりだけど、\x01",
            "このクロスベル支部にも過去に\x01",
            "何度か手伝いに来てくれているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x102,
        (
            "#12P#00105F《泰斗流》というと、\x01",
            "確かリンさんの……\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x8,
        (
            "#04000F#5Pええ、彼はリンの兄弟子に当たるわ。\x01",
            "当然ながら実力も凄まじいわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_124B2")

    #C0606
    ChrTalk(
        0x104,
        (
            "#12P#00300Fなるほどな、流石に\x01",
            "ギルドも役者が揃ってやがる。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1253D")

    label("loc_124B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_124FA")

    #C0607
    ChrTalk(
        0x109,
        (
            "#12P#10100Fなるほど、流石に\x01",
            "ギルドも凄腕揃いですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1253D")

    label("loc_124FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1253D")

    #C0608
    ChrTalk(
        0x105,
        (
            "#12P#10300Fフフ、流石に\x01",
            "ギルドも役者が揃ってるよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1253D")


    #C0609
    ChrTalk(
        0x1A2,
        (
            "#12Pそれもそうだが、\x01",
            "ギルドが本当に面倒なのは\x01",
            "あのキヤクってヤツのせいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x1A2,
        (
            "#12P大ゲンソクかなんか知らないが、\x01",
            "『民間人の保護』ってのをタテにして\x01",
            "やりたい放題がすぎるだろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x8,
        (
            "#04004F#5Pふふ、まあその原則に従えば、\x01",
            "時には『国家権力への不干渉』だって\x01",
            "その限りではないからね。\x02\x03",

            "#04005F――ってボウヤ、\x01",
            "そのトシでどこまで物知りなのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        (
            "#12P#00000F確かに……\x01",
            "正直ここまでとは思ってなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x1A2,
        (
            "#12Pフフン、ほめたって何もでないぞ。\x01",
            "とにかくギルドの連中なんてのは――\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x8,
        (
            "#04006F#5Pはいはい、ギルド批判も結構だけど\x01",
            "子供は子供らしくするものよ。\x02\x03",

            "#04000Fということで、今は２階に\x01",
            "キーアちゃんとシズクちゃんがいるから。\x02\x03",

            "仲良くお喋りでもしていらっしゃい。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、そういえば\x01",
            "キーアがお邪魔していましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x102,
        (
            "#12P#00100Fそうですね、ここは子供同士\x01",
            "少し相手をしてもらいましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x1A2,
        "#12Pな、なんだ……ダレだよ、それ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x153, 7)
    OP_29(0x73, 0x1, 0x5)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 800, 0, 8760, 0)
    EventEnd(0x5)
    Return()

    # Function_32_111D0 end

    def Function_33_128C4(): pass

    label("Function_33_128C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1940, 1100, 44370, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20320, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1292E")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")

    label("loc_1292E")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12988")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x104, -2190, 0, 45050, 90)
    Jump("loc_12A27")

    label("loc_12988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_129DA")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x109, -2190, 0, 45050, 90)
    Jump("loc_12A27")

    label("loc_129DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12A27")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x105, -2190, 0, 45050, 90)

    label("loc_12A27")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_END)), "loc_12AC4")

    def lambda_12A36():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12A36)
    Sleep(50)

    def lambda_12A46():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_12A46)
    Sleep(300)

    #C0618
    ChrTalk(
        0xD,
        (
            "#11P#01102Fあ、ロイドたち。\x01",
            "えへへ、どーしたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xE,
        (
            "#11P#06002Fお疲れさまです。\x01",
            "お仕事中みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C77")

    label("loc_12AC4")

    SetScenarioFlags(0x14D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)

    #C0620
    ChrTalk(
        0xD,
        "#11P#01110Fあっ、ロイドたちだー！\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(300)

    #C0621
    ChrTalk(
        0xE,
        (
            "#11P#06002Fあっ……\x01",
            "こんにちは、みなさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x101,
        (
            "#6P#00000Fやあ、キーア。\x01",
            "楽しんでるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x102,
        "#6P#00102Fシズクちゃんも久しぶりね。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0624
    AnonymousTalk(
        0xE,
        (
            "ふふ、お久しぶりです。\x02\x03",

            "皆さんはどうやら\x01",
            "お仕事中みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_12C77")


    #C0625
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、一応は\x01",
            "そう言えなくもないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x1A2,
        (
            "#6Pなんだ、そのコドモたちは。\x01",
            "お前たちのシリアイなのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0627
    ChrTalk(
        0xD,
        (
            "#11P#01105Fあれ～？\x01",
            "そのコ、だれー？\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xE,
        "#11P#06005F小さな男の子……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0629
    ChrTalk(
        0x1A2,
        "#6Pち、小さな男の子とはなんだ！\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x1A2,
        (
            "#6Pボクはシン！\x01",
            "《黒月》長老の孫にして\x01",
            "将来を背負うオトコなんだぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xE,
        "#11P#06010Fご、ごめんなさい。\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xD,
        (
            "#11P#01105Fへー、ちっちゃいけど\x01",
            "ロイドたちと同じオトナなんだー。\x02\x03",

            "#01109Fそんなにちっちゃいのに\x01",
            "えらいんだね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x1A2,
        "#6Pち、ちっちゃいちっちゃい言うなぁ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12F50")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    #C0634
    ChrTalk(
        0x104,
        (
            "#11P#00304Fはは、キー坊にかかったら\x01",
            "生意気坊主も形ナシだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13089")

    label("loc_12F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12FE7")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    #C0635
    ChrTalk(
        0x109,
        (
            "#11P#10109Fあはは……\x01",
            "（さすがキーアちゃん。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13089")

    label("loc_12FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_13089")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    #C0636
    ChrTalk(
        0x105,
        (
            "#11P#10309Fフフ、キーアにかかったら\x01",
            "黒月の御曹司も形なしだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13089")

    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0637
    ChrTalk(
        0x102,
        (
            "#5P#00109Fふふっ、シン君。\x02\x03",

            "こちらはキーアちゃんに\x01",
            "シズクちゃんていうの。\x02\x03",

            "#00100F２人とも、シン君より少し\x01",
            "お姉さんになるのかしら？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0638
    ChrTalk(
        0x101,
        (
            "#11P#00000Fあ、ちなみにシズクちゃんは\x01",
            "さっき言っていたアリオスさんの\x01",
            "娘さんになるんだぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0639
    ChrTalk(
        0x1A2,
        "#6Pか、《風の剣聖》の……！\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x1A2,
        (
            "#6Pや、やっぱりムスメのほうも\x01",
            "剣のたつじんだったりするのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x1A2,
        (
            "#6Pもしかして目をつむってるのも\x01",
            "《しんがん》の訓練のためとか！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_132A2")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1334F")

    label("loc_132A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_132FB")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1334F")

    label("loc_132FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1334F")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_1334F")


    #C0642
    ChrTalk(
        0xD,
        "#11P#01105Fしんがん～？\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#11P#00005F《心眼》か……\x01",
            "よくそんな言葉知ってるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xE,
        (
            "#11P#06002Fあはは……\x01",
            "あの、わたし目が見えなくて。\x02\x03",

            "おかげで耳はいい方だけど\x01",
            "お父さんみたいに凄くないよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0645
    ChrTalk(
        0x1A2,
        "#6Pそ、それは失礼した！\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x1A2,
        (
            "#6P紳士にあるまじきことを……\x01",
            "どうかゆるしてほしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xE,
        "#11P#06002Fふふっ、気にしてないよ。\x02",
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x101,
        "#11P#00005F（へえ……）\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        (
            "#6P#00102F（ふふっ、やっぱり\x01",
            "  根はいい子みたいね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 0)
    OP_29(0x73, 0x1, 0x6)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2720, 0, 44250, 90)
    EventEnd(0x5)
    Return()

    # Function_33_128C4 end

    def Function_34_13558(): pass

    label("Function_34_13558")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")
    OP_68(-1940, 1100, 44370, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -2200, 0, 45100, 90)
    SetChrPos(0x102, -2200, 0, 43900, 90)
    SetChrPos(0x104, -3400, 0, 45300, 90)
    SetChrPos(0x109, -3400, 0, 43700, 90)
    SetChrPos(0x105, -4600, 0, 44500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0xD, 0xFF)
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xD, 0x10E, 0x1F4)

    #C0650
    ChrTalk(
        0xD,
        "#11P#01110Fあっ、ロイドたちだー！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 0xFF)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)

    #C0651
    ChrTalk(
        0xE,
        (
            "#11P#06002Fあっ……\x01",
            "こんにちは、みなさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x101,
        (
            "#6P#00000Fやあ、キーア。\x01",
            "楽しんでるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x102,
        "#6P#00100Fシズクちゃんも久しぶりね。\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xE,
        "#11P#06000Fふふ、お久しぶりです。\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x105,
        (
            "#6P#10305Fへえ、この子が\x01",
            "《風の剣聖》の娘さんか。\x02\x03",

            "#10309Fフフ、聞いていたとおり\x01",
            "可愛い子じゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_139BA")

    #C0656
    ChrTalk(
        0x109,
        "#6P#10109Fね、言ったとおりでしょ？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0657
    ChrTalk(
        0xE,
        (
            "#11P#06005Fこの声は、確か……\x01",
            "ノエルさんですよね？\x02\x03",

            "#06002F前にお父さんへのプレゼントを\x01",
            "一緒に探してくださった。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0658
    ChrTalk(
        0x109,
        (
            "#6P#10105Fわっ、覚えててくれたんだ？\x02\x03",

            "#10109F少ししか会った事ないのに……\x01",
            "ふふっ、嬉しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xE,
        (
            "#11P#06002Fえへへ、キーアちゃんに\x01",
            "新しいメンバーが入ったって\x01",
            "聞いてましたから。\x02\x03",

            "#06000Fそれじゃあ……そちらの方は？\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x105,
        (
            "#6P#10302Fワジ・ヘミスフィアだ。\x01",
            "フフ、よろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B97")

    label("loc_139BA")


    #C0661
    ChrTalk(
        0x109,
        "#6P#10109Fうん、フランの言ってた通りだよ～！\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0662
    ChrTalk(
        0xE,
        (
            "#11P#06005Fえっと……そちらの方々は？\x02\x03",

            "キーアちゃんに新しいメンバーが\x01",
            "入ったって聞いてましたけど、\x01",
            "もしかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x109,
        (
            "#6P#10105Fあ、そういえば初めてだったね。\x02\x03",

            "#10109Fあたしはノエル・シーカー。\x01",
            "フランのお姉さんって言えば\x01",
            "分かるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xE,
        (
            "#11P#06005Fあっ、フランさんの……\x01",
            "そういえばなんだか雰囲気が\x01",
            "似ている気がしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x105,
        (
            "#6P#10302F僕のほうはワジ・ヘミスフィアだ。\x01",
            "フフ、よろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B97")


    #C0666
    ChrTalk(
        0xE,
        (
            "#11P#06002Fはい、こちらこそ\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xD,
        (
            "#11P#01109Fほらほら、シズクも\x01",
            "自己紹介しないとー！\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xE,
        (
            "#11P#06005Fあっ……\x01",
            "そうだね、それじゃあ。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0669
    AnonymousTalk(
        0xE,
        (
            "えっと、キーアちゃんのお友達の\x01",
            "シズク・マクレインって言います。\x02\x03",

            "支援課のみなさんには、お父さん共々\x01",
            "お世話にならせてもらっています。\x02\x03",

            "改めて、よろしくお願いしますね。\x02",
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

    #C0670
    ChrTalk(
        0x102,
        (
            "#6P#00102Fあはは、まあ……\x01",
            "アリオスさんにお世話になってるのは\x01",
            "むしろこちらの方なんだけれどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x101,
        "#6P#00003Fうーん、それは言えてるなあ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0672
    ChrTalk(
        0xE,
        (
            "#11P#06010Fそ、そんなことないですよ。\x02\x03",

            "前の事件の時には、皆さんに\x01",
            "たくさん助けて頂きましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x104,
        (
            "#6P#00309Fはは、相変わらず\x01",
            "しっかりした子だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xD,
        (
            "#11P#01102Fねー、みんなも\x01",
            "キーアたちと遊んでくのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#6P#00009Fああいや、\x01",
            "シズクちゃんが来てるから\x01",
            "せっかくだし挨拶でもと思ってね。\x02\x03",

            "#00000F俺たちはこのまま仕事に行くから、\x01",
            "今日一日、キーアはシズクちゃんと\x01",
            "ゆっくり楽しんでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xD,
        "#11P#01109Fうん、分かったー！\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xE,
        (
            "#11P#06002Fえっと、皆さんも\x01",
            "お仕事頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x14D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2200, 50, 44500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_34_13558 end

    def Function_35_1403C(): pass

    label("Function_35_1403C")

    EventBegin(0x1)
    SetChrPos(0x0, -2110, 0, 740, 0)
    EventEnd(0x4)
    Return()

    # Function_35_1403C end

    SaveToFile()

Try(main)
