from ScenarioHelper import *

def main():
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
        "强霍",                   # 1
        "芬",                     # 2
        "桑桑",                   # 3
        "帕库",                   # 4
        "鲁斯",                   # 5
        "古利德",                 # 6
        "本德",                   # 7
        "库雷优",                 # 8
        "萨妮塔",                 # 9
        "玛丽",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "记者诺蒂亚",             # 15
        "格蕾丝",                 # 16
        "雷因兹",                 # 17
        "夫人",                   # 18
        "男孩",                   # 19
        "市民",                   # 20
        "莉夏",                   # 21
        "莉丝修女",               # 22
        "阿鲁姆",                 # 23
        "艾娅莉",                 # 24
        "阿雷库瑟队员",           # 25
        "库隆克",                 # 26
        "迪因兹",                 # 27
        "莉莉",                   # 28
        "玛尔缇",                 # 29
        "曹",                     # 30
        "刘",                     # 31
        "尼尔森",                 # 32
        "雷克特",                 # 33
        "餐具",                   # 34
        "餐具",                   # 35
        "餐具",                   # 36
        "餐具",                   # 37
        "餐具",                   # 38
        "餐具",                   # 39
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
    DeclNpc(13989,   -29,     -19,     90,   453,  0x0, 0,   19,  0,   0,   0,   0,   40,  255,  0)
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
        "Function_7_31FF",         # 07, 7
        "Function_8_3E36",         # 08, 8
        "Function_9_3F3C",         # 09, 9
        "Function_10_5038",        # 0A, 10
        "Function_11_50BB",        # 0B, 11
        "Function_12_52AC",        # 0C, 12
        "Function_13_53B2",        # 0D, 13
        "Function_14_5DE8",        # 0E, 14
        "Function_15_5EEE",        # 0F, 15
        "Function_16_6BDA",        # 10, 16
        "Function_17_76CD",        # 11, 17
        "Function_18_7727",        # 12, 18
        "Function_19_7755",        # 13, 19
        "Function_20_7776",        # 14, 20
        "Function_21_77CD",        # 15, 21
        "Function_22_794A",        # 16, 22
        "Function_23_80CE",        # 17, 23
        "Function_24_839A",        # 18, 24
        "Function_25_84B0",        # 19, 25
        "Function_26_8508",        # 1A, 26
        "Function_27_85E2",        # 1B, 27
        "Function_28_8646",        # 1C, 28
        "Function_29_8659",        # 1D, 29
        "Function_30_8B5C",        # 1E, 30
        "Function_31_8BF2",        # 1F, 31
        "Function_32_8C64",        # 20, 32
        "Function_33_8DCD",        # 21, 33
        "Function_34_8EB9",        # 22, 34
        "Function_35_93A7",        # 23, 35
        "Function_36_9439",        # 24, 36
        "Function_37_94BF",        # 25, 37
        "Function_38_9F0F",        # 26, 38
        "Function_39_A1A1",        # 27, 39
        "Function_40_A2E2",        # 28, 40
        "Function_41_A513",        # 29, 41
        "Function_42_A5C9",        # 2A, 42
        "Function_43_A6A8",        # 2B, 43
        "Function_44_A795",        # 2C, 44
        "Function_45_A7B1",        # 2D, 45
        "Function_46_A907",        # 2E, 46
        "Function_47_A9D0",        # 2F, 47
        "Function_48_AA85",        # 30, 48
        "Function_49_B226",        # 31, 49
        "Function_50_C191",        # 32, 50
        "Function_51_CD9E",        # 33, 51
        "Function_52_CDCF",        # 34, 52
        "Function_53_DC67",        # 35, 53
        "Function_54_E2FA",        # 36, 54
        "Function_55_EA91",        # 37, 55
        "Function_56_EC89",        # 38, 56
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_15FD")
    TurnDirection(0xFE, 0x0, 0)

    #C0001
    ChrTalk(
        0xFE,
        (
            "能让你那么满意，\x01",
            "我也算没有白做啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "如果以后还想吃我做的料理，\x01",
            "欢迎随时过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_15FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2023")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EE4")

    #C0003
    ChrTalk(
        0xFE,
        (
            "……哎呀呀，外面的骚乱\x01",
            "好不容易结束了，本以为能松一口气，\x01",
            "结果奇怪的事情却一件接一件……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "……哦，你们聚在一起，\x01",
            "是要去什么地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "在这种状况下，\x01",
            "希望警察多加努力啊。\x02",
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
        "#00005F那个……怎么了……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1956")

    #C0008
    ChrTalk(
        0xFE,
        (
            "嗯……看来你们一直都在\x01",
            "努力磨练料理技术啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "没办法了，今天就把我\x01",
            "赖以为生的祖传食谱\x01",
            "教给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "强霍一把将料理手册抢了过去，\x01",
            "在上面写了些什么。\x07\x00\x02",
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
            "『药膳麻婆豆腐』\x07\x00",
            "的食谱获得了。\x02",
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
        "……好，拿去吧！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00003F（这……把手册的最后一页\x01",
            "  填上了呢。）\x02\x03",

            "#00000F那个……这样好吗？\x01",
            "竟把如此重要的\x01",
            "食谱教给我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "哼，用不着客气。\x01",
            "我想教就教，\x01",
            "仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "厨师之道可是很险峻的。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "你们今后还要继续\x01",
            "努力修行哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A78")

    label("loc_1956")


    #C0017
    ChrTalk(
        0xFE,
        (
            "嗯……看来你们一直都在\x01",
            "努力磨练料理技术啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "那就把我精心烹制的\x01",
            "这道究极料理拿去吧。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '神仙麻婆『麒麟』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('神仙麻婆『麒麟』', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0020
    ChrTalk(
        0x101,
        "#00000F非、非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "哼，用不着客气。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "厨师的道路可是很险峻的。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "你们今后还要继续\x01",
            "努力修行哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A78")


    #C0024
    ChrTalk(
        0x101,
        "#00011F……哎？啊……嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "以后如果有机会，就再过来吧。\x01",
            "到时我会指导你们真正的东方料理技术。\x02",
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
            "#00012F那、那个……\x01",
            "其实我早就想问了。\x02\x03",

            "莫非您直到现在\x01",
            "都还误以为我们是来\x01",
            "学习料理技术的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "嗯？你是指我几个月之前\x01",
            "搞错的那次吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "不不不，这完全是两回事。\x01",
            "看看你们的料理手册吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔料理师联盟，\x01",
            "罗伊德·班宁斯。\x01",
            "手册上不是写得很清楚吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "拥有这本手册的人就等同于加盟者，\x01",
            "我有责任指导其修行，\x01",
            "就是这样！\x02",
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
            "#00200F那本料理手册……\x01",
            "竟是如此正式的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00106F嗯～完全都没\x01",
            "注意到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，也就是说，\x01",
            "我们已经是\x01",
            "修行中的厨师了啊。\x02\x03",

            "不然索性就以\x01",
            "专业厨师为目标吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F那、那终究还是\x01",
            "有点乱来了吧……\x02\x03",

            "#00000F……那个，\x01",
            "总之谢谢了。\x02\x03",

            "您一直都对我们\x01",
            "如此关照……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "哼，用不着客气。\x01",
            "面对你们这种有潜力的年轻人，\x01",
            "这只是我应尽的责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "总之，吃了我的料理，保证体力十足。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "你们多吃些，然后赶快\x01",
            "平息这场事件吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……我把你们当自己人，\x01",
            "所以相信你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DE, 4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDF")

    label("loc_1EDF")

    Jump("loc_201E")

    label("loc_1EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")

    #C0039
    ChrTalk(
        0xFE,
        (
            "怎么尽是一些莫名其妙的怪事啊。\x01",
            "哼，但惊慌失措也解决不了任何问题，\x01",
            "还是继续开店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "话虽如此，那棵散发着蓝白色光芒的树实在是让人\x01",
            "心情不快，真希望能尽快恢复平稳的生活啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_201E")

    label("loc_1FA9")


    #C0041
    ChrTalk(
        0xFE,
        (
            "龙老饭店仍在正常营业，\x01",
            "想吃什么的话，随便坐吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "……你们聚在一起，\x01",
            "是要去什么地方吧？\x01",
            "先填饱肚子再出发吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201E")

    Jump("loc_31FB")

    label("loc_2023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20C9")

    #C0043
    ChrTalk(
        0xFE,
        (
            "不知会持续到何时的戒严令\x01",
            "已经让人很郁闷了……\x01",
            "这骚乱又是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "要是那些徘徊在街上的怪物\x01",
            "敢把我的店损坏哪怕一丝一毫，\x01",
            "我也不会轻易罢休！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_20C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2130")

    #C0045
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的独立\x01",
            "似乎让市民们很兴奋。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "怎样都好，\x01",
            "只要他们别在店里\x01",
            "胡闹就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_2130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_244C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C8")

    #C0047
    ChrTalk(
        0xFE,
        (
            "莉夏消失踪迹之后，\x01",
            "桑桑显得非常消沉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "难得交到了一个好友，\x01",
            "结果却变成这样……\x01",
            "这也难怪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "但愿她能\x01",
            "振作精神。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2447")

    label("loc_21C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2223")

    #C0050
    ChrTalk(
        0xFE,
        (
            "是我的心理作用吗？\x01",
            "桑桑好像很开心的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "已经恢复精神了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2447")

    label("loc_2223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C4")

    #C0052
    ChrTalk(
        0xFE,
        (
            "桑桑她……\x01",
            "竟然瞒着我，去参加\x01",
            "什么职业女性选秀……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "我明明和她说过，一定要拒绝\x01",
            "工商协会会长的孙子的邀请……！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "……究竟是谁怂恿她的！？\x01",
            "要是让我知道了，\x01",
            "非用这把菜刀把他大卸八块不可！！\x02",
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
        "#00306F（绝、绝对不能说漏嘴啊……）\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10309F（呵呵，但暴露之后的反应\x01",
            "  似乎也会很有趣呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2447")

    label("loc_23C4")


    #C0057
    ChrTalk(
        0xFE,
        (
            "当然了，桑桑能恢复笑容，\x01",
            "实在是件好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "……但两件事可不能混为一谈，\x01",
            "要是让我找到了怂恿桑桑的家伙，\x01",
            "还是要把他大卸八块。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2447")

    Jump("loc_31FB")

    label("loc_244C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_24CD")

    #C0059
    ChrTalk(
        0xFE,
        (
            "嗯……怎么了？\x01",
            "为何一副胆战心惊的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "饿着肚子是没法战斗的，\x01",
            "这是永远不变的真理。\x01",
            "你们尽量多吃点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_24CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2535")

    #C0061
    ChrTalk(
        0xFE,
        (
            "一到下雨天，客人就少了，\x01",
            "感觉真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "一鼓作气，把明天要用\x01",
            "的食材也准备好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_2535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2657")

    #C0063
    ChrTalk(
        0xFE,
        (
            "唉，我让那个来打工的小子\x01",
            "试着做了简单的料理……\x01",
            "但他完全派不上用场啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "短时间内，还是只能让他\x01",
            "干些杂活了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2652")

    #C0065
    ChrTalk(
        0x101,
        (
            "#00008F（在这里似乎可以进行\x01",
            "  美食向导的取材……）\x02\x03",

            "#00003F（但现在并不是做这种事的时候，\x01",
            "  以后别忘了再过来一趟。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2652")

    Jump("loc_31FB")

    label("loc_2657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27AC")
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2749")

    #C0066
    ChrTalk(
        0xFE,
        (
            "要想把饭给炒好，\x01",
            "关键就是要用大火来炒。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "那样的话，饭就不会粘在锅上，\x01",
            "吃起来一粒是一粒。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    OP_4B(0xC, 0xFF)

    #C0068
    ChrTalk(
        0xC,
        "嘿，原来如此……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "喂！\x01",
            "不要东张西望的！\x02",
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
        "对、对不起！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    Jump("loc_27A3")

    label("loc_2749")


    #C0071
    ChrTalk(
        0xFE,
        (
            "唉，真是的……\x01",
            "正说着就炒糊了！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "炒坏的饭必须要\x01",
            "自己全部吃光！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        "呜哇哇……！\x02",
    )

    CloseMessageWindow()

    label("loc_27A3")

    OP_4C(0xC, 0xFF)
    Jump("loc_31FB")

    label("loc_27AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288A")

    #C0074
    ChrTalk(
        0xFE,
        (
            "我原本并不关心克洛斯贝尔是否独立，\x01",
            "他们要是想独立，就随他们去好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "但是否能在帝国和共和国的威胁下\x01",
            "保证自身的安全，\x01",
            "实在是个问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "我不希望桑桑\x01",
            "面对丝毫危险，\x01",
            "所以我反对独立。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28E7")

    label("loc_288A")


    #C0077
    ChrTalk(
        0xFE,
        (
            "如果克洛斯贝尔没能力保障自身安全，\x01",
            "我便反对独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "因为我不希望\x01",
            "桑桑面对\x01",
            "丝毫危险。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E7")

    Jump("loc_31FB")

    label("loc_28EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2990")

    #C0079
    ChrTalk(
        0xFE,
        (
            "那两个新来的打工小子，\x01",
            "干什么都干不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "而且总是用色咪咪的眼神\x01",
            "盯着桑桑……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "哼，下次再让我看到，\x01",
            "一定要好好教训他们一顿。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29FE")

    label("loc_2990")


    #C0082
    ChrTalk(
        0xFE,
        (
            "话说回来，盯着桑桑看\x01",
            "的好色之徒实在是太多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "要是有人敢对桑桑出手……\x01",
            "……哼，后果就不用多说了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FE")

    Jump("loc_31FB")

    label("loc_2A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A96")

    #C0084
    ChrTalk(
        0xFE,
        (
            "今天早上，外面真是\x01",
            "太吵闹了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "据说是共和国\x01",
            "的总统来到\x01",
            "克洛斯贝尔了……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "扰我清静者，无论是谁\x01",
            "也不能原谅。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2AD3")

    label("loc_2A96")


    #C0087
    ChrTalk(
        0xFE,
        "我喜欢安静的店。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "扰我清静者，无论是谁\x01",
            "也不能原谅。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD3")

    Jump("loc_31FB")

    label("loc_2AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFC")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)
    Sleep(300)

    #C0089
    ChrTalk(
        0x8,
        (
            "哎呀，这不是刚才在那桌\x01",
            "用餐的小客人吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "我做的料理如何？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    #C0091
    ChrTalk(
        0x1A2,
        "小、小字是多余的！\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x1A2,
        "不过……嗯，料理倒是让我很满意。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x1A2,
        (
            "只是味道如此出众，价格定得未免也太低了。\x01",
            "老板，你应该把价格抬高一些才是。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "唔，客人，\x01",
            "你年纪小小，却很精明啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "不过请你记住，\x01",
            "这里只是面向平民的龙老饭店，\x01",
            "我并不想经营那种高档次的店。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "所以我不打算\x01",
            "调整现在的价格。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1A2,
        (
            "原、原来如此……\x01",
            "是我考虑不周。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00009F（哈哈，真是很坦诚呢。）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1DC, 5)
    Jump("loc_2D6B")

    label("loc_2CFC")


    #C0099
    ChrTalk(
        0x8,
        (
            "话说回来，这位小客人……\x01",
            "虽然年纪幼小，\x01",
            "但却是个精干的男人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "真希望鲁斯和帕库\x01",
            "也能向你学习学习啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D6B")

    Jump("loc_2EA0")

    label("loc_2D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E23")

    #C0101
    ChrTalk(
        0xFE,
        (
            "大概是为了明天的通商会议吧，\x01",
            "听说有很多记者涌进了\x01",
            "克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "哼，有些记者\x01",
            "说不定会擅自\x01",
            "给桑桑拍照呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "要是真有人敢这么做，\x01",
            "我绝不会轻饶他们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2EA0")

    label("loc_2E23")


    #C0104
    ChrTalk(
        0xFE,
        (
            "在记者之中，大概也会有\x01",
            "擅自偷拍桑桑的无耻之辈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "如果是女记者也就罢了，\x01",
            "但男记者要是敢那么干，\x01",
            "我绝不会轻饶他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA0")

    Jump("loc_31FB")

    label("loc_2EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2C")

    #C0106
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "最近好像很少看到旧城区\x01",
            "的那些红衣服小混混了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "那些臭小子\x01",
            "该不会是想把\x01",
            "以前赊的帐赖掉吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F8A")

    label("loc_2F2C")


    #C0108
    ChrTalk(
        0xFE,
        (
            "对桑桑图谋不轨的家伙变少了，\x01",
            "自然是件好事……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "但最好是先把帐\x01",
            "还清再消失啊，真是的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8A")

    Jump("loc_31FB")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_END)), "loc_30E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3057")

    #C0110
    ChrTalk(
        0xFE,
        (
            "我本以为终于\x01",
            "可以收到新弟子了，\x01",
            "结果却……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "算了，既然搞错了，那也没办法啊。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "我交给你们的那本料理手册，\x01",
            "你们可以随意使用，\x01",
            "努力提高自己的烹饪技术吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_30E3")

    label("loc_3057")


    #C0113
    ChrTalk(
        0xFE,
        (
            "我交给你们的那本料理手册，\x01",
            "你们可以随意使用，\x01",
            "努力提高自己的烹饪技术吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "要想获得成长，\x01",
            "最基本的诀窍就是多做料理。\x01",
            "……明白了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E3")

    Jump("loc_31FB")

    label("loc_30E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3186")

    #C0115
    ChrTalk(
        0xFE,
        (
            "客人是不能随便\x01",
            "进入厨房的。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "理由很简单，\x01",
            "对厨师而言，这里相当于\x01",
            "不容侵犯的圣域。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "不过，如果你们想拜我为师，\x01",
            "那就另当别论了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_31FB")

    label("loc_3186")


    #C0118
    ChrTalk(
        0xFE,
        (
            "如果你们想学习东方料理，\x01",
            "我一定毫不藏私，倾囊相授。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "如果不是想拜师的话，\x01",
            "就不要随意踏入\x01",
            "这名为厨房的圣域。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FB")

    TalkEnd(0xFE)
    Return()

    # Function_6_1556 end

    def Function_7_31FF(): pass

    label("Function_7_31FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EA")

    #C0120
    ChrTalk(
        0xFE,
        (
            "嘿嘿，面对那么惊人的巨树，\x01",
            "却还能若无其事地烹饪料理，\x01",
            "真不愧是老板啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "虽然挺担心居住在共和国的妈妈，\x01",
            "但那里的情况应该没有\x01",
            "发生了内战的帝国那么危险吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "我没时间分心了，\x01",
            "必须要努力帮助老板。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_336B")

    label("loc_32EA")


    #C0123
    ChrTalk(
        0xFE,
        (
            "虽然挺担心居住在共和国的妈妈，\x01",
            "但那里的情况应该没有\x01",
            "发生了内战的帝国那么危险吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "我没时间分心了，\x01",
            "必须要努力帮助老板。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_336B")

    Jump("loc_3E32")

    label("loc_3370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33C9")

    #C0125
    ChrTalk(
        0xFE,
        (
            "似乎发生了非同寻常\x01",
            "的情况啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "现在可不是\x01",
            "在店里干活\x01",
            "的时候吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E32")

    label("loc_33C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_34B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345B")

    #C0127
    ChrTalk(
        0xFE,
        (
            "是不是应该今天就赶快离开，\x01",
            "暂时回共和国\x01",
            "避上一阵子呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……真担心住在共和国的妈妈啊。\x01",
            "我是不是应该回去呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34B3")

    label("loc_345B")


    #C0129
    ChrTalk(
        0xFE,
        (
            "话说回来，莉夏\x01",
            "到底去哪里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "桑桑也很担心她，\x01",
            "要是能打探到她的下落就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B3")

    Jump("loc_3E32")

    label("loc_34B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34C6")
    Jump("loc_3E32")

    label("loc_34C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3515")

    #C0131
    ChrTalk(
        0xFE,
        "总觉得最近一直不太平呢。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "算了，反正我\x01",
            "什么都改变不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E32")

    label("loc_3515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E4")

    #C0133
    ChrTalk(
        0xFE,
        (
            "那两个打工的家伙\x01",
            "干杂活好像比以前\x01",
            "努力了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "嘿嘿，我以前\x01",
            "一直都叫他们\x01",
            "『永远翻不了身的帕库和鲁斯』……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "现在总算可以\x01",
            "改口叫他们\x01",
            "『稍微有点可取之处的帕库和鲁斯』了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_363F")

    label("loc_35E4")


    #C0136
    ChrTalk(
        0xFE,
        (
            "帕库和鲁斯总算\x01",
            "改变了原来那种\x01",
            "幼稚的思维方式。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "呵呵，他们也稍微\x01",
            "有些可取之处了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363F")

    Jump("loc_3E32")

    label("loc_3644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_36DA")

    #C0138
    ChrTalk(
        0xFE,
        (
            "帕库和鲁斯认识到\x01",
            "自己的不足之处后，\x01",
            "正在消沉之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "如果这样就无法再振作起来，\x01",
            "以后就算真的从事商业工作，\x01",
            "也不可能坚持下去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E32")

    label("loc_36DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37AD")

    #C0140
    ChrTalk(
        0xFE,
        (
            "帕库和鲁斯那两个家伙，\x01",
            "竟然用狂妄的口气要求老板\x01",
            "给他们安排些更好的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "我以前也曾说过同样的话，\x01",
            "惹得老板大发雷霆。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "杂活也是非常重要的工作，\x01",
            "他们必须要理解这一点才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3822")

    label("loc_37AD")


    #C0143
    ChrTalk(
        0xFE,
        (
            "无论是什么工作，\x01",
            "一旦接受了，\x01",
            "就应该心怀荣耀，认真完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "呵呵，这些都是老板说过的话，\x01",
            "我只是转述一下而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3822")

    Jump("loc_3E32")

    label("loc_3827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38BF")

    #C0145
    ChrTalk(
        0xFE,
        (
            "说起来，我已经很久\x01",
            "没有回过共和国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "算了，在这里工作也很愉快，\x01",
            "倒也无所谓。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "不过，偶尔也要和妈妈\x01",
            "联络一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38FB")

    label("loc_38BF")


    #C0148
    ChrTalk(
        0xFE,
        (
            "偶尔也要和妈妈\x01",
            "联络一下，\x01",
            "毕竟我已经好久没回去过了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38FB")

    Jump("loc_3E32")

    label("loc_3900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D0")

    #C0149
    ChrTalk(
        0xFE,
        (
            "总觉得直到现在，\x01",
            "老板还是把我放在\x01",
            "『对桑桑图谋不轨者』的黑名单里。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "老板指派我管理打工人员，\x01",
            "也是为了让我没机会\x01",
            "和桑桑接触吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "唔……但我只是把\x01",
            "桑桑视为妹妹而已啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A44")

    label("loc_39D0")


    #C0152
    ChrTalk(
        0xFE,
        (
            "我已经和老板共事很久了，\x01",
            "在我眼里，\x01",
            "桑桑就像是妹妹一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "我只想默默保护她而已，\x01",
            "完全没有任何\x01",
            "不良企图啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A44")

    Jump("loc_3E32")

    label("loc_3A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AD3")

    #C0154
    ChrTalk(
        0xFE,
        (
            "据说老板当年曾在\x01",
            "东方人街治安最恶劣\x01",
            "的地方开过店。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "不过我是在克洛斯贝尔\x01",
            "与老板认识的，\x01",
            "他很少对我说起自己的往事～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E32")

    label("loc_3AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B95")

    #C0156
    ChrTalk(
        0xFE,
        (
            "老板好像很喜欢\x01",
            "修炼东方武术。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "听说他当年在东方人街开店的时候，\x01",
            "到店里闹事的家伙们\x01",
            "都是他自己打退的。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "也难怪他瞪着\x01",
            "靠近桑桑的男人时，\x01",
            "目光能如此锐利了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BE9")

    label("loc_3B95")


    #C0159
    ChrTalk(
        0xFE,
        (
            "老板好像很喜欢\x01",
            "修炼东方武术。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "嘿嘿，要是真的把他惹怒，\x01",
            "可就要后悔莫及了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE9")

    Jump("loc_3E32")

    label("loc_3BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBE")

    #C0161
    ChrTalk(
        0xFE,
        (
            "最近这段时间，我经常\x01",
            "向莉夏暗送秋波……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "但她每次都像完全没看到一样，\x01",
            "只是轻松地打个招呼，\x01",
            "然后就跑去练习了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "比起男女之情，\x01",
            "她现在还是对彩虹剧团的\x01",
            "表演更有兴趣啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D34")

    label("loc_3CBE")


    #C0164
    ChrTalk(
        0xFE,
        (
            "莉夏现在还是\x01",
            "对彩虹剧团的\x01",
            "表演更有兴趣啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "唔……相比之下，\x01",
            "不由得为自己这种过于悠闲的\x01",
            "生活态度感到羞愧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D34")

    Jump("loc_3E32")

    label("loc_3D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DBB")

    #C0166
    ChrTalk(
        0xFE,
        (
            "我让新来的帕库和鲁斯\x01",
            "负责算账、扫除和洗盘子\x01",
            "等杂活。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "这样一来，我终于可以\x01",
            "专心在厨房工作了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E32")

    label("loc_3DBB")


    #C0168
    ChrTalk(
        0xFE,
        (
            "我把所有杂活都分配给了\x01",
            "新来的帕库和鲁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "和连柜台后面都不能\x01",
            "让他们进来的时期相比，\x01",
            "这两个人也算有进步了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E32")

    TalkEnd(0xFE)
    Return()

    # Function_7_31FF end

    def Function_8_3E36(): pass

    label("Function_8_3E36")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3F35")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F30")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EAB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3EAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3ECA")
    OP_AF(0x34)
    Jump("loc_3ECC")

    label("loc_3ECA")

    OP_AF(0x33)

    label("loc_3ECC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F2B")

    label("loc_3EDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EFB")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F2B")

    label("loc_3EFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F0F")
    Jump("loc_3F2B")

    label("loc_3F0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_3F2B")

    Jump("loc_3E4C")

    label("loc_3F30")

    Jump("loc_3F38")

    label("loc_3F35")

    Call(0, 9)

    label("loc_3F38")

    TalkEnd(0xA)
    Return()

    # Function_8_3E36 end

    def Function_9_3F3C(): pass

    label("Function_9_3F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_41A4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_408D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F67")
    Call(0, 11)
    Jump("loc_4088")

    label("loc_3F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4033")

    #C0170
    ChrTalk(
        0xA,
        (
            "莉夏，\x01",
            "你们好像要去\x01",
            "很危险的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "其实我真想阻止你……\x01",
            "但既然你已经决定要去，\x01",
            "我就不说什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "我、我会等你的……\x01",
            "一定要平安回来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x106,
        "#10704F嗯……我一定会回来的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4088")

    label("loc_4033")


    #C0174
    ChrTalk(
        0xA,
        (
            "莉夏，\x01",
            "你们好像要去\x01",
            "很危险的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "我、我会等你的……\x01",
            "一定要平安回来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4088")

    Jump("loc_419F")

    label("loc_408D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_409F")
    Call(0, 10)
    Jump("loc_419F")

    label("loc_409F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414A")

    #C0176
    ChrTalk(
        0xA,
        (
            "莉夏好像\x01",
            "要和你们去\x01",
            "很危险的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "其实我真想阻止她……\x01",
            "但既然莉夏已经决定要去，\x01",
            "我就不说什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "我、我会等她的……\x01",
            "一定要平安回来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_419F")

    label("loc_414A")


    #C0179
    ChrTalk(
        0xA,
        (
            "莉夏好像\x01",
            "要和你们去\x01",
            "很危险的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "我、我会等她的……\x01",
            "一定要平安回来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_419F")

    Jump("loc_5037")

    label("loc_41A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_42ED")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_426B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41CF")
    Call(0, 11)
    Jump("loc_4266")

    label("loc_41CF")


    #C0181
    ChrTalk(
        0xA,
        (
            "（抽泣……）\x01",
            "能和莉夏再次见面，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "下次可不许一言不发就消失了！\x01",
            "不然我绝对不再原谅你！\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x106,
        (
            "#10704F嗯……一言为定。\x01",
            "谢谢你，桑桑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4266")

    Jump("loc_42E8")

    label("loc_426B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_427D")
    Call(0, 10)
    Jump("loc_42E8")

    label("loc_427D")


    #C0184
    ChrTalk(
        0xA,
        (
            "（抽泣……）\x01",
            "能和莉夏再次见面，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "下次可不许一言不发就消失了！\x01",
            "不然我绝对不再原谅你！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E8")

    Jump("loc_5037")

    label("loc_42ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_43F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438B")

    #C0186
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔竟然会\x01",
            "变成这样……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "我总有种感觉，\x01",
            "如果发生战争，\x01",
            "也许就真的无法再见到莉夏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        "莉夏现在在什么地方呢……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_43EB")

    label("loc_438B")


    #C0189
    ChrTalk(
        0xA,
        (
            "我总有种感觉，\x01",
            "如果发生战争，\x01",
            "也许就真的无法再见到莉夏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        "莉夏现在在什么地方呢……？\x02",
    )

    CloseMessageWindow()

    label("loc_43EB")

    Jump("loc_5037")

    label("loc_43F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4608")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4422")
    Call(0, 53)
    Return()

    label("loc_4422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4528")

    #C0191
    ChrTalk(
        0xA,
        (
            "……莉夏在离开之前，\x01",
            "给我留下了一张字条。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "『由于某些原因，\x01",
            "  我要离开克洛斯贝尔』——\x01",
            "字条上是这样写的……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "把彩虹剧团扔下不管，\x01",
            "说走就走……\x01",
            "这绝对不是莉夏的作风啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "……难道有什么隐情吗？\x01",
            "她要是和我谈谈该多好……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_459D")

    label("loc_4528")


    #C0195
    ChrTalk(
        0xA,
        (
            "把彩虹剧团扔下不管，\x01",
            "说走就走……\x01",
            "这绝对不是莉夏的作风啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        (
            "莫非有什么对我这个好朋友\x01",
            "都不能透露的隐情吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459D")

    Jump("loc_4603")

    label("loc_45A2")


    #C0197
    ChrTalk(
        0xA,
        (
            "我一定会努力为职业女性选秀\x01",
            "活动贡献一份力量！\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        (
            "我会在活动\x01",
            "开始前赶到的，\x01",
            "稍后再联系吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4603")

    Jump("loc_5037")

    label("loc_4608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_478A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4722")

    #C0199
    ChrTalk(
        0xA,
        (
            "今天一大早看到了\x01",
            "准备赶往彩虹剧团\x01",
            "的莉夏。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "我和她打了招呼……\x01",
            "但不知为什么，\x01",
            "她好像非常没精神呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 7)), scpexpr(EXPR_END)), "loc_46CF")

    #C0201
    ChrTalk(
        0x101,
        (
            "#00008F（……现在也只能让她\x01",
            "  一个人慢慢平复了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471A")

    label("loc_46CF")


    #C0202
    ChrTalk(
        0x101,
        (
            "#00003F（……莉夏……\x01",
            "　要不要去彩虹剧团\x01",
            "  看看她现在的情况呢……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471A")

    SetScenarioFlags(0x0, 2)
    Jump("loc_4785")

    label("loc_4722")


    #C0203
    ChrTalk(
        0xA,
        (
            "我今天早上见到了莉夏……\x01",
            "但她非常没精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "……发生什么事情了吗？\x01",
            "本来还想和她\x01",
            "聊一聊呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4785")

    Jump("loc_5037")

    label("loc_478A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_4857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47FA")

    #C0205
    ChrTalk(
        0xA,
        (
            "但莉夏说还有事要去做，\x01",
            "直接走掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        (
            "呼，要是能多聊\x01",
            "几句就好了……真没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4852")

    label("loc_47FA")


    #C0207
    ChrTalk(
        0xA,
        (
            "要是能和莉夏多聊\x01",
            "几句就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xA,
        (
            "但她还有事要办，也没办法。\x01",
            "……必须要工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4852")

    Jump("loc_5037")

    label("loc_4857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_48CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4872")
    Call(0, 48)
    Jump("loc_48C9")

    label("loc_4872")


    #C0209
    ChrTalk(
        0xA,
        (
            "嘿嘿嘿……莉夏把话说得那么坦率，\x01",
            "真让人不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        "我们永远都是朋友哦，莉夏！\x02",
    )

    CloseMessageWindow()

    label("loc_48C9")

    Jump("loc_5037")

    label("loc_48CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_493C")

    #C0211
    ChrTalk(
        0xA,
        (
            "帕库和鲁斯的工作能力\x01",
            "还是达不到要求，\x01",
            "最后又回到原来的岗位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        "真是的，爸爸也够坏的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5037")

    label("loc_493C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A9B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49BD")

    #C0213
    ChrTalk(
        0xA,
        (
            "……美食向导的取材？\x01",
            "哦，我听说过～\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xA,
        (
            "爸爸在厨房呢，\x01",
            "你们去和他说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A96")

    label("loc_49BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3C")

    #C0215
    ChrTalk(
        0xA,
        (
            "爸爸和芬先生\x01",
            "让我今天只负责会计工作，\x01",
            "把我留在了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        (
            "……但帕库和鲁斯好像\x01",
            "手忙脚乱的，没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A96")

    label("loc_4A3C")


    #C0217
    ChrTalk(
        0xA,
        (
            "今天要由帕库负责\x01",
            "所有的服务工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xA,
        (
            "……他好像手忙脚乱的。\x01",
            "真的不用过去帮帮他吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A96")

    Jump("loc_5037")

    label("loc_4A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4B1C")

    #C0219
    ChrTalk(
        0xA,
        (
            "欢迎光临～\x01",
            "要点些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "来店的客人好像都在聊\x01",
            "有关通商会议的话题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "市长说的事情\x01",
            "是那么重要的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5037")

    label("loc_4B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD3")

    #C0222
    ChrTalk(
        0xA,
        (
            "帕库和鲁斯是我的童年玩伴，\x01",
            "推荐他们来这里打工的就是我。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xA,
        (
            "嗯嗯，他们两个好像都很努力，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xA,
        "在爸爸面前，我这个推荐人也觉得面上有光呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4C27")

    label("loc_4BD3")


    #C0225
    ChrTalk(
        0xA,
        (
            "帕库和鲁斯\x01",
            "工作得好像\x01",
            "很努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xA,
        "在爸爸面前，我这个推荐人也觉得面上有光呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4C27")

    Jump("loc_5037")

    label("loc_4C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE4")

    #C0227
    ChrTalk(
        0xA,
        (
            "爸爸说，共和国的\x01",
            "东方人要比克洛斯贝尔\x01",
            "更多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xA,
        (
            "不过我从小就\x01",
            "移居到了这里，\x01",
            "已经没印象了……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xA,
        (
            "共和国应该是个很热闹的地方吧，\x01",
            "想想就觉得很有趣～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D44")

    label("loc_4CE4")


    #C0230
    ChrTalk(
        0xA,
        (
            "共和国的东方人好像\x01",
            "比克洛斯贝尔还多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "肯定又热闹又有趣吧～\x01",
            "如果有机会，真想去看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D44")

    Jump("loc_5037")

    label("loc_4D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DD6")
    TurnDirection(0xA, 0x1A2, 0)
    Sleep(300)

    #C0232
    ChrTalk(
        0xA,
        "啊，是刚才那位可爱的客人。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        "下次还要再来哦～随时都欢迎你光临。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x1A2,
        "啊……嗯嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E36")

    label("loc_4DD6")


    #C0235
    ChrTalk(
        0xA,
        (
            "坐在吧台前的那个女人\x01",
            "好像是利贝尔的记者～\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xA,
        (
            "呵呵，机会难得，\x01",
            "请她帮我拍张可爱的照片吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E36")

    Jump("loc_5037")

    label("loc_4E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EFB")

    #C0237
    ChrTalk(
        0xA,
        (
            "芬先生可真是的，\x01",
            "竟然向莉夏搭讪，\x01",
            "太伤脑筋了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xA,
        (
            "莉夏将来\x01",
            "一定会遇到\x01",
            "更优秀的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        (
            "虽然这样说对芬先生有些失礼，\x01",
            "但身为莉夏的好友，我还是坚持这种看法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4F52")

    label("loc_4EFB")


    #C0240
    ChrTalk(
        0xA,
        (
            "莉夏将来\x01",
            "一定会遇到\x01",
            "更优秀的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "嘿嘿嘿，身为她的好友，\x01",
            "我可以保证这一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F52")

    Jump("loc_5037")

    label("loc_4F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5037")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC2")

    #C0242
    ChrTalk(
        0xA,
        (
            "欢迎～\x01",
            "请随意就坐～\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        (
            "爸爸虽然有点可怕，\x01",
            "但做出的料理可是天下一流的哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5037")

    label("loc_4FC2")


    #C0244
    ChrTalk(
        0xA,
        (
            "我来店里帮忙\x01",
            "虽然还不足一年，\x01",
            "但已经完全习惯了这里的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "客人们都很友善，\x01",
            "我想应该可以就这样一直干下去～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5037")

    Return()

    # Function_9_3F3C end

    def Function_10_5038(): pass

    label("Function_10_5038")


    #C0246
    ChrTalk(
        0xA,
        (
            "莉夏……\x01",
            "现在正在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔发生了\x01",
            "这样的事情……我好担心她。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        (
            "#00003F（……稍后应该\x01",
            "  带莉夏过来啊……）\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_10_5038 end

    def Function_11_50BB(): pass

    label("Function_11_50BB")

    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    #C0249
    ChrTalk(
        0xA,
        (
            "莉、莉夏……\x01",
            "这不是莉夏吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "你、你这段时间到底去哪里了！？\x01",
            "我好担心啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x106,
        (
            "#10703F对不起，桑桑……\x01",
            "让你担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "呜呜……真是的！\x01",
            "莉夏是笨蛋！\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xA,
        (
            "……不过……\x01",
            "能再次见到你，真是太好了……\x01",
            "呜～呜呜呜呜呜……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x106)

    #C0254
    ChrTalk(
        0x106,
        "#10705F别、别哭了，桑桑……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "呜……\x01",
            "可是我真的很担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xA,
        (
            "下次可不许一言不发就消失了！\x01",
            "不然我绝对不再原谅你！\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x106,
        (
            "#10704F嗯，真对不起。\x01",
            "……谢谢你一直等我。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#00002F（莉夏……太好了。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 0)
    Return()

    # Function_11_50BB end

    def Function_12_52AC(): pass

    label("Function_12_52AC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_53AB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5321")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5340")
    OP_AF(0x34)
    Jump("loc_5342")

    label("loc_5340")

    OP_AF(0x33)

    label("loc_5342")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53A1")

    label("loc_5351")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5371")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53A1")

    label("loc_5371")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5385")
    Jump("loc_53A1")

    label("loc_5385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_53A1")

    Jump("loc_52C2")

    label("loc_53A6")

    Jump("loc_53AE")

    label("loc_53AB")

    Call(0, 13)

    label("loc_53AE")

    TalkEnd(0xB)
    Return()

    # Function_12_52AC end

    def Function_13_53B2(): pass

    label("Function_13_53B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_54A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544C")

    #C0259
    ChrTalk(
        0xB,
        (
            "填饱肚子就是最大的幸福——\x01",
            "这是老板的座右铭。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        (
            "等我将来和鲁斯一起开店的时候，\x01",
            "也要像老板这样，\x01",
            "时刻把客人放在第一位。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_54A0")

    label("loc_544C")


    #C0261
    ChrTalk(
        0xB,
        (
            "对了，今天可以免费添饭，\x01",
            "想添多少都可以哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xB,
        (
            "多吃一些，\x01",
            "让自己充满干劲吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54A0")

    Jump("loc_5DE7")

    label("loc_54A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5517")

    #C0263
    ChrTalk(
        0xB,
        (
            "现在可不是扫除的时候啊。\x01",
            "……虽说如此，\x01",
            "也没办法逃到什么地方去……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        "呼……真是只能叹气了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DE7")

    label("loc_5517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_558B")

    #C0265
    ChrTalk(
        0xB,
        (
            "今后到底会怎样呢，\x01",
            "反正我是完全预测不到……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "但正是在这种时候，\x01",
            "才更要鼓起勇气，跨越困难啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE7")

    label("loc_558B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5620")

    #C0267
    ChrTalk(
        0xB,
        (
            "芬先生去\x01",
            "慈善宴会的会场\x01",
            "帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xB,
        (
            "所以由我代替他进入厨房，\x01",
            "给老板打下手。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        (
            "我必须要尽己所能，\x01",
            "努力完成工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_566E")

    label("loc_5620")


    #C0270
    ChrTalk(
        0xB,
        (
            "虽然我只会做\x01",
            "一些杂活……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "但芬先生现在不在，\x01",
            "我也只能努力试试看了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566E")

    Jump("loc_5DE7")

    label("loc_5673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5703")

    #C0272
    ChrTalk(
        0xB,
        "一百米拉、两百米拉、三百米拉……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xB,
        (
            "呵呵，收款工作做得\x01",
            "已经比原来顺手多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xB,
        (
            "只有一步一步努力，\x01",
            "才能获得真正的成长啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE7")

    label("loc_5703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_580A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AF")

    #C0275
    ChrTalk(
        0xB,
        (
            "我原本一直以为，\x01",
            "光凭干劲就能应付任何工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xB,
        (
            "但那种想法的确是\x01",
            "有些天真啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        (
            "总之，现在要先把我所能做到的事做好！\x01",
            "这才是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5805")

    label("loc_57AF")


    #C0278
    ChrTalk(
        0xB,
        (
            "我和鲁斯那家伙\x01",
            "昨天相当沮丧……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "呼，但现在也只能\x01",
            "先把能做到的事尽力做好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5805")

    Jump("loc_5DE7")

    label("loc_580A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_587E")

    #C0280
    ChrTalk(
        0xB,
        "呼，好累啊……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xB,
        (
            "看桑桑工作的时候，\x01",
            "觉得一天到晚都很轻松有趣，\x01",
            "实际上却完全不是那么回事啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE7")

    label("loc_587E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_58D0")

    #C0282
    ChrTalk(
        0xB,
        (
            "擦桌子，写单子，\x01",
            "端菜……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "呜哇哇，忙得都要\x01",
            "晕头转向了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE7")

    label("loc_58D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599A")

    #C0284
    ChrTalk(
        0xB,
        (
            "为了获得更多薪水，\x01",
            "鲁斯希望转到\x01",
            "更加重要的工作岗位。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "为了将来一起开店，\x01",
            "确实需要从现在开始努力攒钱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xB,
        (
            "呵呵，无论是什么样的工作，\x01",
            "我和鲁斯也都能\x01",
            "鼓足干劲完成。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_59DA")

    label("loc_599A")


    #C0287
    ChrTalk(
        0xB,
        (
            "嘿嘿，说不定我有\x01",
            "当店员的才能呢……\x01",
            "去和老板商量一下好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59DA")

    Jump("loc_5DE7")

    label("loc_59DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ABC")

    #C0288
    ChrTalk(
        0xB,
        (
            "我、鲁斯和桑桑\x01",
            "在上主日学校时\x01",
            "是同年级的学生……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "从那时开始，\x01",
            "只要和桑桑稍有来往，\x01",
            "老板的脸色就很恐怖。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "刚才也是，我只不过\x01",
            "和桑桑打了个招呼，\x01",
            "他就狠狠瞪我。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xB,
        "呼，真是受不了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5B27")

    label("loc_5ABC")


    #C0292
    ChrTalk(
        0xB,
        (
            "我只不过和桑桑打了个招呼，\x01",
            "就被老板狠狠瞪……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xB,
        (
            "从主日学校时代开始\x01",
            "就一直是这样……\x01",
            "真是受不了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B27")

    Jump("loc_5DE7")

    label("loc_5B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B9F")

    #C0294
    ChrTalk(
        0xB,
        (
            "鲁斯不管做什么事情，\x01",
            "总是非常在意形式。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "其实就算把我们\x01",
            "要开的店变为饭店，\x01",
            "我也完全不介意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE7")

    label("loc_5B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C10")

    #C0296
    ChrTalk(
        0xB,
        (
            "鲁斯那家伙总是\x01",
            "考虑得太多。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "我们这么努力，\x01",
            "将来一定会成为了不起的人物！\x01",
            "没什么好担心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE7")

    label("loc_5C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C7A")

    #C0298
    ChrTalk(
        0xB,
        (
            "疼死了……\x01",
            "刚才不小心\x01",
            "摔了个四脚朝天。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "噢噢～用斗志来\x01",
            "驱散这痛楚吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5CE1")

    label("loc_5C7A")


    #C0300
    ChrTalk(
        0xB,
        (
            "……疼死了。\x01",
            "呼，不管有没有斗志，\x01",
            "痛楚也是不会消失的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "下雨天，地面太滑了，\x01",
            "你们也要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CE1")

    Jump("loc_5DE7")

    label("loc_5CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5DE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D99")

    #C0302
    ChrTalk(
        0xB,
        (
            "从不久前开始，我和好搭档鲁斯\x01",
            "一起在这里打工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xB,
        (
            "不过收钱算帐这种工作，\x01",
            "我并不是很擅长。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "工作虽然很有趣，\x01",
            "但总是把钱算错，\x01",
            "遭到严厉训斥。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DE7")

    label("loc_5D99")


    #C0305
    ChrTalk(
        0xB,
        (
            "话说回来，\x01",
            "饮食店店员这种工作\x01",
            "倒是挺符合我的性格。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xB,
        "继续开心工作吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5DE7")

    Return()

    # Function_13_53B2 end

    def Function_14_5DE8(): pass

    label("Function_14_5DE8")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_5EE7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EE2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E5D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5E5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E7C")
    OP_AF(0x34)
    Jump("loc_5E7E")

    label("loc_5E7C")

    OP_AF(0x33)

    label("loc_5E7E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EDD")

    label("loc_5E8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EAD")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EDD")

    label("loc_5EAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EC1")
    Jump("loc_5EDD")

    label("loc_5EC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EDD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 15)

    label("loc_5EDD")

    Jump("loc_5DFE")

    label("loc_5EE2")

    Jump("loc_5EEA")

    label("loc_5EE7")

    Call(0, 15)

    label("loc_5EEA")

    TalkEnd(0xC)
    Return()

    # Function_14_5DE8 end

    def Function_15_5EEE(): pass

    label("Function_15_5EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_604D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC5")

    #C0307
    ChrTalk(
        0xC,
        (
            "在这种非常时期所获得的经验，\x01",
            "将来一定会发挥作用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "我将来想和搭档帕库\x01",
            "一起开一家大商店……\x01",
            "不过目前还是要专心做好眼前的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "……好～既然已经决定了，\x01",
            "就赶快开始扫除吧！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6048")

    label("loc_5FC5")


    #C0310
    ChrTalk(
        0xC,
        (
            "在这种非常时期所获得的经验，\x01",
            "将来和帕库一起开商店的时候\x01",
            "也一定能发挥作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xC,
        (
            "……好～既然已经决定了，\x01",
            "就赶快开始扫除吧！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6048")

    Jump("loc_6BD9")

    label("loc_604D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_609B")

    #C0312
    ChrTalk(
        0xC,
        "那种东西竟然在外面徘徊……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xC,
        "我们到底该怎么办才好……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BD9")

    label("loc_609B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_60FB")

    #C0314
    ChrTalk(
        0xC,
        (
            "呀哈！克洛斯贝尔\x01",
            "成为独立国家了！\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "哈哈，可喜可贺。\x01",
            "扫除时都充满干劲呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD9")

    label("loc_60FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6167")

    #C0316
    ChrTalk(
        0xC,
        (
            "这里紧挨着旧城区，\x01",
            "运气不好的话，\x01",
            "说不定就像旧城区那样一片狼藉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "……（发抖）。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BD9")

    label("loc_6167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_622A")

    #C0318
    ChrTalk(
        0xC,
        (
            "唔，因为嫌麻烦，所以我在打扫时\x01",
            "总是东扫一下，西扫一下的……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        (
            "但仔细想想，如果认认真真地从头到尾打扫一遍，\x01",
            "说不定反而会比我来回重复更省时间呢。\x01",
            "扫除里面也有很深的学问呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD9")

    label("loc_622A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_63EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62CA")

    #C0320
    ChrTalk(
        0xC,
        (
            "美食向导的取材……？\x01",
            "哦哦，说起来，老板好像\x01",
            "也说起过这件事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "老板就在厨房，\x01",
            "你们去那边和他说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_62CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6395")

    #C0322
    ChrTalk(
        0xC,
        (
            "昨天去厨房学习了，\x01",
            "结果大受挫折……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xC,
        (
            "但和帕库谈过之后，\x01",
            "我决定振作精神，\x01",
            "努力做好如今力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xC,
        (
            "如果我连简单的工作都做不好，\x01",
            "老板自然不会把更难的重要工作\x01",
            "交给我……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_63E9")

    label("loc_6395")


    #C0325
    ChrTalk(
        0xC,
        (
            "为了将来和搭档帕库\x01",
            "一起开一家大商店……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "我现在一定要努力\x01",
            "把这些杂活做好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E9")

    Jump("loc_6BD9")

    label("loc_63EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6446")

    #C0327
    ChrTalk(
        0xC,
        (
            "……终于从地狱般的\x01",
            "厨房解放出来了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xC,
        (
            "我们真是\x01",
            "完全不行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD9")

    label("loc_6446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C3")
    OP_4B(0x8, 0xFF)

    #C0329
    ChrTalk(
        0xC,
        (
            "好、好热……！\x01",
            "而且东方的大锅\x01",
            "真是重死了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        "喂！动作快点！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        "对、对不起！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_6524")

    label("loc_64C3")


    #C0332
    ChrTalk(
        0xC,
        (
            "呜、呜啊……\x01",
            "之前打下手的时候，\x01",
            "本以为可以轻松搞定……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "没想到光是炒个饭\x01",
            "就如此艰难……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6524")

    Jump("loc_6BD9")

    label("loc_6529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6703")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65C5")

    #C0334
    ChrTalk(
        0xC,
        (
            "美食向导的取材……？\x01",
            "哦，说起来，老板好像\x01",
            "也说起过这件事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        (
            "老板在厨房呢，\x01",
            "你们过去和他说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66FE")

    label("loc_65C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668D")

    #C0336
    ChrTalk(
        0xC,
        (
            "光靠打零工赚的\x01",
            "这点小钱，\x01",
            "根本就不可能积累创业资金啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xC,
        (
            "不然去和老板商量商量，\x01",
            "让他把我换到更重要\x01",
            "的工作岗位吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xC,
        (
            "反正～不管是什么工作，\x01",
            "我和帕库都一定可以\x01",
            "轻松搞定。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66FE")

    label("loc_668D")


    #C0339
    ChrTalk(
        0xC,
        (
            "差不多也该让我们放弃杂活，\x01",
            "去做些重要的工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xC,
        (
            "我之前也曾去厨房\x01",
            "帮过一些忙……\x01",
            "下次就找老板谈谈好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66FE")

    Jump("loc_6BD9")

    label("loc_6703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67AC")

    #C0341
    ChrTalk(
        0xC,
        (
            "需要扫除的地方\x01",
            "突然就增加到了两倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xC,
        (
            "莫非是帕库那小子\x01",
            "在老板面前\x01",
            "和桑桑搭话了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "如果真是那样，我可就是平白遭受牵连了。\x01",
            "呼～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_67F4")

    label("loc_67AC")


    #C0344
    ChrTalk(
        0xC,
        (
            "嗯，稍后还要\x01",
            "打扫厨房……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xC,
        (
            "都怪帕库太大意，\x01",
            "害得我要做大扫除。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67F4")

    Jump("loc_6BD9")

    label("loc_67F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_68E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6884")

    #C0346
    ChrTalk(
        0xC,
        (
            "帕库说，\x01",
            "我们将来开了商店之后，\x01",
            "可以在里面加入个餐厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xC,
        (
            "唉……\x01",
            "连基本资金都还没攒够，\x01",
            "就开始说胡话了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_68DE")

    label("loc_6884")


    #C0348
    ChrTalk(
        0xC,
        (
            "我将来想和帕库\x01",
            "一起开家大商店……\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        (
            "但他却突然开始说\x01",
            "要在店里经营个餐厅这种胡话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68DE")

    Jump("loc_6BD9")

    label("loc_68E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_69C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_695A")

    #C0350
    ChrTalk(
        0xC,
        (
            "帕库那家伙\x01",
            "好像很喜欢\x01",
            "这份工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xC,
        (
            "难道他忘了我们的\x01",
            "真正目的是要\x01",
            "一起开店了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69BB")

    label("loc_695A")


    #C0352
    ChrTalk(
        0xC,
        (
            "这份工作只不过是\x01",
            "积累开店资金的\x01",
            "准备手段而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xC,
        (
            "帕库那家伙，\x01",
            "怎么一副乐在其中的样子……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69BB")

    Jump("loc_6BD9")

    label("loc_69C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A72")

    #C0354
    ChrTalk(
        0xC,
        (
            "呼……\x01",
            "每当听到雨声，\x01",
            "就会不由得陷入忧愁。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xC,
        (
            "虽然正在慢慢地攒钱，\x01",
            "但离能自己开店还差得很远。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xC,
        (
            "一直这样继续\x01",
            "打工下去，\x01",
            "真的就能接近梦想吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6ACB")

    label("loc_6A72")


    #C0357
    ChrTalk(
        0xC,
        (
            "一直这样继续\x01",
            "打工下去，\x01",
            "真的就能接近梦想吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xC,
        (
            "稍后去听听\x01",
            "帕库那家伙的意见吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ACB")

    Jump("loc_6BD9")

    label("loc_6AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B60")

    #C0359
    ChrTalk(
        0xC,
        (
            "我和搭档帕库\x01",
            "为了积累开店的资金，\x01",
            "开始在这里打工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xC,
        (
            "我们是为了有朝一日自己开店，\x01",
            "才会在这里做些低等工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BD9")

    label("loc_6B60")


    #C0361
    ChrTalk(
        0xC,
        (
            "话说回来，老板非常严厉，\x01",
            "薪水给得又少……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "多亏童年好友桑桑的推荐，\x01",
            "我才能来这里打工……\x01",
            "但最近总觉得有些后悔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD9")

    Return()

    # Function_15_5EEE end

    def Function_16_6BDA(): pass

    label("Function_16_6BDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6D26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CB8")

    #C0363
    ChrTalk(
        0xFE,
        (
            "（大吃大嚼）……\x01",
            "我们公司的运输业务已经恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "以前一直以共和国和自治州\x01",
            "之间的运输路线为主要业务，\x01",
            "但今后暂时只能在自治州内运输了。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "算啦，反正做的都是同样的工作，\x01",
            "继续努力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6D21")

    label("loc_6CB8")


    #C0366
    ChrTalk(
        0xFE,
        (
            "虽然只能在自治州内\x01",
            "运输了，\x01",
            "但做的仍然是同样的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "先把肚子填饱，\x01",
            "然后和往常一样努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D21")

    Jump("loc_76C9")

    label("loc_6D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6D34")
    Jump("loc_76C9")

    label("loc_6D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DED")

    #C0368
    ChrTalk(
        0xFE,
        (
            "身为克洛斯贝尔的居民，\x01",
            "自然对独立感到欢喜。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "更何况，担任国防军\x01",
            "长官的人就是\x01",
            "英雄亚里欧斯·马克莱因。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "就算与帝国和共和国为敌，\x01",
            "也让人很有底气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6E81")

    label("loc_6DED")


    #C0371
    ChrTalk(
        0xFE,
        (
            "在了解到帝国和共和国的对策之前，\x01",
            "我们公司准备暂时停业。\x01",
            "……总之不必担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "再怎么说，克洛斯贝尔\x01",
            "还有风之剑圣坐镇呢。\x01",
            "他一定会保护我们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E81")

    Jump("loc_76C9")

    label("loc_6E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F24")

    #C0373
    ChrTalk(
        0xFE,
        (
            "由于工作原因，\x01",
            "我要经常前往唐古拉姆门……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "那里的气氛似乎\x01",
            "变得比平时紧张多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "对出入人员的盘查\x01",
            "也比平时更加严格了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6F88")

    label("loc_6F24")


    #C0376
    ChrTalk(
        0xFE,
        (
            "边境大门要是一直保持那种状态，\x01",
            "我的工作都不能顺利完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "先吃点东西吧。\x01",
            "（大吃大嚼）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F88")

    Jump("loc_76C9")

    label("loc_6F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7027")

    #C0378
    ChrTalk(
        0xFE,
        (
            "竟然占领了玛因兹……\x01",
            "不知道是什么人干的，\x01",
            "总之真是很惊人的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "算了，克洛斯贝尔的警备队\x01",
            "精英云集，\x01",
            "有他们处理，肯定没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76C9")

    label("loc_7027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7080")

    #C0380
    ChrTalk(
        0xFE,
        "真不凑巧，今天又赶上下雨啊……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "在雨天驾驶很危险，\x01",
            "必须得小心点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76C9")

    label("loc_7080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7175")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7120")

    #C0382
    ChrTalk(
        0xFE,
        (
            "哦，服务员换回\x01",
            "原来那个小姑娘了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "嗯，既然如此，\x01",
            "就点杯饭后\x01",
            "饮料吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "……嗯，哇！？\x01",
            "都已经过了\x01",
            "送货的出发时间了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7170")

    label("loc_7120")


    #C0385
    ChrTalk(
        0xFE,
        (
            "不、不好了，\x01",
            "送货的出发时间\x01",
            "都已经过去好久了！\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        "再、再不赶快就糟了……\x02",
    )

    CloseMessageWindow()

    label("loc_7170")

    Jump("loc_76C9")

    label("loc_7175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71DE")

    #C0387
    ChrTalk(
        0xFE,
        (
            "哦……今天的服务员\x01",
            "不是平时那个小姑娘啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "唔……总感觉\x01",
            "有点不协调。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_720C")

    label("loc_71DE")


    #C0389
    ChrTalk(
        0xFE,
        (
            "只有那个小姑娘\x01",
            "的笑脸才与这家店\x01",
            "相称啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_720C")

    Jump("loc_76C9")

    label("loc_7211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B3")

    #C0390
    ChrTalk(
        0xFE,
        (
            "说起现在性能最强\x01",
            "的导力卡车，\x01",
            "还要属乌尔努公司的最新型。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "不过，新型车\x01",
            "可不是我们公司\x01",
            "能负担得起的……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "毕竟价格\x01",
            "太高了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7313")

    label("loc_72B3")


    #C0393
    ChrTalk(
        0xFE,
        (
            "最新型的导力车\x01",
            "可不是一般公司能买得起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "除非是经济效益特别好的公司，\x01",
            "不然很难负担。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7313")

    Jump("loc_76C9")

    label("loc_7318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7391")

    #C0395
    ChrTalk(
        0xFE,
        (
            "唔，其实我也有点\x01",
            "在意通商会议……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "但毕竟还有工作要做，\x01",
            "现在还是赶紧填饱肚子吧。\x01",
            "（大吃大嚼）……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76C9")

    label("loc_7391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_73FE")

    #C0397
    ChrTalk(
        0xFE,
        (
            "哎呀呀，东街\x01",
            "真够热闹的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "交通管制好像已经解除了……\x01",
            "我也要恢复工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76C9")

    label("loc_73FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74E3")

    #C0399
    ChrTalk(
        0xFE,
        (
            "听说明天要对唐古拉姆门\x01",
            "到东克洛斯贝尔街道\x01",
            "的地段实行交通管制。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "好像是因为共和国的总统\x01",
            "要来参加通商会议，\x01",
            "所以准备采取戒严措施。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "呼，虽然并不会\x01",
            "戒严一整天……\x01",
            "但对工作多少还是有点影响啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7561")

    label("loc_74E3")


    #C0402
    ChrTalk(
        0xFE,
        (
            "听说明天要对唐古拉姆门\x01",
            "到东克洛斯贝尔街道\x01",
            "的地段实行交通管制。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "虽然并不会戒严一整天……\x01",
            "但还是要重新安排\x01",
            "行程表啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7561")

    Jump("loc_76C9")

    label("loc_7566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_75C3")

    #C0404
    ChrTalk(
        0xFE,
        (
            "今天好像有\x01",
            "大面积降雨。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "趁着雨下大之前，\x01",
            "还是尽快把工作\x01",
            "解决为好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76C9")

    label("loc_75C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_76C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7661")

    #C0406
    ChrTalk(
        0xFE,
        (
            "今天从\x01",
            "共和国那边\x01",
            "发来了很多货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "穿越流经\x01",
            "边境线的丘利河，\x01",
            "跨越唐古拉姆丘陵。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "运输业也不是那么好干的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_76C9")

    label("loc_7661")


    #C0409
    ChrTalk(
        0xFE,
        (
            "穿越流经\x01",
            "边境线的丘利河，\x01",
            "跨越唐古拉姆丘陵。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "已经吃饱了……\x01",
            "差不多该开始\x01",
            "把市里的货送一送了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76C9")

    TalkEnd(0xFE)
    Return()

    # Function_16_6BDA end

    def Function_17_76CD(): pass

    label("Function_17_76CD")

    TalkBegin(0xFE)

    #C0411
    ChrTalk(
        0xFE,
        "我很担心露天店铺的状况……\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "更重要的是，摩尔斯会长和洛依\x01",
            "他们还好吧……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_76CD end

    def Function_18_7727(): pass

    label("Function_18_7727")

    TalkBegin(0xFE)

    #C0413
    ChrTalk(
        0xFE,
        (
            "莉莉，有我在你身边呢，\x01",
            "不用担心。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_7727 end

    def Function_19_7755(): pass

    label("Function_19_7755")

    TalkBegin(0xFE)

    #C0414
    ChrTalk(
        0xFE,
        "迪因兹，我好害怕……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_7755 end

    def Function_20_7776(): pass

    label("Function_20_7776")

    TalkBegin(0xFE)

    #C0415
    ChrTalk(
        0xFE,
        (
            "希望我那在家里\x01",
            "的丈夫平安无事……\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "呼，发生了这种事，\x01",
            "只能赶快关店了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_7776 end

    def Function_21_77CD(): pass

    label("Function_21_77CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77E1")
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    label("loc_77E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7802")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7802")
    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    label("loc_7802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D3")

    #C0417
    ChrTalk(
        0x25,
        (
            "#03204F在事态平息下来之前，\x01",
            "我们准备暂时旁观。\x02\x03",

            "鲁巴彻和赤色星座都已不在了，\x01",
            "克洛斯贝尔的地下世界\x01",
            "便要慢慢重回我们手中了。\x02\x03",

            "#03210F呵呵，今后说不定\x01",
            "还会与各位对立，\x01",
            "到时还请多多包涵了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_7946")

    label("loc_78D3")


    #C0418
    ChrTalk(
        0x25,
        (
            "#03204F在事态平息下来之前，\x01",
            "我们准备暂时旁观。\x02\x03",

            "#03210F呵呵，今后说不定\x01",
            "还会与各位对立，\x01",
            "到时还请多多包涵了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7946")

    TalkEnd(0xFE)
    Return()

    # Function_21_77CD end

    def Function_22_794A(): pass

    label("Function_22_794A")


    #C0419
    ChrTalk(
        0x25,
        (
            "#03200F呀，是罗伊德警官和各位……\x01",
            "大家辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#00005F曹、曹先生！？\x01",
            "你们在这种地方做什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x25,
        (
            "#03204F呵呵，我们在这里\x01",
            "难道很奇怪吗？\x02\x03",

            "#03200F市里已经平静下来了，\x01",
            "我们只不过是来吃些东西，\x01",
            "放松一下而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x104,
        (
            "#00306F话虽如此，\x01",
            "但未免也太肆无忌惮了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        (
            "#00106F而、而且还坐在\x01",
            "正中间的座位……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x26,
        "我也觉得不太合适……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x26,
        (
            "但服务员小姐把我们带到了这个位子，\x01",
            "曹先生也没有拒绝。\x02",
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
            "#03204F呵呵，这不是很好嘛，\x01",
            "用餐时总要\x01",
            "轻松一些。\x02\x03",

            "#03200F毕竟在解放克洛斯贝尔市的作战中，\x01",
            "我们刚刚与『赤色星座』大战了一番，\x01",
            "好久都没有这么拼命过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x101,
        (
            "#00003F……关于这件事，真是\x01",
            "多谢你们的帮忙了。\x02\x03",

            "#00001F曹先生，你们今后\x01",
            "有什么打算呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x25,
        (
            "#03205F在事态平息下来之前，\x01",
            "我们准备暂时旁观。\x02\x03",

            "#03209F等到事态平息下来之后，\x01",
            "我们就准备建立新事务所，\x01",
            "重新开始业务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x103,
        "#00201F……果然如此啊。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x25,
        (
            "#03204F『赤色星座』和『鲁巴彻』等\x01",
            "竞争对手都已不在了，\x01",
            "如今已经没有妨碍我们的东西了。\x02\x03",

            "#03202F呵呵，虽然一波三折……\x01",
            "但我们最初的目的——掌控克洛斯贝尔\x01",
            "的地下世界，总算是可以实现了。\x02\x03",

            "可以说，这全都是托支援科的各位，\x01",
            "还有一直帮我们做事的\x01",
            "『银』大人的福啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        "#00013F你……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E1D")

    #C0432
    ChrTalk(
        0x106,
        "#10708F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_7E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E70")

    #C0433
    ChrTalk(
        0x10A,
        (
            "#00603F……也就是说，我们将会\x01",
            "再次与『黑月』展开对立啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0B")

    label("loc_7E70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EC1")

    #C0434
    ChrTalk(
        0x109,
        (
            "#10103F也就是说，我们将会\x01",
            "再次与『黑月』展开对立啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0B")

    label("loc_7EC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F0B")

    #C0435
    ChrTalk(
        0x105,
        (
            "#10403F也就是说，我们将会\x01",
            "再次与『黑月』展开对立吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F0B")


    #C0436
    ChrTalk(
        0x25,
        (
            "#03209F呵呵，也可以这么说吧……\x01",
            "总之，今后还请继续关照了，\x01",
            "各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#00003F……无论你们竖立起\x01",
            "怎样的『壁障』……\x02\x03",

            "#00001F我们也绝不会输的。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x25,
        (
            "#03209F呵呵，这才是罗伊德警官啊。\x02\x03",

            "#03204F哎呀，不过我们这边的\x01",
            "『壁障』也没什么了不起的。\x02\x03",

            "#03210F和整个大陆的混乱，特别是来自西方的\x01",
            "威胁相比，实在是不值一提。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        "#00011F……这、这个……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x25,
        (
            "#03204F呵呵，总之，\x01",
            "在事态平息下来之前，\x01",
            "就请各位多加努力吧。\x02\x03",

            "#03200F我们会在这里\x01",
            "默默声援大家的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 1)
    Return()

    # Function_22_794A end

    def Function_23_80CE(): pass

    label("Function_23_80CE")


    #C0441
    ChrTalk(
        0x25,
        (
            "#03204F对了……等事态平息下来以后，\x01",
            "我们还想与莉夏小姐\x01",
            "重新签订契约。\x02\x03",

            "#03202F呵呵，不知莉夏小姐\x01",
            "意下如何呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x106,
        (
            "#10703F……这次欠下你们的人情，\x01",
            "有朝一日一定\x01",
            "会以某种形式奉还……\x02\x03",

            "#10701F但我如今还无法\x01",
            "做出肯定的答复。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        "#00002F莉夏……\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x25,
        (
            "#03204F也罢，我们并没有\x01",
            "强迫你的权力。\x02\x03",

            "而且这次的事情\x01",
            "只是对等的协助关系而已，\x01",
            "还谈不上什么欠人情。\x02\x03",

            "#03200F不过，如果莉夏小姐\x01",
            "觉得有些亏欠我们……\x02\x03",

            "#03209F就送我们几张彩虹剧团\x01",
            "的Ｓ席门票好了。\x02",
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
            "#03204F呵呵，开个玩笑。\x02\x03",

            "#03200F不过……正如之前所说，\x01",
            "为了完成更进一步的目标，\x01",
            "『黑月』需要你的力量。\x02\x03",

            "我们会支持你的表演事业，\x01",
            "希望今后能继续保持\x01",
            "友好往来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 2)
    Return()

    # Function_23_80CE end

    def Function_24_839A(): pass

    label("Function_24_839A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83AF")
    Call(0, 22)
    Jump("loc_84AC")

    label("loc_83AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8445")

    #C0446
    ChrTalk(
        0xFE,
        (
            "……这次真是\x01",
            "十分感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "我们刚刚已经撤离了\x01",
            "古战场的隐蔽据点。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "现在已经没有\x01",
            "我们可以帮忙的事情了……\x01",
            "请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_84AC")

    label("loc_8445")


    #C0449
    ChrTalk(
        0xFE,
        (
            "我们刚刚已经撤离了\x01",
            "古战场的隐蔽据点。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "现在已经没有\x01",
            "我们可以帮忙的事情了……\x01",
            "请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84AC")

    TalkEnd(0xFE)
    Return()

    # Function_24_839A end

    def Function_25_84B0(): pass

    label("Function_25_84B0")

    TalkBegin(0xFE)

    #C0451
    ChrTalk(
        0xFE,
        "我们全家今天一起一起来外面吃饭。\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "呵呵，大家过得开心，\x01",
            "比什么都重要啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_84B0 end

    def Function_26_8508(): pass

    label("Function_26_8508")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8598")

    #C0453
    ChrTalk(
        0xFE,
        "（狼吞虎咽）……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "这汤面的味道真是\x01",
            "很辣很刺激。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        (
            "我有生以来第一次\x01",
            "在吃东西时流这么多汗……\x01",
            "不过味道真是棒啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_85DE")

    label("loc_8598")


    #C0456
    ChrTalk(
        0xFE,
        (
            "我非常喜欢\x01",
            "这道汤面。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "虽然辣得我大汗淋漓，\x01",
            "但味道真是很棒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85DE")

    TalkEnd(0xFE)
    Return()

    # Function_26_8508 end

    def Function_27_85E2(): pass

    label("Function_27_85E2")

    TalkBegin(0xFE)

    #C0458
    ChrTalk(
        0xFE,
        (
            "我们全家今天一起\x01",
            "来外面吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……\x01",
            "这道『麻婆豆腐』\x01",
            "的味道真是绝妙无比啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_85E2 end

    def Function_28_8646(): pass

    label("Function_28_8646")

    TalkBegin(0xFE)

    #C0460
    ChrTalk(
        0xFE,
        "喵……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_8646 end

    def Function_29_8659(): pass

    label("Function_29_8659")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A27")

    #C0461
    ChrTalk(
        0x20,
        (
            "呼，虽然这样说有些对不住提马斯先生，\x01",
            "但还是这里的料理最美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x20,
        (
            "（大吃大嚼）……\x01",
            "好，再加碗饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#00005F啊，克洛斯贝尔的警备队员\x01",
            "竟然在这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x109,
        (
            "#10100F这不是……\x01",
            "阿雷库瑟队员吗。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_87D4")
    Jump("loc_881E")

    label("loc_87D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87F4")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_881E")

    label("loc_87F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8814")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_881E")

    label("loc_8814")

    OP_52(0x20, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_881E")

    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x20, 0x10)

    #C0465
    ChrTalk(
        0x20,
        (
            "呀，诺艾尔上士，\x01",
            "真是巧遇啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x20,
        (
            "现在是休息时间，\x01",
            "我想放松一下，\x01",
            "就来这里吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x109,
        (
            "#10106F你还是老样子呢。\x01",
            "为了吃午饭，竟然在下雨天\x01",
            "特意从唐古拉姆门跑到这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x105,
        (
            "#10300F唐古拉姆门……\x01",
            "就是位于东克洛斯贝尔街道\x01",
            "尽头的那个边境大门吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x102,
        (
            "#00100F嗯，那是克洛斯贝尔的重要\x01",
            "守备地点，有警备队严加守卫。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x20,
        (
            "最近有新的副司令前来赴任，\x01",
            "又开始忙碌起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x20,
        (
            "诺艾尔上士，你们好像也很辛苦啊，\x01",
            "请继续加油吧。\x01",
            "唐古拉姆门的各位都会支持你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x109,
        "#10109F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 6)
    ClearChrFlags(0x20, 0x10)
    Jump("loc_8B58")

    label("loc_8A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AE2")

    #C0473
    ChrTalk(
        0x20,
        (
            "最近有新的副司令前来赴任，\x01",
            "警备队又开始忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x20,
        (
            "那个新的副司令\x01",
            "的严厉程度不逊于\x01",
            "索妮亚司令……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x20,
        (
            "我偶尔也得放松一下，\x01",
            "到市里来换换口味，\x01",
            "这样才能提起精神啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_8B58")

    label("loc_8AE2")


    #C0476
    ChrTalk(
        0x20,
        (
            "那个新的副司令\x01",
            "的严厉程度不逊于\x01",
            "索妮亚司令……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x20,
        (
            "我偶尔也得放松一下，\x01",
            "到市里来换换口味，\x01",
            "这样才能提起精神啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B58")

    TalkEnd(0xFE)
    Return()

    # Function_29_8659 end

    def Function_30_8B5C(): pass

    label("Function_30_8B5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8BB7")

    #C0478
    ChrTalk(
        0xFE,
        (
            "难得来旅行，\x01",
            "竟然下雨了。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xFE,
        (
            "虽然不是很大的雨，\x01",
            "但还是有一些冷呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BEE")

    label("loc_8BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8BEE")

    #C0480
    ChrTalk(
        0xFE,
        "嗯，好吃好吃。\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        "东方料理果然最美味。\x02",
    )

    CloseMessageWindow()

    label("loc_8BEE")

    TalkEnd(0xFE)
    Return()

    # Function_30_8B5C end

    def Function_31_8BF2(): pass

    label("Function_31_8BF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8C34")

    #C0482
    ChrTalk(
        0xFE,
        "来，老头子。\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "吃一些热的，\x01",
            "暖暖身子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C60")

    label("loc_8C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8C60")

    #C0484
    ChrTalk(
        0xFE,
        (
            "还是故乡的料理\x01",
            "最合我的口味。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C60")

    TalkEnd(0xFE)
    Return()

    # Function_31_8BF2 end

    def Function_32_8C64(): pass

    label("Function_32_8C64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8CDA")

    #C0485
    ChrTalk(
        0xFE,
        (
            "（翻书……）\x01",
            "嗯嗯……嗯嗯……\x01",
            "这本观光向导册上说……\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔有很多\x01",
            "景色优美的好地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DC9")

    label("loc_8CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8D53")

    #C0487
    ChrTalk(
        0xFE,
        (
            "（狼吞虎咽……）\x01",
            "（嗞溜嗞溜）……好喝好喝。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "住在这里的那些记者，\x01",
            "一大早就出去取材了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DC9")

    label("loc_8D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8DC9")

    #C0489
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……克洛斯贝尔\x01",
            "果然是个热闹又富裕\x01",
            "的好地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "再加上通商会议的影响，\x01",
            "街上的气氛真是热烈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DC9")

    TalkEnd(0xFE)
    Return()

    # Function_32_8C64 end

    def Function_33_8DCD(): pass

    label("Function_33_8DCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E1E")

    #C0491
    ChrTalk(
        0xFE,
        "老公，老公。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "不要一边吃饭\x01",
            "一边看书，\x01",
            "这样太没修养了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EB5")

    label("loc_8E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8E6D")

    #C0493
    ChrTalk(
        0xFE,
        "老公，老公。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "吃东西时嘴里不要出声啊，\x01",
            "这样太没修养了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EB5")

    label("loc_8E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8EB5")

    #C0495
    ChrTalk(
        0xFE,
        "老公，老公。\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "不要一边吃饭一边说话，\x01",
            "这样太没修养了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EB5")

    TalkEnd(0xFE)
    Return()

    # Function_33_8DCD end

    def Function_34_8EB9(): pass

    label("Function_34_8EB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F94")

    #C0497
    ChrTalk(
        0xFE,
        (
            "听说飞船过了今天\x01",
            "就不运营了。\x01",
            "没办法，只能回利贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        (
            "在如此状况下，本来还打算\x01",
            "再取材一段时间的……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "……希望克洛斯贝尔\x01",
            "能维持稳定啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        (
            "总之，就期待\x01",
            "国防军的活跃表现吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8FDE")

    label("loc_8F94")


    #C0501
    ChrTalk(
        0xFE,
        (
            "希望克洛斯贝尔\x01",
            "能维持稳定啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        (
            "总之，就期待\x01",
            "国防军的活跃表现吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FDE")

    Jump("loc_93A3")

    label("loc_8FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FFE")
    Call(0, 45)
    Jump("loc_9001")

    label("loc_8FFE")

    Call(0, 46)

    label("loc_9001")

    Jump("loc_93A3")

    label("loc_9006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9288")

    #C0503
    ChrTalk(
        0xFE,
        (
            "啊，这不是特别任务支援科\x01",
            "的各位吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        "#00005F啊，您是利贝尔通讯社的……\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x102,
        (
            "#00100F您又来克洛斯\x01",
            "贝尔了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "呵呵，通商会议结束之后，\x01",
            "我一直都没有回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        (
            "毕竟独立提案\x01",
            "算是轰动性的\x01",
            "大新闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "所以我接到了紧急命令，\x01",
            "要留在这里进行长期取材，\x01",
            "直到居民投票结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        "#00104F原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        (
            "机会难得，\x01",
            "我准备去观赏\x01",
            "彩虹剧团的新版舞剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        "而且是在公演第一天哦。\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x109,
        (
            "#10105F公演第一天……\x01",
            "竟然能得到那天的门票啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x103,
        (
            "#00200F听说第一天的门票被争抢得很凶，\x01",
            "价格也一直在不断炒高。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        (
            "呵呵，身为记者，\x01",
            "总得有点小手段嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "总之，情况就是这样，\x01",
            "如果以后在市里再次见面，\x01",
            "还请多关照哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 0)
    Jump("loc_9324")

    label("loc_9288")


    #C0516
    ChrTalk(
        0xFE,
        (
            "观赏过彩虹剧团的新版舞剧，\x01",
            "并见证居民投票之后，\x01",
            "我在克洛斯贝尔的采访任务也就结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xFE,
        (
            "总之，情况就是这样，\x01",
            "如果以后在市里再次见面，\x01",
            "还请多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9324")

    Jump("loc_93A3")

    label("loc_9329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_93A3")

    #C0518
    ChrTalk(
        0xFE,
        (
            "呵呵，这家店的料理很美味，\x01",
            "一点都不逊于东方人街的店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "奈尔他们现在\x01",
            "说不定也在吃着\x01",
            "美味的东方料理吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93A3")

    TalkEnd(0xFE)
    Return()

    # Function_34_8EB9 end

    def Function_35_93A7(): pass

    label("Function_35_93A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93B9")
    Call(0, 37)
    Jump("loc_9438")

    label("loc_93B9")

    TalkBegin(0xFE)

    #C0520
    ChrTalk(
        0x17,
        (
            "#02109F好，吃过饭之后，\x01",
            "就去街上取材吧～\x02\x03",

            "#02104F首脑们的安保措施虽然强大，\x01",
            "但在他们移动途中，\x01",
            "说不定会有机会的～¤\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_9438")

    Return()

    # Function_35_93A7 end

    def Function_36_9439(): pass

    label("Function_36_9439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944B")
    Call(0, 37)
    Jump("loc_94BE")

    label("loc_944B")

    TalkBegin(0xFE)

    #C0521
    ChrTalk(
        0xFE,
        (
            "按照预定，从下午开始，\x01",
            "主要就是在街头\x01",
            "采访市民了。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "运气好的话，说不定能在\x01",
            "哪里拍到首脑们的照片呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_94BE")

    Return()

    # Function_36_9439 end

    def Function_37_94BF(): pass

    label("Function_37_94BF")

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
        "#6P哦，支援科的各位。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x17, 0x2)
    Sleep(200)

    #C0524
    ChrTalk(
        0x17,
        (
            "#12P#02100F罗伊德，你们也是\x01",
            "来这里吃饭的吗？\x02\x03",

            "#02109F呵呵，先不说这个了，\x01",
            "揭幕式真是精彩啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        "#00000F嗯，确实很震撼呢。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#00104F各国首脑的气场\x01",
            "极具压迫力。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x17,
        (
            "#12P#02106F对吧对吧～\x01",
            "特别是『铁血宰相』，\x01",
            "存在感真是非同小可～！\x02\x03",

            "#02100F我还是第一次在那么\x01",
            "近的距离下见到他，\x01",
            "真是彻底感受到他的强大了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0528
    ChrTalk(
        0x17,
        (
            "#12P#02105F对了，说起来，\x01",
            "站在宰相旁边的那个\x01",
            "书记官打扮的男性……\x02\x03",

            "#02103F就是以前曾经\x01",
            "来过克洛斯贝尔，\x01",
            "名叫雷克特的那个孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        "#00005F哎，这个……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x17,
        (
            "#12P#02104F呵呵，我知道\x01",
            "你们不方便回答。\x02\x03",

            "#02101F其实我想起了\x01",
            "一件很重要的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0531
    ChrTalk(
        0x101,
        "#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x109,
        "#10105F那是……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x17,
        (
            "#12P#02103F……在去年春季，\x01",
            "铁血宰相和哈尔特曼议长\x01",
            "曾经进行过一次非正式的秘密会谈……\x02\x03",

            "#02100F罗伊德，你们当然也\x01",
            "知道这件事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        "#00005F嗯，是啊……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x102,
        (
            "#00103F对情报灵通的人士来说，\x01",
            "这是公开的秘密了。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x17,
        (
            "#12P#02103F嗯……\x01",
            "但当时的情况却并非如此。\x02\x03",

            "克洛斯贝尔的媒体自不必说，\x01",
            "连帝国的媒体也没有得到任何消息……\x02\x03",

            "#02101F当然，克洛斯贝尔警察局\x01",
            "对此情况也没有丝毫掌握。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x18,
        (
            "#6P……另外，铁血宰相这种\x01",
            "重要人物的身边\x01",
            "却几乎没有护卫人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x18,
        (
            "#6P简直就像在散步途中，\x01",
            "顺便过来逛逛而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x18,
        (
            "#6P……可以说也正因如此，\x01",
            "反而没有让任何组织机构得到消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x105,
        "#10303F唔……真是不得了啊。\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        "#00301F是啊，简直让人难以置信。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x17,
        (
            "#12P#02106F没错，难以置信，\x01",
            "而且很不甘心！\x02\x03",

            "#02100F所以我之后想尽一切办法，\x01",
            "展开了大量调查。\x02\x03",

            "#02103F最后查到了数名\x01",
            "与会谈的安排工作\x01",
            "有所牵连的人物……\x02\x03",

            "#02101F我正是想起了那其中\x01",
            "有一名男性的名字是雷克特。\x02",
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
            "#00005F我们也知道\x01",
            "他当时和宰相一起\x01",
            "参加了会谈……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#00101F但没想连会谈的安排工作\x01",
            "都是由雷克特先生负责的……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x109,
        (
            "#10106F该怎么说呢……\x01",
            "真是很厉害的反间谍技术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x17,
        (
            "#12P#02103F……不错，一个普通的书记官，\x01",
            "是不可能做到这种事的。\x02\x03",

            "#02102F除非他是著名的\x01",
            "帝国情报部的成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#00005F确、确实呢……\x02\x03",

            "#00003F（单凭一己之力就能调查到如此地步，\x01",
            "  格蕾丝小姐真是厉害呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x104,
        "#00306F（嗯，很强大的执念啊。）\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x17,
        (
            "#12P#02109F看你们的表情，似乎是说中了呢。\x02\x03",

            "#02106F呼，不过之前真是\x01",
            "完全没想到那个孩子\x01",
            "就是那个雷克特啊～\x02\x03",

            "#02102F好啦，我知道你们也有\x01",
            "自己的立场，\x01",
            "就不多问什么了……\x02\x03",

            "#02100F总之，那个叫雷克特的孩子\x01",
            "绝不是寻常之辈。\x02\x03",

            "罗伊德，你们以后如果\x01",
            "与他有所牵连，\x01",
            "一定要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        "#00000F嗯，我一定牢记在心。\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#00100F谢谢您的情报。\x02",
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

    # Function_37_94BF end

    def Function_38_9F0F(): pass

    label("Function_38_9F0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A01D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FB1")

    #C0552
    ChrTalk(
        0xFE,
        (
            "我和老公吵架，\x01",
            "然后离家出走……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "结果他昨天终于哭着\x01",
            "来向我道歉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "唔、唔……\x01",
            "他做到这种地步，\x01",
            "我反而有些罪恶感了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A018")

    label("loc_9FB1")


    #C0555
    ChrTalk(
        0xFE,
        (
            "呼，算啦，反正离家出走这么久，\x01",
            "我也有点腻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "而且好像发生了\x01",
            "什么事件……\x01",
            "差不多也该回家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A018")

    Jump("loc_A19D")

    label("loc_A01D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A097")

    #C0557
    ChrTalk(
        0xFE,
        (
            "我和老公吵架之后离家出走，\x01",
            "他找到了我，还要我回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        (
            "哼，那种道歉方式是不行的，\x01",
            "根本感觉不到诚意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19D")

    label("loc_A097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A0F6")

    #C0559
    ChrTalk(
        0xFE,
        (
            "服务员又换回\x01",
            "平时那个女孩了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        (
            "刚才那个\x01",
            "做事不利落的\x01",
            "服务员去哪里了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19D")

    label("loc_A0F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A146")

    #C0561
    ChrTalk(
        0xFE,
        (
            "那个服务员做事情\x01",
            "真是不利落啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "快点把菜给我\x01",
            "端上来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19D")

    label("loc_A146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A19D")

    #C0563
    ChrTalk(
        0xFE,
        (
            "我和老公吵架，\x01",
            "离家出走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "哼……\x01",
            "除非他过来道歉，不然我绝不原谅。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19D")

    TalkEnd(0xFE)
    Return()

    # Function_38_9F0F end

    def Function_39_A1A1(): pass

    label("Function_39_A1A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A1E9")

    #C0565
    ChrTalk(
        0xFE,
        (
            "啊啊，我在姥姥家\x01",
            "已经住腻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        "好想见爸爸啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2DE")

    label("loc_A1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A212")

    #C0567
    ChrTalk(
        0xFE,
        (
            "爸爸还不\x01",
            "过来吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2DE")

    label("loc_A212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A245")

    #C0568
    ChrTalk(
        0xFE,
        (
            "（大吃大嚼）……\x01",
            "嘿嘿，真好吃！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2DE")

    label("loc_A245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A282")

    #C0569
    ChrTalk(
        0xFE,
        (
            "妈妈，这桌子\x01",
            "好脏啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        "店员忘擦了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2DE")

    label("loc_A282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A2DE")

    #C0571
    ChrTalk(
        0xFE,
        "我和妈妈一起来姥姥家玩，\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "妈妈说爸爸过一阵子再过来。\x01",
            "因为他的工作太忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2DE")

    TalkEnd(0xFE)
    Return()

    # Function_39_A1A1 end

    def Function_40_A2E2(): pass

    label("Function_40_A2E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4C2")

    #C0573
    ChrTalk(
        0x1D,
        (
            "#04405F啊……各位，竟在这里\x01",
            "遇到你们，真是巧遇啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        (
            "#00005F那个……\x01",
            "你正在吃饭啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x1D,
        (
            "#04400F嗯，现在是休息时间，\x01",
            "所以过来吃个午饭。\x02\x03",

            "#04403F这家店的炒饭\x01",
            "真是让人回味无穷。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，莉丝小姐\x01",
            "还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x109,
        "#10109F看、看起来的确很好吃，可是这……\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x104,
        (
            "#00303F（桌子上的盘子已经\x01",
            "  积起了很厚一叠了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x105,
        (
            "#10304F（呵呵，\x01",
            "  龙老饭店和修女……\x01",
            "  真是很不协调啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x103,
        (
            "#00200F（艾莉前辈完全没有\x01",
            "  吃惊的表情，\x01",
            "  难道她平时就……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 3)
    Jump("loc_A50F")

    label("loc_A4C2")


    #C0581
    ChrTalk(
        0x1D,
        (
            "#04400F再过一会，我就要\x01",
            "回大圣堂了。\x02\x03",

            "如果有什么事情，\x01",
            "可以去那里找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50F")

    TalkEnd(0xFE)
    Return()

    # Function_40_A2E2 end

    def Function_41_A513(): pass

    label("Function_41_A513")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A2, 3)), scpexpr(EXPR_END)), "loc_A57F")

    #C0582
    ChrTalk(
        0xFE,
        (
            "为了让城市复兴，\x01",
            "我参加了很多志愿活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        (
            "流过汗水之后再吃饭，\x01",
            "真是格外美味啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A2, 3)
    Jump("loc_A5C5")

    label("loc_A57F")


    #C0584
    ChrTalk(
        0xFE,
        (
            "旧城区的重建工作\x01",
            "还在持续中……\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "我似乎也有\x01",
            "不少事情应该做。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5C5")

    TalkEnd(0xFE)
    Return()

    # Function_41_A513 end

    def Function_42_A5C9(): pass

    label("Function_42_A5C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A66B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5FB")
    Call(0, 54)
    Return()

    label("loc_A5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_A666")

    #C0586
    ChrTalk(
        0xFE,
        (
            "哎呀，这样一来，\x01",
            "说不定就可以见到父亲了！\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "总之，一切都交给你们了。\x01",
            "请务必帮我找到父亲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A666")

    Jump("loc_A6A4")

    label("loc_A66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A6A4")

    #C0588
    ChrTalk(
        0xFE,
        (
            "艾娅莉，阿尔米……\x01",
            "昨天真是美好\x01",
            "的一天啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6A4")

    TalkEnd(0xFE)
    Return()

    # Function_42_A5C9 end

    def Function_43_A6A8(): pass

    label("Function_43_A6A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A74B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6DA")
    Call(0, 54)
    Return()

    label("loc_A6DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_A746")

    #C0589
    ChrTalk(
        0xFE,
        (
            "我们一定能见到\x01",
            "阿鲁姆的父亲。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        (
            "必须要让他亲手抱抱\x01",
            "我们的爱情结晶阿尔米。\x02",
        )
    )

    CloseMessageWindow()

    #N0591
    NpcTalk(
        0xFE,
        "婴儿",
        "呼呼。\x02",
    )

    CloseMessageWindow()

    label("loc_A746")

    Jump("loc_A791")

    label("loc_A74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A791")

    #C0592
    ChrTalk(
        0xFE,
        (
            "嗯，阿鲁姆……\x01",
            "昨天真是美好\x01",
            "的一天啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0593
    NpcTalk(
        0xFE,
        "婴儿",
        "呼呼¤\x02",
    )

    CloseMessageWindow()

    label("loc_A791")

    TalkEnd(0xFE)
    Return()

    # Function_43_A6A8 end

    def Function_44_A795(): pass

    label("Function_44_A795")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7AA")
    Call(0, 45)
    Jump("loc_A7AD")

    label("loc_A7AA")

    Call(0, 46)

    label("loc_A7AD")

    TalkEnd(0xFE)
    Return()

    # Function_44_A795 end

    def Function_45_A7B1(): pass

    label("Function_45_A7B1")


    #C0594
    ChrTalk(
        0x27,
        (
            "原来如此，你这段时间\x01",
            "一直住在龙老饭店啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x27,
        (
            "这里的饭菜非常美味，\x01",
            "你肯定住得很舒适吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x16,
        (
            "嗯，但是我拼命\x01",
            "忍着别吃得太多，\x01",
            "也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x16,
        (
            "您今天竟然还特地过来，\x01",
            "真是让人不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x16,
        (
            "本来应该由我\x01",
            "去拜访您才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x27,
        "呵呵，请不必在意。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x27,
        (
            "到处散步闲逛\x01",
            "是我的爱好。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x16,
        "呵呵，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x16,
        (
            "真不愧是天下闻名\x01",
            "的自由记者啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Return()

    # Function_45_A7B1 end

    def Function_46_A907(): pass

    label("Function_46_A907")


    #C0603
    ChrTalk(
        0x16,
        (
            "话说回来，尼尔森先生，\x01",
            "您这次在克洛斯贝尔\x01",
            "住了很长时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x16,
        (
            "想必是因为很在意\x01",
            "故乡的情况吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x27,
        (
            "是啊，该怎么说呢，\x01",
            "就是想亲自感受\x01",
            "这里的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x27,
        (
            "总之，我还要在克洛斯贝尔\x01",
            "暂居一段时间。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_46_A907 end

    def Function_47_A9D0(): pass

    label("Function_47_A9D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9E5")
    Call(0, 48)
    Jump("loc_AA81")

    label("loc_A9E5")


    #C0607
    ChrTalk(
        0x1C,
        (
            "#01803F居住在共和国时，\x01",
            "由于父亲的工作原因，\x01",
            "我总是不断搬家……\x02\x03",

            "#01802F呵呵，我真是很感谢\x01",
            "桑桑呢。\x02\x03",

            "与大家和伊莉娅小姐他们的情谊，\x01",
            "我也会倍加珍惜的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA81")

    TalkEnd(0xFE)
    Return()

    # Function_47_A9D0 end

    def Function_48_AA85(): pass

    label("Function_48_AA85")

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
            "#01802F啊……\x01",
            "各位，你们好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        "#12P#00100F呵呵，你好啊，莉夏小姐。\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        "#12P#00000F今天来这里吃饭了啊？\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x1C,
        (
            "#01802F呵呵，是的。\x02\x03",

            "现在正在吃饭后甜点，\x01",
            "顺便和桑桑聊聊天。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xA,
        (
            "#11P你们好像是\x01",
            "警察吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xA,
        (
            "#11P真是的～竟然破坏我和莉夏\x01",
            "难得的女生独处时间～\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x104,
        "#6P#00302F哈哈，真不好意思啊。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x109,
        (
            "#12P#10100F话说回来，能见到\x01",
            "艺人的私人生活，\x01",
            "真是很难得呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x105,
        (
            "#6P#10304F的确，\x01",
            "一般来说，很难了解到\x01",
            "名人的交友关系呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x1C,
        (
            "#01809F啊哈哈……\x01",
            "哪里的话，我只是个新人而已。\x02\x03",

            "#01802F我在休息日只知道闷在家里，\x01",
            "多亏桑桑经常拉我出来玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xA,
        "#11P呵呵，因为我们同岁，所以很聊得来嘛～\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xA,
        (
            "#11P而且拉着莉夏逛商场，\x01",
            "寻找合她身的可爱衣服也很有乐趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x1C,
        (
            "#01809F啊哈哈，不过很少能发现\x01",
            "合适的可爱衣服呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x102,
        (
            "#12P#00103F（唔，的确，以莉夏小姐的身材来说，\x01",
            "  很难找到尺寸合适的衣服吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x103,
        "#12P#00203F（……这就是过大的烦恼吧。）\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        "#12P#00002F哈哈，你们的关系真是不错啊。\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x1C,
        (
            "#01802F呵呵，我真的很感谢\x01",
            "桑桑呢。\x02\x03",

            "#01803F居住在共和国时，\x01",
            "由于父亲的工作原因，\x01",
            "我总是不断搬家……\x02\x03",

            "#01808F所以很难交到\x01",
            "好朋友，\x01",
            "总是独自一人。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x104,
        "#6P#00303F是吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x1C, 500)

    #C0626
    ChrTalk(
        0xA,
        "#11P呵呵，放心吧，莉夏。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x1)

    #C0627
    ChrTalk(
        0xA,
        (
            "#11P有我和你做朋友，\x01",
            "绝不会再让你独自一人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xA,
        (
            "#11P莉夏，我们永远都是朋友，\x01",
            "直到一起进坟墓！\x02",
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
            "#01802F啊哈哈……\x01",
            "谢谢，桑桑。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，看样子，\x01",
            "我们在这里很多余啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x109,
        (
            "#12P#10102F嗯，差不多也该\x01",
            "识趣的离开了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x0)

    #C0632
    ChrTalk(
        0x1C,
        (
            "#01806F抱歉啊，各位，\x01",
            "占用了你们不少时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x101,
        (
            "#12P#00004F哪里，和你聊了聊天，\x01",
            "我们正好也放松了一下呢。\x02\x03",

            "#00002F那我们就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x1C,
        "#01802F好的，下次见。\x02",
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

    # Function_48_AA85 end

    def Function_49_B226(): pass

    label("Function_49_B226")

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

    def lambda_B2DB():
        OP_98(0x101, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2DB)
    Sleep(50)

    def lambda_B2F8():
        OP_98(0x102, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B2F8)
    Sleep(50)

    def lambda_B315():
        OP_98(0x109, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B315)
    Sleep(50)

    def lambda_B332():
        OP_98(0x105, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B332)
    OP_68(890, 1400, -390, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_0D()

    def lambda_B374():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B374)
    Sleep(50)

    def lambda_B384():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B384)
    Sleep(50)

    def lambda_B394():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B394)
    Sleep(50)

    def lambda_B3A4():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B3A4)
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
        "#12P#00001F找到了……！\x02",
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
            "#03500F原来如此……\x01",
            "要使用花山椒啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x8,
        (
            "#6P不错，无论是辣度还是口味，\x01",
            "都和普通山椒有很大区别。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x8,
        (
            "#6P这种花山椒虽然只能在东方栽培，\x01",
            "但最近已经可以通过铁路货运来订购了。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x28,
        (
            "#03502F#11P哈哈～怪不得我做的麻婆豆腐\x01",
            "总是味道不对。\x02\x03",

            "#03504F原来关键是『麻』啊……\x01",
            "学到了一些窍门呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 5010, 0, 15540, 45)

    #C0640
    ChrTalk(
        0x101,
        (
            "#00000F#N雷克特先生……\x01",
            "你在这里啊。\x02",
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

    def lambda_B69A():
        OP_98(0x101, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B69A)
    Sleep(50)

    def lambda_B6B7():
        OP_98(0x102, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B6B7)
    Sleep(50)

    def lambda_B6D4():
        OP_98(0x109, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B6D4)
    Sleep(50)

    def lambda_B6F1():
        OP_98(0x105, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B6F1)
    Sleep(50)
    OP_68(14290, 1400, 14500, 1500)
    OP_0D()

    #C0641
    ChrTalk(
        0x102,
        "#6P#00105F（轻轻松松就找到了啊……）\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x109,
        (
            "#6P#10106F（总、总觉得看起来\x01",
            "  非常散漫呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x105,
        (
            "#6P#10300F（接下来，只要确认他的身份，\x01",
            "  就算是完成使命了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x28,
        (
            "#03505F哟，你们好慢啊。\x02\x03",

            "#03509F等你们很久了，我的挚友们！\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x101,
        "#00005F哎……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x8, 500)
    Sleep(100)

    #C0646
    ChrTalk(
        0x28,
        (
            "#12P#03502F老板，这就是\x01",
            "我刚才说的那些朋友。\x02\x03",

            "#03504F他们很有干劲，而且毅力十足，\x01",
            "请不必客气，尽管训练他们吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x28, 500)
    Sleep(100)

    #C0647
    ChrTalk(
        0x8,
        "没问题，交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    #C0648
    ChrTalk(
        0x8,
        (
            "#11P一次来了四人，多少有些麻烦，\x01",
            "但东方料理可以广泛传播，我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x8,
        "#11P好，你们过来努力学习吧！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(100)

    #C0650
    ChrTalk(
        0x101,
        "#6P#00012F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x102,
        "#6P#00105F您在说什么……\x02",
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

    def lambda_B9FA():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9FA)
    Sleep(50)

    def lambda_BA0A():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BA0A)
    Sleep(50)

    def lambda_BA1A():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BA1A)
    Sleep(50)

    def lambda_BA2A():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BA2A)
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
        "#11P#00011F啊……！\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x109,
        "#5P#10105F逃、逃跑了……！\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x105,
        "#5P#10309F哈哈，还是老样子呢。\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x102,
        "#5P#00107F必、必须得赶快追上！\x02",
    )

    CloseMessageWindow()

    def lambda_BB24():
        OP_98(0x8, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BB24)
    Sound(802, 0, 100, 0)
    OP_68(13640, 1400, 14410, 1000)
    MoveCamera(37, 24, 0, 1000)

    #C0656
    ChrTalk(
        0x8,
        "喂！你们要去哪里！？\x02",
    )

    CloseMessageWindow()
    OP_6F(0x1)
    WaitChrThread(0x8, 1)

    #C0657
    ChrTalk(
        0x8,
        (
            "修行已经开始了！\x01",
            "首先从做准备工作开始练习！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BBB1():
        OP_93(0x101, 0x5A, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BBB1)
    Sleep(50)

    def lambda_BBC1():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BBC1)
    Sleep(50)

    def lambda_BBD1():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BBD1)
    Sleep(50)

    def lambda_BBE1():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BBE1)

    #C0658
    ChrTalk(
        0x101,
        "#6P#00011F不、不是啦，您误会了！\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x102,
        (
            "#6P#00106F我们是克洛斯贝尔\x01",
            "警察局的……\x02",
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
            "唔……\x01",
            "既然搞错了，那也没办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x8,
        (
            "不过这也算是缘分，\x01",
            "你们把这个带走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDFD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0662
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "龙老炒饭的食谱\x07\x00",
            "收下了。\x02",
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
            "同时",
            scpstr(SCPSTR_CODE_ITEM, '料理手册'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
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
            "#12P#00005F这……可以收下吗？\x01",
            "连手册都送给我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE76")

    label("loc_BDFD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0665
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '料理手册'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
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
            "#12P#00005F这……可以收下吗？\x01",
            "就这么免费拿走……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE76")

    AddItemNumber('料理手册', 1)

    #C0667
    ChrTalk(
        0x8,
        (
            "这只是店里剩下的，不用客气。\x01",
            "你们就努力学习吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x101,
        (
            "#12P#00003F谢谢您，\x01",
            "那、那我们就先告辞了。\x02\x03",

            "#00001F各位，赶快追！\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x102,
        "#11P#00101F嗯！\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x109,
        "#12P#10101F明白！\x02",
    )

    CloseMessageWindow()

    def lambda_BF28():
        OP_93(0x101, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF28)

    def lambda_BF35():
        OP_93(0x102, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BF35)

    def lambda_BF42():
        OP_93(0x109, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BF42)

    def lambda_BF4F():
        OP_93(0x105, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BF4F)
    WaitChrThread(0x105, 1)

    def lambda_BF60():
        OP_98(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF60)
    Sleep(50)

    def lambda_BF7D():
        OP_98(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BF7D)
    Sleep(50)

    def lambda_BF9A():
        OP_98(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BF9A)
    Sleep(50)

    def lambda_BFB7():
        OP_98(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BFB7)
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
            "※调查放置在各种场所的书籍等特定的位置，\x01",
            "  可以记住料理的『食谱』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0672
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※『食谱』会记录在『料理手册』中。\x01",
            "  只要使用『料理手册』，\x01",
            "  随时都可以制作各种效果各异的料理。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0673
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※另外，还有一定几率做出\x01",
            "  『大成功料理』、『预想外料理』等变化型料理。\x01",
            "  （制作料理时，有时也会『失败』。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0674
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※至于在制作料理时所需的『食材』，\x01",
            "  可以在杂货店等商店购买。\x01",
            "  另外，魔兽有时也会掉落食材。\x07\x00\x02",
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

    # Function_49_B226 end

    def Function_50_C191(): pass

    label("Function_50_C191")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_C34F")
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

    def lambda_C283():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_C283)

    def lambda_C294():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C294)

    def lambda_C2AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C2AE)

    def lambda_C2BF():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C2BF)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_C2F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C2F6)

    def lambda_C307():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C307)
    Sleep(200)

    def lambda_C324():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C324)

    def lambda_C335():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C335)
    Jump("loc_C5FE")

    label("loc_C34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_C4A9")
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

    def lambda_C3DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_C3DD)

    def lambda_C3EE():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C3EE)

    def lambda_C408():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C408)

    def lambda_C419():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C419)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_C450():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C450)

    def lambda_C461():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C461)
    Sleep(200)

    def lambda_C47E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C47E)

    def lambda_C48F():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C48F)
    Jump("loc_C5FE")

    label("loc_C4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_C5FE")
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

    def lambda_C537():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_C537)

    def lambda_C548():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C548)

    def lambda_C562():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C562)

    def lambda_C573():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C573)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_C5AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C5AA)

    def lambda_C5BB():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5BB)
    Sleep(200)

    def lambda_C5D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C5D8)

    def lambda_C5E9():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C5E9)

    label("loc_C5FE")

    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    #C0675
    ChrTalk(
        0x1A2,
        (
            "『龙老饭店』……\x01",
            "是……东街的东方料理店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x101,
        "#00002F要进去稍微休息一下吗？\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x1A2,
        (
            "嗯，也好。\x01",
            "正好有点饿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x1A2,
        (
            "就进去坐坐，看看这家店\x01",
            "会端出什么样的料理吧。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_C80F")
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
    Jump("loc_C916")

    label("loc_C80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_C895")
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
    Jump("loc_C916")

    label("loc_C895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_C916")
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

    label("loc_C916")

    FadeToBright(1000, 0)
    OP_0D()

    #C0679
    ChrTalk(
        0x102,
        "#11P#00102F怎么样？龙老饭店的料理如何？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_C994")

    #C0680
    ChrTalk(
        0x104,
        (
            "#6P#00309F对啊，一定得让我们听听\x01",
            "正宗东方人的意见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1F")

    label("loc_C994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_C9DB")

    #C0681
    ChrTalk(
        0x109,
        (
            "#6P#10109F对啊，一定得让我们听听\x01",
            "正宗东方人的意见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1F")

    label("loc_C9DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CA1F")

    #C0682
    ChrTalk(
        0x105,
        (
            "#6P#10302F对啊，一定得让我们听听\x01",
            "正宗东方人的意见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA1F")

    BeginChrThread(0x1A2, 3, 0, 51)
    Sleep(1000)
    EndChrThread(0x1A2, 0x3)

    #C0683
    ChrTalk(
        0x1A2,
        (
            "#5P唔——\x01",
            "这到底是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x1A2,
        (
            "#5P这家店为什么会给\x01",
            "这种料理定出这样的价格？\x01",
            "店主究竟在想什么！？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#12P#00006F喂喂，不要那么大声\x01",
            "说人家的坏话……\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        "#11P#00100F不，秦的意思应该是……\x02",
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x1A2,
        (
            "#5P比如这道麻婆豆腐……\x01",
            "味道完全不比东方人街那些\x01",
            "三星高级餐厅的差。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x1A2,
        (
            "#5P这么美味的料理，完全应该卖三倍的价格——\x01",
            "老板为什么没那样做！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CBB9")

    #C0689
    ChrTalk(
        0x104,
        "#6P#00306F原、原来是这个意思啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC1C")

    label("loc_CBB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CBEB")

    #C0690
    ChrTalk(
        0x109,
        "#6P#10106F原来是这个意思啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC1C")

    label("loc_CBEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CC1C")

    #C0691
    ChrTalk(
        0x105,
        "#6P#10304F呵呵，原来是这个意思啊。\x02",
    )

    CloseMessageWindow()

    label("loc_CC1C")


    #C0692
    ChrTalk(
        0x1A2,
        (
            "#5P不、不可能……\x01",
            "克洛斯贝尔竟然有这样的店……\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        (
            "#12P#00009F哈哈，不管怎么说，\x01",
            "只要你满意就好。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 1)
    OP_29(0x73, 0x1, 0x9)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CCE4")
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
    Jump("loc_CD63")

    label("loc_CCE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CD26")
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
    Jump("loc_CD63")

    label("loc_CD26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CD63")
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

    label("loc_CD63")

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

    # Function_50_C191 end

    def Function_51_CD9E(): pass

    label("Function_51_CD9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDCE")

    def lambda_CDAE():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CDAE)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_51_CD9E")

    label("loc_CDCE")

    Return()

    # Function_51_CD9E end

    def Function_52_CDCF(): pass

    label("Function_52_CDCF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CEF2")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_CF35")

    label("loc_CEF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CF0A")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_CF35")

    label("loc_CF0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CF22")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Jump("loc_CF35")

    label("loc_CF22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF35")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_CF35")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D042")

    #C0694
    ChrTalk(
        0x8,
        (
            "喂！你在干什么！\x01",
            "怎么又把饭炒糊了！\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0xC,
        "哇、哇哇！对不起！\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x101,
        "#00000F那个……打扰一下可以吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0697
    ChrTalk(
        0x8,
        "嗯……找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x8,
        (
            "如你所见，我现在很忙。\x01",
            "如果想点菜，请去柜台点。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#00000F哦，并不是点菜。\x01",
            "其实……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0B5")

    label("loc_D042")

    TurnDirection(0x8, 0x101, 500)

    #C0700
    ChrTalk(
        0x8,
        "哦，找我有什么事？\x02",
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        "如果想点菜，请去柜台点。\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#00000F不好意思，\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0B5")

    SetChrName("")

    #A0703
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将『美食向导』取材一事的\x01",
            "情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0704
    ChrTalk(
        0x8,
        (
            "哦，就是那个美食介绍活动啊。\x01",
            "杂志社确实已经和我打过招呼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x8,
        (
            "唔，虽然很忙，但也没办法了。\x01",
            "你们找个空座位等着吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "我让你们尝尝我引以为傲的\x01",
            "『天下一品炒饭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x104,
        "#00309F噢噢，那可真让人期待。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0708
    ChrTalk(
        0x101,
        "#00000F那好，我们先就坐吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x8, 5440, 0, 9730, 225)
    SetChrPos(0x101, 3230, 100, 8960, 180)
    SetChrPos(0x103, 1720, 100, 8710, 135)
    SetChrPos(0x102, 1600, 50, 7150, 90)
    SetChrPos(0x104, 3290, 100, 5440, 0)
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
            "罗伊德等人品尝了天下一品炒饭。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0710
    ChrTalk(
        0x103,
        "#00204F……真是美味。\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x104,
        (
            "#00309F哎呀呀，老板的手艺\x01",
            "果然名不虚传。\x02\x03",

            "#00304F如此美味的顶级炒饭，\x01",
            "也只有在龙老饭店\x01",
            "才能吃到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x8,
        "哼哼，那当然。\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x8,
        (
            "炒饭一直都是我的擅长料理……\x01",
            "前一阵子又做了进一步的改良，\x01",
            "不好吃才怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x109,
        (
            "#10102F（狼吞虎咽）……\x01",
            "嗯，确实……！\x02\x03",

            "#10103F只是最简单的料理，\x01",
            "竟然能炒出如此浓厚的味道！\x02\x03",

            "#10109F我在警备队的宿舍\x01",
            "也炒过几次饭，\x01",
            "但专业厨师炒的就是不一样啊……！\x02",
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
        "#00306F不要边吃边说嘛。\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x105,
        (
            "#10302F哎呀呀，真是\x01",
            "狼吞虎咽呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)

    #C0717
    ChrTalk(
        0x8,
        (
            "唔，能让你\x01",
            "如此满意，\x01",
            "我也算没白做啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x8,
        (
            "既然如此，要不要\x01",
            "再添一份呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(100)

    #C0719
    ChrTalk(
        0x109,
        "#10109F好的！请务必给我添一份！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0720
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，诺艾尔小姐可真是的……\x01",
            "简直就像个发育期的男孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x101,
        (
            "#00000F嗯，她好像相当喜欢呢……\x01",
            "这里的报道就交给诺艾尔来写吧。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D892")
    SetChrPos(0x8, 17080, 0, 15430, 0)
    BeginChrThread(0x8, 0, 0, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_D8A3")

    label("loc_D892")

    SetChrPos(0x8, 16000, 0, 15990, 0)

    label("loc_D8A3")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_D950")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_D96D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_D980")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_D993")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_D9B0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_D9C3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D9C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_D9E0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_D9F3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_DA10")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_DA23")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_DA40")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA40")

    OP_29(0x80, 0x1, 0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB15")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0722
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在六家饮食店完成了取材！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DB0C")

    #A0723
    AnonymousTalk(
        0x101,
        (
            "#00003F现在就可以去向\x01",
            "格蕾丝小姐报告了……\x02\x03",

            "#00000F不过，还没有把六个人\x01",
            "喜欢的美食全部找到。\x01",
            "不如再努努力吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DB0C")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_DB15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DBD8")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0724
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了特别任务支援科\x01",
            "全体成员各自喜欢的美食。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0725
    AnonymousTalk(
        0x101,
        (
            "#00000F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_DBD8")

    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DBF8")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_DC3B")

    label("loc_DBF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DC10")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_DC3B")

    label("loc_DC10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DC28")
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Jump("loc_DC3B")

    label("loc_DC28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DC3B")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_DC3B")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2880, 0, -40, 278)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_CDCF end

    def Function_53_DC67(): pass

    label("Function_53_DC67")

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
        "唉……\x02",
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x105,
        (
            "#10300F（职业女性选秀活动\x01",
            "  中的『服务员』……\x01",
            "  让她来担当应该很不错吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x101,
        (
            "#00003F（看起来，她好像\x01",
            "  很没精神……\x01",
            "  不过还是问问看吧。）\x02\x03",

            "#00000F那个……有点事情\x01",
            "想和你商量……可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0xA,
        "……什么事？\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0730
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人邀请对方参加\x01",
            "慈善宴会中的职业女性选秀活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0731
    ChrTalk(
        0xA,
        "哦，那个活动啊……\x02",
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xA,
        (
            "之前洛依来邀请过我，\x01",
            "我已经拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xA,
        (
            "莉夏现在行踪不明，\x01",
            "我实在没心情参加那种活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x103,
        "#00203F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x102,
        (
            "#00108F既然如此，\x01",
            "那就不勉强你参加了。\x02",
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
            "#00300F嗯……\x01",
            "看起来，你好像\x01",
            "还在犹豫吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xA,
        "嗯……\x02",
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xA,
        (
            "因为我一直无精打采，\x01",
            "已经把负面情绪传染给了\x01",
            "来店的客人们。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xA,
        (
            "如果我总是这副样子，\x01",
            "客人们也不会开心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，既然心存犹豫，\x01",
            "何不过去试试看呢？\x02\x03",

            "#10300F要是今后可能因为\x01",
            "放弃这次机会而感到后悔，\x01",
            "那我认为还是去参加为好。\x02",
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
        "……嗯，我决定了。\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xA,
        (
            "还是应该努力\x01",
            "为活动贡献一份力量！\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "女性选秀也好，泡开水澡也好，\x01",
            "尽管放马过来吧！\x02",
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
        "#10106F泡开水澡……\x02",
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x101,
        (
            "#00012F那个……这么说，\x01",
            "你同意参加了？\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0xA,
        "嗯，没问题！\x02",
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xA,
        (
            "我会在活动\x01",
            "开始前赶到的，\x01",
            "稍后再联系吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        "#00000F嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E2AC")

    #C0750
    ChrTalk(
        0x101,
        (
            "#00003F好，我们总算\x01",
            "把参选者找齐了。\x02\x03",

            "#00000F我们这就去市民会馆，\x01",
            "向洛依先生他们报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_E2AC")

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

    # Function_53_DC67 end

    def Function_54_E2FA(): pass

    label("Function_54_E2FA")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9C1")
    OP_93(0x1E, 0x5A, 0x0)
    OP_93(0x1F, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0751
    NpcTalk(
        0x1F,
        "婴儿",
        "呼，呼……\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x1F,
        "乖哦……\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x1F,
        (
            "呵呵，看啊，阿鲁姆。\x01",
            "这孩子睡得\x01",
            "好熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x1E,
        "嗯，是啊，艾娅莉。\x02",
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x1E,
        (
            "看这美丽的睡脸，\x01",
            "简直就像个小天使。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x1E,
        (
            "呵呵，毕竟是女神般的你\x01",
            "所生的孩子，\x01",
            "这也是当然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x1F,
        "哎呀，阿鲁姆真是的……\x02",
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
            "#00003F……那、那个，\x01",
            "实在不好意思，\x01",
            "打扰二位了……\x02\x03",

            "#00000F请问您就是阿鲁姆先生吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E57B():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_E57B)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    #C0759
    ChrTalk(
        0x1E,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x1F,
        "各位是……？\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        (
            "#00000F我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02\x03",

            "收到了您的委托，\x01",
            "特此前来……\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x1E,
        "哦哦，是你们啊！\x02",
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x1E,
        (
            "来得正好！\x01",
            "我太高兴了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    #C0764
    ChrTalk(
        0x1F,
        (
            "太好了，阿鲁姆，\x01",
            "这样一来，总算是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    #C0765
    ChrTalk(
        0x1E,
        "嗯，艾娅莉……\x02",
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x1E,
        (
            "你刚刚生下孩子，\x01",
            "却如此颠簸劳累，\x01",
            "真是太辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x1E,
        (
            "都怪我如此\x01",
            "没用……\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x1F,
        (
            "阿鲁姆，你真是的……\x01",
            "我们不是约好不说这些的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x1F,
        (
            "在初次抱起这孩子的时候，\x01",
            "我们便相互许下了誓言。\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x1F,
        "无论遇到多大的困难……\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x1E,
        (
            "……我和你，还有\x01",
            "我们的宝贝孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x1E,
        (
            "也都要紧紧团结，全家携手跨越难关。\x01",
            "……对吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x1E,
        "啊啊，艾娅莉，我好爱你！\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x1F,
        "我也爱你！阿鲁姆！\x02",
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
            "#10106F呼……\x01",
            "一直卿卿我我，旁若无人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x102,
        (
            "#00102F完全沉浸在他们的\x01",
            "二人世界了……\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x101,
        (
            "#00006F是、是啊……\x02\x03",

            "#00000F……咳咳。\x01",
            "不好意思，可以和我们\x01",
            "说说委托的内容吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x1E,
        "啊……！\x02",
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x1F,
        "对了，差点忘了！\x02",
    )

    CloseMessageWindow()

    def lambda_E957():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_E957)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    #C0780
    ChrTalk(
        0x1E,
        (
            "那个……\x01",
            "我们希望各位帮忙\x01",
            "寻找某个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x1E,
        (
            "不好意思，\x01",
            "可以请你们立刻接受吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA41")

    label("loc_E9C1")

    OP_93(0x1E, 0x0, 0x0)
    OP_93(0x1F, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0782
    ChrTalk(
        0x1E,
        "哦哦，你们已经有空了吗？\x02",
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x1E,
        (
            "我们希望各位帮忙\x01",
            "寻找某个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x1E,
        (
            "不好意思，\x01",
            "可以请你们立刻接受吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA41")

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

    # Function_54_E2FA end

    def Function_55_EA91(): pass

    label("Function_55_EA91")

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
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
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
        (0, "loc_EAF3"),
        (1, "loc_EAFB"),
        (SWITCH_DEFAULT, "loc_EC88"),
    )


    label("loc_EAF3")

    Call(0, 56)
    Jump("loc_EC88")

    label("loc_EAFB")


    #C0785
    ChrTalk(
        0x101,
        (
            "#00006F那个……不好意思，\x01",
            "立刻接受恐怕有点勉强……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC31")

    #C0786
    ChrTalk(
        0x1E,
        (
            "怎、怎么会……\x01",
            "我们现在只能依靠你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x1F,
        (
            "拜托了……\x01",
            "就算是为了这个可爱的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #N0788
    NpcTalk(
        0x1F,
        "婴儿",
        "……唔、唔……\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x1F,
        (
            "乖哦，阿尔米，\x01",
            "没事的……\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x102,
        (
            "#00106F等、等我们有空之后，\x01",
            "一定会回来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x1E,
        (
            "嗯，拜托了。\x01",
            "我们会一直在这里等各位的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC80")

    label("loc_EC31")


    #C0792
    ChrTalk(
        0x1E,
        "怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x1E,
        (
            "那……等你们有空之后，\x01",
            "一定要回来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x1F,
        "拜托了……\x02",
    )

    CloseMessageWindow()

    label("loc_EC80")

    SetScenarioFlags(0x19A, 5)
    Jump("loc_EC88")

    label("loc_EC88")

    Return()

    # Function_55_EA91 end

    def Function_56_EC89(): pass

    label("Function_56_EC89")


    #C0795
    ChrTalk(
        0x101,
        (
            "#00000F嗯，明白了，\x01",
            "交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x1E,
        "哦哦……真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x1E,
        (
            "哎呀呀～得救了啊！\x01",
            "我们真的已经\x01",
            "一筹莫展了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    #C0798
    ChrTalk(
        0x1F,
        (
            "太好了，阿鲁姆！\x01",
            "我好开心！\x02",
        )
    )

    CloseMessageWindow()

    #N0799
    NpcTalk(
        0x1F,
        "婴儿",
        "哇，哇！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    #C0800
    ChrTalk(
        0x1E,
        (
            "啊啊，艾娅莉……\x01",
            "连阿尔米都很\x01",
            "高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x1F,
        "嗯，阿鲁姆……\x02",
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x103,
        "#00211F……请告诉我们委托的详情。\x02",
    )

    CloseMessageWindow()

    def lambda_EDA9():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_EDA9)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    #C0803
    ChrTalk(
        0x1E,
        "啊……嗯嗯，说的是啊。\x02",
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x1E,
        (
            "咳咳，不好意思……\x01",
            "我现在就说明一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x101,
        "#00006F（多、多亏有你啊，缇欧……）\x02",
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x103,
        (
            "#00206F（如果放着他们不管，\x01",
            "  不管再等多久，恐怕也\x01",
            "  无法进入正题。）\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x105,
        (
            "#10309F（呵呵……\x01",
            "  但我本想再\x01",
            "  旁观一阵子呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x1E,
        (
            "咳咳，希望各位帮忙\x01",
            "寻找的人是……\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x1E,
        (
            "在我幼年时期便已\x01",
            "天各一方的父亲。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x101,
        "#00005F天各一方的父亲吗……？\x02",
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x1E,
        (
            "嗯，虽然我们现在居住在\x01",
            "利贝尔王国……\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x1E,
        (
            "但我小时候是住在\x01",
            "克洛斯贝尔的。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x1E,
        (
            "由于某些原因，我的父母离了婚，\x01",
            "母亲带着我回到了\x01",
            "利贝尔的娘家。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x1E,
        (
            "我原本一直都以为，\x01",
            "不会再和父亲见面了……\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x1F,
        (
            "但在不久前，这个可爱的\x01",
            "孩子诞生了。\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x1F,
        (
            "阿鲁姆说，\x01",
            "无论如何也想让父亲\x01",
            "看看这孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x105,
        "#10305F哎……\x02",
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x1E,
        (
            "虽然他和母亲之间\x01",
            "曾经发生过一些不好的事情，\x01",
            "但对我而言，终究是生父。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x1E,
        (
            "如今我已经建立了幸福的家庭，\x01",
            "无论如何也想向他报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x1E,
        (
            "于是我说服了母亲，\x01",
            "来到了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x1E,
        "可是……\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x104,
        (
            "#00303F因为时隔太久，\x01",
            "所以已经找不到\x01",
            "你爸爸的住所了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x1E,
        "嗯，是的……\x02",
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x1E,
        (
            "他本来应该在住宅街有一栋房子，\x01",
            "但我们找过去时，\x01",
            "却已经人去楼空。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x1E,
        (
            "之后我用通讯联络的方式询问了母亲，\x01",
            "但自从离婚之后，\x01",
            "他们就几乎没有联系了。\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x1E,
        (
            "所以我们就开始\x01",
            "努力寻找父亲。\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x1F,
        (
            "我和阿鲁姆\x01",
            "去各种地方打听过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x1F,
        (
            "最终得知他曾因急病而\x01",
            "住进了医院，出院之后\x01",
            "搬到了旧城区……\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x1F,
        (
            "但我们过去拜访的时候，\x01",
            "人却总是不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x109,
        (
            "#10105F说不定，\x01",
            "他只是碰巧出门，\x01",
            "或者出去旅行了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x101,
        (
            "#00003F唔，不清楚……\x02\x03",

            "#00000F不过，从住宅街搬到旧城区，\x01",
            "真是很特殊的经历呢。\x02\x03",

            "艾莉，你听说住宅街的哪个居民\x01",
            "搬到旧城区了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1E, 500)
    Sleep(300)

    #C0832
    ChrTalk(
        0x102,
        (
            "#00103F完全没有呢……\x02\x03",

            "#00100F对了，阿鲁姆先生，\x01",
            "您还记得令尊的\x01",
            "姓名和职业吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)
    Sleep(300)

    #C0833
    ChrTalk(
        0x1E,
        (
            "嗯，这个嘛……\x01",
            "之前虽然听母亲说起过，\x01",
            "但不知道他现在是否还从事原来的工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x1E,
        (
            "名字自然知道——\x01",
            "他名叫『盖巴尔』，\x01",
            "是克洛斯贝尔市议会的一名议员。\x02",
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
        "#00005F盖巴尔议员……！\x02",
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x105,
        "#10305F哦，是那位先生啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    #C0837
    ChrTalk(
        0x1E,
        "哦哦……你们认识吗！？\x02",
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x102,
        (
            "#00103F嗯，之前处理某个委托时，\x01",
            "曾经见过一面。\x02\x03",

            "#00100F总之，我们先去旧城区\x01",
            "的公寓拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x101,
        (
            "#00003F嗯，赞成。\x02\x03",

            "#00000F说不定能了解到\x01",
            "他为何消失不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x1E,
        (
            "啊啊，委托你们来寻找父亲，\x01",
            "这一定是命运的安排！\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x1E,
        (
            "那就全部交给你们了，\x01",
            "请务必帮我找到父亲！\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x1F,
        "拜托各位了！\x02",
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x101,
        "#00000F嗯，交给我们吧。\x02",
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
            "任务【寻找自幼分离的父亲】\x07\x00",
            "开始！\x02",
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

    # Function_56_EC89 end

    SaveToFile()

Try(main)
