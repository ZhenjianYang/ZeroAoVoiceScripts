from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0110.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("c0110", "c0110_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1000, 0, 2000, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0110",                  # 0
        "赛尔盖科长",             # 1
        "赛尔盖科长",             # 2
        "琪雅",                   # 3
        "琪雅",                   # 4
        "蔡特",                   # 5
        "蔡特",                   # 6
        "蔡特",                   # 7
        "滴",                     # 8
        "艾莉",                   # 9
        "缇欧",                   # 10
        "兰迪",                   # 11
        "索妮亚副司令",           # 12
        "诺艾尔上士",             # 13
        "莉夏",                   # 14
        "达德利搜查官",           # 15
        "白板",                   # 16
        "魔兽调查报告",           # 17
        "餐具",                   # 18
        "餐具",                   # 19
        "餐具",                   # 20
        "餐具",                   # 21
        "餐具",                   # 22
        "餐具",                   # 23
        "餐具",                   # 24
        "餐具",                   # 25
        "餐具",                   # 26
        "餐具",                   # 27
        "餐具",                   # 28
        "餐具",                   # 29
        "餐具",                   # 30
        "餐具",                   # 31
        "餐具",                   # 32
        "书籍",                   # 33
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch08200.itc",                   # 01
        "chr/ch02700.itc",                   # 02
        "chr/ch08700.itc",                   # 03
        "chr/ch02502.itc",                   # 04
        "chr/ch02707.itc",                   # 05
        "chr/ch02708.itc",                   # 06
        "chr/ch08202.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch02702.itc",                   # 09
        "chr/ch00100.itc",                   # 0A
        "chr/ch00202.itc",                   # 0B
        "chr/ch00302.itc",                   # 0C
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

    DeclNpc(14699,   850,     11199,   180,  389,  0x0, 0,   0,   0,   0,   0,   1,   2,   255,  0)
    DeclNpc(64000,   200,     11399,   180,  469,  0x0, 0,   4,   0,   255, 255, 1,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   1,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   7,   0,   255, 255, 1,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   2,   0,   255, 255, 1,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    404,  0x0, 0,   5,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   6,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   3,   0,   0,   0,   1,   9,   255,  0)
    DeclNpc(155759,  29,      129339,  0,    389,  0x0, 0,   10,  0,   0,   0,   1,   10,  255,  0)
    DeclNpc(203660,  150,     128610,  0,    469,  0x0, 0,   11,  0,   255, 255, 1,   11,  255,  0)
    DeclNpc(51840,   150,     126410,  270,  469,  0x0, 0,   12,  0,   255, 255, 1,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclEvent(0x0000, 0, 17,  10.0,                  10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -5.0,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 51,  7.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -3.5,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 52,  11.0,                  13.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.5,                  -6.75,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 53,  19.0,                  4.0,                   0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  -2.0,                  -0.0,                  1.0])

    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  3,  0x0000)
    DeclActor(18240,   850,     7560,    1000,    18240,   1850,    7560,    0x007C, 1,  0,  0x0000)
    DeclActor(12500,   850,     5600,    2500,    12500,   1500,    5600,    0x007C, 0,  4,  0x0000)
    DeclActor(64000,   30,      9800,    1500,    64000,   1500,    11400,   0x007E, 1,  1,  0x0000)
    DeclActor(180910,  0,       62020,   1500,    180910,  1500,    62020,   0x007C, 0,  56, 0x0000)
    DeclActor(19980,   0,       63920,   1500,    19980,   1500,    63920,   0x007C, 0,  56, 0x0000)
    DeclActor(175940,  0,       63930,   1500,    175940,  1500,    63930,   0x007C, 0,  56, 0x0000)
    DeclActor(-3150,   0,       122280,  1200,    -3150,   1000,    122280,  0x007C, 1,  31, 0x0000)
    DeclActor(-2300,   0,       129960,  1200,    -2300,   2000,    129960,  0x007C, 1,  32, 0x0000)
    DeclActor(155150,  30,      129699,  1200,    153340,  2029,    130490,  0x007C, 1,  33, 0x0000)
    DeclActor(155120,  30,      123880,  1200,    155120,  2029,    123880,  0x007C, 1,  34, 0x0000)
    DeclActor(208570,  0,       128030,  1200,    208840,  3000,    130410,  0x007C, 1,  35, 0x0000)
    DeclActor(208680,  0,       126170,  1200,    209210,  2000,    127040,  0x007C, 1,  36, 0x0000)
    DeclActor(51920,   0,       130570,  1200,    51920,   2500,    130570,  0x007C, 1,  37, 0x0000)
    DeclActor(52900,   0,       124470,  1200,    53700,   2000,    125270,  0x007C, 1,  38, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  57, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  58, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  59, 0x0000)
    DeclActor(48000,   30,      127860,  1200,    47560,   1500,    128630,  0x007C, 0,  60, 0x0000)
    DeclActor(257190,  0,       67990,   1200,    257350,  1500,    68870,   0x007E, 1,  9,  0x0000)

    ScpFunction((
        "Function_0_9EC",          # 00, 0
        "Function_1_AA4",          # 01, 1
        "Function_2_1311",         # 02, 2
        "Function_3_1824",         # 03, 3
        "Function_4_2048",         # 04, 4
        "Function_5_21D8",         # 05, 5
        "Function_6_2D03",         # 06, 6
        "Function_7_3B2B",         # 07, 7
        "Function_8_3B6B",         # 08, 8
        "Function_9_3BA8",         # 09, 9
        "Function_10_47A9",        # 0A, 10
        "Function_11_4883",        # 0B, 11
        "Function_12_570E",        # 0C, 12
        "Function_13_5766",        # 0D, 13
        "Function_14_57BE",        # 0E, 14
        "Function_15_5816",        # 0F, 15
        "Function_16_586E",        # 10, 16
        "Function_17_5921",        # 11, 17
        "Function_18_5D00",        # 12, 18
        "Function_19_789C",        # 13, 19
        "Function_20_7E43",        # 14, 20
        "Function_21_8BC0",        # 15, 21
        "Function_22_BB98",        # 16, 22
        "Function_23_BC36",        # 17, 23
        "Function_24_BC8B",        # 18, 24
        "Function_25_BCE0",        # 19, 25
        "Function_26_BD35",        # 1A, 26
        "Function_27_BD8A",        # 1B, 27
        "Function_28_CE30",        # 1C, 28
        "Function_29_CEA4",        # 1D, 29
        "Function_30_E4E6",        # 1E, 30
        "Function_31_EB1E",        # 1F, 31
        "Function_32_F12D",        # 20, 32
        "Function_33_10505",       # 21, 33
        "Function_34_10E5A",       # 22, 34
        "Function_35_13357",       # 23, 35
        "Function_36_13380",       # 24, 36
        "Function_37_133C4",       # 25, 37
        "Function_38_13E21",       # 26, 38
        "Function_39_16A5F",       # 27, 39
        "Function_40_16B0A",       # 28, 40
        "Function_41_16B29",       # 29, 41
        "Function_42_1703F",       # 2A, 42
        "Function_43_17590",       # 2B, 43
        "Function_44_17AE3",       # 2C, 44
        "Function_45_1BAAB",       # 2D, 45
        "Function_46_1BB3E",       # 2E, 46
        "Function_47_1CD94",       # 2F, 47
        "Function_48_202D0",       # 30, 48
        "Function_49_208B1",       # 31, 49
        "Function_50_21B9F",       # 32, 50
        "Function_51_2250A",       # 33, 51
        "Function_52_22638",       # 34, 52
        "Function_53_226DA",       # 35, 53
        "Function_54_2277A",       # 36, 54
        "Function_55_22801",       # 37, 55
        "Function_56_22CF3",       # 38, 56
        "Function_57_22E4F",       # 39, 57
        "Function_58_22EEE",       # 3A, 58
        "Function_59_22F8D",       # 3B, 59
        "Function_60_2302C",       # 3C, 60
    ))


    def Function_0_9EC(): pass

    label("Function_0_9EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A2C"),
        (1, "loc_A38"),
        (2, "loc_A44"),
        (3, "loc_A50"),
        (4, "loc_A5C"),
        (5, "loc_A68"),
        (6, "loc_A74"),
        (SWITCH_DEFAULT, "loc_A80"),
    )


    label("loc_A2C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A38")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A44")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A50")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A5C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A68")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A74")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_AA3")

    Return()

    # Function_0_9EC end

    def Function_1_AA4(): pass

    label("Function_1_AA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6F")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6F")
    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B42")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_B61")

    label("loc_B42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B61")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_B61")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B6F")

    label("loc_B6F")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D09")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('竞赛旗', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB2")
    Event(1, 22)

    label("loc_BB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小径自行车', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE3")
    Event(1, 23)

    label("loc_BE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('安乐椅', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C14")
    Event(1, 24)

    label("loc_C14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你水族馆', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C45")
    Event(1, 25)

    label("loc_C45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('古怪靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C76")
    Event(1, 26)

    label("loc_C76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('波波靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA7")
    Event(1, 27)

    label("loc_CA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑泰迪熊', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD8")
    Event(1, 28)

    label("loc_CD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦番茄人玩偶', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D09")
    Event(1, 29)

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D5E")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 256490, 30, 69370, 180)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 257350, 0, 68870, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 255850, 0, 67920, 225)
    Jump("loc_114B")

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_D9D")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5570, 150, 6230, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3470, 30, 6380, 180)
    Jump("loc_114B")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DDC")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 257620, 350, 68650, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 256820, 30, 69850, 180)
    Jump("loc_114B")

    label("loc_DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_E1B")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5570, 150, 6230, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2880, 0, 1750, 225)
    Jump("loc_114B")

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_E5F")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 117660, 30, 8100, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2970, 0, 4170, 225)
    Jump("loc_114B")

    label("loc_E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_EAF")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 124620, 30, 5490, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 117660, 30, 8100, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2970, 0, 4170, 225)
    Jump("loc_114B")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_EBD")
    Jump("loc_114B")

    label("loc_EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_ECB")
    Jump("loc_114B")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_F37")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 14350, 850, 12060, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F07")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_F32")

    label("loc_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F1F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_F32")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F32")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_F32")

    Jump("loc_114B")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_FDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F67")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_FDA")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_F8B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_FDA")

    label("loc_F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_F9D")
    Jump("loc_FDA")

    label("loc_F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_FC4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_FDA")

    label("loc_FC4")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)

    label("loc_FDA")

    Jump("loc_114B")

    label("loc_FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1071")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1014")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_106C")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1038")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_106C")

    label("loc_1038")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_104A")
    Jump("loc_106C")

    label("loc_104A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_106C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)

    label("loc_106C")

    Jump("loc_114B")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_107F")
    Jump("loc_114B")

    label("loc_107F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_108D")
    Jump("loc_114B")

    label("loc_108D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10B1")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 97720, 0, 72570, 0)
    Jump("loc_114B")

    label("loc_10B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_10C4")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_10D2")
    Jump("loc_114B")

    label("loc_10D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_10E5")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_10E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_10F3")
    Jump("loc_114B")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1106")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_1119")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_1119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_112C")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_112C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_114B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14700, 870, 11200, 180)

    label("loc_114B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1165")
    Event(0, 11)

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118E")
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_119F")

    label("loc_118E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119F")
    Event(0, 31)

    label("loc_119F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_11B3")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)
    Jump("loc_12F1")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_11C7")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 6)
    Jump("loc_12F1")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_11DB")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 19)
    Jump("loc_12F1")

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_11F2")
    ClearScenarioFlags(0x5C, 3)
    SetScenarioFlags(0x1, 6)
    Event(0, 20)
    Jump("loc_12F1")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_1206")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 21)
    Jump("loc_12F1")

    label("loc_1206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_121A")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 27)
    Jump("loc_12F1")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_122E")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 29)
    Jump("loc_12F1")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_123F")
    ClearScenarioFlags(0x5C, 7)
    Jump("loc_12F1")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_1253")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 33)
    Jump("loc_12F1")

    label("loc_1253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_1267")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 34)
    Jump("loc_12F1")

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_127E")
    ClearScenarioFlags(0x5D, 2)
    SetScenarioFlags(0x1, 6)
    Event(0, 37)
    Jump("loc_12F1")

    label("loc_127E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_1292")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 38)
    Jump("loc_12F1")

    label("loc_1292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_12A6")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 44)
    Jump("loc_12F1")

    label("loc_12A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_12BA")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 46)
    Jump("loc_12F1")

    label("loc_12BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_12CE")
    ClearScenarioFlags(0x5D, 6)
    Event(0, 49)
    Jump("loc_12F1")

    label("loc_12CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_12E2")
    ClearScenarioFlags(0x5D, 7)
    Event(0, 50)
    Jump("loc_12F1")

    label("loc_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 1)), scpexpr(EXPR_END)), "loc_12F1")
    ClearScenarioFlags(0x5E, 1)
    Event(1, 18)

    label("loc_12F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1310")
    Event(1, 14)

    label("loc_1310")

    Return()

    # Function_1_AA4 end

    def Function_2_1311(): pass

    label("Function_2_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_137A")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1347")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 6)
    Jump("loc_137A")

    label("loc_1347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1363")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_137A")

    label("loc_1363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137A")

    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x1, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_13DE")
    OP_66(0x3, 0x1)
    OP_66(0x13, 0x1)
    Jump("loc_1525")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13F0")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1402")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1414")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1426")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1434")
    Jump("loc_1525")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1442")
    Jump("loc_1525")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1454")
    OP_66(0x1, 0x1)
    Jump("loc_1525")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1466")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1474")
    Jump("loc_1525")

    label("loc_1474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1486")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1494")
    Jump("loc_1525")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_14A6")
    OP_66(0x1, 0x1)
    Jump("loc_1525")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14B4")
    Jump("loc_1525")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_14C6")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_14C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_14D4")
    Jump("loc_1525")

    label("loc_14D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_14E6")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_14F8")
    OP_66(0x1, 0x1)
    Jump("loc_1525")

    label("loc_14F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_150A")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_151C")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_1525")

    label("loc_1525")

    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1556")
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)

    label("loc_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1572")
    SetMapObjFrame(0xFF, "box01", 0x0, 0x1)
    Jump("loc_1582")

    label("loc_1572")

    SetMapObjFrame(0xFF, "objects2", 0x0, 0x1)

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CB")
    SetMapObjFrame(0xFF, "objects2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "box01", 0x1, 0x1)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 257500, -1000, 68700, 11000, 5000, 90000)
    Jump("loc_15E8")

    label("loc_15CB")

    SetMapObjFrame(0xFF, "box01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "objects2", 0x1, 0x1)

    label("loc_15E8")

    OP_65(0x2, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1603")
    OP_66(0x2, 0x1)

    label("loc_1603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1616")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1616")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1646")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    OP_65(0x7, 0x1)

    label("loc_1646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165E")
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_65(0x8, 0x1)

    label("loc_165E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1676")
    SetMapObjFrame(0xFF, "05", 0x0, 0x1)
    OP_65(0x9, 0x1)

    label("loc_1676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1699")
    SetMapObjFrame(0xFF, "06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x0, 0x1)
    OP_65(0xA, 0x1)

    label("loc_1699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B1")
    SetMapObjFrame(0xFF, "07", 0x0, 0x1)
    OP_65(0xB, 0x1)

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C9")
    SetMapObjFrame(0xFF, "08", 0x0, 0x1)
    OP_65(0xC, 0x1)

    label("loc_16C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E1")
    SetMapObjFrame(0xFF, "03", 0x0, 0x1)
    OP_65(0xD, 0x1)

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1704")
    SetMapObjFrame(0xFF, "04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x0, 0x1)
    OP_65(0xE, 0x1)

    label("loc_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1720")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1737")

    label("loc_1720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1737")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1737")

    label("loc_1737")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1768")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1783")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1796")
    OP_1B(0x8, 0x0, 0x37)

    label("loc_1796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17A9")
    OP_1B(0x8, 0x0, 0x37)

    label("loc_17A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D3")
    OP_1B(0x0, 0x0, 0x36)

    label("loc_17D3")

    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_17FF")
    SetMapObjFlags(0x7, 0x10)
    OP_65(0x4, 0x1)
    Jump("loc_1809")

    label("loc_17FF")

    ClearMapObjFlags(0x7, 0x10)
    OP_66(0x4, 0x1)

    label("loc_1809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1823")
    OP_65(0xF, 0x1)
    OP_65(0x10, 0x1)
    OP_65(0x11, 0x1)
    OP_65(0x12, 0x1)

    label("loc_1823")

    Return()

    # Function_2_1311 end

    def Function_3_1824(): pass

    label("Function_3_1824")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A69")
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "终端的导力已经停止了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1E")

    #C0002
    ChrTalk(
        0x101,
        (
            "#0000F说起来，总部的\x01",
            "终端线路不是要在\x01",
            "今天进行维护吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1909")

    #C0003
    ChrTalk(
        0x102,
        (
            "#0100F芙兰小姐也说过\x01",
            "这件事呢。\x02\x03",

            "说是今天一天都不能使用终端，\x01",
            "所以她也可以\x01",
            "放假了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E5")

    label("loc_1909")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_197C")

    #C0004
    ChrTalk(
        0x103,
        (
            "#0200F嗯，确实如此。\x02\x03",

            "听芙兰小姐说，因为一整天\x01",
            "都不能使用终端，所以她也可以\x01",
            "得到休假了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E5")

    label("loc_197C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19E5")

    #C0005
    ChrTalk(
        0x104,
        (
            "#0300F是啊，小芙兰\x01",
            "也说过的吧。\x02\x03",

            "今天一天都不能使用终端，\x01",
            "所以她也可以\x01",
            "休息一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E5")


    #C0006
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……我们也\x01",
            "有一段时间没工作了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 5)
    Jump("loc_1A60")

    label("loc_1A1E")


    #C0007
    ChrTalk(
        0x101,
        (
            "#0000F总部的终端线路\x01",
            "正在进行维护，\x01",
            "今天就不能使用终端了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A60")

    TalkEnd(0xFF)
    Return()

    label("loc_1A69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A81")
    Call(1, 20)
    Return()

    label("loc_1A81")

    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFD")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1AC7"),
        (1, "loc_1C73"),
        (SWITCH_DEFAULT, "loc_1FF8"),
    )


    label("loc_1AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AEE")
    OP_2B(0x34, 0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B0F")
    OP_2B(0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1B2A")
    OP_2B(0x2D, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B41")
    OP_2B(0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B5A")
    OP_2B(0x28, 0x29, 0x2A, 0x2F, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1B6D")
    OP_2B(0x25, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1B8C")
    OP_2B(0x22, 0x23, 0x18, 0x1A, 0x1C, 0x1E, 0x21, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BAB")
    OP_2B(0x1F, 0x20, 0x21, 0x18, 0x1A, 0x1C, 0x1E, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BC8")
    OP_2B(0x1B, 0x1C, 0x1D, 0x1E, 0x18, 0x1A, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1BE3")
    OP_2B(0x16, 0x17, 0x18, 0x19, 0x1A, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C00")
    OP_2B(0x11, 0x12, 0x13, 0x14, 0xE, 0x10, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C19")
    OP_2B(0xD, 0xE, 0xF, 0x10, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1C36")
    OP_2B(0x9, 0xA, 0xB, 0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1C4D")
    OP_2B(0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1C69")
    OP_2B(0x1, 0x35, 0x2, 0x3, 0xFFFF)
    Jump("loc_1C6E")

    label("loc_1C69")

    OP_2B(0x1, 0xFFFF)

    label("loc_1C6E")

    Jump("loc_1FF8")

    label("loc_1C73")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("接待小姐芙兰")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1CCF")
    Sound(2062, 255, 100, 0)    #voice#Fran

    #A0008
    AnonymousTalk(
        0xFF,
        "#28A您好，这里是克洛斯贝尔警察局～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CED")

    label("loc_1CCF")

    Sound(2061, 255, 100, 0)    #voice#Fran

    #A0009
    AnonymousTalk(
        0xFF,
        "#26A各位，真是辛苦了～\x02",
    )

    CloseMessageWindow()

    label("loc_1CED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_1F1A")
    Sound(2067, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0010
    AnonymousTalk(
        0xFF,
        "#27A那么，我将对各位的报告进行处理～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA7")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_1D62"),
        (13, "loc_1DAA"),
        (12, "loc_1DEE"),
        (SWITCH_DEFAULT, "loc_1E34"),
    )


    label("loc_1D62")

    Sound(2075, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            "#36A级别１ｓｔ――\x01",
            "罗伊德警官，实在太厉害了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E34")

    label("loc_1DAA")

    Sound(2074, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            "#35A级别２ｎｄ──\x01",
            "罗伊德警官，好厉害呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E34")

    label("loc_1DEE")

    Sound(2073, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "#32A级别３ｒｄ──\x01",
            "罗伊德警官，做得很好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E34")

    label("loc_1E34")

    Sound(2076, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "#31A奖励物品\x01",
            "也会马上给你们送去的～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)    #voice#Fran

    #A0015
    AnonymousTalk(
        0xFF,
        (
            "#34A大家辛苦了～！\x01",
            "以后也请随时来向我报告～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F12")

    label("loc_1EA7")

    Sound(2078, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0016
    AnonymousTalk(
        0xFF,
        "#16A报告就是以上这些吧～\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)    #voice#Fran

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "#37A那么，以后如果完成了新的委托，\x01",
            "请再来向我报告吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F12")

    SetScenarioFlags(0x1, 5)
    Jump("loc_1FEA")

    label("loc_1F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1F91")
    Sound(2063, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            "#32A哎……\x01",
            "刚才已经报告过了哦。        \x02",
        )
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)    #voice#Fran

    #A0019
    AnonymousTalk(
        0xFF,
        "#32A等完成了新的委托之后再来报告吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FEA")

    label("loc_1F91")

    Sound(2065, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            "#37A哎，好像并没有可以\x01",
            "报告的委托哦～\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)    #voice#Fran

    #A0021
    AnonymousTalk(
        0xFF,
        "#16A请下次再来报告吧～\x02",
    )

    CloseMessageWindow()

    label("loc_1FEA")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_1FF8")

    label("loc_1FF8")

    Jump("loc_1A9A")

    label("loc_1FFD")

    OP_E3(0x6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_201D")
    OP_E3(0xB)
    TalkEnd(0xFF)
    Call(0, 9)
    Return()

    label("loc_201D")

    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2047")
    OP_29(0x41, 0x1, 0x1)

    label("loc_2047")

    Return()

    # Function_3_1824 end

    def Function_4_2048(): pass

    label("Function_4_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D7")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【开始临时会议】\x01",      # 0
            "【还有其它要事】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20B4"),
        (1, "loc_2123"),
        (SWITCH_DEFAULT, "loc_21D5"),
    )


    label("loc_20B4")


    #C0022
    ChrTalk(
        0x101,
        (
            "#0001F那么，我们赶快\x01",
            "开始临时会议吧。\x02\x03",

            "首先试着整理一下\x01",
            "和事件有关的情报吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_65(0x2, 0x1)
    Call(0, 18)
    Jump("loc_21D5")

    label("loc_2123")


    #C0023
    ChrTalk(
        0x102,
        (
            "#0100F那么，在处理完其它要事之后，\x01",
            "再回到这里吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "若想召开临时会议，\x01",
            "请靠近桌子，在！的标记出现时\x01",
            "按下○键。  \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_21D5")

    label("loc_21D5")

    EventEnd(0x3)

    label("loc_21D7")

    Return()

    # Function_4_2048 end

    def Function_5_21D8(): pass

    label("Function_5_21D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0025
    AnonymousTalk(
        0x8,
        (
            "那么……\x01",
            "就来听听你们的答复吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7110", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0026
    ChrTalk(
        0x104,
        (
            "#0304F我没问题，\x01",
            "就在这里继续混下去吧。\x02\x03",

            "#0301F话说回来，当时把我拉到\x01",
            "警察局总部的人不就是你嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#5P#1002F呵呵，如果你不愿意待在这里，\x01",
            "我也可以推荐你去一科啊。\x02\x03",

            "他们或许也很需要\x01",
            "你这样的战斗力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#0306F呼……好麻烦，还是免了。\x02\x03",

            "#0300F要是警备队的话倒还可以，\x01",
            "像那种紧张死板的地方就算了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "#5P#1000F艾莉你呢？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#0104F我也想继续\x01",
            "留在这里。\x02\x03",

            "#0100F赛尔盖科长，再次\x01",
            "请您多加关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#5P#1006F呼，你的加入\x01",
            "倒真是连我都没想到呢……\x02\x03",

            "#1001F总部的大人物们之所以会\x01",
            "把你推荐到这里来，是因为他们以为\x01",
            "这个科负责的都是些安全的杂务吧……\x02\x03",

            "当然，这里今后的工作可不是那么\x01",
            "简单的，你应该早有觉悟了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#0102F嗯，当然。\x02\x03",

            "#0104F我已经开始期待着\x01",
            "高密度的繁重工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#5P#1004F哼，有骨气。\x02\x03",

            "#1002F缇欧嘛……嗯，应该就不必再问了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#4P#0203F嗯，因为和这边从最初开始\x01",
            "就是这样约定的。\x02\x03",

            "#0200F话说回来……\x01",
            "今天下午好像有导力缆线的\x01",
            "配线工程吧。\x02\x03",

            "终端的设置\x01",
            "就交给我如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5P#1004F嗯，原本就是这样打算的。\x02\x03",

            "#1000F那么──\x01",
            "就只剩下你了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26D5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_26D5)
    Sleep(50)

    def lambda_26E5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_26E5)
    Sleep(50)

    def lambda_26F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_26F5)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0036
    ChrTalk(
        0x8,
        (
            "#5P#1003F──罗伊德·班宁斯。\x02\x03",

            "毕业于警察学校，在课堂培训和\x01",
            "实战训练中全都取得了优秀成绩──\x02\x03",

            "随即便挑战搜查官资格考试，\x01",
            "并漂亮地取得了资格证。\x02\x03",

            "#1001F说实话，你待在这个科里，\x01",
            "完全可以称得上是屈才了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        "#12P#0001F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#5P#1004F像你这种人才，无论\x01",
            "去哪个科就职，恐怕都是游刃有余的。\x02\x03",

            "已经有好几个人来要求我\x01",
            "放你去他们的部门了。\x02\x03",

            "#1002F你是不是也感到有些犹豫呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#12P#0004F──不。\x01",
            "我在经过多方面的考虑之后，已经做出了决定。\x02\x03",

            "#0000F赛尔盖科长，\x01",
            "今后请您多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#11P#0302F嘿嘿……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#11P#0102F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#12P#0202F………………………………\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#5P#1006F什么嘛，真是没意思。\x02\x03",

            "我还期待你会稍微露出些\x01",
            "烦恼迷惑的表情呢～……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#12P#0012F……请您严肃一点啊。\x02",
    )

    CloseMessageWindow()

    def lambda_29D2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29D2)
    Sleep(50)

    def lambda_29E2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_29E2)
    Sleep(50)

    def lambda_29F2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_29F2)
    WaitChrThread(0x103, 2)
    Sleep(300)

    #C0045
    ChrTalk(
        0x8,
        (
            "#5P#1003F算啦，今天一天，\x01",
            "就让你们全体休假好了。\x02\x03",

            "把这当做是地狱般的工作量到来之前，\x01",
            "最后的一次休假吧。\x02\x03",

            "#1002F啊，缇欧。\x01",
            "终端的设置就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        "#12P#0204F是，了解。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P#1005F噢……\x01",
            "对了，把这个给忘了。\x02\x03",

            "#1003F那么，再次确认──\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#12P#0001F到！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#5P#1001F艾莉·麦克道尔。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#0101F到。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#5P#1001F兰迪·奥兰多。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        "#0301F在。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "#5P#1001F缇欧·普拉托。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#12P#0201F……到。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#5P#1003F本日９：００，\x01",
            "正式认可以上四名人员分配至此。\x02\x03",

            "#1002F欢迎来到特别任务支援科。\x02\x03",

            "你们今后将要面对的，是\x01",
            "五花八门、堆积如山的工作。\x01",
            "请尽情期待吧──\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "作为初期调查的津贴，\x01\x07\x02",

            "１０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(1000)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("t4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_21D8 end

    def Function_6_2D03(): pass

    label("Function_6_2D03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 2350, 5200, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 11300, 900, 6650, 90)
    SetChrPos(0x102, 11300, 900, 4600, 90)
    SetChrPos(0x103, 13900, 900, 4600, 270)
    SetChrPos(0x104, 11300, 900, 2550, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrSubChip(0x8, 0x1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis011.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性的声音")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            "──那么，从今天开始，\x01",
            "就要正式展开工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7110", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(12600, 1850, 5200, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0058
    ChrTalk(
        0x8,
        (
            "#5P#1000F好啦，不管怎么样，\x01",
            "总之先补充说明一下好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    #C0059
    ChrTalk(
        0x8,
        "#11P#1000F罗伊德，把调查手册拿出来。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0001F啊……是的！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #A0061
    AnonymousTalk(
        0x104,
        (
            "#0300F是那个印有警察徽章的黑色手册吗，\x01",
            "这东西确实很有调查手册的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0062
    AnonymousTalk(
        0x102,
        (
            "#0100F这个也可以算是警官的\x01",
            "身份证明吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0063
    AnonymousTalk(
        0x8,
        (
            "#1003F嗯，而且上面还记载着\x01",
            "各种说明与注意事项。\x02\x03",

            "同时也有着关于战术导力器的说明，\x01",
            "你们可以适当参考。\x02\x03",

            "#1002F──不过，这手册最主要的用处\x01",
            "是对『调查状况』的记录与确认。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x104,
        "#0305F『调查状况』……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0065
    AnonymousTalk(
        0x8,
        "#1003F罗伊德，你来说明。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0066
    AnonymousTalk(
        0x101,
        (
            "#0000F啊，是。\x01",
            "（这都是在警察学校里学过的东西啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0067
    ChrTalk(
        0x101,
        (
            "#0000F──根据警察局的规定，\x01",
            "无论进行何种调查任务，\x01",
            "都要做好详细记录。\x02\x03",

            "#0003F在接受了调查任务之后，\x01",
            "就要把调查过程中的一切进展与\x01",
            "状况记录到调查手册上。\x02\x03",

            "在完成任务之后，还要用它来进行报告，\x01",
            "所以也关系到考勤评定与特别津贴的发放。\x02\x03",

            "#0000F因此，在记录的时候，\x01",
            "一定要尽可能的详细简练。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        "#6P#0100F原来如此，很有道理啊。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#12P#0306F唉……\x01",
            "听起来好像真是很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#11P#1000F嗯，大概就是这样。\x02\x03",

            "#1003F不过呢，在我们特别任务支援科，\x01",
            "情况会稍微有些特殊。\x02\x03",

            "#1002F除了正规的『调查任务』之外，\x01",
            "还会有一些其它的『支援请求』。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)

    #C0071
    ChrTalk(
        0x101,
        "#0005F哎……\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    #C0072
    ChrTalk(
        0x8,
        "#5P#1002F缇欧，下面就拜托你了。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        "#2P#0203F……是。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 14800, 850, 5400, 270)
    OP_0D()
    Sleep(300)

    #C0074
    ChrTalk(
        0x103,
        "#2P#0200F各位，请看这里。\x02",
    )

    CloseMessageWindow()
    OP_68(16100, 1850, 10000, 3000)
    MoveCamera(7, 21, 0, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_343C():
        OP_95(0xFE, 16100, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_343C)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_90(0x8, 14700, 850, 7600, 270)
    OP_0D()
    OP_92(0x8, 0x396C, 0x2BC0, 0x1F4)

    def lambda_3485():
        OP_95(0xFE, 14700, 850, 11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3485)
    WaitChrThread(0x103, 1)

    def lambda_34A3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_34A3)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_90(0x101, 10400, 850, 7600, 90)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, 10400, 850, 5400, 125)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x104, 10400, 850, 3200, 125)
    OP_0D()
    BeginChrThread(0x104, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 7)
    OP_92(0x101, 0x3B60, 0x2134, 0x1F4)
    Sleep(150)

    def lambda_352C():
        OP_95(0xFE, 15200, 850, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_352C)
    WaitChrThread(0x8, 1)

    def lambda_354A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_354A)
    WaitChrThread(0x101, 1)

    def lambda_355B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_355B)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x51)

    #C0075
    ChrTalk(
        0x101,
        "#6P#0000F啊，这是前天的……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#3P#0100F这个就是连接到导力网络的\x01",
            "终端装置吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    #C0077
    ChrTalk(
        0x103,
        (
            "#11P#0200F是的，我在昨天\x01",
            "已经设置完毕了。\x02\x03",

            "基本来说，它会一直保持着运行状态，\x01",
            "登陆之后，就会转到这个画面。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(300)
    Sound(72, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)

    #A0078
    AnonymousTalk(
        0x104,
        "#0305F好像出现了什么文字呢……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0079
    AnonymousTalk(
        0x101,
        "#0005F要在这里……接受『支援请求』吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0080
    AnonymousTalk(
        0x8,
        (
            "#1000F嗯，除了正规的任务之外，\x01",
            "这里还会收到从各处发来的委托。\x02\x03",

            "#1003F例如市民和游客的委托，\x01",
            "克洛斯贝尔市政府的协助请求等等，\x01",
            "大概会有各式各样的委托吧。\x02\x03",

            "#1002F但这些委托并不一定要全部接受──\x01",
            "有些任务，就算放着不管，\x01",
            "也会有游击士那边的人负责解决。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_381B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_381B)
    Sleep(50)

    def lambda_382B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_382B)
    Sleep(50)

    def lambda_383B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_383B)
    WaitChrThread(0x103, 2)

    #C0081
    ChrTalk(
        0x101,
        "#12P#0001F啊……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        "#3P#0309F哈哈，原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#3P#0103F游击士在市民中有着极高的评价，\x01",
            "而我们或多或少也要为警察挽回一些声誉……\x02\x03",

            "#0100F大概就是这么一回事吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0084
    ChrTalk(
        0x8,
        (
            "#5P#1002F哈，算是吧。\x02\x03",

            "除此之外，在总部繁忙的时候，\x01",
            "大概也会叫你们帮忙。\x02\x03",

            "像市内的巡逻工作啦，或是\x01",
            "一些无足轻重的文案工作啦，等等。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x104,
        "#3P#0306F呼……不是开玩笑的吧。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#12P#0012F哈哈……\x01",
            "总之，先不说那个。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#0000F好像已经有『支援请求』\x01",
            "被发送到这个终端了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "#5P#1003F哦，那你们就\x01",
            "自己去确认吧。\x02\x03",

            "#1000F在进行确认之后，记得将『支援请求』\x01",
            "记录在调查手册里啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    #C0089
    ChrTalk(
        0x101,
        "#12P#0000F了解。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x40)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetScenarioFlags(0x41, 5)
    OP_29(0x3D, 0x4, 0x2)
    OP_29(0x3D, 0x1, 0x0)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_2D03 end

    def Function_7_3B2B(): pass

    label("Function_7_3B2B")

    Sleep(100)

    def lambda_3B33():
        OP_95(0xFE, 10400, 850, 9300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B33)
    WaitChrThread(0x102, 1)

    def lambda_3B51():
        OP_95(0xFE, 14000, 850, 9300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B51)
    WaitChrThread(0x102, 1)
    Return()

    # Function_7_3B2B end

    def Function_8_3B6B(): pass

    label("Function_8_3B6B")


    def lambda_3B70():
        OP_95(0xFE, 10400, 850, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B70)
    WaitChrThread(0x104, 1)

    def lambda_3B8E():
        OP_95(0xFE, 13200, 850, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B8E)
    WaitChrThread(0x104, 1)
    Return()

    # Function_8_3B6B end

    def Function_9_3BA8(): pass

    label("Function_9_3BA8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 14100, 850, 9500, 45)
    SetChrPos(0x104, 15600, 850, 8000, 45)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 12400, 850, 10200, 90)
    OP_4B(0x8, 0xFF)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【支援请求的补充说明】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #C0091
    ChrTalk(
        0x104,
        (
            "#12P#0305F哎，我还以为是什么大任务，\x01",
            "原来只是工作联络而已啊。\x02\x03",

            "#0300F总之，只要去警察局总部\x01",
            "听取那些说明就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#5P#0003F是啊，似乎是这样没错。\x02\x03",

            "#0000F不过，『导力网络』吗……\x01",
            "好像有点明白\x01",
            "它是什么东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#11P#0100F和通讯器有所区别的是，\x01",
            "它除了声音之外，连图像和文字情报也能发送呢。\x02\x03",

            "之前也听过相关介绍……\x01",
            "现在看来，确实是可以应用到各种场合呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#6P#0203F嗯，现在已经开始在克洛斯贝尔\x01",
            "进行各种各样的实验应用了。\x02\x03",

            "#0200F目前导入警察局的这个\x01",
            "系统也是其中一环呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#6P#1003F嗯，听说在游击士协会\x01",
            "也导入了同样技术的试验装置呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x12C)
    Sleep(300)

    #C0096
    ChrTalk(
        0x8,
        (
            "#6P#1002F──概要就是这些了。\x02\x03",

            "那么，你们就尽快\x01",
            "将刚才那个『支援请求』\x01",
            "完成吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3FAE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FAE)
    Sleep(50)

    def lambda_3FBE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3FBE)
    Sleep(50)

    def lambda_3FCE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3FCE)
    Sleep(50)

    def lambda_3FDE():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3FDE)
    WaitChrThread(0x103, 2)

    #C0097
    ChrTalk(
        0x101,
        (
            "#11P#0000F明白了。\x02\x03",

            "#0001F那个，接下来\x01",
            "该做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "#3P#1003F随你们高兴……本来是想这样说的，\x01",
            "不过，在你们去总部听取说明之后，应该\x01",
            "就会接到好几件正式的支援请求了。\x02\x03",

            "#1002F……对了。\x02\x03",

            "考虑到是第一次，而且还要向总部交差，\x01",
            "所以你们至少先完成一件委托吧。\x02\x03",

            "那样一来，总部的人也就\x01",
            "不会像那样挖苦讽刺你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x101,
        "#11P#0006F（问题并不在那里吧……）\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    #C0100
    ChrTalk(
        0x8,
        (
            "#3P#1000F另外，罗伊德……\x01",
            "你顺便带大家熟悉一下市里吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        "#11P#0005F熟悉一下……市里吗？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#3P#1000F这个城市，可以说是你们今后\x01",
            "将要守护的地方了。\x01",
            "所以先亲眼做个大致的了解吧。\x02\x03",

            "出门之后，附近就有武器商会\x01",
            "和『导力商店』，先去这两个\x01",
            "地方看看吧。\x02\x03",

            "身为警官，今后可能\x01",
            "经常需要到那里去。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#11P#0000F原来如此……明白了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(300)

    #C0104
    ChrTalk(
        0x8,
        (
            "#3P#1003F我基本上都会待在那边的房间里，\x01",
            "但还要午睡、看杂志，所以很忙的。\x02\x03",

            "如果有事的话，最好别打扰我，\x01",
            "尽量自己解决吧。\x02\x03",

            "#1002F那就先这样吧～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43AF():

        label("loc_43AF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_43AF")

    QueueWorkItem2(0x101, 2, lambda_43AF)

    def lambda_43C1():

        label("loc_43C1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_43C1")

    QueueWorkItem2(0x102, 2, lambda_43C1)

    def lambda_43D3():

        label("loc_43D3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_43D3")

    QueueWorkItem2(0x104, 2, lambda_43D3)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(1000)

    def lambda_43EE():

        label("loc_43EE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_43EE")

    QueueWorkItem2(0x103, 2, lambda_43EE)
    Sleep(1000)

    #C0105
    ChrTalk(
        0x101,
        "#6P#0011F等、等一下……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#0301F喂喂……\x01",
            "真是个不负责任的大叔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#0106F唉，这样散漫，不要紧吗？\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x103,
        "#0211F……对今后充满不安呢。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#0012F算、算啦……\x01",
            "总之，这是我们的初次任务。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(15900, 1750, 9800, 1500)

    def lambda_44E8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44E8)
    Sleep(50)

    def lambda_44F8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_44F8)
    Sleep(50)

    def lambda_4508():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4508)
    Sleep(50)

    def lambda_4518():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4518)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    #C0110
    ChrTalk(
        0x101,
        (
            "#5P#0000F先在市内逛一逛，\x01",
            "然后就去处理『支援请求』吧。\x02\x03",

            "因为是第一次，所以不必太过焦急。\x01",
            "要把事情稳妥处理好。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#2P#0100F嗯，说得也是。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#6P#0204F了解。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#12P#0300F嗯，那我们就出发吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※使用○键调查放置在支援科的终端装置，  \x01",
            "  在项目列表中选择［确认支援请求］，\x01",
            "  即可阅览发送给罗伊德等人的工作委托（任务）一览表。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※虽然并没有必要接受每一个委托，\x01",
            "  但顺利完成之后，便可获得ＤＰ与米拉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(15000, 1850, 8900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrPos(0x1, 15000, 850, 8900, 225)
    SetChrPos(0x2, 15000, 850, 8900, 225)
    SetChrPos(0x3, 15000, 850, 8900, 225)
    SetScenarioFlags(0x41, 6)
    OP_29(0x3D, 0x1, 0x1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    PlayBGM("ed7100", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_9_3BA8 end

    def Function_10_47A9(): pass

    label("Function_10_47A9")

    OP_68(15900, 1750, 5400, 4000)

    def lambda_47BF():
        OP_95(0xFE, 16500, 850, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47BF)
    WaitChrThread(0x8, 1)

    def lambda_47DD():
        OP_95(0xFE, 16500, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47DD)
    WaitChrThread(0x8, 1)

    def lambda_47FB():
        OP_95(0xFE, 18300, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47FB)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_482E():
        OP_95(0xFE, 19800, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_482E)
    Sleep(300)

    def lambda_484B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_484B)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x1)
    Return()

    # Function_10_47A9 end

    def Function_11_4883(): pass

    label("Function_11_4883")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50091.itc", 0x1E)
    OP_68(64000, 1100, 11400, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 58500, 0, 3200, 90)
    SetChrPos(0x102, 58500, 0, 3200, 90)
    SetChrPos(0x103, 58500, 0, 3200, 90)
    SetChrPos(0x104, 58500, 0, 3200, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x1D)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 63700, 750, 10300, 0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x9, 0x80)
    LoadEffect(0x0, "event\\eva05_00.eff")
    PlayEffect(0x0, 0x0, 0x8, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_68(64000, 1100, 8600, 5000)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 14)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0116
    AnonymousTalk(
        0x8,
        (
            "噢噢，回来了啊。\x02\x03",

            "已经顺利阻止了\x01",
            "不良团伙的斗殴了？\x02",
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

    #C0117
    ChrTalk(
        0x101,
        (
            "#12P#0006F科长……这个嘛。\x02\x03",

            "#0001F情况可能会\x01",
            "变得比较麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "#5P#1005F嗯……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将事情的经过\x01",
            "对赛尔盖进行了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0120
    ChrTalk(
        0x8,
        (
            "#5P#1001F……哼，原来如此啊。\x02\x03",

            "#1003F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0121
    ChrTalk(
        0x101,
        "#12P#0005F那个，科长……？\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#5P#1003F……好吧。\x02\x03",

            "#1000F这件事情，就交给你们\x01",
            "全权处理吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x101,
        "#12P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        "#0105F那个，这是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#5P#1003F就此罢手也好，继续追查下去也好，\x01",
            "一切都交给你们自己去判断。\x02\x03",

            "#1000F关于『鲁巴彻』方面的事情，\x01",
            "我也没有什么可告诉你们的。\x02\x03",

            "全部都要靠你们自己去调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#12P#0013F这、这种不负责任的发言也太乱来了吧……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#5P#1001F……如果我让你们就此收手的话，\x01",
            "你们能接受吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x101,
        "#12P#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#5P#1003F只要牵扯到黑手党，\x01",
            "情况肯定就会变得非常麻烦。\x02\x03",

            "如果要我以上司的立场\x01",
            "做出最妥当的判断，\x01",
            "那我也只能让你们别再管了。\x02\x03",

            "#1001F那样也可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#12P#0008F…………不。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#0306F哎，如果在这种时候放弃，\x01",
            "以后要是想起来，也许会觉得很不甘心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0108F是啊……\x01",
            "我们都已经了解到这么多情况了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#4P#0203F……同感。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#5P#1004F──嗯，不过呢。\x02\x03",

            "如果放任你们这群什么都不懂的小鬼们\x01",
            "莽撞乱来，最后身受重伤的话，\x01",
            "我大概也会睡不安稳吧……\x02\x03",

            "#1002F所以至少也给你们介绍一位有用的\x01",
            "指引者吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#12P#0005F有用的指引者……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 62800, 0, 11600, 270)
    Sound(820, 0, 100, 0)

    def lambda_50C1():

        label("loc_50C1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50C1")

    QueueWorkItem2(0x101, 2, lambda_50C1)

    def lambda_50D3():

        label("loc_50D3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50D3")

    QueueWorkItem2(0x102, 2, lambda_50D3)

    def lambda_50E5():

        label("loc_50E5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50E5")

    QueueWorkItem2(0x103, 2, lambda_50E5)

    def lambda_50F7():

        label("loc_50F7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50F7")

    QueueWorkItem2(0x104, 2, lambda_50F7)
    OP_0D()

    def lambda_510A():
        OP_95(0xFE, 61600, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_510A)
    WaitChrThread(0x8, 1)
    OP_68(64120, 1100, 7920, 2500)

    def lambda_5139():
        OP_95(0xFE, 61600, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5139)
    WaitChrThread(0x8, 1)

    def lambda_5157():
        OP_95(0xFE, 63000, 0, 7800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5157)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrName("")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔盖递给罗伊德一张名片。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0005F『格里姆伍德法律事务所』？\x02\x03",

            "#0001F哎，好像在哪里\x01",
            "听到过这个名字呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#1004F#5P那是家位于西街的法律事务所。\x02\x03",

            "#1002F里面有位名叫伊安的\x01",
            "大胡子律师。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#12P#0000F啊啊……！\x01",
            "那家事务所就在面包店的后面吧？\x02\x03",

            "说起来，我以前住在那里时，\x01",
            "也曾和他打过几次招呼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#0104F我也听说过。\x02\x03",

            "#0100F伊安律师好像是为企业、贸易商等群体\x01",
            "提供法律咨询的律师吧？\x02\x03",

            "同时，他好像也经常亲自给一般市民\x01",
            "提供法律援助……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#1003F#5P嗯，因为他满脸胡子，像熊一样，\x01",
            "所以总是被人称作『大胡子熊先生』。\x02\x03",

            "那位律师应该掌握着\x01",
            "不少关于黑手党的情报。\x02\x03",

            "#1002F说不定……\x01",
            "甚至还有一些连警察都不了解的最新情报呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0142
    ChrTalk(
        0x101,
        "#12P#0002F啊……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        "#12P#0202F……那可真是很厉害呢。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        "#2P#0305F那位律师到底是何方神圣啊？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#1004F#5P哈，见到他之后，马上就会知道啦。\x02\x03",

            "#1000F我之前去见他的时候，\x01",
            "也提起过有关特别任务支援科的事。\x02\x03",

            "只要你们将自己的身份表明，\x01",
            "他至少应该会把你们的话听完。\x02\x03",

            "正好趁这个机会去和他打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#12P#0001F明、明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_55AE():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_55AE)
    Sleep(150)

    def lambda_55BE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55BE)
    Sleep(50)

    def lambda_55CE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_55CE)
    Sleep(50)

    def lambda_55DE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_55DE)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#0000F……西街离这里很近。\x02\x03",

            "总之，我们就去那个\x01",
            "法律事务所拜访一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#11P#0100F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrFlags(0x8, 0x80)
    StopEffect(0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_68(64000, 1330, 6000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 64000, 0, 6000, 0)
    SetChrPos(0x1, 64000, 0, 6000, 0)
    SetChrPos(0x2, 64000, 0, 6000, 0)
    SetChrPos(0x3, 64000, 0, 6000, 0)
    SetScenarioFlags(0x42, 6)
    OP_29(0x3E, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_11_4883 end

    def Function_12_570E(): pass

    label("Function_12_570E")


    def lambda_5713():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5713)
    Sleep(500)

    def lambda_5730():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5730)
    WaitChrThread(0x101, 1)

    def lambda_5745():
        OP_95(0xFE, 63000, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5745)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_12_570E end

    def Function_13_5766(): pass

    label("Function_13_5766")


    def lambda_576B():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_576B)
    Sleep(500)

    def lambda_5788():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5788)
    WaitChrThread(0x102, 1)

    def lambda_579D():
        OP_95(0xFE, 64300, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_579D)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_13_5766 end

    def Function_14_57BE(): pass

    label("Function_14_57BE")


    def lambda_57C3():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57C3)
    Sleep(500)

    def lambda_57E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_57E0)
    WaitChrThread(0x103, 1)

    def lambda_57F5():
        OP_95(0xFE, 63200, 0, 5400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57F5)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_14_57BE end

    def Function_15_5816(): pass

    label("Function_15_5816")


    def lambda_581B():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_581B)
    Sleep(500)

    def lambda_5838():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5838)
    WaitChrThread(0x104, 1)

    def lambda_584D():
        OP_95(0xFE, 64500, 0, 5400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_584D)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_15_5816 end

    def Function_16_586E(): pass

    label("Function_16_586E")

    OP_92(0x8, 0xF0A0, 0x1FA4, 0x1F4)

    def lambda_5880():
        OP_95(0xFE, 61600, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5880)
    WaitChrThread(0x8, 1)

    def lambda_589E():
        OP_95(0xFE, 61600, 30, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_589E)
    WaitChrThread(0x8, 1)

    def lambda_58BC():
        OP_95(0xFE, 62800, 30, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58BC)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrPos(0x8, 64000, 0, 11500, 180)

    def lambda_58F0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58F0)

    def lambda_58FD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_58FD)

    def lambda_590A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_590A)

    def lambda_5917():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5917)
    OP_0D()
    Return()

    # Function_16_586E end

    def Function_17_5921(): pass

    label("Function_17_5921")

    EventBegin(0x0)
    Fade(1000)
    OP_68(9900, 1750, 10600, 0)
    MoveCamera(50, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 9900, 850, 9800, 90)
    SetChrPos(0x103, 9900, 850, 11000, 135)
    SetChrPos(0x102, 8700, 850, 9800, 90)
    SetChrPos(0x104, 8700, 850, 11000, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0149
    ChrTalk(
        0x101,
        "#6P#0005F那是……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        "#6P#0105F……好像写着什么呢。\x02",
    )

    CloseMessageWindow()
    OP_68(16800, 1750, 7500, 3500)

    def lambda_5A00():
        OP_95(0xFE, 16500, 850, 7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A00)
    Sleep(300)

    def lambda_5A1D():
        OP_96(0xFE, 0x3F48, 0x352, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A1D)
    Sleep(300)

    def lambda_5A3A():
        OP_95(0xFE, 15100, 850, 6500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A3A)
    Sleep(300)

    def lambda_5A57():
        OP_96(0xFE, 0x39D0, 0x352, 0x206C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A57)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    SetChrName("")

    #A0151
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "留言板上写有文字。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『有点私事，出去了。\x01",
            "  那件事就交给你们随便处理吧。\x01",
            "                       赛尔盖』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0153
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0003F科长不在吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3P#0301F那个大叔不会因为\x01",
            "怕麻烦，所以故意逃走了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0203F确实无法否定\x01",
            "那种可能性呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)

    #C0156
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#12P#0100F算啦算啦……\x01",
            "其实允许我们自由处理，\x01",
            "也算是对我们有利。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0157
    ChrTalk(
        0x102,
        (
            "#6P#0101F那么，该怎么办？\x02\x03",

            "要立刻展开关于\x01",
            "此次事件的临时会议吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0158
    ChrTalk(
        0x101,
        "#11P#0000F嗯，我想想──\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "若想召开临时会议，\x01",
            "请靠近桌子，在！的标记出现时\x01",
            "按下○键。  \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 16500, 850, 7000, 90)
    ModifyEventFlags(0, 0, 0x80)
    OP_66(0x2, 0x1)
    SetScenarioFlags(0x43, 1)
    OP_29(0x3E, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_17_5921 end

    def Function_18_5D00(): pass

    label("Function_18_5D00")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    OP_68(12600, 2350, 7000, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13500, 850, 8400, 315)
    SetChrPos(0x102, 13900, 900, 6650, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white_sd", 0x0, 0x1)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xA, 0x17)
    OP_49()
    SetChrPos(0x17, 12600, 850, 9500, 0)
    OP_D3(0x17, 0x0, 0x0, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis012.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis013.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis114.itp")
    PlayBGM("ed7516", 0)
    OP_68(12600, 1850, 7000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0160
    ChrTalk(
        0x101,
        (
            "#11P#0003F──案发时间是五天前的深夜。\x02\x03",

            "『剑蛇帮』和\x01",
            "『圣书会』的成员\x01",
            "都遭受到了某些人的袭击。\x02\x03",

            "#0001F案发地点是旧城区中两个不同的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(300)

    #A0161
    AnonymousTalk(
        0x101,
        "#0001F也就是这里，还有这里。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(1000)
    OP_C9(0x3, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(500)

    #A0162
    AnonymousTalk(
        0x102,
        (
            "#0101F『圣书会』的成员\x01",
            "遭到袭击的地点是西边的小巷……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0163
    AnonymousTalk(
        0x104,
        (
            "#0301F然后，东边的小剧场门前\x01",
            "则是『剑蛇帮』的成员\x01",
            "遭到袭击的地点。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x103,
        (
            "#6P#0205F……这么一看的话，\x01",
            "就是旧城区完全相反的两侧呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_6287")
    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0165
    ChrTalk(
        0x101,
        (
            "#5P#0001F嗯，所以两起事件即使是在同一夜发生，\x01",
            "双方应该也无法立刻得知对方成员遇袭。\x02\x03",

            "#0008F把伤员运送到各自的据点进行\x01",
            "包扎救治，第二天早上再送往医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#12P#0101F被袭击的两个人好像\x01",
            "是用同一辆急救车送走的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯，急救车上的工作人员\x01",
            "想必也很手忙脚乱吧。\x02\x03",

            "#0001F接下来，双方才终于确信\x01",
            "此次暗算是对方下的手了。\x01",
            "然后事态便发展至如今的状况──大概就是这样了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_633F")

    label("loc_6287")


    #C0168
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯，两起事件即使是在同一夜发生，\x01",
            "双方应该也无法立刻得知对方成员遇袭。\x02\x03",

            "#0000F接下来，双方终于确信\x01",
            "此次暗算是对方下的手了。\x01",
            "然后事态便发展至如今的状况──大概就是这样了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_633F")


    #C0169
    ChrTalk(
        0x104,
        (
            "#6P#0306F嗯……这样一来，\x01",
            "果然只能理解为，有第三方势力插手吧。\x02\x03",

            "#0301F双方成员都没有\x01",
            "事先统一过口径，在此情况下，\x01",
            "恐怕任何一方都没有作案的可能吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯……以现阶段的情报为基础，\x01",
            "暂时先把两起案件都假设为\x01",
            "是第三者所为吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#12P#0104F是啊……\x01",
            "不把握住每一点可能性的话，\x01",
            "推理也就无法继续进展了。\x02\x03",

            "#0101F──那么，关于那个第三者，\x01",
            "我们应该已经可以想到那个名字了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#5P#0003F是啊。\x02\x03",

            "#0001F『鲁巴彻商会』，\x01",
            "他们是掌控着克洛斯贝尔\x01",
            "黑道势力的黑手党。\x02\x03",

            "根据格蕾丝小姐的情报，\x01",
            "大约在半个月之前，曾有人在\x01",
            "旧城区目击到了他们的成员。\x02\x03",

            "#0006F我们现在并没有时间去\x01",
            "确认这个情报的真假，不过……\x02\x03",

            "#0001F暂且就先假定这两起伤害\x01",
            "事件都是『鲁巴彻』所为，然后\x01",
            "以这个假设为前提继续推理下去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#6P#0203F……这样一来……\x02\x03",

            "#0201F接下来的问题果然就是『动机』了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯，那正是关键问题。\x02\x03",

            "#0001F……反过来说，\x01",
            "如果不把这个问题弄清，\x01",
            "推理说不定还会回到原点。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x104,
        (
            "#6P#0303F嗯～动机嘛……\x02\x03",

            "#0308F黑手党和两个不良团伙，\x01",
            "这三方之间应该也扯不上什么利害关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#12P#0103F连接三『点』，\x01",
            "结成一『线』……\x02\x03",

            "#0100F──那个，罗伊德，\x01",
            "你心里应该已经大致有数了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#5P#0004F哈哈，虽然还不能\x01",
            "完全确信吧……\x02\x03",

            "#0000F连接三『点』，结成一『线』。\x01",
            "这样的话，应该考虑的是──\x02",
        )
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
            "【瓦吉的经历】\x01",        # 0
            "【瓦鲁多的过去】\x01",      # 1
            "【黑月的存在】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_684D"),
        (1, "loc_6A63"),
        (2, "loc_6BA2"),
        (SWITCH_DEFAULT, "loc_6D5B"),
    )


    label("loc_684D")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0178
    ChrTalk(
        0x101,
        (
            "#5P#0003F这也许是个比较荒谬的\x01",
            "想法，不过……\x02\x03",

            "#0001F两年前出现在旧城区的\x01",
            "瓦吉，有可能正是那条『线』。\x02\x03",

            "比如说，他有可能是鲁巴彻首领的\x01",
            "儿子什么的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0179
    ChrTalk(
        0x102,
        "#12P#0105F然、然后呢……！？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        "#6P#0301F喂喂，这是真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        (
            "#5P#0006F可能性，只是可能性而已啦。\x02\x03",

            "#0000F在这种情况下，首领为了\x01",
            "将离家出走的儿子带回去，\x01",
            "就在旧城区设计了那两起事件。\x02\x03",

            "#0012F不过，假设到这个份上，\x01",
            "与其说是推理，倒更像是在幻想了……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        "#6P#0306F喂喂……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D5B")

    label("loc_6A63")


    #C0183
    ChrTalk(
        0x101,
        (
            "#5P#0003F虽然这仅仅是一种可能性……\x02\x03",

            "#0001F也许那个瓦鲁多过去\x01",
            "曾经得罪过黑手党中的\x01",
            "某个成员。\x02\x03",

            "于是招来怨恨与报复，\x01",
            "从而引发了这次的事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#12P#0106F嗯～……\x01",
            "这种情况确实也不能排除。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        (
            "#6P#0301F但是，就为了这种程度的小事，\x01",
            "再怎么说也不会如此大费周折吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        "#5P#0006F……确实如此，果然是想错了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D5B")

    label("loc_6BA2")

    OP_2C(0x3E, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0187
    ChrTalk(
        0x101,
        (
            "#5P#0003F说到可能性的话……\x01",
            "比较实际的也就是『黑月』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        (
            "#6P#0305F哦哦，是那位大胡子先生\x01",
            "和我们说的那个组织吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        (
            "#12P#0103F确实，在各种可能性之中，\x01",
            "这个大概是最接近真相的……\x02\x03",

            "#0101F不过，如果是这样的话，\x01",
            "要怎样才能把事件连成一条线呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#6P#0203F如果想把各个点连接成一条线，\x01",
            "就需要某种程度的『必然性』……\x02\x03",

            "#0200F也就是说，『黑月』与\x01",
            "黑手党袭击两组不良团伙这件事\x01",
            "之间，存在着某些『必然性』的联系吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D5B")

    label("loc_6D5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EFF")
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0191
    ChrTalk(
        0x103,
        (
            "#6P#0200F……那个，罗伊德前辈。\x02\x03",

            "『黑月』才是那条线——难道就没有\x01",
            "这个可能性吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)

    #C0192
    ChrTalk(
        0x101,
        "#5P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#6P#0305F喂喂，难道幕后真凶不是\x01",
            "黑手党，而是同他们对抗的组织吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        (
            "#6P#0203F不……我们是在『真凶是黑手党』\x01",
            "这个前提下展开讨论的。\x02\x03",

            "#0200F在此基础上，『黑月』也有可能\x01",
            "就是那条『线』吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EFF")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0195
    ChrTalk(
        0x101,
        (
            "#5P#0008F──是啊。\x01",
            "这样一来，就能说得通了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x2)

    #C0196
    ChrTalk(
        0x102,
        "#12P#0105F哎……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        "#6P#0300F你想到什么了吗？\x02",
    )

    CloseMessageWindow()

    def lambda_6FC6():
        OP_95(0xFE, 12600, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FC6)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0198
    ChrTalk(
        0x101,
        (
            "#0001F#5P就是那个『必然性』。\x02\x03",

            "如果『黑月』想要在克洛斯贝尔的黑道势力分一杯羹，\x01",
            "那么鲁巴彻将会采取何种对策呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#6P#0305F这个嘛……\x01",
            "单纯来考虑，就是增强战斗力吧。\x02\x03",

            "#0303F部队的增强和武装的强化，\x01",
            "这两点他们应该都会想要实现吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0003F#5P身为黑手党，武装强化方面应该\x01",
            "可以通过走私交易来解决。\x02\x03",

            "#0001F可是，他们该如何增加战斗人员呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        "#6P#0305F这个……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x102,
        (
            "#12P#0108F按照一般想法来考虑的话，\x01",
            "自然是雇佣猎兵团吧……\x02\x03",

            "#0103F……不对，好像行不通呢。\x01",
            "克洛斯贝尔这个地区在很多意义上\x01",
            "都一直被周边诸国密切注视着。\x02\x03",

            "#0101F再加上《互不侵犯条约》的签订，\x01",
            "在这种情况下，如果擅自动用猎兵团的话，\x01",
            "帝国与共和国恐怕都不会坐视不理的。\x02\x03",

            "而遵从两国意愿的那些\x01",
            "政治家与议员们也是一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0203
    ChrTalk(
        0x102,
        "#12P#0105F──啊。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        "#6P#0205F罗伊德前辈，莫非他们……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x104,
        (
            "#6P#0301F是想将那些不良团伙的成员\x01",
            "当作部队的候补士兵！？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯……那些成员们都是一些血气方刚，\x01",
            "并且具有一定组织性的年轻人。\x02\x03",

            "#0001F作为在这个城市中使用的战斗力，\x01",
            "他们实在是再合适不过了吧。\x02\x03",

            "可是，无论在哪个团伙中，\x01",
            "都存在着很大的障碍呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        (
            "#12P#0101F原来如此……\x02\x03",

            "不出意外的话，那个瓦吉\x01",
            "应该是不会愿意协助黑手党的……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#6P#0203F而以那个瓦鲁多先生的性格来说，\x01",
            "应该也只想当老大……\x02\x03",

            "#0201F无论如何，他肯定也不会愿意\x01",
            "在黑手党的手下工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        (
            "#6P#0308F所以，要设计让他们自相残杀，\x01",
            "使两边的实力都被削弱。然后抓准时机，\x01",
            "一口气将他们全都收为己用……\x02\x03",

            "#0301F原来如此，是这么回事啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#0012F#5P这仅仅是可能之一罢了。\x02\x03",

            "#0000F而且也只是将现有的情报\x01",
            "逐一拼凑起来的结果而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x104,
        (
            "#6P#0309F又来了～！\x01",
            "何必这么谦虚嘛～！\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x102,
        (
            "#12P#0104F嗯，我也认为这种\x01",
            "分析很接近真相了。\x02\x03",

            "#0102F推理过程严丝合缝，\x01",
            "而且就目前情况来看，也相当具有说服力。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        (
            "#6P#0202F……搜查官的资格证\x01",
            "果然不是摆设呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#0004F#5P哈哈……谢谢夸奖。\x02\x03",

            "#0000F──那么，接下来。\x02\x03",

            "我们就去把这些推理……传达给\x01",
            "那两人如何呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0215
    ChrTalk(
        0x102,
        "#12P#0105F那两个人……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        "#6P#0305F喂喂，难道是……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#0003F#5P没错……\x02\x03",

            "就是瓦鲁多·瓦雷斯\x01",
            "和瓦吉·赫米斯菲亚──\x02\x03",

            "#0000F『剑蛇帮』与\x01",
            "『圣书会』的两个首领。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
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
    SetScenarioFlags(0x43, 2)
    SetScenarioFlags(0x5C, 0)
    NewScene("c000B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_5D00 end

    def Function_19_789C(): pass

    label("Function_19_789C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0218
    ChrTalk(
        0x101,
        "#11P#0006F……科长来得好慢啊。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0219
    ChrTalk(
        0x101,
        (
            "#5P#0001F差不多也该开始早晨的\x01",
            "临时会议了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    #C0220
    ChrTalk(
        0x102,
        (
            "#0106F再怎么说，也不能把科长\x01",
            "排除在外，直接就开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0221
    ChrTalk(
        0x104,
        (
            "#6P#0303F嗯～既然如此，\x01",
            "我不如再去睡个回笼觉吧。\x02\x03",

            "#0302F一直睡到中午之后再起来，\x01",
            "然后去『巴鲁卡』之类的地方玩玩。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0222
    ChrTalk(
        0x103,
        "#5P#0211F真是典型的游手好闲者呢……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 6000, 850, 10200, 90)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)

    #N0223
    NpcTalk(
        0x8,
        "男人的声音",
        "#2P……我迟到了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    OP_68(3000, 1850, 10200, 2000)
    SetChrPos(0x8, 3000, 850, 10200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x1)
    OP_6F(0x1)

    def lambda_7BAD():
        OP_96(0xFE, 0x3138, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7BAD)
    Sleep(3000)
    Fade(500)
    OP_68(12600, 1850, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0224
    ChrTalk(
        0x101,
        (
            "#2P#0000F──科长，\x01",
            "早上好。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#4P#0100F早上好，\x01",
            "我们立刻开始临时会议吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "#5P#1003F不，没那个必要。\x02\x03",

            "#1000F刚才总部发来了联络。\x02\x03",

            "今天要你们去执行\x01",
            "一项特别任务。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0227
    ChrTalk(
        0x101,
        "#2P#0005F特别任务……？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x104,
        "#6P#0301F听起来好像很可疑啊……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x103,
        (
            "#6P#0200F……还是像上次\x01",
            "那样的任务吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "#5P#1004F很遗憾，我也不清楚。\x02\x03",

            "#1002F先去警察局总部吧，\x01",
            "应该有客人在那里等你们。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_789C end

    def Function_20_7E43(): pass

    label("Function_20_7E43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    ClearChrFlags(0x18, 0x80)
    OP_78(0xB, 0x18)
    ClearMapObjFlags(0xB, 0x4)
    OP_49()
    SetChrPos(0x18, 12700, 1650, 5300, 0)
    OP_D3(0x18, 0x0, 0x15F90, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    Sleep(500)
    Sound(18, 0, 100, 0)
    UseItem(0x2D4, 0xFF)
    Sleep(500)
    PlayBGM("ed7110", 0)
    SetCameraDistance(25000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0231
    ChrTalk(
        0x101,
        "#0001F#5P这是……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        (
            "#0103F#11P真的是在各地都发生了呢……\x02\x03",

            "#0101F但媒体方面却几乎\x01",
            "没有任何报道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x104,
        (
            "#6P#0303F嗯……原来如此啊。\x02\x03",

            "#0301F看起来，这好像并不是\x01",
            "普通的魔兽侵害事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x103,
        (
            "#6P#0200F狼形魔兽……\x01",
            "好像是克洛斯贝尔的特有品种吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#5P#0003F这还真是不太清楚……\x02\x03",

            "#0001F不过，在受害地点\x01",
            "似乎有清晰的\x01",
            "脚印残留。\x02\x03",

            "应该可以确定那种魔兽是真实存在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#0101F#11P不过，警备队在搜索之后，\x01",
            "好像还没有正式确认其存在吧？\x02\x03",

            "这个稍微让人有些在意呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x104,
        (
            "#6P#0306F嗯……还会隐藏行踪，\x01",
            "看来是种相当狡猾的魔兽呢。\x02\x03",

            "#0301F这种时候，是不是该雇个\x01",
            "经验丰富的猎人比较好啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        (
            "#6P#0203F……是啊。\x02\x03",

            "#0200F就算我们几个出动，\x01",
            "大概也不会有什么收获吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0239
    ChrTalk(
        0x102,
        "#0105F#11P罗伊德，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#6P#0300F怎么了？\x01",
            "又突然想到什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#5P#0004F与其说是突然想到……\x02\x03",

            "#0000F其实我一直在考虑，如果以『办案』的视角\x01",
            "来对此次的魔兽侵害事件进行调查，\x01",
            "应该能发现一些关键点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x102,
        "#0105F#11P以『办案』的视角……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x103,
        "#6P#0205F来调查魔兽侵害事件……？\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#5P#0000F比如说，如果将这一连串的魔兽侵害事件\x01",
            "当作『案件』来看待……\x02\x03",

            "那么在这种场合下，『犯人』会是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        (
            "#6P#0300F那肯定是报告中提到的\x01",
            "那些狼形魔兽吧。\x02\x03",

            "而且好像并不只是一只，\x01",
            "而是成群结队地行动的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#5P#0003F那就继续说下一个问题……\x02\x03",

            "#0001F那个『犯人』的『身份』\x01",
            "与『动机』，你们怎么看？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x104,
        "#6P#0305F那个……\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0104F#11P……原来如此。\x02\x03",

            "#0100F只看调查报告书的话，\x01",
            "是无法掌握到这些的，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯，既然是高智慧魔兽，\x01",
            "通常情况下，应该会生活在远离人类的地方。\x02\x03",

            "如果动机仅仅是因为饥饿，\x01",
            "那医院方面的受害报告就完全解释不通了。\x02\x03",

            "#0000F如此一来，总会存在某种可以让这\x01",
            "一切谜团都得到合理解释的『真相』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        "#6P#0300F嗯……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x103,
        (
            "#6P#0204F确实……\x01",
            "从理论上说，确实如此呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#0100F#11P这样一来，调查方针\x01",
            "就已经决定了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯……\x01",
            "总之，我们先去受害场所，\x01",
            "询问一下相关人员吧。\x02\x03",

            "#0000F再怎么说，以我们的方式\x01",
            "至少能给出一个最低限度的成果，\x01",
            "也就是将调查报告书补充完整。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        (
            "#0104F#11P是啊……\x02\x03",

            "#0100F哪怕只是一点点也好，只要能对警备队的\x01",
            "工作起到帮助，也就不算是白费力气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#6P#0309F呼～得救了。\x02\x03",

            "还好不用漫无目的地\x01",
            "跑到荒山里去抓捕魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        (
            "#6P#0203F那么，罗伊德前辈。\x02\x03",

            "#0200F如果要进行询问的话……\x01",
            "首先要从哪个地方开始问起呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0257
    ChrTalk(
        0x101,
        "#11P#0005F这个嘛……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0258
    ChrTalk(
        0x101,
        (
            "#11P#0000F那就先去最初遭到侵害的\x01",
            "阿尔摩利卡村看看吧。\x02\x03",

            "那里的受害情况报告是最具体的……\x01",
            "如果能在那里掌握到一点\x01",
            "魔兽的特征，就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        (
            "#0104F#11P原来如此……\x01",
            "这个提议好像不错呢。\x02\x03",

            "#0100F那个，要去阿尔摩利卡村，\x01",
            "应该是从城市的东北方向出发吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0260
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，从东出口出去，\x01",
            "然后乘坐导力巴士就可以了。\x02\x03",

            "#0003F而且……\x01",
            "这是我们的第一次市外行动。\x02\x03",

            "#0001F还不知道将会在目的地遇到何种情况。\x01",
            "先做好充分准备再出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        "#6P#0300F说得对。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        (
            "#6P#0202F谨慎起见，最好也先查看\x01",
            "一下其它的支援请求。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
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
    SetChrPos(0x18, 25600, 1650, 9500, 0)
    SetChrFlags(0x18, 0x80)
    SetMapObjFlags(0xB, 0x4)
    SetScenarioFlags(0x60, 0)
    OP_65(0x1, 0x1)
    OP_29(0x3E, 0x1, 0x9)
    OP_29(0x3F, 0x4, 0x2)
    OP_29(0x3F, 0x1, 0x0)
    PlayBGM("ed7100", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_20_7E43 end

    def Function_21_8BC0(): pass

    label("Function_21_8BC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("apl/ch50106.itc", 0x22)
    LoadChrToIndex("apl/ch50107.itc", 0x23)
    LoadChrToIndex("apl/ch50108.itc", 0x24)
    LoadChrToIndex("apl/ch50109.itc", 0x25)
    LoadChrToIndex("apl/ch50117.itc", 0x26)
    LoadChrToIndex("apl/ch50092.itc", 0x27)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis020.itp")
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    LoadEffect(0x0, "event\\eva05_00.eff")
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 3000, 450, 126000, 180)
    SetChrChipByIndex(0x19, 0x27)
    SetChrSubChip(0x19, 0x12)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2800, 850, 128500, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0x10, 0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少年的声音")

    #A0263
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W等、等一下啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7515", 0)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(800)
    SetMessageWindowPos(50, 170, -1, -1)

    #A0264
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "说什么要出趟远门……\x01",
            "这也太突然了吧。\x02\x03",

            "你究竟要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "雷米菲利亚公国。\x02\x03",

            "不过呢，虽说是出趟『远门』，\x01",
            "大概也只要两个月左右就能回来了吧。\x02\x03",

            "如果情况顺利，也许\x01",
            "不到半个月就能回来了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0266
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "这、这我知道，可是……\x02\x03",

            "哥哥好歹也是\x01",
            "警察局的搜查官吧？\x02\x03",

            "花那么长的时间去旅行，\x01",
            "真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "噢，怎么啦～\x02\x03",

            "哥哥不在家，\x01",
            "你就那么寂寞吗～？\x02\x03",

            "真是的，小罗伊德原来是个\x01",
            "这么离不开人的孩子吗～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0268
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "……我说，你别只出去两个月，\x01",
            "干脆去旅行两年怎么样？\x02\x03",

            "就算那样，我一个人也完全没问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "抱歉抱歉，是我玩笑开过头了。\x02\x03",

            "其实呢……\x01",
            "我这次出行，是有很重要的理由的。\x02\x03",

            "也就是所谓的绝秘任务啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0270
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "实在是很可疑啊。\x02\x03",

            "顺便问一下，\x01",
            "是什么样的绝密任务啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "噢噢，问得好。\x02\x03",

            "其实……\x01",
            "我要护送一位特别可爱的女孩，\x01",
            "和她一起去旅行啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0272
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "是吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "我要带着那个女孩，\x01",
            "逃亡到美丽的北国——雷米菲利亚。\x02\x03",

            "怎么样啊，很羡慕吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0274
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "算啦，玩笑就开到这里吧。\x02\x03",

            "我不在的这段日子，你的晚饭\x01",
            "问题就去拜托邻居帮忙吧。\x02\x03",

            "早饭和午饭的话，自己应该就能解决了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0276
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "那个，吃饭问题倒是无所谓啦，\x01",
            "我自己就完全可以……\x02\x03",

            "──不对，重点不是这个啦！\x02\x03",

            "可爱的女孩……\x01",
            "你究竟打算做什么啊！？\x02\x03",

            "这种事情，要是被塞茜尔姐姐\x01",
            "知道的话怎么办啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "嘿……\x02\x03",

            "这和塞茜尔有什么关系啊，\x01",
            "为什么要在这里提她的名字啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0278
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "你还问为什么……啊啊，真是受不了！！\x02\x03",

            "（塞茜尔姐姐为何\x01",
            "  会对如此迟钝的白痴大哥……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "？？？\x02\x03",

            "说起来的话，这件事情\x01",
            "我早就已经和塞茜尔说过了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    #A0280
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("青年")

    #A0281
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "嗯～但她好像产生了\x01",
            "一些奇怪的误解呢。\x02\x03",

            "虽说是旅行，\x01",
            "但也算是警察的出差工作吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0xBB8, 0x0)

    #A0282
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#40W#30A而且那个孩子…#1000W…#20W \x01",
            "#50W才只有…#400W…#100W岁而已啊…#300W…\x07\x00\x02",
        )
    )
    #Auto

    Sleep(3500)
    OP_57(0x0)
    OP_5A()
    OP_CA(0x0, 0x0, 0x3)
    StopBGM(0xFA0)
    WaitBGM()
    SoundLoad(806)
    Sound(829, 0, 100, 0)
    Sleep(2000)
    SetCameraDistance(23500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0283
    ChrTalk(
        0x101,
        "#5P………嗯…………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    OP_71(0x10, 0x0, 0x14, 0x0, 0x0)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x2)
    Sleep(150)
    SetChrSubChip(0x101, 0x3)
    Sleep(1000)
    SetChrSubChip(0x101, 0x4)
    Sleep(150)
    SetChrSubChip(0x101, 0x5)
    Sleep(1000)
    OP_79(0x10)
    SetChrSubChip(0x101, 0x7)
    Sleep(700)
    SetChrSubChip(0x101, 0x5)
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    Sleep(700)

    #C0284
    ChrTalk(
        0x101,
        (
            "#5206F#5P……是梦吗………\x02\x03",

            "#5208F真怀念啊……\x01",
            "那是什么时候的事情了……\x02\x03",

            "好像是我十二……\x01",
            "不，是十三岁左右时的事情吧？\x02\x03",

            "#5205F说起来，我记得在那之后──\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1400, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 125700, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_9648():
        OP_95(0xFE, 1000, 30, 128100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9648)
    WaitChrThread(0x101, 1)

    def lambda_9666():
        OP_95(0xFE, 1700, 30, 128100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9666)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x1, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0285
    AnonymousTalk(
        0x101,
        "#5201F你好，我是罗伊德。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7111", 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "噢，起来了吗？\x02\x03",

            "调查报告书\x01",
            "已经整理好了吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0287
    AnonymousTalk(
        0x101,
        (
            "#5205F啊，是的。\x02\x03",

            "#5200F关于昨天的调查，\x01",
            "已经全部整理过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那就可以了。\x02\x03",

            "赶快收拾准备一下，\x01",
            "然后都来科长室。\x02\x03",

            "有客人在等你们。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0289
    AnonymousTalk(
        0x101,
        "#5201F！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x1, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(63800, 1000, 7900, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 62900, 0, 7900, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 64599, 0, 7900, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 65600, 0, 7400, 270)
    SetChrPos(0x101, 59000, -1000, 3000, 90)
    SetChrPos(0x102, 59000, 0, 3400, 90)
    SetChrPos(0x103, 59000, 0, 3400, 90)
    SetChrPos(0x104, 59000, 0, 3400, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0290
    ChrTalk(
        0x101,
        "#11P──打扰了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(64080, 1000, 7060, 4000)
    SetCameraDistance(22500, 4000)

    def lambda_99BA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_99BA)

    def lambda_99C7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_99C7)

    def lambda_99D4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_99D4)
    Sound(103, 0, 100, 0)
    Sleep(200)
    SetChrPos(0x101, 59000, 0, 3400, 90)
    BeginChrThread(0x101, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x101, 3)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    OP_6F(0x11)

    #C0291
    ChrTalk(
        0x101,
        "#0005F#12P索妮亚副司令……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        "#0300F#12P果然猜中了啊。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x13,
        "#5P#2002F#5P呵呵，早安。\x02",
    )

    CloseMessageWindow()

    #N0294
    NpcTalk(
        0x14,
        "女性队员",
        "#5P#0502F大家辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#6P#0104F早上好。\x02\x03",

            "#0102F科长所说的客人\x01",
            "果然就是副司令啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "#5P#1002F#5P嗯，她们也是\x01",
            "刚刚才到的。\x02\x03",

            "好像是想问问你们的\x01",
            "调查情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#12P#0000F那倒是没问题……\x01",
            "不过，看起来好像很紧急啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#6P#0105F矿山镇那边的调查工作\x01",
            "还没有完成呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x13,
        (
            "#5P#2006F不好意思哦，原本\x01",
            "也没打算要这么急的……\x02\x03",

            "不过，我们那边的状况\x01",
            "稍微发生了一些变故呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        "#0305F#12P状况发生变故……？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x13,
        (
            "#5P#2001F事实上，截止到昨天为止，\x01",
            "我们都在矿山镇那边进行警备\x01",
            "与巡逻工作……\x02\x03",

            "可是，就在今天早上，\x01",
            "却全都撤退回去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0302
    ChrTalk(
        0x101,
        "#12P#0001F警备队撤退了……？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x103,
        (
            "#12P#0201F魔兽出现在矿山镇，\x01",
            "应该是三天前的事情吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x13,
        (
            "#5P#2003F嗯，按照我们原本的计划，\x01",
            "至少也要将警备工作持续\x01",
            "一周左右的……\x02\x03",

            "#2001F可是，警备队司令下达了指示。\x01",
            "说什么不要再做毫无意义的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#6P#0101F怎、怎么会毫无意义……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#0308F#12P嘁……\x01",
            "那个只会阿谀奉承的大叔……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9E96():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E96)
    Sleep(50)

    def lambda_9EA6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9EA6)
    Sleep(50)
    TurnDirection(0x103, 0x104, 500)

    #C0307
    ChrTalk(
        0x101,
        "#5P#0005F兰迪，你认识他吗？\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#0303F#12P我在贝尔加德门任职的时候，\x01",
            "见过他无数次呢。\x02\x03",

            "#0301F虽说身为警备队的领头人物，\x01",
            "但似乎与帝国派议员中的一些\x01",
            "权贵人物有着很深的瓜葛。\x02\x03",

            "根本就不干什么实事，\x01",
            "好像一天到晚都在接待应酬。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x102,
        (
            "#6P#0108F虽然早就听过传闻……\x01",
            "但没想到他还真是这种人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        (
            "#6P#0201F不过，如果对魔兽侵害事件\x01",
            "放任不管的话，\x01",
            "恐怕还会出现更严重的问题吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x13,
        (
            "#5P#2003F嗯……正如你所说。\x02\x03",

            "#2001F如果只是局部地区遭受侵害的话，\x01",
            "以最坏的事态来说，也可以委托\x01",
            "游击士协会解决……\x02\x03",

            "但这次的受害范围实在是太大了。\x02\x03",

            "身为警备队的成员，我们无论如何\x01",
            "也不能再继续坐视下去了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A105():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A105)

    def lambda_A112():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A112)

    def lambda_A11F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A11F)
    WaitChrThread(0x103, 2)
    Sleep(300)

    #N0312
    NpcTalk(
        0x14,
        "女性队员",
        (
            "#5P#0506F──问题是，\x01",
            "都已经过去三周了，但魔兽的\x01",
            "来历却仍然未能查明……\x02\x03",

            "而且，虽然受害范围很广，\x01",
            "但实际的受害状况却并不是\x01",
            "非常严重……\x02\x03",

            "#0501F基于这种理由，司令阁下\x01",
            "便下达了终止警备工作的命令。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#12P#0001F原来如此啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x13,
        (
            "#5P#2005F啊，话说回来，\x01",
            "还没给你们做过介绍呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)

    def lambda_A272():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A272)

    def lambda_A27F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A27F)

    def lambda_A28C():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A28C)
    Sleep(300)

    #C0315
    ChrTalk(
        0x13,
        (
            "#5P#2004F──这位是诺艾尔上士。\x02\x03",

            "#2002F虽然还很年轻，但战斗能力\x01",
            "和驾驶技术都相当优秀呢。\x02\x03",

            "目前正在担任我的\x01",
            "护卫与支援工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Sound(1493, 255, 100, 0)    #voice#Noel
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1100)
    SetChrName("女性队员")

    #A0316
    AnonymousTalk(
        0xFF,
        (
            "我是诺艾尔·希卡。\x01",
            "再次问候，今后请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0317
    ChrTalk(
        0x101,
        (
            "#12P#0000F彼此彼此……\x01",
            "请多多指教了。\x02",
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
    Sleep(1000)

    #C0318
    ChrTalk(
        0x101,
        "#12P#0005F哎，希卡……\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        (
            "#6P#0100F莫非，是警察局总部\x01",
            "接待员芙兰小姐的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x14,
        (
            "#5P#0509F嗯，我是她的姐姐。\x02\x03",

            "#0502F听说我妹妹一直\x01",
            "承蒙各位的关照呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#12P#0002F哈哈，哪里，应该说是\x01",
            "我们一直在给她添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x104,
        (
            "#0304F#12P不过，原来如此……\x01",
            "你就是诺艾尔上士啊。\x02\x03",

            "#0300F我听说过你哦。\x01",
            "唐古拉姆门的女性队员，\x01",
            "倍受期待的希望之星啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    OP_0D()
    TurnDirection(0x14, 0x104, 500)
    Sleep(300)

    #C0323
    ChrTalk(
        0x14,
        (
            "#5P#0504F呵呵，我也久闻\x01",
            "兰迪前辈的大名了。\x02\x03",

            "#0500F我听说过各种各样关于你的传闻……\x01",
            "一直都希望能见上一面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        "#0309F#12P哈哈，这可真是让我倍感光荣啊。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        "#6P#0005F各种各样的传闻……？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        "#6P#0211F肯定是女性关系方面的吧？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        (
            "#0304F#12P没错没错，因为我受到\x01",
            "大量女性队员的爱慕，\x01",
            "而男人们也只能向我投来羡慕的目光……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(300)

    #C0328
    ChrTalk(
        0x13,
        (
            "#5P#2004F#5P好了，社交辞令\x01",
            "差不多就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x104,
        "#0306F#12P（唔）……\x02",
    )

    CloseMessageWindow()

    def lambda_A76C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A76C)
    Sleep(50)

    def lambda_A77C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A77C)
    Sleep(50)

    def lambda_A78C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A78C)
    Sleep(50)

    def lambda_A79C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A79C)
    Sleep(50)
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(300)

    #C0330
    ChrTalk(
        0x13,
        (
            "#5P#2001F正如我刚才所说……\x01",
            "目前的状况稍微有些不妙呢。\x02\x03",

            "要说能打破现状的要素，\x01",
            "也就只有你们的调查结果了……\x02\x03",

            "说实话，我只是抱着聊胜于无的心态\x01",
            "到你们这里确认一下情况的。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#12P#0001F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        (
            "#6P#0103F那么，在提交调查报告书的同时，\x01",
            "让我来做个大致的说明吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(64080, 1000, 7060, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    Sleep(1000)
    SetCameraDistance(22500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0333
    ChrTalk(
        0x13,
        "#5P#2005F………………………………\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        "#5P#1003F嗯……原来如此啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x13, 500)
    Sleep(300)

    #C0335
    ChrTalk(
        0x8,
        (
            "#6P#1002F索妮亚，我们科这些小家伙们的\x01",
            "能力怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x13,
        (
            "#5P#2004F……超出期待呢。\x02\x03",

            "『神狼』的传说，\x01",
            "还有魔兽出现在医院楼顶的入侵路线……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 400)
    Sleep(400)

    #C0337
    ChrTalk(
        0x13,
        "#5P#2000F怎么样，诺艾尔？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    #C0338
    ChrTalk(
        0x14,
        (
            "#11P#0506F……老实说，我真是很吃惊。\x02\x03",

            "#0500F不愧是专业的搜查官，\x01",
            "看问题的着眼点果然和常人有所不同呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x13,
        (
            "#5P#2000F与其说是着眼点，\x01",
            "倒不如说是思路不同呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)

    def lambda_AAE2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_AAE2)

    def lambda_AAEF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AAEF)
    Sleep(300)

    #C0340
    ChrTalk(
        0x13,
        (
            "#5P#2004F──嗯，决定了。\x02\x03",

            "#2001F请你们继续进行\x01",
            "矿山镇那边的调查吧。\x02\x03",

            "按照这种势头，说不定\x01",
            "还能发现一些出乎意料的新线索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#12P#0005F嗯，我们也\x01",
            "正有此意……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#0301F#12P但这样一来，\x01",
            "不就等于违反司令大人的那个命令了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x13,
        (
            "#5P#2004F呵呵，他可没说要连委托给\x01",
            "你们的支援请求也一并撤销啊。\x02\x03",

            "#2002F既然都已经发现了魔兽的线索，\x01",
            "在此情况下，自然应该马上采取下一步的行动──\x02\x03",

            "这样的话，应该就没有问题了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x104,
        "#0302F#12P原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        (
            "#6P#0102F呵呵，您还真是\x01",
            "足智多谋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x14,
        (
            "#5P#0503F……而且，\x01",
            "总觉得那些魔兽好像\x01",
            "可以感知到我们的行动。\x02\x03",

            "比起大部队的搜索，\x01",
            "也许还是少数人的行动\x01",
            "更容易探查到对手的破绽吧……\x02\x03",

            "#0500F这也正是我们期待各位的原因哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#12P#0000F原来如此……明白了。\x02\x03",

            "总之，我们接下来就\x01",
            "打算前往矿山镇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x13,
        (
            "#5P#2000F嗯，拜托了。\x02\x03",

            "如果有什么发现，就请与\x01",
            "唐古拉姆门的副司令部联络。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x13, 0x8, 500)
    Sleep(300)

    #C0349
    ChrTalk(
        0x13,
        (
            "#11P#2000F那么，赛尔盖，\x01",
            "那件事情就容后再谈吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x13, 500)

    #C0350
    ChrTalk(
        0x8,
        (
            "#6P#1003F嗯，知道了。\x02\x03",

            "#1000F你可别太过勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x13,
        "#11P#2002F呵呵，这话应该是我对你说。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    #C0352
    ChrTalk(
        0x13,
        "#2000F#5P诺艾尔，我们就先行告辞吧。\x02",
    )

    CloseMessageWindow()
    #Sound(1478, 255, 100, 0)    #voice#Noel

    #N0353
    NpcTalk(
        0x14,
        "女性队员",
        "#0502F#5P是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 500)
    Sleep(300)
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    OP_0D()
    Sound(1498, 255, 100, 0)    #voice#Noel
    Sleep(1000)

    def lambda_AF53():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_AF53)
    Sleep(150)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    OP_93(0x14, 0xE1, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(750)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)

    def lambda_AFA0():

        label("loc_AFA0")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_AFA0")

    QueueWorkItem2(0x8, 2, lambda_AFA0)
    BeginChrThread(0x13, 3, 0, 22)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 22)
    Sleep(300)

    def lambda_AFC4():

        label("loc_AFC4")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_AFC4")

    QueueWorkItem2(0x101, 2, lambda_AFC4)

    def lambda_AFD6():

        label("loc_AFD6")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_AFD6")

    QueueWorkItem2(0x102, 2, lambda_AFD6)

    def lambda_AFE8():

        label("loc_AFE8")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_AFE8")

    QueueWorkItem2(0x103, 2, lambda_AFE8)

    def lambda_AFFA():

        label("loc_AFFA")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_AFFA")

    QueueWorkItem2(0x104, 2, lambda_AFFA)
    Sleep(2700)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    StopBGM(0xBB8)
    OP_6F(0x1)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    Sleep(200)
    Sound(104, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7110", 0)

    #C0354
    ChrTalk(
        0x101,
        "#5P#0001F好像很忙啊……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        (
            "#5P#0103F是啊……警备队好像是今天早上\x01",
            "才刚从矿山镇撤出的。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#5P#1003F嗯，看来是被无能的上司\x01",
            "折腾了一趟呢。\x02\x03",

            "#1000F而且，对共和国那边的警戒\x01",
            "工作也不能掉以轻心……\x02\x03",

            "她还是那么倒霉，抽到了下下签呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B147():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B147)
    Sleep(50)

    def lambda_B157():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B157)
    Sleep(50)

    def lambda_B167():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B167)
    Sleep(50)

    def lambda_B177():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B177)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0357
    ChrTalk(
        0x101,
        (
            "#11P#0003F原来如此……\x02\x03",

            "#0005F对了，科长您和\x01",
            "副司令很熟吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x103,
        (
            "#12P#0200F相互之间还轻松随意地\x01",
            "直呼对方的名字……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x104,
        (
            "#0303F说起来，把我\x01",
            "推荐到这里的人\x01",
            "就是副司令哦。\x02\x03",

            "#0302F你们到底是什么关系啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0360
    ChrTalk(
        0x8,
        "#5P#1003F呵，可以说是老交情了吧。\x02",
    )

    CloseMessageWindow()
    Sound(852, 0, 100, 0)
    Sleep(1200)
    PlayEffect(0x0, 0x0, 0x8, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0361
    ChrTalk(
        0x8,
        (
            "#5P#1003F呼～……\x02\x03",

            "#1002F先不说这些，你们几个\x01",
            "昨天好像很辛苦啊。\x02\x03",

            "看来今天还要去矿山镇啊，\x01",
            "又打算步行去吗？\x02",
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

    #C0362
    ChrTalk(
        0x101,
        (
            "#11P#0006F不，昨天那只是因为\x01",
            "重重偶然而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#12P#0100F再怎么说，今天\x01",
            "也得坐巴士去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#5P#1005F什么嘛，原来只是这样啊？\x02\x03",

            "#1004F哼哼，本来还以为\x01",
            "你们肯定是在效仿游击士呢。\x02",
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
    Sleep(1000)

    #C0365
    ChrTalk(
        0x103,
        "#12P#0205F效仿游击士……？\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x104,
        "#0305F什么意思呢？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#5P#1002F据说这是他们的习惯……\x01",
            "在正式开始工作之前，首先要徒步\x01",
            "在周边地区转一圈。\x02\x03",

            "#1004F既能增强耐力，\x01",
            "又能积累与魔兽实战的经验，\x01",
            "最重要的是可以勘察一遍地形……\x02\x03",

            "#1002F正所谓一举三得呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        "#11P#0001F徒步勘察周边地区……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x104,
        (
            "#0301F原来如此……\x01",
            "他们还会这样做啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#12P#0201F莫非，我们昨天遇到的\x01",
            "艾丝蒂尔他们也是……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#12P#0103F……说不定正是打算\x01",
            "徒步走遍这一带呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        (
            "#5P#1002F呵呵，那两个人啊……\x01",
            "好像有过相当不得了的经历呢。\x02\x03",

            "在解决去年发生的那起\x01",
            "利贝尔异变事件中，\x01",
            "他们也做出了重要贡献呢。\x02",
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

    #C0373
    ChrTalk(
        0x101,
        "#11P#0001F利贝尔的异变……！\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        (
            "#12P#0205F是那件……整个王国的\x01",
            "导力全部停滞的……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x104,
        "#0301F喂喂，真的假的啊……？\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        (
            "#12P#0106F如果那是真的……\x01",
            "也就不难理解他们为什么拥有那么强的实力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#5P#1002F呵，但在克洛斯贝尔的话，\x01",
            "他们可是比你们还要新的新人啊。\x02\x03",

            "如果不希望在转瞬之间就被追上，\x01",
            "并被他们远远抛在后面的话，\x01",
            "可就要拼命努力了。\x02\x03",

            "#1003F这次的事件也是一样，如果拖得太久，\x01",
            "游击士协会那边恐怕就会出动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            "#11P#0003F……明白了，\x01",
            "我们会努力将事件解决的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B92D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B92D)
    Sleep(150)

    def lambda_B93D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B93D)
    Sleep(50)

    def lambda_B94D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B94D)
    Sleep(50)

    def lambda_B95D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B95D)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0379
    ChrTalk(
        0x101,
        (
            "#5P#0001F那么，各位，\x01",
            "我们这就向矿山镇出发吧。\x02\x03",

            "首先应该去的地方是\x01",
            "城市北出口的巴士站。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        (
            "#6P#0101F要是有什么补给品已经用完，\x01",
            "可以先到街上补充一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x103,
        (
            "#6P#0203F谨慎起见，最好\x01",
            "也检查一下终端上的信息。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#0300F#12P哈，总之我们就一步一步地耐心来吧。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22750, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    StopEffect(0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_66(0x3, 0x1)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_68(64000, 1330, 6000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 64000, 0, 6000, 0)
    SetChrPos(0x1, 64000, 0, 6000, 0)
    SetChrPos(0x2, 64000, 0, 6000, 0)
    SetChrPos(0x3, 64000, 0, 6000, 0)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0x10, 0x4)
    SetScenarioFlags(0x64, 1)
    OP_29(0x40, 0x4, 0x2)
    OP_29(0x40, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB6A")
    OP_29(0x8, 0x4, 0x40)
    Jump("loc_BB7C")

    label("loc_BB6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7C")
    OP_29(0x8, 0x4, 0x40)

    label("loc_BB7C")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7103")
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_21_8BC0 end

    def Function_22_BB98(): pass

    label("Function_22_BB98")

    OP_92(0xFE, 0xF8D4, 0x1B58, 0x1F4)

    def lambda_BBAA():
        OP_95(0xFE, 63700, 0, 7300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBAA)
    WaitChrThread(0xFE, 1)

    def lambda_BBC8():
        OP_95(0xFE, 61600, 0, 6100, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBC8)
    WaitChrThread(0xFE, 1)

    def lambda_BBE6():
        OP_95(0xFE, 61600, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBE6)
    WaitChrThread(0xFE, 1)

    def lambda_BC04():
        OP_95(0xFE, 59000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC04)
    Sleep(500)

    def lambda_BC21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BC21)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_BB98 end

    def Function_23_BC36(): pass

    label("Function_23_BC36")


    def lambda_BC3B():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC3B)

    def lambda_BC55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC55)
    WaitChrThread(0x101, 1)

    def lambda_BC6A():
        OP_95(0xFE, 64099, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC6A)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_23_BC36 end

    def Function_24_BC8B(): pass

    label("Function_24_BC8B")


    def lambda_BC90():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BC90)

    def lambda_BCAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BCAA)
    WaitChrThread(0x102, 1)

    def lambda_BCBF():
        OP_95(0xFE, 62800, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BCBF)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_24_BC8B end

    def Function_25_BCE0(): pass

    label("Function_25_BCE0")


    def lambda_BCE5():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BCE5)

    def lambda_BCFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BCFF)
    WaitChrThread(0x103, 1)

    def lambda_BD14():
        OP_95(0xFE, 62800, 30, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BD14)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_25_BCE0 end

    def Function_26_BD35(): pass

    label("Function_26_BD35")


    def lambda_BD3A():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BD3A)

    def lambda_BD54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BD54)
    WaitChrThread(0x104, 1)

    def lambda_BD69():
        OP_95(0xFE, 64099, 30, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BD69)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_26_BD35 end

    def Function_27_BD8A(): pass

    label("Function_27_BD8A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02607.itc", 0x1E)
    LoadChrToIndex("chr/ch02608.itc", 0x1F)
    LoadChrToIndex("apl/ch50116.itc", 0x20)
    OP_68(900, 700, 6200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 800, 0, 500, 0)
    SetChrPos(0x102, 800, 0, 500, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 900, 0, 6200, 180)
    BeginChrThread(0xC, 3, 0, 0)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 800, 0, 0, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis153.itp")
    SetCameraDistance(24500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(900, 700, 5200, 2000)
    SetCameraDistance(25500, 2000)

    def lambda_BF6E():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF6E)

    def lambda_BF88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF88)
    Sleep(250)

    def lambda_BF9C():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BF9C)

    def lambda_BFB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BFB6)
    Sleep(400)

    def lambda_BFCA():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BFCA)

    def lambda_BFE4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BFE4)
    Sleep(250)

    def lambda_BFF8():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BFF8)

    def lambda_C012():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C012)
    WaitChrThread(0x101, 1)
    Sleep(500)
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0383
    ChrTalk(
        0x101,
        "#12P#0011F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x102,
        "#0105F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x104,
        "#0307F哈！？\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x103,
        "#4P#0205F为什么……\x02",
    )

    CloseMessageWindow()

    def lambda_C104():
        OP_95(0xFE, 800, 0, 600, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C104)

    def lambda_C11E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C11E)
    WaitChrThread(0x8, 1)

    def lambda_C133():
        OP_95(0xFE, 2850, 0, 2000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C133)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    #C0387
    ChrTalk(
        0x8,
        (
            "#1011F#11P果然和你们认识吗？\x02\x03",

            "#1001F哎，它突然就闯了进来，\x01",
            "我想都没想就直接拔出了枪……\x02\x03",

            "但它却毫不在意，\x01",
            "直接就到那里睡起来了，\x01",
            "这样的话，我实在是没法出手啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C200():
        OP_95(0xFE, -900, 0, 3000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C200)
    WaitChrThread(0x103, 1)
    OP_68(1470, 700, 5610, 1000)

    def lambda_C22F():
        OP_95(0xFE, 600, 0, 4500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C22F)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0388
    ChrTalk(
        0x103,
        (
            "#11P#0205F你怎么了……？\x02\x03",

            "为什么会来这种地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xC, 0x3)
    Fade(250)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)
    #Sound(2053, 255, 100, 0)    #voice#Zeit
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("白狼")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            "#30W呜噜噜噜……\x02\x03",

            "呜噜噜噜噜噜噜……\x02",
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
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0390
    ChrTalk(
        0x103,
        "#11P#0202F啊……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#12P#0005F……缇欧。\x01",
            "它在说什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    #C0392
    ChrTalk(
        0x103,
        (
            "#0204F#5P……那个。\x02\x03",

            "#0202F『我的名字是蔡特。』\x02\x03",

            "『各位替我们洗刷了冤屈，\x01",
            "  辛苦了。』\x02\x03",

            "#0204F──就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#12P#0002F『蔡特』……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        "#0102F是、是来道谢的吗……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x104,
        (
            "#0309F不、不管怎么说，\x01",
            "还真是个傲气十足的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xC,
        (
            "#5414F#5P#30W呜噜噜噜噜噜噜……\x02\x03",

            "呜噜噜噜噜噜噜噜噜……\x02\x03",

            "#5413F呜噜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)

    #C0397
    ChrTalk(
        0x103,
        "#11P#0205F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        "#12P#0001F怎、怎么了？\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    #C0399
    ChrTalk(
        0x103,
        (
            "#0208F那个……\x02\x03",

            "#0203F『但你们还太年轻，\x01",
            "  实在是靠不住……』\x02\x03",

            "『没办法，我只能暂时\x01",
            "  助你们一臂之力了。』\x02\x03",

            "『心情好时，我会帮助你们的。』\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0400
    ChrTalk(
        0x101,
        "#12P#0011F什么！？\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#0105F哎哎哎哎！？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x104,
        "#0307F喂喂喂喂！\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xC,
        (
            "#5414F#5P#30W呜嗷……\x02\x03",

            "#5412F呜噜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x103,
        (
            "#0204F#5P『不用担心。』\x02\x03",

            "『狼群已经交给部下来指挥了，\x01",
            "  你们尽管放心吧。』\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0405
    ChrTalk(
        0x101,
        (
            "#12P#0012F那个，我们并不是\x01",
            "在担心那种事啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)

    def lambda_C770():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_C770)
    Sound(848, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(1100)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_63(0xC, 0x1F4, 1200, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1600)

    #C0406
    ChrTalk(
        0x8,
        (
            "#1004F#11P呵呵，传说中的『神狼』吗……\x02\x03",

            "#1002F虽然有些奇怪，但看这个样子，\x01",
            "它好像是认准你们了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C8AB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C8AB)
    Sleep(50)

    def lambda_C8BB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C8BB)
    Sleep(50)

    def lambda_C8CB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C8CB)
    Sleep(50)

    def lambda_C8DB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C8DB)
    WaitChrThread(0x104, 2)

    #C0407
    ChrTalk(
        0x101,
        "#6P#0011F科长……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        (
            "#1002F#11P总之，和上层说是\x01",
            "『警犬』就可以了。\x02\x03",

            "至于今后要怎么和它相处，\x01",
            "就由你们自己来决定吧。\x02\x03",

            "#1004F那我就回去睡啦。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 28)
    Sleep(500)

    def lambda_C988():

        label("loc_C988")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C988")

    QueueWorkItem2(0x101, 2, lambda_C988)

    def lambda_C99A():

        label("loc_C99A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C99A")

    QueueWorkItem2(0x102, 2, lambda_C99A)

    def lambda_C9AC():

        label("loc_C9AC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C9AC")

    QueueWorkItem2(0x103, 2, lambda_C9AC)

    def lambda_C9BE():

        label("loc_C9BE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C9BE")

    QueueWorkItem2(0x104, 2, lambda_C9BE)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0409
    ChrTalk(
        0x101,
        "#12P#0011F等、等一下啊，科长！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    #C0410
    ChrTalk(
        0x104,
        "#0301F这还真是麻烦了啊……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x102,
        "#0106F呼……这么做没问题吗？\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#0204F……我赞成，\x01",
            "因为感觉它非常可靠呢。\x02\x03",

            "#0202F更重要的是，它这柔软的\x01",
            "白色绒毛好有魅力……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x102,
        (
            "#0109F嗯、嗯～……\x01",
            "这个倒是不能否认呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x104,
        (
            "#0302F算啦，可靠的帮手又多了一个。\x01",
            "这样想的话，不是也很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        (
            "#6P#0006F哈……是啊。\x02\x03",

            "#0000F但一直这样下去，情况可能会变得麻烦，\x01",
            "还是先去哪里给它买个项圈吧……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_29(0x3F, 0x4, 0x10)
    OP_29(0x40, 0x4, 0x10)
    OP_29(0x40, 0x4, 0x20)
    SubItemNumber(0x2D4, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC39")
    OP_29(0x5, 0x4, 0x40)
    Jump("loc_CC4B")

    label("loc_CC39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC4B")
    OP_29(0x5, 0x4, 0x40)

    label("loc_CC4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC69")
    OP_29(0x6, 0x4, 0x40)
    Jump("loc_CC7B")

    label("loc_CC69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC7B")
    OP_29(0x6, 0x4, 0x40)

    label("loc_CC7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC9E")
    OP_29(0x7, 0x4, 0x40)
    SubItemNumber(0x35B, 1)
    Jump("loc_CCB0")

    label("loc_CC9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCB0")
    OP_29(0x7, 0x4, 0x40)

    label("loc_CCB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCCE")
    OP_29(0x9, 0x4, 0x40)
    Jump("loc_CCE0")

    label("loc_CCCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCE0")
    OP_29(0x9, 0x4, 0x40)

    label("loc_CCE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCFE")
    OP_29(0xA, 0x4, 0x40)
    Jump("loc_CD10")

    label("loc_CCFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD10")
    OP_29(0xA, 0x4, 0x40)

    label("loc_CD10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xB, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD22")
    OP_29(0xB, 0x4, 0x40)

    label("loc_CD22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD40")
    OP_29(0xC, 0x4, 0x40)
    Jump("loc_CD52")

    label("loc_CD40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD52")
    OP_29(0xC, 0x4, 0x40)

    label("loc_CD52")

    SubItemNumber('铁道爱好者的推荐', 1)
    SubItemNumber('玛尔克与森林深处的魔女·上', 1)
    SubItemNumber('改变大陆的美人们', 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x25, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_BD8A end

    def Function_28_CE30(): pass

    label("Function_28_CE30")

    ClearChrFlags(0x8, 0x4)

    def lambda_CE3A():
        OP_95(0xFE, 2600, 850, 9000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE3A)
    WaitChrThread(0x8, 1)

    def lambda_CE58():
        OP_95(0xFE, 1300, 850, 10300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE58)
    WaitChrThread(0x8, 1)

    def lambda_CE76():
        OP_95(0xFE, 1300, 2650, 13800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE76)
    Sleep(1500)

    def lambda_CE93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CE93)
    WaitChrThread(0x8, 1)
    Return()

    # Function_28_CE30 end

    def Function_29_CEA4(): pass

    label("Function_29_CEA4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("apl/ch50092.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis113.itp")
    OP_68(500, 1100, 2500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 1000, 0, 0, 0)
    SetChrPos(0x102, 11100, 870, 5700, 90)
    SetChrPos(0x103, 12700, 870, 8200, 180)
    SetChrPos(0x104, 1000, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0xA)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0xA)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0xA)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0xA)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x7)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12700, 1400, 5500, 0)
    SetCameraDistance(25000, 2500)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_D0CC():
        OP_96(0xFE, 0x1F4, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0CC)

    def lambda_D0E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D0E6)
    Sleep(700)

    def lambda_D0FA():
        OP_96(0xFE, 0x5DC, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D0FA)

    def lambda_D114():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D114)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    #C0416
    ChrTalk(
        0x101,
        "#0000F#5P我们回来了。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x104,
        "#0300F#11P回来啦～\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)

    #N0418
    NpcTalk(
        0x102,
        "艾莉的声音",
        "#3P啊，你们回来了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D1B6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D1B6)
    Sleep(50)

    def lambda_D1C6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D1C6)
    OP_68(11100, 1950, 5700, 2000)
    MoveCamera(45, 19, 0, 2000)
    OP_6F(0x41)

    #C0419
    ChrTalk(
        0x101,
        (
            "#0005F#2P怎么，\x01",
            "你们先回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#11P#0104F呵呵，因为我们只是在总部\x01",
            "做了一点简单的文件整理啦。\x02\x03",

            "#0102F回来以后，还和缇欧\x01",
            "一起把午餐做好了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        "#0302F#2P噢，也准备了我们的吗？\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)
    Sleep(300)

    #C0422
    ChrTalk(
        0x103,
        (
            "#0202F#5P是的……不过也只是做了简单的\x01",
            "通心粉和沙拉而已，不嫌弃的话请用。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0009F#9P这就足够了，\x01",
            "那我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x102,
        (
            "#11P#0109F呵呵，那你们两个\x01",
            "先去洗手吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    Sleep(500)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0425
    ChrTalk(
        0x103,
        (
            "#6P#0205F对了……\x02\x03",

            "#0200F罗伊德前辈那边的\x01",
            "交通管理工作，做得如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#11P#0006F啊，那工作相当麻烦呢。\x02\x03",

            "#0000F要用人力将那些违章停靠的导力车\x01",
            "都推到墙边。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0427
    ChrTalk(
        0x104,
        (
            "#6P#0300F欢乐街那里有很多车呢。\x02\x03",

            "因为正好是在公演之前，\x01",
            "所以相当热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#0104F#11P说起来……\x01",
            "下个月终于就要公开演出了呢。\x02\x03",

            "#0100F『彩虹剧团』的新剧目。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(200)

    #C0429
    ChrTalk(
        0x104,
        (
            "#6P#0300F是叫『金之太阳、银之月』啊。\x02\x03",

            "#0306F我之前也想去买票的，但不幸的是，\x01",
            "连下个月的票都已经全部卖光了～\x02\x03",

            "最后总算是勉强买到了\x01",
            "下下个月的Ｂ席票。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    #C0430
    ChrTalk(
        0x103,
        (
            "#6P#0205F『彩虹剧团』，\x01",
            "竟然如此受欢迎吗……\x02\x03",

            "#0203F虽然我也知道剧团的\x01",
            "招牌明星伊莉娅·普拉提耶\x01",
            "是个超级名人。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0431
    ChrTalk(
        0x101,
        (
            "#5P#0003F说起来，我虽然\x01",
            "看过彩虹剧团的舞剧……\x02\x03",

            "#0000F但从没欣赏过\x01",
            "伊莉娅·普拉提耶的表演啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0432
    ChrTalk(
        0x104,
        (
            "#6P#0306F哎呀呀，那可真是太令人同情了。\x02\x03",

            "#0301F──这个世界上的人只分为两种。\x02\x03",

            "#0304F欣赏过伊莉娅·普拉提耶之表演的人\x01",
            "与没有欣赏过的人──\x01",
            "ｂｙ兰迪·奥兰多。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        "#5P#0012F这也太夸张了……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0434
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，不过她确实很厉害呢。\x02\x03",

            "#0104F该怎么说才好呢……\x01",
            "只要欣赏过一次她的表演，\x01",
            "仿佛就连灵魂也要被夺去一般……\x02\x03",

            "#0100F如果这个世界上存在着『天才』，\x01",
            "那她毫无疑问就是其中之一了。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#5P#0005F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        (
            "#6P#0202F……稍微有点兴趣了呢。\x02\x03",

            "#0206F不过，我们最近的工作\x01",
            "真是莫名其妙地多呢……\x02\x03",

            "#0200F彩虹剧团的公演也是原因之一吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#0106F那是自然，因为克洛斯贝尔的创立纪念庆典\x01",
            "和彩虹剧团的新剧公开日\x01",
            "正好赶在一起了……\x02\x03",

            "#0100F警察的工作肯定要比\x01",
            "往年都忙得多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x104,
        (
            "#6P#0306F哈，不过丢到咱们这里的工作\x01",
            "全都是一些杂务啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        (
            "#5P#0012F算了算了。\x02\x03",

            "#0000F再怎么说，和最初那时相比，\x01",
            "我们接到的工作已经重要不少了。\x02\x03",

            "克洛斯贝尔时代周刊也不再\x01",
            "写那种讽刺我们的报道了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0440
    ChrTalk(
        0x103,
        (
            "#6P#0203F……不过，现在仍然\x01",
            "还会将我们与游击士做比较呢。\x02\x03",

            "#0211F特别是和……艾丝蒂尔他们……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0441
    ChrTalk(
        0x101,
        (
            "#5P#0006F呼……确实啊。\x02\x03",

            "#0001F他们只有两个人而已，\x01",
            "为什么可以活跃到这种程度呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x102,
        (
            "#0108F因为他们和其他游击士也有合作，\x01",
            "所以工作效率应该会比较高……\x02\x03",

            "#0106F而我们虽然有四个人，\x01",
            "但和其它的部门基本没形成互助关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x104,
        (
            "#6P#0303F不，在我看来，\x01",
            "更关键的是那个叫约修亚的小子。\x02\x03",

            "他为那个莽撞冲动的艾丝蒂尔\x01",
            "提供了非常高效的后方支援工作。\x02\x03",

            "#0301F战斗也好，各种日常工作也好，\x01",
            "两个人的默契程度实在是非同寻常。\x02\x03",

            "再加上，他们的经验相当丰富呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        (
            "#6P#0206F这也就是说，现在的我们\x01",
            "还差得很远吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0445
    ChrTalk(
        0x101,
        (
            "#5P#0012F算、算啦……\x01",
            "我们也已经成长了不少呢。\x02\x03",

            "#0000F而且就在不久前，不是刚有位\x01",
            "可靠的帮手来帮我们吗──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0446
    ChrTalk(
        0x101,
        "#11P#0005F……说起来，蔡特去哪里了？\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x102,
        (
            "#0105F今天都没看见它呢……\x02\x03",

            "#0100F昨天倒是一整天都在楼顶上\x01",
            "晒太阳睡觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x104,
        (
            "#6P#0306F在和魔兽战斗的时候，\x01",
            "它确实是帮了我们不少……\x02\x03",

            "#0300F但平时究竟都在干些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0449
    ChrTalk(
        0x103,
        (
            "#6P#0204F……它的性格非常孤高。\x02\x03",

            "即使想用我们人类的规章制度\x01",
            "去束缚它，也是毫无意义的……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        (
            "#11P#0006F不过，毕竟是作为警犬登记的，\x01",
            "所以希望它至少也能遵守最低限度的规章啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0451
    ChrTalk(
        0x101,
        (
            "#5P#0000F话说回来，最初我还担心\x01",
            "周围的居民们会怕它呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x104,
        (
            "#6P#0302F但没想到它竟然会\x01",
            "在那起车祸中救出了小孩啊。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0xBB8)
    MiniGame(0x17, 0xBB8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(3000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)

    #A0453
    AnonymousTalk(
        0x102,
        (
            "#0103F搬运车的方向盘失灵了，\x01",
            "撞上了路边的围栏……\x02\x03",

            "#0102F当时我还在想是什么声音呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0454
    AnonymousTalk(
        0x101,
        (
            "#0004F慌慌张张地跑到外面一看，\x01",
            "正好看到蔡特把即将被车轮辗过的\x01",
            "隆救下的飒爽之姿……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0455
    AnonymousTalk(
        0x104,
        (
            "#0309F哈哈，如此出色的表现，大概\x01",
            "都能和那位亚里欧斯大叔一较高下了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0456
    AnonymousTalk(
        0x103,
        "#0202F……确实呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    #C0457
    ChrTalk(
        0x102,
        (
            "#0104F呵呵……自那之后，\x01",
            "它在西街就变得特别受欢迎了。\x02\x03",

            "#0102F隆他们好像也\x01",
            "非常喜欢和它亲近呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#5P#0004F哈哈，是啊。\x02\x03",

            "#0000F算啦，也不能太过依赖\x01",
            "蔡特博得的人气……\x02\x03",

            "我们要靠自己努力才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        "#6P#0204F……赞成。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x104,
        (
            "#6P#0300F那么，从下午开始，\x01",
            "我们就来处理支援请求吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0xAC)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0461
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧习得了特殊战技\x01",
            "『神狼召唤』。\x02",
        )
    )

    CloseMessageWindow()

    #A0462
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在战斗中使用此战技，\x01",
            "蔡特就会出现在ＡＴ顺序栏中，\x01",
            "并在相应回合进行支援行动。\x02",
        )
    )

    CloseMessageWindow()

    #A0463
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，根据剧情的进展，\x01",
            "此战技有时也会无法使用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x5A, 2)
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
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, 13820, 850, 9650, 270)
    SetChrPos(0x1, 13820, 850, 9650, 270)
    SetChrPos(0x2, 13820, 850, 9650, 270)
    SetChrPos(0x3, 13820, 850, 9650, 270)
    SetScenarioFlags(0x80, 0)
    OP_29(0x40, 0x1, 0xD)
    OP_29(0x41, 0x4, 0x2)
    OP_29(0x41, 0x1, 0x0)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_29_CEA4 end

    def Function_30_E4E6(): pass

    label("Function_30_E4E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50091.itc", 0x23)
    OP_68(1000, 900, 2800, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 500, 0, 1800, 0)
    SetChrPos(0x102, 1500, 0, 1800, 0)
    SetChrPos(0x103, 500, 0, 700, 0)
    SetChrPos(0x104, 1500, 0, 700, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 3000, 0, 4700, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E63E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E63E)
    Sleep(50)

    def lambda_E64E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E64E)
    Sleep(50)

    def lambda_E65E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E65E)
    Sleep(50)

    def lambda_E66E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E66E)
    WaitChrThread(0x101, 2)

    #C0464
    ChrTalk(
        0x101,
        "#6P#0005F噢……\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x102,
        "#6P#0100F好像已经来了呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)
    #Sound(1635, 255, 100, 0)    #voice#Rixia

    #N0466
    NpcTalk(
        0x15,
        "紫发的女孩",
        "#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(620, 1000, 2850, 1500)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_E718():
        OP_95(0xFE, 880, 0, 4250, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E718)

    def lambda_E732():

        label("loc_E732")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_E732")

    QueueWorkItem2(0x101, 2, lambda_E732)

    def lambda_E744():

        label("loc_E744")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_E744")

    QueueWorkItem2(0x102, 2, lambda_E744)

    def lambda_E756():

        label("loc_E756")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_E756")

    QueueWorkItem2(0x103, 2, lambda_E756)

    def lambda_E768():

        label("loc_E768")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_E768")

    QueueWorkItem2(0x104, 2, lambda_E768)
    WaitChrThread(0x15, 1)
    TurnDirection(0x15, 0x101, 500)
    OP_6F(0x1)

    #N0467
    NpcTalk(
        0x15,
        "紫发的女孩",
        (
            "#1805F#5P对、对不起……！\x02\x03",

            "#1803F我擅自就进来了。\x01",
            "……那个……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    #C0468
    ChrTalk(
        0x101,
        (
            "#12P#0004F不，没关系的，\x01",
            "我们已经知道你要来了。\x02\x03",

            "#0002F是来找我们商量事情的吧？\x01",
            "欢迎来到特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #N0469
    NpcTalk(
        0x15,
        "紫发的女孩",
        "#1802F#5P哦……\x02",
    )

    CloseMessageWindow()
    #Sound(1636, 255, 100, 0)    #voice#Rixia
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrName("紫发的女孩")

    #A0470
    AnonymousTalk(
        0xFF,
        (
            "那个，我的名字叫莉夏·毛。\x02\x03",

            "非常感谢各位今天\x01",
            "愿意接待我……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    SetMessageWindowPos(14, 80, -1, -1)

    #A0471
    AnonymousTalk(
        0x101,
        "#12P#0005F（哇……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 20, -1, -1)

    #A0472
    AnonymousTalk(
        0x104,
        "#0301F（这、这真是……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0473
    AnonymousTalk(
        0x103,
        "#0205F#12P（身材娇小，内涵丰富呢～……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0474
    AnonymousTalk(
        0x102,
        (
            "#0106F（呼……\x01",
            "  别这么露骨地盯着人家看啊。）\x02\x03",

            "#0111F（──喂，罗伊德？）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 80, -1, -1)

    #A0475
    AnonymousTalk(
        0x101,
        "#12P#0011F（啊……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0476
    ChrTalk(
        0x101,
        (
            "#12P#0003F总、总之，\x01",
            "请到那边就坐吧。\x02\x03",

            "#0000F然后可以请你先把事情大概说明一下吗？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x9C4)
    WaitBGM()
    ClearMapFlags(0x10000000)
    Call(0, 32)
    Return()

    # Function_30_E4E6 end

    def Function_31_EB1E(): pass

    label("Function_31_EB1E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50091.itc", 0x23)
    OP_68(1700, 1200, 7000, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 1900, 850, 9900, 180)
    SetChrPos(0x102, 700, 850, 9900, 180)
    SetChrPos(0x103, 700, 850, 11100, 180)
    SetChrPos(0x104, 1900, 850, 11100, 180)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 2700, 0, 3200, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0477
    ChrTalk(
        0x101,
        "#0005F#6P噢……\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x102,
        "#0100F好像已经来了呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)
    #Sound(1635, 255, 100, 0)    #voice#Rixia

    #N0479
    NpcTalk(
        0x15,
        "紫发的女孩",
        "#2P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(900, 1850, 7450, 1500)
    SetCameraDistance(26000, 1500)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_ED15():
        OP_95(0xFE, 1150, 0, 6330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_ED15)

    def lambda_ED2F():
        OP_96(0xFE, 0x76C, 0x352, 0x20D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED2F)
    Sleep(50)

    def lambda_ED4C():
        OP_96(0xFE, 0x2BC, 0x352, 0x20D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED4C)
    Sleep(100)

    def lambda_ED69():
        OP_96(0xFE, 0x76C, 0x352, 0x2580, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ED69)
    Sleep(50)

    def lambda_ED86():
        OP_96(0xFE, 0x2BC, 0x352, 0x2580, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ED86)
    WaitChrThread(0x15, 1)
    TurnDirection(0x15, 0x101, 500)
    OP_6F(0x1)

    #N0480
    NpcTalk(
        0x15,
        "紫发的女孩",
        (
            "#1805F#2P对、对不起……！\x02\x03",

            "#1806F我擅自就进来了。\x01",
            "……那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        (
            "#5P#0004F不，没关系的，\x01",
            "我们已经知道你要来了。\x02\x03",

            "#0002F是来找我们商量事情的吧？\x01",
            "欢迎来到特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #N0482
    NpcTalk(
        0x15,
        "紫发的女孩",
        "#2P#1802F哦……\x02",
    )

    CloseMessageWindow()
    #Sound(1636, 255, 100, 0)    #voice#Rixia
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrName("紫发的女孩")

    #A0483
    AnonymousTalk(
        0xFF,
        (
            "那个，我的名字叫莉夏·毛。\x02\x03",

            "非常感谢各位今天\x01",
            "愿意接待我……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    SetMessageWindowPos(14, 80, -1, -1)

    #A0484
    AnonymousTalk(
        0x101,
        "#12P#0005F（哇……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 20, -1, -1)

    #A0485
    AnonymousTalk(
        0x104,
        "#0301F（这、这真是……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0486
    AnonymousTalk(
        0x103,
        "#0205F#12P（身材娇小，内涵丰富呢～……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0487
    AnonymousTalk(
        0x102,
        (
            "#0106F（呼……\x01",
            "  别这么露骨地盯着人家看啊。）\x02\x03",

            "#0111F（──喂，罗伊德？）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 80, -1, -1)

    #A0488
    AnonymousTalk(
        0x101,
        "#12P#0011F（啊……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0489
    ChrTalk(
        0x101,
        (
            "#0003F#5P总、总之，\x01",
            "请到那边就坐吧。\x02\x03",

            "#0000F然后可以请你先把事情大概说明一下吗？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x9C4)
    WaitBGM()
    Call(0, 32)
    Return()

    # Function_31_EB1E end

    def Function_32_F12D(): pass

    label("Function_32_F12D")

    FadeToDark(0, 0, -1)
    OP_68(5500, 950, 4300, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 6050, 130, 6250, 180)
    SetChrPos(0x102, 4600, 130, 2200, 0)
    SetChrPos(0x103, 5500, 130, 2200, 0)
    SetChrPos(0x104, 6400, 130, 2200, 0)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 4900, 130, 6250, 180)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x19)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 4900, 280, 4600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x1A)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 5500, 330, 4300, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0490
    AnonymousTalk(
        0x101,
        "#0013F──恐吓信！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(23000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0491
    ChrTalk(
        0x15,
        (
            "#1P#1803F是的……是一周前的事。\x02\x03",

            "伊莉娅小姐收到了\x01",
            "一封寄信人不明的信……\x02\x03",

            "#1805F啊，伊莉娅小姐就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x104,
        (
            "#0303F拥有『炎之舞姬』的称号，\x01",
            "彩虹剧团的超级大明星。\x02\x03",

            "#0301F在国际上都有着极高知名度的\x01",
            "头号女演员，顶级艺术家。\x02\x03",

            "#0309F呀呀～！\x01",
            "真没想到，居然是要商量有关\x01",
            "伊莉娅·普拉提耶的事啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0493
    ChrTalk(
        0x103,
        (
            "#12P#0203F兰迪前辈……\x01",
            "请稍微冷静一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x101,
        (
            "#11P#0003F那个，毕竟是名人，\x01",
            "所以名字我们还是知道的……\x02\x03",

            "#0001F不过……\x01",
            "那恐吓信是发给她的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x15,
        (
            "#1P#1803F是的……虽然她本人\x01",
            "说这只是恶作剧而已……\x02\x03",

            "但总觉得信中的措辞有些诡异……\x01",
            "似乎并不像是普通的恶作剧呢。\x02\x03",

            "#1801F然后，我就和剧团长商量了一下，\x01",
            "最后决定还是找警察来报案。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        "#6P#0101F……那封恐吓信现在在谁手里呢？\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x15,
        (
            "#1P#1806F那个……\x01",
            "在伊莉娅小姐自己手中。\x02\x03",

            "她本打算马上就扔掉的，\x01",
            "但总算是被我们阻止了……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x101,
        (
            "#11P#0003F既然如此，我们首先还是\x01",
            "应该亲眼看看那封恐吓信吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0499
    ChrTalk(
        0x101,
        (
            "#11P#0005F对了……\x01",
            "你是叫莉夏吧。\x02\x03",

            "#0000F想必是『彩虹剧团』\x01",
            "中的工作人员吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    Sleep(300)

    #C0500
    ChrTalk(
        0x15,
        (
            "#1P#1802F啊，是的。\x01",
            "算是剧团的演员吧。\x02\x03",

            "#1809F不过……\x01",
            "我还只是个新人而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0501
    ChrTalk(
        0x104,
        "#0305F#4S哎！！啊啊！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x15, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)

    #C0502
    ChrTalk(
        0x101,
        "#5P#0011F怎、怎么了啊，从刚才开始就一直大呼小叫的。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x104,
        (
            "#0301F我、我在新剧特辑页中\x01",
            "看见过你！\x02\x03",

            "#0303F你是与伊莉娅扮演的『太阳之姬』演\x01",
            "对手戏的，扮演『月之姬』的第二主角……\x02\x03",

            "#0302F由伊莉娅·普拉提耶亲自破格提拔，\x01",
            "如彗星一般突然闪现的超级新人！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0504
    ChrTalk(
        0x15,
        (
            "#1P#1805F没、没那回事，我并不算什么超级新人。\x02\x03",

            "#1806F我的练习还远远不够呢……\x01",
            "总是拖大家的后腿。\x02\x03",

            "#1808F要想正式登台出道，\x01",
            "我觉得自己还需要多加磨练呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x102,
        (
            "#6P#0109F呵呵，那也很厉害了啊。\x02\x03",

            "#0102F竟然能被彩虹剧团所选拔，\x01",
            "并在出道时就出演这么重要的角色。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x15,
        "#1P#1806F唔唔……\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#11P#0004F哈哈……我们已经了解大致情况了。\x02\x03",

            "#0001F不过，据你所说，\x01",
            "伊莉娅小姐本人好像\x01",
            "并不在意这件事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x15,
        (
            "#1P#1808F是的……而且她说，\x01",
            "为了提高舞台表演的完成度，现在要\x01",
            "专心排练，所以不想让无关人员前去打扰……\x02\x03",

            "#1806F特别是，那个……\x01",
            "特别是警察，更是绝对免谈……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0509
    ChrTalk(
        0x101,
        "#11P#0011F那个……\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        (
            "#12P#0211F那就是说，我们好像\x01",
            "也没有什么能做的了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x15,
        (
            "#1P#1802F不、不过，各位不是\x01",
            "『特别任务支援科』的吗？\x02\x03",

            "从杂志上的报道来看，\x01",
            "你们与普通警察相比，\x01",
            "似乎更加亲和近民吧……\x02\x03",

            "#1809F这样一来，伊莉娅小姐\x01",
            "或许也可以接受了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        "#11P#0003F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x102,
        (
            "#6P#0100F虽然这话由我们来说似乎不太合适……\x01",
            "不过，你们没有和游击士协会那边沟通吗？\x02\x03",

            "伊莉娅小姐属于民间人士……\x01",
            "我想应该属于他们的保护对象吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x15,
        (
            "#1P#1808F这、这个嘛……\x02\x03",

            "#1803F因为游击士协会在克洛斯贝尔\x01",
            "也相当受欢迎……\x02\x03",

            "如果那些备受关注的人在公演之前频繁进出剧团，\x01",
            "恐怕会引起一些奇怪的传闻吧……\x02\x03",

            "#1802F出于这种考虑，我认为如果是\x01",
            "各位，大概就不会引起那么大的话题……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0515
    ChrTalk(
        0x15,
        (
            "#1P#1801F啊！对、对不起！\x01",
            "我竟然说了如此失礼的话……！\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        (
            "#11P#0012F没、没什么，\x01",
            "我们完全没有在意啦。\x02\x03",

            "#0000F总而言之……\x01",
            "事情的大致情况，我们已经了解了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    #C0517
    ChrTalk(
        0x101,
        (
            "#5P#0000F……这个委托，我觉得\x01",
            "还是受理比较好，\x01",
            "各位，你们怎么想？\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        "#6P#0102F我当然赞成啊。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x103,
        "#12P#0204F我也没有异议。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0520
    ChrTalk(
        0x104,
        (
            "#0309F哈，这还用说，\x01",
            "当然没有拒绝的理由吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0521
    ChrTalk(
        0x101,
        (
            "#11P#0004F就是这样了，莉夏小姐。\x02\x03",

            "#0000F有关恐吓信的委托，就由我们\x01",
            "特别任务支援科正式受理了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    Sleep(200)

    #C0522
    ChrTalk(
        0x15,
        (
            "#1P#1802F非、非常感谢！\x02\x03",

            "#1809F那我就……\x01",
            "先回剧团了。\x02\x03",

            "我会提前去向剧团长和\x01",
            "伊莉娅小姐报告的，\x01",
            "所以各位可以随时来访。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x102,
        "#6P#0102F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0524
    ChrTalk(
        0x104,
        "#0309F下次见啊～小莉夏！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 4900, 30, 5500, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(1638, 255, 100, 0)    #voice#Rixia
    Sleep(1000)
    OP_68(3000, 950, 1800, 3500)

    def lambda_1010B():
        OP_95(0xFE, 3600, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1010B)
    WaitChrThread(0x15, 1)

    def lambda_10129():
        OP_95(0xFE, 1000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10129)
    Sleep(500)
    SetChrSubChip(0x103, 0x1)
    Sleep(500)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x15, 1)

    def lambda_10155():
        OP_95(0xFE, 1000, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10155)
    Sleep(500)
    Sound(103, 0, 100, 0)

    def lambda_10178():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_10178)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    Sound(104, 0, 100, 0)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    OP_6F(0x1)
    Sleep(500)
    OP_68(6060, 950, 4530, 1600)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    OP_6F(0x1)

    #C0525
    ChrTalk(
        0x101,
        (
            "#5P#0003F那么……\x01",
            "总之我们就去剧团看看吧。\x02\x03",

            "#0000F如果不亲眼对恐吓信进行确认，\x01",
            "调查也就无法展开呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x103,
        (
            "#12P#0204F是啊。\x02\x03",

            "#0202F而且，那也许只是一起恶作剧而已，\x01",
            "这种可能性也不能否认……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        (
            "#0302F呀～不过还真是赚到了啊！\x02\x03",

            "竟然得到了在公演开始之前\x01",
            "进入彩虹剧团的机会呢！\x02\x03",

            "#0309F而且还能见到伊莉娅本人啊！是伊莉娅本人哦！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0528
    ChrTalk(
        0x102,
        (
            "#6P#0108F确实如此……\x01",
            "而且说不定要和那个伊莉娅·普拉提耶\x01",
            "小姐面对面地直接对话呢。\x02\x03",

            "#0106F还真是有点紧张起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        (
            "#5P#0005F有、有那么紧张吗？\x02\x03",

            "#0006F嗯～不过，从杂志上来看，\x01",
            "她确实是个美人……\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x103,
        "#12P#0202F……稍微有些期待哦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7100", 0)
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
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(3000, 1030, 4300, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3000, 0, 4300, 270)
    SetChrPos(0x1, 3000, 0, 4300, 270)
    SetChrPos(0x2, 3000, 0, 4300, 270)
    SetChrPos(0x3, 3000, 0, 4300, 270)
    SetScenarioFlags(0x80, 2)
    OP_29(0x42, 0x4, 0x2)
    OP_29(0x42, 0x1, 0x0)
    OP_29(0x41, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_32_F12D end

    def Function_33_10505(): pass

    label("Function_33_10505")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50120.itc", 0x1E)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 63600, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 61600, 30, 8000, 225)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0531
    AnonymousTalk(
        0x8,
        (
            "原来如此……\x01",
            "好啦，情况我已经基本知道了。\x02\x03",

            "然后呢？\x01",
            "你们准备去哭湿枕头，就此罢手吗？\x02",
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

    #C0532
    ChrTalk(
        0x101,
        (
            "#12P#0006F什、什么哭湿枕头啊……\x02\x03",

            "#0001F一科都已经出动了，\x01",
            "以我们的立场来说，\x01",
            "不也只能选择退让了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x8,
        (
            "#5P#1003F嗯，大概也只能如此了吧。\x02\x03",

            "#1000F不然的话，那个老狐狸副局长多半\x01",
            "又要唠唠叨叨，对你们做出严重警告了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        "#12P#0006F是啊……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#12P#0200F那样的话，我们就提出申请，\x01",
            "对一科进行协助如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x104,
        (
            "#0306F唔，从那个西装眼镜男的\x01",
            "态度来看，这恐怕是很难的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "#5P#1000F嗯，多半如此。\x02\x03",

            "#1003F警察的领地意识是很强的，\x01",
            "一般都不希望别人插手自己的案子。\x02\x03",

            "特别是一科这种精英部门，\x01",
            "像你们这种小鬼如果提出协助，\x01",
            "肯定会被他们二话不说直接拒绝吧。\x02\x03",

            "#1002F──不过，如果你们暗中行事的话，\x01",
            "那就另当别论了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0538
    ChrTalk(
        0x101,
        "#12P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        (
            "#5P#1004F呵呵……我们特别任务支援科，\x01",
            "从某种意义上来说，是属于编制之外的部门。\x02\x03",

            "虽然经常被总部排斥在外，\x01",
            "但反过来说，也可以解释为\x01",
            "拥有一定程度的自主裁量权。\x02\x03",

            "#1002F如果抓准这一点的话，\x01",
            "我们就可以暗中行动，\x01",
            "插足到其它部门的领域中。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#12P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        (
            "#0305F喂喂……\x01",
            "说这种话没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x103,
        "#12P#0211F真是个不良上司呢……\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x8,
        (
            "#5P#1004F呵呵，我也说过的吧？\x02\x03",

            "我基本上是不会给你们提供什么帮助的，\x01",
            "只是负责收拾残局而已。\x02\x03",

            "#1002F真正需要下决心办案的还是你们自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x8,
        (
            "#5P#1003F不过，话虽如此，\x01",
            "但看你们的样子，好像还是很勉强啊。\x02\x03",

            "#1000F毕竟在我们的团队中\x01",
            "有一位迷茫不定的同伴啊。\x02\x03",

            "以现在的状态，还没法团结一心，\x01",
            "做出重大决定吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        "#12P#0006F……那个………\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x104,
        (
            "#0306F算啦，看大小姐现在的样子，\x01",
            "恐怕没办法在短时间内打起精神吧。\x02\x03",

            "#0308F总觉得，她的情绪好像\x01",
            "相当低迷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x103,
        (
            "#12P#0208F确实，感觉她今天一整天\x01",
            "都是那种状态……\x02\x03",

            "#0206F……艾莉前辈，\x01",
            "不要紧吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)

    def lambda_10DA7():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_10DA7)
    Sound(848, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(1100)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)
    OP_63(0xC, 0x12C, 1000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM("ed7513", "ed7515")
    OP_CA(0x1, 0xFF, 0x0)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_10505 end

    def Function_34_10E5A(): pass

    label("Function_34_10E5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis121.itp")
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0550
    ChrTalk(
        0x102,
        (
            "#0103F──不过，还真是奇怪啊。\x02\x03",

            "#0101F这次的事件如此严重，一科本应事先有所察觉才对。\x01",
            "但现在看来，他们的出场却只是个被动的结果而已。\x02\x03",

            "因为要不是莉夏小姐不愿意闹出\x01",
            "太大动静而来委托我们，\x01",
            "估计他们根本就不会知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯～确实……\x02\x03",

            "#0008F也就是说，那并不是犯人为了\x01",
            "混淆一科的视线而采取的策略吗……\x02\x03",

            "#0001F说起来，知道『银』的\x01",
            "存在的人都有谁呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#0103F这个嘛……身为其雇主的\x01",
            "『黑月』当然不用说。\x02\x03",

            "还有一直与他们进行竞争的『鲁巴彻』\x01",
            "和密切关注其动向的搜查一科……\x02\x03",

            "#0100F然后就是，和鲁巴彻有着密切\x01",
            "关系的哈尔特曼议长应该也知道吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0553
    ChrTalk(
        0x101,
        (
            "#5P#0005F哈尔特曼议长……\x01",
            "就是昨天说的那个？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x102,
        (
            "#0106F嗯，帝国派议员的领袖人物，\x01",
            "在议会中拥有首脑级地位的大政治家。\x02\x03",

            "大概可以算是\x01",
            "鲁巴彻的最大后盾了。\x02\x03",

            "#0101F顺便一提，外公的改革方案\x01",
            "几乎全都是被这个人推翻的。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x101,
        (
            "#5P#0008F是吗……\x01",
            "我只是听说过他的名字而已。\x02\x03",

            "#0001F这样一来，对于『银』来说，\x01",
            "他也属于敌对势力了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        "#0106F嗯嗯……虽然关系不大，但也可以这么说吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(500)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0557
    ChrTalk(
        0x101,
        "#11P#0005F缇欧、兰迪？\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#0105F#11P怎么了？\x01",
            "为什么一脸若有所思的表情。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        "#6P#0306F啊……那个，哈哈。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x103,
        (
            "#6P#0202F艾莉前辈……\x01",
            "你今天好像很有精神啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0561
    ChrTalk(
        0x102,
        (
            "#0105F#11P啊，那个……\x02\x03",

            "#0106F──对不起，\x01",
            "昨天真是让大家担心了。\x02\x03",

            "#0100F不过，我已经没事了。\x01",
            "绝对不会拖大家后腿的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0562
    ChrTalk(
        0x101,
        (
            "#5P#0003F那个，艾莉……\x01",
            "不必说拖后腿这种见外的话啦。\x02\x03",

            "#0000F这段时间以来，我们不也都\x01",
            "经常依靠你的各种帮助嘛。\x02\x03",

            "你看，现在也是，有艾莉在，\x01",
            "推理的进展也都顺利很多。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0563
    ChrTalk(
        0x102,
        "#0102F是、是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    OP_64(0x104)

    #C0564
    ChrTalk(
        0x104,
        "#6P#0301F……好诡异。\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x103,
        "#6P#0211F……很可疑。\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)

    #C0566
    ChrTalk(
        0x101,
        "#11P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x102,
        "#0112F#11P等、等一下啦……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x104,
        (
            "#6P#0303F说起来，就在昨天晚上……\x01",
            "我听到楼顶上传来了谈话声呢。\x02\x03",

            "#0302F莫非……\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x103,
        (
            "#6P#0202F……原来如此。\x02\x03",

            "#0204F恭喜你们，\x01",
            "罗伊德前辈、艾莉前辈。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)

    #C0570
    ChrTalk(
        0x101,
        (
            "#11P#0011F慢、慢着啊，有什么\x01",
            "特别的事情需要恭喜吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x102,
        (
            "#0112F#11P对、对啊……\x02\x03",

            "#0113F我们只不过是随便\x01",
            "谈了些各方面的事情而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x104,
        (
            "#6P#0302F原来如此，各方面的事情吗？\x02\x03",

            "#0309F──那，已经进展到什么程度了啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0573
    ChrTalk(
        0x101,
        "#5P#0007F兰迪！\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x102,
        (
            "#0112F#11P等、等一下啦！\x01",
            "缇欧还在这里呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x103,
        (
            "#6P#0205F进展到什么程度……\x02\x03",

            "#0204F啊，我明白了，这是指在交往的过程中，\x01",
            "需要一步一步逐渐进展到各个阶段──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0576
    ChrTalk(
        0x101,
        "#11P#0012F不对不对，没那回事啊！\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x104,
        "#6P#0309F嘘～嘘～\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x103,
        "#6P#0202F……嘘～嘘～\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x3E8, 0x5DC)

    #C0579
    ChrTalk(
        0x102,
        "#0109F#4S#90W#11P请 你 们 适 可 而 止 哦。#20W\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x104,
        "#6P#0306F是……\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x101,
        (
            "#11P#0006F真是的……\x02\x03",

            "竟然会怀疑我和艾莉的关系，\x01",
            "那种事情根本就不可能吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)

    #C0582
    ChrTalk(
        0x102,
        "#0105F#40W………哎…………#20W\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#11P#0012F我们两个根本就不配啊，\x01",
            "还是该说，完全不会有那种感觉呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0584
    ChrTalk(
        0x101,
        "#5P#0000F对吧，艾莉？\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x102,
        "#0101F#70W…………………………………#20W\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x101,
        "#5P#0005F……咦？\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x104,
        "#6P#0306F（喂喂……）\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x103,
        "#6P#0211F（好像踩到地雷了呢……）\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        (
            "#0104F#40W……对啊，说得没错……\x02\x03",

            "那只是一次非常普通的谈话而已，完全就是\x01",
            "麻烦你耐着性子听我说了一大堆无聊的话……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)

    #C0590
    ChrTalk(
        0x102,
        (
            "#0101F#4S说得没错，完全没有产生过什么\x01",
            "甜蜜的氛围！一点都没有！\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x101,
        (
            "#5P#0011F……那、那个……\x02\x03",

            "#0012F那个，我刚才说我们两个\x01",
            "不配，意思其实是我\x01",
            "配不上艾莉你……\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x102,
        "#0111F（瞪眼）……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x101,
        "#5P#0006F……对不起。\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#6P#0309F呵呵呵……\x02\x03",

            "#0302F算了，不管这些啦，\x01",
            "总之，能打起精神就是最好了，对吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0595
    ChrTalk(
        0x102,
        "#0105F#11P啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)

    #C0596
    ChrTalk(
        0x103,
        (
            "#6P#0204F……我也安心了。\x02\x03",

            "#0208F我还以为前辈会……\x01",
            "会辞去警察的工作，\x01",
            "离开我们呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x102,
        (
            "#0106F#11P……抱歉哦，让你担心了。\x02\x03",

            "#0102F虽然我还不知道\x01",
            "将来的路该怎么走……\x02\x03",

            "但对于现在的我来说，最正确的\x01",
            "选择就是留在这里，这是一定没错的。\x02\x03",

            "#0104F所以，就再一次……\x01",
            "请大家多多关照吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        "#5P#0002F艾莉……\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x103,
        "#6P#0202F……艾莉前辈。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x104,
        (
            "#6P#0309F哈哈，要是没有了大小姐的说教，\x01",
            "就产生不了紧张感啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        (
            "#0111F#11P我之所以会说教，\x01",
            "还不都是因为你们……\x02\x03",

            "#0103F──算啦，这都无所谓了。\x02\x03",

            "#0101F调查方针已经考虑过了吧，\x01",
            "最后决定要怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        "#5P#0003F这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x103,
        (
            "#6P#0206F虽说是决定了要使用与\x01",
            "一科不同的途径来接近『银』……\x02\x03",

            "但如今出现了这么多个切入点，\x01",
            "反而让人有些迷惑了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x104,
        (
            "#6P#0303F既然如此，那就这样吧。\x02\x03",

            "#0300F我们就先去卡尔瓦德的\x01",
            "东方人街看看，怎么样？\x02\x03",

            "这样一来，多少也能掌握一点\x01",
            "关于『银』的线索吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        "#5P#0005F这、这确实是个盲点呢。\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x102,
        (
            "#0101F#11P不过，上层会批准我们\x01",
            "去外国出差吗？\x02\x03",

            "似乎已经超过支援科的\x01",
            "责任范畴了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x103,
        "#6P#0203F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 10400, 850, 7600, 90)
    Sound(820, 0, 100, 0)
    Sleep(500)
    OP_68(16100, 1850, 10000, 3000)
    MoveCamera(7, 21, 0, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_1216F():
        OP_95(0xFE, 16100, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1216F)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    WaitChrThread(0x103, 1)

    def lambda_121A6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_121A6)
    OP_6F(0x51)

    #C0608
    ChrTalk(
        0x101,
        "#0005F缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        "#0105F#5P怎么了？\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x103,
        (
            "#0200F我想稍微调查一下\x01",
            "警察局的数据库。\x02\x03",

            "或许能掌握到\x01",
            "一科的动向呢……\x02\x03",

            "#0203F不过，昨天晚上才刚刚调查过，\x01",
            "现在大概也不会有什么新情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#0001F是吗……\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x104,
        "#1P#0300F哎，总比什么都不干好嘛。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_90(0x101, 14800, 850, 7600, 270)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, 14800, 850, 5400, 270)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x104, 10400, 850, 5400, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x104, 3, 0, 36)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 35)
    OP_92(0x101, 0x3B60, 0x2134, 0x1F4)

    def lambda_1232F():
        OP_95(0xFE, 15200, 850, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1232F)
    WaitChrThread(0x101, 1)

    def lambda_1234D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1234D)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    Sound(824, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0613
    ChrTalk(
        0x103,
        "#0205F啊……\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x101,
        "#6P#0001F怎么了？\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x103,
        (
            "#0202F……真少见呢……\x02\x03",

            "好像有导力邮件\x01",
            "发送过来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x101,
        "#6P#0005F导力邮件？\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x102,
        (
            "#6P#0100F也就是发送到终端的\x01",
            "文字类情报吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x103,
        (
            "#0206F是的，虽然非常便利，\x01",
            "但在警察系统，却几乎没有人\x01",
            "使用到这个功能……\x02\x03",

            "可能是因为目前会操作\x01",
            "键盘的人太少了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x101,
        (
            "#6P#0006F原来如此……\x01",
            "确实，我也不会用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x104,
        "#0300F先不说这些了，这到底是谁发的？\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x103,
        "#0202F我来打开看看。\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1200)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0622
    ChrTalk(
        0x103,
        "#0205F…………哎………………\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        "#6P#0005F怎么了……？\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x102,
        (
            "#6P#0105F到底是谁啊──\x02\x03",

            "#0101F！？\x02",
        )
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, 130, -1, -1)
    SetChrName("")

    #A0625
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "此乃『银』之委托。\x01",
            "越过试炼，至吾所在。\x01",
            "如是，将授予汝等使命。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0626
    AnonymousTalk(
        0x101,
        "#0007F这、这是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0627
    AnonymousTalk(
        0x104,
        (
            "#0307F喂喂……\x01",
            "这是谁搞的恶作剧吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0628
    AnonymousTalk(
        0x102,
        (
            "#0101F缇欧……\x01",
            "这邮件是从哪里发来的！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0629
    AnonymousTalk(
        0x103,
        "#0201F不是警察局总部……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #A0630
    AnonymousTalk(
        0x103,
        (
            "#0205F……找到了。\x02\x03",

            "#0203F『克洛斯贝尔国际银行』\x01",
            "（International Bank of Crossbell）……\x02\x03",

            "#0201F──通称ＩＢＣ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0631
    ChrTalk(
        0x101,
        "#6P#0013F……怎么回事……？\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x104,
        (
            "#0301FＩＢＣ的话，也就是那个\x01",
            "汇聚了整个大陆的米拉的银行吧？\x02\x03",

            "这种恶作剧邮件\x01",
            "为什么会从那种地方发来呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x103,
        (
            "#0206F……问我也没用啊。\x02\x03",

            "#0201F不过，这封邮件确实是从\x01",
            "ＩＢＣ的终端发来的，肯定没错。\x02\x03",

            "虽然并不知道发信人是谁。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0634
    ChrTalk(
        0x101,
        (
            "#6P#0008F莫非，『银』已经潜入到\x01",
            "ＩＢＣ中了吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    #C0635
    ChrTalk(
        0x102,
        (
            "#12P#0103F说实话，这也并非完全不可能啊。\x02\x03",

            "#0101F而且ＩＢＣ的大楼内\x01",
            "也入驻了好几家外部公司。\x02\x03",

            "好像……连爱普斯泰恩财团的\x01",
            "事务所也在那里面吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(150)

    #C0636
    ChrTalk(
        0x103,
        (
            "#0203F是的……\x01",
            "我的熟人就在那里工作。\x02\x03",

            "#0200F可是……这封邮件似乎\x01",
            "是从ＩＢＣ的主终端\x01",
            "发送来的。\x02\x03",

            "我想，和外部公司产生关联的\x01",
            "可能性应该很低……\x02",
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

    #C0637
    ChrTalk(
        0x101,
        (
            "#6P#0006F……那就只能直接去问问看了吧。\x02\x03",

            "虽说我们要尽量在瞒着一科的\x01",
            "前提下展开调查……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    #C0638
    ChrTalk(
        0x104,
        (
            "#0306F但如果我们不公开身份，\x01",
            "恐怕很难在那里进行询问工作啊。\x02\x03",

            "#0300F不过，总之必须要在某些人\x01",
            "横插一腿之前赶快行动，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        (
            "#12P#0103F……………………………………\x02\x03",

            "#0100F……说不定，\x01",
            "ＩＢＣ会允许我们进行秘密调查呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    #C0640
    ChrTalk(
        0x101,
        "#5P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x103,
        "#0205F要怎么做呢……？\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x102,
        (
            "#12P#0104F……我有个朋友\x01",
            "是ＩＢＣ的相关人员哦。\x02\x03",

            "#0100F如果和她父亲说清楚事情经过的话，\x01",
            "或许可以得到一些协助吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        "#5P#0000F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x104,
        (
            "#0309F#5P噢噢，这可真是及时雨啊。\x02\x03",

            "#0300F不愧是大小姐，\x01",
            "关系网真广啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x102,
        (
            "#12P#0104F呵，普普通通啦。\x02\x03",

            "#0108F不过，她的父亲可是个大忙人，\x01",
            "而且还不知道现在是否在克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x103,
        "#0200F他到底是什么身份呢？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x102,
        (
            "#12P#0103F……我想你们大概听说过他。\x02\x03",

            "#0100F他的名字是迪塔·库罗伊斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0648
    ChrTalk(
        0x101,
        "#5P#0005F哎！？\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x103,
        "#0205F啊……\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x104,
        "#0305F#5P什么啊，他很有名吗？\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        (
            "#5P#0000F啊，是啊……\x02\x03",

            "#0003F从某种意义上来说，他的知名度\x01",
            "或许和伊莉娅小姐不相上下呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x103,
        (
            "#0204F迪塔·库罗伊斯……\x02\x03",

            "大陆中首屈一指的资产家，\x01",
            "国际经济界的中心人物之一……\x02\x03",

            "#0202F也是ＩＢＣ的现任总裁，没错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x104,
        "#0307F#5P哦哦，原来是银行的首脑啊！？\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        (
            "#12P#0104F他是我爸爸以前的老朋友。\x02\x03",

            "和我外公也是早有往来，关系甚好，\x01",
            "所以我才能与他熟识的……\x02\x03",

            "#0102F他的女儿和我也是童年的玩伴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        (
            "#5P#0002F是这样啊……\x02\x03",

            "#0006F不过，像那种日理万机的人……\x01",
            "不在自治州内也是常有的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x102,
        (
            "#12P#0106F嗯……一年之中，他似乎有\x01",
            "大半时间都在国外奔波忙碌呢。\x02\x03",

            "#0101F不过，就算白跑一趟，也没什么损失啊。\x02\x03",

            "而且我的朋友应该在的。\x01",
            "即使只是去拜访一下也好，总之就过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，就这么办吧。\x02\x03",

            "#0003F不过，虽然这样一来，\x01",
            "调查的目标是已经确定了，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x103,
        (
            "#0206F……邮件的用意还不能确定，对吧？\x02\x03",

            "#0201F恐吓信也是一样，\x01",
            "发信人的目的究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x104,
        (
            "#0302F#5P算了，难得对方特意\x01",
            "与我们主动接触。\x02\x03",

            "我们就大胆迎上去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x102,
        (
            "#12P#0104F说得也是呢……\x02\x03",

            "#0100F出发吧，目标是ＩＢＣ大楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    OP_68(15000, 1850, 8900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetChrPos(0x1, 15000, 850, 8900, 45)
    SetChrPos(0x2, 15000, 850, 8900, 45)
    SetChrPos(0x3, 15000, 850, 8900, 45)
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetScenarioFlags(0x82, 0)
    OP_C7(0x1, 0x1000)
    OP_29(0x43, 0x4, 0x2)
    OP_29(0x43, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13331")
    OP_29(0xF, 0x4, 0x40)
    Jump("loc_13343")

    label("loc_13331")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13343")
    OP_29(0xF, 0x4, 0x40)

    label("loc_13343")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7100", 0)
    EventEnd(0x5)
    Return()

    # Function_34_10E5A end

    def Function_35_13357(): pass

    label("Function_35_13357")

    Sleep(500)
    OP_93(0x102, 0x0, 0x1F4)

    def lambda_13366():
        OP_96(0xFE, 0x4010, 0x352, 0x1EDC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13366)
    WaitChrThread(0x102, 1)
    Return()

    # Function_35_13357 end

    def Function_36_13380(): pass

    label("Function_36_13380")


    def lambda_13385():
        OP_95(0xFE, 10400, 850, 8600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13385)
    WaitChrThread(0x104, 1)

    def lambda_133A3():
        OP_95(0xFE, 14400, 850, 9900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_133A3)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_36_13380 end

    def Function_37_133C4(): pass

    label("Function_37_133C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("apl/ch50091.itc", 0x1F)
    OP_68(5500, 900, 4200, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 5500, 130, 6250, 180)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 4900, 130, 2200, 0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, 6000, 130, 2200, 0)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 3000, 0, 2500, 225)
    ClearChrFlags(0xC, 0x1)
    BeginChrThread(0xC, 3, 0, 0)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x1D)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 5300, 350, 4500, 0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    Sleep(500)
    Sound(18, 0, 100, 0)
    UseItem(0x2BF, 0xFF)
    Sleep(500)
    PlayBGM("ed7110", 0)
    SetCameraDistance(24000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0661
    ChrTalk(
        0x104,
        (
            "#4P#0306F哎呀……\x01",
            "事态扩大了呢。\x02\x03",

            "#0301F眼下，恐怕大部分市民\x01",
            "都已经陷入骚乱了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x103,
        (
            "#12P#0206F这也没办法啊，在彩虹剧团的\x01",
            "新剧首次公开的过程中，\x01",
            "竟然发生了暗杀市长未遂的事件……\x02\x03",

            "#0211F丑闻这个词汇的意义，我想在此时\x01",
            "已经发挥到了极致吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#5P#0006F同情市长的意见占到了多数，\x01",
            "倒还算是不幸中的万幸……\x02\x03",

            "#0008F不过，和阿奈斯特有关的那个\x01",
            "帝国派议员，到最后也没有被曝光姓名呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x104,
        (
            "#4P#0303F算啦，反正他大概也已经被限制行动了。\x02\x03",

            "#0301F而且，再怎么说，这次暗杀未遂事件的\x01",
            "主要起因还在于那个混蛋秘书自己发疯吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯……多半如此。\x02\x03",

            "#0001F对帝国派而言，\x01",
            "暗杀市长这种事情并不会\x01",
            "给他们带来什么好处……\x02\x03",

            "#0008F只是，共和国派与『黑月』有所瓜葛，\x01",
            "所以只要将暗杀者的嫌疑推到『银』头上，\x01",
            "就能成为针对共和国派的攻击材料了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x104,
        "#4P#0305F原来如此啊……\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x103,
        (
            "#12P#0208F可是，那个秘书……\x01",
            "总觉得他的样子很奇怪呢。\x02\x03",

            "#0201F该说是一时冲动、失去理智……\x01",
            "还是已经听不进人说话了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯……我也很在意呢。\x02\x03",

            "#0001F据说一科已经审问过他了，\x01",
            "最后的结果如何呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x8, 16500, 850, 3700, 270)

    #N0669
    NpcTalk(
        0x8,
        "男人的声音",
        (
            "──似乎是精神完全错乱，\x01",
            "已经陷入无法正常对话的状态了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x4)
    OP_68(14500, 1850, 3700, 2000)
    SetCameraDistance(23500, 2000)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    OP_6F(0x11)

    #C0670
    ChrTalk(
        0x101,
        "#0005F科长……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_139C1():
        OP_95(0xFE, 16500, 850, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_139C1)
    Sleep(1000)
    Fade(1000)
    OP_68(6500, 900, 5000, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    OP_68(4500, 900, 5000, 3000)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 4500, 850, 9100, 270)

    def lambda_13A43():
        OP_95(0xFE, 2500, 850, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13A43)
    WaitChrThread(0x8, 1)

    def lambda_13A61():
        OP_95(0xFE, 2500, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13A61)
    Sleep(700)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    OP_6F(0x1)

    #C0671
    ChrTalk(
        0x104,
        (
            "#11P#0301F精神状态已经混乱\x01",
            "到了没法接受审问的程度吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x8,
        (
            "#6P#1003F嗯，审问工作一无所获，\x01",
            "所以暂时将他送到拘留所去了。\x02\x03",

            "#1000F据说是打算去\x01",
            "请教会的精神问题专家或\x01",
            "乌尔斯拉医院的相关人员来帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x101,
        "#5P#0006F是吗……\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x8,
        (
            "#6P#1002F呵呵，不过你们\x01",
            "还真是立了大功哦。\x02\x03",

            "今天去总部的时候，\x01",
            "连那个老狐狸都满脸\x01",
            "堆笑地表扬你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        "#5P#0011F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x103,
        "#12P#0211F这场面真是难以想象呢……\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x104,
        (
            "#11P#0306F就算听到这种消息，\x01",
            "也完全高兴不起来啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x8,
        (
            "#6P#1003F不光是老狐狸一个人，\x01",
            "全体警察都在夸奖你们呢。\x02\x03",

            "#1002F哈，至于一科那边的人，心情大概会有些\x01",
            "复杂吧，不过这样一来，他们肯定也会对\x01",
            "你们有少许改观，这是毫无疑问的。\x02\x03",

            "你们就坦率一点，表现得开心些吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x101,
        "#5P#0000F说得……也对啊。\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x103,
        (
            "#12P#0208F不过……\x01",
            "说心里话，还真是开心不起来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x104,
        (
            "#11P#0303F是啊……\x01",
            "只要一想到大小姐此刻的心情……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x102, 0x8)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_133C4 end

    def Function_38_13E21(): pass

    label("Function_38_13E21")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("chr/ch05000.itc", 0x21)
    LoadChrToIndex("chr/ch08201.itc", 0x22)
    LoadChrToIndex("apl/ch50380.itc", 0x23)
    LoadChrToIndex("apl/ch50092.itc", 0x24)
    OP_68(258000, 700, 68700, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 256399, 0, 68100, 180)
    SetChrPos(0x103, 254900, 0, 68100, 90)
    SetChrPos(0x102, 256399, 0, 66600, 0)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 255400, 30, 71000, 180)

    def lambda_13F1D():

        label("loc_13F1D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_13F1D")

    QueueWorkItem2(0xC, 1, lambda_13F1D)
    SetChrFlags(0x9, 0x80)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01109.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis158.itp")
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    Sleep(1000)
    SetChrName("")

    #A0682
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──１周过去了。\x02\x03",

            "救出琪雅的罗伊德一行人将\x01",
            "她藏匿在了特别任务支援科的大楼内，\x01",
            "并随时警戒着黑手党们前来报复。\x02\x03",

            "通过警察局总部的监视，外加约纳的情报网，大家随时\x01",
            "都在密切注意着黑手党与哈尔特曼议长的动向，\x01",
            "日子就这么一天天过去……\x02\x03",

            "而另一方面，虽然记忆还没有恢复，\x01",
            "但琪雅却并没有表现出丝毫不安，\x01",
            "反而很快就和支援科的成员们熟悉起来。\x02\x03",

            "接下来──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    PlayBGM("ed7110", 0)
    OP_68(257000, 700, 68700, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 39)
    WaitChrThread(0x102, 3)

    def lambda_14159():
        OP_96(0xFE, 0x3E738, 0x0, 0x10A04, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14159)
    Sleep(300)

    def lambda_14176():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14176)
    WaitChrThread(0x103, 1)
    Sound(820, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    def lambda_141A8():
        OP_96(0xFE, 0x3E3B4, 0x0, 0x10A04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_141A8)
    WaitChrThread(0x103, 1)

    def lambda_141C6():
        OP_93(0xA, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_141C6)
    WaitChrThread(0xA, 2)

    def lambda_141D7():
        OP_93(0xA, 0x10F, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_141D7)
    WaitChrThread(0xA, 2)
    OP_63(0xA, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    BeginChrThread(0x102, 3, 0, 39)
    OP_68(256000, 700, 68700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    OP_64(0x102)
    OP_64(0x103)
    SetMapObjFlags(0xE, 0x4)
    OP_68(64000, 1100, 6900, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 65300, 0, 6900, 270)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 62700, 0, 6300, 90)
    SetChrPos(0x104, 62700, 0, 7500, 90)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0683
    AnonymousTalk(
        0x101,
        "#0005F──停战吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0684
    ChrTalk(
        0x8,
        (
            "#1003F#11P嗯，虽然并不是正式声明，\x01",
            "但听说鲁巴彻向警察局总部传达了这个意向。\x02\x03",

            "#1001F那个孩子之所以会混在拍卖商品中，\x01",
            "完全是因为某些地方出了差错──也就是说，\x01",
            "他们对那孩子的事情也是一无所知。\x02\x03",

            "#1006F虽然他们主张说这一切都是『黑月』布的局，\x01",
            "不过，就现阶段而言，这个说法也许很难成立吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#6P#0006F……也是呢。\x02\x03",

            "#0001F我们闯进去的时候，\x01",
            "刚好看到『银』打倒了房间中的黑手党部下，\x01",
            "时机非常巧。\x02\x03",

            "我想他应该并没有把琪雅从外面带进来，\x01",
            "并同箱子里的人偶进行掉包的时间。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_14560")

    #C0686
    ChrTalk(
        0x104,
        (
            "#6P#0306F也就是说，在那个箱子\x01",
            "刚被搬运到宅子里时，\x01",
            "里面的东西就已经被掉过包了吧。\x02\x03",

            "#0301F话说，那个本来应该被展出的\x01",
            "人偶是从哪里来的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145EE")

    label("loc_14560")


    #C0687
    ChrTalk(
        0x104,
        (
            "#6P#0306F也就是说，在那个箱子\x01",
            "刚被搬运到宅子里时，\x01",
            "里面的东西就已经被掉过包了吧。\x02\x03",

            "#0301F话说，那个本来应该被拍卖的\x01",
            "人偶是从哪里来的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145EE")


    #C0688
    ChrTalk(
        0x8,
        (
            "#1003F#11P具体的情况我也不清楚，\x01",
            "但好像是通过雷米菲利亚那边的\x01",
            "地下交易而获得的。\x02\x03",

            "#1001F好像是在纪念庆典的最终日──\x01",
            "也就是竞拍会的当天\x01",
            "才被送到议长宅邸里的……\x02\x03",

            "他们还主张说，那个运送公司\x01",
            "也是个徒有空壳的皮包公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x101,
        (
            "#6P#0011F这怎么可能……\x02\x03",

            "#0010F也就是说，那些家伙坚决\x01",
            "主张自己是完全的受害者吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x8,
        (
            "#1003F#11P呵，就是这么回事。\x02\x03",

            "虽然还不清楚那些主张是真是假……\x01",
            "但他们肯定要拼命辩解就是了。\x02\x03",

            "#1001F──因为要是处理不妥，\x01",
            "可就要背上『贩卖人口』的嫌疑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x101,
        "#6P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x104,
        (
            "#6P#0303F武器走私、洗黑钱、\x01",
            "拍卖赃物的地下拍卖会……\x02\x03",

            "#0301F连这些犯罪行为都可以轻松为之的\x01",
            "家伙们，却唯独害怕贩卖人口的罪行，\x01",
            "无论如何也想拼命洗刷自己的嫌疑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x8,
        (
            "#1001F#11P这也是理所当然的吧。\x02\x03",

            "#1003F人口交易属于最恶劣的罪行……\x01",
            "是绝对不会被原谅的重罪。\x02\x03",

            "所以警察无论如何都不会再坐视不理，\x01",
            "而且，如果消息传到游击士协会那里，\x01",
            "恐怕他们也会倾尽全力来进行制裁吧。\x02\x03",

            "#1000F——这也是为了不让其标志徽章『支援护臂甲』蒙灰。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        (
            "#6P#0006F这么巨大的风险，议长就不用说了，\x01",
            "即使是鲁巴彻也无法承担……\x02\x03",

            "#0001F──虽然道理上明白，\x01",
            "但说实话，我还是很难接受呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x8,
        (
            "#1003F#11P嗯，所以才更要暂时休战啊。\x02\x03",

            "#1000F关于你们的潜入调查──\x01",
            "用那边的话来说就是非法入侵。\x01",
            "总之，他们可以从此不再追究。\x02\x03",

            "而你们『偶然』救出的那名少女，\x01",
            "他们也同意完全交给我们来负责。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x104,
        (
            "#6P#0306F作为代价，对于这次的事件，\x01",
            "就要认同他们的主张吧……\x02\x03",

            "而且绝对不能对游击士协会\x01",
            "透露半点风声，没错吧？\x02\x03",

            "#0300F哎呀呀，他们确实很拼命呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x101,
        (
            "#6P#0008F……………………………………\x02\x03",

            "#0006F……虽然一想到琪雅所受的对待，\x01",
            "就无法认同这种暧昧不清的处理办法……\x02\x03",

            "#0000F但只要能保证那个孩子今后\x01",
            "不会再成为那些黑手党的目标，\x01",
            "我们或许还是应该接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x8,
        (
            "#1002F#11P嗯，我也这么想。\x02\x03",

            "#1003F……不过呢，最关键的\x01",
            "问题还是那个孩子的身份。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        "#6P#0006F嗯……\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x104,
        (
            "#6P#0306F除了名字之外，\x01",
            "她好像什么都不记得呢。\x02\x03",

            "#0302F──不过呢，\x01",
            "性格倒是很开朗活泼，\x01",
            "总之是个很愿意与人亲近的小鬼。\x02\x03",

            "总觉得才过了很短时间，\x01",
            "她就和我们所有人都混熟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        (
            "#6P#0014F哈哈……确实如此。\x02\x03",

            "#0002F蔡特就不用说了，\x01",
            "她和科长都很亲近呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x8,
        (
            "#1004F#11P哈哈，还好吧。\x02\x03",

            "#1002F因为我抽烟，所以\x01",
            "小孩一般都不会靠近我……\x02\x03",

            "但她好像一点都不在意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        (
            "#6P#0302F大小姐和阿缇非常宠爱那小鬼，\x01",
            "好像已经完全入了迷呢……\x02\x03",

            "今天大概又会去百货店\x01",
            "给她买一大堆衣服回来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x101,
        (
            "#6P#0004F哈哈，这种时候有\x01",
            "女性成员在，可真是得救了呢。\x02\x03",

            "有些事情，我们男人\x01",
            "无论如何也都做不好呢……\x02\x03",

            "#0008F不过……\x01",
            "她到底是哪里的孩子呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Sound(103, 0, 100, 0)
    Fade(500)
    OP_68(59700, 900, 3400, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21500, 0)
    OP_68(61700, 900, 3400, 1500)
    SetChrPos(0xA, 59000, 0, 3400, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_14F80():
        OP_96(0xFE, 0xF104, 0x0, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14F80)

    def lambda_14F9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14F9A)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_6F(0x1)

    #C0705
    ChrTalk(
        0xA,
        (
            "#12P#1110F啊，找到了！\x02\x03",

            "#1109F罗伊德，快看快看～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_15041():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15041)

    def lambda_1504E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1504E)

    def lambda_1505B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1505B)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    OP_68(62600, 1200, 5800, 1000)
    MoveCamera(50, 15, 0, 1000)
    SetCameraDistance(23000, 1000)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)

    def lambda_150B5():
        OP_95(0xFE, 62600, 0, 5800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_150B5)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)

    def lambda_150DB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_150DB)
    Sound(819, 0, 100, 0)
    OP_6F(0x79)

    #C0706
    ChrTalk(
        0x101,
        (
            "#0011F#5P哇哇……\x01",
            "等一下啊，琪雅！？\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0xA,
        (
            "#12P#1109F艾莉和缇欧给我\x01",
            "买了很多新衣服哦！\x02\x03",

            "虽然每件都很可爱，\x01",
            "但我还是最喜欢这件！\x02\x03",

            "#1110F看啊看啊，合身吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        (
            "#0012F#5P哎，你一直这么抱着我，\x01",
            "我要怎么看呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xA,
        "#12P#1105F啊，对哦～\x02",
    )

    CloseMessageWindow()
    OP_68(62700, 1200, 4900, 1000)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)

    def lambda_15205():
        OP_96(0xFE, 0xF4EC, 0x0, 0x1324, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15205)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    def lambda_15225():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15225)
    WaitChrThread(0xA, 2)

    def lambda_15236():
        OP_93(0xA, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15236)
    Sleep(150)
    Sound(2031, 255, 100, 0)    #voice#KeA
    WaitChrThread(0xA, 2)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrPos(0x103, 64599, 30, 5100, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMessageWindowPos(280, 150, -1, -1)

    #N0710
    NpcTalk(
        0x103,
        "琪雅",
        "#1P看啊看啊，合身吗！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 120, -1, -1)

    #A0711
    AnonymousTalk(
        0x101,
        "#0002F嘿……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 70, -1, -1)

    #A0712
    AnonymousTalk(
        0x104,
        "#0305F哦哦……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 20, -1, -1)

    #A0713
    AnonymousTalk(
        0x8,
        "#1002F嗯……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0714
    ChrTalk(
        0xA,
        "#12P#1110F怎么样！？\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x101,
        (
            "#0004F#5P嗯……非常可爱。\x02\x03",

            "#0002F特别适合琪雅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xA,
        (
            "#12P#1109F真的吗～！？\x02\x03",

            "#1102F喂喂，兰迪和科长\x01",
            "也觉得可爱吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x104,
        "#5P#0309F噢～可爱可爱。\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x8,
        "#5P#1002F嗯，不错啊。\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xA,
        "#12P#1109F嘿嘿嘿……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x102, 59000, 0, 3400, 90)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x103, 59000, 0, 3400, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_15482():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15482)

    def lambda_1549C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1549C)
    Sleep(700)

    def lambda_154B0():
        OP_95(0xFE, 60000, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_154B0)

    def lambda_154CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_154CA)
    WaitChrThread(0x102, 1)

    def lambda_154DF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_154DF)
    WaitChrThread(0x103, 1)

    def lambda_154F0():
        OP_95(0xFE, 61000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_154F0)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x1F4)

    #C0720
    ChrTalk(
        0x102,
        (
            "#12P#0102F呵呵，马上\x01",
            "就来展示给大家看了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x103,
        (
            "#6P#0206F……还有很多衣服\x01",
            "想给你试穿呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)

    #C0722
    ChrTalk(
        0xA,
        (
            "#1110F艾莉、缇欧！\x01",
            "罗伊德他们都说我可爱！\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x102,
        "#12P#0109F呵呵，那太好啦。\x02",
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x103,
        (
            "#6P#0202F不过，罗伊德前辈的话，\x01",
            "不管琪雅穿什么衣服\x01",
            "也都会说可爱的……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0725
    ChrTalk(
        0x101,
        (
            "#0012F#5P这个……\x01",
            "哈哈，也许说得没错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x104,
        (
            "#5P#0309F哈哈，你们简直就像溺爱小孩的父母嘛。\x02\x03",

            "#0300F嗯～不过，阿琪\x01",
            "才刚来了一个星期吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x102,
        (
            "#12P#0104F呵呵……\x01",
            "总觉得有些难以相信呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0728
    ChrTalk(
        0x102,
        (
            "#12P#0105F对了……\x02\x03",

            "#0101F警察局总部发来的联络，\x01",
            "最后怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x103,
        (
            "#6P#0200F听说鲁巴彻那边\x01",
            "好像传达了什么意向……？\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x8,
        "#5P#1003F啊，那个嘛……\x02",
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x101,
        (
            "#0006F#5P……等到吃午饭的时候\x01",
            "再慢慢说给你们听吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(12600, 2350, 4800, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x103, 11300, 900, 2550, 90)
    SetChrPos(0x104, 13900, 900, 2550, 270)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 11300, 900, 4600, 90)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16000, 850, 6400, 180)
    EndChrThread(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x6)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x6)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x6)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x6)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x24)
    SetChrSubChip(0x21, 0x6)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12400, 1400, 2600, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0xC)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12000, 1300, 2600, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x6)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 13000, 1400, 2600, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0xC)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13400, 1300, 2600, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x20)
    SetChrSubChip(0x25, 0x7)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12700, 1400, 5500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x7)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 12700, 1400, 3500, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x24)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 16000, 750, 5500, 0)
    OP_68(12600, 1850, 4800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0732
    ChrTalk(
        0x102,
        (
            "#0104F原来如此……\x02\x03",

            "#0100F总之，暂时是不必再担心\x01",
            "黑手党那边了。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x103,
        (
            "#6P#0208F只是，最根本的问题\x01",
            "却仍然留在我们的眼前……\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x8,
        (
            "#5P#1006F嗯，把最棘手的那部分\x01",
            "完全丢给我们了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        (
            "#0003F#11P总之，最关键的\x01",
            "还是琪雅的记忆与身份……\x02\x03",

            "#0001F──那个，琪雅，\x01",
            "还是什么都想不起来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xA,
        (
            "#6P#1100F嗯～……完全想不起来。\x02\x03",

            "#1109F罗伊德张大嘴，\x01",
            "眼睛瞪圆的样子\x01",
            "倒是想得起来～\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x101,
        (
            "#0006F#11P呃……\x02\x03",

            "#0011F那是一周之前，\x01",
            "我们第一次见面时的事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xA,
        (
            "#6P#1108F可是，那之前的事情\x01",
            "我就什么也想不起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        "#0000F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x104,
        (
            "#0304F#11P算啦，既然想不起来，\x01",
            "那也就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x103,
        (
            "#6P#0200F#6P……对各方面的咨询，\x01",
            "都有什么结果吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x8,
        (
            "#5P#1000F啊……那个啊。\x02\x03",

            "车站、空港，还有国境门那边都问过了，\x01",
            "但目前似乎还没有发现任何线索。\x02\x03",

            "#1003F以后恐怕也不会有什么进展吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x101,
        "#0008F#11P……这样啊……\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "#6P#1105F？？？\x02\x03",

            "#1101F怎么了，罗伊德？\x01",
            "你肚子疼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        "#0012F#11P哈哈，没有啦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0746
    ChrTalk(
        0x101,
        (
            "#0003F#11P──科长，\x01",
            "今天下午……\x02\x03",

            "#0001F我可不可以带琪雅\x01",
            "去外面散散步呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0747
    ChrTalk(
        0x8,
        "#5P#1001F嗯……\x02",
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x102,
        "#0101F罗伊德，你有什么想法吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0749
    ChrTalk(
        0x101,
        (
            "#0004F#11P嗯……\x02\x03",

            "#0000F我想去委托\x01",
            "游击士协会帮忙试试。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
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

    #C0750
    ChrTalk(
        0x102,
        "#0105F咦咦！？\x02",
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x103,
        "#6P#0205F你是认真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0xA,
        "#6P#1111F游～击？\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x8,
        (
            "#5P#1004F……原来如此啊。\x02\x03",

            "#1002F那些家伙在大陆各地\x01",
            "都设有协会分部……\x02\x03",

            "你想利用他们那庞大的情报网寻找线索吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    #C0754
    ChrTalk(
        0x101,
        (
            "#0006F#11P嗯，在这种时候，\x01",
            "我觉得应该请求他们帮忙。\x02\x03",

            "#0001F……不行吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x8,
        (
            "#5P#1002F算啦，这不是也挺好的吗？\x02\x03",

            "#1004F警察和游击士协会\x01",
            "又不是对立关系。\x02\x03",

            "要说稍微有些心存芥蒂的话，\x01",
            "那肯定也主要是我们警察这边吧。\x02\x03",

            "#1002F而且案件情况也摆在那里，如果请求\x01",
            "他们协助，应该不会被拒绝吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x101,
        "#0004F#11P嗯，我也是这么想的。\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x104,
        (
            "#0300F#11P哈，反正我们和艾丝蒂尔\x01",
            "他们的关系也一直都挺融洽的。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x102,
        (
            "#0104F确实，如果想与协会商量的话，\x01",
            "现在也许是个很好的机会呢。\x02\x03",

            "#0101F不过，罗伊德……\x01",
            "你说要带小琪雅出去，\x01",
            "是准备一个人带着她吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    #C0759
    ChrTalk(
        0x101,
        (
            "#0005F#11P我确实是这么打算的……\x02\x03",

            "#0000F这并不是什么值得全员出动的事情，\x01",
            "我觉得自己一个人就已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x102,
        (
            "#0103F……我无法赞同哦。\x02\x03",

            "#0111F琪雅本来就和你最亲密，\x01",
            "你居然还想更进一步地独占她。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        "#0011F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x103,
        (
            "#6P#0206F罗伊德前辈好狡猾。\x02\x03",

            "#0211F我想，和这孩子接触的机会，\x01",
            "应该平等地分给大家啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0xA,
        "#6P#1100F哎～？\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x101,
        "#0011F#11P那个，这是什么意思嘛？\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#0309F#11P哈哈，你好像被嫉恨啦。\x02\x03",

            "说起来，这些天，你好像\x01",
            "一直都是和阿琪一起睡的吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0766
    ChrTalk(
        0x101,
        (
            "#0006F#5P不，那是琪雅\x01",
            "她擅自爬到我的床上……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0767
    ChrTalk(
        0x101,
        (
            "#0001F#11P──那个，琪雅，\x01",
            "我们都给你准备好单独的房间了，\x01",
            "你要一个人乖乖睡哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xA,
        (
            "#6P#1106F可是，和罗伊德一起睡，\x01",
            "我总觉得很安心嘛。\x02\x03",

            "#1112F如果给你添麻烦了，\x01",
            "那我以后就不再这样了……\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x101,
        (
            "#0011F#11P不不，没有……\x01",
            "也并没有添什么麻烦啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x102,
        (
            "#0101F喂，罗伊德……\x01",
            "你也太冷淡了吧。\x02\x03",

            "她刚刚经历过那种遭遇，\x01",
            "肯定还会感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x103,
        (
            "#6P#0211F她只是想和你一起睡而已，\x01",
            "这点事情总该承担得起吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0772
    ChrTalk(
        0x101,
        "#0012F#11P你们到底希望我怎么做啊！？\x02",
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x8,
        (
            "#5P#1002F呵呵……\x01",
            "算了，你就暂时多陪陪她吧。\x02\x03",

            "#1003F至于外出嘛……\x01",
            "保险起见，还是再加一个人一起去吧。\x02\x03",

            "#1000F鲁巴彻虽然表示要休战和解，\x01",
            "但我们还是小心一点比较好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0774
    ChrTalk(
        0x101,
        (
            "#0005F#11P啊……\x02\x03",

            "#0000F明白了，\x01",
            "我们会小心的。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0x7D0)
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_E3(0xA)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_E3(0xB)
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
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
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
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 14350, 850, 12060, 180)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0775
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要选择谁作为同行者呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【邀请艾莉同行】\x01",      # 0
            "【邀请缇欧同行】\x01",      # 1
            "【邀请兰迪同行】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_169FB"),
        (1, "loc_16A1C"),
        (2, "loc_16A3D"),
        (SWITCH_DEFAULT, "loc_16A5E"),
    )


    label("loc_169FB")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Call(0, 41)
    Jump("loc_16A5E")

    label("loc_16A1C")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 5)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    Call(0, 42)
    Jump("loc_16A5E")

    label("loc_16A3D")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 6)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Call(0, 43)
    Jump("loc_16A5E")

    label("loc_16A5E")

    Return()

    # Function_38_13E21 end

    def Function_39_16A5F(): pass

    label("Function_39_16A5F")


    def lambda_16A64():
        OP_96(0xFE, 0x3E98F, 0x0, 0x107AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16A64)
    Sleep(300)

    def lambda_16A81():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16A81)
    WaitChrThread(0x102, 1)
    Sound(820, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    def lambda_16AB3():
        OP_96(0xFE, 0x3E98F, 0x0, 0x10428, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16AB3)
    WaitChrThread(0x102, 1)

    def lambda_16AD1():
        OP_93(0xA, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16AD1)
    WaitChrThread(0xA, 2)

    def lambda_16AE2():
        OP_93(0xA, 0xB5, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16AE2)
    WaitChrThread(0xA, 2)
    OP_63(0xA, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    Return()

    # Function_39_16A5F end

    def Function_40_16B0A(): pass

    label("Function_40_16B0A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16B28")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_40_16B0A")

    label("loc_16B28")

    Return()

    # Function_40_16B0A end

    def Function_41_16B29(): pass

    label("Function_41_16B29")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x1, 0xEF, 0xFF)
    OP_68(1000, 1000, 3700, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 200, 0, 2200, 90)
    SetChrPos(0x102, 1800, 0, 2200, 270)
    SetChrPos(0x153, 1000, 0, 3800, 180)
    Sleep(1000)
    OP_68(1000, 1000, 2700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0776
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "我们这就出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x102,
        (
            "#0104F#11P目标是东街的游击士协会哦。\x02\x03",

            "#0100F还是不要去其它地方\x01",
            "闲逛比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x101,
        (
            "#6P#0003F不，说不定某些场所\x01",
            "正是能使琪雅恢复记忆的契机呢。\x02\x03",

            "#0000F虽然确实需要小心……\x01",
            "但只是去一趟协会而已，在来回的路上，\x01",
            "我们就算到处闲逛一下，应该也没有关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x102,
        "#0102F#11P原来如此，也有道理。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)

    def lambda_16D13():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16D13)
    Sleep(300)

    #C0780
    ChrTalk(
        0x102,
        (
            "#0109F呵呵，小琪雅，\x01",
            "那我们这就出门好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x153,
        (
            "#1109F#5P嗯！\x02\x03",

            "#1105F不过，要去哪里呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#0103F嗯～\x01",
            "是一个叫做游击士协会的地方……\x02\x03",

            "#0100F你应该没听说过那里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x153,
        (
            "#1103F#5P游～击士……\x02\x03",

            "#1100F……那个，那些人莫非\x01",
            "就是所谓的正义的同伴？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0784
    ChrTalk(
        0x101,
        (
            "#12P#0005F怎么，原来你知道吗？\x02\x03",

            "#0000F看来这种程度的一般常识\x01",
            "倒是还记得呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x102,
        "#0100F嗯，看来是这样呢。\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x153,
        (
            "#1100F#5P嘿嘿嘿……\x01",
            "虽然不知道为什么要去那里。\x02\x03",

            "#1109F但只要和罗伊德还有艾莉在一起，\x01",
            "琪雅不管去哪里都可以！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0787
    ChrTalk(
        0x101,
        "#12P#0011F唔……\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0788
    ChrTalk(
        0x102,
        (
            "#0109F………啊啊，真是的………！\x01",
            "为什么会如此可爱啊……！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0789
    ChrTalk(
        0x153,
        "#1109F#5P#4S那我们就快点出发啦～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 2000, 180)
    SetScenarioFlags(0xA7, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x47, 0x1, 0x13)
    OP_29(0x48, 0x4, 0x2)
    OP_29(0x48, 0x1, 0x0)
    VolumeBGM(0x64, 0x7D0)
    EventEnd(0x5)
    Return()

    # Function_41_16B29 end

    def Function_42_1703F(): pass

    label("Function_42_1703F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x2, 0xEF, 0xFF)
    OP_68(1000, 1000, 3700, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 200, 0, 2200, 90)
    SetChrPos(0x103, 1800, 0, 2200, 270)
    SetChrPos(0x153, 1000, 0, 3800, 180)
    Sleep(1000)
    OP_68(1000, 1000, 2700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0790
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "我们这就出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x103,
        (
            "#0204F#11P是东街的游击士协会哦。\x02\x03",

            "#0201F……果然还是不要\x01",
            "去其它的地方闲逛比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x101,
        (
            "#6P#0003F不，说不定某些场所\x01",
            "正是能使琪雅恢复记忆的契机呢。\x02\x03",

            "#0000F虽然确实需要小心……\x01",
            "但只是去一趟协会而已，在来回的路上，\x01",
            "我们就算到处闲逛一下，应该也没有关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x103,
        "#0204F#11P原来如此，有道理哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x153, 500)

    def lambda_1722F():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1722F)
    Sleep(300)

    #C0794
    ChrTalk(
        0x103,
        (
            "#0202F……那，琪雅，\x01",
            "我们这就出发，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x153,
        (
            "#1109F#5P嗯！\x02\x03",

            "#1105F不过，要去哪里呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x103,
        (
            "#0205F是一个叫做游击士协会的地方……\x02\x03",

            "#0206F要对琪雅解释起来的话，\x01",
            "可能会有一点困难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x153,
        (
            "#1103F#5P游～击士……\x02\x03",

            "#1100F……那个，那些人莫非\x01",
            "就是所谓的正义的同伴？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0798
    ChrTalk(
        0x101,
        (
            "#12P#0005F怎么，原来你知道吗？\x02\x03",

            "#0000F看来这种程度的一般常识\x01",
            "倒是还记得呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x103,
        (
            "#0202F是啊……\x02\x03",

            "#0204F这毕竟没有涉及到\x01",
            "比较复杂的长期记忆。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x153,
        (
            "#1100F#5P嘿嘿嘿……\x01",
            "虽然不知道为什么要去那里。\x02\x03",

            "#1109F但只要和罗伊德还有缇欧在一起，\x01",
            "琪雅不管去哪里都可以！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0801
    ChrTalk(
        0x101,
        "#12P#0011F唔……\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0802
    ChrTalk(
        0x103,
        (
            "#0209F……这种笑脸，也太犯规了吧，\x01",
            "简直让人完全无法抵抗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0803
    ChrTalk(
        0x153,
        "#1109F#5P#4S那我们就快点出发啦～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 2000, 180)
    SetScenarioFlags(0xA7, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x47, 0x1, 0x13)
    OP_29(0x48, 0x4, 0x2)
    OP_29(0x48, 0x1, 0x1)
    VolumeBGM(0x64, 0x7D0)
    EventEnd(0x5)
    Return()

    # Function_42_1703F end

    def Function_43_17590(): pass

    label("Function_43_17590")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x3, 0xEF, 0xFF)
    OP_68(1000, 1000, 3700, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 200, 0, 2200, 90)
    SetChrPos(0x104, 1800, 0, 2200, 270)
    SetChrPos(0x153, 1000, 0, 3800, 180)
    Sleep(1000)
    OP_68(1000, 1000, 2700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0804
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "我们这就出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x104,
        (
            "#0304F#11P是东街的游击士协会啊。\x02\x03",

            "#0301F怎么样？果然还是应该\x01",
            "直奔目标，不要去别处乱逛吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x101,
        (
            "#6P#0003F不，说不定某些场所\x01",
            "正是能使琪雅恢复记忆的契机呢。\x02\x03",

            "#0000F虽然确实需要小心……\x01",
            "但只是去一趟协会而已，在来回的路上，\x01",
            "我们就算到处闲逛一下，应该也没有关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x104,
        (
            "#0300F#11P原来如此。\x02\x03",

            "#0309F算啦，反正你我都在，\x01",
            "不管遇到什么情况都没关系吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x153, 500)

    def lambda_177B5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_177B5)
    Sleep(300)

    #C0808
    ChrTalk(
        0x104,
        (
            "#0302F好啦～阿琪，\x01",
            "我们这就出发吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x153,
        (
            "#1109F#5P嗯！\x02\x03",

            "#1105F不过，要去哪里呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x104,
        (
            "#0305F刚才说了啊，是游击士协会……\x02\x03",

            "#0302F不过你应该没听说过\x01",
            "那种地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x153,
        (
            "#1103F#5P游～击士……\x02\x03",

            "#1100F……那个，那些人莫非\x01",
            "就是所谓的正义的同伴？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0812
    ChrTalk(
        0x101,
        (
            "#12P#0005F怎么，原来你知道吗？\x02\x03",

            "#0000F看来这种程度的一般常识\x01",
            "倒是还记得呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x104,
        "#0300F嗯，看来是这样。\x02",
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x153,
        (
            "#1100F#5P嘿嘿嘿……\x01",
            "虽然不知道为什么要去那里。\x02\x03",

            "#1109F但只要和罗伊德还有兰迪在一起，\x01",
            "琪雅不管去哪里都可以！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0815
    ChrTalk(
        0x101,
        "#12P#0011F唔……\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0816
    ChrTalk(
        0x104,
        (
            "#0306F……为孩子而烦恼的父亲是什么心情，\x01",
            "我现在好像稍微有点明白了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0817
    ChrTalk(
        0x153,
        "#1109F#5P#4S那我们就快点出发啦～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 2000, 180)
    SetScenarioFlags(0xA7, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x47, 0x1, 0x13)
    OP_29(0x48, 0x4, 0x2)
    OP_29(0x48, 0x1, 0x2)
    VolumeBGM(0x64, 0x7D0)
    EventEnd(0x5)
    Return()

    # Function_43_17590 end

    def Function_44_17AE3(): pass

    label("Function_44_17AE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x8, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("apl/ch50092.itc", 0x21)
    LoadChrToIndex("chr/ch00802.itc", 0x22)
    LoadChrToIndex("chr/ch08201.itc", 0x23)
    LoadChrToIndex("apl/ch50380.itc", 0x24)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(821)
    OP_32(0x8, 0x0, 0x1D)
    RemoveCraft(0x8, 0xFFFF)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x8, 0x81, 0x2)
    OP_38(0x8, 0x82, 0x2)
    OP_38(0x8, 0x83, 0x2)
    OP_38(0x8, 0x84, 0x2)
    OP_38(0x8, 0x85, 0x2)
    OP_38(0x8, 0x86, 0x2)
    OP_42(0x8, 0x44D, 0xFF)
    OP_42(0x8, 0x5E9, 0xFF)
    OP_42(0x8, 0x64D, 0xFF)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0x122)
    SetChrChipPat(0x8, 0x6, 0x122)
    AddCraft(0x8, 0x144)
    OP_42(0x8, 0x6F, 0x0)
    OP_42(0x8, 0x92, 0x4)
    OP_42(0x8, 0x7B, 0x3)
    OP_42(0x8, 0x81, 0x2)
    OP_42(0x8, 0x65, 0x1)
    OP_42(0x8, 0x6B, 0x6)
    OP_42(0x8, 0xAC, 0x5)
    OP_68(900, 1000, 400, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 800, 0, 500, 0)
    SetChrPos(0x102, 800, 0, 500, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    OP_90(0xA, 800, 3000, 14000, 180)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis080.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis081.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis082.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01103.itp")
    OP_68(900, 1000, 2400, 2000)
    SetCameraDistance(25500, 2000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_17D39():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17D39)

    def lambda_17D53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17D53)
    Sleep(250)

    def lambda_17D67():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17D67)

    def lambda_17D81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17D81)
    Sleep(400)

    def lambda_17D95():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17D95)

    def lambda_17DAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_17DAF)
    Sleep(250)

    def lambda_17DC3():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17DC3)

    def lambda_17DDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_17DDD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0818
    ChrTalk(
        0x101,
        "#0000F#12P我们回来了～\x02",
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x104,
        "#0309F#12P回来啦～\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    #Sound(2036, 255, 90, 0)    #voice#KeA

    #C0820
    ChrTalk(
        0xA,
        "#4P#1110F啊，你们回来了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(800, 1900, 8000, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    BeginChrThread(0xA, 3, 0, 45)

    def lambda_17E9D():

        label("loc_17E9D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_17E9D")

    QueueWorkItem2(0x102, 2, lambda_17E9D)

    def lambda_17EAF():

        label("loc_17EAF")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_17EAF")

    QueueWorkItem2(0x104, 2, lambda_17EAF)
    Sleep(1000)
    Sound(2037, 255, 100, 0)    #voice#KeA
    WaitChrThread(0xA, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)

    #C0821
    ChrTalk(
        0x101,
        (
            "#12P#0014F哈哈，撞得好准呢。\x02\x03",

            "#0002F我们回来啦，琪雅。\x01",
            "今天有没有乖乖的啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0822
    AnonymousTalk(
        0xA,
        (
            "#5P嗯～！\x02\x03",

            "琪雅一直都和蔡特一起\x01",
            "乖乖看家呢。\x02\x03",

            "图书馆的书也已经\x01",
            "读完三册了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0823
    ChrTalk(
        0x101,
        "#12P#0005F嘿，那可真是厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x102,
        (
            "#0102F#11P呵呵，虽然是儿童读物，\x01",
            "但一上午居然能看完三本。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x103,
        (
            "#0204F#12P这个孩子似乎\x01",
            "拥有相当惊人的\x01",
            "情报处理能力呢……\x02\x03",

            "#0202F非常期待她将来的表现啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x104,
        (
            "#0306F#11P真是的，你们整天只知道\x01",
            "凑在一起哄小孩啊。\x02\x03",

            "#0302F哈，不过我好像也没资格说别人吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)

    def lambda_18106():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18106)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x40)

    #C0827
    ChrTalk(
        0xA,
        (
            "#1105F#5P哎～？\x02\x03",

            "#1110F比起那个，\x01",
            "琪雅的肚子饿啦。\x02\x03",

            "#1109F快点做午饭吃吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x101,
        "#12P#0002F哈哈，好啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0829
    ChrTalk(
        0x101,
        (
            "#6P#0000F今天轮到我做饭了。\x01",
            "各位，吃薏面可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x102,
        "#0102F#11P嗯，好啊。\x02",
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x103,
        (
            "#12P#0204F只要是罗伊德前辈做的，\x01",
            "不管是什么都可以。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x104,
        "#0309F#11P要给我多盛一些啊。\x02",
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x101,
        "#6P#0002F哈哈，知道啦。\x02",
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0xA,
        (
            "#1105F#5P罗伊德来做饭吗？\x02\x03",

            "#1109F那琪雅也要帮忙～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_182ED():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_182ED)
    Sleep(300)

    #C0835
    ChrTalk(
        0x102,
        (
            "#0105F#11P小琪雅……\x01",
            "难道你做过料理吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x103,
        (
            "#12P#0200F莫非是，\x01",
            "想起什么了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0xA,
        (
            "#1100F#5P刚才看的那本书里\x01",
            "有个厨师呢～\x02\x03",

            "他做出来的料理\x01",
            "很～好吃呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x104,
        "#0302F#11P哈哈，原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么，既然难得琪雅有兴致，\x01",
            "就来帮帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0xA,
        "#1109F#5P嗯～要上啦～！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(116700, 1200, 6000, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 116700, 30, 7600, 0)
    SetChrPos(0xA, 116700, 30, 6400, 0)
    OP_68(116700, 1200, 7000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0841
    ChrTalk(
        0x101,
        (
            "#0003F#11P那么……\x01",
            "要做哪种薏面呢？\x02\x03",

            "#0000F这里有阿尔摩利卡产的\x01",
            "鸡蛋和培根，\x01",
            "做熏肉鸡蛋乳酪面应该不错……\x02\x03",

            "另外也有利贝尔产的蛤蜊罐头，\x01",
            "也可以做蛤蜊面呢。\x02\x03",

            "#0005F啊，还是用\x01",
            "茄子和肉酱来做比较好？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0842
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要做什么呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【熏肉鸡蛋乳酪面】\x01",      # 0
            "【蛤蜊面】\x01",              # 1
            "【茄子肉酱面】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18603"),
        (1, "loc_1865C"),
        (2, "loc_186A9"),
        (SWITCH_DEFAULT, "loc_18704"),
    )


    label("loc_18603")


    #C0843
    ChrTalk(
        0x101,
        (
            "#0000F#11P好，机会难得，\x01",
            "趁着还新鲜，就把这些鸡蛋用掉吧。\x02\x03",

            "那么，接下来──\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18704")

    label("loc_1865C")


    #C0844
    ChrTalk(
        0x101,
        (
            "#0000F#11P好，机会难得，\x01",
            "就把蛤蜊罐头用掉吧。\x02\x03",

            "那么，接下来──\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18704")

    label("loc_186A9")


    #C0845
    ChrTalk(
        0x101,
        (
            "#0000F#11P好，正好有些肉末，\x01",
            "马上将它和茄子一起做成肉酱吧。\x02\x03",

            "那么，接下来──\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18704")

    label("loc_18704")


    #C0846
    ChrTalk(
        0xA,
        (
            "#11P#1110F那个～那个～罗伊德。\x02\x03",

            "琪雅可以帮你做什么呢～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(300)

    #C0847
    ChrTalk(
        0x101,
        (
            "#0002F#5P那么，就去帮我把\x01",
            "刚刚说过的材料给拿来好吗？\x02\x03",

            "我来准备\x01",
            "煮面条。\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0xA,
        "#11P#1109F没问题～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(122700, 1000, 8300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 123700, 30, 8300, 0)
    SetChrPos(0xA, 122700, 30, 8300, 0)
    ClearMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x9)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 123100, 800, 9300, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetMapObjFrame(0xF, "pan00", 0x1, 0x1)
    SetMapObjFrame(0xF, "pan01", 0x0, 0x1)
    SetMapObjFrame(0xF, "kemuri2_add", 0x0, 0x1)
    Sleep(500)
    OP_68(123700, 1000, 8300, 2000)
    Sound(84, 0, 70, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0849
    ChrTalk(
        0xA,
        "#12P#1100F（开心……激动……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0850
    ChrTalk(
        0xA,
        (
            "#6P#1101F喂～喂～罗伊德，\x01",
            "还没做好吗～！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_189AB")

    #C0851
    ChrTalk(
        0x101,
        (
            "#11P#0004F还要再等一下哦。\x01",
            "煮面条时，最重要的就是火候了。\x02\x03",

            "#0000F在火候正好时将面条捞出，\x01",
            "然后在平底锅里把肉、蛋和面条拌好，\x01",
            "最后再撒上胡椒粉……\x02\x03",

            "#0014F这样就算是大功告成啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B50")

    label("loc_189AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18A7E")

    #C0852
    ChrTalk(
        0x101,
        (
            "#11P#0004F还要再等一下哦。\x01",
            "煮面条时，最重要的就是火候了。\x02\x03",

            "#0000F在火候正好时将面条捞出，\x01",
            "然后在平底锅里把蛤蜊、酱汁和面条拌好，\x01",
            "最后再放上大蒜和香芹做调味料……\x02\x03",

            "#0014F这样就算是大功告成啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B50")

    label("loc_18A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18B50")

    #C0853
    ChrTalk(
        0x101,
        (
            "#11P#0004F还要再等一下哦。\x01",
            "煮面条时，最重要的就是火候了。\x02\x03",

            "#0000F在火候正好时将面条捞出，\x01",
            "然后在平底锅里把肉酱和面条拌好，接下来再放入\x01",
            "炸熟的茄子，最后撒上乳酪粉……\x02\x03",

            "#0014F这样就算是大功告成啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B50")


    #C0854
    ChrTalk(
        0xA,
        (
            "#6P#1105F嘿～……\x02\x03",

            "#1110F那，接下来就让\x01",
            "琪雅试试看吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xA, 500)

    #C0855
    ChrTalk(
        0x101,
        (
            "#11P#0005F哎，没问题吗？\x02\x03",

            "#0004F（虽然觉得她应该做不好……不过算了，\x01",
            "  只要有我在一旁帮忙就没问题了吧。）\x02\x03",

            "#0000F好，那你就试试看吧。\x02\x03",

            "不过可要小心，别被火烫伤了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0xA,
        "#6P#1109F嗯～！\x02",
    )

    CloseMessageWindow()
    OP_68(124090, 1000, 8260, 1500)

    def lambda_18C7E():
        OP_96(0xFE, 0x1E780, 0x1E, 0x206C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18C7E)
    Sleep(300)

    def lambda_18C9B():
        OP_96(0xFE, 0x1E334, 0x1E, 0x206C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18C9B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(300)

    #C0857
    ChrTalk(
        0xA,
        (
            "#1101F#11P#30W那个……\x02\x03",

            "#30W在火候正好时将面条捞出，\x01",
            "然后在平底锅里……\x02\x03",

            "#1105F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 20000)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    #C0858
    ChrTalk(
        0x101,
        (
            "#0006F#11P（果然还是太勉强了啊……）\x02\x03",

            "#0000F（不过没关系，只要是琪雅做的，\x01",
            "  即使有些失败，大家也都会很开心的──）\x02",
        )
    )

    CloseMessageWindow()
    Sound(931, 0, 80, 0)
    VolumeBGM(0x3C, 0x3E8)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1200)
    #Sound(2038, 255, 100, 0)    #voice#KeA

    #C0859
    ChrTalk(
        0xA,
        "#11P#1103F#30W───嗯，我明白啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0860
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅用相当娴熟的动作\x01",
            "将已经煮熟的面条从锅中捞起，\x01",
            "随后放到平底锅里进行烹调。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0861
    ChrTalk(
        0x101,
        "#0011F#11P哎……！？\x02",
    )

    CloseMessageWindow()
    Sound(81, 0, 100, 0)
    Sleep(300)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(20500, 0)
    SetMapObjFrame(0xF, "pan00", 0x0, 0x1)
    SetMapObjFrame(0xF, "pan01", 0x1, 0x1)
    SetMapObjFrame(0xF, "kemuri2_add", 0x1, 0x1)
    OP_0D()
    OP_6F(0x10)
    CancelBlur(0)
    StopEffect(0x0, 0x2)
    VolumeBGM(0x64, 0x3E8)
    Sleep(1300)
    #Sound(2039, 255, 100, 0)    #voice#KeA
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0862
    ChrTalk(
        0xA,
        "#11P#1109F#4S嗯，做好啦～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18FC1")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jump("loc_19024")

    label("loc_18FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18FF5")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Jump("loc_19024")

    label("loc_18FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_19024")
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    label("loc_19024")

    Sleep(1000)

    #A0863
    AnonymousTalk(
        0x101,
        (
            "#0005F噢噢……\x01",
            "很厉害啊！琪雅！？\x02\x03",

            "你的烹饪技术实在是太好了，\x01",
            "不过，到底是怎么掌握的啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0xA, 0x101, 500)

    #A0864
    AnonymousTalk(
        0xA,
        (
            "#1104F嘿嘿嘿～\x01",
            "不知道是怎么回事，脑中突然就灵光一闪。\x02\x03",

            "#1110F我的做法，没有弄错吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19123")
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jump("loc_19186")

    label("loc_19123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19157")
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Jump("loc_19186")

    label("loc_19157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_19186")
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    label("loc_19186")


    #C0865
    ChrTalk(
        0x101,
        (
            "#0004F#11P完全没有，不如说\x01",
            "比我的技术还要好呢。\x02\x03",

            "#0000F琪雅……你是不是……\x01",
            "以前曾经做过料理呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0xA,
        (
            "#6P#1111F嗯～有过那种事吗？\x02\x03",

            "#1109F算啦，不管了，肚子已经很饿了，\x01",
            "快去拿给大家吃吧～！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x104, 13900, 900, 4600, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x103, 11300, 900, 2550, 90)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 11300, 900, 4600, 90)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16000, 850, 6400, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 1, 0, 40)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12400, 1400, 2600, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0xC)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12000, 1300, 2600, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 13000, 1400, 2600, 0)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0xE)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13400, 1300, 2600, 0)
    SetChrChipByIndex(0x25, 0x20)
    SetChrSubChip(0x25, 0x7)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12700, 1400, 5500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x7)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 12700, 1400, 3500, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x21)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 16000, 750, 5500, 0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19634")
    SetChrSubChip(0x19, 0xC)
    SetChrSubChip(0x1B, 0xC)
    SetChrSubChip(0x1D, 0xC)
    SetChrSubChip(0x1F, 0xC)
    SetChrSubChip(0x21, 0xC)
    SetChrSubChip(0x23, 0xC)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x19, 13100, 1400, 6600, 0)
    SetChrPos(0x1B, 12300, 1400, 6600, 0)
    SetChrPos(0x1D, 13100, 1400, 4600, 0)
    SetChrPos(0x1F, 12300, 1400, 4600, 0)
    SetChrPos(0x21, 12300, 1400, 2600, 0)
    SetChrPos(0x23, 13100, 1400, 2600, 0)
    Jump("loc_1967B")

    label("loc_19634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1965A")
    SetChrSubChip(0x19, 0xE)
    SetChrSubChip(0x1B, 0xE)
    SetChrSubChip(0x1D, 0xE)
    SetChrSubChip(0x1F, 0xE)
    SetChrSubChip(0x21, 0xE)
    SetChrSubChip(0x23, 0xE)
    Jump("loc_1967B")

    label("loc_1965A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1967B")
    SetChrSubChip(0x19, 0xA)
    SetChrSubChip(0x1B, 0xA)
    SetChrSubChip(0x1D, 0xA)
    SetChrSubChip(0x1F, 0xA)
    SetChrSubChip(0x21, 0xA)
    SetChrSubChip(0x23, 0xA)

    label("loc_1967B")

    Sleep(1000)
    OP_68(12600, 2350, 4800, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_68(12600, 1850, 4800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19810")

    #C0867
    ChrTalk(
        0x104,
        (
            "#0305F#11P喂喂，这实在是相当美味啊！\x02\x03",

            "这真的是阿琪\x01",
            "做的吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0868
    ChrTalk(
        0x101,
        (
            "#5P#0004F面条下锅之前的准备工作\x01",
            "虽然是我做的……\x02\x03",

            "#0002F但下锅以后的全部烹调工作\x01",
            "都是琪雅一个人完成的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0869
    ChrTalk(
        0x103,
        "#12P#0202F好厉害……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0870
    ChrTalk(
        0x102,
        (
            "#0109F#5P嗯……\x01",
            "这味道简直可以与餐厅里的相媲美了。\x02\x03",

            "#0102F小琪雅，你实在是太厉害了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A6F")

    label("loc_19810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19945")

    #C0871
    ChrTalk(
        0x102,
        (
            "#0105F#5P好、好美味……\x02\x03",

            "这……这真的是小琪雅\x01",
            "做出来的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x101,
        (
            "#11P#0004F面条下锅之前的准备工作\x01",
            "虽然是我做的……\x02\x03",

            "#0000F但下锅以后的全部烹调工作\x01",
            "都是琪雅一个人完成的。\x02",
        )
    )

    CloseMessageWindow()

    #C0873
    ChrTalk(
        0x104,
        "#0305F#11P真的假的啊……！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0874
    ChrTalk(
        0x103,
        (
            "#12P#0204F这已经可以与餐厅的料理一较高下了……\x02\x03",

            "#0202F琪雅，干得漂亮啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A6F")

    label("loc_19945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_19A6F")
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0875
    ChrTalk(
        0x103,
        (
            "#12P#0205F……真美味……\x02\x03",

            "这个，真的是\x01",
            "琪雅做的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    #C0876
    ChrTalk(
        0x101,
        (
            "#5P#0000F面条下锅之前的准备工作\x01",
            "虽然是我做的……\x02\x03",

            "但下锅以后的全部烹调工作\x01",
            "都是琪雅一个人完成的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0877
    ChrTalk(
        0x102,
        "#0102F#5P厉、厉害……\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x104,
        (
            "#0305F#11P哎呀，这绝对达到了\x01",
            "餐厅厨师的水平啊。\x02\x03",

            "#0309F阿琪，你很有一套嘛！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A6F")


    #C0879
    ChrTalk(
        0xA,
        (
            "#6P#1109F嘿嘿嘿～\x01",
            "大家觉得好吃就好啦～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0880
    ChrTalk(
        0x101,
        (
            "#5P#0000F莫非琪雅是……\x01",
            "厨师家的孩子吗？\x02\x03",

            "#0006F如果她的父母健在，\x01",
            "现在肯定担心得不得了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x102,
        (
            "#0103F#5P……是啊。\x01",
            "不过，这也没办法呢。\x02\x03",

            "#0108F都已经借助了游击士协会的情报网，\x01",
            "却仍然没能查到任何情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x103,
        (
            "#6P#0208F是出身于非常偏僻的边境地区呢，\x01",
            "还是有什么隐情……\x02",
        )
    )

    CloseMessageWindow()

    #C0883
    ChrTalk(
        0xA,
        "#6P#1100F嗯～？\x02",
    )

    CloseMessageWindow()

    #C0884
    ChrTalk(
        0x104,
        (
            "#0306F#11P算了吧，要是真的开始考虑那些问题，\x01",
            "可就没完没了了。\x02\x03",

            "#0300F在找到线索之前，就把她\x01",
            "当成是我们的孩子，这不也很好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x101,
        (
            "#5P#0004F是啊……\x02\x03",

            "#0002F──哈哈，不过科长他\x01",
            "居然不在，还真是不走运啊。\x02\x03",

            "难得有机会可以吃到琪雅亲手\x01",
            "做的料理，他却白白错过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x103,
        (
            "#6P#0200F科长是在警察局总部开会吗……\x01",
            "最近，会议似乎有些频繁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0887
    ChrTalk(
        0x102,
        "#0105F#5P是啊……莫非是出了什么事吗？\x02",
    )

    CloseMessageWindow()
    Sound(821, 2, 100, 0)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    OP_70(0xD, 0x0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x14, 0x0, 0x20)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0xA, 0x1)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0888
    ChrTalk(
        0x101,
        "#11P#0005F有通讯联络……是谁呢？\x02",
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x104,
        (
            "#0300F#11P没有直接拨打艾尼格玛，\x01",
            "看来应该不是科长或小芙兰啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 14100, 850, 7600, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_92(0x101, 0x35E8, 0x2EE0, 0x1F4)
    OP_68(13800, 1850, 12000, 2500)

    def lambda_19E97():
        OP_95(0xFE, 13800, 850, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19E97)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x1)
    ClearMapObjFlags(0xD, 0x20)
    OP_70(0xD, 0x32)
    OP_24(0x335)
    Sound(822, 0, 100, 0)
    FadeToDark(500, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0890
    AnonymousTalk(
        0x101,
        (
            "#0000F您好，这里是克洛斯贝尔警察局·特别\x01",
            "任务支援科。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女孩的声音")

    #A0891
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德警官吗？\x02\x03",

            "那个……我是诺艾尔，\x01",
            "就是警备队的希卡上士。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0892
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0009F啊，好久不见，\x01",
            "大概有一个月了吧。\x02\x03",

            "#0002F怎么了？\x01",
            "有什么任务要委托给支援科吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0893
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，其实是……\x02\x03",

            "我个人有些私事想与\x01",
            "支援科的各位商量一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0894
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F要商量私事……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0895
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，虽然是私事，\x01",
            "但应该也属于工作的范畴……\x02\x03",

            "那个，很抱歉，\x01",
            "这么突然和你们联络……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0896
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F哪里，现在正好是午休时间，\x01",
            "没关系的。\x02\x03",

            "#0001F你现在在哪里呢？\x01",
            "方便的话，就直接过来和我们面谈如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0897
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "真、真的吗？\x02\x03",

            "我现在正好就在\x01",
            "克洛斯贝尔市的北出口。\x02\x03",

            "那么，我可以马上前去拜访吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0898
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F嗯，没问题，我们会在这里等你。\x02\x03",

            "#0005F对了，如果愿意的话，\x01",
            "就来和我们一起吃午餐吧？\x02\x03",

            "我们准备了一些简单的薏面，\x01",
            "如果不嫌弃，就来一起吃吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0899
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，不用，那倒是不必……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(932, 0, 100, 0)
    Sleep(1300)
    #Sound(1496, 255, 100, 0)    #voice#Noel
    Sleep(800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0900
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S……不好意思……\x01",
            "还是麻烦你们吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0901
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002F哈哈，了解。\x01",
            "那就快点过来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0902
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    SetMapObjFlags(0xD, 0x4)
    Sound(822, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_68(12600, 1850, 4800, 2500)

    def lambda_1A3C9():
        OP_95(0xFE, 14100, 850, 7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A3C9)
    WaitChrThread(0x101, 1)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    #C0903
    ChrTalk(
        0x102,
        "#0105F#6P是谁打来的啊？\x02",
    )

    CloseMessageWindow()

    #C0904
    ChrTalk(
        0x101,
        (
            "#11P#0000F啊，是诺艾尔上士。\x02\x03",

            "好像是有什么事情\x01",
            "想来和我们商量……\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0x104,
        (
            "#0305F#11P哎～\x01",
            "这可真少见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0xA,
        "#6P#1110F怎么了怎么了，有谁要来吗～？\x02",
    )

    CloseMessageWindow()

    #C0907
    ChrTalk(
        0x103,
        "#12P#0204F嗯，是警备队的大姐姐哦。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    #C0908
    ChrTalk(
        0xA,
        "#6P#1105F警～备～队？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0909
    ChrTalk(
        0x101,
        (
            "#5P#0002F她好像还没吃午饭呢，\x01",
            "再去多煮一份面条吧。\x02\x03",

            "琪雅，还要来帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0910
    ChrTalk(
        0xA,
        "#6P#1109F嗯！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(13090, 1850, 5300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 13900, 900, 6650, 270)
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrSubChip(0x101, 0x2)
    SetChrPos(0x104, 13900, 900, 2550, 270)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0x18)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1300, 7250, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0x18)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 7250, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x18)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13100, 1300, 5200, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x18)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12300, 1300, 5200, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0x18)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12300, 1300, 3150, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x18)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13100, 1300, 3150, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A787")
    SetChrSubChip(0x19, 0xD)
    SetChrSubChip(0x1B, 0xD)
    SetChrSubChip(0x1D, 0xD)
    SetChrSubChip(0x1F, 0xD)
    SetChrSubChip(0x21, 0xD)
    SetChrSubChip(0x23, 0xD)
    Jump("loc_1A7CE")

    label("loc_1A787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A7AD")
    SetChrSubChip(0x19, 0xF)
    SetChrSubChip(0x1B, 0xF)
    SetChrSubChip(0x1D, 0xF)
    SetChrSubChip(0x1F, 0xF)
    SetChrSubChip(0x21, 0xF)
    SetChrSubChip(0x23, 0xF)
    Jump("loc_1A7CE")

    label("loc_1A7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A7CE")
    SetChrSubChip(0x19, 0xB)
    SetChrSubChip(0x1B, 0xB)
    SetChrSubChip(0x1D, 0xB)
    SetChrSubChip(0x1F, 0xB)
    SetChrSubChip(0x21, 0xB)
    SetChrSubChip(0x23, 0xB)

    label("loc_1A7CE")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16500, 850, 6400, 225)
    ClearChrFlags(0xC, 0x1)
    OP_CA(0x1, 0x3, 0x0)
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis160.itp")
    Sleep(1000)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0911
    ChrTalk(
        0x109,
        "#11P#0504F多谢款待。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0912
    ChrTalk(
        0x109,
        (
            "#5P#0502F──真是太好吃了！\x01",
            "这真是小琪雅做的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0913
    ChrTalk(
        0xA,
        (
            "#6P#1100F嗯，是呀～\x02\x03",

            "#1105F不过下锅之前的……准备工作\x01",
            "是罗伊德做的～\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x109,
        (
            "#5P#0509F哈哈，那你也已经很厉害啦！\x02\x03",

            "#0504F嗯～关于小琪雅的事情，\x01",
            "我从芙兰那里也听说了不少……\x02\x03",

            "#0502F没想到不仅可爱，\x01",
            "而且还身怀这种绝技呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0915
    ChrTalk(
        0x101,
        (
            "#0002F#11P哈哈，芙兰她好像\x01",
            "非常喜欢琪雅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x103,
        (
            "#6P#0204F#N每次通过终端联络时，\x01",
            "她都要我们把琪雅叫过来\x01",
            "和她说几句话呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0917
    ChrTalk(
        0x109,
        (
            "#5P#0509F啊哈哈，我妹妹\x01",
            "最喜欢可爱的小孩子了……\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0xA,
        (
            "#6P#1110F那个那个，诺艾尔\x01",
            "是芙兰的姐姐吗～？\x02\x03",

            "这么一说，不止是头发的颜色一样，\x01",
            "连长相都非常像呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x109,
        (
            "#5P#0505F是、是吗？\x02\x03",

            "#0502F不过我并不是她那种\x01",
            "可爱的类型啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0920
    ChrTalk(
        0x109,
        (
            "#5P#0503F噢噢……\x01",
            "好险，差点就把正事都给忘了。\x02\x03",

            "#0501F──那个，我这就开始\x01",
            "进入正题了，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0921
    ChrTalk(
        0x101,
        "#0001F#11P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()

    #C0922
    ChrTalk(
        0x104,
        (
            "#0301F你要说的事，好像与山道尽头的\x01",
            "某个遗迹有关吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0923
    ChrTalk(
        0x109,
        "#5P#0508F嗯，那是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xDAC)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0924
    AnonymousTalk(
        0x101,
        "#0005F──幽灵出没的遗迹？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0925
    ChrTalk(
        0x109,
        (
            "#5P#0503F……正是。\x02\x03",

            "正确地说，也不知道是幽灵，\x01",
            "还是传说中的妖怪……\x02\x03",

            "#0501F总之，确实是有前所未见的\x01",
            "奇异魔兽在出没……\x02",
        )
    )

    CloseMessageWindow()

    #C0926
    ChrTalk(
        0x104,
        (
            "#0303F当初负责调查那里的\x01",
            "贝尔加德门部队已经撤回了……\x02\x03",

            "#0301F于是就由唐古拉姆门的你们\x01",
            "来负责收拾烂摊子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0927
    ChrTalk(
        0x109,
        (
            "#5P#0501F嗯……\x02\x03",

            "#0506F而且，昨天我和几名队员\x01",
            "试着进去调查了一下……\x02\x03",

            "但出现了很多十分诡异的魔兽，\x01",
            "大家都吓得不轻……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0928
    ChrTalk(
        0x102,
        (
            "#0105F#6P等、等一下。\x02\x03",

            "#0109F……莫非……\x01",
            "是想让我们帮忙驱赶幽灵吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0929
    ChrTalk(
        0x109,
        (
            "#11P#0505F也、也不是啦……\x01",
            "主要目的还是希望你们能彻底\x01",
            "调查一下遗迹内部……\x02\x03",

            "#0506F……果然不行吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0930
    ChrTalk(
        0x101,
        (
            "#0008F#11P嗯、嗯～……\x02\x03",

            "#0003F虽说是要调查遗迹，\x01",
            "但具体应该如何着手，\x01",
            "我们也完全没有头绪啊……\x02\x03",

            "#0000F──但既然你都来找我们了，\x01",
            "想必已经找到一些着手点了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0931
    ChrTalk(
        0x109,
        (
            "#5P#0500F……所料不错，不愧是罗伊德警官啊。\x02\x03",

            "#0503F其实……\x01",
            "在和那些怪物战斗的时候……\x02\x03",

            "#0501F感觉导力魔法的效果特性似乎\x01",
            "与平常有些不同呢。\x02",
        )
    )

    CloseMessageWindow()
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

    #C0932
    ChrTalk(
        0x101,
        "#0013F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0933
    ChrTalk(
        0x102,
        "#0105F#6P这，莫非又是……\x02",
    )

    CloseMessageWindow()

    #C0934
    ChrTalk(
        0x103,
        (
            "#6P#0203F#N和我们以前进入\x01",
            "『星见之塔』时一样……\x02\x03",

            "#0201F时、空、幻这三种上级属性\x01",
            "也在产生影响……是这种感觉吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0935
    ChrTalk(
        0x109,
        (
            "#5P#0506F嗯……\x01",
            "我也想起了那时的事。\x02\x03",

            "所以，我才想是不是应该来\x01",
            "让大家也了解一下情况，听听你们的意见……\x02",
        )
    )

    CloseMessageWindow()

    #C0936
    ChrTalk(
        0x101,
        "#0003F#11P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0937
    ChrTalk(
        0x102,
        "#0106F#6P所以才来支援科……\x02",
    )

    CloseMessageWindow()

    #C0938
    ChrTalk(
        0x109,
        (
            "#5P#0508F各位，我非常理解\x01",
            "你们平时都很忙，可是……\x02\x03",

            "#0506F再这么下去，司令阁下\x01",
            "也许又要下达放置不管的命令了……\x02",
        )
    )

    CloseMessageWindow()

    #C0939
    ChrTalk(
        0x104,
        (
            "#0301F哈，那个只懂鸵鸟政策的司令，\x01",
            "很有可能会那样做吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0940
    ChrTalk(
        0x101,
        "#0003F#11P嗯～……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0941
    ChrTalk(
        0x101,
        (
            "#0000F#11P各位，既然上士特意提出请求，\x01",
            "我们就协助她一下如何？\x02\x03",

            "虽然要跑到市外去执行任务，\x01",
            "但放着不管的话还是稍微有些在意。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0942
    ChrTalk(
        0x102,
        "#0108F#5P也、也有道理啊……\x02",
    )

    CloseMessageWindow()

    #C0943
    ChrTalk(
        0x103,
        "#6P#0204F#N我没有异议。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0944
    ChrTalk(
        0x104,
        (
            "#0304F#11P我也没问题啊。\x02\x03",

            "#0302F不过大小姐看起来\x01",
            "好像有点不太愿意啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0945
    ChrTalk(
        0x102,
        (
            "#0113F#5P才、才没有那种事！\x02\x03",

            "#0112F谁会幼稚到像小孩子\x01",
            "一样害怕幽灵──啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0946
    ChrTalk(
        0x104,
        "#0304F#11P说漏嘴了吗……\x02",
    )

    CloseMessageWindow()

    #C0947
    ChrTalk(
        0xA,
        "#6P#1105F艾莉，害怕幽灵吗～？\x02",
    )

    CloseMessageWindow()

    #C0948
    ChrTalk(
        0x102,
        (
            "#0109F#5P才、才没有呢！\x02\x03",

            "只是，那个……面对那种不明究竟的对手，\x01",
            "我们是不是应该采取更慎重的对策呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0949
    ChrTalk(
        0x109,
        (
            "#11P#0506F我理解你的心情……\x02\x03",

            "如果不是任务在身，\x01",
            "连我也都不想再调查下去了呢。\x02\x03",

            "#0508F……可是，如果就这么罢手，\x01",
            "然后被上面认定为什么事情都没发生的话，\x01",
            "我实在是有些难以接受……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0950
    ChrTalk(
        0x102,
        "#0108F#6P啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    #C0951
    ChrTalk(
        0x101,
        (
            "#0006F#11P这种心情我非常理解。\x02\x03",

            "#0002F那个，要不这样吧，\x01",
            "艾莉就留下来看家好了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0952
    ChrTalk(
        0x102,
        (
            "#0113F#5P好啦好啦，我明白啦！\x02\x03",

            "#0107F我也去，和大家一起去！\x02",
        )
    )

    CloseMessageWindow()

    #C0953
    ChrTalk(
        0x103,
        "#6P#0202F#N艾莉前辈好像豁出去了。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0954
    ChrTalk(
        0x104,
        "#0303F#11P哎呀呀，真是爱逞强。\x02",
    )

    CloseMessageWindow()

    #C0955
    ChrTalk(
        0x102,
        (
            "#0113F先、先不说这些……\x02\x03",

            "#0100F好像也有其它支援请求呢，\x01",
            "那些都要怎么处理？\x02",
        )
    )

    CloseMessageWindow()

    #C0956
    ChrTalk(
        0x101,
        (
            "#0003F#11P说得也是啊，嗯～……\x02\x03",

            "#0008F如果先把那些都处理完，然后\x01",
            "再与上士会合的话，未免也太麻烦……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0957
    ChrTalk(
        0x109,
        (
            "#5P#0505F啊，这样的话……\x02\x03",

            "#0502F今天一天，我就和大家\x01",
            "一起行动好了。\x02\x03",

            "而且我开着警备队的车辆，不管大家\x01",
            "想去哪里，我都可以开车送你们哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0958
    ChrTalk(
        0x101,
        "#0005F#11P哎，这样好吗？\x02",
    )

    CloseMessageWindow()

    #C0959
    ChrTalk(
        0x109,
        (
            "#5P#0504F当然没问题啦，小事一桩。\x02\x03",

            "#0500F等大家把该办的事情都\x01",
            "办完之后，我们再一起去山道的\x01",
            "遗迹那边，如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0960
    ChrTalk(
        0x102,
        (
            "#0100F#6P原来如此……\x01",
            "这样的话，行动应该会更有效率吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0961
    ChrTalk(
        0x103,
        (
            "#6P#0204F#N还要麻烦您开车送我们，\x01",
            "真是十分感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0962
    ChrTalk(
        0x104,
        (
            "#0309F嘿，我们这次也能好好体验一下\x01",
            "一科那些家伙的待遇了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0963
    ChrTalk(
        0x101,
        "#0004F#11P──那就这么决定了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0964
    ChrTalk(
        0x101,
        (
            "#0000F#11P琪雅，\x01",
            "我们下午还要再次外出……\x02\x03",

            "你和蔡特一起\x01",
            "乖乖看家，可以吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0965
    ChrTalk(
        0xA,
        (
            "#6P#1104F嗯，没问题～\x02\x03",

            "#1110F罗伊德，你们也要\x01",
            "加油赶走幽灵啊！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_57(0x3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_E3(0xB)
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
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7102")
    OP_24(0x335)
    SetScenarioFlags(0x5D, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_17AE3 end

    def Function_45_1BAAB(): pass

    label("Function_45_1BAAB")

    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)

    def lambda_1BAC2():
        OP_95(0xFE, 800, 850, 10000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BAC2)
    WaitChrThread(0xA, 1)
    OP_68(200, 1000, 3500, 1500)
    SetCameraDistance(25000, 1500)

    def lambda_1BAFA():
        OP_95(0xFE, 200, 0, 3500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BAFA)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    Sound(819, 0, 100, 0)

    def lambda_1BB26():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BB26)
    Sleep(500)
    Return()

    # Function_45_1BAAB end

    def Function_46_1BB3E(): pass

    label("Function_46_1BB3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("apl/ch50092.itc", 0x21)
    LoadChrToIndex("apl/ch50011.itc", 0x22)
    SoundLoad(806)
    OP_68(12600, 2350, 4800, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x103, 11300, 900, 2550, 90)
    SetChrPos(0x104, 13900, 900, 2550, 270)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 11300, 900, 4600, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16000, 850, 6400, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 1, 0, 40)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x5)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x5)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x5)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x5)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x5)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12400, 1400, 2600, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0xC)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12000, 1300, 2600, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x5)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 13000, 1400, 2600, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0xC)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13400, 1300, 2600, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x20)
    SetChrSubChip(0x25, 0x7)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12700, 1400, 5500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x7)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 12700, 1400, 3500, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x21)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 16000, 750, 5500, 0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(12600, 1850, 4800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0966
    ChrTalk(
        0x101,
        (
            "#0004F#11P话说，这可真让人吃惊啊……\x02\x03",

            "#0000F这个煎蛋……\x01",
            "真的是琪雅做的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0967
    ChrTalk(
        0x102,
        (
            "#0102F#5P呵呵，是呀。\x02\x03",

            "#0109F手艺实在太精湛了，\x01",
            "我在旁边都看得入迷了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0968
    ChrTalk(
        0x8,
        "#11P#1002F嗯，煎得还真是不老不嫩啊。\x02",
    )

    CloseMessageWindow()

    #C0969
    ChrTalk(
        0x104,
        (
            "#0304F#11P培根也煎得嫩滑酥脆，\x01",
            "简直挑不出任何毛病。\x02",
        )
    )

    CloseMessageWindow()

    #C0970
    ChrTalk(
        0x103,
        (
            "#6P#0204F昨天帮我一起做\x01",
            "奶汁炖菜时也是，\x01",
            "技艺相当高超……\x02\x03",

            "#0202F果然是有过丰富的\x01",
            "料理经验吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0971
    ChrTalk(
        0xA,
        (
            "#6P#1111F嗯～是这样吗？\x02\x03",

            "#1102F我好像没想那么多，手不知\x01",
            "不觉就自己动起来了～\x02",
        )
    )

    CloseMessageWindow()

    #C0972
    ChrTalk(
        0x101,
        (
            "#0003F#11P嗯～制作料理的记忆\x01",
            "大概是牢牢留存在了身体中……\x02\x03",

            "#0000F（……但即使如此，这么小的年龄\x01",
            "  就能做这么好，实在是很厉害……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xA, 0x2)

    #C0973
    ChrTalk(
        0xA,
        (
            "#5P#1101F那个那个，缇欧～\x02\x03",

            "你今天没事了吧～？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0974
    ChrTalk(
        0x103,
        "#12P#0205F啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(150)

    #C0975
    ChrTalk(
        0x102,
        (
            "#0108F#5P看脸色好像\x01",
            "不是很差，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0976
    ChrTalk(
        0x104,
        (
            "#0301F#11P还是别太勉强了，\x01",
            "多休息一下比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0977
    ChrTalk(
        0x103,
        (
            "#6P#0204F不，没关系的。\x02\x03",

            "#0202F昨天休息得很早，\x01",
            "已经恢复过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0978
    ChrTalk(
        0x8,
        "#5P#1000F嗯……\x02",
    )

    CloseMessageWindow()

    #C0979
    ChrTalk(
        0x101,
        (
            "#0000F#5P算啦，反正现在也没有什么\x01",
            "紧急的工作，不如就先──\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    #C0980
    ChrTalk(
        0x101,
        "#0005F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0981
    ChrTalk(
        0x104,
        "#0305F#11P这么早就来联络，真少见啊。\x02",
    )

    CloseMessageWindow()

    #C0982
    ChrTalk(
        0x102,
        "#0100F#5P也许是芙兰小姐吧？\x02",
    )

    CloseMessageWindow()

    #C0983
    ChrTalk(
        0x101,
        "#0001F#11P嗯，我看看……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x8)
    OP_24(0x326)
    Sound(804, 0, 100, 0)
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0984
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F您好，这里是特别任务支援科，\x01",
            "我是罗伊德·班宁斯──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年的声音")

    #A0985
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊～啊～这些事情\x01",
            "早就知道啦，用不着再说～！\x02\x03",

            "现在在哪里！正在干什么呢！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0986
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊，是约纳吗？\x02\x03",

            "#0002F早安。\x01",
            "夜行动物约纳这么早就起床，\x01",
            "还真是少见啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0987
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，这当然是因为\x01",
            "我熬夜干了一通宵啊。\x02\x03",

            "──啊啊，真是的！\x01",
            "这种小事怎样都无所谓啦！\x02\x03",

            "不过，听你这口气，\x01",
            "好像还什么都不知道吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0988
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F什么都不知道……是指什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0989
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，约纳大人今天就来个特别\x01",
            "大服务，免费告诉你好了！\x02\x03",

            "在昨天的深夜──\x01",
            "啊，不对，从日期来看应该算今天了。\x02\x03",

            "『黑月』的事务所似乎遭到了\x01",
            "某些人的袭击呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0990
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F什么……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0991
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "而且『黑月』那边似乎\x01",
            "被压制得只有招架之力～！\x02\x03",

            "受害情况好像相当严重呢！\x02\x03",

            "哈，至于袭击他们的人，\x01",
            "不用说，肯定是鲁巴彻的那些家伙吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0992
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F是这样啊……\x02\x03",

            "#0000F谢谢，约纳。\x01",
            "感谢你提供情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0993
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，下次可要记得报答我啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(825, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)

    #C0994
    ChrTalk(
        0x103,
        "#6P#0205F约纳打来的吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(807, 0, 100, 0)
    OP_0D()

    #C0995
    ChrTalk(
        0x101,
        (
            "#0006F#11P嗯嗯……看起来，\x01",
            "似乎是发生了不得了的事件呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0996
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将约纳提供的情报转告了大家。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0997
    ChrTalk(
        0x102,
        "#0101F#5P真、真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0998
    ChrTalk(
        0x104,
        "#0301F#11P喂喂，真的假的啊！？\x02",
    )

    CloseMessageWindow()

    #C0999
    ChrTalk(
        0x103,
        (
            "#6P#0206F虽说是在半夜，\x01",
            "但市区里居然会发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C1000
    ChrTalk(
        0xA,
        "#6P#1105F哎～？\x02",
    )

    CloseMessageWindow()

    #C1001
    ChrTalk(
        0x8,
        (
            "#5P#1003F嗯……\x02\x03",

            "如果情况属实，一科的人\x01",
            "大概已经出动了吧……\x02\x03",

            "#1002F如果在意的话，你们也去吧。\x01",
            "──不过还是先把饭吃完再说。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C1002
    ChrTalk(
        0x101,
        "#0001F是，遵命！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C1003
    ChrTalk(
        0x101,
        (
            "#0005F#5P啊……\x01",
            "缇欧，你没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1004
    ChrTalk(
        0x103,
        (
            "#6P#0204F嗯，没问题。\x02\x03",

            "#0202F吃完早饭后，\x01",
            "我们就去港湾区吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
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
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
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
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x4)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, 122940, 0, 5100, 180)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 124620, 30, 5490, 90)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2970, 0, 4170, 225)
    SetScenarioFlags(0xC2, 2)
    OP_C7(0x1, 0x1000)
    OP_29(0x4A, 0x1, 0x7)
    OP_29(0x4B, 0x4, 0x2)
    OP_29(0x4B, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD49")
    OP_29(0x2A, 0x4, 0x40)
    Jump("loc_1CD5B")

    label("loc_1CD49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD5B")
    OP_29(0x2A, 0x4, 0x40)

    label("loc_1CD5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD79")
    OP_29(0x2C, 0x4, 0x40)
    Jump("loc_1CD8B")

    label("loc_1CD79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD8B")
    OP_29(0x2C, 0x4, 0x40)

    label("loc_1CD8B")

    OP_24(0x326)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_46_1BB3E end

    def Function_47_1CD94(): pass

    label("Function_47_1CD94")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    EventBegin(0x0)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 57000, -1030, 3400, 90)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 59000, 30, 3400, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    FadeToBright(1000, 0)
    OP_0D()

    #C1005
    ChrTalk(
        0x9,
        "#5P#1001F…………………………………\x02",
    )

    CloseMessageWindow()

    #C1006
    ChrTalk(
        0x101,
        "#12P#0005F那个……科长？\x02",
    )

    CloseMessageWindow()

    #C1007
    ChrTalk(
        0x102,
        (
            "#0106F对、对不起，\x01",
            "我们的报告大概很难懂吧？\x02",
        )
    )

    CloseMessageWindow()

    #C1008
    ChrTalk(
        0x9,
        "#5P#1003F不……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C1009
    ChrTalk(
        0x9,
        (
            "#5P#1001F这一连串的情报……\x02\x03",

            "如果我没猜错的话，\x01",
            "应该全部都存在着某种联系。\x02",
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

    #C1010
    ChrTalk(
        0x101,
        "#12P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C1011
    ChrTalk(
        0x104,
        "#0307F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C1012
    ChrTalk(
        0x102,
        "#0101F这、这是怎么回事呢！？\x02",
    )

    CloseMessageWindow()

    #C1013
    ChrTalk(
        0x103,
        "#12P#0208F…………………………………\x02",
    )

    CloseMessageWindow()

    #C1014
    ChrTalk(
        0x9,
        (
            "#5P#1003F连续发生了这么多的事情，\x01",
            "也许你们会感到有些混乱……\x02\x03",

            "但不妨试着把今天经历过的\x01",
            "一系列见闻系统地归结到一起吧。\x02\x03",

            "#1002F特别是罗伊德──正是在这种时候，\x01",
            "才需要你发挥出搜查官的本领。\x02",
        )
    )

    CloseMessageWindow()

    #C1015
    ChrTalk(
        0x101,
        "#12P#0011F啊，是的……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C1016
    ChrTalk(
        0x101,
        (
            "#12P#0008F今天我们询问得来的情报，\x01",
            "可以粗略归结为三条……\x02\x03",

            "#0003F从曹先生他们那里听来的，\x01",
            "『黑月』受袭方面的情报……\x02\x03",

            "与格蕾丝小姐交换来的，\x01",
            "关于鲁巴彻现状的情报……\x02\x03",

            "#0001F还有就是，玛因兹的矿工\x01",
            "冈兹先生那方面的情报……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D285():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D285)
    Sleep(50)

    def lambda_1D295():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1D295)
    Sleep(50)

    def lambda_1D2A5():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D2A5)
    WaitChrThread(0x102, 2)

    #C1017
    ChrTalk(
        0x102,
        (
            "#0100F应该存在着某些要素，能把这三类\x01",
            "情报联系到一起吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1018
    ChrTalk(
        0x104,
        (
            "#0300F嗯……\x01",
            "似乎能看出一点眉目了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C1019
    ChrTalk(
        0x101,
        "#6P#0000F好，那就来整理一下吧。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_1D352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6F3")
    SetScenarioFlags(0x0, 3)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    #A1020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K在『黑月』受袭方面的情报中，\x01",
            "共通的关联要素是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "袭击者的身体能力\x01",          # 0
            "『黑月』总部的增援\x01",        # 1
            "有关琪雅情报的提供者\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D40F")
    ClearScenarioFlags(0x0, 3)

    label("loc_1D40F")

    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    #A1021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K在鲁巴彻现状方面的情报中，\x01",
            "共通的关联要素是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "马尔克尼会长的动向\x01",            # 0
            "将军犬作为战斗力投入使用\x01",      # 1
            "无计划的组织运用\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D4B6")
    ClearScenarioFlags(0x0, 3)

    label("loc_1D4B6")

    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    #A1022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K在矿工冈兹方面的情报中，\x01",
            "共通的关联要素是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "从矿山镇失踪的时间\x01",              # 0
            "在『巴鲁卡』与雷克特的比试\x01",      # 1
            "所携带的蓝色药片\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D55D")
    ClearScenarioFlags(0x0, 3)

    label("loc_1D55D")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D67E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D613")
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C1023
    ChrTalk(
        0x101,
        (
            "#0006F#6P（嗯～……\x01",
            "  好像还是不对啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    #C1024
    ChrTalk(
        0x101,
        "#0005F#6P（莫非，是这样吗……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D679")

    label("loc_1D613")


    #C1025
    ChrTalk(
        0x101,
        (
            "#6P#0006F（不对……\x01",
            "  这些情报之间好像没什么关系。）\x02\x03",

            "#0001F（重新再选择一次吧。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D679")

    Jump("loc_1D6EE")

    label("loc_1D67E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1D68E"),
        (SWITCH_DEFAULT, "loc_1D6BD"),
    )


    label("loc_1D68E")

    OP_2C(0x4C, 0x2)

    #C1026
    ChrTalk(
        0x101,
        "#6P#0000F（没错……就是这个。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6EE")

    label("loc_1D6BD")

    OP_2C(0x4C, 0x1)

    #C1027
    ChrTalk(
        0x101,
        "#6P#0003F（……多半就是这个了。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6EE")

    label("loc_1D6EE")

    Jump("loc_1D352")

    label("loc_1D6F3")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A1028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "【存在联系的要素】\x01",
            "①袭击者的身体能力\x01",
            "②无计划的组织运用\x01",
            "③所携带的蓝色药物\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C1029
    ChrTalk(
        0x102,
        "#0101F这、这个……\x02",
    )

    CloseMessageWindow()

    #C1030
    ChrTalk(
        0x104,
        (
            "#0310F喂喂……\x01",
            "这也太莫名其妙了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C1031
    ChrTalk(
        0x101,
        (
            "#6P#0006F但是，将这些联系到一起之后，\x01",
            "我们就可以看清很多东西了。\x02\x03",

            "#0008F袭击『黑月』的那些\x01",
            "黑手党所展现的身体能力……\x02\x03",

            "在『巴鲁卡』有如神助一般\x01",
            "连战连胜的矿工冈兹先生……\x02\x03",

            "#0013F虽然看似毫无关联，\x01",
            "但却有着一个相同点——他们的\x01",
            "『潜在能力』都得到了提升。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #A1032
    AnonymousTalk(
        0x101,
        (
            "#0013F如果说，造成这一切的原因\x01",
            "是这个『蓝色药片』……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A1033
    AnonymousTalk(
        0x103,
        (
            "#0203F……也就表明，那些黑手党\x01",
            "已经开始染指违禁药物了……\x02\x03",

            "而且不只将其\x01",
            "流到了市民群体中，\x01",
            "还用来对战斗力进行强化……\x02\x03",

            "#0201F……就是这么回事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A1034
    AnonymousTalk(
        0x101,
        (
            "#0006F嗯……\x01",
            "虽然这目前还只是我们的臆测。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C1035
    ChrTalk(
        0x102,
        (
            "#0101F不、不过，这样想的话，\x01",
            "确实就可以解开很多疑问了。\x02\x03",

            "那个副头目在鲁巴彻组织内的\x01",
            "统率力也已经开始下降，\x01",
            "莫非……\x02",
        )
    )

    CloseMessageWindow()

    #C1036
    ChrTalk(
        0x104,
        (
            "#0306F是因为那些靠药物获得力量，\x01",
            "从而变得狂妄自大的部下们\x01",
            "开始增多了吗……\x02\x03",

            "#0301F原来是这么回事吗……\x02",
        )
    )

    CloseMessageWindow()

    #C1037
    ChrTalk(
        0x9,
        (
            "#5P#1003F──分析得很好。\x02\x03",

            "#1000F再加上伊安律师\x01",
            "昨天说过的传闻。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1DB46():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DB46)
    Sleep(150)

    def lambda_1DB56():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DB56)

    def lambda_1DB63():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1DB63)
    Sleep(50)

    def lambda_1DB73():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DB73)
    WaitChrThread(0x104, 2)

    #C1038
    ChrTalk(
        0x101,
        (
            "#12P#0005F是指那两位业绩突然激增的\x01",
            "贸易商和证券经理吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C1039
    ChrTalk(
        0x102,
        (
            "#0105F那、那难道是因为他们也\x01",
            "服用了那种蓝色药片……！？\x02",
        )
    )

    CloseMessageWindow()

    #C1040
    ChrTalk(
        0x9,
        (
            "#5P#1006F从现阶段来看，\x01",
            "终究也只是猜测而已。\x02\x03",

            "#1003F但是，一个个点联结成了线，\x01",
            "线又渐渐交织成了完整的面……\x02\x03",

            "#1002F你们应该也有这种感觉吧？\x02",
        )
    )

    CloseMessageWindow()

    #C1041
    ChrTalk(
        0x101,
        (
            "#12P#0006F嗯……\x02\x03",

            "#0008F不过，说实话，如此严重的状况，\x01",
            "或许不是我们支援科可以独自解决的。\x02\x03",

            "#0001F特别是关系到那种药品的事件，\x01",
            "我想，恐怕有必要\x01",
            "与一科联络吧？\x02",
        )
    )

    CloseMessageWindow()

    #C1042
    ChrTalk(
        0x9,
        (
            "#5P#1004F嗯，关于这方面的问题，\x01",
            "现在正是同他们联络的最佳时机。\x02",
        )
    )

    CloseMessageWindow()

    #C1043
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(63000, 1100, 4600, 2000)
    MoveCamera(60, 17, 0, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    def lambda_1DDBC():
        OP_95(0xFE, 62000, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1DDBC)

    def lambda_1DDD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1DDD6)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x101, 500)
    OP_6F(0x41)

    #C1044
    ChrTalk(
        0xA,
        "#12P#1110F啊，你们在这里啊～\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1DE61():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DE61)
    Sleep(50)

    def lambda_1DE71():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DE71)
    Sleep(50)

    def lambda_1DE81():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1DE81)
    Sleep(50)

    def lambda_1DE91():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DE91)
    WaitChrThread(0x104, 2)

    #C1045
    ChrTalk(
        0x101,
        "#0005F#5P琪雅，怎么了？\x02",
    )

    CloseMessageWindow()

    #C1046
    ChrTalk(
        0x102,
        "#5P#0100F肚子饿了吗？\x02",
    )

    CloseMessageWindow()

    #C1047
    ChrTalk(
        0xA,
        (
            "#12P#1103F不是～是有客人来啦。\x02\x03",

            "#1105F是个表情好严肃的\x01",
            "叔叔哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C1048
    ChrTalk(
        0x101,
        "#0001F#5P表情严肃的叔叔……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    Sleep(150)
    Sound(1561, 255, 100, 0)    #voice#Dudley
    Sleep(1000)
    SetChrPos(0x16, 59000, 30, 3400, 90)

    def lambda_1DF6B():

        label("loc_1DF6B")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1DF6B")

    QueueWorkItem2(0xA, 2, lambda_1DF6B)

    def lambda_1DF7D():
        OP_95(0xFE, 61800, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1DF7D)

    def lambda_1DF97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1DF97)
    Sleep(300)

    def lambda_1DFAB():
        OP_96(0xFE, 0xF8D4, 0x0, 0xD48, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1DFAB)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x9, 500)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xA, 1)

    #C1049
    ChrTalk(
        0x101,
        "#0011F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C1050
    ChrTalk(
        0x102,
        "#5P#0105F达德利搜查官……！\x02",
    )

    CloseMessageWindow()

    #C1051
    ChrTalk(
        0x9,
        "#1002F#5P#N哦，你来得好迟啊。\x02",
    )

    CloseMessageWindow()
    OP_68(64000, 1100, 8600, 2000)
    MoveCamera(50, 17, 0, 2000)

    def lambda_1E0B5():

        label("loc_1E0B5")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1E0B5")

    QueueWorkItem2(0x101, 2, lambda_1E0B5)

    def lambda_1E0C7():

        label("loc_1E0C7")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1E0C7")

    QueueWorkItem2(0x102, 2, lambda_1E0C7)

    def lambda_1E0D9():

        label("loc_1E0D9")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1E0D9")

    QueueWorkItem2(0x103, 2, lambda_1E0D9)

    def lambda_1E0EB():

        label("loc_1E0EB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1E0EB")

    QueueWorkItem2(0x104, 2, lambda_1E0EB)

    def lambda_1E0FD():
        OP_95(0xFE, 62800, 0, 7200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1E0FD)
    Sleep(500)

    def lambda_1E11A():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E11A)
    Sleep(100)

    def lambda_1E137():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E137)
    Sleep(100)

    def lambda_1E154():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E154)
    Sleep(100)

    def lambda_1E171():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E171)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xA, 0x2)
    OP_6F(0x41)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A1052
    AnonymousTalk(
        0x16,
        (
            "……很抱歉，\x01",
            "调查会议拖了很久。\x02\x03",

            "关于那件事情……\x01",
            "我们就别浪费时间，\x01",
            "立刻进入正题如何？\x02",
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

    #C1053
    ChrTalk(
        0x9,
        (
            "#5P#1003F哦，可以啊。\x02\x03",

            "#1002F如果你不介意他们也一起听的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C1054
    ChrTalk(
        0x16,
        (
            "#12P#0601F赛尔盖长官！\x01",
            "请不要再开玩笑了！\x02\x03",

            "这可不是能说给这些\x01",
            "菜鸟们听的事啊──\x02",
        )
    )

    CloseMessageWindow()

    #C1055
    ChrTalk(
        0x9,
        (
            "#5P#1004F可是，在这次事件中，\x01",
            "他们收集到的情报\x01",
            "一定能派得上用场。\x02\x03",

            "#1000F如果让他们同席旁听，我们的进展也许会快得多哦。\x02",
        )
    )

    CloseMessageWindow()

    #C1056
    ChrTalk(
        0x16,
        "#12P#0605F您说什么……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(300)

    #C1057
    ChrTalk(
        0x16,
        (
            "#6P#0601F不过话说回来，对『黑月』的\x01",
            "询问工作也是由你们完成的呢。\x02\x03",

            "#0608F既然如此，那就……\x01",
            "……不、不行，但是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    #C1058
    ChrTalk(
        0x101,
        (
            "#11P#0006F那个，科长……\x02\x03",

            "#0000F如果不太方便的话，\x01",
            "我们还是先回避一下吧？\x02",
        )
    )

    CloseMessageWindow()

    #C1059
    ChrTalk(
        0x9,
        (
            "#5P#1003F不，没那个必要。\x02\x03",

            "#1002F这个男人身为一科的精英，\x01",
            "可不是浪得虚名的。\x02\x03",

            "在这种情况下，需要做出何种判断，\x01",
            "相信他一定能够考虑清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C1060
    ChrTalk(
        0x16,
        (
            "#6P#0603F唔……我明白了。\x02\x03",

            "#0601F──听好，你们几个。\x01",
            "接下来的谈话内容\x01",
            "可是警察局内部的机密事项……\x02\x03",

            "#0607F绝对不允许透露给任何人，\x01",
            "记住了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C1061
    ChrTalk(
        0x101,
        "#11P#0005F明、明白了。\x02",
    )

    CloseMessageWindow()

    #C1062
    ChrTalk(
        0xA,
        (
            "#1110F什么什么，机密的话～？\x02\x03",

            "#1109F琪雅也要听～！\x02",
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
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1E6AA():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E6AA)

    def lambda_1E6B7():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1E6B7)

    def lambda_1E6C4():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1E6C4)

    def lambda_1E6D1():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E6D1)

    def lambda_1E6DE():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1E6DE)
    WaitChrThread(0x104, 2)

    #C1063
    ChrTalk(
        0x101,
        "#5P#0012F那、那个……\x02",
    )

    CloseMessageWindow()

    #C1064
    ChrTalk(
        0x102,
        (
            "#5P#0102F我准备了美味的点心哦，\x01",
            "琪雅还是先去和蔡特一起吃吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xBB8)
    WaitBGM()
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_68(63880, 1100, 8580, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x16, 65300, 0, 6900, 270)
    SetChrPos(0x101, 62700, 0, 6300, 90)
    SetChrPos(0x102, 62700, 0, 7500, 90)
    SetChrPos(0x103, 61400, 0, 6500, 90)
    SetChrPos(0x104, 61400, 0, 7700, 90)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A1065
    AnonymousTalk(
        0x101,
        "#0013F给搜查一科施加压力……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C1066
    ChrTalk(
        0x16,
        (
            "#0603F#11P不，倒也并没有\x01",
            "那么露骨……\x02\x03",

            "#0601F之前上级也曾下达过指示，\x01",
            "要我们对『黑月』的受袭事件展开调查，\x01",
            "并倾尽全力处理黑手党之间的斗争事件。\x02\x03",

            "#0606F……但在不久之前开始调查的\x01",
            "神秘药物事件，却被强行中断了。\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C1067
    ChrTalk(
        0x101,
        "#6P#0011F什么……！？\x02",
    )

    CloseMessageWindow()

    #C1068
    ChrTalk(
        0x103,
        (
            "#6P#0205F一科那边也在对\x01",
            "药物事件进行调查……？\x02",
        )
    )

    CloseMessageWindow()

    #C1069
    ChrTalk(
        0x16,
        (
            "#0603F#11P哼，早在几天之前就已经开始了。\x02\x03",

            "#0600F就我来说，你们会知道这件事\x01",
            "才比较令人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    #C1070
    ChrTalk(
        0x9,
        (
            "#5P#1001F不过，一科那边是怎么\x01",
            "掌握到关于药物的消息的？\x02",
        )
    )

    CloseMessageWindow()

    #C1071
    ChrTalk(
        0x16,
        (
            "#0603F……自然是通过从以前开始\x01",
            "就和我们有所联系的『情报商』。\x02\x03",

            "#0600F其情报源非常值得信赖，\x01",
            "所以我们经常由此来收集信息……\x02\x03",

            "不过，这次我们所得到的，\x01",
            "都是些类似都市传说一类的传闻而已。\x02\x03",

            "#0606F像是『可以实现愿望的药』，\x01",
            "『可以带来幸福的蓝色药物』之类的……\x02\x03",

            "因为感觉事有蹊跷，所以我们正在\x01",
            "着手整理与此类传闻有关的市民名单，\x01",
            "但就在调查的途中……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C1072
    ChrTalk(
        0x16,
        (
            "#0605F#11P怎、怎么回事……你们几个的表情\x01",
            "就好像是在说『果然如此』一样。\x02",
        )
    )

    CloseMessageWindow()

    #C1073
    ChrTalk(
        0x9,
        (
            "#5P#1003F哼……\x01",
            "不出所料啊。\x02\x03",

            "#1000F罗伊德，把那个给他看。\x02",
        )
    )

    CloseMessageWindow()

    #C1074
    ChrTalk(
        0x101,
        "#6P#0003F……是。\x02",
    )

    CloseMessageWindow()

    #C1075
    ChrTalk(
        0x16,
        "#0605F#11P？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 0)

    def lambda_1ECFF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ECFF)
    WaitChrThread(0x101, 1)

    #C1076
    ChrTalk(
        0x101,
        "#6P#0001F这个──\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)
    #Sound(1558, 255, 100, 0)    #voice#Dudley
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #A1077
    AnonymousTalk(
        0x16,
        (
            "#0607F#4S什么……！\x02\x03",

            "这、这难道就是……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A1078
    AnonymousTalk(
        0x101,
        (
            "#0006F……这是我们今天通过\x01",
            "某个渠道而得到的证物。\x02\x03",

            "#0001F以严格保护提供者的名誉为条件，\x01",
            "暂时将其保管在我们这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)

    def lambda_1EE3C():
        OP_96(0xFE, 0xF4EC, 0x0, 0x189C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EE3C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A1079
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将至今为止的事情经过向达德利做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C1080
    ChrTalk(
        0x16,
        (
            "#0608F#11P哼……\x01",
            "果然是真实存在的吗……\x02\x03",

            "#0610F而且很有可能是\x01",
            "鲁巴彻的人所流出的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C1081
    ChrTalk(
        0x9,
        (
            "#5P#1003F命令你们停止对这种药物进行\x01",
            "调查的指示……\x02\x03",

            "#1000F具体是从哪里传达下来的，\x01",
            "对此你有什么头绪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1082
    ChrTalk(
        0x16,
        (
            "#0606F……总之是高层的某个人吧。\x02\x03",

            "#0608F连一科的科长都无法接受，\x01",
            "但也只能无奈地将指示下达给我们。\x02",
        )
    )

    CloseMessageWindow()

    #C1083
    ChrTalk(
        0x9,
        "#5P#1006F哼，真是最糟糕的情况啊……\x02",
    )

    CloseMessageWindow()

    #C1084
    ChrTalk(
        0x102,
        (
            "#6P#0105F请、请等一下。\x02\x03",

            "#0110F难道说，警察局的领导层竟然向\x01",
            "黑手党妥协，接受了他们的请求……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    OP_64(0x16)

    #C1085
    ChrTalk(
        0x101,
        "#6P#0006F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C1086
    ChrTalk(
        0x104,
        "#6P#0301F喂喂，不是开玩笑吧……\x02",
    )

    CloseMessageWindow()

    #C1087
    ChrTalk(
        0x103,
        "#6P#0206F……情况确实是再糟糕不过了呢。\x02",
    )

    CloseMessageWindow()

    #C1088
    ChrTalk(
        0x9,
        (
            "#5P#1003F──达德利。\x02\x03",

            "#1000F你会来找我们商讨这种事，\x01",
            "肯定是因为你已经对上层产生怀疑了吧。\x02\x03",

            "那么，你有什么打算吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1089
    ChrTalk(
        0x16,
        (
            "#0608F…………………………………\x02\x03",

            "#0606F……老实说，关于药物的调查工作，\x01",
            "我们这边已经无法再继续展开了。\x02\x03",

            "如果硬来，上层也许就该\x01",
            "直截了当地加以干涉了。\x02\x03",

            "#0610F可是，身为警察组织的一员，\x01",
            "如果就此罢手的话，也未免太过无能了……！\x02",
        )
    )

    CloseMessageWindow()

    #C1090
    ChrTalk(
        0x101,
        "#6P#0005F达德利搜查官……\x02",
    )

    CloseMessageWindow()

    #C1091
    ChrTalk(
        0x9,
        (
            "#5P#1002F那么，关于药物方面的\x01",
            "调查工作，也只能交给我们负责啦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    #C1092
    ChrTalk(
        0x9,
        (
            "#5P#1000F──罗伊德、艾莉，\x01",
            "还有兰迪和缇欧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F327():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F327)
    Sleep(50)

    def lambda_1F337():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F337)
    Sleep(50)

    def lambda_1F347():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F347)
    Sleep(50)

    def lambda_1F357():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1F357)
    Sleep(500)

    #C1093
    ChrTalk(
        0x9,
        (
            "#5P#1003F接下来，特别任务支援科将以非正式的\x01",
            "形式，与搜查一科进入合作阶段。\x02\x03",

            "#1001F你们就代替无法采取行动的一科，\x01",
            "继续对药物进行调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1094
    ChrTalk(
        0x101,
        "#12P#0001F是……！\x02",
    )

    CloseMessageWindow()

    #C1095
    ChrTalk(
        0x102,
        "#12P#0101F明白了！\x02",
    )

    CloseMessageWindow()

    #C1096
    ChrTalk(
        0x9,
        "#5P#1003F嗯，作为回报……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    #C1097
    ChrTalk(
        0x9,
        (
            "#5P#1002F一科手中的那些与黑手党有关的情报，\x01",
            "要无限制地提供给我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x16, 0x9, 500)

    def lambda_1F4C9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F4C9)
    Sleep(50)

    def lambda_1F4D9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F4D9)
    Sleep(50)

    def lambda_1F4E9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1F4E9)
    Sleep(50)

    def lambda_1F4F9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F4F9)
    Sleep(150)

    #C1098
    ChrTalk(
        0x16,
        (
            "#0605F赛、赛尔盖长官！？\x02\x03",

            "再怎么说，那些极其机密的情报\x01",
            "也不能毫无限制地随意……\x02",
        )
    )

    CloseMessageWindow()

    #C1099
    ChrTalk(
        0x9,
        (
            "#5P#1002F我们是无所谓哦。\x02\x03",

            "反正你们那边现在已经无计可施了，\x01",
            "不答应的话，我们随意行动就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C1100
    ChrTalk(
        0x16,
        (
            "#0601F唔……\x02\x03",

            "#0606F……明白了，\x01",
            "我接受这个条件。\x02",
        )
    )

    CloseMessageWindow()

    #C1101
    ChrTalk(
        0x9,
        "#5P#1002F呵呵，那就这么决定啦。\x02",
    )

    CloseMessageWindow()

    #C1102
    ChrTalk(
        0x104,
        (
            "#6P#0309F哎呀～真没想到我们竟然能\x01",
            "替代那个一科来展开行动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C1103
    ChrTalk(
        0x103,
        (
            "#6P#0204F真是有种莫名的\x01",
            "优越感呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0x10E, 0x1F4)

    #C1104
    ChrTalk(
        0x16,
        "#0610F#11P……………………（瞪眼）\x02",
    )

    CloseMessageWindow()

    #C1105
    ChrTalk(
        0x104,
        "#6P#0305F噢噢，好可怕……\x02",
    )

    CloseMessageWindow()

    #C1106
    ChrTalk(
        0x103,
        "#6P#0206F……女神救命女神救命。\x02",
    )

    CloseMessageWindow()

    #C1107
    ChrTalk(
        0x16,
        (
            "#0603F#11P哼，算了，没办法。\x02\x03",

            "#0601F在这种情况下，也只能同意\x01",
            "由你们来负责药物的调查工作了……\x02\x03",

            "不过，关于今后的调查方针，你们有什么想法吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1108
    ChrTalk(
        0x101,
        (
            "#6P#0003F说得也是啊……\x02\x03",

            "#0001F──不管怎么说，\x01",
            "药品的实物就在我们手里。\x02\x03",

            "无论如何，也有必要\x01",
            "查清楚其成分吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1109
    ChrTalk(
        0x16,
        (
            "#0600F#11P嗯……\x01",
            "可是，你们要怎么查呢？\x02\x03",

            "从现有情报来推测，\x01",
            "不难发现这是全新种类的药物。\x02\x03",

            "总部的鉴定部门恐怕没有能力查明其成分，\x01",
            "而且这么做也很容易被上层发觉。\x02",
        )
    )

    CloseMessageWindow()

    #C1110
    ChrTalk(
        0x101,
        (
            "#6P#0008F原来如此……\x02\x03",

            "#0000F……这样的话，我们也许\x01",
            "应该去拜托医科大学那边的人吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1F951")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C1111
    ChrTalk(
        0x102,
        (
            "#5P#0100F原来如此……\x01",
            "是要请那位医生帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA04")

    label("loc_1F951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1F9AD")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x101, 500)

    #C1112
    ChrTalk(
        0x103,
        (
            "#6P#0202F……原来如此，\x01",
            "要请那位医生帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA04")

    label("loc_1F9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1FA04")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    #C1113
    ChrTalk(
        0x104,
        (
            "#3P#0300F原来如此啊……\x01",
            "要找那位医生帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA04")


    #C1114
    ChrTalk(
        0x16,
        (
            "#0605F#11P医科大学……\x01",
            "是圣乌尔斯拉医科大学吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FA3E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FA3E)

    def lambda_1FA4B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1FA4B)

    def lambda_1FA58():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1FA58)

    #C1115
    ChrTalk(
        0x101,
        (
            "#6P#0004F嗯，我们认识那里的一位专门\x01",
            "研究药物学的医生。\x02\x03",

            "#0000F听说他的专业能力相当优秀，\x01",
            "如果拜托他来检查药物成分的话，\x01",
            "查明的可能性应该很高吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1116
    ChrTalk(
        0x16,
        "#0600F#11P哼，原来如此啊……\x02",
    )

    CloseMessageWindow()

    #C1117
    ChrTalk(
        0x9,
        (
            "#5P#1003F看样子，调查药物成分的工作\x01",
            "也只能这么办了。\x02\x03",

            "#1000F达德利，今日之内，\x01",
            "把在一科整理好的调查\x01",
            "报告书拿给我们。\x02\x03",

            "我让他们以此为基础，\x01",
            "决定今后的调查方针。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x9, 500)
    Sleep(150)

    #C1118
    ChrTalk(
        0x16,
        (
            "#0600F明白了，\x01",
            "马上就会送到。\x02\x03",

            "#0604F──那么，我就先行告辞了，\x01",
            "今后也请多多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C1119
    ChrTalk(
        0x9,
        (
            "#5P#1004F嗯，彼此彼此啊。\x02\x03",

            "#1002F而且，你这句话应该\x01",
            "也对他们说一说。\x02",
        )
    )

    CloseMessageWindow()

    #C1120
    ChrTalk(
        0x16,
        "#0610F唔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)
    OP_93(0x16, 0x10E, 0x1F4)

    #C1121
    ChrTalk(
        0x16,
        (
            "#0603F──听好，你们几个。\x02\x03",

            "#0601F一定要谨慎仔细，不要干出\x01",
            "一些蠢事，让事态进一步恶化啊。\x02\x03",

            "#0607F另外，药物的调查也就算了，\x01",
            "黑手党斗争那方面的处理工作就\x01",
            "由我们一科来负责！\x02\x03",

            "你们最好不要胡乱插手，\x01",
            "一切都交给我们来办就行了！\x02",
        )
    )

    CloseMessageWindow()

    #C1122
    ChrTalk(
        0x101,
        "#6P#0005F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_1FD98():

        label("loc_1FD98")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1FD98")

    QueueWorkItem2(0x101, 2, lambda_1FD98)

    def lambda_1FDAA():

        label("loc_1FDAA")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1FDAA")

    QueueWorkItem2(0x102, 2, lambda_1FDAA)

    def lambda_1FDBC():

        label("loc_1FDBC")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1FDBC")

    QueueWorkItem2(0x103, 2, lambda_1FDBC)

    def lambda_1FDCE():

        label("loc_1FDCE")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1FDCE")

    QueueWorkItem2(0x104, 2, lambda_1FDCE)
    OP_92(0x16, 0xF230, 0xD48, 0x1F4)
    OP_68(62000, 1100, 5500, 2000)

    def lambda_1FDFE():
        OP_95(0xFE, 62000, 0, 3400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1FDFE)
    WaitChrThread(0x16, 1)

    def lambda_1FE1C():
        OP_95(0xFE, 59000, 0, 3400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1FE1C)
    Sleep(500)
    SetChrSubChip(0x9, 0x2)
    Sound(103, 0, 100, 0)

    def lambda_1FE43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1FE43)
    WaitChrThread(0x16, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_6F(0x1)
    Sound(104, 0, 100, 0)
    Sleep(500)
    Fade(500)
    OP_68(63500, 1100, 9000, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23000, 0)
    OP_0D()

    #C1123
    ChrTalk(
        0x104,
        (
            "#5P#0302F哎呀呀，\x01",
            "真是个不坦率的老兄。\x02",
        )
    )

    CloseMessageWindow()

    #C1124
    ChrTalk(
        0x103,
        (
            "#5P#0204F……我想，那可能也是\x01",
            "一种掩饰害羞的方式吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1125
    ChrTalk(
        0x102,
        (
            "#5P#0109F呵呵，或许吧。\x02\x03",

            "#0102F而且，他是个正派的人，\x01",
            "正义感似乎比想象中的还要强呢。\x02",
        )
    )

    CloseMessageWindow()

    #C1126
    ChrTalk(
        0x101,
        (
            "#11P#0002F是啊……\x01",
            "给人一种值得信赖的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C1127
    ChrTalk(
        0x9,
        (
            "#5P#1004F基本上说，一科的人大多都是\x01",
            "这种性格认真，正义感又很强的家伙。\x02\x03",

            "不过，他们大多也都\x01",
            "墨守成规，不懂通融就是了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    #C1128
    ChrTalk(
        0x9,
        (
            "#5P#1005F──那么，你们几个，\x01",
            "打算立刻出发去医院吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20061():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20061)
    Sleep(100)

    def lambda_20071():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_20071)
    Sleep(50)

    def lambda_20081():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_20081)
    Sleep(50)
    TurnDirection(0x104, 0x9, 500)

    #C1129
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，正有此意。\x02\x03",

            "如果时间充裕，也可以先把\x01",
            "其它支援请求都解决，然后再去医院。\x02",
        )
    )

    CloseMessageWindow()

    #C1130
    ChrTalk(
        0x102,
        (
            "#0106F#6P也对哦……\x01",
            "上午也没有时间到市外去。\x02",
        )
    )

    CloseMessageWindow()

    #C1131
    ChrTalk(
        0x104,
        (
            "#6P#0300F哈，似乎会很忙啊，\x01",
            "还是先把事情都逐一解决之后再去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1132
    ChrTalk(
        0x9,
        (
            "#5P#1004F哼哼，你们有干劲就好。\x02\x03",

            "#1002F虽说是要和一科进行合作，\x01",
            "但你们也没有必要因此而过于争强。\x02\x03",

            "就像平时一样，用你们自己的方法\x01",
            "来解开药物之谜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1133
    ChrTalk(
        0x101,
        "#12P#0000F是！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_68(64000, 1330, 5500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 64000, 30, 5500, 180)
    SetChrPos(0x1, 64000, 30, 5500, 180)
    SetChrPos(0x2, 64000, 30, 5500, 180)
    SetChrPos(0x3, 64000, 30, 5500, 180)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0xC3, 0)
    OP_29(0x4A, 0x4, 0x10)
    OP_29(0x4B, 0x4, 0x10)
    OP_29(0x4C, 0x4, 0x2)
    OP_29(0x4C, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_47_1CD94 end

    def Function_48_202D0(): pass

    label("Function_48_202D0")

    EventBegin(0x0)
    Fade(1000)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    OP_0D()

    #C1134
    ChrTalk(
        0x9,
        (
            "#5P#1000F乌尔斯拉医院吗……\x02\x03",

            "你们要找的那位医生，\x01",
            "就是之前给琪雅检查\x01",
            "记忆丧失症状的那个人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1135
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，就是那位名叫约亚西姆的医生，\x01",
            "他是药物学和神经科的副教授。\x02\x03",

            "印象中，以前和他谈话时，\x01",
            "他对药物学好像有相当详尽的了解呢……\x02",
        )
    )

    CloseMessageWindow()

    #C1136
    ChrTalk(
        0x9,
        (
            "#5P#1003F嗯，那位医生要是\x01",
            "能帮得上忙就最好不过了。可是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C1137
    ChrTalk(
        0x101,
        "#12P#0005F科长……？\x02",
    )

    CloseMessageWindow()

    #C1138
    ChrTalk(
        0x102,
        "#0101F那个，您有什么在意的事吗？\x02",
    )

    CloseMessageWindow()

    #C1139
    ChrTalk(
        0x9,
        (
            "#5P#1006F……算是吧。\x02\x03",

            "#1003F力量、速度、集中力、直觉。\x02\x03",

            "这些东西，或许都可以通过药物\x01",
            "从生理方面来进行提高。\x02\x03",

            "#1001F可是……\x01",
            "『运气』这种东西，能够提高吗？\x02",
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

    #C1140
    ChrTalk(
        0x101,
        "#12P#0011F这、这个……\x02",
    )

    CloseMessageWindow()

    #C1141
    ChrTalk(
        0x102,
        (
            "#0106F按照一般的想法，\x01",
            "自然是不可能的……\x02\x03",

            "#0101F可是，那个冈兹先生的运气\x01",
            "却惊人地强，您是想说这个吧？\x02",
        )
    )

    CloseMessageWindow()

    #C1142
    ChrTalk(
        0x104,
        (
            "#0303F嗯，无论是哪种玩法，\x01",
            "光靠直觉和策略，恐怕也不可能\x01",
            "一直常胜不败。\x02\x03",

            "#0308F难道是女神站在了他这边？\x01",
            "还是说他求助于恶魔了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C1143
    ChrTalk(
        0x103,
        "#12P#0208F……………………………………\x02",
    )

    CloseMessageWindow()

    #C1144
    ChrTalk(
        0x9,
        (
            "#5P#1003F嗯，目前好像还是留有不少谜团。\x02\x03",

            "#1000F──缇欧。\x01",
            "如果可以的话，关于这方面的事情，\x01",
            "你就好好确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1145
    ChrTalk(
        0x103,
        "#12P#0203F是……我正有此意。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_20824():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20824)
    Sleep(50)

    def lambda_20834():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20834)
    Sleep(50)

    def lambda_20844():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20844)
    Sleep(200)

    #C1146
    ChrTalk(
        0x101,
        "#5P#0005F（为什么是缇欧……？）\x02",
    )

    CloseMessageWindow()

    #C1147
    ChrTalk(
        0x102,
        "#5P#0105F（有什么隐情吗……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 64000, 30, 5500, 180)
    SetScenarioFlags(0xC3, 1)
    EventEnd(0x5)
    Return()

    # Function_48_202D0 end

    def Function_49_208B1(): pass

    label("Function_49_208B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(800, 1700, 3400, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23220, 0)
    SetChrPos(0x101, 800, 0, 2400, 0)
    SetChrPos(0x102, -500, 0, 1300, 0)
    SetChrPos(0x103, 1000, 0, 4500, 180)
    SetChrPos(0x104, 1400, 0, 1500, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 3000, 0, 4700, 225)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 0, 0, 4600, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, -320, 0, 5900, 168)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(800, 1300, 3400, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C1148
    ChrTalk(
        0x101,
        (
            "#0006F#11P──缇欧，你真的没问题吗？\x02\x03",

            "#0001F如果身体还没恢复的话，你可以\x01",
            "和科长、琪雅他们一起留在支援科……\x02",
        )
    )

    CloseMessageWindow()

    #C1149
    ChrTalk(
        0x103,
        (
            "#0204F#5P……不用担心。\x02\x03",

            "#0202F我早就已经充分休息过了，\x01",
            "现在的状态比平时还要好。\x02",
        )
    )

    CloseMessageWindow()

    #C1150
    ChrTalk(
        0x101,
        (
            "#0002F#11P是吗……\x01",
            "嗯，脸色好像也不错。\x02\x03",

            "#0006F不过，琪雅突然说要\x01",
            "和你一起睡的时候，我还真\x01",
            "是吃了一惊呢……\x02",
        )
    )

    CloseMessageWindow()

    #C1151
    ChrTalk(
        0xA,
        (
            "#5P#1100F嗯～不知为什么，\x01",
            "突然就那样想。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 500)

    #C1152
    ChrTalk(
        0xA,
        (
            "#6P#1101F那个那个，缇欧，\x01",
            "你睡得好吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 500)

    #C1153
    ChrTalk(
        0x103,
        (
            "#11P#0202F嗯，那当然。\x02\x03",

            "#0204F之所以能有这么好的状态，\x01",
            "最大的理由也许就是琪雅\x01",
            "给我补充了源源不断的能量呢。\x02",
        )
    )

    CloseMessageWindow()

    #C1154
    ChrTalk(
        0xA,
        "#6P#1109F嘿嘿嘿，太好啦～！\x02",
    )

    CloseMessageWindow()

    #C1155
    ChrTalk(
        0x104,
        "#12P#0309F哈哈，原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C1156
    ChrTalk(
        0x102,
        (
            "#12P#0109F也许小琪雅确实是\x01",
            "最棒的特效药呢。\x02",
        )
    )

    CloseMessageWindow()

    #C1157
    ChrTalk(
        0x101,
        (
            "#0004F嗯#11P……是啊。\x02\x03",

            "#0008F──我说，缇欧，\x01",
            "答应我一件事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_20CE1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_20CE1)
    Sleep(100)
    OP_93(0xA, 0xB4, 0x1F4)

    #C1158
    ChrTalk(
        0x103,
        "#0205F#5P……什么………\x02",
    )

    CloseMessageWindow()

    #C1159
    ChrTalk(
        0x101,
        (
            "#0006F#11P如果今后再次发生了像昨天那种事，\x01",
            "一定要马上和我们说。\x02\x03",

            "绝对不要再勉强自己\x01",
            "一个人来承受了。\x02\x03",

            "#0001F这么说也许有些过分……\x01",
            "但你如果在战斗时突然倒下，\x01",
            "有可能会成为我们的累赘。\x02",
        )
    )

    CloseMessageWindow()

    #C1160
    ChrTalk(
        0x103,
        (
            "#0204F#5P……是，我一定铭记在心。\x02\x03",

            "我也是支援科的一员……\x01",
            "是大家的同伴。\x02\x03",

            "#0214F所以……\x01",
            "我的痛苦、压力……\x01",
            "就请大家来帮我分担吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1161
    ChrTalk(
        0x102,
        "#12P#0102F缇欧……\x02",
    )

    CloseMessageWindow()

    #C1162
    ChrTalk(
        0x104,
        (
            "#12P#0309F……哈哈。\x01",
            "没问题，小事一桩。\x02",
        )
    )

    CloseMessageWindow()

    #C1163
    ChrTalk(
        0x101,
        (
            "#0002F#11P嗯……我们\x01",
            "都很乐意替你分担哦。\x02",
        )
    )

    CloseMessageWindow()

    #C1164
    ChrTalk(
        0xA,
        "#5P#1105F嘿～……\x02",
    )

    CloseMessageWindow()

    #C1165
    ChrTalk(
        0x8,
        (
            "#5P#1009F呵呵，这样的话，\x01",
            "也就不需要我这大叔再说什么了。\x02\x03",

            "#1002F──你们要在今天上午\x01",
            "去对那些有使用药物嫌疑的\x01",
            "市民们进行询问吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20F6A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20F6A)
    Sleep(50)

    def lambda_20F7A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_20F7A)
    Sleep(50)

    def lambda_20F8A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_20F8A)
    Sleep(300)

    #C1166
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯，我准备以一科的资料为参考，\x01",
            "再次去确认一下。\x02\x03",

            "#0000F而且，一旦开始调查，大概就会非常忙了。\x01",
            "所以打算趁现在先将\x01",
            "其它的支援请求处理一下。\x02",
        )
    )

    CloseMessageWindow()

    #C1167
    ChrTalk(
        0x103,
        (
            "#6P#0203F是啊……\x01",
            "如果错过这个时机，\x01",
            "也就没有时间去市外了。\x02",
        )
    )

    CloseMessageWindow()

    #C1168
    ChrTalk(
        0x104,
        (
            "#12P#0306F不过，住宅街的证券经理、\x01",
            "剑蛇帮的小弟……\x02\x03",

            "#0301F还有彩虹剧团的\x01",
            "新演员吗……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2111F")
    OP_2C(0x4C, 0x2)

    #C1169
    ChrTalk(
        0x102,
        (
            "#0106F#6P全部都是在昨天就感觉\x01",
            "样子有些奇怪的人呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_211A5")

    label("loc_2111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21166")

    #C1170
    ChrTalk(
        0x102,
        (
            "#0101F#6P真不愧是一科……\x01",
            "全都查到了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_211A5")

    label("loc_21166")

    OP_2C(0x4C, 0x1)

    #C1171
    ChrTalk(
        0x102,
        (
            "#0108F#6P确实，昨天就感觉有些人的样子\x01",
            "比较奇怪了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211A5")


    #C1172
    ChrTalk(
        0x8,
        (
            "#5P#1003F如果有时间的话，最好\x01",
            "再去一趟伊安律师的事务所吧。\x02\x03",

            "#1001F在从伊安律师那里得知的两个人中，\x01",
            "证券经理和一科资料中写到的那个好像是\x01",
            "同一个人……\x02\x03",

            "至于贸易公司的那个经营者，\x01",
            "资料中好像并没有记录呢。\x02",
        )
    )

    CloseMessageWindow()

    #C1173
    ChrTalk(
        0x101,
        (
            "#6P#0003F是啊……\x01",
            "也去法律事务所看看吧。\x02\x03",

            "#0001F然后，等到下午，\x01",
            "约亚西姆医生应该就会和我们联络，\x01",
            "把药物成分的调查结果告诉我们了……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2136E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2136E)
    Sleep(50)

    def lambda_2137E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2137E)
    Sleep(50)

    def lambda_2138E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2138E)
    Sleep(50)

    def lambda_2139E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2139E)
    Sleep(300)
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
    SetMessageWindowPos(90, 130, -1, -1)

    #A1174
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F您好，这里是特别任务支援科，\x01",
            "我是罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A1175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……罗伊德？\x01",
            "是我，玛因兹的比克森。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A1176
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊，镇长先生。\x02\x03",

            "#0000F──您联络得正是时候，\x01",
            "冈兹先生的状态怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A1177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这、这个嘛……\x02\x03",

            "那个……冈兹那家伙\x01",
            "又消失不见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A1178
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F！？\x02\x03",

            "#0001F……能请您说得再\x01",
            "详细一点吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A1179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在那之后，冈兹\x01",
            "在半夜时清醒过来了……\x02\x03",

            "不过意识好像还很模糊，\x01",
            "所以我就让他继续睡下去了。\x02\x03",

            "谨慎起见，我也留在了房间里。\x01",
            "本来是打算第二天早上\x01",
            "就和你们联络的……\x02\x03",

            "结果，等我早上醒来之后……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A1180
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F……原来如此。\x02\x03",

            "#0001F您问过酒店和『巴鲁卡』的工作人员吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A1181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全、全都去问过了，\x01",
            "可是好像没人见到过他……\x02\x03",

            "罗伊德……\x01",
            "你认为该怎么办好？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A1182
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F……镇长先生请暂时\x01",
            "留在酒店吧。\x02\x03",

            "说不定冈兹先生\x01",
            "还会回去的。\x02\x03",

            "#0000F我们正要出去进行案情询问，\x01",
            "同时也会留意一下他的行踪。\x02\x03",

            "如果有什么新情况，\x01",
            "就请再次和我联络吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A1183
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "明、明白了……那就拜托你了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7103", 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C1184
    ChrTalk(
        0x102,
        (
            "#12P#0101F……冈兹先生\x01",
            "不见了吗？\x02",
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

    #C1185
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯……好像是\x01",
            "今天早上离开酒店的。\x02\x03",

            "#0008F是自己离开的吗，\x01",
            "还是说……\x02",
        )
    )

    CloseMessageWindow()

    #C1186
    ChrTalk(
        0x103,
        (
            "#0201F#5P……看来，果然有必要\x01",
            "去确认一下其他人的状态啊。\x02",
        )
    )

    CloseMessageWindow()

    #C1187
    ChrTalk(
        0x104,
        (
            "#12P#0301F是啊……\x01",
            "我有种莫名的不祥预感呢。\x02",
        )
    )

    CloseMessageWindow()

    #C1188
    ChrTalk(
        0x8,
        (
            "#5P#1003F……看起来，事态的进展速度\x01",
            "似乎比我们预想中的还要快呢。\x02\x03",

            "#1000F不用担心这边，\x01",
            "你们快去进行确认吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_219D1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_219D1)
    Sleep(50)

    def lambda_219E1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_219E1)
    Sleep(50)

    def lambda_219F1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_219F1)
    Sleep(300)

    #C1189
    ChrTalk(
        0x101,
        "#6P#0000F是！\x02",
    )

    CloseMessageWindow()

    #C1190
    ChrTalk(
        0xA,
        "#5P#1109F慢走哦～！\x02",
    )

    CloseMessageWindow()

    #C1191
    ChrTalk(
        0xE,
        "#1200F#5P呜～！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23720, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_68(800, 1000, 2000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 750, 0, 3410, 180)
    SetChrPos(0x1, 750, 0, 3410, 180)
    SetChrPos(0x2, 750, 0, 3410, 180)
    SetChrPos(0x3, 750, 0, 3410, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 257620, 350, 68650, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, 256820, 30, 69850, 180)
    SetScenarioFlags(0xC3, 6)
    OP_29(0x4C, 0x1, 0x5)
    OP_29(0x4C, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B57")
    OP_29(0x2D, 0x4, 0x40)
    Jump("loc_21B69")

    label("loc_21B57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B69")
    OP_29(0x2D, 0x4, 0x40)

    label("loc_21B69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B87")
    OP_29(0x30, 0x4, 0x40)
    Jump("loc_21B99")

    label("loc_21B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B99")
    OP_29(0x30, 0x4, 0x40)

    label("loc_21B99")

    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_49_208B1 end

    def Function_50_21B9F(): pass

    label("Function_50_21B9F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch08702.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 256000, 0, 68700, 90)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x1)
    SetChrPos(0xF, 257550, 400, 68700, 270)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 256000, 0, 67200, 45)
    BeginChrThread(0xC, 3, 0, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(258000, 1000, 68700, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_68(257000, 1000, 68700, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(500)
    OP_63(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_21D8C():
        OP_93(0xA, 0x10E, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_21D8C)
    WaitChrThread(0xA, 2)

    def lambda_21D9D():
        OP_93(0xA, 0x59, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_21D9D)
    WaitChrThread(0xA, 2)
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0xF, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_68(256000, 1000, 68700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_68(12600, 1850, 5600, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C1192
    ChrTalk(
        0x101,
        "#11P#0003F………………………………\x02",
    )

    CloseMessageWindow()

    #C1193
    ChrTalk(
        0x102,
        "#0103F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C1194
    ChrTalk(
        0x103,
        "#6P#0206F………………………………\x02",
    )

    CloseMessageWindow()

    #C1195
    ChrTalk(
        0x104,
        "#6P#0306F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C1196
    ChrTalk(
        0x104,
        (
            "#6P#0307F哇啊啊！\x01",
            "好慢，这也太慢了吧！？\x02\x03",

            "#0301F那个医生不是说好\x01",
            "要在下午联络我们的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C1197
    ChrTalk(
        0x102,
        (
            "#0108F#11P和医院的接待员也联络过了，\x01",
            "据说他把自己关在研究室里，\x01",
            "正在专心地进行成分检验呢……\x02",
        )
    )

    CloseMessageWindow()

    #C1198
    ChrTalk(
        0x103,
        (
            "#6P#0203F检验那种药物成分的工作\x01",
            "也许相当棘手吧。\x02\x03",

            "#0211F……但说不定他也只是在偷懒，\x01",
            "其实溜出去钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C1199
    ChrTalk(
        0x101,
        (
            "#11P#0012F我、我想应该\x01",
            "不至于吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 19000, 850, 3500, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_68(14200, 1850, 5000, 2500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    Sleep(300)

    def lambda_22108():
        OP_96(0xFE, 0x3A34, 0x352, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22108)

    def lambda_22122():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_22122)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x13B, 0x1F4)
    OP_6F(0x1)

    #C1200
    ChrTalk(
        0x8,
        (
            "#12P#1005F怎么回事，那个医生\x01",
            "还没有联络你们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1201
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯，他好像正在专心进行成分检验，\x01",
            "把自己关在研究室里，不出一步呢。\x02\x03",

            "#0000F这样的话，我们也许\x01",
            "还是应该直接过去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1202
    ChrTalk(
        0x8,
        (
            "#12P#1003F嗯，或许正该如此。\x02\x03",

            "#1000F既然已经出现了受害者，\x01",
            "最好尽早检验出药物的成分。\x02\x03",

            "游击士协会那边的联络就交给我，\x01",
            "你们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1203
    ChrTalk(
        0x102,
        (
            "#0100F#5P不好意思，\x01",
            "那就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C1204
    ChrTalk(
        0x104,
        (
            "#6P#0300F那么，我们就赶快乘巴士\x01",
            "去乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 256490, 30, 69370, 180)
    SetChrChipByIndex(0xF, 0x3)
    SetChrSubChip(0xF, 0x0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x1)
    SetChrPos(0xF, 257350, 0, 68870, 225)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 255850, 0, 67920, 225)
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
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetScenarioFlags(0xE0, 0)
    OP_C7(0x1, 0x1000)
    OP_29(0x4C, 0x1, 0x1B)
    OP_29(0x4D, 0x4, 0x2)
    OP_29(0x4D, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22480")
    OP_29(0x2B, 0x4, 0x40)

    label("loc_22480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22492")
    OP_29(0x2F, 0x4, 0x40)

    label("loc_22492")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x33, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224A4")
    OP_29(0x33, 0x4, 0x40)

    label("loc_224A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224C2")
    OP_29(0x28, 0x4, 0x40)
    Jump("loc_224D4")

    label("loc_224C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224D4")
    OP_29(0x28, 0x4, 0x40)

    label("loc_224D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224F2")
    OP_29(0x2E, 0x4, 0x40)
    Jump("loc_22504")

    label("loc_224F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22504")
    OP_29(0x2E, 0x4, 0x40)

    label("loc_22504")

    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_50_21B9F end

    def Function_51_2250A(): pass

    label("Function_51_2250A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22596")
    EventBegin(0x1)

    #C1205
    ChrTalk(
        0x101,
        (
            "#0000F在出门之前，\x01",
            "还是先确认一下\x01",
            "支援请求吧……\x02\x03",

            "说不定会有什么\x01",
            "紧急的案件发来呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Jump("loc_22637")

    label("loc_22596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22637")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C1206
    ChrTalk(
        0x8,
        (
            "#1000F啊，你们要去哪里啊？\x02\x03",

            "快去确认支援请求啊。\x01",
            "只要调查这个终端，\x01",
            "就可以把情报给调出来了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_22637")

    Return()

    # Function_51_2250A end

    def Function_52_22638(): pass

    label("Function_52_22638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_226D9")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C1207
    ChrTalk(
        0x8,
        (
            "#1000F啊，你们要去哪里啊？\x02\x03",

            "快去确认支援请求啊。\x01",
            "只要调查这个终端，\x01",
            "就可以把情报给调出来了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_226D9")

    Return()

    # Function_52_22638 end

    def Function_53_226DA(): pass

    label("Function_53_226DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22779")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C1208
    ChrTalk(
        0x8,
        (
            "#1000F啊，你们要去哪里啊\x02\x03",

            "赶快确认支援请求啊。\x01",
            "只要调查这个终端，\x01",
            "就可以把情报给调出来了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_22779")

    Return()

    # Function_53_226DA end

    def Function_54_2277A(): pass

    label("Function_54_2277A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22800")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C1209
    ChrTalk(
        0x101,
        (
            "#0000F啊……\x02\x03",

            "我们还带着小猫呢。\x01",
            "还是不要去太远的地方了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    label("loc_22800")

    Return()

    # Function_54_2277A end

    def Function_55_22801(): pass

    label("Function_55_22801")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22869")

    #C1210
    ChrTalk(
        0x101,
        (
            "#0000F……这里是后门啊。\x02\x03",

            "现在要带琪雅去游击士协会，\x01",
            "还是从一楼的正门出去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CDC")

    label("loc_22869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22965")

    #C1211
    ChrTalk(
        0x101,
        (
            "#0005F啊……还是先去\x01",
            "导力商店看看吧。\x02\x03",

            "#0000F应该就是位于中央广场一角的那个建筑物。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22905")

    #C1212
    ChrTalk(
        0x103,
        "#0200F了解，那么就去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22960")

    label("loc_22905")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22934")

    #C1213
    ChrTalk(
        0x104,
        "#0300F了解，去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22960")

    label("loc_22934")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22960")

    #C1214
    ChrTalk(
        0x102,
        "#0100F嗯，这就去看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_22960")

    Jump("loc_22CDC")

    label("loc_22965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C0C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A05")

    #C1215
    ChrTalk(
        0x101,
        (
            "#0000F啊……这里好像\x01",
            "是后门啊。\x02\x03",

            "要带大家去街上熟悉环境，\x01",
            "还是从一楼的正门出去吧。\x01",
            "出去之后应该就是中央广场了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C04")

    label("loc_22A05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AB1")

    #C1216
    ChrTalk(
        0x102,
        "#0100F啊呀……这里好像是后门呢。\x02",
    )

    CloseMessageWindow()

    #C1217
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，还是从一楼的正门出去吧。\x01",
            "从那边出去，更方便为你们做向导。\x02",
        )
    )

    CloseMessageWindow()

    #C1218
    ChrTalk(
        0x102,
        "#0100F了解，是一楼的正门对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22C04")

    label("loc_22AB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B5C")

    #C1219
    ChrTalk(
        0x103,
        "#0200F啊……这里似乎是后门哦。\x02",
    )

    CloseMessageWindow()

    #C1220
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，还是从一楼的正门出去吧。\x01",
            "从那边出去，更方便为你们做向导。\x02",
        )
    )

    CloseMessageWindow()

    #C1221
    ChrTalk(
        0x103,
        (
            "#0200F知道了。\x01",
            "是一楼的正门吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C04")

    label("loc_22B5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C04")

    #C1222
    ChrTalk(
        0x104,
        "#0300F噢，这里看起来是后门。\x02",
    )

    CloseMessageWindow()

    #C1223
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，还是从一楼的正门出去吧。\x01",
            "从那边出去，更方便为你们做向导。\x02",
        )
    )

    CloseMessageWindow()

    #C1224
    ChrTalk(
        0x104,
        (
            "#0300FＯＫ，队长。\x01",
            "是一楼的正门哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C04")

    SetScenarioFlags(0x1, 3)
    Jump("loc_22CDC")

    label("loc_22C0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C76")

    #C1225
    ChrTalk(
        0x101,
        (
            "#0000F从一楼的正门出门之后，\x01",
            "正面应该就是中央广场了。\x02\x03",

            "还要带大家熟悉一下市内哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CDC")

    label("loc_22C76")


    #C1226
    ChrTalk(
        0x101,
        (
            "#0000F从一楼的正门出门之后，\x01",
            "正面应该就是中央广场了。\x02\x03",

            "想带大家熟悉市内的话，\x01",
            "还是从那边出门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CDC")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_22801 end

    def Function_56_22CF3(): pass

    label("Function_56_22CF3")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_22D31")
    SetChrName("")

    #A1227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是空房间。\x01",
            "平时都上着锁。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4B")

    label("loc_22D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E24")
    SetChrName("")

    #A1228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C1229
    ChrTalk(
        0x101,
        "#0000F这里是空房间哦。\x02",
    )

    CloseMessageWindow()

    #C1230
    ChrTalk(
        0x102,
        (
            "#0100F这栋大楼虽然很旧，\x01",
            "但房间倒是有很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C1231
    ChrTalk(
        0x101,
        (
            "#0000F一直到前几年，\x01",
            "克洛斯贝尔通讯社都\x01",
            "一直在这栋楼里呢。\x02\x03",

            "#0003F虽然平时都上着锁……\x01",
            "但放假时还是要打扫一下的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 5)
    Jump("loc_22E4B")

    label("loc_22E24")

    SetChrName("")

    #A1232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是空房间。\x01",
            "平时都上着锁。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E4B")

    TalkEnd(0xFF)
    Return()

    # Function_56_22CF3 end

    def Function_57_22E4F(): pass

    label("Function_57_22E4F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22ED0")
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

    label("loc_22ED0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22EEC")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_22EEC")

    Return()

    # Function_57_22E4F end

    def Function_58_22EEE(): pass

    label("Function_58_22EEE")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F6F")
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

    label("loc_22F6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F8B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_22F8B")

    Return()

    # Function_58_22EEE end

    def Function_59_22F8D(): pass

    label("Function_59_22F8D")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2300E")
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

    label("loc_2300E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2302A")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2302A")

    Return()

    # Function_59_22F8D end

    def Function_60_2302C(): pass

    label("Function_60_2302C")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230AD")
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

    label("loc_230AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_230C9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_230C9")

    Return()

    # Function_60_2302C end

    SaveToFile()

Try(main)
