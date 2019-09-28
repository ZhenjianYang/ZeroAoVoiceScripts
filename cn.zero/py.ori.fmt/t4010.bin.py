from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t4010.bin",                # FileName
        "t4010",                    # MapName
        "t4010",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4010",                  # 0
        "艾拉尔达大主教",         # 1
        "基纳斯祭司",             # 2
        "伦顿祭司",               # 3
        "哈缇娜修女",             # 4
        "玛布尔修女",             # 5
        "贸易商摩尔吉奥",         # 6
        "诺艾尔上士",             # 7
        "塔米尔",                 # 8
        "哈米尔",                 # 9
        "小桃",                   # 10
        "潘莎",                   # 11
        "库塔",                   # 12
        "尤格特",                 # 13
        "亨利",                   # 14
        "游客塔库特",             # 15
        "男孩",                   # 16
        "女孩",                   # 17
        "男孩",                   # 18
        "女孩",                   # 19
        "男孩",                   # 20
        "女孩",                   # 21
        "哈罗德",                 # 22
        "索菲亚",                 # 23
        "柯林",                   # 24
        "雷缇",                   # 25
        "隆",                     # 26
        "SE控制",                 # 27
    ))

    AddCharChip((
        "chr/ch26500.itc",                   # 00
        "chr/ch25300.itc",                   # 01
        "chr/ch25400.itc",                   # 02
        "chr/ch25500.itc",                   # 03
        "chr/ch21802.itc",                   # 04
        "chr/ch00800.itc",                   # 05
        "chr/ch23800.itc",                   # 06
        "chr/ch23802.itc",                   # 07
        "chr/ch20702.itc",                   # 08
        "chr/ch22302.itc",                   # 09
        "chr/ch21402.itc",                   # 0A
        "chr/ch20602.itc",                   # 0B
        "chr/ch22202.itc",                   # 0C
        "chr/ch09302.itc",                   # 0D
        "chr/ch09402.itc",                   # 0E
        "chr/ch07202.itc",                   # 0F
        "chr/ch10300.itc",                   # 10
        "chr/ch24602.itc",                   # 11
        "chr/ch24702.itc",                   # 12
        "chr/ch23902.itc",                   # 13
        "chr/ch34202.itc",                   # 14
        "chr/ch21502.itc",                   # 15
        "chr/ch24400.itc",                   # 16
    ))

    DeclNpc(-209,    379,     23229,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-2960,   250,     20010,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(98069,   0,       6789,    315,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(2950,    189,     19709,   165,  257,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(150800,  200,     17500,   180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-3849,   150,     6519,    0,    341,  0x0, 0,   4,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(1289,    0,       23229,   270,  385,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(153690,  200,     16420,   45,   385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(154850,  200,     16180,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    469,  0x0, 0,   9,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(147139,  150,     9130,    0,    469,  0x0, 0,   20,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    469,  0x0, 0,   12,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(1649,    0,       11819,   0,    385,  0x0, 0,   22,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(154929,  150,     9130,    0,    469,  0x0, 0,   17,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(153619,  150,     6150,    0,    469,  0x0, 0,   18,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(153619,  150,     6150,    0,    469,  0x0, 0,   7,   0,   255, 255, 0,   28,  255,  0)
    DeclNpc(148490,  150,     6150,    0,    469,  0x0, 0,   19,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    469,  0x0, 0,   11,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    469,  0x0, 0,   21,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-5250,   200,     16600,   360,  389,  0x0, 0,   13,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-3250,   200,     16600,   360,  389,  0x0, 0,   14,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-4250,   200,     16600,   360,  389,  0x0, 0,   15,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(29,      0,       10930,   0,    385,  0x0, 0,   16,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(153619,  150,     12229,   0,    453,  0x0, 0,   11,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(150910,  200,     16530,   1200,    150800,  1700,    17500,   0x007E, 0,  10, 0x0000)
    DeclActor(40,      500,     21930,   1200,    -210,    2100,    23230,   0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_500",          # 00, 0
        "Function_1_5B8",          # 01, 1
        "Function_2_5E3",          # 02, 2
        "Function_3_86D",          # 03, 3
        "Function_4_99E",          # 04, 4
        "Function_5_9A2",          # 05, 5
        "Function_6_1AD2",         # 06, 6
        "Function_7_1CE0",         # 07, 7
        "Function_8_256B",         # 08, 8
        "Function_9_3112",         # 09, 9
        "Function_10_394B",        # 0A, 10
        "Function_11_394F",        # 0B, 11
        "Function_12_4967",        # 0C, 12
        "Function_13_4A7D",        # 0D, 13
        "Function_14_5284",        # 0E, 14
        "Function_15_5B99",        # 0F, 15
        "Function_16_5C42",        # 10, 16
        "Function_17_607D",        # 11, 17
        "Function_18_651B",        # 12, 18
        "Function_19_67CE",        # 13, 19
        "Function_20_69D6",        # 14, 20
        "Function_21_6BB2",        # 15, 21
        "Function_22_6D6D",        # 16, 22
        "Function_23_6EF0",        # 17, 23
        "Function_24_70CA",        # 18, 24
        "Function_25_7258",        # 19, 25
        "Function_26_7406",        # 1A, 26
        "Function_27_7551",        # 1B, 27
        "Function_28_767B",        # 1C, 28
        "Function_29_77D5",        # 1D, 29
        "Function_30_793F",        # 1E, 30
        "Function_31_7E81",        # 1F, 31
        "Function_32_7FBB",        # 20, 32
        "Function_33_818D",        # 21, 33
        "Function_34_842F",        # 22, 34
        "Function_35_85D8",        # 23, 35
        "Function_36_86B8",        # 24, 36
        "Function_37_8925",        # 25, 37
        "Function_38_8BB1",        # 26, 38
        "Function_39_A9DB",        # 27, 39
        "Function_40_AA1E",        # 28, 40
        "Function_41_B499",        # 29, 41
        "Function_42_BE62",        # 2A, 42
        "Function_43_C041",        # 2B, 43
        "Function_44_CAF4",        # 2C, 44
        "Function_45_D235",        # 2D, 45
        "Function_46_12118",       # 2E, 46
        "Function_47_12134",       # 2F, 47
        "Function_48_12157",       # 30, 48
        "Function_49_12EF5",       # 31, 49
        "Function_50_12F6A",       # 32, 50
        "Function_51_12F83",       # 33, 51
        "Function_52_12FF5",       # 34, 52
    ))


    def Function_0_500(): pass

    label("Function_0_500")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_540"),
        (1, "loc_54C"),
        (2, "loc_558"),
        (3, "loc_564"),
        (4, "loc_570"),
        (5, "loc_57C"),
        (6, "loc_588"),
        (SWITCH_DEFAULT, "loc_594"),
    )


    label("loc_540")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_54C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_558")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_564")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_570")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_57C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_588")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_594")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_5A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_5B7")

    Return()

    # Function_0_500 end

    def Function_1_5B8(): pass

    label("Function_1_5B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E2")
    OP_94(0xFE, 0x17A8E, 0x125C, 0x186A0, 0x1D4C, 0x3E8)
    Sleep(450)
    Jump("Function_1_5B8")

    label("loc_5E2")

    Return()

    # Function_1_5B8 end

    def Function_2_5E3(): pass

    label("Function_2_5E3")

    BeginChrThread(0xA, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5FC")
    ClearChrFlags(0x20, 0x80)
    Jump("loc_859")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_62E")
    SetChrPos(0xB, 149530, 200, 17470, 90)
    OP_93(0xC, 0x10E, 0x0)
    ClearChrFlags(0xE, 0x80)
    OP_93(0x8, 0x5A, 0x0)
    Jump("loc_859")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_63C")
    Jump("loc_859")

    label("loc_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_66D")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_859")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_6F3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 154930, 150, 9130, 0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xF, 148490, 150, 12230, 0)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 147140, 150, 12230, 0)
    Jump("loc_859")

    label("loc_6F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_701")
    Jump("loc_859")

    label("loc_701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_720")
    SetChrPos(0xC, 148920, 0, 13890, 180)
    Jump("loc_859")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_72E")
    Jump("loc_859")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_757")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xC, 154300, 200, 17590, 180)
    Jump("loc_859")

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_765")
    Jump("loc_859")

    label("loc_765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_773")
    Jump("loc_859")

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7AC")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 96000, 0, 7830, 270)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_859")

    label("loc_7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7D6")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 96000, 0, 7830, 270)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_859")

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_850")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xF, 154930, 0, 12230, 0)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 153620, 0, 12230, 0)
    Jump("loc_859")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_859")

    label("loc_859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86C")
    ClearChrFlags(0x16, 0x80)

    label("loc_86C")

    Return()

    # Function_2_5E3 end

    def Function_3_86D(): pass

    label("Function_3_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_87B")
    Jump("loc_942")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_889")
    Jump("loc_942")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_897")
    Jump("loc_942")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8A5")
    Jump("loc_942")

    label("loc_8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_8B3")
    Jump("loc_942")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_8C1")
    Jump("loc_942")

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8D3")
    OP_65(0x0, 0x1)
    Jump("loc_942")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8E1")
    Jump("loc_942")

    label("loc_8E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8F3")
    OP_65(0x0, 0x1)
    Jump("loc_942")

    label("loc_8F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_901")
    Jump("loc_942")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_90F")
    Jump("loc_942")

    label("loc_90F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_91D")
    Jump("loc_942")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_92B")
    Jump("loc_942")

    label("loc_92B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_939")
    Jump("loc_942")

    label("loc_939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_942")

    label("loc_942")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B")
    Event(0, 37)

    label("loc_96B")

    Jump("loc_98B")

    label("loc_970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")
    Event(0, 36)

    label("loc_98B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_99D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_99D")

    Return()

    # Function_3_86D end

    def Function_4_99E(): pass

    label("Function_4_99E")

    Call(0, 5)
    Return()

    # Function_4_99E end

    def Function_5_9A2(): pass

    label("Function_5_9A2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A87")

    #C0001
    ChrTalk(
        0x8,
        (
            "遗迹中的那口大钟……\x01",
            "到底是怎么回事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "（如果那个钟是古代遗物的话……\x01",
            "　引来那些人插手的\x01",
            "　可能性就很高了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "（……哼，岂能让他们得逞。\x01",
            "　我绝对不会允许那种人\x01",
            "　进入克洛斯贝尔。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AD5")

    label("loc_A87")


    #C0004
    ChrTalk(
        0x8,
        (
            "……嗯，那就这样吧。\x01",
            "关于那个遗迹与『星见之塔』，\x01",
            "我们这边也会进行调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD5")

    Jump("loc_1ACE")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF5")
    Call(0, 6)
    Jump("loc_B3B")

    label("loc_AF5")


    #C0005
    ChrTalk(
        0x8,
        (
            "能够召唤出『恶魔』的钟……\x01",
            "那个遗迹中居然还\x01",
            "存在着这种东西吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3B")

    Jump("loc_1ACE")

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF9")

    #C0006
    ChrTalk(
        0x8,
        "听说黑手党之间发生了斗争啊。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "没有将普通市民卷入，也算是万幸……\x01",
            "但这种行为实在是太愚蠢了……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "女神啊！请把人们从斗争\x01",
            "的因果循环中解放出来吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C5B")

    label("loc_BF9")


    #C0009
    ChrTalk(
        0x8,
        (
            "没有将无辜的市民卷入，\x01",
            "实在是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "女神啊！请把人们从斗争\x01",
            "的因果循环中解放出来吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5B")

    Jump("loc_1ACE")

    label("loc_C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D03")

    #C0011
    ChrTalk(
        0x8,
        (
            "……嗯……是错觉吗？\x01",
            "似乎从山道那边传来了钟声。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "奇怪，玛因兹那边\x01",
            "应该没有钟楼之类的地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        (
            "#0505F（……钟……？\x01",
            "　有点在意呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACE")

    label("loc_D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD9")

    #C0014
    ChrTalk(
        0x8,
        (
            "你们好像已经和\x01",
            "玛布尔修女谈过了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "……事情已经解决了吗？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0000F是、是的。\x01",
            "得到了贵重的情报，非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……那就好，\x01",
            "欢迎随时再来。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "空之女神啊，请引导他们吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E24")

    label("loc_DD9")


    #C0019
    ChrTalk(
        0x8,
        (
            "要是有什么烦恼，\x01",
            "欢迎随时前来拜访。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "空之女神啊，请引导他们吧……\x02",
    )

    CloseMessageWindow()

    label("loc_E24")

    Jump("loc_1ACE")

    label("loc_E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100D")

    #C0021
    ChrTalk(
        0x8,
        (
            "欢迎来到\x01",
            "克洛斯贝尔大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        (
            "#1110F……啊，长胡子老爷爷！\x01",
            "嘿嘿，我可以摸一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 500)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x153, 500)
    Sleep(1000)

    #C0023
    ChrTalk(
        0x8,
        "唔……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0011F等一下，琪、琪雅！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F2C")

    #C0025
    ChrTalk(
        0x102,
        (
            "#0103F真、真是十分抱歉，大主教。\x01",
            "这孩子太没礼貌了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9E")

    label("loc_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F73")

    #C0026
    ChrTalk(
        0x103,
        (
            "#0203F……失礼了。\x01",
            "请您原谅，她毕竟只是个小孩子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9E")

    label("loc_F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F9E")

    #C0027
    ChrTalk(
        0x104,
        "#0303F真、真对不起，大主教。\x02",
    )

    CloseMessageWindow()

    label("loc_F9E")


    #C0028
    ChrTalk(
        0x8,
        "哪里……不用介意。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "对于小孩子来说，\x01",
            "活泼有精神就是最好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "女神啊，请赐予这孩子祝福……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_105B")

    label("loc_100D")


    #C0031
    ChrTalk(
        0x8,
        "对于小孩子来说，活泼有精神就是最好的。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "女神啊，请赐予这孩子祝福……\x02",
    )

    CloseMessageWindow()

    label("loc_105B")

    Jump("loc_1ACE")

    label("loc_1060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_114F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1102")

    #C0033
    ChrTalk(
        0x8,
        (
            "好了……\x01",
            "今晚的弥撒结束之后，\x01",
            "创立纪念庆典的所有活动便将圆满落幕。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "今年也有很多人前来参加弥撒呢，\x01",
            "愿女神的祝福与他们同在……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_114A")

    label("loc_1102")


    #C0035
    ChrTalk(
        0x8,
        (
            "今年的纪念庆典\x01",
            "也来了很多参加弥撒的人。\x01",
            "愿女神的祝福与他们同在……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114A")

    Jump("loc_1ACE")

    label("loc_114F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1236")

    #C0036
    ChrTalk(
        0x8,
        (
            "有一个看起来像是帝国政府要员的男人\x01",
            "在深夜造访大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "似乎是看中了七耀教会的影响力，\x01",
            "想要拉拢\x01",
            "身为大主教的我……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        "我以严厉的呵斥将他赶了出去。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "身为空之女神仆人的我\x01",
            "必须要彻底保持中立。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_129C")

    label("loc_1236")


    #C0040
    ChrTalk(
        0x8,
        (
            "七耀教会在这片大陆上\x01",
            "得到了人们深厚的信仰。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "竟然想要将它利用于政治，\x01",
            "那简直是对女神的侮辱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_129C")

    Jump("loc_1ACE")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141B")

    #C0042
    ChrTalk(
        0x8,
        (
            "听说昨晚有人在旧城区\x01",
            "那边引起了很大的骚动。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "本来还以为只是旧城区的那些年轻人，\x01",
            "没想到竟然连游击士和警察也跟着\x01",
            "一起胡闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0005F（惊……！）\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "……嗯？果然是你们吗？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "虽然纪念庆典让人情绪高昂，\x01",
            "有时难免会失去冷静的判断力。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "但身为警察，可不能那样乱来啊。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0306F对、对不起……\x02\x03",

            "（这个老爷爷\x01",
            "　有种奇妙的压迫感啊……！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_148F")

    label("loc_141B")


    #C0049
    ChrTalk(
        0x8,
        (
            "……不过，在昨天的事件中\x01",
            "并没有人遭受重伤，\x01",
            "这可以算是不幸中的万幸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "你们以后务必要严于律己、谨慎行动。\x02",
    )

    CloseMessageWindow()

    label("loc_148F")

    Jump("loc_1ACE")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_15FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")

    #C0051
    ChrTalk(
        0x8,
        (
            "创立七十周年纪念吗？\x01",
            "想想的话，这段历史也不算短了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "痛苦与悲伤……\x01",
            "这个自治州也发生过很多事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "大家都会以自己的方式\x01",
            "来度过此次庆典吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "……唔，\x01",
            "我也不能满足于\x01",
            "只举行弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "还是回归初愿，\x01",
            "读读调配药剂的书吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15FA")

    label("loc_159D")


    #C0056
    ChrTalk(
        0x8,
        (
            "我也不能在这七十周年\x01",
            "的庆典中只顾着\x01",
            "举行弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "还是回归初愿，\x01",
            "读读调配药剂的书吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FA")

    Jump("loc_1ACE")

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_176F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_161D")
    Call(0, 42)
    Jump("loc_176A")

    label("loc_161D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1632")
    Call(0, 40)
    Jump("loc_176A")

    label("loc_1632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1702")

    #C0058
    ChrTalk(
        0x8,
        (
            "据说，在向空之女神祈祷时，\x01",
            "人们的心灵将会回归至最清净的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "进而从苦闷中解放出来，\x01",
            "闭上双眼，在黑暗中\x01",
            "获得一个重新审视自己的机会……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "……你们如果愿意的话，\x01",
            "也来参加弥撒吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_176A")

    label("loc_1702")


    #C0061
    ChrTalk(
        0x8,
        (
            "在向空之女神祈祷时，\x01",
            "人们的心灵将会回归最清净的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "……你们如果愿意的话，\x01",
            "也来参加弥撒吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176A")

    Jump("loc_1ACE")

    label("loc_176F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_178D")
    Call(0, 42)
    Jump("loc_189B")

    label("loc_178D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_17A2")
    Call(0, 40)
    Jump("loc_189B")

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")

    #C0063
    ChrTalk(
        0x8,
        (
            "今天将会在这个大圣堂中\x01",
            "举行弥撒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "空之女神守护着人们的生活，\x01",
            "赐予我们生命……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "为了让大家铭记女神的恩惠，\x01",
            "举办弥撒这样的活动是很有必要的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_189B")

    label("loc_184F")


    #C0066
    ChrTalk(
        0x8,
        (
            "今天将会在这个大圣堂里\x01",
            "举行弥撒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "你们也不要忘记\x01",
            "向女神感恩哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189B")

    Jump("loc_1ACE")

    label("loc_18A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_19F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_197A")

    #C0068
    ChrTalk(
        0x8,
        (
            "关于你们特别任务支援科的活动……\x01",
            "虽然只有少许，但我也有所耳闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "虽然世人都挪揄说\x01",
            "你们在模仿游击士……\x01",
            "但你们并没有必要介意。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "空之女神\x01",
            "绝对不会抛弃\x01",
            "贯彻正确的信念而行动的人们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19ED")

    label("loc_197A")


    #C0071
    ChrTalk(
        0x8,
        (
            "志愿帮助他人的人，\x01",
            "对于这个世界来说，可谓是一笔财富。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "空之女神\x01",
            "绝对不会抛弃\x01",
            "贯彻正确的信念而行动的人们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19ED")

    Jump("loc_1ACE")

    label("loc_19F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7F")

    #C0073
    ChrTalk(
        0x8,
        (
            "欢迎各位来到这所\x01",
            "克洛斯贝尔大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "看样子，你们似乎\x01",
            "准备进入山道啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "空之女神啊，请引导他们吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ACE")

    label("loc_1A7F")


    #C0076
    ChrTalk(
        0x8,
        (
            "七耀的教诲定会将你们\x01",
            "从迷茫中拯救出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "空之女神啊，请引导他们吧……\x02",
    )

    CloseMessageWindow()

    label("loc_1ACE")

    TalkEnd(0x8)
    Return()

    # Function_5_9A2 end

    def Function_6_1AD2(): pass

    label("Function_6_1AD2")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0x8, 0xE, 0)
    TurnDirection(0xE, 0x8, 0)

    #C0078
    ChrTalk(
        0xE,
        (
            "#0501F……这是有关遗迹内部的\x01",
            "调查报告书。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "呼唤出魔物的钟……\x01",
            "那座遗迹里面竟然有那样的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "………………………………………\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "确实，它很有可能\x01",
            "是古代遗物……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "嗯，感谢你提供这些情报。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xE,
        "#0500F是。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD4")

    #C0084
    ChrTalk(
        0x10A,
        (
            "#0604F警备队的诺艾尔上士吗……\x01",
            "听说她是一个恪守礼仪，并且很有才能的新星。\x02\x03",

            "#0602F……哼，你们也稍微\x01",
            "学习一下她的那股勤奋劲吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0310F（唔……\x01",
            "　阿缇，他明显是在攻击\x01",
            "　我们的软肋啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        (
            "#0211F（哪有……被攻击的\x01",
            "　只有兰迪前辈你一个人吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD4")

    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_6_1AD2 end

    def Function_7_1CE0(): pass

    label("Function_7_1CE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1D7F")

    #C0087
    ChrTalk(
        0xFE,
        (
            "今天早上，警备队的诺艾尔上士\x01",
            "把调查克洛斯贝尔遗迹\x01",
            "的报告书送来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "既然很有可能\x01",
            "与古代遗物有所关联……\x01",
            "那么教会也不可能坐视不理啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E02")

    #C0089
    ChrTalk(
        0xFE,
        (
            "……诺艾尔上士所说的那口钟\x01",
            "到底是个什么样的东西呢？\x01",
            "真让人在意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "而且，那口钟为什么会\x01",
            "突然响起来呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_1E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1E78")

    #C0091
    ChrTalk(
        0xFE,
        (
            "对于在市内发生的那起袭击事件，\x01",
            "艾拉尔达大主教感到十分痛心。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "因为大主教最厌恶\x01",
            "有违道德之事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_1E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1EFE")

    #C0093
    ChrTalk(
        0xFE,
        (
            "哈缇娜修女\x01",
            "今天要去给旧城区\x01",
            "的孩子们授课。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "因为旧城区的孩子们\x01",
            "几乎都不来主日学校，\x01",
            "所以我们才会主动派人过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_1EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1FF6")

    #C0095
    ChrTalk(
        0xFE,
        (
            "教会里传承的『法术』与\x01",
            "乌尔斯拉医院的近代医疗技术……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "两者所注重的领域分别为\x01",
            "精神的治愈与身体的诊疗，共同为人们带来福音。\x01",
            "但现阶段，这两者基本无法协同合作。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "这其中，也有近代医疗技术\x01",
            "尚处于发展之中，还未成熟的原因在内。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_209A")

    #C0098
    ChrTalk(
        0xFE,
        (
            "在纪念庆典结束后的这一周，\x01",
            "城市虽然和平……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "但有些市民似乎却\x01",
            "感到了某种紧张的气氛，\x01",
            "所以来教会进行祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "是不是发生什么事了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_209A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2119")

    #C0101
    ChrTalk(
        0xFE,
        (
            "今年也有很多人\x01",
            "来参加弥撒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "到了明年的纪念庆典，\x01",
            "希望他们还能保持着愉快明朗的心情，\x01",
            "再次造访这里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_2119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_215E")

    #C0103
    ChrTalk(
        0xFE,
        (
            "空之女神啊，请为迷途的羔羊们\x01",
            "指引正确的道路吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_215E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21E7")

    #C0104
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教在药剂调配领域\x01",
            "的成就十分卓越。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "乌尔斯拉医院的药\x01",
            "有许多都是以大主教从前\x01",
            "所调配的药剂为范本制作的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_21E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_22A9")

    #C0106
    ChrTalk(
        0xFE,
        (
            "庆典的第一天，为了祈祷纪念庆典能够成功，\x01",
            "麦克道尔市长与哈尔特曼议长\x01",
            "都来到了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "虽然两人一直都处于对立状态，\x01",
            "但为了克洛斯贝尔市的市民，\x01",
            "真希望他们两个能够携手合作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_22A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2360")

    #C0108
    ChrTalk(
        0xFE,
        (
            "哈罗德先生一家\x01",
            "经常拜访这所圣堂，\x01",
            "然后虔诚地祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "不忘却对空之女神的信仰……\x01",
            "这份诚心十分值得赞赏。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "伟大的空之女神啊，\x01",
            "请保佑虔诚的他们……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_238D")

    label("loc_2360")


    #C0111
    ChrTalk(
        0xFE,
        (
            "伟大的空之女神啊，\x01",
            "请保佑虔诚的他们……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238D")

    Jump("loc_2567")

    label("loc_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2438")

    #C0112
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的迪塔先生\x01",
            "来祈祷的时候，\x01",
            "总是开着巨大的高级轿车过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "虽然好几次都差点被撞到，\x01",
            "但只要一看到他面带爽朗笑容的道歉，\x01",
            "便觉得生不起气来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_2438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_24C2")

    #C0114
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市的\x01",
            "市长阁下有时候也会\x01",
            "拜访这所大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "似乎是趁着工作空闲的时候，\x01",
            "为了克洛斯贝尔市的和平\x01",
            "而来祈祷的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2567")

    label("loc_24C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2567")

    #C0116
    ChrTalk(
        0xFE,
        (
            "从很久很久以前的大崩坏\x01",
            "时代开始，七耀教会\x01",
            "就一直为人们带来光明。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "这所大圣堂也是七耀教会的设施之一……\x01",
            "空之女神肯定会为迷途的人们\x01",
            "指明正确的道路。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2567")

    TalkEnd(0xFE)
    Return()

    # Function_7_1CE0 end

    def Function_8_256B(): pass

    label("Function_8_256B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_26F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2665")

    #C0118
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教对\x01",
            "古代遗物的管理机关\x01",
            "『封圣省』很没有好感。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "因为据传闻说，隶属于封圣省的组织\x01",
            "『星杯骑士团』在暗地里进行了\x01",
            "许多肮脏的勾当。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "对于厌恶非法活动的\x01",
            "艾拉尔达大主教来说，\x01",
            "他们是绝对无法原谅的存在。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26F0")

    label("loc_2665")


    #C0121
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教对隶属于封圣省的组织\x01",
            "『星杯骑士团』很没有好感。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "对于厌恶非法活动的\x01",
            "艾拉尔达大主教来说，\x01",
            "他们是绝对无法原谅的存在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F0")

    Jump("loc_310E")

    label("loc_26F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2726")

    #C0123
    ChrTalk(
        0xFE,
        (
            "主日学校放假了哦，\x01",
            "好安静啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_2726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_27CD")

    #C0124
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教也对这次的事件\x01",
            "感到非常愤慨。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "虽然这次事件没有给市民带来伤害，\x01",
            "但仅仅出于争斗这样自私的理由\x01",
            "就让大家陷入不安，实在是无法原谅啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_27CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2889")

    #C0126
    ChrTalk(
        0xFE,
        (
            "教会的圣典中记载了\x01",
            "『恶魔』这种存在。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "传说，那是与女神相对的负面存在，\x01",
            "有时会利用人们心灵的弱点，\x01",
            "引诱他们做下恶事。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "对我们教会的人来说，\x01",
            "那确实是戒律的象征。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2922")

    #C0129
    ChrTalk(
        0xFE,
        (
            "玛布尔修女从很久以前开始\x01",
            "就在大圣堂工作了，\x01",
            "在七耀教会中有着很广的人脉。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "再加上她品行端方，\x01",
            "为了向她求助而前来拜访的人也不少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_2922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2974")

    #C0131
    ChrTalk(
        0xFE,
        (
            "嗯……为了让艾拉尔达大主教\x01",
            "能够安心工作，\x01",
            "我必须要努力支持他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_2974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A00")

    #C0132
    ChrTalk(
        0xFE,
        (
            "创立纪念庆典到今天就要结束了，\x01",
            "主日学校也会从明天重新开课。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "一想到可以再次见到那群孩子们，\x01",
            "就感觉突然充满了干劲呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_2A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2AD3")

    #C0134
    ChrTalk(
        0xFE,
        (
            "大主教这种职位，其发言\x01",
            "在七耀教会中也有着相当大的影响力。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "特别艾拉尔达大主教，\x01",
            "可是七耀教会的机关——典礼省\x01",
            "的高层人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "他绝对不会参与违法行为，\x01",
            "因此我们这些下属\x01",
            "都能放心的追随他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_2AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B56")

    #C0137
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的迪塔总裁\x01",
            "利用他雄厚的经济实力\x01",
            "进行着各种各样的慈善活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "作为教会的相关人员，\x01",
            "我实在是非常敬佩他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2C")

    #C0139
    ChrTalk(
        0xFE,
        (
            "经常来这所圣堂祈祷的\x01",
            "贸易商摩尔吉奥先生……\x01",
            "有点过于依赖女神了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "他把自己的成功\x01",
            "全部都归结于向女神献上了祈祷……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "但我觉得，将自己的努力\x01",
            "全部都归功于女神，\x01",
            "似乎也不太好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CBE")

    label("loc_2C2C")


    #C0142
    ChrTalk(
        0xFE,
        (
            "经常来这所圣堂祈祷的\x01",
            "贸易商摩尔吉奥先生……\x01",
            "有点过于依赖女神了。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "虽然由身为祭司的我来说有些不太合适，\x01",
            "但我觉得过于依赖女神\x01",
            "也不太好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBE")

    Jump("loc_310E")

    label("loc_2CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E9D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D3D")

    #C0144
    ChrTalk(
        0xA,
        (
            "嗯……希望那个羽扇豆草\x01",
            "能帮上医院的忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "我们七耀教会也对\x01",
            "乌尔斯拉医院抱有很大期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2DB5")

    #C0146
    ChrTalk(
        0xA,
        (
            "哎，虽然大主教有些顽固……\x01",
            "但却是一个明事理的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "对于拉格教授的实力，\x01",
            "大主教还是很认可的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2DB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_2DCA")
    Call(0, 41)
    Jump("loc_2E98")

    label("loc_2DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2E33")

    #C0148
    ChrTalk(
        0xA,
        "哎呀，有什么事情吗？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "这里是艾拉尔达大主教的办公室，\x01",
            "无关人员不能随便进入哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2E33")


    #C0150
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教\x01",
            "出版了好几本\x01",
            "有关七耀教会的书籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "读者都评价说书的内容\x01",
            "言简意赅，十分好懂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E98")

    Jump("loc_310E")

    label("loc_2E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F75")

    #C0152
    ChrTalk(
        0xFE,
        (
            "旧城区的不良团伙\x01",
            "是叫『剑蛇帮』跟\x01",
            "『圣书会』吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "特别是圣书会的孩子们，\x01",
            "打扮得简直就像是个\x01",
            "宗教团体。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "真是令人叹息啊。\x01",
            "如果可以的话，真希望他们能得到一个改过自新的机会呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FD2")

    label("loc_2F75")


    #C0155
    ChrTalk(
        0xFE,
        (
            "剑蛇帮还有\x01",
            "圣书会的孩子们……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "如果可以的话，真希望他们能得到一个改过自新的机会呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2FD2")

    Jump("loc_310E")

    label("loc_2FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_310E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308B")

    #C0157
    ChrTalk(
        0xFE,
        "艾拉尔达大主教是一个很严格的人。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "对有违道德的行为绝不姑息，\x01",
            "但对心存迷惘的人，\x01",
            "一定会温柔地伸出援助之手……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "作为祭司，\x01",
            "我真是十分憧憬他。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_310E")

    label("loc_308B")


    #C0160
    ChrTalk(
        0xFE,
        (
            "对有违道德的行为绝不姑息，\x01",
            "但对心存迷惘的人，\x01",
            "一定会温柔地伸出援助之手……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教就是那样的人，\x01",
            "真是让人憧憬啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310E")

    TalkEnd(0xFE)
    Return()

    # Function_8_256B end

    def Function_9_3112(): pass

    label("Function_9_3112")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3171")

    #C0162
    ChrTalk(
        0xFE,
        (
            "明天一大早\x01",
            "要去矿山镇玛因兹出差。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "希望孩子们\x01",
            "还像以前一样健康活泼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3947")

    label("loc_3171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3213")

    #C0164
    ChrTalk(
        0xFE,
        (
            "明天将要出差去矿山镇玛因兹，\x01",
            "进行主日学校的授课，\x01",
            "所以正在讨论上课的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "虽然出差很辛苦，\x01",
            "但可以见到平时看不到的孩子们，\x01",
            "很让人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3947")

    label("loc_3213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3283")

    #C0166
    ChrTalk(
        0xFE,
        (
            "今天来做礼拜的人数\x01",
            "似乎比平时多了不少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "由于港湾区的骚乱，\x01",
            "市里的人似乎也感到了不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3947")

    label("loc_3283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3291")
    Jump("loc_3947")

    label("loc_3291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_32EA")

    #C0168
    ChrTalk(
        0xFE,
        (
            "……看你们的样子，\x01",
            "应该是有些收获吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "呵呵，真不愧是玛布尔修女。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3947")

    label("loc_32EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3390")

    #C0170
    ChrTalk(
        0xFE,
        "遇到什么困难了吗？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "如果有什么烦恼的话，可以去\x01",
            "跟大主教或玛布尔修女\x01",
            "商量一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "那两位都长年\x01",
            "在教会工作，\x01",
            "一定能为你们提供一些有用的建议。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3947")

    label("loc_3390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_33F8")

    #C0173
    ChrTalk(
        0xFE,
        (
            "创立纪念庆典剩下的日子\x01",
            "就只有今天了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "空之女神啊，\x01",
            "请保佑庆典就这样顺利结束……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3947")

    label("loc_33F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349A")

    #C0175
    ChrTalk(
        0xFE,
        (
            "昨天真是吓了一大跳。\x01",
            "那个人竟然\x01",
            "对大主教提出了那种建议……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "笼罩在克洛斯贝尔自治州的黑暗，\x01",
            "说不定比预想中还要根深蒂固得多呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3512")

    label("loc_349A")


    #C0177
    ChrTalk(
        0xFE,
        (
            "竟然如此大胆，妄图拉拢\x01",
            "一个教区的大主教……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "笼罩在克洛斯贝尔自治州的黑暗，\x01",
            "说不定比预想中还要根深蒂固得多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3512")

    Jump("loc_3947")

    label("loc_3517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3592")

    #C0179
    ChrTalk(
        0xFE,
        (
            "久久修女虽然很冒失，\x01",
            "但十分擅长制作料理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "孩子们说不定就是被她做的曲奇\x01",
            "给吸引过来的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3947")

    label("loc_3592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3676")

    #C0181
    ChrTalk(
        0xFE,
        (
            "昨天是纪念庆典的第一天，\x01",
            "有很多人来参加弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "悼念曾在过去发生的数次战争中\x01",
            "不幸丧生的人们……\x01",
            "很多人正是抱着这种想法而来。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "以创立第七十周年为契机，\x01",
            "克洛斯贝尔自治州\x01",
            "到底会变成什么样呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3701")

    label("loc_3676")


    #C0184
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔居民的脑海中，\x01",
            "残留最深刻的大概还是有关战争的回忆吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "以创立第七十周年为契机，\x01",
            "克洛斯贝尔自治州\x01",
            "到底会变成什么样呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3701")

    Jump("loc_3947")

    label("loc_3706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3714")
    Jump("loc_3947")

    label("loc_3714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3803")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3799")

    #C0186
    ChrTalk(
        0xFE,
        (
            "在七耀教会的设施中，\x01",
            "开设了向孩子们传授知识的\x01",
            "『主日学校』。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "玛布尔修女今天\x01",
            "也在主日学校\x01",
            "授课。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_37FE")

    label("loc_3799")


    #C0188
    ChrTalk(
        0xFE,
        (
            "这所大圣堂的主日学校\x01",
            "从很久以前开始\x01",
            "就是由玛布尔修女负责的。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "我明天也要去\x01",
            "旧城区那边出差。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FE")

    Jump("loc_3947")

    label("loc_3803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D7")

    #C0190
    ChrTalk(
        0xFE,
        (
            "听说外面现在\x01",
            "正因为狼形魔兽的事件闹得沸沸扬扬。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "对很多人来说，魔兽本来就是不安的源头。\x01",
            "如果魔兽再袭击人的话，就更加令人惶恐了……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "希望之后不要再发生\x01",
            "更加严重的事件了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3947")

    label("loc_38D7")


    #C0193
    ChrTalk(
        0xFE,
        (
            "关于狼形魔兽所带来的受害情况……\x01",
            "听说已经有受伤的人员出现了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "希望之后不要再发生\x01",
            "更加严重的事件了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3947")

    TalkEnd(0xFE)
    Return()

    # Function_9_3112 end

    def Function_10_394B(): pass

    label("Function_10_394B")

    Call(0, 11)
    Return()

    # Function_10_394B end

    def Function_11_394F(): pass

    label("Function_11_394F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3968")
    Call(0, 38)
    Jump("loc_4963")

    label("loc_3968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A07")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_398A")
    Jump("loc_39FF")

    label("loc_398A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3998")
    Jump("loc_39FF")

    label("loc_3998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39A6")
    Jump("loc_39FF")

    label("loc_39A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_39B4")
    Jump("loc_39FF")

    label("loc_39B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_39C2")
    Jump("loc_39FF")

    label("loc_39C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_39D0")
    Jump("loc_39FF")

    label("loc_39D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_39DE")
    Jump("loc_39FF")

    label("loc_39DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_39F6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39FF")

    label("loc_39F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_39FF")

    label("loc_39FF")

    Call(0, 13)
    Jump("loc_4963")

    label("loc_3A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A92")

    #C0195
    ChrTalk(
        0xC,
        (
            "罗伊德、艾莉……\x01",
            "虽然很高兴能再次见到你们，\x01",
            "但我现在还在上课。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "如果你们不介意的话，\x01",
            "可以等到学校没课的时候再来吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4963")

    label("loc_3A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9E")

    #C0197
    ChrTalk(
        0xC,
        (
            "听说你们也协助\x01",
            "警备队参加了调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xC,
        (
            "呵呵，你们在各项工作中都表现得很活跃呢。\x01",
            "作为你们曾经的老师，我感到很自豪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        "下次在主日学校上课时，要不要炫耀一下呢～\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0006F哈哈……\x01",
            "老师，您就放过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        "#0113F老师您可真是的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C2C")

    label("loc_3B9E")


    #C0202
    ChrTalk(
        0xC,
        "呵呵，我真的很为你们感到自豪啊。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "我的学生罗伊德与艾莉\x01",
            "作为市民的模范而展现出了正义的一面……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xC,
        (
            "我觉得没有比这\x01",
            "更了不起的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2C")

    Jump("loc_4963")

    label("loc_3C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD9")
    OP_93(0xC, 0x10E, 0x0)

    #C0205
    ChrTalk(
        0xC,
        (
            "嗯……玛因兹那边\x01",
            "从以前开始就一直支撑着\x01",
            "克洛斯贝尔的经济。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xC,
        (
            "为了让年纪幼小的孩子们\x01",
            "也能为此感到自豪，\x01",
            "教他们学学历史如何呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D33")

    label("loc_3CD9")


    #C0207
    ChrTalk(
        0xC,
        (
            "哎呀，罗伊德、艾莉……\x01",
            "今天有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xC,
        (
            "现在还有些忙，\x01",
            "稍微晚点再过来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D33")

    Jump("loc_4963")

    label("loc_3D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EC0")

    #C0209
    ChrTalk(
        0xC,
        (
            "哎呀，罗伊德和艾莉……\x01",
            "发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xC,
        "你们的表情看起来好严肃……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#0008F……不，没什么事情。\x02\x03",

            "#0003F（在克洛斯贝尔市内\x01",
            "　发现了这种药片，\x01",
            "　这种事情实在是无法向老师开口啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        (
            "……总之，\x01",
            "不管发生什么事情，都要笑着面对哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "你们要是没有精神的话，\x01",
            "对特别任务支援科抱有期待的人们\x01",
            "也会陷入不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#0103F……说的对啊。\x01",
            "谢谢您，老师……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F32")

    label("loc_3EC0")


    #C0215
    ChrTalk(
        0xC,
        (
            "你们要是没有精神的话，\x01",
            "对特别任务支援科抱有期待的人们\x01",
            "也会陷入不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        "所以无论何时都不要忘记面带笑容。\x02",
    )

    CloseMessageWindow()

    label("loc_3F32")

    Jump("loc_4963")

    label("loc_3F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_41B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415F")
    OP_93(0xC, 0xB4, 0x0)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x0, 500)

    #C0217
    ChrTalk(
        0xC,
        "哎呀，罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xC,
        (
            "听说琪雅拒绝\x01",
            "住院接受检查？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#0006F是的……\x01",
            "对不起，难得您提出建议，\x01",
            "却浪费了您的一片心意……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "哎呀呀，没关系啦。\x01",
            "不能强迫小孩子做他们不想做的事情嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "以后总会有机会的，\x01",
            "再耐心观察一段时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        "#0100F说的也对……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x1B,
        (
            "玛布尔老师～\x01",
            "上课时可以说无关的话吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x1B, 500)

    #C0224
    ChrTalk(
        0xC,
        (
            "哎呀呀，\x01",
            "真对不起啊。\x01",
            "身为一名老师，竟然会……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x104,
        "#0305F喔喔，这……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x103,
        "#0200F真是妨碍到您了呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0227
    ChrTalk(
        0xC,
        (
            "（就是这样啦……\x01",
            "　等以后没课的时候，\x01",
            "　再来找我好好谈谈吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41B4")

    label("loc_415F")

    OP_93(0xC, 0xB4, 0x0)

    #C0228
    ChrTalk(
        0xC,
        (
            "那个……\x01",
            "刚才讲到哪里了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xC,
        (
            "呵呵，上了年纪之后，\x01",
            "人就变得健忘了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B4")

    Jump("loc_4963")

    label("loc_41B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_43DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_42C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_42BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425E")

    #C0230
    ChrTalk(
        0xC,
        (
            "辛苦了，罗伊德，\x01",
            "今天真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "小琪雅，\x01",
            "如果愿意的话，\x01",
            "欢迎再来主日学校哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x153,
        "#1109F嗯！　知道啦～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42B7")

    label("loc_425E")


    #C0233
    ChrTalk(
        0xC,
        (
            "小琪雅。\x01",
            "如果愿意的话，以后\x01",
            "也要来主日学校哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        (
            "其他的孩子们\x01",
            "肯定也会欢迎你的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42B7")

    Jump("loc_42BF")

    label("loc_42BC")

    Call(0, 43)

    label("loc_42BF")

    Jump("loc_43D6")

    label("loc_42C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437C")

    #C0235
    ChrTalk(
        0xC,
        (
            "以我的『法术』，想要唤起\x01",
            "琪雅更深层的记忆，\x01",
            "恐怕就有点困难了……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "圣乌尔斯拉医院\x01",
            "『神经科』的医生，\x01",
            "或许会对这方面有更加详细的了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        "去找他们谈一下吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43D6")

    label("loc_437C")


    #C0238
    ChrTalk(
        0xC,
        (
            "如果去圣乌尔斯拉医院，\x01",
            "或许能了解到有关\x01",
            "琪雅记忆的详细情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xC,
        "去找他们谈一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_43D6")

    Jump("loc_4963")

    label("loc_43DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_43EC")
    Call(0, 38)
    Jump("loc_4963")

    label("loc_43EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_44D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4462")

    #C0240
    ChrTalk(
        0xC,
        "我正在思考从明天起的教学内容。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xC,
        (
            "嗯……我想，教他们外国的风俗人情\x01",
            "也许会很有趣呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44D2")

    label("loc_4462")


    #C0242
    ChrTalk(
        0xC,
        (
            "教他们外国的风俗人情\x01",
            "也许会很有趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "虽然同样位于塞姆里亚大陆，\x01",
            "但各个国家之间的文化差异是相当大的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D2")

    Jump("loc_4963")

    label("loc_44D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_455F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F2")
    Call(0, 12)
    Jump("loc_455A")

    label("loc_44F2")


    #C0244
    ChrTalk(
        0xC,
        (
            "呵呵，主日学校今天明明放假，\x01",
            "却特意来找我……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "我当讲师已经很久了，\x01",
            "每个时代的孩子都很可爱呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_455A")

    Jump("loc_4963")

    label("loc_455F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_45F5")

    #C0246
    ChrTalk(
        0xC,
        (
            "在主日学校放假的时候，\x01",
            "我会考虑下次上课\x01",
            "的授课内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "但在休息日，\x01",
            "偶尔也会有孩子\x01",
            "来这里玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        "呵呵，比想象中的要热闹呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4963")

    label("loc_45F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4650")

    #C0249
    ChrTalk(
        0xC,
        "呵呵，有没有好好地享受纪念庆典呢？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        (
            "你们要是有空的话，\x01",
            "也去祈祷吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4963")

    label("loc_4650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471E")

    #C0251
    ChrTalk(
        0xC,
        (
            "最近会定期安排主日学校的\x01",
            "讲师去大圣堂外出差。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "住在阿尔摩利卡村、矿山镇玛因兹\x01",
            "还有旧城区的孩子们\x01",
            "很难有机会来上课。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "哈缇娜修女最近\x01",
            "也在协助我工作，\x01",
            "真是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_477C")

    label("loc_471E")


    #C0254
    ChrTalk(
        0xC,
        (
            "哈缇娜修女今天\x01",
            "会代替我去旧城区那边出差。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        (
            "那边的孩子很少来主日学校，\x01",
            "情况很棘手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477C")

    Jump("loc_4963")

    label("loc_4781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4897")
    OP_93(0xC, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482A")

    #C0256
    ChrTalk(
        0xC,
        "据说，因为很久以前发生的『大崩坏』……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        (
            "这片塞姆里亚大陆\x01",
            "遭到了毁灭。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "当时拥有先进技术的\x01",
            "古代塞姆里亚文明\x01",
            "也随之消亡了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4892")

    label("loc_482A")


    #C0259
    ChrTalk(
        0xC,
        (
            "『大崩坏』，正如其名，\x01",
            "它毁灭了塞姆里亚大陆……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "──呼，不知道这些孩子们\x01",
            "有没有认真听我讲课。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4892")

    Jump("loc_4963")

    label("loc_4897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490F")

    #C0261
    ChrTalk(
        0xC,
        (
            "我现在也担任\x01",
            "着主日学校的\x01",
            "教师一职。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "如果愿意的话，有时间的时候\x01",
            "就来看看我上课吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4963")

    label("loc_490F")


    #C0263
    ChrTalk(
        0xC,
        (
            "现在的孩子们\x01",
            "也都非常可爱。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "如果愿意的话，有时间的时候\x01",
            "就来看看我上课吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4963")

    TalkEnd(0xC)
    Return()

    # Function_11_394F end

    def Function_12_4967(): pass

    label("Function_12_4967")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_93(0xC, 0xB4, 0x0)
    TurnDirection(0xF, 0xC, 0)
    TurnDirection(0x10, 0xC, 0)

    #C0265
    ChrTalk(
        0xF,
        "我们打算稍后去逛街。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xF,
        (
            "有很多小店都开张了，\x01",
            "似乎很有趣的样子，修女也一起去吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "哎呀呀，\x01",
            "那还真是让人羡慕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        "但我忙着举行弥撒，不能去呢。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xC,
        "大家玩得开心点吧。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xF,
        "哎，这样啊……\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x10,
        "唔唔，好遗憾啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_12_4967 end

    def Function_13_4A7D(): pass

    label("Function_13_4A7D")

    EventBegin(0x0)
    Fade(500)
    OP_68(150650, 1700, 16780, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 149440, 200, 17150, 90)
    SetChrPos(0x102, 149390, 200, 15890, 45)
    SetChrPos(0x103, 148500, 200, 17170, 90)
    SetChrPos(0x104, 149330, 200, 18150, 135)
    OP_93(0xC, 0xB4, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BC8")
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(500)

    #C0272
    ChrTalk(
        0xC,
        "哎呀，是哪位呢？\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0000F#5P啊，不好意思。\x01",
            "看到你们上课的情景，\x01",
            "总觉得有些怀念……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        (
            "#0105F（……哎？\x01",
            "　这位修女，似乎曾在哪里……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1F")

    label("loc_4BC8")


    #C0275
    ChrTalk(
        0x102,
        (
            "#0105F（……哎？\x01",
            "　这位修女，似乎曾在哪里……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_4C1F")


    #C0276
    ChrTalk(
        0xC,
        (
            "……啊……\x01",
            "你难道是……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "──罗伊德。\x01",
            "是罗伊德·班宁斯吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x101,
        "#0005F#5P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#0300F什么啊，罗伊德，你们认识吗？\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#0002F#5P难、难道是……\x01",
            "玛布尔老师！？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        "真是好久不见了，罗伊德。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    #C0282
    ChrTalk(
        0xC,
        (
            "还有……\x01",
            "那边的是艾莉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        (
            "呵呵……你们两个\x01",
            "都长大成人了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#0109F果然……！\x01",
            "好久不见了，老师。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0285
    ChrTalk(
        0x101,
        (
            "#0000F#11P那个……莫非\x01",
            "艾莉你也认识玛布尔老师？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0286
    ChrTalk(
        0x102,
        (
            "#0102F嗯，我在主日学校上课时，\x01",
            "也是受教于老师的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0287
    ChrTalk(
        0x103,
        (
            "#0205F#5P罗伊德前辈与艾莉前辈\x01",
            "的年龄不是很接近吗……\x02\x03",

            "而且同样受教于修女，\x01",
            "但当时却互不相识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔市是很广阔的，\x01",
            "不同街区的孩子，来主日学校\x01",
            "上课的日程也不一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        (
            "罗伊德与艾莉来学校\x01",
            "的日子就是不同的。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        "#0300F原来～如此。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#0104F……感觉有点奇怪呢。\x02\x03",

            "#0102F要不是上课时间不同的话，\x01",
            "当年或许还能成为童年玩伴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#0009F#11P哈哈，说得也是啊。\x02",
    )

    CloseMessageWindow()

    def lambda_4F61():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F61)
    Sleep(50)

    def lambda_4F71():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F71)

    def lambda_4F7E():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F7E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0293
    ChrTalk(
        0x101,
        (
            "#0002F#5P说起来，玛布尔老师您\x01",
            "居然还记得我们啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xC,
        (
            "呵呵……\x01",
            "只要是自己教过的学生，\x01",
            "我一个都不会忘记的。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "而且你们两个\x01",
            "又都是非常有个性的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#0205F#5P有个性……吗？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        "没错。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "罗伊德是个喜欢粘着姐姐，\x01",
            "很爱撒娇的孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        (
            "艾莉小时候则非常不像个小孩子，\x01",
            "该说是对男女之间的事很早熟吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#0011F#5P等、等一下！？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        "#0112F老师……！\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x104,
        (
            "#0304F哈哈～\x01",
            "听别人过去的事情真是有趣啊。\x02\x03",

            "#0309F那么，具体来说，究竟发生过怎样的小故事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xC,
        "对了，比如──\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#0012F#5P老师，请您放过我吧……！\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#0113F真是的。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        "呵呵，开玩笑啦。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        "#0206F#5P……真遗憾。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "……罗伊德、艾莉，\x01",
            "能与你们再会，\x01",
            "我感到很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "如果愿意的话，随时\x01",
            "欢迎你们来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#0002F#5P……好的！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 149440, 200, 17150, 90)
    SetScenarioFlags(0x8C, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5281")
    SetScenarioFlags(0x0, 4)

    label("loc_5281")

    EventEnd(0x5)
    Return()

    # Function_13_4A7D end

    def Function_14_5284(): pass

    label("Function_14_5284")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5318")
    Jump("loc_5362")

    label("loc_5318")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5338")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5362")

    label("loc_5338")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5358")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5362")

    label("loc_5358")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5362")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_53ED")

    #C0311
    ChrTalk(
        0xFE,
        (
            "……那位夫人，\x01",
            "好像经常在圣堂露面。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "虔诚是非常重要的，\x01",
            "我也不能忘记那份诚心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_53ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5432")

    #C0313
    ChrTalk(
        0xFE,
        (
            "哎呀……我还是第一次看见\x01",
            "警备队的人来到大圣堂呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_5432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_54C3")

    #C0314
    ChrTalk(
        0xFE,
        (
            "该死的黑手党……\x01",
            "竟然在那一带开战，\x01",
            "真是无法无天……！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "女神啊……保护我们这些热心做生意的人\x01",
            "免遭那些凶恶毒牙的伤害吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_54C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5565")

    #C0316
    ChrTalk(
        0xFE,
        (
            "我想把从玛因兹\x01",
            "订购的七耀石\x01",
            "作为下次交易的重头戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "虽然贩卖新商品\x01",
            "总让我感觉有点不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "不过没什么，空之女神肯定\x01",
            "会对我展露笑颜的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_5565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_55A9")

    #C0319
    ChrTalk(
        0xFE,
        (
            "空之女神啊……\x01",
            "明年的纪念庆典\x01",
            "也请多保佑我……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_55A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5637")

    #C0320
    ChrTalk(
        0xFE,
        (
            "我在今年的纪念庆典\x01",
            "获得了很大的收益呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "因为游客的数量\x01",
            "比往年多了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "向空之女神\x01",
            "虔诚地祈祷，\x01",
            "果然没有白费啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_5637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_56BA")

    #C0323
    ChrTalk(
        0xFE,
        (
            "今天是庆典的最后一天了……\x01",
            "很多客人都去了米修拉姆，\x01",
            "现在正是做生意的良机。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "空之女神啊……\x01",
            "请给我带来商机！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_56BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5720")

    #C0325
    ChrTalk(
        0xFE,
        (
            "空之女神啊……\x01",
            "今年的业绩真是超好啊，\x01",
            "商品卖得飞快。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "啊啊，真是感激不尽……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_5720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_577C")

    #C0327
    ChrTalk(
        0xFE,
        (
            "空之女神啊……\x01",
            "昨天的销售额\x01",
            "也非常可观。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        "啊啊，实在是太感谢了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_577C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_58B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584A")

    #C0329
    ChrTalk(
        0xFE,
        (
            "虽然工作很忙……\x01",
            "但我也不打算错过弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "因为，全靠平时坚持\x01",
            "向空之女神献上祈祷，\x01",
            "才能有今天的我。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "所以，像这样的活动，\x01",
            "我一次都不会错过，\x01",
            "这样才能表达我的感激之情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_58B1")

    label("loc_584A")


    #C0332
    ChrTalk(
        0xFE,
        "我现在的成就全都是空之女神所赐……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "所以必须要一次不漏的参加这样的活动，\x01",
            "这也是理所当然的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58B1")

    Jump("loc_5B91")

    label("loc_58B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_59A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5963")

    #C0334
    ChrTalk(
        0xFE,
        "下个月终于要到创立纪念庆典了……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "对我们贸易商来说，\x01",
            "这是赚钱的大好时机。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "好了，为了今年也能生意兴隆，\x01",
            "必须要向空之女神献上祈祷……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_599F")

    label("loc_5963")


    #C0337
    ChrTalk(
        0xFE,
        (
            "空之女神啊……\x01",
            "在这次的创立纪念庆典期间\x01",
            "也请保佑我……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_599F")

    Jump("loc_5B91")

    label("loc_59A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A60")

    #C0338
    ChrTalk(
        0xFE,
        "嗯嗯，有孩子们在的话就很热闹呢，真好啊。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        "虽然我以前最讨厌小孩子了……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "但自从在这里坚持祈祷，事业大获成功之后，\x01",
            "便感觉自己的心胸也变得宽阔起来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5ACA")

    label("loc_5A60")


    #C0341
    ChrTalk(
        0xFE,
        (
            "通过向空之女神祈祷，\x01",
            "我的事业获得了成功，心胸也变得宽阔起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "必须要感谢这个地方呢。\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ACA")

    Jump("loc_5B91")

    label("loc_5ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B57")

    #C0343
    ChrTalk(
        0xFE,
        (
            "我是一个贸易商……\x01",
            "自从在这里祈祷之后，\x01",
            "生意就取得了很大的成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "自那之后，我就经常\x01",
            "来这里祈祷了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5B91")

    label("loc_5B57")


    #C0345
    ChrTalk(
        0xFE,
        (
            "啊啊，空之女神啊……\x01",
            "请保佑我下次生意\x01",
            "也一帆风顺……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B91")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_5284 end

    def Function_15_5B99(): pass

    label("Function_15_5B99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5C3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BB7")
    Call(0, 6)
    Jump("loc_5C3E")

    label("loc_5BB7")


    #C0346
    ChrTalk(
        0xE,
        (
            "#0502F啊，支援科的各位……\x02\x03",

            "#0504F我刚才已经向大主教\x01",
            "报告了有关那处\x01",
            "遗迹的情况。\x02\x03",

            "#0508F如果调查工作可以因此\x01",
            "而取得进展就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C3E")

    TalkEnd(0xFE)
    Return()

    # Function_15_5B99 end

    def Function_16_5C42(): pass

    label("Function_16_5C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5C50")
    Jump("loc_607C")

    label("loc_5C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5C5E")
    Jump("loc_607C")

    label("loc_5C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5C6C")
    Jump("loc_607C")

    label("loc_5C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5C7A")
    Jump("loc_607C")

    label("loc_5C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5E46")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D17")
    Jump("loc_5D61")

    label("loc_5D17")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D37")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D61")

    label("loc_5D37")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D57")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D61")

    label("loc_5D57")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D61")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5DF2")

    #C0347
    ChrTalk(
        0xFE,
        (
            "哼，还以为\x01",
            "上了刚才的课，\x01",
            "就不用再上普通的课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "修女对这种事情\x01",
            "真是从不敷衍啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E3A")

    label("loc_5DF2")


    #C0349
    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "我完全忘了\x01",
            "主日学校今天有课。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        "啊啊～真想去外面玩啊～\x02",
    )

    CloseMessageWindow()

    label("loc_5E3A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_607C")

    label("loc_5E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5E54")
    Jump("loc_607C")

    label("loc_5E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5ED3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E72")
    Call(0, 12)
    Jump("loc_5ECB")

    label("loc_5E72")


    #C0351
    ChrTalk(
        0xFE,
        (
            "啧……\x01",
            "难得我想带老师去\x01",
            "参观城市的。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "因为总是跟哈米尔在一起，\x01",
            "都没有新鲜感了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ECB")

    TalkEnd(0xFE)
    Jump("loc_607C")

    label("loc_5ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EE1")
    Jump("loc_607C")

    label("loc_5EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5EEF")
    Jump("loc_607C")

    label("loc_5EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5EFD")
    Jump("loc_607C")

    label("loc_5EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6073")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F9A")
    Jump("loc_5FE4")

    label("loc_5F9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5FBA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FE4")

    label("loc_5FBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FDA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FE4")

    label("loc_5FDA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FE4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601B")
    Call(0, 18)
    Jump("loc_6067")

    label("loc_601B")


    #C0353
    ChrTalk(
        0xFE,
        (
            "哼，哈米尔那家伙，\x01",
            "只不过是学习成绩比我稍微强一点，\x01",
            "就那么得意忘形……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6067")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_607C")

    label("loc_6073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_607C")

    label("loc_607C")

    Return()

    # Function_16_5C42 end

    def Function_17_607D(): pass

    label("Function_17_607D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_608B")
    Jump("loc_651A")

    label("loc_608B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6099")
    Jump("loc_651A")

    label("loc_6099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_60A7")
    Jump("loc_651A")

    label("loc_60A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_60B5")
    Jump("loc_651A")

    label("loc_60B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_62A2")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6152")
    Jump("loc_619C")

    label("loc_6152")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6172")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_619C")

    label("loc_6172")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6192")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_619C")

    label("loc_6192")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_619C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6224")

    #C0354
    ChrTalk(
        0xFE,
        (
            "真是的～塔米尔这家伙，\x01",
            "明明刚才都还\x01",
            "那么得意忘形。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "节制很重要，要节制。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6296")

    label("loc_6224")

    SetChrSubChip(0xFE, 0x2)

    #C0356
    ChrTalk(
        0xFE,
        (
            "真是的～塔米尔这家伙\x01",
            "直到刚才不是还\x01",
            "一直都在玩吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "修女不是\x01",
            "一直都教导我们说，\x01",
            "节制是很重要的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6296")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_651A")

    label("loc_62A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_62B0")
    Jump("loc_651A")

    label("loc_62B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6355")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62CE")
    Call(0, 12)
    Jump("loc_634D")

    label("loc_62CE")


    #C0358
    ChrTalk(
        0xFE,
        (
            "虽然很想和经常照顾我们的玛布尔老师\x01",
            "一起去逛逛露天店……\x01",
            "但老师太忙，那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "本来还想请\x01",
            "老师吃冰激凌什么的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_634D")

    TalkEnd(0xFE)
    Jump("loc_651A")

    label("loc_6355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6363")
    Jump("loc_651A")

    label("loc_6363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6371")
    Jump("loc_651A")

    label("loc_6371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_637F")
    Jump("loc_651A")

    label("loc_637F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A0")
    TalkBegin(0xFE)
    Call(0, 18)
    TalkEnd(0xFE)
    Jump("loc_650C")

    label("loc_63A0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6434")
    Jump("loc_647E")

    label("loc_6434")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6454")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_647E")

    label("loc_6454")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6474")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_647E")

    label("loc_6474")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_647E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0360
    ChrTalk(
        0xFE,
        (
            "我的双胞胎兄弟塔米尔，\x01",
            "学习完全不行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "只是比较擅长运动的话，\x01",
            "在主日学校可没资格骄傲。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_650C")

    Jump("loc_651A")

    label("loc_6511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_651A")

    label("loc_651A")

    Return()

    # Function_17_607D end

    def Function_18_651B(): pass

    label("Function_18_651B")

    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x10, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_65AF")
    Jump("loc_65F9")

    label("loc_65AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_65CF")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65F9")

    label("loc_65CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65EF")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65F9")

    label("loc_65EF")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65F9")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0362
    ChrTalk(
        0xF,
        (
            "我说，哈米尔。\x01",
            "你听明白玛布尔老师讲的东西了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x10)
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0xF, 0)
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66E7")
    Jump("loc_6731")

    label("loc_66E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6707")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6731")

    label("loc_6707")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6727")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6731")

    label("loc_6727")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6731")

    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    #C0363
    ChrTalk(
        0x10,
        (
            "塔米尔，你有没有在认真听啊？\x01",
            "并不是那么难的内容啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "是、是吗……？\x01",
            "嗯，那等一下把笔记借给我看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_18_651B end

    def Function_19_67CE(): pass

    label("Function_19_67CE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6862")
    Jump("loc_68AC")

    label("loc_6862")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6882")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68AC")

    label("loc_6882")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68AC")

    label("loc_68A2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68AC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6985")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6938")

    #C0365
    ChrTalk(
        0xFE,
        (
            "刚才的课……\x01",
            "虽然有点难，\x01",
            "但是很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "那个……\x01",
            "谢谢了，大哥哥。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6980")

    label("loc_6938")


    #C0367
    ChrTalk(
        0xFE,
        (
            "能够与隆和亨利\x01",
            "一起学习，\x01",
            "真开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "今天的课会教些什么呢……\x02",
    )

    CloseMessageWindow()

    label("loc_6980")

    Jump("loc_69CE")

    label("loc_6985")


    #C0369
    ChrTalk(
        0xFE,
        (
            "大崩坏……\x01",
            "原来还发生过那样的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        "好可怕啊……（发抖）……\x02",
    )

    CloseMessageWindow()

    label("loc_69CE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_67CE end

    def Function_20_69D6(): pass

    label("Function_20_69D6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A6A")
    Jump("loc_6AB4")

    label("loc_6A6A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A8A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AB4")

    label("loc_6A8A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AAA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AB4")

    label("loc_6AAA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AB4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B75")

    #C0371
    ChrTalk(
        0xFE,
        (
            "塞姆里亚文明……\x01",
            "似乎是我爸爸\x01",
            "很喜欢的话题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "……说起来，隆与亨利\x01",
            "今天逃学了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "明明已经告诉过他们\x01",
            "主日学校今天有课了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BAA")

    label("loc_6B75")


    #C0374
    ChrTalk(
        0xFE,
        (
            "……算了，不管那两个家伙了，\x01",
            "要抓紧时间学习啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BAA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_69D6 end

    def Function_21_6BB2(): pass

    label("Function_21_6BB2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C46")
    Jump("loc_6C90")

    label("loc_6C46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C66")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C90")

    label("loc_6C66")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C86")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C90")

    label("loc_6C86")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C90")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0375
    ChrTalk(
        0xFE,
        (
            "如果导力器就像这样\x01",
            "继续发展下去的话，\x01",
            "生活大概会变得更加便捷吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "比如说，待在家里\x01",
            "就能购物之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "……啊！要是变成那样的话，\x01",
            "帮家里买东西赚到的零钱就没有了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_6BB2 end

    def Function_22_6D6D(): pass

    label("Function_22_6D6D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E01")
    Jump("loc_6E4B")

    label("loc_6E01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E4B")

    label("loc_6E21")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E41")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E4B")

    label("loc_6E41")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E4B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0378
    ChrTalk(
        0xFE,
        (
            "当上游击士的话，\x01",
            "就可以从爱普斯泰恩财团那里\x01",
            "得到战术导力器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "真好啊～\x01",
            "有朝一日，我也想使用\x01",
            "那些华丽的魔法。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_6D6D end

    def Function_23_6EF0(): pass

    label("Function_23_6EF0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F84")
    Jump("loc_6FCE")

    label("loc_6F84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6FA4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FCE")

    label("loc_6FA4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FC4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FCE")

    label("loc_6FC4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FCE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7001")
    Jump("loc_70C2")

    label("loc_7001")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7072")

    #C0380
    ChrTalk(
        0xFE,
        (
            "我对警察并不是\x01",
            "很了解，\x01",
            "所以在这堂课上真是学到了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "以后还请再多教我们一些东西哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_70C2")

    label("loc_7072")


    #C0382
    ChrTalk(
        0xFE,
        (
            "啊，你是刚才的……\x01",
            "是叫小琪雅吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "你也来\x01",
            "上课了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x153,
        "#1106F嗯～？\x02",
    )

    CloseMessageWindow()

    label("loc_70C2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_6EF0 end

    def Function_24_70CA(): pass

    label("Function_24_70CA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_715E")
    Jump("loc_71A8")

    label("loc_715E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_717E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71A8")

    label("loc_717E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_719E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71A8")

    label("loc_719E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71A8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0385
    ChrTalk(
        0xFE,
        (
            "我记得，爱普斯泰恩财团好像就是以\x01",
            "Ｃ·爱普斯泰恩博士的\x01",
            "庞大遗产为基础发展起来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "爱普斯泰恩博士到底\x01",
            "是个怎样的人呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_70CA end

    def Function_25_7258(): pass

    label("Function_25_7258")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72EC")
    Jump("loc_7336")

    label("loc_72EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_730C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7336")

    label("loc_730C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_732C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7336")

    label("loc_732C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7336")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D9")

    #C0387
    ChrTalk(
        0xFE,
        (
            "太简单了，简直让人发笑。\x01",
            "这种程度的知识是常识啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "……啊，居然在上课时随便\x01",
            "和别人搭话，真没礼貌！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_73FE")

    label("loc_73D9")


    #C0389
    ChrTalk(
        0xFE,
        (
            "真是的，到那边去！\x01",
            "我要学习啦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73FE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_7258 end

    def Function_26_7406(): pass

    label("Function_26_7406")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_749A")
    Jump("loc_74E4")

    label("loc_749A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_74BA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74E4")

    label("loc_74BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74E4")

    label("loc_74DA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_74E4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0390
    ChrTalk(
        0xFE,
        (
            "以现在的技术水平来说，\x01",
            "不是能够轻松避免\x01",
            "那种严重的灾难吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_7406 end

    def Function_27_7551(): pass

    label("Function_27_7551")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75E5")
    Jump("loc_762F")

    label("loc_75E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7605")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_762F")

    label("loc_7605")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7625")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_762F")

    label("loc_7625")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_762F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0391
    ChrTalk(
        0xFE,
        (
            "……啊！\x01",
            "别看我的笔记啦！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_7551 end

    def Function_28_767B(): pass

    label("Function_28_767B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_770F")
    Jump("loc_7759")

    label("loc_770F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_772F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7759")

    label("loc_772F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_774F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7759")

    label("loc_774F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7759")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0392
    ChrTalk(
        0xFE,
        "呼～……只要一学习就想睡觉。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "……哇，修女在看着呢，\x01",
            "必须得打起精神。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_767B end

    def Function_29_77D5(): pass

    label("Function_29_77D5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7869")
    Jump("loc_78B3")

    label("loc_7869")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7889")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_78B3")

    label("loc_7889")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78A9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_78B3")

    label("loc_78A9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78B3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0394
    ChrTalk(
        0xFE,
        (
            "为了将来，\x01",
            "必须要好好学习，\x01",
            "妈妈是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "……大哥哥，你们以前\x01",
            "有没有好好学习呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_77D5 end

    def Function_30_793F(): pass

    label("Function_30_793F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79D3")
    Jump("loc_7A1D")

    label("loc_79D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A1D")

    label("loc_79F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A13")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A1D")

    label("loc_7A13")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A1D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 7)), scpexpr(EXPR_END)), "loc_7BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7ADE")

    #C0396
    ChrTalk(
        0x1D,
        (
            "#3600F我一般都会注意时间，\x01",
            "尽量来参加的……\x01",
            "但经常会由于工作原因而无法赶过来。\x02\x03",

            "#3603F老是给妻子增添负担。\x01",
            "……我也真是没用呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BDA")

    label("loc_7ADE")


    #C0397
    ChrTalk(
        0x1D,
        (
            "#3600F参加弥撒是\x01",
            "妻子的习惯。\x01",
            "她每周都会来，从未缺席过。\x02\x03",

            "#3603F我一般都会注意时间，\x01",
            "尽量来参加的……\x01",
            "但经常会由于工作原因而无法赶过来。\x02\x03",

            "#3600F哈哈，总是给妻子\x01",
            "增添负担。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#0005F（……………………？\x01",
            "　难道有什么必须\x01",
            "　来祈祷的理由吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_7BDA")

    Jump("loc_7E79")

    label("loc_7BDF")


    #C0399
    ChrTalk(
        0x1D,
        (
            "#3605F啊，各位……\x02\x03",

            "#3609F哈哈哈，竟会在这种地方相遇，还真巧啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        "#0000F对了，今天是举行弥撒的日子啊。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#0100F哈罗德先生也是来祈祷的吗？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x1D,
        (
            "#3600F嗯，这是妻子的习惯。\x02\x03",

            "#3609F虽然我经常缺席……\x01",
            "但也会尽量抽时间\x01",
            "陪妻子过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x104,
        "#0309F还是一如既往地关心家人呢～\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x103,
        "#0200F在百忙之中还抽空前来，真是十分虔诚呢。\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x1D,
        (
            "#3609F哈哈，并不是那样的……\x02\x03",

            "#3608F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0406
    ChrTalk(
        0x1D,
        (
            "#3603F……不，没什么。\x02\x03",

            "#3600F那个，其实我并没有\x01",
            "那么深厚的信仰。\x02\x03",

            "只是听说祈祷\x01",
            "对保佑生意兴隆很有效。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        "#0305F哎呀，是听那边那位说的吗？\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x1D,
        "#3609F啊哈哈哈哈……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 7)

    label("loc_7E79")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_793F end

    def Function_31_7E81(): pass

    label("Function_31_7E81")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F15")
    Jump("loc_7F5F")

    label("loc_7F15")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7F35")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F5F")

    label("loc_7F35")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F55")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F5F")

    label("loc_7F55")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F5F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0x1E, 0x0)

    #C0409
    ChrTalk(
        0x1E,
        (
            "#3700F祭司大人，那么今天\x01",
            "也拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_7E81 end

    def Function_32_7FBB(): pass

    label("Function_32_7FBB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_804F")
    Jump("loc_8099")

    label("loc_804F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_806F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8099")

    label("loc_806F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_808F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8099")

    label("loc_808F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8099")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8107")

    #C0410
    ChrTalk(
        0x1F,
        (
            "#3809F祈祷～祈祷～……\x02\x03",

            "跟爸爸妈妈\x01",
            "在一起好开心啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8185")

    label("loc_8107")


    #C0411
    ChrTalk(
        0x1F,
        (
            "#3800F今天是我和妈妈\x01",
            "来祈祷的日子～\x02\x03",

            "那个，结果爸爸\x01",
            "也赶过来了！\x02\x03",

            "#3809F爸爸总是很忙，\x01",
            "这次也是匆匆忙忙的跑过来的～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_8185")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_7FBB end

    def Function_33_818D(): pass

    label("Function_33_818D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A4")

    #C0412
    ChrTalk(
        0x102,
        "#0105F啊……是塞茜尔小姐的母亲。\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "哎呀呀，大家聚在一起，\x01",
            "莫非是来祈祷的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)

    #C0414
    ChrTalk(
        0xFE,
        "罗伊德……发生什么事情了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0415
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        "……没什么，我只是随便问问。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "呵呵，你真是\x01",
            "越来越像盖伊了，\x01",
            "在黄昏时很容易看错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#0011F啊，哈哈……\x01",
            "再怎么说，也是有血缘关系的兄弟嘛。\x01",
            "（……怎么，原来阿姨是来为大哥祈祷的吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "要是方便的话，\x01",
            "罗伊德也一起来祈祷吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "因为盖伊也……沉睡\x01",
            "在这里呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_842B")

    label("loc_83A4")


    #C0421
    ChrTalk(
        0xFE,
        (
            "罗伊德真是\x01",
            "越来越像盖伊了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "呵呵……你一定能够成为不输给\x01",
            "盖伊的优秀搜查官。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "阿姨我会替你加油的。\x01",
            "可不能输哦，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_842B")

    TalkEnd(0xFE)
    Return()

    # Function_33_818D end

    def Function_34_842F(): pass

    label("Function_34_842F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84C3")
    Jump("loc_850D")

    label("loc_84C3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_84E3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_850D")

    label("loc_84E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8503")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_850D")

    label("loc_8503")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_850D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8581")

    #C0424
    ChrTalk(
        0xFE,
        (
            "大哥哥讲的课\x01",
            "好有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "我还会再去找蔡特\x01",
            "一起玩的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85D0")

    label("loc_8581")


    #C0426
    ChrTalk(
        0xFE,
        (
            "哼，老实说，\x01",
            "学习真是让人提不起劲来～\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        "不过，修女的课其实挺有意思的。\x02",
    )

    CloseMessageWindow()

    label("loc_85D0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_842F end

    def Function_35_85D8(): pass

    label("Function_35_85D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8657")

    #C0428
    ChrTalk(
        0xFE,
        "我是来向女神祈祷旅途平安的。\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "要是不小心受伤的话，\x01",
            "难得的旅行也就泡汤了。\x01",
            "必须得十分小心才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_86B4")

    label("loc_8657")


    #C0430
    ChrTalk(
        0xFE,
        (
            "要是不小心受伤，\x01",
            "浪费了旅行的时光，\x01",
            "可就太不划算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "以防万一，\x01",
            "再祈祷一次好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B4")

    TalkEnd(0xFE)
    Return()

    # Function_35_85D8 end

    def Function_36_86B8(): pass

    label("Function_36_86B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(151810, 1500, 11060, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31350, 0)
    SetChrPos(0x101, 148350, 0, 3500, 0)
    SetChrPos(0x102, 146900, 0, 3750, 0)
    SetChrPos(0x103, 148350, 0, 1920, 0)
    SetChrPos(0x104, 146900, 0, 2250, 0)
    OP_4B(0xC, 0xFF)
    OP_68(151810, 1500, 13060, 5000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0432
    ChrTalk(
        0xC,
        "──据说，很久以前发生的『大崩坏』……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "将这片塞姆里亚大陆\x01",
            "彻底毁灭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xC,
        (
            "在当时拥有先进技术的\x01",
            "古代塞姆里亚文明\x01",
            "也随之消失了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(147550, 1500, 2910, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    OP_0D()

    #C0435
    ChrTalk(
        0x102,
        "#0100F……看样子，主日学校正在上课呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_8891")

    #C0436
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，真让人怀念啊。\x01",
            "而且孩子们当中也有我们认识的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_890A")

    label("loc_8891")


    #C0437
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，真让人怀念啊。\x01",
            "而且孩子们当中也有我们认识的呢……\x02\x03",

            "#0005F（……嗯？\x01",
            "　正在授课的修女……\x01",
            "　莫非是……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_890A")

    SetChrPos(0x0, 147550, 0, 2900, 0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x86, 4)
    EventEnd(0x5)
    Return()

    # Function_36_86B8 end

    def Function_37_8925(): pass

    label("Function_37_8925")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(151810, 1500, 11060, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31350, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89D8")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8994")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, 149460, 0, 1750, 0)

    label("loc_8994")

    SetChrPos(0x101, 148350, 0, 3500, 0)
    SetChrPos(0x102, 146900, 0, 3750, 0)
    SetChrPos(0x103, 148350, 0, 1920, 0)
    SetChrPos(0x104, 146900, 0, 2250, 0)

    label("loc_89D8")

    OP_4B(0xC, 0xFF)
    OP_68(151810, 1500, 13060, 5000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0438
    ChrTalk(
        0xC,
        (
            "──半世纪前，\x01",
            "Ｃ·爱普斯泰恩博士\x01",
            "发起了『导力革命』……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xC,
        (
            "虽然一开始并不被人们所接受，\x01",
            "但在如今，我们周围\x01",
            "已经有了很多便利的『导力器』。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xC,
        (
            "例如最近出现的导力车，\x01",
            "便利的产品接二连三地被发明了出来……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B7C")
    Fade(500)
    OP_68(147550, 1500, 2910, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    OP_0D()

    #C0441
    ChrTalk(
        0x102,
        (
            "#0100F……主日学校\x01",
            "好像正在上课呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，真让人怀念呢。\x01",
            "而且孩子们当中也有我们认识的呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B7C")

    SetChrPos(0x0, 147550, 0, 2900, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BA7")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_8BA7")

    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x86, 5)
    EventEnd(0x5)
    Return()

    # Function_37_8925 end

    def Function_38_8BB1(): pass

    label("Function_38_8BB1")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50381.itc", 0x1E)
    LoadEffect(0x0, "event\\ev400_00.eff")
    LoadEffect(0x1, "event\\ev401_00.eff")
    SoundLoad(840)
    OP_4B(0xC, 0xFF)
    SetChrPos(0xC, 148920, 0, 13890, 90)
    SetChrPos(0x101, 150330, 0, 14130, 270)
    SetChrPos(0x153, 151460, 0, 13520, 270)
    SetChrPos(0xEF, 150640, 0, 12780, 315)
    FadeToBright(1000, 0)
    OP_68(150000, 1100, 14000, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8D0F")

    #C0443
    ChrTalk(
        0xC,
        (
            "#5P哎呀……\x01",
            "罗伊德，还有艾莉。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#0002F#11P下午好，玛布尔老师。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x102,
        "#0102F#6P在您百忙之中还来打扰，真不好意思。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D79")

    label("loc_8D0F")


    #C0446
    ChrTalk(
        0xC,
        (
            "#5P哎呀……\x01",
            "这不是罗伊德嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x101,
        (
            "#0002F#11P下午好，玛布尔老师。\x02\x03",

            "在您百忙之中还来打扰，真不好意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D79")


    #C0448
    ChrTalk(
        0xC,
        (
            "#5P呵呵，没关系啦，\x01",
            "现在刚好是休息时间。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EC6")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0449
    ChrTalk(
        0xC,
        (
            "#5P说起来，你们似乎\x01",
            "是同一个部门的同事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xC,
        (
            "#5P呵呵，看到你们两个在一起，\x01",
            "总觉得感慨万千啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        "#0012F#11P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        "#0112F#6P是、是那样的吗？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        (
            "#5P呵呵……\x01",
            "那么，你们来此有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xC,
        (
            "#5P今天是来做礼拜的吗？\x01",
            "还是来扫墓的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EF4")

    label("loc_8EC6")


    #C0455
    ChrTalk(
        0xC,
        (
            "#5P你们是来做礼拜的吗，\x01",
            "还是来扫墓的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EF4")


    #C0456
    ChrTalk(
        0x101,
        "#0008F#11P不，实际上……\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x153,
        (
            "#1100F#12P喂喂，罗伊德。\x02\x03",

            "这个人是修女吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0458
    ChrTalk(
        0xC,
        "#5P哎呀，这个孩子是……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#0003F#11P那个，实际上……\x02\x03",

            "#0001F我们想找您谈一谈\x01",
            "关于这个孩子的一些事情。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_68(151000, 1100, 12500, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0xC, 151000, 0, 13800, 180)
    SetChrPos(0x153, 151000, 0, 12000, 0)
    SetChrPos(0x101, 151500, 0, 10800, 0)
    SetChrPos(0xEF, 150500, 0, 10800, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0460
    ChrTalk(
        0xC,
        "#11P……是吗，原来发生了那种事啊。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xC,
        (
            "#11P啊，女神啊……\x01",
            "请赐予迷途的羔羊光明与幸福。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "#11P感谢您指引\x01",
            "他们相遇……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        "#0000F#6P玛布尔老师……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9145")

    #C0464
    ChrTalk(
        0x102,
        (
            "#0104F#6P……确实，能与她相遇，\x01",
            "说不定都是因为女神的指引呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91DE")

    label("loc_9145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9193")

    #C0465
    ChrTalk(
        0x103,
        (
            "#0204F#6P……确实，能与她相遇，\x01",
            "说不定都是因为某种指引呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91DE")

    label("loc_9193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_91DE")

    #C0466
    ChrTalk(
        0x104,
        (
            "#0304F#6P……确实，能与她相遇，\x01",
            "说不定都是因为女神的指引啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91DE")


    #C0467
    ChrTalk(
        0x153,
        "#1105F#6P咦咦～……？\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "#11P总之……\x01",
            "你们是来商量关于这个\x01",
            "孩子失去记忆的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xC,
        (
            "#11P听你所言，她除了名字之外\x01",
            "什么都不记得……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#0006F#6P嗯……是这样的。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x153,
        (
            "#1106F#6P那个，虽然琪雅\x01",
            "试着努力想过了。\x02\x03",

            "#1108F但好像完全想不起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        "#11P是吗……真是个好孩子哦。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xC)

    #C0473
    ChrTalk(
        0xC,
        (
            "#11P……教会中的确传承着\x01",
            "关于心灵与精神\x01",
            "领域的知识和技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xC,
        (
            "#11P而且……\x01",
            "也有失忆症状的治疗方法。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0475
    ChrTalk(
        0x101,
        "#0002F#6P那、那么……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_940D")

    #C0476
    ChrTalk(
        0x102,
        (
            "#0100F#6P您有办法找回\x01",
            "这个孩子的记忆吗……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9490")

    label("loc_940D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_944F")

    #C0477
    ChrTalk(
        0x103,
        (
            "#0202F#6P您有办法恢复\x01",
            "这个孩子的记忆吗……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9490")

    label("loc_944F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9490")

    #C0478
    ChrTalk(
        0x104,
        (
            "#0300F#6P也就是说，这个孩子的记忆\x01",
            "可以找回来吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9490")


    #C0479
    ChrTalk(
        0xC,
        (
            "#11P虽然不能断言，\x01",
            "但应该值得一试。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        (
            "#11P时间并不充裕呢……\x01",
            "立即来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0481
    ChrTalk(
        0x101,
        (
            "#0005F#6P莫非……\x01",
            "由老师您亲自帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xC,
        (
            "#11P嗯，我也算是\x01",
            "学过一些东西吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xC,
        (
            "#11P就是在教会中传承的，\x01",
            "有关心灵与精神的『法术』。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        "#0001F#6P『法术』……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9602")

    #C0485
    ChrTalk(
        0x102,
        (
            "#0101F#6P在教会圣职者中传承的，\x01",
            "与祈祷和圣礼相关的技术……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9695")

    label("loc_9602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_964A")

    #C0486
    ChrTalk(
        0x103,
        (
            "#0201F#6P那是不依靠导力器，\x01",
            "仅凭祈祷所引发的魔法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9695")

    label("loc_964A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9695")

    #C0487
    ChrTalk(
        0x104,
        (
            "#0301F#6P传闻说，只有教会人员才能\x01",
            "使用的不可思议的祈祷术吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9695")


    #C0488
    ChrTalk(
        0xC,
        (
            "#11P嗯，本来有个组织是专门\x01",
            "研究那些技术的……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xC,
        (
            "#11P但很不巧，\x01",
            "那方面的专家很少来克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0490
    ChrTalk(
        0x101,
        "#0005F#6P专家吗……？\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xC,
        (
            "#11P……虽然不便公开提起，\x01",
            "但教会中也是有很多内幕的。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        (
            "#11P那个组织隶属于\x01",
            "被称为『封圣省』的机关……\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xC,
        (
            "#11P管理这座大圣堂的\x01",
            "艾拉尔达大主教似乎非常讨厌\x01",
            "那个组织所进行的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xC,
        (
            "#11P因此，那些专家很少有机会\x01",
            "来克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        (
            "#0006F#6P感、感觉有很多\x01",
            "复杂的背景呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9945")

    #C0496
    ChrTalk(
        0x102,
        (
            "#0103F#6P隶属于『封圣省』的组织……\x01",
            "也就是『星杯骑士团』吧。\x02\x03",

            "#0108F虽然听说过艾拉尔达大主教\x01",
            "是偏向『典礼省』的教会高层人士，\x01",
            "但没想到竟然还有那种内情啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xC,
        (
            "#11P呵呵，真不愧是艾莉，\x01",
            "对这类情况很了解呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99FC")

    label("loc_9945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_99A5")

    #C0498
    ChrTalk(
        0x103,
        (
            "#0201F#6P也就是说，这是教会\x01",
            "内部的权利斗争吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        "#11P嗯，真让人惭愧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_99FC")

    label("loc_99A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_99FC")

    #C0500
    ChrTalk(
        0x104,
        (
            "#0301F#6P也就是说，是教会\x01",
            "内部的权利斗争吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xC,
        "#11P嗯，真让人惭愧……\x02",
    )

    CloseMessageWindow()

    label("loc_99FC")


    #C0502
    ChrTalk(
        0xC,
        (
            "#11P不过，我所使用的法术\x01",
            "与他们使用的并没有什么两样。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        "#11P我想还是值得一试的。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        (
            "#0000F#6P知道了，\x01",
            "那就拜托您了。\x02\x03",

            "#0005F那个，是不是换个地方\x01",
            "比较好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xC,
        "#11P不，在这里就可以了。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "#11P你是叫琪雅吧，\x01",
            "可以到我这里来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x153,
        "#1109F#6P好呀～！\x02",
    )

    CloseMessageWindow()
    OP_68(151110, 1100, 12960, 1000)

    def lambda_9B18():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9B18)
    WaitChrThread(0x153, 1)
    Sleep(500)

    #C0508
    ChrTalk(
        0xC,
        (
            "#11P请闭上眼睛，\x01",
            "慢慢深呼吸。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x153,
        (
            "#1110F#5P嗯！\x02\x03",

            "#1103F#40W呼……哈……\x02\x03",

            "#40W呼……哈……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xC,
        "#11P嗯，这样就行了。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xC,
        "#11P……那么……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Fade(500)
    SetCameraDistance(23500, 0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x10)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sound(882, 0, 100, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)

    #C0512
    ChrTalk(
        0xC,
        (
            "#11P#40W──以空之女神之名，\x01",
            "祝圣之七耀，于此处显现。\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0xC, 0x40, 200, 900, -450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(893, 0, 100, 0)
    Sound(840, 2, 100, 0)
    SetCameraDistance(23000, 30000)
    Sleep(1000)

    #C0513
    ChrTalk(
        0x101,
        "#0005F#6P（啊……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9CC5")

    #C0514
    ChrTalk(
        0x102,
        "#0105F#6P（这就是法术……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D22")

    label("loc_9CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9CF6")

    #C0515
    ChrTalk(
        0x103,
        "#0201F#6P（这就是法术吗……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D22")

    label("loc_9CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9D22")

    #C0516
    ChrTalk(
        0x104,
        "#0301F#6P（这就是法术啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_9D22")


    #C0517
    ChrTalk(
        0xC,
        "#11P#40W空之金耀，识之银耀──\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xC,
        (
            "#11P#40W以此融合为契，\x01",
            "请为其明示\x01",
            "缺失碎片之所在吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x1, 0x1, 0x153, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(228, 0, 100, 0)
    Sleep(500)

    def lambda_9DCA():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_9DCA)
    Sleep(800)

    #C0519
    ChrTalk(
        0x153,
        "#1105F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        "#0013F#6P琪雅……！？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x10)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Sleep(300)

    #C0521
    ChrTalk(
        0xC,
        "#11P没关系，不必担心。\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xC,
        "#11P……感觉如何，琪雅。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xC,
        "#11P想起什么了吗？\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x153,
        (
            "#1103F#5P#40W嗯……\x02\x03",

            "#40W………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)

    #C0525
    ChrTalk(
        0x153,
        (
            "#1108F#5P……感觉，\x01",
            "脑袋里面浮现出了\x01",
            "一个又黑暗又广阔的地方。\x02\x03",

            "#1112F上面有朦胧的光线洒下来，\x01",
            "虽然很漂亮，但感觉又有点恐怖。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        "#0005F#6P又黑暗又广阔的地方……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9FA1")

    #C0527
    ChrTalk(
        0x102,
        "#0108F#6P那是哪里呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FFA")

    label("loc_9FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9FD0")

    #C0528
    ChrTalk(
        0x103,
        "#0208F#6P指的是哪里呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FFA")

    label("loc_9FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9FFA")

    #C0529
    ChrTalk(
        0x104,
        "#0301F#6P到底是哪里啊……？\x02",
    )

    CloseMessageWindow()

    label("loc_9FFA")


    #C0530
    ChrTalk(
        0xC,
        (
            "#11P除了那个场景之外，\x01",
            "还想起了别的什么吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "#11P比如家人是谁，\x01",
            "住在什么地方之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x153,
        "#1106F#5P唔……那些完全没想起来。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xC,
        "#11P这样啊……\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xC,
        "#11P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    StopBGM(0xFA0)
    BeginChrThread(0x22, 1, 0, 39)
    StopEffect(0x1, 0x2)
    Sleep(3000)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    EndChrThread(0x22, 0x1)

    #C0535
    ChrTalk(
        0x101,
        "#0001F#6P那个，玛布尔老师？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7124", 0)
    OP_64(0xC)
    Sleep(500)

    #C0536
    ChrTalk(
        0xC,
        (
            "#11P……看样子，使用法术的话，\x01",
            "做到这点就已经是极限了。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xC,
        (
            "#11P心理暗示所能唤起的记忆\x01",
            "就只有这么多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xC,
        (
            "#11P或许……\x01",
            "是神经系统\x01",
            "出了什么问题也说不定。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        "#0005F#6P神经系统的问题……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A20F")

    #C0540
    ChrTalk(
        0x102,
        "#0101F#6P这、这是怎么一回事呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A272")

    label("loc_A20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A246")

    #C0541
    ChrTalk(
        0x103,
        "#0201F#6P请问，那是怎么一回事……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A272")

    label("loc_A246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A272")

    #C0542
    ChrTalk(
        0x104,
        "#0301F#6P那是怎么回事啊……？\x02",
    )

    CloseMessageWindow()

    label("loc_A272")


    #C0543
    ChrTalk(
        0xC,
        (
            "#11P……简单来说，\x01",
            "就是有关脑神经的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xC,
        (
            "#11P出于某种原因，\x01",
            "掌管记忆功能的神经指令\x01",
            "传达受到了阻碍……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xC,
        "#11P这种可能性也是有的。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        (
            "#0011F#6P怎、怎么会……\x02\x03",

            "#0007F那样的话……\x01",
            "难道就束手无策了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xC,
        "#11P这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xC,
        (
            "#11P教会中传承的法术\x01",
            "是关于心灵与精神领域的……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xC,
        (
            "#11P说不定，\x01",
            "近代医学技术更加适合\x01",
            "解决这个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        "#0005F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A414")

    #C0551
    ChrTalk(
        0x102,
        "#0105F#6P近代医学的话，也就是说……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A47D")

    label("loc_A414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A449")

    #C0552
    ChrTalk(
        0x103,
        "#0205F#6P近代医学的话，也就是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A47D")

    label("loc_A449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A47D")

    #C0553
    ChrTalk(
        0x104,
        "#0305F#6P说起近代医学的话，也就是……\x02",
    )

    CloseMessageWindow()

    label("loc_A47D")


    #C0554
    ChrTalk(
        0xC,
        "#11P没错，就是圣乌尔斯拉医科大学。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xC,
        (
            "#11P虽然近代医学\x01",
            "对于心灵与精神领域的研究\x01",
            "至今还不够充分……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xC,
        (
            "#11P但在几年前，那里成立了\x01",
            "一个名为『神经科』的新部门，\x01",
            "听说那里拥有十分优秀的研究者。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xC,
        (
            "#11P你们去那里寻求帮助的话，\x01",
            "说不定会寻找到不同于教会的解决途径。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        (
            "#0000F#6P『神经科』吗……\x01",
            "（咦，似乎在什么地方听到过。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A61A")

    #C0559
    ChrTalk(
        0x102,
        (
            "#0103F#6P我说，罗伊德……\x02\x03",

            "#0101F我们应该去找\x01",
            "那里的人谈谈吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6AF")

    label("loc_A61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A66C")

    #C0560
    ChrTalk(
        0x103,
        (
            "#0203F#6P罗伊德前辈……\x02\x03",

            "#0201F我们还是应该\x01",
            "去那边商量一下吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6AF")

    label("loc_A66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A6AF")

    #C0561
    ChrTalk(
        0x104,
        (
            "#0303F#6P喂，罗伊德。\x02\x03",

            "#0300F我们应该\x01",
            "去那边看看吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6AF")


    #C0562
    ChrTalk(
        0x101,
        (
            "#0003F#6P嗯，说得也是呢……\x02\x03",

            "#0002F──老师，\x01",
            "谢谢您了。\x02\x03",

            "我们立刻就去乌尔斯拉\x01",
            "医院看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xC,
        "#11P嗯，那就好。\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xC,
        (
            "#11P……真不好意思，\x01",
            "没能帮上什么忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#0005F#6P没、没那回事！\x01",
            "您都告诉我们有关神经科的事了。\x02\x03",

            "#0000F还有……\x01",
            "琪雅回想起来的那个场景\x01",
            "应该也会成为相关线索。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A802")

    #C0566
    ChrTalk(
        0x102,
        "#0103F#6P『又黑暗又广阔的地方』啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A86F")

    label("loc_A802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A83B")

    #C0567
    ChrTalk(
        0x103,
        "#0203F#6P『又黑暗又广阔的地方』么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A86F")

    label("loc_A83B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A86F")

    #C0568
    ChrTalk(
        0x104,
        "#0303F#6P『又黑暗又广阔的地方』吗……\x02",
    )

    CloseMessageWindow()

    label("loc_A86F")

    OP_93(0x153, 0xB4, 0x1F4)

    #C0569
    ChrTalk(
        0x153,
        (
            "#1103F#11P嗯，而且上面还有\x01",
            "朦胧的光线照射下来。\x02\x03",

            "#1112F还有嗡嗡嗡嗡的声音……\x01",
            "那地方虽然很漂亮，但是感觉有点可怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        "#0003F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xC,
        (
            "#11P听上去……\x01",
            "确实不是普通的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xC,
        "#11P愿你们得到女神的祝福。\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xC,
        (
            "#11P我也会祈祷琪雅的问题\x01",
            "能有一个好的结果。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(23250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    SetChrPos(0x0, 150800, 0, 14000, 180)
    SetChrPos(0xC, 150800, 200, 17500, 180)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xA8, 2)
    SetScenarioFlags(0x8C, 3)
    OP_29(0x48, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_38_8BB1 end

    def Function_39_A9DB(): pass

    label("Function_39_A9DB")

    OP_25(0x348, 0x5A)
    Sleep(100)
    OP_25(0x348, 0x50)
    Sleep(100)
    OP_25(0x348, 0x46)
    Sleep(100)
    OP_25(0x348, 0x3C)
    Sleep(100)
    OP_25(0x348, 0x32)
    Sleep(100)
    OP_25(0x348, 0x28)
    Sleep(100)
    OP_25(0x348, 0x1E)
    Sleep(100)
    OP_25(0x348, 0x14)
    Sleep(100)
    OP_25(0x348, 0xA)
    Sleep(100)
    OP_24(0x348)
    Return()

    # Function_39_A9DB end

    def Function_40_AA1E(): pass

    label("Function_40_AA1E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2780, 2290, 22200, 0)
    MoveCamera(319, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28080, 0)
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x101, 2500, 500, 22500, 270)
    SetChrPos(0x102, 2500, 500, 24000, 270)
    SetChrPos(0x103, 4000, 500, 22500, 270)
    SetChrPos(0x104, 4000, 500, 24000, 270)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0574
    ChrTalk(
        0x8,
        (
            "#5P欢迎来到这所\x01",
            "克洛斯贝尔大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x8,
        "#5P今天有什么事情呢？\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        (
            "#12P#0000F您就是艾拉尔达大主教吧？\x02\x03",

            "我们是警察局·特别任务支援科的人，\x01",
            "今天是因为工作上的事情来拜访您的。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x8,
        "#5P唔？是工作吗？\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x102,
        (
            "#12P#0100F我们接到了乌尔斯拉医院\x01",
            "内科教授拉格先生的委托。\x02\x03",

            "来这里领取一种叫做『羽扇豆草』的药材，\x01",
            "关于此事，他事先好像已经联络过您了吧？\x02\x03",

            "#0103F教授由于工作繁忙，\x01",
            "所以才委托我们代他过来，\x01",
            "找您领取那种药草……\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x8,
        "#5P……稍等一下。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0580
    ChrTalk(
        0x8,
        "#5P拉格……你刚才说的是拉格教授吧？\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x8,
        (
            "#5P嗯，之前确实\x01",
            "收到过他的来信……\x01",
            "但关于此事，我还是第一次听说。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x104,
        "#11P#0305F……啊？\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x8,
        "#5P原因很简单。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x8,
        (
            "#5P因为拉格教授的来信，\x01",
            "我是一封也不会看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#12P#0005F咦……咦咦！？\x02\x03",

            "您、您为什么不……\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x8,
        (
            "#5P不为什么。\x01",
            "关于这件事，\x01",
            "我已经向女神发过誓了。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x104,
        "#11P#0305F（喂，罗伊德，这样的话……）\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x103,
        (
            "#12P#0203F（……这二人的关系\x01",
            "　似乎很麻烦呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        "#12P#0106F（真令人头痛呢……）\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#12P#0003F（但、但是我们已经接下了这项委托……\x01",
            "　总得想办法完成啊。）\x02\x03",

            "#0001F那、那个……\x01",
            "艾拉尔达大主教。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x8,
        "#5P……什么事？\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#12P#0001F拉格教授委托我们领取的药草，\x01",
            "据说是要用于内科研究的。\x02\x03",

            "我想，以乌尔斯拉医院的研究条件，\x01",
            "将来肯定可以让\x01",
            "那种药草帮助到更多的病人。\x02\x03",

            "#0008F那个……我并不准备打听\x01",
            "您与拉格教授之间有什么过节。\x02\x03",

            "#0003F只是，无论如何，\x01",
            "也想请您将『羽扇豆草』交给\x01",
            "拉格教授，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x8,
        (
            "#5P……你是不是\x01",
            "误会了什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x8,
        (
            "#5P我并没说过\x01",
            "不把药草交给你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x101,
        "#12P#0005F……咦？\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x8,
        (
            "#5P……『羽扇豆草』的话，\x01",
            "就在我的办公室里，在大圣堂左侧的最里面。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x8,
        (
            "#5P跟伦顿祭司说\x01",
            "已经得到了我的许可，\x01",
            "他就会给你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x8,
        (
            "#5P……好了，话说完了。\x01",
            "你们快点走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x101,
        (
            "#12P#0005F那、那个……\x01",
            "谢谢您……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2750, 2490, 2009, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27740, 1000)
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x101, -500, 500, 7500, 180)
    SetChrPos(0x102, 1000, 500, 7500, 180)
    SetChrPos(0x103, -500, 500, 9000, 180)
    SetChrPos(0x104, 1000, 500, 9000, 180)

    def lambda_B1FE():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1FE)

    def lambda_B218():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B218)

    def lambda_B232():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B232)

    def lambda_B24C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B24C)
    Sleep(500)
    SetCameraDistance(26740, 0)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_B28C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B28C)

    def lambda_B299():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B299)

    def lambda_B2A6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B2A6)

    def lambda_B2B3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B2B3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0601
    ChrTalk(
        0x101,
        "#5P#0003F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x104,
        (
            "#12P#0300F总觉得\x01",
            "说服的过程太轻松了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x102,
        (
            "#12P#0100F与其说是被罗伊德说服了，\x01",
            "倒不如说是\x01",
            "大主教自愿交给我们的……\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x103,
        (
            "#11P#0200F虽然不是很明白……\x02\x03",

            "但趁着大主教还没有\x01",
            "改变主意，还是赶快\x01",
            "去拿药草为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        (
            "#5P#0003F说得也是。\x02\x03",

            "#0000F那个……应该是左侧里面的办公室，\x01",
            "我们去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1900, 2490, 2430, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(22000, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0x0, -500, 0, 3500, 180)
    SetChrPos(0x1, -500, 0, 3500, 180)
    SetChrPos(0x2, -500, 0, 3500, 180)
    SetChrPos(0x3, -500, 0, 3500, 180)
    OP_29(0x13, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_AA1E end

    def Function_41_B499(): pass

    label("Function_41_B499")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(97580, 1200, 7510, 0)
    MoveCamera(314, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27740, 0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrPos(0x101, 98000, 0, 7000, 270)
    SetChrPos(0x102, 98000, 0, 8300, 270)
    SetChrPos(0x103, 99300, 500, 7000, 270)
    SetChrPos(0x104, 99300, 500, 8300, 270)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0606
    ChrTalk(
        0xA,
        "#5P哎呀，有什么事情吗？\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xA,
        (
            "#5P这里是艾拉尔达大主教的办公室，\x01",
            "无关人员不能随便进入哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个，我们是\x01",
            "警察局·特别任务支援科的人……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0609
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将前来领取『羽扇豆草』的事情\x01",
            "做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0610
    ChrTalk(
        0xA,
        (
            "#5P……哦，原来如此，\x01",
            "是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xA,
        (
            "#5P你们已经获得大主教的许可了吧？\x01",
            "那么，请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(98390, 1500, 8960, 4000)
    OP_93(0xA, 0x0, 0x1F4)

    def lambda_B67D():
        OP_95(0xFE, 96000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B67D)
    WaitChrThread(0xA, 1)

    def lambda_B69B():
        OP_95(0xFE, 100000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B69B)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    OP_68(97580, 1500, 7510, 4000)
    OP_93(0xA, 0x10E, 0x1F4)

    def lambda_B6FF():
        OP_95(0xFE, 96000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B6FF)
    WaitChrThread(0xA, 1)

    def lambda_B71D():
        OP_95(0xFE, 96000, 0, 7830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B71D)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)

    #C0612
    ChrTalk(
        0xA,
        "#5P好了，这就是『羽扇豆草』。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('选秀活动特别奖纪念盾', 1)

    #C0614
    ChrTalk(
        0xA,
        (
            "#5P羽扇豆（Ｌｕｐｉｎｕｓ）在古语中\x01",
            "是『狼』的意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xA,
        (
            "#5P据说是很久以前由神狼赠与人类，\x01",
            "拥有悠久历史的药草。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xA,
        (
            "#5P过去，似乎在克洛斯贝尔市附近\x01",
            "就能采集到，但由于城市开发的影响，\x01",
            "其数量正在逐渐减少……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x102,
        (
            "#12P#0100F我小时候好像\x01",
            "也听外公说过\x01",
            "同样的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        (
            "#12P#0005F这样啊……\x02\x03",

            "#0003F但是……大主教为什么\x01",
            "愿意把如此贵重的药草\x01",
            "交给我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x104,
        (
            "#12P#0306F真让人难以理解啊。\x01",
            "大主教好像很讨厌\x01",
            "拉格教授。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x103,
        (
            "#12P#0200F大主教如此讨厌教授的理由\x01",
            "也让人觉得有些在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xA,
        (
            "#5P哦，那个啊。\x01",
            "……唉，那也是没有办法的。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xA,
        (
            "#5P乌尔斯拉医院的拉格教授\x01",
            "原来是这所大圣堂\x01",
            "的见习祭司。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0623
    ChrTalk(
        0x101,
        "#12P#0005F医院的医生以前竟然是祭司……？\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xA,
        "#5P没什么可奇怪的。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0xA,
        (
            "#5P虽说是先进医疗技术，\x01",
            "但内科与七耀教会的研究领域\x01",
            "非常相近。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x103,
        (
            "#12P#0200F确实，七耀教会中\x01",
            "也在进行着关于药剂调配的研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x102,
        (
            "#12P#0105F但是，为什么拉格教授\x01",
            "会放弃成为祭司，而去了医院呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xA,
        (
            "#5P据说，当时是医院的院长\x01",
            "来挖角的。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xA,
        (
            "#5P拉格教授虽然在跟随大主教\x01",
            "学习调配药剂……\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xA,
        (
            "#5P但他也很想挑战一下\x01",
            "先进医疗这个领域，\x01",
            "因此就放弃了祭司这条道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xA,
        (
            "#5P而大主教也是个顽固的人，\x01",
            "无法原谅放弃祭司之路的拉格教授。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x104,
        "#12P#0303F嗯，这种心情也不是不能理解啊。\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xA,
        (
            "#5P不过，大主教虽然很顽固……\x01",
            "但也是个明事理的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xA,
        (
            "#5P你看，他不是自愿\x01",
            "把药草交给你们了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xA,
        (
            "#5P对于拉格教授的实力，\x01",
            "大主教还是非常认同的。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x103,
        (
            "#12P#0203F看来，他们之间的关系并不是很麻烦……\x02\x03",

            "#0200F而是超级麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        (
            "#12P#0012F哈、哈哈……\x01",
            "（说得还真直接啊……）\x02\x03",

            "#0003F总之，\x01",
            "已经得到了目标物品。\x02\x03",

            "#0000F快点去乌尔斯拉医院，\x01",
            "把药草交给拉格教授吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(98000, 2000, 7000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0x0, 98000, 0, 7000, 270)
    SetChrPos(0x1, 98000, 0, 7000, 270)
    SetChrPos(0x2, 98000, 0, 7000, 270)
    SetChrPos(0x3, 98000, 0, 7000, 270)
    OP_29(0x13, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_41_B499 end

    def Function_42_BE62(): pass

    label("Function_42_BE62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BECE")

    #C0638
    ChrTalk(
        0x8,
        (
            "……拉格教授他\x01",
            "是遵从自己的意志\x01",
            "而选择从医之路的。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x8,
        (
            "对此，我也无法\x01",
            "再多说些什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C040")

    label("loc_BECE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_BF2E")

    #C0640
    ChrTalk(
        0x8,
        (
            "……怎么了，\x01",
            "还有什么别的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x8,
        (
            "拿到了药草的话，\x01",
            "就快点送过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C040")

    label("loc_BF2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_C040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BFA7")

    #C0642
    ChrTalk(
        0x8,
        (
            "『羽扇豆草』储备在圣堂左侧\x01",
            "的最里面，我的办公室内。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x8,
        (
            "去找伦顿祭司，\x01",
            "他会拿给你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C040")

    label("loc_BFA7")


    #C0644
    ChrTalk(
        0x8,
        (
            "『羽扇豆草』储备在圣堂左侧\x01",
            "的最里面，我的办公室内。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x8,
        (
            "去找伦顿祭司，\x01",
            "他会拿给你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x8,
        "……还有什么别的事情吗？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        "#0005F不，没有了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C040")

    Return()

    # Function_42_BE62 end

    def Function_43_C041(): pass

    label("Function_43_C041")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1700, 16650, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27870, 0)
    OP_93(0xC, 0x5A, 0x0)
    SetChrPos(0x101, 153300, 200, 16500, 270)
    SetChrPos(0xEF, 154500, 200, 17180, 270)
    SetChrPos(0x153, 153300, 200, 17700, 270)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C47F")

    #C0648
    ChrTalk(
        0x153,
        "#11P#1110F下午好，我们又来了！\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xC,
        "#5P哎呀，下午好，小琪雅。\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xC,
        "#5P……难道是忘记什么东西了吗？\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        (
            "#12P#0000F不，并不是\x01",
            "那样的……\x02\x03",

            "其实，刚才正好跟孩子们擦肩而过，\x01",
            "所以有点在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0xC,
        (
            "#5P呵呵，主日学校\x01",
            "又要开始上课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xC,
        (
            "#5P不过……\x01",
            "你们来得\x01",
            "倒是正好。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0654
    ChrTalk(
        0xC,
        (
            "#5P实际上，很久之前……\x01",
            "就想给孩子们讲讲\x01",
            "关于克洛斯贝尔警察的事情了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C289")

    #C0655
    ChrTalk(
        0x102,
        "#12P#0105F关于警察的……事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C301")

    label("loc_C289")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C2BC")

    #C0656
    ChrTalk(
        0x103,
        "#12P#0205F关于警察……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C301")

    label("loc_C2BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C301")

    #C0657
    ChrTalk(
        0x104,
        (
            "#12P#0305F在主日学校\x01",
            "给孩子们上关于警察的课吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C301")


    #C0658
    ChrTalk(
        0xC,
        "#5P嗯，没错。\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xC,
        (
            "#5P因此，想拜托你们……\x01",
            "担任这堂课的\x01",
            "特别讲师。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0660
    ChrTalk(
        0x101,
        (
            "#12P#0005F特别讲师？也就是说……\x01",
            "需要我上讲台吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xC,
        "#5P嗯，请一定要帮这个忙。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0xC,
        (
            "#5P警察的知识，\x01",
            "果然还是由警察\x01",
            "来讲最合适吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xC,
        (
            "#5P我想，与我相比，\x01",
            "你们来教的效果会好得多。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xC,
        (
            "#5P怎么样？要不要试着做一回……\x01",
            "主日学校的讲师呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x4, 0x2)
    OP_29(0x27, 0x1, 0x0)
    Jump("loc_C4B6")

    label("loc_C47F")


    #C0665
    ChrTalk(
        0xC,
        (
            "#5P担任主日学校的讲师一事……\x01",
            "你们愿意\x01",
            "接受了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4B6")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5C6")

    #C0666
    ChrTalk(
        0x101,
        (
            "#12P#0003F不……\x01",
            "还请容我推辞。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xC,
        (
            "#5P哎呀，这样吗？\x01",
            "我还觉得\x01",
            "这是个不错的想法呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xC,
        (
            "#5P不过，如果不方便的话，\x01",
            "那就不勉强你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xC,
        (
            "#5P要是改变主意了，\x01",
            "就再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)

    label("loc_C5C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF3")

    #C0670
    ChrTalk(
        0x101,
        (
            "#12P#0000F……嗯，\x01",
            "请务必让我接受这项委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xC,
        (
            "#5P哎呀，真的吗？\x01",
            "呵呵，真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C637():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C637)

    def lambda_C644():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_C644)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C6B5")

    #C0672
    ChrTalk(
        0x102,
        (
            "#12P#0105F罗伊德……没问题吗？\x02\x03",

            "#0103F我想，教人学习\x01",
            "并不是一件\x01",
            "简单的事情哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78B")

    label("loc_C6B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C717")

    #C0673
    ChrTalk(
        0x103,
        (
            "#12P#0200F……没问题吗？\x02\x03",

            "#0203F教学生这种事情，\x01",
            "半桶水是应付不来的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78B")

    label("loc_C717")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C78B")

    #C0674
    ChrTalk(
        0x104,
        (
            "#12P#0306F喂喂，你没问题吧？\x02\x03",

            "#0300F虽然由我来说也不太合适……\x01",
            "但这并不是\x01",
            "可以轻易答应的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C78B")


    def lambda_C790():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C790)

    #C0675
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，我知道。\x01",
            "我也不是\x01",
            "不经思考就接受的。\x02\x03",

            "#0003F只是……我觉得这是一个\x01",
            "让大家了解警察\x01",
            "的难得机会。\x02\x03",

            "#0000F就像过去的我和艾莉一样，\x01",
            "在这些孩子当中，说不定也会有\x01",
            "未来的警察呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8A7")

    #C0676
    ChrTalk(
        0x102,
        (
            "#12P#0104F……原来如此，\x01",
            "真是很符合罗伊德风格的想法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C933")

    label("loc_C8A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8E8")

    #C0677
    ChrTalk(
        0x103,
        "#12P#0204F嗯……确实也有一定的道理呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C933")

    label("loc_C8E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C933")

    #C0678
    ChrTalk(
        0x104,
        (
            "#12P#0300F原来如此……\x01",
            "也就是说，有点类似传教活动吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C933")


    def lambda_C938():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C938)

    #C0679
    ChrTalk(
        0x101,
        (
            "#6P#0000F这样的话，就要迟一点再去\x01",
            "乌尔斯拉医院了……\x01",
            "琪雅，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x153,
        (
            "#11P#1109F嗯，可以啊！\x02\x03",

            "#1100F虽然不是很明白，\x01",
            "但罗伊德要是想做的话，\x01",
            "琪雅会支持你的！\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#6P#0009F哈哈，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xC,
        (
            "#5P好了，那么……\x01",
            "先出去一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xC,
        (
            "#5P我先把讲课的流程\x01",
            "告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CA4D():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA4D)

    def lambda_CA5A():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_CA5A)

    def lambda_CA67():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_CA67)

    #C0684
    ChrTalk(
        0x101,
        (
            "#12P#0000F拜托您了，\x01",
            "玛布尔老师。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0685
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【主日学校的特别讲师】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Call(0, 44)
    Call(0, 45)
    Call(0, 48)

    label("loc_CAF3")

    Return()

    # Function_43_C041 end

    def Function_44_CAF4(): pass

    label("Function_44_CAF4")

    OP_68(7710, 2300, -90, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(26410, 0)
    SetChrPos(0xC, 7600, 0, 1320, 270)
    SetChrPos(0x101, 5570, 0, 1350, 90)
    SetChrPos(0xEF, 4380, 0, 2050, 90)
    SetChrPos(0x153, 4720, 0, 510, 90)
    Sleep(500)
    SetCameraDistance(25410, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_64(0xC)
    OP_6F(0x79)

    #C0686
    ChrTalk(
        0x101,
        (
            "#5P#0003F──原来如此，我大致清楚了。\x02\x03",

            "首先要把有关警察的知识\x01",
            "简单易懂地说明一遍……\x02\x03",

            "#0000F最后再留出答疑的时间。\x01",
            "……差不多就是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0xC,
        "#12P嗯，那样就足够了。\x02",
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xC,
        "#12P另外，我有一个提议。\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x101,
        "#5P#0005F提议……吗？\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0xC,
        "#12P对，如果方便的话……\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0xC,
        (
            "#12P让琪雅也来\x01",
            "听罗伊德\x01",
            "讲课吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0692
    ChrTalk(
        0x101,
        "#5P#0005F哎……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD38")

    #C0693
    ChrTalk(
        0x102,
        (
            "#5P#0100F玛布尔老师……\x01",
            "真的可以吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDAC")

    label("loc_CD38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD77")

    #C0694
    ChrTalk(
        0x103,
        (
            "#5P#0204F确实……\x01",
            "那样好像很有趣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDAC")

    label("loc_CD77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDAC")

    #C0695
    ChrTalk(
        0x104,
        "#5P#0309F哈哈，不是挺有趣的嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_CDAC")


    #C0696
    ChrTalk(
        0x153,
        (
            "#5P#1105F琪雅也可以听\x01",
            "罗伊德讲课吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0xC,
        "#12P嗯，当然可以了。\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0xC,
        (
            "#12P像你这个年纪的孩子，\x01",
            "本来也已经可以\x01",
            "来主日学校上课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x153,
        "#5P#1110F哇……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    #C0700
    ChrTalk(
        0x153,
        (
            "#6P#1109F那琪雅\x01",
            "也要听课！\x02\x03",

            "因为琪雅想要知道很多\x01",
            "有关罗伊德他们的事情！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CEA0():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEA0)
    Sleep(50)

    def lambda_CEB0():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_CEB0)

    #C0701
    ChrTalk(
        0x101,
        "#12P#0005F琪雅……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF24")

    #C0702
    ChrTalk(
        0x102,
        (
            "#5P#0100F罗伊德，这样的话，\x01",
            "你真是不上也不行了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFB1")

    label("loc_CF24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF69")

    #C0703
    ChrTalk(
        0x103,
        (
            "#5P#0200F罗伊德前辈……\x01",
            "似乎没有退路了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFB1")

    label("loc_CF69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFB1")

    #C0704
    ChrTalk(
        0x104,
        (
            "#5P#0300F话都说到这份上了，\x01",
            "看来你是逃不掉了吧～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFB1")


    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#0004F……哈哈，似乎是这样啊。\x02\x03",

            "#0000F琪雅，要和其他孩子\x01",
            "一起认真听课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x153,
        "#6P#1110F嗯！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D07B")

    #C0707
    ChrTalk(
        0x102,
        (
            "#5P#0104F我也到\x01",
            "教室的后面\x01",
            "去看看你上课的样子吧。\x02\x03",

            "#0100F加油哦，罗伊德。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D156")

    label("loc_D07B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0EB")

    #C0708
    ChrTalk(
        0x103,
        (
            "#5P#0203F我也打算去教室后面\x01",
            "旁听一下。\x02\x03",

            "#0211F……我会为前辈加油的，\x01",
            "所以请不要搞砸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D156")

    label("loc_D0EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D156")

    #C0709
    ChrTalk(
        0x104,
        (
            "#5P#0304F那么，我也去教室后面\x01",
            "看看你上课的样子吧。\x02\x03",

            "#0300F罗伊德老师，\x01",
            "给我露一手吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D156")


    def lambda_D15B():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D15B)

    #C0710
    ChrTalk(
        0x101,
        (
            "#12P#0006F（感、感觉好狡猾啊……）\x02\x03",

            "#0000F不过……\x01",
            "也只有加油上了。\x02\x03",

            "这是一个让大家\x01",
            "了解警察的好机会……\x01",
            "可不能错过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xC,
        "#12P就是要有那股气势。\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0xC,
        (
            "#12P好了……\x01",
            "差不多也该\x01",
            "开始上课了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Return()

    # Function_44_CAF4 end

    def Function_45_D235(): pass

    label("Function_45_D235")

    LoadChrToIndex("chr/ch08202.itc", 0x1E)
    OP_68(151700, 1500, 4100, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    SetChrPos(0xC, 150800, 200, 17500, 180)
    SetChrPos(0x153, 153000, 200, 17650, 180)
    SetChrPos(0x101, 155630, 200, 17510, 270)
    SetChrPos(0xEF, 150910, 0, 1530, 0)
    OP_68(151620, 1500, 14920, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0713
    ChrTalk(
        0xC,
        "#11P那么……\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0xC,
        (
            "#11P今天在上课之前，\x01",
            "先给大家\x01",
            "介绍一位新朋友。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x153, 500)

    #C0715
    ChrTalk(
        0xC,
        "#5P──琪雅，请做下自我介绍吧。\x02",
    )

    CloseMessageWindow()

    def lambda_D341():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D341)
    OP_98(0x153, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)

    #C0716
    ChrTalk(
        0x153,
        (
            "#11P#1110F那个，我是琪雅哦！\x01",
            "请多关照！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 200, -1, -1)
    SetChrName("孩子们")

    #A0717
    AnonymousTalk(
        0xFF,
        "#5S请多关照～～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0718
    ChrTalk(
        0xC,
        (
            "#11P呵呵，谢谢你充满朝气的\x01",
            "自我介绍。请找个\x01",
            "空位置坐下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x153,
        "#11P#1109F好～\x02",
    )

    CloseMessageWindow()
    OP_68(154300, 1500, 8280, 4000)
    OP_95(0x153, 153000, 200, 14000, 2000, 0x0)
    OP_95(0x153, 152000, 200, 14000, 2000, 0x0)
    OP_95(0x153, 152000, 200, 9100, 2000, 0x0)
    OP_93(0x153, 0x5A, 0x12C)
    Fade(500)
    SetChrChipByIndex(0x153, 0x1E)
    SetChrPos(0x153, 153620, 150, 9130, 0)
    SetChrFlags(0x153, 0x4)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x153, 0x2)
    SetChrSubChip(0x11, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    #C0720
    ChrTalk(
        0x153,
        "#5P#1109F嘿嘿，请多关照哦！\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x11,
        (
            "#12P嗯、嗯，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(152620, 1500, 3180, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D591")

    #C0722
    ChrTalk(
        0x102,
        (
            "#6P#0104F（呵呵……感觉自己有点像\x01",
            "　参加教学旁听的母亲呢。）\x02\x03",

            "#0100F（小琪雅，加油啊！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D686")

    label("loc_D591")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D60C")

    #C0723
    ChrTalk(
        0x103,
        (
            "#6P#0204F（……家长们的教学参观……\x01",
            "　现在大概就是这种感觉吧。）\x02\x03",

            "#0200F（必须要给琪雅加油呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D686")

    label("loc_D60C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D686")

    #C0724
    ChrTalk(
        0x104,
        (
            "#6P#0304F（默默守护认真学习的女儿……\x01",
            "　哈，这种立场可真让人振奋百倍呢。）\x02\x03",

            "#0309F（加油啊！阿琪！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D686")

    OP_5A()
    Fade(500)
    SetChrSubChip(0x153, 0x0)
    SetChrSubChip(0x11, 0x0)
    OP_68(152750, 1500, 15630, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()

    #C0725
    ChrTalk(
        0xC,
        (
            "#11P还有……今天\x01",
            "我们请来了特别讲师\x01",
            "为大家讲课。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 300)

    #C0726
    ChrTalk(
        0xC,
        "#5P──罗伊德，请吧。\x02",
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x101,
        "#12P#0003F是、是。\x02",
    )

    CloseMessageWindow()
    OP_68(152250, 1700, 12670, 3000)
    MoveCamera(310, 14, 0, 3000)
    SetCameraDistance(30190, 3000)
    BeginChrThread(0x101, 3, 0, 46)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 47)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    #C0728
    ChrTalk(
        0x21,
        (
            "#6P喂喂，\x01",
            "我刚才还在想，会不会是这样……\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x15,
        "#6P真没想到，特别讲师居然就是……\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x101,
        (
            "#11P#0003F那、那个……\x01",
            "有些同学似乎\x01",
            "已经认识我了呢……\x02\x03",

            "#0000F我的名字是\x01",
            "罗伊德·班宁斯。\x02\x03",

            "是隶属于克洛斯贝尔\x01",
            "警察局·特别任务支援科的\x01",
            "现役警察。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0xF,
        (
            "#5P警察～？\x01",
            "什么啊，你认识\x01",
            "隆他们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x10,
        "#5P特别任务支援科……\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x10,
        (
            "#5P啊，我好像看到过\x01",
            "克洛斯贝尔时代周刊上的报道！\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0xF,
        "#5P……啊啊，说起来！\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0xF,
        (
            "#5P虽然我没有读新闻，\x01",
            "但记得上面登了张\x01",
            "很小的照片……\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xC,
        "#11P好了好了，大家安静。\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0xC,
        (
            "#11P今天想让大家学习\x01",
            "关于警察的知识，\x01",
            "所以就拜托罗伊德老师过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xC,
        (
            "#11P大家要认真\x01",
            "听讲哦～\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("孩子们")

    #A0739
    AnonymousTalk(
        0xFF,
        "#5S是～～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TurnDirection(0xC, 0x101, 300)

    #C0740
    ChrTalk(
        0xC,
        (
            "#5P那么，接下来就拜托你啦，\x01",
            "罗伊德老师⊥\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 300)

    #C0741
    ChrTalk(
        0x101,
        (
            "#11P#0003F好、好的，\x01",
            "请交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x12C)
    OP_95(0xC, 146430, 200, 17490, 2000, 0x0)
    OP_93(0xC, 0x87, 0x12C)
    OP_93(0x101, 0xB4, 0x12C)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0742
    ChrTalk(
        0x101,
        (
            "#11P#0003F（糟糕……\x01",
            "　突然好紧张啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(153200, 1700, 9500, 3000)
    MoveCamera(319, 10, 0, 3000)
    OP_6F(0x79)
    OP_64(0x153)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0743
    ChrTalk(
        0x153,
        "#6P#1107F#5S#N……罗伊德，加油哦！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x21, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0744
    ChrTalk(
        0x21,
        (
            "#6P啊哈哈！怎么了啊，大哥哥！\x01",
            "她在给你加油哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x15,
        "#6P我说隆，你别这样啦～\x02",
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x15,
        (
            "#6P大哥哥\x01",
            "也很努力的～\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x101,
        (
            "#11P#0006F那个，琪雅……\x01",
            "要开始上课了，安静一点哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x153,
        "#6P#1106F哼，琪雅明明是在给你加油。\x02",
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#11P#0004F（……紧张的感觉\x01",
            "　好像稍微有点缓解了。）\x02\x03",

            "#0000F……咳咳。\x01",
            "那么，我们现在就开始吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0x7D0)
    Fade(500)
    OP_68(151090, 1500, 15660, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32470, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0750
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　 开始上课！\x01",
            "～关于警察组织～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0751
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※请选择正确的答案，\x01",
            "　使特别授课获得成功！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0752
    ChrTalk(
        0x101,
        (
            "#0004F首先……\x01",
            "大家知道警察\x01",
            "是什么吗？\x02\x03",

            "#0000F在克洛斯贝尔自治州，\x01",
            "规定了不能拥有\x01",
            "其它国家具备的『某项东西』。\x02\x03",

            "作为替代，才会有『警备队』以及\x01",
            "我们这些『警察』存在。\x02\x03",

            "#0003F克洛斯贝尔自治州所没有的，\x01",
            "『对国家来说非常重要的东西』指的是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0753
    AnonymousTalk(
        0xFF,
        (
            "克洛斯贝尔自治州所没有的，\x01",
            "『对国家来说非常重要的东西』指的是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①情报机关】\x01",        # 0
            "【②游击士协会】\x01",      # 1
            "【③军队】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DF01"),
        (1, "loc_E032"),
        (2, "loc_E0FA"),
        (SWITCH_DEFAULT, "loc_E1FF"),
    )


    label("loc_DF01")


    #C0754
    ChrTalk(
        0x101,
        "#0000F……是情报机关。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0755
    ChrTalk(
        0x101,
        (
            "#0005F（那种组织确实并不存在，\x01",
            "　但好像也没有被法律所禁止啊……）\x02\x03",

            "#0012F那个……为了保护国家，\x01",
            "收集邻近各国的情报\x01",
            "是必不可少的……\x02\x03",

            "虽然平时都致力于防止犯罪，\x01",
            "但暗地里却通过游客等途径\x01",
            "收集重要的情报。\x02\x03",

            "#0011F（我、我到底在说些什么啊……\x01",
            "　果然是太紧张了吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1FF")

    label("loc_E032")


    #C0756
    ChrTalk(
        0x101,
        "#0000F……游击士协会。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0757
    ChrTalk(
        0x101,
        (
            "#0012F虽、虽然游击士协会\x01",
            "现在的表现非常活跃……\x02\x03",

            "但在过去，扮演其角色，\x01",
            "并守卫着市民们的是警察。\x02\x03",

            "#0006F（说、说的实在是乱七八糟……\x01",
            "　果然是太紧张了吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1FF")

    label("loc_E0FA")


    #C0758
    ChrTalk(
        0x101,
        (
            "#0000F……是军队。\x02\x03",

            "举例来说，在邻国埃雷波尼亚，\x01",
            "由军队全权负责抵御入侵\x01",
            "与防止犯罪……\x02\x03",

            "但在没有军队的克洛斯贝尔，\x01",
            "这些职能就分别\x01",
            "由数个组织来承担。\x02\x03",

            "……在那之中，\x01",
            "负责调查案件，以及防止犯罪\x01",
            "的就是我们警察了。\x02\x03",

            "#0004F（很好，应该没有错。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_E1FF")

    label("loc_E1FF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    #C0759
    ChrTalk(
        0x101,
        (
            "#0000F警察局中设有各种部门，\x01",
            "人员会依据职能被分配到不同部门中。\x02\x03",

            "然后各事件会按照其种类与紧急程度\x01",
            "被分派给各部门，以便他们\x01",
            "采取妥善的方法来处理。\x02\x03",

            "#0003F其中，有一个处理\x01",
            "震动社会的大事件，\x01",
            "以及国际性案件的部门……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0760
    AnonymousTalk(
        0xFF,
        (
            "处理大事件以及\x01",
            "国际性案件的部门是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①搜查一科】\x01",            # 0
            "【②搜查二科】\x01",            # 1
            "【③特别任务支援科】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E3B3"),
        (1, "loc_E48D"),
        (2, "loc_E584"),
        (SWITCH_DEFAULT, "loc_E67A"),
    )


    label("loc_E3B3")


    #C0761
    ChrTalk(
        0x101,
        (
            "#0000F……是搜查一科。\x02\x03",

            "要解决绑架、杀人之类的大案件，\x01",
            "就需要一流的搜查官\x01",
            "全力以赴。\x02\x03",

            "因此，聚集了精英搜查官的\x01",
            "搜查一科便负责全权处理\x01",
            "此类案件。\x02\x03",

            "#0004F（我们也不能输给他们，\x01",
            "　必须得继续加油啊。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_E67A")

    label("loc_E48D")


    #C0762
    ChrTalk(
        0x101,
        "#0000F……是搜查二科。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0763
    ChrTalk(
        0x101,
        (
            "#0000F要处理绑架、杀人\x01",
            "之类的大案件，当然也得具备\x01",
            "解决小案子的能力。\x02\x03",

            "平日就负责处理盗窃等案件的\x01",
            "搜查二科，也会勤勤恳恳地\x01",
            "对大型案件进行调查哦。\x02\x03",

            "#0006F（……虽然说得\x01",
            "　像模像样……\x01",
            "　但真的是那样吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E67A")

    label("loc_E584")


    #C0764
    ChrTalk(
        0x101,
        "#0000F……是我们，特别任务支援科。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0765
    ChrTalk(
        0x101,
        (
            "#0000F要想解决绑架、杀人\x01",
            "之类的大型案件，大范围的\x01",
            "调查活动是很重要的。\x02\x03",

            "从这层意义上讲，\x01",
            "行动自由的特别任务支援科\x01",
            "最适合调查大型案件了。\x02\x03",

            "#0006F（……啊，好像把我们自己\x01",
            "　美化过头了呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E67A")

    label("loc_E67A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    #C0766
    ChrTalk(
        0x101,
        (
            "#0000F每一位警察都会得到一本叫做\x01",
            "调查手册的东西。\x02\x03",

            "这本调查手册\x01",
            "除了可以证明我们的警察身份之外，\x01",
            "还有一个最大，也是最重要的用途。\x02\x03",

            "#0003F那是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0767
    AnonymousTalk(
        0xFF,
        (
            "调查手册的重要用途是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①记录调查情况】\x01",      # 0
            "【②代替逮捕令】\x01",        # 1
            "【③报告当前位置】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E7E1"),
        (1, "loc_E8C7"),
        (2, "loc_E9B5"),
        (SWITCH_DEFAULT, "loc_EA8C"),
    )


    label("loc_E7E1")


    #C0768
    ChrTalk(
        0x101,
        (
            "#0000F……记录调查情况。\x01",
            "也就是说，调查手册与笔记本相同。\x02\x03",

            "它在用于整理任务情况时非常便利，而警察局也会\x01",
            "以此为依据来审核勤务，以及发放各种经费。\x02\x03",

            "调查手册确实是\x01",
            "警察的必备物品啊。\x02\x03",

            "#0004F（嗯，完全没有问题。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_EA8C")

    label("loc_E8C7")


    #C0769
    ChrTalk(
        0x101,
        "#0000F……代替逮捕令。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0770
    ChrTalk(
        0x101,
        (
            "#0012F那、那个，要逮捕嫌疑犯的话，\x01",
            "需要向警察局总部\x01",
            "提交正式的申请……\x02\x03",

            "#0000F但在紧急时刻，\x01",
            "只要出示这本手册，\x01",
            "即使没有逮捕令，也可以将嫌疑人逮捕。\x02\x03",

            "#0006F（嗯、嗯……\x01",
            "　稍微有点没自信呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA8C")

    label("loc_E9B5")


    #C0771
    ChrTalk(
        0x101,
        "#0000F……报告当前位置。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0772
    ChrTalk(
        0x101,
        (
            "#0012F那、那个……\x01",
            "这本手册带有将\x01",
            "所在地信息发送出去的机能……\x02\x03",

            "#0000F所以，即使出勤在外，\x01",
            "也能让同伴们知道\x01",
            "自己所处的位置。\x02\x03",

            "#0006F（不、不管怎么说，这都太夸张了啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA8C")

    label("loc_EA8C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    #C0773
    ChrTalk(
        0x101,
        (
            "#0000F警察与游击士一样，\x01",
            "配备有最新型的\x01",
            "战术导力器。\x02\x03",

            "#0003F警察虽然不是专门的战斗集团，\x01",
            "但搜查官在追捕犯人时，\x01",
            "经常避免不了战斗。\x02\x03",

            "#0000F顺便说一下，战术导力器的型号\x01",
            "已经更新过好几代了，\x01",
            "而且每次更新都会追加新功能。\x02\x03",

            "#0003F现在我们所使用的\x01",
            "战术导力器的型号是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0774
    AnonymousTalk(
        0xFF,
        (
            "目前的战术导力器的型号是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①第５代】\x01",      # 0
            "【②第６代】\x01",      # 1
            "【③第７代】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EC5D"),
        (1, "loc_ED14"),
        (2, "loc_EDC4"),
        (SWITCH_DEFAULT, "loc_EE7A"),
    )


    label("loc_EC5D")


    #C0775
    ChrTalk(
        0x101,
        (
            "#0000F……第５代，\x01",
            "通常被称为\x01",
            "『艾尼格玛』。\x02\x03",

            "艾尼格玛内设有通讯器。\x01",
            "因为可以在紧急时刻进行联络，\x01",
            "所以这项功能对警察行业来说十分宝贵。\x02\x03",

            "#0004F（嗯，应该没说错。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_EE7A")

    label("loc_ED14")


    #C0776
    ChrTalk(
        0x101,
        (
            "#0000F……第６代，\x01",
            "通常被称为\x01",
            "『艾尼格玛』。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0777
    ChrTalk(
        0x101,
        (
            "#0000F由于型号的变化，结晶回路也\x01",
            "必须重新合成，\x01",
            "所以用起来很麻烦。\x02\x03",

            "#0006F（……咦，是第６代\x01",
            "　没错吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE7A")

    label("loc_EDC4")


    #C0778
    ChrTalk(
        0x101,
        (
            "#0000F……第７代，\x01",
            "通常被称为\x01",
            "『艾尼格玛』。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0779
    ChrTalk(
        0x101,
        (
            "#0012F那、那个……\x01",
            "因为各种功能都变得十分新颖，\x01",
            "所以用起来很麻烦呢。\x02\x03",

            "#0006F（嗯、嗯……\x01",
            "　更新过那么多代吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE7A")

    label("loc_EE7A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    #C0780
    ChrTalk(
        0x101,
        (
            "#0000F巡警、搜查官……\x01",
            "担当各类职责的警察们，\x01",
            "都在为了克洛斯贝尔而辛勤工作。\x02\x03",

            "#0003F虽然从表面上看起来，\x01",
            "他们之间完全没有联系……\x02\x03",

            "#0000F但是，警察们\x01",
            "在工作时，\x01",
            "都是按照某个基本理念来行动的。\x02\x03",

            "#0003F那个基本理念是…………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0781
    AnonymousTalk(
        0xFF,
        (
            "警察的基本理念是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①保障克洛斯贝尔市民的安全】\x01",      # 0
            "【②维持治安与遵守当地法律】\x01",        # 1
            "【③警戒国外势力与维护和平】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F04B"),
        (1, "loc_F125"),
        (2, "loc_F258"),
        (SWITCH_DEFAULT, "loc_F371"),
    )


    label("loc_F04B")


    #C0782
    ChrTalk(
        0x101,
        "#0000F……保障克洛斯贝尔市民的安全。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0783
    ChrTalk(
        0x101,
        (
            "#0000F无论在何种情况下，\x01",
            "都要誓死守护克洛斯贝尔市民……\x02\x03",

            "创造一个让大家都能\x01",
            "安心生活的社会，这就是警察的本职。\x02\x03",

            "#0006F（嗯、嗯。\x01",
            "　说明好像稍微有点不够吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F371")

    label("loc_F125")


    #C0784
    ChrTalk(
        0x101,
        (
            "#0000F……是维持自治州的治安与遵守自治州法律。\x02\x03",

            "通过管制破坏法规的人，\x01",
            "来创造一个可以让大家\x01",
            "安心生活的社会……\x02\x03",

            "将自己遵纪守法的一面展示给市民，\x01",
            "成为大家的榜样，\x01",
            "从而抑制犯罪的发生。\x02\x03",

            "综上所述，维持治安，\x01",
            "努力建立一个没有\x01",
            "犯罪的世界，便是警察的本职。\x02\x03",

            "#0004F（好了……总结得非常不错！）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_F371")

    label("loc_F258")


    #C0785
    ChrTalk(
        0x101,
        "#0000F……是保持对国外势力的警戒与维护和平。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0786
    ChrTalk(
        0x101,
        (
            "#0000F被帝国与共和国\x01",
            "这两个大国夹在中间的克洛斯贝尔，\x01",
            "是个犯罪频发的地方。\x02\x03",

            "抵御他国敌对势力的入侵，\x01",
            "创造一个大家能够\x01",
            "安心生活的社会，便是警察的本职。\x02\x03",

            "#0006F（……呃，硬要说的话，\x01",
            "　这应该是\x01",
            "　警备队的工作吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F371")

    label("loc_F371")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    #C0787
    ChrTalk(
        0x101,
        (
            "#0004F──综上所述，克洛斯贝尔警察局\x01",
            "便是这样一种组织。\x02\x03",

            "#0000F……虽然对你们来说有可能还有些复杂，\x01",
            "但大家应该都听明白了吧？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(152620, 1500, 3180, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F68E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F52C")

    #C0788
    ChrTalk(
        0x102,
        (
            "#6P#0100F（这样一来，教学的前半部分就结束了。）\x02\x03",

            "#0104F（虽然刚开始还有点紧张，\x01",
            "　但却让人一点都看不出来，\x01",
            "　很有老师的样子呢。）\x02\x03",

            "#0100F（真不愧是通过了\x01",
            "　搜查官考试的实力派。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F689")

    label("loc_F52C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F5D7")

    #C0789
    ChrTalk(
        0x102,
        (
            "#6P#0100F（这样一来，教学的前半部分就结束了。）\x02\x03",

            "#0103F（嗯，即使是罗伊德，\x01",
            "　似乎也稍微陷入了苦战呢。）\x02\x03",

            "（不知道是不是\x01",
            "　因为开始时太紧张了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F689")

    label("loc_F5D7")


    #C0790
    ChrTalk(
        0x102,
        (
            "#6P#0103F（这样一来，教学的前半部分就结束了。）\x02\x03",

            "#0111F（但是……\x01",
            "　总觉得，如果是罗伊德的话，\x01",
            "　应该能够表现得更好一点的。）\x02\x03",

            "（也就是说，玛布尔老师\x01",
            "　似乎看错人了呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F689")

    Jump("loc_FB53")

    label("loc_F68E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F904")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F782")

    #C0791
    ChrTalk(
        0x103,
        (
            "#6P#0200F（教学的前半部分\x01",
            "　终于结束了。）\x02\x03",

            "#0204F（授课内容完美地把握住了重点，\x01",
            "　而且声音洪亮，讲解内容有条不紊……\x01",
            "　真是无懈可击。）\x02\x03",

            "（罗伊德前辈就算\x01",
            "　去大学之类的地方执教，\x01",
            "　或许也足以胜任呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8FF")

    label("loc_F782")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F83A")

    #C0792
    ChrTalk(
        0x103,
        (
            "#6P#0200F（教学的前半部分\x01",
            "　终于结束了。）\x02\x03",

            "#0203F（声音偶尔会有一种缺乏自信的感觉，\x01",
            "　让我稍稍担心了一下……）\x02\x03",

            "（毕竟是我们的领队，\x01",
            "　希望他能再加把劲呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8FF")

    label("loc_F83A")


    #C0793
    ChrTalk(
        0x103,
        (
            "#6P#0200F（教学的前半部分\x01",
            "　终于结束了。）\x02\x03",

            "#0211F（……眼睛完全不敢正视学生，\x01",
            "　紧张得连手都不知道该放在哪里了……）\x02\x03",

            "（……讲得实在是不怎么样呢。\x01",
            "　就算由我来教，\x01",
            "　可能都要比这好一些……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8FF")

    Jump("loc_FB53")

    label("loc_F904")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB53")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F9C8")

    #C0794
    ChrTalk(
        0x104,
        (
            "#6P#0305F（哦，前半战已经结束了啊。）\x02\x03",

            "#0309F（真不错，\x01",
            "　挺有摸有样的嘛。）\x02\x03",

            "#0303F（世界上的淑女们\x01",
            "　都对这样的男人没有抵抗力。\x01",
            "　真是个可恶的家伙……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB53")

    label("loc_F9C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FAA3")

    #C0795
    ChrTalk(
        0x104,
        (
            "#6P#0305F（哦，前半战已经结束了啊。）\x02\x03",

            "#0303F（不过，感觉有点危险啊。\x01",
            "　连我都知道的问题也给弄错了，\x01",
            "　真是不应该啊。）\x02\x03",

            "#0309F（不过，稍微笨拙一点，\x01",
            "　反而更容易激发出\x01",
            "　淑女们的母性本能吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB53")

    label("loc_FAA3")


    #C0796
    ChrTalk(
        0x104,
        (
            "#6P#0305F（哦，前半战已经结束了啊。）\x02\x03",

            "#0306F（真是的，别让小鬼们看到\x01",
            "　你那么逊的样子啊～）\x02\x03",

            "（如果不表现得知性十足，\x01",
            "　不就白白浪费了在米修拉姆\x01",
            "　发掘的眼镜属性了嘛。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB53")

    OP_5A()
    Fade(500)
    OP_68(151640, 2100, 12440, 0)
    MoveCamera(329, 14, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30960, 0)
    OP_0D()

    #C0797
    ChrTalk(
        0xC,
        (
            "#5P……那么，同学们，\x01",
            "还有什么问题\x01",
            "要问罗伊德老师吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0xC,
        (
            "#5P老师很有耐心，\x01",
            "无论有什么问题，他都会为大家解答的。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x101,
        (
            "#11P#0005F（玛、玛布尔老师！？\x01",
            "　这太勉强了……）\x02\x03",

            "#0006F（……呼，看来也只有硬着头皮上了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0800
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　         提问时间到！\x01",
            "～学生们会提出平时产生的任何疑问～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0801
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※请选择正确的答案，\x01",
            "　解答各种棘手的问题！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0802
    ChrTalk(
        0x101,
        "#0000F……那么，有人要提问吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0803
    ChrTalk(
        0xF,
        (
            "#5P我、我！\x01",
            "我有问题！我有问题！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(149370, 1500, 14370, 2000)
    OP_93(0x101, 0xE1, 0x12C)
    OP_6F(0x79)

    #C0804
    ChrTalk(
        0x101,
        "#11P#0000F嗯，想问什么呢？\x02",
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0xF,
        (
            "#6P要怎样才能\x01",
            "成为老师这样的警察呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0xF,
        (
            "#6P……那个，我倒是并没打算\x01",
            "要成为警察啦，一点都没有。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)

    #C0807
    ChrTalk(
        0x10,
        (
            "#6P等一下啦，塔米尔。\x01",
            "这样说太失礼了……\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x101,
        (
            "#11P#0006F啊，没关系啦……\x02\x03",

            "#0000F这个问题是指，想成为警察\x01",
            "是否需要获得某些特别的资格吗？\x02\x03",

            "这个嘛，要成为警察的话……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0809
    AnonymousTalk(
        0xFF,
        (
            "要成为警察的话，\x01",
            "该怎么做呢？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①通过搜查官考试】\x01",      # 0
            "【②从警察学校毕业】\x01",      # 1
            "【③没有特定的方法】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FF52"),
        (1, "loc_100AF"),
        (2, "loc_1024E"),
        (SWITCH_DEFAULT, "loc_103CA"),
    )


    label("loc_FF52")


    #C0810
    ChrTalk(
        0x101,
        (
            "#11P#0000F……需要通过\x01",
            "搜查官考试。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0811
    ChrTalk(
        0x101,
        (
            "#11P#0006F不、不对……\x01",
            "如果只是想成为警察的话，并不是一定要\x01",
            "通过搜查官考试……\x02\x03",

            "#0000F基本来说，只要\x01",
            "修完警察学校的全套课程，\x01",
            "就有成为警察的资格了。\x02\x03",

            "虽然也有像我的同伴这样，\x01",
            "没有去过警察学校就直接当上警察的……\x01",
            "不过，那也算是非常特殊的例子了。\x02\x03",

            "#0006F（真、真是危险啊，\x01",
            "　差一点就说错了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103CA")

    label("loc_100AF")


    #C0812
    ChrTalk(
        0x101,
        (
            "#11P#0000F……需要从\x01",
            "警察学校毕业。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x101,
        (
            "#11P#0000F基本来说，只要\x01",
            "修完警察学校的全套课程，\x01",
            "就有成为警察的资格了。\x02\x03",

            "但是，刚才也说过了，\x01",
            "根据职能的不同，警察分为多个部门。\x02\x03",

            "比如说，想要成为搜查官的话，\x01",
            "除了修完警察学校的所有课程之外，\x01",
            "还必须要另外通过搜查官考试。\x02\x03",

            "虽然也有像我的同伴这样，\x01",
            "没有去过警察学校就直接当上警察的……\x01",
            "不过，那也算是非常特殊的例子了。\x02\x03",

            "#0004F（嗯，大概就是这个样子吧。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_103CA")

    label("loc_1024E")


    #C0814
    ChrTalk(
        0x101,
        (
            "#11P#0000F……实际上，\x01",
            "并没有特定的方法。\x02",
        )
    )

    BeginChrThread(0x101, 3, 0, 50)

    #C0815
    ChrTalk(
        0x101,
        (
            "#11P#0006F不、不对……\x01",
            "我的同伴确实没有上过警察学校，\x01",
            "就直接成为了警察……\x02\x03",

            "#0000F但一般来说，只有\x01",
            "修完警察学校的全套课程，\x01",
            "才可以成为警察。\x02\x03",

            "还有，刚才也已经说过了，\x01",
            "警察按职能划分为各种各样的部门。\x02\x03",

            "比如说，想要成为搜查官的话，\x01",
            "除了修完所有的课程之外，\x01",
            "还必须要另外通过搜查官考试。\x02\x03",

            "#0006F（唔，稍微有点混乱吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103CA")

    label("loc_103CA")

    SetChrSubChip(0x10, 0x0)

    #C0816
    ChrTalk(
        0xF,
        "#6P哼～原来如此。\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0xF,
        (
            "#6P虽然我并没打算成为警察……\x01",
            "但还是谢谢你告诉我，老师！\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x15,
        (
            "#5P啊，那么……\x01",
            "我也可以提一个问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(152570, 1200, 14810, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    #C0819
    ChrTalk(
        0x101,
        "#5P#0000F嗯，是什么呢？\x02",
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x15,
        (
            "#12P上次在克洛斯贝尔发生的事件，\x01",
            "总觉得报道得不怎么详细，\x01",
            "所以我不是很明白……\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x15,
        (
            "#12P关于之前发生的那起\x01",
            "狼形魔兽事件，最后解决它的\x01",
            "关键是什么呢？？\x02",
        )
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x101,
        (
            "#5P#0005F啊，就是黑手党滥用军犬\x01",
            "的那次事件啊。\x02\x03",

            "#0003F我记得，将那次事件\x01",
            "解决的关键是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0823
    AnonymousTalk(
        0xFF,
        (
            "解决军犬事件的关键是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①特别任务支援科的推理】\x01",      # 0
            "【②白狼的帮助】\x01",                # 1
            "【③警备队的支援】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10630"),
        (1, "loc_1076E"),
        (2, "loc_10861"),
        (SWITCH_DEFAULT, "loc_1095F"),
    )


    label("loc_10630")


    #C0824
    ChrTalk(
        0x101,
        "#5P#0000F……是特别任务支援科的推理。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0825
    ChrTalk(
        0x101,
        (
            "#5P#0006F啊，但是……\x01",
            "在最后关头，是靠蔡特\x01",
            "才将我们从危机中解救出来的。\x02\x03",

            "要是没有它的话，\x01",
            "得知真相的我们恐怕凶多吉少，\x01",
            "事件也没法得到解决……\x02\x03",

            "#0000F也就是说，解决事件的关键\x01",
            "应该还是蔡特和它带领的\x01",
            "那些白狼吧。\x02\x03",

            "#0006F（嗯……\x01",
            "　刚才的回答真是对不起蔡特啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1095F")

    label("loc_1076E")


    #C0826
    ChrTalk(
        0x101,
        (
            "#5P#0000F……是白狼的帮助哦。\x02\x03",

            "在我们只差一步就要\x01",
            "被那些军犬干掉的时候，\x01",
            "白狼率领狼群前来救援了。\x02\x03",

            "在那之后，由于某些原因，\x01",
            "狼群中的蔡特\x01",
            "就留在了特别任务支援科。\x02\x03",

            "#0004F（因为那实在是太具有冲击性了……\x01",
            "　所以没法忘记呢。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1095F")

    label("loc_10861")


    #C0827
    ChrTalk(
        0x101,
        "#5P#0000F……是警备队的支援。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0828
    ChrTalk(
        0x101,
        (
            "#5P#0005F嗯……？虽然最后确实\x01",
            "是交给了警备队……\x01",
            "但解决的关键应该在那之前吧。\x02\x03",

            "#0000F是蔡特它们将我们从\x01",
            "那场令人绝望的危机中解救出来的，\x01",
            "所以我们才能顺利将犯人逮捕。\x02\x03",

            "#0006F（唔唔，\x01",
            "　似乎搞错了呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1095F")

    label("loc_1095F")


    #C0829
    ChrTalk(
        0x15,
        (
            "#12P嘿……蔡特果然\x01",
            "好厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x15,
        "#12P谢谢你，大哥哥。\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0831
    ChrTalk(
        0x11,
        (
            "#6P#N那、那个……老师，\x01",
            "我、我也有问题……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(153270, 1500, 12030, 2000)
    SetCameraDistance(30650, 2000)
    MoveCamera(327, 8, 0, 2000)
    OP_6F(0x79)
    OP_93(0x101, 0x87, 0x12C)

    #C0832
    ChrTalk(
        0x101,
        "#11P#0000F嗯，是什么呢？\x02",
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x11,
        (
            "#6P那个，之前\x01",
            "隆跟亨利\x01",
            "在地下迷路了……\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x11,
        "#6P那里是什么地方呢？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_93(0x21, 0x5A, 0x0)
    SetChrSubChip(0x21, 0x2)
    OP_0D()

    #C0835
    ChrTalk(
        0x21,
        (
            "#5P笨蛋……小桃！\x01",
            "别提那种让我丢脸的事啊～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    #C0836
    ChrTalk(
        0x11,
        (
            "#6P因、因为，\x01",
            "你们都不肯告诉我啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x101,
        (
            "#11P#0000F是发生在地下空间的那次事件吗……\x02\x03",

            "#0003F孩子们误闯进去的是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0838
    AnonymousTalk(
        0xFF,
        (
            "隆与亨利\x01",
            "误闯进去的地方是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①地下空间·Ａ区域】\x01",      # 0
            "【②地下空间·Ｂ区域】\x01",      # 1
            "【③地下空间·Ｃ区域】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10C00"),
        (1, "loc_10CB1"),
        (2, "loc_10DC4"),
        (SWITCH_DEFAULT, "loc_10ED7"),
    )


    label("loc_10C00")


    #C0839
    ChrTalk(
        0x101,
        (
            "#11P#0000F……是地下空间·Ａ区域。\x02\x03",

            "那个时候有魔兽出现，情况相当危险呢，\x01",
            "幸好有亚里欧斯先生救援，\x01",
            "大家才能平安无事地全部返回。\x02\x03",

            "#0004F（嗯，似乎没有问题。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_10ED7")

    label("loc_10CB1")


    #C0840
    ChrTalk(
        0x101,
        (
            "#11P#0000F……是地下空间·Ｂ区域。\x02\x03",

            "#0005F……嗯？\x01",
            "好像不对……？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0841
    ChrTalk(
        0x15,
        "#12P咦？好像是Ａ区域吧……\x02",
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x101,
        (
            "#11P#0012F是、是那样吗？\x02\x03",

            "#0003F那、那个，总之……\x01",
            "当时多亏有亚里欧斯先生帮忙，\x01",
            "大家才能平安无事地全部返回。\x02\x03",

            "#0006F（对了，Ｂ区域是\x01",
            "　约纳所在的地方……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10ED7")

    label("loc_10DC4")


    #C0843
    ChrTalk(
        0x101,
        (
            "#11P#0000F……是地下空间·Ｃ区域。\x02\x03",

            "#0005F……咦，我们\x01",
            "去过Ｃ区域吗……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0844
    ChrTalk(
        0x15,
        "#12P咦？好像是Ａ区域吧……\x02",
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x101,
        (
            "#11P#0012F是、是那样吗？\x02\x03",

            "#0003F那、那个，总之……\x01",
            "当时多亏有亚里欧斯先生帮忙，\x01",
            "大家才能平安无事地全部返回。\x02\x03",

            "#0006F（嗯，记忆\x01",
            "　好像有点模糊了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10ED7")

    label("loc_10ED7")


    #C0846
    ChrTalk(
        0x11,
        (
            "#6P嘿嘿……\x01",
            "老师，谢谢你。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x21, 0x0)
    OP_93(0x21, 0x0, 0x0)
    OP_0D()

    #C0847
    ChrTalk(
        0x101,
        "#11P#0000F……那么，还有其它问题吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0848
    ChrTalk(
        0x21,
        "#6P老师！我想到了一个问题！\x02",
    )

    CloseMessageWindow()
    OP_68(152480, 1500, 13840, 2000)
    SetCameraDistance(29120, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    #C0849
    ChrTalk(
        0x101,
        "#11P#0000F好的，请说。\x02",
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x21,
        "#6P这个问题我以前就想问了……\x02",
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x21,
        (
            "#6P像哥哥们这样的警察组织，\x01",
            "跟游击士协会有什么区别呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x21,
        (
            "#6P你们不都是\x01",
            "抓坏人的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x101,
        (
            "#11P#0003F（来了个比较棘手的问题呢……）\x02\x03",

            "#0000F嗯，但是大家都很在意，\x01",
            "就趁这个机会说清楚吧。\x02\x03",

            "#0003F我们警察与游击士\x01",
            "的本质区别是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0854
    AnonymousTalk(
        0xFF,
        (
            "警察与游击士\x01",
            "的本质区别是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①是否有逮捕权】\x01",                  # 0
            "【②是否有对政府权力的干涉力】\x01",      # 1
            "【③基本没有】\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11180"),
        (1, "loc_112D2"),
        (2, "loc_11432"),
        (SWITCH_DEFAULT, "loc_11565"),
    )


    label("loc_11180")


    #C0855
    ChrTalk(
        0x101,
        "#11P#0000F……大概是逮捕权的有无吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0856
    ChrTalk(
        0x101,
        (
            "#11P#0011F不、不对，游击士也有\x01",
            "一般的逮捕权力。\x02\x03",

            "#0003F──那个，游击士不能\x01",
            "直接逮捕国家或\x01",
            "自治州的政府要员。\x02\x03",

            "当然，在其突然施暴，伤害他人\x01",
            "的场合，还是可以无视规定，\x01",
            "直接逮捕的。\x02\x03",

            "#0001F相对地，\x01",
            "警察拥有逮捕政治家\x01",
            "以及政府官员的权力……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11565")

    label("loc_112D2")


    #C0857
    ChrTalk(
        0x101,
        (
            "#11P#0004F虽然对你们来说还有点太难了……\x01",
            "但简单来说，游击士会被『规章』所约束。\x02\x03",

            "正是因为有这个规章的存在，\x01",
            "游击士协会\x01",
            "才能设立于大陆各国……\x02\x03",

            "#0000F──那个，游击士不能\x01",
            "直接逮捕国家或\x01",
            "自治州的政府要员。\x02\x03",

            "当然，在其突然施暴，伤害他人\x01",
            "的场合，还是可以无视规定，\x01",
            "直接逮捕的。\x02\x03",

            "#0003F相对的，\x01",
            "警察拥有逮捕政治家\x01",
            "以及政府官员的权力……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_11565")

    label("loc_11432")


    #C0858
    ChrTalk(
        0x101,
        "#11P#0004F……基本没有。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0859
    ChrTalk(
        0x101,
        (
            "#11P#0011F（喂，怎么可能！）\x02\x03",

            "#0003F──那个，游击士不能\x01",
            "直接逮捕国家或\x01",
            "自治州的政府要员。\x02\x03",

            "当然，在其突然施暴，伤害他人\x01",
            "的场合，还是可以无视规定，\x01",
            "直接逮捕的。\x02\x03",

            "#0001F相对的，\x01",
            "警察拥有逮捕政治家\x01",
            "以及政府官员的权力……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11565")

    label("loc_11565")


    #C0860
    ChrTalk(
        0x21,
        (
            "#6P哎，但是爸爸\x01",
            "总是抱怨警察不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x21,
        (
            "#6P说他们连贪污的政府官员\x01",
            "都逮捕不了，真是没用。\x02",
        )
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x15,
        (
            "#12P真、真是的，隆。\x01",
            "你太失礼了啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x101,
        (
            "#11P#0006F……嗯。\x01",
            "我们的努力还远远不够，这也是事实。\x02\x03",

            "#0000F虽说不能立刻解决这些问题，\x01",
            "但我们会继续努力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x21,
        "#6P哦，我也会给你们加油的！\x02",
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x15,
        (
            "#12P真是的……\x01",
            "说得那么嚣张。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x12C)
    OP_6F(0x79)

    #C0866
    ChrTalk(
        0x101,
        (
            "#11P#0012F哈哈……\x01",
            "嗯，那么，\x01",
            "提问就到这里了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0867
    ChrTalk(
        0x153,
        (
            "#6P#1109F#N──那个、那个！！\x01",
            "琪雅也有问题！有问题！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(153250, 1500, 11180, 2000)
    SetCameraDistance(29120, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    #C0868
    ChrTalk(
        0x101,
        (
            "#11P#0011F琪、琪雅……！？\x01",
            "（本来还以为她肯乖乖待着呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x153,
        "#6P#1105F喂，我可以提问吗？\x02",
    )

    CloseMessageWindow()

    #C0870
    ChrTalk(
        0x101,
        "#11P#0000F嗯，可以啊。\x02",
    )

    CloseMessageWindow()

    #C0871
    ChrTalk(
        0x153,
        (
            "#6P#1110F那个，罗伊德……\x02\x03",

            "你为什么要成为警察呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0872
    ChrTalk(
        0x101,
        (
            "#11P#0005F（啊……）\x02\x03",

            "#0003F那、那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0873
    ChrTalk(
        0x101,
        (
            "#11P#0008F（来到特别任务支援科的第一天晚上……\x01",
            "　好像也思考过类似的事情呢。）\x02\x03",

            "#0004F（……嗯，我觉得如今\x01",
            "　已经可以回答这个问题了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0874
    ChrTalk(
        0x153,
        "#6P#1105F罗伊德？怎么了？\x02",
    )

    CloseMessageWindow()

    #C0875
    ChrTalk(
        0x101,
        (
            "#11P#0002F……不，没什么。\x02\x03",

            "#0003F（这个问题，\x01",
            "　肯定没有『正确的答案』。）\x02\x03",

            "（只有将自己在支援科逐渐产生的\x01",
            "　真实心情坦率地告诉大家……\x01",
            "　以此作为回答。）\x02\x03",

            "#0000F我成为警察的理由，\x01",
            "就是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0876
    AnonymousTalk(
        0xFF,
        (
            "罗伊德成为警察的理由是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①想要变强】\x01",          # 0
            "【②想要守护大家】\x01",      # 1
            "【③自己也不知道】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11AAD"),
        (1, "loc_11C6E"),
        (2, "loc_11DEE"),
        (SWITCH_DEFAULT, "loc_11FF5"),
    )


    label("loc_11AAD")


    #C0877
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯，到底该怎么回答呢？\x01",
            "有点让人犹豫呢……\x02\x03",

            "#0000F大概是因为……\x01",
            "想要帮助有困难的人，\x01",
            "以及阻止做坏事的人吧。\x02\x03",

            "#0008F为了做到那点，\x01",
            "我自己也必须变强……\x02\x03",

            "要想实现这个愿望的话，\x01",
            "对我来说，就只有成为警察了……\x02\x03",

            "#0012F……哈哈，但那样一来，\x01",
            "似乎跟游击士没有什么区别呢。\x02\x03",

            "#0006F对不起……\x01",
            "我好像没法回答得很清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x153,
        (
            "#6P#1104F嗯，但琪雅好像还是明白了什么。\x02\x03",

            "#1110F罗伊德一定有\x01",
            "自己的理由吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x101,
        (
            "#11P#0002F哈哈……嗯，\x01",
            "那倒是没错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FF5")

    label("loc_11C6E")


    #C0880
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯，到底该怎么回答呢？\x01",
            "有点让人犹豫呢……\x02\x03",

            "#0000F大概是因为……\x01",
            "想要守护大家吧。\x02\x03",

            "#0008F朋友和家人自不必说，\x01",
            "不过，我所指的大家并不仅限于此，\x01",
            "该说是……\x02\x03",

            "克洛斯贝尔的市民吗？\x01",
            "不，也不单是那样……\x02\x03",

            "#0006F……对不起……\x01",
            "我好像没法回答得很清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x153,
        (
            "#6P#1104F嗯，但琪雅好像还是明白了什么。\x02\x03",

            "#1110F罗伊德一定有\x01",
            "自己的理由吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x101,
        (
            "#11P#0002F哈哈……嗯。\x01",
            "那倒是没错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FF5")

    label("loc_11DEE")


    #C0883
    ChrTalk(
        0x101,
        (
            "#11P#0006F老实说……\x01",
            "我现在，还不是很清楚。\x02\x03",

            "#0008F一开始，只是想\x01",
            "追赶上自己的目标，\x01",
            "所以才想像那个人一样成为警察的……\x02\x03",

            "但现在认真想想的话，\x01",
            "其实理由并不只是那样……\x02\x03",

            "#0003F当然，想要超越大哥的\x01",
            "这份心情还是没有改变，\x01",
            "但也并不只是单纯的想要超越他……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0884
    ChrTalk(
        0x101,
        (
            "#11P#0011F对、对不起，各位。\x01",
            "好像对你们说了些奇怪的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x153,
        (
            "#6P#1110F嗯，但琪雅好像还是明白了什么。\x02\x03",

            "#1109F罗伊德在努力思考\x01",
            "一些很重要的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x101,
        (
            "#0002F哈哈……\x01",
            "谢谢你，琪雅。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FF5")

    label("loc_11FF5")

    OP_68(151640, 2100, 12440, 2000)
    MoveCamera(329, 14, 0, 2000)
    SetCameraDistance(30960, 2000)
    OP_93(0x101, 0xB4, 0x12C)
    OP_6F(0x79)
    OP_93(0xC, 0x87, 0x12C)

    #C0887
    ChrTalk(
        0xC,
        (
            "#5P呵呵……好了，提问\x01",
            "就到这里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0888
    ChrTalk(
        0xC,
        (
            "#5P那么，罗伊德老师的课\x01",
            "就此结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0xC,
        "#5P同学们，请向老师表示感谢。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("孩子们")

    #A0890
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5S谢谢老师～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0891
    ChrTalk(
        0x101,
        "#11P#0000F哈哈……那么，再见了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x153, 0x4)
    OP_D5(0x1E)
    Return()

    # Function_45_D235 end

    def Function_46_12118(): pass

    label("Function_46_12118")

    OP_95(0xFE, 151000, 200, 17500, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_46_12118 end

    def Function_47_12134(): pass

    label("Function_47_12134")

    OP_93(0xFE, 0x10E, 0x12C)
    OP_98(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_47_12134 end

    def Function_48_12157(): pass

    label("Function_48_12157")

    OP_68(7710, 2300, -90, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(26410, 0)
    SetChrPos(0xC, 7600, 0, 1320, 270)
    SetChrPos(0x101, 5570, 0, 1350, 90)
    SetChrPos(0xEF, 4380, 0, 2050, 90)
    SetChrPos(0x153, 4720, 0, 510, 90)
    Sleep(500)
    PlayBGM("ed7124", 0)
    SetCameraDistance(25410, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1231A")

    #C0892
    ChrTalk(
        0xC,
        (
            "#12P辛苦了，罗伊德，\x01",
            "今天真是太谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0893
    ChrTalk(
        0xC,
        (
            "#12P孩子们好像也都\x01",
            "听得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x101,
        (
            "#5P#0009F哈哈……\x01",
            "如果真是那样就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0xC,
        "#12P呵呵，没必要那么谦虚哦。\x02",
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0xC,
        (
            "#12P你教得非常不错了，\x01",
            "连我都学到了很多东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0xC,
        (
            "#12P看到站在讲台上的你，\x01",
            "感觉到你的成长，\x01",
            "真是比什么都要高兴。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x1)
    Jump("loc_124FF")

    label("loc_1231A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1241D")

    #C0898
    ChrTalk(
        0xC,
        (
            "#12P辛苦了，罗伊德，\x01",
            "今天真是太谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0xC,
        (
            "#12P孩子们好像也都\x01",
            "听得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x101,
        (
            "#5P#0000F哈哈……\x01",
            "如果真是那样就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0xC,
        (
            "#12P呵呵，我也\x01",
            "学到了很多东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0902
    ChrTalk(
        0xC,
        (
            "#12P看到站在讲台的你，\x01",
            "感觉到你的成长，\x01",
            "真是比什么都要高兴。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x2)
    Jump("loc_124FF")

    label("loc_1241D")


    #C0903
    ChrTalk(
        0xC,
        (
            "#12P辛苦了，罗伊德，\x01",
            "今天真是太谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0904
    ChrTalk(
        0xC,
        (
            "#12P但是，你的学习似乎\x01",
            "有点不足呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0x101,
        (
            "#5P#0006F那、那个……\x01",
            "真是对不起。\x02\x03",

            "我为自己的知识不足\x01",
            "而感到十分羞愧。\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0xC,
        (
            "#12P不，在那么忙的时候还麻烦你，\x01",
            "是我考虑不周呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x3)

    label("loc_124FF")

    TurnDirection(0x153, 0x101, 500)

    #C0907
    ChrTalk(
        0x153,
        (
            "#5P#1109F琪雅觉得罗伊德上的课\x01",
            "很有趣哦！\x02\x03",

            "#1100F虽然你说的大部分话\x01",
            "都不太能听懂。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_1257A():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1257A)
    Sleep(50)

    def lambda_1258A():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1258A)
    Sleep(1000)

    #C0908
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯……对孩子来说，\x01",
            "这些东西果然还是太难了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_125D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_125D7)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1275D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_126AC")

    #C0909
    ChrTalk(
        0x102,
        (
            "#5P#0103F真是的，必须得再加把劲了。\x02\x03",

            "#0111F虽然出了那么多丑，\x01",
            "不过，从某种意义上来说，\x01",
            "孩子们反而会觉得警察更加亲切吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0910
    ChrTalk(
        0x101,
        "#12P#0006F这、这么说，结果也不算太坏吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12758")

    label("loc_126AC")


    #C0911
    ChrTalk(
        0x102,
        (
            "#5P#0104F呵呵，能够\x01",
            "顺利完成，真是太好了。\x02\x03",

            "#0100F我想，孩子们对警察的感觉\x01",
            "一定比以前更加亲近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0912
    ChrTalk(
        0x101,
        (
            "#12P#0004F……嗯，光是能够得到\x01",
            "这样的机会，就算是一种收获了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12758")

    Jump("loc_12A54")

    label("loc_1275D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_128CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_12824")

    #C0913
    ChrTalk(
        0x103,
        (
            "#5P#0203F……确实是一堂\x01",
            "令人深感兴趣的课。\x02\x03",

            "#0211F从某种意义上说，倒也让他们\x01",
            "感受到警察只是很平易近人的存在了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x101,
        "#12P#0006F这、这么说，结果也不算太坏吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_128CA")

    label("loc_12824")


    #C0915
    ChrTalk(
        0x103,
        (
            "#5P#0204F能够顺利结束，\x01",
            "真是太好了。\x02\x03",

            "#0202F而且似乎也让孩子们\x01",
            "对警察留下了一个良好的印象。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x101,
        (
            "#12P#0004F……嗯，光是能够得到\x01",
            "这样的机会，就算是一种收获了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128CA")

    Jump("loc_12A54")

    label("loc_128CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12A54")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_129AB")

    #C0917
    ChrTalk(
        0x104,
        (
            "#5P#0306F唉，没想到你竟然把\x01",
            "那些乱七八糟的东西教给孩子。\x02\x03",

            "#0309F不过，在某种意义上说，\x01",
            "也算是在小鬼们的心目中\x01",
            "树立了警察的良好形象吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x101,
        "#12P#0006F这、这么说，结果也不算太坏吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A54")

    label("loc_129AB")


    #C0919
    ChrTalk(
        0x104,
        (
            "#5P#0300F算啦，能够顺利结束就好，\x01",
            "别想那么多了。\x02\x03",

            "#0309F小鬼们似乎\x01",
            "对警察留下了\x01",
            "很好的印象嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0920
    ChrTalk(
        0x101,
        (
            "#12P#0004F……嗯，光是能够得到\x01",
            "这样的机会，就算是一种收获了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A54")


    def lambda_12A59():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A59)

    def lambda_12A66():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_12A66)

    def lambda_12A73():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_12A73)

    #C0921
    ChrTalk(
        0xC,
        (
            "#12P……那么，\x01",
            "我还要回去上课，\x01",
            "就先失陪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0922
    ChrTalk(
        0xC,
        (
            "#12P小琪雅，\x01",
            "如果方便的话，\x01",
            "以后也请来主日学校哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0923
    ChrTalk(
        0xC,
        (
            "#12P其他的孩子\x01",
            "肯定也会欢迎你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0924
    ChrTalk(
        0x153,
        (
            "#5P#1110F嗯！今天虽然很忙……\x01",
            "但以后一定还会再来的～！\x02",
        )
    )

    CloseMessageWindow()

    #C0925
    ChrTalk(
        0x101,
        (
            "#5P#0000F（哈哈……琪雅似乎\x01",
            "　很喜欢主日学校呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_12CDF")
    OP_2C(0x27, 0x3)

    #C0926
    ChrTalk(
        0xC,
        "#12P呵呵，我会期待你的到来哦。\x02",
    )

    CloseMessageWindow()

    #C0927
    ChrTalk(
        0xC,
        (
            "#12P……对了对了，罗伊德\x01",
            "你能收下这个吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0928
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x61),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('神圣挂坠', 1)

    #C0929
    ChrTalk(
        0x101,
        "#5P#0005F您太客气了……真的可以收下吗？\x02",
    )

    CloseMessageWindow()

    #C0930
    ChrTalk(
        0xC,
        (
            "#12P你已经很忙了，但还是抽空给我们上了\x01",
            "一堂如此精彩的课，这只是谢礼而已。\x01",
            "不要客气，请收下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0931
    ChrTalk(
        0xC,
        "#12P……那么，再见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D1D")

    label("loc_12CDF")


    #C0932
    ChrTalk(
        0xC,
        "#12P呵呵，我会期待着你的到来哦。\x02",
    )

    CloseMessageWindow()

    #C0933
    ChrTalk(
        0xC,
        "#12P那么，再见了。\x02",
    )

    CloseMessageWindow()

    label("loc_12D1D")

    BeginChrThread(0xC, 3, 0, 49)
    WaitChrThread(0xC, 3)

    #C0934
    ChrTalk(
        0x101,
        (
            "#5P#0003F……好了，\x01",
            "稍微耗去了\x01",
            "一点时间……\x02\x03",

            "#0000F差不多也该去医院了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12DC4")

    #C0935
    ChrTalk(
        0x102,
        (
            "#5P#0100F说得也是哦，\x01",
            "我们快点去\x01",
            "南出口的巴士站吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E59")

    label("loc_12DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12E16")

    #C0936
    ChrTalk(
        0x103,
        (
            "#5P#0200F……说得也是呢，\x01",
            "我们快点去\x01",
            "南出口的巴士站吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E59")

    label("loc_12E16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12E59")

    #C0937
    ChrTalk(
        0x104,
        (
            "#5P#0300F是啊，\x01",
            "我们快点去\x01",
            "南出口的巴士站吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E59")


    #C0938
    ChrTalk(
        0x153,
        "#5P#1110F嗯，走吧！\x02",
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0939
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【主日学校的特别讲师】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5570, 0, 1350, 90)
    SetChrPos(0xC, 150800, 200, 17500, 180)
    OP_29(0x27, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_48_12157 end

    def Function_49_12EF5(): pass

    label("Function_49_12EF5")


    def lambda_12EFA():
        OP_95(0xFE, 8600, 0, 1320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12EFA)
    WaitChrThread(0xC, 1)

    def lambda_12F18():
        OP_95(0xFE, 8600, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12F18)
    WaitChrThread(0xC, 1)

    def lambda_12F36():
        OP_95(0xFE, 11600, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12F36)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_12F59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_12F59)
    WaitChrThread(0xC, 1)
    Return()

    # Function_49_12EF5 end

    def Function_50_12F6A(): pass

    label("Function_50_12F6A")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    Return()

    # Function_50_12F6A end

    def Function_51_12F83(): pass

    label("Function_51_12F83")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_63(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x21, 0x2)
    Sleep(300)
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x15, 0x1)
    Sleep(200)
    OP_63(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Return()

    # Function_51_12F83 end

    def Function_52_12FF5(): pass

    label("Function_52_12FF5")

    OP_64(0xFFFF)
    SetChrSubChip(0x21, 0x0)
    SetChrSubChip(0x15, 0x0)
    Return()

    # Function_52_12FF5 end

    SaveToFile()

Try(main)
