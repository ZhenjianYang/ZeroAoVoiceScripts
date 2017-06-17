from ScenarioHelper import *

def main():
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
        "接待小姐莉莉埃",         # 1
        "接待小姐维奥拉",         # 2
        "莫雷特主任",             # 3
        "塔基库",                 # 4
        "蒂博巡警",               # 5
        "接待小姐兰菲",           # 6
        "罗伯兹主任",             # 7
        "研究员达比德",           # 8
        "研究员库雷",             # 9
        "玛格丽特夫人",           # 10
        "皮埃尔副局长",           # 11
        "诺艾尔",                 # 12
        "瓦吉",                   # 13
        "莉夏",                   # 14
        "达德利搜查官",           # 15
        "警官",                   # 16
        "市政府职员",             # 17
        "市政府职员",             # 18
        "市民",                   # 19
        "市民",                   # 20
        "游客",                   # 21
        "市民",                   # 22
        "贸易商利泽罗",           # 23
        "乔吉欧巡警",             # 24
        "格蕾丝",                 # 25
        "雷因兹",                 # 26
        "约纳",                   # 27
        "迪塔市长",               # 28
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
        "Function_6_EC2",          # 06, 6
        "Function_7_EC6",          # 07, 7
        "Function_8_1933",         # 08, 8
        "Function_9_1937",         # 09, 9
        "Function_10_2232",        # 0A, 10
        "Function_11_2236",        # 0B, 11
        "Function_12_2C19",        # 0C, 12
        "Function_13_2C1D",        # 0D, 13
        "Function_14_2CD3",        # 0E, 14
        "Function_15_2F9F",        # 0F, 15
        "Function_16_3A9D",        # 10, 16
        "Function_17_3B43",        # 11, 17
        "Function_18_3BFE",        # 12, 18
        "Function_19_3C3D",        # 13, 19
        "Function_20_3C6E",        # 14, 20
        "Function_21_3CBA",        # 15, 21
        "Function_22_3D31",        # 16, 22
        "Function_23_40F0",        # 17, 23
        "Function_24_4150",        # 18, 24
        "Function_25_41F7",        # 19, 25
        "Function_26_4283",        # 1A, 26
        "Function_27_42E2",        # 1B, 27
        "Function_28_4533",        # 1C, 28
        "Function_29_45CF",        # 1D, 29
        "Function_30_46FC",        # 1E, 30
        "Function_31_4752",        # 1F, 31
        "Function_32_4822",        # 20, 32
        "Function_33_4FD3",        # 21, 33
        "Function_34_52DB",        # 22, 34
        "Function_35_5600",        # 23, 35
        "Function_36_5660",        # 24, 36
        "Function_37_5836",        # 25, 37
        "Function_38_5A8D",        # 26, 38
        "Function_39_5C60",        # 27, 39
        "Function_40_5E1A",        # 28, 40
        "Function_41_5ED4",        # 29, 41
        "Function_42_5EDB",        # 2A, 42
        "Function_43_750D",        # 2B, 43
        "Function_44_7551",        # 2C, 44
        "Function_45_78DC",        # 2D, 45
        "Function_46_7910",        # 2E, 46
        "Function_47_7961",        # 2F, 47
        "Function_48_7F2D",        # 30, 48
        "Function_49_821D",        # 31, 49
        "Function_50_87F2",        # 32, 50
        "Function_51_885F",        # 33, 51
        "Function_52_8933",        # 34, 52
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
            "摆放着车辆杂志《音速疾驰》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('凉爽色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBE")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『凉爽色彩』\x07\x00",
            "已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('凉爽色彩', 1)

    label("loc_EBE")

    TalkEnd(0xFF)
    Return()

    # Function_5_E25 end

    def Function_6_EC2(): pass

    label("Function_6_EC2")

    Call(0, 7)
    Return()

    # Function_6_EC2 end

    def Function_7_EC6(): pass

    label("Function_7_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED8")
    Call(0, 48)
    Return()

    label("loc_ED8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F85")

    #C0003
    ChrTalk(
        0x8,
        (
            "兰花塔现在由\x01",
            "麦克道尔议长\x01",
            "负责管理。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "虽然还存在很多混乱的地方……\x01",
            "但这里会继续为市民服务，\x01",
            "这是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "今后也请\x01",
            "多多关照。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD2")

    label("loc_F85")


    #C0006
    ChrTalk(
        0x8,
        (
            "兰花塔今后会继续\x01",
            "为市民服务，\x01",
            "这是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "今后也请\x01",
            "多多关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD2")

    Jump("loc_192F")

    label("loc_FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FE5")
    Jump("loc_192F")

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FF3")
    Jump("loc_192F")

    label("loc_FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109B")

    #C0008
    ChrTalk(
        0x8,
        (
            "市民会馆今天将会举办\x01",
            "支援城市复兴的\x01",
            "慈善宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "为了让大家绽放笑颜，\x01",
            "宴会中将开展\x01",
            "许多活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "如果各位有时间，\x01",
            "请务必前去参加。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1103")

    label("loc_109B")


    #C0011
    ChrTalk(
        0x8,
        (
            "话说回来……\x01",
            "ＩＢＣ恢复业务的速度\x01",
            "真是惊人。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "我再次深刻体会到了\x01",
            "导力网络这项技术\x01",
            "有多么重要。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1103")

    Jump("loc_192F")

    label("loc_1108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1216")

    #C0013
    ChrTalk(
        0x8,
        (
            "市民们的不安情绪\x01",
            "仍然很严重，\x01",
            "这也是理所当然的……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "因为市民们对事件\x01",
            "提出的疑问只能得到\x01",
            "模棱两可的回答……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "但警备队的各位成员，\x01",
            "还有市长和议长都在竭力解决事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "总之，我们这些职员现在\x01",
            "一定要相信他们，\x01",
            "尽力做好力所能及的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A8")

    label("loc_1216")


    #C0017
    ChrTalk(
        0x8,
        (
            "为了平息如今的事态，\x01",
            "警备队的各位成员自不用说，\x01",
            "市长和议长也在拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "总之，我们这些职员现在\x01",
            "一定要相信他们，\x01",
            "尽力做好力所能及的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A8")

    Jump("loc_192F")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1349")

    #C0019
    ChrTalk(
        0x8,
        (
            "今天将在市民会馆举办\x01",
            "以『独立的利弊』为主题的\x01",
            "市民座谈会。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "我们已经按照计划，\x01",
            "预留出了若干空位，\x01",
            "有兴趣的市民请务必参加。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BE")

    label("loc_1349")


    #C0021
    ChrTalk(
        0x8,
        (
            "把交给您的那张卡片插入\x01",
            "导力梯内的控制面板，\x01",
            "就可以直达四十层了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "卡片在一个月内有效，\x01",
            "过期之后请随意处理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BE")

    Jump("loc_192F")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_152A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CA")

    #C0023
    ChrTalk(
        0x8,
        (
            "欢迎。\x01",
            "列车事故方面的咨询\x01",
            "由我来负责解答。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "由于西克洛斯贝尔街道\x01",
            "发生了列车事故，\x01",
            "铁道列车将暂时停运。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "另外，事故的原因正在调查之中，\x01",
            "现在还无法得知\x01",
            "何时可以恢复通车。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "着急去帝国和共和国的旅客\x01",
            "请前往巴士车站\x01",
            "或空港。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1525")

    label("loc_14CA")


    #C0027
    ChrTalk(
        0x8,
        (
            "着急去帝国和共和国的旅客\x01",
            "请前往巴士车站\x01",
            "或空港。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "假如有需要，\x01",
            "我们可以帮您购票。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1525")

    Jump("loc_192F")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1646")

    #C0029
    ChrTalk(
        0x8,
        (
            "为了推进与各国的文化交流，\x01",
            "克洛斯贝尔市正在商讨\x01",
            "各种各样的计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "比如克洛斯贝尔观光宣传展览、\x01",
            "外国文化历史学习展览、\x01",
            "贩卖各国特产的店铺等等……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "为了向各位市民\x01",
            "提供更有意义的服务，\x01",
            "我们全体职员一直在不断努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "敬请期待兰花塔\x01",
            "今后的发展。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16AD")

    label("loc_1646")


    #C0033
    ChrTalk(
        0x8,
        (
            "为了推进与各国的文化交流，\x01",
            "克洛斯贝尔市正在商讨\x01",
            "各种各样的计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "敬请期待兰花塔\x01",
            "今后的发展。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AD")

    Jump("loc_192F")

    label("loc_16B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1804")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1771")

    #C0035
    ChrTalk(
        0x8,
        "欢迎来到兰花塔。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "这里是总服务台，\x01",
            "我们接受各方面的咨询，\x01",
            "并为市民提供各种服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "从观光向导，到医疗、福利等\x01",
            "与市民生活相关的问题，\x01",
            "都可以在这里咨询。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17FF")

    label("loc_1771")


    #C0038
    ChrTalk(
        0x8,
        (
            "这里是总服务台，\x01",
            "我们接受各方面的咨询，\x01",
            "并为市民提供各种服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "从观光向导，到医疗、福利等\x01",
            "与市民生活相关的问题，\x01",
            "都可以在这里咨询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FF")

    Jump("loc_192F")

    label("loc_1804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_192F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C0")

    #C0040
    ChrTalk(
        0x8,
        (
            "各位，真是辛苦了。\x01",
            "这里是兰花塔的\x01",
            "总服务台。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "我们全体职员今天将\x01",
            "依照警备对策室的指示，\x01",
            "分别承担各种工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "如果发生了特殊情况，\x01",
            "我们就互相协助吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_192F")

    label("loc_18C0")


    #C0043
    ChrTalk(
        0x8,
        (
            "我们全体职员今天将\x01",
            "依照警备对策室的指示，\x01",
            "分别承担各种工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "如果发生了特殊情况，\x01",
            "我们就互相协助吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_192F")

    TalkEnd(0x8)
    Return()

    # Function_7_EC6 end

    def Function_8_1933(): pass

    label("Function_8_1933")

    Call(0, 9)
    Return()

    # Function_8_1933 end

    def Function_9_1937(): pass

    label("Function_9_1937")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E5")

    #C0045
    ChrTalk(
        0x9,
        (
            "在市内出现的怪物\x01",
            "好像已经全部消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "我被关在塔里的时候，\x01",
            "真是十分恐慌。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "虽然并没有受到什么伤害，\x01",
            "但真不想再经历\x01",
            "那样的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A4A")

    label("loc_19E5")


    #C0048
    ChrTalk(
        0x9,
        (
            "我被关在塔里的时候，\x01",
            "真是十分恐慌。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "虽然并没有受到什么伤害，\x01",
            "但真不想再经历\x01",
            "那样的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4A")

    Jump("loc_222E")

    label("loc_1A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A5D")
    Jump("loc_222E")

    label("loc_1A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A6B")
    Jump("loc_222E")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3E")

    #C0050
    ChrTalk(
        0x9,
        (
            "我在兰花塔遭到袭击，\x01",
            "去地下避难的时候，\x01",
            "看到了广场上的战况……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "武装集团那大军压境的\x01",
            "场面真是只能用恐怖\x01",
            "来形容啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "所幸这栋大楼\x01",
            "总算平安无事……\x01",
            "我当时还以为自己死定了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BB2")

    label("loc_1B3E")


    #C0053
    ChrTalk(
        0x9,
        (
            "武装集团那大军压境的\x01",
            "场面真是只能用恐怖\x01",
            "来形容啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "所幸这栋大楼\x01",
            "总算平安无事……\x01",
            "我当时还以为自己死定了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")

    Jump("loc_222E")

    label("loc_1BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1CEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C72")

    #C0055
    ChrTalk(
        0x9,
        (
            "乌尔斯拉医院\x01",
            "从昨晚一直\x01",
            "忙乱到了现在。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "伤者的数量实在太多，\x01",
            "救援人手和各种物资\x01",
            "远远不足……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "一想到在现场奋战的\x01",
            "各位如此辛苦，\x01",
            "真是由衷地感谢啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CE6")

    label("loc_1C72")


    #C0058
    ChrTalk(
        0x9,
        (
            "市内的人们也在倾尽全力\x01",
            "对医院提供各种各样的\x01",
            "支援……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "一想到在现场奋战的\x01",
            "各位如此辛苦，\x01",
            "真是由衷地感谢啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE6")

    Jump("loc_222E")

    label("loc_1CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D98")

    #C0060
    ChrTalk(
        0x9,
        (
            "由于列车事故的影响而\x01",
            "被迫滞留在自治州的旅客们，\x01",
            "今早基本都已经启程了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "虽然今后还要面对赔偿问题……\x01",
            "但这么快就能恢复通车，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DFB")

    label("loc_1D98")


    #C0062
    ChrTalk(
        0x9,
        (
            "虽然今后肯定\x01",
            "还要面对因列车事故\x01",
            "而产生的赔偿问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "但这么快就能恢复通车，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFB")

    Jump("loc_222E")

    label("loc_1E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E8B")

    #C0064
    ChrTalk(
        0x9,
        (
            "刚才接到了联络，\x01",
            "各位受伤的乘客\x01",
            "已经被安全送到医院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "总算可以暂时放心了……\x01",
            "不过，事故现场的状况还是很令人担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222E")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F75")

    #C0066
    ChrTalk(
        0x9,
        (
            "各位，\x01",
            "你们知道兰花塔这个名称\x01",
            "有什么含义吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "所谓『兰花』……\x01",
            "是一种一根茎上只开一朵花的\x01",
            "美丽花卉。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "也就是说，\x01",
            "这栋大楼就像是一朵\x01",
            "直耸天空的花朵。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "呵呵，这样一想，\x01",
            "还真是个贴切的名字啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FE5")

    label("loc_1F75")


    #C0070
    ChrTalk(
        0x9,
        (
            "所谓『兰花』……\x01",
            "是一种一根茎上只开一朵花的\x01",
            "美丽花卉。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "也就是说，\x01",
            "这栋大楼就像是一朵\x01",
            "直耸天空的花朵。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE5")

    Jump("loc_222E")

    label("loc_1FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2071")

    #C0072
    ChrTalk(
        0x9,
        (
            "欢迎光临，\x01",
            "这里是负责办理各种\x01",
            "行政手续的接待窗口。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "市民可以在此\x01",
            "缴纳公共费用，\x01",
            "以及申请变更住址。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20D9")

    label("loc_2071")


    #C0074
    ChrTalk(
        0x9,
        (
            "另外，本窗口受理的手续\x01",
            "基本都可以在市民会馆\x01",
            "办理。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "不方便来这里的\x01",
            "市民也可以去\x01",
            "市民会馆办理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D9")

    Jump("loc_222E")

    label("loc_20DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_222E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B8")

    #C0076
    ChrTalk(
        0x9,
        (
            "再过一个小时，\x01",
            "会议就要正式开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "在会议期间，我的工作主要就是\x01",
            "在这里传达市政职员们的\x01",
            "各种联络信息……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "怎么说呢，\x01",
            "一想到自己的工作与这么重要的活动相关，\x01",
            "就不由得紧张起来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_222E")

    label("loc_21B8")


    #C0079
    ChrTalk(
        0x9,
        (
            "离正式会议还有一个小时……\x01",
            "不久之后，\x01",
            "各国首脑就会莅临此地……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "呼，虽然我的工作\x01",
            "并不重要，\x01",
            "但还是很紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222E")

    TalkEnd(0x9)
    Return()

    # Function_9_1937 end

    def Function_10_2232(): pass

    label("Function_10_2232")

    Call(0, 11)
    Return()

    # Function_10_2232 end

    def Function_11_2236(): pass

    label("Function_11_2236")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EE")

    #C0081
    ChrTalk(
        0xA,
        (
            "被拘禁在兰花塔内的职员\x01",
            "和国防军士兵都已经获得释放了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "他们基本都在一片混乱的\x01",
            "职场进行善后工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "在这种时候，\x01",
            "我们就更要为了\x01",
            "市民努力工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2364")

    label("loc_22EE")


    #C0084
    ChrTalk(
        0xA,
        (
            "被拘禁在兰花塔内的\x01",
            "职员和国防军都在\x01",
            "一片混乱的职场进行善后工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "在这种时候，\x01",
            "我们就更要为了\x01",
            "市民努力工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2364")

    Jump("loc_2C15")

    label("loc_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2377")
    Jump("loc_2C15")

    label("loc_2377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2385")
    Jump("loc_2C15")

    label("loc_2385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2479")

    #C0086
    ChrTalk(
        0xA,
        (
            "亚里欧斯·马克莱因……\x01",
            "不愧是克洛斯贝尔的英雄啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        (
            "我亲眼看到他冲进武装集团的敌阵，\x01",
            "他当时的神勇表现\x01",
            "真是无法用语言来形容。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "这样想或许有些夸大，\x01",
            "但我真的觉得，只要有他在这里，\x01",
            "就算是两大国也不足为惧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2504")

    label("loc_2479")


    #C0089
    ChrTalk(
        0xA,
        (
            "亚里欧斯·马克莱因……\x01",
            "不愧是克洛斯贝尔的英雄啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "这样想或许有些夸大，\x01",
            "但我真的觉得，只要有他在这里，\x01",
            "就算是两大国也不足为惧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2504")

    Jump("loc_2C15")

    label("loc_2509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F7")

    #C0091
    ChrTalk(
        0xA,
        (
            "据传闻说，\x01",
            "警备队现在的状况不容乐观。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "如果损失进一步扩大，\x01",
            "就得考虑投入警队了……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "话虽如此，\x01",
            "但市内的防卫毕竟也不能忽略。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "现在各处都在竭尽全力，\x01",
            "但最好还是能设法\x01",
            "通过交涉及谈判来解决问题啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2689")

    label("loc_25F7")


    #C0095
    ChrTalk(
        0xA,
        (
            "现在各处都在竭尽全力，\x01",
            "但最好还是能设法\x01",
            "通过交涉及谈判来解决问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "虽然我们总务一科\x01",
            "很难做出直接贡献，\x01",
            "但仍然要尽全力处理好各种业务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2689")

    Jump("loc_2C15")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275A")

    #C0097
    ChrTalk(
        0xA,
        (
            "呼，铁道列车总算\x01",
            "在昨天恢复了通车，\x01",
            "让人松了一口气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "要是列车一直停运下去，\x01",
            "各方面对克洛斯贝尔提出的\x01",
            "各种赔偿肯定会升到天文数字。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "太感谢彻夜工作的\x01",
            "警备队员了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27CF")

    label("loc_275A")


    #C0100
    ChrTalk(
        0xA,
        (
            "要是列车一直停运下去，\x01",
            "各方面对克洛斯贝尔提出的\x01",
            "各种赔偿肯定会升到天文数字。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "太感谢彻夜工作的\x01",
            "警备队员了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CF")

    Jump("loc_2C15")

    label("loc_27D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_287E")

    #C0102
    ChrTalk(
        0xA,
        (
            "我们第一时间接到了\x01",
            "发生列车事故的\x01",
            "通知。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "来自各界的询问\x01",
            "也很快纷纷而来。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "我们随时可以为大家\x01",
            "安排替代导力铁路的\x01",
            "客运及货运手段。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28E7")

    label("loc_287E")


    #C0105
    ChrTalk(
        0xA,
        (
            "话说回来，列车事故\x01",
            "还真是极其少见。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔的铁道\x01",
            "是一条直线，视野也不错，\x01",
            "很难发生事故……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E7")

    Jump("loc_2C15")

    label("loc_28EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_299C")

    #C0107
    ChrTalk(
        0xA,
        (
            "在市政厅开放的时候，\x01",
            "许多市民为了参观而来，\x01",
            "整个大厅中人来人往。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "呵呵，第一次走进这栋建筑的人\x01",
            "全都被震撼得目瞪口呆，\x01",
            "看到他们那种表情，真是心情愉快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C15")

    label("loc_299C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A88")

    #C0109
    ChrTalk(
        0xA,
        (
            "啊，你们不是\x01",
            "负责通商会议警备的\x01",
            "特别任务支援科吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "嗯，机会难得，\x01",
            "就让我来说明一下吧，\x01",
            "这里是行政窗口。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "如需索取各种资料，\x01",
            "或询问相关政策，\x01",
            "都可以来此咨询。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "如果有什么需要，\x01",
            "随时可以吩咐。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2AE3")

    label("loc_2A88")


    #C0113
    ChrTalk(
        0xA,
        (
            "这里是办理\x01",
            "行政业务的窗口。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "如需索取各种资料，\x01",
            "或询问相关政策，\x01",
            "都可以来此咨询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE3")

    Jump("loc_2C15")

    label("loc_2AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_2C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B9D")

    #C0115
    ChrTalk(
        0xA,
        (
            "管理兰花塔是我们\x01",
            "总务一科的重要工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "比如准备今天的会场\x01",
            "及各间休息室等，\x01",
            "就是我们的任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "现在终于可以歇歇了……\x01",
            "直到刚才都忙得一塌糊涂。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C15")

    label("loc_2B9D")


    #C0118
    ChrTalk(
        0xA,
        (
            "呼，各项事务能赶在开会之前\x01",
            "安排完毕，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "虽然直到最后一刻都不可大意，\x01",
            "但接下来就只需等待会议开始了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C15")

    TalkEnd(0xA)
    Return()

    # Function_11_2236 end

    def Function_12_2C19(): pass

    label("Function_12_2C19")

    Call(0, 13)
    Return()

    # Function_12_2C19 end

    def Function_13_2C1D(): pass

    label("Function_13_2C1D")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CCF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "换钱\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C7A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C9A")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CCA")

    label("loc_2C9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAE")
    Jump("loc_2CCA")

    label("loc_2CAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CCA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_2CCA")

    Jump("loc_2C2A")

    label("loc_2CCF")

    TalkEnd(0xD)
    Return()

    # Function_13_2C1D end

    def Function_14_2CD3(): pass

    label("Function_14_2CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D95")

    #C0120
    ChrTalk(
        0xD,
        (
            "ＩＢＣ业务已经基本停止……\x01",
            "半数职员都在\x01",
            "家里听候通知。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "身为在银行工作多年的员工，\x01",
            "迪塔先生被拘捕一事\x01",
            "让我受了很大的打击……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "但我们必须要\x01",
            "坚强地撑下去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_2DF2")

    label("loc_2D95")


    #C0123
    ChrTalk(
        0xD,
        (
            "ＩＢＣ业务已经基本停止，\x01",
            "但耀晶片换钱业务\x01",
            "还在继续办理。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "如果有需要，\x01",
            "请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF2")

    Jump("loc_2F9E")

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F31")

    #C0125
    ChrTalk(
        0x102,
        (
            "#00100F辛苦了，兰菲小姐。\x02\x03",

            "业务窗口的转移工作已经\x01",
            "差不多了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xD,
        "哎呀呀，这不是艾莉小姐嘛。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "是的，这多亏玛丽亚贝尔\x01",
            "代理总裁的过人能力和\x01",
            "技术部那些优秀职员的努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "半数以上的职员\x01",
            "都已在这栋建筑里\x01",
            "重新展开日常业务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xD,
        (
            "如果各位有什么需要，\x01",
            "请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        "#00102F嗯，多谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_2F9E")

    label("loc_2F31")


    #C0131
    ChrTalk(
        0xD,
        (
            "ＩＢＣ现在正在\x01",
            "兰花塔营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xD,
        (
            "耀晶片换钱业务\x01",
            "仍然在照常受理。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "如果各位有什么需要，\x01",
            "请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9E")

    Return()

    # Function_14_2CD3 end

    def Function_15_2F9F(): pass

    label("Function_15_2F9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3044")

    #C0134
    ChrTalk(
        0xFE,
        (
            "大家似乎已经陆续和分别多时的\x01",
            "亲友们重逢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "现在的事态实在是很严峻……\x01",
            "在这种时候，果然还是要和\x01",
            "重要的亲友们在一起才安心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_30B0")

    label("loc_3044")


    #C0136
    ChrTalk(
        0xFE,
        (
            "说起来，那辆坏掉的\x01",
            "导力车刚才被运出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "工作人员在搬运时都很小心，\x01",
            "你们日后一定要更加珍惜它哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B0")

    Jump("loc_3A99")

    label("loc_30B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_30C3")
    Jump("loc_3A99")

    label("loc_30C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30D1")
    Jump("loc_3A99")

    label("loc_30D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31DF")

    #C0138
    ChrTalk(
        0xFE,
        (
            "多亏亚里欧斯先生的神勇表现，\x01",
            "兰花塔才\x01",
            "幸免于难……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "但ＩＢＣ大楼……\x01",
            "已经完全化为一片废墟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "虽然普通民众\x01",
            "基本没有受到伤害……\x01",
            "但彩虹剧团却被……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "不知道他们的目的是不是为了示威，\x01",
            "无论出于什么理由，这种行为\x01",
            "都是不可饶恕的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_326B")

    label("loc_31DF")


    #C0142
    ChrTalk(
        0xFE,
        (
            "虽然普通民众\x01",
            "基本没有受到伤害……\x01",
            "但彩虹剧团却被……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "不知道他们的目的是不是为了示威，\x01",
            "无论出于什么理由，这种行为\x01",
            "都是不可饶恕的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326B")

    Jump("loc_3A99")

    label("loc_3270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_32FA")

    #C0144
    ChrTalk(
        0xFE,
        (
            "市长和议长从昨晚开始\x01",
            "就一直忙于应对\x01",
            "占领事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "在现在这种状况下，\x01",
            "我们能做的也只有绷紧精神，\x01",
            "准备应对意外情况了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A99")

    label("loc_32FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D4")

    #C0146
    ChrTalk(
        0xFE,
        (
            "据说造成昨天那起列车事故的\x01",
            "怪物并不是幻兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "但最近常常出现的幻兽\x01",
            "还是很令人在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "听说还在它们的\x01",
            "附近发现了来历\x01",
            "不明的蓝花……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "这该不会是……\x01",
            "即将发生更大异变的预兆吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3444")

    label("loc_33D4")


    #C0150
    ChrTalk(
        0xFE,
        (
            "既然具体原因不明，\x01",
            "那幻兽在市区内出现\x01",
            "也不是没有可能吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "真是令人毛骨悚然……\x01",
            "总之，\x01",
            "不能放松警戒啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3444")

    Jump("loc_3A99")

    label("loc_3449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34A4")

    #C0152
    ChrTalk(
        0xFE,
        "导力列车脱轨事故吗……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "听说还在调查原因，\x01",
            "该不会是恐怖活动吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A99")

    label("loc_34A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35CD")

    #C0154
    ChrTalk(
        0xFE,
        (
            "虽然我是警察，\x01",
            "但在这里可以享受到\x01",
            "与市政职员相同的待遇。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "也就是说，这栋大楼内的\x01",
            "职工专用咖啡厅、食堂等设施，\x01",
            "我都可以自由使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "虽然这些设施只是位于兰花塔的中部，\x01",
            "但仍旧比ＩＢＣ的顶楼\x01",
            "高出很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "总之，景色真是棒极了，\x01",
            "但总觉得有些\x01",
            "对不住各位市民。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_364F")

    label("loc_35CD")


    #C0158
    ChrTalk(
        0xFE,
        (
            "话说回来，已经有人\x01",
            "提出尽早向市民开放\x01",
            "咖啡厅的意见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "不知要过多久才能实施，\x01",
            "到时候，咖啡厅一定会\x01",
            "成为很受欢迎的场所。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364F")

    Jump("loc_3A99")

    label("loc_3654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_377D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370D")

    #C0160
    ChrTalk(
        0xFE,
        (
            "啊，这不是特别任务支援科吗。\x01",
            "欢迎来到兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "如果有什么事情，\x01",
            "请到正面服务台咨询。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "外来人员入内之后，\x01",
            "要先到那里说明情况，\x01",
            "否则什么都做不了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3778")

    label("loc_370D")


    #C0163
    ChrTalk(
        0xFE,
        (
            "如果有什么事情，\x01",
            "请到正面服务台咨询。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "外来人员入内之后，\x01",
            "要先到那里说明情况，\x01",
            "否则什么都做不了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3778")

    Jump("loc_3A99")

    label("loc_377D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_3A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4B")

    #C0165
    ChrTalk(
        0xFE,
        (
            "迪塔市长竟然亲自\x01",
            "引领你们去会场，\x01",
            "真不愧是特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "市长欣赏你们的传言\x01",
            "果然是真的。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#00005F那个……该怎么说呢……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "啊，我绝对没有\x01",
            "嫉妒你们的意思，\x01",
            "请不要在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "话说回来，我个人\x01",
            "其实是很支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "虽然职责不同，\x01",
            "但能和你们一起工作，\x01",
            "我感到很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        "#00105F谢、谢谢。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#00202F……该怎么说呢，和半年前相比，\x01",
            "我们的境遇真是天差地别啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#00302F说起来，在一开始，\x01",
            "我们经常遭受『冒牌游击士』、\x01",
            "『耍猴子戏』等讽刺啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x109,
        "#10105F是、是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，在警察局内部\x01",
            "也受到排挤呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "哈哈，以前确实有人\x01",
            "那样说过。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "但现在已经\x01",
            "不会再有那种说法了，\x01",
            "你们尽管放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "这个话题就到此为止，\x01",
            "我们今天一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#00000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 0)
    Jump("loc_3A99")

    label("loc_3A4B")


    #C0180
    ChrTalk(
        0xFE,
        (
            "虽然职责不同，\x01",
            "但能和你们一起工作，\x01",
            "我感到很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "今天一起加油吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3A99")

    TalkEnd(0xFE)
    Return()

    # Function_15_2F9F end

    def Function_16_3A9D(): pass

    label("Function_16_3A9D")

    TalkBegin(0xFE)

    #C0182
    ChrTalk(
        0xFE,
        (
            "唉，一下雨，想放松的时候\x01",
            "都不能去外边呼吸新鲜空气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "不过，这个大厅也是个\x01",
            "不错的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "最让人满意的是这个超高的天花板，\x01",
            "这种开阔感真是太棒了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_3A9D end

    def Function_17_3B43(): pass

    label("Function_17_3B43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BBA")

    #C0185
    ChrTalk(
        0xFE,
        (
            "１２:００——\x01",
            "目前并无异常。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "还没有发现\x01",
            "恐怖分子的踪迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "他们到底想从\x01",
            "哪里潜入呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3BFA")

    label("loc_3BBA")


    #C0188
    ChrTalk(
        0xFE,
        (
            "还没有发现\x01",
            "恐怖分子的踪迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "他们到底想从\x01",
            "哪里潜入呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFA")

    TalkEnd(0xFE)
    Return()

    # Function_17_3B43 end

    def Function_18_3BFE(): pass

    label("Function_18_3BFE")

    TalkBegin(0xFE)

    #C0190
    ChrTalk(
        0xFE,
        (
            "唔，那么……\x01",
            "从那个时间开始\x01",
            "就禁止进入ＶＩＰ室了？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3BFE end

    def Function_19_3C3D(): pass

    label("Function_19_3C3D")

    TalkBegin(0xFE)

    #C0191
    ChrTalk(
        0xFE,
        (
            "嗯，是的。\x01",
            "事前准备自然是\x01",
            "越早越好。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3C3D end

    def Function_20_3C6E(): pass

    label("Function_20_3C6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C83")
    Call(0, 29)
    Jump("loc_3CB6")

    label("loc_3C83")


    #C0192
    ChrTalk(
        0xFE,
        (
            "你、你们……\x01",
            "喂，一边去！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "我现在忙着呢！\x02",
    )

    CloseMessageWindow()

    label("loc_3CB6")

    TalkEnd(0xFE)
    Return()

    # Function_20_3C6E end

    def Function_21_3CBA(): pass

    label("Function_21_3CBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CCF")
    Call(0, 31)
    Jump("loc_3D2D")

    label("loc_3CCF")


    #C0194
    ChrTalk(
        0xFE,
        (
            "既然罗伯兹主任来了，\x01",
            "导力网络方面的麻烦\x01",
            "肯定就不成问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "呵呵，就让我大干一场吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3D2D")

    TalkEnd(0xFE)
    Return()

    # Function_21_3CBA end

    def Function_22_3D31(): pass

    label("Function_22_3D31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DCD")

    #C0196
    ChrTalk(
        0xFE,
        (
            "刚才有个小女孩\x01",
            "坐上了通向塔顶的\x01",
            "导力梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "那孩子好像是\x01",
            "国防长官的女儿……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "看来她很担心出现在\x01",
            "湿地的『大树』啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3E2A")

    label("loc_3DCD")


    #C0199
    ChrTalk(
        0xFE,
        (
            "国防长官的女儿刚才\x01",
            "坐上了通向塔顶的\x01",
            "导力梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "看来她很担心出现在\x01",
            "湿地的『大树』啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E2A")

    Jump("loc_40EC")

    label("loc_3E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E3D")
    Jump("loc_40EC")

    label("loc_3E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E4B")
    Jump("loc_40EC")

    label("loc_3E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3EA2")

    #C0201
    ChrTalk(
        0xFE,
        (
            "『赤色星座』的背后\x01",
            "肯定有帝国政府在操纵……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        "唔，真是不可饶恕。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_3EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3EE1")

    #C0203
    ChrTalk(
        0xFE,
        (
            "『赤色星座』……\x01",
            "果然是个非同寻常的组织啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_3EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_END)), "loc_3F34")

    #C0204
    ChrTalk(
        0xFE,
        "各位，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "如果要去上面的楼层，\x01",
            "请使用入口前的导力梯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_3F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F85")

    #C0206
    ChrTalk(
        0xFE,
        "唔，今天下雨了呀。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "不过，导力网络上说，\x01",
            "下午就能放晴了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_3F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4008")

    #C0208
    ChrTalk(
        0xFE,
        (
            "唔，克洛斯贝尔竟然发生了\x01",
            "列车事故，真是少见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "列车会脱轨，说明\x01",
            "承受了相当的冲击……\x01",
            "到底发生什么事了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_4008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4070")

    #C0210
    ChrTalk(
        0xFE,
        (
            "说起兰花塔，\x01",
            "最棒的就是这开阔的空间。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "哎呀呀，我真是觉得\x01",
            "这栋建筑造得太奢华了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_4070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40E3")

    #C0212
    ChrTalk(
        0xFE,
        (
            "据说兰花塔的\x01",
            "导力梯是目前整个\x01",
            "大陆中最快的。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "大概是因为基本不会摇晃，\x01",
            "倒也没什么实际感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EC")

    label("loc_40E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_40EC")

    label("loc_40EC")

    TalkEnd(0xFE)
    Return()

    # Function_22_3D31 end

    def Function_23_40F0(): pass

    label("Function_23_40F0")

    TalkBegin(0xFE)

    #C0214
    ChrTalk(
        0xFE,
        (
            "呼，真惊人……\x01",
            "这就是兰花塔的\x01",
            "大厅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "感觉自己就像变成了\x01",
            "科幻小说中的未来人。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_40F0 end

    def Function_24_4150(): pass

    label("Function_24_4150")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41A5")

    #C0216
    ChrTalk(
        0xFE,
        (
            "听这里的职员说，\x01",
            "列车发生了\x01",
            "脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "到底是什么原因呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_41F3")

    label("loc_41A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41F3")

    #C0218
    ChrTalk(
        0xFE,
        (
            "我还是第一次来兰花塔，\x01",
            "这大厅可真壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "确实是与众不同。\x02",
    )

    CloseMessageWindow()

    label("loc_41F3")

    TalkEnd(0xFE)
    Return()

    # Function_24_4150 end

    def Function_25_41F7(): pass

    label("Function_25_41F7")

    TalkBegin(0xFE)

    #C0220
    ChrTalk(
        0xFE,
        (
            "这么帅气又高科技的大楼\x01",
            "竟然是市政厅，\x01",
            "真是令人陶醉。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "虽然独立提案引起了一定程度的骚乱，\x01",
            "但我以后还真想搬到克洛斯贝尔定居。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_41F7 end

    def Function_26_4283(): pass

    label("Function_26_4283")

    TalkBegin(0xFE)

    #C0222
    ChrTalk(
        0xFE,
        (
            "唔，受玛因兹事件的影响，\x01",
            "市政厅也有点嘈杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "还是赶快办完事情，\x01",
            "早点回去吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_4283 end

    def Function_27_42E2(): pass

    label("Function_27_42E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4477")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43DA")

    #C0224
    ChrTalk(
        0xFE,
        (
            "前总裁迪塔先生\x01",
            "和曾担任代理总裁的大小姐\x01",
            "如今都已经不在ＩＢＣ了。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "这对今后的股价肯定也会产生巨大影响吧……\x01",
            "但ＩＢＣ毕竟拥有大陆最雄厚的资本，地位仍然难以撼动。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "在下任总裁确定人选之前，\x01",
            "我暂时观望一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4472")

    label("loc_43DA")


    #C0227
    ChrTalk(
        0xFE,
        (
            "人事变动肯定会对今后的股价产生巨大影响吧……\x01",
            "但ＩＢＣ毕竟拥有大陆最雄厚的资本，地位仍然难以撼动。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "在下任总裁确定人选之前，\x01",
            "我暂时观望一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4472")

    Jump("loc_452F")

    label("loc_4477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4485")
    Jump("loc_452F")

    label("loc_4485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_452F")

    #C0229
    ChrTalk(
        0xFE,
        (
            "竟然提前将\x01",
            "顾客的数据\x01",
            "备份到了兰花塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "不愧是ＩＢＣ……\x01",
            "处理危机的能力实在是厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "作为多年以来一直支撑着\x01",
            "大陆经济的支柱，\x01",
            "果然不是浪得虚名。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_452F")

    TalkEnd(0xFE)
    Return()

    # Function_27_42E2 end

    def Function_28_4533(): pass

    label("Function_28_4533")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4548")
    Call(0, 29)
    Jump("loc_45CB")

    label("loc_4548")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0232
    ChrTalk(
        0x11,
        (
            "……作为害我担心的惩罚，\x01",
            "下个月的零用钱就减半吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x12)

    #C0233
    ChrTalk(
        0x12,
        "千、千万不要啊！饶了我吧……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)

    label("loc_45CB")

    TalkEnd(0xFE)
    Return()

    # Function_28_4533 end

    def Function_29_45CF(): pass

    label("Function_29_45CF")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0234
    ChrTalk(
        0x11,
        (
            "真是的，你这个人\x01",
            "总是让别人担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x12,
        "可、可是……玛格丽特……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x12,
        (
            "我身为警局的副局长，\x01",
            "在有些时候必须要\x01",
            "站出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x11,
        (
            "你平时\x01",
            "就该这么干。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x11,
        (
            "都是因为你突然做这种反常的事，\x01",
            "才会被卷进麻烦里。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x12,
        "……对、对不起。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46EB")

    #C0240
    ChrTalk(
        0x101,
        "#00012F（啊，还是那么严厉呀……）\x02",
    )

    CloseMessageWindow()

    label("loc_46EB")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_29_45CF end

    def Function_30_46FC(): pass

    label("Function_30_46FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4711")
    Call(0, 31)
    Jump("loc_474E")

    label("loc_4711")


    #C0241
    ChrTalk(
        0xFE,
        (
            "还是和搭档一起工作\x01",
            "让人心情舒畅。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "我们赶快开始吧。\x02",
    )

    CloseMessageWindow()

    label("loc_474E")

    TalkEnd(0xFE)
    Return()

    # Function_30_46FC end

    def Function_31_4752(): pass

    label("Function_31_4752")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0243
    ChrTalk(
        0x10,
        (
            "那么，赶快开始对导力网络\x01",
            "进行检查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x10,
        (
            "怪物四处徘徊时的那股蓝色雾气\x01",
            "使通讯信号很不稳定，\x01",
            "说不定对系统也产生了影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xF,
        (
            "那就从兰花塔的终端\x01",
            "开始测试运转机能吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_31_4752 end

    def Function_32_4822(): pass

    label("Function_32_4822")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7E")
    TurnDirection(0xFE, 0x103, 0)

    #C0247
    ChrTalk(
        0xFE,
        (
            "缇欧……\x01",
            "听说你要去那棵『大树』？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "万一缇欧出了什么事……\x01",
            "光是想象一下，我的心就要碎了。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        "#00206F……主任，你担心过度了。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "……啊，对了！\x01",
            "我也带上魔导杖，\x01",
            "跟你们一起去如何！？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "我很了解魔导杖的构造，\x01",
            "说不定能在战斗中用辅助战技\x01",
            "来援护缇欧呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "嗯嗯，这主意不错！\x01",
            "既然决定了，就赶紧准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        "#00211F太烦人了，并不需要。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49C0")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_49C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49E6")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_49E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A0C")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4A0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A32")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4A32")

    Sleep(1000)

    #C0254
    ChrTalk(
        0x101,
        "#00012F（……还是老样子。）\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#00204F……主任，请不要\x01",
            "过分担心。\x02\x03",

            "#00202F我和大家一定会带琪雅\x01",
            "一起平安归来的。\x02\x03",

            "而且市内还处于混乱状态，\x01",
            "处理这里的问题才是主任的职责吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        "缇、缇欧……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "……你说的对。\x01",
            "既然缇欧都这么说了……\x01",
            "我就集中精神，在这里认真工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "但请答应我一个条件，\x01",
            "一定要平安无事地回来！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 3)
    Jump("loc_4DD9")

    label("loc_4B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D47")

    #C0259
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "听说『结社』的那个博士\x01",
            "和白色的智能兵器一起消失了？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#00206F嗯……老实说，\x01",
            "我再也不想接触到他了。\x02\x03",

            "#00211F和那种人相比，\x01",
            "主任要强上一千倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "缇、缇欧！（感动……）\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00012F（和那种人相提并论，\x01",
            "  难道还值得高兴吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        "话说回来，『神机』……\x02",
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
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        "啊哈哈，没什么。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "（和我们正在开发的\x01",
            "  『永世系统』……）\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "（……应该只是巧合吧？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4DD9")

    label("loc_4D47")


    #C0269
    ChrTalk(
        0xFE,
        (
            "我就在这里\x01",
            "等大家回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "虽然很想跟大家一起去……\x01",
            "但是既然被缇欧拒绝，\x01",
            "也就没有办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "但请答应我一个条件，\x01",
            "一定要平安无事地回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD9")

    Jump("loc_4FCF")

    label("loc_4DDE")

    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F60")

    #C0272
    ChrTalk(
        0xFE,
        (
            "唉，要是能了解到\x01",
            "湿地的详细状况\x01",
            "就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "……啊，突然又开始\x01",
            "担心起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "竟然要把缇欧送到那种\x01",
            "不知底细的地方……！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#00203F这是为了平安带回\x01",
            "两位游击士。\x02\x03",

            "主任，不用太担心，\x01",
            "你就在这里等着我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "缇欧……\x01",
            "你真的长大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "刚来财团的时候，\x01",
            "你才那么小……\x01",
            "呜，我都快哭出来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x103,
        (
            "#00211F……那会很烦的，\x01",
            "请不要在这种\x01",
            "地方哭出来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4FCF")

    label("loc_4F60")


    #C0279
    ChrTalk(
        0xFE,
        (
            "竟然要把缇欧送到那种\x01",
            "不知底细的地方……！\x01",
            "我真是担心得要死……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "但缇欧已经长大了，\x01",
            "一定不会有事的！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FCF")

    TalkEnd(0xFE)
    Return()

    # Function_32_4822 end

    def Function_33_4FD3(): pass

    label("Function_33_4FD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E5")

    #C0281
    ChrTalk(
        0x22,
        (
            "#02302F对了……\x01",
            "听说你们有『波波碰！』\x01",
            "的账号？\x02\x03",

            "#02304F哼哼，机会难得，\x01",
            "就把我约纳大人的账号当作礼物告诉你们吧。\x02\x03",

            "#02302F我可是从研发阶段就开始玩这个游戏了，\x01",
            "要是自以为能战胜我，就尽管试试看吧～\x02",
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
            "『约纳的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_52D7")

    label("loc_50E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528B")

    #C0283
    ChrTalk(
        0x22,
        (
            "#02306F冒雨赶过来，\x01",
            "真是累人啊。\x02\x03",

            "#02300F回财团分部之前，\x01",
            "一定要好好偷偷懒～\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00005F喂喂……\x01",
            "你是坐导力梯上的塔顶，\x01",
            "并没有什么剧烈运动吧？\x02\x03",

            "#00001F太缺乏运动可不好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x103,
        (
            "#00203F没办法，约纳有\x01",
            "豆芽菜儿童综合症嘛。\x02",
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
            "#02310F什、什么啊，\x01",
            "那是什么莫名其妙的综合症……\x02\x03",

            "#02306F哼，真是的……\x01",
            "要去湿地的话，\x01",
            "就赶紧去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00000F嗯，我们这就出发，\x01",
            "多谢你帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_52D7")

    label("loc_528B")


    #C0288
    ChrTalk(
        0x22,
        (
            "#02303F我要偷够懒之后\x01",
            "再回去。\x02\x03",

            "#02301F你们要去湿地的话，\x01",
            "就赶紧去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D7")

    TalkEnd(0xFE)
    Return()

    # Function_33_4FD3 end

    def Function_34_52DB(): pass

    label("Function_34_52DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F3")

    #C0289
    ChrTalk(
        0x20,
        (
            "#02100F哦，是你们啊，\x01",
            "看来还是和平时一样忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#00100F格蕾丝小姐，你们是为\x01",
            "议会而来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x20,
        (
            "#02109F没错，我们要报道最近\x01",
            "刚刚通过的法案～\x02\x03",

            "顺带还打算\x01",
            "采访各位议员，\x01",
            "询问他们对独立的看法。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#00200F原来如此，最近的新闻重点是\x01",
            "社会时事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x20,
        (
            "#02106F是啊～\x02\x03",

            "政界方面最近\x01",
            "少有丑闻，\x01",
            "感觉有些无聊……\x02\x03",

            "#02102F唔～就没有什么\x01",
            "有意思的八卦消息\x01",
            "流传吗？\x02",
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
        "#00006F您只关心这些吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 7)
    Jump("loc_55FC")

    label("loc_54F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5574")

    #C0296
    ChrTalk(
        0x20,
        (
            "#02106F虽然丑闻少\x01",
            "是件好事，但最近\x01",
            "没什么好的八卦消息啊～\x02\x03",

            "#02102F唔～就没有什么\x01",
            "有意思的八卦消息流传吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_55DF")

    label("loc_5574")


    #C0297
    ChrTalk(
        0x20,
        (
            "#02100F哦，对了，\x01",
            "如果『美食向导』的任务完成了，\x01",
            "就去杂志社的前台叫我吧。\x02\x03",

            "#02109F拜托你们了哦～¤\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 5)

    label("loc_55DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_55FC")
    ClearScenarioFlags(0x0, 5)

    label("loc_55FC")

    TalkEnd(0xFE)
    Return()

    # Function_34_52DB end

    def Function_35_5600(): pass

    label("Function_35_5600")

    TalkBegin(0xFE)

    #C0298
    ChrTalk(
        0xFE,
        (
            "……但愿格蕾丝前辈不要\x01",
            "向议员们提出奇怪的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "呼，负责看着她可是份苦差事啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_5600 end

    def Function_36_5660(): pass

    label("Function_36_5660")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_566D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5832")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56FC")

    #C0300
    ChrTalk(
        0x13,
        (
            "#10100F要编队吗？\x01",
            "明白了！\x02",
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
    Jump("loc_582D")

    label("loc_56FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5710")
    Jump("loc_582D")

    label("loc_5710")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_582D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57DD")

    #C0301
    ChrTalk(
        0x13,
        (
            "#10100F虽然损毁严重……\x01",
            "但车内的各种功能还可以使用。\x02\x03",

            "等到把事态平息之后，\x01",
            "我们一定要修好它。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x103,
        (
            "#00204F嗯……\x01",
            "到时去找罗伯兹主任和\x01",
            "基约姆师傅他们帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_582D")

    label("loc_57DD")


    #C0303
    ChrTalk(
        0x13,
        (
            "#10100F车内的各种功能还可以使用。\x02\x03",

            "等到把事态平息之后，\x01",
            "我们一定要修好它。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582D")

    Jump("loc_566D")

    label("loc_5832")

    TalkEnd(0xFE)
    Return()

    # Function_36_5660 end

    def Function_37_5836(): pass

    label("Function_37_5836")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5843")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A89")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D1")

    #C0304
    ChrTalk(
        0x14,
        "#10400F呵呵，要换班了吗？\x02",
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
    Jump("loc_5A84")

    label("loc_58D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58E5")
    Jump("loc_5A84")

    label("loc_58E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A84")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F4")

    #C0305
    ChrTalk(
        0x14,
        (
            "#10406F不管消灭多少，\x01",
            "都会有无数新敌人涌来……\x02\x03",

            "哎呀呀，对方用上了\x01",
            "很棘手的东西呢。\x02\x03",

            "#10401F如果再这样下去，外面的人\x01",
            "恐怕只能徒增消耗……\x01",
            "还是尽快行动为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#00101F嗯，必须赶快找到迪塔叔叔，\x01",
            "让他立刻停止这种愚行……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_5A84")

    label("loc_59F4")


    #C0307
    ChrTalk(
        0x14,
        (
            "#10406F不管消灭多少，\x01",
            "都会有无数新敌人涌来……\x01",
            "哎呀呀，真麻烦呢。\x02\x03",

            "#10401F如果再这样下去，外面的人\x01",
            "恐怕只能徒增消耗……\x01",
            "还是尽快行动为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A84")

    Jump("loc_5843")

    label("loc_5A89")

    TalkEnd(0xFE)
    Return()

    # Function_37_5836 end

    def Function_38_5A8D(): pass

    label("Function_38_5A8D")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C5C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B2A")

    #C0308
    ChrTalk(
        0x15,
        "#10702F要交替成员吗？好的。\x02",
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
    Jump("loc_5C57")

    label("loc_5B2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B3E")
    Jump("loc_5C57")

    label("loc_5B3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C57")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C09")

    #C0309
    ChrTalk(
        0x15,
        (
            "#10703F这个大厅里暂时\x01",
            "还没有敌人的气息……\x02\x03",

            "但最好不要\x01",
            "放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#00300F嗯，不怕一万，就怕万一……\x01",
            "这里就拜托你了，莉夏。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x15,
        "#10702F嗯，交给我吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5C57")

    label("loc_5C09")


    #C0312
    ChrTalk(
        0x15,
        (
            "#10703F谨慎起见，\x01",
            "必须要时刻注意\x01",
            "周围的情况。\x02\x03",

            "#10701F各位也请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C57")

    Jump("loc_5A9A")

    label("loc_5C5C")

    TalkEnd(0xFE)
    Return()

    # Function_38_5A8D end

    def Function_39_5C60(): pass

    label("Function_39_5C60")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E16")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0C")

    #C0313
    ChrTalk(
        0x16,
        (
            "#00600F要编组队伍吗？\x01",
            "……那就赶快决定吧。\x02",
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
    Jump("loc_5E11")

    label("loc_5D0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D20")
    Jump("loc_5E11")

    label("loc_5D20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E11")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DDB")

    #C0314
    ChrTalk(
        0x16,
        (
            "#00603F按照事先商定的计划，\x01",
            "留下两个人看守入口，\x01",
            "以便应对特殊状况。\x02\x03",

            "#00601F……好了，不要慢吞吞的。\x01",
            "你们赶快行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        "#00001F……是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_5E11")

    label("loc_5DDB")


    #C0316
    ChrTalk(
        0x16,
        (
            "#00601F……好了，不要慢吞吞的。\x01",
            "你们赶快行动吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E11")

    Jump("loc_5C6D")

    label("loc_5E16")

    TalkEnd(0xFE)
    Return()

    # Function_39_5C60 end

    def Function_40_5E1A(): pass

    label("Function_40_5E1A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E5F")

    #A0317
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯停在了\x01",
            "其它楼层，\x01",
            "暂时无法使用。\x07\x00\x02",
        )
    )

    Jump("loc_5ECC")

    label("loc_5E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E94")

    #A0318
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯前的卷帘门\x01",
            "紧闭着。\x07\x00\x02",
        )
    )

    Jump("loc_5ECC")

    label("loc_5E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5ECC")

    #A0319
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯停在了\x01",
            "其它楼层，\x01",
            "暂时无法使用。\x07\x00\x02",
        )
    )


    label("loc_5ECC")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_5E1A end

    def Function_41_5ED4(): pass

    label("Function_41_5ED4")

    Sound(160, 0, 100, 0)
    Return()

    # Function_41_5ED4 end

    def Function_42_5EDB(): pass

    label("Function_42_5EDB")

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

    def lambda_60BA():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_60BA)
    Sleep(200)

    def lambda_60D7():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_60D7)
    Sleep(200)

    def lambda_60F4():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_60F4)
    Sleep(200)

    def lambda_6111():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6111)
    Sleep(200)

    def lambda_612E():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_612E)
    Sleep(200)

    def lambda_614B():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_614B)
    Sleep(100)

    def lambda_6168():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6168)
    Sleep(300)

    def lambda_617C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_617C)
    Sleep(200)

    def lambda_6190():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6190)
    Sleep(600)

    def lambda_61A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_61A4)
    Sleep(200)

    def lambda_61B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_61B8)
    Sleep(300)

    def lambda_61CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_61CC)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0320
    ChrTalk(
        0x101,
        "#00002F#11P好惊人……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#00302F#11P该怎么形容呢，感觉又豪华\x01",
            "又充满高科技感……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x109,
        (
            "#10109F#5P未来世界的感觉比ＩＢＣ\x01",
            "更加强烈呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        (
            "#00203F#11P听说所有楼层\x01",
            "都接通了导力网络。\x02\x03",

            "#00200F因为同时与ＩＢＣ相连，\x01",
            "所以随时都可以查询\x01",
            "股票指数之类的数据。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#00104F#5P嗯，这些好像都是\x01",
            "迪塔叔叔的主意。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x105,
        (
            "#10302F#11P原来如此，这种创意\x01",
            "很符合银行家的风格啊。\x02",
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
            "#00000F#5P好，在达德利警官\x01",
            "到来之前，\x01",
            "我们就在这里等吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63CE():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_63CE)
    Sleep(50)

    def lambda_63DE():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_63DE)
    Sleep(50)

    def lambda_63EE():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_63EE)
    Sleep(50)

    def lambda_63FE():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63FE)
    Sleep(50)

    def lambda_640E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_640E)
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
            "#6P#00102F今天没有普通访客，\x01",
            "我们可以坐在那边的\x01",
            "沙发上等候。\x02",
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
            "#1K当日１２：００──\x02",
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
        "男人的声音",
        "#3454V#30W#11A你们到了啊。\x02",
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

    def lambda_664F():

        label("loc_664F")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_664F")

    QueueWorkItem2(0x101, 2, lambda_664F)
    Sleep(50)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 5000, 0, 6500, 270)

    def lambda_6688():

        label("loc_6688")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6688")

    QueueWorkItem2(0x102, 2, lambda_6688)
    Sleep(50)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 5000, 0, 7600, 270)

    def lambda_66BB():

        label("loc_66BB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_66BB")

    QueueWorkItem2(0x103, 2, lambda_66BB)
    Sleep(50)

    def lambda_66D0():

        label("loc_66D0")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_66D0")

    QueueWorkItem2(0x104, 2, lambda_66D0)
    Sleep(50)

    def lambda_66E5():

        label("loc_66E5")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_66E5")

    QueueWorkItem2(0x105, 2, lambda_66E5)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 5000, 0, 8700, 270)

    def lambda_6715():
        OP_95(0xFE, 4500, 0, 8700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6715)
    WaitChrThread(0x109, 1)

    def lambda_6733():

        label("loc_6733")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6733")

    QueueWorkItem2(0x109, 2, lambda_6733)
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
        "#00000F#5P达德利警官。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        "#11P#00104F您辛苦了。\x02",
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
            "现在是正午时分……\x02\x03",

            "通商会议的开始时间\x01",
            "是１３：００。\x02\x03",

            "再过三十分钟左右，\x01",
            "各国首脑应该就会来了。\x02",
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
        "#00001F#5P这样啊……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#11P#00101F那么，我们接下来\x01",
            "要去哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x16,
        (
            "#12P#00606F其实我本打算\x01",
            "带你们在会场附近转转……\x02\x03",

            "但有位意想不到的人\x01",
            "主动提出要带你们参观。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        "#00005F#5P意想不到的人……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)

    #N0337
    NpcTalk(
        0x23,
        "男人的声音",
        (
            "哟，各位，\x01",
            "你们来了啊。\x02",
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

    def lambda_6A5D():
        OP_95(0xFE, 7800, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6A5D)

    def lambda_6A77():

        label("loc_6A77")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_6A77")

    QueueWorkItem2(0x101, 2, lambda_6A77)

    def lambda_6A89():

        label("loc_6A89")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_6A89")

    QueueWorkItem2(0x102, 2, lambda_6A89)

    def lambda_6A9B():

        label("loc_6A9B")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_6A9B")

    QueueWorkItem2(0x103, 2, lambda_6A9B)

    def lambda_6AAD():

        label("loc_6AAD")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_6AAD")

    QueueWorkItem2(0x104, 2, lambda_6AAD)

    def lambda_6ABF():

        label("loc_6ABF")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_6ABF")

    QueueWorkItem2(0x109, 2, lambda_6ABF)

    def lambda_6AD1():

        label("loc_6AD1")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_6AD1")

    QueueWorkItem2(0x105, 2, lambda_6AD1)

    def lambda_6AE3():

        label("loc_6AE3")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_6AE3")

    QueueWorkItem2(0x16, 2, lambda_6AE3)
    WaitChrThread(0x23, 1)
    TurnDirection(0x23, 0x101, 500)
    OP_6F(0x79)

    #C0338
    ChrTalk(
        0x101,
        "#00011F迪塔市长！？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        "#00105F迪塔叔叔……！\x02",
    )

    CloseMessageWindow()

    def lambda_6B36():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6B36)
    Sleep(1000)
    Fade(500)
    OP_68(4000, 900, 6200, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)

    def lambda_6B86():
        OP_96(0xFE, 0x898, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6B86)
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
            "半个月不见了啊，\x01",
            "艾莉、罗伊德。\x02\x03",

            "还有瓦吉和诺艾尔……\x02\x03",

            "哦哦，兰迪和缇欧也回来了啊，\x01",
            "真是好久不见了。\x02",
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
        "#00309F#5P哈哈，好久不见。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#5P#00204F久疏问候。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        "#00102F#11P但是迪塔叔叔为何要……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00002F#5P通商会议马上就要开始了，\x01",
            "您应该很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x23,
        (
            "#12P#02804F准备工作早就完成了，\x01",
            "接下来，只要等首脑们到场就行了。\x02\x03",

            "#02800F所以就想带你们四处转转，\x01",
            "顺便转换一下心情。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x16, 500)
    Sleep(150)

    #C0346
    ChrTalk(
        0x23,
        "#02800F#11P达德利，不介意吧？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x16,
        "#6P#00606F呼……既然市长都发话了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(150)

    #C0348
    ChrTalk(
        0x16,
        (
            "#6P#00600F你们几个，\x01",
            "千万不要对市长失礼。\x02\x03",

            "等你们参观完毕之后，\x01",
            "就来三十四层的警备对策室。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 500)

    #C0349
    ChrTalk(
        0x101,
        "#5P#00000F明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x23, 500)
    Sleep(300)

    #C0350
    ChrTalk(
        0x16,
        "#6P#00603F市长，我先告辞了。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x23,
        "#02800F#11P嗯，辛苦了。\x02",
    )

    CloseMessageWindow()

    def lambda_6ECD():

        label("loc_6ECD")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6ECD")

    QueueWorkItem2(0x101, 2, lambda_6ECD)

    def lambda_6EDF():

        label("loc_6EDF")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6EDF")

    QueueWorkItem2(0x102, 2, lambda_6EDF)

    def lambda_6EF1():

        label("loc_6EF1")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6EF1")

    QueueWorkItem2(0x103, 2, lambda_6EF1)

    def lambda_6F03():

        label("loc_6F03")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6F03")

    QueueWorkItem2(0x104, 2, lambda_6F03)

    def lambda_6F15():

        label("loc_6F15")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6F15")

    QueueWorkItem2(0x109, 2, lambda_6F15)

    def lambda_6F27():

        label("loc_6F27")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6F27")

    QueueWorkItem2(0x105, 2, lambda_6F27)

    def lambda_6F39():

        label("loc_6F39")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_6F39")

    QueueWorkItem2(0x23, 2, lambda_6F39)
    OP_92(0x16, 0x0, 0x8FC, 0x1F4)
    OP_68(1000, 900, 2200, 3000)

    def lambda_6F69():
        OP_95(0xFE, 0, 0, 2300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6F69)
    WaitChrThread(0x16, 1)

    def lambda_6F87():
        OP_95(0xFE, 0, 0, -5000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6F87)
    Sleep(2000)
    Sound(107, 0, 100, 0)

    def lambda_6FAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6FAA)
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
            "#02804F呵呵，虽然是位能干的搜查官，\x01",
            "但好像有点古板呢。\x02\x03",

            "#02800F以他的职业来说，\x01",
            "这也算是一种优点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#00012F#6P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x105,
        (
            "#10304F#6P他毕竟要保持\x01",
            "鬼之搜查一科的威严嘛。\x02",
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
            "#6P#02805F哦，差点把\x01",
            "重要的话忘记……\x02\x03",

            "#02809F支援科的诸位，\x01",
            "欢迎你们来到『兰花塔』！\x02\x03",

            "请跟我来吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_71BB():

        label("loc_71BB")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_71BB")

    QueueWorkItem2(0x101, 2, lambda_71BB)

    def lambda_71CD():

        label("loc_71CD")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_71CD")

    QueueWorkItem2(0x102, 2, lambda_71CD)

    def lambda_71DF():

        label("loc_71DF")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_71DF")

    QueueWorkItem2(0x103, 2, lambda_71DF)

    def lambda_71F1():

        label("loc_71F1")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_71F1")

    QueueWorkItem2(0x104, 2, lambda_71F1)

    def lambda_7203():

        label("loc_7203")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_7203")

    QueueWorkItem2(0x109, 2, lambda_7203)

    def lambda_7215():

        label("loc_7215")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_7215")

    QueueWorkItem2(0x105, 2, lambda_7215)
    OP_92(0x23, 0x1B58, 0x3E8, 0x1F4)
    OP_68(6500, 1000, 3000, 3000)

    def lambda_7245():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7245)
    WaitChrThread(0x23, 1)

    def lambda_7263():
        OP_95(0xFE, 12000, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7263)
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
        "#00302F#5P哈哈，一点都没变。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#5P#00204F真不愧是玛丽亚贝尔\x01",
            "小姐的父亲。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x102,
        (
            "#5P#00109F总之，迪塔叔叔亲自\x01",
            "带我们参观，这种机会很难得。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#5P#00000F嗯，那就却之不恭了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_747C")
    Jump("loc_7481")

    label("loc_747C")

    OP_29(0x71, 0x4, 0x40)

    label("loc_7481")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7492")
    Jump("loc_7497")

    label("loc_7492")

    OP_29(0x72, 0x4, 0x40)

    label("loc_7497")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_74A8")
    Jump("loc_74AD")

    label("loc_74A8")

    OP_29(0x77, 0x4, 0x40)

    label("loc_74AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_74BE")
    Jump("loc_74C3")

    label("loc_74BE")

    OP_29(0x79, 0x4, 0x40)

    label("loc_74C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_74D4")
    Jump("loc_74D9")

    label("loc_74D4")

    OP_29(0x7A, 0x4, 0x40)

    label("loc_74D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_74EA")
    Jump("loc_74EF")

    label("loc_74EA")

    OP_29(0x7B, 0x4, 0x40)

    label("loc_74EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7500")
    Jump("loc_7505")

    label("loc_7500")

    OP_29(0x7C, 0x4, 0x40)

    label("loc_7505")

    OP_1B(0x0, 0x0, 0x33)
    EventEnd(0x5)
    Return()

    # Function_42_5EDB end

    def Function_43_750D(): pass

    label("Function_43_750D")


    def lambda_7512():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7512)
    WaitChrThread(0x16, 1)

    def lambda_7530():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7530)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x0, 0x1F4)
    Return()

    # Function_43_750D end

    def Function_44_7551(): pass

    label("Function_44_7551")

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
        "#6P#10105F导力梯有三部……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x105,
        "#6P#10302F嘿，真阔气啊。\x02",
    )

    CloseMessageWindow()

    def lambda_76A1():
        OP_97(0x102, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_76A1)
    Sleep(50)

    def lambda_76BE():
        OP_97(0x101, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_76BE)
    Sleep(50)

    def lambda_76DB():
        OP_97(0x104, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_76DB)
    Sleep(50)

    def lambda_76F8():
        OP_97(0x103, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_76F8)
    Sleep(50)

    def lambda_7715():
        OP_97(0x105, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7715)
    Sleep(50)

    def lambda_7732():
        OP_97(0x109, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7732)
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
            "#02804F#11P呵呵，毕竟有四十层呢。\x02\x03",

            "#02800F算上专用梯，\x01",
            "共有六部导力梯可供使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#6P#00002F真厉害啊……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x23,
        (
            "#02803F#11P好了，今天来不及\x01",
            "带你们参观所有楼层了，\x01",
            "就熟悉一下与会议有关的楼层吧。\x02\x03",

            "#02800F首先是警备对策室所在的三十四层。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x102,
        "#00102F#6P麻烦您了。\x02",
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

    # Function_44_7551 end

    def Function_45_78DC(): pass

    label("Function_45_78DC")

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

    # Function_45_78DC end

    def Function_46_7910(): pass

    label("Function_46_7910")


    def lambda_7915():
        OP_95(0xFE, 81000, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7915)
    WaitChrThread(0xFE, 1)

    def lambda_7933():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7933)
    Sleep(500)

    def lambda_7950():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7950)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_7910 end

    def Function_47_7961(): pass

    label("Function_47_7961")

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

    def lambda_7A91():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7A91)
    Sleep(200)

    def lambda_7AAE():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7AAE)
    Sleep(200)

    def lambda_7ACB():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7ACB)
    Sleep(200)

    def lambda_7AE8():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7AE8)
    Sleep(200)

    def lambda_7B05():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7B05)
    Sleep(200)

    def lambda_7B22():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7B22)
    SetCameraDistance(18500, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)
    Sleep(100)

    def lambda_7B57():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B57)
    Sleep(300)

    def lambda_7B6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7B6B)
    Sleep(200)

    def lambda_7B7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B7F)
    Sleep(600)

    def lambda_7B93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7B93)
    Sleep(200)

    def lambda_7BA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7BA7)
    Sleep(300)

    def lambda_7BBB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7BBB)
    Sound(803, 2, 100, 0)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_7BF1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7BF1)
    Sleep(50)

    def lambda_7C01():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7C01)
    Sleep(50)

    def lambda_7C11():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7C11)
    Sleep(50)

    def lambda_7C21():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7C21)
    Sleep(50)

    def lambda_7C31():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7C31)

    #C0366
    ChrTalk(
        0x101,
        "#00005F#11P哦……\x02",
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
    SetChrName("约纳的声音")

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "喂喂，你们在哪里？\x02\x03",

            "我已经把各种装置\x01",
            "都设置好了。\x02",
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
            "#00004F哦，我们正在兰花塔的\x01",
            "入口大厅，马上就来。\x02\x03",

            "#00000F直接去塔顶就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0369
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，跟前台说一声，\x01",
            "就能拿到导力梯的认证卡。\x02\x03",

            "快点上来吧。\x02",
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
            "#00002F知道了，辛苦你啦。\x02",
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
        "#11P#00202F约纳他们好像已经准备好了啊。\x02",
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
            "#00000F#5P嗯，我们去前台领取认证卡片，\x01",
            "然后去塔顶找他们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#6P#00104F现在还下着雨，\x01",
            "最好别让对方等太久。\x02",
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

    # Function_47_7961 end

    def Function_48_7F2D(): pass

    label("Function_48_7F2D")

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
        "#5P欢迎来到兰花塔。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        "#5P啊，是特别任务支援科的各位吧？\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            "#00000F#11P嗯，听说可以在这里\x01",
            "领取认证卡？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        "#5P是的，请拿好。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '临时认证卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('临时认证卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0379
    ChrTalk(
        0x8,
        (
            "#5P把交给您的那张卡片插入\x01",
            "导力梯内的控制面板，\x01",
            "就可以直达顶层——四十层了。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#5P卡片在一个月内有效，\x01",
            "过期之后请随意处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        "#00011F#11P明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x109,
        "#12P#10112F（听起来就觉得很厉害啊……）\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x104,
        (
            "#00306F#11P（嗯，比ＩＢＣ大楼\x01",
            "  还要先进……）\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x105,
        (
            "#12P#10302F（不愧是集最新技术\x01",
            "  之大成的建筑啊。）\x02",
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

    # Function_48_7F2D end

    def Function_49_821D(): pass

    label("Function_49_821D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_823D")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_823D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8251")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_8251")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8265")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_8265")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8279")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_8279")

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
            "#12P#10104F……不要紧，\x01",
            "各种功能还能正常使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#00000F是吗……\x01",
            "这次真是多亏有它。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#00104F#6P……是啊。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x103,
        (
            "#6P#00202F以后一定要\x01",
            "把它修理好。\x02",
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

    def lambda_8521():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_8521)
    Sleep(30)

    def lambda_8531():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8531)
    Sleep(30)

    def lambda_8541():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_8541)
    Sleep(30)

    def lambda_8551():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8551)
    Sleep(30)

    def lambda_8561():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8561)
    Sleep(30)

    def lambda_8571():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8571)
    Sleep(30)

    def lambda_8581():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8581)
    Sleep(30)

    def lambda_8591():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8591)
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
        "#5P#10708F……似乎还有敌人啊。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x105,
        (
            "#10401F嗯，敌人简直\x01",
            "无穷无尽。\x02",
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
            "#5P#00306F没时间了……\x01",
            "赶快乘导力梯\x01",
            "上去吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)

    #C0392
    ChrTalk(
        0x10A,
        (
            "#6P#00603F按照事先商定的计划，\x01",
            "留下两个人在这里待命。\x02\x03",

            "#00600F你来安排吧，班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)

    def lambda_86E1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_86E1)
    Sleep(30)

    def lambda_86F1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_86F1)
    Sleep(30)

    def lambda_8701():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8701)
    Sleep(30)

    def lambda_8711():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8711)
    Sleep(30)

    def lambda_8721():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_8721)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    #C0393
    ChrTalk(
        0x101,
        "#11P#00001F明白了。\x02",
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

    # Function_49_821D end

    def Function_50_87F2(): pass

    label("Function_50_87F2")

    EventBegin(0x1)
    OP_4B(0x1F, 0xFF)
    TurnDirection(0x1F, 0x0, 500)

    #C0394
    ChrTalk(
        0x1F,
        "各位有认证卡吗？\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x1F,
        (
            "如果没有认证卡，\x01",
            "是无法乘坐导力梯的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 74460, 0, 1270, 180)
    OP_93(0x1F, 0xB4, 0x0)
    OP_4C(0x1F, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_50_87F2 end

    def Function_51_885F(): pass

    label("Function_51_885F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88E1")
    SetChrName("")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从广场方向断断续续地传来\x01",
            "枪击和刀剑斩击声。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0397
    ChrTalk(
        0x101,
        (
            "#00001F大家正在为了我们\x01",
            "而拼命战斗……\x02\x03",

            "赶快前进吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_891F")

    #C0398
    ChrTalk(
        0x101,
        (
            "#00001F不能让市长久等，\x01",
            "我们赶快跟上去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_891F")

    SetChrPos(0x0, -290, 0, -3540, 0)
    EventEnd(0x4)
    Return()

    # Function_51_885F end

    def Function_52_8933(): pass

    label("Function_52_8933")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8945")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A95")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_89AC")
    MenuCmd(1, 0, "在导力车内休息")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89AC")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A10")

    #C0399
    ChrTalk(
        0x101,
        (
            "#00001F……现在不要勉强开动它了，\x01",
            "等事件平息之后再去修理吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A90")

    label("loc_8A10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A86")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_8A49")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_8A61")

    label("loc_8A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_8A5C")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_8A61")

    label("loc_8A5C")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_8A61")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A90")

    label("loc_8A86")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A90")

    Jump("loc_8945")

    label("loc_8A95")

    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_52_8933 end

    SaveToFile()

Try(main)
