from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0180.bin",                # FileName
        "c0180",                    # MapName
        "c0180",                    # Location
        0x0005,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0180",                  # 0
        "ジャネッタ",             # 1
        "ユージーン",             # 2
        "テオドール",             # 3
        "チルル",                 # 4
        "コロナ",                 # 5
        "リマ",                   # 6
        "メルスン",               # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "市民",                   # 10
        "女の子",                 # 11
        "観光客",                 # 12
        "観光客",                 # 13
        "市民",                   # 14
        "市民",                   # 15
        "観光客",                 # 16
        "観光客",                 # 17
        "市民",                   # 18
        "市民",                   # 19
        "観光客",                 # 20
        "観光客",                 # 21
        "市民",                   # 22
        "男の子",                 # 23
        "観光客",                 # 24
        "ドノバン警部",           # 25
        "市民",                   # 26
        "市民",                   # 27
        "市民",                   # 28
        "市民",                   # 29
        "リュウ",                 # 30
        "アンリ",                 # 31
        "モモ",                   # 32
        "シン",                   # 33
        "黒月",                   # 34
        "シズク",                 # 35
        "キーア",                 # 36
        "ツァイト",               # 37
        "ツァオ",                 # 38
        "レクター",               # 39
        "ザイル",                 # 40
        "アルセイユ",             # 41
        "SE制御",                 # 42
    ))

    AddCharChip((
        "chr/ch26600.itc",                   # 00
        "chr/ch28700.itc",                   # 01
        "chr/ch28800.itc",                   # 02
        "chr/ch22700.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch26200.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch33100.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch20100.itc",                   # 09
        "chr/ch22300.itc",                   # 0A
        "chr/ch22000.itc",                   # 0B
        "chr/ch34300.itc",                   # 0C
        "chr/ch24500.itc",                   # 0D
        "chr/ch22100.itc",                   # 0E
        "chr/ch33000.itc",                   # 0F
        "chr/ch33300.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch20000.itc",                   # 13
        "chr/ch20102.itc",                   # 14
        "chr/ch21102.itc",                   # 15
        "chr/ch21400.itc",                   # 16
        "chr/ch33202.itc",                   # 17
        "chr/ch48800.itc",                   # 18
        "chr/ch30300.itc",                   # 19
        "chr/ch21100.itc",                   # 1A
    ))

    DeclNpc(11409,   -189,    -6550,   180,  385,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9340,   -200,    -3940,   270,  389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-8640,   -200,    -3970,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-13640,  -200,    6610,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-5690,   -200,    3660,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6690,   -200,    3660,    0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-7690,   -200,    3660,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-14550,  -200,    -4780,   270,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-15779,  -50,     -4780,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-15779,  -50,     -4780,   90,   389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-14550,  -200,    -4780,   270,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-6719,   -200,    5000,    0,    389,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-5590,   -200,    5000,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-7000,   -200,    -4280,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-7559,   -200,    -3000,   225,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-10659,  -200,    -2779,   135,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-10979,  -200,    -3910,   90,   389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-10619,  -200,    -1070,   0,    389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-9619,   -200,    -1070,   0,    389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-6719,   -200,    5000,    0,    389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5590,   -200,    5000,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-15779,  -50,     -4780,   90,   389,  0x0, 0,   26,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-14550,  -200,    -5320,   270,  385,  0x0, 0,   22,  0,   0,   1,   0,   28,  255,  0)
    DeclNpc(-5519,   -200,    3869,    15,   389,  0x0, 0,   24,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(3809,    -200,    7099,    0,    389,  0x0, 0,   25,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1664, 0)                                       # 0

    ScpFunction((
        "Function_0_680",          # 00, 0
        "Function_1_730",          # 01, 1
        "Function_2_75B",          # 02, 2
        "Function_3_777",          # 03, 3
        "Function_4_A96",          # 04, 4
        "Function_5_D9B",          # 05, 5
        "Function_6_1210",         # 06, 6
        "Function_7_12FE",         # 07, 7
        "Function_8_1373",         # 08, 8
        "Function_9_13CD",         # 09, 9
        "Function_10_143C",        # 0A, 10
        "Function_11_1488",        # 0B, 11
        "Function_12_14EB",        # 0C, 12
        "Function_13_1C13",        # 0D, 13
        "Function_14_1C62",        # 0E, 14
        "Function_15_1CBC",        # 0F, 15
        "Function_16_1D3D",        # 10, 16
        "Function_17_1D9F",        # 11, 17
        "Function_18_1DF5",        # 12, 18
        "Function_19_1E6E",        # 13, 19
        "Function_20_1EFD",        # 14, 20
        "Function_21_1F8D",        # 15, 21
        "Function_22_2013",        # 16, 22
        "Function_23_2070",        # 17, 23
        "Function_24_20F1",        # 18, 24
        "Function_25_215E",        # 19, 25
        "Function_26_21D3",        # 1A, 26
        "Function_27_2223",        # 1B, 27
        "Function_28_267A",        # 1C, 28
        "Function_29_2A42",        # 1D, 29
        "Function_30_2B30",        # 1E, 30
        "Function_31_2BE4",        # 1F, 31
        "Function_32_2F75",        # 20, 32
        "Function_33_3019",        # 21, 33
        "Function_34_3116",        # 22, 34
        "Function_35_314E",        # 23, 35
        "Function_36_317A",        # 24, 36
        "Function_37_31B7",        # 25, 37
        "Function_38_31E8",        # 26, 38
        "Function_39_3BF0",        # 27, 39
        "Function_40_5212",        # 28, 40
        "Function_41_52E8",        # 29, 41
        "Function_42_533D",        # 2A, 42
        "Function_43_5392",        # 2B, 43
        "Function_44_53E7",        # 2C, 44
        "Function_45_543C",        # 2D, 45
        "Function_46_5486",        # 2E, 46
        "Function_47_6591",        # 2F, 47
        "Function_48_65D5",        # 30, 48
        "Function_49_6619",        # 31, 49
        "Function_50_665D",        # 32, 50
        "Function_51_66A1",        # 33, 51
        "Function_52_74C2",        # 34, 52
        "Function_53_750D",        # 35, 53
        "Function_54_7558",        # 36, 54
        "Function_55_75A3",        # 37, 55
        "Function_56_75EE",        # 38, 56
        "Function_57_7639",        # 39, 57
    ))


    def Function_0_680(): pass

    label("Function_0_680")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6B8"),
        (1, "loc_6C4"),
        (2, "loc_6D0"),
        (3, "loc_6DC"),
        (4, "loc_6E8"),
        (5, "loc_6F4"),
        (6, "loc_700"),
        (SWITCH_DEFAULT, "loc_70C"),
    )


    label("loc_6B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_700")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_70C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_72F")

    Return()

    # Function_0_680 end

    def Function_1_730(): pass

    label("Function_1_730")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75A")
    OP_94(0xFE, 0xFFFFC4AA, 0xFFFFEFCA, 0xFFFFCD24, 0xFFFFE46C, 0x3E8)
    Sleep(300)
    Jump("Function_1_730")

    label("loc_75A")

    Return()

    # Function_1_730 end

    def Function_2_75B(): pass

    label("Function_2_75B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_776")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_75B")

    label("loc_776")

    Return()

    # Function_2_75B end

    def Function_3_777(): pass

    label("Function_3_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B7")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1D, -6820, -200, -3460, 105)
    SetChrPos(0x1E, -7510, -200, -4550, 105)
    BeginChrThread(0x1E, 0, 0, 0)
    Jump("loc_9E4")

    label("loc_7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7C5")
    Jump("loc_9E4")

    label("loc_7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7EE")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_817")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_840")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_853")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9E4")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_87C")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8A5")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8D8")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_8D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8FF")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jump("loc_9E4")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_966")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9A8")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x14)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9BB")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9E4")

    label("loc_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9E4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x17)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_9F8")
    ClearScenarioFlags(0x22, 0)
    Event(0, 30)
    Jump("loc_A2F")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A0C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 31)
    Jump("loc_A2F")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_A20")
    ClearScenarioFlags(0x22, 2)
    Event(0, 38)
    Jump("loc_A2F")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_A2F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 33)

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A40")
    Event(0, 39)

    label("loc_A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6D")
    Event(0, 51)
    Jump("loc_A95")

    label("loc_A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A95")
    Event(0, 46)

    label("loc_A95")

    Return()

    # Function_3_777 end

    def Function_4_A96(): pass

    label("Function_4_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B89")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x168, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C67")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x168, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CF8")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x46, 0x1A4, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D35")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "heiyue", 0x0, 0x1)
    Jump("loc_D64")

    label("loc_D35")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "heiyue", 0x1, 0x1)

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D86")
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    Jump("loc_D9A")

    label("loc_D86")

    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)

    label("loc_D9A")

    Return()

    # Function_4_A96 end

    def Function_5_D9B(): pass

    label("Function_5_D9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_120C")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E69")

    #C0001
    ChrTalk(
        0xFE,
        (
            "はあ、あの夜のサザークさん、\x01",
            "かっこよかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "あんなに真剣な顔をして\x01",
            "『僕なら君の良さが分かる』なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "うふふ、本当に最高の時間だったなぁ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EE1")

    label("loc_E69")


    #C0004
    ChrTalk(
        0xFE,
        (
            "それにまさか、\x01",
            "アルカンシェルのチケットまで\x01",
            "プレゼントしてくれるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "うふふ、私って本当に幸せ者だなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_EE1")

    Jump("loc_120C")

    label("loc_EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EF4")
    Jump("loc_120C")

    label("loc_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1076")

    #C0006
    ChrTalk(
        0xFE,
        (
            "は～あ、私もパールさんみたいに\x01",
            "頼りがいのある素敵な彼氏が欲しいな～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0007
    ChrTalk(
        0xFE,
        (
            "あっと、いけない、いけない……\x01",
            "ちゃんとお花さんにお水をあげないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "うふふ、ごめんなちゃい。\x01",
            "今たっぷり注いであげまちゅからね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#00305F（なっ、まさかの赤ちゃん言葉たぁ……\x01",
            "　こいつはポイント高えぜっ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        "#10106F（な、何のポイントですか……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10BD")

    label("loc_1076")


    #C0011
    ChrTalk(
        0xFE,
        (
            "うふふ、ごめんなちゃいね。\x01",
            "今たっぷりと注いであげまちゅからね～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BD")

    Jump("loc_120C")

    label("loc_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10D0")
    Jump("loc_120C")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_120C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1192")

    #C0012
    ChrTalk(
        0xFE,
        (
            "ふう、ここは\x01",
            "見晴らしがよくて素敵ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "あ、ちなみに私、\x01",
            "さぼってるワケじゃないですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "支配人から植え込みの\x01",
            "水遣り係に任命されたんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_120C")

    label("loc_1192")


    #C0015
    ChrTalk(
        0xFE,
        (
            "うふふ、今お水をあげまちゅからね。\x01",
            "一杯飲んで元気に育つんでちゅよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00006F（な、なんで赤ちゃん言葉なんだ？）\x02",
    )

    CloseMessageWindow()

    label("loc_120C")

    TalkEnd(0xFE)
    Return()

    # Function_5_D9B end

    def Function_6_1210(): pass

    label("Function_6_1210")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A1")

    #C0017
    ChrTalk(
        0xFE,
        (
            "最近、旅から帰ってくる毎に\x01",
            "段々完成に近づいていたビル……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "シートの下はあんなのだったんだ。\x01",
            "けっこうすごいかも……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12FA")

    label("loc_12A1")


    #C0019
    ChrTalk(
        0xFE,
        (
            "さて、ビルは見れたし……\x01",
            "そろそろ次の場所に行こうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "家には……今度帰ろう。\x02",
    )

    CloseMessageWindow()

    label("loc_12FA")

    TalkEnd(0xFE)
    Return()

    # Function_6_1210 end

    def Function_7_12FE(): pass

    label("Function_7_12FE")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "いや～、やっぱ俺たちって\x01",
            "オーラが出てんだな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "すまん、テオドール。\x01",
            "こればっかりは俺の計算ミスだ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_12FE end

    def Function_8_1373(): pass

    label("Function_8_1373")

    TalkBegin(0xFE)

    #C0023
    ChrTalk(
        0xFE,
        (
            "……くっ、何が\x01",
            "『練習着姿ならバレない』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "お前を信じた俺がバカだった。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1373 end

    def Function_9_13CD(): pass

    label("Function_9_13CD")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        (
            "あんな立派な建物の建設に\x01",
            "主人が関わったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ふふ、こんなに誇らしいことは\x01",
            "ありませんね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_13CD end

    def Function_10_143C(): pass

    label("Function_10_143C")

    TalkBegin(0xFE)

    #C0027
    ChrTalk(
        0xFE,
        "ふわ～、そーなんだー！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "えへへ、やっぱり\x01",
            "パパはすごいなー♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_143C end

    def Function_11_1488(): pass

    label("Function_11_1488")

    TalkBegin(0xFE)

    #C0029
    ChrTalk(
        0xFE,
        "ほらリマ、見てごらん。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "あのビルはね、\x01",
            "パパが仲間たちと力を\x01",
            "合わせて造ったんだよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1488 end

    def Function_12_14EB(): pass

    label("Function_12_14EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160C")

    #C0031
    ChrTalk(
        0xFE,
        "両国の首脳を狙うテロリストか……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "この情報ばかりに\x01",
            "囚われるわけにもいかねえが、\x01",
            "良い心構えにはなったのは確かだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "ともかく、警備シフトについては\x01",
            "昨日の内にダドリーが\x01",
            "調整したものに従うまで……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "あとは各人、\x01",
            "せいぜい気合いを入れるだけだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1693")

    label("loc_160C")


    #C0035
    ChrTalk(
        0xFE,
        (
            "ともかく、警備シフトについては\x01",
            "昨日の内にダドリーが\x01",
            "調整したものに従うまで……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "あとは各人、\x01",
            "せいぜい気合いを入れるだけだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1693")

    Jump("loc_1C0F")

    label("loc_1698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1975")

    #C0037
    ChrTalk(
        0xFE,
        (
            "よう、お前たち。\x01",
            "何でも除幕式の警備に\x01",
            "参加したそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "間近で見る首脳たちはどうだった？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00000Fええ、本当に凄い迫力でした。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00304Fああ、なんつうか\x01",
            "マジでオーラってモンが\x01",
            "見えた気がしたよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "なるほど、しっかり\x01",
            "感じ取ってんじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "まあ、なんつうか、\x01",
            "そういった雰囲気を感じる事も\x01",
            "もちろん大事なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "実際に傍で触れた時なんかに\x01",
            "呑まれねえ事も大事だからな？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#00100Fええ、確かにそうですね。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        (
            "#10106Fちょ、ちょっと\x01",
            "自信はないですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "はは、まあその辺は経験も\x01",
            "重要になってくるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "ま、ともかくお前らには\x01",
            "良い体験だったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "警備に押し込んでくれた\x01",
            "セルゲイの野郎には、\x01",
            "ちゃんと感謝しておけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00000Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 3)
    Jump("loc_1A27")

    label("loc_1975")


    #C0050
    ChrTalk(
        0xFE,
        (
            "お前たちが感じたように、\x01",
            "首脳たちのオーラってのは\x01",
            "それぞれ独特で本物だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "ま、とにかく俺が言いたいのは、\x01",
            "そんなお偉方を相手にするときゃ\x01",
            "呑まれねえ事も大事だってこった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A27")

    Jump("loc_1C0F")

    label("loc_1A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B87")

    #C0052
    ChrTalk(
        0xFE,
        (
            "よう、お前らか。\x01",
            "何か変わったことはあったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、まあ\x01",
            "大きな変事はないですね。\x02\x03",

            "警部はこちらで警戒の指揮を？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "ああ、各方面と連絡を取るには\x01",
            "この場所が色々と都合がよくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ま、とりあえず今んトコ\x01",
            "こっちも別段変わりはねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "お前たちは遊軍の活動を続けてくれ。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00100Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C0F")

    label("loc_1B87")


    #C0058
    ChrTalk(
        0xFE,
        (
            "しかしまあ、各所の人出も\x01",
            "記念祭ほどじゃなくて助かるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "もっとも明日は、除幕式があるから\x01",
            "今日のようにはいかないだろうがなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0F")

    TalkEnd(0xFE)
    Return()

    # Function_12_14EB end

    def Function_13_1C13(): pass

    label("Function_13_1C13")

    TalkBegin(0xFE)

    #C0060
    ChrTalk(
        0xFE,
        (
            "百貨店の屋上かぁ、\x01",
            "まさかこんな良いスポットが\x01",
            "出来ていたなんてね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1C13 end

    def Function_14_1C62(): pass

    label("Function_14_1C62")

    TalkBegin(0xFE)

    #C0061
    ChrTalk(
        0xFE,
        "ふう、風が気持ちいいわ。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "見晴らしもいいし、\x01",
            "ここはとっても素敵な場所ね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1C62 end

    def Function_15_1CBC(): pass

    label("Function_15_1CBC")

    TalkBegin(0xFE)

    #C0063
    ChrTalk(
        0xFE,
        (
            "そういえばウチの子、\x01",
            "街の外をほとんど知らないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "ふふ、今度アルモリカ村にでも\x01",
            "連れて行ってあげようかしら。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1CBC end

    def Function_16_1D3D(): pass

    label("Function_16_1D3D")

    TalkBegin(0xFE)

    #C0065
    ChrTalk(
        0xFE,
        (
            "ふわー、とおくの方に\x01",
            "みどり色がたくさんあるのっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "あそこもクロスベルなのかなぁ？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1D3D end

    def Function_17_1D9F(): pass

    label("Function_17_1D9F")

    TalkBegin(0xFE)

    #C0067
    ChrTalk(
        0xFE,
        (
            "あの中、ほんと一体\x01",
            "どうなってんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "除幕式が楽しみすぎるぜ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1D9F end

    def Function_18_1DF5(): pass

    label("Function_18_1DF5")

    TalkBegin(0xFE)

    #C0069
    ChrTalk(
        0xFE,
        (
            "でも、あの覆いって\x01",
            "どうやって取り外すのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "まさか、みんなで下から\x01",
            "引っ張るわけじゃないだろうし……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1DF5 end

    def Function_19_1E6E(): pass

    label("Function_19_1E6E")

    TalkBegin(0xFE)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0071
    ChrTalk(
        0xFE,
        "#4Sキャーーーーッ！#3S\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "まさかこんな所でお２人に\x01",
            "お会いできるなんてっっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "あ、あの、サイン下さいっ！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1E6E end

    def Function_20_1EFD(): pass

    label("Function_20_1EFD")

    TalkBegin(0xFE)
    TurnDirection(0x16, 0x15, 0)

    #C0074
    ChrTalk(
        0xFE,
        (
            "ちょ、ちょっとアンタ。\x01",
            "そんなにうるさくしたら\x01",
            "ご迷惑でしょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "それにサインをもらうのは、\x01",
            "わたしが先なんだからっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_1EFD end

    def Function_21_1F8D(): pass

    label("Function_21_1F8D")

    TalkBegin(0xFE)

    #C0076
    ChrTalk(
        0xFE,
        (
            "ふむ、２人とも舞台で見るより\x01",
            "ずっと男前でたくましいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "ちょっぴり悔しいが、\x01",
            "妻が惚れてしまうのも\x01",
            "分かる気がするぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1F8D end

    def Function_22_2013(): pass

    label("Function_22_2013")

    TalkBegin(0xFE)

    #C0078
    ChrTalk(
        0xFE,
        (
            "ああ、実物のテオドール様と\x01",
            "ユージーン様が目の前に……\x01",
            "気絶してしまいそうですわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2013 end

    def Function_23_2070(): pass

    label("Function_23_2070")

    TalkBegin(0xFE)

    #C0079
    ChrTalk(
        0xFE,
        (
            "何でも、まさにこれから\x01",
            "会議の本番が始まるんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "難しいことは分からないが、\x01",
            "市長たちには頑張って欲しいぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2070 end

    def Function_24_20F1(): pass

    label("Function_24_20F1")

    TalkBegin(0xFE)

    #C0081
    ChrTalk(
        0xFE,
        (
            "ここから声援を送ったら、\x01",
            "市長さんたちに届かないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "フレーフレー、市長！\x01",
            "……なんてね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_20F1 end

    def Function_25_215E(): pass

    label("Function_25_215E")

    TalkBegin(0xFE)

    #C0083
    ChrTalk(
        0xFE,
        (
            "はぁ、何度見ても\x01",
            "たまげたビルじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "クロスベルの新たなランドマークとは\x01",
            "よく言ったもんじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_215E end

    def Function_26_21D3(): pass

    label("Function_26_21D3")

    TalkBegin(0xFE)

    #C0085
    ChrTalk(
        0xFE,
        (
            "ふふ、あのビルの屋上から眺める\x01",
            "景色はさぞ素晴らしいんでしょうねぇ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_21D3 end

    def Function_27_2223(): pass

    label("Function_27_2223")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_226D")

    #C0086
    ChrTalk(
        0xFE,
        (
            "あの大きな樹……\x01",
            "青白い光が幻想的な感じもするわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_227B")
    Jump("loc_2676")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_232C")

    #C0087
    ChrTalk(
        0xFE,
        (
            "ディーター大統領とアリオス国防長官、\x01",
            "この２人になら安心して\x01",
            "クロスベルを任せられるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "長い戦いになるかもしれないけど、\x01",
            "ぜひとも独立を勝ち取らなきゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_232C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23CB")

    #C0089
    ChrTalk(
        0xFE,
        (
            "アリオスさんは、\x01",
            "オルキスタワーを守るために\x01",
            "本当に見事な活躍をされたそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "改めて感じたけどこの街は\x01",
            "やっぱりあの人がいてこそ、よね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_23CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2483")

    #C0091
    ChrTalk(
        0xFE,
        (
            "武装集団は突然現れたそうだけど……\x01",
            "どうにかして未然に防ぐことは\x01",
            "できなかったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "警察と警備隊には\x01",
            "もっとしっかりしてもらわないと\x01",
            "安心して夜も眠れないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_2483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2491")
    Jump("loc_2676")

    label("loc_2491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2505")

    #C0093
    ChrTalk(
        0xFE,
        (
            "街道方面で何か事故が\x01",
            "あったみたいだけど心配ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "救急車も結構な台数が\x01",
            "出ていたみたいだし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_2505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_259E")

    #C0095
    ChrTalk(
        0xFE,
        (
            "ここで休むようになってから\x01",
            "何だか百貨店に長居するように\x01",
            "なっちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "ここで風に当たっていると、\x01",
            "買い物疲れも吹き飛ぶのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2676")

    #C0097
    ChrTalk(
        0xFE,
        (
            "ふふ、何だかオルキスタワーの見える\x01",
            "景色にもすっかり慣れた気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "この先１０年２０年経てば、\x01",
            "街並みも変わって行くんだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "あのビルの存在感だけは、\x01",
            "そのまま変わらないんだろうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2676")

    TalkEnd(0xFE)
    Return()

    # Function_27_2223 end

    def Function_28_267A(): pass

    label("Function_28_267A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26D5")

    #C0100
    ChrTalk(
        0xFE,
        (
            "なんで、あんな\x01",
            "でっかい木が浮いてんだ？\x01",
            "よのなかってナゾだらけだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_26D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_26E3")
    Jump("loc_2A3E")

    label("loc_26E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2765")

    #C0101
    ChrTalk(
        0xFE,
        (
            "アリオスさん、ゆーげきしから\x01",
            "ちょーかんになったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "よく分かんねーけど、\x01",
            "たぶんこれでムテキだなっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_2765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27CC")

    #C0103
    ChrTalk(
        0xFE,
        (
            "オレはアリオス・マクレイン……\x01",
            "ゆーげきしだぜッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "シャキーン、スパパパパパッ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_27CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2837")

    #C0105
    ChrTalk(
        0xFE,
        (
            "なんか、マインツの方が\x01",
            "スゲー大変なんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "はやく悪いヤツ、つかまんねーかな？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_2837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2845")
    Jump("loc_2A3E")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2905")

    #C0107
    ChrTalk(
        0xFE,
        (
            "きゅーきゅー車ってのが\x01",
            "通って行った時に、\x01",
            "音がヘンな風に聞こえたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "ピーポーピーポーが、\x01",
            "プーポープーポーって感じでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "アレ、一体なんだったんだ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2971")

    label("loc_2905")


    #C0110
    ChrTalk(
        0xFE,
        (
            "きゅーきゅー車ってのが\x01",
            "通って行った時に、\x01",
            "音がヘンな風に聞こえたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "アレ、一体なんだったんだ？\x02",
    )

    CloseMessageWindow()

    label("loc_2971")

    Jump("loc_2A3E")

    label("loc_2976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29F8")

    #C0112
    ChrTalk(
        0xFE,
        (
            "おくじょーはオレも好きだけど、\x01",
            "なんもねーのがナヤミだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "なんか食い物屋でも、\x01",
            "作ってくれねーモンかなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_29F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A3E")

    #C0114
    ChrTalk(
        0xFE,
        (
            "へへ、今日もいい天気だな。\x01",
            "おくじょーの空気がうまいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3E")

    TalkEnd(0xFE)
    Return()

    # Function_28_267A end

    def Function_29_2A42(): pass

    label("Function_29_2A42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AAB")

    #N0115
    NpcTalk(
        0xFE,
        "娘",
        "今日の雨は午後には晴れるそうよ。\x02",
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0xFE,
        "娘",
        "ふふ、虹でも見られるかもしれないわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2C")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B2C")

    #N0117
    NpcTalk(
        0xFE,
        "市民",
        (
            "ふふ、雨の街ってどうして\x01",
            "こんなに心をくすぐるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #N0118
    NpcTalk(
        0xFE,
        "市民",
        (
            "哀愁ある雰囲気が\x01",
            "何とも情緒的で堪らないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2C")

    TalkEnd(0xFE)
    Return()

    # Function_29_2A42 end

    def Function_30_2B30(): pass

    label("Function_30_2B30")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(9900, 2800, 25300, 0)
    MoveCamera(30, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(23750, 0)
    OP_68(5550, 4800, 33000, 10000)
    MoveCamera(10, -5, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(21000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_2B30 end

    def Function_31_2BE4(): pass

    label("Function_31_2BE4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch20600.itc", 0x21)
    LoadChrToIndex("chr/ch22200.itc", 0x22)
    LoadChrToIndex("chr/ch45000.itc", 0x23)
    LoadChrToIndex("chr/ch47600.itc", 0x24)
    SoundLoad(835)
    SoundLoad(821)
    SetChrChipByIndex(0x2B, 0x1E)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2C, 0x20)
    SetChrSubChip(0x2C, 0x5)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x22)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrChipByIndex(0x29, 0x24)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x23, 0x7)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x21, 0x8)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x24, 0xB)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0x19, 0xFF)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    BeginChrThread(0x2C, 3, 0, 0)
    SetChrPos(0x2B, -12800, -200, 6900, 225)
    SetChrPos(0x2A, -14000, -200, 6500, 135)
    SetChrPos(0x2C, -13000, -200, 4800, 0)
    SetChrPos(0x25, -10700, -200, 7100, 135)
    SetChrPos(0x26, -9500, -200, 7100, 225)
    SetChrPos(0x27, -10200, -200, 5900, 0)
    SetChrPos(0x28, -11900, -200, 4900, 135)
    SetChrPos(0x29, -11200, -200, 4100, 315)
    SetChrPos(0x23, -7200, -200, 4800, 0)
    SetChrPos(0x21, -5100, -200, 5600, 0)
    SetChrPos(0x24, -5000, -200, 4100, 0)
    SetChrPos(0x22, -3200, -200, 5000, 0)
    SetChrPos(0x8, -1800, -200, 4500, 0)
    SetChrPos(0xB, -5400, -200, 6800, 0)
    SetChrPos(0x19, -3000, -200, 6900, 0)
    SetChrPos(0x11, -8400, -200, 4900, 0)
    OP_68(-8000, 4800, 5500, 0)
    MoveCamera(12, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12500, 0)
    OP_68(-8000, 2500, 5500, 10000)
    MoveCamera(12, 5, 0, 10000)
    SetCameraDistance(12000, 10000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x2B, 3, 0, 32)
    BeginChrThread(0x2A, 3, 0, 32)
    BeginChrThread(0x25, 3, 0, 32)
    BeginChrThread(0x26, 3, 0, 32)
    BeginChrThread(0x27, 3, 0, 32)
    BeginChrThread(0x28, 3, 0, 32)
    BeginChrThread(0x23, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0x21, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x24, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0x22, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x8, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 35)
    Sleep(8000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_2BE4 end

    def Function_32_2F75(): pass

    label("Function_32_2F75")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2FAD"),
        (1, "loc_2FB5"),
        (2, "loc_2FBD"),
        (3, "loc_2FC5"),
        (4, "loc_2FCD"),
        (5, "loc_2FD5"),
        (6, "loc_2FDD"),
        (SWITCH_DEFAULT, "loc_2FE5"),
    )


    label("loc_2FAD")

    Sleep(200)
    Jump("loc_2FED")

    label("loc_2FB5")

    Sleep(400)
    Jump("loc_2FED")

    label("loc_2FBD")

    Sleep(600)
    Jump("loc_2FED")

    label("loc_2FC5")

    Sleep(800)
    Jump("loc_2FED")

    label("loc_2FCD")

    Sleep(1000)
    Jump("loc_2FED")

    label("loc_2FD5")

    Sleep(1200)
    Jump("loc_2FED")

    label("loc_2FDD")

    Sleep(1400)
    Jump("loc_2FED")

    label("loc_2FE5")

    Sleep(1600)
    Jump("loc_2FED")

    label("loc_2FED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3018")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("loc_2FED")

    label("loc_3018")

    Return()

    # Function_32_2F75 end

    def Function_33_3019(): pass

    label("Function_33_3019")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(496)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x2, 0x30)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_FF(0x2, 0x15E, 0x15E, 0x15E)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x30, -30000, 10000, 50000, 135)
    OP_D5(0x30, 0x0, 0x20F58, 0x0, 0x0)
    BeginChrThread(0x30, 1, 0, 34)
    BeginChrThread(0x31, 1, 0, 37)
    OP_68(7750, 5200, 37650, 0)
    MoveCamera(30, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(29000, 0)
    MoveCamera(45, -10, 0, 8000)
    SetCameraDistance(42500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    StopSound(496, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_3019 end

    def Function_34_3116(): pass

    label("Function_34_3116")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -30000, 10000, 60000)
    OP_9F(0x1, 5000, 10000, 50000)
    OP_9F(0x1, 20000, 12000, 0)
    OP_9F(0x2, 0xFE, 14000, 0x7)
    Return()

    # Function_34_3116 end

    def Function_35_314E(): pass

    label("Function_35_314E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3179")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("Function_35_314E")

    label("loc_3179")

    Return()

    # Function_35_314E end

    def Function_36_317A(): pass

    label("Function_36_317A")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Return()

    # Function_36_317A end

    def Function_37_31B7(): pass

    label("Function_37_31B7")

    Sound(496, 2, 20, 0)
    Sleep(300)
    OP_25(0x1F0, 0x1E)
    Sleep(300)
    OP_25(0x1F0, 0x28)
    Sleep(300)
    OP_25(0x1F0, 0x32)
    Sleep(300)
    OP_25(0x1F0, 0x3C)
    Sleep(300)
    OP_25(0x1F0, 0x46)
    Sleep(300)
    OP_25(0x1F0, 0x50)
    Return()

    # Function_37_31B7 end

    def Function_38_31E8(): pass

    label("Function_38_31E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch20600.itc", 0x21)
    LoadChrToIndex("chr/ch22200.itc", 0x22)
    LoadChrToIndex("chr/ch45000.itc", 0x23)
    LoadChrToIndex("chr/ch47600.itc", 0x24)
    SoundLoad(851)
    SoundLoad(3603)
    SoundLoad(3604)
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2B, 0x1E)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, -12800, -200, 6900, 0)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -14000, -200, 6500, 0)
    SetChrChipByIndex(0x2C, 0x20)
    SetChrSubChip(0x2C, 0x5)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -13000, -200, 4800, 0)
    BeginChrThread(0x2C, 3, 0, 0)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -10700, -200, 7100, 0)
    SetChrChipByIndex(0x26, 0x22)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -9700, -200, 7100, 0)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -9900, -200, 5900, 0)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, -11400, -200, 4900, 0)
    SetChrChipByIndex(0x29, 0x24)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -10900, -200, 4100, 0)
    SetChrChipByIndex(0x23, 0x7)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7200, -200, 4800, 0)
    SetChrChipByIndex(0x21, 0x8)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -5100, -200, 5600, 0)
    SetChrChipByIndex(0x24, 0xB)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -4800, -200, 4100, 0)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -3200, -200, 5000, 0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1800, -200, 4500, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6400, -200, 6800, 0)
    OP_4B(0x19, 0xFF)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -3000, -200, 6900, 0)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -8900, -200, 4900, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    VolumeBGM(0x5A, 0x3E8)
    OP_68(-7000, 4100, 10500, 0)
    MoveCamera(37, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    Sound(851, 2, 100, 0)
    OP_68(-7000, 1100, 10500, 5000)
    MoveCamera(37, 11, 0, 5000)
    FadeToBright(2000, 0)
    BeginChrThread(0x23, 3, 0, 35)
    BeginChrThread(0xB, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x21, 3, 0, 35)
    BeginChrThread(0x19, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x24, 3, 0, 35)
    BeginChrThread(0x22, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x8, 3, 0, 35)
    BeginChrThread(0x11, 3, 0, 35)
    OP_0D()
    OP_6F(0x79)

    #C0119
    ChrTalk(
        0x21,
        "#11Pす、すごいわ……！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x23,
        (
            "#11Pあのビル、ＩＢＣのテコ入れで\x01",
            "やっと完成したんだっけ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x22,
        (
            "#11Pまさかあんな綺麗なビルが\x01",
            "建てられていたなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x24,
        (
            "#11Pやっぱディーター市長は\x01",
            "やる事がデカすぎるぜ！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-10000, 700, 7000, 0)
    MoveCamera(37, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    OP_6F(0x79)
    BeginChrThread(0x25, 3, 0, 36)
    OP_63(0x25, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0123
    ChrTalk(
        0x25,
        "#11P#4Sす、すっげ───ッ！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x25, 3)
    TurnDirection(0x25, 0x26, 500)

    #C0124
    ChrTalk(
        0x25,
        (
            "#6Pなあなあアンリ！\x01",
            "探検に行ってみようぜ、探検！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x25, 500)

    #C0125
    ChrTalk(
        0x26,
        "#11Pま、また怒られるってば～！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x26,
        (
            "#11Pまあ……\x01",
            "気持ちは判らなくもないけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3738():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_3738)
    Sleep(50)

    def lambda_3748():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_3748)

    #C0127
    ChrTalk(
        0x27,
        "#11P……ス、スゴイの……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3804")

    #C0128
    ChrTalk(
        0x28,
        (
            "#12Pた、確かに凄いビルだな……\x01",
            "カルバードじゃ考えられないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x28,
        (
            "#12Pうーん、ウチがこの街に\x01",
            "こだわるのもわかる気がする……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3894")

    label("loc_3804")


    #N0130
    NpcTalk(
        0x28,
        "男の子",
        (
            "#12Pた、確かに凄いビルだな……\x01",
            "カルバードじゃ考えられないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #N0131
    NpcTalk(
        0x28,
        "男の子",
        (
            "#12Pうーん、ウチがこの街に\x01",
            "こだわるのもわかる気がする……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3894")

    OP_68(-13300, 700, 7000, 2000)
    OP_6F(0x79)

    #C0132
    ChrTalk(
        0x2A,
        (
            "#12P#06000Fふふっ……\x01",
            "みんな、すごく盛り上がってるね。\x02\x03",

            "#06002Fねえねえ、キーアちゃん。\x01",
            "そんなにおっきなビルなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x2B,
        "#11P#01105F#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(150)

    #C0134
    ChrTalk(
        0x2A,
        (
            "#5P#06005Fキーアちゃん……？\x01",
            "そこにいるよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x2B, 0x2A, 500)

    #C0135
    ChrTalk(
        0x2B,
        (
            "#11P#01109Fあっ──ゴメンね、シズク。\x02\x03",

            "#01110Fえっとね、すっごく大きいよ！\x02\x03",

            "色も青と白でキレーで、\x01",
            "スラっとしててカッコよくて！\x02\x03",

            "#01108F#30W……でも………\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x2A,
        "#5P#06008F？　どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x2B,
        (
            "#11P#01102Fあ……\x01",
            "ううん、なんでもないっ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10460, 6100, 24340, 4000)
    MoveCamera(17, -5, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(15820, 4000)
    OP_93(0x2B, 0x0, 0x12C)
    OP_6F(0x79)
    SetChrFlags(0x2B, 0x4)
    SetChrPos(0x2B, -15500, 1200, -2900, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0138
    ChrTalk(
        0x2B,
        (
            "#01106F#3603V#40W#12P#N（なんでだろ……\x01",
            "  はじめて見るはずなのに……）\x02\x03",

            "#01112F#3604V#30W（キーア、あのビル……\x01",
            "  どこかで見たことある気がする。）\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE14)
    OP_C9(0x1, 0x80000000)
    StopSound(851, 2000, 100)
    SetCameraDistance(15320, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x64, 0x64)
    Sleep(100)
    OP_24(0x353)
    Sleep(1000)
    SetScenarioFlags(0x22, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_31E8 end

    def Function_39_3BF0(): pass

    label("Function_39_3BF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("apl/ch50237.itc", 0x1F)
    SetChrPos(0x101, 12000, 0, 1000, 180)
    SetChrPos(0x102, 12000, 0, 1000, 180)
    SetChrPos(0x103, 12000, 0, 1000, 180)
    SetChrPos(0x109, 12000, 0, 1000, 180)
    SetChrPos(0x105, 12000, 0, 1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2D, 0x1E)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, -12000, -200, 6900, 0)
    OP_68(11250, 1000, -2300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetCameraDistance(14500, 4000)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 42)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 43)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 44)
    WaitChrThread(0x105, 3)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(-12000, 1000, 6900, 3000)
    MoveCamera(33, 16, 0, 3000)
    SetCameraDistance(12500, 3000)
    OP_6F(0x79)
    Sleep(300)

    #C0139
    ChrTalk(
        0x2D,
        (
            "#03204F#11Pフフ……\x01",
            "急いで来て頂いたようで\x01",
            "何よりです。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-12000, 900, 5400, 3000)
    MoveCamera(37, 19, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(14000, 3000)
    SetChrPos(0x101, -4000, -200, -1000, 270)
    SetChrPos(0x102, -4000, -200, -1000, 270)
    SetChrPos(0x103, -4000, -200, -1500, 270)
    SetChrPos(0x109, -4000, -200, -1000, 270)
    SetChrPos(0x105, -4000, -200, -1500, 270)

    def lambda_3E7E():
        OP_95(0xFE, -12600, -200, 3900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E7E)
    Sleep(300)

    def lambda_3E9B():
        OP_95(0xFE, -12200, -200, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E9B)
    Sleep(600)

    def lambda_3EB8():
        OP_95(0xFE, -11500, -200, 3700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EB8)
    Sleep(600)

    def lambda_3ED5():
        OP_95(0xFE, -10200, -200, 3800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3ED5)
    Sleep(300)

    def lambda_3EF2():
        OP_95(0xFE, -10200, -200, 2800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3EF2)
    WaitChrThread(0x101, 1)

    def lambda_3F10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F10)
    WaitChrThread(0x103, 1)

    def lambda_3F21():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3F21)
    WaitChrThread(0x102, 1)

    def lambda_3F32():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F32)
    WaitChrThread(0x109, 1)

    def lambda_3F43():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3F43)
    WaitChrThread(0x105, 1)

    def lambda_3F54():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3F54)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0140
    ChrTalk(
        0x101,
        (
            "#12P#00001Fツァオさん……\x01",
            "一人で大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#00105F#12Pラウさんでしたか。\x01",
            "いつもいる護衛の方は？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    OP_93(0x2D, 0xB4, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0142
    AnonymousTalk(
        0x2D,
        (
            "フフ、少々忙しくなったので\x01",
            "色々と手配してもらっています。\x02\x03",

            "それにあの物騒な方々が\x01",
            "街から居なくなりましたからね。\x02\x03",

            "こうして私も大手を振って\x01",
            "青空の下を歩けるという訳です。\x02",
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

    #C0143
    ChrTalk(
        0x103,
        (
            "#12P#00211F……相変わらず\x01",
            "うさんくさいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#12P#10302F《黒月》きっての若手幹部に\x01",
            "青空は似合わないと思うけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x2D,
        (
            "#5P#03209Fハハ、それは確かに。\x02\x03",

            "#03200F──お互い時間もない事ですし、\x01",
            "本題に入らせていただきます。\x02\x03",

            "#03206F実は昨夜、《銀#2Rイン#》殿から\x01",
            "突然連絡がありましてね。\x02\x03",

            "黒月#4Rわれわれ#との長期契約を\x01",
            "打ち切ると伝えてきたのですよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0146
    ChrTalk(
        0x109,
        "#10108Fあ……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#00108F#12Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x2D,
        (
            "#5P#03201Fいや、さすがに驚きましてね。\x02\x03",

            "何とか引き止めようとしたんですが\x01",
            "相当、頑#2Rかたく#なな様子で……\x02\x03",

            "#03206Fほとほと困り果てていたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#12P#00003F……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#12P#00200Fそれがわたしたちに\x01",
            "何の関係が……？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x2D,
        (
            "#5P#03202F──昨日、エルム湖南岸で\x01",
            "いったい何があったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x109,
        "#10101Fひょっとして……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#12P#10301F僕たちが一緒だったのは\x01",
            "既に掴んでいるみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x2D,
        (
            "#5P#03204Fええ、そして遊撃士協会と\x01",
            "《蛇》の者たちが\x01",
            "現れたという事くらいまでは。\x02\x03",

            "#03201Fいったい《銀》殿に\x01",
            "何が起きたというのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#12P#00008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#00103F#12P……貴方に話す義理は\x01",
            "無いと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x2D,
        (
            "#5P#03202Fという事は、やはり彼女に\x01",
            "何かがあったのですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        "#00110F#12P……っ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0159
    ChrTalk(
        0x101,
        (
            "#6P#00006F……ダメだ、エリィ。\x01",
            "尋常な相手じゃない。\x02\x03",

            "#00011F下手に喋ると情報を──あ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x105,
        (
            "#12P#10306Fやれやれ。\x01",
            "なかなか悪辣#4Rあくらつ#だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x2D,
        (
            "#5P#03209Fフフ、やはり\x01",
            "《銀》殿は女性でしたか。\x02\x03",

            "#03210F恐らく超人的な内功で\x01",
            "気と体型を変化させていたと\x01",
            "いったところでしょうか？\x02\x03",

            "#03204Fそれだけの身体能力があれば\x01",
            "ステージでの活躍も納得ですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2D, 500)

    #C0162
    ChrTalk(
        0x101,
        "#12P#00010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        "#12P#00201F……………………………\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x2D,
        (
            "#5P#03204Fいや、どうも気になったので\x01",
            "前にアルカンシェル関係者の\x01",
            "スケジュールを調べたんですよ。\x02\x03",

            "#03210Fすると《銀》殿が\x01",
            "こちらの仕事を断るタイミングが\x01",
            "公演の日などと一致しまして。\x02\x03",

            "いやはや、皆さんのおかげで\x01",
            "ようやく確信が持てました。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#12P#00006F……………………………\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#00101F#12P……“彼女”を\x01",
            "どうするつもりなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x2D,
        (
            "#5P#03205F──今のところ、特には。\x02\x03",

            "#03209Fまあ、正体を知ったのが\x01",
            "私だけなら、脅しという手も\x01",
            "考えられたんですが……\x02\x03",

            "#03202Fギルド関係者もいた以上、\x01",
            "ここで皆さんの口を封じるわけにも\x01",
            "いきませんし。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0168
    ChrTalk(
        0x109,
        "#10110F……！\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        "#12P#10306F冗談キツイねぇ……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#12P#00003F……話がそれだけなら\x01",
            "急いでいるので失礼しますよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x2D,
        (
            "#5P#03204Fフフ、まあそう言わずに。\x02\x03",

            "#03210F──今の情報のお礼に\x01",
            "耳寄りな話を提供しましょう。\x02\x03",

            "ランディさんですが……\x01",
            "３時間ほど前、マインツ山道の\x01",
            "とある地点を訪れたそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0172
    ChrTalk(
        0x101,
        "#12P#00011F#4S！？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#12P#00205Fほ、本当ですか……？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x2D,
        (
            "#5P#03204F《赤い星座》の動向については\x01",
            "専門の監視班を持っていましてね。\x02\x03",

            "#03200Fその監視班からの連絡です。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x105,
        "#12P#10301Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        "#00107F#12Pそれで、その地点というのは？\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x2D,
        (
            "#5P#03203F現在、クロスベル警備隊が\x01",
            "防衛線を敷いている滝の手前……\x02\x03",

            "#03201Fその付近にある高台から\x01",
            "ザイルで崖下に降りたとの事です。\x02\x03",

            "その先は、気付かれそうだったので\x01",
            "追跡を諦めたそうですが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0178
    ChrTalk(
        0x102,
        "#00101F#11Pロイド……！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#12P#00004Fああ、この上もない情報だ。\x02\x03",

            "#00000F──ツァオさん。\x01",
            "情報感謝します……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E45():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E45)

    #C0180
    ChrTalk(
        0x2D,
        (
            "#5P#03200Fフフ、あなた方が頑張れば\x01",
            "こちらの利にもなりますし。\x02\x03",

            "#03204Fまあ、ランディさん共々\x01",
            "死なないように気を付けて下さい。\x02\x03",

            "#03210F──強いですよ、“彼ら”は。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#12P#00003F……分かりました。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x258)
    Sleep(150)

    #C0182
    ChrTalk(
        0x101,
        (
            "#5P#00007Fよし、エニグマで課長に連絡して\x01",
            "すぐにマインツ山道へ出よう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F72():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4F72)
    Sleep(50)

    def lambda_4F82():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4F82)
    Sleep(50)

    def lambda_4F92():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4F92)
    Sleep(50)

    def lambda_4FA2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4FA2)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0183
    ChrTalk(
        0x103,
        "#12P#00201Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x109,
        "#10107F了解です！\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#00107F#11P何とか追いつかないと……！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_5024():

        label("loc_5024")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5024")

    QueueWorkItem2(0x2D, 2, lambda_5024)
    OP_68(-7000, 900, 3400, 4000)
    SetCameraDistance(15500, 4000)
    BeginChrThread(0x105, 3, 0, 45)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 45)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 45)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 45)
    Sleep(4000)
    EndChrThread(0x2D, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-12000, 1000, 6900, 0)
    MoveCamera(33, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_63(0x2D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x2D)
    OP_93(0x2D, 0xB4, 0x1F4)
    Sleep(150)
    SetChrChipByIndex(0x2D, 0x1F)
    SetChrSubChip(0x2D, 0x0)
    Sleep(90)
    SetChrSubChip(0x2D, 0x1)
    Sleep(90)
    SetChrSubChip(0x2D, 0x2)
    Sleep(90)
    Sound(318, 0, 60, 0)
    SetChrSubChip(0x2D, 0x3)
    Sleep(200)

    #C0186
    ChrTalk(
        0x2D,
        (
            "#03204F#5Pハハ……あんな青臭さも\x01",
            "たまには悪くはありませんね。\x02\x03",

            "#03200Fさてと──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2D, 0x2)
    Sleep(90)
    SetChrSubChip(0x2D, 0x1)
    Sleep(90)
    SetChrSubChip(0x2D, 0x0)
    Sleep(90)
    SetChrChipByIndex(0x2D, 0x1E)
    SetChrSubChip(0x2D, 0x0)
    Sleep(200)
    SetCameraDistance(12000, 1000)
    OP_93(0x2D, 0x0, 0x15E)
    OP_6F(0x79)

    #C0187
    ChrTalk(
        0x2D,
        (
            "#03203F#11Pここが正念場ですか。\x02\x03",

            "#03202F──どうやらこちらも\x01",
            "全力を出す必要がありそうです。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(11500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x166, 2)
    OP_29(0xAA, 0x1, 0x5)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    NewScene("c0100", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_39_3BF0 end

    def Function_40_5212(): pass

    label("Function_40_5212")


    def lambda_5217():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5217)

    def lambda_5231():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5231)
    WaitChrThread(0xFE, 1)

    def lambda_5246():
        OP_95(0xFE, 10500, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5246)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Return()

    # Function_40_5212 end

    def Function_41_52E8(): pass

    label("Function_41_52E8")


    def lambda_52ED():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52ED)

    def lambda_5307():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5307)
    WaitChrThread(0xFE, 1)

    def lambda_531C():
        OP_95(0xFE, 12000, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_531C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_41_52E8 end

    def Function_42_533D(): pass

    label("Function_42_533D")


    def lambda_5342():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5342)

    def lambda_535C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_535C)
    WaitChrThread(0xFE, 1)

    def lambda_5371():
        OP_95(0xFE, 10500, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5371)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_533D end

    def Function_43_5392(): pass

    label("Function_43_5392")


    def lambda_5397():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5397)

    def lambda_53B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_53B1)
    WaitChrThread(0xFE, 1)

    def lambda_53C6():
        OP_95(0xFE, 12000, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53C6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_5392 end

    def Function_44_53E7(): pass

    label("Function_44_53E7")


    def lambda_53EC():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53EC)

    def lambda_5406():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5406)
    WaitChrThread(0xFE, 1)

    def lambda_541B():
        OP_95(0xFE, 11800, -200, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_541B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_44_53E7 end

    def Function_45_543C(): pass

    label("Function_45_543C")

    OP_92(0xFE, 0x1388, 0xFFFFF830, 0x1F4)

    def lambda_544E():
        OP_95(0xFE, 5000, -200, -2000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_544E)
    WaitChrThread(0xFE, 1)

    def lambda_546C():
        OP_95(0xFE, 10000, -200, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_546C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_543C end

    def Function_46_5486(): pass

    label("Function_46_5486")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03500.itp")
    SetChrChipByIndex(0x2E, 0x1E)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, -2960, -200, 7150, 15)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0x2F)
    SetChrPos(0x2F, -17280, -200, 6420, 90)
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    Fade(1000)
    OP_68(-2900, 780, 7160, 0)
    MoveCamera(57, 18, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(8260, 0)
    SetCameraDistance(10260, 3000)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(1000)
    OP_68(5540, 2800, -6730, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7220, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 49)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x105, 3)

    def lambda_5686():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5686)
    Sleep(50)

    def lambda_5696():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5696)
    Sleep(50)

    def lambda_56A6():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56A6)
    Sleep(50)

    def lambda_56B6():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56B6)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x101,
        "#11P#00005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        "#12P#00101Fいた……\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    Fade(1000)
    OP_68(-19590, 20100, 22530, 0)
    MoveCamera(27, 2, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(1530, 0)
    OP_0D()
    OP_68(-13810, 9200, 12250, 9000)
    MoveCamera(27, 2, 0, 9000)
    OP_6E(780, 9000)
    SetCameraDistance(37930, 9000)
    OP_6F(0x1)
    Sleep(800)
    OP_68(1610, 2500, 790, 5000)
    MoveCamera(350, -3, 0, 5000)
    OP_6E(780, 5000)
    SetCameraDistance(5910, 5000)
    OP_6F(0x1)
    Sleep(1000)

    #C0190
    ChrTalk(
        0x2E,
        (
            "#03506Fふ～……\x02\x03",

            "#03510F……しかしクロスベルってのは\x01",
            "マジで訳わからんよなァ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-1640, 1400, 4800, 0)
    MoveCamera(7, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12380, 0)
    SetCameraDistance(10380, 3000)
    SetChrPos(0x101, -3960, -200, 1110, 15)
    SetChrPos(0x102, -2460, -200, 1110, 15)
    SetChrPos(0x109, -3460, -200, 110, 15)
    SetChrPos(0x105, -1960, -200, 110, 15)

    def lambda_58DD():
        OP_98(0x101, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58DD)
    Sleep(50)

    def lambda_58FA():
        OP_98(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58FA)
    Sleep(50)

    def lambda_5917():
        OP_98(0x109, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5917)
    Sleep(50)

    def lambda_5934():
        OP_98(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5934)
    Sleep(50)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0191
    ChrTalk(
        0x101,
        (
            "#6P#00001F……言いたいことは\x01",
            "何となく分かりますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        (
            "#12P#00103F──通称《オルキスタワー》。\x02\x03",

            "地上２５０アージュ、４０階建ての\x01",
            "世界初の超高層ビルディング。\x02\x03",

            "#00100F新市庁に加えて、企業用のフロア、\x01",
            "国際会議場なども用意されているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x109,
        (
            "#6P#10103F確かに圧巻ですよね……\x02\x03",

            "#10100Fこんなに離れているのに\x01",
            "あんなに大きく見えるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、まだ隠れているから\x01",
            "どんなデザインか分からないけど……\x02\x03",

            "#10302Fもう一通り完成してるんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、もう市の職員の半分は\x01",
            "あちらに移っているらしい。\x02\x03",

            "#00004F実際のビルのお披露目は\x01",
            "通商会議の時になるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x2E,
        (
            "#6P#03500Fで、並みいる首脳たちの\x01",
            "度肝を抜くつもりってわけだ。\x02\x03",

            "#03506Fやれやれ。\x01",
            "ディーター・クロイスってのは\x01",
            "思ってた以上の人物みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#6P#00003F………………………………\x02\x03",

            "#00001F──クロスベル警察、\x01",
            "特務支援課としてお聞きします。\x02\x03",

            "レクター・アランドール殿。\x01",
            "身元の確認にご協力ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x2E,
        (
            "#6P#03504Fくくっ……\x02\x03",

            "#03500F真面目だねぇ。\x01",
            "──イヤだと言ったら？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#12P#00103F……確かにクロスベルでは\x01",
            "帝国、共和国政府関係者に対して\x01",
            "法的拘束力を行使できません。\x02\x03",

            "#00101Fですがそれは、あくまで身元が\x01",
            "明らかになっている場合だけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#12P#10303F逆に明らかに出来なければ\x01",
            "普通の外国人と同じレベルでは\x01",
            "取り調べる事ができる……\x02\x03",

            "#10300Fなるほど、そういうことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x2E,
        "#6P#03504Fフム、そう来たか。\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0xB4, 0x1F4)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0202
    AnonymousTalk(
        0x2E,
        (
            "……仕方ない。\x01",
            "年貢の納め時のようだな。\x02\x03",

            "いいぜ、オレの所属は──\x02",
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
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x2E, 0x2D, 0x1F4)

    #C0203
    ChrTalk(
        0x2E,
        "#6P#03505Fんー……？\x02",
    )

    CloseMessageWindow()

    def lambda_5F6C():
        OP_93(0x101, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F6C)
    Sleep(50)

    def lambda_5F7C():
        OP_93(0x102, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F7C)
    Sleep(50)

    def lambda_5F8C():
        OP_93(0x109, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F8C)
    Sleep(50)

    def lambda_5F9C():
        OP_93(0x105, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F9C)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(5510, 2800, 17730, 0)
    MoveCamera(32, 9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    #C0204
    ChrTalk(
        0x101,
        "#N#00005Fどうしたんですか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0205
    ChrTalk(
        0x2E,
        (
            "#N#03505Fああ、向こうの建物だ。\x02\x03",

            "#03506F……なんか黒い人影が\x01",
            "屋根を飛び回ってないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0206
    ChrTalk(
        0x101,
        "#N#00011Fえ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0207
    ChrTalk(
        0x102,
        "#N#11P#00105Fま、まさか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0208
    ChrTalk(
        0x105,
        (
            "#N#11P#10305Fへえ、もしかして\x01",
            "あの《銀》って人かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0209
    ChrTalk(
        0x109,
        (
            "#N#11P#10105Fで、でも……\x01",
            "こんな昼間からですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrFlags(0x2E, 0x80)
    OP_0D()
    SetChrPos(0x101, 0, -200, 5110, 30)
    SetChrPos(0x102, 2000, -200, 5110, 30)
    SetChrPos(0x109, 1000, -200, 4110, 30)
    SetChrPos(0x105, 2500, -200, 4110, 30)
    Fade(500)
    OP_68(-5750, 2800, 3270, 0)
    MoveCamera(53, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5280, 0)
    OP_0D()
    OP_93(0x109, 0x10E, 0x3E8)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0210
    ChrTalk(
        0x109,
        "#10111Fああっ！？\x02",
    )

    CloseMessageWindow()

    def lambda_6227():
        OP_93(0x101, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6227)
    Sleep(50)

    def lambda_6237():
        OP_93(0x102, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6237)
    Sleep(50)

    def lambda_6247():
        OP_93(0x105, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6247)

    #C0211
    ChrTalk(
        0x101,
        "#00011Fし、しまった！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_628A():
        OP_95(0x101, -16360, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_628A)
    Sleep(100)

    def lambda_62A7():
        OP_95(0x102, -16360, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_62A7)
    Sleep(50)

    def lambda_62C4():
        OP_95(0x109, -15060, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62C4)
    Sleep(50)

    def lambda_62E1():
        OP_95(0x105, -15060, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_62E1)
    Sleep(50)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(500)
    OP_68(-20920, 2800, 4200, 0)
    MoveCamera(54, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5220, 0)
    SetChrPos(0x101, -11360, -200, 4810, 270)
    SetChrPos(0x102, -11360, -200, 6110, 270)
    SetChrPos(0x109, -10060, -200, 4810, 270)
    SetChrPos(0x105, -10060, -200, 6110, 270)

    def lambda_6386():
        OP_95(0x101, -16180, -200, 5770, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6386)
    Sleep(100)

    def lambda_63A3():
        OP_95(0x102, -16149, -200, 6900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63A3)
    Sleep(50)

    def lambda_63C0():
        OP_95(0x109, -14800, -200, 5880, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63C0)
    Sleep(50)

    def lambda_63DD():
        OP_95(0x105, -15150, -200, 6830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63DD)
    WaitChrThread(0x102, 1)

    def lambda_63FB():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63FB)
    WaitChrThread(0x105, 1)

    def lambda_640C():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_640C)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0212
    ChrTalk(
        0x102,
        (
            "#5P#00105Fま、まさか\x01",
            "このザイルで下へ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x109,
        "#10106Fあ、ありえない……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x105,
        (
            "#10309Fあはは！\x01",
            "信じられない事するなぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00006Fくっ……ここまで常識が\x01",
            "通用しない相手だなんて……\x02\x03",

            "#00007Fこの下は裏通りだ！\x01",
            "とにかく階段で降りるぞ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("c0500", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_46_5486 end

    def Function_47_6591(): pass

    label("Function_47_6591")


    def lambda_6596():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6596)

    def lambda_65A7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65A7)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 6830, -200, -3780, 2000, 0x0)
    Return()

    # Function_47_6591 end

    def Function_48_65D5(): pass

    label("Function_48_65D5")


    def lambda_65DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_65DA)

    def lambda_65EB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65EB)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 8000, -200, -4990, 2000, 0x0)
    Return()

    # Function_48_65D5 end

    def Function_49_6619(): pass

    label("Function_49_6619")


    def lambda_661E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_661E)

    def lambda_662F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_662F)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 8850, -200, -3200, 2000, 0x0)
    Return()

    # Function_49_6619 end

    def Function_50_665D(): pass

    label("Function_50_665D")


    def lambda_6662():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6662)

    def lambda_6673():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6673)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 9880, -200, -4810, 2000, 0x0)
    Return()

    # Function_50_665D end

    def Function_51_66A1(): pass

    label("Function_51_66A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(11860, 1800, -3520, 0)
    MoveCamera(53, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10770, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_676D")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x104, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6864")

    label("loc_676D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_67EB")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6864")

    label("loc_67EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6864")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_6864")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_68CF")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 55)
    Jump("loc_694A")

    label("loc_68CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_690F")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 56)
    Jump("loc_694A")

    label("loc_690F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_694A")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 57)

    label("loc_694A")

    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    OP_6F(0x1)

    #C0216
    ChrTalk(
        0x1A2,
        (
            "#6Pここが百貨店の屋上……\x01",
            "へえ、なかなかいい眺めじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、すごいでしょ？\x01",
            "ここから市の全体が見渡せるのよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0218
    ChrTalk(
        0x1A2,
        "#5Pええ、思った以上でした！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    #C0219
    ChrTalk(
        0x1A2,
        "#11Pそうだ、オルキスタワーは……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6A97")

    def lambda_6A61():

        label("loc_6A61")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6A61")

    QueueWorkItem2(0x101, 1, lambda_6A61)

    def lambda_6A73():

        label("loc_6A73")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6A73")

    QueueWorkItem2(0x102, 1, lambda_6A73)

    def lambda_6A85():

        label("loc_6A85")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6A85")

    QueueWorkItem2(0x104, 1, lambda_6A85)
    Jump("loc_6B1A")

    label("loc_6A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6ADB")

    def lambda_6AA5():

        label("loc_6AA5")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AA5")

    QueueWorkItem2(0x101, 1, lambda_6AA5)

    def lambda_6AB7():

        label("loc_6AB7")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AB7")

    QueueWorkItem2(0x102, 1, lambda_6AB7)

    def lambda_6AC9():

        label("loc_6AC9")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AC9")

    QueueWorkItem2(0x109, 1, lambda_6AC9)
    Jump("loc_6B1A")

    label("loc_6ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6B1A")

    def lambda_6AE9():

        label("loc_6AE9")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AE9")

    QueueWorkItem2(0x101, 1, lambda_6AE9)

    def lambda_6AFB():

        label("loc_6AFB")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AFB")

    QueueWorkItem2(0x102, 1, lambda_6AFB)

    def lambda_6B0D():

        label("loc_6B0D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6B0D")

    QueueWorkItem2(0x105, 1, lambda_6B0D)

    label("loc_6B1A")


    def lambda_6B1F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6B1F)
    Sleep(500)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6B51")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    Jump("loc_6B88")

    label("loc_6B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6B6F")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    Jump("loc_6B88")

    label("loc_6B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6B88")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x105, 0x1)

    label("loc_6B88")

    Fade(500)
    OP_68(-8320, 2600, 1920, 0)
    MoveCamera(26, -1, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7370, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6C7E")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x104, -1960, -200, 110, 0)

    def lambda_6C0D():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6C0D)
    Sleep(50)

    def lambda_6C2A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C2A)
    Sleep(50)

    def lambda_6C47():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C47)
    Sleep(50)

    def lambda_6C64():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C64)
    Jump("loc_6DFF")

    label("loc_6C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6D41")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x109, -1960, -200, 110, 0)

    def lambda_6CD0():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6CD0)
    Sleep(50)

    def lambda_6CED():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CED)
    Sleep(50)

    def lambda_6D0A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D0A)
    Sleep(50)

    def lambda_6D27():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D27)
    Jump("loc_6DFF")

    label("loc_6D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6DFF")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x105, -1960, -200, 110, 0)

    def lambda_6D93():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6D93)
    Sleep(50)

    def lambda_6DB0():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DB0)
    Sleep(50)

    def lambda_6DCD():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DCD)
    Sleep(50)

    def lambda_6DEA():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6DEA)

    label("loc_6DFF")

    OP_0D()
    WaitChrThread(0x101, 1)

    #C0220
    ChrTalk(
        0x1A2,
        "あれか……！\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x1A2,
        (
            "まだヴェールに包まれた状態で\x01",
            "あのソンザイ感はすごいな！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0222
    ChrTalk(
        0x1A2,
        (
            "#5Pささ、エリィお姉さんも\x01",
            "もっと前へ、そしてボクのそばへ！\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        "#00109Fふふっ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00006Fふぅ、くれぐれも\x01",
            "落ちないように気を付けてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1620, -2300, 8900, 0)
    MoveCamera(48, 26, 2, 0)
    OP_6E(700, 0)
    SetCameraDistance(20270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6F87")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x104, -1960, -200, 3110, 0)
    Jump("loc_7026")

    label("loc_6F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6FD9")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x109, -1960, -200, 3110, 0)
    Jump("loc_7026")

    label("loc_6FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7026")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x105, -1960, -200, 3110, 0)

    label("loc_7026")

    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0225
    ChrTalk(
        0x101,
        (
            "#12P#00000Fさてと、屋上からの景色は\x01",
            "満足できたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x1A2,
        "ああ、タンノウしたぞ。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1A2,
        (
            "お前たちの市街案内も\x01",
            "なかなか悪くなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x1A2,
        (
            "なんていうか……\x01",
            "イイ思い出になりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#12P#00009Fそうか、そう言ってもらえて\x01",
            "何よりだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)
    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0230
    ChrTalk(
        0x1A2,
        (
            "ボクは、明後日の朝には\x01",
            "カルバードに帰る予定だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x1A2,
        (
            "そしてまた、\x01",
            "オトナたちにかこまれて\x01",
            "勉強ヅケの毎日ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x1A2,
        (
            "それが人の上に立つ者の\x01",
            "宿命ってことでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        "#11P#00105Fシン君……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_723B")

    #C0234
    ChrTalk(
        0x104,
        "#00303F……なるほどな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728A")

    label("loc_723B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7264")

    #C0235
    ChrTalk(
        0x109,
        "#10103F……なるほど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728A")

    label("loc_7264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_728A")

    #C0236
    ChrTalk(
        0x105,
        "#10303F……なるほどね。\x02",
    )

    CloseMessageWindow()

    label("loc_728A")


    #C0237
    ChrTalk(
        0x101,
        (
            "#12P#00000Fちなみに、シンは\x01",
            "日曜学校には行ってるのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0xB4, 0x1F4)
    Sleep(300)

    #C0238
    ChrTalk(
        0x1A2,
        (
            "ああ、ケンブンを\x01",
            "広めるためってことで一応な。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x1A2,
        (
            "ま、みんなボクの周りの\x01",
            "オトナをおそれて、\x01",
            "近寄ろうともしないけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_73EC")

    #C0240
    ChrTalk(
        0x1A2,
        (
            "だからかな、\x01",
            "キーアとシズクって言ったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x1A2,
        (
            "ああいうコドモと話ができるのは\x01",
            "けっこう新鮮で楽しかったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        "#12P#00000Fはは、そうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7405")

    label("loc_73EC")


    #C0243
    ChrTalk(
        0x101,
        "#12P#00008Fシン……\x02",
    )

    CloseMessageWindow()

    label("loc_7405")


    #C0244
    ChrTalk(
        0x1A2,
        (
            "……なんていうか、\x01",
            "くだらない話をしてしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1A2,
        "とにかく、案内の方はもう十分だ。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1A2,
        "あとは事務所に送りとどけてくれ。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        "#12P#00000Fああ、了解だ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 4)
    SetScenarioFlags(0x22, 5)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_66A1 end

    def Function_52_74C2(): pass

    label("Function_52_74C2")


    def lambda_74C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_74C7)

    def lambda_74D8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_74D8)
    WaitChrThread(0x1A2, 1)
    OP_95(0x1A2, 14590, -200, -3020, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_52_74C2 end

    def Function_53_750D(): pass

    label("Function_53_750D")


    def lambda_7512():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7512)

    def lambda_7523():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7523)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 13970, -200, -4930, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_53_750D end

    def Function_54_7558(): pass

    label("Function_54_7558")


    def lambda_755D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_755D)

    def lambda_756E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_756E)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13740, -200, -1810, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_7558 end

    def Function_55_75A3(): pass

    label("Function_55_75A3")


    def lambda_75A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_75A8)

    def lambda_75B9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75B9)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_75A3 end

    def Function_56_75EE(): pass

    label("Function_56_75EE")


    def lambda_75F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_75F3)

    def lambda_7604():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7604)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_56_75EE end

    def Function_57_7639(): pass

    label("Function_57_7639")


    def lambda_763E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_763E)

    def lambda_764F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_764F)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_57_7639 end

    SaveToFile()

Try(main)
