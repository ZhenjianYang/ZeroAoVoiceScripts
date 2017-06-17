from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t2010.bin",                # FileName
        "t2010",                    # MapName
        "t2010",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 6, 0, 7],
    )

    BuildStringList((
        "t2010",                  # 0
        "柯纳斯队员",             # 1
        "西格队员",               # 2
        "库雷斯队员",             # 3
        "史黛拉",                 # 4
        "比约德",                 # 5
        "游击士斯克特",           # 6
        "游击士温蔡尔",           # 7
        "游客",                   # 8
        "商人",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "商人",                   # 17
        "游客",                   # 18
        "游客",                   # 19
        "商人",                   # 20
        "游客",                   # 21
        "游客",                   # 22
        "游客",                   # 23
        "女孩",                   # 24
        "商人",                   # 25
        "游客",                   # 26
        "游客库卡",               # 27
        "游客纳特",               # 28
        "车１",                   # 29
        "游客",                   # 30
        "游客",                   # 31
        "车１",                   # 32
        "迪塔总裁",               # 33
        "迪塔总裁",               # 34
        "米蕾优准尉",             # 35
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch24900.itc",                   # 01
        "chr/ch24800.itc",                   # 02
        "chr/ch31202.itc",                   # 03
        "chr/ch32202.itc",                   # 04
        "chr/ch21800.itc",                   # 05
        "chr/ch21802.itc",                   # 06
        "chr/ch22000.itc",                   # 07
        "chr/ch21902.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch21702.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch27600.itc",                   # 0C
        "chr/ch22302.itc",                   # 0D
        "chr/ch32400.itc",                   # 0E
        "chr/ch32402.itc",                   # 0F
        "chr/ch27202.itc",                   # 10
        "chr/ch27302.itc",                   # 11
        "chr/ch32200.itc",                   # 12
        "chr/ch32600.itc",                   # 13
        "chr/ch23000.itc",                   # 14
        "chr/ch26900.itc",                   # 15
        "chr/ch00000.itc",                   # 16
    ))

    DeclNpc(-6590,   0,       7079,    200,  257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8720,    0,       4400,    135,  257,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-97470,  100,     -3950,   270,  341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-105500, 0,       2099,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-162110, 0,       -2500,   90,   257,  0x0, 0,   2,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-99519,  150,     3930,    270,  469,  0x0, 0,   16,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-101790, 150,     3930,    90,   469,  0x0, 0,   17,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   469,  0x0, 0,   4,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-5829,   0,       2259,    180,  385,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-2660,   0,       3680,    90,   385,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-94699,  0,       4190,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-92129,  0,       4190,    270,  469,  0x0, 0,   8,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(10130,   0,       6190,    180,  385,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-101949, 150,     3859,    90,   469,  0x0, 0,   8,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-6329,   0,       5099,    0,    401,  0x0, 0,   9,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-94669,  150,     2319,    90,   401,  0x0, 0,   10,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(5099,    0,       2269,    180,  385,  0x0, 0,   5,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-7019,   0,       2200,    90,   401,  0x0, 0,   7,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-5929,   0,       2200,    270,  401,  0x0, 0,   11,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-1470,   0,       3309,    180,  385,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(2109,    0,       6769,    180,  385,  0x0, 0,   12,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-94669,  150,     4070,    90,   469,  0x0, 0,   15,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-94669,  150,     4070,    90,   469,  0x0, 0,   13,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(-9600,   0,       400,     270,  385,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   469,  0x0, 0,   4,   0,   255, 255, 0,   35,  255,  0)
    DeclNpc(-93300,  0,       -1700,   0,    385,  0x0, 0,   21,  0,   0,   4,   0,   39,  255,  0)
    DeclNpc(-154259, 0,       1389,    45,   385,  0x0, 0,   20,  0,   0,   5,   0,   41,  255,  0)
    DeclNpc(-6000,   0,       0,       225,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(11789,   0,       6219,    180,  385,  0x0, 0,   11,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(4150,    0,       3130,    0,    385,  0x0, 0,   18,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(16569,   0,       5380,    0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(12060,   0,       -3710,   225,  405,  0x0, 0,   19,  0,   0,   0,   0,   38,  255,  0)

    DeclActor(-6600,   0,       6140,    1000,    -6590,   1500,    7080,    0x007E, 0,  8,  0x0000)
    DeclActor(-103650, 0,       1450,    1000,    -105500, 1500,    2100,    0x007E, 0,  12, 0x0000)
    DeclActor(-161140, 0,       -2700,   1000,    -162110, 1500,    -2500,   0x007E, 0,  15, 0x0000)
    DeclActor(9250,    0,       -5930,   2000,    9650,    4000,    -8830,   0x007C, 0,  43, 0x0000)
    DeclActor(2900,    0,       -12480,  1000,    2900,    1000,    -12480,  0x007C, 0,  40, 0x0000)

    ScpFunction((
        "Function_0_630",          # 00, 0
        "Function_1_6E8",          # 01, 1
        "Function_2_785",          # 02, 2
        "Function_3_80E",          # 03, 3
        "Function_4_839",          # 04, 4
        "Function_5_864",          # 05, 5
        "Function_6_88F",          # 06, 6
        "Function_7_A1D",          # 07, 7
        "Function_8_BAB",          # 08, 8
        "Function_9_BAF",          # 09, 9
        "Function_10_1343",        # 0A, 10
        "Function_11_1ADF",        # 0B, 11
        "Function_12_25DF",        # 0C, 12
        "Function_13_25E3",        # 0D, 13
        "Function_14_2FBF",        # 0E, 14
        "Function_15_310E",        # 0F, 15
        "Function_16_3112",        # 10, 16
        "Function_17_40EE",        # 11, 17
        "Function_18_4344",        # 12, 18
        "Function_19_44B5",        # 13, 19
        "Function_20_4609",        # 14, 20
        "Function_21_4693",        # 15, 21
        "Function_22_46FC",        # 16, 22
        "Function_23_4875",        # 17, 23
        "Function_24_49F6",        # 18, 24
        "Function_25_4A4E",        # 19, 25
        "Function_26_4BA9",        # 1A, 26
        "Function_27_4D2D",        # 1B, 27
        "Function_28_4D8E",        # 1C, 28
        "Function_29_4E23",        # 1D, 29
        "Function_30_4E61",        # 1E, 30
        "Function_31_4E93",        # 1F, 31
        "Function_32_4FFD",        # 20, 32
        "Function_33_515B",        # 21, 33
        "Function_34_5174",        # 22, 34
        "Function_35_51DC",        # 23, 35
        "Function_36_54DE",        # 24, 36
        "Function_37_550C",        # 25, 37
        "Function_38_555B",        # 26, 38
        "Function_39_5658",        # 27, 39
        "Function_40_5752",        # 28, 40
        "Function_41_57BB",        # 29, 41
        "Function_42_5851",        # 2A, 42
        "Function_43_5EA0",        # 2B, 43
        "Function_44_74A3",        # 2C, 44
        "Function_45_833C",        # 2D, 45
    ))


    def Function_0_630(): pass

    label("Function_0_630")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_670"),
        (1, "loc_67C"),
        (2, "loc_688"),
        (3, "loc_694"),
        (4, "loc_6A0"),
        (5, "loc_6AC"),
        (6, "loc_6B8"),
        (SWITCH_DEFAULT, "loc_6C4"),
    )


    label("loc_670")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_67C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_688")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_694")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6E7")

    Return()

    # Function_0_630 end

    def Function_1_6E8(): pass

    label("Function_1_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_784")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    Jump("Function_1_6E8")

    label("loc_784")

    Return()

    # Function_1_6E8 end

    def Function_2_785(): pass

    label("Function_2_785")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_80D")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_2_785")

    label("loc_80D")

    Return()

    # Function_2_785 end

    def Function_3_80E(): pass

    label("Function_3_80E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_838")
    OP_94(0xFE, 0xFFFFFC5E, 0x12A2, 0x1194, 0x1E8C, 0x3E8)
    Sleep(300)
    Jump("Function_3_80E")

    label("loc_838")

    Return()

    # Function_3_80E end

    def Function_4_839(): pass

    label("Function_4_839")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_863")
    OP_94(0xFE, 0xFFFE8D6A, 0xFFFFF0EC, 0xFFFE9A8A, 0xFFFFFB46, 0x3E8)
    Sleep(400)
    Jump("Function_4_839")

    label("loc_863")

    Return()

    # Function_4_839 end

    def Function_5_864(): pass

    label("Function_5_864")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88E")
    OP_94(0xFE, 0xFFFD9E1E, 0x32, 0xFFFDAD46, 0xBE0, 0x3E8)
    Sleep(300)
    Jump("Function_5_864")

    label("loc_88E")

    Return()

    # Function_5_864 end

    def Function_6_88F(): pass

    label("Function_6_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8B7")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_A04")

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8D5")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_A04")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8F9")
    ClearChrFlags(0x1C, 0x80)
    BeginChrThread(0x1C, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_A04")

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_92C")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x9, -110, 0, 1840, 180)
    SetChrFlags(0x9, 0x10)
    Jump("loc_A04")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_94F")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_A04")

    label("loc_94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_96D")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_A04")

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9D7")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x9, -6660, 0, -4750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9B1")
    ClearChrFlags(0x2A, 0x80)

    label("loc_9B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D2")
    Event(0, 42)

    label("loc_9D2")

    Jump("loc_A04")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9F0")
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_A04")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A04")
    ClearChrFlags(0xF, 0x80)
    BeginChrThread(0x9, 0, 0, 1)

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1C")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x80)

    label("loc_A1C")

    Return()

    # Function_6_88F end

    def Function_7_A1D(): pass

    label("Function_7_A1D")

    OP_70(0x7, 0x8C)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x8, 0x4)
    OP_78(0x4, 0x24)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A76")
    Jump("loc_BAA")

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A84")
    Jump("loc_BAA")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A92")
    Jump("loc_BAA")

    label("loc_A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_ABF")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    Jump("loc_BAA")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AF7")
    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x24, 5500, 0, 0, 0)
    OP_D3(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_BAA")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B05")
    Jump("loc_BAA")

    label("loc_B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B7A")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x24, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x24, 2840, 0, 5360, 0)
    OP_78(0x5, 0x27)
    ClearMapObjFlags(0x5, 0x4)
    OP_D3(0x27, 0x0, 0x15F90, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B75")
    OP_66(0x3, 0x1)

    label("loc_B75")

    Jump("loc_BAA")

    label("loc_B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BA1")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_BAA")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BAA")

    label("loc_BAA")

    Return()

    # Function_7_A1D end

    def Function_8_BAB(): pass

    label("Function_8_BAB")

    Call(0, 9)
    Return()

    # Function_8_BAB end

    def Function_9_BAF(): pass

    label("Function_9_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC5")
    TalkBegin(0x16)
    Jump("loc_BC8")

    label("loc_BC5")

    TalkBegin(0x8)

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C86")

    #C0001
    ChrTalk(
        0x8,
        (
            "虽然也会有各种困扰……\x01",
            "但这个接待处的工作同样是\x01",
            "警备队的重要任务之一呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "既然负责了这个工作，\x01",
            "就要努力完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "尽管这份工作很普通，但我觉得它很重要。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CF8")

    label("loc_C86")


    #C0004
    ChrTalk(
        0x8,
        (
            "为警备队出力，却得不到任何回报\x01",
            "的时候虽然也有不少……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "不过，既然现在负责了这份工作，\x01",
            "就一定要努力做好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF8")

    Jump("loc_1329")

    label("loc_CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D72")

    #C0006
    ChrTalk(
        0x8,
        "那么，今天也要好好接待来客啊。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "……我如今是否已成为刚入队的时候\x01",
            "所憧憬的那种警备队员了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1329")

    label("loc_D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E18")

    #C0008
    ChrTalk(
        0x8,
        (
            "由驻守贝尔加德门的警备队员\x01",
            "所负责的遗迹调查工作草草收场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "虽然选择适当的时机撤退，也是司令的工作。\x01",
            "不过，他这次的态度只能说是消极懈怠了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1329")

    label("loc_E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EA3")

    #C0010
    ChrTalk(
        0x8,
        (
            "回国的游客还在不断增加……\x01",
            "哎呀呀，今天能不能处理完呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "难得的纪念庆典，\x01",
            "我却不得不待在这个破地方，\x01",
            "还真是可怜啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1329")

    label("loc_EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F2F")
    OP_4B(0x8, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0012
    ChrTalk(
        0x8,
        "您好，出国手续已经办完了。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "我们这就将大门打开，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x16,
        (
            "嗯，是吗，\x01",
            "那我赶紧叫妻子过来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_1329")

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCC")

    #C0015
    ChrTalk(
        0x8,
        (
            "呼……\x01",
            "高峰期差不多也过去了吧。\x01",
            "真是相当忙碌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "虽然听说帝国人的性格\x01",
            "大多都质朴刚毅……\x01",
            "但喜欢庆典的人似乎也非常多呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1012")

    label("loc_FCC")


    #C0017
    ChrTalk(
        0x8,
        (
            "毕竟是难得的纪念庆典，\x01",
            "希望帝国和共和国的人\x01",
            "也都好好享受一下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1012")

    Jump("loc_1329")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1105")

    #C0018
    ChrTalk(
        0x8,
        (
            "哎呀，真忙啊。\x01",
            "总算把那个长蛇般的队伍接待完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "今年走陆路的旅客真是不少啊。\x01",
            "选择乘坐列车的话，\x01",
            "明明能更加轻松地直达市内呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "……算啦，毕竟是难得的庆典，\x01",
            "大家可能都想体验一下\x01",
            "与往日不同的感觉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11A3")

    label("loc_1105")


    #C0021
    ChrTalk(
        0x8,
        (
            "今年走陆路的旅客真是不少啊。\x01",
            "选择乘坐列车的话，\x01",
            "明明能更加轻松地直达市内呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "……算啦，毕竟是难得的庆典，\x01",
            "大家可能都想体验一下\x01",
            "与往日不同的感觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A3")

    Jump("loc_1329")

    label("loc_11A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_128A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1234")

    #C0023
    ChrTalk(
        0x8,
        "几乎都没有前往帝国那边的巴士呢。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "因为帝国全境都铺设着铁路网。\x01",
            "来克洛斯贝尔的话，也是选择铁路更加便利。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1285")

    label("loc_1234")


    #C0025
    ChrTalk(
        0x8,
        "几乎都没有前往帝国那边的巴士呢。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "只有仅限纪念庆典期间\x01",
            "特别开通的专线。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1285")

    Jump("loc_1329")

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1329")

    #C0027
    ChrTalk(
        0x8,
        (
            "越过这道护栏的话，\x01",
            "对面就是帝国的国境了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "……既没有厚重的铁门也没有坚固的墙壁，\x01",
            "就靠这种破护栏来做屏障。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "真是一点都靠不住，太好笑了。\x02",
    )

    CloseMessageWindow()

    label("loc_1329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133F")
    TalkEnd(0x16)
    Jump("loc_1342")

    label("loc_133F")

    TalkEnd(0x8)

    label("loc_1342")

    Return()

    # Function_9_BAF end

    def Function_10_1343(): pass

    label("Function_10_1343")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_152C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1484")

    #C0030
    ChrTalk(
        0xFE,
        (
            "偷偷告诉你……\x01",
            "我可是盯上了警备队司令的位子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "与那种完全不懂得体会\x01",
            "部下心情的家伙相比，\x01",
            "我有自信能干得更加出色呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0300F嗯……司令也就算了，\x01",
            "但想超越准尉和副司令的话，\x01",
            "似乎没那么容易哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "…………呃。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "也对啊，我光把焦点\x01",
            "放在司令这个职位上……\x01",
            "都没有想到这些呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1527")

    label("loc_1484")


    #C0035
    ChrTalk(
        0xFE,
        (
            "总有一天，我一定\x01",
            "要当上统率这支警备队的司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "就算是索妮亚副司令……\x01",
            "我、我也会努力超越她的！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#0306F……以你现在的样子来看，\x01",
            "恐怕要花上很长时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1527")

    Jump("loc_1ADB")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_15A6")

    #C0038
    ChrTalk(
        0xFE,
        (
            "是吗……你们已经调查过\x01",
            "那个遗迹了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "可恶，如果我是司令的话，\x01",
            "绝不会下达让部队撤退的命令……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADB")

    label("loc_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1659")

    #C0040
    ChrTalk(
        0xFE,
        "虽然是为进行调查而去了那个遗迹……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "但那里绝非寻常之地，\x01",
            "老实说，根本就不是个能调查的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        (
            "#0501F……看来，那个地方\x01",
            "果然存在着什么呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16CD")

    label("loc_1659")


    #C0043
    ChrTalk(
        0xFE,
        (
            "那个遗迹给人一种毛骨悚然的感觉，\x01",
            "用语言很难表达清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "总之，绝非寻常之地……\x01",
            "你们自己到那里看看就知道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CD")

    Jump("loc_1ADB")

    label("loc_16D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1711")

    #C0045
    ChrTalk(
        0xFE,
        (
            "……似乎没有禁止出口的东西，\x01",
            "货物没有问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADB")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1739")

    #C0046
    ChrTalk(
        0xFE,
        "真是热闹起来了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADB")

    label("loc_1739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_175F")

    #C0047
    ChrTalk(
        0xFE,
        "今天没有发现异常。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADB")

    label("loc_175F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_180A")

    #C0048
    ChrTalk(
        0xFE,
        (
            "从昨天到今天，\x01",
            "入境的游客数量相当多……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "肯定也有谍报人员\x01",
            "混在人群之中，\x01",
            "潜入克洛斯贝尔了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "这也是无可奈何的——只能用这句话糊弄过去了吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADB")

    label("loc_180A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_198C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E8")

    #C0051
    ChrTalk(
        0xFE,
        (
            "虽然从表面上看，出入此门的人\x01",
            "都会受到一定程度的盘查。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "但是也可以乘坐列车进入克洛斯贝尔，\x01",
            "而车站那边并不会进行相关检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "所以，帝国与共和国的谍报人员\x01",
            "如今根本就处于随意进出的状态。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1987")

    label("loc_18E8")


    #C0054
    ChrTalk(
        0xFE,
        (
            "如今现状就是帝国与共和国的\x01",
            "谍报人员完全可以随意进出克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "我们在这里所做的盘查工作，\x01",
            "说得直白一点，其实只是给\x01",
            "克洛斯贝尔的市民做个样子看而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1987")

    Jump("loc_1ADB")

    label("loc_198C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1ADB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A55")

    #C0056
    ChrTalk(
        0xFE,
        (
            "按照自治州的法律，这里是不能像\x01",
            "其它国家那样拥有军队的。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "这是为了避免被帝国或共和国视为眼中钉，\x01",
            "从而引发争端。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "所以，从名义上说，\x01",
            "我们只能叫做\x01",
            "『警备队』而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ADB")

    label("loc_1A55")


    #C0059
    ChrTalk(
        0xFE,
        (
            "……不过还是要说清楚。尽管只是警备队，\x01",
            "但我们也都是经受过严格训练的精英成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "如今这种只能自卫的现状，\x01",
            "实在是让人很焦急呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADB")

    TalkEnd(0xFE)
    Return()

    # Function_10_1343 end

    def Function_11_1ADF(): pass

    label("Function_11_1ADF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B73")
    Jump("loc_1BBD")

    label("loc_1B73")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B93")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BBD")

    label("loc_1B93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BB3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BBD")

    label("loc_1BB3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BBD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC6")

    #C0061
    ChrTalk(
        0xFE,
        (
            "我向史黛拉小姐表白之后，\x01",
            "她竟然同意了呢，真不敢相信。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……但是，\x01",
            "她的回答也只是\x01",
            "『先交往一段时间试试吧』而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "不过我还是很高兴啦……\x01",
            "但总感觉，我们的关系\x01",
            "似乎稳定在了一个微妙的程度……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D58")

    label("loc_1CC6")


    #C0064
    ChrTalk(
        0xFE,
        (
            "……算啦，就算只是尝试交往也没关系，\x01",
            "毕竟史黛拉小姐还是愿意接受我， \x01",
            "这是毫无疑问的，嗯。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "现在开始，必须要继续加油，\x01",
            "让她喜欢上我才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D58")

    Jump("loc_25D7")

    label("loc_1D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E21")

    #C0066
    ChrTalk(
        0xFE,
        (
            "……决定了。\x01",
            "今天的工作结束之后，\x01",
            "我就要向史黛拉小姐表白！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#0309F很好，鼓起勇气吧，撞个头破血流也没关系！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "……我可不想头破血流，\x01",
            "你别说这么不吉利的话啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E9C")

    label("loc_1E21")


    #C0069
    ChrTalk(
        0xFE,
        (
            "约史黛拉小姐出来的话，\x01",
            "去哪里比较好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "纪念庆典已经结束了，\x01",
            "米修拉姆应该比较清静了吧，\x01",
            "去那里或许是个好选择。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9C")

    Jump("loc_25D7")

    label("loc_1EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F2A")

    #C0071
    ChrTalk(
        0xFE,
        (
            "纪念庆典结束了，\x01",
            "史黛拉小姐的工作也开始闲下来了……\x01",
            "哎呀，真棒……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……光是这样远远看着她，\x01",
            "果然还是不够啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D7")

    label("loc_1F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FAD")

    #C0073
    ChrTalk(
        0xFE,
        (
            "今天忙得四脚朝天，\x01",
            "连偷偷看看史黛拉小姐\x01",
            "的时间都没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "不过，饿着肚子可没法上战场。\x01",
            "我还是先把肚子填饱吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D7")

    label("loc_1FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2076")

    #C0075
    ChrTalk(
        0xFE,
        (
            "……史黛拉小姐……\x01",
            "昨天也给我们买来了慰问品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "虽然是分给所有队员的，但我已经很满足了。\x01",
            "我好像已经被她的温柔\x01",
            "深深打动了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "史黛拉小姐……\x01",
            "温柔的你最美了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_209D")

    label("loc_2076")


    #C0078
    ChrTalk(
        0xFE,
        (
            "史黛拉小姐……\x01",
            "温柔的你最美了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209D")

    Jump("loc_25D7")

    label("loc_20A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2187")

    #C0079
    ChrTalk(
        0xFE,
        (
            "史黛拉小姐昨天来慰问我们，\x01",
            "还送来了水果呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "难道这就是常见的\x01",
            "『前辈，加油⊥』之类的\x01",
            "暗示吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        (
            "#0306F……我觉得是你想多了，\x01",
            "那只不过是送给全体队员的慰问品啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "不要打破我的幻想啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21F1")

    label("loc_2187")


    #C0083
    ChrTalk(
        0xFE,
        (
            "呼……总之，史黛拉小姐是个\x01",
            "很体贴的女孩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "那么，这饱含了爱意的慰问品……\x01",
            "就让我来好好品尝吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F1")

    Jump("loc_25D7")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_226C")

    #C0085
    ChrTalk(
        0xFE,
        (
            "越是忙碌，就越是闪耀出光辉，\x01",
            "史黛拉小姐……真美啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "好，吃完饭以后，\x01",
            "我也必须要开始努力了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D7")

    label("loc_226C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2301")

    #C0087
    ChrTalk(
        0xFE,
        (
            "我们这个国境门，由于那个司令的缘故，\x01",
            "气氛总有些不好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "在这种环境下，\x01",
            "史黛拉小姐那开朗明快的言谈举止，\x01",
            "让人觉得非常舒畅呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D7")

    label("loc_2301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_25D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F5")

    #C0089
    ChrTalk(
        0xFE,
        (
            "史黛拉小姐……真可爱啊，\x01",
            "真希望能和她更加亲近呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "兰迪，如今你已经不在这里了……\x01",
            "我是不会把史黛拉小姐让给你的！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#0309F哈哈哈，\x01",
            "这是什么话啊，前辈。\x02\x03",

            "在我进警备队之前，你就已经在了，\x01",
            "但却从没做出过任何\x01",
            "向她示好的举动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "呃呃……\x01",
            "因为我要花很多时间\x01",
            "来准备迂回战术嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        "#0309F哈哈，总之，请加油吧。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0005F（兰迪……\x01",
            "  好像和警备队的人\x01",
            "  相处得非常好呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#0100F（嗯……之前听说他是因为\x01",
            "  女性问题而离职的，\x01",
            "  还以为会和同伴们关系紧张呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25D7")

    label("loc_24F5")


    #C0096
    ChrTalk(
        0xFE,
        (
            "当我最大的情敌兰迪还在这里的时候，\x01",
            "我向史黛拉小姐搭话的机会\x01",
            "不知被他抢走了多少次……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "但是，现在你已经离开了！\x01",
            "这正是我接近史黛拉小姐\x01",
            "的最佳时机！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#0303F（我和史黛拉也只是\x01",
            "  随便～地聊聊天而已嘛。\x01",
            "  呵，算了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1ADF end

    def Function_12_25DF(): pass

    label("Function_12_25DF")

    Call(0, 13)
    Return()

    # Function_12_25DF end

    def Function_13_25E3(): pass

    label("Function_13_25E3")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_260E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_260E")
    Call(0, 44)
    Return()

    label("loc_260E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FBB")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2668")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2668")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2688")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FB6")

    label("loc_2688")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_269C")
    Jump("loc_2FB6")

    label("loc_269C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2800")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D1")
    Call(0, 14)
    Jump("loc_27FB")

    label("loc_26D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278F")

    #C0099
    ChrTalk(
        0xB,
        (
            "昨天晚上，\x01",
            "库雷斯先生对我说——\x01",
            "『可以和我交往吗』。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "虽然我对库雷斯先生\x01",
            "并没有什么特殊的感觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "不过，也许以后会慢慢产生兴趣呢，\x01",
            "所以我就答应和他试着交往。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27FB")

    label("loc_278F")


    #C0102
    ChrTalk(
        0xB,
        (
            "虽然我答应与库雷斯先生\x01",
            "试着交往一段时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "但他好像有些失落呢。\x01",
            "……嗯，真是不太容易理解的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FB")

    Jump("loc_2FB6")

    label("loc_2800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_289B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281C")
    Call(0, 14)
    Jump("loc_2896")

    label("loc_281C")


    #C0104
    ChrTalk(
        0xB,
        (
            "来这个国境门的路上，\x01",
            "有一个分岔路口吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "顺着那条岔路继续走，有个警察学校。\x01",
            "那里也是由贝尔加德门的队员在守卫呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2896")

    Jump("loc_2FB6")

    label("loc_289B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_291A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B7")
    Call(0, 14)
    Jump("loc_2915")

    label("loc_28B7")


    #C0106
    ChrTalk(
        0xB,
        "欢迎光临，要吃点什么吗？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xB,
        (
            "因为随时都有可能\x01",
            "紧急出动，\x01",
            "所以吃饭的时候一定要好好吃饱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2915")

    Jump("loc_2FB6")

    label("loc_291A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_298F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2936")
    Call(0, 14)
    Jump("loc_298A")

    label("loc_2936")


    #C0108
    ChrTalk(
        0xB,
        (
            "哎呀，今天可\x01",
            "真是忙得不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "嗯，看来今天没有时间\x01",
            "去给队员们送慰问品了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298A")

    Jump("loc_2FB6")

    label("loc_298F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A1F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AB")
    Call(0, 14)
    Jump("loc_2A1A")

    label("loc_29AB")


    #C0110
    ChrTalk(
        0xB,
        (
            "库雷斯先生好像\x01",
            "从昨天开始就有点奇怪呢。\x01",
            "一直冲着我傻笑……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "除了桃子之外，\x01",
            "要不要再送去一点炸肉排呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1A")

    Jump("loc_2FB6")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3B")
    Call(0, 14)
    Jump("loc_2B43")

    label("loc_2A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEF")

    #C0112
    ChrTalk(
        0xB,
        (
            "我昨天去慰问队员们，\x01",
            "给他们送去了水果，\x01",
            "结果他们非常感激呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "啊哈，虽然不太习惯这种事，\x01",
            "但偶尔也还是要做呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "因为这有可能关系到\x01",
            "下个月的营业额哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B43")

    label("loc_2AEF")


    #C0115
    ChrTalk(
        0xB,
        (
            "至少在纪念庆典期间，\x01",
            "一定要办些派送活动才行。\x01",
            "只是切点水果的话，既简单又省力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B43")

    Jump("loc_2FB6")

    label("loc_2B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2DC4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B64")
    Call(0, 14)
    Jump("loc_2DBF")

    label("loc_2B64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7F")

    #C0116
    ChrTalk(
        0xB,
        (
            "呼，工作结束啦。\x01",
            "身体虽然很疲劳，但感觉很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "队员们也都很累了吧，\x01",
            "我去给他们送些慰问品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        (
            "#0309F哦，真好啊，\x01",
            "也送给我一点慰问品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xB,
        (
            "不～行。\x01",
            "兰迪你已经不是\x01",
            "警备队的成员了哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        "还是老老实实地点单付账吧。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        "#0303F真小气。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CED")

    label("loc_2C7F")


    #C0122
    ChrTalk(
        0xB,
        (
            "嗯，给队员们送慰问品的话，\x01",
            "选什么比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "水果之类的，比较有助于消除疲劳吧。\x01",
            "好，就这么决定了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CED")

    Jump("loc_2DBF")

    label("loc_2CF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2D5F")

    #C0124
    ChrTalk(
        0xB,
        (
            "我虽然不太清楚\x01",
            "那个启动钥匙\x01",
            "有多重要……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "但就算是为了准尉，\x01",
            "也请努力帮她找到哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2D5F")


    #C0126
    ChrTalk(
        0xB,
        (
            "昨天半夜，因为司令任性的要求，\x01",
            "害我不得不加班了呢，\x01",
            "到现在都还很疲惫。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        "呼，好忙好忙。\x02",
    )

    CloseMessageWindow()

    label("loc_2DBF")

    Jump("loc_2FB6")

    label("loc_2DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE0")
    Call(0, 14)
    Jump("loc_2E3E")

    label("loc_2DE0")


    #C0128
    ChrTalk(
        0xB,
        (
            "您好，欢迎光临。\x01",
            "请随意点些喜欢的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "话虽如此，其实这里\x01",
            "可供选择的东西也不多啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3E")

    Jump("loc_2FB6")

    label("loc_2E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F46")

    #C0130
    ChrTalk(
        0xB,
        "欢迎光……嗯？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "仔细一看，这不是兰迪嘛。\x01",
            "啊哈，好久不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0300F哟，你还是老样子啊，史黛拉。\x01",
            "一切都还好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "我还想问你呢，你现在是在……特别任务支援科？\x01",
            "工作肯定很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "好啦，别光顾着寒暄，\x01",
            "先吃点什么吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 6)
    Jump("loc_2FB6")

    label("loc_2F46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F59")
    Call(0, 14)
    Jump("loc_2FB6")

    label("loc_2F59")


    #C0135
    ChrTalk(
        0xB,
        (
            "别光顾着寒暄，\x01",
            "先吃点什么吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "不过，事先声明，\x01",
            "我们这里可没有给熟人\x01",
            "打折的规矩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB6")

    Jump("loc_2618")

    label("loc_2FBB")

    TalkEnd(0xB)
    Return()

    # Function_13_25E3 end

    def Function_14_2FBF(): pass

    label("Function_14_2FBF")


    #C0137
    ChrTalk(
        0xB,
        (
            "我想让队员们好好\x01",
            "补充体力，\x01",
            "所以举办过肉火锅大会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "真是的，还没等我下筷子，\x01",
            "肉就快被他们吃光了……\x01",
            "从事体力劳动的话，肚子果然特别容易饿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "你们要不要也办一场肉火锅大会呢？\x01",
            "想学的话，我可以教你们火锅的做法哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '大饱口福锅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '大饱口福锅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x6)
    Return()

    # Function_14_2FBF end

    def Function_15_310E(): pass

    label("Function_15_310E")

    Call(0, 16)
    Return()

    # Function_15_310E end

    def Function_16_3112(): pass

    label("Function_16_3112")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_311F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40EA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_316F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_316F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318F")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40E5")

    label("loc_318F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31A3")
    Jump("loc_40E5")

    label("loc_31A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_333B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B2")

    #C0142
    ChrTalk(
        0xC,
        (
            "如果是为了自己的利益，司令随时都有可能\x01",
            "把警备队员们弃之不顾吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        (
            "对于警备队来说，现在最需要的\x01",
            "就是一个能关怀下属的好上司了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32AA")

    #C0144
    ChrTalk(
        0x10A,
        (
            "#0603F的确……\x02\x03",

            "#0601F可恶，想想就生气。\x01",
            "警察高层的那些混蛋……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AA")

    SetScenarioFlags(0x0, 4)
    Jump("loc_3336")

    label("loc_32B2")


    #C0145
    ChrTalk(
        0xC,
        (
            "如果是为了自己的利益，司令随时都有可能\x01",
            "把警备队员们弃之不顾吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        (
            "只要有个关怀部下的好上司，\x01",
            "警备队该是一个多好的地方啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3336")

    Jump("loc_40E5")

    label("loc_333B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3450")

    #C0147
    ChrTalk(
        0xC,
        (
            "在缔结了《互不侵犯条约》之后，\x01",
            "克洛斯贝尔的人们过上了安心的生活……\x01",
            "但是，真的就可以彻底放心了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xC,
        (
            "抵御帝国与共和国的防线\x01",
            "就只有一道破护栏而已，\x01",
            "在我看来，无论如何也都无法安心。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xC,
        (
            "如果帝国或共和国\x01",
            "真的有意进攻，\x01",
            "随时都可以轻松打过来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_34E5")

    label("loc_3450")


    #C0150
    ChrTalk(
        0xC,
        (
            "单凭一份《互不侵犯条约》，\x01",
            "真的就能让克洛斯贝尔维持和平吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xC,
        (
            "抵御帝国与共和国的防线\x01",
            "就只有一道破护栏而已，\x01",
            "在我看来，无论如何也都无法安心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E5")

    Jump("loc_40E5")

    label("loc_34EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C6")

    #C0152
    ChrTalk(
        0xC,
        (
            "虽然经常被人误解，\x01",
            "但其实像我这样的军事迷\x01",
            "并不喜欢战争。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xC,
        (
            "说到底，我们也只是喜欢\x01",
            "欣赏军事装备的精妙设计，\x01",
            "沉醉于机械方面的美感。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "请不要把我们与那些\x01",
            "嗜好互相残杀的家伙们视为同类。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35FF")

    label("loc_35C6")


    #C0155
    ChrTalk(
        0xC,
        (
            "军事迷并不一定是\x01",
            "战争狂。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xC,
        "请不要把这两者搞混。\x02",
    )

    CloseMessageWindow()

    label("loc_35FF")

    Jump("loc_40E5")

    label("loc_3604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374F")

    #C0157
    ChrTalk(
        0xC,
        (
            "警备队的装甲车拥有\x01",
            "很高的机动性，非常易于操纵。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xC,
        (
            "不过，虽然单独来看尚算优秀，\x01",
            "但要是与其它国家的军备对比，\x01",
            "它就明显差得远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "帝国有强大的列车炮，\x01",
            "那个导力技术先进的国家利贝尔\x01",
            "则拥有名叫『埃尔赛尤』的高速飞行船。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        (
            "面对那些强力的载人兵器，克洛斯贝尔\x01",
            "完全没有任何对抗手段，这是个致命伤。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_380D")

    label("loc_374F")


    #C0161
    ChrTalk(
        0xC,
        (
            "不管拥有多么优秀的武器，\x01",
            "一旦遭到飞行船的轰炸，也就无力回天了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        (
            "警备队的装备可以说\x01",
            "实在是很落后啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "但考虑到克洛斯贝尔的特殊情况，\x01",
            "无法拥有强大的军事配备\x01",
            "也是没有办法的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_380D")

    Jump("loc_40E5")

    label("loc_3812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_396A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F8")

    #C0164
    ChrTalk(
        0xC,
        (
            "最近运到的便携干粮……\x01",
            "我向史黛拉小姐偷偷要到了一点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "唉，那可真是难吃死了。\x01",
            "虽然听说它很有营养……\x01",
            "但我可不想再吃第二次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "队员们每次进行\x01",
            "野外演习的时候都要吃那个，\x01",
            "真是很同情他们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3965")

    label("loc_38F8")


    #C0167
    ChrTalk(
        0xC,
        (
            "话说回来，那个便携干粮\x01",
            "真是难吃得要死啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xC,
        (
            "虽然营养也很重要，\x01",
            "但对食物来说，味道不是\x01",
            "更重要的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3965")

    Jump("loc_40E5")

    label("loc_396A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A72")

    #C0169
    ChrTalk(
        0xC,
        (
            "警备队的队员们\x01",
            "经常抱怨司令呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        (
            "其实，我也很讨厌那个人。\x01",
            "因为他总是乱摆架子。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "哪怕他会使用任何一种武器，\x01",
            "评价也都不至于这么不堪呢。\x01",
            "但他就只会坐在高位上下命令而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0006F这、这个……\x01",
            "但司令的工作本来就是这样的吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B0D")

    label("loc_3A72")


    #C0173
    ChrTalk(
        0xC,
        (
            "总而言之……那家伙只会下命令，\x01",
            "却连一种武器都不会使用，\x01",
            "根本就不是一个合格的警备队首领。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "大家都对司令抱有很强烈的不满，\x01",
            "这种心情，我也很理解呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0D")

    Jump("loc_40E5")

    label("loc_3B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3DBC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1B")

    #C0175
    ChrTalk(
        0xC,
        (
            "说起纪念庆典，\x01",
            "如果是在帝国那边举办的话，\x01",
            "肯定会有军队的表演活动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "比如阅兵游行，或是公开演习之类的……\x01",
            "便携干粮的试吃会\x01",
            "也很让人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "还能加深军民之间的情谊……\x01",
            "哎呀，我们警备队\x01",
            "也应该举办这样的活动嘛……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3C9E")

    label("loc_3C1B")


    #C0178
    ChrTalk(
        0xC,
        (
            "贝尔加德门的警备队\x01",
            "也应该举办些活动呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xC,
        (
            "……算啦，毕竟有那种司令在。\x01",
            "就算我提出意见也没用，\x01",
            "他肯定会一句话就否决掉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C9E")

    Jump("loc_3DB7")

    label("loc_3CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3D5C")

    #C0180
    ChrTalk(
        0xC,
        (
            "昨晚，我和正要上屋顶\x01",
            "的司令擦身而过。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xC,
        (
            "他拿着一个像是钥匙链的东西，\x01",
            "还套在手指上甩来甩去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "现在一想，我当时看到的应该就是\x01",
            "那个叫什么启动钥匙的东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DB7")

    label("loc_3D5C")


    #C0183
    ChrTalk(
        0xC,
        (
            "嗯，再怎么说，\x01",
            "应该也不会掉在\x01",
            "柜台下面吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xC,
        (
            "……哎呀，是客人吗？\x01",
            "请随意参观吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB7")

    Jump("loc_40E5")

    label("loc_3DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3FBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F20")

    #C0185
    ChrTalk(
        0xC,
        (
            "警备队的武装主要\x01",
            "包括两种。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "有近身作战用的\x01",
            "冲击斧枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "还有远距离作战用的\x01",
            "来复枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "熟练掌握两者的使用方法，\x01",
            "是身为警备队员的必要条件。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xC,
        (
            "……说起来，兰迪前辈\x01",
            "使用冲击斧枪的技巧被\x01",
            "私下评为警备队第一呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#0300F……哈哈，过去的事情\x01",
            "就不必再提啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xC,
        (
            "哎呀，演习的时候可真是\x01",
            "让我开了眼界呢。\x01",
            "实在厉害……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FB5")

    label("loc_3F20")


    #C0192
    ChrTalk(
        0xC,
        (
            "冲击斧枪和\x01",
            "来复枪……\x01",
            "两者都是很难掌握，但却威力强大的装备。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xC,
        (
            "尤其是冲击斧枪的运用，\x01",
            "兰迪前辈的技巧可是无人能出其右的。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xC,
        "真是厉害啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3FB5")

    Jump("loc_40E5")

    label("loc_3FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_40E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406C")

    #C0195
    ChrTalk(
        0xC,
        (
            "我是个军事迷，\x01",
            "特别喜欢欣赏军人、武器和战车。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "但是，警备队为了不刺激到\x01",
            "帝国和共和国，\x01",
            "特意限制了大规模的演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xC,
        "哎呀……真是遗憾至极啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40E5")

    label("loc_406C")


    #C0198
    ChrTalk(
        0xC,
        (
            "……不过，尽管如此，\x01",
            "平时的演习也还是\x01",
            "能让人看得很尽兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        (
            "但我还是更想欣赏用上\x01",
            "装甲车与导力炮的大规模演习呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E5")

    Jump("loc_311F")

    label("loc_40EA")

    TalkEnd(0xC)
    Return()

    # Function_16_3112 end

    def Function_17_40EE(): pass

    label("Function_17_40EE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4182")
    Jump("loc_41CC")

    label("loc_4182")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41CC")

    label("loc_41A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41C2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41CC")

    label("loc_41C2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41CC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_433C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F7")

    #C0200
    ChrTalk(
        0xFE,
        (
            "有情报说，在昨天夜晚，\x01",
            "警备队的司令曾与疑似黑手党的黑衣人\x01",
            "进行过秘密会面。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "因为此事与之前发生的\x01",
            "争斗骚乱事件间隔不久，\x01",
            "所以稍微有些在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "不过，那个司令已经出门了。\x01",
            "看来是无法对他进行调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        "哎，白跑了一趟呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_433C")

    label("loc_42F7")


    #C0204
    ChrTalk(
        0xFE,
        "哎，白跑了一趟呢……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "没办法，差不多也该\x01",
            "回克洛斯贝尔市了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_433C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_40EE end

    def Function_18_4344(): pass

    label("Function_18_4344")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43D8")
    Jump("loc_4422")

    label("loc_43D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4422")

    label("loc_43F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4418")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4422")

    label("loc_4418")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4422")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44AD")

    #C0206
    ChrTalk(
        0xFE,
        (
            "我经常会经过这个国境门……\x01",
            "但每次来，司令好像都不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "……我真是很同情警备队员啊。\x02",
    )

    CloseMessageWindow()

    label("loc_44AD")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_4344 end

    def Function_19_44B5(): pass

    label("Function_19_44B5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4549")
    Jump("loc_4593")

    label("loc_4549")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4569")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4593")

    label("loc_4569")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4589")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4593")

    label("loc_4589")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4593")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0208
    ChrTalk(
        0xFE,
        "（咀嚼）……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "比预定时刻提早到达了啊，\x01",
            "我正在吃零食打发时间呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_44B5 end

    def Function_20_4609(): pass

    label("Function_20_4609")

    TalkBegin(0xFE)

    #C0210
    ChrTalk(
        0xFE,
        (
            "经常乘导力车去帝国的话，\x01",
            "就觉得这里的检查好麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "呼，虽然乘坐巴士和列车\x01",
            "更加有效率，但还是觉得\x01",
            "私家车更适合商业谈判啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4609 end

    def Function_21_4693(): pass

    label("Function_21_4693")

    TalkBegin(0xFE)

    #C0212
    ChrTalk(
        0xFE,
        (
            "入境手续总算办好了。\x01",
            "排了那么长的队伍，真够受的。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "那么，赶快出发，\x01",
            "前往克洛斯贝尔市吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4693 end

    def Function_22_46FC(): pass

    label("Function_22_46FC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4790")
    Jump("loc_47DA")

    label("loc_4790")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_47B0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47DA")

    label("loc_47B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47D0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47DA")

    label("loc_47D0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47DA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0214
    ChrTalk(
        0xFE,
        (
            "我有些事情\x01",
            "要去米修拉姆。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "呵呵……反正是预定在庆典最终日过去，\x01",
            "在那之前，就好好享受一下纪念庆典吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_46FC end

    def Function_23_4875(): pass

    label("Function_23_4875")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4909")
    Jump("loc_4953")

    label("loc_4909")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4929")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4953")

    label("loc_4929")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4949")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4953")

    label("loc_4949")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4953")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0216
    ChrTalk(
        0xFE,
        (
            "我丈夫今年好像要带我去\x01",
            "一个非常好玩的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "哈哈哈，他好像很有自信的样子，\x01",
            "看来我也必须要好好期待一下啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_4875 end

    def Function_24_49F6(): pass

    label("Function_24_49F6")

    TalkBegin(0xFE)

    #C0218
    ChrTalk(
        0xFE,
        "哎呀……她跑到哪里去了？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "我明明说过要去买点小吃，\x01",
            "让她在这里等我的……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_49F6 end

    def Function_25_4A4E(): pass

    label("Function_25_4A4E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AE2")
    Jump("loc_4B2C")

    label("loc_4AE2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B02")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B2C")

    label("loc_4B02")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B22")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B2C")

    label("loc_4B22")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B2C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0220
    ChrTalk(
        0xFE,
        (
            "离巴士到站\x01",
            "似乎还有一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "肚子也开始饿了呢，\x01",
            "趁现在先吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_4A4E end

    def Function_26_4BA9(): pass

    label("Function_26_4BA9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C3D")
    Jump("loc_4C87")

    label("loc_4C3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C5D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C87")

    label("loc_4C5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C7D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C87")

    label("loc_4C7D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C87")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0222
    ChrTalk(
        0xFE,
        (
            "我在等丈夫\x01",
            "办理出国手续呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "虽然我很想再享受一下逛纪念庆典的乐趣……\x01",
            "但假期就截止到今天，\x01",
            "也只能打道回府了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_4BA9 end

    def Function_27_4D2D(): pass

    label("Function_27_4D2D")

    TalkBegin(0xFE)

    #C0224
    ChrTalk(
        0xFE,
        (
            "纪念庆典？不知道，不知道。\x01",
            "我只是来做买卖的。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "买卖做完之后，\x01",
            "我就得赶快回去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_4D2D end

    def Function_28_4D8E(): pass

    label("Function_28_4D8E")

    TalkBegin(0xFE)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0226
    ChrTalk(
        0x19,
        (
            "亲爱的，你就在这等我好吗？\x01",
            "我现在就去办理出国手续。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1A,
        "亲爱的，我知道啦⊥\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x1A,
        (
            "不过，我很讨厌等待，\x01",
            "你可要快点办好哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_28_4D8E end

    def Function_29_4E23(): pass

    label("Function_29_4E23")

    TalkBegin(0xFE)

    #C0229
    ChrTalk(
        0xFE,
        (
            "嗯，果然很花时间啊。\x01",
            "在夜晚之前过来，真是太对了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_4E23 end

    def Function_30_4E61(): pass

    label("Function_30_4E61")

    TalkBegin(0xFE)

    #C0230
    ChrTalk(
        0xFE,
        (
            "那个……\x01",
            "请问出国手续应该在哪里办理？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_4E61 end

    def Function_31_4E93(): pass

    label("Function_31_4E93")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F27")
    Jump("loc_4F71")

    label("loc_4F27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F71")

    label("loc_4F47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F71")

    label("loc_4F67")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F71")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0231
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "这是和警备队共用的食堂吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "虽然有些不适应，\x01",
            "但是肚子好饿，\x01",
            "就暂且忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_4E93 end

    def Function_32_4FFD(): pass

    label("Function_32_4FFD")

    TalkBegin(0xFE)
    OP_52(0x1F, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x1F, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5094")
    Jump("loc_50DE")

    label("loc_5094")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50B4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50DE")

    label("loc_50B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50D4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50DE")

    label("loc_50D4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50DE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1F, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0233
    ChrTalk(
        0xFE,
        "哈哈，你慢点吃啊。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "前往克洛斯贝尔市的巴士\x01",
            "还有很多趟呢，\x01",
            "不用着急的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_4FFD end

    def Function_33_515B(): pass

    label("Function_33_515B")

    TalkBegin(0xFE)

    #C0235
    ChrTalk(
        0xFE,
        "（咀嚼）……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_515B end

    def Function_34_5174(): pass

    label("Function_34_5174")

    TalkBegin(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "这次我收购到了\x01",
            "一大堆好东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "接下来，我打算立刻回帝国转卖，\x01",
            "好好赚上一笔。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_5174 end

    def Function_35_51DC(): pass

    label("Function_35_51DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5383")

    #C0238
    ChrTalk(
        0xFE,
        (
            "（呼噜呼噜）……\x01",
            "（吧唧吧唧）……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        "（嚼嚼嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        "…………呼啊。\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52CE")
    Jump("loc_5318")

    label("loc_52CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5318")

    label("loc_52EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_530E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5318")

    label("loc_530E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5318")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0241
    ChrTalk(
        0xFE,
        (
            "……有什么事吗？\x01",
            "别人正在吃饭的时候，\x01",
            "你不要紧盯着看啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54D6")

    label("loc_5383")


    #C0242
    ChrTalk(
        0xFE,
        "（咀嚼）……\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5429")
    Jump("loc_5473")

    label("loc_5429")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5449")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5473")

    label("loc_5449")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5469")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5473")

    label("loc_5469")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5473")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0243
    ChrTalk(
        0xFE,
        (
            "……有什么事吗？\x01",
            "别人正在吃饭的时候，\x01",
            "你不要紧盯着看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54D6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_51DC end

    def Function_36_54DE(): pass

    label("Function_36_54DE")

    TalkBegin(0xFE)

    #C0244
    ChrTalk(
        0xFE,
        (
            "那个蓝色的罩子……\x01",
            "真是很惹眼呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_54DE end

    def Function_37_550C(): pass

    label("Function_37_550C")

    TalkBegin(0xFE)

    #C0245
    ChrTalk(
        0xFE,
        (
            "好……赶快\x01",
            "出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "期待已久的纪念庆典，\x01",
            "一定要好好玩个够呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_550C end

    def Function_38_555B(): pass

    label("Function_38_555B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561A")
    TurnDirection(0xFE, 0x0, 0)

    #C0247
    ChrTalk(
        0xFE,
        (
            "兰迪，还有诸位，\x01",
            "这次真是谢谢大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "如果以后再有什么事情的话，\x01",
            "还要麻烦各位多多帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "那么，趁着游客\x01",
            "不多的时候，\x01",
            "要赶快把它移走才行……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    Jump("loc_5654")

    label("loc_561A")


    #C0250
    ChrTalk(
        0xFE,
        (
            "要抓住游客数量\x01",
            "稀少的时机，\x01",
            "赶快把装甲车移走才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5654")

    TalkEnd(0xFE)
    Return()

    # Function_38_555B end

    def Function_39_5658(): pass

    label("Function_39_5658")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D9")

    #C0251
    ChrTalk(
        0xFE,
        (
            "既然来观光旅游，\x01",
            "就一定要好好品尝\x01",
            "一下当地的特色料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔\x01",
            "能吃到什么美食呢，\x01",
            "真期待啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_574E")

    label("loc_56D9")


    #C0253
    ChrTalk(
        0xFE,
        (
            "我可称得上是美食家哦，\x01",
            "克洛斯贝尔究竟会有什么美食呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……一想到这点，\x01",
            "肚子就开始饿了呢，\x01",
            "点些什么来吃吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_574E")

    TalkEnd(0xFE)
    Return()

    # Function_39_5658 end

    def Function_40_5752(): pass

    label("Function_40_5752")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "前方是警备队专用货物路线\x01",
            "    无关人员不得入内\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_5752 end

    def Function_41_57BB(): pass

    label("Function_41_57BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_582A")

    #C0256
    ChrTalk(
        0xFE,
        (
            "好像是迷路了呢，\x01",
            "这里是什么地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "……嗯，算啦。\x01",
            "难得过来，就当是探险好了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_584D")

    label("loc_582A")


    #C0258
    ChrTalk(
        0xFE,
        (
            "迷路了也不要气馁～\x01",
            "探险探险！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_584D")

    TalkEnd(0xFE)
    Return()

    # Function_41_57BB end

    def Function_42_5851(): pass

    label("Function_42_5851")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-6540, 1000, 4160, 0)
    MoveCamera(314, 35, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(37720, 0)
    SetChrPos(0x101, 14000, 0, -2300, 270)
    SetChrPos(0x102, 15300, 0, -1200, 270)
    SetChrPos(0x103, 17900, 0, -1200, 270)
    SetChrPos(0x104, 16600, 0, -2300, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    OP_68(13390, 1000, 690, 8000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    SetChrFlags(0x9, 0x80)
    OP_68(11350, 1500, -3170, 0)
    MoveCamera(254, 22, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(17830, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_5985():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5985)

    def lambda_599F():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_599F)

    def lambda_59B9():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_59B9)

    def lambda_59D3():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_59D3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5A13():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A13)
    WaitChrThread(0x101, 1)

    #C0259
    ChrTalk(
        0x101,
        "#11P#0005F……这是什么东西啊？\x02",
    )

    CloseMessageWindow()

    def lambda_5A48():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A48)
    Sleep(100)

    def lambda_5A58():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A58)
    Sleep(100)

    def lambda_5A68():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A68)
    Sleep(100)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0260
    ChrTalk(
        0x104,
        (
            "#6P#0305F……嗯？原来好像\x01",
            "没有这种东西吧？\x02\x03",

            "#0309F让我看看……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5AC8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5AC8)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0261
    ChrTalk(
        0x102,
        "#11P#0105F……兰迪，怎么回事呢？\x02",
    )

    CloseMessageWindow()

    def lambda_5B24():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B24)
    WaitChrThread(0x104, 1)

    #C0262
    ChrTalk(
        0x104,
        "#6P#0301F这……看起来，像是警备队的装甲车呢。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#12P#0205F装甲车为何会停在这种地方……？\x02\x03",

            "而且还要盖上罩子来掩藏……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        (
            "#6P#0306F……说是掩藏，其实根本就藏不住嘛。\x02\x03",

            "不如说，盖上这种东西之后，\x01",
            "反而更加显眼了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#11P#0003F这么一说，贝尔加德门好像\x01",
            "发来了支援请求吧。\x02\x03",

            "#0001F或许正和这辆装甲车\x01",
            "有什么关系呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x103,
        (
            "#12P#0203F的确，是那项『搜索遗失物』的委托吧。\x02\x03",

            "#0200F委托人是……米蕾优准尉。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_END)), "loc_5D1D")

    #C0267
    ChrTalk(
        0x101,
        (
            "#11P#0005F米蕾优小姐是……\x01",
            "那位女士官吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        "#6P#0304F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DD4")

    label("loc_5D1D")


    #C0269
    ChrTalk(
        0x101,
        (
            "#11P#0005F米蕾优准尉……\x01",
            "兰迪，你认识她吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        (
            "#6P#0300F嗯，认识。\x01",
            "……是原来的同事呢。\x02\x03",

            "#0304F都已经是准尉了吗。我在警备队的时候，\x01",
            "她还只是个上士呢……\x01",
            "不知是什么时候升迁的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD4")


    #C0271
    ChrTalk(
        0x102,
        (
            "#12P#0100F米蕾优准尉现在也许很忙，\x01",
            "但我们还是\x01",
            "去见她一面吧。\x02\x03",

            "如果很在意那辆\x01",
            "装甲车的话，委婉地\x01",
            "问问她也好。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#11P#0000F……是啊。\x01",
            "好，那就去见她吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x0, 7260, 0, -2410, 192)
    OP_29(0x19, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_42_5851 end

    def Function_43_5EA0(): pass

    label("Function_43_5EA0")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x0)
    OP_68(11350, 1500, -3170, 0)
    MoveCamera(253, 22, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(17830, 0)
    SetChrPos(0x101, 8000, 0, -2300, 192)
    SetChrPos(0x102, 9300, 0, -1200, 192)
    SetChrPos(0x103, 11900, 0, -1200, 192)
    SetChrPos(0x104, 10600, 0, -2300, 192)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0273
    ChrTalk(
        0x101,
        (
            "#11P#0001F司令先是把装甲车\x01",
            "停在了这里吧。\x02\x03",

            "#0003F谨慎起见，确实也应该调查一下……\x01",
            "不过，警备队员肯定早就在\x01",
            "装甲车的附近搜索过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        (
            "#12P#0100F是啊……\x01",
            "我们也没必要再重新搜索一次了吧。\x02\x03",

            "#0103F而且，战车上好像还装设有机关炮，\x01",
            "也不能把罩子扯下来\x01",
            "进行调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x104,
        (
            "#6P#0303F嗯……\x01",
            "其实我倒是很想坐上去试试呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x103,
        (
            "#12P#0200F兰迪前辈曾在警备队待过，\x01",
            "应该乘坐过装甲车吧？\x02\x03",

            "这辆装甲车也只是将旧型号进行改良制造的，\x01",
            "坐在里面的感觉应该不会有太大变化吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#6P#0300F哈，我只是稍微有点兴趣而已啦。\x02\x03",

            "#0309F如果它能正式投入使用的话，\x01",
            "一定会大为活跃的……\x01",
            "诺艾尔他们肯定也会很高兴吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x101,
        "#11P#0009F哈哈，的确。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_61B5():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61B5)
    Sleep(100)
    WaitChrThread(0x101, 1)

    #C0279
    ChrTalk(
        0x101,
        (
            "#11P#0005F噢，从帝国那边\x01",
            "开过来一辆新车呢。\x02\x03",

            "#0000F我们过去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-12310, 1000, -1110, 0)
    MoveCamera(333, 29, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24260, 0)
    SetChrPos(0x101, 8000, 0, -4300, 0)
    SetChrPos(0x102, 9300, 0, -4300, 0)
    SetChrPos(0x103, 11900, 0, -4300, 0)
    SetChrPos(0x104, 10600, 0, -4300, 0)
    ClearChrFlags(0x29, 0x80)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x29)
    OP_D3(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x29, -33000, 0, 1000, 0)
    OP_70(0x9, 0x0)
    OP_74(0x9, 0x1E)
    OP_0D()
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_62E6():
        OP_98(0xFE, 0x36B0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_62E6)
    Sound(456, 0, 100, 0)
    WaitChrThread(0x29, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    Sleep(500)
    OP_71(0x6, 0x0, 0x8C, 0x0, 0x0)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    OP_79(0x6)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x9)
    Sound(472, 0, 100, 0)
    OP_68(10280, 1000, -1250, 8000)
    MoveCamera(358, 39, 0, 8000)
    OP_6E(470, 8000)
    SetCameraDistance(24260, 8000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_638C():
        OP_98(0xFE, 0x6D60, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_638C)
    SetMessageWindowPos(350, 0, -1, -1)

    #A0280
    AnonymousTalk(
        0x104,
        (
            "#0306F#10A哇……高级轿车啊，\x01",
            "帝国人果然非同一般呢。\x02",
        )
    )
    #Auto

    Sleep(2000)
    SetMessageWindowPos(350, 40, -1, -1)

    #A0281
    AnonymousTalk(
        0x103,
        (
            "#0200F#10A……似乎是莱恩福尔特公司制造的啊，\x01",
            "而且，好像还是特别定制型的。\x02",
        )
    )
    #Auto

    Sleep(2000)
    SetMessageWindowPos(310, 0, -1, -1)

    #A0282
    AnonymousTalk(
        0x101,
        "#0005F#10A车主究竟是何方神圣呢……\x02",
    )
    #Auto

    Sleep(1000)
    Sound(456, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(310, 40, -1, -1)

    #A0283
    AnonymousTalk(
        0x102,
        "#0105F#10A（……哎？这辆高级轿车是……）\x02",
    )
    #Auto

    Sleep(2000)
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x29, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    OP_6F(0x79)
    Fade(500)
    OP_68(9340, 1000, -2690, 0)
    MoveCamera(244, 24, 2, 0)
    OP_6E(470, 0)
    SetCameraDistance(20640, 0)
    OP_0D()
    SetMessageWindowPos(200, 250, -1, -1)
    SetChrName("男性的声音")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            "呀，我就说怎么这么眼熟……\x01",
            "这不是特别任务支援科的诸位嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_71(0x9, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x28, 9740, 0, 0, 180)

    def lambda_6606():
        OP_95(0xFE, 9740, 0, -1430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6606)

    def lambda_6620():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_6620)
    WaitChrThread(0x28, 1)

    #C0285
    ChrTalk(
        0x28,
        (
            "#12P#2800F──大家好啊，\x01",
            "最近身体还不错吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x102,
        "#5P#0105F迪塔叔叔……！\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#5P#0000F总裁……好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x28,
        (
            "#12P#2800F哈哈哈，抱歉，\x01",
            "我打扰到你们工作了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        "#6P#0203F不……没关系的。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        (
            "#5P#0300F总裁还是老样子，\x01",
            "气质仍然如此爽朗啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#5P#0100F叔叔，您是去忙工作，\x01",
            "刚刚才回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x28,
        (
            "#12P#2800F嗯，在帝国那边有个商务谈判。\x02\x03",

            "#2803F……说起来……\x02\x03",

            "#2801F你们身后那个\x01",
            "奇怪的庞然大物是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0293
    ChrTalk(
        0x101,
        (
            "#5P#0011F这个，其实是……\x01",
            "说来可就话长了……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x28,
        (
            "#12P#2803F是吗……\x01",
            "嗯，那就让我猜猜看吧。\x02\x03",

            "#2800F恐怕是警备队的新型装甲车，\x01",
            "对不对？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0295
    ChrTalk(
        0x102,
        "#5P#0105F您、您怎么会知……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x28,
        (
            "#12P#2804F哈哈，让你们吓了一跳吗。\x01",
            "……其实很简单。\x02\x03",

            "#2800F我昨天参加的那场庆祝会，\x01",
            "警备队的司令也出席了。\x02\x03",

            "司令喝醉之后，就命令部下把这辆车\x01",
            "开了过去，我可是亲眼看见的。\x02\x03",

            "#2806F我已经和他同席过很多次了，\x01",
            "真是觉得他的酒品\x01",
            "应该好好改正一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x103,
        (
            "#6P#0200F原来如此……\x01",
            "总裁当时也在场啊。\x02\x03",

            "然后在庆祝会结束之后就前往帝国了……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#0001F对了……既然如此，\x01",
            "您也许会有什么线索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x28,
        (
            "#12P#2805F……嗯？\x01",
            "有关什么的线索呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        "#5P#0100F那个，事情是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人将事情的经过做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0302
    ChrTalk(
        0x28,
        (
            "#12P#2800F……嗯……原来如此啊。\x02\x03",

            "怪不得把装甲车停在\x01",
            "人来人往的国境门正中。\x02\x03",

            "#2803F……不过，真不好意思啊，\x01",
            "我好像帮不上什么忙。\x02\x03",

            "因为我要赶在今天去进行商务谈判，\x01",
            "所以当时提前离开了庆祝会场，\x01",
            "随后就去了帝国。\x02\x03",

            "#2800F也就是说，在我通过贝尔加德门的时候，\x01",
            "司令还没有回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x104,
        (
            "#5P#0306F唉……那就没办法了啊。\x02\x03",

            "#0301F也就是说，我们只能顺着\x01",
            "司令走过的路线，老老实实地寻找了。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x28,
        (
            "#12P#2803F……嗯，是啊。\x01",
            "不过，作为补偿……\x02\x03",

            "#2800F就把贝尔从前送给我的忠告\x01",
            "说给你们听吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#5P#0005F玛丽亚贝尔小姐的忠告……？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x28,
        (
            "#12P#2803F那是很久之前的事情了……\x01",
            "想当初，我也是个总爱丢三落四的人。\x02\x03",

            "#2800F再加上我要负责的工作太多了。\x01",
            "像文件之类的琐碎东西，刚一转身，\x01",
            "马上就忘记扔到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#5P#0105F咦……原来叔叔也曾有过这样的一面啊……\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x28,
        (
            "#12P#2804F哈哈……大概也是因为\x01",
            "我当时还年轻吧。\x02\x03",

            "#2800F──总之，每当我找不到东西的时候，\x01",
            "贝尔就会帮我把丢掉的\x01",
            "东西找回来。\x02\x03",

            "每到这种时候，\x01",
            "她就会一边叹气一边说着。\x02\x03",

            "#2806F『爸爸，在找东西的时候，\x01",
            "  一定要去那些意想不到的地方找啊。』\x01",
            " ……就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#6P#0200F去意想不到的地方找……\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#5P#0300F嗯，很有道理，\x01",
            "很有道理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x28,
        (
            "#12P#2804F简单来说，贝尔说的其实就是\x01",
            "所谓的『转变视角』。\x02\x03",

            "#2800F不过，我也不敢保证这种思路\x01",
            "能对你们有所帮助……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0000F不，哪里的话，\x01",
            "很有参考价值呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#5P#0100F谢谢您了，叔叔。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x28,
        (
            "#12P#2804F呵呵，没什么大不了的。\x02\x03",

            "#2805F……哎呀，\x01",
            "不知不觉就说了这么久呢。\x02\x03",

            "#2800F把车一直停在这种地方，\x01",
            "会给别人造成麻烦吧。\x02\x03",

            "那我就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#5P#0105F啊……好的，\x01",
            "请您注意安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        "#5P#0000F真是非常感谢您。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x28,
        "#12P#2800F呵呵，再会了，诸位。\x02",
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x12C)

    def lambda_71A0():
        OP_95(0xFE, 9740, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_71A0)

    def lambda_71BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_71BA)
    WaitChrThread(0x28, 1)
    SetChrFlags(0x28, 0x80)
    OP_71(0x9, 0x14B, 0x168, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    Sleep(1000)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x9)
    Sound(457, 0, 100, 0)
    OP_68(21180, 1000, 100, 4000)
    MoveCamera(320, 33, 2, 4000)
    OP_6E(470, 4000)
    SetCameraDistance(21510, 4000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_7238():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7238)

    def lambda_7252():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7252)

    def lambda_725F():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_725F)

    def lambda_726C():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_726C)

    def lambda_7279():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7279)
    OP_6F(0x79)
    WaitChrThread(0x29, 1)
    Fade(500)
    OP_68(10320, 900, -2290, 0)
    MoveCamera(244, 25, 2, 0)
    OP_6E(470, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 11200, 0, 100, 90)
    SetChrPos(0x102, 10600, 0, -1500, 90)
    SetChrPos(0x103, 10600, 0, -700, 90)
    SetChrPos(0x104, 11200, 0, -2300, 90)
    OP_0D()

    #C0318
    ChrTalk(
        0x104,
        "#5P#0304F……那个人还是老样子啊。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        "#5P#0100F不过……得到了很好的建议呢。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#11P#0003F『转变视角』吗……\x02\x03",

            "#0000F在找东西的时候，这个思路的确很关键，\x01",
            "我们就把它牢记在心吧。\x02\x03",

            "好，接下来……\x01",
            "我们赶快去下一个地方找吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x103,
        (
            "#11P#0200F据米蕾优准尉所说……\x01",
            "司令把装甲车停在这里之后，\x01",
            "就去了食堂吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        "#11P#0000F嗯，我们去打听一下吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 7260, 0, -2410, 192)
    OP_29(0x19, 0x1, 0x3)
    ClearChrFlags(0x29, 0x80)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x1000)
    OP_65(0x3, 0x1)
    OP_70(0x6, 0x0)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    OP_49()
    OP_D5(0x1E)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_5EA0 end

    def Function_44_74A3(): pass

    label("Function_44_74A3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-104190, 750, 1480, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25670, 0)
    SetChrPos(0x101, -102980, 0, -110, 315)
    SetChrPos(0x102, -102300, 0, 860, 270)
    SetChrPos(0x103, -103100, 0, -1390, 315)
    SetChrPos(0x104, -103380, 0, 1490, 270)
    SetChrPos(0xC, -97850, 0, 5970, 270)
    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xB, 0x104, 0)
    SetChrSubChip(0xB, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0323
    ChrTalk(
        0x104,
        (
            "#12P#0309F哟，史黛拉，\x01",
            "你好像很忙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0324
    ChrTalk(
        0xB,
        (
            "#5P哎呀，这不是兰迪嘛。\x01",
            "你竟然会来这里，真是少见。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xB,
        "#5P想点些什么吗？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#12P#0001F那个……\x01",
            "不用了。\x02\x03",

            "我们接受了米蕾优准尉\x01",
            "的委托，正在搜索\x01",
            "启动钥匙……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 300)

    #C0327
    ChrTalk(
        0xB,
        (
            "#5P啊，原来准尉委托的人\x01",
            "就是你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#5P准尉之前也来拜托我了，\x01",
            "空闲的时候，我把食堂仔细找了一遍，\x01",
            "但还是没有找到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        "#12P#0106F这样啊……看来不在食堂里呢。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x103,
        (
            "#6P#0200F我们现在正沿着\x01",
            "司令的行迹进行搜索。\x02\x03",

            "方便的话，可以把昨天晚上\x01",
            "的情况告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xB,
        "#5P嗯，没问题啊。\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        (
            "#5P昨天是纪念庆典的第一天，\x01",
            "这里非常忙呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        (
            "#5P最后总算熬了过去，正打算休息\x01",
            "一下的时候，烂醉如泥的司令就\x01",
            "来到了食堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "#5P然后，他突然提出要求，\x01",
            "让我给他做点醒酒的东西，\x01",
            "没办法，我就只能做给他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xB,
        (
            "#5P我还得忙着准备今天的材料啊……\x01",
            "唉，真拿他没办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        "#12P#0006F嗯……他真是非常任性呢。\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x104,
        (
            "#12P#0303F那家伙总是滥用职权，\x01",
            "真让人受不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        (
            "#12P#0100F和索妮亚副司令相比，\x01",
            "可真是天差地别啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x103,
        (
            "#6P#0200F那么……\x01",
            "在那个时候，\x01",
            "他还拿着启动钥匙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xB,
        "#5P这个嘛……我有点想不起来了。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xB,
        (
            "#5P丢失钥匙的事情，\x01",
            "我也是在今天早晨才听说呢……\x01",
            "究竟是什么时候丢的，我也不太清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#12P#0001F这样啊……\x02\x03",

            "#0003F嗯，在这里也没有收获吗。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(400, 300, -1, -1)
    SetChrName("男性的声音")

    #A0343
    AnonymousTalk(
        0xC,
        (
            "……哎呀，怎么了？\x01",
            "你们怎么聚在这里？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-103780, 750, 2029, 2000)
    BeginChrThread(0xC, 3, 0, 45)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0x5A, 0x12C)

    def lambda_7AB9():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7AB9)

    def lambda_7AC6():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AC6)

    def lambda_7AD3():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AD3)

    def lambda_7AE0():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7AE0)

    def lambda_7AED():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7AED)
    WaitChrThread(0xC, 3)

    #C0344
    ChrTalk(
        0xB,
        (
            "#5P啊，比约德先生，\x01",
            "你来得正好。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xB,
        (
            "#5P这几位是来帮我们\x01",
            "寻找那把钥匙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x102,
        "#6P#0100F您好，我们是特别任务支援科的成员。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xC,
        (
            "#11P啊，就是那个传闻中的……\x01",
            "你们好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#6P#0309F呦，比约德。\x01",
            "你这个军事迷，还是老样子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        "#11P兰迪先生，好久不见了啊。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xB,
        (
            "#5P那……\x01",
            "准尉说的那把启动钥匙，\x01",
            "你那边有什么发现吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 300)

    #C0351
    ChrTalk(
        0xC,
        (
            "#11P没有呢，我虽然仔细找了一通，\x01",
            "但是毫无收获啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xC,
        (
            "#11P而且，司令似乎没来过旅舍这边……\x01",
            "总之，应该是不会\x01",
            "丢在这边的。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#0005F那个……『似乎』是什么意思呢？\x02\x03",

            "你当时不是一直在旅舍吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 300)

    #C0354
    ChrTalk(
        0xC,
        (
            "#11P哦，工作告一段落之后，\x01",
            "在司令过来之前的那段时间里，\x01",
            "我都在屋顶上休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xC,
        "#11P……啊，这么一说的话……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x103,
        "#6P#0205F想起什么了吗？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xC,
        (
            "#11P嗯，从屋顶上下来的时候，\x01",
            "我和司令正好擦肩而过。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xC,
        (
            "#11P想起来了，他当时确实拿着一个\x01",
            "看起来像是钥匙链的东西，\x01",
            "还套在手指上甩来甩去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xC,
        (
            "#11P说不定，我当时看到的\x01",
            "正是那把启动钥匙呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0360
    ChrTalk(
        0x101,
        (
            "#6P#0006F也就是说……\x02\x03",

            "#0001F从食堂前往屋顶这段路上，\x01",
            "司令还拿着启动钥匙的可能性\x01",
            "非常高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x103,
        (
            "#6P#0203F……不过，那么重要的东西，\x01",
            "他居然这么随意对待，实在让人费解。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#12P#0106F的确……\x01",
            "不过，我们算是得到了宝贵的证言呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        (
            "#6P#0309F哈哈，你这不是都能想起来嘛。\x01",
            "臭小子，非要先吊人胃口。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xC,
        (
            "#11P啊，是吗？\x01",
            "啊哈哈……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xB,
        (
            "#5P我说……\x01",
            "这种事情为什么不早点告诉我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xB,
        (
            "#5P害我把整个食堂都翻了一遍，\x01",
            "岂不都是白费力气嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xC, 0xB, 300)

    #C0367
    ChrTalk(
        0xC,
        "#11P啊哈，抱歉抱歉。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xC,
        (
            "#11P那么，我也得赶快回去工作了。\x01",
            "再见啦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80D1():
        OP_95(0xFE, -103000, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_80D1)
    WaitChrThread(0xC, 1)

    def lambda_80EF():
        OP_95(0xFE, -97850, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_80EF)
    WaitChrThread(0xC, 1)
    OP_68(-104190, 750, 1480, 2000)

    #C0369
    ChrTalk(
        0xB,
        "#5P哼，让他逃掉了。\x02",
    )

    CloseMessageWindow()

    def lambda_8137():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8137)

    def lambda_8144():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8144)

    def lambda_8151():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8151)

    def lambda_815E():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_815E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0370
    ChrTalk(
        0x104,
        (
            "#12P#0300F不过，托他的福，\x01",
            "我们得到了很有价值的线索呢。\x01",
            "谢谢你，史黛拉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 300)

    #C0371
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，即使只是确认了钥匙不在这里，\x01",
            "也使搜索范围缩小了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xB,
        "#5P不必客气。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "#5P我虽然不清楚\x01",
            "那个东西到底\x01",
            "有多重要……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xB,
        (
            "#5P但就算是为了准尉，\x01",
            "也请你们要努力找到钥匙，\x01",
            "交还给她哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        "#12P#0100F放心，我们一定会妥善解决的。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        "#6P#0203F……那么，我们接下来就去屋顶吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -101240, 0, -30, 90)
    SetChrPos(0xC, -162110, 0, -2500, 90)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_29(0x19, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_44_74A3 end

    def Function_45_833C(): pass

    label("Function_45_833C")


    def lambda_8341():
        OP_95(0xFE, -103000, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8341)
    WaitChrThread(0xC, 1)

    def lambda_835F():
        OP_95(0xFE, -103000, 0, 3500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_835F)
    WaitChrThread(0xC, 1)
    Return()

    # Function_45_833C end

    SaveToFile()

Try(main)
