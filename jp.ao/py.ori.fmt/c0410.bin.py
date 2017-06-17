from ScenarioHelper import *

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
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0410",                  # 0
        "カレリア",               # 1
        "バルサモ支配人",         # 2
        "受付ローランド",         # 3
        "アバン劇団長",           # 4
        "ユージーン",             # 5
        "テオドール",             # 6
        "ニコル",                 # 7
        "プリエ",                 # 8
        "セリーヌ",               # 9
        "記者ノティシア",         # 10
        "シュリ",                 # 11
        "イリア",                 # 12
        "マリー",                 # 13
        "リーシャ",               # 14
        "ハインツ",               # 15
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch24200.itc",                   # 01
        "chr/ch28900.itc",                   # 02
        "chr/ch05102.itc",                   # 03
        "chr/ch05200.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch25900.itc",                   # 06
        "chr/ch27500.itc",                   # 07
        "chr/ch28700.itc",                   # 08
        "chr/ch28702.itc",                   # 09
        "chr/ch28800.itc",                   # 0A
        "chr/ch29000.itc",                   # 0B
        "chr/ch29100.itc",                   # 0C
        "chr/ch29102.itc",                   # 0D
        "chr/ch36600.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch36700.itc",                   # 10
        "chr/ch36900.itc",                   # 11
        "apl/ch50257.itc",                   # 12
        "chr/ch09800.itc",                   # 13
        "chr/ch10000.itc",                   # 14
        "chr/ch36800.itc",                   # 15
        "chr/ch47900.itc",                   # 16
        "chr/ch14100.itc",                   # 17
        "chr/ch37000.itc",                   # 18
    ))

    DeclNpc(-123800, 0,       -2289,   180,  261,  0x0, 0,   5,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-2250,   2500,    15000,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6969,    0,       3480,    270,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-42090,  5599,    102569,  135,  389,  0x0, 0,   7,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-125209, 0,       -479,    270,  261,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-87309,  0,       -1980,   90,   261,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-49939,  0,       13039,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-93360,  0,       -2000,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-125250, 0,       -460,    270,  261,  0x0, 0,   12,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-3920,   0,       -649,    0,    389,  0x0, 0,   22,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-122160, 0,       1000,    270,  389,  0x0, 0,   23,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-87540,  50,      -29,     90,   389,  0x0, 0,   3,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  9.0,                   14.0,                  2.5,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -4.5,                  -2.799999713897705,    -0.4999999701976776,   1.0])

    DeclActor(6500,    0,       3480,    1200,    6970,    1500,    3480,    0x007E, 0,  11, 0x0000)
    DeclActor(-125890, 0,       4530,    1200,    -125890, 2000,    4530,    0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1068, 0)                                       # 0

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4DC",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_532",          # 03, 3
        "Function_4_55D",          # 04, 4
        "Function_5_588",          # 05, 5
        "Function_6_CC0",          # 06, 6
        "Function_7_DE2",          # 07, 7
        "Function_8_E83",          # 08, 8
        "Function_9_11A5",         # 09, 9
        "Function_10_15C9",        # 0A, 10
        "Function_11_2264",        # 0B, 11
        "Function_12_2268",        # 0C, 12
        "Function_13_2B61",        # 0D, 13
        "Function_14_2ECE",        # 0E, 14
        "Function_15_304C",        # 0F, 15
        "Function_16_319A",        # 10, 16
        "Function_17_34A7",        # 11, 17
        "Function_18_38BF",        # 12, 18
        "Function_19_3A18",        # 13, 19
        "Function_20_3F74",        # 14, 20
        "Function_21_4115",        # 15, 21
        "Function_22_438C",        # 16, 22
        "Function_23_4564",        # 17, 23
        "Function_24_49CB",        # 18, 24
        "Function_25_4BA6",        # 19, 25
        "Function_26_528B",        # 1A, 26
        "Function_27_55B4",        # 1B, 27
        "Function_28_58AF",        # 1C, 28
        "Function_29_5945",        # 1D, 29
        "Function_30_5C46",        # 1E, 30
        "Function_31_6397",        # 1F, 31
        "Function_32_7070",        # 20, 32
        "Function_33_70BB",        # 21, 33
        "Function_34_7106",        # 22, 34
        "Function_35_7151",        # 23, 35
        "Function_36_719C",        # 24, 36
        "Function_37_71E7",        # 25, 37
        "Function_38_7232",        # 26, 38
        "Function_39_7269",        # 27, 39
        "Function_40_7295",        # 28, 40
        "Function_41_85A1",        # 29, 41
        "Function_42_85EC",        # 2A, 42
        "Function_43_8637",        # 2B, 43
        "Function_44_9117",        # 2C, 44
        "Function_45_9146",        # 2D, 45
        "Function_46_9175",        # 2E, 46
        "Function_47_91A4",        # 2F, 47
        "Function_48_91D3",        # 30, 48
        "Function_49_9890",        # 31, 49
        "Function_50_98B4",        # 32, 50
        "Function_51_9F3C",        # 33, 51
        "Function_52_A950",        # 34, 52
        "Function_53_AD1F",        # 35, 53
        "Function_54_B212",        # 36, 54
        "Function_55_B29C",        # 37, 55
        "Function_56_B315",        # 38, 56
        "Function_57_B38E",        # 39, 57
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_464"),
        (1, "loc_470"),
        (2, "loc_47C"),
        (3, "loc_488"),
        (4, "loc_494"),
        (5, "loc_4A0"),
        (6, "loc_4AC"),
        (SWITCH_DEFAULT, "loc_4B8"),
    )


    label("loc_464")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_470")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_47C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_488")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_494")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4DB")

    Return()

    # Function_0_42C end

    def Function_1_4DC(): pass

    label("Function_1_4DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_506")
    OP_94(0xFE, 0xFFFFF402, 0xFFFFF59C, 0xB72, 0xD0C, 0x3E8)
    Sleep(300)
    Jump("Function_1_4DC")

    label("loc_506")

    Return()

    # Function_1_4DC end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_531")
    OP_94(0xFE, 0xFFFE9F26, 0x5B4, 0xFFFE9346, 0xFFFFFA56, 0x3E8)
    Sleep(300)
    Jump("Function_2_507")

    label("loc_531")

    Return()

    # Function_2_507 end

    def Function_3_532(): pass

    label("Function_3_532")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55C")
    OP_94(0xFE, 0xFFFE17C2, 0xFFFFF8C6, 0xFFFE244C, 0x546, 0x3E8)
    Sleep(300)
    Jump("Function_3_532")

    label("loc_55C")

    Return()

    # Function_3_532 end

    def Function_4_55D(): pass

    label("Function_4_55D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_587")
    OP_94(0xFE, 0xFFFF403E, 0x201C, 0xFFFF3760, 0x42E0, 0x3E8)
    Sleep(300)
    Jump("Function_4_55D")

    label("loc_587")

    Return()

    # Function_4_55D end

    def Function_5_588(): pass

    label("Function_5_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_629")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xF, -6840, 0, 7100, 180)
    SetChrPos(0xB, -6840, 0, 6000, 0)
    SetChrPos(0x9, 3940, 0, 2900, 90)
    SetChrPos(0x8, -125110, 0, -1840, 270)
    SetChrPos(0x10, -90070, 0, 0, 270)
    SetChrPos(0xE, -91860, 0, 0, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_624")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_624")

    Jump("loc_B24")

    label("loc_629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6A0")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xF, -90070, 0, 0, 270)
    SetChrPos(0xD, -91860, 0, 0, 90)
    SetChrPos(0x8, -123770, 0, 1000, 90)
    SetChrPos(0x12, -122160, 0, 1000, 270)
    SetChrChipByIndex(0x12, 0x17)
    SetChrChipByIndex(0xD, 0x10)
    SetChrChipByIndex(0xF, 0x11)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x12, 0x10)
    Jump("loc_B24")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6C7")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_740")
    SetChrPos(0xC, -123770, 0, 1000, 90)
    SetChrPos(0xD, -122160, 0, 1000, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -48960, 0, 11170, 0)
    SetChrPos(0x10, -48960, 0, 12870, 180)
    SetChrPos(0xF, -90070, 0, 0, 270)
    SetChrPos(0x8, -91860, 0, 0, 90)
    Jump("loc_B24")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_784")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xF, -90070, 0, 0, 270)
    SetChrPos(0x8, -91860, 0, 0, 90)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_B24")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7B0")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7DC")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_808")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8FB")
    SetChrPos(0x10, -87750, 200, -2320, 90)
    SetChrPos(0x8, -88360, 0, -980, 135)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_847")
    SetChrFlags(0x8, 0x10)

    label("loc_847")

    SetChrChipByIndex(0x10, 0xD)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0xC, -124240, 0, -2210, 180)
    SetChrPos(0xF, -125280, 0, -1530, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_893")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_8A1")

    label("loc_893")

    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)

    label("loc_8A1")

    SetChrChipByIndex(0xF, 0x11)
    SetChrChipByIndex(0xC, 0xE)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -90360, 0, 4590, 270)
    SetChrPos(0xD, -92070, 0, 4590, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF")
    SetChrFlags(0xD, 0x10)

    label("loc_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EE")
    SetChrFlags(0xE, 0x10)

    label("loc_8EE")

    SetChrChipByIndex(0xE, 0x15)
    SetChrChipByIndex(0xD, 0x10)
    Jump("loc_B24")

    label("loc_8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9A4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -122610, 0, 2100, 45)
    SetChrPos(0x8, -121870, 0, 3110, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93F")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_93F")

    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x13, 0x3)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xF, -92910, 0, 5840, 180)
    SetChrPos(0x10, -92910, 0, 4520, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_990")
    SetChrFlags(0xF, 0x10)

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F")
    SetChrFlags(0x10, 0x10)

    label("loc_99F")

    Jump("loc_B24")

    label("loc_9A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9C6")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A7C")
    SetChrPos(0xC, -123770, 0, 1000, 90)
    SetChrPos(0xD, -122160, 0, 1000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A00")
    SetChrFlags(0xC, 0x10)

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0F")
    SetChrFlags(0xD, 0x10)

    label("loc_A0F")

    SetChrChipByIndex(0xC, 0xE)
    SetChrChipByIndex(0xD, 0x10)
    SetChrPos(0x8, -91860, 0, 1270, 135)
    SetChrPos(0x10, -89460, 0, 1670, 225)
    SetChrPos(0xF, -90070, 0, -590, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A59")
    SetChrFlags(0x8, 0x10)

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A68")
    SetChrFlags(0x10, 0x10)

    label("loc_A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A77")
    SetChrFlags(0xF, 0x10)

    label("loc_A77")

    Jump("loc_B24")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AA8")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B24")
    SetChrPos(0x10, -90860, 0, 5430, 180)
    SetChrPos(0xC, -90360, 0, -590, 270)
    SetChrPos(0xD, -92070, 0, -590, 90)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x8, -123770, 0, 1000, 90)
    SetChrPos(0xF, -122160, 0, 1000, 270)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B24")
    SetChrFlags(0xF, 0x10)

    label("loc_B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_B3F")

    Jump("loc_C22")

    label("loc_B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5F")
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_B5F")

    Jump("loc_C22")

    label("loc_B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B72")
    Jump("loc_C22")

    label("loc_B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B80")
    Jump("loc_C22")

    label("loc_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B8E")
    Jump("loc_C22")

    label("loc_B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9C")
    Jump("loc_C22")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BAD")
    Event(0, 53)
    Jump("loc_C22")

    label("loc_BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BBE")
    Event(0, 53)
    Jump("loc_C22")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BCC")
    Jump("loc_C22")

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BDA")
    Jump("loc_C22")

    label("loc_BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BE8")
    Jump("loc_C22")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BF6")
    Jump("loc_C22")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C07")
    Event(0, 52)
    Jump("loc_C22")

    label("loc_C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C22")
    SetMapFlags(0x10000000)
    Event(0, 50)

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C3B")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_C63")

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C54")
    ClearScenarioFlags(0x22, 1)
    SetMapFlags(0x10000000)
    Event(0, 43)
    Jump("loc_C63")

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_C63")
    ClearScenarioFlags(0x22, 2)
    Event(0, 49)

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C93")
    SetMapFlags(0x10000000)
    Event(0, 48)
    Jump("loc_CBF")

    label("loc_C93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    Event(0, 40)

    label("loc_CBF")

    Return()

    # Function_5_588 end

    def Function_6_CC0(): pass

    label("Function_6_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF3")

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0F")
    OP_10(0x0, 0x0)
    OP_10(0x11, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_D34")

    label("loc_D0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2B")
    OP_10(0x0, 0x0)
    OP_10(0x11, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_D34")

    label("loc_D2B")

    OP_10(0x0, 0x1)
    OP_10(0x11, 0x0)
    OP_10(0x10, 0x0)

    label("loc_D34")

    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x3, 0x0, 0x37)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D56")
    ModifyEventFlags(0, 0, 0x80)
    OP_1B(0x3, 0xFF, 0xFFFF)

    label("loc_D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6A")
    ClearMapObjFlags(0x1D, 0x4)

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D82")
    OP_1B(0x4, 0x0, 0x39)

    label("loc_D82")

    Jump("loc_DAA")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAA")
    OP_1B(0x4, 0x0, 0x39)

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC2")
    ModifyEventFlags(1, 5, 0x80)
    OP_1B(0x5, 0x0, 0x36)

    label("loc_DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD4")
    OP_65(0x0, 0x1)

    label("loc_DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_DE1")
    OP_65(0x0, 0x1)

    label("loc_DE1")

    Return()

    # Function_6_CC0 end

    def Function_7_DE2(): pass

    label("Function_7_DE2")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『導力車貴族』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36D, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7F")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『ノーブルカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36D, 1)

    label("loc_E7F")

    TalkEnd(0xFF)
    Return()

    # Function_7_DE2 end

    def Function_8_E83(): pass

    label("Function_8_E83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F27")

    #C0003
    ChrTalk(
        0xFE,
        (
            "実はさっき、イリア君から\x01",
            "劇団のみんなに導力通信を通して\x01",
            "エールが届いたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "なんていうか、イリア君には\x01",
            "本当に勇気をもらってばかりだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A1")

    label("loc_F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F35")
    Jump("loc_11A1")

    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F43")
    Jump("loc_11A1")

    label("loc_F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F51")
    Jump("loc_11A1")

    label("loc_F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F5F")
    Jump("loc_11A1")

    label("loc_F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F6D")
    Jump("loc_11A1")

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F7B")
    Jump("loc_11A1")

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F89")
    Jump("loc_11A1")

    label("loc_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F97")
    Jump("loc_11A1")

    label("loc_F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_116E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB2")
    Call(0, 9)
    Jump("loc_1169")

    label("loc_FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D9")

    #C0005
    ChrTalk(
        0xB,
        (
            "ううむ……私としたことが。\x01",
            "興奮して全く気配に気付かなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xB,
        "だが、まだ君たちでよかった。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "もし他の団員に見られていたら……\x01",
            "イリア君に百叩きにされていた所だよ。\x02",
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
    SetScenarioFlags(0x0, 0)
    Jump("loc_1169")

    label("loc_10D9")


    #C0008
    ChrTalk(
        0xFE,
        (
            "ううむ……私としたことが。\x01",
            "興奮して全く気配に気付かなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "もし他の団員に見られていたら……\x01",
            "イリア君に百叩きにされていた所だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1169")

    Jump("loc_11A1")

    label("loc_116E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_117C")
    Jump("loc_11A1")

    label("loc_117C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_118A")
    Jump("loc_11A1")

    label("loc_118A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1198")
    Jump("loc_11A1")

    label("loc_1198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_11A1")

    label("loc_11A1")

    TalkEnd(0xFE)
    Return()

    # Function_8_E83 end

    def Function_9_11A5(): pass

    label("Function_9_11A5")

    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0010
    ChrTalk(
        0x8,
        (
            "例の衣装のデザイン画を\x01",
            "起こしてみたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "こんな感じでどうでしょう？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "うん、いいじゃないか！\x01",
            "基本的な方向性はこれで\x01",
            "問題ないと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "イリア君にも見てもらって\x01",
            "意見をまとめておくから、\x01",
            "後でまた打ち合わせよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00005F（新衣装のデザイン画……？）\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#00100F（……凄く興味深いわね。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 0)

    #C0016
    ChrTalk(
        0x8,
        "あら、あなた方は……？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        "むむ、誰かね……（ささっ）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 0)

    #C0018
    ChrTalk(
        0xB,
        (
            "おや、君たちは……\x01",
            "………まさか、今の話を？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B7")

    #C0019
    ChrTalk(
        0x101,
        (
            "#00006Fえっと……\x01",
            "なんかすみません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_13B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EB")

    #C0020
    ChrTalk(
        0x102,
        "#00106Fあの……すみません。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_13EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")

    #C0021
    ChrTalk(
        0x103,
        "#00206Fえと……申し訳ないです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1423")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1464")

    #C0022
    ChrTalk(
        0x104,
        (
            "#00306Fええと……\x01",
            "なんつうか、すまねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1464")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149F")

    #C0023
    ChrTalk(
        0x109,
        (
            "#10106Fえ、えっと……\x01",
            "すみません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_149F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D5")

    #C0024
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、さあね。\x01",
            "どうだろう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D5")


    #C0025
    ChrTalk(
        0xB,
        "……ま、まあいい。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "とにかく、今の話は当劇団の\x01",
            "トップシークレット事項でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "君たちはここで何もみなかったし、\x01",
            "何も聞かなかった……いいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00005Fは、はい……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#00106Fお、お約束します。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x14B, 5)
    Return()

    # Function_9_11A5 end

    def Function_10_15C9(): pass

    label("Function_10_15C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16A0")

    #C0030
    ChrTalk(
        0xFE,
        (
            "クロスベルを取り巻く状況は\x01",
            "更に混迷を極めて参りましたが……\x01",
            "くよくよ考えている暇はありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "我々のすべきことは一つ――\x01",
            "一刻も早い公演再開に向けてあらゆる\x01",
            "努力を行うことだけですからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1780")

    #C0032
    ChrTalk(
        0xFE,
        (
            "突然の戒厳令と外出禁止令には\x01",
            "戸惑いましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "自宅に戻るくらいなら、\x01",
            "ここで練習をしていようと\x01",
            "全員で話し合って決めましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "今も皆さん、驚くほどの集中力で\x01",
            "舞台の練習に取り組んでおられますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_1780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_18BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1848")

    #C0035
    ChrTalk(
        0xFE,
        (
            "今日はイリアさんの病室へは\x01",
            "カレリアさんが行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "イリアさんは、まだ目を\x01",
            "覚まされないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "劇団メンバー全員が、\x01",
            "目覚めの日を信じておりますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18B6")

    label("loc_1848")


    #C0038
    ChrTalk(
        0xFE,
        (
            "イリアさんはまだ目を\x01",
            "覚まされないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "劇団メンバー全員が、\x01",
            "目覚めの日を信じておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B6")

    Jump("loc_2260")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4E")

    #C0040
    ChrTalk(
        0x9,
        "おや、皆さん……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00005Fあの………\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#00105F団員の皆さんはこちらに……？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "はい、一応全員が毎日顔を\x01",
            "出すようにしておりますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "といっても、リーシャさんはあの日以来、\x01",
            "一向に姿を見せておりませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00203Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "ちなみに、イリアさんの病室へは\x01",
            "毎日交替で劇団のメンバーが\x01",
            "お世話をしに行くことになりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "今日はシュリさんが一日中\x01",
            "付きっ切りで看病しているはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A98")

    #C0048
    ChrTalk(
        0x109,
        "#10105Fシュリちゃんが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD9")

    label("loc_1A98")


    #C0049
    ChrTalk(
        0x109,
        "#10100Fええ……さっき会って来ました。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "そうでしたか……\x02",
    )

    CloseMessageWindow()

    label("loc_1AD9")


    #C0051
    ChrTalk(
        0x9,
        (
            "……しかし、\x01",
            "私にはまだ信じられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "長い夢でも見ているじゃないかと、\x01",
            "そう思えて……仕方ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#00303F支配人……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "……取り留めのない話をして\x01",
            "申し訳ございません。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "とにかく、皆さんであれば\x01",
            "劇場への出入りはご自由に\x01",
            "して下さって結構ですので。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "また何かありましたら、\x01",
            "いつでもお越し下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00003F……お心遣い、感謝します。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 4)
    SetScenarioFlags(0x18C, 7)
    Jump("loc_1CC8")

    label("loc_1C4E")


    #C0058
    ChrTalk(
        0xFE,
        (
            "イリアさんの病室へは\x01",
            "今日はシュリさんが行っているはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "とにかく、早く意識を\x01",
            "取り戻して頂きたいのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC8")

    Jump("loc_2260")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D7F")

    #C0060
    ChrTalk(
        0xFE,
        (
            "本日午後、\x01",
            "ついに『金の太陽、銀の月』の\x01",
            "リニューアル公演が封切りとなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "舞台の仕上がりは上々……\x01",
            "必ずや皆様にご満足して頂けると\x01",
            "確信しておりますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1ECD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E12")

    #C0062
    ChrTalk(
        0xFE,
        (
            "よろしければ、シュリさんに\x01",
            "お声でも掛けてあげて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "きっと、あの娘にとっても\x01",
            "良い息抜きになると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC8")

    label("loc_1E12")


    #C0064
    ChrTalk(
        0xFE,
        (
            "シュリさんはイリアさんに内緒で\x01",
            "出てきたと言っていましたが……\x01",
            "流石に居場所は明白でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "ふふ、しかしイリアさんも\x01",
            "シュリさんのことがどうにも\x01",
            "放っておけないみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC8")

    Jump("loc_2260")

    label("loc_1ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1EDB")
    Jump("loc_2260")

    label("loc_1EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1EE9")
    Jump("loc_2260")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2076")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDB")

    #C0066
    ChrTalk(
        0xFE,
        (
            "リニューアル公演の公開日も\x01",
            "ついに３日後に迫って参りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "ちなみに、明日は一日かけて\x01",
            "本番を想定した最終リハーサルを\x01",
            "行う予定でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "劇団関係者以外は、\x01",
            "立ち入り禁止となりますので\x01",
            "ご了承下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2071")

    label("loc_1FDB")


    #C0069
    ChrTalk(
        0xFE,
        (
            "明日は一日かけて\x01",
            "本番を想定した最終リハーサルを\x01",
            "行う予定となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "劇団関係者以外は、\x01",
            "立ち入り禁止となりますので\x01",
            "ご了承下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2071")

    Jump("loc_2260")

    label("loc_2076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2126")

    #C0071
    ChrTalk(
        0xFE,
        (
            "昨日の舞台はいつにも増して\x01",
            "会心の出来栄えだったと\x01",
            "劇団長も喜んでおられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "首脳の皆様方にもそれぞれ\x01",
            "大変にご満足頂けたご様子で\x01",
            "本当に何よりですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2134")
    Jump("loc_2260")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21CF")

    #C0073
    ChrTalk(
        0xFE,
        (
            "おや、皆様。\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "イリアさんでしたら、\x01",
            "今は劇団長とリーシャさんの３人で\x01",
            "ステージの方にいらっしゃいますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_21CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21DD")
    Jump("loc_2260")

    label("loc_21DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2260")

    #C0075
    ChrTalk(
        0xFE,
        (
            "イリアさんとリーシャさんでしたら、\x01",
            "今はホールの方にいるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "よろしければ、\x01",
            "お会いになって行ってください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2260")

    TalkEnd(0xFE)
    Return()

    # Function_10_15C9 end

    def Function_11_2264(): pass

    label("Function_11_2264")

    Call(0, 12)
    Return()

    # Function_11_2264 end

    def Function_12_2268(): pass

    label("Function_12_2268")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2314")

    #C0077
    ChrTalk(
        0xA,
        (
            "まだまだ混乱の最中ですが……\x01",
            "それでも徐々に各所との連絡が\x01",
            "付くようになって参りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "とにかく、まずは出来る限り\x01",
            "情報を集めないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E3")

    #C0079
    ChrTalk(
        0xA,
        (
            "国防軍の設立直後、政府側から\x01",
            "市民に向けた特別公演の\x01",
            "開催の要請があったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "キャストも揃わない状況で\x01",
            "すぐには無理だということで、\x01",
            "時間をいただく形になったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "それから劇団長は１人で\x01",
            "脚本を書き上げ、それを皆さんが\x01",
            "今日まで練習してきたわけですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "この情勢を見る限り、\x01",
            "政府主導による公演開催など\x01",
            "到底不可能でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "ですが、例えどんな形になっても\x01",
            "私たちはこの再公演を\x01",
            "必ず実現させるつもりですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2583")

    label("loc_24E3")


    #C0084
    ChrTalk(
        0xA,
        (
            "この情勢を見る限り、\x01",
            "政府主導による公演開催など\x01",
            "到底不可能でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "ですが、例えどんな形になっても\x01",
            "私たちはこの再公演を\x01",
            "必ず実現させるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2583")

    Jump("loc_2B5D")

    label("loc_2588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_26F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2669")

    #C0086
    ChrTalk(
        0xA,
        (
            "……クロスベルは今、\x01",
            "重要な局面にあるようですが\x01",
            "我々のやるべきことは一つです。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        (
            "それは、イリアさんの回復を\x01",
            "信じて練習を続けること……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "私も全力を尽くして、\x01",
            "サポートさせて頂いています。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26EE")

    label("loc_2669")


    #C0089
    ChrTalk(
        0xA,
        (
            "我々のやるべきことは一つ。\x01",
            "イリアさんの回復を信じて\x01",
            "練習を続けること……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "私も全力を尽くして、\x01",
            "サポートさせて頂いています。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EE")

    Jump("loc_2B5D")

    label("loc_26F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_280F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AE")

    #C0091
    ChrTalk(
        0xA,
        (
            "あの赤毛の少女は\x01",
            "一体何者なんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "それに、リーシャさんは\x01",
            "一体どこに……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "とにかく……\x01",
            "わけの分からないことばかりで\x01",
            "混乱してしまいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_280A")

    label("loc_27AE")


    #C0094
    ChrTalk(
        0xA,
        (
            "あの赤毛の少女は\x01",
            "一体何者なんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "それに、リーシャさんは\x01",
            "一体どこに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280A")

    Jump("loc_2B5D")

    label("loc_280F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2887")

    #C0096
    ChrTalk(
        0xA,
        (
            "ついに、リニューアル公演の\x01",
            "公開日がやって来ましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "とにかく、今は舞台の成功を\x01",
            "祈るのみです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2895")
    Jump("loc_2B5D")

    label("loc_2895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28A3")
    Jump("loc_2B5D")

    label("loc_28A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28B1")
    Jump("loc_2B5D")

    label("loc_28B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2954")

    #C0098
    ChrTalk(
        0xA,
        (
            "公開の日が、いよいよ\x01",
            "間近に迫って参りました……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "アーティストはもちろん、\x01",
            "私を含めて他のスタッフ全員の\x01",
            "気合いが高まっているのを感じますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A1E")

    #C0100
    ChrTalk(
        0xA,
        (
            "昨夜、ここを立ち去られる際に\x01",
            "リベールのクローディア殿下から\x01",
            "直接お礼の言葉を頂いたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "私のような一スタッフにも\x01",
            "わざわざ声を掛けて下さるなんて、\x01",
            "本当に心の優しいお方ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A2C")
    Jump("loc_2B5D")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AD1")

    #C0102
    ChrTalk(
        0xA,
        (
            "『西ゼムリア通商会議』……\x01",
            "いよいよ明日から始まりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "ここまでの規模の国際会議は\x01",
            "非常に珍しいですからね。\x01",
            "何だか私まで緊張してきますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2ADF")
    Jump("loc_2B5D")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2B5D")

    #C0104
    ChrTalk(
        0xA,
        (
            "皆様、ようこそ\x01",
            "劇団《アルカンシェル》へ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "劇場のことで\x01",
            "何かご不明なことがあれば、\x01",
            "遠慮なくお尋ね下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5D")

    TalkEnd(0xA)
    Return()

    # Function_12_2268 end

    def Function_13_2B61(): pass

    label("Function_13_2B61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B72")
    Jump("loc_2EB0")

    label("loc_2B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C75")

    #C0106
    ChrTalk(
        0xFE,
        "イリアさん……すげえよな。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "咄嗟にシュリを庇って……\x01",
            "自分が怪我を負っても、\x01",
            "シュリの無事を喜んでた。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        "それに最後まで舞台のことを……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "俺たちに出来ることなら\x01",
            "何でもしたいが……こういう時、\x01",
            "一体何が出来るんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CF8")

    label("loc_2C75")


    #C0110
    ChrTalk(
        0xFE,
        (
            "俺たちに出来ることなら\x01",
            "何でもしたいが……こういう時、\x01",
            "一体何が出来るんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "くそっ……\x01",
            "どうにも考えがまとまらねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF8")

    Jump("loc_2EB0")

    label("loc_2CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D0B")
    Jump("loc_2EB0")

    label("loc_2D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D19")
    Jump("loc_2EB0")

    label("loc_2D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D27")
    Jump("loc_2EB0")

    label("loc_2D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D35")
    Jump("loc_2EB0")

    label("loc_2D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D50")
    Call(0, 14)
    Jump("loc_2D8E")

    label("loc_2D50")


    #C0112
    ChrTalk(
        0xFE,
        "うう、何か緊張すんな……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "下手すりゃ、舞台以上かも。\x02",
    )

    CloseMessageWindow()

    label("loc_2D8E")

    Jump("loc_2EB0")

    label("loc_2D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DA1")
    Jump("loc_2EB0")

    label("loc_2DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2DAF")
    Jump("loc_2EB0")

    label("loc_2DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCA")
    Call(0, 15)
    Jump("loc_2E2F")

    label("loc_2DCA")


    #C0114
    ChrTalk(
        0xC,
        (
            "はぁ、ちょっと\x01",
            "激しい動きをすると\x01",
            "すぐこれだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "早いとこ、\x01",
            "カレリアさんに言わねえと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2F")

    Jump("loc_2EB0")

    label("loc_2E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E42")
    Jump("loc_2EB0")

    label("loc_2E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5D")
    Call(0, 16)
    Jump("loc_2EB0")

    label("loc_2E5D")


    #C0116
    ChrTalk(
        0xC,
        (
            "草食系男子……\x01",
            "要は奥手な温厚キャラか？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        "フッ、だったら役作りは簡単だな。\x02",
    )

    CloseMessageWindow()

    label("loc_2EB0")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2ECD")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_2ECD")

    Return()

    # Function_13_2B61 end

    def Function_14_2ECE(): pass

    label("Function_14_2ECE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0118
    ChrTalk(
        0xF,
        (
            "あ～ん、カレリアったら\x01",
            "どこで油を売ってるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xF,
        "いいわ、こうなったら……\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x0)

    #C0120
    ChrTalk(
        0xF,
        (
            "ユージーン君、ちょっと\x01",
            "頼まれて欲しいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x13B, 0x0)

    #C0121
    ChrTalk(
        0xC,
        "何ですか、プリエさん？\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xF,
        (
            "ちょ～と、衣装の帯が\x01",
            "緩くなっちゃったんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xF,
        (
            "私１人じゃ締められないの。\x01",
            "手伝って㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0124
    ChrTalk(
        0xC,
        "マ、マジですか？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x16D, 4)
    Return()

    # Function_14_2ECE end

    def Function_15_304C(): pass

    label("Function_15_304C")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0125
    ChrTalk(
        0xC,
        (
            "いや～、しかし相変わらず\x01",
            "オレ様の衣装姿は罪作りだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "この凛々しい姿……\x01",
            "またファンが増えちまいそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        "……それはいいが、ユージーン。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "肩のところ、また糸がほつれて\x01",
            "飛び出しているぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0129
    ChrTalk(
        0xC,
        (
            "げ、まじか……\x01",
            "カレリアさんに言わねえと。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xD,
        "フッ、とんだ王子様だな。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_15_304C end

    def Function_16_319A(): pass

    label("Function_16_319A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348E")

    #C0131
    ChrTalk(
        0xC,
        (
            "しかし、ニコルの奴も\x01",
            "すっかり元通りって感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xD,
        (
            "ああ、それにあいつは地道ながらも\x01",
            "着実に力を伸ばしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        "油断していると、その内抜かれるぞ。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        "フッ、誰に向かって言ってやがる。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "この《アルカンシェルの王子》が\x01",
            "そう簡単に抜かれるハズないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        (
            "……最近、一部の間で\x01",
            "ニコルのような草食系男子というのが\x01",
            "流行っているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xD,
        (
            "ローランドの話では、\x01",
            "ニコル宛てのファンレターも\x01",
            "この所かなり増えているらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0138
    ChrTalk(
        0xC,
        "マ、マジか？　一体どんだけ……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xD,
        (
            "フフ、さあな。\x01",
            "本人に聞いてみたらどうだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0140
    ChrTalk(
        0xC,
        (
            "……テオドール、その草食系男子に\x01",
            "必要な要素ってのを洗いざらい教えろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        "一週間でマスターしてやる。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0142
    ChrTalk(
        0xD,
        "……そういう問題ではないだろう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 3)

    label("loc_348E")

    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_16_319A end

    def Function_17_34A7(): pass

    label("Function_17_34A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34B8")
    Jump("loc_38BB")

    label("loc_34B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_356F")

    #C0143
    ChrTalk(
        0xFE,
        (
            "ここ最近の、シュリの\x01",
            "演技への気持ちの入りようは\x01",
            "まさに圧巻という感じでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "技術うんぬんの前に、\x01",
            "見る者の心を奪う迫力がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "……俺たちも負けてられんな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_356F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_357D")
    Jump("loc_38BB")

    label("loc_357D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3658")

    #C0146
    ChrTalk(
        0xFE,
        (
            "しかし……リーシャは\x01",
            "一体どうしているんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "何か伏せている事実があるようだが……\x01",
            "あいつは俺たちの仲間だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "このまま姿も見せずに\x01",
            "いなくなるなんてことはないと\x01",
            "信じたいが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_36CF")

    label("loc_3658")


    #C0149
    ChrTalk(
        0xFE,
        (
            "……リーシャは\x01",
            "一体どうしているんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "このまま姿も見せずに\x01",
            "いなくなるなんてことはないと\x01",
            "信じたいが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CF")

    Jump("loc_38BB")

    label("loc_36D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_36E2")
    Jump("loc_38BB")

    label("loc_36E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36F0")
    Jump("loc_38BB")

    label("loc_36F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_36FE")
    Jump("loc_38BB")

    label("loc_36FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_370C")
    Jump("loc_38BB")

    label("loc_370C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_379E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3727")
    Call(0, 18)
    Jump("loc_3799")

    label("loc_3727")


    #C0151
    ChrTalk(
        0xFE,
        (
            "……自分自身の問題は結局の所、\x01",
            "自分で気付くしか解決はできない。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "イリアさんも、\x01",
            "正直もどかしいだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3799")

    Jump("loc_38BB")

    label("loc_379E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_37AC")
    Jump("loc_38BB")

    label("loc_37AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37BA")
    Jump("loc_38BB")

    label("loc_37BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D5")
    Call(0, 15)
    Jump("loc_381F")

    label("loc_37D5")


    #C0153
    ChrTalk(
        0xFE,
        (
            "……さて、着替えも\x01",
            "終わったことだし、\x01",
            "さっそく練習に向かうとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_381F")

    Jump("loc_38BB")

    label("loc_3824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3832")
    Jump("loc_38BB")

    label("loc_3832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_38BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384D")
    Call(0, 16)
    Jump("loc_38BB")

    label("loc_384D")


    #C0154
    ChrTalk(
        0xD,
        (
            "……どうやら\x01",
            "焚き付け方を誤ったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xD,
        (
            "ま、これはこれである意味、\x01",
            "効果的だったのかもしれないが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BB")

    TalkEnd(0xFE)
    Return()

    # Function_17_34A7 end

    def Function_18_38BF(): pass

    label("Function_18_38BF")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0156
    ChrTalk(
        0xE,
        (
            "シュリの奴……\x01",
            "かなり悩んでいるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xE,
        (
            "自分の演技に何が足りないのか、\x01",
            "ずっと考えているみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        "ああ……そのようだな。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xD,
        (
            "だが、これはシュリ自身の問題……\x01",
            "答えは本人にしか見つけられない。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "……だったら、\x01",
            "俺たちは黙って見守ってやればいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        "え、ええ……確かにそうですね。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_18_38BF end

    def Function_19_3A18(): pass

    label("Function_19_3A18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A9B")

    #C0162
    ChrTalk(
        0xFE,
        (
            "イリアの元気そうな声が聞けて\x01",
            "本当によかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "やっぱりイリアはイリアよね～。\x01",
            "私たちもがんばらないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F56")

    label("loc_3A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B5B")

    #C0164
    ChrTalk(
        0xFE,
        (
            "シュリは、姫の役を１人で\x01",
            "背負うプレッシャーに負けずに\x01",
            "よく頑張っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "舞台を頑張ることがイリアへの\x01",
            "何よりの恩返しになるって……\x01",
            "口に出さないけど分かってるのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F56")

    label("loc_3B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B69")
    Jump("loc_3F56")

    label("loc_3B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF4")

    #C0166
    ChrTalk(
        0xFE,
        (
            "いつもなら歌の練習を\x01",
            "している時間だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "……はあ………………\x01",
            "とてもそんな気分にはなれないわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3C4B")

    label("loc_3BF4")


    #C0168
    ChrTalk(
        0xFE,
        (
            "イリアがあんなことに\x01",
            "なってしまうなんて…………\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "……ほんと、信じられないわ。\x02",
    )

    CloseMessageWindow()

    label("loc_3C4B")

    Jump("loc_3F56")

    label("loc_3C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE3")

    #C0170
    ChrTalk(
        0xFE,
        (
            "あー、あー、あー。\x01",
            "うふ、今日も声の調子はバッチリね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "後は本番までマスクでも付けて、\x01",
            "喉を守っていようかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3D22")

    label("loc_3CE3")


    #C0172
    ChrTalk(
        0xFE,
        (
            "歌姫にとって喉は大事よね～。\x01",
            "のど飴をもう１つ頂こうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D22")

    Jump("loc_3F56")

    label("loc_3D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D35")
    Jump("loc_3F56")

    label("loc_3D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D43")
    Jump("loc_3F56")

    label("loc_3D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D51")
    Jump("loc_3F56")

    label("loc_3D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6C")
    Call(0, 14)
    Jump("loc_3DCF")

    label("loc_3D6C")


    #C0173
    ChrTalk(
        0xFE,
        (
            "うふふ、ユージーン君って\x01",
            "こう見えて意外とウブなのよね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "何だかお姉さんまで照れちゃうわ。\x02",
    )

    CloseMessageWindow()

    label("loc_3DCF")

    Jump("loc_3F56")

    label("loc_3DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEF")
    Call(0, 20)
    Jump("loc_3E80")

    label("loc_3DEF")


    #C0175
    ChrTalk(
        0xFE,
        (
            "う～ん、みんな超が付くほど\x01",
            "有名な方たちだから何となくは\x01",
            "分かったんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "あれだけ勢ぞろいされると、\x01",
            "流石に把握はしきれなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E80")

    Jump("loc_3F56")

    label("loc_3E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E93")
    Jump("loc_3F56")

    label("loc_3E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAE")
    Call(0, 21)
    Jump("loc_3EFD")

    label("loc_3EAE")


    #C0177
    ChrTalk(
        0xFE,
        "う～ん、残念ね。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "リーシャにもらったせんべい、\x01",
            "本当においしいのに～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EFD")

    Jump("loc_3F56")

    label("loc_3F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F10")
    Jump("loc_3F56")

    label("loc_3F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3F56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2B")
    Call(0, 22)
    Jump("loc_3F56")

    label("loc_3F2B")


    #C0179
    ChrTalk(
        0xFE,
        (
            "ぽりぽり……\x01",
            "あー、し・あ・わ・せ～㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F56")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3F73")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_3F73")

    Return()

    # Function_19_3A18 end

    def Function_20_3F74(): pass

    label("Function_20_3F74")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0180
    ChrTalk(
        0x10,
        (
            "……昨日は本当に\x01",
            "圧倒されましたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x10,
        (
            "オズボーン宰相に、\x01",
            "オリヴァルト皇子……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x10,
        (
            "ロックスミス大統領に\x01",
            "アルバート大公……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x10,
        (
            "クローディア殿下に\x01",
            "ユリア准佐……\x01",
            "それからそれから……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xF,
        (
            "ふふ、セリーヌったら\x01",
            "よく勉強しているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xF,
        (
            "私には結局、\x01",
            "誰が誰だか何となくしか\x01",
            "分からなかったわよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0186
    ChrTalk(
        0x10,
        (
            "うう……プリエさんの\x01",
            "お気楽さが羨ましいですわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_20_3F74 end

    def Function_21_4115(): pass

    label("Function_21_4115")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0187
    ChrTalk(
        0x10,
        (
            "うう、まだ前日とはいえ……\x01",
            "やはり緊張してしまいますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "まあ、流石に今回は\x01",
            "ただの賓客とも違いますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "でもあなたは、これまで何度も\x01",
            "苦難を乗り越えて来たんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        "もっと自信を持ってくださいな。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x10,
        "カレリアさん……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xF,
        (
            "そうよ、セリーヌ。\x01",
            "色々と気を回したところで\x01",
            "お腹が減るだけなんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xF,
        (
            "そうだ、一緒にオヤツ食べない？\x01",
            "ちょうどリーシャにもらった\x01",
            "東方のせんべいがあったのよねー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x10,
        (
            "いえ、こういう時は基本的に\x01",
            "胃の中へ物を入れたくないので……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "プリエさん……\x01",
            "貴女も本当にマイペースですわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_21_4115 end

    def Function_22_438C(): pass

    label("Function_22_438C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0196
    ChrTalk(
        0xF,
        (
            "ぽりぽり……\x01",
            "うふ、稽古の合間の\x01",
            "オヤツは最高ね～㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "はあ～、プリエさんったら。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "衣装部屋にはお菓子を\x01",
            "持ち込まないでって、\x01",
            "何度言ったら分かるんですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xF,
        "え～、だって今は休憩中なのよ？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xF,
        (
            "練習中はお菓子禁止なんだから、\x01",
            "食べるなら今しかないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "まったくもう……\x01",
            "本当に子供なんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#10302F（《神秘の歌姫》プリエ……\x01",
            "  なかなか、お茶目じゃないか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x109,
        (
            "#10106F（ほ、ほんと。\x01",
            "  舞台上とはえらい違いだね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_22_438C end

    def Function_23_4564(): pass

    label("Function_23_4564")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4614")

    #C0204
    ChrTalk(
        0xFE,
        (
            "イリアさんの声……\x01",
            "久しぶりにお聞きしましたけど\x01",
            "お元気そうで本当に何よりでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "大樹だか何だか知りませんけど、\x01",
            "私たちはとにかく練習あるのみですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C7")

    label("loc_4614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4622")
    Jump("loc_49C7")

    label("loc_4622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4630")
    Jump("loc_49C7")

    label("loc_4630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46BE")

    #C0206
    ChrTalk(
        0xFE,
        (
            "シュリは……あの子はまた……\x01",
            "……人一倍つらいでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "自分を庇ったせいだ、って……\x01",
            "ずっと、自分を責めてたから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C7")

    label("loc_46BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46CC")
    Jump("loc_49C7")

    label("loc_46CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46DA")
    Jump("loc_49C7")

    label("loc_46DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46E8")
    Jump("loc_49C7")

    label("loc_46E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46F6")
    Jump("loc_49C7")

    label("loc_46F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_474D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4711")
    Call(0, 24)
    Jump("loc_4748")

    label("loc_4711")


    #C0208
    ChrTalk(
        0xFE,
        (
            "わたくしはわたくし……\x01",
            "本当にそうなのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4748")

    Jump("loc_49C7")

    label("loc_474D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4768")
    Call(0, 20)
    Jump("loc_479D")

    label("loc_4768")


    #C0209
    ChrTalk(
        0xFE,
        (
            "うう……プリエさんの\x01",
            "お気楽さが羨ましいですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_479D")

    Jump("loc_49C7")

    label("loc_47A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47B0")
    Jump("loc_49C7")

    label("loc_47B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_482E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47CB")
    Call(0, 21)
    Jump("loc_4829")

    label("loc_47CB")


    #C0210
    ChrTalk(
        0xFE,
        (
            "プリエさんを見ていると、\x01",
            "何で自分がこんな緊張しているのか\x01",
            "ちょっと判らなくなりますわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4829")

    Jump("loc_49C7")

    label("loc_482E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_483C")
    Jump("loc_49C7")

    label("loc_483C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_49C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495B")

    #C0211
    ChrTalk(
        0xFE,
        (
            "テオ先輩とユージーン先輩、\x01",
            "本当にいつも一緒ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "……確かＢＬとか言ったかしら？\x01",
            "ファンの想像もあながち……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    #C0213
    ChrTalk(
        0xFE,
        (
            "……って、わたくしは\x01",
            "一体何を考えているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "さ、こうしている間にも\x01",
            "演技のイメージを固めませんと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_49C7")

    label("loc_495B")


    #C0215
    ChrTalk(
        0xFE,
        (
            "わ、わたくしは\x01",
            "一体何を考えているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "さ、こうしている間にも\x01",
            "演技のイメージを固めませんと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C7")

    TalkEnd(0xFE)
    Return()

    # Function_23_4564 end

    def Function_24_49CB(): pass

    label("Function_24_49CB")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0217
    ChrTalk(
        0x10,
        "はあ……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x10,
        (
            "ニコルだってより重要な配役を\x01",
            "もらいましたのに、わたくしは……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "もう何を言ってるんですか、\x01",
            "セリーヌさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "あなただって今回の舞台では\x01",
            "出番だって増えているじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x10,
        "それでも、他に比べたら……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "もう、何もそうやって殊更に\x01",
            "他と比べることなんてないのですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "あなたはあなた、この劇団でも\x01",
            "唯一無二の存在なんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "ほら、笑顔になって下さいまし。\x01",
            "そんなお顔のままじゃ、\x01",
            "せっかくのメイクも台無しですわよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_24_49CB end

    def Function_25_4BA6(): pass

    label("Function_25_4BA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C2F")

    #C0225
    ChrTalk(
        0xFE,
        (
            "今はイリアさんの\x01",
            "衣装の手入れをしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "いつでも袖を通せるように\x01",
            "準備しておくのが私の仕事ですからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5287")

    label("loc_4C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4A")
    Call(0, 26)
    Jump("loc_4CBA")

    label("loc_4C4A")


    #C0227
    ChrTalk(
        0xFE,
        (
            "ふふ、よく考えると\x01",
            "シュリさんはまだまだ\x01",
            "これからが成長期なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "ホント今後が益々楽しみですわ。\x02",
    )

    CloseMessageWindow()

    label("loc_4CBA")

    Jump("loc_5287")

    label("loc_4CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CCD")
    Jump("loc_5287")

    label("loc_4CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DAA")

    #C0229
    ChrTalk(
        0xFE,
        (
            "……あの日のことは、\x01",
            "今思い出しただけでも恐ろしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "イリアさんの衣装が、\x01",
            "痛々しく血に塗れていて……\x01",
            "とても見ていられませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "うう、イリアさん……\x01",
            "どうしてこんなことに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4E18")

    label("loc_4DAA")


    #C0232
    ChrTalk(
        0xFE,
        (
            "……あの日のことは、\x01",
            "今思い出しただけでも恐ろしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "うう、イリアさん……\x01",
            "どうしてこんなことに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E18")

    Jump("loc_5287")

    label("loc_4E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4EAC")

    #C0234
    ChrTalk(
        0xFE,
        (
            "ふふ、プリエさんは本当に\x01",
            "いつもマイペースですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "セリーヌさんも\x01",
            "今朝は元気そうでしたし、\x01",
            "安心して見ていられそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5287")

    label("loc_4EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EBA")
    Jump("loc_5287")

    label("loc_4EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4EC8")
    Jump("loc_5287")

    label("loc_4EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4ED6")
    Jump("loc_5287")

    label("loc_4ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF1")
    Call(0, 24)
    Jump("loc_4F70")

    label("loc_4EF1")


    #C0236
    ChrTalk(
        0xFE,
        (
            "セリーヌさんも\x01",
            "相当お悩みのようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "彼女の心情を思うと\x01",
            "無理もない気はしますけど……\x01",
            "何とか立ち直って欲しいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F70")

    Jump("loc_5287")

    label("loc_4F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F90")
    Call(0, 9)
    Jump("loc_5112")

    label("loc_4F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506D")

    #C0238
    ChrTalk(
        0xFE,
        "えっと、何だかすみません皆さん。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "リニューアル公演の詳細については\x01",
            "まだイリアさん以外のアーティストに\x01",
            "伝えていない状況でして……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "ですから、ここで見たことは\x01",
            "暫く内緒にしておいてくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5112")

    label("loc_506D")


    #C0241
    ChrTalk(
        0xFE,
        (
            "リニューアル公演の詳細については\x01",
            "まだイリアさん以外のアーティストに\x01",
            "伝えていない状況でして……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "ですから、ここで見たことは\x01",
            "暫く内緒にしておいてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5112")

    Jump("loc_5287")

    label("loc_5117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5125")
    Jump("loc_5287")

    label("loc_5125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_51E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5140")
    Call(0, 21)
    Jump("loc_51DC")

    label("loc_5140")


    #C0243
    ChrTalk(
        0xFE,
        (
            "イリアさんもそうですけど、\x01",
            "プリエさんもプレッシャーとは\x01",
            "無縁の人なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "そのハートの強さを\x01",
            "セリーヌさんにも分けてあげて\x01",
            "欲しいものですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DC")

    Jump("loc_5287")

    label("loc_51E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_51EF")
    Jump("loc_5287")

    label("loc_51EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_520A")
    Call(0, 22)
    Jump("loc_5287")

    label("loc_520A")


    #C0245
    ChrTalk(
        0xFE,
        (
            "ふう、とにかく\x01",
            "休憩の間に衣装合わせを\x01",
            "させていただきますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "もう止めませんから、\x01",
            "早く食べちゃってくださいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5287")

    TalkEnd(0xFE)
    Return()

    # Function_25_4BA6 end

    def Function_26_528B(): pass

    label("Function_26_528B")

    OP_4B(0x12, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x8,
        (
            "あら、シュリさん……\x01",
            "また身体が大きくなりました？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x12,
        "#12205Fえ、どうしてだ？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "ふふ、衣装係を\x01",
            "舐めてはいけませんわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        (
            "ちょっとした着立ての\x01",
            "感じで分かるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "といっても、\x01",
            "丈直しが必要になる程では\x01",
            "ありませんけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x12,
        (
            "#12202Fなるほど……\x01",
            "すごいな、カレリアさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "ふふ、よく考えると\x01",
            "シュリさんはまだまだ\x01",
            "これからが成長期なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x8,
        (
            "これからも一杯食べて\x01",
            "一杯練習に励んでくださいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x12,
        (
            "#12206Fう、うん……\x01",
            "ありがとう、カレリアさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#00000F（こんな状況だけど……\x01",
            "  なんか、ほのぼのするな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_553B")

    #C0257
    ChrTalk(
        0x106,
        (
            "#10702F（ふふ、そうですね。）\x02\x03",

            "#10704F（なんていうか、この劇場だけ\x01",
            "  別世界という感じがします。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_559E")

    label("loc_553B")


    #C0258
    ChrTalk(
        0x102,
        (
            "#00100F（ふふ、確かにね。）\x02\x03",

            "#00104F（なんていうか、この劇場だけ\x01",
            "  別世界って感じがするわ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_559E")

    SetScenarioFlags(0x1, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_26_528B end

    def Function_27_55B4(): pass

    label("Function_27_55B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_575F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56E5")

    #C0259
    ChrTalk(
        0xFE,
        (
            "なにがあっても、\x01",
            "とにかく全力で演技と向き合う……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "そんな風に考えていると、\x01",
            "不安とかそういう気持ちには\x01",
            "不思議とならないものだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "って、偉そうなこと言ったけど\x01",
            "これも全てイリアさんのおかげだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "あの人の言葉を聞いていると、\x01",
            "ホント力が湧き出す感じがするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_575A")

    label("loc_56E5")


    #C0263
    ChrTalk(
        0xFE,
        (
            "イリアさんって、\x01",
            "まさに太陽そのものだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "言葉だけで\x01",
            "こんなに力をもらえるなんて……\x01",
            "本当にありがたいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_575A")

    Jump("loc_58AB")

    label("loc_575F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_576D")
    Jump("loc_58AB")

    label("loc_576D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_577B")
    Jump("loc_58AB")

    label("loc_577B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5811")

    #C0265
    ChrTalk(
        0xFE,
        (
            "こんな時……イリアさんだったら\x01",
            "僕たちになんて声をかけるかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "しっかりしなきゃいけないのは\x01",
            "分かるけど……でも……でも………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AB")

    label("loc_5811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_58AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_582C")
    Call(0, 18)
    Jump("loc_58AB")

    label("loc_582C")


    #C0267
    ChrTalk(
        0xFE,
        (
            "シュリの奴、\x01",
            "かなり悩んでいるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "でも自分自身の問題、か。\x01",
            "……テオドール先輩の言葉には\x01",
            "含蓄があるなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58AB")

    TalkEnd(0xFE)
    Return()

    # Function_27_55B4 end

    def Function_28_58AF(): pass

    label("Function_28_58AF")

    TalkBegin(0xFE)

    #C0269
    ChrTalk(
        0xFE,
        (
            "ふふ、開場前にこうして\x01",
            "中へ入れるのは記者の特権ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "鉱山町の事も気がかりだけど、\x01",
            "今日はアルカンシェルの取材に\x01",
            "集中させてもらうわよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_58AF end

    def Function_29_5945(): pass

    label("Function_29_5945")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5963")
    Call(0, 26)
    Jump("loc_5C42")

    label("loc_5963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A85")
    TurnDirection(0x12, 0x106, 500)

    #C0271
    ChrTalk(
        0x12,
        (
            "#12201Fリーシャ姉……\x01",
            "突入作戦ってヤツ、\x01",
            "くれぐれも気を付けてな。\x02\x03",

            "#12203Fオレは何も出来ないけど、\x01",
            "とにかく練習だけは\x01",
            "一生懸命がんばるから……\x02\x03",

            "#12201Fだからリーシャ姉たちも\x01",
            "全力でがんばってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x106,
        (
            "#10702Fシュリちゃん……\x01",
            "うん、分かった！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B16")

    label("loc_5A85")


    #C0273
    ChrTalk(
        0x12,
        (
            "#12200Fアンタら……\x01",
            "突入作戦ってヤツ、\x01",
            "くれぐれも気を付けてな。\x02\x03",

            "それと、リーシャ姉のこと\x01",
            "よろしく頼んだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#00002Fああ、了解だ。\x02",
    )

    CloseMessageWindow()

    label("loc_5B16")

    SetScenarioFlags(0x1, 3)
    Jump("loc_5C42")

    label("loc_5B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BC5")
    TurnDirection(0x12, 0x106, 500)

    #C0275
    ChrTalk(
        0x12,
        (
            "#12203Fオレは何も出来ないけど、\x01",
            "とにかく練習だけは\x01",
            "一生懸命がんばるから……\x02\x03",

            "#12202Fだからリーシャ姉たちも\x01",
            "全力でがんばってきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C42")

    label("loc_5BC5")


    #C0276
    ChrTalk(
        0x12,
        (
            "#12200Fアンタら……\x01",
            "突入作戦ってヤツ、\x01",
            "くれぐれも気を付けてな。\x02\x03",

            "#12203Fそれと、リーシャ姉のこと\x01",
            "よろしく頼んだからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C42")

    TalkEnd(0xFE)
    Return()

    # Function_29_5945 end

    def Function_30_5C46(): pass

    label("Function_30_5C46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6305")

    #C0277
    ChrTalk(
        0x13,
        "#01700Fあら、弟君たちじゃない。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x13,
        (
            "#01700Fそれからティオちゃんも。\x01",
            "フフ、ずいぶん久しぶりね。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        "#00202Fはい、こちらこそお久しぶりです。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x13,
        (
            "#01700Fこれでとうとう支援課も\x01",
            "フルメンバーってわけね。\x02\x03",

            "#01704Fどうやら、みんなそれぞれ\x01",
            "前とは一回りも二回りも\x01",
            "成長したみたいだけど……\x02\x03",

            "#01709Fあたしたちアルカンシェルも\x01",
            "負けていられないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        "#00000Fはは、そう言って頂けて光栄です。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x104,
        (
            "#00305Fだが、なんつうか今日はまた\x01",
            "一段と気合い十分って感じッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x13,
        (
            "#01703Fまあ、なんてったって\x01",
            "次の公演はリニューアル前の\x01",
            "最後の公演になるからね。\x02\x03",

            "#01700F一つの集大成って思うと、\x01",
            "自然と気合いも入るって所かしら。\x02\x03",

            "#01706F今日は、リーシャが休みなのが\x01",
            "残念だけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_END)), "loc_609A")

    #C0284
    ChrTalk(
        0x109,
        (
            "#10105Fそういえばリーシャさん、\x01",
            "市役所に行く用事があるとか\x01",
            "言っていましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x13,
        (
            "#01705Fふぅん、リーシャに会ったのね？\x02\x03",

            "#01703F最近は少なくなったけど……\x01",
            "あの子は休みを取る時、割と直前に\x01",
            "申告してくることが何度かあってね。\x02\x03",

            "#01709Fその度に、隠れて\x01",
            "男とでも会ってるんじゃないかと\x01",
            "疑っちゃうのよね～。\x02\x03",

            "#01704Fま、もしそうだったとしたら\x01",
            "このイリアハンドが黙っちゃいないけど。\x01",
            "（わきわきっ）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61D2")

    label("loc_609A")


    #C0286
    ChrTalk(
        0x109,
        "#10100Fそうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x13,
        (
            "#01703Fええ、最近は少なくなったけど……\x01",
            "あの子は休みを取る時、割と直前に\x01",
            "申告してくることが何度かあってね。\x02\x03",

            "#01709Fその度に、隠れて\x01",
            "男とでも会ってるんじゃないかと\x01",
            "疑っちゃうのよね～。\x02\x03",

            "#01704Fま、もしそうだったとしたら\x01",
            "このイリアハンドが黙っちゃいないけど。\x01",
            "（わきわきっ）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D2")


    #C0288
    ChrTalk(
        0x102,
        "#00105F（ぞくっ……）\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、今一瞬何かの光景が\x01",
            "目に浮かんだ気がするね。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        "#00206F（エリィさん……）\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x13,
        (
            "#01700Fま、リーシャのことはともかく\x01",
            "今日も張り切って行かないとね。\x02\x03",

            "#01709F弟君たちも色々と忙しいでしょうけど\x01",
            "お互いやるべきことを尽くしましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#00000Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 5)
    Jump("loc_6393")

    label("loc_6305")


    #C0293
    ChrTalk(
        0x13,
        (
            "#01704Fさてと、何はともあれ\x01",
            "今日も張り切って行かないとね。\x02\x03",

            "#01700F弟君たちも色々と忙しいでしょうけど\x01",
            "お互いやるべきことを尽くしましょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6393")

    TalkEnd(0xFE)
    Return()

    # Function_30_5C46 end

    def Function_31_6397(): pass

    label("Function_31_6397")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 0, 0, 900, 180)
    OP_4B(0x9, 0xFF)
    OP_68(-470, 1350, -3340, 0)
    MoveCamera(52, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14990, 0)
    SetChrPos(0x101, -70, 0, -7720, 0)
    SetChrPos(0x102, -70, 0, -7720, 0)
    SetChrPos(0x109, -70, 0, -7720, 0)
    SetChrPos(0x105, -70, 0, -7720, 0)
    SetChrPos(0x104, -70, 0, -7720, 0)
    SetChrPos(0x1A3, -70, 0, -7720, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 32)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(700)
    OP_68(-400, 1350, -2210, 3000)
    BeginChrThread(0x109, 3, 0, 35)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 36)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 37)
    OP_6F(0x1)
    WaitChrThread(0x1A3, 3)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0294
    ChrTalk(
        0x9,
        (
            "#5Pああ、皆様……\x01",
            "ようこそお越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "#5P今、仔猫が突然入ってきて\x01",
            "ものすごいスピードで\x01",
            "駆け抜けていったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#12P#00006Fああ、すみません。\x02\x03",

            "#00000F実は俺たち、その仔猫を\x01",
            "追っている最中なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#12P#00100Fその……\x01",
            "劇場内を捜しても平気ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x9,
        (
            "#5Pええ、むしろ\x01",
            "そうして頂けると助かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x9,
        (
            "#5P本日は夜に各国首脳を招いての\x01",
            "ステージを控えているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#5Pちょうどアーティスト全員が\x01",
            "休憩している所でしたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#12P#00000Fよかった、それは好都合でした。\x02\x03",

            "それじゃ、パパッと捜します。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        (
            "#12P#00100Fちなみに、仔猫が\x01",
            "どこに向かったかご存知ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        "#5Pそれが申し訳ないのですが……\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x9,
        (
            "#5Pあまりに凄い勢いだったのと\x01",
            "突然の出来事だったもので\x01",
            "詳しいことはちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x9,
        (
            "#5Pただ、その階段を駆け上がって\x01",
            "行ったのは間違いありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#12P#00003Fなるほど……となると手分けして\x01",
            "捜した方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0307
    ChrTalk(
        0x102,
        (
            "#6P#00100Fそうね、分担はどうしましょう？\x02\x03",

            "#00103Fちょうど扉が３つあるから\x01",
            "２人ずつに分かれて行く？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0308
    ChrTalk(
        0x101,
        "#11P#00003Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_68(-30, 1150, -2770, 3000)
    MoveCamera(42, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15460, 3000)
    OP_95(0x1A3, 1560, 0, -3800, 3000, 0x0)
    OP_95(0x1A3, 1610, 0, -1100, 3000, 0x0)
    OP_95(0x1A3, 610, 0, -1240, 3000, 0x0)
    Sound(812, 0, 100, 0)
    TurnDirection(0x1A3, 0x105, 500)
    OP_6F(0x79)

    #C0309
    ChrTalk(
        0x1A3,
        (
            "#04609Fじゃあ、シャーリィは\x01",
            "お兄さんと一緒に行動するよ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#11P#00005Fへ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6A0F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A0F)
    Sleep(50)

    def lambda_6A1F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6A1F)
    Sleep(50)

    def lambda_6A2F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6A2F)
    Sleep(50)

    def lambda_6A3F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6A3F)
    Sleep(50)

    def lambda_6A4F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6A4F)
    WaitChrThread(0x104, 2)

    #C0311
    ChrTalk(
        0x102,
        "#6P#00101Fちょ、ちょっと待って！\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x109,
        "#12P#10105Fど、どうしてそうなるの？\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x1A3,
        (
            "#04605Fんー、なんとなく？\x02\x03",

            "#04609Fあ、ひょっとして\x01",
            "お姉さんたちが一緒に\x01",
            "お兄さんと回りたかった？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)
    OP_64(0x109)

    #C0314
    ChrTalk(
        0x102,
        "#6P#00106Fそ、そんなことは……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x109,
        "#12P#10101Fそういう問題じゃなくて……！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#6P#10309Fあはは、何だか\x01",
            "面白いことになってるなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0317
    ChrTalk(
        0x101,
        "#11P#00006Fお前、他人事だと思って……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        (
            "#12P#00303F……ま、ここまで来たら\x01",
            "おかしなマネはしねぇだろ。\x02\x03",

            "#00301Fシャーリィ。\x01",
            "ロイドに変なちょっかい\x01",
            "掛けるんじゃねえぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1A3,
        "#04604Fはいはい、分かってるって。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    #C0320
    ChrTalk(
        0x1A3,
        (
            "#04600Fお兄さん可愛いけど、\x01",
            "シャーリィの趣味とは違うしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#11P#00006F可愛いって……\x01",
            "ふう、まあいいや。\x02\x03",

            "#00000Fとりあえず手分けして\x01",
            "劇場内を捜すことにしよう。\x02\x03",

            "みんな、一通り調べたら\x01",
            "エントランスに集合してくれ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(48590, 1300, -180, 0)
    MoveCamera(34, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14900, 0)
    SetChrPos(0x101, 45300, 0, 40, 90)
    SetChrPos(0x1A3, 45300, 0, 40, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 39)
    WaitChrThread(0x101, 3)

    #C0322
    ChrTalk(
        0x1A3,
        (
            "#6P#04602Fふふっ、それじゃ、\x01",
            "さっそくマリーを捜そっか？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00000Fああ、もちろんだ。\x02\x03",

            "#00003F（しかしこうして話してると\x01",
            "  無邪気で気まぐれな女の子にしか\x01",
            "  見えないけど……）\x02\x03",

            "（さっき、ドラ息子たちを\x01",
            "  脅かした殺気は本物だった……）\x02\x03",

            "#00001F（いったいどっちが\x01",
            "  本当のこの子なんだ……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0324
    ChrTalk(
        0x1A3,
        (
            "#6P#04605Fあれれ、どしたの？\x02\x03",

            "#04609Fひょっとして\x01",
            "シャーリィに惚れちゃった？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#00003F……惚れません。\x02\x03",

            "#00000Fとりあえず、２Ｆの\x01",
            "Ｓ席を調べてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x1A3,
        "#6P#04609Fあはは、イエッサー。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x155, 5)
    ModifyEventFlags(1, 5, 0x80)
    OP_1B(0x5, 0x0, 0x36)
    OP_29(0x74, 0x1, 0x6)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 49470, 0, 40, 0)
    EventEnd(0x5)
    Return()

    # Function_31_6397 end

    def Function_32_7070(): pass

    label("Function_32_7070")


    def lambda_7075():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7075)

    def lambda_7086():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7086)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 900, 0, -1900, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_7070 end

    def Function_33_70BB(): pass

    label("Function_33_70BB")


    def lambda_70C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_70C0)

    def lambda_70D1():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70D1)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -900, 0, -1900, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_70BB end

    def Function_34_7106(): pass

    label("Function_34_7106")


    def lambda_710B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_710B)

    def lambda_711C():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_711C)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -900, 0, -4300, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_7106 end

    def Function_35_7151(): pass

    label("Function_35_7151")


    def lambda_7156():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7156)

    def lambda_7167():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7167)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 0, -3100, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_35_7151 end

    def Function_36_719C(): pass

    label("Function_36_719C")


    def lambda_71A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_71A1)

    def lambda_71B2():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71B2)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -900, 0, -3100, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_36_719C end

    def Function_37_71E7(): pass

    label("Function_37_71E7")


    def lambda_71EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_71EC)

    def lambda_71FD():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_71FD)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 800, 0, -4300, 2000, 0x0)
    OP_93(0x1A3, 0x0, 0x1F4)
    Return()

    # Function_37_71E7 end

    def Function_38_7232(): pass

    label("Function_38_7232")


    def lambda_7237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7237)

    def lambda_7248():
        OP_95(0xFE, 50110, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7248)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x1A3, 500)
    Return()

    # Function_38_7232 end

    def Function_39_7269(): pass

    label("Function_39_7269")


    def lambda_726E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_726E)

    def lambda_727F():
        OP_95(0xFE, 48110, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_727F)
    Return()

    # Function_39_7269 end

    def Function_40_7295(): pass

    label("Function_40_7295")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, 660, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x15, 0x13)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, 1200, 0, 2260, 270)
    OP_68(-3160, 3750, -1920, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, 7220, 2500, 13500, 225)
    SetChrPos(0x1A3, 7220, 2500, 14500, 225)
    SetChrPos(0x104, -900, 0, 1060, 90)
    SetChrPos(0x109, -900, 0, 2260, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetCameraDistance(9010, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(5640, 3950, 12260, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11610, 0)
    OP_0D()
    OP_63(0x1A3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x1A3,
        "#5P#04605Fあれ、あのお姉さんは……！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#11P#00005Fあれは……\x01",
            "もしかしてリーシャか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-70, 1450, 5100, 0)
    MoveCamera(42, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13470, 0)
    SetChrPos(0x101, 960, 1530, 9450, 180)
    SetChrPos(0x1A3, -450, 1620, 9500, 180)
    OP_93(0x15, 0x0, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_93(0x109, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)

    def lambda_7529():
        OP_95(0xFE, 900, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7529)
    Sleep(50)

    def lambda_7546():
        OP_95(0xFE, -800, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7546)
    OP_68(-660, 1450, 2200, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13470, 3000)
    WaitChrThread(0x1A3, 1)

    def lambda_7592():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7592)
    WaitChrThread(0x1A3, 1)
    OP_6F(0x79)

    #C0329
    ChrTalk(
        0x101,
        (
            "#5P#00000Fやっぱり、リーシャじゃないか。\x02\x03",

            "#00005Fアーティストは全員、\x01",
            "休憩中だったんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0330
    AnonymousTalk(
        0x15,
        (
            "あ、ロイドさん。\x02\x03",

            "えっと、昨日の夜遅くに\x01",
            "衣装を修繕してもらっていて……\x02\x03",

            "本番前の最終チェックとして\x01",
            "衣装合わせてをしていたんです。\x02\x03",

            "それよりも……\x01",
            "仔猫が入り込んだそうですね？\x02",
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

    #C0331
    ChrTalk(
        0x101,
        "#5P#00001Fああ、そうなんだけど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0332
    ChrTalk(
        0x101,
        (
            "#11P#00005Fって、あれ？\x02\x03",

            "俺たち、逃げた仔猫を追って\x01",
            "ここに戻ってきたんだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    TurnDirection(0x104, 0x15, 500)

    #C0333
    ChrTalk(
        0x104,
        "#12P#00305Fなんだ、そうなのか？\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x109,
        (
            "#6P#10100F少なくともこちらには\x01",
            "来ていないと思いますけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)
    Fade(500)
    OP_68(-9590, 3950, 12900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12320, 0)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    SetChrPos(0x102, -10590, 2500, 14070, 135)
    SetChrPos(0x105, -10590, 2500, 14070, 135)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_68(-8560, 3950, 12020, 3000)
    Sound(103, 0, 100, 0)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 42)
    WaitChrThread(0x105, 3)
    Sleep(1000)
    OP_6F(0x1)

    #C0335
    ChrTalk(
        0x105,
        "#6P#10300Fやあ、みんなお揃いだね。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#5P#00100Fそうみたいね。\x01",
            "それに、リーシャさんまで。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#6P#N#00000Fワジにエリィ……\x01",
            "その様子だと見てないようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-870, 1450, 2630, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14250, 0)
    SetChrPos(0x105, -2400, 0, 3460, 90)
    SetChrPos(0x102, -2200, 0, 1960, 90)
    SetChrPos(0x104, -900, 0, 560, 90)
    SetChrPos(0x109, -900, 0, 1960, 90)
    OP_93(0x101, 0xE1, 0x0)
    OP_93(0x1A3, 0x87, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x109, 0x2D, 0x0)
    OP_93(0x9, 0x13B, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0338
    ChrTalk(
        0x101,
        (
            "#11P#00005Fすると、俺たちが見失ってから\x01",
            "誰もマリーを見ていないのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#6P#00103F玄関は閉じてもらったし……\x02\x03",

            "#00100Fやっぱりこのホール付近が\x01",
            "怪しいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        (
            "#12P#00303Fふむ、どこかの陰に\x01",
            "隠れてる可能性はありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x109,
        (
            "#6P#10100Fそうですね。\x01",
            "一度全員で捜してみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x105,
        "#6P#10304Fま、それしかなさそうだね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A3)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x15, 0x1A3, 500)
    Sleep(300)

    #C0343
    ChrTalk(
        0x15,
        (
            "#12P#06202Fえっと……？\x02\x03",

            "あの、こちらの女の子は？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        "#5P#00000Fああ、その子は──\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    #C0345
    ChrTalk(
        0x1A3,
        (
            "#5P#04609Fあはは、お姉さん凄いね♪\x02\x03",

            "#04611Fさっきから狙ってるのに\x01",
            "ゼンゼン隙がないんだもん！\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x15,
        "#12P#06205Fえ、え……？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x104,
        (
            "#12P#00303F……そいつは俺の、\x01",
            "不肖の従妹#5R  イトコ#でな。\x02\x03",

            "#00300Fあんま気にしないでやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x15,
        "#11P#06205Fランディさんの……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0349
    AnonymousTalk(
        0x1A3,
        (
            "シャーリィ・オルランド！\x01",
            "シャーリィって呼んでね！\x02\x03",

            "いや～、お姉さんのことは\x01",
            "アルカンシェルの舞台で見たけど。\x02\x03",

            "こうして近くで見ると\x01",
            "また破壊力はカクベツだね～！\x02\x03",

            "いいな～。\x01",
            "おっきくてうらやましいよ㈱\x02",
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
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x15, 0xB4, 0x1F4, 0x5DC, 0x0)

    #C0350
    ChrTalk(
        0x15,
        "#12P#06209Fえっと、それって……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#6P#00113F……既に私は一度、\x01",
            "被害に遭っているから。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0352
    ChrTalk(
        0x1A3,
        (
            "#5P#04609Fあはは、いいじゃん。\x01",
            "減るもんじゃないんだし。\x02\x03",

            "これも何かの縁って事で──\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x15)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8074():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8074)
    Sleep(50)

    def lambda_8084():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8084)
    Sleep(300)

    #C0353
    ChrTalk(
        0x1A3,
        "#6P#04605Fあれっ……？\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x15,
        "#12P#06205Fあ……！\x02",
    )

    CloseMessageWindow()

    def lambda_80C9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80C9)
    Sleep(50)

    def lambda_80D9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_80D9)
    Sleep(50)

    def lambda_80E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_80E9)
    Sleep(50)

    def lambda_80F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_80F9)
    Sleep(50)

    def lambda_8109():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8109)
    Sleep(50)

    def lambda_8119():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8119)
    Sleep(50)

    def lambda_8129():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8129)
    OP_68(3650, 1450, 17480, 4000)
    MoveCamera(28, 27, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15360, 4000)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3500, 2500, 15290, 135)
    OP_95(0x14, 4420, 2500, 14500, 1500, 0x0)
    OP_68(-50, 3950, 13550, 3000)
    MoveCamera(32, 33, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14250, 3000)
    OP_95(0x14, 3250, 2500, 13660, 1500, 0x0)
    OP_95(0x14, 50, 2500, 13570, 1500, 0x0)
    Sleep(300)
    OP_6F(0x79)
    TurnDirection(0x14, 0x101, 500)
    OP_63(0x14, 0x0, 1200, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-50, 3950, 15320, 3000)

    def lambda_822F():
        OP_95(0xFE, 0, 2500, 18930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_822F)
    Sleep(1000)

    def lambda_824C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_824C)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-870, 1450, 2630, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14250, 0)
    SetChrFlags(0x14, 0x80)
    OP_0D()

    #C0355
    ChrTalk(
        0x101,
        (
            "#11P#00011Fあ、あんな所に\x01",
            "隠れていたのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x15,
        "#11P#06201F私、追いかけてきます！\x02",
    )

    CloseMessageWindow()

    def lambda_82F6():

        label("loc_82F6")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_82F6")

    QueueWorkItem2(0x102, 1, lambda_82F6)

    def lambda_8308():

        label("loc_8308")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_8308")

    QueueWorkItem2(0x104, 1, lambda_8308)

    def lambda_831A():

        label("loc_831A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_831A")

    QueueWorkItem2(0x109, 1, lambda_831A)

    def lambda_832C():

        label("loc_832C")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_832C")

    QueueWorkItem2(0x105, 1, lambda_832C)
    OP_95(0x15, 1290, 0, 5610, 4000, 0x0)

    def lambda_8352():
        OP_95(0xFE, 0, 2500, 15240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8352)
    Sleep(500)

    #C0357
    ChrTalk(
        0x1A3,
        "#11P#04602Fあはは、シャーリィも！\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A3, -230, 10, 3500, 4000, 0x0)
    OP_95(0x1A3, 0, 2500, 15240, 4000, 0x0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x1A3, 0x80)
    OP_0D()

    #C0358
    ChrTalk(
        0x104,
        "#12P#00306Fはあ、ったく……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        (
            "#6P#00105Fえっと……\x01",
            "どうしたらいいのかしら？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0360
    ChrTalk(
        0x101,
        (
            "#5P#00000F俺が２人のフォローに回るよ。\x02\x03",

            "また逃げてくるかもしれないし、\x01",
            "みんなはここで待機してくれ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_849D():

        label("loc_849D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_849D")

    QueueWorkItem2(0x102, 1, lambda_849D)
    Sleep(50)

    def lambda_84B2():

        label("loc_84B2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_84B2")

    QueueWorkItem2(0x104, 1, lambda_84B2)
    Sleep(50)

    def lambda_84C7():

        label("loc_84C7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_84C7")

    QueueWorkItem2(0x109, 1, lambda_84C7)
    Sleep(50)

    def lambda_84DC():

        label("loc_84DC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_84DC")

    QueueWorkItem2(0x105, 1, lambda_84DC)
    Sleep(300)

    #C0361
    ChrTalk(
        0x109,
        "#6P#10100F了解しました。\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、今度こそちゃんと\x01",
            "捕まえられるといいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 40, 0, 5330, 4000, 0x0)
    OP_95(0x101, 0, 2500, 15240, 4000, 0x0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SoundLoad(3243)
    SoundLoad(3244)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c0420", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_40_7295 end

    def Function_41_85A1(): pass

    label("Function_41_85A1")


    def lambda_85A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_85A6)

    def lambda_85B7():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85B7)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -6510, 2500, 12970, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_41_85A1 end

    def Function_42_85EC(): pass

    label("Function_42_85EC")


    def lambda_85F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_85F1)

    def lambda_8602():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8602)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -7770, 2500, 12730, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_42_85EC end

    def Function_43_8637(): pass

    label("Function_43_8637")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 1200, 0, 900, 180)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -1200, 0, 900, 180)
    SetChrChipByIndex(0x15, 0x13)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 0, 0, 900, 180)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -1400, 0, -1900, 0)
    OP_68(-740, 1550, -1860, 0)
    MoveCamera(41, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14480, 0)
    SetChrPos(0x101, 900, 0, -1900, 0)
    SetChrPos(0x1A3, -400, 0, -1900, 0)
    SetChrPos(0x102, 900, 0, -3100, 0)
    SetChrPos(0x109, -900, 0, -3100, 0)
    SetChrPos(0x104, -900, 0, -4300, 0)
    SetChrPos(0x105, 900, 0, -4300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-740, 1450, -1860, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0363
    ChrTalk(
        0x1A3,
        (
            "#12P#04600Fアハハ、ありがと♪\x01",
            "お姉さんには助けられちゃったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、俺からも\x01",
            "お礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x15,
        (
            "#06209Fいえ、とっさに\x01",
            "体が動いただけですから。\x02\x03",

            "#06204Fそれに、私がでしゃばらなくても\x01",
            "シャーリィさんだったら\x01",
            "仔猫を助けていたと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0366
    ChrTalk(
        0x101,
        "#12P#00005Fそ、そうなのか……？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x1A3,
        (
            "#12P#04605Fへえ、分かるんだ？\x02\x03",

            "#04604F確かにあのタイミングなら\x01",
            "飛び込んだら助けられたけど……\x02\x03",

            "#04609Fとりあえず、お姉さんのジャンプと\x01",
            "ダイナミックな胸の動きが\x01",
            "見られたから満足かなー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0368
    ChrTalk(
        0x104,
        "#12P#00306Fシャーリィ、お前な……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x102,
        "#12P#00106F……ご愁傷様、リーシャさん。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x15,
        "#06209Fあ、あはは……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x16,
        (
            "そ、それにしても\x01",
            "本当に申し訳ありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x16,
        "まさか舞台に仔猫がいたなんて……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x16,
        (
            "なのに確認もせず、点検のために\x01",
            "装置を動かしてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x1A3,
        (
            "#12P#04600Fま、いいんじゃない？\x02\x03",

            "#04604F誰かが怪我したわけでもなし。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、ですから\x01",
            "そんなに気にしないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x109,
        (
            "#6P#10100Fとりあえず……\x01",
            "そろそろボンドさんの所に\x01",
            "戻りましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそうだね、今も心配して\x01",
            "捜している最中だろうし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    #C0378
    ChrTalk(
        0x14,
        "#6Pにゃ～ん♪\x02",
    )

    CloseMessageWindow()

    def lambda_8C4F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C4F)
    Sleep(50)

    def lambda_8C5F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8C5F)
    Sleep(50)

    def lambda_8C6F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8C6F)
    Sleep(50)

    def lambda_8C7F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C7F)
    Sleep(50)

    def lambda_8C8F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C8F)
    Sleep(50)

    def lambda_8C9F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C9F)
    Sleep(300)

    #C0379
    ChrTalk(
        0x104,
        (
            "#11P#00309Fはは……\x01",
            "現金だな、コイツ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        (
            "#11P#00102Fそうね、さっきまで\x01",
            "あんなに怯えていたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x1A3,
        "#11P#04609Fあはは、だってそれが猫だし。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#11P#00003F（この子が言うと\x01",
            "  物凄く説得力があるような……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0383
    ChrTalk(
        0x101,
        (
            "#12P#00000F──それじゃあ、\x01",
            "俺たち、これで失礼します。\x02\x03",

            "ご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DEC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8DEC)
    Sleep(50)

    def lambda_8DFC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DFC)
    Sleep(50)

    def lambda_8E0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8E0C)
    Sleep(50)

    def lambda_8E1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E1C)
    Sleep(50)

    def lambda_8E2C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8E2C)
    Sleep(300)

    #C0384
    ChrTalk(
        0x9,
        "いやいや、とんでもありません。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x15,
        "#06202Fふふっ、どうかお気をつけて。\x02",
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    OP_68(-940, 1450, -2690, 2000)
    MoveCamera(38, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14480, 2000)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 44)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 45)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 46)
    Sleep(300)
    BeginChrThread(0x14, 3, 0, 46)
    Sleep(700)

    def lambda_8EF3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8EF3)
    WaitChrThread(0x14, 3)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A3, 0x15, 500)
    Sleep(300)

    #C0386
    ChrTalk(
        0x1A3,
        (
            "#12P#04605Fあ、ねえねえお姉さん。\x02\x03",

            "#04602Fお姉さんのこと、\x01",
            "リーシャって呼んでいいかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0387
    ChrTalk(
        0x15,
        (
            "#5P#06205Fあ……\x02\x03",

            "#06202F……ええ。\x01",
            "もちろん構いませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x1A3,
        (
            "#12P#04609Fふふっ、ありがとリーシャ。\x02\x03",

            "#04600Fそれじゃあ、まったねー！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1A3, 3, 0, 47)
    WaitChrThread(0x1A3, 3)
    Sleep(500)
    Sound(107, 0, 100, 0)
    OP_68(-700, 1450, 80, 3000)
    SetCameraDistance(13480, 3000)
    OP_6F(0x1)
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x15)
    OP_C9(0x0, 0x80000000)

    #C0389
    ChrTalk(
        0x15,
        (
            "#06203F#3243V（ランディさんの従妹……）\x02\x03",

            "#06201F#3244V（……あれが噂の\x01",
            "  《血染めの#9R ブラッディ#シャーリィ》……）\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCAC)
    OP_C9(0x1, 0x80000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("c1040", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_43_8637 end

    def Function_44_9117(): pass

    label("Function_44_9117")


    def lambda_911C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_911C)
    Sleep(800)

    def lambda_9139():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9139)
    Return()

    # Function_44_9117 end

    def Function_45_9146(): pass

    label("Function_45_9146")


    def lambda_914B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_914B)
    Sleep(1500)

    def lambda_9168():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9168)
    Return()

    # Function_45_9146 end

    def Function_46_9175(): pass

    label("Function_46_9175")


    def lambda_917A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_917A)
    Sleep(2000)

    def lambda_9197():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9197)
    Return()

    # Function_46_9175 end

    def Function_47_91A4(): pass

    label("Function_47_91A4")


    def lambda_91A9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91A9)
    Sleep(500)

    def lambda_91C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_91C6)
    Return()

    # Function_47_91A4 end

    def Function_48_91D3(): pass

    label("Function_48_91D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-480, 1500, -1260, 0)
    MoveCamera(58, 20, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(17780, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2410, 0, 4800, 360)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9430, 0)
    SetChrPos(0x104, -500, 0, -9630, 0)
    SetChrPos(0x109, 500, 0, -10630, 0)
    SetChrPos(0x105, -500, 0, -10830, 0)
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

    def lambda_92E8():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92E8)

    def lambda_9302():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9302)
    Sleep(50)

    def lambda_9316():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9316)

    def lambda_9330():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9330)
    Sleep(50)

    def lambda_9344():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9344)

    def lambda_935E():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_935E)
    Sleep(50)

    def lambda_9372():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9372)

    def lambda_938C():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_938C)
    Sleep(50)

    def lambda_93A0():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_93A0)

    def lambda_93BA():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_93BA)
    Sleep(50)

    def lambda_93CE():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_93CE)

    def lambda_93E8():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93E8)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-160, 1500, -2060, 3000)
    OP_95(0x9, 0, 0, 0, 3000, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0390
    ChrTalk(
        0x9,
        "おや、特務支援課の皆さん。\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x9,
        (
            "本日は休館日ですが、\x01",
            "何か御用でもございましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        (
            "#00000Fああいえ、ちょっと\x01",
            "立ち寄っただけなので。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#00100Fリニューアル舞台の公開……\x01",
            "いよいよ明日に迫りましたね。\x02\x03",

            "今日は、そのための\x01",
            "お休みということでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x9,
        "ええ、その通りです。\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x9,
        (
            "ただ、今も１人だけ\x01",
            "練習している者もおりますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x109,
        (
            "#10105Fへえ、熱心なんですね。\x01",
            "それってもしかして……？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "お分かりになりますか。\x01",
            "はい、シュリさんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x9,
        (
            "何と言っても、\x01",
            "明日は彼女の晴れ舞台……\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x9,
        (
            "どうやら身体を動かしていないと\x01",
            "落ち着かないみたいでしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x9,
        (
            "よろしければ、練習の様子でも\x01",
            "覗いて行ってやって下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#00005Fい、いいんですか？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x9,
        (
            "ええ、いつも懇意にさせて\x01",
            "頂いている皆さんであれば、\x01",
            "誰も文句は言いません。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x9,
        (
            "それにどうやら、\x01",
            "朝からほとんど休憩もせずに\x01",
            "根を詰めているみたいですので……\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x9,
        (
            "よろしければ、\x01",
            "お声でも掛けてあげて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x9,
        (
            "あの娘にとっても\x01",
            "良い息抜きになると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        "#00000Fなるほど、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x102,
        "#00100Fご丁寧に有難うございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 3)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, -2250, 2500, 15000, 180)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -2000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x1, 5)
    EventEnd(0x5)
    Return()

    # Function_48_91D3 end

    def Function_49_9890(): pass

    label("Function_49_9890")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -70, 2500, 15340, 180)
    EventEnd(0x5)
    Return()

    # Function_49_9890 end

    def Function_50_98B4(): pass

    label("Function_50_98B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -70, 0, -7720, 0)
    SetChrPos(0x102, -70, 0, -7720, 0)
    SetChrPos(0x109, -70, 0, -7720, 0)
    SetChrPos(0x105, -70, 0, -7720, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 4500, 0, 4500, 90)
    OP_68(0, 1750, 5000, 6000)
    MoveCamera(34, 10, 0, 6000)
    SetCameraDistance(25500, 6000)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 1050, -1700, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    def lambda_99AD():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99AD)

    def lambda_99C7():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_99C7)
    Sleep(50)

    def lambda_99DB():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_99DB)

    def lambda_99F5():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_99F5)
    Sleep(500)

    def lambda_9A09():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A09)

    def lambda_9A23():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9A23)
    Sleep(50)

    def lambda_9A37():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A37)

    def lambda_9A51():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9A51)
    WaitChrThread(0x105, 1)

    #C0408
    ChrTalk(
        0x101,
        (
            "#00005Fアルカンシェルか……\x01",
            "劇場に入るのも久しぶりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、そうね。\x01",
            "イリアさんやリーシャさんは\x01",
            "いらっしゃるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、君たちって本当に\x01",
            "有名人の知り合いが多いよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x109,
        (
            "#12P#10105Fで、でもいいんですか？\x01",
            "勝手に入っちゃって……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 500)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9B8D():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9B8D)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0412
    ChrTalk(
        0x9,
        (
            "これはこれは、特務支援課の\x01",
            "ロイド様にエリィ様ではありませんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x9,
        (
            "大変お久しぶりですね。\x01",
            "本日はどういった御用でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        (
            "#00000Fはい、実はこの度支援課の活動を\x01",
            "再開することになりまして。\x02\x03",

            "市内の様子を見回りがてら、\x01",
            "こちらにも顔を出しておこうと。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x102,
        "#00100Fご迷惑じゃなかったですか？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x9,
        (
            "ええ、もちろん迷惑だなんて\x01",
            "とんでもありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x9,
        (
            "今はちょうど休憩時間なので、\x01",
            "どうぞ挨拶されて行って下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x9,
        "イリアさんたちも喜ぶと思います。\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        "#00000Fどうもありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x109,
        "#12P#10112Fえ、えっと………\x02",
    )

    CloseMessageWindow()

    def lambda_9DC0():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DC0)
    TurnDirection(0x102, 0x109, 500)

    #C0421
    ChrTalk(
        0x102,
        "#00105Fどうかした、ノエルさん？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0422
    ChrTalk(
        0x109,
        (
            "#12P#10102Fいえ、何ていうか改めて\x01",
            "特務支援課って凄いなって。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0423
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、そうだね。\x01",
            "あのアルカンシェルを\x01",
            "まさか顔パスだなんて。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0424
    ChrTalk(
        0x101,
        (
            "#5P#00000Fはは、言われてみれば\x01",
            "確かにそうだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x102,
        "#00100Fええ、本当にありがたい縁よね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -600, 0, -2900, 0)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, -2250, 2500, 15000, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x137, 1)
    Sleep(50)
    EventEnd(0x5)
    Return()

    # Function_50_98B4 end

    def Function_51_9F3C(): pass

    label("Function_51_9F3C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1380, 1850, -1910, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15070, 0)
    SetChrPos(0xA, 740, 0, 4400, 270)
    SetChrPos(0x9, -740, 0, 4400, 90)
    SetChrPos(0x101, -500, 0, -7720, 0)
    SetChrPos(0x102, 500, 0, -7720, 0)
    SetChrPos(0x103, -500, 0, -7720, 0)
    SetChrPos(0x104, 500, 0, -7720, 0)
    SetChrPos(0xF4, -500, 0, -7720, 0)
    SetChrPos(0xF5, 500, 0, -7720, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_A063():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A063)

    def lambda_A07D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A07D)
    Sleep(100)

    def lambda_A091():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A091)

    def lambda_A0AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A0AB)
    Sleep(500)

    def lambda_A0BF():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A0BF)

    def lambda_A0D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A0D9)
    Sleep(100)
    OP_68(-970, 1450, -1300, 3000)
    MoveCamera(44, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15070, 3000)

    def lambda_A11B():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A11B)

    def lambda_A135():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A135)
    Sleep(500)

    def lambda_A149():
        OP_95(0xFE, -500, 0, -5100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A149)

    def lambda_A163():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A163)
    Sleep(100)

    def lambda_A177():
        OP_95(0xFE, 500, 0, -5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A177)

    def lambda_A191():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A191)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A1E6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A1E6)
    Sleep(50)

    def lambda_A1F6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A1F6)
    Sleep(300)

    #C0426
    ChrTalk(
        0xA,
        "#5Pああ、あなたがたは……！\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x9,
        (
            "#5P特務支援課の皆様では\x01",
            "ありませんか……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-270, 1350, 1970, 3000)
    MoveCamera(44, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13600, 3000)

    def lambda_A285():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A285)
    Sleep(50)

    def lambda_A2A2():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2A2)
    Sleep(50)

    def lambda_A2BF():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2BF)
    Sleep(50)

    def lambda_A2DC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2DC)
    Sleep(50)

    def lambda_A2F9():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A2F9)
    Sleep(50)

    def lambda_A316():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A316)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    #C0428
    ChrTalk(
        0x101,
        "#12P#00000Fお２人とも、ご無事でしたか。\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x102,
        (
            "#12P#00100Fもしかして、\x01",
            "他の方たちもこちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "はい、スタッフもアーティストも\x01",
            "皆さん一通り揃っています。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4B9")

    #C0431
    ChrTalk(
        0x9,
        (
            "ちなみに今は、新しく\x01",
            "再構成した舞台の練習に\x01",
            "一丸で取り組んでいる所でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x9,
        (
            "突然の戒厳令と外出禁止令には\x01",
            "戸惑いましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x9,
        (
            "自宅に戻るくらいなら、\x01",
            "ここで練習をしていようと\x01",
            "全員で話し合って決めたのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A557")

    label("loc_A4B9")


    #C0434
    ChrTalk(
        0x9,
        (
            "ちなみに今は、新しく\x01",
            "再構成した舞台の練習に\x01",
            "一丸で取り組んでいる所でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x9,
        (
            "このような状況とはいえ、\x01",
            "私たちに出来ることは\x01",
            "それしかありませんからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A557")


    #C0436
    ChrTalk(
        0x103,
        (
            "#12P#00204Fなるほど……\x01",
            "頭が下がります。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A822")

    #C0437
    ChrTalk(
        0x106,
        "#12P#10708F…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    #C0438
    ChrTalk(
        0xA,
        (
            "#5Pもしかして……\x01",
            "そちらにおられるのは\x01",
            "リーシャさんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x106, 500)

    #C0439
    ChrTalk(
        0x9,
        "リーシャさん……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x106,
        (
            "#12P#10706F……ご無沙汰しています。\x02\x03",

            "#10710F皆さんがご無事で何よりでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x9,
        (
            "いえ……リーシャさんも\x01",
            "よくぞ顔を見せてくれましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x9,
        (
            "色々と事情がおありなのは\x01",
            "承知していますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x9,
        (
            "宜しければ、練習の様子を\x01",
            "見て行ってあげて頂けませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x9,
        (
            "シュリさんをはじめ、皆さん全力で\x01",
            "取り組んでいらっしゃいますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x106,
        (
            "#12P#10712F#30W……………………………\x02\x03",

            "#10704Fそう……ですね……\x02\x01",

            "#10710F少し覗いていく程度なら……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    #C0446
    ChrTalk(
        0x101,
        "#5P#00002Fリーシャ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A8CD")

    label("loc_A822")


    #C0447
    ChrTalk(
        0x9,
        (
            "宜しければ、練習の様子を\x01",
            "見て行ってあげて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x9,
        (
            "シュリさんをはじめ、皆さん全力で\x01",
            "取り組んでいらっしゃいますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        "#12P#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    label("loc_A8CD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 2110, 0)
    SetScenarioFlags(0x1CF, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A92B")
    SetChrPos(0x9, 3940, 0, 2900, 90)
    Jump("loc_A93C")

    label("loc_A92B")

    SetChrPos(0x9, -2250, 2500, 15000, 180)

    label("loc_A93C")

    SetChrPos(0xA, 6970, 0, 3480, 270)
    EventEnd(0x5)
    Return()

    # Function_51_9F3C end

    def Function_52_A950(): pass

    label("Function_52_A950")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_68(-570, 1450, -4770, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16420, 0)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x109, 500, 0, -9730, 0)
    SetChrPos(0x105, -500, 0, -9930, 0)
    SetChrPos(0x9, 5120, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AA14():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA14)

    def lambda_AA2E():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA2E)
    Sleep(50)

    def lambda_AA42():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA42)

    def lambda_AA5C():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AA5C)
    Sleep(50)

    def lambda_AA70():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AA70)

    def lambda_AA8A():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AA8A)
    Sleep(50)

    def lambda_AA9E():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AA9E)

    def lambda_AAB8():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AAB8)
    OP_68(-510, 1450, -3330, 3000)
    SetCameraDistance(17420, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AB4A():

        label("loc_AB4A")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB4A")

    QueueWorkItem2(0x0, 1, lambda_AB4A)

    def lambda_AB5C():

        label("loc_AB5C")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB5C")

    QueueWorkItem2(0x1, 1, lambda_AB5C)

    def lambda_AB6E():

        label("loc_AB6E")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB6E")

    QueueWorkItem2(0x2, 1, lambda_AB6E)

    def lambda_AB80():

        label("loc_AB80")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB80")

    QueueWorkItem2(0x3, 1, lambda_AB80)
    OP_95(0x9, 0, 0, -1760, 3000, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0450
    ChrTalk(
        0x9,
        (
            "これは支援課の皆様、\x01",
            "ようこそお越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        (
            "ですが、申し訳ありません。\x01",
            "今は午後の公演に向けた\x01",
            "準備の最中でして……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x101,
        (
            "#11P#00005Fそうですか、\x01",
            "それは失礼しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x102,
        (
            "#6P#00104Fまあ用事があったわけでもないし、\x01",
            "改めて出直しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x105,
        "#12P#10300Fフフ、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x109,
        "#12P#10100Fお邪魔してすみませんでした。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x137, 0)
    SetScenarioFlags(0x22, 6)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_A950 end

    def Function_53_AD1F(): pass

    label("Function_53_AD1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1450, -6360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16420, 0)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9430, 0)
    SetChrPos(0x104, -500, 0, -9630, 0)
    SetChrPos(0x109, 500, 0, -10630, 0)
    SetChrPos(0x105, -500, 0, -10830, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x9, 5120, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AE2F():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE2F)

    def lambda_AE49():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE49)
    Sleep(50)

    def lambda_AE5D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE5D)

    def lambda_AE77():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AE77)
    Sleep(50)

    def lambda_AE8B():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AE8B)

    def lambda_AEA5():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AEA5)
    Sleep(50)

    def lambda_AEB9():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AEB9)

    def lambda_AED3():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AED3)
    Sleep(50)

    def lambda_AEE7():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AEE7)

    def lambda_AF01():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF01)
    Sleep(50)

    def lambda_AF15():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF15)

    def lambda_AF2F():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AF2F)
    OP_68(0, 1450, -4360, 3000)
    SetCameraDistance(17420, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AFED():

        label("loc_AFED")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AFED")

    QueueWorkItem2(0x0, 1, lambda_AFED)

    def lambda_AFFF():

        label("loc_AFFF")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AFFF")

    QueueWorkItem2(0x1, 1, lambda_AFFF)

    def lambda_B011():

        label("loc_B011")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B011")

    QueueWorkItem2(0x2, 1, lambda_B011)

    def lambda_B023():

        label("loc_B023")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B023")

    QueueWorkItem2(0x3, 1, lambda_B023)

    def lambda_B035():

        label("loc_B035")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B035")

    QueueWorkItem2(0x4, 1, lambda_B035)

    def lambda_B047():

        label("loc_B047")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B047")

    QueueWorkItem2(0x5, 1, lambda_B047)
    OP_95(0x9, 0, 0, -1760, 3000, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    #C0456
    ChrTalk(
        0x9,
        (
            "これは支援課の皆様、\x01",
            "ようこそお越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x9,
        (
            "ですが、申し訳ありません。\x01",
            "今はリニューアル舞台の\x01",
            "最終リハーサルの最中でして……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#00000Fそうですか、\x01",
            "確かにいよいよですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x104,
        (
            "#00306Fぜひ覗いてみてえが、\x01",
            "こればっかりはなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x103,
        (
            "#00200Fはい、迷惑にならない内に\x01",
            "引き返しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x102,
        "#00100Fお邪魔してすみませんでした。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x16D, 5)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 6)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_AD1F end

    def Function_54_B212(): pass

    label("Function_54_B212")

    EventBegin(0x1)

    #C0462
    ChrTalk(
        0x101,
        (
            "#00000Fさてと、すぐに\x01",
            "マリーを追いかけないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x1A3,
        (
            "#04600F２ＦのＳ席を調べるんだよね。\x01",
            "それじゃレッツゴー。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 48300, 0, -230, 90)
    EventEnd(0x4)
    Return()

    # Function_54_B212 end

    def Function_55_B29C(): pass

    label("Function_55_B29C")

    EventBegin(0x1)
    Sleep(50)

    #C0464
    ChrTalk(
        0x101,
        (
            "#00000Fこっちは２階の観客席だな。\x02\x03",

            "あまりウロウロすると迷惑だ。\x01",
            "立ち入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_B29C end

    def Function_56_B315(): pass

    label("Function_56_B315")

    EventBegin(0x1)
    Sleep(50)

    #C0465
    ChrTalk(
        0x101,
        (
            "#00000Fこっちは２階の観客席だな。\x02\x03",

            "あまりウロウロすると迷惑だ。\x01",
            "立ち入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_56_B315 end

    def Function_57_B38E(): pass

    label("Function_57_B38E")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B405")

    #C0466
    ChrTalk(
        0x101,
        (
            "#00000Fみんな練習に励んでいるという話だ。\x02\x03",

            "様子を窺うなら、正面の入り口から\x01",
            "ステージに入ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B467")

    label("loc_B405")


    #C0467
    ChrTalk(
        0x101,
        (
            "#00000F……今日はシュリが\x01",
            "１人で練習しているんだったな。\x02\x03",

            "楽屋の方には立ち入らないでおくか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B467")

    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_57_B38E end

    SaveToFile()

Try(main)
