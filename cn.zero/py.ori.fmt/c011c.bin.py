from ZeroScenarioHelper import *

def main():
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
        "赛尔盖科长",             # 1
        "赛尔盖科长",             # 2
        "蔡特",                   # 3
        "柯贝",                   # 4
        "比利",                   # 5
        "柯林",                   # 6
        "哈罗德",                 # 7
        "索菲亚",                 # 8
        "艾丝蒂尔",               # 9
        "约修亚",                 # 10
        "蔡特",                   # 11
        "餐具",                   # 12
        "餐具",                   # 13
        "餐具",                   # 14
        "餐具",                   # 15
        "餐具",                   # 16
        "餐具",                   # 17
        "餐具",                   # 18
        "餐具",                   # 19
        "餐具",                   # 20
        "餐具",                   # 21
        "伊斯",                   # 22
        "金色蔷薇卡片",           # 23
        "诺邦",                   # 24
        "SE控制",                 # 25
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
        "Function_4_F9E",          # 04, 4
        "Function_5_FA2",          # 05, 5
        "Function_6_11F9",         # 06, 6
        "Function_7_1220",         # 07, 7
        "Function_8_12AE",         # 08, 8
        "Function_9_1857",         # 09, 9
        "Function_10_2615",        # 0A, 10
        "Function_11_2634",        # 0B, 11
        "Function_12_3FBD",        # 0C, 12
        "Function_13_48A6",        # 0D, 13
        "Function_14_5528",        # 0E, 14
        "Function_15_55B5",        # 0F, 15
        "Function_16_5F42",        # 10, 16
        "Function_17_5F5D",        # 11, 17
        "Function_18_6286",        # 12, 18
        "Function_19_7A76",        # 13, 19
        "Function_20_7A91",        # 14, 20
        "Function_21_7ABA",        # 15, 21
        "Function_22_A8F4",        # 16, 22
        "Function_23_A949",        # 17, 23
        "Function_24_A99B",        # 18, 24
        "Function_25_D1EC",        # 19, 25
        "Function_26_D206",        # 1A, 26
        "Function_27_D221",        # 1B, 27
        "Function_28_D276",        # 1C, 28
        "Function_29_D2CB",        # 1D, 29
        "Function_30_D320",        # 1E, 30
        "Function_31_D375",        # 1F, 31
        "Function_32_D3F1",        # 20, 32
        "Function_33_E2EE",        # 21, 33
        "Function_34_E309",        # 22, 34
        "Function_35_E324",        # 23, 35
        "Function_36_E359",        # 24, 36
        "Function_37_E73F",        # 25, 37
        "Function_38_E76A",        # 26, 38
        "Function_39_E783",        # 27, 39
        "Function_40_EE1F",        # 28, 40
        "Function_41_F4B0",        # 29, 41
        "Function_42_F701",        # 2A, 42
        "Function_43_F795",        # 2B, 43
        "Function_44_F7E3",        # 2C, 44
        "Function_45_F8E8",        # 2D, 45
        "Function_46_F90C",        # 2E, 46
        "Function_47_F90D",        # 2F, 47
        "Function_48_FACE",        # 30, 48
        "Function_49_FC8F",        # 31, 49
        "Function_50_FE4E",        # 32, 50
        "Function_51_10018",       # 33, 51
        "Function_52_101D3",       # 34, 52
        "Function_53_1038E",       # 35, 53
        "Function_54_10549",       # 36, 54
        "Function_55_1070F",       # 37, 55
        "Function_56_10762",       # 38, 56
        "Function_57_10807",       # 39, 57
        "Function_58_1093E",       # 3A, 58
        "Function_59_109DF",       # 3B, 59
        "Function_60_10A82",       # 3C, 60
        "Function_61_10B25",       # 3D, 61
        "Function_62_10BC8",       # 3E, 62
        "Function_63_10C71",       # 3F, 63
        "Function_64_10D14",       # 40, 64
        "Function_65_10D4D",       # 41, 65
        "Function_66_10DEC",       # 42, 66
        "Function_67_10E8B",       # 43, 67
        "Function_68_10F2A",       # 44, 68
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('竞赛旗', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A5")
    Event(0, 47)

    label("loc_9A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小径自行车', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D6")
    Event(0, 48)

    label("loc_9D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('安乐椅', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A07")
    Event(0, 49)

    label("loc_A07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你水族馆', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38")
    Event(0, 50)

    label("loc_A38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('古怪靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A69")
    Event(0, 51)

    label("loc_A69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('波波靠垫', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9A")
    Event(0, 52)

    label("loc_A9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑泰迪熊', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACB")
    Event(0, 53)

    label("loc_ACB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦番茄人玩偶', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFC")
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
            "留言板上有留言。\x07\x00\x02",
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
            "『我去出席总部的会议。\x01",
            "  到时候就回来，你们先去工作吧。\x01",
            "                    　　赛尔盖』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_EFF end

    def Function_4_F9E(): pass

    label("Function_4_F9E")

    Call(0, 5)
    Return()

    # Function_4_F9E end

    def Function_5_FA2(): pass

    label("Function_5_FA2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1036")
    Jump("loc_1080")

    label("loc_1036")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1056")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1080")

    label("loc_1056")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1076")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1080")

    label("loc_1076")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1080")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118E")

    #C0003
    ChrTalk(
        0x9,
        (
            "#1000F在纪念庆典期间，\x01",
            "支援请求也会接连不断地\x01",
            "发过来吧。\x02\x03",

            "到最终日为止的四天内，\x01",
            "就专心完成支援请求吧。\x02\x03",

            "#1003F我大概也会时不时地\x01",
            "去支援下总部那边……\x01",
            "不过，你们不用管我，做好自己的工作就是。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#0000F明白。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F1")

    label("loc_118E")


    #C0005
    ChrTalk(
        0x9,
        (
            "#1000F在纪念庆典期间，\x01",
            "支援请求也会接连不断地\x01",
            "发过来吧。\x02\x03",

            "你们不用管我，\x01",
            "专心完成支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F1")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_5_FA2 end

    def Function_6_11F9(): pass

    label("Function_6_11F9")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xA,
        "#1200F…………………………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_11F9 end

    def Function_7_1220(): pass

    label("Function_7_1220")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1296")

    #C0007
    ChrTalk(
        0xB,
        "喵～～呜……⊥\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#0005F咦……？\x01",
            "饵食都放在外面，\x01",
            "没收进去吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_12AA")

    label("loc_1296")


    #C0009
    ChrTalk(
        0xB,
        "喵～～呜……⊥\x02",
    )

    CloseMessageWindow()

    label("loc_12AA")

    TalkEnd(0xFE)
    Return()

    # Function_7_1220 end

    def Function_8_12AE(): pass

    label("Function_8_12AE")

    TalkBegin(0xFF)
    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_182D")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_12F7"),
        (1, "loc_14A3"),
        (SWITCH_DEFAULT, "loc_1828"),
    )


    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131E")
    OP_2B(0x34, 0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_149E")

    label("loc_131E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_133F")
    OP_2B(0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_149E")

    label("loc_133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_135A")
    OP_2B(0x2D, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_149E")

    label("loc_135A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1371")
    OP_2B(0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_149E")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_138A")
    OP_2B(0x28, 0x29, 0x2A, 0x2F, 0xFFFF)
    Jump("loc_149E")

    label("loc_138A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_139D")
    OP_2B(0x25, 0xFFFF)
    Jump("loc_149E")

    label("loc_139D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_13BC")
    OP_2B(0x22, 0x23, 0x18, 0x1A, 0x1C, 0x1E, 0x21, 0xFFFF)
    Jump("loc_149E")

    label("loc_13BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_13DB")
    OP_2B(0x1F, 0x20, 0x21, 0x18, 0x1A, 0x1C, 0x1E, 0xFFFF)
    Jump("loc_149E")

    label("loc_13DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13F8")
    OP_2B(0x1B, 0x1C, 0x1D, 0x1E, 0x18, 0x1A, 0xFFFF)
    Jump("loc_149E")

    label("loc_13F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1413")
    OP_2B(0x16, 0x17, 0x18, 0x19, 0x1A, 0xFFFF)
    Jump("loc_149E")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1430")
    OP_2B(0x11, 0x12, 0x13, 0x14, 0xE, 0x10, 0xFFFF)
    Jump("loc_149E")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1449")
    OP_2B(0xD, 0xE, 0xF, 0x10, 0xFFFF)
    Jump("loc_149E")

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1466")
    OP_2B(0x9, 0xA, 0xB, 0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_149E")

    label("loc_1466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_147D")
    OP_2B(0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_149E")

    label("loc_147D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1499")
    OP_2B(0x1, 0x35, 0x2, 0x3, 0xFFFF)
    Jump("loc_149E")

    label("loc_1499")

    OP_2B(0x1, 0xFFFF)

    label("loc_149E")

    Jump("loc_1828")

    label("loc_14A3")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("接待小姐芙兰")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14FF")
    Sound(2062, 255, 100, 0)    #voice#Fran

    #A0010
    AnonymousTalk(
        0xFF,
        "#28A您好，这里是克洛斯贝尔警察局～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_151D")

    label("loc_14FF")

    Sound(2061, 255, 100, 0)    #voice#Fran

    #A0011
    AnonymousTalk(
        0xFF,
        "#26A各位，真是辛苦了～\x02",
    )

    CloseMessageWindow()

    label("loc_151D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_174A")
    Sound(2067, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0012
    AnonymousTalk(
        0xFF,
        "#27A那么，我将对各位的报告进行处理～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D7")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_1592"),
        (13, "loc_15DA"),
        (12, "loc_161E"),
        (SWITCH_DEFAULT, "loc_1664"),
    )


    label("loc_1592")

    Sound(2075, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "#36A等级１ｓｔ――\x01",
            "罗伊德警官，实在太厉害了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1664")

    label("loc_15DA")

    Sound(2074, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "#35A等级２ｎｄ──\x01",
            "罗伊德警官，好厉害呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1664")

    label("loc_161E")

    Sound(2073, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            "#32A等级３ｒｄ──\x01",
            "罗伊德警官，做得很好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1664")

    label("loc_1664")

    Sound(2076, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            "#31A奖励物品\x01",
            "也会马上给你们送去的～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)    #voice#Fran

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "#34A大家辛苦了～！\x01",
            "以后也请随时来向我报告～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1742")

    label("loc_16D7")

    Sound(2078, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0018
    AnonymousTalk(
        0xFF,
        "#16A报告就是以上这些吧～\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)    #voice#Fran

    #A0019
    AnonymousTalk(
        0xFF,
        (
            "#37A那么，以后如果完成了新的委托，\x01",
            "请再来向我报告吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1742")

    SetScenarioFlags(0x0, 4)
    Jump("loc_181A")

    label("loc_174A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_17C1")
    Sound(2063, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            "#32A哎……\x01",
            "刚才已经报告过了哦。        \x02",
        )
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)    #voice#Fran

    #A0021
    AnonymousTalk(
        0xFF,
        "#32A等完成了新的委托之后再来报告吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_181A")

    label("loc_17C1")

    Sound(2065, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            "#37A哎，好像并没有可以\x01",
            "报告的委托哦～\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)    #voice#Fran

    #A0023
    AnonymousTalk(
        0xFF,
        "#16A请下次再来报告吧～\x02",
    )

    CloseMessageWindow()

    label("loc_181A")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_1828")

    label("loc_1828")

    Jump("loc_12CA")

    label("loc_182D")

    OP_E3(0x6)
    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1856")
    Call(0, 41)

    label("loc_1856")

    Return()

    # Function_8_12AE end

    def Function_9_1857(): pass

    label("Function_9_1857")

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
            "#1K创立纪念庆典　第三天\x02",
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
            "#6P#0306F呼～哎呀呀，\x01",
            "昨天可真是累死了。\x02\x03",

            "#0302F一想到这样的日子还要过三天，\x01",
            "就不由得烦躁起来了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0026
    ChrTalk(
        0x103,
        (
            "#5P#0200F昨天那件事只是自作自受吧……？\x02\x03",

            "#0204F提议展开那种追逐赛的人\x01",
            "可是兰迪前辈你自己……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    #C0027
    ChrTalk(
        0x104,
        (
            "#6P#0301F事到如今，我已经后悔啦～\x02\x03",

            "#0306F我都一把年纪了，\x01",
            "不该陪着年轻人胡闹的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0102F才刚过二十岁的人，\x01",
            "说什么呢……\x02",
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
        "#0105F罗伊德？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        "#6P#0205F……怎么了？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0032
    ChrTalk(
        0x101,
        (
            "#5P#0005F哦，嗯……\x02\x03",

            "#0012F我有点在意昨天\x01",
            "艾丝蒂尔他们说的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#0101F啊……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#6P#0301F是那个『黑之竞拍会』吧。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#6P#0200F可是，也很有可能\x01",
            "只是传闻而已吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯，话虽如此啦。\x02\x03",

            "#0001F考虑到克洛斯贝尔目前的形势，\x01",
            "总感觉，并非只是\x01",
            "单纯的传闻啊。\x02",
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
            "#6P#0306F的确，连黑手党\x01",
            "都可以在这里横行霸道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0203F不管发生什么事都不足为奇……\x01",
            "或许的确如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0108F……………………………………\x02\x03",

            "#0103F……其实，我以前也听过一个\x01",
            "令人有点在意的传闻。\x02",
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
        "#5P#0005F令人在意的传闻……？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        "#3P#0205F具体来说是……？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#0103F以前和大家说过，\x01",
            "我当年曾经去各国留过学……\x02\x03",

            "就是当时从一位认识的\x01",
            "贵族小姐那里听来的。\x02\x03",

            "#0101F据说，每年在克洛斯贝尔的\x01",
            "某处都会召开一场秘密的社交宴会。\x02",
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
        "#5P#0011F秘密的社交宴会……？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#6P#0302F我说，听上去就很可疑啊。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#0106F似乎是各国的贵族和企业家\x01",
            "暗中齐聚一堂的宴会……\x02\x03",

            "#0108F当时我只觉得\x01",
            "是单纯的传闻……\x02\x03",

            "#0101F不过，你们不觉得有些令人在意吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#5P#0003F的确……\x02\x03",

            "#0001F那很有可能就是\x01",
            "『黑之竞拍会』吗……\x02\x03",

            "#0008F嗯～这样一来，科长\x01",
            "很可能会知道些什么……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0047
    ChrTalk(
        0x103,
        (
            "#6P#0200F不过，科长今天\x01",
            "去了总部那边呢。\x02\x03",

            "说是有推不开的会议。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#5P#0006F是啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    #C0049
    ChrTalk(
        0x104,
        (
            "#6P#0303F不过，就算是真的，\x01",
            "我们也无能为力吧？\x02\x03",

            "#0301F再怎么想，议员们肯定也会下达指示，\x01",
            "让警察局总部装聋作哑的。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#5P#0008F……这倒也是啊。\x02\x03",

            "#0006F嗯～可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#0103F……我明白你的心情。\x02\x03",

            "#0100F总之，在纪念庆典期间\x01",
            "姑且留意一下吧。\x02\x03",

            "说不定能获得什么情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#5P#0003F──是啊。\x02\x03",

            "#0000F好，赶快把饭吃完，\x01",
            "然后去解决今天的支援请求吧。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25BB")
    OP_29(0x17, 0x4, 0x40)
    Jump("loc_25CD")

    label("loc_25BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25CD")
    OP_29(0x17, 0x4, 0x40)

    label("loc_25CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25EB")
    OP_29(0x19, 0x4, 0x40)
    Jump("loc_25FD")

    label("loc_25EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FD")
    OP_29(0x19, 0x4, 0x40)

    label("loc_25FD")

    ModifyEventFlags(1, 0, 0x80)
    ClearScenarioFlags(0x0, 3)
    PlayBGM("ed7106", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_9_1857 end

    def Function_10_2615(): pass

    label("Function_10_2615")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2633")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_10_2615")

    label("loc_2633")

    Return()

    # Function_10_2615 end

    def Function_11_2634(): pass

    label("Function_11_2634")

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
            "#1K创立纪念庆典　最终日\x02",
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
            "#6P#0309F哎呀～！\x01",
            "话说，昨天听到的那些事情可真是不得了啊。\x02\x03",

            "#0300F那两个人，到底经历过\x01",
            "何等惊人的试炼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#0103F关于利贝尔的异变，\x01",
            "我虽然也听过不少传闻……\x02\x03",

            "#0100F不过，真相远比\x01",
            "传闻更加惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#6P#0206F还有那个『结社』……\x02\x03",

            "#0201F凭借最尖端技术，实力甚至\x01",
            "超越了爱普斯泰恩财团和ＺＣＦ，\x01",
            "这些传闻倒是听说过一二……\x02\x03",

            "没想到它真的存在，\x01",
            "而且还有那么大的规模……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯……\x01",
            "老实说，真是很难想象呢。\x02\x03",

            "#0000F不过，据约修亚说，\x01",
            "『结社』的势力基本还没有\x01",
            "扩张到克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#0108F说不定是因为在这里，帝国和共和国的\x01",
            "监视比别处都森严吧。\x02\x03",

            "两国应该都派遣了\x01",
            "很多谍报工作人员进来，\x01",
            "所以结社不想被抓到尾巴……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#5P#0006F……这真是\x01",
            "完全不值得高兴的原因啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#6P#0303F又是神秘结社，又是大国的谍报组织，\x01",
            "再加上巨大的犯罪团伙吗。\x02\x03",

            "#0301F唉，每一个都同样棘手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#6P#0206F……是啊。\x02",
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
        "声音",
        (
            "#5P各位好～！\x01",
            "我是莱姆斯运输公司的！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(800, 1000, 1500, 2000)
    OP_6F(0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sound(103, 0, 100, 0)

    def lambda_2CD5():
        OP_96(0xFE, 0x320, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2CD5)

    def lambda_2CEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2CEF)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xC, 1)

    #C0064
    ChrTalk(
        0x101,
        "#3P#0005F您是……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        "#0105F昨天那个运输公司的……\x02",
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

    def lambda_2E00():
        OP_96(0xFE, 0x12C, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E00)
    Sleep(50)

    def lambda_2E1D():
        OP_96(0xFE, 0x514, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E1D)
    Sleep(50)

    def lambda_2E3A():
        OP_96(0xFE, 0x12C, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2E3A)
    Sleep(50)

    def lambda_2E57():
        OP_96(0xFE, 0x514, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E57)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0066
    ChrTalk(
        0xC,
        "#2P哎呀～昨天可真是辛苦各位了！\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#2P不过，真是太好了！\x01",
            "总算是顺利找到了那个孩子！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        "#2P他的父母一定很担心吧？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#5P#0012F哈哈，那自然。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#5P#0300F你有没有\x01",
            "被公司责骂啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#2P嗯，因为送货迟到了，\x01",
            "还被警备队的人抱怨了一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#2P不过老爸──呃，经理倒是\x01",
            "没怎么责怪我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "#2P嗯，也就挨了一拳头，\x01",
            "叫我以后好好检查车里。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#5P#0102F呵呵……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#5P#0204F嗯，这种程度就了事，\x01",
            "应该算是幸运了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        "#2P哈哈，没错。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "#2P──啊，我可不是来\x01",
            "汇报昨天的事情啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        "#2P是给你们送货来的。\x02",
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
        "#5P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#5P#0105F从警察局总部发来的吗？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#2P不，好像是一大早\x01",
            "送来的一个快件……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        "#2P就是这个，请收下吧。\x02",
    )

    CloseMessageWindow()

    def lambda_3160():
        OP_96(0xFE, 0x12C, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3160)
    WaitChrThread(0xC, 1)

    def lambda_317E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_317E)

    def lambda_318B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_318B)
    Sleep(300)
    SetChrName("")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "收下了一个小包裹。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_31BC():
        OP_96(0xFE, 0x320, 0x0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_31BC)

    #C0084
    ChrTalk(
        0x101,
        "#5P#0005F这是……？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#11P#0100F好像是个很小的东西……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 1)

    #C0086
    ChrTalk(
        0xC,
        "#2P那么，货已经送到了。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xC,
        (
            "#2P还有其它的货要送，\x01",
            "我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3260():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3260)
    Sleep(50)
    OP_93(0x102, 0xB4, 0x1F4)

    #C0088
    ChrTalk(
        0x104,
        "#5P#0300F哦，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#5P#0202F请多加小心，\x01",
            "不要再让走失的孩子钻进车里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        "#2P哈哈，我会铭记在心的！\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    def lambda_32F2():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_32F2)
    Sleep(500)

    def lambda_330F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_330F)
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

    def lambda_336A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_336A)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    #C0092
    ChrTalk(
        0x104,
        "#5P#0305F那么，究竟是谁送来的呢？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#6P#0003F──这里写有寄件人姓名。\x02\x03",

            "#0000F好像是『小猫』寄来的。\x02",
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
        "#0105F#11P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        "#0205F#5P是玲寄来的……\x02",
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
            "罗伊德打开小包裹，\x01",
            "取出了里面的东西。\x02\x03",

            "除了留言卡，\x01",
            "还有一张漆黑的卡片。\x07\x00\x02",
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
            "『──作为昨天的谢礼，\x01",
            "  这张卡送给你们了。』\x02\x03",

            "『听说那里会展出很有趣的商品，\x01",
            "  所以我本打算过去看看。不过，\x01",
            "  就把机会让给大哥哥你们好了。』\x02\x03",

            "『呵呵，要有效利用哦。』\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('纯白之石', 1)
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
        "#11P#0013F『黑之竞拍会』的……！\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#0105F那、那孩子怎么会有\x01",
            "这种东西……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        (
            "#6P#0305F我记得，这是只发给各国ＶＩＰ的\x01",
            "邀请卡吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#6P#0206F而且……\x02\x03",

            "#0201F她怎么会知道\x01",
            "我们对这件事\x01",
            "有兴趣呢……？\x02",
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
            "#5P#0003F──关于那孩子的事，\x01",
            "想太多似乎也无济于事。\x02\x03",

            "#0001F话说回来……\x01",
            "你们觉得这张卡是真品吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0108F这个……\x02\x03",

            "#0101F从这种高档的制作工艺来看，\x01",
            "我觉得是真品的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#6P#0201F金色蔷薇的刻印……\x01",
            "用的是真正的金箔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#0301F今晚七时，于疗养地米修拉姆的\x01",
            "哈尔特曼议长宅邸举行啊。\x02",
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
            "#5P#0006F──那个，各位。\x02\x03",

            "#0008F虽然科长在不久前\x01",
            "还那么郑重地叮嘱过我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        "#0100F不用说了，罗伊德，我们都懂的。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#6P#0309F嗯，这就是所谓的，\x01",
            "有便宜不占就是那个什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#6P#0202F……幸好科长今天\x01",
            "也去了总部。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#5P#0001F大家……这样好吗？\x02\x03",

            "总是勉强大家\x01",
            "迁就我的任性……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#0104F呵呵，你可别误会哦。\x02\x03",

            "#0108F从某种意义上来说，\x01",
            "我对『黑之竞拍会』的兴趣可是比你还大……\x02\x03",

            "#0101F因为，这个宴会上的人，\x01",
            "距离我所在的世界很近啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#6P#0204F我则是纯粹\x01",
            "对竞拍会感到好奇。\x02\x03",

            "玲所说的\x01",
            "『有趣的商品』\x01",
            "也很令人在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#6P#0309F哈，我是对豪华的\x01",
            "上流社会晚宴本身很有兴趣呢。\x02\x03",

            "#0304F可以尽情享用美食美酒，\x01",
            "而且还有机会接近上流社会那些\x01",
            "高贵的大小姐们……\x02\x03",

            "#0302F怎么可能错过呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        "#5P#0002F……各位……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0116
    ChrTalk(
        0x101,
        (
            "#5P#0003F──今天就是最终日了。\x02\x03",

            "#0001F中午之前，把其它工作都处理完，\x01",
            "然后就去港湾区的水上巴士渡口吧。\x02\x03",

            "而是否真的要潜入竞拍会……\x01",
            "等去了『米修拉姆』之后再考虑吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#0100F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        (
            "#6P#0300F那么，就赶快把\x01",
            "剩下的工作解决掉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#6P#0204F还是先去终端\x01",
            "确认一下有没有新委托吧。\x02",
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

    # Function_11_2634 end

    def Function_12_3FBD(): pass

    label("Function_12_3FBD")

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
        "#2S#60W……伊德……\x02",
    )

    CloseMessageWindow()

    #A0121
    AnonymousTalk(
        0xFF,
        "#2S#50W………罗伊德……真是的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0122
    AnonymousTalk(
        0x101,
        "#5206F#40W嗯～……\x02",
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
            "……好啦，快起床。\x01",
            "已经到开会时间了哦。\x02",
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

    def lambda_41C9():
        OP_96(0xFE, 0x2BC, 0x1E, 0x1E974, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41C9)

    #C0125
    ChrTalk(
        0x102,
        "#6P#0105F#8A呀……\x02",
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
            "#11P#5205F啊……\x02\x03",

            "……早上好，艾莉，\x01",
            "你怎么在这里……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4261():
        OP_96(0xFE, 0x3E8, 0x1E, 0x1E974, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4261)
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
            "因为你一直没起来，\x01",
            "所以我来看看情况。\x02\x03",

            "看来，你一定是昨晚想得太多，\x01",
            "所以睡不着吧？\x02",
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
            "#11P#5212F哈哈……都被你看穿了吗。\x02\x03",

            "#5200F艾莉你……好像没受什么影响啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#6P#0104F如果遇到这种程度的事情就消沉，\x01",
            "烦恼可就没完没了啦。\x02\x03",

            "#0108F而且……我可能\x01",
            "早就隐约察觉到了。\x02\x03",

            "在克洛斯贝尔举办的\x01",
            "所谓『秘密社交宴会』\x01",
            "可能另有黑幕……\x02\x03",

            "#0106F但是，我之前或许只是在自欺欺人，\x01",
            "装作没察觉的样子罢了。\x02\x03",

            "因为不想再经历会让自己沮丧\x01",
            "或是悔恨的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#11P#5201F艾莉……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#6P#0102F所以现在，我决定坦然接受\x01",
            "这种悔恨和沮丧。\x02\x03",

            "不是因为科长的话……\x01",
            "而是因为我觉得这会成为我的动力。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#11P#5204F是吗……\x02",
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
        "#11P#5200F──好！\x02",
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

    def lambda_4609():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4609)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0134
    ChrTalk(
        0x101,
        (
            "#5204F#5P既然连艾莉都这么\x01",
            "努力地调整心态了，\x01",
            "我也不能再优柔寡断了。\x02\x03",

            "#5200F我这就去换衣服，\x01",
            "你先在一楼等我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#12P#0102F嗯，好。\x02\x03",

            "#0109F早餐也准备好了，\x01",
            "边吃边开会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#5202F#5P嗯，谢了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    OP_68(2000, 700, 124000, 2000)

    def lambda_4705():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4705)
    WaitChrThread(0x102, 1)

    def lambda_4723():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4723)

    def lambda_473D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_473D)
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
            "#5202F#5P（艾莉……和之前谈心时比起来，\x01",
            "  似乎已经没有那么多迷惘了。）\x02\x03",

            "#5204F（嗯，我也不能输给她呢。）\x02",
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
            "#2P#5200F纪念庆典也到了第四天……\x02\x03",

            "看来今天也会很忙呢。\x02",
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

    # Function_12_3FBD end

    def Function_13_48A6(): pass

    label("Function_13_48A6")

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
        "#2S#60W…………………（摇摇）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0140
    AnonymousTalk(
        0x101,
        "#5206F#40W……嗯…………\x02",
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
            "（摇摇，摇摇，摇摇）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0142
    AnonymousTalk(
        0x101,
        (
            "#5208F#30W（……怎么了……地震？）\x02\x03",

            "（可是，地震的话……\x01",
            "  好像不会这么舒服……）\x02\x03",

            "#5203F（不行了……还是很困……）\x02",
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
        "#2S……输出功率最低，极小档。\x02",
    )

    CloseMessageWindow()
    SetChrName("？？？")

    #A0145
    AnonymousTalk(
        0xFF,
        "#2S冻结程序开启───发动。\x02",
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
        "#5211F#4S好冷！？\x02",
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
        "#11P#5205F哎……\x02",
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
            "……早上好。\x01",
            "罗伊德前辈。\x02",
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
            "#11P#5202F嗯，早上好……\x02\x03",

            "#5205F咦……\x01",
            "缇欧怎么会在这里……？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#6P#0203F开会时间到了，\x01",
            "可是罗伊德前辈一直没下来，\x01",
            "所以我来叫醒你。\x02",
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
            "#11P#5205F啊……\x01",
            "都已经这么晚了吗。\x02\x03",

            "#5206F不过，好奇怪啊……\x02\x03",

            "我感觉有什么冰凉的东西\x01",
            "打在我的脖子上，\x01",
            "难道是做梦吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#6P#0203F不，不是做梦。\x02\x03",

            "#0200F因为我怎么摇晃，你都不醒，\x01",
            "就尝试释放了极小功率的\x01",
            "钻石星尘。\x02",
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
            "#11P#5211F──等一下。\x02\x03",

            "我好像听到了什么\x01",
            "难以忽略的词语……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        (
            "#6P#0204F……没问题。\x01",
            "因为我把功率设置到最低了。\x02\x03",

            "#0202F是不是完全清醒了？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#11P#5212F这个……倒是没错。\x02",
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
            "#6P#0208F而且，要如何叫醒熟睡的人，\x01",
            "这个问题令我十分迷惑……\x02\x03",

            "#0206F所以就不由得选择了\x01",
            "最有效的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        "#11P#5205F如何叫醒熟睡的人……\x02",
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
            "#11P#5208F（……是吗……）\x02\x03",

            "（这孩子以前连叫别人起床\x01",
            "  的经验都没有……）\x02",
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
            "#6P#0205F……罗伊德前辈？\x02\x03",

            "#0206F那个，你生气了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#11P#5204F不……怎么会生气呢。\x02\x03",

            "#5202F不过，以后你再叫我的时候，\x01",
            "不要光是摇晃，\x01",
            "出声叫我就好了。\x02\x03",

            "这样我一定会醒来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        (
            "#6P#0202F……原来如此。\x02\x03",

            "#0204F──那样的话，\x01",
            "只要叫『早上好，主人⊥』\x01",
            "就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#11P#5201F……为什么会是这种叫法～？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#6P#0211F那么，『哥哥，再不起来的话，\x01",
            "我就要踢你了哦！』──这样？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0164
    ChrTalk(
        0x101,
        "#11P#5207F你这些都是从哪里学来的啊！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#6P#0204F开玩笑的。\x02\x03",

            "#0202F艾莉前辈准备了早餐，\x01",
            "换好衣服就请下楼来吧。\x02\x03",

            "那么，我就先……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x190)

    #C0166
    ChrTalk(
        0x101,
        "#11P#5205F啊，稍等一下。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x5A, 0x1F4)

    #C0167
    ChrTalk(
        0x103,
        "#6P#0205F……什么事呢？\x02",
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

    def lambda_533A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_533A)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0168
    ChrTalk(
        0x101,
        (
            "#5204F#5P──谢谢你了，缇欧。\x02\x03",

            "#5202F你是关心我，\x01",
            "才过来看看情况的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        "#12P#0205F哎……！？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(1800)

    #C0170
    ChrTalk(
        0x101,
        "#5205F#5P#N啊……\x02",
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
            "#5204F#5P哈哈……\x01",
            "不知为何，感觉昨天的烦恼\x01",
            "全都烟消云散了。\x02\x03",

            "#5202F……要感谢缇欧才是啊。\x02",
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
            "#2P#5200F纪念庆典也到了第四天……\x02\x03",

            "看来今天也会很忙呢。\x02",
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

    # Function_13_48A6 end

    def Function_14_5528(): pass

    label("Function_14_5528")

    OP_93(0x103, 0xB4, 0x2BC)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_68(2000, 700, 124000, 1500)

    def lambda_5557():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5557)
    WaitChrThread(0x103, 1)
    OP_64(0x103)
    Sound(103, 0, 100, 0)

    def lambda_557E():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_557E)

    def lambda_5598():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5598)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Return()

    # Function_14_5528 end

    def Function_15_55B5(): pass

    label("Function_15_55B5")

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
        "#2S#60W……喂～……快起床啊。\x02",
    )

    CloseMessageWindow()

    #A0174
    AnonymousTalk(
        0xFF,
        (
            "#2S#50W不要一直\x01",
            "呼呼大睡个没完啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0175
    AnonymousTalk(
        0x101,
        "#5206F#40W……嗯…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("？？？")

    #A0176
    AnonymousTalk(
        0xFF,
        "#2S#30W唉，真拿你没办法啊。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(1377, 255, 90, 0)    #voice#Randy
    Sleep(2000)

    #A0177
    AnonymousTalk(
        0x101,
        "#5205F啊……\x02",
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
        "#11P#5205F咦……\x02",
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
            "话说回来，我为什么非得\x01",
            "过来叫男人起床不可啊～！\x02\x03",

            "被漂亮姐姐\x01",
            "在早晨温柔地叫醒，\x01",
            "才是本大爷的风格啊～\x02\x03",

            "然后再泡杯咖啡，\x01",
            "悠闲享受两人世界……\x02\x03",

            "不不，还是直接就这样\x01",
            "做点什么呢？\x02",
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
            "#11P#5206F……抱歉。\x01",
            "我的脑子还没有灵活到\x01",
            "可以陪你想入非非……\x02\x03",

            "#5205F呃……\x01",
            "已经到开会时间了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x104,
        (
            "#6P#0304F嗯，早就到了。\x02\x03",

            "#0300F大小姐和阿缇\x01",
            "给我们做了早饭，\x01",
            "赶快去吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#11P#5200F是吗……\x01",
            "我马上换衣服。\x02\x03",

            "#5209F……哈哈……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0183
    ChrTalk(
        0x104,
        "#6P#0305F……怎么啦？\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#11P#5204F只是觉得兰迪有些帅气啊。\x02\x03",

            "#5202F像这种关心人的方式，\x01",
            "我可是怎么也都学不会呢。\x02",
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
            "#6P#0301F笨、笨蛋，你小子……\x01",
            "说什么肉麻的话呢！\x02\x03",

            "#0303F我可没兴趣安慰\x01",
            "消沉的男人啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#11P#5214F哈哈，我可没提到安慰不安慰哦，你自己承认了呢。\x02\x03",

            "#5204F──没问题。\x01",
            "睡了一晚上，好像镇定下来了。\x02\x03",

            "#5200F虽然还是有点懊悔的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x104,
        "#6P#0302F……是吗。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(3420, 700, 126420, 1500)
    SetChrFlags(0x104, 0x40)

    def lambda_5BEA():
        OP_96(0xFE, 0x578, 0x1E, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BEA)
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
            "#6P#0309F──嗯，尽管去悔恨吧，青少年。\x02\x03",

            "只有经历过这种挫折，\x01",
            "才能成长为真正的男子汉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#11P#5211F都说过不要把我\x01",
            "当小孩子看待了……\x02\x03",

            "#5213F我马上就换衣服，\x01",
            "你先下去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        "#6P#0300F好好。\x02",
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

    def lambda_5D85():
        OP_96(0xFE, 0x3E8, 0x1E, 0x1EB68, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D85)
    WaitChrThread(0x104, 1)
    Sleep(300)
    ClearChrFlags(0x104, 0x40)
    OP_93(0x104, 0xB4, 0x1F4)
    OP_68(2000, 700, 124000, 2000)

    def lambda_5DC3():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DC3)
    WaitChrThread(0x104, 1)
    Sound(103, 0, 100, 0)

    def lambda_5DE7():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DE7)

    def lambda_5E01():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E01)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)

    #C0191
    ChrTalk(
        0x101,
        "#5204F#5P#N那么……\x02",
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
            "#2P#5200F纪念庆典也到了第四天……\x02\x03",

            "看来今天也会很忙呢。\x02",
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

    # Function_15_55B5 end

    def Function_16_5F42(): pass

    label("Function_16_5F42")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F5C")
    OP_A1(0xFE, 0x3E8, 0x4, 0x7, 0x8, 0x9, 0x8)
    Jump("Function_16_5F42")

    label("loc_5F5C")

    Return()

    # Function_16_5F42 end

    def Function_17_5F5D(): pass

    label("Function_17_5F5D")

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
            "#1K创立纪念庆典　第四天\x02",
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
            "#6P#0004F──好了，\x01",
            "开始处理第四天的公务吧。\x02\x03",

            "#0000F保险起见，得先确认一下\x01",
            "有没有收到新的请求才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x102,
        (
            "#0102F是呀。\x02\x03",

            "#0104F市内今天会有游行活动，\x01",
            "另外，应该也会有一些游客\x01",
            "前去郊外观光……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        (
            "#0202F寻找遗失物品和迷路走失的游客……\x01",
            "类似的委托似乎都很可能出现呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        (
            "#5P#0306F嗯，老实说，像这些事情，\x01",
            "也没可能全部照顾到。\x02\x03",

            "#0300F就在我们力所能及的范围之内\x01",
            "尽量提供协助就好了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#6P#0000F嗯，说得也是。\x02",
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

    # Function_17_5F5D end

    def Function_18_6286(): pass

    label("Function_18_6286")

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

    def lambda_63F5():
        OP_96(0xFE, 0x514, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63F5)

    def lambda_640F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_640F)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0199
    ChrTalk(
        0x101,
        "#6P#0005F啊……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(16100, 1850, 10000, 3000)
    SetCameraDistance(24000, 3000)

    def lambda_647E():
        OP_96(0xFE, 0x364C, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_647E)
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
            "#6P#0001F……莫非你是在\x01",
            "通过导力网络\x01",
            "搜索车辆的情报？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x160,
        (
            "#3303F#5P嗯，是啊。\x02\x03",

            "一小时前至现在，\x01",
            "曾经停泊在港湾区东南部的\x01",
            "所有可疑车辆……\x02\x03",

            "正在通过链接克洛斯贝尔的所有\x01",
            "网络终端进行检索。\x02\x03",

            "#3300FＩＢＣ的主终端\x01",
            "和小雀斑的数据库\x01",
            "也让我利用一下吧。\x02",
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
            "#6P#0006F你……到底是什么人呢？\x02\x03",

            "#0001F著名人偶师的孙女……\x01",
            "似乎并不是这么简单吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x160,
        (
            "#3304F#5P呵呵……爷爷只是\x01",
            "玲的协助者而已。\x02\x03",

            "会帮忙修好『爸爸和妈妈』，\x01",
            "是玲的同伴之一……\x02\x03",

            "#3302F『博士』不太值得信任，\x01",
            "所以就秘密拜托他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#6P#0011F博、博士……？\x02\x03",

            "#0001F还有，『爸爸和妈妈』是……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x160,
        (
            "#3304F#5P呵呵，大哥哥没有必要知道哦。\x02\x03",

            "在克洛斯贝尔，\x01",
            "玲只不过是个观察者而已。\x02\x03",

            "#3302F名为『小猫』的观察者。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x101,
        "#6P#0003F……果然是你吗。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x160,
        (
            "#3309F#5P呵呵，昨天的追踪游戏\x01",
            "惊险刺激，让我紧张得心怦怦跳呢。\x02\x03",

            "小雀斑干得还算不错，\x01",
            "那位姐姐似乎也相当有一手哦～\x02\x03",

            "#3302F呵呵，虽然好像用了\x01",
            "一点有趣的小伎俩。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        "#6P#0005F竟然连那个都能看得出来吗……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_68A2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68A2)
    OP_68(900, 1000, 3000, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1500)

    def lambda_68CC():
        OP_96(0xFE, 0x384, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68CC)

    def lambda_68E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_68E6)
    Sleep(450)

    def lambda_68FA():
        OP_96(0xFE, 0x640, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68FA)

    def lambda_6914():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6914)
    Sleep(450)

    def lambda_6928():
        OP_96(0xFE, 0xC8, 0x0, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6928)

    def lambda_6942():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6942)
    WaitChrThread(0x102, 1)

    def lambda_6957():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6957)
    WaitChrThread(0x104, 1)

    def lambda_6968():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6968)
    WaitChrThread(0x103, 1)

    def lambda_6979():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6979)
    WaitChrThread(0x103, 2)
    OP_6F(0x11)

    #C0210
    ChrTalk(
        0x102,
        (
            "#0105F#6P我们回来了，罗伊德。\x01",
            "按照你说的，返回支援科了……\x02",
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
        "#0105F#6P哎呀……？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#0205F#6P这孩子是……\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x104,
        (
            "#0305F#12P好像是……\x01",
            "人偶工房的那个女孩……是人偶师的孙女吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯……\x01",
            "之前发生了点事，所以就带她回来了。\x02",
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

    def lambda_6B35():
        OP_96(0xFE, 0x30D4, 0x352, 0x2648, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B35)
    Sleep(50)

    def lambda_6B52():
        OP_96(0xFE, 0x30D4, 0x352, 0x2A30, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B52)
    Sleep(50)

    def lambda_6B6F():
        OP_96(0xFE, 0x2C24, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B6F)
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
        "#5P#3301F──找到了。\x02",
    )

    CloseMessageWindow()

    def lambda_6BD6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BD6)
    Sleep(500)

    #C0216
    ChrTalk(
        0x160,
        (
            "#5P#3308F『莱姆斯运输公司』的搬运车\x01",
            "好像在半小时之前停在那里。\x02\x03",

            "下一个送货点是贝尔加德门……\x02\x03",

            "#3304F搬运车的通讯号码是……\x01",
            "嗯，这样应该就行了。\x02",
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
            "#11P#3300F请联络那个通讯号码试试。\x02\x03",

            "应该能查出那孩子的去向。\x02",
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
        "#6P#0004F……干得漂亮。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        "#6P#0108F那个……这是怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x104,
        (
            "#6P#0306F从刚才开始，就完全\x01",
            "跟不上你们的步调……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#0203F#5P──原来如此。\x02\x03",

            "#0201F你就是『小猫』吧。\x02",
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
        "#12P#0105F咦……！？\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x104,
        (
            "#6P#0301F喂喂……\x01",
            "这到底是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x160,
        (
            "#11P#3309F呵呵，真要感谢姐姐\x01",
            "昨天陪我玩呢。\x02\x03",

            "#3302F不过，现在是不是应该\x01",
            "把这个问题延后一下呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        "#0206F#5P……嗯，确实没错。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#6P#0001F好……\x01",
            "这就联络一下试试吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)

    def lambda_6F2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6F2A)
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
            "罗伊德联络了玲给的通讯号码。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(902, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "喂喂！\x01",
            "您是哪位！？\x02",
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
            "#0005F啊……\x02\x03",

            "#0001F嗯，我是克洛斯贝尔警察局·特别\x01",
            "任务支援科的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

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
            "太、太好了！\x01",
            "我正想联络游击士\x01",
            "协会或者警察局呢！\x02\x03",

            "可、可是两边的号码我都不知道，\x01",
            "所以就想联络老爸……唔！\x02",
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
            "#0011F请、请冷静一点。\x02\x03",

            "#0001F您似乎有些慌乱……\x01",
            "请问到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这、这个……\x02\x03",

            "小、小、小男孩\x01",
            "不知道跑到哪里去了！\x02",
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
            "#0005F哎……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "刚才，我在西克洛斯贝尔街道的\x01",
            "途中停了下车……！\x02\x03",

            "因为听到有动静，就去确认一下货箱，\x01",
            "结果发现有个小男孩在里面……！\x02\x03",

            "好像是自己偷偷钻进去的。\x01",
            "就这么把他带到贝尔加德门也不太好，\x01",
            "所以便打算和公司商量一下……！\x02\x03",

            "结果，就在我通话的时候，\x01",
            "那孩子不知道跑到哪里去了！！\x02",
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
        "#0101F怎、怎么了？\x02",
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
            "#11P#0001F嗯……\x01",
            "事情有些不妙了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德简短地说明了情况。\x07\x00\x02",
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
        "#11P#3305F哎……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        "#0201F#5P……怎么会……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#6P#0301F这可不太妙啊……！\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        "#11P#0003F嗯，赶快出城吧。\x02",
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
            "#0001F情况紧急，我们立即就赶过去。\x02\x03",

            "请您不要随便乱动，\x01",
            "就留在原处等待吧。\x02\x03",

            "说不定那个孩子还会回来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年的声音")

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "麻、麻烦你们了！\x02\x03",

            "无论如何，请尽快赶来……！\x02",
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
        "#11P#0003F赶快从西出口出去吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0247
    ChrTalk(
        0x101,
        "#0001F#6P还有小玲，你就……\x02",
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
            "#11P#3300F……要一起去。\x02\x03",

            "玲不会碍手碍脚的，\x01",
            "让玲也一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        "#6P#0105F但、但是……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0205F#5P你还是在这里等待\x01",
            "比较安全吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x160,
        (
            "#11P#3303F找到那孩子\x01",
            "下落的可是玲哦。\x02\x03",

            "#3300F所以，玲必须要\x01",
            "见证到最后。\x02\x03",

            "#3302F呵呵……无论降临于那孩子身上的\x01",
            "是何种命运。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        "#6P#0101F你……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x104,
        (
            "#6P#0306F虽然不清楚有什么内情，\x01",
            "不过你好像意外地执著呢。\x02\x03",

            "#0301F刻不容缓。\x01",
            "罗伊德，带上她一起走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#0006F#6P嗯。\x02\x03",

            "#0001F──小玲，\x01",
            "虽然我已经知道你不是普通的\x01",
            "女孩子了，但还是千万不要乱来啊。\x02\x03",

            "只有这一点，请一定要做到。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x160,
        (
            "#11P#3306F知道啦。\x02\x03",

            "#3300F还有，直接叫\x01",
            "玲的名字就可以了。\x02\x03",

            "不然会让人家觉得\x01",
            "有点难为情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#0004F#6P哈哈，明白了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(150)

    #C0257
    ChrTalk(
        0x101,
        (
            "#11P#0007F──好，那就\x01",
            "立即赶往西出口吧。\x02\x03",

            "去西克洛斯贝尔街道\x01",
            "寻找柯林。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        "#6P#0101F嗯……！\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x103,
        "#0201F#5P明白了……！\x02",
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

    # Function_18_6286 end

    def Function_19_7A76(): pass

    label("Function_19_7A76")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A90")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x6, 0x7, 0x6)
    Jump("Function_19_7A76")

    label("loc_7A90")

    Return()

    # Function_19_7A76 end

    def Function_20_7A91(): pass

    label("Function_20_7A91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AB9")
    Sound(849, 0, 70, 0)
    Sound(850, 0, 70, 0)
    Sleep(900)
    Sound(849, 0, 70, 0)
    Sleep(900)
    Jump("Function_20_7A91")

    label("loc_7AB9")

    Return()

    # Function_20_7A91 end

    def Function_21_7ABA(): pass

    label("Function_21_7ABA")

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

    def lambda_7D0D():
        OP_95(0xFE, 0, 0, 122000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D0D)

    def lambda_7D27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D27)
    Sleep(1000)

    def lambda_7D3B():

        label("loc_7D3B")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_7D3B")

    QueueWorkItem2(0x160, 2, lambda_7D3B)
    WaitChrThread(0x101, 1)

    def lambda_7D51():
        OP_95(0xFE, 1000, 30, 124000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D51)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)
    EndChrThread(0x160, 0x2)

    #C0261
    ChrTalk(
        0x101,
        "#12P#0002F……睡着了啊。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x160,
        "#3304F#5P呵呵……\x02",
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
            "#3300F#5P好可爱的睡脸呢……\x02\x03",

            "是个对罪恶一无所知，\x01",
            "纯洁无垢的好孩子啊……\x02\x03",

            "#3304F……都长得这么大了。\x02",
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
            "#12P#0003F我刚才联络了\x01",
            "这孩子的父母。\x02\x03",

            "#0000F他们说马上就来接他。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x160,
        "#3308F#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#12P#0001F你是最大的功臣。\x02\x03",

            "我认为，理应把你\x01",
            "介绍给他们……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x160,
        (
            "#3303F#5P──没这个必要哦。\x02\x03",

            "#3300F玲的名字，以及存在，\x01",
            "都没有必要告诉那些人。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#12P#0008F可是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0270
    ChrTalk(
        0x101,
        (
            "#12P#0001F──我说，玲。\x02\x03",

            "我已经明白你不是可以用常识\x01",
            "来衡量的普通女孩子了。\x02\x03",

            "#0003F投掷那把大镰刀的能力、\x01",
            "以『小猫』的身份所使用的黑客技术……\x02\x03",

            "还有推定那孩子所在位置时的\x01",
            "理性而多角度的推理能力……\x02\x03",

            "#0008F……你实在是太过多才多艺，\x01",
            "甚至都让人感觉有些不太现实……\x02\x03",

            "#0000F我现在已经理解了，\x01",
            "你就是那种真正意义上的『天才』。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x160,
        "#3304F#5P呵呵……\x02",
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
            "#3302F#5P──大哥哥，你果然\x01",
            "很有一套呢。\x02\x03",

            "#3304F没错，玲的本质正在于此。\x02\x03",

            "吸收各种情报并加以处理，\x01",
            "对包括自己在内的环境进行适当操作……\x02\x03",

            "#3300F战斗技术、黑客知识、博士论文、\x01",
            "人偶操作、茶会礼仪等等，\x01",
            "可以说，全都是由这个本质发展而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#12P#0011F博、博士论文！？\x02\x01",

            "#0003F──好吧，这个暂且忽略。\x02\x03",

            "#0001F也就是说，你心里是很清楚的。\x02\x03",

            "清楚到底应该怎样做，\x01",
            "才能实现自己的愿望。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x160,
        (
            "#3309F#5P嘻嘻，正是。\x02\x03",

            "#3302F不管是什么愿望，\x01",
            "玲都能够实现。\x02\x03",

            "不，正确来说，\x01",
            "是明白应该怎样做，\x01",
            "才能让世界为玲实现愿望。\x02\x03",

            "#3304F因为这就是玲的力量的本质。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        (
            "#12P#0006F……原来如此啊。\x02\x03",

            "#0001F既然如此──\x01",
            "那你究竟有什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x160,
        "#3305F#5P…………哎………………\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        (
            "#12P#0003F你本应是无论有什么愿望，\x01",
            "都能让世界为你实现的小公主……\x02\x03",

            "但是，现在的你，\x01",
            "看起来却更像是一只不知该何去何从，\x01",
            "完全迷失了路途的小猫。\x02\x03",

            "#0008F不……说不定，你其实早就知道\x01",
            "自己真正的归宿在哪里。\x02\x03",

            "然而，却有好几块巨石\x01",
            "阻挡在归途中，让你无法回去……\x02\x03",

            "#0001F难道不是这样吗……？\x02",
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
            "#12P#0004F……这都是我的直觉和臆测。\x01",
            "如果猜错的话，我愿意道歉。\x02\x03",

            "#0000F──但是，我们是特别任务支援科。\x02\x03",

            "如果有女孩子在烦恼，\x01",
            "就希望能尽力帮助她……\x02\x03",

            "#0002F即使没办法陪你一起回去，\x01",
            "至少也可以帮你搬走那些岩石。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x160,
        (
            "#3309F#5P……呵呵……\x02\x03",

            "#3300F大哥哥，看来你不仅擅长推理，\x01",
            "连妄想也很拿手呢。\x02\x03",

            "#3302F像你这种人……\x01",
            "又能了解玲多少呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#12P#0006F我当然不了解你。\x02\x03",

            "而且，说不定你其实已经有了\x01",
            "真正想要依靠的人。\x02\x03",

            "#0000F不过──横在路上的岩石\x01",
            "并不只有一块吧？\x02\x03",

            "有没有那种连我们也能搬走的……\x01",
            "比较小的岩石呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x160,
        (
            "#3308F#5P#30W那种……那种事……\x02\x03",

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
        "艾莉的声音",
        (
            "#1P#2S……罗伊德？\x01",
            "哈罗德夫妇已经来了。\x02\x03",

            "#2S我带他们进来了哦？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        "#0011F#5P不，那个──\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x160, 500)
    Sleep(800)

    #C0285
    ChrTalk(
        0x160,
        "#3308F#40W#5P………………啊…………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0286
    ChrTalk(
        0x101,
        (
            "#12P#0000F……不然的话，\x01",
            "你先藏在衣橱里如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x160,
        (
            "#3305F#5P啊……\x02\x03",

            "#3306F………………（点头）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88CD():

        label("loc_88CD")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_88CD")

    QueueWorkItem2(0x101, 2, lambda_88CD)

    def lambda_88DF():
        OP_96(0xFE, 0x0, 0x1E, 0x1E460, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88DF)
    Sleep(500)

    def lambda_88FC():
        OP_95(0xFE, 1000, 0, 122500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_88FC)
    WaitChrThread(0x160, 1)

    def lambda_891A():
        OP_95(0xFE, 2000, 30, 121500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_891A)
    WaitChrThread(0x160, 1)
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move")
    Sound(913, 0, 100, 0)
    Sleep(500)

    def lambda_8951():
        OP_96(0xFE, 0xBB8, 0x1E, 0x1D8A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_8951)

    def lambda_896B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_896B)
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
            "#0000F#5P──嗯！\x01",
            "请他们进来吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0289
    NpcTalk(
        0x102,
        "艾莉的声音",
        (
            "#1P#2S……？\x01",
            "好的，稍等一下哦。\x02",
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
        "男性的声音",
        "#1P#2S打扰了……！\x02",
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

    def lambda_8A62():

        label("loc_8A62")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8A62")

    QueueWorkItem2(0x101, 2, lambda_8A62)

    def lambda_8A74():
        OP_96(0xFE, 0xFFFFFC7C, 0x1E, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A74)
    BeginChrThread(0xF, 3, 0, 23)
    Sleep(500)

    #C0291
    ChrTalk(
        0xF,
        "#3707F#5P#8A啊啊……柯林！\x02",
    )
    #Auto

    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    EndChrThread(0x101, 0x2)

    #C0292
    ChrTalk(
        0xE,
        (
            "#3609F#5P太好了……\x01",
            "真是太好了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1000, 700, 126000, 2500)
    MoveCamera(45, 21, 0, 2500)
    SetCameraDistance(24000, 2500)
    SetChrPos(0x102, 0, 0, 119000, 0)

    def lambda_8B22():
        OP_96(0xFE, 0xFFFFFC7C, 0x1E, 0x1E654, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B22)

    def lambda_8B3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8B3C)
    Sleep(500)

    def lambda_8B50():
        OP_96(0xFE, 0xFFFFFBB4, 0x1E, 0x1E0DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8B50)

    def lambda_8B6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8B6A)
    Sleep(500)

    def lambda_8B7E():
        OP_96(0xFE, 0xFFFFFF9C, 0x1E, 0x1E0DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8B7E)

    def lambda_8B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8B98)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0293
    ChrTalk(
        0x102,
        "#12P#0105F（咦……小玲呢？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0294
    ChrTalk(
        0x101,
        (
            "#0006F#5P（嗯……\x01",
            "  她有点原因，不方便露面。）\x02\x03",

            "#0008F（就藏在那边的衣橱里。）\x02",
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
        "#12P#0101F（哎？）\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#12P#0205F（这又是怎么回事呢……）\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x104,
        "#12P#0305F（好像有什么隐情啊。）\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    def lambda_8D07():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8D07)

    def lambda_8D14():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D14)

    def lambda_8D21():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8D21)

    def lambda_8D2E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8D2E)
    Sleep(300)

    #C0298
    ChrTalk(
        0xE,
        (
            "#11P#3610F──各位，\x01",
            "真是太感激你们了。\x02\x03",

            "#3601F我真不知该如何道谢才好……\x01",
            "大恩大德，实在是永生难忘……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈罗德深深低下了头。\x07\x00\x02",
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
            "#6P#0011F您言重了……！\x01",
            "请赶快把头抬起来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#0100F那个，对我们来说，\x01",
            "寻找柯林也只是执行分内的任务而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)

    #C0302
    ChrTalk(
        0xF,
        (
            "#3701F#11P哪里，哪里！\x02\x03",

            "#3708F如果各位没有找到他，\x01",
            "柯林可能就……这孩子可能就会……\x02\x03",

            "#3710F……呜呜呜……\x01",
            "真是……真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(300)

    #C0303
    ChrTalk(
        0xE,
        "#3600F没事了……已经没事了……\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x104,
        "#12P#0301F唔……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        "#6P#0208F为什么会如此激动……\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xD,
        "#11P#60W嗯……\x02",
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

    def lambda_8FFE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8FFE)

    def lambda_900B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_900B)
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
        "#6P#3700F柯林……\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xD,
        (
            "#11P#3805F哎……？\x02\x03",

            "为什么\x01",
            "爸爸和妈妈会在这里～？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xF,
        "#6P#3709F啊啊，柯林……！\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xE,
        (
            "#6P#3609F……太好了……真是太好了……！\x02\x03",

            "#3600F以后可不能再这样了哦……\x01",
            "让爸爸和妈妈这么担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xD,
        (
            "#11P#3800F？？？\x02\x03",

            "#3809F听我说哦～！\x01",
            "刚刚玩得好开心呢～！\x02\x03",

            "我追着咪西的车子，\x01",
            "还交了好多原本不认识的朋友！\x02\x03",

            "然后一起玩捉迷藏，爬上了\x01",
            "都是货物的车子，里面好黑好暗的～！\x02\x03",

            "出来之后，又看到了\x01",
            "好漂亮的黄色蝴蝶哦！\x02\x03",

            "#3802F然后、然后呢……！\x02",
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
            "#11P#3805F咦……？\x02\x03",

            "紫色的姐姐呢～？\x02",
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
        "#6P#3605F紫色的……？\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xF,
        "#6P#3700F姐姐……？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xD,
        (
            "#11P#3809F嗯～！\x02\x03",

            "跟你们说哦！\x01",
            "她好强好强呢～！\x02\x03",

            "而且好温柔，\x01",
            "还很香……\x02\x03",

            "#3802F还有哦……\x01",
            "她的头发和爸爸一样，\x01",
            "是紫色的哦～！\x02",
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
        "#6P#3705F哎……\x02",
    )

    CloseMessageWindow()

    def lambda_937C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_937C)
    Sleep(50)
    OP_93(0xF, 0x10E, 0x190)
    Sleep(200)

    #C0317
    ChrTalk(
        0xE,
        (
            "#11P#3601F请问……\x01",
            "那位女孩是！？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#6P#0006F那个……是帮我们寻找\x01",
            "柯林的女孩子。\x02\x03",

            "#0008F好像是外国的旅行者……\x01",
            "至于身份，我们也不太清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xE,
        "#11P#3603F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xF,
        "#11P#3708F………竟然有这种事…………\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xD,
        (
            "#5P#3809F#40W姐姐……\x01",
            "……好想再见她一面哦……\x02\x03",

            "#60W嘿嘿……\x01",
            "然后再……\x01",
            "………请她和我玩………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)

    def lambda_94EA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_94EA)
    Sleep(50)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(300)

    #C0322
    ChrTalk(
        0xF,
        "#6P#3705F啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0323
    ChrTalk(
        0xD,
        "#5P#60W……呼～呼～……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xF,
        "#6P#3700F柯林……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xE,
        (
            "#6P#3600F哈哈……\x01",
            "又睡着了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#6P#0004F不嫌弃的话，\x01",
            "就让他在这继续睡吧。\x02\x03",

            "#0000F我们这里没问题的。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1420, 700, 126070, 2000)
    MoveCamera(45, 21, 0, 2000)
    SetCameraDistance(24000, 2000)

    def lambda_95E5():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_95E5)
    Sleep(100)
    OP_93(0xF, 0x10E, 0x190)
    OP_6F(0x79)

    #C0327
    ChrTalk(
        0xE,
        (
            "#11P#3609F太感谢了。\x01",
            "真是一直给你们添麻烦……\x02\x03",

            "#3600F话说回来……\x01",
            "和我同样发色的女孩吗？\x02\x03",

            "#3604F或许这也是女神\x01",
            "和那孩子的指引啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        "#3700F#11P嗯……我也这么觉得。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#6P#0001F那个……\x01",
            "似乎有什么隐情啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xE,
        "#11P#3605F啊，不……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    #C0331
    ChrTalk(
        0xF,
        (
            "#3700F……亲爱的，我不介意。\x02\x03",

            "人家帮了我们这么大的忙，\x01",
            "没必要对他们隐瞒……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xE,
        "#11P#3600F……说得也是。\x02",
    )

    CloseMessageWindow()

    def lambda_9765():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_9765)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    #C0333
    ChrTalk(
        0xE,
        (
            "#11P#3603F──我们夫妇\x01",
            "曾经有过一个女儿。\x02\x03",

            "那已经是七年以前的事情了。\x02",
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
        "#6P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#6P#0101F请问……\x01",
            "您说曾经，也就是说……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xE,
        (
            "#11P#3608F是的，因为一场不幸的事故……\x02\x03",

            "#3610F不──不是事故。\x02\x03",

            "#3601F那孩子……可以说是\x01",
            "被我们亲手害死的。\x02",
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
        "#6P#0205F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x104,
        "#12P#0301F这话怎么说……\x02",
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
            "#30W──八年前。\x02\x03",

            "#30W我还是个初出茅庐的贸易商。\x01",
            "为了在逐渐扩大的克洛斯贝尔贸易市场\x01",
            "占据一席之地，我拼尽了浑身解数。\x02\x03",

            "#30W最后不惜在共和国那边\x01",
            "做起了危险的投机买卖……\x02\x03",

            "#30W结果，因此背上了巨额的债务。\x02",
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
            "#30W我们带着年幼的女儿，开始了逃亡生活……\x02\x03",

            "可是，我们逃到哪里，债主就会追到哪里，\x01",
            "我们找不到任何安身之处。\x02\x03",

            "#30W再这样下去，说不定会迫使\x01",
            "恶名昭彰的黑手党出马──\x02\x03",

            "#30W害怕事态发展到那种地步的我们，\x01",
            "便将女儿托付给了一个老朋友。\x02",
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
            "#30W──那是一个居住在共和国，很值得信赖的友人。\x02\x03",

            "#30W我们打算尽快偿还掉所有欠款……\x01",
            "等到再无借债之后，\x01",
            "再回来迎接女儿。\x02",
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
            "#30W──幸好，在一位可靠律师的帮助之下，\x01",
            "我们总算是理清了债务。\x02\x03",

            "#30W然后托关系、找门路、重建事业，\x01",
            "拼死拼活地努力工作……\x02\x03",

            "#30W最后，总算在一年之内，\x01",
            "成功还清了所有的欠款。\x02\x03",

            "#30W这下终于能见到女儿了……\x01",
            "一家三口终于能再次团聚在一起，幸福地生活了……\x02\x03",

            "#30W……我们怀着这样的喜悦之情……\x01",
            "来到了那个朋友的家，准备接回女儿……\x02",
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
            "#30W──听说，是发生了原因不明的火灾。\x02\x03",

            "#30W当时，有组织的放火抢劫事件\x01",
            "在共和国那边似乎频频发生……\x02\x03",

            "#30W我那个朋友的家也遭到了袭击。\x02\x03",

            "#30W由于朋友的家位于郊外，\x01",
            "所以负责处理的部门发现得很晚……\x02\x03",

            "#30W而且……我们寄养在那里的女儿\x01",
            "也被卷入到了事件……\x02",
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
            "#30W我们……\x01",
            "几近疯狂地寻找着女儿。\x02\x03",

            "#30W可是……每具遗体都是无法辨认的惨状。\x01",
            "最终，我们得到了家中所有人都已身亡的\x01",
            "验尸结果。\x02\x03",

            "#30W我们的女儿……\x01",
            "我们无可替代的宝贝，\x01",
            "已经永远地失去了。\x02\x03",

            "#30W留给我们的……\x01",
            "只有无尽的绝望。\x02\x03",

            "#30W……是我们将死亡的命运带给了那孩子，\x01",
            "而自己继续活下去，究竟还有什么意义……\x02\x03",

            "#30W我们甚至都想过自尽，\x01",
            "夫妻二人一起追随那孩子而去……\x02\x03",

            "#30W──可就在这时，却突然发生了一件意外之事。\x02\x03",

            "#30W我的妻子已经怀上了柯林……\x01",
            "也就是那个孩子的弟弟。\x02",
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
            "#30W人就是这么现实，当发现了这一事实后，\x01",
            "我们便找回了生存的勇气。\x02\x03",

            "#30W我们下定了决心，绝不会再重蹈覆辙，\x01",
            "之后就脚踏实地，一心一意地诚信经商……\x02\x03",

            "#30W就这样，柯林诞生了……\x01",
            "我们也渐渐从绝望的打击中再次站了起来。\x02\x03",

            "#30W──然而，长久以来，\x01",
            "我们其实一直都在逃避。\x02\x03",

            "#30W逃避着自己因为无能\x01",
            "而将爱女害死的痛苦……\x02\x03",

            "#30W……逃避着我们所犯下的罪孽……\x02",
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
            "#11P#3608F这就是──\x01",
            "我们夫妇所背负的罪孽。\x02\x03",

            "#3603F实在抱歉……\x01",
            "让你们听我说了这么多令人难受的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#6P#0008F……竟然有这种事…………\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#6P#0106F这……真不知该说什么好……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        "#12P#0306F……这就是因果循环啊。\x02",
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
            "#3708F#11P可是……\x01",
            "随着这孩子逐渐长大，\x01",
            "模样就和女儿越来越像……\x02\x03",

            "不知不觉中，我们又开始\x01",
            "被强烈的罪恶感所苛责。\x02\x03",

            "#3710F……当时，若是没有放开\x01",
            "那双小手该多好……\x02\x03",

            "无论多么痛苦、多么艰辛，\x01",
            "一家人一起坚持努力就好了……\x02\x03",

            "这追悔莫及的感觉，\x01",
            "无时无刻不萦绕在我们心头……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "#11P#3603F……于是，我们便重新\x01",
            "坚定了这样一个信念。\x02\x03",

            "#3600F能怀上柯林，\x01",
            "是因为亡女和女神的指引……\x02\x03",

            "正因如此，我们一家人……\x01",
            "必须要过得幸福才行。\x02\x03",

            "这才是回报女儿的\x01",
            "唯一方法……\x02\x03",

            "#3603F……即使我们深知，\x01",
            "这只不过是自私的借口罢了……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        "#6P#0108F哈罗德先生……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#6P#0204F……我认为，这也是\x01",
            "一种值得赞同的思考方式。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0356
    ChrTalk(
        0x104,
        (
            "#12P#0302F嗯……比起捶胸顿足、\x01",
            "止步不前可要强得多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xE,
        (
            "#11P#3609F哈哈……谢谢你们。\x02\x03",

            "#3600F……话说回来……\x01",
            "还真是不可思议呢。\x02\x03",

            "听说，那位救了柯林的小姑娘……\x01",
            "发色和我一样吧。\x02\x03",

            "#3604F那孩子──我们去世的女儿\x01",
            "也有同样的紫色头发呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#6P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        "#6P#0108F也就是说……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xF,
        (
            "#3709F#11P嗯……简直就像是那孩子\x01",
            "从天堂降临，保护了柯林一样……\x02\x03",

            "#3700F──对了，各位。\x02\x03",

            "如果以后找到那位小姑娘的话，\x01",
            "可以再和我们联络吗？\x02\x03",

            "希望能与她正式见个面……\x01",
            "衷心地向她表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#6P#0003F──我明白了。\x02\x03",

            "#0000F……如果能联系上的话，\x01",
            "我一定会转告给那孩子。\x02",
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

    # Function_21_7ABA end

    def Function_22_A8F4(): pass

    label("Function_22_A8F4")


    def lambda_A8F9():
        OP_95(0xFE, 0, 0, 122000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A8F9)

    def lambda_A913():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A913)
    WaitChrThread(0xE, 1)

    def lambda_A928():
        OP_95(0xFE, 1200, 30, 125700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A928)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x5A, 0x1F4)
    Return()

    # Function_22_A8F4 end

    def Function_23_A949(): pass

    label("Function_23_A949")


    def lambda_A94E():
        OP_95(0xFE, 0, 0, 122000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A94E)

    def lambda_A968():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A968)
    WaitChrThread(0xF, 1)

    def lambda_A97D():
        OP_95(0xFE, 1200, 30, 124700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A97D)
    WaitChrThread(0xF, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_23_A949 end

    def Function_24_A99B(): pass

    label("Function_24_A99B")

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
            "#6P#0003F……他们回去了。\x02\x03",

            "#0000F你可以出来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0363
    NpcTalk(
        0x160,
        "玲",
        "#2S#11P#40W………………………………\x02",
    )

    CloseMessageWindow()
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move")
    Sound(913, 0, 100, 0)
    Sleep(500)
    SetCameraDistance(21500, 2500)

    def lambda_ABA3():
        OP_96(0xFE, 0x7D0, 0x1E, 0x1DA9C, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_ABA3)

    def lambda_ABBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_ABBD)
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
        "#6P#0105F啊……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x103,
        "#0208F#6P玲……\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#6P#0008F……这样好吗？\x02\x03",

            "#0001F现在追过去的话，\x01",
            "应该还来得及……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x160,
        (
            "#11P#3312F#40W……不……不用了……\x02\x03",

            "因为，玲来这个城市的原因……\x01",
            "已经有一个消失掉了……\x02\x03",

            "#3314F所以……这样就足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#6P#0006F是吗……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x102,
        (
            "#6P#0101F怎么能这样……\x01",
            "真的没关系吗……！？\x02\x03",

            "小玲，\x01",
            "不管再怎么想，你也……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0371
    ChrTalk(
        0x104,
        (
            "#0306F#5P──别说了，大小姐。\x02\x03",

            "#0301F这世上，有一些隐情\x01",
            "是遵纪守法的普通人无法想象的。\x02\x03",

            "外人还是不要插嘴为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        "#6P#0108F这、这个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0373
    ChrTalk(
        0x103,
        "#0206F……我也有同感。\x02",
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
            "#11P#3314F#40W呵呵……别露出这种表情嘛。\x02\x03",

            "#3312F#40W──谢谢你，大哥哥。\x02\x03",

            "挡在玲的归途上的\x01",
            "#40W几块大石头……\x02\x03",

            "#3300F你已经帮我搬掉其中一块了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AEFA():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AEFA)
    Sleep(50)

    def lambda_AF0A():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AF0A)

    #C0376
    ChrTalk(
        0x101,
        (
            "#6P#0006F是吗……\x02\x03",

            "#0000F能帮助你，是我的荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x160,
        (
            "#11P#3300F呵呵……\x01",
            "也要感谢大姐姐们。\x02\x03",

            "#3312F……今天的谢礼，\x01",
            "以后一定会补上的……\x02\x03",

            "#3314F所以……\x01",
            "玲就先告辞啦。\x02",
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

    def lambda_B026():

        label("loc_B026")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_B026")

    QueueWorkItem2(0x101, 2, lambda_B026)

    def lambda_B038():

        label("loc_B038")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_B038")

    QueueWorkItem2(0x102, 2, lambda_B038)

    def lambda_B04A():

        label("loc_B04A")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_B04A")

    QueueWorkItem2(0x103, 2, lambda_B04A)

    def lambda_B05C():

        label("loc_B05C")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_B05C")

    QueueWorkItem2(0x104, 2, lambda_B05C)

    def lambda_B06E():
        OP_95(0xFE, 0, 0, 120400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_B06E)
    WaitChrThread(0x160, 1)
    Sound(103, 0, 100, 0)

    def lambda_B092():
        OP_95(0xFE, 0, 0, 119000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_B092)

    def lambda_B0AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_B0AC)
    Sleep(800)
    Sound(104, 0, 100, 0)

    #C0378
    ChrTalk(
        0x101,
        "#0011F#5P啊……\x02",
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
            "#12P#0108F……这样真的好吗？\x01",
            "不追上去保护她没关系吗……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B28A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B28A)
    Sleep(50)

    def lambda_B29A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B29A)
    Sleep(300)

    #C0381
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯……\x01",
            "这个我当然也想过。\x02\x03",

            "#0000F不过，我感觉\x01",
            "那并不是属于我们的使命。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#0305F哎……？\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x103,
        (
            "#0205F#11P又是罗伊德前辈\x01",
            "拿手的推理吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#5P#0002F不，与其说是推理──\x02",
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
        "#1P#2S#15A#40W请问～有人在吗～！\x02",
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

    def lambda_B416():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B416)

    def lambda_B423():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B423)

    def lambda_B430():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B430)

    def lambda_B43D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B43D)
    Sleep(300)

    #C0386
    ChrTalk(
        0x101,
        "#0005F#6P这声音是……\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#12P#0105F好像是从一楼传来的。\x02",
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

    def lambda_B59D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B59D)

    def lambda_B5AE():
        OP_96(0xFE, 0x384, 0x352, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5AE)
    Sleep(150)

    def lambda_B5CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B5CB)

    def lambda_B5DC():
        OP_96(0xFE, 0x7D0, 0x352, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5DC)
    Sleep(50)

    def lambda_B5F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B5F9)

    def lambda_B60A():
        OP_96(0xFE, 0x384, 0x352, 0x2A30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B60A)
    Sleep(150)

    def lambda_B627():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B627)

    def lambda_B638():
        OP_96(0xFE, 0x7D0, 0x352, 0x2A30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B638)
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
        "#0102F#5P哎呀……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        "#5P#0000F你们是……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(400, 1100, 2900, 2000)
    MoveCamera(53, 19, 0, 2000)
    SetCameraDistance(25000, 2000)
    Sleep(1000)

    def lambda_B734():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B734)
    Sleep(200)

    def lambda_B751():
        OP_96(0xFE, 0x5DC, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B751)
    Sleep(80)

    def lambda_B76E():
        OP_96(0xFE, 0xFFFFFF9C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B76E)
    Sleep(120)

    def lambda_B78B():
        OP_96(0xFE, 0x4B0, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B78B)
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
            "嘿嘿……你们好。\x02\x03",

            "突然来访，真是抱歉哦。\x01",
            "也没事先联络一下……\x02",
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
            "我知道打扰各位了，\x01",
            "但是，有件事情急着要确认……\x02\x03",

            "能不能占用各位一点时间呢？\x02",
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
        "#0000F#5P这个倒是没问题……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x104,
        "#5P#0305F到底是什么事情呢？\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x103,
        (
            "#5P#0201F是关于\x01",
            "『黑之竞拍会』吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "#12P#0806F啊～那件事\x01",
            "就先不用去管啦……\x02\x03",

            "#0801F……更、更重要的是……\x02\x03",

            "我们获取了一份目击情报，\x01",
            "据说罗伊德今天下午\x01",
            "曾和某个人物一起行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#0005F#5P某个人物……？\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x11,
        (
            "#12P#0903F……是一个紫色头发的女孩子。\x02\x03",

            "#0901F我想，应该\x01",
            "还穿着白裙子……\x02",
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
        "#0011F#5P哎，这个……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x102,
        "#5P#0101F是说小玲吧？\x02",
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
        "#12P#0813F#4S啊！！！\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x11,
        "#12P#0901F果然是……！\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        (
            "#0011F#5P稍、稍微等一下。\x02\x03",

            "#0001F那孩子……\x01",
            "原来和你们有关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x11,
        (
            "#12P#0903F嗯……是的。\x02\x03",

            "#0908F虽然我们也有好几个月\x01",
            "都没见到她了……\x02\x03",

            "#0902F不过……\x01",
            "她果然还在克洛斯贝尔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x10,
        "#12P#0809F#40W……啊、啊哈哈…………\x02",
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
        "#0901F#11P艾丝蒂尔……！？\x02",
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
            "#12P#0806F没、没关系……\x01",
            "一放下心来，就有些全身脱力……\x02",
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
            "#12P#0804F好～……！\x01",
            "既然如此，我就不客气了～！\x02\x03",

            "#0802F已经彻底锁定目标，\x01",
            "这次绝对要抓到她！\x02",
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
            "#5P#0302F喂喂，\x01",
            "那个小姑娘好受欢迎啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x103,
        (
            "#5P#0204F约纳好像也对她很执著……\x01",
            "还真不是一般地受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#0006F#5P那个……那孩子\x01",
            "该不会是游击士吧？\x02\x03",

            "#0001F她的年纪太小了……\x01",
            "而且好像也做过不少危险的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    #C0411
    ChrTalk(
        0x11,
        "#12P#0904F嗯……她的确不是游击士。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x10,
        (
            "#12P#0804F不过，对我们来说，\x01",
            "她可是如同家人一般重要的孩子哦。\x02\x03",

            "#0800F这大半年来……\x01",
            "我们一直在寻找她。\x02\x03",

            "为了抓住那孩子……\x01",
            "让她成为我们的『家人』。\x02",
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
        "#0005F#5P家、家人……？\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        (
            "#5P#0101F这个……\x01",
            "似乎有很多隐情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x10,
        (
            "#12P#0806F那是自然啊……\x01",
            "事情相当错综复杂呢。\x02\x03",

            "#0808F#30W……来到克洛斯贝尔之后，\x01",
            "我们也查清了不少事……\x02\x03",

            "#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)

    #C0416
    ChrTalk(
        0x11,
        (
            "#0906F#11P唉，你可不能\x01",
            "自己在那里沮丧啊。\x02\x03",

            "#0900F我们不是收集了海瓦斯夫妇的情报，\x01",
            "准备让那孩子敞开心扉的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 500)

    #C0417
    ChrTalk(
        0x10,
        "#6P#0800F嗯、嗯……是呀！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0418
    ChrTalk(
        0x101,
        (
            "#0001F#5P海瓦斯夫妇……\x01",
            "是指哈罗德先生他们吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C21F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_C21F)

    def lambda_C22C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_C22C)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0419
    ChrTalk(
        0x10,
        (
            "#12P#0813F咦咦咦！？\x02\x03",

            "为什么你们会知道\x01",
            "这个名字啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#0012F#5P这个，其实\x01",
            "我也正想问这句呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#5P#0106F……看来，还是把今天发生的事情\x01",
            "从头到尾说明一下比较好呢。\x02",
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
            "#12P#0003F──事情就是这样，\x01",
            "那个孩子刚刚回去，\x01",
            "正好和你们错过了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0423
    ChrTalk(
        0x101,
        "#12P#0011F等、等一下，艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x10,
        "#5P#0808F#60W啊……\x02",
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
            "#5P#0811F#50W讨、讨厌……\x01",
            "……怎么会这样……\x02\x03",

            "#0810F#60W呜……呜……\x02",
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

    def lambda_C543():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_C543)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0426
    ChrTalk(
        0x10,
        (
            "#0810F#5P……呜呜……\x01",
            "#4S哇啊啊啊啊啊啊啊……！\x02",
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
        "#11P#0910F#40W艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0428
    ChrTalk(
        0x10,
        (
            "#5P#0810F#40W对、对不起啊，约修亚……\x01",
            "……还有罗伊德和大家……\x02\x03",

            "#40W可是我……\x01",
            "不知道该说什么好……\x02\x03",

            "#0808F#40W……她并不是被抛弃的……\x01",
            "是被爸爸妈妈爱着的……\x02\x03",

            "#40W那孩子终于……\x01",
            "可以敞开心扉……去面对这痛苦悲哀……\x01",
            "#40W……而又温暖的事实了……\x02\x03",

            "#0810F#40W………呜呜呜…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0429
    ChrTalk(
        0x102,
        "#12P#0108F痛苦悲哀，而又温暖的事实……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        "#12P#0008F就是哈罗德先生他们所说的往事吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)

    #C0431
    ChrTalk(
        0x11,
        (
            "#5P#0908F──在这其中，曾出现过数次\x01",
            "悲哀的偶然与误解。\x02\x03",

            "其结果……\x01",
            "就是让那个经历过残酷地狱的孩子\x01",
            "开始欺骗自己。\x02\x03",

            "#0903F她制造出虚假的双亲——帕蒂尔·玛蒂尔，\x01",
            "而放弃去寻找真相。\x02\x03",

            "可是……这也不能怪她。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x104,
        (
            "#0306F……原来如此，正因为年幼，\x01",
            "所以只能用这种方式来进行自我保护吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x103,
        (
            "#6P#0208F可是……\x01",
            "这样是无法前进的。\x02\x03",

            "#0206F别说前进……\x01",
            "就连真正的归所也回不去。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x11,
        (
            "#5P#0908F嗯……\x02\x03",

            "#0903F所以我们打算\x01",
            "帮助她燃起\x01",
            "面对真相的勇气。\x02\x03",

            "因为，根据我们的调查得知，真相虽然悲哀，\x01",
            "但其中依然包含着真实的亲情……\x02\x03",

            "所以，我们觉得……\x01",
            "现在的她，一定能克服自己的过去。\x02\x03",

            "#0902F不过……\x01",
            "看来已经没有这个必要了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        (
            "#12P#0004F……嗯。\x02\x03",

            "#0000F至少，她看上去\x01",
            "好像已经完全理解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x11,
        "#5P#0911F是吗……\x02",
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
            "#0903F#5P谢谢你，罗伊德，\x01",
            "还有支援科的各位。\x02\x03",

            "真不知该如何感谢你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        (
            "#12P#0004F哈哈……不必放在心上。\x02\x03",

            "#0002F这应该算是顺水推舟吧，\x01",
            "而且那孩子也帮了我们很多忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x102,
        "#12P#0104F呵呵……的确是哦。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x10,
        "#5P#0810F呜……\x02",
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
        "#5P#0800F#4S──嗯，决定了！\x02",
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
            "#5P#0802F既然最大的障碍已经消失了，\x01",
            "我就再也不会跟她客气了！\x02\x03",

            "#0809F你看着吧～玲！\x02\x03",

            "我绝对会继续铲平障碍，\x01",
            "让你成为我们家的一份子！\x02",
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
        "#12P#0009F哈哈……好厉害的气势啊。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x104,
        (
            "#0309F#12P哎呀～虽然不太明白状况，\x01",
            "不过，这才是艾丝蒂尔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x103,
        "#6P#0202F该怎么说呢……真是太耀眼了。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x11,
        (
            "#11P#0904F呵呵，热情值得肯定。\x02\x03",

            "#0902F再没有什么能比鼓足干劲的\x01",
            "艾丝蒂尔更可怕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x10,
        "#5P#0804F哼哼，一切都包在我的身上吧。\x02",
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
            "#5P#0800F──罗伊德先生、艾莉小姐，\x01",
            "还有小缇欧和兰迪先生。\x02\x03",

            "也请允许我郑重\x01",
            "向你们道谢。\x02\x03",

            "#0804F真是太谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0449
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔深深低下了头。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0450
    ChrTalk(
        0x101,
        "#12P#0002F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        "#12P#0102F……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x11, 0x0)
    Sleep(500)

    #C0452
    ChrTalk(
        0x11,
        (
            "#5P#0904F今后如果需要我们帮忙，\x01",
            "请不要客气，随时告诉我们。\x02\x03",

            "#0902F我们之间，应该没必要在意\x01",
            "警察与游击士的芥蒂了。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x10,
        (
            "#5P#0809F嗯嗯！\x01",
            "我们会尽全力协助你们的！\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        (
            "#12P#0004F哈哈……明白了。\x02\x03",

            "#0000F万一发生了紧急状况，\x01",
            "我们肯定会向你们求助的。\x02",
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
            "其后，罗伊德与艾丝蒂尔等人\x01",
            "来到东街的『龙老饭店』，\x01",
            "共进了晚餐，彼此的关系变得更加融洽了。\x02\x03",

            "关于发生在两人的故乡——『利贝尔王国』的\x01",
            "『异变』真相及其始末……\x02\x03",

            "以及玲所属的，\x01",
            "名为『结社』的神秘组织……\x02\x03",

            "各种惊天动地的情报接踵而至，\x01",
            "而纪念庆典第四天的夜色也渐渐深了。\x07\x00\x02",
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
    SubItemNumber('废弃材料', 1)
    Call(0, 11)
    Return()

    # Function_24_A99B end

    def Function_25_D1EC(): pass

    label("Function_25_D1EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D205")
    OP_A1(0xFE, 0x3E8, 0x3, 0xE, 0xF, 0x10)
    Jump("Function_25_D1EC")

    label("loc_D205")

    Return()

    # Function_25_D1EC end

    def Function_26_D206(): pass

    label("Function_26_D206")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D220")
    OP_A1(0xFE, 0x3E8, 0x4, 0x6, 0x7, 0x8, 0x9)
    Jump("Function_26_D206")

    label("loc_D220")

    Return()

    # Function_26_D206 end

    def Function_27_D221(): pass

    label("Function_27_D221")


    def lambda_D226():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D226)

    def lambda_D237():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D237)
    WaitChrThread(0x101, 1)

    def lambda_D255():
        OP_95(0xFE, 700, 0, 62700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D255)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    Return()

    # Function_27_D221 end

    def Function_28_D276(): pass

    label("Function_28_D276")


    def lambda_D27B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D27B)

    def lambda_D28C():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D28C)
    WaitChrThread(0x102, 1)

    def lambda_D2AA():
        OP_95(0xFE, 700, 0, 61500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D2AA)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Return()

    # Function_28_D276 end

    def Function_29_D2CB(): pass

    label("Function_29_D2CB")


    def lambda_D2D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D2D0)

    def lambda_D2E1():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D2E1)
    WaitChrThread(0x103, 1)

    def lambda_D2FF():
        OP_95(0xFE, 2000, 0, 62700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D2FF)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x13B, 0x1F4)
    Return()

    # Function_29_D2CB end

    def Function_30_D320(): pass

    label("Function_30_D320")


    def lambda_D325():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D325)

    def lambda_D336():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D336)
    WaitChrThread(0x104, 1)

    def lambda_D354():
        OP_95(0xFE, 2000, 0, 61500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D354)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    Return()

    # Function_30_D320 end

    def Function_31_D375(): pass

    label("Function_31_D375")


    def lambda_D37A():
        OP_95(0xFE, -700, 0, 62700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_D37A)
    WaitChrThread(0x160, 1)

    def lambda_D398():
        OP_95(0xFE, -2200, 0, 67900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_D398)
    WaitChrThread(0x160, 1)

    def lambda_D3B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_D3B6)
    Sound(103, 0, 100, 0)

    def lambda_D3CD():
        OP_95(0xFE, -5000, 0, 67900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_D3CD)
    WaitChrThread(0x160, 1)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x160, 2)
    Return()

    # Function_31_D375 end

    def Function_32_D3F1(): pass

    label("Function_32_D3F1")

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
            "#1K创立纪念庆典　第二天\x02",
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
            "──好了，你们几个，\x01",
            "假期过得开心吗？\x02\x03",

            "说是代价也许有点不合适吧，不过，\x01",
            "从今天开始，到最终日的四天之内……\x02\x03",

            "你们可要鼓足干劲，拼命工作，\x01",
            "拜托了哦。\x02",
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
        "#12P#0006F呼……明白了。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x104,
        (
            "#0306F话说，五天的纪念庆典，\x01",
            "居然只有第一天放假……\x02\x03",

            "#0301F这未免也太小气了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#0106F算了，这也正能说明\x01",
            "警察局上下都很忙吧。\x02\x03",

            "#0100F警备和巡逻工作，在庆典的第一天\x01",
            "应该是最忙的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#5P#1004F嗯，就是这么回事。\x02\x03",

            "#1002F所以，给你们放假姑且算是\x01",
            "将暗杀市长事件防范于未然的褒奖吧。\x02\x03",

            "而且总部似乎也不打算在纪念庆典期间\x01",
            "把杂务扔给你们哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        (
            "#12P#0006F相对地，支援请求\x01",
            "倒是发来了不少呢。\x02\x03",

            "#0000F游客好像也比平时多了好几倍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#5P#1002F哼哼，你们好不容易\x01",
            "打出名声，人气差不多也快接近\x01",
            "游击士的脚跟了。\x02\x03",

            "不趁现在努力的话，更待何时？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#12P#0002F嗯，这倒是。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#0306F我怎么觉得，好像是被\x01",
            "巧妙地哄骗了过去……\x02\x03",

            "#0308F唉，其实我好想和\x01",
            "那些护士妹妹们一起去\x01",
            "『米修拉姆』玩啊～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(150)

    #C0466
    ChrTalk(
        0x103,
        (
            "#6P#0205F说到『米修拉姆』……\x01",
            "是从港湾区乘游览船\x01",
            "就能抵达的那个主题公园吧？\x02\x03",

            "#0202F听说『咪西』\x01",
            "是那里的吉祥物……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DA23():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DA23)
    Sleep(50)
    TurnDirection(0x102, 0x104, 500)

    #C0467
    ChrTalk(
        0x101,
        (
            "#5P#0005F『咪西』……\x01",
            "啊，是那个猫咪吉祥物啊。\x02\x03",

            "#0000F那个造型，我以前见过。\x01",
            "不过，主题公园这种东西，\x01",
            "在三年前应该还没有吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        (
            "#5P#0104F『米修拉姆』本身\x01",
            "一直以疗养地而著称……\x02\x03",

            "#0102F至于主题公园那边，\x01",
            "应该是在两年多之前建成的吧。\x02\x03",

            "自那以来，似乎就十分受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x104,
        (
            "#0309F嗯，我以前也去过一次，\x01",
            "那里可真是相当壮观呢。\x02\x03",

            "#0302F不过，那里的游客平时就络绎不绝，\x01",
            "在纪念庆典期间肯定就更加拥挤了。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x103,
        (
            "#6P#0204F原来如此……\x01",
            "我也有一点兴趣呢。\x02",
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

    def lambda_DC6F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DC6F)
    Sleep(50)

    def lambda_DC7F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DC7F)
    Sleep(50)
    OP_93(0x103, 0x0, 0x1F4)

    #C0472
    ChrTalk(
        0x101,
        "#12P#0005F……科长？\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x8,
        (
            "#5P#1005F嗯，哦……\x02\x03",

            "#1003F总而言之，到最终日为止的四天之内，\x01",
            "你们只要专心解决支援请求就好了。\x02\x03",

            "#1002F嗯，至于具体该怎么做，\x01",
            "就和以前一样，由你们自己判断。\x02\x03",

            "支援请求应该会每天更新，\x01",
            "好好期待吧。\x02",
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

    def lambda_DEA4():
        OP_96(0xFE, 0x3E80, 0x352, 0xB54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DEA4)

    def lambda_DEBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DEBE)
    Sleep(250)

    def lambda_DED2():
        OP_96(0xFE, 0x3E80, 0x352, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DED2)

    def lambda_DEEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DEEC)
    Sleep(400)

    def lambda_DF00():
        OP_96(0xFE, 0x4394, 0x352, 0xB54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DF00)

    def lambda_DF1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DF1A)
    Sleep(250)

    def lambda_DF2E():
        OP_96(0xFE, 0x4394, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DF2E)

    def lambda_DF48():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DF48)
    WaitChrThread(0x101, 1)

    def lambda_DF5D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DF5D)
    WaitChrThread(0x102, 1)

    def lambda_DF6E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DF6E)
    WaitChrThread(0x103, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)

    def lambda_DF94():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DF94)
    WaitChrThread(0x104, 1)

    def lambda_DFA5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DFA5)
    WaitChrThread(0x104, 2)
    SetMapObjFlags(0x0, 0x10)
    OP_6F(0x1)
    Sleep(300)

    #C0474
    ChrTalk(
        0x101,
        (
            "#6P#0004F#6P好吧……总之，\x01",
            "先去确认一下终端上的支援请求吧。\x02\x03",

            "#0000F视情况，\x01",
            "说不定还有必要前往\x01",
            "克洛斯贝尔市外呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x102,
        (
            "#0103F#5P嗯，是呀。\x02\x03",

            "#0100F最近去阿尔摩利卡村\x01",
            "那边观光的人\x01",
            "似乎也有不少……\x02\x03",

            "除了铁道和飞行船之外，\x01",
            "好像还有从陆路来的游客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x104,
        (
            "#5P#0305F也就是说，东西国境门的\x01",
            "客流量也会比平时多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x103,
        (
            "#0203F……诺艾尔上士他们\x01",
            "在纪念庆典期间肯定也很辛苦吧。\x02\x03",

            "#0200F游击士们就\x01",
            "更不用说了。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#6P#0001F嗯，\x01",
            "我们也不能认输啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#0104F#5P不过，要是绷得太紧，\x01",
            "我们的体力也会撑不住吧。\x02\x03",

            "#0102F先确认一下委托的紧急程度，\x01",
            "安排好之后再处理会比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        "#6P#0000F这倒也是……\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x104,
        "#5P#0300F好啦，一件件认真解决吧。\x02",
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

    # Function_32_D3F1 end

    def Function_33_E2EE(): pass

    label("Function_33_E2EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E308")
    OP_A1(0x103, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_33_E2EE")

    label("loc_E308")

    Return()

    # Function_33_E2EE end

    def Function_34_E309(): pass

    label("Function_34_E309")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E323")
    OP_A1(0x103, 0xBB8, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_34_E309")

    label("loc_E323")

    Return()

    # Function_34_E309 end

    def Function_35_E324(): pass

    label("Function_35_E324")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E358")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    Sleep(300)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(300)
    Jump("Function_35_E324")

    label("loc_E358")

    Return()

    # Function_35_E324 end

    def Function_36_E359(): pass

    label("Function_36_E359")

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

    # Function_36_E359 end

    def Function_37_E73F(): pass

    label("Function_37_E73F")

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

    # Function_37_E73F end

    def Function_38_E76A(): pass

    label("Function_38_E76A")

    Sound(849, 0, 100, 0)
    Sleep(200)
    Sound(850, 0, 100, 0)
    Sleep(700)
    Sound(849, 0, 100, 0)
    Return()

    # Function_38_E76A end

    def Function_39_E783(): pass

    label("Function_39_E783")

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

    def lambda_E86B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E86B)
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
        "#0000F您好，我是罗伊德。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2083, 255, 100, 0)    #voice#Fran
    #Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0483
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德警官。\x02\x03"      #line#50
            "抱歉，百忙之中打扰了哦。\x01",
            "现在方便吗？\x02",
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
            "#0000F嗯……\x01",
            "工作刚刚告一段落，\x01",
            "应该没问题。\x02\x03",

            "总部有紧急任务吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0485
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不，是有位先生希望与你们\x01",
            "当面商量委托事宜。\x02\x03",

            "他是位贸易商，\x01",
            "名叫哈罗德……\x02",
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
            "#0005F啊，我们认识……\x01",
            "究竟是什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0487
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个……\x02\x03",

            "好像是在观看市内游行的时候，\x01",
            "他的孩子走失了。\x02",
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
            "#0003F是吗，明白了。\x02\x03",

            "#0001F我们要去哪里和他见面呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就在警察局总部附近，\x01",
            "喷泉前面的长椅那里。\x02\x03",

            "孩子似乎就是在那附近\x01",
            "走失的。\x02",
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
            "#0000F明白了，我们立刻赶去看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0491
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好的，麻烦各位了。\x02",
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
            "#11P#0105F怎么了？\x02",
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
            "#6P#0003F啊，贸易商哈罗德先生\x01",
            "有事情要委托我们。\x02\x03",

            "#0001F据说是在看游行的时候，\x01",
            "他的孩子走失了。\x02",
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
        "#11P#0101F这……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x103,
        (
            "#12P#0206F今天这么多人，\x01",
            "走散了可真是不得了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x104,
        (
            "#0300F#11P这么说，也就是庆典时期的\x01",
            "惯例任务——寻找走失的小孩吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0497
    ChrTalk(
        0x101,
        (
            "#5P#0004F嗯，多半是。\x02\x03",

            "#0000F说是在警察局总部附近的\x01",
            "喷泉前等着我们，\x01",
            "总之，先去问问情况吧。\x02",
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

    # Function_39_E783 end

    def Function_40_EE1F(): pass

    label("Function_40_EE1F")

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

    def lambda_EF04():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EF04)
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
        "#0000F您好，我是罗伊德。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2083, 255, 100, 0)    #voice#Fran
    #Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0499
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德警官。\x02\x03"      #line#50
            "抱歉，百忙之中打扰了哦。\x01",
            "现在方便吗？\x02",
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
            "#0000F嗯……\x01",
            "工作刚刚告一段落，\x01",
            "应该没问题。\x02\x03",

            "总部有紧急任务吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0501
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不，是有位先生希望与你们\x01",
            "当面商量委托事宜。\x02\x03",

            "他是位贸易商，\x01",
            "名叫哈罗德……\x02",
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
            "#0005F啊，我们认识……\x01",
            "究竟是什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个……\x02\x03",

            "好像是在观看市内游行的时候，\x01",
            "他的孩子走失了。\x02",
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
            "#0003F是吗，明白了。\x02\x03",

            "#0001F我们要去哪里和他见面呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0505
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就在警察局总部附近，\x01",
            "喷泉前面的长椅那里。\x02\x03",

            "孩子似乎就是在那附近\x01",
            "走失的。\x02",
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
            "#0000F明白了，我们立刻赶去看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0507
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好的，麻烦各位了。\x02",
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
            "#6P#0105F怎么了？\x02",
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
            "#11P#0003F啊，贸易商哈罗德先生\x01",
            "有事要委托我们。\x02\x03",

            "#0001F说是在看游行的时候，\x01",
            "他的孩子走失了。\x02",
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
        "#6P#0101F这……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x103,
        (
            "#5P#0206F今天这么多人，\x01",
            "走散了可真是不得了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x104,
        (
            "#0300F#5P这么说，也就是庆典时期的\x01",
            "惯例任务——寻找走失的小孩吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0513
    ChrTalk(
        0x101,
        (
            "#12P#0004F嗯，多半是。\x02\x03",

            "#0000F说是在警察局总部附近的\x01",
            "喷泉前等我们，\x01",
            "总之，先去问问情况吧。\x02",
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

    # Function_40_EE1F end

    def Function_41_F4B0(): pass

    label("Function_41_F4B0")

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
        "#0005F搜查二科发来了委托呢。\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x102,
        (
            "#0105F揭发假货贩子……\x01",
            "具体委托内容到底是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        (
            "#0302F话说，从警察局总部\x01",
            "发来重要的支援请求，\x01",
            "这还是头一次吧？\x02\x03",

            "#0304F这也就表示，警察局的其他家伙\x01",
            "总算也承认了我们的实力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        (
            "#0203F#12P这个……也难说吧。\x02\x03",

            "#0211F也有可能只是又把\x01",
            "一些麻烦的杂务推过来而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        (
            "#0000F嗯，总之，先去听听\x01",
            "多诺邦警督怎么说吧。\x02\x03",

            "顺利的话，说不定以后还能获得\x01",
            "更多与其它科合作的机会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        (
            "#0100F是呀……\x01",
            "去行政区的警察局总部看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_41_F4B0 end

    def Function_42_F701(): pass

    label("Function_42_F701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F732")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_F732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F763")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_F763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F794")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_F794")

    Return()

    # Function_42_F701 end

    def Function_43_F795(): pass

    label("Function_43_F795")


    #C0520
    ChrTalk(
        0x101,
        (
            "#0000F出门之前，\x01",
            "还是先确认一下\x01",
            "支援请求吧……\x02\x03",

            "说不定会有\x01",
            "紧急的委托。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_43_F795 end

    def Function_44_F7E3(): pass

    label("Function_44_F7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8E7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F887")

    #C0521
    ChrTalk(
        0x103,
        (
            "#0200F罗伊德前辈，约纳\x01",
            "可能会发来联络。\x02\x03",

            "还是不要走太远为好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#0000F说得也是……\x01",
            "做好准备之后，\x01",
            "就赶快去地下空间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8D1")

    label("loc_F887")


    #C0523
    ChrTalk(
        0x103,
        (
            "#0200F……约纳\x01",
            "可能会发来联络。\x02\x03",

            "做好准备之后，\x01",
            "就赶快去地下空间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8D1")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)

    label("loc_F8E7")

    Return()

    # Function_44_F7E3 end

    def Function_45_F8E8(): pass

    label("Function_45_F8E8")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_45_F8E8 end

    def Function_46_F90C(): pass

    label("Function_46_F90C")

    Return()

    # Function_46_F90C end

    def Function_47_F90D(): pass

    label("Function_47_F90D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F965")
    SetChrFlags(0x0, 0x8)

    label("loc_F965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F978")
    SetChrFlags(0x1, 0x8)

    label("loc_F978")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F98B")
    SetChrFlags(0x2, 0x8)

    label("loc_F98B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F99E")
    SetChrFlags(0x3, 0x8)

    label("loc_F99E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9B1")
    SetChrFlags(0x4, 0x8)

    label("loc_F9B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9C4")
    SetChrFlags(0x5, 0x8)

    label("loc_F9C4")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    #C0525
    ChrTalk(
        0x101,
        "#0000F放在这里就行了吧。\x02",
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
            "罗伊德的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('竞赛旗', 1)
    SetScenarioFlags(0x50, 6)
    OP_66(0x7, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA58")
    ClearChrFlags(0x0, 0x8)

    label("loc_FA58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA6B")
    ClearChrFlags(0x1, 0x8)

    label("loc_FA6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA7E")
    ClearChrFlags(0x2, 0x8)

    label("loc_FA7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA91")
    ClearChrFlags(0x3, 0x8)

    label("loc_FA91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAA4")
    ClearChrFlags(0x4, 0x8)

    label("loc_FAA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAB7")
    ClearChrFlags(0x5, 0x8)

    label("loc_FAB7")

    Call(0, 64)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_47_F90D end

    def Function_48_FACE(): pass

    label("Function_48_FACE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB26")
    SetChrFlags(0x0, 0x8)

    label("loc_FB26")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB39")
    SetChrFlags(0x1, 0x8)

    label("loc_FB39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB4C")
    SetChrFlags(0x2, 0x8)

    label("loc_FB4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB5F")
    SetChrFlags(0x3, 0x8)

    label("loc_FB5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB72")
    SetChrFlags(0x4, 0x8)

    label("loc_FB72")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB85")
    SetChrFlags(0x5, 0x8)

    label("loc_FB85")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0527
    ChrTalk(
        0x101,
        "#0000F放在这里就行了吧。\x02",
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
            "罗伊德的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('小径自行车', 1)
    SetScenarioFlags(0x50, 7)
    OP_66(0x8, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC19")
    ClearChrFlags(0x0, 0x8)

    label("loc_FC19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC2C")
    ClearChrFlags(0x1, 0x8)

    label("loc_FC2C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC3F")
    ClearChrFlags(0x2, 0x8)

    label("loc_FC3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC52")
    ClearChrFlags(0x3, 0x8)

    label("loc_FC52")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC65")
    ClearChrFlags(0x4, 0x8)

    label("loc_FC65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC78")
    ClearChrFlags(0x5, 0x8)

    label("loc_FC78")

    Call(0, 64)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_48_FACE end

    def Function_49_FC8F(): pass

    label("Function_49_FC8F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCE7")
    SetChrFlags(0x0, 0x8)

    label("loc_FCE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCFA")
    SetChrFlags(0x1, 0x8)

    label("loc_FCFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD0D")
    SetChrFlags(0x2, 0x8)

    label("loc_FD0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD20")
    SetChrFlags(0x3, 0x8)

    label("loc_FD20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD33")
    SetChrFlags(0x4, 0x8)

    label("loc_FD33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD46")
    SetChrFlags(0x5, 0x8)

    label("loc_FD46")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    #C0529
    ChrTalk(
        0x102,
        "#0100F放在这里就好了吧。\x02",
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
            "艾莉的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('安乐椅', 1)
    SetScenarioFlags(0x51, 0)
    OP_66(0x9, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDD8")
    ClearChrFlags(0x0, 0x8)

    label("loc_FDD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDEB")
    ClearChrFlags(0x1, 0x8)

    label("loc_FDEB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDFE")
    ClearChrFlags(0x2, 0x8)

    label("loc_FDFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE11")
    ClearChrFlags(0x3, 0x8)

    label("loc_FE11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE24")
    ClearChrFlags(0x4, 0x8)

    label("loc_FE24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE37")
    ClearChrFlags(0x5, 0x8)

    label("loc_FE37")

    Call(0, 64)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_49_FC8F end

    def Function_50_FE4E(): pass

    label("Function_50_FE4E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEB1")
    SetChrFlags(0x0, 0x8)

    label("loc_FEB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEC4")
    SetChrFlags(0x1, 0x8)

    label("loc_FEC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FED7")
    SetChrFlags(0x2, 0x8)

    label("loc_FED7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEEA")
    SetChrFlags(0x3, 0x8)

    label("loc_FEEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEFD")
    SetChrFlags(0x4, 0x8)

    label("loc_FEFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF10")
    SetChrFlags(0x5, 0x8)

    label("loc_FF10")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0531
    ChrTalk(
        0x102,
        "#0100F放在这里就好了吧。\x02",
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
            "艾莉的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('迷你水族馆', 1)
    SetScenarioFlags(0x51, 1)
    OP_66(0xA, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFA2")
    ClearChrFlags(0x0, 0x8)

    label("loc_FFA2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFB5")
    ClearChrFlags(0x1, 0x8)

    label("loc_FFB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFC8")
    ClearChrFlags(0x2, 0x8)

    label("loc_FFC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFDB")
    ClearChrFlags(0x3, 0x8)

    label("loc_FFDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFEE")
    ClearChrFlags(0x4, 0x8)

    label("loc_FFEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10001")
    ClearChrFlags(0x5, 0x8)

    label("loc_10001")

    Call(0, 64)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_50_FE4E end

    def Function_51_10018(): pass

    label("Function_51_10018")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10070")
    SetChrFlags(0x0, 0x8)

    label("loc_10070")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10083")
    SetChrFlags(0x1, 0x8)

    label("loc_10083")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10096")
    SetChrFlags(0x2, 0x8)

    label("loc_10096")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_100A9")
    SetChrFlags(0x3, 0x8)

    label("loc_100A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_100BC")
    SetChrFlags(0x4, 0x8)

    label("loc_100BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_100CF")
    SetChrFlags(0x5, 0x8)

    label("loc_100CF")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0533
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
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
            "缇欧的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('古怪靠垫', 1)
    SetScenarioFlags(0x51, 2)
    OP_66(0xB, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1015D")
    ClearChrFlags(0x0, 0x8)

    label("loc_1015D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10170")
    ClearChrFlags(0x1, 0x8)

    label("loc_10170")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10183")
    ClearChrFlags(0x2, 0x8)

    label("loc_10183")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10196")
    ClearChrFlags(0x3, 0x8)

    label("loc_10196")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101A9")
    ClearChrFlags(0x4, 0x8)

    label("loc_101A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101BC")
    ClearChrFlags(0x5, 0x8)

    label("loc_101BC")

    Call(0, 64)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_51_10018 end

    def Function_52_101D3(): pass

    label("Function_52_101D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1022B")
    SetChrFlags(0x0, 0x8)

    label("loc_1022B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1023E")
    SetChrFlags(0x1, 0x8)

    label("loc_1023E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10251")
    SetChrFlags(0x2, 0x8)

    label("loc_10251")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10264")
    SetChrFlags(0x3, 0x8)

    label("loc_10264")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10277")
    SetChrFlags(0x4, 0x8)

    label("loc_10277")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1028A")
    SetChrFlags(0x5, 0x8)

    label("loc_1028A")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    #C0535
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
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
            "缇欧的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('波波靠垫', 1)
    SetScenarioFlags(0x51, 3)
    OP_66(0xC, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10318")
    ClearChrFlags(0x0, 0x8)

    label("loc_10318")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1032B")
    ClearChrFlags(0x1, 0x8)

    label("loc_1032B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1033E")
    ClearChrFlags(0x2, 0x8)

    label("loc_1033E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10351")
    ClearChrFlags(0x3, 0x8)

    label("loc_10351")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10364")
    ClearChrFlags(0x4, 0x8)

    label("loc_10364")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10377")
    ClearChrFlags(0x5, 0x8)

    label("loc_10377")

    Call(0, 64)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_52_101D3 end

    def Function_53_1038E(): pass

    label("Function_53_1038E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_103E6")
    SetChrFlags(0x0, 0x8)

    label("loc_103E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_103F9")
    SetChrFlags(0x1, 0x8)

    label("loc_103F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1040C")
    SetChrFlags(0x2, 0x8)

    label("loc_1040C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1041F")
    SetChrFlags(0x3, 0x8)

    label("loc_1041F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10432")
    SetChrFlags(0x4, 0x8)

    label("loc_10432")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10445")
    SetChrFlags(0x5, 0x8)

    label("loc_10445")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0537
    ChrTalk(
        0x104,
        "#0300F就放这里好了。\x02",
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
            "兰迪的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('黑泰迪熊', 1)
    SetScenarioFlags(0x51, 4)
    OP_66(0xD, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104D3")
    ClearChrFlags(0x0, 0x8)

    label("loc_104D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104E6")
    ClearChrFlags(0x1, 0x8)

    label("loc_104E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104F9")
    ClearChrFlags(0x2, 0x8)

    label("loc_104F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1050C")
    ClearChrFlags(0x3, 0x8)

    label("loc_1050C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1051F")
    ClearChrFlags(0x4, 0x8)

    label("loc_1051F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10532")
    ClearChrFlags(0x5, 0x8)

    label("loc_10532")

    Call(0, 64)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_53_1038E end

    def Function_54_10549(): pass

    label("Function_54_10549")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105AC")
    SetChrFlags(0x0, 0x8)

    label("loc_105AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105BF")
    SetChrFlags(0x1, 0x8)

    label("loc_105BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105D2")
    SetChrFlags(0x2, 0x8)

    label("loc_105D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105E5")
    SetChrFlags(0x3, 0x8)

    label("loc_105E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105F8")
    SetChrFlags(0x4, 0x8)

    label("loc_105F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1060B")
    SetChrFlags(0x5, 0x8)

    label("loc_1060B")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    #C0539
    ChrTalk(
        0x104,
        "#0300F就放这里好了。\x02",
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
            "兰迪的房间里\x01",
            "添加了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('苦番茄人玩偶', 1)
    SetScenarioFlags(0x51, 5)
    OP_66(0xE, 0x1)
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10699")
    ClearChrFlags(0x0, 0x8)

    label("loc_10699")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106AC")
    ClearChrFlags(0x1, 0x8)

    label("loc_106AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106BF")
    ClearChrFlags(0x2, 0x8)

    label("loc_106BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106D2")
    ClearChrFlags(0x3, 0x8)

    label("loc_106D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106E5")
    ClearChrFlags(0x4, 0x8)

    label("loc_106E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106F8")
    ClearChrFlags(0x5, 0x8)

    label("loc_106F8")

    Call(0, 64)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_54_10549 end

    def Function_55_1070F(): pass

    label("Function_55_1070F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10761")
    SetChrName("")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "获得了家具类物品之后，\x01",
            "可以将其放置在主人公们的房间里。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x51, 6)

    label("loc_10761")

    Return()

    # Function_55_1070F end

    def Function_56_10762(): pass

    label("Function_56_10762")

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

    # Function_56_10762 end

    def Function_57_10807(): pass

    label("Function_57_10807")

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
            "这里放着导力音响。\x02",
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
        (0, "loc_108C7"),
        (1, "loc_108D0"),
        (2, "loc_108D9"),
        (3, "loc_108E2"),
        (4, "loc_108EB"),
        (5, "loc_108F4"),
        (6, "loc_108FD"),
        (7, "loc_10906"),
        (SWITCH_DEFAULT, "loc_1090F"),
    )


    label("loc_108C7")

    PlayBGM("ed7400", 0)
    Jump("loc_1090F")

    label("loc_108D0")

    PlayBGM("ed7401", 0)
    Jump("loc_1090F")

    label("loc_108D9")

    PlayBGM("ed7402", 0)
    Jump("loc_1090F")

    label("loc_108E2")

    PlayBGM("ed7204", 0)
    Jump("loc_1090F")

    label("loc_108EB")

    PlayBGM("ed7205", 0)
    Jump("loc_1090F")

    label("loc_108F4")

    PlayBGM("ed7201", 0)
    Jump("loc_1090F")

    label("loc_108FD")

    PlayBGM("ed7200", 0)
    Jump("loc_1090F")

    label("loc_10906")

    PlayBGM("ed7202", 0)
    Jump("loc_1090F")

    label("loc_1090F")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_57_10807 end

    def Function_58_1093E(): pass

    label("Function_58_1093E")

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

    # Function_58_1093E end

    def Function_59_109DF(): pass

    label("Function_59_109DF")

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

    # Function_59_109DF end

    def Function_60_10A82(): pass

    label("Function_60_10A82")

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

    # Function_60_10A82 end

    def Function_61_10B25(): pass

    label("Function_61_10B25")

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

    # Function_61_10B25 end

    def Function_62_10BC8(): pass

    label("Function_62_10BC8")

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

    # Function_62_10BC8 end

    def Function_63_10C71(): pass

    label("Function_63_10C71")

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

    # Function_63_10C71 end

    def Function_64_10D14(): pass

    label("Function_64_10D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D4C")
    OP_DE(0x16, 0x0)

    label("loc_10D4C")

    Return()

    # Function_64_10D14 end

    def Function_65_10D4D(): pass

    label("Function_65_10D4D")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DCE")
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

    label("loc_10DCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DEA")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_10DEA")

    Return()

    # Function_65_10D4D end

    def Function_66_10DEC(): pass

    label("Function_66_10DEC")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E6D")
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

    label("loc_10E6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E89")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_10E89")

    Return()

    # Function_66_10DEC end

    def Function_67_10E8B(): pass

    label("Function_67_10E8B")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F0C")
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

    label("loc_10F0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F28")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_10F28")

    Return()

    # Function_67_10E8B end

    def Function_68_10F2A(): pass

    label("Function_68_10F2A")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FAB")
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

    label("loc_10FAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FC7")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_10FC7")

    Return()

    # Function_68_10F2A end

    SaveToFile()

Try(main)
