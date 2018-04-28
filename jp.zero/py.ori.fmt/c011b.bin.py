from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c011b.bin",                # FileName
        "c011b",                    # MapName
        "c011b",                    # Location
        0x0009,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 1000, 0, 2000, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c011b",                  # 0
        "ランディ",               # 1
        "ランディ",               # 2
        "エリィ",                 # 3
        "ティオ",                 # 4
        "ティオ",                 # 5
        "キーア",                 # 6
        "キーア",                 # 7
        "ツァイト",               # 8
        "ツァイト",               # 9
        "セルゲイ課長",           # 10
        "セルゲイ課長",           # 11
        "イアン弁護士",           # 12
        "シズク",                 # 13
        "警備隊員",               # 14
        "警備隊員",               # 15
        "本",                     # 16
        "食器",                   # 17
        "食器",                   # 18
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch00300.itc",                   # 01
        "chr/ch00100.itc",                   # 02
        "chr/ch00200.itc",                   # 03
        "chr/ch08200.itc",                   # 04
        "chr/ch02700.itc",                   # 05
        "chr/ch02502.itc",                   # 06
        "chr/ch02702.itc",                   # 07
        "chr/ch08202.itc",                   # 08
        "chr/ch00202.itc",                   # 09
        "chr/ch00302.itc",                   # 0A
        "chr/ch02707.itc",                   # 0B
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(51840,   150,     126410,  270,  405,  0x0, 0,   10,  0,   255, 255, 0,   3,   255,  0)
    DeclNpc(157419,  0,       128649,  0,    389,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(205529,  29,      128350,  45,   389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(203660,  150,     128610,  0,    389,  0x0, 0,   9,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2710,    0,       2509,    225,  404,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(102910,  0,       72099,   90,   389,  0x0, 0,   0,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(101139,  150,     65339,   180,  389,  0x0, 0,   6,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 20,  4.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -2.0,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 58,  1.350000023841858,     12.390000343322754,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.675000011920929,    -6.195000171661377,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 60,  206.02999877929688,    121.13999938964844,    -1.0,                  1.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  1.0,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -103.01499938964844,   -121.13999938964844,   0.20000000298023224,   1.0])

    DeclActor(14000,   0,       63800,   2000,    14000,   1000,    63800,   0x007C, 0,  11, 0x0000)
    DeclActor(164000,  0,       63800,   2000,    164000,  1000,    63800,   0x007C, 0,  12, 0x0000)
    DeclActor(164000,  0,       63800,   2000,    164000,  1000,    63800,   0x007C, 0,  13, 0x0000)
    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  15, 0x0000)
    DeclActor(180910,  0,       62020,   1500,    180910,  1500,    62020,   0x007C, 0,  61, 0x0000)
    DeclActor(19980,   0,       63920,   1500,    19980,   1500,    63920,   0x007C, 0,  61, 0x0000)
    DeclActor(175940,  0,       63930,   1500,    175940,  1500,    63930,   0x007C, 0,  61, 0x0000)
    DeclActor(-3150,   0,       122280,  1200,    -3150,   1000,    122280,  0x007C, 0,  71, 0x0000)
    DeclActor(-2300,   0,       129960,  1200,    -2300,   2000,    129960,  0x007C, 0,  72, 0x0000)
    DeclActor(155150,  30,      129699,  1200,    153340,  2029,    130490,  0x007C, 0,  73, 0x0000)
    DeclActor(155120,  30,      123880,  1200,    155120,  2029,    123880,  0x007C, 0,  74, 0x0000)
    DeclActor(207280,  30,      128039,  1200,    208840,  3000,    130410,  0x007C, 0,  75, 0x0000)
    DeclActor(209020,  0,       126830,  1200,    209210,  2000,    127040,  0x007C, 0,  76, 0x0000)
    DeclActor(51920,   0,       130570,  1200,    51920,   2500,    130570,  0x007C, 0,  77, 0x0000)
    DeclActor(52900,   0,       124470,  1200,    53700,   2000,    125270,  0x007C, 0,  78, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  80, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  81, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  82, 0x0000)
    DeclActor(48000,   30,      127860,  1200,    47560,   1500,    128630,  0x007C, 0,  83, 0x0000)
    DeclActor(170000,  0,       63800,   2000,    170000,  1000,    63800,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_844",          # 00, 0
        "Function_1_8FC",          # 01, 1
        "Function_2_CF7",          # 02, 2
        "Function_3_1149",         # 03, 3
        "Function_4_14E0",         # 04, 4
        "Function_5_15AC",         # 05, 5
        "Function_6_172C",         # 06, 6
        "Function_7_1A38",         # 07, 7
        "Function_8_1A9C",         # 08, 8
        "Function_9_1BF9",         # 09, 9
        "Function_10_1D80",        # 0A, 10
        "Function_11_1FFD",        # 0B, 11
        "Function_12_2001",        # 0C, 12
        "Function_13_2005",        # 0D, 13
        "Function_14_2009",        # 0E, 14
        "Function_15_200D",        # 0F, 15
        "Function_16_205F",        # 10, 16
        "Function_17_2A6C",        # 11, 17
        "Function_18_2E41",        # 12, 18
        "Function_19_3C41",        # 13, 19
        "Function_20_4B4D",        # 14, 20
        "Function_21_5CC4",        # 15, 21
        "Function_22_6458",        # 16, 22
        "Function_23_7646",        # 17, 23
        "Function_24_7BE2",        # 18, 24
        "Function_25_7E8D",        # 19, 25
        "Function_26_BCDA",        # 1A, 26
        "Function_27_C913",        # 1B, 27
        "Function_28_C9D8",        # 1C, 28
        "Function_29_CAE6",        # 1D, 29
        "Function_30_CB5F",        # 1E, 30
        "Function_31_CBD8",        # 1F, 31
        "Function_32_E5EB",        # 20, 32
        "Function_33_E640",        # 21, 33
        "Function_34_E695",        # 22, 34
        "Function_35_E6EA",        # 23, 35
        "Function_36_10EA0",       # 24, 36
        "Function_37_10EBF",       # 25, 37
        "Function_38_13A8B",       # 26, 38
        "Function_39_13BBA",       # 27, 39
        "Function_40_13CBC",       # 28, 40
        "Function_41_13DE5",       # 29, 41
        "Function_42_13E76",       # 2A, 42
        "Function_43_13EE9",       # 2B, 43
        "Function_44_13F7A",       # 2C, 44
        "Function_45_1401E",       # 2D, 45
        "Function_46_140C2",       # 2E, 46
        "Function_47_14796",       # 2F, 47
        "Function_48_147BC",       # 30, 48
        "Function_49_147EF",       # 31, 49
        "Function_50_14853",       # 32, 50
        "Function_51_148C4",       # 33, 51
        "Function_52_14919",       # 34, 52
        "Function_53_1496E",       # 35, 53
        "Function_54_149C3",       # 36, 54
        "Function_55_14A36",       # 37, 55
        "Function_56_14AA9",       # 38, 56
        "Function_57_14BE6",       # 39, 57
        "Function_58_14CB5",       # 3A, 58
        "Function_59_14DE7",       # 3B, 59
        "Function_60_14FB3",       # 3C, 60
        "Function_61_150D3",       # 3D, 61
        "Function_62_15191",       # 3E, 62
        "Function_63_1535E",       # 3F, 63
        "Function_64_1552B",       # 40, 64
        "Function_65_156FA",       # 41, 65
        "Function_66_158D4",       # 42, 66
        "Function_67_15AA5",       # 43, 67
        "Function_68_15C76",       # 44, 68
        "Function_69_15E43",       # 45, 69
        "Function_70_1601B",       # 46, 70
        "Function_71_16072",       # 47, 71
        "Function_72_1611D",       # 48, 72
        "Function_73_1625F",       # 49, 73
        "Function_74_16302",       # 4A, 74
        "Function_75_163AD",       # 4B, 75
        "Function_76_16454",       # 4C, 76
        "Function_77_164FD",       # 4D, 77
        "Function_78_165AC",       # 4E, 78
        "Function_79_16659",       # 4F, 79
        "Function_80_16692",       # 50, 80
        "Function_81_16737",       # 51, 81
        "Function_82_167DC",       # 52, 82
        "Function_83_16881",       # 53, 83
    ))


    def Function_0_844(): pass

    label("Function_0_844")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_884"),
        (1, "loc_890"),
        (2, "loc_89C"),
        (3, "loc_8A8"),
        (4, "loc_8B4"),
        (5, "loc_8C0"),
        (6, "loc_8CC"),
        (SWITCH_DEFAULT, "loc_8D8"),
    )


    label("loc_884")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_890")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_89C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8FB")

    Return()

    # Function_0_844 end

    def Function_1_8FC(): pass

    label("Function_1_8FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BE")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BE")
    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99A")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_9B9")

    label("loc_99A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B9")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_9B9")

    Jump("loc_9BE")

    label("loc_9BE")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B58")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A01")
    Event(0, 62)

    label("loc_A01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A32")
    Event(0, 63)

    label("loc_A32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A63")
    Event(0, 64)

    label("loc_A63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A94")
    Event(0, 65)

    label("loc_A94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC5")
    Event(0, 66)

    label("loc_AC5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF6")
    Event(0, 67)

    label("loc_AF6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B27")
    Event(0, 68)

    label("loc_B27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58")
    Event(0, 69)

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_B97")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 124140, 30, 8440, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 123070, 0, 8320, 45)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_BF9")

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_END)), "loc_BB9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_BF9")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_BDB")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_BF9")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_BF9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 0)

    label("loc_BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C26")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C41")
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_C5B")

    label("loc_C41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5B")
    Event(0, 31)

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_C6F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 16)
    Jump("loc_CF6")

    label("loc_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_C83")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 17)
    Jump("loc_CF6")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_C97")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 21)
    Jump("loc_CF6")

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_CAB")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 22)
    Jump("loc_CF6")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_CBF")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 23)
    Jump("loc_CF6")

    label("loc_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_CD3")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 25)
    Jump("loc_CF6")

    label("loc_CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_CE7")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 35)
    Jump("loc_CF6")

    label("loc_CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_CF6")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 37)

    label("loc_CF6")

    Return()

    # Function_1_8FC end

    def Function_2_CF7(): pass

    label("Function_2_CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D13")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D2A")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D2A")

    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9A")
    SetMapObjFrame(0xFF, "objects", 0x0, 0x1)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    Jump("loc_DB7")

    label("loc_D9A")

    SetMapObjFrame(0xFF, "box00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE3")
    SetMapObjFrame(0xFF, "objects2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "box01", 0x1, 0x1)
    Jump("loc_E00")

    label("loc_DE3")

    SetMapObjFrame(0xFF, "box01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "objects2", 0x1, 0x1)

    label("loc_E00")

    SetMapObjFrame(0xFF, "floor02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02_wood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02_sd", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02_dankon", 0x0, 0x1)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_E72")
    OP_66(0x3, 0x1)

    label("loc_E72")

    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9D")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x3, 0x10)

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB5")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECD")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_ECD")

    OP_65(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEA")
    OP_66(0x13, 0x1)
    ClearMapObjFlags(0x6, 0x10)

    label("loc_EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F01")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F15")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F59")
    SetBarrier(0x0, 0x0, 0x1, 0x0, -800, -1000, 128400, 8000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 1800, -1000, 122300, 5000, 5000, 90000)

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F80")
    SetBarrier(0x0, 0x2, 0x1, 0x0, 257500, -1000, 68700, 11000, 5000, 90000)

    label("loc_F80")

    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB0")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    OP_65(0x7, 0x1)

    label("loc_FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC8")
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_65(0x8, 0x1)

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")
    SetMapObjFrame(0xFF, "05", 0x0, 0x1)
    OP_65(0x9, 0x1)

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1003")
    SetMapObjFrame(0xFF, "06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x0, 0x1)
    OP_65(0xA, 0x1)

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101B")
    SetMapObjFrame(0xFF, "07", 0x0, 0x1)
    OP_65(0xB, 0x1)

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1033")
    SetMapObjFrame(0xFF, "08", 0x0, 0x1)
    OP_65(0xC, 0x1)

    label("loc_1033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104B")
    SetMapObjFrame(0xFF, "03", 0x0, 0x1)
    OP_65(0xD, 0x1)

    label("loc_104B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106E")
    SetMapObjFrame(0xFF, "04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x0, 0x1)
    OP_65(0xE, 0x1)

    label("loc_106E")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1086")
    OP_1B(0x0, 0x0, 0x38)

    label("loc_1086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1099")
    OP_1B(0x0, 0x0, 0x38)

    label("loc_1099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AC")
    OP_1B(0x0, 0x0, 0x38)

    label("loc_10AC")

    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C4")
    OP_1B(0x8, 0x0, 0x39)

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D7")
    OP_1B(0x8, 0x0, 0x39)

    label("loc_10D7")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EF")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_10EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1102")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_111A")
    SetMapObjFlags(0x7, 0x10)
    OP_65(0x4, 0x1)
    Jump("loc_1124")

    label("loc_111A")

    ClearMapObjFlags(0x7, 0x10)
    OP_66(0x4, 0x1)

    label("loc_1124")

    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    OP_65(0xF, 0x1)
    OP_65(0x10, 0x1)
    OP_65(0x11, 0x1)
    OP_65(0x12, 0x1)
    Return()

    # Function_2_CF7 end

    def Function_3_1149(): pass

    label("Function_3_1149")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11DD")
    Jump("loc_1227")

    label("loc_11DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11FD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1227")

    label("loc_11FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_121D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1227")

    label("loc_121D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1227")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1391")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#0305F……なんだロイドか。\x01",
            "こんな時間に出掛けんのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0012Fはは、そういう\x01",
            "訳じゃないんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "#0303F……お嬢のことか。\x02\x03",

            "#0300Fま、色々と事情が\x01",
            "ありそうだったよな。\x02\x03",

            "俺たちが立ち入っていいのかは\x01",
            "分かんねえが。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0008Fそうなんだよな……\x01",
            "（悩みごとなら\x01",
            "  話して欲しいけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_13FF")

    label("loc_1391")


    #C0005
    ChrTalk(
        0xFE,
        (
            "#0306Fお嬢の冴えない顔なんざ\x01",
            "見たくねえもんだな。\x02\x03",

            "#0308F俺たちが立ち入っていいのか\x01",
            "分かんねえけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FF")

    Jump("loc_14D8")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_14D8")

    #C0006
    ChrTalk(
        0xFE,
        (
            "#0303Fま、お前が迷うのも\x01",
            "分からんでもないさ。\x02\x03",

            "#0300F一晩じっくり考えてみるのが\x01",
            "いいんじゃねえか？\x02\x03",

            "#0309F正式にお仲間になった暁には\x01",
            "一緒に遊びに繰り出すとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0002Fはは、考えておくよ。\x02",
    )

    CloseMessageWindow()

    label("loc_14D8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_1149 end

    def Function_4_14E0(): pass

    label("Function_4_14E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_15A8")

    #C0008
    ChrTalk(
        0xFE,
        (
            "#0106F今日は初日だったし、\x01",
            "色々あったわよね。\x02\x03",

            "#0100F私も少し疲れちゃった。\x01",
            "日記をつけたら\x01",
            "早めに休ませてもらおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A8")

    #C0009
    ChrTalk(
        0x101,
        (
            "#0002Fはは、そうだな。\x02\x03",

            "おやすみ、エリィ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_15A8")

    TalkEnd(0xFE)
    Return()

    # Function_4_14E0 end

    def Function_5_15AC(): pass

    label("Function_5_15AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_167A")

    #C0010
    ChrTalk(
        0xFE,
        (
            "#0202Fすみません、すぐに支度するので\x01",
            "もう少し待っていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0002Fああ……\x01",
            "ティオ、急がなくてもいいよ。\x01",
            "後で俺たちも手伝うからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "#0204F……はい、宜しくお願いします。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_167A")


    #C0013
    ChrTalk(
        0xFE,
        (
            "#0200Fロイドさんですか。\x01",
            "まだ何か……？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#0002Fいや、なんでもないんだ。\x01",
            "悪いな邪魔しちゃって。\x02\x03",

            "おやすみ。\x01",
            "ゆっくり休んでくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "#0204Fはい。\x01",
            "おやすみなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1728")

    TalkEnd(0xFE)
    Return()

    # Function_5_15AC end

    def Function_6_172C(): pass

    label("Function_6_172C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17C0")
    Jump("loc_180A")

    label("loc_17C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180A")

    label("loc_17E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1800")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180A")

    label("loc_1800")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198F")

    #C0016
    ChrTalk(
        0x101,
        (
            "#0002Fあ……ティオは\x01",
            "読書中だったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "#0203F読みかけの\x01",
            "専門誌があったもので。\x02\x03",

            "#0208F……あの、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F判ってる……\x01",
            "エリィのことだよな？\x02\x03",

            "#0000F少し、俺の方から\x01",
            "話をしてみようと思ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "#0202F……そうですか。\x01",
            "では、ロイドさんにお任せします。\x02\x03",

            "#0206F私はあまりそういうのは\x01",
            "得意ではないので……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_1A30")

    label("loc_198F")


    #C0020
    ChrTalk(
        0xFE,
        (
            "#0202Fエリィさんのことは\x01",
            "ロイドさんにお任せします。\x02\x03",

            "#0206Fこういうことは本当なら\x01",
            "同性の私の方がいいのかも\x01",
            "知れないですが……\x02\x03",

            "なにぶん、苦手分野ですから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A30")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_172C end

    def Function_7_1A38(): pass

    label("Function_7_1A38")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "#1109Fおてつだいー、おてつだいー♪\x02\x03",

            "#1110Fロイドー、晩ゴハンは\x01",
            "もうちょっと待ってねー！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1A38 end

    def Function_8_1A9C(): pass

    label("Function_8_1A9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B33")

    #C0022
    ChrTalk(
        0xFE,
        "#1203Fグルルルル……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0300F（俺たちの事は\x01",
            "  お構いなしで寝てんな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0012F（まあ、いつもの事だけど。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_1B4D")

    label("loc_1B33")


    #C0025
    ChrTalk(
        0xFE,
        "#1203Fグルルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_1B4D")

    Jump("loc_1BF5")

    label("loc_1B52")


    #C0026
    ChrTalk(
        0xFE,
        "#1203Fグルルルル…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA9")

    #C0027
    ChrTalk(
        0x101,
        "#0002F（はは、寛いでるみたいだな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_1BA9")


    #C0028
    ChrTalk(
        0x101,
        (
            "#0008F（ツァイトは……\x01",
            "  エリィがどこにいるかなんて\x01",
            "  知らないよな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF5")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A9C end

    def Function_9_1BF9(): pass

    label("Function_9_1BF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDC")

    #C0029
    ChrTalk(
        0xFE,
        (
            "#1002Fクク、どうした？\x02\x03",

            "#1003F──繰り返すが、支援課#6Rウ　チ#への\x01",
            "配属を辞退することは可能だ。\x02\x03",

            "お前は捜査官資格を持ってるから\x01",
            "捜査課のどこかに配属になるだろう。\x02\x03",

            "#1000F一晩ゆっくり考えてみるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1D7C")

    label("loc_1CDC")


    #C0030
    ChrTalk(
        0xFE,
        (
            "#1003F特務支援課への\x01",
            "配属を辞退することは可能だ。\x02\x03",

            "お前は捜査官資格を持ってるから\x01",
            "捜査課のどこかに配属になるだろう。\x02\x03",

            "#1000F一晩ゆっくり考えてみるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1BF9 end

    def Function_10_1D80(): pass

    label("Function_10_1D80")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E14")
    Jump("loc_1E5E")

    label("loc_1E14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E34")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E5E")

    label("loc_1E34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E54")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E5E")

    label("loc_1E54")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E5E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA7")

    #C0031
    ChrTalk(
        0xFE,
        (
            "#1005F何だお前か。\x01",
            "そんな冴えねえツラ\x01",
            "出すんじゃねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0012Fはは、すみません……\x01",
            "課長はお仕事ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "#1006Fこんな部署でも\x01",
            "書類仕事は回ってきてな。\x02\x03",

            "#1000F用が無いならさっさと下がれ。\x01",
            "俺も早いこと\x01",
            "片付けちまいたいんでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#0000Fはい、お邪魔しました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1FF5")

    label("loc_1FA7")


    #C0035
    ChrTalk(
        0xFE,
        (
            "#1000F用が無いならさっさと下がれ。\x01",
            "俺も早いこと\x01",
            "片付けちまいたいんでな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_1D80 end

    def Function_11_1FFD(): pass

    label("Function_11_1FFD")

    Call(0, 18)
    Return()

    # Function_11_1FFD end

    def Function_12_2001(): pass

    label("Function_12_2001")

    Call(0, 19)
    Return()

    # Function_12_2001 end

    def Function_13_2005(): pass

    label("Function_13_2005")

    Call(0, 24)
    Return()

    # Function_13_2005 end

    def Function_14_2009(): pass

    label("Function_14_2009")

    Call(0, 59)
    Return()

    # Function_14_2009 end

    def Function_15_200D(): pass

    label("Function_15_200D")

    TalkBegin(0xFF)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "端末の導力は落ちている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0037
    ChrTalk(
        0x101,
        "#0000F……今は使う必要はないな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_15_200D end

    def Function_16_205F(): pass

    label("Function_16_205F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x11, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0038
    AnonymousTalk(
        0x101,
        (
            "#0011F市民の安全を第一に考え、\x01",
            "様々な要望に応える部署……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0039
    ChrTalk(
        0x11,
        (
            "#1P#1003Fそう、それが新たに設立された\x01",
            "『特務支援課』の行動方針だ。\x02\x03",

            "市民の生活に密着できるよう、\x01",
            "こんな街中に分室も用意された。\x02\x03",

            "#1002Fクク、なかなか合理的だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#12P#0011Fで、でもそれって……！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0106F完全に遊撃士協会#10Rブレイサーギルド#の\x01",
            "真似っていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#4P#0211Fありていに言えば、パクリですね。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#0306Fだよなぁ。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x11,
        (
            "#1P#1000F知っているかもしれんが、\x01",
            "現在、このクロスベルにおいて\x01",
            "遊撃士協会の評判は大したもんだ。\x02\x03",

            "#1003FＡ級遊撃士アリオス・マクレイン──\x02\x03",

            "《風の剣聖》なんて呼ばれている\x01",
            "あの男に加えて、かなりの実力者が\x01",
            "クロスベル支部に常駐している。\x02\x03",

            "#1000Fそれが警察のお偉方にとって\x01",
            "何を意味するか判るか？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#12P#0005Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0103F警察とギルドとの比較評価と\x01",
            "組織としての問題点の指摘……\x02\x03",

            "#0108F更には自治州政府への\x01",
            "批判に繋がっているんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0304Fなるほど、そういう事か。\x02\x03",

            "#0300F要はギルドのお株を何とか奪って\x01",
            "人気取りをしようって肚#2Rハラ#なわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#4P#0206F……なんか露骨ですね。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x11,
        (
            "#1P#1004Fま、ぶっちゃけて言うと\x01",
            "お前らの指摘する通りだ。\x02\x03",

            "#1001Fだが、警察の基本理念は\x01",
            "治安維持と自治州法の遵守……\x02\x03",

            "市民へのサービスってのは\x01",
            "本来、二の次ではあるわけだ。\x02\x03",

            "#1003Fだからこそ、警察内部では\x01",
            "そうした人気取りを\x01",
            "快く思わない声も多くてな。\x02\x03",

            "『便利屋』だの『ニセ遊撃士』だの\x01",
            "『猿回しのサル』だの……\x02\x03",

            "#1002Fまあ、早くも散々な\x01",
            "陰口を叩かれてるってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#12P#0011F……………………（パクパク）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#0106Fなるほど……\x01",
            "色々と合点がいきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#0301Fやれやれ、そんな部署で\x01",
            "俺たちを働かせようってか？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#4P#0211F……正直、想定外ですね。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x11,
        (
            "#1P#1004Fまあまあ、そう急くな。\x02\x03",

            "#1002F──聞いているかもしれんが\x01",
            "配属を辞退することは可能だ。\x02",
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

    #C0055
    ChrTalk(
        0x101,
        "#12P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x11,
        (
            "#1P#1003F正式に配属された場合、\x01",
            "やってもらう仕事は様々だ。\x02\x03",

            "今日みたいな、魔獣退治の\x01",
            "仕事なんかも入ってくるし……\x02\x03",

            "落とし物探しや、本部の手伝いなど\x01",
            "細かい雑用も入ってくるだろう。\x02\x03",

            "#1001F──その気がない人間に\x01",
            "勤まるとはとても思えんからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(300)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0057
    AnonymousTalk(
        0x11,
        (
            "#1003F一晩、考える時間をやろう。\x02\x03",

            "配属を辞退した場合、\x01",
            "他の部署に配属される事になるが\x01",
            "今ならデメリットは無い。\x02\x03",

            "#1000F全てはお前たち次第というわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CA(0x1, 0xFF, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Sleep(1000)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x47, 5)
    SetScenarioFlags(0x5C, 1)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_205F end

    def Function_17_2A6C(): pass

    label("Function_17_2A6C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50000.itc", 0x1E)
    OP_68(1900, 1100, 123500, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrPos(0x101, 1900, 300, 125500, 270)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_68(1900, 1100, 125500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0058
    ChrTalk(
        0x101,
        "#0008F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    #A0059
    AnonymousTalk(
        0x101,
        (
            "#0006F……何だかとんでもない場所に\x01",
            "回されたみたいだな……\x02\x03",

            "#0008F遊撃士の真似事か……\x02\x03",

            "そんな事をするために\x01",
            "警察に入ったんじゃないんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0003F#11P……兄貴が所属してたのは\x01",
            "たしか『捜査一課』だったよな。\x02\x03",

            "大事件や政治的・国際的な案件を\x01",
            "一手に引き受けるエリート集団……\x02\x03",

            "#0008F……やっぱり遠すぎるよな……\x02\x03",

            "…………………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(1550, 1100, 125710, 500)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 1000, 30, 125500, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0061
    ChrTalk(
        0x101,
        (
            "#5P#0001F……他のみんなは\x01",
            "どうするつもりなんだろう？\x02\x03",

            "あの３人……\x01",
            "警察学校も出てないみたいだし、\x01",
            "色々訳アリみたいだったけど……\x02\x03",

            "#0000Fちょっと話を聞いてみるか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 900, 0, 125500, 180)
    SetScenarioFlags(0x41, 1)
    OP_29(0x3C, 0x1, 0x4)
    OP_29(0x3C, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_17_2A6C end

    def Function_18_2E41(): pass

    label("Function_18_2E41")

    EventBegin(0x0)
    Fade(1000)
    OP_68(13700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 13700, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F03")

    #C0062
    ChrTalk(
        0x101,
        (
            "#12P#0005Fここは……\x01",
            "ランディの部屋だったな。\x02\x03",

            "#0001Fさっきまで物を動かすような\x01",
            "音が聞こえてきたけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2F03")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ノックする】\x01",        # 0
            "【ノックしない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F5D"),
        (1, "loc_3C39"),
        (SWITCH_DEFAULT, "loc_3C40"),
    )


    label("loc_2F5D")

    OP_95(0x101, 13700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0x8, 13700, 0, 66000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)

    #N0063
    NpcTalk(
        0x8,
        "ランディの声",
        "#5P#2S……ん、誰だ？\x07\x00\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#12P#0000Fロイドだけど、\x01",
            "ちょっといいかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0065
    NpcTalk(
        0x8,
        "ランディの声",
        (
            "#5P#2Sおお、いいぞ。\x01",
            "遠慮なく入って来いよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#12P#0000Fそれじゃ、お邪魔するよ。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)

    def lambda_3071():
        OP_95(0xFE, 13700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3071)
    Sleep(300)

    def lambda_308E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_308E)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_68(51500, 600, 130000, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0xA)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 51840, 150, 126400, 270)
    SetChrPos(0x101, 50000, 0, 121100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    OP_68(51500, 600, 125000, 5000)
    MoveCamera(55, 14, 0, 5000)
    SetCameraDistance(25500, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0067
    ChrTalk(
        0x101,
        "#0005Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(51000, 1000, 124200, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_31DB():
        OP_95(0xFE, 51000, 0, 123200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31DB)
    OP_0D()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    SetChrPos(0x8, 51000, 0, 126400, 270)
    OP_0D()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_3225():
        OP_95(0xFE, 51000, 0, 125100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3225)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x8, 500)
    WaitChrThread(0x8, 1)
    Sound(1364, 255, 100, 0)    #voice#Randy
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0068
    AnonymousTalk(
        0x8,
        (
            "ようこそ、俺様の城へ。\x02\x03",

            "お前さんの方も\x01",
            "荷ほどきは終わったのか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3367")

    #C0069
    ChrTalk(
        0x101,
        (
            "#12P#0006Fい、いや……まだだけど。\x02\x03",

            "#0000F──どうやらランディは\x01",
            "もう結論が出てるみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CA")

    label("loc_3367")


    #C0070
    ChrTalk(
        0x101,
        (
            "#12P#0006Fい、いや……まだだけど。\x02\x03",

            "#0000F──どうやらランディも\x01",
            "もう結論が出てるみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33CA")


    #C0071
    ChrTalk(
        0x8,
        (
            "#5P#0305Fああ、配属を辞退するって話か。\x02\x03",

            "#0304Fま、デスクワークは少なそうだし、\x01",
            "気楽そうなのも性に合っている。\x02\x03",

            "#0300F職場と住む場所が一緒なのも\x01",
            "ラクで良さそうだし、\x01",
            "このまま厄介になるつもりだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#12P#0003Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "#5P#0300Fお前の方は\x01",
            "さすがに迷ってるみたいだな？\x02\x03",

            "せっかく取った捜査官の資格を\x01",
            "無駄にしたくないってところか。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#0004Fはは……それもあるけどね。\x02\x03",

            "#0008Fそれ以上に、目指している目標から\x01",
            "遠ざかっていきそうな気がして……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "#5P#0305F目指している目標……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#0012Fいや、まあ……\x01",
            "大したことじゃないんだ。\x02\x03",

            "#0000Fそういえば……\x01",
            "ランディはどういう経緯で\x01",
            "ここに配属されたんだ？\x02\x03",

            "俺たちより年上だけど……\x01",
            "警察学校は出てないんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#5P#0305Fああ、その通りだが。\x02\x03",

            "#0303Fうーん、俺がここに\x01",
            "配属された経緯ねぇ……\x02\x03",

            "#0301F──本当に聞きたい？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ、ああ。\x01",
            "差し支えなければだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "#5P#0303Fそこまで言うなら仕方ねぇ。\x02\x03",

            "#0302F実はな──女絡みのトラブルだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#12P#0011Fへっ……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5P#0309Fいや～、前の職場で\x01",
            "複数手を出したのがバレてさ。\x02\x03",

            "あやうくクビになりかけた所を\x01",
            "オッサンに拾ってもらったんだよ。\x02\x03",

            "これも空の女神#8Rエ イ ド ス#の\x01",
            "お導きってところかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#0011Fえっと……\x01",
            "ランディの前の職場って？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#5P#0300Fああ、クロスベル警備隊さ。\x02\x03",

            "帝国方面に\x01",
            "ベルガード門ってあるだろ？\x01",
            "あっちの方に詰めていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#0000F警備隊……そういう事か。\x02\x03",

            "道理であんなハルバードを\x01",
            "自由自在に振り回せるわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "#5P#0306Fま、国境付近の詰所あたりじゃ\x01",
            "訓練とパトロールくらいしか\x01",
            "やることが無かったからなぁ。\x02\x03",

            "#0300Fその点、クロスベル市勤務なら\x01",
            "歓楽街とかにも行きたい放題だ。\x02\x03",

            "#0309Fいや～、マジで\x01",
            "警備隊を辞めて正解だったぜ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#12P#0012Fはは……\x01",
            "まあ、気持ちは分かるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "#5P#0305Fおっと、気が合うじゃない。\x02\x03",

            "#0302F……いやさ、実は何軒か\x01",
            "色っぽい姉ちゃんたちがいる店を\x01",
            "見つけているんだよ。\x02\x03",

            "正式にお仲間になったら\x01",
            "一緒に遊びに繰り出そうぜ？\x02\x03",

            "#0309Fお嬢は固そうだし、\x01",
            "お子様もお呼びじゃないし、\x01",
            "男同士の付き合いってやつだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#12P#0002Fはは……\x01",
            "わかった、考えておくよ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x3, 0x10)
    SetChrPos(0x0, 50250, 0, 122560, 180)
    OP_68(50250, 1300, 122560, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0x41, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C2F")
    ModifyEventFlags(1, 0, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_3C2F")

    Sleep(500)
    EventEnd(0x5)
    Jump("loc_3C40")

    label("loc_3C39")

    EventEnd(0x5)
    Jump("loc_3C40")

    label("loc_3C40")

    Return()

    # Function_18_2E41 end

    def Function_19_3C41(): pass

    label("Function_19_3C41")

    EventBegin(0x0)
    Fade(1000)
    OP_68(163700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 163700, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEC")

    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#0005Fここは……\x01",
            "確かエリィの部屋だったな。\x02\x03",

            "#0001Fもう寝てないといいけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3CEC")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ノックする】\x01",        # 0
            "【ノックしない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D46"),
        (1, "loc_4B45"),
        (SWITCH_DEFAULT, "loc_4B4C"),
    )


    label("loc_3D46")

    OP_95(0x101, 163700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0xA, 163700, 0, 66000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    #N0090
    NpcTalk(
        0xA,
        "エリィの声",
        "#5P#2S……どなたですか？\x07\x00\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0000Fえっと……ロイドだけど。\x02\x03",

            "今、ちょっといいかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0092
    NpcTalk(
        0xA,
        "エリィの声",
        "#5P#2Sあ、うん、別にいいわよ。\x07\x00\x02",
    )

    CloseMessageWindow()

    #N0093
    NpcTalk(
        0xA,
        "エリィの声",
        "#5P#2S鍵は開いてるから入ってきて。\x07\x00\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#12P#0000Fそれじゃ……お邪魔します。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x5)

    def lambda_3E93():
        OP_95(0xFE, 163700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E93)
    Sleep(300)

    def lambda_3EB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EB0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_68(157300, 600, 130000, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x8)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 157800, 0, 126700, 45)
    SetChrPos(0x101, 155800, 0, 120800, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00100.itp")
    OP_68(157300, 600, 125000, 5000)
    MoveCamera(55, 14, 0, 5000)
    SetCameraDistance(25500, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0095
    ChrTalk(
        0x101,
        "#0005F………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(157800, 1000, 123900, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_3FF7():
        OP_95(0xFE, 157800, 0, 122900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FF7)
    Sleep(200)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(100)

    def lambda_401E():
        OP_95(0xFE, 157800, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_401E)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)
    WaitChrThread(0xA, 1)
    #Sound(1174, 255, 90, 0)    #voice#Elie
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0096
    AnonymousTalk(
        0xA,
        (
            "ふふっ……\x01",
            "何とか片付けが終わって良かったわ。\x02\x03",

            "そこに座ってくれる？\x01",
            "今、紅茶でも淹#2Rい#れるから。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4185")

    #C0097
    ChrTalk(
        0x101,
        (
            "#12P#0004Fいや、お構いなく。\x02\x03",

            "#0001Fでも、この部屋の様子を見ると\x01",
            "もう結論は出ているみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E0")

    label("loc_4185")


    #C0098
    ChrTalk(
        0x101,
        (
            "#12P#0004Fいや、お構いなく。\x02\x03",

            "#0001Fしかしエリィも……\x01",
            "もう結論は出ているみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E0")


    #C0099
    ChrTalk(
        0xA,
        (
            "#5P#0105Fああ、配属を辞退する話ね。\x02\x03",

            "#0104F少し迷ったんだけど……\x01",
            "ここで頑張ることに決めたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#12P#0000Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "#5P#0100F……あなたの方は\x01",
            "さすがに迷っているみたいね。\x02\x03",

            "#0106Fでも、無理もないと思うわ。\x02\x03",

            "#0108Fこの特務支援課だけど……\x01",
            "正直、無理がありすぎるもの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x101,
        "#12P#0005F無理がある？\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#5P#0101F話を聞く限り、色んなしがらみや\x01",
            "打算によって出来た部署でしょう？\x02\x03",

            "組織としての合理性に欠けるし、\x01",
            "目的も今一つはっきりしていない。\x02\x03",

            "#0103Fこれで成果が上がらなければ\x01",
            "予算の都合で、本当に無くなる\x01",
            "可能性が高いんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#12P#0006F……まあ、\x01",
            "普通に考えればそうだよな。\x02\x03",

            "#0001Fでも、そこまで判って\x01",
            "どうしてエリィは残るんだ？\x02\x03",

            "何か理由でもあるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#5P#0100Fそうね……\x02\x03",

            "#0104F……色々な歪みを観察するには\x01",
            "割と良さそうな場所だから、かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#12P#0005Fへっ……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#5P#0109Fふふっ、なんちゃって。\x02\x03",

            "#0100F多分私は、ずっと警察に\x01",
            "勤め続けることはないと思うの。\x02\x03",

            "そういう意味では、\x01",
            "ここが出世コースから外れても\x01",
            "あんまり関係がないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそうなのか……\x02\x03",

            "#0000F確かエリィは、警察学校には\x01",
            "行ってなかったんだよな？\x02\x03",

            "どういう経緯で警察に？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "#5P#0101Fうーん……\x01",
            "ありていに言うと社会勉強ね。\x02\x03",

            "#0103Fちなみに入る時の試験は\x01",
            "筆記と射撃だったんだけど……\x02\x03",

            "#0102Fどちらも満点だったから\x01",
            "断りきれなかったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0110
    ChrTalk(
        0x101,
        (
            "#12P#0012Fな、なんか聞けば聞くほど\x01",
            "俺の場合とは違うような……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "#5P#0100Fあら、あなただって\x01",
            "新人で捜査官資格を取ったのは\x01",
            "珍しいんじゃないかしら？\x02\x03",

            "やっぱり事情があるんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#12P#0005F……それは………\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "#5P#0104Fふふっ……\x02\x03",

            "#0102Fここから先は、正式な同僚に\x01",
            "なってからの方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#12P#0002Fああ……そうだな。\x02\x03",

            "#0004F悪い、気を遣わせたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "#5P#0104Fいえいえ。\x02\x03",

            "#0102Fでも、私個人の意見で言えば\x01",
            "あなたが居てくれた方が嬉しいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#12P#0005Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "#5P#0106Fまあ、お互い新米だから\x01",
            "まだまだな所もあったけど……\x02\x03",

            "#0102F今日だって、慣れない状況でも\x01",
            "リーダーとして頑張ってくれたし。\x02\x03",

            "指示も的確だったから、\x01",
            "私も安心してサポートできたもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#0012Fはは……\x01",
            "そう言ってくれると助かるよ。\x02\x03",

            "#0004F──ありがとう。\x01",
            "話に付き合ってくれて。\x02\x03",

            "#0000Fあとは自分なりに考えてみる。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "#5P#0104Fうん……そうね。\x02\x03",

            "#0102Fおやすみなさい、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#12P#0002Fおやすみ、エリィ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x1, 0x1)
    SetMapObjFlags(0x5, 0x10)
    SetChrPos(0x0, 156610, 30, 121830, 180)
    OP_68(156610, 1330, 121830, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x40)
    SetChrPos(0xA, 157420, 0, 128650, 0)
    SetScenarioFlags(0x41, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B3B")
    ModifyEventFlags(1, 0, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_4B3B")

    Sleep(500)
    EventEnd(0x5)
    Jump("loc_4B4C")

    label("loc_4B45")

    EventEnd(0x5)
    Jump("loc_4B4C")

    label("loc_4B4C")

    Return()

    # Function_19_3C41 end

    def Function_20_4B4D(): pass

    label("Function_20_4B4D")

    EventBegin(0x0)
    Fade(1000)
    OP_68(4000, 1850, 10300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 4000, 850, 10300, 90)
    SetChrPos(0xB, 16100, 850, 10200, 45)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(15000, 1850, 10300, 3000)
    SetCameraDistance(25500, 3000)
    Sleep(1000)

    def lambda_4C1B():
        OP_96(0xFE, 0x42CC, 0x352, 0x23F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4C1B)
    WaitChrThread(0xB, 1)
    Sleep(1000)

    def lambda_4C3C():
        OP_96(0xFE, 0x3EE4, 0x352, 0x27D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4C3C)
    OP_6F(0x1)
    OP_6F(0x10)

    #C0121
    ChrTalk(
        0x101,
        (
            "#0005Fティオ……\x01",
            "何やってるんだ？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(11900, 1850, 10200, 0)
    MoveCamera(50, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 8000, 1000, 10300, 90)
    OP_68(13900, 1850, 10200, 2000)

    def lambda_4CEF():
        OP_97(0x101, 0x12C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CEF)
    Sleep(500)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)

    def lambda_4D16():
        OP_95(0xFE, 15000, 850, 10200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4D16)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Sound(1267, 255, 90, 0)    #voice#Tio
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0122
    AnonymousTalk(
        0xB,
        (
            "……ロイドさん。\x02\x03",

            "見ての通り、\x01",
            "端末のチェックをしていました。\x02",
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

    #C0123
    ChrTalk(
        0x101,
        "#6P#0005F端末って……それのことか？\x02",
    )

    CloseMessageWindow()
    OP_68(16500, 1750, 10300, 1500)
    MoveCamera(35, 16, 0, 1500)
    SetCameraDistance(22000, 1500)

    def lambda_4E35():
        OP_95(0x101, 13300, 850, 9800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E35)
    Sleep(300)
    OP_93(0xB, 0x5A, 0x1F4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    #C0124
    ChrTalk(
        0xB,
        (
            "#0200F#5PＺＣＦのカペルシステムを\x01",
            "財団で改良した汎用端末です。\x02\x03",

            "警察本部から、\x01",
            "導力ネットワークを通じて\x01",
            "情報を受け取ることが可能です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0125
    ChrTalk(
        0x101,
        (
            "#6P#0011Fへ……？\x02\x03",

            "ちょ、ちょっと待て。\x01",
            "いきなり訳が分かんないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "#0203F#5P……そうですね。\x02\x03",

            "#0200Fロイドさんは、\x01",
            "『導力ネットワーク計画』について\x01",
            "どこまでご存知ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#0005F『導力ネットワーク』……\x02\x03",

            "#0006F雑誌の記事でたまに見るけど\x01",
            "ちゃんと理解はしていないな。\x02\x03",

            "#0001F確かエプスタイン財団が\x01",
            "提唱してるとか何とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#0200F#5P元は、エプスタイン財団と\x01",
            "ツァイス中央工房#16RＺ    Ｃ    Ｆ#が共同して\x01",
            "スタートさせたプロジェクトです。\x02\x03",

            "今では、主に財団によって\x01",
            "進められていますが……\x02\x03",

            "その大規模な試験運用が\x01",
            "現在、このクロスベル市で\x01",
            "進められているんです。\x02\x03",

            "まあ、これもその一環ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#6P#0005Fよ、よく分からないけど……\x02\x03",

            "#0012F結局のところ、\x01",
            "どういう事をする計画なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        "#0203F#5Pふう……\x02",
    )

    CloseMessageWindow()
    OP_68(15180, 1750, 10680, 1200)
    TurnDirection(0xB, 0x101, 500)
    Sleep(300)
    OP_6F(0x1)

    #C0131
    ChrTalk(
        0xB,
        (
            "#11P#0200F要するに、旧来の通信器を\x01",
            "発展させた技術ということです。\x02\x03",

            "単に会話のやり取りをするだけでなく\x01",
            "演算能力を持った端末同士を結んで\x01",
            "効率的な情報ネットワークを構築する。\x02\x03",

            "判りやすく言うとそんな所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#0006F全然判りやすくないんだが……\x02\x03",

            "#0001Fえっと、要するに\x01",
            "警察内部の連絡や指揮系統を\x01",
            "効率化する装置ってところか？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "#11P#0204F……まあ、この端末については\x01",
            "間違いではないです。\x02\x03",

            "#0202Fわたしの専門ではありませんが\x01",
            "端末の操作くらいはできますし。\x02\x03",

            "今後のことを考えると\x01",
            "一応、チェックしておこうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#6P#0005Fそ、そうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#0000Fその様子だと、ティオは\x01",
            "配属を辞退するなんて\x01",
            "考えてもいないみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        "#0205F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや、そもそも……\x01",
            "俺がティオくらいの歳は\x01",
            "まだ遊びたい盛りだったよな。\x02\x03",

            "#0000F財団から出向したって話だけど、\x01",
            "その、無理矢理働かされてるとか\x01",
            "そういうわけじゃないんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        "#0205F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#0011Fえ……！？\x01",
            "まさか、本当にそうなのか！？\x02\x03",

            "#0013Fどんな事情があっても\x01",
            "そんなの我慢したら駄目だぞ！？\x02\x03",

            "その、俺でよかったら\x01",
            "いくらでも力を貸すから──\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "#0206F#11Pあの、落ち着いてください。\x02\x03",

            "#0208F……別に強制されて\x01",
            "働いているんじゃありません。\x02\x03",

            "#0202Fそれどころか……\x01",
            "今回の出向は、むしろわたしが\x01",
            "我侭を言わせてもらった結果です。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "#0204F#11Pわたしはわたしで\x01",
            "ここに居る理由がある……\x02\x03",

            "つまりはそういう事です。\x02\x03",

            "#0211Fロイドさんは人の心配をする前に\x01",
            "自分の心配をするべきでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ、ああ……\x02\x03",

            "#0006Fはは、そうだな。\x01",
            "ティオの言うとおりだった。\x02\x03",

            "#0000Fごめんな。\x01",
            "差し出がましいことを言って。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "#0203F#11Pいえ……\x02\x03",

            "#0202Fただ、あんまりお人好しなのは\x01",
            "捜査官としてはどうかと。\x02\x03",

            "遊撃士と違って、人を疑うことも\x01",
            "しなくてはいけない仕事ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#6P#0011Fうぐっ……\x01",
            "痛いところを突いてくるなぁ。\x02\x03",

            "#0006Fうーん、やっぱり俺って\x01",
            "まだまだ甘ちゃんなのかな……\x02\x03",

            "警察学校の訓練で徹底的に\x01",
            "自分を鍛えたつもりだったけど……\x02\x03",

            "#0008Fでも、確かにそれだけじゃ\x01",
            "捜査官は務まらないだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        "#0202F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x101,
        "#6P#0005Fティオ……？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "#0203F#11P……端末のチェックは\x01",
            "一通り終わりました。\x02\x03",

            "#0200F明日、導力ケーブルの\x01",
            "接続工事があるようなので\x01",
            "今日は早めに休みます。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそうか……\x02\x03",

            "#0002Fおやすみ。\x01",
            "ゆっくり休んでくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "#0204F#11Pはい。\x01",
            "それでは──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1270, 255, 90, 0)    #voice#Tio
    Sleep(300)

    def lambda_5AD4():

        label("loc_5AD4")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_5AD4")

    QueueWorkItem2(0x101, 2, lambda_5AD4)

    def lambda_5AE6():
        OP_95(0xFE, 13300, 850, 11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5AE6)
    WaitChrThread(0xB, 1)
    OP_68(13300, 1850, 9800, 2000)

    def lambda_5B15():
        OP_97(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5B15)
    WaitChrThread(0xB, 1)
    EndChrThread(0x101, 0x2)
    SetChrFlags(0xB, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0151
    ChrTalk(
        0x101,
        (
            "#11P#0003F……３人ともちゃんと\x01",
            "自分のやるべき事を\x01",
            "考えているみたいだな。\x02\x03",

            "#0008F迷っているのは俺だけか……\x02\x03",

            "………………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0152
    ChrTalk(
        0x101,
        (
            "#11P#0006F……だめだ。\x01",
            "なんだか煮詰まってきた。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    #C0153
    ChrTalk(
        0x101,
        "#5P#0000F少し外に出て風に当たるか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_CA(0x1, 0xFF, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 9620, 850, 10260, 270)
    OP_68(9620, 1850, 10260, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetScenarioFlags(0x41, 4)
    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x1)
    Return()

    # Function_20_4B4D end

    def Function_21_5CC4(): pass

    label("Function_21_5CC4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(821)
    OP_68(800, 850, 1550, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 800, 40, 50, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x1F, 0x1000)
    OP_70(0x1F, 0x0)
    OP_74(0x1F, 0x1E)
    OP_71(0x1F, 0x0, 0x14, 0x0, 0x20)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_5D7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D7E)

    def lambda_5D8F():
        OP_95(0xFE, 800, 40, 1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D8F)
    WaitChrThread(0x101, 1)
    Sleep(300)
    Sound(821, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x2D, 0x1F4)

    #C0154
    ChrTalk(
        0x101,
        "#6P#0005F通信器のベル……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    def lambda_5E00():
        OP_95(0xFE, 1800, 850, 10000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E00)
    Sleep(800)
    OP_68(13800, 1850, 12000, 4000)
    SetCameraDistance(23000, 4000)
    WaitChrThread(0x101, 1)

    def lambda_5E3B():
        OP_95(0xFE, 11800, 850, 10000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E3B)
    WaitChrThread(0x101, 1)

    def lambda_5E59():
        OP_95(0xFE, 13800, 850, 12000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E59)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x0)
    OP_6F(0x1)
    OP_24(0x335)
    Sound(822, 0, 100, 0)
    ClearMapObjFlags(0x1F, 0x20)
    OP_70(0x1F, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    #Sound(1084, 255, 90, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0155
    AnonymousTalk(
        0x101,
        (
            "#0001Fはい、もしもし。\x02\x03",

            "えっと……\x01",
            "こちらクロスベル警察、\x01",
            "特務支援課・分室ビルです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性の声")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ロイド？\x01",
            "その声はロイドね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0157
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fなっ……セシル姉か！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性の声")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はあ、よかったぁ……\x02\x03",

            "警察の方に連絡したら\x01",
            "こちらの番号を教えてくれたの。\x02\x03",

            "『特務支援課』だったかしら。\x01",
            "そういう部署に配属になったのね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0159
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fあ、いや……\x01",
            "まだ正式じゃないけどさ。\x02\x03",

            "#0006Fそれよりも、ごめん。\x01",
            "本当はすぐにでもセシル姉に\x01",
            "挨拶しに行きたかったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性の声")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ううん、気にしないで。\x02\x03",

            "私の方こそ、あなたを駅まで\x01",
            "出迎えるべきだったのに……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0161
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fそれこそ気にしないでよ。\x02\x03",

            "仕事、忙しいんだろ？\x01",
            "休暇が取れた時でもいいからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性の声")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ううっ、ロイドが冷たい……\x02\x03",

            "せっかく３年ぶりに\x01",
            "再会するお姉ちゃんに対して\x01",
            "なんて素っ気ないのかしら……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0163
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0012Fああもう……\x01",
            "何とか時間を作るからさ。\x02\x03",

            "#0000Fそれと、おばさんたちには\x01",
            "明日にでも挨拶しに行くよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性の声")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "うん、そうね。\x02\x03",

            "お母さんたちもロイドのことを\x01",
            "すごく心配してたから……\x02\x03",

            "でも、ふふっ……嬉しいな。\x02\x03",

            "やっと……\x01",
            "クロスベルに帰ってきたのね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0165
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004Fうん……\x02\x03",

            "#0002F──ただいま、セシル姉。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性の声")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おかえりなさい、ロイド。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x335)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_5CC4 end

    def Function_22_6458(): pass

    label("Function_22_6458")

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
    SetChrPos(0x11, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis151.itp")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0167
    AnonymousTalk(
        0x11,
        "──ふむ、話は分かった。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6627")

    #C0168
    ChrTalk(
        0x11,
        (
            "#5P#1004Fま、新人にしちゃあ\x01",
            "頑張った方じゃねえか？\x02\x03",

            "#1002F無い知恵絞って\x01",
            "色々考えたみたいだしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#12P#0012Fは、はあ……\x01",
            "（一応、誉めてるんだよな？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6796")

    label("loc_6627")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_66E0")

    #C0170
    ChrTalk(
        0x11,
        (
            "#5P#1003Fまあ、新人にしたら\x01",
            "こんなもんだろ。\x02\x03",

            "#1000F次、似たような事件がありゃあ\x01",
            "もう少し上手く捌けるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#12P#0005Fは、はい。\x01",
            "（けっこう厳しいな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6796")

    label("loc_66E0")


    #C0172
    ChrTalk(
        0x11,
        (
            "#5P#1006F結果オーライなのはいいが\x01",
            "ちょいと粗#2Rアラ#も目立つな……\x02\x03",

            "#1000Fまあ新人だから\x01",
            "こんなモンかもしれねえが。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#12P#0006F……すみません。\x01",
            "（確かに大雑把だったか……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6796")

    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0174
    ChrTalk(
        0x11,
        (
            "#5P#1003Fしかし、今回の一件で\x01",
            "お前らにも見えてきただろ。\x02\x03",

            "#1001Fこのクロスベルって場所の\x01",
            "やっかいな側面が。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#12P#0008F………それは…………\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#0306Fまあ、確かにちょいと\x01",
            "面倒くさい場所みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#4P#0211F様々な暗部やしがらみ……\x01",
            "大人の事情の温床って感じです。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#0108F………そうね。\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x11,
        (
            "#5P#1000F警察本部の連中だって\x01",
            "決して無能ってわけじゃない。\x02\x03",

            "賄賂を受け取ってるような\x01",
            "バカ野郎もいるみたいだが……\x02\x03",

            "多くの捜査官は、そこそこ優秀で\x01",
            "自分なりの正義感を持ってる連中だ。\x02\x03",

            "#1003Fだが……有形無形の《壁》がある。\x02\x03",

            "#1001Fマフィアの利権と繋がっている\x01",
            "議員や役人どもとかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x11,
        (
            "#5P#1002Fどうだ、ロイド？\x02\x03",

            "警察辞めて遊撃士にでも\x01",
            "転職したくなってきたか？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0182
    ChrTalk(
        0x101,
        (
            "#12P#0003F……いえ。\x02\x03",

            "#0000Fそんな事情があっての\x01",
            "『特務支援課』でしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6B13():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B13)
    Sleep(50)

    def lambda_6B23():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6B23)
    Sleep(50)

    def lambda_6B33():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6B33)
    WaitChrThread(0x102, 2)

    #C0183
    ChrTalk(
        0x11,
        "#5P#1005Fほう……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Sleep(300)

    #C0184
    ChrTalk(
        0x101,
        (
            "#12P#0001F『人を守る』──\x01",
            "遊撃士の理念は確かに素晴らしいけど\x01",
            "それだけじゃ解決できない問題もある。\x02\x03",

            "#0003F密貿易に違法な武器取引。\x02\x03",

            "盗品売買にミラ・ロンダリング。\x02\x03",

            "そしてマフィアと政治家の癒着……\x02\x03",

            "#0001Fどれも遊撃士が\x01",
            "直接的には介入できない問題です。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        "#2P#0305F確かに……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        (
            "#4P#0203F『支える籠手』の力にも\x01",
            "限界はあるという事ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#12P#0004F──でも、警察なら\x01",
            "本来それが可能なはずです。\x02\x03",

            "#0000F現実として、様々な《壁》が\x01",
            "立ち塞がっていたとしても……\x02\x03",

            "そうした壁を突破できる\x01",
            "可能性はゼロじゃないはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#11P#0104F……なるほど。\x02\x03",

            "#0100F支援課#6Rこ　こ#ならその可能性を\x01",
            "見出せるかもしれない……\x02\x03",

            "つまり、そういうことね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0189
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ……\x01",
            "ちょっと楽天的すぎるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#4P#0204F……現実はそこまで\x01",
            "甘くないと思いますけど。\x02\x03",

            "#0202Fただ、どんな可能性も\x01",
            "ゼロではないのは確かです。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        (
            "#11P#0304Fやれやれ……\x02\x03",

            "不良の頭#2Rヘッド#とタイマン張ったり、\x01",
            "危険な囮役を買って出たり……\x02\x03",

            "#0302F真面目で大人しそうなツラして\x01",
            "大した熱血野郎だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#6P#0005F別に熱血って\x01",
            "わけじゃないと思うけど……\x02\x03",

            "#0000F──でも今回、みんなと一緒に\x01",
            "仕事をしてて改めて思った。\x02\x03",

            "#0004Fお互い、まだまだ未熟な\x01",
            "ところはあるだろうけど……\x02\x03",

            "#0002Fこのメンバーだったら\x01",
            "どんな壁も、力を合わせて\x01",
            "乗り越えて行けそうだってね。\x02",
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

    #C0193
    ChrTalk(
        0x102,
        "#11P#0105Fロ、ロイド……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        "#11P#0302Fはは……なんつーか。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        "#4P#0206F……クサすぎです……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x11,
        "#5P#1004Fククク……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0197
    ChrTalk(
        0x11,
        "#5P#1009F#4Sハーッハッハッハッ！\x02",
    )

    CloseMessageWindow()

    def lambda_713C():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_713C)
    Sleep(50)

    def lambda_714C():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_714C)
    Sleep(50)

    def lambda_715C():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_715C)
    Sleep(50)

    def lambda_716C():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_716C)
    Sleep(300)

    #C0198
    ChrTalk(
        0x101,
        (
            "#12P#0011Fそ、そんな笑わなくても。\x02\x03",

            "#0006Fえっと……\x01",
            "さすがに夢見すぎですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x11,
        (
            "#5P#1004Fクク……\x01",
            "まあ、いいんじゃねえか？\x02\x03",

            "#1002F『特務支援課』が設立されたのは\x01",
            "色々なしがらみによるもんだが……\x02\x03",

            "その場所をどう利用するかは\x01",
            "お前たちの自由っちゃ自由だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#12P#0002Fあ……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x11,
        (
            "#5P#1004F俺は直接、お前たちに\x01",
            "力を貸すことはないだろうが……\x02\x03",

            "やりすぎちまっても\x01",
            "お偉いさんに睨まれないよう、\x01",
            "ケムに巻くくらいはしてやるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#12P#0000F課長……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#0102Fふふ……\x01",
            "要するに放任主義ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#0306Fったく、話が判るんだか、\x01",
            "いい加減なだけなんだか。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#4P#0211Fと言うより\x01",
            "ただ面倒なだけでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x11,
        (
            "#5P#1002Fま、ズルイ大人だからな。\x02\x03",

            "#1003F『特務支援課』が単なる\x01",
            "遊撃士のパクリで終わるか……\x02\x03",

            "それとも新たな可能性を\x01",
            "見出すことが出来るのか……\x02\x03",

            "#1002F俺は煙草でもふかしながら\x01",
            "せいぜい眺めさせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1388)
    WaitBGM()
    OP_29(0x3D, 0x4, 0x10)
    OP_29(0x3E, 0x4, 0x10)
    OP_29(0x3D, 0x4, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74F1")
    OP_29(0x2, 0x4, 0x40)
    Jump("loc_7503")

    label("loc_74F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7503")
    OP_29(0x2, 0x4, 0x40)

    label("loc_7503")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7521")
    OP_29(0x3, 0x4, 0x40)
    Jump("loc_7533")

    label("loc_7521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7533")
    OP_29(0x3, 0x4, 0x40)

    label("loc_7533")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7551")
    OP_29(0x4, 0x4, 0x40)
    Jump("loc_7563")

    label("loc_7551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7563")
    OP_29(0x4, 0x4, 0x40)

    label("loc_7563")

    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    SubItemNumber(0x339, 1)
    SubItemNumber(0x35A, 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x24, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_6458 end

    def Function_23_7646(): pass

    label("Function_23_7646")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50210.itc", 0x1E)
    OP_68(3000, 700, 127500, 0)
    MoveCamera(35, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 3000, 500, 125500, 270)
    OP_68(3000, 700, 125500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    OP_63(0x101, 0xFFFFFE0C, 1300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0207
    ChrTalk(
        0x101,
        (
            "#0003F（……エリィか……）\x02\x03",

            "#0008F（この２ヶ月、結構親密に\x01",
            "  なれたと思ってたけど……）\x02\x03",

            "（肝心なことは何も\x01",
            "  判ってなかったんだよな……）\x02\x03",

            "#0006F（マクダエル市長の孫娘で\x01",
            "  政治家志望か……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "確かエリィは、警察学校には\x01",
            "行ってなかったんだよな？\x02\x03",

            "どういう経緯で警察に？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "うーん……\x01",
            "ありていに言うと社会勉強ね。\x02\x03",

            "ちなみに入る時の試験は\x01",
            "筆記と射撃だったんだけど……\x02\x03",

            "どちらも満点だったから\x01",
            "断りきれなかったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "な、なんか聞けば聞くほど\x01",
            "俺の場合とは違うような……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "あら、あなただって\x01",
            "新人で捜査官資格を取ったのは\x01",
            "珍しいんじゃないかしら？\x02\x03",

            "やっぱり事情があるんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "……それは………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "ふふっ……\x02\x03",

            "ここから先は、正式な同僚に\x01",
            "なってからの方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0xFFFFFE0C, 1300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)
    MoveCamera(45, 18, 0, 900)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x3)
    Sleep(200)
    SetChrSubChip(0x101, 0x4)
    Sleep(500)
    OP_6F(0x40)

    #C0214
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F──よし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2470, 700, 126170, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 125500, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0215
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F#5P（少し、エリィと話してみよう。）\x02\x03",

            "（何を悩んでいるのか……\x01",
            "  力になれるかもしれないし。）\x02\x03",

            "#0000F（それに──あの時の続きを\x01",
            "  そろそろ話してもいいよな……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_D5(0x1E)
    SetChrPos(0x0, 1000, 30, 125500, 180)
    SetScenarioFlags(0x81, 6)
    OP_29(0x42, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_23_7646 end

    def Function_24_7BE2(): pass

    label("Function_24_7BE2")

    EventBegin(0x0)
    Fade(1000)
    OP_68(163700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 163700, 0, 62100, 0)
    OP_0D()

    #C0216
    ChrTalk(
        0x101,
        "#4P#0003F（よし……）\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 163700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x101,
        (
            "#4P#0000F──エリィ。\x01",
            "ちょっといいかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0218
    ChrTalk(
        0x101,
        (
            "#4P#0005F（返事がない……寝てるのか？）\x02\x03",

            "#0008F（いや……\x01",
            "  それにしては気配がないな。）\x02\x03",

            "#0001Fすまない、開けるぞ？\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x5)

    def lambda_7D3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D3B)

    def lambda_7D4C():
        OP_95(0xFE, 163700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D4C)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_68(156000, 1300, 123500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 156000, 0, 120000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_7DCF():
        OP_96(0xFE, 0x26160, 0x0, 0x1DA9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DCF)

    def lambda_7DE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7DE9)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x0, 0x1F4)

    #C0219
    ChrTalk(
        0x101,
        (
            "#0008F（いない……\x01",
            "  どこに行ったんだ？）\x02\x03",

            "#0000F（……ちょっと捜してみるか。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x5, 0x10)
    SetChrPos(0x0, 156000, 30, 121500, 0)
    SetScenarioFlags(0x81, 7)
    EventEnd(0x5)
    Return()

    # Function_24_7BE2 end

    def Function_25_7E8D(): pass

    label("Function_25_7E8D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14100, 1850, 8000, 0)
    MoveCamera(7, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 15200, 850, 8500, 45)
    SetChrPos(0x102, 16400, 850, 7900, 0)
    SetChrPos(0x103, 16100, 850, 10000, 45)
    SetChrPos(0x104, 14400, 850, 9900, 90)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x1, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis124.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    OP_68(16100, 1850, 10000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(72, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetMapFlags(0x400)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【概要・沿革】")
    MenuCmd(1, 0, "【武装・勢力範囲】")
    MenuCmd(1, 0, "【マルコーニ会長】")
    MenuCmd(1, 0, "【ガルシア・ロッシ】")
    MenuCmd(1, 0, "【ハルトマン議長】")
    MenuCmd(1, 0, "【閲覧をやめる】")
    MenuCmd(3, 0, 0x5)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Sleep(1000)

    #A0220
    AnonymousTalk(
        0x103,
        (
            "#0203F──記録結晶を接続#4Rコネクト#。\x02\x03",

            "#0200Fこれで一通りの項目に\x01",
            "アクセスする事ができます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0221
    AnonymousTalk(
        0x101,
        "#0001F結構揃っているな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0222
    AnonymousTalk(
        0x102,
        (
            "#0103F今まで不明なところも多かった\x01",
            "《ルバーチェ》の情報……\x02\x03",

            "#0101Fまとまった形で確認できるのは\x01",
            "初めてかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0223
    AnonymousTalk(
        0x104,
        (
            "#0300Fそんじゃま、\x01",
            "一通り目を通していくか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0224
    AnonymousTalk(
        0x101,
        "#0001Fああ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    ClearScenarioFlags(0x1, 0)
    ClearMapFlags(0x400)

    label("loc_8242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_830B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【概要・沿革】")
    MenuCmd(1, 0, "【武装・勢力範囲】")
    MenuCmd(1, 0, "【マルコーニ会長】")
    MenuCmd(1, 0, "【ガルシア・ロッシ】")
    MenuCmd(1, 0, "【ハルトマン議長】")
    MenuCmd(1, 0, "【閲覧をやめる】")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82F6")
    Jump("loc_82FA")

    label("loc_82F6")

    MenuCmd(3, 0, 0x5)

    label("loc_82FA")

    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Jump("loc_830E")

    label("loc_830B")

    SetScenarioFlags(0x1, 0)

    label("loc_830E")

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8342"),
        (1, "loc_86AC"),
        (2, "loc_8A43"),
        (3, "loc_8E1E"),
        (4, "loc_9238"),
        (5, "loc_96D1"),
        (SWITCH_DEFAULT, "loc_9779"),
    )


    label("loc_8342")

    MenuTitle(-1, 30, 0, "概要・沿革")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クロスベル自治州に存在する\x01",
            "最大のマフィア組織。\x02\x03",

            "その歴史は古く、自治州が成立した\x01",
            "七耀暦１１３０年前後に遡ると思われる。\x02\x03",

            "『商会』の名を冠する事からも分かるように\x01",
            "当初は帝国－共和国間の密貿易で財を成し、\x01",
            "自治州における暗部を一手に引き受けてきた。\x02\x03",

            "現在、その非合法なビジネスは多岐に渡り、\x01",
            "武器の密貿易、盗品売買、地上げ、総会屋、\x01",
            "ミラ・ロンダリング、各種風俗産業の運営、\x01",
            "猟兵団の仲介斡旋などが確認されている。\x02\x03",

            "有力議員と密接な関係を持っているため\x01",
            "その犯罪行為の多くは摘発を免れており、\x01",
            "仮に構成員が逮捕されたとしても\x01",
            "すぐに保釈されてしまうことが多い。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86A7")

    #A0226
    AnonymousTalk(
        0x101,
        (
            "#0005Fなるほど……\x01",
            "よくまとまってる情報だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0227
    AnonymousTalk(
        0x102,
        (
            "#0100F今まで聞いていた話が\x01",
            "的確に纏められている感じね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0228
    AnonymousTalk(
        0x103,
        (
            "#0206Fしかし……改めて見ると\x01",
            "やっぱりとんでもないですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0229
    AnonymousTalk(
        0x104,
        (
            "#0301Fああ、非合法なビジネスで\x01",
            "相当儲けまくってる感じだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 2)

    label("loc_86A7")

    Jump("loc_9779")

    label("loc_86AC")

    MenuTitle(-1, 30, 0, "武装・勢力範囲")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "構成員数はおよそ３００名。\x01",
            "自治州内外の末端構成員も含めると\x01",
            "５００名以上になると推定される。\x02\x03",

            "猟兵団や、周辺国の軍隊経験者も多く、\x01",
            "最新の導力兵器を密貿易しているため\x01",
            "相当な戦力を保持していると思われる。\x02\x03",

            "広域暴力組織でないにも関わらず、\x01",
            "その影響力はクロスベルに留まらず、\x01",
            "帝国・共和国の有力者との繋がりも深い。\x02\x03",

            "最新の情報では、対抗組織である\x01",
            "《黒月》に押され気味であったようだが、\x01",
            "軍用犬を導入することで戦力を補強し、\x01",
            "再び優位を取り戻したと目されている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3E")

    #A0231
    AnonymousTalk(
        0x101,
        (
            "#0001Fこうして見ると……\x01",
            "やっぱり大きな組織だよな。\x02\x03",

            "それに、軍隊経験者も\x01",
            "かなり多そうな感じだし……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0232
    AnonymousTalk(
        0x104,
        (
            "#0303Fああ、前に下っ端と戦った時、\x01",
            "かなり手強かったのも納得だぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0233
    AnonymousTalk(
        0x103,
        (
            "#0203Fでも、あの時の軍用犬……\x01",
            "そのまま運用しているみたいですね。\x02\x03",

            "#0211Fわたしたちが捕まえたのも\x01",
            "無駄になったというわけですか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0234
    AnonymousTalk(
        0x101,
        "#0006Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0235
    AnonymousTalk(
        0x102,
        "#0106Fちょっと空しくなるわね……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 3)

    label("loc_8A3E")

    Jump("loc_9779")

    label("loc_8A43")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "マルコーニ会長")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ルバーチェ商会の代表にして\x01",
            "マフィア組織を支配している人物。\x02\x03",

            "ルバーチェの会長としては５代目だが\x01",
            "正式な代替わりをしたのではなく、\x01",
            "８年ほど前、謀略と裏切りによって\x01",
            "４代目を追い落として組織を掌握した。\x02\x03",

            "帝国系移民のためか、どちらかというと\x01",
            "帝国派議員との関係を重視しており、\x01",
            "特にハルトマン議長との繋がりは深い。\x02\x03",

            "一方、共和国方面のパイプも確保しており、\x01",
            "その意味では、クロスベルという特異な地域で\x01",
            "抜け目なく立ち回っていると言えるだろう。\x02\x03",

            "なお、帝国貴族への憧れがあるらしく、\x01",
            "悪趣味な成金趣味の服装・調度を好む模様。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E06")

    #A0237
    AnonymousTalk(
        0x104,
        (
            "#0305Fこりゃあ……\x01",
            "なんつーか、印象的なオッサンだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0238
    AnonymousTalk(
        0x103,
        (
            "#0211Fユーモラスな外見ですけど\x01",
            "やってる事はえげつないです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0239
    AnonymousTalk(
        0x102,
        (
            "#0103Fそれに、思っていた以上に\x01",
            "柔軟で頭も切れるみたいね。\x02\x03",

            "#0101F帝国寄りなのに、共和国方面にも\x01",
            "コネクションを持ってるなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0240
    AnonymousTalk(
        0x101,
        "#0001F相当、やっかいそうな相手だな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 4)

    label("loc_8E06")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_9779")

    label("loc_8E1E")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis053.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "ガルシア・ロッシ")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ルバーチェ商会の営業本部長にして\x01",
            "マフィア組織の若頭と目されている人物。\x02\x03",

            "猟兵団『西風の旅団』の部隊長だったが\x01",
            "８年前、マルコーニが先代会長を\x01",
            "追い落とす時に実行部隊として雇われた。\x02\x03",

            "その後、マルコーニに引き抜かれる形で\x01",
            "猟兵団を抜けてルバーチェ商会に入社。\x01",
            "マフィアの武装化・戦力強化に貢献した。\x02\x03",

            "猟兵時代は《キリングベア》と呼ばれ、\x01",
            "その巨体を活かした軍用格闘術をもって\x01",
            "数多の敵兵を屠#2Rほふ#ったと伝えられている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9220")

    #A0242
    AnonymousTalk(
        0x102,
        (
            "#0105Fあの若頭の人……\x01",
            "猟兵団の出身だったのね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0243
    AnonymousTalk(
        0x103,
        (
            "#0208F『西風の旅団』……\x01",
            "どこかで聞いた事があるような。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0244
    AnonymousTalk(
        0x104,
        (
            "#0303F……大陸西部において\x01",
            "最強と謳われた猟兵団の一つだ。\x02\x03",

            "その部隊長をやってたって事は\x01",
            "相当な戦闘力なのは間違いねぇな。\x02\x03",

            "#0301F《キリングベア》って名前も\x01",
            "何度か耳にした事があるぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0245
    AnonymousTalk(
        0x101,
        (
            "#0001Fそうか……\x01",
            "確かに凄い迫力だったけど。\x02\x03",

            "#0005Fでも、やっぱりランディ、\x01",
            "そういうのは詳しいんだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0246
    AnonymousTalk(
        0x104,
        (
            "#0304Fはは……\x01",
            "昔、噂で聞いたくらいだけどな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 5)

    label("loc_9220")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_9779")

    label("loc_9238")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis054.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "ハルトマン議長")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クロスベル自治州議会の\x01",
            "議長を務めている大物政治家。\x02\x03",

            "自治州政府代表の一人でもあり、\x01",
            "帝国派議員のリーダーを務めている。\x02\x03",

            "帝国貴族に連なる名門の出身であり、\x01",
            "自治州にある保養地ミシュラムに\x01",
            "贅を尽くした巨大な邸宅を構えている。\x02\x03",

            "ルバーチェのマルコーニ会長とは\x01",
            "旧知の仲であり、各種利権や密貿易、\x01",
            "ミラ・ロンダリングなどにおいて\x01",
            "密接な協力関係にあると目されている。\x02\x03",

            "なお昨年、非公式ではあるが\x01",
            "帝国宰相ギリアス・オズボーンと会談し、\x01",
            "その権威を内外に改めて見せ付けた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B9")

    #A0248
    AnonymousTalk(
        0x101,
        "#0005Fこれがハルトマン議長……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0249
    AnonymousTalk(
        0x104,
        (
            "#0301Fなんつーか、政治家ってより\x01",
            "帝国の大貴族って感じだな。\x02\x03",

            "しかし、あの《鉄血宰相》と\x01",
            "会見したってのはマジなのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0250
    AnonymousTalk(
        0x102,
        (
            "#0103Fええ、非公式ではあるけれど\x01",
            "去年の春頃、オズボーン宰相が\x01",
            "クロスベルを訪れたらしいの。\x02\x03",

            "#0101Fおじいさまには会わずに\x01",
            "ハルトマン議長とだけ会談して\x01",
            "すぐに帰国したらしいけど……\x02\x03",

            "一時期、各国の政界では\x01",
            "その話で持ちきりだったみたい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0251
    AnonymousTalk(
        0x101,
        (
            "#0001Fそんな事があったのか……\x02\x03",

            "#0008F《鉄血宰相》……\x01",
            "相当、有名な人みたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0252
    AnonymousTalk(
        0x103,
        (
            "#0203F何のために訪れたのか\x01",
            "ちょっと気になりますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 6)

    label("loc_96B9")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_9779")

    label("loc_96D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9753")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "◆全項目見た\x01",          # 0
            "◆全項目見てない\x01",      # 1
            "◆変更しない\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_972B"),
        (1, "loc_973F"),
        (SWITCH_DEFAULT, "loc_9753"),
    )


    label("loc_972B")

    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Jump("loc_9753")

    label("loc_973F")

    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    Jump("loc_9753")

    label("loc_9753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9774")
    SetScenarioFlags(0x0, 7)
    Jump("loc_9774")

    label("loc_9774")

    Jump("loc_9779")

    label("loc_9779")

    Jump("loc_8242")

    label("loc_977E")

    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MenuCmd(4, 0, 0x0)

    #C0253
    ChrTalk(
        0x101,
        (
            "#6P#0003F──なるほど。\x02\x03",

            "#0001F今まで漠然としてたところが\x01",
            "かなり見えるようになったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        (
            "#6P#0106Fええ……\x02\x03",

            "#0108F冷酷かつ抜け目ないトップと\x01",
            "歴戦の猟兵だった若頭の存在……\x02\x03",

            "#0101Fそしてハルトマン議長との関係ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#0306Fしかもその議長ってのは\x01",
            "あの《鉄血宰相》とも\x01",
            "何かしらの関係があるんだろ？\x02\x03",

            "確かにクロスベルの警察が\x01",
            "全く手を出せないのも納得だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#6P#0008F……そうだな………\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x103,
        (
            "#0205F#5P……待ってください。\x02\x03",

            "#0201F渡された記録結晶の中に\x01",
            "隠されたデータがありました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0258
    ChrTalk(
        0x101,
        "#6P#0005F隠されたデータ……？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#0301Fって、隠したってんなら\x01",
            "あのガキが隠したんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#0206F#5Pええ、どうやらわたしが気付くか\x01",
            "試そうとしたらしいですね。\x02\x03",

            "#0211F……後でおしおきをしないと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0261
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれはともかく……\x01",
            "その隠されたデータも見れるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        "#0202F#5Pええ、お茶の子さいさいです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(849, 0, 100, 0)
    Sleep(1000)
    Sound(72, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    SetMapFlags(0x400)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【概要・沿革】")
    MenuCmd(1, 0, "【武装・勢力範囲】")
    MenuCmd(1, 0, "【マルコーニ会長】")
    MenuCmd(1, 0, "【ガルシア・ロッシ】")
    MenuCmd(1, 0, "【ハルトマン議長】")
    MenuCmd(1, 0, "【黒の競売会】")
    MenuCmd(1, 0, "【閲覧をやめる】")
    MenuCmd(3, 0, 0x6)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Sleep(1000)
    MenuCmd(5, 0, 0x1)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x2)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x3)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x4)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x5)
    Sound(4, 0, 100, 0)
    Sleep(500)

    #A0263
    AnonymousTalk(
        0x101,
        (
            "#4S#0005F！！\x02\x03",

            "#0013F#3Sこれは……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0264
    AnonymousTalk(
        0x102,
        "#0101F《黒の競売会#10Rシュバルツオークション#》……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0265
    AnonymousTalk(
        0x104,
        (
            "#0305Fエステルちゃんたちが言ってた\x01",
            "例のイベントってやつか。\x02\x03",

            "#0309Fハハ、あのガキ、\x01",
            "洒落たマネをすんじゃねーか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0266
    AnonymousTalk(
        0x103,
        (
            "#0203F……どうやら本当に\x01",
            "存在するイベントのようですね。\x02\x03",

            "#0201Fそれもルバーチェ絡みですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0267
    AnonymousTalk(
        0x101,
        (
            "#0006Fああ……\x01",
            "怪しいとは思ってたけど。\x02\x03",

            "#0001Fよし──とにかく見てみるか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x0, 7)
    ClearMapFlags(0x400)

    label("loc_9E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_9EDA")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【概要・沿革】")
    MenuCmd(1, 0, "【武装・勢力範囲】")
    MenuCmd(1, 0, "【マルコーニ会長】")
    MenuCmd(1, 0, "【ガルシア・ロッシ】")
    MenuCmd(1, 0, "【ハルトマン議長】")
    MenuCmd(1, 0, "【黒の競売会】")
    MenuCmd(1, 0, "【閲覧をやめる】")
    MenuCmd(3, 0, 0x6)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Jump("loc_9EDD")

    label("loc_9EDA")

    SetScenarioFlags(0x1, 0)

    label("loc_9EDD")

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9F17"),
        (1, "loc_A178"),
        (2, "loc_A37C"),
        (3, "loc_A610"),
        (4, "loc_A842"),
        (5, "loc_AAA0"),
        (6, "loc_AF52"),
        (SWITCH_DEFAULT, "loc_AF57"),
    )


    label("loc_9F17")

    MenuTitle(-1, 30, 0, "概要・沿革")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クロスベル自治州に存在する\x01",
            "最大のマフィア組織。\x02\x03",

            "その歴史は古く、自治州が成立した\x01",
            "七耀暦１１３０年前後に遡ると思われる。\x02\x03",

            "『商会』の名を冠する事からも分かるように\x01",
            "当初は帝国－共和国間の密貿易で財を成し、\x01",
            "自治州における暗部を一手に引き受けてきた。\x02\x03",

            "現在、その非合法なビジネスは多岐に渡り、\x01",
            "武器の密貿易、盗品売買、地上げ、総会屋、\x01",
            "ミラ・ロンダリング、各種風俗産業の運営、\x01",
            "猟兵団の仲介斡旋などが確認されている。\x02\x03",

            "有力議員と密接な関係を持っているため\x01",
            "その犯罪行為の多くは摘発を免れており、\x01",
            "仮に構成員が逮捕されたとしても\x01",
            "すぐに保釈されてしまうことが多い。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_AF57")

    label("loc_A178")

    MenuTitle(-1, 30, 0, "武装・勢力範囲")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "構成員数はおよそ３００名。\x01",
            "自治州内外の末端構成員も含めると\x01",
            "５００名以上になると推定される。\x02\x03",

            "猟兵団や、周辺国の軍隊経験者も多く、\x01",
            "最新の導力兵器を密貿易しているため\x01",
            "相当な戦力を保持していると思われる。\x02\x03",

            "広域暴力組織でないにも関わらず、\x01",
            "その影響力はクロスベルに留まらず、\x01",
            "帝国・共和国の有力者との繋がりも深い。\x02\x03",

            "最新の情報では、対抗組織である\x01",
            "《黒月》に押され気味であったようだが、\x01",
            "軍用犬を導入することで戦力を補強し、\x01",
            "再び優位を取り戻したと目されている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_AF57")

    label("loc_A37C")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "マルコーニ会長")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ルバーチェ商会の代表にして\x01",
            "マフィア組織を支配している人物。\x02\x03",

            "ルバーチェの会長としては５代目だが\x01",
            "正式な代替わりをしたのではなく、\x01",
            "８年ほど前、謀略と裏切りによって\x01",
            "４代目を追い落として組織を掌握した。\x02\x03",

            "帝国系移民のためか、どちらかというと\x01",
            "帝国派議員との関係を重視しており、\x01",
            "特にハルトマン議長との繋がりは深い。\x02\x03",

            "一方、共和国方面のパイプも確保しており、\x01",
            "その意味では、クロスベルという特異な地域で\x01",
            "抜け目なく立ち回っていると言えるだろう。\x02\x03",

            "なお、帝国貴族への憧れがあるらしく、\x01",
            "悪趣味な成金趣味の服装・調度を好む模様。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_AF57")

    label("loc_A610")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis053.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "ガルシア・ロッシ")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ルバーチェ商会の営業本部長にして\x01",
            "マフィア組織の若頭と目されている人物。\x02\x03",

            "猟兵団『西風の旅団』の部隊長だったが\x01",
            "８年前、マルコーニが先代会長を\x01",
            "追い落とす時に実行部隊として雇われた。\x02\x03",

            "その後、マルコーニに引き抜かれる形で\x01",
            "猟兵団を抜けてルバーチェ商会に入社。\x01",
            "マフィアの武装化・戦力強化に貢献した。\x02\x03",

            "猟兵時代は《キリングベア》と呼ばれ、\x01",
            "その巨体を活かした軍用格闘術をもって\x01",
            "数多の敵兵を屠#2Rほふ#ったと伝えられている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_AF57")

    label("loc_A842")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis054.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "ハルトマン議長")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クロスベル自治州議会の\x01",
            "議長を務めている大物政治家。\x02\x03",

            "自治州政府代表の一人でもあり、\x01",
            "帝国派議員のリーダーを務めている。\x02\x03",

            "帝国貴族に連なる名門の出身であり、\x01",
            "自治州にある保養地ミシュラムに\x01",
            "贅を尽くした巨大な邸宅を構えている。\x02\x03",

            "ルバーチェのマルコーニ会長とは\x01",
            "旧知の仲であり、各種利権や密貿易、\x01",
            "ミラ・ロンダリングなどにおいて\x01",
            "密接な協力関係にあると目されている。\x02\x03",

            "なお昨年、非公式ではあるが\x01",
            "帝国宰相ギリアス・オズボーンと会談し、\x01",
            "その権威を内外に改めて見せ付けた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_AF57")

    label("loc_AAA0")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis055.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "黒の競売会#10Rシュバルツオークション#")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "毎年、創立記念祭の最終日に\x01",
            "ルバーチェが開催しているオークション。\x02\x03",

            "保養地ミシュラムにあるハルトマン議長の\x01",
            "大邸宅を借り切って開催されている。\x02\x03",

            "出品される品は一流のものばかりだが、\x01",
            "盗品や賄賂・脱税・横流しなどに関連する\x01",
            "美術品・絵画・宝飾品であることが多い。\x02\x03",

            "また、クロスベルのみならず、\x01",
            "周辺諸国の貴族や資産家が多く招待され、\x01",
            "裏の社交界的な催しとしても機能している。\x02\x03",

            "ルバーチェにとっては重要な収入源であり、\x01",
            "ハルトマン議長にとっては各国の有力者と\x01",
            "繋がりを持つ絶好の場となっているようだ。\x02\x03",

            "なお、オークション会場の警備は\x01",
            "ルバーチェの構成員が厳重に行っており、\x01",
            "《金の薔薇》が刻まれた招待カードがない限り、\x01",
            "中に入ることは出来ないらしい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0274
    AnonymousTalk(
        0x101,
        "#0007Fこ、これは……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0275
    AnonymousTalk(
        0x102,
        (
            "#0105Fし、信じられない……\x02\x03",

            "#0101Fそんなものが\x01",
            "毎年開かれていたなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0276
    AnonymousTalk(
        0x103,
        (
            "#0201Fでも、ちょっとおかしいです。\x02\x03",

            "秘密にしている割には\x01",
            "かなり大規模な催しですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0277
    AnonymousTalk(
        0x104,
        (
            "#0306Fいや、警察とマスコミには\x01",
            "厳重に規制がかかってんだろ。\x02\x03",

            "#0301Fでもなけりゃ、こんなモンが\x01",
            "表沙汰にならねぇわけがねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("男の声")

    #A0278
    AnonymousTalk(
        0xFF,
        "──その通りだ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0279
    AnonymousTalk(
        0x101,
        "#0011F！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    SetScenarioFlags(0x0, 7)
    Jump("loc_AF57")

    label("loc_AF52")

    Jump("loc_AF57")

    label("loc_AF57")

    Jump("loc_9E1D")

    label("loc_AF5C")

    OP_68(14500, 1850, 10200, 2000)
    MoveCamera(60, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 6500, 850, 10500, 90)
    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    OP_68(13500, 1850, 10200, 2000)

    def lambda_AFEA():
        OP_95(0xFE, 10500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AFEA)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MenuCmd(4, 0, 0x0)

    def lambda_B01B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B01B)
    Sleep(50)

    def lambda_B02B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B02B)
    Sleep(50)

    def lambda_B03B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B03B)
    Sleep(50)

    def lambda_B04B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B04B)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x11, 1)

    #C0280
    ChrTalk(
        0x101,
        "#0005F#11P課長……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        "#11P#0108Fお、お疲れさまです。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0282
    AnonymousTalk(
        0x11,
        (
            "やれやれ……\x01",
            "まさか自力でそこまで\x01",
            "辿り着いちまうとはな。\x02\x03",

            "まあいい、ここじゃなんだ。\x02\x03",

            "そっちの部屋で一通り話してやろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x11, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0283
    ChrTalk(
        0x101,
        (
            "#12P#0013F──それじゃあ、\x01",
            "あのファイルにあった情報は\x01",
            "全て事実ってわけですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        (
            "#5P#1003Fああ、そうだ。\x02\x03",

            "#1002F誰が調べたモンかは知らんが\x01",
            "なかなか的確にまとめてやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x102,
        (
            "#0106Fで、でも……\x02\x03",

            "#0101F警察の上層部では\x01",
            "全て掴んでいるんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x11,
        (
            "#5P#1003Fああ、全員とは言わねぇがな。\x02\x03",

            "#1001F警部クラス以上はもちろん、\x01",
            "一課の連中は全員知ってるハズだ。\x02\x03",

            "遊撃士協会だって\x01",
            "受付やアリオスあたりだったら\x01",
            "とっくに承知しているだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0010Fくっ……\x01",
            "これも《壁》ってわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x11,
        (
            "#5P#1011Fああ……とびきりデカイ《壁》だ。\x02\x03",

            "#1001F基本的に俺は、お前たちの行動に\x01",
            "制限を付けるつもりはないが……\x02\x03",

            "《黒の競売会#10Rシュバルツオークション#》にだけは\x01",
            "手を出すのは止めろ。\x02\x03",

            "お前たちには荷が重過ぎる。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        "#12P#0007Fで、でも……！\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        (
            "#0303Fおいおい、課長。\x01",
            "言葉を間違えてんじゃねえよ。\x02\x03",

            "#0301F俺たちに荷が重いってより、\x01",
            "警察そのものが動けねぇんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x11,
        "#5P#1000F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        (
            "#0108Fそれだけの有力者を招待して、\x01",
            "しかも実質的な主催者の一人が\x01",
            "あのハルトマン議長……\x02\x03",

            "#0106F……そんなの動けるわけがないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#12P#0206F民間人に危険が迫らない限り、\x01",
            "遊撃士協会も動けませんし……\x02\x03",

            "誰も手が出せないという事ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        "#12P#0010Fだ、だからと言って……！\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x11,
        (
            "#5P#1003F……悔しい思いをしてんのは\x01",
            "お前たちだけじゃねえ。\x02\x03",

            "特に一課の連中は毎年、\x01",
            "歯軋りするような思いだろうさ。\x02\x03",

            "#1001F非人道的な催しだったら\x01",
            "それこそギルドに動かれる前に\x01",
            "意地でも突っ込むところだが……\x02\x03",

            "どうやら出品物が“黒い”以外は\x01",
            "豪華なパーティってだけらしいからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#12P#0008Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x11,
        (
            "#5P#1003F実際、下手に手を出しちまったら\x01",
            "支援課ごと潰される可能性は高い。\x02\x03",

            "だから今回ばかりは\x01",
            "俺もお前らを止めざるを得ない。\x02\x03",

            "#1000Fま、そういうことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        "#0108F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        "#0303Fハッ……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x103,
        "#12P#0203F……やれやれです。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x11,
        "#5P#1001F──納得しろ、とは言わん。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x11,
        (
            "#5P#1001Fだが、現実を直視し、\x01",
            "自分たちに何がどこまで出来るか\x01",
            "見極めるってのも時には必要だ。\x02\x03",

            "そして、その悔しさを忘れない限り、\x01",
            "いつかきっとチャンスは来るだろう。\x02\x03",

            "#1004Fお前たちが諦めなければ、な。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0305
    ChrTalk(
        0x101,
        (
            "#12P#0006F#40W……わかり、ました。\x02\x03",

            "#0008F#30Wこの件に関しては……\x01",
            "手を出すのは止めておきます。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BAAD():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BAAD)
    Sleep(50)

    def lambda_BABD():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BABD)
    Sleep(50)

    def lambda_BACD():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BACD)
    Sleep(300)

    #C0306
    ChrTalk(
        0x102,
        "#0108F#11Pロイド……\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        "#12P#0208F……ロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        "#0306Fやれやれ……だな。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0309
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして……\x01",
            "記念祭３日目は過ぎて行った。\x02\x03",

            "ティオの過去、知られざる兄の話、\x01",
            "仔猫という謎のハッカー、\x01",
            "ルバーチェに関する詳細な情報……\x02\x03",

            "──そしてクロスベルの歪みを\x01",
            "体現したかのような《黒の競売会》。\x02\x03",

            "それらがグルグルと頭の中をめぐり、\x01",
            "いつしかロイドは眠りに落ちていった──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(2000)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_7E8D end

    def Function_26_BCDA(): pass

    label("Function_26_BCDA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50092.itc", 0x1E)
    LoadChrToIndex("apl/ch50404.itc", 0x1F)
    LoadChrToIndex("chr/ch08201.itc", 0x20)
    LoadChrToIndex("apl/ch50380.itc", 0x21)
    OP_68(5500, 700, 6300, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, -1000, 0, -1500, 0)
    SetChrPos(0x102, 800, 0, 500, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, 5500, 100, 6300, 180)
    SetChrPos(0x10, 2710, 0, 2100, 225)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x10)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 5300, 350, 4400, 0)
    ClearMapFlags(0x10000000)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0310
    ChrTalk(
        0x101,
        "#1P#0002Fふう、ただいま。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(2036, 255, 100, 0)    #voice#KeA
    Sleep(150)

    #C0311
    ChrTalk(
        0xD,
        "#5P#1110Fあ、かえってきた！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    Sound(804, 0, 100, 0)
    OP_9D(0xD, 0x157C, 0x0, 0x157C, 0x12C, 0xFA0)
    BeginChrThread(0xD, 3, 0, 27)
    SetChrPos(0x101, 800, 0, 500, 0)
    BeginChrThread(0x101, 3, 0, 28)
    Sleep(1000)
    Sound(2037, 255, 100, 0)    #voice#KeA
    WaitChrThread(0xD, 3)
    WaitChrThread(0x101, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    #C0312
    ChrTalk(
        0x101,
        (
            "#12P#0012F#11Pはは……\x01",
            "キーアはいつも元気だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "#1109F#5Pうんっ！\x01",
            "キーアげんきだよー。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)

    def lambda_BF64():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BF64)
    WaitChrThread(0xD, 1)
    SetChrFlags(0xD, 0x40)

    #C0314
    ChrTalk(
        0xD,
        (
            "#1110F#5Pロイドたちは遅かったねー。\x01",
            "おしごと、いそがしかったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#0102F#11Pふふっ、まあまあかしら。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#0309F#11Pま、今日は移動に車を使えたから\x01",
            "その意味では助かったかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        "#12P#0203Fですね……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C06F():

        label("loc_C06F")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_C06F")

    QueueWorkItem2(0x101, 2, lambda_C06F)

    def lambda_C081():

        label("loc_C081")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_C081")

    QueueWorkItem2(0x102, 2, lambda_C081)

    def lambda_C093():

        label("loc_C093")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_C093")

    QueueWorkItem2(0x103, 2, lambda_C093)

    def lambda_C0A5():

        label("loc_C0A5")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_C0A5")

    QueueWorkItem2(0x104, 2, lambda_C0A5)
    OP_68(200, 1000, 2500, 1500)

    def lambda_C0C8():
        OP_95(0xFE, -900, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C0C8)
    WaitChrThread(0xD, 1)

    def lambda_C0E6():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C0E6)
    WaitChrThread(0xD, 1)
    TurnDirection(0xD, 0x103, 500)

    #C0318
    ChrTalk(
        0xD,
        (
            "#6P#1112Fねえねえ、ティオー。\x02\x03",

            "なんか疲れたカオしてるけど\x01",
            "だいじょーぶ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0319
    ChrTalk(
        0x103,
        (
            "#0204F#11Pええ……大丈夫です。\x02\x03",

            "#0202Fキーアの顔を見たら\x01",
            "元気になっちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xD,
        "#6P#1111Fんー……\x02",
    )

    CloseMessageWindow()
    OP_68(500, 1000, 2500, 600)

    def lambda_C1ED():
        OP_95(0xFE, -300, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C1ED)
    WaitChrThread(0xD, 1)

    def lambda_C20B():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C20B)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    Sound(804, 0, 100, 0)
    Sound(910, 0, 100, 0)
    Sleep(500)

    #C0321
    ChrTalk(
        0x103,
        "#0205F#11Pキ、キーア……！？\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xD,
        (
            "#6P#1109Fキーア、げんきだから\x01",
            "ティオにおすそ分けしてあげるね！\x02\x03",

            "#1104Fん～、すりすり。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        "#0202F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        "#5P#0009Fはは、なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        "#0304F#11P確かにそいつは効きそうだな。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        (
            "#5P#0109Fふふっ、何よりの\x01",
            "特効薬かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x103,
        (
            "#0204F#11P……ありがとう、キーア。\x02\x03",

            "#0202F元気、出てきました。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)

    def lambda_C3A0():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C3A0)
    WaitChrThread(0xD, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    #C0328
    ChrTalk(
        0xD,
        "#6P#1110Fえへへ、そっかー。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0329
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそういえば……\x01",
            "課長はまだ帰ってないのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    #C0330
    ChrTalk(
        0xD,
        (
            "#6P#1100Fかちょーなら\x01",
            "そこの部屋にいるよー。\x02\x03",

            "さっきおきゃくさんがきて\x01",
            "お話してるみたい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0331
    ChrTalk(
        0x101,
        (
            "#5P#0005Fお客さん？\x01",
            "こんな時間に珍しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        "#5P#0100Fどんな人だったの？\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xD,
        (
            "#6P#1103Fんー、おヒゲが生えた\x01",
            "クマさんみたいなオジサン。\x02\x03",

            "#1110Fかちょーはせんせーって\x01",
            "呼んでたかなぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#5P#0000Fああ、イアン先生か。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        "#0300F#11P珍しいな、こんな時間に。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#5P#0100F一応、わたしたちも\x01",
            "挨拶した方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0337
    ChrTalk(
        0x103,
        (
            "#12P#0202Fわたしは夕食当番ですから\x01",
            "そちらはお任せしておきます。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0338
    ChrTalk(
        0x101,
        (
            "#5P#0001F大丈夫か？\x01",
            "何だったら夕食当番くらい\x01",
            "俺が代わるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x103,
        (
            "#12P#0204Fいえ、既に下ごしらえは\x01",
            "済ませてありますから。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xD, 500)
    Sleep(300)

    #C0340
    ChrTalk(
        0x103,
        (
            "#0202F#11Pキーア、晩ご飯、\x01",
            "もう少し待ってください。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x103, 500)

    #C0341
    ChrTalk(
        0xD,
        (
            "#6P#1109Fあ、だったら\x01",
            "キーアもてつだうー！\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#0205F#11Pそうですか……？\x02\x03",

            "#0204Fふふっ、それでは\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C7CE():

        label("loc_C7CE")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_C7CE")

    QueueWorkItem2(0x101, 2, lambda_C7CE)

    def lambda_C7E0():

        label("loc_C7E0")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_C7E0")

    QueueWorkItem2(0x102, 2, lambda_C7E0)

    def lambda_C7F2():

        label("loc_C7F2")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_C7F2")

    QueueWorkItem2(0x104, 2, lambda_C7F2)
    OP_93(0xD, 0x0, 0x1F4)
    BeginChrThread(0xD, 3, 0, 29)
    Sleep(250)
    BeginChrThread(0x103, 3, 0, 30)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x2, 0x0)
    SetChrPos(0xB, 124300, 0, 8200, 0)
    OP_4C(0xD, 0xFF)
    SetChrPos(0xD, 123300, 30, 8200, 0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_68(900, 1000, 2800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 900, 0, 2800, 0)
    SetChrPos(0x1, 900, 0, 2800, 0)
    SetChrPos(0x2, 900, 0, 2800, 0)
    SetChrPos(0x10, 2710, 0, 2510, 225)
    SetScenarioFlags(0xC2, 1)
    OP_29(0x4A, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_26_BCDA end

    def Function_27_C913(): pass

    label("Function_27_C913")

    SetChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    Sound(51, 0, 100, 0)
    Sound(58, 0, 100, 0)

    def lambda_C931():
        OP_95(0xFE, 2800, 0, 5500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C931)
    WaitChrThread(0xD, 1)
    OP_68(200, 1000, 3500, 1500)
    SetCameraDistance(23000, 1500)

    def lambda_C969():
        OP_95(0xFE, 900, 0, 4900, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C969)
    WaitChrThread(0xD, 1)

    def lambda_C987():
        OP_95(0xFE, 200, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C987)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    Sound(819, 0, 100, 0)

    def lambda_C9B3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_C9B3)

    def lambda_C9C0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C9C0)
    Sleep(500)
    Return()

    # Function_27_C913 end

    def Function_28_C9D8(): pass

    label("Function_28_C9D8")


    def lambda_C9DD():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C9DD)

    def lambda_C9F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C9F7)
    Sleep(250)

    def lambda_CA0B():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA0B)

    def lambda_CA25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CA25)
    Sleep(400)

    def lambda_CA39():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CA39)

    def lambda_CA53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CA53)
    Sleep(250)

    def lambda_CA67():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CA67)

    def lambda_CA81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CA81)
    WaitChrThread(0x101, 1)

    def lambda_CA96():

        label("loc_CA96")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_CA96")

    QueueWorkItem2(0x101, 2, lambda_CA96)
    WaitChrThread(0x102, 1)

    def lambda_CAAC():

        label("loc_CAAC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_CAAC")

    QueueWorkItem2(0x102, 2, lambda_CAAC)
    WaitChrThread(0x103, 1)

    def lambda_CAC2():

        label("loc_CAC2")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_CAC2")

    QueueWorkItem2(0x103, 2, lambda_CAC2)
    WaitChrThread(0x104, 1)

    def lambda_CAD8():

        label("loc_CAD8")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_CAD8")

    QueueWorkItem2(0x104, 2, lambda_CAD8)
    Return()

    # Function_28_C9D8 end

    def Function_29_CAE6(): pass

    label("Function_29_CAE6")


    def lambda_CAEB():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CAEB)
    WaitChrThread(0xD, 1)

    def lambda_CB09():
        OP_95(0xFE, 400, 0, 6600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CB09)
    WaitChrThread(0xD, 1)

    def lambda_CB27():
        OP_95(0xFE, 3500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CB27)
    WaitChrThread(0xD, 1)

    def lambda_CB45():
        OP_95(0xFE, 8500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CB45)
    WaitChrThread(0xD, 1)
    Return()

    # Function_29_CAE6 end

    def Function_30_CB5F(): pass

    label("Function_30_CB5F")


    def lambda_CB64():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CB64)
    WaitChrThread(0x103, 1)

    def lambda_CB82():
        OP_95(0xFE, 400, 0, 6600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CB82)
    WaitChrThread(0x103, 1)

    def lambda_CBA0():
        OP_95(0xFE, 3500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CBA0)
    WaitChrThread(0x103, 1)

    def lambda_CBBE():
        OP_95(0xFE, 8500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CBBE)
    WaitChrThread(0x103, 1)
    Return()

    # Function_30_CB5F end

    def Function_31_CBD8(): pass

    label("Function_31_CBD8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05900.itc", 0x1E)
    OP_68(63800, 1000, 7900, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 59000, -1000, 3000, 90)
    SetChrPos(0x102, 59000, 0, 3400, 90)
    SetChrPos(0x104, 59000, 0, 3400, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 64599, 0, 7900, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 62900, 0, 7900, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    FadeToBright(1000, 0)
    OP_0D()
    Sound(811, 0, 100, 0)
    Sleep(500)

    #N0343
    NpcTalk(
        0x101,
        "ロイドの声",
        "#2P──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    OP_68(64000, 1000, 6900, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_CD5B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_CD5B)

    def lambda_CD68():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_CD68)
    SetChrPos(0x101, 59000, 0, 3400, 90)
    BeginChrThread(0x101, 3, 0, 32)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 34)

    #C0344
    ChrTalk(
        0x11,
        "#1005F#5Pおう、遅かったな。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x13,
        "#2202F#5Pやあ、お邪魔しているよ。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0346
    ChrTalk(
        0x101,
        "#12P#0002Fやっぱりイアン先生でしたか。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#0100F#12P珍しいですね。\x01",
            "先生がいらっしゃるなんて。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0348
    AnonymousTalk(
        0x13,
        (
            "ああ、セルゲイ君に\x01",
            "少し聞きたいことがあってね。\x02\x03",

            "他の用事もあったついでに\x01",
            "足を運んだというわけなんだ。\x02",
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

    #C0349
    ChrTalk(
        0x101,
        "#12P#0005F他の用事、ですか？\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        (
            "#1003F#5Pああ、端的に言うと\x01",
            "キーアの身元についてだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0351
    ChrTalk(
        0x101,
        "#12P#0013Fも、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#12P#0301F何か分かったんスか！？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x13,
        (
            "#2203F#5Pいや……残念ながら。\x02\x03",

            "#2201Fギルドにも依頼したそうだが\x01",
            "私もセルゲイ君に頼まれて、\x01",
            "他の可能性について調べていてね。\x02\x03",

            "#2203F残念だが──いや幸いと言うべきか\x01",
            "その可能性は無いと分かったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        "#12P#0005F他の可能性……ですか？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x11,
        (
            "#1003F#5Pああ……\x01",
            "数年前の話なんだがな。\x02\x03",

            "#1000Fカルバード共和国を中心に\x01",
            "子供が拉#2Rら#致#2Rち#される事件が\x01",
            "相次いだことがあったんだ。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0356
    ChrTalk(
        0x101,
        "#12P#0007F子供が拉致……！？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        "#0101F#12Pそ、それって……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0358
    ChrTalk(
        0x11,
        (
            "#1003F#5P詳細は省くが……\x01",
            "かなりのデカイ事件でな。\x02\x03",

            "カルバードだけじゃなく、\x01",
            "周辺諸国にも被害が及んでいた事から\x01",
            "国際的な捜査体制が組まれる事になった。\x02\x03",

            "#1001Fこの捜査体制には、各国の軍隊、\x01",
            "警察組織、そして遊撃士協会が協力した。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#12P#0001Fそんな事が……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        "#0106F#12P初めて聞きました……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#12P#0303F……俺も初耳だな。\x02\x03",

            "#0301Fあまり知られてないって事は\x01",
            "相当ヤバイ事件だったんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x13,
        (
            "#2203F#5Pああ……\x01",
            "結局、事件は解決したんだがね。\x02\x03",

            "かなり深刻な内容だったので\x01",
            "結局は極秘扱いになってしまった。\x02\x03",

            "#2201F私は民間のアドバイザーとして\x01",
            "偶然、関わっていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#12P#0011Fちょ、ちょっと待ってください。\x02\x03",

            "#0013Fもしかしてキーアが、\x01",
            "その数年前にあったという事件の\x01",
            "被害者である可能性が……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x13,
        (
            "#2201F#5Pそう思って、当時の被害を\x01",
            "改めて調べてみたんだが……\x02\x03",

            "キーア君に該当する子は\x01",
            "結局、見つからなかったんだ。\x02\x03",

            "#2203F事件を起こしていた連中も\x01",
            "殆んど検挙されるか自滅している。\x02\x03",

            "#2200Fその事が改めて分かったので\x01",
            "セルゲイ君に伝えに来たわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#12P#0006Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#0108F#12P少し安心しましたけど……\x01",
            "まさかそんな事件があったなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x11,
        (
            "#1003F#5P……ま、その事件については\x01",
            "いずれお前たちにも話してやる。\x02\x03",

            "#1001Fただ、結局キーアについては\x01",
            "振り出しに戻っちまったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        (
            "#12P#0302Fま、いいんじゃないッスか？\x02\x03",

            "身寄りが見つかるまで\x01",
            "俺たちが面倒見りゃいいんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x13,
        (
            "#2202F#5Pああ、当分の間は\x01",
            "ここで保護した方がいいだろう。\x02\x03",

            "#2210Fただ、本当に身寄りが無かった場合……\x02\x03",

            "#2200F里親を探すなり、教会の福音#4Rふくいん#施設に\x01",
            "預ける事も考えるべきかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        "#12P#0011Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        "#0108F#12P……で、でも………\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x11,
        (
            "#1003F#5Pいずれそういう事も含めて\x01",
            "考える必要があるってことだ。\x02\x03",

            "#1000F子供一人を預かって育てるってのは\x01",
            "ハンパな覚悟で出来る事じゃねぇ。\x02\x03",

            "どれだけその子が可愛くったってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        "#12P#0008Fそう、ですね……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        (
            "#12P#0306F確かに、猫の子を預かるのと\x01",
            "同じわけにはいかねぇか……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x13,
        (
            "#2202F#5Pはは、すまない。\x01",
            "厳しい事を言ってしまったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0376
    ChrTalk(
        0x13,
        (
            "#2205F#5Pそういえば、任務から\x01",
            "戻ってきたばかりみたいだな。\x02\x03",

            "#2202F報告もあるのだろうし、\x01",
            "私はそろそろ失礼させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        (
            "#12P#0000Fいえ、そんな。\x02\x03",

            "実は先生にも相談しようかと\x01",
            "思っていた案件だったんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0378
    ChrTalk(
        0x13,
        "#2205F#5Pほう、私に？\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        "#12P#0001Fええ、実は──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0380
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルゲイとイアン弁護士に\x01",
            "失踪していた鉱員の一件を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0381
    ChrTalk(
        0x11,
        (
            "#1004F#5Pなるほど……\x01",
            "そんな事がありやがったのか。\x02\x03",

            "#1002Fクク、いかにも\x01",
            "支援課らしい仕事じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#12P#0006F結局、事件ではなかったので\x01",
            "本人の説得はしませんでしたが……\x02\x03",

            "#0001F町に帰るよう説得くらいした方が\x01",
            "良かったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x11,
        (
            "#1003F#5Pふむ、難しいところだな。\x02\x03",

            "遊撃士だったら、説得や交渉も\x01",
            "仕事のうちに入るんだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x13,
        (
            "#2203F#5P警察の人間がそれをやった場合、\x01",
            "民事介入になる可能性もある……\x02\x03",

            "#2200Fなかなか難しい線引きの所だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        "#12P#0006Fやはりそうですか……\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#12P#0304Fま、いい歳した大人なんだし、\x01",
            "余計なお世話ってモンだろ。\x02\x03",

            "#0300Fこれでガキだったらケツでも叩いて\x01",
            "家に連れ戻してやるところだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#0102F#11Pふふ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x13,
        (
            "#2201F#5Pしかし天才的なギャンブルの腕と\x01",
            "別人のようなツキとカンか……\x02\x03",

            "#2203F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_64(0x13)
    Sleep(1000)
    TurnDirection(0x11, 0x13, 500)

    #C0389
    ChrTalk(
        0x11,
        (
            "#6P#1001F……先生？\x01",
            "何か心当たりでも？\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x13,
        (
            "#5P#2203Fいや、偶然かもしれないが……\x02\x03",

            "#2200Fここ最近、似たような話を\x01",
            "２つばかり聞いた事があってね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0391
    ChrTalk(
        0x101,
        "#12P#0001F本当ですか……？\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#12P#0307Fまさか他にも、ギャンブルで\x01",
            "一山当てたヤツがいるとか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x13,
        (
            "#2202F#5Pいやいや、そうじゃないよ。\x02\x03",

            "#2210F聞いた話というのは、\x01",
            "とある証券会社の証券マンと\x01",
            "貿易会社の経営者なんだがね。\x02\x03",

            "#2200Fどちらも最近、大きな損失を出して\x01",
            "非常に困っていたそうなんだが……\x02\x03",

            "ここ数日で、耳を疑うほどの\x01",
            "素晴らしい業績を上げたらしいんだ。\x02\x03",

            "#2203F特に証券マンの方は……\x01",
            "まるで未来が見えていたかのような\x01",
            "ツキとカンで株を売買したらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        "#12P#0005Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x104,
        "#12P#0301Fどこかで聞いた話だな……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x13,
        (
            "#2202F#5Pはは、もちろん\x01",
            "ただの偶然だろうけどね。\x02\x03",

            "#2210Fただ、聞くところによると\x01",
            "その２人の態度もあからさまに\x01",
            "横柄になったという話でね。\x02\x03",

            "#2200F少し気になってしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x102,
        "#0103F#12P確かに気になりますね……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x11,
        (
            "#6P#1003Fふむ……イアン先生。\x02\x03",

            "#1000Fその２人の身元について\x01",
            "詳しい情報は判りませんか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x11, 500)

    #C0399
    ChrTalk(
        0x13,
        (
            "#11P#2205Fああ、その気になれば\x01",
            "すぐに調べられるだろうが……\x02\x03",

            "#2200F念のため確かめておくかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x11,
        "#6P#1002Fええ、できれば。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#12P#0001F#12P課長……何か気がかりでも？\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)

    #C0402
    ChrTalk(
        0x11,
        (
            "#1006F#5Pま、こういう稼業をしてたら\x01",
            "情報は多いに越したことはねぇ。\x02\x03",

            "#1002Fただそれだけの話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#12P#0000Fなるほど……\x02\x03",

            "#0004F（兄貴も言ってたな……\x01",
            "  捜査の決め手は、カンと足による\x01",
            "  情報集めだって……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)

    #C0404
    ChrTalk(
        0x13,
        (
            "#2210F#5Pさてと、私はこれで失礼しよう。\x02\x03",

            "#2202F君たちも、気になる事があったら\x01",
            "いつでも相談してきてくれたまえ。\x02\x03",

            "出来る限りの協力をさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x101,
        (
            "#12P#0002Fイアン先生……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x102,
        (
            "#0104F#12Pその時はどうか\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x2, 0xFF, 0xFF)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_CBD8 end

    def Function_32_E5EB(): pass

    label("Function_32_E5EB")


    def lambda_E5F0():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5F0)

    def lambda_E60A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E60A)
    WaitChrThread(0x101, 1)

    def lambda_E61F():
        OP_95(0xFE, 63500, 30, 5600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E61F)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_E5EB end

    def Function_33_E640(): pass

    label("Function_33_E640")


    def lambda_E645():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E645)

    def lambda_E65F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E65F)
    WaitChrThread(0x102, 1)

    def lambda_E674():
        OP_95(0xFE, 64099, 30, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E674)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_E640 end

    def Function_34_E695(): pass

    label("Function_34_E695")


    def lambda_E69A():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E69A)

    def lambda_E6B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E6B4)
    WaitChrThread(0x104, 1)

    def lambda_E6C9():
        OP_95(0xFE, 62900, 30, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E6C9)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_E695 end

    def Function_35_E6EA(): pass

    label("Function_35_E6EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50411.itc", 0x1E)
    LoadChrToIndex("apl/ch50420.itc", 0x1F)
    LoadEffect(0x0, "event\\eva05_00.eff")
    OP_68(206000, 700, 123200, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x1F)
    SetChrPos(0x103, 208750, 50, 129400, 0)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x3)
    SetChrPos(0xD, 208900, 50, 128900, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 206000, 30, 123200, 180)
    BeginChrThread(0xF, 1, 0, 36)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis088.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis089.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFrame(0xFF, "t_huton", 0x0, 0x1)
    ClearMapObjFlags(0x22, 0x4)
    OP_7D(0xB3, 0xB3, 0xC7, 0x0, 0x0)
    OP_68(208800, 700, 129100, 7000)
    MoveCamera(45, 20, 0, 7000)
    SetCameraDistance(22500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(208800, 700, 129100, 0)
    MoveCamera(40, 29, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(20000, 4000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(64800, 1600, 7250, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 66600, 0, 6900, 90)
    OP_4B(0x11, 0xFF)
    SetChrPos(0x101, 62700, 0, 6900, 90)
    SetChrPos(0x102, 61400, 0, 6300, 90)
    SetChrPos(0x104, 61400, 0, 7500, 90)
    OP_68(64800, 1000, 7250, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    #C0407
    ChrTalk(
        0x11,
        (
            "#1003F#5P──そうか。\x01",
            "その名前が出てきたか。\x02\x03",

            "#1001F《真なる叡智#10Rグ ノ ー シ ス#》……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#0003F#6P……課長、教えてください。\x02\x03",

            "#0001F６年前に兄が関わったという、\x01",
            "ティオを拉致した教団について。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#6P#0101F当然……\x01",
            "課長はご存知なんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x104,
        (
            "#6P#0306F最初っからティオすけの事情を\x01",
            "知ってるような感じだったしな。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)
    OP_93(0x11, 0x10E, 0x190)
    Sleep(500)
    OP_68(64650, 900, 7570, 1300)

    def lambda_EB45():
        OP_95(0xFE, 65600, 0, 6900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_EB45)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0411
    ChrTalk(
        0x11,
        (
            "#1003F#11P──俺が知ってるのは当然だ。\x02\x03",

            "#1000F当時、ガイと共に\x01",
            "教団のロッジの一つを\x01",
            "制圧した当事者だったからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetCameraDistance(21500, 100000)

    #C0412
    ChrTalk(
        0x101,
        (
            "#0005F#6Pそ、そうだったんですか！？\x02\x03",

            "#0001Fそれじゃあ課長は、兄貴の──\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x11,
        (
            "#1004F#11P#11P直接の上司だった。\x02\x03",

            "#1006F……当時から俺は\x01",
            "ちょいとハミ出し気味でな。\x02\x03",

            "ある時、規格外の新人を\x01",
            "２人も押し付けられちまったんだ。\x02\x03",

            "#1002Fそのうちの一人が、お前の兄貴だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#0005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x11,
        (
            "#1002F#11P直情的で無鉄砲だったが……\x01",
            "ヤツは優秀な捜査官だったよ。\x02\x03",

            "#1004Fいい意味で、もう一人の新人と\x01",
            "好対照な組み合わせだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        (
            "#6P#0101Fもう一人の\x01",
            "新人の方というのは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x104,
        (
            "#6P#0305Fひょっとして\x01",
            "あの一課のダドリーとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x11,
        (
            "#1003F#11Pいや、ヤツは\x01",
            "生粋の一課上がりの男だ。\x02\x03",

            "俺が受け持った\x01",
            "もう一人の規格外の新人……\x02\x03",

            "#1002F──それはあの、\x01",
            "アリオス・マクレインだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0419
    ChrTalk(
        0x101,
        "#0011F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        "#6P#0105Fあの人、元は警察の……！？\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x11,
        (
            "#1003F#11P数年前に警察を辞め、\x01",
            "遊撃士に転向しちまったがな。\x02\x03",

            "#1000F警察が遊撃士協会に\x01",
            "微妙な距離感を持っている理由の\x01",
            "一つでもあると言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x104,
        "#6P#0306Fなんとまぁ……\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0006F#6P兄貴とアリオスさんが\x01",
            "同期の新人同士だったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x11,
        (
            "#1002F#11P年齢はアリオスの方が\x01",
            "２つばかり年上だったがな。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0425
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──既に結婚して、\x01",
            "娘も生まれたばかりのアリオスは\x01",
            "とにかく生真面目すぎる男だった。\x02\x03",

            "#30W一方ガイは、奔放で無鉄砲で、\x01",
            "とにかく前向きな馬鹿野郎だった。\x02\x03",

            "#30Wそんな２人だからこそ、\x01",
            "逆にウマが合ったんだろうな。\x02\x03",

            "#30Wわずか２年足らずで、\x01",
            "あいつらはクロスベル警察最強の\x01",
            "若手コンビと言われるようになった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis090.itp")

    #C0426
    ChrTalk(
        0x101,
        "#0008F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x102,
        (
            "#6P#0106Fた、確かにその２人なら\x01",
            "最強という言葉も判りますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x11,
        (
            "#1002F#11Pああ……\x01",
            "正直、俺も誇らしかったもんだ。\x02\x03",

            "そんな凄い部下どもを育てる\x01",
            "絶好の機会に恵まれたんだからな。\x02\x03",

            "#1004Fそうして俺たちの班は、\x01",
            "華々しい実績を打ち立てて行き……\x02\x03",

            "ついには一課に代わって\x01",
            "国際的な犯罪事件の合同捜査を\x01",
            "任されることになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        "#0005F#6P国際的な犯罪事件……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x104,
        "#6P#0301Fひょっとしてそいつが……\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x11,
        (
            "#1003F#11Pああ──例の“教団”だ。\x02\x03",
        )
    )
    
    CloseMessageWindow()
    
    AnonymousTalk(    #talk#5000
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルゲイはメモに文字と記号を書き記した。\x07\x00\x02",
        )
    )
    
    CloseMessageWindow()
    

    ChrTalk(     #talk#5001
        0x11,
        (
            "#1001F『Ｄ#2Rディー#∴Ｇ#2Rジー#教団』……\x01",
            "それが連中の正式名称らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        "#0013F#6P『Ｄ∴Ｇ教団』……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x104,
        "#6P#0301Fその∴ってのは何なんだよ？\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x102,
        (
            "#6P#0108F∴は『～ゆえに』を意味する\x01",
            "数学的な記号だけど……\x02\x03",

            "#0101F『Ｄ∴Ｇ』というのは\x01",
            "何を意味してるんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x11,
        (
            "#1003F#11P未だそれは不明だが……\x01",
            "そのうちの“Ｇ”に関しては\x01",
            "何とか突き止められている。\x02\x03",

            "#1001FＧ──すなわち\x01",
            "《真なる叡智#10Rグ ノ ー シ ス#》だ。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0436
    ChrTalk(
        0x101,
        "#0013F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#6P#0101Fヨアヒム先生が言っていた\x01",
            "悪魔の力を得る薬……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x104,
        "#6P#0307Fそう繋がんのかよ……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)

    #C0439
    ChrTalk(
        0x11,
        (
            "#1001F#11P事件が終結して６年あまり──\x02\x03",

            "#1003F多くの謎を残した宗教団体だが……\x01",
            "一つ確かに言えることがある。\x02\x03",

            "それは、ここ数十年で\x01",
            "最悪の組織犯罪を引き起こした\x01",
            "最低の連中だったってことだ。\x02\x03",

            "#1010F……各地で拉致した子供たちを\x01",
            "何十人と犠牲にしやがったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#0010F#6Pっ……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x102,
        "#6P#0108F昨日、イアン先生が言っていた……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0442
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W『Ｄ∴Ｇ教団』……\x02\x03",

            "#30W奴らはゼムリア大陸の各地で\x01",
            "１０以上の拠点#4Rロッジ#を持っていた。\x02\x03",

            "#30Wそして、それぞれのロッジで\x01",
            "様々な形での《儀式》を繰り返した。\x02\x03",

            "#30Wおぞましい悪魔召喚的なもの、\x01",
            "《古代遺物#8Rアーティファクト#》を利用したもの、\x01",
            "そして人体実験的なもの……\x02\x03",

            "#30Wそして、それらの儀式の時に\x01",
            "必ず使用されていたのが……\x02\x03",

            "#30W《グノーシス》という名の\x01",
            "正体不明の薬物だったという。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")

    #C0443
    ChrTalk(
        0x101,
        "#0008F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        (
            "#6P#0106F……その……\x01",
            "衝撃的すぎる話ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x104,
        (
            "#6P#0301Fそれで、事件はどんな風に\x01",
            "解決されたんスか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x11,
        "#1003F#11Pああ……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0447
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──昨日も言ったが、\x01",
            "被害が各国に広がっていた事から\x01",
            "国際的な捜査体制が設立された。\x02\x03",

            "#30W各国の軍、警察、ギルド関係者が\x01",
            "一堂に会する中……\x02\x03",

            "#30Wある高名な遊撃士の指揮により\x01",
            "各地のロッジを一斉検挙・制圧する\x01",
            "大規模な作戦が実行された。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0448
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30Wそして俺たち３名は、\x01",
            "共和国最西端、アルタイル市の\x01",
            "郊外にあるロッジの制圧を担当し……\x02\x03",

            "#30Wガイは、当時８歳だった\x01",
            "ティオ・プラトーを保護した。\x02\x03",

            "#30Wティオは衰弱しきっていたが、\x01",
            "まだマシな方だったのかもしれん。\x02\x03",

            "#30W……それ以外の子供たちが全員、\x01",
            "助からなかったというのもあるが……\x02\x03",

            "#30W他のロッジで試みられていた\x01",
            "おぞましい“儀式”に比べたら、\x01",
            "まだマシな扱われ方だったからだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)

    #C0449
    ChrTalk(
        0x101,
        "#0006F#6P……なんで………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0450
    ChrTalk(
        0x101,
        (
            "#0010F#6Pなんでそんな連中が\x01",
            "存在を許されてるんだ……ッ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        "#6P#0108F……吐き気がしてきたわ……\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x104,
        (
            "#6P#0303Fクロスベルにおける犯罪とは\x01",
            "ちょいと次元が違いすぎるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x11,
        (
            "#1003F#11Pまあな……\x02\x03",

            "#1001F──ただいずれにせよ、\x01",
            "６年前のその作戦をもって、\x01",
            "『教団』は完全に叩き潰された。\x02\x03",

            "信者たちは全員、自決するか\x01",
            "精神に破綻を来たして衰弱死した。\x02\x03",

            "残党もいたって話だが……\x01",
            "教会や例の《結社》とやらが動いて\x01",
            "密かに殲滅したっていう噂もある。\x02\x03",

            "#1003F『Ｄ∴Ｇ教団』の悪夢は\x01",
            "完全に終わったはずだった──\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        "#0008F#6Pですが……この『蒼い錠剤』。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    Sleep(500)

    #A0455
    AnonymousTalk(
        0x101,
        (
            "#0013Fこれがその教団が使っていた\x01",
            "『グノーシス』である可能性が\x01",
            "出てきたというわけですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0456
    AnonymousTalk(
        0x11,
        (
            "#1003F現時点では憶測の範囲だが……\x02\x03",

            "#1001Fもしそれが本当なら\x01",
            "６年前の悪夢が別の形で\x01",
            "引き起こされるかもしれん。\x02\x03",

            "それもマフィア同士の抗争を\x01",
            "巻き込むような形でな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0457
    ChrTalk(
        0x104,
        "#6P#0306F最悪すぎんだろ……\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそれが本当なら……\x01",
            "絶対に見過ごせません……！\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x11,
        "#1010F#11Pああ……もちろんだ。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)
    Sound(852, 0, 100, 0)
    Sleep(500)
    PlayEffect(0x0, 0x0, 0x11, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    #C0460
    ChrTalk(
        0x11,
        (
            "#1001F#11P──ロイド。\x02\x03",

            "３年前、お前の兄貴を殺った\x01",
            "犯人はいまだに見つかっていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        (
            "#0003F#6P……はい。\x02\x03",

            "#0001F何でも手がかりが少なすぎて\x01",
            "迷宮入りになってしまったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x11,
        (
            "#1006F#11Pああ……一課に移ってから\x01",
            "ヤツはもっぱら単独で捜査を\x01",
            "してたって話だからな。\x02\x03",

            "大国の諜報機関、ルバーチェ、\x01",
            "それとも全く別の犯罪組織……\x02\x03",

            "もしくはどこぞの猟兵団や\x01",
            "テロリストなんてのも考えられた。\x02\x03",

            "#1001Fだが──それ以外にも\x01",
            "俺の頭を掠めた可能性があった。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        "#0008F#6P『教団』の残党……ですね。\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x11,
        (
            "#1003F#11Pああ……今となっては\x01",
            "その可能性も現実味を帯びてきた。\x02\x03",

            "その意味では、俺にとっては\x01",
            "元部下の弔い合戦になるだろう。\x02\x03",

            "#1002Fお前らには悪いが、この先は\x01",
            "俺も出しゃばらせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#0005F#6P課長……\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#6P#0102Fわ、悪いどころか\x01",
            "すごく助かりますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#6P#0302Fつーか、まるで今まであえて\x01",
            "放任してたような口ぶりッスね？\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x11,
        (
            "#1004F#11Pクク、どうだかな……\x02\x03",

            "#1002Fただまあ、この特務支援課は\x01",
            "元々はガイのアイデアを参考に\x01",
            "設立したってのは確かだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0469
    ChrTalk(
        0x101,
        "#0005F#6Pそ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        (
            "#6P#0101Fギルドの評判に対抗するため\x01",
            "設立された部署だったのでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x11,
        (
            "#1002F#11Pそいつは上層部を\x01",
            "納得させるための口実だ。\x02\x03",

            "#1004F──生前、ガイのヤツが\x01",
            "俺に語っていた言葉がある。\x02\x03",

            "今のクロスベルに必要なのは\x01",
            "《壁》を乗り越える力だ……\x02\x03",

            "若いモンが失敗してもいいから\x01",
            "力を合わせて前に進める場所……\x02\x03",

            "#1002Fそれが警察には\x01",
            "必要なんじゃないかってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        "#0000F#6P兄貴が……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x104,
        (
            "#6P#0304Fやれやれ……\x01",
            "とんだ熱血アニキだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0474
    ChrTalk(
        0x102,
        (
            "#6P#0105Fもしかしてティオちゃんが\x01",
            "支援課に来たのも……？\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        "#0005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x11,
        (
            "#1003F#11Pああ、ガイの意志が息づく\x01",
            "場所に居たかったんだろう。\x02\x03",

            "本人からはっきりと\x01",
            "聞いたわけじゃないがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        "#0008F#6Pそうか……そうだったのか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0478
    ChrTalk(
        0x101,
        (
            "#0003F#6P兄貴の事はともかく……\x02\x03",

            "今は、この薬の被害を\x01",
            "食い止めることが先決です。\x02\x03",

            "#0013Fそれと、キーアですが……\x02\x03",

            "例の『教団』と何らかの\x01",
            "関わりがあるかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0479
    ChrTalk(
        0x102,
        "#6P#0101Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x104,
        (
            "#6P#0308Fチッ、そいつはありそうだな。\x02\x03",

            "記憶喪失の原因が\x01",
            "薬物って話もあったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x11,
        (
            "#1001F#11Pああ……\x01",
            "俺もそう睨み始めている。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        (
            "#0004F#6Pですから課長……\x02\x03",

            "#0000F動くのは俺たちに任せて\x01",
            "課長はここでキーアを\x01",
            "守ってやってくれませんか？\x02\x03",

            "一課との連携もありますし、\x01",
            "俺たちには司令役が必要なんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0483
    ChrTalk(
        0x11,
        "#1005F#11Pほう……\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        "#6P#0105Fた、確かに……\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x104,
        (
            "#6P#0303F誰かが支援課に\x01",
            "詰めとく必要はありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#0006F#6P……すみません。\x02\x03",

            "せっかくの申し出なのに、\x01",
            "生意気なことを言ってしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x11,
        (
            "#1009F#11Pクク……いや。\x02\x03",

            "#1004F──いいだろう、引き受けた。\x02\x03",

            "#1001Fただし今まで通り、\x01",
            "わざわざ俺から指示は与えん。\x02\x03",

            "相談にはいくらでも乗るし、\x01",
            "各方面と連絡も取ってやるが……\x02\x03",

            "お前たち自身が判断して\x01",
            "今回の事件を解決してみせろ。\x02\x03",

            "#1002Fどうだ、やれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        "#0000F#6Pはい……！\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x102,
        "#6P#0100F了解しました！\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        (
            "#6P#0304Fやれやれ、明日から\x01",
            "鬼のように忙しくなりそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x0)
    StopBGM(0x1388)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(2000)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5D, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_E6EA end

    def Function_36_10EA0(): pass

    label("Function_36_10EA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10EBE")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_36_10EA0")

    label("loc_10EBE")

    Return()

    # Function_36_10EA0 end

    def Function_37_10EBF(): pass

    label("Function_37_10EBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00150.itc", 0x1E)
    LoadChrToIndex("chr/ch00151.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch08700.itc", 0x24)
    LoadChrToIndex("chr/ch08702.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31350.itc", 0x28)
    LoadChrToIndex("chr/ch31351.itc", 0x29)
    LoadChrToIndex("apl/ch50090.itc", 0x2A)
    LoadChrToIndex("apl/ch50011.itc", 0x2B)
    LoadChrToIndex("apl/ch50539.itc", 0x2C)
    LoadChrToIndex("apl/ch50506.itc", 0x2D)
    LoadChrToIndex("chr/ch02751.itc", 0x2E)
    LoadChrToIndex("chr/ch02752.itc", 0x2F)
    LoadChrToIndex("chr/ch10600.itc", 0x30)
    LoadChrToIndex("chr/ch10601.itc", 0x31)
    LoadChrToIndex("chr/ch10700.itc", 0x32)
    LoadChrToIndex("chr/ch10701.itc", 0x33)
    LoadChrToIndex("chr/ch00952.itc", 0x34)
    LoadChrToIndex("apl/ch50509.itc", 0x35)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "event\\ev608_00.eff")
    LoadEffect(0x2, "battle\\btgun00.eff")
    LoadEffect(0x3, "event\\eva01_00.eff")
    SoundLoad(821)
    OP_68(500, 900, 2500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 63800, 30, 8500, 0)
    SetChrPos(0x101, 63000, 0, 5700, 0)
    SetChrPos(0x102, 64300, 0, 5700, 0)
    SetChrPos(0x103, 63200, 0, 4400, 0)
    SetChrPos(0x104, 64500, 0, 4400, 0)
    SetChrPos(0x10A, 65200, 0, 8300, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 11300, 900, 6650, 90)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 500, 0, 2500, 180)
    BeginChrThread(0xF, 1, 0, 36)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13900, 900, 6650, 270)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x28)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x19)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13200, 1300, 6600, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x19)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12200, 1300, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(12600, 1770, 6600, 7000)
    FadeToBright(2000, 0)
    Sleep(3000)
    OP_63(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x14, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(64000, 1100, 7600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    Sound(818, 0, 80, 0)
    Sleep(200)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0491
    AnonymousTalk(
        0x10A,
        (
            "#0607Fクッ……\x01",
            "何を考えている！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)

    #C0492
    ChrTalk(
        0x10A,
        (
            "#11P#0610Fヨアヒム・ギュンター……\x01",
            "一体どういうつもりだ！？\x02\x03",

            "どうして自分が不利になる情報を\x01",
            "わざわざ残したりする！？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x11,
        "#1003F#11Pフン、確かにな……\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    #C0494
    ChrTalk(
        0x11,
        (
            "#1001F#5P──お前たち。\x01",
            "偽装の可能性はどう思う？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11359():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_11359)

    #C0495
    ChrTalk(
        0x101,
        (
            "#12P#0006F……正直、この状況で\x01",
            "偽装する意味はないと思います。\x02\x03",

            "#0013F全ての状況が彼を指し示し、\x01",
            "ルバーチェや議長との関係も\x01",
            "明らかにされていますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#0101F《銀#2Rイン#》の行動を見る限り、\x01",
            "黒月や共和国派の仕掛けの可能性も\x01",
            "低いのではないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x104,
        (
            "#0306Fま、これ見よがしに\x01",
            "誇示してるだけじゃねぇのか？\x02\x03",

            "#0301Fあの秘書野郎の態度だって\x01",
            "かなりイッちまった感じだったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        (
            "#12P#0206F……同感です。\x02\x03",

            "#0208Fその２つのファイルからは\x01",
            "自己顕示欲と合わせて、何らかの\x01",
            "狂信的なメッセージを感じました。\x02\x03",

            "#0201Fそれも恐らく、キーアについて……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x11,
        (
            "#1006F#5Pなるほどな……\x02\x03",

            "#1001F……そこまで拘#2Rこだわ#らせる何かを\x01",
            "あの子が持っているのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x10A,
        (
            "#11P#0602Fば、馬鹿馬鹿しい……\x01",
            "ただの能天気な子供でしょう！？\x02\x03",

            "こんな事をしてまで\x01",
            "一体何をしようって言うんです！？\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x11,
        (
            "#1003F#5Pさてな……\x02\x03",

            "#1001Fだが、この白いファイルに\x01",
            "彼女の写真が挟まっていた事の意味……\x02\x03",

            "──ロイド、どう思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x101,
        (
            "#12P#0003F……はい。\x02\x03",

            "#0008F６年前までに行われていた\x01",
            "幾つもの非道な“儀式”の数々……\x02\x03",

            "#0001Fその締めくくりとして\x01",
            "キーアを利用するという\x01",
            "メッセージかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x102,
        "#0101Fっ……\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x104,
        "#0310Fチッ……\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x103,
        "#12P#0208F……絶対にさせません……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x101,
        "#12P#0003Fああ……もちろんだ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0507
    ChrTalk(
        0x101,
        (
            "#6P#0013F──ダドリーさん。\x01",
            "上層部の方はどうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x10A,
        (
            "#0606F#5P……間が悪いことに\x01",
            "例の拘置所襲撃の報せがあってな。\x02\x03",

            "しかも拘置所の近くにあった\x01",
            "警察学校と訓練場も襲われたらしい。\x02\x03",

            "#0601Fそちらへの対応で警察本部は\x01",
            "蜂の巣を突#2Rつつ#いたようになっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        (
            "#6P#0006F分かりました……\x01",
            "これ以上はアテには出来ません。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0510
    ChrTalk(
        0x101,
        (
            "#12P#0001F──遊撃士協会に頼んで\x01",
            "キーアを外国に逃がしましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_11A0E():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11A0E)
    Sleep(50)

    def lambda_11A1E():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11A1E)
    Sleep(50)

    def lambda_11A2E():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11A2E)
    WaitChrThread(0x102, 2)

    #C0511
    ChrTalk(
        0x102,
        "#0105F#11Pロイド、それは……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        (
            "#12P#0003Fもちろんアリオスさんか、\x01",
            "エステルたちに任せる事が条件だ。\x02\x03",

            "#0000Fリベールあたりなら安全だろうし、\x01",
            "《教団》の手も届きにくいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x11,
        (
            "#1003F#5Pフン……確かにそいつが\x01",
            "一番安全かもしれんな。\x02\x03",

            "#1000F──だが、いいのか？\x02\x03",

            "お前自身の手で\x01",
            "あの子を守れなくなっても。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x101,
        (
            "#12P#0006F……俺の拘りやプライドなんて\x01",
            "どうでもいいんです。\x02\x03",

            "#0008Fみんなは反対かもしれないけど……\x02\x03",

            "#0001Fあの子が少しでも安全なら\x01",
            "俺はそちらの可能性に賭けたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x103,
        "#12P#0205Fロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        "#0306Fやれやれ……仕方ねぇか。\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x10A,
        (
            "#0603F#5P……そのつもりなら\x01",
            "急いだ方が良さそうだな。\x02\x03",

            "#0600F国際定期船の最終便は\x01",
            "確か９：３０だったはずだ。\x02\x03",

            "急げば今夜中にリベールへ\x01",
            "あの子を逃がせるかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x11,
        (
            "#1003F#5Pよし、ギルドに連絡しろ。\x02\x03",

            "#1002Fアリオスあたりが戻っていたら\x01",
            "そのまま任せればいい。\x02\x03",

            "ヤツなら娘とキーアの２人、\x01",
            "何があっても守り切れるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x101,
        "#12P#0000Fはい……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Sleep(300)
    Sound(902, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はいはい、こちら遊撃士協会、\x01",
            "クロスベル支部よ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0521
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001Fミシェルさん。\x01",
            "支援課のロイドです。\x02\x03",

            "今、よろしいですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あら、坊やだったの。\x02\x03",

            "どうしたの？\x01",
            "ウチのメンバーはまだ\x01",
            "戻ってきてないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0523
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fそ、そうですか……\x02\x03",

            "#0001Fアリオスさんあたりが\x01",
            "いつ戻るか分かりませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、彼ならそろそろ\x01",
            "戻ってくるはずだけど──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0x1388)
    Sound(955, 0, 100, 0)
    Sleep(2000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0525
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Sなっ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("ミシェルの声")

    #A0526
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2Sなんなの、アンタたち！？\x01",
            "ここは遊撃士協会#10Rブレイサーギルド#──\x02",
        )
    )

    CloseMessageWindow()
    Sound(531, 0, 60, 0)
    Sleep(300)
    SetChrName("ミシェルの声")

    #A0527
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S……くっ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    Sound(356, 0, 70, 0)
    Sleep(1100)
    Sound(356, 0, 60, 0)
    Sleep(500)
    OP_24(0x164)
    Sound(825, 0, 100, 0)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0528
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F！！！\x02\x03",

            "#0007Fミシェルさん！？\x01",
            "どうしたんですか！？\x02\x03",

            "#0010F（……ダメだ。\x01",
            "  通信器がやられたのか……！？）\x02",
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

    #C0529
    ChrTalk(
        0x10A,
        "#0605F#5Pおい、何があった……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)

    #C0530
    ChrTalk(
        0x101,
        (
            "#12P#0003F……遊撃士協会が\x01",
            "何者かに襲撃されたみたいです。\x02\x03",

            "#0013F通信が切れる直前に\x01",
            "機関銃の音がしていました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0531
    ChrTalk(
        0x102,
        "#0105F#11Pなっ……\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        (
            "#0307Fまさか操られた\x01",
            "マフィアどもか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x11,
        (
            "#1001F#5Pフン……\x01",
            "可能性は高そうだな。\x02",
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
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0534
    ChrTalk(
        0x101,
        (
            "#12P#0013Fいや、その……\x02\x03",

            "マフィアの襲撃にしては\x01",
            "ちょっと気になることが……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x11,
        "#1005F#5Pなに……？\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        "#12P#0008F（そうだ、違和感があったのは……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【機関銃の音】\x01",                  # 0
            "【ミシェルの反応】\x01",              # 1
            "【通信が切れたタイミング】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12455"),
        (1, "loc_124D7"),
        (2, "loc_12541"),
        (SWITCH_DEFAULT, "loc_125A7"),
    )


    label("loc_12455")

    OP_2C(0x4E, 0x1)

    #C0537
    ChrTalk(
        0x101,
        (
            "#12P#0003F（そうだ……\x01",
            "  あれはマフィアが使っていた\x01",
            "  重機関銃の音じゃなかった。）\x02\x03",

            "#0013F（どういうことだ……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125A7")

    label("loc_124D7")


    #C0538
    ChrTalk(
        0x101,
        (
            "#12P#0006F（いや、あの状況からしたら\x01",
            "  当然の反応だったはず……）\x02\x03",

            "#0008F（いったい何が……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125A7")

    label("loc_12541")


    #C0539
    ChrTalk(
        0x101,
        (
            "#12P#0006F（いや、タイミング的には\x01",
            "  特におかしくはない……）\x02\x03",

            "#0008F（いったい何が……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125A7")

    label("loc_125A7")

    Sound(821, 2, 80, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0540
    ChrTalk(
        0x101,
        (
            "#11P#0005Fこの音は……\x01",
            "向こうの通信器？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x102,
        "#0101F#11P早く出ましょう！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(14200, 1750, 5000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 19500, 850, 4000, 270)
    SetChrPos(0x102, 19500, 850, 4000, 270)
    SetChrPos(0x103, 19500, 850, 4000, 270)
    SetChrPos(0x104, 19500, 850, 4000, 270)
    SetChrPos(0x10A, 19500, 850, 4000, 270)
    SetChrPos(0x11, 19500, 850, 4000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x1F, 0x1000)
    OP_70(0x1F, 0x0)
    OP_74(0x1F, 0x1E)
    OP_71(0x1F, 0x0, 0x14, 0x0, 0x20)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    OP_0D()
    OP_25(0x335, 0x64)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)
    SetChrSubChip(0xD, 0x2)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)
    Sleep(250)

    #C0542
    ChrTalk(
        0xD,
        (
            "#1105Fあ、ロイドー。\x02\x03",

            "つーしんきが\x01",
            "鳴ってるよ～？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(13800, 1750, 11000, 3000)
    BeginChrThread(0xD, 3, 0, 49)
    Sleep(500)

    #C0543
    ChrTalk(
        0x101,
        "#0013F#11Pああ、すぐに出る！\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#0102F#11Pごめんね、シズクちゃん。\x01",
            "うるさくしちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x14,
        (
            "#6008F#12Pい、いえ……\x01",
            "……何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)
    ClearMapObjFlags(0x1F, 0x20)
    OP_70(0x1F, 0x32)
    OP_24(0x335)
    Sound(822, 0, 100, 0)
    FadeToDark(500, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0546
    AnonymousTalk(
        0x101,
        "#0013Fはい、特務支援課です！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("娘の声")

    #A0547
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あっ、ロイドさん！？\x02\x03",

            "よ、よかった！\x01",
            "無事に繋がって……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0548
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fその声は……ノエル曹長か？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、先ほどはどうも！\x02\x03",

            "──実はロイドさんたちに\x01",
            "お伝えする事があるんです！\x02\x03",

            "ベルガード門の部隊との連絡が\x01",
            "完全に途絶しました……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0550
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0007F何だって……！？\x02\x03",

            "#0010F一体、何があったんだ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0551
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "わ、分かりません。\x01",
            "こちらも現在確認中で……\x02\x03",

            "一応、そちらにも伝えるよう\x01",
            "副司令に指示されました！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0552
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F分かった、情報感謝する！\x02\x03",

            "#0005Fそうだ──\x01",
            "こちらも伝える事があるんだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0553
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士協会が襲撃されたらしい事を\x01",
            "手短にノエル曹長に伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0554
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "市内でギルドが……！？\x02\x03",

            "分かりました！\x01",
            "副司令に伝えておきます！\x02\x03",

            "何が起きているのか分かりません！\x01",
            "くれぐれも気をつけて……！\x02",
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
            "#0013Fああ、そちらこそ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    SetMapObjFlags(0x1F, 0x4)
    Sound(822, 0, 100, 0)
    Sleep(500)

    #C0556
    ChrTalk(
        0x11,
        "#6P#1001F警備隊方面で何があった？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(150)

    #C0557
    ChrTalk(
        0x101,
        (
            "#5P#0006Fベルガード門の部隊との連絡が\x01",
            "完全に途絶したそうです……\x02\x03",

            "#0013F今、現状を確認中との事でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x10A,
        "#6P#0605Fなんだと……！？\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x102,
        "#0101F#12Pい、一体何が……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(2048, 255, 100, 0)    #voice#Zeit
    Sleep(1000)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0xF, 0x2F)
    SetChrSubChip(0xF, 0x3)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_12DD0():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_12DD0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_12E82():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12E82)

    def lambda_12E8F():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12E8F)

    def lambda_12E9C():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12E9C)

    def lambda_12EA9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12EA9)

    def lambda_12EB6():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_12EB6)

    def lambda_12EC3():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_12EC3)
    SetChrSubChip(0x14, 0x1)
    SetChrSubChip(0xD, 0x2)
    OP_68(500, 1000, 2500, 2000)
    OP_6F(0x1)

    #C0560
    ChrTalk(
        0x101,
        "#0005Fツァイト……！？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x104,
        (
            "#0301Fなんだ……\x01",
            "外に何かいるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xF,
        "#5P#1201Fグルルルル……ウォン！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(13800, 1750, 11000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0xD, 11300, 900, 6400, 180)
    EndChrThread(0xF, 0x2)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0563
    ChrTalk(
        0x103,
        "#5P#0205F『囲まれてる、気をつけろ』！？\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xD,
        (
            "#1101F#11Pなんか集まってきてるって\x01",
            "言ってるみたい～。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_130CA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_130CA)

    def lambda_130D7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_130D7)
    Sleep(50)

    def lambda_130E7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_130E7)

    def lambda_130F4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_130F4)
    Sleep(50)

    def lambda_13104():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_13104)
    SetChrSubChip(0x14, 0x0)
    WaitChrThread(0x10A, 2)
    SetChrSubChip(0x14, 0x2)
    Sleep(50)
    Fade(250)
    SetChrPos(0xD, 11300, 900, 6650, 90)
    SetChrSubChip(0xD, 0x1)
    OP_0D()

    #C0565
    ChrTalk(
        0x101,
        "#0013F#5P本当か……！？\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x102,
        (
            "#0101F#11Pひょっとして……\x01",
            "遊撃士協会を襲撃した！？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0567
    ChrTalk(
        0x11,
        (
            "#6P#1010Fフン……\x01",
            "間違いなさそうだな。\x02\x03",

            "#1001F──総員、脱出の準備を。\x02\x03",

            "ロイドとランディは\x01",
            "キーアとシズクを連れていけ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1321F():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1321F)
    Sleep(50)

    def lambda_1322F():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1322F)
    Sleep(50)
    TurnDirection(0x10A, 0x11, 500)

    #C0568
    ChrTalk(
        0x101,
        "#5P#0007Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x104,
        "#0307F#11Pアイ・サー！\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x11,
        (
            "#6P#1003Fティオは周囲の警戒を。\x01",
            "エリィはフォローに回れ。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x103,
        "#11P#0201Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        "#0101F#11P了解しました！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x11, 0x10A, 500)

    #C0573
    ChrTalk(
        0x11,
        (
            "#12P#1001Fダドリー。\x01",
            "しんがりは俺とお前で持つぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x10A,
        "#5P#0601F了解です……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(13800, 1750, 8900, 2500)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 48)
    Sleep(200)

    def lambda_133B6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_133B6)
    Sleep(50)

    def lambda_133C6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_133C6)
    Sleep(50)

    def lambda_133D6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_133D6)
    Sleep(50)
    WaitChrThread(0x101, 3)

    def lambda_133EA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_133EA)
    OP_6F(0x1)

    #C0575
    ChrTalk(
        0x101,
        (
            "#0000F#5Pキーア。\x01",
            "しっかり掴まっててくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xD,
        (
            "#12P#1110F#Nうんっ！\x01",
            "えへへ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x104, 3)

    #C0577
    ChrTalk(
        0x104,
        (
            "#5P#0304Fシズクちゃん。\x01",
            "失礼させてもらうぜ。\x02\x03",

            "#0300Fオヤジさんに比べりゃ\x01",
            "物足りねぇだろうが勘弁な。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x14,
        (
            "#12P#6002Fそんな事……\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    def lambda_13536():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13536)
    Sleep(50)

    def lambda_13546():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13546)
    WaitChrThread(0x104, 2)
    Sleep(200)

    #C0579
    ChrTalk(
        0x11,
        (
            "#1001F#5Pよし……\x01",
            "なるべく陣形を崩さすに──\x02",
        )
    )

    CloseMessageWindow()
    Sound(921, 0, 80, 0)
    Sleep(200)
    SetCameraDistance(29000, 3000)
    OP_82(0x384, 0x384, 0xBB8, 0xBB8)
    Sound(356, 0, 100, 0)
    Sound(956, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 46)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Sound(539, 0, 100, 0)
    BeginChrThread(0x11, 2, 0, 46)
    Sleep(500)
    Sound(356, 0, 100, 0)
    Sound(956, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(500)
    Sound(539, 0, 100, 0)
    Sleep(400)
    Sound(153, 0, 100, 0)
    Sound(356, 0, 100, 0)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_6F(0x10)
    CancelBlur(0)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    OP_7D(0xB3, 0xB3, 0xC7, 0x0, 0x0)
    SetMapObjFrame(0xFF, "floor02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02_wood", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02_sd", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02_dankon", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor01_wood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white_sd", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd00", 0x0, 0x1)
    OP_68(13800, 1750, 8900, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x15, 15200, 850, -1800, 0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 10200, 850, -1800, 0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_68(12700, 1750, 10000, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x102, 15000, 850, 10300, 180)
    SetChrPos(0x103, 13300, 850, 9800, 180)
    SetChrPos(0x10A, 10300, 850, 10300, 180)
    SetChrPos(0x11, 11900, 850, 9300, 180)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(12700, 1750, 8000, 2000)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 16777215)
    Sleep(1000)
    Sound(854, 0, 100, 0)
    Sound(921, 0, 100, 0)
    BeginChrThread(0x15, 3, 0, 44)
    Sleep(100)
    BeginChrThread(0x16, 3, 0, 45)
    OP_6F(0x11)

    #C0580
    ChrTalk(
        0x101,
        "#0011F#5Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x102,
        "#11P#0107Fけ、警備隊……！？\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x15,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x16,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#35W………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#1007F行くぞ！\x01",
            "裏口から撤退する！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(11300, 1750, 11000, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_68(6300, 1750, 11000, 3000)
    BeginChrThread(0x15, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 43)
    BeginChrThread(0x11, 3, 0, 39)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 42)
    BeginChrThread(0x10A, 3, 0, 40)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x16, 3, 0, 38)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(1350)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x11, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    OP_24(0x335)
    SetScenarioFlags(0x5C, 0)
    NewScene("c020B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_10EBF end

    def Function_38_13A8B(): pass

    label("Function_38_13A8B")

    Sleep(700)
    Sound(356, 0, 100, 0)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9700, 870, 8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8700, 870, 11800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8100, 870, 8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 5900, 470, 7400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 6100, 870, 11300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_38_13A8B end

    def Function_39_13BBA(): pass

    label("Function_39_13BBA")

    SetChrChipByIndex(0x11, 0x35)
    SetChrSubChip(0x11, 0x4)
    Sleep(900)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x11, 0x5)
    Sleep(200)
    SetChrSubChip(0x11, 0x6)
    Sleep(100)
    SetChrSubChip(0x11, 0x7)
    Sleep(100)
    SetChrSubChip(0x11, 0x4)
    Sleep(100)
    SetChrSubChip(0x11, 0x3)
    Sleep(70)
    SetChrSubChip(0x11, 0x2)
    Sleep(70)
    SetChrSubChip(0x11, 0x1)
    Sleep(70)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x11, 0x0)
    Sleep(70)
    SetChrSubChip(0x11, 0x1)
    Sleep(70)
    SetChrSubChip(0x11, 0x2)
    Sleep(70)
    SetChrSubChip(0x11, 0x3)
    Sleep(70)
    SetChrSubChip(0x11, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x11, 0x5)
    Sleep(200)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x11, 0x6)
    Sleep(100)
    SetChrSubChip(0x11, 0x7)
    Sleep(100)
    SetChrSubChip(0x11, 0x4)
    Sleep(100)
    Return()

    # Function_39_13BBA end

    def Function_40_13CBC(): pass

    label("Function_40_13CBC")

    SetChrChipByIndex(0x10A, 0x34)
    SetChrSubChip(0x10A, 0x0)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Return()

    # Function_40_13CBC end

    def Function_41_13DE5(): pass

    label("Function_41_13DE5")


    def lambda_13DEA():
        OP_95(0xFE, 11000, 850, 11400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13DEA)
    WaitChrThread(0xFE, 1)

    def lambda_13E08():
        OP_95(0xFE, 9300, 850, 10400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13E08)
    WaitChrThread(0xFE, 1)

    def lambda_13E26():
        OP_95(0xFE, 1600, 850, 10400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13E26)
    WaitChrThread(0xFE, 1)

    def lambda_13E44():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13E44)
    Sleep(500)

    def lambda_13E61():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13E61)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_13DE5 end

    def Function_42_13E76(): pass

    label("Function_42_13E76")


    def lambda_13E7B():
        OP_95(0xFE, 9500, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13E7B)
    WaitChrThread(0xFE, 1)

    def lambda_13E99():
        OP_95(0xFE, 1600, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13E99)
    WaitChrThread(0xFE, 1)

    def lambda_13EB7():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13EB7)
    Sleep(500)

    def lambda_13ED4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13ED4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_13E76 end

    def Function_43_13EE9(): pass

    label("Function_43_13EE9")


    def lambda_13EEE():
        OP_95(0xFE, 13500, 870, 8600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13EEE)
    WaitChrThread(0x104, 1)

    def lambda_13F0C():
        OP_95(0xFE, 9500, 850, 8600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13F0C)
    WaitChrThread(0x104, 1)

    def lambda_13F2A():
        OP_95(0xFE, 1600, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13F2A)
    WaitChrThread(0x104, 1)

    def lambda_13F48():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13F48)
    Sleep(500)

    def lambda_13F65():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13F65)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    Return()

    # Function_43_13EE9 end

    def Function_44_13F7A(): pass

    label("Function_44_13F7A")

    SetChrChip(0x0, 0x15, 0x1E, 0x12C)
    SetChrChipByIndex(0x15, 0x27)
    SetChrSubChip(0x15, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 15200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_13FD1():
        OP_9D(0xFE, 0x3B60, 0x352, 0x898, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13FD1)

    def lambda_13FEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_13FEE)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x0)
    Sound(58, 0, 100, 0)
    Sound(31, 0, 100, 0)
    Sleep(300)
    SetChrChip(0x1, 0x15, 0x0, 0x0)
    Return()

    # Function_44_13F7A end

    def Function_45_1401E(): pass

    label("Function_45_1401E")

    SetChrChip(0x0, 0x16, 0x1E, 0x12C)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x2)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14075():
        OP_9D(0xFE, 0x27D8, 0x352, 0x898, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_14075)

    def lambda_14092():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_14092)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x28)
    SetChrSubChip(0x16, 0x0)
    Sound(59, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    SetChrChip(0x1, 0x16, 0x0, 0x0)
    Return()

    # Function_45_1401E end

    def Function_46_140C2(): pass

    label("Function_46_140C2")

    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 10200, 870, 5700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12500, 1470, 4700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10200, 870, 5700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 17600, 870, 8400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15300, 870, 3800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 17600, 870, 8400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12900, 1470, 4800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 10300, 870, 3700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10300, 870, 3700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9900, 870, 11500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 17100, 1470, 10500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16900, 1470, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 16900, 1470, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9200, 1270, 6000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8000, 870, 5300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14000, 870, 5800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8000, 870, 5300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15100, 870, 5600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12600, 1470, 3100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 15100, 870, 5600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11700, 1470, 5100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 870, 6900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 15600, 870, 6900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16100, 870, 8300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9700, 870, 9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9500, 870, 10500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 9500, 870, 10500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12900, 1470, 6600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9900, 870, 4500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16800, 870, 5900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 16800, 870, 5900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_46_140C2 end

    def Function_47_14796(): pass

    label("Function_47_14796")


    def lambda_1479B():
        OP_95(0xFE, 11300, 870, 7900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1479B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_47_14796 end

    def Function_48_147BC(): pass

    label("Function_48_147BC")

    OP_92(0x104, 0x3778, 0x1EDC, 0x1F4)

    def lambda_147CE():
        OP_95(0xFE, 14200, 870, 7900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_147CE)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_48_147BC end

    def Function_49_147EF(): pass

    label("Function_49_147EF")

    BeginChrThread(0x101, 3, 0, 50)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 51)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 52)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 53)
    Sleep(500)
    BeginChrThread(0x10A, 3, 0, 54)
    Sleep(500)
    BeginChrThread(0x11, 3, 0, 55)
    Sleep(1000)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x11, 3)
    Return()

    # Function_49_147EF end

    def Function_50_14853(): pass

    label("Function_50_14853")


    def lambda_14858():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14858)

    def lambda_14869():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14869)
    WaitChrThread(0x101, 1)

    def lambda_14887():
        OP_95(0xFE, 13800, 850, 12000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14887)
    Sleep(300)
    SetChrSubChip(0xD, 0x0)
    Sleep(100)
    SetChrSubChip(0x14, 0x1)
    Sleep(300)
    SetChrSubChip(0xD, 0x1)
    Sleep(100)
    SetChrSubChip(0x14, 0x2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_50_14853 end

    def Function_51_148C4(): pass

    label("Function_51_148C4")


    def lambda_148C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_148C9)

    def lambda_148DA():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_148DA)
    WaitChrThread(0x102, 1)

    def lambda_148F8():
        OP_95(0xFE, 14500, 850, 10300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_148F8)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_51_148C4 end

    def Function_52_14919(): pass

    label("Function_52_14919")


    def lambda_1491E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1491E)

    def lambda_1492F():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1492F)
    WaitChrThread(0x103, 1)

    def lambda_1494D():
        OP_95(0xFE, 13300, 850, 9800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1494D)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_52_14919 end

    def Function_53_1496E(): pass

    label("Function_53_1496E")


    def lambda_14973():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14973)

    def lambda_14984():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14984)
    WaitChrThread(0x104, 1)

    def lambda_149A2():
        OP_95(0xFE, 15300, 850, 9800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_149A2)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    Return()

    # Function_53_1496E end

    def Function_54_149C3(): pass

    label("Function_54_149C3")


    def lambda_149C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_149C8)

    def lambda_149D9():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_149D9)
    WaitChrThread(0x10A, 1)

    def lambda_149F7():
        OP_95(0xFE, 15500, 850, 7000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_149F7)
    WaitChrThread(0x10A, 1)

    def lambda_14A15():
        OP_95(0xFE, 11000, 850, 10300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_14A15)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x2D, 0x1F4)
    Return()

    # Function_54_149C3 end

    def Function_55_14A36(): pass

    label("Function_55_14A36")


    def lambda_14A3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14A3B)

    def lambda_14A4C():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14A4C)
    WaitChrThread(0x11, 1)

    def lambda_14A6A():
        OP_95(0xFE, 15500, 850, 7000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14A6A)
    WaitChrThread(0x11, 1)

    def lambda_14A88():
        OP_95(0xFE, 11400, 850, 9300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14A88)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x2D, 0x1F4)
    Return()

    # Function_55_14A36 end

    def Function_56_14AA9(): pass

    label("Function_56_14AA9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B1B")

    #C0585
    ChrTalk(
        0x101,
        (
            "#0001Fこっちは外か。\x01",
            "風が気持ち良さそうだけど……\x02\x03",

            "#0006F……今はみんなの話を\x01",
            "聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B7E")

    #C0586
    ChrTalk(
        0x101,
        (
            "#0008Fエリィ、外に出たのか……？\x02\x03",

            "#0001Fいや、まずは\x01",
            "支援課の中を探してみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BCF")

    #C0587
    ChrTalk(
        0x101,
        (
            "#0000Fイアン先生が訪ねてきてるみたいだ。\x01",
            "一応挨拶しておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BCF")

    Sleep(50)
    SetChrPos(0x0, 1000, 0, 970, 0)
    EventEnd(0x4)
    Return()

    # Function_56_14AA9 end

    def Function_57_14BE6(): pass

    label("Function_57_14BE6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C3B")

    #C0588
    ChrTalk(
        0x101,
        (
            "#0005Fここは裏口……？\x02\x03",

            "#0000Fまあ、今は\x01",
            "外に出る必要はないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C9E")

    #C0589
    ChrTalk(
        0x101,
        (
            "#0008Fエリィ、外に出たのか……？\x02\x03",

            "#0001Fいや、まずは\x01",
            "支援課の中を探してみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C9E")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_57_14BE6 end

    def Function_58_14CB5(): pass

    label("Function_58_14CB5")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D24")

    #C0590
    ChrTalk(
        0x101,
        (
            "#0000F……だめだ。\x01",
            "なんか煮詰まってきた……\x02\x03",

            "ちょっと外の風に当たるか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_14D7F")

    label("loc_14D24")


    #C0591
    ChrTalk(
        0x101,
        (
            "#0000F……こっちは２階だな。\x01",
            "部屋に戻っても仕方ないし……\x02\x03",

            "ちょっと外の風に当たるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DD0")

    #C0592
    ChrTalk(
        0x101,
        (
            "#0000Fイアン先生が訪ねてきてるみたいだ。\x01",
            "一応挨拶しておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DD0")

    Sleep(50)
    SetChrPos(0x0, 1000, 850, 9460, 180)
    EventEnd(0x4)
    Return()

    # Function_58_14CB5 end

    def Function_59_14DE7(): pass

    label("Function_59_14DE7")

    EventBegin(0x0)
    Fade(1000)
    OP_68(170700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 170000, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E92")

    #C0593
    ChrTalk(
        0x101,
        (
            "#12P#0005Fここは……\x01",
            "ティオの部屋だったはずだ。\x02\x03",

            "#0003Fさすがにもう寝てるかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_14E92")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ノックする】\x01",        # 0
            "【ノックしない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14EEC"),
        (1, "loc_14FAB"),
        (SWITCH_DEFAULT, "loc_14FB2"),
    )


    label("loc_14EEC")

    OP_95(0x101, 170000, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0594
    ChrTalk(
        0x101,
        (
            "#0005F#12P返事がない……\x01",
            "というか、全く気配がしないな。\x02\x03",

            "#0001Fもしかして部屋にいないのか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x13, 0x1)
    SetMapObjFlags(0x6, 0x10)
    SetChrPos(0x0, 170000, 0, 62900, 0)
    SetScenarioFlags(0x4A, 6)
    EventEnd(0x5)
    Jump("loc_14FB2")

    label("loc_14FAB")

    EventEnd(0x5)
    Jump("loc_14FB2")

    label("loc_14FB2")

    Return()

    # Function_59_14DE7 end

    def Function_60_14FB3(): pass

    label("Function_60_14FB3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 206030, 0, 119060, 360)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(205930, 1330, 125780, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(206030, 1330, 121140, 3000)
    Sleep(1000)

    def lambda_1502C():
        OP_96(0xFE, 0x324CE, 0x1E, 0x1D934, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1502C)

    def lambda_15046():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15046)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    #C0595
    ChrTalk(
        0x101,
        (
            "#0001F#12P（……やっぱりティオは\x01",
            "  部屋にいないみたいだな。）\x02\x03",

            "（荷ほどきは\x01",
            "  終わってるみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 1)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_60_14FB3 end

    def Function_61_150D3(): pass

    label("Function_61_150D3")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1511F")
    SetChrName("")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ここは空き部屋だ。\x01",
            "普段は鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1518D")

    label("loc_1511F")

    SetChrName("")

    #A0597
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

    #C0598
    ChrTalk(
        0x101,
        (
            "#0001F（ここは空き部屋みたいだな……\x01",
            "  用事も無いし、入らないでおくか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1518D")

    TalkEnd(0xFF)
    Return()

    # Function_61_150D3 end

    def Function_62_15191(): pass

    label("Function_62_15191")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151E9")
    SetChrFlags(0x0, 0x8)

    label("loc_151E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151FC")
    SetChrFlags(0x1, 0x8)

    label("loc_151FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1520F")
    SetChrFlags(0x2, 0x8)

    label("loc_1520F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15222")
    SetChrFlags(0x3, 0x8)

    label("loc_15222")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15235")
    SetChrFlags(0x4, 0x8)

    label("loc_15235")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15248")
    SetChrFlags(0x5, 0x8)

    label("loc_15248")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    #C0599
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0600
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152E8")
    ClearChrFlags(0x0, 0x8)

    label("loc_152E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152FB")
    ClearChrFlags(0x1, 0x8)

    label("loc_152FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1530E")
    ClearChrFlags(0x2, 0x8)

    label("loc_1530E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15321")
    ClearChrFlags(0x3, 0x8)

    label("loc_15321")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15334")
    ClearChrFlags(0x4, 0x8)

    label("loc_15334")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15347")
    ClearChrFlags(0x5, 0x8)

    label("loc_15347")

    Call(0, 79)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_62_15191 end

    def Function_63_1535E(): pass

    label("Function_63_1535E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153B6")
    SetChrFlags(0x0, 0x8)

    label("loc_153B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153C9")
    SetChrFlags(0x1, 0x8)

    label("loc_153C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153DC")
    SetChrFlags(0x2, 0x8)

    label("loc_153DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153EF")
    SetChrFlags(0x3, 0x8)

    label("loc_153EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15402")
    SetChrFlags(0x4, 0x8)

    label("loc_15402")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15415")
    SetChrFlags(0x5, 0x8)

    label("loc_15415")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0601
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0602
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154B5")
    ClearChrFlags(0x0, 0x8)

    label("loc_154B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154C8")
    ClearChrFlags(0x1, 0x8)

    label("loc_154C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154DB")
    ClearChrFlags(0x2, 0x8)

    label("loc_154DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154EE")
    ClearChrFlags(0x3, 0x8)

    label("loc_154EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15501")
    ClearChrFlags(0x4, 0x8)

    label("loc_15501")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15514")
    ClearChrFlags(0x5, 0x8)

    label("loc_15514")

    Call(0, 79)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_63_1535E end

    def Function_64_1552B(): pass

    label("Function_64_1552B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15583")
    SetChrFlags(0x0, 0x8)

    label("loc_15583")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15596")
    SetChrFlags(0x1, 0x8)

    label("loc_15596")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155A9")
    SetChrFlags(0x2, 0x8)

    label("loc_155A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155BC")
    SetChrFlags(0x3, 0x8)

    label("loc_155BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155CF")
    SetChrFlags(0x4, 0x8)

    label("loc_155CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155E2")
    SetChrFlags(0x5, 0x8)

    label("loc_155E2")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    #C0603
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0604
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15684")
    ClearChrFlags(0x0, 0x8)

    label("loc_15684")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15697")
    ClearChrFlags(0x1, 0x8)

    label("loc_15697")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156AA")
    ClearChrFlags(0x2, 0x8)

    label("loc_156AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156BD")
    ClearChrFlags(0x3, 0x8)

    label("loc_156BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156D0")
    ClearChrFlags(0x4, 0x8)

    label("loc_156D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156E3")
    ClearChrFlags(0x5, 0x8)

    label("loc_156E3")

    Call(0, 79)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_64_1552B end

    def Function_65_156FA(): pass

    label("Function_65_156FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1575D")
    SetChrFlags(0x0, 0x8)

    label("loc_1575D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15770")
    SetChrFlags(0x1, 0x8)

    label("loc_15770")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15783")
    SetChrFlags(0x2, 0x8)

    label("loc_15783")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15796")
    SetChrFlags(0x3, 0x8)

    label("loc_15796")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157A9")
    SetChrFlags(0x4, 0x8)

    label("loc_157A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157BC")
    SetChrFlags(0x5, 0x8)

    label("loc_157BC")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0605
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0606
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1585E")
    ClearChrFlags(0x0, 0x8)

    label("loc_1585E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15871")
    ClearChrFlags(0x1, 0x8)

    label("loc_15871")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15884")
    ClearChrFlags(0x2, 0x8)

    label("loc_15884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15897")
    ClearChrFlags(0x3, 0x8)

    label("loc_15897")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158AA")
    ClearChrFlags(0x4, 0x8)

    label("loc_158AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158BD")
    ClearChrFlags(0x5, 0x8)

    label("loc_158BD")

    Call(0, 79)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_65_156FA end

    def Function_66_158D4(): pass

    label("Function_66_158D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1592C")
    SetChrFlags(0x0, 0x8)

    label("loc_1592C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1593F")
    SetChrFlags(0x1, 0x8)

    label("loc_1593F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15952")
    SetChrFlags(0x2, 0x8)

    label("loc_15952")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15965")
    SetChrFlags(0x3, 0x8)

    label("loc_15965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15978")
    SetChrFlags(0x4, 0x8)

    label("loc_15978")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1598B")
    SetChrFlags(0x5, 0x8)

    label("loc_1598B")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0607
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0608
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A2F")
    ClearChrFlags(0x0, 0x8)

    label("loc_15A2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A42")
    ClearChrFlags(0x1, 0x8)

    label("loc_15A42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A55")
    ClearChrFlags(0x2, 0x8)

    label("loc_15A55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A68")
    ClearChrFlags(0x3, 0x8)

    label("loc_15A68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A7B")
    ClearChrFlags(0x4, 0x8)

    label("loc_15A7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A8E")
    ClearChrFlags(0x5, 0x8)

    label("loc_15A8E")

    Call(0, 79)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_66_158D4 end

    def Function_67_15AA5(): pass

    label("Function_67_15AA5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15AFD")
    SetChrFlags(0x0, 0x8)

    label("loc_15AFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B10")
    SetChrFlags(0x1, 0x8)

    label("loc_15B10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B23")
    SetChrFlags(0x2, 0x8)

    label("loc_15B23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B36")
    SetChrFlags(0x3, 0x8)

    label("loc_15B36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B49")
    SetChrFlags(0x4, 0x8)

    label("loc_15B49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B5C")
    SetChrFlags(0x5, 0x8)

    label("loc_15B5C")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    #C0609
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0610
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C00")
    ClearChrFlags(0x0, 0x8)

    label("loc_15C00")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C13")
    ClearChrFlags(0x1, 0x8)

    label("loc_15C13")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C26")
    ClearChrFlags(0x2, 0x8)

    label("loc_15C26")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C39")
    ClearChrFlags(0x3, 0x8)

    label("loc_15C39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C4C")
    ClearChrFlags(0x4, 0x8)

    label("loc_15C4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C5F")
    ClearChrFlags(0x5, 0x8)

    label("loc_15C5F")

    Call(0, 79)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_67_15AA5 end

    def Function_68_15C76(): pass

    label("Function_68_15C76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15CCE")
    SetChrFlags(0x0, 0x8)

    label("loc_15CCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15CE1")
    SetChrFlags(0x1, 0x8)

    label("loc_15CE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15CF4")
    SetChrFlags(0x2, 0x8)

    label("loc_15CF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D07")
    SetChrFlags(0x3, 0x8)

    label("loc_15D07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D1A")
    SetChrFlags(0x4, 0x8)

    label("loc_15D1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D2D")
    SetChrFlags(0x5, 0x8)

    label("loc_15D2D")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0611
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0612
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15DCD")
    ClearChrFlags(0x0, 0x8)

    label("loc_15DCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15DE0")
    ClearChrFlags(0x1, 0x8)

    label("loc_15DE0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15DF3")
    ClearChrFlags(0x2, 0x8)

    label("loc_15DF3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E06")
    ClearChrFlags(0x3, 0x8)

    label("loc_15E06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E19")
    ClearChrFlags(0x4, 0x8)

    label("loc_15E19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E2C")
    ClearChrFlags(0x5, 0x8)

    label("loc_15E2C")

    Call(0, 79)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_68_15C76 end

    def Function_69_15E43(): pass

    label("Function_69_15E43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EA6")
    SetChrFlags(0x0, 0x8)

    label("loc_15EA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EB9")
    SetChrFlags(0x1, 0x8)

    label("loc_15EB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15ECC")
    SetChrFlags(0x2, 0x8)

    label("loc_15ECC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EDF")
    SetChrFlags(0x3, 0x8)

    label("loc_15EDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EF2")
    SetChrFlags(0x4, 0x8)

    label("loc_15EF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F05")
    SetChrFlags(0x5, 0x8)

    label("loc_15F05")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    #C0613
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0614
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
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FA5")
    ClearChrFlags(0x0, 0x8)

    label("loc_15FA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FB8")
    ClearChrFlags(0x1, 0x8)

    label("loc_15FB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FCB")
    ClearChrFlags(0x2, 0x8)

    label("loc_15FCB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FDE")
    ClearChrFlags(0x3, 0x8)

    label("loc_15FDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FF1")
    ClearChrFlags(0x4, 0x8)

    label("loc_15FF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16004")
    ClearChrFlags(0x5, 0x8)

    label("loc_16004")

    Call(0, 79)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_69_15E43 end

    def Function_70_1601B(): pass

    label("Function_70_1601B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16071")
    SetChrName("")

    #A0615
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

    label("loc_16071")

    Return()

    # Function_70_1601B end

    def Function_71_16072(): pass

    label("Function_71_16072")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis164.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0616
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

    # Function_71_16072 end

    def Function_72_1611D(): pass

    label("Function_72_1611D")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis165.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0617
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
    Sleep(10)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_161E8"),
        (1, "loc_161F1"),
        (2, "loc_161FA"),
        (3, "loc_16203"),
        (4, "loc_1620C"),
        (5, "loc_16215"),
        (6, "loc_1621E"),
        (7, "loc_16227"),
        (SWITCH_DEFAULT, "loc_16230"),
    )


    label("loc_161E8")

    PlayBGM("ed7400", 0)
    Jump("loc_16230")

    label("loc_161F1")

    PlayBGM("ed7401", 0)
    Jump("loc_16230")

    label("loc_161FA")

    PlayBGM("ed7402", 0)
    Jump("loc_16230")

    label("loc_16203")

    PlayBGM("ed7204", 0)
    Jump("loc_16230")

    label("loc_1620C")

    PlayBGM("ed7205", 0)
    Jump("loc_16230")

    label("loc_16215")

    PlayBGM("ed7201", 0)
    Jump("loc_16230")

    label("loc_1621E")

    PlayBGM("ed7200", 0)
    Jump("loc_16230")

    label("loc_16227")

    PlayBGM("ed7202", 0)
    Jump("loc_16230")

    label("loc_16230")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_72_1611D end

    def Function_73_1625F(): pass

    label("Function_73_1625F")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis167.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0618
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

    # Function_73_1625F end

    def Function_74_16302(): pass

    label("Function_74_16302")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis166.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0619
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

    # Function_74_16302 end

    def Function_75_163AD(): pass

    label("Function_75_163AD")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis168.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0620
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

    # Function_75_163AD end

    def Function_76_16454(): pass

    label("Function_76_16454")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0621
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

    # Function_76_16454 end

    def Function_77_164FD(): pass

    label("Function_77_164FD")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis171.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0622
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

    # Function_77_164FD end

    def Function_78_165AC(): pass

    label("Function_78_165AC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis170.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0623
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

    # Function_78_165AC end

    def Function_79_16659(): pass

    label("Function_79_16659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16691")
    OP_DE(0x16, 0x0)

    label("loc_16691")

    Return()

    # Function_79_16659 end

    def Function_80_16692(): pass

    label("Function_80_16692")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16719")
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

    label("loc_16719")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16735")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_16735")

    Return()

    # Function_80_16692 end

    def Function_81_16737(): pass

    label("Function_81_16737")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167BE")
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

    label("loc_167BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_167DA")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_167DA")

    Return()

    # Function_81_16737 end

    def Function_82_167DC(): pass

    label("Function_82_167DC")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16863")
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

    label("loc_16863")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1687F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1687F")

    Return()

    # Function_82_167DC end

    def Function_83_16881(): pass

    label("Function_83_16881")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16908")
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

    label("loc_16908")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16924")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_16924")

    Return()

    # Function_83_16881 end

    SaveToFile()

Try(main)
