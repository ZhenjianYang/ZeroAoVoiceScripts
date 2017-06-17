from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0110.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0110",                  # 0
        "セルゲイ課長",           # 1
        "キーア",                 # 2
        "ツァイト",               # 3
        "セシル",                 # 4
        "コッペ",                 # 5
        "キャットフード",         # 6
        "グレイスの声",           # 7
        "食器",                   # 8
        "食器",                   # 9
        "食器",                   # 10
        "食器",                   # 11
        "食器",                   # 12
        "食器",                   # 13
        "食器",                   # 14
        "食器",                   # 15
        "食器",                   # 16
        "食器",                   # 17
        "食器",                   # 18
        "食器",                   # 19
        "食器",                   # 20
        "食器",                   # 21
        "食器",                   # 22
        "食器",                   # 23
        "食器",                   # 24
        "食器",                   # 25
        "食器",                   # 26
        "椅子",                   # 27
        "椅子",                   # 28
        "椅子",                   # 29
        "椅子",                   # 30
        "椅子",                   # 31
        "椅子",                   # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "幻獣調査レポート",       # 35
        "ダミー",                 # 36
        "人形",                   # 37
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
        "chr/ch08202.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch02708.itc",                   # 05
        "chr/ch02702.itc",                   # 06
        "chr/ch14300.itc",                   # 07
        "chr/ch39200.itc",                   # 08
        "apl/ch50092.itc",                   # 09
        "chr/ch14302.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
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

    DeclNpc(64000,   200,     11399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(2710,    0,       2509,    225,  405,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    438,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 64,  7.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -3.5,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 65,  11.0,                  13.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.5,                  -6.75,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 66,  19.0,                  4.0,                   0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  -2.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 15,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  18, 0x0000)
    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  12, 0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  11, 0x0000)
    DeclActor(64000,   30,      9800,    1500,    64000,   1500,    11400,   0x007E, 0,  4,  0x0000)
    DeclActor(63890,   30,      11070,   1500,    63890,   1000,    11070,   0x007C, 0,  63, 0x0000)

    ChipFrameInfo(2332, 0)                                       # 0

    ScpFunction((
        "Function_0_91C",          # 00, 0
        "Function_1_9CC",          # 01, 1
        "Function_2_9F7",          # 02, 2
        "Function_3_10A2",         # 03, 3
        "Function_4_1393",         # 04, 4
        "Function_5_1397",         # 05, 5
        "Function_6_2541",         # 06, 6
        "Function_7_3048",         # 07, 7
        "Function_8_3BAF",         # 08, 8
        "Function_9_3CF4",         # 09, 9
        "Function_10_3F1E",        # 0A, 10
        "Function_11_4363",        # 0B, 11
        "Function_12_43B6",        # 0C, 12
        "Function_13_440B",        # 0D, 13
        "Function_14_44C8",        # 0E, 14
        "Function_15_4585",        # 0F, 15
        "Function_16_45DC",        # 10, 16
        "Function_17_4898",        # 11, 17
        "Function_18_4B74",        # 12, 18
        "Function_19_5605",        # 13, 19
        "Function_20_5996",        # 14, 20
        "Function_21_5B23",        # 15, 21
        "Function_22_6678",        # 16, 22
        "Function_23_724F",        # 17, 23
        "Function_24_7C66",        # 18, 24
        "Function_25_935E",        # 19, 25
        "Function_26_9382",        # 1A, 26
        "Function_27_9CDC",        # 1B, 27
        "Function_28_9FB1",        # 1C, 28
        "Function_29_BAD6",        # 1D, 29
        "Function_30_C53E",        # 1E, 30
        "Function_31_CFB2",        # 1F, 31
        "Function_32_E928",        # 20, 32
        "Function_33_EDD2",        # 21, 33
        "Function_34_103B4",       # 22, 34
        "Function_35_10443",       # 23, 35
        "Function_36_10DBA",       # 24, 36
        "Function_37_10DF7",       # 25, 37
        "Function_38_11B65",       # 26, 38
        "Function_39_1226B",       # 27, 39
        "Function_40_12719",       # 28, 40
        "Function_41_14202",       # 29, 41
        "Function_42_1457F",       # 2A, 42
        "Function_43_16393",       # 2B, 43
        "Function_44_1735F",       # 2C, 44
        "Function_45_179D0",       # 2D, 45
        "Function_46_197E0",       # 2E, 46
        "Function_47_1982A",       # 2F, 47
        "Function_48_1987F",       # 30, 48
        "Function_49_198B6",       # 31, 49
        "Function_50_198FA",       # 32, 50
        "Function_51_1993E",       # 33, 51
        "Function_52_19976",       # 34, 52
        "Function_53_199A6",       # 35, 53
        "Function_54_1AA4A",       # 36, 54
        "Function_55_1AA9B",       # 37, 55
        "Function_56_1B580",       # 38, 56
        "Function_57_1B5F2",       # 39, 57
        "Function_58_1C605",       # 3A, 58
        "Function_59_1C689",       # 3B, 59
        "Function_60_1C6C6",       # 3C, 60
        "Function_61_1C703",       # 3D, 61
        "Function_62_1C765",       # 3E, 62
        "Function_63_1C893",       # 3F, 63
        "Function_64_1D22A",       # 40, 64
        "Function_65_1D285",       # 41, 65
        "Function_66_1D2E0",       # 42, 66
        "Function_67_1D33B",       # 43, 67
    ))


    def Function_0_91C(): pass

    label("Function_0_91C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_954"),
        (1, "loc_960"),
        (2, "loc_96C"),
        (3, "loc_978"),
        (4, "loc_984"),
        (5, "loc_990"),
        (6, "loc_99C"),
        (SWITCH_DEFAULT, "loc_9A8"),
    )


    label("loc_954")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_960")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_96C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_978")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_984")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_990")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_99C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9CB")

    Return()

    # Function_0_91C end

    def Function_1_9CC(): pass

    label("Function_1_9CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F6")
    OP_94(0xFE, 0x1D8DA, 0x1F18, 0x1E53C, 0x1360, 0x3E8)
    Sleep(300)
    Jump("Function_1_9CC")

    label("loc_9F6")

    Return()

    # Function_1_9CC end

    def Function_2_9F7(): pass

    label("Function_2_9F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2F")
    Jump("loc_AD0")

    label("loc_A2F")

    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA8")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_AC7")

    label("loc_AA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC7")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_AC7")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD0")

    Jump("loc_AD5")

    label("loc_AD5")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AF1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3C")

    label("loc_AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B35")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122700, 0, 6000, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 121800, 0, 6000, 0)
    Jump("loc_F3C")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B48")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3C")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BC3")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    SetChrChipByIndex(0xA, 0x5)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0xA)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 5450, 150, 2100, 0)
    Jump("loc_F3C")

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE2")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_F3C")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_C17")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    Jump("loc_F3C")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C73")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    Jump("loc_F3C")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CD4")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 117430, 30, 4080, 90)
    Jump("loc_F3C")

    label("loc_CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D0D")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x5)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D42")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D6B")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D7E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3C")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_DDA")
    SetChrPos(0x8, 14400, 850, 12500, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_E25")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    Jump("loc_F3C")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_E70")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 123270, 0, 4980, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    Jump("loc_F3C")

    label("loc_E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EA5")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EDD")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 65890, 0, 1800, 225)

    label("loc_ED8")

    Jump("loc_F3C")

    label("loc_EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F2E")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122060, 0, 5750, 45)
    BeginChrThread(0xC, 0, 0, 1)
    Jump("loc_F3C")

    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F3C")
    SetChrFlags(0x8, 0x80)

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F50")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)
    Jump("loc_1063")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F61")
    ClearScenarioFlags(0x22, 1)
    Jump("loc_1063")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F75")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)
    Jump("loc_1063")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_F86")
    Event(0, 28)
    Jump("loc_1063")

    label("loc_F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_F9A")
    ClearScenarioFlags(0x22, 4)
    Event(0, 31)
    Jump("loc_1063")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_FB1")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 7)
    Event(0, 35)
    Jump("loc_1063")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_FC2")
    Event(0, 37)
    Jump("loc_1063")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_FD9")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 7)
    Event(0, 38)
    Jump("loc_1063")

    label("loc_FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_FED")
    ClearScenarioFlags(0x23, 0)
    Event(0, 40)
    Jump("loc_1063")

    label("loc_FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1001")
    ClearScenarioFlags(0x23, 1)
    Event(0, 42)
    Jump("loc_1063")

    label("loc_1001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1012")
    ClearScenarioFlags(0x23, 2)
    Jump("loc_1063")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_1026")
    ClearScenarioFlags(0x23, 3)
    Event(0, 43)
    Jump("loc_1063")

    label("loc_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_103D")
    ClearScenarioFlags(0x23, 4)
    SetScenarioFlags(0x0, 7)
    Event(0, 45)
    Jump("loc_1063")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_1054")
    ClearScenarioFlags(0x23, 5)
    SetScenarioFlags(0x0, 7)
    Event(0, 53)
    Jump("loc_1063")

    label("loc_1054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_1063")
    ClearScenarioFlags(0x23, 6)
    Event(0, 55)

    label("loc_1063")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_108B")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_108B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A1")
    SetMapFlags(0x10000000)
    Event(0, 57)

    label("loc_10A1")

    Return()

    # Function_2_9F7 end

    def Function_3_10A2(): pass

    label("Function_3_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_10B7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)

    label("loc_10B7")

    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F0")
    OP_1B(0x0, 0x0, 0x1D)
    OP_1B(0x8, 0x0, 0x1E)

    label("loc_10F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1144")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_1144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118E")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_118E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AF")
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)

    label("loc_11AF")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11D2")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_11E1")

    label("loc_11D2")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_11E1")

    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1200")
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x1, 0x1)

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1213")
    SetMapObjFlags(0x6, 0x10)
    OP_65(0x2, 0x1)

    label("loc_1213")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1225")
    Jump("loc_1328")

    label("loc_1225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1233")
    Jump("loc_1328")

    label("loc_1233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1245")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_1257")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_1257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1269")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_127B")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_127B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_128D")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_128D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_129F")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_129F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12AD")
    Jump("loc_1328")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_12BB")
    Jump("loc_1328")

    label("loc_12BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_12C9")
    Jump("loc_1328")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_12DB")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_12DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_12ED")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_12ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12FF")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_130D")
    Jump("loc_1328")

    label("loc_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_131F")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1328")

    label("loc_1328")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1355")
    OP_66(0x4, 0x1)

    label("loc_1355")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1377")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1377")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_138F")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_138F")

    Call(0, 67)
    Return()

    # Function_3_10A2 end

    def Function_4_1393(): pass

    label("Function_4_1393")

    Call(0, 5)
    Return()

    # Function_4_1393 end

    def Function_5_1397(): pass

    label("Function_5_1397")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_13A8")
    Jump("loc_253D")

    label("loc_13A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1536")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01000Fノエルの警備隊への復帰について、\x01",
            "必要な手続きは俺がやっておく。\x02\x03",

            "襲撃事件の影響で各地に\x01",
            "支援要請がでているはずだから、\x01",
            "余裕があればこなしておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x109,
        (
            "#10100Fはい、今日一日\x01",
            "全力で取り組ませていただきます。\x02\x03",

            "#10103F……セルゲイ課長、\x01",
            "今までありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#01004Fクク、礼なんざいらん。\x02\x03",

            "#01002Fせめて悔いの無いように、\x01",
            "仕事納めに集中するといい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15C6")

    label("loc_1536")


    #C0004
    ChrTalk(
        0x8,
        (
            "#01000Fノエルの警備隊復帰について、\x01",
            "必要な手続きは俺がやっておこう。\x02\x03",

            "#01004F夜は俺の奢りで外食にいくから、\x01",
            "それまでには戻ってくるんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C6")

    Jump("loc_253D")

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_1747")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BC")

    #C0005
    ChrTalk(
        0x8,
        (
            "#01003Fようやくランディの足取りを掴んだか。\x02\x03",

            "#01002Fクク、これでようやく連れ戻す\x01",
            "お膳立てが整ったってワケだ。\x02\x03",

            "#01001Fそうと決まればグズグズするな。\x01",
            "全員であの馬鹿野郎を連れ戻して来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00001Fええ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1742")

    label("loc_16BC")


    #C0007
    ChrTalk(
        0x8,
        (
            "#01003F警備隊も、今は増援部隊の\x01",
            "再構築をしてる所だろう。\x02\x03",

            "#01001Fそうと決まればグズグズするな。\x01",
            "全員でランディを連れ戻して来い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1742")

    Jump("loc_253D")

    label("loc_1747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_18F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")

    #C0008
    ChrTalk(
        0x8,
        (
            "#01000Fマインツ方面の占拠事件の影響で、\x01",
            "支援要請も入ってきてない状態だ。\x02\x03",

            "#01003Fお前たちは、ランディのヤツを\x01",
            "探し出すことに専念するといい。\x02\x03",

            "#01001Fせいぜい気をつけて行ってこい。\x01",
            "俺も何か分かったら連絡する。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00001Fはい……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18F4")

    label("loc_184F")


    #C0010
    ChrTalk(
        0x8,
        (
            "#01003F今日は支援要請もないし、\x01",
            "お前たちは、ランディのヤツを\x01",
            "探し出すことに専念するといい。\x02\x03",

            "#01001Fせいぜい気をつけて行ってこい。\x01",
            "俺も何か分かったら連絡する。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F4")

    Jump("loc_253D")

    label("loc_18F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F9")

    #C0011
    ChrTalk(
        0x8,
        (
            "#01003Fヴァルド・ヴァレスや\x01",
            "グノーシスの件は二課や警備隊が\x01",
            "捜査を進めている。\x02\x03",

            "#01000F横断鉄道の復旧も終わった今、\x01",
            "そうそう焦ることもないだろう。\x02\x03",

            "遊撃士の件については、\x01",
            "余裕があれば仕事がてら\x01",
            "ギルドに顔を出してやるんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A8F")

    label("loc_19F9")


    #C0012
    ChrTalk(
        0x8,
        (
            "#01000F横断鉄道の復旧も終わった今、\x01",
            "そうそう焦ることもないだろう。\x02\x03",

            "遊撃士の件については、\x01",
            "余裕があれば仕事がてら\x01",
            "ギルドに顔を出してやるんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8F")

    Jump("loc_253D")

    label("loc_1A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B88")

    #C0013
    ChrTalk(
        0x8,
        (
            "#01000F……戻ったか。\x01",
            "フランから連絡は来たようだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000Fええ、今から事故現場に\x01",
            "向かうところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#01003Fそうか、分かった。\x02\x03",

            "#01000F人形工房の調査報告は後で聞く。\x01",
            "お前たちも出来ることをやってこい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C2E")

    label("loc_1B88")


    #C0016
    ChrTalk(
        0x8,
        (
            "#01000F西クロスベル街道の事故現場には、\x01",
            "二課の連中やソーニャたち\x01",
            "警備隊も向かっているはずだ。\x02\x03",

            "人形工房の調査報告は後で聞く。\x01",
            "お前たちも出来ることをやってこい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2E")

    Jump("loc_253D")

    label("loc_1C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D47")

    #C0017
    ChrTalk(
        0x8,
        (
            "#01006F国家独立の住民投票の件で、\x01",
            "色々と書類が回ってきていてな。\x02\x03",

            "#01002F気になる案件は入ってるが……\x01",
            "まあ、こっちは他の課に任せておけ。\x02\x03",

            "#01000Fひとまず、今は危機管理が先決だ。\x01",
            "人形工房の聞き込みだけじゃなく、\x01",
            "支援要請もカバーしておくといい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DDB")

    label("loc_1D47")


    #C0018
    ChrTalk(
        0x8,
        (
            "#01004Fああ、キーアならついさっき\x01",
            "夕食の買い物に出かけたようだ。\x02\x03",

            "#01002F少し図書館に寄るっつってたが……\x01",
            "まあ、心配なら様子を見に行ってやれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDB")

    Jump("loc_253D")

    label("loc_1DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB1")

    #C0019
    ChrTalk(
        0x8,
        (
            "#01000Fよう、俺もついさっき\x01",
            "病院から戻ってきた所だ。\x02\x03",

            "#01003Fお前らの方は引き続き、\x01",
            "《幻獣》の調査を進めとけ。\x02\x03",

            "#01002F《風の剣聖》が動けないうちに\x01",
            "せいぜい実績を上げるといい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F31")

    label("loc_1EB1")


    #C0020
    ChrTalk(
        0x8,
        (
            "#01003Fお前らの方は引き続き、\x01",
            "《幻獣》の調査を進めとけ。\x02\x03",

            "#01002F《風の剣聖》が動けないうちに\x01",
            "せいぜい実績を上げるといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F31")

    Jump("loc_253D")

    label("loc_1F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F44")
    Jump("loc_253D")

    label("loc_1F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_20A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2027")

    #C0021
    ChrTalk(
        0x8,
        (
            "#01000F俺はテロリストの情報を\x01",
            "市長や警備隊方面に連絡しておく。\x02\x03",

            "ダドリー、うちの奴らの\x01",
            "お守りを頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x10A,
        (
            "#00603Fええ、任せてください。\x02\x03",

            "#00601F……さあ、行くぞお前たち。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00000Fはい！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_209B")

    label("loc_2027")


    #C0024
    ChrTalk(
        0x8,
        (
            "#01000Fジオフロントで\x01",
            "何があったか分からんが、\x01",
            "せいぜい気をつけろ。\x02\x03",

            "ダドリー、うちの奴らの\x01",
            "お守りを頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209B")

    Jump("loc_253D")

    label("loc_20A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_2259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B3")

    #C0025
    ChrTalk(
        0x8,
        (
            "#01000Fお前たちが出くわした\x01",
            "シャーリィって娘も、狙いがあって\x01",
            "現れたわけじゃあるまい。\x02\x03",

            "#01003F確かに《赤い星座》の動向は\x01",
            "気になるが、そればかりに\x01",
            "捉われても仕方ないだろう。\x02\x03",

            "#01000Fま、引き続きお前たちに任せる。\x01",
            "焦らずにやれる事をやってこい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2254")

    label("loc_21B3")


    #C0026
    ChrTalk(
        0x8,
        (
            "#01003F確かに《赤い星座》の動向は\x01",
            "気になるが、そればかりに\x01",
            "捉われても仕方ないだろう。\x02\x03",

            "#01000Fま、引き続きお前たちに任せる。\x01",
            "焦らずにやれる事をやってこい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2254")

    Jump("loc_253D")

    label("loc_2259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2321")

    #C0027
    ChrTalk(
        0x8,
        (
            "#01003F今日は俺はここで待機だ。\x02\x03",

            "#01000F一課と連絡をとりあって、\x01",
            "明日の通商会議の本番に向けて\x01",
            "最後の準備を進めておく。\x02\x03",

            "何かあったら連絡するから\x01",
            "遠慮なく出かけてこい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_237E")

    label("loc_2321")


    #C0028
    ChrTalk(
        0x8,
        (
            "#01003F今日は俺はここで待機だ。\x02\x03",

            "#01000F何かあったら連絡するから\x01",
            "遠慮なく出かけてこい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_237E")

    Jump("loc_253D")

    label("loc_2383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2391")
    Jump("loc_253D")

    label("loc_2391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2534")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B1")

    #C0029
    ChrTalk(
        0x8,
        (
            "#01002F市民の安全を第一に考え、\x01",
            "様々な要望に応える……\x01",
            "それが特務支援課だ。\x02\x03",

            "#01003Fツァオやレクターって奴らは\x01",
            "一筋縄じゃいかないだろうが、\x01",
            "ひとまず捜査一課に任せとけ。\x02\x03",

            "#01000Fお前たちの本来の役割を\x01",
            "見失うんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00000Fええ、任せてください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_252F")

    label("loc_24B1")


    #C0031
    ChrTalk(
        0x8,
        (
            "#01000F市民の安全を第一に考え、\x01",
            "様々な要望に応える……\x01",
            "それが特務支援課だ。\x02\x03",

            "お前たちの本来の役割を\x01",
            "見失うんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252F")

    Jump("loc_253D")

    label("loc_2534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_253D")

    label("loc_253D")

    TalkEnd(0x8)
    Return()

    # Function_5_1397 end

    def Function_6_2541(): pass

    label("Function_6_2541")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270E")

    #C0032
    ChrTalk(
        0x9,
        (
            "#01108Fみんな、その……ゴメンね。\x02\x03",

            "#01103F突然あんなことしちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00000F気にするな、キーア。\x02\x03",

            "#00004Fこんな状況だし、\x01",
            "色々不安なのは仕方ないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#00202Fそれを受け止めるのは\x01",
            "わたしたち保護者の役目です。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00100F何かあったら、\x01",
            "これからも遠慮なく\x01",
            "飛び込んできてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、頼ってくれると\x01",
            "俺たちも嬉しいしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#01108Fうん……ありがとう。\x02\x03",

            "#01100F気をつけてね……\x01",
            "キーア、待ってるから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 6)
    Jump("loc_2761")

    label("loc_270E")


    #C0038
    ChrTalk(
        0x9,
        (
            "#01108Fみんな……ありがとう。\x02\x03",

            "#01100F気をつけてね……\x01",
            "キーア、待ってるから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2761")

    Jump("loc_3044")

    label("loc_2766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2774")
    Jump("loc_3044")

    label("loc_2774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_290E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A7")

    #C0039
    ChrTalk(
        0x9,
        (
            "#01103Fランディ……\x01",
            "ブジに見つかるといいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000Fきっと見つかるさ。\x01",
            "キーアは何も心配しなくていい。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10106Fランディ先輩も罪作りです。\x01",
            "キーアちゃんにこんなに\x01",
            "心配をかけるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#00100Fええ、見つけたら\x01",
            "うんと叱ってやらなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "#01109Fうんっ、そうだね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2909")

    label("loc_28A7")


    #C0044
    ChrTalk(
        0x9,
        (
            "#01109Fランディが帰ってきたら、\x01",
            "キーアも叱るー！\x02\x03",

            "#01100Fみんな……\x01",
            "くれぐれも気をつけてね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2909")

    Jump("loc_3044")

    label("loc_290E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A40")

    #C0045
    ChrTalk(
        0x9,
        (
            "#01109Fえへへ、実は昨日のうちに\x01",
            "材料をたくさん買ってきてたんだー。\x02\x03",

            "雨が降っちゃったけど、\x01",
            "買い物にはいかなくて済みそうー。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00009Fはは、さすがキーアだ。\x02\x03",

            "#00000F今日こそは鍋に参加するから、\x01",
            "いい子で留守番しててくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        "#01109Fうん、ロイドたちも気をつけてねー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A9D")

    label("loc_2A40")


    #C0048
    ChrTalk(
        0x9,
        (
            "#01100Fキーア、今日も\x01",
            "お鍋を用意して待ってるから。\x02\x03",

            "#01109Fロイドたちも気をつけてねー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9D")

    Jump("loc_3044")

    label("loc_2AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AB0")
    Jump("loc_3044")

    label("loc_2AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2ABE")
    Jump("loc_3044")

    label("loc_2ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ACC")
    Jump("loc_3044")

    label("loc_2ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2ADA")
    Jump("loc_3044")

    label("loc_2ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2C97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C28")

    #C0049
    ChrTalk(
        0x9,
        (
            "#01100Fみんな、いってらっしゃーい。\x02\x03",

            "#01109Fえへへ、ダドリーも気をつけてねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x10A,
        "#00603Fだから呼び捨ては止めろと……！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        "#01105Fんー？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x10A,
        (
            "#00606F……ええい、もういい！\x01",
            "お前たち、さっさと行くぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00012F（うーん、さすがのダドリーさんも\x01",
            "  キーアには敵わないか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C92")

    label("loc_2C28")


    #C0054
    ChrTalk(
        0x9,
        (
            "#01109Fみんな、いってらっしゃーい。\x02\x03",

            "えへへ、ダドリーも気をつけてねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10A,
        "#00603F（まったく……）\x02",
    )

    CloseMessageWindow()

    label("loc_2C92")

    Jump("loc_3044")

    label("loc_2C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_2DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7B")

    #C0056
    ChrTalk(
        0x9,
        (
            "#01105Fあのジークって子、\x01",
            "とってもかっこよかったねー。\x02\x03",

            "#01109Fそれにアタマもすっごくいいし。\x01",
            "キーア、また会いたいかもー。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00006F（メモに押された\x01",
            "  白ハヤブサの紋章……\x01",
            "  ま、まさかなあ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DDC")

    label("loc_2D7B")


    #C0058
    ChrTalk(
        0x9,
        (
            "#01105Fあのジークって子、\x01",
            "とってもかっこよかったねー。\x02\x03",

            "#01109Fキーア、また会いたいかもー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDC")

    Jump("loc_3044")

    label("loc_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_2FF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F67")

    #C0059
    ChrTalk(
        0x9,
        (
            "#01102Fメイプルマフィンは\x01",
            "明日くらいまでなら大丈夫だよー。\x02\x03",

            "#01109Fお仕事中におなかがすいたときの\x01",
            "お弁当にしてねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#00000Fああ、ありがとうキーア。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、とっても美味しかったし、\x01",
            "お腹がすくのが楽しみになっちゃうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        "#01102Fえへへ、キーアまた作るからー。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_END)), "loc_2F5F")

    #C0063
    ChrTalk(
        0x101,
        (
            "#00002F（はは、よかった……\x01",
            "  どうやら元気になったみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5F")

    SetScenarioFlags(0x0, 3)
    Jump("loc_2FF0")

    label("loc_2F67")


    #C0064
    ChrTalk(
        0x9,
        (
            "#01104Fふんふふ～ん♪\x01",
            "早く洗い物を済ませちゃおーっと。\x02\x03",

            "#01100Fメイプルマフィンは\x01",
            "お仕事中におなかがすいたときの\x01",
            "お弁当にしてねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF0")

    Jump("loc_3044")

    label("loc_2FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3003")
    Jump("loc_3044")

    label("loc_3003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3011")
    Jump("loc_3044")

    label("loc_3011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_301F")
    Jump("loc_3044")

    label("loc_301F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_302D")
    Jump("loc_3044")

    label("loc_302D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_303B")
    Jump("loc_3044")

    label("loc_303B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3044")

    label("loc_3044")

    TalkEnd(0xFE)
    Return()

    # Function_6_2541 end

    def Function_7_3048(): pass

    label("Function_7_3048")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_315C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313A")

    #C0065
    ChrTalk(
        0xA,
        "#01200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00200Fツァイト……\x01",
            "なんだか気が立ってますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00003Fこの状況を見て\x01",
            "警戒心が高まってるんだろう。\x02\x03",

            "#00001Fツァイト、キーアたちのこと\x01",
            "よろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        "#01200Fウォン！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3157")

    label("loc_313A")


    #C0069
    ChrTalk(
        0xA,
        "#01200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_3157")

    Jump("loc_3BAB")

    label("loc_315C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_316A")
    Jump("loc_3BAB")

    label("loc_316A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_32AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3284")

    #C0070
    ChrTalk(
        0xA,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#00200F『猟兵達は野戦に慣れている。\x01",
            "  相手のテリトリーに入る以上、\x01",
            "  十分に気をつけるがいい。』\x02\x03",

            "……だそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00000Fありがとうツァイト。\x01",
            "忠告痛み入るよ。\x02\x03",

            "正面から猟兵と鉢合わせに\x01",
            "ならないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_32A5")

    label("loc_3284")


    #C0073
    ChrTalk(
        0xA,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_32A5")

    Jump("loc_3BAB")

    label("loc_32AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3365")

    #C0074
    ChrTalk(
        0xA,
        "#01200Fグルルル……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#00203F……そうですね。\x01",
            "ランディさんは大馬鹿です。\x02\x03",

            "#00200Fなんとしても\x01",
            "連れ戻してやりましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#00000Fああ……もちろんだ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_337E")

    label("loc_3365")


    #C0077
    ChrTalk(
        0xA,
        "#01200Fグルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_337E")

    Jump("loc_3BAB")

    label("loc_3383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_33BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339E")
    Call(0, 8)
    Jump("loc_33B9")

    label("loc_339E")


    #C0078
    ChrTalk(
        0xA,
        "#01203Fグルルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_33B9")

    Jump("loc_3BAB")

    label("loc_33BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3473")

    #C0079
    ChrTalk(
        0xA,
        "#01200Fグルルル……ウォン、ウォン。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#00200Fツァイトも大事が起こったのを\x01",
            "感じ取っているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#00001Fああ……気をつけて現場に向かおう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_349C")

    label("loc_3473")


    #C0082
    ChrTalk(
        0xA,
        "#01200Fグルルル……ウォン、ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_349C")

    Jump("loc_3BAB")

    label("loc_34A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34CC")

    #C0083
    ChrTalk(
        0xA,
        "#01203F……グルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BAB")

    label("loc_34CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    #C0084
    ChrTalk(
        0xA,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#00200F『気をつけていくがいい』\x01",
            "……だそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003F幻獣と戦うとなったら\x01",
            "かなり危険そうだしな……\x02\x03",

            "#00000Fありがとう、ツァイト。\x01",
            "危なくなったら\x01",
            "また力を貸してくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35D8")

    label("loc_35B9")


    #C0087
    ChrTalk(
        0xA,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_35D8")

    Jump("loc_3BAB")

    label("loc_35DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35EB")
    Jump("loc_3BAB")

    label("loc_35EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3851")

    #C0088
    ChrTalk(
        0xA,
        "#01200Fグルルルル……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x10A,
        (
            "#00603Fフン、相変わらず偉そうな狼だ。\x02\x03",

            "#00600Fだが警察犬である以上は\x01",
            "その力を借りることもあるだろう。\x01",
            "いつでも出られる準備をしておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        "#01200F……ウォン。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F2")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_36F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3726")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3726")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_375A")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_375A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378E")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_378E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37C2")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_37C2")

    Sleep(1000)

    #C0091
    ChrTalk(
        0x104,
        (
            "#00306F（偉そうったって、\x01",
            "  他人のこと言えねーだろ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#00100F（ふふ、ダドリーさんなりの\x01",
            "  激励の仕方なんだろうけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3872")

    label("loc_3851")


    #C0093
    ChrTalk(
        0xA,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_3872")

    Jump("loc_3BAB")

    label("loc_3877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_38A6")

    #C0094
    ChrTalk(
        0xA,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BAB")

    label("loc_38A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39CD")

    #C0095
    ChrTalk(
        0xA,
        "#01200Fグルルル……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C8")

    #C0096
    ChrTalk(
        0x101,
        (
            "#00005Fそうだ、ツァイト……\x01",
            "オルキスタワーのお披露目は\x01",
            "キーアと一緒に見たんだよな。\x02\x03",

            "なんだかキーアが元気ないけど\x01",
            "何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00106Fうーん、ティオちゃんがいないと\x01",
            "さすがに分からないわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_39C8")

    Jump("loc_3BAB")

    label("loc_39CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3AD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AAE")

    #C0099
    ChrTalk(
        0xA,
        "#01200Fグルルル……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#00300Fようツァイト。\x02\x03",

            "#00309Fハハ、こないだの旧鉱山のときは\x01",
            "道案内してくれてサンキューな。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#00000Fはは、これからも頼りにしてるよ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3ACD")

    label("loc_3AAE")


    #C0103
    ChrTalk(
        0xA,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_3ACD")

    Jump("loc_3BAB")

    label("loc_3AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B84")

    #C0104
    ChrTalk(
        0xA,
        "#01203Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00000F雨の日はツァイトも\x01",
            "つまらなそうだな。\x02\x03",

            "まあ、今日もおとなしく\x01",
            "留守番しててくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        "#01200F……ウォン。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B9D")

    label("loc_3B84")


    #C0107
    ChrTalk(
        0xA,
        "#01200F……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_3B9D")

    Jump("loc_3BAB")

    label("loc_3BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BAB")

    label("loc_3BAB")

    TalkEnd(0xFE)
    Return()

    # Function_7_3048 end

    def Function_8_3BAF(): pass

    label("Function_8_3BAF")

    OP_4B(0xC, 0xFF)

    #C0108
    ChrTalk(
        0xA,
        "#01200Fグルルルル……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        "にゃあ～～。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#00200Fツァイトとコッペも\x01",
            "夕飯の鍋を楽しみにしてる\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x109,
        (
            "#10105Fあれ、でも猫って\x01",
            "その名の通り猫舌なんじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        (
            "#10300F犬科の動物も\x01",
            "猫舌じゃなかったかな？\x01",
            "フフ、奇妙な表現だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#00203F……わたしが冷ましてあげます。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        "#01200Fウォン。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 4)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_3BAF end

    def Function_9_3CF4(): pass

    label("Function_9_3CF4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D05")
    Jump("loc_3F1A")

    label("loc_3D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E42")

    #C0115
    ChrTalk(
        0xFE,
        "にゃにやゃゃあ～㈱\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#00100Fふふ、よく食べてるみたいね。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#00200Fキャットフードの味が\x01",
            "懐かしいみたいです。\x02\x03",

            "わたしたちの居ない間は、\x01",
            "自分で外にエサをとりに\x01",
            "出かけていたみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#00305Fへえ、そうだったのかよ。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00000Fはは、コッペって意外と\x01",
            "たくましい所があるよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3E5A")

    label("loc_3E42")


    #C0120
    ChrTalk(
        0xFE,
        "にゃにやゃゃあ～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_3E5A")

    Jump("loc_3F1A")

    label("loc_3E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E6D")
    Jump("loc_3F1A")

    label("loc_3E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E88")
    Call(0, 8)
    Jump("loc_3EEC")

    label("loc_3E88")


    #C0121
    ChrTalk(
        0xFE,
        "にゃあ～～。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00004F（キーアもいるし、今日は俺たちから\x01",
            "  エサをやる必要はなさそうだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EEC")

    Jump("loc_3F1A")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EFF")
    Jump("loc_3F1A")

    label("loc_3EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F1A")

    #C0123
    ChrTalk(
        0xFE,
        "にゃ～～ご。\x02",
    )

    CloseMessageWindow()

    label("loc_3F1A")

    TalkEnd(0xFE)
    Return()

    # Function_9_3CF4 end

    def Function_10_3F1E(): pass

    label("Function_10_3F1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41FE")

    #C0124
    ChrTalk(
        0xB,
        (
            "#05928Fアリオスさんがシズクちゃんを\x01",
            "強引に退院させた理由……\x01",
            "こんな大事に繋がってるなんて。\x02\x03",

            "#05923Fシズクちゃんの安全を考えたら\x01",
            "仕方ないのかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#00003Fああ、そうだな……\x02\x03",

            "#00005F……そういえばセシル姉。\x01",
            "ウルスラ病院の様子はどうなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#00100Fそうね、入院していた警察関係者や\x01",
            "イリアさんの容態も気になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "#05920F病院でも混乱があるけど、\x01",
            "患者さんたちへの対応は\x01",
            "通常通り行っているわ。\x02\x03",

            "#05924Fフランさんは順調に回復して\x01",
            "一般病棟に移されたし……\x02\x03",

            "#05920Fドノバンさんも、この間\x01",
            "ようやく意識が戻ったところよ。\x02\x03",

            "#05928F……相変わらず、イリアは\x01",
            "目を覚まさないけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#00203Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#00303F早く元気になってくれると\x01",
            "いいッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        "#05924Fうん……本当にそうね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 1)
    Jump("loc_435F")

    label("loc_41FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42EA")

    #C0131
    ChrTalk(
        0xB,
        (
            "#05920F病院でも混乱があったけど、\x01",
            "患者さんたちへの対応は\x01",
            "通常通り行っているわ。\x02\x03",

            "#05923Fともかく……\x01",
            "私はここでキーアちゃんと\x01",
            "一緒に留守番しているから。\x02\x03",

            "#05920F大変な状況みたいだけど……\x01",
            "くれぐれも気を付けてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_435F")

    label("loc_42EA")


    #C0132
    ChrTalk(
        0xB,
        (
            "#05920F私はここでキーアちゃんと\x01",
            "一緒に留守番しているから。\x02\x03",

            "大変な状況みたいだけど……\x01",
            "くれぐれも気を付けてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435F")

    TalkEnd(0xFE)
    Return()

    # Function_10_3F1E end

    def Function_11_4363(): pass

    label("Function_11_4363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4375")
    Call(0, 16)
    Jump("loc_43B5")

    label("loc_4375")

    TalkBegin(0xFF)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000Fここはティオの部屋だ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_43B5")

    Return()

    # Function_11_4363 end

    def Function_12_43B6(): pass

    label("Function_12_43B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C8")
    Call(0, 17)
    Jump("loc_440A")

    label("loc_43C8")

    TalkBegin(0xFF)

    #C0134
    ChrTalk(
        0x101,
        (
            "#00000Fここはランディの部屋だ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_440A")

    Return()

    # Function_12_43B6 end

    def Function_13_440B(): pass

    label("Function_13_440B")

    EventBegin(0x1)

    #C0135
    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、キーアが\x01",
            "日曜学校に行くって言ってたな。\x02\x03",

            "課長も出かけた事だし、\x01",
            "一緒に出た方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        "#00100Fそうね、声を掛けましょう。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_13_440B end

    def Function_14_44C8(): pass

    label("Function_14_44C8")

    EventBegin(0x1)

    #C0137
    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、キーアが\x01",
            "日曜学校に行くって言ってたな。\x02\x03",

            "課長も出かけた事だし、\x01",
            "一緒に出た方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#00100Fそうね、声を掛けましょう。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_14_44C8 end

    def Function_15_4585(): pass

    label("Function_15_4585")

    EventBegin(0x1)

    #C0139
    ChrTalk(
        0x101,
        (
            "#00000Fキーアはこれから日曜学校だ。\x01",
            "裏口の方が近道だな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_15_4585 end

    def Function_16_45DC(): pass

    label("Function_16_45DC")

    EventBegin(0x0)
    Fade(500)
    OP_68(169990, 1000, 63110, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23860, 0)
    SetChrPos(0x101, 170800, 0, 62310, 315)
    SetChrPos(0x102, 168790, 0, 62190, 45)
    SetChrPos(0x109, 171240, 0, 63400, 270)
    SetChrPos(0x105, 168190, 0, 63200, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4676")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_4676")

    OP_0D()

    #C0140
    ChrTalk(
        0x102,
        "#6P#00100Fここはティオちゃんの部屋ね。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x105,
        (
            "#6P#10300F確か今は、レマン自治州に\x01",
            "出張しているんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ヨナと一緒に\x01",
            "エプスタイン財団の\x01",
            "研究所に行っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#6P#00100F自治州法の改正で導力ネットも\x01",
            "普及が進められているし、\x01",
            "その関係の手伝いなんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x109,
        (
            "#11P#10103F難しいことはわかりませんけど……\x01",
            "そっちもかなり大変そうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_484A")

    #C0145
    ChrTalk(
        0x1A5,
        "#12P#01100Fティオ、早く帰ってこれるといいねー。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#00000Fああ、本当にな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4880")

    label("loc_484A")


    #C0147
    ChrTalk(
        0x101,
        (
            "#00000Fああ、早く帰ってこれると\x01",
            "いいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4880")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_16_45DC end

    def Function_17_4898(): pass

    label("Function_17_4898")

    EventBegin(0x0)
    Fade(500)
    OP_68(14040, 800, 63300, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23800, 0)
    SetChrPos(0x101, 12730, 0, 61720, 45)
    SetChrPos(0x102, 14330, 0, 61720, 315)
    SetChrPos(0x109, 11530, 0, 62750, 90)
    SetChrPos(0x105, 15130, 0, 62750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4932")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_4932")

    OP_0D()

    #C0148
    ChrTalk(
        0x101,
        "#12P#00000Fこっちはランディの部屋だな。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#00100Fランディは今、\x01",
            "ベルガード門の部隊と\x01",
            "リハビリ訓練の真っ最中なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        (
            "#10305Fああ、確か教団事件で\x01",
            "例のクスリを盛られてたんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x109,
        (
            "#6P#10103Fうん……\x01",
            "後遺症というほど酷いものが\x01",
            "残ったわけじゃないけど。\x02\x03",

            "#10108F体力とカンを取り戻すのに\x01",
            "しばらく時間がかかるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#12P#00003Fそうか……\x01",
            "警備隊も早く立ち直ってほしいな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B1E")

    #C0153
    ChrTalk(
        0x1A5,
        "#12P#01100Fランディも早く帰ってこないかなー。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#00100Fふふ、本当にね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B5C")

    label("loc_4B1E")


    #C0155
    ChrTalk(
        0x102,
        (
            "#00100Fそうね、ランディにも\x01",
            "早く帰ってきてもらいたいし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B5C")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_17_4898 end

    def Function_18_4B74(): pass

    label("Function_18_4B74")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9B")
    Call(0, 21)
    Return()

    label("loc_4B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4BE0")
    TalkBegin(0xFF)
    SetChrName("")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "端末の導力は落ちている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    label("loc_4BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D14")
    TalkBegin(0xFF)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "端末の導力は落ちている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D10")

    #C0158
    ChrTalk(
        0x101,
        (
            "#00003F……どうやら導力そのものが\x01",
            "来ていないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#00200Fとりあえず、\x01",
            "壊されるようなことがなくて\x01",
            "よかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#00300Fま、端末を使いたきゃ\x01",
            "メルカバでってことだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00000Fそうだな、\x01",
            "ここは放っておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 5)

    label("loc_4D10")

    TalkEnd(0xFF)
    Return()

    label("loc_4D14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D2E")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_4D2E")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53EF")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4D80"),
        (1, "loc_4F32"),
        (2, "loc_53DA"),
        (3, "loc_53E2"),
        (SWITCH_DEFAULT, "loc_53EA"),
    )


    label("loc_4D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4D93")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4DAE")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4E07")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("自動アナウンス")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "現在、支援要請はありません。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_4F2D")

    label("loc_4E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E22")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E5D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E4B")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_4E58")

    label("loc_4E4B")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_4E58")

    Jump("loc_4F2D")

    label("loc_4E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E76")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4E84")
    Jump("loc_4F2D")

    label("loc_4E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EA1")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_4EBE")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4ED7")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4F0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_4EFB")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_4F06")

    label("loc_4EFB")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_4F06")

    Jump("loc_4F2D")

    label("loc_4F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_4F22")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4F22")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_4F2D")

    Jump("loc_53EA")

    label("loc_4F32")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_500F")
    SetChrName("自動アナウンス")

    #A0163
    AnonymousTalk(
        0xFF,
        "こちらはクロスベル警察です。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_4FE8")

    #A0164
    AnonymousTalk(
        0xFF,
        "報告を承ります。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自動アナウンス")

    #A0165
    AnonymousTalk(
        0xFF,
        (
            "報告処理を終了します。\x01",
            "お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500A")

    label("loc_4FE8")


    #A0166
    AnonymousTalk(
        0xFF,
        "報告可能な依頼はありません。\x02",
    )

    CloseMessageWindow()

    label("loc_500A")

    Jump("loc_53CC")

    label("loc_500F")

    SetChrName("受付嬢フラン")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5063")
    Sound(3062, 255, 100, 0)    #voice#Fran

    #A0167
    AnonymousTalk(
        0xFF,
        "#26Aはい、こちらクロスベル警察です～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_508F")

    label("loc_5063")

    Sound(3061, 255, 100, 0)    #voice#Fran

    #A0168
    AnonymousTalk(
        0xFF,
        "#29A皆さん、どうもお疲れさまですー。\x02",
    )

    CloseMessageWindow()

    label("loc_508F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_52D8")
    Sound(3067, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0169
    AnonymousTalk(
        0xFF,
        "#27Aそれでは報告を承りますね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5263")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_5100"),
        (13, "loc_514A"),
        (12, "loc_5192"),
        (SWITCH_DEFAULT, "loc_51DC"),
    )


    label("loc_5100")

    Sound(3075, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            "#39Aクラス１ｓｔ――\x01",
            "ロイドさん、スゴすぎです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DC")

    label("loc_514A")

    Sound(3074, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            "#38Aクラス２ｎｄ──\x01",
            "ロイドさん、すごいです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DC")

    label("loc_5192")

    Sound(3073, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            "#33Aクラス３ｒｄ──\x01",
            "ロイドさん、やりましたね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DC")

    label("loc_51DC")

    Sound(3076, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            "#33A特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)    #voice#Fran

    #A0174
    AnonymousTalk(
        0xFF,
        (
            "#33Aお疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D0")

    label("loc_5263")

    Sound(3078, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0175
    AnonymousTalk(
        0xFF,
        "#17A報告は以上ですね～。\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)    #voice#Fran

    #A0176
    AnonymousTalk(
        0xFF,
        (
            "#38Aでは、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D0")

    SetScenarioFlags(0x0, 1)
    Jump("loc_53CC")

    label("loc_52D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_535D")
    Sound(3063, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            "#31Aあれっ……\x01",
            "先ほど報告されたばかりですよ？\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)    #voice#Fran

    #A0178
    AnonymousTalk(
        0xFF,
        "#35Aまた依頼を達成されたらお願いしますね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53CC")

    label("loc_535D")

    Sound(3065, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            "#38Aあれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)    #voice#Fran

    #A0180
    AnonymousTalk(
        0xFF,
        "#20Aまたよろしくお願いしますー。\x02",
    )

    CloseMessageWindow()

    label("loc_53CC")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_53EA")

    label("loc_53DA")

    Call(0, 20)
    Jump("loc_53EA")

    label("loc_53E2")

    Call(0, 19)
    Jump("loc_53EA")

    label("loc_53EA")

    Jump("loc_4D47")

    label("loc_53EF")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5435")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 24)
    Return()

    label("loc_5435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546D")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 27)
    Return()

    label("loc_546D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54AC")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 32)
    Return()

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54E4")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 39)
    Return()

    label("loc_54E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5571")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_553B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5536")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_5536")

    Jump("loc_556C")

    label("loc_553B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556C")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_556C")

    Jump("loc_55F2")

    label("loc_5571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_558A")
    SetScenarioFlags(0x168, 2)
    Call(0, 67)
    Jump("loc_55F2")

    label("loc_558A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C9")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 44)
    Return()

    label("loc_55C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_55E0")
    ClearScenarioFlags(0x22, 3)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_55E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_55F2")
    ClearScenarioFlags(0x22, 6)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_55F2")

    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 67)
    TalkEnd(0xFF)
    Return()

    # Function_18_4B74 end

    def Function_19_5605(): pass

    label("Function_19_5605")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5633")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_562E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_562E")

    Jump("loc_5943")

    label("loc_5633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5673")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_566E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_566E")

    Jump("loc_5943")

    label("loc_5673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_568B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5943")

    label("loc_568B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_56CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56C6")

    Jump("loc_5943")

    label("loc_56CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5755")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_571E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5719")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5719")

    Jump("loc_5750")

    label("loc_571E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5750")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5750")

    Jump("loc_5943")

    label("loc_5755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_578E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5789")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5789")

    Jump("loc_5943")

    label("loc_578E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_57A6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5943")

    label("loc_57A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_57ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57E8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57E8")

    Jump("loc_5943")

    label("loc_57ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_5834")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_582F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_582F")

    Jump("loc_5943")

    label("loc_5834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_586D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5868")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5868")

    Jump("loc_5943")

    label("loc_586D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_58E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_58B6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58B1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58B1")

    Jump("loc_58E1")

    label("loc_58B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58E1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58E1")

    Jump("loc_5943")

    label("loc_58E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_5918")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5913")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5913")

    Jump("loc_5943")

    label("loc_5918")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5943")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5943")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5995")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての支援要請を確認してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5995")

    Return()

    # Function_19_5605 end

    def Function_20_5996(): pass

    label("Function_20_5996")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_59B8")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B8")
    ClearScenarioFlags(0x2A, 0)

    label("loc_59B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_59D5")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59D5")
    ClearScenarioFlags(0x2A, 1)

    label("loc_59D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_59F2")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59F2")
    ClearScenarioFlags(0x2A, 2)

    label("loc_59F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_5A0F")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0F")
    ClearScenarioFlags(0x2A, 3)

    label("loc_5A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_5A2C")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A2C")
    ClearScenarioFlags(0x2A, 4)

    label("loc_5A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_5A49")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A49")
    ClearScenarioFlags(0x2A, 5)

    label("loc_5A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_5A55")
    SetScenarioFlags(0x2A, 6)

    label("loc_5A55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA7")
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_5B22")

    label("loc_5AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AF9")
    OP_24(0x80)
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_5B22")

    label("loc_5AF9")

    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_5B22")

    Return()

    # Function_20_5996 end

    def Function_21_5B23(): pass

    label("Function_21_5B23")

    EventBegin(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SoundLoad(939)
    OP_68(16740, 1750, 10380, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24570, 0)
    SetChrPos(0x101, 15000, 850, 10900, 90)
    SetChrPos(0x102, 15970, 850, 9800, 45)
    SetChrPos(0x109, 14390, 850, 9310, 90)
    SetChrPos(0x105, 16500, 850, 8270, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00004Fロバーツ主任によると、\x01",
            "この記憶結晶を端末に\x01",
            "インストールするんだったな。\x02\x03",

            "#00000Fそれじゃあ……\x01",
            "よろしく頼むよエリィ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#12P#00100Fええ、やってみるわ。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィは導力端末に\x01",
            "『ポムっと！』β版をインストールした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    Sound(836, 0, 100, 0)
    Sleep(1000)
    Sound(939, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AB)
    Sound(839, 0, 100, 0)
    Sleep(500)
    Sound(839, 0, 100, 0)

    #C0185
    ChrTalk(
        0x102,
        (
            "#12P#00104Fこれでよし、と……\x02\x03",

            "#00100Fもらっていたロバーツ主任の\x01",
            "アカウントも入力しておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x105,
        "#12P#10302Fへえ、結構手際がいいじゃない。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x109,
        (
            "#6P#10109Fほんとエリィさんって、\x01",
            "色々なことに詳しいですよね。\x02\x03",

            "#10100F政治や法律のことなんかにも\x01",
            "知識も豊富みたいですし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)
    Sleep(300)

    #C0188
    ChrTalk(
        0x102,
        (
            "#11P#00102Fふふ、これに関しては\x01",
            "ティオちゃんがやっているのを\x01",
            "見ていたというだけだから。\x02\x03",

            "#00104F説明書なんかもあったし、\x01",
            "よく読めばそんなに\x01",
            "難しいことでもなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0189
    ChrTalk(
        0x101,
        (
            "#5P#00002Fいや、でも正直助かるよ。\x02\x03",

            "#00006F俺なんか、やっと端末の\x01",
            "キーボードに慣れたくらいだからさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ、どういたしまして。\x02\x03",

            "#00100Fそれで……ロバーツ主任に\x01",
            "連絡を入れればいいのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        "#5P#00000Fああ、早速かけてみるよ。\x02",
    )

    CloseMessageWindow()

    def lambda_5FFB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FFB)
    Sleep(50)

    def lambda_600B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_600B)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──やあ、ロイド君。\x01",
            "うまくインストールできたかな？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0193
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000Fええ、大丈夫です。\x01",
            "次はどうすれば？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それじゃ、ひとつ\x01",
            "僕と対戦してみようか。\x02\x03",

            "端末から『ポムっと！』を\x01",
            "起動してみてくれ。\x02\x03",

            "そこに僕のアカウントが\x01",
            "表示されるはずだから、\x01",
            "それを選択すると対戦できるよ。\x02\x03",

            "……そうだ、折角だから\x01",
            "支援課のリーダーである君が\x01",
            "代表として対戦してくれないかい？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0195
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F？？？\x01",
            "ええ、判りました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)

    #C0196
    ChrTalk(
        0x102,
        "#12P#00100Fそれじゃあ席を替わるわね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x14, 0x1F4)

    def lambda_62D4():
        OP_9B(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62D4)
    Sleep(200)

    def lambda_62EC():
        OP_95(0xFE, 15970, 850, 9800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62EC)

    def lambda_6306():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6306)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x5)
    Sleep(500)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふ、開発者である\x01",
            "この僕に勝てるかな……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("ロバーツの声")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4Sティオちゃんを任せられる男か……\x01",
            "改めて確かめさせてもらうよ！#3S\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0199
    ChrTalk(
        0x109,
        (
            "#6P#10112F……何だか本音が\x01",
            "聞こえてきたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#12P#10309Fアハハ、\x01",
            "結構な親バカみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#6P#00006Fえっと、わざわざ支援課に\x01",
            "依頼してきたのって……？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あはは、いやいや……\x01",
            "せっかくの勝負だし、\x01",
            "ちょっと気合いを入れただけさ。\x02\x03",

            "それじゃ、さっそく\x01",
            "ゲームを始めてみようか！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x27, 2)
    OP_29(0x6C, 0x1, 0x1)
    StopSound(128, 500, 40)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()

    label("loc_65C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6654")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65FD")
    Call(0, 20)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_664F")

    label("loc_65FD")


    #A0203
    AnonymousTalk(
        0x101,
        (
            "#0000Fロバーツ主任が待ってるし、\x01",
            "さっそく『ポムっと！』を起動してみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_664F")

    Jump("loc_65C5")

    label("loc_6654")

    OP_E5(0x6)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 22)
    Return()

    # Function_21_5B23 end

    def Function_22_6678(): pass

    label("Function_22_6678")

    EventBegin(0x0)
    SoundLoad(803)
    SoundLoad(128)
    Sound(128, 2, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_670B")
    OP_2C(0x6C, 0x1)

    #C0204
    ChrTalk(
        0x101,
        (
            "#6P#00009Fよし、なんとか勝てた……！\x02\x03",

            "#00004F（うーん、結構\x01",
            "  楽しいかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x2)
    Jump("loc_6769")

    label("loc_670B")


    #C0205
    ChrTalk(
        0x101,
        (
            "#6P#00006F……負けてしまったか。\x02\x03",

            "#00001F（うーん、なんだか\x01",
            "  無性に悔しいな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x3)

    label("loc_6769")


    #C0206
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ、なんだか結構\x01",
            "ハマっちゃったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x109,
        (
            "#6P#10105F……あの、傍目に見てた\x01",
            "印象なんですけど……\x02\x03",

            "#10106Fロバーツ主任って、\x01",
            "もしかして強くないのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそうだね、開発者なのに\x01",
            "強さ的には初心者の君と\x01",
            "大して変わらないんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0209
    ChrTalk(
        0x101,
        (
            "#5P#00012Fい、いや……\x01",
            "さすがに手加減を\x01",
            "してくれたんじゃないか？\x02\x03",

            "#00003Fレベルをある程度合わせないと\x01",
            "テストにならなそうだし……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0210
    ChrTalk(
        0x101,
        "#6P#00000Fはい、こちら特務支援──\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──いやあ、\x01",
            "今のはいい勝負だったね！\x02\x03",

            "まさに歴史に残る大勝負！\x01",
            "興奮しっぱなしだよ！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0212
    ChrTalk(
        0x101,
        (
            "#6P#00006F（どうやら真剣勝負のつもり\x01",
            "  だったみたいだな……）\x02\x03",

            "#00012Fそ、それで……\x01",
            "テストの結果はどうでした？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、バッチリだよ！\x02\x03",

            "市内でやる分には\x01",
            "目立ったラグもないし、\x01",
            "通信状態も良好だ。\x02\x03",

            "申し分ない大成功といえるね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0214
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそうですか……\x01",
            "それはよかったです。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "インストールしたβ版は、\x01",
            "近いうちにリリース版に\x01",
            "アップデートしておくよ。\x02\x03",

            "プログラムの配布が始まったら、\x01",
            "対戦できる人も増えていくだろう。\x02\x03",

            "色んな人とアカウントを交換して、\x01",
            "存分に楽しんでくれると嬉しいよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D5C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D01")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もちろん、この僕だって\x01",
            "いつかリベンジするつもりだしね！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6D5C")

    label("loc_6D01")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もちろん、今日のリベンジも\x01",
            "いつだって受け付けるからね！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6D5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DCB")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もちろん、この僕だって\x01",
            "いつかリベンジするつもりだしね！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6E26")

    label("loc_6DCB")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もちろん、今日のリベンジも\x01",
            "いつだって受け付けるからね！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6E26")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#00012Fは、はは……\x01",
            "お手柔らかに。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いや、協力してくれて\x01",
            "本当にありがとう。\x02\x03",

            "僕は別の仕事があるから\x01",
            "これで失礼するよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0222
    ChrTalk(
        0x101,
        (
            "#6P#00000Fどういたしまして。\x01",
            "また何かあったら\x01",
            "いつでもご連絡ください。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ロバーツの声")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、そうするよ。\x01",
            "──それじゃあね！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    #C0224
    ChrTalk(
        0x101,
        (
            "#00004Fふぅ……なんとか\x01",
            "うまく行ったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、お疲れさま。\x02\x03",

            "#00104Fなんていうか、\x01",
            "主任らしい依頼だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#00012Fはは、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x105,
        (
            "#12P#10300Fともあれ、これからも\x01",
            "このゲームは楽しめそうだね。\x02\x03",

            "#10309Fこの際だから、クロスベル一の\x01",
            "ポムっと！マスターを\x01",
            "目指してみたらどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#00006Fいや、さすがにティオには\x01",
            "絶対に敵わないだろうけど……\x02\x03",

            "#00000Fでも、仕事の合間に\x01",
            "息抜きがてら練習くらいは\x01",
            "しておいてもいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x109,
        "#6P#10100Fふふっ、そうですね。\x02",
    )

    CloseMessageWindow()
    StopSound(128, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【βテストの参加依頼】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_29(0x6C, 0x1, 0x4)
    OP_29(0x6C, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x11)
    SetChrPos(0x0, 14970, 850, 8800, 225)
    OP_24(0x323)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(128, 2, 50, 0)
    EventEnd(0x5)
    Return()

    # Function_22_6678 end

    def Function_23_724F(): pass

    label("Function_23_724F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis011.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis347.itp")
    OP_68(17000, 1650, 10500, 0)
    MoveCamera(19, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 15200, 850, 10900, 90)
    SetChrPos(0x102, 16300, 850, 10200, 45)
    SetChrPos(0x109, 17200, 850, 8000, 315)
    SetChrPos(0x105, 16200, 850, 7700, 0)
    SetCameraDistance(23500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(836, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(72, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #A0231
    AnonymousTalk(
        0x102,
        (
            "#00104F──うん。\x01",
            "ちゃんと来てるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0232
    AnonymousTalk(
        0x109,
        "#10100Fこれが……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0233
    AnonymousTalk(
        0x105,
        (
            "#10302F特務支援課が処理する\x01",
            "『支援要請』ってわけだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x101, 0x109, 0)
    Sleep(300)

    #A0234
    AnonymousTalk(
        0x101,
        (
            "#00004Fああ、基本は一日一回、\x01",
            "まとめて送られてくる決まりだ。\x02\x03",

            "#00000Fどこまでやるかは\x01",
            "こちらの裁量に任されてるけど……\x02\x03",

            "この『緊急』と書かれているものは\x01",
            "必ずやっておいた方がいいだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0235
    AnonymousTalk(
        0x105,
        (
            "#10304Fなるほど、合理的だね。\x02\x03",

            "#10300F期間が長めに取られてるものは\x01",
            "次の日に回してもいいって事かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0236
    AnonymousTalk(
        0x101,
        "#00000Fああ、そうなるかな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0237
    AnonymousTalk(
        0x102,
        (
            "#00104F一応、毎日チェックしたら\x01",
            "提示された期間も変わっていくから。\x02\x03",

            "#00100Fそれと『捜査手帳』をチェックすれば\x01",
            "そのあたりの状況も確認できるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0238
    AnonymousTalk(
        0x109,
        "#10105F捜査手帳というと……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(24000, 0)
    FadeToBright(0, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    #C0239
    ChrTalk(
        0x109,
        (
            "#12P#10100Fエリィさんが時々書き込んでいた\x01",
            "黒い手帳のことですね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0240
    ChrTalk(
        0x102,
        "#5P#00100Fええ、これね。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0241
    AnonymousTalk(
        0x101,
        (
            "#00003F基本的に、捜査や支援要請で\x01",
            "何か進展があったらこれに書き込む。\x02\x03",

            "そうすることで、複数の案件を\x01",
            "管理することが可能になるわけさ。\x02\x03",

            "#00000Fあと、戦術オーブメント──\x01",
            "《エニグマ》についての説明も\x01",
            "フォローしてくれているんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0242
    AnonymousTalk(
        0x105,
        (
            "#10305Fふーん、割と便利じゃないか。\x02\x03",

            "#10304Fま、いずれはそんな手帳も\x01",
            "導力化されそうな気がするけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0243
    AnonymousTalk(
        0x102,
        (
            "#00102Fそうね……\x01",
            "ティオちゃんからそういう研究も\x01",
            "されていると聞いた事があるわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0244
    AnonymousTalk(
        0x109,
        (
            "#10112Fうーん、そこまで導力化されるのは\x01",
            "何だか抵抗があるっていうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0245
    AnonymousTalk(
        0x101,
        (
            "#00002F確かに、紙とペンの方が\x01",
            "しっくりくるのは同感だよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0246
    ChrTalk(
        0x101,
        (
            "#00004F#5P──まあ、ざっと説明すると\x01",
            "これが支援課の基本スタイルだ。\x02\x03",

            "#00000Fまずは端末に来ている支援要請を\x01",
            "一通りチェックしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x109,
        "#12P#10102F了解しました！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x105,
        "#12P#10309Fフフ、開けてのお楽しみだね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※支援課に置かれている端末を○ボタンで調べて\x01",
            "  項目から［支援要請の確認］を選択すると、\x01",
            "  ロイド達への仕事の依頼（クエスト）が一覧表示されます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※支援要請の中には、緊急度が高く、\x01",
            "　必ず行う必要があるものが存在します。\x01",
            "　こうしたものは『緊急』マークが付き、\x01",
            "　達成するとメインストーリーが進行します。\x02",
        )
    )

    CloseMessageWindow()

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※それ以外の支援要請は、\x01",
            "　必ずしも達成する必要はありませんが\x01",
            "　クリアすればＤＰとミラを獲得することができます。\x01",
            "　また、期限を過ぎると消滅するので注意してください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetScenarioFlags(0x126, 0)
    OP_29(0xA1, 0x4, 0x2)
    OP_29(0xA1, 0x1, 0x0)
    Call(0, 67)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x6, 1)
    OP_C9(0x0, 0x1000)
    OP_C9(0x0, 0x200000)
    EventEnd(0x5)
    Return()

    # Function_23_724F end

    def Function_24_7C66(): pass

    label("Function_24_7C66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis231.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis235.itp")
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 19000, 850, 4000, 270)
    OP_4B(0x8, 0xFF)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0252
    ChrTalk(
        0x109,
        (
            "#6P#10103F緊急２件に、\x01",
            "手配魔獣が２件ですか……\x02\x03",

            "#10101FエニグマⅡの件はともかく\x01",
            "もう一件はかなり特殊ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#00106F#11Pええ、あのレクターって人が\x01",
            "またクロスベルに来ているなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#6P#10303F《黒の競売会#10Rシュバルツオークション#》の時にいた\x01",
            "あのトボけたお兄さんだね。\x02\x03",

            "#10300Fどう考えてもタダ者じゃないとは\x01",
            "思ったけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)

    #A0255
    AnonymousTalk(
        0x101,
        (
            "#00003F……捜査一課で研修した時に\x01",
            "彼についてのファイルを閲覧した。\x02\x03",

            "#00001F帝国軍情報局所属、\x01",
            "レクター・アランドール特務大尉。\x02\x03",

            "帝国政府の二等書記官としての\x01",
            "肩書きも持っているらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0256
    AnonymousTalk(
        0x109,
        "#10108F諜報畑の人間ですか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0257
    ChrTalk(
        0x102,
        (
            "#00103F#11P政治的な工作も出来るような\x01",
            "情報将校みたいね。\x02\x03",

            "#00101F捉えどころがないのも\x01",
            "高度な韜晦#4Rとうかい#の技術なのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x105,
        (
            "#6P#10304F半分以上、素な気もするけど。\x02\x03",

            "#10302Fしかし帝国政府の書記官で\x01",
            "軍情報局の所属ってことは……\x02\x03",

            "あの有名な《鉄血宰相》の\x01",
            "腹心ってところなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#5P#00006F（どうしてそんな背景まで\x01",
            "  しれっと通じてるんだか……）\x02\x03",

            "#00001F──ああ、一課の情報によると\x01",
            "オズボーン宰相の懐刀の一人らしい。\x02\x03",

            "昨年、宰相と共にクロスベルを訪問して\x01",
            "非公式にハルトマン議長と\x01",
            "会談したことが確認されている。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#00108F#11Pそれは本人も言ってたわね。\x02\x03",

            "#00106F冗談みたいな口ぶりだったけど\x01",
            "まさか本当だったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        (
            "#6P#10106Fどう考えても一筋縄では\x01",
            "行かなさそうな人ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x105,
        (
            "#6P#10309Fフフ、面白そうじゃないか。\x02\x03",

            "#10300Fとなるとまずは市内での\x01",
            "支援活動が優先ってわけかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        (
            "#5P#00000Fああ、手配魔獣が１件、\x01",
            "街道に手配されているけど\x01",
            "そちらは後回しにしておこう。\x02\x03",

            "#00003F……ルバーチェの消滅から数ヶ月。\x02\x03",

            "#00001Fそろそろ裏社会で新たな動きが\x01",
            "起こっているのは確かみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#00108F#11P《黒月#4Rヘイユエ#》の動き……\x01",
            "それから帝国政府の動きね。\x02\x03",

            "#00101F月末に開かれる『通商会議』も\x01",
            "かなり影響していそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x105, 0x0)
    Sleep(300)

    #C0265
    ChrTalk(
        0x109,
        "#6P#10105F『通商会議』というと……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x105,
        (
            "#6P#10300F新市長が呼びかけた\x01",
            "首脳クラスが集まる国際会議だね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0267
    ChrTalk(
        0x102,
        "#00102F#11Pええ──\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)

    #A0268
    AnonymousTalk(
        0x102,
        (
            "#00104Fディーター・クロイス新市長。\x02\x03",

            "彼が主催する、帝国、共和国、\x01",
            "リベール、レミフェリアの首脳が\x01",
            "一堂に会する経済関連の国際会議。\x02\x03",

            "#00100F『西ゼムリア通商会議』というのが\x01",
            "正式名称ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0269
    AnonymousTalk(
        0x101,
        (
            "#00004Fまさか就任直後に\x01",
            "あんな大規模な国際会議の\x01",
            "開催を呼びかけるなんてな……\x02\x03",

            "#00000FさすがはＩＢＣの総裁を\x01",
            "兼ねているだけのことはあるか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0270
    ChrTalk(
        0x109,
        (
            "#6P#10109F直接お会いした事はないですけど\x01",
            "物凄いやり手って話ですよね。\x02\x03",

            "#10102Fそういえば、ワジ君は新市長に\x01",
            "お会いしたことがあるんだっけ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0271
    ChrTalk(
        0x105,
        (
            "#6P#10304Fああ、推薦状をもらった時にね。\x02\x03",

            "#10302Fいくら独立愚連隊とはいえ\x01",
            "警察の部署への推薦状を\x01",
            "不良少年にくれるなんてねぇ。\x02\x03",

            "#10309Fフフ、僕が言うのもなんだけど\x01",
            "気前がよすぎるオジサンだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#5P#00006Fいや、笑い事じゃないんだが。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#00111F#11Pおじさまはおじさまで\x01",
            "『ハッハッハッ、面白い子だね』\x01",
            "とか言ってたし……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    Sleep(300)

    #N0274
    NpcTalk(
        0x8,
        "課長の声",
        "おー、やってるみたいだな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(16000, 1850, 4000, 2000)
    MoveCamera(40, 19, 0, 2000)
    SetChrPos(0x8, 20000, 850, 4000, 270)

    def lambda_89A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_89A3)

    def lambda_89B4():
        OP_95(0xFE, 17000, 850, 4000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89B4)
    SetChrSubChip(0x105, 0x0)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_6F(0x79)

    #C0275
    ChrTalk(
        0x101,
        "#00005Fセルゲイ課長……\x02",
    )

    CloseMessageWindow()
    OP_68(12600, 1850, 6600, 4000)
    MoveCamera(35, 17, 0, 4000)
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 25)

    def lambda_8A3D():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8A3D)
    WaitChrThread(0x8, 1)

    def lambda_8A5B():
        OP_95(0xFE, 12700, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8A5B)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Fade(250)
    SetChrPos(0x109, 11100, 850, 5750, 90)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(812, 0, 100, 0)
    OP_0D()
    TurnDirection(0x109, 0x8, 500)

    #C0276
    ChrTalk(
        0x109,
        "#6P#10101Fお早うございます！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)
    Sleep(150)

    #C0277
    ChrTalk(
        0x8,
        (
            "#01003F#5Pああ、そのままでいい。\x02\x03",

            "#01000F基本的に支援課#6Rウ　チ#は放任主義でな。\x02\x03",

            "余程のことがないかぎり\x01",
            "俺の方からは口出ししないから\x01",
            "適当にやっていくといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        "#6P#10105Fは、はあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    Sound(812, 0, 100, 0)
    OP_0D()
    Sleep(200)

    #C0279
    ChrTalk(
        0x105,
        (
            "#6P#10309Fあはは。\x01",
            "理解のある上司ってわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#11P#00012F……うーん……\x01",
            "そう言えなくもないんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#11P#00111F課長の場合、理由の半分は\x01",
            "面倒くさいからですよね……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0282
    ChrTalk(
        0x8,
        (
            "#01004F#5Pクク、分かってんじゃねーか。\x02\x03",

            "#01002Fただまあ、今日は例外的に\x01",
            "俺の方から指令がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x101,
        "#00011F#11Pへ……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        "#00105F#11Pか、課長からですか？\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#01003F#5Pああ、一通り支援要請を\x01",
            "片付けてからでいい。\x02\x03",

            "#01000F警察学校に行ってもらう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x101,
        "#00005F#11P警察学校に……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x109,
        (
            "#6P#10100F西クロスベル街道の途中にある\x01",
            "演習場もある場所ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#01004F#5Pロイドとノエルにとっては\x01",
            "お馴染みの場所だったな。\x02\x03",

            "#01000Fこちらの準備が整ったら\x01",
            "エニグマで連絡する。\x02\x03",

            "それまでは市内を回りつつ\x01",
            "支援要請をこなしていくがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        "#00000F#11Pえっと……了解しました。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x102,
        "#00100F#11Pですが、一体どういう用件で？\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "#01002F#5Pクク、それは行ってからの\x01",
            "お楽しみってヤツだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2328, 0x2648, 0x1F4)
    Sleep(300)

    #C0292
    ChrTalk(
        0x8,
        (
            "#01006F#11Pそんじゃーな。\x01",
            "また後で連絡する。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(10600, 1850, 6600, 3000)

    def lambda_8FFF():
        OP_95(0xFE, 9000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8FFF)
    WaitChrThread(0x8, 1)

    def lambda_901D():
        OP_95(0xFE, 2000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_901D)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    OP_0D()

    #C0293
    ChrTalk(
        0x109,
        "#6P#10105Fえーっと……\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        (
            "#00106F#11Pノエルさん……\x01",
            "非常に申し訳ないんだけど\x01",
            "これが支援課のスタイルなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#5P#00006Fまあ、好意的に考えれば\x01",
            "俺たちの自主性と判断力を\x01",
            "育ててくれているんだろうけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    #C0296
    ChrTalk(
        0x109,
        (
            "#6P#10109Fな、なるほど！\x01",
            "さすがはセルゲイ課長ですね！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、物は言いようだね。\x02\x03",

            "#10302Fで？\x01",
            "さっそく街に出るのかい？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#00004Fああ、そうしよう。\x02\x03",

            "#00005F……そういえば、キーアが\x01",
            "日曜学校に行くって言ってたな。\x02\x03",

            "#00000F課長も出かけた事だし、\x01",
            "一緒に出た方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        (
            "#00102F#11Pそうね、３階に上がって\x01",
            "キーアちゃんに声を掛けましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_4C(0x8, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetScenarioFlags(0x126, 1)
    OP_29(0xA1, 0x1, 0x1)
    OP_32(0x6, 0x0, 0x32)
    OP_42(0x6, 0x3E9, 0xFF)
    Call(0, 67)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_24_7C66 end

    def Function_25_935E(): pass

    label("Function_25_935E")

    Sleep(1500)
    SetChrSubChip(0x109, 0x0)
    Sleep(700)
    SetChrSubChip(0x102, 0x2)
    Sleep(300)
    SetChrSubChip(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    SetChrSubChip(0x109, 0x1)
    Return()

    # Function_25_935E end

    def Function_26_9382(): pass

    label("Function_26_9382")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    OP_68(12600, 2350, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 12700, 850, 8400, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    OP_68(12600, 1850, 6600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    #C0300
    ChrTalk(
        0x8,
        (
            "#01006F#5Pどうやら今日は一日、\x01",
            "小雨が降り続くみたいだな。\x02\x03",

            "#01000F夜にはちょいと荒れるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00003Fそうですか……\x02\x03",

            "#00000F導力車が支給されたから\x01",
            "一通り郊外も回ってみようかと\x01",
            "思ったんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#6P#10304Fまあ、ドライブ日和って\x01",
            "感じじゃないのは確かだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x109,
        "#6P#10106Fうう……残念です。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#00108F#12Pところで……昨日私たちが\x01",
            "街道で遭遇した人については\x01",
            "まだ続報はないんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "#01003F#5Pああ、一課でも\x01",
            "まだ確認できていないようだ。\x02\x03",

            "#01001Fツァオといい、レクターって奴といい\x01",
            "一筋縄じゃいかない連中ばかりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00008Fええ………\x02\x03",

            "#00006F……昨日会った男は、それ以上に\x01",
            "危険な雰囲気をまとっていました。\x02\x03",

            "#00001F落ち着いているけど、得体の知れない\x01",
            "凶暴さをにじませているというか……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0307
    ChrTalk(
        0x109,
        (
            "#6P#10103F確かに……\x01",
            "虎みたいな雰囲気がありましたね。\x02\x03",

            "#10101Fその気になればあっという間に\x01",
            "襲われて食べられちゃいそうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x102,
        (
            "#00106F#12Pゾッとしない喩#2Rたと#えだけど\x01",
            "確かにそんな雰囲気だったわね。\x02\x03",

            "#00108Fテロリストか猟兵……\x01",
            "どちらも考えられそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x105,
        (
            "#6P#10308Fふむ……\x02\x03",

            "#10304Fとなると旧市街あたりで\x01",
            "情報収集するといいかもね。\x02\x03",

            "#10300F《ナインヴァリ》の女主人とか\x01",
            "色々知ってそうな気もするし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)

    #C0310
    ChrTalk(
        0x101,
        (
            "#00005F#11P交換屋のアシュリーさんか。\x02\x03",

            "#00001F元武器商人で、裏の世界にも\x01",
            "色々詳しいみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        (
            "#00101F#11P確かに、そういう意味では\x01",
            "訪ねてみる価値はありそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#01004F#5Pま、せいぜい頑張れ。\x02\x03",

            "#01000Fただ、お前たちがあくまで\x01",
            "支援課だってことは忘れるな。\x02\x03",

            "防諜#4Rぼうちょう#方面に気を張りすぎてると\x01",
            "本来の役割を見失うぞ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    Sleep(200)

    #C0313
    ChrTalk(
        0x101,
        "#00005Fわ、分かりました。\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    OP_68(14900, 1850, 6600, 3000)

    def lambda_9AE8():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9AE8)
    WaitChrThread(0x8, 1)

    def lambda_9B06():
        OP_95(0xFE, 18000, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B06)
    SetChrSubChip(0x105, 0x0)
    Sleep(500)
    SetChrSubChip(0x109, 0x2)
    Sleep(700)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    ClearMapObjFlags(0x0, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_9B5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9B5F)

    def lambda_9B70():
        OP_95(0xFE, 19500, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B70)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Fade(500)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0314
    ChrTalk(
        0x101,
        (
            "#5P#00006F……とりあえず端末で\x01",
            "支援要請をチェックしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#00100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetScenarioFlags(0x128, 1)
    OP_29(0xA1, 0x1, 0xC)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_26_9382 end

    def Function_27_9CDC(): pass

    label("Function_27_9CDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14100, 850, 9500, 45)
    SetChrPos(0x105, 15600, 850, 8000, 45)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0316
    ChrTalk(
        0x101,
        (
            "#00000F#6P出ている緊急要請は\x01",
            "全てクロスベル市内だな。\x02\x03",

            "#00004Fこの程度の数だったら\x01",
            "一通り片付けてもよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        (
            "#00104F#12P財団の依頼も、ティオちゃんが\x01",
            "関係しているかもしれないし……\x02\x03",

            "#00102Fモモちゃんの依頼も\x01",
            "できれば聞いてあげたいわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0318
    ChrTalk(
        0x109,
        (
            "#6P#10100Fでは、緊急要請を片付けながら\x01",
            "旧市街の交換屋を訪ねるんですね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EC4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9EC4)
    Sleep(100)

    def lambda_9ED4():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9ED4)
    Sleep(50)

    def lambda_9EE4():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9EE4)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0319
    ChrTalk(
        0x101,
        "#00002F#5Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x105,
        (
            "#12P#10304Fま、雨も降っている事だし、\x01",
            "ボチボチやって行こうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetScenarioFlags(0x128, 2)
    OP_29(0xA1, 0x1, 0xD)
    Call(0, 67)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7562")
    ReplaceBGM("ed7101", "ed7562")
    ReplaceBGM("ed7116", "ed7562")
    ReplaceBGM("ed7117", "ed7562")
    Sleep(500)
    PlayBGM("ed7562", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_27_9CDC end

    def Function_28_9FB1(): pass

    label("Function_28_9FB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x140, 0)
    OP_29(0xA3, 0x4, 0x2)
    OP_29(0xA3, 0x1, 0x0)
    OP_C9(0x0, 0x1000)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_32(0x6, 0x0, 0x3A)
    OP_42(0x6, 0x3EB, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 65890, 0, 1800, 225)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 18)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0321
    ChrTalk(
        0x101,
        (
            "#00003F#5P緊急度が高そうなのは\x01",
            "警備隊とウルスラ病院からか……\x02\x03",

            "#00002Fでも、あのダグラス教官から\x01",
            "呼ばれることになるなんてな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0322
    ChrTalk(
        0x102,
        (
            "#00105F#11Pダグラス教官？\x01",
            "警備隊の副司令になった方よね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A237():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A237)
    Sleep(100)

    def lambda_A247():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A247)
    Sleep(50)

    def lambda_A257():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A257)
    WaitChrThread(0x101, 2)

    #C0323
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ、副司令になられる前は\x01",
            "警察学校の教官をされていたんだ。\x02\x03",

            "#00000F基礎体力の向上から格闘訓練、\x01",
            "トンファーによる制圧術なんかを\x01",
            "みっちり叩き込まれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x109,
        (
            "#6P#10102F元々、警備隊のホープとして\x01",
            "期待されていた方だったんです。\x02\x03",

            "#10106Fでも、あの前警備隊司令に疎まれて\x01",
            "閑職#4Rかんしょく#に回されたらしくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#6P#00304F俺も演習で世話になったが\x01",
            "凄まじくタフな兄さんだよな。\x02\x03",

            "#00302F戦闘力でいったら多分、\x01",
            "警備隊Ｎｏ．１なんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A42E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A42E)
    Sleep(50)

    def lambda_A43E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A43E)
    WaitChrThread(0x101, 2)

    #C0326
    ChrTalk(
        0x102,
        (
            "#00104F#11Pなるほど……\x01",
            "ずいぶん凄そうな方ね。\x02\x03",

            "#00100Fでも、警備隊との関係を考えると\x01",
            "一度お会いしておきたいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#00002F#5Pああ、挨拶がてら行ってみよう。\x02\x03",

            "#00003Fそれとウルスラ病院に\x01",
            "新たに赴任した教授からか……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#6P#00306Fヨアヒムに代わって薬学と神経科の\x01",
            "両部門を引き継ぐ人物……\x02\x03",

            "#00301Fま、どうしても警戒しちまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x105,
        (
            "#12P#10304Fでも、このセイランドっていうのは\x01",
            "どこかで聞いた事があるね。\x02\x03",

            "#10300F確かレミフェリアあたりで\x01",
            "有名な名前じゃなかったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#00102F#11Pレミフェリアの医療メーカーで\x01",
            "セイランド社という所があるわね。\x02\x03",

            "大公家とも縁のある名家だけど\x01",
            "その関係者の可能性はあるかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00006F#5Pうーん、そうなるとそこまで\x01",
            "怪しい人物じゃなさそうだけど……\x02\x03",

            "#00001F──まあいい。\x01",
            "例の薬についての話もあるみたいし、\x01",
            "ウルスラ病院にも行かなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        (
            "#12P#10309Fフフ、君の憧れの\x01",
            "お姉さんもいるみたいだしね。\x02\x03",

            "#10302Fナース服が凄まじく似合ってる\x01",
            "聖女様みたいなヒトなんだって？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A7F7():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7F7)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0333
    ChrTalk(
        0x101,
        (
            "#00005F#5Pなっ……！？\x02\x03",

            "#00012Fい、いや、セシル姉は昔から\x01",
            "お世話になっているだけで……\x02\x03",

            "#00011F──ていうかワジ！？\x01",
            "面識ないのに何で知ってるんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x104,
        "#6P#00309Fワリワリ、俺が話しちまった。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0335
    ChrTalk(
        0x101,
        "#00013F#5Pくっ、ランディ……お前な！\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#00111F#11P（……ロイド。\x01",
            "  ちょっと動揺しすぎだわ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        (
            "#6P#10112F（結構、図星みたいですね……）\x02\x03",

            "#10102F（確かに素敵な人だったから\x01",
            "  判る気がしますけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00003F#5P……コホン。\x01",
            "まあ、それはそれとして。\x02\x03",

            "#00000Fその先生に会う前にセシル姉には\x01",
            "話を聞いておきたいかな。\x02\x03",

            "#00008F……ヨアヒムの残した傷跡#4Rダメージ#から\x01",
            "病院が立ち直れているかも心配だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#00106F#11Pそうね……\x02\x03",

            "#00100Fあ、でもシズクちゃんは\x01",
            "今日は街に来ているのよね？\x02\x03",

            "さっきキーアちゃんが\x01",
            "ギルドに遊びに行ってたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ、今日は一日\x01",
            "シズクちゃんと遊ぶんだって\x01",
            "張り切って出かけて行ったな。\x02\x03",

            "#00002Fギルドにいるだろうから\x01",
            "時間があったら行ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#00109F#11Pええ、そうしましょう。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x105,
        (
            "#12P#10305Fシズクっていうのは\x01",
            "あの《風の剣聖》の娘だっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        (
            "#6P#00304Fああ、ちょうどキー坊と\x01",
            "同じくらいのトシになるな。\x02\x03",

            "#00302Fあのお堅いオッサンの娘とは\x01",
            "思えないくらいの良い子だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_AD07")

    #C0344
    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふっ……\x01",
            "シズクちゃん、可愛いですよね。\x02\x03",

            "#10102Fフランも会った事があるらしくて\x01",
            "すごく騒いでいましたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD88")

    label("loc_AD07")


    #C0345
    ChrTalk(
        0x109,
        (
            "#6P#10109F噂は聞いていますけど\x01",
            "すごく可愛い子みたいですね。\x02\x03",

            "#10102Fフランも会った事があるらしくて\x01",
            "すごく騒いでいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD88")


    #C0346
    ChrTalk(
        0x105,
        (
            "#12P#10300Fフフ、なるほどね。\x02\x03",

            "#10304Fとなると、今日は挨拶がてら\x01",
            "クロスベル各地を回るわけだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)
    Sleep(300)

    #C0347
    ChrTalk(
        0x105,
        (
            "#11P#10302F──《赤い星座》って連中の\x01",
            "動向なんかも探りながら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_AE8F():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AE8F)
    Sleep(50)

    def lambda_AE9F():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AE9F)
    Sleep(50)

    def lambda_AEAF():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AEAF)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    #C0348
    ChrTalk(
        0x101,
        "#00013F#5Pワジ……！\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x109,
        "#6P#10101Fき、君ねぇ……！\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#6P#00306F……ああ、いい。\x01",
            "コイツの突っ込みももっともだ。\x02\x03",

            "#00303F元、身内が言うのもなんだが\x01",
            "あの連中は正直シャレにならねぇ。\x02\x03",

            "#00301F多分、旧鉱山に爆薬を仕掛けたのも\x01",
            "連中の可能性が高いだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AFD3():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFD3)
    Sleep(50)

    def lambda_AFE3():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AFE3)
    Sleep(50)

    def lambda_AFF3():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AFF3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    #C0351
    ChrTalk(
        0x101,
        "#00005F#5Pランディ……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#00108F#11Pその、そんな風に\x01",
            "決め付けなくてもいいんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        (
            "#6P#00303F叔父貴とシャーリィ──\x01",
            "あの２人のことはよく知っている。\x02\x03",

            "#00308F断言はできねぇが……\x01",
            "支援課の力量を試したんだろう。\x02\x03",

            "#00301F古巣を捨てた俺が流れ着いたのが\x01",
            "どの程度やれる#6R㈲　㈲　㈲#場所なのかをな。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        "#00101F#11P……！\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x109,
        "#5P#10108Fそ、それだけのために……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#00008F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x105,
        (
            "#11P#10303F別に害意があるわけじゃない。\x02\x03",

            "#10300F単なる好奇心であんなことを\x01",
            "やれるような連中ってわけだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x104,
        (
            "#6P#00306Fああ、あの程度のトラップなんざ\x01",
            "連中には挨拶程度ってことだ。\x02\x03",

            "#00301Fその意味じゃ、せっかく戻りはしたが\x01",
            "俺一人で連中の動向を調べた方が──\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#00006F#5P──だったら尚更だ。\x02\x03",

            "#00008F確かに《赤い星座》というのは\x01",
            "放置できる連中じゃないだろう。\x02\x03",

            "クロスベルへの来訪目的にしても\x01",
            "帝国政府との関係にしても\x01",
            "いずれ突き止めていく必要がある。\x02\x03",

            "#00001Fただし……\x01",
            "あくまで特務支援課としてだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        "#6P#00305Fロイド……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#00003F#5P俺たちにはランディが必要だし、\x01",
            "ランディを一人にするつもりもない。\x02\x03",

            "#00001Fランディだって、一人で動いて\x01",
            "何かできる見込みは無いんだろう？\x02\x03",

            "だったら……\x01",
            "勝手に動くなんて言わないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        "#6P#00308F………………………………\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        (
            "#11P#10309Fふふ、相変わらず\x01",
            "大した口説き文句だねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x109,
        (
            "#5P#10101Fで、でもその通りですよ！\x02\x03",

            "こういう時に力を合わせるのが\x01",
            "特務支援課なんですよね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x102,
        (
            "#00104F#11Pええ、勿論よ。\x02\x03",

            "#00100Fあの教団事件でも、私たちは\x01",
            "全員の力を合わせて立ち向かった。\x02\x03",

            "ランディ、今回も同じではないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x104,
        (
            "#6P#00304F……はは。\x02\x03",

            "#00302F悪ぃ、つまらないことを\x01",
            "言いかけたみてぇだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ、まったくだ。\x02\x03",

            "#00000Fとにかく車もあることだし、\x01",
            "今日は支援要請を片付けながら\x01",
            "郊外を回ってみよう。\x02\x03",

            "ベルガード門やアルモリカ村にも\x01",
            "足を延ばしてもいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B6D6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B6D6)
    Sleep(50)

    def lambda_B6E6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B6E6)
    Sleep(150)

    #C0368
    ChrTalk(
        0x102,
        (
            "#00104F#11Pそうね、久しぶりだし……\x02\x03",

            "#00105Fそういえば、ソーニャ司令の方は\x01",
            "ベルガード門にいらっしゃるのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x109,
        (
            "#6P#10102Fええ、その筈です。\x02\x03",

            "通商会議に向けての対応で\x01",
            "忙しくされていると思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#6P#00304Fミレイユのヤツもいるはずだし、\x01",
            "そっちに顔を出してもいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ……\x01",
            "それじゃあ出かけるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パーティが４人を超えた場合、\x01",
            "余った人員は『サポートメンバー』に\x01",
            "登録される事になります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『サポートメンバー』は戦域外に待機し、\x01",
            "たまにＡＴ順に現れ、出番が回ってくると\x01",
            "様々な支援行動を取ってくれます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0374
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アタックエンカウントで背後を取られると、\x01",
            "『サポートメンバー』も含めて隊列が乱されます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『サポートメンバー』の装備も、\x01",
            "準備を怠らないようにしましょう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パーティメンバーの入れ替えは\x01",
            "キャンプメニューの[TACTICS]から行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "また、キャンプメニューの[STATUS]で\x01",
            "サポートクラフトの使用のＯＮ／ＯＦＦを\x01",
            "選択することができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_1B(0x0, 0x0, 0x1D)
    OP_1B(0x8, 0x0, 0x1E)
    EventEnd(0x5)
    Return()

    # Function_28_9FB1 end

    def Function_29_BAD6(): pass

    label("Function_29_BAD6")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(1000, 1100, 1250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 1000, 10, 3300, 180)
    SetChrPos(0x102, 1500, 10, 1500, 180)
    SetChrPos(0x104, 1500, 0, 2500, 180)
    SetChrPos(0x109, 500, 0, 1000, 180)
    SetChrPos(0x105, 500, 10, 2000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_BBB9():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BBB9)
    Sleep(200)

    def lambda_BBD6():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BBD6)
    Sleep(200)

    def lambda_BBF3():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BBF3)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_BC2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BC2E)
    Sleep(400)

    def lambda_BC42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BC42)

    def lambda_BC53():
        OP_96(0xFE, 0x3E8, 0xA, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BC53)
    Sleep(400)

    def lambda_BC70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BC70)

    def lambda_BC81():
        OP_96(0xFE, 0x3E8, 0xA, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC81)
    WaitChrThread(0x101, 1)

    #C0378
    ChrTalk(
        0x101,
        "#00003F#5P──なあ、ランディ。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0379
    AnonymousTalk(
        0x104,
        "ん？　なんだロイド。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0380
    ChrTalk(
        0x101,
        (
            "#00008F#5Pその……\x01",
            "お父さんのことだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0381
    ChrTalk(
        0x104,
        (
            "#12P#00306Fああ、それか……\x02\x03",

            "#00300F別に気にすることはねぇぜ？\x01",
            "あの世界じゃ珍しくもねぇ話だ。\x02\x03",

            "それに、団を抜けた時に\x01",
            "俺と親父は縁を切っている。\x02\x03",

            "#00304F何も感じないわけじゃねぇが……\x01",
            "ま、サバサバしたもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#00006F#5P……そっか。\x02\x03",

            "#00001Fでも、気が向いたら\x01",
            "色々と聞かせてくれよな？\x02\x03",

            "一応、リーダーとして\x01",
            "相談に乗れることがあるかも\x01",
            "しれないしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x104,
        "#12P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#00011F#5Pあ、ゴメン。\x01",
            "ちょっと生意気だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x104,
        (
            "#12P#00304Fハハ、違う違う。\x02\x03",

            "#00302F何だかんだ言って\x01",
            "お前も成長してると思ってな。\x02\x03",

            "#00309Fうーん、お兄さん感慨深いぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_C1DB")

    #C0386
    ChrTalk(
        0x101,
        "#00006F#5Pあのな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0387
    ChrTalk(
        0x101,
        (
            "#00008F#5P……その、こういう時は\x01",
            "何とか力にならせて欲しいんだ。\x02\x03",

            "#00000F頼りないかもしれないけど\x01",
            "それが“相棒”ってもんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x104,
        "#12P#00305Fロイド……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(300)
    SetCameraDistance(22000, 1000)

    def lambda_C0FA():
        OP_96(0xFE, 0x3E8, 0x0, 0x4E2, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0FA)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x101, 0x5)
    Sound(811, 0, 30, 0)
    Sleep(300)

    #C0389
    ChrTalk(
        0x104,
        (
            "#12P#00302F……分かった、いずれ話を\x01",
            "聞いてもらうかもしれねぇ。\x02\x03",

            "#00309Fそん時は頼むぜ──相棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#00002F#5Pああ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C26C")

    label("loc_C1DB")


    #C0391
    ChrTalk(
        0x101,
        "#00006F#5Pあのな……\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#12P#00304F……ま、気が向いたら\x01",
            "相談するかもしれねぇ。\x02\x03",

            "#00300Fそん時はよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#00000F#5Pああ……！\x02",
    )

    CloseMessageWindow()

    label("loc_C26C")

    SetChrPos(0x102, 1500, -1000, -4000, 180)
    SetChrPos(0x105, 500, -1000, -4000, 180)

    #N0394
    NpcTalk(
        0x105,
        "ワジの声",
        "#1P#2Sあれ、何してるの？\x02",
    )

    CloseMessageWindow()

    #N0395
    NpcTalk(
        0x102,
        "エリィの声",
        "#1P#2S２人とも、忘れ物？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_C363")
    SetCameraDistance(22500, 1000)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_C34A():
        OP_96(0xFE, 0x3E8, 0x0, 0x2EE, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C34A)
    WaitChrThread(0x104, 1)

    label("loc_C363")


    def lambda_C368():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C368)

    #C0396
    ChrTalk(
        0x101,
        "#00011F#5Pゴメン、すぐ行く！\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x104,
        (
            "#5P#00304Fそんじゃあボチボチ、\x01",
            "お仕事を始めるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_C3DA():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C3DA)
    Sleep(100)

    def lambda_C3F7():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C3F7)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_C41E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C41E)
    Sleep(400)

    def lambda_C432():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C432)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0398
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力車で、クロスベル全土に\x01",
            "移動することが可能になりました。\x02\x03",

            "西通りに出る特務支援課の裏口に\x01",
            "停めてあるので活用してみてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0100", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_29_BAD6 end

    def Function_30_C53E(): pass

    label("Function_30_C53E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(-2250, 1100, 67800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -2000, 10, 69500, 180)
    SetChrPos(0x102, -2000, 10, 68300, 270)
    SetChrPos(0x104, -1000, 0, 68300, 270)
    SetChrPos(0x109, -2500, 10, 67300, 270)
    SetChrPos(0x105, -1500, 10, 67300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C621():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C621)
    Sleep(200)

    def lambda_C63E():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C63E)
    Sleep(200)

    def lambda_C65B():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C65B)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_C696():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C696)
    Sleep(400)

    def lambda_C6AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C6AA)
    Sleep(400)

    def lambda_C6BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C6BE)

    def lambda_C6CF():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C6CF)
    Sleep(300)

    def lambda_C6EC():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C6EC)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    #C0399
    ChrTalk(
        0x101,
        "#00003F#11P──なあ、ランディ。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0400
    AnonymousTalk(
        0x104,
        "ん？　なんだロイド。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0401
    ChrTalk(
        0x101,
        (
            "#00008F#11Pその……\x01",
            "お父さんのことだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0402
    ChrTalk(
        0x104,
        (
            "#6P#00306Fああ、それか……\x02\x03",

            "#00300F別に気にすることはねぇぜ？\x01",
            "あの世界じゃ珍しくもねぇ話だ。\x02\x03",

            "それに、団を抜けた時に\x01",
            "俺と親父は縁を切っている。\x02\x03",

            "#00304F何も感じないわけじゃねぇが……\x01",
            "ま、サバサバしたもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#00006F#11P……そっか。\x02\x03",

            "#00001Fでも、気が向いたら\x01",
            "色々と聞かせてくれよな？\x02\x03",

            "一応、リーダーとして\x01",
            "相談に乗れることがあるかも\x01",
            "しれないしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x101,
        (
            "#00011F#11Pあ、ゴメン。\x01",
            "ちょっと生意気だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x104,
        (
            "#6P#00304Fハハ、違う違う。\x02\x03",

            "#00302F何だかんだ言って\x01",
            "お前も成長してると思ってな。\x02\x03",

            "#00309Fうーん、お兄さん感慨深いぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_CC4C")

    #C0407
    ChrTalk(
        0x101,
        "#00006F#11Pあのな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0408
    ChrTalk(
        0x101,
        (
            "#00008F#11P……その、こういう時は\x01",
            "何とか力にならせて欲しいんだ。\x02\x03",

            "#00000F頼りないかもしれないけど\x01",
            "それが“相棒”ってもんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x104,
        "#6P#00305Fロイド……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_CB6B():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CB6B)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x101, 0x7)
    Sound(811, 0, 30, 0)
    Sleep(300)

    #C0410
    ChrTalk(
        0x104,
        (
            "#6P#00302F……分かった、いずれ話を\x01",
            "聞いてもらうかもしれねぇ。\x02\x03",

            "#00309Fそん時は頼むぜ──相棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        "#00002F#11Pああ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCDE")

    label("loc_CC4C")


    #C0412
    ChrTalk(
        0x101,
        "#00006F#11Pあのな……\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x104,
        (
            "#6P#00304F……ま、気が向いたら\x01",
            "相談するかもしれねぇ。\x02\x03",

            "#00300Fそん時はよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#00000F#11Pああ……！\x02",
    )

    CloseMessageWindow()

    label("loc_CCDE")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    #N0415
    NpcTalk(
        0x105,
        "ワジの声",
        "#2P#2Sあれ、何してるの？\x02",
    )

    CloseMessageWindow()

    #N0416
    NpcTalk(
        0x102,
        "エリィの声",
        "#2P#2S２人とも、忘れ物？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_CDD5")
    SetCameraDistance(22500, 700)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_CDBC():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CDBC)
    WaitChrThread(0x104, 1)

    label("loc_CDD5")


    def lambda_CDDA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CDDA)

    #C0417
    ChrTalk(
        0x101,
        "#00011F#11Pゴメン、すぐ行く！\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x104,
        (
            "#11P#00304Fそんじゃあボチボチ、\x01",
            "お仕事を始めるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_CE4E():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CE4E)
    Sleep(100)

    def lambda_CE6B():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE6B)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_CE92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CE92)
    Sleep(400)

    def lambda_CEA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEA6)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力車で、クロスベル全土に\x01",
            "移動することが可能になりました。\x02\x03",

            "西通りに出る特務支援課の裏口に\x01",
            "停めてあるので活用してみてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_30_C53E end

    def Function_31_CFB2(): pass

    label("Function_31_CFB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch02710.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    SoundLoad(3605)
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x102, 13900, 900, 2550, 270)
    SetChrPos(0x104, 11300, 900, 2550, 90)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 6600, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0xE)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13400, 1300, 6600, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12400, 1450, 6600, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0xE)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12000, 1300, 6600, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 4600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0xE)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13400, 1300, 4600, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1450, 4600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0xE)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12000, 1300, 4600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12400, 1450, 2600, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0xE)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 12000, 1300, 2600, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0xE)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 2600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x7)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12700, 1400, 5500, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x7)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12700, 1400, 3500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 16000, 750, 5500, 0)
    SetChrSubChip(0xF, 0x7)
    SetChrSubChip(0x11, 0x7)
    SetChrSubChip(0x13, 0x7)
    SetChrSubChip(0x15, 0x7)
    SetChrSubChip(0x17, 0x7)
    SetChrSubChip(0x19, 0x7)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0420
    AnonymousTalk(
        0x101,
        (
            "#00003F──なるほど。\x01",
            "通商会議の本番は明日ですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0421
    ChrTalk(
        0x8,
        (
            "#5P#01003Fああ、今日のところは\x01",
            "昼食会に各種懇談#4Rこんだん#会って所だな。\x02\x03",

            "#01002F夜には晩餐会に加えて\x01",
            "アルカンシェルの観劇があるらしい。\x02\x03",

            "ちなみに首脳たちは全員、\x01",
            "ミシュラムの迎賓館#6Rげいひんかん#に泊まる予定だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x102,
        (
            "#00100F迎賓館というと、\x01",
            "ハルトマン元議長の屋敷ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        (
            "#6P#00305Fへえ、あの馬鹿デカイ屋敷、\x01",
            "そんな風に使われてんのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#5P#01006Fまあ、ハルトマンについては\x01",
            "汚職や違法取引に関する罰金が\x01",
            "凄まじいほどの額になったからな。\x02\x03",

            "#01000Fその代償として没収されて\x01",
            "迎賓館として使われたってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x109,
        (
            "#6P#10106Fうーん……\x01",
            "まあ、自業自得でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x105,
        (
            "#6P#10300Fそれじゃあ当然、ミシュラム方面は\x01",
            "封鎖ってわけかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x8,
        (
            "#5P#01003Fああ、通商会議の期間中は\x01",
            "ホテルやテーマパークも臨時休業だ。\x02\x03",

            "#01002Fそっちは警備隊が詰めているから\x01",
            "心配する必要はないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x101,
        (
            "#00004F#11P判りました。\x02\x03",

            "#00000F俺たちの方は、昨日に続いて\x01",
            "支援活動に専念しますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#5P#01004Fそれで構わんだろう。\x02\x03",

            "#01000F招待客の中には、昼食会の後、\x01",
            "クロスベル各地を訪れる者もいるようだ。\x02\x03",

            "何か問題が起きるかもしれんから\x01",
            "お前らでフォローしとくといいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        "#00104F了解しました。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x104,
        (
            "#6P#00306Fしかし、さすが招待客どもは\x01",
            "並みのオーラじゃなかったな。\x02\x03",

            "#00301F特に《鉄血宰相》……\x01",
            "ありゃタダモンじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0432
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ、あのレクター大尉が\x01",
            "控えていたのも気になったけど……\x02\x03",

            "#00008F宰相本人はそれ以上に\x01",
            "圧倒的な雰囲気の持ち主だったな。\x02\x03",

            "#00001F共和国のロックスミス大統領は\x01",
            "親しみの持てる雰囲気だったけど……\x02\x03",

            "#00005F……でも、すぐ近くに\x01",
            "あのキリカさんが控えていたな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)

    #C0433
    ChrTalk(
        0x102,
        (
            "#00103Fカルバードの諜報組織、\x01",
            "《ロックスミス機関》の人間……\x02\x03",

            "#00108F庶民派で知られる大統領だけど\x01",
            "やっぱり一筋縄では行かなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x109,
        (
            "#5P#10102Fでも、リベールのクローディア姫は\x01",
            "さすがに気品がありましたよね。\x02\x03",

            "#10109F一緒にいたユリア准佐も\x01",
            "すっごく格好よかったですし！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0435
    ChrTalk(
        0x105,
        (
            "#6P#10305Fああ、リベール王国の\x01",
            "王室親衛隊の女性隊長だっけ？\x02\x03",

            "#10302F何でもそのスジじゃ、\x01",
            "熱狂的なファンがいるらしいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x109,
        "#5P#10112Fう、うん……そうだけど。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#00109Fあはは……\x01",
            "私もちょっとファンだったりして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(250)

    #C0438
    ChrTalk(
        0x101,
        "#5P#00005Fへえ、そうなのか？\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x104,
        (
            "#6P#00302Fなんだなんだ～？\x01",
            "お嬢、そういう趣味だったのかよ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(150)

    #C0440
    ChrTalk(
        0x102,
        (
            "#00102F別に趣味ってわけじゃないけど……\x02\x03",

            "#00104Fその、前にリベールに滞在した時、\x01",
            "王室親衛隊のパレードを見物して……\x02\x03",

            "#00100F写真集なんかも出ていたから\x01",
            "思わず買っちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        "#5P#00012Fな、なるほど。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x109,
        "#5P#10101Fそれ、後で見せてください！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0443
    ChrTalk(
        0x102,
        (
            "#00109Fあはは……\x01",
            "うん、いいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x104,
        "#6P#00306Fやれやれ、嘆かわしいねぇ。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、男装の麗人は\x01",
            "一種のロマンだからねぇ。\x02\x03",

            "#10302F僕としては帝国の皇子殿下も\x01",
            "結構気になったけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0446
    ChrTalk(
        0x101,
        (
            "#00000F#11Pオリヴァルト皇子か……\x01",
            "最近、わりと聞く名前だけど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)

    #C0447
    ChrTalk(
        0x102,
        (
            "#00104Fリベールの異変の解決に\x01",
            "一役買ったことで有名な方ね。\x02\x03",

            "#00100Fそれから色々な催しに出席して\x01",
            "評判になっているみたいだけど……\x02\x03",

            "たしか皇位継承権は\x01",
            "持っていらっしゃらないのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    #C0448
    ChrTalk(
        0x101,
        (
            "#5P#00001Fそうなのか……\x02\x03",

            "#00005Fあれ、リベールの異変の解決に\x01",
            "一役買ったっていうことは……\x02\x03",

            "#00000Fエステルやヨシュアたちと\x01",
            "知り合いだったりするのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        "#00105Fああ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x104,
        (
            "#6P#00300Fあの２人、顔が広そうだったし\x01",
            "あり得るかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 1000, 0, -2000, 0)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 1000, 0, -2000, 0)
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #N0451
    NpcTalk(
        0x9,
        "キーアの声",
        "#3605V#30W#12Aただいまー。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1000, 1100, 1500, 2000)
    MoveCamera(40, 23, 0, 2000)
    SetCameraDistance(22000, 2000)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x105, 0x2)
    Sleep(1300)

    def lambda_E25F():
        OP_96(0xFE, 0x3E8, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E25F)

    def lambda_E279():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E279)
    Sleep(1000)

    def lambda_E28D():
        OP_96(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E28D)

    def lambda_E2A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E2A7)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)

    def lambda_E2C0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E2C0)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)
    SetChrSubChip(0xA, 0x5)
    OP_6F(0x79)

    #C0452
    ChrTalk(
        0x101,
        "#00002Fキーア、ツァイト、お帰り。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xA,
        "#6P#01200Fウォン。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_E324():
        OP_96(0xFE, 0x3E8, 0x352, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E324)
    Sleep(1000)
    Fade(1000)
    OP_68(10600, 1850, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_68(12600, 1850, 6600, 3000)
    EndChrThread(0x9, 0x1)
    SetChrPos(0x9, 5000, 850, 8900, 90)

    def lambda_E39A():
        OP_96(0xFE, 0x2AF8, 0x352, 0x22C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E39A)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x104, 0x1)
    OP_0D()
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x8, 0x2)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0454
    ChrTalk(
        0x102,
        (
            "#00105Fあら、シズクちゃんは\x01",
            "一緒じゃなかったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x9,
        (
            "#01106F#5Pあ、うん、おとーさんと\x01",
            "病院に戻っちゃった。\x02\x03",

            "#01110Fでも、ビルのおひろめは\x01",
            "いっしょに見たよー。\x02\x03",

            "#01109Fすごかったねー！\x01",
            "ロイドたちは近くで見たんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#00012Fああ、正直大きすぎて\x01",
            "よく分からないくらいだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x104,
        (
            "#12P#00300F#Nま、とんでもないビルってのは\x01",
            "イヤってほど分かったけどな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0458
    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふっ、キーアちゃんの方が\x01",
            "バッチリ見えたかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x9,
        (
            "#01109F#5Pうんっ！\x01",
            "すっごくカッコよかったー！\x02\x03",

            "#01110Fハナビ……だっけ？\x01",
            "あれもすごくキレイだったし！\x02\x03",

            "#01102Fでも……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C0460
    ChrTalk(
        0x101,
        "#00005Fん、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x9,
        (
            "#01104F#5Pあ、ううん、何でもない。\x02\x03",

            "#01100Fロイドたちはこれから\x01",
            "また仕事に出かけるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        (
            "#00000Fああ、夕方には戻ると思うけど。\x02\x03",

            "課長の方はどうですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0463
    ChrTalk(
        0x8,
        (
            "#5P#01003F今日は俺はここで待機だ。\x02\x03",

            "#01002F何かあったら連絡するから\x01",
            "遠慮なく出かけてこい。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#00004Fはい、お言葉に甘えて。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x102,
        (
            "#00102F端末をチェックしてから\x01",
            "出かけましょうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    Sleep(500)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
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
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 3)
    OP_29(0xA3, 0x1, 0x7)
    OP_29(0xA3, 0x1, 0x8)
    Call(0, 67)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E91D")
    Jump("loc_E922")

    label("loc_E91D")

    OP_29(0x73, 0x4, 0x40)

    label("loc_E922")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_CFB2 end

    def Function_32_E928(): pass

    label("Function_32_E928")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)

    #C0466
    ChrTalk(
        0x101,
        (
            "#00001F#5P色々来ているけど……\x01",
            "どれも気になるな。\x02\x03",

            "#00006Fこの演奏家の捜索っていうのは\x01",
            "ちょっとよく分からないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#6P#00309Fいや～、でもまさか遊撃士の\x01",
            "お姉さんたちの要請とはねぇ。\x02\x03",

            "#00302F訓練ってのは色気がねぇけど\x01",
            "時間があったら寄りたいよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x109,
        (
            "#6P#10104Fふふ、いい機会かもしれませんね。\x02\x03",

            "#10100Fこちらの猫の捜索というのは\x01",
            "あのご家族からみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EB52():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EB52)

    def lambda_EB5F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_EB5F)
    Sleep(50)

    def lambda_EB6F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EB6F)

    def lambda_EB7C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EB7C)
    WaitChrThread(0x101, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EC1A")

    #C0469
    ChrTalk(
        0x101,
        (
            "#00002F#5Pああ、東通りに引っ越した\x01",
            "ボンドさんのところだな。\x02\x03",

            "#00004Fあの猫とも縁があるし……\x01",
            "出来れば力になってあげたいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC97")

    label("loc_EC1A")


    #C0470
    ChrTalk(
        0x101,
        (
            "#00002F#5Pああ、東通りに引っ越した\x01",
            "ボンドさんのところだな。\x02\x03",

            "#00003F色々大変そうだし……\x01",
            "出来れば力になってあげたいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC97")


    #C0471
    ChrTalk(
        0x102,
        (
            "#00104F#11Pそうね、私も賛成。\x02\x03",

            "#00100F私たちを頼ってくれたみたいだし、\x01",
            "忘れずに訪ねてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、タワーのお披露目と\x01",
            "ＶＩＰたちの来訪で\x01",
            "街も浮き立っているみたいだ。\x02\x03",

            "#10302F色々回ってみるのも\x01",
            "楽しいかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 4)
    OP_29(0xA3, 0x1, 0x9)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_32_E928 end

    def Function_33_EDD2(): pass

    label("Function_33_EDD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("apl/ch51090.itc", 0x23)
    LoadChrToIndex("apl/ch50092.itc", 0x24)
    LoadChrToIndex("apl/ch51210.itc", 0x25)
    SoundLoad(3606)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01102.itp")
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF03")
    OP_68(1300, 1850, 11800, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    OP_90(0x101, 1700, 4850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x104, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    Jump("loc_EF86")

    label("loc_EF03")

    OP_68(1000, 1000, 700, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x104, 300, 0, -2900, 0)
    SetChrPos(0x109, 1400, 0, -3200, 0)
    SetChrPos(0x105, 300, 0, -4200, 0)

    label("loc_EF86")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 11000, 850, 14000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F023")
    OP_68(1300, 1850, 9800, 3500)
    BeginChrThread(0x101, 3, 0, 34)
    Jump("loc_F0C2")

    label("loc_F023")

    OP_68(1000, 1000, 2700, 3500)

    def lambda_F039():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F039)
    Sleep(200)

    def lambda_F056():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F056)
    Sleep(200)

    def lambda_F073():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F073)
    Sleep(200)

    def lambda_F090():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F090)
    Sleep(200)

    def lambda_F0AD():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F0AD)

    label("loc_F0C2")

    FadeToBright(1000, 0)

    def lambda_F0D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F0D0)
    Sleep(400)

    def lambda_F0E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F0E4)
    Sleep(600)

    def lambda_F0F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F0F8)
    Sleep(400)

    def lambda_F10C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F10C)
    Sleep(600)

    def lambda_F120():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F120)
    OP_0D()
    StopBGM(0xFA0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F22E")

    #C0473
    ChrTalk(
        0x101,
        "#5P#00002Fあれ……\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x102,
        (
            "#5P#00109Fあら……\x01",
            "すごくいい匂いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x105,
        (
            "#5P#10302Fへえ、メイプルシロップの\x01",
            "匂いみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2AE")

    label("loc_F22E")


    #C0476
    ChrTalk(
        0x101,
        "#00002F#5Pあれ……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        (
            "#00109F#11Pあら……\x01",
            "すごくいい匂いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x105,
        (
            "#12P#10302Fへえ、メイプルシロップの\x01",
            "匂いみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2AE")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    OP_68(11000, 1750, 10500, 2000)
    SetCameraDistance(26500, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_F2F2():
        OP_95(0xFE, 10810, 850, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F2F2)

    def lambda_F30C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F30C)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3B5")
    SetChrPos(0x101, 1700, -850, 9100, 180)
    SetChrPos(0x102, 600, -850, 9400, 180)
    SetChrPos(0x104, 1700, -850, 10400, 180)
    SetChrPos(0x109, 600, -850, 10700, 180)
    SetChrPos(0x105, 1700, -850, 11700, 180)

    label("loc_F3B5")


    def lambda_F3BA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F3BA)
    Sleep(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0479
    AnonymousTalk(
        0x9,
        (
            "#3606V#30Wあ、ロイドたち。\x01",
            "やっぱり帰ってきたんだー。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE16)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0480
    ChrTalk(
        0x101,
        (
            "#00009Fああ、ちょっと休憩にね。\x02\x03",

            "#00000Fそれにしても……\x01",
            "マフィンを焼いてたのか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F556")

    #C0481
    ChrTalk(
        0x9,
        (
            "#01104F#11Pえへへ……なんかみんなが\x01",
            "帰ってきそうな気がしたからー。\x02\x03",

            "#01110Fメイプルマフィンだよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5BE")

    label("loc_F556")


    #C0482
    ChrTalk(
        0x9,
        (
            "#01104F#5Pえへへ……なんかみんなが\x01",
            "帰ってきそうな気がしたからー。\x02\x03",

            "#01110Fメイプルマフィンだよー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5BE")


    #C0483
    ChrTalk(
        0x104,
        (
            "#00305Fおお……\x01",
            "キー坊、気が利くじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x109,
        "#10109Fふふっ、嬉しいな。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        (
            "#00102Fせっかくだし\x01",
            "紅茶でも淹れましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(27000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(12600, 2650, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2550, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, 11300, 900, 4600, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 6650, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 4600, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 2550, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1400, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x2)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1350, 6700, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12400, 1400, 6600, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x2)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1350, 7100, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1400, 5400, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x2)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 5000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1400, 4600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x1)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1350, 5100, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1400, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x2)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 3400, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 2100, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x23)
    SetChrSubChip(0x1A, 0x2)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1350, 1700, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 2600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x2)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1350, 3100, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 16300, 750, 5500, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    Sleep(500)
    OP_68(12600, 2150, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0486
    ChrTalk(
        0x8,
        (
            "#5P#01005F──なるほど。\x01",
            "そんな所で出くわしたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        (
            "#00006F#11Pええ、何か狙いがあって\x01",
            "現れた訳ではなさそうですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x104,
        (
            "#00301F……《赤い星座》の方に\x01",
            "相変わらず動きはないんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x8,
        (
            "#5P#01004F何かあれば一課の方から\x01",
            "こちらに連絡があるはずだ。\x02\x03",

            "#01002F気持ちは判らんでもないが\x01",
            "まあ、そう焦るな。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        "#00304Fはは……了解。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0491
    ChrTalk(
        0x101,
        (
            "#00003F#11Pまあ、気になるのは\x01",
            "《赤い星座》だけじゃない。\x02\x03",

            "#00001Fとにかく、何か兆候はないか\x01",
            "気を付けて回ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)

    #C0492
    ChrTalk(
        0x102,
        (
            "#6P#00108Fそうね……\x01",
            "ＶＩＰが訪れている状況で\x01",
            "何か起きたら大変だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x109,
        (
            "#6P#10101F余裕があったら車で\x01",
            "郊外にも回ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x9,
        "#6P#01105Fロイドたち、また出かけるのー？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    #C0495
    ChrTalk(
        0x101,
        (
            "#00004F#11Pああ、お仕事再開だ。\x02\x03",

            "#00002Fマフィン、ごちそうさま。\x01",
            "すっごく美味しかったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#5P#00109Fふふっ、私たちの誰よりも\x01",
            "料理が上手になっちゃったわね。\x02\x03",

            "#00102Fひょっとしてオスカーさんに\x01",
            "作り方を習ったりしたとか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(150)

    #C0497
    ChrTalk(
        0x9,
        "#6P#01109Fえへへ、そんなとこー。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(150)

    #C0498
    ChrTalk(
        0x9,
        (
            "#6P#01110Fあ、まだ残りがあるから\x01",
            "よかったら食べてー。\x02\x03",

            "明日くらいまでなら\x01",
            "大丈夫だと思うからー。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0499
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を５個貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20F, 5)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0500
    ChrTalk(
        0x105,
        "#10302Fへえ、気が利くじゃない。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#00306Fくううっ……\x01",
            "お父さん、泣けてくるぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0502
    ChrTalk(
        0x101,
        (
            "#00003F#5P……ちょっと待った。\x02\x03",

            "#00013Fいくらランディでも\x01",
            "キーアの父親役は譲れないぞ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    #C0503
    ChrTalk(
        0x104,
        (
            "#00302Fフッ、面白ぇ。\x01",
            "俺様とやり合おうってか？\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x9,
        "#6P#01105Fほえ～……\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x102,
        (
            "#6P#00106Fふう……\x01",
            "何を張り合ってるんだか。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x109,
        "#6P#10112Fあはは……\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x105,
        "#10309F親バカ、ここに極まれりだね。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_32(0xFF, 0xFE, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0x9, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 123270, 0, 4980, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
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
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 6)
    OP_29(0xA3, 0x1, 0x10)
    OP_C9(0x0, 0x1000)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_33_EDD2 end

    def Function_34_103B4(): pass

    label("Function_34_103B4")


    def lambda_103B9():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_103B9)
    Sleep(200)

    def lambda_103D6():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_103D6)
    Sleep(200)

    def lambda_103F3():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_103F3)
    Sleep(200)

    def lambda_10410():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10410)
    Sleep(200)

    def lambda_1042D():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1042D)
    Return()

    # Function_34_103B4 end

    def Function_35_10443(): pass

    label("Function_35_10443")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14100, 1750, 12300, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    SoundLoad(848)
    SoundLoad(3607)
    SoundLoad(3608)
    SetChrPos(0x101, 5000, 0, 15000, 0)
    SetChrPos(0x102, 5000, 0, 15000, 0)
    SetChrPos(0x104, 5000, 0, 15000, 0)
    SetChrPos(0x109, 5000, 0, 15000, 0)
    SetChrPos(0x105, 5000, 0, 15000, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 11000, 850, 14000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 13100, 850, 9300, 0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(848, 2, 100, 0)
    Sleep(2000)
    PlayBGM("ed7102", 0)
    SetCameraDistance(24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_105B2():
        OP_95(0xFE, 11000, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_105B2)

    def lambda_105CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_105CC)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_105FD():
        OP_95(0xFE, 14100, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_105FD)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x0, 0x1F4)
    OP_79(0x1)
    ClearMapObjFlags(0x1, 0x10)
    Sound(838, 0, 100, 0)
    OP_24(0x350)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0508
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01110F#3607V#30Wえっと、もしもし？\x02\x03",

            "#01109F#3608Vこちらクロスベル警察、\x01",
            "特務支援課でーす。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE18)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("少女の声")

    #A0509
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ……キーアですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0510
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105Fあ、ティオだー！\x02\x03",

            "#01109Fまた掛けてくれたんだー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ティオの声")

    #A0511
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふ、昨日と違って\x01",
            "普通の導力通信ですが。\x02\x03",

            "……ひょっとして\x01",
            "近くに誰もいませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0512
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01100Fうん、かちょーも\x01",
            "さっき出かけちゃったし。\x02\x03",

            "ツァイトはそこにいるけどー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 190, -1, -1)

    #A0513
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01200Fウォン。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ティオの声")

    #A0514
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふむ、そうですか。\x02\x03",

            "……実はロイドさんたちの\x01",
            "エニグマに繋がらなくって。\x02\x03",

            "それで支援課に直接、\x01",
            "連絡したんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0515
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105Fふーん、そうなんだ。\x02\x03",

            "#01111Fロイドたちだったら\x01",
            "真っ白なハヤブサに呼ばれて\x01",
            "出かけたみたいだけどー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ティオの声")

    #A0516
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "真っ白なハヤブサ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0517
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01110Fうんっ、ジークって言って\x01",
            "ツァイトみたいに喋れるの。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ティオの声")

    #A0518
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……何だか色々と\x01",
            "進展しているみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(801, 0, 50, 0)
    Sleep(1300)
    SetMessageWindowPos(250, 0, -1, -1)
    SetChrName("女性の声")

    #A0519
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40W……の皆様。\x01",
            "長らくお待たせしました。\x02",
        )
    )

    CloseMessageWindow()

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40Wこれより……レマン……を\x01",
            "………参ります……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0521
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105F？？？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ティオの声")

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──時間みたいですね。\x02\x03",

            "キーア、また後で。\x01",
            "ロイドさんたちと課長にも\x01",
            "よろしく言っておいてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0523
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01109Fうん、またねー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 190, -1, -1)

    #A0524
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01200Fウォン。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, -1500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sleep(500)

    #N0525
    NpcTalk(
        0x8,
        "セルゲイの声",
        "おー、帰ったぞ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10C47():

        label("loc_10C47")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10C47")

    QueueWorkItem2(0x9, 2, lambda_10C47)
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    Sleep(2000)

    def lambda_10C78():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10C78)

    def lambda_10C92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10C92)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x2D, 0x1F4)
    OP_6F(0x79)

    #C0526
    ChrTalk(
        0x9,
        (
            "#01101F#12Pあ、かちょー。\x02\x03",

            "#01106Fもっと早く帰ってきたら\x01",
            "ティオと話せたのにー！\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#01005F#6Pなんだ、通信が入ってたのか。\x02\x03",

            "#01002Fで、何と言っていた？\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x9,
        "#01110F#12Pえっと、あのねー。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 36)
    Sleep(1000)
    OP_68(1960, 2250, 2650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x350)
    SetScenarioFlags(0x22, 0)
    NewScene("e3210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_10443 end

    def Function_36_10DBA(): pass

    label("Function_36_10DBA")


    def lambda_10DBF():
        OP_95(0xFE, 1000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DBF)
    WaitChrThread(0x8, 1)

    def lambda_10DDD():
        OP_95(0xFE, 10000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DDD)
    WaitChrThread(0x8, 1)
    Return()

    # Function_36_10DBA end

    def Function_37_10DF7(): pass

    label("Function_37_10DF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x141, 5)
    OP_29(0xA3, 0x1, 0x14)
    OP_29(0xA3, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10E23")
    Jump("loc_10E28")

    label("loc_10E23")

    OP_29(0x75, 0x4, 0x40)

    label("loc_10E28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10E39")
    Jump("loc_10E3E")

    label("loc_10E39")

    OP_29(0x76, 0x4, 0x40)

    label("loc_10E3E")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 14600, 850, 9200, 45)
    SetChrPos(0x102, 15000, 850, 8200, 45)
    SetChrPos(0x104, 13400, 850, 9400, 90)
    SetChrPos(0x109, 15700, 850, 7400, 0)
    SetChrPos(0x105, 17000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 18)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 14600, 850, 9200, 45)
    SetChrPos(0x102, 15000, 850, 8200, 45)
    SetChrPos(0x104, 13400, 850, 9400, 90)
    SetChrPos(0x109, 15700, 850, 7400, 0)
    SetChrPos(0x105, 17000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    ClearChrFlags(0x8, 0x80)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0529
    ChrTalk(
        0x101,
        (
            "#6P#00003F……やっぱり幾つか\x01",
            "新しいのが来ているか。\x02\x03",

            "#00001Fうーん、どれも結構\x01",
            "気にはなるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        (
            "#12P#00104F時間に余裕があれば\x01",
            "立ち寄ってみましょう。\x02\x03",

            "#00100F午前中だったら\x01",
            "自由に動けそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x109,
        (
            "#12P#10100F車を使えば郊外にも\x01",
            "移動できそうですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1113B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1113B)
    WaitChrThread(0x103, 2)
    Sleep(150)

    #C0532
    ChrTalk(
        0x103,
        (
            "#00204F#5P車ですか……\x01",
            "ちょっと楽しみですね。\x02\x03",

            "#00202F何でもＺＣＦが\x01",
            "開発した導力車だとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x104,
        (
            "#6P#00302Fおお、一課の連中も\x01",
            "見返せそうな新型だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        (
            "#6P#00005Fでもティオ、\x01",
            "昨日着いたばかりなのに\x01",
            "朝早くから動いて大丈夫か？\x02\x03",

            "#00000F何だったら午前中は\x01",
            "ゆっくりしててくれても──\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        "#00211F#5Pジロッ……\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        "#6P#00006Fスミマセン、つい。\x02",
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x103,
        "#00206F#5P……まったく。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x104,
        (
            "#6P#00309Fはは、何だかティオすけが\x01",
            "戻ってきたって感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ……そうね。\x02\x03",

            "#00102Fやっぱり端末前には\x01",
            "ティオちゃんがいる方が\x01",
            "しっくりくる感じだし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11372():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11372)
    Sleep(50)

    def lambda_11382():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11382)
    WaitChrThread(0x109, 2)

    #C0540
    ChrTalk(
        0x109,
        (
            "#12P#10109Fふふっ、やっぱり皆さん、\x01",
            "息が合ってますよね。\x02\x03",

            "#10102Fとりあえず……\x01",
            "これで新生・特務支援課の\x01",
            "フルメンバーですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x105,
        (
            "#10302F#12Pフフ、リーダーとしては\x01",
            "なかなか感慨深いんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#6P#00004Fああ……そうだな。\x02\x03",

            "#00002F──とにかくティオ。\x01",
            "改めてよろしく頼むよ。\x02\x03",

            "それと大変な時にわざわざ\x01",
            "戻ってきてくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x103,
        (
            "#00202F#5Pはい、こちらこそ改めて\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x104,
        (
            "#6P#00302Fはは、何だかテンション、\x01",
            "上がってきちまったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    #C0545
    ChrTalk(
        0x8,
        (
            "#01004F#5Pクク……\x01",
            "調子が出て何よりだ。\x02\x03",

            "#01002Fま、その元気がありゃあ\x01",
            "通商会議の空気にも\x01",
            "呑まれることはねぇだろ。\x02\x03",

            "お前たちなりのやり方で\x01",
            "警備の役に立ってくるといい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1161A():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1161A)
    Sleep(50)

    def lambda_1162A():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1162A)
    Sleep(50)

    def lambda_1163A():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1163A)
    Sleep(50)

    def lambda_1164A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1164A)
    Sleep(50)

    def lambda_1165A():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1165A)
    Sleep(50)

    def lambda_1166A():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1166A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_1168F():

        label("loc_1168F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1168F")

    QueueWorkItem2(0x101, 2, lambda_1168F)

    def lambda_116A1():

        label("loc_116A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116A1")

    QueueWorkItem2(0x102, 2, lambda_116A1)

    def lambda_116B3():

        label("loc_116B3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116B3")

    QueueWorkItem2(0x103, 2, lambda_116B3)

    def lambda_116C5():

        label("loc_116C5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116C5")

    QueueWorkItem2(0x104, 2, lambda_116C5)

    def lambda_116D7():

        label("loc_116D7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116D7")

    QueueWorkItem2(0x109, 2, lambda_116D7)

    def lambda_116E9():

        label("loc_116E9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116E9")

    QueueWorkItem2(0x105, 2, lambda_116E9)

    #C0546
    ChrTalk(
        0x101,
        "#12P#00000F了解です。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x102,
        (
            "#12P#00100F課長の方はこれから\x01",
            "警察本部で待機でしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        (
            "#01006F#5Pああ、各方面との折衝を\x01",
            "押し付けられちまったからな。\x02\x03",

            "#01000Fバックアップには回るが\x01",
            "オルキスタワーの警備には\x01",
            "直接参加はしないだろう。\x02\x03",

            "ただ、何かあったら\x01",
            "お前たちにも必ず連絡する。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        "#12P#00003F……助かります。\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x109,
        "#12P#10101Fよろしくお願いします！\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x8,
        "#01002F#5Pおお、それじゃあ先に行くぞ。\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2DB4, 0x2AF8, 0x1F4)

    def lambda_11896():
        OP_95(0xFE, 11700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11896)
    WaitChrThread(0x8, 1)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_118C5():
        OP_95(0xFE, 5700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_118C5)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    #C0552
    ChrTalk(
        0x101,
        (
            "#5P#00005Fそういえば……\x01",
            "キーアは図書館だったか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1198C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1198C)
    Sleep(100)

    def lambda_1199C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1199C)

    def lambda_119A9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_119A9)
    Sleep(50)

    def lambda_119B9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_119B9)

    def lambda_119C6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_119C6)
    WaitChrThread(0x102, 2)

    #C0553
    ChrTalk(
        0x102,
        (
            "#12P#00104Fええ、朝早くに\x01",
            "出かけて行っちゃったわね。\x02\x03",

            "#00100F昼までには戻るみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#5P#00002Fそっか……\x01",
            "だったら大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x104,
        (
            "#6P#00309Fよーし、そんじゃあ\x01",
            "俺たちも出かけるとすっか！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0556
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0557
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キャンプメニューの[TACTICS]で\x01",
            "アタックメンバーに加える事が出来ます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_37_10DF7 end

    def Function_38_11B65(): pass

    label("Function_38_11B65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(12600, 2450, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x102, 13900, 900, 6650, 270)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrPos(0x109, 11300, 900, 2550, 90)
    SetChrPos(0x105, 13900, 900, 2550, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x13, 0x2A)
    ClearMapObjFlags(0x13, 0x4)
    OP_49()
    SetChrPos(0x2A, 12700, 1650, 4600, 0)
    OP_D5(0x2A, 0x0, 0x15F90, 0x0, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    UseItem(0x2FC, 0xFF)
    Sleep(500)
    AddItemNumber(0x2FC, 1)
    PlayBGM("ed7111", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(12600, 1950, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0558
    ChrTalk(
        0x101,
        (
            "#11P#00003Fウルスラ間道の中洲と\x01",
            "東クロスベル街道の外れか……\x02\x03",

            "#00001Fどちらも最近、\x01",
            "あまり立ち寄ってなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        (
            "#6P#00306F旧鉱山に現れたのほど\x01",
            "デカくはねぇみたいだが……\x02\x03",

            "#00301F万全の準備は\x01",
            "しといた方が良さそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x109,
        (
            "#12P#10101Fそれと……\x01",
            "“原因”の特定ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x102,
        (
            "#00106F#5Pええ……\x02\x03",

            "#00101F時・空・幻の\x01",
            "上位三属性が働いているという\x01",
            "報告もあるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x103,
        (
            "#6P#00203F上位属性の働きに関しては\x01",
            "わたしが感知できると思います。\x02\x03",

            "#00208Fただ“原因”となると……\x01",
            "ちょっと難しいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x105,
        (
            "#10303F確かに《塔》や《僧院》についても\x01",
            "原因は判ってないみたいだし……\x02\x03",

            "#10305Fそういえば古戦場にある\x01",
            "《太陽の砦》もそうなんだっけ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0564
    ChrTalk(
        0x101,
        (
            "#5P#00006Fああ、俺たちが乗り込んだ時は\x01",
            "確かにそうだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x102,
        (
            "#00103F#5Pただ、事件が解決した後は\x01",
            "何の異常も起きていないらしいの。\x02\x03",

            "#00108F《僧院》にあったような\x01",
            "《鐘》が原因でもなさそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x109,
        (
            "#12P#10106Fそうなると本当に原因は\x01",
            "特定が難しそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x104,
        (
            "#6P#00304Fま、とにかく\x01",
            "行くだけ行ってみようぜ。\x02\x03",

            "#00300Fどうせ他の仕事なんかも\x01",
            "入ってきてるんだろうしよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)

    #C0568
    ChrTalk(
        0x101,
        (
            "#11P#00003Fそうだな……\x02\x03",

            "#00000Fよし、支援要請をチェックしてから\x01",
            "出発するとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x2A, 25600, 1650, 9500, 0)
    SetChrFlags(0x2A, 0x80)
    SetMapObjFlags(0x13, 0x4)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 0)
    OP_29(0xA6, 0x4, 0x2)
    OP_29(0xA6, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_32(0x6, 0x0, 0x43)
    OP_42(0x6, 0x3ED, 0xFF)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_38_11B65 end

    def Function_39_1226B(): pass

    label("Function_39_1226B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_1234A():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1234A)
    Sleep(100)

    def lambda_1235A():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1235A)
    Sleep(100)

    def lambda_1236A():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1236A)
    Sleep(100)

    def lambda_1237A():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1237A)
    Sleep(100)

    def lambda_1238A():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1238A)
    Sleep(100)

    def lambda_1239A():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1239A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0569
    ChrTalk(
        0x101,
        (
            "#00003F#5Pやっぱり、けっこうな数の\x01",
            "依頼が来ているみたいだな……\x02\x03",

            "#00008Fアリオスさんが動けないから\x01",
            "じゃないとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x102,
        (
            "#00106F#11P……そうね……\x02\x03",

            "#00108F今日は課長が、病院にお見舞いに\x01",
            "行っているみたいだけど……\x02\x03",

            "#00101F私たちも近いうちに\x01",
            "顔を出した方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x104,
        (
            "#5P#00306Fだな……\x01",
            "キー坊は昨日行ったらしいし。\x02\x03",

            "#00308F……結構、落ち込んでたよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x103,
        (
            "#6P#00206Fはい……\x01",
            "ちょっと心配です。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x109,
        (
            "#12P#10103F車を使えば病院までは\x01",
            "そんなにかかりませんし……\x02\x03",

            "#10100F時間があったら\x01",
            "お見舞いに行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        "#00000F#5Pああ、そうするか。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x105,
        (
            "#12P#10303Fしかし目の回復手術か……\x02\x03",

            "#10301Fやっぱりまだまだ\x01",
            "難しい領域みたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        "#00006F#5P……そうだな。\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x102,
        (
            "#00108F#11P今回の手術も\x01",
            "決して失敗というわけじゃ\x01",
            "ないみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 1)
    Call(0, 67)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    EventEnd(0x5)
    Return()

    # Function_39_1226B end

    def Function_40_12719(): pass

    label("Function_40_12719")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis255.itp")
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 11300, 900, 5400, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x18)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1300, 6700, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12350, 1450, 7100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x18)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1300, 6700, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 5400, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x18)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1300, 5000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12350, 1450, 5400, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x18)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 5000, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1450, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x18)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1300, 3400, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2100, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x18)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1300, 1700, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12350, 1450, 2100, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x18)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 1700, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 12350, 1450, 3800, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x18)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 12300, 1300, 3400, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 16300, 750, 5500, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrSubChip(0xF, 0xA)
    SetChrSubChip(0x11, 0xA)
    SetChrSubChip(0x13, 0xA)
    SetChrSubChip(0x15, 0xA)
    SetChrSubChip(0x17, 0xA)
    SetChrSubChip(0x19, 0xA)
    SetChrSubChip(0x1B, 0xA)
    SetChrSubChip(0x1D, 0xA)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0578
    ChrTalk(
        0x8,
        (
            "#5P#01006F──なるほどな。\x01",
            "例のクスリの原料になった花か。\x02\x03",

            "#01001Fそうなると警察にとっても\x01",
            "他人事じゃなくなって来たな。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x101,
        (
            "#00008F#11Pええ、引き続きギルドと協力して\x01",
            "調査しようと思うんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x102,
        (
            "#6P#00101F他に、気になる案件は\x01",
            "何か入っていませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0581
    ChrTalk(
        0x8,
        (
            "#11P#01003F入ってるといえば入ってるが\x01",
            "まあ、他の課に任せておけ。\x02\x03",

            "#01000Fどのみち、国家独立の住民投票で\x01",
            "ある程度の混乱は避けられねぇだろ。\x02\x03",

            "今は不安要素の\x01",
            "洗い出しの方が先決のはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x109,
        "#6P#10106F……確かにそうですね。\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x105,
        "#10302F#12P所謂#4Rいわゆる#、危機管理ってヤツだね。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        (
            "#6P#00203Fしかしそうなると……\x01",
            "今日の方針はどうしましょう？\x02\x03",

            "#00200F幻獣の調査も、わたし達の担当は\x01",
            "昨日の内に終えてしまいましたし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)

    #C0585
    ChrTalk(
        0x104,
        (
            "#00302F#11Pま、ギルドの遊撃士どもを\x01",
            "手伝うってのもアリかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x102, 0x2)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x104, 0x2)
    OP_63(0x105, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(1000)

    #C0586
    ChrTalk(
        0x102,
        "#6P#00105F……どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x105,
        "#10305F#12P気になる事でもあるのかい？\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    #C0588
    ChrTalk(
        0x101,
        (
            "#00003F#11Pいや……思ったんだけど。\x02\x03",

            "#00001F一度、《ローゼンベルク工房》を\x01",
            "訪ねてみないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0589
    ChrTalk(
        0x102,
        "#6P#00101Fあ……\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x109,
        "#6P#10101F《結社》に関係があるっていう……\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x104,
        (
            "#00303F#11Pそうか……\x01",
            "すっかり忘れてたな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1343F")

    #C0592
    ChrTalk(
        0x101,
        (
            "#00003F#11Pもちろん捜査令状がない以上、\x01",
            "強制捜査ができる訳じゃない。\x02\x03",

            "#00001Fだが……あの老人は\x01",
            "前にこんな風にも言っていた。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0593
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "だが今は、特に話すことが\x01",
            "あるわけでもあるまい。\x02\x03",

            "何か用件ができたら\x01",
            "改めて訪ねてくるがいい。\x02\x03",

            "レンに免じて話くらいは聞こう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Jump("loc_135A9")

    label("loc_1343F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13517")

    #C0594
    ChrTalk(
        0x101,
        (
            "#00006F#11Pもちろん捜査令状がない以上、\x01",
            "強制捜査ができる訳じゃない。\x02\x03",

            "#00001Fだが、レンから話を聞いた限り、\x01",
            "話が通じない相手でもなさそうだ。\x02\x03",

            "イメルダさんの依頼で\x01",
            "俺たちも一応、面識があるしな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135A9")

    label("loc_13517")


    #C0595
    ChrTalk(
        0x101,
        (
            "#00006F#11Pもちろん捜査令状がない以上、\x01",
            "強制捜査ができる訳じゃない。\x02\x03",

            "#00001Fだが、レンから話を聞いた限り、\x01",
            "話が通じない相手でもなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135A9")


    #C0596
    ChrTalk(
        0x103,
        (
            "#6P#00203F……訪ねてみる価値は\x01",
            "あるかもしれませんね。\x02\x03",

            "#00201F危険が伴うかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1369B")

    #C0597
    ChrTalk(
        0x105,
        (
            "#10304F#12P確かに、あの奇妙な少年の\x01",
            "目的くらいは掴んでおきたいね。\x02\x03",

            "#10302Fもしかしたらあの工房に\x01",
            "滞在してるのかもしれないし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1371F")

    label("loc_1369B")


    #C0598
    ChrTalk(
        0x105,
        (
            "#10304F#12P確かに、あの奇妙な少年の\x01",
            "目的くらいは掴んでおきたいね。\x02\x03",

            "#10302Fもしかしたらその工房に\x01",
            "滞在してるのかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1371F")


    #C0599
    ChrTalk(
        0x109,
        (
            "#6P#10100Fさ、賛成です！\x02\x03",

            "#10106Fただでさえ危険な外国勢力が\x01",
            "台頭しているこの状況……\x02\x03",

            "#10101Fこれ以上、怪しげな勢力を\x01",
            "放置するわけにはいきません！\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x102,
        (
            "#6P#00106Fそうね……\x02\x03",

            "#00101Fまずは工房を直接、\x01",
            "訪ねてみる形でいいのね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(250)

    #C0601
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ、様子を見てみよう。\x02\x03",

            "#00003F……場合によっては、捜査令状を\x01",
            "手配する必要があるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x104,
        (
            "#00303F#11Pだな……\x02\x03",

            "#00300Fよし、そんじゃあ\x01",
            "とっとと出かけるとすっか！\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x9,
        (
            "#6P#01105F#6Pねえねえ、みんな。\x02\x03",

            "もうお仕事に出かけるのー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0604
    ChrTalk(
        0x101,
        (
            "#00005F#11Pああ、そのつもりだけど。\x02\x03",

            "#00000Fキーアは今日は……\x01",
            "図書館に行くんだったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x9,
        (
            "#6P#01103Fんー、シズクのために\x01",
            "点字の本を探そうかなって。\x02\x03",

            "#01110Fお買い物して帰るけど\x01",
            "晩ゴハン、食べたいものあるー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0606
    ChrTalk(
        0x102,
        (
            "#5P#00105Fお買い物って……\x01",
            "キーアちゃん、大丈夫なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x103,
        (
            "#6P#00205F確かに料理は何度も\x01",
            "作ってもらっていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x9,
        (
            "#6P#01104Fうん、モモのお父さんとか\x01",
            "オスカーからいつも買ってるし。\x02\x03",

            "#01110Fデパートの食品コーナーの\x01",
            "おばちゃんとも仲いいよー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0609
    ChrTalk(
        0x101,
        "#00012F#11Pい、いつの間に……\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x104,
        "#00309F#11Pハハ、まあキー坊なら納得だぜ。\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x8,
        (
            "#5P#01004Fそうなると……\x01",
            "ちょいと涼しくなって来たし\x01",
            "鍋物なんかいいかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x109,
        (
            "#6P#10102Fあ、いいですね。\x01",
            "みんなで盛り上がれそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x105,
        (
            "#10302F#12P鍋っていうことは\x01",
            "やっぱり東方風なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x102,
        "#5P#00100Fキーアちゃん、大丈夫？\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x9,
        (
            "#6P#01103Fんー、何とかなると思う。\x02\x03",

            "#01101Fおダシをちゃんと取りたいから\x01",
            "東通りの露店街にも寄らないとー。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x104,
        "#00305F#11Pおおっ、本格的じゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x103,
        (
            "#6P#00202F帰って来た時の\x01",
            "お楽しみが出来ましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        (
            "#00009F#11Pありがとう、キーア。\x02\x03",

            "#00002F今日はなるべく\x01",
            "遅くならないように帰って来るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x9,
        "#6P#01109Fえへへ……うんっ！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    OP_4C(0xA, 0xFF)
    OP_49()
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 0)
    OP_29(0xA6, 0x1, 0x9)
    OP_29(0xA6, 0x4, 0x10)
    OP_29(0xA7, 0x4, 0x2)
    OP_29(0xA7, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141B4")
    Jump("loc_141B9")

    label("loc_141B4")

    OP_29(0x81, 0x4, 0x40)

    label("loc_141B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141CA")
    Jump("loc_141CF")

    label("loc_141CA")

    OP_29(0x82, 0x4, 0x40)

    label("loc_141CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141E0")
    Jump("loc_141E5")

    label("loc_141E0")

    OP_29(0x84, 0x4, 0x40)

    label("loc_141E5")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_12719 end

    def Function_41_14202(): pass

    label("Function_41_14202")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_142E1():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_142E1)
    Sleep(100)

    def lambda_142F1():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_142F1)
    Sleep(100)

    def lambda_14301():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_14301)
    Sleep(100)

    def lambda_14311():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14311)
    Sleep(100)

    def lambda_14321():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14321)
    Sleep(100)

    def lambda_14331():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_14331)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0620
    ChrTalk(
        0x105,
        "#11P#10300F幾つか新しいのも来ているね。\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x104,
        (
            "#5P#00300Fどうする？\x01",
            "先に人形工房に行ってから\x01",
            "片付けても良さそうだが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0622
    ChrTalk(
        0x101,
        (
            "#00003F#5Pいや、聞き込み次第では\x01",
            "どうなるかも分からない。\x02\x03",

            "#00001F急ぎの支援要請なんかは\x01",
            "先に片付けておいた方がいいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x109,
        (
            "#12P#10108Fそうですね……\x01",
            "強制捜査の必要があるかも\x01",
            "しれませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x102,
        (
            "#00100F#11Pじゃあ、準備が出来たら\x01",
            "山道の人形工房に行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x103,
        (
            "#6P#00203F（テーマパークのアルバイトは\x01",
            "  無性に心惹かれますね……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 1)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_41_14202 end

    def Function_42_1457F(): pass

    label("Function_42_1457F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    SoundLoad(128)
    SoundLoad(848)
    OP_68(12600, 2650, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 11300, 900, 5400, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x14)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1350, 6800, 0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12200, 1450, 7100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x11)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1300, 6800, 0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 5200, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x14)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 4900, 0)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12200, 1450, 5200, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x11)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 4900, 0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1450, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x14)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 3500, 0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2000, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x14)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1350, 1700, 0)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12200, 1450, 2000, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x11)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 1700, 0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 12200, 1450, 3800, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x11)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 12300, 1300, 3500, 0)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 16300, 750, 5500, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrSubChip(0xF, 0x8)
    SetChrSubChip(0x11, 0x8)
    SetChrSubChip(0x13, 0x8)
    SetChrSubChip(0x15, 0x8)
    SetChrSubChip(0x17, 0x8)
    SetChrSubChip(0x19, 0x8)
    SetChrSubChip(0x1B, 0x8)
    SetChrSubChip(0x1D, 0x8)
    Sound(128, 2, 50, 0)
    OP_68(12600, 2150, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0626
    ChrTalk(
        0x101,
        "#00004F#11P──ふう、ごちそうさま。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x104,
        (
            "#00309F#11Pいや～、冷えた身体に\x01",
            "雑炊ってのは嬉しいねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    #C0628
    ChrTalk(
        0x102,
        (
            "#5P#00102Fふふっ、そうね。\x01",
            "卵と鶏肉も入っていたし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(100)

    #C0629
    ChrTalk(
        0x109,
        "#12P#10109Fご馳走さま、キーアちゃん。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0630
    ChrTalk(
        0x103,
        "#6P#00202Fとても美味しかったです。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    #C0631
    ChrTalk(
        0x9,
        (
            "#6P#01104Fえへへ、昨日のお鍋の\x01",
            "材料を使っただけだけどー。\x02\x03",

            "#01110Fワジ、おなか一杯になったー？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0632
    ChrTalk(
        0x105,
        (
            "#10304F#11P……ああ。\x01",
            "染み入る美味しさだったよ。\x02\x03",

            "#10302Fご馳走さま、キーア。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x9,
        "#6P#01109Fえへへ、よかったー。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0634
    ChrTalk(
        0x8,
        (
            "#5P#01004Fフ……さぞ人心地付いただろ。\x02\x03",

            "#01000Fヴァルド・ヴァレスの件だが……\x01",
            "警備隊方面で捜索は続けられている。\x02\x03",

            "お前らがそこまで思い詰めるな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)

    #C0635
    ChrTalk(
        0x105,
        "#10304F#12P……ハハ、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x101,
        (
            "#00013F#11Pですが、ヴァルドが\x01",
            "どこかで《グノーシス》を\x01",
            "入手したのは間違いありません。\x02\x03",

            "そちらのルートを\x01",
            "何としても解明しないと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x8,
        (
            "#5P#01003Fそれについても\x01",
            "既に二課が動いている状況だ。\x02\x03",

            "一課も外国勢力の関与について\x01",
            "調査に入ったと聞いている。\x02\x03",

            "#01000Fまあ、そう焦るなってことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x101,
        "#00006F#11P……はい。\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x103,
        (
            "#6P#00200F結局、昨日の脱線現場は\x01",
            "一通り復旧できたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "#5P#01005Fああ、昨日の夕方までに\x01",
            "片側を通行できるようにしてから\x01",
            "夜通しで完全復旧したらしい。\x02\x03",

            "#01004Fそこまで大事にならずに済んだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x109,
        "#12P#10106Fふう……何よりでしたね。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x102,
        (
            "#6P#00103F大陸横断鉄道は大動脈……\x01",
            "もし停まったままだったら\x01",
            "今ごろ大混乱だったでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x104,
        (
            "#00306F#11Pそんな事になったらますます、\x01",
            "帝国と共和国のゴリ押しの材料に\x01",
            "されちまいそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    #C0644
    ChrTalk(
        0x101,
        (
            "#00003F#5Pああ……まったくだ。\x02\x03",

            "#00001F……とりあえず支援要請を\x01",
            "チェックしてみるか。\x02\x03",

            "そろそろ今日の分が\x01",
            "届いているかもしれないし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0645
    ChrTalk(
        0x102,
        "#6P#00100Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sound(848, 2, 100, 0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    #C0646
    ChrTalk(
        0x9,
        "#6P#01105Fつーしん、鳴ってるよ？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        "#00000F#11Pああ、俺が出るよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 15000, 850, 5700, 270)
    Sound(812, 0, 100, 0)
    OP_0D()
    OP_92(0x101, 0x3714, 0x300C, 0x1F4)
    OP_68(14100, 1850, 12300, 2500)

    def lambda_1532B():
        OP_95(0xFE, 14100, 850, 12300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1532B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x1)
    OP_24(0x350)
    Sound(838, 0, 100, 0)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0648
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001Fはい、こちらクロスベル警察、\x01",
            "特務支援課ですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0649
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……おはよ。\x01",
            "ギルド受付のミシェルよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0650
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fああ、お早うございます。\x02\x03",

            "#00001F《結社》についての報告は\x01",
            "ご覧になっていただけましたか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0651
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ……正直助かったわ。\x02\x03",

            "現在、レマン総本部に連絡して\x01",
            "情報を分析している所だけど……\x02\x03",

            "ま、得体の知れない連中だから\x01",
            "どこまで本当に動いているのか\x01",
            "判らないかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0652
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006F……そうですか。\x02\x03",

            "#00005Fえっと、その事を伝えに？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0653
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、ううん。\x01",
            "そうじゃないの。\x02\x03",

            "ちょっと聞きたいんだけど\x01",
            "うちのリンとエオリア、\x01",
            "見かけてないかしら……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_END)), "loc_1567E")
    SetMessageWindowPos(90, 130, -1, -1)

    #A0654
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001Fえっと、昨日病院で\x01",
            "会ったばかりですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_156D0")

    label("loc_1567E")

    SetMessageWindowPos(90, 130, -1, -1)

    #A0655
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fえっと、一昨日オルキスタワーで\x01",
            "会ったっきりですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_156D0")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そっか……そうよね。\x02\x03",

            "……まったくあの子たち、\x01",
            "一体何をしているのかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0657
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013Fえっと……\x01",
            "連絡が付かないんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0658
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、昨日の夜から\x01",
            "エニグマに繋がらなくって。\x02\x03",

            "ま、そう珍しい事じゃないから\x01",
            "あまり心配はしてないんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0659
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003Fそうですか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0660
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まあ、気にしないで。\x01",
            "アナタ達も忙しいんでしょうし。\x02\x03",

            "例の不良のリーダーだっけ？\x01",
            "そちらの方もヤバいんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0661
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00008F……ええ、まあ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0662
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もし２人を見かけたら\x01",
            "すぐに連絡するように言って頂戴。\x02\x03",

            "それじゃ、そちらも頑張ってね㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0663
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004Fはい、お疲れさまです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0664
    ChrTalk(
        0x8,
        (
            "#01000Fギルドからみたいだが、\x01",
            "どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0665
    ChrTalk(
        0x101,
        "#00001F#5Pあ、はい……\x02",
    )

    CloseMessageWindow()
    OP_68(12920, 1850, 6140, 2000)
    MoveCamera(35, 17, 0, 2000)

    def lambda_15A41():
        OP_96(0xFE, 0x319C, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A41)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    SetChrName("")

    #A0666
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士のリンとエオリアが昨夜から\x01",
            "連絡が付かなくなっている事を伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0667
    ChrTalk(
        0x102,
        "#6P#00101Fあの人たちが……\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x105,
        (
            "#10301F#12Pどちらもかなりの手練の\x01",
            "お姉さんたちだったよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x104,
        (
            "#00303F#11Pああ、特にエオリアさんは\x01",
            "セシルさんに次ぐ俺のタイプだな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0670
    ChrTalk(
        0x103,
        "#6P#00211Fそれはどうでもいいかと……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15CD5")

    #C0671
    ChrTalk(
        0x109,
        (
            "#12P#10106F#Nでも、ちょっと心配ですね。\x02\x03",

            "#10108Fお２人ともスケジュール管理は\x01",
            "相当しっかりしてそうですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0672
    ChrTalk(
        0x101,
        (
            "#5P#00006Fそうだな……\x01",
            "前に手合わせをした時も\x01",
            "分刻みで動いてる感じだったし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D88")

    label("loc_15CD5")


    #C0673
    ChrTalk(
        0x109,
        (
            "#12P#10106F#Nでも、ちょっと心配ですね。\x02\x03",

            "#10101F遊撃士ともなるとスケジュール管理は\x01",
            "相当しっかりしてそうですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0674
    ChrTalk(
        0x101,
        (
            "#5P#00003Fそうだな……\x01",
            "アリオスさんもそうみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D88")


    #C0675
    ChrTalk(
        0x8,
        (
            "#01003F#11Pま、余裕があれば仕事がてら\x01",
            "ギルドに顔を出してやるといい。\x02\x03",

            "#01002Fこういう時はお互いさまだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x101,
        "#5P#00000Fええ、判りました。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x9,
        (
            "#6P#01105Fロイドたち、\x01",
            "もう出かけるのー？\x02\x03",

            "#01102F今日はお鍋、大丈夫そう？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15E6E():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15E6E)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0678
    ChrTalk(
        0x101,
        (
            "#5P#00002Fああ、今日は\x01",
            "絶対に早めに戻るからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x102,
        (
            "#5P#00106Fごめんね、キーアちゃん。\x02\x03",

            "#00108Fせっかく用意してくれたのに\x01",
            "昨日は食べられなくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x9,
        (
            "#6P#01121Fううん、それだけみんな\x01",
            "頑張ってるんだよねー？\x02\x03",

            "#01109Fだったらキーアも\x01",
            "頑張ってお手伝いしたいモン。\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x9, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    #C0681
    ChrTalk(
        0x101,
        "#5P#00002Fキーア……\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x105,
        (
            "#10309F#11Pハハ……\x01",
            "なかなかの破壊力だね。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0683
    ChrTalk(
        0x103,
        (
            "#6P#00204F天気予報では、午後には\x01",
            "雨も止むみたいですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x104,
        (
            "#00307F#11Pバッチリ仕事を片付けて\x01",
            "とっとと帰ってくるとすっか！\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x109,
        "#12P#10102F#Nはい……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 0)
    OP_29(0xA8, 0x1, 0xB)
    OP_29(0xA8, 0x1, 0xC)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    SubItemNumber(0x330, 1)
    SubItemNumber(0x331, 1)
    SubItemNumber(0x332, 1)
    SubItemNumber(0x33A, 1)
    Call(0, 67)
    ReplaceBGM("ed7150", -1)
    ReplaceBGM("ed7101", "ed7562")
    ReplaceBGM("ed7116", "ed7562")
    OP_24(0x350)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_42_1457F end

    def Function_43_16393(): pass

    label("Function_43_16393")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 11300, 900, 3800, 90)
    SetChrPos(0x102, 13900, 900, 7000, 270)
    SetChrPos(0x103, 13900, 900, 2200, 270)
    SetChrPos(0x104, 11300, 900, 7000, 90)
    SetChrPos(0x109, 13900, 900, 5400, 270)
    SetChrPos(0x105, 11300, 900, 2200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 11300, 900, 5400, 90)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13900, 900, 3800, 270)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 14120, 850, 10500, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0686
    AnonymousTalk(
        0x8,
        "#01003F──そうか、戻るのか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0687
    ChrTalk(
        0x109,
        (
            "#10106F#11Pはい……本当なら半年は\x01",
            "勉強させて頂くつもりでしたが……\x02\x03",

            "#10101F色々考えて──\x01",
            "戻らせていただく事にしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        "#6P#00006F……そっか………\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x102,
        (
            "#5P#00106F……無理もないわ。\x02\x03",

            "#00108F今回の件で警備隊も\x01",
            "かなりの損害を負ったみただし。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x104,
        (
            "#5P#00306Fま、優秀な若手隊員は\x01",
            "喉から手が出るほど欲しいだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x109,
        (
            "#10112F#11Pあはは……\x01",
            "優秀かどうかは疑問ですけど。\x02\x03",

            "#10108F……すみません。\x01",
            "せっかく復興作業が一段落して\x01",
            "通常業務に戻れた矢先に……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x101,
        (
            "#6P#00004Fいや……気にしないでくれ。\x02\x03",

            "#00002F今のクロスベルの状況で\x01",
            "警備隊の役割は大きいしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x103,
        (
            "#00206F#11P寂しくなりますけど……\x01",
            "納得するしかありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x9,
        (
            "#01108F#11Pノエル……\x01",
            "居なくなっちゃうのー？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0695
    ChrTalk(
        0x109,
        (
            "#10112F#5Pあはは……うん。\x02\x03",

            "キーアちゃんに会えなくなるのは\x01",
            "すごく寂しいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x9,
        "#01106F#11P……そっか………\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x109,
        (
            "#10102F#5Pでも、またいつでも\x01",
            "遊びに来ちゃうから……！\x02\x03",

            "#10100F#30Wそれこそフランと一緒に……\x02\x01",

            "#10108F#45W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    #C0698
    ChrTalk(
        0x9,
        "#01112F#11Pノエルぅ……\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x103,
        "#00208F#11Pノエルさん……\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x105,
        (
            "#6P#10301F……妹さん、しばらく\x01",
            "退院できなさそうだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x109,
        (
            "#10106F#5Pうん……手術は成功したし\x01",
            "意識も取り戻したから\x01",
            "もう心配はないんだけど……\x02\x03",

            "#10113Fやっぱり体力が全然、\x01",
            "戻っていないみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x102,
        "#5P#00103F……そう………\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        "#5P#00308F………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    #C0704
    ChrTalk(
        0x109,
        (
            "#10112F#11Pあはは……先輩、\x01",
            "そんな顔しないで下さいよ。\x02\x03",

            "#10104Fあの子だって警察官ですから\x01",
            "相応の危険は覚悟してましたし。\x02\x03",

            "#10100F自分にも責任があるとか……\x01",
            "思ったらダメですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x104,
        (
            "#5P#00304F……ハハ、分かった。\x02\x03",

            "#00302Fしかし、そうなると\x01",
            "今日がノエルの仕事納めか。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x109,
        (
            "#10104F#11Pはい、今日一日、\x01",
            "精一杯頑張らせてもらいます。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0707
    ChrTalk(
        0x109,
        "#10102F#11Pよろしくお願いします、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        "#6P#00004Fああ……こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x102,
        (
            "#5P#00102Fノエルさん……\x01",
            "よろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x8,
        (
            "#6P#01003F──各種手続きは\x01",
            "俺の方でやっておこう。\x02\x03",

            "#01002Fそれと、晩メシは久々に\x01",
            "どこか外にでも繰り出すか。\x02\x03",

            "特別に俺のオゴりにしてやる。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x9, 0x0)

    #C0711
    ChrTalk(
        0x109,
        "#10105F#11Pセルゲイ課長……\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        "#6P#00002Fはは、いいですね。\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x103,
        "#00202F#11Pなかなかの太っ腹です。\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x105,
        (
            "#6P#10309Fフフ、それなら僕の馴染みの\x01",
            "ホストクラブでも行くかい？\x02\x03",

            "#10302F綺麗どころを集めて\x01",
            "豪勢な送別会を準備するけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0715
    ChrTalk(
        0x109,
        "#10111F#5Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x104,
        (
            "#5P#00305Fおっ、アリかもしれねぇな。\x02\x03",

            "#00309F俺としては綺麗な姉ちゃんの\x01",
            "いる店の方が嬉しいが。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(100)

    #C0717
    ChrTalk(
        0x102,
        (
            "#11P#00111Fふう……\x01",
            "そういう問題じゃないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x103,
        (
            "#00201F#11Pならば、みっしぃショーがある\x01",
            "ＭＷＬ内のレストランとか……（キラリ）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)

    #C0719
    ChrTalk(
        0x9,
        "#01105F#5Pそんなお店があるのー？\x02",
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x8,
        (
            "#6P#01006Fそれ以前にお前ら……\x01",
            "俺の財布の中身を考えろっての。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0721
    ChrTalk(
        0x109,
        "#10112F#11Pあはは……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0722
    ChrTalk(
        0x101,
        (
            "#6P#00012Fとりあえず今日は、夜までに\x01",
            "仕事を終わらせないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xA,
        "#01203F#5P#Nグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_49()
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 2)
    Call(0, 67)
    OP_32(0x6, 0x0, 0x49)
    OP_42(0x6, 0x3EF, 0xFF)
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)
    OP_29(0xAB, 0x1, 0x3)
    OP_29(0xAB, 0x4, 0x10)
    OP_29(0xAC, 0x4, 0x2)
    OP_29(0xAC, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C9(0x0, 0x10000)
    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_43_16393 end

    def Function_44_1735F(): pass

    label("Function_44_1735F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_1743E():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1743E)
    Sleep(100)

    def lambda_1744E():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1744E)
    Sleep(100)

    def lambda_1745E():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1745E)
    Sleep(100)

    def lambda_1746E():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1746E)
    Sleep(100)

    def lambda_1747E():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1747E)
    Sleep(100)

    def lambda_1748E():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1748E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0724
    ChrTalk(
        0x102,
        "#00108F#11Pさすがに数が多いわね……\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x103,
        (
            "#6P#00200Fですが、緊急性の高いものは\x01",
            "来ていなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそうだね、アッバスのも\x01",
            "余裕があればって感じだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x104,
        (
            "#6P#00303Fま、各地を回りつつ\x01",
            "ボチボチ進めてみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x109,
        "#12P#10101Fはい！\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0729
    ChrTalk(
        0x101,
        (
            "#00003F#5P──なあ、みんな。\x02\x03",

            "#00002F仕事の合間でいいから\x01",
            "ウルスラ病院に行かないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)

    def lambda_1768D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1768D)
    Sleep(50)

    def lambda_1769D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1769D)
    Sleep(50)

    def lambda_176AD():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_176AD)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0730
    ChrTalk(
        0x109,
        "#12P#10105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x102,
        (
            "#00102F#11Pそうね……いいと思うわ。\x02\x03",

            "#00104Fここ一週間ほど、忙しすぎて\x01",
            "様子を見に行けなかったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x104,
        (
            "#6P#00304F賛成だぜ。\x02\x03",

            "#00302Fフランちゃんが目を覚ましたんなら\x01",
            "是非ともお見舞いしねぇとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x109,
        "#12P#10108Fで、でも……\x02",
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x105,
        (
            "#12P#10304F確かに端末で、\x01",
            "あの賑やかな声が聞けないのは\x01",
            "どうにも寂しい感じだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x103,
        (
            "#6P#00201Fはい……\x01",
            "せめて声だけでも聞きたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#00004F#5Pノエル、遠慮しないでくれ。\x02\x03",

            "#00000F俺たちにとってもフランは\x01",
            "大切なサポート役なんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_178BE():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_178BE)
    Sleep(50)

    def lambda_178CE():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_178CE)
    Sleep(50)

    def lambda_178DE():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_178DE)
    Sleep(50)

    def lambda_178EE():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_178EE)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0737
    ChrTalk(
        0x109,
        (
            "#12P#10104F皆さん……\x01",
            "ありがとうございます。\x02\x03",

            "#10102Fそれじゃあ、一区切り付いたら\x01",
            "ウルスラ病院に行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 3)
    OP_29(0xAC, 0x1, 0x1)
    Call(0, 67)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7101", "ed7563")
    ReplaceBGM("ed7116", "ed7563")
    ReplaceBGM("ed7123", "ed7515")
    EventEnd(0x5)
    Return()

    # Function_44_1735F end

    def Function_45_179D0(): pass

    label("Function_45_179D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05901.itp")
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50091.itc", 0x22)
    SoundLoad(848)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 4900, 130, 6250, 180)
    SetChrPos(0x102, 6050, 130, 6250, 180)
    SetChrPos(0x103, 4600, 130, 2200, 0)
    SetChrPos(0x104, 6400, 130, 2200, 0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5500, 130, 2200, 0)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -900, 0, 4100, 135)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 13800, 850, 13000, 0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x1D)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 4900, 330, 4600, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x1D)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 6000, 330, 3900, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0738
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W　　　　　 ２日後──\x02\x03",

            "クロスベルの国家独立の是非を問う、\x01",
            "住民投票が施行された。\x02\x03",

            "その結果は、即日開票され……\x02\x03",

            "その１週間後──\x01",
            "クロスベルは“運命の日”を迎えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    UseItem(0x2E9, 0xFF)
    AddItemNumber(0x2E9, 1)
    Sleep(1500)
    Sound(18, 0, 100, 0)
    UseItem(0x2EA, 0xFF)
    AddItemNumber(0x2EA, 1)
    OP_68(6020, 3950, 4710, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22800, 0)
    PlayBGM("ed7251", 0)
    Sleep(1500)
    OP_68(6020, 950, 4710, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(22000, 100000)
    MoveCamera(35, 18, 0, 100000)
    Sleep(500)

    #C0739
    ChrTalk(
        0x101,
        "#5P#00013F………………………………\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x104,
        (
            "#00301F……こりゃ、\x01",
            "とんでもない事になったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x102,
        (
            "#5P#00106Fええ……\x01",
            "正直、考えられないくらいの\x01",
            "展開の早さだわ。\x02\x03",

            "#00108F……おじいさまにも\x01",
            "確認しようと思ったのだけど\x01",
            "昨日から連絡が付かないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#12P#00206F課長も朝早くに本部に出かけたきり、\x01",
            "帰って来ませんね……\x02\x03",

            "#00201F『国防軍』という組織について\x01",
            "確認しに行ったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x101,
        (
            "#5P#00006Fああ……\x01",
            "正直、寝耳に水だからな。\x02\x03",

            "#00001F俺たちだけじゃなくて\x01",
            "警察上層部も同じらしいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x104,
        (
            "#00306Fオイオイ……\x01",
            "さすがにそりゃおかしいだろ。\x02\x03",

            "#00301Fノエルやミレイユたちの方は\x01",
            "どうしてんだ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    #C0745
    ChrTalk(
        0x103,
        (
            "#6P#00208F現在、警備隊方面とは\x01",
            "連絡が付かなくなっていますね。\x02\x03",

            "恐らく問い合わせが多すぎて\x01",
            "情報を遮断しているのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x102,
        (
            "#5P#00103F……無理もないわ。\x02\x03",

            "#00101Fこの資産凍結にしても……\x01",
            "帝国や共和国が\x01",
            "黙っているはずがないし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)

    #C0747
    ChrTalk(
        0x101,
        (
            "#5P#00008F『実力行使も辞さない』……\x01",
            "国境方面が心配だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x9,
        "#12P#01108F#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(250)

    #C0749
    ChrTalk(
        0x101,
        (
            "#5P#00002Fゴメン……\x01",
            "不安にさせちゃったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x9,
        (
            "#12P#01121F……ううん。\x01",
            "大変なことが起きてるのは\x01",
            "キーアにだって分かるし。\x02\x03",

            "#01105Fそれよりワジ、\x01",
            "朝から見かけないねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x101,
        "#5P#00005Fああ、そういえば……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0752
    ChrTalk(
        0x103,
        (
            "#12P#00205Fあ、ワジさんなら野暮用で\x01",
            "出かけるって言ってました。\x02\x03",

            "#00200F課長が出た後だったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x101,
        "#5P#00001Fそうなのか？\x02",
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x102,
        (
            "#5P#00106Fもう、こんな時に\x01",
            "ちょっと感心しないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    #C0755
    ChrTalk(
        0x104,
        "#00308Fふむ……\x02",
    )

    CloseMessageWindow()
    Sound(808, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x101, 0x2)
    Sleep(250)
    MoveCamera(35, 18, 0, 2000)
    OP_68(2300, 950, 2300, 2000)
    SetCameraDistance(24000, 2000)
    OP_6F(0x79)

    #C0756
    ChrTalk(
        0x102,
        "#00105Fこんな時に……\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x104,
        "#00301F誰だ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 4900, 30, 5500, 180)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)

    def lambda_183D1():
        OP_95(0xFE, 3500, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_183D1)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xE1, 0x1F4)

    #C0758
    ChrTalk(
        0x101,
        (
            "#00001F──はい！\x01",
            "どちらさまですか！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, 1000, -1000, -2000, 0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)

    #N0759
    NpcTalk(
        0xB,
        "女性の声",
        (
            "#1P#2Sよかった……\x01",
            "いてくれたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #N0760
    NpcTalk(
        0xB,
        "女性の声",
        "#1P#2S私よ、セシルだけど。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0761
    ChrTalk(
        0x101,
        "#00011Fセシル姉！？\x02",
    )

    CloseMessageWindow()

    def lambda_18547():
        OP_95(0xFE, 1000, 0, 2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18547)
    WaitChrThread(0x101, 1)

    def lambda_18565():
        OP_95(0xFE, 1000, 0, 1000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18565)
    WaitChrThread(0x101, 1)
    Sound(806, 0, 80, 0)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_18592():
        OP_96(0xFE, 0x3E8, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18592)
    Sleep(500)
    SetChrPos(0xB, 1000, 0, -1500, 0)

    def lambda_185C0():
        OP_96(0xFE, 0x3E8, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_185C0)

    def lambda_185DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_185DA)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)

    #C0762
    ChrTalk(
        0x9,
        "#12P#01110Fあ、セシルだー。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 46)
    Sleep(250)
    OP_68(4500, 1100, 3300, 2000)
    OP_93(0x101, 0x2D, 0x1F4)

    def lambda_18635():
        OP_95(0xFE, 2000, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18635)
    Sleep(500)

    def lambda_18652():
        OP_95(0xFE, 2000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18652)
    WaitChrThread(0x101, 1)

    def lambda_18670():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18670)
    WaitChrThread(0xB, 1)

    def lambda_18681():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18681)
    OP_6F(0x79)

    #C0763
    ChrTalk(
        0x102,
        (
            "#5P#00105Fセシルさん……\x01",
            "どうなさったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x104,
        (
            "#00302Fここに来てくれるなんて\x01",
            "珍しいッスね？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0765
    AnonymousTalk(
        0xB,
        (
            "ごめんなさい。\x01",
            "いきなり訪ねてしまって。\x02\x03",

            "その……アリオスさんとか\x01",
            "こちらに来たりしていないわよね？\x02",
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

    #C0766
    ChrTalk(
        0x101,
        "#00005F#5P……アリオスさん？\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x103,
        (
            "#12P#00205F来ていませんが……\x01",
            "どういう事でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xB,
        (
            "#6P#05926F……それが………\x02\x03",

            "#05928F昨夜、夜遅くに病院に来て\x01",
            "シズクちゃんを連れていったの。\x02\x03",

            "その場で退院の手続きも\x01",
            "してしまって……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0769
    ChrTalk(
        0x101,
        "#00005F#5Pえっ！？\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x102,
        "#5P#00101Fそれって……！？\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x9,
        "#12P#01112Fシズクが……\x02",
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0xB,
        (
            "#6P#05926Fそれで、どういう事情なのか\x01",
            "確かめに来たのだけど……\x02\x03",

            "ギルドのミシェルさんも\x01",
            "全く心当たりがないみたいで。\x02\x03",

            "#05921Fそれで念のため\x01",
            "あなた達の所も訪ねてみたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x101,
        "#00001F#5Pそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x104,
        (
            "#00301Fあのオッサン……\x01",
            "何だってそんなことを。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x103,
        (
            "#12P#00201F夜遅くというのも\x01",
            "普通ではない気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x9,
        "#12P#01108F………………………………\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    Sound(848, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(14100, 1750, 12300, 3000)
    MoveCamera(40, 17, 0, 3000)
    SetCameraDistance(22500, 3000)
    SetChrSubChip(0x9, 0x2)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)

    def lambda_18BC6():
        TurnDirection(0x101, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18BC6)
    Sleep(50)

    def lambda_18BD6():
        TurnDirection(0x102, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18BD6)
    Sleep(50)

    def lambda_18BE6():
        TurnDirection(0xB, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_18BE6)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    OP_6F(0x79)

    #C0777
    ChrTalk(
        0x101,
        "#00011Fっと……\x02",
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x104,
        (
            "#00301Fエニグマじゃねぇって事は\x01",
            "課長じゃなさそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x102,
        "#00105Fまさかアリオスさん関係とか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(24000, 5000)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 49)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 50)
    Sleep(500)
    BeginChrThread(0x9, 3, 0, 51)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 52)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Sleep(300)
    OP_24(0x350)
    Sound(838, 0, 100, 0)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    Sleep(500)

    #C0780
    ChrTalk(
        0x101,
        (
            "#11P#00001Fはい、こちらクロスベル警察、\x01",
            "特務支援課──\x02",
        )
    )

    WaitChrThread(0xB, 3)
    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0781
    NpcTalk(
        0xE,
        "女性の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S#5Pよかった！\x01",
            "ロイド君、そこにいたのね！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x101,
        "#11P#00011Fわっ……\x02",
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x103,
        (
            "#6P#00200F通話設定がスピーカーに\x01",
            "なっていたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x102,
        "#12P#00105Fこの声……グレイスさん？\x02",
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x104,
        "#12P#00300Fそうみてぇだな。\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        (
            "#11P#00000Fえっと……\x01",
            "グレイスさん、どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5Pどうしたもこうしたも……\x01",
            "あなた達にも教えとこうと思って！\x02\x03",

            "さっき、オルキスタワーから\x01",
            "とんでもない通達があったのよ！\x02\x03",

            "どうやらディーター市長が\x01",
            "『クロスベル独立国』の\x01",
            "初代大統領に就任したらしいわ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0788
    ChrTalk(
        0x101,
        "#11P#00007Fな──\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x103,
        "#6P#00205F初代大統領……\x02",
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x102,
        (
            "#12P#00107F大統領って……\x01",
            "お、おじさまが！？\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x104,
        (
            "#12P#00305Fオイオイ……\x01",
            "なんの冗談だよ、そりゃ？\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5Pあ、あたしだって\x01",
            "最初は冗談だと思ったわよ！\x02\x03",

            "でも、その通達をしてきたのが\x01",
            "白い軍服を着た兵士で……\x02\x03",

            "発表されたばかりの\x01",
            "『国防軍』って名乗ったわよ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x101,
        "#11P#00013Fほ、本当ですか！？\x02",
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x104,
        "#12P#00301F兵士ってことは、まさか……\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5Pええ、多分警備隊の\x01",
            "メンバーなんでしょうけど……\x02\x03",

            "そ、それと驚かないでね……？\x02\x03",

            "就任直後にディーター大統領が\x01",
            "『国防長官』の任命を行ったの。\x02\x03",

            "それも──#350W─\x01",
            "#20Wあの、アリオスさんに#20R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)

    #C0796
    ChrTalk(
        0x101,
        "#11P#00005F──へ。\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x102,
        "#12P#00105F#30W……それって……\x02",
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x104,
        "#12P#00303F#30Wん～～っ……？\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x103,
        "#6P#00208F#30Wアリオス、さん……？\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0xB,
        "#6P#05925F#30W………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("ロイドたち")
    Fade(500)
    SetCameraDistance(24500, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)

    #A0801
    AnonymousTalk(
        0xFF,
        "#5S#16Aえええええええっ！！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(500)

    #C0802
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5Pちょうどこれから\x01",
            "大統領の就任演説が始まるらしいわ！\x02\x03",

            "導力ネットでも配信するみたいだから\x01",
            "よかったら見ておきなさい！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0803
    NpcTalk(
        0xE,
        "青年の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#1S……グレイス先輩！\x01",
            "何とか取材許可が下りました！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#2Sよっしゃ！\x01",
            "レインズ君、でかしたわ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    #C0805
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#3S──ゴメン！\x01",
            "これから就任演説の取材なの！\x02\x03",

            "それじゃあまたね～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    Sleep(500)

    #C0806
    ChrTalk(
        0xB,
        "#6P#05928F今のは……本当なの？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0807
    ChrTalk(
        0x101,
        (
            "#00006Fわ、分からないけど……\x02\x03",

            "#00013Fあのアリオスさんが\x01",
            "『国防長官』……？\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x102,
        (
            "#12P#00107F長官ということは\x01",
            "『国防軍』のトップ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x104,
        (
            "#12P#00310Fあ、ありえねぇだろ……\x01",
            "遊撃士の肩書きはどうすんだ！？\x02\x03",

            "#00306Fディーターのオッサンが\x01",
            "大統領ってのも唐突過ぎるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x103,
        (
            "#6P#00201F……とにかく端末で\x01",
            "就任演説を見てみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        "#00007Fああ……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x350)
    SetScenarioFlags(0x22, 4)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_179D0 end

    def Function_46_197E0(): pass

    label("Function_46_197E0")

    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 6050, 30, 5500, 180)
    OP_0D()

    def lambda_19809():
        OP_95(0xFE, 4750, 30, 5500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19809)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_46_197E0 end

    def Function_47_1982A(): pass

    label("Function_47_1982A")

    SetChrPos(0x101, 4100, 850, 10800, 90)

    def lambda_19840():
        OP_96(0xFE, 0x3138, 0x352, 0x2A30, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19840)
    WaitChrThread(0x101, 1)

    def lambda_1985E():
        OP_95(0xFE, 14100, 850, 12300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1985E)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_47_1982A end

    def Function_48_1987F(): pass

    label("Function_48_1987F")

    SetChrPos(0x102, 4300, 850, 10200, 90)

    def lambda_19895():
        OP_96(0xFE, 0x37DC, 0x352, 0x27D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19895)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_48_1987F end

    def Function_49_198B6(): pass

    label("Function_49_198B6")

    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 2650, 850, 9600, 90)

    def lambda_198D9():
        OP_96(0xFE, 0x316A, 0x352, 0x2580, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_198D9)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    Return()

    # Function_49_198B6 end

    def Function_50_198FA(): pass

    label("Function_50_198FA")

    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 2200, 850, 11000, 90)

    def lambda_1991D():
        OP_96(0xFE, 0x2FA8, 0x352, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1991D)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_50_198FA end

    def Function_51_1993E(): pass

    label("Function_51_1993E")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 800, 850, 10300, 90)

    def lambda_1995C():
        OP_96(0xFE, 0x2A30, 0x352, 0x283C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1995C)
    WaitChrThread(0x9, 1)
    Return()

    # Function_51_1993E end

    def Function_52_19976(): pass

    label("Function_52_19976")

    SetChrPos(0xB, 800, 850, 11500, 90)

    def lambda_1998C():
        OP_96(0xFE, 0x2A30, 0x352, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1998C)
    WaitChrThread(0xB, 1)
    Return()

    # Function_52_19976 end

    def Function_53_199A6(): pass

    label("Function_53_199A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch08201.itc", 0x1F)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(15900, 2250, 9800, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 15150, 870, 8450, 45)
    SetChrPos(0x102, 16200, 850, 7400, 0)
    SetChrPos(0x104, 17200, 850, 7800, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14500, 850, 10500, 90)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13900, 850, 9700, 90)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    PlayBGM("ed7561", 0)
    OP_68(15900, 1750, 9800, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    OP_64(0x9)
    Sleep(500)

    #C0812
    ChrTalk(
        0x101,
        "#6P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_19B8E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19B8E)
    Sleep(50)

    def lambda_19B9E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19B9E)
    Sleep(50)

    def lambda_19BAE():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19BAE)
    Sleep(50)

    def lambda_19BBE():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_19BBE)
    Sleep(50)

    def lambda_19BCE():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_19BCE)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x101, 2)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0813
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007Fはい、ロイドです……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0814
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……おう、俺だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0815
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010F課長！\x01",
            "今の就任演説は──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0816
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……当然、見ていた。\x02\x03",

            "まあ、是非はともかく、\x01",
            "警備隊は『国防軍』として\x01",
            "完全に再編成されたようだ。\x02\x03",

            "俺たち警察も、その一部として\x01",
            "組み込まれる事が決定している。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0817
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006Fそ、そんな……\x02\x03",

            "#00013Fひょっとして\x01",
            "ソーニャ司令も……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0818
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "映像に映ってただろ？\x01",
            "まあ──了承したんだろう。\x02\x03",

            "どうなるか分からんが……\x01",
            "今はオルキスタワーには\x01",
            "近付かないようにしておけ。\x02\x03",

            "国防軍の“兵士”たちが\x01",
            "厳重に警備しているはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0819
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010Fくっ……了解しました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0820
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──また連絡する。\x01",
            "あんま先走るんじゃねえぞ？\x07\x00\x02",
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
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0821
    ChrTalk(
        0x102,
        "#12P#00108F……課長はなんと？\x02",
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
    TurnDirection(0x101, 0x102, 500)

    #C0822
    ChrTalk(
        0x101,
        "#5P#00006Fああ、国防軍だけど……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0823
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルゲイから聞いた話をエリィたちに説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0824
    ChrTalk(
        0x102,
        "#12P#00106Fそう……\x02",
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x104,
        (
            "#00301F#12Pくっ、ソーニャ司令が\x01",
            "あっち側に回ったのかよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x103,
        (
            "#5P#00206Fまあ、立場からすると\x01",
            "仕方のないことかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0xB,
        (
            "#05923F#5P……アリオスさん。\x01",
            "シズクちゃんを連れていったのは\x01",
            "この事が原因だったのね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A18C():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A18C)
    Sleep(50)

    def lambda_1A19C():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A19C)
    Sleep(50)

    def lambda_1A1AC():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A1AC)
    Sleep(50)

    def lambda_1A1BC():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A1BC)
    Sleep(50)

    def lambda_1A1CC():
        TurnDirection(0x9, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1A1CC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x9, 0)

    #C0828
    ChrTalk(
        0x101,
        "#12P#00005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x102,
        (
            "#12P#00108Fそうですね……\x01",
            "あんな立場になってしまったら\x01",
            "シズクちゃんにも影響が……\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x104,
        (
            "#00306F#12P反対派に狙われる可能性とか\x01",
            "出てくるかもしれねぇしな……\x02",
        )
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x103,
        (
            "#11P#00208F……この状況ですと\x01",
            "無いとは言い切れないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x9,
        "#01108F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x101,
        (
            "#12P#00004Fキーア……大丈夫だ。\x02\x03",

            "#00000Fシズクちゃんに危険が及ばないよう\x01",
            "アリオスさんも考えてるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A379():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A379)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(200)

    #C0834
    ChrTalk(
        0x9,
        (
            "#01121F#5Pうん……そうだね。\x02\x03",

            "#01122F……えへへ。\x01",
            "ちょっと心配だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0xB,
        "#5P#05921Fキーアちゃん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0836
    ChrTalk(
        0x101,
        (
            "#12P#00008F……セシル姉、悪いんだけど\x01",
            "ちょっと留守番を頼めないかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A4C6():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1A4C6)
    Sleep(50)

    def lambda_1A4D6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A4D6)
    Sleep(50)

    def lambda_1A4E6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A4E6)
    Sleep(50)

    def lambda_1A4F6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A4F6)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    #C0837
    ChrTalk(
        0x9,
        "#01105F#5Pロイド……？\x02",
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0xB,
        (
            "#05925F#5Pええ、夕方までなら\x01",
            "大丈夫だと思うけど……\x02\x03",

            "#05921Fどこかに出かけるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x101,
        "#12P#00003Fああ──\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0840
    ChrTalk(
        0x101,
        (
            "#5P#00001Fなあ、みんな。\x02\x03",

            "とりあえず……\x01",
            "ギルドを訪ねてみないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0841
    ChrTalk(
        0x102,
        "#12P#00101Fそ、それもそうね。\x02",
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x103,
        (
            "#5P#00201F確かにアリオスさんの件は\x01",
            "事情をお聞きしたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x104,
        (
            "#00303F#12Pだな……\x01",
            "さすがに寝耳に水だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0844
    ChrTalk(
        0xB,
        (
            "#05923F#5P……わかったわ。\x01",
            "キーアちゃんと一緒に\x01",
            "ここで留守番しているから。\x02\x03",

            "#05920F大変な状況みたいだけど……\x01",
            "くれぐれも気を付けてね。\x02\x03",

            "無茶だけはしないこと。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A77B():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A77B)
    Sleep(50)

    def lambda_1A78B():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A78B)
    Sleep(50)

    def lambda_1A79B():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A79B)
    Sleep(50)

    def lambda_1A7AB():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A7AB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    #C0845
    ChrTalk(
        0x101,
        "#12P#00002Fああ、分かってる。\x02",
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x104,
        "#00309F#12Pセシルさん、感謝ッス！\x02",
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x102,
        "#12P#00104Fそれではお願いします。\x02",
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x103,
        (
            "#11P#00202Fキーア、セシルさんと一緒に\x01",
            "いい子でお留守番しててください。\x02",
        )
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0x9,
        "#01112F#5Pあ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_1A8B4():

        label("loc_1A8B4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1A8B4")

    QueueWorkItem2(0xB, 2, lambda_1A8B4)

    def lambda_1A8C6():

        label("loc_1A8C6")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1A8C6")

    QueueWorkItem2(0x9, 2, lambda_1A8C6)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 54)
    Sleep(350)
    BeginChrThread(0x103, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 54)
    EndChrThread(0xB, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(14150, 1750, 10040, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0xB, 14500, 850, 10700, 270)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0850
    ChrTalk(
        0x9,
        "#11P#01101F……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A99B():

        label("loc_1A99B")

        TurnDirection(0xB, 0x9, 500)
        Yield()
        Jump("loc_1A99B")

    QueueWorkItem2(0xB, 2, lambda_1A99B)

    #C0851
    ChrTalk(
        0xB,
        "#05925F#5Pキーアちゃん？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetCameraDistance(24500, 2000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)

    def lambda_1A9E4():
        OP_95(0xFE, 900, 850, 9700, 5500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A9E4)
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xB, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x238), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x323)
    SetScenarioFlags(0x182, 1)
    SetScenarioFlags(0x23, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_199A6 end

    def Function_54_1AA4A(): pass

    label("Function_54_1AA4A")

    OP_95(0xFE, 15150, 850, 8450, 4500, 0x1)
    OP_95(0xFE, 10150, 850, 8950, 4500, 0x1)
    OP_95(0xFE, 5150, 850, 9450, 4500, 0x1)
    OP_95(0xFE, 150, 850, 9450, 4500, 0x1)
    Return()

    # Function_54_1AA4A end

    def Function_55_1AA9B(): pass

    label("Function_55_1AA9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1000, 1000, 5300, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 300, -1000, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x103, 300, 0, -3000, 0)
    SetChrPos(0x104, 1400, 0, -3300, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x2B, 800, 0, 2000, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 2300, 0, 5300, 270)
    SetChrChipByIndex(0xB, 0x7)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetCameraDistance(22500, 5000)
    FadeToBright(2000, 0)

    def lambda_1AB96():
        OP_95(0xFE, -300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AB96)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_1ABBE():
        OP_95(0xFE, 2300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1ABBE)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x10E, 0x1F4)

    def lambda_1ABE6():
        OP_95(0xFE, 1000, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1ABE6)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0852
    NpcTalk(
        0x101,
        "ロイドの声",
        "#1Pセシル姉！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(1000, 1000, 4100, 1500)
    SetChrPos(0x101, 300, 0, -1600, 0)
    BeginChrThread(0x101, 3, 0, 56)

    def lambda_1AC84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AC84)
    Sleep(250)

    def lambda_1AC98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AC98)
    Sleep(350)

    def lambda_1ACAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1ACAC)
    Sleep(450)

    def lambda_1ACC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1ACC0)
    OP_93(0xB, 0xB4, 0x1F4)

    #C0853
    ChrTalk(
        0xB,
        "#05921F#5Pロイド……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    #C0854
    ChrTalk(
        0x101,
        "#12P#00007Fそれで、キーアは！？\x02",
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x102,
        (
            "#00101Fアリオスさんに\x01",
            "連れて行かれたそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0xB,
        (
            "#05926F#5Pええ、あの白い制服を着た\x01",
            "アリオスさんが一人で来て……\x02\x03",

            "#05921F『迎えに来た』って声をかけたら\x01",
            "キーアちゃんも頷いて……\x02",
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
    Sleep(850)

    #C0857
    ChrTalk(
        0x101,
        "#12P#00011Fえ……\x02",
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x104,
        (
            "#00305Fそんじゃキー坊は\x01",
            "自分から付いてったんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0xB,
        (
            "#05923F#5Pええ……私にはそう見えたわ。\x02\x03",

            "#05921Fでも、あなたたちに\x01",
            "無断でというのも変だったから\x01",
            "止めようとしたんだけど……\x02\x03",

            "#05926F『大丈夫だから』って\x01",
            "キーアちゃんに言われて……\x02\x03",

            "それで警戒してたツァイト君も\x01",
            "大人しくなっちゃって……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x13B, 0x1F4)
    Sleep(300)

    #C0860
    ChrTalk(
        0x103,
        (
            "#12P#00208Fそういえば……\x01",
            "ツァイトがどこにもいません。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0xB,
        (
            "#05926F#5P２人が居なくなってから\x01",
            "フラリと出ていっちゃったの。\x02\x03",

            "#05928Fひょっとしたら２人を\x01",
            "追いかけたのかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_1B095():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B095)
    Sleep(100)

    def lambda_1B0A5():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B0A5)
    Sleep(100)

    def lambda_1B0B5():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B0B5)
    Sleep(100)

    def lambda_1B0C5():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B0C5)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(150)

    #C0862
    ChrTalk(
        0x101,
        "#5P#00008F……どういうことだ？\x02",
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x102,
        (
            "#00108Fシズクちゃんのことで\x01",
            "約束でもあったのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0xB,
        (
            "#05923F#5P私もそう思ったんだけど\x01",
            "どうもそうじゃないみたいで……\x02\x03",

            "#05921Fミシュラムに行くような事を\x01",
            "アリオスさんが言っていたし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1B21A():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B21A)
    Sleep(50)

    def lambda_1B22A():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B22A)
    Sleep(50)

    def lambda_1B23A():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B23A)
    Sleep(50)

    def lambda_1B24A():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B24A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0865
    ChrTalk(
        0x101,
        "#12P#00005Fミシュラム……？\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0xB,
        (
            "#05923F#5Pええ、ボートの用意は\x01",
            "出来ているって……\x02\x03",

            "#05921Fつまりミシュラムに\x01",
            "行くということよね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0867
    ChrTalk(
        0x102,
        (
            "#00103F……ここ数日、ミシュラム方面は\x01",
            "完全に営業停止しているはずだわ。\x02\x03",

            "#00101Fそんな所にわざわざ……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0868
    ChrTalk(
        0x104,
        (
            "#00310Fチッ……\x01",
            "やっぱ普通じゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x103,
        "#12P#00201F追いかけましょう、ロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0870
    ChrTalk(
        0x101,
        (
            "#11P#00003Fああ……\x01",
            "何とかボートを調達しよう。\x02\x03",

            "#00007Fセシル姉、ゴメン！\x01",
            "とにかく追いかけてみるよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B435():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B435)
    Sleep(50)

    def lambda_1B445():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B445)
    Sleep(50)

    def lambda_1B455():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B455)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0871
    ChrTalk(
        0xB,
        (
            "#05923F#5Pええ、気をつけて。\x02\x03",

            "#05928F……アリオスさんもキーアちゃんも\x01",
            "いつになく真剣な目をしていたわ。\x02\x03",

            "#05921F多分、よほどの事情があると思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x101,
        "#11P#00013F分かった……！\x02",
    )

    CloseMessageWindow()

    #C0873
    ChrTalk(
        0x102,
        (
            "#00107Fとにかく追いついて\x01",
            "その事情を聞かないと……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    SetScenarioFlags(0x22, 2)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_1AA9B end

    def Function_56_1B580(): pass

    label("Function_56_1B580")


    def lambda_1B585():
        OP_97(0x101, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B585)
    Sleep(200)

    def lambda_1B5A2():
        OP_97(0x102, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B5A2)
    Sleep(200)

    def lambda_1B5BF():
        OP_97(0x103, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B5BF)
    Sleep(200)

    def lambda_1B5DC():
        OP_97(0x104, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B5DC)
    Return()

    # Function_56_1B580 end

    def Function_57_1B5F2(): pass

    label("Function_57_1B5F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51218.itc", 0x1E)
    OP_24(0x101E)
    OP_24(0x101F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis287.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis288.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis289.itp")
    ClearMapFlags(0x10000000)
    OP_68(1000, 1000, 0, 0)
    MoveCamera(55, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x103, 300, 0, -2900, 0)
    SetChrPos(0x104, 1400, 0, -3200, 0)
    SetChrPos(0xF4, 300, 0, -4200, 0)
    SetChrPos(0xF5, 1400, 0, -4500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    StopBGM(0x1388)
    OP_68(1000, 1000, 2000, 3500)
    BeginChrThread(0x101, 3, 0, 58)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_1B7B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B7B0)
    Sleep(400)

    def lambda_1B7C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B7C4)
    Sleep(600)

    def lambda_1B7D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B7D8)
    Sleep(400)

    def lambda_1B7EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B7EC)
    Sleep(600)

    def lambda_1B800():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1B800)
    Sleep(400)

    def lambda_1B814():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1B814)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_1B82A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B82A)
    WaitChrThread(0x102, 1)

    def lambda_1B83B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B83B)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 1)

    def lambda_1B854():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1B854)
    WaitChrThread(0xF5, 1)

    def lambda_1B865():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1B865)
    OP_6F(0x79)
    OP_68(2640, 1300, 3150, 2000)
    MoveCamera(55, 15, 0, 2000)
    SetCameraDistance(29000, 2000)
    OP_6F(0x79)

    #C0874
    ChrTalk(
        0x101,
        "#6P#00001F#30W……特務支援課………\x02",
    )

    CloseMessageWindow()

    #C0875
    ChrTalk(
        0x102,
        "#6P#00108F#30W帰って来た……わね。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    VolumeBGM(0x46, 0x64)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(110, 50, -1, -1)

    #A0876
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4126V#27A#30Wあ、帰って来た！\x02\x03",

            "#4127V#4S#30A#30Wおかえり～！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 62)
    SetMessageWindowPos(170, 25, -1, -1)

    #A0877
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4S#20A行って来ます！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(180, 20, -1, -1)

    #A0878
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#40A#30W──よし。\x01",
            "それじゃあ鍋を始めよう。\x02\x03",

            "#70A#30Wキーアが準備してくれたから\x01",
            "肉、魚、野菜──タップリある。\x02\x03",

            "#50A#30Wたくさん食べて、早めに休んで……\x01",
            "明日に備えよう！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 62)
    SetMessageWindowPos(145, 110, -1, -1)

    #A0879
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4S#20Aいただきます！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    FadeToBright(1000, 16777215)
    VolumeBGM(0x64, 0x7D0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)

    #C0880
    ChrTalk(
        0x101,
        "#6P#00008F#30W……………………………\x02",
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x104,
        (
            "#5P#00304F#30W……ハハ。\x01",
            "何だか懐かしすぎるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x103,
        "#6P#00208Fはい……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BC77")

    #C0883
    ChrTalk(
        0x109,
        (
            "#12P#10106Fまだ１ヶ月くらいしか\x01",
            "経っていませんけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BCB5")

    #C0884
    ChrTalk(
        0x105,
        (
            "#12P#10404Fフフ……\x01",
            "さすがに感慨深いね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BD42")

    #C0885
    ChrTalk(
        0x106,
        (
            "#12P#10708Fでも、思ったよりも\x01",
            "荒らされていませんね……\x02\x03",

            "#10710Fてっきり国防軍の捜索が\x01",
            "入っているかと思いましたが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDB9")

    label("loc_1BD42")


    #C0886
    ChrTalk(
        0x102,
        (
            "#5P#00104Fでも、思ったよりも\x01",
            "荒らされてはいないわね……\x02\x03",

            "#00100Fてっきり国防軍の捜索が\x01",
            "入っているかと思ったけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BEE4")

    #C0887
    ChrTalk(
        0x10A,
        (
            "#12P#00606Fどうやらあの子#6Rキ ー ア#への\x01",
            "配慮があるらしいな。\x02\x03",

            "#00602F大統領サイドにとって\x01",
            "彼女は余りに重要な存在だ。\x02\x03",

            "大切にしていた場所を荒らして\x01",
            "機嫌を損ねたくないのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0888
    ChrTalk(
        0x101,
        "#6P#00000F……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x103,
        (
            "#6P#00204Fなんか露骨ですが……\x01",
            "変わってないのは嬉しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C005")

    label("loc_1BEE4")


    #C0890
    ChrTalk(
        0x101,
        (
            "#6P#00004Fひょっとして、キーアへの\x01",
            "配慮があるのかもしれない。\x02\x03",

            "#00000F大統領サイドにとって\x01",
            "あの子は余りに重要な存在だ。\x02\x03",

            "大切にしていた場所を荒らして\x01",
            "機嫌を損ねたくないのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0891
    ChrTalk(
        0x104,
        "#5P#00305F……なるほどねぇ。\x02",
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0x103,
        (
            "#6P#00204Fなんか露骨ですが……\x01",
            "変わってないのは嬉しいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C005")

    Sound(953, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    OP_90(0xC, 1500, 3000, 15000, 180)

    def lambda_1C033():
        OP_96(0xFE, 0x5DC, 0x0, 0x1838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C033)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1C0C2():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C0C2)
    Sleep(50)

    def lambda_1C0D2():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C0D2)
    Sleep(50)

    def lambda_1C0E2():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C0E2)
    Sleep(50)

    def lambda_1C0F2():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C0F2)
    Sleep(50)

    def lambda_1C102():
        TurnDirection(0xF4, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1C102)
    Sleep(50)

    def lambda_1C112():
        TurnDirection(0xF5, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1C112)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Fade(500)
    OP_68(1000, 1750, 9000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    OP_68(1000, 900, 5000, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    WaitChrThread(0xC, 1)
    OP_4B(0xC, 0xFF)
    OP_6F(0x79)

    #C0893
    ChrTalk(
        0x101,
        "#12P#00005Fコッペ……！\x02",
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x102,
        (
            "#00102Fそう……\x01",
            "無事でいてくれたのね。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 61)

    def lambda_1C1DE():
        OP_97(0x101, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C1DE)
    Sleep(100)

    def lambda_1C1FB():
        OP_97(0x102, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C1FB)
    Sleep(100)

    def lambda_1C218():
        OP_97(0x104, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C218)
    Sleep(100)

    def lambda_1C235():
        OP_97(0xF4, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1C235)
    Sleep(100)

    def lambda_1C252():
        OP_97(0xF5, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1C252)
    WaitChrThread(0x104, 0)

    def lambda_1C270():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C270)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x103, 3)

    #C0895
    ChrTalk(
        0xC,
        "#11Pにゃーご。\x02",
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0xC,
        "#11Pにゃう、にゃん。\x02",
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x103,
        (
            "#00204F……そう、お疲れさま。\x02\x03",

            "#00202Fええ、ええ……\x01",
            "少し留守にしていただけです。\x02\x03",

            "#00204Fまた……きっと戻ってきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x104,
        "#00300Fなんて言ってるんだ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0x103, 0x101, 500)

    #C0899
    ChrTalk(
        0x103,
        (
            "#00206F#5Pどうやら、あれからずっと\x01",
            "ここで暮らしていたみたいで……\x02\x03",

            "#00202Fわたしたち“同居人”のことも\x01",
            "一応、気に掛けてくれたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x101,
        "#12P#00012Fはは、そっか。\x02",
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0x102,
        (
            "#00109Fふふっ、ネコにしては\x01",
            "珍しいくらい律儀ね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4AD")

    #C0902
    ChrTalk(
        0x109,
        (
            "#12P#10102Fせっかくですから\x01",
            "キャットフードの用意を\x01",
            "しておきましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C52A")

    label("loc_1C4AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4F8")

    #C0903
    ChrTalk(
        0x105,
        (
            "#12P#10402Fせっかくだから\x01",
            "エサでも用意しようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C52A")

    label("loc_1C4F8")


    #C0904
    ChrTalk(
        0x104,
        (
            "#00304Fせっかくだから\x01",
            "エサでも用意しとくか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C52A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(122400, 700, 6000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0xC, 122700, 0, 6000, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 121800, 0, 6000, 0)
    OP_4C(0xC, 0xFF)
    SetCameraDistance(21000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 10790, 850, 12360, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A5, 4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    EventEnd(0x5)
    Return()

    # Function_57_1B5F2 end

    def Function_58_1C605(): pass

    label("Function_58_1C605")


    def lambda_1C60A():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C60A)
    Sleep(200)

    def lambda_1C627():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C627)
    Sleep(200)
    BeginChrThread(0x103, 0, 0, 59)
    Sleep(200)
    BeginChrThread(0x104, 0, 0, 60)
    Sleep(200)

    def lambda_1C656():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1C656)
    Sleep(200)

    def lambda_1C673():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1C673)
    Return()

    # Function_58_1C605 end

    def Function_59_1C689(): pass

    label("Function_59_1C689")


    def lambda_1C68E():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C68E)
    WaitChrThread(0x103, 1)

    def lambda_1C6AC():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C6AC)
    WaitChrThread(0x103, 1)
    Return()

    # Function_59_1C689 end

    def Function_60_1C6C6(): pass

    label("Function_60_1C6C6")


    def lambda_1C6CB():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C6CB)
    WaitChrThread(0x104, 1)

    def lambda_1C6E9():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C6E9)
    WaitChrThread(0x104, 1)
    Return()

    # Function_60_1C6C6 end

    def Function_61_1C703(): pass

    label("Function_61_1C703")

    Sleep(200)

    def lambda_1C70B():
        OP_95(0xFE, -400, 0, 4100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C70B)
    WaitChrThread(0x103, 1)

    def lambda_1C729():
        OP_95(0xFE, 300, 0, 6100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C729)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0xC, 500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0xC, 0x103, 500)
    Return()

    # Function_61_1C703 end

    def Function_62_1C765(): pass

    label("Function_62_1C765")

    OP_CB(0x0, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CC(0x0, 0xFF, 0x0)
    Return()

    # Function_62_1C765 end

    def Function_63_1C893(): pass

    label("Function_63_1C893")

    EventBegin(0x0)
    Fade(500)
    OP_68(64879, 1330, 10230, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24880, 0)
    SetChrPos(0x101, 65030, 30, 11420, 225)
    SetChrPos(0x102, 66810, 30, 10890, 270)
    SetChrPos(0x103, 66810, 30, 9740, 270)
    SetChrPos(0x104, 63390, 0, 8370, 0)
    SetChrPos(0x109, 65019, 0, 8370, 0)
    SetChrPos(0x105, 66270, 0, 8280, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0905
    ChrTalk(
        0x101,
        (
            "#00000Fセルゲイ課長の昔の渾名は\x01",
            "『搦#2Rから#め手のセルゲイ』だった\x01",
            "らしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0x102,
        (
            "#11P#00100Fとすると、課長の椅子が\x01",
            "『搦め手の指揮官が座する椅子』に\x01",
            "あてはまりそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0907
    ChrTalk(
        0x101,
        "#00001Fあたりを調べてみるか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0908
    ChrTalk(
        0x101,
        (
            "#00005F……課長の机の下に\x01",
            "何か入っているみたいだ。\x02\x03",

            "#00000Fちょっと引っ張りだしてみよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(63630, 1330, 6190, 0)
    MoveCamera(43, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24880, 0)
    ClearMapObjFlags(0x14, 0x4)
    SetChrPos(0x101, 64060, 30, 5280, 0)
    SetChrPos(0x102, 62990, 30, 5080, 0)
    SetChrPos(0x103, 65190, 30, 5080, 0)
    SetChrPos(0x104, 64060, 30, 4000, 0)
    SetChrPos(0x109, 62990, 30, 4000, 0)
    SetChrPos(0x105, 65190, 30, 4000, 0)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0x2C, 0x1E)
    SetChrSubChip(0x2C, 0xC)
    SetChrPos(0x2C, 64040, 150, 7160, 0)
    OP_52(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x2)
    SetChrFlags(0x2C, 0x10)
    SetChrFlags(0x2C, 0x20)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0909
    ChrTalk(
        0x104,
        (
            "#12P#00305Fこいつは……\x01",
            "もしかしてトランクか？\x02",
        )
    )

    CloseMessageWindow()

    #C0910
    ChrTalk(
        0x105,
        (
            "#12P#10300F例の《競売会》のときに\x01",
            "キーアが入れられていた物にも\x01",
            "似ているみたいだね。\x02\x03",

            "#10304Fフフ、最初の場所に\x01",
            "ここを選ぶなんて\x01",
            "挑発もいいとこだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0911
    ChrTalk(
        0x101,
        (
            "#12P#00006Fた、確かにな。\x01",
            "課長の渾名まで掴んでたみたいだし……\x02\x03",

            "#00000Fとにかく、確認してみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sound(1024, 0, 100, 0)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x14)
    Sleep(1000)
    SetChrName("")

    #A0912
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "トランクの裏側には\x01",
            "カードが貼り付けてあった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0913
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第二の檻は市外に。\x01",
            "『古の道にて里人が\x01",
            "　受け継ぎし場所』を探せ。\x07\x00\x02",
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

    #C0914
    ChrTalk(
        0x103,
        (
            "#00200Fローゼンベルク製の\x01",
            "アンティークドール……\x01",
            "間違いなさそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0915
    ChrTalk(
        0x102,
        (
            "#12P#00100Fええ、私も見た事があるわ。\x02\x03",

            "#00104Fベルが『カナン』って名前で呼んで\x01",
            "可愛がっていた人形だったと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x109,
        (
            "#12P#10100Fふふ、人形に名前をつけるなんて\x01",
            "マリアベルさんも可愛い所がありますね。\x02\x03",

            "#10106F盗んだものをわざわざ\x01",
            "こんなトランクに入れてるなんて\x01",
            "ちょっと意外ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0917
    ChrTalk(
        0x101,
        (
            "#12P#00003F怪盗Ｂ……\x01",
            "美術品に対する礼儀は\x01",
            "ちゃんとしてるのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそれと２枚目のカード……\x01",
            "場所は『市外』か。\x02\x03",

            "#10306Fやれやれ、\x01",
            "探索範囲が広がっちゃったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x102,
        (
            "#12P#00100Fそれと重要そうなのは、\x01",
            "『古の道』と『里人が受け継ぎし』ね。\x02\x03",

            "#00103Fどちらも歴史を感じさせる言葉だけど、\x01",
            "近代都市であるクロスベルで\x01",
            "そんな場所といえば……\x02",
        )
    )

    CloseMessageWindow()

    #C0920
    ChrTalk(
        0x104,
        (
            "#12P#00300Fとにかく、コイツを回収して\x01",
            "次を探しに行ってみるとすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0921
    ChrTalk(
        0x101,
        "#12P#00000Fああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0922
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16Iローゼンベルク人形・Ｃ\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x335, 1)
    SetMapObjFlags(0x14, 0x4)
    SetChrFlags(0x2C, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, 64050, 30, 5290, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x2)
    SetScenarioFlags(0x157, 1)
    OP_65(0x4, 0x1)
    EventEnd(0x5)
    Return()

    # Function_63_1C893 end

    def Function_64_1D22A(): pass

    label("Function_64_1D22A")

    EventBegin(0x1)

    #C0923
    ChrTalk(
        0x101,
        (
            "#00000Fまずは支援要請を確認しよう。\x01",
            "行動するのはそれからだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Return()

    # Function_64_1D22A end

    def Function_65_1D285(): pass

    label("Function_65_1D285")

    EventBegin(0x1)

    #C0924
    ChrTalk(
        0x101,
        (
            "#00000Fまずは支援要請を確認しよう。\x01",
            "行動するのはそれからだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    EventEnd(0x4)
    Return()

    # Function_65_1D285 end

    def Function_66_1D2E0(): pass

    label("Function_66_1D2E0")

    EventBegin(0x1)

    #C0925
    ChrTalk(
        0x101,
        (
            "#00000Fまずは支援要請を確認しよう。\x01",
            "行動するのはそれからだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    EventEnd(0x4)
    Return()

    # Function_66_1D2E0 end

    def Function_67_1D33B(): pass

    label("Function_67_1D33B")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D367")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D384")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3A1")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3BE")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3DB")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3F8")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D415")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D415")

    Return()

    # Function_67_1D33B end

    SaveToFile()

Try(main)
