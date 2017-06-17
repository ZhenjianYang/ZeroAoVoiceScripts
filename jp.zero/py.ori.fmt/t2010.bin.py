from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "コナーズ隊員",           # 1
        "シグ隊員",               # 2
        "クレス隊員",             # 3
        "ステラ",                 # 4
        "ビヨンド",               # 5
        "遊撃士スコット",         # 6
        "遊撃士ヴェンツェル",     # 7
        "観光客",                 # 8
        "商人",                   # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "観光客",                 # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "商人",                   # 17
        "観光客",                 # 18
        "観光客",                 # 19
        "商人",                   # 20
        "観光客",                 # 21
        "観光客",                 # 22
        "観光客",                 # 23
        "女の子",                 # 24
        "商人",                   # 25
        "観光客",                 # 26
        "観光客クウカ",           # 27
        "観光客ナット",           # 28
        "車１",                   # 29
        "観光客",                 # 30
        "観光客",                 # 31
        "車１",                   # 32
        "ディーター総裁",         # 33
        "ディーター総裁",         # 34
        "ミレイユ准尉",           # 35
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
    DeclNpc(-97470,  150,     -3950,   270,  341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
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
        "Function_10_13A7",        # 0A, 10
        "Function_11_1BD3",        # 0B, 11
        "Function_12_27B4",        # 0C, 12
        "Function_13_27B8",        # 0D, 13
        "Function_14_32C6",        # 0E, 14
        "Function_15_343F",        # 0F, 15
        "Function_16_3443",        # 10, 16
        "Function_17_4627",        # 11, 17
        "Function_18_48B5",        # 12, 18
        "Function_19_4A2E",        # 13, 19
        "Function_20_4B92",        # 14, 20
        "Function_21_4C20",        # 15, 21
        "Function_22_4C9D",        # 16, 22
        "Function_23_4E18",        # 17, 23
        "Function_24_4FA5",        # 18, 24
        "Function_25_5007",        # 19, 25
        "Function_26_5176",        # 1A, 26
        "Function_27_5312",        # 1B, 27
        "Function_28_5385",        # 1C, 28
        "Function_29_543A",        # 1D, 29
        "Function_30_5488",        # 1E, 30
        "Function_31_54C6",        # 1F, 31
        "Function_32_5652",        # 20, 32
        "Function_33_57CC",        # 21, 33
        "Function_34_57E9",        # 22, 34
        "Function_35_5869",        # 23, 35
        "Function_36_5B8F",        # 24, 36
        "Function_37_5BC3",        # 25, 37
        "Function_38_5C2A",        # 26, 38
        "Function_39_5D4B",        # 27, 39
        "Function_40_5E65",        # 28, 40
        "Function_41_5ED2",        # 29, 41
        "Function_42_5F76",        # 2A, 42
        "Function_43_6639",        # 2B, 43
        "Function_44_7EE8",        # 2C, 44
        "Function_45_8EE5",        # 2D, 45
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C94")

    #C0001
    ChrTalk(
        0x8,
        (
            "色々悩むこともあるけど……\x01",
            "この受付の仕事だって\x01",
            "警備隊の大切な任務の一つだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "仕事を与えられている以上は\x01",
            "きちんと成し遂げる。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "何はなくとも、それが大事だと思うよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CFC")

    label("loc_C94")


    #C0004
    ChrTalk(
        0x8,
        (
            "警備隊にいると報われないことは\x01",
            "確かに多いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "今与えられている仕事は\x01",
            "ちゃんとしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFC")

    Jump("loc_138D")

    label("loc_D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D6E")

    #C0006
    ChrTalk(
        0x8,
        "さて、今日も受付の仕事だ。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "……俺は、入隊時に夢見ていた\x01",
            "警備隊員をやれてるのかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138D")

    label("loc_D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E18")

    #C0008
    ChrTalk(
        0x8,
        (
            "ベルガード門詰めの警備隊員による\x01",
            "遺跡の調査は、早々に打ち切られた。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "引き時を弁えるのも司令の仕事だけど、\x01",
            "さすがにこれは怠慢と言わざるをえないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138D")

    label("loc_E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EBB")

    #C0010
    ChrTalk(
        0x8,
        (
            "帰国する観光客が増えだしたな……\x01",
            "やれやれ、今日中に終わるのかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "せっかくの記念祭なのに\x01",
            "こんなムサい所で\x01",
            "足止め食らわすとかわいそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138D")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F57")
    OP_4B(0x8, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0012
    ChrTalk(
        0x8,
        "はい、出国手続きは終わりです。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "ゲートを開くので\x01",
            "少しお待ち下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x16,
        (
            "うむ、そうかね。\x01",
            "とっとと妻を呼んで来るか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_138D")

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_104B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1006")

    #C0015
    ChrTalk(
        0x8,
        (
            "ふぅ……\x01",
            "そろそろピークは過ぎたかな。\x01",
            "随分忙しかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "帝国人は質実剛健な気質だって\x01",
            "聞いていたけど……\x01",
            "案外お祭り好きも多いみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1046")

    label("loc_1006")


    #C0017
    ChrTalk(
        0x8,
        (
            "折角の記念祭だ、\x01",
            "帝国や共和国の人も\x01",
            "楽しんできてほしいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1046")

    Jump("loc_138D")

    label("loc_104B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1137")

    #C0018
    ChrTalk(
        0x8,
        (
            "あー、忙しい。\x01",
            "やっと長蛇の列をさばききったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "今年は陸路の客が結構多いね。\x01",
            "素直に列車で来たほうが\x01",
            "直接街に着いて楽だろうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "……ま、折角のお祭りだ。\x01",
            "普段と違うことしたほうが\x01",
            "楽しいだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11D3")

    label("loc_1137")


    #C0021
    ChrTalk(
        0x8,
        (
            "今年は陸路の客が結構多いね。\x01",
            "素直に列車で来たほうが\x01",
            "直接街に着いて楽だろうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "……ま、折角のお祭りだ。\x01",
            "普段と違うことしたほうが\x01",
            "楽しいだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D3")

    Jump("loc_138D")

    label("loc_11D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127E")

    #C0023
    ChrTalk(
        0x8,
        "帝国方面へは、バスは殆ど出ていないんだ。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "帝国は全土に鉄道網が敷かれているからね。\x01",
            "クロスベルに来るにも、そっちの方が便利なのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12E3")

    label("loc_127E")


    #C0025
    ChrTalk(
        0x8,
        "帝国方面へは、バスは殆ど出ていないんだ。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "創立記念祭の期間中に\x01",
            "特別に運行されるくらいかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E3")

    Jump("loc_138D")

    label("loc_12E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_138D")

    #C0027
    ChrTalk(
        0x8,
        (
            "この鉄柵を超えたら、\x01",
            "そこはもう帝国との国境だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "……厚い鉄扉でも何でもない、\x01",
            "こんな棒っきれで遮ってるんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "頼りなさ過ぎて笑っちゃうよな。\x02",
    )

    CloseMessageWindow()

    label("loc_138D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A3")
    TalkEnd(0x16)
    Jump("loc_13A6")

    label("loc_13A3")

    TalkEnd(0x8)

    label("loc_13A6")

    Return()

    # Function_9_BAF end

    def Function_10_13A7(): pass

    label("Function_10_13A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_15C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1516")

    #C0030
    ChrTalk(
        0xFE,
        (
            "ここだけの話……\x01",
            "俺は警備隊司令の座を狙ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "あんな部下の気持ちを\x01",
            "まったく汲もうともしない男より、\x01",
            "よっぽどいい仕事をする自信があるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0300Fふーん……司令はともかく\x01",
            "准尉や副司令を超えるのは\x01",
            "なかなかキビしいと思うぜ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "…………う。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "そうか、司令という役職に\x01",
            "焦点を置いていたから\x01",
            "考えが及ばなかったな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15C1")

    label("loc_1516")


    #C0035
    ChrTalk(
        0xFE,
        (
            "俺はいつかきっと、\x01",
            "この警備隊を率いる司令になってやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令も……\x01",
            "まぁ、なんとか超えてみせよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#0306F……その調子じゃ\x01",
            "まだまだ先は長そうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C1")

    Jump("loc_1BCF")

    label("loc_15C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1644")

    #C0038
    ChrTalk(
        0xFE,
        (
            "そうか……あの遺跡を\x01",
            "調査してきたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "くっ、俺が司令なら\x01",
            "部隊を引き揚げさせはしなかったのに……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCF")

    label("loc_1644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1707")

    #C0040
    ChrTalk(
        0xFE,
        "あの遺跡には調査に行かされたが……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "普通の場所と違いすぎて、\x01",
            "正直言って調査どころじゃあなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        (
            "#0501F……やはりあの場所には\x01",
            "なにかありそうですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1781")

    label("loc_1707")


    #C0043
    ChrTalk(
        0xFE,
        (
            "あの遺跡の不気味な雰囲気は\x01",
            "口では上手く説明できん。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "他の場所と何が違うか……\x01",
            "行ってその目で確かめてみるといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1781")

    Jump("loc_1BCF")

    label("loc_1786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17CB")

    #C0045
    ChrTalk(
        0xFE,
        (
            "……輸出禁止品はないようだな。\x01",
            "積み荷、問題なし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCF")

    label("loc_17CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_17F9")

    #C0046
    ChrTalk(
        0xFE,
        "さすがに賑わってきたな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BCF")

    label("loc_17F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1823")

    #C0047
    ChrTalk(
        0xFE,
        "今のところ異常なしだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BCF")

    label("loc_1823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18E8")

    #C0048
    ChrTalk(
        0xFE,
        (
            "昨日から今日にかけて\x01",
            "相当大勢の観光客が訪れたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "きっとそれにまぎれて、\x01",
            "諜報員などもクロスベル入りして\x01",
            "しまったことだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "仕方ない、で済ませていいのだろうか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BCF")

    label("loc_18E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C0")

    #C0051
    ChrTalk(
        0xFE,
        (
            "表向き、この門では\x01",
            "ある程度出入りする人間を検める。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "けど、クロスベルへは列車でも来れる。\x01",
            "しかも駅では検分はやっていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "帝国や共和国の諜報員なんかは\x01",
            "現状、入り放題なんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A65")

    label("loc_19C0")


    #C0054
    ChrTalk(
        0xFE,
        (
            "帝国や共和国の諜報員なんかは\x01",
            "クロスベルに入り放題なのが現状だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "俺たちがここでやってる検分は\x01",
            "言ってみればクロスベル市民への\x01",
            "パフォーマンスみたいなもんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A65")

    Jump("loc_1BCF")

    label("loc_1A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B49")

    #C0056
    ChrTalk(
        0xFE,
        (
            "自治州の法律では他の国のように\x01",
            "軍隊を持つことはできない。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "帝国や共和国に目を付けられて\x01",
            "紛争を仕掛けられないようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "だから名目上、\x01",
            "俺たちは『警備隊』を\x01",
            "名乗るしかないってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BCF")

    label("loc_1B49")


    #C0059
    ChrTalk(
        0xFE,
        (
            "……言っておくが、警備隊はこれでも\x01",
            "厳しい訓練を耐え抜いたエリートなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "自衛しか出来ない現状が\x01",
            "もどかしいところだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCF")

    TalkEnd(0xFE)
    Return()

    # Function_10_13A7 end

    def Function_11_1BD3(): pass

    label("Function_11_1BD3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C67")
    Jump("loc_1CB1")

    label("loc_1C67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C87")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CB1")

    label("loc_1C87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CA7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CB1")

    label("loc_1CA7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CB1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC8")

    #C0061
    ChrTalk(
        0xFE,
        (
            "ステラちゃんに気持ちを伝えたら、\x01",
            "まさかのＯＫをもらえたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……ただ、返事は\x01",
            "『お試しで付き合ってみましょ』\x01",
            "だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "嬉しいは嬉しいんだけど……\x01",
            "なんだか微妙な所に\x01",
            "落ち着いてしまった気がするな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E57")

    label("loc_1DC8")


    #C0064
    ChrTalk(
        0xFE,
        (
            "……まぁ、お試しでも\x01",
            "ステラちゃんにＯＫをもらえたのには\x01",
            "間違いないだろう、うん。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "これから好きになってもらえるよう\x01",
            "がんばらないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E57")

    Jump("loc_27AC")

    label("loc_1E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2E")

    #C0066
    ChrTalk(
        0xFE,
        (
            "……決めた。\x01",
            "今日の勤務が終わったら\x01",
            "ステラちゃんにアタックかけてみるぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#0309Fおお、当たって砕けろッスよ！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "……あんま砕けたくないんだけど。\x01",
            "縁起悪いこと言うなよなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FA5")

    label("loc_1F2E")


    #C0069
    ChrTalk(
        0xFE,
        (
            "ステラちゃんを誘うなら\x01",
            "どこがいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "記念祭終わった今\x01",
            "ミシュラムなら空いてるだろうし\x01",
            "案外狙い目かもなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA5")

    Jump("loc_27AC")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_203D")

    #C0071
    ChrTalk(
        0xFE,
        (
            "記念祭が終わって\x01",
            "仕事に余裕が出てきたステラちゃん……\x01",
            "ああ、素敵だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……やっぱりこのまま\x01",
            "眺めているだけじゃだめだ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_203D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20D6")

    #C0073
    ChrTalk(
        0xFE,
        (
            "今日はステラちゃんを\x01",
            "ゆっくり眺めてられないほど\x01",
            "忙しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "だけど、腹が減っては戦はできぬ。\x01",
            "しっかりと腹ごしらえを済ませとこう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_20D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_21DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A7")

    #C0075
    ChrTalk(
        0xFE,
        (
            "……ステラちゃん……\x01",
            "昨日も差し入れしてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "隊員全員に配っててもいいんだ。\x01",
            "彼女の優しさに\x01",
            "触れられた気がするからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "ステラちゃん……\x01",
            "優しいあなたは素敵だ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21D6")

    label("loc_21A7")


    #C0078
    ChrTalk(
        0xFE,
        (
            "ステラちゃん……\x01",
            "優しいあなたは素敵だ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D6")

    Jump("loc_27AC")

    label("loc_21DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EC")

    #C0079
    ChrTalk(
        0xFE,
        (
            "昨日、ステラちゃんから\x01",
            "フルーツの差し入れがあったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "これはもしや、よくある\x01",
            "『頑張って、センパイ㈱』的な\x01",
            "メッセージなのではっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        (
            "#0306F……いや、普通に隊員全員に\x01",
            "配ったんだと思うッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "夢の無いことを言わないでくれよ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2374")

    label("loc_22EC")


    #C0083
    ChrTalk(
        0xFE,
        (
            "まぁ……とにかくステラちゃんは\x01",
            "よく気がつく子だってことさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "さーて、愛の込められた差し入れ……\x01",
            "よく味わって食べるとしますか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2374")

    Jump("loc_27AC")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23ED")

    #C0085
    ChrTalk(
        0xFE,
        (
            "忙しい中でこそ輝く\x01",
            "ステラちゃん……素敵だぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "よおし、メシ食ったら\x01",
            "俺もがんばらないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_23ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_247C")

    #C0087
    ChrTalk(
        0xFE,
        (
            "この門の中は司令のせいで\x01",
            "若干雰囲気が悪くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "そんな中、\x01",
            "あのステラちゃんのサバサバっぷりは\x01",
            "とてもスカッとするんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_247C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_27AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269A")

    #C0089
    ChrTalk(
        0xFE,
        (
            "ステラちゃん……いいなぁ。\x01",
            "もっとお近づきになりたいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "ランディ、お前がいない今……\x01",
            "ステラちゃんは渡さないからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#0309Fはっはっは、\x01",
            "なーに言ってんスか先輩。\x02\x03",

            "俺が入る前からいたのに\x01",
            "何のアプローチも\x01",
            "かけてなかったんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "ぐぐっ……\x01",
            "外堀を埋めるのに\x01",
            "時間がかかってただけさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        "#0309Fはは、まぁ頑張ってくださいッス。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0005F（ランディ……\x01",
            "  警備隊の人とは結構上手く\x01",
            "  やれてたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#0100F（ええ……女性問題が原因で\x01",
            "  辞めたとかいうから\x01",
            "  もっと険悪なのかと思ったけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27AC")

    label("loc_269A")


    #C0096
    ChrTalk(
        0xFE,
        (
            "最大のライバル、ランディがいた頃は\x01",
            "何度ステラちゃんに話しかけるチャンスを\x01",
            "奪われたことか分からない……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "だが今はお前はいない！\x01",
            "ステラちゃんにアプローチをかける\x01",
            "最大のチャンスだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#0303F（ステラとは普っ通～に\x01",
            "  お喋りしてただけなんだけどなぁ。\x01",
            "  ま、いいか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1BD3 end

    def Function_12_27B4(): pass

    label("Function_12_27B4")

    Call(0, 13)
    Return()

    # Function_12_27B4 end

    def Function_13_27B8(): pass

    label("Function_13_27B8")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27E3")
    Call(0, 44)
    Return()

    label("loc_27E3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_284B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_284B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286B")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32BD")

    label("loc_286B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287F")
    Jump("loc_32BD")

    label("loc_287F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32BD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A25")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B4")
    Call(0, 14)
    Jump("loc_2A20")

    label("loc_28B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A2")

    #C0099
    ChrTalk(
        0xB,
        (
            "昨日の夜、クレスさんに\x01",
            "『付き合ってくれないか！？』\x01",
            "なーんて言われちゃったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "別にクレスさんのことなんて\x01",
            "何とも思ってなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "まぁ、これから面白くなるかもしれないし\x01",
            "お試しってことでＯＫしたわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A20")

    label("loc_29A2")


    #C0102
    ChrTalk(
        0xB,
        (
            "クレスさんとお試しで\x01",
            "付き合うことになったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "なーんか落ち込んでるみたい。\x01",
            "……んー、よくわかんない人ねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A20")

    Jump("loc_32BD")

    label("loc_2A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2ABE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A41")
    Call(0, 14)
    Jump("loc_2AB9")

    label("loc_2A41")


    #C0104
    ChrTalk(
        0xB,
        (
            "この門に来る途中の街道で\x01",
            "分かれ道があるでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "あの先にある警察学校にも\x01",
            "ベルガード門の隊員が詰めてるのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB9")

    Jump("loc_32BD")

    label("loc_2ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2B55")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADA")
    Call(0, 14)
    Jump("loc_2B50")

    label("loc_2ADA")


    #C0106
    ChrTalk(
        0xB,
        "いらっしゃい、食事はいかが？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xB,
        (
            "緊急出動なんてことも\x01",
            "充分ありうるんだし、\x01",
            "食べれるときにしっかり食べないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B50")

    Jump("loc_32BD")

    label("loc_2B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2BDC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B71")
    Call(0, 14)
    Jump("loc_2BD7")

    label("loc_2B71")


    #C0108
    ChrTalk(
        0xB,
        (
            "ひゃー、今日はまた\x01",
            "随分と忙しいこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "んー、今日は隊員さんに\x01",
            "差し入れするヒマはなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD7")

    Jump("loc_32BD")

    label("loc_2BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2C78")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF8")
    Call(0, 14)
    Jump("loc_2C73")

    label("loc_2BF8")


    #C0110
    ChrTalk(
        0xB,
        (
            "クレスさん、\x01",
            "なーんかヘンなのよね昨日から。\x01",
            "ニヤニヤしちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "ちょっとカツでも\x01",
            "入れてやろうかしら、モモに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C73")

    Jump("loc_32BD")

    label("loc_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C94")
    Call(0, 14)
    Jump("loc_2DB0")

    label("loc_2C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D56")

    #C0112
    ChrTalk(
        0xB,
        (
            "昨日隊員さんたちに\x01",
            "フルーツを差し入れたら\x01",
            "随分感謝されちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "あはっ、馴れないことでも\x01",
            "たまにはやんないとね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "これが次の売り上げに\x01",
            "繋がるかも知んないし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DB0")

    label("loc_2D56")


    #C0115
    ChrTalk(
        0xB,
        (
            "記念祭中くらいは\x01",
            "サービスサービス！　しないとね。\x01",
            "フルーツ切るくらいなら楽でいいし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB0")

    Jump("loc_32BD")

    label("loc_2DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3095")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD1")
    Call(0, 14)
    Jump("loc_3090")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0A")

    #C0116
    ChrTalk(
        0xB,
        (
            "ふー、働いたァ。\x01",
            "いい感じに疲労が溜まってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "隊員さんたちも疲れてるだろうし\x01",
            "差し入れでも持ってってやろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        (
            "#0309Fおっ、いいねぇ。\x01",
            "俺にも差し入れしてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xB,
        (
            "ダーメ。\x01",
            "ランディくんは\x01",
            "もう警備隊じゃないっしょ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        "ちゃんと注文するならいいよ。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        "#0303Fケチ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F76")

    label("loc_2F0A")


    #C0122
    ChrTalk(
        0xB,
        (
            "んー、隊員さんたちへの差し入れは\x01",
            "なにがいいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "フルーツなんかは疲れによさそうね。\x01",
            "よし決定～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F76")

    Jump("loc_3090")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3018")

    #C0124
    ChrTalk(
        0xB,
        (
            "あたしには起動キーってのが、\x01",
            "どれだけ大事なものか\x01",
            "よくわかんないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "准尉さんの為にも、\x01",
            "なんとか見つけてあげてちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3090")

    label("loc_3018")


    #C0126
    ChrTalk(
        0xB,
        (
            "昨日、夜中に司令がわがままいって、\x01",
            "残業するハメになっちゃったから\x01",
            "疲れが取れてないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        "はー、忙しい忙しい。\x02",
    )

    CloseMessageWindow()

    label("loc_3090")

    Jump("loc_32BD")

    label("loc_3095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3128")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B1")
    Call(0, 14)
    Jump("loc_3123")

    label("loc_30B1")


    #C0128
    ChrTalk(
        0xB,
        (
            "あいよー、いらっしゃい。\x01",
            "好きなものを注文してちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "って言っても、\x01",
            "品揃えは大したことないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3123")

    Jump("loc_32BD")

    label("loc_3128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_32BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323B")

    #C0130
    ChrTalk(
        0xB,
        "いらっしゃー……ん？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "よく見たらランディくんじゃない。\x01",
            "あは、ひさしぶり。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0300Fよお、相変わらずだなステラ。\x01",
            "元気にやってっか？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "そっちこそ、特務支援課……だっけ？\x01",
            "大変そうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "ま、懐かしいついでに\x01",
            "なんか食べてってよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 6)
    Jump("loc_32BD")

    label("loc_323B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324E")
    Call(0, 14)
    Jump("loc_32BD")

    label("loc_324E")


    #C0135
    ChrTalk(
        0xB,
        (
            "懐かしいついでに\x01",
            "なんか食べてってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "でも言っとくけど、\x01",
            "ウチは知り合い割引なんて\x01",
            "やってないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BD")

    Jump("loc_27ED")

    label("loc_32C2")

    TalkEnd(0xB)
    Return()

    # Function_13_27B8 end

    def Function_14_32C6(): pass

    label("Function_14_32C6")


    #C0137
    ChrTalk(
        0xB,
        (
            "隊員さんたちにしっかり\x01",
            "スタミナつけてもらおうと思って、\x01",
            "肉鍋大会をしたことがあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "もう、箸をつけるヒマもなく\x01",
            "お肉がなくなっていってねぇ……\x01",
            "やっぱ肉体労働はお腹がすくわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "あなた達も肉鍋大会、やってみたら？\x01",
            "良かったら作り方を教えるわ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1A0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x6)
    Return()

    # Function_14_32C6 end

    def Function_15_343F(): pass

    label("Function_15_343F")

    Call(0, 16)
    Return()

    # Function_15_343F end

    def Function_16_3443(): pass

    label("Function_16_3443")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4623")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "休憩をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_34AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34CC")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_461E")

    label("loc_34CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E0")
    Jump("loc_461E")

    label("loc_34E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_461E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_360B")

    #C0142
    ChrTalk(
        0xC,
        (
            "司令は、その気になればいつでも\x01",
            "警備隊員を見捨ててしまうだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        (
            "今、警備隊にとって最も必要なものは\x01",
            "部下を大切に使える上司だと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3603")

    #C0144
    ChrTalk(
        0x10A,
        (
            "#0603F確かにな……\x02\x03",

            "#0601Fく、思い出したら腹が立ってきた。\x01",
            "警察の上層部どもめ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3603")

    SetScenarioFlags(0x0, 4)
    Jump("loc_369D")

    label("loc_360B")


    #C0145
    ChrTalk(
        0xC,
        (
            "司令は、その気になればいつでも\x01",
            "警備隊員を見捨ててしまうだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        (
            "部下を大切に使える上司だったら\x01",
            "この警備隊もどれだけいい場所だったか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369D")

    Jump("loc_461E")

    label("loc_36A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3851")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B9")

    #C0147
    ChrTalk(
        0xC,
        (
            "《不戦条約》が締結されて\x01",
            "クロスベルの人々は安心しているけど……\x01",
            "本当に大丈夫なのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xC,
        (
            "帝国・共和国への守りが\x01",
            "門の鉄柵一本という現状、\x01",
            "僕はどうしても不安だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xC,
        (
            "その気になれば帝国や共和国の軍に\x01",
            "いつでも攻めてこられるんじゃ\x01",
            "ないかってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_384C")

    label("loc_37B9")


    #C0150
    ChrTalk(
        0xC,
        (
            "《不戦条約》一つあるだけで\x01",
            "クロスベルの平和を信じていいのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xC,
        (
            "帝国・共和国への守りが\x01",
            "門の鉄柵一本という現状、\x01",
            "僕はどうしても不安だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384C")

    Jump("loc_461E")

    label("loc_3851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3953")

    #C0152
    ChrTalk(
        0xC,
        (
            "よく誤解されるんだけど、\x01",
            "僕のようなミリタリーオタクは\x01",
            "別に戦争が好きってワケじゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xC,
        (
            "あくまで軍の装備なんかに\x01",
            "機能美的なものを感じている\x01",
            "ってだけなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "殺し合いを楽しむような人種と\x01",
            "一緒にしないでくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_39BA")

    label("loc_3953")


    #C0155
    ChrTalk(
        0xC,
        (
            "ミリタリーオタクは、\x01",
            "別に戦争オタクってワケじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xC,
        "そこのところを一緒にしないでくれよな。\x02",
    )

    CloseMessageWindow()

    label("loc_39BA")

    Jump("loc_461E")

    label("loc_39BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3BD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B06")

    #C0157
    ChrTalk(
        0xC,
        (
            "警備隊の装甲車は\x01",
            "機動力が高く、小回りが聞くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xC,
        (
            "ただ、単体では優秀だけど\x01",
            "よその国と比べると\x01",
            "明らかに冷遇されてる。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "帝国には強力な列車砲があるし、\x01",
            "かの導力先進国リベールには\x01",
            "《アルセイユ》という高速飛行船がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        (
            "そういった強力な搭乗兵器に\x01",
            "対抗手段が何もないってのは致命的だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3BD0")

    label("loc_3B06")


    #C0161
    ChrTalk(
        0xC,
        (
            "どれだけ素晴らしい武器があっても\x01",
            "飛行船から爆撃されたら為す術がない。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        (
            "警備隊の装備は\x01",
            "冷遇されてると言えるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "クロスベルの情勢を考えると\x01",
            "強力な装備を持てないのは\x01",
            "仕方のないことだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD0")

    Jump("loc_461E")

    label("loc_3BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF5")

    #C0164
    ChrTalk(
        0xC,
        (
            "こないだ輸送されてきた携帯食糧#8Rレ ー シ ョ ン#……\x01",
            "ステラちゃんにこっそり分けてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "いやぁ、ありゃマズかったよ。\x01",
            "栄養はバッチリあるんだろうけど……\x01",
            "もう二度と食べたくないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "隊員さんたちは\x01",
            "野外演習の度に食べてるんだから\x01",
            "同情するよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D80")

    label("loc_3CF5")


    #C0167
    ChrTalk(
        0xC,
        (
            "しかし、あの携帯食糧#8Rレ ー シ ョ ン#は\x01",
            "死ぬほどマズかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xC,
        (
            "栄養も大事だけど、\x01",
            "美味しいことはもっと大事だと\x01",
            "思わないかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D80")

    Jump("loc_461E")

    label("loc_3D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB3")

    #C0169
    ChrTalk(
        0xC,
        (
            "隊員さんたち、\x01",
            "いつも司令への不満をこぼしてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        (
            "ま、僕もあの人嫌いだけどね。\x01",
            "やたらと偉ぶってるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "なにか武器の一つでも使えれば\x01",
            "評価はあがるんだけどなー。\x01",
            "上から命令するばかりなんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0006Fい、いやいや……\x01",
            "司令って本来そういうもんなんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F34")

    label("loc_3EB3")


    #C0173
    ChrTalk(
        0xC,
        (
            "とにかく……上から命令するだけで\x01",
            "武器の一つも使えないなら\x01",
            "警備隊失格だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "皆が司令への不満を\x01",
            "漏らす気持ちも分かるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F34")

    Jump("loc_461E")

    label("loc_3F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4225")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_40F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406C")

    #C0175
    ChrTalk(
        0xC,
        (
            "記念祭って言ったら、\x01",
            "たとえば帝国なんかでは\x01",
            "軍のパフォーマンスもあるんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "行軍パレードや公開演習……\x01",
            "携帯食糧#8Rレ ー シ ョ ン#の試食会なんてのも\x01",
            "楽しそうでいいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "市民との親睦も深められるし……\x01",
            "あ～あ、警備隊も\x01",
            "そういうのをやればいいのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40EB")

    label("loc_406C")


    #C0178
    ChrTalk(
        0xC,
        (
            "ベルガード門の警備隊も\x01",
            "何かすればいいのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xC,
        (
            "……ま、あの司令のことだ。\x01",
            "提案してもムダの一言で\x01",
            "却下しそうだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40EB")

    Jump("loc_4220")

    label("loc_40F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_41AF")

    #C0180
    ChrTalk(
        0xC,
        (
            "昨夜、屋上に行く司令と\x01",
            "すれ違ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xC,
        (
            "何かキーホルダーみたいなものを\x01",
            "指でくるくる回してたみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "今考えると、あれが例の\x01",
            "起動キーとやらだったんだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_41AF")


    #C0183
    ChrTalk(
        0xC,
        (
            "んー、さすがに\x01",
            "カウンターの下には\x01",
            "なさそうだなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xC,
        (
            "……おっと、お客さんかい？\x01",
            "ゆっくりしていってよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4220")

    Jump("loc_461E")

    label("loc_4225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_44AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E5")

    #C0185
    ChrTalk(
        0xC,
        (
            "警備隊の武装ってのは\x01",
            "大きく分けて二つだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "近接戦闘用に\x01",
            "スタンハルバード。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "そして、遠距離戦闘用に\x01",
            "アサルトライフル。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "この二つが使いこなせるのが\x01",
            "警備隊としての必須条件なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xC,
        (
            "……そういえば、ランディさんは\x01",
            "スタンハルバードの扱いは\x01",
            "警備隊一って囁かれてたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#0300F……ハハ、昔の話を\x01",
            "蒸し返すなっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xC,
        (
            "いやいや、演習の時は\x01",
            "よく拝見させてもらったもんだよ。\x01",
            "あれはスゴかったなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_44A6")

    label("loc_43E5")


    #C0192
    ChrTalk(
        0xC,
        (
            "スタンハルバードに\x01",
            "アサルトライフル……\x01",
            "どちらも扱いは難しいけど強力な武装だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xC,
        (
            "特にスタンハルバードの扱いじゃ、\x01",
            "ランディさんの右に出るものはいなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xC,
        "あれはスゴかったなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_44A6")

    Jump("loc_461E")

    label("loc_44AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_461E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458D")

    #C0195
    ChrTalk(
        0xC,
        (
            "僕、ミリタリーオタクってやつでね。\x01",
            "軍人や武器や戦車を見るのが大好きなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "だけど、警備隊は\x01",
            "帝国や共和国を刺激しないように\x01",
            "大規模な演習を控えてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xC,
        "いやはや……残念極まりないよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_461E")

    label("loc_458D")


    #C0198
    ChrTalk(
        0xC,
        (
            "……まぁ、それでも\x01",
            "通常時の演習なんかは\x01",
            "結構楽しみに見てるんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        (
            "本当なら装甲車や導力砲を使った\x01",
            "大規模な演習が見たいんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_461E")

    Jump("loc_3450")

    label("loc_4623")

    TalkEnd(0xC)
    Return()

    # Function_16_3443 end

    def Function_17_4627(): pass

    label("Function_17_4627")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46BB")
    Jump("loc_4705")

    label("loc_46BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_46DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4705")

    label("loc_46DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46FB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4705")

    label("loc_46FB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4705")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_48AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4856")

    #C0200
    ChrTalk(
        0xFE,
        (
            "昨夜、マフィアらしき黒服の人間が\x01",
            "警備隊の司令と密会してたっていう\x01",
            "情報が入ってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "この間の抗争騒ぎから\x01",
            "ほとんど間も空いてないし、\x01",
            "ちょっと気になってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "当の司令が出かけててね。\x01",
            "聞き込みはどうも無理そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        "うーん、無駄足だったなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_48AD")

    label("loc_4856")


    #C0204
    ChrTalk(
        0xFE,
        "うーん、無駄足だったなぁ……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "仕方ない、そろそろ\x01",
            "クロスベル市に戻るとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AD")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_4627 end

    def Function_18_48B5(): pass

    label("Function_18_48B5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4949")
    Jump("loc_4993")

    label("loc_4949")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4969")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4993")

    label("loc_4969")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4989")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4993")

    label("loc_4989")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4993")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A26")

    #C0206
    ChrTalk(
        0xFE,
        (
            "この門はときどき利用するが……\x01",
            "いつも司令がいないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "……警備隊隊員の心中を察するな。\x02",
    )

    CloseMessageWindow()

    label("loc_4A26")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_48B5 end

    def Function_19_4A2E(): pass

    label("Function_19_4A2E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AC2")
    Jump("loc_4B0C")

    label("loc_4AC2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4AE2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B0C")

    label("loc_4AE2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B02")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B0C")

    label("loc_4B02")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B0C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0208
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "予定よりも早く着いちゃってね。\x01",
            "軽食をとって時間を潰しているのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_4A2E end

    def Function_20_4B92(): pass

    label("Function_20_4B92")

    TalkBegin(0xFE)

    #C0210
    ChrTalk(
        0xFE,
        (
            "導力車で帝国と行き来していると\x01",
            "ここでの検分が面倒だわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "まぁ、小回りが効く分\x01",
            "バスや列車よりは\x01",
            "商談に向いていると思うがね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4B92 end

    def Function_21_4C20(): pass

    label("Function_21_4C20")

    TalkBegin(0xFE)

    #C0212
    ChrTalk(
        0xFE,
        (
            "入国手続きがやっと済んだよ。\x01",
            "長い列が出来て大変だったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "さーて、早速クロスベル市に\x01",
            "向かうとしようかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4C20 end

    def Function_22_4C9D(): pass

    label("Function_22_4C9D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D31")
    Jump("loc_4D7B")

    label("loc_4D31")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D51")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D7B")

    label("loc_4D51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D71")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D7B")

    label("loc_4D71")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D7B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0214
    ChrTalk(
        0xFE,
        (
            "私はミシュラムに\x01",
            "用事があって来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "フフ……予定は最終日だし、\x01",
            "それまで記念祭を楽しむとするかね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_4C9D end

    def Function_23_4E18(): pass

    label("Function_23_4E18")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4EAC")
    Jump("loc_4EF6")

    label("loc_4EAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4ECC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4EF6")

    label("loc_4ECC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EEC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4EF6")

    label("loc_4EEC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EF6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0216
    ChrTalk(
        0xFE,
        (
            "今年は主人がとても楽しいところに\x01",
            "連れて行ってくれるそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "ホホホ、自信満々そうですし\x01",
            "楽しみにしておかなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_4E18 end

    def Function_24_4FA5(): pass

    label("Function_24_4FA5")

    TalkBegin(0xFE)

    #C0218
    ChrTalk(
        0xFE,
        "おや……彼女はどこいった？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "軽食を買ってくるから\x01",
            "待ってるように言っといたのに……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4FA5 end

    def Function_25_5007(): pass

    label("Function_25_5007")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_509B")
    Jump("loc_50E5")

    label("loc_509B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50E5")

    label("loc_50BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50E5")

    label("loc_50DB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50E5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0220
    ChrTalk(
        0xFE,
        (
            "バスが来るまで\x01",
            "まだ時間がありそうざます。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "おなかも空いたし、\x01",
            "今のうちに腹ごしらえざます。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_5007 end

    def Function_26_5176(): pass

    label("Function_26_5176")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_520A")
    Jump("loc_5254")

    label("loc_520A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_522A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5254")

    label("loc_522A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_524A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5254")

    label("loc_524A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5254")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0222
    ChrTalk(
        0xFE,
        (
            "夫が出国手続きを済ますのを\x01",
            "待っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "もう少し記念祭を堪能したかったけど……\x01",
            "休みが今日までしか取れなかったから\x01",
            "仕方が無いわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_5176 end

    def Function_27_5312(): pass

    label("Function_27_5312")

    TalkBegin(0xFE)

    #C0224
    ChrTalk(
        0xFE,
        (
            "記念祭？　知らん知らん。\x01",
            "わしは商売に来ただけだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "商売が終わったら\x01",
            "さっさと帰るに限るわい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_5312 end

    def Function_28_5385(): pass

    label("Function_28_5385")

    TalkBegin(0xFE)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0226
    ChrTalk(
        0x19,
        (
            "ハニー、ここで待っててくれるかい？\x01",
            "いまから出国手続きをしてくるからサ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1A,
        "ダーリン、わかったわ㈱\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x1A,
        (
            "でも待つのは嫌いだから、\x01",
            "早く終わらせてきてね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_28_5385 end

    def Function_29_543A(): pass

    label("Function_29_543A")

    TalkBegin(0xFE)

    #C0229
    ChrTalk(
        0xFE,
        (
            "うーむ、やはり時間がかかりそうだな。\x01",
            "夜になる前に来て正解だった。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_543A end

    def Function_30_5488(): pass

    label("Function_30_5488")

    TalkBegin(0xFE)

    #C0230
    ChrTalk(
        0xFE,
        (
            "えーっと……\x01",
            "出国手続きはどこでとればいいのかな？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_5488 end

    def Function_31_54C6(): pass

    label("Function_31_54C6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_555A")
    Jump("loc_55A4")

    label("loc_555A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_557A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55A4")

    label("loc_557A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_559A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55A4")

    label("loc_559A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55A4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0231
    ChrTalk(
        0xFE,
        (
            "ふむぅ……\x01",
            "警備隊の方と共同の食堂なのですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "あまり気は進みませんが、\x01",
            "おなかもすきましたし\x01",
            "我慢するとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_54C6 end

    def Function_32_5652(): pass

    label("Function_32_5652")

    TalkBegin(0xFE)
    OP_52(0x1F, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x1F, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_56E9")
    Jump("loc_5733")

    label("loc_56E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5709")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5733")

    label("loc_5709")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5729")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5733")

    label("loc_5729")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5733")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1F, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0233
    ChrTalk(
        0xFE,
        "ほらほら、落ち着いて食べなさい。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "クロスベル市へのバスは\x01",
            "何本も出てるんだから、\x01",
            "慌てる事はないぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_5652 end

    def Function_33_57CC(): pass

    label("Function_33_57CC")

    TalkBegin(0xFE)

    #C0235
    ChrTalk(
        0xFE,
        "もくもくもく……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_57CC end

    def Function_34_57E9(): pass

    label("Function_34_57E9")

    TalkBegin(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        (
            "うふふ……\x01",
            "沢山いい品を手に入れる事が\x01",
            "できましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "これから帝国に帰って、\x01",
            "さっそく売りさばきたいと思います。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_57E9 end

    def Function_35_5869(): pass

    label("Function_35_5869")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A26")

    #C0238
    ChrTalk(
        0xFE,
        (
            "ズルズル～……\x01",
            "ムシャムシャムシャムシャ……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        "もぐもぐもぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        "…………ぷはぁ。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_596B")
    Jump("loc_59B5")

    label("loc_596B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_598B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59B5")

    label("loc_598B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59AB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59B5")

    label("loc_59AB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59B5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0241
    ChrTalk(
        0xFE,
        (
            "……何か用か？\x01",
            "人の食べるところを\x01",
            "ジロジロ見るもんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B87")

    label("loc_5A26")


    #C0242
    ChrTalk(
        0xFE,
        "もぐもぐもぐもぐ……\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AD4")
    Jump("loc_5B1E")

    label("loc_5AD4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AF4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B1E")

    label("loc_5AF4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B14")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B1E")

    label("loc_5B14")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B1E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0243
    ChrTalk(
        0xFE,
        (
            "……何か用か？\x01",
            "人の食べるところを\x01",
            "ジロジロ見るもんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B87")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_5869 end

    def Function_36_5B8F(): pass

    label("Function_36_5B8F")

    TalkBegin(0xFE)

    #C0244
    ChrTalk(
        0xFE,
        (
            "あの青いカバー……\x01",
            "すごく気になるわね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_5B8F end

    def Function_37_5BC3(): pass

    label("Function_37_5BC3")

    TalkBegin(0xFE)

    #C0245
    ChrTalk(
        0xFE,
        (
            "よっと……早いところ\x01",
            "出発するとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "待ちに待った記念祭、\x01",
            "存分に楽しまなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_5BC3 end

    def Function_38_5C2A(): pass

    label("Function_38_5C2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D01")
    TurnDirection(0xFE, 0x0, 0)

    #C0247
    ChrTalk(
        0xFE,
        (
            "皆さん、それにランディ。\x01",
            "今回はありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "また何かあったら\x01",
            "要請を出させてもらいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "さて、観光客の波が\x01",
            "引いたところを見計らって\x01",
            "移動させないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    Jump("loc_5D47")

    label("loc_5D01")


    #C0250
    ChrTalk(
        0xFE,
        (
            "観光客の波が\x01",
            "引いたところを見計らって\x01",
            "装甲車を移動させないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D47")

    TalkEnd(0xFE)
    Return()

    # Function_38_5C2A end

    def Function_39_5D4B(): pass

    label("Function_39_5D4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DDE")

    #C0251
    ChrTalk(
        0xFE,
        (
            "観光に来たら、\x01",
            "その土地の料理には\x01",
            "必ず手を出さなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "クロスベルでは\x01",
            "どんなものが食べられるかしら。\x01",
            "たのしみ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5E61")

    label("loc_5DDE")


    #C0253
    ChrTalk(
        0xFE,
        (
            "あたし、結構グルメなのよ。\x01",
            "クロスベルは何が美味しいのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……考えたら\x01",
            "お腹が空いてきちゃった。\x01",
            "何か注文しようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E61")

    TalkEnd(0xFE)
    Return()

    # Function_39_5D4B end

    def Function_40_5E65(): pass

    label("Function_40_5E65")

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
            "この先、警備隊専用貨物線路\x01",
            "    関係者以外立入禁止\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_5E65 end

    def Function_41_5ED2(): pass

    label("Function_41_5ED2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F4B")

    #C0256
    ChrTalk(
        0xFE,
        (
            "なんだか迷っちゃったよ。\x01",
            "どこだろうここ……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "……ま、いっか。\x01",
            "せっかくだし探検しちゃえ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5F72")

    label("loc_5F4B")


    #C0258
    ChrTalk(
        0xFE,
        (
            "迷っても気にしな～い。\x01",
            "探検探検！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F72")

    TalkEnd(0xFE)
    Return()

    # Function_41_5ED2 end

    def Function_42_5F76(): pass

    label("Function_42_5F76")

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

    def lambda_60AA():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60AA)

    def lambda_60C4():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60C4)

    def lambda_60DE():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_60DE)

    def lambda_60F8():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_60F8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6138():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6138)
    WaitChrThread(0x101, 1)

    #C0259
    ChrTalk(
        0x101,
        "#11P#0005F……なんだろう、コレ。\x02",
    )

    CloseMessageWindow()

    def lambda_616F():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_616F)
    Sleep(100)

    def lambda_617F():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_617F)
    Sleep(100)

    def lambda_618F():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_618F)
    Sleep(100)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0260
    ChrTalk(
        0x104,
        (
            "#6P#0305F……んん、こんなもん\x01",
            "こないだまであったか？\x02\x03",

            "#0309Fどれどれ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_61F9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_61F9)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0261
    ChrTalk(
        0x102,
        "#11P#0105F……どうしたの、ランディ？\x02",
    )

    CloseMessageWindow()

    def lambda_6259():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6259)
    WaitChrThread(0x104, 1)

    #C0262
    ChrTalk(
        0x104,
        "#6P#0301Fこれ……警備隊の装甲車みたいだぜ。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#12P#0205F何故こんなところに装甲車が……？\x02\x03",

            "しかも被せ物をして隠しているなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        (
            "#6P#0306F……っていうか、隠せてねぇよな。\x02\x03",

            "むしろ存在感ありありに\x01",
            "なっちまってる気がするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそういえば、ベルガード門から\x01",
            "支援要請が来てたよな。\x02\x03",

            "#0001Fもしかしたらこの装甲車が\x01",
            "関係あるのかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x103,
        (
            "#12P#0203F確か、『紛失物の捜索』との事でしたね。\x02\x03",

            "#0200F依頼者は確か……ミレイユ准尉。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_END)), "loc_6488")

    #C0267
    ChrTalk(
        0x101,
        (
            "#11P#0005Fミレイユさんっていうと……\x01",
            "あの女性士官の。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        "#6P#0304Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6545")

    label("loc_6488")


    #C0269
    ChrTalk(
        0x101,
        (
            "#11P#0005Fミレイユ准尉……\x01",
            "ランディ、知ってるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        (
            "#6P#0300Fああ、知ってるぜ。\x01",
            "……元同僚だ。\x02\x03",

            "#0304Fそっか、俺がいた頃は\x01",
            "まだ曹長だったはずだが……\x01",
            "いつの間にか昇進してたんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6545")


    #C0271
    ChrTalk(
        0x102,
        (
            "#12P#0100F忙しくしてるかもしれないけど、\x01",
            "そのミレイユ准尉に\x01",
            "話を聞いてみましょう。\x02\x03",

            "その装甲車の事も、\x01",
            "気になるならそれとなく\x01",
            "聞けばいいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#11P#0000F……だな。\x01",
            "よし、じゃあ行ってみるか。\x02",
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

    # Function_42_5F76 end

    def Function_43_6639(): pass

    label("Function_43_6639")

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
            "#11P#0001F司令はまず、ここに装甲車を止めて\x01",
            "いったって話だったな。\x02\x03",

            "#0003F念のため調べておこうかと思ったけど……\x01",
            "さすがに装甲車の周辺くらいは\x01",
            "警備隊員が捜索しているだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそうね……\x01",
            "改めて調べる必要もないでしょう。\x02\x03",

            "#0103Fバルカン砲を積んでいるそうだから、\x01",
            "カバーを外して調べるわけにも\x01",
            "いかないでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x104,
        (
            "#6P#0303Fふーむ……\x01",
            "いっぺん拝んでみたかったもんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x103,
        (
            "#12P#0200Fランディさんは警備隊にいたんですから、\x01",
            "装甲車に乗ったことはあるのでは？\x02\x03",

            "従来の装甲車を改良したものらしいですし\x01",
            "乗り心地はあまり変わらないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#6P#0300Fま、ちょっと興味があるってことよ。\x02\x03",

            "#0309F正式に運用しだしたらそりゃあ\x01",
            "活躍するだろうし……\x01",
            "ノエルあたりが喜ぶんじゃねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x101,
        "#11P#0009Fはは、確かにな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_69C0():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69C0)
    Sleep(100)
    WaitChrThread(0x101, 1)

    #C0279
    ChrTalk(
        0x101,
        (
            "#11P#0005Fおっと、帝国から新しい車両が\x01",
            "来たみたいだ。\x02\x03",

            "#0000Fちょっと端に寄っていよう。\x02",
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

    def lambda_6B05():
        OP_98(0xFE, 0x36B0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_6B05)
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

    def lambda_6BAB():
        OP_98(0xFE, 0x6D60, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_6BAB)
    SetMessageWindowPos(350, 0, -1, -1)

    #A0280
    AnonymousTalk(
        0x104,
        (
            "#0306F#10Aうはー……リムジンかよ。\x01",
            "やっぱ帝国人は違うねぇ。\x02",
        )
    )
    #Auto

    Sleep(2000)
    SetMessageWindowPos(350, 40, -1, -1)

    #A0281
    AnonymousTalk(
        0x103,
        (
            "#0200F#10A……ラインフォルト社製のようですね。\x01",
            "それもオーダーメイドのようです。\x02",
        )
    )
    #Auto

    Sleep(2000)
    SetMessageWindowPos(310, 0, -1, -1)

    #A0282
    AnonymousTalk(
        0x101,
        "#0005F#10A一体どこの誰だろう……\x02",
    )
    #Auto

    Sleep(1000)
    Sound(456, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(310, 40, -1, -1)

    #A0283
    AnonymousTalk(
        0x102,
        "#0105F#10A（……あれ？　このリムジンって……）\x02",
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
    SetChrName("男性の声")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            "おや、どこかで見た顔だと思えば……\x01",
            "特務支援課の諸君じゃないか。\x02",
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

    def lambda_6E3B():
        OP_95(0xFE, 9740, 0, -1430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6E3B)

    def lambda_6E55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_6E55)
    WaitChrThread(0x28, 1)

    #C0285
    ChrTalk(
        0x28,
        (
            "#12P#2800F──ごきげんよう。\x01",
            "元気にしていたかね？\x02",
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
        "#5P#0105Fディーターおじさま……！\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#5P#0000F総裁……ご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x28,
        (
            "#12P#2800Fハハハ、すまない。\x01",
            "仕事の邪魔をしてしまったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        "#6P#0203Fいえ……問題ありません。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        (
            "#5P#0300F相変わらず、\x01",
            "爽やかオーラ満載だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#5P#0100Fおじさまは、お仕事から\x01",
            "お帰りになった所ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x28,
        (
            "#12P#2800Fああ、帝国の方で商談があってね。\x02\x03",

            "#2803F……ところで……\x02\x03",

            "#2801F君たちの後ろの、やたらと\x01",
            "巨大な存在感を有する物体は……\x02",
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
            "#5P#0011Fええっと、これはですね……\x01",
            "話せば長くなるというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x28,
        (
            "#12P#2803Fそうか……\x01",
            "フム、ならば当てて見せよう。\x02\x03",

            "#2800F恐らく、警備隊の新型装甲車両、\x01",
            "といった所ではないかね？\x02",
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
        "#5P#0105Fど、どうしてそれを……？\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x28,
        (
            "#12P#2804Fハハ、驚かせてしまったかな。\x01",
            "……簡単なことだよ。\x02\x03",

            "#2800F昨日、私が参加した祝賀会の席に\x01",
            "警備隊の司令も出席していてね。\x02\x03",

            "酔った司令が部下に持ち出させた車両を\x01",
            "この目で見ているのだよ。\x02\x03",

            "#2806F彼とは何度か同席したことがあるが、\x01",
            "もう少し酒癖を良くしたほうが\x01",
            "いいと思うのだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x103,
        (
            "#6P#0200Fなるほど……\x01",
            "総裁もその場にいたんですね。\x02\x03",

            "それから、帝国に出かけたのなら……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#0001Fそうだ……だったら何か、\x01",
            "心当たりがあるかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x28,
        (
            "#12P#2805F……ふむ、\x01",
            "一体なんのことかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        "#5P#0100Fえっと、実は……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは事情を説明した。\x07\x00\x02",
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
            "#12P#2800F……ふむ……なるほどな。\x02\x03",

            "道理で人通りの多い門の中に\x01",
            "装甲車が放置されているわけだ。\x02\x03",

            "#2803F……しかし、すまないな。\x01",
            "どうやら力にはなれないようだ。\x02\x03",

            "私は今日の商談があったから、\x01",
            "祝賀会は早めにお暇して\x01",
            "帝国に向かったのだよ。\x02\x03",

            "#2800Fつまり、私がベルガード門を通ったのは\x01",
            "司令が戻る前ということになる。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x104,
        (
            "#5P#0306Fあ～……なら仕方ないッスね。\x02\x03",

            "#0301Fとすると、やっぱ地道に足取りを\x01",
            "辿っていくしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x28,
        (
            "#12P#2803F……ふむ、そうだな。\x01",
            "代わりと言ってはなんだが……\x02\x03",

            "#2800F昔、ベルに注意された話を\x01",
            "させてもらってもいいかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#5P#0005Fマリアベルさんに……？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x28,
        (
            "#12P#2803F昔のことだが……\x01",
            "私は、よく物を失くす人間だった。\x02\x03",

            "#2800F何せ抱える仕事が多いものでね。\x01",
            "書類やら何やらが、どこにやったか\x01",
            "すぐ分からなくなってしまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#5P#0105Fへぇ……おじさまにそんな一面が……\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x28,
        (
            "#12P#2804Fはは……若かったから\x01",
            "というのもあると思うがね。\x02\x03",

            "#2800F──まぁ、そうやって物を失くす度に\x01",
            "ベルがどこからか失くした物を\x01",
            "見つけてきてくれてね。\x02\x03",

            "その度に彼女は、\x01",
            "ため息をつきながらこう言うんだ。\x02\x03",

            "#2806F『お父様、失くしたものを探すときは\x01",
            "  思いもよらない場所を探すことですわ。』\x01",
            " ……とね。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#6P#0200F思いもよらない場所を探す……\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#5P#0300Fまぁ、当たり前っちゃあ、\x01",
            "当たり前ッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x28,
        (
            "#12P#2804F要するにベルが言いたかったのは、\x01",
            "『視点を変えろ』ということなのだろう。\x02\x03",

            "#2800Fもっとも、君たちの役に立つかまでは\x01",
            "保障しないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0000Fい、いえ。\x01",
            "参考になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#5P#0100Fありがとうございます、おじさま。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x28,
        (
            "#12P#2804Fふふ、大した話ではなかったがね。\x02\x03",

            "#2805F……おっと、\x01",
            "ずいぶん話し込んでしまったな。\x02\x03",

            "#2800Fこんな所にいつまでも車を停めていては\x01",
            "いささか邪魔になってしまう。\x02\x03",

            "私はこれで失礼させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#5P#0105Fあ……はい、\x01",
            "おじさまもお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        "#5P#0000Fどうも、ありがとうございました。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x28,
        "#12P#2800Fふふ、さらばだ諸君。\x02",
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x12C)

    def lambda_7B93():
        OP_95(0xFE, 9740, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7B93)

    def lambda_7BAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_7BAD)
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

    def lambda_7C2B():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7C2B)

    def lambda_7C45():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C45)

    def lambda_7C52():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C52)

    def lambda_7C5F():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C5F)

    def lambda_7C6C():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C6C)
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
        "#5P#0304F……あの人も相変わらずだなぁ。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        "#5P#0100Fでも……いい助言をもらったわ。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#11P#0003F『視点を変えろ』か……\x02\x03",

            "#0000F確かに物を探すためには大切なことだし\x01",
            "心に留めておいたほうがよさそうだ。\x02\x03",

            "よし、それじゃあ……\x01",
            "早速次の足取りを辿ってみるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x103,
        (
            "#11P#0200F確か、ミレイユ准尉の話では……\x01",
            "司令はここに装甲車を停めた後、\x01",
            "食堂に向かったということでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        "#11P#0000Fああ、話を聞きに行ってみよう。\x02",
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

    # Function_43_6639 end

    def Function_44_7EE8(): pass

    label("Function_44_7EE8")

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
            "#12P#0309Fよう、ステラ。\x01",
            "忙しそうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0324
    ChrTalk(
        0xB,
        (
            "#5Pあら、ランディくんじゃない。\x01",
            "珍しいわね、ここに来るなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xB,
        "#5Pなにかご注文かしら？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#12P#0001Fえっと……\x01",
            "そうではないんです。\x02\x03",

            "ミレイユ准尉からの依頼で、\x01",
            "例の起動キーの捜索を\x01",
            "行なっている所でして……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 300)

    #C0327
    ChrTalk(
        0xB,
        (
            "#5Pああ、准尉さんが頼んだのは\x01",
            "あなた達のことだったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#5P私も准尉さんに頼まれて、\x01",
            "空いた時間に食堂内をくまなく探したけど\x01",
            "見つけられなかったのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        "#12P#0106Fそう……食堂には無いみたいね。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x103,
        (
            "#6P#0200F今、司令の足取りを追って\x01",
            "捜索をしているところなんです。\x02\x03",

            "よければ昨夜の様子を\x01",
            "お聞かせ願えませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xB,
        "#5Pああ、別にいいわよ。\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        (
            "#5P昨日は記念祭初日で\x01",
            "すっごく忙しかったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        (
            "#5P何とか乗り切って一息ついてたら、\x01",
            "ぐでんぐでんに酔っ払った司令が\x01",
            "食堂に入ってきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "#5Pそしていきなり、\x01",
            "酒の締めになるものを作れって\x01",
            "言われたから、仕方なく作ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xB,
        (
            "#5P今日の仕込みもあったのに……\x01",
            "ほんと、参っちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        "#12P#0006Fうーん……我が物顔だなぁ。\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x104,
        (
            "#12P#0303F振り回される方は\x01",
            "たまったもんじゃないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        (
            "#12P#0100Fソーニャ副司令とは\x01",
            "大違いの人物ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x103,
        (
            "#6P#0200Fそれで……\x01",
            "そのときはまだ起動キーは\x01",
            "持っていたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xB,
        "#5Pさぁ……どうだったかしら。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xB,
        (
            "#5Pキーを失くしたって聞いたのも\x01",
            "今日の朝だったし……\x01",
            "ちょっと私にはわからないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#12P#0001Fそうですか……\x02\x03",

            "#0003Fううん、ここでも収穫なしか。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(400, 300, -1, -1)
    SetChrName("男の声")

    #A0343
    AnonymousTalk(
        0xC,
        (
            "……おや、どうしたんだい、\x01",
            "こんな所に固まっちゃって。\x02",
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

    def lambda_85C2():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_85C2)

    def lambda_85CF():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85CF)

    def lambda_85DC():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85DC)

    def lambda_85E9():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_85E9)

    def lambda_85F6():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_85F6)
    WaitChrThread(0xC, 3)

    #C0344
    ChrTalk(
        0xB,
        (
            "#5Pあ、ビヨンドさん、\x01",
            "ちょうどよかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xB,
        (
            "#5Pこちら、例のキーを捜すのを\x01",
            "手伝ってくれてる人たち。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x102,
        "#6P#0100Fどうも、特務支援課の者です。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xC,
        (
            "#11Pあぁ、あの噂の……\x01",
            "どうもこんにちは。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#6P#0309Fよっ、ビヨンド。\x01",
            "相変わらずミリオタってるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        "#11Pランディさんも久しぶりだねぇ。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xB,
        (
            "#5Pそれで……\x01",
            "准尉さんに言われてた起動キー、\x01",
            "そっちにはあった？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 300)

    #C0351
    ChrTalk(
        0xC,
        (
            "#11Pいや、一応探したけど\x01",
            "見つからないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xC,
        (
            "#11P宿の方には来なかったらしいし……\x01",
            "まぁ、こっちには\x01",
            "無いと見ていいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#0005Fえっと……らしい、というのは？\x02\x03",

            "あなたは宿にいたんじゃないんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 300)

    #C0354
    ChrTalk(
        0xC,
        (
            "#11Pや、一応業務が終わってたから、\x01",
            "司令が来てたときは\x01",
            "屋上で休憩してたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xC,
        "#11P……あ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x103,
        "#6P#0205F何か気づいたことでも？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xC,
        (
            "#11Pああ、屋上から戻る途中に\x01",
            "司令とすれ違ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xC,
        (
            "#11P何かキーホルダーみたいなものを\x01",
            "指でくるくる回してたのを\x01",
            "思い出したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xC,
        (
            "#11Pもしかしたらあれが\x01",
            "例のキーだったのかもしれないな。\x02",
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
            "#6P#0006Fということは……\x02\x03",

            "#0001F食堂から屋上に向かうまで、\x01",
            "司令は起動キーを持ってた可能性は\x01",
            "かなり高いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x103,
        (
            "#6P#0203F……重要なものにしては\x01",
            "扱いが乱雑なのが気になりますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#12P#0106F確かに……\x01",
            "でも、貴重な証言が得られたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        (
            "#6P#0309Fハハ、よく思い出したじゃねぇか。\x01",
            "憎いぜ、このこの。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xC,
        (
            "#11Pえ、そうかい？\x01",
            "アハハ……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xB,
        (
            "#5Pあのねぇ……\x01",
            "そういうことは早く言ってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xB,
        (
            "#5P私が食堂を探してたのが\x01",
            "全くの無駄だったんじゃない。\x02",
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
        "#11Pあは、ごめんごめん。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xC,
        (
            "#11Pさーて、僕も仕事に戻らないと。\x01",
            "それじゃあね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C3C():
        OP_95(0xFE, -103000, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8C3C)
    WaitChrThread(0xC, 1)

    def lambda_8C5A():
        OP_95(0xFE, -97850, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8C5A)
    WaitChrThread(0xC, 1)
    OP_68(-104190, 750, 1480, 2000)

    #C0369
    ChrTalk(
        0xB,
        "#5Pちぇ、逃げられちゃった。\x02",
    )

    CloseMessageWindow()

    def lambda_8CAA():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CAA)

    def lambda_8CB7():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CB7)

    def lambda_8CC4():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CC4)

    def lambda_8CD1():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CD1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0370
    ChrTalk(
        0x104,
        (
            "#12P#0300Fまぁ、おかげで\x01",
            "いい手がかりが手に入ったぜ。\x01",
            "ありがとよ、ステラ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 300)

    #C0371
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ、ここにないと分かっただけでも\x01",
            "捜索範囲をかなり絞れそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xB,
        "#5Pどういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "#5Pあたしにはアレが、\x01",
            "どれだけ大事なものか\x01",
            "なんてよくわかんないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xB,
        (
            "#5P准尉さんの為にも、\x01",
            "なんとかキーを見つけて\x01",
            "あげてちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        "#12P#0100Fはい、善処させていただきます。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        "#6P#0203F……では、屋上に向かいましょうか。\x02",
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

    # Function_44_7EE8 end

    def Function_45_8EE5(): pass

    label("Function_45_8EE5")


    def lambda_8EEA():
        OP_95(0xFE, -103000, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8EEA)
    WaitChrThread(0xC, 1)

    def lambda_8F08():
        OP_95(0xFE, -103000, 0, 3500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8F08)
    WaitChrThread(0xC, 1)
    Return()

    # Function_45_8EE5 end

    SaveToFile()

Try(main)
