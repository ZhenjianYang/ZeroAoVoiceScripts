from ZeroScenarioHelper import *

def main():
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
        "兰迪",                   # 1
        "兰迪",                   # 2
        "艾莉",                   # 3
        "缇欧",                   # 4
        "缇欧",                   # 5
        "琪雅",                   # 6
        "琪雅",                   # 7
        "蔡特",                   # 8
        "蔡特",                   # 9
        "赛尔盖科长",             # 10
        "赛尔盖科长",             # 11
        "伊安律师",               # 12
        "小滴",                   # 13
        "警备队员",               # 14
        "警备队员",               # 15
        "书籍",                   # 16
        "餐具",                   # 17
        "餐具",                   # 18
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
        "Function_4_146E",         # 04, 4
        "Function_5_151C",         # 05, 5
        "Function_6_1656",         # 06, 6
        "Function_7_18FE",         # 07, 7
        "Function_8_194A",         # 08, 8
        "Function_9_1A87",         # 09, 9
        "Function_10_1BD0",        # 0A, 10
        "Function_11_1E27",        # 0B, 11
        "Function_12_1E2B",        # 0C, 12
        "Function_13_1E2F",        # 0D, 13
        "Function_14_1E33",        # 0E, 14
        "Function_15_1E37",        # 0F, 15
        "Function_16_1E85",        # 10, 16
        "Function_17_27C3",        # 11, 17
        "Function_18_2B28",        # 12, 18
        "Function_19_37BF",        # 13, 19
        "Function_20_4575",        # 14, 20
        "Function_21_54F1",        # 15, 21
        "Function_22_5BE9",        # 16, 22
        "Function_23_6C7D",        # 17, 23
        "Function_24_71D5",        # 18, 24
        "Function_25_746A",        # 19, 25
        "Function_26_AC40",        # 1A, 26
        "Function_27_B73D",        # 1B, 27
        "Function_28_B802",        # 1C, 28
        "Function_29_B910",        # 1D, 29
        "Function_30_B989",        # 1E, 30
        "Function_31_BA02",        # 1F, 31
        "Function_32_D085",        # 20, 32
        "Function_33_D0DA",        # 21, 33
        "Function_34_D12F",        # 22, 34
        "Function_35_D184",        # 23, 35
        "Function_36_F5CE",        # 24, 36
        "Function_37_F5ED",        # 25, 37
        "Function_38_11E3C",       # 26, 38
        "Function_39_11F6B",       # 27, 39
        "Function_40_1206D",       # 28, 40
        "Function_41_12196",       # 29, 41
        "Function_42_12227",       # 2A, 42
        "Function_43_1229A",       # 2B, 43
        "Function_44_1232B",       # 2C, 44
        "Function_45_123CF",       # 2D, 45
        "Function_46_12473",       # 2E, 46
        "Function_47_12B47",       # 2F, 47
        "Function_48_12B6D",       # 30, 48
        "Function_49_12BA0",       # 31, 49
        "Function_50_12C04",       # 32, 50
        "Function_51_12C75",       # 33, 51
        "Function_52_12CCA",       # 34, 52
        "Function_53_12D1F",       # 35, 53
        "Function_54_12D74",       # 36, 54
        "Function_55_12DE7",       # 37, 55
        "Function_56_12E5A",       # 38, 56
        "Function_57_12F75",       # 39, 57
        "Function_58_1302C",       # 3A, 58
        "Function_59_13134",       # 3B, 59
        "Function_60_132DE",       # 3C, 60
        "Function_61_133E2",       # 3D, 61
        "Function_62_1347E",       # 3E, 62
        "Function_63_1363F",       # 3F, 63
        "Function_64_13800",       # 40, 64
        "Function_65_139BF",       # 41, 65
        "Function_66_13B89",       # 42, 66
        "Function_67_13D44",       # 43, 67
        "Function_68_13EFF",       # 44, 68
        "Function_69_140BA",       # 45, 69
        "Function_70_14280",       # 46, 70
        "Function_71_142D3",       # 47, 71
        "Function_72_14378",       # 48, 72
        "Function_73_144B2",       # 49, 73
        "Function_74_14553",       # 4A, 74
        "Function_75_145F6",       # 4B, 75
        "Function_76_14699",       # 4C, 76
        "Function_77_1473C",       # 4D, 77
        "Function_78_147E5",       # 4E, 78
        "Function_79_14888",       # 4F, 79
        "Function_80_148C1",       # 50, 80
        "Function_81_14960",       # 51, 81
        "Function_82_149FF",       # 52, 82
        "Function_83_14A9E",       # 53, 83
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_END)), "loc_13BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1365")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#0305F……怎么，是罗伊德啊。\x01",
            "这么晚还要出门吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，那倒\x01",
            "不是啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "#0303F……大小姐的事吗？\x02\x03",

            "#0300F嗯，看来似乎有\x01",
            "不少内情呢。\x02\x03",

            "但不知道我们\x01",
            "是否应该插手。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0008F说得也是啊……\x01",
            "（要是有烦恼的话，\x01",
            "  还是希望她能自己说出来……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_13B7")

    label("loc_1365")


    #C0005
    ChrTalk(
        0xFE,
        (
            "#0306F真不想看到\x01",
            "大小姐那种沮丧的表情啊。\x02\x03",

            "#0308F但不知道我们\x01",
            "是否应该插手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B7")

    Jump("loc_1466")

    label("loc_13BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_1466")

    #C0006
    ChrTalk(
        0xFE,
        (
            "#0303F哎，你的迷惘\x01",
            "也是可以理解的。\x02\x03",

            "#0300F不如好好考虑\x01",
            "一个晚上如何？\x02\x03",

            "#0309F如果正式成为同伴的话，\x01",
            "我们就一起出去玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0002F哈哈，我会好好考虑的。\x02",
    )

    CloseMessageWindow()

    label("loc_1466")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_1149 end

    def Function_4_146E(): pass

    label("Function_4_146E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_1518")

    #C0008
    ChrTalk(
        0xFE,
        (
            "#0106F今天是上任的第一天，\x01",
            "而且也发生了不少事呢。\x02\x03",

            "#0100F我也有点累了。\x01",
            "写完日记之后\x01",
            "就想早点休息了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1518")

    #C0009
    ChrTalk(
        0x101,
        (
            "#0002F哈哈，是啊。\x02\x03",

            "晚安，艾莉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_1518")

    TalkEnd(0xFE)
    Return()

    # Function_4_146E end

    def Function_5_151C(): pass

    label("Function_5_151C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_15CA")

    #C0010
    ChrTalk(
        0xFE,
        (
            "#0202F不好意思，我们马上就准备好了，\x01",
            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0002F嗯……\x01",
            "缇欧，你们慢慢来，不用急。\x01",
            "稍后我们也会来帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "#0204F……好的，麻烦大家了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1652")

    label("loc_15CA")


    #C0013
    ChrTalk(
        0xFE,
        (
            "#0200F是罗伊德前辈啊。\x01",
            "还有什么事吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#0002F不，没什么啦。\x01",
            "抱歉，打扰你了。\x02\x03",

            "晚安。\x01",
            "好好休息哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "#0204F好的。\x01",
            "晚安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1652")

    TalkEnd(0xFE)
    Return()

    # Function_5_151C end

    def Function_6_1656(): pass

    label("Function_6_1656")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16EA")
    Jump("loc_1734")

    label("loc_16EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_170A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1734")

    label("loc_170A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1734")

    label("loc_172A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1734")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186B")

    #C0016
    ChrTalk(
        0x101,
        (
            "#0002F啊……缇欧，\x01",
            "你好像正在看书啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "#0203F有些专业杂志\x01",
            "还没看完。\x02\x03",

            "#0208F……那个，罗伊德前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F我知道……\x01",
            "是艾莉的事吧？\x02\x03",

            "#0000F我打算和她\x01",
            "稍微谈谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "#0202F……是吗？\x01",
            "那么，就交给罗伊德前辈了。\x02\x03",

            "#0206F我不太擅长\x01",
            "处理这种事……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_18F6")

    label("loc_186B")


    #C0020
    ChrTalk(
        0xFE,
        (
            "#0202F艾莉前辈的事\x01",
            "就交给罗伊德前辈了。\x02\x03",

            "#0206F本来，这种事情\x01",
            "也许应该由身为同性的我\x01",
            "去处理比较好……\x02\x03",

            "可是，我实在是不擅长这种事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1656 end

    def Function_7_18FE(): pass

    label("Function_7_18FE")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "#1109F打下手～打下手～¤\x02\x03",

            "#1110F罗伊德～晚饭\x01",
            "还要稍等一下哦～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_18FE end

    def Function_8_194A(): pass

    label("Function_8_194A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_19FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DD")

    #C0022
    ChrTalk(
        0xFE,
        "#1203F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0300F（一点都不在意我们，\x01",
            "  睡得可真熟啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0012F（嗯，不过它一向如此嘛。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_19F7")

    label("loc_19DD")


    #C0025
    ChrTalk(
        0xFE,
        "#1203F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_19F7")

    Jump("loc_1A83")

    label("loc_19FC")


    #C0026
    ChrTalk(
        0xFE,
        "#1203F呜噜噜噜噜…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4D")

    #C0027
    ChrTalk(
        0x101,
        "#0002F（哈哈，似乎很放松呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A83")

    label("loc_1A4D")


    #C0028
    ChrTalk(
        0x101,
        (
            "#0008F（蔡特……\x01",
            "  应该不知道艾莉\x01",
            "  在哪里吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A83")

    TalkEnd(0xFE)
    Return()

    # Function_8_194A end

    def Function_9_1A87(): pass

    label("Function_9_1A87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B46")

    #C0029
    ChrTalk(
        0xFE,
        (
            "#1002F呵呵，怎么了？\x02\x03",

            "#1003F──再说一遍，如果想辞掉支援科的\x01",
            "工作，也是可以的。\x02\x03",

            "因为你拥有搜查官资格，\x01",
            "应该会被分配到搜查科的某个部门吧。\x02\x03",

            "#1000F好好考虑一晚上吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1BCC")

    label("loc_1B46")


    #C0030
    ChrTalk(
        0xFE,
        (
            "#1003F如果想辞掉支援科的\x01",
            "工作，也是可以的。\x02\x03",

            "因为你拥有搜查官资格，\x01",
            "应该会被分配到搜查科的某个部门吧。\x02\x03",

            "#1000F好好考虑一晚上吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCC")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A87 end

    def Function_10_1BD0(): pass

    label("Function_10_1BD0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C64")
    Jump("loc_1CAE")

    label("loc_1C64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CAE")

    label("loc_1C84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CA4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CAE")

    label("loc_1CA4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CAE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD5")

    #C0031
    ChrTalk(
        0xFE,
        (
            "#1005F怎么，是你啊。\x01",
            "别露出那么\x01",
            "沮丧的表情啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，抱歉……\x01",
            "科长在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "#1006F就算是我们这种部门，\x01",
            "也是有文案工作的。\x02\x03",

            "#1000F没什么事的话，就赶快出去吧。\x01",
            "我也得快点\x01",
            "把这些事情解决掉才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#0000F是，打扰您了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1E1F")

    label("loc_1DD5")


    #C0035
    ChrTalk(
        0xFE,
        (
            "#1000F没什么事的话，就赶快出去吧。\x01",
            "我也得快点\x01",
            "把这些事情解决掉才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_1BD0 end

    def Function_11_1E27(): pass

    label("Function_11_1E27")

    Call(0, 18)
    Return()

    # Function_11_1E27 end

    def Function_12_1E2B(): pass

    label("Function_12_1E2B")

    Call(0, 19)
    Return()

    # Function_12_1E2B end

    def Function_13_1E2F(): pass

    label("Function_13_1E2F")

    Call(0, 24)
    Return()

    # Function_13_1E2F end

    def Function_14_1E33(): pass

    label("Function_14_1E33")

    Call(0, 59)
    Return()

    # Function_14_1E33 end

    def Function_15_1E37(): pass

    label("Function_15_1E37")

    TalkBegin(0xFF)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "终端的导力已经停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0037
    ChrTalk(
        0x101,
        "#0000F……现在没有必要使用吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_15_1E37 end

    def Function_16_1E85(): pass

    label("Function_16_1E85")

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
            "#0011F以市民的安全为优先目的，\x01",
            "应对各种请求的部门……！？\x02",
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
            "#1P#1003F对，这就是新设立的\x01",
            "『特别任务支援科』的行动方针。\x02\x03",

            "为了能更好地贴近市民们的生活，\x01",
            "还在这种市中心地段准备了部门大楼。\x02\x03",

            "#1002F哼哼，很合理吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#12P#0011F但、但是，这个……！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0106F好像完全是在模仿\x01",
            "游击士协会吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#4P#0211F说白了，根本就是抄袭吧。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#0306F就是啊。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x11,
        (
            "#1P#1000F你们可能也知道，\x01",
            "游击士协会如今在克洛斯贝尔的\x01",
            "地位与评价之高，可是非比寻常的。\x02\x03",

            "#1003F除了人称『风之剑圣』的Ａ级游击士——\x02\x03",

            "亚里欧斯·马克莱因以外，\x01",
            "还有许多相当有能力的人\x01",
            "常驻于克洛斯贝尔分部。\x02\x03",

            "#1000F这对警察局的高层来说，意味着什么，\x01",
            "你们能理解吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#12P#0005F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0103F警察局会被人拿来同协会进行比较与评价，\x01",
            "并就组织上的种种问题受到指责……\x02\x03",

            "#0108F最后批评更是会直接指向自治州政府，\x01",
            "是这样的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0304F原来如此，是这么回事啊。\x02\x03",

            "#0300F也就是说，要想办法抢协会的风头，\x01",
            "以此来赚取人气吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#4P#0206F……说得真是露骨啊。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x11,
        (
            "#1P#1004F嗯，说白了，\x01",
            "正如你们所言。\x02\x03",

            "#1001F但是，警察的基本理念是\x01",
            "维持治安与遵守自治州法……\x02\x03",

            "服务市民\x01",
            "本来就是排在第二位的。\x02\x03",

            "#1003F正因如此，在警察局内部，\x01",
            "也有不少人都对这种赚取人气的\x01",
            "行为表示不满。\x02\x03",

            "『打杂事务所』啦、『假游击士』啦、\x01",
            "『演戏的猴子』什么的……\x02\x03",

            "#1002F呼，总之，各种阴损的坏话\x01",
            "都听过无数次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#12P#0011F……………………（张口结舌）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#0106F原来如此……\x01",
            "情况大致了解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#0301F哎呀呀，难道是\x01",
            "要我们在这种部门中工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#4P#0211F……说实话，真是意料之外呢。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x11,
        (
            "#1P#1004F好啦，先别着急嘛。\x02\x03",

            "#1002F──你们可能也听说过了，\x01",
            "想辞掉这个职位也是可以的。\x02",
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
        "#12P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x11,
        (
            "#1P#1003F被正式分配以后，\x01",
            "你们就需要做各种各样的工作。\x02\x03",

            "其中也包括像今天这种\x01",
            "清剿魔兽的工作……\x02\x03",

            "此外，还有寻找失物、帮总部打杂\x01",
            "之类的琐碎杂务吧。\x02\x03",

            "#1001F──我想，没有兴趣的人\x01",
            "肯定是干不下来的。\x02",
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
            "#1003F所以，就给你们一个晚上的时间来考虑吧。\x02\x03",

            "如果辞掉这个职位，\x01",
            "就会被分配到其它部门去，\x01",
            "现在辞职的话，并没有负面影响。\x02\x03",

            "#1000F一切都由你们自己决定了。\x02",
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

    # Function_16_1E85 end

    def Function_17_27C3(): pass

    label("Function_17_27C3")

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
            "#0006F……好像被分到了\x01",
            "很奇怪的地方呢……\x02\x03",

            "#0008F模仿游击士吗……\x02\x03",

            "我不是为了做这种事\x01",
            "才当警察的啊……\x02",
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
            "#0003F#11P……记得大哥当时所属的部门\x01",
            "是『搜查一科』吧。\x02\x03",

            "一手包办大案要案与政治性、\x01",
            "国际性案件的精英集团……\x02\x03",

            "#0008F……果然离我很遥远啊……\x02\x03",

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
            "#5P#0001F……其他人\x01",
            "都有何打算呢？\x02\x03",

            "那三个人……\x01",
            "好像都没有上过警察学校，\x01",
            "而且各有隐情呢……\x02\x03",

            "#0000F不如去问问看吧。\x02",
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

    # Function_17_27C3 end

    def Function_18_2B28(): pass

    label("Function_18_2B28")

    EventBegin(0x0)
    Fade(1000)
    OP_68(13700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 13700, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD2")

    #C0062
    ChrTalk(
        0x101,
        (
            "#12P#0005F这里……\x01",
            "应该是兰迪的房间吧。\x02\x03",

            "#0001F刚才好像还\x01",
            "听到了搬东西的响动……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2BD2")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【敲门】\x01",        # 0
            "【不敲门】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C20"),
        (1, "loc_37B7"),
        (SWITCH_DEFAULT, "loc_37BE"),
    )


    label("loc_2C20")

    OP_95(0x101, 13700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0x8, 13700, 0, 66000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)

    #N0063
    NpcTalk(
        0x8,
        "兰迪的声音",
        "#5P#2S……嗯，是谁？\x07\x00\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#12P#0000F是我，罗伊德，\x01",
            "可以打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0065
    NpcTalk(
        0x8,
        "兰迪的声音",
        (
            "#5P#2S哦，可以啊。\x01",
            "别客气，进来吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#12P#0000F那么，我就打扰了。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)

    def lambda_2D20():
        OP_95(0xFE, 13700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D20)
    Sleep(300)

    def lambda_2D3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D3D)
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
        "#0005F啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(51000, 1000, 124200, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_2E8A():
        OP_95(0xFE, 51000, 0, 123200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E8A)
    OP_0D()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    SetChrPos(0x8, 51000, 0, 126400, 270)
    OP_0D()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_2ED4():
        OP_95(0xFE, 51000, 0, 125100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2ED4)
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
            "欢迎来到本大爷的城堡。\x02\x03",

            "你的行李\x01",
            "也都放好了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FEC")

    #C0069
    ChrTalk(
        0x101,
        (
            "#12P#0006F不、不……还没有。\x02\x03",

            "#0000F──看来兰迪\x01",
            "已经得出结论了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3037")

    label("loc_2FEC")


    #C0070
    ChrTalk(
        0x101,
        (
            "#12P#0006F不、不……还没有。\x02\x03",

            "#0000F──看来兰迪\x01",
            "也已经得出结论了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3037")


    #C0071
    ChrTalk(
        0x8,
        (
            "#5P#0305F哦，是说要不要辞职的事吗？\x02\x03",

            "#0304F嗯，看样子，文案的工作好像不多，\x01",
            "而且氛围又比较轻松，很合我的个性。\x02\x03",

            "#0300F工作场所和住处都在一起\x01",
            "也很省事，\x01",
            "所以我是打算待下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#12P#0003F是吗……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "#5P#0300F看样子，你好像\x01",
            "还是很迷茫啊？\x02\x03",

            "是不想把好不容易才取得的搜查官资格\x01",
            "浪费在这种地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#0004F哈哈……也有这方面的原因。\x02\x03",

            "#0008F更重要的是，总觉得离自己原本的\x01",
            "目标越来越远了……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "#5P#0305F原本的目标……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#0012F这个，嗯……\x01",
            "其实也没什么大不了的。\x02\x03",

            "#0000F说起来……\x01",
            "兰迪是因为什么\x01",
            "而被分配到这里来的？\x02\x03",

            "你好像比我们都年长……\x01",
            "但却没上过警察学校吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#5P#0305F哦，没错。\x02\x03",

            "#0303F嗯～我被分配\x01",
            "到这里的原委啊……\x02\x03",

            "#0301F──你真的想听吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#12P#0005F嗯，\x01",
            "如果你不介意的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "#5P#0303F既然你这么想听，那就没办法啦。\x02\x03",

            "#0302F其实啊──都是女性关系问题惹的祸。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#12P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5P#0309F哎呀～我在之前的工作地点\x01",
            "一直脚踏多条船，最后被拆穿啦。\x02\x03",

            "就在要被解雇的时候，\x01",
            "大叔收留了我。\x02\x03",

            "这也是空之女神的\x01",
            "指引吧。\x02",
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
            "#12P#0011F呃……\x01",
            "兰迪以前工作的地方是？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#5P#0300F哦，是克洛斯贝尔警备队。\x02\x03",

            "位于帝国方向的国境门，\x01",
            "叫做贝尔加德门来着，你知道吧？\x01",
            "我本来一直待在那里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#0000F警备队……原来是这样啊。\x02\x03",

            "难怪能将那么巨大的斧枪\x01",
            "操纵自如。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "#5P#0306F嗯，毕竟我一直都待在国境附近，\x01",
            "除了训练和巡逻之外，\x01",
            "也没别的事情可做嘛。\x02\x03",

            "#0300F从这一点来看，在克洛斯贝尔市工作的话，\x01",
            "就可以去欢乐街之类的地方尽情玩乐了。\x02\x03",

            "#0309F哎呀～脱离警备队\x01",
            "看来真是个正确的选择啊¤\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#12P#0012F哈哈……\x01",
            "这种心情还是可以理解的。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "#5P#0305F哦哦，我们还挺合得来嘛。\x02\x03",

            "#0302F……话说，其实我\x01",
            "找到好几间\x01",
            "有性感美女的店哦。\x02\x03",

            "要是正式成为同伴的话，\x01",
            "就一起结伴出游吧？\x02\x03",

            "#0309F大小姐好像很顽固，\x01",
            "小孩子又不能约，\x01",
            "这就是所谓的男人的游乐啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#12P#0002F哈哈……\x01",
            "明白了，我会考虑的。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37AD")
    ModifyEventFlags(1, 0, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_37AD")

    Sleep(500)
    EventEnd(0x5)
    Jump("loc_37BE")

    label("loc_37B7")

    EventEnd(0x5)
    Jump("loc_37BE")

    label("loc_37BE")

    Return()

    # Function_18_2B28 end

    def Function_19_37BF(): pass

    label("Function_19_37BF")

    EventBegin(0x0)
    Fade(1000)
    OP_68(163700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 163700, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3858")

    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#0005F这里……\x01",
            "好像是艾莉的房间吧。\x02\x03",

            "#0001F希望她还没睡……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3858")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【敲门】\x01",        # 0
            "【不敲门】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_38A6"),
        (1, "loc_456D"),
        (SWITCH_DEFAULT, "loc_4574"),
    )


    label("loc_38A6")

    OP_95(0x101, 163700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0xA, 163700, 0, 66000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    #N0090
    NpcTalk(
        0xA,
        "艾莉的声音",
        "#5P#2S……是哪位？\x07\x00\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个……是我，罗伊德。\x02\x03",

            "现在方便打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0092
    NpcTalk(
        0xA,
        "艾莉的声音",
        "#5P#2S嗯，可以啊。\x07\x00\x02",
    )

    CloseMessageWindow()

    #N0093
    NpcTalk(
        0xA,
        "艾莉的声音",
        "#5P#2S门没锁，进来吧。\x07\x00\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#12P#0000F那么就……打扰了。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x5)

    def lambda_39C9():
        OP_95(0xFE, 163700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39C9)
    Sleep(300)

    def lambda_39E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39E6)
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

    def lambda_3B2D():
        OP_95(0xFE, 157800, 0, 122900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B2D)
    Sleep(200)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(100)

    def lambda_3B54():
        OP_95(0xFE, 157800, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3B54)
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
            "呵呵……\x01",
            "总算收拾好了，这样就行了。\x02\x03",

            "你先坐在那边吧？\x01",
            "我这就去泡红茶。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C91")

    #C0097
    ChrTalk(
        0x101,
        (
            "#12P#0004F啊，不用麻烦了。\x02\x03",

            "#0001F不过，看这房间的样子，\x01",
            "你好像已经得出结论了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CDE")

    label("loc_3C91")


    #C0098
    ChrTalk(
        0x101,
        (
            "#12P#0004F啊，不用麻烦了。\x02\x03",

            "#0001F话说，连艾莉也……\x01",
            "已经得出结论了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CDE")


    #C0099
    ChrTalk(
        0xA,
        (
            "#5P#0105F哦，你是说辞职的事吧。\x02\x03",

            "#0104F虽然之前也犹豫过……\x01",
            "不过，我还是决定留在这里努力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#12P#0000F是吗……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "#5P#0100F……你好像\x01",
            "还在迷惑呢。\x02\x03",

            "#0106F不过，这也难怪吧。\x02\x03",

            "#0108F关于这个特别任务支援科……\x01",
            "说实话，确实是太勉强了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x101,
        "#12P#0005F勉强？\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#5P#0101F从已知的信息看来，这里似乎是\x01",
            "在各种阻碍与算计中成立的部门吧？\x02\x03",

            "欠缺作为组织的合理性，\x01",
            "目的也不清不楚。\x02\x03",

            "#0103F如果拿不出成果的话，\x01",
            "很可能真的会因为预算问题\x01",
            "而被强制解散吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#12P#0006F……嗯，\x01",
            "按照常识来考虑的话，确实如此啊。\x02\x03",

            "#0001F不过，既然艾莉对情况了解得这么清楚，\x01",
            "为什么还决定留下来呢？\x02\x03",

            "莫非有什么原因吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#5P#0100F这个嘛……\x02\x03",

            "#0104F……因为，这里似乎很适合\x01",
            "观察各种扭曲的现象吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#5P#0109F呵呵，开玩笑啦。\x02\x03",

            "#0100F我想，我大概不会一直\x01",
            "在警察系统工作的。\x02\x03",

            "从这层意义上来说，\x01",
            "就算这里偏离了职业规划的轨道，\x01",
            "对我而言，也没有太大的关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#12P#0003F是这样吗……\x02\x03",

            "#0000F我记得，艾莉好像没上过\x01",
            "警察学校吧？\x02\x03",

            "你是怎么进入警察局工作的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "#5P#0101F嗯～……\x01",
            "简单来说，算是社会实践吧。\x02\x03",

            "#0103F顺带一提，入职的测试项目\x01",
            "是笔记和射击……\x02\x03",

            "#0102F两项我都是满分，\x01",
            "所以警察局总部似乎也没法拒绝呢。\x02",
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
            "#12P#0012F越、越听越觉得\x01",
            "我和你不是一个层次的人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "#5P#0100F哎呀，你不也很厉害嘛，\x01",
            "身为新人就取得搜查官资格，\x01",
            "这也是很少见的吧？\x02\x03",

            "其中一定也有什么隐情吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#12P#0005F……这个………\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "#5P#0104F呵呵……\x02\x03",

            "#0102F看来，更多详情还是等\x01",
            "正式成为同事以后再问为好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#12P#0002F嗯……也是啊。\x02\x03",

            "#0004F抱歉，让你费心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "#5P#0104F哪里哪里。\x02\x03",

            "#0102F不过，若以我的个人意见来说，\x01",
            "比较希望你能留下来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "#5P#0106F就是说，虽然我们都是新人，\x01",
            "还有很多不足之处……\x02\x03",

            "#0102F不过，像今天这样，在面对不熟悉的紧急情况时，\x01",
            "你也出色担当起了队长的职责。\x02\x03",

            "做出的指示也很明确，\x01",
            "所以我才能安心提供支援嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#0012F哈哈……\x01",
            "你能这么说，我真是安心了不少。\x02\x03",

            "#0004F──谢谢你，\x01",
            "还这样陪我谈心。\x02\x03",

            "#0000F接下来，我就自己好好思考一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "#5P#0104F嗯……也是。\x02\x03",

            "#0102F晚安，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#12P#0002F晚安，艾莉。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4563")
    ModifyEventFlags(1, 0, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_4563")

    Sleep(500)
    EventEnd(0x5)
    Jump("loc_4574")

    label("loc_456D")

    EventEnd(0x5)
    Jump("loc_4574")

    label("loc_4574")

    Return()

    # Function_19_37BF end

    def Function_20_4575(): pass

    label("Function_20_4575")

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

    def lambda_4643():
        OP_96(0xFE, 0x42CC, 0x352, 0x23F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4643)
    WaitChrThread(0xB, 1)
    Sleep(1000)

    def lambda_4664():
        OP_96(0xFE, 0x3EE4, 0x352, 0x27D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4664)
    OP_6F(0x1)
    OP_6F(0x10)

    #C0121
    ChrTalk(
        0x101,
        (
            "#0005F缇欧……\x01",
            "你在干什么呢？\x02",
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

    def lambda_4713():
        OP_97(0x101, 0x12C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4713)
    Sleep(500)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)

    def lambda_473A():
        OP_95(0xFE, 15000, 850, 10200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_473A)
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
            "……罗伊德前辈。\x02\x03",

            "如你所见，\x01",
            "我正在检查终端。\x02",
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
        "#6P#0005F终端……是说这个吗？\x02",
    )

    CloseMessageWindow()
    OP_68(16500, 1750, 10300, 1500)
    MoveCamera(35, 16, 0, 1500)
    SetCameraDistance(22000, 1500)

    def lambda_4843():
        OP_95(0x101, 13300, 850, 9800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4843)
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
            "#0200F#5P这是财团对ＺＣＦ的卡佩尔系统\x01",
            "进行改良之后的通用终端。\x02\x03",

            "可以通过导力网络，\x01",
            "从警察局总部\x01",
            "接收情报。\x02",
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
            "#6P#0011F哎……？\x02\x03",

            "等、等一下。\x01",
            "突然说这些，我可听不懂啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "#0203F#5P……说得也是。\x02\x03",

            "#0200F罗伊德前辈，\x01",
            "关于『导力网络计划』，\x01",
            "你了解多少呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#0005F『导力网络』……\x02\x03",

            "#0006F偶尔在杂志的报道上看过，\x01",
            "但是基本都没有看懂。\x02\x03",

            "#0001F记得好像是爱普斯泰恩财团\x01",
            "推行的什么来着……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#0200F#5P原本是由爱普斯泰恩财团\x01",
            "和蔡斯中央工房共同发起的\x01",
            "开发计划。\x02\x03",

            "现在主要是由\x01",
            "财团在继续推进……\x02\x03",

            "如今正在克洛斯贝尔市\x01",
            "进行大规模的\x01",
            "试验运用。\x02\x03",

            "唔，这个也是其中的一环。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#6P#0005F我、我还是不太明白……\x02\x03",

            "#0012F说到底，\x01",
            "这计划究竟是要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        "#0203F#5P唉……\x02",
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
            "#11P#0200F总之，终端运用的是在旧式通讯器的基础上\x01",
            "发展起来的新技术。\x02\x03",

            "凭借此技术，不仅可以进行通话，\x01",
            "还可通过将有演算能力的终端连接起来，\x01",
            "构筑出一个高效率的情报网络。\x02\x03",

            "简单明了地来说，差不多就是这样吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#0006F一点也不简单明了……\x02\x03",

            "#0001F嗯，也就是说，\x01",
            "这个终端就是用来提高警察局内部的联络\x01",
            "与指挥系统效率的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "#11P#0204F……嗯，就这个终端来说，\x01",
            "是这样没错。\x02\x03",

            "#0202F虽然导力网络不是我的专业领域，\x01",
            "不过操作终端还是没问题的。\x02\x03",

            "考虑到今后的使用需求，\x01",
            "我想还是先检查一遍为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#6P#0005F是、是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#0000F这样看来，\x01",
            "缇欧好像完全没有考虑过\x01",
            "辞职的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        "#0205F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#6P#0003F那个，就是说……\x01",
            "我在缇欧这个年纪的时候，\x01",
            "还只是一个玩心十足的小毛孩呢。\x02\x03",

            "#0000F你说是财团派你来的，\x01",
            "那个……该不会是强迫你\x01",
            "劳动什么的吧？\x02",
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
            "#6P#0011F哎……！？\x01",
            "难不成，真被我说中了吗！？\x02\x03",

            "#0013F无论有什么样的隐情，\x01",
            "遇到这种事情也都不能忍气吞声啊！？\x02\x03",

            "那个，如果不嫌弃的话，\x01",
            "我可以尽力帮忙──\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "#0206F#11P那个，请冷静一下。\x02\x03",

            "#0208F……我并不是\x01",
            "被人强制进行劳动的。\x02\x03",

            "#0202F倒不如说……\x01",
            "这次外派，是我自己\x01",
            "提出的任性要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "#0204F#11P我自有留在这里的\x01",
            "个人原因……\x02\x03",

            "简单来说，就是这样。\x02\x03",

            "#0211F罗伊德前辈，你在担心别人之前，\x01",
            "应该先担心一下自己才对吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……\x02\x03",

            "#0006F哈哈，也是啊。\x01",
            "正如你所说。\x02\x03",

            "#0000F对不起啊，\x01",
            "我太多管闲事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "#0203F#11P不会……\x02\x03",

            "#0202F只不过，以搜查官来说，\x01",
            "性格太过善良似乎会对履行职务造成不便……\x02\x03",

            "和游击士不同，做这种工作的话，\x01",
            "必须要学会怀疑别人才行吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#6P#0011F呃……\x01",
            "你还真是一针见血啊。\x02\x03",

            "#0006F嗯～看来我\x01",
            "确实是太天真了吧……\x02\x03",

            "本以为通过警察学校的训练\x01",
            "已经彻底锻炼了自己……\x02\x03",

            "#0008F不过，光凭那些，\x01",
            "的确无法胜任搜查官的工作……\x02",
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
        "#6P#0005F缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "#0203F#11P……终端的检查工作\x01",
            "已经基本完毕了。\x02\x03",

            "#0200F明天好像还有\x01",
            "连接导力线路的工程，\x01",
            "今天我要早点休息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#0000F是吗……\x02\x03",

            "#0002F晚安。\x01",
            "好好休息哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "#0204F#11P好的。\x01",
            "那么我先回房间了──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1270, 255, 90, 0)    #voice#Tio
    Sleep(300)

    def lambda_531B():

        label("loc_531B")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_531B")

    QueueWorkItem2(0x101, 2, lambda_531B)

    def lambda_532D():
        OP_95(0xFE, 13300, 850, 11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_532D)
    WaitChrThread(0xB, 1)
    OP_68(13300, 1850, 9800, 2000)

    def lambda_535C():
        OP_97(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_535C)
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
            "#11P#0003F……看来他们三个\x01",
            "都已好好考虑过\x01",
            "自己该做的事情了呢。\x02\x03",

            "#0008F迷惘的只有我一个人而已吗……\x02\x03",

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
            "#11P#0006F……不行，\x01",
            "开始钻牛角尖了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    #C0153
    ChrTalk(
        0x101,
        "#5P#0000F还是出去吹吹风吧……\x02",
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

    # Function_20_4575 end

    def Function_21_54F1(): pass

    label("Function_21_54F1")

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

    def lambda_55AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_55AB)

    def lambda_55BC():
        OP_95(0xFE, 800, 40, 1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55BC)
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
        "#6P#0005F通讯器的铃声……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    def lambda_562D():
        OP_95(0xFE, 1800, 850, 10000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_562D)
    Sleep(800)
    OP_68(13800, 1850, 12000, 4000)
    SetCameraDistance(23000, 4000)
    WaitChrThread(0x101, 1)

    def lambda_5668():
        OP_95(0xFE, 11800, 850, 10000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5668)
    WaitChrThread(0x101, 1)

    def lambda_5686():
        OP_95(0xFE, 13800, 850, 12000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5686)
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
            "#0001F喂，您好。\x02\x03",

            "嗯……\x01",
            "这里是克洛斯贝尔警察局·特别\x01",
            "任务支援科的部门楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性的声音")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──罗伊德？\x01",
            "这声音是罗伊德吧？\x02",
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
            "#0005F什么……是塞茜尔姐姐吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性的声音")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呼，太好了……\x02\x03",

            "我联络过警察局那边，\x01",
            "结果他们告诉我这个号码。\x02\x03",

            "是叫『特别任务支援科』吧。\x01",
            "你被分到那个部门去了吗？\x02",
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
            "#0000F啊，不……\x01",
            "其实还没有正式决定。\x02\x03",

            "#0006F话说回来，对不起。\x01",
            "本来是打算回来之后就马上\x01",
            "去问候塞茜尔姐姐的……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性的声音")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没事，不用介意。\x02\x03",

            "倒是我，本该去车站\x01",
            "接你才对的……\x02",
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
            "#0000F这才真是不用费心啦。\x02\x03",

            "你的工作很忙吧？\x01",
            "等休假的时候再见面就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性的声音")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呜呜，罗伊德好冷淡……\x02\x03",

            "面对久别三年\x01",
            "不见的姐姐，\x01",
            "怎么这么无情嘛……\x02",
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
            "#0012F好啦好啦……\x01",
            "我会想办法抽出时间的。\x02\x03",

            "#0000F对了，我明天\x01",
            "也会去跟叔叔和阿姨打声招呼的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性的声音")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，也好。\x02\x03",

            "爸爸和妈妈也一直\x01",
            "都很挂念罗伊德的……\x02\x03",

            "不过，呵呵……好开心哦。\x02\x03",

            "你终于……\x01",
            "回到克洛斯贝尔了啊。\x02",
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
            "#0004F嗯……\x02\x03",

            "#0002F──我回来了，塞茜尔姐姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女性的声音")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "欢迎回来，罗伊德。\x07\x00\x02",
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

    # Function_21_54F1 end

    def Function_22_5BE9(): pass

    label("Function_22_5BE9")

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
        "──唔，情况我已经明白了。\x02",
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
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5DB8")

    #C0168
    ChrTalk(
        0x11,
        (
            "#5P#1004F嗯，以新人来说，\x01",
            "你们已经很努力了啊。\x02\x03",

            "#1002F而且，似乎也曾绞尽脑汁地\x01",
            "思考过各种对策呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#12P#0012F是、是啊……\x01",
            "（姑且算是在夸奖我们吧？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F0D")

    label("loc_5DB8")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5E63")

    #C0170
    ChrTalk(
        0x11,
        (
            "#5P#1003F算啦，以新人来说，\x01",
            "也算是马马虎虎吧。\x02\x03",

            "#1000F如果下次再碰上类似的事件，\x01",
            "应该能处理得更好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#12P#0005F是、是。\x01",
            "（还真是严厉啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F0D")

    label("loc_5E63")


    #C0172
    ChrTalk(
        0x11,
        (
            "#5P#1006F虽然结果还算不错，\x01",
            "不过办事方法实在是有点欠妥当啊……\x02\x03",

            "#1000F算了，你们毕竟是新人，\x01",
            "大概也就这点水平吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#12P#0006F……对不起。\x01",
            "（的确是有点草率……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F0D")

    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0174
    ChrTalk(
        0x11,
        (
            "#5P#1003F不过，通过这次事件，\x01",
            "你们应该也看清楚了吧。\x02\x03",

            "#1001F克洛斯贝尔这个地方\x01",
            "有着很棘手的一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#12P#0008F………这个…………\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#0306F嗯，的确是个\x01",
            "有点麻烦的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#4P#0211F各种阴暗面与阻碍……\x01",
            "感觉是让大人们的勾心斗角随意滋生的温床啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#0108F………是呀。\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x11,
        (
            "#5P#1000F警察局总部的人\x01",
            "也绝不是无能之辈。\x02\x03",

            "虽然似乎也有些\x01",
            "收受贿赂的蠢货……\x02\x03",

            "但大多数搜查官都很优秀，\x01",
            "而且有着自己的正义感。\x02\x03",

            "#1003F但是……面前总会矗立着各种有形无形的『壁障』。\x02\x03",

            "#1001F比如说，和黑手党有权钱交易的\x01",
            "议员与官员之流。\x02",
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
            "#5P#1002F怎么样，罗伊德？\x02\x03",

            "是不是想辞去警察的工作，\x01",
            "转职去当游击士了？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0182
    ChrTalk(
        0x101,
        (
            "#12P#0003F……不。\x02\x03",

            "#0000F正是因为有这些内情，\x01",
            "才需要『特别任务支援科』吧？\x02",
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

    def lambda_6244():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6244)
    Sleep(50)

    def lambda_6254():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6254)
    Sleep(50)

    def lambda_6264():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6264)
    WaitChrThread(0x102, 2)

    #C0183
    ChrTalk(
        0x11,
        "#5P#1005F哦……\x02",
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
            "#12P#0001F『守护民众』──\x01",
            "游击士的理念的确很正确，\x01",
            "但光靠这一点，也无法解决所有问题。\x02\x03",

            "#0003F走私贸易和违法的武器交易。\x02\x03",

            "赃物买卖及洗黑钱。\x02\x03",

            "再加上黑手党和政治家的暗中勾结……\x02\x03",

            "#0001F这些都是游击士\x01",
            "无法直接介入的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        "#2P#0305F的确……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        (
            "#4P#0203F游击士的力量\x01",
            "终究也是有极限的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#12P#0004F──但是，身为警察，\x01",
            "理应拥有解决这些问题的能力。\x02\x03",

            "#0000F虽然在现实中会有各种各样的\x01",
            "『壁障』阻挡在面前……\x02\x03",

            "但是，突破这些壁障的\x01",
            "可能性应该也并非为零。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#11P#0104F……原来如此。\x02\x03",

            "#0100F我们支援科说不定能\x01",
            "找出这种可能性……\x02\x03",

            "你就是这个意思吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0189
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯……\x01",
            "是不是有点乐观过头了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#4P#0204F……我认为，现实\x01",
            "可没有那么简单。\x02\x03",

            "#0202F只不过，任何可能性\x01",
            "都不会是零，这点的确没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        (
            "#11P#0304F哎呀呀……\x02\x03",

            "又是跟不良团伙的头目单挑，\x01",
            "又是主动去当危险的诱饵……\x02\x03",

            "#0302F看你一副认真沉稳的样子，\x01",
            "骨子里还真是个热血男儿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#6P#0005F我觉得这也\x01",
            "不算是热血吧……\x02\x03",

            "#0000F──不过，这次和大家\x01",
            "共事，让我重新认识到了这一点。\x02\x03",

            "#0004F虽然我们\x01",
            "都还有许多不成熟之处……\x02\x03",

            "#0002F但是，只要我们大家\x01",
            "齐心协力，无论多高的壁障\x01",
            "应该也都可以跨越。\x02",
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
        "#11P#0105F罗、罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        "#11P#0302F哈哈……该怎么说呢～\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        "#4P#0206F……太夸张了……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x11,
        "#5P#1004F哼哼哼……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0197
    ChrTalk(
        0x11,
        "#5P#1009F#4S哈～哈哈哈！\x02",
    )

    CloseMessageWindow()

    def lambda_67BF():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67BF)
    Sleep(50)

    def lambda_67CF():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_67CF)
    Sleep(50)

    def lambda_67DF():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_67DF)
    Sleep(50)

    def lambda_67EF():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_67EF)
    Sleep(300)

    #C0198
    ChrTalk(
        0x101,
        (
            "#12P#0011F也、也不用笑得这么厉害吧。\x02\x03",

            "#0006F嗯……\x01",
            "果然还是太过理想化了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x11,
        (
            "#5P#1004F呵呵……\x01",
            "算啦，这样也不错啊。\x02\x03",

            "#1002F虽说『特别任务支援科』\x01",
            "是在种种阻碍之下成立的部门……\x02\x03",

            "但是，要如何利用这片天地\x01",
            "却是你们的自由。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#12P#0002F啊……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x11,
        (
            "#5P#1004F虽然我可能不会\x01",
            "给你们提供直接帮助……\x02\x03",

            "不过，至少可以放放烟幕弹什么的，\x01",
            "让你们即使做得过头一点，\x01",
            "也不至于被高层找麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#12P#0000F科长……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#0102F呵呵……\x01",
            "说白了，就是放任主义吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#0306F真是的，道理倒是明白，\x01",
            "不过总觉得科长太随意了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#4P#0211F倒不如说，\x01",
            "科长只是怕麻烦而已吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x11,
        (
            "#5P#1002F哈，因为我是圆滑的大人嘛。\x02\x03",

            "#1003F到最后，『特别任务支援科』\x01",
            "是会成为游击士的仿制品……\x02\x03",

            "还是说，能找到\x01",
            "新的可能性呢……\x02\x03",

            "#1002F我就悠闲地抽着烟，\x01",
            "拭目以待吧。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B28")
    OP_29(0x2, 0x4, 0x40)
    Jump("loc_6B3A")

    label("loc_6B28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B3A")
    OP_29(0x2, 0x4, 0x40)

    label("loc_6B3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B58")
    OP_29(0x3, 0x4, 0x40)
    Jump("loc_6B6A")

    label("loc_6B58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B6A")
    OP_29(0x3, 0x4, 0x40)

    label("loc_6B6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B88")
    OP_29(0x4, 0x4, 0x40)
    Jump("loc_6B9A")

    label("loc_6B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B9A")
    OP_29(0x4, 0x4, 0x40)

    label("loc_6B9A")

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

    # Function_22_5BE9 end

    def Function_23_6C7D(): pass

    label("Function_23_6C7D")

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
            "#0003F（……艾莉吗……）\x02\x03",

            "#0008F（这两个月以来，我本以为\x01",
            "  大家的关系已经很亲密了……）\x02\x03",

            "（结果，真正关键的事情，\x01",
            "  彼此还是一无所知啊……）\x02\x03",

            "#0006F（麦克道尔市长的孙女，\x01",
            "  志向是当政治家吗……）\x02",
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
            "我记得，艾莉好像没上过\x01",
            "警察学校吧？\x02\x03",

            "你是怎么进入警察局工作的呢？\x02",
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
            "嗯～……\x01",
            "简单来说，算是社会实践吧。\x02\x03",

            "顺带一提，入职的测试项目\x01",
            "是笔记和射击……\x02\x03",

            "两项我都是满分，\x01",
            "所以警察局总部似乎也没法拒绝呢。\x02",
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
            "越、越听越觉得\x01",
            "我和你不是一个层次的人啊……\x02",
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
            "哎呀，你不也很厉害嘛，\x01",
            "身为新人就取得搜查官资格，\x01",
            "这也是很少见的吧？\x02\x03",

            "其中一定也有什么隐情吧？\x02",
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
            "……这个………\x02",
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
            "呵呵……\x02\x03",

            "看来，更多详情还是等\x01",
            "正式成为同事以后再问为好呢。\x02",
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
            "#0000F──好。\x02",
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
            "#0004F#5P（去和艾莉谈谈看吧。）\x02\x03",

            "（想知道她在烦恼些什么啊……\x01",
            "  而且，我说不定也能帮上忙。）\x02\x03",

            "#0000F（另外，那时的话题\x01",
            "  差不多也可以继续了吧……？）\x02",
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

    # Function_23_6C7D end

    def Function_24_71D5(): pass

    label("Function_24_71D5")

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
        "#4P#0003F（好……）\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 163700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x101,
        (
            "#4P#0000F──艾莉。\x01",
            "可以打扰一下吗？\x02",
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
            "#4P#0005F（没有反应……已经睡了吗？）\x02\x03",

            "#0008F（不……\x01",
            "  里面好像一点声息都没有啊。）\x02\x03",

            "#0001F不好意思，我开门了哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x5)

    def lambda_7326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7326)

    def lambda_7337():
        OP_95(0xFE, 163700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7337)
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

    def lambda_73BA():
        OP_96(0xFE, 0x26160, 0x0, 0x1DA9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73BA)

    def lambda_73D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_73D4)
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
            "#0008F（不在……\x01",
            "  去哪里了呢？）\x02\x03",

            "#0000F（……还是去找找看吧。）\x02",
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

    # Function_24_71D5 end

    def Function_25_746A(): pass

    label("Function_25_746A")

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
    MenuCmd(1, 0, "【概要·沿革】")
    MenuCmd(1, 0, "【武装·势力范围】")
    MenuCmd(1, 0, "【马尔克尼会长】")
    MenuCmd(1, 0, "【加尔西亚·罗西】")
    MenuCmd(1, 0, "【哈尔特曼议长】")
    MenuCmd(1, 0, "【放弃阅览】")
    MenuCmd(3, 0, 0x5)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Sleep(1000)

    #A0220
    AnonymousTalk(
        0x103,
        (
            "#0203F──记录结晶已连接。\x02\x03",

            "#0200F这样就可以\x01",
            "访问里面的项目了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0221
    AnonymousTalk(
        0x101,
        "#0001F还挺齐全呢……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0222
    AnonymousTalk(
        0x102,
        (
            "#0103F关于『鲁巴彻』的情报，\x01",
            "一直有许多不明之处……\x02\x03",

            "#0101F说不定这还是我们第一次\x01",
            "看到如此完整的信息呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0223
    AnonymousTalk(
        0x104,
        (
            "#0300F那么，\x01",
            "就从头到尾看一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0224
    AnonymousTalk(
        0x101,
        "#0001F嗯……\x02",
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

    label("loc_77D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7894")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【概要·沿革】")
    MenuCmd(1, 0, "【武装·势力范围】")
    MenuCmd(1, 0, "【马尔克尼会长】")
    MenuCmd(1, 0, "【加尔西亚·罗西】")
    MenuCmd(1, 0, "【哈尔特曼议长】")
    MenuCmd(1, 0, "【放弃阅览】")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_787F")
    Jump("loc_7883")

    label("loc_787F")

    MenuCmd(3, 0, 0x5)

    label("loc_7883")

    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Jump("loc_7897")

    label("loc_7894")

    SetScenarioFlags(0x1, 0)

    label("loc_7897")

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_78CB"),
        (1, "loc_7BC3"),
        (2, "loc_7EF8"),
        (3, "loc_828F"),
        (4, "loc_861F"),
        (5, "loc_8A24"),
        (SWITCH_DEFAULT, "loc_8ACA"),
    )


    label("loc_78CB")

    MenuTitle(-1, 30, 0, "概要·沿革")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "克洛斯贝尔自治州现存的\x01",
            "最大黑手党组织。\x02\x03",

            "其历史悠久，推测可追溯到\x01",
            "自治州成立的七耀历１１３０年前后。\x02\x03",

            "从其冠名为『商会』也可获知，\x01",
            "起初是通过在帝国——共和国之间进行走私贸易\x01",
            "而发迹，随后则一手掌握了自治州黑道势力的霸权。\x02\x03",

            "目前，其非法贸易的范围已经十分广泛。\x01",
            "已确认的有武器走私贸易、赃物买卖、炒地皮、\x01",
            "破坏股东大会、洗黑钱、各种不良业、\x01",
            "猎兵团的中介斡旋等。\x02\x03",

            "由于与权威议员关系密切，\x01",
            "其犯罪行为大多免受揭发，\x01",
            "多数情况下，即使成员被捕，\x01",
            "也很快就能获得保释。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BBE")

    #A0226
    AnonymousTalk(
        0x101,
        (
            "#0005F原来如此……\x01",
            "情报整理得很好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0227
    AnonymousTalk(
        0x102,
        (
            "#0100F感觉把以前听到的消息\x01",
            "都系统准确地总结出来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0228
    AnonymousTalk(
        0x103,
        (
            "#0206F话说……重新看下来，\x01",
            "果然是个不得了的组织啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0229
    AnonymousTalk(
        0x104,
        (
            "#0301F嗯，看起来，他们似乎在通过\x01",
            "非法贸易而大肆牟取暴利啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 2)

    label("loc_7BBE")

    Jump("loc_8ACA")

    label("loc_7BC3")

    MenuTitle(-1, 30, 0, "武装·势力范围")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "成员人数约三百名。\x01",
            "如果算上自治州内外的底层成员，\x01",
            "推测有五百名以上。\x02\x03",

            "其中，出身于猎兵团和周边国家军队的成员也为数众多，\x01",
            "再加上，此组织也从事最新导力兵器的走私，\x01",
            "因而拥有相当的战斗力。\x02\x03",

            "此组织并非单纯的大型暴力组织，\x01",
            "其影响力并不局限于克洛斯贝尔，\x01",
            "与帝国及共和国的当权者也有十分密切的关系。\x02\x03",

            "根据最新情报，虽然一度有被敌对组织\x01",
            "『黑月』压制的迹象，\x01",
            "但通过导入军犬而增强了战斗力后，\x01",
            "可以判断为，已经再度取回了优势。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF3")

    #A0231
    AnonymousTalk(
        0x101,
        (
            "#0001F这样看来……\x01",
            "鲁巴彻果然是很庞大的组织啊。\x02\x03",

            "而且，其中好像有很多\x01",
            "出身军队的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0232
    AnonymousTalk(
        0x104,
        (
            "#0303F嗯，难怪以前和他们的底层人员\x01",
            "战斗时，觉得那么棘手啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0233
    AnonymousTalk(
        0x103,
        (
            "#0203F话说回来，那时的军犬……\x01",
            "似乎已经正式投入使用了呢。\x02\x03",

            "#0211F我们逮捕了那些人，\x01",
            "也都是白费了力气吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0234
    AnonymousTalk(
        0x101,
        "#0006F是啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0235
    AnonymousTalk(
        0x102,
        "#0106F感觉有点失落呢……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 3)

    label("loc_7EF3")

    Jump("loc_8ACA")

    label("loc_7EF8")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "马尔克尼会长")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "鲁巴彻商会的代表，\x01",
            "支配此黑手党组织的人物。\x02\x03",

            "虽然身为鲁巴彻的第五代会长，\x01",
            "但并未经过正式的继任程序，\x01",
            "而是在八年前左右，使用计谋和背叛手段，\x01",
            "将第四代会长赶下台，从而掌握了组织的领导权。\x02\x03",

            "不知是否由于其本身为帝国系移民，\x01",
            "似乎更重视与帝国派议员的关系，\x01",
            "特别是与哈尔特曼议长的关系十分密切。\x02\x03",

            "另一方面，也努力保持了共和国方面的人脉，\x01",
            "从此种意义上来说，在克洛斯贝尔这个特殊地域，\x01",
            "此人可谓是毫无破绽，从而得以横行州内，畅通无阻。\x02\x03",

            "同时，似乎对帝国贵族怀有憧憬，\x01",
            "所以喜欢低级趣味的，暴发户风格的服装和家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8277")

    #A0237
    AnonymousTalk(
        0x104,
        (
            "#0305F这个……\x01",
            "怎么说呢，这大叔给人的印象还真很深刻啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0238
    AnonymousTalk(
        0x103,
        (
            "#0211F虽然外表很可笑，\x01",
            "但做事可是毫不手软啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0239
    AnonymousTalk(
        0x102,
        (
            "#0103F而且，似乎比想象中的\x01",
            "更加圆滑狡诈呢。\x02\x03",

            "#0101F偏向帝国，却也掌握了\x01",
            "共和国方面的人脉……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0240
    AnonymousTalk(
        0x101,
        "#0001F看来是个相当难缠的对手啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 4)

    label("loc_8277")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_8ACA")

    label("loc_828F")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis053.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "加尔西亚·罗西")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "鲁巴彻商会的营业总部部长，\x01",
            "兼任此黑手党组织副头目的人物。\x02\x03",

            "原本是猎兵团『西风旅团』的部队长，\x01",
            "八年前，在马尔克尼陷害上代会长时，\x01",
            "作为其执行部队的负责人被雇佣。\x02\x03",

            "其后被马尔克尼挖角，\x01",
            "脱离猎兵团，跳槽到鲁巴彻商会。\x01",
            "为黑手党的武装化和战斗力强化做出了贡献。\x02\x03",

            "在猎兵时代，人称『杀戮之熊』，\x01",
            "相传，曾以充分发挥了其巨大体格优势的\x01",
            "军用格斗术屠戮了众多敌兵。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8607")

    #A0242
    AnonymousTalk(
        0x102,
        (
            "#0105F那个副头目……\x01",
            "原来是猎兵团出身啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0243
    AnonymousTalk(
        0x103,
        (
            "#0208F『西风旅团』……\x01",
            "好像曾在哪里听过呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0244
    AnonymousTalk(
        0x104,
        (
            "#0303F……在大陆西部，\x01",
            "那是人称最强的猎兵团之一。\x02\x03",

            "既然曾经是那里的部队长，\x01",
            "想必拥有相当强的战斗力。\x02\x03",

            "#0301F『杀戮之熊』这名号，\x01",
            "我也听过不止一次了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0245
    AnonymousTalk(
        0x101,
        (
            "#0001F是吗……\x01",
            "他的确是有着很强的魄力呢。\x02\x03",

            "#0005F不过，兰迪你\x01",
            "果然对这些事很清楚啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0246
    AnonymousTalk(
        0x104,
        (
            "#0304F哈哈……\x01",
            "只是以前听过一些传闻罢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 5)

    label("loc_8607")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_8ACA")

    label("loc_861F")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis054.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "哈尔特曼议长")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "担任克洛斯贝尔自治州议会\x01",
            "议长的重量级政治家。\x02\x03",

            "同时也是自治州政府的代表之一，\x01",
            "担任帝国派议员的领袖。\x02\x03",

            "出身于和帝国贵族有关系的名门，\x01",
            "在自治州的疗养地米修拉姆\x01",
            "拥有极其奢华的巨大宅邸。\x02\x03",

            "与鲁巴彻的马尔克尼会长\x01",
            "是旧识，在各种权钱交易、走私贸易、\x01",
            "洗黑钱等活动中，\x01",
            "均与其有着密切的合作关系。\x02\x03",

            "此外，去年曾与帝国宰相\x01",
            "吉利亚斯·奥斯本进行了非正式会谈，\x01",
            "再次向自治州内外显示了其权威。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A0C")

    #A0248
    AnonymousTalk(
        0x101,
        "#0005F这就是哈尔特曼议长……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0249
    AnonymousTalk(
        0x104,
        (
            "#0301F怎么说呢，与其说是政治家，\x01",
            "不如说感觉更像帝国的大贵族呢。\x02\x03",

            "不过，竟然还会见了那个『铁血宰相』，\x01",
            "这是真的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0250
    AnonymousTalk(
        0x102,
        (
            "#0103F嗯，虽然是非正式的，\x01",
            "但在去年春天的时候，奥斯本宰相\x01",
            "确实来过克洛斯贝尔。\x02\x03",

            "#0101F连外公都没有会见，\x01",
            "与哈尔特曼议长进行过会谈之后\x01",
            "就马上回国了……\x02\x03",

            "一时间，各国的政界\x01",
            "似乎都对此事议论纷纷呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0251
    AnonymousTalk(
        0x101,
        (
            "#0001F竟然有这种事吗……\x02\x03",

            "#0008F『铁血宰相』……\x01",
            "好像是个很有名的人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0252
    AnonymousTalk(
        0x103,
        (
            "#0203F他为何要来访问，\x01",
            "这点令人有些在意呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 6)

    label("loc_8A0C")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_8ACA")

    label("loc_8A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA4")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "◆看完所有项目\x01",        # 0
            "◆未看完所有项目\x01",      # 1
            "◆无变更\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8A7C"),
        (1, "loc_8A90"),
        (SWITCH_DEFAULT, "loc_8AA4"),
    )


    label("loc_8A7C")

    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Jump("loc_8AA4")

    label("loc_8A90")

    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    Jump("loc_8AA4")

    label("loc_8AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AC5")
    SetScenarioFlags(0x0, 7)
    Jump("loc_8AC5")

    label("loc_8AC5")

    Jump("loc_8ACA")

    label("loc_8ACA")

    Jump("loc_77D5")

    label("loc_8ACF")

    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MenuCmd(4, 0, 0x0)

    #C0253
    ChrTalk(
        0x101,
        (
            "#6P#0003F──原来如此。\x02\x03",

            "#0001F之前一直不甚明了的地方，\x01",
            "如今也已经了解得相当透彻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        (
            "#6P#0106F嗯……\x02\x03",

            "#0108F冷酷而思考周密的顶层，\x01",
            "和身经百战的前猎兵副头目……\x02\x03",

            "#0101F以及与哈尔特曼议长的密切关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#0306F而且，那个议长\x01",
            "似乎和那个『铁血宰相』\x01",
            "还有什么关系吧？\x02\x03",

            "这样的话，克洛斯贝尔的警察\x01",
            "完全无从下手，也就可以理解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#6P#0008F……是啊………\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x103,
        (
            "#0205F#5P……请等一下。\x02\x03",

            "#0201F这个记录结晶里\x01",
            "还有隐藏数据。\x02",
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
        "#6P#0005F隐藏数据……？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#0301F嘿，要说隐藏的话，\x01",
            "也只能是那个小鬼藏起来的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#0206F#5P嗯，他似乎是想\x01",
            "试探我能不能发现。\x02\x03",

            "#0211F……稍后有必要给他点教训呢。\x02",
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
            "#6P#0000F这个暂且不提……\x01",
            "那个隐藏数据也能看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        "#0202F#5P嗯，简单至极。\x02",
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
    MenuCmd(1, 0, "【概要·沿革】")
    MenuCmd(1, 0, "【武装·势力范围】")
    MenuCmd(1, 0, "【马尔克尼会长】")
    MenuCmd(1, 0, "【加尔西亚·罗西】")
    MenuCmd(1, 0, "【哈尔特曼议长】")
    MenuCmd(1, 0, "【黑之竞拍会】")
    MenuCmd(1, 0, "【放弃阅览】")
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

            "#0013F#3S这是……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0264
    AnonymousTalk(
        0x102,
        "#0101F『黑之竞拍会』……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0265
    AnonymousTalk(
        0x104,
        (
            "#0305F就是艾丝蒂尔他们\x01",
            "曾提到过的那个活动吧。\x02\x03",

            "#0309F哈哈，那个臭小鬼，\x01",
            "还会搞这种小把戏啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0266
    AnonymousTalk(
        0x103,
        (
            "#0203F……看来那个活动\x01",
            "是真实存在的啊。\x02\x03",

            "#0201F而且还和鲁巴彻有关吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0267
    AnonymousTalk(
        0x101,
        (
            "#0006F嗯……\x01",
            "我之前就觉得很可疑了。\x02\x03",

            "#0001F好──总之，先看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x0, 7)
    ClearMapFlags(0x400)

    label("loc_909F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_9152")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【概要·沿革】")
    MenuCmd(1, 0, "【武装·势力范围】")
    MenuCmd(1, 0, "【马尔克尼会长】")
    MenuCmd(1, 0, "【加尔西亚·罗西】")
    MenuCmd(1, 0, "【哈尔特曼议长】")
    MenuCmd(1, 0, "【黑之竞拍会】")
    MenuCmd(1, 0, "【放弃阅览】")
    MenuCmd(3, 0, 0x6)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Jump("loc_9155")

    label("loc_9152")

    SetScenarioFlags(0x1, 0)

    label("loc_9155")

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_918F"),
        (1, "loc_9390"),
        (2, "loc_956A"),
        (3, "loc_97EA"),
        (4, "loc_99D8"),
        (5, "loc_9BDE"),
        (6, "loc_9FE3"),
        (SWITCH_DEFAULT, "loc_9FE8"),
    )


    label("loc_918F")

    MenuTitle(-1, 30, 0, "概要·沿革")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "克洛斯贝尔自治州现存的\x01",
            "最大黑手党组织。\x02\x03",

            "其历史悠久，推测可追溯到\x01",
            "自治州成立的七耀历１１３０年前后。\x02\x03",

            "从其冠名为『商会』也可获知，\x01",
            "起初是通过在帝国——共和国之间进行走私贸易\x01",
            "而发迹，随后则一手掌握了自治州黑道势力的霸权。\x02\x03",

            "目前，其非法贸易的范围已经十分广泛。\x01",
            "已确认的有武器走私贸易、赃物买卖、炒地皮、\x01",
            "破坏股东大会、洗黑钱、各种不良业、\x01",
            "猎兵团的中介斡旋等。\x02\x03",

            "由于与权威议员关系密切，\x01",
            "其犯罪行为大多免受揭发，\x01",
            "多数情况下，即使成员被捕，\x01",
            "也很快就能获得保释。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_9FE8")

    label("loc_9390")

    MenuTitle(-1, 30, 0, "武装·势力范围")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "成员人数约三百名。\x01",
            "如果算上自治州内外的底层成员，\x01",
            "推测有五百名以上。\x02\x03",

            "其中，出身于猎兵团和周边国家军队的成员也为数众多，\x01",
            "再加上，此组织也从事最新导力兵器的走私，\x01",
            "因而拥有相当的战斗力。\x02\x03",

            "此组织并非单纯的大型暴力组织，\x01",
            "其影响力并不局限于克洛斯贝尔，\x01",
            "与帝国及共和国的当权者也有十分密切的关系。\x02\x03",

            "根据最新情报，虽然一度有被敌对组织\x01",
            "『黑月』压制的迹象，\x01",
            "但通过导入军犬而增强了战斗力后，\x01",
            "可以判断为，已经再度取回了优势。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_9FE8")

    label("loc_956A")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "马尔克尼会长")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "鲁巴彻商会的代表，\x01",
            "支配此黑手党组织的人物。\x02\x03",

            "虽然身为鲁巴彻的第五代会长，\x01",
            "但并未经过正式的继任程序，\x01",
            "而是在八年前左右，使用计谋和背叛手段，\x01",
            "将第四代会长赶下台，从而掌握了组织的领导权。\x02\x03",

            "不知是否由于其本身为帝国系移民，\x01",
            "似乎更重视与帝国派议员的关系，\x01",
            "特别是与哈尔特曼议长的关系十分密切。\x02\x03",

            "另一方面，也努力保持了共和国方面的人脉，\x01",
            "此种意义上来说，在克洛斯贝尔这个特殊地域\x01",
            "此人可谓是毫无破绽，从而得以横行州内，畅通无阻。\x02\x03",

            "同时，似乎对帝国贵族怀有憧憬，\x01",
            "所以喜欢低级趣味的，暴发户风格的服装和家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_9FE8")

    label("loc_97EA")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis053.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "加尔西亚·罗西")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "鲁巴彻商会的营业总部部长\x01",
            "兼任此黑手党组织副头目的人物。\x02\x03",

            "原本是猎兵团『西风旅团』的部队长，\x01",
            "八年前，在马尔克尼陷害上代会长时，\x01",
            "作为其执行部队的负责人被雇佣。\x02\x03",

            "其后被马尔克尼挖角，\x01",
            "脱离猎兵团，跳槽到鲁巴彻商会。\x01",
            "为黑手党的武装化和战斗力強化做出了贡献。\x02\x03",

            "在猎兵时代，人称『杀戮之熊』，\x01",
            "相传，曾以充分发挥了其巨大体格优势的\x01",
            "军用格斗术屠戮了众多敌兵。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_9FE8")

    label("loc_99D8")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis054.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "哈尔特曼议长")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "担任克洛斯贝尔自治州议会\x01",
            "议长的重量级政治家。\x02\x03",

            "同时也是自治州政府的代表之一，\x01",
            "担任帝国派议员的领袖。\x02\x03",

            "出身于和帝国贵族有关系的名门，\x01",
            "在自治州的疗养地米修拉姆\x01",
            "拥有极其奢华的巨大宅邸。\x02\x03",

            "和鲁巴彻的马尔克尼会长\x01",
            "是旧识，在各种权钱交易、走私贸易、\x01",
            "洗黑钱等活动中\x01",
            "均与其有着密切的合作关系。\x02\x03",

            "此外，去年曾与帝国宰相\x01",
            "吉利亚斯·奥斯本进行了非正式会谈，\x01",
            "再次向自治州内外显示了其权威。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_9FE8")

    label("loc_9BDE")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis055.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "黑之竞拍会")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "在每年的创立纪念庆典最终日，\x01",
            "由鲁巴彻所举办的竞拍会。\x02\x03",

            "举办地点为哈尔特曼议长位于\x01",
            "疗养地米修拉姆的豪宅。\x02\x03",

            "参展商品都是价值不菲的珍品，\x01",
            "但多数是赃物，或是与贿赂、逃税、贪污\x01",
            "等违法行为有所关联的美术品、绘画和珠宝饰品。\x02\x03",

            "与会客人不仅包括克洛斯贝尔本地人士，\x01",
            "还有众多周边诸国的贵族和资产家，\x01",
            "所以此竞拍会同时也是一场地下社交活动。\x02\x03",

            "对鲁巴彻来说，是重要的收入来源，\x01",
            "对哈尔特曼议长而言，似乎是\x01",
            "与各国的权威人士建立关系的绝好机会。\x02\x03",

            "同时，拍卖会场的保安工作\x01",
            "由鲁巴彻的成员严格执行，\x01",
            "据说，如果没有印着『金色蔷薇』的邀请卡，\x01",
            "就绝对无法进入场内。\x07\x00\x02",
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
        "#0007F这、这是……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0275
    AnonymousTalk(
        0x102,
        (
            "#0105F难、难以置信……\x02\x03",

            "#0101F这种活动\x01",
            "居然每年都举行……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0276
    AnonymousTalk(
        0x103,
        (
            "#0201F可是，有点奇怪。\x02\x03",

            "虽说是秘密进行，\x01",
            "但这个活动的规模相当之大……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0277
    AnonymousTalk(
        0x104,
        (
            "#0306F呼，一定是对警察和媒体界人士的行动\x01",
            "进行了严格的限制吧。\x02\x03",

            "#0301F否则，这种事情\x01",
            "是不可能不被公之于众的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("男性的声音")

    #A0278
    AnonymousTalk(
        0xFF,
        "──说得没错。\x02",
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
    Jump("loc_9FE8")

    label("loc_9FE3")

    Jump("loc_9FE8")

    label("loc_9FE8")

    Jump("loc_909F")

    label("loc_9FED")

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

    def lambda_A07B():
        OP_95(0xFE, 10500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A07B)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MenuCmd(4, 0, 0x0)

    def lambda_A0AC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A0AC)
    Sleep(50)

    def lambda_A0BC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A0BC)
    Sleep(50)

    def lambda_A0CC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A0CC)
    Sleep(50)

    def lambda_A0DC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A0DC)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x11, 1)

    #C0280
    ChrTalk(
        0x101,
        "#0005F#11P科长……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        "#11P#0108F您、您辛苦了。\x02",
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
            "哎呀呀……\x01",
            "没想到你们凭借一己之力，\x01",
            "竟能调查到这个地步。\x02\x03",

            "也罢，这里不太方便。\x02\x03",

            "去那边房间里再好好说吧。\x02",
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
            "#12P#0013F──这么说，\x01",
            "那个文件夹里的情报\x01",
            "全部是事实吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        (
            "#5P#1003F嗯，没错。\x02\x03",

            "#1002F虽然不知道是谁查出来的，\x01",
            "但总结得倒是相当准确嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x102,
        (
            "#0106F可、可是……\x02\x03",

            "#0101F这些情报，警察局的高层\x01",
            "全都有所掌握吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x11,
        (
            "#5P#1003F嗯，虽然还不至于所有人都知道。\x02\x03",

            "#1001F警督级别以上的人自不必说，\x01",
            "一科的人应该也都知道的。\x02\x03",

            "游击士协会的接待员，\x01",
            "还有亚里欧斯他们\x01",
            "大概也早就知道了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0010F唔……\x01",
            "这也是所谓的『壁障』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x11,
        (
            "#5P#1011F嗯……而且还是无比巨大的『壁障』。\x02\x03",

            "#1001F基本上，我是不打算\x01",
            "限制你们的行动的……\x02\x03",

            "不过，只有这个『黑之竞拍会』，\x01",
            "劝你们还是不要插手了。\x02\x03",

            "对你们来说，负担太重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        "#12P#0007F但、但是……！\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        (
            "#0303F喂喂，科长，\x01",
            "你说得好像不太准确啊。\x02\x03",

            "#0301F并不是对我们来说负担太重，\x01",
            "而是警察本身就无法行动吧？\x02",
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
            "#0108F招待了那么多权威人士，\x01",
            "而且，实质上的主办者之一\x01",
            "正是那个哈尔特曼议长……\x02\x03",

            "#0106F……根本就不可能采取任何行动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#12P#0206F只要没威胁到民间人士的安全，\x01",
            "连游击士协会也无法行动……\x02\x03",

            "就是说，任何人都无法插手吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        "#12P#0010F话、话虽如此……！\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x11,
        (
            "#5P#1003F……觉得懊恼不甘的\x01",
            "可不止是你们。\x02\x03",

            "特别是一科的那些人，\x01",
            "恐怕每年都会恨得咬牙切齿吧。\x02\x03",

            "#1001F若是有违人道的活动，\x01",
            "就算只是为了赌上一口气，也要在\x01",
            "游击士协会行动之前先除掉他们……\x02\x03",

            "可是，除了拍卖品是『黑货』以外，\x01",
            "那纯粹只是个豪华的宴会罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#12P#0008F唔……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x11,
        (
            "#5P#1003F说实话，若是轻举妄动，\x01",
            "很可能会毁了整个支援科。\x02\x03",

            "所以，唯独这次，\x01",
            "我也不得不阻止你们了。\x02\x03",

            "#1000F嗯，言尽于此。\x02",
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
        "#0303F唉……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x103,
        "#12P#0203F……真是没办法。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x11,
        "#5P#1001F──我并没说过要你们就此接受现实。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x11,
        (
            "#5P#1001F然而，有些时候，也需要直面现实，\x01",
            "看清楚自己究竟能够\x01",
            "做到什么地步。\x02\x03",

            "只要不把这份懊悔的感觉遗忘，\x01",
            "总有一天，一定能找到机会的。\x02\x03",

            "#1004F当然了，前提是你们坚持不懈，永不放弃。\x02",
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
            "#12P#0006F#40W……我、我明白了。\x02\x03",

            "#0008F#30W关于这件事……\x01",
            "我们就不插手了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA41():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AA41)
    Sleep(50)

    def lambda_AA51():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AA51)
    Sleep(50)

    def lambda_AA61():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AA61)
    Sleep(300)

    #C0306
    ChrTalk(
        0x102,
        "#0108F#11P罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        "#12P#0208F……罗伊德前辈。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        "#0306F真是……没办法啊。\x02",
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
            "就这样……\x01",
            "纪念庆典的第三天过去了。\x02\x03",

            "缇欧的过去，大哥未知的经历，\x01",
            "名为小猫的神秘黑客，\x01",
            "关于鲁巴彻的详细情报……\x02\x03",

            "──还有展现了克洛斯贝尔种种扭曲现状的\x01",
            "『黑之竞拍会』。\x02\x03",

            "脑海中不断回想着这些事情，\x01",
            "罗伊德不知不觉地进入了梦乡──\x07\x00\x02",
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

    # Function_25_746A end

    def Function_26_AC40(): pass

    label("Function_26_AC40")

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
        "#1P#0002F呼，我们回来了。\x02",
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
        "#5P#1110F啊，回来了！\x02",
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
            "#12P#0012F#11P哈哈……\x01",
            "琪雅总是充满活力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "#1109F#5P嗯！\x01",
            "琪雅很有活力哦～\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)

    def lambda_AEB6():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_AEB6)
    WaitChrThread(0xD, 1)
    SetChrFlags(0xD, 0x40)

    #C0314
    ChrTalk(
        0xD,
        (
            "#1110F#5P罗伊德，你们回来得好晚哦～\x01",
            "工作很忙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#0102F#11P呵呵，还好吧。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#0309F#11P嗯，今天行动时都有车坐，\x01",
            "从这点来说，真是得救了。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        "#12P#0203F是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AF9B():

        label("loc_AF9B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_AF9B")

    QueueWorkItem2(0x101, 2, lambda_AF9B)

    def lambda_AFAD():

        label("loc_AFAD")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_AFAD")

    QueueWorkItem2(0x102, 2, lambda_AFAD)

    def lambda_AFBF():

        label("loc_AFBF")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_AFBF")

    QueueWorkItem2(0x103, 2, lambda_AFBF)

    def lambda_AFD1():

        label("loc_AFD1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_AFD1")

    QueueWorkItem2(0x104, 2, lambda_AFD1)
    OP_68(200, 1000, 2500, 1500)

    def lambda_AFF4():
        OP_95(0xFE, -900, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_AFF4)
    WaitChrThread(0xD, 1)

    def lambda_B012():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B012)
    WaitChrThread(0xD, 1)
    TurnDirection(0xD, 0x103, 500)

    #C0318
    ChrTalk(
        0xD,
        (
            "#6P#1112F那个，缇欧～\x02\x03",

            "你看起来好累啊，\x01",
            "没事吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0319
    ChrTalk(
        0x103,
        (
            "#0204F#11P嗯……没问题。\x02\x03",

            "#0202F一看到琪雅的脸，\x01",
            "我就有精神了。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xD,
        "#6P#1111F嗯～……\x02",
    )

    CloseMessageWindow()
    OP_68(500, 1000, 2500, 600)

    def lambda_B0F1():
        OP_95(0xFE, -300, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B0F1)
    WaitChrThread(0xD, 1)

    def lambda_B10F():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B10F)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    Sound(804, 0, 100, 0)
    Sound(910, 0, 100, 0)
    Sleep(500)

    #C0321
    ChrTalk(
        0x103,
        "#0205F#11P琪、琪雅……！？\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xD,
        (
            "#6P#1109F琪雅有很多活力，\x01",
            "所以也分给缇欧一点哦！\x02\x03",

            "#1104F嗯～（蹭蹭）\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        "#0202F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        "#5P#0009F哈哈，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        "#0304F#11P看来这招会很管用啊。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        (
            "#5P#0109F呵呵，说不定是\x01",
            "无与伦比的特效药呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x103,
        (
            "#0204F#11P……谢谢你，琪雅。\x02\x03",

            "#0202F我觉得有精神多了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)

    def lambda_B278():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B278)
    WaitChrThread(0xD, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    #C0328
    ChrTalk(
        0xD,
        "#6P#1110F嘿嘿，是吗～\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0329
    ChrTalk(
        0x101,
        (
            "#5P#0000F说起来……\x01",
            "科长还没回来吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    #C0330
    ChrTalk(
        0xD,
        (
            "#6P#1100F科长他\x01",
            "在那边的房间里哦～\x02\x03",

            "刚才来了客人，\x01",
            "他们好像在谈话。\x02",
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
            "#5P#0005F客人？\x01",
            "这么晚来，真少见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        "#5P#0100F是怎样的人呢？\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xD,
        (
            "#6P#1103F嗯～长了好多胡子，\x01",
            "看起来像熊一样的叔叔。\x02\x03",

            "#1110F科长好像叫他\x01",
            "律师呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#5P#0000F啊，是伊安律师吗？\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        "#0300F#11P真少见啊，这么晚来。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#5P#0100F看来，我们也去\x01",
            "打个招呼比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0337
    ChrTalk(
        0x103,
        (
            "#12P#0202F我今天负责做晚饭，\x01",
            "所以那边就交给大家了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0338
    ChrTalk(
        0x101,
        (
            "#5P#0001F没问题吗？\x01",
            "不然，我可以代替你\x01",
            "做晚饭的……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x103,
        (
            "#12P#0204F不用，反正事前准备\x01",
            "都已经做好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xD, 500)
    Sleep(300)

    #C0340
    ChrTalk(
        0x103,
        (
            "#0202F#11P琪雅，晚饭\x01",
            "还要再等一下哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x103, 500)

    #C0341
    ChrTalk(
        0xD,
        (
            "#6P#1109F啊，那琪雅\x01",
            "也要来帮忙～！\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#0205F#11P是吗……？\x02\x03",

            "#0204F呵呵，那就\x01",
            "麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B5F8():

        label("loc_B5F8")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_B5F8")

    QueueWorkItem2(0x101, 2, lambda_B5F8)

    def lambda_B60A():

        label("loc_B60A")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_B60A")

    QueueWorkItem2(0x102, 2, lambda_B60A)

    def lambda_B61C():

        label("loc_B61C")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_B61C")

    QueueWorkItem2(0x104, 2, lambda_B61C)
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

    # Function_26_AC40 end

    def Function_27_B73D(): pass

    label("Function_27_B73D")

    SetChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    Sound(51, 0, 100, 0)
    Sound(58, 0, 100, 0)

    def lambda_B75B():
        OP_95(0xFE, 2800, 0, 5500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B75B)
    WaitChrThread(0xD, 1)
    OP_68(200, 1000, 3500, 1500)
    SetCameraDistance(23000, 1500)

    def lambda_B793():
        OP_95(0xFE, 900, 0, 4900, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B793)
    WaitChrThread(0xD, 1)

    def lambda_B7B1():
        OP_95(0xFE, 200, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B7B1)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    Sound(819, 0, 100, 0)

    def lambda_B7DD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_B7DD)

    def lambda_B7EA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B7EA)
    Sleep(500)
    Return()

    # Function_27_B73D end

    def Function_28_B802(): pass

    label("Function_28_B802")


    def lambda_B807():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B807)

    def lambda_B821():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B821)
    Sleep(250)

    def lambda_B835():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B835)

    def lambda_B84F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B84F)
    Sleep(400)

    def lambda_B863():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B863)

    def lambda_B87D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B87D)
    Sleep(250)

    def lambda_B891():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B891)

    def lambda_B8AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B8AB)
    WaitChrThread(0x101, 1)

    def lambda_B8C0():

        label("loc_B8C0")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_B8C0")

    QueueWorkItem2(0x101, 2, lambda_B8C0)
    WaitChrThread(0x102, 1)

    def lambda_B8D6():

        label("loc_B8D6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_B8D6")

    QueueWorkItem2(0x102, 2, lambda_B8D6)
    WaitChrThread(0x103, 1)

    def lambda_B8EC():

        label("loc_B8EC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_B8EC")

    QueueWorkItem2(0x103, 2, lambda_B8EC)
    WaitChrThread(0x104, 1)

    def lambda_B902():

        label("loc_B902")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_B902")

    QueueWorkItem2(0x104, 2, lambda_B902)
    Return()

    # Function_28_B802 end

    def Function_29_B910(): pass

    label("Function_29_B910")


    def lambda_B915():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B915)
    WaitChrThread(0xD, 1)

    def lambda_B933():
        OP_95(0xFE, 400, 0, 6600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B933)
    WaitChrThread(0xD, 1)

    def lambda_B951():
        OP_95(0xFE, 3500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B951)
    WaitChrThread(0xD, 1)

    def lambda_B96F():
        OP_95(0xFE, 8500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B96F)
    WaitChrThread(0xD, 1)
    Return()

    # Function_29_B910 end

    def Function_30_B989(): pass

    label("Function_30_B989")


    def lambda_B98E():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B98E)
    WaitChrThread(0x103, 1)

    def lambda_B9AC():
        OP_95(0xFE, 400, 0, 6600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B9AC)
    WaitChrThread(0x103, 1)

    def lambda_B9CA():
        OP_95(0xFE, 3500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B9CA)
    WaitChrThread(0x103, 1)

    def lambda_B9E8():
        OP_95(0xFE, 8500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B9E8)
    WaitChrThread(0x103, 1)
    Return()

    # Function_30_B989 end

    def Function_31_BA02(): pass

    label("Function_31_BA02")

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
        "罗伊德的声音",
        "#2P──打扰了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    OP_68(64000, 1000, 6900, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_BB83():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_BB83)

    def lambda_BB90():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_BB90)
    SetChrPos(0x101, 59000, 0, 3400, 90)
    BeginChrThread(0x101, 3, 0, 32)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 34)

    #C0344
    ChrTalk(
        0x11,
        "#1005F#5P喔，回来得好晚啊。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x13,
        "#2202F#5P你们好，我来叨扰了。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0346
    ChrTalk(
        0x101,
        "#12P#0002F果然是伊安律师啊。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#0100F#12P律师您会来这里\x01",
            "还真少见呢。\x02",
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
            "嗯，有点事情\x01",
            "想问问赛尔盖。\x02\x03",

            "再加上正好还有其它事情，\x01",
            "所以就特意过来了。\x02",
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
        "#12P#0005F其它事情吗？\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        (
            "#1003F#5P嗯，直说的话，\x01",
            "就是关于琪雅的身世。\x02",
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
        "#12P#0013F难、难不成……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#12P#0301F查到什么了吗！？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x13,
        (
            "#2203F#5P不……很遗憾。\x02\x03",

            "#2201F你们似乎去委托了协会，\x01",
            "而赛尔盖也拜托我\x01",
            "去调查其它的可能性了。\x02\x03",

            "#2203F很遗憾──不，应该说幸好才对吧，\x01",
            "并没有发现那种可能性。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        "#12P#0005F那种可能性是指……？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x11,
        (
            "#1003F#5P嗯……\x01",
            "那是几年前的事情了。\x02\x03",

            "#1000F以卡尔瓦德共和国为中心，\x01",
            "相继发生了一连串的\x01",
            "绑架儿童事件。\x02",
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
        "#12P#0007F绑架儿童……！？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        "#0101F#12P那、那是……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0358
    ChrTalk(
        0x11,
        (
            "#1003F#5P细节方面就略过不提……\x01",
            "总之那次事件的规模相当大。\x02\x03",

            "不仅是卡尔瓦德，\x01",
            "连周边诸国也出现了受害者，\x01",
            "因此，当时还成立了国际性的调查团队。\x02\x03",

            "#1001F这个调查团队，由各国的军队、\x01",
            "警察组织，以及游击士协会组成。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#12P#0001F竟然有这种事……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        "#0106F#12P还是第一次听说……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#12P#0303F……我也是头一次听说呢。\x02\x03",

            "#0301F一直都没有对外声张，\x01",
            "也就是说，事件的性质相当恶劣吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x13,
        (
            "#2203F#5P嗯……\x01",
            "虽然事件最后还是解决了。\x02\x03",

            "但因为性质太过严重，\x01",
            "便还是作为机密事件处理了。\x02\x03",

            "#2201F我作为民间的律师顾问，\x01",
            "偶然同此事扯上了关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#12P#0011F请、请等一下。\x02\x03",

            "#0013F难道说，琪雅\x01",
            "有可能是几年前\x01",
            "那个事件的受害者……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x13,
        (
            "#2201F#5P我们正是有此怀疑，\x01",
            "才重新调查了当时的受害情况……\x02\x03",

            "结果，并没有找到\x01",
            "符合琪雅情况的孩子。\x02\x03",

            "#2203F当年犯案的恶人们\x01",
            "也基本都被逮捕，或者自杀了。\x02\x03",

            "#2200F因为确认了这些，\x01",
            "所以来告诉赛尔盖。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#12P#0006F原来是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#0108F#12P虽然稍微安心了些……\x01",
            "但真没想到，竟然发生过那种事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x11,
        (
            "#1003F#5P……嗯，关于那件事，\x01",
            "以后有机会的话，会和你们说的。\x02\x03",

            "#1001F只是，关于琪雅的问题，\x01",
            "最后又回到起点了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        (
            "#12P#0302F嗯，这也没关系吧？\x02\x03",

            "在找到她的归宿之前，\x01",
            "由我们负责照顾她就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x13,
        (
            "#2202F#5P嗯，暂时让她\x01",
            "待在这里比较好吧。\x02\x03",

            "#2210F只是，如果她真的无依无靠……\x02\x03",

            "#2200F或许应该考虑给她寻找养父母，\x01",
            "或者交给教会的福利设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        "#12P#0011F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        "#0108F#12P……可、可是………\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x11,
        (
            "#1003F#5P再怎么说，这些事情也是\x01",
            "迟早都要考虑的。\x02\x03",

            "#1000F若想将一个小孩子抚养长大，\x01",
            "没有相当的觉悟可是做不来的。\x02\x03",

            "无论那个孩子有多可爱。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        "#12P#0008F话是……没错……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        (
            "#12P#0306F的确，这和养只\x01",
            "小猫完全是两回事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x13,
        (
            "#2202F#5P哈哈，抱歉。\x01",
            "话说得可能有点重了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0376
    ChrTalk(
        0x13,
        (
            "#2205F#5P话说回来，你们似乎\x01",
            "刚刚执行任务归来嘛。\x02\x03",

            "#2202F应该还要报告吧，\x01",
            "那我差不多也该告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        (
            "#12P#0000F不，哪里的话。\x02\x03",

            "其实我们正好有个案子\x01",
            "想跟律师您商量一下呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0378
    ChrTalk(
        0x13,
        "#2205F#5P哦，跟我商量？\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        "#12P#0001F嗯，其实是──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0380
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向赛尔盖和伊安律师\x01",
            "说明了失踪矿工一事。\x07\x00\x02",
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
            "#1004F#5P原来如此……\x01",
            "竟然发生了这种事啊。\x02\x03",

            "#1002F呵呵，很有支援科\x01",
            "风格的工作，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#12P#0006F由于并未涉及犯罪行为，\x01",
            "就没有对其本人进行说服……\x02\x03",

            "#0001F也许还是应该劝他\x01",
            "回镇上更好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x11,
        (
            "#1003F#5P唔，这的确很难讲啊。\x02\x03",

            "如果是游击士的话，说服与交涉\x01",
            "也算是分内之职……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x13,
        (
            "#2203F#5P可是，如果警察这么做的话，\x01",
            "也许就难逃干涉民事的嫌疑了……\x02\x03",

            "#2200F真是很难划清界线啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        "#12P#0006F果然是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#12P#0304F也罢，他毕竟都是个成年人了，\x01",
            "应该也不用我们多管闲事吧。\x02\x03",

            "#0300F如果是小孩子，就该打他的屁股，\x01",
            "然后把他带回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#0102F#11P呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x13,
        (
            "#2201F#5P话说，那天才般的技巧，\x01",
            "还有判若两人的运气与直觉……\x02\x03",

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
            "#6P#1001F……律师，\x01",
            "您有什么头绪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x13,
        (
            "#5P#2203F不，可能只是偶然吧……\x02\x03",

            "#2200F最近我也听说过\x01",
            "两件很相似的事情呢。\x02",
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
        "#12P#0001F真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#12P#0307F难道说，还有其他人\x01",
            "也在『巴鲁卡』狂赚了一笔吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x13,
        (
            "#2202F#5P不不，不是这样的。\x02\x03",

            "#2210F我听说的事情，\x01",
            "是某个证券公司的证券经理，\x01",
            "和一个贸易公司的经营者。\x02\x03",

            "#2200F他们两人最近都蒙受了巨大损失，\x01",
            "本来非常烦恼……\x02\x03",

            "但就在这几天，业绩却突然\x01",
            "奇迹般地好转了。\x02\x03",

            "#2203F特别是证券经理……\x01",
            "简直就像是可以预测未来一样，\x01",
            "完全靠运气和直觉买卖股票。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        "#12P#0005F这个……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x104,
        "#12P#0301F听起来好耳熟啊……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x13,
        (
            "#2202F#5P哈哈，当然了，\x01",
            "这应该只是巧合而已吧。\x02\x03",

            "#2210F只不过，\x01",
            "听说那两人的态度\x01",
            "也开始明显变得蛮横起来。\x02\x03",

            "#2200F令我稍微有些在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x102,
        "#0103F#12P的确令人在意呢……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x11,
        (
            "#6P#1003F唔……伊安律师。\x02\x03",

            "#1000F您知道关于那两人的\x01",
            "详细情况吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x11, 500)

    #C0399
    ChrTalk(
        0x13,
        (
            "#11P#2205F嗯，如果想查的话，\x01",
            "应该可以马上查到……\x02\x03",

            "#2200F保险起见，要确认一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x11,
        "#6P#1002F嗯，可以的话。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#12P#0001F#12P科长……您是不是在担心什么？\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)

    #C0402
    ChrTalk(
        0x11,
        (
            "#1006F#5P嗯，干我们这一行的，\x01",
            "情报是越多越好嘛。\x02\x03",

            "#1002F仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#12P#0000F原来如此……\x02\x03",

            "#0004F（大哥也说过呢……\x01",
            "  调查的关键，就是凭借自身直觉\x01",
            "  以及行动力收集来的情报……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)

    #C0404
    ChrTalk(
        0x13,
        (
            "#2210F#5P好了，那么，我就先告辞了。\x02\x03",

            "#2202F你们如果有什么在意的事情，\x01",
            "随时都可以来找我商量。\x02\x03",

            "我会尽可能帮助你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x101,
        (
            "#12P#0002F伊安律师……\x01",
            "太谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x102,
        (
            "#0104F#12P到时候\x01",
            "还请多多关照。\x02",
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

    # Function_31_BA02 end

    def Function_32_D085(): pass

    label("Function_32_D085")


    def lambda_D08A():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D08A)

    def lambda_D0A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D0A4)
    WaitChrThread(0x101, 1)

    def lambda_D0B9():
        OP_95(0xFE, 63500, 30, 5600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0B9)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_D085 end

    def Function_33_D0DA(): pass

    label("Function_33_D0DA")


    def lambda_D0DF():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D0DF)

    def lambda_D0F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D0F9)
    WaitChrThread(0x102, 1)

    def lambda_D10E():
        OP_95(0xFE, 64099, 30, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D10E)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_D0DA end

    def Function_34_D12F(): pass

    label("Function_34_D12F")


    def lambda_D134():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D134)

    def lambda_D14E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D14E)
    WaitChrThread(0x104, 1)

    def lambda_D163():
        OP_95(0xFE, 62900, 30, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D163)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_D12F end

    def Function_35_D184(): pass

    label("Function_35_D184")

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
            "#1003F#5P──是吗，\x01",
            "结果冒出了这个名字啊。\x02\x03",

            "#1001F『真之睿智（真知）』……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#0003F#6P……科长，请告诉我们吧。\x02\x03",

            "#0001F关于六年前大哥曾经参与调查的，\x01",
            "那个曾绑架过缇欧的教团。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#6P#0101F科长……\x01",
            "您肯定知道的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x104,
        (
            "#6P#0306F总感觉，您从一开始\x01",
            "就很清楚阿缇的隐情嘛。\x02",
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

    def lambda_D5AE():
        OP_95(0xFE, 65600, 0, 6900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D5AE)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0411
    ChrTalk(
        0x11,
        (
            "#1003F#11P──我当然清楚。\x02\x03",

            "#1000F因为我就是当时\x01",
            "和盖伊一起捣毁了\x01",
            "教团据点之一的当事人啊。\x02",
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
            "#0005F#6P是、是这样的吗！？\x02\x03",

            "#0001F这么说，科长是大哥的──\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x11,
        (
            "#1004F#11P#11P直属上司。\x02\x03",

            "#1006F……从那时起，\x01",
            "我就算是个问题分子。\x02\x03",

            "有一天，上头突然给我\x01",
            "塞了两个非同寻常的新人。\x02\x03",

            "#1002F其中之一，就是你大哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#0005F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x11,
        (
            "#1002F#11P虽然性情耿直，又做事冲动……\x01",
            "但他却是个很优秀的搜查官。\x02\x03",

            "#1004F从某种意义上来说，和另一个新人\x01",
            "刚好是一对互补的最佳拍档。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        (
            "#6P#0101F另一个\x01",
            "新人是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x104,
        (
            "#6P#0305F莫非是\x01",
            "那个一科的达德利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x11,
        (
            "#1003F#11P不，他是彻头彻尾的\x01",
            "一科出身之人。\x02\x03",

            "我所接收的\x01",
            "另一个非同寻常的新人……\x02\x03",

            "#1002F──就是那个\x01",
            "亚里欧斯·马克莱因。\x02",
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
        "#0011F#6P哎！？\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        "#6P#0105F那个人，原本是警察吗……！？\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x11,
        (
            "#1003F#11P嗯，不过他几年前辞去了警察的工作，\x01",
            "转行去当游击士了。\x02\x03",

            "#1000F可以说是警察局\x01",
            "和游击士协会保持着\x01",
            "微妙距离感的原因之一吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x104,
        "#6P#0306F居然还有这种事……\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0006F#6P大哥和亚里欧斯先生\x01",
            "竟然是同期入职的新人……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x11,
        (
            "#1002F#11P从年龄上来说，\x01",
            "亚里欧斯要大盖伊两岁。\x02",
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
            "#30W──当时已经结了婚，\x01",
            "而且还刚刚喜得爱女的亚里欧斯，\x01",
            "是个一本正经得有些过头的男人。\x02\x03",

            "#30W另一方面，盖伊则奔放又冲动，\x01",
            "是个无比乐观的愣头傻小子。\x02\x03",

            "#30W但正是这样的两个人，\x01",
            "反而更加意气相投吧。\x02\x03",

            "#30W在短短不到两年的时间内，\x01",
            "他们就已经被称为克洛斯贝尔警界\x01",
            "最强的年轻搭档了。\x02",
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
            "#6P#0106F确、确实，如果是那两人的话，\x01",
            "被称为最强也不足为奇呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x11,
        (
            "#1002F#11P嗯……\x01",
            "说实话，我也感到面上有光呢。\x02\x03",

            "因为获得了培养如此优秀部下的\x01",
            "绝好机会嘛。\x02\x03",

            "#1004F就这样，我们这个团队\x01",
            "步步进发，立下了赫赫战功……\x02\x03",

            "终于代替一科接受委任，\x01",
            "参加了国际性\x01",
            "犯罪事件的联合调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        "#0005F#6P国际性犯罪事件……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x104,
        "#6P#0301F莫非就是……\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x11,
        (
            "#1003F#11P嗯──就是那个『教团』的事件。\x02\x03",
        )
    )
    
    CloseMessageWindow()
    
    AnonymousTalk(    #talk#5000
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "塞尔盖在笔记上写下了文字与符号。\x07\x00\x02",
        )
    )
    
    CloseMessageWindow()
    

    ChrTalk(     #talk#5001
        0x11,
        (
            "#1001F『Ｄ∴Ｇ教团』……\x01",
            "这似乎就是他们的正式名称。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        "#0013F#6P『Ｄ∴Ｇ教团』……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x104,
        "#6P#0301F那个∴是什么啊？\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x102,
        (
            "#6P#0108F∴是表示『所以』的\x01",
            "数学符号……\x02\x03",

            "#0101F所谓的『Ｄ∴Ｇ』，\x01",
            "到底是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x11,
        (
            "#1003F#11P这个至今仍未弄清……\x01",
            "不过，关于其中的『Ｇ』，\x01",
            "总算是有点头绪。\x02\x03",

            "#1001FＧ──亦即\x01",
            "『Ｇｎｏｓｉｓ（真之睿智）』。\x02",
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
        "#0013F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#6P#0101F约亚西姆医生所说的那种\x01",
            "能让人获得恶魔之力的药……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x104,
        "#6P#0307F竟然有这种联系……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)

    #C0439
    ChrTalk(
        0x11,
        (
            "#1001F#11P事件终结之后，过了六年多──\x02\x03",

            "#1003F这个宗教团体留下了众多谜团……\x01",
            "但是，只有一点很明确。\x02\x03",

            "那就是，他们共同犯下的罪行，\x01",
            "在这数十年中是最恶劣的，\x01",
            "可以说没有什么罪犯能比他们更邪恶了。\x02\x03",

            "#1010F……他们从各地绑架孩子们，\x01",
            "并且造成了数十人的牺牲。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#0010F#6P……！\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x102,
        "#6P#0108F昨天，伊安律师也曾提起过……\x02",
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
            "#30W『Ｄ∴Ｇ教团』……\x02\x03",

            "#30W他们在塞姆里亚大陆各地\x01",
            "拥有十处以上的据点。\x02\x03",

            "#30W并且分别在各个据点\x01",
            "不断举行各种各样的『仪式』。\x02\x03",

            "#30W召唤恐怖恶魔的仪式，\x01",
            "利用『古代遗物』的仪式，\x01",
            "以及人体实验性质的仪式……\x02\x03",

            "#30W而在进行这些仪式时，\x01",
            "必然要使用的……\x02\x03",

            "#30W就是那种名为『真知』的\x01",
            "神秘药物。\x02",
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
            "#6P#0106F……这……\x01",
            "真是令人震惊的事实啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x104,
        (
            "#6P#0301F然后呢，事件是怎样\x01",
            "解决的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x11,
        "#1003F#11P嗯……\x02",
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
            "#30W──昨天也提到过，\x01",
            "由于危害性已经波及到了各国，\x01",
            "于是当时便成立了国际性调查小组。\x02\x03",

            "#30W各国的军人、警察以及协会的相关人士\x01",
            "齐聚一堂……\x02\x03",

            "#30W在一位声名显赫的游击士的指挥下，\x01",
            "展开了共同检举、捣毁各地教团据点的\x01",
            "大规模作战。\x02",
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
            "#30W而我们三人，\x01",
            "便负责捣毁位于共和国最西端，\x01",
            "阿尔泰尔市郊外的一个据点……\x02\x03",

            "#30W盖伊救下了当时年仅八岁的\x01",
            "缇欧·普拉托。\x02\x03",

            "#30W虽然缇欧当时相当虚弱，\x01",
            "但或许还算是情况最好的。\x02\x03",

            "#30W……因为，除她之外的所有孩子，\x01",
            "都已经回天乏术了……\x02\x03",

            "#30W而和在其它据点试验的\x01",
            "恐怖『仪式』相比，即使是那些\x01",
            "不幸身亡的孩子，恐怕也都算得上是幸运了。\x07\x00\x02",
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
        "#0006F#6P……为什么………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0450
    ChrTalk(
        0x101,
        (
            "#0010F#6P为什么会有\x01",
            "这种丧尽天良的人存在啊……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        "#6P#0108F……真令人作呕……\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x104,
        (
            "#6P#0303F克洛斯贝尔的犯罪事件与它相比，\x01",
            "根本就不能相提并论啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x11,
        (
            "#1003F#11P是啊……\x02\x03",

            "#1001F──但不管怎么说，\x01",
            "在六年前的那次作战行动中，\x01",
            "『教团』已经被完全摧毁了。\x02\x03",

            "信徒全员不是自杀，\x01",
            "就是精神错乱，最终衰弱致死。\x02\x03",

            "虽然听说还有残党活了下来……\x01",
            "但有传闻说，教会和那个『结社』\x01",
            "都已采取了行动，暗中将其歼灭了。\x02\x03",

            "#1003F『Ｄ∴Ｇ教团』的噩梦\x01",
            "应该已经完全终结了──\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        "#0008F#6P然而……这个『蓝色药片』。\x02",
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
            "#0013F以目前的情况来看，\x01",
            "这很有可能就是那个教团\x01",
            "所使用过的『真知』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0456
    AnonymousTalk(
        0x11,
        (
            "#1003F关于这点，当前尚在臆测的范围之内……\x02\x03",

            "#1001F不过，如果真是如此，\x01",
            "说不定，六年前的那场噩梦\x01",
            "将会以另一种形式重现。\x02\x03",

            "而且，还会将黑手党之间的对抗\x01",
            "也卷入其中。\x02",
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
        "#6P#0306F这真是再糟糕不过了吧……\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#6P#0101F如果这是真的……\x01",
            "我们绝对不能袖手旁观……！\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x11,
        "#1010F#11P嗯……当然了。\x02",
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
            "#1001F#11P──罗伊德。\x02\x03",

            "三年前杀害你大哥的凶手，\x01",
            "至今仍然未能查明。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        (
            "#0003F#6P……是。\x02\x03",

            "#0001F因为线索实在太少，\x01",
            "最终成了悬案呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x11,
        (
            "#1006F#11P嗯……\x01",
            "据说，他转去一科以后，\x01",
            "基本都是单独进行调查。\x02\x03",

            "所以，凶手是大国的谍报机关、鲁巴彻，\x01",
            "还是与这些完全无关的其它犯罪组织……\x02\x03",

            "又或者也有可能是哪里的猎兵团，\x01",
            "或是恐怖分子。\x02\x03",

            "#1001F只不过──除此之外，\x01",
            "还有一种可能性也曾掠过我的脑海。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        "#0008F#6P『教团』的残党吗……\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x11,
        (
            "#1003F#11P嗯……事到如今，\x01",
            "这种可能性也逐渐有了现实的味道。\x02\x03",

            "从这种意义上说，对我而言，\x01",
            "这也将是吊唁前部下的复仇之战吧。\x02\x03",

            "#1002F虽然有些对不住你们，\x01",
            "但接下来，我也要插手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#0005F#6P科长……\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#6P#0102F何、何来对不住一说呢，\x01",
            "您能帮忙真是再好不过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#6P#0302F这话说得，就好像以前\x01",
            "是在故意放任我们不管啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x11,
        (
            "#1004F#11P呵呵，怎么说好呢……\x02\x03",

            "#1002F只不过，这个特别任务支援科，\x01",
            "原本就是参考了盖伊的想法\x01",
            "而设立的。\x02",
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
        "#0005F#6P是、是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        (
            "#6P#0101F不是为了对抗协会，赢得市民好评\x01",
            "而设立的部门吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x11,
        (
            "#1002F#11P那只是让高层们\x01",
            "接受的借口罢了。\x02\x03",

            "#1004F──盖伊那家伙，\x01",
            "在生前曾经对我说过。\x02\x03",

            "如今的克洛斯贝尔，最需要的就是\x01",
            "跨越『壁障』的力量……\x02\x03",

            "年轻人即使遭遇失败也没关系，\x01",
            "只要齐心协力，就能不断向前迈进……\x02\x03",

            "#1002F他说，我们警察是不是\x01",
            "正需要这样一个环境呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        "#0000F#6P大哥他……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x104,
        (
            "#6P#0304F哎呀呀……\x01",
            "还真是个热血的大哥啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0474
    ChrTalk(
        0x102,
        (
            "#6P#0105F莫非，缇欧会来\x01",
            "支援科，也是因为……？\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        "#0005F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x11,
        (
            "#1003F#11P嗯，她是想待在\x01",
            "继承了盖伊意志的地方吧。\x02\x03",

            "虽然她本人\x01",
            "并没有明确说出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        "#0008F#6P是吗……原来是这么回事。\x02",
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
            "#0003F#6P大哥的事暂且不提……\x02\x03",

            "目前，阻止这种药物继续害人\x01",
            "才是第一要务。\x02\x03",

            "#0013F还有，关于琪雅……\x02\x03",

            "说不定，她也和那个『教团』\x01",
            "存在着什么关联。\x02",
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
        "#6P#0101F啊……！\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x104,
        (
            "#6P#0308F嘁，这还真有可能呢。\x02\x03",

            "之前修女说过，阿琪失去记忆的原因\x01",
            "也可能是由于药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x11,
        (
            "#1001F#11P嗯……\x01",
            "我也开始有这种怀疑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        (
            "#0004F#6P所以，科长……\x02\x03",

            "#0000F行动就交给我们，\x01",
            "科长能不能留在这里，\x01",
            "保护好琪雅？\x02\x03",

            "还有，因为要与一科合作，\x01",
            "我们也需要有人担任司令才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0483
    ChrTalk(
        0x11,
        "#1005F#11P哦……？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        "#6P#0105F的、的确……\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x104,
        (
            "#6P#0303F支援科中确实需要\x01",
            "有人驻守呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#0006F#6P……对不起。\x02\x03",

            "难得您提出主动出马，\x01",
            "我却说了这种自以为是的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x11,
        (
            "#1009F#11P呵呵……别在意。\x02\x03",

            "#1004F──好吧，我接受。\x02\x03",

            "#1001F只不过，和以前一样，\x01",
            "我还是不会直接对你们做出指示。\x02\x03",

            "有问题的话，尽管和我商量，\x01",
            "与各方面的联络工作也由我负责……\x02\x03",

            "至于你们，就依靠自己的判断\x01",
            "来解决这次的事件吧。\x02\x03",

            "#1002F怎么样，能行吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        "#0000F#6P是……！\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x102,
        "#6P#0100F明白了！\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        (
            "#6P#0304F哎呀呀，看样子，从明天开始，\x01",
            "就要忙到焦头烂额啦。\x02",
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

    # Function_35_D184 end

    def Function_36_F5CE(): pass

    label("Function_36_F5CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F5EC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_36_F5CE")

    label("loc_F5EC")

    Return()

    # Function_36_F5CE end

    def Function_37_F5ED(): pass

    label("Function_37_F5ED")

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
            "#0607F唔……\x01",
            "到底在想什么！？\x02",
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
            "#11P#0610F约亚西姆·琼塔……\x01",
            "他到底打的是什么算盘！？\x02\x03",

            "为什么要特地留下\x01",
            "对自己不利的情报！？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x11,
        "#1003F#11P嗯，确实……\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    #C0494
    ChrTalk(
        0x11,
        (
            "#1001F#5P──你们几个，\x01",
            "对伪装的可能性有什么看法？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA67():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_FA67)

    #C0495
    ChrTalk(
        0x101,
        (
            "#12P#0006F……说实话，我认为\x01",
            "在这种情况下，伪装毫无意义。\x02\x03",

            "#0013F一切状况都把矛头指向他，\x01",
            "他和鲁巴彻以及议长的关系\x01",
            "也已经曝光了……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#0101F从『银』的行动来看，\x01",
            "黑月和共和国派做了手脚的\x01",
            "可能性也很低……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x104,
        (
            "#0306F嗯，不过就是单纯\x01",
            "在炫耀而已吧？\x02\x03",

            "#0301F还有那个混账秘书的态度也\x01",
            "相当狂妄呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        (
            "#12P#0206F……有同感。\x02\x03",

            "#0208F从那两份文件中，\x01",
            "除了能感觉到他的自我显示欲之外，\x01",
            "似乎还传递出了某种疯狂的信仰。\x02\x03",

            "#0201F那恐怕是关于琪雅的……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x11,
        (
            "#1006F#5P原来如此啊……\x02\x03",

            "#1001F……难道那孩子拥有什么东西，\x01",
            "能让他如此执著吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x10A,
        (
            "#11P#0602F荒、荒唐……\x01",
            "她只不过是个什么都不懂的小孩子吧！？\x02\x03",

            "不惜干出这种勾当，\x01",
            "到底能有什么好处呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x11,
        (
            "#1003F#5P谁知道呢……\x02\x03",

            "#1001F不过，那份白色的文件中\x01",
            "却夹着她的照片，其中的意义……\x02\x03",

            "──罗伊德，你怎么看？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x101,
        (
            "#12P#0003F……嗯。\x02\x03",

            "#0008F六年前进行的\x01",
            "种种残酷『仪式』……\x02\x03",

            "#0001F其最终目的\x01",
            "就是要利用到琪雅，\x01",
            "这或许就是那个信息的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x102,
        "#0101F唔……\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x104,
        "#0310F嘁……\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x103,
        "#12P#0208F……绝不让他得逞……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x101,
        "#12P#0003F嗯……当然了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0507
    ChrTalk(
        0x101,
        (
            "#6P#0013F──达德利警官，\x01",
            "高层那边怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x10A,
        (
            "#0606F#5P……时机很不凑巧，\x01",
            "刚接到那个拘留所遇袭的消息。\x02\x03",

            "而且，拘留所附近的\x01",
            "警察学校和训练场似乎也遭到了袭击。\x02\x03",

            "#0601F为了应对这些状况，\x01",
            "警察局总部现在乱得就像被捅了的蜂窝一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        (
            "#6P#0006F我明白了……\x01",
            "看来是无法指望他们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0510
    ChrTalk(
        0x101,
        (
            "#12P#0001F──拜托游击士协会，\x01",
            "带琪雅逃往国外吧。\x02",
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

    def lambda_1002C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1002C)
    Sleep(50)

    def lambda_1003C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1003C)
    Sleep(50)

    def lambda_1004C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1004C)
    WaitChrThread(0x102, 2)

    #C0511
    ChrTalk(
        0x102,
        "#0105F#11P罗伊德，这……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        (
            "#12P#0003F当然，条件是必须要\x01",
            "交给亚里欧斯先生或者艾丝蒂尔他们。\x02\x03",

            "#0000F利贝尔一带应该很安全，\x01",
            "『教团』也难以下手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x11,
        (
            "#1003F#5P唔……或许这的确是\x01",
            "最安全的办法。\x02\x03",

            "#1000F──不过，这样好吗？\x02\x03",

            "如此一来，你们就无法\x01",
            "亲手保护那孩子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x101,
        (
            "#12P#0006F……我的执著与自尊\x01",
            "并不重要。\x02\x03",

            "#0008F虽然大家说不定会反对……\x02\x03",

            "#0001F但是，只要能让那孩子更加安全一点，\x01",
            "我就愿意赌上那种可能性。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x103,
        "#12P#0205F罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        "#0306F哎呀呀……没办法了吗？\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x10A,
        (
            "#0603F#5P……如果有此打算的话，\x01",
            "那就事不宜迟。\x02\x03",

            "#0600F国际定期船的末班船\x01",
            "时间应该是九点半。\x02\x03",

            "如果动作足够迅速，说不定在今晚之内\x01",
            "就能送那孩子逃往利贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x11,
        (
            "#1003F#5P好，联络协会吧。\x02\x03",

            "#1002F如果亚里欧斯已经回来了，\x01",
            "直接拜托他就可以了。\x02\x03",

            "如果是他的话，无论如何\x01",
            "也都能保护好女儿和琪雅这两个孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x101,
        "#12P#0000F是的……！\x02",
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
    SetChrName("男性的声音")

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "喂喂，这里是游击士协会，\x01",
            "克洛斯贝尔分部哦。\x02",
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
            "#0001F米歇尔先生，\x01",
            "我是支援科的罗伊德。\x02\x03",

            "您现在方便吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哎呀，是小弟你啊。\x02\x03",

            "怎么了？\x01",
            "想找我们的成员吗，\x01",
            "他们都还没回来呢……\x02",
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
            "#0005F这、这样啊……\x02\x03",

            "#0001F您知道亚里欧斯先生\x01",
            "大概会在何时回来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，他啊，应该\x01",
            "快回来了──\x02",
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
    SetChrName("米歇尔的声音")

    #A0525
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S什么……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("米歇尔的声音")

    #A0526
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S你们是什么人！？\x01",
            "这里可是游击士协会——\x02",
        )
    )

    CloseMessageWindow()
    Sound(531, 0, 60, 0)
    Sleep(300)
    SetChrName("米歇尔的声音")

    #A0527
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S……呜……\x02",
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

            "#0007F米歇尔先生！？\x01",
            "您怎么了！？\x02\x03",

            "#0010F（……断掉了，\x01",
            "  通讯器被破坏了吗……！？）\x02",
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
        "#0605F#5P喂，出什么事了……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)

    #C0530
    ChrTalk(
        0x101,
        (
            "#12P#0003F……游击士协会\x01",
            "似乎被什么人袭击了。\x02\x03",

            "#0013F通讯切断之前，\x01",
            "听到了机关枪的声音。\x02",
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
        "#0105F#11P什么……\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        (
            "#0307F难不成，是那些\x01",
            "被操纵的黑手党……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x11,
        (
            "#1001F#5P唔……\x01",
            "可能性似乎很高啊。\x02",
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
            "#12P#0013F不，那个……\x02\x03",

            "如果说是黑手党的袭击，\x01",
            "似乎有些不对劲……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x11,
        "#1005F#5P什么……？\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        "#12P#0008F（对了，感觉不自然的是……）\x02",
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
            "【机关枪的声音】\x01",        # 0
            "【米歇尔的反应】\x01",        # 1
            "【通讯切断的时机】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1098C"),
        (1, "loc_109F8"),
        (2, "loc_10A66"),
        (SWITCH_DEFAULT, "loc_10AC2"),
    )


    label("loc_1098C")

    OP_2C(0x4E, 0x1)

    #C0537
    ChrTalk(
        0x101,
        (
            "#12P#0003F（对了……\x01",
            "  那不是黑手党所使用的\x01",
            "  重型机关枪的声音。）\x02\x03",

            "#0013F（怎么回事……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AC2")

    label("loc_109F8")


    #C0538
    ChrTalk(
        0x101,
        (
            "#12P#0006F（不，在那种情况下，\x01",
            "  米歇尔先生的反应应该算是很正常……）\x02\x03",

            "#0008F（到底是什么呢……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AC2")

    label("loc_10A66")


    #C0539
    ChrTalk(
        0x101,
        (
            "#12P#0006F（不，时机方面\x01",
            "  并没有什么奇怪之处……）\x02\x03",

            "#0008F（到底是什么呢……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AC2")

    label("loc_10AC2")

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
            "#11P#0005F这个声音是……\x01",
            "那边的通讯器？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x102,
        "#0101F#11P赶快接吧！\x02",
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
            "#1105F啊，罗伊德～\x02\x03",

            "通讯器\x01",
            "在响哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_68(13800, 1750, 11000, 3000)
    BeginChrThread(0xD, 3, 0, 49)
    Sleep(500)

    #C0543
    ChrTalk(
        0x101,
        "#0013F#11P嗯，我马上接！\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#0102F#11P对不起哦，小滴，\x01",
            "吵到你了……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x14,
        (
            "#6008F#12P不、不会……\x01",
            "……出什么事了吗？\x02",
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
        "#0013F您好，这里是特别任务支援科！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女孩的声音")

    #A0547
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德警官！？\x02\x03",

            "太、太好了！\x01",
            "顺利接通了……！\x02",
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
            "#0000F这声音是……诺艾尔上士吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是，刚才承蒙关照了！\x02\x03",

            "──其实，我有事情要\x01",
            "通知你们！\x02\x03",

            "我们完全联络不上\x01",
            "贝尔加德门的部队……！\x02",
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
            "#0007F你说什么……！？\x02\x03",

            "#0010F到底发生了什么事！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0551
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不、不清楚，\x01",
            "我们现在也正在确认……\x02\x03",

            "副司令指示我\x01",
            "先通知你们一声！\x02",
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
            "#0013F明白了，感谢你的情报！\x02\x03",

            "#0005F对了──\x01",
            "我们也有事要通知你们！\x02",
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
            "将游击士协会遇袭的事情\x01",
            "简短地告知给了诺艾尔上士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0554
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "市内的协会被……！？\x02\x03",

            "明白了！\x01",
            "我立即转告副司令！\x02\x03",

            "不知道具体发生了什么事！\x01",
            "请各位多加小心……！\x02",
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
            "#0013F嗯，你们也是！\x02",
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
        "#6P#1001F警备队那边出了什么事？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(150)

    #C0557
    ChrTalk(
        0x101,
        (
            "#5P#0006F说是完全联络不上\x01",
            "贝尔加德门的部队……\x02\x03",

            "#0013F目前正在确认状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x10A,
        "#6P#0605F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x102,
        "#0101F#12P究、究竟是怎么回事……\x02",
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

    def lambda_1122B():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1122B)
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

    def lambda_112DD():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_112DD)

    def lambda_112EA():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_112EA)

    def lambda_112F7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_112F7)

    def lambda_11304():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11304)

    def lambda_11311():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_11311)

    def lambda_1131E():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1131E)
    SetChrSubChip(0x14, 0x1)
    SetChrSubChip(0xD, 0x2)
    OP_68(500, 1000, 2500, 2000)
    OP_6F(0x1)

    #C0560
    ChrTalk(
        0x101,
        "#0005F蔡特……！？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x104,
        (
            "#0301F怎么了……\x01",
            "外面有什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xF,
        "#5P#1201F呜噜噜噜噜……嗷呜！\x02",
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
        "#5P#0205F它说『被包围了，小心』！？\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xD,
        (
            "#1101F#11P它好像说，有什么东西\x01",
            "聚集过来了～\x02",
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

    def lambda_1150D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1150D)

    def lambda_1151A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1151A)
    Sleep(50)

    def lambda_1152A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1152A)

    def lambda_11537():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11537)
    Sleep(50)

    def lambda_11547():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_11547)
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
        "#0013F#5P真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x102,
        (
            "#0101F#11P难不成……\x01",
            "是袭击了游击士协会的那些……！？\x02",
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
            "#6P#1010F哼……\x01",
            "看来没错了。\x02\x03",

            "#1001F──全员，准备脱离。\x02\x03",

            "罗伊德和兰迪\x01",
            "带着琪雅和小滴走。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11646():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11646)
    Sleep(50)

    def lambda_11656():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11656)
    Sleep(50)
    TurnDirection(0x10A, 0x11, 500)

    #C0568
    ChrTalk(
        0x101,
        "#5P#0007F是……！\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x104,
        "#0307F#11P是，长官！\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x11,
        (
            "#6P#1003F缇欧负责周围的警戒，\x01",
            "艾莉负责掩护。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x103,
        "#11P#0201F是……！\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        "#0101F#11P明白！\x02",
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
            "#12P#1001F达德利，\x01",
            "你和我负责殿后。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x10A,
        "#5P#0601F明白……！\x02",
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

    def lambda_117B1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_117B1)
    Sleep(50)

    def lambda_117C1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_117C1)
    Sleep(50)

    def lambda_117D1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_117D1)
    Sleep(50)
    WaitChrThread(0x101, 3)

    def lambda_117E5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_117E5)
    OP_6F(0x1)

    #C0575
    ChrTalk(
        0x101,
        (
            "#0000F#5P琪雅，\x01",
            "抓紧我。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xD,
        (
            "#12P#1110F#N嗯！\x01",
            "嘿嘿嘿……\x02",
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
            "#5P#0304F小滴，\x01",
            "容我失礼了。\x02\x03",

            "#0300F跟你老爸相比，\x01",
            "感觉肯定差远了，忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x14,
        (
            "#12P#6002F哪里的话……\x01",
            "麻烦您了。\x02",
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

    def lambda_118FB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_118FB)
    Sleep(50)

    def lambda_1190B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1190B)
    WaitChrThread(0x104, 2)
    Sleep(200)

    #C0579
    ChrTalk(
        0x11,
        (
            "#1001F#5P好……\x01",
            "尽量保持阵型──\x02",
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
        "#0011F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x102,
        "#11P#0107F警、警备队……！？\x02",
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
            "#5P#1007F快走！\x01",
            "从后门撤退！\x02",
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

    # Function_37_F5ED end

    def Function_38_11E3C(): pass

    label("Function_38_11E3C")

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

    # Function_38_11E3C end

    def Function_39_11F6B(): pass

    label("Function_39_11F6B")

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

    # Function_39_11F6B end

    def Function_40_1206D(): pass

    label("Function_40_1206D")

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

    # Function_40_1206D end

    def Function_41_12196(): pass

    label("Function_41_12196")


    def lambda_1219B():
        OP_95(0xFE, 11000, 850, 11400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1219B)
    WaitChrThread(0xFE, 1)

    def lambda_121B9():
        OP_95(0xFE, 9300, 850, 10400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_121B9)
    WaitChrThread(0xFE, 1)

    def lambda_121D7():
        OP_95(0xFE, 1600, 850, 10400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_121D7)
    WaitChrThread(0xFE, 1)

    def lambda_121F5():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_121F5)
    Sleep(500)

    def lambda_12212():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12212)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_12196 end

    def Function_42_12227(): pass

    label("Function_42_12227")


    def lambda_1222C():
        OP_95(0xFE, 9500, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1222C)
    WaitChrThread(0xFE, 1)

    def lambda_1224A():
        OP_95(0xFE, 1600, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1224A)
    WaitChrThread(0xFE, 1)

    def lambda_12268():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12268)
    Sleep(500)

    def lambda_12285():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12285)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_12227 end

    def Function_43_1229A(): pass

    label("Function_43_1229A")


    def lambda_1229F():
        OP_95(0xFE, 13500, 870, 8600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1229F)
    WaitChrThread(0x104, 1)

    def lambda_122BD():
        OP_95(0xFE, 9500, 850, 8600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_122BD)
    WaitChrThread(0x104, 1)

    def lambda_122DB():
        OP_95(0xFE, 1600, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_122DB)
    WaitChrThread(0x104, 1)

    def lambda_122F9():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_122F9)
    Sleep(500)

    def lambda_12316():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12316)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    Return()

    # Function_43_1229A end

    def Function_44_1232B(): pass

    label("Function_44_1232B")

    SetChrChip(0x0, 0x15, 0x1E, 0x12C)
    SetChrChipByIndex(0x15, 0x27)
    SetChrSubChip(0x15, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 15200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_12382():
        OP_9D(0xFE, 0x3B60, 0x352, 0x898, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_12382)

    def lambda_1239F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1239F)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x0)
    Sound(58, 0, 100, 0)
    Sound(31, 0, 100, 0)
    Sleep(300)
    SetChrChip(0x1, 0x15, 0x0, 0x0)
    Return()

    # Function_44_1232B end

    def Function_45_123CF(): pass

    label("Function_45_123CF")

    SetChrChip(0x0, 0x16, 0x1E, 0x12C)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x2)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_12426():
        OP_9D(0xFE, 0x27D8, 0x352, 0x898, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_12426)

    def lambda_12443():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_12443)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x28)
    SetChrSubChip(0x16, 0x0)
    Sound(59, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    SetChrChip(0x1, 0x16, 0x0, 0x0)
    Return()

    # Function_45_123CF end

    def Function_46_12473(): pass

    label("Function_46_12473")

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

    # Function_46_12473 end

    def Function_47_12B47(): pass

    label("Function_47_12B47")


    def lambda_12B4C():
        OP_95(0xFE, 11300, 870, 7900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12B4C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_47_12B47 end

    def Function_48_12B6D(): pass

    label("Function_48_12B6D")

    OP_92(0x104, 0x3778, 0x1EDC, 0x1F4)

    def lambda_12B7F():
        OP_95(0xFE, 14200, 870, 7900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12B7F)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_48_12B6D end

    def Function_49_12BA0(): pass

    label("Function_49_12BA0")

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

    # Function_49_12BA0 end

    def Function_50_12C04(): pass

    label("Function_50_12C04")


    def lambda_12C09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12C09)

    def lambda_12C1A():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12C1A)
    WaitChrThread(0x101, 1)

    def lambda_12C38():
        OP_95(0xFE, 13800, 850, 12000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12C38)
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

    # Function_50_12C04 end

    def Function_51_12C75(): pass

    label("Function_51_12C75")


    def lambda_12C7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12C7A)

    def lambda_12C8B():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12C8B)
    WaitChrThread(0x102, 1)

    def lambda_12CA9():
        OP_95(0xFE, 14500, 850, 10300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12CA9)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_51_12C75 end

    def Function_52_12CCA(): pass

    label("Function_52_12CCA")


    def lambda_12CCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12CCF)

    def lambda_12CE0():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12CE0)
    WaitChrThread(0x103, 1)

    def lambda_12CFE():
        OP_95(0xFE, 13300, 850, 9800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12CFE)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_52_12CCA end

    def Function_53_12D1F(): pass

    label("Function_53_12D1F")


    def lambda_12D24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12D24)

    def lambda_12D35():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12D35)
    WaitChrThread(0x104, 1)

    def lambda_12D53():
        OP_95(0xFE, 15300, 850, 9800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12D53)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    Return()

    # Function_53_12D1F end

    def Function_54_12D74(): pass

    label("Function_54_12D74")


    def lambda_12D79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12D79)

    def lambda_12D8A():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_12D8A)
    WaitChrThread(0x10A, 1)

    def lambda_12DA8():
        OP_95(0xFE, 15500, 850, 7000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_12DA8)
    WaitChrThread(0x10A, 1)

    def lambda_12DC6():
        OP_95(0xFE, 11000, 850, 10300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_12DC6)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x2D, 0x1F4)
    Return()

    # Function_54_12D74 end

    def Function_55_12DE7(): pass

    label("Function_55_12DE7")


    def lambda_12DEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12DEC)

    def lambda_12DFD():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12DFD)
    WaitChrThread(0x11, 1)

    def lambda_12E1B():
        OP_95(0xFE, 15500, 850, 7000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12E1B)
    WaitChrThread(0x11, 1)

    def lambda_12E39():
        OP_95(0xFE, 11400, 850, 9300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12E39)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x2D, 0x1F4)
    Return()

    # Function_55_12DE7 end

    def Function_56_12E5A(): pass

    label("Function_56_12E5A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12EC8")

    #C0585
    ChrTalk(
        0x101,
        (
            "#0001F这里就是出口，\x01",
            "外面的清风凉爽怡人……\x02\x03",

            "#0006F……但现在还是先去\x01",
            "听听大家怎么说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F1D")

    #C0586
    ChrTalk(
        0x101,
        (
            "#0008F艾莉，出去了吗……？\x02\x03",

            "#0001F不，还是先在\x01",
            "支援科里面找找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F5E")

    #C0587
    ChrTalk(
        0x101,
        (
            "#0000F伊安律师好像来了，\x01",
            "还是先去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F5E")

    Sleep(50)
    SetChrPos(0x0, 1000, 0, 970, 0)
    EventEnd(0x4)
    Return()

    # Function_56_12E5A end

    def Function_57_12F75(): pass

    label("Function_57_12F75")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FC0")

    #C0588
    ChrTalk(
        0x101,
        (
            "#0005F这边是后门……？\x02\x03",

            "#0000F嗯，现在没必要\x01",
            "出去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13015")

    #C0589
    ChrTalk(
        0x101,
        (
            "#0008F艾莉，出去了吗……？\x02\x03",

            "#0001F不，还是先在\x01",
            "支援科里面找找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13015")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_57_12F75 end

    def Function_58_1302C(): pass

    label("Function_58_1302C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13093")

    #C0590
    ChrTalk(
        0x101,
        (
            "#0000F……不行了。\x01",
            "好像开始钻牛角尖了……\x02\x03",

            "还是去外面吹吹风吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_130DC")

    label("loc_13093")


    #C0591
    ChrTalk(
        0x101,
        (
            "#0000F……这边是二楼吧。\x01",
            "回房间也无济于事……\x02\x03",

            "还是去外面吹吹风吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1311D")

    #C0592
    ChrTalk(
        0x101,
        (
            "#0000F伊安律师好像来了，\x01",
            "还是先去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1311D")

    Sleep(50)
    SetChrPos(0x0, 1000, 850, 9460, 180)
    EventEnd(0x4)
    Return()

    # Function_58_1302C end

    def Function_59_13134(): pass

    label("Function_59_13134")

    EventBegin(0x0)
    Fade(1000)
    OP_68(170700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 170000, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131D7")

    #C0593
    ChrTalk(
        0x101,
        (
            "#12P#0005F这里……\x01",
            "应该是缇欧的房间。\x02\x03",

            "#0003F这么晚了，应该已经睡了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_131D7")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【敲门】\x01",        # 0
            "【不敲门】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13225"),
        (1, "loc_132D6"),
        (SWITCH_DEFAULT, "loc_132DD"),
    )


    label("loc_13225")

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
            "#0005F#12P没反应……\x01",
            "话说，好像连一点声息都没有啊。\x02\x03",

            "#0001F难道不在房间里吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x13, 0x1)
    SetMapObjFlags(0x6, 0x10)
    SetChrPos(0x0, 170000, 0, 62900, 0)
    SetScenarioFlags(0x4A, 6)
    EventEnd(0x5)
    Jump("loc_132DD")

    label("loc_132D6")

    EventEnd(0x5)
    Jump("loc_132DD")

    label("loc_132DD")

    Return()

    # Function_59_13134 end

    def Function_60_132DE(): pass

    label("Function_60_132DE")

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

    def lambda_13357():
        OP_96(0xFE, 0x324CE, 0x1E, 0x1D934, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13357)

    def lambda_13371():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13371)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    #C0595
    ChrTalk(
        0x101,
        (
            "#0001F#12P（……缇欧果然\x01",
            "  不在房间里啊。）\x02\x03",

            "（行李好像倒是\x01",
            "  都整理好了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 1)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_60_132DE end

    def Function_61_133E2(): pass

    label("Function_61_133E2")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1341E")
    SetChrName("")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是空房间，\x01",
            "平时上着锁。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1347A")

    label("loc_1341E")

    SetChrName("")

    #A0597
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0598
    ChrTalk(
        0x101,
        (
            "#0001F（这里好像是空房间啊……\x01",
            "  也没什么事，还是不要进去了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1347A")

    TalkEnd(0xFF)
    Return()

    # Function_61_133E2 end

    def Function_62_1347E(): pass

    label("Function_62_1347E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134D6")
    SetChrFlags(0x0, 0x8)

    label("loc_134D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134E9")
    SetChrFlags(0x1, 0x8)

    label("loc_134E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134FC")
    SetChrFlags(0x2, 0x8)

    label("loc_134FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1350F")
    SetChrFlags(0x3, 0x8)

    label("loc_1350F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13522")
    SetChrFlags(0x4, 0x8)

    label("loc_13522")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13535")
    SetChrFlags(0x5, 0x8)

    label("loc_13535")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    #C0599
    ChrTalk(
        0x101,
        "#0000F放在这里就行了吧。\x02",
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
            "罗伊德的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x50, 6)
    OP_66(0x7, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_135C9")
    ClearChrFlags(0x0, 0x8)

    label("loc_135C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_135DC")
    ClearChrFlags(0x1, 0x8)

    label("loc_135DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_135EF")
    ClearChrFlags(0x2, 0x8)

    label("loc_135EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13602")
    ClearChrFlags(0x3, 0x8)

    label("loc_13602")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13615")
    ClearChrFlags(0x4, 0x8)

    label("loc_13615")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13628")
    ClearChrFlags(0x5, 0x8)

    label("loc_13628")

    Call(0, 79)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_62_1347E end

    def Function_63_1363F(): pass

    label("Function_63_1363F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13697")
    SetChrFlags(0x0, 0x8)

    label("loc_13697")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136AA")
    SetChrFlags(0x1, 0x8)

    label("loc_136AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136BD")
    SetChrFlags(0x2, 0x8)

    label("loc_136BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136D0")
    SetChrFlags(0x3, 0x8)

    label("loc_136D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136E3")
    SetChrFlags(0x4, 0x8)

    label("loc_136E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136F6")
    SetChrFlags(0x5, 0x8)

    label("loc_136F6")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0601
    ChrTalk(
        0x101,
        "#0000F放在这里就行了吧。\x02",
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
            "罗伊德的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x50, 7)
    OP_66(0x8, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1378A")
    ClearChrFlags(0x0, 0x8)

    label("loc_1378A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1379D")
    ClearChrFlags(0x1, 0x8)

    label("loc_1379D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137B0")
    ClearChrFlags(0x2, 0x8)

    label("loc_137B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137C3")
    ClearChrFlags(0x3, 0x8)

    label("loc_137C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137D6")
    ClearChrFlags(0x4, 0x8)

    label("loc_137D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137E9")
    ClearChrFlags(0x5, 0x8)

    label("loc_137E9")

    Call(0, 79)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_63_1363F end

    def Function_64_13800(): pass

    label("Function_64_13800")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13858")
    SetChrFlags(0x0, 0x8)

    label("loc_13858")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1386B")
    SetChrFlags(0x1, 0x8)

    label("loc_1386B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1387E")
    SetChrFlags(0x2, 0x8)

    label("loc_1387E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13891")
    SetChrFlags(0x3, 0x8)

    label("loc_13891")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138A4")
    SetChrFlags(0x4, 0x8)

    label("loc_138A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138B7")
    SetChrFlags(0x5, 0x8)

    label("loc_138B7")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    #C0603
    ChrTalk(
        0x102,
        "#0100F放在这里就好了吧。\x02",
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
            "艾莉的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x51, 0)
    OP_66(0x9, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13949")
    ClearChrFlags(0x0, 0x8)

    label("loc_13949")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1395C")
    ClearChrFlags(0x1, 0x8)

    label("loc_1395C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1396F")
    ClearChrFlags(0x2, 0x8)

    label("loc_1396F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13982")
    ClearChrFlags(0x3, 0x8)

    label("loc_13982")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13995")
    ClearChrFlags(0x4, 0x8)

    label("loc_13995")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_139A8")
    ClearChrFlags(0x5, 0x8)

    label("loc_139A8")

    Call(0, 79)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_64_13800 end

    def Function_65_139BF(): pass

    label("Function_65_139BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A22")
    SetChrFlags(0x0, 0x8)

    label("loc_13A22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A35")
    SetChrFlags(0x1, 0x8)

    label("loc_13A35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A48")
    SetChrFlags(0x2, 0x8)

    label("loc_13A48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A5B")
    SetChrFlags(0x3, 0x8)

    label("loc_13A5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A6E")
    SetChrFlags(0x4, 0x8)

    label("loc_13A6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A81")
    SetChrFlags(0x5, 0x8)

    label("loc_13A81")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0605
    ChrTalk(
        0x102,
        "#0100F放在这里就好了吧。\x02",
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
            "艾莉的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x51, 1)
    OP_66(0xA, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B13")
    ClearChrFlags(0x0, 0x8)

    label("loc_13B13")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B26")
    ClearChrFlags(0x1, 0x8)

    label("loc_13B26")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B39")
    ClearChrFlags(0x2, 0x8)

    label("loc_13B39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B4C")
    ClearChrFlags(0x3, 0x8)

    label("loc_13B4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B5F")
    ClearChrFlags(0x4, 0x8)

    label("loc_13B5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B72")
    ClearChrFlags(0x5, 0x8)

    label("loc_13B72")

    Call(0, 79)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_65_139BF end

    def Function_66_13B89(): pass

    label("Function_66_13B89")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BE1")
    SetChrFlags(0x0, 0x8)

    label("loc_13BE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BF4")
    SetChrFlags(0x1, 0x8)

    label("loc_13BF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C07")
    SetChrFlags(0x2, 0x8)

    label("loc_13C07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C1A")
    SetChrFlags(0x3, 0x8)

    label("loc_13C1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C2D")
    SetChrFlags(0x4, 0x8)

    label("loc_13C2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C40")
    SetChrFlags(0x5, 0x8)

    label("loc_13C40")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0607
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
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
            "缇欧的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x51, 2)
    OP_66(0xB, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CCE")
    ClearChrFlags(0x0, 0x8)

    label("loc_13CCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CE1")
    ClearChrFlags(0x1, 0x8)

    label("loc_13CE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CF4")
    ClearChrFlags(0x2, 0x8)

    label("loc_13CF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D07")
    ClearChrFlags(0x3, 0x8)

    label("loc_13D07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D1A")
    ClearChrFlags(0x4, 0x8)

    label("loc_13D1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D2D")
    ClearChrFlags(0x5, 0x8)

    label("loc_13D2D")

    Call(0, 79)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_66_13B89 end

    def Function_67_13D44(): pass

    label("Function_67_13D44")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D9C")
    SetChrFlags(0x0, 0x8)

    label("loc_13D9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DAF")
    SetChrFlags(0x1, 0x8)

    label("loc_13DAF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DC2")
    SetChrFlags(0x2, 0x8)

    label("loc_13DC2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DD5")
    SetChrFlags(0x3, 0x8)

    label("loc_13DD5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DE8")
    SetChrFlags(0x4, 0x8)

    label("loc_13DE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DFB")
    SetChrFlags(0x5, 0x8)

    label("loc_13DFB")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    #C0609
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
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
            "缇欧的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x51, 3)
    OP_66(0xC, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E89")
    ClearChrFlags(0x0, 0x8)

    label("loc_13E89")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E9C")
    ClearChrFlags(0x1, 0x8)

    label("loc_13E9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EAF")
    ClearChrFlags(0x2, 0x8)

    label("loc_13EAF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EC2")
    ClearChrFlags(0x3, 0x8)

    label("loc_13EC2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13ED5")
    ClearChrFlags(0x4, 0x8)

    label("loc_13ED5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EE8")
    ClearChrFlags(0x5, 0x8)

    label("loc_13EE8")

    Call(0, 79)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_67_13D44 end

    def Function_68_13EFF(): pass

    label("Function_68_13EFF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F57")
    SetChrFlags(0x0, 0x8)

    label("loc_13F57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F6A")
    SetChrFlags(0x1, 0x8)

    label("loc_13F6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F7D")
    SetChrFlags(0x2, 0x8)

    label("loc_13F7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F90")
    SetChrFlags(0x3, 0x8)

    label("loc_13F90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FA3")
    SetChrFlags(0x4, 0x8)

    label("loc_13FA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FB6")
    SetChrFlags(0x5, 0x8)

    label("loc_13FB6")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0611
    ChrTalk(
        0x104,
        "#0300F就放这里好啦。\x02",
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
            "兰迪的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x51, 4)
    OP_66(0xD, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14044")
    ClearChrFlags(0x0, 0x8)

    label("loc_14044")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14057")
    ClearChrFlags(0x1, 0x8)

    label("loc_14057")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1406A")
    ClearChrFlags(0x2, 0x8)

    label("loc_1406A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1407D")
    ClearChrFlags(0x3, 0x8)

    label("loc_1407D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14090")
    ClearChrFlags(0x4, 0x8)

    label("loc_14090")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140A3")
    ClearChrFlags(0x5, 0x8)

    label("loc_140A3")

    Call(0, 79)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_68_13EFF end

    def Function_69_140BA(): pass

    label("Function_69_140BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1411D")
    SetChrFlags(0x0, 0x8)

    label("loc_1411D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14130")
    SetChrFlags(0x1, 0x8)

    label("loc_14130")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14143")
    SetChrFlags(0x2, 0x8)

    label("loc_14143")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14156")
    SetChrFlags(0x3, 0x8)

    label("loc_14156")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14169")
    SetChrFlags(0x4, 0x8)

    label("loc_14169")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1417C")
    SetChrFlags(0x5, 0x8)

    label("loc_1417C")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    #C0613
    ChrTalk(
        0x104,
        "#0300F就放这里好啦。\x02",
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
            "兰迪的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x51, 5)
    OP_66(0xE, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1420A")
    ClearChrFlags(0x0, 0x8)

    label("loc_1420A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1421D")
    ClearChrFlags(0x1, 0x8)

    label("loc_1421D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14230")
    ClearChrFlags(0x2, 0x8)

    label("loc_14230")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14243")
    ClearChrFlags(0x3, 0x8)

    label("loc_14243")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14256")
    ClearChrFlags(0x4, 0x8)

    label("loc_14256")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14269")
    ClearChrFlags(0x5, 0x8)

    label("loc_14269")

    Call(0, 79)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_69_140BA end

    def Function_70_14280(): pass

    label("Function_70_14280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142D2")
    SetChrName("")

    #A0615
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "获得了家具类道具之后，\x01",
            "可以将其放置于主人公们的房间里。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x51, 6)

    label("loc_142D2")

    Return()

    # Function_70_14280 end

    def Function_71_142D3(): pass

    label("Function_71_142D3")

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
            "这里放着导力车模型。\x02",
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

    # Function_71_142D3 end

    def Function_72_14378(): pass

    label("Function_72_14378")

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
            "这里放着导力音响。\x02",
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
        (0, "loc_1443B"),
        (1, "loc_14444"),
        (2, "loc_1444D"),
        (3, "loc_14456"),
        (4, "loc_1445F"),
        (5, "loc_14468"),
        (6, "loc_14471"),
        (7, "loc_1447A"),
        (SWITCH_DEFAULT, "loc_14483"),
    )


    label("loc_1443B")

    PlayBGM("ed7400", 0)
    Jump("loc_14483")

    label("loc_14444")

    PlayBGM("ed7401", 0)
    Jump("loc_14483")

    label("loc_1444D")

    PlayBGM("ed7402", 0)
    Jump("loc_14483")

    label("loc_14456")

    PlayBGM("ed7204", 0)
    Jump("loc_14483")

    label("loc_1445F")

    PlayBGM("ed7205", 0)
    Jump("loc_14483")

    label("loc_14468")

    PlayBGM("ed7201", 0)
    Jump("loc_14483")

    label("loc_14471")

    PlayBGM("ed7200", 0)
    Jump("loc_14483")

    label("loc_1447A")

    PlayBGM("ed7202", 0)
    Jump("loc_14483")

    label("loc_14483")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_72_14378 end

    def Function_73_144B2(): pass

    label("Function_73_144B2")

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
            "这里挂着壁挂钟。\x02",
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

    # Function_73_144B2 end

    def Function_74_14553(): pass

    label("Function_74_14553")

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
            "这里放着典雅花瓶。\x02",
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

    # Function_74_14553 end

    def Function_75_145F6(): pass

    label("Function_75_145F6")

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
            "这里挂着壁挂咪西。\x02",
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

    # Function_75_145F6 end

    def Function_76_14699(): pass

    label("Function_76_14699")

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
            "这里放着坐姿咪西。\x02",
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

    # Function_76_14699 end

    def Function_77_1473C(): pass

    label("Function_77_1473C")

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
            "这里装饰着伊莉娅的海报。\x02",
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

    # Function_77_1473C end

    def Function_78_147E5(): pass

    label("Function_78_147E5")

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
            "这里挂着飞镖套装。\x02",
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

    # Function_78_147E5 end

    def Function_79_14888(): pass

    label("Function_79_14888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148C0")
    OP_DE(0x16, 0x0)

    label("loc_148C0")

    Return()

    # Function_79_14888 end

    def Function_80_148C1(): pass

    label("Function_80_148C1")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14942")
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

    label("loc_14942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1495E")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1495E")

    Return()

    # Function_80_148C1 end

    def Function_81_14960(): pass

    label("Function_81_14960")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149E1")
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

    label("loc_149E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149FD")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_149FD")

    Return()

    # Function_81_14960 end

    def Function_82_149FF(): pass

    label("Function_82_149FF")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A80")
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

    label("loc_14A80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A9C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_14A9C")

    Return()

    # Function_82_149FF end

    def Function_83_14A9E(): pass

    label("Function_83_14A9E")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B1F")
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

    label("loc_14B1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B3B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_14B3B")

    Return()

    # Function_83_14A9E end

    SaveToFile()

Try(main)
