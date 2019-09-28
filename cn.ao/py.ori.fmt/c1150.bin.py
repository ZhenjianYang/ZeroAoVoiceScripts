from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1150.bin",                # FileName
        "c1150",                    # MapName
        "c1150",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 5000, 1500, 0, 0, 1, 24, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1150",                  # 0
        "接待小姐瑞贝卡",         # 1
        "接待小姐芙兰",           # 2
        "多诺邦警督",             # 3
        "雷蒙德搜查官",           # 4
        "达德利搜查官",           # 5
        "艾玛搜查官",             # 6
        "凯特巡警",               # 7
        "弗兰茨巡警",             # 8
        "皮埃尔副局长",           # 9
        "尤利",                   # 10
        "塞克斯",                 # 11
        "瑞吉",                   # 12
        "乔里基科长",             # 13
        "国防军士兵",             # 14
        "国防军士兵",             # 15
        "警官",                   # 16
        "警官",                   # 17
        "赛尔盖科长",             # 18
        "伊斯",                   # 19
        "伊斯",                   # 20
        "伊斯",                   # 21
        "伊斯",                   # 22
        "伊斯",                   # 23
        "伊斯",                   # 24
        "伊斯",                   # 25
        "伊斯",                   # 26
        "SE制御",                 # 27
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch30600.itc",                   # 03
        "chr/ch30000.itc",                   # 04
        "chr/ch06400.itc",                   # 05
        "chr/ch30100.itc",                   # 06
        "chr/ch44102.itc",                   # 07
        "chr/ch47500.itc",                   # 08
        "chr/ch23600.itc",                   # 09
        "chr/ch30002.itc",                   # 0A
        "chr/ch30300.itc",                   # 0B
        "chr/ch30200.itc",                   # 0C
        "chr/ch41400.itc",                   # 0D
        "chr/ch41500.itc",                   # 0E
        "chr/ch00900.itc",                   # 0F
    ))

    DeclNpc(-100,    0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   11,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-125379, 0,       19520,   0,    453,  0x0, 0,   2,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 0,   37,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   9,   0,   255, 255, 0,   35,  255,  0)
    DeclNpc(-58049,  0,       15899,   90,   389,  0x0, 0,   6,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   43,  255,  0)
    DeclNpc(-12409,  0,       19770,   180,  389,  0x0, 0,   14,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   4,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   4,   0,   0,   0,   0,   42,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  -12.699999809265137,   18.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.4350004196167,      0.1428571492433548,    1.0])
    DeclEvent(0x0000, 0, 50,  -8.260000228881836,    10.029999732971191,    -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.130000114440918,     -2.507499933242798,    0.1428571492433548,    1.0])

    DeclActor(-100,    0,       14400,   1100,    -100,    1500,    15400,   0x007E, 0,  5,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  17, 0x0000)
    DeclActor(-9850,   0,       16000,   1000,    -9850,   1500,    16000,   0x007C, 0,  57, 0x0000)
    DeclActor(-9850,   0,       13750,   1000,    -9850,   1500,    13750,   0x007C, 0,  57, 0x0000)

    ChipFrameInfo(1536, 0)                                       # 0

    ScpFunction((
        "Function_0_600",          # 00, 0
        "Function_1_6B8",          # 01, 1
        "Function_2_6E3",          # 02, 2
        "Function_3_736",          # 03, 3
        "Function_4_E7A",          # 04, 4
        "Function_5_F4D",          # 05, 5
        "Function_6_F51",          # 06, 6
        "Function_7_13D6",         # 07, 7
        "Function_8_2520",         # 08, 8
        "Function_9_252F",         # 09, 9
        "Function_10_405B",        # 0A, 10
        "Function_11_414E",        # 0B, 11
        "Function_12_4B0B",        # 0C, 12
        "Function_13_55CA",        # 0D, 13
        "Function_14_5D74",        # 0E, 14
        "Function_15_5E5C",        # 0F, 15
        "Function_16_5F51",        # 10, 16
        "Function_17_6A99",        # 11, 17
        "Function_18_6BC7",        # 12, 18
        "Function_19_85F4",        # 13, 19
        "Function_20_8D8D",        # 14, 20
        "Function_21_93A0",        # 15, 21
        "Function_22_9A21",        # 16, 22
        "Function_23_A397",        # 17, 23
        "Function_24_A3BD",        # 18, 24
        "Function_25_AA7A",        # 19, 25
        "Function_26_AF6C",        # 1A, 26
        "Function_27_B1F9",        # 1B, 27
        "Function_28_B608",        # 1C, 28
        "Function_29_BE31",        # 1D, 29
        "Function_30_C362",        # 1E, 30
        "Function_31_D2E7",        # 1F, 31
        "Function_32_D55C",        # 20, 32
        "Function_33_D646",        # 21, 33
        "Function_34_D722",        # 22, 34
        "Function_35_D838",        # 23, 35
        "Function_36_D91E",        # 24, 36
        "Function_37_DC26",        # 25, 37
        "Function_38_DEA1",        # 26, 38
        "Function_39_E082",        # 27, 39
        "Function_40_E5E5",        # 28, 40
        "Function_41_E68A",        # 29, 41
        "Function_42_E7B6",        # 2A, 42
        "Function_43_E90B",        # 2B, 43
        "Function_44_E9D7",        # 2C, 44
        "Function_45_EDDC",        # 2D, 45
        "Function_46_100DC",       # 2E, 46
        "Function_47_10636",       # 2F, 47
        "Function_48_11506",       # 30, 48
        "Function_49_11519",       # 31, 49
        "Function_50_11BDC",       # 32, 50
        "Function_51_12678",       # 33, 51
        "Function_52_13139",       # 34, 52
        "Function_53_13B7C",       # 35, 53
        "Function_54_13CB4",       # 36, 54
        "Function_55_13D93",       # 37, 55
        "Function_56_140AB",       # 38, 56
        "Function_57_141AC",       # 39, 57
    ))


    def Function_0_600(): pass

    label("Function_0_600")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_640"),
        (1, "loc_64C"),
        (2, "loc_658"),
        (3, "loc_664"),
        (4, "loc_670"),
        (5, "loc_67C"),
        (6, "loc_688"),
        (SWITCH_DEFAULT, "loc_694"),
    )


    label("loc_640")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_64C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_658")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_664")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_670")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_67C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_688")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_694")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_6A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_6B7")

    Return()

    # Function_0_600 end

    def Function_1_6B8(): pass

    label("Function_1_6B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E2")
    OP_94(0xFE, 0xFFFF8508, 0x24CC, 0xFFFF93C2, 0x288C, 0x3E8)
    Sleep(300)
    Jump("Function_1_6B8")

    label("loc_6E2")

    Return()

    # Function_1_6B8 end

    def Function_2_6E3(): pass

    label("Function_2_6E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_735")
    OP_95(0x10, -57300, 0, 20000, 2000, 0x0)
    Sleep(500)
    OP_93(0x10, 0xB4, 0x2EE)
    Sleep(500)
    OP_95(0x10, -57300, 0, 16000, 2000, 0x0)
    Sleep(500)
    OP_93(0x10, 0x0, 0x2EE)
    Sleep(500)
    Jump("Function_2_6E3")

    label("loc_735")

    Return()

    # Function_2_6E3 end

    def Function_3_736(): pass

    label("Function_3_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_78B")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x17, -57400, 0, 16210, 0)
    SetChrPos(0x18, -57420, 0, 18000, 180)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7AD")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_838")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -69670, 30, 19510, 315)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -70670, 0, 20710, 135)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -57400, 0, 16210, 0)
    ClearChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -57420, 0, 18000, 180)
    ClearChrFlags(0xE, 0x40)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_B69")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_85A")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_B69")

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8F2")
    SetChrPos(0xA, -121660, 0, 18190, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -56800, 0, 16000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -58000, 30, 15910, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -58210, 0, 18000, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xF, -56700, 0, 18000, 180)
    Jump("loc_B69")

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_922")
    SetChrPos(0xA, -12180, 0, 7890, 270)
    SetChrPos(0xB, -13680, 0, 7890, 90)
    Jump("loc_B69")

    label("loc_922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_990")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57400, 0, 16000, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -56700, 0, 18000, 180)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -58210, 0, 18000, 180)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x18, 0x10)
    Jump("loc_B69")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EA")
    SetChrPos(0xA, -121550, 0, 18180, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E5")
    SetChrFlags(0xD, 0x10)

    label("loc_9E5")

    Jump("loc_B69")

    label("loc_9EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A24")
    SetChrPos(0xA, -57400, 0, 16210, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -57420, 0, 18000, 180)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A3C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B69")

    label("loc_A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A9B")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -57400, 0, 16210, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -57420, 0, 18000, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -10590, 0, 15740, 90)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ACE")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B28")
    SetChrPos(0xA, -57400, 0, 16210, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57420, 0, 18000, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B12")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x14, 0x10)

    label("loc_B12")

    SetChrPos(0xB, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B69")
    SetChrPos(0xA, -11040, 0, 13810, 225)
    SetChrPos(0xB, -12290, 0, 12530, 45)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -10590, 0, 15740, 90)

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B84")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB5")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -11040, 0, 13810, 90)

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE5")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -57300, 0, 18750, 270)

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CEA")
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124800, 0, 18080, 135)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x40)

    label("loc_CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DE3")
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124800, 0, 18080, 135)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    ClearChrFlags(0xF, 0x40)

    label("loc_DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_DF7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 45)
    Jump("loc_E50")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E0B")
    ClearScenarioFlags(0x22, 1)
    Event(0, 49)
    Jump("loc_E50")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_E1F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 51)
    Jump("loc_E50")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_E33")
    ClearScenarioFlags(0x22, 3)
    Event(0, 55)
    Jump("loc_E50")

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_E50")
    ClearScenarioFlags(0x22, 4)
    SetChrPos(0x0, -12810, 0, 14970, 180)

    label("loc_E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E79")
    SetMapFlags(0x10000000)
    Event(0, 46)

    label("loc_E79")

    Return()

    # Function_3_736 end

    def Function_4_E7A(): pass

    label("Function_4_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBF")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EFA")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_EFA")

    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F28")
    OP_65(0x1, 0x1)

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3A")
    OP_65(0x0, 0x1)

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4C")
    OP_65(0x0, 0x1)

    label("loc_F4C")

    Return()

    # Function_4_E7A end

    def Function_5_F4D(): pass

    label("Function_5_F4D")

    Call(0, 6)
    Return()

    # Function_5_F4D end

    def Function_6_F51(): pass

    label("Function_6_F51")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_123A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_123A")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0001
    ChrTalk(
        0x8,
        (
            "啊，各位身上\x01",
            "带着的……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "莫非是\x01",
            "『结晶碎片』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00005F哎，是指这个吗？\x02\x03",

            "#00000F这是之前无意中得到的，\x01",
            "但一直不知道\x01",
            "有什么用处……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将结晶碎片\x01",
            "交给瑞贝卡查看。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0005
    ChrTalk(
        0x8,
        "嗯，果然没错……！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "这正是鉴定科的人正在寻找的\x01",
            "结晶碎片，可以用来修复\x01",
            "破损的记录结晶。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "只要有它，\x01",
            "应该就可以解析教团终端\x01",
            "中的一部分情报了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110C")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_110C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1135")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_1135")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115E")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_115E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1184")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_1184")

    Sleep(1000)

    #C0008
    ChrTalk(
        0x102,
        (
            "#00105F这、这就是说……\x01",
            "可以查阅约亚西姆·琼塔\x01",
            "隐藏起来的文章了……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "嗯，虽然只是\x01",
            "一部分而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "我想马上就能得出结果了，\x01",
            "要把『结晶碎片』\x01",
            "交给鉴定科吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 9)
    TalkEnd(0x8)
    Return()

    label("loc_123A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125D")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_125D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1272")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_1272")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_127C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C5")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x1, 3)
    Call(0, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_12EC")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                    # 0
            "出示战斗手册\x01",            # 1
            "确认教团终端的资料\x01",      # 2
            "交付结晶碎片\x01",            # 3
            "放弃\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_133B")

    label("loc_12EC")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                    # 0
            "出示战斗手册\x01",            # 1
            "确认教团终端的资料\x01",      # 2
            "放弃\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_133B")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1369")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)
    Jump("loc_13C0")

    label("loc_1369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 6)
    Call(0, 16)
    Jump("loc_13C0")

    label("loc_138D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AE")
    Call(0, 10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13C0")

    label("loc_13AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C0")
    Call(0, 9)

    label("loc_13C0")

    Jump("loc_127C")

    label("loc_13C5")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    Return()

    # Function_6_F51 end

    def Function_7_13D6(): pass

    label("Function_7_13D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DD")

    #C0011
    ChrTalk(
        0x8,
        "各位……真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00000F瑞贝卡小姐，你也辛苦了。\x01",
            "已经返回总部了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "嗯，凯特巡警和\x01",
            "雷蒙德警官他们\x01",
            "也恢复正常工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "我们已经脱离了\x01",
            "国防军的指挥系统……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "现在已经恢复正常工作，\x01",
            "在各自的岗位上，为平息事态\x01",
            "应对各方面的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        "#00300F嗯，那可真是不错呢。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "呵呵，这多亏了各位。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "……对了，能不能帮我\x01",
            "带句话给芙兰？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "警察局的接待工作就交给我，\x01",
            "让她专心协助你们的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15C6")

    #C0020
    ChrTalk(
        0x109,
        (
            "#10102F呵呵，好的，\x01",
            "一定会仔细转告给她的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F6")

    label("loc_15C6")


    #C0021
    ChrTalk(
        0x103,
        (
            "#00202F呵呵，知道了，\x01",
            "一定会原话传达给她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_163B")

    #C0022
    ChrTalk(
        0x10A,
        (
            "#00600F瑞贝卡，总部这边的事情\x01",
            "就拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1671")

    label("loc_163B")


    #C0023
    ChrTalk(
        0x101,
        (
            "#00000F瑞贝卡小姐也请加油，\x01",
            "总部这边就拜托你啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1671")


    #C0024
    ChrTalk(
        0x8,
        (
            "是！为了广大市民，\x01",
            "我一定会竭尽全力！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "在如今的状况下，还不能松懈大意……\x01",
            "请各位继续努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 3)
    Jump("loc_17FC")

    label("loc_16DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1790")

    #C0026
    ChrTalk(
        0x8,
        (
            "为了平息目前的事态，\x01",
            "警察总部也在努力应对各方面的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "请转告芙兰，\x01",
            "让她专心协助你们的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "在如今的状况下，还不能松懈大意……\x01",
            "请各位继续努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_17FC")

    label("loc_1790")


    #C0029
    ChrTalk(
        0x8,
        (
            "为了平息目前的事态，\x01",
            "警察总部也正在全力应对。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "在如今的状况下，还不能松懈大意……\x01",
            "请各位继续努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FC")

    Jump("loc_251F")

    label("loc_1801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_180F")
    Jump("loc_251F")

    label("loc_180F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_192D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CB")

    #C0031
    ChrTalk(
        0x8,
        (
            "今天早上，国防军的一些人\x01",
            "突然来到了总部，\x01",
            "命令我们在这里待命。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "由于太过突然，\x01",
            "我们有些\x01",
            "不知所措……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "不管怎么说，现在能做的\x01",
            "也只有等待会议结束啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1928")

    label("loc_18CB")


    #C0034
    ChrTalk(
        0x8,
        (
            "由于太过突然，\x01",
            "我们有些\x01",
            "不知所措……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "不管怎么说，现在能做的\x01",
            "也只有等待会议结束啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1928")

    Jump("loc_251F")

    label("loc_192D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_193B")
    Jump("loc_251F")

    label("loc_193B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19C2")

    #C0036
    ChrTalk(
        0x8,
        (
            "达德利警官今天的表情\x01",
            "也相当严肃……\x01",
            "看样子，状况似乎不容乐观呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "不管怎么说，希望能找到\x01",
            "武力之外的解决方法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251F")

    label("loc_19C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A7B")

    #C0038
    ChrTalk(
        0x8,
        (
            "多亏警备队的各位，\x01",
            "铁道列车在今天早上\x01",
            "就已经完全恢复运行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "总算赶在首班车发车时间之前修复完毕，\x01",
            "连车次表都\x01",
            "不需要更改……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "这充分体现了\x01",
            "警备队员的执著啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251F")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B15")

    #C0041
    ChrTalk(
        0x8,
        (
            "拜列车事故所赐，\x01",
            "很快就有各方人士\x01",
            "前来咨询各种问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "临时替代的运输手段\x01",
            "已经开始准备了……\x01",
            "但如果再这样持续下去，实在是很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251F")

    label("loc_1B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BB5")

    #C0043
    ChrTalk(
        0x8,
        (
            "『灵智之草』……\x01",
            "曾在教团的数据库中看到过，\x01",
            "『真知』的原料……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "那种东西竟然突然出现在\x01",
            "克洛斯贝尔的各个地区……\x01",
            "究竟发生了什么事情呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251F")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6D")

    #C0045
    ChrTalk(
        0x8,
        (
            "各位，你们在这次的任务中\x01",
            "将要和游击士协会联手行动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "呵呵，没想到竟然有一天\x01",
            "会与协会并肩作战，共同处理委托……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "各位总是能给我们\x01",
            "带来惊喜呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1CB3")

    label("loc_1C6D")


    #C0048
    ChrTalk(
        0x8,
        (
            "正如芙兰所说，\x01",
            "与幻兽为敌，想必会十分棘手……\x01",
            "但还请努力加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB3")

    Jump("loc_251F")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D61")

    #C0049
    ChrTalk(
        0x8,
        (
            "赛尔盖科长已经在\x01",
            "二层的警备对策总部待命了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "正式会议的开始时间\x01",
            "终于近在眼前了……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "最初的重要任务\x01",
            "就是要让首脑们\x01",
            "安全进入会场。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1DBE")

    label("loc_1D61")


    #C0052
    ChrTalk(
        0x8,
        (
            "正式会议的开始时间\x01",
            "终于近在眼前了……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "最初的重要任务\x01",
            "就是要让首脑们\x01",
            "安全进入会场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBE")

    Jump("loc_251F")

    label("loc_1DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E40")

    #C0054
    ChrTalk(
        0x8,
        (
            "我和芙兰都在休息时间\x01",
            "去参观了兰花塔……\x01",
            "真是被那压迫力彻底折服了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "不愧是克洛斯贝尔\x01",
            "新的标志性建筑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251F")

    label("loc_1E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_217D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E0")

    #C0056
    ChrTalk(
        0x8,
        (
            "这次的警备体制是由\x01",
            "警察局与警备队共同建立的协力体制，\x01",
            "可谓前所未有。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "如果在以往，\x01",
            "想要建起这样的体制\x01",
            "几乎就是不可能的……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "如今能有此变化，\x01",
            "最大的要因应该就是\x01",
            "对警察有着深刻理解的索妮亚司令了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#00303F（嗯～瑞贝卡小姐\x01",
            "  真是个美人啊。）\x02\x03",

            "#00309F（虽然都戴眼镜，但与已经青春不再的\x01",
            "  索妮亚司令完全不同啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#10106F（呼，兰迪前辈……\x01",
            "  小心我报告给司令哦～）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x104)

    #C0061
    ChrTalk(
        0x104,
        (
            "#00305F（不、不要啊，\x01",
            "  刚才只是一时口误而已……）\x02\x03",

            "#00309F（嗯嗯～瑞贝卡小姐虽然也算个美人，\x01",
            "  但终究还是不能和索妮亚司令相比啊～）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 7)
    Jump("loc_2178")

    label("loc_20E0")


    #C0062
    ChrTalk(
        0x8,
        (
            "这次的警备体制是由\x01",
            "警察局与警备队共同建立的协力体制，\x01",
            "可谓前所未有。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "如今能有此变化，\x01",
            "最大的要因应该就是\x01",
            "对警察有着深刻理解的索妮亚司令了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2178")

    Jump("loc_251F")

    label("loc_217D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_22D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227A")

    #C0064
    ChrTalk(
        0x8,
        (
            "自从前任局长下台，\x01",
            "迪塔先生就任为市长之后，\x01",
            "警察局的体制有了很大改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "虽然也出现了很多新的困难，\x01",
            "但仍能明显感觉到前进的脚步。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "我想，今后一定会更加需要\x01",
            "各位的努力，\x01",
            "请继续加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "我们也会全力\x01",
            "支持你们的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_22D3")

    label("loc_227A")


    #C0068
    ChrTalk(
        0x8,
        (
            "我想，今后一定会更加需要\x01",
            "各位的努力，\x01",
            "请继续加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "我们也会全力\x01",
            "支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D3")

    Jump("loc_251F")

    label("loc_22D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_251F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_END)), "loc_2497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240A")

    #C0070
    ChrTalk(
        0x8,
        (
            "有关新型魔兽的报告\x01",
            "也有增加的趋势……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "为了把握其特性，从而制定安全对策，\x01",
            "希望能尽可能地收集更多的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "与以往一样，总部会阶段性地\x01",
            "支付一定奖励，\x01",
            "还请各位多加协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "另外，还可以在这里确认\x01",
            "教团终端中的资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "想要查阅的时候，\x01",
            "只要来找我就可以了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2492")

    label("loc_240A")


    #C0075
    ChrTalk(
        0x8,
        (
            "提交战斗手册中的情报后，\x01",
            "总部会支付一定的奖励津贴，\x01",
            "请各位多加协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "另外，如果想查阅\x01",
            "教团终端中的资料，\x01",
            "只要来找我就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2492")

    Jump("loc_251F")

    label("loc_2497")


    #C0077
    ChrTalk(
        0x8,
        (
            "呵呵，话说回来，\x01",
            "竟然会接到一科的协助请求，\x01",
            "各位可真是混出头了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "身为一名见证了特别任务\x01",
            "支援科活跃历程的人，\x01",
            "不由得感慨良多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251F")

    Return()

    # Function_7_13D6 end

    def Function_8_2520(): pass

    label("Function_8_2520")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_252E")
    SetScenarioFlags(0x1, 3)

    label("loc_252E")

    Return()

    # Function_8_2520 end

    def Function_9_252F(): pass

    label("Function_9_252F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_25A1")

    #C0079
    ChrTalk(
        0x8,
        (
            "啊，你们把『结晶碎片』\x01",
            "带来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "为了解析教团终端中的资料，\x01",
            "可以把『结晶碎片』\x01",
            "交给鉴定科吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A1")


    #C0081
    ChrTalk(
        0x101,
        "#00000F嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "好，请稍等一下。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_25DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F67")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_3F62")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber('结晶碎片', 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2662")
    Sound(9, 0, 100, 0)

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情报终端的资料\x01",
            "『关于教团』的第一页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2662")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26BA")
    Sound(9, 0, 100, 0)

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情报终端的资料\x01",
            "『关于教团』的第三页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_26BA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2712")
    Sound(9, 0, 100, 0)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第一页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2712")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_276A")
    Sound(9, 0, 100, 0)

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第二页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_276A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7A")
    Sound(9, 0, 100, 0)

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情报终端的资料\x01",
            "『关于教团』的第四页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情报终端的资料\x01",
            "『关于教团』已经全部解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(1000, 0)
    OP_0D()

    #C0089
    ChrTalk(
        0x8,
        (
            "#5P第０１情报终端的全部资料\x01",
            "已经解析完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#5P要立刻查阅吗？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#12P#00001F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 11)

    #C0092
    ChrTalk(
        0x8,
        (
            "#5P……这些资料中\x01",
            "似乎记载了有关教团的\x01",
            "基本概要呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "#5P否定女神的教义……\x01",
            "真是让人难以置信。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯……\x01",
            "不过，确实与约亚西姆·琼塔\x01",
            "的证言一致。\x02\x03",

            "#00001F另外，『Ｄ』这个字眼……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AB8")

    #C0095
    ChrTalk(
        0x103,
        (
            "#12P#00203F应该就是指代他们否定女神\x01",
            "而信奉的所谓『真神』吧。\x02\x03",

            "#00201F在Ｄ∴Ｇ教团的名称中，\x01",
            "『Ｇ』是指『真知』，\x01",
            "这是之前就了解的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2A6F")

    #C0096
    ChrTalk(
        0x105,
        (
            "#12P#10403F嗯，这样的话，『Ｄ∴Ｇ』的含义\x01",
            "总算是已经解明了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB3")

    label("loc_2A6F")


    #C0097
    ChrTalk(
        0x105,
        (
            "#12P#10303F嗯，如此一来，『Ｄ∴Ｇ』的含义\x01",
            "也算是彻底解明了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB3")

    Jump("loc_2B72")

    label("loc_2AB8")


    #C0098
    ChrTalk(
        0x103,
        (
            "#12P#00200F应该就是指代他们否定女神\x01",
            "而信奉的所谓『真神』吧。\x02\x03",

            "#00201F在Ｄ∴Ｇ教团的名称中，\x01",
            "『Ｇ』是指『真知』，\x01",
            "这是之前就了解的……\x02\x03",

            "这样一来，『Ｄ∴Ｇ』的含义\x01",
            "总算是完全解明了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B72")


    #C0099
    ChrTalk(
        0x102,
        (
            "#12P#00108F说起来……\x01",
            "约亚西姆医生说过，小琪雅\x01",
            "『将会成为真正的神』吧。\x02\x03",

            "既然如此，『Ｄ』\x01",
            "不就是指代\x01",
            "小琪雅的字眼了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C54")

    #C0100
    ChrTalk(
        0x109,
        (
            "#12P#10101F约亚西姆·琼塔\x01",
            "究竟了解多少隐情……\x02\x03",

            "……我们目前还无法得知啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D14")

    label("loc_2C54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CC8")

    #C0101
    ChrTalk(
        0x104,
        (
            "#12P#00301F约亚西姆那混帐\x01",
            "到底知道多少隐情……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        "#12P#10101F……我们目前还无法得知啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D14")

    label("loc_2CC8")


    #C0103
    ChrTalk(
        0x104,
        (
            "#12P#00301F约亚西姆那混帐\x01",
            "到底了解多少隐情……\x02\x03",

            "我们目前还无法得知啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D14")


    #C0104
    ChrTalk(
        0x101,
        (
            "#12P#00001F阿奈斯特先生\x01",
            "似乎也没有从约亚西姆口中\x01",
            "得知一切……\x02\x03",

            "#00003F当时要是能将他顺利逮捕就好了……\x01",
            "现在想想，真是越来越懊恼了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DFA")

    #C0105
    ChrTalk(
        0x8,
        (
            "#5P……总之，只要继续\x01",
            "解析这些资料，\x01",
            "应该就能了解到各种内情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7A")

    label("loc_2DFA")


    #C0106
    ChrTalk(
        0x8,
        (
            "#5P……总之，只要继续\x01",
            "解析这些资料，\x01",
            "应该就能了解到各种内情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "#5P把剩下的『结晶碎片』\x01",
            "也拿来解析一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_2E7A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED2")
    Sound(9, 0, 100, 0)

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第三页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2ED2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2A")
    Sound(9, 0, 100, 0)

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情报终端的资料\x01",
            "『关于圣子』的第一页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2F2A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E6")
    Sound(9, 0, 100, 0)

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第四页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』已经全部解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(1000, 0)
    OP_0D()

    #C0112
    ChrTalk(
        0x8,
        (
            "#5P第０２情报终端的全部资料\x01",
            "已经解析完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "#5P要立刻查阅吗？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#12P#00001F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 12)

    #C0115
    ChrTalk(
        0x8,
        (
            "#5P……在这些资料中，\x01",
            "似乎详细记录了有关那个\x01",
            "『真知』的信息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#5P可以提高服用者的身体能力与感应力，\x01",
            "进而引发出潜在能力\x01",
            "的药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#5P而且还会造成『魔人化』现象，\x01",
            "真是种充满谜团的药物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#00001F作为其原料而使用，\x01",
            "名为『灵智之草』的植物\x01",
            "广泛生长在湿地一带……\x02\x03",

            "约亚西姆曾经前往那里\x01",
            "采摘材料，\x01",
            "这一点也无需怀疑了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3296")

    #C0119
    ChrTalk(
        0x102,
        (
            "#12P#00101F另外，根据资料中的某一段记录，\x01",
            "『真知』正是让他们信奉的所谓真神……\x02\x03",

            "也就是『Ｄ』复活\x01",
            "所需要的药物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x109,
        (
            "#12P#10108F老实说，听起来\x01",
            "完全就是些荒唐的无稽之谈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_3296")


    #C0121
    ChrTalk(
        0x102,
        (
            "#12P#00101F另外，根据资料中的某一段记录，\x01",
            "『真知』正是让他们信奉的所谓真神……\x02\x03",

            "也就是『Ｄ』复活\x01",
            "所需要的药物呢。\x02\x03",

            "#00108F老实说，听起来\x01",
            "完全就是些荒唐的无稽之谈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3341")


    #C0122
    ChrTalk(
        0x103,
        (
            "#12P#00201F话虽如此，但教团在这五百年间，\x01",
            "一直以『仪式』的形式\x01",
            "进行着『真知』的研究……\x02\x03",

            "#00203F……虽然我幸运地被盖伊先生所救，\x01",
            "不过至今为止，已经有无数人\x01",
            "成为了他们的牺牲品。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#12P#00301F可在他们的眼里，\x01",
            "却仅仅是『这点牺牲』而已……\x02\x03",

            "真是一群无可救药的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_352E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_34A9")

    #C0124
    ChrTalk(
        0x105,
        (
            "#12P#10403F……而且，瓦鲁多最近\x01",
            "也服用了『真知』……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E3")

    label("loc_34A9")


    #C0125
    ChrTalk(
        0x105,
        (
            "#12P#10303F……而且，瓦鲁多最近\x01",
            "也服用了『真知』呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E3")


    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#00001F嗯……虽然教团已经不复存在了，\x01",
            "但似乎还是需要注意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_359E")

    label("loc_352E")


    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#00003F……而且，瓦鲁多最近\x01",
            "也服用了『真知』。\x02\x03",

            "#00001F虽然教团已经不复存在了，\x01",
            "但似乎还是需要注意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_359E")


    #C0128
    ChrTalk(
        0x102,
        (
            "#12P#00101F嗯……确实如此。\x02\x03",

            "不仅是『真知』，\x01",
            "像这样的违禁药物，\x01",
            "我们警察都要严厉取缔才行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3660")

    #C0129
    ChrTalk(
        0x8,
        "#5P嗯，的确如此。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#5P……总之，关于『真知』的内容\x01",
            "就只有这些了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E6")

    label("loc_3660")


    #C0131
    ChrTalk(
        0x8,
        "#5P嗯，的确如此。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#5P……总之，关于『真知』的内容\x01",
            "就只有这些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "#5P把剩下的『结晶碎片』\x01",
            "也拿来解析一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_36E6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373E")
    Sound(9, 0, 100, 0)

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情报终端的资料\x01",
            "『关于圣子』的第２页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_373E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F62")
    Sound(9, 0, 100, 0)

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情报终端的资料\x01",
            "『关于圣子』的第３页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情报终端的资料\x01",
            "『关于圣子』已经全部解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    SetScenarioFlags(0x12A, 6)
    FadeToBright(1000, 0)
    OP_0D()

    #C0137
    ChrTalk(
        0x8,
        (
            "#5P第０３情报终端的全部资料\x01",
            "已经解析完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        "#5P要立刻查阅吗？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#12P#00001F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 13)

    #C0140
    ChrTalk(
        0x8,
        (
            "#5P这些内容……\x01",
            "似乎都和支援科看护的\x01",
            "小琪雅有关……？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#12P#00003F五百年前，库罗伊斯家族\x01",
            "创造了琪雅……\x01",
            "并将她作为信仰对象交给了教团。\x02\x03",

            "此后，她就作为象征着神的『圣子』，\x01",
            "一直沉睡在摇篮之中……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#12P#00101F……即使是教团中的成员，\x01",
            "也不了解其中的真相呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#12P#00203F库罗伊斯家族为了达到真正目的，\x01",
            "在暗中诱导着他们。而他们却毫无察觉，\x01",
            "一直都在盲目追寻着虚无缥缈的『真神』……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A68")

    #C0144
    ChrTalk(
        0x106,
        "#12P#10708F……从某种意义上说，也是一群可怜的人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF1")

    label("loc_3A68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AB6")

    #C0145
    ChrTalk(
        0x109,
        "#12P#10108F……从某种意义上说，也是一群可怜的人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF1")

    label("loc_3AB6")


    #C0146
    ChrTalk(
        0x105,
        "#12P#10408F……从某种意义上说，也是一群可怜的家伙呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B4C")

    #C0147
    ChrTalk(
        0x10A,
        (
            "#12P#00603F但只要想想那群家伙做过的事情，\x01",
            "就实在是同情不起来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE3")

    label("loc_3B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B9F")

    #C0148
    ChrTalk(
        0x105,
        (
            "#12P#10403F但想想他们的所作所为，\x01",
            "便也没有同情的余地了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE3")

    label("loc_3B9F")


    #C0149
    ChrTalk(
        0x109,
        (
            "#12P#10103F但只要想想他们做过的事情，\x01",
            "也就没有同情的必要了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE3")


    #C0150
    ChrTalk(
        0x101,
        (
            "#12P#00001F教团的成员暂且不说……\x01",
            "琪雅可是没有任何罪过的。\x02\x03",

            "#00003F就算她是库罗伊斯家族为了\x01",
            "达成自己的目的而制造出来的……\x02\x03",

            "就算她拥有\x01",
            "不可思议的能力……\x01",
            "那一切也都与她无关。\x02\x03",

            "在我们的眼前醒来的琪雅，\x01",
            "只是一个有血有肉的普通女孩。\x02\x03",

            "#00001F这样一个普通的孩子，却被独自关在\x01",
            "那种地方长达数百年……\x02\x03",

            "直到现在，她还继续被\x01",
            "玛丽亚贝尔小姐和\x01",
            "伊安律师利用着。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#12P#00301F……无论有任何理由，\x01",
            "我们也绝对不能任由这种事情发生。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "#5P……有关教团的资料\x01",
            "已经全部解析完毕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#5P我对此次事件的了解\x01",
            "虽然不像各位一样详细……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#5P但琪雅对你们而言\x01",
            "有多么重要，我却有着\x01",
            "深切的体会。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#5P请各位……多加努力。\x01",
            "我也会默默支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#12P#00000F谢谢了，瑞贝卡小姐。\x02\x03",

            "#00003F我们绝对会凭借自己的双手\x01",
            "把琪雅带回来。\x02\x03",

            "#00001F一定要努力创造出让琪雅……\x01",
            "让我们最疼爱的那个孩子\x01",
            "可以欢笑生活的未来……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F3A")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_3F3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F53")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_3F53")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)
    TalkEnd(0x8)

    label("loc_3F62")

    Jump("loc_25DE")

    label("loc_3F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405A")
    FadeToBright(1000, 0)
    OP_0D()

    #C0157
    ChrTalk(
        0x8,
        (
            "#5P如果今后取得了新的『结晶碎片』，\x01",
            "请拿到我这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "#5P如果想再次查阅已经解析过的资料，\x01",
            "也可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_403B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_403B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4054")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4054")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_405A")

    Return()

    # Function_9_252F end

    def Function_10_405B(): pass

    label("Function_10_405B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4065")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_414D")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【关于教团】\x01",      # 0
            "【关于真知】\x01",      # 1
            "【关于圣子】\x01",      # 2
            "【放弃】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4100"),
        (1, "loc_410E"),
        (2, "loc_411C"),
        (3, "loc_412A"),
        (SWITCH_DEFAULT, "loc_4139"),
    )


    label("loc_4100")

    Sound(72, 0, 100, 0)
    Call(0, 11)
    Jump("loc_4148")

    label("loc_410E")

    Sound(72, 0, 100, 0)
    Call(0, 12)
    Jump("loc_4148")

    label("loc_411C")

    Sound(72, 0, 100, 0)
    Call(0, 13)
    Jump("loc_4148")

    label("loc_412A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4148")

    label("loc_4139")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4148")

    label("loc_4148")

    Jump("loc_4065")

    label("loc_414D")

    Return()

    # Function_10_405B end

    def Function_11_414E(): pass

    label("Function_11_414E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D5")
    SetChrName("")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于教团』\x01\x01",
            "我的名字是约亚西姆·琼塔。\x01",
            "隶属于『Ｄ∴Ｇ教团』的干部祭司。\x01",
            "六年前，在众多势力与游击士共同联手之下，\x01",
            "我们的教团被毁灭了。\x01",
            "但是，唯有我逃了出来，\x01",
            "并来到了这片■■之地。\x01",
            "在伟大的『■』的引导下，\x01",
            "为了完成教团的伟业，我努力坚持了下来。\x01",
            "那一刻终将到来──\x01",
            "为了留下书写新时代圣典所用的资料，\x01",
            "我决定把这些数据保存在各个终端之上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4436")

    label("loc_42D5")

    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于教团』\x01\x01",
            "我的名字是约亚西姆·琼塔。\x01",
            "隶属于『Ｄ∴Ｇ教团』的干部祭司。\x01",
            "六年前，在众多势力与游击士共同联手之下，\x01",
            "我们的教团被毁灭了。\x01",
            "但是，唯有我逃了出来，\x01",
            "并来到了这片起源之地。\x01",
            "在伟大的『Ｄ』的引导下，\x01",
            "为了完成教团的伟业，我努力坚持了下来。\x01",
            "那一刻终将到来──\x01",
            "为了留下书写新时代圣典所用的资料，\x01",
            "我决定把这些数据保存在各个终端之上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4436")

    SetChrName("")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S首先，从我们教团的成立说起吧。\x01",
            "关于这件事，有必要回顾一下\x01",
            "塞姆里亚大陆那段骇人听闻的历史。\x01\x01",
            "经历了大约在一千两百年前发生的\x01",
            "『大崩坏』，大陆失去了高度的文明与秩序，\x01",
            "迎来了被战争与贫困支配的『黑暗时代』。\x01",
            "最终，精疲力尽的人们\x01",
            "犯下了巨大的错误。\x01\x01",
            "被突然出现的愚蠢之人的花言巧语迷惑，\x01",
            "接受了那些人创造的，\x01",
            "毫无道理的秩序。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_46FB")
    SetChrName("")

    #A0163
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S即──愚蠢的■■■■\x01",
            "与象征着其信仰的『■之■■』。\x01",
            "他们创造的秩序使『黑暗时代』终结，\x01",
            "但这种信仰也散播到了大陆各处……\x01\x01",
            "可是，请仔细想一想。\x01",
            "如果『■■』真的存在，\x01",
            "每个人不是应该都能得到平等的救赎吗？\x01",
            "然而，差距这种概念并没有消失，\x01",
            "依然不断有人因为灾难与不幸而丧命。\x01\x01",
            "『■■』在赐予救赎时，难道是有选择性的吗？\x01",
            "这未免也太过愚蠢可笑了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_485E")

    label("loc_46FB")

    SetChrName("")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S即──愚蠢的七耀教会\x01",
            "与象征着其信仰的『空之女神』。\x01",
            "他们创造的秩序使『黑暗时代』终结，\x01",
            "但这种信仰也散播到了大陆各处……\x01\x01",
            "可是，请仔细想一想。\x01",
            "如果『女神』真的存在，\x01",
            "每个人不是应该都能得到平等的救赎吗？\x01",
            "然而，差距这种概念并没有消失，\x01",
            "依然不断有人因为灾难与不幸而丧命。\x01\x01",
            "『女神』在赐予救赎时，难道是有选择性的吗？\x01",
            "这未免也太过愚蠢可笑了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_485E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49B4")
    SetChrName("")

    #A0165
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S其实，那不过就是■■■■为了得到权势，\x01",
            "而人为创造出来的虚幻存在罢了。\x01",
            "『■■』这种东西，是不可能存在的。\x01\x01",
            "我们那些终于寻得真理的前辈们，\x01",
            "为了与『■■』相遇，踏上了漫长的旅途。\x01\x01",
            "时代不断变迁，当中世纪来临时，\x01",
            "他们终于发现了……\x01",
            "在这地底深处，■■■■■■■■■■\x01",
            "■■■■■■■■……\x01\x01",
            "『■』──便是其名字。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4AF7")

    label("loc_49B4")

    SetChrName("")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S其实，那不过就是七耀教会为了得到权势，\x01",
            "而人为创造出来的虚幻存在罢了。\x01",
            "『女神』这种东西，是不可能存在的。\x01\x01",
            "我们那些终于寻得真理的前辈们，\x01",
            "为了与『真神』相遇，踏上了漫长的旅途。\x01\x01",
            "时代不断变迁，当中世纪来临时，\x01",
            "他们终于发现了……\x01",
            "在这地底深处，蕴藏着伟大力量的东西\x01",
            "正在安祥地长眠中……\x01\x01",
            "『Ｄ』──便是其名字。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4AF7")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_414E end

    def Function_12_4B0B(): pass

    label("Function_12_4B0B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C8A")
    SetChrName("")

    #A0167
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于真知』\x01\x01",
            "『真知』……是以盛开在\x01",
            "■■■■■的■■■■■■■■\x01",
            "『灵智之草』为原料制成的秘药。\x01\x01",
            "它的调配方法■■■■■■■■■■，\x01",
            "服用之后，可以提高身体能力与感应力，\x01",
            "更拥有激发出人体潜在能力的效果。\x01",
            "■■■■■■■■■■■■■■■■■。\x01",
            "■■■■■■■■■■■■■■■。\x01",
            "『真知』是可以将■■■的■■\x01",
            "■■■『■』的■■的药物。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4DE3")

    label("loc_4C8A")

    SetChrName("")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于真知』\x01\x01",
            "『真知』……是以盛开在\x01",
            "七耀脉之上的传说中的植物——\x01",
            "『灵智之草』为原料而制成的秘药。\x01\x01",
            "它的调配方法与『Ｄ』一同传承下来，\x01",
            "服用之后，可以提高身体能力与感应力，\x01",
            "更拥有激发出人体潜在能力的效果。\x01",
            "不过，那些仅仅是不值一提的辅助作用而已。\x01",
            "此药物的真正力量不止于此。\x01",
            "『真知』是为了将服用者的精神\x01",
            "接续至『Ｄ』的核心的药物。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4DE3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F39")
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『■』拥有通过将■■■的■■进行■■，\x01",
            "储存■■，并获得■■的性质。\x01",
            "当那■■达到『■■』的境界之时，\x01",
            "『■』就会■■。\x01\x01",
            "另外，『真知』\x01",
            "尚有改良的余地。\x01",
            "■■■■■■■■■■■■■■■，\x01",
            "就可以■■■■■■■■■『■』。\x01\x01",
            "在随后的■■■■，我们教团一直\x01",
            "在对更具效果的『真知』进行研究……\x01",
            "即举行所谓的『仪式』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_507C")

    label("loc_4F39")

    SetChrName("")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『Ｄ』拥有通过将服用者的精神进行聚合，\x01",
            "储存知识，并获得成长的性质。\x01",
            "当那知识达到『睿智』的境界之时，\x01",
            "『Ｄ』就会复活。\x01\x01",
            "另外，『真知』\x01",
            "尚有改良的余地。\x01",
            "如果能将服用者的能力引发至极限，\x01",
            "就可以将更多的知识贡献给『Ｄ』。\x01\x01",
            "在随后的五百年间，我们教团一直\x01",
            "在对更具效果的『真知』进行研究……\x01",
            "即举行所谓的『仪式』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_507C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51BE")
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S因此，■■■■的■■\x01",
            "■■■■■■■■■■■■■，\x01",
            "虽然『真知』已经接近完成，\x01",
            "但就在只差一步的关头，出现了差错。\x01\x01",
            "由于实验规模太过庞大，\x01",
            "所以被游击士及其它势力所察觉，\x01",
            "各据点，以及整个教团，\x01",
            "因此步入毁灭。\x01\x01",
            "不得不说，这确实太过愚蠢了。\x01",
            "但为了『■■』的■■，\x01",
            "多少有点牺牲也是免不了的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_52ED")

    label("loc_51BE")

    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S因此，研究进展的速度\x01",
            "是五百年前起步时无法比拟的，\x01",
            "虽然『真知』已经接近完成，\x01",
            "但就在只差一步的关头，出现了差错。\x01\x01",
            "由于实验规模太过庞大，\x01",
            "所以被游击士及其它势力所察觉，\x01",
            "各据点，以及整个教团，\x01",
            "因此步入毁灭。\x01\x01",
            "不得不说，这确实太过愚蠢了。\x01",
            "但为了『真神』的复活，\x01",
            "多少有点牺牲也是免不了的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_52ED")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_545B")
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S我从已经覆灭的据点中\x01",
            "秘密回收了实验资料，\x01",
            "并来到了克洛斯贝尔这个■■之地。\x01\x01",
            "由于『真知』的材料\x01",
            "『灵智之草』■■生长在■■■■■■■\x01",
            "的■■■■，所以■■\x01",
            "■■■■■并没有任何困难。\x01",
            "此外，在这『太阳堡垒』的深层地带，\x01",
            "有着■■■的■■■■■■的研究设施，\x01",
            "备有众多先进设备。\x01",
            "如此一来，我拥有了完美的研究环境，\x01",
            "最后终于将秘药彻底完成。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_55B6")

    label("loc_545B")

    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S我从已经覆灭的据点中\x01",
            "秘密回收了实验资料，\x01",
            "并来到了克洛斯贝尔这个起源之地。\x01\x01",
            "由于『真知』的材料\x01",
            "『灵智之草』大量生长在克洛斯贝尔南部\x01",
            "的湿地一带，所以采集\x01",
            "材料的工作并没有任何困难。\x01",
            "此外，在这『太阳堡垒』的深层地带，\x01",
            "有着中世纪的炼金术师建造的研究设施，\x01",
            "备有众多先进设备。\x01",
            "如此一来，我拥有了完美的研究环境，\x01",
            "最后终于将秘药彻底完成。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_55B6")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_12_4B0B end

    def Function_13_55CA(): pass

    label("Function_13_55CA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_572B")
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于圣子』\x01\x01",
            "克洛斯贝尔不仅是我们『Ｄ∴Ｇ教团』\x01",
            "的■■■，而且也是■■■■。\x01",
            "这是■■，■■■■■■■■■■■\x01",
            "■■■『圣子』■。\x01\x01",
            "所谓『圣子』，是『■■』■■■，\x01",
            "■■■■■■『Ｄ∴Ｇ教团』。\x01",
            "■『太阳堡垒』■■■■■■■■，\x01",
            "■■■■■■■■，\x01",
            "■■■■■■■『太阳堡垒』\x01",
            "■■■■■■■■■■■■。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5866")

    label("loc_572B")

    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于圣子』\x01\x01",
            "克洛斯贝尔不仅是我们『Ｄ∴Ｇ教团』\x01",
            "的根据地，而且也是起源之地。\x01",
            "这是因为，我们就是在此地从始祖处\x01",
            "继承了『圣子』的。\x01\x01",
            "所谓『圣子』，是『真神』的宿主，\x01",
            "也象征着我们『Ｄ∴Ｇ教团』。\x01",
            "在『太阳堡垒』地下沉睡着的圣子，\x01",
            "外表形如人类少女，\x01",
            "五百年间一直在『太阳堡垒』\x01",
            "的祭坛等待着醒来的那一天。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5866")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_59BC")
    SetChrName("")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S■■竟能■■如此■■的■■，\x01",
            "对凡夫俗子而言，也许难以置信吧。\x01\x01",
            "但是，我确实曾经亲眼见证过。\x01",
            "在被称作『■■■■■』的■■之■\x01",
            "■■■■■■■──\x01",
            "那神圣的■■。\x01\x01",
            "『■■■■■』是■■■■■\x01",
            "以■■『古代遗物』的■■■■的■■为基础，\x01",
            "从而■■■■■。\x01",
            "既然如此，这■■■■■■■■■■\x01",
            "也就没什么不可思议的了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5B01")

    label("loc_59BC")

    SetChrName("")

    #A0178
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S人类竟能存活如此长久的时间，\x01",
            "对凡夫俗子而言，也许难以置信吧。\x01\x01",
            "但是，我确实曾经亲眼见证过。\x01",
            "在被称作『神圣的摇篮』的球体之中\x01",
            "一直沉睡的少女──\x01",
            "那神圣的姿态。\x01\x01",
            "『神圣的摇篮』是教团的前人们\x01",
            "以研究『古代遗物』的炼金术师的技术为基础，\x01",
            "从而创造出来的。\x01",
            "既然如此，这可以称之为奇迹的现象\x01",
            "也就没什么不可思议的了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5B01")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C3A")
    SetChrName("")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『圣子』从■■■■■■■，\x01",
            "■■『真知』，■■■\x01",
            "■■■■■■■■■。\x01\x01",
            "■■■『■■』■■■，『圣子』■■■■，\x01",
            "■■■■■『■』。\x01",
            "接下来，■■■■的■■与■■\x01",
            "会归集于『■』之下，\x01",
            "人类将从『■■』的咒缚中解放。\x01\x01",
            "那正是我们『Ｄ∴Ｇ教团』的前人们\x01",
            "留下的预言，终将实现的伟大愿望。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5D60")

    label("loc_5C3A")

    SetChrName("")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『圣子』从诞生的时代开始，\x01",
            "通过『真知』，获取了\x01",
            "可以说是无限的知识。\x01\x01",
            "当达到『睿智』境界时，『圣子』便将苏醒，\x01",
            "并化为真神『Ｄ』。\x01",
            "接下来，全部人类的意志与魂魄\x01",
            "会归集于『Ｄ』之下，\x01",
            "人类将从『女神』的咒缚中解放。\x01\x01",
            "那正是我们『Ｄ∴Ｇ教团』的前人们\x01",
            "留下的预言，终将实现的伟大愿望。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5D60")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_13_55CA end

    def Function_14_5D74(): pass

    label("Function_14_5D74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D99")
    SetChrPos(0xFE, 40, 40, 12610, 0)
    Jump("loc_5E4D")

    label("loc_5D99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DBE")
    SetChrPos(0xFE, -1000, 40, 12400, 0)
    Jump("loc_5E4D")

    label("loc_5DBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DE3")
    SetChrPos(0xFE, 1140, 40, 12400, 0)
    Jump("loc_5E4D")

    label("loc_5DE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E08")
    SetChrPos(0xFE, 110, 0, 11010, 0)
    Jump("loc_5E4D")

    label("loc_5E08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E2D")
    SetChrPos(0xFE, -950, 0, 10770, 0)
    Jump("loc_5E4D")

    label("loc_5E2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E4D")
    SetChrPos(0xFE, 1080, 0, 10720, 0)

    label("loc_5E4D")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_5D74 end

    def Function_15_5E5C(): pass

    label("Function_15_5E5C")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7C")
    BeginChrThread(0x101, 1, 0, 14)

    label("loc_5E7C")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E93")
    BeginChrThread(0x102, 1, 0, 14)

    label("loc_5E93")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EAA")
    BeginChrThread(0x103, 1, 0, 14)

    label("loc_5EAA")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EC1")
    BeginChrThread(0x104, 1, 0, 14)

    label("loc_5EC1")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ED8")
    BeginChrThread(0x109, 1, 0, 14)

    label("loc_5ED8")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EEF")
    BeginChrThread(0x105, 1, 0, 14)

    label("loc_5EEF")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F06")
    BeginChrThread(0x106, 1, 0, 14)

    label("loc_5F06")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F1D")
    BeginChrThread(0x10A, 1, 0, 14)

    label("loc_5F1D")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5F37")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5F37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5F50")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_5F50")

    Return()

    # Function_15_5E5C end

    def Function_16_5F51(): pass

    label("Function_16_5F51")

    ClearScenarioFlags(0x1, 6)
    ClearScenarioFlags(0x1, 7)
    ClearScenarioFlags(0x2, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6187")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FA3")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_5FA3")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FD7")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_5FD7")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_600B")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_600B")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_603F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_603F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6073")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_6073")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60A7")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_60A7")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60DB")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_60DB")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_610F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_6182")

    label("loc_610F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6146")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Jump("loc_6182")

    label("loc_6146")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_617D")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_6182")

    label("loc_617D")

    Jump("loc_6187")

    label("loc_6182")

    Jump("loc_5F64")

    label("loc_6187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_69B4")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(500, 0)
    OP_0D()

    #C0181
    ChrTalk(
        0x8,
        (
            "啊，各位……\x01",
            "你们的战斗手册内容\x01",
            "似乎有了很多更新呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "为了协助总部收集魔兽情报，\x01",
            "可以把手册给我检查一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#0000F#12P嗯，没问题。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0184
    ChrTalk(
        0x8,
        (
            "谢谢，\x01",
            "手册还给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "这是这次的奖励津贴，\x01",
            "请收下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_633C")

    #A0186
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "1个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 1)
    Jump("loc_6635")

    label("loc_633C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6391")

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "2个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 2)
    Jump("loc_6635")

    label("loc_6391")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63E6")

    #A0190
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "3个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 3)
    Jump("loc_6635")

    label("loc_63E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_643B")

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "4个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 4)
    Jump("loc_6635")

    label("loc_643B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6490")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "5个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 5)
    Jump("loc_6635")

    label("loc_6490")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64E5")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "6个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 6)
    Jump("loc_6635")

    label("loc_64E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_653A")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0199
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "7个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 7)
    Jump("loc_6635")

    label("loc_653A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_658F")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "8个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 8)
    Jump("loc_6635")

    label("loc_658F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E4")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "9个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 9)
    Jump("loc_6635")

    label("loc_65E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6635")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "10个收下了。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 10)

    label("loc_6635")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6669")
    Sound(17, 0, 100, 0)

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "2个收下了。\x02",
        )
    )

    AddItemNumber('神圣布料', 2)
    CloseMessageWindow()
    Jump("loc_6694")

    label("loc_6669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6694")
    Sound(17, 0, 100, 0)

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('神圣布料', 1)
    CloseMessageWindow()

    label("loc_6694")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67B5")

    #C0208
    ChrTalk(
        0x8,
        (
            "如果今后收集到了更多的魔兽情报，\x01",
            "请再拿来给我看哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        "#12P#0000F好的，那到时就麻烦了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_674B")

    #C0210
    ChrTalk(
        0x102,
        "#12P#0100F下次再来打扰啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67B0")

    label("loc_674B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_677E")

    #C0211
    ChrTalk(
        0x103,
        "#12P#0200F下次再来打扰。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67B0")

    label("loc_677E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67B0")

    #C0212
    ChrTalk(
        0x104,
        "#12P#0300F下次再来打扰你啦。\x02",
    )

    CloseMessageWindow()

    label("loc_67B0")

    Jump("loc_694C")

    label("loc_67B5")


    #C0213
    ChrTalk(
        0x8,
        (
            "你们也收集了很多\x01",
            "新型魔兽的情报啊。\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "如此一来，今后应该就能制定出\x01",
            "更加完善的安全对策了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#12P#0000F哈哈……能帮上忙，是我们的荣幸。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "呵呵，真是多谢各位\x01",
            "的协助了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "那么，这次就将\x01",
            "特别报酬交给你们，\x01",
            "请一定要收下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１００００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    #C0219
    ChrTalk(
        0x8,
        (
            "期待各位今后\x01",
            "的活跃表现。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "如果遇到什么事情，\x01",
            "随时都可以过来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_694C")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_6963")
    ClearScenarioFlags(0x1, 5)

    label("loc_6963")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_697C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_697C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6995")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_6995")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_6A98")

    label("loc_69B4")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A31")

    #C0221
    ChrTalk(
        0x8,
        (
            "总部收集的情报\x01",
            "已经足够了，\x01",
            "所以调查就到此为止。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "以后也许还有事情\x01",
            "需要麻烦各位，\x01",
            "到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A98")

    label("loc_6A31")


    #C0223
    ChrTalk(
        0x8,
        (
            "战斗手册上好像\x01",
            "没有新内容呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "收集到更多的情报之后\x01",
            "再来拿给我看吧，\x01",
            "我们会将情报记录整理的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A98")

    Return()

    # Function_16_5F51 end

    def Function_17_6A99(): pass

    label("Function_17_6A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AC2")
    Call(0, 18)
    Jump("loc_6BBE")

    label("loc_6AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ADD")
    Call(0, 18)
    Jump("loc_6BBE")

    label("loc_6ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AF3")
    Call(0, 18)
    Jump("loc_6BBE")

    label("loc_6AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B09")
    Call(0, 18)
    Jump("loc_6BBE")

    label("loc_6B09")

    TalkBegin(0x9)

    #C0225
    ChrTalk(
        0x9,
        (
            "#01900F大家知道名叫『波波碰！』\x01",
            "的导力游戏吗～？\x02\x03",

            "#01909F呵呵，其实我也已经开始玩了。\x01",
            "不介意的话，互相留个账号吧～\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『芙兰的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    TalkEnd(0x9)

    label("loc_6BBE")

    Jump("loc_6BC6")

    label("loc_6BC3")

    Call(0, 18)

    label("loc_6BC6")

    Return()

    # Function_17_6A99 end

    def Function_18_6BC7(): pass

    label("Function_18_6BC7")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6BD8")
    Jump("loc_85F0")

    label("loc_6BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6BE6")
    Jump("loc_85F0")

    label("loc_6BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6E06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D79")
    SoundLoad(803)

    #C0227
    ChrTalk(
        0x9,
        (
            "#01901F各、各位……\x01",
            "真是不得了了呢。\x02\x03",

            "警察总部这边从今天一大早开始\x01",
            "就忙得焦头烂额……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0228
    ChrTalk(
        0x9,
        "#01905F啊，不好意思。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    OP_24(0x323)
    Sound(804, 0, 100, 0)

    #C0229
    ChrTalk(
        0x9,
        (
            "#01903F您好，这里是克洛斯贝尔警察局。\x02\x03",

            "#01901F好的、好的……\x02\x03",

            "是的，从昨晚开始，\x01",
            "警备队就开始控制事态……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#00001F（实在是很忙啊……）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        (
            "#00101F（嗯，我们也赶快去做\x01",
            "  自己该做的事情吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 7)
    OP_24(0x323)
    Jump("loc_6E01")

    label("loc_6D79")

    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "芙兰正在用通讯器进行联络。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0233
    ChrTalk(
        0x9,
        (
            "#01901F好的、好的……\x02\x03",

            "#01908F……实在抱歉。\x01",
            "关于武装集团的来历，\x01",
            "目前还不明确……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E01")

    Jump("loc_85F0")

    label("loc_6E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_6EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E21")
    Call(0, 21)
    Jump("loc_6EBE")

    label("loc_6E21")


    #C0234
    ChrTalk(
        0x9,
        (
            "#01900F正如之前联络时所说，\x01",
            "导力艇已经停靠在了\x01",
            "港湾区的码头～\x02\x03",

            "#01904F维修员先生应该\x01",
            "就在船附近等你们，\x01",
            "请过去找他就好了～！\x02\x03",

            "#01900F一路小心啊，各位！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EBE")

    Jump("loc_85F0")

    label("loc_6EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_712B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_709E")

    #C0235
    ChrTalk(
        0x9,
        (
            "#01900F各位，昨天真是\x01",
            "辛苦啦～\x02\x03",

            "有关那个名为『结社』的组织，\x01",
            "还有列车事故的原因，\x01",
            "各位都取得了很重要的情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#00006F哪里，其实我们\x01",
            "并没做什么啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#00100F是啊，在处理事故的工作中，\x01",
            "还是那些通宵作业的人员\x01",
            "更加辛苦。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x9,
        (
            "#01904F话虽如此，但各位\x01",
            "昨天的调查行动\x01",
            "也一直持续到了很晚吧。\x02\x03",

            "#01902F要注意休息，\x01",
            "不要操劳过度哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x103,
        "#00202F多谢关心。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#00302F要说忙的话，芙兰也是一样啊。\x01",
            "你也别太勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x9,
        "#01909F是的，知道啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 0)
    Jump("loc_7126")

    label("loc_709E")


    #C0242
    ChrTalk(
        0x9,
        (
            "#01900F今天也接到了\x01",
            "好几件支援请求……\x02\x03",

            "请大家量力而行，\x01",
            "在力所能及的范围内加油吧。\x02\x03",

            "我也会把握尺度，\x01",
            "在不勉强自己的前提下努力的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7126")

    Jump("loc_85F0")

    label("loc_712B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7264")
    SetChrName("")

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "芙兰正在用通讯器进行联络。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0244
    ChrTalk(
        0x9,
        (
            "#01903F是的、是的……\x02\x03",

            "#01901F……真是抱歉。\x01",
            "关于事故发生的原因，\x01",
            "目前还在调查过程中……\x02\x03",

            "关于恢复运行的时间，\x01",
            "目前还无法……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#00001F（看来是正在处理\x01",
            "  列车事故方面的问题啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#00101F（嗯，看起来非常忙，\x01",
            "  还是不要打扰她了吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7310")

    label("loc_7264")

    SetChrName("")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "芙兰正在用通讯器进行联络。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0248
    ChrTalk(
        0x9,
        (
            "#01903F是的、是的……\x02\x03",

            "#01901F……真是抱歉。\x01",
            "关于事故发生的原因，\x01",
            "目前还在调查过程中……\x02\x03",

            "关于恢复运行的时间，\x01",
            "目前还无法……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7310")

    Jump("loc_85F0")

    label("loc_7315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_74B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73FD")

    #C0249
    ChrTalk(
        0x9,
        (
            "#01903F蓝色的花，还有幻兽……\x02\x03",

            "#01901F不知为何，总有种不祥的感觉呢。\x01",
            "总之，我们现在也只能\x01",
            "尽力而为。\x02\x03",

            "那个……各位，\x01",
            "请一定要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#00000F嗯，多谢。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x109,
        "#10100F也拜托芙兰继续协助我们啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_74AB")

    label("loc_73FD")


    #C0252
    ChrTalk(
        0x9,
        (
            "#01903F由于独立提案而造成的紧张状态也罢，\x01",
            "还有这次的异常事态也罢，\x01",
            "总让人有种不祥的感觉呢。\x02\x03",

            "#01901F但想得太多\x01",
            "也没什么用……\x02\x03",

            "总之，我现在也只能\x01",
            "认真处理眼前的工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74AB")

    Jump("loc_85F0")

    label("loc_74B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_773A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76D3")

    #C0253
    ChrTalk(
        0x9,
        (
            "#01901F各位……你们好像正在\x01",
            "调查所谓的『幻兽』吧？\x02\x03",

            "据说和出现在旧矿山的那只类似，\x01",
            "是非常不可思议的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00000F嗯，目前还是\x01",
            "一头雾水呢。\x01",
            "现在也只能先展开调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#10105F嗯？你好像有些不安？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "#01906F嗯……因为我听说\x01",
            "幻兽非常强大……\x01",
            "希望各位不要受伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x109,
        (
            "#10103F嗯，确实如此呢。\x02\x03",

            "#10100F不过我们不会勉强行事的，\x01",
            "不必那么担心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x9,
        (
            "#01904F嗯……说得也是。\x02\x03",

            "毕竟各位是经过\x01",
            "百般磨练的特别任务支援科嘛。\x02\x03",

            "#01909F芙兰·希卡相信\x01",
            "大家的实力，\x01",
            "在此等待各位的报告！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，谢谢啦，\x01",
            "小芙兰。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 1)
    Jump("loc_7735")

    label("loc_76D3")


    #C0260
    ChrTalk(
        0x9,
        (
            "#01902F各位，在调查幻兽时\x01",
            "请一定要小心哦。\x02\x03",

            "芙兰·希卡相信\x01",
            "大家的实力，\x01",
            "在此等待各位的报告！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7735")

    Jump("loc_85F0")

    label("loc_773A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7755")
    Call(0, 20)
    Jump("loc_794C")

    label("loc_7755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C6")

    #C0261
    ChrTalk(
        0x9,
        (
            "#01900F尤莉亚准校仪表堂堂，\x01",
            "真是太有气质了……\x01",
            "我好崇拜她啊～\x02\x03",

            "#01909F嘿嘿，不过我觉得\x01",
            "还是姐姐更帅气呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x109,
        (
            "#10106F呼，这孩子……\x02\x03",

            "#10101F这话要是被尤莉亚准校的崇拜者们听到，\x01",
            "绝对会暴怒的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，大概吧。\x01",
            "不过，凭你的素质，完全可以拥有\x01",
            "和尤莉亚准校一样多的支持者呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        "#01909F嘿嘿～果然如此吧～！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x109,
        "#10106F饶、饶了我吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_794C")

    label("loc_78C6")


    #C0266
    ChrTalk(
        0x9,
        (
            "#01900F机会难得，\x01",
            "我也好想被安排到兰花塔\x01",
            "参加今天的警备工作啊～\x02\x03",

            "#01906F好想欣赏英姿飒爽的\x01",
            "尤莉亚准校和姐姐\x01",
            "在警备时的样子呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_794C")

    Jump("loc_85F0")

    label("loc_7951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B4A")
    TurnDirection(0x9, 0x109, 0)

    #C0267
    ChrTalk(
        0x9,
        (
            "#01902F啊，姐姐。\x02\x03",

            "你们参加揭幕式的警备工作了吧？\x01",
            "怎么样，是不是很精彩？\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x109,
        (
            "#10109F嗯，是啊。\x02\x03",

            "特别是利贝尔王国的\x01",
            "科洛蒂娅公主和尤莉亚准校，\x01",
            "实在是气质非凡！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x9,
        (
            "#01905F近、近距离看到她们了吗！？\x02\x03",

            "#01906F呜呜，好羡慕啊。\x01",
            "姐姐好狡猾，竟然独自享受～\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x109,
        (
            "#10100F啊哈哈，抱歉啦，芙兰。\x01",
            "下次要是有机会，一定好好补偿你。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈，芙兰果然也是\x01",
            "  尤莉亚准校的崇拜者啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        (
            "#00306F（唔～该说什么好呢，\x01",
            "  让世间男人颜面何存啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 6)
    Jump("loc_7B9F")

    label("loc_7B4A")


    #C0273
    ChrTalk(
        0x9,
        (
            "#01902F科洛蒂娅公主，\x01",
            "还有尤莉娅准校……！\x02\x03",

            "真羡慕啊，我也想\x01",
            "近距离地看看她们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B9F")

    Jump("loc_85F0")

    label("loc_7BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6A")

    #C0274
    ChrTalk(
        0x9,
        (
            "#01902F呵呵，通商会议\x01",
            "明天就要开始啦～\x02\x03",

            "来自各国的首脑们齐聚一堂，\x01",
            "还有兰花塔的揭幕式……\x01",
            "光是想想就让人兴奋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x109,
        (
            "#10106F真是的，你已经不是小孩子了，\x01",
            "不要总说那种幼稚的话，\x01",
            "集中精神工作啦！\x02\x03",

            "#10106F芙兰，在会议召开期间，\x01",
            "你们会比平时更忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        (
            "#01900F是啊，但正是因为如此，\x01",
            "才更需要忙中寻开心嘛。\x02\x03",

            "倒是姐姐你，\x01",
            "总是这样严肃过头～\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x105,
        "#10304F呵呵，说得的确没错呢。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        "#10101F瓦、瓦吉……！\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        "#00012F啊哈哈……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 7)
    Jump("loc_7DD2")

    label("loc_7D6A")


    #C0280
    ChrTalk(
        0x9,
        (
            "#01902F虽然工作确实很忙，\x01",
            "但如此重要的活动\x01",
            "实在是让人兴奋不已啊～\x02\x03",

            "#01909F呵呵，好期待明天的仪式。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD2")

    Jump("loc_85F0")

    label("loc_7DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_7E58")

    #C0281
    ChrTalk(
        0x9,
        (
            "#01901F听比克森镇长说，\x01",
            "旧矿山的内部\x01",
            "似乎出现了异常的情况呢。\x02\x03",

            "虽然还不知道\x01",
            "具体情况……\x01",
            "但一切都拜托大家啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85F0")

    label("loc_7E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_807B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E73")
    Call(0, 19)
    Jump("loc_8076")

    label("loc_7E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FE5")

    #C0282
    ChrTalk(
        0x9,
        (
            "#01906F哈～现在可以随便\x01",
            "叫姐姐了，\x01",
            "真是太好啦～\x02\x03",

            "#01902F这样一来，\x01",
            "就可以集中精神\x01",
            "处理工作了呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x109,
        (
            "#10106F你、你那么讨厌正式称呼，\x01",
            "居然严重到会影响工作的程度……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    #C0284
    ChrTalk(
        0x9,
        (
            "#01901F因为啊，对我来说，\x01",
            "这可是关系到死活的大问题哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x109,
        "#10106F（唉唉，连职场的基本礼节都……）\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#00012F（别、别在意啦，诺艾尔。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8076")

    label("loc_7FE5")


    #C0287
    ChrTalk(
        0x9,
        (
            "#01902F呵呵，这样一来，\x01",
            "就可以集中精神\x01",
            "处理工作了呢～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    #C0288
    ChrTalk(
        0x9,
        (
            "#01909F今天也要加油工作哟，\x01",
            "姐姐⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x109,
        "#10106F（还是别说她什么了吧……）\x02",
    )

    CloseMessageWindow()

    label("loc_8076")

    Jump("loc_85F0")

    label("loc_807B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_85F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84A7")

    #C0290
    ChrTalk(
        0x9,
        (
            "#01900F呵呵，话说回来，\x01",
            "特别任务支援科总算\x01",
            "重新恢复工作了啊～\x02\x03",

            "#01909F身为各位的联络员，\x01",
            "我也非常\x01",
            "感动哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，看到芙兰，\x01",
            "我们也更有回到\x01",
            "支援科的感觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，是啊，\x01",
            "又能和芙兰小姐\x01",
            "一起工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "#01909F嗯嗯，\x01",
            "真是充满干劲啊～\x02\x03",

            "#01906F在各位休息的这段时间，\x01",
            "市民们的委托仍旧接连不断，\x01",
            "处理起来非常辛苦……\x02\x03",

            "#01902F所以真是发自内心地\x01",
            "期盼支援科恢复工作啊～\x02\x03",

            "#01909F……而且，总算可以和姐姐\x01",
            "一起工作了～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0294
    ChrTalk(
        0x101,
        "#00009F哈哈……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x109,
        (
            "#10106F真是的，芙兰……\x01",
            "我都说过多少次了，\x01",
            "在工作时间不要叫我姐姐。\x02\x03",

            "#10101F记住了吗？\x01",
            "既然在同一个地方工作，哪怕是亲姐妹，\x01",
            "也一定要遵守最基本的礼节。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0296
    ChrTalk(
        0x9,
        (
            "#01906F呜……对不起～\x02\x03",

            "#01908F可、可是，我都已经习惯了……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        "#10103F这不是习惯不习惯的问题。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x105,
        "#10302F哈哈，真是个严厉的姐姐啊。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x9,
        (
            "#01906F总、总之～\x02\x03",

            "#01900F接下来，只要等到\x01",
            "缇欧和兰迪先生归队，\x01",
            "大家就算是所向无敌了。\x02\x03",

            "#01902F呵呵，衷心期待\x01",
            "大家全员集结～\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#00004F嗯，我也是同样心情哦。\x02\x03",

            "#00002F那么……\x01",
            "今后请继续关照了，芙兰。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x9,
        "#01909F是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 1)
    Jump("loc_85F0")

    label("loc_84A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8575")

    #C0302
    ChrTalk(
        0x9,
        (
            "#01902F呵呵，又能和大家一起工作了，\x01",
            "真是充满干劲啊～\x02\x03",

            "#01909F更何况还能和姐……咳咳，\x01",
            "还能和诺艾尔小姐一起工作！\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x109,
        "#10106F（真是的，这孩子……）\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#00012F（哈哈，算啦算啦……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_85F0")

    label("loc_8575")


    #C0305
    ChrTalk(
        0x9,
        (
            "#01900F支援科重新恢复工作，\x01",
            "今后应该会接到\x01",
            "很多委托。\x02\x03",

            "#01909F和从前一样，我会继续\x01",
            "担当各位的联络员，用心协助大家～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85F0")

    TalkEnd(0x9)
    Return()

    # Function_18_6BC7 end

    def Function_19_85F4(): pass

    label("Function_19_85F4")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2550, 0, 12860, 0)
    SetChrPos(0x102, 3690, 0, 12840, 0)
    SetChrPos(0x109, 1950, 0, 11360, 0)
    SetChrPos(0x105, 3360, 0, 11340, 0)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0306
    ChrTalk(
        0x9,
        (
            "#01900F啊，来得正好～！\x02\x03",

            "#01901F其实我……有很重要的事情，\x01",
            "要和姐……要和诺艾尔小姐说～\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x109,
        (
            "#12P#10105F芙兰，怎、怎么了？\x01",
            "一脸严肃的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x9,
        (
            "#01908F那个…………………………………\x02\x03",

            "#01906F……在工作的时候，\x01",
            "无论如何也不可以叫你『姐姐』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0309
    ChrTalk(
        0x101,
        "#00006F#12P呼……\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        (
            "#12P#10106F我、我还以为是什么要紧事呢……\x02\x03",

            "#10101F……咳咳。\x01",
            "在决定外派我到支援科的时候，\x01",
            "不就已经和你说过很多次了吗。\x02\x03",

            "#10103F既然你我现在是同事，\x01",
            "最基本的礼节还是要遵守的。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        (
            "#01905F可、可是，姐……\x01",
            "不、不对！诺艾尔小姐……\x02\x03",

            "#01906F啊啊！果然还是不行～！\x01",
            "根本就不可能习惯嘛～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_8975():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8975)
    Sleep(50)

    def lambda_8985():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8985)
    Sleep(300)

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#00012F诺艾尔，算、算啦……\x01",
            "也没必要一丝不苟\x01",
            "到这种程度吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        (
            "#00104F呵呵，是啊。\x01",
            "芙兰小姐用『诺艾尔小姐』这种称呼，\x01",
            "显得过于见外……\x02\x03",

            "#00100F而且，在紧急联络时如果使用不习惯的称呼，\x01",
            "反而有可能影响效率呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x109,
        "#12P#10106F虽、虽然也有一定道理……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0315
    ChrTalk(
        0x9,
        (
            "#01902F对、对吧～！\x01",
            "大家也都这么说！\x02\x03",

            "#01909F那以后叫『姐姐』就可以了吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#12P#10304F好啦，处事稍微灵活些，\x01",
            "才更符合\x01",
            "支援科的特色吧？\x02\x03",

            "#10302F毕竟连科长都是\x01",
            "那种不拘小节的作风。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0317
    ChrTalk(
        0x101,
        "#5P#00006F（这倒真是无法反驳呢……）\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#12P#10106F……呼，没办法啦，\x01",
            "既然大家都这么说……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x9,
        (
            "#01909F太好啦～！那就这么定了！\x02\x03",

            "#01900F嘿嘿嘿，\x01",
            "真是太感谢大家啦～！\x02\x03",

            "#01904F咳咳，那么……\x02\x01",

            "#01909F姐姐，今后请多指教啦⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0320
    ChrTalk(
        0x109,
        (
            "#12P#10101F不、不过呢！芙兰，\x01",
            "我再强调一次，至少不能公私不分……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x9,
        "#01909F我都明白的啦，姐姐⊥\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x109,
        "#12P#10106F（她、她绝对没明白……）\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#00012F（哈哈，诺艾尔也拿芙兰没办法呢。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x13F, 0)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_85F4 end

    def Function_20_8D8D(): pass

    label("Function_20_8D8D")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2400, 0, 12670, 0)
    SetChrPos(0x102, 3550, 0, 12670, 0)
    SetChrPos(0x103, 1360, 0, 12490, 0)
    SetChrPos(0x104, 1860, 0, 11200, 0)
    SetChrPos(0x109, 3040, 0, 11190, 0)
    SetChrPos(0x105, 4090, 0, 11380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0324
    ChrTalk(
        0x9,
        (
            "#01900F啊，缇欧～！\x01",
            "你总算回来了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x103,
        (
            "#12P#00202F嗯，多谢挂怀。\x02\x03",

            "#00204F芙兰小姐，\x01",
            "今后也请继续关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x9,
        (
            "#01909F呵呵，彼此彼此～\x02\x03",

            "#01900F如此一来，\x01",
            "特别任务支援科的全体成员\x01",
            "终于都凑齐了呢～！\x02\x03",

            "期待大家更进一步的活跃表现～！\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#12P#00002F哈哈，谢谢啦，芙兰。\x01",
            "我们一定会拼命努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0328
    ChrTalk(
        0x9,
        (
            "#01905F啊，对了……\x01",
            "要正式道个谢才行！\x02\x03",

            "#01900F姐姐在找尤莉亚准校要签名时，\x01",
            "连我的份也一起要来了呢～！\x02\x03",

            "#01909F真是太谢谢啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x109,
        (
            "#12P#10102F啊哈哈，没什么，不必在意啦。\x02\x03",

            "#10106F毕竟只有我有机会面对面和准校谈话，\x01",
            "总觉得有点对不住芙兰……\x02\x03",

            "#10100F等下次有空时给你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x9,
        "#01909F嗯！好期待啊～！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，想起来了，是艾莉和诺艾尔\x01",
            "昨天在埃尔赛尤号上要来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        (
            "#00100F嗯，公主殿下和尤莉亚准校\x01",
            "都是心胸宽广的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        (
            "#12P#00302F哈哈，小芙兰果然也是\x01",
            "尤莉亚准校的崇拜者啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x9,
        (
            "#01904F那当然！\x02\x03",

            "#01900F尤莉亚准校仪表堂堂，\x01",
            "真是太有气质了……\x01",
            "我好崇拜她啊～\x02\x03",

            "#01909F嘿嘿，不过当然还是\x01",
            "姐姐更加帅气⊥\x02",
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

    #C0335
    ChrTalk(
        0x109,
        (
            "#12P#10111F这这……等一下……！\x02\x03",

            "#10106F芙兰真是的！\x01",
            "怎么说出对尤莉亚准校这么失礼的话……！\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，在芙兰小姐的眼里，\x01",
            "不管与谁相比，\x01",
            "诺艾尔小姐也永远都是最棒的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        "#12P#00012F嗯～确实如此……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x148, 5)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_8D8D end

    def Function_21_93A0(): pass

    label("Function_21_93A0")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2400, 0, 12670, 0)
    SetChrPos(0x102, 3550, 0, 12670, 0)
    SetChrPos(0x103, 1360, 0, 12490, 0)
    SetChrPos(0x104, 1860, 0, 11200, 0)
    SetChrPos(0x109, 3040, 0, 11190, 0)
    SetChrPos(0x105, 4090, 0, 11380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0338
    ChrTalk(
        0x9,
        (
            "#01905F啊，各位……\x02\x03",

            "#01900F正如之前联络时所说，\x01",
            "导力艇已经停靠在了\x01",
            "港湾区的码头～\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        "#12P#00000F嗯，谢谢啦，芙兰。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        "#12P#00100F我们马上就过去。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0341
    ChrTalk(
        0x9,
        (
            "#01903F听说大家要去湿地一带\x01",
            "搜寻下落不明的游击士……\x02\x03",

            "#01908F那个……没问题吗……？\x01",
            "连两位级别高达准Ａ级的游击士\x01",
            "都在那个地方失去了联络……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#12P#00200F芙兰小姐……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        "#12P#00303F抱歉，让你担心了……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x9,
        (
            "#01906F唉，在这种时候，\x01",
            "要是我也能发挥作用就好了……\x02\x03",

            "#01900F那个……要是愿意的话，\x01",
            "可以带着邦邦一起去，当作护身符。\x02",
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

    #C0345
    ChrTalk(
        0x101,
        "#12P#00005F邦邦？好像是那个……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x109,
        (
            "#12P#10106F嗯……\x01",
            "是那个小熊玩偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x9,
        (
            "#01909F只要把它抱在怀里，心情马上就会平静下来～！\x02\x03",

            "#01900F在没有别人在的时候，\x01",
            "姐姐偶尔也会抱它吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0348
    ChrTalk(
        0x109,
        (
            "#12P#10111F等、等一下……！\x01",
            "我、我才没有……！\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x9,
        (
            "#01901F让邦邦去那么危险的地方，\x01",
            "我实在是万分不舍，\x01",
            "但为了保佑大家……！\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        (
            "#12P#00012F这、这个，还是不要了……\x01",
            "你先冷静一下吧。\x02\x03",

            "#00002F总之，好意就心领了。\x01",
            "虽然我们之前有一些不安，\x01",
            "但多亏你，好像已经可以放松下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，这正是芙兰的真正价值呢。\x02\x03",

            "#10309F而且还了解到了诺艾尔不为人知的一面。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x109,
        (
            "#12P#10106F（呜呜，芙兰你给我记着，\x01",
            "  以后再找你算帐……）\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x9,
        (
            "#01909F啊哈哈，那就再好不过啦～\x02\x03",

            "#01900F各位，一路小心哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        "#00000F嗯！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x17B, 7)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_93A0 end

    def Function_22_9A21(): pass

    label("Function_22_9A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A3F")
    Call(0, 47)
    Return()

    label("loc_9A3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9A50")
    Jump("loc_A393")

    label("loc_9A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9A5E")
    Jump("loc_A393")

    label("loc_9A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9ADF")

    #C0355
    ChrTalk(
        0xFE,
        (
            "我们会倾尽克洛斯贝尔的\x01",
            "全部战力，无论如何\x01",
            "也要驱逐赤色星座的势力。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "你们也要尽全力做好\x01",
            "自己所能做到的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A393")

    label("loc_9ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9AED")
    Jump("loc_A393")

    label("loc_9AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9AFB")
    Jump("loc_A393")

    label("loc_9AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E54")

    #C0357
    ChrTalk(
        0xFE,
        "呼，好累啊……\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#00005F（艾玛警官拿的那个瓶子，\x01",
            "  是营养剂吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x103,
        (
            "#00200F（好像是呢……\x01",
            "  她大概非常疲劳吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，是『运动汽水Ｘ』——\x02\x03",

            "竟然在喝效力这么强劲\x01",
            "的饮料啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0361
    ChrTalk(
        0x109,
        "#10105F瓦、瓦吉——\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0362
    ChrTalk(
        0xFE,
        (
            "我、我刚工作了一个通宵，\x01",
            "这也是没办法的事吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "你有什么意见吗？\x01",
            "我喝些营养饮料\x01",
            "有那么奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "请回答——\x01",
            "罗伊德·班宁斯搜查官！\x02",
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
    Sleep(1000)

    #C0365
    ChrTalk(
        0x101,
        "#00006F不不，我并不觉得有什么……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "哼、哼……\x01",
            "那就是没问题啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "你们几个在这种地方偷懒，\x01",
            "不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "那个……在这种时候，\x01",
            "应该努力去完成更多的支援请求才对吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#00006F呼……是。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x105,
        "#10302F（呵呵，真是不幸啊。）\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        "#00001F（……都怪你。）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x171, 6)
    Jump("loc_9EBA")

    label("loc_9E54")


    #C0372
    ChrTalk(
        0xFE,
        (
            "不管怎么说，在如今这种时候，\x01",
            "应该认真处理支援请求，\x01",
            "绝不可偷懒懈怠。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        "——我要说的就这么多。\x02",
    )

    CloseMessageWindow()

    label("loc_9EBA")

    Jump("loc_A393")

    label("loc_9EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9ECD")
    Jump("loc_A393")

    label("loc_9ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9EDB")
    Jump("loc_A393")

    label("loc_9EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A08E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F03")
    Call(0, 30)
    Jump("loc_9F95")

    label("loc_9F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F15")
    Call(0, 31)
    Jump("loc_9F95")

    label("loc_9F15")


    #C0374
    ChrTalk(
        0xFE,
        (
            "达德利长官期待支援科\x01",
            "以机动队伍的形式\x01",
            "发挥作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "只要仔细思考其中的含义，\x01",
            "你们就能明白自己该做的事情……\x01",
            "拜托大家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F95")

    Jump("loc_A089")

    label("loc_9F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A028")

    #C0376
    ChrTalk(
        0xFE,
        (
            "雷克特·亚兰德尔和\x01",
            "雾香·楼兰就由\x01",
            "搜查一科继续监视。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "虽然目前还无法判断\x01",
            "两大国究竟有何企图……\x01",
            "但也只能耐心调查。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A089")

    label("loc_A028")


    #C0378
    ChrTalk(
        0xFE,
        (
            "雷克特·亚兰德尔和\x01",
            "雾香·楼兰就交给\x01",
            "搜查一科来负责吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "你们只要处理好\x01",
            "自己的业务即可。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A089")

    Jump("loc_A393")

    label("loc_A08E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A37C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2F4")

    #C0380
    ChrTalk(
        0xFE,
        (
            "班宁斯搜查官……\x01",
            "支援请求方面的工作进展得顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#00000F哎，这个……总之，\x01",
            "就是在按照平时的步调工作啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        "……是吗。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "顺便一说，达德利长官\x01",
            "已经前往兰花塔，去对正式会议时的\x01",
            "警备体制进行最终确认了。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "而赛尔盖科长预计今天全天都在\x01",
            "二层的对策总部负责各个方面的协调工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……你们几个也要认真对待工作，\x01",
            "不能有丝毫松懈。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "只有如此，\x01",
            "才不用尴尬地说什么平时的步调。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        "#00001F是、是的，明白了。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，还是老样子，\x01",
            "  真是个严厉的姐姐啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x104,
        (
            "#00303F（嗯～如果不说话，\x01",
            "  倒也十足是个美人呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x109,
        (
            "#10106F（兰迪前辈，\x01",
            "  重点并不是那种问题吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 0)
    Jump("loc_A377")

    label("loc_A2F4")


    #C0391
    ChrTalk(
        0xFE,
        (
            "达德利长官和赛尔盖科长\x01",
            "为了顺利完成任务，\x01",
            "都在最大限度地发挥自己的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "……你们几个也要认真对待工作，\x01",
            "不能有丝毫松懈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A377")

    Jump("loc_A393")

    label("loc_A37C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A38A")
    Jump("loc_A393")

    label("loc_A38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A393")

    label("loc_A393")

    TalkEnd(0xFE)
    Return()

    # Function_22_9A21 end

    def Function_23_A397(): pass

    label("Function_23_A397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3B6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3B6")
    Call(0, 52)
    Return()

    label("loc_A3B6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_23_A397 end

    def Function_24_A3BD(): pass

    label("Function_24_A3BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A3CE")
    Jump("loc_AA76")

    label("loc_A3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A3DC")
    Jump("loc_AA76")

    label("loc_A3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A49E")

    #C0393
    ChrTalk(
        0xFE,
        (
            "真是的，事情似乎\x01",
            "变得很棘手了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "总之，二科暂且将\x01",
            "其它所有案件放下，\x01",
            "全力协助一科的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "现在正在排查\x01",
            "潜入克洛斯贝尔的谍报员……\x01",
            "特别是帝国的谍报员。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A51E")

    label("loc_A49E")


    #C0396
    ChrTalk(
        0xFE,
        (
            "总之，二科暂且将\x01",
            "其它所有案件放下，\x01",
            "全力协助一科的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "现在正在排查\x01",
            "潜入克洛斯贝尔的谍报员……\x01",
            "特别是帝国的谍报员。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A51E")

    Jump("loc_AA76")

    label("loc_A523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A629")

    #C0398
    ChrTalk(
        0xFE,
        "『真知』吗……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "首先还是准备采取常规手段，\x01",
            "从鲁巴彻的渠道\x01",
            "开始再次检查……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "但我总觉得，\x01",
            "从那边流出的可能性很低呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "算了，在目前阶段，\x01",
            "想太多也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "现在能做的，也只有耐下心来，\x01",
            "一一调查所有能想到的渠道了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A693")

    label("loc_A629")


    #C0403
    ChrTalk(
        0xFE,
        (
            "算了，在目前阶段，\x01",
            "想太多也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "现在能做的，也只有耐下心来，\x01",
            "一一调查所有能想到的渠道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A693")

    Jump("loc_AA76")

    label("loc_A698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A6A6")
    Jump("loc_AA76")

    label("loc_A6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A7DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A748")

    #C0405
    ChrTalk(
        0xFE,
        (
            "支援科的协助自不必说，\x01",
            "雷蒙德那家伙\x01",
            "昨天好像也很拼命呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "追捕假货商竟然会遭遇到恐怖分子的残党，\x01",
            "真是让人难以置信啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7DA")

    label("loc_A748")


    #C0407
    ChrTalk(
        0xFE,
        (
            "黑月的暗中行动暂且不提，\x01",
            "雷蒙德那家伙\x01",
            "昨天独自一人，好像很拼命呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "追捕假货商竟然会遭遇到恐怖分子的残党，\x01",
            "真是让人难以置信啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7DA")

    Jump("loc_AA76")

    label("loc_A7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7FA")
    Call(0, 25)
    Jump("loc_A86F")

    label("loc_A7FA")


    #C0409
    ChrTalk(
        0xFE,
        (
            "原本由一科负责的工作，\x01",
            "也分出了几件\x01",
            "交给二科来处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "毕竟目前的状况比较特殊，\x01",
            "简直就是全体总动员的体制啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A86F")

    Jump("loc_AA76")

    label("loc_A874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A882")
    Jump("loc_AA76")

    label("loc_A882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A890")
    Jump("loc_AA76")

    label("loc_A890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A89E")
    Jump("loc_AA76")

    label("loc_A89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8B9")
    Call(0, 26)
    Jump("loc_A8FD")

    label("loc_A8B9")


    #C0411
    ChrTalk(
        0xA,
        (
            "疯狂飙车的年轻人吗……\x01",
            "真是的，给别人找麻烦\x01",
            "难道就这么有趣吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8FD")

    Jump("loc_AA76")

    label("loc_A902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_AA76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A91D")
    Call(0, 27)
    Jump("loc_AA76")

    label("loc_A91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA18")

    #C0412
    ChrTalk(
        0xFE,
        (
            "算了，不说这些了。\x01",
            "如果今后遇到什么事情，\x01",
            "还请多多帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "我们搜查二科也是\x01",
            "非常期待各位的。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        (
            "#00002F是、是的。\x02\x03",

            "（不知为何，听到这样的话\x01",
            "  就会打心底里高兴呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x102,
        (
            "#00102F（嗯，感觉我们已经\x01",
            "  得到大家很大的认同。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AA76")

    label("loc_AA18")


    #C0416
    ChrTalk(
        0xFE,
        (
            "好啦，如果今后遇到什么事情，\x01",
            "还请各位多多帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "我们搜查二科也是\x01",
            "非常期待各位的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA76")

    TalkEnd(0xFE)
    Return()

    # Function_24_A3BD end

    def Function_25_AA7A(): pass

    label("Function_25_AA7A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    #C0418
    ChrTalk(
        0xA,
        "哟，这不是特别任务支援科的各位吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0419
    ChrTalk(
        0xC,
        (
            "#00603F我还以为是谁，原来是你们啊。\x02\x03",

            "#00600F听说你们接受了\x01",
            "调查那个什么『幻兽』的任务？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        "#00000F嗯，是的……\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x105,
        "#10300F呵呵，消息果然灵通啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x105, 500)

    #C0422
    ChrTalk(
        0xC,
        (
            "#00603F哼，因为那是警备队的正式委托，\x01",
            "我自然会得知情报……\x02\x03",

            "#00600F根据现有情报来看，对手似乎\x01",
            "无法以常理度之。\x02\x03",

            "在与它们交战时，\x01",
            "一定要拿出十足干劲。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#00100F感谢您的忠告。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x101,
        (
            "#00005F话说回来……\x01",
            "反间谍方面的工作\x01",
            "似乎也相当繁忙吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0425
    ChrTalk(
        0xA,
        (
            "当然，毕竟独立提案\x01",
            "获得了热烈的响应。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xA,
        (
            "为了探查克洛斯贝尔的动向，\x01",
            "来自大陆各国的谍报员\x01",
            "接二连三地潜入克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xA,
        (
            "谍报人员的数量极其惊人，\x01",
            "光是掌握其具体数字，\x01",
            "就足以忙得不可开交了。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x109,
        "#10105F竟、竟然有那么夸张吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    #C0429
    ChrTalk(
        0xC,
        (
            "#00601F……再加上还要密切注意\x01",
            "『赤色星座』和『黑月』的动向。\x02\x03",

            "当然，\x01",
            "除此之外，对其它的犯罪行为\x01",
            "也不能置之不管。\x02\x03",

            "#00603F应该即时处理的案子\x01",
            "还有很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "就是因为这样，\x01",
            "现在打算由二科来接手一些\x01",
            "本来由一科负责的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xA,
        (
            "我们就是在\x01",
            "商量这件事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x103,
        (
            "#00200F原来如此……\x01",
            "正在谈这些啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x104,
        (
            "#00300F该怎么说呢，\x01",
            "情况好像真的很严峻啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x104, 500)

    #C0434
    ChrTalk(
        0xC,
        (
            "#00603F哼，无论面对\x01",
            "怎样的险恶状况，\x01",
            "我们也会做好自己该做的事情。\x02\x03",

            "#00601F总之，你们几个也要\x01",
            "尽力完成自己的任务。\x02\x03",

            "『幻兽』的问题\x01",
            "恐怕也不容久置。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#00001F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    SetScenarioFlags(0x16A, 2)
    Return()

    # Function_25_AA7A end

    def Function_26_AF6C(): pass

    label("Function_26_AF6C")

    OP_4B(0xA, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0436
    ChrTalk(
        0xA,
        (
            "说起来，\x01",
            "那些飙车族的年轻人……\x01",
            "昨天是被你们抓住的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x14,
        "嗯，情节严重，实在是不能放任不理啊。\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x14,
        (
            "由于只是处以罚款而已，\x01",
            "他们似乎并没有吸取教训。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x14,
        (
            "不过，至少今天没有在市内\x01",
            "看到他们。这样一想，\x01",
            "似乎也算是有些效果的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xA,
        "呼，但愿如此吧。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xA,
        (
            "可恶，如果他们不是外国人，\x01",
            "就可以拘留起来，\x01",
            "狠狠训斥一顿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xA,
        (
            "唉，关于这种问题，\x01",
            "也只能期待法律今后能完善一些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x14,
        (
            "说得也是，算啦，\x01",
            "我们只要踏实做好\x01",
            "自己能做的事情就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_B1AB")

    #C0444
    ChrTalk(
        0x101,
        (
            "#00001F（看样子，\x01",
            "  似乎正在谈论那个三人组呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x102,
        (
            "#00103F（是啊，真希望他们\x01",
            "  不要再次危险驾驶了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1E3")

    label("loc_B1AB")


    #C0446
    ChrTalk(
        0x101,
        (
            "#00001F（昨天么……\x01",
            "  难道市内发生了什么事情吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1E3")

    SetScenarioFlags(0x13E, 7)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_26_AF6C end

    def Function_27_B1F9(): pass

    label("Function_27_B1F9")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 500)

    #C0447
    ChrTalk(
        0xA,
        (
            "哦？好像还混杂着一些\x01",
            "新面孔啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xA,
        (
            "莫非就是传闻中的\x01",
            "特别任务支援科新成员吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        "#00000F嗯，正是。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    #C0450
    ChrTalk(
        0xB,
        (
            "那也就是说……\x01",
            "你就是警备队的诺艾尔小姐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xB,
        (
            "嘿嘿嘿，要是有空的话，\x01",
            "下次一起去喝个茶如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x109,
        "#10106F哎，这、这个……\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x105,
        "#10302F呵呵，看来是被拒绝了呢。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xB,
        "哎……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 500)

    #C0455
    ChrTalk(
        0xB,
        (
            "嗯，如此说来，\x01",
            "你就是圣书会的瓦吉·赫米斯菲亚了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xB,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xB,
        (
            "……该怎么说才好呢，离近一看，\x01",
            "长得还真是相当漂亮呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，是吗？\x02\x03",

            "#10304F但遗憾得很，\x01",
            "你并不是我喜欢的类型哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xB,
        "是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xB,
        (
            "……不对！我为什么要\x01",
            "因为被同性拒绝而消沉啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)
    TurnDirection(0xA, 0xB, 500)

    #C0461
    ChrTalk(
        0xA,
        (
            "……真是的，我不出声，\x01",
            "你们就一直在谈论这种无聊的话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xA,
        (
            "你小子也是，好好学学支援科的人，\x01",
            "有点长进吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xA,
        (
            "要不然，我把你扔回警察学校，\x01",
            "让你重新再学习一遍如何啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0464
    ChrTalk(
        0xB,
        (
            "警督～不要啊！\x01",
            "还是饶了我吧～\x02",
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
    OP_93(0xA, 0xE1, 0x0)
    OP_93(0xB, 0x2D, 0x0)
    SetScenarioFlags(0x13F, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_27_B1F9 end

    def Function_28_B608(): pass

    label("Function_28_B608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B7C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B75D")

    #C0465
    ChrTalk(
        0xFE,
        (
            "嘿，听我说哦～\x01",
            "多诺邦警督\x01",
            "很快就要回警察局了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xFE,
        (
            "为了填补警督不在而出现的空缺，\x01",
            "这段时间真是很辛苦，\x01",
            "这么一来，终于可以解放了～\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        "#00002F哈哈，太好了呢～\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        (
            "#00200F要是这些话被警督听到了，\x01",
            "应该会被臭骂一顿吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0469
    ChrTalk(
        0xFE,
        (
            "呃，这、这个……说得倒也是。\x01",
            "……请一定要帮我保密啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B7BB")

    label("loc_B75D")


    #C0470
    ChrTalk(
        0xFE,
        (
            "等到警督回来以后，\x01",
            "搜查二科也就可以安心了～\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xFE,
        (
            "好～在那之前，\x01",
            "我们也得好好努力才行～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7BB")

    Jump("loc_BE2D")

    label("loc_B7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B7CE")
    Jump("loc_BE2D")

    label("loc_B7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B85E")

    #C0472
    ChrTalk(
        0xFE,
        (
            "事先毫无联络，\x01",
            "突然就过来，\x01",
            "要把我们编入国防军……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        (
            "虽然不能公然表示不满，\x01",
            "但这真是太过蛮横了～\x01",
            "……呼，这到底是怎么了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE2D")

    label("loc_B85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B86C")
    Jump("loc_BE2D")

    label("loc_B86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B92B")

    #C0474
    ChrTalk(
        0xFE,
        (
            "帝国已经发表了正式声明，\x01",
            "否认自己与犯罪行为有任何关联……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xFE,
        (
            "我正在摸索能不能想办法\x01",
            "在暗中和猎兵们交涉一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        (
            "既然做出了这种过分行径，\x01",
            "毫无疑问，自然是有着某种企图。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE2D")

    label("loc_B92B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9AB")

    #C0477
    ChrTalk(
        0xFE,
        (
            "瓦鲁多·瓦雷斯是从\x01",
            "什么地方得到『真知』的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        (
            "如果不是通过鲁巴彻的渠道取得的，\x01",
            "那又会是哪里的渠道呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE2D")

    label("loc_B9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B9B9")
    Jump("loc_BE2D")

    label("loc_B9B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BC0F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BB89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB50")

    #C0479
    ChrTalk(
        0xFE,
        (
            "啊，是你们啊～\x01",
            "昨天可真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        (
            "对了对了，昨天晚上，\x01",
            "我做梦都梦到那个老婆婆了呢～\x01",
            "不知道为什么，在梦里反而是被她追。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "呼，拜其所赐，\x01",
            "我一晚上都没睡好啊。\x02",
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

    #C0482
    ChrTalk(
        0x101,
        (
            "#00006F（听他这么一说，\x01",
            "  总觉得自己今晚也会做那种梦了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x102,
        "#00106F（……努力忘记吧。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BB84")

    label("loc_BB50")


    #C0484
    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "昨天真是太感谢了。\x01",
            "你们真是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB84")

    Jump("loc_BC0A")

    label("loc_BB89")


    #C0485
    ChrTalk(
        0xFE,
        (
            "呼，我昨天做了个\x01",
            "超级讨厌的梦呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "竟然被昨天拘捕的老婆婆\x01",
            "反过来追赶……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        (
            "呜哇哇，只要稍微一回想，\x01",
            "就忍不住冒冷汗～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC0A")

    Jump("loc_BE2D")

    label("loc_BC0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BC1D")
    Jump("loc_BE2D")

    label("loc_BC1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BC2B")
    Jump("loc_BE2D")

    label("loc_BC2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BC39")
    Jump("loc_BE2D")

    label("loc_BC39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BC47")
    Jump("loc_BE2D")

    label("loc_BC47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BDAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD19")

    #C0488
    ChrTalk(
        0xFE,
        (
            "呼，在这种时期，\x01",
            "总部内的气氛也相当紧张啊。\x01",
            "真是受不了～\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        (
            "虽然来自议员与上级的压力\x01",
            "有所减轻，\x01",
            "但自治州自身的问题却仍然堆积如山。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "呼，究竟要到什么时候\x01",
            "才能稍微轻松些呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BDA6")

    label("loc_BD19")


    #C0491
    ChrTalk(
        0xFE,
        (
            "算啦，现在也只能把迪塔市长的\x01",
            "政治改革当作心灵支柱，\x01",
            "继续努力啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "另外，要是议会那边能把我们的工资\x01",
            "调高一些就更好了……开个玩笑啦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDA6")

    Jump("loc_BE2D")

    label("loc_BDAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BE2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDC6")
    Call(0, 27)
    Jump("loc_BE2D")

    label("loc_BDC6")


    #C0493
    ChrTalk(
        0xFE,
        (
            "呼，又被警督戳到了\x01",
            "我的痛处啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "其实我也一直想\x01",
            "稍微稳重一些……\x01",
            "但性格这种东西是无法改变的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE2D")

    TalkEnd(0xFE)
    Return()

    # Function_28_B608 end

    def Function_29_BE31(): pass

    label("Function_29_BE31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BE42")
    Jump("loc_C35E")

    label("loc_BE42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE50")
    Jump("loc_C35E")

    label("loc_BE50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFC9")

    #C0495
    ChrTalk(
        0xC,
        (
            "#00600F是你们啊。\x02\x03",

            "#00603F……奥兰多的事情我已经听说了。\x01",
            "情况似乎\x01",
            "相当棘手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        "#00001F嗯，但我们一定会把他带回来。\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xC,
        (
            "#00603F哼，是吗。\x01",
            "既然如此，我也就不必再说什么了。\x02\x03",

            "#00600F总之，如今的状况就是这样。\x01",
            "需要派给你们的工作\x01",
            "自然也是堆积如山。\x02\x03",

            "所以说，\x01",
            "有关同伴的问题，\x01",
            "你们要尽快解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x102,
        "#00100F达德利警官……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        "#00001F是！那当然！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 3)
    Jump("loc_C04C")

    label("loc_BFC9")


    #C0500
    ChrTalk(
        0xC,
        (
            "#00603F这里的商讨结束之后，\x01",
            "我准备前往市长那里，\x01",
            "讨论下一步的对策。\x02\x03",

            "#00600F你们尽快处理完自己该做的事情，\x01",
            "然后就赶快过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C04C")

    Jump("loc_C35E")

    label("loc_C051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C05F")
    Jump("loc_C35E")

    label("loc_C05F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C06D")
    Jump("loc_C35E")

    label("loc_C06D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C07B")
    Jump("loc_C35E")

    label("loc_C07B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C10C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C096")
    Call(0, 25)
    Jump("loc_C107")

    label("loc_C096")


    #C0501
    ChrTalk(
        0xC,
        (
            "#00600F虽然一科的案件堆积如山，\x01",
            "但反间谍的工作还是交给我们处理吧。\x02\x03",

            "你们只需专心完成\x01",
            "自己负责的任务就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C107")

    Jump("loc_C35E")

    label("loc_C10C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C11A")
    Jump("loc_C35E")

    label("loc_C11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C142")
    Call(0, 30)
    Jump("loc_C1BA")

    label("loc_C142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C154")
    Call(0, 31)
    Jump("loc_C1BA")

    label("loc_C154")


    #C0502
    ChrTalk(
        0xC,
        (
            "#00603F我暂时留在这里，\x01",
            "检查一下各方面的情报。\x02\x03",

            "#00600F如果有什么事情，\x01",
            "随时都可以直接和我联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1BA")

    Jump("loc_C334")

    label("loc_C1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2CB")

    #C0503
    ChrTalk(
        0xFE,
        (
            "#00603F帝国军情报局，\x01",
            "还有共和国的洛克史密斯机关……\x01",
            "二者均是不容忽视的对手。\x02\x03",

            "如果这两方势力有所接触……\x01",
            "那便毫无疑问，必然会在\x01",
            "暗中有所行动。\x02\x03",

            "#00600F总之，身为警察，\x01",
            "目前也只能做好自己力所能及的事情。\x02\x03",

            "如果发现了什么新情况，\x01",
            "就和一科联络吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C334")

    label("loc_C2CB")


    #C0504
    ChrTalk(
        0xFE,
        (
            "#00600F总之，身为警察，\x01",
            "目前也只能做好自己力所能及的事情。\x02\x03",

            "如果发现了什么新情况，\x01",
            "就和一科联络吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C334")

    Jump("loc_C35E")

    label("loc_C339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C347")
    Jump("loc_C35E")

    label("loc_C347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C355")
    Jump("loc_C35E")

    label("loc_C355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C35E")

    label("loc_C35E")

    TalkEnd(0xFE)
    Return()

    # Function_29_BE31 end

    def Function_30_C362(): pass

    label("Function_30_C362")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0x0)
    OP_4B(0xD, 0x0)
    OP_68(-59230, 1730, 14590, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23690, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -59000, 30, 14800, 45)
    SetChrPos(0x102, -58970, 30, 16280, 90)
    SetChrPos(0x104, -57950, 0, 14250, 0)
    SetChrPos(0x109, -59810, 30, 14920, 45)
    SetChrPos(0x105, -59060, 0, 13870, 45)
    OP_93(0xC, 0xE1, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_0D()
    Sleep(500)

    #C0505
    ChrTalk(
        0xC,
        "#00600F#2P是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xD,
        "#5P……有什么事情吗？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#00001F#6P嗯……有件事情\x01",
            "必须要向搜查一科报告。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0508
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将雾香和雷克特出现在市内\x01",
            "的情况进行了报告。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0509
    ChrTalk(
        0xC,
        (
            "#00603F#2P……原来如此。\x02\x03",

            "帝国军情报部与共和国的洛克史密斯机关，\x01",
            "两个机关中的重要人物同时出现在市内……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xD,
        "#5P达德利长官，这……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x101,
        (
            "#00001F#6P……您如何看待这种情况？\x02\x03",

            "在会议正式召开的前一天，\x01",
            "两大国的谍报人员同时出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x102,
        "#00108F#6P如果理解为偶然，未免太过巧合……\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x105,
        (
            "#10302F#12P呵呵，但据他们本人的说法，\x01",
            "只是跑腿和出来散心而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x109,
        "#10106F#6P再、再怎么说，也太过可疑了吧。\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        (
            "#00603F#2P嗯，他们自然有着某种目的。\x02\x03",

            "#00600F但如果想推断出具体答案，\x01",
            "我认为曾与他们直接对过话的你们\x01",
            "才更有发言权。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        "#00303F#12P……说得好像没错呢。\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xC,
        (
            "#00600F#2P……反问你一句，班宁斯。\x01",
            "你觉得他们是为了什么目的\x01",
            "而在市内现身的？\x02\x03",

            "#00603F通过与他们的对话，还有他们的行动路线……\x01",
            "应该能在某些地方发现一些迹象。\x02\x03",

            "#00600F即使是推测也无妨，说说看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        "#00001F#6P这、这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0519
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "雾香和雷克特\x01",
            "出现在市内的理由是……？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "为了首脑的警备工作\x01",      # 0
            "散心和购物\x01",              # 1
            "进行密谈\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C895"),
        (1, "loc_C9D3"),
        (2, "loc_CB26"),
        (SWITCH_DEFAULT, "loc_CB69"),
    )


    label("loc_C895")


    #C0520
    ChrTalk(
        0x101,
        (
            "#00001F#6P是为了给首脑做好警备工作吧？\x02\x03",

            "#00003F比如说，为了预防紧急状况，\x01",
            "事先出来熟悉一下\x01",
            "克洛斯贝尔市内的地形……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xC,
        (
            "#00603F#2P……那种可能性应该很低。\x02\x03",

            "#00600F谍报人员并不负责警备工作，\x01",
            "更何况，他们两人在几个月之前\x01",
            "就曾到访过克洛斯贝尔。\x02\x03",

            "如今并无再次熟悉地形\x01",
            "的必要性。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        "#00006F#6P确、确实如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB69")

    label("loc_C9D3")


    #C0523
    ChrTalk(
        0x101,
        (
            "#00001F#6P……或许正如他们自己所说，\x01",
            "只是为了散心和购物而已吧？\x02\x03",

            "#00003F虽然已经临近通商会议，\x01",
            "但也不能断言没有必要……\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xC,
        (
            "#00603F#2P……那种可能性恐怕并不存在。\x02\x03",

            "#00600F从他们那种敷衍的回答方式来看，\x01",
            "那显然只是单纯的伪装而已。\x02\x03",

            "#00606F呼，唉呀呀……\x01",
            "本以为你能说出点像样的看法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#00001F#6P等、等一下。\x01",
            "嗯，既然如此……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB69")

    label("loc_CB26")

    OP_2C(0xA3, 0x1)

    #C0526
    ChrTalk(
        0x101,
        (
            "#00001F#6P……我想，他们两人\x01",
            "有可能是为了进行密谈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB69")

    label("loc_CB69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBC7")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0527
    ChrTalk(
        0x101,
        (
            "#00001F#6P对了，说不定……\x01",
            "他们两人是为了\x01",
            "进行密谈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBC7")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CC41():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CC41)
    Sleep(50)

    def lambda_CC51():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CC51)
    Sleep(50)

    def lambda_CC61():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CC61)
    Sleep(50)

    def lambda_CC71():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CC71)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0528
    ChrTalk(
        0xD,
        "#5P密谈吗……？\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xC,
        "#00600F#2P嗯……你为何这样想？\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x101,
        (
            "#00003F#6P最初目击到这两人的地点\x01",
            "全都在港湾区。\x02\x03",

            "#00001F在我们展开追踪之前，\x01",
            "他们正好在同一区域……\x01",
            "我想这恐怕并非偶然。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x102,
        (
            "#00105F#5P啊……确实如此呢。\x02\x03",

            "#00100F共和国的总统\x01",
            "在昨天就预定到\x01",
            "港湾区的ＩＢＣ视察……\x02\x03",

            "如果想以密谈为目的而会面，\x01",
            "那里或许正是最合适的场所呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x109,
        (
            "#10100F#6P而且港湾区正好在\x01",
            "举办咪西的演出活动，\x01",
            "还可以用来当作掩护。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xD,
        (
            "#5P因此，他们分别以稍微散散心，\x01",
            "还有替总统购物为借口，\x01",
            "进行秘密会面……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xD,
        "#5P……这样就能对上了呢。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x104,
        (
            "#00301F#12P不过，说到密谈，\x01",
            "具体会谈些什么呢？\x02\x03",

            "帝国和共和国之间\x01",
            "不是一直都保持着\x01",
            "对立的关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        (
            "#00108F#5P……并不是很难推测啊。\x02\x03",

            "#00103F由于之前的教团事件，\x01",
            "自治州议会中的大量帝国派议员\x01",
            "与共和国派议员纷纷落马……\x02\x03",

            "再加上新市长与新议长共同建立\x01",
            "起来的协力体制，使克洛斯贝尔\x01",
            "渐渐拥有了一定影响力。\x02\x03",

            "#00101F面对如此状况……帝国和共和国\x01",
            "自然不会坐视不理。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#00005F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x105,
        (
            "#10300F#12P原来如此，在这个问题上，\x01",
            "两大国的利害关系是一致的。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xC,
        (
            "#00608F#2P虽然还不能断言……\x01",
            "但他们应该会在暗中\x01",
            "采取某些行动。\x02\x03",

            "#00603F……目前能说的，大概也就是这些了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D0CA():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D0CA)
    Sleep(50)

    def lambda_D0DA():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D0DA)
    Sleep(50)

    def lambda_D0EA():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D0EA)
    Sleep(50)

    def lambda_D0FA():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D0FA)
    Sleep(50)

    def lambda_D10A():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D10A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0540
    ChrTalk(
        0xD,
        (
            "#5P对雷克特·亚兰德尔\x01",
            "与雾香·楼兰的监视工作\x01",
            "就由搜查一科来继续负责。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xD,
        "#5P你们特意前来报告，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        "#00000F#6P哪里，能发挥作用，是我们的荣幸。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x102,
        (
            "#00108F#6P明天的正式会议……\x01",
            "但愿能顺利结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xC,
        (
            "#00603F#2P为此，我们身为警察，\x01",
            "现在一定要尽力做好自己力所能及的事情。\x02\x03",

            "#00601F如果发现了什么新情况，\x01",
            "就和一科联络吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        "#00000F#6P是，那到时就麻烦您了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_2C(0xA3, 0x1)
    OP_29(0xA3, 0x1, 0xD)
    OP_93(0xC, 0x0, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, -59320, 30, 14570, 45)
    SetScenarioFlags(0x1C7, 4)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_30_C362 end

    def Function_31_D2E7(): pass

    label("Function_31_D2E7")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x101, 0)

    #C0546
    ChrTalk(
        0xD,
        "班宁斯搜查官。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0547
    ChrTalk(
        0xC,
        (
            "#00600F是你们啊……\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        "#00000F不，没什么特别的事情。\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xC,
        (
            "#00603F是吗……不过，\x01",
            "即使如此也不可松懈大意。\x02\x03",

            "我想你们应该也感觉得到，\x01",
            "众多要人的来访，使整个市内\x01",
            "的气氛变得有些喧嚣放松。\x02\x03",

            "#00600F在这种气氛下，\x01",
            "无论多么反常意外的事都是非常\x01",
            "容易发生的。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x109,
        "#10101F确实如此呢……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，我们可要瞪大眼睛，\x01",
            "随时保持警惕才行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#00100F顺便问一句，\x01",
            "达德利警官暂时\x01",
            "还要留在这里吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    #C0553
    ChrTalk(
        0xC,
        (
            "#00603F嗯，在首脑们前往\x01",
            "彩虹剧团观赏舞剧之前，\x01",
            "我会一直留在总部。\x02\x03",

            "#00600F如果有什么情况，\x01",
            "随时都可以直接联络我。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        "#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_31_D2E7 end

    def Function_32_D55C(): pass

    label("Function_32_D55C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D56D")
    Jump("loc_D642")

    label("loc_D56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D59F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D59A")

    #C0555
    ChrTalk(
        0x11,
        "…………嘁…………\x02",
    )

    CloseMessageWindow()

    label("loc_D59A")

    Jump("loc_D642")

    label("loc_D59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D5AD")
    Jump("loc_D642")

    label("loc_D5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D642")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5D4")
    Call(0, 33)
    Jump("loc_D642")

    label("loc_D5D4")

    ClearChrFlags(0x11, 0x10)

    #C0556
    ChrTalk(
        0x11,
        (
            "就算抓到了我们，\x01",
            "也不过就是罚点钱而已，\x01",
            "何必这么拼命嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x11,
        (
            "哼哼，难道警察就这么\x01",
            "想要这点小钱吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D642")

    TalkEnd(0xFE)
    Return()

    # Function_32_D55C end

    def Function_33_D646(): pass

    label("Function_33_D646")


    #C0558
    ChrTalk(
        0xF,
        (
            "接下来……\x01",
            "你们现在住在\x01",
            "什么地方？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x11,
        "哼，我没有回答你的义务。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x11,
        (
            "反正是你这种平民\x01",
            "永远都住不起的地方就是了……\x01",
            "只能告诉你这么多。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xF,
        "（可、可恶……！）\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x101,
        "#00001F（加、加油啊，弗兰茨……）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_33_D646 end

    def Function_34_D722(): pass

    label("Function_34_D722")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D733")
    Jump("loc_D834")

    label("loc_D733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D796")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D791")

    #C0563
    ChrTalk(
        0x12,
        "吊销……吊销驾照吗！？\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x12,
        (
            "而且居然还要一个月……\x01",
            "哇啊啊啊啊啊！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D791")

    Jump("loc_D834")

    label("loc_D796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D7A4")
    Jump("loc_D834")

    label("loc_D7A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D834")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D834")

    #C0565
    ChrTalk(
        0x12,
        (
            "你们几个……\x01",
            "就是摆放障碍物拦截我们的家伙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x12,
        (
            "哼，就会耍这种低级把戏。\x01",
            "要是太过得意忘形，\x01",
            "可不会有什么好下场哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D834")

    TalkEnd(0xFE)
    Return()

    # Function_34_D722 end

    def Function_35_D838(): pass

    label("Function_35_D838")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D849")
    Jump("loc_D91A")

    label("loc_D849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D8C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D8C1")

    #C0567
    ChrTalk(
        0x13,
        (
            "呼，这次似乎真是\x01",
            "做得有点过分了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x13,
        (
            "连导力车都报废了，\x01",
            "看来短时间内还是\x01",
            "安分一些为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8C1")

    Jump("loc_D91A")

    label("loc_D8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D8D4")
    Jump("loc_D91A")

    label("loc_D8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D91A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D91A")

    #C0569
    ChrTalk(
        0x13,
        (
            "啊啊～好想早点回去啊～\x01",
            "审问怎么这么烦人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D91A")

    TalkEnd(0xFE)
    Return()

    # Function_35_D838 end

    def Function_36_D91E(): pass

    label("Function_36_D91E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D97E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D93C")
    Call(0, 38)
    Jump("loc_D979")

    label("loc_D93C")


    #C0570
    ChrTalk(
        0xFE,
        (
            "老实说，现在的感觉还像在做梦一样…\x01",
            "今后到底会怎么样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D979")

    Jump("loc_DC22")

    label("loc_D97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D98C")
    Jump("loc_DC22")

    label("loc_D98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D99A")
    Jump("loc_DC22")

    label("loc_D99A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DA8E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DA89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA34")

    #C0571
    ChrTalk(
        0xE,
        (
            "各位取缔飙车族，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xE,
        (
            "这些孩子就交给\x01",
            "我们来处理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xE,
        (
            "如果以后再有什么事情，\x01",
            "还请各位帮忙哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DA84")

    label("loc_DA34")


    #C0574
    ChrTalk(
        0xE,
        (
            "这些孩子就交给\x01",
            "我们来处理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xE,
        (
            "如果以后再有什么事情，\x01",
            "还请各位帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA84")

    Jump("loc_DA89")

    label("loc_DA89")

    Jump("loc_DC22")

    label("loc_DA8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DA9C")
    Jump("loc_DC22")

    label("loc_DA9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DAAA")
    Jump("loc_DC22")

    label("loc_DAAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DAB8")
    Jump("loc_DC22")

    label("loc_DAB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DAC6")
    Jump("loc_DC22")

    label("loc_DAC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DAD4")
    Jump("loc_DC22")

    label("loc_DAD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DAE2")
    Jump("loc_DC22")

    label("loc_DAE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DAF0")
    Jump("loc_DC22")

    label("loc_DAF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DC22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DC22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBD2")
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0576
    ChrTalk(
        0xE,
        (
            "你们的所作所为\x01",
            "已经完全算是犯罪行为了。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xE,
        "就不能稍微反省一下吗！？\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x11,
        "哼，别那么凶巴巴的。\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x13,
        (
            "反省～反省～\x01",
            "好啦，反省完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x12,
        (
            "真烦人，真希望能\x01",
            "早点回去啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_DC1D")

    label("loc_DBD2")


    #C0581
    ChrTalk(
        0xE,
        (
            "你们的所作所为\x01",
            "已经完全算是犯罪行为了。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xE,
        "就不能稍微反省一下吗！？\x02",
    )

    CloseMessageWindow()

    label("loc_DC1D")

    Jump("loc_DC22")

    label("loc_DC22")

    TalkEnd(0xFE)
    Return()

    # Function_36_D91E end

    def Function_37_DC26(): pass

    label("Function_37_DC26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DCB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC44")
    Call(0, 38)
    Jump("loc_DCB4")

    label("loc_DC44")


    #C0583
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "那个总统演说\x01",
            "简直就是宣战公告啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "虽说有国防军，\x01",
            "但我可不觉得他们\x01",
            "有实力与两大国对抗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCB4")

    Jump("loc_DE9D")

    label("loc_DCB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DCC7")
    Jump("loc_DE9D")

    label("loc_DCC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DD3C")

    #C0585
    ChrTalk(
        0xFE,
        (
            "终于熬过一晚了……\x01",
            "看样子，状况还在不断恶化啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "公共安全科今后\x01",
            "还要进一步努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE9D")

    label("loc_DD3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DDE0")

    #C0587
    ChrTalk(
        0xF,
        (
            "虽然还不能说\x01",
            "现在已经可以严格管制\x01",
            "外国人的违法行为了……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xF,
        (
            "但通过这次的案例，也算是迈出了很重要的一步。\x01",
            "我们警察一定要不畏困难，\x01",
            "继续努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE9D")

    label("loc_DDE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DDEE")
    Jump("loc_DE9D")

    label("loc_DDEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DDFC")
    Jump("loc_DE9D")

    label("loc_DDFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DE0A")
    Jump("loc_DE9D")

    label("loc_DE0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DE18")
    Jump("loc_DE9D")

    label("loc_DE18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DE26")
    Jump("loc_DE9D")

    label("loc_DE26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DE34")
    Jump("loc_DE9D")

    label("loc_DE34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DE42")
    Jump("loc_DE9D")

    label("loc_DE42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DE9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE5D")
    Call(0, 33)
    Jump("loc_DE9D")

    label("loc_DE5D")

    ClearChrFlags(0xF, 0x10)

    #C0589
    ChrTalk(
        0xF,
        (
            "（这些家伙到底是\x01",
            "  如何养成如此恶劣的性格的……！？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE9D")

    TalkEnd(0xFE)
    Return()

    # Function_37_DC26 end

    def Function_38_DEA1(): pass

    label("Function_38_DEA1")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x101, 0)

    #C0590
    ChrTalk(
        0xE,
        (
            "啊，罗伊德，\x01",
            "不得了了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    #C0591
    ChrTalk(
        0xF,
        (
            "你们支援科有没有\x01",
            "听到什么消息？\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#00003F啊，不，并没有……\x02\x03",

            "#00001F我们还不了解详细情况，\x01",
            "正在等待科长的联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xF,
        (
            "原来如此，\x01",
            "和我们公共安全科一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xE,
        (
            "在会议结束后，\x01",
            "应该就会下达具体通知……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xE,
        (
            "但到底会是什么结果，\x01",
            "真是完全猜想不到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xF,
        (
            "不管怎么说，现在似乎也只能\x01",
            "顺其自然了……\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xF,
        (
            "罗伊德，你们似乎还在\x01",
            "自由行动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xF,
        (
            "总之，\x01",
            "注意不要被国防军\x01",
            "给盯上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x18F, 6)
    Return()

    # Function_38_DEA1 end

    def Function_39_E082(): pass

    label("Function_39_E082")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E093")
    Jump("loc_E5E1")

    label("loc_E093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E0A1")
    Jump("loc_E5E1")

    label("loc_E0A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E1B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E14A")

    #C0600
    ChrTalk(
        0xFE,
        (
            "警队一分为二，\x01",
            "其中一半要留下待命，\x01",
            "为警备队提供援助。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "另一半将要加强\x01",
            "市内的巡逻工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xFE,
        (
            "正是在艰难的时期，\x01",
            "才更需要互相支撑啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_E1B0")

    label("loc_E14A")


    #C0603
    ChrTalk(
        0xFE,
        (
            "毕竟不能只让警备队\x01",
            "的成员为我们流血拼命。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xFE,
        (
            "如果在困难的时候却不能帮上忙，\x01",
            "那还算什么警察嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1B0")

    Jump("loc_E5E1")

    label("loc_E1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E230")

    #C0605
    ChrTalk(
        0xFE,
        (
            "那些难以管教的孩子\x01",
            "今天却在老老实实地\x01",
            "回答问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        (
            "凯特好像喝斥了他们，\x01",
            "没想到竟然会有这么大效果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5E1")

    label("loc_E230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E241")
    Call(0, 40)
    Jump("loc_E5E1")

    label("loc_E241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E24F")
    Jump("loc_E5E1")

    label("loc_E24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E25D")
    Jump("loc_E5E1")

    label("loc_E25D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E26B")
    Jump("loc_E5E1")

    label("loc_E26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E2D7")

    #C0607
    ChrTalk(
        0xFE,
        (
            "嗯，揭幕式已经结束，\x01",
            "总算是可以稍微喘口气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        (
            "呼，休息的时候\x01",
            "果然还是要首选咖啡啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5E1")

    label("loc_E2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E2E5")
    Jump("loc_E5E1")

    label("loc_E2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E300")
    Call(0, 26)
    Jump("loc_E34E")

    label("loc_E300")


    #C0609
    ChrTalk(
        0xFE,
        (
            "唔……那就是所谓的\x01",
            "自我主义者吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xFE,
        (
            "遭到侵害的人们\x01",
            "肯定是无法接受的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E34E")

    Jump("loc_E5E1")

    label("loc_E353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E5E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4F8")

    #C0611
    ChrTalk(
        0xFE,
        (
            "哦，是你们，\x01",
            "加入了新成员的特别任务支援科啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        (
            "你们终于恢复\x01",
            "正常工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        "#00000F是的，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x105,
        (
            "#10302F唔，如此说来，\x01",
            "您就是公共安全科的科长吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x109,
        "#10101F那个……请多指教。\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xFE,
        "哦，你们特地赶来，真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "唔，看起来，\x01",
            "支援科聚集了不少有趣的人才嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "我是很看好你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "今后也希望你们跨越各科之间的隔阂，\x01",
            "表现得更加活跃。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x102,
        "#00102F嗯，谢谢您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 3)
    Jump("loc_E5E1")

    label("loc_E4F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E563")

    #C0621
    ChrTalk(
        0x14,
        (
            "嗯，话说回来，\x01",
            "真是来了几个很棘手的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x14,
        (
            "算啦，交给凯特他们负责\x01",
            "应该没问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5E1")

    label("loc_E563")


    #C0623
    ChrTalk(
        0xFE,
        (
            "呼，喝完这罐之后，\x01",
            "还要回去继续开会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "唉呀呀，最近这段时间，会议一直接连不断，\x01",
            "我这快要退休的老头子还真是吃不消。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5E1")

    TalkEnd(0xFE)
    Return()

    # Function_39_E082 end

    def Function_40_E5E5(): pass

    label("Function_40_E5E5")

    OP_4B(0x14, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)

    #C0625
    ChrTalk(
        0x14,
        (
            "等共和国那边的列车到达之后，\x01",
            "就有临时替代的运输手段了。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x14,
        (
            "你们就去车站和空港那边\x01",
            "支援吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x17,
        "是，明白了。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x18,
        "我们马上前往现场。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_40_E5E5 end

    def Function_41_E68A(): pass

    label("Function_41_E68A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E6FE")

    #C0629
    ChrTalk(
        0xFE,
        (
            "公共安全科也重新\x01",
            "开始市内巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xFE,
        (
            "巨大的混乱有可能会造成\x01",
            "治安恶化，\x01",
            "必须要认真巡逻才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7B2")

    label("loc_E6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E70C")
    Jump("loc_E7B2")

    label("loc_E70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E7A6")

    #C0631
    ChrTalk(
        0xFE,
        (
            "总部的复原工作总算告一段落，\x01",
            "刚要松口气，\x01",
            "就被编入到了国防军……\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "从今以后，我就是\x01",
            "一名军人了……老实说，\x01",
            "一时还真是没办法接受呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7B2")

    label("loc_E7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E7B2")
    Call(0, 40)

    label("loc_E7B2")

    TalkEnd(0xFE)
    Return()

    # Function_41_E68A end

    def Function_42_E7B6(): pass

    label("Function_42_E7B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E82F")

    #C0633
    ChrTalk(
        0xFE,
        (
            "国防军已经撤离警察学校，\x01",
            "乔里基科长前往那边\x01",
            "展开事后处理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        "科长不在时，我们必须要好好努力。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E907")

    label("loc_E82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E83D")
    Jump("loc_E907")

    label("loc_E83D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E8D1")

    #C0635
    ChrTalk(
        0xFE,
        (
            "刚觉得总部的复原工作\x01",
            "告一段落了，\x01",
            "马上又被编入了国防军……\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        (
            "从今以后，我就是\x01",
            "一名军人了……老实说，\x01",
            "一时还真是没办法接受呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E907")

    label("loc_E8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E8DF")
    Jump("loc_E907")

    label("loc_E8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E8ED")
    Jump("loc_E907")

    label("loc_E8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E8FB")
    Jump("loc_E907")

    label("loc_E8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E907")
    Call(0, 40)

    label("loc_E907")

    TalkEnd(0xFE)
    Return()

    # Function_42_E7B6 end

    def Function_43_E90B(): pass

    label("Function_43_E90B")

    TalkBegin(0xFE)

    #C0637
    ChrTalk(
        0xFE,
        (
            "我想你们应该听说了，\x01",
            "上层已经做出了决定，\x01",
            "将警察组织编入到了国防军中。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        (
            "在二层的会议室里，\x01",
            "现在正在向各方负责人\x01",
            "介绍今后的体制。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xFE,
        (
            "在上级下达指示之前，\x01",
            "各位就先在自己的部门楼里待命吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_E90B end

    def Function_44_E9D7(): pass

    label("Function_44_E9D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-950, 1500, 7780, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21800, 0)
    SetChrPos(0x101, -900, 40, 1900, 0)
    SetChrPos(0x102, 300, 40, 1900, 0)
    SetChrPos(0x103, -900, 40, 700, 0)
    SetChrPos(0x104, 300, 40, 700, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)

    def lambda_EA62():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA62)
    Sleep(50)

    def lambda_EA7F():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EA7F)
    Sleep(50)

    def lambda_EA9C():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EA9C)
    Sleep(50)

    def lambda_EAB9():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EAB9)
    Sleep(50)
    SetCameraDistance(25000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0640
    ChrTalk(
        0x8,
        "啊，各位……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)

    #C0641
    ChrTalk(
        0x15,
        "哦……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-350, 1540, 12250, 0)
    SetCameraDistance(19950, 0)
    SetChrPos(0x15, 1000, 0, 13400, 180)
    SetChrPos(0x101, 0, 40, 11800, 0)
    SetChrPos(0x102, 2000, 40, 11800, 0)
    SetChrPos(0x103, -200, 40, 10300, 0)
    SetChrPos(0x104, 2200, 40, 10300, 0)
    OP_0D()

    #C0642
    ChrTalk(
        0x15,
        (
            "你们就是特别任务支援科\x01",
            "的各位吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x15,
        (
            "我想你们应该听说了，\x01",
            "上层已经做出了决定，\x01",
            "将警察组织编入到了国防军中。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x15,
        (
            "在二层的会议室里，\x01",
            "现在正在向各方负责人\x01",
            "介绍今后的体制。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x15,
        (
            "在上级下达指示之前，\x01",
            "各位就先在自己的部门楼里待命吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x101,
        "#12P#00001F知、知道了……\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x15,
        (
            "在一层可以自由行动，\x01",
            "但要注意，不要有多余的举动。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x15,
        (
            "如果被认定为举止可疑的人员，\x01",
            "有可能会当场遭到拘捕，\x01",
            "还请谅解。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#12P#00006F明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x102,
        "#12P#00108F（有种很强的威严感呢……）\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x104,
        (
            "#12P#00303F（嗯，看来我们不能\x01",
            "  鲁莽顶撞。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrPos(0x15, 2990, 0, 11810, 270)
    SetScenarioFlags(0x18F, 7)
    ClearMapFlags(0x10000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_44_E9D7 end

    def Function_45_EDDC(): pass

    label("Function_45_EDDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch02502.itc", 0x24)
    LoadChrToIndex("chr/ch30102.itc", 0x25)
    LoadChrToIndex("chr/ch30302.itc", 0x26)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis312.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis404.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -62750, 150, 16149, 0)
    SetChrPos(0x102, -65000, 150, 16149, 0)
    SetChrPos(0x104, -65000, 150, 19900, 180)
    SetChrPos(0x109, -67250, 150, 19900, 180)
    SetChrPos(0x105, -67250, 150, 16149, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0xF)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, -57600, 0, 18000, 270)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x2)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x4)
    SetChrPos(0x19, -60500, 150, 16149, 0)
    OP_4B(0x14, 0xFF)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, -62750, 150, 19900, 180)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -60500, 150, 19900, 180)
    SetMapObjFrame(0xFF, "isu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu_sd", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_78(0x3, 0x1A)
    OP_78(0x4, 0x1B)
    OP_78(0x5, 0x1C)
    OP_78(0x6, 0x1D)
    OP_78(0x7, 0x1E)
    OP_78(0x8, 0x1F)
    OP_78(0x9, 0x20)
    OP_78(0xA, 0x21)
    OP_49()
    SetChrPos(0x1A, -60500, 0, 15900, 0)
    OP_D5(0x1A, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1B, -60500, 0, 20100, 0)
    OP_D5(0x1B, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1C, -62750, 0, 15900, 0)
    OP_D5(0x1C, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1D, -62750, 0, 20100, 0)
    OP_D5(0x1D, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1E, -65000, 0, 15900, 0)
    OP_D5(0x1E, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1F, -65000, 0, 20100, 0)
    OP_D5(0x1F, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x20, -67250, 0, 15900, 0)
    OP_D5(0x20, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x21, -67250, 0, 20100, 0)
    OP_D5(0x21, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(-62500, 2200, 18000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0652
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "在各国首脑\x01",
            "抵达克洛斯贝尔及\x01",
            "兰花塔正式对外公开的前一天。\x02\x03",

            "特别任务支援科的成员\x01",
            "被叫到警察总部的对策会议现场。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(-62500, 1200, 18000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0653
    AnonymousTalk(
        0xC,
        (
            "──以上就是从明日开始的三天之内，\x01",
            "针对通商会议的警备体制。\x02\x03",

            "贝尔加德门、唐古拉姆门\x01",
            "及边境附近都由警备队\x01",
            "设立了盘查人员。\x02\x03",

            "至于市内──\x01",
            "乔里基科长，多诺邦警督。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetChrSubChip(0x14, 0x0)
    Sleep(250)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x19, 0x0)

    #C0654
    ChrTalk(
        0x14,
        (
            "#5P嗯，已经派公共安全科\x01",
            "的全体成员在市内展开巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x14,
        "#5P在会议结束前，都会保持全力工作状态。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0656
    ChrTalk(
        0xA,
        (
            "#5P二科正在车站、空港及商业区域\x01",
            "进行重点警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xA,
        (
            "#5P在会议结束之前，\x01",
            "我们也会全体出动。\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0xC,
        (
            "#11P#00603F警备工作的整体指挥目前由\x01",
            "搜查一科来负责。\x02\x03",

            "#00600F我们自信可以应对\x01",
            "任何所能想到的紧急事态……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x2)
    Sleep(200)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)

    #C0659
    ChrTalk(
        0x19,
        (
            "#12P#01003F……不过，无论多么严密的警备体制，\x01",
            "也都不会是绝对完美的。\x02\x03",

            "#01000F所以，这时就该轮到我们支援科出动啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xC,
        (
            "#11P#00604F嗯，正如之前所说，\x01",
            "赛尔盖科长将以对外联络负责人\x01",
            "的身份留守警备指挥总部。\x02\x03",

            "#00602F与警备队那边的联络工作\x01",
            "也由赛尔盖科长负责。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x19,
        "#12P#01006F哎呀呀，真会使唤人。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0xA,
        (
            "#5P哈哈，因为你一直\x01",
            "喜欢四处插手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xA,
        (
            "#5P而且每次都能突击到各种死角，\x01",
            "建立完善的搜查体制……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x14,
        (
            "#5P嗯嗯，『见缝插针的赛尔盖』\x01",
            "大显身手的景象\x01",
            "似乎已经浮现在我眼前了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x0)
    Sleep(300)

    #C0665
    ChrTalk(
        0x19,
        "#12P#01005F喂，不要再提过去的事情了。\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x101,
        "#12P#00002F『见缝插针的赛尔盖』吗……\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x102,
        (
            "#6P#00109F呵呵……\x01",
            "真是个非常贴切的称呼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x1)
    Sleep(300)

    #C0668
    ChrTalk(
        0x19,
        "#11P#01006F那都是以前的事情啦，以前的。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x19, 0x2)
    Sleep(200)

    #C0669
    ChrTalk(
        0x19,
        (
            "#12P#01000F那么……\x01",
            "暂时没这些家伙什么事了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0xC,
        (
            "#11P#00603F嗯，目前没有。\x02\x03",

            "#00600F我希望他们暂时以\x01",
            "机动队伍的形式来行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0671
    ChrTalk(
        0x109,
        "#10105F机动队伍是……\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x101,
        (
            "#12P#00001F也就是继续处理平时的支援任务，\x01",
            "如果出现什么特殊情况，\x01",
            "就立刻进行支援吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xC,
        (
            "#11P#00606F嗯，正是如此。\x02\x03",

            "虽然也委托了游击士协会做同样的事情，\x01",
            "但我们毕竟不能完全依靠协会。\x02\x03",

            "#00601F而且……\x01",
            "既然连那种家伙都已潜入克洛斯贝尔，\x01",
            "我希望能对预想外的事态多加一道保险。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)

    #C0674
    ChrTalk(
        0x102,
        "#6P#00108F那种家伙……\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x104,
        "#00303F是指『赤色星座』吧。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xC,
        "#11P#00601F嗯……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0677
    AnonymousTalk(
        0xC,
        (
            "#00603F猎兵团『赤色星座』……\x02\x03",

            "活动于塞姆里亚大陆西部，\x01",
            "被称为最强的猎兵团之一。\x02\x03",

            "#00601F已经确认，\x01",
            "他们的大部分成员\x01",
            "现在都已潜入克洛斯贝尔。\x02\x03",

            "顺便一提，大约在一年前左右，\x01",
            "他们在共和国地区似乎曾与\x01",
            "『黑月』展开过大规模的争斗。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0678
    ChrTalk(
        0x14,
        "#5P唔，真是群危险的家伙啊。\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xA,
        (
            "#5P也就是说，他们打算在市内\x01",
            "与黑月继续争斗吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0xC,
        (
            "#11P#00603F不，一般来说，\x01",
            "猎兵团只有收了钱才会行动。\x02\x03",

            "否则，就算以前有过冲突，\x01",
            "也不会因此而再次开战。\x02\x03",

            "#00600F奥兰多，是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x104,
        (
            "#00306F不错。\x02\x03",

            "#00303F与领地观念很强的黑手党有所不同，\x01",
            "对猎兵团而言，米拉和战场就是一切。\x02\x03",

            "昨天的敌人变成今天的朋友……这算是家常便饭，\x01",
            "当然反过来也是一样。\x02\x03",

            "#00300F从这层意义来说，\x01",
            "他们并不会因为过去的争斗而纠缠不休。\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x105,
        (
            "#6P#N#10304F呵呵，既然如此，\x01",
            "似乎就有一个谜团浮出水面了。\x02\x03",

            "#10302F那就是——『赤色星座』\x01",
            "为什么要来到克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0683
    ChrTalk(
        0xC,
        (
            "#11P#00606F一科虽然也曾调查过，\x01",
            "但并未查明他们的目的。\x02\x03",

            "#00601F不过，帝国政府是他们的后盾，\x01",
            "这一点是可以确定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x102,
        (
            "#6P#00108F他们可能会在\x01",
            "和通商会议相关的事情上有所行动……\x02\x03",

            "#00101F也可能是想压制共和国派组织『黑月』\x01",
            "的成长势头？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x19,
        (
            "#12P#01006F嗯，各种推测都有一定的可能性。\x02\x03",

            "#01000F不管怎么说，\x01",
            "在通商会议期间，他们绝对是\x01",
            "一股不容忽视的势力。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0xC,
        (
            "#11P#00603F嗯，那当然。\x02\x03",

            "#00600F顺便一说，\x01",
            "『赤色星座』似乎曾多次\x01",
            "前往克洛斯贝尔市的周边地区。\x02\x03",

            "如果你们前往市外各地，\x01",
            "希望能顺便探查他们的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x101,
        (
            "#12P#00003F──明白了。\x02\x03",

            "#00001F那么，我们就在处理支援请求的同时，\x01",
            "收集有关『赤色星座』的情报。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(50)
    SetChrSubChip(0x14, 0x0)
    Sleep(100)

    #C0688
    ChrTalk(
        0x102,
        (
            "#6P#00100F如果有什么需要，\x01",
            "我们就为各方面提供支援，\x01",
            "请随时联络我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xA,
        "#5P哦哦，真是可靠啊。\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x14,
        "#5P那到时候就不客气啦～\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E5(0xA)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_EDDC end

    def Function_46_100DC(): pass

    label("Function_46_100DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-690, 1400, 7180, 0)
    MoveCamera(34, 9, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0x101, -900, 40, 1900, 0)
    SetChrPos(0x102, 300, 40, 1900, 0)
    SetChrPos(0x109, -900, 40, 700, 0)
    SetChrPos(0x105, 300, 40, 700, 0)

    def lambda_1015F():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1015F)
    Sleep(50)

    def lambda_1017C():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1017C)
    Sleep(50)

    def lambda_10199():
        OP_98(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10199)
    Sleep(50)

    def lambda_101B6():
        OP_98(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_101B6)
    Sleep(50)
    SetCameraDistance(20430, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0691
    ChrTalk(
        0x8,
        "哦，各位。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(500)

    #C0692
    ChrTalk(
        0x9,
        "#5P#01902F啊，大家，还有姐姐！\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x109,
        (
            "#12P#10106F真是的，我不是说过，\x01",
            "在工作场合不要叫我姐姐吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-900, 1540, 13080, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, -900, 40, 12200, 0)
    SetChrPos(0x102, 300, 40, 11800, 0)
    SetChrPos(0x109, -1200, 40, 10800, 0)
    SetChrPos(0x105, 500, 40, 10600, 0)

    def lambda_10314():
        OP_98(0x101, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10314)
    Sleep(50)

    def lambda_10331():
        OP_98(0x102, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10331)
    Sleep(50)

    def lambda_1034E():
        OP_98(0x109, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1034E)
    Sleep(50)

    def lambda_1036B():
        OP_98(0x105, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1036B)
    Sleep(50)
    TurnDirection(0x9, 0x101, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    #C0694
    ChrTalk(
        0x101,
        (
            "#12P#00002F哈哈，瑞贝卡小姐，\x01",
            "你辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x102,
        "#12P#00102F好久不见。\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x8,
        (
            "呵呵呵，\x01",
            "特别任务支援科重新开始工作了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x8,
        (
            "马上就开始\x01",
            "处理支援请求了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，刚刚加入了新成员，\x01",
            "准备在市内巡逻，同时处理支援请求。\x02\x03",

            "对了，我们还接到了一科的支援请求，\x01",
            "请问艾玛警官在哪里？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x8,
        "她在那边的会议室里等着你们呢。\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x8,
        (
            "竟然会接到一科的协助请求，\x01",
            "各位可真是混出头了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        "呵呵，不由得感慨良多啊。\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        "#12P#00012F啊哈哈，哪里……\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，只要别把一些\x01",
            "刁难人的麻烦事情推给我们就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x102,
        "#12P#00106F瓦吉，你真是的……\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#00001F好、好啦，我们赶快\x01",
            "去听听艾玛警官的指示吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x9,
        "#11P#01909F加油哦～\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x130, 0)
    OP_29(0x66, 0x1, 0x0)
    SetChrPos(0x0, -350, 0, 12250, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_46_100DC end

    def Function_47_10636(): pass

    label("Function_47_10636")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-57410, 1500, 17030, 0)
    MoveCamera(47, 35, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, -56800, 0, 17250, 0)
    SetChrPos(0x102, -57800, 0, 17000, 0)
    SetChrPos(0x109, -56800, 0, 16000, 0)
    SetChrPos(0x105, -57800, 0, 15750, 0)
    OP_4B(0xD, 0xFF)
    OP_93(0xD, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0707
    ChrTalk(
        0xD,
        (
            "已经来了啊……\x01",
            "班宁斯搜查官。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        (
            "#12P#00012F您、您好，艾玛警官，\x01",
            "之前真是承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xD,
        (
            "是指在一科研修时的事情吗？\x01",
            "我并没有关照你什么，\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xD,
        (
            "只是听从达德利长官\x01",
            "的指示而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xD,
        (
            "你的资质确实不错……\x01",
            "但竟然拒绝一科的邀请，重回支援科，\x01",
            "实在是让人很难理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        "#12P#00006F不、不好意思。\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x102,
        "#12P#00105F（似乎发生过不少事情……）\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x109,
        (
            "#12P#10100F（像罗伊德警官这么优秀的人，\x01",
            "  肯定会是各部门的争抢目标呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0xD,
        (
            "算啦，不说这些了，\x01",
            "赶快进入正题。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xD,
        (
            "既然来了，\x01",
            "就说明你们\x01",
            "愿意帮忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯，那当然。\x02\x03",

            "#00001F听说……\x01",
            "那个雷克特·亚兰德尔\x01",
            "来到克洛斯贝尔了？\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0xD,
        "一科掌握到的情报是这样。\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xD,
        (
            "……但很遗憾，\x01",
            "目前还无法确定。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0720
    ChrTalk(
        0x101,
        "#12P#00005F那是由于……？\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x102,
        (
            "#12P#00105F是因为无法确认\x01",
            "他的具体所在地吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0xD,
        (
            "雷克特来到克洛斯贝尔这条情报\x01",
            "本身就尚未得到确认。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xD,
        (
            "虽然也有相关的目击情报……\x01",
            "但是，每当追查他的行踪时，\x01",
            "都会被其神出鬼没地摆脱……\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xD,
        (
            "恐怕是察觉到了我们的举动，\x01",
            "有意逃离追踪的。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x101,
        "#12P#00013F……原来如此……\x02",
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x109,
        "#12P#10106F真、真是个不得了的人呢。\x02",
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，对那位老兄来说，\x01",
            "这种程度的躲藏大概并不为难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xD,
        (
            "正因如此，\x01",
            "所以希望由你们来确认\x01",
            "雷克特·亚兰德尔滞留在此的事实。\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0xD,
        (
            "确定他是否真的来到克洛斯贝尔了，\x01",
            "还是说，这仅仅是假情报而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0xD,
        (
            "如果可能的话，\x01",
            "希望你们同时确认其帝国军官，\x01",
            "以及帝国政府书记官的身份。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x101,
        "#12P#00000F……明白了。\x02",
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x102,
        "#12P#00100F不过，为什么要找我们呢？\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xD,
        (
            "因为你们以前\x01",
            "曾与他有过数次接触。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0xD,
        "再有就是我想赌赌运气。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0735
    ChrTalk(
        0x101,
        "#12P#00012F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，虽然是精英警官，\x01",
            "但处理事情时却意外地懂得灵活变通啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0xD,
        "哼……这也是没办法的事吧。\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xD,
        (
            "如果多派些人手，自然也能捉到他，\x01",
            "但如果行事过于草率，有可能会演变成外交问题，\x01",
            "而且我们还有其它案件需要处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xD,
        (
            "……如果不是达德利长官不在，\x01",
            "才不需要拜托你们帮忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0740
    ChrTalk(
        0x101,
        (
            "#12P#00005F如此说来……\x01",
            "达德利警官去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xD,
        (
            "为了商讨通商会议\x01",
            "期间的警备问题，\x01",
            "昨天晚上前往利贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xD,
        "大概要明天才能回来。\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x101,
        "#12P#00001F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x102,
        "#12P#00100F真是很忙呢……\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0xD,
        (
            "所以说，在他回来之前，\x01",
            "我无论如何也想把问题彻底解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0xD,
        (
            "否则的话，他出差归来之后，无论多么疲惫，\x01",
            "也会把事情都揽在自己身上。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        "#12P#00103F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x109,
        (
            "#12P#10106F确实，达德利警官\x01",
            "肯定会那样做的……\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#12P#00003F明白了，\x01",
            "我们接受任务。\x02\x03",

            "#00000F对了……\x01",
            "请问目击到雷克特大尉\x01",
            "的地点是哪里？\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0xD,
        (
            "这个嘛……\x01",
            "真伪还无法确定。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xD,
        (
            "但根据目击情报，\x01",
            "是在后巷一带。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x102,
        (
            "#12P#00105F后巷……\x01",
            "是鲁巴彻旧址的附近呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x105,
        "#12P#10302F呵呵，这地方倒是和他的风格很相称。\x02",
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x101,
        (
            "#12P#00000F明白了，\x01",
            "我们会尽快开始调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0xD,
        "拜托了。\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xD,
        (
            "我会在一科等待，\x01",
            "报告时请让接待员联系我。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xD,
        "那就先告辞了。\x02",
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_111FC():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_111FC)

    def lambda_11209():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11209)

    def lambda_11216():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11216)

    def lambda_11223():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11223)
    OP_68(-57500, 1500, 16430, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_11275():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11275)

    def lambda_11282():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11282)

    def lambda_1128F():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1128F)

    def lambda_1129C():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1129C)
    OP_0D()
    OP_6F(0x1)

    #C0758
    ChrTalk(
        0x101,
        "#11P#00006F呼……\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x102,
        (
            "#6P#00100F你在一科研修的时候，\x01",
            "受过她不少关照吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x101,
        (
            "#11P#00000F嗯，态度虽然很严厉，\x01",
            "但一直都耐心细致地教导我。\x02\x03",

            "#00004F该怎么说好呢……\x01",
            "总之就是个一丝不苟的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x109,
        "#10102F呵呵，的确就是那种感觉。\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x105,
        (
            "#12P#10304F嗯～但越是这种性格的姐姐，\x01",
            "越是渴望有人安慰……\x02\x03",

            "#10302F呵呵，不如今晚就\x01",
            "邀请她一起喝酒吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        (
            "#11P#00006F我说你啊……\x02\x03",

            "#00000F总之，已经有了初期目标，\x01",
            "我们赶快去寻找雷克特先生吧。\x02\x03",

            "首先从后巷开始找。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x102,
        "#6P#00100F嗯，我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0765
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【确认帝国书记官的身份】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x130, 1)
    OP_29(0x66, 0x1, 0x1)
    SetChrPos(0x0, -56800, 0, 17500, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_47_10636 end

    def Function_48_11506(): pass

    label("Function_48_11506")

    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(400)
    Sound(104, 0, 100, 0)
    Return()

    # Function_48_11506 end

    def Function_49_11519(): pass

    label("Function_49_11519")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x4)
    SetChrPos(0xD, -57300, 0, 18750, 180)
    OP_4B(0xD, 0xFF)
    OP_68(-57300, 1500, 17520, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -56800, 0, 17250, 0)
    SetChrPos(0x102, -57800, 0, 17000, 0)
    SetChrPos(0x109, -56800, 0, 16000, 0)
    SetChrPos(0x105, -57800, 0, 15750, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0766
    ChrTalk(
        0xD,
        (
            "辛苦了，\x01",
            "你们似乎掌握了不少情报啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#12P#00001F嗯，真是没想到，\x01",
            "他竟然会那么坦然自若地\x01",
            "正面承认自己是情报局的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xD,
        (
            "……他大概是有着十足的自信，\x01",
            "认为自己即使暴露了身份，\x01",
            "我们也限制不住他的谍报活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0xD,
        (
            "不过，如此一来，连他的滞留时间\x01",
            "也大致掌握到了……\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0xD,
        (
            "你们真是取得了\x01",
            "预想之上的成果啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x101,
        (
            "#12P#00002F哈哈……\x01",
            "真是太过奖了。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，某人总算是没有\x01",
            "白白献出自己的身体啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x102,
        "#6P#00113F才、才没有献出身体！\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0xD,
        (
            "说起来……我也有些在意\x01",
            "同行的那名少女。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xD,
        (
            "你们认为她会是雷克特大尉\x01",
            "在谍报工作方面的部下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x101,
        (
            "#12P#00003F……不，我认为不是。\x02\x03",

            "#00008F以谍报人员的标准来看，她的年纪太小了，\x01",
            "而且十分天真无邪。\x02\x03",

            "#00001F当然，我也不认为\x01",
            "她只是普通民间人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x109,
        (
            "#12P#10101F……是啊，\x01",
            "她的身手十分敏捷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xD,
        (
            "明白了，\x01",
            "一科这边也会去调查\x01",
            "那名少女的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0xD,
        (
            "那么，我就先告辞了。\x01",
            "这次真是承蒙各位的关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x101,
        (
            "#12P#00002F哪里，如果以后还有什么事情，\x01",
            "请不必客气，随时联络我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_1197F():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1197F)

    def lambda_1198C():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1198C)

    def lambda_11999():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11999)

    def lambda_119A6():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_119A6)
    OP_68(-57300, 1500, 16880, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_119F8():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_119F8)

    def lambda_11A05():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11A05)

    def lambda_11A12():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11A12)

    def lambda_11A1F():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11A1F)
    OP_0D()
    OP_6F(0x1)

    #C0781
    ChrTalk(
        0x101,
        (
            "#00006F呼……\x01",
            "总算是不负所望。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#6P#00106F……呼，是啊……\x02\x03",

            "#00108F但话说回来，那个孩子……\x01",
            "究竟是什么人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x109,
        (
            "#10101F嗯，确实让人在意……\x01",
            "虽然她轻松自然地蒙混了过去，\x01",
            "但实在是不像普通的旅行者。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x105,
        (
            "#12P#10302F与大国的情报局军官同行，\x01",
            "天真无邪的奔放少女……\x02\x03",

            "#10304F呵呵，真是很耐人寻味呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0785
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【确认帝国书记官的身份】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x66, 0x1, 0x5)
    OP_29(0x66, 0x1, 0x6)
    OP_29(0x66, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x3)
    SetChrPos(0x0, -56800, 0, 17500, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_49_11519 end

    def Function_50_11BDC(): pass

    label("Function_50_11BDC")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(-4980, 1900, 10000, 0)
    MoveCamera(27, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20960, 0)
    SetChrPos(0x101, -5180, 0, 11860, 90)
    SetChrPos(0x102, -5660, 0, 10860, 90)
    SetChrPos(0x109, -6640, 0, 11950, 90)
    SetChrPos(0x105, -7250, 0, 10910, 90)
    OP_68(-1640, 1900, 10930, 3000)

    def lambda_11C6F():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C6F)
    Sleep(50)

    def lambda_11C8C():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11C8C)
    Sleep(50)

    def lambda_11CA9():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11CA9)
    Sleep(50)

    def lambda_11CC6():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11CC6)
    Sleep(300)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    #C0786
    ChrTalk(
        0x8,
        (
            "啊……支援科的各位，\x01",
            "你们的工作好像已经完成了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-710, 1500, 13250, 1500)
    MoveCamera(43, 24, 0, 1500)

    def lambda_11D91():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11D91)
    Sleep(50)

    def lambda_11DAE():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11DAE)
    Sleep(50)

    def lambda_11DCB():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11DCB)
    Sleep(50)

    def lambda_11DE8():
        OP_97(0xFE, 0x3E8, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11DE8)
    WaitChrThread(0x101, 1)

    def lambda_11E06():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11E06)
    WaitChrThread(0x109, 1)

    def lambda_11E17():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11E17)
    WaitChrThread(0x102, 1)

    def lambda_11E28():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11E28)
    WaitChrThread(0x105, 1)

    def lambda_11E39():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11E39)
    Sleep(300)
    OP_6F(0x79)

    #C0787
    ChrTalk(
        0x101,
        (
            "#12P#00002F嗯，刚才已经\x01",
            "报告完毕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，总算是\x01",
            "完成了一件工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x8,
        "呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x8,
        (
            "支援科再次开始工作，\x01",
            "我想今后也会有大量的委托等着你们，\x01",
            "请继续加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x102,
        (
            "#12P#00102F谢谢，\x01",
            "瑞贝卡小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x109,
        (
            "#12P#10100F身为支援科的新成员，\x01",
            "我的不足之处还有很多……\x01",
            "但一定会多加努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0793
    ChrTalk(
        0x8,
        (
            "对了，各位，\x01",
            "你们有没有好好活用新战斗手册呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x8,
        (
            "罗伊德警官在一科研修时\x01",
            "应该收到过它……\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x101,
        (
            "#12P#00000F啊，如此说来……\x01",
            "嗯，我们会多加活用的。\x02\x03",

            "#00004F当手册中的情报有所增加后，\x01",
            "带来向瑞贝卡小姐\x01",
            "报告就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x8,
        "嗯，那样再好不过。\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x8,
        (
            "特别是在最近，有关新型魔兽的报告\x01",
            "也有增加的趋势……\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x8,
        (
            "为了把握其特性，从而制定安全对策，\x01",
            "希望能尽可能地收集更多的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x8,
        (
            "与以往一样，总部会阶段性地\x01",
            "支付一定奖励，\x01",
            "还请各位多加协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x101,
        "#12P#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x109,
        (
            "#12P#10100F就是说，最好定期\x01",
            "来这里提交战斗手册吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x8,
        "呵呵，我会在这里等着的。\x02",
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x8,
        (
            "对了……\x01",
            "还有一件事情\x01",
            "必须要告诉大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x8,
        (
            "各位在处理教团事件时，\x01",
            "曾在据点的终端装置中发现了一些信息……\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x8,
        (
            "不久前，鉴定科终于找到了\x01",
            "解析那些信息的可能性。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0806
    ChrTalk(
        0x102,
        "#12P#00105F真、真的吗！？\x02",
    )

    CloseMessageWindow()

    def lambda_122B2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_122B2)
    Sleep(50)

    def lambda_122C2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_122C2)
    Sleep(300)

    #C0807
    ChrTalk(
        0x105,
        "#6P#10305F嗯？你们在说什么？\x02",
    )

    CloseMessageWindow()

    def lambda_122F4():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_122F4)
    Sleep(50)

    def lambda_12304():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12304)
    Sleep(300)

    #C0808
    ChrTalk(
        0x101,
        (
            "#11P#00003F……处理教团事件时，\x01",
            "我们曾在『太阳堡垒』的终端内\x01",
            "取得了一些信息。\x02\x03",

            "那是约亚西姆·琼塔所记载的，\x01",
            "关于『Ｄ∴Ｇ教团』\x01",
            "的文字记录。\x02\x03",

            "#00008F由于部分文字被故意消除，\x01",
            "无法顺利解读，\x01",
            "所以就交给了鉴定科……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0809
    ChrTalk(
        0x101,
        (
            "#12P#00001F莫非鉴定科已经将那些\x01",
            "被消除掉的文字恢复了？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12432():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12432)
    Sleep(50)

    def lambda_12442():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12442)
    Sleep(50)

    def lambda_12452():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12452)
    Sleep(300)

    #C0810
    ChrTalk(
        0x8,
        (
            "不，据鉴定科的成员表示，\x01",
            "目前只是发现了恢复的\x01",
            "可能性而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x8,
        (
            "在记录结晶的内部\x01",
            "存在着破损的\x01",
            "数据碎片……\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x8,
        (
            "要想完全解析，\x01",
            "恐怕需要相当长的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x109,
        (
            "#12P#10106F是吗……\x02\x03",

            "#10108F还以为终于可以\x01",
            "了解到那起事件中的\x01",
            "不明之处了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x101,
        (
            "#12P#00003F……现在似乎也只能\x01",
            "老老实实地等着了。\x02\x03",

            "#00000F瑞贝卡小姐，\x01",
            "多谢你告诉我们这个消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x8,
        "呵呵，别客气。\x02",
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        (
            "只要和我说一声，\x01",
            "随时都可以查阅\x01",
            "终端中的资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "如果解析工作取得了进展，\x01",
            "我会通知大家的。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x102,
        "#12P#00100F嗯，那就拜托啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    SetScenarioFlags(0x130, 7)
    ModifyEventFlags(0, 1, 0x80)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_11BDC end

    def Function_51_12678(): pass

    label("Function_51_12678")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-124920, 1500, 15840, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    LoadChrToIndex("chr/ch44102.itc", 0x1E)
    LoadChrToIndex("chr/ch47500.itc", 0x1F)
    LoadChrToIndex("chr/ch23600.itc", 0x20)
    LoadChrToIndex("chr/ch30100.itc", 0x21)
    LoadChrToIndex("chr/ch30002.itc", 0x22)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xE, -34500, 0, 18310, 180)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    SetChrPos(0x101, -35350, 0, 16000, 0)
    SetChrPos(0x102, -34150, 0, 16000, 0)
    SetChrPos(0x109, -35350, 0, 14800, 0)
    SetChrPos(0x105, -34150, 0, 14800, 0)
    OP_4B(0x14, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0819
    ChrTalk(
        0xF,
        (
            "好了，现在要开始备案，\x01",
            "请你们回答我的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0xF,
        "嗯……你们的姓名是什么？\x02",
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x13,
        "无名氏。（不屑一顾）\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x12,
        "洛克史密斯。（摇头晃脑）\x02",
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x11,
        (
            "哼，我们有义务回答\x01",
            "你这种人的问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0824
    ChrTalk(
        0xF,
        (
            "你、你们几个！！\x01",
            "得意忘形也要有个限度……！\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x14,
        (
            "好啦好啦，弗兰茨，\x01",
            "先冷静一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x12,
        "哈哈，被人警告了吧。\x02",
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x13,
        "活该。\x02",
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x11,
        "哎呀呀，平民果然就是平民……\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-35670, 1800, 15820, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20190, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0829
    ChrTalk(
        0x109,
        (
            "#10101F……他们受到的惩罚\x01",
            "竟然只有罚款吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0xE,
        "……很遗憾，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0xE,
        (
            "根据自治州法，\x01",
            "如果触犯了交通方面的法规，\x01",
            "至少也会暂时取消驾驶资格……\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0xE,
        (
            "但由于他们是共和国人士，\x01",
            "因此无论如何也无法严格惩处。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0xE,
        (
            "今天对他们进行了严重警告，\x01",
            "但马上就得释放了。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x101,
        "#00003F……果然如此啊。\x02",
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x105,
        (
            "#10300F嗯？你好像早就猜到\x01",
            "会是这种结果了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12B1E():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12B1E)
    Sleep(50)

    def lambda_12B2E():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12B2E)
    Sleep(100)

    #C0836
    ChrTalk(
        0x102,
        (
            "#00108F……因为以前也发生过\x01",
            "类似的事情呢。\x02\x03",

            "像当时的假货商事件，\x01",
            "也只是对违法者进行了严重警告，\x01",
            "并下达了为期仅仅一个月的驱逐令。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x109,
        (
            "#10106F说起来……\x01",
            "确实是有这么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x102,
        (
            "#00103F……迪塔叔叔就任新市长之后，\x01",
            "已经开始了审视、修正\x01",
            "自治州法的工作……\x02\x03",

            "但在如今的状况下，\x01",
            "还是有很多情况是无力改变的呢。\x02\x03",

            "#00101F无权对外国人采取任何强硬措施，\x01",
            "可以说是克洛斯贝尔长年来\x01",
            "始终无法消除的『扭曲现象』之一吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x105,
        (
            "#10306F呼，哎呀呀……\x02\x03",

            "也就是说，\x01",
            "在这起案件中，\x01",
            "我们就算白费力气了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(100)

    #C0840
    ChrTalk(
        0x101,
        (
            "#00004F……不，也不能这么说。\x02\x03",

            "#00000F至今为止，我们确实\x01",
            "经历过很多次同样的事情，\x01",
            "但每一次都绝对不是毫无作用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0xE,
        (
            "这次也一样，\x01",
            "我相信我们的努力不会没有价值。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12DD5():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12DD5)
    Sleep(50)

    def lambda_12DE5():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12DE5)
    Sleep(100)

    #C0842
    ChrTalk(
        0xE,
        (
            "至少，今天不会再有\x01",
            "飙车族的车辆横冲直撞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x101,
        (
            "#00003F……我想，我们今后仍会\x01",
            "多次面对这样的挫折。\x02\x03",

            "#00000F但正因如此，才更要\x01",
            "积极向前，永不放弃。\x01",
            "我认为这是非常重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0844
    ChrTalk(
        0x109,
        (
            "#10101F说得对呢……\x01",
            "我也会继续加油的！\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x105,
        (
            "#10304F既然如此，\x01",
            "那我就努力让你们\x01",
            "凉快凉快吧。\x02\x03",

            "#10302F免得你们头脑发热过了头，\x01",
            "最后情绪失控。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0846
    ChrTalk(
        0x102,
        (
            "#00106F瓦吉，你可真是的……\x01",
            "难得大家充满斗志，\x01",
            "不要在旁边泼冷水嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x101,
        (
            "#00012F……算、算啦。\x02\x03",

            "#00000F那么，凯特前辈……\x01",
            "接下来的事情就交给您了？\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0xE,
        "嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0xE,
        (
            "今天真是谢谢你们了。\x01",
            "如果以后再有什么事情，\x01",
            "还要再拜托大家哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x101,
        "#00002F嗯，随时欢迎。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0851
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【取缔飙车族】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x69, 0x1, 0x0)
    OP_29(0x69, 0x1, 0x1)
    OP_29(0x69, 0x4, 0x10)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0x14, 0x40)
    OP_4C(0x14, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -34750, 0, 15400, 180)
    EventEnd(0x5)
    Return()

    # Function_51_12678 end

    def Function_52_13139(): pass

    label("Function_52_13139")

    EventBegin(0x0)
    Fade(500)
    OP_68(-13030, 1500, 12910, 0)
    MoveCamera(27, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -12540, 0, 13210, 90)
    SetChrPos(0x102, -12540, 0, 14610, 135)
    SetChrPos(0x103, -13740, 0, 13610, 90)
    SetChrPos(0x104, -14000, 0, 14810, 135)
    SetChrPos(0x109, -15000, 0, 13400, 90)
    SetChrPos(0x105, -14100, 0, 12000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13ACA")
    OP_0D()

    #C0852
    ChrTalk(
        0x10,
        (
            "啊啊！玛格丽特……\x01",
            "你为什么要这样……\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x10,
        (
            "竟然会被那种男人吸引，\x01",
            "根本就不像你啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x10,
        (
            "总、总之，\x01",
            "在事情彻底无法挽回之前，\x01",
            "我必须得做点什么才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x101,
        (
            "#00005F（皮埃尔副局长……\x01",
            "  真少见啊，竟然在这种地方。）\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x102,
        "#00105F（他好像正在为什么事情而烦恼呢……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x10, 0x10E, 0x3E8)
    Sleep(50)

    #C0857
    ChrTalk(
        0x10,
        (
            "你、你们几个……\x01",
            "是什么时候开始待在那里的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x10,
        (
            "难……难道说，我刚才自言自语时\x01",
            "说的那些话都被你们听到了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0x104,
        (
            "#00302F没、没有……\x01",
            "并没有听到详细内容啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x103,
        (
            "#00203F只是听到一部分而已，\x01",
            "比如玛格丽特啦，\x01",
            "被那种男人吸引啦……等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x10,
        "（大受打击）……\x02",
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，那是副局长专属的\x01",
            "女公关的名字吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0863
    ChrTalk(
        0x10,
        (
            "不、不要说这种\x01",
            "会让人误会的话！\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x10,
        (
            "玛格丽特……\x01",
            "是我太太的名字！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0865
    ChrTalk(
        0x109,
        "#10105F太、太太……\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x101,
        "#00005F也就是妻子吧？\x02",
    )

    CloseMessageWindow()

    #C0867
    ChrTalk(
        0x10,
        "那还用说！\x02",
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x10,
        (
            "……唉，之前丢了戒指，\x01",
            "又没当上新局长，\x01",
            "如今竟然再次遭受到如此残酷的对待……\x02",
        )
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x10,
        (
            "……呃，我为什么要把这些事情\x01",
            "全都说出来啊！？\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13758")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0870
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆前作的「寻找戒指任务」（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【完成】\x01",          # 1
            "【其它】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1373F"),
        (1, "loc_13744"),
        (2, "loc_1374E"),
        (SWITCH_DEFAULT, "loc_13758"),
    )


    label("loc_1373F")

    Jump("loc_13758")

    label("loc_13744")

    OP_29(0x15, 0x4, 0x10)
    Jump("loc_13758")

    label("loc_1374E")

    OP_29(0x15, 0x3, 0x10)
    Jump("loc_13758")

    label("loc_13758")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_137E1")

    #C0871
    ChrTalk(
        0x101,
        (
            "#00003F（说起来……\x01",
            "  副局长惧内可是很出名的呢。）\x02\x03",

            "#00008F（也就是说，副局长现在的烦恼\x01",
            "  与自己的妻子有关吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1384F")

    label("loc_137E1")


    #C0872
    ChrTalk(
        0x101,
        (
            "#00003F（副局长……\x01",
            "  好像非常惧内呢。）\x02\x03",

            "#00008F（也就是说，副局长现在的烦恼\x01",
            "  与自己的妻子有关吗……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1384F")


    #C0873
    ChrTalk(
        0x10,
        (
            "……唉唉！没办法了！\x01",
            "在这种时候，也顾不得这么多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0874
    ChrTalk(
        0x10,
        (
            "特别任务支援科的各位！\x01",
            "我要交给你们一件机密任务！！\x02",
        )
    )

    CloseMessageWindow()

    #C0875
    ChrTalk(
        0x102,
        (
            "#00105F机密任务吗……？\x01",
            "那究竟是什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0876
    ChrTalk(
        0x10,
        (
            "嗯、嗯……具体来说……\x01",
            "就是委托你们跟踪调查我的太太。\x02",
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

    #C0877
    ChrTalk(
        0x104,
        "#00305F跟、跟踪调查……\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x103,
        (
            "#00206F将职权用于私人目的，\x01",
            "是违反警察局规定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x10,
        (
            "现在就不要在意这些无关紧要的小问题了！\x01",
            "我都已经到了生死攸关的地步了！\x02",
        )
    )

    CloseMessageWindow()

    #C0880
    ChrTalk(
        0x10,
        (
            "总之，你们就当作\x01",
            "正式的委托来处理就行了！\x01",
            "这样可以了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x101,
        (
            "#00006F呃，这个……\x01",
            "（该怎么办呢？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B5D")

    label("loc_13ACA")

    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    #C0882
    ChrTalk(
        0x10,
        (
            "特别任务支援科的各位！\x01",
            "我要交给你们一件机密任务！！\x02",
        )
    )

    CloseMessageWindow()

    #C0883
    ChrTalk(
        0x10,
        (
            "总之，你们就当作\x01",
            "正式的委托来处理就行了！\x01",
            "怎么样，你们就接受这任务吧！？！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B5D")

    Call(0, 53)
    OP_4C(0x10, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -12540, 0, 14410, 0)
    EventEnd(0x5)
    Return()

    # Function_52_13139 end

    def Function_53_13B7C(): pass

    label("Function_53_13B7C")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BD2")
    Call(0, 54)
    Jump("loc_13CB3")

    label("loc_13BD2")


    #C0884
    ChrTalk(
        0x101,
        (
            "#00006F抱歉……\x01",
            "我们还有工作在身呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x10,
        "是、是吗……那也没办法。\x02",
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x10,
        (
            "既然如此，那就尽快完成，\x01",
            "然后赶快回来！\x01",
            "……明白了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0887
    ChrTalk(
        0x101,
        "#00005F我、我们尽力而为。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x174, 7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x10, 0x5A, 0x0)
    SetChrPos(0x0, -12540, 0, 1096611267, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_13CB3")

    Return()

    # Function_53_13B7C end

    def Function_54_13CB4(): pass

    label("Function_54_13CB4")


    #C0888
    ChrTalk(
        0x101,
        (
            "#00001F明、明白了。\x01",
            "看来您真的遇到困难了……\x01",
            "有什么事情就说给我们听听吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x10,
        "哦哦……真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0890
    ChrTalk(
        0x10,
        (
            "很好，既然已经决定了，\x01",
            "那就到副局长室来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0891
    ChrTalk(
        0x10,
        (
            "这里不是说话的地方，\x01",
            "到了那边再详细说明。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_54_13CB4 end

    def Function_55_13D93(): pass

    label("Function_55_13D93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0xFF)
    OP_68(-12660, 1500, 14950, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24690, 0)
    SetChrPos(0x101, -11960, 0, 15570, 225)
    SetChrPos(0x102, -11390, 0, 13820, 315)
    SetChrPos(0x103, -13360, 0, 16370, 135)
    SetChrPos(0x104, -14520, 0, 15460, 90)
    SetChrPos(0x109, -14300, 0, 13610, 90)
    SetChrPos(0x105, -12900, 0, 12810, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0892
    ChrTalk(
        0x104,
        (
            "#00306F哎呀呀，\x01",
            "最后还是接受了\x01",
            "他的请求啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0893
    ChrTalk(
        0x102,
        (
            "#00102F算啦，毕竟副局长\x01",
            "很担心他的夫人……\x02\x03",

            "在查清真相之前，\x01",
            "我们就先帮帮他\x01",
            "好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x103,
        "#00206F呼，没办法啊。\x02",
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x109,
        (
            "#10100F那么，首先应该\x01",
            "去什么地方调查？\x02",
        )
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0x101,
        (
            "#00000F先去中央广场的\x01",
            "西餐厅看看吧。\x02\x03",

            "那个疑似男公关的人\x01",
            "最近好像经常在那里与副局长夫人会面，\x01",
            "我们说不定能直接听到他们的对话。\x02",
        )
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，这主意\x01",
            "似乎不坏呢。\x02\x03",

            "#10309F那好，我们就\x01",
            "赶快出发吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x101,
        "#00006F（他好像一副乐在其中的样子呢……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0899
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【副局长的委托】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x84, 0x4, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x84, 0x4, 0x2)
    OP_29(0x84, 0x1, 0x0)
    SetScenarioFlags(0x175, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_55_13D93 end

    def Function_56_140AB(): pass

    label("Function_56_140AB")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_140F6")

    #C0900
    ChrTalk(
        0x101,
        (
            "#00000F……没什么事情要去上层啊，\x01",
            "还是不要上去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14198")

    label("loc_140F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_14160")
    OP_4B(0x16, 0xFF)
    TurnDirection(0x16, 0x0, 500)

    #C0901
    ChrTalk(
        0x16,
        (
            "导力梯现在\x01",
            "禁止使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0902
    ChrTalk(
        0x16,
        (
            "请各位在一层的会议室\x01",
            "等待指示的下达。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xB4, 0x0)
    OP_4C(0x16, 0xFF)
    Jump("loc_14198")

    label("loc_14160")


    #C0903
    ChrTalk(
        0x101,
        (
            "#00000F……没什么事情要去上层啊，\x01",
            "还是不要上去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14198")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_56_140AB end

    def Function_57_141AC(): pass

    label("Function_57_141AC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_57_141AC end

    SaveToFile()

Try(main)
