from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1030.bin",                # FileName
        "c1030",                    # MapName
        "c1030",                    # Location
        0x0012,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 18, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1030",                  # 0
        "强霍",                   # 1
        "芬",                     # 2
        "桑桑",                   # 3
        "古利德",                 # 4
        "帕库",                   # 5
        "帕库",                   # 6
        "鲁斯",                   # 7
        "鲁斯",                   # 8
        "紫发的女孩",             # 9
        "赛尔盖科长",             # 10
        "格蕾丝",                 # 11
        "雷因兹",                 # 12
        "弗里吉亚",               # 13
        "莱蒂娜",                 # 14
        "安敦",                   # 15
        "利库斯",                 # 16
        "瓦鲁多",                 # 17
        "诺加诺夫",               # 18
        "拉尔斯",                 # 19
        "库鲁特",                 # 20
        "伊斯",                   # 21
        "伊斯",                   # 22
        "餐具",                   # 23
        "餐具",                   # 24
        "餐具",                   # 25
        "餐具",                   # 26
        "餐具",                   # 27
        "餐具",                   # 28
        "餐具",                   # 29
        "餐具",                   # 30
        "餐具",                   # 31
        "餐具",                   # 32
        "餐具",                   # 33
        "SE控制",                 # 34
    ))

    AddCharChip((
        "chr/ch31600.itc",                   # 00
        "chr/ch25100.itc",                   # 01
        "chr/ch32500.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch20400.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch05202.itc",                   # 06
        "chr/ch20402.itc",                   # 07
        "chr/ch21202.itc",                   # 08
        "chr/ch06002.itc",                   # 09
        "chr/ch28102.itc",                   # 0A
        "chr/ch02502.itc",                   # 0B
        "chr/ch33300.itc",                   # 0C
        "chr/ch34500.itc",                   # 0D
        "chr/ch33302.itc",                   # 0E
        "chr/ch37300.itc",                   # 0F
        "chr/ch37400.itc",                   # 10
        "apl/ch50018.itc",                   # 11
        "chr/ch30802.itc",                   # 12
        "chr/ch23400.itc",                   # 13
        "chr/ch21400.itc",                   # 14
        "apl/ch50092.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(16000,   0,       15989,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(16030,   0,       6050,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(12310,   0,       -1990,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(7130,    200,     -1480,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(16030,   0,       6050,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10689,   150,     3170,    270,  341,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(17909,   0,       8399,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(7300,    129,     3230,    90,   341,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(13949,   50,      2900,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(14100,   50,      5909,    90,   469,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4900,    100,     7099,    270,  469,  0x0, 0,   9,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1299,    50,      7099,    90,   469,  0x0, 0,   10,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-49830,  29,      -54020,  180,  389,  0x0, 0,   12,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-49830,  29,      -55880,  0,    389,  0x0, 0,   13,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-100000, 19,      -54500,  270,  389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-103849, 0,       -53459,  180,  389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4849,    0,       7099,    270,  389,  0x0, 0,   17,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(3200,    0,       8899,    180,  389,  0x0, 0,   18,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-50970,  29,      -56450,  180,  389,  0x0, 0,   19,  0,   0,   2,   0,   34,  255,  0)
    DeclNpc(-53849,  0,       -55180,  180,  389,  0x0, 0,   20,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14590,   0,       4630,    1000,    16030,   1500,    6050,    0x007E, 0,  5,  0x0000)

    ScpFunction((
        "Function_0_598",          # 00, 0
        "Function_1_650",          # 01, 1
        "Function_2_7A4",          # 02, 2
        "Function_3_7CC",          # 03, 3
        "Function_4_B3F",          # 04, 4
        "Function_5_B9D",          # 05, 5
        "Function_6_BC8",          # 06, 6
        "Function_7_CBE",          # 07, 7
        "Function_8_17EC",         # 08, 8
        "Function_9_18E2",         # 09, 9
        "Function_10_28F0",        # 0A, 10
        "Function_11_3B1D",        # 0B, 11
        "Function_12_486D",        # 0C, 12
        "Function_13_4963",        # 0D, 13
        "Function_14_4A9A",        # 0E, 14
        "Function_15_519C",        # 0F, 15
        "Function_16_51FD",        # 10, 16
        "Function_17_611A",        # 11, 17
        "Function_18_6285",        # 12, 18
        "Function_19_6289",        # 13, 19
        "Function_20_6663",        # 14, 20
        "Function_21_68FE",        # 15, 21
        "Function_22_6CFE",        # 16, 22
        "Function_23_6E07",        # 17, 23
        "Function_24_7103",        # 18, 24
        "Function_25_747A",        # 19, 25
        "Function_26_78DB",        # 1A, 26
        "Function_27_7BB6",        # 1B, 27
        "Function_28_91A1",        # 1C, 28
        "Function_29_9600",        # 1D, 29
        "Function_30_9C15",        # 1E, 30
        "Function_31_BDF7",        # 1F, 31
        "Function_32_C6C8",        # 20, 32
        "Function_33_C880",        # 21, 33
        "Function_34_CD1F",        # 22, 34
        "Function_35_D1E5",        # 23, 35
        "Function_36_D339",        # 24, 36
        "Function_37_DB59",        # 25, 37
        "Function_38_E294",        # 26, 38
        "Function_39_E5B2",        # 27, 39
        "Function_40_F507",        # 28, 40
        "Function_41_F743",        # 29, 41
        "Function_42_F997",        # 2A, 42
        "Function_43_F9E2",        # 2B, 43
    ))


    def Function_0_598(): pass

    label("Function_0_598")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5D8"),
        (1, "loc_5E4"),
        (2, "loc_5F0"),
        (3, "loc_5FC"),
        (4, "loc_608"),
        (5, "loc_614"),
        (6, "loc_620"),
        (SWITCH_DEFAULT, "loc_62C"),
    )


    label("loc_5D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_5E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_5F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_5FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_608")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_614")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_620")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_62C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_638")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_64F")

    Return()

    # Function_0_598 end

    def Function_1_650(): pass

    label("Function_1_650")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A3")
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
    Jump("Function_1_650")

    label("loc_7A3")

    Return()

    # Function_1_650 end

    def Function_2_7A4(): pass

    label("Function_2_7A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7CB")
    OP_94(0xFE, 0xFFFF3D96, 0xFFFF29BE, 0xFFFF381E, 0xFFFF2126, 0x3E8)
    Jump("Function_2_7A4")

    label("loc_7CB")

    Return()

    # Function_2_7A4 end

    def Function_3_7CC(): pass

    label("Function_3_7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7FA")
    SetChrPos(0x9, 11180, 0, 15810, 0)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B14")

    label("loc_7FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_84A")
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, -103790, 0, -55180, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_B14")

    label("loc_84A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_85D")
    SetChrFlags(0x8, 0x10)
    Jump("loc_B14")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8AD")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8A8")
    SetChrPos(0x16, -100320, 30, -56530, 180)
    SetChrPos(0x17, -101160, 30, -55430, 180)
    SetChrFlags(0x17, 0x10)

    label("loc_8A8")

    Jump("loc_B14")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_925")
    SetChrPos(0x8, 16030, 0, 6050, 270)
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0xA, 0x80)
    Jump("loc_920")

    label("loc_909")

    SetChrPos(0xA, 13950, 0, 6940, 135)
    BeginChrThread(0xA, 0, 0, 0)

    label("loc_920")

    Jump("loc_B14")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_99E")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x19, 0x1)
    SetChrChipByIndex(0x1E, 0x15)
    SetChrSubChip(0x1E, 0xF)
    SetChrPos(0x1E, 4000, 600, 7100, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x15)
    SetChrSubChip(0x1F, 0xF)
    SetChrPos(0x1F, 3300, 600, 8000, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    Jump("loc_B14")

    label("loc_99E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9B6")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_B14")

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9C4")
    Jump("loc_B14")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9D2")
    Jump("loc_B14")

    label("loc_9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A41")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A1E")
    SetChrPos(0x1A, -49440, 30, -56190, 270)
    SetChrPos(0x1B, -51000, 30, -56190, 90)
    BeginChrThread(0x1A, 0, 0, 0)
    Jump("loc_A3C")

    label("loc_A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A35")
    SetChrFlags(0x1B, 0x10)
    Jump("loc_A3C")

    label("loc_A35")

    OP_93(0x1B, 0x2D, 0x0)

    label("loc_A3C")

    Jump("loc_B14")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A90")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1A, -49800, 20, -53530, 180)
    SetChrPos(0x1B, -50200, 20, -55110, 0)
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1B, 0x10)
    BeginChrThread(0x1A, 0, 0, 0)
    Jump("loc_B14")

    label("loc_A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AE7")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x40)
    SetChrChipByIndex(0x14, 0xE)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, 3230, 150, 9000, 180)
    ClearChrFlags(0x15, 0x80)
    BeginChrThread(0x15, 0, 0, 0)
    SetChrPos(0x15, 2020, 0, 9600, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_B14")

    label("loc_AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_B0B")
    ClearChrFlags(0x14, 0x80)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x15, 0x80)
    BeginChrThread(0x15, 0, 0, 0)
    Jump("loc_B14")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B14")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2B")
    ClearChrFlags(0x10, 0x80)

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3E")
    ClearChrFlags(0x12, 0x80)

    label("loc_B3E")

    Return()

    # Function_3_7CC end

    def Function_4_B3F(): pass

    label("Function_4_B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B50")
    SetScenarioFlags(0x1, 0)
    Jump("loc_B69")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B66")
    SetScenarioFlags(0x0, 6)
    Jump("loc_B69")

    label("loc_B66")

    SetScenarioFlags(0x0, 7)

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B85")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B9C")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B9C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B9C")

    label("loc_B9C")

    Return()

    # Function_4_B3F end

    def Function_5_B9D(): pass

    label("Function_5_B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BAE")
    Call(0, 12)
    Jump("loc_BC7")

    label("loc_BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC4")
    Call(0, 6)
    Jump("loc_BC7")

    label("loc_BC4")

    Call(0, 8)

    label("loc_BC7")

    Return()

    # Function_5_B9D end

    def Function_6_BC8(): pass

    label("Function_6_BC8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CB7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5D")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAD")

    label("loc_C5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAD")

    label("loc_C7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C91")
    Jump("loc_CAD")

    label("loc_C91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_CAD")

    Jump("loc_BDE")

    label("loc_CB2")

    Jump("loc_CBA")

    label("loc_CB7")

    Call(0, 7)

    label("loc_CBA")

    TalkEnd(0x8)
    Return()

    # Function_6_BC8 end

    def Function_7_CBE(): pass

    label("Function_7_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D58")

    #C0001
    ChrTalk(
        0x8,
        (
            "我本来让那个临时工在厨房帮忙，\x01",
            "结果他每次都和来厨房\x01",
            "拿盘子的桑桑撞在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "……那个臭小子，该不会\x01",
            "根本就是故意的吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D9C")

    label("loc_D58")


    #C0003
    ChrTalk(
        0x8,
        "我让那个临时工去招揽客人了，\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "绝对不会再让他踏入厨房一步。\x02",
    )

    CloseMessageWindow()

    label("loc_D9C")

    Jump("loc_17EB")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DD1")

    #C0005
    ChrTalk(
        0x8,
        "……临时工只要老实干活就好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17EB")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F")

    #C0006
    ChrTalk(
        0x8,
        "（滋啦滋啦）……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "今天的汤很不错哦。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_E6C")

    label("loc_E1F")


    #C0008
    ChrTalk(
        0x8,
        (
            "这个汤的配方，\x01",
            "我在共和国时就一直使用，\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "是我们店料理美味的秘诀哦。\x02",
    )

    CloseMessageWindow()

    label("loc_E6C")

    Jump("loc_17EB")

    label("loc_E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F22")

    #C0010
    ChrTalk(
        0x8,
        (
            "我开这家店并不完全是\x01",
            "为了取悦客人，\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "但也并不完全是为了赚钱，\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "……这两个目的都各占一点。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "反正我们这里也不是\x01",
            "什么很受欢迎的大酒馆。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F66")

    label("loc_F22")


    #C0014
    ChrTalk(
        0x8,
        "开店这种事，赚得差不多也就行了，\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "因为我比较喜欢安静的店。\x02",
    )

    CloseMessageWindow()

    label("loc_F66")

    Jump("loc_17EB")

    label("loc_F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_FC8")

    #C0016
    ChrTalk(
        0x8,
        "纪念庆典结束后，这里终于安静下来了。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……而我也能心平气和地\x01",
            "经营了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17EB")

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_104C")

    #C0018
    ChrTalk(
        0x8,
        (
            "如果那些混混敢对桑桑意图不轨，\x01",
            "我一定不会饶过他们的～～～……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "桑桑也真是的。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "根本不需要\x01",
            "接待那种客人！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17EB")

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_110C")

    #C0021
    ChrTalk(
        0x8,
        "那些家伙……又来了啊。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "要是再敢在店里捣乱，\x01",
            "我就把他们赶出去！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1107")

    #C0023
    ChrTalk(
        0x101,
        (
            "#0000F（瓦鲁多好像\x01",
            "  经常来这家店啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#0100F（店里的人\x01",
            "  好像也都见怪不怪了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1107")

    Jump("loc_17EB")

    label("loc_110C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1236")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C3")

    #C0025
    ChrTalk(
        0x8,
        (
            "我移居到这里来的时候，\x01",
            "桑桑还很小。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "而且这附近\x01",
            "也没有与桑桑年纪相仿\x01",
            "的女孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "……不过，现在\x01",
            "她好像终于交了个好朋友哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "我也很开心啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1231")

    label("loc_11C3")


    #C0029
    ChrTalk(
        0x8,
        (
            "桑桑交了个好朋友\x01",
            "我也很开心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "………………只是………\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "如果那个好朋友是男人，\x01",
            "我可不会允许……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1231")

    Jump("loc_17EB")

    label("loc_1236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_13A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130B")

    #C0032
    ChrTalk(
        0x8,
        (
            "……我从客人那里\x01",
            "听说了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "原来黑月也到\x01",
            "这条街来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "……那可是一帮既狡猾又可怕的家伙哦，\x01",
            "去我们共和国的东方人街上问问就知道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "你们还是不要和他们\x01",
            "扯上关系比较好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_139F")

    label("loc_130B")


    #C0036
    ChrTalk(
        0x8,
        (
            "为准备纪念庆典都已经忙得不可开交了，\x01",
            "竟然还听到那么不好的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "……黑月可是一帮既狡猾又可怕的家伙哦，\x01",
            "你们还是不要和他们扯上关系比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139F")

    Jump("loc_17EB")

    label("loc_13A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141E")

    #C0038
    ChrTalk(
        0x8,
        "那边的两个人，总是会聊很长时间。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "真是的……坐那么久\x01",
            "也不多点些东西，真是让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_147C")

    label("loc_141E")


    #C0040
    ChrTalk(
        0x8,
        (
            "那边的两个人，总是会聊很长时间。\x01",
            "真是的，他们要是再不多点些东西，\x01",
            "我就要拿勺子敲他们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147C")

    Jump("loc_17EB")

    label("loc_1481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1501")

    #C0041
    ChrTalk(
        0x8,
        (
            "呼，桑桑这孩子\x01",
            "也真是让人搞不懂啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "明明都跟她说过，\x01",
            "不用在店里帮忙了……\x01",
            "（小声嘟囔……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_152E")

    label("loc_1501")


    #C0043
    ChrTalk(
        0x8,
        (
            "……没什么啦，\x01",
            "想要点餐的话麻烦去那边。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152E")

    Jump("loc_17EB")

    label("loc_1533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1600")

    #C0044
    ChrTalk(
        0x8,
        (
            "最近都没见到\x01",
            "旧城区的那帮小鬼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "我原本以为这样一来，\x01",
            "店里就可以安静一些了……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "但是有帮家伙一下班就会来\x01",
            "店里喝酒，还总是吵吵闹闹的。\x01",
            "真是，害得店里又安静不下来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_163E")

    label("loc_1600")


    #C0047
    ChrTalk(
        0x8,
        (
            "店里总是很吵闹，真让人头疼。\x01",
            "客人们就不能\x01",
            "安静点吃饭吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163E")

    Jump("loc_17EB")

    label("loc_1643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_174E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CB")

    #C0048
    ChrTalk(
        0x8,
        (
            "旧城区的那帮小鬼\x01",
            "很让我生气。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "之前就曾经来我们店里\x01",
            "大吵大闹过。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "……虽然当时就被我\x01",
            "赶出去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1749")

    label("loc_16CB")


    #C0051
    ChrTalk(
        0x8,
        (
            "旧城区的那帮小鬼\x01",
            "之前就来我们店里大吵大闹过。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "哼，给人添麻烦也要有个限度。\x01",
            "再有下次的话，就不只是赶出去那么简单了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1749")

    Jump("loc_17EB")

    label("loc_174E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_17EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BA")

    #C0053
    ChrTalk(
        0x8,
        "唔……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "……这里是厨房，\x01",
            "客人可不能进来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "要点餐的话麻烦去柜台！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17EB")

    label("loc_17BA")


    #C0056
    ChrTalk(
        0x8,
        (
            "几位客人，这里是厨房。\x01",
            "要点餐的话请去那边！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EB")

    Return()

    # Function_7_CBE end

    def Function_8_17EC(): pass

    label("Function_8_17EC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_18DB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1802")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1861")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1881")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18D1")

    label("loc_1881")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A1")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18D1")

    label("loc_18A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B5")
    Jump("loc_18D1")

    label("loc_18B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_18D1")

    Jump("loc_1802")

    label("loc_18D6")

    Jump("loc_18DE")

    label("loc_18DB")

    Call(0, 9)

    label("loc_18DE")

    TalkEnd(0x9)
    Return()

    # Function_8_17EC end

    def Function_9_18E2(): pass

    label("Function_9_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_191B")

    #C0057
    ChrTalk(
        0x9,
        (
            "呵呵……老板还是\x01",
            "一如既往地爱操心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EF")

    label("loc_191B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1995")

    #C0058
    ChrTalk(
        0x9,
        (
            "帕库和鲁斯开始\x01",
            "在我们店当临时工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "他们之前赊的账还没有还清，\x01",
            "所以我会毫不客气地给他们安排工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EF")

    label("loc_1995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A19")

    #C0060
    ChrTalk(
        0x9,
        (
            "哟，欢迎光临！\x01",
            "各位想吃什么呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "……各位这是怎么了，\x01",
            "怎么都一脸愁容啊。\x01",
            "市内发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A8E")

    label("loc_1A19")


    #C0062
    ChrTalk(
        0x9,
        (
            "最近我们店里的大事件，\x01",
            "应该就是帕库和鲁斯\x01",
            "的幻想终于破灭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "……那两个人，\x01",
            "总是在我们店里漫无目的地聊天～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8E")

    Jump("loc_28EF")

    label("loc_1A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1E")

    #C0064
    ChrTalk(
        0x9,
        "欢迎光临城边酒馆！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "纪念庆典结束后，\x01",
            "来店里的就都是些老顾客了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "哎呀……真希望还能\x01",
            "再大赚一笔啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B92")

    label("loc_1B1E")


    #C0067
    ChrTalk(
        0x9,
        (
            "我们店也是做生意的，\x01",
            "为的就是大赚一笔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "真希望再办场纪念庆典这种活动，\x01",
            "那样的话，店里就又会热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B92")

    Jump("loc_28EF")

    label("loc_1B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF8")

    #C0069
    ChrTalk(
        0x9,
        (
            "桑桑说她要和莉夏\x01",
            "一起去逛街买衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "啊啊，我也想\x01",
            "跟着去啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C5E")

    label("loc_1BF8")


    #C0071
    ChrTalk(
        0x9,
        (
            "如果顺利的话，\x01",
            "还能和莉夏约会……！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "不过陪女孩子购物要花很多钱啊。\x01",
            "……嗯，今天就先不去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5E")

    Jump("loc_28EF")

    label("loc_1C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7D")

    #C0073
    ChrTalk(
        0x9,
        (
            "呦，你们是\x01",
            "给我们送鱼来的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "哈哈，真是谢谢啊。\x01",
            "这样一来，今晚应该能应付过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "话说回来，那些客人好像要在这里\x01",
            "住到彩虹剧团的预演开始……\x01",
            "真是很有品位的客人呐。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "要是连生鱼片都拿不出，\x01",
            "可是会让这家店的招牌蒙羞哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D78")
    SetScenarioFlags(0x0, 1)

    label("loc_1D78")

    Jump("loc_28EF")

    label("loc_1D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1EDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7E")

    #C0077
    ChrTalk(
        0x9,
        (
            "在我的故乡——共和国，\x01",
            "也有很多危险事件和恐怖袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "那个国家虽然表面上看起来一派平静祥和，\x01",
            "但暗地里其实也有很多问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "不过，和克洛斯贝尔不一样的是，\x01",
            "它拥有很强大的军队。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "名字叫治安维持部队，\x01",
            "可谓十分优秀啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ED8")

    label("loc_1E7E")


    #C0081
    ChrTalk(
        0x9,
        (
            "而克洛斯贝尔\x01",
            "的警察却都很不可靠……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "啊，不好意思。\x01",
            "看那徽章，难道你们是警官吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED8")

    Jump("loc_28EF")

    label("loc_1EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_211E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAC")

    #C0083
    ChrTalk(
        0x9,
        (
            "糟糕了，今天突然\x01",
            "接到几位客人的预约。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "如果在平时，我们会很乐意\x01",
            "端出生鱼片来招待……\x01",
            "不过今天刚好没有那种鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "你们能帮忙找来五条鱼吗？\x01",
            "不用特别名贵，普通的也可以。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2119")

    label("loc_1FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AB")

    #C0086
    ChrTalk(
        0x9,
        (
            "哟，你们是\x01",
            "给我们送鱼来的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "哈哈，真是谢谢啊。\x01",
            "这样一来，今晚应该就能应付过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "话说回来，那些客人好像要在这里\x01",
            "住到彩虹剧团的预演开始……\x01",
            "真是很有品位的客人呐。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "要是连生鱼片都拿不出，\x01",
            "可是会让这家店的招牌蒙羞哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2119")

    label("loc_20AB")


    #C0090
    ChrTalk(
        0x9,
        (
            "总之，你们帮大忙了，\x01",
            "这样一来，晚上就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "接下来……只要那些穿红色外套的家伙\x01",
            "不来捣乱就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2119")

    Jump("loc_28EF")

    label("loc_211E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E1")

    #C0092
    ChrTalk(
        0x9,
        (
            "最近有个叫莉夏的女孩\x01",
            "和桑桑相处得很好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "今天早上她也来了。\x01",
            "啊，她真的好可爱啊～⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "正是我喜欢的类型！\x01",
            "而且她跟我还是共和国出身的同乡，\x01",
            "真是太完美了～⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2242")

    label("loc_21E1")


    #C0095
    ChrTalk(
        0x9,
        (
            "莉夏好像也是共和国出身的，\x01",
            "实在太好了……这下就不愁没话题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "这次我准备认真追求她～⊥\x02",
    )

    CloseMessageWindow()

    label("loc_2242")

    Jump("loc_28EF")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_233C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D8")

    #C0097
    ChrTalk(
        0x9,
        "喂喂，你们听我说啊。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "最近，有许多客人来预订\x01",
            "纪念庆典期间的房间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "竟然会来远离中心市区的\x01",
            "酒馆订房间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2337")

    label("loc_22D8")


    #C0100
    ChrTalk(
        0x9,
        (
            "去酒店的话还说得过去，\x01",
            "竟然会来我们这种\x01",
            "偏远的小酒馆……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "那些酒店\x01",
            "不会都爆满了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2337")

    Jump("loc_28EF")

    label("loc_233C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2475")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2418")

    #C0102
    ChrTalk(
        0x9,
        (
            "那边的两个人是\x01",
            "『永远翻不了身的\x01",
            "帕库和鲁斯』。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "曾经是桑桑在主日学校里\x01",
            "同年级的同学。\x01",
            "听说当时在学校里他们俩也是这么没用。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "哈哈，总是听他们说要做生意，\x01",
            "但从没见过他们实际行动过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2470")

    label("loc_2418")


    #C0105
    ChrTalk(
        0x9,
        (
            "那边的两个人是\x01",
            "『永远翻不了身的\x01",
            "帕库和鲁斯』。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        "不过，这只是我给他们取的绰号。\x02",
    )

    CloseMessageWindow()

    label("loc_2470")

    Jump("loc_28EF")

    label("loc_2475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_24E1")

    #C0107
    ChrTalk(
        0x9,
        (
            "嘿嘿，这位客人\x01",
            "很会吃嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "我们店的叉烧肉可是很正宗的，\x01",
            "因为我们老板来自东方人街哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EF")

    label("loc_24E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_262A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D7")

    #C0109
    ChrTalk(
        0x9,
        "桑桑她很可爱吧～\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "既有出众的工作能力，\x01",
            "又有着甜美的声音，\x01",
            "简直是贤妻的不二人选！\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "……所以老板才很担心，\x01",
            "怕她被坏男人骗。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "虽然表面上装着在颠锅炒菜，\x01",
            "其实一直都在注意这些呢。\x01",
            "呵呵……看起来很有意思吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2625")

    label("loc_25D7")


    #C0113
    ChrTalk(
        0x9,
        (
            "桑桑她\x01",
            "很受客人欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "呵呵，不过老板倒是很担心，\x01",
            "怕她被坏男人骗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2625")

    Jump("loc_28EF")

    label("loc_262A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2777")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271C")

    #C0115
    ChrTalk(
        0x9,
        (
            "我们这里是偏远的小酒馆～\x01",
            "位于街道最末端哦～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "……也就是说，\x01",
            "我们这里是离旧城区最近的一家店。\x01",
            "所以是受那帮不良团伙危害最深的。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "特别是那些穿红色衣服的家伙，\x01",
            "每隔两天就会来我们店里捣乱。\x01",
            "真让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2772")

    label("loc_271C")


    #C0118
    ChrTalk(
        0x9,
        (
            "旧城区的小鬼们\x01",
            "在这附近也是臭名远扬。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "反正他们都不是好人，\x01",
            "你们最好别去惹。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2772")

    Jump("loc_28EF")

    label("loc_2777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_28EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288F")

    #C0120
    ChrTalk(
        0x9,
        (
            "哟，欢迎光临，\x01",
            "欢迎来我们这个偏远小酒馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "这一带的建筑风格看起来\x01",
            "就像一个大杂烩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔受共和国管辖的时候，\x01",
            "这里住着许多东方移民。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "之后各地的移民都逐渐入住，\x01",
            "到现在都分不清国籍了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "算了，我也不是不喜欢\x01",
            "这种大杂烩的感觉～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28EF")

    label("loc_288F")


    #C0125
    ChrTalk(
        0x9,
        (
            "各位是来观光旅游的吗？\x01",
            "还是克洛斯贝尔人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "不过，不管是哪里来的都好，\x01",
            "来点些吃的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EF")

    Return()

    # Function_9_18E2 end

    def Function_10_28F0(): pass

    label("Function_10_28F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2911")
    Call(0, 36)
    Return()

    label("loc_2911")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E4A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_293B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E46")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "将鱼交出\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2982"),
        (1, "loc_2A43"),
        (SWITCH_DEFAULT, "loc_2E32"),
    )


    label("loc_2982")


    #C0127
    ChrTalk(
        0xFE,
        (
            "是打杂事务所的人吧，你们好～\x01",
            "……你们把鱼送来了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "我要求的是\x01",
            "五条『非常细长的鱼』哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "虽然用其它鱼也不是不行……\x01",
            "但一定要是五条\x01",
            "同种类的鱼哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "因为预约的客人有五位。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E41")

    label("loc_2A43")

    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC5")

    #C0131
    ChrTalk(
        0xA,
        (
            "啊呀～你们好像\x01",
            "没有五条符合条件的鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "五条鱼必须都是\x01",
            "同种类的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "因为预约的\x01",
            "客人有五位。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2D")

    label("loc_2AC5")

    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1A")

    #C0134
    ChrTalk(
        0xA,
        "这样啊……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "客人晚上就会来了，\x01",
            "麻烦你们尽快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E41")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BAB")

    #C0136
    ChrTalk(
        0xA,
        (
            "这是……\x01",
            "没错，就是这种『细长的鱼』哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "用这种鱼做出的盖饭十分美味哦。\x01",
            "而且刚好也有五条……\x01",
            "……可以转让给我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4E")

    label("loc_2BAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C88")

    #C0138
    ChrTalk(
        0xA,
        (
            "这是…………？？\x01",
            "虽然也很细长，但好像在发光啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "嗯……嗯……\x01",
            "虽然和平时的不大一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0140
    ChrTalk(
        0xA,
        (
            "但看起来差不多，一定没问题的～\x01",
            "而且刚好也有五条……\x01",
            "……可以转让给我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4E")

    label("loc_2C88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CF7")

    #C0141
    ChrTalk(
        0xA,
        "？　这是……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "啊呀～这不是鱼哦，\x01",
            "不是鱼的话可不行。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D4E")

    label("loc_2CF7")


    #C0143
    ChrTalk(
        0xA,
        "这好像……不是『细长的鱼』啊。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "不过五条倒都是同种类的。\x01",
            "……可以转让给我吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D62")
    Jump("loc_2E41")

    label("loc_2D62")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【转让】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB4")
    Call(0, 37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E41")

    label("loc_2DB4")


    #C0145
    ChrTalk(
        0xA,
        (
            "这样啊……\x01",
            "……那也没办法。\x01",
            "打杂事务所的人也有不方便的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "不过你们要是回心转意了，\x01",
            "希望能把鱼转让给我哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2D")

    Jump("loc_2E41")

    label("loc_2E32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E41")

    label("loc_2E41")

    Jump("loc_293B")

    label("loc_2E46")

    TalkEnd(0xFE)
    Return()

    label("loc_2E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_2EBA")

    #C0147
    ChrTalk(
        0xA,
        (
            "这样一来，晚上的客人们\x01",
            "就能吃得很开心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "呵呵，打杂事务所的各位，\x01",
            "今天谢谢你们了哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B19")

    label("loc_2EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F48")

    #C0149
    ChrTalk(
        0xFE,
        "莉夏遇到什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "白天稍微跟她说了一会话，\x01",
            "感觉她好像有点没精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "又有……什么担心的事情了吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F99")

    label("loc_2F48")


    #C0152
    ChrTalk(
        0xFE,
        (
            "就算莉夏不说，我也知道哦。\x01",
            "莉夏一定是在担心什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "发生什么事了呢……\x02",
    )

    CloseMessageWindow()

    label("loc_2F99")

    Jump("loc_3B19")

    label("loc_2F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3023")

    #C0154
    ChrTalk(
        0xFE,
        (
            "帕库和鲁斯说他们\x01",
            "想在店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "呵呵，我去拜托爸爸后，\x01",
            "他马上就答应了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "爸爸就是这么温柔。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3081")

    label("loc_3023")


    #C0157
    ChrTalk(
        0xFE,
        (
            "有帕库和鲁斯帮忙，\x01",
            "我们也会轻松许多。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "呵呵，而且这样就可以给\x01",
            "客人提供更好的服务了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3081")

    Jump("loc_3B19")

    label("loc_3086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_313D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3115")

    #C0159
    ChrTalk(
        0xFE,
        (
            "帕库和鲁斯\x01",
            "好像一直都很快乐～\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "他们两个是我以前\x01",
            "在主日学校的同学哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "看他们关系那么好，真是让人羡慕。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3138")

    label("loc_3115")


    #C0162
    ChrTalk(
        0xFE,
        (
            "帕库和鲁斯\x01",
            "好像一直都很快乐～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3138")

    Jump("loc_3B19")

    label("loc_313D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31DF")

    #C0163
    ChrTalk(
        0xFE,
        (
            "我在店里帮忙，\x01",
            "也已经有四个月了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "我得做服务员、洗盘子，还要铺床。\x01",
            "把店里收拾得干干净净，我就会开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        "看到客人高兴，我也很开心哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B19")

    label("loc_31DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_32C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328D")

    #C0166
    ChrTalk(
        0xFE,
        (
            "听我说，听我说～！\x01",
            "今天我和莉夏约好\x01",
            "要一起去逛百货店哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "莉夏说她今天休息。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "呵呵，纪念庆典时忙得要死，\x01",
            "但今天可要好好玩个痛快啊～⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32C0")

    label("loc_328D")


    #C0169
    ChrTalk(
        0xFE,
        (
            "快到我和她约定的时间了哦。\x01",
            "呵呵，好期待啊～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C0")

    Jump("loc_3B19")

    label("loc_32C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_339D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335A")

    #C0170
    ChrTalk(
        0xFE,
        (
            "纪念庆典快到了，所以店里非常忙，\x01",
            "我也得努力工作才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "不过……爸爸今天\x01",
            "好像一直瞪着我……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "我做错什么了吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3398")

    label("loc_335A")


    #C0173
    ChrTalk(
        0xFE,
        (
            "我今天经常感觉到爸爸的视线，\x01",
            "……我应该\x01",
            "没有打破盘子吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3398")

    Jump("loc_3B19")

    label("loc_339D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_346D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3408")

    #C0174
    ChrTalk(
        0xFE,
        (
            "只要那位客人一来，\x01",
            "爸爸就很警觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "这是为什么呢？\x01",
            "那位客人并不可怕吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3468")

    label("loc_3408")


    #C0176
    ChrTalk(
        0xFE,
        (
            "（忙忙碌碌）……\x01",
            "今天店内的工作很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "跟各种各样的客人聊天，\x01",
            "是件很开心的事，对吧¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3468")

    Jump("loc_3B19")

    label("loc_346D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E9")

    #C0178
    ChrTalk(
        0xFE,
        (
            "那个……\x01",
            "莉夏最近好像有点烦恼，\x01",
            "经常看到她发呆哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "作为彩虹剧团的团员，\x01",
            "果然很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3523")

    label("loc_34E9")


    #C0180
    ChrTalk(
        0xFE,
        (
            "莉夏最近\x01",
            "好像有点烦恼。\x01",
            "真希望我也能为她做点什么……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3523")

    Jump("loc_3B19")

    label("loc_3528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35BE")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0181
    ChrTalk(
        0xFE,
        "……听我说听我说！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "莉夏好像是那个\x01",
            "彩虹剧团的团员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "哇，真是太厉害了！\x01",
            "我也很崇拜她～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_360D")

    label("loc_35BE")


    #C0184
    ChrTalk(
        0xFE,
        (
            "我的朋友莉夏\x01",
            "好像是彩虹剧团\x01",
            "的团员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "哈，好厉害哦～\x01",
            "我也很崇拜她～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360D")

    Jump("loc_3B19")

    label("loc_3612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F3")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0186
    ChrTalk(
        0xFE,
        "……我告诉你们哦！\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "最近啊，店里\x01",
            "来了一个很可爱的客人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "是一个叫做莉夏的女孩。\x01",
            "好像是刚搬到这附近来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "说是和我年龄一样。\x01",
            "呵呵，要是能跟她做朋友就好了哦¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_374D")

    label("loc_36F3")


    #C0190
    ChrTalk(
        0xFE,
        (
            "莉夏好像是\x01",
            "刚搬到这附近来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "说是和我年龄一样。\x01",
            "呵呵，要是能跟她做朋友就好了¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374D")

    Jump("loc_3B19")

    label("loc_3752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3812")

    #C0192
    ChrTalk(
        0xFE,
        (
            "我今年刚从\x01",
            "主日学校毕业哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "经过再三考虑后……\x01",
            "最终决定留在店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "因为爸爸总是一副严肃的表情，\x01",
            "有时还会瞪客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "再这样下去这家店可就危险了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3884")

    label("loc_3812")


    #C0196
    ChrTalk(
        0xFE,
        (
            "要是完全交给爸爸，这家店就危险了。\x01",
            "所以我才要留下来帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "虽然现在还有点不习惯……\x01",
            "要保持微笑、微笑～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3884")

    Jump("loc_3B19")

    label("loc_3889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_39D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3976")

    #C0198
    ChrTalk(
        0xFE,
        (
            "每到周末，警备队的人\x01",
            "都会成群结队来我们店吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "呵呵，能认识各种各样的人\x01",
            "真是开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "不过……大家工作好像都很忙。\x01",
            "所以不当班时就会来我们这里放松放松。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "唔唔，我必须好好\x01",
            "给他们加油鼓劲呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39D2")

    label("loc_3976")


    #C0202
    ChrTalk(
        0xFE,
        (
            "警备队的人经常\x01",
            "来我们店里吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "大家工作好像都很忙。\x01",
            "我必须好好给他们加油鼓劲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D2")

    Jump("loc_3B19")

    label("loc_39D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3A32")

    #C0204
    ChrTalk(
        0xFE,
        "我们店里的饭菜怎么样？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "呵呵，很好吃吧。\x01",
            "爸爸做的菜可是天下第一哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B19")

    label("loc_3A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC4")

    #C0206
    ChrTalk(
        0xFE,
        "哎呀，好可爱的客人呢～\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "是想吃饭呢？还是想住宿？\x01",
            "两者都还有空位哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "呵呵，如果有什么要求，请随意吩咐～⊥\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B19")

    label("loc_3AC4")


    #C0209
    ChrTalk(
        0xFE,
        (
            "我们这里是集饮食与\x01",
            "住宿为一体的酒馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "呵呵，如果有什么要求，请随意吩咐～⊥\x02",
    )

    CloseMessageWindow()

    label("loc_3B19")

    TalkEnd(0xFE)
    Return()

    # Function_10_28F0 end

    def Function_11_3B1D(): pass

    label("Function_11_3B1D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BB1")
    Jump("loc_3BFB")

    label("loc_3BB1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BD1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BFB")

    label("loc_3BD1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BF1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BFB")

    label("loc_3BF1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BFB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD5")

    #C0211
    ChrTalk(
        0xFE,
        "啊，太阳都快下山了啊……\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "（大吃大喝、狼吞虎咽）……\x01",
            "必须快点吃完，赶快出发才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "我是往返于共和国和自治州的卡车送货员，\x01",
            "今天得再往返一趟。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D40")

    label("loc_3CD5")


    #C0214
    ChrTalk(
        0xFE,
        (
            "我是往返于共和国和自治州的卡车送货员，\x01",
            "今天得再往返一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "最近往返的次数有所增加，都忙不过来了。\x02",
    )

    CloseMessageWindow()

    label("loc_3D40")

    Jump("loc_4865")

    label("loc_3D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF7")

    #C0216
    ChrTalk(
        0xFE,
        (
            "昨天我去『利泽罗贸易公司』\x01",
            "送货……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "那家公司的员工都惊慌失措的，\x01",
            "说是经理失踪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "虽然不知道具体情况……\x01",
            "但我当时费了很大劲才拿到印章。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E31")

    label("loc_3DF7")


    #C0219
    ChrTalk(
        0xFE,
        (
            "那家公司的经理，\x01",
            "到底是怎么了呢？\x01",
            "难道是出去旅行了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E31")

    Jump("loc_4865")

    label("loc_3E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED8")

    #C0220
    ChrTalk(
        0xFE,
        (
            "最近我在开车时，\x01",
            "总是会碰到黑色的搬运车。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "驾驶员是\x01",
            "戴着墨镜的男人，\x01",
            "而且完全不跟人打招呼……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "只是碰到就让人感觉不舒服。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F2A")

    label("loc_3ED8")


    #C0223
    ChrTalk(
        0xFE,
        (
            "那辆搬运车应该是\x01",
            "帝国产的高价车……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "不过……有使用那种车\x01",
            "的运输公司吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2A")

    Jump("loc_4865")

    label("loc_3F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4033")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE7")

    #C0225
    ChrTalk(
        0xFE,
        (
            "最近，卡车货运的往返次数\x01",
            "增加了好几趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "一天就得往返共和国四趟……\x01",
            "就算是开着卡车也吃不消啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "不过，工资也因此涨了不少，\x01",
            "所以没什么好抱怨的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_402E")

    label("loc_3FE7")


    #C0228
    ChrTalk(
        0xFE,
        (
            "最近，卡车货运的往返次数\x01",
            "增加了好几趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "这个工作可不轻松啊。\x02",
    )

    CloseMessageWindow()

    label("loc_402E")

    Jump("loc_4865")

    label("loc_4033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_40A8")

    #C0230
    ChrTalk(
        0xFE,
        "（大吃大喝，狼吞虎咽）……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "…………………………\x01",
            "……唔………………！\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "有、有点吃太多了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4865")

    label("loc_40A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_411E")

    #C0233
    ChrTalk(
        0xFE,
        (
            "通往共和国方向的道路已经修好了，\x01",
            "以后又能继续行车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "（嚼嚼嚼）……\x01",
            "能吃的时候就必须多吃点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4865")

    label("loc_411E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_428C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420B")

    #C0235
    ChrTalk(
        0xFE,
        (
            "我听说共和国那边出事故的卡车，\x01",
            "其实是用来运送走私品的。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "那辆车好像还是莱恩福尔特公司\x01",
            "生产的最新型搬运车……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "……难道，\x01",
            "那并不是一起单纯的事故？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "事不关己……事不关己……\x01",
            "我可不想被牵连进去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4287")

    label("loc_420B")


    #C0239
    ChrTalk(
        0xFE,
        (
            "我听说共和国那边出事故的卡车，\x01",
            "其实是用来运送走私品的。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "难道，那并不是一起单纯的事故吗？\x01",
            "事不关己……事不关己……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4287")

    Jump("loc_4865")

    label("loc_428C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4321")

    #C0241
    ChrTalk(
        0xFE,
        (
            "公司联系我了，说是在共和国那边\x01",
            "处理完卡车事故之前，\x01",
            "暂时没有任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "听说那起事故\x01",
            "好像很严重啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "虽然我并不知道具体情况。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4865")

    label("loc_4321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D9")

    #C0244
    ChrTalk(
        0xFE,
        (
            "（嚼嚼嚼）……共和国那边\x01",
            "好像又发生了一起卡车事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "虽然不知道详细情况，\x01",
            "但共和国的军队好像也出动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "郊外的道路已经被管制，\x01",
            "几乎都无法通行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_440C")

    label("loc_43D9")


    #C0247
    ChrTalk(
        0xFE,
        (
            "（嚼嚼嚼）……看来今天再怎么赶\x01",
            "也回不去了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_440C")

    Jump("loc_4865")

    label("loc_4411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4464")

    #C0248
    ChrTalk(
        0xFE,
        "（嚼嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "最近警备队\x01",
            "好像出动了啊，\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "是在演习吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4865")

    label("loc_4464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_456D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4508")

    #C0251
    ChrTalk(
        0xFE,
        "（嚼嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "我的同伴是\x01",
            "往返于帝国和自治州的卡车送货员。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "虽然我不清楚具体情况，\x01",
            "但听说在那边要穿越国境\x01",
            "可是很麻烦的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4568")

    label("loc_4508")


    #C0254
    ChrTalk(
        0xFE,
        (
            "帝国那边的出入境手续\x01",
            "好像很严格……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "或许因为埃雷波尼亚帝国\x01",
            "是个质朴刚毅的军事大国吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4568")

    Jump("loc_4865")

    label("loc_456D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4622")

    #C0256
    ChrTalk(
        0xFE,
        (
            "共和国那边的国境市\x01",
            "是阿尔泰尔市哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "虽然并不大，\x01",
            "但市民很早之前就和克洛斯贝尔\x01",
            "来往颇多。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔这边的国境门——唐古拉姆门\x01",
            "总是很热闹。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_468F")

    label("loc_4622")


    #C0259
    ChrTalk(
        0xFE,
        (
            "共和国那边的国境市\x01",
            "是阿尔泰尔市哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "沿着东边的路一直走，\x01",
            "走出唐古拉姆门后就到了，\x01",
            "出乎意料地近呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_468F")

    Jump("loc_4865")

    label("loc_4694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4730")

    #C0261
    ChrTalk(
        0xFE,
        "（嚼嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "导力卡车这东西\x01",
            "非常昂贵哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "不过政府现在\x01",
            "会发放补助金。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "多亏如此，我们公司才能\x01",
            "购置了好几辆。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4792")

    label("loc_4730")


    #C0265
    ChrTalk(
        0xFE,
        (
            "购买导力卡车时，\x01",
            "政府会发放补助金。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "因此无论在哪个公司，\x01",
            "导力卡车都成为了主流运输工具。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4792")

    Jump("loc_4865")

    label("loc_4797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4830")

    #C0267
    ChrTalk(
        0xFE,
        "（嚼嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "我是货运卡车的驾驶员哦。\x01",
            "每天往返于克洛斯贝尔与共和国之间。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "这工作实在是很累人。\x01",
            "（嚼嚼嚼）……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4865")

    label("loc_4830")


    #C0270
    ChrTalk(
        0xFE,
        (
            "（嚼嚼嚼）……趁现在有时间，\x01",
            "必须快点填饱肚子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4865")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_3B1D end

    def Function_12_486D(): pass

    label("Function_12_486D")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_495C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4883")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4957")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48E2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_48E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4902")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4952")

    label("loc_4902")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4922")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4952")

    label("loc_4922")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4936")
    Jump("loc_4952")

    label("loc_4936")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4952")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_4952")

    Jump("loc_4883")

    label("loc_4957")

    Jump("loc_495F")

    label("loc_495C")

    Call(0, 13)

    label("loc_495F")

    TalkEnd(0xC)
    Return()

    # Function_12_486D end

    def Function_13_4963(): pass

    label("Function_13_4963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_49D4")

    #C0271
    ChrTalk(
        0xC,
        (
            "欢迎光临，\x01",
            "各位要吃点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "……我或许有当\x01",
            "餐饮店店员的才能哦，\x01",
            "这种感觉最近越来越强！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A99")

    label("loc_49D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A47")

    #C0273
    ChrTalk(
        0xC,
        (
            "我和同伴鲁斯正在\x01",
            "考虑开店的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "……目前还处于准备期，\x01",
            "所以我们才在基层锻炼！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A99")

    label("loc_4A47")


    #C0275
    ChrTalk(
        0xC,
        (
            "每个大人物都有过\x01",
            "在基层锻炼的经历啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "嗯，我将来肯定\x01",
            "也能成为大人物哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A99")

    Return()

    # Function_13_4963 end

    def Function_14_4A9A(): pass

    label("Function_14_4A9A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B2E")
    Jump("loc_4B78")

    label("loc_4B2E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B4E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B78")

    label("loc_4B4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B6E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B78")

    label("loc_4B6E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B78")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4BAE")
    Call(0, 16)
    Jump("loc_5194")

    label("loc_4BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BC9")
    Call(0, 16)
    Jump("loc_4C11")

    label("loc_4BC9")


    #C0277
    ChrTalk(
        0xFE,
        (
            "明天要去问候\x01",
            "工商协会的会长。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "今晚估计睡不着了。\x01",
            "好兴奋……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C11")

    Jump("loc_5194")

    label("loc_4C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBD")

    #C0279
    ChrTalk(
        0xFE,
        (
            "看到纪念庆典的人潮之后，\x01",
            "我脑海中就不断浮现出\x01",
            "许多生意点子。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "嘿嘿，我果然\x01",
            "是个商业天才啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "所以我一定要\x01",
            "成为商人，大放异彩！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D0D")

    label("loc_4CBD")


    #C0282
    ChrTalk(
        0xFE,
        (
            "我果然\x01",
            "是个商业天才啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "我一定要在商界大放异彩，\x01",
            "让人们对我刮目相看！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D0D")

    Jump("loc_5194")

    label("loc_4D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4DA3")

    #C0284
    ChrTalk(
        0xFE,
        (
            "我正在考虑要不要放弃\x01",
            "和同伴一起开店的计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "因为鲁斯那家伙\x01",
            "对小事实在太斤斤计较了。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "做生意应该要\x01",
            "快快乐乐的才对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5194")

    label("loc_4DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4E00")
    SetChrSubChip(0xD, 0x0)

    #C0287
    ChrTalk(
        0xFE,
        "嘁，鲁斯那个不肯听人意见的家伙。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "都说了我继承了爷爷\x01",
            "的经商才能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5194")

    label("loc_4E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4E3E")

    #C0289
    ChrTalk(
        0xFE,
        "我觉得我有当经理的才能。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "你们觉得呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5194")

    label("loc_4E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4EA4")

    #C0291
    ChrTalk(
        0xFE,
        (
            "鲁斯那家伙，\x01",
            "最近满嘴都是大道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "都跟他说了，店都还没开起来，\x01",
            "讲那些也没用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5194")

    label("loc_4EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F15")

    #C0293
    ChrTalk(
        0xFE,
        (
            "鲁斯那家伙，\x01",
            "太喜欢说大道理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "以那种死板僵化的思维，\x01",
            "生意是不可能成功的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F4F")

    label("loc_4F15")


    #C0295
    ChrTalk(
        0xFE,
        (
            "鲁斯那家伙\x01",
            "要是能向我学习，\x01",
            "更加大方洒脱一点就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4F")

    Jump("loc_5194")

    label("loc_4F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4FD3")
    SetChrSubChip(0xD, 0x0)

    #C0296
    ChrTalk(
        0xFE,
        (
            "（狼吞虎咽）……\x01",
            "虽然桑桑只是在店里帮忙，\x01",
            "但她也算是开始做生意了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "所以我们就\x01",
            "更不可能做不到了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5194")

    label("loc_4FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_50C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5087")

    #C0298
    ChrTalk(
        0xFE,
        (
            "我和同伴意见不合，\x01",
            "所以我就去跟一位叫伊安的\x01",
            "律师先生商量了。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "……他却对我很无奈，说是必须\x01",
            "先决定要开办什么样的公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "呵呵，不过确实如此。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50BC")

    label("loc_5087")


    #C0301
    ChrTalk(
        0xFE,
        (
            "如果要办公司的话，必须\x01",
            "先决定要办什么样的公司。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50BC")

    Jump("loc_5194")

    label("loc_50C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5124")
    SetChrSubChip(0xD, 0x0)

    #C0302
    ChrTalk(
        0xFE,
        (
            "也就是说，我果然充满了\x01",
            "当经理的才能啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        "喂，鲁斯，你有在听我说话吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5194")

    label("loc_5124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5194")

    #C0304
    ChrTalk(
        0xFE,
        "我和同伴准备开一家店，然后逐渐做大，\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "最后成为克洛斯贝尔第一的公司！\x01",
            "男人果然必须胸怀大志啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5194")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_4A9A end

    def Function_15_519C(): pass

    label("Function_15_519C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_51F9")

    #C0306
    ChrTalk(
        0xFE,
        (
            "为了筹集开店的启动资金，\x01",
            "所以我们在这里打工。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        "不过时薪低得让人想哭啊。\x02",
    )

    CloseMessageWindow()

    label("loc_51F9")

    TalkEnd(0xFE)
    Return()

    # Function_15_519C end

    def Function_16_51FD(): pass

    label("Function_16_51FD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5291")
    Jump("loc_52DB")

    label("loc_5291")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52B1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52DB")

    label("loc_52B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52D1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52DB")

    label("loc_52D1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52DB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_542E")
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C1")

    #C0308
    ChrTalk(
        0xF,
        (
            "糟、糟糕了，帕库……\x01",
            "我们竟然忘了一件很重要的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xF,
        (
            "想要开店，\x01",
            "必须得有启动资金啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xD,
        "……啊，这么一说的话……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5429")

    label("loc_53C1")


    #C0312
    ChrTalk(
        0xF,
        (
            "啊啊啊啊啊……为什么\x01",
            "你竟然会忘记这么重要的事情啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "说、说什么呢，鲁斯……\x01",
            "你自己不也忘了！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5429")

    Jump("loc_6112")

    label("loc_542E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_550A")
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0314
    ChrTalk(
        0xF,
        "……很好，实在太完美了！\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xF,
        (
            "店名起好了，\x01",
            "要贩卖的商品也决定好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xD,
        "而且经理也定好了！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xD,
        (
            "就叫做帕库＆鲁斯综合商店！\x01",
            "一开始先卖杂货！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xF,
        (
            "很好，明天就要\x01",
            "开始动真格了！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_558F")

    label("loc_550A")


    #C0319
    ChrTalk(
        0xFE,
        (
            "而且最巧的是，\x01",
            "工商协会的会长\x01",
            "刚刚经过这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "并且给我们介绍了批发商。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "女神并没有抛弃我们……\x01",
            "信者果然会得到救赎啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_558F")

    Jump("loc_6112")

    label("loc_5594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_56F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564C")

    #C0322
    ChrTalk(
        0xFE,
        (
            "哼，那些人以前总说我们是\x01",
            "翻不了身的咸鱼，\x01",
            "还说我们一直光说不练……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        "我要用实际行动来证明他们的鼠目寸光。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "哈哈哈，让他们好好\x01",
            "看看我们的真本事！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_56F2")

    label("loc_564C")


    #C0325
    ChrTalk(
        0xFE,
        (
            "……对了，你们知道吗？\x01",
            "纪念庆典的时候有两个\x01",
            "男的来这里住宿。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "哈哈，那两个人都是一脸笨相，\x01",
            "还总喜欢聊一些废话。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "那种人太没前途了，\x01",
            "肯定不会有什么出息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56F2")

    Jump("loc_6112")

    label("loc_56F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_589F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5833")
    SetChrSubChip(0xF, 0x0)

    #C0328
    ChrTalk(
        0xFE,
        (
            "可恶，我们的意见\x01",
            "怎么都不合啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        "帕库，听好啊，我从基础知识开始跟你说！\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "拉面必须是酱油味的，对吧！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    #C0331
    ChrTalk(
        0xD,
        "你在说什么啊，鲁斯……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xD,
        (
            "酱油味肯定不行啊，\x01",
            "拉面绝对应该是味噌味的吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    #C0333
    ChrTalk(
        0xFE,
        (
            "什么……！？\x01",
            "我绝不承认那点！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_589A")

    label("loc_5833")


    #C0334
    ChrTalk(
        0xFE,
        (
            "可恶，我们怎么\x01",
            "就不能说到一起呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "不行……和帕库\x01",
            "一起做生意这种想法，\x01",
            "或许一开始就是错的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_589A")

    Jump("loc_6112")

    label("loc_589F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_59C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597C")
    SetChrSubChip(0xF, 0x0)

    #C0336
    ChrTalk(
        0xFE,
        (
            "我拜读过ＩＢＣ的\x01",
            "库洛伊斯总裁的自传，\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "从中了解到，想要经营一家公司，\x01",
            "必须事先进行周密的计算。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "所以啊，我翻出爷爷\x01",
            "的日记来研究学习了。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xD,
        (
            "可上面写着……\x01",
            "做生意靠的是干劲哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_59C0")

    label("loc_597C")

    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0340
    ChrTalk(
        0xFE,
        (
            "看来我和帕库的爷爷\x01",
            "的观点不一致啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C0")

    Jump("loc_6112")

    label("loc_59C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5AA4")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A83")

    #C0341
    ChrTalk(
        0xFE,
        "我觉得做生意最重要的是信用。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "我们的公司\x01",
            "如此这般……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "所以说，果然应该由我当经理吧。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xD,
        "不对不对，应该是我吧？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xD,
        "因为鲁斯你的眼神太锐利了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A9F")

    label("loc_5A83")


    #C0346
    ChrTalk(
        0xFE,
        "这跟外表有什么关系啊！\x02",
    )

    CloseMessageWindow()

    label("loc_5A9F")

    Jump("loc_6112")

    label("loc_5AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5BC9")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B85")

    #C0347
    ChrTalk(
        0xFE,
        (
            "（狼吞虎咽、大吃大喝）……\x01",
            "帕库，你听好了哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "商品有原价和售价吧，\x01",
            "利润赚的就是售价和原价的差价……\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xD,
        "啊哈哈，鲁斯你这个笨蛋～\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xD,
        "那种事凭干劲就能解决了吧？\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "……能才怪！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BC4")

    label("loc_5B85")


    #C0352
    ChrTalk(
        0xFE,
        (
            "没想到你竟然\x01",
            "笨到了这种地步啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        "也太缺乏常识了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5BC4")

    Jump("loc_6112")

    label("loc_5BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAF")
    SetChrSubChip(0xF, 0x0)

    #C0354
    ChrTalk(
        0xFE,
        (
            "混账，我们一定经常\x01",
            "被他们认为是只会闲聊，\x01",
            "一无是处的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "刚才的那些游客\x01",
            "也一直看着我们笑……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        "帕库，这都是你的错。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        "才不是，这是鲁斯你的错。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xD,
        "你也不看看你自己那乱七八糟的头发。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5CF0")

    label("loc_5CAF")


    #C0359
    ChrTalk(
        0xFE,
        "我和同伴说话说不到一起。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "帕库那家伙，\x01",
            "到底想不想干啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF0")

    Jump("loc_6112")

    label("loc_5CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5E61")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD9")

    #C0361
    ChrTalk(
        0xFE,
        "（狼吞虎咽、大吃大喝）……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    #C0362
    ChrTalk(
        0xFE,
        (
            "帕库，那个包子是我的吧？\x01",
            "你别随便吃啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xD,
        "（狼吞虎咽、大吃大喝）……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "你自己不也一样，别把饺子都吃光了啊。\x01",
            "吃太多会口臭的吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E5C")

    label("loc_5DD9")


    #C0365
    ChrTalk(
        0xFE,
        (
            "桑桑从以前开始就一直很有亲和力。\x01",
            "她从事服务业实在是再合适不过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "先别说桑桑的事了，\x01",
            "我想说的是……\x01",
            "（狼吞虎咽）……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E5C")

    Jump("loc_6112")

    label("loc_5E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5FA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F47")
    SetChrSubChip(0xF, 0x0)

    #C0367
    ChrTalk(
        0xFE,
        (
            "现在克洛斯贝尔\x01",
            "最热门的商品是……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "导力车！\x02",
    )


    #C0369
    ChrTalk(
        0xD,
        "彩虹剧团的门票！\x02",
    )

    OP_57(0x1)
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0370
    ChrTalk(
        0xFE,
        (
            "喂喂，帕库……\x01",
            "你不会想去做黄牛党吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xD,
        (
            "你不知道吗？\x01",
            "彩虹剧团的门票可是\x01",
            "非常抢手的哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5FA1")

    label("loc_5F47")


    #C0372
    ChrTalk(
        0xFE,
        (
            "但果然还是\x01",
            "帅气的导力车比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "导力车是男人的浪漫……\x01",
            "你们应该也是这么想的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA1")

    Jump("loc_6112")

    label("loc_5FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6045")
    SetChrSubChip(0xF, 0x0)

    #C0374
    ChrTalk(
        0xFE,
        (
            "（刚才坐在后面座位上的\x01",
            "　姐姐很漂亮啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xD,
        "喂，鲁斯，你有在听我说话吗！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0376
    ChrTalk(
        0xFE,
        (
            "哎？有啊……\x01",
            "你在说什么来着？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6112")

    label("loc_6045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6112")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E6")

    #C0377
    ChrTalk(
        0xFE,
        (
            "#1P要创办公司，\x01",
            "首先必须决定的是……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        "#2P经理！\x02",
    )


    #C0379
    ChrTalk(
        0xFE,
        "#1P公司名！\x02",
    )

    OP_57(0x1)

    #C0380
    ChrTalk(
        0xFE,
        "#1P……喂，是公司名吧？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        "#2P不对不对，是经理。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6112")

    label("loc_60E6")


    #C0382
    ChrTalk(
        0xFE,
        (
            "喂，帕库，你不会是\x01",
            "自己想当\x01",
            "经理吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6112")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_51FD end

    def Function_17_611A(): pass

    label("Function_17_611A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61AE")
    Jump("loc_61F8")

    label("loc_61AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61F8")

    label("loc_61CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61F8")

    label("loc_61EE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61F8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0383
    ChrTalk(
        0xFE,
        (
            "#1806F呼，就没有租金\x01",
            "便宜点的地方吗……\x02\x03",

            "#1802F市政厅说的地方……\x01",
            "应该就是这附近了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_611A end

    def Function_18_6285(): pass

    label("Function_18_6285")

    Call(0, 19)
    Return()

    # Function_18_6285 end

    def Function_19_6289(): pass

    label("Function_19_6289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6651")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6389")

    #C0384
    ChrTalk(
        0x13,
        (
            "……前辈您为什么会成为\x01",
            "克洛斯贝尔时代周刊的记者呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x12,
        (
            "#2102F嗯～我想想啊，\x01",
            "应该是因为喜欢看热闹吧？\x02\x03",

            "#2109F像名人的花边新闻啦、\x01",
            "政界的丑闻啦，\x01",
            "都让人兴趣盎然啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0386
    ChrTalk(
        0x13,
        (
            "您真是诚实得让人\x01",
            "喜欢啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6649")

    label("loc_6389")


    #C0387
    ChrTalk(
        0x12,
        (
            "#2105F（嚼嚼嚼）……\x01",
            "哎～你还有个双胞胎哥哥啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x13,
        (
            "哈哈哈……他现在\x01",
            "在奥雷德自治州从事农业工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x13,
        (
            "我孤身一人来这里，\x01",
            "就是为了当记者。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64D7")

    #C0390
    ChrTalk(
        0x102,
        (
            "#0100F（格蕾丝小姐……\x01",
            "　好像正在和同事吃饭啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#0003F（还是别和她打招呼了，不然的话，\x01",
            "　琪雅的事情一定会让她追问不休的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x102,
        "#0106F（也、也是哦……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6646")

    label("loc_64D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6592")

    #C0393
    ChrTalk(
        0x103,
        (
            "#0200F（格蕾丝小姐……\x01",
            "　好像正在和同事吃饭啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#0003F（还是别和她打招呼了，不然的话，\x01",
            "　琪雅的事情一定会让她追问不休的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x103,
        "#0211F（可以想象……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6646")

    label("loc_6592")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6646")

    #C0396
    ChrTalk(
        0x104,
        (
            "#0300F（是格蕾丝小姐啊……\x01",
            "　好像正在和同事吃饭。）\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#0003F（还是别和她打招呼了，不然的话，\x01",
            "　琪雅的事情一定会让她追问不休的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        "#0309F（也是……）\x02",
    )

    CloseMessageWindow()

    label("loc_6646")

    SetScenarioFlags(0x1, 1)

    label("loc_6649")

    TalkEnd(0xFE)
    Jump("loc_6662")

    label("loc_6651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6662")
    Call(0, 30)

    label("loc_6662")

    Return()

    # Function_19_6289 end

    def Function_20_6663(): pass

    label("Function_20_6663")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66F7")
    Jump("loc_6741")

    label("loc_66F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6717")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6741")

    label("loc_6717")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6737")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6741")

    label("loc_6737")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6741")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_686B")

    #C0399
    ChrTalk(
        0x103,
        "#0205F科长……您怎么会在这里？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x11,
        (
            "#1000F哟，是你们啊。\x02\x03",

            "怎么样，调查还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#0100F嗯，还算顺利吧。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        (
            "#0000F我们接下来\x01",
            "准备去乌尔斯拉\x01",
            "医科大学。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x11,
        (
            "#1000F呵呵，很有干劲嘛。\x02\x03",

            "#1003F嗯，你们自己加油啊。\x01",
            "调查完了再来给我报告。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_68F6")

    label("loc_686B")


    #C0404
    ChrTalk(
        0x11,
        (
            "#1000F这里的饭菜很好吃哦，\x01",
            "你们午饭吃了没？没吃的话就吃点再走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x101,
        "#0000F不用了，我们都吃过了……\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x104,
        "#0300F科长好悠闲自得啊……\x02",
    )

    CloseMessageWindow()

    label("loc_68F6")

    SetChrSubChip(0x11, 0x0)
    TalkEnd(0x11)
    Return()

    # Function_20_6663 end

    def Function_21_68FE(): pass

    label("Function_21_68FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6B7D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_699B")
    Jump("loc_69E5")

    label("loc_699B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69E5")

    label("loc_69BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69E5")

    label("loc_69DB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_69E5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6A83")

    #C0407
    ChrTalk(
        0xFE,
        (
            "采购七耀石的结晶，\x01",
            "是我为追上作为成功商人的父亲\x01",
            "所迈出的第一步……！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "玩也玩够了，\x01",
            "该开始创业了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B71")

    label("loc_6A83")


    #C0409
    ChrTalk(
        0xFE,
        (
            "呵呵，我已经在克洛斯贝尔\x01",
            "玩够了……\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "差不多\x01",
            "也该去采购\x01",
            "『七耀石的结晶』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "城市的西出口那边好像\x01",
            "有前往矿山镇玛因兹的定期巴士哦。\x01",
            "只要乘坐就能轻松去玛因兹了。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "为了追上身为成功商人\x01",
            "的父亲……！\x01",
            "我终于要迈出第一步了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_6B71")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_6CFD")

    label("loc_6B7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6BDF")

    #C0413
    ChrTalk(
        0xFE,
        (
            "我从空港来这里的时候，\x01",
            "看到了一家很大的百货商店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        "就先去那里看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CFA")

    label("loc_6BDF")

    OP_4B(0x15, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x14, 0x15, 0)
    TurnDirection(0x15, 0x14, 0)

    #C0415
    ChrTalk(
        0x14,
        "接下来的一个月，就用来做市场调查吧。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x14,
        "总之就先在市内走走逛逛吧……\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x15,
        "哎……？\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x15,
        (
            "那个……小姐。\x01",
            "七耀石的采购\x01",
            "要怎么办啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x14,
        "哎？你在说什么啊。\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x14,
        (
            "难得来到了\x01",
            "遥远的克洛斯贝尔，\x01",
            "只做生意岂不是太可惜。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x15,
        "（还是一心想着游玩啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    OP_4C(0x15, 0xFF)
    OP_4C(0x14, 0xFF)

    label("loc_6CFA")

    TalkEnd(0xFE)

    label("loc_6CFD")

    Return()

    # Function_21_68FE end

    def Function_22_6CFE(): pass

    label("Function_22_6CFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6D7C")

    #C0422
    ChrTalk(
        0xFE,
        (
            "……我们原本是来克洛斯贝尔\x01",
            "采购商品的，\x01",
            "结果却游玩了一个月。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "在帝国那边的宅邸\x01",
            "现在不知道怎样了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E03")

    label("loc_6D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6DF2")

    #C0424
    ChrTalk(
        0xFE,
        (
            "我本想直接去采购七耀石，\x01",
            "成交之后就马上回去的……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "但小姐看起来好像\x01",
            "还想再玩一段时间后再去……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E03")

    label("loc_6DF2")

    TurnDirection(0x14, 0x15, 0)
    TurnDirection(0x15, 0x14, 0)
    Call(0, 21)

    label("loc_6E03")

    TalkEnd(0xFE)
    Return()

    # Function_22_6CFE end

    def Function_23_6E07(): pass

    label("Function_23_6E07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7065")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6F2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_6E87")

    #C0426
    ChrTalk(
        0x16,
        (
            "诗人之路吗……\x01",
            "这或许可行。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x16,
        (
            "虽然来这里之后受过一次挫折……\x01",
            "但我还是再试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F2A")

    label("loc_6E87")


    #C0428
    ChrTalk(
        0x16,
        (
            "……很久没失恋过了，\x01",
            "所以这次的打击让我颓废不堪。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x16,
        (
            "我说，利库斯。\x01",
            "我到底\x01",
            "该怎么做才好啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        (
            "#0006F（虽然令人同情……\x01",
            "　但现在还是让他静一静吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_6F2A")

    Jump("loc_7060")

    label("loc_6F2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6F44")
    Call(0, 29)
    Jump("loc_7060")

    label("loc_6F44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6FDF")

    #C0431
    ChrTalk(
        0x16,
        (
            "实在没想到在最后的一站\x01",
            "竟然会遇到她的姐姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x16,
        (
            "利库斯，这一定\x01",
            "是命运的安排。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x16,
        (
            "我和她的相遇是命中注定的。\x01",
            "哈哈哈，真开心啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7060")

    label("loc_6FDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6FF4")
    Call(0, 28)
    Jump("loc_7060")

    label("loc_6FF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7008")
    Call(0, 27)
    Jump("loc_7060")

    label("loc_7008")


    #C0434
    ChrTalk(
        0x16,
        (
            "喂，利库斯，\x01",
            "我觉得我的愿望这次就会实现了。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x16,
        (
            "现在她正在哪里，\x01",
            "又在做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7060")

    Jump("loc_70FF")

    label("loc_7065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_70A6")

    #C0436
    ChrTalk(
        0xFE,
        (
            "不知姓名的女孩……\x01",
            "她现在正在哪里做着什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FF")

    label("loc_70A6")


    #C0437
    ChrTalk(
        0xFE,
        (
            "被全世界所抛弃的我，\x01",
            "终于迎来了一位天使。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "现在她正在哪里，\x01",
            "又在做什么呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_70FF")

    TalkEnd(0xFE)
    Return()

    # Function_23_6E07 end

    def Function_24_7103(): pass

    label("Function_24_7103")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7372")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_718B")

    #C0439
    ChrTalk(
        0x17,
        "打起精神啊，安敦。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x17,
        (
            "不管怎么说，\x01",
            "你还有诗人之路\x01",
            "可以走啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x17,
        (
            "现在的你或许可以\x01",
            "写出悲恋之诗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_736D")

    label("loc_718B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_71F1")

    #C0442
    ChrTalk(
        0x17,
        (
            "安敦好像一直\x01",
            "在焦急地等着你们的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x17,
        (
            "这么想见的话，\x01",
            "自己去见她不就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_736D")

    label("loc_71F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_72A3")

    #C0444
    ChrTalk(
        0x17,
        (
            "安敦非常相信命运这种东西。\x01",
            "所以他总是不自己努力，\x01",
            "而是一心等待上天的眷顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x17,
        (
            "他和那女孩要是真的有缘，\x01",
            "只要他自己去一趟警察局，\x01",
            "现在应该都已经见到面了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_736D")

    label("loc_72A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7317")

    #C0446
    ChrTalk(
        0x17,
        (
            "我们决定还要在\x01",
            "这里待三个星期。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x17,
        (
            "和安敦在一起，\x01",
            "总会发生一些无法预料的事，\x01",
            "非常有意思哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_736D")

    label("loc_7317")


    #C0448
    ChrTalk(
        0x17,
        (
            "虽然不知道他们会不会受理，\x01",
            "总之我已经发出委托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x17,
        (
            "我觉得耐心等待\x01",
            "也很重要。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_736D")

    Jump("loc_7476")

    label("loc_7372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_73DE")

    #C0450
    ChrTalk(
        0xFE,
        (
            "我们正在寻找一个帮助安敦\x01",
            "找到钱包的女孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "不问姓名就跟人家道别，\x01",
            "还真像安敦的作风。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7476")

    label("loc_73DE")


    #C0452
    ChrTalk(
        0xFE,
        (
            "一个路过的女孩\x01",
            "很热心地帮助\x01",
            "安敦找到了钱包。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xFE,
        (
            "然后安敦就觉得\x01",
            "他和那女孩的相遇是命中注定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "还推迟了回国时间，\x01",
            "留在这里寻找那个女孩。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)

    label("loc_7476")

    TalkEnd(0xFE)
    Return()

    # Function_24_7103 end

    def Function_25_747A(): pass

    label("Function_25_747A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_750E")
    Jump("loc_7558")

    label("loc_750E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_752E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7558")

    label("loc_752E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_754E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7558")

    label("loc_754E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7558")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_75E9")

    #C0455
    ChrTalk(
        0x18,
        (
            "#1602F传说中的杀手吗……真有趣。\x02\x03",

            "要是他敢来我们的地盘，\x01",
            "我还真想跟他交手看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7710")

    label("loc_75E9")


    #C0456
    ChrTalk(
        0x18,
        (
            "#1603F那些就是\x01",
            "『黑月』的人吧……\x02\x03",

            "#1600F那帮东方人最近\x01",
            "好像很嚣张啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        "#0005F你从哪里听说的……\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#0301F这件事好像已经\x01",
            "在各处传开了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x18,
        (
            "#1602F哼，旧城区这里\x01",
            "可是有很多情报来源的。\x02\x03",

            "#1604F还听说他们雇佣了\x01",
            "很厉害的杀手……呵呵。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#0006F……拜托你，\x01",
            "一定不要去挑衅他们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_7710")

    Jump("loc_78D3")

    label("loc_7715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7785")

    #C0461
    ChrTalk(
        0x18,
        (
            "#1603F哼……我从早上就\x01",
            "开始训练那些小兔崽子了，\x01",
            "现在肚子饿得要死。\x02\x03",

            "#1600F嘁，还不赶快上菜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78D3")

    label("loc_7785")


    #C0462
    ChrTalk(
        0x18,
        "#1600F啊，原来是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#0000F是你啊……\x01",
            "你经常来这家店吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x18,
        (
            "#1603F哼，算是吧。\x01",
            "虽然老板很啰嗦，\x01",
            "但饭菜味道不错。\x02\x03",

            "#1602F呵呵，而且服务员\x01",
            "挺有魅力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        "#0309F哦哦，这个我有同感。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    #C0466
    ChrTalk(
        0x102,
        "#0106F真是……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#0211F兰迪前辈，\x01",
            "你也太没节操了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_78D3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_747A end

    def Function_26_78DB(): pass

    label("Function_26_78DB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_796F")
    Jump("loc_79B9")

    label("loc_796F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_798F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79B9")

    label("loc_798F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79AF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79B9")

    label("loc_79AF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_79B9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7B09")

    #C0468
    ChrTalk(
        0x19,
        (
            "哦～用钉棍～教训他们～！\x01",
            "血洗圣书会啊啊～啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x19,
        "……（狼吞虎咽）\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x19,
        (
            "嗯～甜品就点\x01",
            "布丁吧～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AF9")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0471
    ChrTalk(
        0x101,
        (
            "#0006F（到底要唱歌、吃饭还是点菜，\x01",
            "　你倒是确定一下啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AF9")

    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x19, 0x1)
    TalkEnd(0xFE)
    Return()

    label("loc_7B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7B6C")

    #C0472
    ChrTalk(
        0x19,
        "话说肚子好饿啊～\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x19,
        (
            "哦哦，呀呀，肚子饿了哦～！\x01",
            "快点～把菜～端上来啊～……唔！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BAE")

    label("loc_7B6C")


    #C0474
    ChrTalk(
        0x19,
        "什么啊，原来是警察啊？\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x19,
        (
            "哎呀，你们可不要\x01",
            "妨碍我们哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_7BAE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_78DB end

    def Function_27_7BB6(): pass

    label("Function_27_7BB6")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x17, 0xFF)
    OP_68(-100600, 1420, -53410, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -100000, 20, -53500, 180)
    SetChrPos(0x102, -100750, 20, -53000, 180)
    SetChrPos(0x103, -99250, 20, -52000, 180)
    SetChrPos(0x104, -101000, 20, -52000, 180)
    SetChrPos(0x109, -99500, 20, -51000, 180)
    OP_93(0x16, 0x10E, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    #C0476
    ChrTalk(
        0x16,
        "#12P爱德丝女神，我诚心向您祷告……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x16,
        (
            "#12P求您保佑我与那位可爱的女孩\x01",
            "再次相遇吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#5P#0000F那个……\x01",
            "您是安敦先生吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)

    #C0479
    ChrTalk(
        0x16,
        (
            "#12P嗯，我是……\x01",
            "你们是？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        (
            "#5P#0000F我们是克洛斯贝尔警察局·特别任务支援科的人。\x01",
            "因为看到了您的委托，所以前来拜访……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0481
    ChrTalk(
        0x16,
        (
            "#12P哦哦……！\x01",
            "我等你们好久了。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x16,
        (
            "#12P我的委托\x01",
            "很紧急，\x01",
            "你们愿意听一听吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        "#5P#0000F好的，您请说。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        (
            "#5P#0100F从委托说明上来看……\x01",
            "您是想让我们帮忙\x01",
            "寻找一位女孩吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x16,
        (
            "#12P对对，我想找到那位女孩……\x01",
            "然后好好感谢她。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x16,
        (
            "#12P是她把我从\x01",
            "黑暗深渊中拯救出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#5P#0001F……听起来，似乎是有什么内情吧？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x16,
        (
            "#12P我是利贝尔王国的人，\x01",
            "和朋友利库斯一起\x01",
            "来克洛斯贝尔旅行。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        (
            "#12P我的人生总是暗淡无光……\x01",
            "所以抱着看看会不会有所改变的想法，\x01",
            "来到了这种繁华的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        "#5P#0003F这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x16,
        (
            "#12P然而……\x01",
            "在这里等待我的，\x01",
            "最终却还是冰冷的现实。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x16,
        (
            "#12P我竟然……\x01",
            "我竟然把放有旅费的\x01",
            "钱包丢失了。\x02",
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

    #C0493
    ChrTalk(
        0x101,
        "#5P#0006F这个，您还真是不幸啊……\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x16,
        (
            "#12P……嗯，没错。\x01",
            "我就是个既迟钝\x01",
            "又没用的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "#12P虽然利库斯\x01",
            "也帮忙找了，\x01",
            "但还是没能找到钱包。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x16,
        (
            "#12P感到绝望的我已经放弃寻找，\x01",
            "准备向利库斯借点钱，\x01",
            "就这样回利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x16,
        (
            "#12P就在那时……\x01",
            "那位女孩温柔地\x01",
            "向我伸出了援手。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x104,
        (
            "#5P#0300F哎……这可真让人羡慕啊。\x01",
            "那么好的女孩可不常见。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x16,
        (
            "#12P是啊，然后……\x01",
            "多亏了她，我才能顺利找回\x01",
            "丢失的钱包。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x16,
        (
            "#12P那个时候我就确信了，\x01",
            "这次相遇是命中注定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x16,
        (
            "#12P她对我这个身陷黑暗的人\x01",
            "伸出援手，拯救了我的心。\x01",
            "简直就如同天使一般啊……\x02",
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

    #C0502
    ChrTalk(
        0x101,
        (
            "#5P#0006F那、那个……\x01",
            "总之，您的意思就是要我们\x01",
            "帮忙找出那个女孩，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x16,
        "#12P嗯，没错。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "#12P虽然我们决定\x01",
            "在这里多待三个星期来寻找她，\x01",
            "但却毫无头绪。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x16,
        (
            "#12P之前虽然去\x01",
            "委托游击士协会，\x01",
            "不过被拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x16,
        (
            "#12P说这并不是什么紧急的失踪案件，\x01",
            "所以他们想优先完成\x01",
            "其它重要的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "#12P真是的，如果是利贝尔的游击士，\x01",
            "连和人拼酒这种委托\x01",
            "都会帮……忙呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_64(0x16)

    #C0508
    ChrTalk(
        0x101,
        (
            "#5P#0005F…………\x01",
            "请问您怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x16,
        (
            "#12P……没什么，稍微戳到旧伤了。\x01",
            "算、算了，先不说这个……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x16,
        (
            "#12P利库斯在街上听说了支援科，\x01",
            "所以他就替我\x01",
            "向你们提出了委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x16,
        (
            "#12P你们虽然是警察，但服务性质\x01",
            "也跟游击士差不多吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x16,
        "#12P你们会接受我的委托吧？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#5P#0006F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x109,
        (
            "#5P#0505F……特别任务支援科\x01",
            "连这种事都要帮忙吗？\x02\x03",

            "#0500F那个……工作范围\x01",
            "还真广泛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x102,
        (
            "#5P#0106F这种委托\x01",
            "比较少见……\x02\x03",

            "#0100F罗伊德，怎么办？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x103,
        (
            "#11P#0203F……说实话，像恋爱烦恼\x01",
            "这种事，警察好像不太方便管。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x101,
        "#5P#0003F（嗯，也是……）\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x104,
        (
            "#5P#0304F不过我想至少\x01",
            "看看那个女孩长什么样子啊。\x02\x03",

            "#0300F……请问一下，那女孩\x01",
            "大概是什么类型的呢？\x02\x03",

            "#0309F应该是很可爱\x01",
            "的类型吧¤\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x16,
        (
            "#12P是啊，她那美丽的身姿\x01",
            "至今仍在我心中挥之不去。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x16,
        (
            "#12P她那亲切温和的气质\x01",
            "能滋润他人荒芜的心。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x16,
        (
            "#12P而且就连说话方式\x01",
            "也透着温柔。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x16,
        (
            "#12P还有，她梳成两束的粉褐色头发\x01",
            "充溢着可爱的感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0523
    ChrTalk(
        0x101,
        (
            "#5P#0005F啊，听这形容，感觉好像\x01",
            "有点熟悉啊，难道是认识的人吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x102,
        "#5P#0103F对啊……\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x103,
        (
            "#11P#0200F经你这么一说，\x01",
            "感觉好像还见过对方很多次呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x104,
        (
            "#5P#0306F我说……无论怎么想，\x01",
            "他说的不就是小芙兰吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0527
    ChrTalk(
        0x109,
        "#5P#0505F啊……很有可能！\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x16,
        (
            "#12P……你、你们……！\x01",
            "你们认识她吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x109,
        (
            "#5P#0503F那个，可能性应该很高吧……\x02\x03",

            "#0500F话说回来，您刚才说的\x01",
            "粉褐色头发……\x01",
            "是不是和我的头发颜色一样呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x16, 0x109, 500)
    Sleep(500)

    #C0530
    ChrTalk(
        0x16,
        "#12P啊啊、啊啊啊啊啊！！！\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x16,
        (
            "#12P确实是一样的！\x01",
            "她的发色和你相同呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x16,
        (
            "#12P啊！！\x01",
            "难道你是……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0533
    ChrTalk(
        0x109,
        (
            "#5P#0503F那、那个，\x01",
            "如果没弄错的话……\x01",
            "那个女孩应该就是我的妹妹。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x16,
        "#12P什么……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x17, 500)

    #C0535
    ChrTalk(
        0x16,
        (
            "#12P哈哈，你听到了吗，利库斯。\x01",
            "这毫无疑问是命运的安排啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)

    #C0536
    ChrTalk(
        0x17,
        (
            "#5P既然你这么认为，\x01",
            "那应该就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x17,
        (
            "#5P虽然也不能否定\x01",
            "其它可能性。\x02",
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
    Sleep(500)
    TurnDirection(0x16, 0x109, 500)

    #C0538
    ChrTalk(
        0x16,
        (
            "#12P那、那那那那那那个……\x01",
            "姐姐！！\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x109,
        "#5P#0505F什、什什什什什么！？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x16,
        (
            "#12P您妹妹，那个……\x01",
            "有恋人或\x01",
            "男朋友吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x109,
        (
            "#5P#0505F咦、咦咦咦！？\x02\x03",

            "#0503F没、没有吧，\x01",
            "我没听她说过。\x02\x03",

            "#0508F不过，\x01",
            "我现在没和她住在一起，\x01",
            "所以也不确定……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x16,
        (
            "#12P总、总之……\x01",
            "在回利贝尔之前，\x01",
            "我想当面向她表示感谢！\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x16,
        (
            "#12P能不能请您问问她，\x01",
            "看她愿不愿意跟我见个面！？\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x109,
        "#5P#0503F这、这个啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0545
    ChrTalk(
        0x109,
        (
            "#5P#0500F……罗伊德警官，\x01",
            "我可以接受吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2A, 0x1, 0x0)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FED")

    #C0546
    ChrTalk(
        0x101,
        (
            "#5P#0000F我知道了，\x01",
            "那就接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x16,
        "#12P哦哦！太感谢你们了！\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x16,
        (
            "#12P那、那就拜托你们了哦。\x01",
            "请务必让她\x01",
            "见我一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        (
            "#5P#0003F这样的话，\x01",
            "我们就快点去\x01",
            "警察局总部吧。\x02\x03",

            "#0000F她现在应该\x01",
            "在接待处。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x109,
        (
            "#5P#0500F嗯，说得也是呢。\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0551
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【真心的报恩】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2A, 0x1, 0x1)
    Jump("loc_9171")

    label("loc_8FED")


    #C0552
    ChrTalk(
        0x101,
        (
            "#5P#0006F那个，实在不好意思，\x01",
            "我们暂时还有别的\x01",
            "事情要办……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x16,
        (
            "#12P……这样啊，\x01",
            "果然是这种结果。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x16,
        (
            "#12P总是这样，\x01",
            "谁都不愿意听我说话。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x16,
        (
            "#12P唉，即使听我说话了，\x01",
            "也永远不会有\x01",
            "好结果……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        (
            "#5P#0012F那、那个……\x01",
            "您也不必这么沮丧。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x109,
        (
            "#5P#0505F是、是啊。\x01",
            "我们并没有\x01",
            "拒绝您……\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x16,
        (
            "#12P……没事，\x01",
            "你们不用管我。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x16,
        (
            "#12P不过说得也是，\x01",
            "虽然不抱希望，但我还是等着你们回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9171")

    SetChrPos(0x0, -100000, 20, -53500, 180)
    OP_93(0x16, 0x10E, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_27_7BB6 end

    def Function_28_91A1(): pass

    label("Function_28_91A1")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x17, 0xFF)
    OP_68(-100600, 1420, -53410, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -100000, 20, -53500, 180)
    SetChrPos(0x102, -100750, 20, -53000, 180)
    SetChrPos(0x103, -99250, 20, -52000, 180)
    SetChrPos(0x104, -101000, 20, -52000, 180)
    SetChrPos(0x109, -99500, 20, -51000, 180)
    OP_93(0x16, 0x0, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    #C0560
    ChrTalk(
        0x16,
        "#12P……是警察吗？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x16,
        (
            "#12P这样啊……\x01",
            "你们真的回来帮我了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x101,
        "#5P#0005F是、是啊。\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x16,
        (
            "#12P那么，那女孩……\x01",
            "是叫做芙兰吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x16,
        (
            "#12P能不能请你们……\x01",
            "拜托她见我一面呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94A9")

    #C0565
    ChrTalk(
        0x101,
        (
            "#5P#0000F我知道了，\x01",
            "那我们就接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x16,
        "#12P……哦哦，真的吗！\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x16,
        "#12P真的吗真的吗真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#5P#0005F嗯、嗯，当然了。\x02\x03",

            "#0003F（刚才明明就是一副\x01",
            "　快要世界末日的表情……)\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x16,
        (
            "#12P那、那就拜托你们了，\x01",
            "请务必让她\x01",
            "见我一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        (
            "#5P#0000F这样的话，\x01",
            "那我们就赶快\x01",
            "去警察局总部吧。\x02\x03",

            "她现在应该\x01",
            "在接待处。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x109,
        (
            "#5P#0500F嗯，说得也是呢，\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2A, 0x1, 0x1)
    Jump("loc_95D0")

    label("loc_94A9")


    #C0572
    ChrTalk(
        0x101,
        (
            "#5P#0006F那、那个，不好意思，\x01",
            "我们现在还有事……\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x16,
        (
            "#12P……没事，没关系，\x01",
            "我已经习惯了。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x16,
        (
            "#12P总是这样。\x01",
            "每当我想做些什么，\x01",
            "总是不会有好结果。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        (
            "#5P#0006F（真、真是位麻烦的人啊……）\x02\x03",

            "#0000F不、不好意思。\x01",
            "等我们有空了就回来帮你。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x16,
        "#12P……虽然不抱希望，但我还是等着你们回来。\x02",
    )

    CloseMessageWindow()

    label("loc_95D0")

    SetChrPos(0x0, -100000, 20, -53500, 180)
    OP_93(0x16, 0x10E, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_91A1 end

    def Function_29_9600(): pass

    label("Function_29_9600")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x17, 0xFF)
    OP_68(-100600, 1420, -53410, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -100000, 20, -53500, 180)
    SetChrPos(0x109, -100750, 20, -53000, 180)
    SetChrPos(0x102, -99250, 20, -52000, 180)
    SetChrPos(0x103, -101000, 20, -52000, 180)
    SetChrPos(0x104, -99500, 20, -51000, 180)
    OP_93(0x16, 0x0, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    #C0577
    ChrTalk(
        0x101,
        "#5P#0000F那个，安敦先生。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x16,
        "#12P啊，是你们……\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x16,
        (
            "#12P怎、怎么样了？\x01",
            "芙兰小姐愿意见我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x101,
        (
            "#5P#0003F关于这件事……\x01",
            "好像没问题了。\x02\x03",

            "#0000F再过一会就是她的休息时间，\x01",
            "所以她想约你到时在\x01",
            "中央广场的西餐厅见面……\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x16,
        "#12P哦、哦哦……\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x16,
        (
            "#12P谢、谢谢你们。\x01",
            "实在是不胜感激啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x16,
        (
            "#12P啊，我竟然也能迎来\x01",
            "这么美好的一天……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        "#5P#0200F……看来已经高兴得忘乎所以了。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x102,
        "#5P#0100F呵呵，真是太好了呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0586
    ChrTalk(
        0x16,
        (
            "#12P对了，我必须送点\x01",
            "礼物给芙兰小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x16,
        "#12P我还什么都没准备啊。\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x104,
        (
            "#5P#0306F喂喂，想和女士约会，\x01",
            "却连礼物都不事先准备好，前途堪忧啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x16,
        (
            "#12P因为我实在是\x01",
            "没想到这么快就能见面啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x16,
        "#12P……对了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x109, 500)

    #C0591
    ChrTalk(
        0x16,
        (
            "#12P那、那个，姐姐。\x01",
            "您能陪我去\x01",
            "一趟百货商店吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x109,
        "#5P#0505F去百货商店……吗？\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x16,
        (
            "#12P我想选一个\x01",
            "芙兰小姐\x01",
            "喜欢的礼物！\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x16,
        (
            "#12P如果姐姐您\x01",
            "能将她的喜好告诉我，\x01",
            "那一定会万无一失的！\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x109,
        (
            "#5P#0508F……说、说得也是呢。\x02\x03",

            "#0506F不过，\x01",
            "能不能请您\x01",
            "别叫我『姐姐』……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)

    #C0596
    ChrTalk(
        0x16,
        (
            "#12P你们……\x01",
            "一定会帮我\x01",
            "挑选礼物的吧？\x02",
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

    #C0597
    ChrTalk(
        0x101,
        (
            "#5P#0006F唔……\x01",
            "（别用那种可怜兮兮\x01",
            "　的眼神看我啊……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x103,
        (
            "#5P#0203F……事情好像\x01",
            "变得很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x101,
        (
            "#5P#0006F（……呼，真没办法……\x01",
            "　看这样子，也只能奉陪到\x01",
            "　他满意为止了。）\x02\x03",

            "#0000F那么……\x01",
            "我们就先去一趟\x01",
            "百货店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x16,
        (
            "#12P嗯，\x01",
            "拜托你们了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5E, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_9600 end

    def Function_30_9C15(): pass

    label("Function_30_9C15")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch06000.itc", 0x22)
    LoadChrToIndex("apl/ch50090.itc", 0x23)
    SoundLoad(827)
    OP_68(4900, 1000, 6400, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 4800, 0, 5400, 0)
    SetChrPos(0x102, 6100, 0, 4800, 315)
    SetChrPos(0x103, 4400, 0, 4100, 0)
    SetChrPos(0x104, 6600, 0, 6200, 270)
    SetChrPos(0x12, 4900, 100, 7100, 270)
    SetChrSubChip(0x12, 0x1)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0601
    AnonymousTalk(
        0x12,
        (
            "呵呵¤\x01",
            "你们果然来了啊。\x02\x03",

            "来，坐吧坐吧。\x01",
            "姐姐请你们吃饭哦¤\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0602
    ChrTalk(
        0x101,
        (
            "#12P#0006F那个……\x01",
            "吃饭就不必了。\x02\x03",

            "#0001F还请把详细情况告诉我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x12,
        (
            "#2101F#5P什么呀～吃顿饭又没关系。\x02\x03",

            "#2102F或者说……『我们可不会像警察局的\x01",
            "高层领导一样收受贿赂』，\x01",
            "是这个意思吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0604
    ChrTalk(
        0x101,
        "#12P#0005F什么……\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x104,
        (
            "#0303F我可没那样想。\x02\x03",

            "#0302F您要是请客，我就欣然接受啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x103,
        (
            "#2P#0204F我也无所谓……\x01",
            "如果您不是在做人情的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x102,
        (
            "#0103F嗯，也是……\x02\x03",

            "#0100F一般来说，\x01",
            "吃顿饭应该没问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x101,
        "#12P#0011F唔……\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x12,
        (
            "#2102F#5P呵呵，有精神洁癖的\x01",
            "好像只有罗伊德你哦。\x02\x03",

            "#2109F太过死板的话，\x01",
            "可无法成为一名优秀的搜查官哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#12P#0013F唔……我知道啦！\x02\x03",

            "#0003F不过不能喝酒！\x01",
            "那样我们就接受您的邀请！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x7D0)
    OP_68(3200, 1000, 7100, 0)
    MoveCamera(54, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 1500, 100, 6500, 90)
    SetChrPos(0x102, 1500, 100, 7600, 90)
    SetChrPos(0x103, 3200, 100, 5500, 0)
    SetChrPos(0x104, 3200, 100, 8900, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x12, 4900, 100, 7100, 270)
    SetChrSubChip(0x12, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x3, 0x1C)
    OP_78(0x4, 0x1D)
    SetChrPos(0x1C, 1400, 0, 6500, 0)
    OP_D3(0x1C, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1D, 1400, 0, 7700, 0)
    OP_D3(0x1D, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetChrChipByIndex(0x1E, 0x15)
    SetChrSubChip(0x1E, 0x2)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 2400, 600, 6600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x23)
    SetChrSubChip(0x1F, 0xE)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 2100, 500, 6600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x15)
    SetChrSubChip(0x20, 0x1)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 3300, 600, 6400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x14)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 3300, 500, 6100, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x2)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 2400, 600, 7700, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x23)
    SetChrSubChip(0x23, 0xE)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 2100, 500, 7700, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x15)
    SetChrSubChip(0x24, 0x1)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 3300, 600, 8000, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x23)
    SetChrSubChip(0x25, 0x14)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 3300, 500, 8300, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x15)
    SetChrSubChip(0x26, 0x2)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 4000, 600, 7100, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x23)
    SetChrSubChip(0x27, 0xE)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 4400, 500, 7100, 0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x6)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 3200, 600, 7100, 0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    Sound(827, 2, 0, 0)
    BeginChrThread(0x29, 0, 0, 42)
    SetCameraDistance(18500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0611
    ChrTalk(
        0x102,
        (
            "#6P#0109F真美味……\x02\x03",

            "#0102F这位厨师的手艺\x01",
            "十分厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x103,
        (
            "#12P#0204F（嚼嚼嚼）……\x01",
            "……真是好吃……\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x104,
        (
            "#5P#0306F不过，吃着这么美味的食物，\x01",
            "怎么能没有美酒相伴呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(200)

    #C0614
    ChrTalk(
        0x104,
        (
            "#5P#0302F罗伊德，难得格蕾丝小姐请客，\x01",
            "喝一点也没事吧～？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0615
    ChrTalk(
        0x101,
        (
            "#6P#0003F……不行，\x01",
            "我们可是正在工作。\x02\x03",

            "#0001F为防万一，要随时保持清醒。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x104,
        (
            "#5P#0306F知道了知道了，真是的。\x01",
            "我们队长就是太死板了。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x103,
        (
            "#12P#0211F应该是兰迪前辈\x01",
            "你太随便了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x102,
        (
            "#6P#0101F也是，工作中\x01",
            "喝酒确实不合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x12,
        "#11P#2104F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    #C0620
    ChrTalk(
        0x12,
        (
            "#11P#2109F你们可真有意思啊～\x02\x03",

            "#2100F明明性格相差甚远，\x01",
            "却给人某种团结的感觉……\x02\x03",

            "算是个很不错的队伍吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x101,
        (
            "#6P#0006F……就算表扬我们也没什么好处哦。\x02\x03",

            "#0001F重归正题吧──\x01",
            "关于旧城区的事件，\x01",
            "就像我们刚才告诉您的那样。\x02\x03",

            "而您所说的那个\x01",
            "『缺失的拼图碎片』……\x02\x03",

            "差不多也可以告诉我们了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x12,
        (
            "#11P#2102F呵呵……\x01",
            "如果我说，我不告诉你们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#6P#0003F……那我们今后将不会再\x01",
            "相信您所说的任何事，仅此而已。\x02\x03",

            "#0001F而进行对话的机会，\x01",
            "也就到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x12,
        (
            "#11P#2105F唔唔，你当真了啊。\x02\x03",

            "#2109F不过，这坚决的态度\x01",
            "可真不错呢～\x02\x03",

            "#2102F和你那副温柔的面庞\x01",
            "形成了鲜明反差，令人相当感兴趣哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x101,
        (
            "#6P#0004F──那么，各位。\x01",
            "我们回去继续调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        "#6P#0102F嗯，好的。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x103,
        "#12P#0204F……承蒙款待了。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x12,
        (
            "#11P#2106F哎呀呀，我是开玩笑的啦～\x02\x03",

            "#2101F有关拼图碎片的情报是吧？\x01",
            "我会全部告诉你们啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x101,
        "#6P#0006F唉……\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x12,
        (
            "#11P#2103F──首先，\x02\x03",

            "#2100F你们知道\x01",
            "『鲁巴彻』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0631
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x102,
        "#6P#0101F这名字……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(1000)

    #C0633
    ChrTalk(
        0x104,
        (
            "#5P#0305F你们两个……\x01",
            "怎么这么吃惊啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x103,
        (
            "#12P#0205F『鲁巴彻商会』……\x02\x03",

            "#0203F克洛斯贝尔市的注册法人中\x01",
            "好像是有这个名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x12,
        (
            "#11P#2104F呵呵，那个组织\x01",
            "虽然表面上是注册法人。\x02\x03",

            "#2101F但其实──\x01",
            "它的真实面目是掌控着克洛斯贝尔\x01",
            "黑道势力的『黑手党』哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x104, 0x1)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x103, 0x2)
    Sleep(1000)

    #C0636
    ChrTalk(
        0x103,
        (
            "#12P#0201F黑手党……\x01",
            "也就是犯罪组织吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x104,
        (
            "#5P#0301F原来如此……\x01",
            "确实是听说过\x01",
            "类似传闻。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(200)

    #C0638
    ChrTalk(
        0x104,
        (
            "#5P#0301F罗伊德和大小姐\x01",
            "好像知道啊？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0639
    ChrTalk(
        0x101,
        (
            "#6P#0003F是啊……\x02\x03",

            "#0001F住在克洛斯贝尔，\x01",
            "就算并非本意，也会有所耳闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x102,
        (
            "#6P#0108F好像是一个拥有\x01",
            "复杂关系网的组织……\x02\x03",

            "#0101F听说因为他们和一些\x01",
            "当权得势的大人物相勾结，\x01",
            "所以警察也束手无策……\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x104,
        (
            "#5P#0303F原来如此……\x01",
            "每个国家的黑道都一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x103,
        (
            "#12P#0200F那个『鲁巴彻』\x01",
            "做了什么吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0643
    ChrTalk(
        0x12,
        (
            "#11P#2103F嗯，没错。\x02\x03",

            "#2101F最近『鲁巴彻』成员的\x01",
            "动向好像有些可疑哦。\x02\x03",

            "该说看起来都是一副忙碌的样子吗……\x01",
            "还是说正在积极计划着什么……\x02\x03",

            "所以我抽空\x01",
            "进行了许多调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x101,
        (
            "#6P#0005F黑手党\x01",
            "有异动……？\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x102,
        (
            "#6P#0103F……无论怎么想，\x01",
            "这都不是好兆头啊。\x02\x03",

            "#0101F您之所以会来到旧城区，\x01",
            "莫非也是因为这个……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0646
    ChrTalk(
        0x101,
        "#6P#0013F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x12,
        (
            "#11P#2100F呵呵，正是如此。\x02\x03",

            "#2103F我从某条渠道了解到，\x01",
            "半个月之前，黑手党的成员\x01",
            "就经常在旧城区晃荡。\x02\x03",

            "而且，好像都穿着朴素的衣服，\x01",
            "应该是为了掩人耳目。\x02\x03",

            "#2102F你们不觉得这其中有蹊跷吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0648
    ChrTalk(
        0x104,
        "#5P#0301F……确实很奇怪。\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#6P#0003F嗯，明显有什么蹊跷。\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x102,
        (
            "#6P#0103F两个不良团伙\x01",
            "同时向对方发起了暗中袭击，\x01",
            "这种可能性太低了……\x02\x03",

            "#0101F所以，也就是说，\x01",
            "这里出现的鲁巴彻是第三方嫌疑人吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    #C0651
    ChrTalk(
        0x103,
        (
            "#12P#0201F……不过，很奇怪呢。\x02\x03",

            "为什么黑手党\x01",
            "要特意袭击\x01",
            "不良团伙的成员呢……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0652
    ChrTalk(
        0x101,
        (
            "#6P#0001F嗯，这就是问题所在。\x02\x03",

            "如果他们有什么敌对关系的话，\x01",
            "事情就简单了，不过……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)

    #C0653
    ChrTalk(
        0x12,
        (
            "#11P#2106F嗯，据我所知，\x01",
            "迄今为止，他们之间并没有发生过\x01",
            "什么冲突啊～\x02\x03",

            "#2101F虽然同是暴力组织，\x01",
            "但黑手党是专业的，\x01",
            "不良团伙只是业余的……\x02\x03",

            "双方没有利益冲突，\x01",
            "所以应该没有对立的理由呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x104,
        (
            "#5P#0300F那会不会是其中某个\x01",
            "团伙想要打垮对手，\x01",
            "于是联合黑手党发动了这次袭击呢？\x02\x03",

            "如果是这种情况，那么他们自己受到的袭击\x01",
            "也就成了掩人耳目的幌子……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x102,
        (
            "#6P#0106F嗯……\x01",
            "他们有必要做到那个地步吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        (
            "#6P#0001F嗯，至少\x01",
            "瓦吉和瓦鲁多这两个人\x01",
            "之间的关系并没有那么差。\x02\x03",

            "硬要说的话，他们反而\x01",
            "有点互相欣赏的感觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x12,
        (
            "#11P#2105F不错嘛，很有观察力呀。\x02\x03",

            "#2104F据我所知，\x01",
            "瓦鲁多和瓦吉的关系\x01",
            "更像是对手间的惺惺相惜哦。\x02\x03",

            "#2100F一开始，旧城区的\x01",
            "不良团伙就只有\x01",
            "瓦鲁多的『剑蛇帮』……\x02\x03",

            "不过，大约在两年前，\x01",
            "瓦吉突然出现并\x01",
            "组建了『圣书会』。\x02\x03",

            "#2106F当然，瓦鲁多他们很快就跑去\x01",
            "找瓦吉的麻烦，但结果却……\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        "#6P#0005F……难道反而是瓦鲁多被打败了？\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x12,
        (
            "#11P#2109F对对，没错！\x02\x03",

            "#2110F你们别看瓦吉那样，\x01",
            "其实他好像会格斗术。\x02\x03",

            "听说他当时用快得\x01",
            "让人眼花缭乱的拳脚\x01",
            "打倒了大意的瓦鲁多哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x102,
        "#6P#0105F啊……\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x103,
        "#12P#0205F……真意外啊。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x104,
        (
            "#5P#0305F哈～没想到他长得那么可爱，\x01",
            "竟然有这么好的身手。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯，但那个瓦鲁多\x01",
            "也不是好惹的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x12,
        (
            "#11P#2104F对，他一开始只是大意而已，\x01",
            "后来他们也交过好几次手，\x01",
            "但几乎都不分胜负。\x02\x03",

            "#2100F但是，也正因如此，\x01",
            "他们才逐渐开始欣赏对方了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x102,
        (
            "#6P#0100F原来如此……也就是说他们\x01",
            "将彼此当成难得一见的好对手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x104,
        (
            "#5P#0301F这样的话，利用黑手党\x01",
            "击溃对方的说法也不成立了。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#6P#0008F没错……\x02\x03",

            "两个人在手下面前好像都很有威望，\x01",
            "所以应该也不是手下的擅做主张……\x02\x03",

            "#0006F嗯，这样说来……\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x12,
        (
            "#11P#2104F呵呵……\x02\x03",

            "#2102F──就我一贯的作风来说，\x01",
            "这次算是情报大赠送了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x12, 0x4)
    SetChrPos(0x12, 5100, 0, 6200, 270)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()

    #C0670
    ChrTalk(
        0x12,
        (
            "#11P#2110F我还有其它采访任务，\x01",
            "就先失陪了哦。\x02\x03",

            "你们要加油调查下去，\x01",
            "好让我写一篇出色的报道。\x02\x03",

            "#2109F那么，再见了哦～¤\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1500, 1000, 0, 3000)
    OP_92(0x12, 0x5DC, 0x0, 0x1F4)

    def lambda_B846():
        OP_95(0xFE, 1500, 0, 0, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B846)
    Sleep(300)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetChrSubChip(0x102, 0x2)
    Sleep(300)
    SetChrSubChip(0x101, 0x2)
    Sleep(1500)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x12, 1)

    def lambda_B880():
        OP_95(0xFE, -2000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B880)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_B8A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_B8A6)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x12, 2)
    Sound(104, 0, 100, 0)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(3200, 1000, 7100, 0)
    MoveCamera(54, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0671
    ChrTalk(
        0x101,
        "#6P#0006F呼……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    #C0672
    ChrTalk(
        0x102,
        (
            "#3P#0102F呵呵……\x01",
            "很我行我素的人啊。\x02\x03",

            "#0100F不过也多亏了她，\x01",
            "我们才得到了这么重要的情报。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0673
    ChrTalk(
        0x101,
        (
            "#6P#0000F是啊……\x01",
            "这次能知道黑手党的事情，\x01",
            "已经是很大的收获了。\x02\x03",

            "#0003F问题是，为什么\x01",
            "黑手党要介入旧城区的事……\x02\x03",

            "#0008F……这实在让人想不明白，\x01",
            "能作为判断依据的情报太少了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    #C0674
    ChrTalk(
        0x103,
        (
            "#11P#0203F警察的数据库里\x01",
            "好像也没有相关资料……\x02\x03",

            "#0201F应该是因为那些资料的\x01",
            "安全等级较高，所以我们无法查看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x104,
        "#5P#0306F也就是说，那属于机密资料吧。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x102,
        (
            "#3P#0108F考虑到他们的后台，\x01",
            "这种可能性很大……\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x101,
        "#6P#0003F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearChrFlags(0x101, 0x4)
    OP_68(3100, 1000, 6720, 0)
    SetChrPos(0x101, 1500, 0, 5300, 45)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0678
    ChrTalk(
        0x101,
        (
            "#0001F#12P……我们先回支援科，\x01",
            "听听赛尔盖科长的看法吧。\x02\x03",

            "虽然想靠自己的力量解决，\x01",
            "但现状似乎不允许了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x102,
        "#3P#0100F也是呢。\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x104,
        (
            "#1P#0300F那么，我们快点回去\x01",
            "问问大叔吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 0, 0, 43)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 21000, 0, 19000, 0)
    SetChrPos(0x1D, 21000, 0, 19000, 0)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(1500, 1400, 5300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 1500, 0, 5300, 180)
    SetChrPos(0x1, 1500, 0, 5300, 180)
    SetChrPos(0x2, 1500, 0, 5300, 180)
    SetChrPos(0x3, 1500, 0, 5300, 180)
    SetScenarioFlags(0x42, 5)
    OP_29(0x3E, 0x1, 0x5)
    ReplaceBGM("ed7100", "ed7000")
    ReplaceBGM("ed7101", "ed7000")
    ReplaceBGM("ed7100", "ed7102")
    EndChrThread(0x29, 0x0)
    OP_24(0x33B)
    EventEnd(0x5)
    Return()

    # Function_30_9C15 end

    def Function_31_BDF7(): pass

    label("Function_31_BDF7")

    EventBegin(0x0)
    OP_4B(0x1A, 0xFF)
    Fade(800)
    OP_68(-50420, 1400, -54190, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20940, 0)
    SetChrPos(0x101, -51120, 30, -54260, 180)
    SetChrPos(0x102, -51120, 30, -52840, 180)
    SetChrPos(0x103, -50000, 30, -54260, 180)
    SetChrPos(0x104, -50000, 30, -52840, 180)
    SetChrPos(0x1A, -50570, 30, -55800, 90)
    OP_0D()

    #C0681
    ChrTalk(
        0x1A,
        (
            "#12P真苦恼啊……\x01",
            "竟然会卖光了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x1A, 0x0, 0x1F4)
    Sleep(500)

    #C0682
    ChrTalk(
        0x1A,
        "#12P啊，各位，请问一下……\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x1A,
        (
            "#12P你们有\x01",
            "这个月发售的\x01",
            "『咪西』玩偶吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x1A,
        (
            "#12P如果有的话，\x01",
            "请务必转让给我！\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#5P#0005F那个，『咪西』\x01",
            "的玩偶吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        (
            "#5P#0100F『咪西』好像是\x01",
            "疗养地『米修拉姆』的\x01",
            "吉祥物吧。\x02\x03",

            "缇欧好像在\x01",
            "收集它的周边物品呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x103,
        (
            "#0200F嗯，算是吧……\x01",
            "不过那玩偶\x01",
            "我还没买。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x2D, 0x1F4)
    Sleep(200)

    #C0688
    ChrTalk(
        0x1A,
        "#12P哦，各位也是『咪西』的爱好者吗？\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x1A,
        (
            "#12P哈哈哈，其实我儿子\x01",
            "也是它的忠实爱好者哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1A,
        (
            "#12P所以才不畏路途辛苦，\x01",
            "大老远地跑到克洛斯贝尔，\x01",
            "就专门为了买它的玩偶……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x0, 0x1F4)

    #C0691
    ChrTalk(
        0x1A,
        (
            "#12P不过没想到中央广场的\x01",
            "百货商店里竟然卖光了……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x101,
        (
            "#5P#0005F那个百货商店里的都卖光了……\x01",
            "那、那个玩偶这么有人气啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x103,
        (
            "#0203F嗯，没错。\x02\x03",

            "#0200F因为最近每个月都会\x01",
            "发售各种周边产品,所以在\x01",
            "部分人群中可以说是很受欢迎的吧。\x02\x03",

            "#0202F……这个月发售的就是\x01",
            "『咪西玩偶』了，它最大的魅力就\x01",
            "在于平易近人的价格和卓越的便携感。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x104,
        (
            "#0305F哇，阿缇的\x01",
            "数据库果然名不虚传啊……\x02\x03",

            "……………………………\x02\x03",

            "#0303F对了，那个玩偶……\x01",
            "我好像在『巴鲁卡』的\x01",
            "奖品里看到过。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C2DD():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2DD)

    def lambda_C2EA():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C2EA)

    def lambda_C2F7():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C2F7)

    def lambda_C304():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_C304)
    Sleep(600)
    OP_93(0x104, 0xE1, 0x12C)

    #C0695
    ChrTalk(
        0x104,
        (
            "#0303F我对它完全没兴趣，\x01",
            "所以就没在意……\x02\x03",

            "#0300F不过那个好像\x01",
            "是『巴鲁卡』的常规奖品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x1A,
        "#12P真的吗！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x13B, 0x12C)
    Sleep(300)

    #C0697
    ChrTalk(
        0x1A,
        (
            "#12P不过，『巴鲁卡』有点……\x01",
            "因为我从来不去那种地方。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C3D2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C3D2)

    def lambda_C3DF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C3DF)

    def lambda_C3EC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C3EC)

    def lambda_C3F9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C3F9)
    OP_63(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A)
    Sleep(300)
    OP_93(0x1A, 0x0, 0x12C)

    #C0698
    ChrTalk(
        0x1A,
        (
            "#12P那个，如果各位方便的话，\x01",
            "能不能帮我\x01",
            "赢回来呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x1A,
        (
            "#12P我会酬谢各位的！\x01",
            "拜托了！\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x101,
        (
            "#5P#0006F（『巴鲁卡』吗……怎么办，\x01",
            "　好像有点脱离了\x01",
            "　警察的本职工作啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x102,
        (
            "#5P#0100F（这又不是正式的委托，\x01",
            "　就当做好事，\x01",
            "　帮他一下吧。）\x02\x03",

            "#0106F（不然的话……）\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x104,
        (
            "#5P#0309F好，那我们\x01",
            "向『巴鲁卡』出发吧！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    def lambda_C5B2():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5B2)

    def lambda_C5BF():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C5BF)

    def lambda_C5CC():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C5CC)
    Sleep(300)

    #C0703
    ChrTalk(
        0x103,
        (
            "#0200F……兰迪前辈干劲十足啊。\x02\x03",

            "#0211F不会是因为自己想去『巴鲁卡』玩，\x01",
            "所以才撒谎说奖品里有玩偶吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0704
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【梦寐以求的咪西】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50510, 30, -53790, 180)
    OP_4C(0x1A, 0xFF)
    BeginChrThread(0x1A, 0, 0, 2)
    ClearChrFlags(0x1B, 0x10)
    OP_29(0xC, 0x4, 0x2)
    OP_29(0xC, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_BDF7 end

    def Function_32_C6C8(): pass

    label("Function_32_C6C8")

    EventBegin(0x0)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Fade(800)
    OP_68(-50420, 1400, -54190, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20940, 0)
    SetChrPos(0x101, -51120, 30, -54260, 180)
    SetChrPos(0x102, -51120, 30, -52840, 180)
    SetChrPos(0x103, -50000, 30, -54260, 180)
    SetChrPos(0x104, -50000, 30, -52840, 180)
    SetChrPos(0x1A, -50570, 30, -55800, 0)
    OP_0D()

    #C0705
    ChrTalk(
        0x1A,
        (
            "#12P……哦哦！？\x01",
            "这就是『咪西』的玩偶吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x1A,
        (
            "#12P一个就够了。\x01",
            "请务必\x01",
            "转让给我！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【转让】\x01",        # 0
            "【不转让】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C7FA"),
        (1, "loc_C7FE"),
        (SWITCH_DEFAULT, "loc_C87F"),
    )


    label("loc_C7FA")

    Call(0, 33)
    Return()

    label("loc_C7FE")


    #C0707
    ChrTalk(
        0x1A,
        "#12P这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x1A,
        (
            "#12P如果各位改变心意了，\x01",
            "能不能再来找我呢？\x01",
            "我不到最后绝不死心……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -50510, 30, -53790, 180)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    EventEnd(0x5)
    Jump("loc_C87F")

    label("loc_C87F")

    Return()

    # Function_32_C6C8 end

    def Function_33_C880(): pass

    label("Function_33_C880")

    ClearChrFlags(0x1B, 0x4)

    #C0709
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，可以。\x01",
            "这并不是什么特别贵重的东西……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0710
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将『咪西玩偶』交给拉尔斯了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SubItemNumber(0x5D, 1)

    #C0711
    ChrTalk(
        0x1A,
        "#12P这就是咪西的玩偶啊……\x02",
    )

    CloseMessageWindow()
    OP_68(-53210, 1400, -55140, 2000)

    def lambda_C93A():

        label("loc_C93A")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_C93A")

    QueueWorkItem2(0x0, 1, lambda_C93A)

    def lambda_C94C():

        label("loc_C94C")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_C94C")

    QueueWorkItem2(0x1, 1, lambda_C94C)

    def lambda_C95E():

        label("loc_C95E")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_C95E")

    QueueWorkItem2(0x2, 1, lambda_C95E)

    def lambda_C970():

        label("loc_C970")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_C970")

    QueueWorkItem2(0x3, 1, lambda_C970)
    OP_95(0x1A, -52950, 0, -54800, 4000, 0x0)
    OP_93(0x1A, 0xE1, 0x1F4)
    OP_6F(0x1)

    #C0712
    ChrTalk(
        0x1A,
        (
            "#11P库鲁特，你看，\x01",
            "我们终于得到它了哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    Sleep(600)
    TurnDirection(0x1B, 0x1A, 500)

    #C0713
    ChrTalk(
        0x1B,
        "#6P啊，是咪西……！\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x1B,
        "#6P哇～是真的啊！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_68(-50420, 1400, -54190, 2000)
    OP_95(0x1A, -50570, 30, -55800, 4000, 0x0)
    OP_93(0x1A, 0x0, 0x1F4)
    Sleep(300)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    OP_6F(0x1)

    #C0715
    ChrTalk(
        0x1A,
        (
            "#12P啊啊，各位，\x01",
            "非常感谢。\x01",
            "该怎么报答你们才好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1A,
        (
            "#12P对了，这点钱虽然不多，\x01",
            "但请务必收下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0717
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１２０米拉\x07\x00",
            "收下了\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(120)

    #C0718
    ChrTalk(
        0x101,
        (
            "#5P#0000F哈哈，谢谢……\x01",
            "其实您不用这么客气的。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x104,
        (
            "#5P#0304F嘿，赢这个东西\x01",
            "实在太轻松了。\x02\x03",

            "如果再给我点时间，\x01",
            "我还可以\x01",
            "赢回更多好东西呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x102,
        (
            "#5P#0103F咳咳，我们\x01",
            "差不多该回去工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x103,
        (
            "#0200F是啊。\x01",
            "等下次有机会了，\x01",
            "兰迪前辈你再加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x104,
        "#5P#0306F唔……这样啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0723
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【梦寐以求的咪西】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -50110, 30, -52370, 180)
    SetChrPos(0x1A, -49440, 30, -56190, 270)
    SetChrPos(0x1B, -51000, 30, -56190, 90)
    SetChrFlags(0x1B, 0x4)
    BeginChrThread(0x1A, 0, 0, 0)
    TalkBegin(0x1A)
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_29(0xC, 0x4, 0x10)
    OP_29(0xC, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_33_C880 end

    def Function_34_CD1F(): pass

    label("Function_34_CD1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D0D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CE88")

    #C0724
    ChrTalk(
        0xFE,
        (
            "各位，实在非常感谢你们。\x01",
            "看到儿子这么高兴……\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0xFE,
        (
            "我觉得这趟克洛斯贝尔之行算是值了……\x01",
            "谢谢你让我的儿子露出笑容，『咪西』！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE80")

    #C0726
    ChrTalk(
        0x104,
        (
            "#0300F（克洛斯贝尔还真是\x01",
            "　什么样的游客都有啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x103,
        (
            "#0200F（如果是为了『咪西』的话，\x01",
            "　倒是可以理解。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_CE80")

    SetScenarioFlags(0x2, 1)
    Jump("loc_D0D4")

    label("loc_CE88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x5D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D02A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEBA")
    Call(0, 32)
    Jump("loc_D025")

    label("loc_CEBA")


    #C0728
    ChrTalk(
        0x1A,
        (
            "『咪西』的玩偶……\x01",
            "请务必\x01",
            "转让给我！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【转让】\x01",        # 0
            "【不转让】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CF2A"),
        (1, "loc_CFC8"),
        (SWITCH_DEFAULT, "loc_D025"),
    )


    label("loc_CF2A")

    TalkEnd(0x1A)
    EventBegin(0x0)
    EndChrThread(0x1A, 0x0)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Fade(800)
    OP_68(-50420, 1400, -54190, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20940, 0)
    SetChrPos(0x101, -51120, 30, -54260, 180)
    SetChrPos(0x102, -51120, 30, -52840, 180)
    SetChrPos(0x103, -50000, 30, -54260, 180)
    SetChrPos(0x104, -50000, 30, -52840, 180)
    SetChrPos(0x1A, -50570, 30, -55800, 0)
    OP_0D()
    Call(0, 33)
    Return()

    label("loc_CFC8")


    #C0729
    ChrTalk(
        0x1A,
        "这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x1A,
        (
            "如果各位改变主意了，\x01",
            "能不能再来找我呢？\x01",
            "我不到最后绝不死心……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D025")

    label("loc_D025")

    Jump("loc_D0D4")

    label("loc_D02A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_D0D1")

    #C0731
    ChrTalk(
        0xFE,
        (
            "没想到『巴鲁卡』\x01",
            "的奖品里就有咪西……\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xFE,
        (
            "不过，我是个\x01",
            "从来不赌博的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xFE,
        (
            "如果各位方便的话，\x01",
            "能不能帮我赢回那个玩偶呢……\x01",
            "我好像太自私了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0D4")

    label("loc_D0D1")

    Call(0, 31)

    label("loc_D0D4")

    Jump("loc_D1E1")

    label("loc_D0D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D171")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)

    #C0734
    ChrTalk(
        0x1A,
        "好了，肚子也填饱了。\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x1A,
        (
            "接下来和爸爸\x01",
            "一起去买那个东西吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x1B,
        "哇～太棒了！\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x1A,
        (
            "啊哈哈，你可真是\x01",
            "喜欢『咪西』啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Jump("loc_D1E1")

    label("loc_D171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D1E1")

    #C0738
    ChrTalk(
        0xFE,
        (
            "今天是为了儿子，\x01",
            "才来到路途遥远的克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xFE,
        (
            "哈哈哈，\x01",
            "只要儿子开心，\x01",
            "回去后加班再多也不怕！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1E1")

    TalkEnd(0xFE)
    Return()

    # Function_34_CD1F end

    def Function_35_D1E5(): pass

    label("Function_35_D1E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D2BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D23A")

    #C0740
    ChrTalk(
        0xFE,
        (
            "哇～是咪西！\x01",
            "太可爱了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xFE,
        (
            "大哥哥，\x01",
            "谢谢你们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2B9")

    label("loc_D23A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_D28A")

    #C0742
    ChrTalk(
        0xFE,
        (
            "大哥哥，你们给我\x01",
            "带来『咪西』了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xFE,
        "哇～我等好久了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D2B9")

    label("loc_D28A")


    #C0744
    ChrTalk(
        0xFE,
        (
            "呜呜呜……我还以为\x01",
            "可以见到『咪西』的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2B9")

    Jump("loc_D335")

    label("loc_D2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D2CF")
    Call(0, 34)
    Jump("loc_D335")

    label("loc_D2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D335")

    #C0745
    ChrTalk(
        0xFE,
        (
            "哇～床也\x01",
            "好软啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0xFE,
        (
            "还有哦，爸爸\x01",
            "答应要给我买一个\x01",
            "我喜欢的东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0xFE,
        "哇～真期待！\x02",
    )

    CloseMessageWindow()

    label("loc_D335")

    TalkEnd(0xFE)
    Return()

    # Function_35_D1E5 end

    def Function_36_D339(): pass

    label("Function_36_D339")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x0, 0xA, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10960, 1400, -1150, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(25660, 0)
    SetChrPos(0x101, 11270, 0, -600, 90)
    SetChrPos(0x102, 11270, 0, -2110, 90)
    SetChrPos(0x103, 9810, 0, -600, 90)
    SetChrPos(0x104, 9810, 0, -2110, 90)
    SetChrPos(0xA, 12840, 0, -1050, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0748
    ChrTalk(
        0xA,
        "#11P各位～欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#5P#0000F你是桑桑小姐吧。\x01",
            "我们看到了你的支援请求，所以就来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0750
    ChrTalk(
        0xA,
        "#11P哇，这么快就来了啊！？\x02",
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xA,
        "#11P实在太好了！\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0752
    ChrTalk(
        0x104,
        (
            "#6P#0309F（哈哈，这女孩好可爱啊。）\x02\x03",

            "#0300F委托好像是\x01",
            "……『寻找鱼料理的食材』吧。\x02\x03",

            "#0306F怎么说呢，对支援科来说，\x01",
            "这委托内容有点不寻常啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x102,
        (
            "#6P#0106F嗯，我想委托人\x01",
            "应该各有各的苦恼，不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0754
    ChrTalk(
        0xA,
        (
            "#11P虽然不清楚你们在说什么……\x01",
            "但我的委托真的很紧急。\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0xA,
        (
            "#11P其实今天早上，有几位客人突然来预约。\x01",
            "不过做鱼料理的食材却不够了！\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xA,
        (
            "#11P虽然去市场的鱼贩那里看过了，\x01",
            "但合适的好鱼都没有现货，需要预订……\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xA,
        (
            "#11P打杂事务所的各位，拜托\x01",
            "你们帮我找点来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(15)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)

    #C0758
    ChrTalk(
        0x101,
        (
            "#5P#0003F那个，不好意思，\x01",
            "你刚才说什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x103,
        (
            "#5P#0200F我们并不是\x01",
            "打杂事务所的……\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0xA,
        "#11P咦？\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0xA,
        (
            "#11P但我去找游击士协会的接待员\x01",
            "商量的时候，他跟我说他会\x01",
            "安排妥当的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0xA,
        (
            "#11P说是游击士现在都没有空，\x01",
            "不过他会叫几个打杂事务所的熟人来……\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0xA,
        "#11P各位难道不是他叫来的人吗？\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x104,
        "#6P#0306F（……原来是那个接待员的恶作剧啊。）\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x101,
        (
            "#5P#0003F（说是打杂事务所倒也差不多，\x01",
            "　很难否定啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x102,
        "#6P#0106F（真可悲……）\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x103,
        (
            "#5P#0200F反正罗伊德前辈\x01",
            "会钓鱼，\x01",
            "帮帮她也没什么吧？\x02\x03",

            "她看上去好像很苦恼呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        (
            "#5P#0000F也是……\x01",
            "那就接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0xA,
        "#11P真的吗？太好了～！\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0xA,
        (
            "#11P制作鱼料理需要\x01",
            "的是『极其细长的鱼』哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0xA,
        (
            "#11P而且预约的客人有五位，\x01",
            "所以需要五条同种类的鱼，可以吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0xA,
        (
            "#11P嗯……如果钓不到细长的鱼的话，\x01",
            "其它鱼也可以……\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0xA,
        (
            "#11P总之得是五条同种类的鱼哦。\x01",
            "这一点请务必记住！\x02",
        )
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x101,
        (
            "#5P#0003F五条『极其细长的鱼』……\x01",
            "如果实在没办法，\x01",
            "五条同种类的鱼也行是吧。\x02\x03",

            "#0000F我明白了，\x01",
            "要是钓到的话，会给你拿来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xA,
        (
            "#11P嗯，多谢多谢。\x01",
            "拜托你们啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0776
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找鱼类料理的食材！】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 9670, 30, -2060, 90)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_DB50")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)

    label("loc_DB50")

    OP_29(0x11, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_D339 end

    def Function_37_DB59(): pass

    label("Function_37_DB59")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(800)
    OP_68(10960, 1400, -1150, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(25660, 0)
    SetChrPos(0x101, 11270, 0, -600, 90)
    SetChrPos(0x102, 11270, 0, -2110, 90)
    SetChrPos(0x103, 9810, 0, -600, 90)
    SetChrPos(0x104, 9810, 0, -2110, 90)
    SetChrPos(0xA, 12840, 0, -1050, 270)
    OP_0D()
    Call(0, 41)

    #C0777
    ChrTalk(
        0xA,
        (
            "#11P谢谢你们，\x01",
            "这样一来，晚上就没问题了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC78")
    OP_2C(0x11, 0x5)
    OP_29(0x11, 0x1, 0x2)

    #C0778
    ChrTalk(
        0xA,
        (
            "#11P和平时用的鱼一样，\x01",
            "这样一来，晚上肯定能让客人满意了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD75")

    label("loc_DC78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD1D")
    OP_2C(0x11, 0x5)
    OP_29(0x11, 0x1, 0x3)

    #C0779
    ChrTalk(
        0xA,
        (
            "#11P虽然和平时用的鱼不一样……\x01",
            "但这些鱼也很珍贵，\x01",
            "爸爸一定能将它们做成美味的料理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0xA,
        "#11P这样一来，晚上肯定能让客人满意了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD75")

    label("loc_DD1D")

    OP_2C(0x11, 0x2)
    OP_29(0x11, 0x1, 0x4)

    #C0781
    ChrTalk(
        0xA,
        (
            "#11P虽然不是『极其细长的鱼』，\x01",
            "但爸爸应该也可以将它们做成美味的生鱼片。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD75")


    #C0782
    ChrTalk(
        0xA,
        (
            "#11P对了，这个就\x01",
            "作为对各位的谢礼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE00")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0783
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('中回复药', 2)
    Jump("loc_DEAC")

    label("loc_DE00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE60")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0784
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('中回复药', 3)
    Jump("loc_DEAC")

    label("loc_DE60")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0785
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('回复药', 2)

    label("loc_DEAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFF8")

    #C0786
    ChrTalk(
        0xA,
        (
            "#11P还有……对了，\x01",
            "你们对这个有兴趣吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0787
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x197),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的食谱收下了。\x02",
        )
    )

    CloseMessageWindow()

    #A0788
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x197),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x3)

    #C0789
    ChrTalk(
        0xA,
        (
            "#11P这是我们店秘传的炒饭菜谱哦。\x01",
            "晚上准备和生鱼片一起，\x01",
            "用来款待客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0xA,
        "#11P可以的话你们试试。\x02",
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x101,
        (
            "#5P#0000F这样啊，\x01",
            "那我们就却之不恭了。\x02\x03",

            "你工作也加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0F7")

    label("loc_DFF8")


    #C0792
    ChrTalk(
        0xA,
        (
            "#11P还有……对了，\x01",
            "这个也送给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0793
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x197),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('龙老炒饭', 1)

    #C0794
    ChrTalk(
        0xA,
        (
            "#11P这是刚才\x01",
            "给客人做错的菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0xA,
        (
            "#11P刚刚做好的，\x01",
            "你们吃吃看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        (
            "#5P#0000F哈哈……谢谢了，\x01",
            "那我们就不客气了。\x02\x03",

            "你工作也加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0F7")


    #C0797
    ChrTalk(
        0xA,
        (
            "#11P嗯，打杂事务所的各位，\x01",
            "真的十分感谢你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0798
    ChrTalk(
        0x101,
        "#5P#0012F哈、哈哈哈……\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x102,
        (
            "#6P#0106F（到最后还是没能\x01",
            "    澄清误会啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0800
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找鱼类料理的食材！】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 9670, 30, -2060, 90)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E286")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)

    label("loc_E286")

    OP_29(0x11, 0x4, 0x10)
    SetScenarioFlags(0x2, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_37_DB59 end

    def Function_38_E294(): pass

    label("Function_38_E294")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2BF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x175), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2E0")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x174), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E2E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E301")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x173), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E301")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E322")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E322")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E343")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x171), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E343")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E364")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E364")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E385")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E385")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E3A6")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E3A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E3C7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E3C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E3E8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E3E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E409")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E42A")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E42A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E44B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E44B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E46C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E46C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E48D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E48D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4AE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x166), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E4AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4CF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E4CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4F0")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E4F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E511")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x163), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E511")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E532")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E532")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E553")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E553")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E574")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E574")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E595")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E595")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E5B1")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_E5B1")

    Return()

    # Function_38_E294 end

    def Function_39_E5B2(): pass

    label("Function_39_E5B2")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E616")
    MenuCmd(1, 1, "雪花蟹")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E60C")
    Call(0, 40)

    label("loc_E60C")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E616")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E675")
    MenuCmd(1, 1, "阿尔摩利卡鲫鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E66B")
    Call(0, 40)

    label("loc_E66B")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E675")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6CC")
    MenuCmd(1, 1, "橙河鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E6C2")
    Call(0, 40)

    label("loc_E6C2")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E723")
    MenuCmd(1, 1, "岩穴鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E719")
    Call(0, 40)

    label("loc_E719")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E723")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E778")
    MenuCmd(1, 1, "鲤鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E76E")
    Call(0, 40)

    label("loc_E76E")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E778")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7CF")
    MenuCmd(1, 1, "冷水鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E7C5")
    Call(0, 40)

    label("loc_E7C5")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E7CF")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E82A")
    MenuCmd(1, 1, "蓝带神仙鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E820")
    Call(0, 40)

    label("loc_E820")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E82A")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E881")
    MenuCmd(1, 1, "银伞鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E877")
    Call(0, 40)

    label("loc_E877")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E881")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E8D8")
    MenuCmd(1, 1, "虹鳟鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E8CE")
    Call(0, 40)

    label("loc_E8CE")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E8D8")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E92D")
    MenuCmd(1, 1, "黑鲑")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E923")
    Call(0, 40)

    label("loc_E923")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E92D")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E982")
    MenuCmd(1, 1, "鲑鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E978")
    Call(0, 40)

    label("loc_E978")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E982")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9D7")
    MenuCmd(1, 1, "鳗鲡")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E9CD")
    Call(0, 40)

    label("loc_E9CD")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E9D7")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA2E")
    MenuCmd(1, 1, "珍珠草")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA24")
    Call(0, 40)

    label("loc_EA24")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EA2E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA87")
    MenuCmd(1, 1, "大口鲈鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA7D")
    Call(0, 40)

    label("loc_EA7D")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EA87")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAE0")
    MenuCmd(1, 1, "云斑蛇头")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EAD6")
    Call(0, 40)

    label("loc_EAD6")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EAE0")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EB39")
    MenuCmd(1, 1, "暗纹蛇鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EB2F")
    Call(0, 40)

    label("loc_EB2F")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EB39")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EB8E")
    MenuCmd(1, 1, "巨鲶")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EB84")
    Call(0, 40)

    label("loc_EB84")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EB8E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBE5")
    MenuCmd(1, 1, "巨血蟹")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EBDB")
    Call(0, 40)

    label("loc_EBDB")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EBE5")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC3A")
    MenuCmd(1, 1, "电鳗")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EC30")
    Call(0, 40)

    label("loc_EC30")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EC3A")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC93")
    MenuCmd(1, 1, "魔鬼巨鲶")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EC89")
    Call(0, 40)

    label("loc_EC89")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EC93")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECEA")
    MenuCmd(1, 1, "弧光蟹")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ECE0")
    Call(0, 40)

    label("loc_ECE0")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ECEA")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED3F")
    MenuCmd(1, 1, "金鲑")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ED35")
    Call(0, 40)

    label("loc_ED35")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ED3F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED94")
    MenuCmd(1, 1, "锦鲤")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ED8A")
    Call(0, 40)

    label("loc_ED8A")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ED94")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EDED")
    MenuCmd(1, 1, "霸王蛇鱼")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EDE3")
    Call(0, 40)

    label("loc_EDE3")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EDED")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x1)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE37")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_EE37")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE7F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EE7F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEC7")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EEC7")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF0F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF0F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF57")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF57")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF9F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF9F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EFE7")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EFE7")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F02F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F02F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F077")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F077")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0BF")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F0BF")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F107")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F107")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F14F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F14F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F197")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F197")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1DF")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F1DF")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F227")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F227")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F26F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F26F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2B7")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F2B7")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2FF")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F2FF")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F347")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F347")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F38F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F38F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3D7")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3D7")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F41F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F41F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F467")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F467")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4AF")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4AF")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4F7")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4F7")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_E5B2 end

    def Function_40_F507(): pass

    label("Function_40_F507")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F51F")
    MenuCmd(3, 1, 0x0)
    Jump("loc_F742")

    label("loc_F51F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F537")
    MenuCmd(3, 1, 0x1)
    Jump("loc_F742")

    label("loc_F537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F54F")
    MenuCmd(3, 1, 0x2)
    Jump("loc_F742")

    label("loc_F54F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F567")
    MenuCmd(3, 1, 0x3)
    Jump("loc_F742")

    label("loc_F567")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F57F")
    MenuCmd(3, 1, 0x4)
    Jump("loc_F742")

    label("loc_F57F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F597")
    MenuCmd(3, 1, 0x5)
    Jump("loc_F742")

    label("loc_F597")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5AF")
    MenuCmd(3, 1, 0x6)
    Jump("loc_F742")

    label("loc_F5AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5C7")
    MenuCmd(3, 1, 0x7)
    Jump("loc_F742")

    label("loc_F5C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5DF")
    MenuCmd(3, 1, 0x8)
    Jump("loc_F742")

    label("loc_F5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F7")
    MenuCmd(3, 1, 0x9)
    Jump("loc_F742")

    label("loc_F5F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F60F")
    MenuCmd(3, 1, 0xA)
    Jump("loc_F742")

    label("loc_F60F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F627")
    MenuCmd(3, 1, 0xB)
    Jump("loc_F742")

    label("loc_F627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F63F")
    MenuCmd(3, 1, 0xC)
    Jump("loc_F742")

    label("loc_F63F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F657")
    MenuCmd(3, 1, 0xD)
    Jump("loc_F742")

    label("loc_F657")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F66F")
    MenuCmd(3, 1, 0xE)
    Jump("loc_F742")

    label("loc_F66F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F687")
    MenuCmd(3, 1, 0xF)
    Jump("loc_F742")

    label("loc_F687")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F69F")
    MenuCmd(3, 1, 0x10)
    Jump("loc_F742")

    label("loc_F69F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6B7")
    MenuCmd(3, 1, 0x11)
    Jump("loc_F742")

    label("loc_F6B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6CF")
    MenuCmd(3, 1, 0x12)
    Jump("loc_F742")

    label("loc_F6CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6E7")
    MenuCmd(3, 1, 0x13)
    Jump("loc_F742")

    label("loc_F6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6FF")
    MenuCmd(3, 1, 0x14)
    Jump("loc_F742")

    label("loc_F6FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F717")
    MenuCmd(3, 1, 0x15)
    Jump("loc_F742")

    label("loc_F717")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F72F")
    MenuCmd(3, 1, 0x16)
    Jump("loc_F742")

    label("loc_F72F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F742")
    MenuCmd(3, 1, 0x17)

    label("loc_F742")

    Return()

    # Function_40_F507 end

    def Function_41_F743(): pass

    label("Function_41_F743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x175), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F75C")
    SubItemNumber('金鲑', 5)
    Jump("loc_F996")

    label("loc_F75C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x174), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F775")
    SubItemNumber('巨鲶', 5)
    Jump("loc_F996")

    label("loc_F775")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x173), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78E")
    SubItemNumber('珍珠龙鱼', 5)
    Jump("loc_F996")

    label("loc_F78E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A7")
    SubItemNumber('巨血蟹', 5)
    Jump("loc_F996")

    label("loc_F7A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x171), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C0")
    SubItemNumber('钢壳龟', 5)
    Jump("loc_F996")

    label("loc_F7C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7D9")
    SubItemNumber('鳗鲡', 5)
    Jump("loc_F996")

    label("loc_F7D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7F2")
    SubItemNumber('金龙鱼', 5)
    Jump("loc_F996")

    label("loc_F7F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F80B")
    SubItemNumber('鲑鱼', 5)
    Jump("loc_F996")

    label("loc_F80B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F824")
    SubItemNumber('小鲵', 5)
    Jump("loc_F996")

    label("loc_F824")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F83D")
    SubItemNumber('冷水鱼', 5)
    Jump("loc_F996")

    label("loc_F83D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F856")
    SubItemNumber('角斗鱼', 5)
    Jump("loc_F996")

    label("loc_F856")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F86F")
    SubItemNumber('黑鲑', 5)
    Jump("loc_F996")

    label("loc_F86F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F888")
    SubItemNumber('大口鲈鱼', 5)
    Jump("loc_F996")

    label("loc_F888")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8A1")
    SubItemNumber('鲤鱼', 5)
    Jump("loc_F996")

    label("loc_F8A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8BA")
    SubItemNumber('食人鱼', 5)
    Jump("loc_F996")

    label("loc_F8BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x166), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8D3")
    SubItemNumber('虹鳟鱼', 5)
    Jump("loc_F996")

    label("loc_F8D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8EC")
    SubItemNumber('岩穴鱼', 5)
    Jump("loc_F996")

    label("loc_F8EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F905")
    SubItemNumber('橙河鱼', 5)
    Jump("loc_F996")

    label("loc_F905")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x163), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F91E")
    SubItemNumber('乌龟', 5)
    Jump("loc_F996")

    label("loc_F91E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F937")
    SubItemNumber('阿尔摩利卡鲫鱼', 5)
    Jump("loc_F996")

    label("loc_F937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F950")
    SubItemNumber('银伞鱼', 5)
    Jump("loc_F996")

    label("loc_F950")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F969")
    SubItemNumber('蓝带神仙鱼', 5)
    Jump("loc_F996")

    label("loc_F969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F982")
    SubItemNumber('雪花蟹', 5)
    Jump("loc_F996")

    label("loc_F982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F996")
    SubItemNumber('斗鱼', 5)

    label("loc_F996")

    Return()

    # Function_41_F743 end

    def Function_42_F997(): pass

    label("Function_42_F997")

    OP_25(0x33B, 0x0)
    Sleep(80)
    OP_25(0x33B, 0xA)
    Sleep(80)
    OP_25(0x33B, 0x14)
    Sleep(80)
    OP_25(0x33B, 0x1E)
    Sleep(80)
    OP_25(0x33B, 0x28)
    Sleep(80)
    OP_25(0x33B, 0x32)
    Sleep(80)
    OP_25(0x33B, 0x3C)
    Sleep(80)
    OP_25(0x33B, 0x46)
    Sleep(80)
    OP_25(0x33B, 0x50)
    Sleep(80)
    OP_25(0x33B, 0x5A)
    Sleep(80)
    OP_25(0x33B, 0x64)
    Return()

    # Function_42_F997 end

    def Function_43_F9E2(): pass

    label("Function_43_F9E2")

    OP_25(0x33B, 0x64)
    Sleep(80)
    OP_25(0x33B, 0x5A)
    Sleep(80)
    OP_25(0x33B, 0x50)
    Sleep(80)
    OP_25(0x33B, 0x46)
    Sleep(80)
    OP_25(0x33B, 0x3C)
    Sleep(80)
    OP_25(0x33B, 0x32)
    Sleep(80)
    OP_25(0x33B, 0x28)
    Sleep(80)
    OP_25(0x33B, 0x1E)
    Sleep(80)
    OP_25(0x33B, 0x14)
    Sleep(80)
    OP_25(0x33B, 0xA)
    Sleep(80)
    OP_25(0x33B, 0x0)
    OP_24(0x33B)
    Return()

    # Function_43_F9E2 end

    SaveToFile()

Try(main)
