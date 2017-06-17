from ScenarioHelper import *

def main():
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
        "卡雷利亚",               # 1
        "巴尔萨摩经理",           # 2
        "接待员罗兰多",           # 3
        "亚邦剧团长",             # 4
        "尤金",                   # 5
        "缇奥多尔",               # 6
        "尼克鲁",                 # 7
        "普莉埃",                 # 8
        "塞利娜",                 # 9
        "记者诺蒂亚",             # 10
        "修利",                   # 11
        "伊莉娅",                 # 12
        "玛丽",                   # 13
        "莉夏",                   # 14
        "海因兹",                 # 15
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
        "Function_8_E73",          # 08, 8
        "Function_9_1145",         # 09, 9
        "Function_10_14B9",        # 0A, 10
        "Function_11_1E58",        # 0B, 11
        "Function_12_1E5C",        # 0C, 12
        "Function_13_258D",        # 0D, 13
        "Function_14_28E0",        # 0E, 14
        "Function_15_2A1A",        # 0F, 15
        "Function_16_2B42",        # 10, 16
        "Function_17_2DF9",        # 11, 17
        "Function_18_314D",        # 12, 18
        "Function_19_3250",        # 13, 19
        "Function_20_36E2",        # 14, 20
        "Function_21_3833",        # 15, 21
        "Function_22_3A3C",        # 16, 22
        "Function_23_3BD8",        # 17, 23
        "Function_24_3FAF",        # 18, 24
        "Function_25_410C",        # 19, 25
        "Function_26_469F",        # 1A, 26
        "Function_27_4950",        # 1B, 27
        "Function_28_4BC9",        # 1C, 28
        "Function_29_4C41",        # 1D, 29
        "Function_30_4E9A",        # 1E, 30
        "Function_31_5473",        # 1F, 31
        "Function_32_5F8A",        # 20, 32
        "Function_33_5FD5",        # 21, 33
        "Function_34_6020",        # 22, 34
        "Function_35_606B",        # 23, 35
        "Function_36_60B6",        # 24, 36
        "Function_37_6101",        # 25, 37
        "Function_38_614C",        # 26, 38
        "Function_39_6183",        # 27, 39
        "Function_40_61AF",        # 28, 40
        "Function_41_72FB",        # 29, 41
        "Function_42_7346",        # 2A, 42
        "Function_43_7391",        # 2B, 43
        "Function_44_7D12",        # 2C, 44
        "Function_45_7D41",        # 2D, 45
        "Function_46_7D70",        # 2E, 46
        "Function_47_7D9F",        # 2F, 47
        "Function_48_7DCE",        # 30, 48
        "Function_49_83C5",        # 31, 49
        "Function_50_83E9",        # 32, 50
        "Function_51_89B3",        # 33, 51
        "Function_52_925F",        # 34, 52
        "Function_53_95DC",        # 35, 53
        "Function_54_9A87",        # 36, 54
        "Function_55_9AF1",        # 37, 55
        "Function_56_9B56",        # 38, 56
        "Function_57_9BBB",        # 39, 57
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
            "放置着《导力车贵族》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('高贵色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6F")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『高贵色彩』\x07\x00",
            "记下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('高贵色彩', 1)

    label("loc_E6F")

    TalkEnd(0xFF)
    Return()

    # Function_7_DE2 end

    def Function_8_E73(): pass

    label("Function_8_E73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_EF9")

    #C0003
    ChrTalk(
        0xFE,
        (
            "伊莉娅刚刚发来了\x01",
            "导力通讯，\x01",
            "为剧团的各位加油声援。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "该怎么说才好呢……伊莉娅真是\x01",
            "为我们带来了无尽的勇气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1141")

    label("loc_EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F07")
    Jump("loc_1141")

    label("loc_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F15")
    Jump("loc_1141")

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F23")
    Jump("loc_1141")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F31")
    Jump("loc_1141")

    label("loc_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F3F")
    Jump("loc_1141")

    label("loc_F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F4D")
    Jump("loc_1141")

    label("loc_F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F5B")
    Jump("loc_1141")

    label("loc_F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F69")
    Jump("loc_1141")

    label("loc_F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_110E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F84")
    Call(0, 9)
    Jump("loc_1109")

    label("loc_F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108D")

    #C0005
    ChrTalk(
        0xB,
        (
            "唔唔……我可真是的……\x01",
            "因为太过兴奋，完全没察觉到有人进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xB,
        "不过，还好是你们。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "如果被其他团员看到了……\x01",
            "我肯定会被伊莉娅狠揍一顿的。\x02",
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
    Jump("loc_1109")

    label("loc_108D")


    #C0008
    ChrTalk(
        0xFE,
        (
            "唔唔……我可真是的……\x01",
            "因为太过兴奋，完全没察觉到有人进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "如果被其他团员看到了……\x01",
            "我肯定会被伊莉娅狠揍一顿的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1109")

    Jump("loc_1141")

    label("loc_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_111C")
    Jump("loc_1141")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_112A")
    Jump("loc_1141")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1138")
    Jump("loc_1141")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1141")

    label("loc_1141")

    TalkEnd(0xFE)
    Return()

    # Function_8_E73 end

    def Function_9_1145(): pass

    label("Function_9_1145")

    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0010
    ChrTalk(
        0x8,
        (
            "那个服装的设计稿\x01",
            "已经基本完成了……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "这种式样如何？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "嗯，不错啊！\x01",
            "我认为大方向\x01",
            "没什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "我拿去让伊莉娅看看，\x01",
            "交换一下意见，\x01",
            "然后再和你沟通吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00005F（新服装的设计稿……？）\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#00100F（……很有兴趣呢。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 0)

    #C0016
    ChrTalk(
        0x8,
        "啊，你们是……？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        "唔唔，是谁来着……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 0)

    #C0018
    ChrTalk(
        0xB,
        (
            "啊，你们……\x01",
            "………莫非听到刚才的话了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E9")

    #C0019
    ChrTalk(
        0x101,
        (
            "#00006F那个……\x01",
            "真对不起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E9")

    label("loc_12E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1317")

    #C0020
    ChrTalk(
        0x102,
        "#00106F那个……抱歉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E9")

    label("loc_1317")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")

    #C0021
    ChrTalk(
        0x103,
        "#00206F那个……很抱歉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E9")

    label("loc_1347")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137C")

    #C0022
    ChrTalk(
        0x104,
        (
            "#00306F那个……\x01",
            "呃，真抱歉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E9")

    label("loc_137C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B1")

    #C0023
    ChrTalk(
        0x109,
        (
            "#10106F那、那个……\x01",
            "对不起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E9")

    label("loc_13B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E9")

    #C0024
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，算是吧，\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E9")


    #C0025
    ChrTalk(
        0xB,
        "……呼，算了。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "总之，刚才说的那些\x01",
            "是本剧团的最高机密事项。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "你们就当自己什么都没看到，\x01",
            "什么都没听到……可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00005F好、好的……明白了。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#00106F一、一言为定。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x14B, 5)
    Return()

    # Function_9_1145 end

    def Function_10_14B9(): pass

    label("Function_10_14B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_155C")

    #C0030
    ChrTalk(
        0xFE,
        (
            "虽然克洛斯贝尔的状况\x01",
            "已经变得更加混乱……\x01",
            "但现在没时间想那些烦心事。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "我们该做的事情只有一件——\x01",
            "那就是尽到一切努力，\x01",
            "争取早日恢复演出。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E54")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1614")

    #C0032
    ChrTalk(
        0xFE,
        (
            "突然下达的戒严令和禁止外出令\x01",
            "的确是让人困惑……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "但经过集体商讨之后，\x01",
            "大家都认为与其回家，\x01",
            "不如在这里一起练习。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "而且，大家现在练习的\x01",
            "注意力还惊人地集中呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E54")

    label("loc_1614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B0")

    #C0035
    ChrTalk(
        0xFE,
        (
            "今天由卡雷利亚小姐\x01",
            "去伊莉娅小姐的病房探视。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐好像\x01",
            "还是没有苏醒……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "但剧团的所有成员\x01",
            "都坚信她一定会醒来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1700")

    label("loc_16B0")


    #C0038
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐好像\x01",
            "还是没有苏醒……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "但剧团的所有成员\x01",
            "都坚信她一定会醒来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1700")

    Jump("loc_1E54")

    label("loc_1705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C6")

    #C0040
    ChrTalk(
        0x9,
        "啊，各位……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00005F那个………\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#00105F各位团员都在这里……？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "是的，所有团员都会\x01",
            "每天来这里报到。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "不过，自从那天之后，\x01",
            "莉夏就再也没有出现过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00203F是吗……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "顺便一说，我们采取轮班制，\x01",
            "每天都有团员去医院病房\x01",
            "探望伊莉娅小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "今天一整天，会由修利\x01",
            "在病房陪伴她。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186C")

    #C0048
    ChrTalk(
        0x109,
        "#10105F修利她……\x02",
    )

    CloseMessageWindow()
    Jump("loc_189F")

    label("loc_186C")


    #C0049
    ChrTalk(
        0x109,
        "#10100F嗯……我们之前见过她了。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "是吗……\x02",
    )

    CloseMessageWindow()

    label("loc_189F")


    #C0051
    ChrTalk(
        0x9,
        (
            "……说起来，\x01",
            "我到现在还无法相信呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "总觉得只是做了一场很长的梦\x01",
            "而已……但这么想也没有用啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#00303F经理……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "……说了些乱七八糟的话，\x01",
            "真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "总之，如果有需要，\x01",
            "各位可以自由\x01",
            "出入本剧场。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "如果以后有什么事情，\x01",
            "随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00003F……多谢关照。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 4)
    SetScenarioFlags(0x18C, 7)
    Jump("loc_1A18")

    label("loc_19C6")


    #C0058
    ChrTalk(
        0xFE,
        (
            "今天由修利在病房\x01",
            "陪伴伊莉娅小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "真希望伊莉娅小姐\x01",
            "能早日恢复意识啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A18")

    Jump("loc_1E54")

    label("loc_1A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1AA5")

    #C0060
    ChrTalk(
        0xFE,
        (
            "今天下午，\x01",
            "『金之太阳、银之月』的新版\x01",
            "终于要首次公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "舞台已经准备得非常完善……\x01",
            "相信表演一定能让\x01",
            "大家满足。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E54")

    label("loc_1AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B99")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B10")

    #C0062
    ChrTalk(
        0xFE,
        (
            "如果方便，希望大家\x01",
            "去和修利打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "这样也能让那孩子\x01",
            "稍微歇息一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1B10")


    #C0064
    ChrTalk(
        0xFE,
        (
            "修利虽然是瞒着伊莉娅\x01",
            "从家里出来的……\x01",
            "但她的目的地实在是显而易见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "呵呵，话说回来，\x01",
            "伊莉娅小姐对修利\x01",
            "还真是放心不下呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B94")

    Jump("loc_1E54")

    label("loc_1B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1BA7")
    Jump("loc_1E54")

    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BB5")
    Jump("loc_1E54")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C73")

    #C0066
    ChrTalk(
        0xFE,
        (
            "三天之后，就是新版舞剧\x01",
            "的公演日了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "我们明天准备花一整天时间\x01",
            "来进行最终的\x01",
            "模拟彩排。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "到时候，除了剧团人员之外，\x01",
            "其他人全都不得进入，\x01",
            "还望大家理解。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CED")

    label("loc_1C73")


    #C0069
    ChrTalk(
        0xFE,
        (
            "我们明天准备花一整天时间\x01",
            "来进行最终的\x01",
            "模拟彩排。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "到时候，除了剧团人员之外，\x01",
            "其他人全都不得进入，\x01",
            "还望大家理解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CED")

    Jump("loc_1E54")

    label("loc_1CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D7C")

    #C0071
    ChrTalk(
        0xFE,
        (
            "昨天的表演非常成功，\x01",
            "完成度要比以往更高，\x01",
            "剧团长也很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "首脑们都露出了一副\x01",
            "十分满意的表情，\x01",
            "这真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E54")

    label("loc_1D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D8A")
    Jump("loc_1E54")

    label("loc_1D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DEB")

    #C0073
    ChrTalk(
        0xFE,
        (
            "哦，各位，\x01",
            "欢迎来访。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐、\x01",
            "剧团长和莉夏小姐三人\x01",
            "现在正在舞台呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E54")

    label("loc_1DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1DF9")
    Jump("loc_1E54")

    label("loc_1DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E54")

    #C0075
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐和莉夏小姐\x01",
            "现在应该在大厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "各位如果愿意，\x01",
            "可以去见见她们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E54")

    TalkEnd(0xFE)
    Return()

    # Function_10_14B9 end

    def Function_11_1E58(): pass

    label("Function_11_1E58")

    Call(0, 12)
    Return()

    # Function_11_1E58 end

    def Function_12_1E5C(): pass

    label("Function_12_1E5C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EDC")

    #C0077
    ChrTalk(
        0xA,
        (
            "虽然现在的情况还是很混乱……\x01",
            "但已经能陆续与各地\x01",
            "取得联络了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "总之，当务之急还是\x01",
            "尽可能地收集情报啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_1EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2043")

    #C0079
    ChrTalk(
        0xA,
        (
            "国防军成立之后，\x01",
            "政府马上便要求我们\x01",
            "举办面向市民的特别公演……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "但由于演员不足，\x01",
            "无法立刻演出，\x01",
            "我们要求延后一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "自那之后，剧团长\x01",
            "一个人编写脚本，\x01",
            "而大家一直努力练习到了今天……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "以目前的形势来看，\x01",
            "由政府主导的公演\x01",
            "已经不可能照常举办了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "不过，无论是怎样的形式也好，\x01",
            "我们一定要努力使\x01",
            "再次公演成为现实。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_20C9")

    label("loc_2043")


    #C0084
    ChrTalk(
        0xA,
        (
            "以目前的形势来看，\x01",
            "由政府主导的公演\x01",
            "已经不可能照常举办了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "不过，无论是怎样的形式也好，\x01",
            "我们一定要努力使\x01",
            "再次公演成为现实。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C9")

    Jump("loc_2589")

    label("loc_20CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2191")

    #C0086
    ChrTalk(
        0xA,
        (
            "……克洛斯贝尔目前\x01",
            "正处在很关键的局面，\x01",
            "而我们该做的事情只有一件。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        (
            "那就是坚信伊莉娅小姐可以完全恢复，\x01",
            "并继续坚持练习……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "我也会倾尽全力，\x01",
            "做好辅助工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_220A")

    label("loc_2191")


    #C0089
    ChrTalk(
        0xA,
        (
            "我们该做的事情只有一件，\x01",
            "那就是坚信伊莉娅小姐可以完全恢复，\x01",
            "并继续坚持练习……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "我也会倾尽全力，\x01",
            "做好辅助工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220A")

    Jump("loc_2589")

    label("loc_220F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B0")

    #C0091
    ChrTalk(
        0xA,
        (
            "那个红发少女\x01",
            "究竟是什么人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "还有，莉夏小姐\x01",
            "到底去哪里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "总之……\x01",
            "所有的事情都让人摸不清头脑，\x01",
            "已经完全混乱了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22FA")

    label("loc_22B0")


    #C0094
    ChrTalk(
        0xA,
        (
            "那个红发少女\x01",
            "究竟是什么人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "还有，莉夏小姐\x01",
            "到底去哪里了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22FA")

    Jump("loc_2589")

    label("loc_22FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2359")

    #C0096
    ChrTalk(
        0xA,
        (
            "终于要迎来\x01",
            "新版舞剧的公演日了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "总之，先祈祷这次公演\x01",
            "顺利成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_2359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2367")
    Jump("loc_2589")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2375")
    Jump("loc_2589")

    label("loc_2375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2383")
    Jump("loc_2589")

    label("loc_2383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23F4")

    #C0098
    ChrTalk(
        0xA,
        (
            "公演日已经\x01",
            "近在眼前了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "演员们自不必说，\x01",
            "连包含我在内的全体工作人员们\x01",
            "也都情绪高涨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_23F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2486")

    #C0100
    ChrTalk(
        0xA,
        (
            "利贝尔的科洛蒂娅殿下\x01",
            "在昨晚离去的时候，\x01",
            "还当面向我表达了谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "竟然还特意和我这种\x01",
            "工作人员打招呼，\x01",
            "真是个温和善良的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_2486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2494")
    Jump("loc_2589")

    label("loc_2494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_251F")

    #C0102
    ChrTalk(
        0xA,
        (
            "『西塞姆里亚通商会议』……\x01",
            "终于要在明天开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "这种规模的国际会议\x01",
            "是非常少有的。\x01",
            "不知为何，连我都紧张起来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_251F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_252D")
    Jump("loc_2589")

    label("loc_252D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2589")

    #C0104
    ChrTalk(
        0xA,
        (
            "各位，欢迎光临\x01",
            "彩虹剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "如果对本剧场\x01",
            "有什么不明之处，\x01",
            "请尽管向我咨询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2589")

    TalkEnd(0xA)
    Return()

    # Function_12_1E5C end

    def Function_13_258D(): pass

    label("Function_13_258D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_259E")
    Jump("loc_28C2")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A9")

    #C0106
    ChrTalk(
        0xFE,
        "伊莉娅小姐……好伟大啊。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "毫不迟疑地护住了修利……\x01",
            "虽然自己受了伤，但看到修利\x01",
            "平安无事时，却还是那么欣喜。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        "而且，直到最后都还挂念着表演……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "只要我们能做得到，\x01",
            "无论让我们做什么都可以……\x01",
            "但在这种时候，我们又能做些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2722")

    label("loc_26A9")


    #C0110
    ChrTalk(
        0xFE,
        (
            "只要我们能做得到，\x01",
            "无论让我们做什么都可以……\x01",
            "但在这种时候，我们又能做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "可恶……\x01",
            "无论如何都想不出啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2722")

    Jump("loc_28C2")

    label("loc_2727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2735")
    Jump("loc_28C2")

    label("loc_2735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2743")
    Jump("loc_28C2")

    label("loc_2743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2751")
    Jump("loc_28C2")

    label("loc_2751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_275F")
    Jump("loc_28C2")

    label("loc_275F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277A")
    Call(0, 14)
    Jump("loc_27B6")

    label("loc_277A")


    #C0112
    ChrTalk(
        0xFE,
        "呜呜，总觉得好紧张啊……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "感觉比正式表演时还紧张。\x02",
    )

    CloseMessageWindow()

    label("loc_27B6")

    Jump("loc_28C2")

    label("loc_27BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27C9")
    Jump("loc_28C2")

    label("loc_27C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27D7")
    Jump("loc_28C2")

    label("loc_27D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_284E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F2")
    Call(0, 15)
    Jump("loc_2849")

    label("loc_27F2")


    #C0114
    ChrTalk(
        0xC,
        (
            "呼，稍微做了一些\x01",
            "激烈动作，\x01",
            "马上就变成这样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "必须要赶快和\x01",
            "卡雷利亚小姐说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2849")

    Jump("loc_28C2")

    label("loc_284E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_285C")
    Jump("loc_28C2")

    label("loc_285C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2877")
    Call(0, 16)
    Jump("loc_28C2")

    label("loc_2877")


    #C0116
    ChrTalk(
        0xC,
        (
            "草食系男子……？\x01",
            "就是那种单纯温厚的？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        "哼，扮演那种角色很简单啊。\x02",
    )

    CloseMessageWindow()

    label("loc_28C2")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_28DF")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_28DF")

    Return()

    # Function_13_258D end

    def Function_14_28E0(): pass

    label("Function_14_28E0")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0118
    ChrTalk(
        0xF,
        (
            "嗯～加雷利亚是不是\x01",
            "跑到什么地方偷懒去了？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xF,
        "好吧，既然这样……\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x0)

    #C0120
    ChrTalk(
        0xF,
        (
            "尤金，有件事情\x01",
            "想拜托你……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x13B, 0x0)

    #C0121
    ChrTalk(
        0xC,
        "什么事？普莉埃小姐。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xF,
        (
            "我衣服上的带子稍微\x01",
            "有点松了～\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xF,
        (
            "自己又够不到。\x01",
            "来帮我一下⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0124
    ChrTalk(
        0xC,
        "真、真的要我来吗？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x16D, 4)
    Return()

    # Function_14_28E0 end

    def Function_15_2A1A(): pass

    label("Function_15_2A1A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0125
    ChrTalk(
        0xC,
        (
            "哎～话说回来，我的舞台形象\x01",
            "还是如此罪孽深重啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "这副威风凛凛的形姿……\x01",
            "似乎又要使崇拜者的数量增加了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        "……先别说这些，尤金。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "你肩部的线\x01",
            "又崩开了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0129
    ChrTalk(
        0xC,
        (
            "唔，真的……\x01",
            "必须要赶快和卡雷利亚小姐说。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xD,
        "哼，这是什么王子啊。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_15_2A1A end

    def Function_16_2B42(): pass

    label("Function_16_2B42")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE0")

    #C0131
    ChrTalk(
        0xC,
        (
            "话说回来，尼克鲁那家伙\x01",
            "似乎完全恢复原样了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xD,
        (
            "嗯，而且那家伙已经开始\x01",
            "踏踏实实地努力提高自己的水平了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        "如果不努力，你可就要被他超越了哦。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        "哼，你在和谁说话啊。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "想超越我这个『彩虹剧团的王子』？\x01",
            "哪有那么容易。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        (
            "……最近，像尼克鲁这种\x01",
            "所谓的什么草食系男子\x01",
            "好像在一部分群体之中很受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xD,
        (
            "据罗兰德说，\x01",
            "写给尼克鲁的崇拜者来信\x01",
            "在这一阵子增加了很多。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0138
    ChrTalk(
        0xC,
        "真、真的吗？到底有多少……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xD,
        (
            "呵呵，谁知道，\x01",
            "不然去问问他本人如何？\x02",
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
            "……缇奥多尔，将那什么草食系男子\x01",
            "的必需要素详细介绍给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        "我会用一周时间去掌握。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0142
    ChrTalk(
        0xD,
        "……问题的重点并不在这里吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 3)

    label("loc_2DE0")

    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_16_2B42 end

    def Function_17_2DF9(): pass

    label("Function_17_2DF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E0A")
    Jump("loc_3149")

    label("loc_2E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2EAD")

    #C0143
    ChrTalk(
        0xFE,
        (
            "最近，修利表演时\x01",
            "充满感情，\x01",
            "十分精彩。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "演技就不用说了，更重要的是，\x01",
            "她的表演充满感染力，能吸引住观赏者的心。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "……我们也不能输给她啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3149")

    label("loc_2EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2EBB")
    Jump("loc_3149")

    label("loc_2EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5A")

    #C0146
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "莉夏到底是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "她好像有什么事情瞒着我们……\x01",
            "不过，她是我们的伙伴。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "我相信她\x01",
            "不会就这么\x01",
            "一走了之……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2F9D")

    label("loc_2F5A")


    #C0149
    ChrTalk(
        0xFE,
        (
            "……莉夏到底是\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "我相信她\x01",
            "不会就这么\x01",
            "一走了之……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9D")

    Jump("loc_3149")

    label("loc_2FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FB0")
    Jump("loc_3149")

    label("loc_2FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FBE")
    Jump("loc_3149")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FCC")
    Jump("loc_3149")

    label("loc_2FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FDA")
    Jump("loc_3149")

    label("loc_2FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF5")
    Call(0, 18)
    Jump("loc_3053")

    label("loc_2FF5")


    #C0151
    ChrTalk(
        0xFE,
        (
            "……自己的问题，最后也只有\x01",
            "靠自己找到答案才能解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐大概\x01",
            "也很为她着急吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3053")

    Jump("loc_3149")

    label("loc_3058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3066")
    Jump("loc_3149")

    label("loc_3066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3074")
    Jump("loc_3149")

    label("loc_3074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_30C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308F")
    Call(0, 15)
    Jump("loc_30BF")

    label("loc_308F")


    #C0153
    ChrTalk(
        0xFE,
        (
            "……好，服装\x01",
            "已经换完了，\x01",
            "得赶快去练习了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30BF")

    Jump("loc_3149")

    label("loc_30C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_30D2")
    Jump("loc_3149")

    label("loc_30D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30ED")
    Call(0, 16)
    Jump("loc_3149")

    label("loc_30ED")


    #C0154
    ChrTalk(
        0xD,
        (
            "……看来我的\x01",
            "煽动方式好像不太对啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xD,
        (
            "算啦，说不定在某种意义上，\x01",
            "这也算是有效果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3149")

    TalkEnd(0xFE)
    Return()

    # Function_17_2DF9 end

    def Function_18_314D(): pass

    label("Function_18_314D")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0156
    ChrTalk(
        0xE,
        (
            "修利那家伙……\x01",
            "好像非常烦恼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xE,
        (
            "她似乎一直在思考\x01",
            "自己的演技有哪些不足……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        "嗯……是啊。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xD,
        (
            "但那是修利自己的问题……\x01",
            "只有她本人才能找到答案。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "……所以，\x01",
            "我们只要默默注视着她就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        "嗯……确实如此啊。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_18_314D end

    def Function_19_3250(): pass

    label("Function_19_3250")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_32BF")

    #C0162
    ChrTalk(
        0xFE,
        (
            "能听到伊莉娅那充满活力的声音，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "伊莉娅就是伊莉娅啊～\x01",
            "我们也必须要加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C4")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_337F")

    #C0164
    ChrTalk(
        0xFE,
        (
            "舞姬角色的重担都压在了修利\x01",
            "一个人身上，但她并没有被压力击垮，\x01",
            "非常努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "修利肯定是觉得只有在舞台上努力\x01",
            "才是报答伊莉娅的最好方式……\x01",
            "虽然她没有说出口，但我很清楚呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C4")

    label("loc_337F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_338D")
    Jump("loc_36C4")

    label("loc_338D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_344A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3400")

    #C0166
    ChrTalk(
        0xFE,
        (
            "在平时，现在应该是\x01",
            "练歌的时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "……呼………………\x01",
            "但实在是没有那种心情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3445")

    label("loc_3400")


    #C0168
    ChrTalk(
        0xFE,
        (
            "伊莉娅竟然会遭遇到\x01",
            "那种事情…………\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "……简直让人不敢相信。\x02",
    )

    CloseMessageWindow()

    label("loc_3445")

    Jump("loc_36C4")

    label("loc_344A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C5")

    #C0170
    ChrTalk(
        0xFE,
        (
            "啊～啊～啊～\x01",
            "嗯，今天的嗓音也很不错呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "在正式表演开始前，就戴上口罩，\x01",
            "保护好嗓子吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_34FC")

    label("loc_34C5")


    #C0172
    ChrTalk(
        0xFE,
        (
            "对歌姬来说，嗓子可是最重要的～\x01",
            "再吃一块润喉糖吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FC")

    Jump("loc_36C4")

    label("loc_3501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_350F")
    Jump("loc_36C4")

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_351D")
    Jump("loc_36C4")

    label("loc_351D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_352B")
    Jump("loc_36C4")

    label("loc_352B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3546")
    Call(0, 14)
    Jump("loc_358B")

    label("loc_3546")


    #C0173
    ChrTalk(
        0xFE,
        (
            "呵呵，没想到尤金\x01",
            "意外地单纯呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "连姐姐我都有点不好意思了。\x02",
    )

    CloseMessageWindow()

    label("loc_358B")

    Jump("loc_36C4")

    label("loc_3590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AB")
    Call(0, 20)
    Jump("loc_3612")

    label("loc_35AB")


    #C0175
    ChrTalk(
        0xFE,
        (
            "嗯～他们都是\x01",
            "极其有名的人士，\x01",
            "这我还是知道的。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "但那么多人聚集在一起，\x01",
            "实在是难以一一辨别啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3612")

    Jump("loc_36C4")

    label("loc_3617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3625")
    Jump("loc_36C4")

    label("loc_3625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_367A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3640")
    Call(0, 21)
    Jump("loc_3675")

    label("loc_3640")


    #C0177
    ChrTalk(
        0xFE,
        "唔～好遗憾。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "莉夏给我的煎饼\x01",
            "真的很好吃啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3675")

    Jump("loc_36C4")

    label("loc_367A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3688")
    Jump("loc_36C4")

    label("loc_3688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_36C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A3")
    Call(0, 22)
    Jump("loc_36C4")

    label("loc_36A3")


    #C0179
    ChrTalk(
        0xFE,
        (
            "（嚼）……\x01",
            "啊～好·幸·福⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C4")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_36E1")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_36E1")

    Return()

    # Function_19_3250 end

    def Function_20_36E2(): pass

    label("Function_20_36E2")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0180
    ChrTalk(
        0x10,
        (
            "……昨天的观众阵容\x01",
            "简直让人窒息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x10,
        (
            "奥斯本宰相、\x01",
            "奥利维特皇子……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x10,
        (
            "洛克史密斯总统和\x01",
            "阿尔伯特大公……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x10,
        (
            "科洛蒂娅和\x01",
            "尤莉亚准校……\x01",
            "另外还有……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xF,
        (
            "呵呵，塞利娜了解得\x01",
            "很清楚嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xF,
        (
            "我直到最后\x01",
            "都分不清\x01",
            "谁是谁呢。\x02",
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
            "呜呜……真羡慕普莉埃小姐\x01",
            "这种乐天性格啊。\x02",
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

    # Function_20_36E2 end

    def Function_21_3833(): pass

    label("Function_21_3833")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0187
    ChrTalk(
        0x10,
        (
            "呜呜，虽然明天才要演出……\x01",
            "但现在就很紧张了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "呼，毕竟这次前来观剧的\x01",
            "可不是一般的宾客啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "不过，你至今为止跨越了无数挑战，\x01",
            "才走到了这一步。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        "多拿出些自信来吧。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x10,
        "卡雷利亚小姐……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xF,
        (
            "是啊，塞利娜。\x01",
            "过度在意各种事情，\x01",
            "只会让肚子饿得更快而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xF,
        (
            "对了，要不要一起吃些点心？\x01",
            "正好莉夏给了我一些\x01",
            "东方煎饼呢。\x02",
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
            "不了，在这种时候，\x01",
            "基本上是不会想吃东西的……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "普莉埃小姐……\x01",
            "你还真是我行我素呢。\x02",
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

    # Function_21_3833 end

    def Function_22_3A3C(): pass

    label("Function_22_3A3C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0196
    ChrTalk(
        0xF,
        (
            "（嚼）……\x01",
            "呼，在练习间隙吃点心\x01",
            "真是最高享受～⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "呼～普莉埃小姐可真是的。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "要我说多少次，你才能明白呢？\x01",
            "不能把点心带进\x01",
            "衣装间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xF,
        "哎～但现在不是在休息吗？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xF,
        (
            "在练习时是不能吃点心的，\x01",
            "所以也只能趁现在吃啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "真是的……\x01",
            "简直就像个小孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#10302F（『神秘歌姬』普莉埃……\x01",
            "  竟是个如此孩子气的人啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x109,
        (
            "#10106F（确、确实、\x01",
            "  和舞台上的形象完全不同呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_22_3A3C end

    def Function_23_3BD8(): pass

    label("Function_23_3BD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C72")

    #C0204
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐的声音……\x01",
            "真是好久都没听到了。\x01",
            "她似乎很有精神，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "我们不知道那个大树是怎么回事，\x01",
            "现在能做的就是专心练习。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAB")

    label("loc_3C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C80")
    Jump("loc_3FAB")

    label("loc_3C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C8E")
    Jump("loc_3FAB")

    label("loc_3C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D04")

    #C0206
    ChrTalk(
        0xFE,
        (
            "修利那孩子……\x01",
            "肯定要比别人更加痛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "她一直都在责怪自己，\x01",
            "说伊莉娅是为了保护她才受伤的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAB")

    label("loc_3D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D12")
    Jump("loc_3FAB")

    label("loc_3D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D20")
    Jump("loc_3FAB")

    label("loc_3D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D2E")
    Jump("loc_3FAB")

    label("loc_3D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D3C")
    Jump("loc_3FAB")

    label("loc_3D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D57")
    Call(0, 24)
    Jump("loc_3D78")

    label("loc_3D57")


    #C0208
    ChrTalk(
        0xFE,
        (
            "我就是我……\x01",
            "真的是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D78")

    Jump("loc_3FAB")

    label("loc_3D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D98")
    Call(0, 20)
    Jump("loc_3DC7")

    label("loc_3D98")


    #C0209
    ChrTalk(
        0xFE,
        (
            "呜呜……真羡慕普莉埃小姐\x01",
            "这种乐天性格啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC7")

    Jump("loc_3FAB")

    label("loc_3DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3DDA")
    Jump("loc_3FAB")

    label("loc_3DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF5")
    Call(0, 21)
    Jump("loc_3E39")

    label("loc_3DF5")


    #C0210
    ChrTalk(
        0xFE,
        (
            "看到普莉埃小姐的样子之后，\x01",
            "都有点不明白\x01",
            "自己为何要如此紧张了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E39")

    Jump("loc_3FAB")

    label("loc_3E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E4C")
    Jump("loc_3FAB")

    label("loc_3E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4D")

    #C0211
    ChrTalk(
        0xFE,
        (
            "缇奥多尔前辈和尤金前辈\x01",
            "总是形影不离啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "……好像有人说他们是ＢＬ吧？\x01",
            "支持者的想象也未必就没有道理……\x02",
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
            "……真是的，我到底\x01",
            "在想些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "好了，虽然只有这点时间，\x01",
            "但也要充分用于演技练习。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3FAB")

    label("loc_3F4D")


    #C0215
    ChrTalk(
        0xFE,
        (
            "……真是的，我到底\x01",
            "在想些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "好了，虽然只有这点时间，\x01",
            "但也要充分用于演技练习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FAB")

    TalkEnd(0xFE)
    Return()

    # Function_23_3BD8 end

    def Function_24_3FAF(): pass

    label("Function_24_3FAF")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0217
    ChrTalk(
        0x10,
        "呼……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x10,
        (
            "尼克鲁都可以担任重要配角，\x01",
            "而我却……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "你在说什么啊，\x01",
            "塞利娜小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "在这次的表演中，\x01",
            "你的出场机会不是增加了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x10,
        "但和其他人相比……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "真是的，为什么非要\x01",
            "和其他人比来比去呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "你就是你，在这个剧团里，\x01",
            "你是独一无二的。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "好啦，笑一个吧。\x01",
            "那么用心地化了妆，\x01",
            "总板着脸岂不是太可惜了嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_24_3FAF end

    def Function_25_410C(): pass

    label("Function_25_410C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4175")

    #C0225
    ChrTalk(
        0xFE,
        (
            "我正在检查\x01",
            "伊莉娅小姐的服装。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "让她无论何时归来都能穿得合身，\x01",
            "可是我的工作呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469B")

    label("loc_4175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_41E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4190")
    Call(0, 26)
    Jump("loc_41E0")

    label("loc_4190")


    #C0227
    ChrTalk(
        0xFE,
        (
            "呵呵，仔细想想，\x01",
            "修利还处在\x01",
            "成长期呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "真是越来越期待她今后的表现了。\x02",
    )

    CloseMessageWindow()

    label("loc_41E0")

    Jump("loc_469B")

    label("loc_41E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_41F3")
    Jump("loc_469B")

    label("loc_41F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A8")

    #C0229
    ChrTalk(
        0xFE,
        (
            "……现在回想起那天的事情，\x01",
            "我仍然会觉得很害怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐的服装\x01",
            "被鲜血染红……\x01",
            "真是惨不忍睹。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "呜呜，伊莉娅小姐……\x01",
            "为什么会遭遇那种事呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_430E")

    label("loc_42A8")


    #C0232
    ChrTalk(
        0xFE,
        (
            "……现在回想起那天的事情，\x01",
            "我仍然会觉得很害怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "呜呜，伊莉娅小姐……\x01",
            "为什么会遭遇那种事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_430E")

    Jump("loc_469B")

    label("loc_4313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4382")

    #C0234
    ChrTalk(
        0xFE,
        (
            "呵呵，普莉埃小姐\x01",
            "总是这么我行我素呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "塞利娜小姐\x01",
            "今天早上也很有精神，\x01",
            "应该可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469B")

    label("loc_4382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4390")
    Jump("loc_469B")

    label("loc_4390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_439E")
    Jump("loc_469B")

    label("loc_439E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_43AC")
    Jump("loc_469B")

    label("loc_43AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C7")
    Call(0, 24)
    Jump("loc_441E")

    label("loc_43C7")


    #C0236
    ChrTalk(
        0xFE,
        (
            "塞利娜小姐\x01",
            "好像很烦恼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "想想她现在的心情，\x01",
            "这也难怪……\x01",
            "希望她能振作起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_441E")

    Jump("loc_469B")

    label("loc_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4575")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443E")
    Call(0, 9)
    Jump("loc_4570")

    label("loc_443E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F1")

    #C0238
    ChrTalk(
        0xFE,
        "那个……各位，真是不好意思。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "关于新版舞剧的详细情况，\x01",
            "现在还没有向伊莉娅小姐\x01",
            "之外的演员透露……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "所以，不管各位在这里看到了什么，\x01",
            "都请暂时保密哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4570")

    label("loc_44F1")


    #C0241
    ChrTalk(
        0xFE,
        (
            "关于新版舞剧的详细情况，\x01",
            "现在还没有向伊莉娅小姐\x01",
            "之外的演员透露……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "所以，不管各位在这里看到了什么，\x01",
            "都请暂时保密哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4570")

    Jump("loc_469B")

    label("loc_4575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4583")
    Jump("loc_469B")

    label("loc_4583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_461D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459E")
    Call(0, 21)
    Jump("loc_4618")

    label("loc_459E")


    #C0243
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐自不用说，\x01",
            "普莉埃小姐也是个\x01",
            "不知道何为紧张的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "她们那种心理素质，\x01",
            "要是能分些\x01",
            "给塞利娜小姐就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4618")

    Jump("loc_469B")

    label("loc_461D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_462B")
    Jump("loc_469B")

    label("loc_462B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_469B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4646")
    Call(0, 22)
    Jump("loc_469B")

    label("loc_4646")


    #C0245
    ChrTalk(
        0xFE,
        (
            "呼，总之，\x01",
            "我还得趁休息时间\x01",
            "整理一下服装呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "就不阻止你了，\x01",
            "你快点吃光吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_469B")

    TalkEnd(0xFE)
    Return()

    # Function_25_410C end

    def Function_26_469F(): pass

    label("Function_26_469F")

    OP_4B(0x12, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x8,
        (
            "啊，修利……\x01",
            "你又长高了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x12,
        "#12205F哎，这是怎么看出来的？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "呵呵，可别小看\x01",
            "服装人员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        (
            "看一下你换了衣服之后的样子，\x01",
            "我马上就会知道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "不过，\x01",
            "变化倒也没大到\x01",
            "需要修改尺寸。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x12,
        (
            "#12202F原来如此……\x01",
            "卡雷利亚小姐好厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "呵呵，仔细想想，\x01",
            "修利还处在\x01",
            "成长期呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x8,
        (
            "今后也要稍微多吃些，\x01",
            "努力练习哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x12,
        (
            "#12206F嗯、嗯……\x01",
            "谢谢您，卡雷利亚小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#00000F（虽然现在是如此状况……\x01",
            "  但总觉得很温暖呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48DB")

    #C0257
    ChrTalk(
        0x106,
        (
            "#10702F（呵呵，是啊。）\x02\x03",

            "#10704F（该怎么说呢，这个剧场里\x01",
            "  就像是一个独立的世界。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_493A")

    label("loc_48DB")


    #C0258
    ChrTalk(
        0x102,
        (
            "#00100F（呵呵，的确如此呢。）\x02\x03",

            "#00104F（该怎么说呢，这个剧场里\x01",
            "  就像是一个独立的世界。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_493A")

    SetScenarioFlags(0x1, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_26_469F end

    def Function_27_4950(): pass

    label("Function_27_4950")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3F")

    #C0259
    ChrTalk(
        0xFE,
        (
            "无论发生了什么，\x01",
            "也要全力磨练演技……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "只要这样想，\x01",
            "不安的心情就会\x01",
            "奇迹般地消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "不过，我能说出这种大道理，\x01",
            "全是受了伊莉娅小姐的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "只要听到她的话语，\x01",
            "就会觉得身体中涌现出了无穷力量。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4A9C")

    label("loc_4A3F")


    #C0263
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐\x01",
            "简直像太阳一般呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "光凭言语，\x01",
            "就能使他人产生如此力量……\x01",
            "真是太厉害了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9C")

    Jump("loc_4BC5")

    label("loc_4AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4AAF")
    Jump("loc_4BC5")

    label("loc_4AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4ABD")
    Jump("loc_4BC5")

    label("loc_4ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B3F")

    #C0265
    ChrTalk(
        0xFE,
        (
            "在这种时候……如果伊莉娅小姐在的话，\x01",
            "会怎样激励我们呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "我也知道现在必须\x01",
            "要振作起来……可是……可是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BC5")

    label("loc_4B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B5A")
    Call(0, 18)
    Jump("loc_4BC5")

    label("loc_4B5A")


    #C0267
    ChrTalk(
        0xFE,
        (
            "修利那家伙\x01",
            "好像相当烦恼呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "自己的问题要靠自己解决吗……\x01",
            "……缇奥多尔前辈说的话\x01",
            "相当有深意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BC5")

    TalkEnd(0xFE)
    Return()

    # Function_27_4950 end

    def Function_28_4BC9(): pass

    label("Function_28_4BC9")

    TalkBegin(0xFE)

    #C0269
    ChrTalk(
        0xFE,
        (
            "呵呵，在开场之前入内\x01",
            "是记者的特权啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "虽然也很在意矿山镇的事情，\x01",
            "但现在还是集中精神，\x01",
            "采访彩虹剧团吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_4BC9 end

    def Function_29_4C41(): pass

    label("Function_29_4C41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C5F")
    Call(0, 26)
    Jump("loc_4E96")

    label("loc_4C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DB6")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D45")
    TurnDirection(0x12, 0x106, 500)

    #C0271
    ChrTalk(
        0x12,
        (
            "#12201F莉夏姐……\x01",
            "突击作战的时候\x01",
            "一定要小心啊。\x02\x03",

            "#12203F虽然我什么忙都帮不上，\x01",
            "但一定会在这里\x01",
            "拼命练习的……\x02\x03",

            "#12201F所以……莉夏姐，\x01",
            "你们也要全力加油。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x106,
        (
            "#10702F修利……\x01",
            "嗯，我明白！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAE")

    label("loc_4D45")


    #C0273
    ChrTalk(
        0x12,
        (
            "#12200F各位……\x01",
            "突击作战的时候\x01",
            "一定要小心啊。\x02\x03",

            "还有，莉夏姐就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#00002F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_4DAE")

    SetScenarioFlags(0x1, 3)
    Jump("loc_4E96")

    label("loc_4DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E3F")
    TurnDirection(0x12, 0x106, 500)

    #C0275
    ChrTalk(
        0x12,
        (
            "#12203F虽然我什么忙都帮不上，\x01",
            "但一定会在这里\x01",
            "拼命练习的……\x02\x03",

            "#12202F所以……莉夏姐，\x01",
            "你们也要全力加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E96")

    label("loc_4E3F")


    #C0276
    ChrTalk(
        0x12,
        (
            "#12200F各位……\x01",
            "突击作战的时候\x01",
            "一定要小心啊。\x02\x03",

            "#12203F还有，莉夏姐就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E96")

    TalkEnd(0xFE)
    Return()

    # Function_29_4C41 end

    def Function_30_4E9A(): pass

    label("Function_30_4E9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5401")

    #C0277
    ChrTalk(
        0x13,
        "#01700F啊，这不是警察弟弟吗。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x13,
        (
            "#01700F还有缇欧也在。\x01",
            "呵呵，真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        "#00202F是的，久疏问候了。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x13,
        (
            "#01700F这样一来，支援科的成员\x01",
            "总算是凑齐了啊。\x02\x03",

            "#01704F和以前相比，\x01",
            "大家似乎都有了\x01",
            "一定的成长……\x02\x03",

            "#01709F我们彩虹剧团\x01",
            "也不会输给你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        "#00000F哈哈，被如此夸奖，真是荣幸。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x104,
        (
            "#00305F不过，该怎么说才好呢……\x01",
            "总觉得你们今天比以往更有干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x13,
        (
            "#01703F嗯，毕竟下场演出\x01",
            "已经是新版作品公演之前\x01",
            "的最后一场公演了。\x02\x03",

            "#01700F一想到是集大成的最后演出，\x01",
            "自然就充满干劲了。\x02\x03",

            "#01706F不过莉夏今天休息，\x01",
            "真是有点遗憾呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_END)), "loc_5208")

    #C0284
    ChrTalk(
        0x109,
        (
            "#10105F对了，莉夏小姐\x01",
            "说要去市政厅\x01",
            "办些事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x13,
        (
            "#01705F哦，你们见到莉夏了吗？\x02\x03",

            "#01703F虽然最近很少那样了……\x01",
            "但那孩子之前有好几次请假\x01",
            "都是在临走之前才突然申请。\x02\x03",

            "#01709F每次我都怀疑\x01",
            "她是不是要去和男人\x01",
            "偷偷约会呢～\x02\x03",

            "#01704F哼，如果真是那样，\x01",
            "我的双手可是不会放过她的。\x01",
            "（做抓握状）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52F0")

    label("loc_5208")


    #C0286
    ChrTalk(
        0x109,
        "#10100F这样啊。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x13,
        (
            "#01703F嗯，虽然最近很少那样了……\x01",
            "但那孩子之前有好几次请假\x01",
            "都是在临走之前才突然申请。\x02\x03",

            "#01709F每次我都怀疑\x01",
            "她是不是要去和男人\x01",
            "偷偷约会呢～\x02\x03",

            "#01704F哼，如果真是那样，\x01",
            "我的双手可是不会放过她的。\x01",
            "（做抓握状）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F0")


    #C0288
    ChrTalk(
        0x102,
        "#00105F唔……（一惊）\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，你刚才好像\x01",
            "突然回想起了某个场面吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        "#00206F（艾莉前辈……）\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x13,
        (
            "#01700F算啦，先不说莉夏的事情了，\x01",
            "今天也要拼命练习才行啊。\x02\x03",

            "#01709F你们似乎也很忙呢，我们就互相加油，\x01",
            "做好各自该做的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 5)
    Jump("loc_546F")

    label("loc_5401")


    #C0293
    ChrTalk(
        0x13,
        (
            "#01704F总之，\x01",
            "今天也要拼命练习才行啊。\x02\x03",

            "#01700F你们似乎也很忙呢，我们就互相加油，\x01",
            "做好各自该做的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546F")

    TalkEnd(0xFE)
    Return()

    # Function_30_4E9A end

    def Function_31_5473(): pass

    label("Function_31_5473")

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
            "#5P哦，各位……\x01",
            "欢迎大家光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "#5P刚才突然进来一只小猫，\x01",
            "它以惊人的速度\x01",
            "冲到里面去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#12P#00006F啊，抱歉。\x02\x03",

            "#00000F其实我们正是在\x01",
            "追那只小猫。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#12P#00100F那个……\x01",
            "可以在剧场内找一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x9,
        (
            "#5P嗯，当然，\x01",
            "这也是帮了我们的忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x9,
        (
            "#5P晚上将要招待各国首脑，\x01",
            "所以本日有彩排……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#5P但现在所有\x01",
            "演员正好都在休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#12P#00000F太好了，真是个好机会。\x02\x03",

            "那我们就赶快行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        (
            "#12P#00100F顺便问一下，\x01",
            "您知道小猫跑到哪里了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        "#5P真抱歉……\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x9,
        (
            "#5P它的速度太快了，\x01",
            "而且事发突然，\x01",
            "我看得也不是很清楚……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x9,
        (
            "#5P不过，肯定是跑上\x01",
            "楼梯了。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#12P#00003F原来如此……既然这样，\x01",
            "我们还是分头搜寻为好啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0307
    ChrTalk(
        0x102,
        (
            "#6P#00100F是啊，要怎么分工呢？\x02\x03",

            "#00103F正好有三道门，\x01",
            "不然就两人一组行动吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0308
    ChrTalk(
        0x101,
        "#11P#00003F有道理啊……\x02",
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
            "#04609F那谢莉就和\x01",
            "这位小哥一起行动了⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#11P#00005F哎……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_59DD():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59DD)
    Sleep(50)

    def lambda_59ED():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59ED)
    Sleep(50)

    def lambda_59FD():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_59FD)
    Sleep(50)

    def lambda_5A0D():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5A0D)
    Sleep(50)

    def lambda_5A1D():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5A1D)
    WaitChrThread(0x104, 2)

    #C0311
    ChrTalk(
        0x102,
        "#6P#00101F等、等一下！\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x109,
        "#12P#10105F为、为什么要这样组合呢？\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x1A3,
        (
            "#04605F嗯？不为什么啊。\x02\x03",

            "#04609F啊，莫非\x01",
            "两位姐姐也想和\x01",
            "他一起行动？\x02",
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
        "#6P#00106F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x109,
        "#12P#10101F并不是这种问题……！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#6P#10309F哈哈，好像\x01",
            "越来越有趣了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0317
    ChrTalk(
        0x101,
        "#11P#00006F不要一副事不关己的口气……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        (
            "#12P#00303F……算了，既然已经一起行动这么久了，\x01",
            "她应该不会再做出奇怪的事情。\x02\x03",

            "#00301F谢莉，\x01",
            "不要对罗伊德\x01",
            "做一些奇怪的举动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1A3,
        "#04604F好啦好啦，我知道的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    #C0320
    ChrTalk(
        0x1A3,
        (
            "#04600F这位小哥虽然可爱，\x01",
            "但并不是谢莉感兴趣的类型啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#11P#00006F可爱……\x01",
            "呼，算了。\x02\x03",

            "#00000F总之，我们就分头行动，\x01",
            "在剧场内展开搜索吧。\x02\x03",

            "调查结束以后，\x01",
            "大家来大厅集合。\x02",
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
            "#6P#04602F呵呵，那我们就\x01",
            "赶快去找玛丽吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00000F嗯，当然。\x02\x03",

            "#00003F（话说回来，如此交谈的时候，\x01",
            "  感觉她只是一个天真无邪，\x01",
            "  随性开朗的女孩……）\x02\x03",

            "（但之前威胁那些公子哥时\x01",
            "  所散发出来的杀气也是实实在在的……）\x02\x03",

            "#00001F（究竟哪一面\x01",
            "  才是她的本性呢……？）\x02",
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
            "#6P#04605F哎哎，怎么了？\x02\x03",

            "#04609F难道被谢莉\x01",
            "迷住了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#00003F……才没有。\x02\x03",

            "#00000F总之，我们去调查\x01",
            "二层的Ｓ席吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x1A3,
        "#6P#04609F哈哈，好的，队长。\x02",
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

    # Function_31_5473 end

    def Function_32_5F8A(): pass

    label("Function_32_5F8A")


    def lambda_5F8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F8F)

    def lambda_5FA0():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FA0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 900, 0, -1900, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_5F8A end

    def Function_33_5FD5(): pass

    label("Function_33_5FD5")


    def lambda_5FDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5FDA)

    def lambda_5FEB():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FEB)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -900, 0, -1900, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_5FD5 end

    def Function_34_6020(): pass

    label("Function_34_6020")


    def lambda_6025():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6025)

    def lambda_6036():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6036)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -900, 0, -4300, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_6020 end

    def Function_35_606B(): pass

    label("Function_35_606B")


    def lambda_6070():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6070)

    def lambda_6081():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6081)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 0, -3100, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_35_606B end

    def Function_36_60B6(): pass

    label("Function_36_60B6")


    def lambda_60BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_60BB)

    def lambda_60CC():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_60CC)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -900, 0, -3100, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_36_60B6 end

    def Function_37_6101(): pass

    label("Function_37_6101")


    def lambda_6106():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_6106)

    def lambda_6117():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_6117)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 800, 0, -4300, 2000, 0x0)
    OP_93(0x1A3, 0x0, 0x1F4)
    Return()

    # Function_37_6101 end

    def Function_38_614C(): pass

    label("Function_38_614C")


    def lambda_6151():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6151)

    def lambda_6162():
        OP_95(0xFE, 50110, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6162)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x1A3, 500)
    Return()

    # Function_38_614C end

    def Function_39_6183(): pass

    label("Function_39_6183")


    def lambda_6188():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_6188)

    def lambda_6199():
        OP_95(0xFE, 48110, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_6199)
    Return()

    # Function_39_6183 end

    def Function_40_61AF(): pass

    label("Function_40_61AF")

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
        "#5P#04605F哎，那个姐姐是……！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#11P#00005F那是……\x01",
            "莉夏吗？\x02",
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

    def lambda_642D():
        OP_95(0xFE, 900, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_642D)
    Sleep(50)

    def lambda_644A():
        OP_95(0xFE, -800, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_644A)
    OP_68(-660, 1450, 2200, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13470, 3000)
    WaitChrThread(0x1A3, 1)

    def lambda_6496():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_6496)
    WaitChrThread(0x1A3, 1)
    OP_6F(0x79)

    #C0329
    ChrTalk(
        0x101,
        (
            "#5P#00000F果然是莉夏啊。\x02\x03",

            "#00005F全体演员不是\x01",
            "都在休息吗？\x02",
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
            "啊，罗伊德警官。\x02\x03",

            "那个……我的舞台装昨天\x01",
            "一直到很晚才修补好……\x02\x03",

            "在正式演出之前，想试穿一下，\x01",
            "做个最终检查。\x02\x03",

            "先不说这个了……\x01",
            "听说有小猫跑进来了？\x02",
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
        "#5P#00001F嗯，是的……\x02",
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
            "#11P#00005F哎？\x02\x03",

            "我们是追着小猫出来的，\x01",
            "怎么会……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    TurnDirection(0x104, 0x15, 500)

    #C0333
    ChrTalk(
        0x104,
        "#12P#00305F怎么，原来是这样啊？\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x109,
        (
            "#6P#10100F我想它并没有\x01",
            "来过这边……\x02",
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
        "#6P#10300F呀，大家都到齐了啊。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#5P#00100F是啊，而且连\x01",
            "莉夏小姐都在。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#6P#N#00000F瓦吉、艾莉……\x01",
            "看样子，你们好像也没找到啊。\x02",
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
            "#11P#00005F也就是说，在我们跟丢之后，\x01",
            "没有任何人看到过玛丽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#6P#00103F大门已经关好了……\x02\x03",

            "#00100F看来还是藏身在\x01",
            "这个大厅的可能性比较高吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        (
            "#12P#00303F嗯，也许是躲在了\x01",
            "某个不起眼的角落里。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x109,
        (
            "#6P#10100F是啊，我们再\x01",
            "一起找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x105,
        "#6P#10304F嗯，看来也只能这样了。\x02",
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
            "#12P#06202F那个……\x02\x03",

            "请问这位女孩是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        "#5P#00000F哦，她是──\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    #C0345
    ChrTalk(
        0x1A3,
        (
            "#5P#04609F啊哈哈，这位姐姐很厉害嘛¤\x02\x03",

            "#04611F我从刚才开始就一直在寻找破绽，\x01",
            "但完全没有可乘之机呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x15,
        "#12P#06205F哎、哎……？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x104,
        (
            "#12P#00303F……这是我\x01",
            "顽劣的堂妹。\x02\x03",

            "#00300F不用太在意她。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x15,
        "#11P#06205F兰迪先生的……\x02",
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
            "谢莉·奥兰多，\x01",
            "叫我谢莉吧！\x02\x03",

            "嘿～我虽然见过姐姐\x01",
            "在彩虹剧团舞台上的表演。\x02\x03",

            "但在近距离一看，\x01",
            "这视觉杀伤力真是完全不同呢～！\x02\x03",

            "真好啊～\x01",
            "这么大的胸部，太让人羡慕了⊥\x02",
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
        "#12P#06209F哎，那个……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#6P#00113F……我之前还被她\x01",
            "侵犯过一次。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0352
    ChrTalk(
        0x1A3,
        (
            "#5P#04609F啊哈哈，这有什么嘛，\x01",
            "又不会少块肉。\x02\x03",

            "而且这也算是一种缘──\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x15)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6E2A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_6E2A)
    Sleep(50)

    def lambda_6E3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E3A)
    Sleep(300)

    #C0353
    ChrTalk(
        0x1A3,
        "#6P#04605F哎……？\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x15,
        "#12P#06205F啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_6E7B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E7B)
    Sleep(50)

    def lambda_6E8B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E8B)
    Sleep(50)

    def lambda_6E9B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E9B)
    Sleep(50)

    def lambda_6EAB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6EAB)
    Sleep(50)

    def lambda_6EBB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6EBB)
    Sleep(50)

    def lambda_6ECB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6ECB)
    Sleep(50)

    def lambda_6EDB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6EDB)
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

    def lambda_6FE1():
        OP_95(0xFE, 0, 2500, 18930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6FE1)
    Sleep(1000)

    def lambda_6FFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_6FFE)
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
            "#11P#00011F原、原来藏在了\x01",
            "那种地方吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x15,
        "#11P#06201F我去抓！\x02",
    )

    CloseMessageWindow()

    def lambda_7096():

        label("loc_7096")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_7096")

    QueueWorkItem2(0x102, 1, lambda_7096)

    def lambda_70A8():

        label("loc_70A8")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_70A8")

    QueueWorkItem2(0x104, 1, lambda_70A8)

    def lambda_70BA():

        label("loc_70BA")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_70BA")

    QueueWorkItem2(0x109, 1, lambda_70BA)

    def lambda_70CC():

        label("loc_70CC")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_70CC")

    QueueWorkItem2(0x105, 1, lambda_70CC)
    OP_95(0x15, 1290, 0, 5610, 4000, 0x0)

    def lambda_70F2():
        OP_95(0xFE, 0, 2500, 15240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_70F2)
    Sleep(500)

    #C0357
    ChrTalk(
        0x1A3,
        "#11P#04602F啊哈哈，我也去！\x02",
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
        "#12P#00306F呼，真是的……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        (
            "#6P#00105F那个……\x01",
            "我们该怎么办才好？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0360
    ChrTalk(
        0x101,
        (
            "#5P#00000F我和谢莉过去帮忙。\x02\x03",

            "其他人留在这里待命，\x01",
            "防止它再次逃跑。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_720D():

        label("loc_720D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_720D")

    QueueWorkItem2(0x102, 1, lambda_720D)
    Sleep(50)

    def lambda_7222():

        label("loc_7222")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7222")

    QueueWorkItem2(0x104, 1, lambda_7222)
    Sleep(50)

    def lambda_7237():

        label("loc_7237")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7237")

    QueueWorkItem2(0x109, 1, lambda_7237)
    Sleep(50)

    def lambda_724C():

        label("loc_724C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_724C")

    QueueWorkItem2(0x105, 1, lambda_724C)
    Sleep(300)

    #C0361
    ChrTalk(
        0x109,
        "#6P#10100F明白了。\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，但愿这次能\x01",
            "顺利抓到啊。\x02",
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

    # Function_40_61AF end

    def Function_41_72FB(): pass

    label("Function_41_72FB")


    def lambda_7300():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7300)

    def lambda_7311():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7311)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -6510, 2500, 12970, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_41_72FB end

    def Function_42_7346(): pass

    label("Function_42_7346")


    def lambda_734B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_734B)

    def lambda_735C():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_735C)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -7770, 2500, 12730, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_42_7346 end

    def Function_43_7391(): pass

    label("Function_43_7391")

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
            "#12P#04600F啊哈哈，谢啦¤\x01",
            "多亏有姐姐帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，我也要\x01",
            "向你道谢啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x15,
        (
            "#06209F哪里，只是身体\x01",
            "不由自主地动了起来而已。\x02\x03",

            "#06204F而且，就算我没有多事出手，\x01",
            "谢莉小姐也完全可以\x01",
            "救到小猫的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0366
    ChrTalk(
        0x101,
        "#12P#00005F是、是这样吗……？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x1A3,
        (
            "#12P#04605F嘿，你能看出来啊？\x02\x03",

            "#04604F如果我当时跳出去，\x01",
            "的确可以及时救到……\x02\x03",

            "#04609F不过，欣赏到了姐姐的\x01",
            "轻盈跳跃和超级乳摇，\x01",
            "真是十分满足啊。\x02",
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
        "#12P#00306F谢莉，你可真是……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x102,
        "#12P#00106F……莉夏小姐，我好同情你。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x15,
        "#06209F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x16,
        (
            "话、话说回来，\x01",
            "真是很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x16,
        "没想到小猫竟然在舞台上……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x16,
        (
            "我没有经过确认，\x01",
            "就为了检查而启动装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x1A3,
        (
            "#12P#04600F算啦，结果不是很好嘛。\x02\x03",

            "#04604F没有任何人受伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，是啊，\x01",
            "所以请不必在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x109,
        (
            "#6P#10100F那么……\x01",
            "我们现在就回\x01",
            "本德先生那里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x105,
        (
            "#12P#10300F是啊，他们肯定很担心，\x01",
            "大概还在拼命找呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    #C0378
    ChrTalk(
        0x14,
        "#6P喵～¤\x02",
    )

    CloseMessageWindow()

    def lambda_78DD():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_78DD)
    Sleep(50)

    def lambda_78ED():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_78ED)
    Sleep(50)

    def lambda_78FD():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_78FD)
    Sleep(50)

    def lambda_790D():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_790D)
    Sleep(50)

    def lambda_791D():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_791D)
    Sleep(50)

    def lambda_792D():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_792D)
    Sleep(300)

    #C0379
    ChrTalk(
        0x104,
        (
            "#11P#00309F哈哈……\x01",
            "它变脸变得好快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        (
            "#11P#00102F是啊，刚才还怕成那副样子，\x01",
            "现在就像没事一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x1A3,
        "#11P#04609F哈哈，猫就是这样的嘛。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#11P#00003F（从她嘴里说出这种话，\x01",
            "  说服力真是相当强呢……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0383
    ChrTalk(
        0x101,
        (
            "#12P#00000F那我们这就\x01",
            "告辞了。\x02\x03",

            "多谢你们的协助。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A50():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7A50)
    Sleep(50)

    def lambda_7A60():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A60)
    Sleep(50)

    def lambda_7A70():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A70)
    Sleep(50)

    def lambda_7A80():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7A80)
    Sleep(50)

    def lambda_7A90():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A90)
    Sleep(300)

    #C0384
    ChrTalk(
        0x9,
        "哪里哪里，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x15,
        "#06202F呵呵，路上请小心。\x02",
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

    def lambda_7B43():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7B43)
    WaitChrThread(0x14, 3)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A3, 0x15, 500)
    Sleep(300)

    #C0386
    ChrTalk(
        0x1A3,
        (
            "#12P#04605F啊，对了，姐姐。\x02\x03",

            "#04602F我可以直接叫你\x01",
            "莉夏吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0387
    ChrTalk(
        0x15,
        (
            "#5P#06205F啊……\x02\x03",

            "#06202F……嗯，\x01",
            "当然可以啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x1A3,
        (
            "#12P#04609F嘿嘿，谢啦，莉夏。\x02\x03",

            "#04600F那就再见了！\x02",
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
            "#06203F#3243V（兰迪先生的堂妹……）\x02\x03",

            "#06201F#3244V（……她就是传说中的\x01",
            "  『血腥谢莉』……）\x02",
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

    # Function_43_7391 end

    def Function_44_7D12(): pass

    label("Function_44_7D12")


    def lambda_7D17():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D17)
    Sleep(800)

    def lambda_7D34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7D34)
    Return()

    # Function_44_7D12 end

    def Function_45_7D41(): pass

    label("Function_45_7D41")


    def lambda_7D46():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D46)
    Sleep(1500)

    def lambda_7D63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7D63)
    Return()

    # Function_45_7D41 end

    def Function_46_7D70(): pass

    label("Function_46_7D70")


    def lambda_7D75():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D75)
    Sleep(2000)

    def lambda_7D92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7D92)
    Return()

    # Function_46_7D70 end

    def Function_47_7D9F(): pass

    label("Function_47_7D9F")


    def lambda_7DA4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DA4)
    Sleep(500)

    def lambda_7DC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7DC1)
    Return()

    # Function_47_7D9F end

    def Function_48_7DCE(): pass

    label("Function_48_7DCE")

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

    def lambda_7EE3():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EE3)

    def lambda_7EFD():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EFD)
    Sleep(50)

    def lambda_7F11():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F11)

    def lambda_7F2B():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F2B)
    Sleep(50)

    def lambda_7F3F():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7F3F)

    def lambda_7F59():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7F59)
    Sleep(50)

    def lambda_7F6D():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7F6D)

    def lambda_7F87():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7F87)
    Sleep(50)

    def lambda_7F9B():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7F9B)

    def lambda_7FB5():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7FB5)
    Sleep(50)

    def lambda_7FC9():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7FC9)

    def lambda_7FE3():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7FE3)
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
        "哦，特别任务支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x9,
        (
            "今天是剧团的休息日，\x01",
            "请问有何贵干？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        (
            "#00000F啊，没有的，\x01",
            "只是顺路过来看看而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#00100F新版舞剧……\x01",
            "就要在明天公演了呢。\x02\x03",

            "所以今天才会\x01",
            "休息吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x9,
        "嗯，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x9,
        (
            "不过，有一个人\x01",
            "还在里面继续练习呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x109,
        (
            "#10105F哎，真有热情啊，\x01",
            "莫非是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "看来你已经猜到了啊。\x01",
            "不错，正是修利。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x9,
        (
            "明天毕竟是她\x01",
            "首次向公众亮相……\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x9,
        (
            "她似乎非常紧张，如果不活动身体\x01",
            "就无法平静下来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x9,
        (
            "如果各位方便，\x01",
            "不妨去看看她的练习。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#00005F可、可以吗？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x9,
        (
            "当然，各位平时一直都\x01",
            "亲切关照我们。\x01",
            "让你们进去，谁都不会有意见的。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x9,
        (
            "而且……修利好像从早上开始，\x01",
            "一直聚精会神地练到了现在，\x01",
            "中途几乎没有休息过……\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x9,
        (
            "如果各位方便，\x01",
            "就过去和她打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x9,
        (
            "这样也能让那孩子\x01",
            "稍微歇息一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        "#00000F原来如此，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x102,
        "#00100F多谢您的关照。\x02",
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

    # Function_48_7DCE end

    def Function_49_83C5(): pass

    label("Function_49_83C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -70, 2500, 15340, 180)
    EventEnd(0x5)
    Return()

    # Function_49_83C5 end

    def Function_50_83E9(): pass

    label("Function_50_83E9")

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

    def lambda_84E2():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84E2)

    def lambda_84FC():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84FC)
    Sleep(50)

    def lambda_8510():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8510)

    def lambda_852A():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_852A)
    Sleep(500)

    def lambda_853E():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_853E)

    def lambda_8558():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8558)
    Sleep(50)

    def lambda_856C():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_856C)

    def lambda_8586():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8586)
    WaitChrThread(0x105, 1)

    #C0408
    ChrTalk(
        0x101,
        (
            "#00005F彩虹剧团啊……\x01",
            "好久没进过这个剧场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，是啊。\x01",
            "不知道伊莉娅小姐\x01",
            "和莉夏小姐在不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，你们真是认识\x01",
            "不少名人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x109,
        (
            "#12P#10105F不、不过……真的可以\x01",
            "随便进来吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 500)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_868A():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_868A)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0412
    ChrTalk(
        0x9,
        (
            "这不是特别任务支援科的\x01",
            "罗伊德警官和艾莉小姐吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x9,
        (
            "真是好久不见了啊，\x01",
            "今日有何贵干呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        (
            "#00000F我们支援科已经\x01",
            "恢复工作了。\x02\x03",

            "现在正在市内巡视，\x01",
            "所以就过来和大家打声招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x102,
        "#00100F没有给各位造成不便吧？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x9,
        (
            "嗯，当然没有\x01",
            "什么不便。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x9,
        (
            "现在正好是休息时间，\x01",
            "请进去和大家打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x9,
        "我想伊莉娅小姐她们肯定会很高兴的。\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        "#00000F非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x109,
        "#12P#10112F那、那个……\x02",
    )

    CloseMessageWindow()

    def lambda_8833():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8833)
    TurnDirection(0x102, 0x109, 500)

    #C0421
    ChrTalk(
        0x102,
        "#00105F怎么了？诺艾尔小姐。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0422
    ChrTalk(
        0x109,
        (
            "#12P#10102F没什么，只是……该怎么说呢……\x01",
            "真是再次体会到了特别任务支援科的强大之处。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0423
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，是啊。\x01",
            "名闻天下的彩虹剧团\x01",
            "竟然这么给你们面子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0424
    ChrTalk(
        0x101,
        (
            "#5P#00000F哈哈，听你这么一说，\x01",
            "还真是这样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x102,
        "#00100F嗯，实在是很可贵的缘分啊。\x02",
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

    # Function_50_83E9 end

    def Function_51_89B3(): pass

    label("Function_51_89B3")

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

    def lambda_8ADA():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8ADA)

    def lambda_8AF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8AF4)
    Sleep(100)

    def lambda_8B08():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B08)

    def lambda_8B22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8B22)
    Sleep(500)

    def lambda_8B36():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8B36)

    def lambda_8B50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8B50)
    Sleep(100)
    OP_68(-970, 1450, -1300, 3000)
    MoveCamera(44, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15070, 3000)

    def lambda_8B92():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8B92)

    def lambda_8BAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8BAC)
    Sleep(500)

    def lambda_8BC0():
        OP_95(0xFE, -500, 0, -5100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_8BC0)

    def lambda_8BDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_8BDA)
    Sleep(100)

    def lambda_8BEE():
        OP_95(0xFE, 500, 0, -5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_8BEE)

    def lambda_8C08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_8C08)
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

    def lambda_8C5D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8C5D)
    Sleep(50)

    def lambda_8C6D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8C6D)
    Sleep(300)

    #C0426
    ChrTalk(
        0xA,
        "#5P啊，这不是……！\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x9,
        (
            "#5P特别任务支援科\x01",
            "的各位吗……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-270, 1350, 1970, 3000)
    MoveCamera(44, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13600, 3000)

    def lambda_8CEA():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CEA)
    Sleep(50)

    def lambda_8D07():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D07)
    Sleep(50)

    def lambda_8D24():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D24)
    Sleep(50)

    def lambda_8D41():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8D41)
    Sleep(50)

    def lambda_8D5E():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_8D5E)
    Sleep(50)

    def lambda_8D7B():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_8D7B)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    #C0428
    ChrTalk(
        0x101,
        "#12P#00000F二位都平安无事啊。\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x102,
        (
            "#12P#00100F莫非其他人\x01",
            "也都在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "是的，工作人员和演员\x01",
            "全都在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EC2")

    #C0431
    ChrTalk(
        0x9,
        (
            "大家正在\x01",
            "团结一心地努力组建\x01",
            "新的演出阵容。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x9,
        (
            "突然下达的戒严令和禁止外出令\x01",
            "的确是让人困惑……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x9,
        (
            "但经过集体商讨之后，\x01",
            "大家都认为与其回家，\x01",
            "不如在这里一起练习。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F26")

    label("loc_8EC2")


    #C0434
    ChrTalk(
        0x9,
        (
            "大家正在\x01",
            "团结一心地努力组建\x01",
            "新的演出阵容。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x9,
        (
            "在这样的状况下，\x01",
            "我们能做的事情\x01",
            "也只有这些了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F26")


    #C0436
    ChrTalk(
        0x103,
        (
            "#12P#00204F原来如此……\x01",
            "真是让人佩服。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9175")

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
            "#5P莫非……\x01",
            "站在那里的\x01",
            "是莉夏吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x106, 500)

    #C0439
    ChrTalk(
        0x9,
        "莉夏小姐……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x106,
        (
            "#12P#10706F……好久不见。\x02\x03",

            "#10710F大家都平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x9,
        (
            "……莉夏小姐终于\x01",
            "肯来见我们了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x9,
        (
            "我们知道你肯定\x01",
            "有很多自己的想法……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x9,
        (
            "不过，如果可以，\x01",
            "能不能去看看大家的练习呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x9,
        (
            "修利小姐和大家\x01",
            "都在全力准备呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x106,
        (
            "#12P#10712F#30W……………………………\x02\x03",

            "#10704F说的……也是啊……\x02\x01",

            "#10710F如果只是稍稍看一眼的话……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    #C0446
    ChrTalk(
        0x101,
        "#5P#00002F莉夏……\x02",
    )

    CloseMessageWindow()
    Jump("loc_91DC")

    label("loc_9175")


    #C0447
    ChrTalk(
        0x9,
        (
            "如果可以，就去看看\x01",
            "大家的练习吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x9,
        (
            "修利小姐和大家\x01",
            "都在全力准备呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        "#12P#00000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    label("loc_91DC")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_923A")
    SetChrPos(0x9, 3940, 0, 2900, 90)
    Jump("loc_924B")

    label("loc_923A")

    SetChrPos(0x9, -2250, 2500, 15000, 180)

    label("loc_924B")

    SetChrPos(0xA, 6970, 0, 3480, 270)
    EventEnd(0x5)
    Return()

    # Function_51_89B3 end

    def Function_52_925F(): pass

    label("Function_52_925F")

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

    def lambda_9323():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9323)

    def lambda_933D():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_933D)
    Sleep(50)

    def lambda_9351():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9351)

    def lambda_936B():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_936B)
    Sleep(50)

    def lambda_937F():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_937F)

    def lambda_9399():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9399)
    Sleep(50)

    def lambda_93AD():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_93AD)

    def lambda_93C7():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93C7)
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

    def lambda_9459():

        label("loc_9459")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_9459")

    QueueWorkItem2(0x0, 1, lambda_9459)

    def lambda_946B():

        label("loc_946B")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_946B")

    QueueWorkItem2(0x1, 1, lambda_946B)

    def lambda_947D():

        label("loc_947D")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_947D")

    QueueWorkItem2(0x2, 1, lambda_947D)

    def lambda_948F():

        label("loc_948F")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_948F")

    QueueWorkItem2(0x3, 1, lambda_948F)
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
            "是支援科的各位啊，\x01",
            "欢迎大家来访。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        (
            "但是，真抱歉。\x01",
            "我们正在准备\x01",
            "下午的公演……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x101,
        (
            "#11P#00005F这样啊，\x01",
            "实在是打扰了。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x102,
        (
            "#6P#00104F反正我们也没什么事，\x01",
            "还是下次再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x105,
        "#12P#10300F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x109,
        "#12P#10100F打扰各位了，真抱歉。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x137, 0)
    SetScenarioFlags(0x22, 6)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_925F end

    def Function_53_95DC(): pass

    label("Function_53_95DC")

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

    def lambda_96EC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_96EC)

    def lambda_9706():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9706)
    Sleep(50)

    def lambda_971A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_971A)

    def lambda_9734():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9734)
    Sleep(50)

    def lambda_9748():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9748)

    def lambda_9762():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9762)
    Sleep(50)

    def lambda_9776():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9776)

    def lambda_9790():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9790)
    Sleep(50)

    def lambda_97A4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_97A4)

    def lambda_97BE():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_97BE)
    Sleep(50)

    def lambda_97D2():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_97D2)

    def lambda_97EC():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_97EC)
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

    def lambda_98AA():

        label("loc_98AA")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_98AA")

    QueueWorkItem2(0x0, 1, lambda_98AA)

    def lambda_98BC():

        label("loc_98BC")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_98BC")

    QueueWorkItem2(0x1, 1, lambda_98BC)

    def lambda_98CE():

        label("loc_98CE")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_98CE")

    QueueWorkItem2(0x2, 1, lambda_98CE)

    def lambda_98E0():

        label("loc_98E0")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_98E0")

    QueueWorkItem2(0x3, 1, lambda_98E0)

    def lambda_98F2():

        label("loc_98F2")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_98F2")

    QueueWorkItem2(0x4, 1, lambda_98F2)

    def lambda_9904():

        label("loc_9904")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_9904")

    QueueWorkItem2(0x5, 1, lambda_9904)
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
            "是支援科的各位啊，\x01",
            "欢迎大家来访。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x9,
        (
            "但是，真抱歉。\x01",
            "我们正在为新版舞剧\x01",
            "进行最终彩排……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#00000F哦，对了，\x01",
            "新版舞剧的公演日就快到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x104,
        (
            "#00306F虽然很想偷偷看看，\x01",
            "但这次还是算了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x103,
        (
            "#00200F是啊，还是赶快离开吧，\x01",
            "免得打扰到大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x102,
        "#00100F真是打扰了。\x02",
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

    # Function_53_95DC end

    def Function_54_9A87(): pass

    label("Function_54_9A87")

    EventBegin(0x1)

    #C0462
    ChrTalk(
        0x101,
        (
            "#00000F我们得先赶快\x01",
            "找到玛丽。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x1A3,
        (
            "#04600F是要调查二层的Ｓ席吧？\x01",
            "那就出发吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 48300, 0, -230, 90)
    EventEnd(0x4)
    Return()

    # Function_54_9A87 end

    def Function_55_9AF1(): pass

    label("Function_55_9AF1")

    EventBegin(0x1)
    Sleep(50)

    #C0464
    ChrTalk(
        0x101,
        (
            "#00000F这边是二层观众席。\x02\x03",

            "随便乱转会给人家添麻烦的，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_9AF1 end

    def Function_56_9B56(): pass

    label("Function_56_9B56")

    EventBegin(0x1)
    Sleep(50)

    #C0465
    ChrTalk(
        0x101,
        (
            "#00000F这边是二层观众席。\x02\x03",

            "随便乱转会给人家添麻烦的，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_56_9B56 end

    def Function_57_9BBB(): pass

    label("Function_57_9BBB")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9C24")

    #C0466
    ChrTalk(
        0x101,
        (
            "#00000F大家正在讨论练习的事情呢。\x02\x03",

            "如果想和他们打招呼，\x01",
            "还是从正面的入口过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C62")

    label("loc_9C24")


    #C0467
    ChrTalk(
        0x101,
        (
            "#00000F今天只有修利\x01",
            "一个人在练习……\x02\x03",

            "还是不要进后台了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C62")

    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_57_9BBB end

    SaveToFile()

Try(main)
