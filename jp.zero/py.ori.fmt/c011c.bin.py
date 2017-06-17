from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c011c.bin",                # FileName
        "c011c",                    # MapName
        "c011c",                    # Location
        0x0009,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c011c",                  # 0
        "セルゲイ課長",           # 1
        "セルゲイ課長",           # 2
        "ツァイト",               # 3
        "コッペ",                 # 4
        "ビリー",                 # 5
        "コリン",                 # 6
        "ハロルド",               # 7
        "ソフィア",               # 8
        "エステル",               # 9
        "ヨシュア",               # 10
        "ツァイト",               # 11
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
        "イス",                   # 22
        "金の薔薇のカード",       # 23
        "ノーパソ",               # 24
        "SE制御",                 # 25
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch39200.itc",                   # 02
        "chr/ch02707.itc",                   # 03
        "apl/ch50092.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
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

    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(64000,   200,     11399,   180,  469,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(123940,  0,       5840,    225,  404,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(123139,  0,       7639,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 42,  7.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -3.5,                  -2.0999999046325684,   -0.0,                  1.0])

    DeclActor(18240,   850,     7560,    1000,    18240,   1850,    7560,    0x007C, 0,  3,  0x0000)
    DeclActor(64000,   30,      9800,    1500,    64000,   1500,    11400,   0x007E, 0,  4,  0x0000)
    DeclActor(-12920,  0,       7560,    2000,    -12920,  0,       7560,    0x007C, 0,  46, 0x0000)
    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  8,  0x0000)
    DeclActor(180910,  0,       62020,   1500,    180910,  1500,    62020,   0x007C, 0,  45, 0x0000)
    DeclActor(19980,   0,       63920,   1500,    19980,   1500,    63920,   0x007C, 0,  45, 0x0000)
    DeclActor(175940,  0,       63930,   1500,    175940,  1500,    63930,   0x007C, 0,  45, 0x0000)
    DeclActor(-3150,   0,       122280,  1200,    -3150,   1000,    122280,  0x007C, 0,  56, 0x0000)
    DeclActor(-2300,   0,       129960,  1200,    -2300,   2000,    129960,  0x007C, 0,  57, 0x0000)
    DeclActor(155150,  30,      129699,  1200,    153340,  2029,    130490,  0x007C, 0,  58, 0x0000)
    DeclActor(155120,  30,      123880,  1200,    155120,  2029,    123880,  0x007C, 0,  59, 0x0000)
    DeclActor(207280,  30,      128039,  1200,    208840,  3000,    130410,  0x007C, 0,  60, 0x0000)
    DeclActor(209020,  0,       126830,  1200,    209210,  2000,    127040,  0x007C, 0,  61, 0x0000)
    DeclActor(51920,   0,       130570,  1200,    51920,   2500,    130570,  0x007C, 0,  62, 0x0000)
    DeclActor(52900,   0,       124470,  1200,    53700,   2000,    125270,  0x007C, 0,  63, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  65, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  66, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  67, 0x0000)
    DeclActor(48000,   30,      127860,  1200,    47560,   1500,    128630,  0x007C, 0,  68, 0x0000)

    ScpFunction((
        "Function_0_7E8",          # 00, 0
        "Function_1_8A0",          # 01, 1
        "Function_2_CA0",          # 02, 2
        "Function_3_EFF",          # 03, 3
        "Function_4_FAA",          # 04, 4
        "Function_5_FAE",          # 05, 5
        "Function_6_120F",         # 06, 6
        "Function_7_1236",         # 07, 7
        "Function_8_12D4",         # 08, 8
        "Function_9_18CD",         # 09, 9
        "Function_10_2816",        # 0A, 10
        "Function_11_2835",        # 0B, 11
        "Function_12_4435",        # 0C, 12
        "Function_13_4DD8",        # 0D, 13
        "Function_14_5B78",        # 0E, 14
        "Function_15_5C05",        # 0F, 15
        "Function_16_6676",        # 10, 16
        "Function_17_6691",        # 11, 17
        "Function_18_69E2",        # 12, 18
        "Function_19_843D",        # 13, 19
        "Function_20_8458",        # 14, 20
        "Function_21_8481",        # 15, 21
        "Function_22_B749",        # 16, 22
        "Function_23_B79E",        # 17, 23
        "Function_24_B7F0",        # 18, 24
        "Function_25_E3F7",        # 19, 25
        "Function_26_E411",        # 1A, 26
        "Function_27_E42C",        # 1B, 27
        "Function_28_E481",        # 1C, 28
        "Function_29_E4D6",        # 1D, 29
        "Function_30_E52B",        # 1E, 30
        "Function_31_E580",        # 1F, 31
        "Function_32_E5FC",        # 20, 32
        "Function_33_F67B",        # 21, 33
        "Function_34_F696",        # 22, 34
        "Function_35_F6B1",        # 23, 35
        "Function_36_F6E6",        # 24, 36
        "Function_37_FACC",        # 25, 37
        "Function_38_FAF7",        # 26, 38
        "Function_39_FB10",        # 27, 39
        "Function_40_10274",       # 28, 40
        "Function_41_109D3",       # 29, 41
        "Function_42_10C74",       # 2A, 42
        "Function_43_10D08",       # 2B, 43
        "Function_44_10D6C",       # 2C, 44
        "Function_45_10EAD",       # 2D, 45
        "Function_46_10ED9",       # 2E, 46
        "Function_47_10EDA",       # 2F, 47
        "Function_48_110A7",       # 30, 48
        "Function_49_11274",       # 31, 49
        "Function_50_11443",       # 32, 50
        "Function_51_1161D",       # 33, 51
        "Function_52_117EE",       # 34, 52
        "Function_53_119BF",       # 35, 53
        "Function_54_11B8C",       # 36, 54
        "Function_55_11D64",       # 37, 55
        "Function_56_11DBB",       # 38, 56
        "Function_57_11E66",       # 39, 57
        "Function_58_11FA5",       # 3A, 58
        "Function_59_12048",       # 3B, 59
        "Function_60_120F3",       # 3C, 60
        "Function_61_1219A",       # 3D, 61
        "Function_62_12243",       # 3E, 62
        "Function_63_122F2",       # 3F, 63
        "Function_64_1239F",       # 40, 64
        "Function_65_123D8",       # 41, 65
        "Function_66_1247D",       # 42, 66
        "Function_67_12522",       # 43, 67
        "Function_68_125C7",       # 44, 68
    ))


    def Function_0_7E8(): pass

    label("Function_0_7E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_828"),
        (1, "loc_834"),
        (2, "loc_840"),
        (3, "loc_84C"),
        (4, "loc_858"),
        (5, "loc_864"),
        (6, "loc_870"),
        (SWITCH_DEFAULT, "loc_87C"),
    )


    label("loc_828")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_834")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_840")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_84C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_858")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_864")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_870")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_87C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_888")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_89F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_89F")

    Return()

    # Function_0_7E8 end

    def Function_1_8A0(): pass

    label("Function_1_8A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96B")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96B")
    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93E")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_95D")

    label("loc_93E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95D")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_95D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96B")

    label("loc_96B")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A5")
    Event(0, 47)

    label("loc_9A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D6")
    Event(0, 48)

    label("loc_9D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A07")
    Event(0, 49)

    label("loc_A07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38")
    Event(0, 50)

    label("loc_A38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A69")
    Event(0, 51)

    label("loc_A69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9A")
    Event(0, 52)

    label("loc_A9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACB")
    Event(0, 53)

    label("loc_ACB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFC")
    Event(0, 54)

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B0A")
    Jump("loc_B7D")

    label("loc_B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B45")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x40)
    SetChrPos(0x13, 122440, 0, 7540, 45)
    SetChrChipByIndex(0x13, 0x4)
    SetChrSubChip(0x13, 0x0)
    Jump("loc_B7D")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B53")
    Jump("loc_B7D")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_B61")
    Jump("loc_B7D")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B6F")
    Jump("loc_B7D")

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B7D")
    ClearChrFlags(0x9, 0x80)

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA6")
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_BB7")

    label("loc_BA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB7")
    Event(0, 40)

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_BCE")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x0, 3)
    Event(0, 9)
    Jump("loc_C9F")

    label("loc_BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_BE2")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_C9F")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_C3D")
    ClearScenarioFlags(0x5C, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C0F")
    Event(0, 12)
    Jump("loc_C38")

    label("loc_C0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C26")
    Event(0, 13)
    Jump("loc_C38")

    label("loc_C26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C38")
    Event(0, 15)

    label("loc_C38")

    Jump("loc_C9F")

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_C51")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 18)
    Jump("loc_C9F")

    label("loc_C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_C65")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 21)
    Jump("loc_C9F")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_C79")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 24)
    Jump("loc_C9F")

    label("loc_C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_C8D")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 32)
    Jump("loc_C9F")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_C9F")
    ClearScenarioFlags(0x5C, 7)
    SetScenarioFlags(0x0, 2)
    Event(0, 36)

    label("loc_C9F")

    Return()

    # Function_1_8A0 end

    def Function_2_CA0(): pass

    label("Function_2_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CB7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CC5")
    Jump("loc_CF8")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF8")

    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D2F")
    Jump("loc_D5C")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D3D")
    Jump("loc_D5C")

    label("loc_D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D4F")
    OP_66(0x0, 0x1)
    Jump("loc_D5C")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D5C")
    OP_66(0x1, 0x1)

    label("loc_D5C")

    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9C")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    OP_65(0x7, 0x1)

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB4")
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_65(0x8, 0x1)

    label("loc_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC")
    SetMapObjFrame(0xFF, "05", 0x0, 0x1)
    OP_65(0x9, 0x1)

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEF")
    SetMapObjFrame(0xFF, "06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x0, 0x1)
    OP_65(0xA, 0x1)

    label("loc_DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E07")
    SetMapObjFrame(0xFF, "07", 0x0, 0x1)
    OP_65(0xB, 0x1)

    label("loc_E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F")
    SetMapObjFrame(0xFF, "08", 0x0, 0x1)
    OP_65(0xC, 0x1)

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E37")
    SetMapObjFrame(0xFF, "03", 0x0, 0x1)
    OP_65(0xD, 0x1)

    label("loc_E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5A")
    SetMapObjFrame(0xFF, "04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x0, 0x1)
    OP_65(0xE, 0x1)

    label("loc_E5A")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E95")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_EB0")

    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC8")
    OP_1B(0x8, 0x0, 0x2C)

    label("loc_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EE0")
    SetMapObjFlags(0x7, 0x10)
    OP_65(0x4, 0x1)
    Jump("loc_EEA")

    label("loc_EE0")

    ClearMapObjFlags(0x7, 0x10)
    OP_66(0x4, 0x1)

    label("loc_EEA")

    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    Return()

    # Function_2_CA0 end

    def Function_3_EFF(): pass

    label("Function_3_EFF")

    TalkBegin(0xFF)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伝言板にメッセージがある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『本部の会議に出席してくる。\x01",
            "  適当に戻るから仕事しておけ。\x01",
            "                    セルゲイ』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_EFF end

    def Function_4_FAA(): pass

    label("Function_4_FAA")

    Call(0, 5)
    Return()

    # Function_4_FAA end

    def Function_5_FAE(): pass

    label("Function_5_FAE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1042")
    Jump("loc_108C")

    label("loc_1042")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1062")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_108C")

    label("loc_1062")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1082")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_108C")

    label("loc_1082")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_108C")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1196")

    #C0003
    ChrTalk(
        0x9,
        (
            "#1000F記念祭中は\x01",
            "支援要請も引っ切り無しに\x01",
            "入ってくるだろう。\x02\x03",

            "最終日までの４日間は\x01",
            "支援要請だけに専念しろ。\x02\x03",

            "#1003F俺も本部の応援に\x01",
            "出かけたりするだろうが……\x01",
            "ま、気にせず仕事してろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#0000F了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1207")

    label("loc_1196")


    #C0005
    ChrTalk(
        0x9,
        (
            "#1000F記念祭中は\x01",
            "支援要請も引っ切り無しに\x01",
            "入ってくるだろう。\x02\x03",

            "俺のことは気にせず\x01",
            "支援要請だけに専念してろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1207")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_5_FAE end

    def Function_6_120F(): pass

    label("Function_6_120F")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xA,
        "#1200F…………………………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_120F end

    def Function_7_1236(): pass

    label("Function_7_1236")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B8")

    #C0007
    ChrTalk(
        0xB,
        "にやぁ～～お……㈱\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#0005Fあれ……？\x01",
            "エサ、出しっぱなしに\x01",
            "してったけな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_12D0")

    label("loc_12B8")


    #C0009
    ChrTalk(
        0xB,
        "にやぁ～～お……㈱\x02",
    )

    CloseMessageWindow()

    label("loc_12D0")

    TalkEnd(0xFE)
    Return()

    # Function_7_1236 end

    def Function_8_12D4(): pass

    label("Function_8_12D4")

    TalkBegin(0xFF)
    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18A3")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_131D"),
        (1, "loc_14C9"),
        (SWITCH_DEFAULT, "loc_189E"),
    )


    label("loc_131D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1344")
    OP_2B(0x34, 0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_14C4")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1365")
    OP_2B(0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_14C4")

    label("loc_1365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1380")
    OP_2B(0x2D, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_14C4")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1397")
    OP_2B(0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_14C4")

    label("loc_1397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_13B0")
    OP_2B(0x28, 0x29, 0x2A, 0x2F, 0xFFFF)
    Jump("loc_14C4")

    label("loc_13B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_13C3")
    OP_2B(0x25, 0xFFFF)
    Jump("loc_14C4")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_13E2")
    OP_2B(0x22, 0x23, 0x18, 0x1A, 0x1C, 0x1E, 0x21, 0xFFFF)
    Jump("loc_14C4")

    label("loc_13E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1401")
    OP_2B(0x1F, 0x20, 0x21, 0x18, 0x1A, 0x1C, 0x1E, 0xFFFF)
    Jump("loc_14C4")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_141E")
    OP_2B(0x1B, 0x1C, 0x1D, 0x1E, 0x18, 0x1A, 0xFFFF)
    Jump("loc_14C4")

    label("loc_141E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1439")
    OP_2B(0x16, 0x17, 0x18, 0x19, 0x1A, 0xFFFF)
    Jump("loc_14C4")

    label("loc_1439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1456")
    OP_2B(0x11, 0x12, 0x13, 0x14, 0xE, 0x10, 0xFFFF)
    Jump("loc_14C4")

    label("loc_1456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_146F")
    OP_2B(0xD, 0xE, 0xF, 0x10, 0xFFFF)
    Jump("loc_14C4")

    label("loc_146F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_148C")
    OP_2B(0x9, 0xA, 0xB, 0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_14C4")

    label("loc_148C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_14A3")
    OP_2B(0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_14C4")

    label("loc_14A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_14BF")
    OP_2B(0x1, 0x35, 0x2, 0x3, 0xFFFF)
    Jump("loc_14C4")

    label("loc_14BF")

    OP_2B(0x1, 0xFFFF)

    label("loc_14C4")

    Jump("loc_189E")

    label("loc_14C9")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("受付嬢フラン")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1527")
    Sound(2062, 255, 100, 0)    #voice#Fran

    #A0010
    AnonymousTalk(
        0xFF,
        "#28Aはい、こちらクロスベル警察です～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1553")

    label("loc_1527")

    Sound(2061, 255, 100, 0)    #voice#Fran

    #A0011
    AnonymousTalk(
        0xFF,
        "#26A皆さん、どうもお疲れさまですー。\x02",
    )

    CloseMessageWindow()

    label("loc_1553")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_179C")
    Sound(2067, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0012
    AnonymousTalk(
        0xFF,
        "#27Aそれでは報告を承りますね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1727")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_15C4"),
        (13, "loc_160E"),
        (12, "loc_1656"),
        (SWITCH_DEFAULT, "loc_16A0"),
    )


    label("loc_15C4")

    Sound(2075, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "#36Aクラス１ｓｔ――\x01",
            "ロイドさん、スゴすぎです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A0")

    label("loc_160E")

    Sound(2074, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "#35Aクラス２ｎｄ──\x01",
            "ロイドさん、すごいです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A0")

    label("loc_1656")

    Sound(2073, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            "#32Aクラス３ｒｄ──\x01",
            "ロイドさん、やりましたね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A0")

    label("loc_16A0")

    Sound(2076, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            "#31A特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)    #voice#Fran

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "#34Aお疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1794")

    label("loc_1727")

    Sound(2078, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0018
    AnonymousTalk(
        0xFF,
        "#16A報告は以上ですね～。\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)    #voice#Fran

    #A0019
    AnonymousTalk(
        0xFF,
        (
            "#37Aでは、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1794")

    SetScenarioFlags(0x0, 4)
    Jump("loc_1890")

    label("loc_179C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1821")
    Sound(2063, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            "#32Aあれっ……\x01",
            "先ほど報告されたばかりですよ？\x02",
        )
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)    #voice#Fran

    #A0021
    AnonymousTalk(
        0xFF,
        "#32Aまた依頼を達成されたらお願いしますね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1890")

    label("loc_1821")

    Sound(2065, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            "#37Aあれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)    #voice#Fran

    #A0023
    AnonymousTalk(
        0xFF,
        "#16Aまたよろしくお願いしますー。\x02",
    )

    CloseMessageWindow()

    label("loc_1890")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_189E")

    label("loc_189E")

    Jump("loc_12F0")

    label("loc_18A3")

    OP_E3(0x6)
    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18CC")
    Call(0, 41)

    label("loc_18CC")

    Return()

    # Function_8_12D4 end

    def Function_9_18CD(): pass

    label("Function_9_18CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50092.itc", 0x23)
    LoadChrToIndex("chr/ch02702.itc", 0x24)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
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
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 16000, 850, 6400, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    BeginChrThread(0x12, 0, 0, 10)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x5)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1400, 6600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0xC)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13400, 1300, 6600, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x5)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1400, 6600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0xC)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12000, 1300, 6600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x5)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1400, 4600, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0xC)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13400, 1300, 4600, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x5)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12400, 1400, 4600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 12000, 1300, 4600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x7)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12700, 1400, 5500, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 16000, 750, 5500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_52(0x1C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K創立記念祭　３日目\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7110", 0)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0025
    ChrTalk(
        0x104,
        (
            "#6P#0306Fは～、やれやれ。\x01",
            "昨日はマジで疲れたぜ。\x02\x03",

            "#0302Fこんなのがあと３日あるかと思うと\x01",
            "ちょっとウンザリしてくるな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0026
    ChrTalk(
        0x103,
        (
            "#5P#0200F昨日の件は自業自得では……？\x02\x03",

            "#0204Fああいうレースを提案したのは\x01",
            "ランディさん自身ですし……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0027
    ChrTalk(
        0x104,
        (
            "#6P#0301F今になって後悔してるっつーの。\x02\x03",

            "#0306F俺もトシだし、若いのに混じって\x01",
            "ヤンチャするもんじゃねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0102Fまだ二十歳かそこらで\x01",
            "何を言ってるんだか……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#11P#0008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0030
    ChrTalk(
        0x102,
        "#0105Fロイド？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        "#6P#0205F……どうしたんですか？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0032
    ChrTalk(
        0x101,
        (
            "#5P#0005Fん、ああ……\x02\x03",

            "#0012F昨日、エステルたちが\x01",
            "言ってた事が気になってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#0101Fあ……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#6P#0301F《黒の競売会#10Rシュバルツオークション#》だったか。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#6P#0200Fでも、ただの噂の可能性も\x01",
            "高そうなんですよね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ、そうなんだけどさ。\x02\x03",

            "#0001Fクロスベルの状況を考えると\x01",
            "あながち噂だけの話じゃ\x01",
            "無さそうな気がするんだよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0037
    ChrTalk(
        0x104,
        (
            "#6P#0306F確かに、マフィアが大手を振って\x01",
            "歩いているような場所だしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0203F何があっても不思議ではない……\x01",
            "その通りかもしません。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0108F……………………………………\x02\x03",

            "#0103F……実は、前にちょっと\x01",
            "気になる噂を聞いたことがあるわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0040
    ChrTalk(
        0x101,
        "#5P#0005F気になる噂……？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        "#3P#0205Fそれはどういう……？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#0103F私が以前、各国に留学していたのは\x01",
            "話したと思うけど……\x02\x03",

            "その時、知り合った貴族の\x01",
            "お嬢さんから聞いたことがあるの。\x02\x03",

            "#0101F毎年、クロスベルのある場所で\x01",
            "秘密の社交会#6Rパーティー#が開かれているって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x101,
        "#5P#0011F秘密の社交会……？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#6P#0302Fいかがわしい響きだな、オイ。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#0106Fどうやら、各国の貴族や実業家が\x01",
            "秘密裏に集まるパーティーらしくて……\x02\x03",

            "#0108Fその時は、ただの噂としか\x01",
            "思っていなかったけど……\x02\x03",

            "#0101Fちょっと気になると思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#5P#0003F確かに……\x02\x03",

            "#0001Fそれが《黒の競売会》って\x01",
            "可能性はあるということか……\x02\x03",

            "#0008Fうーん、そうなると課長あたりは\x01",
            "何か知ってそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0047
    ChrTalk(
        0x103,
        (
            "#6P#0200F課長は今日は、\x01",
            "本部の方に行ってますね。\x02\x03",

            "何でも外せない会議があるとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#5P#0006Fそうだったな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    #C0049
    ChrTalk(
        0x104,
        (
            "#6P#0303Fしかし、もし本当だったとしても\x01",
            "俺たちにはどうしようもなくねぇか？\x02\x03",

            "#0301Fどう考えても議員どもの指示で\x01",
            "警察本部に黙認されてそうだしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#5P#0008F……そうなんだよな。\x02\x03",

            "#0006Fうーん、でもなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#0103F……気持ちは判るわ。\x02\x03",

            "#0100F一応、記念祭の間は\x01",
            "気にかけておきましょう。\x02\x03",

            "何か情報があるかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#5P#0003F──そうだな。\x02\x03",

            "#0000Fよし、とっとと食べて、\x01",
            "今日も支援要請を片付けるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#6P#0202F…………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x7D0)
    WaitBGM()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
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
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetScenarioFlags(0xA0, 2)
    OP_29(0x44, 0x1, 0x2)
    OP_29(0x44, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27BC")
    OP_29(0x17, 0x4, 0x40)
    Jump("loc_27CE")

    label("loc_27BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CE")
    OP_29(0x17, 0x4, 0x40)

    label("loc_27CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27EC")
    OP_29(0x19, 0x4, 0x40)
    Jump("loc_27FE")

    label("loc_27EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FE")
    OP_29(0x19, 0x4, 0x40)

    label("loc_27FE")

    ModifyEventFlags(1, 0, 0x80)
    ClearScenarioFlags(0x0, 3)
    PlayBGM("ed7106", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_9_18CD end

    def Function_10_2816(): pass

    label("Function_10_2816")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2834")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_10_2816")

    label("loc_2834")

    Return()

    # Function_10_2816 end

    def Function_11_2835(): pass

    label("Function_11_2835")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50092.itc", 0x23)
    LoadChrToIndex("chr/ch02702.itc", 0x24)
    LoadChrToIndex("chr/ch23600.itc", 0x25)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrChipByIndex(0xC, 0x25)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x8)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 12700, 1400, 6600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x18)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13300, 1300, 6700, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x18)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12100, 1300, 6700, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x8)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12700, 1400, 4600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x18)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13300, 1300, 4700, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x18)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 12100, 1300, 4700, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x7)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12700, 1400, 5500, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis062.itp")
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K創立記念祭　最終日\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7110", 0)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0055
    ChrTalk(
        0x104,
        (
            "#6P#0309Fいや～！\x01",
            "しかし昨日の話は凄かったな。\x02\x03",

            "#0300Fあの２人、どんだけ修羅場を\x01",
            "潜り抜けてんだよって話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#0103Fリベールの異変については\x01",
            "色々と話は聞いていたけど……\x02\x03",

            "#0100F真相はそれ以上に\x01",
            "驚くべきものだったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#6P#0206Fそれに《結社》ですか……\x02\x03",

            "#0201F最先端技術で、エプスタイン財団や\x01",
            "ＺＣＦを超える勢力があるというのは\x01",
            "噂程度には耳にしていましたけど……\x02\x03",

            "まさかそのような規模で\x01",
            "本当に実在していたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#5P#0006Fああ……\x01",
            "正直、実感は湧いてこないよな。\x02\x03",

            "#0000Fまあヨシュア曰く、\x01",
            "クロスベルに《結社》の手は\x01",
            "殆んど及んでいないって話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#0108Fもしかしたら、帝国と共和国の目が\x01",
            "他より厳しいからかもしれないわね。\x02\x03",

            "両国の諜報関係者も\x01",
            "多く入り込んでいるでしょうから\x01",
            "尻尾を掴まれたくないのかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#5P#0006F……それはそれで\x01",
            "全然嬉しくない話だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#6P#0303F謎の結社か、大国の諜報組織か、\x01",
            "はたまた巨大な犯罪シンジケートか。\x02\x03",

            "#0301Fま、どれも厄介なのは変わらねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#6P#0206F……ですね。\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    SetChrPos(0xC, 800, 0, -1500, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    #N0063
    NpcTalk(
        0xC,
        "声",
        (
            "#5Pちわーす！\x01",
            "ライムス運送会社です！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(800, 1000, 1500, 2000)
    OP_6F(0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sound(103, 0, 100, 0)

    def lambda_2F56():
        OP_96(0xFE, 0x320, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2F56)

    def lambda_2F70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2F70)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xC, 1)

    #C0064
    ChrTalk(
        0x101,
        "#3P#0005Fあなたは……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        "#0105F昨日の運送会社の……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(800, 1100, 5500, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_90(0x101, 300, 850, 7500, 180)
    OP_90(0x102, 1300, 850, 7500, 180)
    OP_90(0x103, 300, 850, 8700, 180)
    OP_90(0x104, 1300, 850, 8700, 180)
    OP_68(800, 1100, 2500, 2000)

    def lambda_3083():
        OP_96(0xFE, 0x12C, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3083)
    Sleep(50)

    def lambda_30A0():
        OP_96(0xFE, 0x514, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30A0)
    Sleep(50)

    def lambda_30BD():
        OP_96(0xFE, 0x12C, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30BD)
    Sleep(50)

    def lambda_30DA():
        OP_96(0xFE, 0x514, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30DA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0066
    ChrTalk(
        0xC,
        "#2Pいや～、昨日はお疲れさま！\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#2Pでも良かったよ！\x01",
            "あの子が無事見つかって！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        "#2P親御さん、心配してただろう？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#5P#0012Fはは、それはもう。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#5P#0300Fアンタの方は\x01",
            "会社にどやされなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#2Pああ、配達が遅れたことは\x01",
            "警備隊の人に文句言われたけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#2P親父──社長の方からは\x01",
            "そこまでお咎めはされなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "#2Pま、ちゃんと車内をチェックしろって\x01",
            "一発ゲンコはもらっちまったけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#5P#0102Fふふ……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#5P#0204Fまあ、その程度で済んで\x01",
            "幸いだったかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        "#2Pはは、違いない。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "#2P──おっと、昨日の確認を\x01",
            "しに来たんじゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        "#2Pあんた達にお届け物だよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x101,
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#5P#0105F警察本部からですか？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#2Pいや、何でも朝一番で\x01",
            "速達で入ったらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        "#2Pはいこれ、受け取って。\x02",
    )

    CloseMessageWindow()

    def lambda_3457():
        OP_96(0xFE, 0x12C, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3457)
    WaitChrThread(0xC, 1)

    def lambda_3475():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3475)

    def lambda_3482():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3482)
    Sleep(300)
    SetChrName("")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "小さな小包を受け取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_34B9():
        OP_96(0xFE, 0x320, 0x0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_34B9)

    #C0084
    ChrTalk(
        0x101,
        "#5P#0005Fこれは……？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#11P#0100Fずいぶん小さなものだけど……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 1)

    #C0086
    ChrTalk(
        0xC,
        "#2Pそれじゃあ、確かに渡したぜ。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xC,
        (
            "#2P配達があるんで\x01",
            "俺はこれで失礼するよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3571():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3571)
    Sleep(50)
    OP_93(0x102, 0xB4, 0x1F4)

    #C0088
    ChrTalk(
        0x104,
        "#5P#0300Fおお、お疲れさん。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#5P#0202Fまた迷子に忍び込まれないよう\x01",
            "気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        "#2Pはは、肝に銘じとくよ！\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    def lambda_360F():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_360F)
    Sleep(500)

    def lambda_362C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_362C)
    WaitChrThread(0xC, 2)
    Sound(104, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_68(800, 1100, 4100, 1500)
    OP_6F(0x1)

    #C0091
    ChrTalk(
        0x101,
        "#6P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_3687():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3687)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    #C0092
    ChrTalk(
        0x104,
        "#5P#0305Fそれで結局、誰からなんだ？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#6P#0003F──差出人の名前がある。\x02\x03",

            "#0000F《仔猫#4Rキティ#》からみたいだ。\x02",
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

    #C0094
    ChrTalk(
        0x102,
        "#0105F#11Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        "#0205F#5Pレンさんから……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
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
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    OP_78(0xC, 0x1E)
    ClearMapObjFlags(0xC, 0x4)
    OP_49()
    SetChrPos(0x1E, 12700, 1650, 6400, 0)
    OP_D3(0x1E, 0x0, 0x0, 0x0, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetCameraDistance(25000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは小包を開いて\x01",
            "入っていたものを取り出した。\x02\x03",

            "メッセージカードと共に\x01",
            "漆黒のカードが入っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『──昨日のお礼に\x01",
            "  そのカードをプレゼントするわ。』\x02\x03",

            "『面白い出物があるみたいだから\x01",
            "  覗きに行こうと思ってたんだけど\x01",
            "  お兄さんたちに譲ってあげる。』\x02\x03",

            "『うふふ、有効に使って頂戴ね。』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x329),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x329, 1)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x101,
        "#11P#0013F《黒の競売会#10Rシュバルツオークション#》の……！\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#0105Fど、どうして\x01",
            "あの子がこんなものを……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        (
            "#6P#0305F確か、各国のＶＩＰにしか\x01",
            "贈られない招待カードだったよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#6P#0206Fそれ以前に……\x02\x03",

            "#0201Fどうして、わたしたちが\x01",
            "これに関心を持っているのを\x01",
            "知っていたんでしょう……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0103
    ChrTalk(
        0x101,
        (
            "#5P#0003F──あの子に関しては\x01",
            "深く考えても仕方なさそうだ。\x02\x03",

            "#0001Fそれより……\x01",
            "このカード、本物だと思うか？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0108Fそうね……\x02\x03",

            "#0101F高級感のあるあつらえといい、\x01",
            "本物である可能性は高いと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#6P#0201F金色の薔薇の刻印……\x01",
            "本物の金箔が使われていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#0301F本日夜７時、保養地ミシュラムの\x01",
            "ハルトマン議長邸にて開催、か。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0107
    ChrTalk(
        0x101,
        (
            "#5P#0006F──なあ、みんな。\x02\x03",

            "#0008F課長にはあんな風に\x01",
            "釘を刺されたばかりだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        "#0100Fみなまで言わないで、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#6P#0309Fま、据え膳喰わぬは\x01",
            "何とやらってヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#6P#0202F……課長が今日も\x01",
            "本部に出ていて幸いでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#5P#0001Fみんな……いいのか？\x02\x03",

            "俺の我儘に付き合わせる形に\x01",
            "なると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#0104Fふふ、勘違いしないで。\x02\x03",

            "#0108F私はある意味、あなた以上に\x01",
            "《黒の競売会》に興味がある……\x02\x03",

            "#0101F私の属していた世界に\x01",
            "近い人たちが集まるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#6P#0204Fわたしは純粋に\x01",
            "オークションへの好奇心ですね。\x02\x03",

            "レンさんが言っている\x01",
            "『面白い出物』というのも\x01",
            "気になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#6P#0309Fま、俺はゴージャスでセレブな\x01",
            "パーティそのものに興味があるな。\x02\x03",

            "#0304F美味いモンを飲み食いして\x01",
            "セレブで高めなお姉さんとも\x01",
            "お近づきになれるチャンス……\x02\x03",

            "#0302F見逃す手はねえだろうが？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        "#5P#0002F……みんな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0116
    ChrTalk(
        0x101,
        (
            "#5P#0003F──今日は最終日だ。\x02\x03",

            "#0001F昼までに一通り仕事を片付けて\x01",
            "港湾区の水上バス乗り場に行こう。\x02\x03",

            "本当に競売会に潜入するか……\x01",
            "《ミシュラム》に行って考えたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#0100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        (
            "#6P#0300Fそんじゃあ、残った仕事を\x01",
            "とっとと片付けるとすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#6P#0204F一応、新しい依頼がないか\x01",
            "端末もチェックしましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetChrPos(0x1E, 25600, 1650, 9500, 0)
    SetChrFlags(0x1E, 0x80)
    SetMapObjFlags(0xC, 0x4)
    SetScenarioFlags(0xA3, 3)
    OP_C7(0x1, 0x1000)
    OP_29(0x44, 0x1, 0x8)
    OP_29(0x46, 0x1, 0xF)
    OP_29(0x46, 0x4, 0x10)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_2835 end

    def Function_12_4435(): pass

    label("Function_12_4435")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50332.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0xA)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x102, 1000, 30, 125300, 90)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00101.itp")
    Sound(910, 0, 100, 0)
    Sleep(1200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("？？？")

    #A0120
    AnonymousTalk(
        0xFF,
        "#2S#60W……イド……\x02",
    )

    CloseMessageWindow()

    #A0121
    AnonymousTalk(
        0xFF,
        "#2S#50W………ロイド…ってば……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0122
    AnonymousTalk(
        0x101,
        "#5206F#40Wんー……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(910, 0, 100, 0)
    SetChrName("？？？")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            "……ほら、起きて。\x01",
            "もうミーティングの時間よ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0124
    AnonymousTalk(
        0x101,
        "#5205F#4S！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7104", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(23500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0xD, 0x5, 0x14, 0x0, 0x0)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    #Sound(1128, 255, 90, 0)    #voice#Elie

    def lambda_4645():
        OP_96(0xFE, 0x2BC, 0x1E, 0x1E974, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4645)

    #C0125
    ChrTalk(
        0x102,
        "#6P#0105F#8Aきゃっ……\x02",
    )
    #Auto

    Sleep(1000)
    WaitChrThread(0x102, 1)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xE)
    Sleep(150)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_6F(0x10)
    CancelBlur(0)

    #C0126
    ChrTalk(
        0x101,
        (
            "#11P#5205Fあ……\x02\x03",

            "……おはよう、エリィ。\x01",
            "どうしてここに……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_46E7():
        OP_96(0xFE, 0x3E8, 0x1E, 0x1E974, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_46E7)
    WaitChrThread(0x102, 1)
    Sound(1187, 255, 100, 0)    #voice#Elie
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1600)

    #A0127
    AnonymousTalk(
        0x102,
        (
            "あなたが起きて来ないから\x01",
            "様子を見に来たの。\x02\x03",

            "どうせ、ゆうべは色々考えてて\x01",
            "寝付けなかったんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0128
    ChrTalk(
        0x101,
        (
            "#11P#5212Fはは……お見通しか。\x02\x03",

            "#5200Fエリィは……平気そうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#6P#0104Fこの程度でへこたれてたら\x01",
            "キリが無いもの。\x02\x03",

            "#0108Fそれに……私はどこか\x01",
            "気付いていたのかもしれない。\x02\x03",

            "クロスベルで開かれている\x01",
            "“秘密の社交会”というものが\x01",
            "後ろ暗いものである可能性を……\x02\x03",

            "#0106Fでも多分、自分を誤魔化して\x01",
            "気付かないフリをしていたのかも。\x02\x03",

            "これ以上、後ろめたい思いや\x01",
            "悔しい思いをしたくないために。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#11P#5201Fエリィ……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#6P#0102Fだから今は、悔しさや後ろめたさを\x01",
            "素直に受け止めることにしたわ。\x02\x03",

            "課長の言葉じゃないけど……\x01",
            "それが私のバネになると思うから。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#11P#5204Fそっか……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0xD)
    Sleep(100)
    SetChrSubChip(0x101, 0xE)
    Sleep(300)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0xD)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0133
    ChrTalk(
        0x101,
        "#11P#5200F──よし！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2750, 700, 127100, 500)
    MoveCamera(45, 18, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(23500, 500)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x101, 1000, 30, 126400, 270)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4AF1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4AF1)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0134
    ChrTalk(
        0x101,
        (
            "#5204F#5Pエリィがそこまで\x01",
            "気持ちを切り替えてるんだったら\x01",
            "俺もウジウジもしてられないな。\x02\x03",

            "#5200Fすぐに着替えるから\x01",
            "１階で待っててくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#12P#0102Fうん、分かった。\x02\x03",

            "#0109F朝食の準備もしてあるから、\x01",
            "食べながらミーティングしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#5202F#5Pああ、サンキュ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    OP_68(2000, 700, 124000, 2000)

    def lambda_4C33():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C33)
    WaitChrThread(0x102, 1)

    def lambda_4C51():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C51)

    def lambda_4C6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C6B)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)
    OP_6F(0x1)
    Sound(104, 0, 100, 0)
    Fade(500)
    OP_68(1000, 1000, 126400, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)

    #C0137
    ChrTalk(
        0x101,
        (
            "#5202F#5P（エリィ……前に話した時よりも\x01",
            "  迷いがなくなったみたいだ。）\x02\x03",

            "#5204F（うん、俺も負けてられないな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1390, 1000, 128419, 1500)
    OP_93(0x101, 0x163, 0x190)
    OP_6F(0x1)

    #C0138
    ChrTalk(
        0x101,
        (
            "#2P#5200F記念祭も４日目……\x02\x03",

            "今日も忙しくなりそうだ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Call(0, 17)
    Return()

    # Function_12_4435 end

    def Function_13_4DD8(): pass

    label("Function_13_4DD8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50332.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0xA)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x103, 1000, 30, 125300, 90)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    Sound(910, 0, 100, 0)
    Sleep(1200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("？？？")

    #A0139
    AnonymousTalk(
        0xFF,
        "#2S#60W…………………（ゆさゆさ）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0140
    AnonymousTalk(
        0x101,
        "#5206F#40W……ん…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(910, 0, 100, 0)
    SetChrName("？？？")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            "#2S#40W…………………………………\x01",
            "（ゆさゆさ、ゆさゆさ、ゆさゆさ）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0142
    AnonymousTalk(
        0x101,
        (
            "#5208F#30W（……なんだ……地震？）\x02\x03",

            "（それにしちゃあ……\x01",
            "  何だか気持ちいいけど……）\x02\x03",

            "#5203F（ダメだ……また眠く……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("？？？")

    #A0143
    AnonymousTalk(
        0xFF,
        "#2S#40W…………………………………\x02",
    )

    CloseMessageWindow()
    Sound(1219, 255, 90, 0)    #voice#Tio
    Sleep(1200)
    SetChrName("？？？")

    #A0144
    AnonymousTalk(
        0xFF,
        "#2S……出力ミニマム、極小レベル。\x02",
    )

    CloseMessageWindow()
    SetChrName("？？？")

    #A0145
    AnonymousTalk(
        0xFF,
        "#2S凍結プロセス展開───発動。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)
    Sound(1221, 255, 100, 0)    #voice#Tio
    Sleep(500)
    Sound(184, 0, 90, 0)
    Sleep(700)
    Sound(371, 0, 90, 0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0146
    AnonymousTalk(
        0x101,
        "#5211F#4S冷たっ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7104", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(23500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0xD, 0x5, 0x14, 0x0, 0x0)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xE)
    Sleep(150)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_6F(0x10)
    CancelBlur(0)

    #C0147
    ChrTalk(
        0x101,
        "#11P#5205Fえ……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(1283, 255, 100, 0)    #voice#Tio

    #A0148
    AnonymousTalk(
        0x103,
        (
            "……おはようございます。\x01",
            "ロイドさん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0149
    ChrTalk(
        0x101,
        (
            "#11P#5202Fああ、おはよう……\x02\x03",

            "#5205Fあれ……\x01",
            "なんでティオがここに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#6P#0203Fミーティングの時間なのに\x01",
            "ロイドさんが降りてこないので\x01",
            "起こしに来ました。\x02",
        )
    )

    CloseMessageWindow()
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x101,
        (
            "#11P#5205Fあ……\x01",
            "もうそんな時間だったか。\x02\x03",

            "#5206Fでも、おかしいな……\x02\x03",

            "何か冷たいものが\x01",
            "首筋に当たった気がするんだけど\x01",
            "夢だったのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#6P#0203Fいえ、夢ではないです。\x02\x03",

            "#0200Fいくらゆすっても起きないので\x01",
            "極小のダイアモンドダストを\x01",
            "発生させてみました。\x02",
        )
    )

    CloseMessageWindow()
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    #C0153
    ChrTalk(
        0x101,
        (
            "#11P#5211F──ちょっと待て。\x02\x03",

            "なんか聞き捨てならない言葉を\x01",
            "聞いた気がするんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        (
            "#6P#0204F……大丈夫です。\x01",
            "出力最低にしましたから。\x02\x03",

            "#0202Fバッチリ目が覚めたのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#11P#5212Fそれはまあ……そうだけど。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0156
    ChrTalk(
        0x103,
        (
            "#6P#0208Fそれに、寝てる人を起こすのに\x01",
            "どうすればいいのか迷って……\x02\x03",

            "#0206Fそれでつい、確実な方法を\x01",
            "選択してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        "#11P#5205Fどうすればいいのかって……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0158
    ChrTalk(
        0x101,
        (
            "#11P#5208F（……そっか……）\x02\x03",

            "（この子は今まで\x01",
            "  他人を起こした経験も……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x103,
        (
            "#6P#0205F……ロイドさん？\x02\x03",

            "#0206Fその、怒りましたか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#11P#5204Fいや……怒ってないよ。\x02\x03",

            "#5202Fでも、これから起こす時は\x01",
            "ゆするだけじゃなくって\x01",
            "声も掛けてくれ。\x02\x03",

            "それでちゃんと起きられるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        (
            "#6P#0202F……なるほど。\x02\x03",

            "#0204F──そうなると\x01",
            "『おはようございます、ご主人様㈱』と\x01",
            "呼びかければいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#11P#5201F……なぜそーなる？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#6P#0211Fでは、『お兄ちゃん、起きないと\x01",
            "足蹴にするんだからねっ！』──とか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0164
    ChrTalk(
        0x101,
        "#11P#5207Fどこから仕入れた知識だよ！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#6P#0204F冗談です。\x02\x03",

            "#0202Fエリィさんと朝食を用意したので\x01",
            "着替えたら降りてきてください。\x02\x03",

            "それでは……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x190)

    #C0166
    ChrTalk(
        0x101,
        "#11P#5205Fあ、ちょっと待った。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x5A, 0x1F4)

    #C0167
    ChrTalk(
        0x103,
        "#6P#0205F……なんでしょう？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(500)
    OP_68(2750, 700, 127100, 500)
    MoveCamera(45, 18, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(23500, 500)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 126400, 270)
    Sound(804, 0, 100, 0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_596C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_596C)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0168
    ChrTalk(
        0x101,
        (
            "#5204F#5P──ありがとな、ティオ。\x02\x03",

            "#5202F俺を気遣って\x01",
            "様子を見に来てくれたんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        "#12P#0205Fっ……！？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(1800)

    #C0170
    ChrTalk(
        0x101,
        "#5205F#5P#Nあ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    Fade(500)
    OP_68(1000, 1000, 126400, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0171
    ChrTalk(
        0x101,
        (
            "#5204F#5Pははっ……\x01",
            "なんだか昨日悩んでいたのが\x01",
            "どこかに行った気がする。\x02\x03",

            "#5202F……ティオには感謝しないとな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1390, 1000, 128419, 1500)
    OP_93(0x101, 0x163, 0x190)
    OP_6F(0x1)

    #C0172
    ChrTalk(
        0x101,
        (
            "#2P#5200F記念祭も４日目……\x02\x03",

            "今日も忙しくなりそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x1)
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Call(0, 17)
    Return()

    # Function_13_4DD8 end

    def Function_14_5B78(): pass

    label("Function_14_5B78")

    OP_93(0x103, 0xB4, 0x2BC)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_68(2000, 700, 124000, 1500)

    def lambda_5BA7():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BA7)
    WaitChrThread(0x103, 1)
    OP_64(0x103)
    Sound(103, 0, 100, 0)

    def lambda_5BCE():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BCE)

    def lambda_5BE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5BE8)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Return()

    # Function_14_5B78 end

    def Function_15_5C05(): pass

    label("Function_15_5C05")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50332.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0xA)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x104, 700, 30, 125300, 90)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    Sound(910, 0, 100, 0)
    Sleep(1200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("？？？")

    #A0173
    AnonymousTalk(
        0xFF,
        "#2S#60W……おーい……起きろ。\x02",
    )

    CloseMessageWindow()

    #A0174
    AnonymousTalk(
        0xFF,
        (
            "#2S#50Wいつまでも\x01",
            "グースカ寝てんじゃねえよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0175
    AnonymousTalk(
        0x101,
        "#5206F#40W……ん…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("？？？")

    #A0176
    AnonymousTalk(
        0xFF,
        "#2S#30Wったく、仕方ねぇな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(1377, 255, 90, 0)    #voice#Randy
    Sleep(2000)

    #A0177
    AnonymousTalk(
        0x101,
        "#5205Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7104", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(23500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0xD, 0x5, 0x14, 0x0, 0x0)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xE)
    Sleep(150)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_6F(0x10)
    CancelBlur(0)

    #C0178
    ChrTalk(
        0x101,
        "#11P#5205Fあれ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1366, 255, 90, 0)    #voice#Randy
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0179
    AnonymousTalk(
        0x104,
        (
            "どうして俺が野郎なんかを\x01",
            "起こさなきゃならねーんだっつーの。\x02\x03",

            "朝チュンで、半裸のねーちゃんに\x01",
            "優しく起こされるのが\x01",
            "俺様のスタイルだっつーのに。\x02\x03",

            "そしてコーヒーなんか淹れて\x01",
            "２人でまったりと……\x02\x03",

            "いやいや、そのままガバーッと\x01",
            "行っちゃうのも悪くないかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)

    #C0180
    ChrTalk(
        0x101,
        (
            "#11P#5206F……ゴメン。\x01",
            "ランディの妄想に付き合えるほど\x01",
            "頭が回ってないみたいだ……\x02\x03",

            "#5205Fえっと……\x01",
            "もうミーティングの時間なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x104,
        (
            "#6P#0304Fああ、とっくにな。\x02\x03",

            "#0300Fお嬢とティオすけが\x01",
            "朝メシ作ってくれてるから\x01",
            "とっとと喰っちまおうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#11P#5200Fそっか……\x01",
            "すぐに着替えるよ。\x02\x03",

            "#5209F……ははっ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0183
    ChrTalk(
        0x104,
        "#6P#0305F……なんだよ？\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#11P#5204Fランディってカッコいいよな。\x02\x03",

            "#5202Fそういう気の遣い方、\x01",
            "俺にはとても真似できないよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0185
    ChrTalk(
        0x104,
        (
            "#6P#0301Fバ、バカ、お前……\x01",
            "何こッぱずかしいこと言ってんだ！\x02\x03",

            "#0303F落ち込んでる野郎を慰める\x01",
            "趣味なんざ持ってねぇッつーの！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#11P#5214Fはは、自分で言ってんじゃん。\x02\x03",

            "#5204F──大丈夫。\x01",
            "一晩寝たらなんか落ち着いた。\x02\x03",

            "#5200F悔しい気持ちは残ってるけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x104,
        "#6P#0302F……そうか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(3420, 700, 126420, 1500)
    SetChrFlags(0x104, 0x40)

    def lambda_62FC():
        OP_96(0xFE, 0x578, 0x1E, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62FC)
    WaitChrThread(0x104, 1)
    Sleep(500)
    SetCameraDistance(22330, 500)
    Fade(500)
    SetChrFlags(0x104, 0x8)
    SetChrPos(0x101, 2350, 150, 125820, 180)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0x5)
    Sleep(50)
    SetChrSubChip(0x101, 0x6)
    Sleep(50)
    SetChrSubChip(0x101, 0x7)
    OP_0D()
    Sound(820, 0, 100, 0)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x104,
        (
            "#6P#0309F──ま、悔しがれ青少年。\x02\x03",

            "そうやって挫折を知ってこそ\x01",
            "デカイ男になれるってもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#11P#5211Fだから子ども扱いするのは\x01",
            "やめてくれって……\x02\x03",

            "#5213Fとっとと着替えるから\x01",
            "先に下に降りててくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        "#6P#0300Fへいへい。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x104, 0x8)
    EndChrThread(0x101, 0x3)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    SetChrSubChip(0x101, 0xC)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_64B9():
        OP_96(0xFE, 0x3E8, 0x1E, 0x1EB68, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64B9)
    WaitChrThread(0x104, 1)
    Sleep(300)
    ClearChrFlags(0x104, 0x40)
    OP_93(0x104, 0xB4, 0x1F4)
    OP_68(2000, 700, 124000, 2000)

    def lambda_64F7():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64F7)
    WaitChrThread(0x104, 1)
    Sound(103, 0, 100, 0)

    def lambda_651B():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_651B)

    def lambda_6535():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6535)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)

    #C0191
    ChrTalk(
        0x101,
        "#5204F#5P#Nさてと……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1000, 1000, 126400, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 126400, 270)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_68(1390, 1000, 128419, 1500)
    OP_93(0x101, 0x163, 0x190)
    OP_6F(0x1)

    #C0192
    ChrTalk(
        0x101,
        (
            "#2P#5200F記念祭も４日目……\x02\x03",

            "今日も忙しくなりそうだ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Call(0, 17)
    Return()

    # Function_15_5C05 end

    def Function_16_6676(): pass

    label("Function_16_6676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6690")
    OP_A1(0xFE, 0x3E8, 0x4, 0x7, 0x8, 0x9, 0x8)
    Jump("Function_16_6676")

    label("loc_6690")

    Return()

    # Function_16_6676 end

    def Function_17_6691(): pass

    label("Function_17_6691")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(12000, 1850, 9700, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 11300, 850, 9100, 45)
    SetChrPos(0x102, 11300, 850, 10400, 135)
    SetChrPos(0x103, 12600, 850, 9100, 315)
    SetChrPos(0x104, 12600, 850, 10400, 225)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K創立記念祭　４日目\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#0004F──さてと、\x01",
            "４日目の業務を始めよう。\x02\x03",

            "#0000F新しい要請が入っていないか\x01",
            "念のためチェックしないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x102,
        (
            "#0102Fそうね。\x02\x03",

            "#0104F今日は市内でパレードもあるし、\x01",
            "逆に郊外に足を延ばしている観光客も\x01",
            "ちらほら出ているみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        (
            "#0202F紛失物とか迷子とか\x01",
            "色々と入ってきそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        (
            "#5P#0306Fま、そのあたりは正直\x01",
            "全部は面倒見きれねぇけどな。\x02\x03",

            "#0300F俺たちでやれる範囲のフォローを\x01",
            "していけばいいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(25250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetScenarioFlags(0xA1, 4)
    OP_C7(0x1, 0x1000)
    OP_29(0x44, 0x1, 0x5)
    OP_29(0x45, 0x1, 0x5)
    OP_29(0x45, 0x4, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_6691 end

    def Function_18_69E2(): pass

    label("Function_18_69E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50335.itc", 0x1E)
    LoadChrToIndex("apl/ch50011.itc", 0x1F)
    OP_68(1300, 2850, 12300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 1300, 3850, 14800, 180)
    SetChrPos(0x102, 800, 0, 0, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    SetChrFlags(0x160, 0x4)
    SetChrFlags(0x160, 0x2)
    SetChrFlags(0x160, 0x20)
    SetChrChipByIndex(0x160, 0x1E)
    SetChrSubChip(0x160, 0x0)
    SetChrPos(0x160, 16500, 950, 10400, 45)
    BeginChrThread(0x160, 3, 0, 19)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    OP_78(0xE, 0x1D)
    OP_49()
    SetChrPos(0x1D, 16200, 0, 10100, 0)
    OP_D3(0x1D, 0x0, 0xAFC8, 0x0, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    BeginChrThread(0x20, 1, 0, 20)
    OP_68(1300, 1850, 10300, 2000)
    FadeToBright(1000, 0)

    def lambda_6B51():
        OP_96(0xFE, 0x514, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B51)

    def lambda_6B6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B6B)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0199
    ChrTalk(
        0x101,
        "#6P#0005Fあ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(16100, 1850, 10000, 3000)
    SetCameraDistance(24000, 3000)

    def lambda_6BDA():
        OP_96(0xFE, 0x364C, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BDA)
    OP_6F(0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)

    #C0200
    ChrTalk(
        0x160,
        "#3301F#5P………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    #C0201
    ChrTalk(
        0x101,
        (
            "#6P#0001F……ひょっとして\x01",
            "導力ネットワークから\x01",
            "車両の情報を探しているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x160,
        (
            "#3303F#5Pええ、そうよ。\x02\x03",

            "今から１時間以内に\x01",
            "港湾区の南東に停車していた\x01",
            "可能性のある車両について……\x02\x03",

            "クロスベルの全ネット端末に\x01",
            "アクセスをかけて検索しているの。\x02\x03",

            "#3300FＩＢＣのメイン端末と\x01",
            "ソバカス君のデータベースも\x01",
            "利用させてもらおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0203
    ChrTalk(
        0x101,
        (
            "#6P#0006F君は……一体何者なんだ？\x02\x03",

            "#0001F有名な人形師のお孫さん……\x01",
            "ってだけじゃないみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x160,
        (
            "#3304F#5Pうふふ……おじいさんは\x01",
            "レンの協力者というだけよ。\x02\x03",

            "《パパとママ#10Rパ テ ル ＝ マ テ ル#》を直してくれる、\x01",
            "レンの味方の一人……\x02\x03",

            "#3302F《博士》はちょっと信用できないから\x01",
            "内緒で頼らせてもらっているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#6P#0011Fは、博士……？\x02\x03",

            "#0001Fそれに《パパとママ》って……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x160,
        (
            "#3304F#5Pうふふ、分からなくてもいいわ。\x02\x03",

            "このクロスベルにおいて\x01",
            "レンはただの観察者にすぎない。\x02\x03",

            "#3302F《仔猫#4Rキティ#》という名前の、ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x101,
        "#6P#0003F……やっぱりか。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x160,
        (
            "#3309F#5Pうふふ、昨日の追いかけっこは\x01",
            "スリルがあってドキドキしちゃった。\x02\x03",

            "ソバカス君も結構やるけど\x01",
            "あのお姉さんも相当みたいね？\x02\x03",

            "#3302Fふふっ、ちょっと面白い\x01",
            "裏ワザを使われた気もするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        "#6P#0005Fそこまで分かるのか……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_70D7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70D7)
    OP_68(900, 1000, 3000, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1500)

    def lambda_7101():
        OP_96(0xFE, 0x384, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7101)

    def lambda_711B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_711B)
    Sleep(450)

    def lambda_712F():
        OP_96(0xFE, 0x640, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_712F)

    def lambda_7149():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7149)
    Sleep(450)

    def lambda_715D():
        OP_96(0xFE, 0xC8, 0x0, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_715D)

    def lambda_7177():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7177)
    WaitChrThread(0x102, 1)

    def lambda_718C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_718C)
    WaitChrThread(0x104, 1)

    def lambda_719D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_719D)
    WaitChrThread(0x103, 1)

    def lambda_71AE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_71AE)
    WaitChrThread(0x103, 2)
    OP_6F(0x11)

    #C0210
    ChrTalk(
        0x102,
        (
            "#0105F#6Pただいま、ロイド。\x01",
            "言われた通り戻ってきたけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0211
    ChrTalk(
        0x102,
        "#0105F#6Pあら……？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#0205F#6Pその子は……\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x104,
        (
            "#0305F#12Pたしか……\x01",
            "人形工房の孫娘だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ……\x01",
            "ちょっと事情があってさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(13000, 1850, 10000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_93(0x101, 0x10E, 0x0)
    SetChrPos(0x102, 6500, 850, 9800, 90)
    SetChrPos(0x103, 6500, 850, 10800, 90)
    SetChrPos(0x104, 5300, 850, 10300, 90)
    OP_68(15000, 1850, 10000, 2500)

    def lambda_7352():
        OP_96(0xFE, 0x30D4, 0x352, 0x2648, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7352)
    Sleep(50)

    def lambda_736F():
        OP_96(0xFE, 0x30D4, 0x352, 0x2A30, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_736F)
    Sleep(50)

    def lambda_738C():
        OP_96(0xFE, 0x2C24, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_738C)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    EndChrThread(0x20, 0x1)
    Sleep(300)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x160, 0x3)

    #C0215
    ChrTalk(
        0x160,
        "#5P#3301F──見つけた。\x02",
    )

    CloseMessageWindow()

    def lambda_73F5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_73F5)
    Sleep(500)

    #C0216
    ChrTalk(
        0x160,
        (
            "#5P#3308F《ライムス運送会社》の運搬車が\x01",
            "３０分前に駐車しているみたいね。\x02\x03",

            "次の運搬先はベルガード門……\x02\x03",

            "#3304F運搬車の通信番号は……\x01",
            "うん、これでいいみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x160, 0x0)
    Sleep(70)
    SetChrSubChip(0x160, 0x1)
    Sleep(70)
    SetChrSubChip(0x160, 0x2)
    Sleep(70)
    SetChrSubChip(0x160, 0x3)
    Sleep(300)

    #C0217
    ChrTalk(
        0x160,
        (
            "#11P#3300Fこの通信番号に連絡を入れてみて。\x02\x03",

            "多分、あの子の行方が分かるはずよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)

    #C0218
    ChrTalk(
        0x101,
        "#6P#0004F……お見事。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        "#6P#0108Fあの……どうなってるの？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x104,
        (
            "#6P#0306Fさっきから何やってんのか\x01",
            "完璧に付いていけねぇんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#0203F#5P──なるほど。\x02\x03",

            "#0201Fあなたが《仔猫#4Rキティ#》なんですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 500)

    #C0222
    ChrTalk(
        0x102,
        "#12P#0105Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x104,
        (
            "#6P#0301Fおいおい……\x01",
            "マジでどうなってるんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x160,
        (
            "#11P#3309Fうふふ、お姉さんも\x01",
            "昨日は遊んでくれてありがとう。\x02\x03",

            "#3302Fでも今は、それは後回しにした方が\x01",
            "いいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        "#0206F#5P……まあ、確かに。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#6P#0001Fよし……\x01",
            "さっそく連絡してみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)

    def lambda_77BF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_77BF)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetChrName("")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは受け取った通信番号に連絡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(902, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もしもし！\x01",
            "どちらさま！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0229
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fあ……\x02\x03",

            "#0001Fえっと、クロスベル警察、\x01",
            "特務支援課の者ですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "！！\x02",
        )
    )

    CloseMessageWindow()

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よ、よかった！\x01",
            "ギルドか警察あたりに\x01",
            "連絡しようと思ってたんだ！\x02\x03",

            "でもオレ、どっちの番号も知らなくて\x01",
            "それで親父に連絡して……っ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0232
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011Fお、落ち着いてください。\x02\x03",

            "#0001F慌てているみたいですけど……\x01",
            "いったい何があったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そ、それが……\x02\x03",

            "お、お、男の子が\x01",
            "どこかに行っちゃったんだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0234
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fえ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いまオレ、西クロスベル街道の\x01",
            "途中で停車してるんだけど……！\x02\x03",

            "物音がすると思って荷台を確かめたら、\x01",
            "小さい男の子がいて……！\x02\x03",

            "なんか忍び込んだらしくて\x01",
            "このままベルガード門に行くのもアレだし、\x01",
            "会社に相談しようとしたんだけど……！\x02\x03",

            "そしたら通信してる間に\x01",
            "その子、どっかに行っちゃってさ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0236
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F！！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0237
    AnonymousTalk(
        0x102,
        "#0101Fど、どうしたの？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sleep(300)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0238
    ChrTalk(
        0x101,
        (
            "#11P#0001Fああ……\x01",
            "ちょっとまずい事になった。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは手短に状況を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
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

    #C0240
    ChrTalk(
        0x160,
        "#11P#3305Fえ……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        "#0201F#5P……そんな……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#6P#0301Fマズイな、そいつは……！\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        "#11P#0003Fああ、すぐに街道に出よう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    Sound(820, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0244
    AnonymousTalk(
        0x101,
        (
            "#0001F大至急、そちらに向かいます。\x02\x03",

            "あなたは下手に動かないで\x01",
            "その場で待機しててください。\x02\x03",

            "その子が戻ってくるかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よ、よろしく頼む！\x02\x03",

            "とにかく急いでくれ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(807, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0246
    ChrTalk(
        0x101,
        "#11P#0003F急いで西口に出よう。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0247
    ChrTalk(
        0x101,
        "#0001F#6Pそれとレンちゃん、君は……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(14790, 1850, 10210, 500)
    ClearChrFlags(0x160, 0x4)
    ClearChrFlags(0x160, 0x2)
    ClearChrFlags(0x160, 0x20)
    SetChrChipByIndex(0x160, 0xFF)
    SetChrSubChip(0x160, 0x0)
    SetChrPos(0x160, 15300, 950, 10300, 315)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x160, 0x10E, 0x1F4)
    Sleep(300)

    #C0248
    ChrTalk(
        0x160,
        (
            "#11P#3300F……付いていくわ。\x02\x03",

            "足手まといにはならないから\x01",
            "レンも同行させてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        "#6P#0105Fで、でも……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0205F#5Pここで待ってくれた方が\x01",
            "安全だと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x160,
        (
            "#11P#3303Fあの子の行方を\x01",
            "突き止めたのはレンよ。\x02\x03",

            "#3300Fだからレンは\x01",
            "最後まで見届ける必要がある。\x02\x03",

            "#3302Fふふっ……たとえどんな運命が\x01",
            "あの子に降りかかったとしても。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        "#6P#0101Fあなた……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x104,
        (
            "#6P#0306Fよく分からんが\x01",
            "妙に拘ってるみたいだな。\x02\x03",

            "#0301F時間が惜しい。\x01",
            "ロイド、連れて行こうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#0006F#6Pああ。\x02\x03",

            "#0001F──レンちゃん。\x01",
            "君がただの女の子じゃない事は\x01",
            "分かったけど、無茶はしないこと。\x02\x03",

            "それだけは守ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x160,
        (
            "#11P#3306F分かったわ。\x02\x03",

            "#3300Fそれと、レンのことは\x01",
            "呼び捨てにしてちょうだい。\x02\x03",

            "何だかちょっと\x01",
            "くすぐったくなってきたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#0004F#6Pはは、了解だ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(150)

    #C0257
    ChrTalk(
        0x101,
        (
            "#11P#0007F──よし、それじゃあ\x01",
            "すぐにでも西口に向かおう。\x02\x03",

            "西クロスベル街道に出て\x01",
            "コリン君を捜すんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        "#6P#0101Fええ……！\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x103,
        "#0201F#5P了解です……！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x160,
        "#11P#3308F………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x1D, 0x80)
    ClearMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xE, 0x4)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetChrPos(0x4, 12000, 850, 8700, 270)
    SetScenarioFlags(0xA2, 7)
    OP_29(0x46, 0x1, 0xC)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_69E2 end

    def Function_19_843D(): pass

    label("Function_19_843D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8457")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x6, 0x7, 0x6)
    Jump("Function_19_843D")

    label("loc_8457")

    Return()

    # Function_19_843D end

    def Function_20_8458(): pass

    label("Function_20_8458")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8480")
    Sound(849, 0, 70, 0)
    Sound(850, 0, 70, 0)
    Sleep(900)
    Sound(849, 0, 70, 0)
    Sleep(900)
    Jump("Function_20_8458")

    label("loc_8480")

    Return()

    # Function_20_8458 end

    def Function_21_8481(): pass

    label("Function_21_8481")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50343.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch09400.itc", 0x20)
    LoadChrToIndex("apl/ch50344.itc", 0x21)
    LoadChrToIndex("apl/ch50345.itc", 0x22)
    OP_68(3000, 700, 127500, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 0, 0, 119000, 0)
    SetChrPos(0x102, 0, -1000, 118000, 0)
    SetChrPos(0x103, 0, 0, 119000, 0)
    SetChrPos(0x104, 0, 0, 119000, 0)
    SetChrPos(0x160, 1000, 30, 125300, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, 3000, 350, 126100, 180)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 0, -1000, 118000, 0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 0, 0, 119000, 0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis058.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis059.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis060.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis061.itp")
    OP_68(3000, 700, 126000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_86D4():
        OP_95(0xFE, 0, 0, 122000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86D4)

    def lambda_86EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_86EE)
    Sleep(1000)

    def lambda_8702():

        label("loc_8702")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_8702")

    QueueWorkItem2(0x160, 2, lambda_8702)
    WaitChrThread(0x101, 1)

    def lambda_8718():
        OP_95(0xFE, 1000, 30, 124000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8718)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)
    EndChrThread(0x160, 0x2)

    #C0261
    ChrTalk(
        0x101,
        "#12P#0002F……寝ちゃったか。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x160,
        "#3304F#5Pふふ……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x160, 0x20)
    SetChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0x21)
    SetChrSubChip(0x160, 0x0)
    Sleep(70)
    SetChrSubChip(0x160, 0x1)
    Sleep(70)
    SetChrSubChip(0x160, 0x2)
    Sleep(70)
    SetChrSubChip(0x160, 0x3)
    Sleep(500)

    #C0263
    ChrTalk(
        0x160,
        (
            "#3300F#5P可愛い寝顔ね……\x02\x03",

            "何の罪も知らない、\x01",
            "無垢で純粋でまっとうな子……\x02\x03",

            "#3304F……こんなに大きくなったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x160, 500)
    Sleep(300)

    #C0265
    ChrTalk(
        0x101,
        (
            "#12P#0003Fさっき、その子の\x01",
            "親御さんに連絡したよ。\x02\x03",

            "#0000F大急ぎで迎えに来るってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x160,
        "#3308F#5Pそう……\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#12P#0001F君は一番の功労者だ。\x02\x03",

            "当然、紹介するのが\x01",
            "スジだとは思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x160,
        (
            "#3303F#5P──必要ないわ。\x02\x03",

            "#3300Fレンの名前も、存在も。\x01",
            "その人達に伝える必要はない。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#12P#0008Fでも……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0270
    ChrTalk(
        0x101,
        (
            "#12P#0001F──なあ、レン。\x02\x03",

            "君が普通の物差しで計れるような\x01",
            "ただの女の子じゃないのは分かった。\x02\x03",

            "#0003Fあの大鎌を投擲#4Rとうてき#する能力。\x01",
            "《仔猫》としてのハッキング技術。\x02\x03",

            "その子の居場所を特定した\x01",
            "論理的かつ多面的な推理能力……\x02\x03",

            "#0008F……あまりに多才すぎて\x01",
            "現実味が無いくらいだけど……\x02\x03",

            "#0000F君がいわゆる、本当の意味での\x01",
            "『天才』である事は分かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x160,
        "#3304F#5Pふふっ……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x160, 0x21)
    SetChrSubChip(0x160, 0x3)
    Sleep(70)
    SetChrSubChip(0x160, 0x2)
    Sleep(70)
    SetChrSubChip(0x160, 0x1)
    Sleep(70)
    ClearChrFlags(0x160, 0x20)
    ClearChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0xFF)
    SetChrSubChip(0x160, 0x0)
    Sleep(300)

    #C0272
    ChrTalk(
        0x160,
        (
            "#3302F#5P──お兄さん、やっぱり\x01",
            "なかなか見所があるわね。\x02\x03",

            "#3304Fそう、レンの本質はそこにある。\x02\x03",

            "あらゆる情報を取り込み、処理し、\x01",
            "自らを含めた環境を適切に操作する……\x02\x03",

            "#3300F戦闘技術も、ハッキングも、博士論文も、\x01",
            "人形の操作も、お茶会の作法も、\x01",
            "全てはその本質に拠#2Rよ#っていると言えるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#12P#0011Fは、博士論文！？\x02\x01",

            "#0003F──って、まあそれはいいか。\x02\x03",

            "#0001Fつまり、君には分かるってわけだ。\x02\x03",

            "何をどうすれば\x01",
            "自分の望みを叶えられるのかを。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x160,
        (
            "#3309F#5Pクスクス、そうよ。\x02\x03",

            "#3302Fどんな望みでも\x01",
            "レンは叶えることができる。\x02\x03",

            "ううん、正確には\x01",
            "どうやったら世界にレンの望みを\x01",
            "叶えさせればいいのかが分かる。\x02\x03",

            "#3304Fそれがレンの力そのものだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        (
            "#12P#0006F……なるほどね。\x02\x03",

            "#0001Fだったら──\x01",
            "君は一体何を望んでいるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x160,
        "#3305F#5P…………え………………\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        (
            "#12P#0003Fどんな願いでも\x01",
            "世界が叶えてくれるお姫様……\x02\x03",

            "でも、今の君は、\x01",
            "どこに帰ればいいか判らなくて\x01",
            "途方にくれた仔猫みたいに見える。\x02\x03",

            "#0008Fいや……帰るべき場所は\x01",
            "本当は分かっているのかもしれない。\x02\x03",

            "なのに幾つもの大きな岩が\x01",
            "帰り道を塞いでいて帰れない……\x02\x03",

            "#0001Fそうなんじゃないのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x160,
        "#3308F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#12P#0004F……全ては俺の直感と憶測だ。\x01",
            "見当違いだったら謝るよ。\x02\x03",

            "#0000F──だが、俺たちは特務支援課だ。\x02\x03",

            "困っている女の子がいたら\x01",
            "なるべく助けになってあげたいし……\x02\x03",

            "#0002F一緒に帰ってあげる事は出来なくても\x01",
            "岩を取り除く手伝いくらいは出来る。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x160,
        (
            "#3309F#5P……ふふっ……\x02\x03",

            "#3300Fお兄さん、推理だけじゃなくて\x01",
            "妄想も得意だったみたいね。\x02\x03",

            "#3302Fあなたなんかに……\x01",
            "レンの何が分かるっていうの？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#12P#0006Fもちろん分からないさ。\x02\x03",

            "それに、君が頼りたいと思う人は\x01",
            "他にちゃんといるのかもしれない。\x02\x03",

            "#0000Fでも──転がっている岩は\x01",
            "一つだけじゃないんだろう？\x02\x03",

            "俺たちにも任せられるような……\x01",
            "そんな手頃なサイズの岩はないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x160,
        (
            "#3308F#5P#30Wそんな……そんなの……\x02\x03",

            "#3306F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0xBE, 0x1F4)

    #N0283
    NpcTalk(
        0x102,
        "エリィの声",
        (
            "#1P#2S……ロイド？\x01",
            "ハロルドさんが見えたみたい。\x02\x03",

            "#2Sそちらにお通しするわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        "#0011F#5Pいや、その──\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x160, 500)
    Sleep(800)

    #C0285
    ChrTalk(
        0x160,
        "#3308F#40W#5P………………ぁ…………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0286
    ChrTalk(
        0x101,
        (
            "#12P#0000F……何だったら\x01",
            "クローゼットの中に隠れてるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x160,
        (
            "#3305F#5Pあ……\x02\x03",

            "#3306F………………（コクン）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_93F4():

        label("loc_93F4")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_93F4")

    QueueWorkItem2(0x101, 2, lambda_93F4)

    def lambda_9406():
        OP_96(0xFE, 0x0, 0x1E, 0x1E460, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9406)
    Sleep(500)

    def lambda_9423():
        OP_95(0xFE, 1000, 0, 122500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_9423)
    WaitChrThread(0x160, 1)

    def lambda_9441():
        OP_95(0xFE, 2000, 30, 121500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_9441)
    WaitChrThread(0x160, 1)
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move")
    Sound(913, 0, 100, 0)
    Sleep(500)

    def lambda_9478():
        OP_96(0xFE, 0xBB8, 0x1E, 0x1D8A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_9478)

    def lambda_9492():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_9492)
    WaitChrThread(0x160, 1)
    WaitChrThread(0x160, 2)
    EndChrThread(0x101, 0x2)
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move2")
    Sound(914, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0288
    ChrTalk(
        0x101,
        (
            "#0000F#5P──ああ！\x01",
            "こちらにお通ししてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #N0289
    NpcTalk(
        0x102,
        "エリィの声",
        (
            "#1P#2S……？\x01",
            "ええ、ちょっと待っててね。\x02",
        )
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    #N0290
    NpcTalk(
        0xE,
        "男性の声",
        "#1P#2S失礼します……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xE, 0, 0, 119000, 0)
    Sound(103, 0, 100, 0)
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(500)

    def lambda_959F():

        label("loc_959F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_959F")

    QueueWorkItem2(0x101, 2, lambda_959F)

    def lambda_95B1():
        OP_96(0xFE, 0xFFFFFC7C, 0x1E, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95B1)
    BeginChrThread(0xF, 3, 0, 23)
    Sleep(500)

    #C0291
    ChrTalk(
        0xF,
        "#3707F#5P#8Aああ……コリン！\x02",
    )
    #Auto

    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    EndChrThread(0x101, 0x2)

    #C0292
    ChrTalk(
        0xE,
        (
            "#3609F#5P良かった……\x01",
            "本当に良かった……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1000, 700, 126000, 2500)
    MoveCamera(45, 21, 0, 2500)
    SetCameraDistance(24000, 2500)
    SetChrPos(0x102, 0, 0, 119000, 0)

    def lambda_9667():
        OP_96(0xFE, 0xFFFFFC7C, 0x1E, 0x1E654, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9667)

    def lambda_9681():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9681)
    Sleep(500)

    def lambda_9695():
        OP_96(0xFE, 0xFFFFFBB4, 0x1E, 0x1E0DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9695)

    def lambda_96AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_96AF)
    Sleep(500)

    def lambda_96C3():
        OP_96(0xFE, 0xFFFFFF9C, 0x1E, 0x1E0DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_96C3)

    def lambda_96DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_96DD)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0293
    ChrTalk(
        0x102,
        "#12P#0105F（あら……レンちゃんは？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0294
    ChrTalk(
        0x101,
        (
            "#0006F#5P（ああ……\x01",
            "  ちょっと事情があってね。）\x02\x03",

            "#0008F（そこのクローゼットに隠れてる。）\x02",
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

    #C0295
    ChrTalk(
        0x102,
        "#12P#0101F（ええっ？）\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#12P#0205F（またどうして……）\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x104,
        "#12P#0305F（なんか事情がありそうだな。）\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    def lambda_9868():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9868)

    def lambda_9875():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9875)

    def lambda_9882():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9882)

    def lambda_988F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_988F)
    Sleep(300)

    #C0298
    ChrTalk(
        0xE,
        (
            "#11P#3610F──皆さん。\x01",
            "本当にありがとうございました。\x02\x03",

            "#3601F何とお礼を言ったらいいか……\x01",
            "このご恩は決して忘れません……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハロルドは深々と頭を下げた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0300
    ChrTalk(
        0x101,
        (
            "#6P#0011Fそんな……！\x01",
            "どうか頭を上げてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#0100Fその、私たちも任務で\x01",
            "コリン君を捜しただけですし……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)

    #C0302
    ChrTalk(
        0xF,
        (
            "#3701F#11Pいいえ、いいえ！\x02\x03",

            "#3708F皆さんが見つけてくれなかったら\x01",
            "コリンは……この子は……\x02\x03",

            "#3710F……うううっ……\x01",
            "本当に……本当に良かった……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(300)

    #C0303
    ChrTalk(
        0xE,
        "#3600F大丈夫……もう大丈夫だから……\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x104,
        "#12P#0301Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        "#6P#0208Fどうしてそこまで……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xD,
        "#11P#60Wん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3000, 700, 126000, 1500)
    MoveCamera(45, 24, 0, 1500)
    SetCameraDistance(23500, 1500)

    def lambda_9B8F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9B8F)

    def lambda_9B9C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_9B9C)
    Sleep(1200)
    Fade(250)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x1)
    OP_0D()
    Sound(820, 0, 100, 0)
    SetChrSubChip(0xD, 0x0)
    Sleep(250)
    SetChrSubChip(0xD, 0x1)
    Sleep(250)
    SetChrSubChip(0xD, 0x0)
    Sleep(250)
    SetChrSubChip(0xD, 0x1)
    OP_6F(0x79)

    #C0307
    ChrTalk(
        0xF,
        "#6P#3700Fコリン……\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xD,
        (
            "#11P#3805Fあれぇ……？\x02\x03",

            "どうして\x01",
            "パパとママがいるのぉ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xF,
        "#6P#3709Fああ、コリン……！\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xE,
        (
            "#6P#3609F……良かった……本当に……！\x02\x03",

            "#3600Fダメだぞ……？\x01",
            "ママたちに心配をかけたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xD,
        (
            "#11P#3800F？？？\x02\x03",

            "#3809Fあのね、あのね～！\x01",
            "とってもたのしかったのー！\x02\x03",

            "みっしぃのクルマを追いかけて\x01",
            "知らないトモダチもいっぱいできて！\x02\x03",

            "かくれんぼしてニモツばっかりの\x01",
            "クルマにのったらまっくらで～！\x02\x03",

            "おそとに出たらすごくキレイで\x01",
            "きいろいチョウチョウをみつけて！\x02\x03",

            "#3802Fそれで、それでね……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0xFFFFFE70, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xD)

    #C0312
    ChrTalk(
        0xD,
        (
            "#11P#3805Fあれぇ……？\x02\x03",

            "スミレ色のおねえちゃんは～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0313
    ChrTalk(
        0xE,
        "#6P#3605Fスミレ色の……？\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xF,
        "#6P#3700Fおねえちゃん……？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xD,
        (
            "#11P#3809Fうんー！\x02\x03",

            "あのね、あのね！\x01",
            "とってもつよかったのー！\x02\x03",

            "やさしくって\x01",
            "いいにおいがして……\x02\x03",

            "#3802Fそれでね……\x01",
            "パパとおんなじスミレ色の\x01",
            "カミをしてたんだよ～！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0316
    ChrTalk(
        0xF,
        "#6P#3705Fえ……\x02",
    )

    CloseMessageWindow()

    def lambda_9F8D():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9F8D)
    Sleep(50)
    OP_93(0xF, 0x10E, 0x190)
    Sleep(200)

    #C0317
    ChrTalk(
        0xE,
        (
            "#11P#3601Fあの……\x01",
            "その娘さんというのは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#6P#0006Fその……コリン君を捜すのを\x01",
            "手伝ってくれた女の子なんです。\x02\x03",

            "#0008F外国の旅行者みたいで……\x01",
            "身元はちょっと判らないんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xE,
        "#11P#3603Fそ、そうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xF,
        "#11P#3708F………そんな事って…………\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xD,
        (
            "#5P#3809F#40Wおねえちゃん……\x01",
            "……また会いたいなぁ……\x02\x03",

            "#60Wむにゃ……\x01",
            "そしたらもういちど……\x01",
            "………あそんでもらって………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)

    def lambda_A149():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A149)
    Sleep(50)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(300)

    #C0322
    ChrTalk(
        0xF,
        "#6P#3705Fあ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0323
    ChrTalk(
        0xD,
        "#5P#60W……すーすー……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xF,
        "#6P#3700Fコリン……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xE,
        (
            "#6P#3600Fはは……\x01",
            "また寝てしまったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#6P#0004Fよかったらそのまま\x01",
            "寝かせてあげてください。\x02\x03",

            "#0000Fこちらは大丈夫ですから。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1420, 700, 126070, 2000)
    MoveCamera(45, 21, 0, 2000)
    SetCameraDistance(24000, 2000)

    def lambda_A25E():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A25E)
    Sleep(100)
    OP_93(0xF, 0x10E, 0x190)
    OP_6F(0x79)

    #C0327
    ChrTalk(
        0xE,
        (
            "#11P#3609Fありがとうございます。\x01",
            "本当に何から何まで……\x02\x03",

            "#3600Fしかし……\x01",
            "私と同じ髪の色の娘さんか。\x02\x03",

            "#3604Fこれも女神とあの子の\x01",
            "お導きかもしれないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        "#3700F#11Pええ……私もそう思います。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#6P#0001Fその……\x01",
            "何か事情がおありみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xE,
        "#11P#3605Fああ、いえ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    #C0331
    ChrTalk(
        0xF,
        (
            "#3700F……あなた、私は大丈夫です。\x02\x03",

            "ここまでして頂いたのですから\x01",
            "少しは事情をお話しないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xE,
        "#11P#3600F……そうだな。\x02",
    )

    CloseMessageWindow()

    def lambda_A41C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A41C)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    #C0333
    ChrTalk(
        0xE,
        (
            "#11P#3603F──私たち夫婦には\x01",
            "かつて娘が一人いました。\x02\x03",

            "もう７年以上前のことです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0334
    ChrTalk(
        0x101,
        "#6P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#6P#0101Fその……\x01",
            "いたというのは、やはり……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xE,
        (
            "#11P#3608Fはい、不幸な事故で……\x02\x03",

            "#3610Fいえ──事故ではありませんね。\x02\x03",

            "#3601Fあの子は……私たちが\x01",
            "殺したようなものだったんです。\x02",
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

    #C0337
    ChrTalk(
        0x103,
        "#6P#0205Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x104,
        "#12P#0301Fそいつは……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──８年前。\x02\x03",

            "#30W駆け出しの貿易商だった私は\x01",
            "拡大するクロスベルの貿易市場で\x01",
            "何とか勝ち残ることに必死でした。\x02\x03",

            "#30Wその結果、共和国方面の\x01",
            "危険な相場に手を出してしまい……\x02\x03",

            "#30W多額の債務を負う事になったんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W幼い娘を連れながらの逃亡生活……\x02\x03",

            "逃げども逃げども債権者に追われ、\x01",
            "私たちに安住の地はありませんでした。\x02\x03",

            "#30Wこのままでは悪名高いマフィアが\x01",
            "出張ってきてしまうかもしれない──\x02\x03",

            "#30Wそれを恐れた私たちは\x01",
            "娘を旧い友人の所に預けました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──共和国に住む、信頼できる友人です。\x02\x03",

            "#30W全て借金を片付けて……\x01",
            "完全に身奇麗になったところで\x01",
            "娘を迎えに来るつもりだったんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──幸い、頼りになる先生の助言で\x01",
            "私たちは債務を整理する事ができました。\x02\x03",

            "#30Wコネやツテを生かして事業を建て直し、\x01",
            "死にものぐるいで働いて……\x02\x03",

            "#30W何とか１年で、借金の全額を\x01",
            "返済することに成功したんです。\x02\x03",

            "#30Wこれでやっと娘に会える……\x01",
            "また一家３人で暮らすことができる……\x02\x03",

            "#30W……そう思って……\x01",
            "娘を預けた友人の元を訪ねたら……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(1500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──不審火、だったそうです。\x02\x03",

            "#30Wその頃、組織だった放火強盗事件が\x01",
            "共和国方面で頻発していたらしく……\x02\x03",

            "#30W私の友人宅も、その被害に遭いました。\x02\x03",

            "#30W友人宅は郊外にあったため\x01",
            "当局による発見も遅れて……\x02\x03",

            "#30Wそして……預けていた私たちの娘も\x01",
            "それに巻き込まれていました……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W私たちは……\x01",
            "半狂乱になって娘を捜しました。\x02\x03",

            "#30Wですが……遺体の状況はどれも酷く\x01",
            "結局、家にいた全員が亡くなったという\x01",
            "検死結果しか伝えられませんでした。\x02\x03",

            "#30W私たちの娘は……\x01",
            "何物にも替えがたい大切な宝物は\x01",
            "永遠に失われてしまっていたんです。\x02\x03",

            "#30Wもう……\x01",
            "私たちには絶望しか残りませんでした。\x02\x03",

            "#30W……あの子を死の運命に追いやりながら\x01",
            "何のために生きているのかも分からず……\x02\x03",

            "#30Wこのまま夫婦二人で\x01",
            "心中しようかとまで考えましたが……\x02\x03",

            "#30W──そんな時に、判ったんです。\x02\x03",

            "#30W妻がコリンを……\x01",
            "あの子の弟を身篭っていることが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W現金なもので、それが判ってから\x01",
            "私たちは生きる気力を取り戻しました。\x02\x03",

            "#30W二度と失敗しないような\x01",
            "手堅く誠実な商売だけを心がけて……\x02\x03",

            "#30Wそうしてコリンが生まれ……\x01",
            "私たちは徐々に立ち直っていきました。\x02\x03",

            "#30W──ですがその間、\x01",
            "私たちは目を逸らし続けていたんです。\x02\x03",

            "#30W自分たちの不甲斐なさのせいで\x01",
            "娘を亡くしてしまった痛みから……\x02\x03",

            "#30W……私たちが犯してしまった罪から……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    SetCameraDistance(24000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0346
    ChrTalk(
        0xF,
        "#3710F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xE,
        (
            "#11P#3608Fこれが──\x01",
            "私たち夫婦が背負った罪です。\x02\x03",

            "#3603Fすみません……\x01",
            "長々とつまらない話を……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#6P#0008F……そんな事が…………\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#6P#0106Fその……何と言ったらいいか……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        "#12P#0306F……因果な話ッスね。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        "#6P#0208F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xF,
        (
            "#3708F#11Pですが……\x01",
            "この子が大きくなり、娘の面影を\x01",
            "次第に見せるようになるにつれて……\x02\x03",

            "いつしか私たちは\x01",
            "罪悪感に苛#2Rさいな#まれるようになりました。\x02\x03",

            "#3710F……あの小さな手を\x01",
            "手放さなければよかった……\x02\x03",

            "苦しくても、辛くても\x01",
            "親子で一緒にいればよかった……\x02\x03",

            "そんな後悔ばかりを\x01",
            "するようになっていったんです……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "#11P#3603F……そこで私たちは\x01",
            "改めてこう思い込む事にしました。\x02\x03",

            "#3600Fコリンを授かることができたのは\x01",
            "亡き娘と女神が導いてくれたから……\x02\x03",

            "だからこそ私たち一家は……\x01",
            "絶対に幸せにならなくてはならない。\x02\x03",

            "それが娘に報いる事ができる\x01",
            "たった一つの方法なんだと……\x02\x03",

            "#3603F……身勝手な理屈なのは\x01",
            "百も承知しているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        "#6P#0108Fハロルドさん……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#6P#0204F……それもまた\x01",
            "一つの考え方ではないかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0356
    ChrTalk(
        0x104,
        (
            "#12P#0302Fああ……変に悔やんで\x01",
            "立ち止まるより遥かにいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xE,
        (
            "#11P#3609Fはは……ありがとうございます。\x02\x03",

            "#3600F……しかし……\x01",
            "不思議なこともあるものですね。\x02\x03",

            "コリンを助けてくれたお嬢さん……\x01",
            "私と同じ髪の色だったそうですが。\x02\x03",

            "#3604Fあの子も──亡くなった娘も\x01",
            "同じスミレ色の髪だったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#6P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        "#6P#0108Fそれで……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xF,
        (
            "#3709F#11Pええ……まるであの子が天国から\x01",
            "コリンを守ってくれたみたいで……\x02\x03",

            "#3700F──あの、皆さん。\x02\x03",

            "そのお嬢さんを見かけたら\x01",
            "どうか連絡をいただけませんか？\x02\x03",

            "改めてお会いして……\x01",
            "心からのお礼をお伝えしたいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#6P#0003F──判りました。\x02\x03",

            "#0000F……もし、連絡がついたら\x01",
            "必ずあの子に伝えておきます。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x202), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_8481 end

    def Function_22_B749(): pass

    label("Function_22_B749")


    def lambda_B74E():
        OP_95(0xFE, 0, 0, 122000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B74E)

    def lambda_B768():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B768)
    WaitChrThread(0xE, 1)

    def lambda_B77D():
        OP_95(0xFE, 1200, 30, 125700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B77D)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x5A, 0x1F4)
    Return()

    # Function_22_B749 end

    def Function_23_B79E(): pass

    label("Function_23_B79E")


    def lambda_B7A3():
        OP_95(0xFE, 0, 0, 122000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B7A3)

    def lambda_B7BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_B7BD)
    WaitChrThread(0xF, 1)

    def lambda_B7D2():
        OP_95(0xFE, 1200, 30, 124700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B7D2)
    WaitChrThread(0xF, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_23_B79E end

    def Function_24_B7F0(): pass

    label("Function_24_B7F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch00600.itc", 0x22)
    LoadChrToIndex("apl/ch50346.itc", 0x23)
    LoadChrToIndex("chr/ch00700.itc", 0x24)
    LoadChrToIndex("apl/ch50349.itc", 0x25)
    LoadChrToIndex("apl/ch50115.itc", 0x26)
    OP_68(0, 900, 121500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 100, 30, 121800, 90)
    SetChrPos(0x104, 200, 30, 123100, 135)
    SetChrPos(0x103, -800, 30, 123000, 135)
    SetChrPos(0x102, -1300, 30, 121300, 90)
    SetChrPos(0x160, 3000, 30, 121000, 315)
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(1500, 900, 121500, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x1)

    #C0362
    ChrTalk(
        0x101,
        (
            "#6P#0003F……帰ったよ。\x02\x03",

            "#0000Fもう、出てきても大丈夫だ。\x02",
        )
    )

    CloseMessageWindow()

    #N0363
    NpcTalk(
        0x160,
        "レン",
        "#2S#11P#40W………………………………\x02",
    )

    CloseMessageWindow()
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move")
    Sound(913, 0, 100, 0)
    Sleep(500)
    SetCameraDistance(21500, 2500)

    def lambda_BA02():
        OP_96(0xFE, 0x7D0, 0x1E, 0x1DA9C, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_BA02)

    def lambda_BA1C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_BA1C)
    WaitChrThread(0x160, 1)
    WaitChrThread(0x160, 2)
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move2")
    Sound(914, 0, 100, 0)
    Sleep(500)
    OP_93(0x160, 0x10E, 0x190)
    Sleep(500)

    #C0364
    ChrTalk(
        0x160,
        "#11P#3313F#60W……………………………………\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x102,
        "#6P#0105Fあ……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x103,
        "#0208F#6Pレン、さん……\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#6P#0008F……よかったのか？\x02\x03",

            "#0001F追いかければ\x01",
            "まだ間に合うと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x160,
        (
            "#11P#3312F#40W……ううん……いいの……\x02\x03",

            "レンがこの街に来た理由……\x01",
            "その１つが無くなったから……\x02\x03",

            "#3314Fだから……これでいいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#6P#0006Fそう、か……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそんな……\x01",
            "本当にそれでいいの……！？\x02\x03",

            "レンちゃん、\x01",
            "どう考えてもあなたは……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0371
    ChrTalk(
        0x104,
        (
            "#0306F#5P──やめとけや、お嬢。\x02\x03",

            "#0301F世の中には、真っ当な人間には\x01",
            "想像も付かない事情だってある。\x02\x03",

            "他人が口出せることじゃねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        "#6P#0108Fそ、それは……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0373
    ChrTalk(
        0x103,
        "#0206F……わたしも同感です。\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        "#6P#0008F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x160,
        (
            "#11P#3314F#40Wふふっ……そんな顔をしないで。\x02\x03",

            "#3312F#40W──ありがとう、お兄さん。\x02\x03",

            "レンの帰り道を邪魔している\x01",
            "#40W幾つもの大きな岩……\x02\x03",

            "#3300Fその１つを取り除いてくれて。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BDB7():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BDB7)
    Sleep(50)

    def lambda_BDC7():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BDC7)

    #C0376
    ChrTalk(
        0x101,
        (
            "#6P#0006Fそっか……\x02\x03",

            "#0000F力になれたのなら光栄だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x160,
        (
            "#11P#3300Fふふっ……\x01",
            "お姉さんたちも感謝しているわ。\x02\x03",

            "#3312F……今日のお礼はいずれ、\x01",
            "ちゃんとさせてもらうから……\x02\x03",

            "#3314Fだから……\x01",
            "レンはこれで失礼するわね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x160, 0x20)
    SetChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0x26)
    SetChrSubChip(0x160, 0x4)
    Sleep(100)
    SetChrSubChip(0x160, 0x5)
    Sleep(100)
    SetChrSubChip(0x160, 0x6)
    Sound(820, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0x160, 0x7)
    Sleep(1000)
    SetChrSubChip(0x160, 0x6)
    Sleep(100)
    SetChrSubChip(0x160, 0x5)
    Sleep(100)
    ClearChrFlags(0x160, 0x20)
    ClearChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0xFF)
    SetChrSubChip(0x160, 0x0)
    Sleep(500)
    OP_92(0x160, 0x0, 0x1D650, 0x1F4)

    def lambda_BF15():

        label("loc_BF15")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_BF15")

    QueueWorkItem2(0x101, 2, lambda_BF15)

    def lambda_BF27():

        label("loc_BF27")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_BF27")

    QueueWorkItem2(0x102, 2, lambda_BF27)

    def lambda_BF39():

        label("loc_BF39")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_BF39")

    QueueWorkItem2(0x103, 2, lambda_BF39)

    def lambda_BF4B():

        label("loc_BF4B")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_BF4B")

    QueueWorkItem2(0x104, 2, lambda_BF4B)

    def lambda_BF5D():
        OP_95(0xFE, 0, 0, 120400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_BF5D)
    WaitChrThread(0x160, 1)
    Sound(103, 0, 100, 0)

    def lambda_BF81():
        OP_95(0xFE, 0, 0, 119000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_BF81)

    def lambda_BF9B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_BF9B)
    Sleep(800)
    Sound(104, 0, 100, 0)

    #C0378
    ChrTalk(
        0x101,
        "#0011F#5Pあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x160, 1)
    WaitChrThread(0x160, 2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Fade(500)
    OP_68(3300, 1000, 63700, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 8000, 0, 64500, 180)
    SetChrPos(0x102, 8000, 0, 64500, 180)
    SetChrPos(0x103, 8000, 0, 64500, 180)
    SetChrPos(0x104, 8000, 0, 64500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x160, 2700, 0, 62700, 270)
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x160, 3, 0, 31)
    OP_68(-700, 1000, 63700, 4000)
    OP_0D()
    Sleep(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(450)
    BeginChrThread(0x102, 3, 0, 28)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 29)
    Sleep(450)
    BeginChrThread(0x104, 3, 0, 30)
    WaitChrThread(0x160, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)
    Sleep(300)

    #C0379
    ChrTalk(
        0x101,
        "#0008F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        (
            "#12P#0108F……本当に良かったの？\x01",
            "追いかけて保護しなくて……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C17D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C17D)
    Sleep(50)

    def lambda_C18D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C18D)
    Sleep(300)

    #C0381
    ChrTalk(
        0x101,
        (
            "#5P#0006Fああ……\x01",
            "もちろんそれは考えたけど。\x02\x03",

            "#0000Fでも、それは俺たちの\x01",
            "役目じゃない気がしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#0305Fへぇ……？\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x103,
        (
            "#0205F#11Pロイドさんお得意の\x01",
            "推理ですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#5P#0002Fいや、推理というか──\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 2000, -1000, 69500, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x8)
    Sleep(300)
    #Sound(1704, 255, 95, 0)    #voice#Estelle
    Sleep(300)

    #N0385
    NpcTalk(
        0x10,
        "？？？",
        "#1P#2S#15A#40Wあの～、ごめんくださーい！\x02",
    )
    #Auto

    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C32B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C32B)

    def lambda_C338():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C338)

    def lambda_C345():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C345)

    def lambda_C352():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C352)
    Sleep(300)

    #C0386
    ChrTalk(
        0x101,
        "#0005F#6P今のは……\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#12P#0105F１階からみたいね。\x02",
    )

    CloseMessageWindow()
    OP_68(-700, 500, 63700, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(1500, 2850, 10200, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 900, 3000, 14000, 180)
    SetChrPos(0x102, 2000, 3000, 14000, 180)
    SetChrPos(0x103, 900, 3500, 14500, 180)
    SetChrPos(0x104, 2000, 3500, 14500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 400, 0, 1700, 0)
    SetChrPos(0x11, 1500, 0, 1500, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_68(1500, 1850, 10100, 3000)
    FadeToBright(1000, 0)

    def lambda_C4AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C4AE)

    def lambda_C4BF():
        OP_96(0xFE, 0x384, 0x352, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4BF)
    Sleep(150)

    def lambda_C4DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C4DC)

    def lambda_C4ED():
        OP_96(0xFE, 0x7D0, 0x352, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C4ED)
    Sleep(50)

    def lambda_C50A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C50A)

    def lambda_C51B():
        OP_96(0xFE, 0x384, 0x352, 0x2A30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C51B)
    Sleep(150)

    def lambda_C538():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C538)

    def lambda_C549():
        OP_96(0xFE, 0x7D0, 0x352, 0x2A30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C549)
    WaitChrThread(0x101, 1)
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
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0388
    ChrTalk(
        0x102,
        "#0102F#5Pあら……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        "#5P#0000F君たちは……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(400, 1100, 2900, 2000)
    MoveCamera(53, 19, 0, 2000)
    SetCameraDistance(25000, 2000)
    Sleep(1000)

    def lambda_C647():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C647)
    Sleep(200)

    def lambda_C664():
        OP_96(0xFE, 0x5DC, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C664)
    Sleep(80)

    def lambda_C681():
        OP_96(0xFE, 0xFFFFFF9C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C681)
    Sleep(120)

    def lambda_C69E():
        OP_96(0xFE, 0x4B0, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C69E)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7520", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0390
    AnonymousTalk(
        0x10,
        (
            "えへへ……こんにちは。\x02\x03",

            "いきなりゴメンね？\x01",
            "連絡も無しに訪ねちゃって……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0391
    AnonymousTalk(
        0x11,
        (
            "お邪魔かと思ったんですけど\x01",
            "至急、確認したいことがあって……\x02\x03",

            "少しだけお時間を頂けませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0392
    ChrTalk(
        0x101,
        "#0000F#5Pそれは構わないけど……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x104,
        "#5P#0305F一体全体、なんの話だよ？\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x103,
        (
            "#5P#0201F《黒の競売会#10Rシュバルツオークション#》の\x01",
            "件についてでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "#12P#0806Fうーん、あれはちょっと\x01",
            "保留中っていうか……\x02\x03",

            "#0801F……そ、それよりも……\x02\x03",

            "今日の午後、ロイド君が\x01",
            "ある人物と一緒に歩いてたって\x01",
            "目撃情報を聞いたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#0005F#5Pある人物……？\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x11,
        (
            "#12P#0903F……スミレ色の髪の女の子だよ。\x02\x03",

            "#0901F多分、白いドレスを\x01",
            "着ていたと思うんだけど……\x02",
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

    #C0398
    ChrTalk(
        0x101,
        "#0011F#5Pえっと、それって……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x102,
        "#5P#0101Fレンちゃんの事、よね？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0400
    ChrTalk(
        0x10,
        "#12P#0813F#4Sっ！！！\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x11,
        "#12P#0901Fやっぱり……！\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        (
            "#0011F#5Pちょ、ちょっと待ってくれ。\x02\x03",

            "#0001Fあの子……\x01",
            "君たちの関係者だったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x11,
        (
            "#12P#0903Fああ……そうなんだ。\x02\x03",

            "#0908F僕たちも数ヶ月ほど、\x01",
            "顔を合わせていないけど……\x02\x03",

            "#0902Fでもやっぱり……\x01",
            "まだクロスベルにいるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x10,
        "#12P#0809F#40W……あ、あはは…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x10, 0x1)
    Sleep(130)
    SetChrSubChip(0x10, 0x2)
    Sleep(200)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x11, 0x10, 500)

    #C0405
    ChrTalk(
        0x11,
        "#0901F#11Pエステル……！？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrSubChip(0x10, 0x3)
    OP_0D()
    Sleep(300)

    #C0406
    ChrTalk(
        0x10,
        (
            "#12P#0806Fだ、大丈夫……\x01",
            "安心したら気が抜けちゃって……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(200)
    Fade(250)
    ClearChrFlags(0x10, 0x20)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0407
    ChrTalk(
        0x10,
        (
            "#12P#0804Fよーし……！\x01",
            "こうなったら容赦しないわよ～！\x02\x03",

            "#0802F徹底的にマークをかけて\x01",
            "絶対にとっ捕まえてやるんだから！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0408
    ChrTalk(
        0x104,
        (
            "#5P#0302Fおいおい。\x01",
            "あの嬢ちゃんも大人気だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x103,
        (
            "#5P#0204Fヨナといい……\x01",
            "凄いモテっぷりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#0006F#5Pえっと……まさかあの子、\x01",
            "遊撃士ってわけじゃないよな？\x02\x03",

            "#0001Fさすがに若すぎるし……\x01",
            "色々危ない事もしていそうだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    #C0411
    ChrTalk(
        0x11,
        "#12P#0904Fうん……遊撃士ではないかな。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x10,
        (
            "#12P#0804Fでも、あたしたちにとっては\x01",
            "身内同然の大切な子よ。\x02\x03",

            "#0800Fこの半年以上……\x01",
            "ずっとあの子を追っていたわ。\x02\x03",

            "あの子を捕まえて……\x01",
            "一緒の“家族”になるために。\x02",
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

    #C0413
    ChrTalk(
        0x101,
        "#0005F#5Pか、家族……？\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        (
            "#5P#0101Fそれは……\x01",
            "深い事情がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x10,
        (
            "#12P#0806Fそりゃあもう……\x01",
            "すっごく話が込み入ってまして。\x02\x03",

            "#0808F#30W……クロスベルに来てからは\x01",
            "あたしも一通り知っちゃったし……\x02\x03",

            "#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)

    #C0416
    ChrTalk(
        0x11,
        (
            "#0906F#11Pほら、君がそこで\x01",
            "ヘコたれててどうするのさ。\x02\x03",

            "#0900Fヘイワース夫妻の情報も集まったし、\x01",
            "あの子の心を開かせるんだろう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 500)

    #C0417
    ChrTalk(
        0x10,
        "#6P#0800Fう、うん……そうよね！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0418
    ChrTalk(
        0x101,
        (
            "#0001F#5Pヘイワース夫妻……\x01",
            "ハロルドさんたちのことか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_D273():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_D273)

    def lambda_D280():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_D280)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0419
    ChrTalk(
        0x10,
        (
            "#12P#0813Fえええっ！？\x02\x03",

            "なんでロイド君たちが\x01",
            "その名前を知ってるワケ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#0012F#5Pいや、それは\x01",
            "こちらの台詞なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#5P#0106F……どうやら今日の出来事を\x01",
            "一通り説明した方が良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Sleep(1000)
    OP_68(5500, 950, 4200, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0xE)
    BeginChrThread(0x10, 3, 0, 25)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x1)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x101, 5000, 130, 2200, 0)
    SetChrPos(0x102, 6000, 130, 2200, 0)
    SetChrPos(0x103, 3300, 0, 2500, 45)
    SetChrPos(0x104, 7000, 0, 3500, 315)
    SetChrPos(0x10, 5000, 130, 6250, 180)
    SetChrPos(0x11, 5800, 130, 6250, 180)
    SetCameraDistance(23000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    MoveCamera(37, 17, 0, 50000)

    #C0422
    ChrTalk(
        0x101,
        (
            "#12P#0003F──そういうわけで、\x01",
            "ちょうど君たちと入れ違いで\x01",
            "あの子は帰って行ったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0423
    ChrTalk(
        0x101,
        "#12P#0011Fちょ、エステル！？\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x10,
        "#5P#0808F#60Wあ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0x1)
    EndChrThread(0x10, 0x3)
    SetChrSubChip(0x10, 0xE)
    Sleep(100)
    SetChrSubChip(0x10, 0x5)
    Sleep(100)
    SetChrSubChip(0x10, 0x6)
    Sleep(100)
    BeginChrThread(0x10, 3, 0, 26)
    Sleep(300)

    #C0425
    ChrTalk(
        0x10,
        (
            "#5P#0811F#50Wや、やだな……\x01",
            "……どうしてこんな……\x02\x03",

            "#0810F#60Wうぐっ……ひっく……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    EndChrThread(0x10, 0x3)
    SetChrSubChip(0x10, 0xB)
    OP_0D()
    Sleep(500)

    def lambda_D5CF():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_D5CF)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0426
    ChrTalk(
        0x10,
        (
            "#0810F#5P……うぅ……\x01",
            "#4Sああああああああっ……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x11, 0x2)
    Sleep(150)
    SetChrSubChip(0x11, 0x3)
    Sleep(150)
    SetChrSubChip(0x11, 0x4)
    Sound(820, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x11, 0x5)
    Sleep(500)

    #C0427
    ChrTalk(
        0x11,
        "#11P#0910F#40Wエステル……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0428
    ChrTalk(
        0x10,
        (
            "#5P#0810F#40Wご、ごめんねヨシュア……\x01",
            "……それにロイド君たちも……\x02\x03",

            "#40Wでもあたし……\x01",
            "何て言ったらいいのか判らなくて……\x02\x03",

            "#0808F#40W……捨てられたんじゃないって……\x01",
            "ちゃんと愛されていたんだって……\x02\x03",

            "#40Wあの子がやっと……\x01",
            "辛くて哀しくて……優しい真実に\x01",
            "#40W……ちゃんと向き合うことができて……\x02\x03",

            "#0810F#40W………うううっ…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0429
    ChrTalk(
        0x102,
        "#12P#0108F辛くて哀しくて、優しい真実……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        "#12P#0008Fハロルドさんたちの話か……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)

    #C0431
    ChrTalk(
        0x11,
        (
            "#5P#0908F──幾つもの\x01",
            "哀しい偶然と誤解があったんだ。\x02\x03",

            "その結果……\x01",
            "とても過酷な道を歩いてきたあの子は\x01",
            "自分自身を騙すことにしてしまった。\x02\x03",

            "#0903F偽物の両親#10Rパテル＝マテル#を作り出すことで\x01",
            "真実を突き止めることを放棄したんだ。\x02\x03",

            "でも……それは無理もない話だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x104,
        (
            "#0306F……なるほど。\x01",
            "幼いがゆえの自己防衛か。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x103,
        (
            "#6P#0208Fですが……\x01",
            "それでは前に進めません。\x02\x03",

            "#0206Fそれどころか……\x01",
            "帰るべき場所にも帰れない。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x11,
        (
            "#5P#0908Fうん……\x02\x03",

            "#0903Fだからこそ僕たちは、\x01",
            "彼女が真実に向かい合える勇気を\x01",
            "持てるよう手助けするつもりだった。\x02\x03",

            "調べた限り、真実は哀しかったけれど\x01",
            "そこには確かな愛情もあったから……\x02\x03",

            "だからきっと……\x01",
            "今の彼女なら乗り越えられると思った。\x02\x03",

            "#0902Fでも……\x01",
            "もうその必要はないみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        (
            "#12P#0004F……ああ。\x02\x03",

            "#0000F少なくとも彼女は\x01",
            "全てを理解したみたいだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x11,
        "#5P#0911Fそうか……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrSubChip(0x11, 0x0)
    OP_0D()
    Sleep(300)

    #C0437
    ChrTalk(
        0x11,
        (
            "#0903F#5Pありがとう、ロイド。\x01",
            "それに支援課の皆さんも。\x02\x03",

            "何てお礼を言ったらいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        (
            "#12P#0004Fはは……気にしないでくれよ。\x02\x03",

            "#0002F成り行きみたいなものだったし、\x01",
            "あの子には世話になったからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x102,
        "#12P#0104Fふふ……確かにそうね。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x10,
        "#5P#0810Fぐすっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x10, 0x14)
    OP_0D()
    SetChrSubChip(0x10, 0x15)
    Sleep(100)
    SetChrSubChip(0x10, 0x16)
    Sleep(200)
    SetChrSubChip(0x10, 0x15)
    Sleep(100)
    SetChrSubChip(0x10, 0xC)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0441
    ChrTalk(
        0x10,
        "#5P#0800F#4S──うん、決めた！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x11, 0x1)
    Fade(250)
    SetChrSubChip(0x10, 0xD)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0442
    ChrTalk(
        0x10,
        (
            "#5P#0802F最大の障害が無くなった以上、\x01",
            "もう手加減してあげないんだから！\x02\x03",

            "#0809F見てなさいよ～、レン！\x02\x03",

            "このまま外堀を埋め尽くした上で\x01",
            "絶対にウチの子にしちゃうからねっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0443
    ChrTalk(
        0x101,
        "#12P#0009Fはは……凄いな。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x104,
        (
            "#0309F#12Pいや～、何だか知らんが\x01",
            "それでこそエステルちゃんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x103,
        "#6P#0202Fなんというか……眩しすぎます。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x11,
        (
            "#11P#0904Fふふ、意気込みは買うけどね。\x02\x03",

            "#0902F調子に乗った時のエステルほど\x01",
            "恐いものはないからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x10,
        "#5P#0804Fフフン、任せなさいっての。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x10, 0x4)
    OP_0D()
    Sleep(500)

    #C0448
    ChrTalk(
        0x10,
        (
            "#5P#0800F──ロイド君、エリィさん。\x01",
            "ティオちゃんにランディさんも。\x02\x03",

            "改めて、あたしからも\x01",
            "お礼を言わせてください。\x02\x03",

            "#0804F本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0449
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エステルは深々と頭を下げた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0450
    ChrTalk(
        0x101,
        "#12P#0002Fエステル……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        "#12P#0102F……エステルさん……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x11, 0x0)
    Sleep(500)

    #C0452
    ChrTalk(
        0x11,
        (
            "#5P#0904F今後、僕たちの力が必要なら\x01",
            "いつでも遠慮なく言って欲しい。\x02\x03",

            "#0902Fもうお互い、警察とか遊撃士とか\x01",
            "わだかまりなんて無いだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x10,
        (
            "#5P#0809Fうんうん！\x01",
            "全力で協力させてもらうわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        (
            "#12P#0004Fはは……分かった。\x02\x03",

            "#0000Fいざという時は、\x01",
            "本気でアテにさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(800)
    SetChrName("")

    #A0455
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとエステルたちは\x01",
            "東通りにある《龍老飯店》へと向かい、\x01",
            "夕食を共にして互いに親睦を深めた。\x02\x03",

            "２人の故郷《リベール王国》で起こった\x01",
            "『異変』の真相とその顛末……\x02\x03",

            "そしてレンという少女が属している\x01",
            "《結社》という謎の組織について……\x02\x03",

            "驚きに満ちた様々な情報を聞きながら\x01",
            "記念祭４日目の夜は更けていくのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    RemoveParty(0x5F, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    SubItemNumber(0x327, 1)
    SubItemNumber(0x328, 1)
    Call(0, 11)
    Return()

    # Function_24_B7F0 end

    def Function_25_E3F7(): pass

    label("Function_25_E3F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E410")
    OP_A1(0xFE, 0x3E8, 0x3, 0xE, 0xF, 0x10)
    Jump("Function_25_E3F7")

    label("loc_E410")

    Return()

    # Function_25_E3F7 end

    def Function_26_E411(): pass

    label("Function_26_E411")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E42B")
    OP_A1(0xFE, 0x3E8, 0x4, 0x6, 0x7, 0x8, 0x9)
    Jump("Function_26_E411")

    label("loc_E42B")

    Return()

    # Function_26_E411 end

    def Function_27_E42C(): pass

    label("Function_27_E42C")


    def lambda_E431():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E431)

    def lambda_E442():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E442)
    WaitChrThread(0x101, 1)

    def lambda_E460():
        OP_95(0xFE, 700, 0, 62700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E460)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    Return()

    # Function_27_E42C end

    def Function_28_E481(): pass

    label("Function_28_E481")


    def lambda_E486():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E486)

    def lambda_E497():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E497)
    WaitChrThread(0x102, 1)

    def lambda_E4B5():
        OP_95(0xFE, 700, 0, 61500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E4B5)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Return()

    # Function_28_E481 end

    def Function_29_E4D6(): pass

    label("Function_29_E4D6")


    def lambda_E4DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E4DB)

    def lambda_E4EC():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E4EC)
    WaitChrThread(0x103, 1)

    def lambda_E50A():
        OP_95(0xFE, 2000, 0, 62700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E50A)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x13B, 0x1F4)
    Return()

    # Function_29_E4D6 end

    def Function_30_E52B(): pass

    label("Function_30_E52B")


    def lambda_E530():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E530)

    def lambda_E541():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E541)
    WaitChrThread(0x104, 1)

    def lambda_E55F():
        OP_95(0xFE, 2000, 0, 61500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E55F)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    Return()

    # Function_30_E52B end

    def Function_31_E580(): pass

    label("Function_31_E580")


    def lambda_E585():
        OP_95(0xFE, -700, 0, 62700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_E585)
    WaitChrThread(0x160, 1)

    def lambda_E5A3():
        OP_95(0xFE, -2200, 0, 67900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_E5A3)
    WaitChrThread(0x160, 1)

    def lambda_E5C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_E5C1)
    Sound(103, 0, 100, 0)

    def lambda_E5D8():
        OP_95(0xFE, -5000, 0, 67900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_E5D8)
    WaitChrThread(0x160, 1)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x160, 2)
    Return()

    # Function_31_E580 end

    def Function_32_E5FC(): pass

    label("Function_32_E5FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis156.itp")
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0456
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K創立記念祭　２日目\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7110", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0457
    AnonymousTalk(
        0x8,
        (
            "──さて、お前ら。\x01",
            "休暇はちゃんと楽しめたか？\x02\x03",

            "代わりと言っちゃなんだが、\x01",
            "今日から最終日までの４日間……\x02\x03",

            "タップリ働いてもらうつもりだから\x01",
            "よろしく頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0458
    ChrTalk(
        0x101,
        "#12P#0006Fふう……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x104,
        (
            "#0306Fしっかし、５日あるうちの\x01",
            "初日だけしか休暇がないとは……\x02\x03",

            "#0301F正直、ケチすぎるんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#0106Fまあ、それだけ警察全体が\x01",
            "忙しいという事なんでしょうし。\x02\x03",

            "#0100F警備や巡回の仕事は、初日が一番\x01",
            "忙しかったんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#5P#1004Fま、そういう事だ。\x02\x03",

            "#1002F一応、市長暗殺を未然に防いだ\x01",
            "ご褒美ってわけだな。\x02\x03",

            "本部も、記念祭中については\x01",
            "雑用を回すつもりはないらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        (
            "#12P#0006Fその分、支援要請の数も\x01",
            "かなり来ていそうですけどね。\x02\x03",

            "#0000F観光客も普段の数倍はいそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#5P#1002Fクク、せっかく名前を売って\x01",
            "遊撃士の人気の足元くらいには\x01",
            "届くようになって来たんだ。\x02\x03",

            "ここらが頑張りどころじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#12P#0002Fまあ、それは確かに。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#0306Fなんか上手い具合に\x01",
            "騙されてる気がするんだが……\x02\x03",

            "#0308Fああ、本当なら看護師の子たちと\x01",
            "《ミシュラム》あたりに\x01",
            "遊びに行きたいんだけどよ～。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(150)

    #C0466
    ChrTalk(
        0x103,
        (
            "#6P#0205F《ミシュラム》というと……\x01",
            "港湾区からの遊覧船で行ける\x01",
            "テーマパークですね？\x02\x03",

            "#0202F《みっしぃ》がマスコットとして\x01",
            "働いているそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ECE2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ECE2)
    Sleep(50)
    TurnDirection(0x102, 0x104, 500)

    #C0467
    ChrTalk(
        0x101,
        (
            "#5P#0005F《みっしぃ》って……\x01",
            "ああ、あのネコのマスコットか。\x02\x03",

            "#0000Fあのキャラは前から知ってるけど\x01",
            "テーマパークってのは\x01",
            "３年前には無かったはずだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        (
            "#5P#0104F《ミシュラム》そのものは昔から\x01",
            "保養地として知られていたけど……\x02\x03",

            "#0102Fそこにテーマパークが出来たのは\x01",
            "２年くらい前だったかしら。\x02\x03",

            "それ以来、凄い人気らしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x104,
        (
            "#0309Fおお、前に一度行ったけど\x01",
            "ありゃあ大したモンだったぜ。\x02\x03",

            "#0302Fま、普段から人気のスポットだから\x01",
            "記念祭中はごった返してそうだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x103,
        (
            "#6P#0204Fなるほど……\x01",
            "ちょっと興味深いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        "#5P#1003F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_EF7A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EF7A)
    Sleep(50)

    def lambda_EF8A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EF8A)
    Sleep(50)
    OP_93(0x103, 0x0, 0x1F4)

    #C0472
    ChrTalk(
        0x101,
        "#12P#0005F……課長？\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x8,
        (
            "#5P#1005Fん、ああ……\x02\x03",

            "#1003Fとにかく、最終日までの４日間は\x01",
            "支援要請だけに専念していいぞ。\x02\x03",

            "#1002Fま、何をどれだけやるのかは\x01",
            "いつも通りお前らに任せておく。\x02\x03",

            "毎日、要請も更新されるだろうから\x01",
            "せいぜい楽しみにしとくんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_E3(0xB)
    OP_68(18000, 1850, 3500, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 19000, 850, 3500, 270)
    SetChrPos(0x102, 19000, 850, 3500, 270)
    SetChrPos(0x103, 19000, 850, 3500, 270)
    SetChrPos(0x104, 19000, 850, 3500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayBGM("ed7106", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    OP_68(16000, 1850, 3500, 2000)

    def lambda_F1C9():
        OP_96(0xFE, 0x3E80, 0x352, 0xB54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F1C9)

    def lambda_F1E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F1E3)
    Sleep(250)

    def lambda_F1F7():
        OP_96(0xFE, 0x3E80, 0x352, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F1F7)

    def lambda_F211():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F211)
    Sleep(400)

    def lambda_F225():
        OP_96(0xFE, 0x4394, 0x352, 0xB54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F225)

    def lambda_F23F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F23F)
    Sleep(250)

    def lambda_F253():
        OP_96(0xFE, 0x4394, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F253)

    def lambda_F26D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F26D)
    WaitChrThread(0x101, 1)

    def lambda_F282():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F282)
    WaitChrThread(0x102, 1)

    def lambda_F293():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F293)
    WaitChrThread(0x103, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)

    def lambda_F2B9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F2B9)
    WaitChrThread(0x104, 1)

    def lambda_F2CA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F2CA)
    WaitChrThread(0x104, 2)
    SetMapObjFlags(0x0, 0x10)
    OP_6F(0x1)
    Sleep(300)

    #C0474
    ChrTalk(
        0x101,
        (
            "#6P#0004F#6Pさてと……とりあえず\x01",
            "端末で支援要請を確認するか。\x02\x03",

            "#0000F場合によったら、\x01",
            "クロスベル市の外にも\x01",
            "足を運ぶ必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x102,
        (
            "#0103F#5Pええ、そうね。\x02\x03",

            "#0100Fアルモリカ村なんかは\x01",
            "最近、観光で足を延ばす人も\x01",
            "多いみたいだし……\x02\x03",

            "鉄道と飛行船以外にも\x01",
            "陸路で来る観光客もいそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x104,
        (
            "#5P#0305Fってことは、東西の門も\x01",
            "普段より通行量は多いって事か。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x103,
        (
            "#0203F……ノエルさんたちも\x01",
            "記念祭中は大変そうですね。\x02\x03",

            "#0200F遊撃士の人たちは\x01",
            "言うまでもないでしょうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#6P#0001Fああ。\x01",
            "俺たちも負けてられないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#0104F#5Pでも、あまり根を詰めると\x01",
            "こちらの体力も持たないと思う。\x02\x03",

            "#0102F依頼の緊急度を確かめながら\x01",
            "進めた方がいいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        "#6P#0000Fそれもそうか……\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x104,
        "#5P#0300Fま、ボチボチやって行こうぜ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(16600, 1850, 3500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 16600, 850, 3500, 0)
    SetChrPos(0x1, 16600, 850, 3500, 0)
    SetChrPos(0x2, 16600, 850, 3500, 0)
    SetChrPos(0x3, 16600, 850, 3500, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0xA0, 0)
    OP_29(0x43, 0x1, 0xE)
    OP_29(0x44, 0x4, 0x2)
    OP_29(0x44, 0x1, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_32_E5FC end

    def Function_33_F67B(): pass

    label("Function_33_F67B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F695")
    OP_A1(0x103, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_33_F67B")

    label("loc_F695")

    Return()

    # Function_33_F67B end

    def Function_34_F696(): pass

    label("Function_34_F696")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F6B0")
    OP_A1(0x103, 0xBB8, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_34_F696")

    label("loc_F6B0")

    Return()

    # Function_34_F696 end

    def Function_35_F6B1(): pass

    label("Function_35_F6B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F6E5")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    Sleep(300)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(300)
    Jump("Function_35_F6B1")

    label("loc_F6E5")

    Return()

    # Function_35_F6B1 end

    def Function_36_F6E6(): pass

    label("Function_36_F6E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis068.itp")
    CreatePortrait(1, 289, 127, 353, 191, 0, 0, 64, 64, 0, 0, 64, 64, 0xFFFFFF, 0x1, "c_vis069.itp")
    LoadEffect(0x0, "event\\ev398_00.eff")
    OP_68(190000, 10000, 111000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(1000, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 206000, 50, 127000, 180)
    LoadChrToIndex("chr/ch02707.itc", 0x1F)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x0)
    SetChrPos(0x12, 206000, 0, 127100, 180)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x8000)
    LoadChrToIndex("apl/ch50302.itc", 0x1E)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x2)
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x1F)
    SetChrPos(0x1F, 206000, 500, 126300, 0)
    OP_D3(0x1F, 0x0, 0x2BF20, 0x0, 0x0)
    OP_E5()
    FadeToBright(2000, 0)
    BeginChrThread(0x103, 0, 0, 33)
    BeginChrThread(0x20, 1, 0, 37)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_68(190000, 10000, 108000, 1000)
    OP_64(0x103)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(1000)
    BeginChrThread(0x103, 2, 0, 35)
    Sleep(3000)
    EndChrThread(0x103, 0x2)
    OP_C9(0x1, 0x3, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFF000000, 0x1F4, 0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    VolumeBGM(0x3C, 0x1F4)
    FadeToBright(0, 0)
    PlayMovie(0x0, "ed7_ev06.pmf", 0x68, 0x1)
    Sound(725, 0, 100, 0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(0, -1)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x20, 0x1)
    OP_6E(280, 3000)
    OP_A1(0x103, 0x5DC, 0x4, 0x0, 0x3, 0x4, 0x5)
    OP_A1(0x103, 0x5DC, 0x4, 0x5, 0x6, 0x7, 0x6)
    OP_A1(0x103, 0x5DC, 0x4, 0x5, 0x4, 0x3, 0x0)
    BeginChrThread(0x103, 2, 0, 35)
    PlayEffect(0x0, 0x0, 0x103, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1199, 255, 100, 0)    #voice#Tio
    Sound(506, 0, 100, 0)
    Sound(565, 0, 100, 0)
    Sleep(2000)
    BeginChrThread(0x103, 0, 0, 34)
    BeginChrThread(0x20, 1, 0, 38)
    Sleep(1500)
    EndChrThread(0x103, 0x2)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFF000000, 0x1F4, 0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_68(190000, 10000, 111000, 0)
    OP_6E(350, 0)
    StopEffect(0x0, 0x0)
    VolumeBGM(0x3C, 0x1F4)
    FadeToBright(0, 0)
    PlayMovie(0x0, "ed7_ev07.pmf", 0x68, 0x1)
    Sound(726, 0, 100, 0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(0, -1)
    FadeToDark(0, 0, -1)
    OP_0D()
    FadeToBright(500, 0)
    OP_0D()
    Sound(1282, 255, 90, 0)    #voice#Tio
    EndChrThread(0x20, 0x1)
    EndChrThread(0x103, 0xFF)
    OP_A1(0x103, 0x3E8, 0x4, 0x0, 0x3, 0x4, 0x5)
    OP_63(0x103, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)
    OP_6E(360, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x103, 0x4)
    OP_CA(0x1, 0xFF, 0x0)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0570", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_F6E6 end

    def Function_37_FACC(): pass

    label("Function_37_FACC")

    Sound(849, 0, 100, 0)
    Sleep(900)
    Sound(850, 0, 100, 0)
    Sleep(1800)
    Sound(849, 0, 100, 0)
    Sleep(900)
    Sound(850, 0, 100, 0)
    Sleep(1800)
    Sound(849, 0, 100, 0)
    Return()

    # Function_37_FACC end

    def Function_38_FAF7(): pass

    label("Function_38_FAF7")

    Sound(849, 0, 100, 0)
    Sleep(200)
    Sound(850, 0, 100, 0)
    Sleep(700)
    Sound(849, 0, 100, 0)
    Return()

    # Function_38_FAF7 end

    def Function_39_FB10(): pass

    label("Function_39_FB10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(1000, 900, 1900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 400, 0, 1900, 0)
    SetChrPos(0x102, 1600, 0, 1900, 0)
    SetChrPos(0x103, 400, 0, 700, 0)
    SetChrPos(0x104, 1600, 0, 700, 0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_FBF8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FBF8)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    #Sound(1084, 255, 90, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0482
    AnonymousTalk(
        0x101,
        "#0000Fはい、ロイドです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2083, 255, 100, 0)    #voice#Fran
    #Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0483
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、ロイドさん。\x02\x03"      #line#50
            "お忙しい所をすみません。\x01",
            "今、大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0484
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fああ……\x01",
            "一区切りついた所だから\x01",
            "大丈夫だと思うけど。\x02\x03",

            "緊急の要請が入ったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0485
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いえ、ロイドさんたちに直接、\x01",
            "頼りたいという方がいまして。\x02\x03",

            "貿易商のハロルドさんと\x01",
            "おっしゃる方なんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0486
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fああ、知り合いだけど……\x01",
            "一体どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0487
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それが……\x02\x03",

            "市内のパレードを見ている最中、\x01",
            "お子さんが迷子になったそうなんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0488
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003Fそうか、分かった。\x02\x03",

            "#0001Fどこで待ってもらってるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警察本部の近くにある\x01",
            "噴水の前のベンチのところです。\x02\x03",

            "どうやらその近辺で\x01",
            "お子さんとはぐれたらしくて。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0490
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F分かった、すぐに行ってみるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0491
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0492
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#0105Fどうしたの？\x02",
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
    Sound(804, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0493
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ、貿易商のハロルドさんから\x01",
            "俺たちに頼みがあるらしい。\x02\x03",

            "#0001Fパレードの最中、\x01",
            "お子さんが迷子になったそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0494
    ChrTalk(
        0x102,
        "#11P#0101Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x103,
        (
            "#12P#0206F今日の人出だと\x01",
            "はぐれたら大変そうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x104,
        (
            "#0300F#11Pってことは、祭りには定番の\x01",
            "迷子探しのミッションってわけか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0497
    ChrTalk(
        0x101,
        (
            "#5P#0004Fああ、多分ね。\x02\x03",

            "#0000F警察本部近くの\x01",
            "噴水前で待っているらしいから\x01",
            "とにかく事情を聞きに行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 1000, 0, 1900, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA1, 5)
    OP_29(0x44, 0x1, 0x7)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_39_FB10 end

    def Function_40_10274(): pass

    label("Function_40_10274")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(1300, 1950, 9900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 1900, 850, 9900, 180)
    SetChrPos(0x102, 700, 850, 9900, 180)
    SetChrPos(0x103, 700, 850, 11100, 180)
    SetChrPos(0x104, 1900, 850, 11100, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(806, 2, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10359():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10359)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    #Sound(1084, 255, 90, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0498
    AnonymousTalk(
        0x101,
        "#0000Fはい、ロイドです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2083, 255, 100, 0)    #voice#Fran
    #Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0499
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、ロイドさん。\x02\x03"      #line#50
            "お忙しい所をすみません。\x01",
            "今、大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0500
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fああ……\x01",
            "一区切りついた所だから\x01",
            "大丈夫だと思うけど。\x02\x03",

            "緊急の要請が入ったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0501
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いえ、ロイドさんたちに直接、\x01",
            "頼りたいという方がいまして。\x02\x03",

            "貿易商のハロルドさんと\x01",
            "おっしゃる方なんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0502
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fああ、知り合いだけど……\x01",
            "一体どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それが……\x02\x03",

            "市内のパレードを見ている最中、\x01",
            "お子さんが迷子になったそうなんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0504
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003Fそうか、分かった。\x02\x03",

            "#0001Fどこで待ってもらってるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0505
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警察本部の近くにある\x01",
            "噴水の前のベンチのところです。\x02\x03",

            "どうやらその近辺で\x01",
            "お子さんとはぐれたらしくて。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0506
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F分かった、すぐに行ってみるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0507
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0508
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0105Fどうしたの？\x02",
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
    Sound(804, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    #C0509
    ChrTalk(
        0x101,
        (
            "#11P#0003Fああ、貿易商のハロルドさんから\x01",
            "俺たちに頼みがあるらしい。\x02\x03",

            "#0001Fパレードの最中、\x01",
            "お子さんが迷子になったそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0510
    ChrTalk(
        0x102,
        "#6P#0101Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x103,
        (
            "#5P#0206F今日の人出だと\x01",
            "はぐれたら大変そうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x104,
        (
            "#0300F#5Pってことは、祭りには定番の\x01",
            "迷子探しのミッションってわけか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0513
    ChrTalk(
        0x101,
        (
            "#12P#0004Fああ、多分ね。\x02\x03",

            "#0000F警察本部近くの\x01",
            "噴水前で待っているらしいから\x01",
            "とにかく事情を聞きに行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 1300, 850, 9900, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA1, 5)
    OP_29(0x44, 0x1, 0x7)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_40_10274 end

    def Function_41_109D3(): pass

    label("Function_41_109D3")

    EventBegin(0x0)
    Fade(500)
    OP_68(15760, 1850, 10150, 0)
    MoveCamera(79, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 15760, 850, 10150, 45)
    SetChrPos(0x102, 16560, 850, 9350, 45)
    SetChrPos(0x103, 14830, 850, 9220, 45)
    SetChrPos(0x104, 15630, 850, 8410, 45)
    OP_0D()

    #C0514
    ChrTalk(
        0x101,
        "#0005F捜査二課からの依頼が入ってたな。\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x102,
        (
            "#0105F偽ブランド業者の摘発……\x01",
            "一体、どういう頼み事なのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        (
            "#0302Fつーか、警察本部から\x01",
            "重要そうな支援要請が来るのなんて\x01",
            "初めてじゃねぇか？\x02\x03",

            "#0304F他の連中もやっとこさ、\x01",
            "俺たちを認めてくれたのかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        (
            "#0203F#12Pさぁ……どうでしょう。\x02\x03",

            "#0211Fまた面倒な雑用を押し付けられて\x01",
            "終了という可能性もあるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        (
            "#0000Fまあ、とにかくドノバン警部に\x01",
            "話を聞きに行ってみようか。\x02\x03",

            "上手く行けば、今まで以上に\x01",
            "他の課とも協力できそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        (
            "#0100Fそうね……\x01",
            "行政区の警察本部に行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_41_109D3 end

    def Function_42_10C74(): pass

    label("Function_42_10C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10CA5")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_10CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10CD6")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_10CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D07")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_10D07")

    Return()

    # Function_42_10C74 end

    def Function_43_10D08(): pass

    label("Function_43_10D08")


    #C0520
    ChrTalk(
        0x101,
        (
            "#0000F出かける前に\x01",
            "支援要請くらいは\x01",
            "確認しておくか……\x02\x03",

            "緊急の案件が\x01",
            "入ってるかもしれないし。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_43_10D08 end

    def Function_44_10D6C(): pass

    label("Function_44_10D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EAC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E32")

    #C0521
    ChrTalk(
        0x103,
        (
            "#0200Fロイドさん、ヨナから\x01",
            "連絡があるかもしれません。\x02\x03",

            "あまり遠くへ行くのはどうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな……\x01",
            "支度を済ませて\x01",
            "早めにジオフロントに向かおうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E96")

    label("loc_10E32")


    #C0523
    ChrTalk(
        0x103,
        (
            "#0200F……ヨナから\x01",
            "連絡があるかもしれないし。\x02\x03",

            "支度を済ませたら\x01",
            "早めにジオフロントに向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E96")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)

    label("loc_10EAC")

    Return()

    # Function_44_10D6C end

    def Function_45_10EAD(): pass

    label("Function_45_10EAD")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_45_10EAD end

    def Function_46_10ED9(): pass

    label("Function_46_10ED9")

    Return()

    # Function_46_10ED9 end

    def Function_47_10EDA(): pass

    label("Function_47_10EDA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F32")
    SetChrFlags(0x0, 0x8)

    label("loc_10F32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F45")
    SetChrFlags(0x1, 0x8)

    label("loc_10F45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F58")
    SetChrFlags(0x2, 0x8)

    label("loc_10F58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F6B")
    SetChrFlags(0x3, 0x8)

    label("loc_10F6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F7E")
    SetChrFlags(0x4, 0x8)

    label("loc_10F7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F91")
    SetChrFlags(0x5, 0x8)

    label("loc_10F91")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    #C0525
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0526
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x50, 6)
    OP_66(0x7, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11031")
    ClearChrFlags(0x0, 0x8)

    label("loc_11031")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11044")
    ClearChrFlags(0x1, 0x8)

    label("loc_11044")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11057")
    ClearChrFlags(0x2, 0x8)

    label("loc_11057")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1106A")
    ClearChrFlags(0x3, 0x8)

    label("loc_1106A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1107D")
    ClearChrFlags(0x4, 0x8)

    label("loc_1107D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11090")
    ClearChrFlags(0x5, 0x8)

    label("loc_11090")

    Call(0, 64)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_47_10EDA end

    def Function_48_110A7(): pass

    label("Function_48_110A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110FF")
    SetChrFlags(0x0, 0x8)

    label("loc_110FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11112")
    SetChrFlags(0x1, 0x8)

    label("loc_11112")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11125")
    SetChrFlags(0x2, 0x8)

    label("loc_11125")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11138")
    SetChrFlags(0x3, 0x8)

    label("loc_11138")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1114B")
    SetChrFlags(0x4, 0x8)

    label("loc_1114B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1115E")
    SetChrFlags(0x5, 0x8)

    label("loc_1115E")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0527
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0528
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x50, 7)
    OP_66(0x8, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_111FE")
    ClearChrFlags(0x0, 0x8)

    label("loc_111FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11211")
    ClearChrFlags(0x1, 0x8)

    label("loc_11211")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11224")
    ClearChrFlags(0x2, 0x8)

    label("loc_11224")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11237")
    ClearChrFlags(0x3, 0x8)

    label("loc_11237")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1124A")
    ClearChrFlags(0x4, 0x8)

    label("loc_1124A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1125D")
    ClearChrFlags(0x5, 0x8)

    label("loc_1125D")

    Call(0, 64)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_48_110A7 end

    def Function_49_11274(): pass

    label("Function_49_11274")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112CC")
    SetChrFlags(0x0, 0x8)

    label("loc_112CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112DF")
    SetChrFlags(0x1, 0x8)

    label("loc_112DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112F2")
    SetChrFlags(0x2, 0x8)

    label("loc_112F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11305")
    SetChrFlags(0x3, 0x8)

    label("loc_11305")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11318")
    SetChrFlags(0x4, 0x8)

    label("loc_11318")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1132B")
    SetChrFlags(0x5, 0x8)

    label("loc_1132B")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    #C0529
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0530
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x51, 0)
    OP_66(0x9, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113CD")
    ClearChrFlags(0x0, 0x8)

    label("loc_113CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113E0")
    ClearChrFlags(0x1, 0x8)

    label("loc_113E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113F3")
    ClearChrFlags(0x2, 0x8)

    label("loc_113F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11406")
    ClearChrFlags(0x3, 0x8)

    label("loc_11406")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11419")
    ClearChrFlags(0x4, 0x8)

    label("loc_11419")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1142C")
    ClearChrFlags(0x5, 0x8)

    label("loc_1142C")

    Call(0, 64)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_49_11274 end

    def Function_50_11443(): pass

    label("Function_50_11443")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114A6")
    SetChrFlags(0x0, 0x8)

    label("loc_114A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114B9")
    SetChrFlags(0x1, 0x8)

    label("loc_114B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114CC")
    SetChrFlags(0x2, 0x8)

    label("loc_114CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114DF")
    SetChrFlags(0x3, 0x8)

    label("loc_114DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114F2")
    SetChrFlags(0x4, 0x8)

    label("loc_114F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11505")
    SetChrFlags(0x5, 0x8)

    label("loc_11505")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0531
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0532
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x51, 1)
    OP_66(0xA, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115A7")
    ClearChrFlags(0x0, 0x8)

    label("loc_115A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115BA")
    ClearChrFlags(0x1, 0x8)

    label("loc_115BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115CD")
    ClearChrFlags(0x2, 0x8)

    label("loc_115CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115E0")
    ClearChrFlags(0x3, 0x8)

    label("loc_115E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115F3")
    ClearChrFlags(0x4, 0x8)

    label("loc_115F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11606")
    ClearChrFlags(0x5, 0x8)

    label("loc_11606")

    Call(0, 64)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_50_11443 end

    def Function_51_1161D(): pass

    label("Function_51_1161D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11675")
    SetChrFlags(0x0, 0x8)

    label("loc_11675")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11688")
    SetChrFlags(0x1, 0x8)

    label("loc_11688")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1169B")
    SetChrFlags(0x2, 0x8)

    label("loc_1169B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116AE")
    SetChrFlags(0x3, 0x8)

    label("loc_116AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116C1")
    SetChrFlags(0x4, 0x8)

    label("loc_116C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116D4")
    SetChrFlags(0x5, 0x8)

    label("loc_116D4")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0533
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0534
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x51, 2)
    OP_66(0xB, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11778")
    ClearChrFlags(0x0, 0x8)

    label("loc_11778")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1178B")
    ClearChrFlags(0x1, 0x8)

    label("loc_1178B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1179E")
    ClearChrFlags(0x2, 0x8)

    label("loc_1179E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117B1")
    ClearChrFlags(0x3, 0x8)

    label("loc_117B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117C4")
    ClearChrFlags(0x4, 0x8)

    label("loc_117C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117D7")
    ClearChrFlags(0x5, 0x8)

    label("loc_117D7")

    Call(0, 64)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_51_1161D end

    def Function_52_117EE(): pass

    label("Function_52_117EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11846")
    SetChrFlags(0x0, 0x8)

    label("loc_11846")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11859")
    SetChrFlags(0x1, 0x8)

    label("loc_11859")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1186C")
    SetChrFlags(0x2, 0x8)

    label("loc_1186C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1187F")
    SetChrFlags(0x3, 0x8)

    label("loc_1187F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11892")
    SetChrFlags(0x4, 0x8)

    label("loc_11892")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118A5")
    SetChrFlags(0x5, 0x8)

    label("loc_118A5")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    #C0535
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0536
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x51, 3)
    OP_66(0xC, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11949")
    ClearChrFlags(0x0, 0x8)

    label("loc_11949")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1195C")
    ClearChrFlags(0x1, 0x8)

    label("loc_1195C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1196F")
    ClearChrFlags(0x2, 0x8)

    label("loc_1196F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11982")
    ClearChrFlags(0x3, 0x8)

    label("loc_11982")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11995")
    ClearChrFlags(0x4, 0x8)

    label("loc_11995")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_119A8")
    ClearChrFlags(0x5, 0x8)

    label("loc_119A8")

    Call(0, 64)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_52_117EE end

    def Function_53_119BF(): pass

    label("Function_53_119BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A17")
    SetChrFlags(0x0, 0x8)

    label("loc_11A17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A2A")
    SetChrFlags(0x1, 0x8)

    label("loc_11A2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A3D")
    SetChrFlags(0x2, 0x8)

    label("loc_11A3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A50")
    SetChrFlags(0x3, 0x8)

    label("loc_11A50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A63")
    SetChrFlags(0x4, 0x8)

    label("loc_11A63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A76")
    SetChrFlags(0x5, 0x8)

    label("loc_11A76")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0537
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0538
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x51, 4)
    OP_66(0xD, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B16")
    ClearChrFlags(0x0, 0x8)

    label("loc_11B16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B29")
    ClearChrFlags(0x1, 0x8)

    label("loc_11B29")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B3C")
    ClearChrFlags(0x2, 0x8)

    label("loc_11B3C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B4F")
    ClearChrFlags(0x3, 0x8)

    label("loc_11B4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B62")
    ClearChrFlags(0x4, 0x8)

    label("loc_11B62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B75")
    ClearChrFlags(0x5, 0x8)

    label("loc_11B75")

    Call(0, 64)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_53_119BF end

    def Function_54_11B8C(): pass

    label("Function_54_11B8C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11BEF")
    SetChrFlags(0x0, 0x8)

    label("loc_11BEF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C02")
    SetChrFlags(0x1, 0x8)

    label("loc_11C02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C15")
    SetChrFlags(0x2, 0x8)

    label("loc_11C15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C28")
    SetChrFlags(0x3, 0x8)

    label("loc_11C28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C3B")
    SetChrFlags(0x4, 0x8)

    label("loc_11C3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C4E")
    SetChrFlags(0x5, 0x8)

    label("loc_11C4E")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    #C0539
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0540
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x51, 5)
    OP_66(0xE, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CEE")
    ClearChrFlags(0x0, 0x8)

    label("loc_11CEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D01")
    ClearChrFlags(0x1, 0x8)

    label("loc_11D01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D14")
    ClearChrFlags(0x2, 0x8)

    label("loc_11D14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D27")
    ClearChrFlags(0x3, 0x8)

    label("loc_11D27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D3A")
    ClearChrFlags(0x4, 0x8)

    label("loc_11D3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D4D")
    ClearChrFlags(0x5, 0x8)

    label("loc_11D4D")

    Call(0, 64)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_54_11B8C end

    def Function_55_11D64(): pass

    label("Function_55_11D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DBA")
    SetChrName("")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "家具アイテムを入手すると\x01",
            "主人公達の部屋に置く事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x51, 6)

    label("loc_11DBA")

    Return()

    # Function_55_11D64 end

    def Function_56_11DBB(): pass

    label("Function_56_11DBB")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis164.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0542
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力車模型が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_56_11DBB end

    def Function_57_11E66(): pass

    label("Function_57_11E66")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis165.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0543
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力コンポが置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_11F2E"),
        (1, "loc_11F37"),
        (2, "loc_11F40"),
        (3, "loc_11F49"),
        (4, "loc_11F52"),
        (5, "loc_11F5B"),
        (6, "loc_11F64"),
        (7, "loc_11F6D"),
        (SWITCH_DEFAULT, "loc_11F76"),
    )


    label("loc_11F2E")

    PlayBGM("ed7400", 0)
    Jump("loc_11F76")

    label("loc_11F37")

    PlayBGM("ed7401", 0)
    Jump("loc_11F76")

    label("loc_11F40")

    PlayBGM("ed7402", 0)
    Jump("loc_11F76")

    label("loc_11F49")

    PlayBGM("ed7204", 0)
    Jump("loc_11F76")

    label("loc_11F52")

    PlayBGM("ed7205", 0)
    Jump("loc_11F76")

    label("loc_11F5B")

    PlayBGM("ed7201", 0)
    Jump("loc_11F76")

    label("loc_11F64")

    PlayBGM("ed7200", 0)
    Jump("loc_11F76")

    label("loc_11F6D")

    PlayBGM("ed7202", 0)
    Jump("loc_11F76")

    label("loc_11F76")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_57_11E66 end

    def Function_58_11FA5(): pass

    label("Function_58_11FA5")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis167.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0544
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁掛け時計がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_58_11FA5 end

    def Function_59_12048(): pass

    label("Function_59_12048")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis166.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0545
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "上品な花瓶が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_59_12048 end

    def Function_60_120F3(): pass

    label("Function_60_120F3")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis168.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0546
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁かけみっしぃがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_60_120F3 end

    def Function_61_1219A(): pass

    label("Function_61_1219A")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0547
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おすわりみっしぃがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_61_1219A end

    def Function_62_12243(): pass

    label("Function_62_12243")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis171.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0548
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "イリアポスターが飾られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_62_12243 end

    def Function_63_122F2(): pass

    label("Function_63_122F2")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis170.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダーツセットが置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_63_122F2 end

    def Function_64_1239F(): pass

    label("Function_64_1239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_123D7")
    OP_DE(0x16, 0x0)

    label("loc_123D7")

    Return()

    # Function_64_1239F end

    def Function_65_123D8(): pass

    label("Function_65_123D8")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1245F")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1245F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1247B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1247B")

    Return()

    # Function_65_123D8 end

    def Function_66_1247D(): pass

    label("Function_66_1247D")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12504")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_12504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12520")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_12520")

    Return()

    # Function_66_1247D end

    def Function_67_12522(): pass

    label("Function_67_12522")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125A9")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_125A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125C5")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_125C5")

    Return()

    # Function_67_12522 end

    def Function_68_125C7(): pass

    label("Function_68_125C7")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1264E")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1264E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1266A")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1266A")

    Return()

    # Function_68_125C7 end

    SaveToFile()

Try(main)
