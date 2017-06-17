from ScenarioHelper import *

def main():
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
        "接待员米歇尔",           # 1
        "游击士斯克特",           # 2
        "游击士温蔡尔",           # 3
        "游击士林",               # 4
        "游击士艾欧莉娅",         # 5
        "琪雅",                   # 6
        "滴",                     # 7
        "蔡特",                   # 8
        "亚里欧斯",               # 9
        "雾香",                   # 10
        "椅子",                   # 11
        "椅子",                   # 12
        "椅子",                   # 13
        "椅子",                   # 14
        "椅子",                   # 15
        "椅子",                   # 16
        "椅子",                   # 17
        "椅子",                   # 18
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
        "Function_5_3D49",         # 05, 5
        "Function_6_4438",         # 06, 6
        "Function_7_46E7",         # 07, 7
        "Function_8_4818",         # 08, 8
        "Function_9_4FC7",         # 09, 9
        "Function_10_5564",        # 0A, 10
        "Function_11_5CB9",        # 0B, 11
        "Function_12_612E",        # 0C, 12
        "Function_13_6195",        # 0D, 13
        "Function_14_624D",        # 0E, 14
        "Function_15_6F1B",        # 0F, 15
        "Function_16_6FC2",        # 10, 16
        "Function_17_73DB",        # 11, 17
        "Function_18_7582",        # 12, 18
        "Function_19_77FA",        # 13, 19
        "Function_20_7801",        # 14, 20
        "Function_21_811A",        # 15, 21
        "Function_22_849D",        # 16, 22
        "Function_23_8D9A",        # 17, 23
        "Function_24_9582",        # 18, 24
        "Function_25_A125",        # 19, 25
        "Function_26_A5C5",        # 1A, 26
        "Function_27_A60F",        # 1B, 27
        "Function_28_C057",        # 1C, 28
        "Function_29_CA0A",        # 1D, 29
        "Function_30_D0C4",        # 1E, 30
        "Function_31_F4F9",        # 1F, 31
        "Function_32_F74A",        # 20, 32
        "Function_33_10CFE",       # 21, 33
        "Function_34_118B6",       # 22, 34
        "Function_35_121E0",       # 23, 35
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DD")
    Jump("loc_AAE")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F0")
    Jump("loc_AAE")

    label("loc_9F0")

    TalkBegin(0x8)

    #C0001
    ChrTalk(
        0x8,
        (
            "#04000F对了对了，我最近开始玩\x01",
            "那个叫『波波碰！』的\x01",
            "导力游戏了哦。\x02\x03",

            "#04011F你们也在玩吧？\x01",
            "呵呵，有空的时候\x01",
            "就和我对战吧⊥\x02",
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
            "『米歇尔的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 5)
    OP_E4(0x3)
    TalkEnd(0x8)
    Return()

    label("loc_AAE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D09")

    #C0003
    ChrTalk(
        0x8,
        "#04001F是吗……你们打败了亚里欧斯啊。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00008F……是的，总算赢了。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00306F他可真是强得\x01",
            "让人难以置信呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#04003F……亚里欧斯可是达到了\x01",
            "『理』之境界的真正达人。\x02\x03",

            "那是单纯依靠才能\x01",
            "绝对无法到达……\x01",
            "必须还要经过非同寻常的修炼才能进入的境界。\x02\x03",

            "#04011F呵呵，能跨越这道难关，\x01",
            "说明你们也已经变强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#00204F老实说，其实也有一定的运气因素在内。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#00100F经历了一场严酷的激战，\x01",
            "但总算成功取胜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#04004F呵呵，那接下来就只剩下\x01",
            "琪雅那个孩子啦。\x02\x03",

            "#04000F就算是为了苦苦等待的小滴，\x01",
            "你们也要想方设法把她\x01",
            "和亚里欧斯一起带回来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00000F嗯，一定……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 6)
    Jump("loc_E77")

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8")

    #C0011
    ChrTalk(
        0x8,
        (
            "#04003F亚里欧斯可是达到了\x01",
            "『理』之境界的真正达人。\x02\x03",

            "#04011F呵呵，能跨越这道难关，\x01",
            "说明你们也已经变强了。\x02\x03",

            "#04000F就算是为了苦苦等待的小滴，\x01",
            "你们也要想方设法把亚里欧斯\x01",
            "和那个叫琪雅的孩子一起带回来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E77")

    label("loc_DE8")


    #C0012
    ChrTalk(
        0x8,
        (
            "#04004F呵呵，接下来要做的\x01",
            "就只有带回那个叫琪雅的孩子了。\x02\x03",

            "#04000F就算是为了苦苦等待的小滴，\x01",
            "你们也要想方设法把她\x01",
            "和亚里欧斯一起带回来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E77")

    Jump("loc_3D45")

    label("loc_E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C5")

    #C0013
    ChrTalk(
        0x8,
        (
            "#04000F是你们啊……\x01",
            "拘捕总统的事真是辛苦啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000F协会的各位也是一样，\x01",
            "非常感谢你们的协助。\x02\x03",

            "如果没有大家的帮忙，\x01",
            "是绝对不可能成功的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#04011F呵呵，客气了。\x02\x03",

            "#04004F对于想稳定市内状况的\x01",
            "我们来说，你们的行动\x01",
            "也算是一场及时雨呢。\x02\x03",

            "#04000F多亏你们的努力，\x01",
            "协会也总算可以重新开始行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#00105F如此说来，协会的各位已经……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#04000F嗯，结界消除之后，\x01",
            "他们就分头前往市外了。\x02\x03",

            "#04003F由于这段时间一直不能离开市内，\x01",
            "各地都发生了不少问题，\x01",
            "大量委托全都堆了过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        "#00200F那还真是相当麻烦呢……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#00303F只可惜我们现在\x01",
            "不能帮上忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#04004F不用介意啦，这边的事情交给我们就好。\x02\x03",

            "#04001F至于出现在湿地一带的\x01",
            "那棵神秘莫测的大树……\x01",
            "就全交给你们了。\x02\x03",

            "那才是你们现在\x01",
            "真正重要的任务吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F嗯……没错。\x02\x03",

            "琪雅就在那里……\x01",
            "亚里欧斯先生也在。\x02\x03",

            "#00001F无论如何，我们也要亲手\x01",
            "把他们带回来……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11EF")

    #C0022
    ChrTalk(
        0x10A,
        "#00603F……那当然。\x02",
    )

    CloseMessageWindow()

    label("loc_11EF")


    #C0023
    ChrTalk(
        0x8,
        (
            "#04004F呵呵呵，这才像你们嘛。\x02\x03",

            "#04001F……老实说，我认为亚里欧斯的实力\x01",
            "远不是你们可以相比的。\x02\x03",

            "关于这点，曾经与他一起工作过的我们\x01",
            "是再清楚不过的了。\x02\x03",

            "#04011F加油吧！特别任务支援科！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00001F是！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 5)
    Jump("loc_14B8")

    label("loc_12C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1403")

    #C0025
    ChrTalk(
        0x8,
        (
            "#04003F……老实说，我认为亚里欧斯的实力\x01",
            "远不是你们可以相比的。\x02\x03",

            "#04001F关于这点，曾经与他一起工作过的我们\x01",
            "是再清楚不过的了。\x02\x03",

            "等待着你们的，必定是非常严峻的战斗。\x01",
            "但你们无论如何也要把亚里欧斯\x01",
            "和那个叫琪雅的孩子一起带回来哦。\x02\x03",

            "#04011F呵呵，竟敢这么自作主张地提交辞呈，\x01",
            "必须得好好训斥他一顿才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14B8")

    label("loc_1403")


    #C0026
    ChrTalk(
        0x8,
        (
            "#04003F等待着你们的，必定是非常严峻的战斗。\x01",
            "但你们无论如何也要把亚里欧斯\x01",
            "和那个叫琪雅的孩子一起带回来哦。\x02\x03",

            "#04011F呵呵，竟敢这么自作主张地提交辞呈，\x01",
            "必须得好好训斥他一顿才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B8")

    Jump("loc_3D45")

    label("loc_14BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160E")

    #C0027
    ChrTalk(
        0x8,
        (
            "#04006F自从独立宣言发布之后，\x01",
            "连我们也不能自由行动了。\x02\x03",

            "虽说协会处于中立的立场，\x01",
            "但在行动时终究不能无视克洛斯贝尔\x01",
            "以独立国家的形式而建立起来的秩序。\x02\x03",

            "#04001F不过，只有这次另当别论。\x01",
            "既然已有民间人士陷入危险，\x01",
            "游击士协会就绝不能坐视不理。\x02\x03",

            "#04003F突击兰花塔，逮捕总统\x01",
            "的作战……就让我们也\x01",
            "贡献一份力量吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1664")

    label("loc_160E")


    #C0028
    ChrTalk(
        0x8,
        (
            "#04003F作战开始的时候，\x01",
            "请再与我联络。\x02\x03",

            "#04001F在那之前，\x01",
            "我们会认真做好准备的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1664")

    Jump("loc_3D45")

    label("loc_1669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1756")

    #C0029
    ChrTalk(
        0x8,
        (
            "#04006F呼，没想到亚里欧斯\x01",
            "为了与市长……总统秘密会面，\x01",
            "居然会在行程表上做手脚……\x02\x03",

            "虽然曾经觉得有些不对劲，但一直没有发现问题，\x01",
            "这完全是我的失误啊。\x02\x03",

            "#04008F小滴遭遇的那场事故，\x01",
            "他果然一直都无法释怀吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17EC")

    label("loc_1756")


    #C0030
    ChrTalk(
        0x8,
        (
            "#04003F不管怎么说……既然总统已经发表了独立宣言，\x01",
            "保持中立立场的游击士协会\x01",
            "也必须好好考虑一下今后的对策了。\x02\x03",

            "#04008F另外，也要与总部联络一下……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EC")

    Jump("loc_3D45")

    label("loc_17F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_1D6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_19FD")

    #C0031
    ChrTalk(
        0x8,
        (
            "#04005F哦哦，你们几个……\x01",
            "是不是见到亚里欧斯了？\x02\x03",

            "#04006F呼，他怎么还没回来……\x02",
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
            "#00005F我们刚才在墓地\x01",
            "见到亚里欧斯先生了。\x02\x03",

            "已经转告了\x01",
            "您正在找他的事情……\x01",
            "难道他还没回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04003F嗯，还没有呢……\x01",
            "原来如此，是去墓地了啊。\x02\x03",

            "#04000F……算啦，去给纱绫扫墓\x01",
            "也没什么好奇怪的，\x01",
            "应该快回来了吧。\x02\x03",

            "#04011F真是麻烦你们了啊，\x01",
            "这样就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00012F是、是吗，\x01",
            "那我们就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC9")

    label("loc_19FD")


    #C0035
    ChrTalk(
        0x8,
        (
            "#04005F哦，是你们啊……\x01",
            "有点事情想问问各位。\x02\x03",

            "#04001F你们有没有在什么地方见到过亚里欧斯？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00005F哎……？\x01",
            "亚里欧斯先生吗？\x01",
            "我们刚才在墓地见到他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#00105F他好像正在给\x01",
            "自己的夫人扫墓……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#04000F嗯，他为了与市长协商\x01",
            "游击士协会今后的应对工作，\x01",
            "去了兰花塔……\x02\x03",

            "#04006F在之前那起袭击事件中，\x01",
            "亚里欧斯的艾尼格玛Ⅱ被毁坏了。\x02\x03",

            "自那之后一直都很忙，\x01",
            "所以也没时间准备备用品，\x01",
            "现在和他联系不上，真是头疼。\x02\x03",

            "#04008F差不多也该谈完了，\x01",
            "但愿他能早点回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00300F呼，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#04003F嗯，原来如此……\x01",
            "亚里欧斯去了墓地啊……\x02\x03",

            "#04000F……算啦，去给纱绫扫墓\x01",
            "也没什么好奇怪的，\x01",
            "应该快回来了吧。\x02\x03",

            "#04011F麻烦你们啦，不好意思，\x01",
            "这样就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00012F是、是吗，\x01",
            "那我们就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC9")

    SetScenarioFlags(0x18E, 0)
    Jump("loc_1D68")

    label("loc_1CD1")


    #C0042
    ChrTalk(
        0x8,
        (
            "#04008F克洛斯贝尔已经陷入如此状况，\x01",
            "我们实在是无暇顾及湿地一带的灵智之草\x01",
            "以及有关『结社』方面的问题。\x02\x03",

            "#04006F呼，现在或许应该\x01",
            "向总部请求增援了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D68")

    Jump("loc_3D45")

    label("loc_1D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_212C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC9")

    #C0043
    ChrTalk(
        0x8,
        (
            "#04005F啊，是你们啊……\x01",
            "有点事情想问问各位。\x02\x03",

            "#04001F你们有没有在什么地方见到过亚里欧斯？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#00005F没有，今天没见到过。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00105F亚里欧斯先生\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#04000F嗯，他为了与市长协商\x01",
            "游击士协会今后的应对工作，\x01",
            "去了兰花塔……\x02\x03",

            "#04006F在之前那起袭击事件中，\x01",
            "亚里欧斯的艾尼格玛Ⅱ被毁坏了。\x02\x03",

            "自那之后一直都很忙，\x01",
            "所以也没时间准备备用品，\x01",
            "现在和他联系不上，真是头疼。\x02\x03",

            "#04008F差不多也该谈完了，\x01",
            "但愿他能早点回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#00303F嗯～大概是顺路去了其它地方吧？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00000F明白了，\x01",
            "如果见到亚里欧斯先生，\x01",
            "我们会告知您正在找他。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#04000F嗯，那就太好了，\x01",
            "拜托你们了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 7)
    Jump("loc_2127")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2090")

    #C0050
    ChrTalk(
        0x8,
        (
            "#04003F克洛斯贝尔陷入如此状况，\x01",
            "协会现在也非常繁忙。\x02\x03",

            "#04008F我们实在是无暇顾及\x01",
            "湿地一带的灵智之草\x01",
            "以及有关『结社』方面的问题了……\x02\x03",

            "#04006F呼，现在或许应该\x01",
            "向总部请求增援了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2127")

    label("loc_2090")


    #C0051
    ChrTalk(
        0x8,
        (
            "#04008F克洛斯贝尔已经陷入如此状况，\x01",
            "我们实在是无暇顾及湿地一带的灵智之草\x01",
            "以及有关『结社』方面的问题。\x02\x03",

            "#04006F呼，现在或许应该\x01",
            "向总部请求增援了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2127")

    Jump("loc_3D45")

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_230F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214B")
    TalkEnd(0x8)
    Call(0, 23)
    Return()

    label("loc_214B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226A")

    #C0052
    ChrTalk(
        0x8,
        (
            "#04001F如果这样的状况长期持续，\x01",
            "协会恐怕也不得不展开行动了。\x02\x03",

            "#04003F不过，两大国从以前开始\x01",
            "就一直对警备队的维持治安能力抱有质疑。\x01",
            "如果那样做，就更会成为他们的攻击材料。\x02\x03",

            "#04001F不到万不得已的情况，本不想有所行动……\x01",
            "但考虑到民间人士的安全，实在是不能长期观望啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_230A")

    label("loc_226A")


    #C0053
    ChrTalk(
        0x8,
        (
            "#04001F如果这样的状况长期持续，\x01",
            "协会恐怕也不得不展开行动了。\x02\x03",

            "#04006F不到万不得已的情况，本不想有所行动……\x01",
            "但考虑到民间人士的安全，实在是不能长期观望啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230A")

    Jump("loc_3D45")

    label("loc_230F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_245F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DB")

    #C0054
    ChrTalk(
        0x8,
        (
            "#04003F林和艾欧莉娅两人\x01",
            "都是接近Ａ级水平的优秀游击士。\x02\x03",

            "#04008F那两人竟然会\x01",
            "同时被困在湿地，\x01",
            "连联络都没有发回来……\x02\x03",

            "#04001F目前还不知道发生了什么状况，\x01",
            "请你们一定要小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_245A")

    label("loc_23DB")


    #C0055
    ChrTalk(
        0x8,
        (
            "#04008F林和艾欧莉娅竟然会\x01",
            "同时被困在湿地，\x01",
            "连联络都没有发回来……\x02\x03",

            "#04001F目前还不知道发生了什么状况，\x01",
            "请你们一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_245A")

    Jump("loc_3D45")

    label("loc_245F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_END)), "loc_25C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257B")

    #C0056
    ChrTalk(
        0x8,
        (
            "#04005F啊，是你们……\x01",
            "已经查到林和艾欧莉娅的\x01",
            "所在地了吗？\x02\x03",

            "刚才你们说过可以利用艾尼格玛Ⅱ\x01",
            "的警报功能来找人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#00200F多少还需要做些准备工作，\x01",
            "但应该会有所收获。\x02\x03",

            "得到结果后会马上通知您的，\x01",
            "请再稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#04011F嗯，明白了，\x01",
            "那就拜托你们啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25BB")

    label("loc_257B")


    #C0059
    ChrTalk(
        0x8,
        (
            "#04011F无论如何也请你们要想办法\x01",
            "查明林和艾欧莉娅的所在地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BB")

    Jump("loc_3D45")

    label("loc_25C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2645")

    #C0060
    ChrTalk(
        0x8,
        (
            "#04003F我这边要是了解到了\x01",
            "林和艾欧莉娅的情况，\x01",
            "也会联络你们。\x02\x03",

            "#04001F如果形势需要，\x01",
            "我会把亚里欧斯他们叫回来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D45")

    label("loc_2645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_281B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2796")

    #C0061
    ChrTalk(
        0x8,
        (
            "#04007F刚才接到了联络……\x01",
            "列车竟然发生了事故！？\x02\x03",

            "#04006F唉，这可麻烦了啊。\x01",
            "亚里欧斯他们现在正在调查幻兽，\x01",
            "不能马上回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00003F没关系，调查工作也是很重要的……\x01",
            "这边的事情就交给我们来处理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#04006F唔……没办法呢。\x02\x03",

            "#04000F明白了，脱轨事故就拜托你们来负责了。\x01",
            "如果有什么情况，请立刻通知我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2816")

    label("loc_2796")


    #C0064
    ChrTalk(
        0x8,
        (
            "#04006F亚里欧斯他们现在正在调查幻兽，\x01",
            "不能马上回来……\x02\x03",

            "#04000F脱轨事故就拜托你们来负责了，\x01",
            "如果有什么情况，请立刻通知我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2816")

    Jump("loc_3D45")

    label("loc_281B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF7")

    #C0065
    ChrTalk(
        0x8,
        (
            "#04003F你们提交的报告书中所记录的\x01",
            "那种名为『灵智之草』的蓝花……\x01",
            "竟然会与教会的圣典有所关联。\x02\x03",

            "#04001F谨慎起见，我让斯克特和林他们\x01",
            "也去确认了一下……\x02\x03",

            "结果，在其它几处出现幻兽的地点，\x01",
            "也都有蓝花盛开在附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00203F关于蓝花盛开的原因，\x01",
            "目前还不得而知……\x02\x03",

            "#00200F但通过种种状况来分析，\x01",
            "似乎可以推测它与幻兽的出现\x01",
            "存在着某种程度的因果关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00005F话说回来，协会的调查情况\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#04011F昨天已经将出现的三只幻兽\x01",
            "清除了两只。\x02\x03",

            "#04000F今天会分头行动，\x01",
            "清除剩下的一只幻兽，\x01",
            "并再次调查之前出现幻兽的地点。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00102F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#00300F嗯，说不定幻兽\x01",
            "还会再次突然出现，\x01",
            "一定要多加注意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#04004F嗯，那当然。\x02\x03",

            "#04000F如果掌握到什么情况，会和你们联络的，\x01",
            "也拜托你们继续调查。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 3)
    Jump("loc_2B79")

    label("loc_2AF7")


    #C0072
    ChrTalk(
        0x8,
        (
            "#04000F亚里欧斯今天就能回来了，\x01",
            "这方面的调查就交给我们吧。\x02\x03",

            "#04011F如果掌握到什么情况，会和你们联络的，\x01",
            "也拜托你们继续调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B79")

    Jump("loc_3D45")

    label("loc_2B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEA")

    #C0073
    ChrTalk(
        0x8,
        (
            "#04000F各位，幻兽的事情\x01",
            "就拜托了。\x02\x03",

            "#04006F亚里欧斯如今\x01",
            "无法参加行动，我们的\x01",
            "人手实在不足。\x02\x03",

            "#04000F就请你们和斯克特他们\x01",
            "分担完成任务吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00000F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00106F因为小滴的事情，\x01",
            "亚里欧斯先生现在无暇分身，\x01",
            "这也没有办法呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#04003F各位能理解，那就再好不过了。\x02\x03",

            "#04000F你们就尽自己所能，\x01",
            "努力展开调查\x01",
            "工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D40")

    label("loc_2CEA")


    #C0077
    ChrTalk(
        0x8,
        (
            "#04000F各位，幻兽的事情\x01",
            "就拜托你们了。\x02\x03",

            "你们就尽自己所能，\x01",
            "努力展开调查\x01",
            "工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D40")

    Jump("loc_3D45")

    label("loc_2D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2A")

    #C0078
    ChrTalk(
        0x8,
        (
            "#04000F亚里欧斯今天将要负责\x01",
            "正式会议中的警备工作。\x02\x03",

            "即使保护对象是各国首脑，\x01",
            "应该也没有比这更万全的警备体制了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00000F在这种时候，有站在中立立场的\x01",
            "游击士存在，真是让人倍感放心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#00104F嗯，如果仅有力量，\x01",
            "是无法担当\x01",
            "如此重任的。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#04003F话虽如此，但就算是亚里欧斯，\x01",
            "也不可能单凭一人之力，\x01",
            "在恐怖分子的威胁下保护首脑们。\x02\x03",

            "#04000F警察组织与警备队的协助\x01",
            "是必不可少的，\x01",
            "请认真做好后援工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00000F嗯，我们一定会\x01",
            "毫不松懈地努力警戒。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2FDA")

    label("loc_2F2A")


    #C0083
    ChrTalk(
        0x8,
        (
            "#04005F哦，对了对了，说起来……\x01",
            "听到小缇欧回来的消息之后，\x01",
            "艾欧莉娅非常兴奋呢。\x02\x03",

            "#04011F呵呵，要是在什么地方见到她，\x01",
            "就去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#00206F……嗯，如果有心情的话。\x02",
    )

    CloseMessageWindow()

    label("loc_2FDA")

    Jump("loc_3D45")

    label("loc_2FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3313")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3105")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3013")
    Call(0, 13)
    Jump("loc_308D")

    label("loc_3013")


    #C0085
    ChrTalk(
        0x8,
        (
            "#04000F我已经听亚里欧斯说了哦。\x02\x03",

            "克洛斯贝尔协会\x01",
            "与外国有所联系，\x01",
            "储备着一定的物资。\x02\x03",

            "总之一定不会有事的，\x01",
            "不必担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308D")

    Jump("loc_3101")

    label("loc_3092")


    #C0086
    ChrTalk(
        0x8,
        (
            "#04000F我刚才接到了\x01",
            "亚里欧斯的联络。\x01",
            "听说患者已经得救了。\x02\x03",

            "呵呵，你们也得到了\x01",
            "大公阁下的认可，\x01",
            "真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3101")

    TalkEnd(0x8)
    Return()

    label("loc_3105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329C")

    #C0087
    ChrTalk(
        0x8,
        (
            "#04000F通商会议\x01",
            "终于开始了。\x02\x03",

            "#04003F我们会在进行警戒的同时，\x01",
            "处理各地的委托。\x02\x03",

            "#04000F如果发生了什么情况，\x01",
            "附近的游击士\x01",
            "就会立即赶去。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#00100F真是太可靠了。\x02\x03",

            "#00103F『赤色星座』和『黑月』的\x01",
            "目的都还不甚明了，\x01",
            "我们绝不能掉以轻心……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#04003F嗯，无论他们有何企图，\x01",
            "我们都要做好准备，\x01",
            "重点注意。\x02\x03",

            "#04000F总之，如果了解到什么情况，\x01",
            "我会联络你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00000F嗯，那就拜托了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_330E")

    label("loc_329C")


    #C0091
    ChrTalk(
        0x8,
        (
            "#04000F我们会在进行警戒的同时，\x01",
            "处理各地的委托。\x02\x03",

            "如果掌握到了有关\x01",
            "赤色星座或黑月的情报，\x01",
            "我会与你们联络的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330E")

    Jump("loc_3D45")

    label("loc_3313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33A2")

    #C0092
    ChrTalk(
        0x8,
        (
            "#04006F呼，话说回来，\x01",
            "这孩子竟然是黑月长老的孙子啊。\x02\x03",

            "#04000F该怎么说呢，可真是后生可畏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_33A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_340F")

    #C0093
    ChrTalk(
        0x8,
        (
            "#04000F小琪雅现在正在二层\x01",
            "和小滴一起玩呢。\x02\x03",

            "#04011F我会好好照顾她们两个的，\x01",
            "不用担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_340F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3769")

    #C0094
    ChrTalk(
        0x8,
        (
            "#04000F哦，是你们啊。\x01",
            "小琪雅正在二层\x01",
            "和小滴一起玩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00004F不好意思，给您添麻烦了。\x01",
            "协会现在也非常繁忙吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#04000F哪里的话，我可是无比欢迎的。\x01",
            "屋里的气氛热闹点，\x01",
            "也能让我的心情变好。\x02\x03",

            "#04009F而且，看着这两个孩子，\x01",
            "感觉就好像是自己的两个女儿一样，\x01",
            "人家的母性本能都被激发出来了呢～⊥\x02",
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
        "#00306F母、母性本能吗……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#04001F……怎么，你有意见吗？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00109F这、这个……\x01",
            "话说回来，亚里欧斯先生不在吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "#04000F嗯，他把小滴\x01",
            "从医院带过来之后，\x01",
            "就马上前往共和国了。\x02\x03",

            "#04004F在通商会议召开之前，\x01",
            "他既要处理各种委托，又要去尽力\x01",
            "排除共和国方面的不安定要素。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        "#10106F呼，真不愧是亚里欧斯先生啊……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x105,
        (
            "#10302F看起来，协会对明天的工作\x01",
            "已经有了万全的准备了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#04011F呵呵，你们也要\x01",
            "在今天之内做好\x01",
            "最充足的准备哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 5)
    Jump("loc_37EC")

    label("loc_3769")


    #C0104
    ChrTalk(
        0x8,
        (
            "#04000F小琪雅正在二层\x01",
            "和小滴一起玩呢。\x02\x03",

            "#04011F那两个孩子就交给我吧。\x01",
            "在亚里欧斯从共和国回来之前，\x01",
            "我一定会用心照顾好她们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EC")

    Jump("loc_3D45")

    label("loc_37F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_39AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3903")

    #C0105
    ChrTalk(
        0x8,
        (
            "#04000F最近，通过导力网络\x01",
            "发来的委托也渐渐增多了。\x02\x03",

            "特别是在这种下雨天，\x01",
            "用终端提交的委托就更多。\x02\x03",

            "#04006F不过我们是很忙的，\x01",
            "在接到紧急度比较低的工作时，\x01",
            "也只能推掉。\x02\x03",

            "#04000F我想那种委托有的\x01",
            "可能转到你们支援科去了……\x01",
            "一定要想办法解决掉哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_39A5")

    label("loc_3903")


    #C0106
    ChrTalk(
        0x8,
        (
            "#04006F我们也想尽可能地\x01",
            "解决所有委托。但有时实在太忙，\x01",
            "不得不有所取舍啊。\x02\x03",

            "#04000F一些我们没有处理的委托，\x01",
            "可能转到你们支援科去了……\x01",
            "一定要想办法解决掉哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39A5")

    Jump("loc_3D45")

    label("loc_39AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC0")

    #C0107
    ChrTalk(
        0x8,
        (
            "#04000F顺便一说，\x01",
            "亚里欧斯从阿尔泰尔回来之后，\x01",
            "马上又去雷米菲利亚了。\x02\x03",

            "因为大公阁下也会来克洛斯贝尔\x01",
            "参加月底的通商会议，\x01",
            "所以要去帮忙做一些准备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00000F亚里欧斯先生\x01",
            "真是相当忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#04006F嗯，但忙碌的\x01",
            "并不只有亚里欧斯……\x02\x03",

            "#04000F由于要召开通商会议的缘故，\x01",
            "各个机构都很忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x109,
        (
            "#10100F嗯，警备队那边有\x01",
            "人事变动和复健训练等各种问题，\x01",
            "好像也很忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，现在协会\x01",
            "人手不足的\x01",
            "问题很严重吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "#04006F是啊，艾丝蒂尔和约修亚离开以后，\x01",
            "留下的空缺很难填补。\x02\x03",

            "#04008F工作量一直在不断增加，\x01",
            "不管亚里欧斯和斯克特他们有多么优秀，\x01",
            "能做的事还是有限的。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        "#00103F确实如您所说呢……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#04000F算啦，如果今后变得更加繁忙，\x01",
            "我们说不定还会把一些工作\x01",
            "推给你们哦。\x02\x03",

            "#04011F呵呵，到时可就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00000F嗯，彼此彼此，\x01",
            "大家一起努力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 5)
    Jump("loc_3D45")

    label("loc_3CC0")


    #C0116
    ChrTalk(
        0x8,
        (
            "#04003F为了应对月底的通商会议，\x01",
            "接下来大概还会更加繁忙吧。\x02\x03",

            "#04011F我们说不定还会把一些工作\x01",
            "推给你们哦。\x01",
            "呵呵，到时可就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D45")

    TalkEnd(0x8)
    Return()

    # Function_4_993 end

    def Function_5_3D49(): pass

    label("Function_5_3D49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D67")
    Call(0, 6)
    Jump("loc_3E03")

    label("loc_3D67")


    #C0117
    ChrTalk(
        0xFE,
        (
            "竟然能与一直崇敬的\x01",
            "雾香前辈并肩作战……\x01",
            "对我来说，真是再宝贵不过的经验。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "为了今后继续守护克洛斯贝尔，\x01",
            "我一定要不断磨练自己的\x01",
            "『泰斗流』武技才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E03")

    Jump("loc_4434")

    label("loc_3E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ECE")

    #C0119
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "我在市内巡视，\x01",
            "检查是否有来不及逃难的市民时……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "似乎感觉到了一股\x01",
            "很熟悉的气息呢。\x01",
            "那莫非是……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "……应该不可能吧。\x01",
            "抱歉，随便一说，忘了我的话吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F3D")

    label("loc_3ECE")


    #C0122
    ChrTalk(
        0xFE,
        (
            "我在市内感觉到了一股\x01",
            "很熟悉的气息呢。\x01",
            "那莫非是……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "……应该不可能吧。\x01",
            "抱歉，随便一说，忘了我的话吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F3D")

    Jump("loc_4434")

    label("loc_3F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5D")
    Call(0, 7)
    Jump("loc_3FD7")

    label("loc_3F5D")


    #C0124
    ChrTalk(
        0xFE,
        (
            "各位……\x01",
            "如果形势严峻，需要帮忙的话，\x01",
            "请不要客气，尽管开口。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "我们身为协会的游击士，\x01",
            "一定会献出\x01",
            "自己的全部力量。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD7")

    Jump("loc_4434")

    label("loc_3FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3FEA")
    Jump("loc_4434")

    label("loc_3FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_408C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4009")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_4009")


    #C0126
    ChrTalk(
        0xFE,
        (
            "我们打算暂时留在协会，\x01",
            "观望一下接下来的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "不过，以目前的状况来看，绝对不容乐观……\x01",
            "或许应该做好随时出击的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4434")

    label("loc_408C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_409A")
    Jump("loc_4434")

    label("loc_409A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_40A8")
    Jump("loc_4434")

    label("loc_40A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_40B6")
    Jump("loc_4434")

    label("loc_40B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40C4")
    Jump("loc_4434")

    label("loc_40C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424F")

    #C0128
    ChrTalk(
        0xFE,
        (
            "雾香前辈好像随共和国总统\x01",
            "一起前往兰花塔了……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00000F说起来，林小姐\x01",
            "和雾香小姐好像是旧识吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "嗯，她也是『泰斗流』的弟子哦，\x01",
            "可以算是我的师姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "几年前，雾香前辈的父亲去世之后，\x01",
            "她曾在利贝尔王国担任了\x01",
            "一段时间的游击士协会接待员……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "没想到之后又加入到了\x01",
            "直属于共和国总统的谍报机关。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "老实说，她可真是个深不可测的人呢。\x01",
            "或许应该多加注意才是。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 7)
    Jump("loc_42C7")

    label("loc_424F")


    #C0134
    ChrTalk(
        0xFE,
        (
            "雾香前辈在这次的通商会议中\x01",
            "似乎也展开了各种行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "老实说，她可真是个深不可测的人呢。\x01",
            "或许应该多加注意才是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C7")

    Jump("loc_4434")

    label("loc_42CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42DA")
    Jump("loc_4434")

    label("loc_42DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_42E8")
    Jump("loc_4434")

    label("loc_42E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_42F6")
    Jump("loc_4434")

    label("loc_42F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4434")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4315")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_4315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43DC")

    #C0136
    ChrTalk(
        0xFE,
        (
            "在初次见面的时候，\x01",
            "我本以为你们\x01",
            "只是乌合之众……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "但如今的你们已经\x01",
            "完全可以独当一面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "今后我一定会继续毫不留情地\x01",
            "鞭策监督你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#00012F哈哈……还请手下留情啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4434")

    label("loc_43DC")


    #C0140
    ChrTalk(
        0xFE,
        (
            "如今的你们已经\x01",
            "完全可以独当一面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "今后我一定会毫不留情地\x01",
            "继续鞭策监督你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4434")

    TalkEnd(0xFE)
    Return()

    # Function_5_3D49 end

    def Function_6_4438(): pass

    label("Function_6_4438")

    OP_4B(0x11, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0142
    ChrTalk(
        0xB,
        "雾香前辈，您辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xB,
        (
            "能在近距离观摩到\x01",
            "泰斗流『飞燕红儿』的绝技……\x01",
            "真是令我获益良多！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x11,
        (
            "#03404F都已经好久没有实战过了，\x01",
            "没想到还能勉强应付过去。\x02\x03",

            "#03400F……话说回来，林，\x01",
            "你似乎也经历了相当程度的修炼啊。\x02\x03",

            "与八年前切磋时相比，简直就是判若两人，\x01",
            "实在是让我吃了一惊。\x01",
            "呵呵，已经变得很可靠了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        "哈哈，我还差得远呢。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "相比已至达人境界的雾香前辈和金前辈，\x01",
            "我还差得很远，只要能稍稍追近一些，\x01",
            "我就很欣喜了……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x11,
        (
            "#03400F呵呵，继续努力吧。\x02\x03",

            "#03404F嗯，只要再继续\x01",
            "修炼个一两年，\x01",
            "差不多就能胜过金了吧。\x02\x03",

            "#03402F他好像至今都没有克服\x01",
            "那一见到妙龄女性就手足无措的弱点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "哈哈，被雾香前辈这么一说，\x01",
            "连身为Ａ级游击士的金前辈都要无地自容了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1BB, 3)
    Return()

    # Function_6_4438 end

    def Function_7_46E7(): pass

    label("Function_7_46E7")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0149
    ChrTalk(
        0xA,
        (
            "老实说，我可不认为帝国\x01",
            "在听到那样的演说之后会默不作声。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "他们一定会采取\x01",
            "某种行动的……\x01",
            "说不定，已经有所行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            "亚兰德尔发起的接触\x01",
            "恐怕也是行动中的一环。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "嗯，关于此事，\x01",
            "共和国方面应该也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "教会的反应也很令人在意……\x01",
            "总之，不要太过乐观就是了。\x02",
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

    # Function_7_46E7 end

    def Function_8_4818(): pass

    label("Function_8_4818")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4829")
    Jump("loc_4FC3")

    label("loc_4829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4837")
    Jump("loc_4FC3")

    label("loc_4837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4985")

    #C0154
    ChrTalk(
        0xFE,
        (
            "自从麦克道尔议长发表了无效宣言之后，\x01",
            "规章制度又有了进一步的强化，\x01",
            "连急救车的运送都遭到了相当程度的限制。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "那些无法被送往医院的患者，\x01",
            "只能依靠市内储备的药品\x01",
            "来勉强维持……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "市内和教会的医治力量\x01",
            "终究是有限的。\x01",
            "对居民们来说，医院绝对是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "解放克洛斯贝尔市的作战……\x01",
            "一定要取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A04")

    label("loc_4985")


    #C0158
    ChrTalk(
        0xFE,
        (
            "市内和教会的医治力量\x01",
            "终究是有限的。\x01",
            "对居民们来说，医院绝对是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "解放克洛斯贝尔市的作战……\x01",
            "一定要取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A04")

    Jump("loc_4FC3")

    label("loc_4A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0D")

    #C0160
    ChrTalk(
        0xFE,
        (
            "独立宣言发表之后……\x01",
            "我的故乡雷米菲利亚\x01",
            "又会如何应对呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "阿尔伯特大公是个很有智慧的人，\x01",
            "在考虑问题时会把公国居民摆在首位，\x01",
            "应该能做出慎重的判断……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "现在不仅要与乌尔斯拉医院取得联络，\x01",
            "协会也必须要考虑今后的应对方针。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B9B")

    label("loc_4B0D")


    #C0163
    ChrTalk(
        0xFE,
        (
            "现在不仅要与乌尔斯拉医院取得联络，\x01",
            "协会也必须要考虑今后的应对方针。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "之前在湖畔还欠过你们一份人情，\x01",
            "如果遇到什么困难，请尽管开口哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9B")

    Jump("loc_4FC3")

    label("loc_4BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4BAE")
    Jump("loc_4FC3")

    label("loc_4BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BCD")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_4BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA6")

    #C0165
    ChrTalk(
        0xFE,
        (
            "被猎兵团劫持为人质，\x01",
            "事态很严重呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "就算没有遭到他们的伤害，\x01",
            "精神方面也一定会\x01",
            "承受巨大负荷的。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "如果这样的状态长期持续，\x01",
            "很有可能会出现\x01",
            "身体不适的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "营救他们是刻不容缓的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D44")

    label("loc_4CA6")


    #C0169
    ChrTalk(
        0xFE,
        (
            "被猎兵团劫持为人质\x01",
            "的玛因兹居民们\x01",
            "肯定正在承受着很强烈的精神负荷。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "如果这样的状态长期持续，\x01",
            "很有可能会出现身体不适的情况。\x01",
            "营救他们是刻不容缓的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D44")

    Jump("loc_4FC3")

    label("loc_4D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D57")
    Jump("loc_4FC3")

    label("loc_4D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4D65")
    Jump("loc_4FC3")

    label("loc_4D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D73")
    Jump("loc_4FC3")

    label("loc_4D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4D81")
    Jump("loc_4FC3")

    label("loc_4D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D8F")
    Jump("loc_4FC3")

    label("loc_4D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D9D")
    Jump("loc_4FC3")

    label("loc_4D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4DAB")
    Jump("loc_4FC3")

    label("loc_4DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4DB9")
    Jump("loc_4FC3")

    label("loc_4DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD8")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_4DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F57")
    OP_4B(0xB, 0xFF)

    #C0171
    ChrTalk(
        0xC,
        (
            "说起来……\x01",
            "好久都没有见到过\x01",
            "小缇欧了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "听说她去\x01",
            "列曼自治州了？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#00100F嗯，她可能还得\x01",
            "留在那边一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "……哈，对了，\x01",
            "游击士协会的总部就在列曼自治州，\x01",
            "不如我也去那边待上一阵子……！\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "……现在哪有那种闲工夫，\x01",
            "而且米歇尔肯定也不会答应的。\x02",
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
        "说得也是……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#00012F（哈哈……她还是老样子呢。）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_4FC3")

    label("loc_4F57")


    #C0178
    ChrTalk(
        0xFE,
        (
            "啊啊，这么久不见，\x01",
            "好想狠狠地抱抱她……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "……等她回来以后，要马上告诉我哦，\x01",
            "我会立刻飞扑过去的！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC3")

    TalkEnd(0xFE)
    Return()

    # Function_8_4818 end

    def Function_9_4FC7(): pass

    label("Function_9_4FC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4FD8")
    Jump("loc_5560")

    label("loc_4FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FE6")
    Jump("loc_5560")

    label("loc_4FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_517F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F8")

    #C0180
    ChrTalk(
        0xFE,
        (
            "总算将未能及时逃难的人们\x01",
            "迅速引领到室内避难了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "虽然来不及\x01",
            "到建筑物内逐一确认，\x01",
            "不过百货店的帕尔应该没事。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "……竟然会使出这种手段，\x01",
            "总统他们也真是\x01",
            "不管不顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "接下来，他们无论再使用\x01",
            "什么手段也不足为奇，\x01",
            "你们一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_517A")

    label("loc_50F8")


    #C0184
    ChrTalk(
        0xFE,
        (
            "……竟然会使出这种手段，\x01",
            "总统他们也真是\x01",
            "不管不顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "接下来，他们无论再使用\x01",
            "什么手段也不足为奇，\x01",
            "你们一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517A")

    Jump("loc_5560")

    label("loc_517F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_52D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5264")

    #C0186
    ChrTalk(
        0xFE,
        (
            "身为同样出身于克洛斯贝尔的人，\x01",
            "我能够理解\x01",
            "亚里欧斯先生的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "话虽如此，\x01",
            "但他竟然以这样的方式\x01",
            "离开了协会……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "……现在想这些也没用了。\x01",
            "身为一名游击士，\x01",
            "现在只能尽力做好自己能做的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52CC")

    label("loc_5264")


    #C0189
    ChrTalk(
        0xFE,
        (
            "现在再去想亚里欧斯先生的\x01",
            "问题也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "身为一名游击士，\x01",
            "现在只能尽力做好自己能做的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52CC")

    Jump("loc_5560")

    label("loc_52D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52DF")
    Jump("loc_5560")

    label("loc_52DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_535E")
    OP_4B(0xFE, 0xFF)

    #C0191
    ChrTalk(
        0xFE,
        (
            "……是吗，\x01",
            "阿尔摩利卡那边平安无事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "嗯……好的……\x01",
            "保险起见，请通知村民们，\x01",
            "让大家多加注意。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    Jump("loc_5560")

    label("loc_535E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_536C")
    Jump("loc_5560")

    label("loc_536C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_537A")
    Jump("loc_5560")

    label("loc_537A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5388")
    Jump("loc_5560")

    label("loc_5388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5396")
    Jump("loc_5560")

    label("loc_5396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_53A4")
    Jump("loc_5560")

    label("loc_53A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53B2")
    Jump("loc_5560")

    label("loc_53B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_53C0")
    Jump("loc_5560")

    label("loc_53C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53DF")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_53DF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5470")
    Jump("loc_54BA")

    label("loc_5470")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5490")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_54BA")

    label("loc_5490")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54B0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_54BA")

    label("loc_54B0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54BA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0193
    ChrTalk(
        0xFE,
        (
            "与初次见面时相比，\x01",
            "你们真是变得可靠多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "我想今后还会有很多\x01",
            "需要互相协助的事，\x01",
            "就让我们一起努力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_5560")

    label("loc_5557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5560")

    label("loc_5560")

    TalkEnd(0xFE)
    Return()

    # Function_9_4FC7 end

    def Function_10_5564(): pass

    label("Function_10_5564")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5575")
    Jump("loc_5CB5")

    label("loc_5575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5583")
    Jump("loc_5CB5")

    label("loc_5583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_570A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568B")

    #C0195
    ChrTalk(
        0xFE,
        (
            "魔导兵吗……\x01",
            "总统投放了相当危险的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "在展开解放作战时，\x01",
            "我们一定要尽最大努力，\x01",
            "保证市民们免遭伤害。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "……竟然让那样的东西\x01",
            "在街上四处游荡，\x01",
            "实在是不可原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "赌上游击士协会的名誉，\x01",
            "一定要将犯下罪行的总统\x01",
            "加以制裁。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5705")

    label("loc_568B")


    #C0199
    ChrTalk(
        0xFE,
        (
            "……竟然让那样的东西\x01",
            "在街上四处游荡，\x01",
            "实在是不可原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "赌上游击士协会的名誉，\x01",
            "一定要将犯下罪行的总统\x01",
            "加以制裁。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5705")

    Jump("loc_5CB5")

    label("loc_570A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_57D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5725")
    Call(0, 7)
    Jump("loc_57CB")

    label("loc_5725")


    #C0201
    ChrTalk(
        0xFE,
        (
            "情报局的亚兰德尔……\x01",
            "我在帝国的游击士协会任职时，\x01",
            "曾经数次听到过这个名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "你们既然与他有过接触，应该能感觉得到，\x01",
            "他是个很危险的对手。\x01",
            "……一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57CB")

    Jump("loc_5CB5")

    label("loc_57D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_57DE")
    Jump("loc_5CB5")

    label("loc_57DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_596C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58FD")

    #C0203
    ChrTalk(
        0xFE,
        (
            "斯克特已经确认过了……\x01",
            "阿尔摩利卡和医院等地\x01",
            "似乎没有发生任何情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "猎兵们利用了山道的特殊地形，\x01",
            "占据了地利优势。要想击退他们，\x01",
            "实在是困难至极。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "如果这种状况长期持续，\x01",
            "不知玛因兹的居民们\x01",
            "将会遭遇到什么样的危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "看来我们必须要有所行动了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5967")

    label("loc_58FD")


    #C0207
    ChrTalk(
        0xFE,
        (
            "如果这种状况长期持续，\x01",
            "不知玛因兹的居民们\x01",
            "将会遭遇到什么样的危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "看来我们必须要有所行动了……\x02",
    )

    CloseMessageWindow()

    label("loc_5967")

    Jump("loc_5CB5")

    label("loc_596C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_597A")
    Jump("loc_5CB5")

    label("loc_597A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5988")
    Jump("loc_5CB5")

    label("loc_5988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5996")
    Jump("loc_5CB5")

    label("loc_5996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59A4")
    Jump("loc_5CB5")

    label("loc_59A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5AD1")
    OP_4B(0xFE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6A")

    #C0209
    ChrTalk(
        0xFE,
        (
            "……嗯……嗯嗯……\x01",
            "……是吗，恐怖分子果然开始\x01",
            "在帝国行动了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……嗯，那当然，\x01",
            "我们也会加强警戒的。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00003F（似乎正在与帝国的\x01",
            "  游击士协会联络呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5AC8")

    label("loc_5A6A")


    #C0212
    ChrTalk(
        0xFE,
        (
            "……是吗，恐怖分子果然开始\x01",
            "在帝国行动了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "……嗯，那当然，\x01",
            "我们也会加强警戒的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AC8")

    OP_4C(0xFE, 0xFF)
    Jump("loc_5CB5")

    label("loc_5AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5ADF")
    Jump("loc_5CB5")

    label("loc_5ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5AED")
    Jump("loc_5CB5")

    label("loc_5AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B0C")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_5B0C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B9D")
    Jump("loc_5BE7")

    label("loc_5B9D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BBD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BE7")

    label("loc_5BBD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BDD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BE7")

    label("loc_5BDD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BE7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0214
    ChrTalk(
        0xFE,
        (
            "我已经听说你们在阿尔泰尔市的活跃表现了，\x01",
            "干得真是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "在日积月累的努力中所流下的血汗，\x01",
            "正是通向成功的路标。\x01",
            "……就保持这种势头继续努力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_5CB5")

    label("loc_5CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5CB5")

    label("loc_5CB5")

    TalkEnd(0xFE)
    Return()

    # Function_10_5564 end

    def Function_11_5CB9(): pass

    label("Function_11_5CB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CCE")
    Call(0, 6)
    Jump("loc_612A")

    label("loc_5CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA8")

    #C0216
    ChrTalk(
        0x11,
        (
            "#03400F你们几个……\x01",
            "辛苦了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00000F雾香小姐也辛苦了，\x01",
            "感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        "#00309F嗯，真是帮了我们的大忙啊！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x11,
        (
            "#03402F呵呵，我只是稍微\x01",
            "帮了把手而已。\x02\x03",

            "#03403F比起这些……\x01",
            "那棵大树的出现\x01",
            "才真是让人大吃一惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#00205F共和国方面\x01",
            "会怎么应对呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x11,
        (
            "#03403F在阿尔泰尔市也能\x01",
            "看到那棵大树的出现，\x01",
            "因此难免会引起一定程度的慌乱。\x02\x03",

            "但由于还不了解事态的详情，\x01",
            "共和国应该会\x01",
            "暂时保持观望。\x02\x03",

            "#03400F至于更加详细的情况，我也不便透露，\x01",
            "大致就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        "#00103F是吗……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x11,
        (
            "#03400F在这起事件彻底了结之前，\x01",
            "我打算留在这里。\x02\x03",

            "#03403F克洛斯贝尔究竟会走向怎样的道路，\x01",
            "没有任何人可以预料……\x01",
            "一切都将取决于你们。\x02\x03",

            "#03402F为了不让自己在未来后悔，\x01",
            "请坚定地在你们选择的道路上走下去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#00000F是……谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 7)
    Jump("loc_612A")

    label("loc_5FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_608B")

    #C0225
    ChrTalk(
        0x11,
        (
            "#03400F在这起事件彻底了结之前，\x01",
            "我打算留在这里。\x02\x03",

            "#03403F克洛斯贝尔究竟会走向怎样的道路，\x01",
            "没有任何人可以预料……\x01",
            "一切都将取决于你们。\x02\x03",

            "#03402F为了不让自己在未来后悔，\x01",
            "请坚定地在你们选择的道路上走下去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_612A")

    label("loc_608B")


    #C0226
    ChrTalk(
        0x11,
        (
            "#03403F克洛斯贝尔究竟会走向怎样的道路，\x01",
            "没有任何人可以预料……\x01",
            "一切都将取决于你们。\x02\x03",

            "#03400F为了不让自己在未来后悔，\x01",
            "请坚定地在你们选择的道路上走下去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_612A")

    TalkEnd(0xFE)
    Return()

    # Function_11_5CB9 end

    def Function_12_612E(): pass

    label("Function_12_612E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6143")
    Call(0, 13)
    Jump("loc_6191")

    label("loc_6143")


    #C0227
    ChrTalk(
        0x10,
        (
            "#01400F……这里就交给我吧。\x02\x03",

            "你们赶快去乌尔斯拉间道\x01",
            "寻找『纳迪利亚菇』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6191")

    TalkEnd(0xFE)
    Return()

    # Function_12_612E end

    def Function_13_6195(): pass

    label("Function_13_6195")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0228
    ChrTalk(
        0x10,
        (
            "#01400F……嗯，正如之前联络时所说。\x01",
            "不好意思，请尽快帮我找到。\x02\x03",

            "里面应该还有储备吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#04000F嗯……究竟放在哪里了呢……\x02\x03",

            "最好去问问\x01",
            "艾欧莉娅啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_13_6195 end

    def Function_14_624D(): pass

    label("Function_14_624D")

    TalkBegin(0xFF)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着游击士们的行程表。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_636A")
    SetChrName("")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　　 －\x01",
            "　　斯克特　 ：　阿尔摩利卡村\x01",
            "　　温蔡尔　 ：　矿山镇玛因兹\x01",
            "　　　林　　 ：　　 待命中\x01",
            " 　艾欧莉娅　：　乌尔斯拉医院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_636A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6443")
    SetChrName("")

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　　 －\x01",
            "　　斯克特　 ：　　 待命中\x01",
            "　　温蔡尔　 ：　　 待命中\x01",
            "　　　林　　 ：　　 待命中\x01",
            " 　艾欧莉娅　：　　 待命中\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_6443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_651C")
    SetChrName("")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　　 －\x01",
            "　　斯克特　 ：　　 待命中\x01",
            "　　温蔡尔　 ：　　 待命中\x01",
            "　　　林　　 ：　　 待命中\x01",
            " 　艾欧莉娅　：　　 待命中\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_651C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6601")
    SetChrName("")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　 兰花塔\x01",
            "　　斯克特　 ：　 贝尔加德门\x01",
            "　　温蔡尔　 ：　 贝尔加德门\x01",
            "　　　林　　 ：　矿山镇玛因兹\x01",
            " 　艾欧莉娅　：　矿山镇玛因兹\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_6601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_66DC")
    SetChrName("")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　 兰花塔\x01",
            "　　斯克特　 ：　　 待命中\x01",
            "　　温蔡尔　 ：　　 待命中\x01",
            "　　　林　　 ：　　 待命中\x01",
            " 　艾欧莉娅　：　　 待命中\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_66DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_67CD")
    SetChrName("")

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 搜索林、艾欧莉娅\x01",
            "　　斯克特　 ： 搜索林、艾欧莉娅\x01",
            "　　温蔡尔　 ： 搜索林、艾欧莉娅\x01",
            "　　　林　　 ：　　 ※不明\x01",
            " 　艾欧莉娅　：　　 ※不明\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_67CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_68B3")
    SetChrName("")

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　消灭幻兽\x01",
            "　　斯克特　 ：　 唐古拉姆门\x01",
            "　　温蔡尔　 ：　 唐古拉姆门\x01",
            "　　　林　　 ：　乌尔斯拉医院\x01",
            " 　艾欧莉娅　：　乌尔斯拉医院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_68B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_699C")
    SetChrName("")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 调查及消灭幻兽\x01",
            "　　斯克特　 ：　 唐古拉姆门\x01",
            "　　温蔡尔　 ：　 唐古拉姆门\x01",
            "　　　林　　 ：　乌尔斯拉医院\x01",
            " 　艾欧莉娅　：　乌尔斯拉医院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_699C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6A87")
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　 ※休假\x01",
            "　　斯克特　 ： 调查及消灭幻兽\x01",
            "　　温蔡尔　 ： 调查及消灭幻兽\x01",
            "　　　林　　 ： 调查及消灭幻兽\x01",
            " 　艾欧莉娅　： 调查及消灭幻兽\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_6A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6B68")
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　　 兰花塔\x01",
            "　　斯克特　 ：　阿尔摩利卡村\x01",
            "　　温蔡尔　 ：　　 待命中\x01",
            "　　　林　　 ：　　 待命中\x01",
            " 　艾欧莉娅　：　乌尔斯拉医院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_6B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6C52")
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：　乌尔斯拉医院\x01",
            "　　斯克特　 ：　※处理委托中\x01",
            "　　温蔡尔　 ：　※处理委托中\x01",
            "　　　林　　 ：　阿尔摩利卡村\x01",
            " 　艾欧莉娅　：　阿尔摩利卡村\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_6C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6D3C")
    SetChrName("")

    #A0242
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 卡尔瓦德共和国\x01",
            "　　斯克特　 ：　矿山镇玛因兹\x01",
            "　　温蔡尔　 ：　 贝尔加德门\x01",
            "　　　林　　 ：　※处理委托中\x01",
            " 　艾欧莉娅　：　※处理委托中\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_6D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6E23")
    SetChrName("")

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 雷米菲利亚公国\x01",
            "　　斯克特　 ：　　 待命中\x01",
            "　　温蔡尔　 ：　　 待命中\x01",
            "　　　林　　 ：　乌尔斯拉医院\x01",
            " 　艾欧莉娅　：　乌尔斯拉医院　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F04")

    label("loc_6E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6F04")
    SetChrName("")

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　姓　名　　　　　去　向\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 雷米菲利亚公国\x01",
            "　　斯克特　 ：　阿尔摩利卡村\x01",
            "　　温蔡尔　 ： 埃雷波尼亚帝国\x01",
            "　　　林　　 ：　　 待命中\x01",
            " 　艾欧莉娅　：　　 待命中\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6F04")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_624D end

    def Function_15_6F1B(): pass

    label("Function_15_6F1B")

    TalkBegin(0xFF)
    SetChrName("")

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着交付给游击士协会的\x01",
            "大量委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FBE")

    #C0246
    ChrTalk(
        0x101,
        (
            "#00000F协会还是老样子，接到了\x01",
            "数量惊人的委托呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x109,
        (
            "#10103F嗯～我们也不能\x01",
            "输给他们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_6FBE")

    TalkEnd(0xFF)
    Return()

    # Function_15_6F1B end

    def Function_16_6FC2(): pass

    label("Function_16_6FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FE7")
    Call(0, 33)
    Return()

    label("loc_6FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FFA")
    Call(0, 34)
    Return()

    label("loc_6FFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_700B")
    Jump("loc_73D7")

    label("loc_700B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7057")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_702D")
    Call(0, 17)
    Jump("loc_7052")

    label("loc_702D")


    #C0248
    ChrTalk(
        0xD,
        "#01109F滴，一会咱们去支援科吧。\x02",
    )

    CloseMessageWindow()

    label("loc_7052")

    Jump("loc_73D7")

    label("loc_7057")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7390")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7076")
    Jump("loc_738B")

    label("loc_7076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7313")
    TurnDirection(0xD, 0x1A2, 0)

    #C0249
    ChrTalk(
        0xD,
        (
            "#01100F嘿嘿，你是叫秦吧？\x02\x03",

            "看你好像不是克洛斯贝尔的孩子，\x01",
            "可以在这里待多久呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1A2,
        (
            "我吗？\x01",
            "目前预计要待到后天……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xD,
        (
            "#01105F啊，那你明天要去哪里看\x01",
            "那座大楼的揭幕式呢～？\x02\x03",

            "#01102F我们想去百货店的楼顶看，\x01",
            "你要不要一起来？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0252
    ChrTalk(
        0x1A2,
        "真、真的可以吗……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0253
    ChrTalk(
        0xD,
        (
            "#01105F嗯？为什么不可以呢？\x02\x03",

            "#01109F隆和亨利，\x01",
            "还有很多孩子也会来，\x01",
            "肯定会很有趣的～\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x1A2,
        "是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x1A2,
        (
            "……既然你都把话讲到了如此地步，\x01",
            "那我就参加好了！\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x1A2,
        "是明天十一点，没错吧！？\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xD,
        "#01109F嗯，等你哦！\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#00009F（哈哈……\x01",
            "  看起来好像很开心呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        (
            "#00102F（是啊，他大概很少有机会\x01",
            "  能和别的孩子一起玩……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 2)
    TurnDirection(0xD, 0xE, 0)
    Jump("loc_738B")

    label("loc_7313")

    TurnDirection(0xD, 0x1A2, 0)

    #C0260
    ChrTalk(
        0xD,
        (
            "#01100F别忘了明天十一点\x01",
            "在百货店的楼顶见哦！\x02\x03",

            "#01109F我们等着你！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x1A2,
        (
            "啊……嗯嗯……\x01",
            "那……明天见。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 0)

    label("loc_738B")

    Jump("loc_73D7")

    label("loc_7390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_73D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73A8")
    Jump("loc_73D7")

    label("loc_73A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73BA")
    Call(0, 17)
    Jump("loc_73D7")

    label("loc_73BA")


    #C0262
    ChrTalk(
        0xD,
        "#01109F那滴也一起去吧！\x02",
    )

    CloseMessageWindow()

    label("loc_73D7")

    TalkEnd(0xFE)
    Return()

    # Function_16_6FC2 end

    def Function_17_73DB(): pass

    label("Function_17_73DB")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D9")

    #C0263
    ChrTalk(
        0xD,
        (
            "#01104F滴，秦已经走了，\x01",
            "咱们也去外面玩玩吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xE,
        (
            "#06005F啊……嗯，好啊。\x02\x03",

            "#06000F不过，只有我们两个小孩子一起去，\x01",
            "没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xD,
        "#01111F嗯……说得也是…… \x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0266
    ChrTalk(
        0xD,
        "#01110F啊，有了，我想到一个好主意。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7576")

    label("loc_74D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7576")

    #C0267
    ChrTalk(
        0xD,
        (
            "#01109F那座高楼啊～虽然现在\x01",
            "还罩着蓝色的布……\x01",
            "但真是好高好高啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xE,
        (
            "#06002F真好啊……\x01",
            "呵呵，我也想看一看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xD,
        "#01109F那好！滴也一起去！\x02",
    )

    CloseMessageWindow()

    label("loc_7576")

    SetScenarioFlags(0x1, 1)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_17_73DB end

    def Function_18_7582(): pass

    label("Function_18_7582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75A7")
    Call(0, 33)
    Return()

    label("loc_75A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75BA")
    Call(0, 34)
    Return()

    label("loc_75BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_75CB")
    Jump("loc_77F6")

    label("loc_75CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_764B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75ED")
    Call(0, 17)
    Jump("loc_7646")

    label("loc_75ED")


    #C0270
    ChrTalk(
        0xE,
        (
            "#06005F嗯，可以是可以……\x01",
            "不过刚才说的好主意是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        "#01104F嘿嘿嘿，暂时保密。\x02",
    )

    CloseMessageWindow()

    label("loc_7646")

    Jump("loc_77F6")

    label("loc_764B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_766A")
    Jump("loc_779D")

    label("loc_766A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7720")
    TurnDirection(0xE, 0x1A2, 0)

    #C0272
    ChrTalk(
        0xE,
        (
            "#06002F呵呵，秦也是个\x01",
            "很乖的好孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x1A2,
        (
            "哪、哪有……\x01",
            "才、才没有那种事呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1A2,
        (
            "我、我可是\x01",
            "背负着『黑月』未来\x01",
            "的男子汉！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xE,
        "#06002F嘻嘻……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    TurnDirection(0xE, 0xD, 0)
    Jump("loc_779D")

    label("loc_7720")

    TurnDirection(0xE, 0x1A2, 0)

    #C0276
    ChrTalk(
        0xE,
        (
            "#06002F嘻嘻……\x01",
            "虽然不太明白，\x01",
            "但我觉得秦是个乖孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x1A2,
        (
            "（这、这个……\x01",
            "  我才不是什么\x01",
            "  乖孩子呢。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 0)

    label("loc_779D")

    Jump("loc_77F6")

    label("loc_77A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_77F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77BA")
    Jump("loc_77F6")

    label("loc_77BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77CC")
    Call(0, 17)
    Jump("loc_77F6")

    label("loc_77CC")


    #C0278
    ChrTalk(
        0xE,
        (
            "#06002F呵呵，知道了。\x01",
            "我们一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F6")

    TalkEnd(0xFE)
    Return()

    # Function_18_7582 end

    def Function_19_77FA(): pass

    label("Function_19_77FA")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_19_77FA end

    def Function_20_7801(): pass

    label("Function_20_7801")

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

    def lambda_78E9():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_78E9)

    def lambda_7903():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7903)
    Sleep(250)

    def lambda_7917():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7917)

    def lambda_7931():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7931)
    Sleep(600)

    def lambda_7945():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7945)

    def lambda_795F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_795F)
    Sleep(250)

    def lambda_7973():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7973)

    def lambda_798D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_798D)
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
        "#04005F啊，是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#00000F米歇尔先生……\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0x102, -500, 0, 3000, 0)
    SetChrPos(0x105, 0, 0, 1900, 0)
    SetChrPos(0x109, -1000, 0, 1900, 0)

    def lambda_7A60():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A60)
    Sleep(100)

    def lambda_7A7D():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A7D)
    Sleep(150)

    def lambda_7A9A():
        OP_96(0xFE, 0x7D0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A9A)
    Sleep(100)

    def lambda_7AB7():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7AB7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x105, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B64")

    #A0281
    AnonymousTalk(
        0x8,
        (
            "呵呵，好久不见。\x02\x03",

            "在阿尔泰尔市的抓捕行动\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_7BBD")

    label("loc_7B64")


    #A0282
    AnonymousTalk(
        0x8,
        (
            "呵呵，好久不见。\x02\x03",

            "这句话说得也许有些晚，\x01",
            "在阿尔泰尔市的抓捕行动\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7BBD")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0283
    ChrTalk(
        0x101,
        (
            "#12P#00000F谢谢。\x01",
            "多亏亚里欧斯先生和达德利警官\x01",
            "当时给了我们很多帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，\x01",
            "米歇尔先生也很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#04011F呵呵，这还用说¤\x02\x03",

            "#04006F唉，但由于艾丝蒂尔\x01",
            "和约修亚离开了，\x01",
            "最近比以前更加忙了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#12P#00003F果然如此啊……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x109,
        (
            "#12P#10100F不过，亚里欧斯先生\x01",
            "和其他游击士已经顺利\x01",
            "填补上他们留下的空缺了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#04004F哈，毕竟大家都已经习惯了\x01",
            "这种人手不足的状态啦。\x02\x03",

            "#04000F总算还能\x01",
            "将工作分摊完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，毕竟游击士\x01",
            "是民间人士的伙伴……\x02\x03",

            "#10300F无论有多么繁忙，\x01",
            "也都不会退缩\x01",
            "或抱怨吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#04004F正是如此，\x01",
            "你很了解嘛。\x02\x03",

            "#04009F虽说你们警察\x01",
            "也开始得到市民们的认可了，\x01",
            "但正因如此，我们才更要──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x8,
        (
            "#04005F嗯？莫非这两个\x01",
            "孩子就是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#12P#00000F嗯，是支援科的新成员。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x109,
        (
            "#12P#10100F我是由警备队外派至此处的\x01",
            "诺艾尔·希卡！\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        (
            "#12P#10302F瓦吉·赫米斯菲亚……\x01",
            "只要报上姓名，\x01",
            "其它的也就不必再多说了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "#04000F哎……\x01",
            "看来你们召集到了\x01",
            "很有趣的伙伴啊。\x02\x03",

            "#04004F现役警备队员暂且不说，\x01",
            "没想到连『圣书会』的首领\x01",
            "都加入支援科了。\x02\x03",

            "#04000F不管怎么说，支援科能恢复工作，\x01",
            "对我们而言也算是帮了大忙。\x02\x03",

            "如果今后遇到特殊情况，\x01",
            "可能还会需要你们来帮忙哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，那当然没问题。\x02\x03",

            "虽然各自的立场不同，\x01",
            "但理应互相协助，共同努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "#04004F呵呵，与初次见面时相比，\x01",
            "你的表情更棒了呢。\x02\x03",

            "#04011F那么……\x01",
            "今后也请各位继续关照啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x139, 0)
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_7801 end

    def Function_21_811A(): pass

    label("Function_21_811A")

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
        "哦，特别任务支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        "真是好久不见了啊。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#00000F好久不见，\x01",
            "林小姐，艾欧莉娅小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#00100F协会的各位\x01",
            "都还好吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    #C0302
    ChrTalk(
        0xB,
        (
            "嗯，还是老样子，\x01",
            "每天忙得不可开交呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    #C0303
    ChrTalk(
        0xB,
        (
            "那个……这两位就是\x01",
            "新加入的成员吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x105,
        "#6P#10300F嗯，可以这么说。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x109,
        (
            "#6P#10100F二位是协会的游击士吧？\x01",
            "今后请多多关照！\x02\x03",

            "#10109F说起来，\x01",
            "在你们前往共和国时，\x01",
            "我看到过你们好几次呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x109, 500)

    #C0306
    ChrTalk(
        0xB,
        (
            "哦，你是警备队的……\x01",
            "这么一说，我也记得曾在\x01",
            "唐古拉姆门见到过你。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    #C0307
    ChrTalk(
        0xC,
        (
            "呵呵，听说在阿尔泰尔市的作战中，\x01",
            "你们的表现非常活跃。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0308
    ChrTalk(
        0xC,
        (
            "经过教团那起事件的锻炼，\x01",
            "你们差不多也可以\x01",
            "独当一面了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#00012F哈哈，我们仍然还有\x01",
            "很多不足之处……\x02\x03",

            "#00000F但今后一定会尽己所能，\x01",
            "继续努力的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0310
    ChrTalk(
        0xB,
        "哈哈，就得有这股干劲。\x02",
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

    # Function_21_811A end

    def Function_22_849D(): pass

    label("Function_22_849D")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85A7")
    Jump("loc_85F1")

    label("loc_85A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_85C7")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85F1")

    label("loc_85C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85E7")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85F1")

    label("loc_85E7")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_85F1")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86A7")
    Jump("loc_86F1")

    label("loc_86A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_86C7")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_86F1")

    label("loc_86C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86E7")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_86F1")

    label("loc_86E7")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86F1")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_0D()

    #C0311
    ChrTalk(
        0x9,
        "#6P哦，你们是……\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xA,
        (
            "……是特别任务支援科的各位啊。\x01",
            "唔，好久不见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#11P#00000F斯克特先生，温蔡尔先生，\x01",
            "两位工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x105,
        (
            "#11P#10300F是协会的游击士吗？\x01",
            "呵呵，看起来似乎\x01",
            "拥有相当不错的实力呢。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8879")
    Jump("loc_88C3")

    label("loc_8879")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8899")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88C3")

    label("loc_8899")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88B9")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88C3")

    label("loc_88B9")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_88C3")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    #C0315
    ChrTalk(
        0x9,
        (
            "#6P说起来，你不就是\x01",
            "旧城区不良团伙的……\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89AA")
    Jump("loc_89F4")

    label("loc_89AA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_89CA")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89F4")

    label("loc_89CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89EA")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89F4")

    label("loc_89EA")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89F4")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    #C0316
    ChrTalk(
        0x9,
        (
            "#6P旁边那个孩子好像是\x01",
            "警备队员吧？\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AD5")
    Jump("loc_8B1F")

    label("loc_8AD5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AF5")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B1F")

    label("loc_8AF5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B15")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B1F")

    label("loc_8B15")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B1F")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    #C0317
    ChrTalk(
        0x9,
        (
            "#6P哈哈，加入了两位\x01",
            "很有趣的新成员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#11P#10105F瓦、瓦吉也就罢了……\x01",
            "竟然一眼就能看出我的身份？\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C44")
    Jump("loc_8C8E")

    label("loc_8C44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8C64")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C8E")

    label("loc_8C64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C84")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C8E")

    label("loc_8C84")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C8E")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Sleep(150)

    #C0319
    ChrTalk(
        0xA,
        (
            "因为你和普通警察的样子\x01",
            "有着明显的不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xA,
        (
            "既然要从事与游击士\x01",
            "相近的工作，\x01",
            "你们也要好好锻炼自己的观察能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        "#11P#00100F呵呵，多谢忠告。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x9,
        (
            "#6P今后应该还有很多事情\x01",
            "需要我们互相协作，\x01",
            "大家一起努力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x138, 7)
    EventEnd(0x5)
    Return()

    # Function_22_849D end

    def Function_23_8D9A(): pass

    label("Function_23_8D9A")

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
        "#5P#04000F啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        "昨天可真是太感谢了。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#12P#00005F林小姐，艾欧莉娅小姐……\x01",
            "你们已经没事了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "嗯，没问题啦。\x01",
            "多亏你们相救。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 500)
    Sleep(500)

    #C0327
    ChrTalk(
        0xC,
        (
            "小缇欧，稍后就让我蹭蹭\x01",
            "你的小脸蛋，以表谢意吧⊥\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xC, 500)

    #C0328
    ChrTalk(
        0x103,
        (
            "#12P#00203F……请容我拒绝。\x02\x03",

            "#00200F看你们现在的样子，\x01",
            "似乎是没问题了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    #C0329
    ChrTalk(
        0xB,
        (
            "嗯，虽然还无法\x01",
            "过于逞强……\x02",
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
            "啊，说起来……\x01",
            "那个红毛怎么不在？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xB,
        (
            "在这个时候，他一般都会\x01",
            "说些『那么，就由我来代替……』\x01",
            "之类的话……\x02",
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
            "#5P#04001F……似乎发生了一些事情啊。\x01",
            "如果方便，可否告诉我们？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        "#12P#00000F……嗯，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人将兰迪失踪\x01",
            "的事情做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0335
    ChrTalk(
        0x8,
        (
            "#5P#04003F……原来如此。\x02\x03",

            "#04001F关于这次的占领玛因兹事件……\x01",
            "由于牵扯到了『赤色星座』，\x01",
            "因此我多少也预想到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#12P#00101F……协会打算\x01",
            "如何对应这次的事件？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)
    Sleep(500)

    #C0337
    ChrTalk(
        0xB,
        (
            "……警备队目前正在\x01",
            "全力解决事件，\x01",
            "我们暂且先保持观望吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "不过，如果这种状况长期持续，\x01",
            "我们也不得不出动了。\x01",
            "……对吧？米歇尔。\x02",
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
            "#5P#04003F嗯……\x02\x03",

            "#04001F如果情势需要，\x01",
            "说不定还会从周边国家借调一些\x01",
            "Ａ级游击士，请他们直接介入。\x02",
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
        "#12P#00011F那、那么严重吗……！？\x02",
    )

    CloseMessageWindow()

    def lambda_939B():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_939B)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0341
    ChrTalk(
        0xC,
        "那终究只是最坏的情况而已。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xC,
        (
            "亚里欧斯先生已经\x01",
            "去市长那里交涉相关问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "如果警备队始终没有\x01",
            "能解决此事件的迹象……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x109,
        "#12P#10108F……呜……\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x105,
        (
            "#12P#10303F没办法啊，将民间人士的安全摆在\x01",
            "首位的游击士协会当然会采取对策……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    #C0346
    ChrTalk(
        0x8,
        (
            "#5P#04003F……总之，\x01",
            "有关那个红毛小子的事情，\x01",
            "我们也会多加留意的。\x02\x03",

            "#04001F接下来还不知将会出现怎样的情况，\x01",
            "你们可一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#12P#00001F……嗯，明白了。\x02",
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

    # Function_23_8D9A end

    def Function_24_9582(): pass

    label("Function_24_9582")

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
        "#5P#04005F啊……是你们！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_96DF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_96DF)
    Sleep(50)

    def lambda_96EF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_96EF)
    Sleep(50)

    def lambda_96FF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_96FF)
    TurnDirection(0xB, 0x101, 500)

    #C0349
    ChrTalk(
        0xA,
        (
            "自从独立宣言发表之后，\x01",
            "你们就一直杳无音信……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x9,
        "哈哈，看起来很有精神，这就再好不过了。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#12P#00000F米歇尔先生，还有各位……\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        "#12P#00202F呵呵，大家平安无事就好。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xB,
        "呵呵，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xC,
        (
            "小缇欧……\x01",
            "你没事真是太好了！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x8,
        (
            "#5P#04006F……我说，现在可不是\x01",
            "悠闲叙旧的时候哦。\x02\x03",

            "#04001F虽然刚刚重逢就谈这些，有些破坏气氛，\x01",
            "但我们还是尽快交换情报如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#12P#00000F嗯，明白了。\x02",
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
            "……原来如此，\x01",
            "竟然发生了这样的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xB,
        (
            "老实说，目前的状况\x01",
            "实在是让人难以捉摸，\x01",
            "不过总算是大致明白了。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x9,
        (
            "当时听说红色神机\x01",
            "出现在西出口方向时，\x01",
            "我还在想到底发生了什么事……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x9,
        "没想到竟然是艾丝蒂尔他们来了啊。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xC,
        (
            "听说黑月和警备队的成员\x01",
            "也分别在东出口和北出口\x01",
            "参加了反抗作战……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "呵呵，这多亏了你们\x01",
            "平时建立的人脉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        "#12P#00300F哈哈，也可以这么说吧。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x102,
        (
            "#6P#00105F说起来……\x01",
            "市内出现了『魔导兵』之后，\x01",
            "有没有造成什么人员伤亡呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xC,
        "嗯，暂时还没有。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x9,
        (
            "为了确认是否有未能及时避难的人，\x01",
            "我们保持着警戒，\x01",
            "在这附近探查了一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x9,
        (
            "看样子，那些魔导兵\x01",
            "是绝对不会向\x01",
            "克洛斯贝尔的市民出手的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C23")

    #C0368
    ChrTalk(
        0x105,
        (
            "#12P#10403F嗯……看来总统他们\x01",
            "把它们控制得很好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CBA")

    label("loc_9C23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C74")

    #C0369
    ChrTalk(
        0x10A,
        (
            "#12P#00603F嗯……看来总统他们\x01",
            "可以很精确地控制它们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CBA")

    label("loc_9C74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CBA")

    #C0370
    ChrTalk(
        0x109,
        (
            "#12P#10101F看起来，总统他们\x01",
            "可以完美控制它们呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D03")

    #C0371
    ChrTalk(
        0x106,
        (
            "#12P#10705F从某种意义上说，\x01",
            "应该可以放心了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D90")

    label("loc_9D03")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D4C")

    #C0372
    ChrTalk(
        0x109,
        (
            "#12P#10105F从某种意义上说，\x01",
            "应该可以放心了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D90")

    label("loc_9D4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D90")

    #C0373
    ChrTalk(
        0x105,
        (
            "#12P#10304F从某种意义上说，\x01",
            "应该不必担心了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D90")


    #C0374
    ChrTalk(
        0x101,
        (
            "#12P#00001F但即使如此……\x01",
            "应该也会有很多人\x01",
            "感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        (
            "#6P#00103F是啊……如果这种状态长期持续，\x01",
            "说不定就会有人不幸被卷入，\x01",
            "遭到它们的伤害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        (
            "#5P#04003F嗯，既然无辜的\x01",
            "民间人士已经陷入危险，\x01",
            "游击士协会就绝不能坐视不理。\x02\x03",

            "#04011F突击兰花塔，逮捕总统\x01",
            "的作战……就让我们也\x01",
            "贡献一份力量吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        (
            "#12P#00204F谢谢。\x01",
            "……有你们的帮忙，真是让人信心百倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        (
            "#5P#04003F不过……\x01",
            "亚里欧斯恐怕\x01",
            "也在兰花塔内。\x02\x03",

            "那个叫玛丽亚贝尔的大小姐，\x01",
            "还有『战鬼』等人\x01",
            "大概也在里面严阵以待。\x02\x03",

            "#04001F这绝对不是能轻易完成的任务……\x01",
            "你们应该明白吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x104,
        "#12P#00303F……自然再清楚不过了。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        (
            "#12P#00001F但无论面对怎样的『壁障』……\x01",
            "我们也只能全力挑战。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#5P#04004F呵呵，看来你们已经\x01",
            "做好心理准备了啊。\x02\x03",

            "#04001F作战开始的时候，\x01",
            "请再与我联络。\x02\x03",

            "在那之前，\x01",
            "我们会认真做好准备的。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#12P#00000F嗯……那就稍后再见了。\x02",
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

    # Function_24_9582 end

    def Function_25_A125(): pass

    label("Function_25_A125")

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
            "啊，你们来了啊。\x02\x03",

            "亚里欧斯还没回来，\x01",
            "如果方便，要不要去二楼等一等？\x02\x03",

            "要是你们还有别的事情，\x01",
            "也可以办完以后再过来。\x02",
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
            "#12P#00005F啊，是这样啊。\x02\x03",

            "#00008F（已经快到傍晚了……\x01",
            "  还有其它的事情要去办吗？）\x02",
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
            "【还有其它事情】\x01",          # 0
            "【等待亚里欧斯回来】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A394"),
        (1, "loc_A41D"),
        (SWITCH_DEFAULT, "loc_A5C4"),
    )


    label("loc_A394")


    #C0385
    ChrTalk(
        0x8,
        (
            "#5P#04011F是吗，那就等你们\x01",
            "把事情办完之后再过来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        "#12P#00012F嗯，我们一会再来。\x02",
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
    Jump("loc_A5C4")

    label("loc_A41D")


    #C0387
    ChrTalk(
        0x8,
        (
            "#5P#04011F嗯，那就到二楼\x01",
            "休息一下吧。\x02\x03",

            "茶叶和咖啡都有，\x01",
            "自己随便泡吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        "#12P#00012F哈哈，好的。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x102,
        "#12P#00102F那就打扰了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 4500)

    def lambda_A4B1():

        label("loc_A4B1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_A4B1")

    QueueWorkItem2(0x8, 2, lambda_A4B1)
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
            "之后，没过多久，\x01",
            "亚里欧斯就回到了协会。\x02\x03",

            "罗伊德等人针对通商会议，\x01",
            "以及有关『黑月』与『赤色星座』的问题，\x01",
            "与协会众人交换了情报。\x07\x00\x02",
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
    Jump("loc_A5C4")

    label("loc_A5C4")

    Return()

    # Function_25_A125 end

    def Function_26_A5C5(): pass

    label("Function_26_A5C5")

    OP_92(0xFE, 0x1F40, 0x2AF8, 0x1F4)

    def lambda_A5D7():
        OP_95(0xFE, 8000, 0, 11000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A5D7)
    WaitChrThread(0xFE, 1)

    def lambda_A5F5():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A5F5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_A5C5 end

    def Function_27_A60F(): pass

    label("Function_27_A60F")

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
            "#4049V#30W──原来如此。\x02\x03",

            "#4050V没想到『深红商会』\x01",
            "还有这样的背景……\x02",
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
            "#04006F最近这段时间，很难得到\x01",
            "来自帝都那边的情报呢。\x02\x03",

            "#04000F谢谢啦，你们真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#12P#00004F哪里，能发挥作用是我们的荣幸。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x105,
        (
            "#6P#10306F不过，有关『赤色星座』的情报，\x01",
            "你们应该也有一定程度的掌握吧？\x02\x03",

            "#10300F我听说游击士协会经常\x01",
            "会与猎兵团展开一些小型冲突。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "#5P#01403F嗯，冲突确实很多，\x01",
            "但很少会与『赤色星座』\x01",
            "这种级别的大型组织发生纠纷。\x02\x03",

            "#01400F……因为处理不善的话，\x01",
            "很有可能会演变为全面战争。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        "#12P#00101F那么严重啊……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x109,
        (
            "#10108F听说他们的战斗力甚至\x01",
            "可以达到小国军队的等级呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#04003F在众多的猎兵团之中，\x01",
            "『赤色星座』可以称得上是远超群侪。\x02\x03",

            "他们的势力网络遍及整个大陆，\x01",
            "一旦发现战争的征兆，就会立刻介入，\x01",
            "从中获取巨额利益……\x02\x03",

            "#04001F在同行之中，能与他们匹敌的\x01",
            "大概也只有『西风旅团』猎兵团了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x105,
        (
            "#6P#10305F那好像就是鲁巴彻副头目\x01",
            "从前所在的组织吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x104,
        (
            "#00301F……那也是个极强的猎兵团，\x01",
            "汇集着众多身经百战的强者。\x02\x03",

            "特别是那个被称为『猎兵王』的首领，\x01",
            "简直就是个怪物一般的家伙……\x02\x03",

            "#00303F但在半年之前，他已经与『斗神』──\x01",
            "也就是我的父亲同归于尽了。\x02",
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
        "#6P#00108F兰迪……\x02",
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
        "#5P#01405F似乎发生过很多复杂的事情呢。\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x8,
        (
            "#04003F有关这方面的情报，\x01",
            "我们协会也有所掌握。\x02\x03",

            "#04001F顺便一提，『西风旅团』\x01",
            "现在好像已经停止了活动……\x02\x03",

            "但『赤色星座』似乎还是老样子，\x01",
            "仍在精力充沛地持续活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x104,
        (
            "#00306F那是因为我叔叔还在吧。\x02\x03",

            "#00303F赤色星座的副团长──\x01",
            "『赤色战鬼』西格蒙德。\x02\x03",

            "#00301F一个可以与『斗神』和『猎兵王』\x01",
            "相匹敌的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x10,
        (
            "#5P#01400F嗯，这三个人格外有名。\x02\x03",

            "#01403F根据听到的传闻来推测，\x01",
            "恐怕连我也未必能敌得过。\x02",
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
        "#12P#00011F怎、怎么会……！\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x102,
        (
            "#12P#00105F连『风之剑圣』\x01",
            "都无法和他匹敌吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x8,
        (
            "#04006F嗯……在我看来，\x01",
            "双方的胜率大概是五五开吧。\x02\x03",

            "#04000F毕竟剑士和猎兵的战斗类型\x01",
            "与擅长的领域都有很大区别。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x104,
        (
            "#00303F……的确。\x02\x03",

            "#00301F虽然你确实很强，\x01",
            "但叔叔也是真正意义上的怪物。\x02\x03",

            "如果展开正面交战，\x01",
            "恐怕谁也无法保证全身而退吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x10,
        (
            "#5P#01403F嗯，我明白。\x02\x03",

            "#01400F不过，一旦情势需要，\x01",
            "还是会有敌对的可能。\x02\x03",

            "关键问题还是……他们来到\x01",
            "克洛斯贝尔究竟有何目的……\x02",
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
        "#10106F嗯，重点就在这里呢……\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x105,
        (
            "#6P#10306F虽然已经收集到了一些情报，\x01",
            "但对此还是毫无头绪啊。\x02\x03",

            "#10300F我们目前掌握的线索，\x01",
            "似乎也只有他们同帝国政府有所瓜葛这一点吧？\x02",
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
            "#04001F嗯……\x01",
            "另外，还有一件让我很在意的情报。\x02\x03",

            "是亚里欧斯在共和国那边\x01",
            "了解到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        "#12P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        "#12P#00101F是什么情报呢？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x10,
        (
            "#5P#01403F哦，是关于『黑月』的。\x02\x03",

            "#01401F据说，共和国政府\x01",
            "目前正在与『黑月』的长老们\x01",
            "进行着某种交易。\x02",
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
        "#12P#00007F真的吗……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_B5AE")

    #C0419
    ChrTalk(
        0x102,
        (
            "#12P#00108F说到『黑月』的长老，\x01",
            "秦的祖父也是其中之一啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5F2")

    label("loc_B5AE")


    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#00108F『黑月』的长老，\x01",
            "那是组织中地位很高的核心人物吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5F2")


    #C0421
    ChrTalk(
        0x8,
        (
            "#04006F……是啊。\x01",
            "此外还有一个关键的问题。\x02\x03",

            "#04001F主导这场交易的人，\x01",
            "是一位名叫雾香·楼兰的女性。\x02",
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
        "#12P#00011F哎哎！？\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        (
            "#12P#00107F这……\x01",
            "竟然是雾香小姐！？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x105,
        (
            "#6P#10302F哦？是在竞拍会上\x01",
            "见到的那位黑发姐姐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10,
        (
            "#5P#01403F其实，她与游击士协会\x01",
            "也有一定的渊源……\x02\x03",

            "她曾经在利贝尔的蔡斯分部\x01",
            "担任过接待员。\x02\x03",

            "#01400F但在一年前左右递交了辞呈，\x01",
            "转职进入到了卡尔瓦德的情报机关。\x02\x03",

            "那个情报机关的名字是\x01",
            "『洛克史密斯机关』。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        "#12P#00006F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x109,
        (
            "#10108F洛克史密斯……\x01",
            "那是共和国总统的名字呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#12P#00106F我也听说过，共和国总统\x01",
            "主导建立了新的情报机关……\x02",
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
            "#12P#00101F请、请稍等一下！\x02\x03",

            "『赤色星座』和『黑月』\x01",
            "以前不是有过争斗吗！？\x02\x03",

            "两个组织分别与两大国的谍报人员\x01",
            "有所接触，这就意味着……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，两大阵营壁垒分明，\x01",
            "似乎已经做好了对抗的准备呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        "#12P#00013F这……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x109,
        (
            "#10101F难、难道帝国和共和国的代理者\x01",
            "将要在克洛斯贝尔发动战争……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x8,
        (
            "#04003F这种可能性当然也不能排除。\x02\x03",

            "#04001F特别是从明天开始的通商会议。\x01",
            "宰相与皇子将会由埃雷波尼亚帝国前来，\x01",
            "而卡尔瓦德共和国方面则会有总统来访。\x02\x03",

            "说不定双方都想趁着这次的机会，\x01",
            "将对方的首脑暗杀……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x10,
        (
            "#5P#01403F不过，两国都没有隐瞒与违法组织\x01",
            "暗中接触的行为，这未免有些不正常。\x02\x03",

            "一旦『黑月』或『赤色星座』有所行动，\x01",
            "其后台就会暴露无遗，\x01",
            "这必定会遭到国际社会的非议。\x02\x03",

            "#01400F无论是帝国还是共和国，\x01",
            "恐怕都不会甘愿承担如此风险。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x109,
        "#10106F嗯……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x102,
        (
            "#12P#00103F……的确，双方应该都不会\x01",
            "如此草率地发动进攻。\x02\x03",

            "#00108F不过，那又该怎么解释呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x104,
        (
            "#00306F可恶，叔叔他们\x01",
            "到底有什么企图……\x02",
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
            "#12P#00003F不管怎么说，\x01",
            "我们用现有情报所完成的拼图\x01",
            "一定包含着某些含义。\x02\x03",

            "#00008F不出意外的话，我们应该还有\x01",
            "一块『关键的碎片』没能取得……\x02\x03",

            "#00001F有必要尽快将它找到。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    #C0439
    ChrTalk(
        0x102,
        "#12P#00105F啊……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x105,
        "#6P#10302F呵呵，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x8,
        (
            "#04011F呵呵，真不愧是罗伊德，\x01",
            "被你抢先一步说出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x10,
        (
            "#5P#01404F其实我们的想法与你相同。\x02\x03",

            "#01402F目前正在通过\x01",
            "协会的情报网，\x01",
            "寻找那块『关键的碎片』。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)

    #C0443
    ChrTalk(
        0x101,
        "#12P#00002F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x104,
        (
            "#00300F那么，如果掌握到什么情况，\x01",
            "可以告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x8,
        (
            "#04000F嗯，一旦取得新进展，\x01",
            "一定会与警察总部联络的。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x10,
        (
            "#5P#01402F如果你们有什么发现，\x01",
            "也请告知我们。\x02\x03",

            "这也是为了平安无事地\x01",
            "度过从明天开始的三天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x101,
        "#12P#00000F明白了……！\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        (
            "#12P#00102F如果有什么发现，\x01",
            "一定会马上通知您的。\x02",
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
            "之后，琪雅和滴在蔡特的陪伴下\x01",
            "回到了协会。\x02\x03",

            "罗伊德等人为了不打扰亚里欧斯与滴两人\x01",
            "的父女独处时间，以回去吃晚饭为由同\x01",
            "亚里欧斯等人道别，回到了支援科。\x07\x00\x02",
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

    # Function_27_A60F end

    def Function_28_C057(): pass

    label("Function_28_C057")

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
        "#5P#04005F啊，是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        (
            "#12P#00012F哈哈……\x01",
            "您好，米歇尔先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        (
            "#12P#00106F那个……听了您的话之后，\x01",
            "我们有些担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x8,
        (
            "#5P#04006F呼，抱歉啦，\x01",
            "就像在催促你们一样。\x02\x03",

            "#04011F不过，真是谢谢啦。\x01",
            "你们特意赶过来，人家好高兴哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x104,
        (
            "#6P#00305F这么说，\x01",
            "还是没有和艾欧莉娅小姐她们\x01",
            "取得联络吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x8,
        (
            "#5P#04003F嗯，亚里欧斯他们已经去\x01",
            "分头寻找了，但还是没有结果……\x02\x03",

            "#04008F……真是的，\x01",
            "到底发生了什么事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x109,
        "#12P#10108F真是很让人担心呢……\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x105,
        (
            "#12P#10301F嗯……\x01",
            "既然艾尼格玛无法接通，\x01",
            "那就表示她们不在自治州吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x8,
        (
            "#5P#04006F我也曾这样想过，\x01",
            "但在车站和空港都没有\x01",
            "查到她们的乘坐记录。\x02\x03",

            "#04001F在贝尔加德门和唐古拉姆门\x01",
            "也没有通行记录。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#12P#00001F这……\x01",
            "这就太奇怪了。\x02",
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
            "#12P#00203F……如果林小姐她们\x01",
            "还在自治州内……\x02\x03",

            "#00200F说不定有个办法\x01",
            "可以确定她们的所在地。\x02",
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

    def lambda_C4C4():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C4C4)
    Sleep(50)

    def lambda_C4D4():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C4D4)
    Sleep(50)

    def lambda_C4E4():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C4E4)
    Sleep(50)

    def lambda_C4F4():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C4F4)
    Sleep(50)

    def lambda_C504():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C504)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    #C0461
    ChrTalk(
        0x101,
        "#11P#00005F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        "#5P#04005F什么什么！究竟是什么办法！？\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#12P#00203F我记得艾尼格玛Ⅱ\x01",
            "存在一些尚处于研究阶段的功能。\x02\x03",

            "#00200F其中之一，就是在紧急时刻\x01",
            "发送警报信号。\x02",
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
        "#12P#10105F哎！？\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x102,
        "#00105F真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x103,
        (
            "#12P#00206F利用导力器内的备用导力，\x01",
            "每间隔一定时间，就会自动发送\x01",
            "特殊频率的导力波……\x02\x03",

            "但好像是由于导力波的信号太弱，\x01",
            "所以还无法正式实用。\x02\x03",

            "#00201F不过，这个功能似乎\x01",
            "并未取消，仍然保留了下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x109,
        (
            "#12P#10101F如此说来，只要能想办法\x01",
            "确认到那道微弱的导力波……！\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "#5P#04001F就可以确认林和艾欧莉娅\x01",
            "的所在地了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x103,
        (
            "#12P#00204F似乎有一试的价值。\x02\x03",

            "#00202F罗伯兹主任对这个功能\x01",
            "有比较详细的了解，\x01",
            "我们去ＩＢＣ找他吧。\x02\x03",

            "他大概可以帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#11P#00000F明白了，我们走吧。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#5P#04006F……给你们添麻烦了啊，\x01",
            "真是帮了大忙。\x02\x03",

            "#04000F如果有什么新情况，\x01",
            "就再和我联络吧。\x02\x03",

            "要是形势需要，\x01",
            "我会把亚里欧斯他们叫回来的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C91C():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C91C)
    Sleep(50)

    def lambda_C92C():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C92C)
    Sleep(50)

    def lambda_C93C():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C93C)
    Sleep(50)

    def lambda_C94C():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C94C)
    Sleep(50)

    def lambda_C95C():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C95C)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    #C0472
    ChrTalk(
        0x102,
        "#12P#00100F明白了。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x105,
        (
            "#12P#10302F那好，我们这就\x01",
            "去ＩＢＣ吧。\x02",
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

    # Function_28_C057 end

    def Function_29_CA0A(): pass

    label("Function_29_CA0A")

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

    def lambda_CB1A():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CB1A)
    Sleep(0)

    def lambda_CB2A():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CB2A)
    Sleep(0)

    def lambda_CB3A():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CB3A)
    Sleep(0)

    def lambda_CB4A():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CB4A)
    Sleep(0)

    def lambda_CB5A():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CB5A)
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
    SetChrName("芙兰的声音")

    #A0474
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "各位，导力艇已经\x01",
            "停靠在港湾区的码头了。\x02\x03",

            "应该马上就可以乘坐。\x02",
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
            "#00006F是吗，谢谢啦。\x02\x03",

            "#00001F不好意思啊，芙兰，\x01",
            "突然向你提出了如此麻烦的要求。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0476
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不会不会，正是在这种时候，\x01",
            "才更要尽力援助大家～\x02\x03",

            "不过，南部的湿地吗……\x01",
            "大家一定要多加小心哦。\x02",
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
            "#00000F嗯，我们会牢记在心的。\x02",
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
            "#12P#10101F船已经\x01",
            "准备好了吗？\x02",
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
            "#5P#00002F嗯，芙兰这么快就准备好了，\x01",
            "真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#5P#04006F呼，这次真是\x01",
            "多亏有你们帮忙啊。\x02\x03",

            "#04001F不过，真的没问题吗？\x02\x03",

            "只要再等一个小时左右，\x01",
            "亚里欧斯他们应该就能回来了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CE64():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CE64)
    Sleep(50)

    def lambda_CE74():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CE74)
    Sleep(50)

    def lambda_CE84():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE84)
    Sleep(50)

    def lambda_CE94():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CE94)
    Sleep(50)

    def lambda_CEA4():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CEA4)
    Sleep(50)

    def lambda_CEB4():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CEB4)
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
            "#6P#00303F不必了，我们还是\x01",
            "先过去比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x102,
        (
            "#12P#00108F是啊……\x01",
            "毕竟还不知道发生了什么情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x105,
        (
            "#12P#10302F嗯，等他们回来以后，\x01",
            "让他们追过来就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "#5P#04000F……明白了。\x02\x03",

            "#04003F林和艾欧莉娅\x01",
            "都是接近Ａ级水平的优秀游击士。\x02\x03",

            "那两人竟然会同时被困，\x01",
            "连联络都没有发回来……\x02\x03",

            "#04001F目前还不知道发生了什么情况，\x01",
            "请你们一定要小心啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#12P#00013F是……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    #C0486
    ChrTalk(
        0x103,
        (
            "#6P#00201F准备完毕以后，\x01",
            "我们就去码头吧。\x02",
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

    # Function_29_CA0A end

    def Function_30_D0C4(): pass

    label("Function_30_D0C4")

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
        "#00001F不好意思。\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x102,
        "#00103F打扰了。\x02",
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

    def lambda_D340():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_D340)
    Sleep(50)

    def lambda_D350():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_D350)
    Sleep(50)

    def lambda_D360():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_D360)
    Sleep(50)

    def lambda_D370():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_D370)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    Sleep(1000)

    def lambda_D393():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D393)

    def lambda_D3AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D3AD)
    Sleep(600)

    def lambda_D3C1():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D3C1)

    def lambda_D3DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D3DB)
    Sleep(900)

    def lambda_D3EF():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D3EF)

    def lambda_D409():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D409)
    Sleep(600)

    def lambda_D41D():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D41D)

    def lambda_D437():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D437)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0489
    ChrTalk(
        0x8,
        "#04005F#6P是你们……\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x9,
        "#6P啊，这不是罗伊德和各位吗……\x02",
    )

    CloseMessageWindow()

    def lambda_D499():

        label("loc_D499")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D499")

    QueueWorkItem2(0x9, 2, lambda_D499)

    def lambda_D4AB():

        label("loc_D4AB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D4AB")

    QueueWorkItem2(0xA, 2, lambda_D4AB)

    def lambda_D4BD():

        label("loc_D4BD")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_D4BD")

    QueueWorkItem2(0xC, 2, lambda_D4BD)

    def lambda_D4CF():
        OP_96(0xFE, 0x384, 0x0, 0x206C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D4CF)
    Sleep(200)

    def lambda_D4EC():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x1E78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D4EC)
    Sleep(100)

    def lambda_D509():
        OP_96(0xFE, 0x578, 0x0, 0x1C84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D509)
    Sleep(100)

    def lambda_D526():
        OP_96(0xFE, 0xC8, 0x0, 0x1A90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D526)
    Sleep(1500)
    Fade(500)
    OP_68(1000, 1100, 9900, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)

    def lambda_D576():
        OP_96(0xFE, 0xA8C, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D576)
    Sleep(100)

    def lambda_D593():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D593)
    WaitChrThread(0x103, 1)
    EndChrThread(0xC, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    #C0491
    ChrTalk(
        0x104,
        (
            "#00306F#12P哎呀呀，你们这是怎么了，\x01",
            "全都聚在这里，一副无精打采的模样。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xA,
        (
            "#5P本想说\x01",
            "『用不着你多管闲事』……\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xA,
        "#5P……唉，但确实无法否认啊。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xB,
        (
            "#5P实在是想不通，\x01",
            "亚里欧斯先生为什么会……\x02\x03",

            "唉……真是犹如晴天霹雳。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xC,
        (
            "#5P之前真是一丝征兆\x01",
            "都没有感觉到呢……\x02\x03",

            "如果硬要说有什么不对劲，\x01",
            "大概也就是他最近去兰花塔\x01",
            "的次数有些多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x8,
        (
            "#5P#04006F是啊……\x01",
            "本以为只是去商讨\x01",
            "协会今后的应对方针而已。\x02\x03",

            "#04008F没想到竟然是在\x01",
            "为这种事情做准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x101,
        (
            "#12P#00006F……其实我们就是\x01",
            "为了了解此事而来的。\x02\x03",

            "#00001F亚里欧斯先生现在\x01",
            "还隶属于协会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x8,
        (
            "#5P#04001F……他昨晚突然递交了辞呈，\x01",
            "并交还了游击士徽章。\x02\x03",

            "#04006F在那之前，他已经把自己手上的工作\x01",
            "全部完成了，并且制定好了今后的应对方针，\x01",
            "倒也符合他的一贯作风……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x102,
        "#12P#00108F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x103,
        (
            "#12P#00206F有始有终，一丝不苟，\x01",
            "确实是亚里欧斯先生的风格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xA,
        (
            "#5P……可是如此唐突地提出辞职，\x01",
            "终究有些问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xA,
        (
            "#5P而且竟然还担任了『克洛斯贝尔独立国』\x01",
            "的『国防军』长官……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        (
            "#5P……这样说可能有点不妥，\x01",
            "但埃雷波尼亚帝国的反应实在是让人恐惧。\x02\x03",

            "#5P总统竟然会以冻结资产\x01",
            "这种方式来威胁两大国……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xB,
        (
            "#5P……是啊……\x01",
            "共和国的反应也很令人担心。\x02",
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
            "#11P……不过……\x01",
            "我却并不是无法理解\x01",
            "亚里欧斯先生的心情。\x02",
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

    def lambda_DB0C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DB0C)
    Sleep(50)

    def lambda_DB1C():
        TurnDirection(0xB, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_DB1C)
    Sleep(50)

    def lambda_DB2C():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_DB2C)
    Sleep(50)

    def lambda_DB3C():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DB3C)
    Sleep(50)

    def lambda_DB4C():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DB4C)
    Sleep(50)

    def lambda_DB5C():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DB5C)
    Sleep(50)

    def lambda_DB6C():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DB6C)
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
        "#5P斯克特……？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xB,
        "#5P这话如何说起？\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x9,
        (
            "#11P我和亚里欧斯先生一样，\x01",
            "也是出身于克洛斯贝尔市的……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x9,
        (
            "#11P确实如那场演说中所讲的一样，\x01",
            "几乎每年都会发生一两起\x01",
            "原因不明的奇怪事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x9,
        (
            "#11P虽然无法了解真相……\x01",
            "但大家都能隐隐察觉到，\x01",
            "那是帝国或共和国搞的鬼。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xA,
        "#5P…………这……………\x02",
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
            "#11P最近倒是并没有\x01",
            "再发生过那样的事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x9,
        (
            "#11P五年前，将亚里欧斯先生的妻子\x01",
            "和小滴卷入的那起事故，\x01",
            "应该就是最后一起吧。\x02",
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
        "#6P#00011F啊……\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xC,
        "#5P莫非……\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "#5P#04003F……五年前，在大路上发生了\x01",
            "运输车爆炸起火的事故……\x02\x03",

            "#04008F当时将原因归结为导力机关的失控\x01",
            "与货物具有可燃性……\x01",
            "但可疑的地方实在是太多了。\x02\x03",

            "#04001F被卷进那场事故的\x01",
            "纱绫小姐不幸身亡……\x01",
            "小滴也丧失了视力。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x104,
        "#12P#00301F竟然还有这样的往事……\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x103,
        (
            "#6P#00208F……以前也曾听到过\x01",
            "一些零散的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x102,
        (
            "#6P#00106F所以，亚里欧斯先生\x01",
            "才辞去了警察的工作，转入协会……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "#5P#04006F自那之后，\x01",
            "我与亚里欧斯开始来往……\x02\x03",

            "有关此事，他虽然从未提及过一句，\x01",
            "但想必是一直都耿耿于怀吧。\x02\x03",

            "#04008F……如果这样一想，\x01",
            "他如今接受如此重任，\x01",
            "倒也可以让人理解。\x02",
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
            "#12P#00003F米歇尔先生。\x02\x03",

            "#00001F虽然明知很失礼，但还请容我一问……\x01",
            "在亚里欧斯先生的行程表中，\x01",
            "是否存在一些可疑之处？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E13C():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_E13C)
    Sleep(50)

    def lambda_E14C():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_E14C)
    Sleep(50)

    def lambda_E15C():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_E15C)
    Sleep(50)

    def lambda_E16C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E16C)
    Sleep(50)

    def lambda_E17C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E17C)
    Sleep(50)

    def lambda_E18C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E18C)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0524
    ChrTalk(
        0x8,
        "#5P#04005F哎？\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xC,
        "#5P罗伊德，这是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        (
            "#12P#00006F『国防军』的司令长官……\x02\x03",

            "如此重要的职位，我想并不是\x01",
            "可以突然授予的。\x02\x03",

            "#00001F迪塔市长……\x01",
            "不，迪塔总统与亚里欧斯先生之间\x01",
            "恐怕早就已经达成默契了吧？\x02\x03",

            "而且并非最近，而是在稍久之前。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        "#5P#04008F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_E2D1():
        TurnDirection(0xB, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_E2D1)
    Sleep(50)

    def lambda_E2E1():
        TurnDirection(0xA, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_E2E1)
    Sleep(50)

    def lambda_E2F1():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_E2F1)
    Sleep(50)

    def lambda_E301():
        TurnDirection(0xC, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_E301)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    def lambda_E321():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E321)

    def lambda_E32E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E32E)

    def lambda_E33B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E33B)

    #C0528
    ChrTalk(
        0xB,
        "#12P米歇尔……？\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xA,
        "难道……真的是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x8,
        (
            "#5P#04006F……的确，\x01",
            "偶尔会出现亚里欧斯的实际行程与\x01",
            "报告中记载的内容不一致的情况。\x02\x03",

            "#04008F由于他的工作过于繁重，\x01",
            "所以我一直都认为这不足为奇……\x02\x03",

            "#04001F……但现在仔细想想，\x01",
            "亚里欧斯写的报告竟会出现差错，\x01",
            "这明显是极其不正常的。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x9,
        (
            "也就是说，在那些时间里，\x01",
            "他是在与迪塔市长接触吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x8,
        (
            "#5P#04003F……恐怕也只有\x01",
            "这种可能性了吧。\x02\x03",

            "#04001F罗伊德，你果然名不虚传，\x01",
            "真是惊人的洞察力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        (
            "#12P#00006F哪里……\x01",
            "提出了失礼的问题，很抱歉。\x02\x03",

            "#00003F那个……既然已经失礼了，\x01",
            "我就顺便再请教一个问题……\x02\x03",

            "#00008F亚里欧斯先生的实际行程\x01",
            "与行程表中记载的内容出现不一致的情况……\x02\x03",

            "#00013F是否在半年之前\x01",
            "就已经有了？\x02",
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

    def lambda_E66E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E66E)

    def lambda_E67B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E67B)
    Sleep(50)

    def lambda_E68B():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_E68B)
    Sleep(50)

    def lambda_E69B():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_E69B)
    Sleep(50)

    def lambda_E6AB():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_E6AB)
    Sleep(50)

    def lambda_E6BB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E6BB)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x104, 0)

    #C0534
    ChrTalk(
        0x102,
        "#6P#00105F半年之前……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#12P#00200F……也就是迪塔先生\x01",
            "还没有成为市长的时候吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x8,
        (
            "#5P#04006F嗯，这个嘛……\x01",
            "那么久以前的事情，\x01",
            "实在是记不起来了……\x02\x03",

            "#04005F啊，的确！比如那次！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E79A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E79A)
    Sleep(50)

    def lambda_E7AA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E7AA)

    def lambda_E7B7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E7B7)

    #C0537
    ChrTalk(
        0x101,
        "#12P#00005F那次……？\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x8,
        (
            "#5P#04004F是在创立纪念庆典的最终日。\x02\x03",

            "#04000F他由于工作原因，\x01",
            "需要出差去雷米菲利亚公国……\x02\x03",

            "但最后却突然取消了计划，\x01",
            "而且并没有在报告中记录。\x02",
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
        "#12P#00011F哎……\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x8,
        (
            "#5P#04005F事后我察觉到此事，\x01",
            "并向他询问，但他解释为\x01",
            "工作太忙，所以没有把报告写好……\x02\x03",

            "#04001F……怎么，你注意到什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xB,
        (
            "#5P算啦，纪念庆典时\x01",
            "忙得都快死人了……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xA,
        (
            "#5P就算报告中稍微出现小差错，\x01",
            "应该也没什么奇怪的吧……？\x02",
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
        "#6P#00108F……纪念庆典的最终日……\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x103,
        (
            "#12P#00201F说到最终日，\x01",
            "也就是『那一天』……\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#00301F#12P难道与那件事有什么联系吗？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#11P#00006F……现在还不清楚，\x01",
            "但我总觉得存在着某些联系。\x02\x03",

            "#00008F至今为止，我们由于太过忙碌而遗漏无视的\x01",
            "一个又一个『点』，如今已经……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_EB40():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EB40)
    Sleep(50)

    def lambda_EB50():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EB50)

    #C0548
    ChrTalk(
        0x101,
        "#12P#00011F不好意思，我先接一下。\x02",
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
            "#00001F您好，这里是克洛斯贝尔警察局，\x01",
            "特别任务支援科──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0550
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯～？\x01",
            "不对不对，应该是\x01",
            "『克洛斯贝尔国防军·特别任务支援科』吧？\x02",
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
            "#00013F……你是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0552
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵呵……\x01",
            "猜猜看，我是谁？\x02\x03",

            "猜对的人可以得到\x01",
            "豪华奖品哟～\x02",
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
            "#00006F……无聊的玩笑就到此为止吧。\x02\x03",

            "#00010F你还好意思……\x01",
            "来克洛斯贝尔吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0554
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哎呀呀，被人讨厌了呢。\x02\x03",

            "现在的气氛好像很紧张啊，\x01",
            "不过能不能过来聊聊？\x02\x03",

            "呵呵，不会让你们白跑一趟的哦。\x02",
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

            "#00006F……明白了，\x01",
            "要去哪里找你？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0556
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『深红商会』……\x01",
            "嗯，大概还是改叫\x01",
            "原『鲁巴彻商会』比较好吧。\x02\x03",

            "就在那里的会长室好了。\x02",
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
            "#00008F是地下的那个房间吗……\x01",
            "明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那我就等着你们啦～\x02",
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
            "#6P#00101F莫非……\x01",
            "是行踪不明的曹先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x103,
        (
            "#12P#00200F说起来，\x01",
            "兰迪前辈之前不辞而别的时候，\x01",
            "他就和我们联络过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x104,
        "#00305F还有这么回事？\x02",
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
            "#5P#00003F不。\x02\x03",

            "#00013F是帝国军的雷克特大尉。\x02",
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
        "#6P#00107F什么！？\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#12P#00211F那个人……竟然又来\x01",
            "克洛斯贝尔了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x104,
        (
            "#00301F#12P……确实就像你刚才所说，\x01",
            "他怎么还好意思跑来啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x101,
        (
            "#5P#00006F总之，他正在鲁巴彻商会的旧址，\x01",
            "似乎有话要和我们说。\x02\x03",

            "#00001F考虑到他与『赤色星座』之间的瓜葛，\x01",
            "我们绝不能掉以轻心……\x01",
            "但这个面还是要去见的。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x104,
        "#00306F#12P说得对……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x103,
        "#12P#00201F不入虎穴，焉得虎子啊。\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x102,
        (
            "#6P#00103F……过去之前，似乎有必要\x01",
            "做好万全的准备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x8,
        "#5P#04006F你们也真是很辛苦呢……\x02",
    )

    CloseMessageWindow()

    def lambda_F2A3():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F2A3)
    Sleep(50)

    def lambda_F2B3():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F2B3)
    Sleep(50)

    def lambda_F2C3():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F2C3)
    Sleep(50)

    def lambda_F2D3():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F2D3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0571
    ChrTalk(
        0x9,
        (
            "#11P看样子，是要去和\x01",
            "很麻烦的家伙会面了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "#5P情报局的亚兰德尔吗……\x01",
            "那可是个十分难对付的年轻人。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xB,
        (
            "#5P如果形势严峻，需要我们帮忙，\x01",
            "请不必客气，尽管开口。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xC,
        (
            "#5P没错，在湿地时还欠了\x01",
            "你们一份人情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x102,
        "#12P#00102F谢谢各位。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x103,
        (
            "#12P#00204F如果我们难以应付，\x01",
            "请大家务必帮忙。\x02",
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

    # Function_30_D0C4 end

    def Function_31_F4F9(): pass

    label("Function_31_F4F9")

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
    SetChrName("麦克道尔议长")

    #A0577
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W那么，如今的体制，是以宣称『调查独立意愿』的\x01",
            "居民投票为依据而决定的吗？\x02\x03",

            "答案是否定的！\x01",
            "在居民投票活动中，\x01",
            "只询问了『是否决心独立』而已。\x02\x03",

            "因此，国防军、克洛斯贝尔独立国……\x02\x03",

            "以及目前的总统制度\x01",
            "绝无丝毫正当性！\x07\x00\x02",
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

    # Function_31_F4F9 end

    def Function_32_F74A(): pass

    label("Function_32_F74A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3020, 1700, 4270, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22460, 0)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F8CB")
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

    def lambda_F816():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F816)

    def lambda_F827():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F827)
    Sleep(50)

    def lambda_F844():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F844)

    def lambda_F855():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F855)
    Sleep(700)

    def lambda_F872():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F872)

    def lambda_F883():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F883)
    Sleep(50)

    def lambda_F8A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F8A0)

    def lambda_F8B1():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F8B1)
    Jump("loc_FB4C")

    label("loc_F8CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FA0E")
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

    def lambda_F959():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F959)

    def lambda_F96A():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F96A)
    Sleep(50)

    def lambda_F987():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F987)

    def lambda_F998():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F998)
    Sleep(700)

    def lambda_F9B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F9B5)

    def lambda_F9C6():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F9C6)
    Sleep(50)

    def lambda_F9E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F9E3)

    def lambda_F9F4():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F9F4)
    Jump("loc_FB4C")

    label("loc_FA0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FB4C")
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

    def lambda_FA9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FA9C)

    def lambda_FAAD():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FAAD)
    Sleep(50)

    def lambda_FACA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FACA)

    def lambda_FADB():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FADB)
    Sleep(700)

    def lambda_FAF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FAF8)

    def lambda_FB09():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FB09)
    Sleep(50)

    def lambda_FB26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_FB26)

    def lambda_FB37():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FB37)

    label("loc_FB4C")

    OP_68(-2140, 1300, 5160, 3000)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    #C0578
    ChrTalk(
        0x1A2,
        (
            "#12P这里是游击士协会·\x01",
            "克洛斯贝尔分部……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0579
    ChrTalk(
        0x101,
        (
            "#5P#00005F……秦？\x01",
            "你为何要躲躲藏藏的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FBF7")

    def lambda_FBD7():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FBD7)
    Sleep(50)

    def lambda_FBE7():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FBE7)
    Sleep(300)
    Jump("loc_FC4E")

    label("loc_FBF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FC25")

    def lambda_FC05():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC05)
    Sleep(50)

    def lambda_FC15():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FC15)
    Sleep(300)
    Jump("loc_FC4E")

    label("loc_FC25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FC4E")

    def lambda_FC33():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC33)
    Sleep(50)

    def lambda_FC43():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FC43)
    Sleep(300)

    label("loc_FC4E")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0580
    ChrTalk(
        0x1A2,
        "#12P别、别多嘴，不用管我啦……！\x02",
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
            "#5P#N#04005F啊，是你们啊……\x01",
            "怎么带着一个可爱的小男孩？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FD27")

    def lambda_FCF7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FCF7)
    Sleep(50)

    def lambda_FD07():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD07)
    Sleep(50)

    def lambda_FD17():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FD17)
    Sleep(300)
    Jump("loc_FD9E")

    label("loc_FD27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FD65")

    def lambda_FD35():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FD35)
    Sleep(50)

    def lambda_FD45():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD45)
    Sleep(50)

    def lambda_FD55():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FD55)
    Sleep(300)
    Jump("loc_FD9E")

    label("loc_FD65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FD9E")

    def lambda_FD73():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FD73)
    Sleep(50)

    def lambda_FD83():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD83)
    Sleep(50)

    def lambda_FD93():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FD93)
    Sleep(300)

    label("loc_FD9E")


    #C0582
    ChrTalk(
        0x8,
        (
            "#5P#N#04000F站在那里会影响别人进出的，\x01",
            "到这边来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0583
    ChrTalk(
        0x102,
        "#12P#00105F好、好的……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(330, 1300, 10820, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21390, 0)
    OP_93(0x8, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FEF3")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x104, 1640, 0, 8800, 0)

    def lambda_FE82():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FE82)
    Sleep(50)

    def lambda_FE9F():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FE9F)
    Sleep(50)

    def lambda_FEBC():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FEBC)
    Sleep(50)

    def lambda_FED9():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FED9)
    Jump("loc_10074")

    label("loc_FEF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FFB6")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x109, 1640, 0, 8800, 0)

    def lambda_FF45():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FF45)
    Sleep(50)

    def lambda_FF62():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FF62)
    Sleep(50)

    def lambda_FF7F():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF7F)
    Sleep(50)

    def lambda_FF9C():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FF9C)
    Jump("loc_10074")

    label("loc_FFB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10074")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x105, 1640, 0, 8800, 0)

    def lambda_10008():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_10008)
    Sleep(50)

    def lambda_10025():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10025)
    Sleep(50)

    def lambda_10042():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10042)
    Sleep(50)

    def lambda_1005F():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1005F)

    label("loc_10074")

    OP_0D()
    WaitChrThread(0x101, 1)

    #C0584
    ChrTalk(
        0x8,
        (
            "#04000F#5P那个小男孩\x01",
            "到底是谁啊？\x02\x03",

            "#04005F莫非你们正在\x01",
            "带迷路的孩子寻找家长？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        "#12P#00012F那个，该怎么说才好呢……\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x1A2,
        (
            "#12P喂、喂！我问你！\x01",
            "『风之剑圣』现在在吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x8,
        (
            "#04004F#5P哎呀，口气好凶啊。\x02\x03",

            "#04000F亚里欧斯出去了，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x1A2,
        "#12P是、是吗……呼～\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x8,
        (
            "#04005F#5P怎么回事，好像松了口气的样子。\x02\x03",

            "#04003F嗯，这种口气，还有这种打扮……\x02\x03",

            "#04000F原来如此，\x01",
            "这个小家伙和『黑月』有关系吧，\x01",
            "莫非是长老的孙子？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10292")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1036F")

    label("loc_10292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10303")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1036F")

    label("loc_10303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1036F")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_1036F")


    #C0590
    ChrTalk(
        0x102,
        "#12P#00105F为、为什么连这都能……？\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x8,
        (
            "#04011F#5P呵呵呵，顺利\x01",
            "套出了答案啊。\x02\x03",

            "#04001F啊，顺便再说一句，不许在心里暗骂\x01",
            "『可恶的娘娘腔竟敢骗人』之类的话哦～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10482")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1055F")

    label("loc_10482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_104F3")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1055F")

    label("loc_104F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1055F")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_1055F")


    #C0592
    ChrTalk(
        0x101,
        "#12P#00012F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x1A2,
        (
            "#12P唔……这个人的外表和智谋\x01",
            "全都非同寻常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x1A2,
        (
            "#12P所以我才讨厌\x01",
            "游击士协会的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x8,
        (
            "#04006F#5P嗯～刚才的失礼之处\x01",
            "姑且不提，\x01",
            "这孩子确实是个很出色的『黑月』成员呢。\x02\x03",

            "#04008F真是后生可畏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10678")

    #C0596
    ChrTalk(
        0x104,
        "#12P#00303F嗯，我也有同感呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_106CD")

    label("loc_10678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_106A7")

    #C0597
    ChrTalk(
        0x109,
        "#12P#10106F嗯，我也有同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_106CD")

    label("loc_106A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_106CD")

    #C0598
    ChrTalk(
        0x105,
        "#12P#10304F呵呵，同感。\x02",
    )

    CloseMessageWindow()

    label("loc_106CD")


    #C0599
    ChrTalk(
        0x8,
        (
            "#04000F#5P不过，为什么要\x01",
            "对亚里欧斯保持\x01",
            "如此程度的警戒呢？\x02\x03",

            "我们与『黑月』之间\x01",
            "并不存在什么敌对关系啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x1A2,
        (
            "#12P哼、哼……\x01",
            "你们曾经多次坏过祖父大人他们的好事，\x01",
            "竟然还敢坦然自若地说这种话。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x1A2,
        (
            "#12P你知道我们因为『风之剑圣』和『不动』的阻碍\x01",
            "而蒙受过多大的损失吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        "#6P#00005F『不动』……？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x8,
        (
            "#04004F#5P嗯，『不动』金——\x02\x03",

            "#04000F共和国的Ａ级游击士，\x01",
            "他可是精通『泰斗流』古武术的达人哦。\x02\x03",

            "最近虽然很少过来了，\x01",
            "不过以前曾经多次来我们\x01",
            "克洛斯贝尔分部帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x102,
        (
            "#12P#00105F说起『泰斗流』，\x01",
            "不就是林小姐的……\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x8,
        (
            "#04000F#5P嗯，他算是林的师兄，\x01",
            "实力之强自不必说。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10952")

    #C0606
    ChrTalk(
        0x104,
        (
            "#12P#00300F原来如此，\x01",
            "游击士协会可真是强人云集啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109D9")

    label("loc_10952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10998")

    #C0607
    ChrTalk(
        0x109,
        (
            "#12P#10100F原来如此，\x01",
            "游击士协会可真是精英云集啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109D9")

    label("loc_10998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_109D9")

    #C0608
    ChrTalk(
        0x105,
        (
            "#12P#10300F原来如此，\x01",
            "游击士协会可真是强者云集啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109D9")


    #C0609
    ChrTalk(
        0x1A2,
        (
            "#12P的确如此，\x01",
            "但协会真正让人头疼的地方\x01",
            "还是他们的规约。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x1A2,
        (
            "#12P不管是不是什么大原则，\x01",
            "但协会总拿『保护民间人士』当万能挡箭牌，\x01",
            "未免也太过于为所欲为了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x8,
        (
            "#04004F#5P呵呵，只要遵守这项原则，\x01",
            "即使是『不干涉国家权力』这条规定，\x01",
            "有时也都可以打破呢。\x02\x03",

            "#04005F呃……这孩子，\x01",
            "小小年纪，究竟懂得多少事情啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        (
            "#12P#00000F确实……\x01",
            "老实说，真没想到他竟然懂这么多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x1A2,
        (
            "#12P哼哼，奉承我也没有好处哦。\x01",
            "总之，游击士协会的家伙实在是……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x8,
        (
            "#04006F#5P好啦好啦，批评协会虽然没什么，\x01",
            "但小孩子还是应该有些小孩子的样子。\x02\x03",

            "#04000F对了，小琪雅和小滴\x01",
            "现在正在二层呢。\x02\x03",

            "你去和她们开心地聊一聊，做个好朋友吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        (
            "#12P#00000F啊，说起来，\x01",
            "琪雅今天来这里打扰了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x102,
        (
            "#12P#00100F说的也是呢，\x01",
            "让小孩子们一起玩一会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x1A2,
        "#12P什、什么啊……你们说的是谁？\x02",
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

    # Function_32_F74A end

    def Function_33_10CFE(): pass

    label("Function_33_10CFE")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1940, 1100, 44370, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20320, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D68")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")

    label("loc_10D68")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10DC2")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x104, -2190, 0, 45050, 90)
    Jump("loc_10E61")

    label("loc_10DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10E14")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x109, -2190, 0, 45050, 90)
    Jump("loc_10E61")

    label("loc_10E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10E61")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x105, -2190, 0, 45050, 90)

    label("loc_10E61")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_END)), "loc_10EFA")

    def lambda_10E70():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10E70)
    Sleep(50)

    def lambda_10E80():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_10E80)
    Sleep(300)

    #C0618
    ChrTalk(
        0xD,
        (
            "#11P#01102F啊，是罗伊德和大家。\x01",
            "嘿嘿嘿，你们怎么来了？\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xE,
        (
            "#11P#06002F大家正在工作吧，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11079")

    label("loc_10EFA")

    SetScenarioFlags(0x14D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)

    #C0620
    ChrTalk(
        0xD,
        "#11P#01110F啊，是罗伊德和大家！\x02",
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
            "#11P#06002F啊……\x01",
            "大家好。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x101,
        (
            "#6P#00000F嘿，琪雅，\x01",
            "你们好像玩得很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x102,
        "#6P#00102F好久没见到小滴了呢。\x02",
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
            "呵呵，好久不见。\x02\x03",

            "各位好像\x01",
            "正在工作吧？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_11079")


    #C0625
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，算是\x01",
            "在工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x1A2,
        (
            "#6P什么啊，这两个孩子是谁？\x01",
            "是你们的朋友吗？\x02",
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
            "#11P#01105F哎～？\x01",
            "这孩子是谁啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xE,
        "#11P#06005F小男孩……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0629
    ChrTalk(
        0x1A2,
        "#6P谁、谁是小男孩啊！\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x1A2,
        (
            "#6P我是秦！\x01",
            "『黑月』长老之孙，\x01",
            "肩负着『黑月』未来的男子汉！\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xE,
        "#11P#06010F对、对不起。\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xD,
        (
            "#11P#01105F咦，虽然个子很小，\x01",
            "但和罗伊德一样，是个男子汉啊～？\x02\x03",

            "#01109F真了不起～\x01",
            "明明只有这么小的个子……\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x1A2,
        "#6P不、不要一直说个子小个子小了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1130E")
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
            "#11P#00304F哈哈，在阿琪面前，\x01",
            "连这个得意忘形的小鬼也都无所适从了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11441")

    label("loc_1130E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1139F")
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
            "#11P#10109F啊哈哈……\x01",
            "（不愧是小琪雅。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11441")

    label("loc_1139F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11441")
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
            "#11P#10309F呵呵，在琪雅面前，\x01",
            "连黑月的小少爷也都手足无措了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11441")

    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0637
    ChrTalk(
        0x102,
        (
            "#5P#00109F呵呵，秦……\x02\x03",

            "她是小琪雅，\x01",
            "她是小滴。\x02\x03",

            "#00100F她们两个年纪应该都比秦稍大吧？\x01",
            "那就是小姐姐啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0638
    ChrTalk(
        0x101,
        (
            "#11P#00000F啊，顺便一说，\x01",
            "小滴就是你刚才提到的\x01",
            "亚里欧斯先生的女儿哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0639
    ChrTalk(
        0x1A2,
        "#6P风、风之剑圣的……！\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x1A2,
        (
            "#6P既、既然是风之剑圣的女儿，\x01",
            "想必也是精通剑术的高手吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x1A2,
        (
            "#6P你一直都闭着双眼，\x01",
            "莫非是在进行『心眼』的训练吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11618")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_116C5")

    label("loc_11618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11671")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_116C5")

    label("loc_11671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_116C5")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_116C5")


    #C0642
    ChrTalk(
        0xD,
        "#11P#01105F心眼～？\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#11P#00005F『心眼』吗……\x01",
            "你竟然还知道这个啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xE,
        (
            "#11P#06002F啊哈哈……\x01",
            "那个……我只是眼睛看不见而已啦。\x02\x03",

            "虽然听力因此而锻炼得很好，\x01",
            "但我可不像爸爸那样厉害哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0645
    ChrTalk(
        0x1A2,
        "#6P这、这可真是太失礼了！\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x1A2,
        (
            "#6P竟然说了些绅士不该说的话……\x01",
            "还请原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xE,
        "#11P#06002F呵呵，不用在意啦。\x02",
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x101,
        "#11P#00005F（哦……？）\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        (
            "#6P#00102F（呵呵，果然是个\x01",
            "  本性善良的好孩子呢。）\x02",
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

    # Function_33_10CFE end

    def Function_34_118B6(): pass

    label("Function_34_118B6")

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
        "#11P#01110F啊，是罗伊德和大家！\x02",
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
            "#11P#06002F啊……\x01",
            "各位好。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x101,
        (
            "#6P#00000F嘿，琪雅，\x01",
            "你们好像玩得很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x102,
        "#6P#00100F好久没见到小滴了呢。\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xE,
        "#11P#06000F呵呵，好久不见。\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x105,
        (
            "#6P#10305F啊，这孩子就是\x01",
            "『风之剑圣』的女儿吗？\x02\x03",

            "#10309F呵呵，果然和你们说的一样，\x01",
            "是个可爱的孩子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_11CA6")

    #C0656
    ChrTalk(
        0x109,
        "#6P#10109F怎么样，没骗你吧～\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0657
    ChrTalk(
        0xE,
        (
            "#11P#06005F这声音……\x01",
            "是诺艾尔小姐吧？\x02\x03",

            "#06002F之前还麻烦您帮我\x01",
            "给爸爸准备礼物，十分感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0658
    ChrTalk(
        0x109,
        (
            "#6P#10105F哇，你还记得我啊？\x02\x03",

            "#10109F当时只有过那么短暂的接触……\x01",
            "呵呵，好高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xE,
        (
            "#11P#06002F嘿嘿，\x01",
            "因为我听琪雅告诉我了，\x01",
            "支援科加入了新成员。\x02\x03",

            "#06000F嗯……那位是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x105,
        (
            "#6P#10302F瓦吉·赫米斯菲亚。\x01",
            "呵呵，请多关照哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E35")

    label("loc_11CA6")


    #C0661
    ChrTalk(
        0x109,
        "#6P#10109F嗯，果然和芙兰说的一样呢～！\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0662
    ChrTalk(
        0xE,
        (
            "#11P#06005F嗯……那两位是谁呢？\x02\x03",

            "我听琪雅说过，\x01",
            "支援科加入了新成员。\x01",
            "莫非就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x109,
        (
            "#6P#10105F啊，如此说来，我们还是初次见面呢。\x02\x03",

            "#10109F我是诺艾尔·希卡。\x01",
            "也就是芙兰的姐姐啦，\x01",
            "这样说你就知道了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xE,
        (
            "#11P#06005F啊，芙兰小姐的……\x01",
            "这样一说，确实能\x01",
            "感觉到有些相似呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x105,
        (
            "#6P#10302F我是瓦吉·赫米斯菲亚。\x01",
            "呵呵，请多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E35")


    #C0666
    ChrTalk(
        0xE,
        (
            "#11P#06002F是！\x01",
            "请多关照！\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xD,
        (
            "#11P#01109F滴，滴！\x01",
            "你也要自我介绍啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xE,
        (
            "#11P#06005F啊……\x01",
            "说得对，嗯……\x02",
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
            "我是琪雅的朋友，\x01",
            "名字是滴·马克莱因。\x02\x03",

            "我和爸爸都曾受到\x01",
            "支援科各位的关照。\x02\x03",

            "今后也请多多指教。\x02",
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
            "#6P#00102F啊哈哈，这个……\x01",
            "应该说是我们经常受到\x01",
            "亚里欧斯先生的关照才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x101,
        "#6P#00003F嗯，确实如此呢……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0672
    ChrTalk(
        0xE,
        (
            "#11P#06010F哪、哪里的话。\x02\x03",

            "在之前那次事件中，\x01",
            "多亏有大家的帮助……\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈，还是老样子，\x01",
            "真是个严肃又懂礼貌的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xD,
        (
            "#11P#01102F嘿嘿，大家是来和\x01",
            "琪雅一起玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#6P#00009F啊，不是的，\x01",
            "因为小滴难得来这里，\x01",
            "所以过来打个招呼。\x02\x03",

            "#00000F我们还要去继续工作，\x01",
            "今天一天，琪雅就和小滴\x01",
            "一起开心玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xD,
        "#11P#01109F嗯，知道啦！\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xE,
        (
            "#11P#06002F那个……\x01",
            "请大家工作加油哦。\x02",
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

    # Function_34_118B6 end

    def Function_35_121E0(): pass

    label("Function_35_121E0")

    EventBegin(0x1)
    SetChrPos(0x0, -2110, 0, 740, 0)
    EventEnd(0x4)
    Return()

    # Function_35_121E0 end

    SaveToFile()

Try(main)
