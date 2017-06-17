from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1510.bin",                # FileName
        "c1510",                    # MapName
        "c1510",                    # Location
        0x00AB,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 171, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1510",                  # 0
        "受付嬢リーリエ",         # 1
        "受付嬢ヴィオラ",         # 2
        "モレット主任",           # 3
        "タジク",                 # 4
        "ティボー巡査",           # 5
        "受付嬢ランフィ",         # 6
        "ロバーツ主任",           # 7
        "研究員ダビッド",         # 8
        "研究員クレイ",           # 9
        "マーガレット夫人",       # 10
        "ピエール副局長",         # 11
        "ノエル",                 # 12
        "ワジ",                   # 13
        "リーシャ",               # 14
        "ダドリー捜査官",         # 15
        "警官",                   # 16
        "市役所職員",             # 17
        "市役所職員",             # 18
        "市民",                   # 19
        "市民",                   # 20
        "観光客",                 # 21
        "市民",                   # 22
        "貿易商リゼロ",           # 23
        "ジージョ巡査",           # 24
        "グレイス",               # 25
        "レインズ",               # 26
        "ヨナ",                   # 27
        "ディーター市長",         # 28
    ))

    AddCharChip((
        "chr/ch30500.itc",                   # 00
        "chr/ch28200.itc",                   # 01
        "chr/ch27400.itc",                   # 02
        "chr/ch30000.itc",                   # 03
        "chr/ch27600.itc",                   # 04
        "chr/ch28000.itc",                   # 05
        "chr/ch28102.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch21102.itc",                   # 08
        "chr/ch32300.itc",                   # 09
        "chr/ch33002.itc",                   # 0A
        "chr/ch27802.itc",                   # 0B
        "chr/ch06002.itc",                   # 0C
        "chr/ch28100.itc",                   # 0D
        "chr/ch27900.itc",                   # 0E
        "chr/ch29300.itc",                   # 0F
        "chr/ch32800.itc",                   # 10
        "chr/ch44000.itc",                   # 11
        "chr/ch02900.itc",                   # 12
        "chr/ch03100.itc",                   # 13
        "chr/ch03200.itc",                   # 14
        "chr/ch00900.itc",                   # 15
        "chr/ch06400.itc",                   # 16
        "chr/ch29400.itc",                   # 17
        "chr/ch06102.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       1000,    21600,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(8000,    1000,    17959,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-8000,   1000,    17959,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-14920,  150,     2880,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(2819,    0,       -2410,   270,  261,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1500,    1000,    21600,   180,  385,  0x0, 0,   14,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-6769,   0,       2619,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-3819,   0,       4409,    180,  389,  0x0, 0,   23,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-3819,   0,       3019,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(7719,    0,       1889,    315,  389,  0x0, 0,   17,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(6719,    0,       2890,    135,  389,  0x0, 0,   22,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-289,    0,       6699,    45,   389,  0x0, 0,   18,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(-2609,   0,       -790,    180,  389,  0x0, 0,   19,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(-3460,   0,       3950,    270,  389,  0x0, 0,   20,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(1830,    0,       -1590,   180,  453,  0x0, 0,   21,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(3000,    0,       8380,    180,  385,  0x0, 0,   3,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(-16079,  0,       589,     270,  385,  0x0, 0,   4,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-17579,  0,       589,     90,   385,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4280,    0,       7480,    0,    389,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(5179,    150,     6250,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-3269,   0,       4619,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-14920,  150,     2880,    180,  389,  0x0, 0,   10,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5179,    150,     6250,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(78250,   0,       2650,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-14920,  150,     2880,    180,  389,  0x0, 0,   12,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-14920,  150,     1080,    0,    389,  0x0, 0,   13,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(5150,    0,       7150,    270,  389,  0x0, 0,   24,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 50,  74.94999694824219,     4.0,                   -1.0,                  20.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -24.983333587646484,   -1.3333333730697632,   0.20000000298023224,   1.0])

    DeclActor(0,       1000,    20000,   1500,    0,       2500,    21600,   0x007E, 0,  6,  0x0000)
    DeclActor(6750,    1000,    18000,   1700,    8000,    2500,    17960,   0x007E, 0,  8,  0x0000)
    DeclActor(-6750,   1000,    18000,   1700,    -8000,   2500,    17960,   0x007E, 0,  10, 0x0000)
    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  40, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  40, 0x0000)
    DeclActor(-12520,  0,       3040,    1200,    -12520,  0,       3040,    0x007C, 0,  5,  0x0000)
    DeclActor(1500,    1000,    20000,   1500,    1500,    2500,    21600,   0x007E, 0,  12, 0x0000)
    DeclActor(1420,    0,       8550,    1500,    1420,    2000,    8550,    0x007C, 0,  52, 0x0000)

    ChipFrameInfo(1648, 0)                                       # 0

    ScpFunction((
        "Function_0_670",          # 00, 0
        "Function_1_720",          # 01, 1
        "Function_2_7FE",          # 02, 2
        "Function_3_A87",          # 03, 3
        "Function_4_CE4",          # 04, 4
        "Function_5_E25",          # 05, 5
        "Function_6_EC4",          # 06, 6
        "Function_7_EC8",          # 07, 7
        "Function_8_1CD1",         # 08, 8
        "Function_9_1CD5",         # 09, 9
        "Function_10_28E2",        # 0A, 10
        "Function_11_28E6",        # 0B, 11
        "Function_12_357D",        # 0C, 12
        "Function_13_3581",        # 0D, 13
        "Function_14_3643",        # 0E, 14
        "Function_15_3A05",        # 0F, 15
        "Function_16_47DB",        # 10, 16
        "Function_17_488F",        # 11, 17
        "Function_18_49AA",        # 12, 18
        "Function_19_49FF",        # 13, 19
        "Function_20_4A46",        # 14, 20
        "Function_21_4AAE",        # 15, 21
        "Function_22_4B47",        # 16, 22
        "Function_23_5030",        # 17, 23
        "Function_24_50AE",        # 18, 24
        "Function_25_517F",        # 19, 25
        "Function_26_5219",        # 1A, 26
        "Function_27_5296",        # 1B, 27
        "Function_28_5515",        # 1C, 28
        "Function_29_55BF",        # 1D, 29
        "Function_30_5752",        # 1E, 30
        "Function_31_57BE",        # 1F, 31
        "Function_32_58DC",        # 20, 32
        "Function_33_6281",        # 21, 33
        "Function_34_665F",        # 22, 34
        "Function_35_6A58",        # 23, 35
        "Function_36_6AC0",        # 24, 36
        "Function_37_6CF8",        # 25, 37
        "Function_38_6FA7",        # 26, 38
        "Function_39_71D2",        # 27, 39
        "Function_40_73CC",        # 28, 40
        "Function_41_74C8",        # 29, 41
        "Function_42_74CF",        # 2A, 42
        "Function_43_8C7B",        # 2B, 43
        "Function_44_8CBF",        # 2C, 44
        "Function_45_909E",        # 2D, 45
        "Function_46_90D2",        # 2E, 46
        "Function_47_9123",        # 2F, 47
        "Function_48_974B",        # 30, 48
        "Function_49_9AA9",        # 31, 49
        "Function_50_A0CE",        # 32, 50
        "Function_51_A15F",        # 33, 51
        "Function_52_A26B",        # 34, 52
    ))


    def Function_0_670(): pass

    label("Function_0_670")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6A8"),
        (1, "loc_6B4"),
        (2, "loc_6C0"),
        (3, "loc_6CC"),
        (4, "loc_6D8"),
        (5, "loc_6E4"),
        (6, "loc_6F0"),
        (SWITCH_DEFAULT, "loc_6FC"),
    )


    label("loc_6A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_708")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_71F")

    Return()

    # Function_0_670 end

    def Function_1_720(): pass

    label("Function_1_720")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FD")
    OP_95(0xFE, 3000, 0, -850, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -4000, 0, -850, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -4000, 0, 8380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -500, 0, 8380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 3000, 0, 8380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_1_720")

    label("loc_7FD")

    Return()

    # Function_1_720 end

    def Function_2_7FE(): pass

    label("Function_2_7FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_828")
    ClearScenarioFlags(0x25, 1)
    Call(0, 41)

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_892")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0xB)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_865")
    SetChrFlags(0x12, 0x10)

    label("loc_865")

    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_888")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_888")

    ClearChrFlags(0xE, 0x80)
    Jump("loc_A2B")

    label("loc_892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8BC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x1F, 0x80)
    Call(0, 4)
    Jump("loc_A2B")

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8E3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x1F, 0x80)
    Jump("loc_A2B")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_90C")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0xB)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    Jump("loc_A2B")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_930")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0xA)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    Jump("loc_A2B")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_98E")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_989")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3810, 0, 8039, 135)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x22, 0x18)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)

    label("loc_989")

    Jump("loc_A2B")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9B2")
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x8)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    Jump("loc_A2B")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9D6")
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x8)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    Jump("loc_A2B")

    label("loc_9D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A04")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0xC)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_A2B")

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_A2B")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x1F, 0x80)

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A3F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 42)
    Jump("loc_A51")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A51")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x2, 2)
    Event(0, 49)

    label("loc_A51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A70")
    Event(0, 44)
    Jump("loc_A86")

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A86")
    SetMapFlags(0x10000000)
    Event(0, 47)

    label("loc_A86")

    Return()

    # Function_2_7FE end

    def Function_3_A87(): pass

    label("Function_3_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9B")
    Sound(130, 1, 40, 0)

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_AB5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 2)
    Jump("loc_AC7")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AC7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC7")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1D")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)

    label("loc_B1D")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B41")
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B54")
    OP_1B(0x0, 0x0, 0x33)

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B67")
    OP_1B(0x0, 0x0, 0x33)

    label("loc_B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBB")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_C05")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C34")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_C90")

    label("loc_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C73")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    Jump("loc_C90")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C90")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_C90")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CA6")
    OP_66(0x6, 0x1)
    Jump("loc_CCD")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CC0")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jump("loc_CCD")

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CCD")
    OP_66(0x6, 0x1)

    label("loc_CCD")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE3")
    OP_66(0x7, 0x1)

    label("loc_CE3")

    Return()

    # Function_3_A87 end

    def Function_4_CE4(): pass

    label("Function_4_CE4")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearScenarioFlags(0x2, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_D44")
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    SetChrPos(0x13, 3630, 0, 5580, 180)
    Jump("loc_D41")

    label("loc_D30")

    SetChrPos(0x13, 2410, 0, 6050, 180)

    label("loc_D41")

    SetScenarioFlags(0x2, 3)

    label("loc_D44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_D8D")
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")
    SetChrPos(0x14, 3630, 0, 5580, 180)
    Jump("loc_D8A")

    label("loc_D79")

    SetChrPos(0x14, 2410, 0, 6050, 180)

    label("loc_D8A")

    SetScenarioFlags(0x2, 3)

    label("loc_D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_DD6")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC2")
    SetChrPos(0x15, 3630, 0, 5580, 180)
    Jump("loc_DD3")

    label("loc_DC2")

    SetChrPos(0x15, 2410, 0, 6050, 180)

    label("loc_DD3")

    SetScenarioFlags(0x2, 3)

    label("loc_DD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_E24")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E10")
    SetChrPos(0x16, 3630, 0, 5580, 180)
    Jump("loc_E21")

    label("loc_E10")

    SetChrPos(0x16, 2410, 0, 6050, 180)

    label("loc_E21")

    SetScenarioFlags(0x2, 3)

    label("loc_E24")

    Return()

    # Function_4_CE4 end

    def Function_5_E25(): pass

    label("Function_5_E25")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『快走マッハ』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x370, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC0")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『クールカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x370, 1)

    label("loc_EC0")

    TalkEnd(0xFF)
    Return()

    # Function_5_E25 end

    def Function_6_EC4(): pass

    label("Function_6_EC4")

    Call(0, 7)
    Return()

    # Function_6_EC4 end

    def Function_7_EC8(): pass

    label("Function_7_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDA")
    Call(0, 48)
    Return()

    label("loc_EDA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD7")

    #C0003
    ChrTalk(
        0x8,
        (
            "当面、オルキスタワーは\x01",
            "マクダエル議長の主導によって\x01",
            "管理される事になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "まだまだ混乱も多いですが……\x01",
            "ここが市民のためのビルであることに\x01",
            "変わりはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "どうか、今後とも\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1050")

    label("loc_FD7")


    #C0006
    ChrTalk(
        0x8,
        (
            "オルキスタワーが\x01",
            "市民のためのビルであることに\x01",
            "変わりはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "どうか、今後とも\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1050")

    Jump("loc_1CCD")

    label("loc_1055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1063")
    Jump("loc_1CCD")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1071")
    Jump("loc_1CCD")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1161")

    #C0008
    ChrTalk(
        0x8,
        (
            "本日、市民会館では街の復興を\x01",
            "支援するチャリティイベントを\x01",
            "開催しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "みんなが笑顔になれる、\x01",
            "そんな企画を多数\x01",
            "用意しておりますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "もし時間に余裕がございましたら\x01",
            "皆さんも是非ご参加ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E9")

    label("loc_1161")


    #C0011
    ChrTalk(
        0x8,
        (
            "それにしても……\x01",
            "ＩＢＣの復旧の早さには\x01",
            "本当に驚かされました。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "導力ネットという技術の\x01",
            "素晴らしさにも\x01",
            "改めて気付かされますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E9")

    Jump("loc_1CCD")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_140D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1350")

    #C0013
    ChrTalk(
        0x8,
        (
            "当然のことですが……\x01",
            "市民の皆さんの間にもかなり\x01",
            "動揺が広がっているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "事件の質問などに対しては、\x01",
            "どうしても曖昧なことしか\x01",
            "答えられないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "警備隊の方々は勿論、市長も議長も\x01",
            "全力を尽くして頑張ってくれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "とにかく今は皆さんを信じて、\x01",
            "私たち職員も自分たちに\x01",
            "出来ることを尽くすだけです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1408")

    label("loc_1350")


    #C0017
    ChrTalk(
        0x8,
        (
            "事態の収束に向けては、\x01",
            "警備隊の方々は勿論、市長も議長も\x01",
            "全力を尽くして頑張ってくれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "とにかく今は皆さんを信じて、\x01",
            "私たち職員も自分たちに\x01",
            "出来ることを尽くすだけです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1408")

    Jump("loc_1CCD")

    label("loc_140D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_157F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D3")

    #C0019
    ChrTalk(
        0x8,
        (
            "本日は、市民会館にて\x01",
            "『国家独立の是非』がテーマの\x01",
            "市民フォーラムが開催中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "プログラムによっては\x01",
            "若干の空席もあるようなので、\x01",
            "興味のある方はぜひご参加ください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157A")

    label("loc_14D3")


    #C0021
    ChrTalk(
        0x8,
        (
            "お渡ししたカードを\x01",
            "エレベーター内のパネルにかざすと\x01",
            "最上階の４０Ｆに直通で上がれます。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "１ヶ月のみ有効の使い捨てですので\x01",
            "利用後はご自由に処分されてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157A")

    Jump("loc_1CCD")

    label("loc_157F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170A")

    #C0023
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "列車事故に関するお問い合わせでしたら\x01",
            "こちらでご案内させて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "現在、西クロスベル街道で発生した\x01",
            "列車事故の影響で大陸横断鉄道は\x01",
            "一時的に運行を見合わせています。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "なお、原因は只今調査中でして、\x01",
            "復旧の見込みにつきましても\x01",
            "現時点では付いていない状態です。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "急ぎ帝国・共和国方面に\x01",
            "向かわれる方はバス・または空港を\x01",
            "ご利用ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179B")

    label("loc_170A")


    #C0027
    ChrTalk(
        0x8,
        (
            "急ぎ帝国・共和国方面に\x01",
            "向かわれる方はバス・または空港を\x01",
            "ご利用ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "ご必要でしたら、こちらの方で\x01",
            "チケットの手配もさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179B")

    Jump("loc_1CCD")

    label("loc_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1918")

    #C0029
    ChrTalk(
        0x8,
        (
            "現在、クロスベル市では諸外国との\x01",
            "文化交流を推進するための\x01",
            "様々な企画を発案・検討しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "クロスベルの観光ＰＲコーナーや\x01",
            "諸外国の文化・歴史を学ぶコーナー、\x01",
            "各国の名産品を集めた店舗など……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "市民の皆様に、より有意義な\x01",
            "サービスをご提供するべく\x01",
            "職員一同、日々奮闘しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "オルキスタワーの\x01",
            "今後の発展にどうぞご期待ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19B3")

    label("loc_1918")


    #C0033
    ChrTalk(
        0x8,
        (
            "現在、クロスベル市では諸外国との\x01",
            "文化交流を推進するための\x01",
            "様々な企画を発案・検討しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "オルキスタワーの\x01",
            "今後の発展にどうぞご期待ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B3")

    Jump("loc_1CCD")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAF")

    #C0035
    ChrTalk(
        0x8,
        "ようこそ、オルキスタワーへ。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "こちらの総合受付では、\x01",
            "お客様のご相談内容に合わせて\x01",
            "様々なご案内をしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "観光案内から、医療・福祉などの\x01",
            "市民生活に関するご相談まで、\x01",
            "どんなことでもお問い合わせ下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B6B")

    label("loc_1AAF")


    #C0038
    ChrTalk(
        0x8,
        (
            "こちらの総合受付では、\x01",
            "お客様のご相談内容に合わせて\x01",
            "様々なご案内を致しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "観光案内から、医療・福祉などの\x01",
            "市民生活に関するご相談まで、\x01",
            "どんなことでもお問い合わせ下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6B")

    Jump("loc_1CCD")

    label("loc_1B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_1CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C50")

    #C0040
    ChrTalk(
        0x8,
        (
            "皆さん、お疲れ様です。\x01",
            "こちらはオルキスタワーの\x01",
            "総合受付です。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "なお本日は職員一同、\x01",
            "警備対策室の指示に従って\x01",
            "各種業務に当たる予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "何かあった際は、\x01",
            "どうか宜しくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CCD")

    label("loc_1C50")


    #C0043
    ChrTalk(
        0x8,
        (
            "本日は職員一同、\x01",
            "警備対策室の指示に従って\x01",
            "各種業務に当たる予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "何かあった際は、\x01",
            "どうか宜しくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCD")

    TalkEnd(0x8)
    Return()

    # Function_7_EC8 end

    def Function_8_1CD1(): pass

    label("Function_8_1CD1")

    Call(0, 9)
    Return()

    # Function_8_1CD1 end

    def Function_9_1CD5(): pass

    label("Function_9_1CD5")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC5")

    #C0045
    ChrTalk(
        0x9,
        (
            "市内に現れた化物は、\x01",
            "その全てが姿を消したようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "私もタワーに閉じ込められて\x01",
            "本当に恐ろしい思いをしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "ひとまずは大きな被害も\x01",
            "なかったそうですが、二度と\x01",
            "こんな思いはしたくありませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E5C")

    label("loc_1DC5")


    #C0048
    ChrTalk(
        0x9,
        (
            "私もタワーに閉じ込められて\x01",
            "本当に恐ろしい思いをしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "ひとまずは大きな被害も\x01",
            "なかったそうですが、二度と\x01",
            "こんな思いはしたくありませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5C")

    Jump("loc_28DE")

    label("loc_1E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1E6F")
    Jump("loc_28DE")

    label("loc_1E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E7D")
    Jump("loc_28DE")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F90")

    #C0050
    ChrTalk(
        0x9,
        (
            "襲撃に遭った時、地下へと\x01",
            "避難している際に広場での\x01",
            "衝突が目に入ったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "武装集団が迫り来る光景は、\x01",
            "とにかく恐ろしいとしか\x01",
            "言い様がありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "幸いにもこのビルは\x01",
            "何とか無事でしたが……\x01",
            "本当に生きた心地がしませんでした。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2034")

    label("loc_1F90")


    #C0053
    ChrTalk(
        0x9,
        (
            "武装集団が迫り来る光景は、\x01",
            "とにかく恐ろしいとしか\x01",
            "言い様がありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "幸いにもこのビルは\x01",
            "何とか無事でしたが……\x01",
            "本当に生きた心地がしませんでした。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2034")

    Jump("loc_28DE")

    label("loc_2039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_21EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2142")

    #C0055
    ChrTalk(
        0x9,
        (
            "ウルスラ病院の方は\x01",
            "昨夜からずっと騒然とした\x01",
            "状況が続いているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "患者の数が膨大なため、\x01",
            "そもそも人手と各種物資が\x01",
            "足りていないという話ですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "現場で奮戦なさっている\x01",
            "皆さんの苦労を思うと、\x01",
            "ただただ頭が下がります。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E6")

    label("loc_2142")


    #C0058
    ChrTalk(
        0x9,
        (
            "現在、市の方では総力を挙げて\x01",
            "病院に対しても様々な支援措置を\x01",
            "取っているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "現場で奮戦なさっている\x01",
            "皆さんの苦労を思うと、\x01",
            "ただただ頭が下がります。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E6")

    Jump("loc_28DE")

    label("loc_21EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CC")

    #C0060
    ChrTalk(
        0x9,
        (
            "列車事故の影響で自治州への\x01",
            "滞在を余儀なくされていた方々も\x01",
            "今朝には殆ど出発されたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "補償の問題などは今後の話ですが……\x01",
            "とりあえずは事故の復旧が\x01",
            "長期化しなくて本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_235F")

    label("loc_22CC")


    #C0062
    ChrTalk(
        0x9,
        (
            "列車事故の原因によっては\x01",
            "今後補償の問題について\x01",
            "考えなければいけませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "とりあえずは事故の復旧が\x01",
            "長期化しなくて本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235F")

    Jump("loc_28DE")

    label("loc_2364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2415")

    #C0064
    ChrTalk(
        0x9,
        (
            "先ほど連絡を受けたのですが、\x01",
            "怪我をされた乗客の皆さんの搬送は\x01",
            "無事に済んだとのことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "とりあえずは一安心ですが……\x01",
            "あとは事故現場の様子が心配ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DE")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2559")

    #C0066
    ChrTalk(
        0x9,
        (
            "皆さんは、\x01",
            "オルキスタワーの名前の意味を\x01",
            "ご存知でいらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "オルキスは“蘭”……\x01",
            "一つの茎に一つの花を咲かせる\x01",
            "美しい花のことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "つまり例えるなら、\x01",
            "このビルは空に向かって真っ直ぐに\x01",
            "伸びる一輪の花というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "ふふ、そう考えると\x01",
            "ピッタリの名前だと思いませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25FF")

    label("loc_2559")


    #C0070
    ChrTalk(
        0x9,
        (
            "オルキスは“蘭”……\x01",
            "一つの茎に一つの花を咲かせる\x01",
            "美しい花のことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "つまり例えるなら、\x01",
            "このビルは空に向かって真っ直ぐに\x01",
            "伸びる一輪の花というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FF")

    Jump("loc_28DE")

    label("loc_2604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_274C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B1")

    #C0072
    ChrTalk(
        0x9,
        (
            "いらっしゃいませ、\x01",
            "こちらは各種行政手続きの\x01",
            "受付窓口となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "公共料金のお支払いや\x01",
            "住所の変更届けは\x01",
            "こちらをご利用下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2747")

    label("loc_26B1")


    #C0074
    ChrTalk(
        0x9,
        (
            "なお、当窓口で扱っている\x01",
            "手続きの大半は市民会館でも\x01",
            "承っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "こちらに出向かれるのが\x01",
            "大変な方は、是非そちらの方も\x01",
            "ご利用下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2747")

    Jump("loc_28DE")

    label("loc_274C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_28DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283A")

    #C0076
    ChrTalk(
        0x9,
        (
            "あと１時間で、\x01",
            "いよいよ本会議が始まりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "会議の間、私はここで\x01",
            "主に市職員の各種連絡を\x01",
            "取り次ぐ予定なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "何と言いましょうか、\x01",
            "これだけの行事に関わると思うと\x01",
            "何だか緊張してしまいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28DE")

    label("loc_283A")


    #C0079
    ChrTalk(
        0x9,
        (
            "あと１時間で本会議……\x01",
            "それに、しばらくしたら\x01",
            "首脳の皆さんがこちらに……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "ふう、私は別に大した仕事を\x01",
            "するわけではないのですが、\x01",
            "何だか緊張してしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DE")

    TalkEnd(0x9)
    Return()

    # Function_9_1CD5 end

    def Function_10_28E2(): pass

    label("Function_10_28E2")

    Call(0, 11)
    Return()

    # Function_10_28E2 end

    def Function_11_28E6(): pass

    label("Function_11_28E6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")

    #C0081
    ChrTalk(
        0xA,
        (
            "オルキスタワー内に拘束されていた\x01",
            "職員や国防軍は、一通り解放されたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "ほとんどは荒れた職場の\x01",
            "事後処理に当たっている状態でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "こんな時だからこそ、\x01",
            "市民のために\x01",
            "しっかりと働いていかねばね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A7C")

    label("loc_29D0")


    #C0084
    ChrTalk(
        0xA,
        (
            "オルキスタワー内に拘束されていた\x01",
            "職員や国防軍は、ほとんどが職場の\x01",
            "事後処理に当たっている状態でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "こんな時だからこそ、\x01",
            "市民のために\x01",
            "しっかりと働いていかねばね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7C")

    Jump("loc_3579")

    label("loc_2A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A8F")
    Jump("loc_3579")

    label("loc_2A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A9D")
    Jump("loc_3579")

    label("loc_2A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB5")

    #C0086
    ChrTalk(
        0xA,
        (
            "アリオス・マクレイン……\x01",
            "彼は本当にこのクロスベルの英雄だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        (
            "私は彼が武装集団に切り込む姿を\x01",
            "この目で見たんだが、素晴らしいとしか\x01",
            "言い様のない活躍ぶりだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "突飛な考えだけど、\x01",
            "彼がいてくれたら２大国も怖くない……\x01",
            "本当にそう思えたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C4A")

    label("loc_2BB5")


    #C0089
    ChrTalk(
        0xA,
        (
            "アリオス・マクレイン……\x01",
            "彼は本当にこのクロスベルの英雄だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "突飛な考えだけど、\x01",
            "彼がいてくれたら２大国も怖くない……\x01",
            "本当にそう思えたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C4A")

    Jump("loc_3579")

    label("loc_2C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D91")

    #C0091
    ChrTalk(
        0xA,
        (
            "聞いている話だと、どうやら\x01",
            "警備隊の状況は芳しくないようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "これ以上被害が拡大するようなら\x01",
            "警官隊の投入も考えられるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "かといって都市の防衛を\x01",
            "疎かにするわけにはいかないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "今各所で手を尽くしているようだけど、\x01",
            "対話と交渉による解決を\x01",
            "何としてでも実現させないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E49")

    label("loc_2D91")


    #C0095
    ChrTalk(
        0xA,
        (
            "今各所で手を尽くしているようだけど、\x01",
            "対話と交渉による解決を\x01",
            "何としてでも実現させないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "直接貢献することは難しいけど、\x01",
            "私たち総務一課の方も\x01",
            "各種業務に注力させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E49")

    Jump("loc_3579")

    label("loc_2E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_300A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F62")

    #C0097
    ChrTalk(
        0xA,
        (
            "ふう、しかし鉄道の復旧が\x01",
            "何とか昨日の内に終わってくれて\x01",
            "本当に安心したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "もし列車が停まったままだったら、\x01",
            "クロスベルに対する各種補償請求は\x01",
            "青天井に増大していただろうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "夜通しで作業してくれた\x01",
            "警備隊には足を向けて寝られないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3005")

    label("loc_2F62")


    #C0100
    ChrTalk(
        0xA,
        (
            "もし列車が停まったままだったら、\x01",
            "クロスベルに対する各種補償請求は\x01",
            "青天井に増大していただろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "夜通しで作業してくれた\x01",
            "警備隊には足を向けて寝られないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3005")

    Jump("loc_3579")

    label("loc_300A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3188")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F2")

    #C0102
    ChrTalk(
        0xA,
        (
            "列車事故発生の連絡は\x01",
            "当然こちらの方でも\x01",
            "速やかに受け取ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "各方面からの問い合わせも\x01",
            "早速、届いている状況でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "今は導力鉄道に代わる\x01",
            "移動・輸送手段の案内や手配を\x01",
            "随時行っている所なんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3183")

    label("loc_30F2")


    #C0105
    ChrTalk(
        0xA,
        (
            "それにしても列車事故なんて\x01",
            "珍しいこともあるものだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "クロスベルの鉄道は\x01",
            "一直線で見通しも良いから\x01",
            "事故なんて滅多に起こらないんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3183")

    Jump("loc_3579")

    label("loc_3188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_324A")

    #C0107
    ChrTalk(
        0xA,
        (
            "市庁の開放日は、見物目当ての\x01",
            "市民たちでこのエントランスが\x01",
            "ごった返しになってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "ふふ、初めてビルに入った\x01",
            "人たちの度肝を抜かれたような表情は\x01",
            "見ていて気持ちが良かったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3579")

    label("loc_324A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3410")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338A")

    #C0109
    ChrTalk(
        0xA,
        (
            "おや、君たちは通商会議で\x01",
            "警備を担当してくれた\x01",
            "特務支援課じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "ふむ、いい機会だから\x01",
            "説明しておくが、こちらは\x01",
            "行政の窓口になっていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "各種資料の公開請求や、\x01",
            "政策への問い合わせなどは、\x01",
            "ここで受け付けているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "まあ、もし何かあったら\x01",
            "いつでも聞いてくれるといいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_340B")

    label("loc_338A")


    #C0113
    ChrTalk(
        0xA,
        (
            "こちらは行政に関する\x01",
            "対応を行う窓口なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "各種資料の公開請求や、\x01",
            "政策への問い合わせなどは、\x01",
            "ここで受け付けているよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340B")

    Jump("loc_3579")

    label("loc_3410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_3579")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F9")

    #C0115
    ChrTalk(
        0xA,
        (
            "オルキスタワーの管理・運営は\x01",
            "私たち総務一課の重要な業務でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "今日の本会議に使われる\x01",
            "会議場や各種控え室の準備は\x01",
            "我々の仕事なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "今はようやく落ち着いたが……\x01",
            "ついさっきまで大忙しだったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3579")

    label("loc_34F9")


    #C0118
    ChrTalk(
        0xA,
        (
            "ふう、とにかく色んなものが\x01",
            "会議に間に合って良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "最後まで気は抜けないが、あとは\x01",
            "会議が始まるのを待つだけかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3579")

    TalkEnd(0xA)
    Return()

    # Function_11_28E6 end

    def Function_12_357D(): pass

    label("Function_12_357D")

    Call(0, 13)
    Return()

    # Function_12_357D end

    def Function_13_3581(): pass

    label("Function_13_3581")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_358E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "換金をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35EA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_35EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360A")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_363A")

    label("loc_360A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_361E")
    Jump("loc_363A")

    label("loc_361E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_363A")

    Jump("loc_358E")

    label("loc_363F")

    TalkEnd(0xD)
    Return()

    # Function_13_3581 end

    def Function_14_3643(): pass

    label("Function_14_3643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3733")

    #C0120
    ChrTalk(
        0xD,
        (
            "ＩＢＣ業務も停止状態……\x01",
            "職員たちも半数は\x01",
            "自宅待機となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "長年、銀行に勤めていた身としては\x01",
            "ディーター様の拘束は\x01",
            "あまりにもショックですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "私たちも乗り越えて\x01",
            "いかなければいけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_37BA")

    label("loc_3733")


    #C0123
    ChrTalk(
        0xD,
        (
            "ＩＢＣ業務は停止状態ですが、\x01",
            "セピスの換金サービスだけは\x01",
            "引き続き行っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "ご利用の際はお気軽に\x01",
            "声をおかけくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BA")

    Jump("loc_3A04")

    label("loc_37BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394B")

    #C0125
    ChrTalk(
        0x102,
        (
            "#00100Fお疲れ様です、ランフィさん。\x02\x03",

            "どうやら窓口の移設の方も\x01",
            "大分、落ち着いたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xD,
        "これはこれは、エリィ様。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "はい、これも一重に\x01",
            "マリアベル総裁代行の手腕と\x01",
            "優秀な技術部スタッフのおかげです。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "職員の半分以上は、\x01",
            "もうこちらのビルで\x01",
            "通常業務を再開しておりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xD,
        (
            "どうぞ、お気軽に\x01",
            "何でもお申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        "#00102Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3A04")

    label("loc_394B")


    #C0131
    ChrTalk(
        0xD,
        (
            "ＩＢＣは当面、このオルキスタワーにて\x01",
            "営業を行って参ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xD,
        (
            "セピスの換金サービスについても\x01",
            "今まで通りご利用いただけますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "どうぞ、お気軽に\x01",
            "何でもお申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A04")

    Return()

    # Function_14_3643 end

    def Function_15_3A05(): pass

    label("Function_15_3A05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD0")

    #C0134
    ChrTalk(
        0xFE,
        (
            "離れ離れになってた家族や友人が\x01",
            "次々に再会しているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "大変な事態になってしまったけど……\x01",
            "やっぱりこういう時は、大事な人たちと\x01",
            "一緒にいなくちゃいけないよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B4C")

    label("loc_3AD0")


    #C0136
    ChrTalk(
        0xFE,
        (
            "そういえばさっき、壊れてた\x01",
            "導力車を外に運び出したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "大事に扱ってきたみたいだし、\x01",
            "ちゃんと労ってやってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B4C")

    Jump("loc_47D7")

    label("loc_3B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B5F")
    Jump("loc_47D7")

    label("loc_3B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B6D")
    Jump("loc_47D7")

    label("loc_3B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBB")

    #C0138
    ChrTalk(
        0xFE,
        (
            "オルキスタワーは、\x01",
            "アリオスさんの活躍のおかげで\x01",
            "何とか無事だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "ＩＢＣビルは……文字通り\x01",
            "跡形もなく消えてしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "民間人の被害はほとんど\x01",
            "なかったって話だけど\x01",
            "アルカンシェルまで巻き込んで……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "見せしめか何かは知らないが、\x01",
            "こんなことは何があっても\x01",
            "許されていいはずがないよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D65")

    label("loc_3CBB")


    #C0142
    ChrTalk(
        0xFE,
        (
            "民間人の被害はほとんど\x01",
            "なかったって話だけど\x01",
            "アルカンシェルまで巻き込んで……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "見せしめか何かは知らないが、\x01",
            "こんなことは何があっても\x01",
            "許されていいはずがないよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D65")

    Jump("loc_47D7")

    label("loc_3D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E22")

    #C0144
    ChrTalk(
        0xFE,
        (
            "市長も議長も、昨夜からずっと\x01",
            "占拠事件の対応で\x01",
            "お忙しくされているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "今この状況で僕たちに\x01",
            "出来ることは……とにかく有事に備えて\x01",
            "気を抜かないことだけか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D7")

    label("loc_3E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F46")

    #C0146
    ChrTalk(
        0xFE,
        (
            "昨日の列車事故を引き起こした\x01",
            "化物は別物だという話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "近頃よく出現しているらしい\x01",
            "幻獣の存在はやはり気になるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "それらの近くでは、\x01",
            "よく分からない蒼い花ってのも\x01",
            "確認されているらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "これは何か……\x01",
            "さらなる変事の前触れなんだろうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FE0")

    label("loc_3F46")


    #C0150
    ChrTalk(
        0xFE,
        (
            "詳細が分からない以上、\x01",
            "幻獣が市内に現れることだって\x01",
            "ないとは言い切れないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "何とも不気味だけど……\x01",
            "ともかく警戒は怠らないように\x01",
            "しないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE0")

    Jump("loc_47D7")

    label("loc_3FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4058")

    #C0152
    ChrTalk(
        0xFE,
        "導力列車の脱線事故、か……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "今原因を調査してるらしいけど、\x01",
            "まさかテロじゃないだろうな……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D7")

    label("loc_4058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C3")

    #C0154
    ChrTalk(
        0xFE,
        (
            "僕は警察の人間だけど、\x01",
            "ここでは市の職員と同等の\x01",
            "待遇が保障されていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "というわけで、ビル内にある\x01",
            "職員専用のカフェや食堂を\x01",
            "利用することが出来るんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "場所はビルの中程だけど、\x01",
            "それでもＩＢＣの屋上よりも\x01",
            "高い位置にあるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "とにかく景色が最高なんだけど、\x01",
            "何だか市民の皆さんに対して\x01",
            "申し訳ない気持ちになるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_426D")

    label("loc_41C3")


    #C0158
    ChrTalk(
        0xFE,
        (
            "ただ、カフェの方はなるべく\x01",
            "早めに市民に開放しようという\x01",
            "話も挙がっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "いつになるかは分からないけど、\x01",
            "そうなった時は必ず人気の\x01",
            "スポットになると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426D")

    Jump("loc_47D7")

    label("loc_4272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_43C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4347")

    #C0160
    ChrTalk(
        0xFE,
        (
            "おや、特務支援課じゃないか。\x01",
            "オルキスタワーへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "何か用事があるなら\x01",
            "正面受付に聞いてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "外部の人間は\x01",
            "まずあそこで話を通さないと、\x01",
            "ここでは何も出来ないからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43C4")

    label("loc_4347")


    #C0163
    ChrTalk(
        0xFE,
        (
            "何か用事があるなら\x01",
            "正面受付に聞いてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "外部の人間は\x01",
            "まずあそこで話を通さないと、\x01",
            "ここでは何も出来ないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C4")

    Jump("loc_47D7")

    label("loc_43C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_47D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4769")

    #C0165
    ChrTalk(
        0xFE,
        (
            "ディーター市長から直接\x01",
            "会場を案内してもらえるなんて、\x01",
            "流石は特務支援課だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "市長のお気に入りって噂は\x01",
            "やっぱり本当だったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#00005Fえっと、あれは何ていうか……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "ああ、決してやっかみで\x01",
            "言ってるわけじゃないから\x01",
            "気を悪くしないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "というのも、僕は個人的に\x01",
            "君たちのことを応援していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "持ち場は違えど、\x01",
            "こうして一緒に仕事が出来て\x01",
            "嬉しく思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        "#00105Fあ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#00202F……何というか、\x01",
            "半年前とはえらい違いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#00302Fそういや最初は『ニセ遊撃士』だの\x01",
            "『猿回しのサル』だの、\x01",
            "色々言われてたって話だからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x109,
        "#10105Fそ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、身内からも随分\x01",
            "こき下ろされていたんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "はは、確かに前はそんなことを\x01",
            "言っている人もいたっけな。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "けどまあ、今は誰も\x01",
            "そんな風に言う人はいないから\x01",
            "安心していいと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "ま、それはともかく\x01",
            "今日はお互いに頑張って行こうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#00000Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 0)
    Jump("loc_47D7")

    label("loc_4769")


    #C0180
    ChrTalk(
        0xFE,
        (
            "持ち場は違えど、\x01",
            "君たちと一緒に仕事が出来て\x01",
            "嬉しく思っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "今日はお互いに頑張って行こうな。\x02",
    )

    CloseMessageWindow()

    label("loc_47D7")

    TalkEnd(0xFE)
    Return()

    # Function_15_3A05 end

    def Function_16_47DB(): pass

    label("Function_16_47DB")

    TalkBegin(0xFE)

    #C0182
    ChrTalk(
        0xFE,
        (
            "ふー、雨が降ってると\x01",
            "息抜きに外の空気も吸えねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "まあ、だがこのエントランスは\x01",
            "なかなかいい場所だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "何といっても、この天井の高さが\x01",
            "開放的でサイコーだぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_47DB end

    def Function_17_488F(): pass

    label("Function_17_488F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493C")

    #C0185
    ChrTalk(
        0xFE,
        (
            "１２:００――\x01",
            "特に異常は見当たらず、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "テロリストを思わせる影は\x01",
            "まだ現状感じないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "ヤツら一体どこから\x01",
            "進入するつもりなんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49A6")

    label("loc_493C")


    #C0188
    ChrTalk(
        0xFE,
        (
            "テロリストを思わせる影は\x01",
            "まだ現状感じないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "ヤツら一体どこから\x01",
            "進入するつもりなんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A6")

    TalkEnd(0xFE)
    Return()

    # Function_17_488F end

    def Function_18_49AA(): pass

    label("Function_18_49AA")

    TalkBegin(0xFE)

    #C0190
    ChrTalk(
        0xFE,
        (
            "えっとじゃあ、\x01",
            "ＶＩＰルームへはその時間から\x01",
            "立ち入り禁止ってことですね？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_49AA end

    def Function_19_49FF(): pass

    label("Function_19_49FF")

    TalkBegin(0xFE)

    #C0191
    ChrTalk(
        0xFE,
        (
            "ああ、そうなるな。\x01",
            "当然だが準備は早め早めで\x01",
            "回していくぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_49FF end

    def Function_20_4A46(): pass

    label("Function_20_4A46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A5B")
    Call(0, 29)
    Jump("loc_4AAA")

    label("loc_4A5B")


    #C0192
    ChrTalk(
        0xFE,
        (
            "き、君たち……\x01",
            "ええい、あっちに行きたまえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "今、私は忙しいのだよっ！\x02",
    )

    CloseMessageWindow()

    label("loc_4AAA")

    TalkEnd(0xFE)
    Return()

    # Function_20_4A46 end

    def Function_21_4AAE(): pass

    label("Function_21_4AAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC3")
    Call(0, 31)
    Jump("loc_4B43")

    label("loc_4AC3")


    #C0194
    ChrTalk(
        0xFE,
        (
            "ロバーツ主任も来てくれてるし、\x01",
            "導力ネット関係のトラブルは\x01",
            "なんだって対処できるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "へへ、一丁やってやるとすっか。\x02",
    )

    CloseMessageWindow()

    label("loc_4B43")

    TalkEnd(0xFE)
    Return()

    # Function_21_4AAE end

    def Function_22_4B47(): pass

    label("Function_22_4B47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C25")

    #C0196
    ChrTalk(
        0xFE,
        (
            "さっき、小さな女の子が\x01",
            "屋上に向かうエレベーターに\x01",
            "乗っていったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "あの子は確か、\x01",
            "国防長官の娘さんだったはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "やはり、湿地帯に現れた\x01",
            "《大樹》が気になるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4CB6")

    label("loc_4C25")


    #C0199
    ChrTalk(
        0xFE,
        (
            "さっき、国防長官の娘さんが\x01",
            "屋上に向かうエレベーターに\x01",
            "乗っていったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "やはり、湿地帯に現れた\x01",
            "《大樹》が気になるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB6")

    Jump("loc_502C")

    label("loc_4CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4CC9")
    Jump("loc_502C")

    label("loc_4CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CD7")
    Jump("loc_502C")

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D40")

    #C0201
    ChrTalk(
        0xFE,
        (
            "『赤い星座』の背後には\x01",
            "当然、帝国政府が……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        "ふむ、到底許せる話ではありませんね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D89")

    #C0203
    ChrTalk(
        0xFE,
        (
            "『赤い星座』……やはり\x01",
            "尋常じゃない連中のようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_END)), "loc_4DF4")

    #C0204
    ChrTalk(
        0xFE,
        "皆さん、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "上階に行かれる際は入口手前の\x01",
            "エレベーターをお使いください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E67")

    #C0206
    ChrTalk(
        0xFE,
        "ふむ、今日の天気は雨ですか。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "もっとも、導力ネットによると\x01",
            "午後からは晴れるそうですけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4F04")

    #C0208
    ChrTalk(
        0xFE,
        (
            "ふむ、クロスベルで\x01",
            "列車事故とは珍しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "脱線ということは、負荷が\x01",
            "それだけかかったということ……\x01",
            "一体何があったんでしょうかね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F8A")

    #C0210
    ChrTalk(
        0xFE,
        (
            "オルキスタワーは何といっても\x01",
            "この広々とした空間が最高ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "いやはや、本当に\x01",
            "贅沢な造りの建物だと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5023")

    #C0212
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの\x01",
            "エレベーターの速度は現時点で\x01",
            "大陸一との触れ込みです。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "揺れがほとんどないせいか、\x01",
            "あまり実感はできませんけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_5023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_502C")

    label("loc_502C")

    TalkEnd(0xFE)
    Return()

    # Function_22_4B47 end

    def Function_23_5030(): pass

    label("Function_23_5030")

    TalkBegin(0xFE)

    #C0214
    ChrTalk(
        0xFE,
        (
            "はぁ、すごいな……\x01",
            "これがオルキスタワーの\x01",
            "エントランスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "まるでＳＦ小説に出てくる\x01",
            "未来人になった気分だね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_5030 end

    def Function_24_50AE(): pass

    label("Function_24_50AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_511B")

    #C0216
    ChrTalk(
        0xFE,
        (
            "職員の方に聞いたけど、\x01",
            "何でも列車が\x01",
            "脱線したんだってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "一体何が原因なのかしら？\x02",
    )

    CloseMessageWindow()
    Jump("loc_517B")

    label("loc_511B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_517B")

    #C0218
    ChrTalk(
        0xFE,
        (
            "おばさん初めて来たんだけど\x01",
            "本当にすごい空間ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "何だか場違いな感じがするわ。\x02",
    )

    CloseMessageWindow()

    label("loc_517B")

    TalkEnd(0xFE)
    Return()

    # Function_24_50AE end

    def Function_25_517F(): pass

    label("Function_25_517F")

    TalkBegin(0xFE)

    #C0220
    ChrTalk(
        0xFE,
        (
            "こんなにカッコよくて\x01",
            "ハイテクなビルが市役所だなんて\x01",
            "まったくシビれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "独立提唱の騒ぎはともかく、\x01",
            "いつかクロスベルに移住したいかもね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_517F end

    def Function_26_5219(): pass

    label("Function_26_5219")

    TalkBegin(0xFE)

    #C0222
    ChrTalk(
        0xFE,
        (
            "ふむ、マインツの事件を受けて\x01",
            "市庁も少々騒がしいみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "早い所、用事を済ませて\x01",
            "さっさと帰るとするか……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_5219 end

    def Function_27_5296(): pass

    label("Function_27_5296")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5396")

    #C0224
    ChrTalk(
        0xFE,
        (
            "ＩＢＣは、総裁だった大統領も\x01",
            "総裁代行だった令嬢も\x01",
            "いなくなってしまったそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "今後の株価にも大いに影響しそうだが……\x01",
            "大陸トップの資本力は揺るぐまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "次の総裁が決まるまで、\x01",
            "私もしばらく様子を見るとするかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5422")

    label("loc_5396")


    #C0227
    ChrTalk(
        0xFE,
        (
            "今後の株価にも大いに影響しそうだが……\x01",
            "大陸トップの資本力は揺るぐまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "次の総裁が決まるまで、\x01",
            "私もしばらく様子を見るとするかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5422")

    Jump("loc_5511")

    label("loc_5427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5435")
    Jump("loc_5511")

    label("loc_5435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5511")

    #C0229
    ChrTalk(
        0xFE,
        (
            "まさか、前々から\x01",
            "オルキスタワーに顧客情報を\x01",
            "バックアップしていたなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "流石はＩＢＣ……\x01",
            "大した危機管理能力だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "大陸経済を長年に渡って\x01",
            "支えてきた実績は、とことん\x01",
            "伊達じゃなかったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5511")

    TalkEnd(0xFE)
    Return()

    # Function_27_5296 end

    def Function_28_5515(): pass

    label("Function_28_5515")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552A")
    Call(0, 29)
    Jump("loc_55BB")

    label("loc_552A")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0232
    ChrTalk(
        0x11,
        (
            "……心配をかけたバツとして、\x01",
            "来月のお小遣いは５０％カットね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x12)

    #C0233
    ChrTalk(
        0x12,
        "そっ、それだけはご勘弁をっ……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)

    label("loc_55BB")

    TalkEnd(0xFE)
    Return()

    # Function_28_5515 end

    def Function_29_55BF(): pass

    label("Function_29_55BF")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0234
    ChrTalk(
        0x11,
        (
            "まったく、あなたって人は\x01",
            "余計な心配をかけてくれたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x12,
        "し、しかしだね、マーガレット。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x12,
        (
            "やはり警察の副局長として、\x01",
            "立ち上がるべき時というものが\x01",
            "あってだね……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x11,
        (
            "そういうのは、普段から\x01",
            "やっておくべきものでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x11,
        (
            "突然似合わない事をするから、\x01",
            "こんな事に巻き込まれるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x12,
        "……ス、スミマセン。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5741")

    #C0240
    ChrTalk(
        0x101,
        "#00012F（あ、相変わらず手厳しいなあ……）\x02",
    )

    CloseMessageWindow()

    label("loc_5741")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_29_55BF end

    def Function_30_5752(): pass

    label("Function_30_5752")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5767")
    Call(0, 31)
    Jump("loc_57BA")

    label("loc_5767")


    #C0241
    ChrTalk(
        0xFE,
        (
            "やっぱり相棒と仕事するのは\x01",
            "気分がいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "さっそくとりかかるとしようか。\x02",
    )

    CloseMessageWindow()

    label("loc_57BA")

    TalkEnd(0xFE)
    Return()

    # Function_30_5752 end

    def Function_31_57BE(): pass

    label("Function_31_57BE")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0243
    ChrTalk(
        0x10,
        (
            "それじゃ、さっそく導力ネットの\x01",
            "チェックに入ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x10,
        (
            "化物がうろついていたときの青いモヤで、\x01",
            "通信が繋がりにくくなっていたからね。\x01",
            "システムにも影響があったかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "オッケー、了解だ。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xF,
        (
            "んじゃ、まずはタワーの端末から\x01",
            "動作をテストしてみるとするか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_31_57BE end

    def Function_32_58DC(): pass

    label("Function_32_58DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD8")
    TurnDirection(0xFE, 0x103, 0)

    #C0247
    ChrTalk(
        0xFE,
        (
            "ティオ君……\x01",
            "あの《大樹》に向かうんだってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "もしティオ君に何かあったら……\x01",
            "そう思うと身が引き裂かれそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        "#00206F……主任、あまり心配は──\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "……ハッ、そうだ！\x01",
            "僕も魔導杖を持って君たちに\x01",
            "同行するというのはどうだろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "魔導杖の仕組みは理解してるし、\x01",
            "戦闘ではサポートクラフトで\x01",
            "ティオ君を援護できるかもしれない！\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "うんうん、それがいい！\x01",
            "そうと決まればさっそく準備を整えて……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        "#00211Fウザすぎるので結構です。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ADE")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5ADE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B04")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B2A")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B50")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B50")

    Sleep(1000)

    #C0254
    ChrTalk(
        0x101,
        "#00012F（……相変わらずだなあ。）\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#00204F……主任、あまり心配を\x01",
            "しすぎないでください。\x02\x03",

            "#00202F皆さんやキーアと一緒に、\x01",
            "きっと無事に帰ってきますから。\x02\x03",

            "それに、主任の役割は\x01",
            "あくまで混乱する市内にあるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        "ティ、ティオ君……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "……そうだね、\x01",
            "ティオ君がそう言うなら……\x01",
            "僕はここでの作業に集中するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "その代わり、約束してくれ。\x01",
            "絶対に無事に帰ってくるってね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 3)
    Jump("loc_5FE5")

    label("loc_5CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F21")

    #C0259
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "《結社》の博士とやらは\x01",
            "白い人形と一緒に去ったそうだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#00206Fええ……正直２度と\x01",
            "関わり合いになりたくありませんが。\x02\x03",

            "#00211Fあんな人と比べたら、主任の方が\x01",
            "千倍くらいマシに思えます。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "ティ、ティオ君！（じぃん……）\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00012F（比較対象がアレなだけに\x01",
            "  喜んでいいか微妙そうだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        "しかし《アイオーン》か……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#00205F……主任？\x01",
            "どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        "アハハ、何でもないよ。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "（ウチで開発してる《エイオンシステム》と\x01",
            "  同じ語源みたいだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "（……さすがに偶然、だよねぇ？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5FE5")

    label("loc_5F21")


    #C0269
    ChrTalk(
        0xFE,
        (
            "僕はここで\x01",
            "みんなの帰りを待ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "本当はついていきたいけど……\x01",
            "ティオ君に断られてしまったら\x01",
            "さすがに仕方がないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "その代わり、約束してくれ。\x01",
            "絶対に無事に帰ってくるってね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE5")

    Jump("loc_627D")

    label("loc_5FEA")

    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F6")

    #C0272
    ChrTalk(
        0xFE,
        (
            "うーん、本当なら\x01",
            "湿原地帯の詳しい状況なんかも\x01",
            "分かればよかったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "……ああっ、何だか急に\x01",
            "心配になってきてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "そんな得体の知れない場所に\x01",
            "ティオ君を送り出すなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#00203F遊撃士さんたちを\x01",
            "無事に連れ戻す為です。\x02\x03",

            "主任もあまり心配せずに\x01",
            "待っていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "ティオ君……\x01",
            "本当に立派になったねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "財団に来た時はあんなに\x01",
            "小さかったっていうのに……\x01",
            "うっ、なんだか泣けてきたよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x103,
        (
            "#00211F……鬱陶しいですから、\x01",
            "こんな所でマジ泣きは\x01",
            "やめてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_627D")

    label("loc_61F6")


    #C0279
    ChrTalk(
        0xFE,
        (
            "得体の知れない場所に\x01",
            "ティオ君を送り出すのは、\x01",
            "心配でたまらないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "ティオ君も立派になったんだ。\x01",
            "きっと大丈夫だよねっ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_627D")

    TalkEnd(0xFE)
    Return()

    # Function_32_58DC end

    def Function_33_6281(): pass

    label("Function_33_6281")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B9")

    #C0281
    ChrTalk(
        0x22,
        (
            "#02302Fそういえばアンタら……\x01",
            "『ポムっと！』のアカウントを\x01",
            "持ってるんだって？\x02\x03",

            "#02304Fフフン、折角だからこのヨナ様の\x01",
            "アカウントをプレゼントしてやるぜ。\x02\x03",

            "#02302F開発段階から関わってたオレに\x01",
            "勝てるもんなら勝ってみろよな～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0282
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ヨナのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_665B")

    label("loc_63B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E9")

    #C0283
    ChrTalk(
        0x22,
        (
            "#02306F雨の中スタコラ歩いてきて、\x01",
            "さすがに疲れちまったぜ。\x02\x03",

            "#02300F財団の支部に戻る前に\x01",
            "思う存分ダラけとかなきゃな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00005Fおいおい……\x01",
            "屋上まではエレベーターだし\x01",
            "そんな大した運動じゃなかっただろ？\x02\x03",

            "#00001F運動不足がすぎるのはよくないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x103,
        (
            "#00203F仕方ありません、ヨナは\x01",
            "もやしっ子症候群#6Rシンドローム#ですから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x22,
        (
            "#02310Fな、なんだよ、\x01",
            "その症候群ってのは……\x02\x03",

            "#02306Fフン、まったく……\x01",
            "湿地帯に行くなら\x01",
            "さっさと行けっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そうさせてもらうよ。\x01",
            "手伝ってくれてありがとうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_665B")

    label("loc_65E9")


    #C0288
    ChrTalk(
        0x22,
        (
            "#02303Fオレは思う存分\x01",
            "ダラけてから帰るとするぜ。\x02\x03",

            "#02301Fアンタらも、湿地帯に行くなら\x01",
            "さっさと行けっつーの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665B")

    TalkEnd(0xFE)
    Return()

    # Function_33_6281 end

    def Function_34_665F(): pass

    label("Function_34_665F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6905")

    #C0289
    ChrTalk(
        0x20,
        (
            "#02100Fあら、ロイド君たち。\x01",
            "相変わらず忙しそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#00000Fええまあ。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#00100Fグレイスさんたちは\x01",
            "議会の取材か何かですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x20,
        (
            "#02109Fご明察、今度新しく採決された\x01",
            "法案に関する取材でね～。\x02\x03",

            "ついでに、色んな議員先生から\x01",
            "国家独立に対するそれぞれの\x01",
            "考え方なんかも伺う予定なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど、社会ネタも\x01",
            "ど真ん中という感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x20,
        (
            "#02106Fそう、その通りなのよ～。\x02\x03",

            "政界方面も最近は\x01",
            "スキャンダルが少なくて\x01",
            "つまらないっていうか……\x02\x03",

            "#02102Fう～ん、どこかに\x01",
            "良いゴシップネタは\x01",
            "転がっていないものかしら？\x02",
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

    #C0295
    ChrTalk(
        0x101,
        "#00006F心配事はそこですか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 7)
    Jump("loc_6A54")

    label("loc_6905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B8")

    #C0296
    ChrTalk(
        0x20,
        (
            "#02106Fスキャンダルが少ないのは\x01",
            "良い事には違いないんだけど、\x01",
            "最近ゴシップネタが弱いのよね～。\x02\x03",

            "#02102Fう～ん、どこかに良いネタは\x01",
            "転がっていないものかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A37")

    label("loc_69B8")


    #C0297
    ChrTalk(
        0x20,
        (
            "#02100Fあ、そうそう。\x01",
            "一押しグルメがまとまったら\x01",
            "通信社の受付で呼び出してね。\x02\x03",

            "#02109Fそれじゃ、よろしく頼んだわよ～♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 5)

    label("loc_6A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6A54")
    ClearScenarioFlags(0x0, 5)

    label("loc_6A54")

    TalkEnd(0xFE)
    Return()

    # Function_34_665F end

    def Function_35_6A58(): pass

    label("Function_35_6A58")

    TalkBegin(0xFE)

    #C0298
    ChrTalk(
        0xFE,
        (
            "グレイス先輩……議員の方に\x01",
            "変な事を聞かなきゃいいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "ふう、安全装置役も大変ですよ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_6A58 end

    def Function_36_6AC0(): pass

    label("Function_36_6AC0")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ACD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B76")

    #C0300
    ChrTalk(
        0x13,
        (
            "#10100Fメンバー編成ですね、\x01",
            "了解しました！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_6CEF")

    label("loc_6B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B8A")
    Jump("loc_6CEF")

    label("loc_6B8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C89")

    #C0301
    ChrTalk(
        0x13,
        (
            "#10100F派手に壊れていますけど……\x01",
            "各種機能は生きているみたいです。\x02\x03",

            "一通り事態が収拾したら、\x01",
            "きっと修理してあげたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x103,
        (
            "#00204Fそうですね……\x01",
            "ロバーツ主任やギヨーム親方にも\x01",
            "手伝ってもらいましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6CEF")

    label("loc_6C89")


    #C0303
    ChrTalk(
        0x13,
        (
            "#10100F各種機能は生きているみたいです。\x02\x03",

            "一通り事態が収拾したら、\x01",
            "きっと修理してあげたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CEF")

    Jump("loc_6ACD")

    label("loc_6CF4")

    TalkEnd(0xFE)
    Return()

    # Function_36_6AC0 end

    def Function_37_6CF8(): pass

    label("Function_37_6CF8")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA9")

    #C0304
    ChrTalk(
        0x14,
        "#10400Fフフ、メンバーを代えるのかい？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_6F9E")

    label("loc_6DA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DBD")
    Jump("loc_6F9E")

    label("loc_6DBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF0")

    #C0305
    ChrTalk(
        0x14,
        (
            "#10406F倒しても倒しても、\x01",
            "無尽蔵に新手が湧いてくる……\x02\x03",

            "やれやれ、厄介なものを\x01",
            "使われたものだね。\x02\x03",

            "#10401Fこのままじゃ外の連中も\x01",
            "消耗するばかりだろうし……\x01",
            "急いだほうがいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#00101Fええ、早くおじさまに辿り着いて\x01",
            "こんな事、やめさせないと……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6F9E")

    label("loc_6EF0")


    #C0307
    ChrTalk(
        0x14,
        (
            "#10406F倒しても倒しても、\x01",
            "無尽蔵に新手が湧いてくる……\x01",
            "やれやれ、厄介な相手だね。\x02\x03",

            "#10401Fこのままじゃ外の連中も\x01",
            "消耗するばかりだろうし……\x01",
            "急いだほうがいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9E")

    Jump("loc_6D05")

    label("loc_6FA3")

    TalkEnd(0xFE)
    Return()

    # Function_37_6CF8 end

    def Function_38_6FA7(): pass

    label("Function_38_6FA7")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71CE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705C")

    #C0308
    ChrTalk(
        0x15,
        "#10702Fはい、メンバーを変更するんですね。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_71C9")

    label("loc_705C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7070")
    Jump("loc_71C9")

    label("loc_7070")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7165")

    #C0309
    ChrTalk(
        0x15,
        (
            "#10703F今のところ、このロビーに\x01",
            "敵の気配はありませんが……\x02\x03",

            "警戒は怠らないほうが\x01",
            "よさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#00300F万が一は十分ありえそうだしな……\x01",
            "頼むぜ、リーシャちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x15,
        "#10702Fええ、お任せを。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_71C9")

    label("loc_7165")


    #C0312
    ChrTalk(
        0x15,
        (
            "#10703F念の為、周囲に\x01",
            "気を巡らせたほうが\x01",
            "よさそうですね。\x02\x03",

            "#10701F皆さんも気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71C9")

    Jump("loc_6FB4")

    label("loc_71CE")

    TalkEnd(0xFE)
    Return()

    # Function_38_6FA7 end

    def Function_39_71D2(): pass

    label("Function_39_71D2")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7298")

    #C0313
    ChrTalk(
        0x16,
        (
            "#00600Fメンバーを変更するんだな？\x01",
            "……さっさと選ぶがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_73C3")

    label("loc_7298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72AC")
    Jump("loc_73C3")

    label("loc_72AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7381")

    #C0314
    ChrTalk(
        0x16,
        (
            "#00603F打ち合わせどおり、\x01",
            "万が一の場合に備えて\x01",
            "待機した２名で入口を守るぞ。\x02\x03",

            "#00601F……さあ、もたもたするな。\x01",
            "お前たちはさっさと行くがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        "#00001F……はい！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_73C3")

    label("loc_7381")


    #C0316
    ChrTalk(
        0x16,
        (
            "#00601F……さあ、もたもたするな。\x01",
            "さっさと行ってくるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C3")

    Jump("loc_71DF")

    label("loc_73C8")

    TalkEnd(0xFE)
    Return()

    # Function_39_71D2 end

    def Function_40_73CC(): pass

    label("Function_40_73CC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7427")

    #A0317
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターは\x01",
            "他のフロアで使用中らしく、\x01",
            "止まる気配がない。\x07\x00\x02",
        )
    )

    Jump("loc_74C0")

    label("loc_7427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7472")

    #A0318
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのシャッターは\x01",
            "固く閉ざされている。\x07\x00\x02",
        )
    )

    Jump("loc_74C0")

    label("loc_7472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_74C0")

    #A0319
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターは\x01",
            "他のフロアで使用中らしく、\x01",
            "止まる気配がない。\x07\x00\x02",
        )
    )


    label("loc_74C0")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_73CC end

    def Function_41_74C8(): pass

    label("Function_41_74C8")

    Sound(160, 0, 100, 0)
    Return()

    # Function_41_74C8 end

    def Function_42_74CF(): pass

    label("Function_42_74CF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch05600.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch00202.itc", 0x22)
    SoundLoad(3454)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    SetChrPos(0x101, 400, 0, -6100, 0)
    SetChrPos(0x102, -1200, 0, -6900, 0)
    SetChrPos(0x103, 1200, 0, -6900, 0)
    SetChrPos(0x104, 1200, 0, -8500, 0)
    SetChrPos(0x109, -1200, 0, -8500, 0)
    SetChrPos(0x105, -400, 0, -9300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 15500, 0, 1000, 270)
    OP_4B(0x16, 0xFF)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 15500, 0, 1000, 270)
    OP_68(0, 4500, 17500, 0)
    MoveCamera(27, 5, 0, 0)
    OP_6E(690, 0)
    SetCameraDistance(27000, 0)
    OP_68(0, 2000, 7500, 7000)
    MoveCamera(23, 5, 0, 7000)
    FadeToBright(2000, 0)
    Sleep(4000)

    def lambda_76AE():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_76AE)
    Sleep(200)

    def lambda_76CB():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_76CB)
    Sleep(200)

    def lambda_76E8():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_76E8)
    Sleep(200)

    def lambda_7705():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7705)
    Sleep(200)

    def lambda_7722():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7722)
    Sleep(200)

    def lambda_773F():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_773F)
    Sleep(100)

    def lambda_775C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_775C)
    Sleep(300)

    def lambda_7770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7770)
    Sleep(200)

    def lambda_7784():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7784)
    Sleep(600)

    def lambda_7798():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7798)
    Sleep(200)

    def lambda_77AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_77AC)
    Sleep(300)

    def lambda_77C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_77C0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0320
    ChrTalk(
        0x101,
        "#00002F#11P凄いな……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#00302F#11Pなんつーか、豪華かつ\x01",
            "ハイテクって感じだねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x109,
        (
            "#10109F#5PＩＢＣビル以上に\x01",
            "近未来的な雰囲気ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        (
            "#00203F#11Pたしかビルの全フロアに\x01",
            "導力ネットが引かれているはずです。\x02\x03",

            "#00200FＩＢＣとも連動しているため\x01",
            "株価指数などのデータも\x01",
            "リアルタイムで参照できるとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#00104F#5Pええ、そのあたりは\x01",
            "おじさまのアイデアみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x105,
        (
            "#10302F#11Pなるほど、銀行家ならではの\x01",
            "発想ってわけだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(670, 1000, -1310, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17580, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0326
    ChrTalk(
        0x101,
        (
            "#00000F#5Pよし、それじゃあ\x01",
            "ダドリーさんが来るまで\x01",
            "待たせてもらうか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A18():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7A18)
    Sleep(50)

    def lambda_7A28():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7A28)
    Sleep(50)

    def lambda_7A38():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A38)
    Sleep(50)

    def lambda_7A48():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7A48)
    Sleep(50)

    def lambda_7A58():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7A58)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0327
    ChrTalk(
        0x102,
        (
            "#6P#00102F今日は一般客もいないし、\x01",
            "そちらのソファで\x01",
            "待たせてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_68(4500, 900, 7600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 3300, 0, 6700, 90)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x2)
    SetChrPos(0x102, 5200, 50, 6500, 270)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 5200, 50, 7600, 270)
    SetChrPos(0x104, 2700, 0, 7700, 90)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, 5200, 50, 8700, 270)
    SetChrPos(0x105, 3000, 0, 9100, 135)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0328
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K同日、１２：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7111", 0)
    SetCameraDistance(18500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x16, 0x80)
    OP_C9(0x0, 0x80000000)

    #N0329
    NpcTalk(
        0x16,
        "男の声",
        "#3454V#30W#11A──来ていたか。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 43)

    def lambda_7CAB():

        label("loc_7CAB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7CAB")

    QueueWorkItem2(0x101, 2, lambda_7CAB)
    Sleep(50)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 5000, 0, 6500, 270)

    def lambda_7CE4():

        label("loc_7CE4")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7CE4")

    QueueWorkItem2(0x102, 2, lambda_7CE4)
    Sleep(50)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 5000, 0, 7600, 270)

    def lambda_7D17():

        label("loc_7D17")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D17")

    QueueWorkItem2(0x103, 2, lambda_7D17)
    Sleep(50)

    def lambda_7D2C():

        label("loc_7D2C")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D2C")

    QueueWorkItem2(0x104, 2, lambda_7D2C)
    Sleep(50)

    def lambda_7D41():

        label("loc_7D41")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D41")

    QueueWorkItem2(0x105, 2, lambda_7D41)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 5000, 0, 8700, 270)

    def lambda_7D71():
        OP_95(0xFE, 4500, 0, 8700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7D71)
    WaitChrThread(0x109, 1)

    def lambda_7D8F():

        label("loc_7D8F")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D8F")

    QueueWorkItem2(0x109, 2, lambda_7D8F)
    Sleep(300)
    Fade(500)
    OP_68(10500, 900, 1000, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(4000, 900, 6200, 4500)
    OP_0D()
    OP_6F(0x79)

    #C0330
    ChrTalk(
        0x101,
        "#00000F#5Pダドリーさん。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        "#11P#00104Fお疲れ様です。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x16, 3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0332
    AnonymousTalk(
        0x16,
        (
            "現在、正午ちょうど──\x02\x03",

            "通商会議が始まるのは\x01",
            "１３：００となっている。\x02\x03",

            "あと３０分もすれば\x01",
            "首脳たちがやって来るだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0333
    ChrTalk(
        0x101,
        "#00001F#5Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#11P#00101Fそれで、私たちの方は\x01",
            "どちらに向かえば？\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x16,
        (
            "#12P#00606F本当ならば、私が会場回りを\x01",
            "軽く案内するつもりだったが……\x02\x03",

            "思わぬ人が、お前たちを\x01",
            "案内してくれると申し出てな。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        "#00005F#5P思わぬ人……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)

    #N0337
    NpcTalk(
        0x23,
        "男性の声",
        (
            "──やあ諸君。\x01",
            "よく来てくれたね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(7800, 1000, 1000, 3000)
    MoveCamera(75, 21, 0, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_8103():
        OP_95(0xFE, 7800, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8103)

    def lambda_811D():

        label("loc_811D")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_811D")

    QueueWorkItem2(0x101, 2, lambda_811D)

    def lambda_812F():

        label("loc_812F")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_812F")

    QueueWorkItem2(0x102, 2, lambda_812F)

    def lambda_8141():

        label("loc_8141")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8141")

    QueueWorkItem2(0x103, 2, lambda_8141)

    def lambda_8153():

        label("loc_8153")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8153")

    QueueWorkItem2(0x104, 2, lambda_8153)

    def lambda_8165():

        label("loc_8165")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8165")

    QueueWorkItem2(0x109, 2, lambda_8165)

    def lambda_8177():

        label("loc_8177")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8177")

    QueueWorkItem2(0x105, 2, lambda_8177)

    def lambda_8189():

        label("loc_8189")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8189")

    QueueWorkItem2(0x16, 2, lambda_8189)
    WaitChrThread(0x23, 1)
    TurnDirection(0x23, 0x101, 500)
    OP_6F(0x79)

    #C0338
    ChrTalk(
        0x101,
        "#00011Fディーター市長！？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        "#00105Fおじさま……！\x02",
    )

    CloseMessageWindow()

    def lambda_81E2():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_81E2)
    Sleep(1000)
    Fade(500)
    OP_68(4000, 900, 6200, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)

    def lambda_8232():
        OP_96(0xFE, 0x898, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8232)
    WaitChrThread(0x23, 1)
    OP_93(0x23, 0x0, 0x1F4)
    EndChrThread(0x16, 0x2)
    EndChrThread(0x101, 0x2)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0340
    AnonymousTalk(
        0x23,
        (
            "半月ぶりだね、\x01",
            "エリィ、ロイド君。\x02\x03",

            "ワジ君にノエル君に……\x02\x03",

            "おっと、ランディ君と\x01",
            "ティオ君は久しぶりかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0341
    ChrTalk(
        0x104,
        "#00309F#5Pハハ、お久しぶりッス。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#5P#00204Fご無沙汰してます。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        "#00102F#11Pでも、どうしておじさまが……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00002F#5P通商会議の直前で\x01",
            "お忙しいんじゃないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x23,
        (
            "#12P#02804F準備ならとっくに済ませて\x01",
            "あとは首脳たちを待つだけでね。\x02\x03",

            "#02800F気分転換も兼ねて君たちを\x01",
            "案内させてもらおうと思ったんだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x16, 500)
    Sleep(150)

    #C0346
    ChrTalk(
        0x23,
        "#02800F#11Pダドリー君、構わないな？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x16,
        "#6P#00606Fフウ……市長がそう仰るなら。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(150)

    #C0348
    ChrTalk(
        0x16,
        (
            "#6P#00600F──お前たち、くれぐれも\x01",
            "市長に失礼のないように。\x02\x03",

            "それと、一通り案内されたら\x01",
            "３４Ｆの警備対策室に来い。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 500)

    #C0349
    ChrTalk(
        0x101,
        "#5P#00000F了解しました。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x23, 500)
    Sleep(300)

    #C0350
    ChrTalk(
        0x16,
        "#6P#00603Fでは市長、また後ほど。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x23,
        "#02800F#11Pああ、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    def lambda_85DD():

        label("loc_85DD")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_85DD")

    QueueWorkItem2(0x101, 2, lambda_85DD)

    def lambda_85EF():

        label("loc_85EF")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_85EF")

    QueueWorkItem2(0x102, 2, lambda_85EF)

    def lambda_8601():

        label("loc_8601")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8601")

    QueueWorkItem2(0x103, 2, lambda_8601)

    def lambda_8613():

        label("loc_8613")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8613")

    QueueWorkItem2(0x104, 2, lambda_8613)

    def lambda_8625():

        label("loc_8625")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8625")

    QueueWorkItem2(0x109, 2, lambda_8625)

    def lambda_8637():

        label("loc_8637")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8637")

    QueueWorkItem2(0x105, 2, lambda_8637)

    def lambda_8649():

        label("loc_8649")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8649")

    QueueWorkItem2(0x23, 2, lambda_8649)
    OP_92(0x16, 0x0, 0x8FC, 0x1F4)
    OP_68(1000, 900, 2200, 3000)

    def lambda_8679():
        OP_95(0xFE, 0, 0, 2300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8679)
    WaitChrThread(0x16, 1)

    def lambda_8697():
        OP_95(0xFE, 0, 0, -5000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8697)
    Sleep(2000)
    Sound(107, 0, 100, 0)

    def lambda_86BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_86BA)
    WaitChrThread(0x16, 1)
    Sound(107, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x23, 0x2)
    SetChrFlags(0x16, 0x80)
    StopBGM(0xFA0)

    #C0352
    ChrTalk(
        0x23,
        (
            "#02804Fフフ、有能な捜査官だが\x01",
            "少し融通が利かない所があるな。\x02\x03",

            "#02800F彼の職分からすると\x01",
            "それもまた美徳なのだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#00012F#6Pハハ……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x105,
        (
            "#10304F#6Pま、鬼の捜査一課としての\x01",
            "威厳もあるんだろうからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(3500, 1000, 6000, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 3100, 0, 6700, 180)
    SetChrPos(0x104, 2100, 0, 7500, 180)
    SetChrPos(0x105, 2700, 0, 9100, 180)
    SetChrPos(0x102, 5000, 0, 6500, 225)
    SetChrPos(0x103, 4600, 0, 7600, 180)
    SetChrPos(0x109, 4300, 0, 8700, 180)
    OP_0D()
    OP_93(0x23, 0x0, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7550", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0355
    ChrTalk(
        0x23,
        (
            "#6P#02805Fおっと、肝心なことを\x01",
            "言い忘れていたな……\x02\x03",

            "#02809F──支援課の諸君、\x01",
            "《オルキスタワー》へようこそ！\x02\x03",

            "さあ、付いて来たまえ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_890F():

        label("loc_890F")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_890F")

    QueueWorkItem2(0x101, 2, lambda_890F)

    def lambda_8921():

        label("loc_8921")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8921")

    QueueWorkItem2(0x102, 2, lambda_8921)

    def lambda_8933():

        label("loc_8933")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8933")

    QueueWorkItem2(0x103, 2, lambda_8933)

    def lambda_8945():

        label("loc_8945")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8945")

    QueueWorkItem2(0x104, 2, lambda_8945)

    def lambda_8957():

        label("loc_8957")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8957")

    QueueWorkItem2(0x109, 2, lambda_8957)

    def lambda_8969():

        label("loc_8969")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8969")

    QueueWorkItem2(0x105, 2, lambda_8969)
    OP_92(0x23, 0x1B58, 0x3E8, 0x1F4)
    OP_68(6500, 1000, 3000, 3000)

    def lambda_8999():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8999)
    WaitChrThread(0x23, 1)

    def lambda_89B7():
        OP_95(0xFE, 12000, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_89B7)
    WaitChrThread(0x23, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x23, 0x2)
    SetChrFlags(0x23, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(3500, 1000, 7600, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0356
    ChrTalk(
        0x104,
        "#00302F#5Pはは、相変わらずだな。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#5P#00204Fさすがマリアベルさんの\x01",
            "お父さんなだけはありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x102,
        (
            "#5P#00109Fま、まあせっかく\x01",
            "案内してくださるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#5P#00000Fああ、お言葉に甘えるか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    SetChrPos(0x0, 3500, 0, 7600, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetScenarioFlags(0x141, 7)
    OP_29(0xA4, 0x4, 0x2)
    OP_29(0xA4, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8BEA")
    Jump("loc_8BEF")

    label("loc_8BEA")

    OP_29(0x71, 0x4, 0x40)

    label("loc_8BEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C00")
    Jump("loc_8C05")

    label("loc_8C00")

    OP_29(0x72, 0x4, 0x40)

    label("loc_8C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C16")
    Jump("loc_8C1B")

    label("loc_8C16")

    OP_29(0x77, 0x4, 0x40)

    label("loc_8C1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C2C")
    Jump("loc_8C31")

    label("loc_8C2C")

    OP_29(0x79, 0x4, 0x40)

    label("loc_8C31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C42")
    Jump("loc_8C47")

    label("loc_8C42")

    OP_29(0x7A, 0x4, 0x40)

    label("loc_8C47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C58")
    Jump("loc_8C5D")

    label("loc_8C58")

    OP_29(0x7B, 0x4, 0x40)

    label("loc_8C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C6E")
    Jump("loc_8C73")

    label("loc_8C6E")

    OP_29(0x7C, 0x4, 0x40)

    label("loc_8C73")

    OP_1B(0x0, 0x0, 0x33)
    EventEnd(0x5)
    Return()

    # Function_42_74CF end

    def Function_43_8C7B(): pass

    label("Function_43_8C7B")


    def lambda_8C80():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8C80)
    WaitChrThread(0x16, 1)

    def lambda_8C9E():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8C9E)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x0, 0x1F4)
    Return()

    # Function_43_8C7B end

    def Function_44_8CBF(): pass

    label("Function_44_8CBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SetChrPos(0x101, 72000, 0, -600, 90)
    SetChrPos(0x102, 72000, 0, 500, 90)
    SetChrPos(0x103, 70900, 0, -300, 90)
    SetChrPos(0x104, 70900, 0, 800, 90)
    SetChrPos(0x109, 69800, 0, -600, 90)
    SetChrPos(0x105, 69800, 0, 500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 80500, 0, 1800, 270)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0xA)
    OP_68(87000, 900, 2000, 0)
    MoveCamera(53, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_68(75000, 900, 1000, 5000)
    SetCameraDistance(19000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0360
    ChrTalk(
        0x109,
        "#6P#10105Fエレベーターが３基も……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x105,
        "#6P#10302Fへえ、さすが豪勢だねぇ。\x02",
    )

    CloseMessageWindow()

    def lambda_8E21():
        OP_97(0x102, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E21)
    Sleep(50)

    def lambda_8E3E():
        OP_97(0x101, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E3E)
    Sleep(50)

    def lambda_8E5B():
        OP_97(0x104, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8E5B)
    Sleep(50)

    def lambda_8E78():
        OP_97(0x103, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E78)
    Sleep(50)

    def lambda_8E95():
        OP_97(0x105, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E95)
    Sleep(50)

    def lambda_8EB2():
        OP_97(0x109, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8EB2)
    Sleep(1000)
    Fade(500)
    OP_68(79200, 1000, 2000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    WaitChrThread(0x109, 0)

    #C0362
    ChrTalk(
        0x23,
        (
            "#02804F#11Pまあ、地上４０階の高さだからね。\x02\x03",

            "#02800F専用のエレベーターを入れたら\x01",
            "全部で６基が運用されているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#6P#00002Fそれは凄いですね……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x23,
        (
            "#02803F#11Pさて、全部のフロアを\x01",
            "案内するわけにもいかないから、\x01",
            "会議関連のフロアに限定しよう。\x02\x03",

            "#02800Fまずは警備対策室のある３４階だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x102,
        "#00102F#6Pよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_92(0x23, 0x13C68, 0xCE4, 0x1F4)
    BeginChrThread(0x23, 3, 0, 46)
    Sleep(1000)
    BeginChrThread(0x101, 0, 0, 45)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("c1520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_8CBF end

    def Function_45_909E(): pass

    label("Function_45_909E")

    BeginChrThread(0x101, 3, 0, 46)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 46)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 46)
    Sleep(900)
    BeginChrThread(0x104, 3, 0, 46)
    Sleep(400)
    BeginChrThread(0x109, 3, 0, 46)
    Sleep(900)
    BeginChrThread(0x105, 3, 0, 46)
    Return()

    # Function_45_909E end

    def Function_46_90D2(): pass

    label("Function_46_90D2")


    def lambda_90D7():
        OP_95(0xFE, 81000, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90D7)
    WaitChrThread(0xFE, 1)

    def lambda_90F5():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90F5)
    Sleep(500)

    def lambda_9112():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9112)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_90D2 end

    def Function_47_9123(): pass

    label("Function_47_9123")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(0, 1000, -1700, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 400, 0, -6100, 0)
    SetChrPos(0x102, -1200, 0, -6900, 0)
    SetChrPos(0x103, 1200, 0, -6900, 0)
    SetChrPos(0x104, 1200, 0, -8500, 0)
    SetChrPos(0x109, -1200, 0, -8500, 0)
    SetChrPos(0x105, -400, 0, -9300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_9253():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9253)
    Sleep(200)

    def lambda_9270():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9270)
    Sleep(200)

    def lambda_928D():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_928D)
    Sleep(200)

    def lambda_92AA():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_92AA)
    Sleep(200)

    def lambda_92C7():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_92C7)
    Sleep(200)

    def lambda_92E4():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_92E4)
    SetCameraDistance(18500, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)
    Sleep(100)

    def lambda_9319():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9319)
    Sleep(300)

    def lambda_932D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_932D)
    Sleep(200)

    def lambda_9341():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9341)
    Sleep(600)

    def lambda_9355():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9355)
    Sleep(200)

    def lambda_9369():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9369)
    Sleep(300)

    def lambda_937D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_937D)
    Sound(803, 2, 100, 0)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_93B3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_93B3)
    Sleep(50)

    def lambda_93C3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_93C3)
    Sleep(50)

    def lambda_93D3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_93D3)
    Sleep(50)

    def lambda_93E3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_93E3)
    Sleep(50)

    def lambda_93F3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93F3)

    #C0366
    ChrTalk(
        0x101,
        "#00005F#11Pおっと……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もしもし、アンタら今ドコ？\x02\x03",

            "こっちは各種機器の\x01",
            "設置が終わったとこだぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0368
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004Fああ、ちょうどタワーの\x01",
            "エントランスに来たところだ。\x02\x03",

            "#00000Fこのまま屋上に向かえばいいのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0369
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、受付に言えばエレベーター用の\x01",
            "認証カードをくれるそうだぜ。\x02\x03",

            "とっとと上がって来いよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0370
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002F分かった、お疲れさん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0371
    ChrTalk(
        0x103,
        "#11P#00202F準備は完了みたいですね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0xB5, 0x1F4)
    Sleep(100)

    #C0372
    ChrTalk(
        0x101,
        (
            "#00000F#5Pああ、受付で認証カードを借りて\x01",
            "屋上に上がろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#6P#00104F雨も降っている事だし\x01",
            "あまり待たせない方がいいわね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 0, 0, -1500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 3)
    OP_29(0xA9, 0x1, 0x2)
    ClearMapFlags(0x10000000)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_47_9123 end

    def Function_48_974B(): pass

    label("Function_48_974B")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 2100, 20000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 1000, 19000, 0)
    SetChrPos(0x102, -2300, 1000, 18200, 45)
    SetChrPos(0x103, -2000, 1000, 17400, 45)
    SetChrPos(0x104, 800, 1000, 17600, 0)
    SetChrPos(0x109, -500, 1000, 17600, 0)
    SetChrPos(0x105, -200, 1000, 16500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0374
    ChrTalk(
        0x8,
        "#5Pようこそ、オルキスタワーへ。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        "#5Pあ、特務支援課の方々ですね？\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            "#00000F#11Pええ、認証カードを\x01",
            "発行していただけるとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        "#5Pはい、こちらになります。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0378
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x35E, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0379
    ChrTalk(
        0x8,
        (
            "#5Pそちらのカードを\x01",
            "エレベーター内のパネルにかざすと\x01",
            "最上階の４０Ｆに直通で上がれます。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#5P１ヶ月のみ有効の使い捨てですので\x01",
            "利用後はご自由に処分されてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        "#00011F#11Pりょ、了解しました。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x109,
        "#12P#10112F（何だか凄いですね……）\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x104,
        (
            "#00306F#11P（ああ、ＩＢＣビルよりも\x01",
            "  さらに進んでやがるな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x105,
        (
            "#12P#10302F（さすがは最新技術の\x01",
            "  カタマリってところかな？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 0, 1000, 17500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 4)
    SetScenarioFlags(0x2, 1)
    EventEnd(0x5)
    Return()

    # Function_48_974B end

    def Function_49_9AA9(): pass

    label("Function_49_9AA9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC9")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_9AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ADD")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_9ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AF1")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_9AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B05")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_9B05")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0x101, 700, 0, 5800, 45)
    SetChrPos(0x102, 600, 0, 7100, 90)
    SetChrPos(0x103, -500, 0, 6100, 45)
    SetChrPos(0x104, -600, 0, 7400, 90)
    SetChrPos(0x109, 3300, 0, 6300, 0)
    SetChrPos(0x105, -1700, 0, 7500, 90)
    SetChrPos(0x106, -600, 0, 9200, 135)
    SetChrPos(0x10A, -1700, 0, 5300, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(0, 500, -2500, 0)
    MoveCamera(25, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_68(1000, 500, 7500, 7000)
    MoveCamera(60, 35, 0, 7000)
    SetCameraDistance(17000, 7000)
    PlayBGM("ed7302", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(3000, 1300, 9000, 0)
    MoveCamera(15, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(16500, 3500)
    OP_6F(0x79)
    Fade(500)
    OP_68(1400, 1300, 7400, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15680, 0)
    OP_0D()
    Sleep(300)

    #C0385
    ChrTalk(
        0x109,
        (
            "#12P#10104F……大丈夫です。\x01",
            "各種機能は生きています。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそうか……\x01",
            "こいつには世話をかけるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#00104F#6P……そうね。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x103,
        (
            "#6P#00202F後でちゃんと\x01",
            "修理してあげたいです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1700, 1000, 2000)
    SetCameraDistance(17500, 2000)
    Sleep(300)
    OP_25(0x82, 0x32)
    Sleep(200)
    OP_25(0x82, 0x3C)
    Sleep(300)

    def lambda_9DCB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_9DCB)
    Sleep(30)

    def lambda_9DDB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9DDB)
    Sleep(30)

    def lambda_9DEB():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_9DEB)
    Sleep(30)

    def lambda_9DFB():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9DFB)
    Sleep(30)

    def lambda_9E0B():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9E0B)
    Sleep(30)

    def lambda_9E1B():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9E1B)
    Sleep(30)

    def lambda_9E2B():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9E2B)
    Sleep(30)

    def lambda_9E3B():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9E3B)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    Sleep(500)

    #C0389
    ChrTalk(
        0x106,
        "#5P#10708F……まだ続きそうですね。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x105,
        (
            "#10401Fま、無尽蔵に新手が\x01",
            "沸いてくるみたいだからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_25(0x82, 0x32)
    Fade(500)
    OP_68(970, 1300, 6970, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15680, 0)
    OP_0D()
    OP_25(0x82, 0x28)
    TurnDirection(0x104, 0x101, 500)

    #C0391
    ChrTalk(
        0x104,
        (
            "#5P#00306F時間がねぇ……\x01",
            "とっととエレベーターで\x01",
            "上がるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)

    #C0392
    ChrTalk(
        0x10A,
        (
            "#6P#00603F打ち合わせ通り、\x01",
            "ここで２名が待機する。\x02\x03",

            "#00600F選ぶがいい、バニングス。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)

    def lambda_9FBB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9FBB)
    Sleep(30)

    def lambda_9FCB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9FCB)
    Sleep(30)

    def lambda_9FDB():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9FDB)
    Sleep(30)

    def lambda_9FEB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9FEB)
    Sleep(30)

    def lambda_9FFB():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_9FFB)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    #C0393
    ChrTalk(
        0x101,
        "#11P#00001F了解です。\x02",
    )

    CloseMessageWindow()
    StopSound(130, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    SetChrPos(0x0, 60, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    Call(0, 4)
    SetScenarioFlags(0x1A6, 0)
    OP_29(0xB1, 0x1, 0x9)
    OP_66(0x7, 0x1)
    OP_1B(0x0, 0x0, 0x33)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7151", "ed7302")
    ReplaceBGM("ed7352", "ed7302")
    ReplaceBGM("ed7550", "ed7302")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(130, 2, 40, 0)
    EventEnd(0x5)
    Return()

    # Function_49_9AA9 end

    def Function_50_A0CE(): pass

    label("Function_50_A0CE")

    EventBegin(0x1)
    OP_4B(0x1F, 0xFF)
    TurnDirection(0x1F, 0x0, 500)

    #C0394
    ChrTalk(
        0x1F,
        "皆さんは認証カードをお持ちですか？\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x1F,
        (
            "カードがなければ、エレベーターは\x01",
            "ご使用になれませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 74460, 0, 1270, 180)
    OP_93(0x1F, 0xB4, 0x0)
    OP_4C(0x1F, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_50_A0CE end

    def Function_51_A15F(): pass

    label("Function_51_A15F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A203")
    SetChrName("")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "広場の方から断続的な\x01",
            "銃撃と剣戟の音が聞こえてくる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0397
    ChrTalk(
        0x101,
        (
            "#00001F今こうしている間にも\x01",
            "みんなが戦ってくれている。\x02\x03",

            "――急いで先へ進もう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A257")

    #C0398
    ChrTalk(
        0x101,
        (
            "#00001Fあまり市長を待たせられないな。\x01",
            "――早く後を追いかけよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A257")

    SetChrPos(0x0, -290, 0, -3540, 0)
    EventEnd(0x4)
    Return()

    # Function_51_A15F end

    def Function_52_A26B(): pass

    label("Function_52_A26B")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A27D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3E9")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A2E8")
    MenuCmd(1, 0, "導力車で休憩する")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2E8")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A364")

    #C0399
    ChrTalk(
        0x101,
        (
            "#00001F……今は無理に動かす必要はないな。\x01",
            "事件が落ち着いたら修理に出そう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3E4")

    label("loc_A364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3DA")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_A39D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_A3B5")

    label("loc_A39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A3B0")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_A3B5")

    label("loc_A3B0")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_A3B5")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3E4")

    label("loc_A3DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3E4")

    Jump("loc_A27D")

    label("loc_A3E9")

    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_52_A26B end

    SaveToFile()

Try(main)
