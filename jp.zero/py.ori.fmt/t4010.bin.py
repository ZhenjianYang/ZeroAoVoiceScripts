from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "エラルダ大司教",         # 1
        "ジーナス司祭",           # 2
        "レントン司祭",           # 3
        "シスター・ハティナ",     # 4
        "シスター・マーブル",     # 5
        "貿易商モルジオ",         # 6
        "ノエル曹長",             # 7
        "タミル",                 # 8
        "ハミル",                 # 9
        "モモ",                   # 10
        "パンセ",                 # 11
        "クータ",                 # 12
        "ユゴット",               # 13
        "アンリ",                 # 14
        "観光客タクト",           # 15
        "男の子",                 # 16
        "女の子",                 # 17
        "男の子",                 # 18
        "女の子",                 # 19
        "男の子",                 # 20
        "女の子",                 # 21
        "ハロルド",               # 22
        "ソフィア",               # 23
        "コリン",                 # 24
        "レイテ",                 # 25
        "リュウ",                 # 26
        "SE制御",                 # 27
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
        "Function_6_1CF7",         # 06, 6
        "Function_7_1F5F",         # 07, 7
        "Function_8_290A",         # 08, 8
        "Function_9_3625",         # 09, 9
        "Function_10_3F75",        # 0A, 10
        "Function_11_3F79",        # 0B, 11
        "Function_12_526D",        # 0C, 12
        "Function_13_53A9",        # 0D, 13
        "Function_14_5CC6",        # 0E, 14
        "Function_15_6784",        # 0F, 15
        "Function_16_6845",        # 10, 16
        "Function_17_6CC6",        # 11, 17
        "Function_18_719C",        # 12, 18
        "Function_19_7463",        # 13, 19
        "Function_20_76A1",        # 14, 20
        "Function_21_78B3",        # 15, 21
        "Function_22_7A84",        # 16, 22
        "Function_23_7C27",        # 17, 23
        "Function_24_7E15",        # 18, 24
        "Function_25_7FAF",        # 19, 25
        "Function_26_8179",        # 1A, 26
        "Function_27_82CA",        # 1B, 27
        "Function_28_8404",        # 1C, 28
        "Function_29_856C",        # 1D, 29
        "Function_30_86E2",        # 1E, 30
        "Function_31_8CBA",        # 1F, 31
        "Function_32_8E06",        # 20, 32
        "Function_33_8FFE",        # 21, 33
        "Function_34_92F4",        # 22, 34
        "Function_35_94CB",        # 23, 35
        "Function_36_95C5",        # 24, 36
        "Function_37_9868",        # 25, 37
        "Function_38_9B28",        # 26, 38
        "Function_39_BD46",        # 27, 39
        "Function_40_BD89",        # 28, 40
        "Function_41_C944",        # 29, 41
        "Function_42_D42F",        # 2A, 42
        "Function_43_D65E",        # 2B, 43
        "Function_44_E297",        # 2C, 44
        "Function_45_EB0C",        # 2D, 45
        "Function_46_14409",       # 2E, 46
        "Function_47_14425",       # 2F, 47
        "Function_48_14448",       # 30, 48
        "Function_49_15388",       # 31, 49
        "Function_50_153FD",       # 32, 50
        "Function_51_15416",       # 33, 51
        "Function_52_15488",       # 34, 52
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB3")

    #C0001
    ChrTalk(
        0x8,
        (
            "遺跡にあった鐘……\x01",
            "さて、どうしたものか……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "（鐘がアーティファクトだとすると……\x01",
            "  あの者たちがでしゃばってくる\x01",
            "  可能性が高い。）\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "（……フン、させるものか。\x01",
            "  あのような者たちのクロスベル入りを\x01",
            "  断じて認めるわけにはいかん。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B09")

    label("loc_AB3")


    #C0004
    ChrTalk(
        0x8,
        (
            "……ふむ、まぁよい。\x01",
            "あの遺跡と《星見の塔》に関しては\x01",
            "こちらでも調べるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B09")

    Jump("loc_1CF3")

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B29")
    Call(0, 6)
    Jump("loc_B7F")

    label("loc_B29")


    #C0005
    ChrTalk(
        0x8,
        (
            "“悪魔”のようなものを呼び出す鐘……\x01",
            "そんなものがあの遺跡に\x01",
            "あったというのか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7F")

    Jump("loc_1CF3")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C45")

    #C0006
    ChrTalk(
        0x8,
        "マフィアの抗争があったそうだな。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "市民が巻き込まれなかったことが\x01",
            "なによりであったが……愚かな事を……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "女神よ、争いの因果から\x01",
            "人々を解き放たんことを……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CAD")

    label("loc_C45")


    #C0009
    ChrTalk(
        0x8,
        (
            "罪もない市民が巻き込まれず\x01",
            "本当によかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "女神よ、争いの因果から\x01",
            "人々を解き放たんことを……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAD")

    Jump("loc_1CF3")

    label("loc_CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D79")

    #C0011
    ChrTalk(
        0x8,
        (
            "……ふむ……気のせいか、\x01",
            "山道の方から鐘の音が聞こえた気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "はて、マインツの方角に\x01",
            "鐘つき台などはなかったはずだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        (
            "#0505F（……鐘……？\x01",
            "  少し気になりますね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF3")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_EDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E72")

    #C0014
    ChrTalk(
        0x8,
        (
            "シスター・マーブルと\x01",
            "話していたようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "……用は済んだのかね？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0000Fは、はい。\x01",
            "貴重な情報をいただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……よろしい。\x01",
            "またいつでも来なさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "空の女神#8Rエ イ ド ス#よ、彼らを導きたまえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EDA")

    label("loc_E72")


    #C0019
    ChrTalk(
        0x8,
        (
            "困った事があったら\x01",
            "いつでも訪れるがよかろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "空の女神#8Rエ イ ド ス#よ、彼らを導きたまえ……\x02",
    )

    CloseMessageWindow()

    label("loc_EDA")

    Jump("loc_1CF3")

    label("loc_EDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_112A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DD")

    #C0021
    ChrTalk(
        0x8,
        (
            "クロスベル大聖堂に\x01",
            "よくぞいらっしゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        (
            "#1110F……あ、おひげー！\x01",
            "ねぇねぇ、さわってイイ？\x02",
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
        "む……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0011Fちょ、き、キーア！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_FF6")

    #C0025
    ChrTalk(
        0x102,
        (
            "#0103Fも、申し訳ありません大司教。\x01",
            "うちの子がとんだ粗相を……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1068")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1039")

    #C0026
    ChrTalk(
        0x103,
        (
            "#0203F……失礼しました。\x01",
            "何分まだ子供でして……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1068")

    label("loc_1039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1068")

    #C0027
    ChrTalk(
        0x104,
        "#0303Fす、すんませんッス大司教。\x02",
    )

    CloseMessageWindow()

    label("loc_1068")


    #C0028
    ChrTalk(
        0x8,
        "いや……気にするでない。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "子供は活発なのに\x01",
            "越したことはないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "女神よ、この子に祝福を……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1125")

    label("loc_10DD")


    #C0031
    ChrTalk(
        0x8,
        "子供は活発なのに越したことはない。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "女神よ、この子に祝福を……\x02",
    )

    CloseMessageWindow()

    label("loc_1125")

    Jump("loc_1CF3")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CC")

    #C0033
    ChrTalk(
        0x8,
        (
            "さて……\x01",
            "今夜のミサを終えたら\x01",
            "創立記念祭中の行事も終わりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "今年も多くの参拝者が訪れた。\x01",
            "彼らに女神の祝福があらんことを……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_121C")

    label("loc_11CC")


    #C0035
    ChrTalk(
        0x8,
        (
            "今年の記念祭にも\x01",
            "多くの参拝者が訪れた。\x01",
            "彼らに女神の祝福があらんことを……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121C")

    Jump("loc_1CF3")

    label("loc_1221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_13AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1335")

    #C0036
    ChrTalk(
        0x8,
        (
            "帝国の政府要人らしき男が\x01",
            "夜遅くに大聖堂を訪れてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "七耀教会の影響力を見越して、\x01",
            "大司教の私に取り入ろうと\x01",
            "していたようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        "一喝して追い出してやったよ。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "空の女神#8Rエ イ ド ス#の僕たる私は\x01",
            "あくまで中立にいる必要があるのでな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13A9")

    label("loc_1335")


    #C0040
    ChrTalk(
        0x8,
        (
            "七耀教会はこの大陸に住む人々に\x01",
            "強く根付いている。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "それを政治に利用しようなど\x01",
            "女神への侮辱だと思うのだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    Jump("loc_1CF3")

    label("loc_13AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1546")

    #C0042
    ChrTalk(
        0x8,
        (
            "昨晩、旧市街のほうで\x01",
            "大きな乱闘騒ぎがあったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "旧市街の若者だけかと思いきや、\x01",
            "なんと遊撃士や警察も\x01",
            "一緒になって暴れていたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0005F（ギクッ……）\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "……ふぅ、やはり君たちか。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "祭りというのは人を昂ぶらせ、\x01",
            "時として冷静な判断力を失わせる。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "警察がそんなことではいかんぞ。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0306Fす、すんません……\x02\x03",

            "（この爺さん、\x01",
            "  妙な威圧感があるぜ……！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15B8")

    label("loc_1546")


    #C0049
    ChrTalk(
        0x8,
        (
            "……まぁ、昨日の件は\x01",
            "大きな怪我人が出なかっただけ\x01",
            "幸いと言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "これからは重々、慎むがよかろう。\x02",
    )

    CloseMessageWindow()

    label("loc_15B8")

    Jump("loc_1CF3")

    label("loc_15BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_177E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F8")

    #C0051
    ChrTalk(
        0x8,
        (
            "創立７０周年、か。\x01",
            "考えてみれば長い歴史だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "辛いこと、悲しいこと……\x01",
            "この自治州には色々なことがあった。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "人々は思い思いに\x01",
            "この時を過ごしているのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "……ふむ。\x01",
            "私もただミサだけをして\x01",
            "過ごすわけにも行くまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "初心に帰って、調薬の教本でも\x01",
            "読んでいるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1779")

    label("loc_16F8")


    #C0056
    ChrTalk(
        0x8,
        (
            "私もただミサだけをして\x01",
            "この７０周年の日を\x01",
            "過ごすわけにも行くまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "初心に帰って、調薬の教本でも\x01",
            "読んでいるとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1779")

    Jump("loc_1CF3")

    label("loc_177E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_18FE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_179C")
    Call(0, 42)
    Jump("loc_18F9")

    label("loc_179C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_17B1")
    Call(0, 40)
    Jump("loc_18F9")

    label("loc_17B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188B")

    #C0058
    ChrTalk(
        0x8,
        (
            "空の女神に祈る時、人の心は\x01",
            "もっとも清らかになるという。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "苦悩から解き放たれ、\x01",
            "閉じたまぶたの暗闇の中で\x01",
            "己を見つめなおす時を与えられる……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "……君たちもよければ\x01",
            "ミサに参加していくのだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18F9")

    label("loc_188B")


    #C0061
    ChrTalk(
        0x8,
        (
            "空の女神に祈る時、人の心は\x01",
            "もっとも清らかになるという。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "君たちもよければ\x01",
            "ミサに参加していくのだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F9")

    Jump("loc_1CF3")

    label("loc_18FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A59")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_191C")
    Call(0, 42)
    Jump("loc_1A54")

    label("loc_191C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1931")
    Call(0, 40)
    Jump("loc_1A54")

    label("loc_1931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")

    #C0063
    ChrTalk(
        0x8,
        (
            "本日はこの大聖堂で\x01",
            "ミサが開かれるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "空の女神は人々の営みを見守り、\x01",
            "我々に命を与えてくれる……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "かの女神への感謝を忘れないためにも、\x01",
            "ミサという行事は大切なのだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A54")

    label("loc_19F8")


    #C0066
    ChrTalk(
        0x8,
        (
            "本日はこの大聖堂で\x01",
            "ミサが開かれるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "君たちも女神への感謝を\x01",
            "忘れぬようにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A54")

    Jump("loc_1CF3")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B51")

    #C0068
    ChrTalk(
        0x8,
        (
            "君たち、特務支援課の活動……\x01",
            "小さな声ではあるが聞き及んでいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "世では遊撃士の模倣だと\x01",
            "揶揄されているようだが……\x01",
            "気にすることはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "空の女神は、\x01",
            "正しき信念の下に行動する者を\x01",
            "決して見捨てはしないだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BEA")

    label("loc_1B51")


    #C0071
    ChrTalk(
        0x8,
        (
            "人を助けようとする者がいるということは\x01",
            "それだけでこの世の財産と言える。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "空の女神は、\x01",
            "正しき信念の下に行動する者を\x01",
            "決して見捨てはしないだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEA")

    Jump("loc_1CF3")

    label("loc_1BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1CF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C98")

    #C0073
    ChrTalk(
        0x8,
        (
            "このクロスベル大聖堂に\x01",
            "よくぞいらっしゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "どうやら、これから\x01",
            "山に足を踏み入れる様子だな？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "空の女神よ、彼らを導きたまえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CF3")

    label("loc_1C98")


    #C0076
    ChrTalk(
        0x8,
        (
            "七耀の教えは必ずや君たちを\x01",
            "迷いから救うだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "空の女神よ、彼らを導きたまえ……\x02",
    )

    CloseMessageWindow()

    label("loc_1CF3")

    TalkEnd(0x8)
    Return()

    # Function_5_9A2 end

    def Function_6_1CF7(): pass

    label("Function_6_1CF7")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0x8, 0xE, 0)
    TurnDirection(0xE, 0x8, 0)

    #C0078
    ChrTalk(
        0xE,
        (
            "#0501F……これが遺跡内部の\x01",
            "調査報告書です。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "魔物を呼び出す鐘……\x01",
            "あの遺跡にそんなものがあるとは……\x02",
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
            "確かに古代遺物#8Rアーティファクト#である可能性は\x01",
            "高いかもしれんな……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "ふむ、伝えていただき感謝する。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xE,
        "#0500Fはっ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F53")

    #C0084
    ChrTalk(
        0x10A,
        (
            "#0604F警備隊のノエル曹長か……\x01",
            "礼儀正しく有能な若手のホープと聞く。\x02\x03",

            "#0602F……フン、少しは\x01",
            "彼女の勤勉さを見習ったらどうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0310F（う……\x01",
            "  ティオすけ、明らかに俺たちを\x01",
            "  ピンポイントで攻撃してやがるぞ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        (
            "#0211F（心外な……攻撃されているのは\x01",
            "  ランディさんだけでしょう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F53")

    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_6_1CF7 end

    def Function_7_1F5F(): pass

    label("Function_7_1F5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2020")

    #C0087
    ChrTalk(
        0xFE,
        (
            "朝方、警備隊のノエル曹長殿が\x01",
            "クロスベルの遺跡についての報告書を\x01",
            "届けてくれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "アーティファクトが\x01",
            "関与している可能性がある以上……\x01",
            "教会も黙って見過ごせませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_2020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_20B1")

    #C0089
    ChrTalk(
        0xFE,
        (
            "……ノエル殿の言う鐘が\x01",
            "どのようなものであるか\x01",
            "気になりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "そして、なぜその鐘は突然音を\x01",
            "鳴らし始めたのでしょう……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_20B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_213D")

    #C0091
    ChrTalk(
        0xFE,
        (
            "市内の建物で事件が起きたことに\x01",
            "エラルダ大司教は深く悲しんでいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "非道徳な行いは大司教の\x01",
            "最も嫌うことですから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21EB")

    #C0093
    ChrTalk(
        0xFE,
        (
            "今日はシスター・ハティナが\x01",
            "旧市街の方へ勉強を\x01",
            "教えに行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "旧市街の子供たちは\x01",
            "日曜学校に来ないものですから、\x01",
            "こちらから出向いているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_21EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_22CF")

    #C0095
    ChrTalk(
        0xFE,
        (
            "教会に伝わる《法術》と\x01",
            "ウルスラ病院の近代医療……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "心と体、それぞれの分野に特化して\x01",
            "人々を癒していくこの二つは、\x01",
            "現在あまり連携がとれていません。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "今だ近代医療が発展途上という\x01",
            "背景もあるのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_22CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_23A1")

    #C0098
    ChrTalk(
        0xFE,
        (
            "記念祭が終わってから一週間ほど、\x01",
            "街は平和そのものでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "何人かの市民は、\x01",
            "何かピリピリとしたものを感じて\x01",
            "お祈りに来ているようでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "何かが起こっていたのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_23A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_242E")

    #C0101
    ChrTalk(
        0xFE,
        (
            "今年も沢山の人々が\x01",
            "ミサに訪れました。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "来年の記念祭の時にも\x01",
            "彼らが晴れやかな気持ちで\x01",
            "この場所を訪れられますように……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_242E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2479")

    #C0103
    ChrTalk(
        0xFE,
        (
            "空の女神よ、迷える子羊たちに\x01",
            "正しき道を示さんことを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_2479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_251C")

    #C0104
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教は調薬の分野でも\x01",
            "高い功績を残しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院の薬のいくつかは\x01",
            "大司教が昔調合したものを元に\x01",
            "処方されているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_251C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_25E4")

    #C0106
    ChrTalk(
        0xFE,
        (
            "初日に、記念祭の成功を祈りに\x01",
            "マクダエル市長とハルトマン議長が\x01",
            "お見えになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "対立が目されるお２人ですが、\x01",
            "願わくばクロスベル市民のために\x01",
            "手を取り合ってほしいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_25E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C3")

    #C0108
    ChrTalk(
        0xFE,
        (
            "ハロルドさん一家は\x01",
            "よくこの聖堂を訪れては、\x01",
            "熱心に祈っていかれるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "空の女神への信仰を忘れない……\x01",
            "大変よい心がけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "大いなる空の女神よ、\x01",
            "敬虔なる彼らに加護を与えたまえ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_2700")

    label("loc_26C3")


    #C0111
    ChrTalk(
        0xFE,
        (
            "大いなる空の女神よ、\x01",
            "敬虔なる彼らに加護を与えたまえ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2700")

    Jump("loc_2906")

    label("loc_2705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_27BB")

    #C0112
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのディーター殿は\x01",
            "お祈りに来る時はいつも\x01",
            "巨大なリムジンを走らせてきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "何度か轢かれかけたのですが、\x01",
            "あの笑顔で爽やかに謝られると\x01",
            "なんだか怒れません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_27BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2857")

    #C0114
    ChrTalk(
        0xFE,
        (
            "この大聖堂には時折、\x01",
            "クロスベル市の市長殿も\x01",
            "お見えになります。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "仕事の合間をぬって\x01",
            "クロスベル市の平和を\x01",
            "お祈りになっているようです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2906")

    #C0116
    ChrTalk(
        0xFE,
        (
            "七耀教会は遥か昔、\x01",
            "大崩壊直後の時代から\x01",
            "人々に光を与えてきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "この大聖堂も七耀教会施設の一つ……\x01",
            "空の女神は迷いし者に\x01",
            "正しい道を示してくれるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2906")

    TalkEnd(0xFE)
    Return()

    # Function_7_1F5F end

    def Function_8_290A(): pass

    label("Function_8_290A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2AB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1A")

    #C0118
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教は\x01",
            "古代遺物を取り扱う機関\x01",
            "《封聖省》を快く思っていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "封聖省の組織である《星杯騎士団》は\x01",
            "裏で色々と後ろ暗いことをしている\x01",
            "という噂だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "非合法活動を嫌う\x01",
            "エラルダ大司教にとっては\x01",
            "許せない存在に違いないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AB3")

    label("loc_2A1A")


    #C0121
    ChrTalk(
        0xFE,
        (
            "封聖省の組織である《星杯騎士団》を\x01",
            "エラルダ大司教は快く思っていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "非合法活動を嫌う\x01",
            "エラルダ大司教にとっては\x01",
            "許せない存在に違いないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB3")

    Jump("loc_3621")

    label("loc_2AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B03")

    #C0123
    ChrTalk(
        0xFE,
        (
            "本日は日曜学校は休みになっているよ。\x01",
            "とても静かだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2BBE")

    #C0124
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教も、今回の事件について\x01",
            "強い憤りを感じているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "今回は市民に被害はなかったけど、\x01",
            "抗争なんていう利己的な理由で\x01",
            "皆を不安にさせるなんて許せないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CA4")

    #C0126
    ChrTalk(
        0xFE,
        (
            "教会の聖典には“悪魔”という存在が\x01",
            "伝わっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "それは女神と対をなす存在であり、\x01",
            "時には人の心の隙間に入り込んで\x01",
            "悪事を働かせると言われている。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "我々教会の者にとって\x01",
            "戒めの象徴であるのは確かだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2D4F")

    #C0129
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルは\x01",
            "昔からこの大聖堂に勤めていてね。\x01",
            "七耀教会では中々顔が広いんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "その上人柄もいいから\x01",
            "彼女を頼って訪れる人も少なくないのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2DA9")

    #C0131
    ChrTalk(
        0xFE,
        (
            "ふぅ……エラルダ大司教に\x01",
            "しっかり働いてもらえるように\x01",
            "しとかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E35")

    #C0132
    ChrTalk(
        0xFE,
        (
            "創立記念祭も今日で終わり、\x01",
            "明日から日曜学校も再開される。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "子供たちに会えるとなると\x01",
            "俄然やる気がでるというものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2F16")

    #C0134
    ChrTalk(
        0xFE,
        (
            "大司教と言う役職は、\x01",
            "七耀教会でもかなり発言力が強い。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "特にエラルダ大司教は\x01",
            "典礼省という七耀教会の機関の\x01",
            "有力者なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "不正などには絶対手を貸さないから、\x01",
            "私達下の者も信頼して\x01",
            "ついていけるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2FAF")

    #C0137
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのディーター総裁は\x01",
            "その資金力を生かして\x01",
            "様々な慈善活動をなさっているそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "教会関係者として\x01",
            "ただただ感服するばかりだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3621")

    label("loc_2FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309F")

    #C0139
    ChrTalk(
        0xFE,
        (
            "よくこの聖堂にいらっしゃる\x01",
            "貿易商のモルジオさんだが……\x01",
            "少し女神に依存しすぎているね。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "彼は祈りを捧げたおかげで\x01",
            "成功したと言っているが……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "自分の努力すら\x01",
            "『女神のおかげ』なんてのは\x01",
            "どうかと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3143")

    label("loc_309F")


    #C0142
    ChrTalk(
        0xFE,
        (
            "よくこの聖堂にいらっしゃる\x01",
            "貿易商のモルジオさんだが……\x01",
            "少し女神に依存しすぎているね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "司祭の私が言うのもなんだが\x01",
            "女神に頼りすぎるのは\x01",
            "良くないと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3143")

    Jump("loc_3621")

    label("loc_3148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3352")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_31CE")

    #C0144
    ChrTalk(
        0xA,
        (
            "さて……あのルピナス草が\x01",
            "病院の役に立てばいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院には\x01",
            "我々七耀教会も期待してるのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334D")

    label("loc_31CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3254")

    #C0146
    ChrTalk(
        0xA,
        (
            "まぁ、大司教は頑固だけど……\x01",
            "分別は弁えてる方だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "ラゴー教授の実力だけは\x01",
            "ちゃんと認めているってわけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334D")

    label("loc_3254")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3269")
    Call(0, 41)
    Jump("loc_334D")

    label("loc_3269")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_32D4")

    #C0148
    ChrTalk(
        0xA,
        "おや、何の用だい？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "ここはエラルダ大司教の執務室だ。\x01",
            "無闇に入っちゃいけないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334D")

    label("loc_32D4")


    #C0150
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教は\x01",
            "七耀教会に関する本も\x01",
            "いくつか出していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "簡潔に纏められていて\x01",
            "分かりやすいと評判なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334D")

    Jump("loc_3621")

    label("loc_3352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_34C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3460")

    #C0152
    ChrTalk(
        0xFE,
        (
            "旧市街にいる不良グループ、\x01",
            "『サーベルバイパー』に\x01",
            "『テスタメンツ』と言ったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "特にテスタメンツの子達は\x01",
            "まるで宗教団体のような\x01",
            "出で立ちをしているそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "まったく嘆かわしいことだよ。\x01",
            "出来れば更正する機会を得て欲しいものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34C1")

    label("loc_3460")


    #C0155
    ChrTalk(
        0xFE,
        (
            "サーベルバイパーに\x01",
            "テスタメンツの子供たち……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "出来れば更正する機会を得て欲しいものだ。\x02",
    )

    CloseMessageWindow()

    label("loc_34C1")

    Jump("loc_3621")

    label("loc_34C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358E")

    #C0157
    ChrTalk(
        0xFE,
        "エラルダ大司教は実に厳格な方でね。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "非道な行いには厳しくあたり、\x01",
            "それでいて迷いのある者には\x01",
            "優しく手を差し伸べられる……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "私も司祭として\x01",
            "かくありたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3621")

    label("loc_358E")


    #C0160
    ChrTalk(
        0xFE,
        (
            "非道な行いには厳しくあたり、\x01",
            "それでいて迷いのある者には\x01",
            "優しく手を差し伸べられる……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教はそんな方だ。\x01",
            "かくありたいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3621")

    TalkEnd(0xFE)
    Return()

    # Function_8_290A end

    def Function_9_3625(): pass

    label("Function_9_3625")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3694")

    #C0162
    ChrTalk(
        0xFE,
        (
            "明日は朝一で\x01",
            "鉱山町マインツに出張です。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "子供たちが\x01",
            "元気にしているといいのですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_3694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3742")

    #C0164
    ChrTalk(
        0xFE,
        (
            "明日は鉱山町マインツへ\x01",
            "日曜学校の出張に行くので、\x01",
            "授業内容について話していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "出張は大変ですけど、\x01",
            "普段会えない子供たちと会えるので\x01",
            "楽しみです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_3742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_37C2")

    #C0166
    ChrTalk(
        0xFE,
        (
            "本日は普段より参拝者の数が\x01",
            "多いように思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "港街区の騒ぎで、\x01",
            "街の方々も不安を感じているようです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_37C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_37D0")
    Jump("loc_3F71")

    label("loc_37D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3841")

    #C0168
    ChrTalk(
        0xFE,
        (
            "……その様子ですと\x01",
            "なにか収穫があったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "ふふ、さすがシスター・マーブルですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_3841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3913")

    #C0170
    ChrTalk(
        0xFE,
        "何かお困りごとでしょうか？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "でしたら、大司教や\x01",
            "シスター・マーブルに\x01",
            "相談されるとよいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "お２人とも長く教会につとめて\x01",
            "いらっしゃいますから、\x01",
            "きっといいアドバイスを頂けますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_3913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3992")

    #C0173
    ChrTalk(
        0xFE,
        (
            "創立記念祭も残すところ\x01",
            "今日までですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#よ、\x01",
            "このまま無事に終わりますように……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_3992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A38")

    #C0175
    ChrTalk(
        0xFE,
        (
            "昨日は驚きました。\x01",
            "大司教にあんな話を\x01",
            "持ち掛けてくるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "このクロスベル自治州が持つ闇は\x01",
            "予想以上に根深いのかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3AB2")

    label("loc_3A38")


    #C0177
    ChrTalk(
        0xFE,
        (
            "一教区の大司教を\x01",
            "大胆にも取り込もうなどと……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "このクロスベル自治州が持つ闇は\x01",
            "予想以上に根深いのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB2")

    Jump("loc_3F71")

    label("loc_3AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B4E")

    #C0179
    ChrTalk(
        0xFE,
        (
            "シスター・ジュジュは\x01",
            "おっちょこちょいですが料理は上手です。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "ふふ……\x01",
            "子供たちは彼女のクッキーに\x01",
            "誘われてやって来るのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_3B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C46")

    #C0181
    ChrTalk(
        0xFE,
        (
            "昨日は記念祭初日とあって\x01",
            "多くの人がミサに訪れました。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "過去幾度となく起こった紛争で\x01",
            "失われた魂を悼む……\x01",
            "そんな人々が多かったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "この７０年という契機に\x01",
            "クロスベル自治州は\x01",
            "どうなっていくのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3CD9")

    label("loc_3C46")


    #C0184
    ChrTalk(
        0xFE,
        (
            "クロスベルに住む人々に根強く残るのは\x01",
            "やはり、紛争の記憶でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "この７０年という契機に\x01",
            "クロスベル自治州は\x01",
            "どうなっていくのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD9")

    Jump("loc_3F71")

    label("loc_3CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3CEC")
    Jump("loc_3F71")

    label("loc_3CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9D")

    #C0186
    ChrTalk(
        0xFE,
        (
            "七耀教会の施設では、\x01",
            "子供たちに勉強を教える\x01",
            "『日曜学校』が開かれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "今日もシスター・マーブルが\x01",
            "日曜学校の授業を\x01",
            "行っているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3E24")

    label("loc_3D9D")


    #C0188
    ChrTalk(
        0xFE,
        (
            "この大聖堂での日曜学校は、\x01",
            "以前からシスター・マーブルが\x01",
            "担当しているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "私も明日、旧市街の方へ\x01",
            "出張する予定なのです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E24")

    Jump("loc_3F71")

    label("loc_3E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F05")

    #C0190
    ChrTalk(
        0xFE,
        (
            "何でも、世間では\x01",
            "狼型魔獣が人々を騒がせているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "多くの人にとって魔獣は不安の種です。\x01",
            "それが人を襲うとあらば尚更……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "これよりもっとひどいことが\x01",
            "起こらなければいいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3F71")

    label("loc_3F05")


    #C0193
    ChrTalk(
        0xFE,
        (
            "狼型魔獣の被害……\x01",
            "怪我人も出ていると聞きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "もっとひどいことが\x01",
            "起こらなければいいのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F71")

    TalkEnd(0xFE)
    Return()

    # Function_9_3625 end

    def Function_10_3F75(): pass

    label("Function_10_3F75")

    Call(0, 11)
    Return()

    # Function_10_3F75 end

    def Function_11_3F79(): pass

    label("Function_11_3F79")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F92")
    Call(0, 38)
    Jump("loc_5269")

    label("loc_3F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4031")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3FB4")
    Jump("loc_4029")

    label("loc_3FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3FC2")
    Jump("loc_4029")

    label("loc_3FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3FD0")
    Jump("loc_4029")

    label("loc_3FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3FDE")
    Jump("loc_4029")

    label("loc_3FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3FEC")
    Jump("loc_4029")

    label("loc_3FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3FFA")
    Jump("loc_4029")

    label("loc_3FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4008")
    Jump("loc_4029")

    label("loc_4008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4020")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4029")

    label("loc_4020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4029")

    label("loc_4029")

    Call(0, 13)
    Jump("loc_5269")

    label("loc_4031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_40C8")

    #C0195
    ChrTalk(
        0xC,
        (
            "ロイド、エリィ……\x01",
            "再会できてとても嬉しいのですが\x01",
            "現在は授業中なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "もしよかったら、\x01",
            "授業がない日に改めてお話しましょう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5269")

    label("loc_40C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D6")

    #C0197
    ChrTalk(
        0xC,
        (
            "警備隊の調査にあなた達も\x01",
            "協力したそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xC,
        (
            "ふふ、いろいろな場所で大活躍ね。\x01",
            "ロイドたちの元先生として鼻が高いわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        "今度、日曜学校で自慢しちゃおうかしら。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0006Fはは……\x01",
            "勘弁してくださいよ、先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        "#0113F本当ですよ、もう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4282")

    label("loc_41D6")


    #C0202
    ChrTalk(
        0xC,
        "ふふ、あなたたちが自慢なのは本当よ。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "私が教えたロイドやエリィが、\x01",
            "市民の模範となって正義の姿を見せる……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xC,
        (
            "これほど素晴らしい事はないと\x01",
            "思っているのですから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4282")

    Jump("loc_5269")

    label("loc_4287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_43CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4359")
    OP_93(0xC, 0x10E, 0x0)

    #C0205
    ChrTalk(
        0xC,
        (
            "そうね……マインツの辺りは\x01",
            "クロスベルの経済を昔から支えてきた\x01",
            "背景を持っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xC,
        (
            "小さな子供たちがその事を\x01",
            "誇りに思えるように、\x01",
            "歴史を教えてあげるのはどうでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43C7")

    label("loc_4359")


    #C0207
    ChrTalk(
        0xC,
        (
            "あらロイド、エリィ……\x01",
            "今日はどんな用かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xC,
        (
            "少し立て込んでいるから、\x01",
            "またあとで来てちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C7")

    Jump("loc_5269")

    label("loc_43CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_457C")

    #C0209
    ChrTalk(
        0xC,
        (
            "あら、ロイドにエリィ……\x01",
            "何かあったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xC,
        "深刻そうな顔をしているけど……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#0008F……いえ、なんでもないんです。\x02\x03",

            "#0003F（こんな錠剤がクロスベル市内で\x01",
            "  見つかったなんて、\x01",
            "  さすがに相談できないしな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        (
            "……とにかく、\x01",
            "いつでも笑っていることよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "あなたたちの元気がないと\x01",
            "特務支援課に期待している人達が\x01",
            "不安になってしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#0103F……そうですね。\x01",
            "ありがとうございます、先生……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4604")

    label("loc_457C")


    #C0215
    ChrTalk(
        0xC,
        (
            "あなたたちがそんな顔をしていると\x01",
            "特務支援課に期待している人達が\x01",
            "不安になってしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        "どんなときでも笑顔を忘れないようにね。\x02",
    )

    CloseMessageWindow()

    label("loc_4604")

    Jump("loc_5269")

    label("loc_4609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_48E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4877")
    OP_93(0xC, 0xB4, 0x0)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x0, 500)

    #C0217
    ChrTalk(
        0xC,
        "あら、ロイド……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xC,
        (
            "キーアさん、病院への検査入院を\x01",
            "拒んでしまったんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#0006Fええ……\x01",
            "すみません、せっかくの勧めを\x01",
            "無下にする形に……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "あらあら、いいのよ。\x01",
            "子供に無理を強いてはいけないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "いつか機会は来ますから\x01",
            "気長に待つことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        "#0100Fそうですね……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x1B,
        (
            "マーブル先生～。\x01",
            "授業中におしゃべりしていいの～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x1B, 500)

    #C0224
    ChrTalk(
        0xC,
        (
            "あらあら、\x01",
            "ごめんなさいね。\x01",
            "先生としたことが……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x104,
        "#0305Fおっと……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x103,
        "#0200Fすっかり邪魔してしまいましたね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0227
    ChrTalk(
        0xC,
        (
            "（そういうことだから……\x01",
            "  今度、授業のない日にでも\x01",
            "  ゆっくり話しましょうね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48E4")

    label("loc_4877")

    OP_93(0xC, 0xB4, 0x0)

    #C0228
    ChrTalk(
        0xC,
        (
            "ええっと……\x01",
            "どこまで説明したかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xC,
        (
            "うふふ、歳をとると\x01",
            "忘れがちになってしまってダメねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E4")

    Jump("loc_5269")

    label("loc_48E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_4A30")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AC")

    #C0230
    ChrTalk(
        0xC,
        (
            "お疲れ様、ロイド。\x01",
            "今日は本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "キーアちゃんも。\x01",
            "よかったら、また日曜学校に\x01",
            "いらっしゃいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x153,
        "#1109Fうん！　分かった～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A23")

    label("loc_49AC")


    #C0233
    ChrTalk(
        0xC,
        (
            "キーアちゃん。\x01",
            "もしよかったら、これからも\x01",
            "日曜学校にいらっしゃいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        (
            "他の子供たちも\x01",
            "きっと歓迎してくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A23")

    Jump("loc_4A2B")

    label("loc_4A28")

    Call(0, 43)

    label("loc_4A2B")

    Jump("loc_4B82")

    label("loc_4A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0A")

    #C0235
    ChrTalk(
        0xC,
        (
            "私の《法術》でこれ以上\x01",
            "キーアさんの記憶を掘り起こすのは\x01",
            "難しいでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "聖ウルスラ病院の\x01",
            "『神経科』部門の先生なら\x01",
            "詳しい事が分かるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        "一度相談してみるといいでしょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B82")

    label("loc_4B0A")


    #C0238
    ChrTalk(
        0xC,
        (
            "聖ウルスラ病院なら\x01",
            "キーアさんの記憶について\x01",
            "詳しい事が分かるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xC,
        "一度相談してみるといいでしょう。\x02",
    )

    CloseMessageWindow()

    label("loc_4B82")

    Jump("loc_5269")

    label("loc_4B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4B98")
    Call(0, 38)
    Jump("loc_5269")

    label("loc_4B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C20")

    #C0240
    ChrTalk(
        0xC,
        "明日からの授業の内容を考えているのよ。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xC,
        (
            "そうね、外国の風土などを教えるのも\x01",
            "面白いかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C98")

    label("loc_4C20")


    #C0242
    ChrTalk(
        0xC,
        (
            "外国の風土などを教えるのも\x01",
            "面白いかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "同じゼムリア大陸でも\x01",
            "国によって随分と文化が違っているし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C98")

    Jump("loc_5269")

    label("loc_4C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB8")
    Call(0, 12)
    Jump("loc_4D38")

    label("loc_4CB8")


    #C0244
    ChrTalk(
        0xC,
        (
            "ふふ、日曜学校はお休みなのに\x01",
            "わざわざ迎えに来てくれるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "講師を長く続けてるけど、\x01",
            "いつの時代も子供は可愛いわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D38")

    Jump("loc_5269")

    label("loc_4D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E03")

    #C0246
    ChrTalk(
        0xC,
        (
            "日曜学校がない日は\x01",
            "次の授業の内容を\x01",
            "考えたりしているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "でも時々、休みの日にも\x01",
            "子供たちが遊びに来てくれる\x01",
            "こともあったりして……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        "ふふ、思ったより賑やかなのですよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5269")

    label("loc_4E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E6E")

    #C0249
    ChrTalk(
        0xC,
        "ふふ、記念祭は楽しんでいるかしら？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        (
            "あなた達も暇があったら\x01",
            "お祈りしていくといいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5269")

    label("loc_4E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8E")

    #C0251
    ChrTalk(
        0xC,
        (
            "最近は、定期的に日曜学校を\x01",
            "大聖堂の外に出張させているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "アルモリカ村や鉱山町マインツ、\x01",
            "旧市街に住んでいる子供たちは\x01",
            "なかなか足を運んでくれませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "最近ではシスター・ハティナが\x01",
            "その役を手伝ってくれていて、\x01",
            "とても助かっているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_501E")

    label("loc_4F8E")


    #C0254
    ChrTalk(
        0xC,
        (
            "今日は、シスター・ハティナが\x01",
            "旧市街の方へ出張に行ってくれているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        (
            "あの辺りの子はなかなか日曜学校に\x01",
            "来てくれなくて、大変なのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_501E")

    Jump("loc_5269")

    label("loc_5023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_516F")
    OP_93(0xC, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F4")

    #C0256
    ChrTalk(
        0xC,
        "大昔に起きた《大崩壊》……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        (
            "それはこのゼムリア大陸を\x01",
            "壊滅させてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "その時、高度な技術力を持った\x01",
            "古代ゼムリア文明も\x01",
            "共に失われたと言われているのです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_516A")

    label("loc_50F4")


    #C0259
    ChrTalk(
        0xC,
        (
            "《大崩壊》はその名の通り\x01",
            "ゼムリア大陸を壊滅させ……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "──ふう、この子たちったら\x01",
            "ちゃんと聞いてるのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_516A")

    Jump("loc_5269")

    label("loc_516F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51FD")

    #C0261
    ChrTalk(
        0xC,
        (
            "私は今でも、\x01",
            "現役で日曜学校の先生を\x01",
            "任されているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "よかったら時々\x01",
            "授業の様子を見に来てくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5269")

    label("loc_51FD")


    #C0263
    ChrTalk(
        0xC,
        (
            "今の子供たちも、\x01",
            "とても可愛い子達ばかりなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "よかったら時々\x01",
            "授業の様子を見に来てくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5269")

    TalkEnd(0xC)
    Return()

    # Function_11_3F79 end

    def Function_12_526D(): pass

    label("Function_12_526D")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_93(0xC, 0xB4, 0x0)
    TurnDirection(0xF, 0xC, 0)
    TurnDirection(0x10, 0xC, 0)

    #C0265
    ChrTalk(
        0xF,
        "あとで俺達、街に行こうと思ってるんだ。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xF,
        (
            "色々な出店が出てて\x01",
            "楽しそうだしシスターも行こうぜ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "あらあら、\x01",
            "それはうらやましいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        "でも私はミサで忙しいから行けないわ。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xC,
        "皆さんで楽しんできて頂戴ね。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xF,
        "ちぇ、そっか……\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x10,
        "うう、残念だね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_12_526D end

    def Function_13_53A9(): pass

    label("Function_13_53A9")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550E")
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(500)

    #C0272
    ChrTalk(
        0xC,
        "あら、どちら様でしょう？\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0000F#5Pあ、すみません。\x01",
            "授業風景を見ていたら\x01",
            "何だか懐かしくなってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        (
            "#0105F（……あら？\x01",
            "  このシスター、どこかで……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5567")

    label("loc_550E")


    #C0275
    ChrTalk(
        0x102,
        (
            "#0105F（……あら？\x01",
            "  このシスター、どこかで……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_5567")


    #C0276
    ChrTalk(
        0xC,
        (
            "……まぁ……\x01",
            "あなた、もしかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "──ロイド。\x01",
            "ロイド・バニングスでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x101,
        "#0005F#5Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#0300Fなんだロイド、知り合いか？\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#0002F#5Pも、もしかして……\x01",
            "マーブル先生！？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        "久しぶりですね、ロイド。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    #C0282
    ChrTalk(
        0xC,
        (
            "それに……\x01",
            "そちらはエリィでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        (
            "ふふ……二人とも\x01",
            "すっかり大人になって……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#0109Fやっぱり……！\x01",
            "お久しぶりです、先生。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0285
    ChrTalk(
        0x101,
        (
            "#0000F#11Pえっと……もしかして\x01",
            "エリィもマーブル先生のことを？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0286
    ChrTalk(
        0x102,
        (
            "#0102Fえぇ、私も日曜学校時代は\x01",
            "先生に教わっていたの。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0287
    ChrTalk(
        0x103,
        (
            "#0205F#5Pロイドさんとエリィさんは\x01",
            "歳が近かったはずですが……\x02\x03",

            "同じシスターに授業を受けていたのに\x01",
            "互いのことを知らなかったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        (
            "クロスベル市は広いですから\x01",
            "街区ごとに日曜学校がある日が\x01",
            "違っているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        (
            "ロイドとエリィは別々の日に\x01",
            "受け持っていたのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        "#0300Fな～るほどな。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#0104F……なんだか変な感じね。\x02\x03",

            "#0102Fもしかしたらあなたと\x01",
            "幼馴染だったかもしれないなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#0009F#11Pはは、それもそうだな。\x02",
    )

    CloseMessageWindow()

    def lambda_592B():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_592B)
    Sleep(50)

    def lambda_593B():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_593B)

    def lambda_5948():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5948)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0293
    ChrTalk(
        0x101,
        (
            "#0002F#5Pそれにしても、マーブル先生。\x01",
            "よく俺たちのことを覚えていましたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xC,
        (
            "ふふ……\x01",
            "私は受け持った生徒のことは\x01",
            "一人だって忘れたことはないのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "それに、あなた達ときたら\x01",
            "特に個性的な子供でしたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#0205F#5P個性的……ですか？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        "そう。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "ロイドはお姉さんにべったりの\x01",
            "甘えん坊さんだったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        (
            "エリィはとても子供には見えない\x01",
            "耳年増というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#0011F#5Pちょ、ちょっと！？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        "#0112F先生……！\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x104,
        (
            "#0304Fほっほ～う、\x01",
            "他人の過去話ってのは面白いねぇ。\x02\x03",

            "#0309Fそんで、具体的にはどんなエピソードが？\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xC,
        "そうね、例えば──\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#0012F#5Pか、勘弁してくださいよ先生……！\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#0113F全くです。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        "ふふ、冗談ですよ。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        "#0206F#5P……残念です。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "……ロイド、エリィ。\x01",
            "あなた達に再会できたのは\x01",
            "私にとっても嬉しいことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "よかったらいつでも\x01",
            "会いに来てくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#0002F#5P……はい！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 149440, 200, 17150, 90)
    SetScenarioFlags(0x8C, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC3")
    SetScenarioFlags(0x0, 4)

    label("loc_5CC3")

    EventEnd(0x5)
    Return()

    # Function_13_53A9 end

    def Function_14_5CC6(): pass

    label("Function_14_5CC6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D5A")
    Jump("loc_5DA4")

    label("loc_5D5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D7A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DA4")

    label("loc_5D7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D9A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DA4")

    label("loc_5D9A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DA4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5E53")

    #C0311
    ChrTalk(
        0xFE,
        (
            "……あのご夫人、\x01",
            "よく聖堂に顔を出しているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "敬虔なのは大事なことだよ。\x01",
            "僕もその心を忘れないようにしたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_5E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5EA2")

    #C0313
    ChrTalk(
        0xFE,
        (
            "おや……警備隊の人が\x01",
            "大聖堂に来てるのなんて初めて見たなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_5EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5F47")

    #C0314
    ChrTalk(
        0xFE,
        (
            "マフィアどもめ……\x01",
            "あのあたりでドンパチ始めるなんて\x01",
            "とんでもないやつらだ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "おお女神よ……商売熱心な我々を、\x01",
            "不慮の毒牙から護りたまえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_5F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6011")

    #C0316
    ChrTalk(
        0xFE,
        (
            "次の商売の目玉は、\x01",
            "マインツから取り寄せる\x01",
            "七耀石にしようと思っているのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "新しい商品に手を出すのは\x01",
            "いささか怖いが……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "なぁに、きっと空の女神は\x01",
            "私に微笑んでくれるはずさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_6011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6074")

    #C0319
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#よ……\x01",
            "来年の記念祭もどうか、\x01",
            "よろしくお願いします……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_6074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_612D")

    #C0320
    ChrTalk(
        0xFE,
        (
            "今年の記念祭では\x01",
            "かなりの収益が出たよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "例年に比べて\x01",
            "観光客が多かったおかげかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#に\x01",
            "熱心に祈りを捧げた甲斐が\x01",
            "あったと言うものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_612D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_61C9")

    #C0323
    ChrTalk(
        0xFE,
        (
            "今日は最終日……\x01",
            "客の多くがミシュラムに流れる\x01",
            "いまこそが商売のチャンスだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#よ……\x01",
            "私に商機をもたらしたまえ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_61C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6258")

    #C0325
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#よ……\x01",
            "今年はまさに絶好調。\x01",
            "商品が飛ぶように売れていきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "ああ、感謝してもしきれません……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_6258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_62D1")

    #C0327
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#よ……\x01",
            "昨日の売り上げも\x01",
            "なかなかのものでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        "ああ、感謝いたします……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_62D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_643B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C2")

    #C0329
    ChrTalk(
        0xFE,
        (
            "仕事は忙しいけど……\x01",
            "ミサにはバッチリ参加するつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "なんたって、\x01",
            "空の女神#8Rエ イ ド ス#に祈ったお陰で\x01",
            "今の私がある訳だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "こういった行事には\x01",
            "欠かさず参加して、\x01",
            "感謝の気持ちを示したいんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6436")

    label("loc_63C2")


    #C0332
    ChrTalk(
        0xFE,
        "今の私があるのは空の女神#8Rエ イ ド ス#のお陰……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "こういった行事に欠かさず参加するのは\x01",
            "当然のことだろう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6436")

    Jump("loc_677C")

    label("loc_643B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_654B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64EF")

    #C0334
    ChrTalk(
        0xFE,
        "来月はいよいよ創立記念祭……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "私たち貿易商にとっては\x01",
            "書き入れ時なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "さぁ、今年も繁盛するよう、\x01",
            "空の女神#8Rエ イ ド ス#に祈らねば……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6546")

    label("loc_64EF")


    #C0337
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#よ……\x01",
            "今度の創立記念祭でも\x01",
            "どうかご加護をお願いします……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6546")

    Jump("loc_677C")

    label("loc_654B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65FD")

    #C0338
    ChrTalk(
        0xFE,
        "うむうむ、子供たちがいると賑やかでいい。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        "以前は子供など大嫌いだったんだが……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "ここで祈って商売に成功してから\x01",
            "心が広くなった気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_667E")

    label("loc_65FD")


    #C0341
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#に祈ることで\x01",
            "私の商売は成功し、心まで広くなった。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "この場所には感謝しなくちゃな。\x01",
            "はっはっは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_667E")

    Jump("loc_677C")

    label("loc_6683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_677C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_672B")

    #C0343
    ChrTalk(
        0xFE,
        (
            "私は貿易商をしているのだが……\x01",
            "以前ここで祈った直後に\x01",
            "商売が大成功してな。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "以来、ちょくちょく\x01",
            "お祈りさせてもらいに来ているのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_677C")

    label("loc_672B")


    #C0345
    ChrTalk(
        0xFE,
        (
            "おお、空の女神#8Rエ イ ド ス#よ……\x01",
            "次の商売も是非\x01",
            "上手くいかせて下さい……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_677C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_5CC6 end

    def Function_15_6784(): pass

    label("Function_15_6784")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A2")
    Call(0, 6)
    Jump("loc_6841")

    label("loc_67A2")


    #C0346
    ChrTalk(
        0xE,
        (
            "#0502Fあ、支援課の皆さん……\x02\x03",

            "#0504F今しがた、大司教に\x01",
            "あの遺跡の件について\x01",
            "報告したところです。\x02\x03",

            "#0508Fこれで調査に更なる進展があれば\x01",
            "いいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6841")

    TalkEnd(0xFE)
    Return()

    # Function_15_6784 end

    def Function_16_6845(): pass

    label("Function_16_6845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6853")
    Jump("loc_6CC5")

    label("loc_6853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6861")
    Jump("loc_6CC5")

    label("loc_6861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_686F")
    Jump("loc_6CC5")

    label("loc_686F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_687D")
    Jump("loc_6CC5")

    label("loc_687D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6A71")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_691A")
    Jump("loc_6964")

    label("loc_691A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_693A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6964")

    label("loc_693A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_695A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6964")

    label("loc_695A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6964")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A0F")

    #C0347
    ChrTalk(
        0xFE,
        (
            "ちぇっ、さっきの授業で\x01",
            "普通の授業が潰れると\x01",
            "思ったのにな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "シスター、こういうとこは\x01",
            "抜け目無いんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A65")

    label("loc_6A0F")


    #C0349
    ChrTalk(
        0xFE,
        (
            "ふ～……\x01",
            "今日が日曜学校って\x01",
            "すっかり忘れてたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        "あ～あ、外で遊びたいな～。\x02",
    )

    CloseMessageWindow()

    label("loc_6A65")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_6CC5")

    label("loc_6A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6A7F")
    Jump("loc_6CC5")

    label("loc_6A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6B18")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A9D")
    Call(0, 12)
    Jump("loc_6B10")

    label("loc_6A9D")


    #C0351
    ChrTalk(
        0xFE,
        (
            "ちぇっ……\x01",
            "折角街を案内してあげようと\x01",
            "思ったのにさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "ハミルとはいつも一緒だから\x01",
            "新鮮味がないんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B10")

    TalkEnd(0xFE)
    Jump("loc_6CC5")

    label("loc_6B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6B26")
    Jump("loc_6CC5")

    label("loc_6B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6B34")
    Jump("loc_6CC5")

    label("loc_6B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6B42")
    Jump("loc_6CC5")

    label("loc_6B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6CBC")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BDF")
    Jump("loc_6C29")

    label("loc_6BDF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BFF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C29")

    label("loc_6BFF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C1F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C29")

    label("loc_6C1F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C29")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C60")
    Call(0, 18)
    Jump("loc_6CB0")

    label("loc_6C60")


    #C0353
    ChrTalk(
        0xFE,
        (
            "ちぇっ、タミルのやつ\x01",
            "ちょっと勉強が出来るからって\x01",
            "いい気になっちゃって……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CB0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_6CC5")

    label("loc_6CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6CC5")

    label("loc_6CC5")

    Return()

    # Function_16_6845 end

    def Function_17_6CC6(): pass

    label("Function_17_6CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6CD4")
    Jump("loc_719B")

    label("loc_6CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6CE2")
    Jump("loc_719B")

    label("loc_6CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CF0")
    Jump("loc_719B")

    label("loc_6CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6CFE")
    Jump("loc_719B")

    label("loc_6CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6F01")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D9B")
    Jump("loc_6DE5")

    label("loc_6D9B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6DBB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DE5")

    label("loc_6DBB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DDB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DE5")

    label("loc_6DDB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6DE5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6E79")

    #C0354
    ChrTalk(
        0xFE,
        (
            "も～、タミルったら\x01",
            "さっきはあんなに\x01",
            "張り切ってたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "ケジメが大事だよ、ケジメが。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EF5")

    label("loc_6E79")

    SetChrSubChip(0xFE, 0x2)

    #C0356
    ChrTalk(
        0xFE,
        (
            "も～、タミルったら\x01",
            "さっきまで\x01",
            "散々遊んでたじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "ケジメが大事だって\x01",
            "いつもシスターが\x01",
            "言ってるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_719B")

    label("loc_6F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6F0F")
    Jump("loc_719B")

    label("loc_6F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6FCA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F2D")
    Call(0, 12)
    Jump("loc_6FC2")

    label("loc_6F2D")


    #C0358
    ChrTalk(
        0xFE,
        (
            "お世話になってるマーブル先生と\x01",
            "一緒に出店を回りたかったけど……\x01",
            "忙しいなら仕方ないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "先生にアイスクリームとか\x01",
            "おごってあげたかったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FC2")

    TalkEnd(0xFE)
    Jump("loc_719B")

    label("loc_6FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6FD8")
    Jump("loc_719B")

    label("loc_6FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6FE6")
    Jump("loc_719B")

    label("loc_6FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6FF4")
    Jump("loc_719B")

    label("loc_6FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7015")
    TalkBegin(0xFE)
    Call(0, 18)
    TalkEnd(0xFE)
    Jump("loc_718D")

    label("loc_7015")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_70A9")
    Jump("loc_70F3")

    label("loc_70A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70C9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70F3")

    label("loc_70C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70E9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70F3")

    label("loc_70E9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70F3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0360
    ChrTalk(
        0xFE,
        (
            "双子のタミルは\x01",
            "勉強がてんでダメなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "ちょっと運動ができるからって\x01",
            "日曜学校じゃいい顔させないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_718D")

    Jump("loc_719B")

    label("loc_7192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_719B")

    label("loc_719B")

    Return()

    # Function_17_6CC6 end

    def Function_18_719C(): pass

    label("Function_18_719C")

    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x10, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7230")
    Jump("loc_727A")

    label("loc_7230")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7250")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_727A")

    label("loc_7250")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7270")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_727A")

    label("loc_7270")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_727A")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0362
    ChrTalk(
        0xF,
        (
            "なー、ハミル。\x01",
            "お前マーブル先生が言ってたこと分かる？\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_736E")
    Jump("loc_73B8")

    label("loc_736E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_738E")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73B8")

    label("loc_738E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73AE")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73B8")

    label("loc_73AE")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73B8")

    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    #C0363
    ChrTalk(
        0x10,
        (
            "タミル、ちゃんと聞いてた？\x01",
            "そんなに難しいこと言ってなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "そ、そう……？\x01",
            "うーん、後でノート見せてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_18_719C end

    def Function_19_7463(): pass

    label("Function_19_7463")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_74F7")
    Jump("loc_7541")

    label("loc_74F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7517")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7541")

    label("loc_7517")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7537")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7541")

    label("loc_7537")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7541")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7652")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_75E3")

    #C0365
    ChrTalk(
        0xFE,
        (
            "さっきの授業……\x01",
            "むずかしかったけど、\x01",
            "たのしかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "えと……\x01",
            "ありがとうね、お兄ちゃん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_764D")

    label("loc_75E3")


    #C0367
    ChrTalk(
        0xFE,
        (
            "リュウくんとアンリくん、\x01",
            "２人といっしょに勉強できるのは\x01",
            "うれしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "今日は何の授業なんだろ……\x02",
    )

    CloseMessageWindow()

    label("loc_764D")

    Jump("loc_7699")

    label("loc_7652")


    #C0369
    ChrTalk(
        0xFE,
        (
            "大崩壊……\x01",
            "そんなことがあったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        "怖いなぁ……ぶるぶる……\x02",
    )

    CloseMessageWindow()

    label("loc_7699")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_7463 end

    def Function_20_76A1(): pass

    label("Function_20_76A1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7735")
    Jump("loc_777F")

    label("loc_7735")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7755")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_777F")

    label("loc_7755")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7775")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_777F")

    label("loc_7775")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_777F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786A")

    #C0371
    ChrTalk(
        0xFE,
        (
            "ゼムリアぶんめい……\x01",
            "うちのおとーさんとかが\x01",
            "好きそうな話ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "……それにしても、リュウとアンリは\x01",
            "今日、サボリなのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "日曜学校の日ってちゃんと\x01",
            "教えといたのにな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_78AB")

    label("loc_786A")


    #C0374
    ChrTalk(
        0xFE,
        (
            "……ま、あの２人なんかほっといて\x01",
            "ちゃんとお勉強しないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78AB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_76A1 end

    def Function_21_78B3(): pass

    label("Function_21_78B3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7947")
    Jump("loc_7991")

    label("loc_7947")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7967")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7991")

    label("loc_7967")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7987")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7991")

    label("loc_7987")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7991")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0375
    ChrTalk(
        0xFE,
        (
            "このままオーブメントが\x01",
            "進歩していったら、もっと生活が\x01",
            "楽になっちゃうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "家にいながら買い物が\x01",
            "できちゃったりして……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "……あっ！　もしそうなったら、\x01",
            "お使いのお駄賃もなくなっちゃう！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_78B3 end

    def Function_22_7A84(): pass

    label("Function_22_7A84")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7B18")
    Jump("loc_7B62")

    label("loc_7B18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B38")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B62")

    label("loc_7B38")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B58")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B62")

    label("loc_7B58")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B62")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0378
    ChrTalk(
        0xFE,
        (
            "遊撃士になったら、\x01",
            "エプスタイン財団から\x01",
            "戦術オーブメントが貰えるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "いいなぁ～。\x01",
            "ぼくもいつかは華麗に\x01",
            "アーツを扱えるようになりたいな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_7A84 end

    def Function_23_7C27(): pass

    label("Function_23_7C27")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CBB")
    Jump("loc_7D05")

    label("loc_7CBB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CDB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D05")

    label("loc_7CDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CFB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D05")

    label("loc_7CFB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D05")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7D38")
    Jump("loc_7E0D")

    label("loc_7D38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7DA5")

    #C0380
    ChrTalk(
        0xFE,
        (
            "警察のこと、\x01",
            "あまり知らなかったので\x01",
            "勉強になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "また色々教えてくださいね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E0D")

    label("loc_7DA5")


    #C0382
    ChrTalk(
        0xFE,
        (
            "あっ、さっきの……\x01",
            "キーアちゃん、だっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "やっぱり君も\x01",
            "授業を受けにきたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x153,
        "#1106Fん～？\x02",
    )

    CloseMessageWindow()

    label("loc_7E0D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_7C27 end

    def Function_24_7E15(): pass

    label("Function_24_7E15")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EA9")
    Jump("loc_7EF3")

    label("loc_7EA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EC9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EF3")

    label("loc_7EC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EE9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EF3")

    label("loc_7EE9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EF3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0385
    ChrTalk(
        0xFE,
        (
            "確か、Ｃ・エプスタイン博士の\x01",
            "莫大な遺産で作られたのが\x01",
            "エプスタイン財団だったっけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "エプスタイン博士って\x01",
            "どんな人だったんだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_7E15 end

    def Function_25_7FAF(): pass

    label("Function_25_7FAF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8043")
    Jump("loc_808D")

    label("loc_8043")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8063")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_808D")

    label("loc_8063")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8083")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_808D")

    label("loc_8083")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_808D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8138")

    #C0387
    ChrTalk(
        0xFE,
        (
            "簡単すぎて笑っちゃうわ。\x01",
            "この程度の知識は常識よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "……あっ、授業中に\x01",
            "声を掛けるなんてマナーがないわね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8171")

    label("loc_8138")


    #C0389
    ChrTalk(
        0xFE,
        (
            "もう、あっちにいって頂戴！\x01",
            "私は勉強してるんだから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8171")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_7FAF end

    def Function_26_8179(): pass

    label("Function_26_8179")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_820D")
    Jump("loc_8257")

    label("loc_820D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_822D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8257")

    label("loc_822D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_824D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8257")

    label("loc_824D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8257")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0390
    ChrTalk(
        0xFE,
        (
            "今の技術力なら\x01",
            "そんなひどい災害なんか\x01",
            "楽勝に防げるんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_8179 end

    def Function_27_82CA(): pass

    label("Function_27_82CA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_835E")
    Jump("loc_83A8")

    label("loc_835E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_837E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_83A8")

    label("loc_837E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_839E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_83A8")

    label("loc_839E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_83A8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0391
    ChrTalk(
        0xFE,
        (
            "……きゃっ。\x01",
            "あたしのノート見ないでよー！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_82CA end

    def Function_28_8404(): pass

    label("Function_28_8404")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8498")
    Jump("loc_84E2")

    label("loc_8498")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_84B8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84E2")

    label("loc_84B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84E2")

    label("loc_84D8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_84E2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0392
    ChrTalk(
        0xFE,
        "ふぁ～……勉強すると眠くなるなぁ。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "……わ、シスターが見てるや。\x01",
            "しっかりしないと。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_8404 end

    def Function_29_856C(): pass

    label("Function_29_856C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8600")
    Jump("loc_864A")

    label("loc_8600")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8620")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_864A")

    label("loc_8620")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8640")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_864A")

    label("loc_8640")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_864A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0394
    ChrTalk(
        0xFE,
        (
            "将来の為に\x01",
            "しっかり勉強なさいって\x01",
            "ママが言ってたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "……お兄ちゃんたちは\x01",
            "しっかり勉強したひと？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_856C end

    def Function_30_86E2(): pass

    label("Function_30_86E2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8776")
    Jump("loc_87C0")

    label("loc_8776")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8796")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87C0")

    label("loc_8796")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87C0")

    label("loc_87B6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87C0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 7)), scpexpr(EXPR_END)), "loc_89D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_8897")

    #C0396
    ChrTalk(
        0x1D,
        (
            "#3600F私もなるべく参加するようには\x01",
            "しているんですが……\x01",
            "仕事の都合が付かない事も多くて。\x02\x03",

            "#3603F妻にばかり負担をかけています。\x01",
            "……ダメですね、私も。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89D3")

    label("loc_8897")


    #C0397
    ChrTalk(
        0x1D,
        (
            "#3600Fミサに参加するのは\x01",
            "妻の習慣なんです。\x01",
            "毎週欠かした事はありません。\x02\x03",

            "#3603F私もなるべく参加するようには\x01",
            "しているんですが……\x01",
            "仕事の都合が付かない事も多くて。\x02\x03",

            "#3600F……はは、妻にばかり\x01",
            "負担をかけてしまっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#0005F（……………………？\x01",
            "  お祈りに来なくちゃいけない\x01",
            "  理由でもあるのかな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_89D3")

    Jump("loc_8CB2")

    label("loc_89D8")


    #C0399
    ChrTalk(
        0x1D,
        (
            "#3605Fあ、皆さん……\x02\x03",

            "#3609Fははは、珍しい所でお会いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        "#0000Fそうか、今日はミサの日ですね。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#0100Fハロルドさんもお祈りですか？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x1D,
        (
            "#3600Fええ、妻の習慣なんです。\x02\x03",

            "#3609F私はさぼりがちなんですが……\x01",
            "できるだけ時間を作って\x01",
            "来ているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x104,
        "#0309F相変わらず家族思いッスね～。\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x103,
        "#0200Fお忙しい中、マメですよね。\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x1D,
        (
            "#3609Fはは、そういうわけでは……\x02\x03",

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
            "#3603F……いえ、大したことでは。\x02\x03",

            "#3600Fその、私自身はそれほど\x01",
            "信仰が厚いわけではないですよ。\x02\x03",

            "お祈りは商売に効く、\x01",
            "なんて噂話もありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        "#0305Fあれれ、そっちの方だったんスか？\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x1D,
        "#3609Fあはははは……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 7)

    label("loc_8CB2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_86E2 end

    def Function_31_8CBA(): pass

    label("Function_31_8CBA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D4E")
    Jump("loc_8D98")

    label("loc_8D4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D6E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D98")

    label("loc_8D6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D98")

    label("loc_8D8E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D98")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0x1E, 0x0)

    #C0409
    ChrTalk(
        0x1E,
        (
            "#3700F司祭さま、それでは今日も\x01",
            "よろしくお願い致します。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_8CBA end

    def Function_32_8E06(): pass

    label("Function_32_8E06")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E9A")
    Jump("loc_8EE4")

    label("loc_8E9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8EBA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EE4")

    label("loc_8EBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EDA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EE4")

    label("loc_8EDA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8EE4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8F64")

    #C0410
    ChrTalk(
        0x1F,
        (
            "#3809Fおいの～り、おいの～り……\x02\x03",

            "パパとママが\x01",
            "いっしょでたのしいな～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FF6")

    label("loc_8F64")


    #C0411
    ChrTalk(
        0x1F,
        (
            "#3800Fきょうはママと\x01",
            "おいのりに日なんだ～。\x02\x03",

            "あのね、それでパパも\x01",
            "かけつけてきたんだよ！\x02\x03",

            "#3809Fパパ、いつもいそいで\x01",
            "はしってくるんだ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_8FF6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_8E06 end

    def Function_33_8FFE(): pass

    label("Function_33_8FFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9243")

    #C0412
    ChrTalk(
        0x102,
        "#0105Fあら……セシルさんのお母様。\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "あらあら、もしかして\x01",
            "みんなしてお祈りに来たのかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)

    #C0414
    ChrTalk(
        0xFE,
        "ロイド君……何かあったの？\x02",
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
        "#0005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        "……ううん、何でもないわ。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "ふふっ、本当に\x01",
            "ガイ君に似てきたわね。\x01",
            "夕日の中では間違えてしまいそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#0011Fあー、はは……\x01",
            "一応血のつながった兄弟だしね。\x01",
            "（……なんだ、そういう事か。）\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "ロイド君もよかったら\x01",
            "一緒にお祈りして行かないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "ここには……ガイ君も\x01",
            "眠っているんですからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_92F0")

    label("loc_9243")


    #C0421
    ChrTalk(
        0xFE,
        (
            "ロイド君は本当に\x01",
            "ガイ君に似てきたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "ふふ……きっとガイ君にも\x01",
            "負けない立派な捜査官になるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "おばさん、応援してるからね。\x01",
            "誰にも負けちゃ駄目よ、ロイド君。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92F0")

    TalkEnd(0xFE)
    Return()

    # Function_33_8FFE end

    def Function_34_92F4(): pass

    label("Function_34_92F4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9388")
    Jump("loc_93D2")

    label("loc_9388")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_93A8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93D2")

    label("loc_93A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93C8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93D2")

    label("loc_93C8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93D2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9466")

    #C0424
    ChrTalk(
        0xFE,
        (
            "兄ちゃんの授業、\x01",
            "なかなか面白かったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "またツァイトをさわりに\x01",
            "遊びに行くからな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C3")

    label("loc_9466")


    #C0426
    ChrTalk(
        0xFE,
        (
            "ちぇっ、勉強なんて\x01",
            "正直ダルいよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        "まぁ、シスターの授業は結構面白いんだけどさ。\x02",
    )

    CloseMessageWindow()

    label("loc_94C3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_92F4 end

    def Function_35_94CB(): pass

    label("Function_35_94CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9556")

    #C0428
    ChrTalk(
        0xFE,
        "女神様に旅の無事を祈りに来たんだ。\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "怪我なんかしたら、\x01",
            "せっかくの旅行が台無しだからな。\x01",
            "十分気をつけないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_95C1")

    label("loc_9556")


    #C0430
    ChrTalk(
        0xFE,
        (
            "怪我なんかで\x01",
            "旅行が台無しになったら\x01",
            "やりきれないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "念の為、もう一回\x01",
            "お祈りしておこうかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95C1")

    TalkEnd(0xFE)
    Return()

    # Function_35_94CB end

    def Function_36_95C5(): pass

    label("Function_36_95C5")

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
        "──大昔に起きた《大崩壊》……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "それはこのゼムリア大陸を\x01",
            "壊滅させてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xC,
        (
            "その時、高度な技術力を持った\x01",
            "古代ゼムリア文明も\x01",
            "共に失われたと言われているのです。\x02",
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
        "#0100F……どうやら日曜学校の授業中みたいね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_97CA")

    #C0436
    ChrTalk(
        0x101,
        (
            "#0000Fはは、懐かしいな。\x01",
            "子供たちの中には見た顔もいるし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_984D")

    label("loc_97CA")


    #C0437
    ChrTalk(
        0x101,
        (
            "#0000Fはは、懐かしいな。\x01",
            "子供たちの中には見た顔もいるし……\x02\x03",

            "#0005F（……ん？\x01",
            "  授業を教えてるシスター……\x01",
            "  もしかして……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_984D")

    SetChrPos(0x0, 147550, 0, 2900, 0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x86, 4)
    EventEnd(0x5)
    Return()

    # Function_36_95C5 end

    def Function_37_9868(): pass

    label("Function_37_9868")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(151810, 1500, 11060, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31350, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_991B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98D7")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, 149460, 0, 1750, 0)

    label("loc_98D7")

    SetChrPos(0x101, 148350, 0, 3500, 0)
    SetChrPos(0x102, 146900, 0, 3750, 0)
    SetChrPos(0x103, 148350, 0, 1920, 0)
    SetChrPos(0x104, 146900, 0, 2250, 0)

    label("loc_991B")

    OP_4B(0xC, 0xFF)
    OP_68(151810, 1500, 13060, 5000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0438
    ChrTalk(
        0xC,
        (
            "──半世紀前、\x01",
            "Ｃ・エプスタイン博士によって\x01",
            "もたらされた《導力革命》……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xC,
        (
            "初めは受け入れられなかったものの、\x01",
            "現在、私達の周りには数多くの\x01",
            "便利な《導力器#6Rオーブメント#》が存在します。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xC,
        (
            "最近では導力車などの\x01",
            "便利なものが次々と生まれており……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AF3")
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
            "#0100F……どうやら日曜学校の\x01",
            "授業中みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        (
            "#0000Fはは、懐かしいな。\x01",
            "子供たちの中には見た顔もいるし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AF3")

    SetChrPos(0x0, 147550, 0, 2900, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B1E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_9B1E")

    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x86, 5)
    EventEnd(0x5)
    Return()

    # Function_37_9868 end

    def Function_38_9B28(): pass

    label("Function_38_9B28")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9C86")

    #C0443
    ChrTalk(
        0xC,
        (
            "#5Pあら……\x01",
            "ロイド、それにエリィ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#0002F#11Pこんにちは、マーブル先生。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x102,
        "#0102F#6Pお忙しい所をすみません。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CF4")

    label("loc_9C86")


    #C0446
    ChrTalk(
        0xC,
        (
            "#5Pあら……\x01",
            "ロイドではありませんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x101,
        (
            "#0002F#11Pこんにちは、マーブル先生。\x02\x03",

            "お忙しい所をすみません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CF4")


    #C0448
    ChrTalk(
        0xC,
        (
            "#5Pふふ、いいのですよ。\x01",
            "ちょうど休み時間でしたし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E7B")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0449
    ChrTalk(
        0xC,
        (
            "#5Pそういえば、あなた方は\x01",
            "同じ職場の同僚という話でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xC,
        (
            "#5Pふふっ、そうして一緒にいるのを見ると\x01",
            "とても感慨深いものがありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        "#0012F#11Pはは……\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        "#0112F#6Pそ、そういうものでしょうか？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        (
            "#5Pふふ……\x01",
            "それでどうしました？\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xC,
        (
            "#5P今日は礼拝に？\x01",
            "それともお墓参りですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EAF")

    label("loc_9E7B")


    #C0455
    ChrTalk(
        0xC,
        (
            "#5Pあなた方は礼拝に？\x01",
            "それともお墓参りですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EAF")


    #C0456
    ChrTalk(
        0x101,
        "#0008F#11Pいえ、それが……\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x153,
        (
            "#1100F#12Pねえねえ、ロイド。\x02\x03",

            "この人がしすたーさん？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0458
    ChrTalk(
        0xC,
        "#5Pあら、その子は……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#0003F#11Pその、実は……\x02\x03",

            "#0001Fこの子に関することで\x01",
            "相談したい事がありまして。\x02",
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
        "#11P……そうですか、そんな事が。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xC,
        (
            "#11Pおお女神#4Rエイドス#よ……\x01",
            "迷える子羊に光と幸いあれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "#11Pそしてこの者たちを出会わせた\x01",
            "導きに感謝いたします……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        "#0000F#6Pマーブル先生……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A136")

    #C0464
    ChrTalk(
        0x102,
        (
            "#0104F#6P……確かに、出会えたのは\x01",
            "女神の導きかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1D1")

    label("loc_A136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A186")

    #C0465
    ChrTalk(
        0x103,
        (
            "#0204F#6P……確かに、出会えたのは\x01",
            "何かの導きかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1D1")

    label("loc_A186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A1D1")

    #C0466
    ChrTalk(
        0x104,
        (
            "#0304F#6P……確かに、出会えたのは\x01",
            "女神の導きかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1D1")


    #C0467
    ChrTalk(
        0x153,
        "#1105F#6Pほえ～……？\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "#11Pとりあえず……\x01",
            "この子の記憶喪失についての\x01",
            "相談をしに来たのですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xC,
        (
            "#11P何でも名前以外のことは\x01",
            "全く覚えていないとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#0006F#6Pええ……そうなんです。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x153,
        (
            "#1106F#6Pえっと、がんばって\x01",
            "思い出そうとしてるんだけど。\x02\x03",

            "#1108Fぜんぜんダメみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        "#11Pそう……いい子ですね。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xC)

    #C0473
    ChrTalk(
        0xC,
        (
            "#11P……確かに教会には\x01",
            "心と精神の領域に関する\x01",
            "知識と技術が伝わっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xC,
        (
            "#11Pそして……\x01",
            "記憶喪失に関する対症療法も。\x02",
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
        "#0002F#6Pそ、それじゃあ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A448")

    #C0476
    ChrTalk(
        0x102,
        (
            "#0100F#6Pこの子の記憶を\x01",
            "取り戻せるんですか……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4CD")

    label("loc_A448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A48A")

    #C0477
    ChrTalk(
        0x103,
        (
            "#0202F#6Pこの子の記憶を\x01",
            "取り戻せますか……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4CD")

    label("loc_A48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A4CD")

    #C0478
    ChrTalk(
        0x104,
        (
            "#0300F#6Pこの子の記憶も\x01",
            "取り戻せるってことッスか！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4CD")


    #C0479
    ChrTalk(
        0xC,
        (
            "#11P確実ではありませんが\x01",
            "試してみる価値はあるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        (
            "#11P時間も無いことですし……\x01",
            "すぐに試してしまいましょうか。\x02",
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
            "#0005F#6Pもしかして……\x01",
            "先生がやってくれるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xC,
        (
            "#11Pええ、わたくしも一応、\x01",
            "幾つかの技を修めています。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xC,
        (
            "#11P心と精神に関する、\x01",
            "教会に伝わる《法術》を。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        "#0001F#6P《法術》……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A68D")

    #C0485
    ChrTalk(
        0x102,
        (
            "#0101F#6P教会の聖職者に伝わっている\x01",
            "祈りと秘蹟に関する技ですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A742")

    label("loc_A68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A6F1")

    #C0486
    ChrTalk(
        0x103,
        (
            "#0201F#6P導力器#6Rオーブメント#に頼らない\x01",
            "祈りによって紡がれる魔法#4Rアーツ#……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A742")

    label("loc_A6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A742")

    #C0487
    ChrTalk(
        0x104,
        (
            "#0301F#6P教会の人間が使えるっていう\x01",
            "不思議な祈りの技ってやつだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A742")


    #C0488
    ChrTalk(
        0xC,
        (
            "#11Pええ、本来ならばそれに特化した\x01",
            "専門組織があるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xC,
        (
            "#11Pあいにくクロスベルには\x01",
            "その専門家が来る事が少ないのです。\x02",
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
        "#0005F#6P専門家、ですか……？\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xC,
        (
            "#11P……大きな声では言えませんが\x01",
            "教会の中にも色々とあるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        (
            "#11Pその組織は《封聖省》と呼ばれる\x01",
            "機関に所属しているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xC,
        (
            "#11Pこの大聖堂を任されている\x01",
            "エラルダ大司教は、その組織の活動を\x01",
            "快く思っておられないようなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xC,
        (
            "#11Pそのため、そうした専門家が\x01",
            "クロスベルに来る機会が少なくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        (
            "#0006F#6Pな、なんだか色々と\x01",
            "難しい事情があるんですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_AA8A")

    #C0496
    ChrTalk(
        0x102,
        (
            "#0103F#6P《封聖省》に所属する組織……\x01",
            "つまり《星杯騎士団》ですね。\x02\x03",

            "#0108Fエラルダ大司教が《典礼省》寄りの\x01",
            "有力者である事は聞いていましたが\x01",
            "そんな事情があったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xC,
        (
            "#11Pふふ、さすがエリィは\x01",
            "その辺りにも詳しいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB4F")

    label("loc_AA8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AAF0")

    #C0498
    ChrTalk(
        0x103,
        (
            "#0201F#6P要するに教会内部の\x01",
            "縄張り争いですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        "#11Pええ、恥ずかしながら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB4F")

    label("loc_AAF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_AB4F")

    #C0500
    ChrTalk(
        0x104,
        (
            "#0301F#6P要するに教会内部の\x01",
            "縄張り争いッスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xC,
        "#11Pええ、恥ずかしながら……\x02",
    )

    CloseMessageWindow()

    label("loc_AB4F")


    #C0502
    ChrTalk(
        0xC,
        (
            "#11Pただ、わたくしが使える法術も\x01",
            "彼らの使うものと変わりはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        "#11P試してみる価値はあると思います。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        (
            "#0000F#6Pわかりました。\x01",
            "よろしくお願いします。\x02\x03",

            "#0005Fえっと、どこかに\x01",
            "移動した方がいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xC,
        "#11Pいえ、この場で問題ありません。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "#11Pキーアさんと言いましたね。\x01",
            "こちらに来ていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x153,
        "#1109F#6Pはーい！\x02",
    )

    CloseMessageWindow()
    OP_68(151110, 1100, 12960, 1000)

    def lambda_ACC5():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_ACC5)
    WaitChrThread(0x153, 1)
    Sleep(500)

    #C0508
    ChrTalk(
        0xC,
        (
            "#11P目を閉じてゆっくりと\x01",
            "深呼吸をしてみてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x153,
        (
            "#1110F#5Pうんっ！\x02\x03",

            "#1103F#40Wすー……、はー……\x02\x03",

            "#40Wすー……、はー……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xC,
        "#11Pええ、いいですよ。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xC,
        "#11P……それでは……\x02",
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
            "#11P#40W──空の女神の名において\x01",
            "聖別されし七耀#4Rしちよう#、ここに在り。\x02",
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
        "#0005F#6P（あ……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_AEB2")

    #C0514
    ChrTalk(
        0x102,
        "#0105F#6P（これが法術……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF13")

    label("loc_AEB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AEE7")

    #C0515
    ChrTalk(
        0x103,
        "#0201F#6P（これが法術ですか……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF13")

    label("loc_AEE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_AF13")

    #C0516
    ChrTalk(
        0x104,
        "#0301F#6P（これが法術か……）\x02",
    )

    CloseMessageWindow()

    label("loc_AF13")


    #C0517
    ChrTalk(
        0xC,
        "#11P#40W空の金曜、識の銀耀──\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xC,
        (
            "#11P#40Wその融合をもって\x01",
            "失われし欠片の在り処を\x01",
            "彼の者に指し示したまえ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x1, 0x1, 0x153, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(228, 0, 100, 0)
    Sleep(500)

    def lambda_AFCF():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_AFCF)
    Sleep(800)

    #C0519
    ChrTalk(
        0x153,
        "#1105F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        "#0013F#6Pキーア……！？\x02",
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
        "#11P大丈夫、心配いりません。\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xC,
        "#11P……どうですか、キーアさん。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xC,
        "#11P何か思い出してきませんか？\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x153,
        (
            "#1103F#5P#40Wんー……\x02\x03",

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
            "#1108F#5P……なんかね、\x01",
            "暗くてでっかい場所が\x01",
            "アタマの中に浮かんできた。\x02\x03",

            "#1112F上の方がぼんやり光ってて\x01",
            "キレイだけど、ちょっとコワイ感じ。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        "#0005F#6P暗くてでっかい場所……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B1D6")

    #C0527
    ChrTalk(
        0x102,
        "#0108F#6Pどこの事かしら……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B233")

    label("loc_B1D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B20B")

    #C0528
    ChrTalk(
        0x103,
        "#0208F#6Pどこの事でしょうか……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B233")

    label("loc_B20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B233")

    #C0529
    ChrTalk(
        0x104,
        "#0301F#6Pどこの事だ……？\x02",
    )

    CloseMessageWindow()

    label("loc_B233")


    #C0530
    ChrTalk(
        0xC,
        (
            "#11Pその光景以外に\x01",
            "思い出したことは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "#11Pご家族のこととか、\x01",
            "住んでいた家のこととか。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x153,
        "#1106F#5Pんー……そっちはゼンゼン。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xC,
        "#11Pそうですか……\x02",
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
        "#0001F#6Pえっと、マーブル先生？\x02",
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
            "#11P……どうやら法術では\x01",
            "ここまでが限界のようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xC,
        (
            "#11P心理的なアプローチから\x01",
            "引き出せる記憶はここまで……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xC,
        (
            "#11Pひょっとしたら……\x01",
            "何か神経系に関する問題が\x01",
            "あるのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        "#0005F#6P神経系の問題……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B470")

    #C0540
    ChrTalk(
        0x102,
        "#0101F#6Pど、どういう事ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4CF")

    label("loc_B470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B4A1")

    #C0541
    ChrTalk(
        0x103,
        "#0201F#6Pそれはどういう……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4CF")

    label("loc_B4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B4CF")

    #C0542
    ChrTalk(
        0x104,
        "#0301F#6Pそいつはどういう……？\x02",
    )

    CloseMessageWindow()

    label("loc_B4CF")


    #C0543
    ChrTalk(
        0xC,
        (
            "#11P……端的に言うと\x01",
            "脳の神経に関する問題です。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xC,
        (
            "#11P何らかの原因で\x01",
            "記憶に関する神経の伝達が\x01",
            "阻害されてしまっている……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xC,
        "#11Pその可能性がありますね。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        (
            "#0011F#6Pそ、そんな……\x02\x03",

            "#0007Fそれって……\x01",
            "何とかならないんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xC,
        "#11Pそうですね……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xC,
        (
            "#11P教会に伝わっている法術は\x01",
            "心と精神に関する領域……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xC,
        (
            "#11Pひょっとしたら\x01",
            "この問題は、近代医療の方が\x01",
            "向いているのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        "#0005F#6Pえ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B6A9")

    #C0551
    ChrTalk(
        0x102,
        "#0105F#6P近代医療という事は……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B708")

    label("loc_B6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B6DA")

    #C0552
    ChrTalk(
        0x103,
        "#0205F#6P近代医療というと……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B708")

    label("loc_B6DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B708")

    #C0553
    ChrTalk(
        0x104,
        "#0305F#6P近代医療ってことは……\x02",
    )

    CloseMessageWindow()

    label("loc_B708")


    #C0554
    ChrTalk(
        0xC,
        "#11Pええ、聖ウルスラ医科大学です。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xC,
        (
            "#11Pこれまで近代医療では\x01",
            "心と精神に関する分野の研究は\x01",
            "不十分とされていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xC,
        (
            "#11P数年前、あそこでは\x01",
            "『神経科』という部門が立ち上げられ、\x01",
            "優秀な研究者もいると聞いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xC,
        (
            "#11Pそちらに相談したら、教会とは違った\x01",
            "アプローチが期待できるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        (
            "#0000F#6P『神経科』ですか……\x01",
            "（あれ、どこかで聞いたような？）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B8E3")

    #C0559
    ChrTalk(
        0x102,
        (
            "#0103F#6Pねえ、ロイド……\x02\x03",

            "#0101F相談に行ってみた方が\x01",
            "いいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B99A")

    label("loc_B8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B945")

    #C0560
    ChrTalk(
        0x103,
        (
            "#0203F#6Pロイドさん……\x02\x03",

            "#0201F相談に行ってみた方が\x01",
            "いいのではないでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B99A")

    label("loc_B945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B99A")

    #C0561
    ChrTalk(
        0x104,
        (
            "#0303F#6Pおい、ロイド。\x02\x03",

            "#0300F相談に行ってみた方が\x01",
            "いいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B99A")


    #C0562
    ChrTalk(
        0x101,
        (
            "#0003F#6Pああ、そうだな……\x02\x03",

            "#0002F──先生。\x01",
            "ありがとうございます。\x02\x03",

            "早速、ウルスラ病院に\x01",
            "行ってみようかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xC,
        "#11Pええ、それがいいでしょう。\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xC,
        (
            "#11P……すみません。\x01",
            "あまり力になれませんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#0005F#6Pそ、そんな事ないですよ！\x01",
            "神経科の話も教えてもらったし。\x02\x03",

            "#0000Fそれに……\x01",
            "キーアが思い出した光景も\x01",
            "何か手がかりになると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BB3B")

    #C0566
    ChrTalk(
        0x102,
        "#0103F#6P『暗くてでっかい場所』ね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBAC")

    label("loc_BB3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BB78")

    #C0567
    ChrTalk(
        0x103,
        "#0203F#6P『暗くてでっかい場所』ですか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBAC")

    label("loc_BB78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BBAC")

    #C0568
    ChrTalk(
        0x104,
        "#0303F#6P『暗くてでっかい場所』か……\x02",
    )

    CloseMessageWindow()

    label("loc_BBAC")

    OP_93(0x153, 0xB4, 0x1F4)

    #C0569
    ChrTalk(
        0x153,
        (
            "#1103F#11Pうーん、なんか上の方が\x01",
            "ぼんやり光ってたかなぁ。\x02\x03",

            "#1112Fうぉおおおんって音がして……\x01",
            "キレイだけど、ちょっとコワかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        "#0003F#6Pう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xC,
        (
            "#11P確かに……\x01",
            "普通の場所ではなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xC,
        "#11P貴方がたに女神の祝福を。\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xC,
        (
            "#11Pキーアさんに良き導きがある事を\x01",
            "わたくしも祈っております。\x02",
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

    # Function_38_9B28 end

    def Function_39_BD46(): pass

    label("Function_39_BD46")

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

    # Function_39_BD46 end

    def Function_40_BD89(): pass

    label("Function_40_BD89")

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
            "#5Pこのクロスベル大聖堂に\x01",
            "よくぞいらっしゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x8,
        "#5P本日は如何なるご用かね？\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        (
            "#12P#0000Fエラルダ大司教ですね？\x02\x03",

            "警察・特務支援課の者です。\x01",
            "今日は仕事でこちらを訪れました。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x8,
        "#5Pふむ、仕事だったか。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x102,
        (
            "#12P#0100Fウルスラ病院の\x01",
            "ラゴー内科教授の依頼なんです。\x02\x03",

            "教授はこちらに『ルピナス草』を\x01",
            "頂けるよう、連絡差し上げたそうですね？\x02\x03",

            "#0103F多忙な自分の代わりに、\x01",
            "その薬草をエラルダ大司教から\x01",
            "預かってきて欲しいと……\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x8,
        "#5P……待ちたまえ。\x02",
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
        "#5Pラゴー……ラゴー教授と言ったかね？\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x8,
        (
            "#5Pああ、確かにこの間、\x01",
            "手紙が届いていたが……\x01",
            "そのような話は今初めて聞いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x104,
        "#11P#0305Fは……はぁ？\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x8,
        "#5P簡単な話だ。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x8,
        (
            "#5P私は、ラゴー教授の手紙だけは\x01",
            "一切読まない事にしているのでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#12P#0005Fえ……えぇ！？\x02\x03",

            "ど、どうしてそんなこと……\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x8,
        (
            "#5Pどうしても、だ。\x01",
            "こればかりは女神に誓って\x01",
            "決めていることでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x104,
        "#11P#0305F（おいロイド、こいつは……）\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x103,
        (
            "#12P#0203F（……すごく面倒な\x01",
            "  人間関係のようですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        "#12P#0106F（困ったわ……）\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#12P#0003F（で、でも一度請け負った依頼だ……\x01",
            "  なんとしてもやり遂げなくちゃ。）\x02\x03",

            "#0001Fあ、あの……\x01",
            "エラルダ大司教。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x8,
        "#5P……なんだね？\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#12P#0001Fラゴー教授の頼んだ薬草は、\x01",
            "内科の研究に使うと言っていました。\x02\x03",

            "ウルスラ病院の整った研究環境なら、\x01",
            "その薬草が将来、何人かの病人を\x01",
            "助けることに繋がると思うんです。\x02\x03",

            "#0008Fその……ラゴー教授と何があったのか、\x01",
            "立ち入った話を聞くつもりはありません。\x02\x03",

            "#0003Fですが、なんとか『ルピナス草』を\x01",
            "ラゴー教授に譲っていただくわけには\x01",
            "いきませんか？\x02",
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
            "#5P……君は何か、勘違いを\x01",
            "しているようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x8,
        (
            "#5P私は薬草を渡さんとは\x01",
            "一言も言っておらんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x101,
        "#12P#0005F……え。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x8,
        (
            "#5P……『ルピナス草』は、\x01",
            "大聖堂左手奥の私の執務室にある。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x8,
        (
            "#5Pレントン司祭に\x01",
            "私が許可したことを話せば\x01",
            "つつがなく渡してもらえるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x8,
        (
            "#5P……さぁ、話は終わりだ。\x01",
            "さっさと行きたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x101,
        (
            "#12P#0005Fえ、えっと……\x01",
            "ありがとうございます……？\x02",
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

    def lambda_C65D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C65D)

    def lambda_C677():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C677)

    def lambda_C691():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C691)

    def lambda_C6AB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C6AB)
    Sleep(500)
    SetCameraDistance(26740, 0)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_C6EB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C6EB)

    def lambda_C6F8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C6F8)

    def lambda_C705():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C705)

    def lambda_C712():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C712)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0601
    ChrTalk(
        0x101,
        "#5P#0003Fえ、えーっと……\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x104,
        (
            "#12P#0300Fなんだかやけにあっさり\x01",
            "説得できちまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x102,
        (
            "#12P#0100Fロイドに説得されて、というより\x01",
            "普通に譲っていただけるつもりだった\x01",
            "みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x103,
        (
            "#11P#0200Fよく分かりませんが……\x02\x03",

            "大司教の気が変わらないうちに\x01",
            "薬草をもらった方が\x01",
            "いいんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        (
            "#5P#0003Fそれもそうだな。\x02\x03",

            "#0000Fえっと……左手奥の執務室だったな。\x01",
            "ちょっと行ってみよう。\x02",
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

    # Function_40_BD89 end

    def Function_41_C944(): pass

    label("Function_41_C944")

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
        "#5Pおや、何の用だい？\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xA,
        (
            "#5Pここはエラルダ大司教の執務室だ。\x01",
            "無闇に入っちゃいけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x101,
        (
            "#12P#0000Fえっと、警察・特務支援課の者\x01",
            "なのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0609
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは『ルピナス草』を\x01",
            "受け取りに来た事を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0610
    ChrTalk(
        0xA,
        (
            "#5P……ああ、なるほど\x01",
            "そういうことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xA,
        (
            "#5P大司教の許可を頂いてるんだね？\x01",
            "じゃあ、ちょっと待ってくれるかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(98390, 1500, 8960, 4000)
    OP_93(0xA, 0x0, 0x1F4)

    def lambda_CB48():
        OP_95(0xFE, 96000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CB48)
    WaitChrThread(0xA, 1)

    def lambda_CB66():
        OP_95(0xFE, 100000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CB66)
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

    def lambda_CBCA():
        OP_95(0xFE, 96000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CBCA)
    WaitChrThread(0xA, 1)

    def lambda_CBE8():
        OP_95(0xFE, 96000, 0, 7830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CBE8)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)

    #C0612
    ChrTalk(
        0xA,
        "#5Pはい、これが『ルピナス草』だよ。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x341, 1)

    #C0614
    ChrTalk(
        0xA,
        (
            "#5Pルピナスというのは、\x01",
            "古い言葉で『狼』を指していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xA,
        (
            "#5P遥か昔に神狼がもたらしたとされる\x01",
            "由緒正しい薬草なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xA,
        (
            "#5P昔はクロスベル市近辺で\x01",
            "採れたそうだが、開発によって\x01",
            "数が減ってしまってねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x102,
        (
            "#12P#0100F私も小さい頃、おじいさまに\x01",
            "同じ話を聞いたことがある\x01",
            "気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそうだったのか……\x02\x03",

            "#0003Fでも……大司教は\x01",
            "なんでそんな貴重な薬草を\x01",
            "譲ってくれるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x104,
        (
            "#12P#0306F腑に落ちねぇよな。\x01",
            "なんだかラゴー教授さんを\x01",
            "嫌ってるみたいだったしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x103,
        (
            "#12P#0200Fそのあたりの確執の正体も\x01",
            "少し気になりますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xA,
        (
            "#5Pああ、その事か。\x01",
            "……まぁ、仕方ないことだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xA,
        (
            "#5Pウルスラ病院のラゴー教授は、\x01",
            "元はこの大聖堂で司祭の勉強を\x01",
            "されていた方だからね。\x02",
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
        "#12P#0005F病院の先生が司祭を……？\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xA,
        "#5P何もおかしくはないさ。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0xA,
        (
            "#5P先進医療と言っても、\x01",
            "内科の分野は七耀教会の領分に\x01",
            "とても近いものだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x103,
        (
            "#12P#0200F確かに、調薬などの研究は\x01",
            "七耀教会でも行なわれていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x102,
        (
            "#12P#0105Fでも、なんでラゴー教授は\x01",
            "司祭をやめて病院に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xA,
        (
            "#5P当時の病院長から\x01",
            "スカウトがあったそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xA,
        (
            "#5Pラゴー教授は大司教に\x01",
            "調薬などを教わっていたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xA,
        (
            "#5P先進医療に挑んでみたいという\x01",
            "気持ちが強かったから、\x01",
            "司祭の道をやめてしまわれたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xA,
        (
            "#5P大司教も頑固な方だから、\x01",
            "そんなラゴー教授を許せないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x104,
        "#12P#0303Fんー、分からんでもないな。\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xA,
        (
            "#5Pまぁ、大司教は頑固だけど……\x01",
            "分別は弁えてる方だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xA,
        (
            "#5Pホラ、こうやって君たちに\x01",
            "薬草を渡したわけだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xA,
        (
            "#5Pラゴー教授の実力だけは\x01",
            "ちゃんと認めているってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x103,
        (
            "#12P#0203F要するに、面倒くさい関係じゃなくて……\x02\x03",

            "#0200F物凄く、面倒くさい関係なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        (
            "#12P#0012Fハ、ハハ……\x01",
            "（身も蓋もない言い方だな……）\x02\x03",

            "#0003Fと、とにかく。\x01",
            "目的のものは手に入ったんだ。\x02\x03",

            "#0000Fさっそくウルスラ病院のラゴー教授に\x01",
            "薬草を届けに行こう。\x02",
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

    # Function_41_C944 end

    def Function_42_D42F(): pass

    label("Function_42_D42F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D4AB")

    #C0638
    ChrTalk(
        0x8,
        (
            "……ラゴー教授は、\x01",
            "自らの意思で病院医師の道を\x01",
            "選んだのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x8,
        (
            "もはや、私から言う事は\x01",
            "何もあるまい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D65D")

    label("loc_D4AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_D527")

    #C0640
    ChrTalk(
        0x8,
        (
            "……どうしたね。\x01",
            "まだ何か用があるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x8,
        (
            "薬草を受け取ったのなら、\x01",
            "さっさと届けてきたらどうかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D65D")

    label("loc_D527")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_D65D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D5B0")

    #C0642
    ChrTalk(
        0x8,
        (
            "『ルピナス草』は聖堂左手奥の\x01",
            "私の執務室に備蓄がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x8,
        (
            "レントン司祭に言って\x01",
            "貰ってくるといいだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D65D")

    label("loc_D5B0")


    #C0644
    ChrTalk(
        0x8,
        (
            "『ルピナス草』は聖堂左手奥の\x01",
            "私の執務室に備蓄がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x8,
        (
            "レントン司祭に言って\x01",
            "貰ってくるといいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x8,
        "……他にもまだ用があるのかね？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        "#0005Fい、いえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D65D")

    Return()

    # Function_42_D42F end

    def Function_43_D65E(): pass

    label("Function_43_D65E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB3E")

    #C0648
    ChrTalk(
        0x153,
        "#11P#1110Fまたまたこんにちはっ！\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xC,
        "#5Pあらこんにちは、キーアさん。\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xC,
        "#5P……何か忘れ物でもしたのかしら？\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        (
            "#12P#0000Fいえ、そういうわけでは\x01",
            "ないんですが……\x02\x03",

            "さっき子供たちとすれ違ったので、\x01",
            "ちょっと気になったというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0xC,
        (
            "#5Pふふ、今から日曜学校の\x01",
            "授業が入っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xC,
        (
            "#5Pでも……\x01",
            "あなた達が来てくれて\x01",
            "ちょうどよかったかも。\x02",
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
            "#5P実は、前々から……\x01",
            "クロスベル警察について\x01",
            "子供たちに教えようと思ってたの。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D904")

    #C0655
    ChrTalk(
        0x102,
        "#12P#0105F警察について……ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D97E")

    label("loc_D904")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D93B")

    #C0656
    ChrTalk(
        0x103,
        "#12P#0205F警察について……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D97E")

    label("loc_D93B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D97E")

    #C0657
    ChrTalk(
        0x104,
        (
            "#12P#0305F日曜学校で\x01",
            "警察のことを扱うんスか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D97E")


    #C0658
    ChrTalk(
        0xC,
        "#5Pええ、そうよ。\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xC,
        (
            "#5Pそれで、あなた達には……\x01",
            "その授業の特別講師を\x01",
            "頼めないかと思って。\x02",
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
            "#12P#0005F特別講師ってことは……\x01",
            "俺が教壇に立つんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xC,
        "#5P是非お願いしたいわ。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0xC,
        (
            "#5P警察のことは、やっぱり\x01",
            "警察の人間が一番よく\x01",
            "分かるでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xC,
        (
            "#5P私が授業するよりも\x01",
            "ずっと分かりやすいだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xC,
        (
            "#5Pどう？　日曜学校の講師……\x01",
            "引き受けてはもらえないかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x4, 0x2)
    OP_29(0x27, 0x1, 0x0)
    Jump("loc_DB83")

    label("loc_DB3E")


    #C0665
    ChrTalk(
        0xC,
        (
            "#5P日曜学校の講師の件……\x01",
            "引き受けてくれる気に\x01",
            "なったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB83")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCAD")

    #C0666
    ChrTalk(
        0x101,
        (
            "#12P#0003Fいえ……\x01",
            "やっぱり遠慮しておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xC,
        (
            "#5Pあら、そう？\x01",
            "いい考えだと\x01",
            "思ったのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xC,
        (
            "#5P都合が悪いなら\x01",
            "無理にとは言わないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xC,
        (
            "#5P気が向いたら\x01",
            "また声をかけてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)

    label("loc_DCAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E296")

    #C0670
    ChrTalk(
        0x101,
        (
            "#12P#0000F……そうですね。\x01",
            "是非、引き受けてみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xC,
        (
            "#5Pまぁ、本当？\x01",
            "ふふ、助かるわ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DD24():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_DD24)

    def lambda_DD31():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_DD31)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDB8")

    #C0672
    ChrTalk(
        0x102,
        (
            "#12P#0105Fロイド……大丈夫なの？\x02\x03",

            "#0103F人に教えるという事は\x01",
            "そんなに簡単なことじゃ\x01",
            "無いと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEB2")

    label("loc_DDB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE30")

    #C0673
    ChrTalk(
        0x103,
        (
            "#12P#0200F……大丈夫なんですか？\x02\x03",

            "#0203F授業なんて、生半可な事では\x01",
            "務めきれないと思いますが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEB2")

    label("loc_DE30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEB2")

    #C0674
    ChrTalk(
        0x104,
        (
            "#12P#0306Fおいおい、大丈夫か？\x02\x03",

            "#0300F俺がいうのもなんだが……\x01",
            "安請け合いできる\x01",
            "部類のモンじゃねぇと思うぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEB2")


    def lambda_DEB7():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DEB7)

    #C0675
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、分かってる。\x01",
            "別に考えなしに\x01",
            "引き受けるわけじゃないさ。\x02\x03",

            "#0003Fただ……こういうのって、\x01",
            "警察のことを知ってもらう\x01",
            "数少ないチャンスだと思ってさ。\x02\x03",

            "#0000Fかつての俺やエリィみたいに、\x01",
            "この中から未来の警察官が\x01",
            "出てくるかもしれないんだし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E006")

    #C0676
    ChrTalk(
        0x102,
        (
            "#12P#0104F……なるほど。\x01",
            "ロイドらしい考え方ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E08C")

    label("loc_E006")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E043")

    #C0677
    ChrTalk(
        0x103,
        "#12P#0204Fふむ……一理ありますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E08C")

    label("loc_E043")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E08C")

    #C0678
    ChrTalk(
        0x104,
        (
            "#12P#0300Fなるほどな……\x01",
            "一種の布教活動ってやつか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E08C")


    def lambda_E091():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E091)

    #C0679
    ChrTalk(
        0x101,
        (
            "#6P#0000Fウルスラ病院に行くのが\x01",
            "後回しになっちゃうけど……\x01",
            "キーア、いいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x153,
        (
            "#11P#1109Fうん、いーよ！\x02\x03",

            "#1100Fよくわかんないけど、\x01",
            "ロイドがやりたいんなら\x01",
            "キーア、応援する！\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#6P#0009Fはは、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xC,
        (
            "#5Pそうね、それじゃあ……\x01",
            "一旦外に出ましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xC,
        (
            "#5P授業の進め方を\x01",
            "一通り教えてあげるわ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E1D8():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E1D8)

    def lambda_E1E5():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E1E5)

    def lambda_E1F2():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_E1F2)

    #C0684
    ChrTalk(
        0x101,
        (
            "#12P#0000Fよろしくお願いします、\x01",
            "マーブル先生。\x02",
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
            "クエスト【日曜学校の特別講師】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Call(0, 44)
    Call(0, 45)
    Call(0, 48)

    label("loc_E296")

    Return()

    # Function_43_D65E end

    def Function_44_E297(): pass

    label("Function_44_E297")

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
            "#5P#0003F──なるほど、大体分かりました。\x02\x03",

            "まずは警察のことについて\x01",
            "一通り分かりやすく説明して……\x02\x03",

            "#0000F最後に質疑応答の時間を設ける。\x01",
            "……そんな感じですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0xC,
        "#12Pええ、それで充分よ。\x02",
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xC,
        "#12Pあと、一つ提案があるのだけど。\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x101,
        "#5P#0005F提案……ですか？\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0xC,
        "#12Pそう、よければだけれど……\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0xC,
        (
            "#12Pキーアさんにも\x01",
            "ロイドの授業を\x01",
            "受けてもらってはどうかしら？\x02",
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
        "#5P#0005Fえっ……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E52F")

    #C0693
    ChrTalk(
        0x102,
        (
            "#5P#0100Fマーブル先生……\x01",
            "それ、いいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5A7")

    label("loc_E52F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E56E")

    #C0694
    ChrTalk(
        0x103,
        (
            "#5P#0204Fたしかに……\x01",
            "面白そうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5A7")

    label("loc_E56E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E5A7")

    #C0695
    ChrTalk(
        0x104,
        "#5P#0309Fはは、面白そうじゃないか。\x02",
    )

    CloseMessageWindow()

    label("loc_E5A7")


    #C0696
    ChrTalk(
        0x153,
        (
            "#5P#1105Fキーアもロイドのジュギョー、\x01",
            "受けていいの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0xC,
        "#12Pええ、もちろん。\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0xC,
        (
            "#12Pもともと、あなたくらいの年齢なら\x01",
            "日曜学校に通っていいことに\x01",
            "なっているのですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x153,
        "#5P#1110Fわぁ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    #C0700
    ChrTalk(
        0x153,
        (
            "#6P#1109Fだったら、キーアも\x01",
            "ジュギョーに出る！\x02\x03",

            "キーア、ロイドたちのこと\x01",
            "いっぱい知りたいもん！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E6E3():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E6E3)
    Sleep(50)

    def lambda_E6F3():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E6F3)

    #C0701
    ChrTalk(
        0x101,
        "#12P#0005Fキーア……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E765")

    #C0702
    ChrTalk(
        0x102,
        (
            "#5P#0100Fロイド、これはもう\x01",
            "やるしかないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E802")

    label("loc_E765")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7B2")

    #C0703
    ChrTalk(
        0x103,
        (
            "#5P#0200Fロイドさん……\x01",
            "逃げ道はないみたいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E802")

    label("loc_E7B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E802")

    #C0704
    ChrTalk(
        0x104,
        (
            "#5P#0300Fここまで言われちゃ、\x01",
            "逃げるわけにゃ～いかねぇな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E802")


    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#0004F……はは、そうみたいだな。\x02\x03",

            "#0000Fキーア、他の子供たちと\x01",
            "仲良く授業を受けるんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x153,
        "#6P#1110Fうん！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E8F6")

    #C0707
    ChrTalk(
        0x102,
        (
            "#5P#0104F私も教室の後ろのほうで、\x01",
            "あなたの授業ぶりを\x01",
            "見せてもらうわ。\x02\x03",

            "#0100F頑張ってね、ロイド。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9FF")

    label("loc_E8F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E980")

    #C0708
    ChrTalk(
        0x103,
        (
            "#5P#0203Fわたしも教室の後ろで\x01",
            "授業を見ているつもりです。\x02\x03",

            "#0211F……応援しているので\x01",
            "下手な授業はしないように。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9FF")

    label("loc_E980")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9FF")

    #C0709
    ChrTalk(
        0x104,
        (
            "#5P#0304Fさぁて、俺も教室の後ろで\x01",
            "授業を見させてもらうかね。\x02\x03",

            "#0300Fロイド先生の\x01",
            "お手並み拝見ってヤツだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9FF")


    def lambda_EA04():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA04)

    #C0710
    ChrTalk(
        0x101,
        (
            "#12P#0006F（な、なんかずるいな……）\x02\x03",

            "#0000Fでもまぁ……\x01",
            "やるしかないな。\x02\x03",

            "皆に警察のことを\x01",
            "知ってもらうチャンス……\x01",
            "逃さないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xC,
        "#12Pその意気ですよ。\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0xC,
        (
            "#12Pさて、それでは……\x01",
            "そろそろ授業を始めると\x01",
            "しましょうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Return()

    # Function_44_E297 end

    def Function_45_EB0C(): pass

    label("Function_45_EB0C")

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
        "#11Pさて……\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0xC,
        (
            "#11P今日の授業に入る前に、\x01",
            "皆さんに新しいお友達を\x01",
            "紹介しますね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x153, 500)

    #C0715
    ChrTalk(
        0xC,
        "#5P──キーアさん、お願いね。\x02",
    )

    CloseMessageWindow()

    def lambda_EC28():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EC28)
    OP_98(0x153, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)

    #C0716
    ChrTalk(
        0x153,
        (
            "#11P#1110Fんーとね、キーアだよ！\x01",
            "よろしくねー！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 200, -1, -1)
    SetChrName("子供たち")

    #A0717
    AnonymousTalk(
        0xFF,
        "#5Sよろしく～～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0718
    ChrTalk(
        0xC,
        (
            "#11Pふふ、元気な挨拶をありがとう。\x01",
            "それじゃ空いている席に\x01",
            "座って頂戴ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x153,
        "#11P#1109Fは～い。\x02",
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
        "#5P#1109Fえへへ、よろしくね！\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x11,
        (
            "#12Pう、うん。\x01",
            "よろしくね。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(152620, 1500, 3180, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEA2")

    #C0722
    ChrTalk(
        0x102,
        (
            "#6P#0104F（ふふ……授業参観をする\x01",
            "  母親になった気分ね。）\x02\x03",

            "#0100F（キーアちゃん、がんばって！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFB0")

    label("loc_EEA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF30")

    #C0723
    ChrTalk(
        0x103,
        (
            "#6P#0204F（……父兄たちの授業参観……\x01",
            "  こんな気分なのかもしれませんね。）\x02\x03",

            "#0200F（キーアを応援してあげないと。 ）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFB0")

    label("loc_EF30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EFB0")

    #C0724
    ChrTalk(
        0x104,
        (
            "#6P#0304F（学ぶ我が子を見守るこの位置……\x01",
            "  くぅ、ジンと来るものがあるぜ。）\x02\x03",

            "#0309F（頑張れよ、キー坊！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFB0")

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
            "#11Pそれと……今日の授業には\x01",
            "特別講師の先生に\x01",
            "来ていただきました。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 300)

    #C0726
    ChrTalk(
        0xC,
        "#5P──どうぞ。\x02",
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x101,
        "#12P#0003Fは、はい。\x02",
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
            "#6Pおいおい、\x01",
            "まさかとは思ったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x15,
        "#6Pまさか、特別講師の先生って……\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x101,
        (
            "#11P#0003Fえ、えーっと……\x01",
            "何人か、知ってる顔も\x01",
            "いるみたいだけど……\x02\x03",

            "#0000F俺の名前は\x01",
            "ロイド・バニングスといいます。\x02\x03",

            "クロスベル警察の\x01",
            "特務支援課に所属する、\x01",
            "現役の警察官です。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0xF,
        (
            "#5Pけいさつ～？\x01",
            "なに、リュウたちとは\x01",
            "知り合いなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x10,
        "#5Pトクムシエンカ……\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x10,
        (
            "#5Pあっ、クロスベルタイムズに\x01",
            "載ってたの、見たことあるかも！\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0xF,
        "#5P……ああ、そういえば！\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0xF,
        (
            "#5P記事は読んでないけど、\x01",
            "ちーっちゃく写真が\x01",
            "載ってたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xC,
        "#11Pはいはい、お静かにね。\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0xC,
        (
            "#11P今日は皆に、警察について\x01",
            "勉強してもらおうと思って、\x01",
            "ロイド先生にお願いしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xC,
        (
            "#11P皆さん、よ～く\x01",
            "勉強させていただくのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("子供たち")

    #A0739
    AnonymousTalk(
        0xFF,
        "#5Sは～～い！\x02",
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
            "#5Pそれじゃあ、お願いしますね。\x01",
            "ロイド先生㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 300)

    #C0741
    ChrTalk(
        0x101,
        (
            "#11P#0003Fは、はい。\x01",
            "任せてください。\x02",
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
            "#11P#0003F（やばい……\x01",
            "  えらく緊張してきた……）\x02",
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
        "#6P#1107F#5S#N……ロイド、がんばってー！\x02",
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
            "#6Pあはは！　んだよ兄ちゃん、\x01",
            "応援されてるぞー！\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x15,
        "#6Pちょっと、やめなよリュウ～。\x02",
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x15,
        (
            "#6Pお兄さんも\x01",
            "一所懸命やってるんだからさ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x101,
        (
            "#11P#0006Fえっと、キーア……\x01",
            "授業が始まったら静かにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x153,
        "#6P#1106Fぶー、応援してあげたのにー。\x02",
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#11P#0004F（……ちょっとだけ……\x01",
            "  緊張がほぐれたかな。）\x02\x03",

            "#0000F……コホン。\x01",
            "それじゃ、早速授業を始めようか。\x02",
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
            "　　　講義開始！\x01",
            "～警察組織について～\x02",
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
            "※正しい答えを選んで\x01",
            "　特別授業を成功に導け！\x02",
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
            "#0004Fまずは……\x01",
            "警察がどんなものかを\x01",
            "知ってもらいたいな。\x02\x03",

            "#0000Fクロスベル自治州には、\x01",
            "他の国が持っている“あるもの”を\x01",
            "持つことが出来ない決まりがある。\x02\x03",

            "その代わりとして“警備隊”や\x01",
            "俺たち“警察”が存在するんだ。\x02\x03",

            "#0003Fクロスベル自治州にはない、\x01",
            "“国家において重要なもの”とは……\x02",
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
            "クロスベル自治州にはない、\x01",
            "“国家において重要なもの”とは？",
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
            "【①諜報機関】\x01",        # 0
            "【②遊撃士協会】\x01",      # 1
            "【③軍隊】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F930"),
        (1, "loc_FA7F"),
        (2, "loc_FB61"),
        (SWITCH_DEFAULT, "loc_FC88"),
    )


    label("loc_F930")


    #C0754
    ChrTalk(
        0x101,
        "#0000F……諜報機関だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0755
    ChrTalk(
        0x101,
        (
            "#0005F（って、確かにそれも存在しないけど\x01",
            "  法律では禁止されてないような……）\x02\x03",

            "#0012Fええと……国を守るためには\x01",
            "近隣諸国の情報が\x01",
            "必要不可欠で……\x02\x03",

            "普段は防犯をしてるけど、\x01",
            "その裏では観光客などから\x01",
            "重要な情報を集めているんだ。\x02\x03",

            "#0011F（な、何言ってんだ俺……\x01",
            "  やっぱりまだ緊張してるのか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC88")

    label("loc_FA7F")


    #C0756
    ChrTalk(
        0x101,
        "#0000F……遊撃士協会だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0757
    ChrTalk(
        0x101,
        (
            "#0012Fま、まぁ今では遊撃士協会は\x01",
            "大活躍してるけど……\x02\x03",

            "昔は警察がその役目を担って、\x01",
            "人々を守っていたんだ。\x02\x03",

            "#0006F（め、滅茶苦茶言っちゃったぞ……\x01",
            "  やっぱりまだ緊張してるのか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC88")

    label("loc_FB61")


    #C0758
    ChrTalk(
        0x101,
        (
            "#0000F……軍隊だ。\x02\x03",

            "例えばお隣のエレボニアでは\x01",
            "軍隊が防犯や防衛などを\x01",
            "統括しているんだけど……\x02\x03",

            "軍隊を持てないクロスベルでは、\x01",
            "その役目をいくつかの組織に\x01",
            "分担しているんだ。\x02\x03",

            "……そのうち、\x01",
            "事件の捜査や防犯を担うのが\x01",
            "俺たち警察ってわけさ。\x02\x03",

            "#0004F（よし、間違いないはずだ。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_FC88")

    label("loc_FC88")

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
            "#0000F警察には部署というものがあって、\x01",
            "役割ごとに人員を分けているんだ。\x02\x03",

            "事件の種類や緊急度によって\x01",
            "動員する部署を分担することで、\x01",
            "適切な対応を行なうんだ。\x02\x03",

            "#0003F中でも、社会を揺るがすような\x01",
            "大きな事件や、国際的な案件を\x01",
            "引き受ける部署が……\x02",
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
            "大きな事件や、国際的な案件を\x01",
            "引き受ける部署は？",
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
            "【①捜査一課】\x01",        # 0
            "【②捜査二課】\x01",        # 1
            "【③特務支援課】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FE60"),
        (1, "loc_FF64"),
        (2, "loc_10089"),
        (SWITCH_DEFAULT, "loc_101A7"),
    )


    label("loc_FE60")


    #C0761
    ChrTalk(
        0x101,
        (
            "#0000F……捜査一課だ。\x02\x03",

            "誘拐、殺人など大きな事件を\x01",
            "解決するには、一流の捜査官が\x01",
            "全力を尽くす必要がある。\x02\x03",

            "それらを一手に引き受ける\x01",
            "エリート捜査官の集まりが\x01",
            "捜査一課というわけさ。\x02\x03",

            "#0004F（俺たちも負けてられない。\x01",
            "  頑張っていかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_101A7")

    label("loc_FF64")


    #C0762
    ChrTalk(
        0x101,
        "#0000F……捜査二課だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0763
    ChrTalk(
        0x101,
        (
            "#0000F誘拐、殺人などの大きな事件を\x01",
            "解決するには、当然小さな事件も\x01",
            "片付けられる能力が必要だ。\x02\x03",

            "普段から窃盗などの捜査にあたる\x01",
            "捜査二課が、地道に大事件を\x01",
            "捜査していくんだよ。\x02\x03",

            "#0006F（……もっともらしく\x01",
            "  言ってしまったけど……\x01",
            "  本当にそうだっけ？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101A7")

    label("loc_10089")


    #C0764
    ChrTalk(
        0x101,
        "#0000F……俺たち、特務支援課だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0765
    ChrTalk(
        0x101,
        (
            "#0000F誘拐、殺人などの大きな事件を\x01",
            "解決するには、広い範囲での\x01",
            "捜査活動が重要になる。\x02\x03",

            "そういう意味では、\x01",
            "フットワークの軽い特務支援課は\x01",
            "大事件の捜査に最適なのさ。\x02\x03",

            "#0006F（……って、さすがに自分たちを\x01",
            "  カッコよく言いすぎだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101A7")

    label("loc_101A7")

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
            "#0000F警察官一人一人には\x01",
            "捜査手帳という物が渡される。\x02\x03",

            "この捜査手帳には、\x01",
            "身分証明として使われるほかに\x01",
            "最大かつ重要な用途があるんだ。\x02\x03",

            "#0003Fそれは……\x02",
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
            "捜査手帳の重要な用途は？",
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
            "【①捜査状況の記録】\x01",      # 0
            "【②逮捕状の代替品】\x01",      # 1
            "【③位置情報の発信】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1031E"),
        (1, "loc_10400"),
        (2, "loc_10514"),
        (SWITCH_DEFAULT, "loc_105F5"),
    )


    label("loc_1031E")


    #C0768
    ChrTalk(
        0x101,
        (
            "#0000F……捜査状況の記録だ。\x01",
            "ようするに、メモ帳だね。\x02\x03",

            "任務の状況を整理するのに便利だし、\x01",
            "これを元に勤務査定や諸経費を決定する。\x02\x03",

            "まさに、警察官の\x01",
            "必需品というべき物なんだ。\x02\x03",

            "#0004F（うん、バッチリだな。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_105F5")

    label("loc_10400")


    #C0769
    ChrTalk(
        0x101,
        "#0000F……逮捕状の代替品だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0770
    ChrTalk(
        0x101,
        (
            "#0012Fえ、えっと、容疑者を確保するには\x01",
            "あらかじめ警察本部への申請が\x01",
            "必要なんだけど……\x02\x03",

            "#0000F緊急時はこれを提示すれば、\x01",
            "逮捕状がなくても容疑者を\x01",
            "確保することができるのさ。\x02\x03",

            "#0006F（う、うーん……\x01",
            "  ちょっと自信がないな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105F5")

    label("loc_10514")


    #C0771
    ChrTalk(
        0x101,
        "#0000F……位置情報の発信だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0772
    ChrTalk(
        0x101,
        (
            "#0012Fえ、えっと……\x01",
            "この手帳には居場所を送信する\x01",
            "機能がついていて……\x02\x03",

            "#0000F出先でも仲間たちに\x01",
            "居場所が分かるように\x01",
            "なっているんだ。\x02\x03",

            "#0006F（さ、さすがに無理があるなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105F5")

    label("loc_105F5")

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
            "#0000F警察は、遊撃士のように\x01",
            "最新の戦術オーブメントを\x01",
            "実戦配備しているんだ。\x02\x03",

            "#0003F警察は戦闘のプロ集団じゃないけど、\x01",
            "捜査官が犯人を追跡するときには\x01",
            "戦闘が避けられない事も多いからね。\x02\x03",

            "#0000Fちなみに、戦術オーブメントの規格は\x01",
            "既に何世代も変わっていてね。\x01",
            "その都度新たな機能が追加されるんだ。\x02\x03",

            "#0003F現在使用されている\x01",
            "戦術オーブメントの規格は……\x02",
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
            "現在の戦術オーブメントの規格は？",
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
            "【①第５世代】\x01",      # 0
            "【②第６世代】\x01",      # 1
            "【③第７世代】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10826"),
        (1, "loc_1091F"),
        (2, "loc_10A23"),
        (SWITCH_DEFAULT, "loc_10B15"),
    )


    label("loc_10826")


    #C0775
    ChrTalk(
        0x101,
        (
            "#0000F……第５世代、\x01",
            "通称『ＥＮＩＧＭＡ#12R エ　　ニ　　グ　　マ#』と\x01",
            "呼ばれているものだ。\x02\x03",

            "エニグマは通信器を内蔵していてね。\x01",
            "緊急時も連絡がつくようになったから\x01",
            "警察業務には特に重宝するんだよ。\x02\x03",

            "#0004F（うん、合ってたはずだ。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_10B15")

    label("loc_1091F")


    #C0776
    ChrTalk(
        0x101,
        (
            "#0000F……第６世代、\x01",
            "通称『ＥＮＩＧＭＡ#12R エ　　ニ　　グ　　マ#』と\x01",
            "呼ばれているものだ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0777
    ChrTalk(
        0x101,
        (
            "#0000F規格が変わると結晶回路（クオーツ）も\x01",
            "新調しないといけないから、\x01",
            "対応するのは大変なんだ。\x02\x03",

            "#0006F（……あれ、第６世代で\x01",
            "  良かったっけ……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B15")

    label("loc_10A23")


    #C0778
    ChrTalk(
        0x101,
        (
            "#0000F……第７世代、\x01",
            "通称『ＥＮＩＧＭＡ#12R エ　　ニ　　グ　　マ#』と\x01",
            "呼ばれているものだ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0779
    ChrTalk(
        0x101,
        (
            "#0012Fい、いやぁ……\x01",
            "次々と新しくなると\x01",
            "対応するのも大変なんだよな。\x02\x03",

            "#0006F（う、うーん……\x01",
            "  そんなに世代交代してたかな……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B15")

    label("loc_10B15")

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
            "#0000Fお巡りさんや捜査官のように、\x01",
            "色々な役職の警察官が\x01",
            "クロスベルの為に働いてる。\x02\x03",

            "#0003F一見すると、それらは\x01",
            "全く関係のないもののようだけど……\x02\x03",

            "#0000Fでも、警察の仕事は全て、\x01",
            "ある基本理念に基づいて\x01",
            "行なわれているんだ。\x02\x03",

            "#0003Fその基本理念とは…………\x02",
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
            "警察の基本理念とは？",
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
            "【①クロスベル市民の安全保障】\x01",        # 0
            "【②治安維持と自治州法の遵守】\x01",        # 1
            "【③諸外国への警戒と平和の維持】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10D0E"),
        (1, "loc_10DF6"),
        (2, "loc_10F5F"),
        (SWITCH_DEFAULT, "loc_110A4"),
    )


    label("loc_10D0E")


    #C0782
    ChrTalk(
        0x101,
        "#0000F……クロスベル市民の安全保障だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0783
    ChrTalk(
        0x101,
        (
            "#0000Fたとえどんな状況でも、\x01",
            "クロスベル市民を守ること……\x02\x03",

            "皆が安心して暮らせる社会を\x01",
            "作っていくのが警察の本質なんだよ。\x02\x03",

            "#0006F（う、うーん。\x01",
            "  ちょっと説明不足かな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110A4")

    label("loc_10DF6")


    #C0784
    ChrTalk(
        0x101,
        (
            "#0000F……治安維持と自治州法の遵守だ。\x02\x03",

            "ルールを破る人を取り締まることで\x01",
            "皆が安心して暮らせる社会を\x01",
            "作っていくのはもちろんのこと……\x02\x03",

            "自分たちが法を守る姿を見せて\x01",
            "市民たちの規範となり、\x01",
            "発生する犯罪を抑制していくんだ。\x02\x03",

            "そうして治安を維持して、\x01",
            "犯罪の起きない世の中を目指すのが\x01",
            "警察の本質なんだよ。\x02\x03",

            "#0004F（よし……上手くまとめられたぞ！）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_110A4")

    label("loc_10F5F")


    #C0785
    ChrTalk(
        0x101,
        "#0000F……諸外国への警戒と平和の維持だ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    #C0786
    ChrTalk(
        0x101,
        (
            "#0000F帝国と共和国という\x01",
            "２つの国に挟まれているクロスベルは、\x01",
            "とても犯罪の起きやすい場所だ。\x02\x03",

            "他国からの敵の侵入を取り締まって、\x01",
            "皆が安心して暮らせる社会を\x01",
            "作っていくのが警察の本質なんだよ。\x02\x03",

            "#0006F（……って、これは\x01",
            "  どっちかっていうと\x01",
            "  警備隊の仕事だな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110A4")

    label("loc_110A4")

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
            "#0004F──以上、クロスベル警察は\x01",
            "こういう組織なんだ。\x02\x03",

            "#0000F……難しかったかもしれないけど、\x01",
            "わかってもらえたかな？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(152620, 1500, 3180, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113DB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11263")

    #C0788
    ChrTalk(
        0x102,
        (
            "#6P#0100F（これで授業の前半は終わりね。）\x02\x03",

            "#0104F（最初は緊張してたけど、\x01",
            "  それを少しも感じさせない\x01",
            "  立派な先生ぶりだわ。）\x02\x03",

            "#0100F（捜査官試験に合格したという\x01",
            "  実力は伊達じゃないわね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113D6")

    label("loc_11263")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11318")

    #C0789
    ChrTalk(
        0x102,
        (
            "#6P#0100F（これで授業の前半は終わりね。）\x02\x03",

            "#0103F（うーん、さすがのロイドも\x01",
            "  ちょっと苦戦しているみたい。）\x02\x03",

            "（最初の緊張を\x01",
            "  引きずっちゃったのかしら。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113D6")

    label("loc_11318")


    #C0790
    ChrTalk(
        0x102,
        (
            "#6P#0103F（これで授業の前半は終わりね。）\x02\x03",

            "#0111F（それにしても……\x01",
            "  ロイドだったらもう少し\x01",
            "  頑張れると思ったんだけど。）\x02\x03",

            "（これは、マーブル先生も\x01",
            "  アテが外れたんじゃないかしら。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113D6")

    Jump("loc_11914")

    label("loc_113DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1167D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_114D3")

    #C0791
    ChrTalk(
        0x103,
        (
            "#6P#0200F（ようやく授業の前半パートが\x01",
            "  終わりました。）\x02\x03",

            "#0204F（的確に要点を抑えて、\x01",
            "  通る声でしっかりと教える……\x01",
            "  実に見事です。）\x02\x03",

            "（案外、大学などで\x01",
            "  教鞭をとっていても\x01",
            "  成功したかもしれません。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11678")

    label("loc_114D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115A7")

    #C0792
    ChrTalk(
        0x103,
        (
            "#6P#0200F（ようやく授業の前半パートが\x01",
            "  終わりました。）\x02\x03",

            "#0203F（時々自信の無い声色で\x01",
            "  話していたのは心配ですが……）\x02\x03",

            "（わたしたちのリーダーである以上\x01",
            "  もう少し頑張って欲しいです。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11678")

    label("loc_115A7")


    #C0793
    ChrTalk(
        0x103,
        (
            "#6P#0203F（ようやく授業の前半パートが\x01",
            "  終わりました。）\x02\x03",

            "#0211F（……目はあさっての方向を向き、\x01",
            "  身振り手振りは挙動不審……）\x02\x03",

            "（……お粗末な出来です。\x01",
            "  わたしがやった方が\x01",
            "  まだマシだったんじゃ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11678")

    Jump("loc_11914")

    label("loc_1167D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11914")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11751")

    #C0794
    ChrTalk(
        0x104,
        (
            "#6P#0305F（お、今ので前半戦終了か。）\x02\x03",

            "#0309F（いやぁ、なかなか\x01",
            "  サマになってるもんだねぇ。）\x02\x03",

            "#0303F（世のレディたちは\x01",
            "  ああいう男に弱いんだよなぁ。\x01",
            "  憎らしい奴……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11914")

    label("loc_11751")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11846")

    #C0795
    ChrTalk(
        0x104,
        (
            "#6P#0305F（お、今ので前半戦終了か。）\x02\x03",

            "#0303F（しかしまぁ、危なっかしいな。\x01",
            "  俺でも分かる間違いを犯すのは\x01",
            "  どうかと思うぜ。）\x02\x03",

            "#0309F（ま、ちっとくらい抜けてた方が\x01",
            "  レディたちの母性本能を\x01",
            "  くすぐるかもしれねぇな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11914")

    label("loc_11846")


    #C0796
    ChrTalk(
        0x104,
        (
            "#6P#0300F（お、今ので前半戦終了か。）\x02\x03",

            "#0306F（まったく、あんまりガキの前で\x01",
            "  カッコ悪いとこ見せるなよ～。）\x02\x03",

            "（ミシュラムで発掘したメガネキャラ、\x01",
            "  インテリアピールが皆無じゃ\x01",
            "  ちょっと勿体無いぜ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11914")

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
            "#5P……それじゃあ皆さん。\x01",
            "ロイド先生に\x01",
            "なにか質問はあるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0xC,
        (
            "#5P先生は優しいから、\x01",
            "きっと何でも答えてくれるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x101,
        (
            "#11P#0005F（マ、マーブル先生！？\x01",
            "  そんなムチャ振りを……）\x02\x03",

            "#0006F（……はあ、やるしかなさそうだな。）\x02",
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
            "　 質問タイムスタート！\x01",
            "～日頃の疑問を何でも質問～\x02",
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
            "※正しい答えを選んで\x01",
            "　きわどい問題を乗り切れ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0802
    ChrTalk(
        0x101,
        "#0000F……それじゃ、なにか質問はあるかい？\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0803
    ChrTalk(
        0xF,
        (
            "#5Pハイ、ハーイ！\x01",
            "おいら！　おいら！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(149370, 1500, 14370, 2000)
    OP_93(0x101, 0xE1, 0x12C)
    OP_6F(0x79)

    #C0804
    ChrTalk(
        0x101,
        "#11P#0000Fん、どんな質問だい？\x02",
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0xF,
        (
            "#6P先生みたいな警察官って、\x01",
            "どうやったらなれるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0xF,
        (
            "#6P……や、別になるつもりは\x01",
            "これっぽっちもないけどさ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)

    #C0807
    ChrTalk(
        0x10,
        (
            "#6Pちょっとタミル。\x01",
            "それはさすがに失礼なんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x101,
        (
            "#11P#0006Fま、まぁいいよ……\x02\x03",

            "#0000F何か特別な資格が必要か？\x01",
            "ってことだな。\x02\x03",

            "そうだな、警察官になる為には……\x02",
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
            "警察官になる為には\x01",
            "どうすればいい？",
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
            "【①捜査官の試験に合格する】\x01",      # 0
            "【②警察学校を卒業する】\x01",          # 1
            "【③特に決まった方法はない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11D5F"),
        (1, "loc_11EF2"),
        (2, "loc_120B3"),
        (SWITCH_DEFAULT, "loc_12271"),
    )


    label("loc_11D5F")


    #C0810
    ChrTalk(
        0x101,
        (
            "#11P#0000F……捜査官の試験に\x01",
            "合格することかな。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0811
    ChrTalk(
        0x101,
        (
            "#11P#0006Fい、いや……\x01",
            "警察官になるだけだったら\x01",
            "捜査官試験は必須じゃなかった……\x02\x03",

            "#0000F基本的に、警察学校のカリキュラムを\x01",
            "しっかりと修了してさえいれば\x01",
            "警察官になることはできるんだ。\x02\x03",

            "俺の仲間のように、警察学校に行かずに\x01",
            "警察に入る人もいるけど……\x01",
            "これはけっこう特殊な例かな。\x02\x03",

            "#0006F（あ、危ない危ない。\x01",
            "  間違えるところだったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12271")

    label("loc_11EF2")


    #C0812
    ChrTalk(
        0x101,
        (
            "#11P#0000F……警察学校を卒業する\x01",
            "ことかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x101,
        (
            "#11P#0000F基本的に、学校のカリキュラムを\x01",
            "しっかりと修了してさえいれば\x01",
            "警察官になることはできるんだ。\x02\x03",

            "ただ、さっきも言ったけど\x01",
            "警察には色々な役職があるからね。\x02\x03",

            "例えば捜査官を目指す場合は、\x01",
            "カリキュラムとは別に捜査官の試験に\x01",
            "合格する必要があるんだ。\x02\x03",

            "俺の仲間のように、警察学校に行かずに\x01",
            "警察に入る人もいるけど……\x01",
            "これはけっこう特殊な例だな。\x02\x03",

            "#0004F（うん、こんなとこだろう。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_12271")

    label("loc_120B3")


    #C0814
    ChrTalk(
        0x101,
        (
            "#11P#0000F……実は、特に\x01",
            "決まった方法は無いんだ。\x02",
        )
    )

    BeginChrThread(0x101, 3, 0, 50)

    #C0815
    ChrTalk(
        0x101,
        (
            "#11P#0006Fい、いや……確かに俺の仲間は\x01",
            "警察学校に行かずに\x01",
            "警察に入ってきたけど……\x02\x03",

            "#0000F本来は、警察学校のカリキュラムを\x01",
            "しっかりと修了していなければ\x01",
            "警察官になることはできないんだ。\x02\x03",

            "あと、さっきも言ったけど\x01",
            "警察には色々な役職があるからね。\x02\x03",

            "例えば捜査官を目指す場合は、\x01",
            "カリキュラムとは別に捜査官の試験に\x01",
            "合格する必要があるんだ。\x02\x03",

            "#0006F（うー、ちょっと混乱してたな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12271")

    label("loc_12271")

    SetChrSubChip(0x10, 0x0)

    #C0816
    ChrTalk(
        0xF,
        "#6Pふ～ん、なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0xF,
        (
            "#6P別に警察官目指してないけど……\x01",
            "教えてくれてあんがと、先生！\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x15,
        (
            "#5Pあ、じゃあ……\x01",
            "僕も質問いいですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(152570, 1200, 14810, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    #C0819
    ChrTalk(
        0x101,
        "#5P#0000Fうん、なんだい？\x02",
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x15,
        (
            "#12Pクロスベルで起こる事件って、\x01",
            "なんかあんまり詳しく伝わらないから\x01",
            "よく分からないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x15,
        (
            "#12Pこの間の狼型魔獣の事件、\x01",
            "最後の決め手は\x01",
            "なんだったんですか？？\x02",
        )
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあぁ、あのマフィアが\x01",
            "軍用犬を悪用した事件だな。\x02\x03",

            "#0003Fたしか、あの事件を\x01",
            "決めたのは……\x02",
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
            "軍用犬事件解決の決め手は？",
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
            "【①特務支援課の推理】\x01",      # 0
            "【②白い狼の助太刀】\x01",        # 1
            "【③警備隊の応援】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12501"),
        (1, "loc_12663"),
        (2, "loc_1276E"),
        (SWITCH_DEFAULT, "loc_1287E"),
    )


    label("loc_12501")


    #C0824
    ChrTalk(
        0x101,
        "#5P#0000F……特務支援課の推理だよ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0825
    ChrTalk(
        0x101,
        (
            "#5P#0006Fあっ、でも……\x01",
            "最後の最後にピンチになった所を\x01",
            "ツァイトに救われたんだよな。\x02\x03",

            "あれが無かったら、\x01",
            "真相を知る俺たちがやられて\x01",
            "事件は解決できなかったろうし……\x02\x03",

            "#0000Fだったらやっぱり、\x01",
            "ツァイトたち白い狼が\x01",
            "決め手だったって事になるかな。\x02\x03",

            "#0006F（うーん……\x01",
            "  ツァイトに申し訳ない答えだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1287E")

    label("loc_12663")


    #C0826
    ChrTalk(
        0x101,
        (
            "#5P#0000F……白い狼の助太刀だよ。\x02\x03",

            "後一歩の所で軍用犬に\x01",
            "やられてしまうところを、\x01",
            "白い狼の群れが助けてくれたんだ。\x02\x03",

            "その後、縁があって\x01",
            "群れにいたツァイトが\x01",
            "ウチに居座るようになったんだ。\x02\x03",

            "#0004F（あれは衝撃的だったからな……\x01",
            "  忘れるわけないか。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1287E")

    label("loc_1276E")


    #C0827
    ChrTalk(
        0x101,
        "#5P#0000F……警備隊の応援だよ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0828
    ChrTalk(
        0x101,
        (
            "#5P#0005Fん……？　確かに最後\x01",
            "警備隊に引き渡したけど……\x01",
            "決め手というとその前かな。\x02\x03",

            "#0000F絶対絶命のピンチを\x01",
            "ツァイトたちに救われて、\x01",
            "ようやく逮捕できたんだ。\x02\x03",

            "#0006F（うう、ちょっと思い違いを\x01",
            "  してたみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1287E")

    label("loc_1287E")


    #C0829
    ChrTalk(
        0x15,
        (
            "#12Pへぇ……ツァイトって\x01",
            "やっぱりすごいんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x15,
        "#12Pありがとう、お兄さん。\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0831
    ChrTalk(
        0x11,
        (
            "#6P#Nえ、えと……はい先生。\x01",
            "し、しつもんです……\x02",
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
        "#11P#0000Fうん、何かな。\x02",
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x11,
        (
            "#6Pあのね、前にリュウくんと\x01",
            "アンリくんが地下で迷子になった\x01",
            "ことがあったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x11,
        "#6Pあそこって、どこだったの？\x02",
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
            "#5Pバッ……モモ！\x01",
            "かっこ悪いことぶり返すなよ～！\x02",
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
            "#6Pだ、だってリュウくん達、\x01",
            "教えてくれないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x101,
        (
            "#11P#0000Fあのジオフロントでの事件か……\x02\x03",

            "#0003F子供たちが迷い込んだのは……\x02",
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
            "リュウとアンリが\x01",
            "迷い込んだ場所は？",
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
            "【①ジオフロント・Ａ区画】\x01",      # 0
            "【②ジオフロント・Ｂ区画】\x01",      # 1
            "【③ジオフロント・Ｃ区画】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12B95"),
        (1, "loc_12C5C"),
        (2, "loc_12DA1"),
        (SWITCH_DEFAULT, "loc_12EF8"),
    )


    label("loc_12B95")


    #C0839
    ChrTalk(
        0x101,
        (
            "#11P#0000F……ジオフロント・Ａ区画だったな。\x02\x03",

            "あの時は魔獣が出て大変だったけど、\x01",
            "アリオスさんの助太刀もあって\x01",
            "なんとか全員無事に帰還できたんだ。\x02\x03",

            "#0004F（うん、問題なさそうだ。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_12EF8")

    label("loc_12C5C")


    #C0840
    ChrTalk(
        0x101,
        (
            "#11P#0000F……ジオフロント・Ｂ区画だったな。\x02\x03",

            "#0005F……ん？\x01",
            "なんかちがう……？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0841
    ChrTalk(
        0x15,
        "#12Pあれ？　確か、Ａ区画だったような……\x02",
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x101,
        (
            "#11P#0012Fそ、そうだったか。\x02\x03",

            "#0003Fま、まぁとにかく……\x01",
            "あの時はアリオスさんのおかげで\x01",
            "なんとか全員無事に帰還できたんだ。\x02\x03",

            "#0006F（そうか、Ｂ区画は\x01",
            "  ヨナのいる所だったな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EF8")

    label("loc_12DA1")


    #C0843
    ChrTalk(
        0x101,
        (
            "#11P#0000F……ジオフロント・Ｃ区画だったな。\x02\x03",

            "#0005F……あれ、Ｃ区画は\x01",
            "入ったことがあったっけか……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    #C0844
    ChrTalk(
        0x15,
        "#12Pあれ？　確か、Ａ区画だったような……\x02",
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x101,
        (
            "#11P#0012Fそ、そうだったか。\x02\x03",

            "#0003Fま、まぁとにかく……\x01",
            "あの時はアリオスさんのおかげで\x01",
            "なんとか全員無事に帰還できたんだ。\x02\x03",

            "#0006F（うーん、ちょっと記憶が\x01",
            "  あいまいだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EF8")

    label("loc_12EF8")


    #C0846
    ChrTalk(
        0x11,
        (
            "#6Pへ、へぇ……\x01",
            "先生、ありがとう。\x02",
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
        "#11P#0000F……さて、他に質問があるかな？\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0848
    ChrTalk(
        0x21,
        "#6Pハイッ！　質問思いついた！\x02",
    )

    CloseMessageWindow()
    OP_68(152480, 1500, 13840, 2000)
    SetCameraDistance(29120, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    #C0849
    ChrTalk(
        0x101,
        "#11P#0000Fはい、どうぞ。\x02",
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x21,
        "#6P前から聞きたかったんだけど……\x02",
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x21,
        (
            "#6P兄ちゃんたちのいる警察と、\x01",
            "遊撃士協会って何が違うワケ？\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x21,
        (
            "#6Pどっちも一応、悪いやつを\x01",
            "やっつけるのは同じなんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x101,
        (
            "#11P#0003F（わりと重いパンチが来たな……）\x02\x03",

            "#0000Fうん、でも皆気になってるよな。\x01",
            "この際だから答えよう。\x02\x03",

            "#0003F俺たち警察と遊撃士の\x01",
            "明確な違い、それは……\x02",
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
            "警察と遊撃士協会の\x01",
            "明確な違いは？",
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
            "【①逮捕権の有無】\x01",            # 0
            "【②公的権力への干渉力】\x01",      # 1
            "【③ほとんどない】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_131F1"),
        (1, "loc_1338D"),
        (2, "loc_1352D"),
        (SWITCH_DEFAULT, "loc_136AE"),
    )


    label("loc_131F1")


    #C0855
    ChrTalk(
        0x101,
        "#11P#0000F……逮捕権の有無、かな。\x02",
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
            "#11P#0011Fい、いや、遊撃士も\x01",
            "普通の逮捕権なら持ってるんだ。\x02\x03",

            "#0003F──えっと、遊撃士には\x01",
            "国や自治州の偉い人を直接、\x01",
            "逮捕することは出来ないんだ。\x02\x03",

            "もちろん、いきなり暴れて\x01",
            "他人を傷つけたりした場合は\x01",
            "問答無用で逮捕できるけどね。\x02\x03",

            "#0001Fそれに対して、警察は一応、\x01",
            "政治家やお役人も逮捕できる事に\x01",
            "なってるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136AE")

    label("loc_1338D")


    #C0857
    ChrTalk(
        0x101,
        (
            "#11P#0004F難しい話になるけど……\x01",
            "遊撃士には『規約』があるんだ。\x02\x03",

            "この規約があるからこそ\x01",
            "ギルドは色んな国での設立を\x01",
            "認められているんだけど……\x02\x03",

            "#0000F──えっと、遊撃士には\x01",
            "国や自治州の偉い人を直接、\x01",
            "逮捕することは出来ないんだ。\x02\x03",

            "もちろん、いきなり暴れて\x01",
            "他人を傷つけたりした場合は\x01",
            "問答無用で逮捕できるけどね。\x02\x03",

            "#0003Fそれに対して、警察は一応、\x01",
            "政治家やお役人も逮捕できる事に\x01",
            "なってるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_136AE")

    label("loc_1352D")


    #C0858
    ChrTalk(
        0x101,
        "#11P#0004F……ほとんどない。\x02",
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
            "#11P#0011F（って、そんな訳ないだろ！）\x02\x03",

            "#0003F──えっと、遊撃士には\x01",
            "国や自治州の偉い人を直接、\x01",
            "逮捕することは出来ないんだ。\x02\x03",

            "もちろん、いきなり暴れて\x01",
            "他人を傷つけたりした場合は\x01",
            "問答無用で逮捕できるけどね。\x02\x03",

            "#0001Fそれに対して、警察は一応、\x01",
            "政治家やお役人も逮捕できる事に\x01",
            "なってるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136AE")

    label("loc_136AE")


    #C0860
    ChrTalk(
        0x21,
        (
            "#6Pえー、でも父ちゃん、\x01",
            "警察にモンク言ってたぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x21,
        (
            "#6Pオショク役人も逮捕できない\x01",
            "情けないやつらだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x15,
        (
            "#12Pだ、だからリュウ。\x01",
            "失礼だってば～。\x02",
        )
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x101,
        (
            "#11P#0006F……ああ。\x01",
            "俺たちの努力不足は確かだ。\x02\x03",

            "#0000Fすぐには無理だけど\x01",
            "何とか出来るよう頑張るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x21,
        "#6Pおう、応援してるぜ！\x02",
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x15,
        (
            "#12Pまったくもう……\x01",
            "ホント偉そうなんだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x12C)
    OP_6F(0x79)

    #C0866
    ChrTalk(
        0x101,
        (
            "#11P#0012Fはは……\x01",
            "えっと、それじゃあ\x01",
            "質問はこれくらいかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    #C0867
    ChrTalk(
        0x153,
        (
            "#6P#1109F#N──はいはーい！！\x01",
            "キーアも質問！　しつもーん！\x02",
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
            "#11P#0011Fキ、キーア……！？\x01",
            "（静かにしてると思ったら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x153,
        "#6P#1105Fね、質問、イイ？\x02",
    )

    CloseMessageWindow()

    #C0870
    ChrTalk(
        0x101,
        "#11P#0000Fあ、ああ構わないよ。\x02",
    )

    CloseMessageWindow()

    #C0871
    ChrTalk(
        0x153,
        (
            "#6P#1110Fあのね、ロイドって……\x02\x03",

            "どうして警察官になったの？\x02",
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
            "#11P#0005F（あ……）\x02\x03",

            "#0003Fえ、えーと……\x02",
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
            "#11P#0008F（特務支援課での最初の夜……\x01",
            "  似たようなことを考えたっけ。）\x02\x03",

            "#0004F（……そうだな。\x01",
            "  今なら答えられる気がする。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0874
    ChrTalk(
        0x153,
        "#6P#1105Fロイド？　どーしたの？\x02",
    )

    CloseMessageWindow()

    #C0875
    ChrTalk(
        0x101,
        (
            "#11P#0002F……いいや、なんでもないさ。\x02\x03",

            "#0003F（きっと、この質問に\x01",
            "  “正しい答え”はない。）\x02\x03",

            "（支援課にいたことで培った\x01",
            "  俺自身の、ありのままの心……\x01",
            "  それをぶつけてみよう。）\x02\x03",

            "#0000F俺が警察官になった理由。\x01",
            "それは……\x02",
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
            "ロイドが警察官になった理由は？",
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
            "【①強くなるため】\x01",          # 0
            "【②みんなを守るため】\x01",      # 1
            "【③わからない】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13C60"),
        (1, "loc_13E75"),
        (2, "loc_1404B"),
        (SWITCH_DEFAULT, "loc_142A8"),
    )


    label("loc_13C60")


    #C0877
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうだな、どう言ったらいいか\x01",
            "ちょっと迷うんだけど……\x02\x03",

            "#0000F困っている人を助けたり、\x01",
            "悪いことをしている人を\x01",
            "止めたいと思ったからかな。\x02\x03",

            "#0008Fそのためには、自分自身が\x01",
            "強くならなくちゃいけない……\x02\x03",

            "それが出来る場所が俺にとっては\x01",
            "警察だったんだけど……\x02\x03",

            "#0012F……ハハ、でもそれじゃあ\x01",
            "遊撃士とあんまり変わらないか。\x02\x03",

            "#0006Fゴメン……\x01",
            "うまく答えられないみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x153,
        (
            "#6P#1104Fんー、でも何かわかったー。\x02\x03",

            "#1110Fロイドだけのコダワリが\x01",
            "あるってことなんだよねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x101,
        (
            "#11P#0002Fはは……うん。\x01",
            "それは間違いないかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A8")

    label("loc_13E75")


    #C0880
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうだな、どう言ったらいいか\x01",
            "ちょっと迷うんだけど……\x02\x03",

            "#0000Fみんなを守りたい……\x01",
            "そう思ったからだと思う。\x02\x03",

            "#0008Fただ、みんなっていうのは\x01",
            "家族や友だちはもちろんだけど\x01",
            "それだけじゃないっていうか……\x02\x03",

            "クロスベルの市民？\x01",
            "いや、単純にそれだけじゃ……\x02\x03",

            "#0006F……ゴメン……\x01",
            "うまく答えられないみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x153,
        (
            "#6P#1104Fんー、でも何かわかったー。\x02\x03",

            "#1110Fロイドだけのコダワリが\x01",
            "あるってことなんだよねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x101,
        (
            "#11P#0002Fはは……うん。\x01",
            "それは間違いないかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A8")

    label("loc_1404B")


    #C0883
    ChrTalk(
        0x101,
        (
            "#11P#0006F正直なことを言うと……\x01",
            "今は、ちょっと判らないんだ。\x02\x03",

            "#0008F最初は、目標にしていた人に\x01",
            "追いつきたいと思って\x01",
            "同じ警察官を目指したんだけど……\x02\x03",

            "いざなってみると\x01",
            "それだけじゃなかったっていうか……\x02\x03",

            "#0003Fもちろん、兄貴に追いつきたいって\x01",
            "気持ちも変わらずにあるんだけど\x01",
            "単純に追いつきたいわけじゃなくて……\x02",
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
            "#11P#0011Fご、ごめんみんな。\x01",
            "何か変なことを話しちゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x153,
        (
            "#6P#1110Fんー、でも何かわかったー。\x02\x03",

            "#1109Fロイドがだいじなことを\x01",
            "いっしょうけんめい考えてるって－。\x02",
        )
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x101,
        (
            "#0002Fはは……\x01",
            "ありがとう、キーア。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A8")

    label("loc_142A8")

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
            "#5Pふふ……さて、質問は\x01",
            "こんなところでしょうかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0888
    ChrTalk(
        0xC,
        (
            "#5Pそれでは、ロイド先生の授業は\x01",
            "これで終わりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0xC,
        "#5P皆さん、先生にお礼を言いましょうね。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("子供たち")

    #A0890
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5Sありがとうございました～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0891
    ChrTalk(
        0x101,
        "#11P#0000Fはは……それじゃ、またな。\x02",
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

    # Function_45_EB0C end

    def Function_46_14409(): pass

    label("Function_46_14409")

    OP_95(0xFE, 151000, 200, 17500, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_46_14409 end

    def Function_47_14425(): pass

    label("Function_47_14425")

    OP_93(0xFE, 0x10E, 0x12C)
    OP_98(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_47_14425 end

    def Function_48_14448(): pass

    label("Function_48_14448")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14645")

    #C0892
    ChrTalk(
        0xC,
        (
            "#12Pお疲れ様、ロイド。\x01",
            "今日は本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0893
    ChrTalk(
        0xC,
        (
            "#12P子供たちも皆、\x01",
            "楽しんで聞いていたようですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x101,
        (
            "#5P#0009Fはは……\x01",
            "そうだといいんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0xC,
        "#12Pふふ、謙遜しなくていいのよ。\x02",
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0xC,
        (
            "#12Pとても素晴らしい授業でした。\x01",
            "私も存分に勉強させてもらったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0xC,
        (
            "#12P教壇に立つあなたを見て\x01",
            "成長を感じられたのが\x01",
            "何より、嬉しかったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x1)
    Jump("loc_14882")

    label("loc_14645")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14778")

    #C0898
    ChrTalk(
        0xC,
        (
            "#12Pお疲れ様、ロイド。\x01",
            "今日は本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0xC,
        (
            "#12P子供たちも皆、\x01",
            "楽しんで聞いていたようですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x101,
        (
            "#5P#0000Fはは……\x01",
            "そうだといいんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0xC,
        (
            "#12Pふふ、私も存分に\x01",
            "勉強させてもらったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0902
    ChrTalk(
        0xC,
        (
            "#12P教壇に立つあなたを見て\x01",
            "成長を感じられたのが\x01",
            "何より、嬉しかったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x2)
    Jump("loc_14882")

    label("loc_14778")


    #C0903
    ChrTalk(
        0xC,
        (
            "#12Pお疲れ様、ロイド。\x01",
            "今日は本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0904
    ChrTalk(
        0xC,
        (
            "#12Pだけど、少しお勉強が\x01",
            "足りなかったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0x101,
        (
            "#5P#0006Fい、いえ……\x01",
            "本当、すみませんでした。\x02\x03",

            "自分の知識の足りなさが\x01",
            "恥ずかしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0xC,
        (
            "#12Pううん、忙しいときに\x01",
            "頼んでしまった私も悪かったわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x3)

    label("loc_14882")

    TurnDirection(0x153, 0x101, 500)

    #C0907
    ChrTalk(
        0x153,
        (
            "#5P#1109Fキーア、ロイドの授業\x01",
            "たのしかったよー！\x02\x03",

            "#1100F言ってる事はほとんど\x01",
            "イミわかんなかったけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_14911():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14911)
    Sleep(50)

    def lambda_14921():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_14921)
    Sleep(1000)

    #C0908
    ChrTalk(
        0x101,
        (
            "#12P#0003Fうーん……さすがに子供には\x01",
            "ちょっと難しい授業だったかもな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1497C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1497C)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14B2A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_14A65")

    #C0909
    ChrTalk(
        0x102,
        (
            "#5P#0103Fほんと、もう少し努力しなくてはね。\x02\x03",

            "#0111Fあれだけ醜態を晒したら、\x01",
            "子供たちもある意味、警察に対して\x01",
            "親しんでくれたと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0910
    ChrTalk(
        0x101,
        "#12P#0006Fけ、結果オーライということで一つ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B25")

    label("loc_14A65")


    #C0911
    ChrTalk(
        0x102,
        (
            "#5P#0104Fふふ、無事にやり遂げられて\x01",
            "よかったじゃない。\x02\x03",

            "#0100F子供たちも、警察に対して\x01",
            "前より親しみが持てたと思うわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0912
    ChrTalk(
        0x101,
        (
            "#12P#0004F……まぁ、こういう機会を\x01",
            "持てただけでも収穫だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B25")

    Jump("loc_14E5B")

    label("loc_14B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14CBC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_14BFD")

    #C0913
    ChrTalk(
        0x103,
        (
            "#5P#0203F……興味深い授業で\x01",
            "あったことは確かです。\x02\x03",

            "#0211Fある意味、警察を近しい存在に\x01",
            "感じてくれたのではないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x101,
        "#12P#0006Fけ、結果オーライということで一つ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14CB7")

    label("loc_14BFD")


    #C0915
    ChrTalk(
        0x103,
        (
            "#5P#0204F無事に終了して\x01",
            "よかったと思います。\x02\x03",

            "#0202F子供たちも、警察に対して\x01",
            "良いイメージを受けたのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x101,
        (
            "#12P#0004F……まぁ、こういう機会を\x01",
            "持てただけでも収穫だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CB7")

    Jump("loc_14E5B")

    label("loc_14CBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14E5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_14D98")

    #C0917
    ChrTalk(
        0x104,
        (
            "#5P#0306Fいやはや、あんな\x01",
            "デタラメな事を教えるとはなぁ。\x02\x03",

            "#0309Fま、ある意味ガキどもも\x01",
            "警察に良い印象を\x01",
            "持ってくれたんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x101,
        "#12P#0006Fけ、結果オーライということで一つ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14E5B")

    label("loc_14D98")


    #C0919
    ChrTalk(
        0x104,
        (
            "#5P#0300Fま、無事終わっただけでも\x01",
            "よしとしようぜ。\x02\x03",

            "#0309Fガキどもも、警察に対して\x01",
            "いい印象を持ってくれた\x01",
            "ようだったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0920
    ChrTalk(
        0x101,
        (
            "#12P#0004F……まぁ、こういう機会を\x01",
            "持てただけでも収穫だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E5B")


    def lambda_14E60():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14E60)

    def lambda_14E6D():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_14E6D)

    def lambda_14E7A():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_14E7A)

    #C0921
    ChrTalk(
        0xC,
        (
            "#12P……それじゃあ、\x01",
            "まだ授業が残っているから\x01",
            "私は失礼するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0922
    ChrTalk(
        0xC,
        (
            "#12Pキーアさん。\x01",
            "もしよかったら、これからも\x01",
            "日曜学校にいらっしゃいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0923
    ChrTalk(
        0xC,
        (
            "#12P他の子供たちも\x01",
            "きっと歓迎してくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0924
    ChrTalk(
        0x153,
        (
            "#5P#1110Fうん！　今は忙しいけど……\x01",
            "絶対また来るね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0925
    ChrTalk(
        0x101,
        (
            "#5P#0000F（はは……キーアは日曜学校を\x01",
            "　随分気に入ってくれたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1513C")
    OP_2C(0x27, 0x3)

    #C0926
    ChrTalk(
        0xC,
        "#12Pふふ、楽しみにしているわ。\x02",
    )

    CloseMessageWindow()

    #C0927
    ChrTalk(
        0xC,
        (
            "#12P……そうそう、ロイド\x01",
            "これを受け取ってもらえるかしら？\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x61, 1)

    #C0929
    ChrTalk(
        0x101,
        "#5P#0005Fそんな……いいんですか？\x02",
    )

    CloseMessageWindow()

    #C0930
    ChrTalk(
        0xC,
        (
            "#12P忙しい中、素晴らしい授業を\x01",
            "聞かせてくれたお礼よ。\x01",
            "気にせず受け取ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0931
    ChrTalk(
        0xC,
        "#12P……それじゃあ、またね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1517E")

    label("loc_1513C")


    #C0932
    ChrTalk(
        0xC,
        "#12Pふふ、楽しみにしているわ。\x02",
    )

    CloseMessageWindow()

    #C0933
    ChrTalk(
        0xC,
        "#12Pそれじゃあ、またね。\x02",
    )

    CloseMessageWindow()

    label("loc_1517E")

    BeginChrThread(0xC, 3, 0, 49)
    WaitChrThread(0xC, 3)

    #C0934
    ChrTalk(
        0x101,
        (
            "#5P#0003F……さて、と。\x01",
            "ちょっと寄り道に\x01",
            "なっちゃったけど……\x02\x03",

            "#0000Fそろそろ病院に向かうとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15241")

    #C0935
    ChrTalk(
        0x102,
        (
            "#5P#0100Fそうね。\x01",
            "バスが出ている南口に\x01",
            "急ぎましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152DE")

    label("loc_15241")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15299")

    #C0936
    ChrTalk(
        0x103,
        (
            "#5P#0200F……そうですね。\x01",
            "バスが出ている南口に\x01",
            "急ぎましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152DE")

    label("loc_15299")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152DE")

    #C0937
    ChrTalk(
        0x104,
        (
            "#5P#0300Fだな。\x01",
            "バスが出ている南口に\x01",
            "急ごうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152DE")


    #C0938
    ChrTalk(
        0x153,
        "#5P#1110Fうん、行こー！\x02",
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
            "クエスト【日曜学校の特別講師】\x07\x00",
            "を達成した！\x02",
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

    # Function_48_14448 end

    def Function_49_15388(): pass

    label("Function_49_15388")


    def lambda_1538D():
        OP_95(0xFE, 8600, 0, 1320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1538D)
    WaitChrThread(0xC, 1)

    def lambda_153AB():
        OP_95(0xFE, 8600, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_153AB)
    WaitChrThread(0xC, 1)

    def lambda_153C9():
        OP_95(0xFE, 11600, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_153C9)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_153EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_153EC)
    WaitChrThread(0xC, 1)
    Return()

    # Function_49_15388 end

    def Function_50_153FD(): pass

    label("Function_50_153FD")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    Return()

    # Function_50_153FD end

    def Function_51_15416(): pass

    label("Function_51_15416")

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

    # Function_51_15416 end

    def Function_52_15488(): pass

    label("Function_52_15488")

    OP_64(0xFFFF)
    SetChrSubChip(0x21, 0x0)
    SetChrSubChip(0x15, 0x0)
    Return()

    # Function_52_15488 end

    SaveToFile()

Try(main)
