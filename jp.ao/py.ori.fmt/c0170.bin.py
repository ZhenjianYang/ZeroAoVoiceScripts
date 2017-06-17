from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付嬢パール",           # 1
        "受付嬢シンシア",         # 2
        "ハンソン",               # 3
        "リジョン",               # 4
        "プラダ",                 # 5
        "ベイカー",               # 6
        "サザーク",               # 7
        "リナリー",               # 8
        "プルーナ",               # 9
        "ネストン支配人",         # 10
        "ジャネッタ",             # 11
        "バッジョ",               # 12
        "ドロテ",                 # 13
        "ケン",                   # 14
        "オネスト老人",           # 15
        "ユーリ",                 # 16
        "サイクス",               # 17
        "レジー",                 # 18
        "プリエ",                 # 19
        "グレイス",               # 20
        "レインズ",               # 21
        "市民",                   # 22
        "観光客",                 # 23
        "観光客",                 # 24
        "レイモンド捜査官",       # 25
        "ダドリー捜査官",         # 26
        "フェルナンド",           # 27
        "ジョアンナ",             # 28
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
        "Function_5_DD2",          # 05, 5
        "Function_6_DD6",          # 06, 6
        "Function_7_1C76",         # 07, 7
        "Function_8_1C7A",         # 08, 8
        "Function_9_26A5",         # 09, 9
        "Function_10_28DD",        # 0A, 10
        "Function_11_2A79",        # 0B, 11
        "Function_12_2A98",        # 0C, 12
        "Function_13_3B00",        # 0D, 13
        "Function_14_3B07",        # 0E, 14
        "Function_15_4DA3",        # 0F, 15
        "Function_16_4DA7",        # 10, 16
        "Function_17_5DD1",        # 11, 17
        "Function_18_5DD5",        # 12, 18
        "Function_19_6C7A",        # 13, 19
        "Function_20_6C81",        # 14, 20
        "Function_21_85E9",        # 15, 21
        "Function_22_8739",        # 16, 22
        "Function_23_9AD4",        # 17, 23
        "Function_24_9ED5",        # 18, 24
        "Function_25_A29D",        # 19, 25
        "Function_26_A4FA",        # 1A, 26
        "Function_27_A8B2",        # 1B, 27
        "Function_28_B1CC",        # 1C, 28
        "Function_29_B9EB",        # 1D, 29
        "Function_30_C419",        # 1E, 30
        "Function_31_CD55",        # 1F, 31
        "Function_32_CF45",        # 20, 32
        "Function_33_D0B1",        # 21, 33
        "Function_34_D148",        # 22, 34
        "Function_35_D1E9",        # 23, 35
        "Function_36_D280",        # 24, 36
        "Function_37_D45E",        # 25, 37
        "Function_38_D556",        # 26, 38
        "Function_39_DF64",        # 27, 39
        "Function_40_E095",        # 28, 40
        "Function_41_E219",        # 29, 41
        "Function_42_E35E",        # 2A, 42
        "Function_43_E4DC",        # 2B, 43
        "Function_44_E555",        # 2C, 44
        "Function_45_EB99",        # 2D, 45
        "Function_46_EC17",        # 2E, 46
        "Function_47_F3CC",        # 2F, 47
        "Function_48_F4DB",        # 30, 48
        "Function_49_F6AF",        # 31, 49
        "Function_50_F7C7",        # 32, 50
        "Function_51_10079",       # 33, 51
        "Function_52_10258",       # 34, 52
        "Function_53_10982",       # 35, 53
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
            "　　★　リジョンフード・メモ　★\x01",
            "ご来店のお客様に、爽やかな喉ごしの\x01",
            "ベルベリージュースを提案いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ベルベリージュースのレシピが書かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_DCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ベルベリージュース』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DCE")

    TalkEnd(0xFF)
    Return()

    # Function_4_C9C end

    def Function_5_DD2(): pass

    label("Function_5_DD2")

    Call(0, 6)
    Return()

    # Function_5_DD2 end

    def Function_6_DD6(): pass

    label("Function_6_DD6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E9D")

    #C0004
    ChrTalk(
        0x8,
        (
            "少し前にスコットさんが\x01",
            "顔を見せに来てくれたんですが、\x01",
            "とりあえず元気そうで何よりでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "彼があれだけ\x01",
            "頑張ってくれているんですから……\x01",
            "私も出来ることを頑張らないとですね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_101C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB8")
    Call(0, 23)
    Jump("loc_1017")

    label("loc_EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAF")

    #C0006
    ChrTalk(
        0x8,
        (
            "幸い、この場所は当面の間、\x01",
            "食料品や日用品の類に\x01",
            "困ることはありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "この状況が長く続くとすれば、\x01",
            "むしろそういった蓄えのない\x01",
            "ご家庭などの方が心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "本当に……政府はいったい\x01",
            "何を考えているのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1017")

    label("loc_FAF")


    #C0009
    ChrTalk(
        0x8,
        (
            "本当に……政府はいったい\x01",
            "何を考えているのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "スコットさんも\x01",
            "無事だといいんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1017")

    Jump("loc_1C72")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112A")

    #C0011
    ChrTalk(
        0x8,
        (
            "シンシア先輩は住民投票の翌日に\x01",
            "故郷のレミフェリアに帰ったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "先輩も、まさか\x01",
            "今のクロスベルの状況は\x01",
            "予想していなかったと思いますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "以前からご家族も\x01",
            "かなり心配されていたようですし、\x01",
            "早めに帰国できて本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E2")

    label("loc_112A")


    #C0014
    ChrTalk(
        0x8,
        (
            "シンシア先輩は、必ずまた\x01",
            "この百貨店に戻って来るって\x01",
            "約束してくれたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "これから色々不安もありますけど……\x01",
            "先輩とまたご一緒できる日を信じて\x01",
            "とにかく一生懸命がんばります。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E2")

    Jump("loc_1C72")

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AE")

    #C0016
    ChrTalk(
        0x8,
        (
            "シンシア先輩は、行政区で\x01",
            "行われているチャリティイベントに\x01",
            "お手伝いで参加しているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "それに、何でも\x01",
            "ミスコンにも参加するとか。\x01",
            "あとで写真をみせてもらおっと♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_130E")

    label("loc_12AE")


    #C0018
    ChrTalk(
        0x8,
        (
            "シンシア先輩は、何でも\x01",
            "ミスコンにも参加されるらしいんです。\x01",
            "あとで写真をみせてもらおっと♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130E")

    Jump("loc_1C72")

    label("loc_1313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1399")

    #C0019
    ChrTalk(
        0x8,
        "鉱山町を占拠するなんて……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "誰が何のために\x01",
            "計画したかは知りませんけど……\x01",
            "こんなの、許されるわけがありません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_1399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1458")

    #C0021
    ChrTalk(
        0x8,
        (
            "スコットさんから\x01",
            "また当分、仕事が忙しくて\x01",
            "連絡が取れそうにないって言われました。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "でも、へっちゃらです。\x01",
            "それが遊撃士の人と\x01",
            "一緒になるってことですからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14D3")

    label("loc_1458")


    #C0023
    ChrTalk(
        0x8,
        (
            "あの人のことだから\x01",
            "心配はいらないと思うんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "くれぐれも\x01",
            "大きな怪我だけはしないよう\x01",
            "気を付けて欲しいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D3")

    Jump("loc_1C72")

    label("loc_14D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1525")

    #C0025
    ChrTalk(
        0x8,
        (
            "列車が脱線だなんて……\x01",
            "車両トラブルか何かでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_1525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15BC")

    #C0026
    ChrTalk(
        0x8,
        (
            "スコットさん、\x01",
            "最近何だかいつにも増して\x01",
            "忙しくなってきたみたいなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "頑張れ、スコットさん。\x01",
            "いつだって私がついてるからね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D7")
    Call(0, 10)
    Jump("loc_1660")

    label("loc_15D7")


    #C0028
    ChrTalk(
        0x8,
        (
            "あ、皆様は\x01",
            "いつもご利用下さっている\x01",
            "特務支援課の……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "本日もご来店ありがとうございます。\x01",
            "どうぞ、ごゆっくり見て回って下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1660")

    Jump("loc_1C72")

    label("loc_1665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_179F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175B")

    #C0030
    ChrTalk(
        0x8,
        (
            "昨日のお食事会に、\x01",
            "ジャネッタちゃんが男性を\x01",
            "３人呼んでいたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "ちょっと話をしている内に\x01",
            "３人の興味が全部シンシア先輩に\x01",
            "集中したんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "ジャネッタちゃん、今日は\x01",
            "元気なかったけど大丈夫かなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179A")

    label("loc_175B")


    #C0033
    ChrTalk(
        0x8,
        (
            "ジャネッタちゃん、今日は\x01",
            "元気なかったけど大丈夫かなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179A")

    Jump("loc_1C72")

    label("loc_179F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_186F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183D")

    #C0034
    ChrTalk(
        0x8,
        (
            "今日は仕事終わりに、\x01",
            "シンシア先輩とジャネッタちゃんの\x01",
            "３人でお食事に行くんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "久しぶりのお食事会、\x01",
            "ふふ、楽しみだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_186A")

    label("loc_183D")


    #C0036
    ChrTalk(
        0x8,
        (
            "久しぶりのお食事会、\x01",
            "ふふ、楽しみだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186A")

    Jump("loc_1C72")

    label("loc_186F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188A")
    Call(0, 9)
    Jump("loc_192B")

    label("loc_188A")


    #C0037
    ChrTalk(
        0x8,
        (
            "以前からファンとは聞いていましたが、\x01",
            "先輩がまさかこれほどまでに\x01",
            "ユリアさんラブだったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "ふふ、シンシア先輩の\x01",
            "また新たな一面が知れて嬉しいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_192B")

    Jump("loc_1C72")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4D")

    #C0039
    ChrTalk(
        0x8,
        (
            "スコットさん、\x01",
            "今頃何をしているんだろうな。\x01",
            "お仕事なのは分かってるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x8,
        (
            "あっ、すみません……！\x01",
            "私ったら仕事中に余計なことを。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "何か不都合がございましたら\x01",
            "遠慮なく仰ってくださいね。\x01",
            "誠心誠意ご対応させて頂きますので。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AAB")

    label("loc_1A4D")


    #C0042
    ChrTalk(
        0x8,
        (
            "何か不都合がございましたら\x01",
            "遠慮なく仰ってくださいね。\x01",
            "誠心誠意ご対応させて頂きますので。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAB")

    Jump("loc_1C72")

    label("loc_1AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1B3A")

    #C0043
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "雨の日でも当店はもちろん営業中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "本日も素敵なショッピングを\x01",
            "お楽しみ下さいませ。（ニコッ）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_1B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C01")

    #C0045
    ChrTalk(
        0x8,
        (
            "百貨店《タイムズ》をご利用頂き\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "こちらは総合インフォメーションです。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "何かご不明な点がございましたら\x01",
            "いつでもお気軽にお尋ねくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C72")

    label("loc_1C01")


    #C0048
    ChrTalk(
        0x8,
        "こちらは総合インフォメーションです。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "何かご不明な点がございましたら\x01",
            "いつでもお気軽にお尋ねくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C72")

    TalkEnd(0x8)
    Return()

    # Function_6_DD6 end

    def Function_7_1C76(): pass

    label("Function_7_1C76")

    Call(0, 8)
    Return()

    # Function_7_1C76 end

    def Function_8_1C7A(): pass

    label("Function_8_1C7A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C8B")
    Jump("loc_26A1")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C99")
    Jump("loc_26A1")

    label("loc_1C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D38")

    #C0050
    ChrTalk(
        0x9,
        (
            "武装集団の正体については\x01",
            "色々と言われていますが、\x01",
            "実際の所はどうなんでしょう……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "とにかく……住民の皆さんに\x01",
            "怪我がないことを祈ります。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_1D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DBA")

    #C0052
    ChrTalk(
        0x9,
        (
            "パールさんとスコットさんは\x01",
            "昔からの幼馴染なんだそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "幼馴染で婚約者って、\x01",
            "何だか憧れちゃいますよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E63")

    #C0054
    ChrTalk(
        0x9,
        (
            "支配人から聞いたのですが、\x01",
            "どうやら西クロスベル街道の方で\x01",
            "列車が脱線したそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "被害に遭われた皆さんが、\x01",
            "大事に至らなければよいのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_1E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA7")

    #C0056
    ChrTalk(
        0x9,
        (
            "この所、独立に関する議論が徐々に\x01",
            "熱を帯びてきているように感じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "レミフェリアにいる家族からは\x01",
            "何か問題が起こる前に帰って来いとも\x01",
            "言われているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "クロスベルは、私にとって\x01",
            "第二の故郷とも言える場所ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "とりあえず、住民投票の\x01",
            "行方だけは見届けて行くつもりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_204E")

    label("loc_1FA7")


    #C0060
    ChrTalk(
        0x9,
        (
            "何と言いましても……\x01",
            "クロスベルは、私にとって\x01",
            "第二の故郷とも言える場所ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "住民投票には責任を持って参加して、\x01",
            "その行方だけは見届けて行くつもりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204E")

    Jump("loc_26A1")

    label("loc_2053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206E")
    Call(0, 10)
    Jump("loc_20FB")

    label("loc_206E")


    #C0062
    ChrTalk(
        0x9,
        (
            "あら……申し訳ありません。\x01",
            "お仕事中なのに、\x01",
            "つい話に夢中になってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "何か御用が御座いましたら\x01",
            "何なりとお申し付け下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FB")

    Jump("loc_26A1")

    label("loc_2100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2233")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C2")

    #C0064
    ChrTalk(
        0x9,
        (
            "まさかジャネッタさんが\x01",
            "男の人を呼んでいるとは\x01",
            "思いませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "皆さんがお金持ちだというのは\x01",
            "よく分かったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "ふう、ああいうのって疲れますね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_222E")

    label("loc_21C2")


    #C0067
    ChrTalk(
        0x9,
        (
            "まさかジャネッタさんが\x01",
            "男の人を呼んでいるとは\x01",
            "思いませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        "ふう、ああいうのって疲れますね。\x02",
    )

    CloseMessageWindow()

    label("loc_222E")

    Jump("loc_26A1")

    label("loc_2233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E2")

    #C0069
    ChrTalk(
        0x9,
        (
            "ジャネッタさん、\x01",
            "今日はやけに張り切って\x01",
            "何かあったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "３人で食事に行くのは別に\x01",
            "初めてではないんですけど……\x01",
            "気にしすぎかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2330")

    label("loc_22E2")


    #C0071
    ChrTalk(
        0x9,
        (
            "３人で食事に行くのは別に\x01",
            "初めてではないんですけど……\x01",
            "気にしすぎかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2330")

    Jump("loc_26A1")

    label("loc_2335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2350")
    Call(0, 9)
    Jump("loc_23E7")

    label("loc_2350")


    #C0072
    ChrTalk(
        0x9,
        (
            "あ、あら、お客様……\x01",
            "これは失礼をいたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "本日は百貨店《タイムズ》へようこそ。\x01",
            "何か御用が御座いましたら\x01",
            "いつでもお声を掛けて下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E7")

    Jump("loc_26A1")

    label("loc_23EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_24AA")

    #C0074
    ChrTalk(
        0x9,
        (
            "明日から始まる通商会議には\x01",
            "参加各国の色んなＶＩＰの\x01",
            "方々が来られるそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "特に当店にお越しいただける\x01",
            "予定があるわけではないのですが、\x01",
            "何だか緊張してしまいます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_24AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2532")

    #C0076
    ChrTalk(
        0x9,
        (
            "パールさん、この所は婚約者の\x01",
            "スコットさんに定期的に会えたらしく\x01",
            "とても元気なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        "ふふ、羨ましい限りですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260C")

    #C0078
    ChrTalk(
        0x9,
        (
            "先日開放された屋上スペースは\x01",
            "もうご覧いただけましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "特別な施設等はございませんが、\x01",
            "クロスベル市を一望できる\x01",
            "絶景スポットとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        "宜しければ是非お立ち寄り下さい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26A1")

    label("loc_260C")


    #C0081
    ChrTalk(
        0x9,
        (
            "先日開放された屋上スペースは\x01",
            "早くもお客様方から\x01",
            "ご好評の声をいただいております。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "皆様も、ぜひ息抜きに\x01",
            "お立ち寄りになってはいかがでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A1")

    TalkEnd(0x9)
    Return()

    # Function_8_1C7A end

    def Function_9_26A5(): pass

    label("Function_9_26A5")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    #C0083
    ChrTalk(
        0x9,
        "パールさん、聞きましたか？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "どうやらリベールからは\x01",
            "あのユリア様も\x01",
            "来ていらっしゃるとか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "ええ、もちろんチェック済みですよ。\x01",
            "一応、友達に頼んで\x01",
            "写真もお願いしておきましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "ただまあ、うまく撮れてるかどうかは\x01",
            "分かりませんけどね。\x02",
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
            "パールさん、その写真\x01",
            "私にも譲って下さい、絶対ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "は、はい。\x01",
            "もちろん構いませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00000F（ユリア准佐か……\x01",
            "  本当に人気があるんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x109,
        (
            "#10109F（ええ、それは何と言っても\x01",
            "  あのユリア准佐ですからっ。）\x02",
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

    # Function_9_26A5 end

    def Function_10_28DD(): pass

    label("Function_10_28DD")

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
            "それじゃ、サザークさんが\x01",
            "告白した場所というのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "ええ、何でも\x01",
            "ミシュラムの高級レストラン\x01",
            "《フォルトゥナ》らしいんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "それも、お店の人に頼んで\x01",
            "サプライズ演出をしてもらったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        "サザークさんも演出家ですよね～。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "そうね、でもジェネッタちゃんが\x01",
            "幸せになれて本当に良かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "ふふ、私もあやからなくっちゃ。\x02",
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

    # Function_10_28DD end

    def Function_11_2A79(): pass

    label("Function_11_2A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A94")
    Call(0, 46)
    Jump("loc_2A97")

    label("loc_2A94")

    Call(0, 12)

    label("loc_2A97")

    Return()

    # Function_11_2A79 end

    def Function_12_2A98(): pass

    label("Function_12_2A98")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AFC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B03")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B22")
    OP_AF(0x26)
    Jump("loc_2B44")

    label("loc_2B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B32")
    OP_AF(0x25)
    Jump("loc_2B44")

    label("loc_2B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B42")
    OP_AF(0x24)
    Jump("loc_2B44")

    label("loc_2B42")

    OP_AF(0x23)

    label("loc_2B44")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AF7")

    label("loc_2B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B67")
    Jump("loc_3AF7")

    label("loc_2B67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C4A")

    #C0098
    ChrTalk(
        0xA,
        (
            "輸入品の販売が難しくても、\x01",
            "ウチにはオーダーメイドのサービスが\x01",
            "ありますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "これからもっと職人さんを増やして\x01",
            "皆様に充実したサービスをご提供できるよう\x01",
            "努めさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D08")

    #C0100
    ChrTalk(
        0xA,
        (
            "この戒厳令は一体\x01",
            "いつまで続くのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "食料品などにしても\x01",
            "家庭に蓄えのない方は\x01",
            "数日ももたないでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "先の見えない不安というものは\x01",
            "本当に恐怖ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E17")

    #C0103
    ChrTalk(
        0xA,
        (
            "国防軍は、本当にクロスベルを\x01",
            "守りきれるのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "アリオスさんを信じたい気持ちは\x01",
            "勿論あるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "仮に２大国が総出で侵攻してきた場合、\x01",
            "流石に降伏せざるを得ないはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "あるいは……\x01",
            "何か秘策でもあるのでしょうかね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E97")

    label("loc_2E17")


    #C0107
    ChrTalk(
        0xA,
        (
            "仮に２大国が総出で侵攻してきた場合、\x01",
            "流石に降伏せざるを得ないはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "あるいは……\x01",
            "何か秘策でもあるのでしょうかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E97")

    Jump("loc_3AF7")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2F53")

    #C0109
    ChrTalk(
        0xA,
        (
            "街の復興の方も、ようやく\x01",
            "一区切り付いてきたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "私には大したことはできませんが……\x01",
            "せめて一部商品のセールでも行って\x01",
            "皆さんに還元させて頂くつもりです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FC7")

    #C0111
    ChrTalk(
        0xA,
        (
            "マインツにいる\x01",
            "お得意様の顔が思い浮かばれます。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "皆さん、無事でいてくれると\x01",
            "良いのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_319C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DB")

    #C0113
    ChrTalk(
        0xA,
        (
            "昨日、列車が止まったと聞いた時は\x01",
            "どうなることかと思いましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "警備隊を始め、駅関係者の\x01",
            "皆さんの活躍によって、今日には\x01",
            "見事に完全復旧したようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "おかげ様で、今朝の納品も\x01",
            "つつがなく終えることができ、\x01",
            "感謝の言葉もありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3197")

    label("loc_30DB")


    #C0116
    ChrTalk(
        0xA,
        (
            "大陸横断鉄道は、まるで昨日の\x01",
            "列車事故などなかったかのように\x01",
            "見事に完全復旧したようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "復旧に尽力してくださった\x01",
            "警備隊を始め、駅関係者の皆さんには\x01",
            "感謝の言葉もありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3197")

    Jump("loc_3AF7")

    label("loc_319C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_31D4")

    #C0118
    ChrTalk(
        0xA,
        "ふむ、どうやら何か事故のようですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_END)), "loc_326C")

    #C0119
    ChrTalk(
        0xA,
        (
            "ダドリー様は当店の常連様でして、\x01",
            "年に何度か革靴を作って下さるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "その情熱とこだわりぶりは\x01",
            "まさしく本物の愛好家ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326C")

    Jump("loc_3AF7")

    label("loc_3271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_335D")

    #C0121
    ChrTalk(
        0xA,
        (
            "人と人との出会いが一期一会であるように、\x01",
            "人と靴との出会いもまた、\x01",
            "同じく一期一会であると私は思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "少し変だと思われそうですが、\x01",
            "ディスプレイされた商品を眺めていると\x01",
            "何か語りかけてくるような気さえするんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_335D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33E6")

    #C0123
    ChrTalk(
        0xA,
        "本当に良い物は流行に左右されません。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "私は常々、時代を超えて愛されるものを\x01",
            "皆さんに提供したいと思っているのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_33E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_35D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350F")

    #C0125
    ChrTalk(
        0xA,
        (
            "靴選びは夕方以降に行った方が良い事を\x01",
            "皆さんはご存知でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "というのも、人の足は朝起きてから\x01",
            "徐々にむくんでいき、夕方頃にもなると\x01",
            "最大で約１リジュほども大きくなるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "なので、足が最も大きくなる夕方以降に\x01",
            "サイズを選ぶのが良いとされているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35D2")

    label("loc_350F")


    #C0128
    ChrTalk(
        0xA,
        (
            "実は、人の足は朝起きてから\x01",
            "徐々にむくんでいき、夕方頃にもなると\x01",
            "最大で約１リジュほども大きくなるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "なので、足が最も大きくなる夕方以降に\x01",
            "サイズを選ぶのが良いとされているのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D2")

    Jump("loc_3AF7")

    label("loc_35D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_365F")

    #C0130
    ChrTalk(
        0xA,
        (
            "革靴は履き込めば履き込むほど、\x01",
            "足に心地よく馴染んで行きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "人と同じで奥深く、\x01",
            "そして味わい深いものなのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_365F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F1")

    #C0132
    ChrTalk(
        0xA,
        (
            "当店ではお子様向けの品も\x01",
            "充実しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "どうぞごゆっくり\x01",
            "ご覧になって行ってください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A8")

    label("loc_36F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3801")

    #C0134
    ChrTalk(
        0xA,
        (
            "プラダさんからよく、以前のように\x01",
            "服も扱うようにとつつかれるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "靴の世界というものは\x01",
            "それだけで非常に奥の深いものでしてね。\x01",
            "飛び込んでみて改めて実感したのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "だからこそ、今は脇目を振らずに\x01",
            "ただ靴のことだけを追求したいのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38A8")

    label("loc_3801")


    #C0137
    ChrTalk(
        0xA,
        (
            "服の世界も勿論そうですが、\x01",
            "靴の世界というものも\x01",
            "それだけで非常に奥の深いものでしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "だからこそ、今は脇目を振らずに\x01",
            "ただ靴のことだけを追求したいのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A8")

    Jump("loc_3AF7")

    label("loc_38AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3934")

    #C0139
    ChrTalk(
        0xA,
        (
            "当店ではレインシューズも\x01",
            "取り扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "急な雨で、買ってすぐ\x01",
            "履き替えていく方もおりますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_399C")

    label("loc_3934")


    #C0141
    ChrTalk(
        0xA,
        (
            "当店ではレインシューズも\x01",
            "取り扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "ご所望でしたら、\x01",
            "オススメの品をお持ちしますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399C")

    Jump("loc_3AF7")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A56")

    #C0143
    ChrTalk(
        0xA,
        "《ハンソンシューズ》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "商品探しにお困りでしたら、\x01",
            "ぜひお気軽にご相談ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "お客様にピッタリの\x01",
            "一足を見つけて差し上げますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AF7")

    label("loc_3A56")


    #C0146
    ChrTalk(
        0xA,
        (
            "当店ではカジュアルはもちろん、\x01",
            "フォーマルにトレッキング用まで\x01",
            "あらゆる品を取り揃えております。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "きっとお客様にピッタリの\x01",
            "一足を見つけて差し上げますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF7")

    Jump("loc_2AA5")

    label("loc_3AFC")

    TalkEnd(0xA)
    Return()

    # Function_12_2A98 end

    def Function_13_3B00(): pass

    label("Function_13_3B00")

    SetScenarioFlags(0x2, 3)
    Call(0, 14)
    Return()

    # Function_13_3B00 end

    def Function_14_3B07(): pass

    label("Function_14_3B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B76")
    TalkBegin(0xB)

    #C0148
    ChrTalk(
        0xB,
        (
            "搬入担当の方……\x01",
            "ではないみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "お買い物でしたら、\x01",
            "正面に回ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    label("loc_3B76")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D12")

    #C0150
    ChrTalk(
        0x1A2,
        (
            "なるほど、ここでは輸入食材を\x01",
            "多く取り扱っているんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1A2,
        "フム、醤油まで置いてあるのか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x1A2, 500)
    Sleep(300)

    #C0152
    ChrTalk(
        0xB,
        (
            "ふふ、お坊ちゃんは\x01",
            "もしかして東方の出身かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "ここには、東方のかたにも\x01",
            "きっとご満足いただける本場の\x01",
            "食材も多数取り扱っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "何か置いて欲しい\x01",
            "商品の要望などもあれば、\x01",
            "いつでも言ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x1A2,
        "あ、ああ……考えておくぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TalkEnd(0xB)
    Jump("loc_3D8A")

    label("loc_3D12")

    TalkBegin(0xB)

    #C0156
    ChrTalk(
        0xB,
        (
            "お客様のご要望があれば\x01",
            "ウチではお取り寄せを\x01",
            "することだって出来るんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        "何でも気軽にご相談くださいね。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)

    label("loc_3D8A")

    Return()

    label("loc_3D8B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DF3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3DF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E13")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D9A")

    label("loc_3E13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E27")
    Jump("loc_4D9A")

    label("loc_3E27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3ED0")

    #C0158
    ChrTalk(
        0xB,
        (
            "さっき娘と連絡が付いて\x01",
            "無事を確認することができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "娘も早速屋台を出したそうですし、\x01",
            "私も頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_3ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F70")

    #C0160
    ChrTalk(
        0xB,
        (
            "それにしても……\x01",
            "娘はちゃんと家の方に\x01",
            "避難できたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "戒厳令以降、導力通信も\x01",
            "使えない状態が続いていますし……\x01",
            "本当に心配です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_3F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405D")

    #C0162
    ChrTalk(
        0xB,
        (
            "クロスベルを通過する列車が\x01",
            "今朝から全面的に運行を\x01",
            "制限されているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "何でも今日を最後に\x01",
            "鉄道は運行停止となるそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "こうなると、商売以前に\x01",
            "戦争の二文字が頭をよぎってしまいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40DB")

    label("loc_405D")


    #C0165
    ChrTalk(
        0xB,
        (
            "何でも今日を最後に\x01",
            "鉄道は運行停止となるそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xB,
        (
            "こうなると、商売以前に\x01",
            "戦争の二文字が頭をよぎってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DB")

    Jump("loc_4D9A")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4249")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A8")

    #C0167
    ChrTalk(
        0xB,
        (
            "どんなことが起こっても\x01",
            "商売人はへこたれていられません。\x01",
            "とにかく頑張って仕事をするだけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "いらっしゃいませ、疲れた体に\x01",
            "オレド自治州産のニンニクはいかがですか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4244")

    label("loc_41A8")


    #C0169
    ChrTalk(
        0xB,
        (
            "いらっしゃいませ、疲れた体に\x01",
            "オレド自治州産のニンニクはいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "オレドのニンニクは粒が大きくて、\x01",
            "栄養価も高いので滋養強壮に最適なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4244")

    Jump("loc_4D9A")

    label("loc_4249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_42BC")

    #C0171
    ChrTalk(
        0xB,
        (
            "マインツの人たちは\x01",
            "今頃どうしているんでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        "一刻も早く解放されるといいんですが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_42BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A2")

    #C0173
    ChrTalk(
        0xB,
        (
            "どうやら導力鉄道は一晩の内に\x01",
            "完全に復旧されたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "おかげ様で、今日の鉄道便も\x01",
            "いつも通り受け取る事ができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "夜を徹して復旧作業を行ってくれた\x01",
            "警備隊の皆さんには感謝感謝ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_442E")

    label("loc_43A2")


    #C0176
    ChrTalk(
        0xB,
        (
            "おかげ様で、今日の鉄道便も\x01",
            "いつも通り受け取る事ができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "夜を徹して復旧作業を行ってくれた\x01",
            "警備隊の皆さんには感謝感謝ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442E")

    Jump("loc_4D9A")

    label("loc_4433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_450B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AA")

    #C0178
    ChrTalk(
        0xB,
        (
            "何でも西の街道で\x01",
            "列車が脱線したそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "落盤事故でも\x01",
            "あったのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4506")

    label("loc_44AA")


    #C0180
    ChrTalk(
        0xB,
        (
            "何でも西の街道で\x01",
            "列車が脱線したそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "落盤事故でも\x01",
            "あったのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4506")

    Jump("loc_4D9A")

    label("loc_450B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4599")

    #C0182
    ChrTalk(
        0xB,
        (
            "食材のことなら何でもお任せ、\x01",
            "《リジョンフード》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "今日は共和国産のネギが\x01",
            "大変お買い得になっておりま～す。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4616")

    #C0184
    ChrTalk(
        0xB,
        (
            "サザーク君とジャネッタちゃんが\x01",
            "付き合うことになったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        "ふふ、職場恋愛だなんて羨ましいです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_469E")

    #C0186
    ChrTalk(
        0xB,
        (
            "ジャネッタちゃん、\x01",
            "今日は何だか元気がなくて心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        (
            "昨日はあれほど元気だったのに、\x01",
            "何かあったのかしら……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_469E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4729")

    #C0188
    ChrTalk(
        0xB,
        (
            "こんばんは。\x01",
            "《リジョンフード》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xB,
        (
            "晩御飯の支度がまだなら、\x01",
            "ぜひウチで材料を\x01",
            "買い揃えて行って下さいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_48DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4830")

    #C0190
    ChrTalk(
        0xB,
        (
            "食材のことなら何でもお任せ、\x01",
            "《リジョンフード》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "本日から３日間限定で、\x01",
            "《通商会議セット》を販売しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "帝国、王国、公国、共和国、\x01",
            "そしてこのクロスベルの一押し食材を\x01",
            "詰め合わせた豪華なセットなんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48D9")

    label("loc_4830")


    #C0193
    ChrTalk(
        0xB,
        (
            "本日から３日間限定で、\x01",
            "《通商会議セット》を販売しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "帝国、王国、公国、共和国、\x01",
            "そしてこのクロスベルの一押し食材を\x01",
            "詰め合わせた豪華なセットなんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D9")

    Jump("loc_4D9A")

    label("loc_48DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A23")

    #C0195
    ChrTalk(
        0xB,
        (
            "頼れる主婦の味方、\x01",
            "《リジョンフード》へようこそ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "今晩の献立に困ったら、\x01",
            "アドバイスをして差し上げますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "例えば今朝入ったばかりの\x01",
            "新鮮なフレッシュハーブを使った\x01",
            "スープ料理なんていかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "ただし、お出汁に使う\x01",
            "ローリエの葉は煮込み過ぎると\x01",
            "苦味が出るのでご注意くださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A9F")

    label("loc_4A23")


    #C0199
    ChrTalk(
        0xB,
        (
            "今晩の献立に困ったら、\x01",
            "アドバイスをして差し上げますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "ちなみに今日のお勧めは\x01",
            "フレッシュハーブのスープ料理です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9F")

    Jump("loc_4D9A")

    label("loc_4AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B85")

    #C0201
    ChrTalk(
        0xB,
        (
            "うちの娘は最近、\x01",
            "ジュース屋の新メニュー開発に\x01",
            "力を入れているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xB,
        (
            "今日は雨で屋台が営業できない分、\x01",
            "家でじっくり研究するとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "ふふ、向上心があるって\x01",
            "とても素晴らしいことですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C0A")

    label("loc_4B85")


    #C0204
    ChrTalk(
        0xB,
        (
            "うちの娘は最近、\x01",
            "ジュース屋の新メニュー開発に\x01",
            "力を入れているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "ふふ、向上心があるって\x01",
            "とても素晴らしいことですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C0A")

    Jump("loc_4D9A")

    label("loc_4C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D14")

    #C0206
    ChrTalk(
        0xB,
        (
            "食材のことなら何でもお任せ、\x01",
            "《リジョンフード》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "ちなみにウチの食材を使った\x01",
            "ヘルシーなジュース屋があるので\x01",
            "そちらも宜しくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "行政区にあるジューススタンドで、\x01",
            "私の娘がお店をやっているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D9A")

    label("loc_4D14")


    #C0209
    ChrTalk(
        0xB,
        (
            "食材のことなら何でもお任せ、\x01",
            "《リジョンフード》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "ウチの食材を使った行政区の\x01",
            "ジュース屋も宜しくお願いしま～す。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9A")

    Jump("loc_3D95")

    label("loc_4D9F")

    TalkEnd(0xB)
    Return()

    # Function_14_3B07 end

    def Function_15_4DA3(): pass

    label("Function_15_4DA3")

    Call(0, 16)
    Return()

    # Function_15_4DA3 end

    def Function_16_4DA7(): pass

    label("Function_16_4DA7")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DCD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E12")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4E12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E31")
    OP_AF(0x21)
    Jump("loc_4E53")

    label("loc_4E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E41")
    OP_AF(0x20)
    Jump("loc_4E53")

    label("loc_4E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E51")
    OP_AF(0x1F)
    Jump("loc_4E53")

    label("loc_4E51")

    OP_AF(0x1E)

    label("loc_4E53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DC8")

    label("loc_4E62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E76")
    Jump("loc_5DC8")

    label("loc_4E76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F55")

    #C0211
    ChrTalk(
        0xC,
        (
            "いつかはと思っていたのですが……\x01",
            "これを機会にオリジナルブランドを\x01",
            "立ち上げることに決めました。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        (
            "苦境こそ成長の糧――\x01",
            "きっと皆様にご満足いただける\x01",
            "商品を生み出してみせますわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_4F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507C")

    #C0213
    ChrTalk(
        0xC,
        (
            "大統領が強気に出れたのも、\x01",
            "全てはあの《神機》という兵器の\x01",
            "おかげだったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "……ですが、街にいる\x01",
            "あの甲冑の兵士みたいな化け物は\x01",
            "本当に何なのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "ろくに告示もせずに、あんなもので\x01",
            "国民に恐怖を与えるなんて……\x01",
            "本末転倒も甚だしいですわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5134")

    label("loc_507C")


    #C0216
    ChrTalk(
        0xC,
        (
            "……それにしても、街にいる\x01",
            "あの甲冑の兵士みたいな化け物は\x01",
            "本当に何なのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xC,
        (
            "ろくに告示もせずに、あんなもので\x01",
            "国民に恐怖を与えるなんて……\x01",
            "本末転倒も甚だしいですわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5134")

    Jump("loc_5DC8")

    label("loc_5139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5207")

    #C0218
    ChrTalk(
        0xC,
        (
            "客商売をやっているせいでしょうか。\x01",
            "私には、どうにも物事を\x01",
            "一歩引いて見る癖があるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xC,
        (
            "何と言いましょうか……\x01",
            "ディーター大統領の仰っていることは\x01",
            "かなりの暴論に聞こえましたわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52B6")

    #C0220
    ChrTalk(
        0xC,
        (
            "３日後は百貨店の職員それぞれで\x01",
            "休憩を取って投票所に行く予定ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "ちなみに、私はまだ立場を\x01",
            "決めかねているのですが……\x01",
            "ふう、どうしたものでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_52B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_536B")

    #C0222
    ChrTalk(
        0xC,
        (
            "武装集団か何だか知りませんが、\x01",
            "私にはそういった連中が\x01",
            "どうやっても理解できませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xC,
        (
            "暴力で人を押さえ付けるなんて……\x01",
            "愚の骨頂以外の何物でもありませんもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_536B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_546D")

    #C0224
    ChrTalk(
        0xC,
        (
            "最近心なしか、笑顔のお客様が\x01",
            "減って来ているような気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "昨日の列車事故もそうですし、\x01",
            "この所の世情を考えると\x01",
            "無理もないようには思いますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "せめて買い物の時くらいは\x01",
            "小難しいことを\x01",
            "忘れて欲しいものですわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_54F8")

    label("loc_546D")


    #C0227
    ChrTalk(
        0xC,
        (
            "最近心なしか、笑顔のお客様が\x01",
            "減って来ているような気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "せめて買い物の時くらいは\x01",
            "小難しいことを\x01",
            "忘れて欲しいものですわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F8")

    Jump("loc_5DC8")

    label("loc_54FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5533")

    #C0229
    ChrTalk(
        0xC,
        "あら、何やら外が騒がしいですわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_570E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564C")

    #C0230
    ChrTalk(
        0xC,
        (
            "お出かけの際などに、気分に合わせて\x01",
            "服を選ぶことはよくあると思いますが、\x01",
            "逆に服が気分を決めることもあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "たとえば落ち込んでいる時、\x01",
            "わざと明るい服装を選んでみて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "そうすれば、落ち込んだ気分を\x01",
            "吹き飛ばすことだって出来るのですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5709")

    label("loc_564C")


    #C0233
    ChrTalk(
        0xC,
        (
            "お出かけの際などに、気分に合わせて\x01",
            "服を選ぶことはよくあると思いますが、\x01",
            "逆に服が気分を決めることもあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        (
            "なりたい気分に合った服を探す……\x01",
            "そういう選び方もアリだと思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5709")

    Jump("loc_5DC8")

    label("loc_570E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57B2")

    #C0235
    ChrTalk(
        0xC,
        (
            "洋服やバッグは、高価なものほど\x01",
            "見えない所に拘る傾向があるのですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "丈夫で長く使えるものも多いですし、\x01",
            "額に見合う価値はあると思いますわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_57B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5850")

    #C0237
    ChrTalk(
        0xC,
        (
            "流行とは移ろい行くものですが、\x01",
            "誰かが生み出すものでもあるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "セレクトショップのオーナーとして、\x01",
            "私が流行を創り出してみせますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58A0")

    #C0239
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "どうぞ夜のショッピングを\x01",
            "お楽しみ下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_58A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5923")

    #C0240
    ChrTalk(
        0xC,
        "通商会議がいよいよ始まりましたわね。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xC,
        (
            "私は業界人として、各国のＶＩＰの\x01",
            "皆様のファッションが気になりますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5ACB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59E4")

    #C0242
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "トレンドを取り揃えた当店の品を\x01",
            "どうぞご覧になってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "ご試着も可能ですので、\x01",
            "どうぞお気軽にお申し付け下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AC6")

    label("loc_59E4")


    #C0244
    ChrTalk(
        0xC,
        (
            "服を扱っていた頃のハンソンさんとは\x01",
            "商売敵だったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "同時に、互いのセンスを磨き合う\x01",
            "良きライバルでもあったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        (
            "靴に傾倒するのも結構だとは思うのですが……\x01",
            "何も専門で扱わなくても良いと思うのですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5AC6")

    Jump("loc_5DC8")

    label("loc_5ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BCF")

    #C0247
    ChrTalk(
        0xC,
        (
            "雨の日だからと言って\x01",
            "オシャレをサボる人を見かけますが、\x01",
            "そんなのはナンセンスですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "ファッションはＴＰＯ――\x01",
            "むしろ雨の日だからこそ合う\x01",
            "コーディネートもあるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "お客様も、宜しければ\x01",
            "お見立てさせていただきますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5C7F")

    label("loc_5BCF")


    #C0250
    ChrTalk(
        0xC,
        (
            "雨の日だからと言って\x01",
            "オシャレをサボる人を見かけますが、\x01",
            "そんなのはナンセンスですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xC,
        (
            "ファッションはＴＰＯ――\x01",
            "むしろ雨の日だからこそ合う\x01",
            "コーディネートもあるのです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7F")

    Jump("loc_5DC8")

    label("loc_5C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D50")

    #C0252
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "ブティック《ルッカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "当店では、私自身がセレクトした\x01",
            "様々なメーカーの\x01",
            "お洋服を取り扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xC,
        "どうぞごゆっくりご覧下さいませ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DC8")

    label("loc_5D50")


    #C0255
    ChrTalk(
        0xC,
        (
            "当店では、私自身がセレクトした\x01",
            "様々なメーカーの\x01",
            "お洋服を取り扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xC,
        "どうぞごゆっくりご覧下さいませ。\x02",
    )

    CloseMessageWindow()

    label("loc_5DC8")

    Jump("loc_4DB4")

    label("loc_5DCD")

    TalkEnd(0xC)
    Return()

    # Function_16_4DA7 end

    def Function_17_5DD1(): pass

    label("Function_17_5DD1")

    Call(0, 18)
    Return()

    # Function_17_5DD1 end

    def Function_18_5DD5(): pass

    label("Function_18_5DD5")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C76")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E40")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5E40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E5F")
    OP_AF(0x11)
    Jump("loc_5E71")

    label("loc_5E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E6F")
    OP_AF(0x10)
    Jump("loc_5E71")

    label("loc_5E6F")

    OP_AF(0xF)

    label("loc_5E71")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C71")

    label("loc_5E80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E94")
    Jump("loc_6C71")

    label("loc_5E94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C71")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5F5A")

    #C0257
    ChrTalk(
        0xD,
        (
            "あの大樹を見ていると……\x01",
            "昨年リベール王国に現れたという\x01",
            "巨大構造物の話を思い出しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xD,
        (
            "幸い導力が停止するような現象は\x01",
            "起こっていないようですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_5F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_601D")

    #C0259
    ChrTalk(
        0xD,
        (
            "帝国の列車砲を防いだ時には\x01",
            "流石は国防軍とも思いましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xD,
        (
            "今の状況には\x01",
            "ただただ不安にさせられますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xD,
        (
            "『大陸諸国連合』の実現は\x01",
            "やはり机上の空論なのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_601D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D1")

    #C0262
    ChrTalk(
        0xD,
        "確かに急な話で驚きましたね……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xD,
        (
            "ですが、ディーター大統領と\x01",
            "アリオス国防長官があそこまで\x01",
            "言っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xD,
        "私は、お２人のことを信用しますよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_60D1")


    #C0265
    ChrTalk(
        0xD,
        (
            "確かに急な話で驚きましたが……\x01",
            "ディーター大統領とアリオス国防長官が\x01",
            "あそこまで言っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xD,
        "私は、お２人のことを信用しますよ。\x02",
    )

    CloseMessageWindow()

    label("loc_615F")

    Jump("loc_6C71")

    label("loc_6164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6240")

    #C0267
    ChrTalk(
        0xD,
        (
            "クロスベルが抱える数々の問題を\x01",
            "根本から解決するためには、\x01",
            "やはり独立以外に道はないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xD,
        (
            "街であんな事まで起こってしまって……\x01",
            "ここでまた両国に従った所で、\x01",
            "治安が守られるとは思えませんしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_6240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_62F4")

    #C0269
    ChrTalk(
        0xD,
        (
            "多くの方が仰る通り、\x01",
            "マインツの事件はやはり\x01",
            "帝国の陰謀ではないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "こういう事態になると、\x01",
            "自治州を守る軍隊というものが\x01",
            "ますます欲しくなりますが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_62F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6386")

    #C0271
    ChrTalk(
        0xD,
        (
            "何でも昨日の列車の脱線事故は\x01",
            "幻獣というものによって\x01",
            "引き起こされたという噂ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xD,
        "ふむ、幻獣とは一体なんなのでしょうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_6386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6416")

    #C0273
    ChrTalk(
        0xD,
        (
            "先程から救急車のサイレンが\x01",
            "けたたましく鳴っていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xD,
        (
            "まさかテロではないでしょうね。\x01",
            "……悲劇はもうたくさんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_6416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6563")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64E6")

    #C0275
    ChrTalk(
        0xD,
        (
            "アクセサリの価値は全ての人に\x01",
            "等しいものではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "この間、孫から手作りの\x01",
            "ブローチをもらったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xD,
        (
            "私にとっては、どんな\x01",
            "宝石にも勝る素晴らしい宝物ですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_655E")

    label("loc_64E6")


    #C0278
    ChrTalk(
        0xD,
        (
            "この間、孫から手作りの\x01",
            "ブローチをもらったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xD,
        (
            "私にとっては、どんな\x01",
            "宝石にも勝る素晴らしい宝物ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_655E")

    Jump("loc_6C71")

    label("loc_6563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_66AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6630")

    #C0280
    ChrTalk(
        0xD,
        (
            "ふむ、国家独立ですか。\x01",
            "随分と考えさせられる問題ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xD,
        (
            "かつて帝国を捨て、\x01",
            "クロスベルに移り住んで来た\x01",
            "私ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xD,
        (
            "これは、とんでもない\x01",
            "難問と言わざると得ません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66A9")

    label("loc_6630")


    #C0283
    ChrTalk(
        0xD,
        (
            "かつて帝国を捨て、\x01",
            "クロスベルに移り住んで来た\x01",
            "私ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xD,
        (
            "国家独立の提唱に関しては\x01",
            "難問と言わざると得ません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A9")

    Jump("loc_6C71")

    label("loc_66AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_673A")

    #C0285
    ChrTalk(
        0xD,
        (
            "ふむ、ついにいよいよ\x01",
            "通商会議の本番が始まるわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "とにかく、何としてでも\x01",
            "有意義な会議にして欲しいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_673A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67FA")

    #C0287
    ChrTalk(
        0xD,
        "すっかり日も暮れましたね。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        (
            "そういえば、首脳たちによる\x01",
            "アルカンシェルの観劇は\x01",
            "もうそろそろ終わる頃でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xD,
        (
            "ふむ、楽しんで\x01",
            "くれているといいのですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_687F")

    label("loc_67FA")


    #C0290
    ChrTalk(
        0xD,
        (
            "そういえば、首脳たちによる\x01",
            "アルカンシェルの観劇は\x01",
            "もうそろそろ終わる頃でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "ふむ、楽しんで\x01",
            "くれているといいのですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687F")

    Jump("loc_6C71")

    label("loc_6884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_691A")

    #C0292
    ChrTalk(
        0xD,
        (
            "年甲斐もなく屋上に出て\x01",
            "除幕式の様子を拝見したのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "オルキスタワーは実に見事ですね。\x01",
            "しばし言葉を失ってしまいましたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_691A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6A5E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69CC")

    #C0294
    ChrTalk(
        0xD,
        (
            "いらっしゃいませ。\x01",
            "アクセサリ《ベイカー》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        (
            "何か気になるものがございましたら\x01",
            "どうぞ手に取ってご覧くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A59")

    label("loc_69CC")


    #C0296
    ChrTalk(
        0xD,
        (
            "当百貨店に来るお客様は\x01",
            "何と言いますか、\x01",
            "心の暖かい方が多いのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        (
            "比べるものではありませんが、\x01",
            "帝国貴族の連中とは大違いですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A59")

    Jump("loc_6C71")

    label("loc_6A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B60")

    #C0298
    ChrTalk(
        0xD,
        (
            "雨が降ると、なぜか帝国で\x01",
            "美術商をしていた頃のことを\x01",
            "よく思い出します。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xD,
        (
            "あの頃の私と言えば、\x01",
            "美術品の価値を釣り上げる事ばかりに\x01",
            "苦心する毎日を送っていたものですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "ふう、思い返すだけで\x01",
            "息が詰まりそうになりますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BD4")

    label("loc_6B60")


    #C0301
    ChrTalk(
        0xD,
        (
            "すみません、つまらない\x01",
            "身の上話を聞かせてしまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "いらっしゃいませ。\x01",
            "どうぞごゆるりとご覧下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD4")

    Jump("loc_6C71")

    label("loc_6BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6C71")

    #C0303
    ChrTalk(
        0xD,
        (
            "いらっしゃいませ。\x01",
            "どうぞご覧になって行って下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "当店のアクセサリや小物類は\x01",
            "大切な方へのプレゼントや\x01",
            "自分へのご褒美に最適ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C71")

    Jump("loc_5DE2")

    label("loc_6C76")

    TalkEnd(0xD)
    Return()

    # Function_18_5DD5 end

    def Function_19_6C7A(): pass

    label("Function_19_6C7A")

    SetScenarioFlags(0x2, 4)
    Call(0, 20)
    Return()

    # Function_19_6C7A end

    def Function_20_6C81(): pass

    label("Function_20_6C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DB0")
    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2B")

    #C0305
    ChrTalk(
        0xE,
        (
            "あれ、君たちは\x01",
            "一体どこから入ったんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        "ま、いっか。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xE,
        (
            "とりあえず、買い物したいなら\x01",
            "ちゃんとカウンター越しに\x01",
            "言ってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6DAC")

    label("loc_6D2B")


    #C0308
    ChrTalk(
        0xE,
        (
            "とりあえず、買い物したいなら\x01",
            "ちゃんとカウンター越しに\x01",
            "言ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xE,
        (
            "あと、その辺の在庫品には\x01",
            "あまり触らないようにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DAC")

    TalkEnd(0xE)
    Return()

    label("loc_6DB0")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_735E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA5")

    #C0310
    ChrTalk(
        0xE,
        (
            "やあ、いらっしゃい。\x01",
            "雑貨コーナー《サザーク》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        (
            "ウチの店では日用品からお土産まで、\x01",
            "バラエティに富んだ商品を扱っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xE,
        "よければ、じっくり見て行ってくれよな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6F24")

    label("loc_6EA5")


    #C0313
    ChrTalk(
        0xE,
        (
            "ウチの店では日常用品からお土産まで、\x01",
            "バラエティに富んだ商品を扱っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xE,
        "よければ、じっくり見て行ってくれよな。\x02",
    )

    CloseMessageWindow()

    label("loc_6F24")

    TalkEnd(0xE)
    Return()

    label("loc_6F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A6")
    SetChrName("")

    #A0315
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは店主のサザークに\x01",
            "小声で話しかけた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00000F（すみません、\x01",
            "  『チクタクみっしぃ』という\x01",
            "  商品はおいくらですかね？）\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xE,
        "（ああ、５００ミラだけど。）\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xE,
        (
            "（ふふ、もしかしてそこの\x01",
            "  お子さんにプレゼントかい？）\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#00012F（ああはい、まだ考え中ですが。）\x02\x03",

            "#00003F（５００ミラか……\x01",
            "  どうする、シンのために買うか？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_7104")

    label("loc_70A6")


    #C0320
    ChrTalk(
        0xE,
        (
            "（チクタクみっしぃは５００ミラだよ。\x01",
            "  買って行くかい？）\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        "#00000F（そうですね……）\x02",
    )

    CloseMessageWindow()

    label("loc_7104")

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
            "『チクタクみっしぃ』を購入する\x01",      # 0
            "もう少し考える\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72AD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_71ED")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    #C0322
    ChrTalk(
        0x101,
        "#00000F（えっとじゃあ、それもらえますか。）\x02",
    )

    CloseMessageWindow()
    Sound(20, 0, 80, 0)

    #C0323
    ChrTalk(
        0xE,
        "（了解、まいどあり。）\x02",
    )

    CloseMessageWindow()
    Call(0, 52)
    Jump("loc_72A8")

    label("loc_71ED")


    #C0324
    ChrTalk(
        0x101,
        "#00000F（えっとじゃあ、それを……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0325
    ChrTalk(
        0x101,
        (
            "#00006F（ミラがない……\x01",
            "  はぁ、俺はどれだけ赤貧なんだ。）\x02\x03",

            "#00000F（すみません、やっぱり大丈夫です。）\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xE,
        "（？？？）\x02",
    )

    CloseMessageWindow()

    label("loc_72A8")

    Jump("loc_72E5")

    label("loc_72AD")


    #C0327
    ChrTalk(
        0x101,
        (
            "#00003F（とりあえず、\x01",
            "  もう少し考えてみるか……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E5")

    TalkEnd(0xE)
    Return()

    label("loc_72EE")


    #C0328
    ChrTalk(
        0xE,
        (
            "どうやらプレゼントは\x01",
            "喜んでもらえたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xE,
        (
            "う～ん、だけどやっぱり\x01",
            "みっしぃって偉大だよなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    label("loc_735E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7368")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85E5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73C6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_73C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_73E5")
    OP_AF(0x1D)
    Jump("loc_7467")

    label("loc_73E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_73F5")
    OP_AF(0x1C)
    Jump("loc_7467")

    label("loc_73F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7405")
    OP_AF(0x1B)
    Jump("loc_7467")

    label("loc_7405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7415")
    OP_AF(0x1A)
    Jump("loc_7467")

    label("loc_7415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7425")
    OP_AF(0x19)
    Jump("loc_7467")

    label("loc_7425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7435")
    OP_AF(0x18)
    Jump("loc_7467")

    label("loc_7435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_7445")
    OP_AF(0x17)
    Jump("loc_7467")

    label("loc_7445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7455")
    OP_AF(0x16)
    Jump("loc_7467")

    label("loc_7455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7465")
    OP_AF(0x15)
    Jump("loc_7467")

    label("loc_7465")

    OP_AF(0x14)

    label("loc_7467")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85E0")

    label("loc_7476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_748A")
    Jump("loc_85E0")

    label("loc_748A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7557")

    #C0330
    ChrTalk(
        0xE,
        (
            "商売人に出来ることってのは\x01",
            "やっぱり商売を\x01",
            "続けること以外にないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xE,
        (
            "国外の流通ルートは流石に\x01",
            "再開の目処が立たないけど……\x01",
            "知恵を振り絞って乗り切らないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_7557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_75E7")

    #C0332
    ChrTalk(
        0xE,
        (
            "こういう時に大切な人が\x01",
            "傍にいてくれると本当に安心するね。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xE,
        (
            "なんていうか、腹の底から\x01",
            "勇気が湧いてくるような感じがするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_75E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_77E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7774")

    #C0334
    ChrTalk(
        0xE,
        (
            "今朝突然、クロスベルに在留している\x01",
            "共和国人に向けて、共和国政府から\x01",
            "早々の帰国を促す通達が来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xE,
        (
            "もはや実力行使も辞さないという話だし、\x01",
            "これからどんな事態になって行くのかは\x01",
            "想像に難くないところだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xE,
        (
            "このクロスベルには\x01",
            "今の僕にとって、何よりも\x01",
            "大切な彼女がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xE,
        (
            "だから、たとえ\x01",
            "どんなことが起きようとも\x01",
            "僕はこの地に留まることを決めたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_77E3")

    label("loc_7774")


    #C0338
    ChrTalk(
        0xE,
        (
            "たとえどんなことが起きようとも\x01",
            "僕はこの地に留まることを決めたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xE,
        "そして必ず彼女を守ってみせるんだ。\x02",
    )

    CloseMessageWindow()

    label("loc_77E3")

    Jump("loc_85E0")

    label("loc_77E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_787A")

    #C0340
    ChrTalk(
        0xE,
        (
            "せっかくのリニューアル舞台が、\x01",
            "そしてイリアさんがあんなことに……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xE,
        (
            "襲撃の時は恐怖しかなかったけど……\x01",
            "今は怒りで一杯だよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_787A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_797B")

    #C0342
    ChrTalk(
        0xE,
        (
            "『金の太陽、銀の月』の\x01",
            "リニューアル版公開は\x01",
            "いよいよ今日の夕方だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xE,
        (
            "マインツの状況を考えると\x01",
            "流石に浮かれ気分ってわけには\x01",
            "いかないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        (
            "舞台は舞台だし、\x01",
            "勇気と元気を貰う意味でも\x01",
            "うんと楽しませてもらって来るよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7A17")

    label("loc_797B")


    #C0345
    ChrTalk(
        0xE,
        (
            "マインツの状況を考えると\x01",
            "流石に浮かれ気分ってわけには\x01",
            "いかないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xE,
        (
            "舞台は舞台だし、\x01",
            "勇気と元気を貰う意味でも\x01",
            "うんと楽しませてもらって来るよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A17")

    Jump("loc_85E0")

    label("loc_7A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7AB5")

    #C0347
    ChrTalk(
        0xE,
        (
            "今まで商売一筋だったけど、\x01",
            "彼女ができてから\x01",
            "まるで世界が違って見えるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xE,
        (
            "なんていうか……\x01",
            "こういうのを幸せって言うんだろうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_7AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7B20")

    #C0349
    ChrTalk(
        0xE,
        (
            "何だか、西の方で\x01",
            "列車事故があったって大騒ぎだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xE,
        "テロじゃなければいいんだけど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_7B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE9")

    #C0351
    ChrTalk(
        0xE,
        (
            "独立の是非を問う住民投票か……\x01",
            "あくまで意志確認とはいうものの\x01",
            "何気に責任重大な話だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xE,
        (
            "僕は共和国の人間だから\x01",
            "投票することはできないけど、\x01",
            "凄く考えさせられるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7C5D")

    label("loc_7BE9")


    #C0353
    ChrTalk(
        0xE,
        "独立の是非を問う住民投票か……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xE,
        (
            "僕は共和国の人間だから\x01",
            "投票することはできないけど、\x01",
            "凄く考えさせられるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C5D")

    Jump("loc_85E0")

    label("loc_7C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D0E")

    #C0355
    ChrTalk(
        0xE,
        (
            "最初は可愛い妹みたいな\x01",
            "つもりだったんだけど……\x01",
            "人の気持ちって分からないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "とにかく今の僕は幸せだ。\x01",
            "ホント勇気を出して良かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7D94")

    label("loc_7D0E")


    #C0357
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃん、最初は可愛い\x01",
            "妹みたいなつもりだったんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xE,
        (
            "とにかく今の僕は幸せだ。\x01",
            "ホント勇気を出して良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D94")

    Jump("loc_85E0")

    label("loc_7D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E4D")

    #C0359
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃんは昨日、\x01",
            "リッチな男性たちと食事をしたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xE,
        "そして見事玉砕したらしいんだけど……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xE,
        "う～ん、僕は何でほっとしてるんだろう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7EA5")

    label("loc_7E4D")


    #C0362
    ChrTalk(
        0xE,
        "う～ん、僕は何でほっとしてるんだろう。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xE,
        "これはつまり、僕にそういう気持ちが……\x02",
    )

    CloseMessageWindow()

    label("loc_7EA5")

    Jump("loc_85E0")

    label("loc_7EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F82")

    #C0364
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃんが、\x01",
            "今朝からやけに楽しそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        (
            "明日にはスーパージャネッタに\x01",
            "生まれ変わってるとか、\x01",
            "よく分からない事を言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xE,
        "何だろう、何故だか凄く気になるぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7FE3")

    label("loc_7F82")


    #C0367
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃんが、\x01",
            "今朝からやけに楽しそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xE,
        "何だろう、何故だか凄く気になるぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_7FE3")

    Jump("loc_85E0")

    label("loc_7FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_815F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80E3")

    #C0369
    ChrTalk(
        0xE,
        (
            "除幕式か～、僕は見れなかったけど\x01",
            "さぞかし凄かったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xE,
        (
            "いつもはニュース誌なんかでしか\x01",
            "お目に掛かれない各国の首脳たちが\x01",
            "集まってるんだから凄いよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "次号のクロスベルタイムズが\x01",
            "今から楽しみで仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_815A")

    label("loc_80E3")


    #C0372
    ChrTalk(
        0xE,
        (
            "除幕式か～、\x01",
            "さぞかし凄かったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xE,
        (
            "とりあえず、\x01",
            "次号のクロスベルタイムズが\x01",
            "今から楽しみで仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_815A")

    Jump("loc_85E0")

    label("loc_815F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_83FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8352")

    #C0374
    ChrTalk(
        0xE,
        (
            "アルカンシェルの舞台\x01",
            "『金の太陽、銀の月』がリニューアル\x01",
            "されるって話を知ってるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xE,
        (
            "詳細はまだ一切未公表なんだけど、\x01",
            "かなり大胆な演出を追加するらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xE,
        (
            "ふふふ、そして何と……\x01",
            "実はその公開初日のチケットを\x01",
            "２枚ゲットすることに成功したんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x104,
        (
            "#00305Fへえ、そいつは景気のいい話だな。\x02\x03",

            "#00309Fちなみに相手は誰なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        "う……それは聞かないでくれるかな。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xE,
        (
            "と、とにかく、公開まで\x01",
            "まだ１ヶ月ちょっとあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xE,
        "それまでには何とかなるさ、うん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_83F5")

    label("loc_8352")


    #C0381
    ChrTalk(
        0xE,
        (
            "アルカンシェルのリニューアル舞台、\x01",
            "その初回公演のチケットを\x01",
            "幸運にも２枚ゲットできたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xE,
        (
            "ま、一緒に行ってくれる相手は\x01",
            "これから探すところなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83F5")

    Jump("loc_85E0")

    label("loc_83FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8415")
    Call(0, 21)
    Jump("loc_8454")

    label("loc_8415")


    #C0383
    ChrTalk(
        0xE,
        (
            "誕生日とかならまだ分かるけど……\x01",
            "普通にねだられてもなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8454")

    Jump("loc_85E0")

    label("loc_8459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_85E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8585")

    #C0384
    ChrTalk(
        0xE,
        (
            "やあ、いらっしゃい。\x01",
            "雑貨コーナー《サザーク》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xE,
        (
            "最近、お客さんの熱い要望に応えて\x01",
            "みっしぃグッズを強化したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xE,
        "興味があったら、ぜひ見て行くといいよ。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#00002Fへえ、みっしぃグッズか。\x01",
            "ティオが聞いたら喜びそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x102,
        "#00102Fふふ、確かにね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_85E0")

    label("loc_8585")


    #C0389
    ChrTalk(
        0xE,
        (
            "みっしぃグッズは\x01",
            "おかげ様で大好評なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        "興味があったら、ぜひ見て行くといいよ。\x02",
    )

    CloseMessageWindow()

    label("loc_85E0")

    Jump("loc_7368")

    label("loc_85E5")

    TalkEnd(0xE)
    Return()

    # Function_20_6C81 end

    def Function_21_85E9(): pass

    label("Function_21_85E9")

    OP_4B(0x12, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0391
    ChrTalk(
        0x12,
        (
            "あ、みっしぃぐるみだ、かわいいな～。\x01",
            "サザークさん、これください。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        (
            "ああ、うん。\x01",
            "えっと５００ミラになるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x12,
        (
            "じゃなくて。\x01",
            "プレゼントしてくださいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xE,
        "プレゼントって、何でまた僕が？\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x12,
        "同じ百貨店で働いているから。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0396
    ChrTalk(
        0xE,
        (
            "いやいやいや、\x01",
            "そんなの理由にならないから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x12, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_21_85E9 end

    def Function_22_8739(): pass

    label("Function_22_8739")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_88B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8831")

    #C0397
    ChrTalk(
        0xFE,
        (
            "戒厳令が解除されたと思えば\x01",
            "謎の大樹が出現……\x01",
            "そして２大国の脅威も残された現状……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "この未曾有の困難に対して、\x01",
            "自分という人間に何が出来るのか――\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "一人一人が着実に考え、\x01",
            "そして行動していくしかありません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_88B3")

    label("loc_8831")


    #C0400
    ChrTalk(
        0xFE,
        (
            "この未曾有の困難に対して、\x01",
            "自分という人間に何が出来るのか――\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "一人一人が着実に考え、\x01",
            "そして行動していくしかありません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88B3")

    Jump("loc_9AD0")

    label("loc_88B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88D3")
    Call(0, 23)
    Jump("loc_894B")

    label("loc_88D3")


    #C0402
    ChrTalk(
        0xFE,
        (
            "ロイド様のおっしゃる通り、\x01",
            "このまま外出禁止令に従って\x01",
            "様子を見たいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        "……どうか皆様もお気を付けて。\x02",
    )

    CloseMessageWindow()

    label("loc_894B")

    Jump("loc_9AD0")

    label("loc_8950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A57")

    #C0404
    ChrTalk(
        0xFE,
        (
            "住民投票からわずか一週間で\x01",
            "ここまでの事態になろうとは……\x01",
            "流石に想像だに出来ませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "とにかく、恐らくこの先は\x01",
            "何が起きても不思議ではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "この百貨店を存続させるためにも、\x01",
            "色々と考えを尽くす必要がありますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8AE3")

    label("loc_8A57")


    #C0407
    ChrTalk(
        0xFE,
        (
            "とにかく、恐らくこの先は\x01",
            "何が起きても不思議ではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "この百貨店を存続させるためにも、\x01",
            "色々と考えを尽くす必要がありますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AE3")

    Jump("loc_9AD0")

    label("loc_8AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C03")

    #C0409
    ChrTalk(
        0xFE,
        (
            "本日、市民会館にて街の復興支援を\x01",
            "テーマとしたチャリティイベントが\x01",
            "開催されております。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "市と商工会が一体となり、\x01",
            "住民を元気付けようと\x01",
            "立ち上がったこの企画……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "当百貨店も全面的に協力して\x01",
            "盛り上げておりますので、\x01",
            "是非一度お立ち寄り下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8CB7")

    label("loc_8C03")


    #C0412
    ChrTalk(
        0xFE,
        (
            "本日、市民会館にて街の復興支援を\x01",
            "テーマとしたチャリティイベントが\x01",
            "開催されております。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "当百貨店も全面的に協力して\x01",
            "盛り上げておりますので、\x01",
            "是非一度お立ち寄り下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB7")

    Jump("loc_9AD0")

    label("loc_8CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8D71")

    #C0414
    ChrTalk(
        0xFE,
        (
            "謎の武装集団がマインツを占拠……\x01",
            "この状況、まるで紛争時代の悪夢が\x01",
            "蘇ったかのようで居た堪れません。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "とにかく一刻でも早く、\x01",
            "事態が収まって欲しいものですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_8D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8C")
    Call(0, 26)
    Jump("loc_8EF9")

    label("loc_8D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E89")

    #C0416
    ChrTalk(
        0xFE,
        (
            "何でも、昨日の列車脱線事故は\x01",
            "巨大な鬼のような化物によって\x01",
            "引き起こされたらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "最近、自治州各地において\x01",
            "大型の不可思議な魔獣が\x01",
            "出現するという噂もあるようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "ふむ、両者には何か\x01",
            "因果関係があるのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8EF9")

    label("loc_8E89")


    #C0419
    ChrTalk(
        0xFE,
        (
            "巨大な鬼のような化物、\x01",
            "それに大型の不可思議な魔獣……\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "ふむ、両者には何か\x01",
            "因果関係があるのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EF9")

    Jump("loc_9AD0")

    label("loc_8EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8FBA")

    #C0421
    ChrTalk(
        0xFE,
        (
            "駅の方面からいらっしゃった\x01",
            "お客様から伺ったのですが、\x01",
            "どうやら列車が脱線したらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "詳細は分かりませんが……\x01",
            "とにかく救急車で\x01",
            "運ばれた方々のことが心配です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_8FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9086")

    #C0423
    ChrTalk(
        0xFE,
        (
            "最近、色々なお客様の口から\x01",
            "国家独立の是非についての\x01",
            "お話を伺うようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "前向きな意見も多いのですが、\x01",
            "２大国の意向を踏まえると当然ながら\x01",
            "不安に思われる方も多いようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_9086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_918B")

    #C0425
    ChrTalk(
        0xFE,
        (
            "今思うと、先日の通商会議は\x01",
            "まさに嵐のような出来事でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "テロリストの襲撃もそうですが、\x01",
            "何よりディーター市長の提唱には\x01",
            "驚かされました。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "この提唱がどのような形で\x01",
            "国際世論に訴えていく事になるのか……\x01",
            "今後の情勢に目が離せませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_918B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92A1")

    #C0428
    ChrTalk(
        0xFE,
        (
            "本日も、当店の屋上には\x01",
            "オルキスタワーの見物を目当てに\x01",
            "多くの方がいらっしゃっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "おかげ様で客足も伸び、\x01",
            "売り上げの方も好調でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "ですが、何よりも\x01",
            "この賑やかな雰囲気が嬉しいですね。\x01",
            "接客の方も楽しませて頂いておりますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_934C")

    label("loc_92A1")


    #C0431
    ChrTalk(
        0xFE,
        (
            "本日も、当店の屋上には\x01",
            "オルキスタワーの見物を目当てに\x01",
            "多くの方がいらっしゃっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "普段は見られない賑わいがあって、\x01",
            "接客の方も楽しませて頂いておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_934C")

    Jump("loc_9AD0")

    label("loc_9351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_93DE")

    #C0433
    ChrTalk(
        0xFE,
        (
            "本日の営業は通常通り\x01",
            "２０：００をもって\x01",
            "終了とさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        (
            "お買い忘れやお忘れ物のないよう\x01",
            "お気を付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_93DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94EB")

    #C0435
    ChrTalk(
        0xFE,
        (
            "恥ずかしながら、お客様に交じって\x01",
            "除幕式を拝見させて頂いたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "《オルキスタワー》の威容には\x01",
            "ただただ息を呑むばかりでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "流石は地上４０階の超高層ビル……\x01",
            "まさにこのクロスベルの新たな\x01",
            "象徴に相応しいと言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9551")

    label("loc_94EB")


    #C0438
    ChrTalk(
        0xFE,
        (
            "流石は地上４０階の超高層ビル……\x01",
            "まさにこのクロスベルの新たな\x01",
            "象徴に相応しいと言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9551")

    Jump("loc_9AD0")

    label("loc_9556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_98B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_970B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9698")
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    #C0439
    ChrTalk(
        0x11,
        (
            "おや、これはエリィお嬢様。\x01",
            "今日は珍しい客人をお連れですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x102,
        (
            "#00100Fええ、今はこの子にクロスベルを\x01",
            "案内している所なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x11,
        (
            "なるほど、それで当店に\x01",
            "足を運んで頂けるとは幸いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x11,
        (
            "ではどうか、ごゆるりと\x01",
            "素敵な一時をお過ごし下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9706")

    label("loc_9698")


    #C0443
    ChrTalk(
        0x11,
        (
            "本日も当店に足を運んで頂けて\x01",
            "喜ばしい限りです。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x11,
        (
            "どうか、ごゆるりと\x01",
            "素敵な一時をお過ごし下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9706")

    Jump("loc_98AC")

    label("loc_970B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_982C")

    #C0445
    ChrTalk(
        0xFE,
        (
            "明日、いよいよ\x01",
            "通商会議が開催されますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州と、それを取り巻く\x01",
            "４ヶ国の代表者が一同に会する……\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "この数十年を振り返って考えると、\x01",
            "ただそれだけでも歴史的に\x01",
            "大変、意義のあることですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "何と言いましょうか、\x01",
            "気持ちの昂ぶりを感じますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_98AC")

    label("loc_982C")


    #C0449
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州と、それを取り巻く\x01",
            "４ヶ国の代表者が一同に会する……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "何と言いましょうか、\x01",
            "気持ちの昂ぶりを感じますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98AC")

    Jump("loc_9AD0")

    label("loc_98B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_997A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98CC")
    Call(0, 24)
    Jump("loc_9975")

    label("loc_98CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98DE")
    Call(0, 25)
    Jump("loc_9975")

    label("loc_98DE")


    #C0451
    ChrTalk(
        0x11,
        (
            "当店では雨の日にご来店頂いた\x01",
            "お客様にささやかな\x01",
            "プレゼントをご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x11,
        (
            "どうか皆様、本日は心ゆくまで\x01",
            "ショッピングをお楽しみ下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9975")

    Jump("loc_9AD0")

    label("loc_997A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9995")
    Call(0, 24)
    Jump("loc_9AD0")

    label("loc_9995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A5A")

    #C0453
    ChrTalk(
        0xFE,
        (
            "皆様、本日は\x01",
            "百貨店《タイムズ》へのご来店、\x01",
            "誠に有難うございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "当店には、お客様の目を引く\x01",
            "様々な売り場をご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        "どうかごゆっくりご堪能下さいませ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9AD0")

    label("loc_9A5A")


    #C0456
    ChrTalk(
        0xFE,
        (
            "当百貨店には、お客様の目を引く\x01",
            "様々な売り場をご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "皆様、どうか\x01",
            "ごゆっくりご堪能下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AD0")

    TalkEnd(0xFE)
    Return()

    # Function_22_8739 end

    def Function_23_9AD4(): pass

    label("Function_23_9AD4")

    OP_4B(0x11, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    #C0458
    ChrTalk(
        0x11,
        "エリィお嬢様に支援課の皆様……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        "もしかして、外出禁止令が……？\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#00003Fいえ……残念ながら\x01",
            "解除はされていません。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        "そうですか……\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x102,
        (
            "#00101Fネストンさん、百貨店の\x01",
            "状況を聞かせて頂けますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x11,
        (
            "はい、昨日はお客様の\x01",
            "ご要望もあり戒厳令が出た後も\x01",
            "ギリギリまで店を開いておりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x11,
        (
            "その内にあのモヤが出て来て、\x01",
            "直後に駆け込んで来たお客様と\x01",
            "職員全員が留まっている状態です。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x8,
        (
            "一晩経てば新しいアナウンスも\x01",
            "出ると思っていたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        (
            "本当に、政府はいったい\x01",
            "何を考えているのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#00200F……なるほど、\x01",
            "やはり猶予はありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x101,
        (
            "#00001F支配人、俺たちは今、\x01",
            "この事態を収束すべく\x01",
            "行動しています。\x02\x03",

            "どうか外が落ち着くまでは、\x01",
            "皆さんを屋外に出さないよう\x01",
            "引き続き宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x11,
        (
            "かしこまりました。\x01",
            "……どうか皆様もお気を付けて。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x11,
        (
            "そうだ、せっかくですので\x01",
            "お守り代わりに\x01",
            "こちらをお持ち下さい。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FD, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0472
    ChrTalk(
        0x102,
        (
            "#00100Fネストンさん……\x01",
            "どうも有難うございます。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1BB, 4)
    Return()

    # Function_23_9AD4 end

    def Function_24_9ED5(): pass

    label("Function_24_9ED5")


    #C0473
    ChrTalk(
        0x11,
        (
            "いらっしゃいませ。\x01",
            "百貨店《タイムズ》へようこそ。\x02",
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
        "これはこれは、エリィお嬢様。\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x11,
        (
            "マクダエル議長とご一緒に\x01",
            "諸国を巡られていたそうですが、\x01",
            "お戻りになられたのですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x102,
        (
            "#00100Fはい、つい先日に。\x02\x03",

            "これからはまた、特務支援課で\x01",
            "活動するので宜しくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x11,
        (
            "ええ、勿論ですとも。\x01",
            "益々のご清栄をお祈りしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x109,
        (
            "#10105Fエリィさん、百貨店の\x01",
            "支配人さんとお知り合いなんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#00100Fええ、おじいさまの昔からの知り合いで\x01",
            "ずっと良くしてもらっているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、さすがは議長令嬢……\x01",
            "さぞかし融通も利くんじゃない？\x02\x03",

            "例えば、連れである僕らごと\x01",
            "ＶＩＰ待遇にしてもらえるとか。\x02",
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
            "いえ、その点につきましては\x01",
            "お嬢様より決して特別扱いせぬよう\x01",
            "承っておりますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x11,
        (
            "他のお客様と同様のサービスで\x01",
            "ご対応させて頂いております。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x102,
        (
            "#00104Fふふ、そういうこと。\x01",
            "残念だったわね、ワジ君。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x105,
        "#10306Fやれやれ、真面目だねえ。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#00000Fはは、確かに少し勿体無いかもな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 3)
    Return()

    # Function_24_9ED5 end

    def Function_25_A29D(): pass

    label("Function_25_A29D")


    #C0486
    ChrTalk(
        0x11,
        (
            "皆様、本日はお足もとの悪い中、\x01",
            "ご来店頂き有難うございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x11,
        "宜しければ、こちらをどうぞ。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0489
    ChrTalk(
        0x102,
        "#00105Fネストンさん、これは……？\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x11,
        (
            "ええ、雨の日にも関わらず\x01",
            "ご来店下さったお客様への\x01",
            "ささやかな感謝の気持ちです。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x11,
        (
            "１日１００名様限定で、\x01",
            "先月よりサービスを\x01",
            "開始させて頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#00000Fなるほど、これは\x01",
            "嬉しいサービスですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x109,
        (
            "#10100Fええ、それに\x01",
            "何だか雨が楽しくなりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x11,
        (
            "ありがとうございます。\x01",
            "そう仰って頂けると幸いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x11,
        (
            "それでは皆様、どうか雨の日の\x01",
            "ショッピングをお楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 4)
    Return()

    # Function_25_A29D end

    def Function_26_A4FA(): pass

    label("Function_26_A4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_END)), "loc_A65B")

    #C0496
    ChrTalk(
        0x11,
        "本日もご来店、有難うございます。\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x11,
        "宜しければ、こちらをどうぞ。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0499
    ChrTalk(
        0x101,
        "#00000Fああ、雨の日のサービスですね。\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#00100Fどうも、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x11,
        (
            "いえ、こちらこそ\x01",
            "いつも有難うございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x11,
        (
            "どうか皆様、雨の日の\x01",
            "ショッピングをお楽しみ下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8AE")

    label("loc_A65B")


    #C0503
    ChrTalk(
        0x11,
        (
            "本日はお足もとの悪い中、\x01",
            "ご来店頂き有難うございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x11,
        "宜しければ、こちらをどうぞ。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0506
    ChrTalk(
        0x102,
        "#00105Fネストンさん、これは……？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x11,
        (
            "ええ、雨の日にも関わらず\x01",
            "ご来店下さったお客様への\x01",
            "ささやかな感謝の気持ちです。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x11,
        (
            "１日１００名様限定で、\x01",
            "先月よりサービスを\x01",
            "開始させて頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど、これは\x01",
            "嬉しいサービスですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x109,
        (
            "#10100Fええ、それに\x01",
            "何だか雨が楽しくなりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x11,
        (
            "ありがとうございます。\x01",
            "そう仰って頂けると幸いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x11,
        (
            "それでは皆様、どうか雨の日の\x01",
            "ショッピングをお楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8AE")

    SetScenarioFlags(0x16C, 5)
    Return()

    # Function_26_A4FA end

    def Function_27_A8B2(): pass

    label("Function_27_A8B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A95D")

    #C0513
    ChrTalk(
        0xFE,
        (
            "この苦難を乗り越えようと\x01",
            "百貨店スタッフは\x01",
            "全員がやる気満々マンです。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        (
            "私もやる気満々マン……\x01",
            "いや、やる気満々レディとして\x01",
            "全力でがんばりまっす！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_A95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A9EF")

    #C0515
    ChrTalk(
        0xFE,
        (
            "正直不安な気持ちで一杯なんですが……\x01",
            "サザークさんの顔を見ていると\x01",
            "心が落ち着くんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        "ふふ、なんだか不思議な感覚ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_A9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AA92")

    #C0517
    ChrTalk(
        0xFE,
        (
            "サザークさん、\x01",
            "私のためにクロスベルに\x01",
            "残ってくれるって言うんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        (
            "こんな状況で言うことではないとは\x01",
            "思いますけど……私、今とても幸せです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AB2B")

    #C0519
    ChrTalk(
        0xFE,
        (
            "……いくら忘れようと思っても\x01",
            "アルカンシェルが襲撃された時の\x01",
            "恐怖は本当に忘れられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xFE,
        (
            "犯人が一体、\x01",
            "何が目的であんなことを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AB2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_ACA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC24")

    #C0521
    ChrTalk(
        0xFE,
        (
            "今日は早引けして、待ちに待った\x01",
            "アルカンシェルのリニューアル舞台を\x01",
            "観に行く予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "何といっても、この所ずっと\x01",
            "楽しみにしてきた舞台ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        (
            "一瞬たりとも見逃さないように\x01",
            "集中して観劇するつもりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ACA4")

    label("loc_AC24")


    #C0524
    ChrTalk(
        0xFE,
        (
            "何といっても、この所ずっと\x01",
            "楽しみにしてきた舞台ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "一瞬たりとも見逃さないように\x01",
            "集中して観劇するつもりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACA4")

    Jump("loc_B1C8")

    label("loc_ACA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AD6D")

    #C0526
    ChrTalk(
        0xFE,
        (
            "明日はいよいよアルカンシェルの舞台\x01",
            "『金の太陽、銀の月』、\x01",
            "リニューアル版の公開日ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "サザークさんと一緒に\x01",
            "観に行く予定なんですけど、\x01",
            "ホント、今からすっごく楽しみです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AD6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_ADD1")

    #C0528
    ChrTalk(
        0xFE,
        "きゅ、救急車がいっぱい通りましたね。\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        "病院に運ばれた方々のことが心配です……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_ADD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AE77")

    #C0530
    ChrTalk(
        0xFE,
        (
            "結局、国家として独立すると\x01",
            "どんなメリットがあるんでしょうか？\x01",
            "私、難しいことはよく分からなくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        "そうだ、サザークさんに教えてもらおっと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AE77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AE85")
    Jump("loc_B1C8")

    label("loc_AE85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AFDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF8B")

    #C0532
    ChrTalk(
        0xFE,
        (
            "はあ、昨日は絶対に\x01",
            "うまく行くと思ったんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "そりゃあ確かに\x01",
            "シンシア先輩は魅力的ですよ。\x01",
            "女の私でも惚れちゃうくらいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xFE,
        (
            "でも、だからと言って１人くらい\x01",
            "私に興味を持ってくれる人がいたって\x01",
            "いいじゃないですか～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AFD7")

    label("loc_AF8B")


    #C0535
    ChrTalk(
        0xFE,
        (
            "シクシク……\x01",
            "私の魅力を分かってくれる人は\x01",
            "一体どこにいるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFD7")

    Jump("loc_B1C8")

    label("loc_AFDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B04F")

    #C0536
    ChrTalk(
        0xFE,
        (
            "お洋服は準備オッケーだし、\x01",
            "お化粧のノリもバッチリです。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xFE,
        "うふふ、今夜の私は一味違いますよ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_B04F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B16D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0EC")

    #C0538
    ChrTalk(
        0xFE,
        (
            "うふふ、世の中には積極的な\x01",
            "お客さんもいらっしゃるんですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        (
            "合コンなんて一体いつぶりだろう。\x01",
            "早く夜にならないかな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B168")

    label("loc_B0EC")


    #C0540
    ChrTalk(
        0xFE,
        (
            "それもお相手は皆さん、\x01",
            "港湾区で働いていらっしゃる\x01",
            "ビジネスマンってヤツなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xFE,
        "これはチャンス、チャンスですよ！\x02",
    )

    CloseMessageWindow()

    label("loc_B168")

    Jump("loc_B1C8")

    label("loc_B16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B17B")
    Jump("loc_B1C8")

    label("loc_B17B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B1BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B196")
    Call(0, 21)
    Jump("loc_B1BA")

    label("loc_B196")


    #C0542
    ChrTalk(
        0xFE,
        "ぶう、サザークさんのいけず～。\x02",
    )

    CloseMessageWindow()

    label("loc_B1BA")

    Jump("loc_B1C8")

    label("loc_B1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B1C8")

    label("loc_B1C8")

    TalkEnd(0xFE)
    Return()

    # Function_27_A8B2 end

    def Function_28_B1CC(): pass

    label("Function_28_B1CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B241")

    #C0543
    ChrTalk(
        0xFE,
        (
            "やっとお外に出れたと思ったら\x01",
            "空にあんなものが……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        (
            "一体全体……\x01",
            "何が起こっているのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B24F")
    Jump("loc_B9E7")

    label("loc_B24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B2D5")

    #C0545
    ChrTalk(
        0xFE,
        (
            "よ、よく分からないけど、\x01",
            "戦争が起こるんですって……？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        (
            "不安でたまらないけど……\x01",
            "ケン、あなたは私が守るからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B361")

    #C0547
    ChrTalk(
        0xFE,
        (
            "しばらくお休みしちゃったけど、\x01",
            "今日からまた買い物再開よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        (
            "だって、私たちが消費しないことには\x01",
            "経済が回らないものね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B3F4")

    #C0549
    ChrTalk(
        0xFE,
        (
            "家に居るのも不安だし、\x01",
            "落ち着かないから\x01",
            "今日も百貨店に来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xFE,
        (
            "流石に楽しくショッピングって\x01",
            "気分にはならないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B492")

    #C0551
    ChrTalk(
        0xFE,
        (
            "列車の事故なんて物騒な話よね。\x01",
            "でも復旧が早くて本当に助かるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xFE,
        (
            "だって物流が止まっちゃったら、\x01",
            "こうやってお買い物できないんだからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B4EB")

    #C0553
    ChrTalk(
        0xFE,
        (
            "何だか騒ぎが起こっているみたいね。\x01",
            "今日は早めに帰った方がいいかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B5BA")

    #C0554
    ChrTalk(
        0xFE,
        (
            "最近、旦那が難しい顔をしているのよね。\x01",
            "どうやら国家独立に関して\x01",
            "色々と思うところがあるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xFE,
        (
            "ま、とりあえず難しい話は旦那に任せるわ。\x01",
            "私はとにかく、お買い物を楽しむわよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B627")

    #C0556
    ChrTalk(
        0xFE,
        "あら、また新商品が追加されたのね。\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xFE,
        (
            "んもう、さすがは\x01",
            "天下のタイムズ百貨店なんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B6B4")

    #C0558
    ChrTalk(
        0xFE,
        "確か今日って通商会議当日だったっけ？\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "ま、どうせ直接見れるわけじゃないんだし、\x01",
            "気にしても仕方ないかもしれないけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B74E")

    #C0560
    ChrTalk(
        0xFE,
        "いい、ケン。\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        (
            "帰ったらまずパパにゴメンなさい。\x01",
            "それから、すかさずにハグよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "大丈夫、２人で挟み込めば\x01",
            "怖いものナシなんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7C0")

    #C0563
    ChrTalk(
        0xFE,
        "さっきの除幕式、凄かったわね。\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "何だか興奮して\x01",
            "購買意欲が刺激されちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B821")

    label("loc_B7C0")


    #C0565
    ChrTalk(
        0xFE,
        (
            "さ～、今ならお給料日直後で\x01",
            "お財布の中も暖かいんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        "今日はじっくり見て行くわよ～。\x02",
    )

    CloseMessageWindow()

    label("loc_B821")

    Jump("loc_B9E7")

    label("loc_B826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B8C9")

    #C0567
    ChrTalk(
        0xFE,
        (
            "いつも思うんだけど、\x01",
            "商品を考える人って凄いわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xFE,
        (
            "次から次へと新しい事を考えては\x01",
            "毎度毎度、私たち消費者の\x01",
            "ハートをガッチリ掴むんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B8C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B98F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B962")

    #C0569
    ChrTalk(
        0xFE,
        (
            "前は買い物に付き合わせると、\x01",
            "ぐちぐち言っていたケンも\x01",
            "最近では文句を言わなくなったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        "これも愛ね～、ママは幸せよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B98A")

    label("loc_B962")


    #C0571
    ChrTalk(
        0xFE,
        "出来た息子を持つ母親って幸せよね。\x02",
    )

    CloseMessageWindow()

    label("loc_B98A")

    Jump("loc_B9E7")

    label("loc_B98F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B9E7")

    #C0572
    ChrTalk(
        0xFE,
        "ふんふんふ～ん♪\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xFE,
        (
            "百貨店は、いつ来ても\x01",
            "どれだけいても、飽きないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9E7")

    TalkEnd(0xFE)
    Return()

    # Function_28_B1CC end

    def Function_29_B9EB(): pass

    label("Function_29_B9EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BA5E")

    #C0574
    ChrTalk(
        0xFE,
        (
            "木が空中に生えるなんて、\x01",
            "一体どういう原理なんでしょう？\x01",
            "僕は夢か幻を見ているのでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BA5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BA6C")
    Jump("loc_C415")

    label("loc_BA6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BA88")

    #C0575
    ChrTalk(
        0xFE,
        "ママ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BA88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BAEA")

    #C0576
    ChrTalk(
        0xFE,
        (
            "ママは本当にたくましいですね。\x01",
            "何だかよく分からないけど、\x01",
            "勇気付けられますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BAEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BB70")

    #C0577
    ChrTalk(
        0xFE,
        (
            "流石のママも、今日は\x01",
            "お気楽気分とはいかないみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "でも、マインツのことを考えると\x01",
            "無理もないですよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BB70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BC0D")

    #C0579
    ChrTalk(
        0xFE,
        (
            "ママの買い物に対する情熱は\x01",
            "雨如きでは砕けないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xFE,
        (
            "今日はまだマシですけど、\x01",
            "大雨の日に付き合わされた時は\x01",
            "びしょ濡れで散々でした。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BC0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BD30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC5")

    #C0581
    ChrTalk(
        0xFE,
        (
            "救急車のサイレンって、\x01",
            "物凄い大音量ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "至近距離だとかなり\x01",
            "うるさいと思うのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        (
            "車を運転している人は\x01",
            "耳栓でもしているんですかね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_BD2B")

    label("loc_BCC5")


    #C0584
    ChrTalk(
        0xFE,
        (
            "救急車のサイレンって、\x01",
            "物凄い大音量ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "運転している人は\x01",
            "耳栓でもしているんですかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD2B")

    Jump("loc_C415")

    label("loc_BD30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BDE2")

    #C0586
    ChrTalk(
        0xFE,
        (
            "みんながみんな、\x01",
            "うちのママみたいに能天気に\x01",
            "考えられたら幸せなんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "もっとも、それじゃあ\x01",
            "アッと言う間に帝国辺りに\x01",
            "併合されてしまいそうですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BDE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BF0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA1")

    #C0588
    ChrTalk(
        0xFE,
        (
            "さて、今日は\x01",
            "人間観察で暇を潰すことにします。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "そういえば最近、雑貨屋のお兄さんと\x01",
            "案内係のお姉さんの仲がやけに良いんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        "ふむ、これはもしかして……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_BF08")

    label("loc_BEA1")


    #C0591
    ChrTalk(
        0xFE,
        (
            "最近、雑貨屋のお兄さんと\x01",
            "案内係のお姉さんの仲がやけに良いんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xFE,
        "ふむ、これはもしかして……\x02",
    )

    CloseMessageWindow()

    label("loc_BF08")

    Jump("loc_C415")

    label("loc_BF0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF8C")

    #C0593
    ChrTalk(
        0xFE,
        (
            "昨日のママの\x01",
            "謝罪作戦は大成功でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xFE,
        (
            "ハグに加えて泣き落としとは……\x01",
            "恐るべし、ママです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C000")

    label("loc_BF8C")


    #C0595
    ChrTalk(
        0xFE,
        (
            "ママの抱擁と涙に、パパはすっかり\x01",
            "骨抜きになっていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "あれが惚れた男の\x01",
            "弱みというヤツなのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C000")

    Jump("loc_C415")

    label("loc_C005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C06B")

    #C0597
    ChrTalk(
        0xFE,
        (
            "ママが買い物に夢中で\x01",
            "こんな時間まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        (
            "さすがのパパも\x01",
            "怒っていると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_C06B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C16F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10E")

    #C0599
    ChrTalk(
        0xFE,
        "除幕式は、まさに圧巻でした。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        (
            "……それはそうと、\x01",
            "ママのテンションがやや心配です。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "無駄な買い物を\x01",
            "しないといいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C16A")

    label("loc_C10E")


    #C0602
    ChrTalk(
        0xFE,
        (
            "今日のママは少し\x01",
            "目の色が違う気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xFE,
        (
            "無駄な買い物を\x01",
            "しないといいのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C16A")

    Jump("loc_C415")

    label("loc_C16F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C21A")

    #C0604
    ChrTalk(
        0xFE,
        (
            "いつも思うんですが、\x01",
            "商品を考える人は大変ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        (
            "ママみたいな人を引き止めるために\x01",
            "毎度毎度、何かしら新しいことを\x01",
            "考えないといけないんですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_C21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2CF")

    #C0606
    ChrTalk(
        0xFE,
        (
            "僕が編み出した、退屈しのぎの方法の\x01",
            "１つに人間観察というものがあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        (
            "百貨店は色んな人が来ますからね。\x01",
            "人を見る分には意外に飽きないんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C31C")

    label("loc_C2CF")


    #C0608
    ChrTalk(
        0xFE,
        (
            "百貨店は色んな人が来ますからね。\x01",
            "人を見る分には意外に飽きないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C31C")

    Jump("loc_C415")

    label("loc_C321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3AC")

    #C0609
    ChrTalk(
        0xFE,
        (
            "え、バカンスルックの\x01",
            "赤毛の人ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xFE,
        (
            "その人なら、ついさっき\x01",
            "屋上に上がっていった\x01",
            "みたいですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_C3AC")


    #C0611
    ChrTalk(
        0xFE,
        (
            "ママのウィンドウショッピングに\x01",
            "付き合うのが僕の日課なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        "慣れましたけど退屈は退屈ですよ。\x02",
    )

    CloseMessageWindow()

    label("loc_C415")

    TalkEnd(0xFE)
    Return()

    # Function_29_B9EB end

    def Function_30_C419(): pass

    label("Function_30_C419")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C4D0")

    #C0613
    ChrTalk(
        0xFE,
        (
            "突如現れた宙に浮かぶ巨大な樹、か。\x01",
            "現時点で特に問題は\x01",
            "起きておらんようじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xFE,
        (
            "……とにかく、\x01",
            "あんな不気味なものは早く\x01",
            "消えてなくなって欲しいものじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C4DE")
    Jump("loc_CD51")

    label("loc_C4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C521")

    #C0615
    ChrTalk(
        0xFE,
        (
            "ふむむ……これは\x01",
            "尋常ならざる事態になったのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C5CE")

    #C0616
    ChrTalk(
        0xFE,
        (
            "ふむ、確かに現時点で\x01",
            "独立を撤回した所で、２大国を\x01",
            "信じていいかどうかは別問題じゃしな……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "それでもやはり、両国の軍事的脅威は\x01",
            "無視できん問題じゃが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C68C")

    #C0618
    ChrTalk(
        0xFE,
        (
            "ふむ、じゃが仮に独立したとして\x01",
            "２大国に対抗できる軍隊を\x01",
            "用意できるかが問題じゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "例えば帝国の列車砲……\x01",
            "あの兵器１つを取っても\x01",
            "クロスベルなど一溜まりもないぞ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C707")

    #C0620
    ChrTalk(
        0xFE,
        "わしは鬼のような化物と聞いたが……\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        (
            "こんな不可思議な話を聞くのは\x01",
            "それこそ生まれて初めての事じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C74C")

    #C0622
    ChrTalk(
        0xFE,
        (
            "外が騒がしいようじゃが、\x01",
            "一体何があったのかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C7D8")

    #C0623
    ChrTalk(
        0xFE,
        (
            "ふむ、そろそろ婆さんへの\x01",
            "次の贈り物を真剣に考えんとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "ブローチは以前贈ったし……\x01",
            "思い切って指輪にでもするかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C878")

    #C0625
    ChrTalk(
        0xFE,
        (
            "この歳になって、まさか独立という\x01",
            "言葉を聞くとは思わんかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "実現できればそりゃ結構なことだが、\x01",
            "そう上手く行く話でもあるまいに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C91E")

    #C0627
    ChrTalk(
        0xFE,
        (
            "ふむ、会議においてとかく問題なのは\x01",
            "オズボーンとロックスミスの存在じゃな……\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        (
            "あの鉄面皮どもを相手に、\x01",
            "市長はどういう策を用意しておるのかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C978")

    #C0629
    ChrTalk(
        0xFE,
        "さて、そろそろ家に帰らんとのう。\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xFE,
        "婆さんに怒られては敵わんからな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CA16")

    #C0631
    ChrTalk(
        0xFE,
        (
            "フォッフォッ、ここの屋上はタワーを\x01",
            "見るのに絶好のスポットじゃの。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "幕が取り除かれた瞬間のタワーの\x01",
            "壮麗な姿が目に焼きついて離れんわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_CA16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CB44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAD1")

    #C0633
    ChrTalk(
        0xFE,
        (
            "明日からいよいよ\x01",
            "通商会議が開かれるのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        (
            "クロイス市長が\x01",
            "開催を提唱された時は\x01",
            "随分たまげたものじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        (
            "まさか、本当に\x01",
            "実現してしまうとはのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_CB3F")

    label("loc_CAD1")


    #C0636
    ChrTalk(
        0xFE,
        (
            "まさか、通商会議が\x01",
            "本当に実現するとはのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        (
            "流石に、ＩＢＣ総裁を\x01",
            "兼任しているだけのことはあるわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB3F")

    Jump("loc_CD51")

    label("loc_CB44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CBCC")

    #C0638
    ChrTalk(
        0xFE,
        (
            "ふむ、この店の品揃えは\x01",
            "いつ眺めても心くすぐられるわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xFE,
        (
            "どれ、また婆さんへの\x01",
            "プレゼントでも見繕うとするかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_CBCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CD51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCD5")

    #C0640
    ChrTalk(
        0xFE,
        (
            "ふむ、それにしてもクロイス市長と\x01",
            "マクダエル議長の活躍には\x01",
            "まことに目を見張るものがあるのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xFE,
        (
            "特に議長はこのわしとそれほど年齢が\x01",
            "変わらんというのに、あの働きぶり……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        (
            "フォッフォッ、老いてますます盛んとは\x01",
            "まさにこの事じゃて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_CD51")

    label("loc_CCD5")


    #C0643
    ChrTalk(
        0xFE,
        (
            "フォッフォッ、老いてますます盛んとは\x01",
            "まさにこの事じゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xFE,
        (
            "マクダエル議長は、\x01",
            "わしら老いぼれ世代のスターじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD51")

    TalkEnd(0xFE)
    Return()

    # Function_30_C419 end

    def Function_31_CD55(): pass

    label("Function_31_CD55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CD66")
    Jump("loc_CF41")

    label("loc_CD66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CDF9")

    #C0645
    ChrTalk(
        0xFE,
        (
            "ってか、戒厳令とか言って\x01",
            "まさかこんな事態になるなんて\x01",
            "思ってもみなかったしー。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xFE,
        (
            "はあ……素直に家に\x01",
            "帰っとくべきだったかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF41")

    label("loc_CDF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CE91")

    #C0647
    ChrTalk(
        0xFE,
        (
            "何でも独立したら帝国と共和国に\x01",
            "ミラを納めなくていいらしいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xFE,
        (
            "とにかく、ディーターさんの\x01",
            "言うことに間違いはないんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF41")

    label("loc_CE91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CED8")

    #C0649
    ChrTalk(
        0xFE,
        (
            "雨の日のサービスって、\x01",
            "百貨店も粋なことするよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF41")

    label("loc_CED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CF41")

    #C0650
    ChrTalk(
        0xFE,
        (
            "宿題～？\x01",
            "そんなのするわけないじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xFE,
        (
            "そういえばさー、\x01",
            "アリオス様、また出張らしいよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF41")

    TalkEnd(0xFE)
    Return()

    # Function_31_CD55 end

    def Function_32_CF45(): pass

    label("Function_32_CF45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CF56")
    Jump("loc_D0AD")

    label("loc_CF56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CFC1")

    #C0652
    ChrTalk(
        0xFE,
        (
            "でも、この状況だと、\x01",
            "どこにいたって同じじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "家族に会えないのは寂しいけど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0AD")

    label("loc_CFC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D02E")

    #C0654
    ChrTalk(
        0xFE,
        (
            "何か最近、大人たちが\x01",
            "独立、独立ってうるさいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        "つまりは、どういうことなのかな？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0AD")

    label("loc_D02E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D0AD")

    #C0656
    ChrTalk(
        0xFE,
        (
            "っていうかさー、\x01",
            "あの人って支配人なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        (
            "そんな人が、わざわざ自分から\x01",
            "接客するってのも何気に凄いよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0AD")

    TalkEnd(0xFE)
    Return()

    # Function_32_CF45 end

    def Function_33_D0B1(): pass

    label("Function_33_D0B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0C6")
    Call(0, 36)
    Jump("loc_D144")

    label("loc_D0C6")


    #C0658
    ChrTalk(
        0xFE,
        (
            "……ん？　お前たちは確か、\x01",
            "警察のナントカ課だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        (
            "フン、さっさと向こうに行け。\x01",
            "気安く話しかけないでもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D144")

    TalkEnd(0xFE)
    Return()

    # Function_33_D0B1 end

    def Function_34_D148(): pass

    label("Function_34_D148")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D15D")
    Call(0, 36)
    Jump("loc_D1E5")

    label("loc_D15D")


    #C0660
    ChrTalk(
        0xFE,
        (
            "あーあ、せっかく旅行に来たんだし\x01",
            "もう少し刺激的なことをしてえよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xFE,
        (
            "へへ、裏通りの方にあった\x01",
            "キナ臭げな店にでも行ってみるか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1E5")

    TalkEnd(0xFE)
    Return()

    # Function_34_D148 end

    def Function_35_D1E9(): pass

    label("Function_35_D1E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1FE")
    Call(0, 36)
    Jump("loc_D27C")

    label("loc_D1FE")


    #C0662
    ChrTalk(
        0xFE,
        (
            "なーなー、あとで\x01",
            "オーバルストアの方も見にいこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xFE,
        (
            "せっかくだし、クルマもやれる限り\x01",
            "チューンナップしときたいしさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27C")

    TalkEnd(0xFE)
    Return()

    # Function_35_D1E9 end

    def Function_36_D280(): pass

    label("Function_36_D280")

    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)
    OP_4B(0x19, 0xFF)

    #C0664
    ChrTalk(
        0x17,
        (
            "やれやれ……\x01",
            "貿易都市の百貨店って言っても\x01",
            "大したことないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x18,
        (
            "ああ、俺たちの\x01",
            "お眼鏡に敵うもんは\x01",
            "ほとんど置いてねえよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x19,
        (
            "まー、庶民向けの商品が\x01",
            "多いみたいだし、\x01",
            "こんなもんじゃねえ？\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x19,
        (
            "今日も酒のツマミだけ\x01",
            "買って帰ろうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3A0")
    Jump("loc_D449")

    label("loc_D3A0")


    #C0668
    ChrTalk(
        0x104,
        (
            "#00301F（あー、こいつらが噂の\x01",
            "  ナマイキなボンボンどもか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x102,
        (
            "#00106F（まったく、\x01",
            "  こんなところにたむろして……）\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#00003F（……まあ、今は放っておこう。）\x02",
    )

    CloseMessageWindow()

    label("loc_D449")

    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_36_D280 end

    def Function_37_D45E(): pass

    label("Function_37_D45E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D4E3")

    #C0671
    ChrTalk(
        0xFE,
        (
            "お家にストックしていた\x01",
            "お菓子がなくなっちゃったから\x01",
            "慌てて買いに来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        "私ったら、おっちょこちょいね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D552")

    label("loc_D4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D552")

    #C0673
    ChrTalk(
        0xFE,
        (
            "お菓子は時間のある時に\x01",
            "買い溜めしておかないとね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xFE,
        (
            "イザという時に\x01",
            "なくなったら大変だもの～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D552")

    TalkEnd(0xFE)
    Return()

    # Function_37_D45E end

    def Function_38_D556(): pass

    label("Function_38_D556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D61D")

    #C0675
    ChrTalk(
        0xFE,
        (
            "あの馬鹿でかい樹はともかく、\x01",
            "やっぱ自由っていいよな。\x01",
            "戒厳令だなんて窮屈で仕方なかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xFE,
        (
            "へへっ、せっかくだし、\x01",
            "シロン姉ちゃんの所に差し入れでも\x01",
            "持って行ってやろうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D62B")
    Jump("loc_DF60")

    label("loc_D62B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D6D1")

    #C0677
    ChrTalk(
        0xFE,
        (
            "不可解な事故、か。\x01",
            "確かにこれまでそんな感じの\x01",
            "事件ってあったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0xFE,
        (
            "それを見過ごしてきた\x01",
            "俺たちにも罪がある……\x01",
            "確かに大統領の言う通りかもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D774")

    #C0679
    ChrTalk(
        0xFE,
        (
            "当たり前だけど……\x01",
            "ウルスラ病院は大忙しみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0xFE,
        (
            "シロン姉ちゃんも何だか\x01",
            "落ち込んじゃってるみたいだし、\x01",
            "何も出来ない自分が不甲斐ないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D8DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D846")

    #C0681
    ChrTalk(
        0xFE,
        "マ、マインツを襲撃って何だよ。\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xFE,
        (
            "昨日から病院には、\x01",
            "警備隊の人たちが次々と\x01",
            "運び込まれてるって話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xFE,
        (
            "くそっ、なんでこんな無益で\x01",
            "馬鹿なことをするヤツらがいるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D8D9")

    label("loc_D846")


    #C0684
    ChrTalk(
        0xFE,
        (
            "昨日から病院には、\x01",
            "警備隊の人たちが次々と\x01",
            "運び込まれてるって話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0xFE,
        (
            "くそっ、なんでこんな無益で\x01",
            "馬鹿なことをするヤツらがいるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8D9")

    Jump("loc_DF60")

    label("loc_D8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D9A2")

    #C0686
    ChrTalk(
        0xFE,
        (
            "列車事故に遭った人の中には\x01",
            "重傷者もいたそうだけど……\x01",
            "みんな一命は取りとめたらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0xFE,
        (
            "何人もの先生方が夜を徹して\x01",
            "対応したって話だけど、\x01",
            "医者ってのはホント人間の鑑だよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D9EF")

    #C0688
    ChrTalk(
        0xFE,
        (
            "ん、何だ？　救急車……？\x01",
            "けっこうな台数っぽかったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DA7F")

    #C0689
    ChrTalk(
        0xFE,
        "えー、本日の家族のご所望品はっと。\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0xFE,
        (
            "へへっ、いい歳して家族に\x01",
            "養ってもらってる分、せめて\x01",
            "買い物くらいで役に立たなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DA7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DC51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBCA")

    #C0691
    ChrTalk(
        0xFE,
        (
            "シロン姉ちゃんに\x01",
            "勧められた男性看護師の道、\x01",
            "本気で考えることにしてみたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0xFE,
        (
            "とりあえず試験を受けるためには\x01",
            "来年まで待たなきゃだけど、\x01",
            "模試では既にいい結果も出ていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0xFE,
        (
            "ま、来年の研修医試験も\x01",
            "一応は受けるつもりなんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0xFE,
        (
            "道が一つだけじゃないって思ったら\x01",
            "かなり気が楽になったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_DC4C")

    label("loc_DBCA")


    #C0695
    ChrTalk(
        0xFE,
        (
            "人間、前向きに頑張らなきゃ\x01",
            "身につくものも身につかないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0xFE,
        (
            "何だか勉強も前より楽しいんだ。\x01",
            "……ちょっぴりだけだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC4C")

    Jump("loc_DF60")

    label("loc_DC51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DC5F")
    Jump("loc_DF60")

    label("loc_DC5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_DC6D")
    Jump("loc_DF60")

    label("loc_DC6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DD19")

    #C0697
    ChrTalk(
        0xFE,
        (
            "街は除幕式とやらで\x01",
            "浮かれてるみたいだけど……\x01",
            "俺の心は沈むばかりさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0xFE,
        (
            "その点、シロン姉ちゃんは\x01",
            "お気楽な性格で羨ましいよ。\x01",
            "姉弟とはホント思えないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DD19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DDA9")

    #C0699
    ChrTalk(
        0xFE,
        "これからまた１年、浪人生活かぁ。\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0xFE,
        (
            "何か最近、家族の視線が\x01",
            "ますます冷たくなった気もするし……\x01",
            "はぁ、マジで人生どうしよう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DDA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DE63")

    #C0701
    ChrTalk(
        0xFE,
        (
            "えー、今日の買い物は\x01",
            "黒胡椒にマスタードソース、\x01",
            "それからオリーブオイルに……\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0xFE,
        (
            "はぁ、パシリの内容を\x01",
            "メモなしで覚えられてもなぁ。\x01",
            "この記憶力を勉強方面に使いたいぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DE63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DF60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF0B")

    #C0703
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院の研修医の試験、\x01",
            "また今年もダメだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0xFE,
        (
            "３度目の正直って\x01",
            "言葉を信じて挑んだけど……\x01",
            "俺にはやっぱ向いてないのかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_DF60")

    label("loc_DF0B")


    #C0705
    ChrTalk(
        0xFE,
        (
            "そんなしがない俺は\x01",
            "今日も家族の使いパシリ……\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0xFE,
        "はぁ、俺ってダメダメだなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_DF60")

    TalkEnd(0xFE)
    Return()

    # Function_38_D556 end

    def Function_39_DF64(): pass

    label("Function_39_DF64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E01F")

    #C0707
    ChrTalk(
        0xFE,
        (
            "みっしぃぐるみの\x01",
            "Ｌサイズが欲しいんだけど、\x01",
            "流石に値が張るのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0xFE,
        (
            "小遣いを溜めてＬサイズを買うか、\x01",
            "今すぐに手頃なＳサイズを買うか……\x01",
            "う～ん、悩んじゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E091")

    label("loc_E01F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E091")

    #C0709
    ChrTalk(
        0xFE,
        (
            "雑貨屋にみっしぃのコーナーが\x01",
            "出来たってのは本当だったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xFE,
        "こ、これは通わずにいられないわっ。\x02",
    )

    CloseMessageWindow()

    label("loc_E091")

    TalkEnd(0xFE)
    Return()

    # Function_39_DF64 end

    def Function_40_E095(): pass

    label("Function_40_E095")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E118")

    #C0711
    ChrTalk(
        0xFE,
        (
            "さてと、お土産を買ったら\x01",
            "そろそろ空港に向かうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0xFE,
        (
            "いや～、しかし今回も\x01",
            "とても有意義な旅行になったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E215")

    label("loc_E118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_E126")
    Jump("loc_E215")

    label("loc_E126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E191")

    #C0713
    ChrTalk(
        0xFE,
        (
            "いや～、除幕式は\x01",
            "想像していたよりもすごかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0xFE,
        "流石はクロスベルって感じだよね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E215")

    label("loc_E191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E215")

    #C0715
    ChrTalk(
        0xFE,
        (
            "いや～、やっぱり\x01",
            "クロスベルはいい所だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xFE,
        (
            "明日はオルキスタワーの\x01",
            "除幕式もあるし、\x01",
            "今回の旅行も楽しめそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E215")

    TalkEnd(0xFE)
    Return()

    # Function_40_E095 end

    def Function_41_E219(): pass

    label("Function_41_E219")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E276")

    #C0717
    ChrTalk(
        0xFE,
        (
            "あ～あ、今回の旅行も\x01",
            "これでお終いなのね。\x01",
            "ホントあっという間だったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E35A")

    label("loc_E276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_E284")
    Jump("loc_E35A")

    label("loc_E284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E306")

    #C0718
    ChrTalk(
        0xFE,
        (
            "ここの屋上、除幕式を見るのに\x01",
            "ホントいい場所だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xFE,
        (
            "ふふ、ちゃんと事前に\x01",
            "リサーチした甲斐があったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E35A")

    label("loc_E306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E35A")

    #C0720
    ChrTalk(
        0xFE,
        (
            "クロスベルって、\x01",
            "本当に刺激的な場所よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0xFE,
        "何度来ても飽きないわ。\x02",
    )

    CloseMessageWindow()

    label("loc_E35A")

    TalkEnd(0xFE)
    Return()

    # Function_41_E219 end

    def Function_42_E35E(): pass

    label("Function_42_E35E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E445")

    #C0722
    ChrTalk(
        0xFE,
        (
            "ふむ、流石にネストン支配人の\x01",
            "お言葉には含蓄がありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xFE,
        (
            "私は事業家としても商売人としても\x01",
            "まだまだ未熟ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xFE,
        (
            "それでも、この立場を通して\x01",
            "クロスベルのために出来ることを\x01",
            "尽くしたいと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_E4D8")

    label("loc_E445")


    #C0725
    ChrTalk(
        0xFE,
        (
            "私は事業家としても商売人としても\x01",
            "まだまだ未熟ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0xFE,
        (
            "それでも、この立場を通して\x01",
            "クロスベルのために出来ることを\x01",
            "尽くしたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4D8")

    TalkEnd(0xFE)
    Return()

    # Function_42_E35E end

    def Function_43_E4DC(): pass

    label("Function_43_E4DC")

    TalkBegin(0xFE)

    #C0727
    ChrTalk(
        0xFE,
        (
            "今晩の晩餐のために、\x01",
            "色々と買い物をしていたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xFE,
        (
            "表が騒がしいようですが……\x01",
            "何かあったのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_E4DC end

    def Function_44_E555(): pass

    label("Function_44_E555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E5E9")

    #C0729
    ChrTalk(
        0xFE,
        (
            "何でもテロリストが本会議を\x01",
            "襲う可能性が高いんだってね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0xFE,
        (
            "はあ、やれやれ……\x01",
            "万が一鉢合わせになったら\x01",
            "手に負えるかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB95")

    label("loc_E5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6A0")

    #C0731
    ChrTalk(
        0xFE,
        (
            "ふう、今日は流石に\x01",
            "ものすごい人出だね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xFE,
        (
            "忙しすぎて美人を\x01",
            "数える暇もなかったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        (
            "#00012F（う～ん、レイモンドさんは\x01",
            "  相変わらずだなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_E6FE")

    label("loc_E6A0")


    #C0734
    ChrTalk(
        0xFE,
        (
            "ふう、今日は流石に\x01",
            "ものすごい人出だね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0xFE,
        (
            "忙しすぎて美人を\x01",
            "数える暇もなかったよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6FE")

    Jump("loc_EB95")

    label("loc_E703")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E85F")

    #C0736
    ChrTalk(
        0xFE,
        (
            "おや、その子供は……\x01",
            "もしかして迷子の親探しでも\x01",
            "しているのかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0737
    ChrTalk(
        0x1A2,
        "……誰が迷子だ。\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x1A2,
        (
            "ボクは今、クロスベル見学を\x01",
            "しているんだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A2, 500)

    #C0739
    ChrTalk(
        0xFE,
        "へえ、クロスベル見学ね～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0740
    ChrTalk(
        0xFE,
        (
            "これも支援要請ってヤツか。\x01",
            "支援課の仕事も大変だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        "#00000Fはは、ええまあ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_E8D2")

    label("loc_E85F")


    #C0742
    ChrTalk(
        0xFE,
        (
            "ま、とりあえず\x01",
            "まだ警戒体制も初日だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xFE,
        (
            "あんまり飛ばしすぎず、\x01",
            "ほどほどに頑張ると\x01",
            "いいんじゃないかな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8D2")

    Jump("loc_EB95")

    label("loc_E8D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAA2")

    #C0744
    ChrTalk(
        0xFE,
        (
            "あ、君たち～。\x01",
            "お互い大変だね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        (
            "#00003Fええまあ、何といっても\x01",
            "この状況ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x102,
        (
            "#00100Fここにいるということは\x01",
            "百貨店の担当なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0xFE,
        (
            "まあ、厳密には中央広場の\x01",
            "商業施設全般だけどね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xFE,
        (
            "けっこう美人も見かけるから\x01",
            "警戒にも気合いが入るよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x102,
        "#00105Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x109,
        (
            "#10106F（う～ん、おそろしく\x01",
            "  動機が不純ですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x104,
        (
            "#00309F（はは、まあそれで\x01",
            "  気合いが入るってんなら\x01",
            "  結構なことだと思うがな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_EB95")

    label("loc_EAA2")


    #C0752
    ChrTalk(
        0xFE,
        (
            "警戒活動って肩が凝るけどさ～。\x01",
            "美人を見かけると疲れが吹き飛ぶね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0xFE,
        (
            "ここまでの美人数、３１人……\x01",
            "むふふ～、まだまだ期待できそうだよ。\x02",
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

    label("loc_EB95")

    TalkEnd(0xFE)
    Return()

    # Function_44_E555 end

    def Function_45_EB99(): pass

    label("Function_45_EB99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBAE")
    Call(0, 46)
    Jump("loc_EC13")

    label("loc_EBAE")


    #C0754
    ChrTalk(
        0x21,
        (
            "#00603F私はこれから頼んでおいた靴を\x01",
            "試し履きするのだ。\x02\x03",

            "#00600F邪魔をしないでおいてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC13")

    TalkEnd(0xFE)
    Return()

    # Function_45_EB99 end

    def Function_46_EC17(): pass

    label("Function_46_EC17")

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
            "ダドリー様、\x01",
            "こちらがご注文の品となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x21,
        "#11P#00602Fふむ、ではさっそく試し履きを……\x02",
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
            "#11P#00600Fむ、お前たち。\x01",
            "一体こんな所で何をしている？\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x101,
        "#12P#00000F何をと言われましても……\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        (
            "#6P#00306Fむしろ聞きたいのは\x01",
            "こっちだっつう話だぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0760
    ChrTalk(
        0x105,
        (
            "#12P#10305Fふぅん、\x01",
            "大した高級品みたいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x102,
        (
            "#6P#00100F革靴……ですね。\x01",
            "どこかのブランド物でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x21,
        (
            "#11P#00603Fフン、この私を\x01",
            "ブランドと聞くだけで\x01",
            "ありがたがる連中と一緒にするな。\x02\x03",

            "#00602F……これはオーダーメイドだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x109,
        (
            "#6P#10100Fへえ、こだわられて\x01",
            "いらっしゃるんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x101,
        (
            "#12P#00005Fオーダーメイドの革靴か……\x02\x03",

            "#00003F俺は基本的に\x01",
            "スニーカーばかりだからな。\x02",
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
            "#11P#00601F……バニングス。\x01",
            "お前、何が言いたい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0766
    ChrTalk(
        0x101,
        "#12P#00000Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x21,
        (
            "#11P#00600Fまるで革靴が下らんものだと\x01",
            "言いたそうな口ぶりだな。\x02\x03",

            "#00603Fだが……\x01",
            "その考えは間違っているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        "#12P#00011Fお、俺は別に……\x02",
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x21,
        (
            "#11P#00602F靴において\x01",
            "革ほど奥の深い素材はない。\x02\x03",

            "#00604F履くほどに馴染み、\x01",
            "そして手入れを怠らなければ、\x01",
            "風合いはより深みを増していく……\x02\x03",

            "#00601F貴様はこの醍醐味がスニーカーで\x01",
            "味わえると思っているのか？\x02",
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
        "#6P#00206F何故か、やたらと熱いですね……\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x102,
        "#6P#00109Fええ、正直意外な感じね。\x02",
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x21,
        (
            "#11P#00606Fゴ、ゴホン……\x01",
            "少々話が脱線してしまったな。\x02\x03",

            "#00600Fとにかく、私がここにいるのは\x01",
            "たまたま空き時間が出来たからだ。\x02\x03",

            "当然、後の予定はつかえているのでな。\x01",
            "邪魔をしないでおいてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x101,
        "#12P#00012Fりょ、了解です……\x02",
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

    # Function_46_EC17 end

    def Function_47_F3CC(): pass

    label("Function_47_F3CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F45D")

    #C0774
    ChrTalk(
        0x1B,
        (
            "#02106Fはいはい、分かってるってば。\x02\x03",

            "#02109Fとにかくあたし、\x01",
            "ここに置いてあるメーカーの\x01",
            "ペンじゃなきゃダメなのよねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_F4D7")

    label("loc_F45D")


    #C0775
    ChrTalk(
        0x1B,
        (
            "#02105Fへ～、モデルチェンジで\x01",
            "ラインナップが強化されたんだ。\x02\x03",

            "#02109Fふむふむ、こっちの\x01",
            "タイプも試してみようかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4D7")

    TalkEnd(0xFE)
    Return()

    # Function_47_F3CC end

    def Function_48_F4DB(): pass

    label("Function_48_F4DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F5BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F556")

    #C0776
    ChrTalk(
        0xFE,
        (
            "グレイス先輩、\x01",
            "早く済ませて下さいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0xFE,
        (
            "何をそんなに\x01",
            "悠長にしてるんですか～。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x2, 0)
    Jump("loc_F5B6")

    label("loc_F556")


    #C0778
    ChrTalk(
        0xFE,
        (
            "はあ、急にインクが\x01",
            "切れたから買い物って……\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0xFE,
        (
            "まだ時間は全然あるけど、\x01",
            "何か不安だな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5B6")

    Jump("loc_F6AB")

    label("loc_F5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F6AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F657")

    #C0780
    ChrTalk(
        0xFE,
        (
            "えっと、回復薬に解毒薬、\x01",
            "それから気付け薬も必要か……\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#00005F（医療キットの準備か……\x01",
            "  これからどこかに行くのかな？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_F6AB")

    label("loc_F657")


    #C0782
    ChrTalk(
        0xFE,
        (
            "ＥＰチャージ、\x01",
            "……は必要ないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0xFE,
        (
            "あとは一応、\x01",
            "煙り玉も用意しておくかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6AB")

    TalkEnd(0xFE)
    Return()

    # Function_48_F4DB end

    def Function_49_F6AF(): pass

    label("Function_49_F6AF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0784
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２Ｆ　ブティック《ルッカ》\x01",
            "２Ｆ　ハンソンシューズ\x01",
            "２Ｆ　アクセサリ《ベイカー》\x01",
            "１Ｆ　《リジョンフード》\x01",
            "１Ｆ　雑貨コーナー《サザーク》\x02",
        )
    )

    CloseMessageWindow()

    #A0785
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ご不明な点がありましたら\x01",
            "  正面総合インフォメーションにて\x01",
            "  お気軽にお尋ねくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_49_F6AF end

    def Function_50_F7C7(): pass

    label("Function_50_F7C7")

    EventBegin(0x0)
    Fade(500)
    OP_68(-15210, 1000, 9790, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F84E")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x104, -14350, 0, 8000, 0)
    Jump("loc_F8ED")

    label("loc_F84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F8A0")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x109, -14350, 0, 8000, 0)
    Jump("loc_F8ED")

    label("loc_F8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F8ED")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x105, -14350, 0, 8000, 0)

    label("loc_F8ED")

    OP_0D()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0786
    ChrTalk(
        0x1A2,
        (
            "#12Pこ、これはもしかして\x01",
            "『みっしぃぐるみ』……！\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x1A2,
        (
            "#12Pどうしてだ？\x01",
            "テーマパークでもないのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、確か最近になって\x01",
            "出来た専用コーナーなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x101,
        (
            "#12P#00000Fシンはみっしぃに\x01",
            "興味があったりするのか？\x02",
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
            "お、お前……\x01",
            "ボクをブジョクする気か！？\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x1A2,
        (
            "なにがかなしくて\x01",
            "黒月を背負うボクがこんなもの……\x01",
            "無礼にもほどがあるだろうっ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FB8F")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FAE9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FAE9)
    Sleep(50)

    def lambda_FAF9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FAF9)
    Sleep(300)

    #C0792
    ChrTalk(
        0x102,
        "#00105Fシ、シン君……？\x02",
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x101,
        "#12P#00006Fそこまでムキにならなくても……\x02",
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x104,
        (
            "#12P#00309Fああ、それに\x01",
            "黒月はまったく関係ねえしな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD8E")

    label("loc_FB8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FC94")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FBE8():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FBE8)
    Sleep(50)

    def lambda_FBF8():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FBF8)
    Sleep(300)

    #C0795
    ChrTalk(
        0x102,
        "#00105Fシ、シン君……？\x02",
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        "#12P#00006Fそこまでムキにならなくても……\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x109,
        (
            "#12P#10102Fええ、それに黒月は\x01",
            "まったく関係ありませんしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD8E")

    label("loc_FC94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FD8E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FCED():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FCED)
    Sleep(50)

    def lambda_FCFD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FCFD)
    Sleep(300)

    #C0798
    ChrTalk(
        0x102,
        "#00105Fシ、シン君……？\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x101,
        "#12P#00006Fそこまでムキにならなくても……\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x105,
        (
            "#12P#10302Fああ、それに\x01",
            "黒月はまったく関係ないしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD8E")

    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    #C0801
    ChrTalk(
        0x1A2,
        "フンッ、とにかくだ――\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0802
    ChrTalk(
        0x1A2,
        (
            "#12Pなんだこれは……？\x01",
            "タイムズ百貨店限定商品、\x01",
            "『チクタクみっしぃ』だと？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    #C0803
    ChrTalk(
        0x1A2,
        "#12P――ハッ！\x02",
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
            "と、とにかく、こんなのは\x01",
            "コドモだましもいいトコだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x1A2,
        (
            "ボクはいっさい\x01",
            "興味がないんだからな！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FF24")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_FFD1")

    label("loc_FF24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FF7D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_FFD1")

    label("loc_FF7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FFD1")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_FFD1")


    #C0806
    ChrTalk(
        0x101,
        "#12P#00012F（わ、分かりやすいなぁ……）\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x102,
        (
            "#12P#00100F（ええ、これじゃ興味ありますって\x01",
            "  言っているようなものね。）\x02",
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

    # Function_50_F7C7 end

    def Function_51_10079(): pass

    label("Function_51_10079")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-960, 3000, 1530, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17880, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10105")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x104, 600, 0, 2900, 180)
    Jump("loc_101A4")

    label("loc_10105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10157")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x109, 600, 0, 2900, 180)
    Jump("loc_101A4")

    label("loc_10157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_101A4")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x105, 600, 0, 2900, 180)

    label("loc_101A4")

    OP_68(-960, 1600, 1530, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0808
    ChrTalk(
        0x101,
        (
            "#00000Fさてと、それじゃ適当に\x01",
            "店を回りながら屋上を目指そうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x1A2,
        "#12Pああ、では案内は任せたぞ！\x02",
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

    # Function_51_10079 end

    def Function_52_10258(): pass

    label("Function_52_10258")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-17440, 1600, 19460, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16140, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_102E5")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x104, -15690, 30, 21350, 270)
    Jump("loc_10384")

    label("loc_102E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10337")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x109, -15690, 30, 21350, 270)
    Jump("loc_10384")

    label("loc_10337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10384")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x105, -15690, 30, 21350, 270)

    label("loc_10384")

    FadeToBright(1000, 0)
    OP_0D()

    #C0810
    ChrTalk(
        0x1A2,
        (
            "#12Pおい、さっきから\x01",
            "こそこそ何をやってたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        "#00000Fああ、実はこれを買ってたんだ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10411")

    def lambda_103FF():

        label("loc_103FF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_103FF")

    QueueWorkItem2(0x104, 1, lambda_103FF)
    Jump("loc_1044C")

    label("loc_10411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10431")

    def lambda_1041F():

        label("loc_1041F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1041F")

    QueueWorkItem2(0x109, 1, lambda_1041F)
    Jump("loc_1044C")

    label("loc_10431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1044C")

    def lambda_1043F():

        label("loc_1043F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1043F")

    QueueWorkItem2(0x105, 1, lambda_1043F)

    label("loc_1044C")

    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1048A")
    EndChrThread(0x104, 0x1)

    def lambda_1046D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1046D)
    Sleep(50)

    def lambda_1047D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1047D)
    Jump("loc_104E3")

    label("loc_1048A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_104B9")
    EndChrThread(0x109, 0x1)

    def lambda_1049C():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1049C)
    Sleep(50)

    def lambda_104AC():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_104AC)
    Jump("loc_104E3")

    label("loc_104B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_104E3")
    EndChrThread(0x105, 0x1)

    def lambda_104CB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_104CB)
    Sleep(50)

    def lambda_104DB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_104DB)

    label("loc_104E3")

    Sleep(300)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0812
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはシンに\x01",
            "『チクタクみっしぃ』を渡した。\x07\x00\x02",
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
        "#12Pこれは、この百貨店限定の……\x02",
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x102,
        "#00100Fなるほど、そういうことだったのね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_105ED")

    #C0815
    ChrTalk(
        0x104,
        "#11P#00309Fへっ、随分気が利くじゃねえか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1065E")

    label("loc_105ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10626")

    #C0816
    ChrTalk(
        0x109,
        "#11P#10109Fふふ、随分気が利きますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1065E")

    label("loc_10626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1065E")

    #C0817
    ChrTalk(
        0x105,
        "#11P#10302Fフフ、随分気が利くじゃないか。\x02",
    )

    CloseMessageWindow()

    label("loc_1065E")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    #C0818
    ChrTalk(
        0x1A2,
        (
            "#12Pってか何だよ、コレ。\x01",
            "こんなのボクにどうしろと……\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ\x01",
            "プレゼントっていうとアレだけど。\x02\x03",

            "今日の記念ってことで、\x01",
            "せっかくだし受け取ってくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x1A2,
        "#12P今日の記念……\x02",
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
            "#12P……こうして買ってしまった以上\x01",
            "捨てるわけにもいかないからな。\x01",
            "そういうことなら受け取ってやる。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    #C0822
    ChrTalk(
        0x1A2,
        (
            "#12Pただし、これだけは言っておくが\x01",
            "こんなぬいぐるみは\x01",
            "ボクの趣味でもなんでもないからな！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10887")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_10934")

    label("loc_10887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_108E0")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_10934")

    label("loc_108E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10934")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_10934")


    #C0823
    ChrTalk(
        0x101,
        "#00000Fあ、ああ、了解だ。\x02",
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

    # Function_52_10258 end

    def Function_53_10982(): pass

    label("Function_53_10982")

    EventBegin(0x1)

    #C0824
    ChrTalk(
        0x101,
        (
            "#00000Fもう外を案内している時間はないな。\x02\x03",

            "適当に店を回ったら屋上に向かおう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -600, 30, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_53_10982 end

    SaveToFile()

Try(main)
