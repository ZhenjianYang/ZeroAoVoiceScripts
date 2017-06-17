from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "イリア",                 # 1
        "リーシャ",               # 2
        "カレリア",               # 3
        "支配人バルサモ",         # 4
        "受付ローランド",         # 5
        "アバン劇団長",           # 6
        "ハインツ",               # 7
        "ユージーン",             # 8
        "テオドール",             # 9
        "ニコル",                 # 10
        "プリエ",                 # 11
        "セリーヌ",               # 12
        "シュリ",                 # 13
        "イリア",                 # 14
        "ユージーン",             # 15
        "セリーヌ",               # 16
        "観客",                   # 17
        "観客",                   # 18
        "観客",                   # 19
        "観客",                   # 20
        "マクダエル市長",         # 21
        "秘書アーネスト",         # 22
        "グレイス",               # 23
        "ダドリー捜査官",         # 24
        "警官",                   # 25
        "客",                     # 26
        "客",                     # 27
        "客",                     # 28
        "客",                     # 29
        "客",                     # 30
        "客",                     # 31
        "客",                     # 32
        "客",                     # 33
        "客",                     # 34
        "客",                     # 35
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
        "Function_9_22C9",         # 09, 9
        "Function_10_22CD",        # 0A, 10
        "Function_11_242A",        # 0B, 11
        "Function_12_35C0",        # 0C, 12
        "Function_13_35C4",        # 0D, 13
        "Function_14_3695",        # 0E, 14
        "Function_15_394D",        # 0F, 15
        "Function_16_3B63",        # 10, 16
        "Function_17_3E40",        # 11, 17
        "Function_18_4704",        # 12, 18
        "Function_19_4A58",        # 13, 19
        "Function_20_4E6D",        # 14, 20
        "Function_21_4F7B",        # 15, 21
        "Function_22_5324",        # 16, 22
        "Function_23_54BE",        # 17, 23
        "Function_24_5890",        # 18, 24
        "Function_25_60FF",        # 19, 25
        "Function_26_6688",        # 1A, 26
        "Function_27_6BE3",        # 1B, 27
        "Function_28_6F3D",        # 1C, 28
        "Function_29_7CA2",        # 1D, 29
        "Function_30_7D7C",        # 1E, 30
        "Function_31_8040",        # 1F, 31
        "Function_32_814C",        # 20, 32
        "Function_33_81CA",        # 21, 33
        "Function_34_8245",        # 22, 34
        "Function_35_82B6",        # 23, 35
        "Function_36_832E",        # 24, 36
        "Function_37_8AE1",        # 25, 37
        "Function_38_8B46",        # 26, 38
        "Function_39_8B62",        # 27, 39
        "Function_40_8F03",        # 28, 40
        "Function_41_9154",        # 29, 41
        "Function_42_93AF",        # 2A, 42
        "Function_43_96C6",        # 2B, 43
        "Function_44_98AE",        # 2C, 44
        "Function_45_9974",        # 2D, 45
        "Function_46_9A3A",        # 2E, 46
        "Function_47_9AFA",        # 2F, 47
        "Function_48_A564",        # 30, 48
        "Function_49_ABF4",        # 31, 49
        "Function_50_CD04",        # 32, 50
        "Function_51_CD3B",        # 33, 51
        "Function_52_CD7F",        # 34, 52
        "Function_53_CDC3",        # 35, 53
        "Function_54_DD43",        # 36, 54
        "Function_55_DD7E",        # 37, 55
        "Function_56_DDB9",        # 38, 56
        "Function_57_E4F9",        # 39, 57
        "Function_58_E65E",        # 3A, 58
        "Function_59_E78F",        # 3B, 59
        "Function_60_E956",        # 3C, 60
        "Function_61_EAF8",        # 3D, 61
        "Function_62_ECC1",        # 3E, 62
        "Function_63_EEA4",        # 3F, 63
        "Function_64_F021",        # 40, 64
        "Function_65_F14B",        # 41, 65
        "Function_66_F258",        # 42, 66
        "Function_67_F441",        # 43, 67
        "Function_68_F588",        # 44, 68
        "Function_69_F784",        # 45, 69
        "Function_70_F930",        # 46, 70
        "Function_71_FB1B",        # 47, 71
        "Function_72_FFD0",        # 48, 72
        "Function_73_10017",       # 49, 73
        "Function_74_11020",       # 4A, 74
        "Function_75_11089",       # 4B, 75
        "Function_76_110F2",       # 4C, 76
        "Function_77_1114E",       # 4D, 77
        "Function_78_11458",       # 4E, 78
        "Function_79_1151B",       # 4F, 79
        "Function_80_115E9",       # 50, 80
        "Function_81_11678",       # 51, 81
        "Function_82_116CD",       # 52, 82
        "Function_83_11722",       # 53, 83
        "Function_84_11C3E",       # 54, 84
        "Function_85_11C5A",       # 55, 85
        "Function_86_11C76",       # 56, 86
        "Function_87_11C92",       # 57, 87
        "Function_88_11D5C",       # 58, 88
        "Function_89_120B2",       # 59, 89
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
            "脚本と出演順を調整して\x01",
            "上演の段取りは何とかついたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xD,
        (
            "……本当は\x01",
            "ニコル君が戻ってきてくれるのが\x01",
            "一番いいんだが……\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_16C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1626")

    #C0003
    ChrTalk(
        0xB,
        (
            "やはりニコルさんは\x01",
            "戻って来られないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xB,
        (
            "もしやと思い\x01",
            "気を配っているのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C0")

    label("loc_1626")


    #C0005
    ChrTalk(
        0xB,
        (
            "ニコルさんは\x01",
            "戻って来られないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xB,
        (
            "困りましたね……\x01",
            "そろそろ上演の時間でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "やはり代役を立てて\x01",
            "進めるほかありませんか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16C0")

    Jump("loc_22C5")

    label("loc_16C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1747")

    #C0008
    ChrTalk(
        0xFE,
        (
            "楽屋や客席の方は\x01",
            "私たちで気を配っておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "ふう……ニコルさんが\x01",
            "戻ってきてくださるといいんですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C5")

    label("loc_1747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_194F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1762")
    Call(0, 10)
    Jump("loc_194A")

    label("loc_1762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1802")

    #C0010
    ChrTalk(
        0xB,
        (
            "シュリはイリアさんの稽古を\x01",
            "食い入るように見ていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "ずば抜けたセンスもあるようですし、\x01",
            "将来大物になるかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18ED")

    label("loc_1802")


    #C0012
    ChrTalk(
        0xB,
        (
            "シュリは絶対に\x01",
            "舞台に上がろうとしないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "しばらくは下働きだけさせてくれ……\x01",
            "そういう事のようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        (
            "フフ、そのくせイリアさんの稽古は\x01",
            "食い入るように見ています。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "……あの子は将来\x01",
            "大物になるかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18ED")

    Jump("loc_194A")

    label("loc_18F2")


    #C0016
    ChrTalk(
        0xB,
        (
            "さて、本日も\x01",
            "午後からは公演がございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "今の時間に\x01",
            "掃除をしておきませんと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194A")

    Jump("loc_22C5")

    label("loc_194F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196A")
    Call(0, 10)
    Jump("loc_1A77")

    label("loc_196A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19DB")

    #C0018
    ChrTalk(
        0xB,
        "そろそろ夜の部の上演でございます。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "お客様にはごゆっくり\x01",
            "楽しんでいただきたいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_19DB")


    #C0020
    ChrTalk(
        0xB,
        "いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "劇団アルカンシェルは\x01",
            "本日『金の太陽、銀の月』を\x01",
            "上演いたしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "どうか最後まで\x01",
            "ごゆっくりお楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A77")

    Jump("loc_22C5")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1ABF")

    #C0023
    ChrTalk(
        0xB,
        (
            "右奥の階段の上です！\x01",
            "どうかお急ぎください……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C5")

    label("loc_1ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_1BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE1")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B3A")

    #C0024
    ChrTalk(
        0xB,
        "舞台も残るはあと少し。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "どうやら本日は\x01",
            "何事もなかったようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9C")

    label("loc_1B3A")


    #C0026
    ChrTalk(
        0xB,
        "舞台も盛り上がって参りましたね。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "招待客様にも楽しんで\x01",
            "いただけたようで何よりですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B9C")

    Jump("loc_22C5")

    label("loc_1BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC3")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C2F")

    #C0028
    ChrTalk(
        0xB,
        (
            "舞台も第二幕……\x01",
            "滞りなく進んでいるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "この盛況ですと\x01",
            "本公演が楽しみですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB6")

    label("loc_1C2F")


    #C0030
    ChrTalk(
        0xB,
        "見回り、ご苦労様でございます。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        (
            "舞台も第二幕……\x01",
            "滞りなく進んでいるようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "この盛況ですと\x01",
            "本公演が楽しみですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CB6")

    Jump("loc_22C5")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_1E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDD")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D7E")

    #C0033
    ChrTalk(
        0xB,
        (
            "私も目を光らせていましたが、\x01",
            "お客様はみな\x01",
            "ご招待した方ばかりでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "どうやら何事もない様子……\x01",
            "ひとまず安心といった所でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0A")

    label("loc_1D7E")


    #C0035
    ChrTalk(
        0xB,
        "上演も無事始まりました。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        "どうやら何事もないようですね。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        (
            "不審な方も見当たりませんし……\x01",
            "ひとまず安心といった所でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E0A")

    Jump("loc_22C5")

    label("loc_1E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1ECF")

    #C0038
    ChrTalk(
        0xB,
        (
            "ちなみに現在は\x01",
            "２階席を確認なさっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        (
            "プレ公演まであと少し……\x01",
            "舞台にとって大事な時期なのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "これも場内警備のため。\x01",
            "仕方ない事なのでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAD")

    label("loc_1ECF")


    #C0041
    ChrTalk(
        0xB,
        (
            "捜査一課の方が劇場内を\x01",
            "見て回っておられるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "稽古の最中に歩き回られたり\x01",
            "衣装室をかき回したりなされて……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        "ふう、何かと落ち着きません。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "しかしこれも場内警備のため。\x01",
            "仕方ない事なのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1FAD")

    Jump("loc_22C5")

    label("loc_1FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_20ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2028")

    #C0045
    ChrTalk(
        0xB,
        (
            "プレ公演は、今回の新作が\x01",
            "初めて披露される場でもあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        "すべて丹念に進めなければ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20E8")

    label("loc_2028")


    #C0047
    ChrTalk(
        0xB,
        (
            "プレ公演にお招きする\x01",
            "お客様のリストを纏めているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "皆様、劇団のスポンサーであったり\x01",
            "ご関心賜っている方々ですので。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "お手紙も一通一通丹念に\x01",
            "書かせてもらっているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20E8")

    Jump("loc_22C5")

    label("loc_20ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2184")

    #C0050
    ChrTalk(
        0xB,
        (
            "皆様、本日はどうも\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "ともあれ警察の方に\x01",
            "警備をして頂けるようですし……\x01",
            "私たちもこれで安心でございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C5")

    label("loc_2184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2209")

    #C0052
    ChrTalk(
        0xB,
        (
            "このような事で\x01",
            "稽古に取り組む団員達の\x01",
            "気を煩わせたくはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "どうか捜査の方は\x01",
            "よろしくお願い致します。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C5")

    label("loc_2209")


    #C0054
    ChrTalk(
        0xB,
        (
            "これまでにも悪戯半分の脅迫文が\x01",
            "届く事はありましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "今回は文面といい署名といい、\x01",
            "ただの悪戯ではないようなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "皆様、支配人の私からも\x01",
            "よろしくお願い申し上げます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22C5")

    TalkEnd(0xB)
    Return()

    # Function_8_15AC end

    def Function_9_22C9(): pass

    label("Function_9_22C9")

    Call(0, 8)
    Return()

    # Function_9_22C9 end

    def Function_10_22CD(): pass

    label("Function_10_22CD")


    #C0057
    ChrTalk(
        0xFE,
        (
            "そうそう、当劇団では\x01",
            "新しい下働きの子を雇いましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "シュリと申します。\x01",
            "見かけたら仲良くしてやって下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2426")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2395")

    #C0059
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、元気にやっている\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2426")

    label("loc_2395")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23E1")

    #C0060
    ChrTalk(
        0x103,
        (
            "#0200F……どうやら元気に\x01",
            "やっているみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2426")

    label("loc_23E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2426")

    #C0061
    ChrTalk(
        0x104,
        (
            "#0300Fへっ、どうやら\x01",
            "元気にやってるみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2426")

    SetScenarioFlags(0xD1, 6)
    Return()

    # Function_10_22CD end

    def Function_11_242A(): pass

    label("Function_11_242A")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_25D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2543")

    #C0062
    ChrTalk(
        0xC,
        (
            "どんな非常事態でも\x01",
            "舞台に関しては妥協しない\x01",
            "人たちですからね……\x02\x03",

            "まったくやきもきしますよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        (
            "あ、ちなみに本日の公演は\x01",
            "夕方から行われる事になりまして……\x01",
            "現在、各所に通達中なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "皆さんにはご迷惑をお掛けして\x01",
            "大変申しわけございません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25CF")

    label("loc_2543")


    #C0065
    ChrTalk(
        0xC,
        (
            "イ、イリアさんと劇団長、\x01",
            "うまく折り合いついたんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "ずっと脚本の事で\x01",
            "話し込んでいたんですよ……\x01",
            "まったくこんな時に……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_25CF")

    Jump("loc_35BC")

    label("loc_25D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_268E")
    OP_4B(0xB, 0xFF)

    #C0067
    ChrTalk(
        0xC,
        (
            "分かりました、正面ホールは\x01",
            "自分が気を付けておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "後はシュリさんにも\x01",
            "伝えておかないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "あの子は細かい事にも\x01",
            "よく気がつきますからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_2812")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2712")

    #C0070
    ChrTalk(
        0xC,
        (
            "客席ホールの方へ\x01",
            "お越しいただいてよろしいですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "お時間があれば劇団長の相談に\x01",
            "乗っていただきたいんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2812")

    label("loc_2712")


    #C0072
    ChrTalk(
        0xC,
        "あ、確か警察の方……ですよね。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        (
            "#0105Fえ、ええ、そうですけど……\x01",
            "（何かあったのかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "あのう、できれば\x01",
            "客席ホールの方へお越しいただいて\x01",
            "よろしいですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xC,
        (
            "劇団長が困っておられまして……\x01",
            "相談に乗っていだたけると\x01",
            "嬉しいんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2812")

    Jump("loc_35BC")

    label("loc_2817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2832")
    Call(0, 13)
    Jump("loc_296F")

    label("loc_2832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28BD")

    #C0076
    ChrTalk(
        0xC,
        (
            "イリアさんやリーシャさんもそうですが\x01",
            "アーティストの方の情熱には驚かされます。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        "自分達職員も負けてはいられませんね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_296F")

    label("loc_28BD")


    #C0078
    ChrTalk(
        0xC,
        (
            "ニコルさんという\x01",
            "アーティストの方がいるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        (
            "最近とても頑張って\x01",
            "稽古なさっているみたいですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xC,
        (
            "昨晩は徹夜だったとか。\x01",
            "いやはや、情熱には驚かされますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_296F")

    Jump("loc_35BC")

    label("loc_2974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2A90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298F")
    Call(0, 13)
    Jump("loc_2A8B")

    label("loc_298F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29EE")

    #C0081
    ChrTalk(
        0xC,
        "上演まであと１０分少々……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "本日も皆さんに\x01",
            "楽しんで頂きたいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8B")

    label("loc_29EE")


    #C0083
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "こちらではチケットの確認を\x01",
            "させていただいております。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "なお本日の通常席分は\x01",
            "すでに完売となっております。\x01",
            "ご了承くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2A8B")

    Jump("loc_35BC")

    label("loc_2A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAB")
    Call(0, 13)
    Jump("loc_2C44")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B30")

    #C0085
    ChrTalk(
        0xC,
        (
            "本日は休館日ですが\x01",
            "自主練に来ている方も\x01",
            "いらっしゃいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "よろしかったらお会いに\x01",
            "なられてはいかがですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C44")

    label("loc_2B30")


    #C0087
    ChrTalk(
        0xC,
        "新作の舞台は大好評ですよ。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        (
            "本日まで客席はほぼ満席、\x01",
            "チケットも２ヶ月先まで完売です。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "……もっとも、本日は休館日なので\x01",
            "上演はないんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0000Fあはは、そうなんですか。\x02\x03",

            "#0003F（ま、今日はキーアを連れているし\x01",
            "  舞台鑑賞するわけにもいかないけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C44")

    Jump("loc_35BC")

    label("loc_2C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2C83")

    #C0091
    ChrTalk(
        0xC,
        "ふ、不審なお客様？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        "ま、まさか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_2C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_2D6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA5")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D16")

    #C0093
    ChrTalk(
        0xC,
        "こちらは全く異常ありません。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        (
            "捜査一課の方も張り込んでいますし、\x01",
            "賊も諦めたんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D68")

    label("loc_2D16")


    #C0095
    ChrTalk(
        0xC,
        "こちらは全く異常ありません。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "上演中ですし、\x01",
            "人っ子一人通りませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D68")

    Jump("loc_35BC")

    label("loc_2D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8F")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E08")

    #C0097
    ChrTalk(
        0xC,
        "リーシャさんの初舞台です。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xC,
        (
            "練習に付き合っていたせいでしょうか。\x01",
            "こちらまで緊張してしまいますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9C")

    label("loc_2E08")


    #C0099
    ChrTalk(
        0xC,
        (
            "いよいよ第二幕、\x01",
            "リーシャさんの初舞台ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xC,
        (
            "きっと大丈夫ですよ。\x01",
            "なんと言っても、あのイリアさんも\x01",
            "認めた才能の持ち主なんですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E9C")

    Jump("loc_35BC")

    label("loc_2EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_2F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC3")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EC3")


    #C0101
    ChrTalk(
        0xC,
        "上演が始まったようですね……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xC,
        "何事もなければいいんですけど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_2F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3033")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F8A")

    #C0103
    ChrTalk(
        0xC,
        (
            "早朝から捜査一課の方が\x01",
            "見えているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xC,
        (
            "今日の稽古は\x01",
            "いささか遅れるようです。\x01",
            "ふう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302E")

    label("loc_2F8A")


    #C0105
    ChrTalk(
        0xC,
        (
            "早朝から捜査一課の方が\x01",
            "見えているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "団員の皆さんは\x01",
            "気にしてないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "事情聴取なんかもあって\x01",
            "今日の稽古はいささか遅れるようです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_302E")

    Jump("loc_35BC")

    label("loc_3033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_30F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30A5")

    #C0108
    ChrTalk(
        0xC,
        (
            "自分達はこれから新作発表の\x01",
            "打ち合わせがありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        "これから忙しくなりますよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F3")

    label("loc_30A5")


    #C0110
    ChrTalk(
        0xC,
        (
            "これは皆さん。\x01",
            "本日はお疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xC,
        "どうか帰りもお気を付けて。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_30F3")

    Jump("loc_35BC")

    label("loc_30F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_318E")

    #C0112
    ChrTalk(
        0xC,
        (
            "おや……\x01",
            "劇団長やイリアさんに\x01",
            "御用でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "先ほどから正面ホールで\x01",
            "稽古をなさっています。\x01",
            "どうぞ、このままお進みください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_318E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_33D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_328E")

    #C0114
    ChrTalk(
        0xC,
        (
            "今回は《炎の舞姫》イリアさん主演の\x01",
            "５作目の大型新作……\x01",
            "騒がれるのも無理ないことでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "かくいう自分も\x01",
            "実はイリアさんのファンでして。\x01",
            "ここに就職したというわけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        (
            "団員や職員の中にも\x01",
            "結構多いんですよ、そういう方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D2")

    label("loc_328E")


    #C0117
    ChrTalk(
        0xC,
        (
            "アルカンシェルの新作は\x01",
            "大体年に１本程度\x01",
            "公開されるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "作品によっては１年半だったりと\x01",
            "結構まちまちなんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "だから新作が発表されるたびに\x01",
            "ちょっとした騒動になるわけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "今回は《炎の舞姫》イリアさんが\x01",
            "デビューなさってから\x01",
            "５作目の大型新作……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xC,
        (
            "まあ、騒がれるのも\x01",
            "無理ないことでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_33D2")

    Jump("loc_35BC")

    label("loc_33D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_3563")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3465")

    #C0122
    ChrTalk(
        0xC,
        (
            "それにしてもこの時期に\x01",
            "脅迫文騒ぎだなんて……\x01",
            "困った事になりましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "早く悪戯だと\x01",
            "判明するといいんですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_355E")

    label("loc_3465")


    #C0124
    ChrTalk(
        0xC,
        (
            "新作公開前のこの時期に\x01",
            "脅迫文騒ぎだなんて……\x01",
            "困った事になりましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xC,
        (
            "早く悪戯だと\x01",
            "判明するといいんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "ともかく、皆さんには\x01",
            "全面的に協力するよう\x01",
            "言い付かっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        (
            "何かご不明な事がありましたら\x01",
            "遠慮なくお尋ねください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_355E")

    Jump("loc_35BC")

    label("loc_3563")


    #C0128
    ChrTalk(
        0xC,
        (
            "皆さま、\x01",
            "劇団《アルカンシェル》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        "どうぞホールの方へお進みください。\x02",
    )

    CloseMessageWindow()

    label("loc_35BC")

    TalkEnd(0xC)
    Return()

    # Function_11_242A end

    def Function_12_35C0(): pass

    label("Function_12_35C0")

    Call(0, 11)
    Return()

    # Function_12_35C0 end

    def Function_13_35C4(): pass

    label("Function_13_35C4")


    #C0130
    ChrTalk(
        0xC,
        (
            "シュリさんという方が\x01",
            "新しく入ったのですが……\x01",
            "本当に働き者ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "飲み込みも早いですし、\x01",
            "何より積極的です。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        (
            "まだアーティストになるつもりは\x01",
            "ないみたいですが……\x01",
            "居てくれると大助かりですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 7)
    Return()

    # Function_13_35C4 end

    def Function_14_3695(): pass

    label("Function_14_3695")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3768")

    #C0133
    ChrTalk(
        0x8,
        (
            "#1703F昼の公演は４時に延期……\x01",
            "それまでに完璧に仕上げないとね。\x02\x03",

            "#1700Fま、ウチは全員がプロだもの。\x01",
            "何とかなるっしょ。\x02\x03",

            "#1709Fリハ１回だけのぶっつけ本番……\x01",
            "うーん、燃えてきたわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_376B")

    label("loc_3768")

    Call(0, 15)

    label("loc_376B")

    Jump("loc_3949")

    label("loc_3770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_37F3")

    #C0134
    ChrTalk(
        0x8,
        (
            "#1706Fカレリアさんは\x01",
            "昔っから口煩いのよね～。\x02\x03",

            "#1700Fま、平気よ。\x01",
            "こう見えてあたしは\x01",
            "稽古には絶対遅れないから！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3949")

    label("loc_37F3")


    #C0135
    ChrTalk(
        0x8,
        (
            "#1706Fふぁ～ああ……\x02\x03",

            "#1705Fあら弟君たちじゃない。\x01",
            "おはよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#0012Fイ、イリアさん。\x01",
            "何だか眠そうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "#1706Fん～、今朝は\x01",
            "ちょっ～と寝坊をね。\x02\x03",

            "#1700F……ああ、平気よ。\x01",
            "稽古には穴を開けてないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#0105Fそ、そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0301F（ちょっぴりプライベートの\x01",
            "  生イリア……）\x02\x03",

            "#0309F（く～っ、得した気分だな！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3949")

    TalkEnd(0xFE)
    Return()

    # Function_14_3695 end

    def Function_15_394D(): pass

    label("Function_15_394D")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0140
    ChrTalk(
        0xD,
        (
            "やれやれ、ようやく\x01",
            "脚本の調整が付いたよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xD,
        (
            "イリア君が食い下がるものだから\x01",
            "予想外に時間が掛かってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#1706F#11Pだってこのシーンは\x01",
            "絶対にレベル落としたくないんだもの。\x02\x03",

            "#1702F稽古でも力入れてるし\x01",
            "このくらいは当然よね！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xD,
        (
            "だからって食い下がりすぎだと\x01",
            "思うんだがねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xD,
        (
            "しかしまあ、今日は昼公演だけで\x01",
            "ラッキーだったかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xD,
        (
            "時間も無いことだし、\x01",
            "とっととリハに入るとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        "#1709F#11Pええ！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        (
            "#0202F（苦労はあったようですが\x01",
            "  うまく行ったみたいですね。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_394D end

    def Function_16_3B63(): pass

    label("Function_16_3B63")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BF7")
    Jump("loc_3C41")

    label("loc_3BF7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C17")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C41")

    label("loc_3C17")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C37")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C41")

    label("loc_3C37")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C41")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3CD9")

    #C0148
    ChrTalk(
        0x15,
        (
            "#6102F今日はあのシーンの精度を\x01",
            "もう少し上げられるはず……\x02\x03",

            "#6109Fよーし、張り切っていくわよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E38")

    label("loc_3CD9")


    #C0149
    ChrTalk(
        0x15,
        "#6105Fあら、弟君たち。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#0002Fこんばんは、イリアさん。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#0302Fこれから公演ッスか？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x15,
        (
            "#6104Fええ、そろそろ\x01",
            "お客さんが入ってくる頃ね。\x02\x03",

            "#6102F次はあのシーンの精度を\x01",
            "もう少し上げられるはず……\x02\x03",

            "#6109Fよーし、張り切っていくわよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        (
            "#0109F（ふふっ。\x01",
            "  イリアさんは相変わらずね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        (
            "#0204F（ええ……\x01",
            "  妙に安心してしまいます。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3E38")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_3B63 end

    def Function_17_3E40(): pass

    label("Function_17_3E40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_3F3C")

    #C0155
    ChrTalk(
        0x9,
        (
            "#1802Fニコルさん、最近どこかで\x01",
            "特訓でもしたらしくて……\x01",
            "かなり力を付けたみたいなんです。\x02\x03",

            "#1806F悪い事じゃないと思うんですけど、\x01",
            "性格までまるで変わってしまって。\x02\x03",

            "#1808F前とは別人みたいだから\x01",
            "ちょっと心配なんですよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F3F")

    label("loc_3F3C")

    Call(0, 18)

    label("loc_3F3F")

    Jump("loc_4700")

    label("loc_3F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_40DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3FE1")

    #C0156
    ChrTalk(
        0x9,
        (
            "#6202F最近ようやく、人前に出るのが\x01",
            "そんなに緊張しなくなったんです。\x02\x03",

            "#6209Fふふっ、イリアさんのようには\x01",
            "まだまだ行きませんけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_3FE1")


    #C0157
    ChrTalk(
        0x9,
        (
            "#6202Fあ、皆さん！\x02\x03",

            "ひょっとして公演を\x01",
            "見に来てくださったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0012Fいや……\x01",
            "見たいのは山々なんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        (
            "#0102Fちょっと用事で近くに来たから\x01",
            "挨拶に伺っただけなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "#6209Fふふっ、そうでしたか。\x01",
            "遅くまでお疲れさまです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_40D8")

    Jump("loc_4700")

    label("loc_40DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_431A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 4)), scpexpr(EXPR_END)), "loc_417D")

    #C0161
    ChrTalk(
        0x9,
        (
            "#1802F明日からは\x01",
            "本当に最後の仕上げなんです。\x02\x03",

            "#1804F毎日リハーサルもあるし……\x01",
            "私も気持ちを切り替えて\x01",
            "頑張らないといけませんよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4315")

    label("loc_417D")


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
            "#0005Fリーシャ……？\x01",
            "どうかしたのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 750)

    #C0164
    ChrTalk(
        0x9,
        (
            "#1805Fあ、いえ……\x02\x03",

            "#1806Fプレ公演も近づいているので、\x01",
            "少し緊張してしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        "#0300Fそういや、あと一週間くらいか。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "#1802Fはい、明日からは\x01",
            "本当に最後の仕上げなんです。\x02\x03",

            "#1804F……私も、気持ちを切り替えて\x01",
            "いかなきゃダメですよね。\x02\x03",

            "#1808F皆さんの稽古に\x01",
            "置いて行かれないように\x01",
            "頑張らないと。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x91, 4)

    label("loc_4315")

    Jump("loc_4700")

    label("loc_431A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 3)), scpexpr(EXPR_END)), "loc_43EC")

    #C0167
    ChrTalk(
        0x9,
        (
            "#1806F今回の公演だって\x01",
            "全然自信は無いんですけど……\x02\x03",

            "#1802Fイリアさんが\x01",
            "才能があると言ってくれた言葉を\x01",
            "信じてみようと思うんです。\x02\x03",

            "#1804F……まだまだ稽古不足で\x01",
            "足を引っ張ってばかりですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4700")

    label("loc_43EC")


    #C0168
    ChrTalk(
        0x9,
        (
            "#1805Fあ、皆さん……\x02\x03",

            "#1806Fすみません、稽古の支度で\x01",
            "バタバタしてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#0002Fはは、忙しそうだね。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x104,
        "#0302Fま、期待の大型新人だもんな。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "#1809Fあはは……\x02\x03",

            "#1810F……実は私、\x01",
            "劇団に入るつもりなんて\x01",
            "無かったんですけど……\x02",
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
        "#0105Fあら……そうだったの？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        (
            "#1802Fはい、有名なアルカンシェルの舞台を\x01",
            "一度見てみたかっただけなんですけど。\x02\x03",

            "#1806Fその、公開練習を見学していた時に\x01",
            "偶然イリアさんに\x01",
            "目を付けられてしまって。\x02\x03",

            "『あなたには才能がある！』\x01",
            "……とか何とか言って、そのまま\x01",
            "入団させられてしまったんです。\x02",
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
        "#0206F……目に浮かぶようですね。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#0012Fはは……\x01",
            "本当に強引な人だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 3)

    label("loc_4700")

    TalkEnd(0xFE)
    Return()

    # Function_17_3E40 end

    def Function_18_4704(): pass

    label("Function_18_4704")

    OP_4B(0x9, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0176
    ChrTalk(
        0x9,
        (
            "#1806Fあの、プリエさん……\x01",
            "ニコルさんの事なんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x12,
        (
            "そうねぇ、私もさすがに\x01",
            "おかしいって思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x12,
        "あれじゃあまるで別人だもの。\x02",
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
        "#0005Fあの……どうかしたんですか？\x02",
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
        "あらぁ、警察の人たち。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x12,
        (
            "まあ大したことじゃないんだけどね。\x01",
            "ニコル君について、ちょっと。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "#1806Fニコルさん、最近どこかで\x01",
            "特訓でもしたらしくて……\x02\x03",

            "凄い技術とパフォーマンス力を\x01",
            "身に付けたみたいなんですけど……\x02\x03",

            "#1808Fその、何だか様子まで\x01",
            "変わってしまったみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x104,
        (
            "#0301Fへえ……？\x01",
            "様子が変わったねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#0103F人ってときどき\x01",
            "そういう事があるらしいけど……\x02\x03",

            "#0100F一晩で見間違えるほど変わったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "#1804Fそうですね。\x01",
            "きっかけがあれば変わるものだし……\x02\x03",

            "#1810F……きっとニコルさんも\x01",
            "何か掴んだのかもしれませんね。\x02",
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

    # Function_18_4704 end

    def Function_19_4A58(): pass

    label("Function_19_4A58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4AD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4ACE")

    #C0187
    ChrTalk(
        0xF,
        (
            "王子様役の俺が\x01",
            "物乞い役を兼任だなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xF,
        (
            "ううっ、悲しい……\x01",
            "納得がいかないぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD1")

    label("loc_4ACE")

    Call(0, 20)

    label("loc_4AD1")

    Jump("loc_4E69")

    label("loc_4AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4B3E")

    #C0189
    ChrTalk(
        0xF,
        (
            "ニコルは最近\x01",
            "熱心に練習していた……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xF,
        "いい傾向だと思ってたんだけどな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BE4")

    label("loc_4B3E")


    #C0191
    ChrTalk(
        0xF,
        (
            "ニコルのやつ、最近\x01",
            "夜中まで練習してたみたいだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xF,
        (
            "……急に熱心になったから\x01",
            "おかしいとは思ってたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xF,
        (
            "くそっ……イキナリ\x01",
            "姿を消すかよ、普通……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4BE4")

    Jump("loc_4E69")

    label("loc_4BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4CEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4C48")

    #C0194
    ChrTalk(
        0xF,
        (
            "ニコルの奴、まるで別人だな。\x01",
            "よくあそこまで\x01",
            "稽古を積んだものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE6")

    label("loc_4C48")


    #C0195
    ChrTalk(
        0xF,
        (
            "ニコルは最近\x01",
            "急に腕を上げたと思わないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xF,
        (
            "前はウジウジしてやがったけど\x01",
            "まるで別人じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xF,
        (
            "ふっ……あいつなりに\x01",
            "何か吹っ切れたのかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4CE6")

    Jump("loc_4E69")

    label("loc_4CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4D87")

    #C0198
    ChrTalk(
        0xF,
        (
            "今の時期は普通の公演はナシ。\x01",
            "新作に向けてバリバリ\x01",
            "リハーサルがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xF,
        (
            "気をつけてないと\x01",
            "本番までに衣装がぼろぼろに\x01",
            "なっちまうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E69")

    label("loc_4D87")


    #C0200
    ChrTalk(
        0xF,
        "どうだい、キラキラの王子服だろう。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xF,
        (
            "ふっ、新作『金の太陽、銀の月』でも\x01",
            "オレ様は王子様役だからな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xF,
        (
            "……でも調子乗ってると\x01",
            "本番までにほつれて来るんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xF,
        (
            "アルカンシェルの舞台は\x01",
            "動きが激しいからなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4E69")

    TalkEnd(0xFE)
    Return()

    # Function_19_4A58 end

    def Function_20_4E6D(): pass

    label("Function_20_4E6D")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0204
    ChrTalk(
        0xF,
        (
            "おいおい、俺の役\x01",
            "短くなってるじゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x10,
        (
            "俺の役は長くなった……\x01",
            "ローテーションの\x01",
            "時間稼ぎだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xF,
        (
            "で、その時間に着替えて\x01",
            "俺が物乞い役で出ると。\x02",
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
        "マジでやるのか、これ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_20_4E6D end

    def Function_21_4F7B(): pass

    label("Function_21_4F7B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_500F")
    Jump("loc_5059")

    label("loc_500F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_502F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5059")

    label("loc_502F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_504F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5059")

    label("loc_504F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5059")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_510A")
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)

    #C0209
    ChrTalk(
        0x16,
        (
            "そういやニコルの奴、\x01",
            "昨日、派手なアクロバットやってたよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x16,
        (
            "あいつってあんなに\x01",
            "目立ちたがり屋だっけか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    Jump("loc_531C")

    label("loc_510A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_51C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_51B8")
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)

    #C0211
    ChrTalk(
        0x16,
        (
            "はは～ん、\x01",
            "さては自信が無いんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x16,
        (
            "やはりトップ男優は\x01",
            "オレ様で決定か。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x10,
        (
            "フゥ……お前はお馬鹿な\x01",
            "発言ばかりだな、ユージーン。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    Jump("loc_51BB")

    label("loc_51B8")

    Call(0, 22)

    label("loc_51BB")

    Jump("loc_531C")

    label("loc_51C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5272")

    #C0214
    ChrTalk(
        0x16,
        (
            "脅迫文なんて\x01",
            "スターなら珍しくもない代物さ。\x01",
            "オレも何度か受け取ったことがあるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x16,
        (
            "ふっ、この\x01",
            "《アルカンシェルの王子》ユージーンも\x01",
            "男どもに敵が多いからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531C")

    label("loc_5272")


    #C0216
    ChrTalk(
        0x16,
        "ああ、君達が警察の人かい？\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x16,
        (
            "ふっ、ご苦労な事だね。\x01",
            "あんな悪戯をいちいち調査だなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x16,
        (
            "脅迫文なんて\x01",
            "スターなら珍しくもない代物さ。\x01",
            "調べるだけ無駄だって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_531C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_4F7B end

    def Function_22_5324(): pass

    label("Function_22_5324")

    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "青年男優が慣れた手つきで\x01",
            "同僚の髪をセットしている。\x02",
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
            "テオドール、\x01",
            "今度の公演で賭けないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x16,
        (
            "どっちが多く\x01",
            "女性客をメロメロにするかさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x16,
        (
            "ふっ、そうだな。\x01",
            "一週間で受け取るラブレターの数\x01",
            "ってのはどうだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        "…………………………（グキッ）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x16, 0x0, 0x14, 0x258, 0xBB8)
    Sleep(500)

    #C0224
    ChrTalk(
        0x16,
        "あででで……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x16,
        (
            "こら、ヘアセット係！\x01",
            "なんて事しやがる！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x16)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_22_5324 end

    def Function_23_54BE(): pass

    label("Function_23_54BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5529")
    OP_4B(0xF, 0xFF)

    #C0226
    ChrTalk(
        0x10,
        "軽くリハが必要だな。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x10,
        (
            "ユージーン、嘆いてないで\x01",
            "台本をあわせろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_552C")

    label("loc_5529")

    Call(0, 20)

    label("loc_552C")

    Jump("loc_588C")

    label("loc_5531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_55FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_557B")

    #C0228
    ChrTalk(
        0xFE,
        (
            "今日も公演があるが……\x01",
            "果たしてどうなるか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55F9")

    label("loc_557B")


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
            "こういう出来事があると\x01",
            "劇団のテンションが下がるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x10,
        "舞台に影響が出ないか心配だ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_55F9")

    Jump("loc_588C")

    label("loc_55FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5643")
    OP_4B(0xF, 0xFF)

    #C0232
    ChrTalk(
        0x10,
        (
            "………………………………\x01",
            "気に食わんな……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_588C")

    label("loc_5643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5695")
    OP_4B(0xF, 0xFF)

    #C0233
    ChrTalk(
        0x10,
        "……ユージーン、うるさいぞ。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x10,
        "読書の邪魔をするな。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_588C")

    label("loc_5695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5707")

    #C0235
    ChrTalk(
        0x10,
        "やはり空き時間は読書に限るな。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x10,
        (
            "本は精神の糧……\x01",
            "お前たちもなるべく\x01",
            "読書を心がけるといい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588C")

    label("loc_5707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5758")

    #C0237
    ChrTalk(
        0x10,
        "……何か忘れ物か？\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x10,
        (
            "劇団長なら\x01",
            "ホールの方にいるはずだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588C")

    label("loc_5758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_57C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_57B8")

    #C0239
    ChrTalk(
        0x10,
        "リーシャに用事か？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x10,
        (
            "隣の衣装室にいるはずだ。\x01",
            "行ってみるといい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57BB")

    label("loc_57B8")

    Call(0, 22)

    label("loc_57BB")

    Jump("loc_588C")

    label("loc_57C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5824")

    #C0241
    ChrTalk(
        0x10,
        (
            "…………………………\x01",
            "悪いが俺は役作り中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x10,
        (
            "騒ぎたいのなら\x01",
            "出て行くんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588C")

    label("loc_5824")


    #C0243
    ChrTalk(
        0x10,
        "知らない顔だな。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x10,
        "まあいい……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x10,
        (
            "ここはアーティストの楽屋だ。\x01",
            "入るのなら静かにしてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_588C")

    TalkEnd(0xFE)
    Return()

    # Function_23_54BE end

    def Function_24_5890(): pass

    label("Function_24_5890")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_59CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5924")

    #C0246
    ChrTalk(
        0x12,
        (
            "ニコル君、結局\x01",
            "戻ってこなかったわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x12,
        (
            "……残念だけど、劇団長の言うとおり\x01",
            "気持ちを切り替えていかないとダメね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59C8")

    label("loc_5924")


    #C0248
    ChrTalk(
        0x12,
        (
            "ようやく調整の入った\x01",
            "台本が組みあがったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x12,
        (
            "でも、あらあら……\x01",
            "ユージーン君たら大変そうねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x12,
        (
            "ともかくリーシャと\x01",
            "セリーヌにも知らせてこないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_59C8")

    Jump("loc_60FB")

    label("loc_59CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_5A92")
    OP_4B(0x9, 0xFF)

    #C0251
    ChrTalk(
        0x12,
        (
            "そういえばあの子、\x01",
            "記念祭の後に何日か\x01",
            "行方をくらましてたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x12,
        (
            "うーん、その間に\x01",
            "何かあったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        (
            "#1801Fそうですね……\x01",
            "何も仰ってくれませんけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_5A95")

    label("loc_5A92")

    Call(0, 18)

    label("loc_5A95")

    Jump("loc_60FB")

    label("loc_5A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5B13")

    #C0254
    ChrTalk(
        0x12,
        "ニコル君、自信が付いたみたいね。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x12,
        (
            "一時期落ち込んでいたみたいだから\x01",
            "お姉さん心配してたんだけれど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60FB")

    label("loc_5B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5B88")

    #C0256
    ChrTalk(
        0x12,
        (
            "イリアの豪胆さは\x01",
            "ある意味天性の物ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x12,
        (
            "うふ、あの子も新人の頃から\x01",
            "大物だったのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C13")

    label("loc_5B88")


    #C0258
    ChrTalk(
        0x12,
        (
            "イリアったら\x01",
            "こんな日に寝坊するなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x12,
        (
            "うふ、新人の頃から\x01",
            "変わっていないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x12,
        "警察の人、ちょっと怒っていたわよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5C13")

    Jump("loc_60FB")

    label("loc_5C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5C9C")

    #C0261
    ChrTalk(
        0x12,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x12,
        (
            "お稽古中は楽屋も\x01",
            "飲食禁止になってしまうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x12,
        (
            "うふ、おやつを食べるなら\x01",
            "今のうちなのよね～㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60FB")

    label("loc_5C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5E0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5D2B")

    #C0264
    ChrTalk(
        0x12,
        "劇団長はあれでやり手な人なのよ。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x12,
        (
            "もっとも、最近は\x01",
            "イリアのペースに巻き込まれて\x01",
            "苦労する事が多いみたいだけど㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E05")

    label("loc_5D2B")


    #C0266
    ChrTalk(
        0x12,
        (
            "劇団長って、あまり\x01",
            "ぱっとしない人でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x12,
        (
            "でもああ見えて\x01",
            "脚本と舞台監督を務める\x01",
            "劇作家#6Rドラマチスト#なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x12,
        (
            "うふ、アルカンシェルの人気は\x01",
            "すべてあの人から始まっているの。\x01",
            "あれでやり手な人なのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5E05")

    Jump("loc_60FB")

    label("loc_5E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 5)), scpexpr(EXPR_END)), "loc_5F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5E72")

    #C0269
    ChrTalk(
        0x12,
        (
            "最近はリーシャも\x01",
            "力を伸ばしているし……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x12,
        "うふ、来年の今ごろが楽しみね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F2E")

    label("loc_5E72")


    #C0271
    ChrTalk(
        0x12,
        (
            "うふ、スターは\x01",
            "イリアや私だけじゃないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x12,
        (
            "テオドールとユージーンも\x01",
            "女の子の人気を二分する\x01",
            "トップスターだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x12,
        (
            "あまりアルカンシェルの\x01",
            "アーティスト層を\x01",
            "甘く見ちゃダメよ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5F2E")

    Jump("loc_60FB")

    label("loc_5F33")


    #C0274
    ChrTalk(
        0x104,
        (
            "#0305Fあ……\x01",
            "プリエさんじゃないスか！\x02\x03",

            "#0309F《神秘の歌姫》プリエ……\x01",
            "幻想曲の大スター！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x12,
        "あらぁ、ファンの方？\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x12,
        (
            "ごめんなさいね、\x01",
            "色気のない練習着姿で。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#0300Fいえいえ～、\x01",
            "俺は全然構わないッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x12,
        "うふ、でも私の方が構っちゃうかも。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x12,
        (
            "そ・れ・と。\x01",
            "楽屋じゃお静かにね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        "#0300Fはいっ、すんません！\x02",
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
            "#0211F（ランディさんも\x01",
            "  分かりやすいですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 5)

    label("loc_60FB")

    TalkEnd(0xFE)
    Return()

    # Function_24_5890 end

    def Function_25_60FF(): pass

    label("Function_25_60FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_61F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_617B")

    #C0282
    ChrTalk(
        0x13,
        (
            "リーシャはしょっちゅう\x01",
            "自宅に忘れ物をしますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x13,
        (
            "もう、そういう所は\x01",
            "抜けてるんですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61EF")

    label("loc_617B")


    #C0284
    ChrTalk(
        0x13,
        (
            "リーシャったら、\x01",
            "また忘れ物をとりに\x01",
            "自宅に戻ってますのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x13,
        (
            "あの子、そういう所は\x01",
            "抜けてるんですから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_61EF")

    Jump("loc_6684")

    label("loc_61F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_633A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_628F")

    #C0286
    ChrTalk(
        0x13,
        (
            "ニコルの様子に気付いていながら\x01",
            "話を聞いてやる事もしませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x13,
        (
            "もしかしてわたくし……\x01",
            "酷い事をしたかもしれませんわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6335")

    label("loc_628F")


    #C0288
    ChrTalk(
        0x13,
        (
            "……ニコルは最近\x01",
            "様子がおかしかったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x13,
        (
            "わたくしも気付いていましたのに\x01",
            "見て見ぬふりをしていて……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x13,
        (
            "それでまさか\x01",
            "こんな事になってしまうなんて……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_6335")

    Jump("loc_6684")

    label("loc_633A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_64A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_63D2")

    #C0291
    ChrTalk(
        0x13,
        (
            "イリアさんに認めてもらうのが\x01",
            "私の夢なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x13,
        (
            "リーシャには\x01",
            "先を越されてしまったけれど\x01",
            "いつまでも負けていられませんわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64A4")

    label("loc_63D2")


    #C0293
    ChrTalk(
        0x13,
        (
            "私、イリアさんに憧れて\x01",
            "アルカンシェルの\x01",
            "オーディションを受けたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x13,
        (
            "今回はリーシャに\x01",
            "出し抜けれてしまったけれど\x01",
            "いつまでも負けてはいられませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x13,
        (
            "練習を積んで\x01",
            "追い抜き返してやりませんと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_64A4")

    Jump("loc_6684")

    label("loc_64A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6547")

    #C0296
    ChrTalk(
        0x13,
        (
            "リーシャの抜擢は異例中の異例。\x01",
            "それだけ才能があるという事ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x13,
        (
            "ならば、絶対に舞台を成功させる事。\x01",
            "……でないと私が許しませんわよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6684")

    label("loc_6547")


    #C0298
    ChrTalk(
        0x13,
        (
            "リーシャはまだ\x01",
            "アルカンシェルに入ったばかりの\x01",
            "新人ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x13,
        (
            "それが突然準主役への抜擢なんて\x01",
            "異例中の異例なんですのよ。\x02",
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
            "まあ、あの子なりに\x01",
            "稽古に打ち込んだ結果ですし、\x01",
            "何も言うつもりはありませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x13,
        (
            "先輩の私を出し抜いての抜擢ですもの。\x01",
            "無様な真似をしたら許しませんわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_6684")

    TalkEnd(0xFE)
    Return()

    # Function_25_60FF end

    def Function_26_6688(): pass

    label("Function_26_6688")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_671C")
    Jump("loc_6766")

    label("loc_671C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_673C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6766")

    label("loc_673C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_675C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6766")

    label("loc_675C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6766")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6809")

    #C0302
    ChrTalk(
        0x17,
        (
            "リーシャは時々\x01",
            "一人で自信の無さそうな\x01",
            "顔をしていますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        (
            "まったく……\x01",
            "何だか歯がゆいですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A8D")

    label("loc_6809")


    #C0304
    ChrTalk(
        0x17,
        (
            "リーシャは時々\x01",
            "一人で自信の無さそうな\x01",
            "顔をしていますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x17,
        (
            "まったく……\x01",
            "貴女はあのイリアさんが認めた\x01",
            "一流のアーティストですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x17,
        (
            "そんなしょんぼりした\x01",
            "顔でどうしますの！\x01",
            "もっと自信をお持ちなさいな！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692B")

    #C0307
    ChrTalk(
        0x101,
        (
            "#0006Fあの、そういう事は\x01",
            "本人に言った方がいいんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A17")

    label("loc_692B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6984")

    #C0308
    ChrTalk(
        0x102,
        (
            "#0106Fあの、そういう事は\x01",
            "本人に仰った方が\x01",
            "いいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A17")

    label("loc_6984")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D2")

    #C0309
    ChrTalk(
        0x103,
        (
            "#0206F……そういった事は\x01",
            "本人に言った方がいいのでは？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A17")

    label("loc_69D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A17")

    #C0310
    ChrTalk(
        0x104,
        (
            "#0306Fいや、そういう事は\x01",
            "本人に直接言うべきだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A17")

    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0311
    ChrTalk(
        0x17,
        "そ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_64(0x17)

    #C0312
    ChrTalk(
        0x17,
        (
            "こほん、私は厳しい先輩なのです。\x01",
            "こんな事言えるはずありませんわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_6A8D")

    Jump("loc_6BDB")

    label("loc_6A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6AFC")

    #C0313
    ChrTalk(
        0x17,
        (
            "警察の方が来て\x01",
            "お稽古も出来ませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x17,
        "ふう、気が滅入ってしまいますわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B4E")

    label("loc_6AFC")


    #C0315
    ChrTalk(
        0x17,
        (
            "例の脅迫文、\x01",
            "本当かもしれないそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x17,
        "なんだか少し不安ですわ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_6B4E")

    Jump("loc_6BDB")

    label("loc_6B53")


    #C0317
    ChrTalk(
        0x17,
        (
            "今度の新作公演、お父様とお母様が\x01",
            "観にいらっしゃるそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x17,
        (
            "……私も無様な真似はできませんわ。\x01",
            "もっと技術を磨きませんと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BDB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_6688 end

    def Function_27_6BE3(): pass

    label("Function_27_6BE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6C5A")

    #C0319
    ChrTalk(
        0x11,
        "みんな俺の演技をみて驚いていたな。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x11,
        (
            "ハハハ、いい気分だよ。\x01",
            "ざまぁ見ろって感じだな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CC3")

    label("loc_6C5A")


    #C0321
    ChrTalk(
        0x11,
        (
            "ハハハ……！\x01",
            "今日のリハーサルも完璧だよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "まさに絶好調……\x01",
            "リーシャにも負ける気がしないね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6CC3")

    Jump("loc_6F39")

    label("loc_6CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6D92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6D44")

    #C0323
    ChrTalk(
        0x11,
        "もう俺に失敗の文字は無いのさ。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x11,
        (
            "練習量でも誰にも負けない自信がある。\x01",
            "さあ、やりましょうよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8D")

    label("loc_6D44")


    #C0325
    ChrTalk(
        0x11,
        (
            "……さあ、今日も\x01",
            "公演頑張りましょうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x11,
        "#4Sハハハハハ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6D8D")

    Jump("loc_6F39")

    label("loc_6D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6EC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6E22")

    #C0327
    ChrTalk(
        0x11,
        (
            "プリエさんはアルカンシェルで\x01",
            "ずっとスターを張ってる\x01",
            "大ベテランなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x11,
        (
            "声を掛けてもらうと\x01",
            "なんだか楽になるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EC1")

    label("loc_6E22")


    #C0329
    ChrTalk(
        0x11,
        (
            "プリエさんに\x01",
            "励ましてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x11,
        "あまり気負う事はないってさ。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x11,
        (
            "ふう……何だか\x01",
            "少し気分が楽になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x11,
        "やっぱり先輩の言葉は凄いよね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6EC1")

    Jump("loc_6F39")

    label("loc_6EC6")


    #C0333
    ChrTalk(
        0xFE,
        "はあ、今日の稽古も散々だったよ。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        "せっかく役を貰えたってのに……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "やっぱり僕は\x01",
            "才能が無いのかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F39")

    TalkEnd(0xFE)
    Return()

    # Function_27_6BE3 end

    def Function_28_6F3D(): pass

    label("Function_28_6F3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6FBA")
    OP_4B(0x12, 0xFF)

    #C0336
    ChrTalk(
        0xA,
        (
            "これは手早く着替えて\x01",
            "もらわないといけませんね……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xA,
        "衣装出しの順も工夫しませんと。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_7063")

    label("loc_6FBA")

    OP_4B(0x12, 0xFF)

    #C0338
    ChrTalk(
        0xA,
        "あら、私にも見せていただけますか？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xA,
        (
            "ふむふむ……衣装出しの順も\x01",
            "調整が入っていますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xA,
        (
            "時間もギリギリですし\x01",
            "これは手早く着替えてもらわないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x12, 0xFF)

    label("loc_7063")

    Jump("loc_7C9E")

    label("loc_7068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_71AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7102")

    #C0341
    ChrTalk(
        0xA,
        (
            "ニコル君がおかしな事になって\x01",
            "みんな不安に思っているみたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xA,
        (
            "無理もないわね……\x01",
            "元々強いストレスを抱える\x01",
            "職種だもの……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A8")

    label("loc_7102")

    OP_4B(0x10, 0xFF)

    #C0343
    ChrTalk(
        0x10,
        (
            "カレリアさん、\x01",
            "ユージーンは俺が引き受けます。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x10,
        "セリーヌが不安がらないよう、頼む。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xA,
        (
            "ええ、分かったわ。\x01",
            "しばらく傍に付いている事にします。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x10, 0xFF)

    label("loc_71A8")

    Jump("loc_7C9E")

    label("loc_71AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7233")

    #C0346
    ChrTalk(
        0xA,
        (
            "（ニコルさん……最近態度が\x01",
            "  随分と変わったようですけれど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xA,
        (
            "（自信が付くと\x01",
            "  あんな物なのでしょうか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9E")

    label("loc_7233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_72E4")
    SetChrSubChip(0x15, 0x2)

    #C0348
    ChrTalk(
        0xA,
        (
            "まったくもう……\x01",
            "今からでは上演時間に\x01",
            "遅れてしまいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x15,
        (
            "#6104F平気平気、まだ１０分あるし。\x02\x03",

            "#6102Fちゃちゃっと\x01",
            "やっちゃってよ、カレリアさん！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Jump("loc_7C9E")

    label("loc_72E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_742F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_736D")

    #C0350
    ChrTalk(
        0xA,
        (
            "ニコルさんは昨日の公演で\x01",
            "大コケしてしまったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xA,
        (
            "……あの様子では\x01",
            "落ち込んでいるのではないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742A")

    label("loc_736D")


    #C0352
    ChrTalk(
        0xA,
        (
            "ニコルさん、昨日の公演で\x01",
            "大コケしてしまったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xA,
        (
            "その後もパニックになって\x01",
            "セリフを忘れてしまいますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xA,
        (
            "……あの様子では\x01",
            "落ち込んでいるのではないかしら。\x01",
            "心配ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_742A")

    Jump("loc_7C9E")

    label("loc_742F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_753E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7451")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_74B0")

    #C0355
    ChrTalk(
        0xA,
        (
            "舞台もそろそろ\x01",
            "クライマックスですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        "ささ、掃除を済ませておかないと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7539")

    label("loc_74B0")


    #C0357
    ChrTalk(
        0xA,
        (
            "先ほど衣装部屋の方から\x01",
            "ゴト、と物音がした気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xA,
        "まあ気のせいでしょうね。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xA,
        (
            "私もついつい\x01",
            "神経過敏になっているようです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_7539")

    Jump("loc_7C9E")

    label("loc_753E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_75C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7560")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7560")


    #C0360
    ChrTalk(
        0xA,
        (
            "あら、またこんな所に\x01",
            "お菓子を隠して……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xA,
        (
            "プリエさんの癖も\x01",
            "本当に治らないですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9E")

    label("loc_75C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_76D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75E3")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_765F")

    #C0362
    ChrTalk(
        0xA,
        (
            "ここから先は真剣勝負……\x01",
            "私には祈ることしかできません。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xA,
        (
            "せめて、部屋の掃除でも\x01",
            "しておきましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76D4")

    label("loc_765F")


    #C0364
    ChrTalk(
        0xA,
        (
            "アーティストたちは\x01",
            "全員舞台裏に入ってしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xA,
        (
            "ここから先は真剣勝負……\x01",
            "私も成功を祈っていますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_76D4")

    Jump("loc_7C9E")

    label("loc_76D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_77E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_773D")

    #C0366
    ChrTalk(
        0xA,
        (
            "ふふ、新作のお披露目まであと少し。\x01",
            "私もあの子たちを支えていきませんと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77DD")

    label("loc_773D")


    #C0367
    ChrTalk(
        0xA,
        (
            "ここのアーティストたちは\x01",
            "個性が強くて大変です。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xA,
        (
            "それでも、みんな\x01",
            "舞台に向かって真っ直ぐなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xA,
        (
            "そんな子達を支えるのも\x01",
            "悪くない仕事ですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_77DD")

    Jump("loc_7C9E")

    label("loc_77E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_783D")

    #C0370
    ChrTalk(
        0xA,
        (
            "トップスターがこんな\x01",
            "だらしない姿でどうするんですか、\x01",
            "もう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_795C")

    label("loc_783D")

    OP_4B(0x8, 0xFF)

    #C0371
    ChrTalk(
        0xA,
        (
            "はあ、イリアさんたら……\x01",
            "たまに平気な顔で遅刻して。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xA,
        (
            "がさつな所は\x01",
            "昔から少しも治りませんね！\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#1703Fそうなのよね～……\x02\x03",

            "#1700F……あ、カレリアさん。\x01",
            "ちゃちゃっと稽古に入るから\x01",
            "着付け手伝ってもらえます？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xA,
        (
            "またその調子で……\x01",
            "劇団長の日常の\x01",
            "苦労が忍ばれますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x8, 0xFF)

    label("loc_795C")

    Jump("loc_7C9E")

    label("loc_7961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_79BC")

    #C0375
    ChrTalk(
        0xA,
        (
            "プリエさんたら本当に……\x01",
            "舞台の上とは\x01",
            "えらい違いなんですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A3E")

    label("loc_79BC")

    OP_4B(0x12, 0xFF)

    #C0376
    ChrTalk(
        0xA,
        (
            "プリエさん、着替えた後の\x01",
            "飲食は控えてくださいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xA,
        (
            "仕立てたデザイナーとして\x01",
            "それだけは見過ごせませんわ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x12, 0xFF)

    label("loc_7A3E")

    Jump("loc_7C9E")

    label("loc_7A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7AB2")

    #C0378
    ChrTalk(
        0xA,
        (
            "ほらほら、男性方は\x01",
            "退散してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xA,
        (
            "リーシャはこれから\x01",
            "お着替えなのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B80")

    label("loc_7AB2")

    OP_4B(0x9, 0xFF)

    #C0380
    ChrTalk(
        0xA,
        (
            "ほらほらリーシャ、\x01",
            "早く着替えてしまいなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xA,
        (
            "衣装のほつれは\x01",
            "直しておきましたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x9,
        (
            "#1805Fあっ、本当だ……\x01",
            "綺麗に直ってます。\x02\x03",

            "#1800Fありがとうございます、\x01",
            "カレリアさん！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x9, 0xFF)

    label("loc_7B80")

    Jump("loc_7C9E")

    label("loc_7B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7C16")

    #C0383
    ChrTalk(
        0xA,
        (
            "この時期は劇団中が\x01",
            "大忙しなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xA,
        (
            "衣装デザインの微調整に\x01",
            "アーティストたちの体調管理……\x01",
            "裏方も山ほど仕事がありますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9E")

    label("loc_7C16")


    #C0385
    ChrTalk(
        0xA,
        (
            "新作の仕上げも\x01",
            "いよいよ大詰めですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xA,
        (
            "衣装デザインの微調整に\x01",
            "アーティストたちの体調管理……\x01",
            "裏方も山ほど仕事がありますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_7C9E")

    TalkEnd(0xFE)
    Return()

    # Function_28_6F3D end

    def Function_29_7CA2(): pass

    label("Function_29_7CA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7D07")

    #C0387
    ChrTalk(
        0xE,
        (
            "そろそろ夜の\x01",
            "公演が始まるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "ふふ、本日も\x01",
            "お客様で賑わいそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D78")

    label("loc_7D07")


    #C0389
    ChrTalk(
        0xE,
        (
            "おや、申し訳ありません。\x01",
            "そろそろ公演時間ですので。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        (
            "舞台裏への立ち入りは\x01",
            "ご遠慮願えますでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_7D78")

    TalkEnd(0xFE)
    Return()

    # Function_29_7CA2 end

    def Function_30_7D7C(): pass

    label("Function_30_7D7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_7E91")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E41")

    #C0391
    ChrTalk(
        0x101,
        (
            "#0005Fあれ……？\x01",
            "劇団にこんな子、いたっけな。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        "……何だお前ら、客じゃないな？\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "フン……劇団は\x01",
            "一般人立ち入り禁止だぜ。\x01",
            "チケットないなら帰れよな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Jump("loc_7E8C")

    label("loc_7E41")


    #C0394
    ChrTalk(
        0xFE,
        "……チケットないと観れないぞ。\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "オレがしっかり\x01",
            "見張ってるからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E8C")

    Jump("loc_803C")

    label("loc_7E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_803C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EB4")
    Call(0, 31)
    Jump("loc_803C")

    label("loc_7EB4")


    #C0396
    ChrTalk(
        0xFE,
        (
            "……掃除してるんだ。\x01",
            "文句あるかよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8039")

    #C0397
    ChrTalk(
        0x101,
        (
            "#0012Fハハ……\x01",
            "相変わらず反抗的だな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F52")

    #C0398
    ChrTalk(
        0x102,
        "#0100Fでも慣れてきたみたいね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FC5")

    label("loc_7F52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F8F")

    #C0399
    ChrTalk(
        0x103,
        "#0200Fでも慣れてきたみたいですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FC5")

    label("loc_7F8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FC5")

    #C0400
    ChrTalk(
        0x104,
        "#0300Fだが慣れてきたみたいだな？\x02",
    )

    CloseMessageWindow()

    label("loc_7FC5")


    #C0401
    ChrTalk(
        0xFE,
        (
            "フ、フン……\x01",
            "この位の仕事、誰にだってできる。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x153,
        (
            "#1111F（きれーな銀色のカミー。\x01",
            "  ロイド達のシリアイかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8039")

    SetScenarioFlags(0x1, 3)

    label("loc_803C")

    TalkEnd(0xFE)
    Return()

    # Function_30_7D7C end

    def Function_31_8040(): pass

    label("Function_31_8040")


    #C0403
    ChrTalk(
        0x101,
        (
            "#0005Fあれ……？\x01",
            "劇団にこんな子、いたっけな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80B3")

    #C0404
    ChrTalk(
        0xFE,
        (
            "……何だお前、\x01",
            "イリアさんの知り合いか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80E2")

    label("loc_80B3")


    #C0405
    ChrTalk(
        0xFE,
        (
            "……何だお前ら、\x01",
            "イリアさんの知り合いか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80E2")


    #C0406
    ChrTalk(
        0xFE,
        (
            "フン……\x01",
            "劇団は一般人立ち入り禁止だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "いくら知り合いだからって\x01",
            "図々しく上がってくんなよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_31_8040 end

    def Function_32_814C(): pass

    label("Function_32_814C")

    TalkBegin(0xFE)

    #C0408
    ChrTalk(
        0xFE,
        (
            "思い切ってＳ席のチケットを\x01",
            "買っちゃったよ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "ドキドキ……\x01",
            "でもプロポーズなら\x01",
            "このくらいは奮発しないとな！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_814C end

    def Function_33_81CA(): pass

    label("Function_33_81CA")

    TalkBegin(0xFE)

    #C0410
    ChrTalk(
        0xFE,
        (
            "彼がチケットを\x01",
            "手に入れてくれたのよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        "……それもＳ席よ！\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "うふ、思ったより\x01",
            "大胆なトコあるんだから。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_81CA end

    def Function_34_8245(): pass

    label("Function_34_8245")

    TalkBegin(0xFE)

    #C0413
    ChrTalk(
        0xFE,
        (
            "お母さん、急がんと\x01",
            "公演が始まっちゃうわよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "イリア様を見逃したら\x01",
            "お母さんを恨んじゃうんだから！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_8245 end

    def Function_35_82B6(): pass

    label("Function_35_82B6")

    TalkBegin(0xFE)

    #C0415
    ChrTalk(
        0xFE,
        (
            "Ｂ席の２の２８だから……\x01",
            "左側の席よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "よしっ、行きましょ。\x01",
            "いよいよアルカンシェルの舞台を\x01",
            "拝むわよ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_82B6 end

    def Function_36_832E(): pass

    label("Function_36_832E")

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

    def lambda_8442():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8442)

    def lambda_845C():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_845C)
    Sleep(50)

    def lambda_8470():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8470)

    def lambda_848A():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_848A)
    Sleep(50)

    def lambda_849E():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_849E)

    def lambda_84B8():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_84B8)
    Sleep(50)

    def lambda_84CC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_84CC)

    def lambda_84E6():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_84E6)
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
        "#0005F#11Pん……？\x02",
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
        "金髪の女性",
        (
            "#1706F#11Pもう、リーシャったら。\x01",
            "あたしは全然構わないわよ？\x02\x03",

            "#1702F好きなだけ\x01",
            "泊まっていけばいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#1805F#11Pい、いえいえっ、そんな……\x02\x03",

            "#1809F私の方なら大丈夫です。\x01",
            "適当な安いアパルトメントを\x01",
            "探してみますから。\x02\x03",

            "#1802Fえっと、市役所の窓口で\x01",
            "聞いてみればいいんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #N0420
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1702F#5Pええ、多分それが\x01",
            "一番手っ取り早いわね。\x02\x03",

            "#1709F転入届もついでに出せるし㈱\x02",
        )
    )

    CloseMessageWindow()

    #N0421
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#1809F#11Pあはは……そうですね。\x02\x03",

            "#1810Fすみません、練習を\x01",
            "切り上げてしまった上に\x01",
            "色々と教えて頂いて……\x02",
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
            "#0307F#11Pおい、あれって……\x01",
            "イリア・プラティエじゃねえか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0005F#11Pイリア・プラティエ？\x02\x03",

            "#0002Fへえ、雑誌の記事で\x01",
            "何度か見たことがあるけど……\x02",
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
        "おや、あなた方は……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_8943():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8943)
    Sleep(15)

    def lambda_8953():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8953)

    def lambda_8960():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8960)
    Sleep(12)

    def lambda_8970():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8970)
    OP_68(-120, 1450, -3060, 3000)
    MoveCamera(39, 26, 0, 3000)
    SetCameraDistance(12260, 3000)
    BeginChrThread(0xB, 1, 0, 38)
    Sleep(1000)

    def lambda_89AB():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89AB)
    Sleep(180)

    def lambda_89BB():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89BB)
    Sleep(240)

    def lambda_89CB():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_89CB)
    Sleep(250)

    def lambda_89DB():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89DB)
    OP_6F(0x79)
    WaitChrThread(0xB, 1)

    #C0425
    ChrTalk(
        0xB,
        (
            "#5P申し訳ありません、\x01",
            "劇団アルカンシェルの公演は\x01",
            "夕方６時からですので……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xB,
        (
            "#5Pファンの方でしたら\x01",
            "立ち入りはどうかご容赦を。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x101,
        (
            "#0006F#12Pす、すみません。\x01",
            "勝手に入り込んでしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        "#0102F#12P失礼しました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 3)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_832E end

    def Function_37_8AE1(): pass

    label("Function_37_8AE1")


    def lambda_8AE6():
        OP_97(0x8, 0xFFFFD6FC, 0x0, 0xFFFFFE70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8AE6)

    def lambda_8B00():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8B00)
    Sleep(50)

    def lambda_8B14():
        OP_97(0x9, 0xFFFFD6FC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8B14)

    def lambda_8B2E():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8B2E)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x9, 750)
    Return()

    # Function_37_8AE1 end

    def Function_38_8B46(): pass

    label("Function_38_8B46")

    OP_95(0xFE, -180, 0, -1760, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_38_8B46 end

    def Function_39_8B62(): pass

    label("Function_39_8B62")

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

    def lambda_8C26():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C26)

    def lambda_8C40():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C40)
    Sleep(50)

    def lambda_8C54():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8C54)

    def lambda_8C6E():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8C6E)
    Sleep(50)

    def lambda_8C82():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8C82)

    def lambda_8C9C():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8C9C)
    Sleep(50)

    def lambda_8CB0():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CB0)

    def lambda_8CCA():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8CCA)
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

    def lambda_8D5C():

        label("loc_8D5C")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_8D5C")

    QueueWorkItem2(0x0, 1, lambda_8D5C)

    def lambda_8D6E():

        label("loc_8D6E")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_8D6E")

    QueueWorkItem2(0x1, 1, lambda_8D6E)

    def lambda_8D80():

        label("loc_8D80")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_8D80")

    QueueWorkItem2(0x2, 1, lambda_8D80)

    def lambda_8D92():

        label("loc_8D92")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_8D92")

    QueueWorkItem2(0x3, 1, lambda_8D92)
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
            "申し訳ありません、\x01",
            "劇団アルカンシェルの公演は\x01",
            "夕方６時からですので……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xB,
        (
            "ファンの方でしたら\x01",
            "立ち入りはどうかご容赦を。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0006F#2Pす、すみません。\x01",
            "勝手に入り込んでしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#0100F#2P（劇団アルカンシェル……\x01",
            "  有名な劇場だし、用もなく\x01",
            "  お邪魔しない方が良さそうね。）\x02",
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

    # Function_39_8B62 end

    def Function_40_8F03(): pass

    label("Function_40_8F03")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FB5")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -30, 0, -5290, 0)

    label("loc_8FB5")

    SetChrPos(0xB, -40, 0, -1140, 180)
    SetChrPos(0x14, 4670, 0, 3090, 90)
    BeginChrThread(0x14, 0, 0, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0433
    ChrTalk(
        0xB,
        (
            "これは皆様、ようこそ\x01",
            "お越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xB,
        (
            "ですが、申し訳ありません。\x01",
            "ただ今イリアさんやリーシャさんは……\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        (
            "#0000F#2Pすみません、\x01",
            "皆さん出演中なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x104,
        (
            "#0300F#2Pまあ用事があったわけじゃねえし、\x01",
            "また別の機会に訪ねてみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        "#0100F#2Pええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x103,
        "#0200F#2Pどうもお邪魔しました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xC8, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9147")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_9147")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_8F03 end

    def Function_41_9154(): pass

    label("Function_41_9154")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9210")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -30, 0, -5290, 0)

    label("loc_9210")

    SetChrPos(0xB, -40, 0, -1140, 180)
    SetChrPos(0x14, 4670, 0, 3090, 90)
    BeginChrThread(0x14, 0, 0, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0439
    ChrTalk(
        0xB,
        (
            "これは皆様、ようこそ\x01",
            "お越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xB,
        (
            "ですが、申し訳ありません。\x01",
            "ただ今イリアさんやリーシャさんは……\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        (
            "#0000F#2Pすみません、\x01",
            "皆さん出演中なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x104,
        (
            "#0300F#2Pまあ用事があったわけじゃねえし、\x01",
            "また別の機会に訪ねてみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x102,
        "#0100F#2Pええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        "#0200F#2Pどうもお邪魔しました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xC8, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93A2")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_93A2")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_9154 end

    def Function_42_93AF(): pass

    label("Function_42_93AF")

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
            "支援課の皆様……\x01",
            "よくお越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        (
            "#0005Fバルサモさん、公演の方は\x01",
            "どうなりましたか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xB,
        (
            "ええ、何とか舞台の都合も付き、\x01",
            "遅まきの昼公演を上演している所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xB,
        (
            "リハーサル無しですので\x01",
            "不安もありましたが……\x01",
            "何とか乗り切れそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#0100Fよかった……\x01",
            "公演に穴は空けずに\x01",
            "済んだみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x103,
        "#0200Fさすが超一流のメンバーかと。\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x104,
        (
            "#0301Fま、行方不明の連中は\x01",
            "まだ手がかりすら見つかってねえ。\x02\x03",

            "#0303Fここは一つ\x01",
            "頑張ってもらうしかねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xB,
        (
            "皆様、申し訳ありません。\x01",
            "ニコルさんの事は\x01",
            "よろしくお願い致します。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        (
            "#0000Fええ、お任せ下さい。\x01",
            "必ず見つけ出してみせます。\x02",
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

    # Function_42_93AF end

    def Function_43_96C6(): pass

    label("Function_43_96C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9741")
    TalkBegin(0xFF)

    #C0454
    ChrTalk(
        0x101,
        (
            "#0000F観客も大分\x01",
            "入ってきてるみたいだな……\x02\x03",

            "邪魔になりそうだし\x01",
            "正面ホールには入らないでおこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_9741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_97EE")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_979F")

    #C0455
    ChrTalk(
        0x101,
        (
            "#0001F舞台を覗いてる場合じゃない……\x01",
            "右側の階段に急ごう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97E6")

    label("loc_979F")


    #C0456
    ChrTalk(
        0x102,
        (
            "#0101F舞台を覗いてる場合じゃないわね……\x01",
            "右側の階段に急がないと！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97E6")

    TalkEnd(0xFF)
    Jump("loc_98AD")

    label("loc_97EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98AD")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "中の様子をうかがう\x01",      # 0
            "止めておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9856"),
        (1, "loc_98A6"),
        (SWITCH_DEFAULT, "loc_98AB"),
    )


    label("loc_9856")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_987B")
    SetScenarioFlags(0x5C, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_98A1")

    label("loc_987B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_9895")
    SetScenarioFlags(0x5C, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_98A1")

    label("loc_9895")

    SetScenarioFlags(0x5C, 3)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_98A1")

    Jump("loc_98AB")

    label("loc_98A6")

    Jump("loc_98AB")

    label("loc_98AB")

    EventEnd(0x3)

    label("loc_98AD")

    Return()

    # Function_43_96C6 end

    def Function_44_98AE(): pass

    label("Function_44_98AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9973")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "中の様子をうかがう\x01",      # 0
            "止めておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9916"),
        (1, "loc_996C"),
        (SWITCH_DEFAULT, "loc_9971"),
    )


    label("loc_9916")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x86, 3)
    ClearScenarioFlags(0x86, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_9941")
    SetScenarioFlags(0x5D, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_9967")

    label("loc_9941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_995B")
    SetScenarioFlags(0x5C, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_9967")

    label("loc_995B")

    SetScenarioFlags(0x5C, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_9967")

    Jump("loc_9971")

    label("loc_996C")

    Jump("loc_9971")

    label("loc_9971")

    EventEnd(0x3)

    label("loc_9973")

    Return()

    # Function_44_98AE end

    def Function_45_9974(): pass

    label("Function_45_9974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A39")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "中の様子をうかがう\x01",      # 0
            "止めておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_99DC"),
        (1, "loc_9A32"),
        (SWITCH_DEFAULT, "loc_9A37"),
    )


    label("loc_99DC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x86, 2)
    ClearScenarioFlags(0x86, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_9A07")
    SetScenarioFlags(0x5D, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_9A2D")

    label("loc_9A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_9A21")
    SetScenarioFlags(0x5C, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_9A2D")

    label("loc_9A21")

    SetScenarioFlags(0x5C, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_9A2D")

    Jump("loc_9A37")

    label("loc_9A32")

    Jump("loc_9A37")

    label("loc_9A37")

    EventEnd(0x3)

    label("loc_9A39")

    Return()

    # Function_45_9974 end

    def Function_46_9A3A(): pass

    label("Function_46_9A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AF9")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "中の様子をうかがう\x01",      # 0
            "止めておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9AA2"),
        (1, "loc_9AF2"),
        (SWITCH_DEFAULT, "loc_9AF7"),
    )


    label("loc_9AA2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_9AC7")
    SetScenarioFlags(0x5D, 3)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_9AED")

    label("loc_9AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_9AE1")
    SetScenarioFlags(0x5D, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_9AED")

    label("loc_9AE1")

    SetScenarioFlags(0x5D, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_9AED")

    Jump("loc_9AF7")

    label("loc_9AF2")

    Jump("loc_9AF7")

    label("loc_9AF7")

    EventEnd(0x3)

    label("loc_9AF9")

    Return()

    # Function_46_9A3A end

    def Function_47_9AFA(): pass

    label("Function_47_9AFA")

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
        "#1702Fゴメンゴメン、待たせたわね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女性の声")

    #A0458
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ううん、気にしないで。\x02\x03",

            "大方、お気に入りの新人の稽古に\x01",
            "遅くまで付き合っていたんでしょう？\x02\x03",

            "ついでにイチャついて、劇団長さんに\x01",
            "呆れられていたんじゃないかしら？\x02",
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
            "#1709F……ま、まさか～。\x01",
            "そんな事あるわけないじゃない～。\x02\x03",

            "#1702Fそ、それよりセシル、どうしたの？\x02\x03",

            "こんな遅くに珍しいわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0460
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、うん……\x02\x03",

            "貴女が贈ってくれたチケットが\x01",
            "今日、ちょうど届いてて……\x02\x03",

            "それでお礼を言おうと思って。\x02",
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
            "#1700Fああ、そうだったの。\x02\x03",

            "#1704Fま、お互い忙しいとは思うけど\x01",
            "できれば絶対見に来てよね？\x02\x03",

            "#1702F記念祭の初日だし、\x01",
            "さすがに休みは取れるでしょ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0462
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふっ、何とかね。\x02\x03",

            "でも、何だか申し訳ないわね。\x02\x03",

            "本公演の初日……\x01",
            "それもＳ席を２枚もなんて。\x02",
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
            "#1709Fま、一応は\x01",
            "看板女優の特権ってことで。\x02\x03",

            "#1702Fセシルが見に来てくれた方が\x01",
            "あたしも気合いが入るからね～。\x02\x03",

            "親友の前で、あんまり\x01",
            "みっともない真似は出来ないし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0464
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふ……\x01",
            "相変わらず逆境に強いわね。\x02\x03",

            "というか、逆境になればなるほど\x01",
            "燃えてくるタイプなのよねぇ。\x02",
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
            "#1704Fフフン、否定はしないわ。\x02\x03",

            "#1700Fま、せいぜい上玉の男でも\x01",
            "お飾りに連れて来なさいな。\x02\x03",

            "職場が職場なんだし、\x01",
            "将来有望な男も多いでしょ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0466
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……ふふ、そうね………\x02",
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
            "#1705Fあっ………\x02\x03",

            "#1706F………ゴメン…………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0468
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふっ、気にしてないわ。\x02\x03",

            "さすがにもう\x01",
            "いいかげん吹っ切れてるから。\x02",
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
            "#1700F……そっか………\x02",
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
            "#1702Fそうだ！\x01",
            "なら例の弟君を誘いなさいよ？\x02\x03",

            "確かクロスベルに\x01",
            "戻ってきてるんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0471
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、ロイドのこと？\x02\x03",

            "うーん、大丈夫かしら？\x01",
            "忙しいとは思うんだけど……\x02\x03",

            "……でも、あの子たぶん、\x01",
            "イリアの舞台は初めてだろうし、\x01",
            "丁度いい機会かもしれないわね。\x02",
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
            "#1709Fうんうん、そうしなさい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、ゴメン……\x01",
            "そろそろ夜勤の時間だわ。\x02\x03",

            "チケットありがとう。\x01",
            "すごく楽しみにしてるから。\x02\x03",

            "稽古の仕上げ、頑張ってね。\x02",
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
            "#1702Fええ、セシルも頑張って。\x02",
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
            "#1701F（……３年、か。）\x02\x03",

            "#1706F（哀しみが薄れるには……\x01",
            "  まだ早いかもしれないわね。）\x02",
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

    # Function_47_9AFA end

    def Function_48_A564(): pass

    label("Function_48_A564")

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
        "#11P#0205Fわぁ……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        (
            "#0109Fふふ……\x01",
            "相変わらず雰囲気のある玄関ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#6P#0000F音楽が流れてる……\x01",
            "ってことは稽古中なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x104,
        "#0309Fおお、きっとそうに違いねぇ！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    TurnDirection(0xB, 0x101, 500)

    #N0480
    NpcTalk(
        0xB,
        "男性の声",
        "#6P──お客様。\x02",
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

    def lambda_A7AD():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A7AD)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xB4, 0x1F4)

    #C0481
    ChrTalk(
        0xB,
        "#5P大変申しわけありません。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xB,
        (
            "#5Pただいま当劇場は、\x01",
            "関係者以外の立入りを\x01",
            "ご遠慮願っておりまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#6P#0003Fえっと、その……\x02\x03",

            "#0000F実はこちらの方から相談を受けた\x01",
            "警察の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0484
    ChrTalk(
        0xB,
        "#5Pああ、特務支援課の方々でしたか。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xB,
        (
            "#5Pようこそ《アルカンシェル》へ。\x01",
            "リーシャさんから話は伺っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xB,
        (
            "#5P何でも劇団長とイリアさんに\x01",
            "お話を伺いにいらっしゃったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#6P#0000Fええ、お取次ぎ願えますか？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xB,
        (
            "#5Pそれでしたら、正面の扉から\x01",
            "ホール内にお入りください。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xB,
        (
            "#5Pちょうどイリアさんの稽古を\x01",
            "劇団長とリーシャさんが\x01",
            "見学しているはずですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x102,
        (
            "#0101Fいいんですか？\x01",
            "イリアさんの迷惑なのでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xB,
        (
            "#5Pいえいえ、そんな些事を\x01",
            "気にされる人ではありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xB,
        (
            "#5Pむしろ本番に近いといって\x01",
            "喜ばれるんじゃないでしょうか。\x02",
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
        "#6P#0002Fわ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        (
            "#0309Fよし、そんじゃあ俺たちも\x01",
            "早速見学させてもらおうぜ！\x02",
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

    # Function_48_A564 end

    def Function_49_ABF4(): pass

    label("Function_49_ABF4")

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
            "#1806F#1Pまったくイリアさんったら……\x02\x03",

            "#1801Fいきなり抱きついたりして、\x01",
            "ロイドさんに失礼じゃないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x8,
        (
            "#1709F#5Pまあまあ、固いこと言いっこなし。\x02\x03",

            "#1702Fそれにお姉さんに抱き付かれて\x01",
            "ちょっとは嬉しかったでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x101,
        "#0012F#12Pはは……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x103,
        "#0211F#12P………………（ジー）\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#0111F#6P（セシルさんに続いて……）\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#0310F#12P（これがヒエラルキー……\x01",
            "  弟至上主義というやつか！）\x02\x03",

            "（この弟貴族っ！\x01",
            "  弟ブルジョアジーがっ！）\x02",
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
            "#0006F#12Pそ、それでその……\x01",
            "脅迫状の件なんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x8,
        (
            "#1705F#5Pああ、そうだったわね。\x02\x03",

            "#1704F弟君の頼みなら仕方ない。\x01",
            "ちゃんと手紙は持ってきたわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_96(0x8, 0xFFFEA0CA, 0x0, 0xD34, 0x7D0, 0x0)

    #C0504
    ChrTalk(
        0x8,
        "#1700F#5Pはい、これ。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#0002F#12Pど、どうも。\x01",
            "（頼まれたのはこっちだけど……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B000():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B000)

    def lambda_B00D():
        OP_96(0xFE, 0xFFFEA03E, 0x0, 0x10FE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_B00D)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0506
    ChrTalk(
        0x101,
        "#0005F#12Pえっと……\x02",
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
            "新作ノ公演ヲ中止セヨ。\x01",
            "サモナクバ炎ノ舞姫ニ\x01",
            "悲劇ガ訪レルダロウ──《銀》\x07\x00\x02",
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
        "#0101F#6Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x103,
        (
            "#0201F#12P新作の公演を中止せよ……\x02\x03",

            "さもなくば炎の舞姫に\x01",
            "悲劇が訪れるだろう──《銀》。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x104,
        "#0301F#12P確かに脅迫文っぽいな。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#1706F#5P脅迫文というより\x01",
            "ただの嫌がらせじゃない？\x02\x03",

            "#1700F言っちゃあなんだけど\x01",
            "この程度の脅し文句なんか\x01",
            "珍しくもないんだし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B2A1():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B2A1)

    #C0512
    ChrTalk(
        0x101,
        "#0001F#12P……そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xD,
        (
            "まあ、ウチもそれなりに\x01",
            "儲けさせてもらってるからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xD,
        (
            "やっかみ半分、面白半分で\x01",
            "脅しめいた手紙はそこそこ届くよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xD,
        (
            "ただ、今回ばかりはちょっと\x01",
            "気になることがあってねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x103,
        "#0205F#12P気になること……？\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x104,
        (
            "#0301F#12Pふむ……\x01",
            "そこにある差出人か。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xD,
        "ああ、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xD,
        (
            "今まで送られてきた脅迫状は\x01",
            "無記名が殆んどだったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x9,
        (
            "#1806F#5Pそれが今回は《銀》という\x01",
            "思わせぶりな名前が書かれていて……\x02\x03",

            "#1808Fただのイタズラとは\x01",
            "思えない感じがするんです……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "#1703F#5Pう～ん……\x01",
            "気のせいだと思うけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#0003F#12Pふむ……\x02\x03",

            "#0001F皆さん、《銀》という名前に\x01",
            "何か心当たりはないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x8,
        (
            "#1704F#5Pまったくもって無いわね。\x02\x03",

            "#1701Fそもそも人の名前なの、それ？\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x9,
        (
            "#1806F#5P何かの暗号とか\x01",
            "そんな感じはしますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xD,
        (
            "うーん、ウチの新作のタイトルに\x01",
            "『銀』という言葉は入っているが……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xD,
        "そのくらいだねぇ、心当たりは。\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x102,
        "#0103F#6Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x101,
        (
            "#0001F#12Pでは……それ以外の\x01",
            "心当たりはありませんか？\x02\x03",

            "失礼かとは思いますが、\x01",
            "最近、誰かの恨みを買うような\x01",
            "事があったりしたとか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0529
    ChrTalk(
        0x9,
        "#1808F#5Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xD,
        "うーん、まさかねぇ。\x02",
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
            "#1705F#11Pあら……？\x02\x03",

            "あなたたち、誰かに恨まれる\x01",
            "心当たりなんてあるの？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_B7BB():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B7BB)
    Sleep(50)
    TurnDirection(0xD, 0x9, 500)
    Sleep(300)

    #C0532
    ChrTalk(
        0xD,
        "#11Pあ、あのねぇ……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x9,
        (
            "#1806F#6P私たちではなくて……\x01",
            "イリアさんの話ですよ。\x02\x03",

            "#1801Fほら、つい先日、\x01",
            "例の会長さんのことを……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0534
    ChrTalk(
        0x8,
        (
            "#1705F#11Pああ、あのハゲオヤジの事か。\x02\x03",

            "#1706Fあまりにどうでもいいから\x01",
            "すっかり忘れてたわ。\x02",
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
        "#0200F#12Pそのハゲオヤジというのは……？\x02",
    )

    CloseMessageWindow()

    def lambda_B991():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B991)
    Sleep(200)

    def lambda_B9A1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B9A1)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Sleep(100)

    #C0536
    ChrTalk(
        0x8,
        (
            "#1700F#5Pああ、マルコーニっていう\x01",
            "脂ぎったハゲオヤジのことよ。\x02\x03",

            "《ルバーチェ商会》っていう\x01",
            "ゴロツキどもを使ってるっていう。\x02",
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
        "#0005F#12Pえ……！？\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x102,
        "#0101F#6Pルバーチェ商会……！\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x104,
        "#0301F#12Pその名前が出るかよ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0540
    ChrTalk(
        0x8,
        "#1705F#5Pなに、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        (
            "#0006F#12Pい、いえ……\x01",
            "最近よく聞く名前なので。\x02\x03",

            "#0001Fそれでその……\x01",
            "ルバーチェ商会の会長とは\x01",
            "どういう経緯で？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x8,
        (
            "#1706F#5Pよく接待かなんかで\x01",
            "ウチに客を連れてくるのよ。\x02\x03",

            "#1701Fいつも貴賓席を使っているから\x01",
            "相当、羽振りはいいんでしょうけど、\x01",
            "舞台とかには全然興味ないみたいね。\x02\x03",

            "あたしの事も、演技とか全然見ないで\x01",
            "身体ばっかりイヤらしい目で見てたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x9,
        "#1806F#1Pイ、イリアさん……\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xD,
        "よく気付くねぇ、そんな事。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x8,
        (
            "#1704F#5P舞台の最中は、観客席も含めて\x01",
            "あたしの世界だから当然でしょ。\x02\x03",

            "#1700Fで、この前そのハゲオヤジが\x01",
            "あたしに言い寄ってきたわけよ。\x02\x03",

            "帝都のオペラハウスへの進出を\x01",
            "バックアップしてやろうとか\x01",
            "恩着せがましいことを言いながら。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#0305F#12Pへえ、そんな予定があるんスか？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xD,
        (
            "うーん、帝国からだけではなく、\x01",
            "共和国方面からも要請があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xD,
        (
            "期間限定でいいから\x01",
            "特別公演をやってくれないかってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "そういえば、この前リベールの\x01",
            "王立競技場#10Rグランアリーナ#からもオファーがあったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#0003F#12Pやはり凄い人気なんですね……\x02\x03",

            "#0001Fでも、どうしてそれを\x01",
            "ルバーチェの会長が\x01",
            "バックアップするという話に？\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xD,
        (
            "どうやら帝都方面に強力な\x01",
            "コネを持っているらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xD,
        (
            "まあ、彼らの噂を聞いている限り、\x01",
            "遠慮したい類のコネだと思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#0108F#6P……ルバーチェはどちらかというと\x01",
            "帝国と繋がりの深いマフィアです。\x02\x03",

            "#0101F帝都の暗黒街とのコネクションも\x01",
            "それなりにあるのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x9,
        "#1801F#5Pそ、そうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x103,
        (
            "#0205F#12Pそれで結局、そのハゲオヤジを\x01",
            "どうしたんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x8,
        (
            "#1709F#5Pもちろん、丁重にお断りしたわ。\x02\x03",

            "二度と迫って来る気が起こらないよう、\x01",
            "ビンタもかましてあげたけど。\x02",
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
        "#0011F#12Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#0105F#6Pマ、マフィアのボスに\x01",
            "そんなことを……？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x9,
        (
            "#1806F#5Pそうなんです……\x01",
            "私もう気を失いそうになって。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xD,
        "私も気絶しそうだったよ……\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xD,
        (
            "ただまあ、向こうも\x01",
            "イリア君の身体を触ってくるなど\x01",
            "無謀な──いや無礼だったからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xD,
        (
            "周りの取り成しもあって\x01",
            "その場は何とか収まったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x104,
        (
            "#0303F#12P向こうがその時の屈辱を\x01",
            "忘れてない可能性はある……\x02\x03",

            "#0301Fそういう事ッスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#0203F#12P……確かに脅迫状を出す\x01",
            "動機にはなりそうですね。\x02",
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
            "#0003F#12P──事情は大体分かりました。\x02\x03",

            "#0001Fまずは幾つか手がかりを\x01",
            "当たってみようと思います。\x02\x03",

            "イリアさん、この脅迫状は\x01",
            "お預かりしてもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x8,
        (
            "#1700F#5Pええ、構わないわ。\x02\x03",

            "#1704Fふふっ……\x01",
            "少し目付きが変わったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x101,
        "#0005F#12Pえ……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x8,
        (
            "#1704F#5Pあたしたちが舞台#4Rステージ#に\x01",
            "上がる時と同じような目……\x02\x03",

            "#1702Fいいわ、あなたたちなら\x01",
            "良い仕事をしてくれそうだし。\x02\x03",

            "リーシャの心配を取り除くためにも\x01",
            "この件、全てお任せしておくわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x9,
        "#1802F#1Pイリアさん……\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        "#0002F#12P──引き受けました。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x102,
        (
            "#0104F#6Pご期待に沿えるよう、\x01",
            "尽力させていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21960, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddItemNumber(0x324, 1)
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
            "イリアさんも納得してくれたし、\x01",
            "相談して本当に良かったです！\x02",
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
            "#0004F#12Pはは……これからですよ。\x02\x03",

            "#0001Fどうやら一筋縄では\x01",
            "いかなくなりそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x9,
        "#1806F#5Pそ、そうですよね……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0575
    ChrTalk(
        0x9,
        (
            "#1805F#5Pそういえば……\x02\x03",

            "#1802Fあの、どうかそんな丁寧に\x01",
            "話さないで頂けませんか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        "#0005F#12Pえ……？\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x9,
        (
            "#1804F#5Pその、私まだ新米ですし……\x02\x03",

            "ロイドさんやエリィさんよりも\x01",
            "ちょっと年下だと思いますし……\x02\x03",

            "#1800Fそんな丁寧に話しかけられると\x01",
            "何だか申しわけなくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x101,
        (
            "#0000F#12Pそ、そうですか……？\x02\x03",

            "#0002Fそれじゃあ──\x01",
            "ちょっと砕けさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x9,
        (
            "#1809F#5Pは、はい！\x01",
            "どうもありがとうございます！\x02",
        )
    )

    CloseMessageWindow()

    #N0580
    NpcTalk(
        0x8,
        "イリアの声",
        (
            "#2Sリーシャ？\x01",
            "ミーティングを始めるわよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0581
    ChrTalk(
        0x9,
        "#1802F#2Pはい、イリアさん！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0582
    ChrTalk(
        0x9,
        (
            "#1804F#5Pそれでは皆さん……失礼します。\x02\x03",

            "#1802F何か分かったら遠慮なく\x01",
            "劇場にいらっしゃってください。\x02",
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
        "#0000F#5Pさすがに忙しそうだな……\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#0304Fま、公演まで数百回は\x01",
            "稽古を重ねるらしいからな。\x02\x03",

            "#0300F脅迫状を気に懸けている時間が\x01",
            "もったいないのも頷けるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x103,
        "#0204F#11Pなるほど……納得です。\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x102,
        (
            "#0102Fふふ、新作の成功のためにも\x01",
            "何とか解決できるといいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        "#0004F#5Pああ……そうだな。\x02",
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

    # Function_49_ABF4 end

    def Function_50_CD04(): pass

    label("Function_50_CD04")

    OP_95(0x9, -49720, 0, 370, 2500, 0x0)
    OP_95(0x9, -50520, 0, 10010, 2500, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_50_CD04 end

    def Function_51_CD3B(): pass

    label("Function_51_CD3B")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_CD4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CD4A)
    OP_95(0xFE, -620, 0, 5850, 1500, 0x0)
    OP_95(0xFE, -620, 2390, 11360, 1500, 0x0)
    Return()

    # Function_51_CD3B end

    def Function_52_CD7F(): pass

    label("Function_52_CD7F")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_CD8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CD8E)
    OP_95(0xFE, 520, 0, 5850, 1500, 0x0)
    OP_95(0xFE, 520, 2390, 11360, 1500, 0x0)
    Return()

    # Function_52_CD7F end

    def Function_53_CDC3(): pass

    label("Function_53_CDC3")

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
            "#0003F#5Pマクダエル市長も\x01",
            "お出でになったみたいだな……\x02\x03",

            "#0000Fそういえば、今回の新作に\x01",
            "全面的に協力しているんだっけ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0589
    ChrTalk(
        0x102,
        (
            "#0104F#12Pええ、元々おじいさまは\x01",
            "アルカンシェルのファンだから。\x02\x03",

            "#0102Fリーシャさんのデビューも　\x01",
            "すごく楽しみにしているみたい。\x02",
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
            "あはは……期待に\x01",
            "応えられるといいんですけど。\x02\x03",

            "それより……\x01",
            "《銀#2Rイン#》という人が言ったように\x01",
            "本当に何か起こるんでしょうか？\x02",
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

    def lambda_D397():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D397)
    Sleep(50)

    def lambda_D3A7():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D3A7)
    Sleep(300)

    #C0591
    ChrTalk(
        0x101,
        (
            "#0006F#11P……分からない。\x01",
            "だが、可能性は高いと思う。\x02\x03",

            "#0000F捜査一課が警戒しているから\x01",
            "イリアさんは大丈夫だと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x9,
        "#6206F#6Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x102,
        (
            "#0106F#11Pそれよりも……\x01",
            "イリアさんに今回のことを\x01",
            "本当に伝えなくてよかったの？\x02\x03",

            "#0101F劇団長も同じ考えみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x9,
        (
            "#6204F#6Pはい……いいんです。\x02\x03",

            "あの人には──\x01",
            "イリアさんには余計な心配をしないで\x01",
            "輝いていて欲しいですから。\x02\x03",

            "#6202Fそれが私の……\x01",
            "私たち全員の願いなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        (
            "#0002F#11P君は本当に\x01",
            "イリアさんが好きなんだな……\x02\x03",

            "#0000Fいったい、どうしてそこまで？\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x9,
        (
            "#6202F#6Pふふ……\x02\x03",

            "#6204Fこの劇団には、かなり強引に\x01",
            "誘われてしまいましたけど……\x02\x03",

            "でも私、嬉しかったんです。\x02\x03",

            "#6208Fクロスベルに来るまで……\x01",
            "私は決められた道しか\x01",
            "歩いていませんでしたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x101,
        "#0005F#11Pえ……？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x9,
        (
            "#6204F#6Pだからあの人の演技を見て\x01",
            "とても惹き付けられたんです。\x02\x03",

            "ああ、こんな風にただ上を向いて\x01",
            "力強く輝ける人がいるんだって。\x02\x03",

            "#6210Fふふ、決して手が届かないものだから\x01",
            "憧れてしまったのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        "#0108F#11Pリーシャさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0600
    ChrTalk(
        0x101,
        (
            "#0004F#11P──手が届かないなんて\x01",
            "そんな事はないんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x9,
        "#6205F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#0003F#11P確かに、今回の君の役は\x01",
            "《月の姫》……\x02\x03",

            "《太陽の姫》の輝きを受けて\x01",
            "映える役かもしれない。\x02\x03",

            "#0002Fでも、素人目から見ても\x01",
            "君とイリアさんの演技の良さは\x01",
            "それぞれ別物じゃないかと思った。\x02\x03",

            "#0009F君は君自身として……\x01",
            "いつかきっと輝けるはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x9,
        "#6210F#6Pそう……でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ、だからこそイリアさんも\x01",
            "君を誘ったんじゃないかと思う。\x02\x03",

            "#0000F今回の事件……\x01",
            "俺たちも壁にぶつかったけど\x01",
            "何とかここまで辿り着いた。\x02\x03",

            "きっと解決してみせるから……\x01",
            "だから君も全力で頑張って欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x9,
        (
            "#6209F#6Pは、はい……！\x02\x03",

            "#6202Fそれじゃあ私、\x01",
            "そろそろ行きますね。\x02\x03",

            "ロイドさん、エリィさん。\x01",
            "どうか頑張ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x101,
        "#0002F#11Pああ……！\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x102,
        "#0109F#11Pええ、あなたも頑張って。\x02",
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
            "#0000F#5Pさてと……\x01",
            "俺たちもステージが始まるまで\x01",
            "どこか別の場所で待機するか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0609
    ChrTalk(
        0x101,
        "#0005F#5Pん、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x102,
        (
            "#0113F#11Pはあ……まったくもう。\x02\x03",

            "これで無自覚なんだから\x01",
            "タチが悪いというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#0011F#5Pへ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0612
    ChrTalk(
        0x102,
        (
            "#0111F#12P──何でもありません。\x02\x03",

            "#0106Fそれよりも、あそこまで\x01",
            "はっきりと約束したんだから。\x02\x03",

            "#0102F今回の事件……\x01",
            "絶対に解決しないとね？\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        "#0000F#5Pああ……もちろんだ。\x02",
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

    # Function_53_CDC3 end

    def Function_54_DD43(): pass

    label("Function_54_DD43")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, -7470, 0, 4730, 1500, 0x0)
    OP_95(0xFE, -6470, 0, 3720, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_DD43 end

    def Function_55_DD7E(): pass

    label("Function_55_DD7E")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, -7470, 0, 4730, 1500, 0x0)
    OP_95(0xFE, -7000, 0, 5160, 1500, 0x0)
    OP_93(0xFE, 0x80, 0x1F4)
    Return()

    # Function_55_DD7E end

    def Function_56_DDB9(): pass

    label("Function_56_DDB9")

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
            "#0004F#12P始まったか……\x02\x03",

            "#0002Fしかし凄い盛り上がり方だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x102,
        (
            "#0109Fふふ、本当だったら\x01",
            "私もこの目で見たかったわね。\x02\x03",

            "#0102F一課の人たちが羨ましいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x101,
        (
            "#0006F#12Pでも、そんな凄いステージが\x01",
            "目の前で行われてるっていうのに\x01",
            "警戒してなきゃいけないんだろう？\x02\x03",

            "#0001F逆に辛くないかな、それって。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x102,
        (
            "#0104Fふふっ、そうかもね。\x02\x03",

            "#0100F──それじゃあ、私たちも\x01",
            "劇場内の巡回を始めましょう。\x02\x03",

            "ただし一課の人たちがいるから\x01",
            "観客席は覗くくらいにしないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        "#0000F#12Pああ、そうだな。\x02",
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
            "#0000Fこちらロイド……\x01",
            "２人とも、聞こえてるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0620
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、聞こえてるぜ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0621
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……どうやら\x01",
            "始まったみたいですね。\x07\x00\x02",
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
            "#0000Fああ、これから\x01",
            "劇場内の巡回を開始する。\x02\x03",

            "そちらは引き続き、\x01",
            "劇場周辺の警戒を続けてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0623
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……了解しました。\x02\x03",

            "ツァイトも来てくれたので\x01",
            "こちらの方は万全です。\x07\x00\x02",
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
            "#0012Fそ、そうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0625
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "変なヤツがいたら連絡する。\x02\x03",

            "ステージに見とれて\x01",
            "一課の連中に見つかんなよ？\x07\x00\x02",
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
            "#0000Fああ、分かってる。\x02",
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
            "#0003F#12P──巡回を始めよう。\x02\x03",

            "#0001Fまずは一通り回りながら\x01",
            "劇場内のスタッフに声をかけて\x01",
            "異常がないかどうか確かめるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x102,
        "#0101Fええ、分かったわ。\x02",
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

    # Function_56_DDB9 end

    def Function_57_E4F9(): pass

    label("Function_57_E4F9")

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
            "#0004Fどうやら\x01",
            "異常は無さそうだな……\x02\x03",

            "#0002Fそれにしてもイリアさん、\x01",
            "とんでもなく凄いな……\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x102,
        (
            "#0102Fそうね……\x02\x03",

            "#0104F……もう離れましょう。\x02\x03",

            "このまま見ていたら\x01",
            "引き込まれてしまいそうだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x101,
        "#0012Fああ、そうだな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x84, 5)
    EventEnd(0x5)
    Return()

    # Function_57_E4F9 end

    def Function_58_E65E(): pass

    label("Function_58_E65E")

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
            "#0004F異常なし……と。\x02\x03",

            "#0002Fそれにしても\x01",
            "リーシャ、本当に凄いな……\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x102,
        (
            "#0102Fええ、イリアさんとは\x01",
            "違う方向性の舞いね……\x02\x03",

            "まさに銀の光をまとった\x01",
            "月の姫って感じだわ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x85, 1)
    EventEnd(0x5)
    Return()

    # Function_58_E65E end

    def Function_59_E78F(): pass

    label("Function_59_E78F")

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
        "#0012Fうーん、盛り上がってるな……\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x102,
        (
            "#0104Fええ、まさか２人が\x01",
            "姉妹という設定だったなんて……\x02\x03",

            "#0102Fこの先、どうなるのかしら……？\x02",
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
        "#0011F……じゃなくて！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    #C0637
    ChrTalk(
        0x102,
        (
            "#0106Fそ、そうね……\x02\x03",

            "巡回に専念しないと……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x85, 5)
    EventEnd(0x5)
    Return()

    # Function_59_E78F end

    def Function_60_E956(): pass

    label("Function_60_E956")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_E9C0")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_EA19")

    label("loc_E9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_EA19")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_EA19")

    FadeToBright(1000, 0)
    OP_0D()

    #C0638
    ChrTalk(
        0x101,
        (
            "#0003FＳ席は異常なし……\x02\x03",

            "#0000Fまあ、ダドリー捜査官がいるから\x01",
            "こっちの方は心配なさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        (
            "#0100F……そうね。\x02\x03",

            "他を回ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_EAD8")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_EAF2")

    label("loc_EAD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_EAF2")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_EAF2")

    SetScenarioFlags(0x84, 6)
    EventEnd(0x5)
    Return()

    # Function_60_E956 end

    def Function_61_EAF8(): pass

    label("Function_61_EAF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_EB62")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_EBBB")

    label("loc_EB62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_EBBB")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_EBBB")

    FadeToBright(1000, 0)
    OP_0D()

    #C0640
    ChrTalk(
        0x101,
        (
            "#0000F大丈夫そうだな……\x02\x03",

            "#0006Fしかし、ダドリー捜査官も\x01",
            "大したものだよな……\x02\x03",

            "#0001Fあれだけのステージを前にして\x01",
            "警戒が緩んでなさそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        "#0103Fええ……鋼の意志って感じね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_ECA1")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_ECBB")

    label("loc_ECA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_ECBB")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_ECBB")

    SetScenarioFlags(0x85, 2)
    EventEnd(0x5)
    Return()

    # Function_61_EAF8 end

    def Function_62_ECC1(): pass

    label("Function_62_ECC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_ED2B")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_ED84")

    label("loc_ED2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_ED84")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_ED84")

    FadeToBright(1000, 0)
    OP_0D()

    #C0642
    ChrTalk(
        0x101,
        (
            "#0012Fはは……ダドリー捜査官も\x01",
            "ステージが気になるみたいだな。\x02\x03",

            "#0000F警戒は怠っていないみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x102,
        (
            "#0104Fふふ、無理もないわ。\x02\x03",

            "#0100Fアルカンシェルのステージを見て\x01",
            "心が動かない人はいないでしょうし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_EE84")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_EE9E")

    label("loc_EE84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_EE9E")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_EE9E")

    SetScenarioFlags(0x85, 6)
    EventEnd(0x5)
    Return()

    # Function_62_ECC1 end

    def Function_63_EEA4(): pass

    label("Function_63_EEA4")

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
            "#0005F（ここは貴賓席か……）\x02\x03",

            "#0001F（制服警官しかいないけど\x01",
            "  大丈夫なのか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x102,
        (
            "#0104F（まあ、アーネストさんは\x01",
            "  おじいさまの護衛でもあるから。）\x02\x03",

            "#0100F（何か起こった時も十分、\x01",
            "  対処できると思うけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x101,
        "#0000F（それもそうか……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x84, 7)
    EventEnd(0x5)
    Return()

    # Function_63_EEA4 end

    def Function_64_F021(): pass

    label("Function_64_F021")

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
            "#0003F（異常なし……か。）\x02\x03",

            "#0001F（ちょっと警官の注意が\x01",
            "  散漫になっていそうだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x102,
        (
            "#0106F（まあ、あのステージを見てたら\x01",
            "  無理ないかもしれないわね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x85, 3)
    EventEnd(0x5)
    Return()

    # Function_64_F021 end

    def Function_65_F14B(): pass

    label("Function_65_F14B")

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
            "#0000F（……大丈夫そうだな。）\x02\x03",

            "（警官はともかく、アーネストさんは\x01",
            "  周囲を警戒してそうな感じだし……）\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x102,
        "#0100F（ええ、そうね……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x85, 7)
    EventEnd(0x5)
    Return()

    # Function_65_F14B end

    def Function_66_F258(): pass

    label("Function_66_F258")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2C7")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_F37A")

    label("loc_F2C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F32A")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_F37A")

    label("loc_F32A")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_F37A")

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
        "#0005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x102,
        "#0100F第１幕が終わったみたいね。\x02",
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

    # Function_66_F258 end

    def Function_67_F441(): pass

    label("Function_67_F441")

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
            "#0004F#5P第２幕が始まったか……\x02\x03",

            "#0002Fリーシャ、頑張ってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        (
            "#0104Fええ……\x01",
            "かなりの拍手だったわね。\x02\x03",

            "#0100Fそれじゃあ、\x01",
            "また一通り回ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        "#0000F#5Pああ……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -890, 2500, 12720, 0)
    SetScenarioFlags(0x85, 0)
    OP_29(0x43, 0x1, 0xB)
    EventEnd(0x5)
    Return()

    # Function_67_F441 end

    def Function_68_F588(): pass

    label("Function_68_F588")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F7")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_F6AA")

    label("loc_F5F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F65A")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_F6AA")

    label("loc_F65A")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_F6AA")

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
        "#0000F第２幕が終わったか……\x02",
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x102,
        (
            "#0104Fええ……\x01",
            "盛り上がってるみたいね。\x02",
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

    # Function_68_F588 end

    def Function_69_F784(): pass

    label("Function_69_F784")

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
            "#0000F#5P第３幕……折り返し地点か。\x02\x03",

            "#0012Fしかしさっきから凄い反応だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x102,
        (
            "#0104Fええ……\x01",
            "それだけ今回のステージの\x01",
            "完成度が高いんだと思う。\x02\x03",

            "#0108Fこのまま何事もなく\x01",
            "終わってくれるといいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x101,
        (
            "#0006F#5Pああ……\x02\x03",

            "#0000F犯人は捕まえられないけど、\x01",
            "それに越したことはないよな。\x02",
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

    # Function_69_F784 end

    def Function_70_F930(): pass

    label("Function_70_F930")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99F")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_FA52")

    label("loc_F99F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA02")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_FA52")

    label("loc_FA02")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_FA52")

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
        "#0001F……第３幕終了か……\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x102,
        (
            "#0101Fええ……\x01",
            "最終幕が始まるわ。\x02",
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

    # Function_70_F930 end

    def Function_71_FB1B(): pass

    label("Function_71_FB1B")

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
            "#0004F#11Pふう……\x02\x03",

            "#0000Fどうやらプレ公演は\x01",
            "何とか乗り切れそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x102,
        (
            "#0104F#5Pええ、回ってみたところ\x01",
            "不審な人も見かけなかったし。\x02",
        )
    )

    CloseMessageWindow()

    #N0665
    NpcTalk(
        0xB,
        "男性の声",
        "ロイド様、エリィ様……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_FC93():

        label("loc_FC93")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_FC93")

    QueueWorkItem2(0x101, 0, lambda_FC93)

    def lambda_FCA5():

        label("loc_FCA5")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_FCA5")

    QueueWorkItem2(0x102, 0, lambda_FCA5)
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
        "#0005F#12Pバルサモ支配人……\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x102,
        "#0105F#6Pどうなさったんですか？\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xB,
        "#5Pそれが……\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xB,
        (
            "#5P少々、不審な動きをされている\x01",
            "お客様がおりまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0xB,
        (
            "#5Pしかも、招待客リストの中には\x01",
            "いらっしゃらなかったのですが……\x02",
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
        "#0011F#12Pえ……！？\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x102,
        "#0101F#6Pど、何処にいたんですか！？\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xB,
        "#5P右奥にある階段の上です。\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xB,
        (
            "#5PどうやらＳ席の様子を\x01",
            "こっそり伺っているらしく……\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#0013F#12P分かりました……！\x01",
            "すぐに確認してきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x102,
        (
            "#0101F#6P支配人はこちらで\x01",
            "待機していてください！\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xB,
        "#5Pは、はい……！\x02",
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

    # Function_71_FB1B end

    def Function_72_FFD0(): pass

    label("Function_72_FFD0")

    OP_92(0xFE, 0xBC98, 0x38A4, 0x320)
    OP_95(0xFE, 48280, 5600, 14500, 5000, 0x1)

    def lambda_FFF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FFF6)
    OP_95(0xFE, 46280, 5600, 14900, 5000, 0x1)
    Return()

    # Function_72_FFD0 end

    def Function_73_10017(): pass

    label("Function_73_10017")

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
        "#0005F#5P（な……！？）\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x102,
        "#0101F#11P（あの人は……！）\x02",
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
            "#2101F#11Pまったく、どうしてダドリーが\x01",
            "こんな場所にいるんだか……！\x02\x03",

            "せっかくのスクープを前に\x01",
            "お預けもいいところだわ……！\x02\x03",

            "#2106Fかといってシャッターを切ったら\x01",
            "あいつに気付かれそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "グレイスさん……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(49230, 6900, 14230, 3000)
    MoveCamera(44, 18, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_1027A():
        OP_95(0xFE, 49000, 5600, 13200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1027A)
    OP_93(0x1E, 0xB4, 0x1F4)

    def lambda_1029B():
        OP_95(0xFE, 50400, 5600, 13200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1029B)
    WaitChrThread(0x101, 0)

    #C0682
    ChrTalk(
        0x1E,
        (
            "#2105F#5Pあらら……ロイド君！？\x02\x03",

            "エリィちゃんも……\x01",
            "こんな所で何しているのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x101,
        "#0013F#12Pそれはこちらの台詞です……！\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x102,
        (
            "#0101Fグレイスさん、どうしてここに？\x02\x03",

            "招待された訳ではありませんよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x1E,
        (
            "#2109F#5Pあはは……\x01",
            "実はちょっと訳があって……\x02\x03",

            "裏技使って入っちゃったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        "#0105Fう、裏技……？\x02",
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x1E,
        (
            "#2106F#5Pんー、内緒にしててね？\x02\x03",

            "#2102F清掃業者の人たちに紛れて\x01",
            "コッソリと……って感じ？\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        "#0011F#12Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x102,
        "#0101Fど、どうしてそんな事を……\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1E,
        (
            "#2106F#5Pだってだって～、\x01",
            "ウチに来た取材用のチケット、\x01",
            "他の記者に取られちゃったんだもん！\x02\x03",

            "#2110Fプレ公演は絶対見たかったし、\x01",
            "他のネタを追ってる所だったし、\x01",
            "これは忍び込むしかないじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x101,
        "#0006F#12Pあ、あのですね……\x02",
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x102,
        "#0106F……何て人騒がせな……\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x1E,
        (
            "#2102F#5Pほ、ほら、それよりも\x01",
            "一緒にここから舞台を見ない？\x02\x03",

            "#2109Fせっかくのクライマックスだもん。\x01",
            "見ないと一生後悔するわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        (
            "#0003F#12P本公演で見ればいいでしょう！\x02\x03",

            "#0013Fそれよりも……\x01",
            "本当に理由はそれだけなんですか？\x02\x03",

            "まさか、脅迫状を送ったのは\x01",
            "グレイスさんとか言いませんよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x1E,
        (
            "#2105F#5P脅迫状……なにそれ！？\x02\x03",

            "そういえば、いざ忍び込んだら\x01",
            "ダドリーとか一課の連中を見かけて\x01",
            "びっくりしちゃったんだけど……\x02\x03",

            "#2101Fひょっとしてそれ絡みとか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x102,
        "#0108F……違うみたいね。\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x101,
        (
            "#0000F#12Pそ、そうだよな……\x02\x03",

            "いくらグレイスさんでも\x01",
            "そこまではしないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x1E,
        (
            "#2101F#5Pいくらあたしでもって……\x01",
            "ちょっと失礼なんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#0006F#12Pいや現に、忍び込んでまで\x01",
            "取材をしてるわけですし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x101,
        (
            "#0001F#12Pそういえば……\x01",
            "他のネタを追ってる所って\x01",
            "さっき言ってましたよね？\x02\x03",

            "どんなネタなんですか？\x02",
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
            "#2102F#5Pおっと、それは言えないわね。\x02\x03",

            "#2105Fハッ……\x01",
            "もしかして一課が出張ってるのは\x01",
            "『彼』を監視してるからとか……？\x02\x03",

            "#2106Fしまった、気付いているのは\x01",
            "あたしだけと思ってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        "#0005F#12Pそれって……\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x102,
        "#0101F《銀#2Rイン#》の事ですか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0704
    ChrTalk(
        0x1E,
        (
            "#2105F#5P《銀#2Rイン#》……何それ？\x02\x03",

            "#2101Fさっき言ってた脅迫状と\x01",
            "何か関係がある言葉なわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x102,
        "#0105Fち、違うんですか……\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x101,
        (
            "#0003F#12P……グレイスさん。\x01",
            "知ってる事を話してください。\x02\x03",

            "#0013Fでないとこのまま突き出しますよ？\x02",
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
            "#2105F#5Pちょ、ちょっとロイド君……\x01",
            "そんな殺生な。\x02\x03",

            "#2109Fあたしと君たちの仲じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        (
            "#0006F#12P今は少しでも\x01",
            "手がかりが欲しいんです。\x02\x03",

            "#0013Fだから教えてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x1E,
        (
            "#2106F#5Pふう……マジなのね。\x02\x03",

            "#2100Fでも、エリィちゃんの前で\x01",
            "こんなこと話してもいいのかな～。\x02",
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
        "#0005F#12Pそ、それはどういう……\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x102,
        "#0101F私が……どうしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x1E,
        (
            "#2103F#5Pまあいいか……\x01",
            "気をしっかり持ってよね？\x02\x03",

            "#2101F──あたしが追っていたネタは\x01",
            "市長の第一秘書に関する黒い噂よ。\x02",
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
        "#0105F………え…………\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x101,
        "#0007F#12Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x1E,
        (
            "#2104F#5Pアーネストって言ったっけ。\x01",
            "彼、相当ヤバイわよ。\x02\x03",

            "#2102F市長に内緒で事務所の資金を\x01",
            "勝手に流用してるらしいし……\x02\x03",

            "最近じゃ、帝国派議員と密談して\x01",
            "何か企んでるみたいなのよねぇ。\x02\x03",

            "#2109Fまさか市長を亡き者にって……\x01",
            "あはは、流石にそこまではしないか。\x02",
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
            "#0108Fね、ねえロイド……\x02\x03",

            "#0101Fもしこの状況で、おじいさまが\x01",
            "何者かに亡き者にされたら……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0717
    ChrTalk(
        0x101,
        (
            "#0005F#6P……目撃者さえ作らなければ\x01",
            "犯人は別のヤツに偽装できる……\x02\x03",

            "#0010F──それが狙いか！\x02",
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
        "#2105F#11Pちょ、ちょっと……！？\x02",
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

    # Function_73_10017 end

    def Function_74_11020(): pass

    label("Function_74_11020")


    def lambda_11025():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11025)
    OP_95(0xFE, -38080, 5600, 97990, 6000, 0x0)
    OP_95(0xFE, -47290, 5600, 107210, 6000, 0x0)
    OP_95(0xFE, -47070, 11200, 117460, 6000, 0x0)
    OP_95(0xFE, -47270, 11200, 123420, 6000, 0x0)
    TurnDirection(0xFE, 0x20, 800)
    Return()

    # Function_74_11020 end

    def Function_75_11089(): pass

    label("Function_75_11089")


    def lambda_1108E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1108E)
    OP_95(0xFE, -38080, 5600, 97990, 6000, 0x0)
    OP_95(0xFE, -47290, 5600, 107210, 6000, 0x0)
    OP_95(0xFE, -47070, 11200, 117460, 6000, 0x0)
    OP_95(0xFE, -46940, 11200, 122160, 6000, 0x0)
    TurnDirection(0xFE, 0x20, 800)
    Return()

    # Function_75_11089 end

    def Function_76_110F2(): pass

    label("Function_76_110F2")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x1000)
    OP_52(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0xFE, 0xFFFF4854, 0x1E672, 0x320)
    OP_95(0xFE, -47020, 11200, 124530, 6000, 0x0)

    def lambda_1112D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1112D)
    OP_95(0xFE, -47020, 11200, 126530, 6000, 0x0)
    Return()

    # Function_76_110F2 end

    def Function_77_1114E(): pass

    label("Function_77_1114E")

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
        "#0010F#5Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x102,
        "#0101F#5P貴賓席にいた警官……！？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1559, 255, 100, 0)    #voice#Dudley
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    def lambda_1132B():
        OP_95(0xFE, -47100, 11200, 119630, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1132B)
    WaitChrThread(0x1F, 0)
    Sleep(150)

    #C0721
    ChrTalk(
        0x1F,
        "#0607F#5P一体ここで何をしている！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0722
    ChrTalk(
        0x1F,
        "#0605F#5Pなっ……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1F, 800)

    #C0723
    ChrTalk(
        0x101,
        (
            "#0007F#5P話は後です……！\x01",
            "エリィ、飛び込むぞ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    #C0724
    ChrTalk(
        0x102,
        "#0101Fえ、ええ……！\x02",
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

    # Function_77_1114E end

    def Function_78_11458(): pass

    label("Function_78_11458")


    def lambda_1145D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1145D)
    OP_95(0xFE, -47010, 11200, 124560, 8000, 0x1)
    OP_95(0xFE, -47090, 11200, 117520, 8000, 0x1)
    OP_95(0xFE, -46520, 5600, 107590, 8000, 0x1)
    OP_95(0xFE, -41100, 5600, 100220, 8000, 0x1)
    OP_95(0xFE, -40120, 5600, 93460, 8000, 0x1)
    OP_95(0xFE, -39900, 0, 83980, 8000, 0x1)
    OP_95(0xFE, -37970, 0, 81930, 8000, 0x1)

    def lambda_114FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_114FA)
    OP_95(0xFE, -36970, 0, 81930, 7000, 0x0)
    Return()

    # Function_78_11458 end

    def Function_79_1151B(): pass

    label("Function_79_1151B")


    def lambda_11520():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11520)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_95(0xFE, -47010, 11200, 124560, 10000, 0x1)
    OP_95(0xFE, -47090, 11200, 117520, 10000, 0x1)
    OP_95(0xFE, -46520, 5600, 107590, 10000, 0x1)
    OP_95(0xFE, -41100, 5600, 100220, 10000, 0x1)
    OP_95(0xFE, -40120, 5600, 93460, 10000, 0x1)
    OP_9D(0xFE, 0xFFFF6424, 0x0, 0x1480C, 0x7D0, 0xBB8)
    OP_95(0xFE, -37970, 0, 81930, 10000, 0x1)

    def lambda_115C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_115C8)
    OP_95(0xFE, -36970, 0, 81930, 7000, 0x0)
    Return()

    # Function_79_1151B end

    def Function_80_115E9(): pass

    label("Function_80_115E9")


    def lambda_115EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_115EE)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_95(0xFE, -8490, 2500, 14030, 10000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 10000, 0x1)
    OP_95(0xFE, -720, 2500, 11820, 10000, 0x1)
    OP_95(0xFE, -290, 0, -5210, 10000, 0x1)

    def lambda_11657():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11657)
    OP_95(0xFE, -36970, 0, 81930, 600, 0x0)
    Return()

    # Function_80_115E9 end

    def Function_81_11678(): pass

    label("Function_81_11678")


    def lambda_1167D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1167D)
    OP_95(0xFE, -8490, 2500, 14030, 6000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 6000, 0x1)
    OP_95(0xFE, 1100, 2500, 11650, 6000, 0x1)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_81_11678 end

    def Function_82_116CD(): pass

    label("Function_82_116CD")


    def lambda_116D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_116D2)
    OP_95(0xFE, -8490, 2500, 14030, 6000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 6000, 0x1)
    OP_95(0xFE, -720, 2500, 11820, 6000, 0x1)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_82_116CD end

    def Function_83_11722(): pass

    label("Function_83_11722")

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
            "#0607Fくっ……\x01",
            "なんだあの異常な速さは！？\x02",
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
            "#0007Fランディ、ティオ！\x01",
            "そっちに市長の秘書が行く！\x02\x03",

            "真犯人だ、足止めしてくれ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ランディの声")

    #A0727
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "お、おお……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0728
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よく判りませんが了解です。\x07\x00\x02",
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

    # Function_83_11722 end

    def Function_84_11C3E(): pass

    label("Function_84_11C3E")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_84_11C3E end

    def Function_85_11C5A(): pass

    label("Function_85_11C5A")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_85_11C5A end

    def Function_86_11C76(): pass

    label("Function_86_11C76")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_86_11C76 end

    def Function_87_11C92(): pass

    label("Function_87_11C92")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CAD")
    Call(0, 88)
    Jump("loc_11D48")

    label("loc_11CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CC3")
    Call(0, 88)
    Jump("loc_11D48")

    label("loc_11CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CD9")
    Call(0, 88)
    Jump("loc_11D48")

    label("loc_11CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D48")

    #C0729
    ChrTalk(
        0x101,
        (
            "#0000F劇場の外に出てる場合じゃないな。\x02\x03",

            "外はティオとランディに任せて\x01",
            "中の警備に集中しよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D48")

    SetChrPos(0x0, 0, 0, -4730, 0)
    EventEnd(0x4)
    Return()

    # Function_87_11C92 end

    def Function_88_11D5C(): pass

    label("Function_88_11D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DBF")

    #C0730
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……\x01",
            "イリアさんに会わないとな。\x02\x03",

            "#0000F正面の扉からホールに入ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11E4E")

    #C0731
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは２階の観客席みたいだな。\x02\x03",

            "あまりうろうろすると迷惑になるし、\x01",
            "立ち入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FB4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F1C")

    #C0732
    ChrTalk(
        0x103,
        (
            "#0205Fあ……\x02\x03",

            "#0200F舞台の音楽が聞こえます。\x01",
            "イリアさんは稽古中ではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        (
            "#0000Fそうか……\x01",
            "きっとまた舞台にいるんだな。\x01",
            "正面の扉からホールに入ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FAC")

    label("loc_11F1C")


    #C0734
    ChrTalk(
        0x103,
        (
            "#0200F舞台の音楽が聞こえますね……\x01",
            "イリアさんは稽古中ではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        (
            "#0000Fきっとまた舞台にいるんだろう。\x01",
            "正面の扉からホールに入ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FAC")

    SetScenarioFlags(0x1, 4)
    Jump("loc_11FF6")

    label("loc_11FB4")

    SetChrName("")

    #A0736
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "イリアは舞台の方にいるようだ。\x01",
            "ホールに行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_11FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12066")

    #C0737
    ChrTalk(
        0x102,
        (
            "#0101Fロイド、不審者は右側の階段よ。\x01",
            "急ぎましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x101,
        "#0001F……ああ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_120B1")

    label("loc_12066")


    #C0739
    ChrTalk(
        0x101,
        (
            "#0001F不審者は右側の階段だ……\x01",
            "急ごう、エリィ！\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x102,
        "#0101F……ええ！\x02",
    )

    CloseMessageWindow()

    label("loc_120B1")

    Return()

    # Function_88_11D5C end

    def Function_89_120B2(): pass

    label("Function_89_120B2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0741
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "舞台稼動中に付き、\x01",
            "お客様には立ち入りを\x01",
            "ご遠慮頂いております。\x01",
            "    ～劇団アルカンシェル～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_121DD")

    #C0742
    ChrTalk(
        0x101,
        (
            "#0000F舞台裏には捜査一課が\x01",
            "何人も詰めているみたいだ……\x01",
            "こっちは任せて大丈夫そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x102,
        (
            "#0100Fええ、劇場内の見回りに\x01",
            "集中しましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121DD")

    TalkEnd(0xFF)
    Return()

    # Function_89_120B2 end

    SaveToFile()

Try(main)
