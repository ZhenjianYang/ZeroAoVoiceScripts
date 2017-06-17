from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アッバス",               # 1
        "リャン",                 # 2
        "キーンツ",               # 3
        "ベッセ",                 # 4
        "アゼル",                 # 5
        "アシュリー",             # 6
        "サリナ",                 # 7
        "ユゴット",               # 8
        "市民",                   # 9
        "市民",                   # 10
        "金髪の青年",             # 11
        "市民",                   # 12
        "市民",                   # 13
        "ルガノフ",               # 14
        "コウキ",                 # 15
        "ディーノ",               # 16
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
        "Function_7_1BA4",         # 07, 7
        "Function_8_20BA",         # 08, 8
        "Function_9_21FF",         # 09, 9
        "Function_10_23A4",        # 0A, 10
        "Function_11_33FD",        # 0B, 11
        "Function_12_3513",        # 0C, 12
        "Function_13_35F4",        # 0D, 13
        "Function_14_4553",        # 0E, 14
        "Function_15_4572",        # 0F, 15
        "Function_16_4735",        # 10, 16
        "Function_17_5425",        # 11, 17
        "Function_18_5429",        # 12, 18
        "Function_19_6089",        # 13, 19
        "Function_20_61C5",        # 14, 20
        "Function_21_62BF",        # 15, 21
        "Function_22_62C9",        # 16, 22
        "Function_23_641A",        # 17, 23
        "Function_24_6552",        # 18, 24
        "Function_25_66AD",        # 19, 25
        "Function_26_677C",        # 1A, 26
        "Function_27_6863",        # 1B, 27
        "Function_28_68CD",        # 1C, 28
        "Function_29_69E5",        # 1D, 29
        "Function_30_6ABC",        # 1E, 30
        "Function_31_6B8E",        # 1F, 31
        "Function_32_6CB1",        # 20, 32
        "Function_33_6D82",        # 21, 33
        "Function_34_7CD7",        # 22, 34
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
    Jump("loc_1BA0")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C25")
    Jump("loc_C37")

    label("loc_C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    Jump("loc_C37")

    label("loc_C37")

    Jump("loc_1BA0")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    Call(0, 7)
    Jump("loc_CCA")

    label("loc_C57")


    #C0001
    ChrTalk(
        0x8,
        (
            "#04100Fヴァルドのことに関しては\x01",
            "引き続き調査するつもりだ。\x02\x03",

            "何か分かったらすぐに\x01",
            "連絡するから待っていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCA")

    Jump("loc_1BA0")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEA")
    Call(0, 8)
    Jump("loc_D20")

    label("loc_CEA")


    #C0002
    ChrTalk(
        0x8,
        (
            "#04100Fヴァルドに関する情報収集は\x01",
            "我らに任せろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D20")

    Jump("loc_1BA0")

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D85")

    #C0003
    ChrTalk(
        0x8,
        (
            "#04100F……どうやら、\x01",
            "急ぎの仕事のようだな。\x02\x03",

            "何か用があれば、いつでも言え。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA0")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDB")

    #C0004
    ChrTalk(
        0x8,
        (
            "#04100Fバイパーの連中が\x01",
            "ヴァルド探しを始めたようだな。\x02\x03",

            "どうやらここ数日、一切\x01",
            "姿を見かけなくなったらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00301F一切、か……\x01",
            "どこで何をしてんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10301F……アッバスたちも\x01",
            "見かけていないのかい？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)

    #C0007
    ChrTalk(
        0x8,
        (
            "#04100Fああ、この１週間はさっぱりだ。\x02\x03",

            "それ以前は、たまに\x01",
            "見かけることはあったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x105,
        "#10308Fそうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0009
    ChrTalk(
        0x8,
        (
            "#04100F……ワジ、あまり気に病むな。\x02\x03",

            "姿を消したと言っても\x01",
            "たかだか数日だ。\x02\x03",

            "それに、今は他にも\x01",
            "やらねばならない仕事が\x01",
            "あるのだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10304Fああ……そうだね。\x02\x03",

            "#10302Fありがとう、アッバス。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 6)
    Jump("loc_1055")

    label("loc_FDB")

    TurnDirection(0x8, 0x105, 0)

    #C0011
    ChrTalk(
        0x8,
        (
            "#04100Fヴァルドのことは\x01",
            "我らの方でも気に掛けておく。\x02\x03",

            "だからワジ、余計な心配はせず\x01",
            "今の仕事に集中するといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055")

    Jump("loc_1BA0")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1075")
    Call(0, 9)
    Jump("loc_117C")

    label("loc_1075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112C")
    TurnDirection(0x8, 0x105, 0)

    #C0012
    ChrTalk(
        0x8,
        (
            "#04100Fワジ……来ていたのか。\x02\x03",

            "店で寛#2Rくつろ#ぎたい時はいつでも言え。\x01",
            "すぐに席を用意するからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、\x01",
            "ありがとう、アッバス。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_117C")

    label("loc_112C")


    #C0014
    ChrTalk(
        0x8,
        (
            "#04100F店で寛#2Rくつろ#ぎたい時はいつでも言え。\x01",
            "すぐに席を用意するからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117C")

    Jump("loc_1BA0")

    label("loc_1181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_12B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123C")

    #C0015
    ChrTalk(
        0x8,
        (
            "#04100F……最近の旧市街は比較的平穏だ。\x02\x03",

            "だからワジ、\x01",
            "こちら方面のことは気にせず\x01",
            "支援課の仕事に集中するといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        "#10300Fああ……ありがとう、アッバス。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12B1")

    label("loc_123C")


    #C0017
    ChrTalk(
        0x8,
        (
            "#04100F……最近の旧市街は比較的平穏だ。\x02\x03",

            "だからワジ、\x01",
            "こちら方面のことは気にせず\x01",
            "支援課の仕事に集中するといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B1")

    Jump("loc_1BA0")

    label("loc_12B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AA")

    #C0018
    ChrTalk(
        0x8,
        (
            "#04105Fあの客、もしや……\x02\x03",

            "#04102F……フッ、まさかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00005F（わ、笑った……？）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#00305F（ああ、意外だな……）\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        (
            "#10306F（やれやれ……\x01",
            "  フフ、君たちアッバスを\x01",
            "  何だと思ってるんだい？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13DE")

    label("loc_13AA")


    #C0022
    ChrTalk(
        0x8,
        (
            "#04102Fあの客、もしや……\x01",
            "……フッ、まさかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DE")

    Jump("loc_15CC")

    label("loc_13E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1586")

    #C0023
    ChrTalk(
        0x8,
        "#04100F………………………\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        "#10300Fアッバス、考え事かい？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    #C0025
    ChrTalk(
        0x8,
        (
            "#04100Fワジか……\x02\x03",

            "……ああ、世の中には\x01",
            "色々な者がいると思ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10309Fハハ、確かにね。\x02\x03",

            "#10304Fでも、それを言うなら\x01",
            "僕たちもだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "#04102Fフッ……違いない。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00000F（この人……\x01",
            "  ワジとは結構しゃべるんだよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00100F（ふふ、それだけ\x01",
            "  仲が良いって事なんでしょうね。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_15CC")

    label("loc_1586")


    #C0030
    ChrTalk(
        0x8,
        (
            "#04100F………………………\x02\x03",

            "……世の中には\x01",
            "色々な者がいるものだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    Jump("loc_1BA0")

    label("loc_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A1")

    #C0031
    ChrTalk(
        0x8,
        (
            "#04100Fこの旧市街にも、警官が何名か\x01",
            "巡回に来ているようだな。\x02\x03",

            "ワジ、支援課の仕事は滞りないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x105,
        (
            "#10300Fああ、今のところ\x01",
            "特に問題はないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "#04100Fそうか、ならいい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F1")

    label("loc_16A1")


    #C0034
    ChrTalk(
        0x8,
        (
            "#04100Fこの旧市街にも警官が\x01",
            "巡回に来ているようだな。\x02\x03",

            "……ご苦労なことだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F1")

    Jump("loc_1BA0")

    label("loc_16F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_1870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182C")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    #C0035
    ChrTalk(
        0x8,
        (
            "#04100Fワジ、大丈夫か？\x01",
            "少し顔色が悪いようだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10300Fああ、大丈夫さ。\x01",
            "心配はいらないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        "#04100F……そうか、分かった。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10106F（この２人……\x01",
            "  妙にアッサリしてますよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00100F（ええ、でも不思議と\x01",
            "  通じ合っているのよね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_186B")

    label("loc_182C")

    TurnDirection(0x8, 0x105, 0)

    #C0040
    ChrTalk(
        0x8,
        (
            "#04100Fワジ、我らの助けが\x01",
            "必要な時はいつでも言え。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186B")

    Jump("loc_1BA0")

    label("loc_1870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_196C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191B")

    #C0041
    ChrTalk(
        0x8,
        (
            "#04100F注文ならこちらでも\x01",
            "受け付けている。\x02\x03",

            "いつでも気軽に頼むといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#00003F（この人相手に気軽、か……\x01",
            "  何気に難しいことだよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1967")

    label("loc_191B")


    #C0043
    ChrTalk(
        0x8,
        (
            "#04100F注文ならこちらでも\x01",
            "受け付けている。\x02\x03",

            "いつでも気軽に頼むといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1967")

    Jump("loc_1BA0")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B37")

    #C0044
    ChrTalk(
        0x8,
        (
            "#04100Fワジ、テスタメンツのことは\x01",
            "こちらに全て任せておけ。\x02\x03",

            "お前はお前の\x01",
            "やりたいようにやるがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10300Fああ、そうさせてもらうよ。\x02\x03",

            "#10304Fこれからトリニティにも\x01",
            "ときどき顔を出すと思うけど、\x01",
            "店の経営のほうも頑張るといい。\x02\x03",

            "#10302Fフフ、潰れちゃったりしたら\x01",
            "居心地のいい場所が減っちゃうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#04102Fうむ、心得た。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#00003F（この２人って不思議な関係だよな……）\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x109,
        "#10100F（どういう過去があるんでしょうね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA0")

    label("loc_1B37")


    #C0049
    ChrTalk(
        0x8,
        (
            "#04100Fワジ、テスタメンツのことは\x01",
            "こちらに全て任せておけ。\x02\x03",

            "お前はお前の\x01",
            "やりたいようにやるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA0")

    TalkEnd(0xFE)
    Return()

    # Function_6_BF9 end

    def Function_7_1BA4(): pass

    label("Function_7_1BA4")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBD")
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
            "#04100Fワジ……\x01",
            "どうやら色々と大変な事に\x01",
            "なっているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "実は今朝、俺とベッセの２人で\x01",
            "あの赤毛の彼を見かけたんだ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CF9")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x109,
        (
            "#10108Fやっぱり……\x01",
            "旧市街に来ていたんですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF9")


    #C0053
    ChrTalk(
        0xB,
        (
            "何というか……\x01",
            "お、思いつめたような表情だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "交換屋の近くで見かけたと\x01",
            "思ったら、す、すぐに\x01",
            "街の方に消えて行ったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        "な、何かあったのか……？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10303Fああ、ちょっとね。\x02\x03",

            "#10300Fでも、これは\x01",
            "あくまで支援課内の話だ。\x01",
            "みんなの心配には及ばないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#04100F……そうか。\x02\x03",

            "だが、我らの手が必要な時は\x01",
            "いつでも言えよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x105,
        "#10300Fああ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00001F（ランディ……待ってろよ。\x01",
            "  絶対に捕まえてやるからな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 2)
    Jump("loc_2098")

    label("loc_1EBD")


    #C0060
    ChrTalk(
        0x105,
        (
            "#10300Fそういえばアッバス……\x01",
            "ヴァルド関連の情報は集まったかい？\x02",
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
            "#04100Fいや……\x01",
            "今の所、有力な情報は\x01",
            "ほとんど得られていない。\x02\x03",

            "おそらく人目を避けるように\x01",
            "行動していたためか、\x01",
            "目撃情報もほとんどなくてな。\x02\x03",

            "薬の入手ルートを掴むのは\x01",
            "正直、かなり難しいだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        "#10303F……そうか。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#04100Fまあ、それでも\x01",
            "調査は引き続き行うつもりだ。\x02\x03",

            "何か分かったらすぐに\x01",
            "連絡するから待っていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        "#10300Fああ、了解したよ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x16E, 1)

    label("loc_2098")

    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    Return()

    # Function_7_1BA4 end

    def Function_8_20BA(): pass

    label("Function_8_20BA")

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
            "#04100Fワジか……\x01",
            "ヴァルドに関する情報収集は\x01",
            "こちらに任せろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "だ、段取りが整ったら\x01",
            "すぐに聞き込みに行くからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "だからワジ、君は\x01",
            "支援課の仕事に集中してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x105,
        "#10300Fありがとう、よろしく頼んだよ。\x02",
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

    # Function_8_20BA end

    def Function_9_21FF(): pass

    label("Function_9_21FF")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0069
    ChrTalk(
        0xD,
        (
            "この店、最近なかなか\x01",
            "繁盛してるらしいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xD,
        (
            "羨ましいねえ……ぜひとも\x01",
            "景気を分けてもらいたいもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#04102Fフッ、そちらも決して\x01",
            "景気が悪いわけではないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        "はは、まあ否定はしないけどね。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#00000F（２人とも、何だか楽しそうだな。）\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、変わり者同士、\x01",
            "  波長が合うって感じかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#00211F（……それを言うなら\x01",
            "  ワジさんもだと思いますが。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x10)
    Return()

    # Function_9_21FF end

    def Function_10_23A4(): pass

    label("Function_10_23A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2470")

    #C0076
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院のほうに、\x01",
            "かなりの患者が\x01",
            "押し寄せてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "親父に一応連絡をいれたが、\x01",
            "忙しいながらもなんとか\x01",
            "回しているようだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        "……僕も頑張らなくちゃな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24CF")

    label("loc_2470")


    #C0079
    ChrTalk(
        0xFE,
        (
            "まだ、将来僕が親父のような\x01",
            "道を進むかはわからないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "……僕も頑張らなくちゃな。\x02",
    )

    CloseMessageWindow()

    label("loc_24CF")

    Jump("loc_33F9")

    label("loc_24D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_25C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2567")

    #C0081
    ChrTalk(
        0xFE,
        (
            "一番に考えなきゃならないのは\x01",
            "近隣住民の安全だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "万が一の為にも、\x01",
            "東通り方面の様子は\x01",
            "見張っていた方がいいと思う。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BF")

    label("loc_2567")


    #C0083
    ChrTalk(
        0xFE,
        (
            "こっちは僕たちで\x01",
            "なんとかやってみる。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "君たちも何とか無事に\x01",
            "帰ってきてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BF")

    Jump("loc_33F9")

    label("loc_25C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2809")

    #C0085
    ChrTalk(
        0xFE,
        (
            "今朝、アッバスがみんなを集めて\x01",
            "『当分の間、トリニティを任せた』\x01",
            "とだけ言ってどこかに出かけたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "行き先も言わなかったけど、\x01",
            "何かあったんだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#00005Fアッバスが……？\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#00105Fもしかして、\x01",
            "ワジ君と一緒なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "……それは分からない。\x01",
            "国防軍なんてやつらも\x01",
            "街でうろうろしてるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "も、もしかして逮捕されたのか……？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#00201Fワジさんたちがそんなヘマを\x01",
            "するとも思えませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#00303Fふむ……\x01",
            "まあ、とにかく落ち着いたほうが。\x01",
            "いいんじゃねーか？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "……そうだな。\x01",
            "とにかく俺たちは店を守らないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28A0")

    label("loc_2809")


    #C0094
    ChrTalk(
        0xFE,
        (
            "ワジやアッバスも心配だけど……\x01",
            "……ウルスラ病院にいる親父は\x01",
            "大丈夫かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "親父のことだから、こんな状況でも\x01",
            "患者の対応にあたってそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A0")

    Jump("loc_33F9")

    label("loc_28A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28B3")
    Jump("loc_33F9")

    label("loc_28B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_296A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CE")
    Call(0, 7)
    Jump("loc_2965")

    label("loc_28CE")


    #C0096
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "あの赤毛の彼、雨だっていうのに\x01",
            "凄い量の荷物を抱えていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "見た感じでも相当な重さだろうに、\x01",
            "機敏に動いていたから驚いたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2965")

    Jump("loc_33F9")

    label("loc_296A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2985")
    Call(0, 8)
    Jump("loc_2A61")

    label("loc_2985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A24")

    #C0098
    ChrTalk(
        0xFE,
        (
            "そういえば昨日は\x01",
            "西クロスベル街道で脱線事故が\x01",
            "起こったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "何人か重傷者も出たらしいが……\x01",
            "親父も相当忙しくしているみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A61")

    label("loc_2A24")


    #C0100
    ChrTalk(
        0xFE,
        (
            "親父は凄いよな……\x01",
            "こういう時、誰からも頼りにされて……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A61")

    Jump("loc_33F9")

    label("loc_2A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE6")

    #C0101
    ChrTalk(
        0xFE,
        "僕……僕は一体何になりたいんだ？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……くそっ、やはり幾ら\x01",
            "考えても答えが出るものじゃないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B5C")

    label("loc_2AE6")


    #C0103
    ChrTalk(
        0xFE,
        (
            "今思うと、勉強自体はそこまで\x01",
            "嫌いではなかったんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "また机に向かったら\x01",
            "何か見えたりするのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5C")

    Jump("loc_33F9")

    label("loc_2B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C84")

    #C0105
    ChrTalk(
        0xFE,
        (
            "小さい頃は親父のような\x01",
            "医者になりたいって、\x01",
            "そう思ってたんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "でもいつからか、自分は親父ほど\x01",
            "優秀じゃないことに気が付いて……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "……って、\x01",
            "僕は何を口に出してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "はあ……いつまでも\x01",
            "こんな風にウジウジしてるから\x01",
            "僕は中途半端なんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CFE")

    label("loc_2C84")


    #C0109
    ChrTalk(
        0xFE,
        (
            "というか、ウェイターが\x01",
            "ウジウジしていちゃマズイよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "給料だって出ているんだし、\x01",
            "仕事は真面目にこなさないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFE")

    Jump("loc_33F9")

    label("loc_2D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBB")

    #C0111
    ChrTalk(
        0xFE,
        (
            "なんていうか……\x01",
            "最近、みんな生き生きしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "中途半端な気持ちで\x01",
            "働いてるのは僕だけというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "僕は一体何をしているんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#00005F（ワジ……\x01",
            "  声を掛けてやらないのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        (
            "#10304F（ああ、昔からテスタメンツは\x01",
            "  皆の自主性に任せているからね。）\x02\x03",

            "#10300F（僕からわざわざ余計な\x01",
            "  口出しはしないようにしてるんだ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            "#00211F（……何だか、\x01",
            "  セルゲイ課長みたいですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F33")

    label("loc_2EBB")


    #C0117
    ChrTalk(
        0xFE,
        (
            "最近、みんな生き生きしているんだ。\x01",
            "中途半端なのは僕だけというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "僕は一体何をしているんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F33")

    Jump("loc_33F9")

    label("loc_2F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_308A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303D")

    #C0119
    ChrTalk(
        0xFE,
        (
            "今朝、バイパーの連中が\x01",
            "肩をぶつけて来て\x01",
            "因縁をふっかけて来たんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "こちらから素直に謝ったら\x01",
            "ヤツら、バツが悪そうに\x01",
            "大人しく引いていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "アッバスから聞いていた\x01",
            "対処法だったんだが、\x01",
            "本当に効果があるものなんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3085")

    label("loc_303D")


    #C0122
    ChrTalk(
        0xFE,
        (
            "これが平和的対処法か……\x01",
            "アッバスから学ぶべきことは\x01",
            "本当に多いよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3085")

    Jump("loc_33F9")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3118")

    #C0123
    ChrTalk(
        0xFE,
        "す、すごいな、あの金髪の客……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "急に弾き語りを披露したと思ったら\x01",
            "今度はビリヤードで僕たちを\x01",
            "滅多斬りとは……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F6")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AE")

    #C0125
    ChrTalk(
        0xFE,
        (
            "な、何だか外の方が\x01",
            "少し騒がしかったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "もしかしてさっきの客が……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……まあいい、\x01",
            "気にしない方が良さそうだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31F6")

    label("loc_31AE")


    #C0128
    ChrTalk(
        0xFE,
        "もしかしてさっきの客が……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "……まあいい、気にしないでおこう。\x02",
    )

    CloseMessageWindow()

    label("loc_31F6")

    Jump("loc_33F9")

    label("loc_31FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_323D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3216")
    Call(0, 11)
    Jump("loc_3238")

    label("loc_3216")


    #C0130
    ChrTalk(
        0xFE,
        "ではお客様、こちらへどうぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_3238")

    Jump("loc_33F9")

    label("loc_323D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32BF")

    #C0131
    ChrTalk(
        0xFE,
        (
            "ふう、雨の日は\x01",
            "どうにも気分が沈んでしまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "ジメジメするし、髪は跳ねるし……\x01",
            "早く止んで欲しいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F9")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3392")

    #C0133
    ChrTalk(
        0xFE,
        "僕は別に接客向きじゃないんだが……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "他に役どころもなかったから、\x01",
            "仕方なくウェイターを引き受けたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "まあそれでも、引き受けた以上は\x01",
            "責任を持って取り組むつもりだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33F9")

    label("loc_3392")


    #C0136
    ChrTalk(
        0xFE,
        (
            "いらっしゃい、席に着きたかったら\x01",
            "案内するから言ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "これでも一応ウェイターなのでね。\x02",
    )

    CloseMessageWindow()

    label("loc_33F9")

    TalkEnd(0xFE)
    Return()

    # Function_10_23A4 end

    def Function_11_33FD(): pass

    label("Function_11_33FD")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0138
    ChrTalk(
        0xA,
        "えっと、お客様は２名様ですね。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "カウンター席とテーブル席が\x01",
            "ございますが、どちらにしますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x10,
        (
            "そうだな……\x01",
            "それじゃせっかくだし、\x01",
            "カウンター席にしようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x11,
        "うん、そうしましょ。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "かしこまりました。\x01",
            "それではご案内します。\x02",
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

    # Function_11_33FD end

    def Function_12_3513(): pass

    label("Function_12_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35EA")
    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3533")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3591")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B1")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35E1")

    label("loc_35B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35C5")
    Jump("loc_35E1")

    label("loc_35C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_35E1")

    Jump("loc_3533")

    label("loc_35E6")

    TalkEnd(0xB)
    Return()

    label("loc_35EA")

    TalkBegin(0xB)
    Call(0, 13)
    TalkEnd(0xB)
    Return()

    # Function_12_3513 end

    def Function_13_35F4(): pass

    label("Function_13_35F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D7")

    #C0143
    ChrTalk(
        0xB,
        (
            "それにしても……お、驚いたぞ。\x01",
            "ワジとアッバスが教会の関係者だとは。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3788")

    #C0144
    ChrTalk(
        0xB,
        (
            "な、なんだか急に遠い存在のような\x01",
            "気がしてしまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x105,
        (
            "#10402Fフフ、まあ本質は変わらないし\x01",
            "いつもどおり接してくれると嬉しいよ。\x02\x03",

            "#10404F君たちと《テスタメンツ》をやってきた\x01",
            "ワジ・ヘミスフィアこそが、\x01",
            "本当の僕と言ってもいいくらいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "そ、そうか……\x01",
            "そう言ってくれると、嬉しい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CF")

    label("loc_3788")


    #C0147
    ChrTalk(
        0xB,
        (
            "今までそんな素振り無かったし、\x01",
            "しょ、正直いまでも信じられないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CF")

    SetScenarioFlags(0x0, 3)
    Jump("loc_384F")

    label("loc_37D7")


    #C0148
    ChrTalk(
        0xB,
        (
            "ワ、ワジとアッバスが\x01",
            "教会の関係者だとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "今までそんな素振り無かったし、\x01",
            "しょ、正直いまでも信じられないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384F")

    Jump("loc_4552")

    label("loc_3854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E7")

    #C0150
    ChrTalk(
        0xB,
        (
            "さ、さすがにあの化物を\x01",
            "相手にするのは\x01",
            "やめておいた方がいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "い、今は襲ってこないんだし、\x01",
            "触らぬ神に祟りなしだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3944")

    label("loc_38E7")


    #C0152
    ChrTalk(
        0xB,
        (
            "アゼルは、ひ、東通りにいる\x01",
            "家族の元に一旦帰ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        "あ、あっちも無事だといいが。\x02",
    )

    CloseMessageWindow()

    label("loc_3944")

    Jump("loc_4552")

    label("loc_3949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_39C5")

    #C0154
    ChrTalk(
        0xB,
        (
            "アッバスにも……\x01",
            "な、何か事情があるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "今は言いつけどおり、\x01",
            "し、しっかりと店を守らないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4552")

    label("loc_39C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_39D3")
    Jump("loc_4552")

    label("loc_39D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EE")
    Call(0, 7)
    Jump("loc_3A77")

    label("loc_39EE")


    #C0156
    ChrTalk(
        0xB,
        (
            "あ、あいつの表情……\x01",
            "何というか、凄い迫力だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "お、思いつめてるというか\x01",
            "鬼気迫るというか……\x01",
            "正直、かなりびびってしまった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A77")

    Jump("loc_4552")

    label("loc_3A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A97")
    Call(0, 8)
    Jump("loc_3B15")

    label("loc_3A97")


    #C0158
    ChrTalk(
        0xB,
        (
            "こ、これからオレたちで\x01",
            "色々と聞き込んで回る予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "グ、グノーシスとやらの出所を\x01",
            "突き止められるといいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B15")

    Jump("loc_4552")

    label("loc_3B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C93")

    #C0160
    ChrTalk(
        0xB,
        "カ、カクテルは爆発だ。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "お、思い切った発想が\x01",
            "画期的な発明を生み出すんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "だが……少々\x01",
            "思い切り過ぎたのかもしれない。\x01",
            "……オレには才能がなかったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "というわけで……\x01",
            "カ、カクテル作りはもう止めだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "オレの最後の作品……\x01",
            "ど、どこかに処分してきてくれ。\x02",
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
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D7, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 5)
    Jump("loc_3CDD")

    label("loc_3C93")


    #C0166
    ChrTalk(
        0xB,
        "カ、カクテル作りはもう止めだ。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xB,
        "……人殺しになりたくないからな。\x02",
    )

    CloseMessageWindow()

    label("loc_3CDD")

    Jump("loc_4552")

    label("loc_3CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E53")

    #C0168
    ChrTalk(
        0xB,
        (
            "オレのカクテル、\x01",
            "ア、アシュリーさんに大量に\x01",
            "買ってもらえたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "あ、味や見た目はともかく、\x01",
            "戦場で使えるって褒められたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        "ん……？　ほ、褒められたのか？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "と、とにかく……\x01",
            "オレのカクテルは\x01",
            "アシュリーさんのお墨付きだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        "よ、よかったら持って行け。\x02",
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
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 4)
    Jump("loc_3ED1")

    label("loc_3E53")


    #C0174
    ChrTalk(
        0xB,
        (
            "オレのカクテルは戦場で使える……\x01",
            "つ、つまりそれだけ栄養満点ってことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "匂いはアレだが……\x01",
            "グ、グイッといってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED1")

    Jump("loc_4552")

    label("loc_3ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4068")

    #C0176
    ChrTalk(
        0xB,
        (
            "ア、アゼルとリャン、\x01",
            "いつも２人で楽しそうに\x01",
            "カクテルの研究をしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "だ、だからオレも\x01",
            "試しに作ることにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "ふ、２人からは見た目が悪いから\x01",
            "店には置けないと言われたが……\x01",
            "成分が身体に良いのは間違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        "よ、よければ持って行ってくれ。\x02",
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
            "を貰った。\x02",
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
        "#00005Fあ、ああ……ありがとう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 3)
    Jump("loc_40ED")

    label("loc_4068")


    #C0182
    ChrTalk(
        0xB,
        (
            "オレのカクテルは\x01",
            "素材に絶対の自信があるんだ。\x01",
            "か、身体にいいのは間違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "見た目はアレだが……\x01",
            "ゴ、ゴクッといってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40ED")

    Jump("loc_4552")

    label("loc_40F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4213")

    #C0184
    ChrTalk(
        0xB,
        (
            "け、今朝はキーンツと一緒に\x01",
            "仕入れに出かけたんだが、\x01",
            "バイパーと出くわしてしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "思わずキレそうに\x01",
            "なってしまったんだが、\x01",
            "キーンツに止められたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xB,
        (
            "まさか、あんな方法でバイパーが\x01",
            "引き下がるとは思わなかったが……\x01",
            "こ、これは発見かもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4281")

    label("loc_4213")


    #C0187
    ChrTalk(
        0xB,
        (
            "オレたちはも、もう、\x01",
            "無駄なケンカはしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "ア、アザなんて作ろうものなら\x01",
            "店にも顔を出せないからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4281")

    Jump("loc_4552")

    label("loc_4286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F3")

    #C0189
    ChrTalk(
        0xB,
        "くそっ、ついにリャンまで……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        (
            "あの金髪白コート……\x01",
            "そ、相当のツワモノだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432C")

    label("loc_42F3")


    #C0191
    ChrTalk(
        0xB,
        (
            "あ、あの金髪白コート、\x01",
            "まるで嵐のような客だったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432C")

    Jump("loc_4552")

    label("loc_4331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43B3")

    #C0192
    ChrTalk(
        0xB,
        (
            "お、おかげ様で\x01",
            "最近は市街から来る客も増えた。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "ただ、治安に不安があるせいか\x01",
            "夜はそれほどでもないんだがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4552")

    label("loc_43B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445E")

    #C0194
    ChrTalk(
        0xB,
        (
            "あ、後がつかえてさえいなければ、\x01",
            "基本ビリヤードはプレイし放題だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "た、ただし、最低でも１ドリンク以上\x01",
            "注文してもらうことが条件だがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44B3")

    label("loc_445E")


    #C0196
    ChrTalk(
        0xB,
        (
            "ビ、ビリヤードは\x01",
            "基本的にプレイし放題だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        "た、ただし、バーの客限定だがな。\x02",
    )

    CloseMessageWindow()

    label("loc_44B3")

    Jump("loc_4552")

    label("loc_44B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4552")

    #C0198
    ChrTalk(
        0xB,
        (
            "オレはビリヤードの\x01",
            "イ、インストラクター兼スコアラーを\x01",
            "担当することになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "た、球の打ち方やルールが\x01",
            "分からなければ、オレに聞け。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4552")

    Return()

    # Function_13_35F4 end

    def Function_14_4553(): pass

    label("Function_14_4553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_456E")
    Call(0, 12)
    Jump("loc_4571")

    label("loc_456E")

    Call(0, 15)

    label("loc_4571")

    Return()

    # Function_14_4553 end

    def Function_15_4572(): pass

    label("Function_15_4572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4654")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CB")

    #C0200
    ChrTalk(
        0x9,
        (
            "ああ、こんな時にワジや\x01",
            "アッバスがいてくれたらな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4650")

    label("loc_45CB")


    #C0201
    ChrTalk(
        0x9,
        (
            "こうしてまたバイパーと\x01",
            "協力する日が来るなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "ま、彼らの実力は\x01",
            "僕らが一番分かってるし、\x01",
            "味方としてはこれ以上ないけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4650")

    TalkEnd(0x9)
    Return()

    label("loc_4654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4671")
    TalkBegin(0x9)
    Call(0, 22)
    TalkEnd(0x9)
    Return()

    label("loc_4671")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_467E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4731")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46DC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_46DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FC")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_472C")

    label("loc_46FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4710")
    Jump("loc_472C")

    label("loc_4710")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_472C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_472C")

    Jump("loc_467E")

    label("loc_4731")

    TalkEnd(0x9)
    Return()

    # Function_15_4572 end

    def Function_16_4735(): pass

    label("Function_16_4735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_486E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4809")

    #C0203
    ChrTalk(
        0x9,
        (
            "アッバスがしばらく\x01",
            "居なくなることは\x01",
            "たまにあるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "今回はいつにも増して\x01",
            "真剣というか深刻な表情を\x01",
            "していた気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "……早く帰ってきてくれると\x01",
            "いいんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4869")

    label("loc_4809")


    #C0206
    ChrTalk(
        0x9,
        (
            "当分の間って、一体\x01",
            "どのくらいなんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "……早く帰ってきてくれると\x01",
            "いいんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4869")

    Jump("loc_5424")

    label("loc_486E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4911")

    #C0208
    ChrTalk(
        0x9,
        (
            "作業を頑張ってくれている\x01",
            "人たちのために、ここで\x01",
            "特製ドリンクを作ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x9,
        (
            "みんなよく飲むからね。\x01",
            "ミキサーもフル稼働状態だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3F")

    label("loc_4911")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ADB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A83")

    #C0210
    ChrTalk(
        0x9,
        (
            "支援課の方で復興作業を\x01",
            "手伝ってくれてるんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "これを持っていってよ。\x01",
            "みんなに振舞ってる\x01",
            "スペシャルドリンクなんだ。\x02",
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
            "を６個手に入れた。\x02",
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
        "#00005Fこんなに貰っていいのか？\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、人数分ってわけだね。\x01",
            "ありがとう、リャン。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        "はは、どういたしまして。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 4)
    Jump("loc_4AD6")

    label("loc_4A83")


    #C0216
    ChrTalk(
        0x9,
        (
            "復興作業を手伝ってくれて\x01",
            "どうもありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x9,
        "ふふ、流石は特務支援課だね。\x02",
    )

    CloseMessageWindow()

    label("loc_4AD6")

    Jump("loc_4B3F")

    label("loc_4ADB")


    #C0218
    ChrTalk(
        0x9,
        (
            "アゼルたちの作った豚汁、\x01",
            "好評だったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x9,
        (
            "何ていうか、炊き出しって\x01",
            "心が温まるよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3F")

    Jump("loc_5424")

    label("loc_4B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C49")

    #C0220
    ChrTalk(
        0x9,
        (
            "今回の占拠事件は、\x01",
            "帝国政府の陰謀かもっていう\x01",
            "話が出ているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "何でも、この事件を口実に\x01",
            "帝国軍のクロスベル駐留を\x01",
            "目論んでいるとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x9,
        (
            "もし、それが本当だとしたら\x01",
            "とてもじゃないけど、\x01",
            "許すことのできない話だよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CDA")

    label("loc_4C49")


    #C0223
    ChrTalk(
        0x9,
        (
            "もし本当に、帝国政府が\x01",
            "政治目的のために、この占拠事件を\x01",
            "引き起こしたのだとしたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        (
            "とてもじゃないけど、\x01",
            "許すことのできない話だよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDA")

    Jump("loc_5424")

    label("loc_4CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D44")

    #C0225
    ChrTalk(
        0x9,
        (
            "ヴァルド……\x01",
            "本当に何をやっているんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        "酒ならまだしも……薬なんて……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_4D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE6")

    #C0227
    ChrTalk(
        0x9,
        (
            "あのお客さんたち、\x01",
            "ウチのスープパスタをかなり\x01",
            "気に入ってくれたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        (
            "ふふ、流石はアッバス秘伝の\x01",
            "特製レシピって所かな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E71")

    label("loc_4DE6")


    #C0229
    ChrTalk(
        0x9,
        (
            "自分の作ったもので\x01",
            "人を笑顔に出来るって\x01",
            "とても素晴らしいことだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x9,
        (
            "料理ってなかなか苦労も多いけど、\x01",
            "全てが報われる気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E71")

    Jump("loc_5424")

    label("loc_4E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FAE")

    #C0231
    ChrTalk(
        0x9,
        (
            "昨日、バイパーのメンバーが\x01",
            "２人でウチに乗り込んで来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        (
            "何ていうか、凄い剣幕だったから\x01",
            "喧嘩でも吹っかけに来たのかと\x01",
            "思ったんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "彼ら、切羽詰った感じで殊勝に\x01",
            "ヴァルドのことを聞いて行ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x9,
        (
            "舎弟をあそこまで心配させてさ。\x01",
            "ヴァルド……何してるんだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5021")

    label("loc_4FAE")


    #C0235
    ChrTalk(
        0x9,
        (
            "前は敵ながら\x01",
            "少しは尊敬できる所も\x01",
            "あると思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x9,
        (
            "今のヴァルドは、\x01",
            "はっきり言ってヘッド失格だね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5021")

    Jump("loc_5424")

    label("loc_5026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50BB")

    #C0237
    ChrTalk(
        0x9,
        (
            "ベッセ、シェイカーに\x01",
            "何か怪しいものを入れていたけど\x01",
            "大丈夫なのかな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x9,
        (
            "相談してくれたら、\x01",
            "アドバイスだって出来るんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_50BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_516E")

    #C0239
    ChrTalk(
        0x9,
        "やあ、いらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x9,
        (
            "今日は旬の良い素材が入ったから\x01",
            "日替わり小鉢がオススメだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x9,
        (
            "ランチメニューもあるから、\x01",
            "興味があれば気軽に頼んでね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51EC")

    label("loc_516E")


    #C0242
    ChrTalk(
        0x9,
        (
            "今日は旬の良い素材が入ったから\x01",
            "日替わり小鉢がオススメだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        (
            "ランチメニューもあるから、\x01",
            "興味があれば気軽に頼んでね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51EC")

    Jump("loc_5424")

    label("loc_51F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_528C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5209")
    Jump("loc_5287")

    label("loc_5209")


    #C0244
    ChrTalk(
        0x9,
        (
            "結局、あの客との勝負は\x01",
            "決着が着かなかったけど……\x01",
            "はっきり言って僕の完敗だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        "世の中、上には上がいるものだね。\x02",
    )

    CloseMessageWindow()

    label("loc_5287")

    Jump("loc_5424")

    label("loc_528C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5308")

    #C0246
    ChrTalk(
        0x9,
        (
            "はは、アゼルのお姉さんも\x01",
            "相変わらず心配性だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        (
            "２人のやり取りを見ていると\x01",
            "何だか微笑ましくなるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_5308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5390")

    #C0248
    ChrTalk(
        0x9,
        (
            "やれやれ……雨の日は\x01",
            "仕入れ１つを取っても大変だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "あちこち泥で汚れちゃったから、\x01",
            "調理前には服を着替えないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_5390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5424")

    #C0250
    ChrTalk(
        0x9,
        (
            "やあ、いらっしゃい。\x01",
            "注文があればいつでも言ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x9,
        (
            "カクテルでもツマミでも、\x01",
            "アッバス直伝の腕前を\x01",
            "存分に披露させてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5424")

    Return()

    # Function_16_4735 end

    def Function_17_5425(): pass

    label("Function_17_5425")

    Call(0, 18)
    Return()

    # Function_17_5425 end

    def Function_18_5429(): pass

    label("Function_18_5429")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B2")

    #C0252
    ChrTalk(
        0xC,
        "《トリニティ》も営業再開したよ。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "こんな状況になってしまったけど、\x01",
            "普段どおりの日常を過ごすことも\x01",
            "大切には違いないしね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5566")

    #C0254
    ChrTalk(
        0x105,
        (
            "#10400Fフフ、まあがんばってよ。\x01",
            "こんな時でもお店を楽しみに\x01",
            "してる人はいるだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        (
            "ああ、もちろんだ。\x01",
            "そっちも頑張ってくれ、ワジ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AA")

    label("loc_5566")


    #C0256
    ChrTalk(
        0xC,
        (
            "姉さんやユゴットも\x01",
            "応援してくれてるし、\x01",
            "しっかりやんないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55AA")

    SetScenarioFlags(0x0, 5)
    Jump("loc_562D")

    label("loc_55B2")


    #C0257
    ChrTalk(
        0xC,
        (
            "《トリニティ》も営業再開だ。\x01",
            "気軽に注文してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "姉さんやユゴットも\x01",
            "応援してくれてるし、\x01",
            "しっかりやんないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562D")

    Jump("loc_6085")

    label("loc_5632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5640")
    Jump("loc_6085")

    label("loc_5640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_56DD")

    #C0259
    ChrTalk(
        0xC,
        (
            "街のほうで騒がれてた、\x01",
            "独立宣言がどうっていうのも\x01",
            "なんだか気になるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "……姉さんとユゴットの様子を見に\x01",
            "一旦家に帰っておこうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_56DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_56EB")
    Jump("loc_6085")

    label("loc_56EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_581F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A1")

    #C0261
    ChrTalk(
        0xC,
        (
            "マインツを襲った謎の部隊は\x01",
            "恐ろしく手強いらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "警備隊も、かなり\x01",
            "苦戦しているらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "……とにかく、\x01",
            "早く事態が収まって欲しいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_581A")

    label("loc_57A1")


    #C0264
    ChrTalk(
        0xC,
        (
            "こういう時って、\x01",
            "何故か分からないけど\x01",
            "家族のことが心配になるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        (
            "後でちょっと\x01",
            "家の様子を見に行くかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581A")

    Jump("loc_6085")

    label("loc_581F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58AB")

    #C0266
    ChrTalk(
        0xC,
        (
            "ヴァルドがあのディーノって新米と\x01",
            "同じ薬を飲んでいたかもしれない……か。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "敵対していたチームながら、\x01",
            "流石に心配だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_58AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5972")

    #C0268
    ChrTalk(
        0xC,
        "ふう、もう昼過ぎか。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xC,
        (
            "そういえば姉さん、\x01",
            "今日も仕事って言ってたけど、\x01",
            "また無理していないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "俺が働く分、\x01",
            "仕事を減らしていいって\x01",
            "言ってるんだけどな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A04")

    label("loc_5972")


    #C0271
    ChrTalk(
        0xC,
        (
            "そういえば姉さん、\x01",
            "今日も仕事って言ってたけど、\x01",
            "また無理していないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "俺が働く分、\x01",
            "仕事を減らしていいって\x01",
            "言ってるんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A04")

    Jump("loc_6085")

    label("loc_5A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B0B")

    #C0273
    ChrTalk(
        0xC,
        (
            "キーンツの奴、\x01",
            "最近ずっと将来のことについて\x01",
            "悩んでいるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "あいつは頭がいいし、\x01",
            "それに実家も金持ちだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "その気になれば、何にでも\x01",
            "なれると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "何ていうか……\x01",
            "悩みって人それぞれだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BC1")

    label("loc_5B0B")


    #C0277
    ChrTalk(
        0xC,
        (
            "そういえば昔、キーンツの奴、\x01",
            "親父の存在がコンプレックスだって\x01",
            "言ってたことがあったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xC,
        (
            "たとえ頑張って医者になれても\x01",
            "親父を越えられないと、\x01",
            "意味がないとか言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BC1")

    Jump("loc_6085")

    label("loc_5BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C3B")

    #C0279
    ChrTalk(
        0xC,
        (
            "アッバスってあらゆることに\x01",
            "精通してて、知識が豊富なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        "いつも勉強させてもらってるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5CAC")

    #C0281
    ChrTalk(
        0xC,
        "最近、何だか仕事が楽しいんだ。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        (
            "なんかオレ、このままここで\x01",
            "ずっと働いてもいい気がするな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D59")

    #C0283
    ChrTalk(
        0xC,
        (
            "白いコートのお客さんが\x01",
            "急に俺たちとビリヤード対決を\x01",
            "したいって言い出したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "結果、みんな負けちゃって\x01",
            "今は最後の砦のリャンとやってるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB3")

    label("loc_5D59")


    #C0285
    ChrTalk(
        0xC,
        (
            "しかし……\x01",
            "本当に変わった客だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "何ていうか、\x01",
            "誰かに話したくて仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB3")

    Jump("loc_6085")

    label("loc_5DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E26")

    #C0287
    ChrTalk(
        0xC,
        (
            "はあ、姉さんも\x01",
            "何も突然やって来なくても……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        (
            "……まあいいや、\x01",
            "今は仕事に集中集中っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5EC8")

    #C0289
    ChrTalk(
        0xC,
        (
            "リャンに教わりながら、\x01",
            "俺もたまにカクテルを\x01",
            "作らせてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xC,
        (
            "カクテル作りって\x01",
            "奥が深くて大変だけど、\x01",
            "楽しくやらせてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6022")

    #C0291
    ChrTalk(
        0xC,
        (
            "ワジの特務支援課入りを機に、\x01",
            "チームのみんなで\x01",
            "色々話をしたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "とりあえず、しばらくは\x01",
            "みんなで協力して《トリニティ》を\x01",
            "手伝ってみることにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xC,
        (
            "元々はチームの溜まり場を兼ねて\x01",
            "アッバスが細々とやっていた\x01",
            "お店なんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xC,
        (
            "これからはバンバン客を呼び込んで\x01",
            "バンバン営業して行くつもりだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6085")

    label("loc_6022")


    #C0295
    ChrTalk(
        0xC,
        "これからもトリニティをよろしく。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        (
            "メニューも結構豊富だし、\x01",
            "食事だけの利用にもぜひどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6085")

    TalkEnd(0xC)
    Return()

    # Function_18_5429 end

    def Function_19_6089(): pass

    label("Function_19_6089")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_610D")

    #C0297
    ChrTalk(
        0xFE,
        (
            "ここのスープパスタ、\x01",
            "もの凄く美味しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "はっきり言って、\x01",
            "バーで出す一品料理の\x01",
            "レベルを超えているね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61C1")

    label("loc_610D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6169")

    #C0299
    ChrTalk(
        0xFE,
        "ウェイターの人、何かあったのかな？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "何だか、心ここに在らずってだね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_61C1")

    label("loc_6169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_61C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6184")
    Call(0, 11)
    Jump("loc_61C1")

    label("loc_6184")


    #C0301
    ChrTalk(
        0xFE,
        (
            "口コミで聞いて来たけど……\x01",
            "なかなか、いい雰囲気じゃん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61C1")

    TalkEnd(0xFE)
    Return()

    # Function_19_6089 end

    def Function_20_61C5(): pass

    label("Function_20_61C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_620F")

    #C0302
    ChrTalk(
        0xFE,
        (
            "ふふ、このペンネの食感が\x01",
            "たまらないのよね～、幸せ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BB")

    label("loc_620F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6271")

    #C0303
    ChrTalk(
        0xFE,
        (
            "ふふ、このお店、\x01",
            "また来ちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "相変わらず、\x01",
            "オシャレでいい雰囲気ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BB")

    label("loc_6271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_628C")
    Call(0, 11)
    Jump("loc_62BB")

    label("loc_628C")


    #C0305
    ChrTalk(
        0xFE,
        (
            "へえ、こんな所に\x01",
            "こんなお店があったのね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62BB")

    TalkEnd(0xFE)
    Return()

    # Function_20_61C5 end

    def Function_21_62BF(): pass

    label("Function_21_62BF")

    TalkBegin(0xFE)
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    # Function_21_62BF end

    def Function_22_62C9(): pass

    label("Function_22_62C9")

    OP_4B(0x12, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63BA")

    #C0306
    ChrTalk(
        0x12,
        (
            "はっはっはっ、少年。\x01",
            "もう後がないんじゃないかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x9,
        "……お兄さん、かなりやるね。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x9,
        (
            "これはワジと同等……\x01",
            "いや、それ以上かもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x105,
        (
            "#10305F（……ふぅん？\x01",
            "  どうやら大した腕前みたいだね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_640E")

    label("loc_63BA")


    #C0310
    ChrTalk(
        0x12,
        "さあ、次は君の番だよ。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        (
            "あ、ああ……\x01",
            "どう狙うか考えるから\x01",
            "ちょっと待って。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_640E")

    OP_4C(0x12, 0xFF)
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_22_62C9 end

    def Function_23_641A(): pass

    label("Function_23_641A")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0312
    ChrTalk(
        0x14,
        "キャー、すご～い！\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x13,
        "ほんと、かっこいいわ㈱\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x12,
        (
            "ははっ、“狙い”に関しては\x01",
            "それなりに自信があるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x12,
        (
            "もっとも、今僕が狙っているのは\x01",
            "あんな球コロではなく、\x01",
            "君たちのハートの方なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x13,
        "やんっ、またそんなこと言って㈱\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x14,
        "ふふ、ホントお上手ですよね。\x02",
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

    # Function_23_641A end

    def Function_24_6552(): pass

    label("Function_24_6552")


    #C0318
    ChrTalk(
        0x13,
        (
            "あ～ん、まさか\x01",
            "急に出て行っちゃうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x13,
        (
            "こんなことなら滞在先を\x01",
            "聞いておけば良かったわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x14,
        (
            "う～ん、確かに顔は\x01",
            "カッコよかったんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x14,
        (
            "でもちょっと\x01",
            "変わった人じゃなかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x13,
        (
            "バカね～、ちょっと\x01",
            "変わってるくらいなによ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x13,
        (
            "そこがまた、あの人の\x01",
            "魅力の１つなんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x14,
        "そ、そういうものなのかなぁ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    Return()

    # Function_24_6552 end

    def Function_25_66AD(): pass

    label("Function_25_66AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66CC")
    Call(0, 23)
    Jump("loc_66FB")

    label("loc_66CC")


    #C0325
    ChrTalk(
        0xFE,
        (
            "うふふ、今日は\x01",
            "素敵な人に出会っちゃった㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66FB")

    Jump("loc_6778")

    label("loc_6700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6712")
    Call(0, 24)
    Jump("loc_6778")

    label("loc_6712")


    #C0326
    ChrTalk(
        0xFE,
        (
            "あ～ん、まさか\x01",
            "急に出て行っちゃうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "こんなことなら滞在先を\x01",
            "聞いておけば良かったわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6778")

    TalkEnd(0xFE)
    Return()

    # Function_25_66AD end

    def Function_26_677C(): pass

    label("Function_26_677C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_679B")
    Call(0, 23)
    Jump("loc_67D4")

    label("loc_679B")


    #C0328
    ChrTalk(
        0xFE,
        (
            "あの人、楽器だけじゃなくて\x01",
            "ビリヤードも上手なのね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D4")

    Jump("loc_685F")

    label("loc_67D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67EB")
    Call(0, 24)
    Jump("loc_685F")

    label("loc_67EB")


    #C0329
    ChrTalk(
        0xFE,
        (
            "顔はいいし、歌と楽器も上手だし、\x01",
            "おまけにビリヤードまで……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "でも何だろう、\x01",
            "私にはピンと来なかったかな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685F")

    TalkEnd(0xFE)
    Return()

    # Function_26_677C end

    def Function_27_6863(): pass

    label("Function_27_6863")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6878")
    Call(0, 9)
    Jump("loc_68C9")

    label("loc_6878")


    #C0331
    ChrTalk(
        0xFE,
        (
            "クク、昼間から呑む酒の\x01",
            "旨いことったらないねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "五臓六腑に染み渡るよ。\x02",
    )

    CloseMessageWindow()

    label("loc_68C9")

    TalkEnd(0xFE)
    Return()

    # Function_27_6863 end

    def Function_28_68CD(): pass

    label("Function_28_68CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6989")

    #C0333
    ChrTalk(
        0xFE,
        (
            "弟の働いているバーに\x01",
            "内緒で訪ねてみたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "最初は恥ずかしがってたけど\x01",
            "ちゃんともてなしてくれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "プロ意識をもって働いてるのは\x01",
            "いいことですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_69E1")

    label("loc_6989")


    #C0336
    ChrTalk(
        0xFE,
        "こくこく……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "アゼルの作った\x01",
            "ノンアルコールカクテル……\x01",
            "なかなか美味しいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69E1")

    TalkEnd(0xFE)
    Return()

    # Function_28_68CD end

    def Function_29_69E5(): pass

    label("Function_29_69E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A74")

    #C0338
    ChrTalk(
        0xFE,
        (
            "うわ～、\x01",
            "みんなアゼル兄ちゃんと\x01",
            "おんなじ格好だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "いいな～、ぼくも\x01",
            "兄ちゃんとお揃いの\x01",
            "青いパーカーが欲しいなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6AB8")

    label("loc_6A74")


    #C0340
    ChrTalk(
        0xFE,
        (
            "いいな～、ぼくも\x01",
            "兄ちゃんとお揃いの\x01",
            "青いパーカーが欲しいなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AB8")

    TalkEnd(0xFE)
    Return()

    # Function_29_69E5 end

    def Function_30_6ABC(): pass

    label("Function_30_6ABC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4B")

    #C0341
    ChrTalk(
        0xFE,
        (
            "なんだか分かんねえけど、\x01",
            "とりあえずあのヨロイを\x01",
            "全部やっちまおうぜェ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんなら\x01",
            "きっとそうするしなァ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B8A")

    label("loc_6B4B")


    #C0343
    ChrTalk(
        0xFE,
        (
            "なんだかよく分かんねえけど、\x01",
            "ハデに決めてきやがれェ～！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8A")

    TalkEnd(0xFE)
    Return()

    # Function_30_6ABC end

    def Function_31_6B8E(): pass

    label("Function_31_6B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1A")

    #C0344
    ChrTalk(
        0xFE,
        (
            "あのヨロイは旧市街の方までは\x01",
            "入ってきてないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "一応、イグニスの近所の住民たちは\x01",
            "屋内に避難させたが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CAD")

    label("loc_6C1A")


    #C0346
    ChrTalk(
        0xFE,
        (
            "ジェドさんたちも\x01",
            "手伝ってくれるといいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんとあんな形で別れた事に\x01",
            "まだ納得がいってないみたいだし、\x01",
            "仕方ないだろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CAD")

    TalkEnd(0xFE)
    Return()

    # Function_31_6B8E end

    def Function_32_6CB1(): pass

    label("Function_32_6CB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CED")

    #C0348
    ChrTalk(
        0xFE,
        "外の青いモヤは一体なんなんだろう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D7E")

    label("loc_6CED")


    #C0349
    ChrTalk(
        0xFE,
        (
            "ふ、ふんっ……青坊主たちと\x01",
            "協力するのは今回だけだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんが\x01",
            "いつでも帰ってこれるように、\x01",
            "旧市街は俺たちで守ってやるんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D7E")

    TalkEnd(0xFE)
    Return()

    # Function_32_6CB1 end

    def Function_33_6D82(): pass

    label("Function_33_6D82")

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

    def lambda_6EDC():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EDC)

    def lambda_6EF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EF6)
    Sleep(400)

    def lambda_6F0A():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F0A)

    def lambda_6F24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6F24)
    Sleep(400)

    def lambda_6F38():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F38)

    def lambda_6F52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6F52)
    Sleep(400)

    def lambda_6F66():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F66)

    def lambda_6F80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6F80)
    WaitChrThread(0x101, 1)

    def lambda_6F95():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F95)
    WaitChrThread(0x102, 1)

    def lambda_6FA6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FA6)
    WaitChrThread(0x109, 1)

    def lambda_6FB7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6FB7)
    WaitChrThread(0x105, 1)

    def lambda_6FC8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6FC8)
    WaitChrThread(0x105, 2)
    OP_6F(0x10)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 0)

    #C0351
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "お客様は何名様ですか……\x02",
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
            "って、君たちは特務支援課！？\x01",
            "それにワジも……！\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#6P#00005Fい、いらっしゃいませって……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 500)

    #C0354
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、真面目に\x01",
            "営業しているみたいで\x01",
            "なによりだ。\x02\x03",

            "#10302Fフフ、どうだいアッバス。\x01",
            "少しは繁盛してるのかな？\x02",
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
            "……まあ、そこそこと言った所だ。\x02\x03",

            "それよりも、よく来たな。\x01",
            "せっかくだから寛#2Rくつろ#いでいくといい。\x02",
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

    def lambda_7223():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7223)

    def lambda_7230():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7230)

    def lambda_723D():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_723D)

    def lambda_724A():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_724A)

    def lambda_7257():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7257)
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
        "#04100F……ワジ、特務支援課はどうだ？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x105,
        (
            "#12P#10300Fまあ、そこそこ居心地はいいかな？\x02\x03",

            "#10304F課長や先輩も理解があるし、\x01",
            "気楽にやらせてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#12P#00006Fいや、ワジは正直言って\x01",
            "気楽過ぎると思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x109,
        (
            "#12P#10101Fそうだよ、ワジ君。\x01",
            "君も準メンバーとはいえ、\x01",
            "警察の一員としての自覚を……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、そんなこと言っても\x01",
            "これが僕のスタイルだしね。\x02\x03",

            "#10304F君たちもキッチリしすぎないで、\x01",
            "もう少し砕けてもいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        (
            "#12P#00106F……はあ、ワジ君には\x01",
            "何を言ってもムダそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#04100F……ふむ、上手くは\x01",
            "やれているようだな。\x01",
            "ならば何も問題はあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#12P#00006F（むしろ、問題しかないって\x01",
            "　感じなんだが……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x101,
        (
            "#12P#00005Fそういえば……\x01",
            "ワジの特務支援課入りに\x01",
            "反対するメンバーはいなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x102,
        (
            "#12P#00105Fあ、確かに……\x01",
            "さすがに色々と\x01",
            "戸惑ったんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#04100F……反対も何もない。\x01",
            "全てはワジが決めることだからな。\x02",
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
        "#12P#10106F（あまり答えになってませんけど……）\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        (
            "#12P#00006F（そういや、この人って\x01",
            "  こういうノリだったか……）\x02",
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
            "#11Pまあ、確かに戸惑いはしたけど……\x01",
            "一応、メンバー内で話し合って、\x01",
            "ちゃんと納得したことさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77DD():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77DD)
    Sleep(10)

    def lambda_77ED():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77ED)

    def lambda_77FA():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_77FA)
    Sleep(10)

    def lambda_780A():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_780A)
    Sleep(10)

    #C0370
    ChrTalk(
        0xA,
        (
            "#12P親への反発とか、家庭の事情とか、\x01",
            "色々な理由で集まったメンバーだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xA,
        (
            "#12Pワジが進む道を決めて\x01",
            "チームを抜けるなら、\x01",
            "僕たちもそれに反対はしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xA,
        (
            "#12Pむしろ、僕たち自身が\x01",
            "自立していく契機なんじゃないかってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "#11P実際、け、喧嘩ばかりしてた頃より、\x01",
            "トリニティを任されている\x01",
            "今のほうが充実しているしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "#5Pまあ、ワジがいないのは\x01",
            "確かに寂しいけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#6P#00002Fはは……なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x109,
        "#6P#N#10102F結構前向きみたいですね。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0377
    ChrTalk(
        0x105,
        (
            "#6P#10304Fま、もともとテスタメンツは\x01",
            "ほとんどアッバスに任せてたしね。\x02\x03",

            "#10300F僕がいなくても、皆それなりに\x01",
            "うまくやっていけると思ってたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        "#6P#04102F……そういうことだ。\x02",
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
            "#04100F特務支援課、ワジのことは\x01",
            "ひとまずお前たちに任せる。\x02\x03",

            "ワジも、こちらは気にせず\x01",
            "今の仕事に励むといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x105,
        "#12P#10304Fフフ、もとよりそのつもりさ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    #C0381
    ChrTalk(
        0x105,
        "#6P#10304Fというわけで、改めてヨロシク㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0382
    ChrTalk(
        0x101,
        (
            "#11P#00006Fま、まあ色々と\x01",
            "苦労させられそうだけど……\x02\x03",

            "#00000Fコホン、こっちも改めて\x01",
            "歓迎させてもらうよ。\x02",
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

    # Function_33_6D82 end

    def Function_34_7CD7(): pass

    label("Function_34_7CD7")

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

    def lambda_7DDC():
        OP_96(0xFE, 0x384, 0x0, 0x141E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7DDC)

    def lambda_7DF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7DF6)
    Sleep(400)

    def lambda_7E0A():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0x10FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E0A)

    def lambda_7E24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E24)
    Sleep(400)

    def lambda_7E38():
        OP_96(0xFE, 0x4BA, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E38)

    def lambda_7E52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E52)
    Sleep(400)

    def lambda_7E66():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xBE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E66)

    def lambda_7E80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7E80)
    Sleep(400)

    def lambda_7E94():
        OP_96(0xFE, 0x3E8, 0x0, 0x794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E94)

    def lambda_7EAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7EAE)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EFF")

    def lambda_7ED4():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_7ED4)

    def lambda_7EEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_7EEE)
    Jump("loc_7F2A")

    label("loc_7EFF")


    def lambda_7F04():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_7F04)

    def lambda_7F1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_7F1E)

    label("loc_7F2A")

    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)

    #C0383
    ChrTalk(
        0x105,
        (
            "#12P#10405Fおや、珍しいお客さんが\x01",
            "来てるみたいだね。\x02",
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

    def lambda_802B():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_802B)

    def lambda_8038():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8038)

    def lambda_8045():
        TurnDirection(0x9, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8045)

    def lambda_8052():
        TurnDirection(0x15, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8052)

    def lambda_805F():
        TurnDirection(0x16, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_805F)
    TurnDirection(0x17, 0x105, 500)

    #C0384
    ChrTalk(
        0x17,
        "#5Pお、お前はっ……！！\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xA,
        (
            "#11Pワ、ワジッ……！？\x01",
            "それに支援課じゃないか！！\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#00005Fテスタメンツにバイパー……\x01",
            "こんな所に集まってたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x16,
        (
            "#5Pあ、ああ……\x01",
            "街がこんな状況だから\x01",
            "今後について話しとこうとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x15,
        (
            "#5Pンなことより……\x01",
            "ワジの奴、なんか変な服\x01",
            "着てねえかァ～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x9,
        (
            "#11Pそ、そういえば……\x01",
            "それにアッバスは一緒じゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x105,
        (
            "#12P#10406Fやれやれ、せっかく帰ったのに\x01",
            "息つく暇もないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x104,
        (
            "#12P#00300Fいやまあ、さすがに\x01",
            "インパクトは大きいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x103,
        (
            "#6P#00203F一応、彼らにも一通り事情を\x01",
            "説明しておいた方がいいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x105,
        (
            "#12P#10403Fま、騎士団だの教会だのを\x01",
            "いきなり言っても混乱するだろうし、\x01",
            "説明も長くなりそうだ。\x02\x03",

            "#10400F君たちには後で改めて説明するよ。\x01",
            "……それでいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xA,
        (
            "#11Pあ、ああ……それもそうだな。\x01",
            "今はこの状況に集中しないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x105,
        (
            "#12P#10402Fフフ、それにしても……\x01",
            "僕やアッバスの留守をしっかりと\x01",
            "守ってくれていたみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x9,
        "#11Pも、もちろんだ。\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "#11Pワジとアッバスは\x01",
            "必ず戻ってくると\x01",
            "約束してくれたからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x9,
        (
            "#11Pだ、だったら、オレたちも\x01",
            "一所懸命やるだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x17,
        (
            "#5Pふん、別に俺たちは\x01",
            "ワジの留守番をしてた\x01",
            "わけじゃないけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x17,
        (
            "#5Pあんな事になったけど……\x01",
            "ヴァルドさんが帰ってくる場所は\x01",
            "ちゃんと守っておきたいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x16,
        (
            "#5Pああ、旧市街は俺たち\x01",
            "サーベルバイパーにとっても\x01",
            "大切な場所だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x16,
        (
            "#5Pジェドさん含む何人かは、\x01",
            "まだ協力する気に\x01",
            "なってくれてないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x105,
        "#12P#10404Fそうか……ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ、とっても立派よ、\x01",
            "ディーノ君。\x02",
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
        "#5Pべ、別にそんなんじゃ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x17, 500)

    #C0406
    ChrTalk(
        0x15,
        (
            "#5Pハハッ、ディーノお前、\x01",
            "何を照れてんだっつのォ～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8739")

    #C0407
    ChrTalk(
        0x10A,
        (
            "#12P#00603Fとにかく、旧市街には\x01",
            "大統領の操る化物は\x01",
            "出ていないようだし……\x02\x03",

            "#00600Fここは彼らに任せて\x01",
            "大丈夫だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#6P#00000Fええ、そうですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8886")

    label("loc_8739")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D2")

    #C0409
    ChrTalk(
        0x109,
        (
            "#N#12P#10103Fとにかく、旧市街には\x01",
            "大統領の操る化物は\x01",
            "出ていないみたいですし……\x02\x03",

            "#10100Fここは彼らに任せて\x01",
            "大丈夫そうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_8866")

    label("loc_87D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8866")

    #C0410
    ChrTalk(
        0x106,
        (
            "#N#12P#10703Fとにかく、旧市街には\x01",
            "敵側の使役する化物は\x01",
            "出ていないようですし……\x02\x03",

            "#10702Fここは彼らに任せて\x01",
            "大丈夫そうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_8866")


    #C0411
    ChrTalk(
        0x101,
        "#6P#00000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()

    label("loc_8886")

    TurnDirection(0x17, 0x105, 500)

    #C0412
    ChrTalk(
        0x105,
        (
            "#12P#10404Fそういうことだから\x01",
            "僕たちは行くとするよ。\x02\x03",

            "#10400F今しばらくの間、\x01",
            "留守をお願いできるかな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x105, 500)

    #C0413
    ChrTalk(
        0xA,
        "#11Pああ、任せておいてくれ！\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x9,
        "#11P気をつけてな、ワジ！\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x15,
        (
            "#5Pなんだかよく分かんねえけど、\x01",
            "ハデに決めてきやがれェ～！！\x02",
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

    # Function_34_7CD7 end

    SaveToFile()

Try(main)
