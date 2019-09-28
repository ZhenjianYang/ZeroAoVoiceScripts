from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0170.bin",                # FileName
        "c0170",                    # MapName
        "c0170",                    # Location
        0x0005,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0170",                  # 0
        "接待小姐帕尔",           # 1
        "接待小姐辛茜亚",         # 2
        "汉森",                   # 3
        "利乔",                   # 4
        "普拉达",                 # 5
        "贝卡",                   # 6
        "沙扎克",                 # 7
        "利娜莉",                 # 8
        "普鲁娜",                 # 9
        "奈斯顿经理",             # 10
        "珍妮特",                 # 11
        "巴乔",                   # 12
        "德罗缇",                 # 13
        "肯",                     # 14
        "欧奈斯特老人",           # 15
        "尤利",                   # 16
        "塞克斯",                 # 17
        "瑞吉",                   # 18
        "普莉埃",                 # 19
        "格蕾丝",                 # 20
        "雷因兹",                 # 21
        "市民",                   # 22
        "游客",                   # 23
        "游客",                   # 24
        "雷蒙德搜查官",           # 25
        "达德利搜查官",           # 26
        "菲尔纳德",               # 27
        "乔安娜",                 # 28
    ))

    AddCharChip((
        "chr/ch27400.itc",                   # 00
        "chr/ch26600.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch20000.itc",                   # 05
        "chr/ch10400.itc",                   # 06
        "chr/ch34200.itc",                   # 07
        "chr/ch21600.itc",                   # 08
        "chr/ch34600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch20500.itc",                   # 0C
        "chr/ch44102.itc",                   # 0D
        "chr/ch47500.itc",                   # 0E
        "chr/ch23600.itc",                   # 0F
        "chr/ch29000.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch32302.itc",                   # 13
        "chr/ch44202.itc",                   # 14
        "chr/ch06000.itc",                   # 15
        "chr/ch28100.itc",                   # 16
        "chr/ch30200.itc",                   # 17
        "chr/ch00900.itc",                   # 18
        "chr/ch27800.itc",                   # 19
        "chr/ch25700.itc",                   # 1A
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-9119,   0,       2869,    90,   405,  0x0, 0,   11,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-7519,   0,       2869,    270,  405,  0x0, 0,   12,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   17,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   28,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   8,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(6659,    8199,    6300,    180,  389,  0x0, 0,   13,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(5050,    8000,    5130,    90,   389,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(7250,    8000,    4730,    0,    389,  0x0, 0,   15,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(8750,    0,       1879,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(-15840,  0,       15979,   0,    389,  0x0, 0,   21,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(-14829,  0,       14739,   315,  389,  0x0, 0,   22,  0,   0,   0,   0,   48,  255,  0)
    DeclNpc(-14649,  0,       10310,   0,    389,  0x0, 0,   18,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-13470,  8199,    21430,   270,  389,  0x0, 0,   19,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(-13470,  8199,    20629,   270,  389,  0x0, 0,   20,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(-5599,   8000,    5699,    0,    389,  0x0, 0,   23,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(899,     8029,    27729,   315,  389,  0x0, 0,   24,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(-13470,  0,       6510,    315,  389,  0x0, 0,   25,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(8750,    0,       1879,    90,   385,  0x0, 0,   26,  0,   0,   0,   0,   43,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  5,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  7,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  11, 0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  13, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  15, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  17, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  19, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  49, 0x0000)
    DeclActor(12000,   0,       15200,   1200,    12000,   1500,    15200,   0x007C, 0,  4,  0x0000)
    DeclActor(-14980,  0,       11460,   1200,    -14980,  1500,    11460,   0x007C, 0,  50, 0x0000)

    ChipFrameInfo(1616, 0)                                       # 0

    ScpFunction((
        "Function_0_650",          # 00, 0
        "Function_1_700",          # 01, 1
        "Function_2_7D9",          # 02, 2
        "Function_3_B98",          # 03, 3
        "Function_4_C9C",          # 04, 4
        "Function_5_DAC",          # 05, 5
        "Function_6_DB0",          # 06, 6
        "Function_7_18B0",         # 07, 7
        "Function_8_18B4",         # 08, 8
        "Function_9_20AB",         # 09, 9
        "Function_10_226B",        # 0A, 10
        "Function_11_23BD",        # 0B, 11
        "Function_12_23DC",        # 0C, 12
        "Function_13_30AA",        # 0D, 13
        "Function_14_30B1",        # 0E, 14
        "Function_15_4013",        # 0F, 15
        "Function_16_4017",        # 10, 16
        "Function_17_4D85",        # 11, 17
        "Function_18_4D89",        # 12, 18
        "Function_19_5902",        # 13, 19
        "Function_20_5909",        # 14, 20
        "Function_21_6E0D",        # 15, 21
        "Function_22_6F1B",        # 16, 22
        "Function_23_7EB8",        # 17, 23
        "Function_24_81FB",        # 18, 24
        "Function_25_84EF",        # 19, 25
        "Function_26_86C0",        # 1A, 26
        "Function_27_89A2",        # 1B, 27
        "Function_28_907A",        # 1C, 28
        "Function_29_973F",        # 1D, 29
        "Function_30_9F91",        # 1E, 30
        "Function_31_A72D",        # 1F, 31
        "Function_32_A8C7",        # 20, 32
        "Function_33_A9EB",        # 21, 33
        "Function_34_AA64",        # 22, 34
        "Function_35_AAD7",        # 23, 35
        "Function_36_AB44",        # 24, 36
        "Function_37_ACF0",        # 25, 37
        "Function_38_ADA8",        # 26, 38
        "Function_39_B612",        # 27, 39
        "Function_40_B703",        # 28, 40
        "Function_41_B82B",        # 29, 41
        "Function_42_B934",        # 2A, 42
        "Function_43_BA64",        # 2B, 43
        "Function_44_BABF",        # 2C, 44
        "Function_45_C01F",        # 2D, 45
        "Function_46_C06F",        # 2E, 46
        "Function_47_C706",        # 2F, 47
        "Function_48_C7BF",        # 30, 48
        "Function_49_C945",        # 31, 49
        "Function_50_CA19",        # 32, 50
        "Function_51_D1E9",        # 33, 51
        "Function_52_D3B0",        # 34, 52
        "Function_53_DA22",        # 35, 53
    ))


    def Function_0_650(): pass

    label("Function_0_650")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_688"),
        (1, "loc_694"),
        (2, "loc_6A0"),
        (3, "loc_6AC"),
        (4, "loc_6B8"),
        (5, "loc_6C4"),
        (6, "loc_6D0"),
        (SWITCH_DEFAULT, "loc_6DC"),
    )


    label("loc_688")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_694")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6FF")

    Return()

    # Function_0_650 end

    def Function_1_700(): pass

    label("Function_1_700")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D8")
    OP_95(0xFE, 13800, 8000, 6200, 2000, 0x0)
    OP_95(0xFE, 14520, 8000, 20050, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8530, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -14240, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 23430, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 7560, 2000, 0x0)
    OP_95(0xFE, -11380, 8000, 2990, 2000, 0x0)
    OP_95(0xFE, 14040, 8000, 2490, 2000, 0x0)
    Jump("Function_1_700")

    label("loc_7D8")

    Return()

    # Function_1_700 end

    def Function_2_7D9(): pass

    label("Function_2_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_813")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x11, -13470, 0, 6510, 135)
    SetChrPos(0x22, -12670, 0, 5710, 315)
    Jump("loc_B83")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_88F")
    SetChrPos(0x12, -17370, 30, 22740, 45)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -1360, 0, 9830, 270)
    OP_93(0x11, 0x5A, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 8060, 8000, 2080, 90)
    SetChrPos(0xF, 9560, 8000, 2080, 270)
    Jump("loc_B83")

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8E5")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    SetChrPos(0x15, 8020, 8000, 17270, 90)
    SetChrPos(0x14, 9070, 8000, 17290, 270)
    BeginChrThread(0x14, 0, 0, 0)
    Jump("loc_B83")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_913")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_B83")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_93C")
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_B83")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_974")
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_B83")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_987")
    ClearChrFlags(0x23, 0x80)
    Jump("loc_B83")

    label("loc_987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_99A")
    ClearChrFlags(0x21, 0x80)
    Jump("loc_B83")

    label("loc_99A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9AD")
    SetChrFlags(0x12, 0x80)
    Jump("loc_B83")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A0F")
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D4")
    SetChrFlags(0x1C, 0x10)

    label("loc_9D4")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1E, 0x13)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x14)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_B83")

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_A4F")
    SetChrPos(0x15, 8020, 8000, 17270, 90)
    SetChrPos(0x14, 9070, 8000, 17290, 270)
    BeginChrThread(0x14, 0, 0, 0)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x13, 0x80)
    Jump("loc_B83")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A93")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1E, 0x13)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x14)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_B83")

    label("loc_A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B10")
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0xD)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD0")
    SetChrFlags(0x17, 0x10)

    label("loc_AD0")

    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1E, 0x13)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x14)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_B83")

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B70")
    SetChrPos(0x12, -17370, 30, 22740, 45)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6B")
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -15840, 0, 15980, 0)
    SetChrFlags(0x1C, 0x10)

    label("loc_B6B")

    Jump("loc_B83")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B83")
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x1D, 0x80)

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B97")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_B97")

    Return()

    # Function_2_7D9 end

    def Function_3_B98(): pass

    label("Function_3_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BA5")
    OP_65(0x1, 0x1)

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7")
    OP_65(0x0, 0x1)

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C00")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_C3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C60")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_C6E")

    label("loc_C60")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_C6E")

    OP_65(0x9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9B")
    OP_1B(0x0, 0x0, 0x35)
    OP_66(0x9, 0x1)

    label("loc_C9B")

    Return()

    # Function_3_B98 end

    def Function_4_C9C(): pass

    label("Function_4_C9C")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　★　利乔食品店·小贴士　★\x01",
            "各位尊敬的来店顾客，\x01",
            "我们向您推荐润喉爽口的铃铛草莓果汁。\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书写着铃铛草莓果汁的食谱。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_DA8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『铃铛草莓果汁』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DA8")

    TalkEnd(0xFF)
    Return()

    # Function_4_C9C end

    def Function_5_DAC(): pass

    label("Function_5_DAC")

    Call(0, 6)
    Return()

    # Function_5_DAC end

    def Function_6_DB0(): pass

    label("Function_6_DB0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E37")

    #C0004
    ChrTalk(
        0x8,
        (
            "斯克特不久前\x01",
            "来看我了。\x01",
            "他好像很有精神，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "看到他那么\x01",
            "拼命努力……\x01",
            "我也要加油做好自己能做到的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E52")
    Call(0, 23)
    Jump("loc_F59")

    label("loc_E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F11")

    #C0006
    ChrTalk(
        0x8,
        (
            "所幸这里的\x01",
            "食物与日用品还算充足，\x01",
            "暂时不必发愁……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "但如果这种状况长期持续下去，\x01",
            "那些储备不足的家庭\x01",
            "实在是很让人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "真是的……政府的人到底\x01",
            "在想些什么啊？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F59")

    label("loc_F11")


    #C0009
    ChrTalk(
        0x8,
        (
            "真是的……政府的人到底\x01",
            "在想些什么啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "希望斯克特\x01",
            "平安无事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F59")

    Jump("loc_18AC")

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103A")

    #C0011
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈在居民投票的翌日\x01",
            "就回故乡雷米菲利亚去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "前辈恐怕也没有想到\x01",
            "克洛斯贝尔会发展成\x01",
            "如今这种状况吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "从前一段时间开始，\x01",
            "她的家人就一直很担心她，\x01",
            "能及时回国，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10D8")

    label("loc_103A")


    #C0014
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈和我做了约定，\x01",
            "说她一定会回到这个\x01",
            "百货店的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "虽然还有很多事情让人不安……\x01",
            "但我相信以后还可以与前辈一起工作，\x01",
            "所以我现在一定会拼命努力的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D8")

    Jump("loc_18AC")

    label("loc_10DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1166")

    #C0016
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈\x01",
            "去行政区的\x01",
            "慈善宴会帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "而且好像还要参加什么\x01",
            "职业女性选秀。\x01",
            "到时可得找她要照片看看¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11AE")

    label("loc_1166")


    #C0018
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈好像去参加\x01",
            "什么职业女性选秀了。\x01",
            "到时可得找她要照片看看¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AE")

    Jump("loc_18AC")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1223")

    #C0019
    ChrTalk(
        0x8,
        "竟然占领了矿山镇……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "不知是什么人为了\x01",
            "何种目的而策动了这种行动……\x01",
            "但实在是不可原谅啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_1223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B2")

    #C0021
    ChrTalk(
        0x8,
        (
            "斯克特和我说，\x01",
            "最近工作很忙，\x01",
            "暂时没时间联系了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "不过我却并不在意。\x01",
            "和游击士交往，\x01",
            "本来就该习惯这种情况。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12FB")

    label("loc_12B2")


    #C0023
    ChrTalk(
        0x8,
        (
            "斯克特并不需要\x01",
            "我去担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "但还是希望\x01",
            "他小心些，\x01",
            "不要受重伤。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FB")

    Jump("loc_18AC")

    label("loc_1300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1341")

    #C0025
    ChrTalk(
        0x8,
        (
            "列车竟然会脱轨……\x01",
            "是车辆出了故障，还是……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_1341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_139A")

    #C0026
    ChrTalk(
        0x8,
        (
            "斯克特最近\x01",
            "似乎比平时\x01",
            "更加忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "加油啊，斯克特。\x01",
            "我永远支持你！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1417")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B5")
    Call(0, 10)
    Jump("loc_1412")

    label("loc_13B5")


    #C0028
    ChrTalk(
        0x8,
        (
            "啊，是经常光临\x01",
            "本百货店的\x01",
            "特别任务支援科……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "多谢各位今日光临本店。\x01",
            "请随意逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1412")

    Jump("loc_18AC")

    label("loc_1417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D9")

    #C0030
    ChrTalk(
        0x8,
        (
            "在昨天的餐会上，\x01",
            "珍妮特小姐邀请了\x01",
            "三个男人来……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "但聊了没几句，\x01",
            "三人的注意力就都\x01",
            "集中到辛茜亚前辈身上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "珍妮特小姐今天好像没什么精神，\x01",
            "她不要紧吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_150C")

    label("loc_14D9")


    #C0033
    ChrTalk(
        0x8,
        (
            "珍妮特小姐今天好像没什么精神，\x01",
            "她不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150C")

    Jump("loc_18AC")

    label("loc_1511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")

    #C0034
    ChrTalk(
        0x8,
        (
            "今天的工作结束以后，\x01",
            "我要与辛茜亚前辈\x01",
            "和珍妮特小姐一起去吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "好久没一起吃饭聊天了，\x01",
            "呵呵，真期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15CA")

    label("loc_159D")


    #C0036
    ChrTalk(
        0x8,
        (
            "好久没一起吃饭聊天了，\x01",
            "呵呵，真期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CA")

    Jump("loc_18AC")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_166E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EA")
    Call(0, 9)
    Jump("loc_1669")

    label("loc_15EA")


    #C0037
    ChrTalk(
        0x8,
        (
            "虽然以前就听说辛茜亚前辈\x01",
            "崇拜尤莉亚小姐，\x01",
            "但没想到会痴迷到这种程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "呵呵，了解到了辛茜亚前辈\x01",
            "新的一面，真开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1669")

    Jump("loc_18AC")

    label("loc_166E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1747")

    #C0039
    ChrTalk(
        0x8,
        (
            "斯克特现在正\x01",
            "做些什么呢，\x01",
            "虽然知道他肯定在工作……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x8,
        (
            "啊，抱歉……！\x01",
            "我可真是的，在工作时竟然想这些。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "如有什么需要，\x01",
            "请尽管吩咐，\x01",
            "我一定会全心全意为您服务。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1783")

    label("loc_1747")


    #C0042
    ChrTalk(
        0x8,
        (
            "如有什么需要，\x01",
            "请尽管吩咐，\x01",
            "我一定会全心全意为您服务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1783")

    Jump("loc_18AC")

    label("loc_1788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_17EC")

    #C0043
    ChrTalk(
        0x8,
        (
            "欢迎光临，\x01",
            "本店即使在下雨天也会正常营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "今天也请尽情\x01",
            "采购一番吧。（微笑）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_17EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_18AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1869")

    #C0045
    ChrTalk(
        0x8,
        (
            "欢迎光临\x01",
            "『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "这里是综合服务柜台。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "如有什么问题，\x01",
            "随时都可以来此询问。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18AC")

    label("loc_1869")


    #C0048
    ChrTalk(
        0x8,
        "这里是综合服务柜台。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "如有什么问题，\x01",
            "随时都可以来此询问。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AC")

    TalkEnd(0x8)
    Return()

    # Function_6_DB0 end

    def Function_7_18B0(): pass

    label("Function_7_18B0")

    Call(0, 8)
    Return()

    # Function_7_18B0 end

    def Function_8_18B4(): pass

    label("Function_8_18B4")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_18C5")
    Jump("loc_20A7")

    label("loc_18C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18D3")
    Jump("loc_20A7")

    label("loc_18D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_194E")

    #C0050
    ChrTalk(
        0x9,
        (
            "关于武装集团的真实身份，\x01",
            "目前有多种传言，\x01",
            "事实究竟是怎样的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "总之……我祈祷\x01",
            "各位居民不要受伤。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A7")

    label("loc_194E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19C8")

    #C0052
    ChrTalk(
        0x9,
        (
            "听说帕尔小姐和斯克特先生\x01",
            "是从小一起长大的青梅竹马。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "既是童年玩伴，还是未婚夫妇，\x01",
            "真是让人羡慕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A7")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A3D")

    #C0054
    ChrTalk(
        0x9,
        (
            "我听经理说，\x01",
            "西克洛斯贝尔街道\x01",
            "好像发生了列车脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "但愿被卷入事故中的人\x01",
            "没出什么大事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A7")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B33")

    #C0056
    ChrTalk(
        0x9,
        (
            "最近这段时间，关于独立问题的讨论\x01",
            "似乎渐渐热烈起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "住在雷米菲利亚的家人\x01",
            "建议我在出现问题之前\x01",
            "回去……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "但对我而言，\x01",
            "克洛斯贝尔也算是第二故乡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "总之，我至少也要在\x01",
            "亲眼见证过居民投票结果之后再走。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BB0")

    label("loc_1B33")


    #C0060
    ChrTalk(
        0x9,
        (
            "不管怎么说……\x01",
            "克洛斯贝尔对我而言\x01",
            "也算是第二故乡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "我打算尽到居民责任，参加居民投票并\x01",
            "亲眼见证投票结果之后再走。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB0")

    Jump("loc_20A7")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD0")
    Call(0, 10)
    Jump("loc_1C2F")

    label("loc_1BD0")


    #C0062
    ChrTalk(
        0x9,
        (
            "啊……不好意思，\x01",
            "我竟然在工作时\x01",
            "不知不觉聊起这些……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "如果有什么需要，\x01",
            "请您尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2F")

    Jump("loc_20A7")

    label("loc_1C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC0")

    #C0064
    ChrTalk(
        0x9,
        (
            "没想到\x01",
            "珍妮特小姐竟然\x01",
            "会叫男人过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "虽然知道他们\x01",
            "都很有钱……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "唉，但女人的聚会多了男人会很累啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D10")

    label("loc_1CC0")


    #C0067
    ChrTalk(
        0x9,
        (
            "没想到\x01",
            "珍妮特小姐竟然\x01",
            "会叫男人过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        "唉，女人的聚会多了男人会很累啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1D10")

    Jump("loc_20A7")

    label("loc_1D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA8")

    #C0069
    ChrTalk(
        0x9,
        (
            "珍妮特小姐\x01",
            "今天非常兴奋，\x01",
            "莫非有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "我们又不是第一次三个人\x01",
            "聚在一起吃饭……\x01",
            "她的情绪未免也太高涨了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DF0")

    label("loc_1DA8")


    #C0071
    ChrTalk(
        0x9,
        (
            "我们又不是第一次三个人\x01",
            "聚在一起吃饭……\x01",
            "她的情绪未免也太高涨了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF0")

    Jump("loc_20A7")

    label("loc_1DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E10")
    Call(0, 9)
    Jump("loc_1E77")

    label("loc_1E10")


    #C0072
    ChrTalk(
        0x9,
        (
            "啊，客人……\x01",
            "我真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "欢迎您今日光临『时代』百货店。\x01",
            "如果有什么需要，\x01",
            "请随时向我吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E77")

    Jump("loc_20A7")

    label("loc_1E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F16")

    #C0074
    ChrTalk(
        0x9,
        (
            "在从明天开始的通商会议期间，\x01",
            "与会国的各位要人\x01",
            "将会来到克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "虽然并没有贵宾预定\x01",
            "要莅临本店的通知，\x01",
            "但不知为何，还是很紧张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A7")

    label("loc_1F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F80")

    #C0076
    ChrTalk(
        0x9,
        (
            "帕尔小姐最近一直和\x01",
            "未婚夫斯克特先生定期见面，\x01",
            "所以很有精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        "呵呵，真让人羡慕啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20A7")

    label("loc_1F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204C")

    #C0078
    ChrTalk(
        0x9,
        (
            "各位去日前开放的\x01",
            "天台区域参观了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "虽然并不是什么特别的设施，\x01",
            "但登上之后，整个克洛斯贝尔市都能尽收眼底，\x01",
            "可以说是个绝佳的观景地点。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        "如果有兴趣，请一定上去看看。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20A7")

    label("loc_204C")


    #C0081
    ChrTalk(
        0x9,
        (
            "日前开放的天台区域\x01",
            "很快就受到了客人们的\x01",
            "一致好评。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "建议各位也在休息时\x01",
            "上去看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A7")

    TalkEnd(0x9)
    Return()

    # Function_8_18B4 end

    def Function_9_20AB(): pass

    label("Function_9_20AB")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    #C0083
    ChrTalk(
        0x9,
        "帕尔，你听说了吗？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "据说利贝尔的\x01",
            "来访人员之中\x01",
            "还有尤莉亚准校……！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "嗯，我当然已经知道了。\x01",
            "而且已经拜托朋友\x01",
            "帮我拍照片了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "不过，照片能不能拍好\x01",
            "可就不清楚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "！！！\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "帕尔！到时候把照片\x01",
            "也送给我一张吧！一定哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "好、好的，\x01",
            "那当然没问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00000F（尤莉亚准校吗……\x01",
            "  真是非常受欢迎呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x109,
        (
            "#10109F（嗯，那当然，\x01",
            "  毕竟是尤莉亚准校啊。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_9_20AB end

    def Function_10_226B(): pass

    label("Function_10_226B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    #C0092
    ChrTalk(
        0x9,
        (
            "那……沙扎克先生\x01",
            "告白的地点是……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "嗯，听说就是\x01",
            "米修拉姆的高级餐厅\x01",
            "『幸运』。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "而且他好像事先和店里的人打好了招呼，\x01",
            "在告白的时候还有惊喜演出呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        "沙扎克先生真是很浪漫啊～\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "是啊，珍妮特小姐能获得幸福，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "呵呵，我也要像她那么幸福。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_10_226B end

    def Function_11_23BD(): pass

    label("Function_11_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D8")
    Call(0, 46)
    Jump("loc_23DB")

    label("loc_23D8")

    Call(0, 12)

    label("loc_23DB")

    Return()

    # Function_11_23BD end

    def Function_12_23DC(): pass

    label("Function_12_23DC")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2439")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2439")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2458")
    OP_AF(0x26)
    Jump("loc_247A")

    label("loc_2458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2468")
    OP_AF(0x25)
    Jump("loc_247A")

    label("loc_2468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2478")
    OP_AF(0x24)
    Jump("loc_247A")

    label("loc_2478")

    OP_AF(0x23)

    label("loc_247A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A1")

    label("loc_2489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_249D")
    Jump("loc_30A1")

    label("loc_249D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2538")

    #C0098
    ChrTalk(
        0xA,
        (
            "虽然进口货物很难订购到了，\x01",
            "但我这里还接受\x01",
            "订制的业务。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "今后一定会增加人手，\x01",
            "努力为大家提供\x01",
            "更充实的服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_2538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_25CE")

    #C0100
    ChrTalk(
        0xA,
        (
            "这戒严令究竟要\x01",
            "持续到什么时候啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "那些食物储备不足的家庭，\x01",
            "大概坚持不了\x01",
            "几天吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "这种看不到未来的不安感\x01",
            "真是很恐怖呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_25CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_26F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2697")

    #C0103
    ChrTalk(
        0xA,
        (
            "国防军真的有能力\x01",
            "守卫克洛斯贝尔吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "虽然我很愿意相信\x01",
            "亚里欧斯先生……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "但如果两大国真的全力发动进攻，\x01",
            "我们也只能选择投降了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "还是说……\x01",
            "他们另有秘策呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26F3")

    label("loc_2697")


    #C0107
    ChrTalk(
        0xA,
        (
            "如果两大国真的全力发动进攻，\x01",
            "我们也只能选择投降了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "还是说……\x01",
            "他们另有秘策呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F3")

    Jump("loc_30A1")

    label("loc_26F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_277D")

    #C0109
    ChrTalk(
        0xA,
        (
            "城市的复兴工作\x01",
            "总算是告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "我虽然帮不上什么大忙……\x01",
            "但至少也要把一部分商品降价销售，\x01",
            "以此来回馈大家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_277D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27D9")

    #C0111
    ChrTalk(
        0xA,
        (
            "那些玛因兹老主顾的面容\x01",
            "总会浮现在我的眼前。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "希望他们都\x01",
            "平安无事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_27D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B9")

    #C0113
    ChrTalk(
        0xA,
        (
            "昨天听到列车停运的消息时，\x01",
            "我还担心以后该怎么办……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "但在警备队与各位铁路工作人员\x01",
            "的努力下，今天就已经\x01",
            "完全修复了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "多亏如此，今天早上的货\x01",
            "也顺利送达了。\x01",
            "实在是不知该如何感谢他们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2943")

    label("loc_28B9")


    #C0116
    ChrTalk(
        0xA,
        (
            "铁道已经完全修好了，\x01",
            "昨天的列车事故简直\x01",
            "就像完全没有发生过一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "真不知该如何感谢那些\x01",
            "奋力修复铁路的警备队员\x01",
            "和铁路工作人员啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2943")

    Jump("loc_30A1")

    label("loc_2948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2976")

    #C0118
    ChrTalk(
        0xA,
        "嗯，好像发生什么事故了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_2976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_END)), "loc_2A16")

    #C0119
    ChrTalk(
        0xA,
        (
            "达德利先生是本店的老顾客，\x01",
            "每年都会来定制好几双皮鞋。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "从他那对皮鞋的热情，和对做工用料的讲究程度来看，\x01",
            "绝对是一位真正的皮鞋爱好者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A16")

    Jump("loc_30A1")

    label("loc_2A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AD3")

    #C0121
    ChrTalk(
        0xA,
        (
            "人与人的邂逅，一生只有一次，\x01",
            "而人与鞋子的邂逅\x01",
            "同样也是一生只有一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "这么说也许有点奇怪，\x01",
            "但每当望向陈列柜中的那些商品时，\x01",
            "我就总觉得它们像是在对我诉说着什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_2AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B3C")

    #C0123
    ChrTalk(
        0xA,
        "真正优秀的东西不会被潮流所左右。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "我希望能一直为大家提供\x01",
            "超越时代潮流的一流商品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_2B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C27")

    #C0125
    ChrTalk(
        0xA,
        (
            "各位知道吗？如果想选购鞋子，\x01",
            "最好等到傍晚之后。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "因为人在早晨起床后，\x01",
            "脚部会慢慢舒展开，到了傍晚时分，\x01",
            "将比清晨时大出一里矩左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "因此，要挑选鞋子的码数，最好还是选择\x01",
            "脚部舒展得最开的傍晚之后。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CD2")

    label("loc_2C27")


    #C0128
    ChrTalk(
        0xA,
        (
            "其实，这是因为人在早晨睡醒后，\x01",
            "脚部会慢慢舒展开来，到了傍晚时分，\x01",
            "将比清晨时大出一里矩左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "因此，如果想买到码数合适的鞋子，\x01",
            "最好选择脚部舒展得最开的傍晚之后。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD2")

    Jump("loc_30A1")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D3D")

    #C0130
    ChrTalk(
        0xA,
        (
            "皮鞋这种东西，\x01",
            "越穿就越顺脚。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "鞋子就和人一样，是颇有内涵而又\x01",
            "妙趣深远的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_2D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D9F")

    #C0132
    ChrTalk(
        0xA,
        (
            "本店也有很多\x01",
            "儿童用品。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "欢迎您\x01",
            "随意挑选。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFE")

    label("loc_2D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8B")

    #C0134
    ChrTalk(
        0xA,
        (
            "普拉达小姐总是建议我像以前一样，\x01",
            "除了鞋子也做服装的销售……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "但光是鞋子这一个领域就已经非常\x01",
            "深奥了。自从投身到这一行业之后，\x01",
            "我更加深刻地感受到了这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "所以我现在心无旁骛，\x01",
            "只想专心在鞋子的领域中钻研。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EFE")

    label("loc_2E8B")


    #C0137
    ChrTalk(
        0xA,
        (
            "服装的领域自不必说，\x01",
            "而鞋子的领域同样也是\x01",
            "非常深奥的。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "所以我现在心无旁骛，\x01",
            "只想专心在鞋子的领域中钻研。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EFE")

    Jump("loc_30A1")

    label("loc_2F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F64")

    #C0139
    ChrTalk(
        0xA,
        (
            "本店也销售\x01",
            "雨靴。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "突然下雨的时候，可以买下之后\x01",
            "立刻换上哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FA4")

    label("loc_2F64")


    #C0141
    ChrTalk(
        0xA,
        (
            "本店也销售\x01",
            "雨靴。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "如果您有需要，\x01",
            "我可以推荐一些产品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA4")

    Jump("loc_30A1")

    label("loc_2FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_30A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303E")

    #C0143
    ChrTalk(
        0xA,
        "欢迎光临『汉森鞋店』。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "如果在选购商品时有什么困惑的地方，\x01",
            "请随时找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "我会认真帮顾客们挑选\x01",
            "最合适的鞋子。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30A1")

    label("loc_303E")


    #C0146
    ChrTalk(
        0xA,
        (
            "本店不仅经营休闲鞋，\x01",
            "也有正装鞋、登山鞋\x01",
            "等各种类型的鞋子。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "一定可以挑选到\x01",
            "适合您的鞋子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A1")

    Jump("loc_23E9")

    label("loc_30A6")

    TalkEnd(0xA)
    Return()

    # Function_12_23DC end

    def Function_13_30AA(): pass

    label("Function_13_30AA")

    SetScenarioFlags(0x2, 3)
    Call(0, 14)
    Return()

    # Function_13_30AA end

    def Function_14_30B1(): pass

    label("Function_14_30B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3106")
    TalkBegin(0xB)

    #C0148
    ChrTalk(
        0xB,
        (
            "您好像不是……\x01",
            "运货员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "如果想买东西，\x01",
            "还请绕到前方哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    label("loc_3106")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324C")

    #C0150
    ChrTalk(
        0x1A2,
        (
            "原来如此，这里有很多\x01",
            "进口食材啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1A2,
        "唔，连酱油都有啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x1A2, 500)
    Sleep(300)

    #C0152
    ChrTalk(
        0xB,
        (
            "呵呵，小朋友，\x01",
            "你是从东方来的客人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "这里有很多出产自东方的\x01",
            "食材，就算是东方的客人\x01",
            "也一定可以满意而归。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "如果你需要的商品\x01",
            "在这里无法找到，\x01",
            "可以尽管和我说哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x1A2,
        "啊，嗯……我想想。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TalkEnd(0xB)
    Jump("loc_32A8")

    label("loc_324C")

    TalkBegin(0xB)

    #C0156
    ChrTalk(
        0xB,
        (
            "只要客人们有要求，\x01",
            "我这里也可以\x01",
            "接受订货的。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        "如有需要，随时都可以和我说哦。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)

    label("loc_32A8")

    Return()

    label("loc_32A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3303")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3323")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_400A")

    label("loc_3323")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3337")
    Jump("loc_400A")

    label("loc_3337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33DA")

    #C0158
    ChrTalk(
        0xB,
        (
            "我刚才和女儿取得了联络，\x01",
            "确认到她现在一切安好。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "戒严令解除后，女儿好像立刻就摆出摊子工作了，\x01",
            "我也必须要努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400A")

    label("loc_33DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3460")

    #C0160
    ChrTalk(
        0xB,
        (
            "话说回来……\x01",
            "不知我女儿有没有\x01",
            "及时回家避难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "自从戒严令下达之后，\x01",
            "导力通讯也一直无法使用了……\x01",
            "真是好担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400A")

    label("loc_3460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3535")

    #C0162
    ChrTalk(
        0xB,
        (
            "听说从今天早上开始，\x01",
            "经过克洛斯贝尔的列车\x01",
            "就要遭到全面限制了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "也就是说，今天就是\x01",
            "列车运行的最后日子了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "在如此状况下，比起买卖方面的麻烦，\x01",
            "我更加担心的还是战争二字。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35A5")

    label("loc_3535")


    #C0165
    ChrTalk(
        0xB,
        (
            "听说今天就是\x01",
            "列车运行的最后日子了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xB,
        (
            "在如此状况下，比起买卖方面的麻烦，\x01",
            "我更加担心的还是战争二字。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A5")

    Jump("loc_400A")

    label("loc_35AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365E")

    #C0167
    ChrTalk(
        0xB,
        (
            "无论发生什么事情，\x01",
            "我们这些商业人士也不会泄气。\x01",
            "总之，现在要先尽可能地努力工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "欢迎光临，如果身体疲惫，\x01",
            "就来尝尝奥雷德自治州出产的大蒜如何？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36E8")

    label("loc_365E")


    #C0169
    ChrTalk(
        0xB,
        (
            "欢迎光临，如果身体疲惫，\x01",
            "就来尝尝奥雷德自治州出产的大蒜如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "奥雷德自治州出产的大蒜个头很大，\x01",
            "而且营养价值高，最适合滋补身体。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E8")

    Jump("loc_400A")

    label("loc_36ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3742")

    #C0171
    ChrTalk(
        0xB,
        (
            "不知玛因兹的那些人\x01",
            "现在怎样了……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        "真希望能尽快将他们解救……\x02",
    )

    CloseMessageWindow()
    Jump("loc_400A")

    label("loc_3742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F8")

    #C0173
    ChrTalk(
        0xB,
        (
            "导力铁路只用了一个晚上\x01",
            "就彻底修复完毕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "多亏如此，今天的铁路包裹\x01",
            "也像往常一样，按时送到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "真得好好感谢那些通宵修复铁路的\x01",
            "警备队员们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3864")

    label("loc_37F8")


    #C0176
    ChrTalk(
        0xB,
        (
            "多亏如此，今天的铁路包裹\x01",
            "也像往常一样，按时送到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "真得好好感谢那些通宵修复铁路的\x01",
            "警备队员们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3864")

    Jump("loc_400A")

    label("loc_3869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3941")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E0")

    #C0178
    ChrTalk(
        0xB,
        (
            "据说西克洛斯贝尔街道那边\x01",
            "发生了列车脱轨事故呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "难道是因为发生了\x01",
            "塌方事故吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_393C")

    label("loc_38E0")


    #C0180
    ChrTalk(
        0xB,
        (
            "据说西克洛斯贝尔街道那边\x01",
            "发生了列车脱轨事故呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "难道是因为发生了\x01",
            "塌方事故吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_393C")

    Jump("loc_400A")

    label("loc_3941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_39A5")

    #C0182
    ChrTalk(
        0xB,
        (
            "欢迎光临『利乔食品店』，\x01",
            "各种食材应有尽有哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "共和国产的洋葱\x01",
            "今天很便宜哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400A")

    label("loc_39A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A06")

    #C0184
    ChrTalk(
        0xB,
        (
            "听说沙扎克先生和珍妮特小姐\x01",
            "开始交往了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        "呵呵，职场恋爱，真是让人羡慕。\x02",
    )

    CloseMessageWindow()
    Jump("loc_400A")

    label("loc_3A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A88")

    #C0186
    ChrTalk(
        0xB,
        (
            "不知为什么，珍妮特小姐今天好像\x01",
            "很没精神，真让人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        (
            "昨天明明还那么活泼呢，\x01",
            "莫非发生了什么事情吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400A")

    label("loc_3A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3AF7")

    #C0188
    ChrTalk(
        0xB,
        (
            "您好，\x01",
            "欢迎光临『利乔食品店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xB,
        (
            "如果您还没有准备好\x01",
            "晚餐所需的食材，\x01",
            "就请在本店选购吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400A")

    label("loc_3AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE6")

    #C0190
    ChrTalk(
        0xB,
        (
            "欢迎光临『利乔食品店』，\x01",
            "各种食材应有尽有哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "从今天开始的三天之内，\x01",
            "本店将要限时销售『通商会议套装』。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "套装包含了帝国、王国、公国、共和国，\x01",
            "以及我们克洛斯尔的代表性食材，\x01",
            "是非常豪华的食材组合哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C87")

    label("loc_3BE6")


    #C0193
    ChrTalk(
        0xB,
        (
            "从今天开始的三天之内，\x01",
            "本店将要限时销售『通商会议套装』。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "套装包含了帝国、王国、公国、共和国，\x01",
            "以及我们克洛斯尔的代表性食材，\x01",
            "是非常豪华的食材组合哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C87")

    Jump("loc_400A")

    label("loc_3C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D87")

    #C0195
    ChrTalk(
        0xB,
        (
            "欢迎光临家庭主妇最可靠的伙伴——\x01",
            "『利乔食品店』！\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "如果还在为今晚的菜单发愁，\x01",
            "我可以为您提些建议哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "比如说～\x01",
            "用今早刚到的新鲜香草\x01",
            "熬些汤如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "不过，调味用的月桂叶\x01",
            "如果煮过了头就会有苦味，\x01",
            "请一定要注意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DE7")

    label("loc_3D87")


    #C0199
    ChrTalk(
        0xB,
        (
            "如果还在为今晚的菜单发愁，\x01",
            "我可以为您提些建议哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "顺便一说，今天的\x01",
            "推荐料理是香草汤。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE7")

    Jump("loc_400A")

    label("loc_3DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E93")

    #C0201
    ChrTalk(
        0xB,
        (
            "我女儿最近正在\x01",
            "努力开发新的\x01",
            "果汁产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xB,
        (
            "今天下雨，不能出去摆摊子，\x01",
            "所以就在家里专心研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "呵呵，有进取心\x01",
            "是一件很好的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EE8")

    label("loc_3E93")


    #C0204
    ChrTalk(
        0xB,
        (
            "我女儿最近正在\x01",
            "努力开发新的\x01",
            "果汁产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "呵呵，有进取心\x01",
            "是一件很好的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE8")

    Jump("loc_400A")

    label("loc_3EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_400A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9C")

    #C0206
    ChrTalk(
        0xB,
        (
            "欢迎光临『利乔食品店』，\x01",
            "各种食材应有尽有哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "顺便一说，\x01",
            "我女儿在行政区\x01",
            "开了一间果汁店。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "那里使用的就是本店的食材，\x01",
            "还请多多光顾哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_400A")

    label("loc_3F9C")


    #C0209
    ChrTalk(
        0xB,
        (
            "欢迎光临『利乔食品店』，\x01",
            "各种食材应有尽有哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "行政区的果汁店就使用了本店的食材，\x01",
            "还请多光顾那里哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400A")

    Jump("loc_32B3")

    label("loc_400F")

    TalkEnd(0xB)
    Return()

    # Function_14_30B1 end

    def Function_15_4013(): pass

    label("Function_15_4013")

    Call(0, 16)
    Return()

    # Function_15_4013 end

    def Function_16_4017(): pass

    label("Function_16_4017")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4024")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D81")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4074")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4074")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4093")
    OP_AF(0x21)
    Jump("loc_40B5")

    label("loc_4093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40A3")
    OP_AF(0x20)
    Jump("loc_40B5")

    label("loc_40A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40B3")
    OP_AF(0x1F)
    Jump("loc_40B5")

    label("loc_40B3")

    OP_AF(0x1E)

    label("loc_40B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D7C")

    label("loc_40C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40D8")
    Jump("loc_4D7C")

    label("loc_40D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D7C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4189")

    #C0211
    ChrTalk(
        0xC,
        (
            "原本一直有此打算……\x01",
            "如今趁着这个机会，我终于决定\x01",
            "创立自己的独立品牌。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        (
            "苦难正是成长的食粮，\x01",
            "我一定会努力提供\x01",
            "让大家满意的商品！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_4189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4347")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4298")

    #C0213
    ChrTalk(
        0xC,
        (
            "总统之所以底气十足，\x01",
            "完全就是倚仗着那个\x01",
            "名为『神机』的兵器吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "……话说回来，市里到处都徘徊着那种\x01",
            "看起来像铠甲兵一样的怪物，\x01",
            "到底是怎么回事啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "也不下达一个正经的告示，\x01",
            "便投放那种东西，结果让国民陷入恐惧……\x01",
            "完全就是本末倒置啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4342")

    label("loc_4298")


    #C0216
    ChrTalk(
        0xC,
        (
            "……话说回来，\x01",
            "那些徘徊在街上，看起来像铠甲兵\x01",
            "一样的怪物到底是什么东西啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xC,
        (
            "也不下达一个正经的告示，\x01",
            "便投放那种东西，结果让国民陷入恐惧……\x01",
            "完全就是本末倒置啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4342")

    Jump("loc_4D7C")

    label("loc_4347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_43E3")

    #C0218
    ChrTalk(
        0xC,
        (
            "或许是因为从事服务行业的缘故吧，\x01",
            "我无论面对什么事物，\x01",
            "总是习惯退一步来看……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xC,
        (
            "但是，该怎么说呢……\x01",
            "还是觉得迪塔总统的发言\x01",
            "相当荒谬。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_43E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4470")

    #C0220
    ChrTalk(
        0xC,
        (
            "三天后，百货店的职员们\x01",
            "将会轮流休息，并前往投票场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "顺便一说，我还没有\x01",
            "最后决定自己的立场……\x01",
            "呼，到底该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_4470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_44EB")

    #C0222
    ChrTalk(
        0xC,
        (
            "我并不了解那个\x01",
            "所谓的武装集团，\x01",
            "只觉得完全无法理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xC,
        (
            "竟然凭借暴力来控制他人……\x01",
            "实在是愚蠢透顶啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_44EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CB")

    #C0224
    ChrTalk(
        0xC,
        (
            "也许只是我的心理作用吧，\x01",
            "最近总觉得面带笑容的客人变少了。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "再加上昨天又发生了列车事故……\x01",
            "想想最近的状况，\x01",
            "这也是没办法的事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "希望大家至少在\x01",
            "购物的时候暂时\x01",
            "忘记那些令人烦恼的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4644")

    label("loc_45CB")


    #C0227
    ChrTalk(
        0xC,
        (
            "也许只是我的心理作用吧，\x01",
            "最近总觉得面带笑容的客人变少了。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "希望大家至少在\x01",
            "购物的时候暂时\x01",
            "忘记那些令人烦恼的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4644")

    Jump("loc_4D7C")

    label("loc_4649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_467D")

    #C0229
    ChrTalk(
        0xC,
        "啊，怎么回事，外面好像很嘈杂啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_467D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_481A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_476C")

    #C0230
    ChrTalk(
        0xC,
        (
            "我们在出门的时候，往往会根据\x01",
            "自己的心情来选择穿着的服装，\x01",
            "但反过来说，服装有时也会影响我们的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "比如说，当心情消沉的时候，\x01",
            "不妨有意选择一些鲜艳明快的服装。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "那样就可以让不愉快的心情\x01",
            "烟消云散了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4815")

    label("loc_476C")


    #C0233
    ChrTalk(
        0xC,
        (
            "我们在出门的时候，往往会根据\x01",
            "自己的心情来选择穿着的服装，\x01",
            "但反过来说，服装有时也会影响我们的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        (
            "有意选择能让自己心情愉快的服装……\x01",
            "也是一种选择服装的方式。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4815")

    Jump("loc_4D7C")

    label("loc_481A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_48BE")

    #C0235
    ChrTalk(
        0xC,
        (
            "像洋装、手提包这种东西，越是高价的产品，\x01",
            "往往越在一些不易察觉的地方有讲究。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "它们大多都很结实耐用，可以使用很长时间，\x01",
            "可以算得上是物有所值。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_48BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4932")

    #C0237
    ChrTalk(
        0xC,
        (
            "所谓的流行，虽然时而会变化，\x01",
            "但终究是由人所创造的。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "身为服装店的店长，\x01",
            "我也要努力引领潮流。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_4932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_496E")

    #C0239
    ChrTalk(
        0xC,
        (
            "欢迎光临，\x01",
            "请您尽情享受\x01",
            "晚间购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_496E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49CF")

    #C0240
    ChrTalk(
        0xC,
        "通商会议终于开始了啊。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xC,
        (
            "我身为一名业界人士，\x01",
            "十分关注各国要人的服饰打扮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_49CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A5E")

    #C0242
    ChrTalk(
        0xC,
        (
            "欢迎光临，\x01",
            "请随意挑选本店\x01",
            "的时尚产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "本店的衣服可以试穿，\x01",
            "如果有需要，请尽管和我说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2C")

    label("loc_4A5E")


    #C0244
    ChrTalk(
        0xC,
        (
            "在汉森先生经营服装的时候，\x01",
            "我们曾是生意上的劲敌……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "但同时也能互相提高品位，\x01",
            "是很好的竞争对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        (
            "汉森先生转行钻研鞋子，虽然也是不错的选择……\x01",
            "但我还是觉得，也没必要把自己局限在一个领域啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4B2C")

    Jump("loc_4D7C")

    label("loc_4B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C23")

    #C0247
    ChrTalk(
        0xC,
        (
            "由于是下雨天，\x01",
            "所以有些人便不在意自己的打扮，\x01",
            "这可真是让人遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "我们应该根据时间、地点和场合来选择衣服——\x01",
            "也有些服饰搭配是\x01",
            "正适合下雨天的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "客人，如果您愿意的话，\x01",
            "请让我来为您选择合适的装扮吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CBF")

    label("loc_4C23")


    #C0250
    ChrTalk(
        0xC,
        (
            "由于是下雨天，\x01",
            "所以有些人便不在意自己的打扮，\x01",
            "这可真是让人遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xC,
        (
            "我们应该根据时间、地点和场合来选择衣服——\x01",
            "也有些服饰搭配是\x01",
            "正适合下雨天的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CBF")

    Jump("loc_4D7C")

    label("loc_4CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D40")

    #C0252
    ChrTalk(
        0xC,
        (
            "欢迎，\x01",
            "欢迎光临『卢卡时装店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "本店经营由我\x01",
            "挑选的多种品牌\x01",
            "的洋装。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xC,
        "请随意选购。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D7C")

    label("loc_4D40")


    #C0255
    ChrTalk(
        0xC,
        (
            "本店经营由我\x01",
            "挑选的多种品牌\x01",
            "的洋装。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xC,
        "请随意选购。\x02",
    )

    CloseMessageWindow()

    label("loc_4D7C")

    Jump("loc_4024")

    label("loc_4D81")

    TalkEnd(0xC)
    Return()

    # Function_16_4017 end

    def Function_17_4D85(): pass

    label("Function_17_4D85")

    Call(0, 18)
    Return()

    # Function_17_4D85 end

    def Function_18_4D89(): pass

    label("Function_18_4D89")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58FE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DE6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4DE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E05")
    OP_AF(0x11)
    Jump("loc_4E17")

    label("loc_4E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E15")
    OP_AF(0x10)
    Jump("loc_4E17")

    label("loc_4E15")

    OP_AF(0xF)

    label("loc_4E17")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58F9")

    label("loc_4E26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E3A")
    Jump("loc_58F9")

    label("loc_4E3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4ED6")

    #C0257
    ChrTalk(
        0xD,
        (
            "看到那棵大树……\x01",
            "让我想起了去年出现在利贝尔王国\x01",
            "的那个巨大物体。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xD,
        (
            "所幸没有像那次一样，\x01",
            "造成导力停止现象……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_4ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4F87")

    #C0259
    ChrTalk(
        0xD,
        (
            "在抵御住帝国的列车炮时，\x01",
            "我还在想国防军果然了不起……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xD,
        (
            "但在如今的状况下，\x01",
            "唯一的感觉也只有不安了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xD,
        (
            "『大陆诸国联盟』的构想\x01",
            "终究也只是纸上谈兵吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_4F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_508E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5017")

    #C0262
    ChrTalk(
        0xD,
        "事出突然，的确让我吃了一惊……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xD,
        (
            "但迪塔总统和\x01",
            "亚里欧斯国防长官\x01",
            "都已经把话说到那种地步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xD,
        "我相信他们二位。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5089")

    label("loc_5017")


    #C0265
    ChrTalk(
        0xD,
        (
            "事出突然，的确让我吃了一惊……\x01",
            "但迪塔总统和\x01",
            "亚里欧斯国防长官\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xD,
        "都已经把话说到那种地步了，我相信他们二位。\x02",
    )

    CloseMessageWindow()

    label("loc_5089")

    Jump("loc_58F9")

    label("loc_508E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5126")

    #C0267
    ChrTalk(
        0xD,
        (
            "为了从根本上解决问题，\x01",
            "除了独立之外，\x01",
            "确实没有其它道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xD,
        (
            "城市中发生了那样的事……\x01",
            "我可不认为继续遵从两大国\x01",
            "就能使治安得到维护。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_5126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_51B2")

    #C0269
    ChrTalk(
        0xD,
        (
            "正如很多人所说，\x01",
            "玛因兹的事件肯定是\x01",
            "帝国策动的阴谋吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "发生了如此事态，\x01",
            "真是越来越希望\x01",
            "建立起守卫自治州的军队了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_51B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_521C")

    #C0271
    ChrTalk(
        0xD,
        (
            "据传闻说，昨天的那起\x01",
            "列车脱轨事故好像是\x01",
            "由幻兽引起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xD,
        "唔，幻兽究竟是什么东西啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_521C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_528C")

    #C0273
    ChrTalk(
        0xD,
        (
            "急救车的警笛声\x01",
            "从刚才开始就响个不停……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xD,
        (
            "该不会是发生恐怖事件了吧？\x01",
            "悲剧已经够多的了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_528C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5334")

    #C0275
    ChrTalk(
        0xD,
        (
            "同样的一件饰品，\x01",
            "其价值也是因人而异的。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "不久前，孙子送给我一枚\x01",
            "亲手制作的胸针……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xD,
        (
            "对我来说，那可是比任何\x01",
            "宝石都要珍贵的宝物。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5394")

    label("loc_5334")


    #C0278
    ChrTalk(
        0xD,
        (
            "不久前，孙子送给我一枚\x01",
            "亲手制作的胸针……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xD,
        (
            "对我来说，那可是比任何\x01",
            "宝石都要珍贵的宝物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5394")

    Jump("loc_58F9")

    label("loc_5399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5434")

    #C0280
    ChrTalk(
        0xD,
        (
            "唔，独立吗？\x01",
            "真是个值得深思的问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xD,
        (
            "对离开帝国，\x01",
            "移居到了\x01",
            "克洛斯贝尔的我而言……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xD,
        (
            "这可真是个\x01",
            "非常纠结的问题啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_548B")

    label("loc_5434")


    #C0283
    ChrTalk(
        0xD,
        (
            "对离开帝国，\x01",
            "移居到了\x01",
            "克洛斯贝尔的我而言……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xD,
        (
            "有关独立的问题\x01",
            "实在是很纠结啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_548B")

    Jump("loc_58F9")

    label("loc_5490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54EC")

    #C0285
    ChrTalk(
        0xD,
        (
            "嗯，通商会议终于要\x01",
            "正式开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "总之，希望这是一场\x01",
            "有意义的会议。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_54EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_55DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5578")

    #C0287
    ChrTalk(
        0xD,
        "天色已经暗下来了呢。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        (
            "专为首脑们表演的\x01",
            "那场彩虹剧团演出\x01",
            "应该快要结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xD,
        (
            "唔，希望首脑们\x01",
            "看得开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_55D5")

    label("loc_5578")


    #C0290
    ChrTalk(
        0xD,
        (
            "对了，专为首脑们表演的\x01",
            "那场彩虹剧团演出\x01",
            "应该快要结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "唔，希望首脑们\x01",
            "看得开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D5")

    Jump("loc_58F9")

    label("loc_55DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5654")

    #C0292
    ChrTalk(
        0xD,
        (
            "我虽然都一大把年纪了，\x01",
            "但还是跑到楼顶上观看了揭幕式……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "兰花塔确实很惊人啊。\x01",
            "让我震惊到了失语呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F9")

    label("loc_5654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5760")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56D2")

    #C0294
    ChrTalk(
        0xD,
        (
            "欢迎，\x01",
            "欢迎光临『贝卡饰品店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        (
            "如果看中哪件饰品了，\x01",
            "请随意拿起来看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_575B")

    label("loc_56D2")


    #C0296
    ChrTalk(
        0xD,
        (
            "该怎么说呢，\x01",
            "来这家百货店购物的客人\x01",
            "大多都是温和亲切的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        (
            "我并不是想刻意比较，不过这里的\x01",
            "顾客和帝国的那些贵族真是有很大不同。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_575B")

    Jump("loc_58F9")

    label("loc_5760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5834")

    #C0298
    ChrTalk(
        0xD,
        (
            "不知为何，每到下雨时，\x01",
            "我就会想起从前在帝国\x01",
            "当美术商的日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xD,
        (
            "那时候的我，\x01",
            "每天唯一关心的事情就是\x01",
            "想方设法地哄抬美术品的价格……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "呼，现在光是回想一下，\x01",
            "就觉得惭愧万分啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_587C")

    label("loc_5834")


    #C0301
    ChrTalk(
        0xD,
        (
            "抱歉，让你们听了一些\x01",
            "我的无聊经历。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "欢迎光临，\x01",
            "请慢慢挑选吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_587C")

    Jump("loc_58F9")

    label("loc_5881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_58F9")

    #C0303
    ChrTalk(
        0xD,
        (
            "欢迎光临，\x01",
            "请随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "本店销售的这些饰品和小物件，\x01",
            "最适合当作礼物送给重要的人，\x01",
            "或是奖励给自己。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58F9")

    Jump("loc_4D96")

    label("loc_58FE")

    TalkEnd(0xD)
    Return()

    # Function_18_4D89 end

    def Function_19_5902(): pass

    label("Function_19_5902")

    SetScenarioFlags(0x2, 4)
    Call(0, 20)
    Return()

    # Function_19_5902 end

    def Function_20_5909(): pass

    label("Function_20_5909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F0")
    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5991")

    #C0305
    ChrTalk(
        0xE,
        (
            "哎，你们到底是从哪里\x01",
            "进来的啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        "算了，无所谓。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xE,
        (
            "如果想买东西的话，\x01",
            "还请绕到柜台前\x01",
            "和我说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_59EC")

    label("loc_5991")


    #C0308
    ChrTalk(
        0xE,
        (
            "如果想买东西的话，\x01",
            "还请绕到柜台前\x01",
            "和我说。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xE,
        (
            "另外，请不要随意触碰\x01",
            "那边的库存品哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59EC")

    TalkEnd(0xE)
    Return()

    label("loc_59F0")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AAB")

    #C0310
    ChrTalk(
        0xE,
        (
            "哟，欢迎光临\x01",
            "『沙扎克杂货柜台』。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        (
            "本店的商品种类非常丰富，\x01",
            "从日用品到土特产，应有尽有哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xE,
        "如果有兴趣，请慢慢看看。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5B06")

    label("loc_5AAB")


    #C0313
    ChrTalk(
        0xE,
        (
            "本店的商品种类非常丰富，\x01",
            "从日用品到土特产，应有尽有哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xE,
        "如果有兴趣，请慢慢看看。\x02",
    )

    CloseMessageWindow()

    label("loc_5B06")

    TalkEnd(0xE)
    Return()

    label("loc_5B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C34")
    SetChrName("")

    #A0315
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向店主沙扎克\x01",
            "小声搭话。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00000F（请问那个\x01",
            "  『咪西座钟』\x01",
            "  多少钱？）\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xE,
        "（哦，５００米拉。）\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xE,
        (
            "（呵呵，莫非是要送给\x01",
            "  那个孩子的礼物吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#00012F（啊，是的，不过还在考虑。）\x02\x03",

            "#00003F（５００米拉啊……\x01",
            "  如何，要买给秦吗？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_5C82")

    label("loc_5C34")


    #C0320
    ChrTalk(
        0xE,
        (
            "（咪西座钟的价格是５００米拉哦，\x01",
            "  要买吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        "#00000F（这个嘛……）\x02",
    )

    CloseMessageWindow()

    label("loc_5C82")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "购买『咪西座钟』\x01",      # 0
            "再考虑一下\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DF1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D4B")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    #C0322
    ChrTalk(
        0x101,
        "#00000F（嗯，请帮我拿一个吧。）\x02",
    )

    CloseMessageWindow()
    Sound(20, 0, 80, 0)

    #C0323
    ChrTalk(
        0xE,
        "（好的，多谢惠顾。）\x02",
    )

    CloseMessageWindow()
    Call(0, 52)
    Jump("loc_5DEC")

    label("loc_5D4B")


    #C0324
    ChrTalk(
        0x101,
        "#00000F（嗯，请帮我拿……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0325
    ChrTalk(
        0x101,
        (
            "#00006F（没钱了……\x01",
            "  呼，我怎么会穷到如此地步。）\x02\x03",

            "#00000F（不好意思，还是不要了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xE,
        "（？？？）\x02",
    )

    CloseMessageWindow()

    label("loc_5DEC")

    Jump("loc_5E19")

    label("loc_5DF1")


    #C0327
    ChrTalk(
        0x101,
        (
            "#00003F（还是再考虑\x01",
            "  一下吧……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E19")

    TalkEnd(0xE)
    Return()

    label("loc_5E22")


    #C0328
    ChrTalk(
        0xE,
        (
            "看来那个礼物\x01",
            "让他很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xE,
        (
            "嗯～咪西果然\x01",
            "伟大啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    label("loc_5E62")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E09")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EBC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5EBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5EDB")
    OP_AF(0x1D)
    Jump("loc_5F5D")

    label("loc_5EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5EEB")
    OP_AF(0x1C)
    Jump("loc_5F5D")

    label("loc_5EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5EFB")
    OP_AF(0x1B)
    Jump("loc_5F5D")

    label("loc_5EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5F0B")
    OP_AF(0x1A)
    Jump("loc_5F5D")

    label("loc_5F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5F1B")
    OP_AF(0x19)
    Jump("loc_5F5D")

    label("loc_5F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F2B")
    OP_AF(0x18)
    Jump("loc_5F5D")

    label("loc_5F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5F3B")
    OP_AF(0x17)
    Jump("loc_5F5D")

    label("loc_5F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5F4B")
    OP_AF(0x16)
    Jump("loc_5F5D")

    label("loc_5F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F5B")
    OP_AF(0x15)
    Jump("loc_5F5D")

    label("loc_5F5B")

    OP_AF(0x14)

    label("loc_5F5D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E04")

    label("loc_5F6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F80")
    Jump("loc_6E04")

    label("loc_5F80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E04")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_602B")

    #C0330
    ChrTalk(
        0xE,
        (
            "身为一名商人，\x01",
            "现在能做的事情\x01",
            "也只有继续营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xE,
        (
            "国外的供货渠道目前\x01",
            "仍然没有恢复的希望……\x01",
            "如今一定要想尽一切办法渡过难关。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E04")

    label("loc_602B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_60AB")

    #C0332
    ChrTalk(
        0xE,
        (
            "在这种时候，有重要的人在\x01",
            "自己的身边，真是让人安心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xE,
        (
            "该怎么说呢，身体中就好像\x01",
            "有无穷的勇气不断涌现呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E04")

    label("loc_60AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F2")

    #C0334
    ChrTalk(
        0xE,
        (
            "今天早上，共和国政府\x01",
            "突然向滞留在克洛斯贝尔的共和国人\x01",
            "下达了紧急归国的催促令。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xE,
        (
            "共和国已经公然表示，不惜用武力来解决问题。\x01",
            "今后将会发生怎样的事态，\x01",
            "已经不难想象了……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xE,
        (
            "我的女友就居住在\x01",
            "克洛斯贝尔，\x01",
            "她是我最重要的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xE,
        (
            "所以我已经下了决心，\x01",
            "无论今后发生什么情况，\x01",
            "我也一定会留在此地。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_623D")

    label("loc_61F2")


    #C0338
    ChrTalk(
        0xE,
        (
            "无论今后发生什么情况，\x01",
            "我也一定会留在此地。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xE,
        "而且一定会保护好她。\x02",
    )

    CloseMessageWindow()

    label("loc_623D")

    Jump("loc_6E04")

    label("loc_6242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_62C8")

    #C0340
    ChrTalk(
        0xE,
        (
            "新版舞剧终于上演，\x01",
            "伊莉娅小姐却遭遇到那种不幸……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xE,
        (
            "在发生袭击的时候，我非常害怕……\x01",
            "但现在唯一的心情就是愤怒！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E04")

    label("loc_62C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_641A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6399")

    #C0342
    ChrTalk(
        0xE,
        (
            "今天晚上，\x01",
            "『金之太阳、银之月』\x01",
            "的新版终于要开演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xE,
        (
            "想想玛因兹那边的状况，\x01",
            "如今似乎不该\x01",
            "太放松……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        (
            "但艺术就是艺术，\x01",
            "就算是为了从中获得勇气与活力，\x01",
            "也一定要全心享受。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6415")

    label("loc_6399")


    #C0345
    ChrTalk(
        0xE,
        (
            "想想玛因兹那边的状况，\x01",
            "如今似乎不该\x01",
            "太放松……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xE,
        (
            "但艺术就是艺术，\x01",
            "就算是为了从中获得勇气与活力，\x01",
            "也一定要全心享受。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6415")

    Jump("loc_6E04")

    label("loc_641A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_64A1")

    #C0347
    ChrTalk(
        0xE,
        (
            "我从前只知道一心经商，\x01",
            "自从有了她之后，\x01",
            "整个世界好像都发生了改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xE,
        (
            "该怎么说才好呢……\x01",
            "这大概就是所谓的幸福吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E04")

    label("loc_64A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_64FC")

    #C0349
    ChrTalk(
        0xE,
        (
            "据说西边好像发生了列车事故，\x01",
            "场面非常混乱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xE,
        "但愿不是恐怖活动……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E04")

    label("loc_64FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A9")

    #C0351
    ChrTalk(
        0xE,
        (
            "调查是否赞成独立的居民投票吗……\x01",
            "虽然只是调查大家的意向，\x01",
            "但真是觉得责任重大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xE,
        (
            "我是共和国人，\x01",
            "所以不能参加投票，\x01",
            "但还是思考了很久呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_660B")

    label("loc_65A9")


    #C0353
    ChrTalk(
        0xE,
        "调查是否赞成独立的居民投票吗……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xE,
        (
            "虽然我是共和国人，\x01",
            "无法参加投票，\x01",
            "但还是思考了很久呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_660B")

    Jump("loc_6E04")

    label("loc_6610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_672D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B6")

    #C0355
    ChrTalk(
        0xE,
        (
            "我一开始只想把珍妮特\x01",
            "当作一个可爱的妹妹……\x01",
            "呼，人的心思真是很难捉摸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "不管怎么说，现在的我非常幸福。\x01",
            "能鼓起勇气，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6728")

    label("loc_66B6")


    #C0357
    ChrTalk(
        0xE,
        (
            "其实我一开始只想把珍妮特\x01",
            "当作一个可爱的妹妹……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xE,
        (
            "不管怎么说，现在的我非常幸福。\x01",
            "能鼓起勇气，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6728")

    Jump("loc_6E04")

    label("loc_672D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BD")

    #C0359
    ChrTalk(
        0xE,
        (
            "珍妮特昨天好像\x01",
            "和几个有钱的男人去吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xE,
        "而且似乎惨遭冷落……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xE,
        "唔～我为什么会有一种松了口气的感觉呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_680D")

    label("loc_67BD")


    #C0362
    ChrTalk(
        0xE,
        "唔～我为什么会有一种松了口气的感觉呢？\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xE,
        "这也就是说，我其实一直对她……\x02",
    )

    CloseMessageWindow()

    label("loc_680D")

    Jump("loc_6E04")

    label("loc_6812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_691A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68CA")

    #C0364
    ChrTalk(
        0xE,
        (
            "珍妮特从今天早上开始\x01",
            "就非常兴奋。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        (
            "而且总是说一些让人\x01",
            "听不懂的话，比如『明天我就要\x01",
            "变成超级珍妮特了』之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xE,
        "不知为什么，我心里非常在意呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6915")

    label("loc_68CA")


    #C0367
    ChrTalk(
        0xE,
        (
            "珍妮特从今天早上开始\x01",
            "就非常兴奋。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xE,
        "不知为什么，我心里非常在意呢。\x02",
    )

    CloseMessageWindow()

    label("loc_6915")

    Jump("loc_6E04")

    label("loc_691A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6A51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E9")

    #C0369
    ChrTalk(
        0xE,
        (
            "揭幕式吗～我虽然没去看，\x01",
            "但一定非常壮观吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xE,
        (
            "平时只有在杂志上才能看到的\x01",
            "各国首脑在那里齐聚一堂，\x01",
            "绝对很震撼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "我从现在就开始强烈期待\x01",
            "下一期的克洛斯贝尔时代周刊了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6A4C")

    label("loc_69E9")


    #C0372
    ChrTalk(
        0xE,
        (
            "揭幕式吗～\x01",
            "一定非常壮观吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xE,
        (
            "呵呵，\x01",
            "我从现在就开始强烈期待\x01",
            "下一期的克洛斯贝尔时代周刊了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A4C")

    Jump("loc_6E04")

    label("loc_6A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE2")

    #C0374
    ChrTalk(
        0xE,
        (
            "你知道吗？\x01",
            "彩虹剧团的舞剧『金之太阳、银之月』\x01",
            "要推出新版了。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xE,
        (
            "虽然还没有公布详情，\x01",
            "但听说好像会增加非常大胆的表演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xE,
        (
            "呵呵呵，而且……\x01",
            "我已经顺利拿到两张\x01",
            "公演初日的门票了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x104,
        (
            "#00305F嘿，那可真让人羡慕啊。\x02\x03",

            "#00309F顺便问一下，你要和谁一起去看？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        "呜……这个问题就别问了吧。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xE,
        (
            "总、总之，距离公演\x01",
            "只剩下一个月了。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xE,
        "在那之前，一定能找到同伴的……嗯。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6C55")

    label("loc_6BE2")


    #C0381
    ChrTalk(
        0xE,
        (
            "我幸运地拿到了两张\x01",
            "彩虹剧团新版舞剧\x01",
            "的公演初日门票。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xE,
        (
            "呼，不过接下来还得找找\x01",
            "到时一起去观赏表演的同伴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C55")

    Jump("loc_6E04")

    label("loc_6C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C75")
    Call(0, 21)
    Jump("loc_6CBA")

    label("loc_6C75")


    #C0383
    ChrTalk(
        0xE,
        (
            "要是生日什么的要礼物，我倒是还可以理解……\x01",
            "平时也追着要礼物……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CBA")

    Jump("loc_6E04")

    label("loc_6CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DB9")

    #C0384
    ChrTalk(
        0xE,
        (
            "哟，欢迎光临\x01",
            "『沙扎克杂货柜台』。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xE,
        (
            "为了满足客人们强烈的要求，\x01",
            "本店最近丰富了咪西的周边产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xE,
        "如果有兴趣，请一定看看哦。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#00002F嘿，咪西的周边吗？\x01",
            "缇欧要是知道了，一定会很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x102,
        "#00102F呵呵，确实呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6E04")

    label("loc_6DB9")


    #C0389
    ChrTalk(
        0xE,
        (
            "托各位的福，\x01",
            "咪西的周边产品大受好评。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        "如果有兴趣，请一定看看哦。\x02",
    )

    CloseMessageWindow()

    label("loc_6E04")

    Jump("loc_5E6C")

    label("loc_6E09")

    TalkEnd(0xE)
    Return()

    # Function_20_5909 end

    def Function_21_6E0D(): pass

    label("Function_21_6E0D")

    OP_4B(0x12, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0391
    ChrTalk(
        0x12,
        (
            "啊，是咪西玩偶，好可爱～\x01",
            "沙扎克先生，我要这个。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        (
            "啊，好的。\x01",
            "嗯，这个５００米拉……\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x12,
        (
            "不是啦，\x01",
            "送我做礼物吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xE,
        "礼物？为什么我要送你礼物？\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x12,
        "因为我们都在同一个百货店工作。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0396
    ChrTalk(
        0xE,
        (
            "不不不，\x01",
            "这并不算理由啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x12, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_21_6E0D end

    def Function_22_6F1B(): pass

    label("Function_22_6F1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7070")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FFF")

    #C0397
    ChrTalk(
        0xFE,
        (
            "戒严令解除之后，刚想松一口气，\x01",
            "就出现了谜一般的大树……\x01",
            "而且两大国的威胁仍然存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "面对如今这种前所未有的困难，\x01",
            "自己究竟能做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "我们每个人都要认真思考这个问题，\x01",
            "并付诸行动。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_706B")

    label("loc_6FFF")


    #C0400
    ChrTalk(
        0xFE,
        (
            "面对如今这种前所未有的困难，\x01",
            "自己究竟能做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "我们每个人都要认真思考这个问题，\x01",
            "并付诸行动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_706B")

    Jump("loc_7EB4")

    label("loc_7070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_70EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_708B")
    Call(0, 23)
    Jump("loc_70E9")

    label("loc_708B")


    #C0402
    ChrTalk(
        0xFE,
        (
            "我会听从罗伊德警官的建议，\x01",
            "继续遵守外出禁令，\x01",
            "观望状况的发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        "……请各位多加小心。\x02",
    )

    CloseMessageWindow()

    label("loc_70E9")

    Jump("loc_7EB4")

    label("loc_70EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7248")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71CF")

    #C0404
    ChrTalk(
        0xFE,
        (
            "居民投票仅仅过去了一周，\x01",
            "事态竟然就发展到了如此地步……\x01",
            "真是让人难以想象啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "总之，今后不管再发生什么，\x01",
            "恐怕也都不足为奇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "就算是为了这家百货店的存续，\x01",
            "也必须要努力思考一切办法啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7243")

    label("loc_71CF")


    #C0407
    ChrTalk(
        0xFE,
        (
            "总之，今后不管再发生什么，\x01",
            "恐怕也都不足为奇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "就算是为了这家百货店的存续，\x01",
            "也必须要努力思考一切办法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7243")

    Jump("loc_7EB4")

    label("loc_7248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_73BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7331")

    #C0409
    ChrTalk(
        0xFE,
        (
            "今天将要在市民会馆召开\x01",
            "以支援城市复兴为主题\x01",
            "的慈善宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "这是市政府与工商协会\x01",
            "为了让市民们打起精神，\x01",
            "重新振作而策划的活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "本百货店也会提供全面协助，\x01",
            "使活动圆满成功，\x01",
            "请各位一定前去参加。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_73B5")

    label("loc_7331")


    #C0412
    ChrTalk(
        0xFE,
        (
            "今天将要在市民会馆召开\x01",
            "以支援城市复兴为主题\x01",
            "的慈善宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "本百货店也会提供全面协助，\x01",
            "使活动圆满成功，\x01",
            "请各位一定前去参加。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73B5")

    Jump("loc_7EB4")

    label("loc_73BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7453")

    #C0414
    ChrTalk(
        0xFE,
        (
            "神秘武装集团占领了玛因兹……\x01",
            "这种情况，就好像战争时代的噩梦\x01",
            "再度重现眼前一样，让人无法忍受。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "总之，希望能尽早\x01",
            "将事态平息下来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB4")

    label("loc_7453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746E")
    Call(0, 26)
    Jump("loc_7593")

    label("loc_746E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7533")

    #C0416
    ChrTalk(
        0xFE,
        (
            "听说昨天那起列车脱轨事故\x01",
            "是由一只巨大恶鬼般的怪物\x01",
            "引起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "另外还有传闻说，\x01",
            "最近有不可思议的大型魔兽\x01",
            "出现在了自治州各地……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "唔……两者之间，莫非有什么\x01",
            "因果关系吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7593")

    label("loc_7533")


    #C0419
    ChrTalk(
        0xFE,
        (
            "巨大恶鬼般的怪物，\x01",
            "还有不可思议的大型魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "唔……两者之间，莫非有什么\x01",
            "因果关系吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7593")

    Jump("loc_7EB4")

    label("loc_7598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7620")

    #C0421
    ChrTalk(
        0xFE,
        (
            "据从车站那边\x01",
            "过来的客人说，\x01",
            "好像是发生了列车脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "虽然不了解详请……\x01",
            "但真是很担心那些\x01",
            "被急救车送走的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB4")

    label("loc_7620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_76BE")

    #C0423
    ChrTalk(
        0xFE,
        (
            "最近，我听很多客人\x01",
            "谈论了有关独立问题的\x01",
            "看法。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "虽然有很多人持积极向前的意见，\x01",
            "但如此公开地无视两大国的意见，\x01",
            "自然也让很多人感到不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB4")

    label("loc_76BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7795")

    #C0425
    ChrTalk(
        0xFE,
        (
            "现在想想，之前那场通商会议\x01",
            "简直就是暴风雨般的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "恐怖分子的袭击自不必说，\x01",
            "更让人震惊的是，\x01",
            "迪塔市长竟然公然提出独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "这项提议将会\x01",
            "引起怎样的国际舆论呢……\x01",
            "今后的形势真让人关注啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB4")

    label("loc_7795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786F")

    #C0428
    ChrTalk(
        0xFE,
        (
            "今天也有很多人\x01",
            "去本百货店的楼顶\x01",
            "眺望兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "多亏如此，很多客人还会顺便购购物，\x01",
            "让我的销售额相当可观。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "更重要的是，这种热闹欢快的\x01",
            "气氛真是让人愉快啊。\x01",
            "我接待客人也觉得很开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_78D6")

    label("loc_786F")


    #C0431
    ChrTalk(
        0xFE,
        (
            "今天也有很多人\x01",
            "去本百货店的楼顶\x01",
            "眺望兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "气氛远比平时热闹欢快，\x01",
            "我接待客人也觉得很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78D6")

    Jump("loc_7EB4")

    label("loc_78DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7956")

    #C0433
    ChrTalk(
        0xFE,
        (
            "本店今天将一如往常，\x01",
            "在２０：００准时\x01",
            "结束营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        (
            "请各位顾客多加注意，\x01",
            "以免漏买商品或遗落随身物品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB4")

    label("loc_7956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A21")

    #C0435
    ChrTalk(
        0xFE,
        (
            "真是惭愧，其实我也混在客人堆里，\x01",
            "观看了揭幕式……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "结果被『兰花塔』的威容\x01",
            "震撼得瞠目结舌。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "不愧是高达四十层的超高层大楼……\x01",
            "的确有资格称为\x01",
            "克洛斯贝尔的新象征啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7A6D")

    label("loc_7A21")


    #C0438
    ChrTalk(
        0xFE,
        (
            "不愧是高达四十层的超高层大楼……\x01",
            "的确有资格称为\x01",
            "克洛斯贝尔的新象征啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A6D")

    Jump("loc_7EB4")

    label("loc_7A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7D1B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B6C")
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    #C0439
    ChrTalk(
        0x11,
        (
            "啊，艾莉大小姐，\x01",
            "您今天带来了稀客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x102,
        (
            "#00100F嗯，我们正在带着这孩子\x01",
            "在市里游览呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x11,
        (
            "原来如此，各位特意光顾本店，\x01",
            "我们深感荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x11,
        (
            "希望大家能在本店度过\x01",
            "愉快的时光。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7BBA")

    label("loc_7B6C")


    #C0443
    ChrTalk(
        0x11,
        (
            "各位特意光顾本店，\x01",
            "真是让人开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x11,
        (
            "希望大家能在本店度过\x01",
            "愉快的时光。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BBA")

    Jump("loc_7D16")

    label("loc_7BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CA8")

    #C0445
    ChrTalk(
        0xFE,
        (
            "通商会议终于要在\x01",
            "明天召开了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州，以及环绕着自治州的\x01",
            "四个国家……各方代表将一同与会。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "回首这数十年来的发展，\x01",
            "这场会议本身便有着\x01",
            "非常重要的历史意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，\x01",
            "感觉真是很兴奋。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7D16")

    label("loc_7CA8")


    #C0449
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州，以及环绕着自治州的\x01",
            "四个国家……各方代表将一同与会。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，\x01",
            "感觉真是很兴奋。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D16")

    Jump("loc_7EB4")

    label("loc_7D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D36")
    Call(0, 24)
    Jump("loc_7DAB")

    label("loc_7D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D48")
    Call(0, 25)
    Jump("loc_7DAB")

    label("loc_7D48")


    #C0451
    ChrTalk(
        0x11,
        (
            "本店为冒雨前来光顾\x01",
            "的客人们准备了一份\x01",
            "不成敬意的小礼品。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x11,
        (
            "请各位今天\x01",
            "尽情享受购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DAB")

    Jump("loc_7EB4")

    label("loc_7DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DCB")
    Call(0, 24)
    Jump("loc_7EB4")

    label("loc_7DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E5C")

    #C0453
    ChrTalk(
        0xFE,
        (
            "衷心感谢\x01",
            "各位今日光临\x01",
            "『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "为了满足各位顾客的需要，\x01",
            "本店准备了各种卖场。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        "请各位尽情享受购物的乐趣。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7EB4")

    label("loc_7E5C")


    #C0456
    ChrTalk(
        0xFE,
        (
            "本百货店为了满足各位顾客的需要，\x01",
            "准备了各种卖场。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "请各位尽情\x01",
            "享受购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EB4")

    TalkEnd(0xFE)
    Return()

    # Function_22_6F1B end

    def Function_23_7EB8(): pass

    label("Function_23_7EB8")

    OP_4B(0x11, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    #C0458
    ChrTalk(
        0x11,
        "艾莉大小姐，还有支援科的各位……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        "莫非外出禁令已经……？\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#00003F不……很遗憾，\x01",
            "还没有解除。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        "是吗……\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x102,
        (
            "#00101F奈斯顿先生，可以说说\x01",
            "百货店的情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x11,
        (
            "嗯，虽然已经下达了戒严令，\x01",
            "但在顾客的要求下，\x01",
            "本店昨天还是开到了正常关店时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x11,
        (
            "就在开店期间，出现了那种雾气，\x01",
            "之后，跑进店里的客人们和\x01",
            "全体职员就一直被困在店里。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x8,
        (
            "过了一晚上，本以为能听到些新消息，\x01",
            "没想到却……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        (
            "政府到底在\x01",
            "想些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#00200F……原来如此，\x01",
            "果然是刻不容缓了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x101,
        (
            "#00001F经理，\x01",
            "我们正在努力平息事态，\x01",
            "已经展开了行动。\x02\x03",

            "请您转告大家，\x01",
            "在外面彻底平静下来之前，\x01",
            "暂时不要出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x11,
        (
            "明白了。\x01",
            "……请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x11,
        (
            "对了，难得相遇，\x01",
            "请大家把这个收下，\x01",
            "代替护身符吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0471
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('圣灵药·改', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0472
    ChrTalk(
        0x102,
        (
            "#00100F奈斯顿经理……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1BB, 4)
    Return()

    # Function_23_7EB8 end

    def Function_24_81FB(): pass

    label("Function_24_81FB")


    #C0473
    ChrTalk(
        0x11,
        (
            "欢迎，\x01",
            "欢迎光临『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x102, 500)
    Sleep(100)

    #C0474
    ChrTalk(
        0x11,
        "这不是艾莉大小姐吗！\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x11,
        (
            "听说您和麦克道尔议长\x01",
            "一起前往各国巡访了，\x01",
            "原来已经回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x102,
        (
            "#00100F嗯，刚回来没几天。\x02\x03",

            "今后我会继续在特别任务支援科工作，\x01",
            "还请您继续关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x11,
        (
            "嗯，当然，\x01",
            "祝您身体健康，一切顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x109,
        (
            "#10105F艾莉小姐，\x01",
            "你认识百货店的经理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#00100F嗯，经理和外公是老相识，\x01",
            "一直都对我很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，不愧是议长家的大小姐……\x01",
            "想必能获得不少优待吧？\x02\x03",

            "比如说，让随行的我们\x01",
            "也受到ＶＩＰ待遇之类的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x105, 500)
    Sleep(100)

    #C0481
    ChrTalk(
        0x11,
        (
            "不，关于这个问题，\x01",
            "大小姐之前还特意叮嘱过我，\x01",
            "一定不要搞特殊待遇。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x11,
        (
            "要像对待其他\x01",
            "客人一样对待大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x102,
        (
            "#00104F呵呵，正是。\x01",
            "很遗憾哦，瓦吉。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x105,
        "#10306F哎呀呀，真是一本正经。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#00000F哈哈，确实有些可惜呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 3)
    Return()

    # Function_24_81FB end

    def Function_25_84EF(): pass

    label("Function_25_84EF")


    #C0486
    ChrTalk(
        0x11,
        (
            "多谢各位在如此天气下\x01",
            "还来光临本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x11,
        "如果可以，请收下这个。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0488
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('痊愈之药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0489
    ChrTalk(
        0x102,
        "#00105F奈斯顿经理，这是……？\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x11,
        (
            "哦，这是我们对\x01",
            "冒雨前来光顾的客人\x01",
            "表示的小小谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x11,
        (
            "此回馈从上个月开始\x01",
            "正式实施，\x01",
            "每天限定一百名客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#00000F原来如此，\x01",
            "这还真是让人开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x109,
        (
            "#10100F嗯，连这下雨天\x01",
            "都让人感到心情愉快了。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x11,
        (
            "谢谢，\x01",
            "各位这样说，是我们的荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x11,
        (
            "那就请大家尽情享受\x01",
            "下雨天的购物吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 4)
    Return()

    # Function_25_84EF end

    def Function_26_86C0(): pass

    label("Function_26_86C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_END)), "loc_87D1")

    #C0496
    ChrTalk(
        0x11,
        "多谢各位今日光临本店。\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x11,
        "如果可以，请收下这个。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0498
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('痊愈之药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0499
    ChrTalk(
        0x101,
        "#00000F哦，是下雨天的礼品啊。\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#00100F谢谢您了。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x11,
        (
            "哪里，\x01",
            "我们才要感谢各位的光顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x11,
        (
            "请大家尽情享受\x01",
            "下雨天的购物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_899E")

    label("loc_87D1")


    #C0503
    ChrTalk(
        0x11,
        (
            "多谢各位在如此天气下\x01",
            "还来光临本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x11,
        "如果可以，请收下这个。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0505
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('痊愈之药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0506
    ChrTalk(
        0x102,
        "#00105F奈斯顿经理，这是……？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x11,
        (
            "哦，这是我们对\x01",
            "冒雨前来光顾的客人\x01",
            "表示的小小谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x11,
        (
            "此回馈从上个月开始\x01",
            "正式实施，\x01",
            "每天限定一百名客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x103,
        (
            "#00200F原来如此，\x01",
            "这还真是让人开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x109,
        (
            "#10100F嗯，连这下雨天\x01",
            "都让人感到心情愉快了。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x11,
        (
            "谢谢，\x01",
            "各位这样说，是我们的荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x11,
        (
            "那就请大家尽情享受\x01",
            "下雨天的购物吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_899E")

    SetScenarioFlags(0x16C, 5)
    Return()

    # Function_26_86C0 end

    def Function_27_89A2(): pass

    label("Function_27_89A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8A33")

    #C0513
    ChrTalk(
        0xFE,
        (
            "为了努力渡过这次的难关，\x01",
            "百货店的职员们\x01",
            "全都充满干劲。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        (
            "我也充满了干劲……\x01",
            "嗯，身为充满干劲的淑女，\x01",
            "我一定会全力加油！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8AAF")

    #C0515
    ChrTalk(
        0xFE,
        (
            "老实说，我其实很不安……\x01",
            "但只要看到沙扎克先生的脸，\x01",
            "心情就平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        "呵呵，真是不可思议的感觉呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8B2E")

    #C0517
    ChrTalk(
        0xFE,
        (
            "沙扎克先生说，\x01",
            "要为了我留在\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        (
            "在这种局势下说这样的话可能不太合适……\x01",
            "但我现在真的非常幸福。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8BB5")

    #C0519
    ChrTalk(
        0xFE,
        (
            "……无论怎么尝试着遗忘，\x01",
            "我都无法忘记彩虹剧团\x01",
            "遭到袭击时的恐怖感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xFE,
        (
            "犯人到底为了什么目的，\x01",
            "才做出那样的事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C6A")

    #C0521
    ChrTalk(
        0xFE,
        (
            "我今天准备早退，\x01",
            "去观赏期待已久的\x01",
            "彩虹剧团新版舞剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "那可是我这段时间\x01",
            "一直苦苦期待的作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        (
            "我准备集中精神，认真观赏，\x01",
            "每个瞬间都不要错过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8CCA")

    label("loc_8C6A")


    #C0524
    ChrTalk(
        0xFE,
        (
            "那可是我这段时间\x01",
            "一直苦苦期待的作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "我准备集中精神，认真观赏，\x01",
            "每个瞬间都不要错过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CCA")

    Jump("loc_9076")

    label("loc_8CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8D57")

    #C0526
    ChrTalk(
        0xFE,
        (
            "明天就是彩虹剧团的舞剧\x01",
            "『金之太阳、银之月』\x01",
            "的新版公演日了。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "我准备和沙扎克先生\x01",
            "一起去看，\x01",
            "现在就开始兴奋了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8DA9")

    #C0528
    ChrTalk(
        0xFE,
        "有、有好多辆急救车开过去了。\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        "真担心被送到医院的那些人……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8E17")

    #C0530
    ChrTalk(
        0xFE,
        (
            "说到底，独立究竟有\x01",
            "什么好处呢？\x01",
            "我不太懂那些复杂的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        "对了，去问问沙扎克先生吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8E25")
    Jump("loc_9076")

    label("loc_8E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EE1")

    #C0532
    ChrTalk(
        0xFE,
        (
            "唉，本以为昨天能顺利\x01",
            "交到男朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "辛茜亚前辈\x01",
            "确实很有魅力啊。\x01",
            "连身为同性的我都被她迷住了……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xFE,
        (
            "但话虽如此，\x01",
            "对我有兴趣的人\x01",
            "怎么就连一个都没有呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8F17")

    label("loc_8EE1")


    #C0535
    ChrTalk(
        0xFE,
        (
            "（沮丧）……\x01",
            "懂得欣赏我的魅力的人\x01",
            "究竟在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F17")

    Jump("loc_9076")

    label("loc_8F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8F67")

    #C0536
    ChrTalk(
        0xFE,
        (
            "服装合体，\x01",
            "妆容完美。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xFE,
        "呵呵呵，今晚的我别具一格哦⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_8F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FD4")

    #C0538
    ChrTalk(
        0xFE,
        (
            "呵呵呵，有些客人\x01",
            "真是很主动呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        (
            "已经好久没参加过联谊了，\x01",
            "快点到晚上吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_901E")

    label("loc_8FD4")


    #C0540
    ChrTalk(
        0xFE,
        (
            "而且对方全都是\x01",
            "在港湾区工作的\x01",
            "商务人士呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xFE,
        "这可真是个好机会啊！\x02",
    )

    CloseMessageWindow()

    label("loc_901E")

    Jump("loc_9076")

    label("loc_9023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9031")
    Jump("loc_9076")

    label("loc_9031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_906D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_904C")
    Call(0, 21)
    Jump("loc_9068")

    label("loc_904C")


    #C0542
    ChrTalk(
        0xFE,
        "哼，沙扎克先生是坏人～\x02",
    )

    CloseMessageWindow()

    label("loc_9068")

    Jump("loc_9076")

    label("loc_906D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9076")

    label("loc_9076")

    TalkEnd(0xFE)
    Return()

    # Function_27_89A2 end

    def Function_28_907A(): pass

    label("Function_28_907A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_90DD")

    #C0543
    ChrTalk(
        0xFE,
        (
            "终于可以出家门了，\x01",
            "结果天上却出现那种东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        (
            "到底……\x01",
            "发生什么事了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_90DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_90EB")
    Jump("loc_973B")

    label("loc_90EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9151")

    #C0545
    ChrTalk(
        0xFE,
        (
            "怎、怎么回事，\x01",
            "难道要发生战争了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        (
            "虽然非常害怕……\x01",
            "但我会保护你的，肯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_9151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_91C7")

    #C0547
    ChrTalk(
        0xFE,
        (
            "之前稍微休息了一阵子，\x01",
            "从今天开始，又要继续购物了。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        (
            "如果我们都不消费，\x01",
            "就无法促进经济回暖嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_91C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9244")

    #C0549
    ChrTalk(
        0xFE,
        (
            "待在家里烦躁又不安，\x01",
            "完全无法平静下来，\x01",
            "所以我今天也来百货店了……\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xFE,
        (
            "但终究无法以愉快的心情\x01",
            "来购物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_9244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_92BE")

    #C0551
    ChrTalk(
        0xFE,
        (
            "列车事故真是可怕的事情啊，\x01",
            "不过幸好这么快就恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xFE,
        (
            "如果物流都瘫痪了，\x01",
            "我就不能像现在这样购物了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_92BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9303")

    #C0553
    ChrTalk(
        0xFE,
        (
            "好像发生了什么骚乱啊，\x01",
            "今天是不是应该早点回去呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_9303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_93A4")

    #C0554
    ChrTalk(
        0xFE,
        (
            "我老公最近总是一个人沉默思索，\x01",
            "好像是对独立方面的问题\x01",
            "有很多想法……\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xFE,
        (
            "算啦，那些复杂的事情就交给老公去想吧。\x01",
            "我只管享受购物的乐趣就行了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_93A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_93F9")

    #C0556
    ChrTalk(
        0xFE,
        "啊，又增加新商品了呢。\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xFE,
        (
            "呼，真不愧是著名的\x01",
            "『时代』百货店啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_93F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9458")

    #C0558
    ChrTalk(
        0xFE,
        "今天好像是正式会议的召开日吧？\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "反正也无法亲身观摩，\x01",
            "就算在意也没有用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_9458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_94EE")

    #C0560
    ChrTalk(
        0xFE,
        "听好了哦，肯。\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        (
            "回家之后，要立刻对爸爸说对不起，\x01",
            "接着就紧紧抱住他。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "不用担心，只要我们两人一起夹击他，\x01",
            "就没什么好怕的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_94EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9552")

    #C0563
    ChrTalk(
        0xFE,
        "刚才的揭幕式真精彩啊！\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "看得我兴奋不已，\x01",
            "购物欲望被刺激出来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_958F")

    label("loc_9552")


    #C0565
    ChrTalk(
        0xFE,
        (
            "好～薪水刚刚到手，\x01",
            "钱包还很鼓呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        "今天就多逛逛吧～\x02",
    )

    CloseMessageWindow()

    label("loc_958F")

    Jump("loc_973B")

    label("loc_9594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_961F")

    #C0567
    ChrTalk(
        0xFE,
        (
            "我一直都在想，\x01",
            "那些想出新商品的人真是很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xFE,
        (
            "一次又一次的想出新的创意，\x01",
            "每次都能牢牢把握住\x01",
            "我们这些消费者的心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973B")

    label("loc_961F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_96D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96A8")

    #C0569
    ChrTalk(
        0xFE,
        (
            "以前每次让肯陪我来购物，\x01",
            "他都会抱怨不休，\x01",
            "但最近却不再抱怨了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        "这就是爱啊～我这个做妈妈的好幸福。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_96D4")

    label("loc_96A8")


    #C0571
    ChrTalk(
        0xFE,
        "有个这么懂事的儿子，做妈妈的真幸福啊。\x02",
    )

    CloseMessageWindow()

    label("loc_96D4")

    Jump("loc_973B")

    label("loc_96D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_973B")

    #C0572
    ChrTalk(
        0xFE,
        "呵呵呵～¤\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xFE,
        (
            "百货店这种地方，真是无论什么时候来，\x01",
            "无论来多少次，都不会觉得腻呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_973B")

    TalkEnd(0xFE)
    Return()

    # Function_28_907A end

    def Function_29_973F(): pass

    label("Function_29_973F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_979E")

    #C0574
    ChrTalk(
        0xFE,
        (
            "树竟然会生长在空中，\x01",
            "这究竟是什么原理啊？\x01",
            "我是在做梦还是看到了幻象呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_979E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_97AC")
    Jump("loc_9F8D")

    label("loc_97AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_97C8")

    #C0575
    ChrTalk(
        0xFE,
        "妈妈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_97C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_980A")

    #C0576
    ChrTalk(
        0xFE,
        (
            "妈妈真是很坚强呢。\x01",
            "不知为何，\x01",
            "连我都有了勇气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_980A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9878")

    #C0577
    ChrTalk(
        0xFE,
        (
            "一向最爱购物的妈妈\x01",
            "今天也显得很没兴致呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "不过，想想玛因兹那边的事情，\x01",
            "这也难怪呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_9878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_98F3")

    #C0579
    ChrTalk(
        0xFE,
        (
            "就算下雨，也无法浇熄\x01",
            "妈妈的购物热情。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xFE,
        (
            "今天还算好了，\x01",
            "有时在大雨天陪她来购物，\x01",
            "我都被淋成落汤鸡了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_98F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_99C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_997B")

    #C0581
    ChrTalk(
        0xFE,
        (
            "急救车的警笛声\x01",
            "可真响啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "如果待在附近，\x01",
            "肯定会非常吵吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        (
            "开车的人是不是\x01",
            "要戴着耳塞才行呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_99C1")

    label("loc_997B")


    #C0584
    ChrTalk(
        0xFE,
        (
            "急救车的警笛声\x01",
            "可真响啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "开车的人是不是\x01",
            "要戴着耳塞才行呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C1")

    Jump("loc_9F8D")

    label("loc_99C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9A70")

    #C0586
    ChrTalk(
        0xFE,
        (
            "大家要是都能像我妈妈那样\x01",
            "开朗乐观地思考问题，\x01",
            "也许就能感到幸福了。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "不过，要是所有人都像妈妈那样，\x01",
            "克洛斯贝尔也许瞬间就会被\x01",
            "帝国或共和国吞并了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_9A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B01")

    #C0588
    ChrTalk(
        0xFE,
        (
            "好，今天就用观察大家\x01",
            "的方式来消磨时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "说起来，杂货店的哥哥\x01",
            "和导购姐姐最近好像很亲密。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        "唔，难道……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9B40")

    label("loc_9B01")


    #C0591
    ChrTalk(
        0xFE,
        (
            "杂货店的哥哥\x01",
            "和导购姐姐最近好像很亲密。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xFE,
        "唔，难道……\x02",
    )

    CloseMessageWindow()

    label("loc_9B40")

    Jump("loc_9F8D")

    label("loc_9B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9C09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BAE")

    #C0593
    ChrTalk(
        0xFE,
        (
            "妈妈昨天的\x01",
            "道歉作战很成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xFE,
        (
            "又是拥抱，又是哭泣……\x01",
            "妈妈真是可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9C04")

    label("loc_9BAE")


    #C0595
    ChrTalk(
        0xFE,
        (
            "妈妈的拥抱和眼泪\x01",
            "让爸爸彻底投降了。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "这就是男人在心爱之人\x01",
            "面前的最大弱点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C04")

    Jump("loc_9F8D")

    label("loc_9C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9C7F")

    #C0597
    ChrTalk(
        0xFE,
        (
            "妈妈在购物时太过投入了，\x01",
            "不知不觉拖到了这个时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        (
            "就算是好脾气的爸爸，\x01",
            "这次大概也要生气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_9C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D10")

    #C0599
    ChrTalk(
        0xFE,
        "揭幕式真是精彩。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        (
            "……但我真担心妈妈的情绪\x01",
            "因此而高涨起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "希望她不要失去理智，\x01",
            "乱买一些没用的东西……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9D64")

    label("loc_9D10")


    #C0602
    ChrTalk(
        0xFE,
        (
            "妈妈今天的眼神\x01",
            "好像不太正常。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xFE,
        (
            "希望她不要失去理智，\x01",
            "乱买一些没用的东西……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D64")

    Jump("loc_9F8D")

    label("loc_9D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9DE8")

    #C0604
    ChrTalk(
        0xFE,
        (
            "我一直都在想，\x01",
            "那些想出新商品的人真是很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        (
            "为了吸引像妈妈这样的人，\x01",
            "必须要不断思考各种\x01",
            "新的创意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_9DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9ED1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E89")

    #C0606
    ChrTalk(
        0xFE,
        (
            "我为了打发无聊的时间，想出了不少办法，\x01",
            "其中之一就是观察大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        (
            "百货店里有各种各样的人，\x01",
            "观察他们很有意思，怎么看都看不够呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9ECC")

    label("loc_9E89")


    #C0608
    ChrTalk(
        0xFE,
        (
            "百货店里有各种各样的人，\x01",
            "观察他们很有意思，怎么看都看不够呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ECC")

    Jump("loc_9F8D")

    label("loc_9ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F3E")

    #C0609
    ChrTalk(
        0xFE,
        (
            "哎？一副度假装扮\x01",
            "的红发男人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xFE,
        (
            "刚才好像有个\x01",
            "那样的人跑到\x01",
            "楼顶去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8D")

    label("loc_9F3E")


    #C0611
    ChrTalk(
        0xFE,
        (
            "陪妈妈逛商场\x01",
            "是我每天的固定任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        "虽然已经习惯了，但还是觉得很无聊。\x02",
    )

    CloseMessageWindow()

    label("loc_9F8D")

    TalkEnd(0xFE)
    Return()

    # Function_29_973F end

    def Function_30_9F91(): pass

    label("Function_30_9F91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A01A")

    #C0613
    ChrTalk(
        0xFE,
        (
            "突然出现，并浮在空中的巨树吗……\x01",
            "虽然现在似乎还没有\x01",
            "引发什么问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xFE,
        (
            "……但还是希望\x01",
            "那种诡异的东西\x01",
            "尽快消失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A01A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A028")
    Jump("loc_A729")

    label("loc_A028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A05B")

    #C0615
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "真是非同寻常的事态啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A05B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A0F2")

    #C0616
    ChrTalk(
        0xFE,
        (
            "唔，事到如今，\x01",
            "就算撤回独立宣言，\x01",
            "两大国也未必会信任我们了……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "但话又说回来，如果选择独立，\x01",
            "两大国的军事威胁实在是不容忽视……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A0F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A180")

    #C0618
    ChrTalk(
        0xFE,
        (
            "唔，就算真的独立，\x01",
            "军队能否对抗两大国\x01",
            "也是个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "比如说帝国的列车炮……\x01",
            "光是拿出一门来，\x01",
            "克洛斯贝尔便难以抵御了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A1EF")

    #C0620
    ChrTalk(
        0xFE,
        "我也听说了那个看起来像鬼一样的怪物……\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        (
            "有生以来，还是第一次\x01",
            "听到这种不可思议的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A1EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A228")

    #C0622
    ChrTalk(
        0xFE,
        (
            "外面好像很吵闹啊，\x01",
            "到底发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A29A")

    #C0623
    ChrTalk(
        0xFE,
        (
            "唔，差不多也该好好考虑\x01",
            "送给老伴的新礼物了。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "上次已经送过胸针了……\x01",
            "这次索性就送枚戒指吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A320")

    #C0625
    ChrTalk(
        0xFE,
        (
            "都已经这么一大把年纪了，\x01",
            "没想到还会听到独立这个词啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "如果能顺利实现，自然再好不过，\x01",
            "但恐怕不会有那么简单……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A3AA")

    #C0627
    ChrTalk(
        0xFE,
        (
            "唔，说到会议的最大问题，\x01",
            "也就是奥斯本和洛克史密斯这两人了……\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        (
            "面对那种厚颜无耻的对手，\x01",
            "市长究竟准备了什么对策呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_A3FC")

    #C0629
    ChrTalk(
        0xFE,
        "好，差不多也该动身回家了。\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xFE,
        "要是惹恼了老婆子，可就糟糕啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A492")

    #C0631
    ChrTalk(
        0xFE,
        (
            "呵呵，这间百货店的楼顶\x01",
            "可真是观赏兰花塔的绝佳场所啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "兰花塔揭幕亮相的那一瞬间真是壮丽至极，\x01",
            "当时的景象让人完全无法移开目光。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A586")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A535")

    #C0633
    ChrTalk(
        0xFE,
        (
            "通商会议终于要在\x01",
            "明天正式开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        (
            "听说库罗伊斯市长\x01",
            "有意召开会议的时候，\x01",
            "我真是大吃一惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        (
            "没想到会议\x01",
            "还真要顺利召开了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A581")

    label("loc_A535")


    #C0636
    ChrTalk(
        0xFE,
        (
            "没想到通商会议\x01",
            "真要顺利召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        (
            "真不愧是兼任着ＩＢＣ\x01",
            "总裁的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A581")

    Jump("loc_A729")

    label("loc_A586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A5F4")

    #C0638
    ChrTalk(
        0xFE,
        (
            "唔，这家店的东西真不错，\x01",
            "无论什么时候来看都让人心动。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xFE,
        (
            "呵呵，不然再给老伴\x01",
            "挑件礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A729")

    label("loc_A5F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6C3")

    #C0640
    ChrTalk(
        0xFE,
        (
            "唔，话说回来，\x01",
            "库罗伊斯市长和麦克道尔议长的\x01",
            "活跃表现真是有目共睹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xFE,
        (
            "特别是议长，年纪和我相差无几，\x01",
            "却仍然那么能干……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        (
            "呵呵呵，老当益壮这个词\x01",
            "就是形容他这样的人吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A729")

    label("loc_A6C3")


    #C0643
    ChrTalk(
        0xFE,
        (
            "呵呵呵，老当益壮这个词\x01",
            "就是形容他这样的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xFE,
        (
            "麦克道尔议长可真是我们\x01",
            "这些老年人中的大明星。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A729")

    TalkEnd(0xFE)
    Return()

    # Function_30_9F91 end

    def Function_31_A72D(): pass

    label("Function_31_A72D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A73E")
    Jump("loc_A8C3")

    label("loc_A73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A7C1")

    #C0645
    ChrTalk(
        0xFE,
        (
            "话说回来，虽然知道有戒严令，\x01",
            "但真没想到事态会\x01",
            "发展到如此地步啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xFE,
        (
            "呼……早知如此，\x01",
            "真应该老老实实地回家啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C3")

    label("loc_A7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A837")

    #C0647
    ChrTalk(
        0xFE,
        (
            "不管怎么说，只要独立了，\x01",
            "就不用再向帝国和共和国交税了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xFE,
        (
            "总之，迪塔先生的主张\x01",
            "应该是没错的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C3")

    label("loc_A837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A870")

    #C0649
    ChrTalk(
        0xFE,
        (
            "下雨天还有礼品送，\x01",
            "百货店还真大方嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C3")

    label("loc_A870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A8C3")

    #C0650
    ChrTalk(
        0xFE,
        (
            "作业～？\x01",
            "谁会做那种东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "亚里欧斯先生好像又出差了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C3")

    TalkEnd(0xFE)
    Return()

    # Function_31_A72D end

    def Function_32_A8C7(): pass

    label("Function_32_A8C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A8D8")
    Jump("loc_A9E7")

    label("loc_A8D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A92D")

    #C0652
    ChrTalk(
        0xFE,
        (
            "虽然见不到家人\x01",
            "有些寂寞……\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "但这种情况下，在哪里不都一样吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9E7")

    label("loc_A92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A984")

    #C0654
    ChrTalk(
        0xFE,
        (
            "大人们最近总是说\x01",
            "什么独立独立的，烦死了……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        "那到底是什么意思？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9E7")

    label("loc_A984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A9E7")

    #C0656
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "那个人原来是经理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        (
            "如此身份的人，竟然还亲自\x01",
            "接待客人，真是了不起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9E7")

    TalkEnd(0xFE)
    Return()

    # Function_32_A8C7 end

    def Function_33_A9EB(): pass

    label("Function_33_A9EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA00")
    Call(0, 36)
    Jump("loc_AA60")

    label("loc_AA00")


    #C0658
    ChrTalk(
        0xFE,
        (
            "……嗯？你们好像是警察局\x01",
            "那个什么科的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        (
            "哼，一边去，\x01",
            "不要随随便便地过来和我搭话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA60")

    TalkEnd(0xFE)
    Return()

    # Function_33_A9EB end

    def Function_34_AA64(): pass

    label("Function_34_AA64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA79")
    Call(0, 36)
    Jump("loc_AAD3")

    label("loc_AA79")


    #C0660
    ChrTalk(
        0xFE,
        (
            "嗯嗯，难得来旅行，\x01",
            "不找些刺激怎么行。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xFE,
        (
            "嘿嘿，不然就去后巷那家\x01",
            "奇怪的店里看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAD3")

    TalkEnd(0xFE)
    Return()

    # Function_34_AA64 end

    def Function_35_AAD7(): pass

    label("Function_35_AAD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAEC")
    Call(0, 36)
    Jump("loc_AB40")

    label("loc_AAEC")


    #C0662
    ChrTalk(
        0xFE,
        (
            "喂喂，稍后也去\x01",
            "导力商店看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xFE,
        (
            "难得过来一次，我想把导力车\x01",
            "尽量改造一番。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB40")

    TalkEnd(0xFE)
    Return()

    # Function_35_AAD7 end

    def Function_36_AB44(): pass

    label("Function_36_AB44")

    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)
    OP_4B(0x19, 0xFF)

    #C0664
    ChrTalk(
        0x17,
        (
            "哎呀呀……\x01",
            "贸易都市的百货店\x01",
            "也不过如此嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x18,
        (
            "嗯，几乎就没有\x01",
            "我们能看得上眼\x01",
            "的东西嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x19,
        (
            "算啦，毕竟都是些面向\x01",
            "庶民的商品，\x01",
            "也就这种档次了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x19,
        (
            "今天也和平时一样，\x01",
            "随便买些下酒菜回去算了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC3E")
    Jump("loc_ACDB")

    label("loc_AC3E")


    #C0668
    ChrTalk(
        0x104,
        (
            "#00301F（啊，他们就是你们说的\x01",
            "  那些目中无人的公子哥吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x102,
        (
            "#00106F（真是的，\x01",
            "  竟然聚在这种地方……）\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#00003F（……算了，这次就别管他们了。）\x02",
    )

    CloseMessageWindow()

    label("loc_ACDB")

    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_36_AB44 end

    def Function_37_ACF0(): pass

    label("Function_37_ACF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AD47")

    #C0671
    ChrTalk(
        0xFE,
        (
            "家里的零食已经\x01",
            "吃光了，\x01",
            "所以我赶快过来买。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        "我也真够粗心的～\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADA4")

    label("loc_AD47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_ADA4")

    #C0673
    ChrTalk(
        0xFE,
        (
            "零食这种东西，\x01",
            "必须要在有空时提前买好才行⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xFE,
        (
            "如果想吃时没有，\x01",
            "可就糟糕了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADA4")

    TalkEnd(0xFE)
    Return()

    # Function_37_ACF0 end

    def Function_38_ADA8(): pass

    label("Function_38_ADA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AE4B")

    #C0675
    ChrTalk(
        0xFE,
        (
            "虽说出现了那种夸张的巨树，\x01",
            "但恢复自由真好啊。\x01",
            "戒严令解除之前，我都快憋闷死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xFE,
        (
            "嘿嘿，难得可以自由行动了，\x01",
            "不然去给希伦姐\x01",
            "送些慰问品吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_AE4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AE59")
    Jump("loc_B60E")

    label("loc_AE59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AEE5")

    #C0677
    ChrTalk(
        0xFE,
        (
            "原因不明的奇怪事故吗……\x01",
            "的确发生过那样的\x01",
            "事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0xFE,
        (
            "我们一直都对此视而不见，\x01",
            "也应该承担责任……\x01",
            "总统说的确实没错啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_AEE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AF54")

    #C0679
    ChrTalk(
        0xFE,
        (
            "不用说，\x01",
            "乌尔斯拉医院现在非常忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0xFE,
        (
            "希伦姐姐好像\x01",
            "很消沉，\x01",
            "我却什么都做不了，真是没用啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_AF54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B06E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFFC")

    #C0681
    ChrTalk(
        0xFE,
        "玛、玛因兹居然遭到袭击了！\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xFE,
        (
            "听说从昨天开始，\x01",
            "就有很多警备队员\x01",
            "被送往医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xFE,
        (
            "可恶，那些家伙为什么\x01",
            "要做出这种毫无益处的蠢事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_B069")

    label("loc_AFFC")


    #C0684
    ChrTalk(
        0xFE,
        (
            "听说从昨天开始，\x01",
            "就有很多警备队员\x01",
            "被送往医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0xFE,
        (
            "可恶，那些家伙为什么\x01",
            "要做出这种毫无益处的蠢事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B069")

    Jump("loc_B60E")

    label("loc_B06E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B10E")

    #C0686
    ChrTalk(
        0xFE,
        (
            "被卷入列车事故的人当中，\x01",
            "虽然也有身受重伤的……\x01",
            "但至少所有人都保住了性命。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0xFE,
        (
            "听说医生们通宵工作，\x01",
            "全力救治伤员，\x01",
            "他们可真是大家的楷模啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_B10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B155")

    #C0688
    ChrTalk(
        0xFE,
        (
            "嗯，怎么回事？急救车……？\x01",
            "而且好像开过去很多辆……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_B155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B1D3")

    #C0689
    ChrTalk(
        0xFE,
        "嗯，我今天是来替家人买东西的。\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0xFE,
        (
            "嘿嘿，都这么大年纪了，\x01",
            "还要靠父母养着，\x01",
            "至少也得帮他们跑腿买买东西嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_B1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2E4")

    #C0691
    ChrTalk(
        0xFE,
        (
            "希伦姐姐建议我\x01",
            "从事男性护士的职业，\x01",
            "我认真考虑了她的意见。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0xFE,
        (
            "虽然要等到明年\x01",
            "才能参加护士资格考试，\x01",
            "但我已经在模拟考试中取得了不错的成绩。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0xFE,
        (
            "另外，我还打算继续参加\x01",
            "明年的实习医生考试。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0xFE,
        (
            "未来的路又不是只有一条，\x01",
            "想到这里也就轻松了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_B34C")

    label("loc_B2E4")


    #C0695
    ChrTalk(
        0xFE,
        (
            "人必须要一直向前看，\x01",
            "才能不断进步啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0xFE,
        (
            "总觉得连学习也比以前有趣了呢。\x01",
            "……虽然只有一点点而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B34C")

    Jump("loc_B60E")

    label("loc_B351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B35F")
    Jump("loc_B60E")

    label("loc_B35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B36D")
    Jump("loc_B60E")

    label("loc_B36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B3F5")

    #C0697
    ChrTalk(
        0xFE,
        (
            "由于揭幕式的缘故，\x01",
            "市里的人全都兴高采烈……\x01",
            "但我却非常消沉。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0xFE,
        (
            "真羡慕希伦姐\x01",
            "那乐天的性格啊。\x01",
            "我们真不像是亲姐弟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_B3F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B47F")

    #C0699
    ChrTalk(
        0xFE,
        "唉，还要再过一年重考生活啊。\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0xFE,
        (
            "最近这段时间，总觉得家人看我的\x01",
            "眼光变得越来越冷淡了……\x01",
            "呼，我的人生到底该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_B47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B51D")

    #C0701
    ChrTalk(
        0xFE,
        (
            "嗯……今天要买的东西有\x01",
            "黑胡椒、芥末酱汁，\x01",
            "还有橄榄油……\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0xFE,
        (
            "呼，让我买的东西，\x01",
            "不用做笔记我也都可以记住。\x01",
            "真想把这记忆力用在学习方面啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60E")

    label("loc_B51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B60E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5B1")

    #C0703
    ChrTalk(
        0xFE,
        (
            "我又参加了乌尔斯拉医院的实习医生考试，\x01",
            "结果今年还是没通过。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0xFE,
        (
            "虽然我还想\x01",
            "挑战第三次……\x01",
            "但显然还是没什么希望吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_B60E")

    label("loc_B5B1")


    #C0705
    ChrTalk(
        0xFE,
        (
            "我如此没用，在家里自然身份低微，\x01",
            "今天也要跑腿买东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0xFE,
        "呼，我可真是个没用的人啊。\x02",
    )

    CloseMessageWindow()

    label("loc_B60E")

    TalkEnd(0xFE)
    Return()

    # Function_38_ADA8 end

    def Function_39_B612(): pass

    label("Function_39_B612")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B6AF")

    #C0707
    ChrTalk(
        0xFE,
        (
            "我想要Ｌ尺寸\x01",
            "的咪西，\x01",
            "但实在是承受不起那个价格啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0xFE,
        (
            "是攒下零钱买Ｌ尺寸呢，\x01",
            "还是现在就用手里的钱买个Ｓ尺寸呢……\x01",
            "唔～真让人烦恼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6FF")

    label("loc_B6AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B6FF")

    #C0709
    ChrTalk(
        0xFE,
        (
            "原来杂货店真的\x01",
            "增设了咪西专柜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xFE,
        "以、以后一定要经常来看看。\x02",
    )

    CloseMessageWindow()

    label("loc_B6FF")

    TalkEnd(0xFE)
    Return()

    # Function_39_B612 end

    def Function_40_B703(): pass

    label("Function_40_B703")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B762")

    #C0711
    ChrTalk(
        0xFE,
        (
            "好了，买完特产之后，\x01",
            "就该前往空港了。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0xFE,
        (
            "嗯～这次的旅行\x01",
            "也很有意义呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B827")

    label("loc_B762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B770")
    Jump("loc_B827")

    label("loc_B770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B7C1")

    #C0713
    ChrTalk(
        0xFE,
        (
            "嗯～揭幕式\x01",
            "比我想象中的还要精彩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0xFE,
        "不愧是克洛斯贝尔啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B827")

    label("loc_B7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B827")

    #C0715
    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "克洛斯贝尔果然是个好地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xFE,
        (
            "明天还有\x01",
            "兰花塔的揭幕式，\x01",
            "这次的旅行一定会很愉快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B827")

    TalkEnd(0xFE)
    Return()

    # Function_40_B703 end

    def Function_41_B82B(): pass

    label("Function_41_B82B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B874")

    #C0717
    ChrTalk(
        0xFE,
        (
            "唉～这次的旅行\x01",
            "就到此结束了吗。\x01",
            "感觉还真是短暂啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B930")

    label("loc_B874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B882")
    Jump("loc_B930")

    label("loc_B882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B8E4")

    #C0718
    ChrTalk(
        0xFE,
        (
            "这间百货店的屋顶真是\x01",
            "观赏揭幕式的好地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xFE,
        (
            "呵呵，还好我事先\x01",
            "好好调查过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B930")

    label("loc_B8E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B930")

    #C0720
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔\x01",
            "真是个刺激的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0xFE,
        "无论来多少次也都不会腻。\x02",
    )

    CloseMessageWindow()

    label("loc_B930")

    TalkEnd(0xFE)
    Return()

    # Function_41_B82B end

    def Function_42_B934(): pass

    label("Function_42_B934")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9E9")

    #C0722
    ChrTalk(
        0xFE,
        (
            "嗯，奈斯顿经理的话\x01",
            "真是意味深长呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xFE,
        (
            "无论是作为企业家，还是作为商人，\x01",
            "我都还远远不够成熟……\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xFE,
        (
            "但即使如此，\x01",
            "我也想为克洛斯贝尔\x01",
            "贡献自己的一份力量。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_BA60")

    label("loc_B9E9")


    #C0725
    ChrTalk(
        0xFE,
        (
            "无论是作为企业家，还是作为商人，\x01",
            "我都还远远不够成熟……\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0xFE,
        (
            "但即使如此，\x01",
            "我也想为克洛斯贝尔\x01",
            "贡献自己的一份力量。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA60")

    TalkEnd(0xFE)
    Return()

    # Function_42_B934 end

    def Function_43_BA64(): pass

    label("Function_43_BA64")

    TalkBegin(0xFE)

    #C0727
    ChrTalk(
        0xFE,
        (
            "为了准备今天的晚餐，\x01",
            "我买了不少东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xFE,
        (
            "外面很吵闹……\x01",
            "似乎发生什么事了吧？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_BA64 end

    def Function_44_BABF(): pass

    label("Function_44_BABF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BB37")

    #C0729
    ChrTalk(
        0xFE,
        (
            "恐怖分子很有可能会\x01",
            "向正式会议的会场发动袭击～\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "万一和他们开战的话，\x01",
            "应该不会输吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C01B")

    label("loc_BB37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BC2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBD6")

    #C0731
    ChrTalk(
        0xFE,
        (
            "呼，今天的人流\x01",
            "真是相当惊人啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xFE,
        (
            "可惜实在太忙了，\x01",
            "连欣赏美人的时间都没有～\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        (
            "#00012F（嗯～雷蒙德警官\x01",
            "  还是老样子呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_BC2A")

    label("loc_BBD6")


    #C0734
    ChrTalk(
        0xFE,
        (
            "呼，今天的人流\x01",
            "真是相当惊人啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0xFE,
        (
            "可惜实在太忙了，\x01",
            "连欣赏美人的时间都没有～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC2A")

    Jump("loc_C01B")

    label("loc_BC2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BDBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD63")

    #C0736
    ChrTalk(
        0xFE,
        (
            "哦，这孩子是……\x01",
            "莫非你们正在带\x01",
            "迷路的孩子找家人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0737
    ChrTalk(
        0x1A2,
        "……谁是迷路的孩子。\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x1A2,
        (
            "我只是正在参观\x01",
            "克洛斯贝尔而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A2, 500)

    #C0739
    ChrTalk(
        0xFE,
        "哎，参观～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0740
    ChrTalk(
        0xFE,
        (
            "这也是支援请求吗？\x01",
            "支援科的工作还真是辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        "#00000F哈哈，还好吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_BDB6")

    label("loc_BD63")


    #C0742
    ChrTalk(
        0xFE,
        (
            "总之，今天只是\x01",
            "警备体制开始的第一天。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xFE,
        (
            "不用太过拼命，\x01",
            "差不多也就\x01",
            "行了吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDB6")

    Jump("loc_C01B")

    label("loc_BDBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF2E")

    #C0744
    ChrTalk(
        0xFE,
        (
            "哦，是你们～\x01",
            "咱们好像都很辛苦呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        (
            "#00003F嗯，是啊，\x01",
            "现在毕竟是特殊时期。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x102,
        (
            "#00100F您负责百货店\x01",
            "的警备工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0xFE,
        (
            "嗯，严格来说，是负责\x01",
            "中央广场的所有商业设施～\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xFE,
        (
            "在这里可以看到不少美人，\x01",
            "工作时真是很有干劲呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x102,
        "#00105F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x109,
        (
            "#10106F（唔～动机真是\x01",
            "  相当不纯呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x104,
        (
            "#00309F（哈哈，算啦，\x01",
            "  只要能保持干劲\x01",
            "  就好了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_C01B")

    label("loc_BF2E")


    #C0752
    ChrTalk(
        0xFE,
        (
            "警备工作让我肩膀酸痛～\x01",
            "但只要看到美人，疲劳一下就消失了～\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0xFE,
        (
            "至今为止看到的美人一共有三十一人……\x01",
            "嗯嗯嗯～看来可以期待出现更多啊。\x02",
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

    label("loc_C01B")

    TalkEnd(0xFE)
    Return()

    # Function_44_BABF end

    def Function_45_C01F(): pass

    label("Function_45_C01F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C034")
    Call(0, 46)
    Jump("loc_C06B")

    label("loc_C034")


    #C0754
    ChrTalk(
        0x21,
        (
            "#00603F我正要试穿\x01",
            "定制的鞋。\x02\x03",

            "#00600F不要打扰我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C06B")

    TalkEnd(0xFE)
    Return()

    # Function_45_C01F end

    def Function_46_C06F(): pass

    label("Function_46_C06F")

    EventBegin(0x0)
    Fade(500)
    OP_68(-90, 8900, 27440, 0)
    MoveCamera(70, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17690, 0)
    SetChrPos(0x101, -1280, 8029, 26410, 74)
    SetChrPos(0x102, -1420, 8029, 27490, 74)
    SetChrPos(0x103, -2650, 8000, 26650, 74)
    SetChrPos(0x104, -2690, 8000, 27740, 74)
    SetChrPos(0x109, -3700, 8000, 27000, 74)
    SetChrPos(0x105, -3320, 8000, 25680, 74)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0x21, 0x13B, 0x0)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x14, 0x0)
    OP_0D()

    #C0755
    ChrTalk(
        0xA,
        (
            "达德利先生，\x01",
            "这是您定的鞋。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x21,
        "#11P#00602F嗯，我这就试穿……\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x21, 0x101, 500)

    #C0757
    ChrTalk(
        0x21,
        (
            "#11P#00600F哦，是你们，\x01",
            "在这种地方做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x101,
        "#12P#00000F这个……\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        (
            "#6P#00306F那正是我们\x01",
            "想问的问题啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0760
    ChrTalk(
        0x105,
        (
            "#12P#10305F嘿，好像\x01",
            "相当高级呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x102,
        (
            "#6P#00100F是皮鞋啊……\x01",
            "好像还是名牌吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x21,
        (
            "#11P#00603F哼，不要把我\x01",
            "和那种仅仅满足于名牌\x01",
            "的家伙相提并论。\x02\x03",

            "#00602F……这可是专门定制的鞋。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x109,
        (
            "#6P#10100F呵呵，看来您很\x01",
            "讲究这些呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x101,
        (
            "#12P#00005F是特别定制的皮鞋啊……\x02\x03",

            "#00003F我平时基本只穿\x01",
            "运动鞋呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    #C0765
    ChrTalk(
        0x21,
        (
            "#11P#00601F……班宁斯，\x01",
            "你到底想说什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0766
    ChrTalk(
        0x101,
        "#12P#00000F哎……？\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x21,
        (
            "#11P#00600F听你那口气，\x01",
            "似乎是对皮鞋不屑一顾吧？\x02\x03",

            "#00603F不过……\x01",
            "你这种想法可是大错特错。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        "#12P#00011F我、我并没有……\x02",
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x21,
        (
            "#11P#00602F说到鞋子，\x01",
            "没有比皮革更有内涵的材料了。\x02\x03",

            "#00604F越穿就越是合脚，\x01",
            "而且只要悉心护理，\x01",
            "触感会越来越好……\x02\x03",

            "#00601F你能从运动鞋中感受到\x01",
            "这种深奥的绝妙滋味吗？\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0770
    ChrTalk(
        0x103,
        "#6P#00206F不知为何，他好像相当激动呢……\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x102,
        "#6P#00109F嗯，老实说，这真是很意外啊。\x02",
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x21,
        (
            "#11P#00606F咳、咳咳……\x01",
            "好像有点扯远了。\x02\x03",

            "#00600F总之，我只在偶尔有空时\x01",
            "才会来这里。\x02\x03",

            "稍后自然还有很多预定安排，\x01",
            "所以你们不要打扰我。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x101,
        "#12P#00012F知、知道了……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0xA, 0xFF)
    OP_4C(0x21, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0x21, 0x13B, 0x0)
    SetScenarioFlags(0x171, 4)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 13800, 8000, 6200, 225)
    BeginChrThread(0x14, 0, 0, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1700, 8029, 27020, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_46_C06F end

    def Function_47_C706(): pass

    label("Function_47_C706")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C767")

    #C0774
    ChrTalk(
        0x1B,
        (
            "#02106F好的好的，知道啦。\x02\x03",

            "#02109F总之，我必须要用\x01",
            "这里某个品牌\x01",
            "的笔。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_C7BB")

    label("loc_C767")


    #C0775
    ChrTalk(
        0x1B,
        (
            "#02105F嘿～出了一些\x01",
            "新型的增强产品呢。\x02\x03",

            "#02109F嗯嗯，不然也试试\x01",
            "这种类型的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7BB")

    TalkEnd(0xFE)
    Return()

    # Function_47_C706 end

    def Function_48_C7BF(): pass

    label("Function_48_C7BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C87D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C81E")

    #C0776
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈，\x01",
            "请快点啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0xFE,
        (
            "买个东西为什么\x01",
            "这么慢啊～\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x2, 0)
    Jump("loc_C878")

    label("loc_C81E")


    #C0778
    ChrTalk(
        0xFE,
        (
            "呼，墨水突然用完了，\x01",
            "所以过来买……\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0xFE,
        (
            "时间还充裕得很，\x01",
            "但不知为什么，总是很不安～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C878")

    Jump("loc_C941")

    label("loc_C87D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C941")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C903")

    #C0780
    ChrTalk(
        0xFE,
        (
            "嗯……回复药，解毒药，\x01",
            "还需要苏醒药……\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#00005F（在准备医疗用品啊……\x01",
            "  似乎是要去什么地方吧？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_C941")

    label("loc_C903")


    #C0782
    ChrTalk(
        0xFE,
        (
            "ＥＰ填充剂……\x01",
            "似乎不需要。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0xFE,
        (
            "接下来还要准备\x01",
            "烟雾弹。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C941")

    TalkEnd(0xFE)
    Return()

    # Function_48_C7BF end

    def Function_49_C945(): pass

    label("Function_49_C945")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0784
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２Ｆ　『卢卡』时装店\x01",
            "２Ｆ　『汉森』鞋店\x01",
            "２Ｆ　『贝卡』饰品店\x01",
            "１Ｆ　『利乔』食品店\x01",
            "１Ｆ　『沙扎克』杂货柜台\x02",
        )
    )

    CloseMessageWindow()

    #A0785
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※若有不明之处，\x01",
            "　敬请随时咨询\x01",
            "  正门综合服务台。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_49_C945 end

    def Function_50_CA19(): pass

    label("Function_50_CA19")

    EventBegin(0x0)
    Fade(500)
    OP_68(-15210, 1000, 9790, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CAA0")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x104, -14350, 0, 8000, 0)
    Jump("loc_CB3F")

    label("loc_CAA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CAF2")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x109, -14350, 0, 8000, 0)
    Jump("loc_CB3F")

    label("loc_CAF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CB3F")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x105, -14350, 0, 8000, 0)

    label("loc_CB3F")

    OP_0D()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0786
    ChrTalk(
        0x1A2,
        (
            "#12P这、这不是\x01",
            "『咪西玩偶』吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x1A2,
        (
            "#12P怎么回事？\x01",
            "这里并不是主题公园啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，听说是最近增设的\x01",
            "咪西专柜哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x101,
        (
            "#12P#00000F秦，你对\x01",
            "咪西有兴趣？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0790
    ChrTalk(
        0x1A2,
        (
            "你、你这家伙……\x01",
            "难道想侮辱我吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x1A2,
        (
            "身为背负着黑月未来的男人，\x01",
            "我怎么可能会喜欢那种东西……\x01",
            "无礼也要有个限度！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CD85")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_CCFB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CCFB)
    Sleep(50)

    def lambda_CD0B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CD0B)
    Sleep(300)

    #C0792
    ChrTalk(
        0x102,
        "#00105F秦……？\x02",
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x101,
        "#12P#00006F用不着那么生气吧……\x02",
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x104,
        (
            "#12P#00309F嗯，而且这和黑月\x01",
            "完全没关系啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF4C")

    label("loc_CD85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CE6C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_CDDE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CDDE)
    Sleep(50)

    def lambda_CDEE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CDEE)
    Sleep(300)

    #C0795
    ChrTalk(
        0x102,
        "#00105F秦……？\x02",
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        "#12P#00006F用不着那么生气吧……\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x109,
        (
            "#12P#10102F是啊，而且这和黑月\x01",
            "完全没有关系呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF4C")

    label("loc_CE6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CF4C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_CEC5():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CEC5)
    Sleep(50)

    def lambda_CED5():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CED5)
    Sleep(300)

    #C0798
    ChrTalk(
        0x102,
        "#00105F秦……？\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x101,
        "#12P#00006F用不着那么生气吧……\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x105,
        (
            "#12P#10302F嗯，而且这和黑月\x01",
            "完全没有关系啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF4C")

    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    #C0801
    ChrTalk(
        0x1A2,
        "哼，总之——\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0802
    ChrTalk(
        0x1A2,
        (
            "#12P嗯，这是什么……？\x01",
            "『时代』百货店的限定商品\x01",
            "『咪西座钟』？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    #C0803
    ChrTalk(
        0x1A2,
        "#12P——哼！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0804
    ChrTalk(
        0x1A2,
        (
            "总、总之就是些\x01",
            "骗小孩的东西而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x1A2,
        (
            "我对它丝毫兴趣\x01",
            "都没有！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D0AA")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_D157")

    label("loc_D0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D103")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_D157")

    label("loc_D103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D157")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_D157")


    #C0806
    ChrTalk(
        0x101,
        "#12P#00012F（太、太心口不一了……）\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x102,
        (
            "#12P#00100F（嗯，根本就等于是承认\x01",
            "  自己很喜欢了呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 7)
    OP_65(0x9, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -15080, 0, 8820, 0)
    EventEnd(0x5)
    Return()

    # Function_50_CA19 end

    def Function_51_D1E9(): pass

    label("Function_51_D1E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-960, 3000, 1530, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17880, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D275")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x104, 600, 0, 2900, 180)
    Jump("loc_D314")

    label("loc_D275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D2C7")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x109, 600, 0, 2900, 180)
    Jump("loc_D314")

    label("loc_D2C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D314")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x105, 600, 0, 2900, 180)

    label("loc_D314")

    OP_68(-960, 1600, 1530, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0808
    ChrTalk(
        0x101,
        (
            "#00000F那么，我们在店里随便逛逛，\x01",
            "然后就去楼顶吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x1A2,
        "#12P嗯，请带路吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 3)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 2900, 0)
    OP_1B(0x0, 0x0, 0x35)
    OP_66(0x9, 0x1)
    EventEnd(0x5)
    Return()

    # Function_51_D1E9 end

    def Function_52_D3B0(): pass

    label("Function_52_D3B0")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-17440, 1600, 19460, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16140, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D43D")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x104, -15690, 30, 21350, 270)
    Jump("loc_D4DC")

    label("loc_D43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D48F")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x109, -15690, 30, 21350, 270)
    Jump("loc_D4DC")

    label("loc_D48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D4DC")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x105, -15690, 30, 21350, 270)

    label("loc_D4DC")

    FadeToBright(1000, 0)
    OP_0D()

    #C0810
    ChrTalk(
        0x1A2,
        (
            "#12P喂，你怎么从刚才开始\x01",
            "就一直鬼鬼祟祟的？\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        "#00000F哦，其实我刚才去买了这个。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D561")

    def lambda_D54F():

        label("loc_D54F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D54F")

    QueueWorkItem2(0x104, 1, lambda_D54F)
    Jump("loc_D59C")

    label("loc_D561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D581")

    def lambda_D56F():

        label("loc_D56F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D56F")

    QueueWorkItem2(0x109, 1, lambda_D56F)
    Jump("loc_D59C")

    label("loc_D581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D59C")

    def lambda_D58F():

        label("loc_D58F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D58F")

    QueueWorkItem2(0x105, 1, lambda_D58F)

    label("loc_D59C")

    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D5DA")
    EndChrThread(0x104, 0x1)

    def lambda_D5BD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D5BD)
    Sleep(50)

    def lambda_D5CD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D5CD)
    Jump("loc_D633")

    label("loc_D5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D609")
    EndChrThread(0x109, 0x1)

    def lambda_D5EC():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D5EC)
    Sleep(50)

    def lambda_D5FC():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D5FC)
    Jump("loc_D633")

    label("loc_D609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D633")
    EndChrThread(0x105, 0x1)

    def lambda_D61B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D61B)
    Sleep(50)

    def lambda_D62B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D62B)

    label("loc_D633")

    Sleep(300)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0812
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将\x01",
            "『咪西座钟』交给了秦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x5DC, 0x0)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0813
    ChrTalk(
        0x1A2,
        "#12P这、这是百货店限定的……\x02",
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x102,
        "#00100F原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D713")

    #C0815
    ChrTalk(
        0x104,
        "#11P#00309F嘿，很会察言观色啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D778")

    label("loc_D713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D748")

    #C0816
    ChrTalk(
        0x109,
        "#11P#10109F呵呵，真会察言观色啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D778")

    label("loc_D748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D778")

    #C0817
    ChrTalk(
        0x105,
        "#11P#10302F呵呵，很会察言观色嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_D778")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    #C0818
    ChrTalk(
        0x1A2,
        (
            "#12P这是干什么啊，\x01",
            "为什么要给我这个……\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，只是送你个\x01",
            "礼物而已。\x02\x03",

            "就当作是今天的纪念好了，\x01",
            "可以收下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x1A2,
        "#12P今天的纪念……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)
    OP_93(0x1A2, 0xB4, 0x1F4)
    Sleep(300)

    #C0821
    ChrTalk(
        0x1A2,
        (
            "#12P……既然都已经买了，\x01",
            "总不能扔掉。\x01",
            "好吧，那我就收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    #C0822
    ChrTalk(
        0x1A2,
        (
            "#12P不过，话还是要说清楚。\x01",
            "我对这种玩具\x01",
            "可是丝毫兴趣都没有！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D92B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_D9D8")

    label("loc_D92B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D984")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_D9D8")

    label("loc_D984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D9D8")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_D9D8")


    #C0823
    ChrTalk(
        0x101,
        "#00000F嗯嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C6, 0)
    OP_29(0x73, 0x1, 0xC)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -15900, 0, 20830, 180)
    EventEnd(0x5)
    Return()

    # Function_52_D3B0 end

    def Function_53_DA22(): pass

    label("Function_53_DA22")

    EventBegin(0x1)

    #C0824
    ChrTalk(
        0x101,
        (
            "#00000F已经没时间去外面参观了。\x02\x03",

            "在店里随便逛逛，然后就去楼顶吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -600, 30, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_53_DA22 end

    SaveToFile()

Try(main)
