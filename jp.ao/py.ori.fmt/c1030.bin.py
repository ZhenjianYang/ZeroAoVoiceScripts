from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1030.bin",                # FileName
        "c1030",                    # MapName
        "c1030",                    # Location
        0x0012,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 18, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1030",                  # 0
        "チャンホイ",             # 1
        "フェン",                 # 2
        "サンサン",               # 3
        "パック",                 # 4
        "ルース",                 # 5
        "グリッド",               # 6
        "ボンド",                 # 7
        "クレイユ",               # 8
        "サニータ",               # 9
        "マリー",                 # 10
        "観光客",                 # 11
        "観光客",                 # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "記者ノティシア",         # 15
        "グレイス",               # 16
        "レインズ",               # 17
        "夫人",                   # 18
        "男の子",                 # 19
        "市民",                   # 20
        "リーシャ",               # 21
        "シスター・リース",       # 22
        "アルム",                 # 23
        "エアリー",               # 24
        "アレクセイ隊員",         # 25
        "クロンク",               # 26
        "ディンズ",               # 27
        "リリィ",                 # 28
        "マルテ",                 # 29
        "ツァオ",                 # 30
        "ラウ",                   # 31
        "ニールセン",             # 32
        "レクター",               # 33
        "食器",                   # 34
        "食器",                   # 35
        "食器",                   # 36
        "食器",                   # 37
        "食器",                   # 38
        "食器",                   # 39
    ))

    AddCharChip((
        "chr/ch31600.itc",                   # 00
        "chr/ch25100.itc",                   # 01
        "chr/ch32500.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch20400.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch27602.itc",                   # 06
        "chr/ch33302.itc",                   # 07
        "chr/ch34402.itc",                   # 08
        "chr/ch39000.itc",                   # 09
        "chr/ch20002.itc",                   # 0A
        "chr/ch20102.itc",                   # 0B
        "chr/ch20202.itc",                   # 0C
        "chr/ch20302.itc",                   # 0D
        "chr/ch47900.itc",                   # 0E
        "chr/ch32300.itc",                   # 0F
        "chr/ch20302.itc",                   # 10
        "chr/ch23002.itc",                   # 11
        "chr/ch22802.itc",                   # 12
        "chr/ch14002.itc",                   # 13
        "chr/ch46300.itc",                   # 14
        "chr/ch46200.itc",                   # 15
        "chr/ch31302.itc",                   # 16
        "chr/ch06002.itc",                   # 17
        "chr/ch28102.itc",                   # 18
        "chr/ch47902.itc",                   # 19
        "chr/ch45100.itc",                   # 1A
        "chr/ch23500.itc",                   # 1B
        "chr/ch20400.itc",                   # 1C
        "chr/ch24800.itc",                   # 1D
        "chr/ch24900.itc",                   # 1E
        "chr/ch06302.itc",                   # 1F
        "chr/ch31402.itc",                   # 20
        "chr/ch32502.itc",                   # 21
        "chr/ch45102.itc",                   # 22
        "chr/ch47902.itc",                   # 23
        "chr/ch05202.itc",                   # 24
    ))

    DeclNpc(16000,   0,       15989,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(12329,   0,       15989,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(12310,   0,       -1990,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(16030,   0,       6050,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(17909,   0,       8399,    90,   261,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(7130,    150,     -1480,   180,  325,  0x0, 0,   3,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(10550,   100,     3140,    270,  453,  0x0, 0,   6,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(8850,    0,       4840,    180,  453,  0x0, 0,   7,   0,   255, 255, 0,   26,  255,  0)
    DeclNpc(7150,    100,     3140,    90,   453,  0x0, 0,   8,   0,   255, 255, 0,   27,  255,  0)
    DeclNpc(7329,    29,      4590,    165,  389,  0x0, 0,   9,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  453,  0x0, 0,   10,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(7159,    29,      3200,    90,   453,  0x0, 0,   11,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(4940,    150,     7130,    270,  453,  0x0, 0,   12,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(1620,    150,     7320,    90,   453,  0x0, 0,   13,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(14090,   0,       -119,    90,   453,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  389,  0x0, 0,   23,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(7159,    100,     3200,    90,   389,  0x0, 0,   24,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  453,  0x0, 0,   16,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(7159,    150,     3200,    90,   453,  0x0, 0,   17,  0,   255, 255, 0,   39,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  453,  0x0, 0,   18,  0,   255, 255, 0,   41,  255,  0)
    DeclNpc(14000,   50,      0,       90,   453,  0x0, 0,   36,  0,   255, 255, 0,   47,  255,  0)
    DeclNpc(14090,   0,       -119,    90,   453,  0x0, 0,   19,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(-100800, 29,      -55490,  90,   389,  0x0, 0,   20,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(-99599,  29,      -55490,  270,  389,  0x0, 0,   21,  0,   0,   0,   0,   43,  255,  0)
    DeclNpc(13949,   150,     2900,    90,   453,  0x0, 0,   22,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(8819,    0,       8770,    225,  389,  0x0, 0,   28,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(8930,    0,       6710,    90,   389,  0x0, 0,   29,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(9939,    0,       6710,    270,  389,  0x0, 0,   30,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(7599,    0,       8909,    225,  389,  0x0, 0,   27,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  389,  0x0, 0,   31,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(9029,    150,     5059,    180,  389,  0x0, 0,   32,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-46520,  200,     -52250,  180,  453,  0x0, 0,   34,  0,   255, 255, 0,   44,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14590,   0,       4630,    1000,    16030,   1500,    6050,    0x007E, 0,  5,  0x0000)

    ChipFrameInfo(1652, 0)                                       # 0

    ScpFunction((
        "Function_0_674",          # 00, 0
        "Function_1_72C",          # 01, 1
        "Function_2_880",          # 02, 2
        "Function_3_A2C",          # 03, 3
        "Function_4_12D0",         # 04, 4
        "Function_5_1442",         # 05, 5
        "Function_6_1556",         # 06, 6
        "Function_7_36E9",         # 07, 7
        "Function_8_45EC",         # 08, 8
        "Function_9_4706",         # 09, 9
        "Function_10_5B58",        # 0A, 10
        "Function_11_5BFF",        # 0B, 11
        "Function_12_5E5C",        # 0C, 12
        "Function_13_5F76",        # 0D, 13
        "Function_14_6C18",        # 0E, 14
        "Function_15_6D32",        # 0F, 15
        "Function_16_7C4E",        # 10, 16
        "Function_17_89E7",        # 11, 17
        "Function_18_8A45",        # 12, 18
        "Function_19_8A7F",        # 13, 19
        "Function_20_8AA0",        # 14, 20
        "Function_21_8B19",        # 15, 21
        "Function_22_8D18",        # 16, 22
        "Function_23_95D4",        # 17, 23
        "Function_24_9964",        # 18, 24
        "Function_25_9ACC",        # 19, 25
        "Function_26_9B2E",        # 1A, 26
        "Function_27_9C70",        # 1B, 27
        "Function_28_9CE8",        # 1C, 28
        "Function_29_9D09",        # 1D, 29
        "Function_30_A2C0",        # 1E, 30
        "Function_31_A376",        # 1F, 31
        "Function_32_A410",        # 20, 32
        "Function_33_A5C7",        # 21, 33
        "Function_34_A6F5",        # 22, 34
        "Function_35_ACFB",        # 23, 35
        "Function_36_ADB3",        # 24, 36
        "Function_37_AE5D",        # 25, 37
        "Function_38_BA8D",        # 26, 38
        "Function_39_BD93",        # 27, 39
        "Function_40_BF2E",        # 28, 40
        "Function_41_C1F7",        # 29, 41
        "Function_42_C2D5",        # 2A, 42
        "Function_43_C3EC",        # 2B, 43
        "Function_44_C527",        # 2C, 44
        "Function_45_C543",        # 2D, 45
        "Function_46_C6F7",        # 2E, 46
        "Function_47_C7EE",        # 2F, 47
        "Function_48_C8C7",        # 30, 48
        "Function_49_D1BA",        # 31, 49
        "Function_50_E209",        # 32, 50
        "Function_51_EE8E",        # 33, 51
        "Function_52_EEBF",        # 34, 52
        "Function_53_FE7D",        # 35, 53
        "Function_54_105E0",       # 36, 54
        "Function_55_10E6B",       # 37, 55
        "Function_56_110A9",       # 38, 56
    ))


    def Function_0_674(): pass

    label("Function_0_674")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_6B4"),
        (1, "loc_6C0"),
        (2, "loc_6CC"),
        (3, "loc_6D8"),
        (4, "loc_6E4"),
        (5, "loc_6F0"),
        (6, "loc_6FC"),
        (SWITCH_DEFAULT, "loc_708"),
    )


    label("loc_6B4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6C0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6CC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6D8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6E4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6F0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_708")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_714")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_72B")

    Return()

    # Function_0_674 end

    def Function_1_72C(): pass

    label("Function_1_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87F")
    OP_95(0xFE, 7200, 0, 370, 1000, 0x0)
    OP_95(0xFE, 7280, 30, 1390, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_95(0xFE, 5850, 0, 1930, 1000, 0x0)
    OP_95(0xFE, 4730, 0, 3700, 1000, 0x0)
    OP_95(0xFE, 4840, 0, 5570, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 5660, 0, 5540, 1000, 0x0)
    OP_95(0xFE, 10470, 0, 10350, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1200)
    OP_95(0xFE, 12980, 0, 7230, 1000, 0x0)
    OP_95(0xFE, 12730, 0, 2100, 1000, 0x0)
    OP_95(0xFE, 13200, 0, 1420, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1600)
    OP_95(0xFE, 12280, 0, 680, 1000, 0x0)
    OP_95(0xFE, 11230, 0, 110, 1000, 0x0)
    OP_95(0xFE, 8930, 30, -1570, 1000, 0x0)
    Sleep(1400)
    OP_95(0xFE, 8720, 0, -510, 1000, 0x0)
    Jump("Function_1_72C")

    label("loc_87F")

    Return()

    # Function_1_72C end

    def Function_2_880(): pass

    label("Function_2_880")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A2B")
    OP_95(0xFE, -62990, 0, 1230, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -60190, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -57400, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -50960, 0, 1190, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x190)
    OP_95(0xFE, -57400, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x190)
    OP_95(0xFE, -60190, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x190)
    OP_95(0xFE, -62990, 0, 1230, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -65030, 0, 1190, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(300)
    Jump("Function_2_880")

    label("loc_A2B")

    Return()

    # Function_2_880 end

    def Function_3_A2C(): pass

    label("Function_3_A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5E")
    SetMapFlags(0x10000000)
    Event(0, 50)
    Jump("loc_A8B")

    label("loc_A5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8B")
    SetMapFlags(0x10000000)
    Event(0, 49)

    label("loc_A8B")

    SetChrChipByIndex(0xD, 0x3)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B04")
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0x25, 0x80)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    EndChrThread(0x25, 0x0)
    SetChrBattleFlags(0x25, 0x4)
    ClearChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    EndChrThread(0x26, 0x0)
    SetChrBattleFlags(0x26, 0x4)
    Jump("loc_12CF")

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B9C")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x23, 0x10)
    SetChrPos(0x8, 5670, 0, 11670, 225)
    SetChrPos(0x9, 6460, 0, 10550, 225)
    SetChrPos(0xA, 10860, 0, -1600, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xD, 0x80)
    Jump("loc_12CF")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BEE")
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -103850, 0, -53460, 180)
    Jump("loc_12CF")

    label("loc_BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CD1")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C17")
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)

    label("loc_C17")

    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C77")
    SetChrPos(0xA, 13000, 400, -5170, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    EndChrThread(0xA, 0x0)
    Jump("loc_C88")

    label("loc_C77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C88")
    SetChrFlags(0xA, 0x80)

    label("loc_C88")

    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x12)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    SetChrPos(0xB, 12330, 0, 15990, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_12CF")

    label("loc_CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D39")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_12CF")

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E13")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x27, 0x10)
    SetChrPos(0x16, -46690, 200, -56110, 0)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0E")
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0xA, 16120, 0, -40, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)

    label("loc_E0E")

    Jump("loc_12CF")

    label("loc_E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E7B")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_12CF")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F36")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xA, 16030, 0, 6050, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xB, 12310, 0, -1990, 225)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 16000, 0, 15990, 0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x8, 17080, 0, 15430, 315)
    BeginChrThread(0x8, 0, 0, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    Jump("loc_12CF")

    label("loc_F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FF6")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x13)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -96120, 150, -52330, 180)
    SetChrChipByIndex(0x16, 0x19)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_12CF")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1063")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_12CF")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10FC")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x17, 0x17)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrChipByIndex(0x18, 0x18)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_12CF")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11DF")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrPos(0x14, 10690, 150, 3200, 270)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrPos(0x15, 7160, 100, 3200, 90)
    SetChrFlags(0x15, 0x10)
    SetChrChipByIndex(0x16, 0x19)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrPos(0x16, 14090, 150, -120, 90)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DA")
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DA")
    SetChrFlags(0x8, 0x10)

    label("loc_11DA")

    Jump("loc_12CF")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_126C")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0x16)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1267")
    SetChrFlags(0x20, 0x10)

    label("loc_1267")

    Jump("loc_12CF")

    label("loc_126C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_12CF")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)

    label("loc_12CF")

    Return()

    # Function_3_A2C end

    def Function_4_12D0(): pass

    label("Function_4_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1319")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_1319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1358")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_1358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1369")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_137A")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_138B")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_139C")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_13AD")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_13AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13BE")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_13CF")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_13CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_13E0")
    SetScenarioFlags(0x1, 5)
    Jump("loc_1441")

    label("loc_13E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13F1")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_13F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1402")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_1402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1413")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1424")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_1424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1435")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1441")
    SetScenarioFlags(0x1, 6)

    label("loc_1441")

    Return()

    # Function_4_12D0 end

    def Function_5_1442(): pass

    label("Function_5_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1456")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_1456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_146A")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_146A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_147E")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_147E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1492")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_14A6")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14BA")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14CE")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_14E2")
    SetScenarioFlags(0x1, 5)
    Call(0, 8)
    Jump("loc_1555")

    label("loc_14E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14F6")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_14F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_150A")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_151E")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_151E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1532")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_1532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1546")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1555")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)

    label("loc_1555")

    Return()

    # Function_5_1442 end

    def Function_6_1556(): pass

    label("Function_6_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_158D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_158D")
    Call(0, 52)
    Return()

    label("loc_158D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1627")
    TurnDirection(0xFE, 0x0, 0)

    #C0001
    ChrTalk(
        0xFE,
        (
            "あそこまで気に入ってもらえると\x01",
            "ワタシも作った甲斐があったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "またワタシの料理を\x01",
            "食べたくなったら、いつでも来るよろし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2221")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20CA")

    #C0003
    ChrTalk(
        0xFE,
        (
            "……まったくやれやれね。\x01",
            "表の騒動が終わったと思ったら\x01",
            "次から次へと、おかしな事ばかり……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "……おや、アンタたち揃って\x01",
            "どこかへ行くみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "まあこの状況、警察官には\x01",
            "頑張ってほしいと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#00005Fえっと、どうかしましたか……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A20")

    #C0008
    ChrTalk(
        0xFE,
        (
            "フウ……仕方ない、料理人の修業も\x01",
            "頑張っているようだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "今日はウチの稼ぎ頭、\x01",
            "代々伝わる秘伝のレシピを\x01",
            "教えてあげるね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャンホイは強引に料理手帳を奪って\x01",
            "何かを書き込んだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『薬膳麻婆豆腐』\x07\x00",
            "のレシピを手に入れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_B2(0x2)

    #C0012
    ChrTalk(
        0xFE,
        "……はい、持っていくよろし！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00003F（これは……手帳の最後の１ページが\x01",
            "  埋まったみたいだ。）\x02\x03",

            "#00000Fえっと、いいんですか？\x01",
            "そんな大切なレシピを\x01",
            "教えていただいて……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "フン、礼ならいらないよ。\x01",
            "ワタシが教えたいと思ったから\x01",
            "教えただけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "そんなことより\x01",
            "料理人の道はとても険しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "これからも、もっともっと\x01",
            "修行を積む事ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8C")

    label("loc_1A20")


    #C0017
    ChrTalk(
        0xFE,
        (
            "フウ……仕方ない、料理人の修業も\x01",
            "頑張っているようだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "ワタシの魂を込めた究極の一品、\x01",
            "これを持って行くよろし。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x193, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0020
    ChrTalk(
        0x101,
        "#00000Fど、どうもありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "フン、礼ならいらないよ。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "そんなことより\x01",
            "料理人の道はとても険しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "これからも、もっともっと\x01",
            "修行を積む事ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8C")


    #C0024
    ChrTalk(
        0x101,
        "#00011F……え？　はあ……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "また機会があったら来るよろし。\x01",
            "本格的な中華修行を仕込んでやるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00012Fあ、あの……\x01",
            "前々から違和感があったのですが。\x02\x03",

            "ひょっとして自分たち、\x01",
            "まだここに料理修行にきた人と\x01",
            "勘違いされてる気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "ン？　何ヶ月か前に\x01",
            "勘違いしてしまった話！？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "違う違う、それとは別件。\x01",
            "ホラ料理手帳を見るよろし。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "クロスベル調理師連盟所属、\x01",
            "ロイド・バニングス。\x01",
            "手帳にそう書いてあるでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "これを持ってきた人間には\x01",
            "加盟店として、修行を付ける責任がある。\x01",
            "そういうことね！\x02",
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

    #C0031
    ChrTalk(
        0x103,
        (
            "#00200Fその料理手帳……\x01",
            "そんなに本格的なものだったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00106Fう～ん、まったく\x01",
            "気付かなかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、ってことは\x01",
            "俺たちは立派な\x01",
            "調理師のタマゴってわけか。\x02\x03",

            "この際、本気で目指してみるのも\x01",
            "悪くねえかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006Fいや、さすがに\x01",
            "それは無謀というか何というか……\x02\x03",

            "#00000F……ええと、\x01",
            "でもありがとうございます。\x02\x03",

            "なんていうか、\x01",
            "こんなに良くしていただいて……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "フン、礼はいらないね。\x01",
            "ただワタシは見込みある若者に\x01",
            "すべきことをしたまで。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "とにかく、ウチの料理は精が付く。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "たらふく食べて、そしてさっさと\x01",
            "日常を取り戻してほしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……これでもワタシ、\x01",
            "身内は信用しているのだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DE, 4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C5")

    label("loc_20C5")

    Jump("loc_221C")

    label("loc_20CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2181")

    #C0039
    ChrTalk(
        0xFE,
        (
            "まったくおかしな事ばかりね。\x01",
            "フン、慌ててどうなるものでもないから\x01",
            "店は続けるけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "あの青白く光る樹は気味が悪い。\x01",
            "はやく平和に戻ってきて欲しいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_221C")

    label("loc_2181")


    #C0041
    ChrTalk(
        0xFE,
        (
            "龍老飯店は平常営業している。\x01",
            "注文するなら席につくよろし。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "……アンタたち揃ってどこかへ\x01",
            "行くつもりだろう。\x01",
            "さっさと腹ごしらえを済ませるといいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221C")

    Jump("loc_36E5")

    label("loc_2221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22D1")

    #C0043
    ChrTalk(
        0xFE,
        (
            "いつまで続くか分からない\x01",
            "戒厳令にイライラしてたら……\x01",
            "この騒ぎはどういうことね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "外を出歩いている化物が\x01",
            "少しでも店を傷つけたら、\x01",
            "タダじゃおかないよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_22D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_235E")

    #C0045
    ChrTalk(
        0xFE,
        (
            "クロスベルの独立に、\x01",
            "市民たちが興奮しているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "なんでもいいけど、\x01",
            "店で騒いだりするのだけは\x01",
            "遠慮してほしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_235E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_26B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2416")

    #C0047
    ChrTalk(
        0xFE,
        (
            "リーシャがいなくなって、\x01",
            "サンサンも相当こたえてるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "せっかくできた\x01",
            "親友と呼べる存在……\x01",
            "無理もないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "なんとか元気に\x01",
            "なってくれるといいけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B3")

    label("loc_2416")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2477")

    #C0050
    ChrTalk(
        0xFE,
        (
            "心なしか、サンサンが\x01",
            "ウキウキしてるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "元気をとりもどしたか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B3")

    label("loc_2477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262C")

    #C0052
    ChrTalk(
        0xFE,
        (
            "サンサン……\x01",
            "ワタシに黙ってミスコンなんかに\x01",
            "出場してしまうとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "しかし、商工会会長の孫の誘いは\x01",
            "断ったと言ってたはず……！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "……一体誰の仕業ね！？\x01",
            "見つけ次第、この包丁で\x01",
            "八つ裂きにしてやるね！！\x02",
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
    Sleep(1200)

    #C0055
    ChrTalk(
        0x104,
        "#00306F（ぜ、絶対に黙っておこうぜ……）\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10309F（フフ、バラして反応を見るのも\x01",
            "  楽しそうだけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26B3")

    label("loc_262C")


    #C0057
    ChrTalk(
        0xFE,
        (
            "まあ、サンサンが\x01",
            "笑顔を取り戻したのは良かったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "……それはそれとして、\x01",
            "サンサンを出場させた輩は\x01",
            "八つ裂きにしてやるけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B3")

    Jump("loc_36E5")

    label("loc_26B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2759")

    #C0059
    ChrTalk(
        0xFE,
        (
            "ん……どうかしたのかね？\x01",
            "なんだか切羽詰っているようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "腹が減っては戦はできぬ、\x01",
            "というのは万国共通ね。\x01",
            "たっぷり食べていくとよろし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_2759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27CF")

    #C0061
    ChrTalk(
        0xFE,
        (
            "やっぱり雨の日は、\x01",
            "客足も少なくて心地いいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "明日の分の仕込みまで\x01",
            "一気にやっておくとするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_27CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2915")

    #C0063
    ChrTalk(
        0xFE,
        (
            "やれやれ、試しにバイトに\x01",
            "簡単な料理をやらせてみたが……\x01",
            "てんで使い物にならなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "やはりしばらくは、\x01",
            "雑用をしてもらうしかないね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2910")

    #C0065
    ChrTalk(
        0x101,
        (
            "#00008F（ここでグルメガイドの取材が\x01",
            "  出来そうだけど……）\x02\x03",

            "#00003F（今はそれどころじゃない。\x01",
            "  後で忘れずに来るとしよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2910")

    Jump("loc_36E5")

    label("loc_2915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2AB8")
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A33")

    #C0066
    ChrTalk(
        0xFE,
        (
            "チャーハンをうまく作るコツは\x01",
            "とにかく強火で炒めることよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "そうすれば鍋に焦げ付かせずに\x01",
            "パラパラした食感になるね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    OP_4B(0xC, 0xFF)

    #C0068
    ChrTalk(
        0xC,
        "へ、へえなるほど……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "コラッ！\x01",
            "よそ見するのはダメよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1200)
    OP_64(0xC)
    OP_93(0xC, 0x0, 0x1F4)

    #C0070
    ChrTalk(
        0xC,
        "す、すんません！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    Jump("loc_2AAF")

    label("loc_2A33")


    #C0071
    ChrTalk(
        0xFE,
        (
            "ああ、もう……\x01",
            "言ったそばからコゲてるね！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "失敗した分はちゃんと\x01",
            "じぶんで食べなければだめよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        "うひいぃ……！\x02",
    )

    CloseMessageWindow()

    label("loc_2AAF")

    OP_4C(0xC, 0xFF)
    Jump("loc_36E5")

    label("loc_2AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB4")

    #C0074
    ChrTalk(
        0xFE,
        (
            "クロスベルが独立を望むなら\x01",
            "好きにすればいいと思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "帝国、共和国からの\x01",
            "安全が保障されなくなる\x01",
            "というのは少々問題よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "サンサンに１リジュたりとも\x01",
            "危険が及ぶ事があってはならない。\x01",
            "だからワタシは独立に反対ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C3D")

    label("loc_2BB4")


    #C0077
    ChrTalk(
        0xFE,
        (
            "安全保障がされなくなるというなら、\x01",
            "ワタシは独立には反対ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "サンサンに１リジュたりとも\x01",
            "危険が及ぶ事が\x01",
            "あってはならないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C3D")

    Jump("loc_36E5")

    label("loc_2C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D08")

    #C0079
    ChrTalk(
        0xFE,
        (
            "あの新入りバイトども、\x01",
            "いつまでたっても仕事を覚えないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "サンサンに色目を使うのも\x01",
            "一向に止める気配がないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "フン、今度キツ～イお灸を\x01",
            "据えてやろうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D82")

    label("loc_2D08")


    #C0082
    ChrTalk(
        0xFE,
        (
            "そもそも、サンサンに\x01",
            "色目を使う奴が多すぎるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "もし手を出すような輩がいたら……\x01",
            "……フン、あえて言わないけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D82")

    Jump("loc_36E5")

    label("loc_2D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E44")

    #C0084
    ChrTalk(
        0xFE,
        (
            "今朝は表が騒がしくて\x01",
            "しかたなかったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "共和国の大統領が\x01",
            "クロスベル入りしたという\x01",
            "話だったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "ワタシの平穏を邪魔する者は\x01",
            "誰だろうと許せないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E97")

    label("loc_2E44")


    #C0087
    ChrTalk(
        0xFE,
        "ワタシは静かな店が好きね。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "その平穏を邪魔する者は\x01",
            "誰だろうと許せないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E97")

    Jump("loc_36E5")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3102")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)
    Sleep(300)

    #C0089
    ChrTalk(
        0x8,
        (
            "おや、さっきテーブルにいた\x01",
            "小さなお客さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "ワタシの料理どうだったね？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    #C0091
    ChrTalk(
        0x1A2,
        "ち、小さいは余計だ！\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x1A2,
        "だが、まあ料理の方は大満足だ。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x1A2,
        (
            "ただし、あの質であの値段は安すぎる。\x01",
            "店主ももっと価値にみあった額を――\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "ふむ、お客さん。\x01",
            "まだ幼いのにタイヘンお利口さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "だけど覚えておくよろし、\x01",
            "ここは“庶民”の龍老飯店。\x01",
            "敷居の高い店にはしたくない。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "だからワタシは、\x01",
            "今の値段を変えるつもりないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1A2,
        (
            "な、なるほど……\x01",
            "おみそれいたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00009F（はは、何気に素直なんだな。）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1DC, 5)
    Jump("loc_317D")

    label("loc_3102")


    #C0099
    ChrTalk(
        0x8,
        (
            "しかし、小さいお客さん。\x01",
            "まだ幼いのになかなか\x01",
            "違いの分かるオトコね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "ほんと、パックとルースにも\x01",
            "見習わせたいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317D")

    Jump("loc_330E")

    label("loc_3182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3275")

    #C0101
    ChrTalk(
        0xFE,
        (
            "明日からの通商会議に向けてか、\x01",
            "結構な数の記者もクロスベル入り\x01",
            "してるっていう話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "フン、中にはサンサンの写真を\x01",
            "勝手に撮ろうとする\x01",
            "記者もいるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "もしそんなヤツがいたら、\x01",
            "ワタシ、容赦しないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_330E")

    label("loc_3275")


    #C0104
    ChrTalk(
        0xFE,
        (
            "記者の中にはサンサンの写真を\x01",
            "勝手に撮ろうとする輩もいそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "女の記者ならまだしも、\x01",
            "男の記者がそんな事をしようものなら\x01",
            "ワタシ、容赦しないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330E")

    Jump("loc_36E5")

    label("loc_3313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_343F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C8")

    #C0106
    ChrTalk(
        0xFE,
        (
            "そういえば、旧市街の\x01",
            "赤ジャージの悪ガキども、\x01",
            "滅多に顔を見せなくなったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "奴ら、まさか\x01",
            "ツケで飲んでいった分を\x01",
            "踏み倒そうってんじゃあないかね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_343A")

    label("loc_33C8")


    #C0108
    ChrTalk(
        0xFE,
        (
            "サンサンに手を出しそうな輩が\x01",
            "減る分には一向に構わないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "ツケを返してからに\x01",
            "してほしいよ、まったく。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_343A")

    Jump("loc_36E5")

    label("loc_343F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_36E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_END)), "loc_359C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3511")

    #C0110
    ChrTalk(
        0xFE,
        (
            "せっかくワタシにも\x01",
            "あたらしい弟子ができると\x01",
            "思ったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "まあ、カン違いなら仕方ないね。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "渡した料理手帳は\x01",
            "好きに使っていいから、\x01",
            "せいぜい精進するがいいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3597")

    label("loc_3511")


    #C0113
    ChrTalk(
        0xFE,
        (
            "渡した料理手帳は\x01",
            "好きに使っていいから、\x01",
            "せいぜい精進するがいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "成長のコツは、\x01",
            "とにかく料理をすること。\x01",
            "……分かったね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3597")

    Jump("loc_36E5")

    label("loc_359C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3656")

    #C0115
    ChrTalk(
        0xFE,
        (
            "お客さんが無闇に\x01",
            "厨房に入ってはいけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "なんと言っても、\x01",
            "ここは料理人にとっての\x01",
            "聖域なのだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "ま、ワタシに弟子入りしたい\x01",
            "というなら話は別だけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_36E5")

    label("loc_3656")


    #C0118
    ChrTalk(
        0xFE,
        (
            "東方料理を学びたいというなら、\x01",
            "ワタシも教えるにやぶさかでないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "そうじゃないなら、\x01",
            "この厨房という聖域に\x01",
            "無闇に立ち入らないことね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E5")

    TalkEnd(0xFE)
    Return()

    # Function_6_1556 end

    def Function_7_36E9(): pass

    label("Function_7_36E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_380E")

    #C0120
    ChrTalk(
        0xFE,
        (
            "ヘヘ、あんだけ異様な光景なのに\x01",
            "気にもせずに料理してるなんて\x01",
            "さすが、マスターらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "共和国のお袋が心配だが、\x01",
            "そっちは内戦が起こってる帝国ほど\x01",
            "危険な情勢ってわけでもねえだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "俺も気を散らしてるヒマはねえ。\x01",
            "マスターにしっかりついてかねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38B9")

    label("loc_380E")


    #C0123
    ChrTalk(
        0xFE,
        (
            "共和国のお袋が心配だが、\x01",
            "そっちは内戦が起こってる帝国ほど\x01",
            "危険な情勢ってわけでもねえだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "俺も気を散らしてるヒマはねえ。\x01",
            "マスターにしっかりついてかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B9")

    Jump("loc_45E8")

    label("loc_38BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3943")

    #C0125
    ChrTalk(
        0xFE,
        (
            "なにやらトンでもねえことに\x01",
            "なっちまいやがったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "こりゃあ、店なんて\x01",
            "やってる場合じゃ\x01",
            "ねえかもしれねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_3943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E9")

    #C0127
    ChrTalk(
        0xFE,
        (
            "今日を逃したら、\x01",
            "しばらくは共和国に\x01",
            "戻りにくくなんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……共和国のお袋、心配してるかな。\x01",
            "俺も帰ったほうがいいのかねえ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A63")

    label("loc_39E9")


    #C0129
    ChrTalk(
        0xFE,
        (
            "しっかし、リーシャちゃんも\x01",
            "ほんとどこに行っちまったやら……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "サンサンも心配してるし、\x01",
            "消息が分かればいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A63")

    Jump("loc_45E8")

    label("loc_3A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A76")
    Jump("loc_45E8")

    label("loc_3A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3AD7")

    #C0131
    ChrTalk(
        0xFE,
        "なんだか最近物騒だよなぁ。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "ま、かといって\x01",
            "何をできるんでもねえんだがよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_3AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDE")

    #C0133
    ChrTalk(
        0xFE,
        (
            "バイトども、\x01",
            "どうやら前以上に雑用を\x01",
            "がんばることにしたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "へへっ、今までは\x01",
            "『うだつの上がらないパックとルース』\x01",
            "なんて呼んじまってたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "やっとこさ、\x01",
            "『そこそこ見所のあるパックとルース』\x01",
            "になったってところかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C67")

    label("loc_3BDE")


    #C0136
    ChrTalk(
        0xFE,
        (
            "パックとルースも、ようやく\x01",
            "甘っちょろい考え方を\x01",
            "捨てる事ができたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "ま、少しは見所があるように\x01",
            "なってきたってところかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C67")

    Jump("loc_45E8")

    label("loc_3C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D04")

    #C0138
    ChrTalk(
        0xFE,
        (
            "パックもルースも、\x01",
            "自分たちの未熟さを\x01",
            "思い知ってヘコんでるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "ここで立ち直れなきゃ、\x01",
            "商売なんて始めても\x01",
            "続かないと思うけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_3D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEF")

    #C0140
    ChrTalk(
        0xFE,
        (
            "パックとルースの野郎、\x01",
            "もっといい仕事をさせてくれなんて\x01",
            "生意気な口をききやがってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "俺も昔同じような事を言って\x01",
            "マスターに怒られたもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "雑用も立派な仕事だってのを、\x01",
            "ちゃんと理解しねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E60")

    label("loc_3DEF")


    #C0143
    ChrTalk(
        0xFE,
        (
            "どんな仕事も、\x01",
            "与えられた以上は\x01",
            "誇りを持ってやんないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "くっく、まあマスターの\x01",
            "受け売りなんだがよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E60")

    Jump("loc_45E8")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F11")

    #C0145
    ChrTalk(
        0xFE,
        (
            "そういや、共和国にも\x01",
            "久しく帰ってねえなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "ま、ここで働くのは楽しいし\x01",
            "別にいいんだけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "たまにはお袋に\x01",
            "連絡くらいすっかなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F51")

    label("loc_3F11")


    #C0148
    ChrTalk(
        0xFE,
        (
            "たまにはお袋に\x01",
            "連絡くらいすっかなあ。\x01",
            "随分帰ってねえし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F51")

    Jump("loc_45E8")

    label("loc_3F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407A")

    #C0149
    ChrTalk(
        0xFE,
        (
            "なんだか俺、いまだにマスターに\x01",
            "“サンサンに手を出しそうな輩”に\x01",
            "リストアップされてるっぽいなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "バイトの世話係を押し付けられたのも、\x01",
            "サンサンに手を出させないように\x01",
            "っていう理由だろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "うーん、俺にとっちゃサンサンは\x01",
            "妹みたいなもんなんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_410E")

    label("loc_407A")


    #C0152
    ChrTalk(
        0xFE,
        (
            "マスターとは付き合い長いし、\x01",
            "俺にとっちゃサンサンは\x01",
            "妹みたいなもんなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "見守りこそすれど、\x01",
            "手を出すつもりなんて\x01",
            "全くないんだけどな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410E")

    Jump("loc_45E8")

    label("loc_4113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41CF")

    #C0154
    ChrTalk(
        0xFE,
        (
            "噂じゃマスターは、\x01",
            "東方人街の特に治安の悪い場所に\x01",
            "店を開いてたらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "俺がマスターと出会ったのは\x01",
            "クロスベルでだけど、昔の話は\x01",
            "ほとんどしてくれないんだよな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_41CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C3")

    #C0156
    ChrTalk(
        0xFE,
        (
            "マスターは、東方武術を\x01",
            "嗜#2Rたしな#んでいるらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "東方人街にいた頃は、\x01",
            "店に来る荒くれ者どもを\x01",
            "自ら退けてたって話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "サンサンに近づく男を睨みつける\x01",
            "あの眼光の鋭さにも、\x01",
            "納得がいくってもんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_432F")

    label("loc_42C3")


    #C0159
    ChrTalk(
        0xFE,
        (
            "マスターは、東方武術を\x01",
            "嗜#2Rたしな#んでいるらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "へへっ、本気で怒らせたら\x01",
            "後悔するかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432F")

    Jump("loc_45E8")

    label("loc_4334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4420")

    #C0161
    ChrTalk(
        0xFE,
        (
            "実はこの間、リーシャちゃんに\x01",
            "モーションかけてみたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "全然気付いた様子もなく、\x01",
            "爽やかに挨拶してから\x01",
            "練習に出かけて行っちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "今は色恋よりも、\x01",
            "アルカンシェルが楽しい\x01",
            "みたいだなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44B6")

    label("loc_4420")


    #C0164
    ChrTalk(
        0xFE,
        (
            "リーシャちゃん、\x01",
            "今はアルカンシェルが\x01",
            "楽しくて仕方ないんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "うーん、俺もなんだか\x01",
            "のぺぺーんと過ごしてるのが\x01",
            "恥ずかしくなってきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B6")

    Jump("loc_45E8")

    label("loc_44BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_45E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_455D")

    #C0166
    ChrTalk(
        0xFE,
        (
            "新入りのパックとルースに、\x01",
            "会計や掃除、皿洗いとかの\x01",
            "雑用を任すことにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "ようやく俺も厨房に\x01",
            "専念できるようになったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_45E8")

    label("loc_455D")


    #C0168
    ChrTalk(
        0xFE,
        (
            "新入りのパックとルースに、\x01",
            "雑用全般を任すことにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "ま、カウンター裏にすら\x01",
            "入れてもらえなかった頃よりは\x01",
            "進歩したのかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45E8")

    TalkEnd(0xFE)
    Return()

    # Function_7_36E9 end

    def Function_8_45EC(): pass

    label("Function_8_45EC")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_46FF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4602")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4675")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4675")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4694")
    OP_AF(0x34)
    Jump("loc_4696")

    label("loc_4694")

    OP_AF(0x33)

    label("loc_4696")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46F5")

    label("loc_46A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46C5")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46F5")

    label("loc_46C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D9")
    Jump("loc_46F5")

    label("loc_46D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_46F5")

    Jump("loc_4602")

    label("loc_46FA")

    Jump("loc_4702")

    label("loc_46FF")

    Call(0, 9)

    label("loc_4702")

    TalkEnd(0xA)
    Return()

    # Function_8_45EC end

    def Function_9_4706(): pass

    label("Function_9_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A08")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4731")
    Call(0, 11)
    Jump("loc_48A4")

    label("loc_4731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482F")

    #C0170
    ChrTalk(
        0xA,
        (
            "リーシャたち、\x01",
            "今から危険な場所に\x01",
            "乗り込んでいくみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "本当は止めたいけど……\x01",
            "リーシャが行くって言うなら\x01",
            "わたしは止めないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "私、待ってるから……\x01",
            "絶対に無事に帰ってきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x106,
        "#10704Fうん……絶対に帰ってくるから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_48A4")

    label("loc_482F")


    #C0174
    ChrTalk(
        0xA,
        (
            "リーシャたち、\x01",
            "今から危険な場所に\x01",
            "乗り込んでいくみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "私、待ってるから……\x01",
            "絶対に無事に帰ってきてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48A4")

    Jump("loc_4A03")

    label("loc_48A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48BB")
    Call(0, 10)
    Jump("loc_4A03")

    label("loc_48BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498E")

    #C0176
    ChrTalk(
        0xA,
        (
            "リーシャたち、\x01",
            "今から危険な場所に\x01",
            "乗り込んでいくみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "本当は止めたいけど……\x01",
            "リーシャが行くって言うなら\x01",
            "わたしは止めないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "私、待ってるから……\x01",
            "絶対に無事に帰ってきてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A03")

    label("loc_498E")


    #C0179
    ChrTalk(
        0xA,
        (
            "リーシャたち、\x01",
            "今から危険な場所に\x01",
            "乗り込んでいくみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "私、待ってるから……\x01",
            "絶対に無事に帰ってきてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A03")

    Jump("loc_5B57")

    label("loc_4A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4B79")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A33")
    Call(0, 11)
    Jump("loc_4AE4")

    label("loc_4A33")


    #C0181
    ChrTalk(
        0xA,
        (
            "グスッ……\x01",
            "リーシャにまた会えて\x01",
            "本当に良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "今度、黙って出て行ったりしたら\x01",
            "絶対に許さないんだからね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x106,
        (
            "#10704Fうん……約束するね。\x01",
            "ありがとう、サンサン。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE4")

    Jump("loc_4B74")

    label("loc_4AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AFB")
    Call(0, 10)
    Jump("loc_4B74")

    label("loc_4AFB")


    #C0184
    ChrTalk(
        0xA,
        (
            "グスッ……\x01",
            "リーシャにまた会えて\x01",
            "本当に良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "今度、黙って出て行ったりしたら\x01",
            "絶対に許さないんだからね！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B74")

    Jump("loc_5B57")

    label("loc_4B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C3F")

    #C0186
    ChrTalk(
        0xA,
        (
            "クロスベルがこんなことに\x01",
            "なっちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "もし戦争になったりしたら、\x01",
            "本当にもうリーシャに\x01",
            "会えなくなっちゃう気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        "リーシャ、今どこにいるの……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4CB7")

    label("loc_4C3F")


    #C0189
    ChrTalk(
        0xA,
        (
            "もし戦争になったりしたら、\x01",
            "本当にもうリーシャに\x01",
            "会えなくなっちゃう気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        "リーシャ、今どこにいるの……？\x02",
    )

    CloseMessageWindow()

    label("loc_4CB7")

    Jump("loc_5B57")

    label("loc_4CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4F28")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CEE")
    Call(0, 53)
    Return()

    label("loc_4CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E24")

    #C0191
    ChrTalk(
        0xA,
        (
            "……リーシャ、いなくなる直前に\x01",
            "私に書置きを残してくれたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "『事情でクロスベルを\x01",
            "  離れることになった』\x01",
            "なんて書いてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "アルカンシェルを放っといて\x01",
            "いなくなるなんて絶対に\x01",
            "リーシャらしくないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "……何か事情があったのかな。\x01",
            "相談してくれればよかったのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4EA1")

    label("loc_4E24")


    #C0195
    ChrTalk(
        0xA,
        (
            "アルカンシェルを放っといて\x01",
            "いなくなるなんて\x01",
            "リーシャらしくないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        (
            "親友の私にも相談できない\x01",
            "事情があったのかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA1")

    Jump("loc_4F23")

    label("loc_4EA6")


    #C0197
    ChrTalk(
        0xA,
        (
            "がんばってミスコンを\x01",
            "盛り上げさせてもらうよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        (
            "プログラムの開始に\x01",
            "間に合うように行くから、\x01",
            "あとで連絡ちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F23")

    Jump("loc_5B57")

    label("loc_4F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_50EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506C")

    #C0199
    ChrTalk(
        0xA,
        (
            "今日、朝はやくに\x01",
            "アルカンシェルに向かう\x01",
            "リーシャを見かけたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "挨拶したんだけど……\x01",
            "なんていうか\x01",
            "全然元気なかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 7)), scpexpr(EXPR_END)), "loc_5009")

    #C0201
    ChrTalk(
        0x101,
        (
            "#00008F（……今のところは\x01",
            "  そっとしておくしかないな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5064")

    label("loc_5009")


    #C0202
    ChrTalk(
        0x101,
        (
            "#00003F（……リーシャ……\x01",
            "　アルカンシェルのほうに\x01",
            "  様子を見に行ってみようか……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5064")

    SetScenarioFlags(0x0, 2)
    Jump("loc_50E9")

    label("loc_506C")


    #C0203
    ChrTalk(
        0xA,
        (
            "朝、見かけたリーシャ……\x01",
            "全然元気なかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "……何かあったのかな。\x01",
            "相談に乗れるものなら\x01",
            "乗ってあげたいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E9")

    Jump("loc_5B57")

    label("loc_50EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_51ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517C")

    #C0205
    ChrTalk(
        0xA,
        (
            "リーシャ、用事があるからって\x01",
            "出かけて行ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        (
            "ふう、もう少しおしゃべりを\x01",
            "してたかったけど……仕方ないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51E8")

    label("loc_517C")


    #C0207
    ChrTalk(
        0xA,
        (
            "もう少しリーシャと\x01",
            "おしゃべりをしたかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xA,
        (
            "用事なら仕方ないよね。\x01",
            "……お仕事しなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51E8")

    Jump("loc_5B57")

    label("loc_51ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_526E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5208")
    Call(0, 48)
    Jump("loc_5269")

    label("loc_5208")


    #C0209
    ChrTalk(
        0xA,
        (
            "えへへ……リーシャに\x01",
            "そこまで言われると恥ずかしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        "一生の友達でいようね、リーシャ！\x02",
    )

    CloseMessageWindow()

    label("loc_5269")

    Jump("loc_5B57")

    label("loc_526E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_52E6")

    #C0211
    ChrTalk(
        0xA,
        (
            "パックとルース、\x01",
            "結局仕事がおっつかなくて\x01",
            "元のシフトに戻ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        "もー、パパも人が悪いんだから。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B57")

    label("loc_52E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_549F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5387")

    #C0213
    ChrTalk(
        0xA,
        (
            "……グルメガイドの取材？\x01",
            "ああ、話は聞いてるよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xA,
        (
            "パパが厨房にいるから、\x01",
            "そっちに聞いてみてくれる？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_5387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5430")

    #C0215
    ChrTalk(
        0xA,
        (
            "パパとフェイさんから、\x01",
            "今日はお会計だけでいいからって\x01",
            "ここに押し込められたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        (
            "……パックとルースがすっごく\x01",
            "忙しそうだけど、大丈夫なのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_549A")

    label("loc_5430")


    #C0217
    ChrTalk(
        0xA,
        (
            "今日はパックが\x01",
            "給仕をすべてやるらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xA,
        (
            "……すっごく忙しそう。\x01",
            "本当に手伝わなくていいのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_549A")

    Jump("loc_5B57")

    label("loc_549F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5546")

    #C0219
    ChrTalk(
        0xA,
        (
            "いらっしゃ～い。\x01",
            "何か注文する？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "なんだか来るお客さんみんな、\x01",
            "通商会議の話題みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "市長が言ったことって、\x01",
            "そんなに重大なことだったの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B57")

    label("loc_5546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5666")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F9")

    #C0222
    ChrTalk(
        0xA,
        (
            "幼馴染のパックとルースを\x01",
            "バイトに推薦したのは私ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xA,
        (
            "うんうん、２人なりに\x01",
            "がんばってるみたいで感心感心。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xA,
        "パパに頼み込んだ私も鼻が高いよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5661")

    label("loc_55F9")


    #C0225
    ChrTalk(
        0xA,
        (
            "パックとルース、\x01",
            "ちゃんとアルバイトを\x01",
            "がんばってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xA,
        "パパに頼み込んだ私も鼻が高いよ。\x02",
    )

    CloseMessageWindow()

    label("loc_5661")

    Jump("loc_5B57")

    label("loc_5666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_57B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5744")

    #C0227
    ChrTalk(
        0xA,
        (
            "パパがいうには、共和国は\x01",
            "クロスベルよりもさらに\x01",
            "東方人が多い国なんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xA,
        (
            "小さい頃にこっちに\x01",
            "移住してきたから\x01",
            "ほとんど覚えてないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xA,
        (
            "とても賑やかな場所みたい。\x01",
            "楽しそうよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_57B4")

    label("loc_5744")


    #C0230
    ChrTalk(
        0xA,
        (
            "共和国はクロスベルより\x01",
            "さらに東方人が多いらしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "賑やかで楽しそう～。\x01",
            "機会があれば行ってみたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B4")

    Jump("loc_5B57")

    label("loc_57B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_58DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_584C")
    TurnDirection(0xA, 0x1A2, 0)
    Sleep(300)

    #C0232
    ChrTalk(
        0xA,
        "あ、さっきの可愛らしいお客さん。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        "また来てね～、いつでも待ってるから。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x1A2,
        "あ、ああ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_58D8")

    label("loc_584C")


    #C0235
    ChrTalk(
        0xA,
        (
            "あのカウンター席に座ってる女のヒト、\x01",
            "リベールの記者さんなんだって～。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xA,
        (
            "ふふっ、せっかくだから\x01",
            "可愛く写真を撮ってもらえないかな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58D8")

    Jump("loc_5B57")

    label("loc_58DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59CB")

    #C0237
    ChrTalk(
        0xA,
        (
            "まったくフェンさんったら、\x01",
            "リーシャをナンパするなんて\x01",
            "困ったひとよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xA,
        (
            "リーシャだったら、\x01",
            "将来、も～っといいヒトが\x01",
            "見つかるはずだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        (
            "フェンさんには失礼かもだけど、\x01",
            "親友としてそこは譲れないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5A3E")

    label("loc_59CB")


    #C0240
    ChrTalk(
        0xA,
        (
            "リーシャだったら、\x01",
            "将来、も～っといいヒトが\x01",
            "見つかるはずだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "えへへ、親友のわたしが\x01",
            "保証しちゃうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A3E")

    Jump("loc_5B57")

    label("loc_5A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC4")

    #C0242
    ChrTalk(
        0xA,
        (
            "いらっしゃ～い。\x01",
            "お好きな席についてね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        (
            "パパはちょっと怖いけど、\x01",
            "料理の味は天下一品よ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5B57")

    label("loc_5AC4")


    #C0244
    ChrTalk(
        0xA,
        (
            "店の手伝いを始めて\x01",
            "まだ１年も経たないけど、\x01",
            "お仕事にも大分慣れてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "お客さんもいい人ばっかりだし、\x01",
            "これならず～っと続けられそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B57")

    Return()

    # Function_9_4706 end

    def Function_10_5B58(): pass

    label("Function_10_5B58")


    #C0246
    ChrTalk(
        0xA,
        (
            "リーシャ……\x01",
            "今頃どうしてるのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xA,
        (
            "クロスベルがこんな事に\x01",
            "なっちゃって……心配よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        (
            "#00003F（……後で連れてきてあげたほうが\x01",
            "  いいかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_10_5B58 end

    def Function_11_5BFF(): pass

    label("Function_11_5BFF")

    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    #C0249
    ChrTalk(
        0xA,
        (
            "リ、リーシャ……\x01",
            "リーシャだよね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "い、今までどこにいたの！？\x01",
            "すっごく心配したんだから……！\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x106,
        (
            "#10703Fごめんなさい、サンサン……\x01",
            "心配をかけてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "うう……本当よ！\x01",
            "リーシャのばかばか！\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xA,
        (
            "……でも……\x01",
            "また会えてよかったよ～……\x01",
            "ぶえええええ～～～……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x106)

    #C0254
    ChrTalk(
        0x106,
        "#10705Fな、泣かないでサンサン……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "グスッ……だって、\x01",
            "本当に心配してたんだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xA,
        (
            "今度、黙って出て行ったりしたら\x01",
            "絶対に許さないんだからね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x106,
        (
            "#10704Fうん、本当にごめんなさい。\x01",
            "……待っててくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#00002F（リーシャ……良かったな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 0)
    Return()

    # Function_11_5BFF end

    def Function_12_5E5C(): pass

    label("Function_12_5E5C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5F6F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EE5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5EE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F04")
    OP_AF(0x34)
    Jump("loc_5F06")

    label("loc_5F04")

    OP_AF(0x33)

    label("loc_5F06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F65")

    label("loc_5F15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F35")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F65")

    label("loc_5F35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F49")
    Jump("loc_5F65")

    label("loc_5F49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F65")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_5F65")

    Jump("loc_5E72")

    label("loc_5F6A")

    Jump("loc_5F72")

    label("loc_5F6F")

    Call(0, 13)

    label("loc_5F72")

    TalkEnd(0xB)
    Return()

    # Function_12_5E5C end

    def Function_13_5F76(): pass

    label("Function_13_5F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_60A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6032")

    #C0259
    ChrTalk(
        0xB,
        (
            "腹いっぱいならみんな幸せ。\x01",
            "それがマスターのモットーらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        (
            "将来ルースと店をやるときには\x01",
            "そんな風に客のことを思って、\x01",
            "仕事を頑張っていきたいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_60A0")

    label("loc_6032")


    #C0261
    ChrTalk(
        0xB,
        (
            "ってなわけで、今日は大盛り無料、\x01",
            "ご飯のお代わり自由だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xB,
        (
            "ガンガン食べて、\x01",
            "気合を入れてってくれよな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60A0")

    Jump("loc_6C17")

    label("loc_60A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_612D")

    #C0263
    ChrTalk(
        0xB,
        (
            "掃除なんかしてる暇があんのかな。\x01",
            "……とはいえ、どこに\x01",
            "逃げられるわけじゃないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        "はあ……ため息しかでねえぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_612D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_61A9")

    #C0265
    ChrTalk(
        0xB,
        (
            "これからどうなるのか、\x01",
            "オレには全く見当もつかねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "こんなときこそ\x01",
            "気合で乗り切らなくっちゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_61A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_62E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626C")

    #C0267
    ChrTalk(
        0xB,
        (
            "フェイさんが\x01",
            "チャリティイベントの\x01",
            "手伝いに行っててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xB,
        (
            "オレが代わりに厨房に入って\x01",
            "マスターの補佐をしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        (
            "オレもできる限り\x01",
            "やれることをしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_62DE")

    label("loc_626C")


    #C0270
    ChrTalk(
        0xB,
        (
            "オレができるのなんて\x01",
            "所詮雑用レベルだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "フェイさんがいないんだし、\x01",
            "できる限りのことはしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62DE")

    Jump("loc_6C17")

    label("loc_62E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6389")

    #C0272
    ChrTalk(
        0xB,
        "１００、２００、３００ミラっと……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xB,
        (
            "へへ、前より大分\x01",
            "カウンター業が上手くなったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xB,
        (
            "やったらやったぶんだけ、\x01",
            "ちゃんと成長できてるんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_6389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_64C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_645D")

    #C0275
    ChrTalk(
        0xB,
        (
            "仕事なんて、気合だけで\x01",
            "なんとでもなると思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xB,
        (
            "やっぱりどこか\x01",
            "考えが甘かったのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        (
            "とにかく、今はできることをやる！\x01",
            "それが大事なんだって分かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_64C3")

    label("loc_645D")


    #C0278
    ChrTalk(
        0xB,
        (
            "昨日はルースの奴と一緒に、\x01",
            "相当へこんでたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "ま、今はできることを\x01",
            "やるしかないってな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C3")

    Jump("loc_6C17")

    label("loc_64C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6548")

    #C0280
    ChrTalk(
        0xB,
        "はあ、疲れた……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xB,
        (
            "サンサンの仕事を見てたら\x01",
            "楽しいばっかりだと思ってたけど、\x01",
            "全然そんなことなかったな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_6548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_65BE")

    #C0282
    ChrTalk(
        0xB,
        (
            "テーブルを拭いて、\x01",
            "注文をとって、料理を運んで……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "うああ、忙しすぎて\x01",
            "目が回っちまうううう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_65BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B6")

    #C0284
    ChrTalk(
        0xB,
        (
            "ルースがバイト代を増やすために、\x01",
            "仕事をもっと重要なポストに\x01",
            "してもらおうって言うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "確かに将来のためには\x01",
            "ここらでドンと稼がないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xB,
        (
            "ま、オレとルースなら\x01",
            "どんな仕事でも気合で\x01",
            "乗り越えられるだろうしな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_670C")

    label("loc_66B6")


    #C0287
    ChrTalk(
        0xB,
        (
            "へへ、案外オレは店員の\x01",
            "才能があるかもしれないし……\x01",
            "マスターに頼んでみるかなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_670C")

    Jump("loc_6C17")

    label("loc_6711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6814")

    #C0288
    ChrTalk(
        0xB,
        (
            "オレとルースとサンサンは\x01",
            "日曜学校時代の\x01",
            "同級生なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "あのときからマスター、\x01",
            "サンサンに関わるだけで\x01",
            "怖い顔すんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "さっきも、サンサンに\x01",
            "挨拶しただけで\x01",
            "すげえ睨まれちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xB,
        "はあ、勘弁して欲しいぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_688F")

    label("loc_6814")


    #C0292
    ChrTalk(
        0xB,
        (
            "サンサンに挨拶しただけで\x01",
            "マスターにすげえ睨まれたぜ……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xB,
        (
            "日曜学校時代から\x01",
            "こうなんだよな～……\x01",
            "勘弁してほしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_688F")

    Jump("loc_6C17")

    label("loc_6894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6933")

    #C0294
    ChrTalk(
        0xB,
        (
            "ルースはなんでもかんでも\x01",
            "型にはめようとすんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "なんだったら、出す予定の店を\x01",
            "飲食店にしちまっても\x01",
            "俺は全然かまわないんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_6933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_69D8")

    #C0296
    ChrTalk(
        0xB,
        (
            "ルースの奴、なんだか色々と\x01",
            "考えすぎてるんじゃねえかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "こんなにがんばってんだ、\x01",
            "オレらはきっと大物になる！\x01",
            "心配する事なんてなにもないよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_69D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A66")

    #C0298
    ChrTalk(
        0xB,
        (
            "あててて……\x01",
            "さっき思いっきり滑って\x01",
            "尻餅ついちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "うお～、こんな痛み、\x01",
            "気合で吹き飛ばしてやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6ADB")

    label("loc_6A66")


    #C0300
    ChrTalk(
        0xB,
        (
            "……あててて。\x01",
            "まあ気合を出そうが出すまいが\x01",
            "痛いもんは痛いか。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "雨の日は滑るから\x01",
            "お前らも気をつけるんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ADB")

    Jump("loc_6C17")

    label("loc_6AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB7")

    #C0302
    ChrTalk(
        0xB,
        (
            "少し前から、相棒のルースと一緒に\x01",
            "バイトさせてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xB,
        (
            "だけど、カウンター業は\x01",
            "あんまり得意じゃなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "楽しいけど、\x01",
            "ミラを数え間違えたりして\x01",
            "怒られてばっかりだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6C17")

    label("loc_6BB7")


    #C0305
    ChrTalk(
        0xB,
        (
            "でもまあ、\x01",
            "飲食店の店員ってのも\x01",
            "なかなか性に合ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xB,
        "楽しんでやらせてもらってるぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_6C17")

    Return()

    # Function_13_5F76 end

    def Function_14_6C18(): pass

    label("Function_14_6C18")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_6D2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D26")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6CA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6CC0")
    OP_AF(0x34)
    Jump("loc_6CC2")

    label("loc_6CC0")

    OP_AF(0x33)

    label("loc_6CC2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D21")

    label("loc_6CD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF1")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D21")

    label("loc_6CF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D05")
    Jump("loc_6D21")

    label("loc_6D05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D21")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 15)

    label("loc_6D21")

    Jump("loc_6C2E")

    label("loc_6D26")

    Jump("loc_6D2E")

    label("loc_6D2B")

    Call(0, 15)

    label("loc_6D2E")

    TalkEnd(0xC)
    Return()

    # Function_14_6C18 end

    def Function_15_6D32(): pass

    label("Function_15_6D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E15")

    #C0307
    ChrTalk(
        0xC,
        (
            "大変な時に頑張った経験は\x01",
            "将来、絶対に役に立つよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "将来、相棒のパックと\x01",
            "大きな商店を開くつもりだけど……\x01",
            "今は目の前の事を頑張らないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "……よ～し、そうと決まれば\x01",
            "ばばばっと掃除だ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6E9E")

    label("loc_6E15")


    #C0310
    ChrTalk(
        0xC,
        (
            "大変な時に頑張った経験は\x01",
            "将来、パックと商店を開いた時にも\x01",
            "絶対に役に立つよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xC,
        (
            "……よ～し、そうと決まれば\x01",
            "ばばばっと掃除だ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E9E")

    Jump("loc_7C4D")

    label("loc_6EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6F03")

    #C0312
    ChrTalk(
        0xC,
        "あんなのが外を出歩いてるなんて……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xC,
        "俺たち、一体どうなっちまうんだ……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_6F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6F77")

    #C0314
    ChrTalk(
        0xC,
        (
            "ヒャッホー、クロスベルが\x01",
            "独立国になるってな！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "いやー、めでたい。\x01",
            "掃除にも熱が入っちまうぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_6F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6FE7")

    #C0316
    ChrTalk(
        0xC,
        (
            "旧市街なんかすぐ近くだ、\x01",
            "下手したら東通りも\x01",
            "同じような目にあってたかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "……ぞぞっ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_6FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7088")

    #C0318
    ChrTalk(
        0xC,
        (
            "うーむ、今まで面倒だから\x01",
            "四角い床も丸く掃いてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        (
            "ちゃんと端からやってったほうが\x01",
            "むしろ早く済むんだよな。\x01",
            "掃除もまた奥が深いぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_7088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_729A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_714A")

    #C0320
    ChrTalk(
        0xC,
        (
            "グルメガイドの取材……？\x01",
            "ああ、そういえばマスターが\x01",
            "そんな話を言ってたような。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "マスターが厨房にいるから、\x01",
            "そっちに話をしてみてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7295")

    label("loc_714A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722B")

    #C0322
    ChrTalk(
        0xC,
        (
            "昨日、厨房を体験して\x01",
            "くじけそうになったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xC,
        (
            "パックと話し合って、\x01",
            "今できる事をちゃんと\x01",
            "がんばろうって決めたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xC,
        (
            "簡単な仕事すらできない奴が\x01",
            "難しい仕事を任されるわけが\x01",
            "なかったんだよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7295")

    label("loc_722B")


    #C0325
    ChrTalk(
        0xC,
        (
            "将来、相棒のパックと\x01",
            "大きな商店を開くためにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "今は雑用を完璧に\x01",
            "こなせるようにならないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7295")

    Jump("loc_7C4D")

    label("loc_729A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7306")

    #C0327
    ChrTalk(
        0xC,
        (
            "……地獄の厨房から\x01",
            "やっと解放されたよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xC,
        (
            "俺たちって、全然\x01",
            "ダメダメだったんだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_7306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7395")
    OP_4B(0x8, 0xFF)

    #C0329
    ChrTalk(
        0xC,
        (
            "あ、熱ッ……！\x01",
            "それに中華鍋って、\x01",
            "お、重いッ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        "ほら、さっさとするヨ！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        "す、すんませんっ！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_7410")

    label("loc_7395")


    #C0332
    ChrTalk(
        0xC,
        (
            "ひい、ひい……\x01",
            "前に手伝ったときは\x01",
            "楽勝だとおもってたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "チャーハン１つ作るのが\x01",
            "こんなに大変だったなんて……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7410")

    Jump("loc_7C4D")

    label("loc_7415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_764B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D7")

    #C0334
    ChrTalk(
        0xC,
        (
            "グルメガイドの取材……？\x01",
            "ああ、そういえばマスターが\x01",
            "そんな話を言ってたような。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        (
            "マスターが厨房にいるから、\x01",
            "そっちに話をしてみてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7646")

    label("loc_74D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B9")

    #C0336
    ChrTalk(
        0xC,
        (
            "やっぱ、ちまちまと\x01",
            "雑用ばっかりのバイトじゃ\x01",
            "資金はたまらないよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xC,
        (
            "いっちょ、マスターに\x01",
            "仕事のステップアップを\x01",
            "相談してみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xC,
        (
            "なーに、オレとルースなら\x01",
            "どんな仕事でも\x01",
            "ちょちょいのちょいさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7646")

    label("loc_75B9")


    #C0339
    ChrTalk(
        0xC,
        (
            "そろそろ、雑用なんかは脱却して\x01",
            "ステップアップしないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xC,
        (
            "厨房だったら、\x01",
            "前に少しだけ手伝ったし……\x01",
            "今度マスターに相談してみるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7646")

    Jump("loc_7C4D")

    label("loc_764B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7789")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7724")

    #C0341
    ChrTalk(
        0xC,
        (
            "いきなり掃除する箇所を\x01",
            "いつもの２倍に増やされたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xC,
        (
            "もしかしてパックのやつ、\x01",
            "マスターの前でサンサンに\x01",
            "話しかけちまったんじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "だとしたらこれ、連帯責任かよ。\x01",
            "うへ～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7784")

    label("loc_7724")


    #C0344
    ChrTalk(
        0xC,
        (
            "ああ、あとで\x01",
            "店の裏も掃除しないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xC,
        (
            "パックがうっかりしてたせいで\x01",
            "とんだ大掃除だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7784")

    Jump("loc_7C4D")

    label("loc_7789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_784C")

    #C0346
    ChrTalk(
        0xC,
        (
            "パックが、将来の俺たちの商店に\x01",
            "食堂でも作ればいいんじゃないか、\x01",
            "なんて言うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xC,
        (
            "うーん……\x01",
            "最低限の資金すら溜まってないのに\x01",
            "話が混沌としてきてる気がするな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_78C4")

    label("loc_784C")


    #C0348
    ChrTalk(
        0xC,
        (
            "将来、パックとデカい商店を\x01",
            "開くつもりなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        (
            "食堂を入れようかなんて、\x01",
            "話が混沌としてきてる気がするな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78C4")

    Jump("loc_7C4D")

    label("loc_78C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_79E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7974")

    #C0350
    ChrTalk(
        0xC,
        (
            "パックの奴、なんだか結構\x01",
            "このバイトを楽しんでる\x01",
            "みたいなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xC,
        (
            "２人で店をだすっていう\x01",
            "本来の目的を忘れてるんじゃ\x01",
            "ないだろうな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_79E3")

    label("loc_7974")


    #C0352
    ChrTalk(
        0xC,
        (
            "あくまでバイトは\x01",
            "店を出すためのミラを\x01",
            "準備する手段なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xC,
        (
            "パックの奴、なんだか\x01",
            "楽しみやがってよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79E3")

    Jump("loc_7C4D")

    label("loc_79E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ABE")

    #C0354
    ChrTalk(
        0xC,
        (
            "はあ……\x01",
            "雨音を聞いていると\x01",
            "憂鬱になってくるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xC,
        (
            "ミラは少しずつ貯まってきたけど、\x01",
            "まだまだ店を出すには程遠いし。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xC,
        (
            "本当にこのまま\x01",
            "バイトを続けてりゃ、\x01",
            "夢に近づけるのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7B2D")

    label("loc_7ABE")


    #C0357
    ChrTalk(
        0xC,
        (
            "本当にこのまま\x01",
            "バイトを続けてりゃ、\x01",
            "夢に近づけるのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xC,
        (
            "後でパックの奴にも\x01",
            "意見を聞いてみるか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B2D")

    Jump("loc_7C4D")

    label("loc_7B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7C4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC6")

    #C0359
    ChrTalk(
        0xC,
        (
            "相棒のパックと、\x01",
            "店を出すための資金稼ぎに\x01",
            "バイトを始めたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xC,
        (
            "いつか俺たちの店を開くための\x01",
            "下積みってわけさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7C4D")

    label("loc_7BC6")


    #C0361
    ChrTalk(
        0xC,
        (
            "しかし、マスターは厳しいし\x01",
            "時給は少ないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "サンサンに幼馴染のよしみで\x01",
            "雇ってもらったけど……\x01",
            "最近なんだか後悔してきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C4D")

    Return()

    # Function_15_6D32 end

    def Function_16_7C4E(): pass

    label("Function_16_7C4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D46")

    #C0363
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "ウチの運送会社も業務を再開してな。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "今までは共和国との輸送ルートを\x01",
            "主に担ってたんだが、今後しばらくは\x01",
            "自治州内だけになりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "ま、やることはそんな変わらねえし\x01",
            "今後も頑張っていかなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7DD3")

    label("loc_7D46")


    #C0366
    ChrTalk(
        0xFE,
        (
            "ま、仕事が自治州内だけに\x01",
            "なったからって、\x01",
            "やることはそんな変わらねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "きちんと腹ごしらえをして、\x01",
            "今まで通り頑張っていかなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD3")

    Jump("loc_89E3")

    label("loc_7DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7DE6")
    Jump("loc_89E3")

    label("loc_7DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA9")

    #C0368
    ChrTalk(
        0xFE,
        (
            "クロスベルの住民としちゃ\x01",
            "独立は喜ばしいことだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "しかもあの英雄、\x01",
            "アリオス・マクレインが\x01",
            "国防を担うってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "帝国や共和国が相手でも\x01",
            "相当心強いよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7F69")

    label("loc_7EA9")


    #C0371
    ChrTalk(
        0xFE,
        (
            "帝国と共和国の対応が分かるまで、\x01",
            "ウチの会社もしばらく休みらしい。\x01",
            "……ま、心配はいらねえよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "なんたってクロスベルには、\x01",
            "あの《風の剣聖》がいるんだ。\x01",
            "きっと俺たちを守ってくれるさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F69")

    Jump("loc_89E3")

    label("loc_7F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8022")

    #C0373
    ChrTalk(
        0xFE,
        (
            "仕事でタングラム門を\x01",
            "利用したんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "いつもより空気が\x01",
            "ピリッとしてやがった。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "人の出入りにも、いつも以上に\x01",
            "気を使ってるみたいだったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_807E")

    label("loc_8022")


    #C0376
    ChrTalk(
        0xFE,
        (
            "国境門があの調子じゃ、\x01",
            "仕事もはかどらねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "メシでも食ってるかな。\x01",
            "もぐもぐ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_807E")

    Jump("loc_89E3")

    label("loc_8083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8149")

    #C0378
    ChrTalk(
        0xFE,
        (
            "マインツが占領されるとは……\x01",
            "どこのどいつだか知らんが、\x01",
            "とんでもないことをしやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "まあ、クロスベルの警備隊は\x01",
            "なかなか精鋭揃いらしいしな。\x01",
            "任せておけば大丈夫じゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_8149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_81A6")

    #C0380
    ChrTalk(
        0xFE,
        "今日もあいにくの雨か……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "雨だと運転も危ないから、\x01",
            "気ィつけねえとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_81A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_82C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_826C")

    #C0382
    ChrTalk(
        0xFE,
        (
            "どうやら、給仕係は\x01",
            "嬢ちゃんにもどったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "どれ、折角だし\x01",
            "食後のドリンクでも\x01",
            "注文するか……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "……って、うわっ！？\x01",
            "配達の出発時間を\x01",
            "過ぎてるじゃねえか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_82BE")

    label("loc_826C")


    #C0385
    ChrTalk(
        0xFE,
        (
            "や、やべえ。\x01",
            "配達の出発時間を\x01",
            "とっくに過ぎてやがる！\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        "い、急がねえと……\x02",
    )

    CloseMessageWindow()

    label("loc_82BE")

    Jump("loc_89E3")

    label("loc_82C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8348")

    #C0387
    ChrTalk(
        0xFE,
        (
            "おや……今日の給仕は\x01",
            "いつもの嬢ちゃんじゃねえのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "ふーむ、なんだか\x01",
            "しっくりこねえ気がするな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_838C")

    label("loc_8348")


    #C0389
    ChrTalk(
        0xFE,
        (
            "やっぱ、この店は\x01",
            "あの給仕係の嬢ちゃんの\x01",
            "笑顔あってこそだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_838C")

    Jump("loc_89E3")

    label("loc_8391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_84F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8471")

    #C0390
    ChrTalk(
        0xFE,
        (
            "導力トラックだと、\x01",
            "今一番性能がいいのは\x01",
            "ヴェルヌ社の最新型だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "しかし、新型となると\x01",
            "ウチの会社もなかなか\x01",
            "手が出せないらしくてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "まあ要するに、それくらい\x01",
            "高価なものってことさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_84F3")

    label("loc_8471")


    #C0393
    ChrTalk(
        0xFE,
        (
            "導力車の最新型を買うってのは\x01",
            "なかなかできることじゃないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "それこそ、よっぽど景気のいい\x01",
            "会社でもないと厳しいだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84F3")

    Jump("loc_89E3")

    label("loc_84F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8577")

    #C0395
    ChrTalk(
        0xFE,
        (
            "うーん、俺も通商会議が\x01",
            "ちょっと気になるところだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "仕事もあるし、\x01",
            "今は腹ごしらえだな。\x01",
            "もぐもぐ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_8577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8602")

    #C0397
    ChrTalk(
        0xFE,
        (
            "いやあ、東通りは\x01",
            "すげえ賑わいだったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "とりあえず、\x01",
            "交通規制は解除されたようだし……\x01",
            "俺も仕事を再開しなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_8602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_87C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_871B")

    #C0399
    ChrTalk(
        0xFE,
        (
            "何でも明日はタングラム門から\x01",
            "東クロスベル街道にかけて、\x01",
            "交通規制が敷かれるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "共和国の大統領が\x01",
            "通商会議に来るってんで、\x01",
            "厳戒態勢を敷くんだそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "まあ、一日中規制されるって\x01",
            "わけじゃないだろうが……\x01",
            "仕事にも多少影響が出そうだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_87C1")

    label("loc_871B")


    #C0402
    ChrTalk(
        0xFE,
        (
            "明日はタングラム門から\x01",
            "東クロスベル街道にかけて、\x01",
            "交通規制が敷かれるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "一日中じゃあないだろうが……\x01",
            "配達スケジュールを\x01",
            "見直しとく必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87C1")

    Jump("loc_89E3")

    label("loc_87C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_884B")

    #C0404
    ChrTalk(
        0xFE,
        (
            "たしか、今日は広い地域で\x01",
            "雨が降ってるって話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "ひどくならねえうちに\x01",
            "仕事を済ませちまったほうが\x01",
            "いいかもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_884B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_89E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892D")

    #C0406
    ChrTalk(
        0xFE,
        (
            "今日は共和国方面から\x01",
            "結構な量の荷物を\x01",
            "あずかっちまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "国境を流れてる\x01",
            "キュレー河っつうでけえ河を横断して、\x01",
            "タングラム丘陵をかっ飛ばしてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "やれやれ、\x01",
            "運送業も楽じゃねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_89E3")

    label("loc_892D")


    #C0409
    ChrTalk(
        0xFE,
        (
            "共和国との国境を流れてる\x01",
            "キュレー河っつうでけえ河を横断して、\x01",
            "タングラム丘陵をかっ飛ばしてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "腹ごしらえも済んだし……\x01",
            "そろそろ市内をひとっ走り\x01",
            "してくるとすっかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89E3")

    TalkEnd(0xFE)
    Return()

    # Function_16_7C4E end

    def Function_17_89E7(): pass

    label("Function_17_89E7")

    TalkBegin(0xFE)

    #C0411
    ChrTalk(
        0xFE,
        "露店の様子も心配だけど……\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "モルス会長やロイくんたちは\x01",
            "大丈夫ッスかねえ……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_89E7 end

    def Function_18_8A45(): pass

    label("Function_18_8A45")

    TalkBegin(0xFE)

    #C0413
    ChrTalk(
        0xFE,
        (
            "リリィ、俺がついてるから\x01",
            "落ち着いてくれ、な？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_8A45 end

    def Function_19_8A7F(): pass

    label("Function_19_8A7F")

    TalkBegin(0xFE)

    #C0414
    ChrTalk(
        0xFE,
        "ディンズ、私怖い……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_8A7F end

    def Function_20_8AA0(): pass

    label("Function_20_8AA0")

    TalkBegin(0xFE)

    #C0415
    ChrTalk(
        0xFE,
        (
            "家にいるウチの亭主も\x01",
            "無事だといいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "ふう、こんなことになるなら\x01",
            "さっさと店を閉めるんだったよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_8AA0 end

    def Function_21_8B19(): pass

    label("Function_21_8B19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B2D")
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    label("loc_8B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B4E")
    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    label("loc_8B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C69")

    #C0417
    ChrTalk(
        0x25,
        (
            "#03204F事態が収拾するまで、我々は\x01",
            "しばらく傍観しているつもりです。\x02\x03",

            "その後は、ルバーチェも赤い星座も\x01",
            "消えたクロスベルの裏社会を\x01",
            "ゆっくりといただくとしましょう。\x02\x03",

            "#03210Fフフ、いずれ皆さんとは\x01",
            "対立する事になるかもしれませんが、\x01",
            "今後ともよろしくお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8D14")

    label("loc_8C69")


    #C0418
    ChrTalk(
        0x25,
        (
            "#03204F事態が収拾するまで、我々は\x01",
            "しばらく傍観しているつもりです。\x02\x03",

            "#03210Fフフ、いずれ皆さんとは\x01",
            "対立する事になるかもしれませんが、\x01",
            "今後ともよろしくお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D14")

    TalkEnd(0xFE)
    Return()

    # Function_21_8B19 end

    def Function_22_8D18(): pass

    label("Function_22_8D18")


    #C0419
    ChrTalk(
        0x25,
        (
            "#03200Fおや、ロイドさんたち……\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#00005Fツァ、ツァオさん！？\x01",
            "こんな所で何を……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x25,
        (
            "#03204Fフフ、私たちがここにいたら\x01",
            "何かおかしいですか？\x02\x03",

            "#03200F街が落ち着いてきた頃なので\x01",
            "食事に羽根を伸ばしている\x01",
            "だけなのですがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x104,
        (
            "#00306Fそれにしたって\x01",
            "堂々としすぎだろ……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        (
            "#00106Fし、しかも宿酒場の\x01",
            "こんなど真ん中の席に……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x26,
        "私もどうかとは思ったのですが……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x26,
        (
            "ウェイトレスの方に案内されて、\x01",
            "ツァオ様も断らなかったもので。\x02",
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

    #C0426
    ChrTalk(
        0x25,
        (
            "#03204Fフフ、いいじゃありませんか。\x01",
            "食事の時くらいゆっくりと\x01",
            "させて欲しいものです。\x02\x03",

            "#03200Fクロスベル市の解放作戦では、\x01",
            "《赤い星座》との戦いに\x01",
            "久しぶりに骨が折れましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x101,
        (
            "#00003F……それに関しては、\x01",
            "ご協力ありがとうございました。\x02\x03",

            "#00001Fツァオさんたちは、これから\x01",
            "どうされるおつもりですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x25,
        (
            "#03205Fしばらくは、事態が収拾するまで\x01",
            "傍観を決め込むつもりですよ。\x02\x03",

            "#03209Fなんらかの形で事件が収束した後は、\x01",
            "新しい事務所を設けて業務を\x01",
            "再開することになるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x103,
        "#00201F……やはりですか。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x25,
        (
            "#03204F《赤い星座》やルバーチェという\x01",
            "競争相手が消えた今、\x01",
            "もはや障害はありませんから。\x02\x03",

            "#03202Fフフ、紆余曲折ありましたが……\x01",
            "クロスベルの裏社会を押さえるという\x01",
            "当初の目的が、ようやく達成出来そうです。\x02\x03",

            "これも、ロイドさんたちと\x01",
            "今までよく働いてくれた《銀》殿の\x01",
            "おかげと言って過言ではないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        "#00013Fくっ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92B9")

    #C0432
    ChrTalk(
        0x106,
        "#10708F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_92B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9314")

    #C0433
    ChrTalk(
        0x10A,
        (
            "#00603F……いずれ《黒月》とは、\x01",
            "再び対立することになるだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93BD")

    label("loc_9314")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_936D")

    #C0434
    ChrTalk(
        0x109,
        (
            "#10103Fいずれ《黒月》とは\x01",
            "再び対立することになりそうですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93BD")

    label("loc_936D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93BD")

    #C0435
    ChrTalk(
        0x105,
        (
            "#10403Fいずれ《黒月》とは\x01",
            "再び対立することになりそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93BD")


    #C0436
    ChrTalk(
        0x25,
        (
            "#03209Fまあ、そういう意味でも……\x01",
            "今後ともよろしくお願いしますよ、\x01",
            "みなさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#00003F……あなたたちがどんな\x01",
            "《壁》として立ち塞がろうと……\x02\x03",

            "#00001F俺たちは絶対に負けませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x25,
        (
            "#03209Fフフ、それでこそロイドさんです。\x02\x03",

            "#03204Fまあ、我々など《壁》としては\x01",
            "大した物ではないでしょう。\x02\x03",

            "#03210F大陸全土の混乱……\x01",
            "とりわけ西の脅威に較べればね。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        "#00011F……そ、それは……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x25,
        (
            "#03204Fフフ、まあひとまずは\x01",
            "この事態を収束させるために\x01",
            "どうか尽力なさってください。\x02\x03",

            "#03200F私たちはここで、\x01",
            "影ながら応援させて頂きますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 1)
    Return()

    # Function_22_8D18 end

    def Function_23_95D4(): pass

    label("Function_23_95D4")


    #C0441
    ChrTalk(
        0x25,
        (
            "#03204Fそうそう……事態が収拾したら、\x01",
            "リーシャさんにも改めて契約を\x01",
            "お願いしようかと思っています。\x02\x03",

            "#03202Fフフ、リーシャさんの\x01",
            "ご都合はいかがでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x106,
        (
            "#10703F……今回、借りが出来ましたし\x01",
            "何らかの形でお礼ができればとは\x01",
            "思っていますが……\x02\x03",

            "#10701F今はまだ、その問いに\x01",
            "『はい』とは言えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        "#00002Fリーシャ……\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x25,
        (
            "#03204Fまあ、こちらにも\x01",
            "強制する権利はありませんしね。\x02\x03",

            "それに今回に関しても、\x01",
            "あくまで対等な協力関係でしたし\x01",
            "貸し借りなどはないでしょう。\x02\x03",

            "#03200Fですが、それでリーシャさんが\x01",
            "負い目を感じるというなら……\x02\x03",

            "#03209FアルカンシェルのＳ席チケットでも\x01",
            "頂ければ、妥当ではないでしょうか。\x02",
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

    #C0445
    ChrTalk(
        0x25,
        (
            "#03204Fフフ、冗談です。\x02\x03",

            "#03200Fただ……前に言った通り、\x01",
            "《黒月》が高みを目指すためには\x01",
            "やはり貴女の力は欲しい。\x02\x03",

            "舞台は応援させていただきますし、\x01",
            "今後ともよいお付き合いを\x01",
            "お願いしますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 2)
    Return()

    # Function_23_95D4 end

    def Function_24_9964(): pass

    label("Function_24_9964")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9979")
    Call(0, 22)
    Jump("loc_9AC8")

    label("loc_9979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A45")

    #C0446
    ChrTalk(
        0xFE,
        (
            "……今回の件に関しては、\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "古戦場の隠れ処も、\x01",
            "先ほど引き払ってきた所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "我々が協力できる事は\x01",
            "もはやありませんが……\x01",
            "どうかお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_9AC8")

    label("loc_9A45")


    #C0449
    ChrTalk(
        0xFE,
        (
            "古戦場の隠れ処も、\x01",
            "先ほど引き払ってきた所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "我々が協力できる事は\x01",
            "もはやありませんが……\x01",
            "どうかお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AC8")

    TalkEnd(0xFE)
    Return()

    # Function_24_9964 end

    def Function_25_9ACC(): pass

    label("Function_25_9ACC")

    TalkBegin(0xFE)

    #C0451
    ChrTalk(
        0xFE,
        "今日は家族みんなで外食に来たんだ。\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "ふふ、楽しんでくれているようで\x01",
            "なによりだよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_9ACC end

    def Function_26_9B2E(): pass

    label("Function_26_9B2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BF8")

    #C0453
    ChrTalk(
        0xFE,
        "はふはふ、ちゅるちゅる……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "このタンメンというのも、\x01",
            "ぴりりと辛くて刺激的な味ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        (
            "こんなに汗をかくお食事は\x01",
            "生まれてはじめて……\x01",
            "だけど、とっても美味しいですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9C6C")

    label("loc_9BF8")


    #C0456
    ChrTalk(
        0xFE,
        (
            "このタンメンというお料理、\x01",
            "とても気に入りましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "辛さで汗がだくだくですけど、\x01",
            "とっても美味しいですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C6C")

    TalkEnd(0xFE)
    Return()

    # Function_26_9B2E end

    def Function_27_9C70(): pass

    label("Function_27_9C70")

    TalkBegin(0xFE)

    #C0458
    ChrTalk(
        0xFE,
        (
            "今日は家族みんなで\x01",
            "外食しにきたんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "まむまむ……\x01",
            "この『まあぼお』というのは、\x01",
            "ぜっぴんですわね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_9C70 end

    def Function_28_9CE8(): pass

    label("Function_28_9CE8")

    TalkBegin(0xFE)

    #C0460
    ChrTalk(
        0xFE,
        "ごろごろにゃーん……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_9CE8 end

    def Function_29_9D09(): pass

    label("Function_29_9D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A12B")

    #C0461
    ChrTalk(
        0x20,
        (
            "はー、ティマスさんにゃ悪いが\x01",
            "ここの料理は最高だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x20,
        (
            "もぐもぐ……\x01",
            "よし、おかわりしちまうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#00005Fあれ、クロスベル警備隊の人が\x01",
            "こんなところに……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x109,
        (
            "#10100Fもしかして……\x01",
            "アレクセイさんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x20, 0x10)
    TurnDirection(0x20, 0x109, 0)
    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E98")
    Jump("loc_9EE2")

    label("loc_9E98")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9EB8")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9EE2")

    label("loc_9EB8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9ED8")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9EE2")

    label("loc_9ED8")

    OP_52(0x20, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9EE2")

    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x20, 0x10)

    #C0465
    ChrTalk(
        0x20,
        (
            "おや、ノエル曹長。\x01",
            "こいつは奇遇だねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x20,
        (
            "今は休憩時間でね。\x01",
            "ちょっと羽根を伸ばして\x01",
            "ここで食ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x109,
        (
            "#10106Fあ、相変わらずですね。\x01",
            "わざわざ昼食のために、\x01",
            "雨の中タングラム門から……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x105,
        (
            "#10300Fタングラム門……\x01",
            "東の街道の先にある\x01",
            "国境門のことだったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x102,
        (
            "#00100Fええ、警備隊が詰めている\x01",
            "クロスベルの重要な守備地点よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x20,
        (
            "最近は新しい副司令が赴任して、\x01",
            "色々と忙しくなっちまってるけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x20,
        (
            "ノエル曹長、\x01",
            "そっちも大変だろうが頑張ってくれ。\x01",
            "門のみんなも応援してるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x109,
        "#10109Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 6)
    ClearChrFlags(0x20, 0x10)
    Jump("loc_A2BC")

    label("loc_A12B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A21E")

    #C0473
    ChrTalk(
        0x20,
        (
            "最近、新しい副司令が赴任してきて\x01",
            "警備隊も忙しかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x20,
        (
            "その新しい副司令ってのが\x01",
            "ソーニャ司令に負けず劣らずの\x01",
            "厳しいお人でな……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x20,
        (
            "たまには街まで羽根を伸ばして、\x01",
            "変わったモンでも食って\x01",
            "リフレッシュしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_A2BC")

    label("loc_A21E")


    #C0476
    ChrTalk(
        0x20,
        (
            "新しい副司令ってのが\x01",
            "ソーニャ司令に負けず劣らずの\x01",
            "厳しいお人でな……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x20,
        (
            "たまには街まで羽根を伸ばして、\x01",
            "変わったモンでも食って\x01",
            "リフレッシュしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2BC")

    TalkEnd(0xFE)
    Return()

    # Function_29_9D09 end

    def Function_30_A2C0(): pass

    label("Function_30_A2C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A32F")

    #C0478
    ChrTalk(
        0xFE,
        (
            "せっかくの旅行だというのに、\x01",
            "雨など降りおるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xFE,
        (
            "大した雨じゃないが\x01",
            "肌寒いわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A372")

    label("loc_A32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A372")

    #C0480
    ChrTalk(
        0xFE,
        "うむ、うまいうまい。\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        "やはり東方料理は最高じゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_A372")

    TalkEnd(0xFE)
    Return()

    # Function_30_A2C0 end

    def Function_31_A376(): pass

    label("Function_31_A376")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A3D6")

    #C0482
    ChrTalk(
        0xFE,
        "まあまあ、おじいさん。\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "ここは暖かいものでも食べて\x01",
            "温まりましょうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A40C")

    label("loc_A3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A40C")

    #C0484
    ChrTalk(
        0xFE,
        (
            "やっぱり、故郷の料理が\x01",
            "口に合うわねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A40C")

    TalkEnd(0xFE)
    Return()

    # Function_31_A376 end

    def Function_32_A410(): pass

    label("Function_32_A410")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A4A6")

    #C0485
    ChrTalk(
        0xFE,
        (
            "（ペラペラ……）\x01",
            "もぐもぐ……ふむふむ……\x01",
            "この観光ガイドによると……\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "なかなか景色のいい場所が\x01",
            "多いようだね、クロスベルは。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5C3")

    label("loc_A4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A533")

    #C0487
    ChrTalk(
        0xFE,
        (
            "（カチャカチャ……）\x01",
            "ズズー……うまいうまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "泊まっていた記者さんたち、\x01",
            "足早に取材にむかったようだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5C3")

    label("loc_A533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A5C3")

    #C0489
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……やはり\x01",
            "クロスベルというのは、\x01",
            "やはり景気がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "通商会議にあわせて、\x01",
            "街が盛り上がっているのを感じるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5C3")

    TalkEnd(0xFE)
    Return()

    # Function_32_A410 end

    def Function_33_A5C7(): pass

    label("Function_33_A5C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A634")

    #C0491
    ChrTalk(
        0xFE,
        "あなた、あなたったら。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "本を読むのは食事が\x01",
            "終わってからにしなさい、\x01",
            "みっともない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6F1")

    label("loc_A634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A695")

    #C0493
    ChrTalk(
        0xFE,
        "あなた、あなたったら。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "食事中に音を立てるのは\x01",
            "やめなさい、みっともない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6F1")

    label("loc_A695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A6F1")

    #C0495
    ChrTalk(
        0xFE,
        "あなた、あなたったら。\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "食べながらしゃべるのは\x01",
            "やめなさい、みっともない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6F1")

    TalkEnd(0xFE)
    Return()

    # Function_33_A5C7 end

    def Function_34_A6F5(): pass

    label("Function_34_A6F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A89F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A826")

    #C0497
    ChrTalk(
        0xFE,
        (
            "今日で飛行船も\x01",
            "運行しなくなるって話だからね。\x01",
            "仕方なくリベールに帰ることにしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        (
            "この状況、本当ならもう少し\x01",
            "取材を続けたい所だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "……とにかく、クロスベルには\x01",
            "どうか安全であってもらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        (
            "是非はどうあれ、\x01",
            "国防軍の活躍には期待しているわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A89A")

    label("loc_A826")


    #C0501
    ChrTalk(
        0xFE,
        (
            "とにかく、クロスベルには\x01",
            "どうか安全であって欲しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        (
            "是非はどうあれ、\x01",
            "国防軍の活躍には期待しているわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A89A")

    Jump("loc_ACF7")

    label("loc_A89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A8C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8BA")
    Call(0, 45)
    Jump("loc_A8BD")

    label("loc_A8BA")

    Call(0, 46)

    label("loc_A8BD")

    Jump("loc_ACF7")

    label("loc_A8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AC5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABBE")

    #C0503
    ChrTalk(
        0xFE,
        (
            "あら、特務支援課の\x01",
            "皆さんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        "#00005Fあなたは確かリベール通信の。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x102,
        (
            "#00100Fまたクロスベルに\x01",
            "いらしていたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "ふふ、実は通商会議以降\x01",
            "帰っていないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        (
            "何せ、独立提唱なんて\x01",
            "センセーショナルな提案が\x01",
            "行われたものだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "急遽、長期取材を命じられて、\x01",
            "住民投票まで見届けることに\x01",
            "なったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        "#00104Fなるほど、そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        (
            "ちなみに、せっかくだから\x01",
            "アルカンシェルの\x01",
            "リニューアル公演も観る予定よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        "それも公開日の初日にね。\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x109,
        (
            "#10105F公開日の初日……\x01",
            "よくチケットが手に入りましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x103,
        (
            "#00200Fええ、あまりの競争率で\x01",
            "プレミアが付いているそうですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        (
            "ふふ、まあ記者には\x01",
            "色々と裏技があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "ま、そんなわけで\x01",
            "あとしばらくの間、街で\x01",
            "会ったりした時はよろしくね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 0)
    Jump("loc_AC58")

    label("loc_ABBE")


    #C0516
    ChrTalk(
        0xFE,
        (
            "リニューアル公演を観て\x01",
            "住民投票を見届けたら、\x01",
            "私のクロスベル取材も終了よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xFE,
        (
            "ま、そんなわけで\x01",
            "あとしばらくの間、街で\x01",
            "会ったりした時はよろしくね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC58")

    Jump("loc_ACF7")

    label("loc_AC5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ACF7")

    #C0518
    ChrTalk(
        0xFE,
        (
            "ふふ、ここのお店\x01",
            "東方人街並みにおいしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "もしかしたらナイアル君たちも\x01",
            "今頃こんな美味しい東方料理を\x01",
            "食べている所かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACF7")

    TalkEnd(0xFE)
    Return()

    # Function_34_A6F5 end

    def Function_35_ACFB(): pass

    label("Function_35_ACFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD0D")
    Call(0, 37)
    Jump("loc_ADB2")

    label("loc_AD0D")

    TalkBegin(0xFE)

    #C0520
    ChrTalk(
        0x17,
        (
            "#02109Fさてと、食事を終えたら\x01",
            "とにかく街を取材して回るわよ～。\x02\x03",

            "#02104F首脳のガードは固いけど、\x01",
            "移動中とかなら何かしらチャンスが\x01",
            "あるかもしれないしね～♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_ADB2")

    Return()

    # Function_35_ACFB end

    def Function_36_ADB3(): pass

    label("Function_36_ADB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADC5")
    Call(0, 37)
    Jump("loc_AE5C")

    label("loc_ADC5")

    TalkBegin(0xFE)

    #C0521
    ChrTalk(
        0xFE,
        (
            "午後からは基本的に、\x01",
            "市民の街頭インタビューを\x01",
            "集めて回る予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "あわよくば、どこかで首脳の姿を\x01",
            "撮影できればというところですね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_AE5C")

    Return()

    # Function_36_ADB3 end

    def Function_37_AE5D(): pass

    label("Function_37_AE5D")

    EventBegin(0x0)
    Fade(500)
    OP_68(9150, 1230, 4310, 0)
    MoveCamera(40, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 9500, 0, 5800, 180)
    SetChrPos(0x102, 11000, 0, 5410, 180)
    SetChrPos(0x104, 8000, 0, 5410, 180)
    SetChrPos(0x109, 10650, 0, 6220, 180)
    SetChrPos(0x105, 9250, 0, 6620, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_0D()
    SetChrSubChip(0x18, 0x1)
    Sleep(200)

    #C0523
    ChrTalk(
        0x18,
        "#6Pおや、支援課の皆さん。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x17, 0x2)
    Sleep(200)

    #C0524
    ChrTalk(
        0x17,
        (
            "#12P#02100Fもしかして、\x01",
            "ロイド君たちも食事？\x02\x03",

            "#02109Fふふ、それはともかく\x01",
            "除幕式はすごかったわね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        "#00000Fええ、確かに物凄かったですね。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#00104F首脳たちのオーラには\x01",
            "本当に圧倒されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x17,
        (
            "#12P#02106Fでしょでしょ？\x01",
            "特に《鉄血宰相》の存在感は\x01",
            "ハンパじゃないわよね～！\x02\x03",

            "#02100Fあたしもあれだけ近くで\x01",
            "見たのは初めてだったけど、\x01",
            "改めて凄みを思い知らされたわよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0528
    ChrTalk(
        0x17,
        (
            "#12P#02105Fそうそう、そういえば\x01",
            "その宰相の傍にいた\x01",
            "書記官風の男性だけど……\x02\x03",

            "#02103Fあれって、以前からクロスベルに\x01",
            "来ていたレクターって子で\x01",
            "間違いないわよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        "#00005Fえっと、それは……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x17,
        (
            "#12P#02104Fふふ、まあ確かに\x01",
            "答えにくいのは分かるけど。\x02\x03",

            "#02101F――実はあたしも１つ、\x01",
            "思い出した事があったのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0531
    ChrTalk(
        0x101,
        "#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x109,
        "#10105Fそれはどういう……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x17,
        (
            "#12P#02103F……去年の春頃、鉄血宰相と\x01",
            "ハルトマン議長が極秘裏かつ\x01",
            "非公式に会談を行った……\x02\x03",

            "#02100Fロイド君たちも当然、\x01",
            "その事は知っているわよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        "#00005Fええ、それはまあ……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x102,
        (
            "#00103Fある程度の情報筋では\x01",
            "もはや有名な事実ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x17,
        (
            "#12P#02103Fええ……\x01",
            "けど、当時はそうじゃなかった。\x02\x03",

            "クロスベルのマスコミはおろか、\x01",
            "帝国のマスコミも……\x02\x03",

            "#02101Fもちろんクロスベル警察にしても\x01",
            "その情報を一切#4R㈲　㈲#、掴めなかったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x18,
        (
            "#6P……しかも、あれほどの\x01",
            "重要人物にも関わらず護衛を\x01",
            "ほとんど付けなかったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x18,
        (
            "#6Pまるでふらっと散歩の途中で\x01",
            "立ち寄ったかのように……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x18,
        (
            "#6P……まあ、だからこそ逆に\x01",
            "秘密が守られたとも言えますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x105,
        "#10303Fふむ……何とも凄い話だね。\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        "#00301Fああ、正直あり得ねえな。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x17,
        (
            "#12P#02106Fそう、あり得ない――\x01",
            "というか悔しすぎるでしょ！\x02\x03",

            "#02100Fだからあたし、後から\x01",
            "手を尽くして色々調べたのよ。\x02\x03",

            "#02103F結果、会談のセッティングに\x01",
            "関わったと思われる人物の名前が\x01",
            "何名か挙がったんだけど……\x02\x03",

            "#02101Fその中にあったのを思い出したのよ。\x01",
            "レクターという男性の名前がね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0543
    ChrTalk(
        0x101,
        (
            "#00005F彼が宰相と共に\x01",
            "会談に参加した事自体は\x01",
            "把握していましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#00101Fそれをセッティングしたのも\x01",
            "レクターさんの仕業……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x109,
        (
            "#10106F何ていうか……\x01",
            "凄まじい防諜スキルですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x17,
        (
            "#12P#02103F……そう、そしてそんなことが\x01",
            "一介の書記官に出来るはずがないわ。\x02\x03",

            "#02102Fそれこそ、かの名高き\x01",
            "帝国軍情報局の人間でもない限り、ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#00005Fな、なるほど……\x02\x03",

            "#00003F（自力でそこまで辿り着くなんて\x01",
            "  グレイスさんも相当だな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x104,
        "#00306F（ああ、凄まじい執念だぜ。）\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x17,
        (
            "#12P#02109Fふふ、どうやら図星って顔ね？\x02\x03",

            "#02106Fはぁ、でもまさか\x01",
            "あの子がそのレクターとは\x01",
            "露にも思わなかったのよね～。\x02\x03",

            "#02102Fま、ロイド君たちにも立場が\x01",
            "あるでしょうから、\x01",
            "これ以上は止めておくけど……\x02\x03",

            "#02100Fとにかく、あのレクターって子が\x01",
            "とことん尋常じゃないのは確かよ。\x02\x03",

            "ロイド君たちも、\x01",
            "今後とも関わることがあるのなら\x01",
            "せいぜい気を引き締めていくことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        "#00000Fええ、心得ています。\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#00100F情報ありがとうございました。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x0, 9420, 0, 5800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0x148, 0)
    EventEnd(0x5)
    Return()

    # Function_37_AE5D end

    def Function_38_BA8D(): pass

    label("Function_38_BA8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BBB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB3F")

    #C0552
    ChrTalk(
        0xFE,
        (
            "ダンナと喧嘩して\x01",
            "家出してたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "ついに昨日、泣かれながら\x01",
            "謝られちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "う、うーん。\x01",
            "そこまでされると\x01",
            "微妙に罪悪感が……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BBB4")

    label("loc_BB3F")


    #C0555
    ChrTalk(
        0xFE,
        (
            "ふう、まあいい加減\x01",
            "家出も飽きたしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "なんだか事件も\x01",
            "起こってるみたいだし……\x01",
            "そろそろ家に戻る事にするわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBB4")

    Jump("loc_BD8F")

    label("loc_BBB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BC43")

    #C0557
    ChrTalk(
        0xFE,
        (
            "喧嘩したダンナに見つかってね。\x01",
            "家に帰るように言われたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        (
            "フン、あんな謝り方じゃダメね。\x01",
            "誠意が伝わってこないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8F")

    label("loc_BC43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BCBA")

    #C0559
    ChrTalk(
        0xFE,
        (
            "給仕係さんがいつもの人に\x01",
            "なったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        (
            "さっきの頼りない\x01",
            "ウェイターさんは\x01",
            "なんだったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8F")

    label("loc_BCBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BD1C")

    #C0561
    ChrTalk(
        0xFE,
        (
            "なんだか給仕係さんが\x01",
            "頼りないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "さっさと料理を\x01",
            "持ってきてほしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8F")

    label("loc_BD1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BD8F")

    #C0563
    ChrTalk(
        0xFE,
        (
            "ダンナと喧嘩しちゃったから、\x01",
            "プチ家出してきたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "ふん……\x01",
            "謝るまで許してあげないんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD8F")

    TalkEnd(0xFE)
    Return()

    # Function_38_BA8D end

    def Function_39_BD93(): pass

    label("Function_39_BD93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BDF7")

    #C0565
    ChrTalk(
        0xFE,
        (
            "あーあ、ぼくもいい加減\x01",
            "ママの実家は飽きちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        "パパに会いたいなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BDF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BE32")

    #C0567
    ChrTalk(
        0xFE,
        (
            "パパ、まだこっちに\x01",
            "こないのかなあ……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BE32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BE67")

    #C0568
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "えへへ、おいしいね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BE67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BEC4")

    #C0569
    ChrTalk(
        0xFE,
        (
            "ママー、机がなんだか\x01",
            "べたべたしてるー。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        "店の人が拭き忘れたのかなー？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BEC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BF2A")

    #C0571
    ChrTalk(
        0xFE,
        "ママの実家に遊びにきたんだー。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "パパはあとで来るんだって。\x01",
            "お仕事が忙しいんだねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF2A")

    TalkEnd(0xFE)
    Return()

    # Function_39_BD93 end

    def Function_40_BF2E(): pass

    label("Function_40_BF2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C182")

    #C0573
    ChrTalk(
        0x1D,
        (
            "#04405Fあ……みなさん、\x01",
            "こんな所で奇遇ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        (
            "#00005Fえっと、お食事中……\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x1D,
        (
            "#04400Fええ、休憩をいただけたので\x01",
            "昼食をとりに来たところです。\x02\x03",

            "#04403Fこちらのチャーハンは、\x01",
            "深みのあるいい味が出ていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、リースさんったら\x01",
            "相変わらずですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x109,
        "#10109Fお、おいしそうです、けど……\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x104,
        (
            "#00303F（なんだかカウンターの上に\x01",
            "  皿がたくさん乗ってるんだが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x105,
        (
            "#10304F（フフ、それに\x01",
            "  龍老飯店にシスターってのも\x01",
            "  なかなかミスマッチだよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x103,
        (
            "#00200F（エリィさんが\x01",
            "  つっこまないところをみると、\x01",
            "  これが普通なのでは……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 3)
    Jump("loc_C1F3")

    label("loc_C182")


    #C0581
    ChrTalk(
        0x1D,
        (
            "#04400F私はもう少ししたら\x01",
            "大聖堂のほうに戻るつもりです。\x02\x03",

            "何かありましたら\x01",
            "そちらにいらっしゃってください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1F3")

    TalkEnd(0xFE)
    Return()

    # Function_40_BF2E end

    def Function_41_C1F7(): pass

    label("Function_41_C1F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183E, 7)), scpexpr(EXPR_END)), "loc_C26D")

    #C0582
    ChrTalk(
        0xFE,
        (
            "街の復旧のために、\x01",
            "色々とボランティアしてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        (
            "汗を流した後の食事は\x01",
            "本当に格別だね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183E, 7)
    Jump("loc_C2D1")

    label("loc_C26D")


    #C0584
    ChrTalk(
        0xFE,
        (
            "旧市街のほうはまだまだ\x01",
            "復旧作業中みたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "オレにもまだまだ\x01",
            "手伝える事があるかもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2D1")

    TalkEnd(0xFE)
    Return()

    # Function_41_C1F7 end

    def Function_42_C2D5(): pass

    label("Function_42_C2D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C39B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C307")
    Call(0, 54)
    Return()

    label("loc_C307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_C396")

    #C0586
    ChrTalk(
        0xFE,
        (
            "ああ、これでようやく\x01",
            "父さんに会うことができるかもしれない！\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "とにかく、全部君たちに任せるよ。\x01",
            "どうか父さんを探し出してくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C396")

    Jump("loc_C3E8")

    label("loc_C39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C3E8")

    #C0588
    ChrTalk(
        0xFE,
        (
            "エアリーにアルミン……\x01",
            "昨日はとっても素晴らしい\x01",
            "１日だったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3E8")

    TalkEnd(0xFE)
    Return()

    # Function_42_C2D5 end

    def Function_43_C3EC(): pass

    label("Function_43_C3EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C41E")
    Call(0, 54)
    Return()

    label("loc_C41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_C4BE")

    #C0589
    ChrTalk(
        0xFE,
        (
            "私たち、きっとアルムのお父さまに\x01",
            "ご挨拶できるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        (
            "私たちの愛の結晶、アルミンを\x01",
            "ぜひともだっこしてもらわないとね！\x02",
        )
    )

    CloseMessageWindow()

    #N0591
    NpcTalk(
        0xFE,
        "赤ん坊",
        "ばっぶー。\x02",
    )

    CloseMessageWindow()

    label("loc_C4BE")

    Jump("loc_C523")

    label("loc_C4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C523")

    #C0592
    ChrTalk(
        0xFE,
        (
            "ええ、アルム……\x01",
            "昨日はとてもとても\x01",
            "素晴らしい１日だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #N0593
    NpcTalk(
        0xFE,
        "赤ん坊",
        "ばぶぅ♪\x02",
    )

    CloseMessageWindow()

    label("loc_C523")

    TalkEnd(0xFE)
    Return()

    # Function_43_C3EC end

    def Function_44_C527(): pass

    label("Function_44_C527")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C53C")
    Call(0, 45)
    Jump("loc_C53F")

    label("loc_C53C")

    Call(0, 46)

    label("loc_C53F")

    TalkEnd(0xFE)
    Return()

    # Function_44_C527 end

    def Function_45_C543(): pass

    label("Function_45_C543")


    #C0594
    ChrTalk(
        0x27,
        (
            "なるほど、こちらにいる間は\x01",
            "龍老飯店に宿を取っているんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x27,
        (
            "ここは食事も絶品なので\x01",
            "快適でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x16,
        (
            "ええ、おかげで\x01",
            "食べすぎないようにするのが\x01",
            "大変ですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x16,
        (
            "ですが、今日はわざわざ\x01",
            "来ていただいてすみません。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x16,
        (
            "本当ならこちらから\x01",
            "出向くべきだったんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x27,
        "ふふ、気にしないで下さい。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x27,
        (
            "散歩と放浪は私の\x01",
            "趣味みたいなものですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x16,
        "ふふ、なるほど。\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x16,
        (
            "流石は天下の\x01",
            "フリージャーナリストですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Return()

    # Function_45_C543 end

    def Function_46_C6F7(): pass

    label("Function_46_C6F7")


    #C0603
    ChrTalk(
        0x16,
        (
            "ですが、ニールセンさんは\x01",
            "今回はずいぶん長く\x01",
            "留まられていますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x16,
        (
            "やはり、故郷の動静は\x01",
            "気になりますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x27,
        (
            "そうですね、何というか\x01",
            "肌で感じたいというのは\x01",
            "あるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x27,
        (
            "とにかく、まだしばらくは\x01",
            "クロスベルにいるつもりです。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_46_C6F7 end

    def Function_47_C7EE(): pass

    label("Function_47_C7EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C803")
    Call(0, 48)
    Jump("loc_C8C3")

    label("loc_C803")


    #C0607
    ChrTalk(
        0x1C,
        (
            "#01803F共和国にいた頃は、\x01",
            "父の仕事の都合で引越しを\x01",
            "繰り返していましたし……\x02\x03",

            "#01802Fふふ、サンサンには\x01",
            "本当に感謝しているんです。\x02\x03",

            "皆さんやイリアさんたちとの絆も\x01",
            "大切にしていきたいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8C3")

    TalkEnd(0xFE)
    Return()

    # Function_47_C7EE end

    def Function_48_C8C7(): pass

    label("Function_48_C8C7")

    EventBegin(0x0)
    Fade(500)
    OP_68(13370, 1400, -1550, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16720, 0)
    SetChrPos(0x1C, 13800, 50, -320, 180)
    SetChrSubChip(0x1C, 0x0)
    OP_4B(0xA, 0xFF)
    OP_93(0xA, 0xE1, 0x0)
    SetChrPos(0x101, 13620, 0, -1520, 0)
    SetChrPos(0x102, 13450, 0, -2830, 0)
    SetChrPos(0x103, 12500, 0, -2220, 45)
    SetChrPos(0x104, 11630, 0, -460, 90)
    SetChrPos(0x109, 12250, 0, -3430, 0)
    SetChrPos(0x105, 11670, 0, -1620, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0608
    ChrTalk(
        0x1C,
        (
            "#01802Fあっ……\x01",
            "こんにちは、みなさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        "#12P#00100Fふふ、こんにちはリーシャさん。\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        "#12P#00000F今日は食事に来てたのかい？\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x1C,
        (
            "#01802Fふふ、はい。\x02\x03",

            "今は食後のデザートをいただきつつ、\x01",
            "おしゃべりをしていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xA,
        (
            "#11Pあなたたち、\x01",
            "たしか警察のヒトだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xA,
        (
            "#11Pも～、せっかくリーシャと\x01",
            "ガールズトークを楽しんでたのに～。\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x104,
        "#6P#00302Fハハ、そいつは悪かったな。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x109,
        (
            "#12P#10100Fでも、アーティストの方の\x01",
            "プライベートに遭遇できるって\x01",
            "やっぱり貴重な感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x105,
        (
            "#6P#10304F確かに。\x01",
            "有名人は交友関係とかも\x01",
            "なかなか見えにくいしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x1C,
        (
            "#01809Fあはは……\x01",
            "そんな、まだまだ新人ですけど。\x02\x03",

            "#01802Fサンサンは休日、家にこもりがちな私を\x01",
            "よく遊びに連れ出してくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xA,
        "#11Pふふ、同い年だから話も合うんだよね～。\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xA,
        (
            "#11Pそれと、リーシャのプロポーションでも\x01",
            "可愛く着られる服を探すのが楽しいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x1C,
        (
            "#01809Fあはは、なかなか可愛いのって\x01",
            "見つからないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x102,
        (
            "#12P#00103F（うーん、確かにリーシャさんだと\x01",
            "  あんまりサイズがなさそうね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x103,
        "#12P#00203F（……贅沢な悩みかと。）\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        "#12P#00002Fはは、でも本当に仲がいいんだな。\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x1C,
        (
            "#01802Fふふ、サンサンには本当に\x01",
            "感謝しているんです。\x02\x03",

            "#01803F共和国にいた頃は、\x01",
            "父の仕事の都合で引越しを\x01",
            "繰り返していましたし……\x02\x03",

            "#01808F友達と呼べる人なんて\x01",
            "なかなか出来なくて、\x01",
            "いつも一人ぼっちでしたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x104,
        "#6P#00303Fそうだったのか……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x1C, 500)

    #C0626
    ChrTalk(
        0xA,
        "#11Pふふ、安心してリーシャ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x1)

    #C0627
    ChrTalk(
        0xA,
        (
            "#11P私と友達になった以上、\x01",
            "一人ぼっちなんてありえないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xA,
        (
            "#11Pこうなったら墓場まで\x01",
            "一緒だからね！　リーシャ。\x02",
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
    OP_63(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0629
    ChrTalk(
        0x1C,
        (
            "#01802Fあはは……\x01",
            "ありがとう、サンサン。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、どうやら\x01",
            "僕たちはお邪魔虫みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x109,
        (
            "#12P#10102Fうん、そろそろ\x01",
            "お暇させてもらおっか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x0)

    #C0632
    ChrTalk(
        0x1C,
        (
            "#01806Fすみません、皆さん。\x01",
            "何だか時間を取らせちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x101,
        (
            "#12P#00004Fいや、リーシャと話せて\x01",
            "俺たちもいい息抜きになったよ。\x02\x03",

            "#00002Fそれじゃ、俺たちはこれで。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x1C,
        "#01802Fはい、それではまた。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17C, 2)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4C(0xA, 0xFF)
    SetChrPos(0x1C, 14000, 50, 0, 90)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13390, 0, -1690, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_48_C8C7 end

    def Function_49_D1BA(): pass

    label("Function_49_D1BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x28)
    SetChrChipByIndex(0x28, 0x28)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 17010, 0, 15370, 315)
    SetChrFlags(0x9, 0x80)
    OP_4B(0x8, 0xFF)
    OP_68(-200, 1400, -640, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16270, 0)
    SetChrPos(0x101, -200, 0, 600, 90)
    SetChrPos(0x102, -600, 0, -600, 90)
    SetChrPos(0x109, -1400, 0, 600, 90)
    SetChrPos(0x105, -1800, 0, -600, 90)

    def lambda_D26F():
        OP_98(0x101, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D26F)
    Sleep(50)

    def lambda_D28C():
        OP_98(0x102, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D28C)
    Sleep(50)

    def lambda_D2A9():
        OP_98(0x109, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D2A9)
    Sleep(50)

    def lambda_D2C6():
        OP_98(0x105, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D2C6)
    OP_68(890, 1400, -390, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_0D()

    def lambda_D308():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D308)
    Sleep(50)

    def lambda_D318():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D318)
    Sleep(50)

    def lambda_D328():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D328)
    Sleep(50)

    def lambda_D338():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D338)
    Sleep(50)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0635
    ChrTalk(
        0x101,
        "#12P#00001Fいた……！\x02",
    )

    CloseMessageWindow()
    OP_68(15600, 1400, 15180, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(13750, 3000)
    OP_6F(0x1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7518", 0)
    Sleep(100)

    #C0636
    ChrTalk(
        0x28,
        (
            "#03500Fなるほどねぇ……\x01",
            "花山椒ってのを使うのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x8,
        (
            "#6Pそう、ただの山椒とは\x01",
            "辛さも風味も段違い。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x8,
        (
            "#6P東方でしか栽培されてないけど\x01",
            "最近は鉄道便で注文できるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x28,
        (
            "#03502F#11Pいや～、自分でマーボー作ると\x01",
            "どうも物足りなかったんだよなァ。\x02\x03",

            "#03504F『麻#2Rマー#』か……\x01",
            "ひとつ勉強になったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 5010, 0, 15540, 45)

    #C0640
    ChrTalk(
        0x101,
        (
            "#00000F#Nレクターさん……\x01",
            "こちらに居ましたか。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0xA, 0x80)
    OP_63(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(13510, 1400, 14500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15950, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 13000, 0, 14500, 90)
    SetChrPos(0x102, 12600, 0, 15500, 90)
    SetChrPos(0x109, 12000, 0, 14250, 90)
    SetChrPos(0x105, 11500, 0, 15250, 90)
    SetChrPos(0x28, 16010, 0, 14370, 270)
    OP_93(0x8, 0xE1, 0x0)

    def lambda_D644():
        OP_98(0x101, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D644)
    Sleep(50)

    def lambda_D661():
        OP_98(0x102, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D661)
    Sleep(50)

    def lambda_D67E():
        OP_98(0x109, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D67E)
    Sleep(50)

    def lambda_D69B():
        OP_98(0x105, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D69B)
    Sleep(50)
    OP_68(14290, 1400, 14500, 1500)
    OP_0D()

    #C0641
    ChrTalk(
        0x102,
        "#6P#00105F（あっさり見つかったわね……）\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x109,
        (
            "#6P#10106F（な、何だかものすごく\x01",
            "  チャランポランそうな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x105,
        (
            "#6P#10300F（あとは身分確認が出来れば\x01",
            "  ミッション終了だけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x28,
        (
            "#03505Fおー、遅かったな。\x02\x03",

            "#03509F待ってたぜぇ、心の友よ！\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x101,
        "#00005Fへっ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x8, 500)
    Sleep(100)

    #C0646
    ChrTalk(
        0x28,
        (
            "#12P#03502Fマスター。\x01",
            "コイツらがさっき言った連中だ。\x02\x03",

            "#03504Fやる気と根性だけはあるから\x01",
            "ビシビシしごいてやってくれ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x28, 500)
    Sleep(100)

    #C0647
    ChrTalk(
        0x8,
        "わかった、任せるね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    #C0648
    ChrTalk(
        0x8,
        (
            "#11P４人というのは大変だけど\x01",
            "東方料理が広まるのは嬉しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x8,
        "#11P頑張って付いてくるよろし！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(100)

    #C0650
    ChrTalk(
        0x101,
        "#6P#00012Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x102,
        "#6P#00105Fいったい何の話を……\x02",
    )

    CloseMessageWindow()
    OP_68(11460, 1400, 11810, 1000)
    MoveCamera(41, 17, 0, 1000)
    OP_93(0x28, 0x10E, 0x0)
    OP_98(0x28, 0xFFFFF254, 0x0, 0xFFFFFB50, 0x1770, 0x0)
    OP_93(0x28, 0xB4, 0x0)
    Sleep(50)
    Sound(809, 0, 70, 0)
    OP_9D(0x28, 0x2B2A, 0x0, 0x2382, 0x2BC, 0x7D0)
    Sleep(100)
    OP_93(0x28, 0xE1, 0x0)
    OP_98(0x28, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1770, 0x0)
    OP_6F(0x1)
    WaitChrThread(0x101, 3)
    SetChrFlags(0x28, 0x80)
    OP_0D()

    def lambda_D9C0():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9C0)
    Sleep(50)

    def lambda_D9D0():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D9D0)
    Sleep(50)

    def lambda_D9E0():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D9E0)
    Sleep(50)

    def lambda_D9F0():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D9F0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0652
    ChrTalk(
        0x101,
        "#11P#00011Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x109,
        "#5P#10105Fに、逃げた……！\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x105,
        "#5P#10309Fハハ、相変わらずだなぁ。\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x102,
        "#5P#00107Fお、追いかけないと！\x02",
    )

    CloseMessageWindow()

    def lambda_DAEE():
        OP_98(0x8, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DAEE)
    Sound(802, 0, 100, 0)
    OP_68(13640, 1400, 14410, 1000)
    MoveCamera(37, 24, 0, 1000)

    #C0656
    ChrTalk(
        0x8,
        "コラ、どこに行く！？\x02",
    )

    CloseMessageWindow()
    OP_6F(0x1)
    WaitChrThread(0x8, 1)

    #C0657
    ChrTalk(
        0x8,
        (
            "もう修行は始まている！\x01",
            "まずは下ごしらえの練習ね！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DB81():
        OP_93(0x101, 0x5A, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB81)
    Sleep(50)

    def lambda_DB91():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB91)
    Sleep(50)

    def lambda_DBA1():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DBA1)
    Sleep(50)

    def lambda_DBB1():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DBB1)

    #C0658
    ChrTalk(
        0x101,
        "#6P#00011Fい、いや、違うんです！\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x102,
        (
            "#6P#00106F私たち、クロスベル警察に\x01",
            "所属する者で──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    OP_68(15810, 1400, 13900, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15910, 0)
    SetChrPos(0x101, 15500, 0, 14370, 0)
    SetChrPos(0x102, 16500, 0, 14370, 0)
    SetChrPos(0x109, 15500, 0, 13370, 0)
    SetChrPos(0x105, 16500, 0, 13370, 0)
    SetChrPos(0x8, 16000, 0, 15870, 180)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0660
    ChrTalk(
        0x8,
        (
            "むう……\x01",
            "カン違いなら仕方ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x8,
        (
            "でも、何かの縁ね。\x01",
            "これを持っていくといい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDEF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0662
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "龍老炒飯のレシピ\x07\x00",
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0663
    AnonymousTalk(
        0xFF,
        (
            "ついでに",
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0664
    ChrTalk(
        0x101,
        (
            "#12P#00005Fって、いいんですか？\x01",
            "手帳まで貰っちゃって……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE70")

    label("loc_DDEF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0665
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0666
    ChrTalk(
        0x101,
        (
            "#12P#00005Fって、いいんですか？\x01",
            "タダで貰っちゃって……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE70")

    AddItemNumber(0x2, 1)

    #C0667
    ChrTalk(
        0x8,
        (
            "店の余り物だから気にしない。\x01",
            "精進するがいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x101,
        (
            "#12P#00003Fありがとうございます。\x01",
            "そ、それじゃあ失礼します。\x02\x03",

            "#00001F──みんな、追いかけるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x102,
        "#11P#00101Fええ！\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x109,
        "#12P#10101F了解です！\x02",
    )

    CloseMessageWindow()

    def lambda_DF46():
        OP_93(0x101, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF46)

    def lambda_DF53():
        OP_93(0x102, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF53)

    def lambda_DF60():
        OP_93(0x109, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF60)

    def lambda_DF6D():
        OP_93(0x105, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DF6D)
    WaitChrThread(0x105, 1)

    def lambda_DF7E():
        OP_98(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF7E)
    Sleep(50)

    def lambda_DF9B():
        OP_98(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF9B)
    Sleep(50)

    def lambda_DFB8():
        OP_98(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DFB8)
    Sleep(50)

    def lambda_DFD5():
        OP_98(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DFD5)
    Sleep(50)
    OP_93(0x8, 0x10E, 0x1F4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0671
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※様々な場所に置かれた本など、特定の場所を調べると、\x01",
            "  料理の『レシピ』を覚えることがあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0672
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※『レシピ』は『料理手帳』に記録されていきます。\x01",
            "  『料理手帳』を使えば、いつでも\x01",
            "  様々な効力のある料理を作ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0673
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※また、『大成功』料理や、『予想外』料理など、\x01",
            "  一定の確率で完成する料理が変化します。\x01",
            "  （料理に『失敗』してしまうこともあります。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0674
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※料理に使う『食材』は\x01",
            "  雑貨屋などの商店で販売されています。\x01",
            "  また、魔獣が落とす場合もあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x22, 4)
    NewScene("c1000", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_49_D1BA end

    def Function_50_E209(): pass

    label("Function_50_E209")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(250, 1400, -660, 0)
    MoveCamera(46, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19780, 0)
    LoadChrToIndex("chr/ch00002.itc", 0x28)
    LoadChrToIndex("chr/ch00102.itc", 0x29)
    LoadChrToIndex("chr/ch00302.itc", 0x2A)
    LoadChrToIndex("chr/ch02902.itc", 0x2B)
    LoadChrToIndex("chr/ch03002.itc", 0x2C)
    LoadChrToIndex("chr/ch45002.itc", 0x2D)
    LoadChrToIndex("apl/ch50092.itc", 0x2E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E3C7")
    SetChrPos(0x1A2, -2000, 0, 500, 90)
    SetChrPos(0x102, -2000, 0, -500, 90)
    SetChrPos(0x101, -2000, 0, 600, 90)
    SetChrPos(0x104, -2000, 0, -600, 90)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_E2FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_E2FB)

    def lambda_E30C():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E30C)

    def lambda_E326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E326)

    def lambda_E337():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E337)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_E36E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E36E)

    def lambda_E37F():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E37F)
    Sleep(200)

    def lambda_E39C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E39C)

    def lambda_E3AD():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E3AD)
    Jump("loc_E676")

    label("loc_E3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E521")
    SetChrPos(0x1A2, -2000, 0, 500, 90)
    SetChrPos(0x102, -2000, 0, -500, 90)
    SetChrPos(0x101, -2000, 0, 600, 90)
    SetChrPos(0x109, -2000, 0, -600, 90)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_E455():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_E455)

    def lambda_E466():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E466)

    def lambda_E480():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E480)

    def lambda_E491():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E491)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_E4C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E4C8)

    def lambda_E4D9():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4D9)
    Sleep(200)

    def lambda_E4F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E4F6)

    def lambda_E507():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E507)
    Jump("loc_E676")

    label("loc_E521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E676")
    SetChrPos(0x1A2, -2000, 0, 500, 90)
    SetChrPos(0x102, -2000, 0, -500, 90)
    SetChrPos(0x101, -2000, 0, 600, 90)
    SetChrPos(0x105, -2000, 0, -600, 90)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_E5AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_E5AF)

    def lambda_E5C0():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E5C0)

    def lambda_E5DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E5DA)

    def lambda_E5EB():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E5EB)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_E622():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E622)

    def lambda_E633():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E633)
    Sleep(200)

    def lambda_E650():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_E650)

    def lambda_E661():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E661)

    label("loc_E676")

    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    #C0675
    ChrTalk(
        0x1A2,
        (
            "《龍老飯店》……\x01",
            "東通りで東方料理を出す店、か。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x101,
        "#00002F少し休憩でもして行くか？\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x1A2,
        (
            "フム、そうだな。\x01",
            "ちょうど小腹も空いてきたトコロだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x1A2,
        (
            "この店がいったい\x01",
            "どんなモノを出すのか試してやるぞ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(2730, 1400, 6720, 0)
    MoveCamera(41, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16270, 0)
    SetChrChipByIndex(0x29, 0x2E)
    SetChrSubChip(0x29, 0xB)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 4400, 600, 7100, 0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x2E)
    SetChrSubChip(0x2A, 0xB)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 3300, 600, 6100, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x2E)
    SetChrSubChip(0x2B, 0xB)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 2100, 600, 7100, 0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x2C, 0x2E)
    SetChrSubChip(0x2C, 0xB)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 3300, 600, 8300, 0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E8AD")
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x104, 0x2A)
    SetChrChipByIndex(0x1A2, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x1A2, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x1A2, 0x0)
    SetChrPos(0x1A2, 3250, 100, 9050, 180)
    SetChrPos(0x102, 4900, 100, 7100, 270)
    SetChrPos(0x101, 3250, 100, 5450, 0)
    SetChrPos(0x104, 1600, 100, 7150, 90)
    Jump("loc_E9B4")

    label("loc_E8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E933")
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x109, 0x2B)
    SetChrChipByIndex(0x1A2, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x1A2, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x1A2, 0x0)
    SetChrPos(0x1A2, 3250, 100, 9050, 180)
    SetChrPos(0x102, 4900, 100, 7100, 270)
    SetChrPos(0x101, 3250, 100, 5450, 0)
    SetChrPos(0x109, 1600, 100, 7150, 90)
    Jump("loc_E9B4")

    label("loc_E933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E9B4")
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x105, 0x2C)
    SetChrChipByIndex(0x1A2, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x1A2, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x1A2, 0x0)
    SetChrPos(0x1A2, 3250, 100, 9050, 180)
    SetChrPos(0x102, 4900, 100, 7100, 270)
    SetChrPos(0x101, 3250, 100, 5450, 0)
    SetChrPos(0x105, 1600, 100, 7150, 90)

    label("loc_E9B4")

    FadeToBright(1000, 0)
    OP_0D()

    #C0679
    ChrTalk(
        0x102,
        "#11P#00102Fどうだった、龍老飯店の味は？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EA3A")

    #C0680
    ChrTalk(
        0x104,
        (
            "#6P#00309Fああ、ぜひ本場を知る\x01",
            "人間の意見が聞きてえモンだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EACF")

    label("loc_EA3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EA89")

    #C0681
    ChrTalk(
        0x109,
        (
            "#6P#10109Fええ、ぜひ本場を知る\x01",
            "人間の意見が聞きたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EACF")

    label("loc_EA89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EACF")

    #C0682
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、ぜひ本場を知る\x01",
            "人間の意見が聞きたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EACF")

    BeginChrThread(0x1A2, 3, 0, 51)
    Sleep(1000)
    EndChrThread(0x1A2, 0x3)

    #C0683
    ChrTalk(
        0x1A2,
        (
            "#5Pくっ――\x01",
            "これは一体どういうことだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x1A2,
        (
            "#5Pこの店はどうして\x01",
            "こんな料理をこんな値段で出せる？\x01",
            "店主の気は確かなのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#12P#00006Fおいおい、そんな大声で\x01",
            "店のことを悪く……\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        "#11P#00100Fいえ、シン君はたぶん……\x02",
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x1A2,
        (
            "#5Pたとえばこのマーボー豆腐……\x01",
            "味は東方人街の三ツ星レストランにも\x01",
            "まったく引けを取っていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x1A2,
        (
            "#5Pこれなら３倍はミラを取れるはず――\x01",
            "なのにナゼそうしない！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EC99")

    #C0689
    ChrTalk(
        0x104,
        "#6P#00306Fそ、そういう話か……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECFE")

    label("loc_EC99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_ECCF")

    #C0690
    ChrTalk(
        0x109,
        "#6P#10106Fそういう話だったんだ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECFE")

    label("loc_ECCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ECFE")

    #C0691
    ChrTalk(
        0x105,
        "#6P#10304Fフフ、そういうことか。\x02",
    )

    CloseMessageWindow()

    label("loc_ECFE")


    #C0692
    ChrTalk(
        0x1A2,
        (
            "#5Pあ、ありえん……\x01",
            "なぜクロスベルにこんな店が……\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        (
            "#12P#00009Fはは、まあとにかく\x01",
            "満足してくれてよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 1)
    OP_29(0x73, 0x1, 0x9)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EDD4")
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x1A2, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x1A2, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x1A2, 0x4)
    Jump("loc_EE53")

    label("loc_EDD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EE16")
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x1A2, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x1A2, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x1A2, 0x4)
    Jump("loc_EE53")

    label("loc_EE16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EE53")
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x1A2, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x1A2, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x1A2, 0x4)

    label("loc_EE53")

    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_49()
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_D7(0x2B)
    OP_D7(0x2C)
    OP_D7(0x2D)
    OP_D7(0x2E)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1380, 20, -90, 270)
    EventEnd(0x5)
    Return()

    # Function_50_E209 end

    def Function_51_EE8E(): pass

    label("Function_51_EE8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEBE")

    def lambda_EE9E():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EE9E)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_51_EE8E")

    label("loc_EEBE")

    Return()

    # Function_51_EE8E end

    def Function_52_EEBF(): pass

    label("Function_52_EEBF")

    LoadChrToIndex("chr/ch00002.itc", 0x28)
    LoadChrToIndex("chr/ch00102.itc", 0x29)
    LoadChrToIndex("chr/ch00202.itc", 0x2A)
    LoadChrToIndex("chr/ch00302.itc", 0x2B)
    LoadChrToIndex("chr/ch02902.itc", 0x2C)
    LoadChrToIndex("chr/ch03002.itc", 0x2D)
    LoadChrToIndex("apl/ch50092.itc", 0x2E)
    EventBegin(0x0)
    Fade(500)
    OP_68(15350, 1400, 14950, 0)
    MoveCamera(61, 26, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 16000, -200, 14500, 0)
    SetChrPos(0x102, 14880, 0, 13460, 0)
    SetChrPos(0x103, 14200, 0, 14350, 0)
    SetChrPos(0x104, 13000, 0, 14910, 0)
    SetChrPos(0x109, 13590, 0, 13330, 0)
    SetChrPos(0x105, 12700, 0, 13930, 0)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x103, 0x8, 0)
    TurnDirection(0x104, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x105, 0x8, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EFE2")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_F025")

    label("loc_EFE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EFFA")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_F025")

    label("loc_EFFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F012")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Jump("loc_F025")

    label("loc_F012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F025")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_F025")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F15A")

    #C0694
    ChrTalk(
        0x8,
        (
            "ほらっ、何してる！\x01",
            "またコゲついちゃってるよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0xC,
        "ひ、ひいっ、すみません！\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x101,
        "#00000Fあの、ちょっといいですか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0697
    ChrTalk(
        0x8,
        "ん……ワタシに何か用ね？\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x8,
        (
            "見ての通り、今は忙しい。\x01",
            "注文ならカウンターにお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#00000Fえっと、そうではなくて。\x01",
            "実は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1DD")

    label("loc_F15A")

    TurnDirection(0x8, 0x101, 500)

    #C0700
    ChrTalk(
        0x8,
        "おや、ワタシに何か用ね？\x02",
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        "注文ならカウンターにお願いするよ。\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1DD")

    SetChrName("")

    #A0703
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一押しグルメ』の取材で\x01",
            "来たことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0704
    ChrTalk(
        0x8,
        (
            "ああ、例のグルメガイドの話ね。\x01",
            "確かに聞いてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x8,
        (
            "ふむ、忙しいが仕方ない。\x01",
            "空いてるテーブルで待ってるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "ワタシが自慢の『天下一炒飯』を\x01",
            "味あわせてあげるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x104,
        "#00309Fおおっ、そいつは楽しみだぜ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0708
    ChrTalk(
        0x101,
        "#00000Fそれじゃあ、席についているとしよう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x8, 5440, 0, 9730, 225)
    SetChrPos(0x101, 3230, 0, 8960, 180)
    SetChrPos(0x103, 1720, 0, 8710, 135)
    SetChrPos(0x102, 1600, 0, 7150, 90)
    SetChrPos(0x104, 3290, 0, 5440, 0)
    SetChrPos(0x105, 4520, 0, 5990, 315)
    SetChrPos(0x109, 4770, 0, 7180, 270)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x29, 0x2E)
    SetChrSubChip(0x29, 0x1)
    SetChrFlags(0x29, 0x8000)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x2E)
    SetChrSubChip(0x2A, 0x1)
    SetChrFlags(0x2A, 0x8000)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x2E)
    SetChrSubChip(0x2B, 0x1)
    SetChrFlags(0x2B, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x2C, 0x2E)
    SetChrSubChip(0x2C, 0x1)
    SetChrFlags(0x2C, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    SetChrChipByIndex(0x2D, 0x2E)
    SetChrSubChip(0x2D, 0x1)
    SetChrFlags(0x2D, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2E, 0x2E)
    SetChrSubChip(0x2E, 0x1)
    SetChrFlags(0x2E, 0x8000)
    ClearChrFlags(0x2E, 0x80)
    ClearChrBattleFlags(0x2E, 0x8000)
    SetChrPos(0x29, 3990, 600, 7230, 0)
    SetChrPos(0x2A, 2760, 600, 6220, 0)
    SetChrPos(0x2B, 2330, 600, 6900, 0)
    SetChrPos(0x2C, 3300, 600, 8300, 0)
    SetChrPos(0x2D, 3900, 600, 6340, 0)
    SetChrPos(0x2E, 2360, 600, 7880, 0)
    OP_68(3250, 1400, 7170, 0)
    MoveCamera(58, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0709
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは天下一炒飯を食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0710
    ChrTalk(
        0x103,
        "#00204F……美味しいです。\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x104,
        (
            "#00309Fいやー、やっぱ\x01",
            "マスターは流石だぜ。\x02\x03",

            "#00304Fここまでパラっとした\x01",
            "絶品の炒飯は、龍老飯店でしか\x01",
            "食えねえもんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x8,
        "フフン、当然ね。\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x8,
        (
            "もともと炒飯はワタシの得意料理……\x01",
            "先日、それを更に改良したんだから\x01",
            "美味くないわけがないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x109,
        (
            "#10102Fハグハグ、モグモグ……\x01",
            "ええ、本当に……！\x02\x03",

            "#10103Fシンプルな料理なのに\x01",
            "ここまで深い味が出せるなんて！\x02\x03",

            "#10109Fあたしも警備隊の寮で\x01",
            "何度か作ったことありましたけど、\x01",
            "流石プロは違いますね……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x105, 0x2)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0715
    ChrTalk(
        0x104,
        "#00306F食いながら喋るなっつーの。\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x105,
        (
            "#10302Fいやはや、すごい勢いで\x01",
            "かっ込んでるねえ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)

    #C0717
    ChrTalk(
        0x8,
        (
            "うむ、そこまで\x01",
            "気に入ってもらえると\x01",
            "作った甲斐があったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x8,
        (
            "せっかくだから、おかわりを\x01",
            "サービスしてあげようかね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(100)

    #C0719
    ChrTalk(
        0x109,
        "#10109Fはいっ、是非！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0720
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、ノエルさんったら……\x01",
            "まるで育ち盛りの男の子ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x101,
        (
            "#00000Fああ、かなり気に入ったみたいだし……\x01",
            "ここの記事はノエルに任せるか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 2300, 0, 500, 270)
    SetChrPos(0x103, 2300, 0, -500, 270)
    SetChrPos(0x104, 3400, 0, 500, 270)
    SetChrPos(0x105, 3400, 0, -500, 270)
    SetChrPos(0x109, 4500, 0, 500, 270)
    SetChrPos(0x102, 4500, 0, -500, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA6C")
    SetChrPos(0x8, 17080, 0, 15430, 0)
    BeginChrThread(0x8, 0, 0, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_FA7D")

    label("loc_FA6C")

    SetChrPos(0x8, 16000, 0, 15990, 0)

    label("loc_FA7D")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrFlags(0x2E, 0x80)
    SetChrBattleFlags(0x2E, 0x8000)
    OP_68(2880, 1400, -40, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x172, 5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_FB2A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_FB47")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_FB5A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_FB6D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_FB8A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_FB9D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_FBBA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_FBCD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_FBEA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_FBFD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_FC1A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FC1A")

    OP_29(0x80, 0x1, 0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD1D")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0722
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "飲食店６ヶ所の取材を終えた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FD14")

    #A0723
    AnonymousTalk(
        0x101,
        (
            "#00003Fすぐにでもグレイスさんに\x01",
            "報告に行く事はできそうだけど……\x02\x03",

            "#00000Fまだ６人全員のお気に入りが\x01",
            "見つかったわけじゃない。\x01",
            "もう少し頑張ってみるかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_FD14")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_FD1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDEE")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0724
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課メンバー全員の\x01",
            "お気に入りを見つけた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0725
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_FDEE")

    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FE0E")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_FE51")

    label("loc_FE0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_FE26")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_FE51")

    label("loc_FE26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FE3E")
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Jump("loc_FE51")

    label("loc_FE3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FE51")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_FE51")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2880, 0, -40, 278)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_EEBF end

    def Function_53_FE7D(): pass

    label("Function_53_FE7D")

    EventBegin(0x0)
    Fade(500)
    OP_68(11630, 1400, -4690, 0)
    MoveCamera(53, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 11200, 0, -5110, 90)
    SetChrPos(0x102, 10260, 0, -5180, 90)
    SetChrPos(0x104, 10900, 0, -4210, 90)
    SetChrPos(0x103, 9410, 30, -4580, 90)
    SetChrPos(0x105, 11260, 0, -3140, 135)
    SetChrPos(0x109, 10050, 0, -3500, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0726
    ChrTalk(
        0xA,
        "はあ……\x02",
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x105,
        (
            "#10300F（彼女なら、ミスコンの\x01",
            "  『ウェイトレス』枠には\x01",
            "  相応しいんじゃないかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x101,
        (
            "#00003F（なんだか元気がない\x01",
            "  みたいだけど……\x01",
            "  一応お願いしてみるか。）\x02\x03",

            "#00000Fあの、ちょっと相談が\x01",
            "あるんだけど……いいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0xA,
        "……はいな？\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0730
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0731
    ChrTalk(
        0xA,
        "ああ、あの話……\x02",
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xA,
        (
            "この前、ロイに誘われたときに\x01",
            "一度断ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xA,
        (
            "リーシャがいなくなったのに\x01",
            "中々そんな気になれなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x103,
        "#00203Fそうだったのですか……\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x102,
        (
            "#00108Fだったら、ムリに誘うのは\x01",
            "良くないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xA,
        "……………………………\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x104,
        (
            "#00300Fふむ……\x01",
            "どうやら、まだ迷ってる\x01",
            "んじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xA,
        "うん……\x02",
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xA,
        (
            "私が元気ないの、\x01",
            "お店のお客さんにも\x01",
            "伝わってるみたいだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xA,
        (
            "たしかに私がこんな状態じゃ、\x01",
            "お客さんも楽しくないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x105,
        (
            "#10304Fまあ、迷いがあるなら\x01",
            "やってみたらいいんじゃない？\x02\x03",

            "#10300Fやらないで後悔する\x01",
            "可能性があるなら、\x01",
            "やった方がいいと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)
    Sound(809, 0, 40, 0)
    SetChrChipByIndex(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xA, 0x3070, 0x0, 0xFFFFEBB0, 0x2BC, 0x7D0)
    Sound(30, 0, 100, 0)
    Sleep(500)

    #C0742
    ChrTalk(
        0xA,
        "……うん、決めた。\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xA,
        (
            "やっぱり、がんばってイベントを\x01",
            "盛り上げさせてもらうよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "ミスコンだろうが熱湯風呂だろうが、\x01",
            "どんと来いね！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0745
    ChrTalk(
        0x109,
        "#10106F熱湯風呂って……\x02",
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x101,
        (
            "#00012Fえっと、それじゃあ\x01",
            "参加ということでいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0xA,
        "うん、オッケー！\x02",
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xA,
        (
            "プログラムの開始に\x01",
            "間に合うように行くから、\x01",
            "あとで連絡ちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        "#00000Fああ、よろしくお願いするよ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10592")

    #C0750
    ChrTalk(
        0x101,
        (
            "#00003F──さて、これでようやく\x01",
            "参加者枠が埋まったな。\x02\x03",

            "#00000F市民会館に行って\x01",
            "ロイさんたちに報告しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_10592")

    SetScenarioFlags(0x199, 4)
    OP_4C(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)
    ClearChrBattleFlags(0xA, 0x4)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 10980, 0, -4730, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_53_FE7D end

    def Function_54_105E0(): pass

    label("Function_54_105E0")

    EventBegin(0x0)
    OP_4B(0x1E, 0xFF)
    OP_4B(0x1F, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-100570, 1430, -55230, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -100480, 30, -54280, 180)
    SetChrPos(0x102, -99460, 30, -53780, 180)
    SetChrPos(0x103, -101150, 30, -53570, 180)
    SetChrPos(0x104, -100010, 30, -52930, 180)
    SetChrPos(0x109, -101120, 30, -52250, 180)
    SetChrPos(0x105, -100010, 30, -51900, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D81")
    OP_93(0x1E, 0x5A, 0x0)
    OP_93(0x1F, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0751
    NpcTalk(
        0x1F,
        "赤ん坊",
        "すう、すう……\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x1F,
        "よちよち……\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x1F,
        (
            "うふふ、見てアルム。\x01",
            "この子ったらぐっすりと\x01",
            "眠りについているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x1E,
        "ああ、そうだねエアリー。\x02",
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x1E,
        (
            "この寝顔ときたら\x01",
            "まるで天使のようだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x1E,
        (
            "ふふ、女神のような君から\x01",
            "生まれてきたんだから、\x01",
            "当然といえば当然かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x1F,
        "まあ、アルムったら……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x1F, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0758
    ChrTalk(
        0x101,
        (
            "#00003F……え、えっと。\x01",
            "お取り込み中のところ\x01",
            "申し訳ないんですが……\x02\x03",

            "#00000Fあなたがアルムさんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_108B3():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_108B3)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    #C0759
    ChrTalk(
        0x1E,
        "ん……？\x02",
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x1F,
        "ええと、どちら様？\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        (
            "#00000Fクロスベル警察、\x01",
            "特務支援課の者です。\x02\x03",

            "依頼を見て\x01",
            "こちらに伺ったんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x1E,
        "おお、君たちが！\x02",
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x1E,
        (
            "来てくれてよかった、\x01",
            "本当にうれしいよ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    #C0764
    ChrTalk(
        0x1F,
        (
            "よかったわね、アルム！\x01",
            "これでようやく……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    #C0765
    ChrTalk(
        0x1E,
        "ああ、エアリー……\x02",
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x1E,
        (
            "赤ん坊が生まれたばかり\x01",
            "だというのに、本当に\x01",
            "苦労をかけてしまったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x1E,
        (
            "この僕が不甲斐ない\x01",
            "ばっかりに……\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x1F,
        (
            "アルムったら……\x01",
            "それは言わない約束よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x1F,
        (
            "この子を初めて抱いた時、\x01",
            "２人で誓ったじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x1F,
        "どんなに大変な事でも……\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x1E,
        (
            "……僕と君、そして\x01",
            "愛すべきこの子……\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x1E,
        (
            "家族みんなで乗り越えていく。\x01",
            "……そうだったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x1E,
        "ああ、愛しているよエアリー！\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x1F,
        "私もよ、アルム！！\x02",
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

    #C0775
    ChrTalk(
        0x109,
        (
            "#10106Fうはあ……\x01",
            "ラブラブですねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x102,
        (
            "#00102Fすっかり２人の世界に\x01",
            "入り込んじゃったみたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x101,
        (
            "#00006Fそ、そうみたいだな……\x02\x03",

            "#00000F……コホン。\x01",
            "すみませんが、依頼について\x01",
            "お聞かせ願えませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x1E,
        "ハッ……！\x02",
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x1F,
        "そうよ、そうだったわ！\x02",
    )

    CloseMessageWindow()

    def lambda_10CFB():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_10CFB)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    #C0780
    ChrTalk(
        0x1E,
        (
            "えっと……\x01",
            "君たちには、ある人の捜索を\x01",
            "お願いしたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x1E,
        (
            "すまないけど\x01",
            "すぐに引き受けてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E1B")

    label("loc_10D81")

    OP_93(0x1E, 0x0, 0x0)
    OP_93(0x1F, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0782
    ChrTalk(
        0x1E,
        "おお、手が空いたのかな？\x02",
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x1E,
        (
            "君たちには、ある人の捜索を\x01",
            "お願いしたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x1E,
        (
            "すまないけど\x01",
            "すぐに引き受けてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E1B")

    Call(0, 55)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1F, 0xFF)
    OP_93(0x1E, 0x5A, 0x0)
    OP_93(0x1F, 0x10E, 0x0)
    SetChrPos(0x0, -100140, 30, -52870, 180)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_54_105E0 end

    def Function_55_10E6B(): pass

    label("Function_55_10E6B")

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
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
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
        (0, "loc_10ED5"),
        (1, "loc_10EDD"),
        (SWITCH_DEFAULT, "loc_110A8"),
    )


    label("loc_10ED5")

    Call(0, 56)
    Jump("loc_110A8")

    label("loc_10EDD")


    #C0785
    ChrTalk(
        0x101,
        (
            "#00006Fええっと……すいません。\x01",
            "すぐにというわけには……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11043")

    #C0786
    ChrTalk(
        0x1E,
        (
            "そ、そんなぁ……\x01",
            "君たちだけが頼みなんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x1F,
        (
            "お願いよ……\x01",
            "愛するこの子のためでもあるの。\x02",
        )
    )

    CloseMessageWindow()

    #N0788
    NpcTalk(
        0x1F,
        "赤ん坊",
        "……えっく、えっく……\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x1F,
        (
            "おおよしよしアルミン、\x01",
            "大丈夫だからね……\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x102,
        (
            "#00106Fな、なんとか手を空けて\x01",
            "戻りますから……\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x1E,
        (
            "ああ、頼むよ。\x01",
            "ずっとここで待ってるからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110A0")

    label("loc_11043")


    #C0792
    ChrTalk(
        0x1E,
        "そ、そんなぁ……\x02",
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x1E,
        (
            "それじゃあ、早く手を空けて\x01",
            "こっちに来てくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x1F,
        "お願いね……\x02",
    )

    CloseMessageWindow()

    label("loc_110A0")

    SetScenarioFlags(0x19A, 5)
    Jump("loc_110A8")

    label("loc_110A8")

    Return()

    # Function_55_10E6B end

    def Function_56_110A9(): pass

    label("Function_56_110A9")


    #C0795
    ChrTalk(
        0x101,
        (
            "#00000Fええ、分かりました。\x01",
            "お任せください。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x1E,
        "おお……本当かい！？\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x1E,
        (
            "いや～、助かるよ！\x01",
            "本当に困っていたところ\x01",
            "だったんだ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    #C0798
    ChrTalk(
        0x1F,
        (
            "よかったわね、アルム！\x01",
            "私、とっても嬉しい！\x02",
        )
    )

    CloseMessageWindow()

    #N0799
    NpcTalk(
        0x1F,
        "赤ん坊",
        "きゃっきゃっ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    #C0800
    ChrTalk(
        0x1E,
        (
            "ああ、エアリー……\x01",
            "アルミンも喜んで\x01",
            "くれているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x1F,
        "ええ、アルム……\x02",
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x103,
        "#00211F……依頼の詳細をお願いします。\x02",
    )

    CloseMessageWindow()

    def lambda_11211():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_11211)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    #C0803
    ChrTalk(
        0x1E,
        "あ、ああ、そうだったね。\x02",
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x1E,
        (
            "こほん、失敬……\x01",
            "早速話させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x101,
        "#00006F（た、助かったよティオ……）\x02",
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x103,
        (
            "#00206F（このままでは\x01",
            "  いつまでたっても\x01",
            "  本題に入れなさそうなので。）\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x105,
        (
            "#10309F（フフ……\x01",
            "  しばらく見ていたい気も\x01",
            "  するけどね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x1E,
        (
            "こほん、君たちに\x01",
            "捜索して欲しいのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x1E,
        (
            "幼い頃に生き別れた\x01",
            "僕の父さんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x101,
        "#00005F生き別れ……ですか？\x02",
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x1E,
        (
            "ああ、僕たちはリベール王国で\x01",
            "暮らしているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x1E,
        (
            "実は僕の方は、小さい頃は\x01",
            "クロスベルに住んでいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x1E,
        (
            "事情があって両親が離婚して、\x01",
            "母方の実家がある\x01",
            "リベールの方に引き取られたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x1E,
        (
            "もう会うこともないかと\x01",
            "思っていたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x1F,
        (
            "先日、あたしたちの間に\x01",
            "愛するこの子が生まれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x1F,
        (
            "そしたらアルム、\x01",
            "どうしてもお義父さんに\x01",
            "この子を見せたいって言って。\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x105,
        "#10305Fへえ……\x02",
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x1E,
        (
            "母さんとは色々あった\x01",
            "かもしれないけど、\x01",
            "僕にとっては実の父だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x1E,
        (
            "幸せな家庭を築けたことを\x01",
            "どうしても報告したかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x1E,
        (
            "それで、母さんを説得して\x01",
            "クロスベルに来ることにしたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x1E,
        "だけど……\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x104,
        (
            "#00303F久しぶりすぎて、\x01",
            "親父さんの居場所が\x01",
            "分からなくなったってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x1E,
        "ああ、そうなんだ……\x02",
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x1E,
        (
            "住宅街に屋敷があった\x01",
            "はずなんだけど、\x01",
            "綺麗さっぱり無くなっててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x1E,
        (
            "母さんにも通信で聞いたけど、\x01",
            "離婚してからほとんど\x01",
            "連絡はとってなかったらしくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x1E,
        (
            "だから、僕たちは\x01",
            "父さんを探すことにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x1F,
        (
            "アルムと一緒に\x01",
            "色んな場所で話を聞いて回ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x1F,
        (
            "そしたら、急病で入院した後\x01",
            "旧市街に引っ越されたことは\x01",
            "分かったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x1F,
        (
            "私たちが会いに行くときは、\x01",
            "いつもいらっしゃらなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x109,
        (
            "#10105Fもしかして、\x01",
            "入れ違いに旅行にでも\x01",
            "行ってしまったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x101,
        (
            "#00003Fうーん、分からないけど……\x02\x03",

            "#00000F住宅街から旧市街にっていうのは\x01",
            "結構特殊な経歴だな。\x02\x03",

            "エリィ、住宅街に住んでいた人で\x01",
            "心当たりはないか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1E, 500)
    Sleep(300)

    #C0832
    ChrTalk(
        0x102,
        (
            "#00103Fううん、ないこともないけど……\x02\x03",

            "#00100Fあの、アルムさん。\x01",
            "お父様のお名前やご職業は\x01",
            "覚えてらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)
    Sleep(300)

    #C0833
    ChrTalk(
        0x1E,
        (
            "うーん、そうだなあ。\x01",
            "母さんに聞いてた話だけだから\x01",
            "今もその仕事かは知らないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x1E,
        (
            "名前は分かるよ。\x01",
            "クロスベル市議会の議員の１人で、\x01",
            "『ゲバル』という名前の人さ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0835
    ChrTalk(
        0x101,
        "#00005Fゲバル議員って……！\x02",
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x105,
        "#10305Fああ、あの御仁か。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    #C0837
    ChrTalk(
        0x1E,
        "おお……知っているのかい！？\x02",
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x102,
        (
            "#00103Fええ、ちょっと前に\x01",
            "依頼で会ったことがありまして。\x02\x03",

            "#00100Fとにかく、まずは旧市街の\x01",
            "アパートを訪ねてみたほうがよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x101,
        (
            "#00003Fああ、そうだな。\x02\x03",

            "#00000F今、彼がいない事情も\x01",
            "なにか分かるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x1E,
        (
            "ああ、君たちに依頼を出したのも、\x01",
            "きっと運命だね！\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x1E,
        (
            "全部君たちにお任せするから、\x01",
            "どうか父さんを探し出してくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x1F,
        "よろしくお願いするわね！\x02",
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x101,
        "#00000Fええ、お任せください。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0844
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【生き別れの父の捜索】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x90, 0x1, 0x0)
    SetScenarioFlags(0x19A, 6)
    Return()

    # Function_56_110A9 end

    SaveToFile()

Try(main)
