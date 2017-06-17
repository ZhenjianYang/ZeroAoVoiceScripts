from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0410.bin",                # FileName
        "c0410",                    # MapName
        "c0410",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0410",                  # 0
        "伊莉娅",                 # 1
        "莉夏",                   # 2
        "卡雷利亚",               # 3
        "巴尔萨摩经理",           # 4
        "接待员罗兰多",           # 5
        "亚邦剧团长",             # 6
        "海因兹",                 # 7
        "尤金",                   # 8
        "缇奥多尔",               # 9
        "尼克鲁",                 # 10
        "普莉埃",                 # 11
        "塞利娜",                 # 12
        "修利",                   # 13
        "伊莉娅",                 # 14
        "尤金",                   # 15
        "塞利娜",                 # 16
        "观众",                   # 17
        "观众",                   # 18
        "观众",                   # 19
        "观众",                   # 20
        "麦克道尔市长",           # 21
        "阿奈斯特秘书",           # 22
        "格蕾丝",                 # 23
        "达德利搜查官",           # 24
        "警官",                   # 25
        "客人",                   # 26
        "客人",                   # 27
        "客人",                   # 28
        "客人",                   # 29
        "客人",                   # 30
        "客人",                   # 31
        "客人",                   # 32
        "客人",                   # 33
        "客人",                   # 34
        "客人",                   # 35
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch27500.itc",                   # 05
        "chr/ch24200.itc",                   # 06
        "chr/ch28700.itc",                   # 07
        "chr/ch28702.itc",                   # 08
        "chr/ch28800.itc",                   # 09
        "chr/ch28900.itc",                   # 0A
        "chr/ch29000.itc",                   # 0B
        "chr/ch29100.itc",                   # 0C
        "chr/ch29102.itc",                   # 0D
        "chr/ch36600.itc",                   # 0E
        "chr/ch36602.itc",                   # 0F
        "chr/ch36700.itc",                   # 10
        "chr/ch36900.itc",                   # 11
        "apl/ch50257.itc",                   # 12
        "chr/ch09800.itc",                   # 13
        "chr/ch10100.itc",                   # 14
        "chr/ch21200.itc",                   # 15
        "chr/ch33200.itc",                   # 16
        "chr/ch21100.itc",                   # 17
        "chr/ch20100.itc",                   # 18
    ))

    DeclNpc(-123849, 0,       -2240,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-123050, 0,       -920,    315,  389,  0x0, 0,   1,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-123800, 0,       -2289,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-2250,   2500,    15000,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6969,    0,       3480,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-42090,  5599,    102569,  135,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-50150,  0,       24180,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-125209, 0,       -479,    270,  389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-87309,  0,       -1980,   90,   261,  0x0, 0,   9,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-49939,  0,       13039,   90,   389,  0x0, 0,   10,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-93360,  0,       -2000,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-125250, 0,       -460,    270,  261,  0x0, 0,   12,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4920,    0,       5170,    225,  389,  0x0, 0,   20,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-87550,  50,      -50,     90,   389,  0x0, 0,   18,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-87550,  50,      -50,     90,   261,  0x0, 0,   8,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-87550,  50,      -50,     90,   389,  0x0, 0,   13,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-39490,  5599,    99000,   0,    389,  0x0, 0,   21,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-39279,  5599,    100540,  180,  389,  0x0, 0,   22,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(-340,    0,       2079,    315,  405,  0x0, 0,   23,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-949,    0,       2880,    0,    389,  0x0, 0,   24,  0,   0,   0,   0,   35,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 86,  9.0,                   14.0,                  2.5,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -4.5,                  -2.799999713897705,    -0.4999999701976776,   1.0])

    DeclActor(0,       2500,    16500,   1200,    0,       3500,    16500,   0x007C, 0,  43, 0x0000)
    DeclActor(47000,   5600,    15300,   1200,    47000,   6600,    15300,   0x007C, 0,  45, 0x0000)
    DeclActor(-37500,  5600,    98000,   1200,    -37500,  6600,    98000,   0x007C, 0,  44, 0x0000)
    DeclActor(-47000,  11200,   125000,  1200,    -47000,  12200,   125000,  0x007C, 0,  46, 0x0000)
    DeclActor(6500,    0,       5000,    1200,    6970,    1500,    5000,    0x007E, 0,  9,  0x0000)
    DeclActor(6500,    0,       3480,    1200,    6970,    1500,    3480,    0x007E, 0,  12, 0x0000)
    DeclActor(-50140,  0,       24750,   1200,    -50140,  1500,    24750,   0x007C, 0,  89, 0x0000)

    ScpFunction((
        "Function_0_790",          # 00, 0
        "Function_1_848",          # 01, 1
        "Function_2_873",          # 02, 2
        "Function_3_89E",          # 03, 3
        "Function_4_8C9",          # 04, 4
        "Function_5_8F4",          # 05, 5
        "Function_6_11E0",         # 06, 6
        "Function_7_1517",         # 07, 7
        "Function_8_15AC",         # 08, 8
        "Function_9_20E5",         # 09, 9
        "Function_10_20E9",        # 0A, 10
        "Function_11_2208",        # 0B, 11
        "Function_12_30F4",        # 0C, 12
        "Function_13_30F8",        # 0D, 13
        "Function_14_31B5",        # 0E, 14
        "Function_15_3483",        # 0F, 15
        "Function_16_364D",        # 10, 16
        "Function_17_38FC",        # 11, 17
        "Function_18_4082",        # 12, 18
        "Function_19_437E",        # 13, 19
        "Function_20_476B",        # 14, 20
        "Function_21_4867",        # 15, 21
        "Function_22_4BCA",        # 16, 22
        "Function_23_4D2E",        # 17, 23
        "Function_24_50B4",        # 18, 24
        "Function_25_586F",        # 19, 25
        "Function_26_5D18",        # 1A, 26
        "Function_27_61D9",        # 1B, 27
        "Function_28_64F7",        # 1C, 28
        "Function_29_7078",        # 1D, 29
        "Function_30_711A",        # 1E, 30
        "Function_31_73CA",        # 1F, 31
        "Function_32_74C2",        # 20, 32
        "Function_33_7534",        # 21, 33
        "Function_34_7597",        # 22, 34
        "Function_35_75FC",        # 23, 35
        "Function_36_765E",        # 24, 36
        "Function_37_7D7B",        # 25, 37
        "Function_38_7DE0",        # 26, 38
        "Function_39_7DFC",        # 27, 39
        "Function_40_8175",        # 28, 40
        "Function_41_8374",        # 29, 41
        "Function_42_857B",        # 2A, 42
        "Function_43_885E",        # 2B, 43
        "Function_44_8A24",        # 2C, 44
        "Function_45_8ADE",        # 2D, 45
        "Function_46_8B98",        # 2E, 46
        "Function_47_8C4C",        # 2F, 47
        "Function_48_95DE",        # 30, 48
        "Function_49_9BBA",        # 31, 49
        "Function_50_BA08",        # 32, 50
        "Function_51_BA3F",        # 33, 51
        "Function_52_BA83",        # 34, 52
        "Function_53_BAC7",        # 35, 53
        "Function_54_C973",        # 36, 54
        "Function_55_C9AE",        # 37, 55
        "Function_56_C9E9",        # 38, 56
        "Function_57_D067",        # 39, 57
        "Function_58_D1AE",        # 3A, 58
        "Function_59_D2D1",        # 3B, 59
        "Function_60_D484",        # 3C, 60
        "Function_61_D614",        # 3D, 61
        "Function_62_D7CD",        # 3E, 62
        "Function_63_D9A4",        # 3F, 63
        "Function_64_DB09",        # 40, 64
        "Function_65_DC19",        # 41, 65
        "Function_66_DD24",        # 42, 66
        "Function_67_DF03",        # 43, 67
        "Function_68_E01E",        # 44, 68
        "Function_69_E214",        # 45, 69
        "Function_70_E3D2",        # 46, 70
        "Function_71_E5BF",        # 47, 71
        "Function_72_E9F0",        # 48, 72
        "Function_73_EA37",        # 49, 73
        "Function_74_F95A",        # 4A, 74
        "Function_75_F9C3",        # 4B, 75
        "Function_76_FA2C",        # 4C, 76
        "Function_77_FA88",        # 4D, 77
        "Function_78_FD8C",        # 4E, 78
        "Function_79_FE4F",        # 4F, 79
        "Function_80_FF1D",        # 50, 80
        "Function_81_FFAC",        # 51, 81
        "Function_82_10001",       # 52, 82
        "Function_83_10056",       # 53, 83
        "Function_84_1056E",       # 54, 84
        "Function_85_1058A",       # 55, 85
        "Function_86_105A6",       # 56, 86
        "Function_87_105C2",       # 57, 87
        "Function_88_10680",       # 58, 88
        "Function_89_10980",       # 59, 89
    ))


    def Function_0_790(): pass

    label("Function_0_790")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7D0"),
        (1, "loc_7DC"),
        (2, "loc_7E8"),
        (3, "loc_7F4"),
        (4, "loc_800"),
        (5, "loc_80C"),
        (6, "loc_818"),
        (SWITCH_DEFAULT, "loc_824"),
    )


    label("loc_7D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_800")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_80C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_818")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_824")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_830")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_847")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_847")

    Return()

    # Function_0_790 end

    def Function_1_848(): pass

    label("Function_1_848")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_872")
    OP_94(0xFE, 0xFFFFF402, 0xFFFFF59C, 0xB72, 0xD0C, 0x3E8)
    Sleep(300)
    Jump("Function_1_848")

    label("loc_872")

    Return()

    # Function_1_848 end

    def Function_2_873(): pass

    label("Function_2_873")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_89D")
    OP_94(0xFE, 0xFFFE9F26, 0x5B4, 0xFFFE9346, 0xFFFFFA56, 0x3E8)
    Sleep(300)
    Jump("Function_2_873")

    label("loc_89D")

    Return()

    # Function_2_873 end

    def Function_3_89E(): pass

    label("Function_3_89E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C8")
    OP_94(0xFE, 0xFFFE17C2, 0xFFFFF8C6, 0xFFFE244C, 0x546, 0x3E8)
    Sleep(300)
    Jump("Function_3_89E")

    label("loc_8C8")

    Return()

    # Function_3_89E end

    def Function_4_8C9(): pass

    label("Function_4_8C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F3")
    OP_94(0xFE, 0xFFFF403E, 0x201C, 0xFFFF3760, 0x42E0, 0x3E8)
    Sleep(300)
    Jump("Function_4_8C9")

    label("loc_8F3")

    Return()

    # Function_4_8C9 end

    def Function_5_8F4(): pass

    label("Function_5_8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90A")
    SetMapFlags(0x10000000)
    Event(0, 48)

    label("loc_90A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94C")
    Event(0, 66)

    label("loc_94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98E")
    Event(0, 68)

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C7")
    Event(0, 70)

    label("loc_9C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E1")
    Event(0, 73)

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F7")
    Event(0, 42)
    Jump("loc_A70")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A05")
    Jump("loc_A70")

    label("loc_A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1B")
    Event(0, 41)
    Jump("loc_A70")

    label("loc_A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_A29")
    Jump("loc_A70")

    label("loc_A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3F")
    Event(0, 40)
    Jump("loc_A70")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_END)), "loc_A4D")
    Jump("loc_A70")

    label("loc_A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A63")
    Event(0, 39)
    Jump("loc_A70")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A70")
    Event(0, 36)

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A84")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 47)
    Jump("loc_BD3")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_A98")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 49)
    Jump("loc_BD3")

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_AAC")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 53)
    Jump("loc_BD3")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_AC0")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 56)
    Jump("loc_BD3")

    label("loc_AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_AD4")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 57)
    Jump("loc_BD3")

    label("loc_AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_AE8")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 58)
    Jump("loc_BD3")

    label("loc_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_AFC")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 59)
    Jump("loc_BD3")

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_B10")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 60)
    Jump("loc_BD3")

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_B24")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 61)
    Jump("loc_BD3")

    label("loc_B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_B38")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 62)
    Jump("loc_BD3")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_B4C")
    ClearScenarioFlags(0x5D, 2)
    Event(0, 63)
    Jump("loc_BD3")

    label("loc_B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_B60")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 64)
    Jump("loc_BD3")

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_B74")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 65)
    Jump("loc_BD3")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_B88")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 67)
    Jump("loc_BD3")

    label("loc_B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_B9C")
    ClearScenarioFlags(0x5D, 6)
    Event(0, 69)
    Jump("loc_BD3")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_BB0")
    ClearScenarioFlags(0x5D, 7)
    Event(0, 71)
    Jump("loc_BD3")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_BC4")
    ClearScenarioFlags(0x5E, 0)
    Event(0, 77)
    Jump("loc_BD3")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 1)), scpexpr(EXPR_END)), "loc_BD3")
    ClearScenarioFlags(0x5E, 1)
    Event(0, 83)

    label("loc_BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C99")
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -89630, 0, -390, 315)
    SetChrPos(0x10, -90490, 0, 470, 135)
    SetChrPos(0x12, -48930, 0, 4630, 0)
    SetChrPos(0xA, -48930, 0, 6000, 180)
    SetChrPos(0x13, 1440, 0, 14370, 270)
    SetChrPos(0x8, -122330, 0, 670, 270)
    SetChrPos(0xD, -123720, 0, 580, 90)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C85")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C94")
    SetChrFlags(0xF, 0x10)

    label("loc_C94")

    Jump("loc_11DF")

    label("loc_C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D4F")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -90560, 0, 490, 225)
    SetChrPos(0x10, -90970, 0, 4810, 90)
    SetChrPos(0x13, -123590, 0, -450, 225)
    SetChrPos(0xA, -89290, 0, 4810, 270)
    BeginChrThread(0xF, 0, 0, 2)
    BeginChrThread(0x13, 0, 0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D10")
    SetChrFlags(0xA, 0x10)

    label("loc_D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_D45")
    SetChrPos(0xB, -1160, 0, 130, 135)
    SetChrPos(0xC, 230, 0, -860, 315)
    SetChrFlags(0xC, 0x10)
    Jump("loc_D4A")

    label("loc_D45")

    SetChrFlags(0xB, 0x80)

    label("loc_D4A")

    Jump("loc_11DF")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DF5")
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, 3550, 0, -400, 90)
    SetChrPos(0xC, -280, 0, -260, 315)
    SetChrPos(0x9, -91140, 0, 3890, 315)
    SetChrPos(0x10, -88700, 0, -230, 90)
    SetChrPos(0x12, -92130, 0, 4890, 135)
    SetChrPos(0x11, -121580, 0, 1760, 90)
    SetChrChipByIndex(0x16, 0xF)
    BeginChrThread(0xC, 0, 0, 1)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x12, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF0")
    SetChrFlags(0x9, 0x10)

    label("loc_DF0")

    Jump("loc_11DF")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_EBB")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x9, 0x13)
    SetChrChipByIndex(0xF, 0xE)
    SetChrChipByIndex(0x10, 0x10)
    SetChrPos(0x9, -92130, 0, -3120, 270)
    SetChrPos(0xF, -88790, 0, 7470, 270)
    SetChrPos(0x10, -89930, 0, 7480, 0)
    SetChrPos(0x12, -125250, 0, -1380, 270)
    SetChrPos(0x11, -123430, 0, -2280, 180)
    SetChrPos(0xA, -87460, 0, -800, 0)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_11DF")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EFE")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -280, 0, -260, 315)
    BeginChrThread(0x14, 0, 0, 1)
    Jump("loc_11DF")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F2F")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_11DF")

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_F79")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0xA, -90560, 0, 490, 225)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_11DF")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_FC2")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0xA, -87310, 0, -1980, 90)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_11DF")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_100C")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0xA, -90560, 0, 490, 225)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_11DF")

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_105D")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x9, -92130, 0, -3120, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1058")
    SetChrFlags(0x9, 0x10)

    label("loc_1058")

    Jump("loc_11DF")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10C2")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, 6970, 0, 5000, 270)
    SetChrPos(0x11, -90560, 0, 490, 225)
    SetChrPos(0xA, -124560, 0, -1610, 135)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_11DF")

    label("loc_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_115B")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, -1160, 0, 130, 135)
    SetChrPos(0xC, 230, 0, -860, 315)
    SetChrPos(0x10, -124680, 0, 880, 225)
    SetChrPos(0x12, -123460, 0, -2280, 180)
    SetChrPos(0xA, -123410, 0, -980, 180)
    SetChrChipByIndex(0xF, 0xE)
    SetChrChipByIndex(0x12, 0x11)
    BeginChrThread(0x11, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1156")
    SetChrFlags(0xA, 0x10)

    label("loc_1156")

    Jump("loc_11DF")

    label("loc_115B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_11DF")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x10, -88700, 0, -230, 90)
    SetChrPos(0x13, -90560, 0, 490, 225)
    SetChrPos(0xA, -124200, 0, 0, 180)
    SetChrPos(0x9, -124200, 0, -1330, 0)
    SetChrChipByIndex(0x16, 0xF)
    BeginChrThread(0x13, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CB")
    SetChrFlags(0x10, 0x10)

    label("loc_11CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DA")
    SetChrFlags(0xA, 0x10)

    label("loc_11DA")

    Jump("loc_11DF")

    label("loc_11DF")

    Return()

    # Function_5_8F4 end

    def Function_6_11E0(): pass

    label("Function_6_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F9")
    VolumeBGM(0x28, 0xC8)
    Jump("loc_122F")

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_121B")
    VolumeBGM(0x28, 0xC8)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122F")

    label("loc_121B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_122F")
    VolumeBGM(0x32, 0x1F4)

    label("loc_122F")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125C")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x0, 0x1)
    Jump("loc_12A9")

    label("loc_125C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A9")
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 47500, 5650, 15300, 5000, 5000, 90000)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_12A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_12D1")
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    Jump("loc_12EB")

    label("loc_12D1")

    SetMapObjFrame(0xFF, "pos01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x0, 0x1)

    label("loc_12EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1304")
    OP_10(0x0, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_130A")

    label("loc_1304")

    OP_10(0x0, 0x1)
    OP_10(0x10, 0x0)

    label("loc_130A")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_131C")
    Jump("loc_13E8")

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1332")
    OP_65(0x5, 0x1)

    label("loc_1332")

    Jump("loc_13E8")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1349")
    OP_65(0x5, 0x1)
    Jump("loc_13E8")

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1369")
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_13E8")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1377")
    Jump("loc_13E8")

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1389")
    OP_65(0x5, 0x1)
    Jump("loc_13E8")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_13A9")
    OP_63(0xB, 0x0, 1900, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_13E8")

    label("loc_13A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_13B7")
    Jump("loc_13E8")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_13C9")
    OP_65(0x5, 0x1)
    Jump("loc_13E8")

    label("loc_13C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_13DB")
    OP_66(0x4, 0x1)
    Jump("loc_13E8")

    label("loc_13DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13E8")
    OP_65(0x5, 0x1)

    label("loc_13E8")

    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1419")
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1447")
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x3, 0x0, 0x55)

    label("loc_1447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1469")
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    OP_1B(0x0, 0x0, 0x57)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1486")
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    OP_1B(0x0, 0x0, 0x57)

    label("loc_1486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1499")
    OP_1B(0x0, 0x0, 0x57)

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AC")
    OP_1B(0x0, 0x0, 0x57)

    label("loc_14AC")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C4")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_14C4")

    SetMapObjFlags(0x1D, 0x4)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E6")
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14FE")
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1516")
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)

    label("loc_1516")

    Return()

    # Function_6_11E0 end

    def Function_7_1517(): pass

    label("Function_7_1517")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15A5")

    #C0001
    ChrTalk(
        0xD,
        (
            "我将剧本和出场顺序调整了一下，\x01",
            "总算是把演出的步骤搞定了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xD,
        (
            "……老实说，\x01",
            "要是尼克鲁能回来的话，\x01",
            "自然是最好不过了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A8")

    label("loc_15A5")

    Call(0, 15)

    label("loc_15A8")

    TalkEnd(0xFE)
    Return()

    # Function_7_1517 end

    def Function_8_15AC(): pass

    label("Function_8_15AC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_16A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_161C")

    #C0003
    ChrTalk(
        0xB,
        (
            "不过，看样子，\x01",
            "他恐怕是回不来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xB,
        (
            "我原本还盼望他回来，\x01",
            "一直都在仔细留意……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A2")

    label("loc_161C")


    #C0005
    ChrTalk(
        0xB,
        (
            "现在看来，尼克鲁\x01",
            "恐怕是回不来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xB,
        (
            "真让人困扰啊……\x01",
            "马上就要到演出时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "唯一的办法，也只有\x01",
            "找个人来代替他了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16A2")

    Jump("loc_20E1")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1713")

    #C0008
    ChrTalk(
        0xFE,
        (
            "至于演员休息室和观众席那边，\x01",
            "我们会好好留意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "唉……尼克鲁先生\x01",
            "要是能回来就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_18BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172E")
    Call(0, 10)
    Jump("loc_18B8")

    label("loc_172E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17A4")

    #C0010
    ChrTalk(
        0xB,
        (
            "修利看伊莉娅小姐的排练，\x01",
            "看得十分专注。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "她的品味也超乎常人，\x01",
            "以后也许会成大器哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186B")

    label("loc_17A4")


    #C0012
    ChrTalk(
        0xB,
        (
            "修利说她在短时间内\x01",
            "绝对没有上舞台的打算。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "只希望帮忙做些杂事……\x01",
            "就是这样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        (
            "呵呵，话是这么说，但她看伊莉娅小姐\x01",
            "的表演时，看得十分专注呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "……那孩子啊，\x01",
            "将来或许能成大器呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_186B")

    Jump("loc_18B8")

    label("loc_1870")


    #C0016
    ChrTalk(
        0xB,
        (
            "好了，今天也一样，\x01",
            "表演从下午开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "现在必须得把\x01",
            "卫生打扫好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B8")

    Jump("loc_20E1")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_19A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D8")
    Call(0, 10)
    Jump("loc_19A1")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_192D")

    #C0018
    ChrTalk(
        0xB,
        "夜场的表演马上就要开始了。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "希望客人们都能\x01",
            "尽情享受此次表演。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A1")

    label("loc_192D")


    #C0020
    ChrTalk(
        0xB,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "彩虹剧团\x01",
            "今天表演的剧目为\x01",
            "『金之太阳、银之月』。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "希望您能尽情欣赏到\x01",
            "演出结束的那一刻。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19A1")

    Jump("loc_20E1")

    label("loc_19A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_19E5")

    #C0023
    ChrTalk(
        0xB,
        (
            "那位客人在右边的阶梯上方！\x01",
            "请尽快前往……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_1AB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A07")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A6C")

    #C0024
    ChrTalk(
        0xB,
        "表演只剩不到两幕了。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "今天好像什么异常情况都没发生呢，\x01",
            "应该可以平安结束了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAC")

    label("loc_1A6C")


    #C0026
    ChrTalk(
        0xB,
        "表演也开始渐入佳境。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "能让客人们满意，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1AAC")

    Jump("loc_20E1")

    label("loc_1AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD3")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B49")

    #C0028
    ChrTalk(
        0xB,
        (
            "演出已经进行到第二幕……\x01",
            "至今为止，进展都很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "以现在的盛况看来，\x01",
            "正式公演也很值得期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1B49")


    #C0030
    ChrTalk(
        0xB,
        "巡视辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        (
            "演出已经进行到第二幕……\x01",
            "至今为止都很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "从目前的盛况看来，\x01",
            "正式公演也很值得期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BC0")

    Jump("loc_20E1")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_1CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE7")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C56")

    #C0033
    ChrTalk(
        0xB,
        (
            "我仔细看了一下，\x01",
            "所有客人\x01",
            "都是应邀前来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "看来目前还算一切正常……\x01",
            "暂时可以放心了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_1C56")


    #C0035
    ChrTalk(
        0xB,
        "表演顺利开始了。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        "看来目前一切正常呢。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        (
            "也没有看到什么可疑人物……\x01",
            "暂时可以放心了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CBC")

    Jump("loc_20E1")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D7B")

    #C0038
    ChrTalk(
        0xB,
        (
            "另外，目前正在检查\x01",
            "二层的观众席。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        (
            "预演马上就要开始了……\x01",
            "虽然目前正是表演的重要时期。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "但毕竟要做好场内的警备工作，\x01",
            "所以警察走来走去也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4B")

    label("loc_1D7B")


    #C0041
    ChrTalk(
        0xB,
        (
            "搜查一科的成员正在剧场内\x01",
            "巡视警戒……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "我们正在紧张排练，他们却在旁边走来走去，\x01",
            "服装间也被翻了个底朝天……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        "呼，所以总是静不下心来。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "但这毕竟是为了做好场内的警备工作，\x01",
            "也是没办法的事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E4B")

    Jump("loc_20E1")

    label("loc_1E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EA2")

    #C0045
    ChrTalk(
        0xB,
        (
            "预演是新剧目\x01",
            "的首次公开表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        "必须要全力以赴啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F3A")

    label("loc_1EA2")


    #C0047
    ChrTalk(
        0xB,
        (
            "邀请来观看预演的\x01",
            "客人名单已经确定好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "所有的客人都是本剧团的赞助商，\x01",
            "或是给予我们长期关心的大人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "每封邀请信\x01",
            "我们都写得十分用心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F3A")

    Jump("loc_20E1")

    label("loc_1F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1FAE")

    #C0050
    ChrTalk(
        0xB,
        (
            "今天真是太感谢\x01",
            "各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "总之，能够请到警方的人\x01",
            "来进行保安工作……\x01",
            "我们也就可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_1FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2027")

    #C0052
    ChrTalk(
        0xB,
        (
            "我可不想因为这种事情，\x01",
            "令那些忙于排练的\x01",
            "剧团成员们烦心。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "拜托各位了，请一定要\x01",
            "认真进行调查工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_2027")


    #C0054
    ChrTalk(
        0xB,
        (
            "以前也曾收到过这种带有恶作剧\x01",
            "色彩的恐吓信……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "但这次从内容与署名上来看，\x01",
            "似乎并不只是一次单纯的恶作剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "诸位，身为剧团的经理，我也拜托你们了。\x01",
            "请务必要调查个水落石出。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20E1")

    TalkEnd(0xB)
    Return()

    # Function_8_15AC end

    def Function_9_20E5(): pass

    label("Function_9_20E5")

    Call(0, 8)
    Return()

    # Function_9_20E5 end

    def Function_10_20E9(): pass

    label("Function_10_20E9")


    #C0057
    ChrTalk(
        0xFE,
        (
            "对了对了，本剧团新雇了一个\x01",
            "打杂的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "名字叫做修利。\x01",
            "要是见到的话，还请多关照她哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2204")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2195")

    #C0059
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，修利好像\x01",
            "干得还不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2204")

    label("loc_2195")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21CF")

    #C0060
    ChrTalk(
        0x103,
        (
            "#0200F……看来她\x01",
            "干得还不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2204")

    label("loc_21CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2204")

    #C0061
    ChrTalk(
        0x104,
        (
            "#0300F嘿，看来她\x01",
            "干得还挺好嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2204")

    SetScenarioFlags(0xD1, 6)
    Return()

    # Function_10_20E9 end

    def Function_11_2208(): pass

    label("Function_11_2208")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_236A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22EF")

    #C0062
    ChrTalk(
        0xC,
        (
            "无论遇到多么紧急的情况，\x01",
            "只要一牵扯到舞台表演，\x01",
            "这些人就一点也不肯妥协呢……\x02\x03",

            "真是令人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        (
            "啊，另外，今天的表演\x01",
            "改为从傍晚开始……\x01",
            "目前正在紧急发布通知。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "给诸位添了麻烦，\x01",
            "真是万分抱歉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_22EF")


    #C0065
    ChrTalk(
        0xC,
        (
            "伊、伊莉娅小姐和剧团长，\x01",
            "不知商谈得是否顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "两人一直在专注地\x01",
            "讨论着剧本内容……\x01",
            "真是的，在这种时候……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2365")

    Jump("loc_30F0")

    label("loc_236A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2412")
    OP_4B(0xB, 0xFF)

    #C0067
    ChrTalk(
        0xC,
        (
            "我知道了，我会注意\x01",
            "正面大厅的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "另外，稍后还要通知\x01",
            "修利，让她也注意一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "因为那孩子对细微事物\x01",
            "的洞察力十分敏锐呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_2552")

    label("loc_2412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2482")

    #C0070
    ChrTalk(
        0xC,
        (
            "可以请各位去一下\x01",
            "观众席大厅吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "剧团长有些事想跟各位商量一下，\x01",
            "有时间的话还请过去一趟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2552")

    label("loc_2482")


    #C0072
    ChrTalk(
        0xC,
        "啊，各位是警察吧……？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        (
            "#0105F嗯，是的……\x01",
            "（发生什么事了吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "那个，如果可以的话，\x01",
            "能请各位去一下\x01",
            "观众席大厅吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xC,
        (
            "剧团长现在十分困扰……\x01",
            "如果各位愿意跟他谈谈的话，\x01",
            "就再好不过了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2552")

    Jump("loc_30F0")

    label("loc_2557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_266E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2572")
    Call(0, 13)
    Jump("loc_2669")

    label("loc_2572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25ED")

    #C0076
    ChrTalk(
        0xC,
        (
            "不止是伊莉娅小姐和莉夏小姐，\x01",
            "全剧团的演员都如此热衷于表演，真令我惊讶。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        "我们这些职员也不能落后啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2669")

    label("loc_25ED")


    #C0078
    ChrTalk(
        0xC,
        (
            "有一位叫做尼克鲁的\x01",
            "演员……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        (
            "最近似乎练习得\x01",
            "特别努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xC,
        (
            "听说昨天还通宵练习呢。\x01",
            "哎呀，真是令人惊讶的热情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2669")

    Jump("loc_30F0")

    label("loc_266E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2689")
    Call(0, 13)
    Jump("loc_273D")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26E2")

    #C0081
    ChrTalk(
        0xC,
        "距演出开始还有不到十分钟……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "希望今天的表演也能让\x01",
            "诸位满意而归。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273D")

    label("loc_26E2")


    #C0083
    ChrTalk(
        0xC,
        (
            "欢迎光临。\x01",
            "请在这里\x01",
            "检票入场。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "今天的普通座位票\x01",
            "已经售空了，\x01",
            "还请您予以谅解。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_273D")

    Jump("loc_30F0")

    label("loc_2742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_28B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275D")
    Call(0, 13)
    Jump("loc_28AC")

    label("loc_275D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27CC")

    #C0085
    ChrTalk(
        0xC,
        (
            "今天虽然是休馆日，\x01",
            "不过也有一些成员\x01",
            "主动过来练习。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "如果愿意的话，\x01",
            "要不要去见见他们呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28AC")

    label("loc_27CC")


    #C0087
    ChrTalk(
        0xC,
        "新剧目十分受欢迎哦。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        (
            "到今天为止，几乎天天满员，\x01",
            "连两个月后的门票都卖光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "……不过，今天是休馆日，\x01",
            "没有安排演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0000F啊哈哈，是这样啊。\x02\x03",

            "#0003F（不过也好，今天还带着琪雅，\x01",
            "  本来也没法看演出呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_28AC")

    Jump("loc_30F0")

    label("loc_28B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_28E9")

    #C0091
    ChrTalk(
        0xC,
        "可、可疑的客人？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        "难、难道是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F0")

    label("loc_28E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_29C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290B")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_290B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2974")

    #C0093
    ChrTalk(
        0xC,
        "这里没有任何异常。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        (
            "搜查一科的警官们也在认真巡视，\x01",
            "就算有坏人在，也会放弃作恶吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C2")

    label("loc_2974")


    #C0095
    ChrTalk(
        0xC,
        "这里没有任何异常。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "演出已经开始了，\x01",
            "我们连一只苍蝇也不会放行的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_29C2")

    Jump("loc_30F0")

    label("loc_29C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E9")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A50")

    #C0097
    ChrTalk(
        0xC,
        "这是莉夏小姐第一次登台演出。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xC,
        (
            "也许是因为陪她一起练习过吧……\x01",
            "连我也开始紧张了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD0")

    label("loc_2A50")


    #C0099
    ChrTalk(
        0xC,
        (
            "终于到第二幕了，\x01",
            "这是莉夏小姐第一次登台演出呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xC,
        (
            "肯定没问题的。\x01",
            "因为，她可是拥有连那位伊莉娅小姐\x01",
            "都认同的才能呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AD0")

    Jump("loc_30F0")

    label("loc_2AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_2B3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF7")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AF7")


    #C0101
    ChrTalk(
        0xC,
        "演出似乎已经开始了……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xC,
        "要是能平安无事地结束就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F0")

    label("loc_2B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2BA4")

    #C0103
    ChrTalk(
        0xC,
        (
            "从早上开始，就总能看到\x01",
            "搜查一科的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xC,
        (
            "今天的排练似乎\x01",
            "会推迟一会。\x01",
            "呼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C30")

    label("loc_2BA4")


    #C0105
    ChrTalk(
        0xC,
        (
            "从早上开始，就能看到\x01",
            "搜查一科的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "剧团的成员们\x01",
            "似乎并不太在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "但因为要进行调查取证，\x01",
            "所以今天的排练似乎会推迟一点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C30")

    Jump("loc_30F0")

    label("loc_2C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2CDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C99")

    #C0108
    ChrTalk(
        0xC,
        (
            "我们现在要去开个\x01",
            "关于新剧目公演的会议……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        "现在开始就要忙碌起来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD5")

    label("loc_2C99")


    #C0110
    ChrTalk(
        0xC,
        (
            "诸位。\x01",
            "今天辛苦大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xC,
        "回去的路上请注意安全。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2CD5")

    Jump("loc_30F0")

    label("loc_2CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_2D4E")

    #C0112
    ChrTalk(
        0xC,
        (
            "哎呀……\x01",
            "各位找剧团长或伊莉娅小姐\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "她现在正在正面的\x01",
            "大厅里排练，\x01",
            "请向里面直走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F0")

    label("loc_2D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E22")

    #C0114
    ChrTalk(
        0xC,
        (
            "这次是『炎之舞姬』伊莉娅小姐出演的\x01",
            "第五部大型剧目……\x01",
            "会引起骚动也在情理之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "其实我也是\x01",
            "伊莉娅小姐的崇拜者。\x01",
            "所以才会到这里来工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        (
            "剧团成员和职员中\x01",
            "也有很多像我这样的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F3C")

    label("loc_2E22")


    #C0117
    ChrTalk(
        0xC,
        (
            "彩虹剧团大约\x01",
            "一年发表一部\x01",
            "新剧目……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "根据作品的不同，有时也会间隔一年半左右，\x01",
            "并没有特别固定的发表日期。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "所以，每当有新剧目发表的时候，\x01",
            "都会引起一阵骚动。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "这次是『炎之舞姬』伊莉娅小姐\x01",
            "自出道以来，参与的\x01",
            "第五部大型剧目……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xC,
        (
            "所以，会引起骚动\x01",
            "也不足为奇吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F3C")

    Jump("loc_30F0")

    label("loc_2F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_30BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FBF")

    #C0122
    ChrTalk(
        0xC,
        (
            "偏偏在这种时期，\x01",
            "发生了恐吓信事件……\x01",
            "真是令人困扰啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "希望能尽早证实\x01",
            "这只是一场恶作剧而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B8")

    label("loc_2FBF")


    #C0124
    ChrTalk(
        0xC,
        (
            "偏偏在新剧公开之前的这种特殊时期，\x01",
            "发生了恐吓信事件……\x01",
            "真是令人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xC,
        (
            "希望能尽早证实\x01",
            "这只是一场恶作剧而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "总之，已经跟全体成员\x01",
            "强调过了，\x01",
            "让他们提供全方位的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        (
            "如果有什么不明白的地方，\x01",
            "请不要客气，尽管去问他们就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_30B8")

    Jump("loc_30F0")

    label("loc_30BD")


    #C0128
    ChrTalk(
        0xC,
        (
            "诸位，\x01",
            "欢迎光临彩虹剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        "请前往大厅吧。\x02",
    )

    CloseMessageWindow()

    label("loc_30F0")

    TalkEnd(0xC)
    Return()

    # Function_11_2208 end

    def Function_12_30F4(): pass

    label("Function_12_30F4")

    Call(0, 11)
    Return()

    # Function_12_30F4 end

    def Function_13_30F8(): pass

    label("Function_13_30F8")


    #C0130
    ChrTalk(
        0xC,
        (
            "修利小姐\x01",
            "是新加入的成员……\x01",
            "真是个很勤奋的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "学东西学得也很快，\x01",
            "最重要的是积极性非常高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        (
            "虽然她似乎还没打算走上\x01",
            "演员这条道路……\x01",
            "总之，她能来这里，真是帮了大忙呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 7)
    Return()

    # Function_13_30F8 end

    def Function_14_31B5(): pass

    label("Function_14_31B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_32AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_32A2")

    #C0133
    ChrTalk(
        0x8,
        (
            "#1703F白天的演出要推迟到下午四点才开始……\x01",
            "一定要在那之前，排练到完美水准。\x02\x03",

            "#1700F没问题，我们的成员全都是专业水平的。\x01",
            "肯定能顺利完成演出。\x02\x03",

            "#1709F只彩排了一次，就直接上台表演……\x01",
            "嗯——真让人热血沸腾啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A5")

    label("loc_32A2")

    Call(0, 15)

    label("loc_32A5")

    Jump("loc_347F")

    label("loc_32AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3329")

    #C0134
    ChrTalk(
        0x8,
        (
            "#1706F卡雷利亚小姐从以前开始\x01",
            "就一直是这么啰嗦～\x02\x03",

            "#1700F算了，没关系。\x01",
            "不管怎么说，排练时\x01",
            "我肯定不会迟到的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_347F")

    label("loc_3329")


    #C0135
    ChrTalk(
        0x8,
        (
            "#1706F（打呵欠）呼啊～……\x02\x03",

            "#1705F哎呀，这不是警察弟弟嘛，\x01",
            "早啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#0012F伊、伊莉娅小姐。\x01",
            "你看起来好像挺困倦的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "#1706F嗯～今天早上\x01",
            "睡了一个小小的～懒觉。\x02\x03",

            "#1700F……啊，不用担心。\x01",
            "练习时我是不会懈怠的。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#0105F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0301F（这可是伊莉娅小姐私下\x01",
            "  不为人知的真实一面呢……）\x02\x03",

            "#0309F（嘿嘿～感觉赚到了呢！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_347F")

    TalkEnd(0xFE)
    Return()

    # Function_14_31B5 end

    def Function_15_3483(): pass

    label("Function_15_3483")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0140
    ChrTalk(
        0xD,
        (
            "哎呀呀，\x01",
            "好不容易把剧本调整好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xD,
        (
            "因为伊莉娅不肯妥协，\x01",
            "所以比预计中多花了一点时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#1706F#11P因为我绝对不想\x01",
            "让这一场戏的水准下滑嘛。\x02\x03",

            "#1702F排练的时候我也很努力，\x01",
            "这种程度不是理所当然的嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xD,
        (
            "就算如此，我也觉得你有点\x01",
            "太固执了……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xD,
        (
            "不过呢……只有今天日场的公演需要推迟，\x01",
            "也算是幸运的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xD,
        (
            "没有多少时间了，\x01",
            "立刻开始彩排吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        "#1709F#11P嗯！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        (
            "#0202F（虽然遇到些挫折，\x01",
            "  不过总算是顺利进行了。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_3483 end

    def Function_16_364D(): pass

    label("Function_16_364D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36E1")
    Jump("loc_372B")

    label("loc_36E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3701")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_372B")

    label("loc_3701")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3721")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_372B")

    label("loc_3721")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_372B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_37AD")

    #C0148
    ChrTalk(
        0x15,
        (
            "#6102F今天应该能把那一场戏\x01",
            "演得再到位一点……\x02\x03",

            "#6109F好啦，全力以赴吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F4")

    label("loc_37AD")


    #C0149
    ChrTalk(
        0x15,
        "#6105F啊呀，这不是警察弟弟和大家嘛。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#0002F晚上好，伊莉娅小姐。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#0302F现在要开始演出了吗？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x15,
        (
            "#6104F嗯，是啊。\x01",
            "客人们就快要入场了吧。\x02\x03",

            "#6102F下次应该能把那一场戏\x01",
            "演得更到位一点……\x02\x03",

            "#6109F好啦，全力以赴吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        (
            "#0109F（呵呵，\x01",
            "  伊莉娅小姐还是老样子呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        (
            "#0204F（是啊……\x01",
            "  让人有种莫名的安心感。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_38F4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_364D end

    def Function_17_38FC(): pass

    label("Function_17_38FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_39C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_39C0")

    #C0155
    ChrTalk(
        0x9,
        (
            "#1802F尼克鲁先生最近似乎在某处\x01",
            "进行特训……\x01",
            "实力进步了不少呢。\x02\x03",

            "#1806F这虽然不是什么坏事，\x01",
            "可是他连性格也变了。\x02\x03",

            "#1808F跟以前相比，简直判若两人，\x01",
            "让人有点担心呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C3")

    label("loc_39C0")

    Call(0, 18)

    label("loc_39C3")

    Jump("loc_407E")

    label("loc_39C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_3B27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A55")

    #C0156
    ChrTalk(
        0x9,
        (
            "#6202F最近，我在观众面前表演的时候，\x01",
            "总算不会像以前那么紧张了。\x02\x03",

            "#6209F呵呵，但肯定还没有伊莉娅小姐\x01",
            "那么厉害哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B22")

    label("loc_3A55")


    #C0157
    ChrTalk(
        0x9,
        (
            "#6202F啊，大家来了啊！\x02\x03",

            "难道是来观看\x01",
            "表演的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0012F不是……\x01",
            "虽然我们十分想看……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        (
            "#0102F我们要到这附近办点事，\x01",
            "只是顺便过来打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "#6209F呵呵，这样啊。\x01",
            "都这么晚了，真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3B22")

    Jump("loc_407E")

    label("loc_3B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3D06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 4)), scpexpr(EXPR_END)), "loc_3BA1")

    #C0161
    ChrTalk(
        0x9,
        (
            "#1802F从明天开始，\x01",
            "就是最后的排练了。\x02\x03",

            "#1804F每天都有彩排……\x01",
            "我也得调整好心态，\x01",
            "努力加油了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D01")

    label("loc_3BA1")


    #C0162
    ChrTalk(
        0x9,
        "#1803F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#0005F莉夏……？\x01",
            "怎么了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 750)

    #C0164
    ChrTalk(
        0x9,
        (
            "#1805F啊，没事……\x02\x03",

            "#1806F预演也已经临近了，\x01",
            "感觉稍微有点紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        "#0300F说起来，只剩下一周左右了吧。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "#1802F是的，从明天开始，\x01",
            "就是最后的排练了。\x02\x03",

            "#1804F……我也得调整好心态，\x01",
            "努力加油了。\x02\x03",

            "#1808F为了不在排练时\x01",
            "拖大家的后腿，\x01",
            "必须要好好努力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x91, 4)

    label("loc_3D01")

    Jump("loc_407E")

    label("loc_3D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 3)), scpexpr(EXPR_END)), "loc_3DB8")

    #C0167
    ChrTalk(
        0x9,
        (
            "#1806F其实，我对这次的演出\x01",
            "完全没有自信……\x02\x03",

            "#1802F但伊莉娅小姐\x01",
            "说我很有才能，\x01",
            "所以我想试着去相信这些话。\x02\x03",

            "#1804F……但我的练习还是很不够，\x01",
            "总是拖大家的后腿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3DB8")


    #C0168
    ChrTalk(
        0x9,
        (
            "#1805F啊，大家都来了啊……\x02\x03",

            "#1806F不好意思，我忙着准备排练，\x01",
            "一直慌慌忙忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#0002F哈哈，好像很忙呢。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x104,
        "#0302F毕竟是众所瞩目的超级新人嘛。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "#1809F啊哈哈……\x02\x03",

            "#1810F……其实我\x01",
            "原本并没有进入\x01",
            "剧团的打算……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x102,
        "#0105F哎呀……是这样的吗？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        (
            "#1802F是的，只是想看一次远近驰名的\x01",
            "彩虹剧团的表演而已。\x02\x03",

            "#1806F在参观公开排练的时候，\x01",
            "偶然间被伊莉娅小姐\x01",
            "注意到了。\x02\x03",

            "『你是很有才能的！』\x01",
            "……她当时就是这样说的，\x01",
            "然后就强行把我拉进剧团了。\x02",
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
    Sleep(1000)

    #C0174
    ChrTalk(
        0x103,
        "#0206F……那情景，似乎能想象得出来。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#0012F哈哈……\x01",
            "她真是个强硬的人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 3)

    label("loc_407E")

    TalkEnd(0xFE)
    Return()

    # Function_17_38FC end

    def Function_18_4082(): pass

    label("Function_18_4082")

    OP_4B(0x9, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0176
    ChrTalk(
        0x9,
        (
            "#1806F那个，普莉埃小姐……\x01",
            "关于尼克鲁先生的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x12,
        (
            "是啊，我也觉得\x01",
            "十分奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x12,
        "因为跟以前相比，简直就是判若两人嘛。\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        "#1808F………………………………\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#0005F那个……发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x0, 750)
    TurnDirection(0x12, 0x0, 750)
    Sleep(750)

    #C0181
    ChrTalk(
        0x12,
        "哎呀，是警察啊。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x12,
        (
            "其实也没什么大不了的，\x01",
            "就是尼克鲁稍微有点奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "#1806F尼克鲁先生最近似乎在某处\x01",
            "进行特训……\x02\x03",

            "在技巧与表现力方面，\x01",
            "都有了飞跃般的提高……\x02\x03",

            "#1808F但是，他的样子有些奇怪，\x01",
            "总觉得，就像是变了个人一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x104,
        (
            "#0301F哎……？\x01",
            "像变了个人一样吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#0103F我听说，有一些人\x01",
            "确实会出现这样的情况……\x02\x03",

            "#0100F一晚上不见，第二天就像变了个人一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "#1804F是啊。\x01",
            "要是有什么契机，出现改变倒也正常……\x02\x03",

            "#1810F……尼克鲁先生或许是\x01",
            "找到了什么窍门吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x12, 0)
    TurnDirection(0x12, 0x9, 0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0xCE, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_18_4082 end

    def Function_19_437E(): pass

    label("Function_19_437E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_43EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_43E4")

    #C0187
    ChrTalk(
        0xF,
        (
            "出演王子的我，\x01",
            "却要兼演乞丐……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xF,
        (
            "呜呜，太悲惨了……\x01",
            "实在无法接受。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E7")

    label("loc_43E4")

    Call(0, 20)

    label("loc_43E7")

    Jump("loc_4767")

    label("loc_43EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_444A")

    #C0189
    ChrTalk(
        0xF,
        (
            "尼克鲁近来\x01",
            "很热衷于练习……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xF,
        "我本以为这是个好现象，结果却……\x02",
    )

    CloseMessageWindow()
    Jump("loc_44D6")

    label("loc_444A")


    #C0191
    ChrTalk(
        0xF,
        (
            "尼克鲁那家伙，最近似乎\x01",
            "一直练习到深夜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xF,
        (
            "……他突然间变得如此积极，\x01",
            "我也觉得有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xF,
        (
            "可恶……怎么突然就\x01",
            "没影了啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_44D6")

    Jump("loc_4767")

    label("loc_44DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_45CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4532")

    #C0194
    ChrTalk(
        0xF,
        (
            "尼克鲁那家伙简直像是变了一个人啊，\x01",
            "竟然能练习\x01",
            "那么长时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C8")

    label("loc_4532")


    #C0195
    ChrTalk(
        0xF,
        (
            "你不觉得尼克鲁的演技\x01",
            "最近突然提升了很多吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xF,
        (
            "之前还有些拖泥带水，\x01",
            "但现在简直像是变了一个人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xF,
        (
            "呵呵……他也许是斩断了\x01",
            "心中的杂念吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_45C8")

    Jump("loc_4767")

    label("loc_45CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4671")

    #C0198
    ChrTalk(
        0xF,
        (
            "目前没有一般演出。\x01",
            "为了给新剧目做准备，\x01",
            "正在紧张地进行排练。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xF,
        (
            "要是不小心一点的话，\x01",
            "等到正式上场表演的时候，\x01",
            "衣服也许就会被弄得破破烂烂的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4767")

    label("loc_4671")


    #C0200
    ChrTalk(
        0xF,
        "怎么样啊，我这一身闪闪发亮的王子服装？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xF,
        (
            "呵呵，在新剧目『金之太阳、银之月』中，\x01",
            "本大人将要扮演王子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xF,
        (
            "……不过，要是彩排时太过兴奋，\x01",
            "到正式上场表演的时候，衣服可能就会开线了。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xF,
        (
            "因为在彩虹剧团的演出中，\x01",
            "运动量都是相当大的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4767")

    TalkEnd(0xFE)
    Return()

    # Function_19_437E end

    def Function_20_476B(): pass

    label("Function_20_476B")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0204
    ChrTalk(
        0xF,
        (
            "喂喂，我的戏份\x01",
            "怎么变少了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x10,
        (
            "我的戏份变多了……\x01",
            "大概是要给幕间换装\x01",
            "多争取一些时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xF,
        (
            "哎？我还要趁那段时间换衣服，\x01",
            "扮演乞丐的角色？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xF,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0208
    ChrTalk(
        0xF,
        "这不是真的吧……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_20_476B end

    def Function_21_4867(): pass

    label("Function_21_4867")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48FB")
    Jump("loc_4945")

    label("loc_48FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_491B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4945")

    label("loc_491B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_493B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4945")

    label("loc_493B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4945")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49EE")
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)

    #C0209
    ChrTalk(
        0x16,
        (
            "说起来，尼克鲁那家伙\x01",
            "昨天展示了一次惊人的特技表演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x16,
        (
            "那家伙原来是那么喜欢\x01",
            "吸引别人眼球的人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    Jump("loc_4BC2")

    label("loc_49EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4A86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4A7E")
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)

    #C0211
    ChrTalk(
        0x16,
        (
            "哈哈～\x01",
            "果然还是没自信吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x16,
        (
            "头号男演员果然\x01",
            "还是非本大人莫属啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x10,
        (
            "哼……你只会说些蠢话啊，\x01",
            "尤金。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    Jump("loc_4A81")

    label("loc_4A7E")

    Call(0, 22)

    label("loc_4A81")

    Jump("loc_4BC2")

    label("loc_4A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4B24")

    #C0214
    ChrTalk(
        0x16,
        (
            "恐吓信对于大明星来说，\x01",
            "并不算什么罕见的东西吧。\x01",
            "本人也收到过好几回了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x16,
        (
            "呵，本人可是\x01",
            "『彩虹剧团的王子』尤金啊，\x01",
            "所以会被很多同性嫉恨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BC2")

    label("loc_4B24")


    #C0216
    ChrTalk(
        0x16,
        "啊，你们是警察？\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x16,
        (
            "哼，真是辛苦啦。\x01",
            "那种恶作剧竟然还要这么仔细地调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x16,
        (
            "恐吓信这种东西，\x01",
            "对于明星来说，实在是太常见了。\x01",
            "再调查也是白费力气啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4BC2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_4867 end

    def Function_22_4BCA(): pass

    label("Function_22_4BCA")

    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "青年男演员用熟练的动作\x01",
            "整理着同伴的头发。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0220
    ChrTalk(
        0x16,
        (
            "缇奥多尔，\x01",
            "这次的演出，咱们就来赌一赌如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x16,
        (
            "看看谁能吸引\x01",
            "更多的女客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x16,
        (
            "哼，对了。\x01",
            "就看在一周之内，\x01",
            "谁收到的情书更多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        "…………………………（一惊）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x16, 0x0, 0x14, 0x258, 0xBB8)
    Sleep(500)

    #C0224
    ChrTalk(
        0x16,
        "好痛啊……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x16,
        (
            "喂！发型师！\x01",
            "你在搞什么鬼！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x16)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_22_4BCA end

    def Function_23_4D2E(): pass

    label("Function_23_4D2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4D93")
    OP_4B(0xF, 0xFF)

    #C0226
    ChrTalk(
        0x10,
        "看来还需要再稍微彩排一下。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x10,
        (
            "尤金，别叹气了，\x01",
            "快来对台词。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_4D96")

    label("loc_4D93")

    Call(0, 20)

    label("loc_4D96")

    Jump("loc_50B0")

    label("loc_4D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4DD9")

    #C0228
    ChrTalk(
        0xFE,
        (
            "今天也有演出……\x01",
            "到底会怎样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4B")

    label("loc_4DD9")


    #C0229
    ChrTalk(
        0x10,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "出了这种事，\x01",
            "剧团成员的情绪也会受影响……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x10,
        "真担心会不会影响演出效果啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4E4B")

    Jump("loc_50B0")

    label("loc_4E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E93")
    OP_4B(0xF, 0xFF)

    #C0232
    ChrTalk(
        0x10,
        (
            "………………………………\x01",
            "真令人不爽……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_50B0")

    label("loc_4E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4ED9")
    OP_4B(0xF, 0xFF)

    #C0233
    ChrTalk(
        0x10,
        "……尤金，你很吵啊。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x10,
        "你影响我读书了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_50B0")

    label("loc_4ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4F3F")

    #C0235
    ChrTalk(
        0x10,
        "空闲时，果然还是读书最好啊。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x10,
        (
            "书是精神食粮……\x01",
            "你们平时也应该\x01",
            "尽量多读些书呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B0")

    label("loc_4F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4F86")

    #C0237
    ChrTalk(
        0x10,
        "……忘拿什么东西了吗？\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x10,
        (
            "剧团长应该\x01",
            "在大厅里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B0")

    label("loc_4F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4FE0")

    #C0239
    ChrTalk(
        0x10,
        "找莉夏有事吗？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x10,
        (
            "她应该在旁边的服装间，\x01",
            "你们可以过去找她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE3")

    label("loc_4FE0")

    Call(0, 22)

    label("loc_4FE3")

    Jump("loc_50B0")

    label("loc_4FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_504C")

    #C0241
    ChrTalk(
        0x10,
        (
            "…………………………\x01",
            "抱歉，我正在揣摩角色。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x10,
        (
            "如果你们打算喧哗，\x01",
            "请到外面去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B0")

    label("loc_504C")


    #C0243
    ChrTalk(
        0x10,
        "我没见过你们啊。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x10,
        "算了，无所谓……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x10,
        (
            "这里是演员的休息室。\x01",
            "既然进来了，就请保持安静。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_50B0")

    TalkEnd(0xFE)
    Return()

    # Function_23_4D2E end

    def Function_24_50B4(): pass

    label("Function_24_50B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_51A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5132")

    #C0246
    ChrTalk(
        0x12,
        (
            "尼克鲁终究\x01",
            "还是没有回来啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x12,
        (
            "……虽然很遗憾，但就像剧团长说的，\x01",
            "我们得振作起精神才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A4")

    label("loc_5132")


    #C0248
    ChrTalk(
        0x12,
        (
            "好不容易把\x01",
            "剧本给整理好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x12,
        (
            "但是，哎呀呀……\x01",
            "尤金似乎很辛苦啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x12,
        (
            "总之，得去通知\x01",
            "莉夏和塞利娜。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_51A4")

    Jump("loc_586B")

    label("loc_51A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5264")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_525C")
    OP_4B(0x9, 0xFF)

    #C0251
    ChrTalk(
        0x12,
        (
            "说起来，\x01",
            "那孩子在纪念庆典结束后，\x01",
            "连续好几天都行踪不明呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x12,
        (
            "嗯，在那几天里，\x01",
            "到底发生了什么事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        (
            "#1801F是啊……\x01",
            "他什么也没告诉我……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_525F")

    label("loc_525C")

    Call(0, 18)

    label("loc_525F")

    Jump("loc_586B")

    label("loc_5264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_52C7")

    #C0254
    ChrTalk(
        0x12,
        "尼克鲁似乎变得很自信了呢。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x12,
        (
            "他有段时间曾经十分失落，\x01",
            "姐姐我可是十分担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_52C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_53EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5364")

    #C0256
    ChrTalk(
        0x12,
        (
            "伊莉娅的那股豪爽劲头，\x01",
            "从某种意义上说，可以算是与生俱来的天性吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x12,
        (
            "嗯，那孩子从还是个新人的时候，\x01",
            "就已经展露出了不凡的一面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53E7")

    label("loc_5364")


    #C0258
    ChrTalk(
        0x12,
        (
            "伊莉娅真是的，\x01",
            "竟然在这种日子睡懒觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x12,
        (
            "呼，从她还是个新人的时候，\x01",
            "就一直都是这个样子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x12,
        "警察好像有点生气了啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_53E7")

    Jump("loc_586B")

    label("loc_53EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_545C")

    #C0261
    ChrTalk(
        0x12,
        "（嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x12,
        (
            "排练时期，后台是\x01",
            "禁止饮食的。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x12,
        (
            "唔，要是想吃零食的话，\x01",
            "就要趁现在啊～⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_545C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_55B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_54E5")

    #C0264
    ChrTalk(
        0x12,
        "别看剧团长那样子，其实他挺有能力的。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x12,
        (
            "不过，最近这些日子，\x01",
            "他被带进了伊莉娅小姐的步调里，\x01",
            "好像很辛苦呢⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AF")

    label("loc_54E5")


    #C0266
    ChrTalk(
        0x12,
        (
            "你不觉得剧团长是那种\x01",
            "深藏不露的类型吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x12,
        (
            "别看他平时那样，\x01",
            "其实可是一位身兼剧本与舞台监督\x01",
            "两项要务的剧作家呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x12,
        (
            "嗯，彩虹剧团的人气\x01",
            "可是那个人一手拉起来的。\x01",
            "所以说，他是个很有能力的人呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_55AF")

    Jump("loc_586B")

    label("loc_55B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 5)), scpexpr(EXPR_END)), "loc_56AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5614")

    #C0269
    ChrTalk(
        0x12,
        (
            "近些日子，莉夏\x01",
            "的演技也很有进步……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x12,
        "嗯，好期待明年这个时候啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AA")

    label("loc_5614")


    #C0271
    ChrTalk(
        0x12,
        (
            "嗯，明星可不止是\x01",
            "伊莉娅和我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x12,
        (
            "缇奥多尔和尤金\x01",
            "也是瓜分了女观众人气\x01",
            "的顶级明星啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x12,
        (
            "可千万不要小看我们\x01",
            "彩虹剧团这华丽的\x01",
            "演员阵容哦⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_56AA")

    Jump("loc_586B")

    label("loc_56AF")


    #C0274
    ChrTalk(
        0x104,
        (
            "#0305F啊……\x01",
            "这不是普莉埃小姐吗！\x02\x03",

            "#0309F『神秘的歌姬』普莉埃……\x01",
            "幻想曲的大明星！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x12,
        "哎呀，您是我的支持者吗？\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x12,
        (
            "真是太抱歉了，我竟然穿着这种\x01",
            "毫无魅力的朴素练习服与您会面。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#0300F哪里哪里～\x01",
            "我是完全不在意啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x12,
        "嗯，但是我却有点在意哦。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x12,
        (
            "另·外·呢。\x01",
            "在后台请保持安静哦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        "#0300F好，抱歉呢！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x103,
        (
            "#0211F（兰迪前辈还真是个\x01",
            "　好对付的人呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 5)

    label("loc_586B")

    TalkEnd(0xFE)
    Return()

    # Function_24_50B4 end

    def Function_25_586F(): pass

    label("Function_25_586F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_592E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_58D1")

    #C0282
    ChrTalk(
        0x13,
        (
            "莉夏总是把东西\x01",
            "落在家里。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x13,
        (
            "真是的，她在这方面\x01",
            "总是粗心大意的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5929")

    label("loc_58D1")


    #C0284
    ChrTalk(
        0x13,
        (
            "莉夏可真是的，\x01",
            "又回家去取\x01",
            "忘带的东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x13,
        (
            "那孩子在这方面\x01",
            "总是粗心大意的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_5929")

    Jump("loc_5D14")

    label("loc_592E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_59B3")

    #C0286
    ChrTalk(
        0x13,
        (
            "我注意到了尼克鲁的状态有所异常，\x01",
            "却没有好好听他说话。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x13,
        (
            "我这种冷僻的态度……\x01",
            "也许实在是太过分了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A3B")

    label("loc_59B3")


    #C0288
    ChrTalk(
        0x13,
        (
            "……尼克鲁最近一段时间的\x01",
            "样子确实很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x13,
        (
            "我明明已经察觉到了，\x01",
            "却一直都装作没看到……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x13,
        (
            "没想到，\x01",
            "事情竟然会变成这样……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_5A3B")

    Jump("loc_5D14")

    label("loc_5A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5B67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5AC0")

    #C0291
    ChrTalk(
        0x13,
        (
            "能得到伊莉娅小姐的认同，\x01",
            "是我最大的梦想。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x13,
        (
            "虽然暂时被莉夏\x01",
            "抛在了后面。\x01",
            "但我可不想永远输下去啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B62")

    label("loc_5AC0")


    #C0293
    ChrTalk(
        0x13,
        (
            "我是因为憧憬\x01",
            "伊莉娅小姐，才会接受\x01",
            "彩虹剧团面试的。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x13,
        (
            "虽然这次被莉夏\x01",
            "抛在了后面，\x01",
            "但我是不会永远输下去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x13,
        (
            "我一定要努力练习，\x01",
            "争取有朝一日超过她。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_5B62")

    Jump("loc_5D14")

    label("loc_5B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5C03")

    #C0296
    ChrTalk(
        0x13,
        (
            "对莉夏的提拔是特例中的特例。\x01",
            "这也正能看出她的才能有多么惊人。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x13,
        (
            "既然如此，就一定要让表演完美成功啊。\x01",
            "……否则，我是绝对不会原谅她的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D14")

    label("loc_5C03")


    #C0298
    ChrTalk(
        0x13,
        (
            "莉夏只是个\x01",
            "刚加入彩虹剧团的\x01",
            "新人而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x13,
        (
            "突然间就被提拔为二号主演，\x01",
            "可以算是特例中的特例了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x13)

    #C0300
    ChrTalk(
        0x13,
        (
            "不过，这也是她\x01",
            "努力练习的成果，\x01",
            "虽然我并不打算对此多做评论。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x13,
        (
            "但她可是后来居上，超越了我这个前辈的天才。\x01",
            "要是演砸了，我可不会原谅她的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_5D14")

    TalkEnd(0xFE)
    Return()

    # Function_25_586F end

    def Function_26_5D18(): pass

    label("Function_26_5D18")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DAC")
    Jump("loc_5DF6")

    label("loc_5DAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5DCC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DF6")

    label("loc_5DCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DEC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DF6")

    label("loc_5DEC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DF6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_60CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5E91")

    #C0302
    ChrTalk(
        0x17,
        (
            "莉夏在独自一人的时候，\x01",
            "时常会显露出\x01",
            "没有自信的表情。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        (
            "真是的……\x01",
            "总觉得有些令人火大。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60C9")

    label("loc_5E91")


    #C0304
    ChrTalk(
        0x17,
        (
            "莉夏在独自一人的时候，\x01",
            "时常会显露出\x01",
            "没有自信的表情。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x17,
        (
            "真是的……\x01",
            "她可是连伊莉娅小姐都认可的\x01",
            "一流演员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x17,
        (
            "竟然摆出那种垂头丧气的模样，\x01",
            "到底在想什么啊！\x01",
            "给我多拿出点自信来！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8D")

    #C0307
    ChrTalk(
        0x101,
        (
            "#0006F那个，这种话最好还是\x01",
            "对她本人说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6063")

    label("loc_5F8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FDA")

    #C0308
    ChrTalk(
        0x102,
        (
            "#0106F那个，这种问题\x01",
            "还是当面说给\x01",
            "她本人听比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6063")

    label("loc_5FDA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6022")

    #C0309
    ChrTalk(
        0x103,
        (
            "#0206F……这种事情，\x01",
            "还是应该直接找当事人说吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6063")

    label("loc_6022")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6063")

    #C0310
    ChrTalk(
        0x104,
        (
            "#0306F那个，这种话最好还是应该\x01",
            "当面跟她说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6063")

    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0311
    ChrTalk(
        0x17,
        "这、这个……\x02",
    )

    CloseMessageWindow()
    OP_64(0x17)

    #C0312
    ChrTalk(
        0x17,
        (
            "咳咳，我可是有威严的前辈。\x01",
            "这种话怎么能说得出口嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_60C9")

    Jump("loc_61D1")

    label("loc_60CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_616D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6128")

    #C0313
    ChrTalk(
        0x17,
        (
            "警察来了，\x01",
            "排练也无法进行……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x17,
        "唉，真是让人提不起精神啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6168")

    label("loc_6128")


    #C0315
    ChrTalk(
        0x17,
        (
            "据说那封恐吓信\x01",
            "有可能是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x17,
        "稍微有点不安啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_6168")

    Jump("loc_61D1")

    label("loc_616D")


    #C0317
    ChrTalk(
        0x17,
        (
            "听说父亲和母亲\x01",
            "也会前来观看这次的新剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x17,
        (
            "……我可绝对不能演砸啊。\x01",
            "必须要继续努力练习才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_5D18 end

    def Function_27_61D9(): pass

    label("Function_27_61D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_62B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_624C")

    #C0319
    ChrTalk(
        0x11,
        "大家都被我的演技震惊了呢。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x11,
        (
            "哈哈哈，感觉真不错啊。\x01",
            "总算让他们见识到我的才能了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62AF")

    label("loc_624C")


    #C0321
    ChrTalk(
        0x11,
        (
            "哈哈哈……！\x01",
            "今天的彩排也很完美！\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "状态实在是太好了……\x01",
            "就算对手是莉夏，我也不会输的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_62AF")

    Jump("loc_64F3")

    label("loc_62B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_632E")

    #C0323
    ChrTalk(
        0x11,
        "我的字典里已经没有失败二字了。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x11,
        (
            "对于训练量，我也有自信绝不会输给任何人。\x01",
            "好了，开始干吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6371")

    label("loc_632E")


    #C0325
    ChrTalk(
        0x11,
        (
            "……好了，\x01",
            "今天的演出也要加油啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x11,
        "#4S哈哈哈哈哈……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6371")

    Jump("loc_64F3")

    label("loc_6376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_63EC")

    #C0327
    ChrTalk(
        0x11,
        (
            "普莉埃小姐在彩虹剧团里\x01",
            "是如同标志性人物\x01",
            "一般的大明星。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x11,
        (
            "她能跟我说话，\x01",
            "真令人开心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_648D")

    label("loc_63EC")


    #C0329
    ChrTalk(
        0x11,
        (
            "普莉埃小姐刚才\x01",
            "来鼓励我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x11,
        "说我不用因为演出失误的事情而过于沮丧。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x11,
        (
            "呼……不知怎么回事，\x01",
            "心情似乎稍微有点好转了。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x11,
        "前辈的话果然很有效果啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_648D")

    Jump("loc_64F3")

    label("loc_6492")


    #C0333
    ChrTalk(
        0xFE,
        "呼，今天的排练也是失误不断啊。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        "好不容易有个角色可演……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "我果然还是\x01",
            "没有才能吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64F3")

    TalkEnd(0xFE)
    Return()

    # Function_27_61D9 end

    def Function_28_64F7(): pass

    label("Function_28_64F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_65D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_655C")
    OP_4B(0x12, 0xFF)

    #C0336
    ChrTalk(
        0xA,
        (
            "这下可得拜托他们\x01",
            "快点换衣服了……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xA,
        "换装顺序也得好好决定。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_65D3")

    label("loc_655C")

    OP_4B(0x12, 0xFF)

    #C0338
    ChrTalk(
        0xA,
        "啊呀，能让我也看看吗？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xA,
        (
            "嗯嗯……换装顺序\x01",
            "也有调整呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xA,
        (
            "时间也有点紧张，\x01",
            "不快点换装可不行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x12, 0xFF)

    label("loc_65D3")

    Jump("loc_7074")

    label("loc_65D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_66E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6658")

    #C0341
    ChrTalk(
        0xA,
        (
            "尼克鲁离奇失踪，\x01",
            "大家似乎也开始感到不安了……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xA,
        (
            "这也没办法啊……\x01",
            "我们这一行的压力\x01",
            "本来就很大……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66DE")

    label("loc_6658")

    OP_4B(0x10, 0xFF)

    #C0343
    ChrTalk(
        0x10,
        (
            "卡雷利亚小姐，\x01",
            "我来负责尤金的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x10,
        "拜托您了，别让塞利娜感到不安。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xA,
        (
            "嗯，我知道了，\x01",
            "我暂时会陪在她身边的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x10, 0xFF)

    label("loc_66DE")

    Jump("loc_7074")

    label("loc_66E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6757")

    #C0346
    ChrTalk(
        0xA,
        (
            "（尼克鲁先生……最近的\x01",
            "  态度变得相当奇怪……）\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xA,
        (
            "（有了自信之后，\x01",
            "  就会变成那种样子吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7074")

    label("loc_6757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_67F8")
    SetChrSubChip(0x15, 0x2)

    #C0348
    ChrTalk(
        0xA,
        (
            "真是的……\x01",
            "这样的话，恐怕就赶不上\x01",
            "演出时间了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x15,
        (
            "#6104F没事没事，还有十分钟啦。\x02\x03",

            "#6102F我们再加快一点速度\x01",
            "就行啦，卡雷利亚小姐！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Jump("loc_7074")

    label("loc_67F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6869")

    #C0350
    ChrTalk(
        0xA,
        (
            "尼克鲁先生在昨天的公演中\x01",
            "出现了很严重的失误。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xA,
        (
            "……看他的样子，\x01",
            "肯定很失落吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68FE")

    label("loc_6869")


    #C0352
    ChrTalk(
        0xA,
        (
            "尼克鲁先生在昨天的公演中\x01",
            "出现了很严重的失误。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xA,
        (
            "随后就彻底陷入慌乱，\x01",
            "连台词都忘了……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xA,
        (
            "……看他的样子，\x01",
            "肯定很失落吧。\x01",
            "真令人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_68FE")

    Jump("loc_7074")

    label("loc_6903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_69DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6925")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6972")

    #C0355
    ChrTalk(
        0xA,
        (
            "表演也快要\x01",
            "进入高潮部分了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        "好了，得快点打扫干净。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69D5")

    label("loc_6972")


    #C0357
    ChrTalk(
        0xA,
        (
            "刚才从服装间里传来了\x01",
            "咯噔的声音……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xA,
        "算了，可能是错觉吧。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xA,
        (
            "我似乎总有点\x01",
            "神经过敏。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_69D5")

    Jump("loc_7074")

    label("loc_69DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_6A51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69FC")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_69FC")


    #C0360
    ChrTalk(
        0xA,
        (
            "哎呀，又把零食\x01",
            "藏在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xA,
        (
            "普莉埃小姐总是\x01",
            "改不掉这个坏习惯呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7074")

    label("loc_6A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_6B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A73")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6AD5")

    #C0362
    ChrTalk(
        0xA,
        (
            "接下来就是关键时刻了……\x01",
            "我现在也只能祈祷而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xA,
        (
            "至少先把房间\x01",
            "打扫一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B2A")

    label("loc_6AD5")


    #C0364
    ChrTalk(
        0xA,
        (
            "演员们都去\x01",
            "后台准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xA,
        (
            "接下来就是关键时刻了……\x01",
            "我也会祈祷演出顺利的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_6B2A")

    Jump("loc_7074")

    label("loc_6B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6B8F")

    #C0366
    ChrTalk(
        0xA,
        (
            "呵呵，马上就要到新剧开演的时刻了，\x01",
            "我也要给那些孩子们做好幕后工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C41")

    label("loc_6B8F")


    #C0367
    ChrTalk(
        0xA,
        (
            "这里的演员们的个性都太强了，\x01",
            "真是不好相处啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xA,
        (
            "但是，大家在面对舞台的时候，\x01",
            "又都能表现出自己最真实的一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xA,
        (
            "在幕后支援那些认真的孩子们……\x01",
            "也是件挺不错的工作呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_6C41")

    Jump("loc_7074")

    label("loc_6C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6D97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6C89")

    #C0370
    ChrTalk(
        0xA,
        (
            "头号明星竟然\x01",
            "搞得这么邋遢，\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D92")

    label("loc_6C89")

    OP_4B(0x8, 0xFF)

    #C0371
    ChrTalk(
        0xA,
        (
            "唉，伊莉娅小姐……\x01",
            "偶尔会大摇大摆地迟到。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xA,
        (
            "她这种粗叶大叶的性格，\x01",
            "从来都没有过一点改变！\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#1703F说得是啊～……\x02\x03",

            "#1700F……啊，卡雷利亚小姐。\x01",
            "我这就要去排练了，\x01",
            "来帮忙准备一下服装吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xA,
        (
            "又是这种样子……\x01",
            "剧团长每天都很辛苦，\x01",
            "真令人同情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x8, 0xFF)

    label("loc_6D92")

    Jump("loc_7074")

    label("loc_6D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6DF0")

    #C0375
    ChrTalk(
        0xA,
        (
            "普莉埃小姐……\x01",
            "只要一站在舞台上，\x01",
            "就像是完全变成了另一个人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E5A")

    label("loc_6DF0")

    OP_4B(0x12, 0xFF)

    #C0376
    ChrTalk(
        0xA,
        (
            "普莉埃小姐，换装后\x01",
            "请尽量避免饮食哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xA,
        (
            "作为服装设计师，\x01",
            "对这件事可不能视而不见。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x12, 0xFF)

    label("loc_6E5A")

    Jump("loc_7074")

    label("loc_6E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6EB4")

    #C0378
    ChrTalk(
        0xA,
        (
            "好了好了，男性就\x01",
            "赶紧出去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xA,
        (
            "莉夏这就要\x01",
            "换衣服了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F60")

    label("loc_6EB4")

    OP_4B(0x9, 0xFF)

    #C0380
    ChrTalk(
        0xA,
        (
            "好啦，莉夏，\x01",
            "快点把衣服换了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xA,
        (
            "衣服开线的地方，\x01",
            "我都已经重新缝好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x9,
        (
            "#1805F啊，真的……\x01",
            "补得真漂亮。\x02\x03",

            "#1800F真是太感谢您了，\x01",
            "卡雷利亚小姐！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x9, 0xFF)

    label("loc_6F60")

    Jump("loc_7074")

    label("loc_6F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6FEC")

    #C0383
    ChrTalk(
        0xA,
        (
            "在这个时期，\x01",
            "全剧团都很忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xA,
        (
            "又要调整服装设计的细节，\x01",
            "还要随时留意演员们的身体状况……\x01",
            "后勤工作也堆积如山啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7074")

    label("loc_6FEC")


    #C0385
    ChrTalk(
        0xA,
        (
            "新剧目的排练进程\x01",
            "马上就要进入到收尾阶段了。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xA,
        (
            "要调整服装设计的细节，\x01",
            "还要随时留意演员们的身体状况……\x01",
            "后勤工作也堆积如山啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_7074")

    TalkEnd(0xFE)
    Return()

    # Function_28_64F7 end

    def Function_29_7078(): pass

    label("Function_29_7078")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_70CB")

    #C0387
    ChrTalk(
        0xE,
        (
            "夜场的演出\x01",
            "马上就要开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "呵呵，\x01",
            "今天的客人也很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7116")

    label("loc_70CB")


    #C0389
    ChrTalk(
        0xE,
        (
            "哎呀，真是抱歉。\x01",
            "马上就要到开演时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        (
            "请您不要进入\x01",
            "后台哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_7116")

    TalkEnd(0xFE)
    Return()

    # Function_29_7078 end

    def Function_30_711A(): pass

    label("Function_30_711A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_721D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71D7")

    #C0391
    ChrTalk(
        0x101,
        (
            "#0005F咦……？\x01",
            "剧团里还有这样的孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        "……干什么，你们好像不是客人吧？\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "哼……无关人士\x01",
            "是禁止进入剧团的。\x01",
            "要是没票的话，就赶快回去吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Jump("loc_7218")

    label("loc_71D7")


    #C0394
    ChrTalk(
        0xFE,
        "……没有票的话就看不了表演哦。\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "我会在这里\x01",
            "认真检票的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7218")

    Jump("loc_73C6")

    label("loc_721D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_73C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7240")
    Call(0, 31)
    Jump("loc_73C6")

    label("loc_7240")


    #C0396
    ChrTalk(
        0xFE,
        (
            "……我在打扫卫生，\x01",
            "你有意见吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73C3")

    #C0397
    ChrTalk(
        0x101,
        (
            "#0012F哈哈……\x01",
            "还是一如既往地叛逆啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72E4")

    #C0398
    ChrTalk(
        0x102,
        "#0100F但好像已经渐渐习惯了这里的工作呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7365")

    label("loc_72E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7325")

    #C0399
    ChrTalk(
        0x103,
        "#0200F但好像也慢慢习惯了这里的工作呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7365")

    label("loc_7325")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7365")

    #C0400
    ChrTalk(
        0x104,
        "#0300F不过，好像也渐渐习惯了这里的工作吧。\x02",
    )

    CloseMessageWindow()

    label("loc_7365")


    #C0401
    ChrTalk(
        0xFE,
        (
            "哼、哼……\x01",
            "这种工作，谁都能做。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x153,
        (
            "#1111F（好漂亮的银色头发啊，\x01",
            "  是罗伊德的朋友吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C3")

    SetScenarioFlags(0x1, 3)

    label("loc_73C6")

    TalkEnd(0xFE)
    Return()

    # Function_30_711A end

    def Function_31_73CA(): pass

    label("Function_31_73CA")


    #C0403
    ChrTalk(
        0x101,
        (
            "#0005F咦……？\x01",
            "剧团里还有这样的孩子吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_743B")

    #C0404
    ChrTalk(
        0xFE,
        (
            "……你们是干什么的，\x01",
            "难道认识伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746C")

    label("loc_743B")


    #C0405
    ChrTalk(
        0xFE,
        (
            "……你们是干什么的，\x01",
            "难道认识伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_746C")


    #C0406
    ChrTalk(
        0xFE,
        (
            "哼……\x01",
            "无关人员禁止进入剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "就算认识伊莉娅小姐，\x01",
            "也别厚着脸皮进来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_31_73CA end

    def Function_32_74C2(): pass

    label("Function_32_74C2")

    TalkBegin(0xFE)

    #C0408
    ChrTalk(
        0xFE,
        (
            "我痛下决心，\x01",
            "买了Ｓ席的票……！\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "（心跳加速）……\x01",
            "不过，毕竟是准备求婚，\x01",
            "这点血本还是必须要下的！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_74C2 end

    def Function_33_7534(): pass

    label("Function_33_7534")

    TalkBegin(0xFE)

    #C0410
    ChrTalk(
        0xFE,
        (
            "他为我\x01",
            "买到票了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        "……而且还是在Ｓ席！\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "嗯，他有时候比我想象得\x01",
            "还要豪爽嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_7534 end

    def Function_34_7597(): pass

    label("Function_34_7597")

    TalkBegin(0xFE)

    #C0413
    ChrTalk(
        0xFE,
        (
            "妈妈，再不快点的话，\x01",
            "演出就要开始了哟！\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "要是错过了伊莉娅小姐的表演，\x01",
            "我会恨妈妈的！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_7597 end

    def Function_35_75FC(): pass

    label("Function_35_75FC")

    TalkBegin(0xFE)

    #C0415
    ChrTalk(
        0xFE,
        (
            "Ｂ区２排２８号……\x01",
            "位子是在左侧。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "好，出发吧。\x01",
            "马上就能欣赏到\x01",
            "彩虹剧团的演出了！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_75FC end

    def Function_36_765E(): pass

    label("Function_36_765E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1450, -5360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9730, 0)
    SetChrPos(0x104, -500, 0, -9930, 0)
    SetChrPos(0x8, 10000, 2400, 13900, 270)
    SetChrPos(0x9, 11000, 2400, 13500, 270)
    SetChrPos(0xB, 4500, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7772():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7772)

    def lambda_778C():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_778C)
    Sleep(50)

    def lambda_77A0():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77A0)

    def lambda_77BA():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_77BA)
    Sleep(50)

    def lambda_77CE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_77CE)

    def lambda_77E8():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_77E8)
    Sleep(50)

    def lambda_77FC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77FC)

    def lambda_7816():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7816)
    OP_68(0, 1450, -4360, 3000)
    SetCameraDistance(12000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0417
    ChrTalk(
        0x101,
        "#0005F#11P嗯……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(7680, 3950, 13870, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    OP_68(0, 3950, 13500, 5000)
    MoveCamera(33, 25, 0, 5000)
    SetCameraDistance(12920, 5000)
    BeginChrThread(0x8, 3, 0, 37)
    Sleep(800)

    #N0418
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1706F#11P莉夏可真是的。\x01",
            "我完全都不在意啊。\x02\x03",

            "#1702F想住多久\x01",
            "就住多久嘛。\x02",
        )
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0x9,
        "紫发的少女",
        (
            "#1805F#11P不、不不，不用了……\x02\x03",

            "#1809F请不用担心我。\x01",
            "我会去找一间合适又便宜的\x01",
            "出租公寓的。\x02\x03",

            "#1802F去市政厅的接待窗口\x01",
            "咨询一下就可以吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0420
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1702F#5P嗯，那应该是\x01",
            "最简单的办法。\x02\x03",

            "#1709F还可以顺便办理入户手续呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #N0421
    NpcTalk(
        0x9,
        "紫发的少女",
        (
            "#1809F#11P啊哈哈……是啊。\x02\x03",

            "#1810F真不好意思，\x01",
            "伊莉娅小姐不但要指导我练习，\x01",
            "还要教我这么多事情……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(150, 1450, -3940, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    OP_0D()

    #C0422
    ChrTalk(
        0x104,
        (
            "#0307F#11P啊，那不是……\x01",
            "伊莉娅·普拉提耶吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0005F#11P伊莉娅·普拉提耶？\x02\x03",

            "#0002F啊，以前只是在杂志上\x01",
            "看到过几次……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0x0, 400)
    TurnDirection(0xC, 0x0, 400)
    Sleep(300)

    #N0424
    NpcTalk(
        0xB,
        "男性",
        "哎呀，各位是……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_7C03():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7C03)
    Sleep(15)

    def lambda_7C13():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7C13)

    def lambda_7C20():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7C20)
    Sleep(12)

    def lambda_7C30():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7C30)
    OP_68(-120, 1450, -3060, 3000)
    MoveCamera(39, 26, 0, 3000)
    SetCameraDistance(12260, 3000)
    BeginChrThread(0xB, 1, 0, 38)
    Sleep(1000)

    def lambda_7C6B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C6B)
    Sleep(180)

    def lambda_7C7B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C7B)
    Sleep(240)

    def lambda_7C8B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C8B)
    Sleep(250)

    def lambda_7C9B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C9B)
    OP_6F(0x79)
    WaitChrThread(0xB, 1)

    #C0425
    ChrTalk(
        0xB,
        (
            "#5P十分抱歉，\x01",
            "彩虹剧团的演出\x01",
            "是从傍晚六点开始的……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xB,
        (
            "#5P如果各位是观众，\x01",
            "现在还请不要进入。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x101,
        (
            "#0006F#12P对、对不起，\x01",
            "我们没打招呼就擅自进来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        "#0102F#12P真是失礼了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 3)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_765E end

    def Function_37_7D7B(): pass

    label("Function_37_7D7B")


    def lambda_7D80():
        OP_97(0x8, 0xFFFFD6FC, 0x0, 0xFFFFFE70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7D80)

    def lambda_7D9A():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7D9A)
    Sleep(50)

    def lambda_7DAE():
        OP_97(0x9, 0xFFFFD6FC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7DAE)

    def lambda_7DC8():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7DC8)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x9, 750)
    Return()

    # Function_37_7D7B end

    def Function_38_7DE0(): pass

    label("Function_38_7DE0")

    OP_95(0xFE, -180, 0, -1760, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_38_7DE0 end

    def Function_39_7DFC(): pass

    label("Function_39_7DFC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -6360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16420, 0)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9730, 0)
    SetChrPos(0x104, -500, 0, -9930, 0)
    SetChrPos(0xB, 5120, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7EC0():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EC0)

    def lambda_7EDA():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EDA)
    Sleep(50)

    def lambda_7EEE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7EEE)

    def lambda_7F08():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F08)
    Sleep(50)

    def lambda_7F1C():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7F1C)

    def lambda_7F36():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7F36)
    Sleep(50)

    def lambda_7F4A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7F4A)

    def lambda_7F64():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7F64)
    OP_68(0, 1450, -4360, 3000)
    SetCameraDistance(17420, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7FF6():

        label("loc_7FF6")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_7FF6")

    QueueWorkItem2(0x0, 1, lambda_7FF6)

    def lambda_8008():

        label("loc_8008")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_8008")

    QueueWorkItem2(0x1, 1, lambda_8008)

    def lambda_801A():

        label("loc_801A")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_801A")

    QueueWorkItem2(0x2, 1, lambda_801A)

    def lambda_802C():

        label("loc_802C")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_802C")

    QueueWorkItem2(0x3, 1, lambda_802C)
    OP_95(0xB, 0, 0, -1760, 3000, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0429
    ChrTalk(
        0xB,
        (
            "十分抱歉，\x01",
            "彩虹剧团的演出\x01",
            "是从傍晚六点开始的……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xB,
        (
            "如果各位是观众，\x01",
            "现在还请不要进入。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0006F#2P对、对不起，\x01",
            "我们没打招呼就擅自进来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#0100F#2P（彩虹剧团……\x01",
            "  如此有名的剧团，如果没什么事的话，\x01",
            "  还是不要擅自进入比较好。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x67, 7)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_7DFC end

    def Function_40_8175(): pass

    label("Function_40_8175")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    OP_68(-400, 1450, -2870, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, -800, 0, -3050, 0)
    SetChrPos(0x102, 600, 0, -3050, 0)
    SetChrPos(0x103, -800, 0, -4180, 0)
    SetChrPos(0x104, 600, 0, -4180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8227")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -30, 0, -5290, 0)

    label("loc_8227")

    SetChrPos(0xB, -40, 0, -1140, 180)
    SetChrPos(0x14, 4670, 0, 3090, 90)
    BeginChrThread(0x14, 0, 0, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0433
    ChrTalk(
        0xB,
        (
            "诸位，\x01",
            "欢迎大驾光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xB,
        (
            "但是，十分抱歉。\x01",
            "伊莉娅小姐和莉夏小姐现在……\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        (
            "#0000F#2P对不起，\x01",
            "大家都在演出吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x104,
        (
            "#0300F#2P算了，也没什么大事，\x01",
            "以后有机会再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        "#0100F#2P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x103,
        "#0200F#2P抱歉，打扰了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xC8, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8367")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_8367")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_8175 end

    def Function_41_8374(): pass

    label("Function_41_8374")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(-400, 1450, -2870, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, -800, 0, -3050, 0)
    SetChrPos(0x102, 600, 0, -3050, 0)
    SetChrPos(0x103, -800, 0, -4180, 0)
    SetChrPos(0x104, 600, 0, -4180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8430")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -30, 0, -5290, 0)

    label("loc_8430")

    SetChrPos(0xB, -40, 0, -1140, 180)
    SetChrPos(0x14, 4670, 0, 3090, 90)
    BeginChrThread(0x14, 0, 0, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0439
    ChrTalk(
        0xB,
        (
            "诸位，\x01",
            "欢迎大驾光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xB,
        (
            "但是，十分抱歉。\x01",
            "伊莉娅小姐和莉夏小姐现在……\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        (
            "#0000F#2P对不起，\x01",
            "大家都在演出吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x104,
        (
            "#0300F#2P算了，也没什么大事，\x01",
            "以后有机会再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x102,
        "#0100F#2P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        "#0200F#2P抱歉打扰了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xC8, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_856E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_856E")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_8374 end

    def Function_42_857B(): pass

    label("Function_42_857B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xB, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    #C0445
    ChrTalk(
        0xB,
        (
            "支援科的诸位……\x01",
            "欢迎大驾光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        (
            "#0005F巴尔萨摩先生，\x01",
            "演出进行得怎么样了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xB,
        (
            "准备工作总算是全部就绪了，\x01",
            "现在正在上演白天那场因故推迟的演出呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xB,
        (
            "没有正式彩排，就直接公开演出，\x01",
            "我还是有点不安……\x01",
            "不过，看样子好像是没什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#0100F太好了……\x01",
            "看来演出并没有停止，\x01",
            "仍在照常进行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x103,
        "#0200F真不愧是超一流的演员。\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x104,
        (
            "#0301F总之，关于那个行踪不明的家伙，\x01",
            "到现在也没有任何线索。\x02\x03",

            "#0303F目前也只能期待\x01",
            "大家努力完成演出了。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xB,
        (
            "各位，真是不好意思，\x01",
            "尼克鲁的事情\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        (
            "#0000F嗯，交给我们吧，\x01",
            "我们一定会找到他的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xE7, 0)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_857B end

    def Function_43_885E(): pass

    label("Function_43_885E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88D1")
    TalkBegin(0xFF)

    #C0454
    ChrTalk(
        0x101,
        (
            "#0000F观众们似乎\x01",
            "开始大量进场了……\x02\x03",

            "我们会妨碍他们入场落座的，\x01",
            "还是不要进入正面大厅了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_88D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_8970")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_892B")

    #C0455
    ChrTalk(
        0x101,
        (
            "#0001F现在可不是看表演的时候……\x01",
            "赶快去右边的阶梯吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8968")

    label("loc_892B")


    #C0456
    ChrTalk(
        0x102,
        (
            "#0101F现在可不是看演出的时候……\x01",
            "必须赶快去右边的阶梯！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8968")

    TalkEnd(0xFF)
    Jump("loc_8A23")

    label("loc_8970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A23")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "窥视场内情况\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_89CC"),
        (1, "loc_8A1C"),
        (SWITCH_DEFAULT, "loc_8A21"),
    )


    label("loc_89CC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_89F1")
    SetScenarioFlags(0x5C, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8A17")

    label("loc_89F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_8A0B")
    SetScenarioFlags(0x5C, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8A17")

    label("loc_8A0B")

    SetScenarioFlags(0x5C, 3)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_8A17")

    Jump("loc_8A21")

    label("loc_8A1C")

    Jump("loc_8A21")

    label("loc_8A21")

    EventEnd(0x3)

    label("loc_8A23")

    Return()

    # Function_43_885E end

    def Function_44_8A24(): pass

    label("Function_44_8A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8ADD")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "窥视场内情况\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8A80"),
        (1, "loc_8AD6"),
        (SWITCH_DEFAULT, "loc_8ADB"),
    )


    label("loc_8A80")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x86, 3)
    ClearScenarioFlags(0x86, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_8AAB")
    SetScenarioFlags(0x5D, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8AD1")

    label("loc_8AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_8AC5")
    SetScenarioFlags(0x5C, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8AD1")

    label("loc_8AC5")

    SetScenarioFlags(0x5C, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_8AD1")

    Jump("loc_8ADB")

    label("loc_8AD6")

    Jump("loc_8ADB")

    label("loc_8ADB")

    EventEnd(0x3)

    label("loc_8ADD")

    Return()

    # Function_44_8A24 end

    def Function_45_8ADE(): pass

    label("Function_45_8ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B97")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "窥视场内情况\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8B3A"),
        (1, "loc_8B90"),
        (SWITCH_DEFAULT, "loc_8B95"),
    )


    label("loc_8B3A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x86, 2)
    ClearScenarioFlags(0x86, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_8B65")
    SetScenarioFlags(0x5D, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8B8B")

    label("loc_8B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_8B7F")
    SetScenarioFlags(0x5C, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8B8B")

    label("loc_8B7F")

    SetScenarioFlags(0x5C, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_8B8B")

    Jump("loc_8B95")

    label("loc_8B90")

    Jump("loc_8B95")

    label("loc_8B95")

    EventEnd(0x3)

    label("loc_8B97")

    Return()

    # Function_45_8ADE end

    def Function_46_8B98(): pass

    label("Function_46_8B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C4B")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "窥视场内情况\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8BF4"),
        (1, "loc_8C44"),
        (SWITCH_DEFAULT, "loc_8C49"),
    )


    label("loc_8BF4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_8C19")
    SetScenarioFlags(0x5D, 3)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8C3F")

    label("loc_8C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_8C33")
    SetScenarioFlags(0x5D, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_8C3F")

    label("loc_8C33")

    SetScenarioFlags(0x5D, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_8C3F")

    Jump("loc_8C49")

    label("loc_8C44")

    Jump("loc_8C49")

    label("loc_8C49")

    EventEnd(0x3)

    label("loc_8C4B")

    Return()

    # Function_46_8B98 end

    def Function_47_8C4C(): pass

    label("Function_47_8C4C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -91050, 0, 6720, 0)
    OP_68(-91310, 1500, 6690, 0)
    MoveCamera(29, 11, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    OP_74(0x1C, 0x1E)
    OP_70(0x1C, 0x0)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1C, 0x4)
    OP_71(0x1C, 0x19, 0x2D, 0x0, 0x20)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
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
    SetCameraDistance(19500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_71(0x1C, 0x32, 0x46, 0x0, 0x20)
    Sleep(800)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0457
    AnonymousTalk(
        0x8,
        "#1702F抱歉抱歉，久等啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女性的声音")

    #A0458
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──不，请别在意。\x02\x03",

            "你肯定又陪自己欣赏的新人\x01",
            "一直排练到了深夜吧。\x02\x03",

            "顺便还趁机嬉闹一番，\x01",
            "让剧团长看得目瞪口呆？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0459
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1709F……怎、怎么会呢～\x01",
            "怎么可能会有那种事啦～\x02\x03",

            "#1702F说、说起来，塞茜尔，你怎么了？\x02\x03",

            "这么晚还跟我联络，太少见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0460
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，那个……\x02\x03",

            "你送给我的票，\x01",
            "今天正好送到了……\x02\x03",

            "所以我想跟你道声谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0461
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1700F啊，是吗，已经收到了啊。\x02\x03",

            "#1704F嗯，虽然知道你也是个大忙人，\x01",
            "不过，如果有时间的话，可一定要来看哟。\x02\x03",

            "#1702F那天是纪念庆典的第一天，\x01",
            "肯定能请到假吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0462
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，我会努力的。\x02\x03",

            "不过，真是不好意思啊。\x02\x03",

            "正式公演的第一天……\x01",
            "而且还是两张Ｓ席的票。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0463
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1709F别在意，这也是\x01",
            "头牌女星的特权啊。\x02\x03",

            "#1702F塞茜尔要是能来看的话，\x01",
            "我也会更加努力的～\x02\x03",

            "当着好朋友的面，\x01",
            "可绝对不能把戏演砸啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0464
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵……\x01",
            "你还是老样子，越挫越勇呢。\x02\x03",

            "大概就是那种越是陷入绝境，\x01",
            "就越能燃烧斗志的类型吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0465
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1704F呵呵，这一点确实无法否认。\x02\x03",

            "#1700F对了，到时你也带个好男人\x01",
            "陪你一起来吧，就当是个装饰品好了。\x02\x03",

            "你工作的那个地方，\x01",
            "应该也有不少前途光明的好男人吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0466
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……呵呵，是啊………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0467
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1705F啊………\x02\x03",

            "#1706F………抱歉…………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0468
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，不用在意。\x02\x03",

            "都已经过去这么久了，\x01",
            "我也早就平静下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0469
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1700F……是吗………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0470
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1702F对了！\x01",
            "那就叫你那个警察弟弟一起来吧？\x02\x03",

            "他应该已经回到\x01",
            "克洛斯贝尔了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0471
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，你是说罗伊德吗？\x02\x03",

            "嗯，能行吗？\x01",
            "我想他应该很忙的……\x02\x03",

            "……不过，那孩子应该还没有\x01",
            "看过伊莉娅的表演，\x01",
            "或许正是个好机会呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0472
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1709F嗯嗯，就这么办吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，抱歉……\x01",
            "要到上夜班的时间了。\x02\x03",

            "谢谢你的票，\x01",
            "我会非常期待的。\x02\x03",

            "要加油排练哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0474
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1702F嗯，塞茜尔也要加油。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMapObjFlags(0x1C, 0x4)
    Sound(822, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0475
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1701F（……已经过去三年了呢。）\x02\x03",

            "#1706F（要想淡忘悲伤……\x01",
            "  恐怕还要再花点时间啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_8C4C end

    def Function_48_95DE(): pass

    label("Function_48_95DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1250, -1000, 0)
    MoveCamera(54, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -600, 0, -2900, 0)
    SetChrPos(0x102, 600, 0, -2900, 0)
    SetChrPos(0x103, -900, 0, -4100, 0)
    SetChrPos(0x104, 900, 0, -4100, 0)
    SetChrPos(0xB, 4500, 0, 4500, 90)
    OP_68(0, 1750, 5000, 6000)
    MoveCamera(34, 10, 0, 6000)
    SetCameraDistance(25500, 6000)
    FadeToBright(1000, 0)
    StopBGM(0x5DC)
    WaitBGM()
    Sleep(50)
    PlayBGM("ed7529", 0)
    VolumeBGM(0x28, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x211), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 1050, -1700, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0476
    ChrTalk(
        0x103,
        "#11P#0205F哇……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        (
            "#0109F呵呵……\x01",
            "正门大厅的设计，无论什么时候看都感觉很棒啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#6P#0000F还在放着音乐……\x01",
            "也就是说，现在正在排练吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x104,
        "#0309F哦哦，一定是这样！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    TurnDirection(0xB, 0x101, 500)

    #N0480
    NpcTalk(
        0xB,
        "男性的声音",
        "#6P──各位客人。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetCameraDistance(19000, 2000)

    def lambda_982B():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_982B)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xB4, 0x1F4)

    #C0481
    ChrTalk(
        0xB,
        "#5P真是十分抱歉。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xB,
        (
            "#5P目前并非公演时期，\x01",
            "无关人员是谢绝进入\x01",
            "本剧场的……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#6P#0003F啊，那个……\x02\x03",

            "#0000F其实我们是警察局的人，\x01",
            "为受理贵剧团的委托而来……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0484
    ChrTalk(
        0xB,
        "#5P啊，是特别任务支援科的各位吧。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xB,
        (
            "#5P欢迎光临『彩虹剧团』，\x01",
            "我从莉夏小姐那里听说了。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xB,
        (
            "#5P你们是来找剧团长和伊莉娅小姐\x01",
            "商谈的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#6P#0000F是的，可以帮我们通报一下吗？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xB,
        (
            "#5P请各位从正门进入\x01",
            "大厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xB,
        (
            "#5P剧团长和莉夏小姐\x01",
            "现在应该在里面观看\x01",
            "伊莉娅小姐的练习。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x102,
        (
            "#0101F可以吗？\x01",
            "不会给伊莉娅小姐添麻烦吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xB,
        (
            "#5P不会不会，她不会\x01",
            "在意这种小事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xB,
        (
            "#5P不如说，这样更像是正式演出，\x01",
            "她说不定会更加高兴呢。\x02",
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

    #C0494
    ChrTalk(
        0x101,
        "#6P#0002F明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        (
            "#0309F好，那我们就快点\x01",
            "进去参观吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, -2900, 0)
    OP_4C(0xB, 0xFF)
    SetChrPos(0xB, -2890, 2500, 14820, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x80, 4)
    OP_29(0x42, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_48_95DE end

    def Function_49_9BBA(): pass

    label("Function_49_9BBA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-90090, 1250, 3310, 0)
    MoveCamera(52, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22160, 0)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x8, -90050, 0, 4350, 180)
    SetChrPos(0x9, -90970, 0, 4840, 180)
    SetChrPos(0xD, -88670, 0, 4830, 225)
    SetChrPos(0x101, -89850, 0, 2450, 0)
    SetChrPos(0x102, -91090, 0, 2130, 0)
    SetChrPos(0x104, -91200, 0, 710, 0)
    SetChrPos(0x103, -89830, 0, 950, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    SetCameraDistance(21660, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0496
    ChrTalk(
        0x9,
        (
            "#1806F#1P伊莉娅小姐可真是的……\x02\x03",

            "#1801F突然就抱过去了，\x01",
            "这对罗伊德警官不是很失礼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x8,
        (
            "#1709F#5P算啦算啦，别在意这种小事嘛。\x02\x03",

            "#1702F能被姐姐拥抱，\x01",
            "警察弟弟的心里肯定也有些窃喜吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x101,
        "#0012F#12P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x103,
        "#0211F#12P………………（瞪）\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#0111F#6P（继塞茜尔小姐之后，再次……）\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#0310F#12P（这就是所谓的等级分化……\x01",
            "  弟弟至上主义吗！）\x02\x03",

            "（这个可恶的贵族弟弟！\x01",
            "  无耻的资本家弟弟！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0502
    ChrTalk(
        0x101,
        (
            "#0006F#12P那、那个……\x01",
            "关于恐吓信的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x8,
        (
            "#1705F#5P啊，那件事啊。\x02\x03",

            "#1704F既然警察弟弟出言拜托，那就没办法了。\x01",
            "我已经把信带来了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_96(0x8, 0xFFFEA0CA, 0x0, 0xD34, 0x7D0, 0x0)

    #C0504
    ChrTalk(
        0x8,
        "#1700F#5P给，就是这个。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#0002F#12P谢、谢谢。\x01",
            "（出言拜托的明明应该是你才对啊……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9F96():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9F96)

    def lambda_9FA3():
        OP_96(0xFE, 0xFFFEA03E, 0x0, 0x10FE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9FA3)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0506
    ChrTalk(
        0x101,
        "#0005F#12P嗯……\x02",
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0507
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "立即中止新剧公演。\x01",
            "否则炎之舞姬\x01",
            "将会迎来悲剧──『银』。\x07\x00\x02",
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

    #C0508
    ChrTalk(
        0x102,
        "#0101F#6P这是……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x103,
        (
            "#0201F#12P立即终止新剧公演……\x02\x03",

            "否则炎之舞姬\x01",
            "将会迎来悲剧──『银』。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x104,
        "#0301F#12P确实很有恐吓信的感觉啊。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#1706F#5P与其说是恐吓信，\x01",
            "更像是普通的恶作剧吧？\x02\x03",

            "#1700F这么说好像有点随便。\x01",
            "不过，像这种程度的恐吓\x01",
            "根本不足为奇哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A209():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A209)

    #C0512
    ChrTalk(
        0x101,
        "#0001F#12P……是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xD,
        (
            "嗯，因为我们这里\x01",
            "算是很赚钱的。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xD,
        (
            "所以总能收到这种半嫉妒，\x01",
            "半恶作剧式的恐吓信。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xD,
        (
            "不过，这次只有一点\x01",
            "让我很在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x103,
        "#0205F#12P您在意的事情是指……？\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x104,
        (
            "#0301F#12P嗯……\x01",
            "是寄件人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xD,
        "对，正是。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xD,
        (
            "到目前为止，所收到的恐吓信\x01",
            "绝大多数都是匿名的……\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x9,
        (
            "#1806F#5P但这次却留下了『银』这种\x01",
            "让人不禁浮想联翩的名字……\x02\x03",

            "#1808F所以我才觉得\x01",
            "并不是单纯的恶作剧……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "#1703F#5P嗯……\x01",
            "但我觉得，那也只是心理作用吧。 \x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#0003F#12P嗯……\x02\x03",

            "#0001F各位，关于『银』这个名字，\x01",
            "你们有什么头绪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x8,
        (
            "#1704F#5P一点也没有呢。\x02\x03",

            "#1701F话说回来，这是人名吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x9,
        (
            "#1806F#5P感觉也有点像是\x01",
            "某种暗号一类的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xD,
        (
            "嗯……在本次新剧的标题中，\x01",
            "也包含了『银』这个文字……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xD,
        "我只能想到这些了。\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x102,
        "#0103F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x101,
        (
            "#0001F#12P那么……没有其它\x01",
            "能想到的线索了吗？\x02\x03",

            "虽然有些失礼，\x01",
            "但还请允许我冒昧问上一句，\x01",
            "各位最近有没有与什么人结怨呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0529
    ChrTalk(
        0x9,
        "#1808F#5P那、那个……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xD,
        "嗯……应该不会吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 500)

    #C0531
    ChrTalk(
        0x8,
        (
            "#1705F#11P哎呀……？\x02\x03",

            "难道说，你们两个\x01",
            "得罪过什么人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_A664():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A664)
    Sleep(50)
    TurnDirection(0xD, 0x9, 500)
    Sleep(300)

    #C0532
    ChrTalk(
        0xD,
        "#11P那、那个……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x9,
        (
            "#1806F#6P得罪人的不是我们……\x01",
            "而是伊莉娅小姐你啊。\x02\x03",

            "#1801F你忘了吗，就是前几天，\x01",
            "会长先生的那件事……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0534
    ChrTalk(
        0x8,
        (
            "#1705F#11P啊啊，是说那个秃头大叔啊。\x02\x03",

            "#1706F因为实在是不值一提，\x01",
            "所以我都忘得干干净净了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0535
    ChrTalk(
        0x103,
        "#0200F#12P那个秃头大叔是指……？\x02",
    )

    CloseMessageWindow()

    def lambda_A82C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A82C)
    Sleep(200)

    def lambda_A83C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A83C)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Sleep(100)

    #C0536
    ChrTalk(
        0x8,
        (
            "#1700F#5P哦，那是一个名叫马尔克尼，\x01",
            "满身肥肉的秃头大叔。\x02\x03",

            "他率领着一个名字叫做『鲁巴彻商会』，\x01",
            "尽是无赖混混的组织。\x02",
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

    #C0537
    ChrTalk(
        0x101,
        "#0005F#12P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x102,
        "#0101F#6P鲁巴彻商会……！\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x104,
        "#0301F#12P竟然听到了这个名字……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0540
    ChrTalk(
        0x8,
        "#1705F#5P嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        (
            "#0006F#12P不，没什么……\x01",
            "最近好像总能听到这个名字。\x02\x03",

            "#0001F那么……\x01",
            "您与鲁巴彻商会的会长\x01",
            "到底发生了什么摩擦呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x8,
        (
            "#1706F#5P他们总是有接待之类的活动，\x01",
            "经常会带一些客人来我们这里。\x02\x03",

            "#1701F每次都会坐在贵宾席，\x01",
            "看上去似乎还挺有地位的。\x01",
            "不过，他们好像对演出完全没有兴趣呢。\x02\x03",

            "在看我的时候，也完全不关注我的表演，\x01",
            "只会一直用下流的眼神盯着我看。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x9,
        "#1806F#1P伊、伊莉娅小姐……\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xD,
        "你竟然能察觉到这种细节啊。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x8,
        (
            "#1704F#5P在表演的时候，舞台与观众席\x01",
            "都是我的世界嘛，这是理所当然的。\x02\x03",

            "#1700F然后，那个秃头大叔\x01",
            "就过来和我搭讪。\x02\x03",

            "说什么可以介绍我去\x01",
            "帝都的歌剧院之类的，\x01",
            "一副居高临下的讨厌姿态。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#0305F#12P哦，原来剧团还有这种计划吗？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xD,
        (
            "嗯，不止是帝国，\x01",
            "还有来自共和国那边的邀请呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xD,
        (
            "对方表示，哪怕只是短期也好，\x01",
            "希望我们能去那边进行特别演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "说起来，利贝尔王国的格兰竞技场\x01",
            "之前好像也发来过邀请吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#0003F#12P果然很受欢迎啊……\x02\x03",

            "#0001F不过，鲁巴彻的会长\x01",
            "为什么可以介绍\x01",
            "伊莉娅小姐去演出呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xD,
        (
            "他在帝都那边好像是\x01",
            "很有人脉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xD,
        (
            "不过，从与他有关的传闻上来看，\x01",
            "应该也不是什么正道的人脉关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#0108F#6P……鲁巴彻应该算是\x01",
            "一个与帝国有着密切联系的黑手党组织。\x02\x03",

            "#0101F他大概和帝都的黑道人物\x01",
            "有着很密切的来往吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x9,
        "#1801F#5P是、是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x103,
        (
            "#0205F#12P那么，您最后是怎么回应\x01",
            "那个秃头大叔的呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x8,
        (
            "#1709F#5P我当然是郑重拒绝啦。\x02\x03",

            "而且，为了让他以后别再产生纠缠我的念头，\x01",
            "我还赏了他一个耳光。\x02",
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

    #C0557
    ChrTalk(
        0x101,
        "#0011F#12P哎！？\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#0105F#6P竟、竟然对黑手党的老大\x01",
            "做出那种事……？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x9,
        (
            "#1806F#5P是啊……\x01",
            "我当时吓得都快晕过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xD,
        "我也差点吓晕呢……\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xD,
        (
            "不过，毕竟是对方犯错在先，\x01",
            "居然做出对伊莉娅毛手毛脚\x01",
            "这种鲁莽──不对，无礼的行为啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xD,
        (
            "因为当时现场有很多人劝说调解，\x01",
            "事情总算是平息下来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x104,
        (
            "#0303F#12P不过，对方很可能对当时的屈辱\x01",
            "耿耿于怀，所以才……\x02\x03",

            "#0301F是那么回事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#0203F#12P……的确，这件事情完全\x01",
            "可以定为恐吓信的动机。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0565
    ChrTalk(
        0x101,
        (
            "#0003F#12P──大致情况我已经了解了。\x02\x03",

            "#0001F我们首先会以目前的几条线索为基础，\x01",
            "着手开始调查。\x02\x03",

            "伊莉娅小姐，这封恐吓信\x01",
            "可以先放在我这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x8,
        (
            "#1700F#5P嗯，可以啊。\x02\x03",

            "#1704F呵呵……\x01",
            "你的眼神都变了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x101,
        "#0005F#12P哎……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x8,
        (
            "#1704F#5P和我们站在舞台时\x01",
            "的眼神很相似……\x02\x03",

            "#1702F很好，看来你们一定\x01",
            "能查出什么头绪。\x02\x03",

            "也算是为了消除莉夏的担忧，\x01",
            "这件事就全权委托你们解决了。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x9,
        "#1802F#1P伊莉娅小姐……\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        "#0002F#12P──我们接受这项工作。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x102,
        (
            "#0104F#6P我们一定会努力工作，\x01",
            "绝不辜负各位的期待。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21960, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddItemNumber('ＩＢＣ认证卡片', 1)
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_68(-50, 1070, -1770, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x8, -120, 2500, 15910, 42)
    SetChrPos(0x9, -80, 0, -280, 179)
    SetChrPos(0x101, 0, 0, -2000, 0)
    SetChrPos(0x102, -1290, 0, -2840, 0)
    SetChrPos(0x104, 580, 0, -2980, 0)
    SetChrPos(0x103, -660, 0, -3670, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    Sleep(500)
    SetCameraDistance(17000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Sound(1639, 255, 100, 0)    #voice#Rixia
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1300)

    #A0572
    AnonymousTalk(
        0x9,
        (
            "伊莉娅小姐似乎也同意进行调查了啊，\x01",
            "找各位商量果然是正确的选择！\x02",
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

    #C0573
    ChrTalk(
        0x101,
        (
            "#0004F#12P哈哈……工作才刚刚开始啊。\x02\x03",

            "#0001F看样子，这件事恐怕不是\x01",
            "那么简单就能解决呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x9,
        "#1806F#5P说、说得也是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0575
    ChrTalk(
        0x9,
        (
            "#1805F#5P对了……\x02\x03",

            "#1802F那个，大家和我说话的时候，\x01",
            "可以不要那么拘谨客气吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        "#0005F#12P哎……？\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x9,
        (
            "#1804F#5P那个，我只是个新人而已……\x02\x03",

            "而且比罗伊德警官和艾莉小姐\x01",
            "的年纪还要小……\x02\x03",

            "#1800F你们要是太过客气的话，\x01",
            "我会很不好意思的。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x101,
        (
            "#0000F#12P是、是吗……？\x02\x03",

            "#0002F那我们以后就──\x01",
            "不那么在意礼节了。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x9,
        (
            "#1809F#5P嗯，好的！\x01",
            "谢谢大家了！\x02",
        )
    )

    CloseMessageWindow()

    #N0580
    NpcTalk(
        0x8,
        "伊莉娅的声音",
        (
            "#2S莉夏，\x01",
            "会议就要开始啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0581
    ChrTalk(
        0x9,
        "#1802F#2P是，伊莉娅小姐！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0582
    ChrTalk(
        0x9,
        (
            "#1804F#5P那么，各位……我先失陪了。\x02\x03",

            "#1802F如果发现什么线索，\x01",
            "请不要客气，随时来剧团吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    OP_68(150, 1070, 0, 4000)
    MoveCamera(25, 20, 0, 4000)
    OP_6E(520, 4000)
    SetCameraDistance(18500, 4000)
    SetChrFlags(0x9, 0x40)
    OP_95(0x9, 310, 0, 5940, 4000, 0x1)
    OP_95(0x9, 610, 2490, 11890, 4000, 0x1)
    OP_95(0x9, 570, 2490, 14730, 4000, 0x1)
    SetChrFlags(0x9, 0x80)

    #C0583
    ChrTalk(
        0x101,
        "#0000F#5P大家好像都很忙啊……\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#0304F是啊，在公演之前，怎么也都要\x01",
            "反复排练个数百遍吧。\x02\x03",

            "#0300F不想因为恐吓信的事情浪费太多宝贵时间，\x01",
            "也是可以理解的。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x103,
        "#0204F#11P原来如此……明白了。\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，就算是为了新剧的成功，\x01",
            "我们也要想办法把这件事情顺利解决啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        "#0004F#5P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    OP_68(0, 1450, -1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x0, 0, 0, -1000, 0)
    SetChrPos(0x1, 0, 0, -1000, 0)
    SetChrPos(0x2, 0, 0, -1000, 0)
    SetChrPos(0x3, 0, 0, -1000, 0)
    SetScenarioFlags(0x80, 5)
    OP_29(0x42, 0x1, 0x2)
    OP_1B(0x4, 0xFF, 0xFFFF)
    OP_1B(0x0, 0xFF, 0xFFFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_49_9BBA end

    def Function_50_BA08(): pass

    label("Function_50_BA08")

    OP_95(0x9, -49720, 0, 370, 2500, 0x0)
    OP_95(0x9, -50520, 0, 10010, 2500, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_50_BA08 end

    def Function_51_BA3F(): pass

    label("Function_51_BA3F")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_BA4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA4E)
    OP_95(0xFE, -620, 0, 5850, 1500, 0x0)
    OP_95(0xFE, -620, 2390, 11360, 1500, 0x0)
    Return()

    # Function_51_BA3F end

    def Function_52_BA83(): pass

    label("Function_52_BA83")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_BA92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA92)
    OP_95(0xFE, 520, 0, 5850, 1500, 0x0)
    OP_95(0xFE, 520, 2390, 11360, 1500, 0x0)
    Return()

    # Function_52_BA83 end

    def Function_53_BAC7(): pass

    label("Function_53_BAC7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06200.itp")
    LoadChrToIndex("chr/ch33000.itc", 0x28)
    LoadChrToIndex("chr/ch33300.itc", 0x29)
    LoadChrToIndex("chr/ch27700.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadChrToIndex("chr/ch33100.itc", 0x2C)
    LoadChrToIndex("chr/ch32400.itc", 0x2D)
    LoadChrToIndex("chr/ch22000.itc", 0x2E)
    LoadChrToIndex("chr/ch33200.itc", 0x2F)
    LoadChrToIndex("chr/ch27800.itc", 0x30)
    LoadChrToIndex("chr/ch27900.itc", 0x31)
    LoadChrToIndex("chr/ch09800.itc", 0x32)
    SetChrChipByIndex(0x21, 0x28)
    SetChrChipByIndex(0x22, 0x29)
    SetChrChipByIndex(0x23, 0x2A)
    SetChrChipByIndex(0x24, 0x2B)
    SetChrChipByIndex(0x25, 0x2C)
    SetChrChipByIndex(0x26, 0x2D)
    SetChrChipByIndex(0x27, 0x2E)
    SetChrChipByIndex(0x28, 0x2F)
    SetChrChipByIndex(0x29, 0x30)
    SetChrChipByIndex(0x2A, 0x31)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x21, -670, 0, 5740, 0)
    SetChrPos(0x22, 520, 0, 5700, 0)
    SetChrPos(0x23, -670, 0, 240, 0)
    SetChrPos(0x24, 520, 0, 1240, 0)
    SetChrPos(0x25, -670, 0, -3240, 0)
    SetChrPos(0x26, 520, 0, -2240, 0)
    SetChrPos(0x27, -670, 0, -6240, 0)
    SetChrPos(0x28, 520, 0, -6240, 0)
    SetChrPos(0x29, -670, 0, -6240, 0)
    SetChrPos(0x2A, 520, 0, -6240, 0)
    SetChrPos(0x1C, -670, 0, -6240, 0)
    SetChrPos(0x1D, 520, 0, -6240, 0)
    ClearChrFlags(0xC, 0x80)
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    OP_68(0, 1450, 1500, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    MoveCamera(90, 12, 0, 10000)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -45300, 0, 400, 90)
    SetChrPos(0x102, -45270, 0, -700, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -46840, 0, -100, 90)
    SetChrChipByIndex(0x9, 0x32)
    FadeToBright(2000, 0)
    BeginChrThread(0x21, 0, 0, 51)
    BeginChrThread(0x22, 0, 0, 52)
    BeginChrThread(0x23, 0, 0, 51)
    BeginChrThread(0x24, 0, 0, 52)
    BeginChrThread(0x25, 0, 0, 51)
    BeginChrThread(0x26, 0, 0, 52)
    Sleep(500)
    BeginChrThread(0x1C, 0, 0, 51)
    Sleep(200)
    BeginChrThread(0x1D, 0, 0, 52)
    Sleep(1500)
    BeginChrThread(0x27, 0, 0, 51)
    BeginChrThread(0x28, 0, 0, 52)
    Sleep(500)
    Sleep(2000)
    BeginChrThread(0x29, 0, 0, 51)
    Sleep(500)
    BeginChrThread(0x2A, 0, 0, 52)
    Fade(500)
    OP_68(-45820, 1300, -390, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    OP_0D()
    Sleep(300)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0588
    ChrTalk(
        0x101,
        (
            "#0003F#5P麦克道尔市长似乎\x01",
            "也出席了……\x02\x03",

            "#0000F说起来，他好像说过，\x01",
            "会全力支持这次的新剧吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0589
    ChrTalk(
        0x102,
        (
            "#0104F#12P嗯，因为外公原本\x01",
            "就是彩虹剧团的支持者啊。\x02\x03",

            "#0102F他似乎也非常期待\x01",
            "莉夏小姐的出道表演呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0590
    AnonymousTalk(
        0x9,
        (
            "啊哈哈……\x01",
            "希望能不负他的期待。\x02\x03",

            "话说回来……如果演出照常进行的话，\x01",
            "会不会真的像那个『银』说的一样，\x01",
            "发生什么不好的事情呢？\x02",
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

    def lambda_C05F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C05F)
    Sleep(50)

    def lambda_C06F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C06F)
    Sleep(300)

    #C0591
    ChrTalk(
        0x101,
        (
            "#0006F#11P……不知道，\x01",
            "但我觉得很有可能吧。\x02\x03",

            "#0000F搜查一科会进行警戒工作，\x01",
            "伊莉娅小姐应该不会有事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x9,
        "#6206F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x102,
        (
            "#0106F#11P比起那个，我更在意的是……\x01",
            "不把这件事告诉伊莉娅小姐……\x01",
            "真的妥当吗？\x02\x03",

            "#0101F虽然剧团长也是同样的想法……\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x9,
        (
            "#6204F#6P是的……没问题。\x02\x03",

            "我不想让她──\x01",
            "不想让伊莉娅小姐产生多余的担忧，\x01",
            "只希望她能尽情展现演技。\x02\x03",

            "#6202F这是我……\x01",
            "也是我们所有人的共同期望。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        (
            "#0002F#11P你还真是\x01",
            "喜欢伊莉娅小姐呢……\x02\x03",

            "#0000F为什么要为她做这么多呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x9,
        (
            "#6202F#6P呵呵……\x02\x03",

            "#6204F虽然我算是被她\x01",
            "强拉进这个剧团的……\x02\x03",

            "但是，我还是很开心。\x02\x03",

            "#6208F在来到克洛斯贝尔之前……\x01",
            "我一直走着被别人\x01",
            "决定好的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x101,
        "#0005F#11P哎……？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x9,
        (
            "#6204F#6P所以，当看到她的表演时，就被彻底\x01",
            "吸引住了。我当时就在想——\x02\x03",

            "『啊啊，原来还有这样的人。心无杂念、勇往直前，\x01",
            "  活着只为了让自己绽放出更耀眼的光芒。』\x02\x03",

            "#6210F呵呵，也许正是因为我无论如何也做不到，\x01",
            "所以才会觉得很羡慕，很憧憬吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        "#0108F#11P莉夏小姐……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0600
    ChrTalk(
        0x101,
        (
            "#0004F#11P──无论如何也做不到，\x01",
            "这话说得太绝对了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x9,
        "#6205F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#0003F#11P你这次扮演的角色\x01",
            "『月之姬』……\x02\x03",

            "也许确实是在『太阳之姬』的照耀之下\x01",
            "才能散发出光芒。\x02\x03",

            "#0002F不过，就算是我这个外行人\x01",
            "也能看得出来。你和伊莉娅小姐的演技\x01",
            "是两种完全不同的类型，各有妙处。\x02\x03",

            "#0009F总有一天……\x01",
            "你肯定也会散发出属于自己的光辉。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x9,
        "#6210F#6P是……是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        (
            "#0004F#11P嗯，我想……也许正是因为如此，\x01",
            "伊莉娅小姐才会邀你踏入这个世界吧。\x02\x03",

            "#0000F这次的事件……\x01",
            "我们在中途也曾多次碰壁，\x01",
            "不过，总算进展到了这一步。\x02\x03",

            "无论如何，也一定会把事件顺利解决的……\x01",
            "所以，希望你也要好好加油，全力演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x9,
        (
            "#6209F#6P好、好的……！\x02\x03",

            "#6202F那么，\x01",
            "我差不多也该走了。\x02\x03",

            "罗伊德警官、艾莉小姐，\x01",
            "请你们加油。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x101,
        "#0002F#11P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x102,
        "#0109F#11P好的，你也要多加油。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x190)
    OP_68(-47770, 1300, 420, 3000)
    BeginChrThread(0x9, 0, 0, 50)
    Sleep(1000)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-45290, 1300, -570, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17580, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0608
    ChrTalk(
        0x101,
        (
            "#0000F#5P那么……\x01",
            "在演出开始之前，\x01",
            "我们先到别的地方待命吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0609
    ChrTalk(
        0x101,
        "#0005F#5P嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x102,
        (
            "#0113F#11P唉……真是的。\x02\x03",

            "竟然会如此迟钝，\x01",
            "该说是性格所致吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#0011F#5P哎……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0612
    ChrTalk(
        0x102,
        (
            "#0111F#12P──没什么。\x02\x03",

            "#0106F话说回来，既然都已经做了\x01",
            "如此正式的约定……\x02\x03",

            "#0102F这次的事件……\x01",
            "我们绝对要顺利解决哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        "#0000F#5P嗯……那是当然的。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18080, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_BAC7 end

    def Function_54_C973(): pass

    label("Function_54_C973")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, -7470, 0, 4730, 1500, 0x0)
    OP_95(0xFE, -6470, 0, 3720, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_C973 end

    def Function_55_C9AE(): pass

    label("Function_55_C9AE")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, -7470, 0, 4730, 1500, 0x0)
    OP_95(0xFE, -7000, 0, 5160, 1500, 0x0)
    OP_93(0xFE, 0x80, 0x1F4)
    Return()

    # Function_55_C9AE end

    def Function_56_C9E9(): pass

    label("Function_56_C9E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    OP_68(-7840, 1450, 4510, 0)
    MoveCamera(20, 26, 0, 5000)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -10000, 0, 4730, 90)
    SetChrPos(0x102, -10000, 0, 4730, 90)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    ClearChrFlags(0xC, 0x80)
    OP_66(0x5, 0x1)
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    OP_68(-6840, 1450, 4510, 5000)
    MoveCamera(14, 26, 0, 5000)
    OP_6E(560, 5000)
    SetCameraDistance(17500, 5000)
    Sound(875, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 54)
    Sleep(1000)
    BeginChrThread(0x102, 0, 0, 55)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    #C0614
    ChrTalk(
        0x101,
        (
            "#0004F#12P开始了吗……\x02\x03",

            "#0002F还真是热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x102,
        (
            "#0109F呵呵，其实我也很想\x01",
            "亲眼看看呢。\x02\x03",

            "#0102F好羡慕一科的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x101,
        (
            "#0006F#12P不过，眼前就是\x01",
            "那么精彩的演出，\x01",
            "却要集中精神警戒。\x02\x03",

            "#0001F说不定……反而会更加痛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x102,
        (
            "#0104F呵呵，说的也有道理。\x02\x03",

            "#0100F──那么，我们也开始\x01",
            "巡视剧场内部吧。\x02\x03",

            "不过，一科的人也在，\x01",
            "窥视观众席的时候可要小心一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        "#0000F#12P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0619
    AnonymousTalk(
        0x101,
        (
            "#0000F我是罗伊德……\x01",
            "你们两位，能听到吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0620
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，听得到啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0621
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……看样子，\x01",
            "好像已经开始了啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0622
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F嗯，我们这就开始\x01",
            "巡视剧场内部。\x02\x03",

            "请你们继续\x01",
            "在剧场周围警戒。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0623
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……明白。\x02\x03",

            "蔡特也来了，\x01",
            "我们这边完全没有问题。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2052, 255, 80, 0)    #voice#Zeit
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0624
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0012F是、是吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0625
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要是发现什么可疑人物，就马上联络。\x02\x03",

            "可别看表演看得太入神，\x01",
            "被一科的那些家伙发现啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0626
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F嗯，我知道。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0627
    ChrTalk(
        0x101,
        (
            "#0003F#12P──立即开始巡逻吧。\x02\x03",

            "#0001F先在剧场里巡视一圈，\x01",
            "顺便问问剧场内的工作人员，\x01",
            "确认一下是否有什么异常吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x102,
        "#0101F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -6680, 0, 4710, 90)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 45000, 5650, 15300, 3000, 5000, 0)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    SetScenarioFlags(0x84, 4)
    OP_29(0x43, 0x1, 0xA)
    OP_1B(0x0, 0x0, 0x57)
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x93, 1)
    ClearScenarioFlags(0x93, 2)
    ClearScenarioFlags(0x93, 3)
    EventEnd(0x5)
    Return()

    # Function_56_C9E9 end

    def Function_57_D067(): pass

    label("Function_57_D067")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 3950, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 2500, 15000, 0)
    SetChrPos(0x102, -1000, 2500, 15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0629
    ChrTalk(
        0x101,
        (
            "#0004F看起来，\x01",
            "好像没什么异常情况……\x02\x03",

            "#0002F话说回来，伊莉娅小姐\x01",
            "还真不是一般的厉害啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x102,
        (
            "#0102F是啊……\x02\x03",

            "#0104F……该走了。\x02\x03",

            "要是再看下去的话，\x01",
            "会被完全吸引住的。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x101,
        "#0012F嗯，对啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x84, 5)
    EventEnd(0x5)
    Return()

    # Function_57_D067 end

    def Function_58_D1AE(): pass

    label("Function_58_D1AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 3950, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 2500, 15000, 0)
    SetChrPos(0x102, -1000, 2500, 15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0632
    ChrTalk(
        0x101,
        (
            "#0004F没有异常……\x02\x03",

            "#0002F不过，\x01",
            "莉夏还真是厉害啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x102,
        (
            "#0102F是啊，她的舞蹈与伊莉娅小姐的\x01",
            "舞蹈风格不同……\x02\x03",

            "是名符其实的，闪耀着银色光芒的\x01",
            "月之舞姬啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x85, 1)
    EventEnd(0x5)
    Return()

    # Function_58_D1AE end

    def Function_59_D2D1(): pass

    label("Function_59_D2D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 3950, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 2500, 15000, 0)
    SetChrPos(0x102, -1000, 2500, 15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0634
    ChrTalk(
        0x101,
        "#0012F嗯，演出接近高潮了啊……\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x102,
        (
            "#0104F是啊，真没想到她们在剧中\x01",
            "的关系是姐妹……\x02\x03",

            "#0102F之后会怎么发展下去呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 800)

    #C0636
    ChrTalk(
        0x101,
        "#0011F……到此为止吧！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    #C0637
    ChrTalk(
        0x102,
        (
            "#0106F对、对啊……\x02\x03",

            "现在还要专心巡逻……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x85, 5)
    EventEnd(0x5)
    Return()

    # Function_59_D2D1 end

    def Function_60_D484(): pass

    label("Function_60_D484")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_D4EE")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_D547")

    label("loc_D4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_D547")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_D547")

    FadeToBright(1000, 0)
    OP_0D()

    #C0638
    ChrTalk(
        0x101,
        (
            "#0003FＳ席没有异常……\x02\x03",

            "#0000F嗯，达德利搜查官也在呢，\x01",
            "这边应该不需要担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        (
            "#0100F……说得也是。\x02\x03",

            "我们去别处巡视吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_D5F4")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_D60E")

    label("loc_D5F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_D60E")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_D60E")

    SetScenarioFlags(0x84, 6)
    EventEnd(0x5)
    Return()

    # Function_60_D484 end

    def Function_61_D614(): pass

    label("Function_61_D614")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_D67E")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_D6D7")

    label("loc_D67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_D6D7")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_D6D7")

    FadeToBright(1000, 0)
    OP_0D()

    #C0640
    ChrTalk(
        0x101,
        (
            "#0000F看来没什么问题……\x02\x03",

            "#0006F不过，达德利搜查官\x01",
            "也很了不起啊……\x02\x03",

            "#0001F竟然能在那种表演面前保持冷静，\x01",
            "丝毫都没有放松警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        "#0103F是啊……真是钢铁般的意志。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_D7AD")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_D7C7")

    label("loc_D7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_D7C7")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_D7C7")

    SetScenarioFlags(0x85, 2)
    EventEnd(0x5)
    Return()

    # Function_61_D614 end

    def Function_62_D7CD(): pass

    label("Function_62_D7CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_D837")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_D890")

    label("loc_D837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_D890")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_D890")

    FadeToBright(1000, 0)
    OP_0D()

    #C0642
    ChrTalk(
        0x101,
        (
            "#0012F哈哈……其实达德利搜查官\x01",
            "好像也挺在意舞台上的表演呢。\x02\x03",

            "#0000F虽然他并没有因此而放松警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x102,
        (
            "#0104F呵呵，这也是可以理解的。\x02\x03",

            "#0100F看了彩虹剧团的舞台演出，\x01",
            "恐怕没有任何人能够毫不动心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_D984")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_D99E")

    label("loc_D984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_D99E")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_D99E")

    SetScenarioFlags(0x85, 6)
    EventEnd(0x5)
    Return()

    # Function_62_D7CD end

    def Function_63_D9A4(): pass

    label("Function_63_D9A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrPos(0x102, -46700, 11200, 124000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0644
    ChrTalk(
        0x101,
        (
            "#0005F（这里是贵宾席吗……）\x02\x03",

            "#0001F（只有普通警官在守卫，\x01",
            "  没问题吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x102,
        (
            "#0104F（没关系，阿奈斯特先生\x01",
            "  也兼任外公的保镖。）\x02\x03",

            "#0100F（如果发生什么异常状况，\x01",
            "  我相信他能很好的处理……）\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x101,
        "#0000F（说得也对……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x84, 7)
    EventEnd(0x5)
    Return()

    # Function_63_D9A4 end

    def Function_64_DB09(): pass

    label("Function_64_DB09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrPos(0x102, -46700, 11200, 124000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0647
    ChrTalk(
        0x101,
        (
            "#0003F（没有异常吗……）\x02\x03",

            "#0001F（警官的注意力\x01",
            "  似乎有点散漫了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x102,
        (
            "#0106F（唉，一边看着那种表演一边工作，\x01",
            "  也难怪他会走神呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x85, 3)
    EventEnd(0x5)
    Return()

    # Function_64_DB09 end

    def Function_65_DC19(): pass

    label("Function_65_DC19")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrPos(0x102, -46700, 11200, 124000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0649
    ChrTalk(
        0x101,
        (
            "#0000F（……似乎没什么问题。）\x02\x03",

            "（那名警官暂且不说，但阿奈斯特先生\x01",
            "  好像一直都在警戒着周围的情况呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x102,
        "#0100F（嗯，是啊……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x85, 7)
    EventEnd(0x5)
    Return()

    # Function_65_DC19 end

    def Function_66_DD24(): pass

    label("Function_66_DD24")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD93")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_DE46")

    label("loc_DD93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDF6")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_DE46")

    label("loc_DDF6")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_DE46")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x93, 1)
    ClearScenarioFlags(0x93, 2)
    ClearScenarioFlags(0x93, 3)
    Sound(875, 0, 100, 0)
    Sleep(1000)
    Sound(876, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0651
    ChrTalk(
        0x101,
        "#0005F这是……\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x102,
        "#0100F第一幕好像结束了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_DD24 end

    def Function_67_DF03(): pass

    label("Function_67_DF03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-460, 3950, 12700, 0)
    MoveCamera(29, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -890, 2500, 12720, 0)
    SetChrPos(0x102, 210, 2500, 12660, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0653
    ChrTalk(
        0x101,
        (
            "#0004F#5P第二幕开始了吗……\x02\x03",

            "#0002F莉夏似乎很努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        (
            "#0104F是啊……\x01",
            "掌声很热烈呢。\x02\x03",

            "#0100F那么，\x01",
            "我们再去巡视一遍吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        "#0000F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -890, 2500, 12720, 0)
    SetScenarioFlags(0x85, 0)
    OP_29(0x43, 0x1, 0xB)
    EventEnd(0x5)
    Return()

    # Function_67_DF03 end

    def Function_68_E01E(): pass

    label("Function_68_E01E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E08D")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_E140")

    label("loc_E08D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0F0")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_E140")

    label("loc_E0F0")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_E140")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x93, 1)
    ClearScenarioFlags(0x93, 2)
    ClearScenarioFlags(0x93, 3)
    Sound(875, 0, 100, 0)
    Sleep(1000)
    Sound(876, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0656
    ChrTalk(
        0x101,
        "#0000F第二幕已经结束了吗……\x02",
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x102,
        (
            "#0104F是啊……\x01",
            "演出似乎很精彩啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_68_E01E end

    def Function_69_E214(): pass

    label("Function_69_E214")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-460, 3950, 12700, 0)
    MoveCamera(29, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -890, 2500, 12720, 0)
    SetChrPos(0x102, 210, 2500, 12660, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0658
    ChrTalk(
        0x101,
        (
            "#0000F#5P第三幕……已经到了剧目的转折点了啊。\x02\x03",

            "#0012F话说回来，观众们刚才的反应可真是热烈呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x102,
        (
            "#0104F是啊……\x01",
            "光凭那些掌声，就能想象出\x01",
            "这次的表演有多么精彩了。\x02\x03",

            "#0108F要是能平安无事地\x01",
            "继续进行下去，直到结束就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x101,
        (
            "#0006F#5P是啊……\x02\x03",

            "#0000F那样的话，虽然无法逮捕到犯人，\x01",
            "但也确实是最好的结果了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -890, 2500, 12720, 0)
    SetScenarioFlags(0x85, 4)
    OP_29(0x43, 0x1, 0xC)
    EventEnd(0x5)
    Return()

    # Function_69_E214 end

    def Function_70_E3D2(): pass

    label("Function_70_E3D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E441")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_E4F4")

    label("loc_E441")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4A4")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_E4F4")

    label("loc_E4A4")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_E4F4")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(875, 0, 100, 0)
    Sleep(1000)
    Sound(876, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0661
    ChrTalk(
        0x101,
        "#0001F……第三幕结束了吗……\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x102,
        (
            "#0101F是啊……\x01",
            "最后一幕要开始了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_E3D2 end

    def Function_71_E5BF(): pass

    label("Function_71_E5BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-280, 1450, -290, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    ClearChrFlags(0xB, 0x4)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 500, 0, -100, 0)
    SetChrPos(0x102, -740, 0, 330, 0)
    SetChrPos(0xB, -440, 2500, 15470, 180)
    PlayBGM("ed7531", 0)
    VolumeBGM(0x32, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    #C0663
    ChrTalk(
        0x101,
        (
            "#0004F#11P呼……\x02\x03",

            "#0000F看样子，预演\x01",
            "将会平安落幕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x102,
        (
            "#0104F#5P是啊，巡逻的时候\x01",
            "也没有发现什么可疑人物。\x02",
        )
    )

    CloseMessageWindow()

    #N0665
    NpcTalk(
        0xB,
        "男性的声音",
        "罗伊德警官、艾莉小姐……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E721():

        label("loc_E721")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_E721")

    QueueWorkItem2(0x101, 0, lambda_E721)

    def lambda_E733():

        label("loc_E733")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_E733")

    QueueWorkItem2(0x102, 0, lambda_E733)
    Fade(500)
    OP_68(-260, 3950, 11720, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(190, 1450, 500, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15000, 3000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xB, 310, 10, 2240, 4000, 0x0)
    OP_64(0xB)

    #C0666
    ChrTalk(
        0x101,
        "#0005F#12P巴尔萨摩经理……\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x102,
        "#0105F#6P发生什么事了？\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xB,
        "#5P其实……\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xB,
        (
            "#5P我们发现了一位\x01",
            "举止有些可疑的客人……\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0xB,
        (
            "#5P而且，那位客人\x01",
            "并不在邀请名单里……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)

    #C0671
    ChrTalk(
        0x101,
        "#0011F#12P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x102,
        "#0101F#6P他、他在哪里！？\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xB,
        "#5P就在右边的阶梯上方。\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xB,
        (
            "#5P似乎正在偷偷\x01",
            "窥视Ｓ席呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#0013F#12P知道了……！\x01",
            "我们马上去看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x102,
        (
            "#0101F#6P经理，请您在这里\x01",
            "稍等一下吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xB,
        "#5P好、好的……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -240, 0, -190, 0)
    SetChrPos(0xB, 1640, 0, 3600, 225)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x86, 0)
    OP_29(0x43, 0x1, 0xD)
    OP_63(0xB, 0x0, 1900, 0x28, 0x2B, 0x64, 0x0)
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    OP_1B(0x0, 0x0, 0x57)
    EventEnd(0x5)
    Return()

    # Function_71_E5BF end

    def Function_72_E9F0(): pass

    label("Function_72_E9F0")

    OP_92(0xFE, 0xBC98, 0x38A4, 0x320)
    OP_95(0xFE, 48280, 5600, 14500, 5000, 0x1)

    def lambda_EA16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EA16)
    OP_95(0xFE, 46280, 5600, 14900, 5000, 0x1)
    Return()

    # Function_72_E9F0 end

    def Function_73_EA37(): pass

    label("Function_73_EA37")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    OP_68(48850, 1300, 800, 0)
    MoveCamera(52, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 48060, 0, 480, 0)
    SetChrPos(0x102, 49680, 0, 560, 0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 49400, 5600, 15100, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0678
    ChrTalk(
        0x101,
        "#0005F#5P（什么……！？）\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x102,
        "#0101F#11P（那个人是……！）\x02",
    )

    CloseMessageWindow()
    OP_68(49230, 6900, 14230, 3000)
    MoveCamera(27, 22, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    Sleep(3000)

    #C0680
    ChrTalk(
        0x1E,
        (
            "#2101F#11P真是的，为什么\x01",
            "达德利会在那种地方啊……！\x02\x03",

            "难得的好镜头，却被他挡住光线了，\x01",
            "就不能闪开一点吗……！\x02\x03",

            "#2106F不过，要是使用闪光灯的话，\x01",
            "那家伙肯定会马上察觉的……\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "格蕾丝小姐……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(49230, 6900, 14230, 3000)
    MoveCamera(44, 18, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_EC86():
        OP_95(0xFE, 49000, 5600, 13200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EC86)
    OP_93(0x1E, 0xB4, 0x1F4)

    def lambda_ECA7():
        OP_95(0xFE, 50400, 5600, 13200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ECA7)
    WaitChrThread(0x101, 0)

    #C0682
    ChrTalk(
        0x1E,
        (
            "#2105F#5P哎呀呀……罗伊德！？\x02\x03",

            "连艾莉也在……\x01",
            "你们在这里干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x101,
        "#0013F#12P这句话应该由我来问吧……！\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x102,
        (
            "#0101F格蕾丝小姐，您为什么会在这里呢？\x02\x03",

            "您应该没有接到邀请吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x1E,
        (
            "#2109F#5P啊哈哈……\x01",
            "其实是有点原因的啦……\x02\x03",

            "我稍微耍了点小手段，就混进来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        "#0105F小、小手段……？\x02",
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x1E,
        (
            "#2106F#5P嗯，要帮我保密哟。\x02\x03",

            "#2102F我混在了清洁工的队伍里，\x01",
            "趁乱溜了进来……就是这么简单。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        "#0011F#12P哎！？\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x102,
        "#0101F为、为什么要做这种事……\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1E,
        (
            "#2106F#5P因为～\x01",
            "寄到我们这边，用于采访的门票\x01",
            "都被其他的记者抢走了嘛！\x02\x03",

            "#2110F我超想看预演的，\x01",
            "而且还要追查其它消息，\x01",
            "所以也就只能偷偷溜进来啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x101,
        "#0006F#12P那、那个啊……\x02",
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x102,
        "#0106F……真是太会添乱了……\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x1E,
        (
            "#2102F#5P好、好啦，别管这些了，\x01",
            "你们就在这里和我一起看演出吧？\x02\x03",

            "#2109F马上就要到高潮部分了。\x01",
            "如果不看的话，可是会后悔一辈子的哟。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        (
            "#0003F#12P等正式公演时再看不就好了吗！\x02\x03",

            "#0013F先不说这些了……\x01",
            "请问，您潜入这里的理由真的只有这些吗？\x02\x03",

            "寄出恐吓信的人，该不会\x01",
            "就是格蕾丝小姐你吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x1E,
        (
            "#2105F#5P恐吓信……那是什么啊！？\x02\x03",

            "这么一说，我刚才溜进来的时候，\x01",
            "正好看到了达德利还有一科的那些人，\x01",
            "真是吓了一跳呢……\x02\x03",

            "#2101F难不成，就是因为你刚才说的恐吓信吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x102,
        "#0108F……似乎不是她呢。\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x101,
        (
            "#0000F#12P是、是啊……\x02\x03",

            "就算是格蕾丝小姐，\x01",
            "也不可能做出那种事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x1E,
        (
            "#2101F#5P『就算是格蕾丝小姐』……这叫什么话！\x01",
            "不觉得有点失礼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#0006F#12P可您明明就很出格啊，\x01",
            "为了报道，居然还偷偷潜入进来……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x101,
        (
            "#0001F#12P说起来……\x01",
            "您刚才好像说过，\x01",
            "还要追查其它消息吧？\x02\x03",

            "到底是什么消息呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0701
    ChrTalk(
        0x1E,
        (
            "#2102F#5P哎呀，这可不能说哦。\x02\x03",

            "#2105F啊……\x01",
            "一科会来这里进行警卫，\x01",
            "难道就是为了监视『他』吗……？\x02\x03",

            "#2106F真糟糕，本来还以为\x01",
            "只有我一个人注意到了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        "#0005F#12P您是指……\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x102,
        "#0101F『银』吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0704
    ChrTalk(
        0x1E,
        (
            "#2105F#5P『银』……那是什么啊？\x02\x03",

            "#2101F跟刚才你们说的恐吓信\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x102,
        "#0105F啊，又搞错了吗……\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x101,
        (
            "#0003F#12P……格蕾丝小姐，\x01",
            "请把您知道的事情都告诉我们吧。\x02\x03",

            "#0013F否则，我们就要把您强行驱逐出去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0707
    ChrTalk(
        0x1E,
        (
            "#2105F#5P等、等一下啦，罗伊德……\x01",
            "怎么可以这么过分啊。\x02\x03",

            "#2109F我们不是好朋友嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        (
            "#0006F#12P我们现在十分需要线索，\x01",
            "哪怕只有一点点也好。\x02\x03",

            "#0013F所以，请告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x1E,
        (
            "#2106F#5P呼……你是认真的吗？\x02\x03",

            "#2100F可是，在艾莉面前，\x01",
            "把这种消息说出来真的好吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0710
    ChrTalk(
        0x101,
        "#0005F#12P这、这是什么意思……\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x102,
        "#0101F为什么……不能当着我面说呢？\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x1E,
        (
            "#2103F#5P算了，不管这么多了……\x01",
            "听了之后可要保持镇静哦。\x02\x03",

            "#2101F──我正在追查的这个消息，\x01",
            "就是与市长的首席秘书有关的负面传闻。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0713
    ChrTalk(
        0x102,
        "#0105F………哎…………\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x101,
        "#0007F#12P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x1E,
        (
            "#2104F#5P好像是叫阿奈斯特吧，\x01",
            "他可是相当危险的家伙哟。\x02\x03",

            "#2102F他瞒着市长，擅自挪用\x01",
            "事务所的资金……\x02\x03",

            "最近又跟帝国派的议员进行密谈，\x01",
            "似乎有什么企图呢。\x02\x03",

            "#2109F该不会是想暗杀市长……\x01",
            "啊哈哈，但再怎么说，也不可能做到那种地步吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    TurnDirection(0x102, 0x101, 500)

    #C0716
    ChrTalk(
        0x102,
        (
            "#0108F那个，罗伊德……\x02\x03",

            "#0101F如果外公在这种状况下\x01",
            "被人杀死的话……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0717
    ChrTalk(
        0x101,
        (
            "#0005F#6P……只要没有目击者，就能通过\x01",
            "各种伪装手段，将罪行嫁祸于人……\x02\x03",

            "#0010F──难道这就是他的目的吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(49110, 6900, 15180, 1000)
    BeginChrThread(0x101, 0, 0, 72)
    Sleep(500)
    Sound(103, 0, 100, 0)
    BeginChrThread(0x102, 0, 0, 72)
    OP_93(0x1E, 0x10E, 0x1F4)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0718
    ChrTalk(
        0x1E,
        "#2105F#11P等、等一下……！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x87, 5)
    SetScenarioFlags(0x5D, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_73_EA37 end

    def Function_74_F95A(): pass

    label("Function_74_F95A")


    def lambda_F95F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F95F)
    OP_95(0xFE, -38080, 5600, 97990, 6000, 0x0)
    OP_95(0xFE, -47290, 5600, 107210, 6000, 0x0)
    OP_95(0xFE, -47070, 11200, 117460, 6000, 0x0)
    OP_95(0xFE, -47270, 11200, 123420, 6000, 0x0)
    TurnDirection(0xFE, 0x20, 800)
    Return()

    # Function_74_F95A end

    def Function_75_F9C3(): pass

    label("Function_75_F9C3")


    def lambda_F9C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F9C8)
    OP_95(0xFE, -38080, 5600, 97990, 6000, 0x0)
    OP_95(0xFE, -47290, 5600, 107210, 6000, 0x0)
    OP_95(0xFE, -47070, 11200, 117460, 6000, 0x0)
    OP_95(0xFE, -46940, 11200, 122160, 6000, 0x0)
    TurnDirection(0xFE, 0x20, 800)
    Return()

    # Function_75_F9C3 end

    def Function_76_FA2C(): pass

    label("Function_76_FA2C")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x1000)
    OP_52(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0xFE, 0xFFFF4854, 0x1E672, 0x320)
    OP_95(0xFE, -47020, 11200, 124530, 6000, 0x0)

    def lambda_FA67():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FA67)
    OP_95(0xFE, -47020, 11200, 126530, 6000, 0x0)
    Return()

    # Function_76_FA2C end

    def Function_77_FA88(): pass

    label("Function_77_FA88")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("apl/ch50222.itc", 0x1F)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -36500, 5600, 97990, 0)
    SetChrPos(0x102, -36500, 5600, 97990, 0)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -47470, 8000, 112190, 93)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x20, 0x2)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -45230, 11200, 123570, 45)
    OP_6B(0x101)
    OP_68(-36500, 7050, 97990, 0)
    MoveCamera(57, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x6, 0x0, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x2)
    Sound(103, 0, 100, 0)
    OP_79(0x6)
    MoveCamera(20, 22, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(19500, 7000)
    BeginChrThread(0x101, 0, 0, 74)
    Sleep(500)
    BeginChrThread(0x102, 0, 0, 75)
    Sleep(4000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x101, 0)

    #C0719
    ChrTalk(
        0x101,
        "#0010F#5P这是……\x02",
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x102,
        "#0101F#5P本应在贵宾席的警官……！？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1559, 255, 100, 0)    #voice#Dudley
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    def lambda_FC65():
        OP_95(0xFE, -47100, 11200, 119630, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_FC65)
    WaitChrThread(0x1F, 0)
    Sleep(150)

    #C0721
    ChrTalk(
        0x1F,
        "#0607F#5P你们在这里做什么！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0722
    ChrTalk(
        0x1F,
        "#0605F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1F, 800)

    #C0723
    ChrTalk(
        0x101,
        (
            "#0007F#5P以后再跟您解释……！\x01",
            "艾莉，快冲进去！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    #C0724
    ChrTalk(
        0x102,
        "#0101F好、好的……！\x02",
    )

    CloseMessageWindow()
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x2)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 76)
    Sleep(100)
    BeginChrThread(0x102, 0, 0, 76)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5E, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_77_FA88 end

    def Function_78_FD8C(): pass

    label("Function_78_FD8C")


    def lambda_FD91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FD91)
    OP_95(0xFE, -47010, 11200, 124560, 8000, 0x1)
    OP_95(0xFE, -47090, 11200, 117520, 8000, 0x1)
    OP_95(0xFE, -46520, 5600, 107590, 8000, 0x1)
    OP_95(0xFE, -41100, 5600, 100220, 8000, 0x1)
    OP_95(0xFE, -40120, 5600, 93460, 8000, 0x1)
    OP_95(0xFE, -39900, 0, 83980, 8000, 0x1)
    OP_95(0xFE, -37970, 0, 81930, 8000, 0x1)

    def lambda_FE2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FE2E)
    OP_95(0xFE, -36970, 0, 81930, 7000, 0x0)
    Return()

    # Function_78_FD8C end

    def Function_79_FE4F(): pass

    label("Function_79_FE4F")


    def lambda_FE54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FE54)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_95(0xFE, -47010, 11200, 124560, 10000, 0x1)
    OP_95(0xFE, -47090, 11200, 117520, 10000, 0x1)
    OP_95(0xFE, -46520, 5600, 107590, 10000, 0x1)
    OP_95(0xFE, -41100, 5600, 100220, 10000, 0x1)
    OP_95(0xFE, -40120, 5600, 93460, 10000, 0x1)
    OP_9D(0xFE, 0xFFFF6424, 0x0, 0x1480C, 0x7D0, 0xBB8)
    OP_95(0xFE, -37970, 0, 81930, 10000, 0x1)

    def lambda_FEFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FEFC)
    OP_95(0xFE, -36970, 0, 81930, 7000, 0x0)
    Return()

    # Function_79_FE4F end

    def Function_80_FF1D(): pass

    label("Function_80_FF1D")


    def lambda_FF22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FF22)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_95(0xFE, -8490, 2500, 14030, 10000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 10000, 0x1)
    OP_95(0xFE, -720, 2500, 11820, 10000, 0x1)
    OP_95(0xFE, -290, 0, -5210, 10000, 0x1)

    def lambda_FF8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FF8B)
    OP_95(0xFE, -36970, 0, 81930, 600, 0x0)
    Return()

    # Function_80_FF1D end

    def Function_81_FFAC(): pass

    label("Function_81_FFAC")


    def lambda_FFB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FFB1)
    OP_95(0xFE, -8490, 2500, 14030, 6000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 6000, 0x1)
    OP_95(0xFE, 1100, 2500, 11650, 6000, 0x1)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_81_FFAC end

    def Function_82_10001(): pass

    label("Function_82_10001")


    def lambda_10006():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10006)
    OP_95(0xFE, -8490, 2500, 14030, 6000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 6000, 0x1)
    OP_95(0xFE, -720, 2500, 11820, 6000, 0x1)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_82_10001 end

    def Function_83_10056(): pass

    label("Function_83_10056")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50229.itc", 0x1E)
    LoadChrToIndex("apl/ch50222.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x28)
    LoadChrToIndex("chr/ch00051.itc", 0x29)
    LoadChrToIndex("apl/ch50011.itc", 0x2A)
    LoadChrToIndex("chr/ch00950.itc", 0x32)
    LoadChrToIndex("chr/ch00951.itc", 0x33)
    OP_71(0x7, 0x5, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x2)
    OP_71(0x5, 0x5, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x2)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x10)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x1F, 0x33)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -47300, 11200, 118500, 0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -46200, 11200, 121500, 315)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrPos(0x102, -47010, 11200, 125500, 0)
    SetChrPos(0x101, -47010, 11200, 125500, 0)
    SetChrPos(0x1F, -47010, 11200, 125500, 0)
    SetChrPos(0x1D, -47010, 11200, 125500, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrFlags(0x20, 0x2)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -45230, 11200, 123570, 45)
    OP_64(0xB)
    OP_64(0xC)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    BeginChrThread(0x1D, 0, 0, 79)
    OP_68(-47130, 12500, 117520, 0)
    MoveCamera(68, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_68(-46470, 8900, 108360, 3000)
    MoveCamera(113, 22, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(21500, 3000)
    Sleep(3000)
    Fade(500)
    OP_6B(0x101)
    OP_68(-47010, 12500, 125500, 0)
    MoveCamera(32, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    BeginChrThread(0x101, 0, 0, 78)
    Sleep(500)
    BeginChrThread(0x1F, 0, 0, 78)
    WaitChrThread(0x101, 0)
    Fade(500)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x1D, 0xFF)
    SetChrPos(0x101, -9490, 2500, 14030, 90)
    SetChrPos(0x1F, -9490, 2500, 14030, 90)
    SetChrPos(0x1D, -9490, 2500, 14030, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6B(0xFF)
    OP_68(-4290, 3950, 13100, 0)
    MoveCamera(39, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 3290, 10040, 4000)
    MoveCamera(67, 18, 0, 4000)
    OP_6E(540, 4000)
    SetCameraDistance(18500, 4000)
    BeginChrThread(0x1D, 0, 0, 80)
    Sleep(2000)
    BeginChrThread(0x101, 0, 0, 81)
    Sleep(1000)
    BeginChrThread(0x1F, 0, 0, 82)
    WaitChrThread(0x1F, 0)
    SetChrChipByIndex(0x1F, 0x32)
    SetChrSubChip(0x1F, 0x0)

    #C0725
    ChrTalk(
        0x1F,
        (
            "#0607F唔……\x01",
            "那种异常的速度究竟是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0726
    AnonymousTalk(
        0x101,
        (
            "#0007F兰迪、缇欧！\x01",
            "市长秘书往你们那边去了！\x02\x03",

            "他才是真正的犯人，拦住他！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("兰迪的声音")

    #A0727
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "什、什么……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0728
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "完全无法理解，但命令已收到。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 1)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_10056 end

    def Function_84_1056E(): pass

    label("Function_84_1056E")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_84_1056E end

    def Function_85_1058A(): pass

    label("Function_85_1058A")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_85_1058A end

    def Function_86_105A6(): pass

    label("Function_86_105A6")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_86_105A6 end

    def Function_87_105C2(): pass

    label("Function_87_105C2")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105DD")
    Call(0, 88)
    Jump("loc_1066C")

    label("loc_105DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105F3")
    Call(0, 88)
    Jump("loc_1066C")

    label("loc_105F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10609")
    Call(0, 88)
    Jump("loc_1066C")

    label("loc_10609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1066C")

    #C0729
    ChrTalk(
        0x101,
        (
            "#0000F现在还不是离开剧场的时候。\x02\x03",

            "外面就交给缇欧和兰迪，\x01",
            "我们专心在场内警戒吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1066C")

    SetChrPos(0x0, 0, 0, -4730, 0)
    EventEnd(0x4)
    Return()

    # Function_87_105C2 end

    def Function_88_10680(): pass

    label("Function_88_10680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_106D3")

    #C0730
    ChrTalk(
        0x101,
        (
            "#0005F啊……\x01",
            "得去见伊莉娅小姐一面呢。\x02\x03",

            "#0000F从正门进入大厅吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1074E")

    #C0731
    ChrTalk(
        0x101,
        (
            "#0000F这里似乎是二层的观众席。\x02\x03",

            "进入闲晃的话会给人家造成麻烦的，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1074E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_108C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10890")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1080A")

    #C0732
    ChrTalk(
        0x103,
        (
            "#0205F啊……\x02\x03",

            "#0200F能听到舞台上传来的音乐。\x01",
            "也许伊莉娅小姐正在练习吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "那她肯定还在舞台上呢。\x01",
            "我们就从正门进入大厅吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10888")

    label("loc_1080A")


    #C0734
    ChrTalk(
        0x103,
        (
            "#0200F能听到舞台上传来的音乐呢……\x01",
            "也许伊莉娅小姐正在练习吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        (
            "#0000F那她应该还在舞台上呢，\x01",
            "我们就从正门进入大厅吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10888")

    SetScenarioFlags(0x1, 4)
    Jump("loc_108C6")

    label("loc_10890")

    SetChrName("")

    #A0736
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊莉娅似乎在舞台那边，\x01",
            "去大厅里面看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_108C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1097F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10934")

    #C0737
    ChrTalk(
        0x102,
        (
            "#0101F罗伊德，可疑的人在右边的阶梯那里。\x01",
            "快点去吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x101,
        "#0001F……嗯！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1097F")

    label("loc_10934")


    #C0739
    ChrTalk(
        0x101,
        (
            "#0001F可疑的人在右边的阶梯那里……\x01",
            "快走吧，艾莉！\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x102,
        "#0101F……嗯！\x02",
    )

    CloseMessageWindow()

    label("loc_1097F")

    Return()

    # Function_88_10680 end

    def Function_89_10980(): pass

    label("Function_89_10980")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0741
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "舞台正在使用，\x01",
            "请各位观众\x01",
            "切勿入内。\x01",
            "    ～彩虹剧团～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A6F")

    #C0742
    ChrTalk(
        0x101,
        (
            "#0000F搜查一科似乎\x01",
            "派了不少人去后台……\x01",
            "交给他们应该没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x102,
        (
            "#0100F是啊，我们就集中精神，\x01",
            "在剧场内巡逻吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A6F")

    TalkEnd(0xFF)
    Return()

    # Function_89_10980 end

    SaveToFile()

Try(main)
