from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "セルゲイ課長",           # 1
        "セルゲイ課長",           # 2
        "キーア",                 # 3
        "キーア",                 # 4
        "ツァイト",               # 5
        "ツァイト",               # 6
        "ツァイト",               # 7
        "シズク",                 # 8
        "エリィ",                 # 9
        "ティオ",                 # 10
        "ランディ",               # 11
        "ソーニャ副司令",         # 12
        "ノエル曹長",             # 13
        "リーシャ",               # 14
        "ダドリー捜査官",         # 15
        "ホワイトボード",         # 16
        "魔獣調査レポート",       # 17
        "食器",                   # 18
        "食器",                   # 19
        "食器",                   # 20
        "食器",                   # 21
        "食器",                   # 22
        "食器",                   # 23
        "食器",                   # 24
        "食器",                   # 25
        "食器",                   # 26
        "食器",                   # 27
        "食器",                   # 28
        "食器",                   # 29
        "食器",                   # 30
        "食器",                   # 31
        "食器",                   # 32
        "本",                     # 33
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
        "Function_4_2104",         # 04, 4
        "Function_5_22D6",         # 05, 5
        "Function_6_2EDD",         # 06, 6
        "Function_7_3D71",         # 07, 7
        "Function_8_3DB1",         # 08, 8
        "Function_9_3DEE",         # 09, 9
        "Function_10_4A9D",        # 0A, 10
        "Function_11_4B77",        # 0B, 11
        "Function_12_5AA8",        # 0C, 12
        "Function_13_5B00",        # 0D, 13
        "Function_14_5B58",        # 0E, 14
        "Function_15_5BB0",        # 0F, 15
        "Function_16_5C08",        # 10, 16
        "Function_17_5CBB",        # 11, 17
        "Function_18_60F8",        # 12, 18
        "Function_19_7CDC",        # 13, 19
        "Function_20_82EB",        # 14, 20
        "Function_21_90EE",        # 15, 21
        "Function_22_C412",        # 16, 22
        "Function_23_C4B0",        # 17, 23
        "Function_24_C505",        # 18, 24
        "Function_25_C55A",        # 19, 25
        "Function_26_C5AF",        # 1A, 26
        "Function_27_C604",        # 1B, 27
        "Function_28_D786",        # 1C, 28
        "Function_29_D7FA",        # 1D, 29
        "Function_30_F01A",        # 1E, 30
        "Function_31_F696",        # 1F, 31
        "Function_32_FCE9",        # 20, 32
        "Function_33_111DF",       # 21, 33
        "Function_34_11B3E",       # 22, 34
        "Function_35_1425B",       # 23, 35
        "Function_36_14284",       # 24, 36
        "Function_37_142C8",       # 25, 37
        "Function_38_14D19",       # 26, 38
        "Function_39_17C55",       # 27, 39
        "Function_40_17D00",       # 28, 40
        "Function_41_17D1F",       # 29, 41
        "Function_42_18275",       # 2A, 42
        "Function_43_187F8",       # 2B, 43
        "Function_44_18D75",       # 2C, 44
        "Function_45_1D179",       # 2D, 45
        "Function_46_1D20C",       # 2E, 46
        "Function_47_1E524",       # 2F, 47
        "Function_48_21C79",       # 30, 48
        "Function_49_2227E",       # 31, 49
        "Function_50_23718",       # 32, 50
        "Function_51_240D5",       # 33, 51
        "Function_52_2421D",       # 34, 52
        "Function_53_242CF",       # 35, 53
        "Function_54_24381",       # 36, 54
        "Function_55_24416",       # 37, 55
        "Function_56_24924",       # 38, 56
        "Function_57_24AC4",       # 39, 57
        "Function_58_24B69",       # 3A, 58
        "Function_59_24C0E",       # 3B, 59
        "Function_60_24CB3",       # 3C, 60
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB2")
    Event(1, 22)

    label("loc_BB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE3")
    Event(1, 23)

    label("loc_BE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C14")
    Event(1, 24)

    label("loc_C14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C45")
    Event(1, 25)

    label("loc_C45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C76")
    Event(1, 26)

    label("loc_C76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA7")
    Event(1, 27)

    label("loc_CA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD8")
    Event(1, 28)

    label("loc_CD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D09")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD5")
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "端末の導力は落ちている。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A82")

    #C0002
    ChrTalk(
        0x101,
        (
            "#0000Fそういえば、今日は\x01",
            "本部の端末回線の\x01",
            "メンテナンスがあるんだったな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_193B")

    #C0003
    ChrTalk(
        0x102,
        (
            "#0100Fフランさんがそんな事を\x01",
            "おっしゃっていたわね。\x02\x03",

            "１日端末が使えないから、\x01",
            "フランさんはお休みが\x01",
            "貰えたそうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3B")

    label("loc_193B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19B6")

    #C0004
    ChrTalk(
        0x103,
        (
            "#0200Fええ、確かそのはずです。\x02\x03",

            "１日端末が使えないので、\x01",
            "フランさんもお休みが\x01",
            "貰えたそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3B")

    label("loc_19B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A3B")

    #C0005
    ChrTalk(
        0x104,
        (
            "#0300Fああ、フランちゃんが\x01",
            "そんな事を言ってたか。\x02\x03",

            "１日端末が使えねえから、\x01",
            "今日はお休みが\x01",
            "貰えたとかなんとか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3B")


    #C0006
    ChrTalk(
        0x101,
        (
            "#0000Fハハ……俺たちもしばらくは\x01",
            "仕事してなかったしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 5)
    Jump("loc_1ACC")

    label("loc_1A82")


    #C0007
    ChrTalk(
        0x101,
        (
            "#0000F本部の端末回線が\x01",
            "メンテナンス中だから\x01",
            "今日は使えないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACC")

    TalkEnd(0xFF)
    Return()

    label("loc_1AD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AED")
    Call(1, 20)
    Return()

    label("loc_1AED")

    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B9")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B33"),
        (1, "loc_1CDF"),
        (SWITCH_DEFAULT, "loc_20B4"),
    )


    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B5A")
    OP_2B(0x34, 0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B7B")
    OP_2B(0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1B96")
    OP_2B(0x2D, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1BAD")
    OP_2B(0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BC6")
    OP_2B(0x28, 0x29, 0x2A, 0x2F, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1BD9")
    OP_2B(0x25, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1BF8")
    OP_2B(0x22, 0x23, 0x18, 0x1A, 0x1C, 0x1E, 0x21, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C17")
    OP_2B(0x1F, 0x20, 0x21, 0x18, 0x1A, 0x1C, 0x1E, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C34")
    OP_2B(0x1B, 0x1C, 0x1D, 0x1E, 0x18, 0x1A, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C4F")
    OP_2B(0x16, 0x17, 0x18, 0x19, 0x1A, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C6C")
    OP_2B(0x11, 0x12, 0x13, 0x14, 0xE, 0x10, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C85")
    OP_2B(0xD, 0xE, 0xF, 0x10, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1CA2")
    OP_2B(0x9, 0xA, 0xB, 0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1CB9")
    OP_2B(0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1CD5")
    OP_2B(0x1, 0x35, 0x2, 0x3, 0xFFFF)
    Jump("loc_1CDA")

    label("loc_1CD5")

    OP_2B(0x1, 0xFFFF)

    label("loc_1CDA")

    Jump("loc_20B4")

    label("loc_1CDF")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("受付嬢フラン")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D3D")
    Sound(2062, 255, 100, 0)    #voice#Fran

    #A0008
    AnonymousTalk(
        0xFF,
        "#28Aはい、こちらクロスベル警察です～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D69")

    label("loc_1D3D")

    Sound(2061, 255, 100, 0)    #voice#Fran

    #A0009
    AnonymousTalk(
        0xFF,
        "#26A皆さん、どうもお疲れさまですー。\x02",
    )

    CloseMessageWindow()

    label("loc_1D69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_1FB2")
    Sound(2067, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0010
    AnonymousTalk(
        0xFF,
        "#27Aそれでは報告を承りますね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F3D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_1DDA"),
        (13, "loc_1E24"),
        (12, "loc_1E6C"),
        (SWITCH_DEFAULT, "loc_1EB6"),
    )


    label("loc_1DDA")

    Sound(2075, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            "#36Aクラス１ｓｔ――\x01",
            "ロイドさん、スゴすぎです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB6")

    label("loc_1E24")

    Sound(2074, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            "#35Aクラス２ｎｄ──\x01",
            "ロイドさん、すごいです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB6")

    label("loc_1E6C")

    Sound(2073, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "#32Aクラス３ｒｄ──\x01",
            "ロイドさん、やりましたね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB6")

    label("loc_1EB6")

    Sound(2076, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "#31A特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)    #voice#Fran

    #A0015
    AnonymousTalk(
        0xFF,
        (
            "#34Aお疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAA")

    label("loc_1F3D")

    Sound(2078, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0016
    AnonymousTalk(
        0xFF,
        "#16A報告は以上ですね～。\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)    #voice#Fran

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "#37Aでは、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAA")

    SetScenarioFlags(0x1, 5)
    Jump("loc_20A6")

    label("loc_1FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2037")
    Sound(2063, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            "#32Aあれっ……\x01",
            "先ほど報告されたばかりですよ？\x02",
        )
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)    #voice#Fran

    #A0019
    AnonymousTalk(
        0xFF,
        "#32Aまた依頼を達成されたらお願いしますね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20A6")

    label("loc_2037")

    Sound(2065, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            "#37Aあれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)    #voice#Fran

    #A0021
    AnonymousTalk(
        0xFF,
        "#16Aまたよろしくお願いしますー。\x02",
    )

    CloseMessageWindow()

    label("loc_20A6")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_20B4")

    label("loc_20B4")

    Jump("loc_1B06")

    label("loc_20B9")

    OP_E3(0x6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20D9")
    OP_E3(0xB)
    TalkEnd(0xFF)
    Call(0, 9)
    Return()

    label("loc_20D9")

    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2103")
    OP_29(0x41, 0x1, 0x1)

    label("loc_2103")

    Return()

    # Function_3_1824 end

    def Function_4_2104(): pass

    label("Function_4_2104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D5")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ミーティングを始める】\x01",      # 0
            "【まだ他に用事がある】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_217E"),
        (1, "loc_21FD"),
        (SWITCH_DEFAULT, "loc_22D3"),
    )


    label("loc_217E")


    #C0022
    ChrTalk(
        0x101,
        (
            "#0001Fそれじゃあ早速、\x01",
            "ミーティングを始めよう。\x02\x03",

            "事件に関する情報を\x01",
            "一通り整理してみるんだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_65(0x2, 0x1)
    Call(0, 18)
    Jump("loc_22D3")

    label("loc_21FD")


    #C0023
    ChrTalk(
        0x102,
        (
            "#0100Fなら、他の用事を済ませたら\x01",
            "ここに戻ってきましょう。\x02",
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
            "ミーティングを始める場合は\x01",
            "テーブルの上に！マークが出た状態で\x01",
            "○ボタンを押してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_22D3")

    label("loc_22D3")

    EventEnd(0x3)

    label("loc_22D5")

    Return()

    # Function_4_2104 end

    def Function_5_22D6(): pass

    label("Function_5_22D6")

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
            "さて……\x01",
            "返事を聞かせてもらおうか。\x02",
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
            "#0304F俺は問題ナシ。\x01",
            "このまま厄介になりますよ。\x02\x03",

            "#0301Fっていうか、俺を警察本部に\x01",
            "引っ張ったのはアンタでしょうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#5P#1002Fクク、何なら一課あたりに\x01",
            "推薦したっていいんだぞ？\x02\x03",

            "連中もお前の戦闘力なら\x01",
            "欲しがるかもしれねぇしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#0306Fうげ……ゴメンこうむりますよ。\x02\x03",

            "#0300F警備隊暮らしならまだしも、\x01",
            "ギスギスした所はちょっとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "#5P#1000Fエリィの方はどうだ？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#0104F私もこのまま\x01",
            "こちらでお世話になります。\x02\x03",

            "#0100Fセルゲイ課長。\x01",
            "改めてよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#5P#1006Fまあ、お前に関しては\x01",
            "俺も予想外だったけどな……\x02\x03",

            "#1001F本部のお偉いさんは\x01",
            "この課を安全な雑用係と思って\x01",
            "推薦してきたんだろうが……\x02\x03",

            "当然、そんな甘いもんじゃ\x01",
            "ないのは覚悟してるだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#0102Fええ、それはもう。\x02\x03",

            "#0104F密度の濃い仕事が出来るのを\x01",
            "今から期待しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#5P#1004Fフッ、上等だ。\x02\x03",

            "#1002Fティオはまあ、聞くまでもないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#4P#0203Fええ、最初から\x01",
            "そういう約束でしたし。\x02\x03",

            "#0200Fそれより……\x01",
            "今日の午後、導力ケーブルの\x01",
            "配線工事があるそうです。\x02\x03",

            "端末のセッティングは\x01",
            "わたしに任せてもらっても？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5P#1004Fああ、元よりそのつもりだ。\x02\x03",

            "#1000Fさてと──\x01",
            "そんじゃあ残るはお前だけか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2857():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2857)
    Sleep(50)

    def lambda_2867():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2867)
    Sleep(50)

    def lambda_2877():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2877)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0036
    ChrTalk(
        0x8,
        (
            "#5P#1003F──ロイド・バニングス。\x02\x03",

            "警察学校のカリキュラムを\x01",
            "座学・訓練共に優秀な成績で修了──\x02\x03",

            "そのまま捜査官試験に挑戦し、\x01",
            "見事これに合格した。\x02\x03",

            "#1001F正直、ウチには不釣合いなくらい\x01",
            "真っ当すぎる人材だ。\x02",
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
            "#5P#1004Fお前なら、どの課に行っても\x01",
            "それなりにやって行けるだろう。\x02\x03",

            "ウチが手放したら引き取りたいって\x01",
            "話も幾つか来てるしな。\x02\x03",

            "#1002F迷う余地はないんじゃねーか？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#12P#0004F──いえ。\x01",
            "色々考えた上で決めました。\x02\x03",

            "#0000Fセルゲイ課長。\x01",
            "これから宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#11P#0302Fへへっ……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#11P#0102Fロイド……\x02",
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
            "#5P#1006Fなんだよ、つまらんなぁ。\x02\x03",

            "もう少し悩みまくるのを\x01",
            "期待してたんだがよ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#12P#0012F……あのですね。\x02",
    )

    CloseMessageWindow()

    def lambda_2B6A():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2B6A)
    Sleep(50)

    def lambda_2B7A():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2B7A)
    Sleep(50)

    def lambda_2B8A():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2B8A)
    WaitChrThread(0x103, 2)
    Sleep(300)

    #C0045
    ChrTalk(
        0x8,
        (
            "#5P#1003Fまあいい、今日一日は\x01",
            "全員休暇という形にしてやる。\x02\x03",

            "地獄のように忙しくなる前の\x01",
            "最後の休暇だと思っておけ。\x02\x03",

            "#1002Fああ、ティオ。\x01",
            "端末のセットだけは頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        "#12P#0204Fええ、了解です。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P#1005Fおっと……\x01",
            "そういや忘れてたな。\x02\x03",

            "#1003F改めて──\x01",
            "ロイド・バニングス。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#12P#0001Fはい！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#5P#1001Fエリィ・マクダエル。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#0101Fはい。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#5P#1001Fランディ・オルランド。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        "#0301Fうっス。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "#5P#1001Fティオ・プラトー。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#12P#0201F……はい。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#5P#1003F本日０９：００をもって\x01",
            "以上４名の配属を承認した。\x02\x03",

            "#1002Fようこそ、特務支援課へ。\x02\x03",

            "バラエティ豊かな仕事を\x01",
            "山ほど回してやるから\x01",
            "楽しみにしてるといい──\x02",
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
            "初期の捜査費用として\x01\x07\x02",

            "１０００ミラ\x07\x00",
            "を入手しました。\x02",
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

    # Function_5_22D6 end

    def Function_6_2EDD(): pass

    label("Function_6_2EDD")

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
    SetChrName("男の声")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            "──さて、改めて\x01",
            "今日から初仕事というワケだが。\x02",
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
            "#5P#1000Fまあ、何はともあれ\x01",
            "改めて説明を補足しておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    #C0059
    ChrTalk(
        0x8,
        "#11P#1000Fロイド、捜査手帳を出せ。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0001Fあ……はい！\x02",
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
            "#0300F警察紋が入った黒手帳か。\x01",
            "何だかソレっぽい感じだよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0062
    AnonymousTalk(
        0x102,
        (
            "#0100F確か、警察官としての\x01",
            "身分証明にもなるんですよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0063
    AnonymousTalk(
        0x8,
        (
            "#1003Fああ、その他にも色んな注意や\x01",
            "説明事項をまとめている。\x02\x03",

            "戦術オーブメントの説明なんかも\x01",
            "載ってるから参考にするといい。\x02\x03",

            "#1002F──だが、コイツの最大の目的は\x01",
            "『捜査状況』の記録と確認にある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x104,
        "#0305F『捜査状況』……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0065
    AnonymousTalk(
        0x8,
        "#1003Fロイド、説明しろ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0066
    AnonymousTalk(
        0x101,
        (
            "#0000Fあ、はい。\x01",
            "（警察学校で習った所だな。）\x02",
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
            "#0000F──警察の規則では、\x01",
            "どんな捜査任務にも記録を\x01",
            "付けることになっているんだ。\x02\x03",

            "#0003F捜査任務を受けてから\x01",
            "それを進めている間の状況を\x01",
            "この捜査手帳にメモしていく。\x02\x03",

            "それを元に報告が行われるし、\x01",
            "勤務査定や特別手当も決定する。\x02\x03",

            "#0000Fだからなるべく細かく簡潔に\x01",
            "メモする必要があるってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        "#6P#0100Fなるほど、合理的ね。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#12P#0306Fうげ……\x01",
            "けっこう面倒くさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#11P#1000Fま、基本はそんな所だ。\x02\x03",

            "#1003Fしかし、この特務支援課では\x01",
            "ちょいと状況が違ってくる。\x02\x03",

            "#1002F正規の『捜査任務』以外にも\x01",
            "『支援要請』ってのがあるからな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)

    #C0071
    ChrTalk(
        0x101,
        "#0005Fえ……\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    #C0072
    ChrTalk(
        0x8,
        "#5P#1002Fティオ、用意を頼む。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        "#2P#0203F……はい。\x02",
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
        "#2P#0200F皆さん、こちらへ。\x02",
    )

    CloseMessageWindow()
    OP_68(16100, 1850, 10000, 3000)
    MoveCamera(7, 21, 0, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_3642():
        OP_95(0xFE, 16100, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3642)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_90(0x8, 14700, 850, 7600, 270)
    OP_0D()
    OP_92(0x8, 0x396C, 0x2BC0, 0x1F4)

    def lambda_368B():
        OP_95(0xFE, 14700, 850, 11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_368B)
    WaitChrThread(0x103, 1)

    def lambda_36A9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_36A9)
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

    def lambda_3732():
        OP_95(0xFE, 15200, 850, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3732)
    WaitChrThread(0x8, 1)

    def lambda_3750():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3750)
    WaitChrThread(0x101, 1)

    def lambda_3761():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3761)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x51)

    #C0075
    ChrTalk(
        0x101,
        "#6P#0000Fああ、一昨日の……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#3P#0100Fたしか、導力ネットワークに\x01",
            "繋がっている端末だったかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    #C0077
    ChrTalk(
        0x103,
        (
            "#11P#0200Fはい、昨日のうちに\x01",
            "セッティングしました。\x02\x03",

            "基本、常時起動したままで、\x01",
            "ログオンするとこの画面になります。\x02",
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
        "#0305Fなんか文字が出てきたな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0079
    AnonymousTalk(
        0x101,
        "#0005Fここに……その『支援要請』が？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0080
    AnonymousTalk(
        0x8,
        (
            "#1000Fああ、正規の任務以外の\x01",
            "各方面からの依頼が届けられる。\x02\x03",

            "#1003F市民や観光客からの頼み事、\x01",
            "クロスベル市からの協力要請など\x01",
            "様々な依頼が考えられるだろう。\x02\x03",

            "#1002F必ずしもやる必要はない──\x01",
            "が、放っておけば遊撃士あたりに\x01",
            "片付けられてしまう内容ではある。\x02",
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

    def lambda_3A43():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A43)
    Sleep(50)

    def lambda_3A53():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A53)
    Sleep(50)

    def lambda_3A63():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A63)
    WaitChrThread(0x103, 2)

    #C0081
    ChrTalk(
        0x101,
        "#12P#0001Fあ……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        "#3P#0309Fはは、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#3P#0103F遊撃士協会への高い評価を\x01",
            "少しでもこちらに持ってくる……\x02\x03",

            "#0100Fつまり、そういう事ですね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0084
    ChrTalk(
        0x8,
        (
            "#5P#1002Fま、微々たるモンだろうがな。\x02\x03",

            "それ以外にも、本部が忙しい時に\x01",
            "手伝いに駆り出される事もあるだろ。\x02\x03",

            "市内の巡回パトロールとか\x01",
            "どうでもいいデスクワークとかな。\x02",
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
        "#3P#0306Fはあ……マジかよ。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#12P#0012Fはは……\x01",
            "まあ、それはともかく。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#0000Fもう『支援要請』は\x01",
            "この端末に来ているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "#5P#1003Fおっと、そいつは\x01",
            "自分で確認してみろ。\x02\x03",

            "#1000F確認した『支援要請』は\x01",
            "捜査手帳にメモしておけよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    #C0089
    ChrTalk(
        0x101,
        "#12P#0000F了解です。\x02",
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

    # Function_6_2EDD end

    def Function_7_3D71(): pass

    label("Function_7_3D71")

    Sleep(100)

    def lambda_3D79():
        OP_95(0xFE, 10400, 850, 9300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D79)
    WaitChrThread(0x102, 1)

    def lambda_3D97():
        OP_95(0xFE, 14000, 850, 9300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D97)
    WaitChrThread(0x102, 1)
    Return()

    # Function_7_3D71 end

    def Function_8_3DB1(): pass

    label("Function_8_3DB1")


    def lambda_3DB6():
        OP_95(0xFE, 10400, 850, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DB6)
    WaitChrThread(0x104, 1)

    def lambda_3DD4():
        OP_95(0xFE, 13200, 850, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DD4)
    WaitChrThread(0x104, 1)
    Return()

    # Function_8_3DB1 end

    def Function_9_3DEE(): pass

    label("Function_9_3DEE")

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
            "クエスト【支援要請の補足説明】\x07\x00",
            "を開始した！\x02",
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
            "#12P#0305Fなんだ、どっちかというと\x01",
            "業務連絡のたぐいみてぇだな。\x02\x03",

            "#0300Fとりあえず警察本部に行って\x01",
            "色々説明を受ければいいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ、そうみたいだ。\x02\x03",

            "#0000Fでも、『導力ネットワーク』か……\x01",
            "何となくどんなものかは\x01",
            "分かったような気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#11P#0100F通信器と違って声以外に\x01",
            "画像や文字情報も送れるのね。\x02\x03",

            "話には聞いていたけど……\x01",
            "確かに色々応用できそうかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#6P#0203Fええ、現在クロスベルでは\x01",
            "様々な試験運用が行われています。\x02\x03",

            "#0200F警察に導入された\x01",
            "このシステムもその一環ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#6P#1003Fま、ギルドでも同じ技術を\x01",
            "試験的に導入したって話だがな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x12C)
    Sleep(300)

    #C0096
    ChrTalk(
        0x8,
        (
            "#6P#1002F──概要はそんな所だ。\x02\x03",

            "早速、お前たちには、\x01",
            "そこに来ている『支援要請』を\x01",
            "達成してきてもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4230():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4230)
    Sleep(50)

    def lambda_4240():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4240)
    Sleep(50)

    def lambda_4250():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4250)
    Sleep(50)

    def lambda_4260():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4260)
    WaitChrThread(0x103, 2)

    #C0097
    ChrTalk(
        0x101,
        (
            "#11P#0000F了解しました。\x02\x03",

            "#0001Fえっと、その後は\x01",
            "何をすればいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "#3P#1003F好きにしろ……と言いたい所だが\x01",
            "本部での説明の後、正式な支援要請が\x01",
            "何件か入ってくるはずだ。\x02\x03",

            "#1002F……そうだな。\x02\x03",

            "最初だし、本部への手前もあるから\x01",
            "１つくらいはこなしておけ。\x02\x03",

            "そうすりゃそこまで\x01",
            "嫌味を言われることはねぇだろ。\x02",
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
        "#11P#0006F（そういう問題なのか……？）\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    #C0100
    ChrTalk(
        0x8,
        (
            "#3P#1000Fそれとロイド……\x01",
            "ついでに街案内でもしてやれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        "#11P#0005F街案内、ですか？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#3P#1000Fこれから自分たちが守る街が\x01",
            "どういった場所なのか、\x01",
            "一通りのその目で確かめてこい。\x02\x03",

            "そうそう、出てすぐの所にある\x01",
            "武器商会と、《オーバルストア》だけは\x01",
            "訪ねておけよ？\x02\x03",

            "警察官としてやっていくなら\x01",
            "今後とも世話になるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#11P#0000Fなるほど……了解です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(300)

    #C0104
    ChrTalk(
        0x8,
        (
            "#3P#1003F俺は大抵、そこの部屋にいるが\x01",
            "昼寝やら雑誌を読むので忙しい。\x02\x03",

            "あんまりアテにしないで\x01",
            "なるべく自分たちで解決しろ。\x02\x03",

            "#1002Fそんじゃーな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4661():

        label("loc_4661")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4661")

    QueueWorkItem2(0x101, 2, lambda_4661)

    def lambda_4673():

        label("loc_4673")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4673")

    QueueWorkItem2(0x102, 2, lambda_4673)

    def lambda_4685():

        label("loc_4685")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4685")

    QueueWorkItem2(0x104, 2, lambda_4685)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(1000)

    def lambda_46A0():

        label("loc_46A0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_46A0")

    QueueWorkItem2(0x103, 2, lambda_46A0)
    Sleep(1000)

    #C0105
    ChrTalk(
        0x101,
        "#6P#0011Fちょ、ちょっと……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#0301Fおいおい……\x01",
            "いい加減なオッサンだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#0106Fふう、大丈夫なのかしら。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x103,
        "#0211F……先行き不安ですね。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#0012Fま、まあ……\x01",
            "とにかく俺たちの初仕事だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(15900, 1750, 9800, 1500)

    def lambda_47A2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47A2)
    Sleep(50)

    def lambda_47B2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_47B2)
    Sleep(50)

    def lambda_47C2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_47C2)
    Sleep(50)

    def lambda_47D2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_47D2)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    #C0110
    ChrTalk(
        0x101,
        (
            "#5P#0000F一通り市内を回りながら\x01",
            "『支援要請』を片付けよう。\x02\x03",

            "最初だから焦っても仕方ない。\x01",
            "確実にやって感じを掴んでいこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#2P#0100Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#6P#0204F了解です。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#12P#0300Fそんじゃま、行きますか。\x02",
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
            "※支援課に置かれている端末を○ボタンで調べて\x01",
            "  項目から［支援要請の確認］を選択すると、\x01",
            "  ロイド達への仕事の依頼（クエスト）が一覧表示されます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※クエストは必ずしもやる必要はありませんが、\x01",
            "  クリアすればＤＰとミラを獲得することができます。\x07\x00\x02",
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

    # Function_9_3DEE end

    def Function_10_4A9D(): pass

    label("Function_10_4A9D")

    OP_68(15900, 1750, 5400, 4000)

    def lambda_4AB3():
        OP_95(0xFE, 16500, 850, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AB3)
    WaitChrThread(0x8, 1)

    def lambda_4AD1():
        OP_95(0xFE, 16500, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AD1)
    WaitChrThread(0x8, 1)

    def lambda_4AEF():
        OP_95(0xFE, 18300, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AEF)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_4B22():
        OP_95(0xFE, 19800, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B22)
    Sleep(300)

    def lambda_4B3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4B3F)
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

    # Function_10_4A9D end

    def Function_11_4B77(): pass

    label("Function_11_4B77")

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
            "おお、戻ったのか。\x02\x03",

            "不良どもの喧嘩、\x01",
            "ちゃんと止めてきたのか？\x02",
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
            "#12P#0006F課長……それなんですが。\x02\x03",

            "#0001F少し厄介なことに\x01",
            "なってきたかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "#5P#1005Fあん……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはセルゲイに\x01",
            "今までの経緯を一通り説明した。\x07\x00\x02",
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
            "#5P#1001F……ふん、なるほどな。\x02\x03",

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
        "#12P#0005Fあの、課長……？\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#5P#1003F……そうだな。\x02\x03",

            "#1000Fこの件に関しては\x01",
            "お前たちに全て任せた。\x02",
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
        "#12P#0011Fへっ……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        "#0105Fあの、それはどういう？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#5P#1003Fここで引くも、さらに突っ込むも\x01",
            "判断は任せたって言ってるんだ。\x02\x03",

            "#1000F『ルバーチェ』の件に関しても\x01",
            "お前たちに教えることはない。\x02\x03",

            "全部、自分たちで調べてみろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#12P#0013Fそ、そんな無茶な……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#5P#1001F……俺が止めろと言ったら\x01",
            "お前らは納得できるのか？\x02",
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
        "#12P#0005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#5P#1003Fマフィアの件に関しては\x01",
            "それだけ面倒くせぇ問題なんだ。\x02\x03",

            "もし俺が上司として\x01",
            "マトモな判断をするんだったら\x01",
            "止めろとしか言いようがない。\x02\x03",

            "#1001Fそれでいいのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#12P#0008F…………いえ。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#0306Fま、ここで打ち切りってのは\x01",
            "ちょいと後味が悪いかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0108Fそうね……\x01",
            "色々と知ってしまったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#4P#0203F……同感です。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#5P#1004F──まあ、そうだな。\x02\x03",

            "何も知らない小僧どもが\x01",
            "足を滑らせて大ケガでもしたら\x01",
            "寝覚めが悪ィしな……\x02\x03",

            "#1002Fせめて良い助言者#6Rアドバイザー#を\x01",
            "お前らに紹介してやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#12P#0005Fいい助言者#6Rアドバイザー#……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 62800, 0, 11600, 270)
    Sound(820, 0, 100, 0)

    def lambda_540F():

        label("loc_540F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_540F")

    QueueWorkItem2(0x101, 2, lambda_540F)

    def lambda_5421():

        label("loc_5421")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5421")

    QueueWorkItem2(0x102, 2, lambda_5421)

    def lambda_5433():

        label("loc_5433")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5433")

    QueueWorkItem2(0x103, 2, lambda_5433)

    def lambda_5445():

        label("loc_5445")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5445")

    QueueWorkItem2(0x104, 2, lambda_5445)
    OP_0D()

    def lambda_5458():
        OP_95(0xFE, 61600, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5458)
    WaitChrThread(0x8, 1)
    OP_68(64120, 1100, 7920, 2500)

    def lambda_5487():
        OP_95(0xFE, 61600, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5487)
    WaitChrThread(0x8, 1)

    def lambda_54A5():
        OP_95(0xFE, 63000, 0, 7800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54A5)
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
            "セルゲイはロイドに一枚の名刺を手渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0005F『グリムウッド法律事務所』？\x02\x03",

            "#0001Fあれ、どこかで\x01",
            "聞いたことがあるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#1004F#5P西通りにある法律事務所だ。\x02\x03",

            "#1002Fイアンっていう名前の\x01",
            "髭面の弁護士先生がいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ……！\x01",
            "あのパン屋の裏手にある。\x02\x03",

            "そういえば俺も、前いた時、\x01",
            "何度か挨拶くらいはしてますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#0104F私も聞いたことがあります。\x02\x03",

            "#0100F確か、企業や貿易商などの\x01",
            "法律相談をしている先生ですよね？\x02\x03",

            "その一方で、市民の法律相談にも\x01",
            "親身に乗ってくれるという……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#1003F#5Pああ、熊みたいな髭面してるから\x01",
            "『熊ヒゲ先生』なんて呼ばれている。\x02\x03",

            "あの先生なら、マフィアについて\x01",
            "かなりの情報を持っているはずだ。\x02\x03",

            "#1002Fひょっとしたら……\x01",
            "警察も知らない最新情報なんかもな。\x02",
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
        "#12P#0002Fあ……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        "#12P#0202F……それは凄いですね。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        "#2P#0305F何者だよ、その先生は？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#1004F#5Pま、会えばすぐに分かるさ。\x02\x03",

            "#1000F前に俺が会った時に、\x01",
            "特務支援課のことは話している。\x02\x03",

            "お前たちの身分を明かせば\x01",
            "話ぐらいは聞いてくれるはずだ。\x02\x03",

            "この機会に挨拶しとけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#12P#0001Fわ、分かりました。\x02",
    )

    CloseMessageWindow()

    def lambda_593E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_593E)
    Sleep(150)

    def lambda_594E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_594E)
    Sleep(50)

    def lambda_595E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_595E)
    Sleep(50)

    def lambda_596E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_596E)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#0000F……西通りならすぐ近くだ。\x02\x03",

            "とにかくその\x01",
            "法律事務所を訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#11P#0100Fええ、分かったわ。\x02",
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

    # Function_11_4B77 end

    def Function_12_5AA8(): pass

    label("Function_12_5AA8")


    def lambda_5AAD():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AAD)
    Sleep(500)

    def lambda_5ACA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5ACA)
    WaitChrThread(0x101, 1)

    def lambda_5ADF():
        OP_95(0xFE, 63000, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5ADF)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_12_5AA8 end

    def Function_13_5B00(): pass

    label("Function_13_5B00")


    def lambda_5B05():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B05)
    Sleep(500)

    def lambda_5B22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5B22)
    WaitChrThread(0x102, 1)

    def lambda_5B37():
        OP_95(0xFE, 64300, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B37)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_13_5B00 end

    def Function_14_5B58(): pass

    label("Function_14_5B58")


    def lambda_5B5D():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B5D)
    Sleep(500)

    def lambda_5B7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5B7A)
    WaitChrThread(0x103, 1)

    def lambda_5B8F():
        OP_95(0xFE, 63200, 0, 5400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B8F)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_14_5B58 end

    def Function_15_5BB0(): pass

    label("Function_15_5BB0")


    def lambda_5BB5():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BB5)
    Sleep(500)

    def lambda_5BD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5BD2)
    WaitChrThread(0x104, 1)

    def lambda_5BE7():
        OP_95(0xFE, 64500, 0, 5400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BE7)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_15_5BB0 end

    def Function_16_5C08(): pass

    label("Function_16_5C08")

    OP_92(0x8, 0xF0A0, 0x1FA4, 0x1F4)

    def lambda_5C1A():
        OP_95(0xFE, 61600, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C1A)
    WaitChrThread(0x8, 1)

    def lambda_5C38():
        OP_95(0xFE, 61600, 30, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C38)
    WaitChrThread(0x8, 1)

    def lambda_5C56():
        OP_95(0xFE, 62800, 30, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C56)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrPos(0x8, 64000, 0, 11500, 180)

    def lambda_5C8A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C8A)

    def lambda_5C97():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5C97)

    def lambda_5CA4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5CA4)

    def lambda_5CB1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5CB1)
    OP_0D()
    Return()

    # Function_16_5C08 end

    def Function_17_5CBB(): pass

    label("Function_17_5CBB")

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
        "#6P#0005Fあれは……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        "#6P#0105F……何か書かれてるわね。\x02",
    )

    CloseMessageWindow()
    OP_68(16800, 1750, 7500, 3500)

    def lambda_5DA0():
        OP_95(0xFE, 16500, 850, 7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DA0)
    Sleep(300)

    def lambda_5DBD():
        OP_96(0xFE, 0x3F48, 0x352, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DBD)
    Sleep(300)

    def lambda_5DDA():
        OP_95(0xFE, 15100, 850, 6500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DDA)
    Sleep(300)

    def lambda_5DF7():
        OP_96(0xFE, 0x39D0, 0x352, 0x206C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DF7)
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
            "伝言板にメッセージがある。\x07\x00\x02",
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
            "『ヤボ用で出かけてくる。\x01",
            "  例の件は好きにやってみろ。\x01",
            "                   セルゲイ』\x07\x00\x02",
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
            "#6P#0003F課長は留守か……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3P#0301Fあのオッサン、面倒になって\x01",
            "トンズラしたんじゃねえだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0203Fその可能性は\x01",
            "否定できませんね……\x02",
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
            "#12P#0100Fまあまあ……\x01",
            "好きにさせてくれるなら、\x01",
            "それはそれで助かるじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0157
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそれで、どうする？\x02\x03",

            "早速、事件に関する\x01",
            "ミーティングを始めましょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0158
    ChrTalk(
        0x101,
        "#11P#0000Fああ、そうだな──\x02",
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
            "ミーティングを始める場合は\x01",
            "テーブルの上に！マークが出た状態で\x01",
            "○ボタンを押してください。\x07\x00\x02",
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

    # Function_17_5CBB end

    def Function_18_60F8(): pass

    label("Function_18_60F8")

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
            "#11P#0003F──発端は５日前の真夜中。\x02\x03",

            "『サーベルバイパー』と\x01",
            "『テスタメンツ』のメンバーが\x01",
            "それぞれ何者かに襲われた。\x02\x03",

            "#0001F場所は、旧市街の別の２箇所。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(300)

    #A0161
    AnonymousTalk(
        0x101,
        "#0001Fここと、ここになる。\x02",
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
            "#0101F西の裏通りが『テスタメンツ』の\x01",
            "メンバーが襲われた場所……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0163
    AnonymousTalk(
        0x104,
        (
            "#0301Fで、東のライブハウス前が\x01",
            "『サーベルバイパー』のヤツが\x01",
            "襲われた場所ってことか。\x02",
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
            "#6P#0205F……こうして見ると\x01",
            "旧市街の反対側同士ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_6689")
    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0165
    ChrTalk(
        0x101,
        (
            "#5P#0001Fああ、同じ夜に起きても\x01",
            "すぐには判らなかったはずだ。\x02\x03",

            "#0008Fそれぞれの溜まり場に運び込んで\x01",
            "手当てをしてから、翌朝病院へ……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#12P#0101Fたしか、襲われた２人は\x01",
            "同じ救急車で運ばれたのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#5P#0006Fああ、救急車の人も\x01",
            "さぞかし面食らっただろう。\x02\x03",

            "#0001Fそしてようやく闇討ちが\x01",
            "お互いの仕業だと確信して\x01",
            "現在に至る──という所かな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_671F")

    label("loc_6689")


    #C0168
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ、同じ夜に起きても\x01",
            "すぐには判らなかったはずだ。\x02\x03",

            "#0000Fそしてようやく闇討ちが\x01",
            "お互いの仕業だと確信して\x01",
            "現在に至る──という所かな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_671F")


    #C0169
    ChrTalk(
        0x104,
        (
            "#6P#0306Fうーん……やっぱり、\x01",
            "第三者がいたとしか思えねえぜ。\x02\x03",

            "#0301Fどちらかのメンバー全員が\x01",
            "口裏を合わせない限り、\x01",
            "どっちの犯行も不可能だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ……この段階で\x01",
            "２つの犯行を第三者の仕業だと\x01",
            "仮定してしまっても構わないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#12P#0104Fそうね……\x01",
            "少しずつ可能性を絞らないと\x01",
            "前に進めないし。\x02\x03",

            "#0101F──で、その第三者として\x01",
            "上がってきた名前があるわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ。\x02\x03",

            "#0001F『ルバーチェ商会』。\x01",
            "クロスベルの裏社会を\x01",
            "支配しているというマフィアだ。\x02\x03",

            "グレイスさんの情報によれば\x01",
            "半月ほど前、その構成員が\x01",
            "旧市街で目撃されている。\x02\x03",

            "#0006Fこの情報自体の真偽を\x01",
            "確かめている時間はないけど……\x02\x03",

            "#0001Fまずは『ルバーチェ』が\x01",
            "２件の傷害事件を起こしたという\x01",
            "仮定で話を進めてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#6P#0203F……そうなると……\x02\x03",

            "#0201Fやはり問題は“動機”ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ、それが問題だ。\x02\x03",

            "#0001F……逆に言えば、\x01",
            "それが明らかにならない限り\x01",
            "推理は振り出しに戻りかねない。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x104,
        (
            "#6P#0303Fうーん、動機ねぇ……\x02\x03",

            "#0308F利害の絡みそうにない、\x01",
            "マフィアと２組の不良集団……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#12P#0103Fそれら３つの“点”を結ぶ\x01",
            "“線”があるはず……\x02\x03",

            "#0100F──ねえ、ロイド。\x01",
            "見当は付いているのでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#5P#0004Fはは、まだ確信が\x01",
            "あるわけじゃないけど……\x02\x03",

            "#0000F３つの“点”を結ぶ“線”。\x01",
            "考えられるとしたら──\x02",
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
            "【ワジの経歴】\x01",          # 0
            "【ヴァルドの過去】\x01",      # 1
            "【黒月の存在】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6C4D"),
        (1, "loc_6E7F"),
        (2, "loc_6FDA"),
        (SWITCH_DEFAULT, "loc_7181"),
    )


    label("loc_6C4D")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0178
    ChrTalk(
        0x101,
        (
            "#5P#0003Fこれは馬鹿げた\x01",
            "考えかもしれないけど……\x02\x03",

            "#0001F２年前、旧市街に現れた\x01",
            "ワジが“線”の可能性はある。\x02\x03",

            "それこそ彼が、ルバーチェの\x01",
            "ボスの息子だったりとかね。\x02",
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
        "#12P#0105Fそ、それって……！？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        "#6P#0301Fおいおい、本当かよ！？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        (
            "#5P#0006F可能性としては、だよ。\x02\x03",

            "#0000Fその場合、そのボスが\x01",
            "家出している息子を連れ戻すため、\x01",
            "旧市街に工作をしかけたとかね。\x02\x03",

            "#0012Fまあ、ここまで仮定を重ねると\x01",
            "推理というより妄想だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        "#6P#0306Fおいおい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7181")

    label("loc_6E7F")


    #C0183
    ChrTalk(
        0x101,
        (
            "#5P#0003Fこれは単に可能性だけど……\x02\x03",

            "#0001F過去、あのヴァルドが\x01",
            "今のマフィアの構成員の一人に\x01",
            "恨みを買うことをしたとかね。\x02\x03",

            "それを逆恨みに思って\x01",
            "今回の事件を起こしたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#12P#0106Fうーん……\x01",
            "考えられなくはないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        (
            "#6P#0301Fさすがに、その程度の事情じゃ\x01",
            "大げさすぎる仕掛けじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        "#5P#0006F……やっぱりそうだよな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7181")

    label("loc_6FDA")

    OP_2C(0x3E, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0187
    ChrTalk(
        0x101,
        (
            "#5P#0003F可能性があるとすれば……\x01",
            "現実的なのは《黒月》だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        (
            "#6P#0305Fああ、あのヒゲ先生が\x01",
            "教えてくれた情報か。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        (
            "#12P#0103F確かに、可能性としては\x01",
            "一番ありそうな気がするけど……\x02\x03",

            "#0101Fでも、そうだとしたら\x01",
            "どんな線になるのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#6P#0203F点同士が線で結ばれるのは\x01",
            "何らかの『必然性』……\x02\x03",

            "#0200Fとなると、《黒月》絡みで\x01",
            "マフィアが２組の不良集団を襲う\x01",
            "『必然性』があるわけですか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7181")

    label("loc_7181")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_732F")
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0191
    ChrTalk(
        0x103,
        (
            "#6P#0200F……あの、ロイドさん。\x02\x03",

            "その線が《黒月》ということは\x01",
            "考えられないでしょうか……？\x02",
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
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#6P#0305Fおいおい、マフィアじゃなくて、\x01",
            "その対抗組織が黒幕ってことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        (
            "#6P#0203Fいえ……マフィアの仕業が\x01",
            "前提としての話です。\x02\x03",

            "#0200Fその上で《黒月》が線である\x01",
            "可能性はないんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_732F")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0195
    ChrTalk(
        0x101,
        (
            "#5P#0008F──そうか。\x01",
            "これなら説明が付くぞ。\x02",
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
        "#12P#0105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        "#6P#0300Fなんか閃いたか？\x02",
    )

    CloseMessageWindow()

    def lambda_73F6():
        OP_95(0xFE, 12600, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73F6)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0198
    ChrTalk(
        0x101,
        (
            "#0001F#5P『必然性』の話だよ。\x02\x03",

            "《黒月》のクロスベル進出を受けて\x01",
            "ルバーチェ側がする事といえば何だ？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#6P#0305Fそりゃあ……\x01",
            "単純に考えれば戦力増強だろ。\x02\x03",

            "#0303F兵隊の増強と武装の強化。\x01",
            "どちらも欲しいところだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0003F#5Pマフィアなら、武装の強化は\x01",
            "密貿易で確保できるだろう。\x02\x03",

            "#0001Fだが、戦闘員の方はどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        "#6P#0305Fそいつは……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x102,
        (
            "#12P#0108F普通に考えたら猟兵団を\x01",
            "雇うところでしょうけど……\x02\x03",

            "#0103F……ううん、駄目ね。\x01",
            "クロスベルは色々な意味で\x01",
            "周辺諸国から注目されすぎている。\x02\x03",

            "#0101F《不戦条約》の手前もあるし、\x01",
            "猟兵団を勝手に動かしたりしたら\x01",
            "帝国と共和国が黙っていないわ。\x02\x03",

            "それは両者の意を受ける\x01",
            "政治家や議員たちにも同じこと……\x02",
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
        "#12P#0105F──あ。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        "#6P#0205Fロイドさん、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x104,
        (
            "#6P#0301Fその兵隊候補として\x01",
            "不良どもをってことかよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#0003F#5Pああ……血の気が多く\x01",
            "しかも統率されている若者たち。\x02\x03",

            "#0001Fこの街で運用できる戦力としては\x01",
            "まさに打ってつけだろう。\x02\x03",

            "しかし、どちらのグループにも\x01",
            "目障りな存在がいるとしたら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        (
            "#12P#0101Fなるほど……\x02\x03",

            "あのワジ君は、間違っても\x01",
            "マフィアに協力しそうにないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#6P#0203Fあのヴァルドさんも\x01",
            "お山の大将でいたいタイプ……\x02\x03",

            "#0201Fとてもマフィアの下で\x01",
            "働きそうにはありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        (
            "#6P#0308Fそこで、お互いを潰し合わせて\x01",
            "弱体化したあたりを見計らって\x01",
            "一気に取り込みにかかる……\x02\x03",

            "#0301Fなるほど、そういう筋書きかよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#0012F#5Pあくまで可能性の一つさ。\x02\x03",

            "#0000F現時点である情報を\x01",
            "一つずつ組み立てた場合のね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x104,
        (
            "#6P#0309Fまたまた～！\x01",
            "謙遜するなってーの！\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x102,
        (
            "#12P#0104Fうん、私もかなり\x01",
            "的を射ていると思うわ。\x02\x03",

            "#0102F推理にも無理がないし、\x01",
            "状況的な説得力もあるもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        (
            "#6P#0202F……伊達に捜査官の\x01",
            "資格を持ってはいませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#0004F#5Pはは……ありがとう。\x02\x03",

            "#0000F──それで、さ。\x02\x03",

            "この推理……あの２人にも\x01",
            "伝えた方がいいと思わないか？\x02",
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
        "#12P#0105Fあの２人って……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        "#6P#0305Fおいおい、まさか……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#0003F#5Pそう……\x02\x03",

            "ヴァルド・ヴァレスに\x01",
            "ワジ・ヘミスフィア──\x02\x03",

            "#0000F『サーベルバイパー』と\x01",
            "『テスタメンツ』のヘッド達さ。\x02",
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

    # Function_18_60F8 end

    def Function_19_7CDC(): pass

    label("Function_19_7CDC")

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
        "#11P#0006F……遅いな、課長。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0219
    ChrTalk(
        0x101,
        (
            "#5P#0001Fそろそろ朝のミーティングを\x01",
            "始めたいんだけど……\x02",
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
            "#0106Fさすがに課長抜きで\x01",
            "始めるわけにはいかないものね。\x02",
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
            "#6P#0303Fんー、こんな事なら\x01",
            "２度寝すりゃあ良かったな。\x02\x03",

            "#0302Fそんで昼過ぎに起きてから\x01",
            "カジノあたりに遊びに行くと。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0222
    ChrTalk(
        0x103,
        "#5P#0211F典型的なダメ人間ですね……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 6000, 850, 10200, 90)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)

    #N0223
    NpcTalk(
        0x8,
        "男の声",
        "#2P……遅れたな。\x02",
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

    def lambda_7FF7():
        OP_96(0xFE, 0x3138, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7FF7)
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
            "#2P#0000F──課長。\x01",
            "おはようございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#4P#0100Fおはようございます。\x01",
            "早速ミーティングを始めますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "#5P#1003Fいや、その必要はない。\x02\x03",

            "#1000F先ほど本部から連絡があった。\x02\x03",

            "今日はお前らに\x01",
            "特別任務を引き受けてもらう。\x02",
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
        "#2P#0005F特別任務……？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x104,
        "#6P#0301F何かウサン臭い響きだな……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x103,
        (
            "#6P#0200F……この前のような\x01",
            "捜査任務ということですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "#5P#1004F残念ながら俺も知らん。\x02\x03",

            "#1002Fまずは警察本部に行って来い。\x01",
            "お前らの客人が待ってるはずだ。\x02",
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

    # Function_19_7CDC end

    def Function_20_82EB(): pass

    label("Function_20_82EB")

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
        "#0001F#5Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        (
            "#0103F#11P本当に各地で起きてるのね……\x02\x03",

            "#0101Fほとんどニュースに\x01",
            "なっていないみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x104,
        (
            "#6P#0303Fふむ……なるほどな。\x02\x03",

            "#0301Fどうやらただの\x01",
            "魔獣被害じゃなさそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x103,
        (
            "#6P#0200F狼型魔獣……\x01",
            "クロスベルの固有種でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#5P#0003Fさすがにちょっと判らないな……\x02\x03",

            "#0001Fただ、被害の起きた場所では\x01",
            "はっきりとした足跡なんかも\x01",
            "残されているみたいだ。\x02\x03",

            "そういう魔獣がいるのは確実だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#0101F#11Pでも、警備隊の捜索では\x01",
            "未だに確認されていないのよね？\x02\x03",

            "それがちょっと気になるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x104,
        (
            "#6P#0306Fああ……姿を隠しているんなら\x01",
            "相当ズル賢い魔獣みたいだぜ。\x02\x03",

            "#0301Fこりゃ、凄腕の狩人かなんかを\x01",
            "雇った方がいいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        (
            "#6P#0203F……そうですね。\x02\x03",

            "#0200Fわたしたちが動いたとして\x01",
            "何か出来るとは思えませんが……\x02",
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
        "#0105F#11Pロイド、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#6P#0300Fなんだ？\x01",
            "また何か閃#2Rひらめ#いたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#5P#0004F閃いたってより……\x02\x03",

            "#0000F『捜査』という観点から\x01",
            "この魔獣被害を調べるんだったら\x01",
            "何がポイントになるかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x102,
        "#0105F#11P『捜査』の観点から……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x103,
        "#6P#0205F魔獣被害を調べる……？\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#5P#0000F例えば一連の魔獣被害を\x01",
            "『事件』として捉えたら……\x02\x03",

            "この場合『犯人』は誰になる？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        (
            "#6P#0300Fそりゃ、報告にもある\x01",
            "狼型魔獣ってやつだろ。\x02\x03",

            "どうやら一匹だけじゃなくて\x01",
            "群れで行動してるみたいだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#5P#0003Fだったらもう一つ……\x02\x03",

            "#0001Fその『犯人』の『プロフィール』と\x01",
            "『動機』についてはどうだろう？\x02",
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
        "#6P#0305Fそいつは……\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0104F#11P……なるほど。\x02\x03",

            "#0100Fこの調書からは\x01",
            "それが見えて来ないわけね？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ、知能が高い魔獣なら\x01",
            "普通は人里には近づかないはずだ。\x02\x03",

            "飢えているのが動機だとすると\x01",
            "病院の被害報告なんかは不可解すぎる。\x02\x03",

            "#0000Fだったら、それらを説明できる\x01",
            "何らかの『真実』があるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        "#6P#0300Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x103,
        (
            "#6P#0204F確かに……\x01",
            "理屈ではそうなりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#0100F#11Pそうすると\x01",
            "捜査方針は決まったわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ……\x01",
            "とにかく被害にあった場所で\x01",
            "関係者から話を聞いてみよう。\x02\x03",

            "#0000F少なくとも、俺たちのやり方で\x01",
            "この調書を補完する事くらいは\x01",
            "最低限できるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        (
            "#0104F#11Pそうね……\x02\x03",

            "#0100F少しでも警備隊の役に立てれば\x01",
            "無駄にはならないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#6P#0309Fは～、助かったぜ。\x02\x03",

            "闇雲に野山を駆け回って\x01",
            "魔獣狩りする羽目にならなくてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそれで、ロイドさん。\x02\x03",

            "#0200F聞き込みをするとして……\x01",
            "まずは何処から行くんですか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0257
    ChrTalk(
        0x101,
        "#11P#0005Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0258
    ChrTalk(
        0x101,
        (
            "#11P#0000Fまずは最初に被害に遭った\x01",
            "アルモリカ村に行ってみよう。\x02\x03",

            "一番被害が具体的だし……\x01",
            "少しでも魔獣の特徴を\x01",
            "掴んでおいた方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        (
            "#0104F#11Pなるほど……\x01",
            "いいかもしれないわね。\x02\x03",

            "#0100Fえっと、アルモリカ村は\x01",
            "確か街の北東だったわよね？\x02",
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
            "#5P#0000Fああ、東口に出て\x01",
            "導力バスに乗ればいいはずだ。\x02\x03",

            "#0003Fそれと……\x01",
            "今回は初めての市外活動だ。\x02\x03",

            "#0001F行った先で何があるか判らない。\x01",
            "準備を済ませてから出発しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        "#6P#0300Fだな。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        (
            "#6P#0202F念のため、他の支援要請も\x01",
            "チェックした方が良さそうですね。\x02",
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

    # Function_20_82EB end

    def Function_21_90EE(): pass

    label("Function_21_90EE")

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
    SetChrName("少年の声")

    #A0263
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30Wちょ、ちょっと待ってよ……！\x02",
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
            "しばらく旅に出るって……\x01",
            "そんないきなり。\x02\x03",

            "一体どこに行くつもりなのさ？\x02",
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
            "レミフェリア公国だ。\x02\x03",

            "なァに、しばらくと言っても\x01",
            "２ヶ月くらいで済むだろう。\x02\x03",

            "場合によっちゃ、半月足らずで\x01",
            "帰ってくるかもしれんしな。\x02",
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
            "そ、それは判ったけど……\x02\x03",

            "兄ちゃん、一応は\x01",
            "警察の捜査官なんだろう？\x02\x03",

            "そんな長いあいだ、\x01",
            "旅行なんかしてもいいのかよ？\x02",
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
            "おっ、なんだなんだ～。\x02\x03",

            "お兄様が留守にするのが\x01",
            "そんな寂しいのか～？\x02\x03",

            "もう、ロイドきゅんったら\x01",
            "寂しがり屋さんなんだから～っ。\x02",
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
            "……２ヶ月と言わずに\x01",
            "２年くらい旅行してればぁ？\x02\x03",

            "僕、そのくらい一人で平気だし。\x02",
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
            "ウソウソ、調子に乗りました。\x02\x03",

            "実はな……\x01",
            "これには深い訳があるんだよ。\x02\x03",

            "トップシークレットってやつだ。\x02",
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
            "うさんくさいなぁ。\x02\x03",

            "ちなみに聞くけど、\x01",
            "どんなシークレットなのさ？\x02",
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
            "おう、よくぞ聞いてくれた。\x02\x03",

            "実はな……\x01",
            "とびっきり可愛い女の子を\x01",
            "エスコートしながらの旅なんだ。\x02",
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
            "へ……   \x02",
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
            "その子と一緒に、麗#2Rうるわ#しの北国、\x01",
            "レミフェリアへ逃避行ってわけだ。\x02\x03",

            "どうだどうだ、うらやましかろ？\x02",
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
            "とまあ、冗談はこれくらいにして。\x02\x03",

            "俺がいない間、お前の夕食は\x01",
            "お隣さんにお願いしといたからな。\x02\x03",

            "朝昼くらいは自分で何とかしろよ？\x02",
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
            "いや、食事くらい\x01",
            "自分で何とかできるけど……\x02\x03",

            "──じゃなくて！\x02\x03",

            "可愛い女の子って……\x01",
            "いったいどういうつもりだよ！？\x02\x03",

            "そんなこと、セシル姉に\x01",
            "知られたらどうするつもりさ！？\x02",
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
            "へっ……\x02\x03",

            "なんでそこに\x01",
            "セシルの名前が出てくるんだ？\x02",
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
            "なんでって……ああもう！！\x02\x03",

            "（セシル姉も何だって\x01",
            "  こんな鈍感な馬鹿兄貴をっ……）\x02",
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

            "ていうかセシルには\x01",
            "もうとっくに話してるんだが……\x02",
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
            "！？     \x02",
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
            "んー、なんか\x01",
            "妙な誤解があるみたいだな。\x02\x03",

            "旅って言っても\x01",
            "一応、警察の出張の仕事だぞ？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0xBB8, 0x0)

    #A0282
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#40W#30Aそれにその子は……#1000W…#20W \x01",
            "#50Wまだ…#400W…#100W歳なんだからな…#300W…\x07\x00\x02",
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
        "#5P………ん…………\x02",
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
            "#5206F#5P……夢、か………\x02\x03",

            "#5208F懐かしいな……\x01",
            "あれはいつ頃だったっけ……\x02\x03",

            "確か俺が１２……\x01",
            "いや、１３くらいだったか？\x02\x03",

            "#5205Fそういえば、確かその後で──\x02",
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

    def lambda_9C18():
        OP_95(0xFE, 1000, 30, 128100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C18)
    WaitChrThread(0x101, 1)

    def lambda_9C36():
        OP_95(0xFE, 1700, 30, 128100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C36)
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
        "#5201Fはい、ロイドです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7111", 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おう、起きてたか。\x02\x03",

            "調書ってのは\x01",
            "もうまとまってるのか？\x07\x00\x02",
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
            "#5205Fあ、はい。\x02\x03",

            "#5200F昨日の調査に関しては\x01",
            "一通りまとまっている状態です。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "結構だ。\x02\x03",

            "とっとと支度をして\x01",
            "全員で課長室まで来い。\x02\x03",

            "お前たちに客人だ。\x07\x00\x02",
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
        "#11P──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(64080, 1000, 7060, 4000)
    SetCameraDistance(22500, 4000)

    def lambda_9FAE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9FAE)

    def lambda_9FBB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9FBB)

    def lambda_9FC8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_9FC8)
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
        "#0005F#12Pソーニャ副司令……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        "#0300F#12Pやっぱ予想通りか。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x13,
        "#5P#2002F#5Pふふ、おはよう。\x02",
    )

    CloseMessageWindow()

    #N0294
    NpcTalk(
        0x14,
        "女性隊員",
        "#5P#0502Fお疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#6P#0104Fおはようございます。\x02\x03",

            "#0102Fやはりお客様というのは\x01",
            "副司令だったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "#5P#1002F#5Pああ、丁度さっき、\x01",
            "こっちを訪ねてきたんだ。\x02\x03",

            "お前たちの調査について\x01",
            "聞いておきたいらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれは構いませんが……\x01",
            "ずいぶん急な話ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#6P#0105Fまだ鉱山町方面の調査が\x01",
            "終わっていませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x13,
        (
            "#5P#2006F悪いわね、急かすつもりでは\x01",
            "なかったんだけど……\x02\x03",

            "こちらの状況が\x01",
            "少し変わってしまったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        "#0305F#12P状況が変わった……？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x13,
        (
            "#5P#2001F実は昨日まで、ウチの方で\x01",
            "鉱山町方面の警備・巡回を\x01",
            "行っていたんだけど……\x02\x03",

            "今朝をもって完全に\x01",
            "引き上げることになったのよ。\x02",
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
        "#12P#0001F警備を引き上げるって……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x103,
        (
            "#12P#0201F確か鉱山町に魔獣が現れたのは\x01",
            "３日前のことですよね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x13,
        (
            "#5P#2003Fええ、こちらとしても\x01",
            "せめて１週間くらいは警備を\x01",
            "続けたかったんだけど……\x02\x03",

            "#2001F警備隊司令からのお達しでね。\x01",
            "これ以上、無駄なことをするなって。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#6P#0101Fむ、無駄なことって……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#0308F#12Pチッ……\x01",
            "あの腰巾着オヤジか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A50A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A50A)
    Sleep(50)

    def lambda_A51A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A51A)
    Sleep(50)
    TurnDirection(0x103, 0x104, 500)

    #C0307
    ChrTalk(
        0x101,
        "#5P#0005Fランディ、知ってるのか？\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#0303F#12P俺がベルガード門に詰めてた時、\x01",
            "何度かお目にかかってるからな。\x02\x03",

            "#0301F一応、警備隊のトップだが\x01",
            "帝国派議員のお偉いさんと\x01",
            "深い繋がりがあるらしくてな。\x02\x03",

            "ロクに仕事もしないで\x01",
            "接待ばかりやってたみたいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x102,
        (
            "#6P#0108F噂には聞いていたけど……\x01",
            "やっぱりそんな人だったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        (
            "#6P#0201Fですが、魔獣の被害を\x01",
            "放っておくというのは\x01",
            "さすがに問題があるのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x13,
        (
            "#5P#2003Fええ……その通りよ。\x02\x03",

            "#2001F局地的な魔獣の被害なら\x01",
            "最悪、遊撃士協会に任せるのも\x01",
            "アリだったけれど……\x02\x03",

            "今回は被害の範囲が広すぎる。\x02\x03",

            "警備隊としてもこれ以上は\x01",
            "看過できるわけがないわ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A78F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A78F)

    def lambda_A79C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A79C)

    def lambda_A7A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A7A9)
    WaitChrThread(0x103, 2)
    Sleep(300)

    #N0312
    NpcTalk(
        0x14,
        "女性隊員",
        (
            "#5P#0506F──問題は、\x01",
            "３週間に渡って魔獣の正体が\x01",
            "突き止められなかったこと……\x02\x03",

            "そして、広範囲とはいえ、\x01",
            "実際の被害状況がそれほど\x01",
            "深刻ではなかったこと……\x02\x03",

            "#0501Fそれを理由に、司令閣下から\x01",
            "ストップがかかったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#12P#0001Fそうだったのか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x13,
        (
            "#5P#2005Fああ、そういえば、\x01",
            "紹介してなかったわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)

    def lambda_A918():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A918)

    def lambda_A925():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A925)

    def lambda_A932():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A932)
    Sleep(300)

    #C0315
    ChrTalk(
        0x13,
        (
            "#5P#2004F──彼女はノエル曹長。\x02\x03",

            "#2002Fまだ若いけど、戦闘能力、\x01",
            "運転技術共に優れていてね。\x02\x03",

            "私の護衛やサポートを\x01",
            "してもらっているわ。\x02",
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
    SetChrName("女性隊員")

    #A0316
    AnonymousTalk(
        0xFF,
        (
            "ノエル・シーカーです。\x01",
            "改めて、よろしくお願いします。\x02",
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
            "#12P#0000Fこちらこそ……\x01",
            "よろしくお願いします。\x02",
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
        "#12P#0005Fあれ、シーカーって……\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        (
            "#6P#0100Fひょっとして、警察本部の\x01",
            "受付をしているフランさんの？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x14,
        (
            "#5P#0509Fええ、姉になります。\x02\x03",

            "#0502Fいつも妹がお世話に\x01",
            "なっているみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#12P#0002Fはは、こちらこそ妹さんには\x01",
            "世話になりっぱなしですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x104,
        (
            "#0304F#12Pしかし、なるほど……\x01",
            "君がノエル曹長だったのか。\x02\x03",

            "#0300F聞いてるぜ。\x01",
            "タングラム門の女性隊員で\x01",
            "期待のホープがいるってな。\x02",
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
            "#5P#0504Fふふっ、自分の方も\x01",
            "ランディ先輩の名は伺ってます。\x02\x03",

            "#0500F色々な伝説をお持ちのようで……\x01",
            "一度お会いしたいと思ってました。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        "#0309F#12Pハハ、そいつは光栄だね。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        "#6P#0005F色々な伝説……？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        "#6P#0211Fやはり女性関係ですか？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        (
            "#0304F#12Pそうそう、俺がいかに\x01",
            "同僚の女性隊員にモテまくって\x01",
            "男どもから羨望の眼差しをだなぁ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(300)

    #C0328
    ChrTalk(
        0x13,
        (
            "#5P#2004F#5Pまあ、社交辞令は\x01",
            "そのくらいにするとして。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x104,
        "#0306F#12Pガクッ……\x02",
    )

    CloseMessageWindow()

    def lambda_AE7C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE7C)
    Sleep(50)

    def lambda_AE8C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AE8C)
    Sleep(50)

    def lambda_AE9C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AE9C)
    Sleep(50)

    def lambda_AEAC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AEAC)
    Sleep(50)
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(300)

    #C0330
    ChrTalk(
        0x13,
        (
            "#5P#2001F現状は伝えた通り……\x01",
            "ちょっとマズイ状況なのよ。\x02\x03",

            "打開できる要素があるとしたら\x01",
            "あなた達の調査結果くらい……\x02\x03",

            "正直、ワラにもすがる思いで\x01",
            "様子を確かめに来たってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#12P#0001Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        (
            "#6P#0103Fでは、調書の提出と合わせて\x01",
            "一通り説明させていただきます。\x02",
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
        "#5P#1003Fふむ……なるほどな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x13, 500)
    Sleep(300)

    #C0335
    ChrTalk(
        0x8,
        (
            "#6P#1002Fどうだ、ソーニャ。\x01",
            "ウチの小僧どもの手際は？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x13,
        (
            "#5P#2004F……期待以上ね。\x02\x03",

            "『神狼』の言い伝えに\x01",
            "病院屋上に現れたルート……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 400)
    Sleep(400)

    #C0337
    ChrTalk(
        0x13,
        "#5P#2000Fどうかしら、ノエル？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    #C0338
    ChrTalk(
        0x14,
        (
            "#11P#0506F……正直、驚きました。\x02\x03",

            "#0500Fやはり本職の捜査官は\x01",
            "目の付け所が違いますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x13,
        (
            "#5P#2000F目の付け所というより\x01",
            "発想法の違いでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)

    def lambda_B1EE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_B1EE)

    def lambda_B1FB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B1FB)
    Sleep(300)

    #C0340
    ChrTalk(
        0x13,
        (
            "#5P#2004F──うん、決めたわ。\x02\x03",

            "#2001Fあなた達には引き続き、\x01",
            "鉱山町方面の調査をお願いします。\x02\x03",

            "この調子だと、思いも寄らぬ\x01",
            "新事実が見えてくるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#12P#0005Fええ、こちらは\x01",
            "そのつもりでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#0301F#12P例の司令殿の命令を\x01",
            "無視することにならないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x13,
        (
            "#5P#2004Fふふ、あなた達への要請まで\x01",
            "取り下げろとは言われなかったもの。\x02\x03",

            "#2002F魔獣の手がかりが判明次第、\x01",
            "すぐに行動に移れるようにする──\x02\x03",

            "それなら問題ないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x104,
        "#0302F#12Pなるほどね。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        (
            "#6P#0102Fふふ、さすがに\x01",
            "やり手でいらっしゃいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x14,
        (
            "#5P#0503F……それにどうも、\x01",
            "魔獣たちに我々の動きを\x01",
            "感づかれているらしいんです。\x02\x03",

            "大部隊で捜索するよりも\x01",
            "少人数で行動したほうが\x01",
            "相手も隙を見せるかもしれない……\x02\x03",

            "#0500Fそれを期待したいところですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#12P#0000Fなるほど……分かりました。\x02\x03",

            "とにかくこれから、\x01",
            "鉱山町に足を運ぶつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x13,
        (
            "#5P#2000Fええ、お願いするわね。\x02\x03",

            "何か分かったらタングラム門の\x01",
            "副司令部に連絡してちょうだい。\x02",
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
            "#11P#2000Fそれじゃ、セルゲイ。\x01",
            "例の話はまた後日にでも。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x13, 500)

    #C0350
    ChrTalk(
        0x8,
        (
            "#6P#1003Fああ、了解した。\x02\x03",

            "#1000Fあんまり無理すんじゃねえぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x13,
        "#11P#2002Fふふ、そちらこそ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    #C0352
    ChrTalk(
        0x13,
        "#2000F#5Pノエル、失礼しましょう。\x02",
    )

    CloseMessageWindow()
    #Sound(1478, 255, 100, 0)    #voice#Noel

    #N0353
    NpcTalk(
        0x14,
        "女性隊員",
        "#0502F#5Pはいっ。\x02",
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

    def lambda_B6DF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_B6DF)
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

    def lambda_B72C():

        label("loc_B72C")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_B72C")

    QueueWorkItem2(0x8, 2, lambda_B72C)
    BeginChrThread(0x13, 3, 0, 22)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 22)
    Sleep(300)

    def lambda_B750():

        label("loc_B750")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_B750")

    QueueWorkItem2(0x101, 2, lambda_B750)

    def lambda_B762():

        label("loc_B762")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_B762")

    QueueWorkItem2(0x102, 2, lambda_B762)

    def lambda_B774():

        label("loc_B774")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_B774")

    QueueWorkItem2(0x103, 2, lambda_B774)

    def lambda_B786():

        label("loc_B786")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_B786")

    QueueWorkItem2(0x104, 2, lambda_B786)
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
        "#5P#0001F忙しそうだな……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        (
            "#5P#0103Fそうね……早朝に鉱山町から\x01",
            "撤収したばかりみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#5P#1003Fま、無能な上司に\x01",
            "振り回されてるみたいだからな。\x02\x03",

            "#1000Fそれでいて共和国方面への\x01",
            "警戒もおろそかにできねぇ……\x02\x03",

            "相変わらず貧乏クジを引いてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B8E9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B8E9)
    Sleep(50)

    def lambda_B8F9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B8F9)
    Sleep(50)

    def lambda_B909():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B909)
    Sleep(50)

    def lambda_B919():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B919)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0357
    ChrTalk(
        0x101,
        (
            "#11P#0003Fなるほど……\x02\x03",

            "#0005Fそういえば、課長と副司令って\x01",
            "お知り合いだったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x103,
        (
            "#12P#0200F何気に名前で\x01",
            "呼び合ってましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x104,
        (
            "#0303Fそういや俺を\x01",
            "ここに推薦してくれたのも\x01",
            "副司令だったんだよな。\x02\x03",

            "#0302F一体どういう関係なんスか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0360
    ChrTalk(
        0x8,
        "#5P#1003Fま、昔馴染みってやつだ。\x02",
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
            "#5P#1003Fふ～っ……\x02\x03",

            "#1002Fそれよりもお前ら、\x01",
            "昨日は大変だったらしいな。\x02\x03",

            "今日は鉱山町に行くみてぇだが\x01",
            "また歩いて行くつもりかよ？\x02",
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
            "#11P#0006Fいや、昨日はその\x01",
            "色々と偶然が重なって……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#12P#0100Fさすがに今日は、バスで\x01",
            "行こうと思っていますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#5P#1005Fなんだ、そうなのか？\x02\x03",

            "#1004Fクク、てっきり遊撃士あたりを\x01",
            "見習ってんのかと思ったぜ。\x02",
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
        "#12P#0205F遊撃士を見習う……？\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x104,
        "#0305Fどういう事ッスか？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#5P#1002F連中の習慣らしいが……\x01",
            "まず手始めに、自分の足だけで\x01",
            "周辺地域を一通り回ってみるらしい。\x02\x03",

            "#1004Fスタミナも付くし、\x01",
            "魔獣との実戦経験も積めるし、\x01",
            "何より土地勘が得られる……\x02\x03",

            "#1002F一石三鳥って理屈らしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        "#11P#0001F自分の足だけで周辺地域を……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x104,
        (
            "#0301Fなるほど……\x01",
            "連中、そんな事をしてんのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#12P#0201Fもしかして、昨日会った\x01",
            "エステルさんたちも……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#12P#0103F……さっそく徒歩で一通り\x01",
            "回るつもりだったのかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        (
            "#5P#1002Fクク、その２人だが……\x01",
            "どうやら大した経歴らしいぜ。\x02\x03",

            "なんでも去年起きた\x01",
            "リベールの異変を解決するのに\x01",
            "かなりの貢献をしたって話だ。\x02",
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
        "#11P#0001Fリベールの異変って……！\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        (
            "#12P#0205Fあの、王国中の導力が\x01",
            "動かなくなったっていう……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x104,
        "#0301Fおいおい、マジかよ……？\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        (
            "#12P#0106Fそれが本当なら……\x01",
            "相当な実力者なのも頷けますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#5P#1002Fま、このクロスベルじゃ\x01",
            "お前たちより新米ではあるんだ。\x02\x03",

            "あっという間に追い抜かれて\x01",
            "引き離されちまわないよう、\x01",
            "せいぜい気張っておくんだな。\x02\x03",

            "#1003F今回の件も、長引かせたら\x01",
            "間違いなくギルドが出張るだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            "#11P#0003F……分かりました。\x01",
            "解決に導けるよう努力します。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C19D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C19D)
    Sleep(150)

    def lambda_C1AD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C1AD)
    Sleep(50)

    def lambda_C1BD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C1BD)
    Sleep(50)

    def lambda_C1CD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C1CD)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0379
    ChrTalk(
        0x101,
        (
            "#5P#0001Fそれじゃあ、みんな。\x01",
            "鉱山町の方に行くとしよう。\x02\x03",

            "街の北口にある\x01",
            "バス停から出ているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        (
            "#6P#0101F切らした備品があれば\x01",
            "街で補充した方がいいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x103,
        (
            "#6P#0203F念のため、端末の方も\x01",
            "チェックしておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#0300F#12Pま、ボチボチ行くとするかね。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3E4")
    OP_29(0x8, 0x4, 0x40)
    Jump("loc_C3F6")

    label("loc_C3E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3F6")
    OP_29(0x8, 0x4, 0x40)

    label("loc_C3F6")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7103")
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_21_90EE end

    def Function_22_C412(): pass

    label("Function_22_C412")

    OP_92(0xFE, 0xF8D4, 0x1B58, 0x1F4)

    def lambda_C424():
        OP_95(0xFE, 63700, 0, 7300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C424)
    WaitChrThread(0xFE, 1)

    def lambda_C442():
        OP_95(0xFE, 61600, 0, 6100, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C442)
    WaitChrThread(0xFE, 1)

    def lambda_C460():
        OP_95(0xFE, 61600, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C460)
    WaitChrThread(0xFE, 1)

    def lambda_C47E():
        OP_95(0xFE, 59000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C47E)
    Sleep(500)

    def lambda_C49B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C49B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_C412 end

    def Function_23_C4B0(): pass

    label("Function_23_C4B0")


    def lambda_C4B5():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4B5)

    def lambda_C4CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C4CF)
    WaitChrThread(0x101, 1)

    def lambda_C4E4():
        OP_95(0xFE, 64099, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4E4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_23_C4B0 end

    def Function_24_C505(): pass

    label("Function_24_C505")


    def lambda_C50A():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C50A)

    def lambda_C524():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C524)
    WaitChrThread(0x102, 1)

    def lambda_C539():
        OP_95(0xFE, 62800, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C539)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_24_C505 end

    def Function_25_C55A(): pass

    label("Function_25_C55A")


    def lambda_C55F():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C55F)

    def lambda_C579():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C579)
    WaitChrThread(0x103, 1)

    def lambda_C58E():
        OP_95(0xFE, 62800, 30, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C58E)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_25_C55A end

    def Function_26_C5AF(): pass

    label("Function_26_C5AF")


    def lambda_C5B4():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C5B4)

    def lambda_C5CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C5CE)
    WaitChrThread(0x104, 1)

    def lambda_C5E3():
        OP_95(0xFE, 64099, 30, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C5E3)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_26_C5AF end

    def Function_27_C604(): pass

    label("Function_27_C604")

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

    def lambda_C7E8():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7E8)

    def lambda_C802():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C802)
    Sleep(250)

    def lambda_C816():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C816)

    def lambda_C830():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C830)
    Sleep(400)

    def lambda_C844():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C844)

    def lambda_C85E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C85E)
    Sleep(250)

    def lambda_C872():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C872)

    def lambda_C88C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C88C)
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
        "#12P#0011Fな……！？\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x102,
        "#0105Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x104,
        "#0307Fハア！？\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x103,
        "#4P#0205Fどうして……\x02",
    )

    CloseMessageWindow()

    def lambda_C980():
        OP_95(0xFE, 800, 0, 600, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C980)

    def lambda_C99A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C99A)
    WaitChrThread(0x8, 1)

    def lambda_C9AF():
        OP_95(0xFE, 2850, 0, 2000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C9AF)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    #C0387
    ChrTalk(
        0x8,
        (
            "#1011F#11Pやっぱりお前らの知り合いか。\x02\x03",

            "#1001Fいや、いきなり入ってくるから\x01",
            "思わず銃を抜いちまったが……\x02\x03",

            "気にした様子もなく、\x01",
            "そこに寝そべりやがるから\x01",
            "どうにも手を出しづらくてなぁ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CA92():
        OP_95(0xFE, -900, 0, 3000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CA92)
    WaitChrThread(0x103, 1)
    OP_68(1470, 700, 5610, 1000)

    def lambda_CAC1():
        OP_95(0xFE, 600, 0, 4500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CAC1)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0388
    ChrTalk(
        0x103,
        (
            "#11P#0205Fあなた、どうしたの……？\x02\x03",

            "なんでこんな場所に……\x02",
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
    SetChrName("白い狼")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            "#30Wグルルル……ウォン。\x02\x03",

            "グルルルルル……\x02",
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
        "#11P#0202Fあ……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#12P#0005F……ティオ。\x01",
            "彼は何て言ってるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    #C0392
    ChrTalk(
        0x103,
        (
            "#0204F#5P……えっと。\x02\x03",

            "#0202F『自分の名前は《ツァイト》。』\x02\x03",

            "『我々への濡れ衣を晴らしたこと、\x01",
            "  ご苦労だった。』\x02\x03",

            "#0204F──だそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#12P#0002F《ツァイト》……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        "#0102Fお、お礼を言いにきたの……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x104,
        (
            "#0309Fそ、それはともかく、\x01",
            "やっぱり偉そうなヤツだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xC,
        (
            "#5414F#5P#30Wグルルルルル……\x02\x03",

            "グルルルルルルル……\x02\x03",

            "#5413Fグルルル……ウォン。\x02",
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
        "#11P#0205Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        "#12P#0001Fど、どうしたんだ？\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    #C0399
    ChrTalk(
        0x103,
        (
            "#0208Fその……\x02\x03",

            "#0203F『だが、お前たちは若く\x01",
            "  どうにも頼りない……』\x02\x03",

            "『仕方ないからしばらく、\x01",
            "  自分が力を貸してやろう。』\x02\x03",

            "『気が向いた時に助けてやる。』\x02",
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
        "#12P#0011Fなっ！？\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#0105Fえええっ！？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x104,
        "#0307Fオイオイオイオイ！\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xC,
        (
            "#5414F#5P#30Wウルゥ……\x02\x03",

            "#5412Fグルルル……ウォン。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x103,
        (
            "#0204F#5P『心配はいらない。』\x02\x03",

            "『群れは部下に任せたから\x01",
            "  安心するがいい。』\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0405
    ChrTalk(
        0x101,
        (
            "#12P#0012Fいや、そんなことを\x01",
            "心配してるんじゃなくて！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)

    def lambda_D07E():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D07E)
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
            "#1004F#11Pクク、伝説の《神狼》か……\x02\x03",

            "#1002Fどうにも妙なのに\x01",
            "見込まれちまったみてぇだな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D1B1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D1B1)
    Sleep(50)

    def lambda_D1C1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D1C1)
    Sleep(50)

    def lambda_D1D1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D1D1)
    Sleep(50)

    def lambda_D1E1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D1E1)
    WaitChrThread(0x104, 2)

    #C0407
    ChrTalk(
        0x101,
        "#6P#0011F課長……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        (
            "#1002F#11Pとりあえず上には\x01",
            "《警察犬》で通しておいてやる。\x02\x03",

            "今後、どう付き合っていくかは\x01",
            "お前らで決めるといいだろう。\x02\x03",

            "#1004Fそんじゃ、俺は寝直すからな。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 28)
    Sleep(500)

    def lambda_D2B0():

        label("loc_D2B0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_D2B0")

    QueueWorkItem2(0x101, 2, lambda_D2B0)

    def lambda_D2C2():

        label("loc_D2C2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_D2C2")

    QueueWorkItem2(0x102, 2, lambda_D2C2)

    def lambda_D2D4():

        label("loc_D2D4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_D2D4")

    QueueWorkItem2(0x103, 2, lambda_D2D4)

    def lambda_D2E6():

        label("loc_D2E6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_D2E6")

    QueueWorkItem2(0x104, 2, lambda_D2E6)
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
        "#12P#0011Fちょ、ちょっと課長！？\x02",
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
        "#0301F面倒くさくなったな、ありゃ……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x102,
        "#0106Fふう……大丈夫なのかしら。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#0204F……わたしは賛成です。\x01",
            "頼りになってくれそうですし。\x02\x03",

            "#0202F何よりもこのマフマフした\x01",
            "白い毛並みは魅力的かと……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x102,
        (
            "#0109Fう、うーん……\x01",
            "それは否定しないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x104,
        (
            "#0302Fま、頼りになる助っ人が\x01",
            "増えたと思えばいいのかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        (
            "#6P#0006Fはあ……そうだな。\x02\x03",

            "#0000Fとりあえず、このままじゃマズイから\x01",
            "どこかで首輪でも買っておくか……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D58F")
    OP_29(0x5, 0x4, 0x40)
    Jump("loc_D5A1")

    label("loc_D58F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A1")
    OP_29(0x5, 0x4, 0x40)

    label("loc_D5A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5BF")
    OP_29(0x6, 0x4, 0x40)
    Jump("loc_D5D1")

    label("loc_D5BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5D1")
    OP_29(0x6, 0x4, 0x40)

    label("loc_D5D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5F4")
    OP_29(0x7, 0x4, 0x40)
    SubItemNumber(0x35B, 1)
    Jump("loc_D606")

    label("loc_D5F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D606")
    OP_29(0x7, 0x4, 0x40)

    label("loc_D606")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D624")
    OP_29(0x9, 0x4, 0x40)
    Jump("loc_D636")

    label("loc_D624")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D636")
    OP_29(0x9, 0x4, 0x40)

    label("loc_D636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D654")
    OP_29(0xA, 0x4, 0x40)
    Jump("loc_D666")

    label("loc_D654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D666")
    OP_29(0xA, 0x4, 0x40)

    label("loc_D666")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xB, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D678")
    OP_29(0xB, 0x4, 0x40)

    label("loc_D678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D696")
    OP_29(0xC, 0x4, 0x40)
    Jump("loc_D6A8")

    label("loc_D696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6A8")
    OP_29(0xC, 0x4, 0x40)

    label("loc_D6A8")

    SubItemNumber(0x2D5, 1)
    SubItemNumber(0x2D6, 1)
    SubItemNumber(0x2D7, 1)
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

    # Function_27_C604 end

    def Function_28_D786(): pass

    label("Function_28_D786")

    ClearChrFlags(0x8, 0x4)

    def lambda_D790():
        OP_95(0xFE, 2600, 850, 9000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D790)
    WaitChrThread(0x8, 1)

    def lambda_D7AE():
        OP_95(0xFE, 1300, 850, 10300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D7AE)
    WaitChrThread(0x8, 1)

    def lambda_D7CC():
        OP_95(0xFE, 1300, 2650, 13800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D7CC)
    Sleep(1500)

    def lambda_D7E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D7E9)
    WaitChrThread(0x8, 1)
    Return()

    # Function_28_D786 end

    def Function_29_D7FA(): pass

    label("Function_29_D7FA")

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

    def lambda_DA22():
        OP_96(0xFE, 0x1F4, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA22)

    def lambda_DA3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DA3C)
    Sleep(700)

    def lambda_DA50():
        OP_96(0xFE, 0x5DC, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DA50)

    def lambda_DA6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DA6A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    #C0416
    ChrTalk(
        0x101,
        "#0000F#5Pただいま。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x104,
        "#0300F#11P帰ったぜ～。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)

    #N0418
    NpcTalk(
        0x102,
        "エリィの声",
        "#3Pあら、お帰りなさい。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DB10():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB10)
    Sleep(50)

    def lambda_DB20():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DB20)
    OP_68(11100, 1950, 5700, 2000)
    MoveCamera(45, 19, 0, 2000)
    OP_6F(0x41)

    #C0419
    ChrTalk(
        0x101,
        (
            "#0005F#2Pなんだ。\x01",
            "エリィたちの方が先だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#11P#0104Fふふ、本部での簡単な\x01",
            "書類整理の手伝いだけだから。\x02\x03",

            "#0102Fそれでティオちゃんと\x01",
            "ランチの用意をしていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        "#0302F#2Pおっ、俺たちの分もあんの？\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)
    Sleep(300)

    #C0422
    ChrTalk(
        0x103,
        (
            "#0202F#5Pええ……簡単なパスタと\x01",
            "サラダで良ければですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0009F#9P十分さ。\x01",
            "ありがたくご馳走になるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x102,
        (
            "#11P#0109Fふふ、それじゃあ\x01",
            "２人とも手を洗って来てね。\x02",
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
            "#6P#0205Fそういえば……\x02\x03",

            "#0200Fロイドさんたちの方は\x01",
            "交通整理の手伝い、どうでした？\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#11P#0006Fああ、結構面倒だったかな。\x02\x03",

            "#0000F違法駐車してる導力車を\x01",
            "力任せで壁際まで移動させたんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0427
    ChrTalk(
        0x104,
        (
            "#6P#0300F歓楽街が多かったな。\x02\x03",

            "ちょうど公演前だから\x01",
            "盛り上がってるみたいだったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#0104F#11Pそういえば……\x01",
            "来月いよいよ公開されるのね。\x02\x03",

            "#0100F劇団《アルカンシェル》の新作が。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(200)

    #C0429
    ChrTalk(
        0x104,
        (
            "#6P#0300F『金の太陽、銀の月』だな。\x02\x03",

            "#0306F俺もチケット取りたかったんだが\x01",
            "あいにく来月分が全部完売でよ～。\x02\x03",

            "再来月の公演のＢ席が\x01",
            "やっと取れたくらいだったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    #C0430
    ChrTalk(
        0x103,
        (
            "#6P#0205F《アルカンシェル》というのは\x01",
            "そこまでの人気なんですか……\x02\x03",

            "#0203F確かに看板スターの\x01",
            "イリア・プラティエといえば\x01",
            "超が付くほどの有名人ですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0431
    ChrTalk(
        0x101,
        (
            "#5P#0003Fそういえば、アルカンシェルの\x01",
            "演目は見たことがあるけど……\x02\x03",

            "#0000Fイリア・プラティエの舞台は\x01",
            "俺も見たことがないんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0432
    ChrTalk(
        0x104,
        (
            "#6P#0306Fやれやれ、不憫#4Rふびん#なことだねぇ。\x02\x03",

            "#0301F──この世には２種類の人間がいる。\x02\x03",

            "#0304Fイリア・プラティエの舞台を見た者と、\x01",
            "そうでない者だ──\x01",
            "ｂｙランディ・オルランド。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        "#5P#0012Fそんな大げさな……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0434
    ChrTalk(
        0x102,
        (
            "#0102Fふふ、でも確かに凄いわよ。\x02\x03",

            "#0104F何ていうか……\x01",
            "一度、演技を目にしてしまったら\x01",
            "魂が鷲掴みにされてしまうような……\x02\x03",

            "#0100Fこの世に《天才》がいるとすれば\x01",
            "彼女は間違いなくその一人でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#5P#0005Fへえ……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        (
            "#6P#0202F……少し興味が出て来ました。\x02\x03",

            "#0206Fしかし、最近回ってくる仕事が\x01",
            "妙に多いとは思いましたが……\x02\x03",

            "#0200Fそれも原因の一つでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#0106Fまあ、クロスベルの創立記念祭と\x01",
            "アルカンシェルの新作のお披露目が\x01",
            "丁度重なってしまったから……\x02\x03",

            "#0100F例年よりも警察の業務が\x01",
            "忙しくなっているんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x104,
        (
            "#6P#0306Fま、こっちに回って来るのは\x01",
            "もっぱら雑用ばっかだけどなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        (
            "#5P#0012Fまあまあ。\x02\x03",

            "#0000Fそれでも一番最初よりは\x01",
            "責任のある仕事も来ているしさ。\x02\x03",

            "クロスベルタイムズでも\x01",
            "皮肉っぽくは書かれなくなったし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0440
    ChrTalk(
        0x103,
        (
            "#6P#0203F……それでも、いまだに\x01",
            "遊撃士とは比較されていますが。\x02\x03",

            "#0211F特にあの、エステルさんたちと……\x02",
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
            "#5P#0006Fはあ……そうなんだよな。\x02\x03",

            "#0001Fあっちは２人だけなのに\x01",
            "何であそこまで活躍できるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x102,
        (
            "#0108F他の遊撃士と連携しているから\x01",
            "効率的に動けているのかも……\x02\x03",

            "#0106F私たちは４人だけど\x01",
            "他の課のバックアップはないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x104,
        (
            "#6P#0303Fいや、見たところ、\x01",
            "鍵はあのヨシュアって野郎だな。\x02\x03",

            "突っ走りがちなエステルちゃんを\x01",
            "実に効率的にフォローしてるぜ。\x02\x03",

            "#0301F戦闘にしても仕事全般にしても\x01",
            "息の合い方が尋常じゃねえ。\x02\x03",

            "加えて、踏んだ場数の多さだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        (
            "#6P#0206Fということは、わたしたちも\x01",
            "まだまだという事ですか……\x02",
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
            "#5P#0012Fま、まあ……\x01",
            "俺たちだって十分成長してるさ。\x02\x03",

            "#0000Fこの前から、頼りになる助っ人も\x01",
            "来てくれていることだし──\x02",
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
        "#11P#0005F……そういや、ツァイトは？\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x102,
        (
            "#0105F今日は見てないわね……\x02\x03",

            "#0100F昨日は屋上で一日中、\x01",
            "日向ぼっこをしてたみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x104,
        (
            "#6P#0306F魔獣との戦闘になった時に\x01",
            "助けてくれるのはいいんだが……\x02\x03",

            "#0300Fいったい普段、何してんだか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0449
    ChrTalk(
        0x103,
        (
            "#6P#0204F……彼は誇り高いですから。\x02\x03",

            "わたしたち人間の決めたルールに\x01",
            "縛ろうとしても無意味かと……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        (
            "#11P#0006Fいや、警察犬として登録してる以上\x01",
            "最低限のルールは守って欲しいんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0451
    ChrTalk(
        0x101,
        (
            "#5P#0000Fしかし最初は、周辺の住民に\x01",
            "怖がられるかと思ったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x104,
        (
            "#6P#0302Fまさか車の事故から\x01",
            "子供を救っちまうなんてなぁ。\x02",
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
            "#0103Fハンドルを切り損ねて\x01",
            "フェンスにぶつかった運搬車……\x02\x03",

            "#0102F最初、何の音かと思ったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0454
    AnonymousTalk(
        0x101,
        (
            "#0004Fそれで慌てて外に出たら\x01",
            "轢かれそうになってたリュウを\x01",
            "ツァイトが颯爽と助けてるし……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0455
    AnonymousTalk(
        0x104,
        (
            "#0309Fいや、あのアリオスのオッサンと\x01",
            "良い勝負の活躍だったんじゃねぇか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0456
    AnonymousTalk(
        0x103,
        "#0202F……ですね。\x02",
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
            "#0104Fふふ……あれ以来、\x01",
            "西通りの人に特に人気ね。\x02\x03",

            "#0102Fリュウ君たちも\x01",
            "すごく懐いているみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#5P#0004Fはは、そうだな。\x02\x03",

            "#0000Fま、あんまりツァイトの人気に\x01",
            "頼るわけにはいかないし……\x02\x03",

            "俺たちは俺たちで頑張るとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        "#6P#0204F……賛成です。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x104,
        (
            "#6P#0300Fそんじゃあ午後からは\x01",
            "支援要請を片付けるとすっか。\x02",
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
            "ティオが特殊クラフト\x01",
            "『ツァイト召喚』を覚えました。\x02",
        )
    )

    CloseMessageWindow()

    #A0462
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戦闘中に使用すると\x01",
            "ＡＴバーのところにツァイトが現れ、\x01",
            "順番が回ると支援行動をしてくれます。\x02",
        )
    )

    CloseMessageWindow()

    #A0463
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお、ストーリーの進行上、\x01",
            "このクラフトを使用できない場合もあります。\x07\x00\x02",
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

    # Function_29_D7FA end

    def Function_30_F01A(): pass

    label("Function_30_F01A")

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

    def lambda_F172():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F172)
    Sleep(50)

    def lambda_F182():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F182)
    Sleep(50)

    def lambda_F192():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F192)
    Sleep(50)

    def lambda_F1A2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F1A2)
    WaitChrThread(0x101, 2)

    #C0464
    ChrTalk(
        0x101,
        "#6P#0005Fおっと……\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x102,
        "#6P#0100Fもう来てたみたいね。\x02",
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
        "紫髪の娘",
        "#5Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(620, 1000, 2850, 1500)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_F252():
        OP_95(0xFE, 880, 0, 4250, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F252)

    def lambda_F26C():

        label("loc_F26C")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_F26C")

    QueueWorkItem2(0x101, 2, lambda_F26C)

    def lambda_F27E():

        label("loc_F27E")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_F27E")

    QueueWorkItem2(0x102, 2, lambda_F27E)

    def lambda_F290():

        label("loc_F290")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_F290")

    QueueWorkItem2(0x103, 2, lambda_F290)

    def lambda_F2A2():

        label("loc_F2A2")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_F2A2")

    QueueWorkItem2(0x104, 2, lambda_F2A2)
    WaitChrThread(0x15, 1)
    TurnDirection(0x15, 0x101, 500)
    OP_6F(0x1)

    #N0467
    NpcTalk(
        0x15,
        "紫髪の娘",
        (
            "#1805F#5Pす、すみません……！\x02\x03",

            "#1803F勝手に上がりこんでしまって\x01",
            "……その……\x02",
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
            "#12P#0004Fああ、いいですよ。\x01",
            "話は聞いていますから。\x02\x03",

            "#0002F相談者の方ですよね？\x01",
            "ようこそ、特務支援課へ。\x02",
        )
    )

    CloseMessageWindow()

    #N0469
    NpcTalk(
        0x15,
        "紫髪の娘",
        "#1802F#5Pほっ……\x02",
    )

    CloseMessageWindow()
    #Sound(1636, 255, 100, 0)    #voice#Rixia
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrName("紫髪の娘")

    #A0470
    AnonymousTalk(
        0xFF,
        (
            "あの、リーシャ・マオといいます。\x02\x03",

            "本日は相談に乗っていただき\x01",
            "ありがとうございました……！\x02",
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
        "#12P#0005F（うわ……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 20, -1, -1)

    #A0472
    AnonymousTalk(
        0x104,
        "#0301F（こ、こいつはまた……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0473
    AnonymousTalk(
        0x103,
        "#0205F#12P（とらんじすたぐらまーです……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0474
    AnonymousTalk(
        0x102,
        (
            "#0106F（ふう……\x01",
            "  あんまり露骨に見つめないの。）\x02\x03",

            "#0111F（──ちょっとロイド？）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 80, -1, -1)

    #A0475
    AnonymousTalk(
        0x101,
        "#12P#0011F（はっ……）\x02",
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
            "#12P#0003Fと、とりあえず\x01",
            "そちらにおかけください。\x02\x03",

            "#0000Fまずは一通りお話を伺います。\x02",
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

    # Function_30_F01A end

    def Function_31_F696(): pass

    label("Function_31_F696")

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
        "#0005F#6Pおっと……\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x102,
        "#0100Fもう来てたみたいね。\x02",
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
        "紫髪の娘",
        "#2Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(900, 1850, 7450, 1500)
    SetCameraDistance(26000, 1500)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_F893():
        OP_95(0xFE, 1150, 0, 6330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F893)

    def lambda_F8AD():
        OP_96(0xFE, 0x76C, 0x352, 0x20D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F8AD)
    Sleep(50)

    def lambda_F8CA():
        OP_96(0xFE, 0x2BC, 0x352, 0x20D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F8CA)
    Sleep(100)

    def lambda_F8E7():
        OP_96(0xFE, 0x76C, 0x352, 0x2580, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F8E7)
    Sleep(50)

    def lambda_F904():
        OP_96(0xFE, 0x2BC, 0x352, 0x2580, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F904)
    WaitChrThread(0x15, 1)
    TurnDirection(0x15, 0x101, 500)
    OP_6F(0x1)

    #N0480
    NpcTalk(
        0x15,
        "紫髪の娘",
        (
            "#1805F#2Pす、すみません……！\x02\x03",

            "#1806F勝手に上がりこんでしまって\x01",
            "……その……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        (
            "#5P#0004Fああ、いいですよ。\x01",
            "話は聞いていますから。\x02\x03",

            "#0002F相談者の方ですよね？\x01",
            "ようこそ、特務支援課へ。\x02",
        )
    )

    CloseMessageWindow()

    #N0482
    NpcTalk(
        0x15,
        "紫髪の娘",
        "#2P#1802Fほっ……\x02",
    )

    CloseMessageWindow()
    #Sound(1636, 255, 100, 0)    #voice#Rixia
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrName("紫髪の娘")

    #A0483
    AnonymousTalk(
        0xFF,
        (
            "あの、リーシャ・マオといいます。\x02\x03",

            "本日は相談に乗っていただき\x01",
            "ありがとうございました……！\x02",
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
        "#12P#0005F（うわ……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 20, -1, -1)

    #A0485
    AnonymousTalk(
        0x104,
        "#0301F（こ、こいつはまた……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0486
    AnonymousTalk(
        0x103,
        "#0205F#12P（とらんじすたぐらまーです……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    #A0487
    AnonymousTalk(
        0x102,
        (
            "#0106F（ふう……\x01",
            "  あんまり露骨に見つめないの。）\x02\x03",

            "#0111F（──ちょっとロイド？）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 80, -1, -1)

    #A0488
    AnonymousTalk(
        0x101,
        "#12P#0011F（はっ……）\x02",
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
            "#0003F#5Pと、とりあえず\x01",
            "そちらにおかけください。\x02\x03",

            "#0000Fまずは一通りお話を伺います。\x02",
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

    # Function_31_F696 end

    def Function_32_FCE9(): pass

    label("Function_32_FCE9")

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
        "#0013F──脅迫状！？\x02",
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
            "#1P#1803Fはい……１週間前のことです。\x02\x03",

            "イリアさんの元に\x01",
            "差出人不明の手紙が届いて……\x02\x03",

            "#1805Fあ、イリアさんというのは、\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x104,
        (
            "#0303F《炎の舞姫》の異名を持つ\x01",
            "劇団アルカンシェルの大スター。\x02\x03",

            "#0301F国際的な知名度を誇る\x01",
            "看板女優にしてアーティスト。\x02\x03",

            "#0309Fいや～！\x01",
            "まさかイリア・プラティエ絡みの\x01",
            "相談事が回ってくるとはねぇ！\x02",
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
            "#12P#0203Fランディさん……\x01",
            "少し落ち着いてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x101,
        (
            "#11P#0003Fその、さすがに有名人ですから\x01",
            "名前くらいは知っていますが……\x02\x03",

            "#0001Fしかし……\x01",
            "その彼女あてに脅迫状が？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x15,
        (
            "#1P#1803Fはい……本人はただの\x01",
            "イタズラだと言ってますけど……\x02\x03",

            "ちょっと不気味な文面で……\x01",
            "ただのイタズラには思えなくって。\x02\x03",

            "#1801Fそれで劇団長とも話し合って\x01",
            "とにかく警察に相談してみようって。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        "#6P#0101F……脅迫状の現物はどちらに？\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x15,
        (
            "#1P#1806Fその……\x01",
            "イリアさん自身が持っています。\x02\x03",

            "すぐに捨てようとしていた所を\x01",
            "何とか止めはしたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうなると、まずはその脅迫状を\x01",
            "見せてもらう必要がありますね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0499
    ChrTalk(
        0x101,
        (
            "#11P#0005Fそういえば……\x01",
            "リーシャさんと言いましたか。\x02\x03",

            "#0000F当然、《アルカンシェル》の\x01",
            "関係者なんですよね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    Sleep(300)

    #C0500
    ChrTalk(
        0x15,
        (
            "#1P#1802Fあ、はい。\x01",
            "一応アーティストの一人です。\x02\x03",

            "#1809Fその……\x01",
            "まだまだ新米なんですけど。\x02",
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
        "#0305F#4Sって、ああ！\x02",
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
        "#5P#0011Fな、何だよ、さっきから。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x104,
        (
            "#0301F君の顔、新作の特集ページで\x01",
            "見かけたことがあるぜ！\x02\x03",

            "#0303Fイリア演じる《太陽の姫》と対になる\x01",
            "《月の姫》を演じる準主役……\x02\x03",

            "#0302Fイリア・プラティエが大抜擢した\x01",
            "彗星のごとく現れた大型新人って！\x02",
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
            "#1P#1805Fそ、そんな、大型新人なんて。\x02\x03",

            "#1806Fまだまだ稽古不足で……\x01",
            "足を引っ張ってばかりなんです。\x02\x03",

            "#1808F本当はデビューなんて\x01",
            "早いと思ってるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x102,
        (
            "#6P#0109Fふふっ、それでも凄いですよ。\x02\x03",

            "#0102Fあのアルカンシェルに採用されて\x01",
            "デビューするんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x15,
        "#1P#1806Fううっ……\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#11P#0004Fはは……大体分かりました。\x02\x03",

            "#0001Fしかし話を聞いていると\x01",
            "イリアさん本人は、この件について\x01",
            "乗り気ではないみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x15,
        (
            "#1P#1808Fはい……とにかく今は、\x01",
            "舞台の完成度を高めたいから\x01",
            "外部の人間は入れたくないって……\x02\x03",

            "#1806F特にその……\x01",
            "警察なんか言語道断だって……\x02",
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
        "#11P#0011Fえっと……\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        (
            "#12P#0211Fそれではわたしたちも\x01",
            "出る幕など無いのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x15,
        (
            "#1P#1802Fで、でも皆さんは\x01",
            "《特務支援課》なんですよね？\x02\x03",

            "雑誌で読んだ限り、\x01",
            "なんだか普通の警察の方よりも\x01",
            "親しみやすそうっていうか……\x02\x03",

            "#1809Fその、イリアさんも\x01",
            "納得してくれるんじゃないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        "#11P#0003Fう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x102,
        (
            "#6P#0100Fこう言っては何ですけど……\x01",
            "遊撃士協会の方には相談は？\x02\x03",

            "イリアさんは民間人ですし……\x01",
            "彼らの護衛対象になると思いますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x15,
        (
            "#1P#1808Fそ、それはその……\x02\x03",

            "#1803Fクロスベルで遊撃士協会は\x01",
            "とても人気があるみたいですから……\x02\x03",

            "公演前にそんな人たちが出入りしたら\x01",
            "変に噂になってしまいそうで……\x02\x03",

            "#1802Fその点、皆さんならそこまで\x01",
            "話題にはならないかと思って……\x02",
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
            "#1P#1801Fす、すみません！\x01",
            "私ったら失礼なことを……！\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        (
            "#11P#0012Fい、いやあ。\x01",
            "全然気にしてませんよ。\x02\x03",

            "#0000Fそれよりも……\x01",
            "大体の事情は了解しました。\x02",
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
            "#5P#0000F……この件、\x01",
            "引き受けようかと思うんだけど\x01",
            "みんな、どうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        "#6P#0102Fもちろん私は賛成よ。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x103,
        "#12P#0204Fわたしも異存ナシです。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0520
    ChrTalk(
        0x104,
        (
            "#0309Fいや、むしろ\x01",
            "断るなんてあり得ないだろ！\x02",
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
            "#11P#0004Fというわけで、リーシャさん。\x02\x03",

            "#0000F脅迫状の件、特務支援課が\x01",
            "引き受けさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    Sleep(200)

    #C0522
    ChrTalk(
        0x15,
        (
            "#1P#1802Fあ、ありがとうございます！\x02\x03",

            "#1809Fそれでは私……\x01",
            "一足先に劇団に戻ります。\x02\x03",

            "劇団長とイリアさんには\x01",
            "私の方から報告しておきますので\x01",
            "いつ来ていただいても大丈夫です。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x102,
        "#6P#0102Fええ、分かりました。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0524
    ChrTalk(
        0x104,
        "#0309Fまったねー、リーシャちゃん！\x02",
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

    def lambda_10DD9():
        OP_95(0xFE, 3600, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10DD9)
    WaitChrThread(0x15, 1)

    def lambda_10DF7():
        OP_95(0xFE, 1000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10DF7)
    Sleep(500)
    SetChrSubChip(0x103, 0x1)
    Sleep(500)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x15, 1)

    def lambda_10E23():
        OP_95(0xFE, 1000, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10E23)
    Sleep(500)
    Sound(103, 0, 100, 0)

    def lambda_10E46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_10E46)
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
            "#5P#0003Fさてと……\x01",
            "とりあえず劇団に行ってみよう。\x02\x03",

            "#0000F脅迫状を見せてもらわない事には\x01",
            "始まらないしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x103,
        (
            "#12P#0204Fそうですね。\x02\x03",

            "#0202Fただのイタズラの可能性も\x01",
            "ありそうですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        (
            "#0302Fいや～、しかし役得だなぁ！\x02\x03",

            "公演直前のアルカンシェルに\x01",
            "入れる機会があるなんてよ！\x02\x03",

            "#0309Fしかも生イリアだぜ、生イリア！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0528
    ChrTalk(
        0x102,
        (
            "#6P#0108F確かに……\x01",
            "あのイリア・プラティエから\x01",
            "直接話を聞くかもしれないのよね。\x02\x03",

            "#0106Fちょっと緊張してきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        (
            "#5P#0005Fそ、そんなにか？\x02\x03",

            "#0006Fうーん、雑誌とかで見る限り\x01",
            "確かに美人だとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x103,
        "#12P#0202F……ちょっと楽しみです。\x02",
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

    # Function_32_FCE9 end

    def Function_33_111DF(): pass

    label("Function_33_111DF")

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
            "なるほど……\x01",
            "ま、事情は大体判ったぜ。\x02\x03",

            "それで？\x01",
            "このまま泣き寝入りすんのか？\x02",
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
            "#12P#0006Fな、泣き寝入りって……\x02\x03",

            "#0001F一課が出張ってきたのに\x01",
            "俺たちの立場で\x01",
            "食い下がれるものなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x8,
        (
            "#5P#1003Fま、無理だろうな。\x02\x03",

            "#1000F大方、あのキツネあたりが\x01",
            "しゃしゃり出てきて厳重注意だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        "#12P#0006Fですよね……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#12P#0200Fなら、一課の手伝いを\x01",
            "申し出るのはどうでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x104,
        (
            "#0306Fいや、あの眼鏡スーツ野郎の\x01",
            "態度を見る限り難しいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "#5P#1000Fああ、多分な。\x02\x03",

            "#1003F警察のナワバリ意識ってのは\x01",
            "結構やっかいなもんだ。\x02\x03",

            "特に一課はエリートだから\x01",
            "お前らみたいなガキの手伝いなんざ\x01",
            "断固拒否してくるだろうぜ。\x02\x03",

            "#1002F──ただし、\x01",
            "黙ってやる分には話が別だ。\x02",
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
        "#12P#0011Fえ……\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        (
            "#5P#1004Fクク……この特務支援課は\x01",
            "ある意味、規格外の部署だ。\x02\x03",

            "本部からハブられてはいるが\x01",
            "それは逆に、ある程度の裁量が\x01",
            "任されているとも解釈できる。\x02\x03",

            "#1002Fそれこそ黙ってやる分には\x01",
            "他の部署のナワバリを\x01",
            "踏み越えられるくらいにはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#12P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        (
            "#0305Fオイオイ……\x01",
            "そんな事言っていいのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x103,
        "#12P#0211Fとんだ不良上司ですね……\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x8,
        (
            "#5P#1004Fクク、言っただろう？\x02\x03",

            "俺は基本的に手は貸さねぇが\x01",
            "尻拭いだけはしてやるってな。\x02\x03",

            "#1002F腹を括って動くのはお前らだ。\x02",
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
            "#5P#1003Fまあ、そうは言っても\x01",
            "その調子じゃ無理だろうがな。\x02\x03",

            "#1000Fなにせ仲間うちに\x01",
            "迷ってるヤツがいるくらいだ。\x02\x03",

            "チーム一丸となって\x01",
            "腹を括れる状態じゃねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        "#12P#0006F……それは………\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x104,
        (
            "#0306Fまあ、お嬢があの調子だと\x01",
            "どうにも調子が出ねぇよな。\x02\x03",

            "#0308Fなんかこう、ピリッと\x01",
            "引き締まらねぇっていうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x103,
        (
            "#12P#0208F確かに今日一日、\x01",
            "そんな感じはしていました……\x02\x03",

            "#0206F……エリィさん、\x01",
            "大丈夫なんでしょうか……？\x02",
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

    def lambda_11A8B():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11A8B)
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

    # Function_33_111DF end

    def Function_34_11B3E(): pass

    label("Function_34_11B3E")

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
            "#0103F──でも、それはおかしいわ。\x02\x03",

            "#0101F今回、一課が出てきたのは\x01",
            "あくまで結果でしかない。\x02\x03",

            "リーシャさんが気を利かせて\x01",
            "私たちに頼まなかったら\x01",
            "表に出なかったわけなんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#5P#0006Fうーん、確かに……\x02\x03",

            "#0008Fとなると、一課の目を欺く\x01",
            "陽動っていう線は無いか……\x02\x03",

            "#0001Fそもそも《銀#2Rイン#》の存在を\x01",
            "知っている人間は誰なんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#0103Fそうね……雇い主である\x01",
            "《黒月#4Rヘイユエ#》は当然として。\x02\x03",

            "やり合っている《ルバーチェ》と\x01",
            "動向を追っている捜査一課……\x02\x03",

            "#0100Fあとは、ルバーチェと関係のある\x01",
            "ハルトマン議長も知っていそうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0553
    ChrTalk(
        0x101,
        (
            "#5P#0005Fハルトマン議長って……\x01",
            "昨日も言っていた？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x102,
        (
            "#0106Fええ、帝国派のリーダーにして\x01",
            "議会を牛耳っている大物政治家よ。\x02\x03",

            "多分、ルバーチェ最大の\x01",
            "後ろ盾と言ってもいい存在ね。\x02\x03",

            "#0101Fちなみに、おじいさまの改革案は\x01",
            "ほぼ全てこの人に潰されているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x101,
        (
            "#5P#0008Fそうなのか……\x01",
            "名前くらいしか知らなかったけど。\x02\x03",

            "#0001Fそうなると、《銀》にとっては\x01",
            "逆に敵対勢力になるってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        "#0106Fええ……関係は薄そうね。\x02",
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
        "#11P#0005Fティオ、ランディ？\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#0105F#11Pどうしたの？\x01",
            "狐につままれた顔をして。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        "#6P#0306Fいや……だって、なあ。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x103,
        (
            "#6P#0202Fエリィさん……\x01",
            "今日はすごく元気ですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0561
    ChrTalk(
        0x102,
        (
            "#0105F#11Pあ、うん……\x02\x03",

            "#0106F──ごめんなさい。\x01",
            "昨日はどうかしていたわ。\x02\x03",

            "#0100Fでも、もう大丈夫。\x01",
            "足手まといにはならないから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0562
    ChrTalk(
        0x101,
        (
            "#5P#0003Fだからエリィ……\x01",
            "足手まといなんて言うなって。\x02\x03",

            "#0000Fむしろ俺たちの方が\x01",
            "色々助けてもらってるんだからさ。\x02\x03",

            "今だってほら、エリィがいると\x01",
            "推理もはかどって助かってるし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0563
    ChrTalk(
        0x102,
        "#0102Fそ、そうかしら……\x02",
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
        "#6P#0301F……怪しい。\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x103,
        "#6P#0211F……妖しいです。\x02",
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
        "#11P#0005Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x102,
        "#0112F#11Pちょ、ちょっと……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x104,
        (
            "#6P#0303Fそういや昨日の夜……\x01",
            "屋上から話し声が聞こえたな。\x02\x03",

            "#0302Fひょっとして……\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x103,
        (
            "#6P#0202F……なるほど。\x02\x03",

            "#0204Fおめでとうございます。\x01",
            "ロイドさん、エリィさん。\x02",
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
            "#11P#0011Fい、いや、別にお祝いを\x01",
            "言われるような事はしてないぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x102,
        (
            "#0112F#11Pそ、そうよ……\x02\x03",

            "#0113Fただちょっと、\x01",
            "色々話したっていうだけで……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x104,
        (
            "#6P#0302Fなるほど、色々ねぇ。\x02\x03",

            "#0309F──で、どこまで行ったんだ？\x02",
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
        "#5P#0007Fランディ！\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x102,
        (
            "#0112F#11Pちょ、ちょっと！\x01",
            "ティオちゃんもいるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x103,
        (
            "#6P#0205Fどこまで行った……\x02\x03",

            "#0204Fああ、お付き合いの過程で\x01",
            "色々な段階を踏むという──\x02",
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
        "#11P#0012Fいやいや、無いから！\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x104,
        "#6P#0309Fひゅーひゅー。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x103,
        "#6P#0202F……ひゅーひゅー。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x3E8, 0x5DC)

    #C0579
    ChrTalk(
        0x102,
        "#0109F#4S#90W#11Pい い か げ ん に し な さ い。#20W\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x104,
        "#6P#0306Fはい……\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x101,
        (
            "#11P#0006Fまったく……\x02\x03",

            "俺とエリィの関係を疑うなんて\x01",
            "そんなのあり得ないだろう？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)

    #C0582
    ChrTalk(
        0x102,
        "#0105F#40W………え…………#20W\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#11P#0012Fそもそも釣り合わないっていうか\x01",
            "そんな雰囲気にならないっていうか……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0584
    ChrTalk(
        0x101,
        "#5P#0000Fなあ、エリィ？\x02",
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
        "#5P#0005F……あれ。\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x104,
        "#6P#0306F（おいおい……）\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x103,
        "#6P#0211F（踏みましたね……）\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        (
            "#0104F#40W……そうね、そうよね……\x02\x03",

            "ただお話して、つまらない相談に\x01",
            "乗ってもらっただけだものねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)

    #C0590
    ChrTalk(
        0x102,
        (
            "#0101F#4Sええ、そんな甘い雰囲気には\x01",
            "全くもってなりませんでしたとも！\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x101,
        (
            "#5P#0011F……え、えっと……\x02\x03",

            "#0012Fあの、釣り合わないってのは\x01",
            "俺がエリィには似合わないって\x01",
            "言ってるだけで……\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x102,
        "#0111Fギロッ……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x101,
        "#5P#0006F……すみません。\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#6P#0309Fくっくっくっ……\x02\x03",

            "#0302Fまあ、なんだ。\x01",
            "元気が出て何よりじゃねえか？\x02",
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
        "#0105F#11Pあ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)

    #C0596
    ChrTalk(
        0x103,
        (
            "#6P#0204F……安心しました。\x02\x03",

            "#0208Fひょっとして警察……\x01",
            "辞めてしまうんじゃないかって\x01",
            "思ったので……\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x102,
        (
            "#0106F#11P……ごめんね、心配かけて。\x02\x03",

            "#0102F将来、どうするかは\x01",
            "まだ分からないけれど……\x02\x03",

            "今、私がいるべき場所は\x01",
            "ここであるのは間違いないから。\x02\x03",

            "#0104Fだからみんな……\x01",
            "改めてよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        "#5P#0002Fエリィ……\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x103,
        "#6P#0202F……エリィさん。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x104,
        (
            "#6P#0309Fはは、お嬢の突っ込みがないと\x01",
            "やっぱり締まらねぇもんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        (
            "#0111F#11P突っ込ませているのは\x01",
            "貴方たちが原因でしょう……\x02\x03",

            "#0103F──まあ、それはともかく。\x02\x03",

            "#0101F捜査方針だけど\x01",
            "結局、どうしようかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        "#5P#0003Fそうだな……\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x103,
        (
            "#6P#0206F一課とは別のアプローチで\x01",
            "《銀》に迫ると言っても……\x02\x03",

            "色々切り口があるので\x01",
            "逆に迷ってしまいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x104,
        (
            "#6P#0303Fこうなったら、あれだ。\x02\x03",

            "#0300Fカルバードの東方人街に\x01",
            "出張しに行くってのはどうだ？\x02\x03",

            "少しは《銀》の手がかりも\x01",
            "掴めるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        "#5P#0005Fそ、それは盲点だったな。\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x102,
        (
            "#0101F#11Pでも、外国に出張なんて\x01",
            "そんなの許されるのかしら？\x02\x03",

            "支援課の範疇から\x01",
            "外れそうな気がするし……\x02",
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

    def lambda_12F25():
        OP_95(0xFE, 16100, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12F25)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    WaitChrThread(0x103, 1)

    def lambda_12F5C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12F5C)
    OP_6F(0x51)

    #C0608
    ChrTalk(
        0x101,
        "#0005Fティオ……？\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        "#0105F#5Pどうしたの？\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x103,
        (
            "#0200F警察のデータベースを\x01",
            "もう少し漁ってみようかと。\x02\x03",

            "一課の動向なども\x01",
            "掴めるかもしれませんし……\x02\x03",

            "#0203Fただ、昨夜調べたばかりなので\x01",
            "追加情報はないかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#0001Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x104,
        "#1P#0300Fま、やらないよりマシか。\x02",
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

    def lambda_1310D():
        OP_95(0xFE, 15200, 850, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1310D)
    WaitChrThread(0x101, 1)

    def lambda_1312B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1312B)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    Sound(824, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0613
    ChrTalk(
        0x103,
        "#0205Fあ……\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x101,
        "#6P#0001Fどうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x103,
        (
            "#0202F……珍しいですね……\x02\x03",

            "導力メールが\x01",
            "届いているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x101,
        "#6P#0005F導力メール？\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x102,
        (
            "#6P#0100F確か、文章だけの情報を\x01",
            "端末に送るものだったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x103,
        (
            "#0206Fはい、すごく便利なのに\x01",
            "警察では使っている人が\x01",
            "殆んどいないみたいで……\x02\x03",

            "キーボードが使える人が\x01",
            "まだ少ないせいでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x101,
        (
            "#6P#0006Fなるほど……\x01",
            "確かに俺も使えないしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x104,
        "#0300Fそれより、誰からなんだ？\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x103,
        "#0202F今、開いてみます。\x02",
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
        "#0205F…………え………………\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        "#6P#0005Fなんだ……？\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x102,
        (
            "#6P#0105Fいったい誰から──\x02\x03",

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
            "《銀》より支援要請あり。\x01",
            "試練を乗り越え、我が元へ参ぜよ。\x01",
            "さすれば汝らに使命を授けん。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0626
    AnonymousTalk(
        0x101,
        "#0007Fこ、これは……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0627
    AnonymousTalk(
        0x104,
        (
            "#0307Fおいおい……\x01",
            "何のイタズラだ、こりゃ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0628
    AnonymousTalk(
        0x102,
        (
            "#0101Fティオちゃん……\x01",
            "このメールはどこから！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0629
    AnonymousTalk(
        0x103,
        "#0201F警察本部ではありません……\x02",
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
            "#0205F……分かりました。\x02\x03",

            "#0203F《クロスベル国際銀行》\x01",
            "（International Bank of Crossbell）……\x02\x03",

            "#0201F──通称ＩＢＣです。\x02",
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
        "#6P#0013F……どういう事だ……？\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x104,
        (
            "#0301FＩＢＣっていやあ、大陸中から\x01",
            "ミラをかき集めてる銀行だろ？\x02\x03",

            "何でそんなところが\x01",
            "こんなイタズラを送って来るんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x103,
        (
            "#0206F……わたしに聞かれても。\x02\x03",

            "#0201Fでも、このメールは間違いなく\x01",
            "ＩＢＣの端末から送られています。\x02\x03",

            "誰が送ったのかまでは判りませんが。\x02",
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
            "#6P#0008Fもしかして《銀》が\x01",
            "ＩＢＣに潜入しているとか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    #C0635
    ChrTalk(
        0x102,
        (
            "#12P#0103F正直、あり得なくはないわね。\x02\x03",

            "#0101FそれにＩＢＣビルには\x01",
            "外部の会社も幾つか入っているわ。\x02\x03",

            "確か……エプスタイン財団の\x01",
            "事務所もあったんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(150)

    #C0636
    ChrTalk(
        0x103,
        (
            "#0203Fええ……\x01",
            "知り合いがそこで働いています。\x02\x03",

            "#0200Fですが……どうやらこのメールは\x01",
            "ＩＢＣのメイン端末から\x01",
            "送信されているみたいですね。\x02\x03",

            "外部の会社が関わっている\x01",
            "可能性は低いと思いますが……\x02",
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
            "#6P#0006F……直接聞いてみるしかないか。\x02\x03",

            "なるべく一課には内密に\x01",
            "捜査を進めたかったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    #C0638
    ChrTalk(
        0x104,
        (
            "#0306Fさすがに身分を明かさないで\x01",
            "聞いてみるのは難しそうだな。\x02\x03",

            "#0300Fま、余計な横槍が入る前に\x01",
            "動いちまえばいいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        (
            "#12P#0103F……………………………………\x02\x03",

            "#0100F……ひょっとしたら\x01",
            "内密に調べさせてもらえるかも。\x02",
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
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x103,
        "#0205Fどういう事ですか……？\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x102,
        (
            "#12P#0104F……私の友人に\x01",
            "ＩＢＣの関係者がいるのよ。\x02\x03",

            "#0100Fその人のお父様に事情を話せば\x01",
            "力になってくれるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        "#5P#0000Fそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x104,
        (
            "#0309F#5Pおお、好都合じゃねえか。\x02\x03",

            "#0300Fさすがお嬢。\x01",
            "色々なコネを持ってるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x102,
        (
            "#12P#0104Fまあ、それなりにね。\x02\x03",

            "#0108Fでも、とても忙しい方だから\x01",
            "クロスベル市にいるかどうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x103,
        "#0200Fどんな立場の方なんですか？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x102,
        (
            "#12P#0103F……多分、知ってると思うけど。\x02\x03",

            "#0100Fディーター・クロイスっていうの。\x02",
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
        "#5P#0005Fえ！？\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x103,
        "#0205Fあ……\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x104,
        "#0305F#5Pなんだ、有名人なのか？\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        (
            "#5P#0000Fあ、うん……\x02\x03",

            "#0003Fある意味、知名度で言うなら\x01",
            "イリアさん並みかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x103,
        (
            "#0204Fディーター・クロイス……\x02\x03",

            "大陸有数の資産家にして\x01",
            "国際経済の中心人物の一人……\x02\x03",

            "#0202F現ＩＢＣ総裁ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x104,
        "#0307F#5Pおお、銀行のトップかよ！？\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        (
            "#12P#0104F元々、父の旧い友人だったの。\x02\x03",

            "祖父とも昔から親交があって\x01",
            "それで仲良くさせてもらっていて……\x02\x03",

            "#0102F娘さんは、私の幼なじみにあたるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        (
            "#5P#0002Fそうだったのか……\x02\x03",

            "#0006Fしかしそんな人だと……\x01",
            "不在だとしても仕方ないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x102,
        (
            "#12P#0106Fうん……一年の半分くらいは\x01",
            "外国を飛び回っているらしいから。\x02\x03",

            "#0101Fでも、駄目で元々だわ。\x02\x03",

            "私の友人ならいるかもしれないし、\x01",
            "訪ねるだけ訪ねてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ、そうしよう。\x02\x03",

            "#0003Fしかし、これで何とか\x01",
            "捜査の目処がついたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x103,
        (
            "#0206F……メールの意図ですね。\x02\x03",

            "#0201F脅迫状もそうでしたが\x01",
            "どういうつもりなんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x104,
        (
            "#0302F#5Pま、せっかく向こうから\x01",
            "わざわざ接触してきたんだ。\x02\x03",

            "ここは敢えて乗ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x102,
        (
            "#12P#0104Fそうね……\x02\x03",

            "#0100F行きましょう、ＩＢＣビルへ。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14235")
    OP_29(0xF, 0x4, 0x40)
    Jump("loc_14247")

    label("loc_14235")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14247")
    OP_29(0xF, 0x4, 0x40)

    label("loc_14247")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7100", 0)
    EventEnd(0x5)
    Return()

    # Function_34_11B3E end

    def Function_35_1425B(): pass

    label("Function_35_1425B")

    Sleep(500)
    OP_93(0x102, 0x0, 0x1F4)

    def lambda_1426A():
        OP_96(0xFE, 0x4010, 0x352, 0x1EDC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1426A)
    WaitChrThread(0x102, 1)
    Return()

    # Function_35_1425B end

    def Function_36_14284(): pass

    label("Function_36_14284")


    def lambda_14289():
        OP_95(0xFE, 10400, 850, 8600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14289)
    WaitChrThread(0x104, 1)

    def lambda_142A7():
        OP_95(0xFE, 14400, 850, 9900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_142A7)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_36_14284 end

    def Function_37_142C8(): pass

    label("Function_37_142C8")

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
            "#4P#0306Fいやはや……\x01",
            "スゲエ事件になったな。\x02\x03",

            "#0301F今ごろ、市民の大半が\x01",
            "大騒ぎしてるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x103,
        (
            "#12P#0206Fまあ、アルカンシェルの\x01",
            "新作のお披露目中に\x01",
            "市長の暗殺未遂ですから……\x02\x03",

            "#0211Fスキャンダル、ここに\x01",
            "極まれりといった感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#5P#0006F市長に同情的な意見が多いのは\x01",
            "不幸中の幸いだったけど……\x02\x03",

            "#0008Fでも、結局アーネストと関係していた\x01",
            "帝国派議員の名前は上がってないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x104,
        (
            "#4P#0303Fまあ、規制されてんだろ。\x02\x03",

            "#0301Fそれに流石に、あの暗殺未遂は\x01",
            "秘書野郎の暴走なんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x101,
        (
            "#5P#0003Fああ……多分ね。\x02\x03",

            "#0001F帝国派にとって\x01",
            "市長を暗殺するメリットなんて\x01",
            "それほど無いはずだし……\x02\x03",

            "#0008Fただ、暗殺者を《銀#2Rイン#》に仕立てて\x01",
            "《黒月》と関係のある共和国派への\x01",
            "攻撃材料にする可能性はあるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x104,
        "#4P#0305Fなるほどねぇ……\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x103,
        (
            "#12P#0208Fでもあの秘書の人……\x01",
            "何だか様子がおかしかったです。\x02\x03",

            "#0201F正気を失っているというか……\x01",
            "歯止めが利かなくなってるというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x101,
        (
            "#5P#0006Fああ……それは思った。\x02\x03",

            "#0001F一課が取調べをしてるらしいけど\x01",
            "結局、どうなったんだろう？\x02",
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
        "男の声",
        (
            "──どうやら錯乱しちまって\x01",
            "話せる状態じゃないらしいな。\x02",
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
        "#0005F課長……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_148D5():
        OP_95(0xFE, 16500, 850, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_148D5)
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

    def lambda_14957():
        OP_95(0xFE, 2500, 850, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14957)
    WaitChrThread(0x8, 1)

    def lambda_14975():
        OP_95(0xFE, 2500, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14975)
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
            "#11P#0301F取調べができる\x01",
            "精神状態じゃないってか？\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x8,
        (
            "#6P#1003Fああ、ラチが明かないんで\x01",
            "一旦拘置所送りにするそうだ。\x02\x03",

            "#1000F教会のカウンセラーか\x01",
            "ウルスラ病院の助けを\x01",
            "借りるつもりらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x101,
        "#5P#0006Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x8,
        (
            "#6P#1002Fクク、しかしお前らも\x01",
            "とんだ大金星じゃねえか？\x02\x03",

            "今日本部に行ったら\x01",
            "あのキツネが猫撫で声を出して\x01",
            "お前らのことを誉めてきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        "#5P#0011Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x103,
        "#12P#0211F想像しにくい光景ですね……\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x104,
        (
            "#11P#0306Fつうか嬉しくも\x01",
            "何ともない情報だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x8,
        (
            "#6P#1003Fキツネだけじゃなくて\x01",
            "警察全体の話でもあるがな。\x02\x03",

            "#1002Fま、一課は複雑だろうが\x01",
            "これでお前らを見る目が\x01",
            "少し変わるのは確かだろう。\x02\x03",

            "素直に喜べよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x101,
        "#5P#0000Fそう……ですね。\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x103,
        (
            "#12P#0208Fでも……\x01",
            "素直には喜べませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x104,
        (
            "#11P#0303Fああ……\x01",
            "お嬢の事を考えるとなぁ。\x02",
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

    # Function_37_142C8 end

    def Function_38_14D19(): pass

    label("Function_38_14D19")

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

    def lambda_14E15():

        label("loc_14E15")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_14E15")

    QueueWorkItem2(0xC, 1, lambda_14E15)
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
            "──１週間が経った。\x02\x03",

            "キーアを保護したロイドたちは\x01",
            "彼女を特務支援課のビルに匿#2Rかくま#いながら\x01",
            "マフィアからの報復を警戒することにした。\x02\x03",

            "警察本部に加え、ヨナの情報網などにも\x01",
            "頼りながら、マフィアとハルトマン議長の\x01",
            "動向を注意深く伺う日々……\x02\x03",

            "一方、記憶が戻らないにも関わらず、\x01",
            "キーアは不安を見せることもなく、\x01",
            "あっという間に支援課に馴染んでいった。\x02\x03",

            "そして──\x07\x00\x02",
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

    def lambda_15065():
        OP_96(0xFE, 0x3E738, 0x0, 0x10A04, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15065)
    Sleep(300)

    def lambda_15082():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15082)
    WaitChrThread(0x103, 1)
    Sound(820, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    def lambda_150B4():
        OP_96(0xFE, 0x3E3B4, 0x0, 0x10A04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_150B4)
    WaitChrThread(0x103, 1)

    def lambda_150D2():
        OP_93(0xA, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_150D2)
    WaitChrThread(0xA, 2)

    def lambda_150E3():
        OP_93(0xA, 0x10F, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_150E3)
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
        "#0005F──手打ち、ですか？\x02",
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
            "#1003F#11Pああ、非公式だが警察本部宛てに\x01",
            "ルバーチェから打診があったそうだ。\x02\x03",

            "#1001F出品物にあの子が紛れ込んでいたのは\x01",
            "完全な手違い──というか、\x01",
            "全く身に覚えがないということだ。\x02\x03",

            "#1006F《黒月》の工作とも主張していたが\x01",
            "ま、状況的には厳しいかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#6P#0006F……そうですね。\x02\x03",

            "#0001F俺たちが駆けつけた時、\x01",
            "《銀#2Rイン#》は丁度、部屋にいた手下を\x01",
            "倒したばかりのタイミングでした。\x02\x03",

            "外からキーアを運んで中の人形と\x01",
            "入れ替える暇は無かったと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_15480")

    #C0686
    ChrTalk(
        0x104,
        (
            "#6P#0306Fって事は、あのトランクが\x01",
            "屋敷に運びこまれた時には\x01",
            "既に入れ替わっていたって事か。\x02\x03",

            "#0301Fそもそも、出品される筈だった\x01",
            "人形の出所はどこだったんスか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15522")

    label("loc_15480")


    #C0687
    ChrTalk(
        0x104,
        (
            "#6P#0306Fって事は、例のトランクが\x01",
            "屋敷に運びこまれた時には\x01",
            "既に入れ替わっていたって事か。\x02\x03",

            "#0301Fそもそも、出品される筈だった\x01",
            "人形の出所はどこだったんスか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15522")


    #C0688
    ChrTalk(
        0x8,
        (
            "#1003F#11Pはっきりした事は判らんが\x01",
            "レミフェリア方面の裏ルートから\x01",
            "手に入れたものだったらしい。\x02\x03",

            "#1001F記念祭最終日──\x01",
            "つまりオークション当日、\x01",
            "屋敷に運び込まれたらしいが……\x02\x03",

            "その運び込んだ運送会社も\x01",
            "架空のものだったと主張している。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x101,
        (
            "#6P#0011Fそんな馬鹿な……\x02\x03",

            "#0010Fつまり連中は、あくまで自分たちは\x01",
            "嵌められた側だと主張してるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x8,
        (
            "#1003F#11Pまあ、そういう事だな。\x02\x03",

            "真偽のほどは分からんが……\x01",
            "連中が必死に弁解するのも判る。\x02\x03",

            "#1001F──下手をしたら『人身売買』の\x01",
            "容疑が掛けられちまう訳だからな。\x02",
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
            "#6P#0303F武器の密輸、マネーロンダリング、\x01",
            "盗品すら扱う闇のオークション……\x02\x03",

            "#0301Fそんな犯罪を平気でやる連中も\x01",
            "人身売買の疑いが掛かるのだけは\x01",
            "何としても避けたいってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x8,
        (
            "#1001F#11P当然といえば当然だ。\x02\x03",

            "#1003F犯罪としてはおよそ最悪の部類……\x01",
            "絶対に許されないたぐいの重罪だ。\x02\x03",

            "警察もさすがに黙っちゃいないし、\x01",
            "何よりも遊撃士協会が聞きつけたら\x01",
            "総力を挙げて叩き潰しに来るだろう。\x02\x03",

            "#1000F《支える籠手》の紋章に懸けてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        (
            "#6P#0006Fそんなリスクを、議長はもちろん、\x01",
            "ルバーチェも負うハズがない……\x02\x03",

            "#0001F──理屈としては判るんですが\x01",
            "正直、とても納得は出来ませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x8,
        (
            "#1003F#11Pああ、だからこその手打ちだ。\x02\x03",

            "#1000Fお前たちの潜入捜査──\x01",
            "向こうは不法侵入と言ってるが\x01",
            "──についても一切不問にする。\x02\x03",

            "“偶然”保護した少女の扱いも\x01",
            "こちらに全てを任せるそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x104,
        (
            "#6P#0306Fその代わり、この件については\x01",
            "自分たちの主張を認めろ……\x02\x03",

            "間違っても遊撃士協会あたりに\x01",
            "チクったりするなってか？\x02\x03",

            "#0300Fやれやれ、確かに必死かもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x101,
        (
            "#6P#0008F……………………………………\x02\x03",

            "#0006F……キーアのことを考えると\x01",
            "曖昧にはしたくはないですけど……\x02\x03",

            "#0000Fあの子がこれ以上、マフィアに\x01",
            "狙われない事が確約されただけでも\x01",
            "納得すべきかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x8,
        (
            "#1002F#11Pああ、俺もそう思う。\x02\x03",

            "#1003F……まあ問題なのは、\x01",
            "肝心のあの子の素性なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        "#6P#0006Fええ……\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x104,
        (
            "#6P#0306F名前以外にはマジで何も\x01",
            "覚えてねえみてぇだからなァ。\x02\x03",

            "#0302F──しかしまあ、\x01",
            "とんでもなく明るいというか\x01",
            "人懐っこいガキンチョだよな。\x02\x03",

            "何かあっという間に\x01",
            "俺たち全員に懐いちまったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        (
            "#6P#0014Fはは……確かに。\x02\x03",

            "#0002Fツァイトはもちろん、\x01",
            "課長も懐かれましたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x8,
        (
            "#1004F#11Pまあ、な。\x02\x03",

            "#1002F俺は煙草を吸うから、あんまり\x01",
            "子供には近寄られねぇんだが……\x02\x03",

            "全然気にしてなさそうだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        (
            "#6P#0302Fお嬢やティオすけなんかも\x01",
            "もう夢中って感じみたいだし……\x02\x03",

            "今日なんか、デパートから\x01",
            "服を山ほど買って来てたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x101,
        (
            "#6P#0004Fはは、こういう時は\x01",
            "女性陣がいてくれて助かるよ。\x02\x03",

            "俺たちじゃどうしても\x01",
            "行き届かない所もあるし……\x02\x03",

            "#0008Fそれにしても……\x01",
            "本当に、どこの子なんだろう。\x02",
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

    def lambda_15F5A():
        OP_96(0xFE, 0xF104, 0x0, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15F5A)

    def lambda_15F74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15F74)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_6F(0x1)

    #C0705
    ChrTalk(
        0xA,
        (
            "#12P#1110Fあ、いた！\x02\x03",

            "#1109Fロイド、見て見て～！\x02",
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

    def lambda_16019():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16019)

    def lambda_16026():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_16026)

    def lambda_16033():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_16033)
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

    def lambda_1608D():
        OP_95(0xFE, 62600, 0, 5800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1608D)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)

    def lambda_160B3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_160B3)
    Sound(819, 0, 100, 0)
    OP_6F(0x79)

    #C0706
    ChrTalk(
        0x101,
        (
            "#0011F#5Pわわっ……\x01",
            "ちょっと、キーア！？\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0xA,
        (
            "#12P#1109Fエリィとティオに\x01",
            "服を選んでもらったの！\x02\x03",

            "どれもカワイかったけど\x01",
            "コレが一番気に入っちゃった！\x02\x03",

            "#1110Fねえねえ、にあう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        (
            "#0012F#5Pいや、抱きつかれたままだと\x01",
            "どんな服か判らないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xA,
        "#12P#1105Fあ、そーか。\x02",
    )

    CloseMessageWindow()
    OP_68(62700, 1200, 4900, 1000)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)

    def lambda_16207():
        OP_96(0xFE, 0xF4EC, 0x0, 0x1324, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16207)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    def lambda_16227():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16227)
    WaitChrThread(0xA, 2)

    def lambda_16238():
        OP_93(0xA, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16238)
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
        "キーア",
        "#1Pねえねえ、にあうー！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 120, -1, -1)

    #A0711
    AnonymousTalk(
        0x101,
        "#0002Fへえ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 70, -1, -1)

    #A0712
    AnonymousTalk(
        0x104,
        "#0305Fほほう……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 20, -1, -1)

    #A0713
    AnonymousTalk(
        0x8,
        "#1002Fふむ……\x02",
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
        "#12P#1110Fどう！？\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x101,
        (
            "#0004F#5Pああ……可愛いよ。\x02\x03",

            "#0002F凄くキーアに似合ってるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xA,
        (
            "#12P#1109Fほんとー！？\x02\x03",

            "#1102Fねえねえ、ランディと\x01",
            "かちょーもかわいいと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x104,
        "#5P#0309Fおー、かわいいかわいい。\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x8,
        "#5P#1002Fうむ、悪くないな。\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xA,
        "#12P#1109Fえへへ……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x102, 59000, 0, 3400, 90)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x103, 59000, 0, 3400, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_164B8():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_164B8)

    def lambda_164D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_164D2)
    Sleep(700)

    def lambda_164E6():
        OP_95(0xFE, 60000, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_164E6)

    def lambda_16500():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_16500)
    WaitChrThread(0x102, 1)

    def lambda_16515():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_16515)
    WaitChrThread(0x103, 1)

    def lambda_16526():
        OP_95(0xFE, 61000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16526)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x1F4)

    #C0720
    ChrTalk(
        0x102,
        (
            "#12P#0102Fふふっ、さっそく\x01",
            "お披露目してるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x103,
        (
            "#6P#0206F……まだ色々と\x01",
            "着て欲しかったんですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)

    #C0722
    ChrTalk(
        0xA,
        (
            "#1110Fエリィ、ティオ！\x01",
            "ロイドたちがかわいいって！\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x102,
        "#12P#0109Fふふ、良かったわね。\x02",
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x103,
        (
            "#6P#0202Fまあ、ロイドさんなら\x01",
            "キーアがどんな服を着てても\x01",
            "可愛いと言いそうですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0725
    ChrTalk(
        0x101,
        (
            "#0012F#5Pそんな事は……\x01",
            "まあ、あるかもしれないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x104,
        (
            "#5P#0309Fハハ、親バカ丸出しだな。\x02\x03",

            "#0300Fうーん、しかしキー坊が来て\x01",
            "まだ１週間しか経ってねぇのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x102,
        (
            "#12P#0104Fふふ……\x01",
            "何だか信じられないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0728
    ChrTalk(
        0x102,
        (
            "#12P#0105Fそういえば……\x02\x03",

            "#0101F警察本部からの連絡は\x01",
            "結局どうだったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x103,
        (
            "#6P#0200F何でもルバーチェの方から\x01",
            "打診があったとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x8,
        "#5P#1003Fああ、それなんだが……\x02",
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x101,
        (
            "#0006F#5P……ランチの時にでも\x01",
            "おいおい説明させてもらうよ。\x02",
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
            "#0104Fなるほど……\x02\x03",

            "#0100F一応、マフィアの心配は\x01",
            "無くなったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x103,
        (
            "#6P#0208Fただ、根本的な問題は\x01",
            "残ったままですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x8,
        (
            "#5P#1006Fああ、完全にこっちに\x01",
            "丸投げされた形になったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        (
            "#0003F#11Pとにかく肝心なのは\x01",
            "記憶と素性についてだけど……\x02\x03",

            "#0001F──なあキーア。\x01",
            "やっぱり何も思い出せないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xA,
        (
            "#6P#1100Fんー……ゼンゼン。\x02\x03",

            "#1109Fロイドが口をぽかんとあけて\x01",
            "目をまんまるにしてたのなら\x01",
            "おぼえてるけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x101,
        (
            "#0006F#11Pガクッ……\x02\x03",

            "#0011Fそれは一週間前、\x01",
            "初めて会った時の話だろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xA,
        (
            "#6P#1108Fだってその前のことは\x01",
            "なんにも覚えてないんだモン。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        "#0000F#11P……そっか。\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x104,
        (
            "#0304F#11Pま、覚えてないってんなら\x01",
            "仕方ねぇやな。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x103,
        (
            "#6P#0200F#6P……各方面への問い合わせは\x01",
            "どうなっているんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x8,
        (
            "#5P#1000Fああ……それなんだが。\x02\x03",

            "駅や空港、門にも問い合わせたが\x01",
            "今のところ該当者はナシのようだ。\x02\x03",

            "#1003F少々、難航するかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x101,
        "#0008F#11P……そうですか……\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "#6P#1105F？？？\x02\x03",

            "#1101Fどうしたのロイド？\x01",
            "おなかでも痛い？\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        "#0012F#11Pはは、大丈夫だよ。\x02",
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
            "#0003F#11P──課長。\x01",
            "今日の午後からなんですけど……\x02\x03",

            "#0001Fキーアを連れて\x01",
            "外に出ても構わないでしょうか？\x02",
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
        "#5P#1001Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x102,
        "#0101F何か心当たりがあるの？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0749
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ……\x02\x03",

            "#0000F一度、遊撃士協会を\x01",
            "頼ってみようかと思ってさ。\x02",
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
        "#0105Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x103,
        "#6P#0205F本気ですか……？\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0xA,
        "#6P#1111Fゆーげきし？\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x8,
        (
            "#5P#1004F……なるほどな。\x02\x03",

            "#1002F連中は大陸各地に\x01",
            "ギルドの支部を持っている……\x02\x03",

            "その情報網をアテにしてみるか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    #C0754
    ChrTalk(
        0x101,
        (
            "#0006F#11Pええ、頼れるものは\x01",
            "この際頼っておくべきかと。\x02\x03",

            "#0001F……駄目でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x8,
        (
            "#5P#1002Fま、いいんじゃねえか？\x02\x03",

            "#1004F警察とギルドは\x01",
            "別に対立してるわけじゃねえ。\x02\x03",

            "わだかまりがあるとしたら\x01",
            "むしろ警察#4Rコチラ#の方だからな。\x02\x03",

            "#1002F案件が案件だし、協力を要請すれば\x01",
            "向こうも断ったりはしねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x101,
        "#0004F#11Pええ、そう思います。\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x104,
        (
            "#0300F#11Pま、エステルちゃんたちとは\x01",
            "この前、結構打ち解けられたしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x102,
        (
            "#0104F確かに相談するには\x01",
            "丁度いい機会かもしれないわね。\x02\x03",

            "#0101Fでもロイド……\x01",
            "キーアちゃんを連れていくって\x01",
            "あなた一人で連れて行くつもり？\x02",
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
            "#0005F#11Pそのつもりだけど……\x02\x03",

            "#0000F全員で行くほどの事じゃないし\x01",
            "俺一人で十分かと思うんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x102,
        (
            "#0103F……納得行かないわね。\x02\x03",

            "#0111Fただでさえ一番懐かれてるのに\x01",
            "更に独り占めしようだなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        "#0011F#11Pへ……\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x103,
        (
            "#6P#0206Fロイドさんはズルいです。\x02\x03",

            "#0211Fこの子と接する機会は\x01",
            "均等であるべきではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0xA,
        "#6P#1100Fふえ～？\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x101,
        "#0011F#11Pえっと、何の話だ？\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#0309F#11Pハハ、オマエ恨まれてんだよ。\x02\x03",

            "何しろここ数日、寝る時は\x01",
            "いつもキー坊と一緒みたいだし。\x02",
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
            "#0006F#5Pいや、それはキーアが勝手に\x01",
            "ベッドに入ってくるからで……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0767
    ChrTalk(
        0x101,
        (
            "#0001F#11P──なあ、キーア。\x01",
            "ちゃんと部屋を用意したんだから\x01",
            "一人で寝ないとダメだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xA,
        (
            "#6P#1106Fだってロイドといっしょだと\x01",
            "なんか落ち着くんだモン。\x02\x03",

            "#1112Fめーわくだったら\x01",
            "あきらめるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x101,
        (
            "#0011F#11Pい、いや……\x01",
            "迷惑ってことはないけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x102,
        (
            "#0101Fちょっとロイド……\x01",
            "何を冷たくしているのよ。\x02\x03",

            "あんな事があったばかりなんだから\x01",
            "まだ不安かもしれないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x103,
        (
            "#6P#0211F一緒に寝てあげるくらいの\x01",
            "甲斐性は欲しいところですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0772
    ChrTalk(
        0x101,
        "#0012F#11P俺にどーしろと！？\x02",
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x8,
        (
            "#5P#1002Fクク……\x01",
            "ま、当分は一緒にいてやれや。\x02\x03",

            "#1003Fそれから外出だが……\x01",
            "念のため、もう一人連れて行け。\x02\x03",

            "#1000Fルバーチェからの打診はあったが\x01",
            "一応、用心した方がいいだろ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0774
    ChrTalk(
        0x101,
        (
            "#0005F#11Pあ……\x02\x03",

            "#0000F──分かりました。\x01",
            "気をつけておきます。\x02",
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
            "#1K誰を同行者に選びますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【エリィに同行してもらう】\x01",        # 0
            "【ティオに同行してもらう】\x01",        # 1
            "【ランディに同行してもらう】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17BF1"),
        (1, "loc_17C12"),
        (2, "loc_17C33"),
        (SWITCH_DEFAULT, "loc_17C54"),
    )


    label("loc_17BF1")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Call(0, 41)
    Jump("loc_17C54")

    label("loc_17C12")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 5)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    Call(0, 42)
    Jump("loc_17C54")

    label("loc_17C33")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 6)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Call(0, 43)
    Jump("loc_17C54")

    label("loc_17C54")

    Return()

    # Function_38_14D19 end

    def Function_39_17C55(): pass

    label("Function_39_17C55")


    def lambda_17C5A():
        OP_96(0xFE, 0x3E98F, 0x0, 0x107AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17C5A)
    Sleep(300)

    def lambda_17C77():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_17C77)
    WaitChrThread(0x102, 1)
    Sound(820, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    def lambda_17CA9():
        OP_96(0xFE, 0x3E98F, 0x0, 0x10428, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17CA9)
    WaitChrThread(0x102, 1)

    def lambda_17CC7():
        OP_93(0xA, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_17CC7)
    WaitChrThread(0xA, 2)

    def lambda_17CD8():
        OP_93(0xA, 0xB5, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_17CD8)
    WaitChrThread(0xA, 2)
    OP_63(0xA, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    Return()

    # Function_39_17C55 end

    def Function_40_17D00(): pass

    label("Function_40_17D00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17D1E")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_40_17D00")

    label("loc_17D1E")

    Return()

    # Function_40_17D00 end

    def Function_41_17D1F(): pass

    label("Function_41_17D1F")

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
            "#6P#0000Fさてと……\x01",
            "それじゃあ出かけようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x102,
        (
            "#0104F#11P東通りにある遊撃士協会ね。\x02\x03",

            "#0100Fあまり寄り道は\x01",
            "しない方がいいのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや、キーアの記憶が戻る\x01",
            "きっかけになるかもしれない。\x02\x03",

            "#0000F用心は必要だけど……\x01",
            "ギルドに行った帰りくらいなら\x01",
            "寄り道もいいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x102,
        "#0102F#11Pなるほど、それもそうね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)

    def lambda_17F0D():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17F0D)
    Sleep(300)

    #C0780
    ChrTalk(
        0x102,
        (
            "#0109Fふふっ、キーアちゃん。\x01",
            "それじゃあ行きましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x153,
        (
            "#1109F#5Pうんっ！\x02\x03",

            "#1105Fって、どこに行くのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#0103Fうーん。\x01",
            "遊撃士協会って所だけど……\x02\x03",

            "#0100Fひょっとして判らないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x153,
        (
            "#1103F#5Pゆーげきし……\x02\x03",

            "#1100F……それってもしかして\x01",
            "正義のミカタみたいな人たち？\x02",
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
            "#12P#0005Fなんだ、知ってるのか？\x02\x03",

            "#0000Fそのくらいの一般常識は\x01",
            "覚えてるってことなのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x102,
        "#0100Fええ、そうみたいね。\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x153,
        (
            "#1100F#5Pえへへ……\x01",
            "なんで行くか知らないけど。\x02\x03",

            "#1109Fロイドとエリィがいっしょなら\x01",
            "キーア、別にどこでもいいよ！\x02",
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
        "#12P#0011Fうっ……\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0788
    ChrTalk(
        0x102,
        (
            "#0109F………ああもうっ………！\x01",
            "なんでこんなに可愛いの……！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0789
    ChrTalk(
        0x153,
        "#1109F#5P#4Sそれじゃあ、れっつごー！\x02",
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

    # Function_41_17D1F end

    def Function_42_18275(): pass

    label("Function_42_18275")

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
            "#6P#0000Fさてと……\x01",
            "それじゃあ出かけようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x103,
        (
            "#0204F#11P東通りの遊撃士協会ですね。\x02\x03",

            "#0201F……やはり寄り道は\x01",
            "しない方がいいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや、キーアの記憶が戻る\x01",
            "きっかけになるかもしれない。\x02\x03",

            "#0000F用心は必要だけど……\x01",
            "ギルドに行った帰りくらいなら\x01",
            "寄り道もいいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x103,
        "#0204F#11Pなるほど、道理ですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x153, 500)

    def lambda_18467():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18467)
    Sleep(300)

    #C0794
    ChrTalk(
        0x103,
        (
            "#0202F……それではキーア。\x01",
            "そろそろ出発しましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x153,
        (
            "#1109F#5Pうんっ！\x02\x03",

            "#1105Fって、どこに行くのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x103,
        (
            "#0205F遊撃士協会という所ですが……\x02\x03",

            "#0206Fキーアにはちょっと\x01",
            "判らないかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x153,
        (
            "#1103F#5Pゆーげきし……\x02\x03",

            "#1100F……それってもしかして\x01",
            "正義のミカタみたいな人たち？\x02",
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
            "#12P#0005Fなんだ、知ってるのか？\x02\x03",

            "#0000Fそのくらいの一般常識は\x01",
            "覚えてるってことなのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x103,
        (
            "#0202Fそうですね……\x02\x03",

            "#0204Fいわゆる長期記憶に\x01",
            "相当するのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x153,
        (
            "#1100F#5Pえへへ……\x01",
            "なんで行くか知らないけど。\x02\x03",

            "#1109Fロイドとティオがいっしょなら\x01",
            "キーア、別にどこでもいいよ！\x02",
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
        "#12P#0011Fうっ……\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0802
    ChrTalk(
        0x103,
        (
            "#0209F……この笑顔は\x01",
            "ちょっと反則すぎますね……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0803
    ChrTalk(
        0x153,
        "#1109F#5P#4Sそれじゃあ、れっつごー！\x02",
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

    # Function_42_18275 end

    def Function_43_187F8(): pass

    label("Function_43_187F8")

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
            "#6P#0000Fさてと……\x01",
            "それじゃあ出かけようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x104,
        (
            "#0304F#11P東通りの遊撃士協会だな。\x02\x03",

            "#0301Fどうする？\x01",
            "やっぱ寄り道は止めとくか？\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや、キーアの記憶が戻る\x01",
            "きっかけになるかもしれない。\x02\x03",

            "#0000F用心は必要だけど……\x01",
            "ギルドに行った帰りくらいなら\x01",
            "寄り道もいいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x104,
        (
            "#0300F#11Pなるほど。\x02\x03",

            "#0309Fま、俺とお前がいりゃあ\x01",
            "何があっても大丈夫だろ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x153, 500)

    def lambda_18A0B():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18A0B)
    Sleep(300)

    #C0808
    ChrTalk(
        0x104,
        (
            "#0302Fよーし、キー坊。\x01",
            "お出かけするとしますか！\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x153,
        (
            "#1109F#5Pうんっ！\x02\x03",

            "#1105Fって、どこに行くのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x104,
        (
            "#0305F遊撃士協会ってとこだが……\x02\x03",

            "#0302Fお前さんにはちょいと\x01",
            "判らないかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x153,
        (
            "#1103F#5Pゆーげきし……\x02\x03",

            "#1100F……それってもしかして\x01",
            "正義のミカタみたいな人たち？\x02",
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
            "#12P#0005Fなんだ、知ってるのか？\x02\x03",

            "#0000Fそのくらいの一般常識は\x01",
            "覚えてるってことなのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x104,
        "#0300Fああ、みたいだな。\x02",
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x153,
        (
            "#1100F#5Pえへへ……\x01",
            "なんで行くか知らないけど。\x02\x03",

            "#1109Fロイドとランディがいっしょなら\x01",
            "キーア、別にどこでもいいよ！\x02",
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
        "#12P#0011Fうっ……\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0816
    ChrTalk(
        0x104,
        (
            "#0306F……子煩悩な父親の気持ちが\x01",
            "ちょっと判る気がしてきたぜ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0817
    ChrTalk(
        0x153,
        "#1109F#5P#4Sそれじゃあ、れっつごー！\x02",
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

    # Function_43_187F8 end

    def Function_44_18D75(): pass

    label("Function_44_18D75")

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

    def lambda_18FCB():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18FCB)

    def lambda_18FE5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18FE5)
    Sleep(250)

    def lambda_18FF9():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18FF9)

    def lambda_19013():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19013)
    Sleep(400)

    def lambda_19027():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19027)

    def lambda_19041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_19041)
    Sleep(250)

    def lambda_19055():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19055)

    def lambda_1906F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1906F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0818
    ChrTalk(
        0x101,
        "#0000F#12Pただいま～。\x02",
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x104,
        "#0309F#12P帰ったぜ～。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    #Sound(2036, 255, 90, 0)    #voice#KeA

    #C0820
    ChrTalk(
        0xA,
        "#4P#1110Fあ、かえってきた！\x02",
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

    def lambda_19135():

        label("loc_19135")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_19135")

    QueueWorkItem2(0x102, 2, lambda_19135)

    def lambda_19147():

        label("loc_19147")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_19147")

    QueueWorkItem2(0x104, 2, lambda_19147)
    Sleep(1000)
    Sound(2037, 255, 100, 0)    #voice#KeA
    WaitChrThread(0xA, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)

    #C0821
    ChrTalk(
        0x101,
        (
            "#12P#0014Fはは、いいタックルだ。\x02\x03",

            "#0002Fおかえりキーア。\x01",
            "いい子にしてたか？\x02",
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
            "#5Pうんー！\x02\x03",

            "ツァイトといっしょに\x01",
            "ちゃんとお留守番してたよ。\x02\x03",

            "としょかんの本も\x01",
            "３さつ読んじゃった。\x02",
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
        "#12P#0005Fへえ、そりゃ凄いな。\x02",
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x102,
        (
            "#0102F#11Pふふ、子供向けの本とはいえ\x01",
            "午前中に３冊も読んじゃうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x103,
        (
            "#0204F#12Pやはりこの子は\x01",
            "かなりの情報処理能力を\x01",
            "持っているのではないかと……\x02\x03",

            "#0202F将来がすごく楽しみです。\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x104,
        (
            "#0306F#11Pまったく、\x01",
            "揃いも揃って親バカ連中だな。\x02\x03",

            "#0302Fって、俺も人のことは言えねぇが。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)

    def lambda_193D4():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_193D4)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x40)

    #C0827
    ChrTalk(
        0xA,
        (
            "#1105F#5Pふえー？\x02\x03",

            "#1110Fそれよりキーア、\x01",
            "お腹がすいちゃった。\x02\x03",

            "#1109F昼ゴハンにしようー！\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x101,
        "#12P#0002Fはは、そうだな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0829
    ChrTalk(
        0x101,
        (
            "#6P#0000F今日の当番は俺だけど、\x01",
            "みんな、パスタでいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x102,
        "#0102F#11Pうん、いいわね。\x02",
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x103,
        (
            "#12P#0204Fロイドさんの料理でしたら\x01",
            "わたしは何でも。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x104,
        "#0309F#11P俺のは大盛りにしてくれや。\x02",
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x101,
        "#6P#0002Fはは、了解。\x02",
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0xA,
        (
            "#1105F#5Pロイドがゴハン作るの？\x02\x03",

            "#1109Fそれじゃあキーアも手伝うー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_195F3():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_195F3)
    Sleep(300)

    #C0835
    ChrTalk(
        0x102,
        (
            "#0105F#11Pキーアちゃん……\x01",
            "料理なんてしたことあるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x103,
        (
            "#12P#0200Fひょっとして\x01",
            "何か思い出したとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0xA,
        (
            "#1100F#5Pさっき読んだ本のなかに\x01",
            "コックさんが出てきたからー。\x02\x03",

            "つくってた料理が\x01",
            "すごくおいしそーだったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x104,
        "#0302F#11Pハハ、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃあ、せっかくだから\x01",
            "キーアに手伝ってもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0xA,
        "#1109F#5Pうんー、れっつごー！\x02",
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
            "#0003F#11Pさてと……\x01",
            "何のパスタにするかな？\x02\x03",

            "#0000Fアルモリカ産の\x01",
            "卵とベーコンがあるから\x01",
            "カルボナーラでもいいし……\x02\x03",

            "リベール産のアサリ缶もあるから\x01",
            "ボンゴレとかもアリだよな。\x02\x03",

            "#0005Fいや、ここはナスを使った\x01",
            "ミートソース和えといくか？\x02",
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
            "#1K何を作りますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【カルボナーラ】\x01",            # 0
            "【アサリのボンゴレ】\x01",        # 1
            "【ナスのミートソース】\x01",      # 2
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
        (0, "loc_19997"),
        (1, "loc_199FA"),
        (2, "loc_19A5B"),
        (SWITCH_DEFAULT, "loc_19ABE"),
    )


    label("loc_19997")


    #C0843
    ChrTalk(
        0x101,
        (
            "#0000F#11Pよし、せっかくだから\x01",
            "新鮮なうちに卵を使っちゃおう。\x02\x03",

            "さてと、それじゃあ──\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19ABE")

    label("loc_199FA")


    #C0844
    ChrTalk(
        0x101,
        (
            "#0000F#11Pよし、せっかくだから\x01",
            "あのアサリ缶を使っちゃおう。\x02\x03",

            "さてと、それじゃあ──\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19ABE")

    label("loc_19A5B")


    #C0845
    ChrTalk(
        0x101,
        (
            "#0000F#11Pよし、挽肉も残ってたし\x01",
            "手早くミートソースを作ろう。\x02\x03",

            "さてと、それじゃあ──\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19ABE")

    label("loc_19ABE")


    #C0846
    ChrTalk(
        0xA,
        (
            "#11P#1110Fねーねー、ロイド。\x02\x03",

            "キーア、何を手伝えばいーの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(300)

    #C0847
    ChrTalk(
        0x101,
        (
            "#0002F#5Pじゃあ、今から言う\x01",
            "材料を持ってきてくれるか？\x02\x03",

            "俺はパスタを\x01",
            "茹でる準備をしてるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0xA,
        "#11P#1109Fおっけー。\x02",
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
        "#12P#1100Fドキドキ、ワクワク……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0850
    ChrTalk(
        0xA,
        (
            "#6P#1101Fねーねー、ロイド。\x01",
            "まだできないのー！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19DA1")

    #C0851
    ChrTalk(
        0x101,
        (
            "#11P#0004Fもうちょっと。\x01",
            "パスタは茹で加減が肝心なんだ。\x02\x03",

            "#0000Fちょうどいい茹で加減で引き上げて\x01",
            "フライパンでカルボナーラソースを\x01",
            "たっぷり絡めてから胡椒を散らす……\x02\x03",

            "#0014Fそれで出来上がりってわけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F5C")

    label("loc_19DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19E84")

    #C0852
    ChrTalk(
        0x101,
        (
            "#11P#0004Fもうちょっと。\x01",
            "パスタは茹で加減が肝心なんだ。\x02\x03",

            "#0000Fちょうどいい茹で加減で引き上げて\x01",
            "フライパンでアサリとスープと合わせて\x01",
            "ニンニクとパセリを加えて味を調える……\x02\x03",

            "#0014Fそれで出来上がりってわけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F5C")

    label("loc_19E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_19F5C")

    #C0853
    ChrTalk(
        0x101,
        (
            "#11P#0004Fもうちょっと。\x01",
            "パスタは茹で加減が肝心なんだ。\x02\x03",

            "#0000Fちょうどいい茹で加減で引き上げて\x01",
            "フライパンでミートソースと和えて\x01",
            "揚げたナスを絡めて粉チーズを振る……\x02\x03",

            "#0014Fそれで出来上がりってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F5C")


    #C0854
    ChrTalk(
        0xA,
        (
            "#6P#1105Fへー……\x02\x03",

            "#1110Fじゃあ、ここからは\x01",
            "キーアがやってみたい！\x02",
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
            "#11P#0005Fえ、そうか？\x02\x03",

            "#0004F（上手くいかないと思うけど……\x01",
            "  まあ、フォローすればいいか。）\x02\x03",

            "#0000Fよし、それじゃあやってごらん。\x02\x03",

            "ただし、火には気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0xA,
        "#6P#1109Fうんー！\x02",
    )

    CloseMessageWindow()
    OP_68(124090, 1000, 8260, 1500)

    def lambda_1A092():
        OP_96(0xFE, 0x1E780, 0x1E, 0x206C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A092)
    Sleep(300)

    def lambda_1A0AF():
        OP_96(0xFE, 0x1E334, 0x1E, 0x206C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A0AF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(300)

    #C0857
    ChrTalk(
        0xA,
        (
            "#1101F#11P#30Wえっと……\x02\x03",

            "#30Wちょうどいい茹でかげんでひきあげて\x01",
            "フライパンで……\x02\x03",

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
            "#0006F#11P（やっぱり無理だよな……）\x02\x03",

            "#0000F（ま、キーアが作ったものなら\x01",
            "  多少失敗してもみんな喜んで──）\x02",
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
        "#11P#1103F#30W───ん、わかった。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0860
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアは手馴れた動作で\x01",
            "鍋から茹で立てのパスタを引き上げ\x01",
            "フライパンで調理していった。\x07\x00\x02",
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
        "#0011F#11Pへ……！？\x02",
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
        "#11P#1109F#4Sうんっ、できたー！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A3E3")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jump("loc_1A446")

    label("loc_1A3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A417")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Jump("loc_1A446")

    label("loc_1A417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A446")
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    label("loc_1A446")

    Sleep(1000)

    #A0863
    AnonymousTalk(
        0x101,
        (
            "#0005Fおおっ……\x01",
            "凄いじゃないかキーア！？\x02\x03",

            "すごく手際がよかったけど\x01",
            "どうやって分かったんだ！？\x02",
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
            "#1104Fえへへー。\x01",
            "なんかアタマにひらめいたの。\x02\x03",

            "#1110Fやり方、まちがってたー？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A541")
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jump("loc_1A5A4")

    label("loc_1A541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A575")
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Jump("loc_1A5A4")

    label("loc_1A575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A5A4")
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    label("loc_1A5A4")


    #C0865
    ChrTalk(
        0x101,
        (
            "#0004F#11Pいや、俺よりもむしろ\x01",
            "手際がいいくらいだったよ。\x02\x03",

            "#0000Fキーア……実は料理、\x01",
            "やった事があるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0xA,
        (
            "#6P#1111Fんー、そうなのかなぁ？\x02\x03",

            "#1109Fまあいいや、おなか空いたから\x01",
            "みんなで食べよー！\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AA64")
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
    Jump("loc_1AAAB")

    label("loc_1AA64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1AA8A")
    SetChrSubChip(0x19, 0xE)
    SetChrSubChip(0x1B, 0xE)
    SetChrSubChip(0x1D, 0xE)
    SetChrSubChip(0x1F, 0xE)
    SetChrSubChip(0x21, 0xE)
    SetChrSubChip(0x23, 0xE)
    Jump("loc_1AAAB")

    label("loc_1AA8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AAAB")
    SetChrSubChip(0x19, 0xA)
    SetChrSubChip(0x1B, 0xA)
    SetChrSubChip(0x1D, 0xA)
    SetChrSubChip(0x1F, 0xA)
    SetChrSubChip(0x21, 0xA)
    SetChrSubChip(0x23, 0xA)

    label("loc_1AAAB")

    Sleep(1000)
    OP_68(12600, 2350, 4800, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_68(12600, 1850, 4800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AC50")

    #C0867
    ChrTalk(
        0x104,
        (
            "#0305F#11Pおいおい、美味いじゃないか！\x02\x03",

            "これ、ホントにキー坊が\x01",
            "作っちまったのか！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0868
    ChrTalk(
        0x101,
        (
            "#5P#0004F下ごしらえまでは\x01",
            "俺がやったけど……\x02\x03",

            "#0002F茹でてからの調理は全部、\x01",
            "キーアがやってくれたんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0869
    ChrTalk(
        0x103,
        "#12P#0202F凄いです……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0870
    ChrTalk(
        0x102,
        (
            "#0109F#5Pええ……\x01",
            "お店で出せるほどの味だわ。\x02\x03",

            "#0102Fキーアちゃん、凄すぎる！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AED1")

    label("loc_1AC50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1AD8D")

    #C0871
    ChrTalk(
        0x102,
        (
            "#0105F#5Pお、美味しい……\x02\x03",

            "これ、本当にキーアちゃんが\x01",
            "作っちゃったの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x101,
        (
            "#11P#0004F下ごしらえまでは\x01",
            "俺がやったけど……\x02\x03",

            "#0000F茹でてからの調理は全部、\x01",
            "キーアがやってくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0873
    ChrTalk(
        0x104,
        "#0305F#11Pマジかよ……！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0874
    ChrTalk(
        0x103,
        (
            "#12P#0204Fお店で出せるレベルですね……\x02\x03",

            "#0202Fキーア、グッジョブです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AED1")

    label("loc_1AD8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AED1")
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0875
    ChrTalk(
        0x103,
        (
            "#12P#0205F……美味しい……\x02\x03",

            "これ、本当に\x01",
            "キーアが作ったのですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    #C0876
    ChrTalk(
        0x101,
        (
            "#5P#0000F下ごしらえまでは\x01",
            "俺がやったけど……\x02\x03",

            "茹でてからの調理は全部、\x01",
            "キーアがやってくれたんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0877
    ChrTalk(
        0x102,
        "#0102F#5Pす、凄い……\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x104,
        (
            "#0305F#11Pいや、マジで店に\x01",
            "出せそうなクオリティだぞ。\x02\x03",

            "#0309Fキー坊、スゲーじゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AED1")


    #C0879
    ChrTalk(
        0xA,
        (
            "#6P#1109Fえへへー。\x01",
            "美味しくできてよかったー。\x02",
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
            "#5P#0000Fひょっとして、\x01",
            "料理人の家の子なのかな？\x02\x03",

            "#0006F親御さんがいるなら今ごろ、\x01",
            "心配で仕方ないだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x102,
        (
            "#0103F#5P……そうね。\x01",
            "でも、仕方がないわ。\x02\x03",

            "#0108F遊撃士協会の情報網を頼っても\x01",
            "未だ情報がないくらいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x103,
        (
            "#6P#0208Fよほどの辺境出身か、\x01",
            "それとも何か事情があるのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0883
    ChrTalk(
        0xA,
        "#6P#1100Fんー？\x02",
    )

    CloseMessageWindow()

    #C0884
    ChrTalk(
        0x104,
        (
            "#0306F#11Pま、その辺のことは\x01",
            "考え出したらキリがねぇさ。\x02\x03",

            "#0300F手がかりが見つかるまで\x01",
            "ウチの子ってことでいいだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x101,
        (
            "#5P#0004Fそうだな……\x02\x03",

            "#0002F──はは、しかし課長も\x01",
            "留守ってのはツイてないよな。\x02\x03",

            "せっかくのキーアの手料理を\x01",
            "食べる機会を逃がしちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x103,
        (
            "#6P#0200F警察本部で会議ですか……\x01",
            "この所、何だか多いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0887
    ChrTalk(
        0x102,
        "#0105F#5Pそうね……何かあるのかしら？\x02",
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
        "#11P#0005F通信だ……誰からだろう？\x02",
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x104,
        (
            "#0300F#11Pエニグマに掛かって来ないって事は\x01",
            "課長やフランちゃんじゃなさそうだな。\x02",
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

    def lambda_1B325():
        OP_95(0xFE, 13800, 850, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B325)
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
            "#0000Fはい、こちらクロスベル警察、\x01",
            "特務支援課です。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("娘の声")

    #A0891
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、ロイドさん？\x02\x03",

            "えっと……ノエルです。\x01",
            "警備隊のシーカー曹長です。\x02",
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
            "#0009Fああ、久しぶり。\x01",
            "一月ぶりくらいかな。\x02\x03",

            "#0002Fどうしたんだい？\x01",
            "支援課の方に用件でも？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0893
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、実はその……\x02\x03",

            "個人的に、支援課の皆さんに\x01",
            "相談したい事がありまして……\x02",
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
            "#0005F個人的な相談……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0895
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、個人的といっても\x01",
            "仕事の範疇ではあるんですけど……\x02\x03",

            "その、すみません。\x01",
            "いきなりこんな連絡をして……\x02",
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
            "#0004Fいや、ちょうど昼時で\x01",
            "休憩してたから構わないよ。\x02\x03",

            "#0001F今、どこにいるんだ？\x01",
            "よかったら直接話そうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0897
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ほ、本当ですか？\x02\x03",

            "今ちょうど、クロスベル市の\x01",
            "北口にいるんです。\x02\x03",

            "これから伺ってもいいですか？\x02",
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
            "#0004Fああ、待ってるよ。\x02\x03",

            "#0005Fそうだ、よかったら\x01",
            "ランチでも食べていくかい？\x02\x03",

            "パスタでよかったら\x01",
            "簡単に用意しておくけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0899
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "い、いえ、そこまでは……\x02",
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
    SetChrName("ノエルの声")

    #A0900
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S……すみません……\x01",
            "よかったらお願いします……\x02",
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
            "#0002Fはは、了解。\x01",
            "それじゃあ急いで来てくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ノエルの声")

    #A0902
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい！\x07\x00\x02",
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

    def lambda_1B883():
        OP_95(0xFE, 14100, 850, 7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B883)
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
        "#0105F#6P誰からの連絡だったの？\x02",
    )

    CloseMessageWindow()

    #C0904
    ChrTalk(
        0x101,
        (
            "#11P#0000Fああ、ノエル曹長だった。\x02\x03",

            "何だか俺たちに\x01",
            "相談があるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0x104,
        (
            "#0305F#11Pへえ。\x01",
            "珍しい事もあるもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0xA,
        "#6P#1110Fなになに、だれか来るのー？\x02",
    )

    CloseMessageWindow()

    #C0907
    ChrTalk(
        0x103,
        "#12P#0204Fええ、警備隊のお姉さんです。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    #C0908
    ChrTalk(
        0xA,
        "#6P#1105Fけーびたい？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0909
    ChrTalk(
        0x101,
        (
            "#5P#0002Fランチがまだみたいだから\x01",
            "追加でパスタを茹でておこう。\x02\x03",

            "キーア、また手伝ってくれるか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0910
    ChrTalk(
        0xA,
        "#6P#1109Fうんっ！\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BC7D")
    SetChrSubChip(0x19, 0xD)
    SetChrSubChip(0x1B, 0xD)
    SetChrSubChip(0x1D, 0xD)
    SetChrSubChip(0x1F, 0xD)
    SetChrSubChip(0x21, 0xD)
    SetChrSubChip(0x23, 0xD)
    Jump("loc_1BCC4")

    label("loc_1BC7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1BCA3")
    SetChrSubChip(0x19, 0xF)
    SetChrSubChip(0x1B, 0xF)
    SetChrSubChip(0x1D, 0xF)
    SetChrSubChip(0x1F, 0xF)
    SetChrSubChip(0x21, 0xF)
    SetChrSubChip(0x23, 0xF)
    Jump("loc_1BCC4")

    label("loc_1BCA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BCC4")
    SetChrSubChip(0x19, 0xB)
    SetChrSubChip(0x1B, 0xB)
    SetChrSubChip(0x1D, 0xB)
    SetChrSubChip(0x1F, 0xB)
    SetChrSubChip(0x21, 0xB)
    SetChrSubChip(0x23, 0xB)

    label("loc_1BCC4")

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
        "#11P#0504Fごちそうさまでした。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0912
    ChrTalk(
        0x109,
        (
            "#5P#0502F──すごく美味しかった！\x01",
            "これ、本当にキーアちゃんが？\x02",
        )
    )

    CloseMessageWindow()

    #C0913
    ChrTalk(
        0xA,
        (
            "#6P#1100Fうん、そだよー。\x02\x03",

            "#1105Fしたごしらえ……だっけ。\x01",
            "それはロイドがしてくれたけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x109,
        (
            "#5P#0509Fいやいや、それでも十分すごいよ！\x02\x03",

            "#0504Fうーん、キーアちゃんの噂は\x01",
            "フランから散々聞いてたけど……\x02\x03",

            "#0502Fまさか可愛い上に\x01",
            "こんな特技まで持ってるなんて！\x02",
        )
    )

    CloseMessageWindow()

    #C0915
    ChrTalk(
        0x101,
        (
            "#0002F#11Pはは、フランはキーアのこと、\x01",
            "すごく気に入ったみたいだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x103,
        (
            "#6P#0204F#N端末で話す度に\x01",
            "キーアと話をさせて欲しいって\x01",
            "いつも頼んできてますよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0917
    ChrTalk(
        0x109,
        (
            "#5P#0509Fあはは、ウチの妹、\x01",
            "可愛い子には目がないんで……\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0xA,
        (
            "#6P#1110Fねえねえ、ノエルって\x01",
            "フランのおねえさんなのー？\x02\x03",

            "そういえばカミの色がおんなじだし\x01",
            "カオもそっくりだねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x109,
        (
            "#5P#0505Fそ、そうかな？\x02\x03",

            "#0502Fあたしはあの子みたいに\x01",
            "可愛いタイプじゃないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0920
    ChrTalk(
        0x109,
        (
            "#5P#0503Fあっと……\x01",
            "危うく本題を忘れる所でした。\x02\x03",

            "#0501F──その、さっそく話を\x01",
            "させてもらってもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0921
    ChrTalk(
        0x101,
        "#0001F#11Pああ、構わないよ。\x02",
    )

    CloseMessageWindow()

    #C0922
    ChrTalk(
        0x104,
        (
            "#0301F確か、山道の外れにある\x01",
            "遺跡についての話だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0923
    ChrTalk(
        0x109,
        "#5P#0508Fええ、それが……\x02",
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
        "#0005F──幽霊が出る遺跡、だって？\x02",
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
            "#5P#0503F……そうなんです。\x02\x03",

            "正確に言うと、幽霊というか\x01",
            "言い伝えの化物というか……\x02\x03",

            "#0501Fとにかく、見たこともないような\x01",
            "不思議な魔獣が出没していて……\x02",
        )
    )

    CloseMessageWindow()

    #C0926
    ChrTalk(
        0x104,
        (
            "#0303F当初、調査に当たっていた\x01",
            "ベルガード門の部隊は撤収……\x02\x03",

            "#0301Fタングラム門のお前さんたちに\x01",
            "お鉢が回ってきたってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0927
    ChrTalk(
        0x109,
        (
            "#5P#0501Fええ……\x02\x03",

            "#0506Fそれで昨日、何人かの隊員と\x01",
            "調査に入ってみたんですけど……\x02\x03",

            "気味の悪い魔獣ばかり現れて\x01",
            "みんな腰が引けてしまって……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0928
    ChrTalk(
        0x102,
        (
            "#0105F#6Pちょ、ちょっと待って。\x02\x03",

            "#0109F……もしかして……\x01",
            "幽霊退治の手伝いを私たちに？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0929
    ChrTalk(
        0x109,
        (
            "#11P#0505Fい、いえ……\x01",
            "あくまで遺跡内部の調査が\x01",
            "目的なんですけど……\x02\x03",

            "#0506F……やっぱり駄目でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0930
    ChrTalk(
        0x101,
        (
            "#0008F#11Pう、うーん……\x02\x03",

            "#0003F遺跡の調査と言われても\x01",
            "俺たちもどうすればいいのか\x01",
            "さっぱり分からないけど……\x02\x03",

            "#0000F──君がここを訪ねたってことは\x01",
            "何か心当たりがあるんだな？\x02",
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
            "#5P#0500F……さすがはロイドさん。\x02\x03",

            "#0503F実は……\x01",
            "その化物と戦った時なんですけど。\x02\x03",

            "#0501F導力魔法#8Rオーバルアーツ#の効き方が\x01",
            "普段と違う感じがしたんです。\x02",
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
        "#0013F#11Pなんだって……！？\x02",
    )

    CloseMessageWindow()

    #C0933
    ChrTalk(
        0x102,
        "#0105F#6Pそれって、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0934
    ChrTalk(
        0x103,
        (
            "#6P#0203F#N以前このメンバーで入った\x01",
            "《星見の塔》と同じ……\x02\x03",

            "#0201F時・空・幻の上位三属性が\x01",
            "働いていたような感じですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0935
    ChrTalk(
        0x109,
        (
            "#5P#0506Fうん……\x01",
            "あの時の事を思い出しちゃって。\x02\x03",

            "それで、皆さんにも見てもらって\x01",
            "ご意見を伺えないかなって……\x02",
        )
    )

    CloseMessageWindow()

    #C0936
    ChrTalk(
        0x101,
        "#0003F#11Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0937
    ChrTalk(
        0x102,
        "#0106F#6Pそれで支援課の方に……\x02",
    )

    CloseMessageWindow()

    #C0938
    ChrTalk(
        0x109,
        (
            "#5P#0508F皆さん、お忙しいのは\x01",
            "重々承知しているんですけど……\x02\x03",

            "#0506Fこのままだと、また司令閣下が\x01",
            "放置しろとか命令してきそうで……\x02",
        )
    )

    CloseMessageWindow()

    #C0939
    ChrTalk(
        0x104,
        (
            "#0301Fま、あの事なかれ主義の\x01",
            "司令だったらあり得そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0940
    ChrTalk(
        0x101,
        "#0003F#11Pうーん……\x02",
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
            "#0000F#11Pみんな、せっかくだから\x01",
            "曹長に協力してみないか？\x02\x03",

            "市外の活動にはなるけど\x01",
            "何だかちょっと気になるし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0942
    ChrTalk(
        0x102,
        "#0108F#5Pそ、そうね……\x02",
    )

    CloseMessageWindow()

    #C0943
    ChrTalk(
        0x103,
        "#6P#0204F#Nわたしの方は異存ありません。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0944
    ChrTalk(
        0x104,
        (
            "#0304F#11P俺の方も問題ないぜ。\x02\x03",

            "#0302Fお嬢の方はどうやら、\x01",
            "気乗りがしないみたいだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0945
    ChrTalk(
        0x102,
        (
            "#0113F#5Pそ、そんな事ありません！\x02\x03",

            "#0112F幽霊が怖いなんて\x01",
            "そんな子供みたいな──あ。\x02",
        )
    )

    CloseMessageWindow()

    #C0946
    ChrTalk(
        0x104,
        "#0304F#11P語るに落ちたか。\x02",
    )

    CloseMessageWindow()

    #C0947
    ChrTalk(
        0xA,
        "#6P#1105Fエリィ、ユーレイが怖いのー？\x02",
    )

    CloseMessageWindow()

    #C0948
    ChrTalk(
        0x102,
        (
            "#0109F#5Pそ、そんなことないのよ？\x02\x03",

            "ただその、得体の知れない相手は\x01",
            "慎重に対処すべきというか……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0949
    ChrTalk(
        0x109,
        (
            "#11P#0506F無理もないですよ……\x02\x03",

            "あたしも任務じゃなかったら\x01",
            "進んで調査したいとは思いませんし。\x02\x03",

            "#0508F……でも、このまま\x01",
            "何も無かった事にされちゃうのは\x01",
            "なんだか納得できなくって……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0950
    ChrTalk(
        0x102,
        "#0108F#6Pあ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    #C0951
    ChrTalk(
        0x101,
        (
            "#0006F#11Pその気持ちはよく分かるよ。\x02\x03",

            "#0002Fえっと、何ならエリィは\x01",
            "留守番してくれてもいいけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0952
    ChrTalk(
        0x102,
        (
            "#0113F#5P分かった、分かりました！\x02\x03",

            "#0107F私も行きます、行きますとも！\x02",
        )
    )

    CloseMessageWindow()

    #C0953
    ChrTalk(
        0x103,
        "#6P#0202F#Nエリィさん、ヤケクソですね。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0954
    ChrTalk(
        0x104,
        "#0303F#11Pやれやれ、無茶しやがって。\x02",
    )

    CloseMessageWindow()

    #C0955
    ChrTalk(
        0x102,
        (
            "#0113F……そ、それはともかく。\x02\x03",

            "#0100F他の支援要請も来ているけど\x01",
            "そちらの方はどうするの？\x02",
        )
    )

    CloseMessageWindow()

    #C0956
    ChrTalk(
        0x101,
        (
            "#0003F#11Pそうだな、うーん……\x02\x03",

            "#0008Fそっちを片付けてから曹長と\x01",
            "合流するってのも面倒だし……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0957
    ChrTalk(
        0x109,
        (
            "#5P#0505Fあ、それなら……\x02\x03",

            "#0502F今日一日、あたしも皆さんに\x01",
            "お付き合いさせて頂きます。\x02\x03",

            "警備隊の車両に乗ってきたので\x01",
            "好きな場所にお送りしますよ？\x02",
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
        "#0005F#11Pえ、いいのか？\x02",
    )

    CloseMessageWindow()

    #C0959
    ChrTalk(
        0x109,
        (
            "#5P#0504Fええ、もちろんそのくらい。\x02\x03",

            "#0500F皆さんの用事が済んだら\x01",
            "山道外れにある遺跡に\x01",
            "向かうって事でどうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0960
    ChrTalk(
        0x102,
        (
            "#0100F#6Pなるほど……\x01",
            "効率的かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0961
    ChrTalk(
        0x103,
        (
            "#6P#0204F#N車で送っていただけるのは\x01",
            "正直、ありがたいですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0962
    ChrTalk(
        0x104,
        (
            "#0309Fヘッ、一課の気分が\x01",
            "味わえるってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0963
    ChrTalk(
        0x101,
        "#0004F#11P──決まりだな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0964
    ChrTalk(
        0x101,
        (
            "#0000F#11Pキーア。\x01",
            "午後からまた出かけるけど……\x02\x03",

            "ツァイトと一緒に\x01",
            "ちゃんと留守番できるかい？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0965
    ChrTalk(
        0xA,
        (
            "#6P#1104Fうん、だいじょーぶ。\x02\x03",

            "#1110Fロイドたちも\x01",
            "ユーレイ退治がんばってね！\x02",
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

    # Function_44_18D75 end

    def Function_45_1D179(): pass

    label("Function_45_1D179")

    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)

    def lambda_1D190():
        OP_95(0xFE, 800, 850, 10000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D190)
    WaitChrThread(0xA, 1)
    OP_68(200, 1000, 3500, 1500)
    SetCameraDistance(25000, 1500)

    def lambda_1D1C8():
        OP_95(0xFE, 200, 0, 3500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D1C8)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    Sound(819, 0, 100, 0)

    def lambda_1D1F4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D1F4)
    Sleep(500)
    Return()

    # Function_45_1D179 end

    def Function_46_1D20C(): pass

    label("Function_46_1D20C")

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
            "#0004F#11Pしかし驚いたな……\x02\x03",

            "#0000Fこの目玉焼き、\x01",
            "本当にキーアが焼いたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0967
    ChrTalk(
        0x102,
        (
            "#0102F#5Pふふ、そうよ。\x02\x03",

            "#0109Fあまりに手際がいいんで\x01",
            "思わず見惚れちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0968
    ChrTalk(
        0x8,
        "#11P#1002Fふむ、いい半熟具合だな。\x02",
    )

    CloseMessageWindow()

    #C0969
    ChrTalk(
        0x104,
        (
            "#0304F#11Pベーコンもカリカリで\x01",
            "言うことナシだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0970
    ChrTalk(
        0x103,
        (
            "#6P#0204F昨日のホワイトシチューを\x01",
            "手伝ってくれた時も\x01",
            "大した腕前でしたし……\x02\x03",

            "#0202Fやはり、料理の経験は\x01",
            "かなりあるのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0971
    ChrTalk(
        0xA,
        (
            "#6P#1111Fんー、そうなのかなぁ？\x02\x03",

            "#1102Fなんかかってに手が動いた\x01",
            "だけなんだけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0972
    ChrTalk(
        0x101,
        (
            "#0003F#11Pうーん、確かに料理は\x01",
            "身体で覚える所があるけど……\x02\x03",

            "#0000F（……それにしてもこの歳で\x01",
            "  ここまで上手なのも凄いな……）\x02",
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
            "#5P#1101Fねえねえ、ティオー。\x02\x03",

            "今日はだいじょーぶなのー？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0974
    ChrTalk(
        0x103,
        "#12P#0205Fあ……\x02",
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
            "#0108F#5P見たところ、顔色は\x01",
            "悪くはないみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0976
    ChrTalk(
        0x104,
        (
            "#0301F#11Pあんまり無理はしないで\x01",
            "休んだ方がいいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0977
    ChrTalk(
        0x103,
        (
            "#6P#0204Fいえ、大丈夫です。\x02\x03",

            "#0202F昨日も早めに\x01",
            "休ませてもらいましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0978
    ChrTalk(
        0x8,
        "#5P#1000Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0979
    ChrTalk(
        0x101,
        (
            "#0000F#5Pまあ、急ぎの仕事もないし\x01",
            "少し様子を見た方が──\x02",
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
        "#0005F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0981
    ChrTalk(
        0x104,
        "#0305F#11P朝っぱらから珍しいな。\x02",
    )

    CloseMessageWindow()

    #C0982
    ChrTalk(
        0x102,
        "#0100F#5Pフランさんかしら？\x02",
    )

    CloseMessageWindow()

    #C0983
    ChrTalk(
        0x101,
        "#0001F#11Pえっと……\x02",
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
            "#0000Fはい、特務支援課、\x01",
            "ロイド・バニングスで──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年の声")

    #A0985
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あーあー、ンなのは\x01",
            "とっくに判ってるっつーの！\x02\x03",

            "今どこ！　何してんのさ！？\x02",
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
            "#0005Fああ、ヨナか。\x02\x03",

            "#0002Fおはよう。\x01",
            "夜型のヨナがこんな早くに\x01",
            "起きてるなんて珍しいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0987
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ、そんなもん、\x01",
            "徹夜明けに決まってんだろ。\x02\x03",

            "──ああもう！\x01",
            "そんなのはどうでもいいんだよ！\x02\x03",

            "でもまあ、その様子じゃ\x01",
            "ゼンゼン知らないみたいだな！？\x02",
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
            "#0005F知らないって……何の事だ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0989
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ、大サービスで\x01",
            "このヨナ様が教えてやるよ！\x02\x03",

            "昨日の真夜中──\x01",
            "いや日付は今日になるのか。\x02\x03",

            "《黒月#4Rヘイユエ#》の事務所が\x01",
            "何者かに襲撃されたそうだぜ！\x02",
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
            "#0013F何だって……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0991
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "何でも《黒月》の方は\x01",
            "防戦一方だったみたいでさ～！\x02\x03",

            "かなり被害も出たみたいだぜ！？\x02\x03",

            "ま、襲ったのは間違いなく\x01",
            "ルバーチェの連中だろうけどな！\x02",
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
            "#0003Fそうだったのか……\x02\x03",

            "#0000Fありがとう、ヨナ。\x01",
            "情報提供感謝するよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0993
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ、今度何かで返せよな！\x07\x00\x02",
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
        "#6P#0205Fヨナからですか？\x02",
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
            "#0006F#11Pああ……どうやら\x01",
            "とんでもない事が起きたみたいだ。\x02",
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
            "ロイドたちは皆に、ヨナから聞いた情報を伝えた。\x07\x00\x02",
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
        "#0101F#5Pほ、本当なの……！？\x02",
    )

    CloseMessageWindow()

    #C0998
    ChrTalk(
        0x104,
        "#0301F#11Pおいおい、マジかよ！？\x02",
    )

    CloseMessageWindow()

    #C0999
    ChrTalk(
        0x103,
        (
            "#6P#0206F真夜中とはいえ、\x01",
            "市街地でそんな事が……\x02",
        )
    )

    CloseMessageWindow()

    #C1000
    ChrTalk(
        0xA,
        "#6P#1105Fほえ～？\x02",
    )

    CloseMessageWindow()

    #C1001
    ChrTalk(
        0x8,
        (
            "#5P#1003Fふむ……\x02\x03",

            "それが本当なら一課あたりが\x01",
            "とっくに動いてるんだろうが……\x02\x03",

            "#1002F気になるんなら行って来い。\x01",
            "──ただしメシを喰ってからな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C1002
    ChrTalk(
        0x101,
        "#0001Fはい、そうしてみます！\x02",
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
            "#0005F#5Pあ……\x01",
            "ティオ、大丈夫か？\x02",
        )
    )

    CloseMessageWindow()

    #C1004
    ChrTalk(
        0x103,
        (
            "#6P#0204Fええ、問題ありません。\x02\x03",

            "#0202F朝食を済ませたら\x01",
            "港湾区に向かいましょう。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4D9")
    OP_29(0x2A, 0x4, 0x40)
    Jump("loc_1E4EB")

    label("loc_1E4D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4EB")
    OP_29(0x2A, 0x4, 0x40)

    label("loc_1E4EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E509")
    OP_29(0x2C, 0x4, 0x40)
    Jump("loc_1E51B")

    label("loc_1E509")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E51B")
    OP_29(0x2C, 0x4, 0x40)

    label("loc_1E51B")

    OP_24(0x326)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_46_1D20C end

    def Function_47_1E524(): pass

    label("Function_47_1E524")

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
        "#12P#0005Fあの……課長？\x02",
    )

    CloseMessageWindow()

    #C1007
    ChrTalk(
        0x102,
        (
            "#0106Fす、すみません。\x01",
            "分かりにくい報告でしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C1008
    ChrTalk(
        0x9,
        "#5P#1003Fいや……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C1009
    ChrTalk(
        0x9,
        (
            "#5P#1001Fその一連の情報だが……\x02\x03",

            "ひょっとしたら全部、\x01",
            "繋がっているかもしれんぞ。\x02",
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
        "#12P#0011Fえ……\x02",
    )

    CloseMessageWindow()

    #C1011
    ChrTalk(
        0x104,
        "#0307Fマジかよ……！？\x02",
    )

    CloseMessageWindow()

    #C1012
    ChrTalk(
        0x102,
        "#0101Fそ、それはどういう！？\x02",
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
            "#5P#1003F色々な事が起きすぎて\x01",
            "混乱してるのかもしれんが……\x02\x03",

            "今日、お前らが見聞きした事を\x01",
            "有機的に結びつけてみろや。\x02\x03",

            "#1002F特にロイド──こういう時こそ\x01",
            "捜査官の本領発揮だろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C1015
    ChrTalk(
        0x101,
        "#12P#0011Fあ、はい……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C1016
    ChrTalk(
        0x101,
        (
            "#12P#0008F今日、聞き込んだ情報は\x01",
            "大まかにまとめて３つ……\x02\x03",

            "#0003Fツァオたちから聞いた\x01",
            "《黒月》襲撃に関する情報……\x02\x03",

            "グレイスさんと情報交換した\x01",
            "ルバーチェの現状に関する情報……\x02\x03",

            "#0001Fそしてマインツの鉱員、\x01",
            "ガンツさんに関する情報……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EA29():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1EA29)
    Sleep(50)

    def lambda_1EA39():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1EA39)
    Sleep(50)

    def lambda_1EA49():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1EA49)
    WaitChrThread(0x102, 2)

    #C1017
    ChrTalk(
        0x102,
        (
            "#0100Fそれらの３つの情報を\x01",
            "結びつける要素があるわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C1018
    ChrTalk(
        0x104,
        (
            "#0300Fふむ……\x01",
            "何となくだが見えてきたな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C1019
    ChrTalk(
        0x101,
        "#6P#0000Fああ、整理してみよう。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_1EAFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEC7")
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
            "#1K《黒月》襲撃に関する情報で\x01",
            "関連しそうな要素は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "襲撃者の身体能力\x01",              # 0
            "《黒月》本体からの増援\x01",        # 1
            "キーアに関する情報提供者\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EBBF")
    ClearScenarioFlags(0x0, 3)

    label("loc_1EBBF")

    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    #A1021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kルバーチェの現状に関する情報で\x01",
            "関連しそうな要素は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "マルコーニ会長の動き\x01",      # 0
            "軍用犬の戦力投入\x01",          # 1
            "場当たり的な組織運用\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC6A")
    ClearScenarioFlags(0x0, 3)

    label("loc_1EC6A")

    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    #A1022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K鉱員ガンツに関する情報で\x01",
            "関連しそうな要素は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "鉱山町から失踪した時期\x01",          # 0
            "カジノでのレクターとの勝負\x01",      # 1
            "所持していた蒼色の錠剤\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED1D")
    ClearScenarioFlags(0x0, 3)

    label("loc_1ED1D")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE4E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EDE1")
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C1023
    ChrTalk(
        0x101,
        (
            "#0006F#6P（うーん……\x01",
            "  やっぱり辻褄が合わない。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    #C1024
    ChrTalk(
        0x101,
        "#0005F#6P（もしかして、これか……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1EE49")

    label("loc_1EDE1")


    #C1025
    ChrTalk(
        0x101,
        (
            "#6P#0006F（いや……\x01",
            "  これだと噛み合わない。）\x02\x03",

            "#0001F（もう一度選び直してみよう。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EE49")

    Jump("loc_1EEC2")

    label("loc_1EE4E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1EE5E"),
        (SWITCH_DEFAULT, "loc_1EE91"),
    )


    label("loc_1EE5E")

    OP_2C(0x4C, 0x2)

    #C1026
    ChrTalk(
        0x101,
        "#6P#0000F（間違いない……これだ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EEC2")

    label("loc_1EE91")

    OP_2C(0x4C, 0x1)

    #C1027
    ChrTalk(
        0x101,
        "#6P#0003F（……多分、これだな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EEC2")

    label("loc_1EEC2")

    Jump("loc_1EAFA")

    label("loc_1EEC7")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A1028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "【関連しそうな要素】\x01",
            "①襲撃者の身体能力\x01",
            "②場当たり的な組織運用\x01",
            "③所持していた蒼色の錠剤\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C1029
    ChrTalk(
        0x102,
        "#0101Fこ、これは……\x02",
    )

    CloseMessageWindow()

    #C1030
    ChrTalk(
        0x104,
        (
            "#0310Fおいおい……\x01",
            "キナ臭すぎるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C1031
    ChrTalk(
        0x101,
        (
            "#6P#0006Fだが、こう関連付けると\x01",
            "色々と見えてくることがある。\x02\x03",

            "#0008F《黒月》を襲撃したマフィアたちが\x01",
            "見せたという身体能力……\x02\x03",

            "神がかり的なギャンブルの腕を\x01",
            "手に入れた鉱員のガンツさん……\x02\x03",

            "#0013Fどちらも別々の現象だけど\x01",
            "その人間の“潜在能力”が\x01",
            "上がっているというのは同じだ。\x02",
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
            "#0013Fもし、それを繋ぐものが\x01",
            "この『蒼い錠剤』だとするなら……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A1033
    AnonymousTalk(
        0x103,
        (
            "#0203F……マフィアたちが\x01",
            "違法薬物に手を出し始めた……\x02\x03",

            "そして一般市民に\x01",
            "流し始めているだけでなく\x01",
            "戦闘力の強化にも使っている……\x02\x03",

            "#0201F……つまりそういう事ですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A1034
    AnonymousTalk(
        0x101,
        (
            "#0006Fああ……\x01",
            "まだ憶測のレベルだけどね。\x02",
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
            "#0101Fで、でも確かに\x01",
            "それだと色々と説明できるわ。\x02\x03",

            "あの若頭の統率力が\x01",
            "ルバーチェ内で低下したのも\x01",
            "もしかして……\x02",
        )
    )

    CloseMessageWindow()

    #C1036
    ChrTalk(
        0x104,
        (
            "#0306Fクスリをキメて力を手に入れ、\x01",
            "態度もデカくなった下っ端連中が\x01",
            "増え始めている……\x02\x03",

            "#0301Fそのせいってわけかよ……\x02",
        )
    )

    CloseMessageWindow()

    #C1037
    ChrTalk(
        0x9,
        (
            "#5P#1003F──上出来だ。\x02\x03",

            "#1000F加えて昨日、イアン先生が\x01",
            "言っていた噂話もあるだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1F378():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F378)
    Sleep(150)

    def lambda_1F388():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F388)

    def lambda_1F395():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1F395)
    Sleep(50)

    def lambda_1F3A5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F3A5)
    WaitChrThread(0x104, 2)

    #C1038
    ChrTalk(
        0x101,
        (
            "#12P#0005F急激に業績を上げたっていう、\x01",
            "貿易商と証券マンですか……！\x02",
        )
    )

    CloseMessageWindow()

    #C1039
    ChrTalk(
        0x102,
        (
            "#0105Fそ、それでは彼らも\x01",
            "その蒼い錠剤を……！？\x02",
        )
    )

    CloseMessageWindow()

    #C1040
    ChrTalk(
        0x9,
        (
            "#5P#1006Fそれこそ現時点では\x01",
            "ただの憶測になっちまうがな。\x02\x03",

            "#1003Fだが、一つ一つの点が\x01",
            "線となり面を構築する……\x02\x03",

            "#1002Fそんな気がしてきたんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C1041
    ChrTalk(
        0x101,
        (
            "#12P#0006Fええ……\x02\x03",

            "#0008Fしかし正直、支援課だけでは\x01",
            "手に負えない状況かもしれません。\x02\x03",

            "#0001F特に薬物の件に関しては\x01",
            "一課に連絡する必要が\x01",
            "あるんじゃないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C1042
    ChrTalk(
        0x9,
        (
            "#5P#1004Fああ、その点に関しては\x01",
            "丁度いいタイミングだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C1043
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(63000, 1100, 4600, 2000)
    MoveCamera(60, 17, 0, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    def lambda_1F5FC():
        OP_95(0xFE, 62000, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F5FC)

    def lambda_1F616():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F616)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x101, 500)
    OP_6F(0x41)

    #C1044
    ChrTalk(
        0xA,
        "#12P#1110Fあ、ここにいたんだー。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1F6A5():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F6A5)
    Sleep(50)

    def lambda_1F6B5():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F6B5)
    Sleep(50)

    def lambda_1F6C5():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1F6C5)
    Sleep(50)

    def lambda_1F6D5():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F6D5)
    WaitChrThread(0x104, 2)

    #C1045
    ChrTalk(
        0x101,
        "#0005F#5Pキーア、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C1046
    ChrTalk(
        0x102,
        "#5P#0100Fお腹でも空いちゃった？\x02",
    )

    CloseMessageWindow()

    #C1047
    ChrTalk(
        0xA,
        (
            "#12P#1103Fんーん、お客さん。\x02\x03",

            "#1105Fぶすっとした\x01",
            "オジサンがきたよー？\x02",
        )
    )

    CloseMessageWindow()

    #C1048
    ChrTalk(
        0x101,
        "#0001F#5Pぶすっとしたオジサン……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    Sleep(150)
    Sound(1561, 255, 100, 0)    #voice#Dudley
    Sleep(1000)
    SetChrPos(0x16, 59000, 30, 3400, 90)

    def lambda_1F7CB():

        label("loc_1F7CB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1F7CB")

    QueueWorkItem2(0xA, 2, lambda_1F7CB)

    def lambda_1F7DD():
        OP_95(0xFE, 61800, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1F7DD)

    def lambda_1F7F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1F7F7)
    Sleep(300)

    def lambda_1F80B():
        OP_96(0xFE, 0xF8D4, 0x0, 0xD48, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F80B)
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
        "#0011F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C1050
    ChrTalk(
        0x102,
        "#5P#0105Fダドリー捜査官……！\x02",
    )

    CloseMessageWindow()

    #C1051
    ChrTalk(
        0x9,
        "#1002F#5P#Nおう、遅かったな。\x02",
    )

    CloseMessageWindow()
    OP_68(64000, 1100, 8600, 2000)
    MoveCamera(50, 17, 0, 2000)

    def lambda_1F917():

        label("loc_1F917")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1F917")

    QueueWorkItem2(0x101, 2, lambda_1F917)

    def lambda_1F929():

        label("loc_1F929")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1F929")

    QueueWorkItem2(0x102, 2, lambda_1F929)

    def lambda_1F93B():

        label("loc_1F93B")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1F93B")

    QueueWorkItem2(0x103, 2, lambda_1F93B)

    def lambda_1F94D():

        label("loc_1F94D")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_1F94D")

    QueueWorkItem2(0x104, 2, lambda_1F94D)

    def lambda_1F95F():
        OP_95(0xFE, 62800, 0, 7200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1F95F)
    Sleep(500)

    def lambda_1F97C():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F97C)
    Sleep(100)

    def lambda_1F999():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F999)
    Sleep(100)

    def lambda_1F9B6():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F9B6)
    Sleep(100)

    def lambda_1F9D3():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F9D3)
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
            "……済みません。\x01",
            "捜査会議が長引いてしまって。\x02\x03",

            "例の話についてですが\x01",
            "早速、始めさせてもらっても\x01",
            "構いませんか？\x02",
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
            "#5P#1003Fおお、構わんぞ。\x02\x03",

            "#1002Fコイツらも一緒で良けりゃあな。\x02",
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
            "#12P#0601Fセルゲイさん！\x01",
            "冗談は止めてください！\x02\x03",

            "こんなヒヨッ子どもに\x01",
            "聞かせるような話では──\x02",
        )
    )

    CloseMessageWindow()

    #C1055
    ChrTalk(
        0x9,
        (
            "#5P#1004Fだが、今回の件については\x01",
            "こいつらが集めてきた情報が\x01",
            "きっと役に立つだろう。\x02\x03",

            "#1000F同席させた方が手っ取り早いぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C1056
    ChrTalk(
        0x16,
        "#12P#0605Fなんですって……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(300)

    #C1057
    ChrTalk(
        0x16,
        (
            "#6P#0601Fそういえば《黒月》の聞き込みも\x01",
            "お前たちに任せていた所だったか。\x02\x03",

            "#0608Fそのついでに……\x01",
            "……い、いやしかし……\x02",
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
            "#11P#0006Fえっと、課長……\x02\x03",

            "#0000F都合が悪いようでしたら\x01",
            "俺たちは退室しましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C1059
    ChrTalk(
        0x9,
        (
            "#5P#1003Fいや、その必要はない。\x02\x03",

            "#1002Fその男も、伊達に一課の\x01",
            "エースを張ってるわけじゃねえ。\x02\x03",

            "この状況で何が必要かは\x01",
            "きちんと見抜けるだろうさ。\x02",
        )
    )

    CloseMessageWindow()

    #C1060
    ChrTalk(
        0x16,
        (
            "#6P#0603Fくっ……分かりましたよ。\x02\x03",

            "#0601F──いいかお前たち。\x01",
            "これから話すのは\x01",
            "警察内部の機密事項だ……\x02\x03",

            "#0607Fみだりに他言することは\x01",
            "絶対に許さんからな！？\x02",
        )
    )

    CloseMessageWindow()

    #C1061
    ChrTalk(
        0x101,
        "#11P#0005Fわ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C1062
    ChrTalk(
        0xA,
        (
            "#1110Fなになに、ひみつのお話ー？\x02\x03",

            "#1109Fキーアも聞きたーい！\x02",
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

    def lambda_1FF6E():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FF6E)

    def lambda_1FF7B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FF7B)

    def lambda_1FF88():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1FF88)

    def lambda_1FF95():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1FF95)

    def lambda_1FFA2():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1FFA2)
    WaitChrThread(0x104, 2)

    #C1063
    ChrTalk(
        0x101,
        "#5P#0012Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C1064
    ChrTalk(
        0x102,
        (
            "#5P#0102Fお菓子を用意するから\x01",
            "ツァイトと一緒に食べててね？\x02",
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
        "#0013F捜査一課に圧力……！？\x02",
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
            "#0603F#11Pいや、そこまで\x01",
            "露骨なものではないが……\x02\x03",

            "#0601F《黒月》の襲撃事件を受けて\x01",
            "マフィア同士の抗争への対処に\x01",
            "全力を傾けろとの指示が下った。\x02\x03",

            "#0606F……少し前から追っていた\x01",
            "謎の薬物の捜査を打ち切ってな。\x02",
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
        "#6P#0011Fな……！？\x02",
    )

    CloseMessageWindow()

    #C1068
    ChrTalk(
        0x103,
        (
            "#6P#0205F一課の方でも\x01",
            "薬物に関する捜査を……？\x02",
        )
    )

    CloseMessageWindow()

    #C1069
    ChrTalk(
        0x16,
        (
            "#0603F#11Pフン、数日前からだがな。\x02\x03",

            "#0600F私としてはお前たちが\x01",
            "知っていた事の方が驚きだが。\x02",
        )
    )

    CloseMessageWindow()

    #C1070
    ChrTalk(
        0x9,
        (
            "#5P#1001Fで、一課の方はどこで\x01",
            "その薬物のネタを掴んだんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C1071
    ChrTalk(
        0x16,
        (
            "#0603F……昔から使っていた\x01",
            "情報屋からのタレコミです。\x02\x03",

            "#0600Fそれなりに信頼できる筋なので\x01",
            "情報収集をしていた所ですが……\x02\x03",

            "今のところ集まっているのは\x01",
            "都市伝説のような噂だけですね。\x02\x03",

            "#0606F『願いが叶う薬』だの\x01",
            "『幸せを運ぶ青い薬』だの……\x02\x03",

            "ただ、どうにもキナ臭いので\x01",
            "噂になっている市民のリストを\x01",
            "揃えている最中だったんですが……\x02",
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
            "#0605F#11Pな、何だお前たち……\x01",
            "その『やっぱり』という顔は。\x02",
        )
    )

    CloseMessageWindow()

    #C1073
    ChrTalk(
        0x9,
        (
            "#5P#1003Fフン……\x01",
            "ビンゴだったようだな。\x02\x03",

            "#1000Fロイド、見せてやれ。\x02",
        )
    )

    CloseMessageWindow()

    #C1074
    ChrTalk(
        0x101,
        "#6P#0003F……はい。\x02",
    )

    CloseMessageWindow()

    #C1075
    ChrTalk(
        0x16,
        "#0605F#11P？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 0)

    def lambda_205AF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_205AF)
    WaitChrThread(0x101, 1)

    #C1076
    ChrTalk(
        0x101,
        "#6P#0001Fこれを──\x02",
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
            "#0607F#4Sな……！\x02\x03",

            "も、もしかしてこれは……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A1078
    AnonymousTalk(
        0x101,
        (
            "#0006F……今日、ある筋から\x01",
            "俺たちが入手した証拠物件です。\x02\x03",

            "#0001Fその人の名誉を守るという条件で\x01",
            "預からせてもらったんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)

    def lambda_206FE():
        OP_96(0xFE, 0xF4EC, 0x0, 0x189C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_206FE)
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
            "これまでの経緯を一通りダドリーに説明した。\x07\x00\x02",
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
            "#0608F#11Pクッ……\x01",
            "やはり存在していたのか……\x02\x03",

            "#0610Fしかもルバーチェが流した\x01",
            "可能性があるだと……！？\x02",
        )
    )

    CloseMessageWindow()

    #C1081
    ChrTalk(
        0x9,
        (
            "#5P#1003Fその薬物捜査を\x01",
            "打ち切れという指示……\x02\x03",

            "#1000Fどこから降りてきたか\x01",
            "見当はつくのか？\x02",
        )
    )

    CloseMessageWindow()

    #C1082
    ChrTalk(
        0x16,
        (
            "#0606F……上層部の誰かかと。\x02\x03",

            "#0608F一課#4Rウ チ#の課長も納得出来ないまま、\x01",
            "我々に指令を下していました。\x02",
        )
    )

    CloseMessageWindow()

    #C1083
    ChrTalk(
        0x9,
        "#5P#1006Fフン、最悪だな……\x02",
    )

    CloseMessageWindow()

    #C1084
    ChrTalk(
        0x102,
        (
            "#6P#0105Fちょ、ちょっと待って下さい。\x02\x03",

            "#0110Fまさか警察の上層部が\x01",
            "マフィアの要請を受けて……！？\x02",
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
        "#6P#0006Fそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C1086
    ChrTalk(
        0x104,
        "#6P#0301Fおいおい、マジかよ……\x02",
    )

    CloseMessageWindow()

    #C1087
    ChrTalk(
        0x103,
        "#6P#0206F……確かに最悪ですね。\x02",
    )

    CloseMessageWindow()

    #C1088
    ChrTalk(
        0x9,
        (
            "#5P#1003F──ダドリー。\x02\x03",

            "#1000F俺の所に相談に来たってことは\x01",
            "上層部に不審を抱いたからだろう。\x02\x03",

            "それで、どうするつもりだ？\x02",
        )
    )

    CloseMessageWindow()

    #C1089
    ChrTalk(
        0x16,
        (
            "#0608F…………………………………\x02\x03",

            "#0606F……正直、薬物捜査に関しては\x01",
            "こちらでは動きようがありません。\x02\x03",

            "下手に動けば、今度は上層部も\x01",
            "露骨に横槍を入れてくるでしょう。\x02\x03",

            "#0610Fだが、それでは警察組織として\x01",
            "余りに不甲斐なさすぎる……！\x02",
        )
    )

    CloseMessageWindow()

    #C1090
    ChrTalk(
        0x101,
        "#6P#0005Fダドリー捜査官……\x02",
    )

    CloseMessageWindow()

    #C1091
    ChrTalk(
        0x9,
        (
            "#5P#1002Fだったら薬物捜査に関しては\x01",
            "ウチに任せてもらうしかないな。\x02",
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
            "#5P#1000F──ロイド、エリィ。\x01",
            "それにランディにティオ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20C00():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20C00)
    Sleep(50)

    def lambda_20C10():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_20C10)
    Sleep(50)

    def lambda_20C20():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_20C20)
    Sleep(50)

    def lambda_20C30():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_20C30)
    Sleep(500)

    #C1093
    ChrTalk(
        0x9,
        (
            "#5P#1003Fこれより特務支援課は非公式に\x01",
            "捜査一課と協力体制に入る。\x02\x03",

            "#1001F身動きの取れない一課に代わって\x01",
            "このまま薬物捜査に当たれ。\x02",
        )
    )

    CloseMessageWindow()

    #C1094
    ChrTalk(
        0x101,
        "#12P#0001Fはい……！\x02",
    )

    CloseMessageWindow()

    #C1095
    ChrTalk(
        0x102,
        "#12P#0101F了解しました！\x02",
    )

    CloseMessageWindow()

    #C1096
    ChrTalk(
        0x9,
        "#5P#1003Fふむ、その見返りだが……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    #C1097
    ChrTalk(
        0x9,
        (
            "#5P#1002F一課からはマフィア関連の情報を\x01",
            "無制限で回してもらう事にする。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x16, 0x9, 500)

    def lambda_20DB0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20DB0)
    Sleep(50)

    def lambda_20DC0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_20DC0)
    Sleep(50)

    def lambda_20DD0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_20DD0)
    Sleep(50)

    def lambda_20DE0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_20DE0)
    Sleep(150)

    #C1098
    ChrTalk(
        0x16,
        (
            "#0605Fセ、セルゲイさん！？\x02\x03",

            "いくらなんでも極秘情報を\x01",
            "無制限というのはさすがに……\x02",
        )
    )

    CloseMessageWindow()

    #C1099
    ChrTalk(
        0x9,
        (
            "#5P#1002F別にこちらは構わんぞ？\x02\x03",

            "そちらが手詰まりになろうが\x01",
            "勝手に動くだけだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C1100
    ChrTalk(
        0x16,
        (
            "#0601Fくっ……\x02\x03",

            "#0606F……分かりました。\x01",
            "その条件で構いません。\x02",
        )
    )

    CloseMessageWindow()

    #C1101
    ChrTalk(
        0x9,
        "#5P#1002Fクク、決まりだな。\x02",
    )

    CloseMessageWindow()

    #C1102
    ChrTalk(
        0x104,
        (
            "#6P#0309Fいや～、あの一課に代わって\x01",
            "わざわざ俺らが動いてやるわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C1103
    ChrTalk(
        0x103,
        (
            "#6P#0204Fなかなか優越感を\x01",
            "くすぐられる状況ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0x10E, 0x1F4)

    #C1104
    ChrTalk(
        0x16,
        "#0610F#11P……………………（ギロッ）\x02",
    )

    CloseMessageWindow()

    #C1105
    ChrTalk(
        0x104,
        "#6P#0305Fおおコワ……\x02",
    )

    CloseMessageWindow()

    #C1106
    ChrTalk(
        0x103,
        "#6P#0206F……くわばらくわばらです。\x02",
    )

    CloseMessageWindow()

    #C1107
    ChrTalk(
        0x16,
        (
            "#0603F#11Pフン、まあ仕方あるまい。\x02\x03",

            "#0601Fこうなった以上、お前たちに\x01",
            "薬物捜査を任せるのは納得したが……\x02\x03",

            "今後の捜査方針はどうするつもりだ？\x02",
        )
    )

    CloseMessageWindow()

    #C1108
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそうですね……\x02\x03",

            "#0001F──何はともあれ、\x01",
            "薬の現物が手元にありますし。\x02\x03",

            "どういった成分かを\x01",
            "突き止める必要があるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C1109
    ChrTalk(
        0x16,
        (
            "#0600F#11Pふむ……\x01",
            "だが、どうやって突き止める？\x02\x03",

            "現時点での情報から推測するに\x01",
            "全く新しいタイプの薬物だ。\x02\x03",

            "本部の鑑識では手に余るし、\x01",
            "上からも目を付けられやすいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C1110
    ChrTalk(
        0x101,
        (
            "#6P#0008Fなるほど……\x02\x03",

            "#0000F……そうなると医科大学を\x01",
            "頼った方がいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_21270")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C1111
    ChrTalk(
        0x102,
        (
            "#5P#0100Fなるほど……\x01",
            "あの先生に頼るわけね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21325")

    label("loc_21270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_212CE")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x101, 500)

    #C1112
    ChrTalk(
        0x103,
        (
            "#6P#0202F……なるほど。\x01",
            "あの先生に頼りますか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21325")

    label("loc_212CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_21325")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    #C1113
    ChrTalk(
        0x104,
        (
            "#3P#0300Fなるほどな……\x01",
            "あの先生に頼んのか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21325")


    #C1114
    ChrTalk(
        0x16,
        (
            "#0605F#11P医科大学……\x01",
            "聖ウルスラ医科大学か？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2135D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2135D)

    def lambda_2136A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2136A)

    def lambda_21377():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_21377)

    #C1115
    ChrTalk(
        0x101,
        (
            "#6P#0004Fええ、薬学を研究している\x01",
            "知り合いの先生がいるんです。\x02\x03",

            "#0000F相当優秀だと聞いているので\x01",
            "薬の成分を突き止められる\x01",
            "可能性は高いのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C1116
    ChrTalk(
        0x16,
        "#0600F#11Pフン、なるほどな……\x02",
    )

    CloseMessageWindow()

    #C1117
    ChrTalk(
        0x9,
        (
            "#5P#1003F成分調査に関しては\x01",
            "それしか手は無さそうだな。\x02\x03",

            "#1000Fダドリー、そちらは\x01",
            "一課でまとめた捜査報告書を\x01",
            "今日中にこちらに回してくれ。\x02\x03",

            "それを元に、こいつらに\x01",
            "今後の捜査方針を決めさせたい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x9, 500)
    Sleep(150)

    #C1118
    ChrTalk(
        0x16,
        (
            "#0600F分かりました。\x01",
            "すぐにお届けに上がります。\x02\x03",

            "#0604F──では、私はこれで。\x01",
            "今後とも宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C1119
    ChrTalk(
        0x9,
        (
            "#5P#1004Fああ、こちらこそな。\x02\x03",

            "#1002Fそれと、その言葉は\x01",
            "こいつらにも言ってやれ。\x02",
        )
    )

    CloseMessageWindow()

    #C1120
    ChrTalk(
        0x16,
        "#0610Fうっ……\x02",
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
            "#0603F──いいか、お前たち。\x02\x03",

            "#0601Fくれぐれも迂闊なことをして\x01",
            "事態を悪化させたりするなよ？\x02\x03",

            "#0607Fそれと薬物捜査はともかく\x01",
            "マフィアどもの抗争への対処は\x01",
            "我々一課の担当だ！\x02\x03",

            "首を突っ込んだりせずに\x01",
            "大人しく任せておくがいい！\x02",
        )
    )

    CloseMessageWindow()

    #C1122
    ChrTalk(
        0x101,
        "#6P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    def lambda_21705():

        label("loc_21705")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_21705")

    QueueWorkItem2(0x101, 2, lambda_21705)

    def lambda_21717():

        label("loc_21717")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_21717")

    QueueWorkItem2(0x102, 2, lambda_21717)

    def lambda_21729():

        label("loc_21729")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_21729")

    QueueWorkItem2(0x103, 2, lambda_21729)

    def lambda_2173B():

        label("loc_2173B")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2173B")

    QueueWorkItem2(0x104, 2, lambda_2173B)
    OP_92(0x16, 0xF230, 0xD48, 0x1F4)
    OP_68(62000, 1100, 5500, 2000)

    def lambda_2176B():
        OP_95(0xFE, 62000, 0, 3400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2176B)
    WaitChrThread(0x16, 1)

    def lambda_21789():
        OP_95(0xFE, 59000, 0, 3400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_21789)
    Sleep(500)
    SetChrSubChip(0x9, 0x2)
    Sound(103, 0, 100, 0)

    def lambda_217B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_217B0)
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
            "#5P#0302Fやれやれ。\x01",
            "素直じゃねえ兄さんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C1124
    ChrTalk(
        0x103,
        (
            "#5P#0204F……あれは一種の\x01",
            "照れ隠しなのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C1125
    ChrTalk(
        0x102,
        (
            "#5P#0109Fふふ、そうかもしれないわね。\x02\x03",

            "#0102Fそれに思っていたより、\x01",
            "正義感がある人みたいだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C1126
    ChrTalk(
        0x101,
        (
            "#11P#0002Fああ……\x01",
            "それは信用できる気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C1127
    ChrTalk(
        0x9,
        (
            "#5P#1004F基本的に一課の連中は\x01",
            "真面目で正義感のあるヤツが多い。\x02\x03",

            "まあ杓子定規で、融通が\x01",
            "利かないヤツも多いんだがな。\x02",
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
            "#5P#1005F──さてと、お前ら。\x01",
            "さっそく病院に向かうのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_219E2():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_219E2)
    Sleep(100)

    def lambda_219F2():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_219F2)
    Sleep(50)

    def lambda_21A02():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21A02)
    Sleep(50)
    TurnDirection(0x104, 0x9, 500)

    #C1129
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、そのつもりです。\x02\x03",

            "それと時間があれば\x01",
            "他の支援要請も片付けておこうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C1130
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそうね……午前中は\x01",
            "市外に出る暇も無かったし。\x02",
        )
    )

    CloseMessageWindow()

    #C1131
    ChrTalk(
        0x104,
        (
            "#6P#0300Fま、忙しくなりそうだから\x01",
            "ボチボチ片付けた方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C1132
    ChrTalk(
        0x9,
        (
            "#5P#1004Fクク、元気なことで結構だ。\x02\x03",

            "#1002F一課と協力する事になったとはいえ、\x01",
            "お前たちが気負う必要はない。\x02\x03",

            "いつも通り、お前たちのやり方で\x01",
            "その薬物の謎に迫ってみせろ。\x02",
        )
    )

    CloseMessageWindow()

    #C1133
    ChrTalk(
        0x101,
        "#12P#0000Fはい！\x02",
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

    # Function_47_1E524 end

    def Function_48_21C79(): pass

    label("Function_48_21C79")

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
            "#5P#1000Fウルスラ病院か……\x02\x03",

            "その先生ってのは\x01",
            "前にキーアの記憶喪失の\x01",
            "相談に乗ってもらった人物か？\x02",
        )
    )

    CloseMessageWindow()

    #C1135
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、ヨアヒム先生という\x01",
            "薬学と神経科の准教授です。\x02\x03",

            "以前話した時、薬物に関しては\x01",
            "相当詳しそうな印象でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C1136
    ChrTalk(
        0x9,
        (
            "#5P#1003Fふむ、何とかその先生が\x01",
            "頼りになるといいんだが……\x02",
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
        "#12P#0005F課長……？\x02",
    )

    CloseMessageWindow()

    #C1138
    ChrTalk(
        0x102,
        "#0101Fその、何か気がかりでも？\x02",
    )

    CloseMessageWindow()

    #C1139
    ChrTalk(
        0x9,
        (
            "#5P#1006F……まあな。\x02\x03",

            "#1003F筋力、スピード、集中力、カン。\x02\x03",

            "そういうものは薬物で生理的に\x01",
            "高めることは出来るのかもしれん。\x02\x03",

            "#1001Fだが……\x01",
            "“ツキ”ってのは上げられるのか？\x02",
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
        "#12P#0011Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C1141
    ChrTalk(
        0x102,
        (
            "#0106F普通に考えたら\x01",
            "無理だと思いますけど……\x02\x03",

            "#0101Fでも、あのガンツさんは\x01",
            "ツキも凄かったという話よね？\x02",
        )
    )

    CloseMessageWindow()

    #C1142
    ChrTalk(
        0x104,
        (
            "#0303Fああ、どんなギャンブルも\x01",
            "カンと駆け引きだけで\x01",
            "勝ち続けられるもんじゃねぇ。\x02\x03",

            "#0308F女神を味方に引き入れたか、\x01",
            "それとも悪魔でも頼ったか……\x02",
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
            "#5P#1003Fふむ、色々と謎は多そうだな。\x02\x03",

            "#1000F──ティオ。\x01",
            "できればその辺りの事は\x01",
            "きちんと確かめてくるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C1145
    ChrTalk(
        0x103,
        "#12P#0203Fはい……そのつもりです。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_221E9():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_221E9)
    Sleep(50)

    def lambda_221F9():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_221F9)
    Sleep(50)

    def lambda_22209():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22209)
    Sleep(200)

    #C1146
    ChrTalk(
        0x101,
        "#5P#0005F（どうしてティオに……？）\x02",
    )

    CloseMessageWindow()

    #C1147
    ChrTalk(
        0x102,
        "#5P#0105F（何かあるのかしら……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 64000, 30, 5500, 180)
    SetScenarioFlags(0xC3, 1)
    EventEnd(0x5)
    Return()

    # Function_48_21C79 end

    def Function_49_2227E(): pass

    label("Function_49_2227E")

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
            "#0006F#11P──ティオ、本当に大丈夫か？\x02\x03",

            "#0001F何だったら課長やキーアと一緒に\x01",
            "支援課で待機してくれても……\x02",
        )
    )

    CloseMessageWindow()

    #C1149
    ChrTalk(
        0x103,
        (
            "#0204F#5P……心配ご無用です。\x02\x03",

            "#0202F早めに休ませてもらいましたし\x01",
            "普段より調子がいいくらいです。\x02",
        )
    )

    CloseMessageWindow()

    #C1150
    ChrTalk(
        0x101,
        (
            "#0002F#11Pそうか……\x01",
            "うん、顔色も良さそうだな。\x02\x03",

            "#0006Fしかしキーアがいきなり\x01",
            "一緒に寝るとか言い出した時は\x01",
            "ビックリしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C1151
    ChrTalk(
        0xA,
        (
            "#5P#1100Fんー、なんか\x01",
            "そーしたいって思ったから。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 500)

    #C1152
    ChrTalk(
        0xA,
        (
            "#6P#1101Fねえねえ、ティオ。\x01",
            "ぐっすりねむれたー？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 500)

    #C1153
    ChrTalk(
        0x103,
        (
            "#11P#0202Fええ、それはもちろん。\x02\x03",

            "#0204Fおそらく絶好調なのは\x01",
            "キーア分を大量に補給したのが\x01",
            "最大の理由かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C1154
    ChrTalk(
        0xA,
        "#6P#1109Fえへへ、よかったー！\x02",
    )

    CloseMessageWindow()

    #C1155
    ChrTalk(
        0x104,
        "#12P#0309Fはは、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C1156
    ChrTalk(
        0x102,
        (
            "#12P#0109F確かにキーアちゃんは\x01",
            "最高の特効薬になりそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C1157
    ChrTalk(
        0x101,
        (
            "#0004Fああ#11P……そうだな。\x02\x03",

            "#0008F──なあティオ。\x01",
            "一つだけ約束してくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_22708():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_22708)
    Sleep(100)
    OP_93(0xA, 0xB4, 0x1F4)

    #C1158
    ChrTalk(
        0x103,
        "#0205F#5P……え………\x02",
    )

    CloseMessageWindow()

    #C1159
    ChrTalk(
        0x101,
        (
            "#0006F#11P昨日みたいな事があったら\x01",
            "すぐに俺たちに言ってくれ。\x02\x03",

            "自分一人で溜め込んで\x01",
            "無理をするのだけはダメだ。\x02\x03",

            "#0001F酷な言い方だけど……\x01",
            "戦闘の時に倒れられたら\x01",
            "足手まといになりかねない。\x02",
        )
    )

    CloseMessageWindow()

    #C1160
    ChrTalk(
        0x103,
        (
            "#0204F#5P……はい、肝に銘じます。\x02\x03",

            "わたしも支援課の一員……\x01",
            "同じ仲間でありたいですから。\x02\x03",

            "#0214Fだから……\x01",
            "わたしの苦しみも、辛さも、\x01",
            "どうか分かち合ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C1161
    ChrTalk(
        0x102,
        "#12P#0102Fティオちゃん……\x02",
    )

    CloseMessageWindow()

    #C1162
    ChrTalk(
        0x104,
        (
            "#12P#0309F……はは。\x01",
            "お安い御用だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C1163
    ChrTalk(
        0x101,
        (
            "#0002F#11Pああ……喜んで\x01",
            "分かち合わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C1164
    ChrTalk(
        0xA,
        "#5P#1105Fほえ～……\x02",
    )

    CloseMessageWindow()

    #C1165
    ChrTalk(
        0x8,
        (
            "#5P#1009Fクク、確かにこりゃあ、\x01",
            "オッサンの出る幕はねぇな。\x02\x03",

            "#1002F──たしか午前中は\x01",
            "薬物を使用した疑いのある\x01",
            "市民の聞き込みだったな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_229CB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_229CB)
    Sleep(50)

    def lambda_229DB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_229DB)
    Sleep(50)

    def lambda_229EB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_229EB)
    Sleep(300)

    #C1166
    ChrTalk(
        0x101,
        (
            "#6P#0003Fええ、一課の資料も参考に\x01",
            "改めて確認してみようかと。\x02\x03",

            "#0000Fそれと、忙しくなりそうなので\x01",
            "今のうちに他の支援要請なども\x01",
            "片付けておくつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C1167
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそうですね……\x01",
            "このタイミングを逃がしたら\x01",
            "市外に出る余裕は無さそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C1168
    ChrTalk(
        0x104,
        (
            "#12P#0306Fしかし住宅街の証券マンに\x01",
            "サーベルバイパーのパシリ……\x02\x03",

            "#0301Fそれにアルカンシェルの\x01",
            "新米キャストか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22BBA")
    OP_2C(0x4C, 0x2)

    #C1169
    ChrTalk(
        0x102,
        (
            "#0106F#6Pどれも昨日の時点で\x01",
            "少し様子が変だった人たちね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C50")

    label("loc_22BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22C05")

    #C1170
    ChrTalk(
        0x102,
        (
            "#0101F#6Pさすが一課……\x01",
            "よく突き止めたわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C50")

    label("loc_22C05")

    OP_2C(0x4C, 0x1)

    #C1171
    ChrTalk(
        0x102,
        (
            "#0108F#6P確かに、昨日の時点で様子が\x01",
            "おかしかった人もいるわね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C50")


    #C1172
    ChrTalk(
        0x8,
        (
            "#5P#1003F時間があるならイアン先生の\x01",
            "事務所にも行った方がいいだろう。\x02\x03",

            "#1001F先生から聞いた２人のうち、\x01",
            "証券マンは一課の資料にあったのと\x01",
            "同一人物のようだが……\x02\x03",

            "貿易会社の経営者ってのは\x01",
            "まだマークされていないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C1173
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそうですね……\x01",
            "法律事務所にも行ってみます。\x02\x03",

            "#0001Fあとは午後あたりに\x01",
            "ヨアヒム先生が成分調査の結果を\x01",
            "連絡してくれるはずですけど……\x02",
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

    def lambda_22E2F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22E2F)
    Sleep(50)

    def lambda_22E3F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_22E3F)
    Sleep(50)

    def lambda_22E4F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_22E4F)
    Sleep(50)

    def lambda_22E5F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_22E5F)
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
            "#0001Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A1175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……ロイド君？\x01",
            "私だ、マインツのビクセンだ。\x02",
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
            "#0005Fああ、町長さん。\x02\x03",

            "#0000F──丁度よかった。\x01",
            "ガンツさんの様子はどうですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A1177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そ、それが……\x02\x03",

            "その……ガンツのやつが\x01",
            "また居なくなってしまったんだ。\x02",
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

            "#0001F……詳しい話を\x01",
            "聞かせてもらえますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A1179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あの後、夜遅くに\x01",
            "ガンツが目を覚ましたんだが……\x02\x03",

            "意識が朦朧としてるようで\x01",
            "そのまま寝かせてしまったんだ。\x02\x03",

            "念のため私も部屋に泊まって\x01",
            "明日の朝、君たちにも話を\x01",
            "聞いてもらうつもりだったが……\x02\x03",

            "朝、目を覚ましたら……\x02",
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
            "#0003F……なるほど。\x02\x03",

            "#0001Fホテルやカジノに問い合わせは？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A1181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "い、一応したが\x01",
            "誰も見た者はいないみたいで……\x02\x03",

            "ロイド君……　\x01",
            "どうしたらいいと思う？\x02",
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
            "#0003F……町長の方は\x01",
            "ホテルに待機してください。\x02\x03",

            "ひょっとしたらガンツさんが\x01",
            "戻ってくるかもしれません。\x02\x03",

            "#0000Fこちらは聞き込みに出るので\x01",
            "彼の事も気に留めておきます。\x02\x03",

            "何かあったら\x01",
            "また連絡してください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A1183
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "わ、分かった……よろしく頼む！\x07\x00\x02",
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
            "#12P#0101F……ガンツさんが\x01",
            "居なくなってしまったの？\x02",
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
            "#0006F#5Pああ……今朝ホテルから\x01",
            "抜け出してしまったらしい。\x02\x03",

            "#0008F自分から消えてしまったのか\x01",
            "それとも……\x02",
        )
    )

    CloseMessageWindow()

    #C1186
    ChrTalk(
        0x103,
        (
            "#0201F#5P……やはり他の人たちの様子も\x01",
            "確認する必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C1187
    ChrTalk(
        0x104,
        (
            "#12P#0301Fああ……\x01",
            "妙に嫌な予感がしやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C1188
    ChrTalk(
        0x8,
        (
            "#5P#1003F……どうやら思ってた以上に\x01",
            "事態の進行が早いかもしれんな。\x02\x03",

            "#1000Fこちらの事は心配するな。\x01",
            "とっとと確かめて来るといい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2353C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2353C)
    Sleep(50)

    def lambda_2354C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2354C)
    Sleep(50)

    def lambda_2355C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2355C)
    Sleep(300)

    #C1189
    ChrTalk(
        0x101,
        "#6P#0000Fはい！\x02",
    )

    CloseMessageWindow()

    #C1190
    ChrTalk(
        0xA,
        "#5P#1109Fいってらっしゃーい！\x02",
    )

    CloseMessageWindow()

    #C1191
    ChrTalk(
        0xE,
        "#1200F#5Pウォン！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_236D0")
    OP_29(0x2D, 0x4, 0x40)
    Jump("loc_236E2")

    label("loc_236D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236E2")
    OP_29(0x2D, 0x4, 0x40)

    label("loc_236E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23700")
    OP_29(0x30, 0x4, 0x40)
    Jump("loc_23712")

    label("loc_23700")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23712")
    OP_29(0x30, 0x4, 0x40)

    label("loc_23712")

    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_49_2227E end

    def Function_50_23718(): pass

    label("Function_50_23718")

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

    def lambda_23905():
        OP_93(0xA, 0x10E, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_23905)
    WaitChrThread(0xA, 2)

    def lambda_23916():
        OP_93(0xA, 0x59, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_23916)
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
            "#6P#0307Fだああっ！\x01",
            "遅い、遅すぎんだろ！？\x02\x03",

            "#0301Fあの先生、午後には連絡を\x01",
            "くれるんじゃなかったのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C1197
    ChrTalk(
        0x102,
        (
            "#0108F#11P病院の受付に連絡したら\x01",
            "どうやら研究室に閉じこもって\x01",
            "熱心に調べているらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C1198
    ChrTalk(
        0x103,
        (
            "#6P#0203F薬の成分の解析に\x01",
            "手こずっているのかもしれません。\x02\x03",

            "#0211F……もしくはサボって\x01",
            "釣りでもしているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C1199
    ChrTalk(
        0x101,
        (
            "#11P#0012Fさ、さすがに\x01",
            "それは無いと思うけど……\x02",
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

    def lambda_23CA1():
        OP_96(0xFE, 0x3A34, 0x352, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23CA1)

    def lambda_23CBB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_23CBB)
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
            "#12P#1005Fなんだ、まだ例の先生からの\x01",
            "連絡はないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C1201
    ChrTalk(
        0x101,
        (
            "#5P#0006Fええ、何でも調査に熱中して\x01",
            "研究室に閉じこもっているみたいで。\x02\x03",

            "#0000Fこうなったら直接、\x01",
            "出向いた方がいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C1202
    ChrTalk(
        0x8,
        (
            "#12P#1003Fふむ、そうかもしれんな。\x02\x03",

            "#1000F被害者が出ている以上、\x01",
            "薬の成分は確かめておきたい所だ。\x02\x03",

            "ギルドからの連絡は任せて\x01",
            "急いで行ってくるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C1203
    ChrTalk(
        0x102,
        (
            "#0100F#5Pすみません。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C1204
    ChrTalk(
        0x104,
        (
            "#6P#0300Fそんじゃ、とっととバスで\x01",
            "ウルスラ病院まで行くとすっか。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2404B")
    OP_29(0x2B, 0x4, 0x40)

    label("loc_2404B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2405D")
    OP_29(0x2F, 0x4, 0x40)

    label("loc_2405D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x33, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2406F")
    OP_29(0x33, 0x4, 0x40)

    label("loc_2406F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2408D")
    OP_29(0x28, 0x4, 0x40)
    Jump("loc_2409F")

    label("loc_2408D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2409F")
    OP_29(0x28, 0x4, 0x40)

    label("loc_2409F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_240BD")
    OP_29(0x2E, 0x4, 0x40)
    Jump("loc_240CF")

    label("loc_240BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240CF")
    OP_29(0x2E, 0x4, 0x40)

    label("loc_240CF")

    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_50_23718 end

    def Function_51_240D5(): pass

    label("Function_51_240D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2416B")
    EventBegin(0x1)

    #C1205
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
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Jump("loc_2421C")

    label("loc_2416B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2421C")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C1206
    ChrTalk(
        0x8,
        (
            "#1000Fおっと、どこに行くつもりだ？\x02\x03",

            "とっとと支援要請を確認しろ。\x01",
            "この端末を調べれば\x01",
            "情報が引き出せるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_2421C")

    Return()

    # Function_51_240D5 end

    def Function_52_2421D(): pass

    label("Function_52_2421D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_242CE")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C1207
    ChrTalk(
        0x8,
        (
            "#1000Fおっと、どこに行くつもりだ？\x02\x03",

            "とっとと支援要請を確認しろ。\x01",
            "この端末を調べれば\x01",
            "情報が引き出せるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_242CE")

    Return()

    # Function_52_2421D end

    def Function_53_242CF(): pass

    label("Function_53_242CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24380")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C1208
    ChrTalk(
        0x8,
        (
            "#1000Fおっと、どこに行くつもりだ？\x02\x03",

            "とっとと支援要請を確認しろ。\x01",
            "この端末を調べれば\x01",
            "情報が引き出せるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_24380")

    Return()

    # Function_53_242CF end

    def Function_54_24381(): pass

    label("Function_54_24381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24415")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C1209
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……\x02\x03",

            "仔猫をつれたままだしな。\x01",
            "遠くへ行くのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    label("loc_24415")

    Return()

    # Function_54_24381 end

    def Function_55_24416(): pass

    label("Function_55_24416")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24486")

    #C1210
    ChrTalk(
        0x101,
        (
            "#0000F……こっちは裏口だな。\x02\x03",

            "キーアをギルドに連れて行くんだし\x01",
            "１階の玄関から出よう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2490D")

    label("loc_24486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24598")

    #C1211
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……先に\x01",
            "オーバルストアに寄ってみよう。\x02\x03",

            "#0000F中央広場の角の建物のはずだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2452E")

    #C1212
    ChrTalk(
        0x103,
        "#0200F了解です、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24593")

    label("loc_2452E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24561")

    #C1213
    ChrTalk(
        0x104,
        "#0300F了解、行ってみるか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24593")

    label("loc_24561")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24593")

    #C1214
    ChrTalk(
        0x102,
        "#0100Fええ、行ってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_24593")

    Jump("loc_2490D")

    label("loc_24598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2490D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2484B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2463A")

    #C1215
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……こっちは\x01",
            "裏口みたいだな。\x02\x03",

            "街の案内をするんだから\x01",
            "１階の玄関から出よう。\x01",
            "正面が中央広場のはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24843")

    label("loc_2463A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_246E0")

    #C1216
    ChrTalk(
        0x102,
        "#0100Fあら……こっちは裏口みたいね。\x02",
    )

    CloseMessageWindow()

    #C1217
    ChrTalk(
        0x101,
        (
            "#0000F悪い、１階の玄関から出てくれ。\x01",
            "その方が街を案内しやすいしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C1218
    ChrTalk(
        0x102,
        "#0100F了解、１階の玄関ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24843")

    label("loc_246E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24795")

    #C1219
    ChrTalk(
        0x103,
        "#0200Fあ……こちらは裏口のようですね。\x02",
    )

    CloseMessageWindow()

    #C1220
    ChrTalk(
        0x101,
        (
            "#0000F悪い、１階の玄関から出てくれ。\x01",
            "その方が街を案内しやすいしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C1221
    ChrTalk(
        0x103,
        (
            "#0200Fわかりました。\x01",
            "１階の玄関ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24843")

    label("loc_24795")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24843")

    #C1222
    ChrTalk(
        0x104,
        "#0300Fっと、こっちは裏口みてえだな。\x02",
    )

    CloseMessageWindow()

    #C1223
    ChrTalk(
        0x101,
        (
            "#0000F悪い、１階の玄関から出てくれ。\x01",
            "その方が街を案内しやすいしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C1224
    ChrTalk(
        0x104,
        (
            "#0300FＯＫ、リーダー。\x01",
            "１階の玄関だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24843")

    SetScenarioFlags(0x1, 3)
    Jump("loc_2490D")

    label("loc_2484B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_248B1")

    #C1225
    ChrTalk(
        0x101,
        (
            "#0000F１階の玄関から出れば\x01",
            "正面が中央広場のはずだ。\x02\x03",

            "みんなを案内しないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2490D")

    label("loc_248B1")


    #C1226
    ChrTalk(
        0x101,
        (
            "#0000F１階の玄関から出れば\x01",
            "正面が中央広場のはずだ。\x02\x03",

            "案内するから\x01",
            "そっちに回ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2490D")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_24416 end

    def Function_56_24924(): pass

    label("Function_56_24924")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_24970")
    SetChrName("")

    #A1227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ここは空き部屋だ。\x01",
            "普段は鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AC0")

    label("loc_24970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A8B")
    SetChrName("")

    #A1228
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

    #C1229
    ChrTalk(
        0x101,
        "#0000Fここは空き部屋なんだよな。\x02",
    )

    CloseMessageWindow()

    #C1230
    ChrTalk(
        0x102,
        (
            "#0100Fこのビルって古いけど\x01",
            "部屋数だけは多いわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C1231
    ChrTalk(
        0x101,
        (
            "#0000F何年か前までは\x01",
            "クロスベルタイムズが\x01",
            "入っていたはずだし。\x02\x03",

            "#0003F普段は鍵を掛けてあるけど……\x01",
            "休みの日には掃除くらいしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 5)
    Jump("loc_24AC0")

    label("loc_24A8B")

    SetChrName("")

    #A1232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ここは空き部屋だ。\x01",
            "普段は鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AC0")

    TalkEnd(0xFF)
    Return()

    # Function_56_24924 end

    def Function_57_24AC4(): pass

    label("Function_57_24AC4")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B4B")
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

    label("loc_24B4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B67")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_24B67")

    Return()

    # Function_57_24AC4 end

    def Function_58_24B69(): pass

    label("Function_58_24B69")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24BF0")
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

    label("loc_24BF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C0C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_24C0C")

    Return()

    # Function_58_24B69 end

    def Function_59_24C0E(): pass

    label("Function_59_24C0E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C95")
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

    label("loc_24C95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24CB1")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_24CB1")

    Return()

    # Function_59_24C0E end

    def Function_60_24CB3(): pass

    label("Function_60_24CB3")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D3A")
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

    label("loc_24D3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24D56")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_24D56")

    Return()

    # Function_60_24CB3 end

    SaveToFile()

Try(main)
