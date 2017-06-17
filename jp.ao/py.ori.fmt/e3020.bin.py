from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3020.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x00D0,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("e3020", "e3020_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3020",                  # 0
        "正騎士アッバス",         # 1
        "ヨナ",                   # 2
        "ワジ",                   # 3
        "ティオ",                 # 4
        "フラン",                 # 5
        "リーシャ",               # 6
        "ランディ",               # 7
        "グレイス",               # 8
        "ノエル",                 # 9
        "エリィ",                 # 10
        "マクダエル議長",         # 11
        "神狼ツァイト",           # 12
        "ダドリー捜査官",         # 13
        "従騎士ヴェントス",       # 14
        "従騎士ジュノー",         # 15
        "従騎士セサル",           # 16
        "従騎士マーカス",         # 17
        "シスター・リース",       # 18
        "ケビン神父",             # 19
        "ノエル",                 # 20
        "フラン",                 # 21
        "グレイス",               # 22
        " ",                      # 23
        "SE制御",                 # 24
    ))

    AddCharChip((
        "chr/ch06712.itc",                   # 00
        "chr/ch06100.itc",                   # 01
        "chr/ch03100.itc",                   # 02
        "chr/ch03102.itc",                   # 03
        "chr/ch00202.itc",                   # 04
        "chr/ch06902.itc",                   # 05
        "chr/ch03200.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch06000.itc",                   # 08
        "chr/ch02900.itc",                   # 09
        "chr/ch00102.itc",                   # 0A
        "chr/ch05800.itc",                   # 0B
        "chr/ch02710.itc",                   # 0C
        "chr/ch00900.itc",                   # 0D
        "chr/ch48400.itc",                   # 0E
        "chr/ch48402.itc",                   # 0F
        "chr/ch02702.itc",                   # 10
        "chr/ch02708.itc",                   # 11
        "chr/ch00200.itc",                   # 12
        "chr/ch00302.itc",                   # 13
        "chr/ch02902.itc",                   # 14
        "chr/ch03202.itc",                   # 15
        "chr/ch00902.itc",                   # 16
        "chr/ch06102.itc",                   # 17
        "chr/ch06002.itc",                   # 18
        "chr/ch05802.itc",                   # 19
        "chr/ch06710.itc",                   # 1A
        "chr/ch06900.itc",                   # 1B
    ))

    DeclNpc(-39,     490,     2500,    0,    261,  0x0, 0,   0,   0,   255, 255, 1,   26,  255,  0)
    DeclNpc(-3119,   -1350,   7039,    315,  389,  0x0, 0,   1,   0,   255, 255, 1,   34,  255,  0)
    DeclNpc(101790,  150,     -93959,  90,   389,  0x0, 0,   2,   0,   0,   0,   1,   15,  255,  0)
    DeclNpc(-3119,   -1350,   7039,    315,  389,  0x0, 0,   18,  0,   0,   0,   1,   2,   255,  0)
    DeclNpc(3000,    -1350,   6960,    45,   389,  0x0, 0,   5,   0,   255, 255, 1,   31,  255,  0)
    DeclNpc(-1500,   0,       -1500,   0,    389,  0x0, 0,   6,   0,   0,   0,   1,   19,  255,  0)
    DeclNpc(98970,   170,     -970,    0,    389,  0x0, 0,   7,   0,   0,   0,   1,   6,   255,  0)
    DeclNpc(-3000,   -1490,   6000,    0,    389,  0x0, 0,   8,   0,   255, 255, 1,   37,  255,  0)
    DeclNpc(100309,  170,     959,     270,  389,  0x0, 0,   9,   0,   0,   0,   1,   12,  255,  0)
    DeclNpc(100169,  100,     -102720, 270,  389,  0x0, 0,   10,  0,   0,   0,   1,   0,   255,  0)
    DeclNpc(98440,   100,     -101110, 180,  389,  0x0, 0,   11,  0,   255, 255, 1,   39,  255,  0)
    DeclNpc(97610,   0,       -97069,  180,  405,  0x0, 0,   12,  0,   255, 255, 1,   22,  255,  0)
    DeclNpc(97639,   170,     959,     90,   389,  0x0, 0,   13,  0,   255, 255, 1,   24,  255,  0)
    DeclNpc(103569,  0,       -97089,  270,  257,  0x0, 0,   14,  0,   0,   0,   1,   43,  255,  0)
    DeclNpc(103949,  0,       -209,    270,  257,  0x0, 0,   14,  0,   0,   0,   1,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(102510,  0,       -97020,  1000,    103570,  1500,    -97090,  0x007E, 1,  42, 0x0000)
    DeclActor(102710,  0,       -200,    400,     103950,  1500,    -210,    0x007E, 1,  45, 0x0000)
    DeclActor(2350,    0,       -92230,  800,     2350,    1500,    -92230,  0x007C, 1,  48, 0x0000)
    DeclActor(103750,  0,       -105640, 2000,    103750,  1500,    -105640, 0x007C, 1,  49, 0x0000)

    ChipFrameInfo(1260, 0)                                       # 0

    ScpFunction((
        "Function_0_4EC",          # 00, 0
        "Function_1_59C",          # 01, 1
        "Function_2_116A",         # 02, 2
        "Function_3_12CA",         # 03, 3
        "Function_4_12EA",         # 04, 4
        "Function_5_13FF",         # 05, 5
        "Function_6_14BC",         # 06, 6
        "Function_7_1573",         # 07, 7
        "Function_8_1A5F",         # 08, 8
        "Function_9_2387",         # 09, 9
        "Function_10_36B5",        # 0A, 10
        "Function_11_36F7",        # 0B, 11
        "Function_12_3C50",        # 0C, 12
        "Function_13_3D0D",        # 0D, 13
        "Function_14_4367",        # 0E, 14
        "Function_15_4382",        # 0F, 15
        "Function_16_50D2",        # 10, 16
        "Function_17_5BB6",        # 11, 17
        "Function_18_60B6",        # 12, 18
        "Function_19_60DB",        # 13, 19
        "Function_20_61DB",        # 14, 20
        "Function_21_7076",        # 15, 21
        "Function_22_72CF",        # 16, 22
        "Function_23_858D",        # 17, 23
        "Function_24_88C2",        # 18, 24
        "Function_25_8CBC",        # 19, 25
        "Function_26_8CD2",        # 1A, 26
        "Function_27_8CEB",        # 1B, 27
        "Function_28_937E",        # 1C, 28
        "Function_29_939E",        # 1D, 29
        "Function_30_A533",        # 1E, 30
        "Function_31_A9EE",        # 1F, 31
        "Function_32_B2F2",        # 20, 32
        "Function_33_B321",        # 21, 33
        "Function_34_B344",        # 22, 34
        "Function_35_B369",        # 23, 35
        "Function_36_B381",        # 24, 36
        "Function_37_B3A4",        # 25, 37
        "Function_38_B3BE",        # 26, 38
        "Function_39_BF25",        # 27, 39
        "Function_40_C163",        # 28, 40
        "Function_41_C66B",        # 29, 41
        "Function_42_C690",        # 2A, 42
        "Function_43_CBEB",        # 2B, 43
        "Function_44_CC0B",        # 2C, 44
        "Function_45_D082",        # 2D, 45
    ))


    def Function_0_4EC(): pass

    label("Function_0_4EC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_524"),
        (1, "loc_530"),
        (2, "loc_53C"),
        (3, "loc_548"),
        (4, "loc_554"),
        (5, "loc_560"),
        (6, "loc_56C"),
        (SWITCH_DEFAULT, "loc_578"),
    )


    label("loc_524")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_530")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_53C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_548")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_554")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_560")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_56C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_578")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_584")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_59B")

    Return()

    # Function_0_4EC end

    def Function_1_59C(): pass

    label("Function_1_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_6F5")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 104200, 100, 5070, 90)
    Jump("loc_61E")

    label("loc_5F5")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_61E")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0x10, 100250, 100, -104800, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_84E")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 104200, 100, 5070, 90)
    Jump("loc_777")

    label("loc_74E")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_777")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0x10, 100250, 100, -104800, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_963")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2110, -1490, 6190, 315)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A8D")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 97620, 170, 970, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -3050, 0, -2960, 0)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88")
    SetChrFlags(0x12, 0x10)

    label("loc_A88")

    Jump("loc_F57")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BCF")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1340, 0, -1280, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 97640, 170, 960, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrPos(0x8, 140, 0, -1320, 89)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, 100170, 100, -102720, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC5")
    SetChrFlags(0xB, 0x10)

    label("loc_BC5")

    SetChrFlags(0x13, 0x10)
    Jump("loc_F57")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_CD8")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xE, 100170, 100, -102720, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3750, 0, -2770, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 2620, 0, -2780, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD3")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_CD3")

    Jump("loc_F57")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_DC1")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 100560, 0, 2190, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 100170, 100, -102720, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, 98440, 100, -101110, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_END)), "loc_DBC")
    SetChrFlags(0xF, 0x10)

    label("loc_DBC")

    Jump("loc_F57")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E4E")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDE")
    SetChrFlags(0xB, 0x10)

    label("loc_DDE")

    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1410, 0, -100570, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_F57")

    label("loc_E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_EEC")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrPos(0x8, -2110, -1490, 6190, 315)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE7")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_EE7")

    Jump("loc_F57")

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F57")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F41")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    Jump("loc_F57")

    label("loc_F41")

    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F93")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAA")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC1")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_FD8")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 4)
    Jump("loc_1169")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_FEC")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)
    Jump("loc_1169")

    label("loc_FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1003")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 9)
    Jump("loc_1169")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1017")
    ClearScenarioFlags(0x22, 3)
    Event(0, 13)
    Jump("loc_1169")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_102B")
    ClearScenarioFlags(0x22, 4)
    Event(0, 15)
    Jump("loc_1169")

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_103F")
    ClearScenarioFlags(0x22, 5)
    Event(0, 16)
    Jump("loc_1169")

    label("loc_103F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1059")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 17)
    Jump("loc_1169")

    label("loc_1059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_106D")
    ClearScenarioFlags(0x22, 7)
    Event(0, 20)
    Jump("loc_1169")

    label("loc_106D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_1081")
    ClearScenarioFlags(0x23, 0)
    Event(0, 22)
    Jump("loc_1169")

    label("loc_1081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1095")
    ClearScenarioFlags(0x23, 1)
    Event(0, 24)
    Jump("loc_1169")

    label("loc_1095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_10A9")
    ClearScenarioFlags(0x23, 2)
    Event(0, 27)
    Jump("loc_1169")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_10C0")
    ClearScenarioFlags(0x23, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 29)
    Jump("loc_1169")

    label("loc_10C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_10D4")
    ClearScenarioFlags(0x23, 4)
    Event(0, 30)
    Jump("loc_1169")

    label("loc_10D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_10E8")
    ClearScenarioFlags(0x23, 5)
    Event(0, 31)
    Jump("loc_1169")

    label("loc_10E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_10FC")
    ClearScenarioFlags(0x23, 6)
    Event(0, 38)
    Jump("loc_1169")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_1110")
    ClearScenarioFlags(0x23, 7)
    Event(0, 40)
    Jump("loc_1169")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_1124")
    ClearScenarioFlags(0x24, 0)
    Event(0, 42)
    Jump("loc_1169")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_1138")
    ClearScenarioFlags(0x24, 1)
    Event(0, 44)
    Jump("loc_1169")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_114C")
    ClearScenarioFlags(0x24, 2)
    Event(0, 3)
    Jump("loc_1169")

    label("loc_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_1169")
    ClearScenarioFlags(0x24, 3)
    SetChrPos(0x0, 102230, 0, -105070, 90)

    label("loc_1169")

    Return()

    # Function_1_59C end

    def Function_2_116A(): pass

    label("Function_2_116A")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1187")
    OP_24(0x1F2)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_11A6")

    label("loc_1187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    Sound(498, 1, 50, 0)
    Jump("loc_11A6")

    label("loc_11A0")

    Sound(498, 1, 100, 0)

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11C0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_11D7")

    label("loc_11C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11D7")

    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1203")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)

    label("loc_1203")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1214")
    OP_66(0x3, 0x1)

    label("loc_1214")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF4080FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1236")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x1)
    Jump("loc_123C")

    label("loc_1236")

    OP_10(0x7, 0x0)
    OP_10(0x0, 0x1)

    label("loc_123C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_126A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1261")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_126A")

    label("loc_1261")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_126A")

    ClearMapObjFlags(0x3, 0x10)
    SetMapFlags(0x10000)
    SetScenarioFlags(0x26, 0)
    SetScenarioFlags(0x26, 4)
    SetScenarioFlags(0x26, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_END)), "loc_128A")
    SetScenarioFlags(0x26, 2)

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1296")
    SetScenarioFlags(0x26, 1)

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_12A2")
    SetScenarioFlags(0x26, 3)

    label("loc_12A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_12B1")
    SetScenarioFlags(0x27, 0)
    ClearScenarioFlags(0x26, 6)

    label("loc_12B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_12BD")
    SetScenarioFlags(0x26, 5)

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12C9")
    SetScenarioFlags(0x27, 1)

    label("loc_12C9")

    Return()

    # Function_2_116A end

    def Function_3_12CA(): pass

    label("Function_3_12CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_3_12CA end

    def Function_4_12EA(): pass

    label("Function_4_12EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    SoundLoad(132)
    SoundLoad(497)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1311")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_1311")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetEventSkip(0x0, "loc_13C4")
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, -30000, 990000, 0)

    def lambda_1352():
        OP_96(0x1E, 0xFFF0BDC0, 0xFFFEA070, 0xF4A10, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1352)
    OP_F0(0x1, 0x7D0)
    OP_68(-1005000, -50000, 1005000, 0)
    MoveCamera(145, -35, 0, 0)
    MoveCamera(140, -30, 0, 2500)
    OP_6E(500, 0)
    SetCameraDistance(35000, 0)
    Sleep(2000)
    StopSound(132, 1000, 80)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_13C4")

    EndChrThread(0x1E, 0x1)
    SetChrPos(0x0, 0, 0, -2940, 0)
    OP_31(0x1)
    Sleep(0)
    OP_6F(0xFF)
    OP_69(0xFF, 0x0)
    Sound(498, 1, 100, 0)
    Sleep(1500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x6)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_4_12EA end

    def Function_5_13FF(): pass

    label("Function_5_13FF")

    SoundLoad(132)
    SoundLoad(497)
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_14BB")
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1050000, 120000, 920000, 0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)

    def lambda_144E():
        OP_96(0x1E, 0xFFEFFA70, 0xEA60, 0xE7EF0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_144E)
    OP_F0(0x1, 0x7D0)
    OP_68(-976190, -500, 1037099, 0)
    MoveCamera(35, 39, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(230250, 0)
    Sleep(2000)
    StopSound(132, 1000, 80)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    SetEventSkip(0x1, 0x0)

    label("loc_14BB")

    Return()

    # Function_5_13FF end

    def Function_6_14BC(): pass

    label("Function_6_14BC")

    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_1572")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_14F9():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14F9)
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 0, 800000, 0)
    MoveCamera(30, -7, 0, 0)
    MoveCamera(20, -7, 0, 3000)
    OP_6E(500, 0)
    SetCameraDistance(111000, 0)
    Sleep(300)
    Sound(499, 0, 100, 0)
    Sleep(1700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    StopBGM(0x7D0)
    WaitBGM()
    SetEventSkip(0x1, 0x0)

    label("loc_1572")

    Return()

    # Function_6_14BC end

    def Function_7_1573(): pass

    label("Function_7_1573")

    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B3")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_16A3")

    label("loc_15B3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D6")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_16A3")

    label("loc_15D6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F9")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_16A3")

    label("loc_15F9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161C")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_16A3")

    label("loc_161C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_163F")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_16A3")

    label("loc_163F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1662")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_16A3")

    label("loc_1662")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1685")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_16A3")

    label("loc_1685")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A3")
    SetScenarioFlags(0x3C, 7)

    label("loc_16A3")

    PartySelect(2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_END)),
        (0, "loc_175C"),
        (1, "loc_1775"),
        (3, "loc_178E"),
        (5, "loc_17A7"),
        (7, "loc_17C0"),
        (9, "loc_17D9"),
        (51, "loc_17F2"),
        (17, "loc_180B"),
        (19, "loc_1824"),
        (21, "loc_183D"),
        (23, "loc_1856"),
        (24, "loc_186F"),
        (25, "loc_1888"),
        (26, "loc_18A1"),
        (27, "loc_18BA"),
        (28, "loc_18D3"),
        (29, "loc_18EC"),
        (33, "loc_1905"),
        (35, "loc_191E"),
        (37, "loc_1937"),
        (41, "loc_1950"),
        (43, "loc_1969"),
        (46, "loc_1982"),
        (52, "loc_199B"),
        (47, "loc_19B4"),
        (48, "loc_19D6"),
        (50, "loc_19F8"),
        (49, "loc_1A1A"),
        (42, "loc_1A3C"),
        (SWITCH_DEFAULT, "loc_1A5E"),
    )


    label("loc_175C")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1775")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_178E")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17A7")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17C0")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17D9")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17F2")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1610", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_180B")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1824")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_183D")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2050", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1856")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r3000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_186F")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1888")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18A1")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1310", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18BA")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t2500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18D3")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t2000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18EC")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1905")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m1000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_191E")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2070", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1937")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t6000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1950")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1969")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1982")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4250", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_199B")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19B4")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19D6")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19F8")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1610", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A1A")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A3C")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m9000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A5E")

    Return()

    # Function_7_1573 end

    def Function_8_1A5F(): pass

    label("Function_8_1A5F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17002.eff")
    SoundLoad(493)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    ClearMapObjFlags(0x1, 0x4)
    OP_32(0x4, 0x0, 0x52)
    OP_32(0x4, 0x5, 0x64)
    OP_42(0x4, 0x441, 0xFF)
    OP_42(0x4, 0x5ED, 0xFF)
    OP_42(0x4, 0x651, 0xFF)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x2)
    OP_38(0x4, 0x83, 0x2)
    OP_38(0x4, 0x84, 0x2)
    OP_38(0x4, 0x85, 0x2)
    OP_38(0x4, 0x86, 0x1)
    OP_42(0x4, 0xA1, 0x2)
    OP_42(0x4, 0x94, 0x3)
    OP_42(0x4, 0xB8, 0x4)
    OP_42(0x4, 0x89, 0x5)
    AddCraft(0x4, 0xC1)
    AddCraft(0x4, 0xC3)
    OP_32(0x6, 0x0, 0x55)
    OP_32(0x6, 0x5, 0x64)
    OP_38(0x6, 0x81, 0x2)
    OP_38(0x6, 0x82, 0x2)
    OP_38(0x6, 0x83, 0x2)
    OP_38(0x6, 0x84, 0x2)
    OP_38(0x6, 0x85, 0x2)
    OP_38(0x6, 0x86, 0x2)
    OP_42(0x6, 0x474, 0xFF)
    OP_42(0x6, 0x477, 0xFF)
    OP_42(0x6, 0x478, 0xFF)
    OP_42(0x6, 0x3A, 0x3)
    OP_42(0x6, 0x27, 0x4)
    SetChrChipPat(0x4, 0x1, 0x1F)
    LoadChrChipPat()
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    RemoveCraft(0x6, 0x53)
    RemoveCraft(0x6, 0x61)
    RemoveCraft(0x6, 0x69)
    RemoveCraft(0x6, 0x72)
    RemoveCraft(0x6, 0x79)
    RemoveCraft(0x6, 0x7C)
    RemoveCraft(0x6, 0x85)
    RemoveCraft(0x6, 0x87)
    RemoveCraft(0x6, 0x34)
    RemoveCraft(0x6, 0x3E)
    RemoveCraft(0x6, 0x48)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrChipByIndex(0x15, 0xF)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    SetChrPos(0x15, -3100, -1350, 7100, 315)
    OP_68(-280, 1800, -1040, 0)
    MoveCamera(44, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(1170, 1800, 3900, 3000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-1360, 3800, 2000, 0)
    OP_68(-1360, 1800, 2720, 4000)
    MoveCamera(44, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17820, 0)
    Sleep(1000)
    Sound(943, 2, 70, 0)
    OP_71(0x1, 0x1, 0x1E, 0x0, 0x8)
    OP_79(0x1)
    Sound(143, 0, 50, 0)
    OP_24(0x3AF)
    Sleep(500)
    SetChrSubChip(0x105, 0x2)
    OP_70(0x1, 0x1F)
    Sound(72, 0, 100, 0)
    Sleep(300)
    SetMessageWindowPos(85, -1, -1, -1)
    SetChrName("ケビン神父")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──手筈の通り、\x01",
            "“人形”はオレらが引き受ける。\x02\x03",

            "くれぐれも気ぃ付けてな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0002
    ChrTalk(
        0x105,
        (
            "#10404F#6Pフフ、そちらこそ。\x01",
            "《外法#4R げ ほう#狩り》──いや《千の護#2Rまもり#手#2Rて#》。\x02\x03",

            "#10402F渾名#4Rあだ な #を変えたばかりなのに\x01",
            "お役御免にならないようにね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(140, -1, -1, -1)
    SetChrName("ケビン神父")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハハ、確かにな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0004
    ChrTalk(
        0x8,
        (
            "#12102F#6Pしかし《千の腕#6Rル フ ィ ナ#》殿から\x01",
            "頂戴した渾名とは……\x02\x03",

            "良き名を名乗られたな、グラハム卿。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(145, -1, -1, -1)
    SetChrName("ケビン神父")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……おおきに。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("シスター・リース")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0007
    ChrTalk(
        0x101,
        "#00008F#12P（色々あるみたいだな……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(85, -1, -1, -1)
    SetChrName("ケビン神父")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ロイド君。\x01",
            "大変かと思うけど気張りや。\x02\x03",

            "クロスベルの今の状況では\x01",
            "外部からの助けはアテに出来ん。\x02\x03",

            "鍵を握るとしたら、今まで君が\x01",
            "クロスベルで培#2Rつちか#ってきた絆やろ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0009
    ChrTalk(
        0x101,
        (
            "#00005F#12P培ってきた絆……\x02\x03",

            "#00004F──分かりました。\x01",
            "肝に銘じておきます。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_70(0x1, 0x20)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("シスター・リース")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドさん、女神#4Rエイドス#の加護を。\x02\x03",

            "それとエリィさんのこと、\x01",
            "どうかよろしくお願いします。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0011
    ChrTalk(
        0x101,
        "#00000F#12Pええ、勿論です！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_70(0x1, 0x1E)
    Sound(73, 0, 100, 0)
    Sleep(300)
    SetCameraDistance(19650, 3000)
    StopBGM(0xBB8)
    Sleep(1000)
    Sound(943, 2, 60, 0)
    OP_71(0x1, 0x2F, 0x4C, 0x0, 0x8)
    Sleep(500)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7542", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_79(0x1)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(1002, 0, 40, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 2000, 0, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    #C0012
    ChrTalk(
        0x101,
        "#00011F#12Pなんだ……？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#12100F#11P光学迷彩機能を起動した。\x02\x03",

            "もちろん完璧ではないし、\x01",
            "使用すると速度が落ちるなどの\x01",
            "デメリットもあるがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x105,
        (
            "#10403F#11Pこのまま潜入したら\x01",
            "すぐに高機動タイプの人形が\x01",
            "迎撃に現れるだろう。\x02\x03",

            "#10401Fまともにやり合っても\x01",
            "まず勝ち目はないだろうから\x01",
            "伍号機に引き付けてもらう。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00001F#12Pなるほど……\x01",
            "その隙に潜入するわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x107,
        (
            "#01200F#3C#12Pふむ、星杯の守り手の手並み、\x01",
            "見せてもらうとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20650, 2000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x4)
    OP_6F(0x79)
    OP_24(0x3AF)
    SetScenarioFlags(0x22, 2)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1A5F end

    def Function_9_2387(): pass

    label("Function_9_2387")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SoundLoad(497)
    SoundLoad(498)
    SoundLoad(132)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis335.itp")
    CreatePortrait(1, 198, 150, 214, 166, 0, 0, 512, 256, 488, 0, 504, 16, 0xFFFFFF, 0x0, "c_vis335.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 100230, 50, -102650, 270)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, 98470, 50, -101100, 180)
    SetChrChipByIndex(0x107, 0x10)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x107, 100400, 0, -101700, 270)
    BeginChrThread(0x107, 3, 0, 0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 750, 0, -2500, 270)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    OP_4B(0x15, 0xFF)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    OP_4B(0x16, 0xFF)
    SetChrPos(0x15, -750, 0, -2000, 90)
    SetChrPos(0x16, -750, 0, -3000, 90)
    SetMapObjFlags(0x0, 0x1000)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 1500, 1000000, 0)
    MoveCamera(120, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    MoveCamera(135, 10, 0, 6000)
    SetCameraDistance(40000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0xFFFF)
    Sleep(500)
    Sound(498, 2, 100, 0)
    OP_68(1500, 1000, 500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_68(1500, 1000, -2500, 6000)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_63(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_68(100110, 3000, -101660, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17730, 0)
    OP_68(100110, 1000, -101660, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0017
    ChrTalk(
        0x105,
        (
            "#10406F#5P──何とか潜入できたけど\x01",
            "クロスベルそのものが《至宝》と\x01",
            "一体化しているような状況だ。\x02\x03",

            "#10401Fここから先は注意して動かないと\x01",
            "また人形が飛んでくるだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00008F#11Pこの飛行艇に頼るのも\x01",
            "限界があるということか。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x107,
        (
            "#01200F#11P#3Cたしかに、この船の大きさだと\x01",
            "地上に降りればプレロマ草を介した\x01",
            "“網”に捉えられるであろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x105,
        (
            "#10406F#5Pそう、このままだと着陸すら\x01",
            "出来なくなってしまう……\x02\x03",

            "#10400Fそこで七耀脈の力場の“隙間”を\x01",
            "探知・発見して行こうと思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#00005F#11P力場の“隙間”……？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3Cふむ、七耀脈の力場は本来、\x01",
            "大地そのものを覆う巨大なものだ。\x02\x03",

            "#01200Fだが大きな流れ同士の間に\x01",
            "たまに“隙間”が生じる事がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00003F#11Pなるほど……\x02\x03",

            "#00000Fそういった“隙間”なら\x01",
            "着陸しても気づかれないわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        (
            "#10404F#5Pフフ、そういう事。\x02\x03",

            "#10402Fで、今いる地点が、\x01",
            "ちょうどその場所ってわけさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(1300)
    SetMessageWindowPos(30, 10, -1, -1)

    #A0025
    AnonymousTalk(
        0x101,
        (
            "#00001Fウルスラ間道の中州……\x01",
            "前に幻獣が出現した場所の近くか。\x02\x03",

            "#00005Fでも、よく見つけられたな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    #A0026
    AnonymousTalk(
        0x105,
        (
            "#10404Fフフ、異変が起きる前に\x01",
            "アッバスと調べておいたのさ。\x02\x03",

            "#10402Fで、少し小細工をしてから\x01",
            "クロスベルを脱出したってわけ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 10, -1, -1)

    #A0027
    AnonymousTalk(
        0x101,
        "#00011Fな、なるほど。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 20, -1, -1)

    #A0028
    AnonymousTalk(
        0x107,
        "#01203F#3Cふむ、用意周到なことだ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    #A0029
    AnonymousTalk(
        0x105,
        (
            "#10404F#0Cま、今はここだけだから\x01",
            "今後も着陸できそうな“隙間”を\x01",
            "探して行く必要があるけどね。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0030
    ChrTalk(
        0x105,
        (
            "#10403F#5P──それで、どうする？\x02\x03",

            "#10400Fどうせ《結界》があるから\x01",
            "クロスベル市には入れないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00006F#11P……そうだな。\x01",
            "それでも一度降ろしてもらおう。\x02\x03",

            "#00008F少しでもクロスベルの状況を\x01",
            "知っておきたいし……\x02\x03",

            "#00001Fウルスラ病院がどうなっているか\x01",
            "確かめておきたい気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x105,
        "#10404F#5Pフフ、了解。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x107,
        "#01203F#11P#3Cならば降りるとしようか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(200)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x105)
    Sleep(500)

    #C0034
    ChrTalk(
        0x107,
        "#01200F#5P#3Cむ、どうした？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00006F#11Pいや、今更ではあるけど……\x02\x03",

            "#00001Fツァイトってどうして\x01",
            "俺たちを助けてくれるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10403F#5Pそれにリベールの竜の話だと……\x02\x03",

            "#10401F君たち聖獣って、《至宝》を巡る\x01",
            "因縁については“見守る”だけで\x01",
            "介入できないんじゃなかったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x107,
        (
            "#01203F#11P#3C然#2Rしか#り──古の“盟約”がある。\x02\x03",

            "#01200Fだが、《幻の至宝》が失われた現在、\x01",
            "私の本来の使命も既に終わっている。\x02\x03",

            "この身を縛る“禁忌#4Rきん き #”も薄れた故、\x01",
            "ある程度自由に動けるというわけだ。\x02\x03",

            "人の子らに少しばかり\x01",
            "力を貸してやるくらいはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        "#10400F#5Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00008F#11Pそれでマフィアの軍用犬事件でも\x01",
            "俺たちを助けてくれたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3Cうむ、そういう事だ。\x02\x03",

            "#01200F無制限の助力は出来ぬが……\x01",
            "しばらくの間だけは\x01",
            "このまま力になってやろう。\x02\x03",

            "一応“警察犬”とやらに\x01",
            "登録されている身でもあるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00012F#11Pハハ、分かった。\x01",
            "ありがたく力を貸してもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x105, 0x0)
    Sleep(150)

    #C0042
    ChrTalk(
        0x105,
        (
            "#10404F#5Pしばらくはこのメンツで\x01",
            "動くことにはなりそうだね。\x02\x03",

            "#10400F──地上に降りたい時は\x01",
            "アッバスに声をかけてくれ。\x02\x03",

            "あと、この《メルカバ》内部にも\x01",
            "幾つかの設備が整っている。\x02\x03",

            "#10404F装備・道具・工房機能──\x01",
            "必要ならクルーに声を掛けるといい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(100)

    #C0043
    ChrTalk(
        0x101,
        "#00000F#11Pああ、了解だ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17980, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジとツァイトがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x4, 0x12D)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジがＳクラフト\x01\x07\x02",

            "『アカシックアーム』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『アカシックアーム』\x07\x05",
            "をＳブレイクに登録しますか？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【は  い】\x01",      # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332D")
    SetChrChipPat(0x4, 0x6, 0x12D)

    label("loc_332D")

    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sleep(1000)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "しばらくの間、ツァイトが\x01",
            "パーティメンバーとして参加します。\x02\x03",

            "エニグマⅡを持っていないため\x01",
            "クオーツのカスタマイズは出来ませんが\x01",
            "強力な上位アーツを使用する事ができます。\x02\x03",

            "ただしＳクラフトは持っていないため、\x01",
            "注意する必要があります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお──メルカバ内では\x01",
            "ロイド１人が行動することとなり、\x01",
            "他のメンバーは艦内に待機しています。\x02\x03",

            "ただしキャンプメニューでは\x01",
            "全メンバーの項目を操作することが可能で、\x01",
            "ショップ・工房でも参照する事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    ClearChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 103570, 0, -97090, 270)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 103950, 0, -210, 270)
    OP_4C(0x16, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 100150, 0, -100950, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x20, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x26, 4)
    SetScenarioFlags(0x26, 6)
    SetScenarioFlags(0x1A0, 0)
    OP_29(0xAF, 0x4, 0x2)
    OP_29(0xAF, 0x1, 0x0)
    Sound(498, 2, 100, 0)
    ClearScenarioFlags(0x32, 0)
    ClearScenarioFlags(0x32, 1)
    ClearScenarioFlags(0x32, 2)
    ClearScenarioFlags(0x32, 3)
    ClearScenarioFlags(0x32, 4)
    ClearScenarioFlags(0x32, 5)
    ClearScenarioFlags(0x32, 6)
    ClearScenarioFlags(0x32, 7)
    ClearScenarioFlags(0x33, 0)
    ClearScenarioFlags(0x33, 1)
    ClearScenarioFlags(0x33, 2)
    ClearScenarioFlags(0x33, 3)
    ClearScenarioFlags(0x33, 4)
    ClearScenarioFlags(0x33, 5)
    ClearScenarioFlags(0x33, 6)
    ClearScenarioFlags(0x33, 7)
    ClearScenarioFlags(0x34, 0)
    ClearScenarioFlags(0x34, 1)
    ClearScenarioFlags(0x34, 2)
    ClearScenarioFlags(0x34, 3)
    ClearScenarioFlags(0x34, 4)
    ClearScenarioFlags(0x34, 5)
    ClearScenarioFlags(0x34, 6)
    ClearScenarioFlags(0x34, 7)
    ClearScenarioFlags(0x31, 6)
    ClearScenarioFlags(0x31, 4)
    ClearScenarioFlags(0x2F, 6)
    ClearScenarioFlags(0x31, 3)
    ClearScenarioFlags(0x2D, 6)
    ClearScenarioFlags(0x2D, 4)
    ClearScenarioFlags(0x2D, 2)
    ClearScenarioFlags(0x2B, 6)
    ClearScenarioFlags(0x35, 0)
    ClearScenarioFlags(0x35, 1)
    ClearScenarioFlags(0x35, 2)
    ClearScenarioFlags(0x35, 3)
    ClearScenarioFlags(0x35, 4)
    ClearScenarioFlags(0x35, 5)
    ClearScenarioFlags(0x35, 6)
    ClearScenarioFlags(0x35, 7)
    ClearScenarioFlags(0x36, 0)
    ClearScenarioFlags(0x36, 1)
    ClearScenarioFlags(0x36, 2)
    ClearScenarioFlags(0x36, 3)
    ClearScenarioFlags(0x36, 4)
    ClearScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x36, 6)
    ClearScenarioFlags(0x36, 7)
    ClearScenarioFlags(0x37, 0)
    ClearScenarioFlags(0x37, 1)
    ClearScenarioFlags(0x37, 2)
    ClearScenarioFlags(0x37, 3)
    ClearScenarioFlags(0x37, 4)
    ClearScenarioFlags(0x37, 5)
    ClearScenarioFlags(0x37, 6)
    ClearScenarioFlags(0x37, 7)
    ClearScenarioFlags(0x31, 7)
    ClearScenarioFlags(0x31, 5)
    ClearScenarioFlags(0x2F, 7)
    ClearScenarioFlags(0x2F, 5)
    ClearScenarioFlags(0x2D, 7)
    ClearScenarioFlags(0x2D, 5)
    ClearScenarioFlags(0x2D, 3)
    ClearScenarioFlags(0x2B, 7)
    EventEnd(0x5)
    Return()

    # Function_9_2387 end

    def Function_10_36B5(): pass

    label("Function_10_36B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F6")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_10_36B5")

    label("loc_36F6")

    Return()

    # Function_10_36B5 end

    def Function_11_36F7(): pass

    label("Function_11_36F7")

    EventBegin(0x0)
    Fade(500)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-220, -500, 6740, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x101, -1500, -1500, 6000, 45)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A96")

    #C0049
    ChrTalk(
        0x8,
        "#12100F#11P──で、結局どうする？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00003F#6Pああ、一度この場所に\x01",
            "降りてみることになったよ。\x02\x03",

            "#00000Fそれはそうと、まさか君たちに\x01",
            "こんな背景があったとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#12102F#11P全ては教会内部の対立──\x01",
            "騎士団に批判的なエラルダ大司教の\x01",
            "目を誤魔化すためでな。\x02\x03",

            "まさか最高位の騎士の一人が\x01",
            "不良グループの頭#2Rヘッド#を張ってるとは\x01",
            "誰も思うまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00006F#6Pそりゃまあ、確かになぁ。\x02\x03",

            "#00005Fあ、でも、聖典#4Rテスタメンツ#とか聖戦とか、\x01",
            "やたらと宗教がかった言葉を\x01",
            "使ってたような気もするんだけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#12105F#11Pふむ、そうか？\x02\x03",

            "#12100Fかえって不謹慎な印象となって\x01",
            "誤魔化せるかと思ったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00012F#6Pま、まあ確かに\x01",
            "独特な雰囲気のチームだったから\x01",
            "誤魔化せていたとは思うよ。\x02\x03",

            "#00000F──それで、\x01",
            "すぐにでも降下できるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#12102F#11Pうむ、“隙間”の位置は\x01",
            "正確に把握できている。\x02\x03",

            "準備が出来たら言うがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 1)
    Jump("loc_3B05")

    label("loc_3A96")


    #C0056
    ChrTalk(
        0x8,
        (
            "#12100F#11P“隙間”の位置は\x01",
            "正確に把握できている。\x02\x03",

            "ウルスラ間道の中洲に降りる\x01",
            "準備が出来たら言うがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B05")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "メルカバで降下する\x01",      # 0
            "やめる\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B59"),
        (1, "loc_3BF7"),
        (SWITCH_DEFAULT, "loc_3C4F"),
    )


    label("loc_3B59")


    #C0057
    ChrTalk(
        0x8,
        (
            "#12102F#11P了解した。\x01",
            "一応、場所を確認するがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_3BD7")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0x0)
    Call(0, 12)
    Call(0, 5)
    Call(0, 7)
    Jump("loc_3BF2")

    label("loc_3BD7")

    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_3BF2")

    Jump("loc_3C4F")

    label("loc_3BF7")


    #C0058
    ChrTalk(
        0x8,
        (
            "#12100F#11Pならば準備が出来たら\x01",
            "声をかけるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_3C4F")

    label("loc_3C4F")

    Return()

    # Function_11_36F7 end

    def Function_12_3C50(): pass

    label("Function_12_3C50")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    OP_68(0, 500, 3500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(0, 5000, 3500, 3000)
    Sleep(2000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 1)
    Return()

    # Function_12_3C50 end

    def Function_13_3D0D(): pass

    label("Function_13_3D0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(938)
    SoundLoad(132)
    SoundLoad(497)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    Sound(938, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0059
    ChrTalk(
        0x103,
        (
            "#00203F#12P#N……七耀脈の力場の\x01",
            "《隙間》を新たに感知……\x02\x03",

            "#00202Fそちらにデータを送ります。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0060
    ChrTalk(
        0xC,
        (
            "#01909F#5Pはい、了解です。\x02\x03",

            "#01901F（カタカタ……）\x01",
            "座標特定できましたー！\x02\x03",

            "クロスベル北東エリア、\x01",
            "《アルモリカ村》近辺です！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    #C0061
    ChrTalk(
        0x101,
        "#00002F#12P凄いな……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#12102F#11Pフム、随分と助かる。\x02\x03",

            "プラトーの感応力は勿論だが、\x01",
            "専門のオペレーターがいると\x01",
            "艦の運用効率が格段に上がるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        (
            "#01909F#5Pえへへ……\x01",
            "まだまだ未熟ですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        (
            "#10404F#11Pフフ、これからは効率的に\x01",
            "降りられる場所を探せそうだね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(200)

    #C0065
    ChrTalk(
        0x105,
        (
            "#10400F#5Pそれで、どうする？\x02\x03",

            "このまま新しい地点#4Rポイント#に\x01",
            "行ってみるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00000F#12Pああ、アルモリカ村の様子も\x01",
            "確かめられそうだしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#12100F#11P機関最大、目的地、\x01",
            "《アルモリカ村》上空。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#00200F#12P#N警戒態勢を維持しつつ、\x01",
            "目的地へと向かいます。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19110, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_24(0x3AA)
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_F3(100000)
    ClearChrFlags(0x1E, 0x80)
    OP_78(0x0, 0x1E)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)
    PlayEffect(0x0, 0x0, 0x1E, 0x5, -4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1E, 0x5, 4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-1000000, 0, 800000, 0)
    MoveCamera(330, -7, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(111000, 0)
    MoveCamera(340, -7, 0, 3000)

    def lambda_425A():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_425A)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sound(499, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopSound(497, 3000, 100)
    Sleep(2000)
    StopSound(132, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0xFFFF)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    Sleep(500)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetScenarioFlags(0x26, 2)
    SetScenarioFlags(0x1A1, 2)
    OP_29(0xAF, 0x1, 0x3)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_435D")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4352")
    Call(0, 6)
    Jump("loc_4355")

    label("loc_4352")

    Call(0, 5)

    label("loc_4355")

    Call(0, 7)
    Jump("loc_4366")

    label("loc_435D")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_4366")

    Return()

    # Function_13_3D0D end

    def Function_14_4367(): pass

    label("Function_14_4367")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4381")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_14_4367")

    label("loc_4381")

    Return()

    # Function_14_4367 end

    def Function_15_4382(): pass

    label("Function_15_4382")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    SoundLoad(938)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -950, 0)
    SetChrPos(0x106, -1400, 0, -1150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    Sound(938, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0069
    ChrTalk(
        0x103,
        (
            "#00204F#12P#N新たな《隙間》を感知。\x02\x03",

            "#00202Fフランさん。\x01",
            "データを送ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xC,
        (
            "#01909F#5Pはーい。\x01",
            "（カタカタカタ……）\x02\x03",

            "#01905F──出ました！\x01",
            "クロスベル北西エリア……\x02\x03",

            "#01901Fマインツ山道中間地点です！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00002F#12Pマインツ方面か……\x01",
            "行動できるエリアが広がるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x105,
        (
            "#10403F#11Pまあ、向こうもこちらの動きに\x01",
            "そろそろ気付いていそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x106,
        (
            "#10708F#12P#N……マインツ方面といえば、\x01",
            "《黒月》とは異なる勢力が\x01",
            "抵抗活動#8Rレジスタンス#をしていた筈です。\x02\x03",

            "#10701F何でもリーダーは\x01",
            "国防軍の現状に異議を唱えた\x01",
            "元警備隊メンバーだそうですが。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-1230, 1100, 3390, 1000)
    SetCameraDistance(19800, 1000)

    def lambda_4797():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4797)
    SetChrFlags(0x107, 0x20)

    def lambda_47A9():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_47A9)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    OP_6F(0x79)
    ClearChrFlags(0x107, 0x20)

    #C0074
    ChrTalk(
        0x101,
        "#00011F#5Pそ、そうなのか！？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#00201F#5Pてっきり全ての隊員が国防軍に\x01",
            "なったと思っていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#12100F#5Pまあ、無理もあるまい。\x02\x03",

            "警備隊に甚大な被害を与えた\x01",
            "《赤い星座》が大手を振って\x01",
            "動き回っているくらいだ。\x02\x03",

            "その欺瞞#4R ぎ まん#に耐えられない者が\x01",
            "出てきても不思議ではなかろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "#01901F#5Pそ、それじゃあ\x01",
            "ひょっとしてお姉ちゃんも……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0078
    ChrTalk(
        0x101,
        (
            "#00006F#11P……いや。\x01",
            "残念だけどそれは無いと思う。\x02\x03",

            "#00008Fノエルは全てを呑み込んだ上で\x01",
            "今のクロスベルを守るという\x01",
            "道を選択した。\x02\x03",

            "#00013Fその決意を\x01",
            "簡単には曲げないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        (
            "#01912F#5P#30W……あはは、そうですよね。\x02\x03",

            "#01908F#30Wお姉ちゃんって本当に\x01",
            "強くって……不器用ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        "#00208F#5P……フランさん。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10403F#5Pま、いずれにせよ、\x01",
            "その抵抗勢力#8Rレジスタンス#ってのには\x01",
            "コンタクトしておきたいね。\x02\x03",

            "#10400F場合によっては《黒月》共々、\x01",
            "力になってくれるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00001F#11Pああ、とにかく降りてみよう。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 500)

    #C0083
    ChrTalk(
        0x101,
        (
            "#00005F#5P……そういえば、リーシャ。\x02\x03",

            "#00000Fその前にウルスラ病院に\x01",
            "寄っておくか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0084
    ChrTalk(
        0x106,
        "#10712F#12Pえ……！？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#00003F#5Pイリアさんは君に\x01",
            "とても会いたがってたよ。\x02\x03",

            "#00002F色々あるとは思うけど……\x01",
            "元気な顔を見せてあげたらどうだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)

    #C0086
    ChrTalk(
        0x106,
        (
            "#10706F#12P……いえ、止めておきます。\x02\x03",

            "#10708F私はまだ、イリアさんの前に\x01",
            "胸を張って立てませんから……\x02\x03",

            "#10710Fせめてクロスベル市を解放して\x01",
            "アルカンシェルを取り戻すまでは\x01",
            "我慢させてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#00006F#5P……そうか。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#00206F#5Pもどかしいですけど……\x01",
            "気持ちは分かる気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x106,
        (
            "#10709F#12Pあはは……ごめんなさい。\x02\x03",

            "#10702Fあ、もちろんご用があれば\x01",
            "ウルスラ病院に行くのは\x01",
            "構いませんから……！\x02\x03",

            "#10704Fわたしはその、病院前で\x01",
            "待たせてもらいますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ、分かった。\x02\x03",

            "#00000F（それにしてもリーシャ……\x01",
            "  やっぱりこちらが素なんだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20050, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リーシャがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4F")
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)
    Jump("loc_4F57")

    label("loc_4F4F")

    AddCraft(0x5, 0x195)
    AddCraft(0x0, 0x195)

    label("loc_4F57")

    SetMessageWindowPos(-1, -1, -1, -1)

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとリーシャがコンビクラフト\x01\x07\x02",

            "『比翼双竜撃』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1520, 0, -100980, 180)
    SetChrChipByIndex(0xA, 0x2)
    BeginChrThread(0xA, 0, 0, 0)
    SetScenarioFlags(0x26, 5)
    SetScenarioFlags(0x1A1, 7)
    OP_29(0xAF, 0x1, 0x7)
    Sleep(300)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    OP_24(0x3AA)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_50C8")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50BD")
    Call(0, 6)
    Jump("loc_50C0")

    label("loc_50BD")

    Call(0, 5)

    label("loc_50C0")

    Call(0, 7)
    Jump("loc_50D1")

    label("loc_50C8")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_50D1")

    Return()

    # Function_15_4382 end

    def Function_16_50D2(): pass

    label("Function_16_50D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    SoundLoad(938)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    MoveCamera(39, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19800, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 1300, 0, -1500, 0)
    SetChrPos(0x106, -1400, 0, -1150, 0)
    SetChrPos(0x104, 200, 0, -750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xF, -750, 500, 3300, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    FadeToBright(1000, 0)
    Sleep(3000)
    OP_63(0xF, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0xF,
        (
            "#02109F#11Pうっわ～……\x01",
            "ホント、すごい飛行艇ねぇ！\x02\x03",

            "#02110Fまさか七耀教会が\x01",
            "こんな船を持ってたなんて！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    #C0095
    ChrTalk(
        0x8,
        (
            "#12100F#5P……繰り返すが\x01",
            "くれぐれも他言無用に願うぞ。\x02\x03",

            "記事にでもしたら\x01",
            "今後、教会の一切の庇護を\x01",
            "受けられぬと覚悟してもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10409F#11Pハハ、まあ記事にしたところで\x01",
            "ヨタ話のたぐいにしか\x01",
            "思われないかもしれないけど。\x02\x03",

            "#10402F《結社》あたりと同じように。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        "#12107F#5Pワジ……！\x02",
    )

    CloseMessageWindow()
    OP_68(-230, 1100, 2950, 1000)
    SetCameraDistance(19800, 1000)
    OP_93(0xF, 0xB4, 0x1F4)
    Sleep(300)
    OP_6F(0x79)

    #C0098
    ChrTalk(
        0xF,
        (
            "#02104F#5P心配せずとも約束は守りますって。\x02\x03",

            "#02100Fあのリーシャ・マオの正体が\x01",
            "謎の魔人《銀#2Rイン#》っていうのもね！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x106,
        "#10706F#12P#N……お願いします。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0100
    ChrTalk(
        0x104,
        (
            "#00306F#12P（なあロイド……）\x02\x03",

            "#00301F（本当に連れて来ちまっても\x01",
            "  よかったのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00012F#11P（ま、まあ一応、\x01",
            "  約束は守る人だと思うし。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-790, 1100, 4000, 1000)
    OP_6F(0x79)
    Sound(938, 2, 100, 0)

    #C0102
    ChrTalk(
        0x103,
        (
            "#00201F#11Pクロスベル西部に\x01",
            "新たな《隙間》を感知しました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x13B, 0x1F4)

    #C0103
    ChrTalk(
        0xC,
        (
            "#01908F#5P（カタカタ……）\x01",
            "正確な座標を特定。\x02\x03",

            "#01903F西クロスベル街道、中間……\x02\x03",

            "#01901F警察学校や拘置所方面への\x01",
            "分岐地点の付近です。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    #C0104
    ChrTalk(
        0x101,
        "#00001F#11Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#00301F#12Pたしか拘置所を脱出する時、\x01",
            "ガルシアのオッサンに\x01",
            "助けてもらったんだったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00006F#11Pああ……何だかんだ言って\x01",
            "力になってくれたよ。\x02\x03",

            "#00008Fあれからどうなったのか\x01",
            "気になっているんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    #C0107
    ChrTalk(
        0x105,
        (
            "#10406F#5Pでも、警察学校方面に\x01",
            "行ってみるのは得策じゃないね。\x02\x03",

            "#10401F君が脱出したことで\x01",
            "警備も強化されているだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x106,
        (
            "#10708F#12P#Nかと言って他に行けるとしたら\x01",
            "国防軍がいるベルガード門だけ……\x02\x03",

            "#10701Fちょっと困りましたね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0109
    ChrTalk(
        0xF,
        (
            "#02106F#11Pまあ、ノコノコ訪ねたら\x01",
            "捕まるのは確実でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        "#01908F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00003F#11P……とにかく\x01",
            "降りるだけ降りてみよう。\x02\x03",

            "#00001Fどの程度、国防軍が\x01",
            "警戒しているか確かめたいし、\x01",
            "幻獣の徘徊具合も気になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#00202F#11P了解です。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#12100F#5P鉱山町の前にも\x01",
            "“法陣”が設置された。\x02\x03",

            "いつでも降りられるので\x01",
            "必要なら声をかけるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20050, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x3, 0x129)
    AddCraft(0x3, 0x168)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディがＳクラフト\x01\x07\x02",

            "『ベルゼルガー』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ベルゼルガー』\x07\x05",
            "をＳブレイクに登録しますか？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【は  い】\x01",      # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B5D")
    SetChrChipPat(0x3, 0x6, 0x129)

    label("loc_5B5D")

    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x0, -150, 0, -88230, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x26, 3)
    SetScenarioFlags(0x1A2, 7)
    OP_29(0xAF, 0x1, 0xD)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_16_50D2 end

    def Function_17_5BB6(): pass

    label("Function_17_5BB6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06900.itc", 0x1E)
    LoadChrToIndex("apl/ch51027.itc", 0x1F)
    LoadChrToIndex("apl/ch51712.itc", 0x20)
    SoundLoad(498)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x101, 500, 0, -104000, 0)
    SetChrPos(0x1B, -500, 0, -104000, 0)
    SetChrPos(0x106, 500, 0, -104000, 0)
    SetChrPos(0x103, -500, 0, -104000, 0)
    SetChrPos(0x104, 500, 0, -104000, 0)
    SetChrPos(0x105, -500, 0, -104000, 0)
    SetChrPos(0x107, 0, 0, -104000, 0)
    SetChrPos(0x1C, 0, 0, -85000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    SetChrName("")

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ノエルは荷物をまとめ\x01",
            "ロイドたちと共にメルカバに乗艦した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7514", 0)
    Sound(498, 2, 100, 0)
    OP_68(0, 1250, -102500, 0)
    OP_68(0, 1250, -93000, 6000)
    MoveCamera(45, 25, 0, 0)
    MoveCamera(45, 20, 0, 6000)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)

    def lambda_5D9F():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D9F)

    def lambda_5DB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DB4)
    Sleep(100)

    def lambda_5DC8():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5DC8)

    def lambda_5DDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_5DDD)
    Sleep(500)

    def lambda_5DF1():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5DF1)

    def lambda_5E06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5E06)
    Sleep(100)

    def lambda_5E1A():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E1A)

    def lambda_5E2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5E2F)
    Sleep(500)

    def lambda_5E43():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E43)

    def lambda_5E58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E58)
    Sleep(100)

    def lambda_5E6C():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E6C)

    def lambda_5E81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5E81)
    Sleep(800)

    def lambda_5E95():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5E95)

    def lambda_5EAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5EAA)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_5ED3():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5ED3)

    def lambda_5EE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5EE8)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1C, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1B, 2)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x107, 2)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5F59():

        label("loc_5F59")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F59")

    QueueWorkItem2(0x101, 2, lambda_5F59)

    def lambda_5F6B():

        label("loc_5F6B")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F6B")

    QueueWorkItem2(0x103, 2, lambda_5F6B)

    def lambda_5F7D():

        label("loc_5F7D")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F7D")

    QueueWorkItem2(0x104, 2, lambda_5F7D)

    def lambda_5F8F():

        label("loc_5F8F")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F8F")

    QueueWorkItem2(0x105, 2, lambda_5F8F)

    def lambda_5FA1():

        label("loc_5FA1")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5FA1")

    QueueWorkItem2(0x106, 2, lambda_5FA1)
    OP_68(0, 1250, -95000, 2500)
    SetCameraDistance(16500, 17000)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x1C, 3, 0, 19)
    Sleep(3000)
    SetChrName("")

    #A0118
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そして、出迎えたフランは\x01",
            "問答無用でノエルに抱きついてから\x01",
            "泣きじゃくってしまい……\x02\x03",

            "ノエルもまた、妹をなだめながら\x01",
            "目を潤ませて涙を浮かべるのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    SetCameraDistance(16500, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_5BB6 end

    def Function_18_60B6(): pass

    label("Function_18_60B6")


    def lambda_60BB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60BB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_60B6 end

    def Function_19_60DB(): pass

    label("Function_19_60DB")

    OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFE8E78, 0x1770, 0x0)
    Fade(250)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    Sound(812, 0, 100, 0)
    Sound(811, 0, 30, 0)
    OP_A6(0x1B, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_0D()
    OP_63(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1B)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)
    Sleep(500)

    def lambda_6162():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6162)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_6182():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6182)
    WaitChrThread(0x1C, 2)
    Sleep(1500)

    def lambda_61A2():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_61A2)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_61C2():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_61C2)
    WaitChrThread(0x1C, 2)
    Return()

    # Function_19_60DB end

    def Function_20_61DB(): pass

    label("Function_20_61DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x8, 0xFF, 0xFF)
    OP_32(0x8, 0x0, 0x56)
    OP_32(0x8, 0x5, 0x64)
    OP_42(0x8, 0x455, 0xFF)
    OP_42(0x8, 0x5ED, 0xFF)
    OP_42(0x8, 0x651, 0xFF)
    OP_38(0x8, 0x81, 0x2)
    OP_38(0x8, 0x84, 0x2)
    OP_38(0x8, 0x85, 0x2)
    OP_38(0x8, 0x86, 0x2)
    OP_42(0x8, 0xB4, 0x1)
    OP_42(0x8, 0x72, 0x4)
    OP_42(0x8, 0xB9, 0x5)
    OP_42(0x8, 0xA0, 0x6)
    AddCraft(0x8, 0xEC)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis284.itp")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-850, 2900, 3210, 0)
    MoveCamera(39, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20690, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 1500, 0, -1500, 0)
    SetChrPos(0x106, -1500, 0, -1250, 0)
    SetChrPos(0x104, 500, 0, -750, 0)
    SetChrPos(0x109, -500, 0, -1750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrPos(0xF, -3480, -1500, 4650, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-850, 1100, 3210, 3500)
    MoveCamera(39, 19, 0, 3500)
    OP_6E(500, 3500)
    SetCameraDistance(20690, 3500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(836, 0, 100, 0)

    #C0119
    ChrTalk(
        0x103,
        (
            "#00204F#11P──ミシュラム方面の\x01",
            "“隙間”を感知しました。\x02\x03",

            "#00202Fフランさん、座標を送ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        "#01908F#5Pうん、グス……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x109,
        (
            "#10106F#12Pもう……\x01",
            "いつまで泣いてるの？\x02\x03",

            "#10101Fみんなに笑われちゃうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#00012F#11Pはは、いいさ。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x106,
        (
            "#10709F#12P#Nふふっ……\x01",
            "何だか羨ましいです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(836, 0, 100, 0)

    #C0124
    ChrTalk(
        0xC,
        (
            "#01909F#5Pえへへ……すみません。\x02\x03",

            "#01900F（カタカタ……）\x01",
            "──特定できました！\x02\x03",

            "#01903Fミシュラム保養地、\x01",
            "ホテル・デルフィニア付近……\x02\x03",

            "#01901Fあの湖水浴場#8Rレイク・ビーチ#のあたりです！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        "#00305F#12Pヒューッ、スゲェ偶然だな。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x105,
        (
            "#10404F#11Pフフ、今度は優雅な\x01",
            "バカンスとは言いがたいけどね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    #C0127
    ChrTalk(
        0xF,
        (
            "#02105F#5Pあら、ひょっとして……\x02\x03",

            "みんなでビーチで\x01",
            "遊びに行った事があるとか？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_66B2():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_66B2)
    Sleep(50)

    def lambda_66C2():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_66C2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(100)

    #C0128
    ChrTalk(
        0x101,
        "#00002F#11Pええ、まあ……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        "#00204F#5P通商会議の後ですけど。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xF,
        (
            "#02106F#5Pもー、つれないわねぇ。\x02\x03",

            "#02101Fそんな楽しそうなイベントに\x01",
            "何であたしを呼んでくれないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#00306F#11Pいや、俺たちだって\x01",
            "招待された身分だったしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x105,
        (
            "#10408F#5P今にして思えば、あの招待も\x01",
            "何か思惑がありそうだったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x106,
        "#10708F#12P#N……確かに。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0134
    ChrTalk(
        0x101,
        "#00008F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    #C0135
    ChrTalk(
        0x101,
        (
            "#00003F#11P──いずれにせよ、\x01",
            "次の目的地は決まった。\x02\x03",

            "#00008F《赤い星座》の部隊が\x01",
            "警備しているらしいが……\x02\x03",

            "#00001Fノエル、どのくらいの規模か\x01",
            "知っているか？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x109,
        (
            "#10106F#12Pそうですね……\x01",
            "一個中隊はいると思います。\x02\x03",

            "#10113Fこの人数で当たっても\x01",
            "正直、勝ち目はないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#00006F#11Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x104,
        (
            "#00308F#11P何とか陽動して\x01",
            "戦力を分散できりゃあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x106,
        "#10701F#12P#Nだったら、ここは私が──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x107, 0x20)
    TurnDirection(0x107, 0x109, 500)
    Sleep(150)
    ClearChrFlags(0x107, 0x20)

    #C0140
    ChrTalk(
        0x107,
        (
            "#01203F#11P#3Cいや、ここは私が引き受けよう。\x02\x03",

            "#01201F元の姿に戻れば、かなりの戦力を\x01",
            "引きつけられるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    OP_68(-50, 1100, 2370, 1000)

    def lambda_6B7F():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6B7F)
    Sleep(50)

    def lambda_6B8F():
        TurnDirection(0x104, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6B8F)
    Sleep(50)

    def lambda_6B9F():
        TurnDirection(0x109, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B9F)
    Sleep(50)

    def lambda_6BAF():
        TurnDirection(0x106, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6BAF)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    OP_6F(0x79)

    #C0141
    ChrTalk(
        0x103,
        "#00205F#5Pツァイト……？\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#00001F#5Pその……いいのか？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x107,
        (
            "#01200F#11P#3C私はあくまでおぬしらの\x01",
            "手助けに徹するつもりだ。\x02\x03",

            "おぬしらが仲間を集め、\x01",
            "力を蓄えつつある今、\x01",
            "そろそろ助力は不要だろう。\x02\x03",

            "#01203Fまあ、最後の大サービスとでも\x01",
            "思うがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#00000F#5Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x103,
        "#00204F#5Pありがとう、ツァイト。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        "#00302F#5Pああ、マジに助かるぜ。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x105,
        (
            "#10406F#5Pといっても、相当厳しい戦いに\x01",
            "なるのは間違いなさそうだけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    #C0148
    ChrTalk(
        0x101,
        (
            "#00003F#5Pそれでもミシュラムには\x01",
            "議長だけじゃなくてエリィもいる。\x02\x03",

            "#00007F万全の準備を整えて……\x01",
            "何としても２人を解放しよう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E19():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6E19)
    Sleep(50)

    def lambda_6E29():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E29)
    Sleep(50)

    def lambda_6E39():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6E39)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    #C0149
    ChrTalk(
        0x103,
        "#00201F#5P……はい！\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#00307F#11Pおうよ！\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x109,
        "#10101F#12P了解です！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20940, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ツァイトがパーティから離脱しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x8, 0x141)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルがＳクラフト\x01\x07\x02",

            "『アームドフォース』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『アームドフォース』\x07\x05",
            "をＳブレイクに登録しますか？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【は  い】\x01",      # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7014")
    SetChrChipPat(0x8, 0x6, 0x141)

    label("loc_7014")

    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x6, 0xFF)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x33, 5)
    SetScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x26, 6)
    SetScenarioFlags(0x27, 0)
    SetScenarioFlags(0x1A3, 3)
    OP_29(0xAF, 0x1, 0x11)
    SetScenarioFlags(0x33, 5)
    SetScenarioFlags(0x36, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sound(498, 2, 100, 0)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_20_61DB end

    def Function_21_7076(): pass

    label("Function_21_7076")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #A0156
    AnonymousTalk(
        0x101,
        (
            "#00003F（……ここに降下したら\x01",
            "  すぐに《赤い星座》の部隊と\x01",
            "  戦闘になるだろう。）\x02\x03",

            "#00013F（補給もできない……\x01",
            "  万全の準備は出来ているか？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",        # 0
            "【ミシュラムに降下する】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7174"),
        (1, "loc_7182"),
        (SWITCH_DEFAULT, "loc_72CE"),
    )


    label("loc_7174")

    FadeToBright(0, 0)
    Jump("loc_72CE")

    label("loc_7182")

    Call(0, 6)
    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C5")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_72B5")

    label("loc_71C5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E8")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_72B5")

    label("loc_71E8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_720B")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_72B5")

    label("loc_720B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_722E")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_72B5")

    label("loc_722E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7251")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_72B5")

    label("loc_7251")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7274")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_72B5")

    label("loc_7274")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7297")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_72B5")

    label("loc_7297")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B5")
    SetScenarioFlags(0x3C, 7)

    label("loc_72B5")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_72CE")

    label("loc_72CE")

    Return()

    # Function_21_7076 end

    def Function_22_72CF(): pass

    label("Function_22_72CF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis285.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02300.itp")
    AddParty(0x1, 0xFF, 0xFF)
    OP_32(0x1, 0x0, 0x58)
    OP_32(0x1, 0x5, 0x64)
    OP_42(0x1, 0x405, 0xFF)
    OP_42(0x1, 0x5ED, 0xFF)
    OP_42(0x1, 0x651, 0xFF)
    OP_38(0x1, 0x83, 0x2)
    OP_38(0x1, 0x84, 0x2)
    OP_38(0x1, 0x85, 0x2)
    OP_38(0x1, 0x86, 0x2)
    OP_42(0x1, 0xA4, 0x3)
    OP_42(0x1, 0x7E, 0x4)
    OP_42(0x1, 0x82, 0x5)
    OP_42(0x1, 0xB3, 0x6)
    SetScenarioFlags(0x20, 3)
    SetScenarioFlags(0x20, 6)
    AddCraft(0x2, 0xB1)
    OP_32(0x6, 0x0, 0x5A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xA)
    SetChrSubChip(0x102, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x1)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 3, 0, 0)
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x12, 98470, 70, -101100, 180)
    SetChrPos(0x101, 100150, 70, -102850, 270)
    SetChrPos(0x102, 100100, 70, -104800, 270)
    SetChrPos(0xF, 96800, 70, -102650, 90)
    SetChrPos(0x105, 96800, 70, -104800, 90)
    SetChrPos(0x103, 102350, 0, -104050, 270)
    SetChrPos(0x104, 102060, 0, -102890, 270)
    SetChrPos(0x9, 101700, 0, -105600, 315)
    SetChrPos(0x109, 96950, 0, -100550, 135)
    SetChrPos(0xC, 96050, 0, -100600, 135)
    SetChrPos(0x106, 101350, 0, -100350, 225)
    SetChrPos(0x13, 99400, 0, -98000, 180)
    SetChrPos(0x8, 97150, 0, -106150, 0)
    OP_68(98500, 1250, -103350, 0)
    MoveCamera(44, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15250, 0)
    SetCameraDistance(16250, 3000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0157
    ChrTalk(
        0xF,
        (
            "#02101F#6P──それでは、議長。\x01",
            "ご決心にお変わりありませんね？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0158
    AnonymousTalk(
        0x12,
        (
            "うむ……この中にも\x01",
            "反対する者はいるだろう。\x02\x03",

            "だが、ここから始めなければ\x01",
            "我々は前に進めないと思うのだ。\x02\x03",

            "いかに仮初#4Rかりそめ#の秩序と\x01",
            "覇権を失ったとしても。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0159
    ChrTalk(
        0x102,
        "#00108F#11Pはい……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        "#10108F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x105,
        (
            "#10404F#6P『クロスベル独立国』の無効宣言か。\x02\x03",

            "#10400Fたしかに前政府代表の一人である\x01",
            "議長閣下ならではのカードだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x106,
        (
            "#10701F#5Pでも、具体的には\x01",
            "どのような形でその宣言を？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "#01908F#6P市民や国防軍にも伝わらないと\x01",
            "効果は薄いんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        (
            "#00204F#11Pそれについてはヨナが\x01",
            "アイデアがあるそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(99360, 1250, -104040, 1000)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0xF, 0x2)
    SetChrSubChip(0x12, 0x1)
    SetChrSubChip(0x105, 0x0)

    def lambda_789F():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_789F)
    Sleep(50)

    def lambda_78AF():
        TurnDirection(0x106, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_78AF)
    Sleep(50)

    def lambda_78BF():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_78BF)
    Sleep(50)

    def lambda_78CF():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_78CF)
    Sleep(50)

    def lambda_78DF():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_78DF)
    Sleep(50)

    def lambda_78EF():
        TurnDirection(0x13, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_78EF)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0165
    AnonymousTalk(
        0x9,
        (
            "ああ、タングラム丘陵に\x01",
            "導力ネットをレマン自治州と結ぶ\x01",
            "実験用の無線ブースターがあるんだ。\x02\x03",

            "あそこからなら隙を突いて\x01",
            "ハッキングを仕掛けられるはずさ。\x02\x03",

            "１０分くらいなら\x01",
            "何とか持たせられるはずだぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0166
    ChrTalk(
        0x104,
        (
            "#00305F#5Pよく分からんが……\x01",
            "要はあの街頭スクリーンなんかも\x01",
            "乗っ取れるわけだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#00204F#11Pはい、それと国防軍方面の\x01",
            "全端末にもアクセスできます。\x02\x03",

            "#00202Fソーニャ司令の出した条件も\x01",
            "クリアできるのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "#12100F#6P大統領サイドの正当性が揺らげば\x01",
            "国防軍はしばらく様子見になる……\x02\x03",

            "#12102F動きやすくなるのは確かだな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0169
    ChrTalk(
        0x101,
        "#00008F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(98990, 1250, -103480, 1000)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0xF, 0x0)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_7C00():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7C00)
    Sleep(50)

    def lambda_7C10():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_7C10)
    Sleep(50)

    def lambda_7C20():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7C20)
    Sleep(50)

    def lambda_7C30():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7C30)
    Sleep(50)

    def lambda_7C40():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7C40)
    Sleep(50)

    def lambda_7C50():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7C50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)

    #C0170
    ChrTalk(
        0x102,
        "#00108F#11Pロイド……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x12,
        (
            "#02503F#5Pふむ、ロイド君。\x02\x03",

            "#02500F『独立国』の無効宣言は\x01",
            "あくまで私の考えでしかない。\x02\x03",

            "リーダーである君が反対なら\x01",
            "実行に移すつもりはないが？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0172
    ChrTalk(
        0x101,
        (
            "#00000F#11P──いえ、お願いします。\x02\x03",

            "#00003Fかつてディーターさんは……\x01",
            "ＩＢＣ総裁だった頃の彼は\x01",
            "『正義』について語っていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        "#00105F#11Pあ……\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(80, 30, -1, -1)

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "結局のところ、人は正義を\x01",
            "求めてしまう生き物なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なぜなら《正義》というものは\x01",
            "人が社会を信頼する“根拠”だからだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    SetMessageWindowPos(10, 100, -1, -1)

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "政治の腐敗や、マフィアの問題……\x02",
        )
    )

    CloseMessageWindow()

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それを警察が取り締まらなくても\x01",
            "経済的には恵まれているから\x01",
            "多くの市民は生活に困らない。\x02",
        )
    )

    CloseMessageWindow()

    #A0178
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "だが、そんな中でも\x01",
            "やはり人は《正義》というものを\x01",
            "どこかに求めざるを得ない。\x02",
        )
    )

    CloseMessageWindow()

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どんな形であれ、社会を信頼できる\x01",
            "安心感を欲してしまうからだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    SetMessageWindowPos(250, 50, -1, -1)

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "だからこそ私は──\x01",
            "君たちに期待したいのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "君たちが、君たちなりに\x01",
            "《正義》を追求している姿……\x02",
        )
    )

    CloseMessageWindow()

    #A0182
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それが目に見える形で市民に\x01",
            "示される事が重要だと思うのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    VolumeBGM(0x64, 0x3E8)

    #C0183
    ChrTalk(
        0x12,
        "#02505F#5Pディーター君がそんな事を……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x104,
        "#00306F#11Pあったなぁ、そんな事も。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#00208F#11Pまだ１年も経っていないのに\x01",
            "すごく懐かしい気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#00003F#11P──あの時の総裁の言葉。\x02\x03",

            "#00008Fあれが本心からか、\x01",
            "それとも単なるポーズなのかは\x01",
            "正直、分かりませんが……\x02\x03",

            "#00001Fそれでも俺たちの心に\x01",
            "響くものがあったのも確かです。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        "#00106F#11Pそうね……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xF,
        "#02103F#6Pふむ、確かに興味深い言葉だわ。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00000F#11Pええ、ですから……\x01",
            "改めてあの言葉を彼自身に\x01",
            "突きつけてみたいんです。\x02\x03",

            "#00003F俺たちのためにも、彼のためにも。\x02\x03",

            "#00001F何よりも市民や国防軍の人たちが\x01",
            "考えるきっかけにするためにも。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x12,
        (
            "#02503F#5P──分かった。\x02\x03",

            "#02500F今の言葉、私なりに噛み砕いて\x01",
            "宣言に反映させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        "#00004F#11Pはい、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x105,
        "#10402F#6P決まりだね。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xF,
        (
            "#02104F#6Pそれじゃあ具体的な段取りを\x01",
            "固めるとしましょう！\x02\x03",

            "#02110Fヨナ君、フランちゃん！\x01",
            "技術的なサポートはよろしくね！\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xC,
        "#01909F#5Pはいっ！\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x9,
        "#02302F#11Pハッ、任せとけって。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16750, 1500)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして、マクダエル議長による\x01",
            "『クロスベル独立国』無効宣言の\x01",
            "具体的な段取りが詰められていった。\x02\x03",

            "ヨナとフランによって\x01",
            "導力ネットにハッキングを仕掛ける\x01",
            "技術的な見込みも付けられ……\x02\x03",

            "後はタイミングを見計らうだけとなった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e4400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_72CF end

    def Function_23_858D(): pass

    label("Function_23_858D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #A0197
    AnonymousTalk(
        0x101,
        (
            "#00003F（実験用の無線ブースター……\x01",
            "  ここから導力ネットをハッキングして\x01",
            "  『クロスベル独立国』の無効宣言をする。）\x02\x03",

            "#00001F（後戻りはできない……\x01",
            "  心の準備は出来ているか？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",          # 0
            "【ブースター地点へ向かう】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_86AF"),
        (1, "loc_86BD"),
        (SWITCH_DEFAULT, "loc_88C1"),
    )


    label("loc_86AF")

    FadeToBright(0, 0)
    Jump("loc_88C1")

    label("loc_86BD")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_877E")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_870B():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_870B)
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 0, 800000, 0)
    MoveCamera(30, -7, 0, 0)
    MoveCamera(20, -7, 0, 3000)
    OP_6E(500, 0)
    SetCameraDistance(111000, 0)
    Sleep(300)
    Sound(499, 0, 100, 0)
    Sleep(1700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    SetEventSkip(0x1, 0x0)

    label("loc_877E")

    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87BE")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_88AE")

    label("loc_87BE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E1")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_88AE")

    label("loc_87E1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8804")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_88AE")

    label("loc_8804")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8827")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_88AE")

    label("loc_8827")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_884A")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_88AE")

    label("loc_884A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_886D")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_88AE")

    label("loc_886D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8890")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_88AE")

    label("loc_8890")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88AE")
    SetScenarioFlags(0x3C, 7)

    label("loc_88AE")

    PartySelect(2)
    SetScenarioFlags(0x23, 0)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_88C1")

    label("loc_88C1")

    Return()

    # Function_23_858D end

    def Function_24_88C2(): pass

    label("Function_24_88C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    SoundLoad(952)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88F0")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_88F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8903")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_8903")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8916")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_8916")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x1E, 0x1E, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x12, 0, 500, 2400, 0)
    SetChrPos(0xF, 900, 500, 1750, 0)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, 2150, -1500, 7300, 90)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 750, 250, 400, 0)
    SetChrPos(0x106, -950, 0, -1650, 0)
    OP_68(0, 3300, 2000, 0)
    OP_68(0, 1500, 2000, 3500)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0198
    ChrTalk(
        0xC,
        (
            "#01901F#5P──カメラの準備はＯＫ！\x01",
            "音声テストもバッチリです！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        (
            "#12100F#5Pこちらもブースターの真上に来た。\x02\x03",

            "いつでも始められるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xF,
        (
            "#02109F#11Pオッケーオッケー。\x02\x03",

            "#02100F議長、よろしいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x12,
        "#02501F#5Pああ、始めてくれたまえ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_68(-2830, -750, 6760, 2000)
    MoveCamera(45, 30, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)

    #C0202
    ChrTalk(
        0x9,
        (
            "#02304F#11Pへへ、そんじゃあ始めるぜ。\x02\x03",

            "#02301F──無線ブースターより、\x01",
            "導力ネットへのハッキングを開始。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(952, 2, 80, 0)
    BeginChrThread(0x1F, 1, 0, 25)
    SetCameraDistance(16000, 3000)
    BeginChrThread(0x9, 0, 0, 26)
    Sleep(1000)
    StopSound(498, 1000, 100)
    StopSound(952, 1000, 70)
    EndChrThread(0x1F, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x0)
    OP_24(0x3B8)
    SetScenarioFlags(0x22, 1)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_88C2 end

    def Function_25_8CBC(): pass

    label("Function_25_8CBC")

    Sound(938, 0, 60, 0)
    Sound(836, 0, 60, 0)
    Sleep(800)
    Sound(836, 0, 60, 0)
    Return()

    # Function_25_8CBC end

    def Function_26_8CD2(): pass

    label("Function_26_8CD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CEA")
    OP_A1(0xFE, 0x7D0, 0x2, 0x0, 0x1)
    Jump("Function_26_8CD2")

    label("loc_8CEA")

    Return()

    # Function_26_8CD2 end

    def Function_27_8CEB(): pass

    label("Function_27_8CEB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    LoadChrToIndex("apl/ch51714.itc", 0x20)
    SoundLoad(952)
    SoundLoad(938)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x1E, 0x1E, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x12, 0, 500, 2400, 0)
    SetChrPos(0xF, 900, 500, 1750, 0)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, 2150, -1500, 7300, 90)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 750, 250, 400, 0)
    SetChrPos(0x106, -950, 0, -1650, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_68(-3150, -750, 7150, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(17000, 5000)
    BeginChrThread(0x9, 0, 0, 26)
    Sound(952, 2, 70, 0)
    BeginChrThread(0x1F, 1, 0, 28)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x9, 0x0)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x1F, 0x1)
    StopSound(938, 1000, 100)
    StopSound(952, 1000, 70)
    Sound(839, 0, 100, 0)
    Sleep(400)
    Sound(839, 0, 100, 0)

    #C0203
    ChrTalk(
        0x9,
        (
            "#02302F#11Pよっしゃ！\x01",
            "通信機能を掌握したぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1500, 2000, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)

    #C0204
    ChrTalk(
        0xC,
        "#01901F#5Pカメラ、切り替えます！\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xF,
        "#02110F#11Pええ、いいわよ！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_68(0, 1800, 2000, 2000)
    MoveCamera(45, 20, 0, 2000)
    OP_6F(0x79)
    Fade(250)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x20)
    OP_A0(0xF, 1500, 0x0, 0x2)
    OP_0D()
    OP_70(0x1, 0x21)
    Sound(72, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0206
    AnonymousTalk(
        0xF,
        (
            "──皆さん、こんにちは。\x02\x03",

            "クロスベル通信社所属、\x01",
            "グレイス・リン報道記者です。\x02\x03",

            "念のため言っておきますと\x01",
            "クロスベル通信社は今回の件に\x01",
            "まったく関知しておりません。\x02\x03",

            "わたくしの独断による報道ですので\x01",
            "あしからずご了承ください。\x02\x03",

            "……さて、早速ですが、\x01",
            "ある方を紹介したいと思います。\x02\x03",

            "《クロスベル自治州》代表、\x01",
            "ヘンリー・マクダエル議長閣下です！\x02",
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
    OP_70(0x1, 0x22)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7566", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0207
    AnonymousTalk(
        0x12,
        (
            "──クロスベルの市民諸君、\x01",
            "及びこの映像をご覧になっている\x01",
            "全ての方々に申し上げる。\x02\x03",

            "《クロスベル自治州議会》議長、\x01",
            "ヘンリー・マクダエルであります。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetCameraDistance(21000, 3000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3B8)
    OP_24(0x3AA)
    SetScenarioFlags(0x23, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_8CEB end

    def Function_28_937E(): pass

    label("Function_28_937E")

    Sound(938, 2, 70, 0)

    label("loc_9384")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_939D")
    Sound(836, 0, 60, 0)
    Sleep(700)
    Jump("loc_9384")

    label("loc_939D")

    Return()

    # Function_28_937E end

    def Function_29_939E(): pass

    label("Function_29_939E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearMapObjFlags(0x1, 0x4)
    OP_70(0x1, 0x23)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0208
    AnonymousTalk(
        0x101,
        (
            "#00005F──《結界》の\x01",
            "解除方法が分かった！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7580", 0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    OP_68(660, 700, 3830, 0)
    MoveCamera(44, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    SetCameraDistance(21850, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(100, 70, -1, -1)
    SetChrName("ヨルグ老人")

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "うむ、それとあの３体の\x01",
            "《神機#4Rアイオーン#》の力を抑える方法をな。\x02\x03",

            "ずばり鍵は“大鐘”にある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0210
    ChrTalk(
        0x103,
        (
            "#00201F#12P#N“大鐘”……\x01",
            "塔や僧院にあったものですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0211
    ChrTalk(
        0x105,
        (
            "#10401F#6Pそれが結界や人形たちを\x01",
            "強化しているってことかい？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 70, -1, -1)
    SetChrName("ヨルグ老人")

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いや、強化しているのは\x01",
            "あくまで《至宝》の力のはずだ。\x02\x03",

            "だが恐らく、現時点では\x01",
            "《至宝》は完全ではないのだろう。\x02\x03",

            "その常識外れの“奇蹟”を\x01",
            "広範囲に渡って顕現させるためには\x01",
            "特異な“場”に頼る必要があるらしい。\x02\x03",

            "大鐘同士による\x01",
            "“共鳴”が生み出す“場”にな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0213
    ChrTalk(
        0x106,
        "#10708F#12Pあの大鐘にはそんな働きが……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#00107F#12Pそ、それでは鐘の共鳴を\x01",
            "止めてしまえば……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, 70, -1, -1)
    SetChrName("ヨルグ老人")

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "うむ、あの巨大な結界を\x01",
            "解除できるかもしれぬし……\x02\x03",

            "ガレリア要塞を消滅させた\x01",
            "白い《神機#4Rアイオーン#》の力なども\x01",
            "ある程度は抑えられるだろう。\x02\x03",

            "まあ、断言までは出来ぬがな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0216
    ChrTalk(
        0x104,
        (
            "#00305F#12Pいや、試してみる価値は\x01",
            "あるんじゃねえか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "#12100F#5Pうむ……あの結界と\x01",
            "白い人形は最大の障害だった。\x02\x03",

            "その２つがある限り、\x01",
            "クロスベル市を解放することは\x01",
            "永遠に不可能だったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x109,
        (
            "#10101F#12Pとなると……\x01",
            "《塔》と《僧院》ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#00003F#11Pああ、古戦場に運ばれた大鐘は\x01",
            "市内の中央広場に戻されたようだ。\x02\x03",

            "#00000Fそれには手が出せないけど、\x01",
            "《塔》と《僧院》の鐘なら共鳴を\x01",
            "止めることは出来る……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 70, -1, -1)
    SetChrName("ヨルグ老人")

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まあ、どちらも《結社》が\x01",
            "守っている場所だがな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0221
    ChrTalk(
        0x101,
        "#00013F#12Pそういえば……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x103,
        "#00206F#12P#N……確かにそうでしたね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(110, 70, -1, -1)
    SetChrName("ヨルグ老人")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうやら《月の僧院》は\x01",
            "カンパネルラがいるらしい。\x02\x03",

            "そして《星見の塔》は……\x01",
            "アリアンロードがいるようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0224
    ChrTalk(
        0x106,
        "#10701F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x104,
        "#00301F#12Pあの常識外れの女騎士か……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x105,
        (
            "#10406F#5P……正直、困ったね。\x02\x03",

            "#10408F《道化師》の方は\x01",
            "何とかなるかもしれないが……\x02\x03",

            "#10401Fかの《鋼の聖女》が相手じゃ、\x01",
            "難攻不落としか言いようがない。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        "#00008F#12P……そんなに強いのか？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x105,
        (
            "#10406F#5Pああ、《結社》には凄まじい\x01",
            "使い手がゴロゴロしてるけど……\x02\x03",

            "彼女はそういった達人たちとも\x01",
            "一線を画している存在でね。\x02\x03",

            "#10401Fまるで人の身では勝てない事が#22R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#\x01",
            "決まっている#12R㈲　㈲　㈲　㈲　㈲　㈲#かのような強さだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x109,
        "#10111F#12Pそ、そこまで……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#00108F#12Pワジ君は教会でも\x01",
            "《守護騎士#8Rド ミ ニ オ ン#》と呼ばれる\x01",
            "特別な存在だそうだけど……\x02\x03",

            "#00101Fそれでも対抗は不可能なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x105,
        (
            "#10403F#5Pああ、《聖痕》の力を使っても\x01",
            "あの鎧には通用しないだろうね。\x02\x03",

            "#10408F何とか太刀打ちできるとしたら\x01",
            "ウチの総長くらいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        (
            "#12100F#5Pだが、大陸全土がこの状況だ。\x02\x03",

            "さすがにセルナート総長に\x01",
            "動いてもらうわけにもいくまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x105,
        (
            "#10406F#5Pはぁ、そうなんだよね。\x02\x03",

            "#10408F……こんな時にケビンがいれば\x01",
            "少しは当てに出来るんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0234
    ChrTalk(
        0x101,
        (
            "#00003F#11P──悩んでいる暇はない。\x02\x03",

            "#00001Fこの状況を打開できる光明が\x01",
            "ようやく見えて来たんだ。\x02\x03",

            "ここは敢えて\x01",
            "踏み込んでみるべきだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        "#00300F#12Pだな。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x103,
        "#00204F#12P#N同感です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0237
    ChrTalk(
        0x106,
        (
            "#10701F#12Pどんな達人だろうと……\x01",
            "突き崩せる一点は\x01",
            "ゼロではないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x105,
        "#10400F#5Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        (
            "#00104F#12Pそうね……\x01",
            "こんな場所で躓#2Rつまづ#いていたら\x01",
            "ベルたちにも届かないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x109,
        (
            "#10100F#12P行きましょう！\x01",
            "《塔》と《僧院》へ！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, 70, -1, -1)
    SetChrName("ヨルグ老人")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まあ、幸運を祈っておこう。\x02\x03",

            "せめてアリアンロードのいる\x01",
            "《塔》は後回しにするがいい。\x02\x03",

            "彼女はおろか、戦乙女たちにすら\x01",
            "返り討ちに遭いたくなければな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22850, 2000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0242
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《月の僧院》はマインツ山道の途中にある\x01",
            "トンネル道の分岐から行く事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PartySelect(1)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A4, 2)
    OP_29(0xAF, 0x1, 0x15)
    OP_29(0xAF, 0x4, 0x10)
    OP_29(0xB0, 0x4, 0x2)
    OP_29(0xB0, 0x1, 0x0)
    PlayBGM("ed7570", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_29_939E end

    def Function_30_A533(): pass

    label("Function_30_A533")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    PartySelect(2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A55A")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_A55A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A56D")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_A56D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A580")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_A580")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_70(0x1, 0x26)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x12, -3300, 0, 250, 45)
    SetChrPos(0xF, -3800, 0, -1000, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    OP_68(410, 800, 4070, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(21500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0243
    ChrTalk(
        0x102,
        "#00105F#12Pす、凄い……！\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        (
            "#00302F#12Pツンツン頭の神父が言ってた\x01",
            "助っ人ってのは、\x01",
            "エステルちゃんたちだったのかよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#10404F#5Pああ、本人達たっての希望で\x01",
            "リベールから連れてきたらしい。\x02\x03",

            "#10402F──それより、チャンスだね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    #C0246
    ChrTalk(
        0x8,
        (
            "#12107F#5Pうむ、光学迷彩を解除しつつ\x01",
            "南口に降下する……！\x02\x03",

            "船底のハッチから降りるがいい！\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        "#00007F#12P分かった……！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x103,
        "#00201F#12P#Nよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_A8B9():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_A8B9)
    Sleep(50)

    def lambda_A8C9():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_A8C9)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0xF, 0)
    Sleep(150)

    #C0249
    ChrTalk(
        0x12,
        "#02507F#6P#N──女神の加護を。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    #C0250
    ChrTalk(
        0xC,
        "#01901F#5P皆さん、どうか気をつけて！\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xF,
        (
            "#02110F#6P#Nあたしは上空から\x01",
            "取材をさせてもらうわ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x9, 0x1)
    Sleep(100)

    #C0252
    ChrTalk(
        0x9,
        (
            "#02302F#5Pま、こっちも導力ネットから\x01",
            "バックアップはしてやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 1500)
    StopSound(498, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_A533 end

    def Function_31_A9EE(): pass

    label("Function_31_A9EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11402.itc", 0x1E)
    LoadChrToIndex("apl/ch51025.itc", 0x1F)
    LoadChrToIndex("chr/ch11502.itc", 0x20)
    LoadEffect(0x0, "event/ev10037.eff")
    LoadEffect(0x1, "event/ev17103.eff")
    LoadEffect(0x2, "event/ev17104.eff")
    LoadEffect(0x3, "event/ev17105.eff")
    SoundLoad(825)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0xF)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani2")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani2")
    SetChrPos(0x1A, 0, 500, 2400, 0)
    SetChrPos(0x19, -3100, -1350, 7100, 315)
    SetChrPos(0x17, 3100, -1350, 7100, 45)
    SetChrPos(0x18, 0, -1350, 6700, 0)
    OP_68(-1590, 1500, 4910, 0)
    MoveCamera(39, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    SetCameraDistance(19850, 2500)
    BeginChrThread(0x17, 0, 0, 32)
    BeginChrThread(0x17, 1, 0, 34)
    BeginChrThread(0x1F, 2, 0, 33)
    Sound(825, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0253
    ChrTalk(
        0x17,
        "#5P──鏡面装甲、７０％破損！\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x18,
        "#11Pこ、これ以上は保ちません！\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x19,
        "#13801F#11P敵アイオーン、さらに加速！\x02",
    )

    CloseMessageWindow()

    #N0256
    NpcTalk(
        0x1A,
        "守護騎士ケビン",
        (
            "#04303F#11Pくっ……マズイな。\x02\x03",

            "#04308Fこうなったら……\x01",
            "アレを使うしかないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x19, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x19, 0x1)
    Sleep(50)
    SetChrSubChip(0x18, 0x1)
    Sleep(50)
    SetChrSubChip(0x17, 0x2)

    #C0257
    ChrTalk(
        0x17,
        "#5Pグラハム卿……！？\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x18,
        "#11Pまさか……\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x19,
        (
            "#13807F#5P待って……！\x01",
            "いきなりすぎる！\x02",
        )
    )

    CloseMessageWindow()

    #N0260
    NpcTalk(
        0x1A,
        "守護騎士ケビン",
        (
            "#04304F#11Pここで踏ん張れないようなら\x01",
            "名を継いだ姉さんに顔向けできん。\x02\x03",

            "#04300Fみんな、サポートしてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x17,
        "#5P……承知しました。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x18, 0x0)
    Sleep(50)
    SetChrSubChip(0x17, 0x0)
    Sleep(300)
    Sound(1002, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1800, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1300, -200, 4500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0262
    ChrTalk(
        0x18,
        "#11Pモード《Ｓ#2Rスティグマ#》を起動……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0263
    ChrTalk(
        0x19,
        "#13808F#5Pケビン……\x02",
    )

    CloseMessageWindow()

    #N0264
    NpcTalk(
        0x1A,
        "守護騎士ケビン",
        (
            "#04304F#11Pリース、心配すんな。\x02\x03",

            "#04302Fお前の仕事や……\x01",
            "敵の捕捉は任せたぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x19,
        "#13801F#5P……わかった！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x19, 0x0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrPos(0x1A, 0, 500, 3300, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    BeginChrThread(0x1A, 0, 0, 35)
    OP_68(-1560, 1500, 5150, 800)
    OP_6F(0x79)
    SetCameraDistance(17800, 25000)
    Sleep(500)

    #N0266
    NpcTalk(
        0x1A,
        "守護騎士ケビン",
        "#04303F#11P#3C#40W#30A『我が深淵にて煌#2Rきらめ#く蒼#2Rあお#の刻印よ……』\x02",
    )
    #Auto

    CloseMessageWindow()
    Sound(895, 0, 100, 0)
    BeginChrThread(0x1F, 0, 0, 36)
    PlayEffect(0x0, 0xFF, 0x1A, 0x3, 0, 400, -100, 0, 0, 0, 650, 650, 650, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    #N0267
    NpcTalk(
        0x1A,
        "守護騎士ケビン",
        "#04303F#11P#3C#40W#46A『天に上りて煉獄#4Rれんごく#を照らす光の柱と化せ……』\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)
    BeginChrThread(0x1F, 1, 0, 37)
    PlayEffect(0x3, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0268
    ChrTalk(
        0x17,
        "#5P──《メルカバ》の全導力を収束！\x05\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    #C0269
    ChrTalk(
        0x18,
        (
            "#11P《聖痕》パターンを認識！\x01",
            "外部への展開を開始します！\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0270
    ChrTalk(
        0x19,
        (
            "#13807F#11P敵アイオーン、変型！\x01",
            "主砲を展開して突っ込んで来る！\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    #N0271
    NpcTalk(
        0x1A,
        "守護騎士ケビン",
        (
            "#04301F#11P#40W#32A守護騎士第五位、\x01",
            "《千の護#2Rまもり#手#2Rて#》が命ずる……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(800)
    Fade(500)
    EndChrThread(0x1A, 0x0)
    SetChrSubChip(0x1A, 0x5)
    SetCameraDistance(16800, 800)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #N0272
    NpcTalk(
        0x1A,
        "守護騎士ケビン",
        "#04307F#11P#4S#36A《聖痕砲》メギデルス──展開！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetCameraDistance(19800, 3000)
    Sound(829, 0, 100, 0)
    FadeToDark(3000, 16777215, -1)
    Sleep(1500)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1F, 0x2)
    OP_0D()
    StopSound(825, 1000, 70)
    StopSound(498, 1000, 100)
    Sleep(1000)
    SetScenarioFlags(0x23, 5)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_A9EE end

    def Function_32_B2F2(): pass

    label("Function_32_B2F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B320")
    OP_7D(0xFF, 0x50, 0x50, 0x0, 0x1F4)
    Sleep(100)
    Sleep(700)
    OP_7D(0xFF, 0xC8, 0xC8, 0x0, 0x1F4)
    Sleep(600)
    Sleep(100)
    Jump("Function_32_B2F2")

    label("loc_B320")

    Return()

    # Function_32_B2F2 end

    def Function_33_B321(): pass

    label("Function_33_B321")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B343")
    Sleep(100)
    Sound(840, 0, 70, 0)
    Sleep(700)
    Sleep(600)
    Sleep(100)
    Jump("Function_33_B321")

    label("loc_B343")

    Return()

    # Function_33_B321 end

    def Function_34_B344(): pass

    label("Function_34_B344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B368")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_34_B344")

    label("loc_B368")

    Return()

    # Function_34_B344 end

    def Function_35_B369(): pass

    label("Function_35_B369")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B380")
    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("Function_35_B369")

    label("loc_B380")

    Return()

    # Function_35_B369 end

    def Function_36_B381(): pass

    label("Function_36_B381")

    Sound(934, 0, 50, 0)
    Sleep(1500)

    label("loc_B38A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3A3")
    Sound(934, 0, 30, 0)
    Sleep(1500)
    Jump("loc_B38A")

    label("loc_B3A3")

    Return()

    # Function_36_B381 end

    def Function_37_B3A4(): pass

    label("Function_37_B3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3BD")
    Sound(929, 0, 50, 0)
    Sleep(2200)
    Jump("Function_37_B3A4")

    label("loc_B3BD")

    Return()

    # Function_37_B3A4 end

    def Function_38_B3BE(): pass

    label("Function_38_B3BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B3E3")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_B3E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B3F6")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_B3F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B409")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_B409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B41C")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_B41C")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_4B(0xF, 0xFF)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x27)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(0, 700, 3000, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(20000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0273
    ChrTalk(
        0x9,
        (
            "#02310F#5P──しっかしまあ、\x01",
            "トンでもねーのが現れたよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "#01908F#5P本当にあれ、キーアちゃんが\x01",
            "出現させたんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#00206F#12Pええ……\x01",
            "間違いなさそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C《碧の大樹》──\x01",
            "人による至宝の完成形か。\x02\x03",

            "#01201Fよもや人の子らの妄執が\x01",
            "ここまでしてのけるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x105,
        (
            "#10401F#5Pあの大樹が\x01",
            "どんな力を持っているのか\x01",
            "君にも判らないんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C……うむ。\x01",
            "ただあの碧い光からは\x01",
            "尋常ならざるものを感じる。\x02\x03",

            "#01200F七耀の力の全て……\x01",
            "特に《幻》《時》《空》を\x01",
            "併せ持つと言うべきか。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        (
            "#00106F#6P元々《零の至宝》は\x01",
            "《幻の至宝》を再現するために\x01",
            "クロイス家の手で創造された……\x02\x03",

            "#00108Fその過程で《時》と《空》まで\x01",
            "併せ持ったということかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x13,
        (
            "#01203F#11P#3Cうむ、正直私にも\x01",
            "どこまでの事が出来るのか\x01",
            "見当もつかぬくらいだ。\x02\x03",

            "#01201F──と言うより、\x01",
            "『出来ないことは無い』と\x01",
            "言ってもいいのかもしれぬ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x104,
        "#00306F#12Pなんとまあ……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        "#12100F#5P女神に匹敵する力か……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0283
    ChrTalk(
        0x101,
        (
            "#00006F#11Pいずれにしても……\x01",
            "俺たちのやる事は変わらない。\x02\x03",

            "#00008Fアリオスさん、マリアベルさん、\x01",
            "イアン先生たち……\x02\x03",

            "#00013F彼らの真意を確かめつつ、\x01",
            "この手でキーアを取り戻すだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        "#00101F#12Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x109,
        "#10107F#12P……はい……！\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xF,
        (
            "#02110F#6Pいっや～、何て言うか、\x01",
            "マジで武者震いしてきたわね！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)

    def lambda_BA9D():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_BA9D)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xC, 0x2)

    def lambda_BAB2():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BAB2)
    Sleep(50)

    def lambda_BAC2():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BAC2)
    Sleep(50)

    def lambda_BAD2():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BAD2)
    Sleep(50)

    def lambda_BAE2():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BAE2)
    Sleep(50)

    def lambda_BAF2():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BAF2)
    Sleep(50)

    def lambda_BB02():
        TurnDirection(0x106, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_BB02)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    SetChrFlags(0x13, 0x20)

    def lambda_BB2C():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_BB2C)
    ClearChrFlags(0x13, 0x20)

    #C0287
    ChrTalk(
        0x10A,
        (
            "#00606F#11P……グレイス。\x01",
            "どうしてお前がここにいる？\x02\x03",

            "#00601Fマクダエル議長と一緒に、\x01",
            "船を降りたのではなかったのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10A, 500)

    #C0288
    ChrTalk(
        0xF,
        (
            "#02103F#5Pうっさいわね～。\x01",
            "あたしの勝手でしょ？\x02\x03",

            "#02100Fそれにクロスベル市民だって\x01",
            "今回の顛末は知りたがるはずよ。\x02\x03",

            "#02109Fまあ、そのあたりの\x01",
            "フォローは任せなさいって㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0289
    ChrTalk(
        0x101,
        "#00006F#11Pう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        "#00211F#11Pイマイチ不安ですが……\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        (
            "#00301F#11Pいずれにせよ、乗り込む前に\x01",
            "準備はしといた方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x106,
        (
            "#10708F#12Pそうですね……\x01",
            "何が待ち受けているか\x01",
            "分かりませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        (
            "#10403F#5P各地の戦闘も終わったし、\x01",
            "今ならクロスベルの何処にでも\x01",
            "メルカバで降りられるだろう。\x02\x03",

            "#10400F必要だったら指示するといい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0294
    ChrTalk(
        0x101,
        "#00000F#11Pああ、分かった。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A7, 1)
    OP_29(0xB2, 0x4, 0x2)
    OP_29(0xB2, 0x1, 0x0)
    SetScenarioFlags(0x34, 6)
    SetScenarioFlags(0x37, 6)
    SetScenarioFlags(0x20, 5)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7563")
    ReplaceBGM("ed7101", "ed7563")
    ReplaceBGM("ed7116", "ed7563")
    ReplaceBGM("ed7117", "ed7563")
    ReplaceBGM("ed7111", "ed7563")
    ReplaceBGM("ed7113", "ed7563")
    Sleep(500)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_38_B3BE end

    def Function_39_BF25(): pass

    label("Function_39_BF25")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    #A0295
    AnonymousTalk(
        0x101,
        (
            "#00003F（《碧の大樹》……\x01",
            "  あそこにキーアと\x01",
            "  全ての真実が待っている……）\x02\x03",

            "#00013F（準備はいいか……？）\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",        # 0
            "【《碧の大樹》へ向かう】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BFFA"),
        (1, "loc_C008"),
        (SWITCH_DEFAULT, "loc_C162"),
    )


    label("loc_BFFA")

    FadeToBright(0, 0)
    Jump("loc_C162")

    label("loc_C008")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C059")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_C149")

    label("loc_C059")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C07C")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_C149")

    label("loc_C07C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C09F")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_C149")

    label("loc_C09F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C2")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_C149")

    label("loc_C0C2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0E5")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_C149")

    label("loc_C0E5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C108")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_C149")

    label("loc_C108")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12B")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_C149")

    label("loc_C12B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C149")
    SetScenarioFlags(0x3C, 7)

    label("loc_C149")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x23, 7)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Jump("loc_C162")

    label("loc_C162")

    Return()

    # Function_39_BF25 end

    def Function_40_C163(): pass

    label("Function_40_C163")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    SoundLoad(498)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C18B")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_C18B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C19E")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_C19E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1B1")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_C1B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1C4")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_C1C4")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x28)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani2")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani2")
    BeginChrThread(0x101, 3, 0, 41)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(370, 700, 3790, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20750, 0)
    SetCameraDistance(20000, 1500)
    Sound(498, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0296
    ChrTalk(
        0xC,
        (
            "#01901F#5P──５時の方向に機影確認！\x02\x03",

            "赤い星座所属、\x01",
            "《ベイオウルフ号》です！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        "#00007F#12P現れたか……！\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x103,
        (
            "#00201F#12P#N《赤い星座》が運用している\x01",
            "強襲揚陸艦ですか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0299
    ChrTalk(
        0x104,
        (
            "#00303F#12Pああ、俺がいた頃から\x01",
            "強襲揚陸艦を運用するっていう\x01",
            "話は出ていたが……\x02\x03",

            "#00311Fまさか、もうあそこまで\x01",
            "使いこなしてるとはな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#00108F#12P今回の計画のため、クロイス家が\x01",
            "資金を出したのかもしれないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x105,
        (
            "#10403F#11Pどうやら《結社》の技術も\x01",
            "使われているみたいだけど……\x02\x03",

            "#10408Fアッバス、振り切れそうかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x8,
        "#12100F#5P何とかしてみよう。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        (
            "#02302F#5Pま、デカイ上にゴツそうだし、\x01",
            "速度じゃ負けないんじゃね？\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sound(499, 0, 80, 0)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani3")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani3")
    OP_68(370, 700, 790, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x24, 0)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_C163 end

    def Function_41_C66B(): pass

    label("Function_41_C66B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C68F")
    OP_82(0x2, 0x2, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_41_C66B")

    label("loc_C68F")

    Return()

    # Function_41_C66B end

    def Function_42_C690(): pass

    label("Function_42_C690")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    LoadChrToIndex("apl/ch51217.itc", 0x20)
    LoadChrToIndex("apl/ch51218.itc", 0x21)
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    LoadChrToIndex("apl/ch51220.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51224.itc", 0x25)
    LoadChrToIndex("apl/ch51774.itc", 0x26)
    LoadEffect(0x0, "event/ev17053.eff")
    LoadEffect(0x1, "event/ev17021.eff")
    LoadEffect(0x2, "event/ev17057.eff")
    SoundLoad(498)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    OP_F3(100000)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    SetChrPos(0x1E, 17000, -750, 13000, 0)
    OP_68(370, 700, 3790, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x101, 0, 0, 32)
    BeginChrThread(0x101, 1, 0, 34)
    BeginChrThread(0x1F, 2, 0, 33)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(498, 2, 100, 0)
    BeginChrThread(0x1F, 1, 0, 43)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0304
    ChrTalk(
        0x9,
        "#02311F#5Pうわあああっ！？\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x106,
        "#10712F#12P#Nこ、これは……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0306
    ChrTalk(
        0x109,
        (
            "#10110F#12P#Nまさか……\x01",
            "空中に撒かれた電磁機雷！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0307
    ChrTalk(
        0x103,
        (
            "#00207F#12P#N……間違いありません！\x01",
            "財団でも実用化されています！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x1, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 80, 80, 80, 0xFF, 0, 0, 0, 0)

    def lambda_CA0E():
        OP_96(0xFE, 0x2710, 0xFFFFFD12, 0x4E20, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CA0E)

    #C0308
    ChrTalk(
        0x10A,
        "#00610F#12P#Nさすがに闘い慣れている……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopEffect(0x0, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1F, 0x2)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1000)

    #C0309
    ChrTalk(
        0x105,
        (
            "#10410F#12Pくっ……やってくれたね。\x02\x03",

            "#10407F右舷前方に回り込まれた！\x01",
            "アッバス、対衝撃フィールドを！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0310
    ChrTalk(
        0x8,
        (
            "#12107F#11P──了解だ！\x02\x03",

            "総員、しゃがんで\x01",
            "衝撃に備えるがいい！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x24)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x106, 0x25)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, 5000, 0, 18000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 1)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_C690 end

    def Function_43_CBEB(): pass

    label("Function_43_CBEB")

    Sound(204, 0, 100, 0)

    label("loc_CBF1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CC0A")
    Sound(203, 0, 100, 0)
    Sleep(900)
    Jump("loc_CBF1")

    label("loc_CC0A")

    Return()

    # Function_43_CBEB end

    def Function_44_CC0B(): pass

    label("Function_44_CC0B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    LoadChrToIndex("apl/ch51217.itc", 0x20)
    LoadChrToIndex("apl/ch51218.itc", 0x21)
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    LoadChrToIndex("apl/ch51220.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51224.itc", 0x25)
    LoadChrToIndex("apl/ch51774.itc", 0x26)
    LoadEffect(0x0, "event/ev17057.eff")
    SoundLoad(498)
    SoundLoad(825)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x24)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x106, 0x25)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(370, 700, 3790, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x101, 0, 0, 32)
    BeginChrThread(0x1F, 2, 0, 33)
    Sound(498, 2, 100, 0)
    Sound(825, 2, 100, 0)
    FadeToBright(1000, 0)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 50, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x3E8)
    Sleep(1000)

    #C0311
    ChrTalk(
        0x101,
        "#00010F#12Pくっ……！\x02",
    )

    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(500)
    OP_82(0x14, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 34)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0312
    ChrTalk(
        0xF,
        "#02106F#6P#Nひゃああああっ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0313
    ChrTalk(
        0xC,
        (
            "#01911F#5P──だ、大丈夫です！\x01",
            "艦へのダメージ、軽微！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x105,
        (
            "#10407F#11Pよし、機首前面に\x01",
            "対衝撃フィールドを集中！\x02\x03",

            "機雷原を強行突破しつつ、\x01",
            "そのまま《大樹》へ向かうよ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0315
    ChrTalk(
        0x8,
        "#12107F#11P#4S了解だ！\x02",
    )

    CloseMessageWindow()
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 0, 13000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    Sound(499, 0, 100, 0)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani3")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani3")
    OP_68(370, 700, 790, 1000)
    StopSound(498, 1000, 100)
    StopSound(825, 1000, 100)
    EndChrThread(0x1F, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x24, 2)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_CC0B end

    def Function_45_D082(): pass

    label("Function_45_D082")

    OP_F4(0x5)
    Return()

    # Function_45_D082 end

    SaveToFile()

Try(main)
