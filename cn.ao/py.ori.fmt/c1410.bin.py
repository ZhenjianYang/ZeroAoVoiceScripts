from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1410.bin",                # FileName
        "c1410",                    # MapName
        "c1410",                    # Location
        0x0030,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 48, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1410",                  # 0
        "阿巴斯",                 # 1
        "良",                     # 2
        "琴兹",                   # 3
        "贝赛",                   # 4
        "亚泽尔",                 # 5
        "亚修莉",                 # 6
        "莎丽娜",                 # 7
        "尤格特",                 # 8
        "市民",                   # 9
        "市民",                   # 10
        "金发青年",               # 11
        "市民",                   # 12
        "市民",                   # 13
        "诺加诺夫",               # 14
        "寇奇",                   # 15
        "迪诺",                   # 16
    ))

    AddCharChip((
        "apl/ch50375.itc",                   # 00
        "chr/ch06700.itc",                   # 01
        "chr/ch30900.itc",                   # 02
        "chr/ch31800.itc",                   # 03
        "chr/ch20502.itc",                   # 04
        "chr/ch34200.itc",                   # 05
        "chr/ch46500.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch34300.itc",                   # 08
        "chr/ch21300.itc",                   # 09
        "chr/ch22100.itc",                   # 0A
        "chr/ch09202.itc",                   # 0B
        "chr/ch06700.itc",                   # 0C
        "chr/ch20402.itc",                   # 0D
        "chr/ch34302.itc",                   # 0E
        "chr/ch21302.itc",                   # 0F
        "chr/ch22102.itc",                   # 10
        "chr/ch06800.itc",                   # 11
        "chr/ch30800.itc",                   # 12
    ))

    DeclNpc(-4719,   0,       11880,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(2980,    0,       14779,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(3200,    0,       7579,    270,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(16149,   0,       12020,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1090,   0,       14909,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-600,    150,     12619,   0,    389,  0x0, 0,   11,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(3789,    0,       55279,   90,   389,  0x0, 0,   4,   0,   255, 255, 0,   28,  255,  0)
    DeclNpc(-2410,   29,      52169,   225,  389,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-1240,   0,       4139,    0,    389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-170,    0,       4019,    315,  389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(15479,   0,       12319,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(15300,   0,       10909,   270,  389,  0x0, 0,   10,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(17079,   1000,    -2579,   225,  389,  0x0, 0,   18,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(11420,   0,       7809,    0,    389,  0x0, 0,   18,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(2920,    0,       6769,    89,   389,  0x0, 0,   17,  0,   0,   0,   0,   32,  255,  0)

    DeclActor(2980,    0,       13420,   1500,    2980,    1500,    14780,   0x007E, 0,  14, 0x0000)
    DeclActor(-1090,   0,       13420,   1500,    -1090,   1500,    14780,   0x007E, 0,  17, 0x0000)

    ChipFrameInfo(884, 0)                                        # 0

    ScpFunction((
        "Function_0_374",          # 00, 0
        "Function_1_424",          # 01, 1
        "Function_2_499",          # 02, 2
        "Function_3_572",          # 03, 3
        "Function_4_661",          # 04, 4
        "Function_5_B47",          # 05, 5
        "Function_6_BF9",          # 06, 6
        "Function_7_19AE",         # 07, 7
        "Function_8_1DFC",         # 08, 8
        "Function_9_1F2D",         # 09, 9
        "Function_10_207C",        # 0A, 10
        "Function_11_2DEB",        # 0B, 11
        "Function_12_2EB1",        # 0C, 12
        "Function_13_2F84",        # 0D, 13
        "Function_14_3C7F",        # 0E, 14
        "Function_15_3C9E",        # 0F, 15
        "Function_16_3E2D",        # 10, 16
        "Function_17_4877",        # 11, 17
        "Function_18_487B",        # 12, 18
        "Function_19_5231",        # 13, 19
        "Function_20_532F",        # 14, 20
        "Function_21_5409",        # 15, 21
        "Function_22_5413",        # 16, 22
        "Function_23_5530",        # 17, 23
        "Function_24_561A",        # 18, 24
        "Function_25_56FD",        # 19, 25
        "Function_26_57A0",        # 1A, 26
        "Function_27_5873",        # 1B, 27
        "Function_28_58D1",        # 1C, 28
        "Function_29_59C1",        # 1D, 29
        "Function_30_5A62",        # 1E, 30
        "Function_31_5B08",        # 1F, 31
        "Function_32_5C05",        # 20, 32
        "Function_33_5CAC",        # 21, 33
        "Function_34_6A87",        # 22, 34
    ))


    def Function_0_374(): pass

    label("Function_0_374")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (1, "loc_3B8"),
        (2, "loc_3C4"),
        (3, "loc_3D0"),
        (4, "loc_3DC"),
        (5, "loc_3E8"),
        (6, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_423")

    Return()

    # Function_0_374 end

    def Function_1_424(): pass

    label("Function_1_424")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_498")
    OP_95(0xFE, 2970, 30, 4200, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(5500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    OP_95(0xFE, 6630, 30, 6580, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Sleep(8500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    Jump("Function_1_424")

    label("loc_498")

    Return()

    # Function_1_424 end

    def Function_2_499(): pass

    label("Function_2_499")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_571")
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 6340, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 5070, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    Jump("Function_2_499")

    label("loc_571")

    Return()

    # Function_2_499 end

    def Function_3_572(): pass

    label("Function_3_572")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_660")
    OP_93(0xFE, 0x0, 0x0)
    OP_95(0xFE, 9900, 30, 10300, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x0)
    OP_95(0xFE, 9900, 30, 12000, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x0)
    OP_95(0xFE, 9900, 30, 13490, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x0)
    OP_95(0xFE, 9900, 30, 12000, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x0)
    OP_95(0xFE, 9900, 30, 10300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x0)
    OP_95(0xFE, 9900, 30, 9810, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    Jump("Function_3_572")

    label("loc_660")

    Return()

    # Function_3_572 end

    def Function_4_661(): pass

    label("Function_4_661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_679")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_B46")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_729")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, -200, 0, 8580, 90)
    SetChrPos(0x17, -1650, 0, 7350, 90)
    SetChrPos(0x16, -1380, 0, 9380, 90)
    SetChrPos(0x9, 2090, 0, 8400, 270)
    SetChrPos(0xB, 3220, 0, 7570, 270)
    SetChrPos(0xA, 4280, 0, 9490, 270)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_724")
    SetMapFlags(0x10000000)
    Event(0, 34)

    label("loc_724")

    Jump("loc_B46")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_775")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 600, 0, 12440, 45)
    SetChrPos(0xB, 4650, 0, 12470, 315)
    SetChrPos(0xC, 2830, 0, 10890, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_B46")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_797")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_B46")

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7F7")
    SetChrPos(0xA, 0, 0, 7400, 90)
    SetChrPos(0xB, 1470, 0, 5650, 0)
    SetChrPos(0x8, 2000, 0, 7720, 225)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F2")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_7F2")

    Jump("loc_B46")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_857")
    SetChrPos(0xA, 0, 0, 7400, 90)
    SetChrPos(0xB, 1470, 0, 5650, 0)
    SetChrPos(0x8, 2000, 0, 7720, 225)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_852")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_852")

    Jump("loc_B46")

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8B3")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -3060, 150, 3640, 0)
    SetChrPos(0x11, -3140, 150, 6740, 180)
    SetChrChipByIndex(0x10, 0xD)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0xE)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_B46")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_90F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -3060, 150, 3640, 0)
    SetChrPos(0x11, -3140, 150, 6740, 180)
    SetChrChipByIndex(0x10, 0xD)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0xE)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_B46")

    label("loc_90F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_973")
    SetChrPos(0x8, -4080, 0, 12480, 45)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2730, 150, 12430, 0)
    SetChrChipByIndex(0xD, 0xB)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95F")
    SetChrFlags(0x8, 0x10)

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96E")
    SetChrFlags(0xD, 0x10)

    label("loc_96E")

    Jump("loc_B46")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_981")
    Jump("loc_B46")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A67")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F1")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 14020, 30, 11650, 270)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x9, 9900, 30, 9810, 90)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 3)
    SetChrPos(0xB, 2980, 0, 14780, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_A44")

    label("loc_9F1")

    SetChrPos(0x13, -3060, 150, 3640, 0)
    SetChrPos(0x14, -3140, 150, 6740, 180)
    SetChrChipByIndex(0x13, 0xF)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A44")
    SetChrFlags(0x8, 0x10)

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A53")
    SetChrFlags(0x13, 0x10)

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A62")
    SetChrFlags(0x14, 0x10)

    label("loc_A62")

    Jump("loc_B46")

    label("loc_A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AFD")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x4)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xE, -2630, 150, 12430, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 15210, 0, 8880, 180)
    SetChrPos(0xB, 15290, 0, 7520, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xA, 0, 0, 7400, 180)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF8")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)

    label("loc_AF8")

    Jump("loc_B46")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_B0B")
    Jump("loc_B46")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B26")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_B26")

    Jump("loc_B46")

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B46")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_B46")

    Return()

    # Function_4_661 end

    def Function_5_B47(): pass

    label("Function_5_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B63")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B82")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B82")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B8F")
    OP_65(0x0, 0x1)

    label("loc_B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA1")
    OP_65(0x1, 0x1)

    label("loc_BA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBA")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_BC0")

    label("loc_BBA")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE1")
    Sound(128, 1, 50, 0)

    label("loc_BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF8")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_BF8")

    Return()

    # Function_5_B47 end

    def Function_6_BF9(): pass

    label("Function_6_BF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C0A")
    Jump("loc_19AA")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C25")
    Jump("loc_C37")

    label("loc_C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    Jump("loc_C37")

    label("loc_C37")

    Jump("loc_19AA")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    Call(0, 7)
    Jump("loc_CC0")

    label("loc_C57")


    #C0001
    ChrTalk(
        0x8,
        (
            "#04100F关于瓦鲁多的事，\x01",
            "我们会继续调查的。\x02\x03",

            "如果有什么新发现，一定会立刻\x01",
            "联络你们，等我们的消息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC0")

    Jump("loc_19AA")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE0")
    Call(0, 8)
    Jump("loc_D14")

    label("loc_CE0")


    #C0002
    ChrTalk(
        0x8,
        (
            "#04100F关于瓦鲁多的情报，\x01",
            "就交给我们来收集吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D14")

    Jump("loc_19AA")

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D79")

    #C0003
    ChrTalk(
        0x8,
        (
            "#04100F……看来你们正在\x01",
            "处理紧急工作啊。\x02\x03",

            "如果有什么事需要帮忙，就尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AA")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6F")

    #C0004
    ChrTalk(
        0x8,
        (
            "#04100F剑蛇帮的人\x01",
            "好像开始寻找瓦鲁多了。\x02\x03",

            "他最近这几天\x01",
            "完全没有现身过……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00301F完全没现身吗……\x01",
            "他到底去了哪里，在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10301F……阿巴斯，\x01",
            "你们也没见过他吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)

    #C0007
    ChrTalk(
        0x8,
        (
            "#04100F嗯，这一周以来，一次都没见过。\x02\x03",

            "在此之前还偶尔\x01",
            "能见到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x105,
        "#10308F是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0009
    ChrTalk(
        0x8,
        (
            "#04100F……瓦吉，你不要太担心。\x02\x03",

            "虽说他消失了踪迹，\x01",
            "但也不过是最近这几天而已。\x02\x03",

            "而且，你现在还有\x01",
            "必须要做的\x01",
            "工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10304F嗯……是啊。\x02\x03",

            "#10302F谢谢你，阿巴斯。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 6)
    Jump("loc_FE1")

    label("loc_F6F")

    TurnDirection(0x8, 0x105, 0)

    #C0011
    ChrTalk(
        0x8,
        (
            "#04100F关于瓦鲁多的事情，\x01",
            "我们也会多加留意的。\x02\x03",

            "瓦吉，你不用操多余的心，\x01",
            "集中精力，做好自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE1")

    Jump("loc_19AA")

    label("loc_FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1001")
    Call(0, 9)
    Jump("loc_10D0")

    label("loc_1001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1096")
    TurnDirection(0x8, 0x105, 0)

    #C0012
    ChrTalk(
        0x8,
        (
            "#04100F瓦吉……你来了啊。\x02\x03",

            "想在店里休息时就尽管说，\x01",
            "我会马上准备席位的。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，\x01",
            "谢了，阿巴斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_10D0")

    label("loc_1096")


    #C0014
    ChrTalk(
        0x8,
        (
            "#04100F想在店里休息时就尽管说，\x01",
            "我会马上准备席位的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D0")

    Jump("loc_19AA")

    label("loc_10D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1178")

    #C0015
    ChrTalk(
        0x8,
        (
            "#04100F……旧城区最近比较安宁。\x02\x03",

            "所以瓦吉你不用\x01",
            "在意这边的事。\x01",
            "集中精力，做好支援科的工作就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        "#10300F嗯……谢了，阿巴斯。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11DF")

    label("loc_1178")


    #C0017
    ChrTalk(
        0x8,
        (
            "#04100F……旧城区最近比较安宁。\x02\x03",

            "所以瓦吉你不用\x01",
            "在意这边的事。\x01",
            "集中精力，做好支援科的工作就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DF")

    Jump("loc_19AA")

    label("loc_11E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C6")

    #C0018
    ChrTalk(
        0x8,
        (
            "#04105F那位客人莫非是……\x02\x03",

            "#04102F……呵，不会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00005F（笑、笑了……？）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#00305F（嗯，真意外啊……）\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        (
            "#10306F（真是的……\x01",
            "  呵呵，你们把阿巴斯\x01",
            "  想成什么样的人了？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12F8")

    label("loc_12C6")


    #C0022
    ChrTalk(
        0x8,
        (
            "#04102F那位客人，莫非是……\x01",
            "……呼，不会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F8")

    Jump("loc_14BA")

    label("loc_12FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147A")

    #C0023
    ChrTalk(
        0x8,
        "#04100F………………………\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        "#10300F阿巴斯，你在想事情吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    #C0025
    ChrTalk(
        0x8,
        (
            "#04100F是瓦吉啊……\x02\x03",

            "……嗯，我在想世上\x01",
            "真是什么样的人都有呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10309F哈哈，确实如此。\x02\x03",

            "#10304F不过，如果这么说的话，\x01",
            "我们也一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "#04102F呵……也对。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00000F（他和瓦吉……\x01",
            "  好像很聊得来。）\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00100F（呵呵，这说明他们的\x01",
            "  关系很好吧。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_14BA")

    label("loc_147A")


    #C0030
    ChrTalk(
        0x8,
        (
            "#04100F………………………\x02\x03",

            "……世上真是\x01",
            "什么样的人都有呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BA")

    Jump("loc_19AA")

    label("loc_14BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1573")

    #C0031
    ChrTalk(
        0x8,
        (
            "#04100F旧城区也有几位\x01",
            "前来巡逻的警官。\x02\x03",

            "瓦吉，支援科的工作没遇到什么困难吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x105,
        (
            "#10300F嗯，至少目前还\x01",
            "没有什么大问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "#04100F是吗，那就好。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15B5")

    label("loc_1573")


    #C0034
    ChrTalk(
        0x8,
        (
            "#04100F旧城区也有几位\x01",
            "前来巡逻的警官。\x02\x03",

            "……真是辛苦他们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B5")

    Jump("loc_19AA")

    label("loc_15BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_171C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DE")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    #C0035
    ChrTalk(
        0x8,
        (
            "#04100F瓦吉，没事吧？\x01",
            "你的脸色好像不太好。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10300F嗯，没事的，\x01",
            "不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        "#04100F……是吗，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10106F（这两人……\x01",
            "  说话莫名地干脆简洁。）\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00100F（嗯，但不可思议的是，\x01",
            "  他们好像完全能明白对方的意思。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1717")

    label("loc_16DE")

    TurnDirection(0x8, 0x105, 0)

    #C0040
    ChrTalk(
        0x8,
        (
            "#04100F瓦吉，在需要我们的\x01",
            "帮助时就尽管开口。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1717")

    Jump("loc_19AA")

    label("loc_171C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_17F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AF")

    #C0041
    ChrTalk(
        0x8,
        (
            "#04100F如果要点单，\x01",
            "和我说也可以。\x02\x03",

            "放松一些，随便点就是。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#00003F（面对着这个人……\x01",
            "  想放松恐怕有些困难。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17EF")

    label("loc_17AF")


    #C0043
    ChrTalk(
        0x8,
        (
            "#04100F如果要点单，\x01",
            "和我说也可以。\x02\x03",

            "放松一些，随便点就是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EF")

    Jump("loc_19AA")

    label("loc_17F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_19AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1965")

    #C0044
    ChrTalk(
        0x8,
        (
            "#04100F瓦吉，圣书会的事\x01",
            "就全交给我吧。\x02\x03",

            "你去做你\x01",
            "想做的事就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10300F嗯，我会的。\x02\x03",

            "#10304F今后我也会时常\x01",
            "来『崔尼蒂』露个面，\x01",
            "但店里的经营工作就要全靠你了。\x02\x03",

            "#10302F呵呵，这里要是倒闭，\x01",
            "可就少了一个可以放松的好地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#04102F嗯，我知道。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#00003F（这两个人的关系真是不可思议啊……）\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x109,
        "#10100F（究竟有着怎样的过去呢？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19AA")

    label("loc_1965")


    #C0049
    ChrTalk(
        0x8,
        (
            "#04100F瓦吉，圣书会的事\x01",
            "就全交给我吧。\x02\x03",

            "你去做你\x01",
            "想做的事就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AA")

    TalkEnd(0xFE)
    Return()

    # Function_6_BF9 end

    def Function_7_19AE(): pass

    label("Function_7_19AE")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C41")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    #C0050
    ChrTalk(
        0x8,
        (
            "#04100F瓦吉……\x01",
            "看来出了\x01",
            "不少大事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "我和贝赛在今天早上\x01",
            "看到过那个红毛老兄……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ACB")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x109,
        (
            "#10108F他果然……\x01",
            "来过旧城区啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACB")


    #C0053
    ChrTalk(
        0xB,
        (
            "怎么说呢……\x01",
            "他、他的表情似乎很凝重。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "我们是在交换店附近\x01",
            "看见他的，但、但他很快\x01",
            "就消失在市区方向了……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        "出、出什么事了吗……？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10303F嗯，是有点事。\x02\x03",

            "#10300F不过，这只是\x01",
            "支援科内部的事情，\x01",
            "大家不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#04100F……是吗。\x02\x03",

            "不过，在需要我们帮忙时，\x01",
            "就尽管开口吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x105,
        "#10300F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00001F（兰迪……你等着，\x01",
            "　我一定会抓到你的……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 2)
    Jump("loc_1DDA")

    label("loc_1C41")


    #C0060
    ChrTalk(
        0x105,
        (
            "#10300F对了，阿巴斯……\x01",
            "有没有收集到关于瓦鲁多的情报？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    #C0061
    ChrTalk(
        0x8,
        (
            "#04100F没有……\x01",
            "目前还没收集到任何\x01",
            "重要的情报。\x02\x03",

            "他在行动时恐怕\x01",
            "有意识地避人耳目，\x01",
            "所以完全没有目击情报。\x02\x03",

            "要想查明他取得药物的渠道，\x01",
            "恐怕是相当困难的。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        "#10303F是吗……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#04100F不过，即使如此，\x01",
            "我们也会继续调查。\x02\x03",

            "如果有什么发现，一定会立刻\x01",
            "联络你们，等我们的消息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        "#10300F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x16E, 1)

    label("loc_1DDA")

    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    Return()

    # Function_7_19AE end

    def Function_8_1DFC(): pass

    label("Function_8_1DFC")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    #C0065
    ChrTalk(
        0x8,
        (
            "#04100F瓦吉……\x01",
            "关于瓦鲁多的情报，\x01",
            "就交给我们来收集吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "等、等制定好计划之后，\x01",
            "我们马上就会去探听消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "你就集中精力，专心处理\x01",
            "支援科的工作吧，瓦吉。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x105,
        "#10300F谢谢，拜托你们了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 0)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    Return()

    # Function_8_1DFC end

    def Function_9_1F2D(): pass

    label("Function_9_1F2D")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0069
    ChrTalk(
        0xD,
        (
            "这家店的生意，\x01",
            "最近好像挺好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xD,
        (
            "真羡慕啊……这种好景气\x01",
            "要是能分我些就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#04102F呵，你那边的状况\x01",
            "也不算差吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        "哈哈，这倒是不能否认。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#00000F（他们两人好像聊得很开心啊。）\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，都是怪人，\x01",
            "  大概很投缘吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#00211F（……如果照这样说，\x01",
            "  瓦吉先生也是一样的。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x10)
    Return()

    # Function_9_1F2D end

    def Function_10_207C(): pass

    label("Function_10_207C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2126")

    #C0076
    ChrTalk(
        0xFE,
        (
            "听说有大量\x01",
            "伤员被送到了\x01",
            "乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "我联络了老爸，\x01",
            "据他说，医院那边虽然\x01",
            "很忙碌，但还能撑得住。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        "……我也要继续加油才行啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_217B")

    label("loc_2126")


    #C0079
    ChrTalk(
        0xFE,
        (
            "虽然还不知道将来会不会\x01",
            "走上和老爸一样的道路……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "……但我也要继续加油才行。\x02",
    )

    CloseMessageWindow()

    label("loc_217B")

    Jump("loc_2DE7")

    label("loc_2180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2236")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F5")

    #C0081
    ChrTalk(
        0xFE,
        (
            "现在最需要考虑的问题\x01",
            "还是附近居民的安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "为防万一，\x01",
            "最好仔细留意\x01",
            "东街那边的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2231")

    label("loc_21F5")


    #C0083
    ChrTalk(
        0xFE,
        (
            "这里的事情就\x01",
            "交给我们好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "你们一定要\x01",
            "平安归来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2231")

    Jump("loc_2DE7")

    label("loc_2236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2409")

    #C0085
    ChrTalk(
        0xFE,
        (
            "阿巴斯今早把大家召集到一起，\x01",
            "只说了一句『崔尼蒂暂时交给你们了』，\x01",
            "然后就离开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "他也没说去哪里，\x01",
            "莫非出了什么事吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#00005F阿巴斯他……？\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#00105F难道和瓦吉\x01",
            "在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "……那就不清楚了。\x01",
            "国防军的那些家伙\x01",
            "一直在市里转来转去……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "该、该不会是被他们逮捕了吧……？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#00201F瓦吉先生他们应该\x01",
            "不会那么大意……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#00303F嗯……\x01",
            "总之，你们还是\x01",
            "先镇定一些吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "……也是呢。\x01",
            "不管怎么说，我们必须守护这家店……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24B8")

    label("loc_2409")


    #C0094
    ChrTalk(
        0xFE,
        (
            "瓦吉和阿巴斯自然令人担心……\x01",
            "……而在乌尔斯拉医院工作的老爸\x01",
            "也很让我惦记，不知他现在是否还好。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "以老爸的性格来说，就算在这种情况下，\x01",
            "大概也只会继续埋头照料患者吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B8")

    Jump("loc_2DE7")

    label("loc_24BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24CB")
    Jump("loc_2DE7")

    label("loc_24CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E6")
    Call(0, 7)
    Jump("loc_255D")

    label("loc_24E6")


    #C0096
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "那位红毛老兄在雨中\x01",
            "还带着大量行李。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "看上去就觉得相当沉重，但他的\x01",
            "行动却能那么敏捷，真是惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255D")

    Jump("loc_2DE7")

    label("loc_2562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257D")
    Call(0, 8)
    Jump("loc_262D")

    label("loc_257D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F6")

    #C0098
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "西克洛斯贝尔街道\x01",
            "昨天发生了脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "听说还有些人受了重伤……\x01",
            "老爸似乎也相当忙碌。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_262D")

    label("loc_25F6")


    #C0100
    ChrTalk(
        0xFE,
        (
            "老爸真是厉害啊……\x01",
            "在这种时候，大家都要依靠他……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262D")

    Jump("loc_2DE7")

    label("loc_2632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269C")

    #C0101
    ChrTalk(
        0xFE,
        "我……我到底想成为怎样的人呢？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……可恶，不管怎么想\x01",
            "都找不到答案啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26F6")

    label("loc_269C")


    #C0103
    ChrTalk(
        0xFE,
        (
            "如今想来，我原本并不是\x01",
            "很讨厌学习……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "如果重新捡起书本，\x01",
            "会不会有什么发现呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F6")

    Jump("loc_2DE7")

    label("loc_26FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_283D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E6")

    #C0105
    ChrTalk(
        0xFE,
        (
            "我小时候也曾想过，\x01",
            "要当一个像老爸\x01",
            "那样的医生……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "但不知从何时起，我发现自己\x01",
            "并没有老爸那么优秀……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "……哎，真是的，\x01",
            "我在说什么呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "唉……就因为我总是\x01",
            "这么优柔寡断，\x01",
            "所以才一直都是半桶水。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2838")

    label("loc_27E6")


    #C0109
    ChrTalk(
        0xFE,
        (
            "话说回来，当服务员\x01",
            "可不能这么不利落。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "我还拿着工资呢，\x01",
            "必须要认真工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2838")

    Jump("loc_2DE7")

    label("loc_283D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2993")

    #C0111
    ChrTalk(
        0xFE,
        (
            "怎么说呢……\x01",
            "大家最近都很有活力。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "怀着混一天算一天的想法而\x01",
            "工作的人只有我一个吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "我到底在干什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#00005F（瓦吉……\x01",
            "  你不和他谈谈吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        (
            "#10304F（嗯，圣书会一直以来\x01",
            "  都尊重大家的自主性。）\x02\x03",

            "#10300F（我不会特意\x01",
            "  说些多余的话。）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            "#00211F（……感觉好像和\x01",
            "  赛尔盖科长一样。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29E5")

    label("loc_2993")


    #C0117
    ChrTalk(
        0xFE,
        (
            "大家最近都很有活力，\x01",
            "只有我一个人在混日子吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "我到底在干什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E5")

    Jump("loc_2DE7")

    label("loc_29EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB1")

    #C0119
    ChrTalk(
        0xFE,
        (
            "今天早上，剑蛇帮的人\x01",
            "撞到了我的肩膀，\x01",
            "并以此为借口找碴挑衅……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "但在我老实道歉之后，\x01",
            "他们就很尴尬地\x01",
            "乖乖走人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "这是阿巴斯\x01",
            "教给我的应对方法，\x01",
            "还真是有效啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2AF5")

    label("loc_2AB1")


    #C0122
    ChrTalk(
        0xFE,
        (
            "这就是所谓的和平应对法吗……\x01",
            "该向阿巴斯学习的东西\x01",
            "真是很多啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF5")

    Jump("loc_2DE7")

    label("loc_2AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B82")

    #C0123
    ChrTalk(
        0xFE,
        "好、好厉害啊，那个金发的客人……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "刚才突然展露了一手弹唱技艺，\x01",
            "随后竟然又用台球把我们\x01",
            "打得落花流水……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C30")

    label("loc_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF4")

    #C0125
    ChrTalk(
        0xFE,
        (
            "外、外面好像\x01",
            "有些吵闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "该不会是刚才的客人……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……算了，\x01",
            "还是不要去想比较好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C30")

    label("loc_2BF4")


    #C0128
    ChrTalk(
        0xFE,
        "该不会是刚才的客人……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "……算了，还是不要去想了。\x02",
    )

    CloseMessageWindow()

    label("loc_2C30")

    Jump("loc_2DE7")

    label("loc_2C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C50")
    Call(0, 11)
    Jump("loc_2C64")

    label("loc_2C50")


    #C0130
    ChrTalk(
        0xFE,
        "客人，这边请。\x02",
    )

    CloseMessageWindow()

    label("loc_2C64")

    Jump("loc_2DE7")

    label("loc_2C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CD9")

    #C0131
    ChrTalk(
        0xFE,
        (
            "呼，一到下雨天，\x01",
            "心情总会有些消沉。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "到处都潮乎乎的，头发也会蓬乱……\x01",
            "真希望雨快些停啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE7")

    label("loc_2CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2DE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D90")

    #C0133
    ChrTalk(
        0xFE,
        "其实我并不擅长接待客人……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "但也没有其它适合做的工作，\x01",
            "无奈之下，也只能当服务员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "话虽如此，既然接受了这份工作，\x01",
            "我就会负起责任，把它做好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DE7")

    label("loc_2D90")


    #C0136
    ChrTalk(
        0xFE,
        (
            "欢迎光临，如果想入座，\x01",
            "我可以为您领路。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "虽然不太像，但我也是本店的服务员呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2DE7")

    TalkEnd(0xFE)
    Return()

    # Function_10_207C end

    def Function_11_2DEB(): pass

    label("Function_11_2DEB")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0138
    ChrTalk(
        0xA,
        "请问是两位吧？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "本店有吧台席和餐桌席，\x01",
            "两位想坐在哪里？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x10,
        (
            "这个嘛……\x01",
            "难得来这样的店，\x01",
            "就坐吧台席如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x11,
        "嗯，好啊。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "明白了，\x01",
            "两位请随我来。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_11_2DEB end

    def Function_12_2EB1(): pass

    label("Function_12_2EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F7A")
    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2ED1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F76")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F21")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2F21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F41")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F71")

    label("loc_2F41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F55")
    Jump("loc_2F71")

    label("loc_2F55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F71")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_2F71")

    Jump("loc_2ED1")

    label("loc_2F76")

    TalkEnd(0xB)
    Return()

    label("loc_2F7A")

    TalkBegin(0xB)
    Call(0, 13)
    TalkEnd(0xB)
    Return()

    # Function_12_2EB1 end

    def Function_13_2F84(): pass

    label("Function_13_2F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_318C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311F")

    #C0143
    ChrTalk(
        0xB,
        (
            "话说回来……真、真是吓了一跳啊。\x01",
            "瓦吉和阿巴斯竟然是教会的人。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30D6")

    #C0144
    ChrTalk(
        0xB,
        (
            "感、感觉你们突然\x01",
            "变得很遥远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x105,
        (
            "#10402F呵呵，本质上并没有变化，\x01",
            "希望你们还像以前一样和我们相处。\x02\x03",

            "#10404F甚至可以说，与你们一起成立『圣书会』\x01",
            "的瓦吉·赫米斯菲亚\x01",
            "才是真正的我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "是、是吗……\x01",
            "你能这么说，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3117")

    label("loc_30D6")


    #C0147
    ChrTalk(
        0xB,
        (
            "你们以前从没显露过丝毫迹象，\x01",
            "说、说实话，我至今都不敢相信。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3117")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3187")

    label("loc_311F")


    #C0148
    ChrTalk(
        0xB,
        (
            "瓦、瓦吉和阿巴斯\x01",
            "竟然是教会的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "你们以前从没显露过丝毫迹象，\x01",
            "说、说实话，我至今都不敢相信。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3187")

    Jump("loc_3C7E")

    label("loc_318C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3255")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3203")

    #C0150
    ChrTalk(
        0xB,
        (
            "还、还是不要\x01",
            "去和那种怪物\x01",
            "战斗为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "它、它现在又没有主动来袭，\x01",
            "多一事不如少一事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3250")

    label("loc_3203")


    #C0152
    ChrTalk(
        0xB,
        (
            "亚泽尔暂、暂时回到\x01",
            "东街陪伴家人去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        "希、希望他和家人都平安无事。\x02",
    )

    CloseMessageWindow()

    label("loc_3250")

    Jump("loc_3C7E")

    label("loc_3255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32C1")

    #C0154
    ChrTalk(
        0xB,
        (
            "阿巴斯也离开了……\x01",
            "有、有什么隐情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "现在也只有照他说的，\x01",
            "好、好好守住这家店才是。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7E")

    label("loc_32C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32CF")
    Jump("loc_3C7E")

    label("loc_32CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3368")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EA")
    Call(0, 7)
    Jump("loc_3363")

    label("loc_32EA")


    #C0156
    ChrTalk(
        0xB,
        (
            "那、那家伙的表情……\x01",
            "怎么说呢，非常有压迫力。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "该、该说是心事重重，\x01",
            "还是煞气逼人呢……\x01",
            "说实话，我真是被吓到了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3363")

    Jump("loc_3C7E")

    label("loc_3368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_33E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3383")
    Call(0, 8)
    Jump("loc_33DB")

    label("loc_3383")


    #C0158
    ChrTalk(
        0xB,
        (
            "接、接下来，我们打算\x01",
            "去各处探听情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "要、要是能查到\x01",
            "『真知』的来路就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DB")

    Jump("loc_3C7E")

    label("loc_33E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_357A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3535")

    #C0160
    ChrTalk(
        0xB,
        "调、调制鸡尾酒，最需要的就是创意。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "只、只有尝试破天荒的创意，\x01",
            "才能创造出划时代的发明。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "但是……我或许是\x01",
            "创新过头了。\x01",
            "……看来我没有才能啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "所以……\x01",
            "我、我决定放弃调制鸡尾酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "这是我最后的作品……\x01",
            "请、请你们处理掉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0165
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D7, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 5)
    Jump("loc_3575")

    label("loc_3535")


    #C0166
    ChrTalk(
        0xB,
        "我、我决定放弃调制鸡尾酒。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xB,
        "……因为我不想变成杀人犯。\x02",
    )

    CloseMessageWindow()

    label("loc_3575")

    Jump("loc_3C7E")

    label("loc_357A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C5")

    #C0168
    ChrTalk(
        0xB,
        (
            "我调的鸡尾酒\x01",
            "被、被亚修莉女士\x01",
            "大量买走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "她、她夸奖说……味道和颜色姑且不提，\x01",
            "至少可以用在战场上。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        "嗯……？这、这算是夸奖吗？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "总、总之……\x01",
            "我的鸡尾酒得到过\x01",
            "亚修莉女士的认可。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        "不、不介意的话，你们就拿去吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0173
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 4)
    Jump("loc_373D")

    label("loc_36C5")


    #C0174
    ChrTalk(
        0xB,
        (
            "我的鸡尾酒可以用在战场上……\x01",
            "也、也就是说，含有丰富的营养。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "虽然气味有点那个……\x01",
            "但、但你们就一口气喝下去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373D")

    Jump("loc_3C7E")

    label("loc_3742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388E")

    #C0176
    ChrTalk(
        0xB,
        (
            "亚、亚泽尔和良\x01",
            "总在一起开心地\x01",
            "研究鸡尾酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "所、所以我也\x01",
            "试着做了一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "虽、虽然他们说颜色太难看，\x01",
            "不能作为店里的商品……\x01",
            "但这种成分一定对身体有好处。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        "不、不介意的话，你们就拿去吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0180
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D1, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0181
    ChrTalk(
        0x101,
        "#00005F啊……嗯……谢谢你。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 3)
    Jump("loc_3903")

    label("loc_388E")


    #C0182
    ChrTalk(
        0xB,
        (
            "我对鸡尾酒的选材\x01",
            "有绝对的自信。\x01",
            "它、它一定对身体有好处。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "虽然颜色有点那个……\x01",
            "但、但你们就一口气喝下去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3903")

    Jump("loc_3C7E")

    label("loc_3908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D9")

    #C0184
    ChrTalk(
        0xB,
        (
            "今、今早我和琴兹\x01",
            "一起出门进货，\x01",
            "结果碰到了剑蛇帮的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "我差点就要\x01",
            "和他们打起来，\x01",
            "但却被琴兹制止了。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xB,
        (
            "没想到用那种方法\x01",
            "就能让剑蛇帮的人退却……\x01",
            "这、这或许是一大发现呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A35")

    label("loc_39D9")


    #C0187
    ChrTalk(
        0xB,
        (
            "我们已、已经不会\x01",
            "再打无意义的架了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "要、要是被打得鼻青脸肿，\x01",
            "就不能来店里工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A35")

    Jump("loc_3C7E")

    label("loc_3A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA9")

    #C0189
    ChrTalk(
        0xB,
        "可恶，竟然连良都要输给他了……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        (
            "那个穿着白大衣的金发客人……\x01",
            "相、相当厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADE")

    label("loc_3AA9")


    #C0191
    ChrTalk(
        0xB,
        (
            "那个穿着白大衣的金发客人……\x01",
            "简直像是一道旋风。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADE")

    Jump("loc_3C7E")

    label("loc_3AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B5D")

    #C0192
    ChrTalk(
        0xB,
        (
            "托、托你们的福，来自市区的\x01",
            "客人最近开始增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "不过，大概是担心治安不好，\x01",
            "一到晚上就没多少人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7E")

    label("loc_3B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD4")

    #C0194
    ChrTalk(
        0xB,
        (
            "只、只要后面没人等着玩，\x01",
            "台球基本上是随便打的。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "不、不过条件是\x01",
            "要至少点一杯饮料。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C13")

    label("loc_3BD4")


    #C0196
    ChrTalk(
        0xB,
        (
            "台、台球基本上\x01",
            "是随便打的。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        "不、不过只限店里的客人。\x02",
    )

    CloseMessageWindow()

    label("loc_3C13")

    Jump("loc_3C7E")

    label("loc_3C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C7E")

    #C0198
    ChrTalk(
        0xB,
        (
            "我负责担任台球\x01",
            "的指、指导员兼\x01",
            "计分员。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "要、要是不懂打球的方法\x01",
            "和规则，就来问我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C7E")

    Return()

    # Function_13_2F84 end

    def Function_14_3C7F(): pass

    label("Function_14_3C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9A")
    Call(0, 12)
    Jump("loc_3C9D")

    label("loc_3C9A")

    Call(0, 15)

    label("loc_3C9D")

    Return()

    # Function_14_3C7F end

    def Function_15_3C9E(): pass

    label("Function_15_3C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D5A")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEF")

    #C0200
    ChrTalk(
        0x9,
        (
            "唉，这种时候，要是瓦吉\x01",
            "和阿巴斯在就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D56")

    label("loc_3CEF")


    #C0201
    ChrTalk(
        0x9,
        (
            "没想到还会有和剑蛇帮\x01",
            "合作的一天。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "不过，我们非常清楚\x01",
            "他们的实力，\x01",
            "没有比他们更合适的同伴了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D56")

    TalkEnd(0x9)
    Return()

    label("loc_3D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D77")
    TalkBegin(0x9)
    Call(0, 22)
    TalkEnd(0x9)
    Return()

    label("loc_3D77")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E29")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DD4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF4")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E24")

    label("loc_3DF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E08")
    Jump("loc_3E24")

    label("loc_3E08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E24")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_3E24")

    Jump("loc_3D84")

    label("loc_3E29")

    TalkEnd(0x9)
    Return()

    # Function_15_3C9E end

    def Function_16_3E2D(): pass

    label("Function_16_3E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EBD")

    #C0203
    ChrTalk(
        0x9,
        (
            "阿巴斯以前也会\x01",
            "偶尔离开\x01",
            "一阵子……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "但我感觉他这次的\x01",
            "表情比以往更加\x01",
            "严肃认真。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "……希望他能\x01",
            "早点回来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F01")

    label("loc_3EBD")


    #C0206
    ChrTalk(
        0x9,
        (
            "他说暂时离开，\x01",
            "暂时到底是多久啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "……希望他能\x01",
            "早点回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F01")

    Jump("loc_4876")

    label("loc_3F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F83")

    #C0208
    ChrTalk(
        0x9,
        (
            "我正在这里\x01",
            "给那些努力工作的\x01",
            "人们调制特制饮料。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x9,
        (
            "大家都很能喝呢，\x01",
            "搅拌机一直是全速运转状态。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4143")

    label("loc_3F83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40AB")

    #C0210
    ChrTalk(
        0x9,
        (
            "听说支援科的各位\x01",
            "也来协助重建工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "把这个拿去吧，\x01",
            "是我给大家做的\x01",
            "特制饮料哦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0212
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了６个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1CF, 6)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0213
    ChrTalk(
        0x101,
        "#00005F白拿这么多，真的好吗？\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，一人一杯嘛。\x01",
            "谢谢啦，良。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        "哈哈，不客气。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 4)
    Jump("loc_40EE")

    label("loc_40AB")


    #C0216
    ChrTalk(
        0x9,
        (
            "谢谢你们\x01",
            "来参与重建工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x9,
        "呵呵，不愧是特别任务支援科啊。\x02",
    )

    CloseMessageWindow()

    label("loc_40EE")

    Jump("loc_4143")

    label("loc_40F3")


    #C0218
    ChrTalk(
        0x9,
        (
            "亚泽尔他们做的猪骨汤\x01",
            "似乎颇受好评。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x9,
        (
            "怎么说呢，赈济餐\x01",
            "真是温暖人心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4143")

    Jump("loc_4876")

    label("loc_4148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4205")

    #C0220
    ChrTalk(
        0x9,
        (
            "听说这次的占领事件\x01",
            "好像是帝国政府\x01",
            "策动的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "据说是要以此事件为借口，\x01",
            "要求克洛斯贝尔\x01",
            "允许帝国驻军……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x9,
        (
            "如果这是真的，\x01",
            "那帝国政府实在是\x01",
            "不可饶恕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_425E")

    label("loc_4205")


    #C0223
    ChrTalk(
        0x9,
        (
            "如果真的是帝国政府\x01",
            "为了政治目的而引发\x01",
            "了这起占领事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        (
            "那实在是\x01",
            "不可饶恕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_425E")

    Jump("loc_4876")

    label("loc_4263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_42B4")

    #C0225
    ChrTalk(
        0x9,
        (
            "瓦鲁多……\x01",
            "现在正在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        "要是酒还好……药物就太……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_42B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_43B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432C")

    #C0227
    ChrTalk(
        0x9,
        (
            "那些客人好像\x01",
            "非常喜欢我们这里的\x01",
            "汤汁薏面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        (
            "呵呵，不愧是阿巴斯秘传的\x01",
            "特制食谱啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_43AF")

    label("loc_432C")


    #C0229
    ChrTalk(
        0x9,
        (
            "自己做出来的料理\x01",
            "能让别人露出笑容，\x01",
            "真是一件幸福的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x9,
        (
            "做料理虽然很辛苦，但只要看到客人\x01",
            "露出笑容，就感觉一切都有了回报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AF")

    Jump("loc_4876")

    label("loc_43B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_451C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A2")

    #C0231
    ChrTalk(
        0x9,
        (
            "昨天有两个剑蛇帮成员\x01",
            "跑到我们这里来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        (
            "看他们那副\x01",
            "气势汹汹的样子，\x01",
            "本以为是来打架的。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "结果他们一直眉头紧锁，\x01",
            "仔细问过瓦鲁多的事情之后就走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x9,
        (
            "竟然让小弟这么担心。\x01",
            "瓦鲁多……到底在干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4517")

    label("loc_44A2")


    #C0235
    ChrTalk(
        0x9,
        (
            "虽然曾是敌人，\x01",
            "可我以前一直觉得瓦鲁多\x01",
            "多少有些值得尊敬的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x9,
        (
            "但老实说，现在的他\x01",
            "真是没资格再当头目了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4517")

    Jump("loc_4876")

    label("loc_451C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_458F")

    #C0237
    ChrTalk(
        0x9,
        (
            "贝赛往调酒壶里\x01",
            "放了些诡异的东西，\x01",
            "真的没问题吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x9,
        (
            "要是他找我商量，\x01",
            "我还可以给点建议呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_458F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_46A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4630")

    #C0239
    ChrTalk(
        0x9,
        "呀，欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x9,
        (
            "今天进到了很应季的好材料，\x01",
            "向您推荐我们每日一换的小盘料理哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x9,
        (
            "另外也有午餐菜单，\x01",
            "如果有兴趣，请随便点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_46A2")

    label("loc_4630")


    #C0242
    ChrTalk(
        0x9,
        (
            "今天进到了很应季的好材料，\x01",
            "向您推荐我们每日一换的小盘料理哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        (
            "另外也有午餐菜单，\x01",
            "如果有兴趣，请随便点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46A2")

    Jump("loc_4876")

    label("loc_46A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BF")
    Jump("loc_471D")

    label("loc_46BF")


    #C0244
    ChrTalk(
        0x9,
        (
            "虽然最后没能和那位客人\x01",
            "分出胜负……\x01",
            "但老实说，我完全不是他的对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        "真是人外有人啊。\x02",
    )

    CloseMessageWindow()

    label("loc_471D")

    Jump("loc_4876")

    label("loc_4722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4780")

    #C0246
    ChrTalk(
        0x9,
        (
            "哈哈，亚泽尔的姐姐\x01",
            "还是那么爱操心。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        (
            "听他们两人说话，\x01",
            "总是忍不住想笑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_4780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47F4")

    #C0248
    ChrTalk(
        0x9,
        (
            "哎呀呀……在下雨天，\x01",
            "光是进货就很麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "全身各处都沾上了泥，\x01",
            "在做料理之前，要先换衣服才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_47F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4876")

    #C0250
    ChrTalk(
        0x9,
        (
            "呀，欢迎光临。\x01",
            "如果想点单，请尽管说哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x9,
        (
            "无论是鸡尾酒还是下酒小菜，\x01",
            "我都会让你们见识一下\x01",
            "阿巴斯亲自传授的技巧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4876")

    Return()

    # Function_16_3E2D end

    def Function_17_4877(): pass

    label("Function_17_4877")

    Call(0, 18)
    Return()

    # Function_17_4877 end

    def Function_18_487B(): pass

    label("Function_18_487B")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AC")

    #C0252
    ChrTalk(
        0xC,
        "『崔尼蒂』重新开业了。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "虽然目前的形势不容乐观，\x01",
            "但还是应该保持平常心，\x01",
            "像以往一样正常生活。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4976")

    #C0254
    ChrTalk(
        0x105,
        (
            "#10400F呵呵，你们加油吧。\x01",
            "即使在这种时期，\x01",
            "也会有人期待来店的。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        (
            "嗯，当然了。\x01",
            "你也加油啊，瓦吉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49A4")

    label("loc_4976")


    #C0256
    ChrTalk(
        0xC,
        (
            "姐姐和尤格特\x01",
            "都支持我，\x01",
            "我得加油干才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A4")

    SetScenarioFlags(0x0, 5)
    Jump("loc_4A09")

    label("loc_49AC")


    #C0257
    ChrTalk(
        0xC,
        (
            "『崔尼蒂』重新开业了。\x01",
            "请各位随意点单吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "姐姐和尤格特\x01",
            "都支持我，\x01",
            "我得加油干才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A09")

    Jump("loc_522D")

    label("loc_4A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4A1C")
    Jump("loc_522D")

    label("loc_4A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4A91")

    #C0259
    ChrTalk(
        0xC,
        (
            "闹得满城风雨的\x01",
            "独立宣言真是\x01",
            "让人在意啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "……不然还是回家一趟，\x01",
            "看看姐姐和尤格特的情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522D")

    label("loc_4A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A9F")
    Jump("loc_522D")

    label("loc_4A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B31")

    #C0261
    ChrTalk(
        0xC,
        (
            "袭击玛因兹的神秘部队\x01",
            "似乎强得可怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "据说连警备队都\x01",
            "陷入了苦战……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "……总而言之，\x01",
            "真希望事态尽快平息啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4B7E")

    label("loc_4B31")


    #C0264
    ChrTalk(
        0xC,
        (
            "不知为何，\x01",
            "在这种时候就会\x01",
            "莫名地担心家人。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        (
            "稍后回家\x01",
            "看看情况吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B7E")

    Jump("loc_522D")

    label("loc_4B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4BF1")

    #C0266
    ChrTalk(
        0xC,
        (
            "瓦鲁多可能也服用了当时\x01",
            "那个叫迪诺的新人吃的药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "虽说是敌对团伙，\x01",
            "但还是很担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522D")

    label("loc_4BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA4")

    #C0268
    ChrTalk(
        0xC,
        "呼，都到下午了啊。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xC,
        (
            "说起来，姐姐说她\x01",
            "今天也要去工作。\x01",
            "该不会是又在逞强吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "我明明和她说过，\x01",
            "我现在也开始工作了，\x01",
            "她可以减少一些工作量……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D24")

    label("loc_4CA4")


    #C0271
    ChrTalk(
        0xC,
        (
            "说起来，姐姐说她\x01",
            "今天也要去工作。\x01",
            "该不会是又在逞强吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "我明明和她说过，\x01",
            "我现在也开始工作了，\x01",
            "她可以减少一些工作量……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D24")

    Jump("loc_522D")

    label("loc_4D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DED")

    #C0273
    ChrTalk(
        0xC,
        (
            "琴兹那家伙，\x01",
            "最近似乎一直在烦恼\x01",
            "将来的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "他头脑聪明，\x01",
            "家里又有钱。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "只要有心，\x01",
            "不管想做什么都能成功吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "不过，怎么说呢……\x01",
            "每个人都有自己的烦恼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4E73")

    label("loc_4DED")


    #C0277
    ChrTalk(
        0xC,
        (
            "说起来，琴兹以前好像说过，\x01",
            "他老爸的存在让他\x01",
            "感到很自卑。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xC,
        (
            "他认为即使通过努力而当上医生，\x01",
            "如果不能超越老爸\x01",
            "也是没有意义的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E73")

    Jump("loc_522D")

    label("loc_4E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ED1")

    #C0279
    ChrTalk(
        0xC,
        (
            "阿巴斯精通各种事情，\x01",
            "学识十分渊博。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        "我总能从他身上学到不少东西。\x02",
    )

    CloseMessageWindow()
    Jump("loc_522D")

    label("loc_4ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F20")

    #C0281
    ChrTalk(
        0xC,
        "最近工作起来很开心。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        (
            "我觉得自己可以\x01",
            "一直在这里干下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522D")

    label("loc_4F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5008")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FAF")

    #C0283
    ChrTalk(
        0xC,
        (
            "有个穿白大衣的客人\x01",
            "突然提出要和我们\x01",
            "比赛台球。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "结果大家都输给他了，现在正在和他\x01",
            "比赛的良，是我们最后的希望。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5003")

    label("loc_4FAF")


    #C0285
    ChrTalk(
        0xC,
        (
            "话说回来……\x01",
            "真是个奇怪的客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "该怎么说呢……\x01",
            "特别想和谁说说他的行为啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5003")

    Jump("loc_522D")

    label("loc_5008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5062")

    #C0287
    ChrTalk(
        0xC,
        (
            "唉，姐姐也不用\x01",
            "突然跑到这里啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        (
            "……算了，\x01",
            "现在要集中精神干活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522D")

    label("loc_5062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_50E8")

    #C0289
    ChrTalk(
        0xC,
        (
            "在良的指导下，\x01",
            "我偶尔也可以\x01",
            "调配鸡尾酒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xC,
        (
            "虽然调鸡尾酒是一门很深奥\x01",
            "的学问，做起来不大容易，\x01",
            "但还是很有趣的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522D")

    label("loc_50E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_522D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51DE")

    #C0291
    ChrTalk(
        0xC,
        (
            "在瓦吉加入特别任务支援科之后，\x01",
            "我们大家讨论了\x01",
            "很多事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "总之，我们决定\x01",
            "齐心协力，\x01",
            "共同打理『崔尼蒂』。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xC,
        (
            "这里原本就是组织的据点，\x01",
            "也是由阿巴斯精心\x01",
            "打理的店。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xC,
        (
            "我们今后要大力招揽顾客，\x01",
            "努力经营店铺。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_522D")

    label("loc_51DE")


    #C0295
    ChrTalk(
        0xC,
        "今后也请多多关照『崔尼蒂』。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        (
            "本店的菜品很丰富，\x01",
            "想来用餐也十分欢迎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_522D")

    TalkEnd(0xC)
    Return()

    # Function_18_487B end

    def Function_19_5231(): pass

    label("Function_19_5231")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5291")

    #C0297
    ChrTalk(
        0xFE,
        (
            "这里的汤汁薏面\x01",
            "非常美味。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "说实话，\x01",
            "这已经超出酒吧\x01",
            "单品料理的水准了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_532B")

    label("loc_5291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_52D7")

    #C0299
    ChrTalk(
        0xFE,
        "那个服务员遇到了什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "感觉他心不在焉的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_532B")

    label("loc_52D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_532B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F2")
    Call(0, 11)
    Jump("loc_532B")

    label("loc_52F2")


    #C0301
    ChrTalk(
        0xFE,
        (
            "我是听了别人的介绍后来这里的……\x01",
            "气氛还挺不错的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_532B")

    TalkEnd(0xFE)
    Return()

    # Function_19_5231 end

    def Function_20_532F(): pass

    label("Function_20_532F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_536F")

    #C0302
    ChrTalk(
        0xFE,
        (
            "呵呵，这通心粉的口感\x01",
            "真是绝妙啊～好幸福⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5405")

    label("loc_536F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_53BF")

    #C0303
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "我又来这家店了。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "这里还是这么别致，\x01",
            "气氛很好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5405")

    label("loc_53BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53DA")
    Call(0, 11)
    Jump("loc_5405")

    label("loc_53DA")


    #C0305
    ChrTalk(
        0xFE,
        (
            "哦，在这种地方，\x01",
            "竟然还有这样的店啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5405")

    TalkEnd(0xFE)
    Return()

    # Function_20_532F end

    def Function_21_5409(): pass

    label("Function_21_5409")

    TalkBegin(0xFE)
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    # Function_21_5409 end

    def Function_22_5413(): pass

    label("Function_22_5413")

    OP_4B(0x12, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54D8")

    #C0306
    ChrTalk(
        0x12,
        (
            "哈哈哈，少年，\x01",
            "你已经无路可退了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x9,
        "……小哥，你很厉害呢。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x9,
        (
            "恐怕和瓦吉不相上下……\x01",
            "不，说不定要更加厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x105,
        (
            "#10305F（……哦？\x01",
            "  看来实力很强呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5524")

    label("loc_54D8")


    #C0310
    ChrTalk(
        0x12,
        "来，接下来轮到你了。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        (
            "嗯、嗯……\x01",
            "我正在考虑该瞄准哪里，\x01",
            "稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5524")

    OP_4C(0x12, 0xFF)
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_22_5413 end

    def Function_23_5530(): pass

    label("Function_23_5530")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0312
    ChrTalk(
        0x14,
        "呀，好厉害～！\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x13,
        "真是好帅啊⊥\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x12,
        (
            "哈哈，说到『瞄准』，\x01",
            "我还是有一些自信的。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x12,
        (
            "不过，我现在瞄准的\x01",
            "并不是那些球，\x01",
            "而是你们的心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x13,
        "讨厌，又说这种话⊥\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x14,
        "呵呵，真是很有一套呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_23_5530 end

    def Function_24_561A(): pass

    label("Function_24_561A")


    #C0318
    ChrTalk(
        0x13,
        (
            "啊～没想到\x01",
            "他突然跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x13,
        (
            "早知如此，\x01",
            "真该问问他住在哪里～\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x14,
        (
            "嗯～他长得\x01",
            "确实很帅啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x14,
        (
            "但性格好像\x01",
            "有些奇怪吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x13,
        (
            "笨蛋～性格奇怪\x01",
            "有什么关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x13,
        (
            "那也是他的\x01",
            "魅力之一嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x14,
        "是、是这样吗。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    Return()

    # Function_24_561A end

    def Function_25_56FD(): pass

    label("Function_25_56FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5744")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571C")
    Call(0, 23)
    Jump("loc_573F")

    label("loc_571C")


    #C0325
    ChrTalk(
        0xFE,
        (
            "呵呵呵，今天遇到了\x01",
            "一位帅哥⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_573F")

    Jump("loc_579C")

    label("loc_5744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5756")
    Call(0, 24)
    Jump("loc_579C")

    label("loc_5756")


    #C0326
    ChrTalk(
        0xFE,
        (
            "啊～没想到\x01",
            "他突然跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "早知如此，\x01",
            "真该问问他住在哪里～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_579C")

    TalkEnd(0xFE)
    Return()

    # Function_25_56FD end

    def Function_26_57A0(): pass

    label("Function_26_57A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57BF")
    Call(0, 23)
    Jump("loc_57F0")

    label("loc_57BF")


    #C0328
    ChrTalk(
        0xFE,
        (
            "这个人不仅擅长乐器演奏，\x01",
            "打台球也很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57F0")

    Jump("loc_586F")

    label("loc_57F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5807")
    Call(0, 24)
    Jump("loc_586F")

    label("loc_5807")


    #C0329
    ChrTalk(
        0xFE,
        (
            "长得帅，唱歌和乐器都很拿手，\x01",
            "而且连台球都打得那么好……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "不过，怎么说呢，\x01",
            "我倒是没什么感觉啦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_586F")

    TalkEnd(0xFE)
    Return()

    # Function_26_57A0 end

    def Function_27_5873(): pass

    label("Function_27_5873")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5888")
    Call(0, 9)
    Jump("loc_58CD")

    label("loc_5888")


    #C0331
    ChrTalk(
        0xFE,
        (
            "呵呵，大白天喝酒，\x01",
            "真是无比美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "感觉五脏六腑都沁透了。\x02",
    )

    CloseMessageWindow()

    label("loc_58CD")

    TalkEnd(0xFE)
    Return()

    # Function_27_5873 end

    def Function_28_58D1(): pass

    label("Function_28_58D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5975")

    #C0333
    ChrTalk(
        0xFE,
        (
            "我事先没有告诉弟弟，\x01",
            "就直接来他打工的酒吧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "他一开始挺难为情，\x01",
            "不过还是用心接待我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "保持着职业意识而工作，\x01",
            "真是值得表扬呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_59BD")

    label("loc_5975")


    #C0336
    ChrTalk(
        0xFE,
        "（咕嘟咕嘟）……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "亚泽尔调的\x01",
            "无酒精鸡尾酒……\x01",
            "真是相当美味啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59BD")

    TalkEnd(0xFE)
    Return()

    # Function_28_58D1 end

    def Function_29_59C1(): pass

    label("Function_29_59C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A2E")

    #C0338
    ChrTalk(
        0xFE,
        (
            "哇～\x01",
            "大家都穿得和\x01",
            "亚泽尔哥哥一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "真好啊～我也想要\x01",
            "和哥哥一样的\x01",
            "蓝色连帽衫。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5A5E")

    label("loc_5A2E")


    #C0340
    ChrTalk(
        0xFE,
        (
            "真好啊～我也想要\x01",
            "和哥哥一样的\x01",
            "蓝色连帽衫。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A5E")

    TalkEnd(0xFE)
    Return()

    # Function_29_59C1 end

    def Function_30_5A62(): pass

    label("Function_30_5A62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD7")

    #C0341
    ChrTalk(
        0xFE,
        (
            "虽然还不太明白，\x01",
            "总之，先把那些\x01",
            "盔甲怪物全干掉吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "换作瓦鲁多大哥，\x01",
            "也一定会这么做的～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B04")

    label("loc_5AD7")


    #C0343
    ChrTalk(
        0xFE,
        (
            "虽然还不太明白，\x01",
            "不过就大干一场吧～！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B04")

    TalkEnd(0xFE)
    Return()

    # Function_30_5A62 end

    def Function_31_5B08(): pass

    label("Function_31_5B08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B7E")

    #C0344
    ChrTalk(
        0xFE,
        (
            "那些盔甲怪物好像\x01",
            "并没有到旧城区这边来。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "我们已经让『鬼火』附近的\x01",
            "居民们都到室内避难了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C01")

    label("loc_5B7E")


    #C0346
    ChrTalk(
        0xFE,
        (
            "要是杰德前辈他们\x01",
            "也来帮忙就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "但他们似乎还是无法接受瓦鲁多大哥\x01",
            "以那样的形式与大家断绝往来的事实，\x01",
            "这也没办法啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C01")

    TalkEnd(0xFE)
    Return()

    # Function_31_5B08 end

    def Function_32_5C05(): pass

    label("Function_32_5C05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3D")

    #C0348
    ChrTalk(
        0xFE,
        "外面那些蓝色的雾气到底是什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CA8")

    label("loc_5C3D")


    #C0349
    ChrTalk(
        0xFE,
        (
            "哼……跟这些蓝衣小子的合作，\x01",
            "仅限这一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "为了让瓦鲁多大哥\x01",
            "今后随时都能回来，\x01",
            "我们要守护旧城区。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA8")

    TalkEnd(0xFE)
    Return()

    # Function_32_5C05 end

    def Function_33_5CAC(): pass

    label("Function_33_5CAC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04100.itp")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(12000, 1000, 12000, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -300, 0, -500, 0)
    SetChrPos(0x102, 500, 0, -500, 0)
    SetChrPos(0x109, -300, 0, -500, 0)
    SetChrPos(0x105, 500, 0, -500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(4000, 1000, 7000, 8000)
    MoveCamera(25, 17, 0, 8000)
    SetCameraDistance(23500, 8000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(500, 1000, 4340, 0)
    MoveCamera(34, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24160, 0)
    SetCameraDistance(23000, 2000)

    def lambda_5E06():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E06)

    def lambda_5E20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E20)
    Sleep(400)

    def lambda_5E34():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E34)

    def lambda_5E4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5E4E)
    Sleep(400)

    def lambda_5E62():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E62)

    def lambda_5E7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5E7C)
    Sleep(400)

    def lambda_5E90():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E90)

    def lambda_5EAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5EAA)
    WaitChrThread(0x101, 1)

    def lambda_5EBF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5EBF)
    WaitChrThread(0x102, 1)

    def lambda_5ED0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5ED0)
    WaitChrThread(0x109, 1)

    def lambda_5EE1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5EE1)
    WaitChrThread(0x105, 1)

    def lambda_5EF2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5EF2)
    WaitChrThread(0x105, 2)
    OP_6F(0x10)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 0)

    #C0351
    ChrTalk(
        0xA,
        (
            "欢迎光临，\x01",
            "客人一共几位……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0352
    ChrTalk(
        0xA,
        (
            "哎，你们不是特别任务支援科吗！？\x01",
            "连瓦吉也来了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#6P#00005F欢、欢迎光临……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 500)

    #C0354
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，看来你们\x01",
            "在认真营业啊，\x01",
            "真是太好了。\x02\x03",

            "#10302F呵呵，怎么样？\x01",
            "阿巴斯，生意还好吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-3430, 1100, 10150, 3000)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0355
    AnonymousTalk(
        0x8,
        (
            "……嗯，还可以吧。\x02\x03",

            "话说回来，你难得回来一趟，\x01",
            "好好休息一下吧。\x02",
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
    FadeToDark(500, 0, -1)
    OP_0D()

    def lambda_60FD():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_60FD)

    def lambda_610A():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_610A)

    def lambda_6117():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6117)

    def lambda_6124():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6124)

    def lambda_6131():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6131)
    OP_68(-3700, 1000, 10960, 0)
    MoveCamera(9, 24, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23630, 0)
    SetChrPos(0xB, 4430, 0, 9820, 270)
    SetChrPos(0xA, 3200, 0, 7580, 270)
    SetChrPos(0x101, -2360, 0, 10680, 295)
    SetChrPos(0x102, -1270, 0, 9630, 295)
    SetChrPos(0x109, -2900, 0, 8830, 340)
    SetChrPos(0x105, -3950, 0, 9870, 340)
    FadeToBright(1000, 0)
    OP_0D()

    #C0356
    ChrTalk(
        0x8,
        "#04100F……瓦吉，特别任务支援科怎么样？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x105,
        (
            "#12P#10300F嗯，待得还算愉快。\x02\x03",

            "#10304F科长和前辈们都很好说话，\x01",
            "我过得挺随性的。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#12P#00006F这个……老实说，\x01",
            "我觉得瓦吉是随性过头了。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x109,
        (
            "#12P#10101F是呀，瓦吉。\x01",
            "虽说你是准成员，\x01",
            "但也应该有身为警察的自觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，话虽如此，\x01",
            "但这就是我的作风啊。\x02\x03",

            "#10304F你们也不要太一本正经了，\x01",
            "稍微放松点也无所谓吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        (
            "#12P#00106F……唉，看来和瓦吉\x01",
            "说什么都是没用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#04100F……唔，看来你在支援科\x01",
            "待得还不错，\x01",
            "那就没有问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#12P#00006F（但我却觉得问题\x01",
            "　多到数不清呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x101,
        (
            "#12P#00005F说起来……\x01",
            "圣书会的成员都不反对\x01",
            "瓦吉加入特别任务支援科吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x102,
        (
            "#12P#00105F啊，的确……\x01",
            "大家多少都会\x01",
            "感到不知所措吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#04100F……没什么好反对的，\x01",
            "因为一切都是瓦吉的决定。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x109,
        "#12P#10106F（这好像不算回答啊……）\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        (
            "#12P#00006F（说起来，这个人\x01",
            "  就是这种性格呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(320, 1500, 10860, 3000)
    MoveCamera(24, 15, 0, 3000)
    OP_6E(360, 3000)
    SetCameraDistance(24690, 3000)
    OP_6F(0x79)

    #C0369
    ChrTalk(
        0x9,
        (
            "#11P嗯，起初的确是有些不知所措……\x01",
            "不过，经过内部讨论之后，\x01",
            "所有成员都已接受了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6605():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6605)
    Sleep(10)

    def lambda_6615():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6615)

    def lambda_6622():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6622)
    Sleep(10)

    def lambda_6632():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6632)
    Sleep(10)

    #C0370
    ChrTalk(
        0xA,
        (
            "#12P我们都是因为反抗父母、遇到家庭矛盾\x01",
            "等各种原因而聚集到一起的……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xA,
        (
            "#12P既然瓦吉找到了自己的道路，\x01",
            "决定要脱离组织，\x01",
            "我们自然没有反对的道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xA,
        (
            "#12P说不定，这反而能成为\x01",
            "我们自立的契机嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "#11P老实说，比、比起成天打架的时候，\x01",
            "如今在这里打理『崔尼蒂』的生活，\x01",
            "让我感到更加充实。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "#5P不过，瓦吉离开了，\x01",
            "确实有点寂寞。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#6P#00002F哈哈……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x109,
        "#6P#N#10102F看来你们还挺乐观啊。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0377
    ChrTalk(
        0x105,
        (
            "#6P#10304F嗯，圣书会的事务原本就是\x01",
            "基本交由阿巴斯来处理的。\x02\x03",

            "#10300F就算没有我，\x01",
            "大家应该也没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        "#6P#04102F……就是这样。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-3700, 1000, 10960, 0)
    MoveCamera(24, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23630, 0)
    SetChrPos(0x101, -2360, 0, 10680, 295)
    SetChrPos(0x102, -1270, 0, 9630, 295)
    SetChrPos(0x109, -2900, 0, 8830, 340)
    SetChrPos(0x105, -3950, 0, 9870, 340)
    OP_6F(0x79)
    OP_0D()

    #C0379
    ChrTalk(
        0x8,
        (
            "#04100F特别任务支援科的各位，\x01",
            "瓦吉就暂时交托给你们了。\x02\x03",

            "瓦吉，你不用担心我们，\x01",
            "努力做好现在的工作就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x105,
        "#12P#10304F呵呵，我本来就是这个打算。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    #C0381
    ChrTalk(
        0x105,
        "#6P#10304F就是这样，今后也请大家多多关照⊥\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0382
    ChrTalk(
        0x101,
        (
            "#11P#00006F嗯……虽然今后可能会\x01",
            "增添不少麻烦……\x02\x03",

            "#00000F但我们非常\x01",
            "欢迎你的加入。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x138, 2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrPos(0x8, -4720, 0, 11880, 180)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    SetChrPos(0xA, 3200, 0, 7580, 270)
    SetChrPos(0xB, 16149, 0, 12020, 270)
    SetChrPos(0xC, -1090, 0, 14910, 180)
    EventEnd(0x5)
    Return()

    # Function_33_5CAC end

    def Function_34_6A87(): pass

    label("Function_34_6A87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(210, 900, 6100, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27360, 0)
    SetChrPos(0x0, 0, 0, -500, 0)
    SetChrPos(0x1, 0, 0, -500, 0)
    SetChrPos(0x2, 0, 0, -500, 0)
    SetChrPos(0x3, 0, 0, -500, 0)
    SetChrPos(0x4, 0, 0, -500, 0)
    SetChrPos(0x5, 0, 0, -500, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_6B8C():
        OP_96(0xFE, 0x384, 0x0, 0x141E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B8C)

    def lambda_6BA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6BA6)
    Sleep(400)

    def lambda_6BBA():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0x10FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BBA)

    def lambda_6BD4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BD4)
    Sleep(400)

    def lambda_6BE8():
        OP_96(0xFE, 0x4BA, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BE8)

    def lambda_6C02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C02)
    Sleep(400)

    def lambda_6C16():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xBE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C16)

    def lambda_6C30():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6C30)
    Sleep(400)

    def lambda_6C44():
        OP_96(0xFE, 0x3E8, 0x0, 0x794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C44)

    def lambda_6C5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6C5E)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CAF")

    def lambda_6C84():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_6C84)

    def lambda_6C9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6C9E)
    Jump("loc_6CDA")

    label("loc_6CAF")


    def lambda_6CB4():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_6CB4)

    def lambda_6CCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6CCE)

    label("loc_6CDA")

    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)

    #C0383
    ChrTalk(
        0x105,
        (
            "#12P#10405F哎呀，好像\x01",
            "来了稀客呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6DC9():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6DC9)

    def lambda_6DD6():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6DD6)

    def lambda_6DE3():
        TurnDirection(0x9, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6DE3)

    def lambda_6DF0():
        TurnDirection(0x15, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6DF0)

    def lambda_6DFD():
        TurnDirection(0x16, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6DFD)
    TurnDirection(0x17, 0x105, 500)

    #C0384
    ChrTalk(
        0x17,
        "#5P你、你是……！！\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xA,
        (
            "#11P瓦、瓦吉……！？\x01",
            "还有支援科的人！！\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#00005F圣书会和剑蛇帮……\x01",
            "都聚在这里了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x16,
        (
            "#5P嗯、嗯……\x01",
            "市里现在变成这样，\x01",
            "我们准备讨论一下今后的对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x15,
        (
            "#5P话说回来……\x01",
            "瓦吉这家伙怎么穿着\x01",
            "那种奇怪的衣服～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x9,
        (
            "#11P对、对了……\x01",
            "阿巴斯没和你在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x105,
        (
            "#12P#10406F哎呀呀，好不容易才回来，\x01",
            "真是连口气都不让人喘啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x104,
        (
            "#12P#00300F哈哈，对他们来说，\x01",
            "冲击力实在太大了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x103,
        (
            "#6P#00203F还是把事情经过\x01",
            "告诉他们为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x105,
        (
            "#12P#10403F不过，如果突然说起骑士团、教会\x01",
            "之类的事情，只会让他们更加混乱，\x01",
            "而且说来就话长了。\x02\x03",

            "#10400F我稍后再向你们说明具体情况。\x01",
            "……可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xA,
        (
            "#11P嗯、嗯……也好，\x01",
            "现在应该集中精力，处理眼前的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x105,
        (
            "#12P#10402F呵呵，话说回来……\x01",
            "我和阿巴斯不在的时候，\x01",
            "你们似乎把家看得很好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x9,
        "#11P那、那当然了。\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "#11P瓦吉和阿巴斯\x01",
            "答应过我们，\x01",
            "一定会回来的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x9,
        (
            "#11P既、既然如此，\x01",
            "我们也只能拼命努力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x17,
        (
            "#5P哼，我们\x01",
            "可不是在\x01",
            "帮瓦吉看家。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x17,
        (
            "#5P虽然发生了那种事……\x01",
            "但我们还是想好好守护\x01",
            "瓦鲁多大哥的归处。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x16,
        (
            "#5P嗯，旧城区对我们\x01",
            "剑蛇帮来说，\x01",
            "也是很重要的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x16,
        (
            "#5P虽然杰德前辈他们\x01",
            "还没有心情\x01",
            "来帮忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x105,
        "#12P#10404F是吗……谢谢你们。\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵，你很\x01",
            "了不起呢，迪诺。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x17)
    TurnDirection(0x17, 0x102, 500)

    #C0405
    ChrTalk(
        0x17,
        "#5P没、没什么啦……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x17, 500)

    #C0406
    ChrTalk(
        0x15,
        (
            "#5P哈哈，迪诺，\x01",
            "你害什么羞啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7399")

    #C0407
    ChrTalk(
        0x10A,
        (
            "#12P#00603F总之，总统操纵的\x01",
            "怪物似乎并没有出现在\x01",
            "旧城区……\x02\x03",

            "#00600F把这里交给他们，\x01",
            "应该没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#6P#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_74AC")

    label("loc_7399")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_741C")

    #C0409
    ChrTalk(
        0x109,
        (
            "#N#12P#10103F总之，总统操纵的\x01",
            "怪物似乎并没有出现在\x01",
            "旧城区……\x02\x03",

            "#10100F把这里交给他们，\x01",
            "应该不会有问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_7492")

    label("loc_741C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7492")

    #C0410
    ChrTalk(
        0x106,
        (
            "#N#12P#10703F总之，敌方操纵的\x01",
            "怪物似乎并没有出现在\x01",
            "旧城区……\x02\x03",

            "#10702F把这里交给他们\x01",
            "应该无妨。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_7492")


    #C0411
    ChrTalk(
        0x101,
        "#6P#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_74AC")

    TurnDirection(0x17, 0x105, 500)

    #C0412
    ChrTalk(
        0x105,
        (
            "#12P#10404F事情就是这样，\x01",
            "我们这就要走了。\x02\x03",

            "#10400F在这段时间，这里就拜托\x01",
            "你们留守了，没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x105, 500)

    #C0413
    ChrTalk(
        0xA,
        "#11P嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x9,
        "#11P小心点啊，瓦吉！\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x15,
        (
            "#5P虽然还不太明白，\x01",
            "不过就大干一场吧～！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, 6160, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x10000000)
    OP_93(0x15, 0x5A, 0x0)
    OP_93(0x17, 0x5A, 0x0)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    ClearChrFlags(0x15, 0x10)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x17, 0xFF)
    SetScenarioFlags(0x1BE, 2)
    EventEnd(0x5)
    Return()

    # Function_34_6A87 end

    SaveToFile()

Try(main)
