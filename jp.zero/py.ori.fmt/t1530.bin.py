from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1530.bin",                # FileName
        "t1530",                    # MapName
        "t1530",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("t1530", "t1530_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 5, 0, 7],
    )

    BuildStringList((
        "t1530",                  # 0
        "受付嬢セラ",             # 1
        "クラーク事務長",         # 2
        "看護師ラン",             # 3
        "ラゴー教授",             # 4
        "ラゴー教授",             # 5
        "研修医グェン",           # 6
        "ゲイリー教授",           # 7
        "ゲイリー教授",           # 8
        "研修医シャルール",       # 9
        "ヨアヒム准教授",         # 10
        "診察医ベルダイン",       # 11
        "アーシュラ主任",         # 12
        "アーシュラ主任",         # 13
        "研修医リットン",         # 14
        "アミサ",                 # 15
        "ディーター総裁",         # 16
        "キーンツ",               # 17
        "外来患者",               # 18
        "外来患者",               # 19
        "外来患者",               # 20
        "外来患者",               # 21
        "外来患者",               # 22
        "外来患者",               # 23
        "外来患者",               # 24
        "外来患者",               # 25
        "外来患者",               # 26
        "外来患者",               # 27
        "外来患者",               # 28
        "外来患者",               # 29
        "外来患者",               # 30
        "外来患者",               # 31
        "外来患者",               # 32
        "外来患者",               # 33
        "外来患者",               # 34
        "外来患者",               # 35
        "外来患者",               # 36
        "外来患者",               # 37
        "外来患者",               # 38
        "外来患者",               # 39
        "外来患者",               # 40
        "外来患者",               # 41
        "外来患者",               # 42
        "市民",                   # 43
        "外来患者",               # 44
        "外来患者",               # 45
        "外来患者",               # 46
        "外来患者",               # 47
        "外来患者",               # 48
        "外来患者",               # 49
        "外来患者",               # 50
        "外来患者",               # 51
        "外来患者",               # 52
        "外来患者",               # 53
        "外来患者",               # 54
        "外来患者",               # 55
        "外来患者",               # 56
        "女の子",                 # 57
        "男の子",                 # 58
        "観光客",                 # 59
        "観光客",                 # 60
        "セシル",                 # 61
        "ミショー",               # 62
        "遊撃士リン",             # 63
        "遊撃士エオリア",         # 64
    ))

    AddCharChip((
        "chr/ch05300.itc",                   # 00
        "chr/ch28200.itc",                   # 01
        "chr/ch28000.itc",                   # 02
        "chr/ch29700.itc",                   # 03
        "chr/ch21002.itc",                   # 04
        "chr/ch20002.itc",                   # 05
        "chr/ch20402.itc",                   # 06
        "chr/ch20302.itc",                   # 07
        "chr/ch22300.itc",                   # 08
        "chr/ch29202.itc",                   # 09
        "chr/ch29500.itc",                   # 0A
        "chr/ch32702.itc",                   # 0B
        "chr/ch32800.itc",                   # 0C
        "chr/ch07100.itc",                   # 0D
        "chr/ch29300.itc",                   # 0E
        "chr/ch32900.itc",                   # 0F
        "chr/ch29200.itc",                   # 10
        "chr/ch32700.itc",                   # 11
        "chr/ch29400.itc",                   # 12
        "chr/ch21602.itc",                   # 13
        "chr/ch20600.itc",                   # 14
        "chr/ch22702.itc",                   # 15
        "chr/ch21802.itc",                   # 16
        "chr/ch23702.itc",                   # 17
        "chr/ch23602.itc",                   # 18
        "chr/ch21902.itc",                   # 19
        "chr/ch22202.itc",                   # 1A
        "chr/ch20502.itc",                   # 1B
        "chr/ch22802.itc",                   # 1C
        "chr/ch20102.itc",                   # 1D
        "chr/ch21600.itc",                   # 1E
        "chr/ch24402.itc",                   # 1F
        "chr/ch24502.itc",                   # 20
        "chr/ch32200.itc",                   # 21
        "chr/ch21102.itc",                   # 22
        "chr/ch20602.itc",                   # 23
        "chr/ch20802.itc",                   # 24
        "chr/ch21502.itc",                   # 25
        "chr/ch21702.itc",                   # 26
        "apl/ch50146.itc",                   # 27
        "chr/ch05600.itc",                   # 28
        "apl/ch50385.itc",                   # 29
        "chr/ch24400.itc",                   # 2A
        "chr/ch32000.itc",                   # 2B
        "chr/ch32100.itc",                   # 2C
    ))

    DeclNpc(17209,   0,       7429,    266,  261,  0x0, 0,   1,   0,   0,   0,   1,   1,   255,  0)
    DeclNpc(19739,   0,       4889,    180,  261,  0x0, 0,   2,   0,   0,   0,   1,   3,   255,  0)
    DeclNpc(10539,   0,       -4489,   325,  261,  0x0, 0,   3,   0,   0,   0,   1,   4,   255,  0)
    DeclNpc(55650,   0,       500,     180,  405,  0x0, 0,   16,  0,   0,   0,   1,   6,   255,  0)
    DeclNpc(50979,   119,     59069,   300,  469,  0x0, 0,   9,   0,   255, 255, 1,   7,   255,  0)
    DeclNpc(58849,   0,       58389,   0,    389,  0x0, 0,   10,  0,   0,   0,   1,   8,   255,  0)
    DeclNpc(55650,   0,       -620,    0,    405,  0x0, 0,   17,  0,   0,   0,   1,   9,   255,  0)
    DeclNpc(49930,   119,     -59340,  260,  469,  0x0, 0,   11,  0,   255, 255, 1,   10,  255,  0)
    DeclNpc(60270,   0,       -56930,  90,   389,  0x0, 0,   12,  0,   0,   0,   1,   13,  255,  0)
    DeclNpc(17180,   0,       -4079,   180,  389,  0x0, 0,   13,  0,   0,   0,   1,   14,  255,  0)
    DeclNpc(17180,   0,       -5289,   0,    389,  0x0, 0,   14,  0,   0,   0,   1,   15,  255,  0)
    DeclNpc(56430,   0,       -55270,  90,   389,  0x0, 0,   15,  0,   0,   0,   1,   17,  255,  0)
    DeclNpc(56889,   800,     -58250,  0,    469,  0x0, 0,   39,  0,   255, 255, 1,   18,  255,  0)
    DeclNpc(53970,   0,       51840,   135,  389,  0x0, 0,   18,  0,   0,   0,   1,   19,  255,  0)
    DeclNpc(16049,   100,     -6989,   0,    469,  0x0, 0,   37,  0,   255, 255, 1,   20,  255,  0)
    DeclNpc(14470,   0,       7309,    90,   389,  0x0, 0,   40,  0,   0,   0,   1,   24,  255,  0)
    DeclNpc(14470,   0,       7309,    90,   389,  0x0, 0,   41,  0,   0,   0,   1,   25,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   4,   0,   255, 255, 1,   27,  255,  0)
    DeclNpc(16559,   119,     -9979,   0,    469,  0x0, 0,   5,   0,   255, 255, 1,   28,  255,  0)
    DeclNpc(8340,    119,     9890,    180,  469,  0x0, 0,   6,   0,   255, 255, 1,   29,  255,  0)
    DeclNpc(5000,    119,     4530,    90,   469,  0x0, 0,   7,   0,   255, 255, 1,   30,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   19,  0,   255, 255, 1,   31,  255,  0)
    DeclNpc(21840,   119,     -7219,   270,  469,  0x0, 0,   6,   0,   255, 255, 1,   32,  255,  0)
    DeclNpc(5099,    119,     4739,    90,   469,  0x0, 0,   7,   0,   255, 255, 1,   33,  255,  0)
    DeclNpc(21840,   119,     -4429,   270,  469,  0x0, 0,   21,  0,   255, 255, 1,   34,  255,  0)
    DeclNpc(16799,   119,     -6889,   0,    469,  0x0, 0,   22,  0,   255, 255, 1,   35,  255,  0)
    DeclNpc(7400,    119,     6849,    180,  469,  0x0, 0,   23,  0,   255, 255, 1,   36,  255,  0)
    DeclNpc(2000,    119,     7880,    90,   469,  0x0, 0,   24,  0,   255, 255, 1,   37,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   19,  0,   255, 255, 1,   38,  255,  0)
    DeclNpc(19729,   119,     -9960,   0,    469,  0x0, 0,   5,   0,   255, 255, 1,   39,  255,  0)
    DeclNpc(5110,    119,     5170,    90,   469,  0x0, 0,   25,  0,   255, 255, 1,   40,  255,  0)
    DeclNpc(5110,    119,     4329,    90,   469,  0x0, 0,   26,  0,   255, 255, 1,   41,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   4,   0,   255, 255, 1,   42,  255,  0)
    DeclNpc(18850,   119,     -5050,   270,  469,  0x0, 0,   27,  0,   255, 255, 1,   43,  255,  0)
    DeclNpc(7750,    119,     9800,    180,  469,  0x0, 0,   28,  0,   255, 255, 1,   44,  255,  0)
    DeclNpc(16809,   119,     -6920,   0,    469,  0x0, 0,   6,   0,   255, 255, 1,   45,  255,  0)
    DeclNpc(21840,   119,     -8199,   270,  469,  0x0, 0,   5,   0,   255, 255, 1,   46,  255,  0)
    DeclNpc(21840,   119,     -7449,   270,  469,  0x0, 0,   29,  0,   255, 255, 1,   47,  255,  0)
    DeclNpc(18850,   119,     -4309,   270,  469,  0x0, 0,   31,  0,   255, 255, 1,   48,  255,  0)
    DeclNpc(18850,   119,     -5219,   270,  469,  0x0, 0,   32,  0,   255, 255, 1,   49,  255,  0)
    DeclNpc(7519,    119,     6840,    180,  469,  0x0, 0,   19,  0,   255, 255, 1,   50,  255,  0)
    DeclNpc(21829,   119,     -3789,   270,  469,  0x0, 0,   19,  0,   255, 255, 1,   51,  255,  0)
    DeclNpc(21829,   119,     -4869,   270,  469,  0x0, 0,   34,  0,   255, 255, 1,   52,  255,  0)
    DeclNpc(4989,    119,     5469,    90,   469,  0x0, 0,   5,   0,   255, 255, 1,   54,  255,  0)
    DeclNpc(4989,    119,     4360,    90,   469,  0x0, 0,   7,   0,   255, 255, 1,   55,  255,  0)
    DeclNpc(18819,   119,     -4750,   270,  469,  0x0, 0,   35,  0,   255, 255, 1,   56,  255,  0)
    DeclNpc(19659,   119,     -9970,   0,    469,  0x0, 0,   28,  0,   255, 255, 1,   57,  255,  0)
    DeclNpc(7349,    119,     6849,    180,  469,  0x0, 0,   25,  0,   255, 255, 1,   58,  255,  0)
    DeclNpc(2000,    119,     4139,    90,   469,  0x0, 0,   36,  0,   255, 255, 1,   59,  255,  0)
    DeclNpc(2000,    119,     7510,    90,   469,  0x0, 0,   4,   0,   255, 255, 1,   60,  255,  0)
    DeclNpc(18909,   119,     -4409,   270,  469,  0x0, 0,   34,  0,   255, 255, 1,   61,  255,  0)
    DeclNpc(18909,   119,     -5349,   270,  469,  0x0, 0,   37,  0,   255, 255, 1,   62,  255,  0)
    DeclNpc(16049,   119,     -6989,   0,    469,  0x0, 0,   6,   0,   255, 255, 1,   63,  255,  0)
    DeclNpc(21829,   119,     -4110,   270,  469,  0x0, 0,   32,  0,   255, 255, 1,   64,  255,  0)
    DeclNpc(8069,    119,     9880,    180,  469,  0x0, 0,   19,  0,   255, 255, 1,   65,  255,  0)
    DeclNpc(5099,    119,     4739,    90,   469,  0x0, 0,   38,  0,   255, 255, 1,   66,  255,  0)
    DeclNpc(7250,    0,       -7599,   90,   389,  0x0, 0,   8,   0,   0,   0,   1,   67,  255,  0)
    DeclNpc(7400,    0,       3740,    270,  389,  0x0, 0,   20,  0,   0,   0,   1,   68,  255,  0)
    DeclNpc(18930,   0,       2579,    15,   389,  0x0, 0,   30,  0,   0,   0,   1,   69,  255,  0)
    DeclNpc(2000,    0,       -7670,   90,   389,  0x0, 0,   33,  0,   0,   0,   1,   70,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   1,   22,  255,  0)
    DeclNpc(11579,   0,       5699,    225,  389,  0x0, 0,   42,  0,   0,   4,   1,   71,  255,  0)
    DeclNpc(22700,   0,       1799,    270,  389,  0x0, 0,   43,  0,   0,   0,   1,   72,  255,  0)
    DeclNpc(49849,   0,       58180,   0,    389,  0x0, 0,   44,  0,   0,   0,   1,   73,  255,  0)

    DeclEvent(0x0000, 0, 15,  12.0,                  12.0,                  -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.0,                  -6.0,                  0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 16,  24.93000030517578,     0.1899999976158142,    -0.0,                  20.25,                 [0.23570220172405243,  0.23570235073566437,   -0.0,                  0.0,                   -0.23570235073566437,  0.23570220172405243,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -5.831272602081299,    -5.920843124389648,    0.0,                   1.0])

    DeclActor(16000,   0,       7000,    2000,    17210,   1500,    7430,    0x007E, 1,  0,  0x0000)
    DeclActor(19680,   0,       3710,    2000,    19740,   1500,    4890,    0x007E, 1,  2,  0x0000)
    DeclActor(65800,   0,       2430,    1200,    65800,   1500,    2430,    0x007C, 0,  17, 0x0000)

    ScpFunction((
        "Function_0_9BC",          # 00, 0
        "Function_1_A74",          # 01, 1
        "Function_2_A8C",          # 02, 2
        "Function_3_B3D",          # 03, 3
        "Function_4_B68",          # 04, 4
        "Function_5_B93",          # 05, 5
        "Function_6_1131",         # 06, 6
        "Function_7_1138",         # 07, 7
        "Function_8_11DB",         # 08, 8
        "Function_9_13C6",         # 09, 9
        "Function_10_2000",        # 0A, 10
        "Function_11_22D4",        # 0B, 11
        "Function_12_2365",        # 0C, 12
        "Function_13_2A2F",        # 0D, 13
        "Function_14_2A8E",        # 0E, 14
        "Function_15_2F9A",        # 0F, 15
        "Function_16_2FEE",        # 10, 16
        "Function_17_3042",        # 11, 17
    ))


    def Function_0_9BC(): pass

    label("Function_0_9BC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9FC"),
        (1, "loc_A08"),
        (2, "loc_A14"),
        (3, "loc_A20"),
        (4, "loc_A2C"),
        (5, "loc_A38"),
        (6, "loc_A44"),
        (SWITCH_DEFAULT, "loc_A50"),
    )


    label("loc_9FC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A08")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A14")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A20")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A2C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A38")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A44")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A50")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A73")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A73")

    Return()

    # Function_0_9BC end

    def Function_1_A74(): pass

    label("Function_1_A74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8B")
    OP_A1(0xFE, 0x4B0, 0x0)
    ExitThread()
    Jump("Function_1_A74")

    label("loc_A8B")

    Return()

    # Function_1_A74 end

    def Function_2_A8C(): pass

    label("Function_2_A8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3C")
    OP_95(0xFE, 7400, 0, -1600, 1500, 0x0)
    OP_95(0xFE, 7400, 0, 1420, 1500, 0x0)
    OP_95(0xFE, 10380, 0, 4530, 1500, 0x0)
    OP_95(0xFE, 13330, 0, 4550, 1500, 0x0)
    OP_95(0xFE, 16420, 0, 1470, 1500, 0x0)
    OP_95(0xFE, 16420, 0, -1430, 1500, 0x0)
    OP_95(0xFE, 13440, 0, -4490, 1500, 0x0)
    OP_95(0xFE, 10540, 0, -4490, 1500, 0x0)
    Jump("Function_2_A8C")

    label("loc_B3C")

    Return()

    # Function_2_A8C end

    def Function_3_B3D(): pass

    label("Function_3_B3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B67")
    OP_94(0xFE, 0x1932, 0x148C, 0x1DBA, 0xDCA, 0x3E8)
    Sleep(400)
    Jump("Function_3_B3D")

    label("loc_B67")

    Return()

    # Function_3_B3D end

    def Function_4_B68(): pass

    label("Function_4_B68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B92")
    OP_94(0xFE, 0x26D4, 0xBCC, 0x34EE, 0x235A, 0x3E8)
    Sleep(300)
    Jump("Function_4_B68")

    label("loc_B92")

    Return()

    # Function_4_B68 end

    def Function_5_B93(): pass

    label("Function_5_B93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BAB")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 6)

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C19")
    SetChrPos(0xA, 16050, 0, -5480, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 56790, 0, 5200, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 57420, 0, -56730, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    Jump("loc_10DC")

    label("loc_C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_C60")
    SetChrPos(0xA, 59030, 0, -1090, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    Jump("loc_10DC")

    label("loc_C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C9C")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    Jump("loc_10DC")

    label("loc_C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CFE")
    SetChrPos(0xA, 17630, 0, -4730, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6660, 0, -5660, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x45, 0x80)
    Jump("loc_10DC")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_D55")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6660, 0, -5660, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    Jump("loc_10DC")

    label("loc_D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_DA7")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6660, 0, -5660, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    Jump("loc_10DC")

    label("loc_DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E11")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 51570, 0, 57430, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 49240, 0, 59850, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 48750, 0, -59740, 180)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x43, 0x80)
    Jump("loc_10DC")

    label("loc_E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E90")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 56790, 0, 5200, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 54470, 0, -4240, 0)
    ClearChrFlags(0x44, 0x80)
    SetChrPos(0x44, 8160, 0, 400, 180)
    SetChrPos(0xA, 8160, 0, -630, 0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x42, 0x80)
    Jump("loc_10DC")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_ED2")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    BeginChrThread(0x13, 0, 0, 1)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    Jump("loc_10DC")

    label("loc_ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F19")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    BeginChrThread(0x13, 0, 0, 1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_10DC")

    label("loc_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_F55")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_10DC")

    label("loc_F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FE3")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, 16050, 0, -5480, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 48580, 0, -59600, 90)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x41, 0x80)
    BeginChrThread(0x41, 0, 0, 3)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    SetChrPos(0xB, 49790, 0, 59830, 180)
    Jump("loc_10DC")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_101C")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 56870, 0, 2560, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_10DC")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1058")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_10DC")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_10A4")
    SetChrPos(0xA, 9660, 0, 2050, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x40, 0x80)
    Jump("loc_10DC")

    label("loc_10A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_10DC")
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 17680, 0, -3850, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)

    label("loc_10DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F7")
    Event(0, 8)
    SetMapFlags(0x10000000)
    Jump("loc_110D")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110D")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_110D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1121")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 12)
    Jump("loc_1130")

    label("loc_1121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1130")
    ClearScenarioFlags(0x5C, 1)
    Event(1, 77)

    label("loc_1130")

    Return()

    # Function_5_B93 end

    def Function_6_1131(): pass

    label("Function_6_1131")

    Sound(160, 0, 100, 0)
    Return()

    # Function_6_1131 end

    def Function_7_1138(): pass

    label("Function_7_1138")

    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1151")
    Jump("loc_1169")

    label("loc_1151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1169")
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_1169")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118B")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_118B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11A7")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_11DA")

    label("loc_11A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_11DA")

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_11DA")

    Return()

    # Function_7_1138 end

    def Function_8_11DB(): pass

    label("Function_8_11DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(20530, 1000, 0, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 2200, 0, -700, 90)
    SetChrPos(0x102, 2200, 0, 600, 90)
    SetChrPos(0x103, 900, 0, -700, 90)
    SetChrPos(0x104, 900, 0, 600, 90)
    OP_68(4000, 1000, 0, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(2520, 1000, -280, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21610, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#6P#0000Fよかった……\x01",
            "それほど混んでなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#0104F#5Pそうね……混んでいる時は\x01",
            "待合席が一杯になるものね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1327():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1327)
    WaitChrThread(0x102, 1)
    Sleep(300)

    #C0003
    ChrTalk(
        0x102,
        (
            "#0100F#5P早速、お姉さんのこと\x01",
            "受付で聞いてみる？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1371():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1371)
    WaitChrThread(0x101, 1)

    #C0004
    ChrTalk(
        0x101,
        "#12P#0000Fああ、呼び出してもらおう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1500, 0, -100, 90)
    SetScenarioFlags(0x61, 7)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_8_11DB end

    def Function_9_13C6(): pass

    label("Function_9_13C6")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50014.itc", 0x3C)
    LoadChrToIndex("apl/ch50102.itc", 0x3D)
    OP_4B(0x8, 0xFF)
    OP_68(15690, 600, 7270, 0)
    MoveCamera(51, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 14410, 0, 6710, 90)
    SetChrPos(0x102, 14130, 0, 5550, 90)
    SetChrPos(0x103, 12820, 0, 5690, 90)
    SetChrPos(0x104, 13070, 0, 6870, 90)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    ClearChrFlags(0x44, 0x4)
    ClearChrFlags(0x44, 0x80)
    OP_4B(0x44, 0xFF)
    SetChrPos(0x44, 12000, 1050, 13300, 180)
    OP_A7(0x44, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(22630, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0005
    ChrTalk(
        0x8,
        "#11Pようこそ、ウルスラ病院へ。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#11P今日は外来ですか？\x01",
            "それともお見舞いでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0005F#6Pあ、いえ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x3C)
    SetChrSubChip(0x101, 0x3)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0000F#6Pクロスベル警察、特務支援課の\x01",
            "ロイド・バニングスといいます。\x02\x03",

            "今日は、捜査任務のために\x01",
            "こちらに伺わせていただきました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x8,
        "#11Pあ、警察の方だったんですか。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#11P捜査と言いますと……\x01",
            "やはり例の魔獣騒ぎでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0011
    ChrTalk(
        0x101,
        (
            "#0003F#6Pええ……\x01",
            "自分たちの方でも調べるように\x01",
            "警備隊から要請がありまして。\x02\x03",

            "#0001F関係者に一通り\x01",
            "話を聞かせていただければと。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "#11Pふふ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#11Pそうですね、病院長は留守ですし、\x01",
            "看護師長をお呼びしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0014
    ChrTalk(
        0x101,
        (
            "#0011F#6Pそ、その……実はですね。\x02\x03",

            "個人的な知り合いが\x01",
            "こちらに勤めていまして……\x02\x03",

            "#0012Fその人がお忙しくなければ、\x01",
            "案内してもらおうと思いまして……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0xFFFF)

    #C0015
    ChrTalk(
        0x103,
        "#0202F#6P（何だか緊張してますね……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0016
    ChrTalk(
        0x104,
        (
            "#0301F（そりゃ、ナースのお姉さんで\x01",
            "  美人とくりゃ緊張もするだろ！）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0017
    ChrTalk(
        0x102,
        "#0106F#11P（それは貴方だけでしょう……）\x02",
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x44,
        "女性の声",
        "──ロイド？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrFlags(0x1B, 0x80)

    def lambda_1967():
        TurnDirection(0xFE, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1967)

    def lambda_1974():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1974)
    Sleep(100)

    def lambda_1984():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1984)

    def lambda_1991():
        TurnDirection(0xFE, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1991)

    def lambda_199E():
        TurnDirection(0xFE, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_199E)
    OP_68(14050, 600, 9110, 3000)
    MoveCamera(30, 18, 0, 3000)

    def lambda_19C7():
        OP_95(0xFE, 11970, 0, 10920, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_19C7)
    Sleep(200)

    def lambda_19E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_19E4)
    WaitChrThread(0x44, 1)
    WaitChrThread(0x44, 2)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
    Sleep(500)

    #N0019
    NpcTalk(
        0x44,
        "看護師の女性",
        "#1305F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0005F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0305F#6Pおおっ……！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#0105F#12P……綺麗な人……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#0205F#6P……ぐらまーです……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "#2Pあら、セシルさん。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "#2Pちょうど良かった。\x01",
            "こちらは警察の方だそうで……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(13560, 600, 9860, 1500)

    def lambda_1B2A():
        OP_95(0xFE, 12960, 0, 8710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B2A)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)

    def lambda_1B4A():
        TurnDirection(0x102, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B4A)

    def lambda_1B57():
        TurnDirection(0x103, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B57)
    Sleep(100)

    def lambda_1B67():
        TurnDirection(0x104, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B67)

    #C0026
    ChrTalk(
        0x101,
        (
            "#0011F#12Pえっと……その。\x02\x03",

            "#0009Fいきなりゴメン……\x01",
            "先に連絡すればよかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x44,
        "#1301F#5P…………っ………………\x02",
    )

    CloseMessageWindow()
    OP_68(13660, 600, 9340, 500)
    SetChrFlags(0x44, 0x40)

    def lambda_1C06():
        OP_95(0xFE, 12750, 0, 9200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_1C06)
    WaitChrThread(0x44, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)

    def lambda_1C35():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C35)
    SetCameraDistance(22130, 0)
    SetChrChipByIndex(0x44, 0x3D)
    SetChrSubChip(0x44, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0028
    ChrTalk(
        0x101,
        "#0011F#12Pちょ、セシル姉……！？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x44,
        (
            "#1304F#5P#40Wやっと……やっと会えたわね。\x02\x03",

            "お帰りなさい……\x01",
            "本当に久しぶりね、ロイド……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0002F#12Pう、うん……\x02\x03",

            "#0004F会いにいけなくてゴメン。\x01",
            "しばらくずっと忙しくてさ……\x02\x03",

            "#0011Fそ、それより、さすがに少し\x01",
            "恥ずかしすぎるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x44,
        (
            "#1304F#5P#30W……いいからこのまま\x01",
            "お姉ちゃんに抱きしめられてなさい。\x02\x03",

            "#1302Fふふっ……\x01",
            "背もこんなに高くなって……\x02\x03",

            "前に別れた時は\x01",
            "私と同じくらいだったのにね……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0012F#12Pそ、そりゃあ、\x01",
            "育ち盛りの３年間だったし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0033
    ChrTalk(
        0x8,
        "#2Pあ、あの～……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0109F#4P（な、何て言うか……）\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#0206F#12P（想像以上に甘々ですね……）\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#0307F#6P（おのれロイド……！\x01",
            "  あんな素敵なお姉さんを……！）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(23130, 3000)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x5C, 0)
    NewScene("t1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_13C6 end

    def Function_10_2000(): pass

    label("Function_10_2000")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_68(2200, 1000, -100, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24440, 0)
    OP_68(3670, 1000, 220, 3000)
    SetChrPos(0x136, 1800, 0, -100, 90)
    SetChrPos(0x101, 0, 0, -700, 90)
    SetChrPos(0x102, 0, 0, 600, 90)
    SetChrPos(0x103, 0, 0, -700, 90)
    SetChrPos(0x104, 0, 0, 600, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20DA():
        OP_96(0xFE, 0x1130, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_20DA)
    Sleep(600)

    def lambda_20F7():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20F7)

    def lambda_2111():
        OP_96(0xFE, 0x898, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2111)

    def lambda_212B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_212B)

    def lambda_213C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_213C)
    Sleep(1200)

    def lambda_2150():
        OP_96(0xFE, 0x384, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2150)

    def lambda_216A():
        OP_96(0xFE, 0x384, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_216A)

    def lambda_2184():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2184)

    def lambda_2195():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2195)
    WaitChrThread(0x136, 1)

    def lambda_21AA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_21AA)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_0D()

    #C0037
    ChrTalk(
        0x136,
        (
            "#1300F#11Pこの病棟という建物の\x01",
            "２階と３階は病室になっているの。\x02\x03",

            "被害にあった研修医の人は\x01",
            "２階の病室にいるから案内するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#0000F#6Pうん、よろしく。\x02",
    )

    CloseMessageWindow()

    def lambda_226F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_226F)
    WaitChrThread(0x136, 1)
    OP_68(11450, 1000, 7080, 12000)
    BeginChrThread(0x136, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 11)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x65, 6)
    SetScenarioFlags(0x5C, 0)
    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2000 end

    def Function_11_22D4(): pass

    label("Function_11_22D4")


    def lambda_22D9():
        OP_95(0xFE, 4400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22D9)
    WaitChrThread(0xFE, 1)

    def lambda_22F7():
        OP_95(0xFE, 11980, 0, 6820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22F7)
    WaitChrThread(0xFE, 1)

    def lambda_2315():
        OP_95(0xFE, 11760, 0, 10650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2315)
    WaitChrThread(0xFE, 1)

    def lambda_2333():
        OP_95(0xFE, 12190, 140, 12390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2333)
    Sleep(500)

    def lambda_2350():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2350)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_22D4 end

    def Function_12_2365(): pass

    label("Function_12_2365")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17660, 1000, 7870, 0)
    MoveCamera(66, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26750, 0)
    SetChrPos(0x101, 14410, 0, 6710, 45)
    SetChrPos(0x153, 12450, 0, 6560, 45)
    SetChrPos(0xEF, 11920, 0, 5340, 45)
    OP_4B(0x44, 0xFF)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    SetChrPos(0x44, 13290, 0, 8050, 90)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 20770, 0, 9100, 45)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(25000, 2500)
    OP_6F(0x10)
    OP_0D()

    #C0039
    ChrTalk(
        0x8,
        "#5P……はい、はい。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#5P分かりました。\x01",
            "それでは研究室へお通しします。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    OP_68(16430, 1000, 7320, 2500)

    def lambda_2491():
        OP_95(0xFE, 17210, 0, 7430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2491)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    #C0041
    ChrTalk(
        0x8,
        (
            "#5Pヨアヒム先生なら\x01",
            "丁度時間が空いているそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#5P研究棟にある研究室まで\x01",
            "直接お越しくださいとの事でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#0004F#6Pそうですか……良かった。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x44, 0x153, 500)
    Sleep(300)

    #C0044
    ChrTalk(
        0x44,
        (
            "#1302F#5Pふふ、それじゃあ私は\x01",
            "このあたりで失礼するわね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2598():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2598)
    Sleep(50)

    def lambda_25A8():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_25A8)
    Sleep(50)

    def lambda_25B8():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_25B8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x153, 1)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0002F#11Pうん、ありがとう。\x01",
            "帰る時にまた声をかけるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x44,
        (
            "#1302F#5Pふふ、分かったわ。\x02\x03",

            "#1309Fキーアちゃん、また後でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x153,
        "#1109F#12Pうんっ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x44, 0x0, 0x1F4)
    OP_68(15600, 1000, 9190, 3000)

    def lambda_2681():

        label("loc_2681")

        TurnDirection(0x101, 0x44, 500)
        Yield()
        Jump("loc_2681")

    QueueWorkItem2(0x101, 1, lambda_2681)

    def lambda_2693():

        label("loc_2693")

        TurnDirection(0xEF, 0x44, 500)
        Yield()
        Jump("loc_2693")

    QueueWorkItem2(0xEF, 1, lambda_2693)

    def lambda_26A5():

        label("loc_26A5")

        TurnDirection(0x153, 0x44, 500)
        Yield()
        Jump("loc_26A5")

    QueueWorkItem2(0x153, 1, lambda_26A5)

    def lambda_26B7():

        label("loc_26B7")

        TurnDirection(0x8, 0x44, 500)
        Yield()
        Jump("loc_26B7")

    QueueWorkItem2(0x8, 1, lambda_26B7)
    BeginChrThread(0x44, 3, 0, 13)
    WaitChrThread(0x44, 3)
    OP_6F(0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x153, 0x1)
    EndChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2712")

    #C0048
    ChrTalk(
        0x102,
        "#0100F相変わらず忙しそうね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_277C")

    label("loc_2712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2746")

    #C0049
    ChrTalk(
        0x103,
        "#0200F相変わらず忙しそうです……\x02",
    )

    CloseMessageWindow()
    Jump("loc_277C")

    label("loc_2746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_277C")

    #C0050
    ChrTalk(
        0x104,
        (
            "#0300Fは～……\x01",
            "相変わらず忙しそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_277C")


    #C0051
    ChrTalk(
        0x8,
        (
            "#11Pふふ、この病院で\x01",
            "セシルさんほどの働き者は\x01",
            "ちょっといませんから……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#11Pサボりがちな先生方にも\x01",
            "見習って欲しいくらいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#0012F#5Pはは……\x02\x03",

            "#0000F（あんまり無理をして\x01",
            "  欲しくはないんだけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(16430, 1000, 7320, 1500)
    TurnDirection(0x8, 0x101, 500)
    OP_6F(0x1)

    #C0054
    ChrTalk(
        0x8,
        (
            "#5Pそういえば……\x01",
            "ヨアヒム先生の研究室は\x01",
            "ご存知でしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#5P研究棟の４階ですけど、\x01",
            "よかったら案内しましょうか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2902():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2902)
    Sleep(50)

    def lambda_2912():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2912)
    Sleep(50)

    def lambda_2922():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_2922)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x153, 1)

    #C0056
    ChrTalk(
        0x101,
        "#0002F#6Pいや、多分大丈夫だと思います。\x02",
    )

    CloseMessageWindow()

    def lambda_2968():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2968)
    Sleep(50)

    def lambda_2978():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2978)
    Sleep(50)

    def lambda_2988():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_2988)
    Sleep(300)

    #C0057
    ChrTalk(
        0x101,
        (
            "#0000F#5Pよし、それじゃあ\x01",
            "その先生に会いに行こうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x153,
        "#1110F#6Pうん、行こうー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0x44, 0xFF)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x0, 14000, 0, 6500, 90)
    SetScenarioFlags(0xA8, 5)
    OP_29(0x48, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_12_2365 end

    def Function_13_2A2F(): pass

    label("Function_13_2A2F")


    def lambda_2A34():
        OP_95(0xFE, 11960, 0, 11140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A34)
    WaitChrThread(0xFE, 1)

    def lambda_2A52():
        OP_95(0xFE, 12060, 1030, 13280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A52)
    Sleep(250)

    def lambda_2A6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A6F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_13_2A2F end

    def Function_14_2A8E(): pass

    label("Function_14_2A8E")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(16430, 800, 7320, 0)
    MoveCamera(66, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 14410, 0, 6710, 45)
    SetChrPos(0x102, 12450, 0, 6560, 45)
    SetChrPos(0x103, 11920, 0, 5340, 45)
    SetChrPos(0x104, 13560, 0, 5070, 45)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_0D()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5Pあら、皆さん。\x01",
            "セシルさんに御用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0005F#6Pあ、いえ……\x02\x03",

            "#0000F実はまた、ヨアヒム先生に\x01",
            "相談したい事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#0100F#6Pお時間がもらえないか\x01",
            "問い合わせて頂けませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        "#5Pええ、お安い御用です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    OP_68(17660, 800, 7870, 3000)

    def lambda_2C16():
        OP_95(0xFE, 20770, 0, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C16)
    WaitChrThread(0x8, 1)
    Sound(807, 0, 100, 0)
    OP_6F(0x1)

    #C0063
    ChrTalk(
        0x8,
        (
            "#5Pあ、ヨアヒム先生。\x01",
            "いらっしゃいましたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#5P先生にご来客ですけど\x01",
            "今、お時間は……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#5Pえ、都合が悪い？\x01",
            "何か診察や研究でも……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "#5P──ああ、分かりました。\x01",
            "釣りに行くおつもりですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#5Pダメです、勤務時間中は\x01",
            "きちんと仕事をしてください。\x02",
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
    Sleep(1000)

    #C0068
    ChrTalk(
        0x101,
        "#0012F#6P（相変わらずみたいだな……）\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        (
            "#0211F#6P#N（普段はとても優秀な\x01",
            "  医師みたいですけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5Pええ、支援課の\x01",
            "ロイドさんたちです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        "#5P……はい、はい……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "#5Pでは、このまま\x01",
            "研究室にお通ししますね。\x02",
        )
    )

    CloseMessageWindow()
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_93(0x8, 0xE1, 0x1F4)
    OP_68(16430, 800, 7320, 2300)

    def lambda_2EAB():
        OP_95(0xFE, 17210, 0, 7430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2EAB)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    #C0073
    ChrTalk(
        0x8,
        (
            "#5Pヨアヒム先生が\x01",
            "お会いになるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        "#5Pどうぞ、研究棟の方へ。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#0002F#6Pど、どうも。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0309F#12Pハハ、お手数を\x01",
            "かけちまったみてぇだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 14000, 0, 6500, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0xC3, 3)
    OP_29(0x4C, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_14_2A8E end

    def Function_15_2F9A(): pass

    label("Function_15_2F9A")

    EventBegin(0x1)

    #C0077
    ChrTalk(
        0x101,
        (
            "#0003F……まずは受付で\x01",
            "セシル姉を呼び出してもらおう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11400, 0, 9830, 180)
    EventEnd(0x4)
    Return()

    # Function_15_2F9A end

    def Function_16_2FEE(): pass

    label("Function_16_2FEE")

    EventBegin(0x1)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0003F……まずは受付で\x01",
            "セシル姉を呼び出してもらおう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 21960, 0, -230, 270)
    EventEnd(0x4)
    Return()

    # Function_16_2FEE end

    def Function_17_3042(): pass

    label("Function_17_3042")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0079
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　ＩＣＵ（集中治療室）\x01",
            "許可なき者の立ち入りを禁ずる。\x01",
            "※入室者はレベル２以上の\x01",
            "  滅菌処理を行ってください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_3042 end

    SaveToFile()

Try(main)
