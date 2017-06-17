from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "チャンホイ",             # 1
        "フェン",                 # 2
        "サンサン",               # 3
        "グリッド",               # 4
        "パック",                 # 5
        "パック",                 # 6
        "ルース",                 # 7
        "ルース",                 # 8
        "紫髪の娘",               # 9
        "セルゲイ課長",           # 10
        "グレイス",               # 11
        "レインズ",               # 12
        "フリージア",             # 13
        "レディナ",               # 14
        "アントン",               # 15
        "リックス",               # 16
        "ヴァルド",               # 17
        "ルガノフ",               # 18
        "ラルス",                 # 19
        "クルト",                 # 20
        "イス",                   # 21
        "イス",                   # 22
        "食器",                   # 23
        "食器",                   # 24
        "食器",                   # 25
        "食器",                   # 26
        "食器",                   # 27
        "食器",                   # 28
        "食器",                   # 29
        "食器",                   # 30
        "食器",                   # 31
        "食器",                   # 32
        "食器",                   # 33
        "SE制御",                 # 34
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
    DeclNpc(7130,    150,     -1480,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(16030,   0,       6050,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10689,   150,     3170,    270,  341,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(17909,   0,       8399,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(7300,    150,     3230,    90,   341,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(13949,   150,     2900,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(13810,   150,     5909,    90,   469,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4900,    100,     7099,    270,  469,  0x0, 0,   9,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1299,    100,     7099,    90,   469,  0x0, 0,   10,  0,   255, 255, 0,   18,  255,  0)
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
        "Function_7_CD2",          # 07, 7
        "Function_8_1904",         # 08, 8
        "Function_9_1A0E",         # 09, 9
        "Function_10_2BF8",        # 0A, 10
        "Function_11_403F",        # 0B, 11
        "Function_12_4EFD",        # 0C, 12
        "Function_13_5007",        # 0D, 13
        "Function_14_5178",        # 0E, 14
        "Function_15_597A",        # 0F, 15
        "Function_16_59E7",        # 10, 16
        "Function_17_6AEE",        # 11, 17
        "Function_18_6C77",        # 12, 18
        "Function_19_6C7B",        # 13, 19
        "Function_20_706B",        # 14, 20
        "Function_21_733A",        # 15, 21
        "Function_22_77D8",        # 16, 22
        "Function_23_790B",        # 17, 23
        "Function_24_7C89",        # 18, 24
        "Function_25_80C6",        # 19, 25
        "Function_26_85D9",        # 1A, 26
        "Function_27_8900",        # 1B, 27
        "Function_28_A22A",        # 1C, 28
        "Function_29_A718",        # 1D, 29
        "Function_30_AE3B",        # 1E, 30
        "Function_31_D413",        # 1F, 31
        "Function_32_DDE3",        # 20, 32
        "Function_33_DFCF",        # 21, 33
        "Function_34_E504",        # 22, 34
        "Function_35_EA48",        # 23, 35
        "Function_36_EC06",        # 24, 36
        "Function_37_F4AA",        # 25, 37
        "Function_38_FC8B",        # 26, 38
        "Function_39_FFA9",        # 27, 39
        "Function_40_10F6E",       # 28, 40
        "Function_41_111AA",       # 29, 41
        "Function_42_113FE",       # 2A, 42
        "Function_43_11449",       # 2B, 43
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CCB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C51")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C71")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC1")

    label("loc_C71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC1")

    label("loc_C91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA5")
    Jump("loc_CC1")

    label("loc_CA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_CC1")

    Jump("loc_BDE")

    label("loc_CC6")

    Jump("loc_CCE")

    label("loc_CCB")

    Call(0, 7)

    label("loc_CCE")

    TalkEnd(0x8)
    Return()

    # Function_6_BC8 end

    def Function_7_CD2(): pass

    label("Function_7_CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D74")

    #C0001
    ChrTalk(
        0x8,
        (
            "バイトを厨房に立たせると、\x01",
            "皿を取りに来る\x01",
            "サンサンと必ずかち合う。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "……あのバイト、まさかそれを\x01",
            "狙っているのではあるまいね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DBE")

    label("loc_D74")


    #C0003
    ChrTalk(
        0x8,
        "バイトには客引きに移ってもらった。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "厨房には絶対入れさせないよ。\x02",
    )

    CloseMessageWindow()

    label("loc_DBE")

    Jump("loc_1903")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DF7")

    #C0005
    ChrTalk(
        0x8,
        "……バイトはキリキリ働くよろし。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1903")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E47")

    #C0006
    ChrTalk(
        0x8,
        "ずずー……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "今日のスープはいい出来ね。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_E98")

    label("loc_E47")


    #C0008
    ChrTalk(
        0x8,
        (
            "このスープは共和国に\x01",
            "いた頃から使っている仕込みよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "ウチの味の秘訣ね。\x02",
    )

    CloseMessageWindow()

    label("loc_E98")

    Jump("loc_1903")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F66")

    #C0010
    ChrTalk(
        0x8,
        (
            "この店は客を楽しませるために\x01",
            "やってるのではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "かといって金儲けのためでもない。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "……どっちも程ほどでいいよ。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "どうせ、大して\x01",
            "流行ってない宿酒場だしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FA6")

    label("loc_F66")


    #C0014
    ChrTalk(
        0x8,
        "店は程ほどでいいよ。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "ワタシは静かな店が好きだからね。\x02",
    )

    CloseMessageWindow()

    label("loc_FA6")

    Jump("loc_1903")

    label("loc_FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1006")

    #C0016
    ChrTalk(
        0x8,
        "記念祭が終わって静かになった。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……少しは落ち着いて\x01",
            "店を開けるね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1903")

    label("loc_1006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_109E")

    #C0018
    ChrTalk(
        0x8,
        (
            "あの不良ども、サンサンに何かしたら\x01",
            "許さないね～～～……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "サンサンもサンサンよ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "あんな客どもに\x01",
            "応対してやる事なんてないよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1903")

    label("loc_109E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1176")

    #C0021
    ChrTalk(
        0x8,
        "あの連中……また来たね。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "また店で騒ぎを起こしたら\x01",
            "叩き出すよ！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1171")

    #C0023
    ChrTalk(
        0x101,
        (
            "#0000F（ヴァルド、よくここに\x01",
            "  来てるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#0100F（お店の人も\x01",
            "  慣れてしまっているみたいね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1171")

    Jump("loc_1903")

    label("loc_1176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_12DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125F")

    #C0025
    ChrTalk(
        0x8,
        (
            "ワタシが移住したのは\x01",
            "まだサンサンが小さい頃だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "そしてこっちでも\x01",
            "周りにサンサンと同い年くらいの\x01",
            "娘がいなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "……でも、ようやく\x01",
            "仲のいい友達が出来たみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "ワタシも嬉しいよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D9")

    label("loc_125F")


    #C0029
    ChrTalk(
        0x8,
        (
            "サンサンに親友が\x01",
            "できてワタシも嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "………………ただし………\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "もし万が一男だったら\x01",
            "許さないけどね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D9")

    Jump("loc_1903")

    label("loc_12DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_146C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D5")

    #C0032
    ChrTalk(
        0x8,
        (
            "……客の噂話で\x01",
            "聞いてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "この街にも黒月#4Rヘイユエ#が\x01",
            "来てるとは知らなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "……連中は狡猾で恐ろしい相手ね。\x01",
            "ワタシ共和国の東方人街にいたから知ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "お客さんたちも\x01",
            "関わらない方がいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1467")

    label("loc_13D5")


    #C0036
    ChrTalk(
        0x8,
        (
            "記念祭の準備で忙しいというのに\x01",
            "嫌な噂を聞いてしまったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "……黒月#4Rヘイユエ#は狡猾で恐ろしい連中。\x01",
            "お客さんたちも関わらない方がいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1467")

    Jump("loc_1903")

    label("loc_146C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EA")

    #C0038
    ChrTalk(
        0x8,
        "そこの２人、いつも長話ばかりね。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "まったく……長居するなら\x01",
            "追加注文してくれないと困るね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1542")

    label("loc_14EA")


    #C0040
    ChrTalk(
        0x8,
        (
            "そこの２人、いつも長話してる。\x01",
            "いい加減にしないとオタマで\x01",
            "殴りつけるよ、まったく。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1542")

    Jump("loc_1903")

    label("loc_1547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C9")

    #C0041
    ChrTalk(
        0x8,
        (
            "フウ、サンサンも\x01",
            "分からない子ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "店など手伝わなくても\x01",
            "いいと言っているのに……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15FE")

    label("loc_15C9")


    #C0043
    ChrTalk(
        0x8,
        (
            "……何でもないよ。\x01",
            "注文ならあっちでするよろし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FE")

    Jump("loc_1903")

    label("loc_1603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1731")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DE")

    #C0044
    ChrTalk(
        0x8,
        (
            "旧市街のガキどもは\x01",
            "近頃顔を出さなくなったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "ようやく静かに営業できる……\x01",
            "と思ったらそうでもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "仕事上がりの連中が\x01",
            "騒がしく飲みにやってくる。\x01",
            "まったく、ウチも相変わらずね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_172C")

    label("loc_16DE")


    #C0047
    ChrTalk(
        0x8,
        (
            "この店、いつも騒がしくて困る。\x01",
            "みんな少しは\x01",
            "静かに食事できないものかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172C")

    Jump("loc_1903")

    label("loc_1731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")

    #C0048
    ChrTalk(
        0x8,
        (
            "旧市街のガキどもには\x01",
            "頭にくるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "前にもウチの店内で\x01",
            "大喧嘩はじめた事があったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "……勿論ワタシが\x01",
            "叩き出してやったけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_184B")

    label("loc_17D7")


    #C0051
    ChrTalk(
        0x8,
        (
            "旧市街のガキどもは、\x01",
            "前にもウチで騒ぎ起こした。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "フン、迷惑もいい所ね。\x01",
            "次は叩き出す程度じゃ済まさないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184B")

    Jump("loc_1903")

    label("loc_1850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CC")

    #C0053
    ChrTalk(
        0x8,
        "む……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "……ここは厨房。\x01",
            "お客さん入ってはいけない。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "注文はカウンターでするよろし！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1903")

    label("loc_18CC")


    #C0056
    ChrTalk(
        0x8,
        (
            "お客さん、ここは厨房。\x01",
            "注文はあっちでするよろし！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1903")

    Return()

    # Function_7_CD2 end

    def Function_8_1904(): pass

    label("Function_8_1904")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1A07")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_191A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A02")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_198D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_198D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AD")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19FD")

    label("loc_19AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CD")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19FD")

    label("loc_19CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E1")
    Jump("loc_19FD")

    label("loc_19E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19FD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_19FD")

    Jump("loc_191A")

    label("loc_1A02")

    Jump("loc_1A0A")

    label("loc_1A07")

    Call(0, 9)

    label("loc_1A0A")

    TalkEnd(0x9)
    Return()

    # Function_8_1904 end

    def Function_9_1A0E(): pass

    label("Function_9_1A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1A4F")

    #C0057
    ChrTalk(
        0x9,
        (
            "くっく……マスターの\x01",
            "心配性も相変わらずだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF7")

    label("loc_1A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1AC7")

    #C0058
    ChrTalk(
        0x9,
        (
            "パックとルースを\x01",
            "バイトとして使ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "今までのツケも溜まってるし\x01",
            "こき使ってやらねえとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF7")

    label("loc_1AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B57")

    #C0060
    ChrTalk(
        0x9,
        (
            "いよう、らっしゃい！\x01",
            "何か食うかい～？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "……ってどうしたんだ、\x01",
            "イマイチ浮かねえ顔だな。\x01",
            "街で何かあったのか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BD6")

    label("loc_1B57")


    #C0062
    ChrTalk(
        0x9,
        (
            "うちで事件っていやあ、\x01",
            "パックとルースが\x01",
            "ついに破局を迎えた事くらいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "……あの２人、\x01",
            "いつもヒマな話してるよな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD6")

    Jump("loc_2BF7")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C84")

    #C0064
    ChrTalk(
        0x9,
        "らっしゃい、場末の宿酒場へ！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "記念祭も終わって\x01",
            "常連客ばかりになっちまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "やれやれ……もっとこう\x01",
            "ぱーっと儲からんもんかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D06")

    label("loc_1C84")


    #C0067
    ChrTalk(
        0x9,
        (
            "俺っちも商売人だ、\x01",
            "店をやるからにはぱーっと儲けたいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "また記念祭みたいな祭りがあって\x01",
            "客がどんどこ来りゃいいのになあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D06")

    Jump("loc_2BF7")

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1E0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8E")

    #C0069
    ChrTalk(
        0x9,
        (
            "サンサンはリーシャちゃんと\x01",
            "洋服を見てくるんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "あーあ、俺も\x01",
            "ついて行きたかったなぁ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E06")

    label("loc_1D8E")


    #C0071
    ChrTalk(
        0x9,
        (
            "うまくすりゃあ\x01",
            "リーシャちゃんとデート……！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "でも女の買い物は金掛かるからな。\x01",
            "……今日はパスしたんだよ、うん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E06")

    Jump("loc_2BF7")

    label("loc_1E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F33")

    #C0073
    ChrTalk(
        0x9,
        (
            "よう、魚を\x01",
            "届けてくれたんだってな？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "ハッハー、ありがたい。\x01",
            "これで今夜は凌げるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "いやなんでも、アルカンシェルの\x01",
            "プレ公演まで滞在する……とかで。\x01",
            "結構上等なお客様なワケよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "魚のお造りくらい出せねえと\x01",
            "店の看板が泣いちまうよなぁ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2E")
    SetScenarioFlags(0x0, 1)

    label("loc_1F2E")

    Jump("loc_2BF7")

    label("loc_1F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_20A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2032")

    #C0077
    ChrTalk(
        0x9,
        (
            "俺の故郷、共和国も\x01",
            "結構事件やテロが多い国でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "表向きのんびりした所なんだが\x01",
            "一皮むけば色々ある国だったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "ま、クロスベルと違うのは\x01",
            "強力な軍隊があるってことだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "治安維持部隊なんざ\x01",
            "そりゃあ優秀なもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_209C")

    label("loc_2032")


    #C0081
    ChrTalk(
        0x9,
        (
            "クロスベルは\x01",
            "警察が頼んねえからなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "って、おっと失礼。\x01",
            "そのバッジ、あんたらも警官だったか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209C")

    Jump("loc_2BF7")

    label("loc_20A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_230C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2182")

    #C0083
    ChrTalk(
        0x9,
        (
            "参ったぜ、今日は\x01",
            "急な予約客が入っててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "いつもなら喜んで\x01",
            "魚のお造りでもてなす所なんだが……\x01",
            "あいにくその魚がねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "そんな上等じゃなくてもいいから\x01",
            "とにかく５匹、集まらねえもんかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2307")

    label("loc_2182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228D")

    #C0086
    ChrTalk(
        0x9,
        (
            "よう、魚を\x01",
            "届けてくれたんだってな？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "ハッハー、ありがたい。\x01",
            "これで今夜は凌げるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "いやなんでも、アルカンシェルの\x01",
            "プレ公演まで滞在する……とかで。\x01",
            "結構上等なお客様なワケよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "魚のお造りくらい出せねえと\x01",
            "店の看板が泣いちまうよなぁ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2307")

    label("loc_228D")


    #C0090
    ChrTalk(
        0x9,
        (
            "とにかく助かったぜ。\x01",
            "これで今夜は凌げそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "あとは……あの赤ジャージどもが\x01",
            "大人しくしててくれりゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2307")

    Jump("loc_2BF7")

    label("loc_230C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_245F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23EB")

    #C0092
    ChrTalk(
        0x9,
        (
            "最近サンサンと仲良くしてる\x01",
            "リーシャちゃんって子がいるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "今朝も来てくれたんだぜ。\x01",
            "ああ、可っ愛いな～っ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "俺の好みにドストライク！\x01",
            "同郷の共和国出身ってのも\x01",
            "ポイント高いよな～㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_245A")

    label("loc_23EB")


    #C0095
    ChrTalk(
        0x9,
        (
            "リーシャちゃんも共和国出身らしい。\x01",
            "しめしめ……話題には事欠かねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "今度本気でアタックしてみるか㈱\x02",
    )

    CloseMessageWindow()

    label("loc_245A")

    Jump("loc_2BF7")

    label("loc_245F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2510")

    #C0097
    ChrTalk(
        0x9,
        "おいおい、聞いてくれよ。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "最近、記念祭の期間中に\x01",
            "宿の予約を入れやがる客がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "こんな街外れの宿酒場に\x01",
            "ふつー予約なんて入れるかね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_258D")

    label("loc_2510")


    #C0100
    ChrTalk(
        0x9,
        (
            "ホテルならともかく\x01",
            "ウチみたいな場末の宿酒場に\x01",
            "予約を入れるとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "まさかホテルの方は\x01",
            "満席だったりすんのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258D")

    Jump("loc_2BF7")

    label("loc_2592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_26F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268A")

    #C0102
    ChrTalk(
        0x9,
        (
            "そこにいる２人は\x01",
            "『万年うだつの上がらない\x01",
            "パックとルース』っていってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "日曜学校はサンサンの\x01",
            "同級生だったんだが、\x01",
            "当時からあんな感じらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "ははっ、商売やるとか言ってるが\x01",
            "いつになったら纏まることやら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26F0")

    label("loc_268A")


    #C0105
    ChrTalk(
        0x9,
        (
            "そこにいる２人は\x01",
            "『万年うだつの上がらない\x01",
            "パックとルース』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        "ま、俺が名づけたんだけどな。\x02",
    )

    CloseMessageWindow()

    label("loc_26F0")

    Jump("loc_2BF7")

    label("loc_26F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2777")

    #C0107
    ChrTalk(
        0x9,
        (
            "へへっ、このお客さん\x01",
            "判ってんじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "ウチのチャーシューは本場だぜ。\x01",
            "マスターは東方人街の出だからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF7")

    label("loc_2777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_28E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_287D")

    #C0109
    ChrTalk(
        0x9,
        "サンサンの奴は可愛いだろ～。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "働き者で器量よし、\x01",
            "おまけにハニーボイスで\x01",
            "お嫁さんにしたい娘ナンバーワン！\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "……その分マスターも\x01",
            "気が気じゃねえんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "ナベ振ってるフリして\x01",
            "ずっと気にしてんだぜ。\x01",
            "くっく……見ものだろ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28DD")

    label("loc_287D")


    #C0113
    ChrTalk(
        0x9,
        (
            "サンサンの奴は\x01",
            "客にも人気があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "くっく、マスターは\x01",
            "気が気じゃねえみたいだがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DD")

    Jump("loc_2BF7")

    label("loc_28E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DC")

    #C0115
    ChrTalk(
        0x9,
        (
            "うちは場末の宿酒場～。\x01",
            "街の一番端っこで～す♪\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "……つーことはつまり、\x01",
            "旧市街に一番近い店ってことだ。\x01",
            "不良どもの被害も一番被ってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "あの赤い服の連中なんざ\x01",
            "２日に一度はぶらついてやがるんだ。\x01",
            "やれやれだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A42")

    label("loc_29DC")


    #C0118
    ChrTalk(
        0x9,
        (
            "旧市街のガキどもは\x01",
            "この辺りでも悪名高いぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "とにかく柄が悪いからな、\x01",
            "近づかねえ方がいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A42")

    Jump("loc_2BF7")

    label("loc_2A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8D")

    #C0120
    ChrTalk(
        0x9,
        (
            "いよう、いらっしゃい。\x01",
            "こんな場末の宿酒場へようこそっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "この辺りの街並みは\x01",
            "ごっちゃごちゃしてるだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "クロスベルが共和国領だった頃に\x01",
            "東方系移民が沢山住み着いたんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "その後も方々からの移民が混じって\x01",
            "今じゃどこの国籍やら。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "ま、ごった煮っぽくて\x01",
            "俺は嫌いじゃないけどな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BF7")

    label("loc_2B8D")


    #C0125
    ChrTalk(
        0x9,
        (
            "お客さんは観光かい？\x01",
            "それともクロスベル人？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "ま、どっちゃでもいいや。\x01",
            "なんか注文してってくれや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF7")

    Return()

    # Function_9_1A0E end

    def Function_10_2BF8(): pass

    label("Function_10_2BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C19")
    Call(0, 36)
    Return()

    label("loc_2C19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31F2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31EE")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",      # 0
            "魚を渡す\x01",      # 1
            "やめる\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C90"),
        (1, "loc_2D89"),
        (SWITCH_DEFAULT, "loc_31DA"),
    )


    label("loc_2C90")


    #C0127
    ChrTalk(
        0xFE,
        (
            "便利屋のヒト、こんにちは～。\x01",
            "……お魚、取ってきてくれたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "サンサンのお願いは\x01",
            "『とっても細長い魚』を５匹よ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "他のお魚でも料理できなくないけど……\x01",
            "その時でも、同じ種類の魚を\x01",
            "５匹でお願いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "予約のお客さま、５名様だもの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E9")

    label("loc_2D89")

    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E19")

    #C0131
    ChrTalk(
        0xA,
        (
            "あう～、お魚５匹\x01",
            "持ってないみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "お魚は同じ種類で\x01",
            "５匹ないとだめね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "予約のお客さま、\x01",
            "５名様だもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_2E19")

    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7A")

    #C0134
    ChrTalk(
        0xA,
        "そう……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "お客さん、今晩きちゃうの。\x01",
            "なるべく早くお願いね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E9")

    label("loc_2E7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F19")

    #C0136
    ChrTalk(
        0xA,
        (
            "これは……\x01",
            "そう、この『細長い魚』よ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "おドンブリにするととっても美味しい。\x01",
            "ちゃんと５匹あるし……\x01",
            "……サンサンに譲ってくれる？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F4")

    label("loc_2F19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3012")

    #C0138
    ChrTalk(
        0xA,
        (
            "これは…………？？\x01",
            "とっても細長いけど、なんか光ってるよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "う～ん……う～ん……\x01",
            "いつものお魚と違うけど……\x02",
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
            "似てるし、きっと大丈夫よ～。\x01",
            "ちゃんと５匹あるし……\x01",
            "……サンサンに譲ってくれる？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F4")

    label("loc_3012")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_308B")

    #C0141
    ChrTalk(
        0xA,
        "？　これは……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "あう～、これ魚違うよ？\x01",
            "お魚でないとだめよ～！\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30F4")

    label("loc_308B")


    #C0143
    ChrTalk(
        0xA,
        "これは……『細長い魚』じゃないみたい。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "でも同じ種類で５匹あるね。\x01",
            "……サンサンに譲ってくれる？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3108")
    Jump("loc_31E9")

    label("loc_3108")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【譲る】\x01",            # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3160")
    Call(0, 37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31E9")

    label("loc_3160")


    #C0145
    ChrTalk(
        0xA,
        (
            "そう……\x01",
            "……仕方ないよ。\x01",
            "便利屋のヒトも都合があるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "でもまた気が向いたら\x01",
            "サンサンにゆずってほしいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D5")

    Jump("loc_31E9")

    label("loc_31DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31E9")

    label("loc_31E9")

    Jump("loc_2C43")

    label("loc_31EE")

    TalkEnd(0xFE)
    Return()

    label("loc_31F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_325C")

    #C0147
    ChrTalk(
        0xA,
        (
            "これで今晩のお客さんも\x01",
            "喜んでくれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "ふふっ、今日はありがとね\x01",
            "便利屋のヒト～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_403B")

    label("loc_325C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F2")

    #C0149
    ChrTalk(
        0xFE,
        "リーシャ、何かあったのかな。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "昼間、少し話したけど\x01",
            "チョット元気が無かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "また……心配事でもあるのかな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3351")

    label("loc_32F2")


    #C0152
    ChrTalk(
        0xFE,
        (
            "私、リーシャが隠していても判る。\x01",
            "リーシャなにか心配事があるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "何かあったのかな……\x02",
    )

    CloseMessageWindow()

    label("loc_3351")

    Jump("loc_403B")

    label("loc_3356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F9")

    #C0154
    ChrTalk(
        0xFE,
        (
            "パックとルースが\x01",
            "お店を手伝いたいんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ふふ、私からパパに頼んだら\x01",
            "一発ＯＫだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "パパ、そういう所は優しいもの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3463")

    label("loc_33F9")


    #C0157
    ChrTalk(
        0xFE,
        (
            "パックとルースが手伝ってくれて\x01",
            "お店も楽になりそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "ふふ、お客さんにもっと\x01",
            "サービスできそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3463")

    Jump("loc_403B")

    label("loc_3468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_352D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FD")

    #C0159
    ChrTalk(
        0xFE,
        (
            "パックとルース、\x01",
            "いつも楽しそうね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "わたし２人とは\x01",
            "日曜学校で一緒だったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "いつも仲がよくて羨ましいよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3528")

    label("loc_34FD")


    #C0162
    ChrTalk(
        0xFE,
        (
            "パックとルース、\x01",
            "いつも楽しそうね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3528")

    Jump("loc_403B")

    label("loc_352D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_35D1")

    #C0163
    ChrTalk(
        0xFE,
        (
            "お店の手伝い始めて\x01",
            "もう４ヶ月ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "お給仕に皿洗いにベッドメイク。\x01",
            "ピカピカにするととっても楽しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        "お客さん喜んでくれると嬉しくなるね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_403B")

    label("loc_35D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_36D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3693")

    #C0166
    ChrTalk(
        0xFE,
        (
            "聞いて聞いて～！\x01",
            "今日はリーシャと\x01",
            "百貨店に行く約束なの！\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "リーシャ、今日はお休みなんだって。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "ふふっ、記念祭は忙しかったけど\x01",
            "今日はたくさん遊べそうよ～㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36D2")

    label("loc_3693")


    #C0169
    ChrTalk(
        0xFE,
        (
            "もうすぐ待ち合わせの時間なの。\x01",
            "ふふっ、今日は楽しみよ～㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D2")

    Jump("loc_403B")

    label("loc_36D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_37D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3786")

    #C0170
    ChrTalk(
        0xFE,
        (
            "記念祭が近いと大忙しなの。\x01",
            "サンサンもお仕事頑張らないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "でも……今日はなんだか\x01",
            "パパが睨んでるみたいよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "私、何か失敗したかな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37CE")

    label("loc_3786")


    #C0173
    ChrTalk(
        0xFE,
        (
            "時々パパの視線を感じるの。\x01",
            "……サンサン、今日は\x01",
            "お皿割ってないよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CE")

    Jump("loc_403B")

    label("loc_37D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_38A3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3848")

    #C0174
    ChrTalk(
        0xFE,
        (
            "あのお客さん来ると、\x01",
            "パパがピリピリするの。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "どうして？\x01",
            "そんなに怖いことないよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_389E")

    label("loc_3848")


    #C0176
    ChrTalk(
        0xFE,
        (
            "せっせっ……\x01",
            "今日も店の手伝い順調よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "色んなお客さんと話するの、\x01",
            "楽しいね♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389E")

    Jump("loc_403B")

    label("loc_38A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_399A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3949")

    #C0178
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "リーシャ、最近少し悩んでるみたい。\x01",
            "ぼーっとしてる事が多いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの団員だと\x01",
            "やっぱり色々大変なのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3995")

    label("loc_3949")


    #C0180
    ChrTalk(
        0xFE,
        (
            "リーシャ、最近\x01",
            "少し悩んでるみたい。\x01",
            "私も力になれればいいんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3995")

    Jump("loc_403B")

    label("loc_399A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4A")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0181
    ChrTalk(
        0xFE,
        "……聞いて聞いて！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "リーシャって、あの\x01",
            "アルカンシェルの団員だそうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "きゃっ、何だかすごい！\x01",
            "私も憧れちゃう～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AB9")

    label("loc_3A4A")


    #C0184
    ChrTalk(
        0xFE,
        (
            "私の友達のリーシャ、\x01",
            "アルカンシェルの\x01",
            "団員だったみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "はあ、すごいな～。\x01",
            "私も憧れちゃうよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB9")

    Jump("loc_403B")

    label("loc_3ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA7")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0186
    ChrTalk(
        0xFE,
        "……あのね、あのね！\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "最近ね、かわいい\x01",
            "お客さん来てくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "リーシャという子。\x01",
            "近くに引っ越してきたそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "私と同い年と言っていた。\x01",
            "ふふっ、友達になれるといいな♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C11")

    label("loc_3BA7")


    #C0190
    ChrTalk(
        0xFE,
        (
            "リーシャ、近くに\x01",
            "引っ越してきたそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "私と同い年と言っていた。\x01",
            "ふふっ、友達になれるといいな♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C11")

    Jump("loc_403B")

    label("loc_3C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0A")

    #C0192
    ChrTalk(
        0xFE,
        (
            "私、今年に\x01",
            "日曜学校を卒業したばかりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "色々考えたけど……\x01",
            "やっぱりお店を手伝うことにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "だってパパはいつも気難しい顔ばかり。\x01",
            "お客さんを睨みつけたりするんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "このままじゃお店が心配よ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D7E")

    label("loc_3D0A")


    #C0196
    ChrTalk(
        0xFE,
        (
            "パパに任せていたらお店が心配。\x01",
            "だから私が手伝うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "まだ少し慣れないけど……\x01",
            "そこはスマイル、スマイル～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D7E")

    Jump("loc_403B")

    label("loc_3D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3EFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E8C")

    #C0198
    ChrTalk(
        0xFE,
        (
            "週末にはね、警備隊の人が\x01",
            "大勢で食べに来てくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "ふふ、色んな人と\x01",
            "お知り合いになれて楽しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "でも……みんなお仕事大変そうよ。\x01",
            "非番だからってぐてーっとしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "ふむむっ、やっぱり\x01",
            "サンサンが励ましてあげないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EF6")

    label("loc_3E8C")


    #C0202
    ChrTalk(
        0xFE,
        (
            "うちにはよく\x01",
            "警備隊の人も来てくれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "みんなお仕事大変そう。\x01",
            "サンサンが励ましてあげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF6")

    Jump("loc_403B")

    label("loc_3EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3F64")

    #C0204
    ChrTalk(
        0xFE,
        "お食事、どうだった？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "ふふ、なかなか美味しかったでしょ。\x01",
            "パパの料理は天下一品ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_403B")

    label("loc_3F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_403B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FEC")

    #C0206
    ChrTalk(
        0xFE,
        "あら、可愛いお客さん～。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "お食事？　お泊り？\x01",
            "どっちもまだ空きがあるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "遠慮せず注文してよ～㈱\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_403B")

    label("loc_3FEC")


    #C0209
    ChrTalk(
        0xFE,
        (
            "ウチは食事もお泊りも\x01",
            "できる宿酒場なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "ふふ、遠慮せず注文してよ～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_403B")

    TalkEnd(0xFE)
    Return()

    # Function_10_2BF8 end

    def Function_11_403F(): pass

    label("Function_11_403F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40D3")
    Jump("loc_411D")

    label("loc_40D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_411D")

    label("loc_40F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4113")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_411D")

    label("loc_4113")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_411D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E7")

    #C0211
    ChrTalk(
        0xFE,
        "おっと、夕暮れか……\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "むしゃむしゃ、ぱくぱく……\x01",
            "早いこと食って出かけねえと。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "共和国とのトラック便、\x01",
            "今日中にもう一往復だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_423E")

    label("loc_41E7")


    #C0214
    ChrTalk(
        0xFE,
        (
            "共和国とのトラック便、\x01",
            "今日中にもう一往復だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "近頃本数が増えて参っちまうぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_423E")

    Jump("loc_4EF5")

    label("loc_4243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4372")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431B")

    #C0216
    ChrTalk(
        0xFE,
        (
            "昨日『リゼロ貿易会社』ってとこに\x01",
            "配達に行ったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "社長がいなくなったとか言って、\x01",
            "社員たちが大騒ぎしてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "詳しいことは知らねえが……\x01",
            "ハンコを貰うのが大変だったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_436D")

    label("loc_431B")


    #C0219
    ChrTalk(
        0xFE,
        (
            "あの会社の社長さん、\x01",
            "どうしちまったんだろうな。\x01",
            "旅行にでも行っちまったのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_436D")

    Jump("loc_4EF5")

    label("loc_4372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4426")

    #C0220
    ChrTalk(
        0xFE,
        (
            "最近街道を走ってると\x01",
            "黒い運搬車とすれ違うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "運転手はたいてい\x01",
            "黒いグラサンで\x01",
            "会釈一つしない男でな……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "すれ違うだけで不気味な感じだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_448C")

    label("loc_4426")


    #C0223
    ChrTalk(
        0xFE,
        (
            "あの運搬車はたしか\x01",
            "帝国製で高価なはずだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "あんなのを使ってる\x01",
            "運送会社なんてあったかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448C")

    Jump("loc_4EF5")

    label("loc_4491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_45A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4551")

    #C0225
    ChrTalk(
        0xFE,
        (
            "最近、トラック便の\x01",
            "往復本数が増えたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "共和国まで１日４往復……\x01",
            "いくらトラックでも大変だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "ま、その分お給料も上がったから\x01",
            "文句は言わねえけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_459E")

    label("loc_4551")


    #C0228
    ChrTalk(
        0xFE,
        (
            "最近、トラック便の\x01",
            "往復本数が増えたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "この仕事も楽じゃねえぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_459E")

    Jump("loc_4EF5")

    label("loc_45A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4620")

    #C0230
    ChrTalk(
        0xFE,
        "もぐもぐ、がつがつ……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "…………………………\x01",
            "……うっ………………！\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "さ、さすがに食いすぎたかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EF5")

    label("loc_4620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_46A0")

    #C0233
    ChrTalk(
        0xFE,
        (
            "共和国方面の道が復旧したんで\x01",
            "これからまだドライブなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "食える時に食っておかねえとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF5")

    label("loc_46A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479B")

    #C0235
    ChrTalk(
        0xFE,
        (
            "共和国で事故ったトラック、\x01",
            "実は密輸品を積んでたって噂だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "ラインフォルト社製の\x01",
            "最新型の運搬車だったとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "……もしかして、\x01",
            "ただの事故じゃねえのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "くわばら、くわばら……\x01",
            "関わりたくねえもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4821")

    label("loc_479B")


    #C0239
    ChrTalk(
        0xFE,
        (
            "共和国で事故ったトラックは\x01",
            "密輸品を積んだ運搬車だったらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "もしかして、ただの事故じゃねえのか？\x01",
            "くわばら、くわばら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4821")

    Jump("loc_4EF5")

    label("loc_4826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_48EB")

    #C0241
    ChrTalk(
        0xFE,
        (
            "会社から連絡があって、共和国方面は\x01",
            "トラック事故の後片付けが終わるまで\x01",
            "配達はナシになったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "なんだか噂じゃ\x01",
            "結構酷い事故だったらしいぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "オレも詳しくは知らないんだが。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EF5")

    label("loc_48EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_49E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AF")

    #C0244
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……また共和国の方で\x01",
            "トラック事故があったらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "よく分からんが\x01",
            "共和国の軍も動いてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "街道が規制されちまって\x01",
            "ほとんど通れないんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_49E4")

    label("loc_49AF")


    #C0247
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……今日は急いでも\x01",
            "仕方なさそうだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E4")

    Jump("loc_4EF5")

    label("loc_49E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4A56")

    #C0248
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "そういや近頃\x01",
            "警備隊が出動してるらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "演習でもやってるのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EF5")

    label("loc_4A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B08")

    #C0251
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "俺の相棒は帝国方面の\x01",
            "輸送トラックを走らせてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "あっちは国境を越えるのが\x01",
            "結構面倒らしいぜ。\x01",
            "俺も詳しくは知らねえけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B6A")

    label("loc_4B08")


    #C0254
    ChrTalk(
        0xFE,
        (
            "帝国方面の国境は\x01",
            "手続きが厳しいらしい……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "エレボニア帝国は\x01",
            "質実剛健の軍事大国だからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B6A")

    Jump("loc_4EF5")

    label("loc_4B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C58")

    #C0256
    ChrTalk(
        0xFE,
        (
            "共和国側の国境の街は\x01",
            "アルタイル市ってんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "それほど大きくはないが、\x01",
            "昔からクロスベルとの間を\x01",
            "行き来する人が多くてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "クロスベル側の国境、タングラム門は\x01",
            "いつもそこそこ混雑してるんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CD7")

    label("loc_4C58")


    #C0259
    ChrTalk(
        0xFE,
        (
            "共和国側の国境の街は\x01",
            "アルタイル市ってんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "東の街道をずーっと進んで、\x01",
            "タングラム門を超えれば\x01",
            "意外とすぐなんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD7")

    Jump("loc_4EF5")

    label("loc_4CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D9A")

    #C0261
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "導力トラックは\x01",
            "かなり高価なシロモノだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "でも今は政府が\x01",
            "助成金を出してくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "おかげでウチの会社も\x01",
            "どんどん数を揃えてるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E14")

    label("loc_4D9A")


    #C0265
    ChrTalk(
        0xFE,
        (
            "導力トラックを買うときは\x01",
            "政府が助成金を出してくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "おかげでどの会社も\x01",
            "導力トラックが主流になってきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E14")

    Jump("loc_4EF5")

    label("loc_4E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EBC")

    #C0267
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "俺は輸送トラックの運転手やってんだ。\x01",
            "共和国との間を毎日往復するのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "これが結構疲れるんだよ、\x01",
            "もぐもぐ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EF5")

    label("loc_4EBC")


    #C0270
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……今のうちに\x01",
            "腹ごしらえしとかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_403F end

    def Function_12_4EFD(): pass

    label("Function_12_4EFD")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5000")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FFB")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F86")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4F86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FA6")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FF6")

    label("loc_4FA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FC6")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FF6")

    label("loc_4FC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FDA")
    Jump("loc_4FF6")

    label("loc_4FDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_4FF6")

    Jump("loc_4F13")

    label("loc_4FFB")

    Jump("loc_5003")

    label("loc_5000")

    Call(0, 13)

    label("loc_5003")

    TalkEnd(0xC)
    Return()

    # Function_12_4EFD end

    def Function_13_5007(): pass

    label("Function_13_5007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5096")

    #C0271
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "何か食べていきます？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "……オレ、飲食店店員の\x01",
            "才能があるかもしれないんだ。\x01",
            "最近そんな気がしてきたぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5177")

    label("loc_5096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5177")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5113")

    #C0273
    ChrTalk(
        0xC,
        (
            "相棒のルースと\x01",
            "店を出す事を考えてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "……今はその準備期間、\x01",
            "下積み時代ってやつさ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5177")

    label("loc_5113")


    #C0275
    ChrTalk(
        0xC,
        (
            "大物になった人はみんな\x01",
            "下積み時代を経験してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "うん、きっとオレも\x01",
            "将来大物になるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5177")

    Return()

    # Function_13_5007 end

    def Function_14_5178(): pass

    label("Function_14_5178")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_520C")
    Jump("loc_5256")

    label("loc_520C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_522C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5256")

    label("loc_522C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_524C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5256")

    label("loc_524C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5256")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_528C")
    Call(0, 16)
    Jump("loc_5972")

    label("loc_528C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A7")
    Call(0, 16)
    Jump("loc_52FD")

    label("loc_52A7")


    #C0277
    ChrTalk(
        0xFE,
        (
            "明日は商工会の会長さんに\x01",
            "挨拶に行くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "今夜は眠れないよ。\x01",
            "ワクワク……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52FD")

    Jump("loc_5972")

    label("loc_5302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5446")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D9")

    #C0279
    ChrTalk(
        0xFE,
        (
            "記念祭の人ごみを見てから\x01",
            "商売のアイデアが\x01",
            "どんどん沸いてくるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "へへっ、やっぱりオレって\x01",
            "天性の才能があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "ここは商売人として\x01",
            "ばばーんとデビューするしかないよな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5441")

    label("loc_53D9")


    #C0282
    ChrTalk(
        0xFE,
        (
            "やっぱりオレって\x01",
            "天性の才能があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "ばばーんと商売をおこして\x01",
            "みんなに見せ付けてやるぜっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5441")

    Jump("loc_5972")

    label("loc_5446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_54E7")

    #C0284
    ChrTalk(
        0xFE,
        (
            "相棒との話を\x01",
            "ナシにすることを考えてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "だってルースの奴、\x01",
            "細かい事にうるさすぎだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "商売って、こう\x01",
            "もっと楽しくやるもんだろ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5972")

    label("loc_54E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5556")
    SetChrSubChip(0xD, 0x0)

    #C0287
    ChrTalk(
        0xFE,
        "ちぇっ、ルースの分からず屋め。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "オレにはじっちゃん譲りの\x01",
            "商売の才能があるんだって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5972")

    label("loc_5556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_55AA")

    #C0289
    ChrTalk(
        0xFE,
        "オレ、社長の才能があると思うんだ。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "あんたらもそう思うだろ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5972")

    label("loc_55AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_562C")

    #C0291
    ChrTalk(
        0xFE,
        (
            "ルースの奴、最近\x01",
            "理論の話ばっかするんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "店を持つ前からそんな話をしても\x01",
            "無駄だって言ってるのにな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5972")

    label("loc_562C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A9")

    #C0293
    ChrTalk(
        0xFE,
        (
            "ルースの奴は\x01",
            "理屈っぽすぎるんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "そんな堅苦しい考えで\x01",
            "商売が始められんのかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_56FD")

    label("loc_56A9")


    #C0295
    ChrTalk(
        0xFE,
        (
            "ルースの奴、もっと\x01",
            "オレみたいに大らかな人間を\x01",
            "見習った方がいいんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FD")

    Jump("loc_5972")

    label("loc_5702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5787")
    SetChrSubChip(0xD, 0x0)

    #C0296
    ChrTalk(
        0xFE,
        (
            "がつがつ……\x01",
            "店の手伝いとはいえ、\x01",
            "サンサンだって商売始めたんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "オレたちにできないはずが\x01",
            "ないっての！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5972")

    label("loc_5787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5891")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584F")

    #C0298
    ChrTalk(
        0xFE,
        (
            "相棒と話が合わなくてさ、\x01",
            "イアンって弁護士の先生に\x01",
            "相談したんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "……まずはどんな会社にするか\x01",
            "決めなきゃって呆れられちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "とほほ、そりゃそうだよね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_588C")

    label("loc_584F")


    #C0301
    ChrTalk(
        0xFE,
        (
            "会社を興すなら、まずは\x01",
            "どんな会社にするか決めなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588C")

    Jump("loc_5972")

    label("loc_5891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5906")
    SetChrSubChip(0xD, 0x0)

    #C0302
    ChrTalk(
        0xFE,
        (
            "つまりだな、やっぱり\x01",
            "社長は才能溢れるこのオレが……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        "ってルース、オレの話聞いてるのか！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5972")

    label("loc_5906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5972")

    #C0304
    ChrTalk(
        0xFE,
        "相棒と店を出すつもりなんだ。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "目指すはクロスベル一の会社！\x01",
            "やっぱ男は夢を持たなくちゃな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5972")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_5178 end

    def Function_15_597A(): pass

    label("Function_15_597A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59E3")

    #C0306
    ChrTalk(
        0xFE,
        (
            "商売を始める資金を稼ぐために\x01",
            "ここでバイトを始めたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        "時給が安くて泣けてくるぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_59E3")

    TalkEnd(0xFE)
    Return()

    # Function_15_597A end

    def Function_16_59E7(): pass

    label("Function_16_59E7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A7B")
    Jump("loc_5AC5")

    label("loc_5A7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A9B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AC5")

    label("loc_5A9B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ABB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AC5")

    label("loc_5ABB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AC5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5C32")
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BB1")

    #C0308
    ChrTalk(
        0xF,
        (
            "た、大変だぞパック……\x01",
            "こんなことを忘れていたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xF,
        (
            "店を開くには\x01",
            "開業資金がいるじゃないか！！\x02",
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
        "……あ、そういえば。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C2D")

    label("loc_5BB1")


    #C0312
    ChrTalk(
        0xF,
        (
            "だあああっ……なんで\x01",
            "こんな基本的なことを忘れてんだよ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "な、なんだよルース……\x01",
            "そりゃあお前だって同じだろっ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C2D")

    Jump("loc_6AE6")

    label("loc_5C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5DD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D16")
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0314
    ChrTalk(
        0xF,
        "……よし、完璧だぜ！\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xF,
        (
            "店の名前も決めたし\x01",
            "売る物も決めた……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xD,
        "社長も決めたしな！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xD,
        (
            "パック＆ルース総合商店！\x01",
            "まずは雑貨を扱うぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xF,
        (
            "っしゃあ、いよいよ\x01",
            "明日から本格始動だな！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5DCD")

    label("loc_5D16")


    #C0319
    ChrTalk(
        0xFE,
        (
            "間合いのいいことに、\x01",
            "さっき商工会の会長さんが\x01",
            "通りがかってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "仕入れ業者を紹介してくれたんだ。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "女神は俺たち見捨てちゃいなかった……\x01",
            "やっぱ信じる者は救われるんだな～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DCD")

    Jump("loc_6AE6")

    label("loc_5DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E96")

    #C0322
    ChrTalk(
        0xFE,
        (
            "フッ、今まで散々\x01",
            "うだつが上がらないだの\x01",
            "口先だけだのと言われてきたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        "とんだ見込み違いだと言ってやろう。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "ハハハ、本気になった\x01",
            "俺たちを見せてやるぜっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F64")

    label("loc_5E96")


    #C0325
    ChrTalk(
        0xFE,
        (
            "……そういや、知ってるか？\x01",
            "記念祭からここの宿に\x01",
            "２人組みの男たちが泊まってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "はは、冴えない連中でな。\x01",
            "いつも下らない話ばかりしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "ああいう連中はダメだよな。\x01",
            "きっと大成しないぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F64")

    Jump("loc_6AE6")

    label("loc_5F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_613F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60BB")
    SetChrSubChip(0xF, 0x0)

    #C0328
    ChrTalk(
        0xFE,
        (
            "くそっ、どうしても\x01",
            "話が合わないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        "よしパック、基本的な所から行くぞ！\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "ラーメンはやっぱ醤油味だよな！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    #C0331
    ChrTalk(
        0xD,
        "何いってんだよルース……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xD,
        (
            "醤油なんてダメだって。\x01",
            "味噌味に決まってるだろ！？\x02",
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
            "なにっ……！？\x01",
            "それだけは絶対許せねえな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_613A")

    label("loc_60BB")


    #C0334
    ChrTalk(
        0xFE,
        (
            "くそっ、どうして\x01",
            "俺たちはこう話が合わないんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "ダメだ……パックと\x01",
            "商売を始めようと思ったのは\x01",
            "間違いだったのかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_613A")

    Jump("loc_6AE6")

    label("loc_613F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6248")
    SetChrSubChip(0xF, 0x0)

    #C0336
    ChrTalk(
        0xFE,
        (
            "俺はＩＢＣのクロイス総裁の\x01",
            "自伝を読んで勉強したんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "会社を始めるには\x01",
            "ちゃんとした計算が必要なんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "だからぁ、オレはじっちゃんの\x01",
            "日記を読んで勉強したんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xD,
        (
            "商売は気合だ～っ！！\x01",
            "……って書いてあったぜ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_628C")

    label("loc_6248")

    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0340
    ChrTalk(
        0xFE,
        (
            "どうも話が\x01",
            "かみ合わねえんだよな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_628C")

    Jump("loc_6AE6")

    label("loc_6291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6380")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6359")

    #C0341
    ChrTalk(
        0xFE,
        "商売に一番必要なのは信用だ。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "ウチの会社は\x01",
            "こうこうっていう……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "その点はやっぱ俺だろ。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xD,
        "いやいや、オレじゃないの？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xD,
        "ルースは目つきが鋭すぎだもの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_637B")

    label("loc_6359")


    #C0346
    ChrTalk(
        0xFE,
        "見た目の問題じゃねえんだよ！\x02",
    )

    CloseMessageWindow()

    label("loc_637B")

    Jump("loc_6AE6")

    label("loc_6380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_64DD")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6485")

    #C0347
    ChrTalk(
        0xFE,
        (
            "むしゃむしゃ、ぱくぱく……\x01",
            "いいかパック、よく聞けよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "商品には原価と売価ってのがあってな、\x01",
            "売価が原価を上回る事によって……\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xD,
        "あはは、馬鹿だなルース～。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xD,
        "そんなの気合でなんとかなるだろ？\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "……ならねえよ！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64D8")

    label("loc_6485")


    #C0352
    ChrTalk(
        0xFE,
        (
            "まさかそこまで\x01",
            "分かってなかったとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        "大体お前は常識がなさ過ぎるぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_64D8")

    Jump("loc_6AE6")

    label("loc_64DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_663F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E9")
    SetChrSubChip(0xF, 0x0)

    #C0354
    ChrTalk(
        0xFE,
        (
            "くそっ、俺たち絶対\x01",
            "いつもだべってるダメ人間だと\x01",
            "思われてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "さっきの観光客なんて\x01",
            "俺たちを見て笑ってやがった……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        "パック、これもお前のせいだぞ。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        "いやいや、ルースのせいだって。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xD,
        "だってお前、今日寝癖ついてるもの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_663A")

    label("loc_65E9")


    #C0359
    ChrTalk(
        0xFE,
        "相棒と中々話が纏まらないんだ。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "パックの奴、\x01",
            "真面目にやる気あんのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_663A")

    Jump("loc_6AE6")

    label("loc_663F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_67BB")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6721")

    #C0361
    ChrTalk(
        0xFE,
        "むしゃむしゃ、ぱくぱく……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    #C0362
    ChrTalk(
        0xFE,
        (
            "パック、その饅頭は俺のだぞ？\x01",
            "勝手に食うなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xD,
        "がつがつ、ごくごく……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "ルースこそ餃子ばっか食うなよ。\x01",
            "息が臭くなるだろ～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_67B6")

    label("loc_6721")


    #C0365
    ChrTalk(
        0xFE,
        (
            "サンサンは昔から愛嬌があるしな。\x01",
            "まさに接客業にはうってつけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "って、サンサンの事はいいんだよ。\x01",
            "俺の言いたいのはだな、\x01",
            "むしゃむしゃ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67B6")

    Jump("loc_6AE6")

    label("loc_67BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6936")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D1")
    SetChrSubChip(0xF, 0x0)

    #C0367
    ChrTalk(
        0xFE,
        (
            "いまクロスベルで\x01",
            "一番ホットな商品、それは……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "導力車だ！\x02",
    )


    #C0369
    ChrTalk(
        0xD,
        "アルカンシェルのチケットだ！\x02",
    )

    OP_57(0x1)
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0370
    ChrTalk(
        0xFE,
        (
            "おいおいパック……\x01",
            "ダフ屋でも始める気かよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xD,
        (
            "知らねえのか？\x01",
            "アルカンシェルのチケット、\x01",
            "凄い人気なんだぜ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6931")

    label("loc_68D1")


    #C0372
    ChrTalk(
        0xFE,
        (
            "やっぱここは\x01",
            "カッコよく導力車だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "導力車は男のロマン……\x01",
            "あんたらもそう思うだろ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6931")

    Jump("loc_6AE6")

    label("loc_6936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_69E7")
    SetChrSubChip(0xF, 0x0)

    #C0374
    ChrTalk(
        0xFE,
        (
            "（さっき後ろの席にいた\x01",
            "  お姉さん、可愛かったなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xD,
        "ってルース、オレの話聞いてるのか！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0376
    ChrTalk(
        0xFE,
        (
            "え？　ああ……\x01",
            "何の話だっけ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AE6")

    label("loc_69E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6AE6")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AA2")

    #C0377
    ChrTalk(
        0xFE,
        (
            "#1P会社を興すとき、真っ先に\x01",
            "決めなきゃいけないものは……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        "#2P社長だ！\x02",
    )


    #C0379
    ChrTalk(
        0xFE,
        "#1P社名だ！\x02",
    )

    OP_57(0x1)

    #C0380
    ChrTalk(
        0xFE,
        "#1P……おい、社名だろ？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        "#2Pいやいや、社長だって。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6AE6")

    label("loc_6AA2")


    #C0382
    ChrTalk(
        0xFE,
        (
            "おいパック、まさか\x01",
            "自分が社長になるつもりじゃ\x01",
            "ねえだろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AE6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_59E7 end

    def Function_17_6AEE(): pass

    label("Function_17_6AEE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B82")
    Jump("loc_6BCC")

    label("loc_6B82")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BA2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6BCC")

    label("loc_6BA2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BC2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6BCC")

    label("loc_6BC2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6BCC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0383
    ChrTalk(
        0xFE,
        (
            "#1806Fふう、どこかお家賃の\x01",
            "安いところは無いかな……\x02\x03",

            "#1802F市庁舎で案内してもらったけど……\x01",
            "やっぱりこの辺りかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_6AEE end

    def Function_18_6C77(): pass

    label("Function_18_6C77")

    Call(0, 19)
    Return()

    # Function_18_6C77 end

    def Function_19_6C7B(): pass

    label("Function_19_6C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7059")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6D81")

    #C0384
    ChrTalk(
        0x13,
        (
            "……先輩はどうして\x01",
            "クロスベルタイムズの記者に？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x12,
        (
            "#2102Fん～そうねえ、\x01",
            "野次馬根性ってやつ？\x02\x03",

            "#2109F気になるじゃない。\x01",
            "有名人のゴシップとか\x01",
            "政界のスキャンダルとか。\x02",
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
            "気持ち良いくらい\x01",
            "正直ですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7051")

    label("loc_6D81")


    #C0387
    ChrTalk(
        0x12,
        (
            "#2105Fもぐもぐ……\x01",
            "へー、双子のお兄さんがいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x13,
        (
            "ははは……今は\x01",
            "オレド自治州で農業やってます。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x13,
        (
            "自分だけこっちに来て\x01",
            "記者を目指したんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6ED7")

    #C0390
    ChrTalk(
        0x102,
        (
            "#0100F（グレイスさん……\x01",
            "  同僚の方と食事中みたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#0003F（声を掛けないでおこう。\x01",
            "  絶対キーアに食いつきそうだ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x102,
        "#0106F（そ、そうね……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_704E")

    label("loc_6ED7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F9C")

    #C0393
    ChrTalk(
        0x103,
        (
            "#0200F（グレイスさん……\x01",
            "  同僚の方と食事中のようですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#0003F（声を掛けないでおこう。\x01",
            "  絶対キーアに食いつきそうだ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x103,
        "#0211F（容易に想像できますね……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_704E")

    label("loc_6F9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_704E")

    #C0396
    ChrTalk(
        0x104,
        (
            "#0300F（グレイスの姉さんか……\x01",
            "  同僚と食事中みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#0003F（声を掛けないでおこう。\x01",
            "  絶対キーアに食いつきそうだ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        "#0309F（だなぁ……）\x02",
    )

    CloseMessageWindow()

    label("loc_704E")

    SetScenarioFlags(0x1, 1)

    label("loc_7051")

    TalkEnd(0xFE)
    Jump("loc_706A")

    label("loc_7059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_706A")
    Call(0, 30)

    label("loc_706A")

    Return()

    # Function_19_6C7B end

    def Function_20_706B(): pass

    label("Function_20_706B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_70FF")
    Jump("loc_7149")

    label("loc_70FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_711F")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7149")

    label("loc_711F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_713F")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7149")

    label("loc_713F")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7149")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72A7")

    #C0399
    ChrTalk(
        0x103,
        "#0205F課長……こんな所に。\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x11,
        (
            "#1000Fよお、お前らか。\x02\x03",

            "どうだ、調査の方は順調か？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#0100Fええまあ、それなりに。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        (
            "#0000Fこれから\x01",
            "ウルスラ医科大学の方へ\x01",
            "向かってみるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x11,
        (
            "#1000Fクク、張り切ってるじゃねえか。\x02\x03",

            "#1003Fまあ適当に頑張っとけ。\x01",
            "後で報告を聞かせてもらうからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7332")

    label("loc_72A7")


    #C0404
    ChrTalk(
        0x11,
        (
            "#1000Fここのメシは美味いぞ。\x01",
            "昼飯がまだなら食っていけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x101,
        "#0000Fいえ、もう頂いてきたんで……\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x104,
        "#0300F課長は悠々自適っすねえ……\x02",
    )

    CloseMessageWindow()

    label("loc_7332")

    SetChrSubChip(0x11, 0x0)
    TalkEnd(0x11)
    Return()

    # Function_20_706B end

    def Function_21_733A(): pass

    label("Function_21_733A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_760B")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73D7")
    Jump("loc_7421")

    label("loc_73D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_73F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7421")

    label("loc_73F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7417")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7421")

    label("loc_7417")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7421")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_74D9")

    #C0407
    ChrTalk(
        0xFE,
        (
            "七耀石の結晶を買い付けることが\x01",
            "大商人たるお父様に\x01",
            "近づくための第一歩……！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "観光も楽しんだし、\x01",
            "そろそろ踏み出すとしましょ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75FF")

    label("loc_74D9")


    #C0409
    ChrTalk(
        0xFE,
        (
            "ふふふ、クロスベル観光は\x01",
            "みっちり楽しめたことだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "そろそろ、\x01",
            "お目当ての『七耀石の結晶』を\x01",
            "買い付けに行くとしましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "街の西口から鉱山町マインツへの\x01",
            "定期バスが出てるらしいし、\x01",
            "それに乗ればらくらくね。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "大商人たるお父様に\x01",
            "近づくための第一歩……！\x01",
            "いよいよ踏み出すわよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_75FF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_77D7")

    label("loc_760B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_7683")

    #C0413
    ChrTalk(
        0xFE,
        (
            "空港からこっちに来る時に\x01",
            "確かでっかいデパートがあったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        "まずはあそこに行ってみようかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_77D4")

    label("loc_7683")

    OP_4B(0x15, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x14, 0x15, 0)
    TurnDirection(0x15, 0x14, 0)

    #C0415
    ChrTalk(
        0x14,
        "まずは、これから１ヵ月は下調べね。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x14,
        "とりあえず市内をぐるっと散策して……\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x15,
        "えっ……？\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x15,
        (
            "あのう……お嬢様。\x01",
            "七耀石の買い付けは\x01",
            "どうなさるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x14,
        "えっ？　何言ってるのよ。\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x14,
        (
            "折角クロスベルくんだりまで来て\x01",
            "商売だけなんて\x01",
            "もったいないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x15,
        "（観光する気まんまんですぅ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    OP_4C(0x15, 0xFF)
    OP_4C(0x14, 0xFF)

    label("loc_77D4")

    TalkEnd(0xFE)

    label("loc_77D7")

    Return()

    # Function_21_733A end

    def Function_22_77D8(): pass

    label("Function_22_77D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7870")

    #C0422
    ChrTalk(
        0xFE,
        (
            "……クロスベルには\x01",
            "商品の買い付けに来たのに、\x01",
            "結局１ヶ月も観光してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "帝国のお屋敷は\x01",
            "今頃どうしてるでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7907")

    label("loc_7870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_78F6")

    #C0424
    ChrTalk(
        0xFE,
        (
            "七耀石の買い付けが終わったら\x01",
            "すぐ帰れると思ってたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "お嬢様ったら\x01",
            "しばらく観光する気まんまんです……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7907")

    label("loc_78F6")

    TurnDirection(0x14, 0x15, 0)
    TurnDirection(0x15, 0x14, 0)
    Call(0, 21)

    label("loc_7907")

    TalkEnd(0xFE)
    Return()

    # Function_22_77D8 end

    def Function_23_790B(): pass

    label("Function_23_790B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7BC5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_79A1")

    #C0426
    ChrTalk(
        0x16,
        (
            "ポエマーの道か……\x01",
            "それもいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x16,
        (
            "こっちに来て一度挫折したけど……\x01",
            "また始めてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A50")

    label("loc_79A1")


    #C0428
    ChrTalk(
        0x16,
        (
            "……久しぶりの失恋で\x01",
            "心がいよいよくじけそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x16,
        (
            "なぁリックス。\x01",
            "僕は一体どうすれば\x01",
            "よかったのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        (
            "#0006F（気の毒だけど……\x01",
            "  ここはそっとしておこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_7A50")

    Jump("loc_7BC0")

    label("loc_7A55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7A6A")
    Call(0, 29)
    Jump("loc_7BC0")

    label("loc_7A6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7B33")

    #C0431
    ChrTalk(
        0x16,
        (
            "まさか、最後に行き着いた先で\x01",
            "あの子のお姉さんに会えるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x16,
        (
            "リックス、これは間違いなく\x01",
            "運命というやつだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x16,
        (
            "僕は彼女と運命で繋がってるんだ。\x01",
            "ハハハ、うれしいなっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BC0")

    label("loc_7B33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_7B48")
    Call(0, 28)
    Jump("loc_7BC0")

    label("loc_7B48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7B5C")
    Call(0, 27)
    Jump("loc_7BC0")

    label("loc_7B5C")


    #C0434
    ChrTalk(
        0x16,
        (
            "なぁリックス、\x01",
            "今度こそ僕の願いは叶うかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x16,
        (
            "今頃あの子はどこで\x01",
            "なにをしているんだろう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BC0")

    Jump("loc_7C85")

    label("loc_7BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_7C14")

    #C0436
    ChrTalk(
        0xFE,
        (
            "名前もなにも知らない彼女……\x01",
            "今頃どこで何をしてるんだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C85")

    label("loc_7C14")


    #C0437
    ChrTalk(
        0xFE,
        (
            "世界の全てから見捨てられた僕に\x01",
            "天使が舞い降りたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "今頃あの子はどこで\x01",
            "なにをしているんだろう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_7C85")

    TalkEnd(0xFE)
    Return()

    # Function_23_790B end

    def Function_24_7C89(): pass

    label("Function_24_7C89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F76")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D2F")

    #C0439
    ChrTalk(
        0x17,
        "元気を出せよ、アントン。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x17,
        (
            "なんだったらまた、\x01",
            "ポエマーの道を\x01",
            "志せばいいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x17,
        (
            "今なら悲恋の詩が\x01",
            "書けるかもしれないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F71")

    label("loc_7D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7DBB")

    #C0442
    ChrTalk(
        0x17,
        (
            "アントンは、君たちの報告を\x01",
            "今か今かと待っているみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x17,
        (
            "そんなに会いたいなら、\x01",
            "自分で会いに行けばいいのにな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F71")

    label("loc_7DBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7E7F")

    #C0444
    ChrTalk(
        0x17,
        (
            "アントンは運命だとか\x01",
            "そういう努力なしに手に入るものに\x01",
            "すこぶる弱いのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x17,
        (
            "本当にその子と運命で結ばれてるなら、\x01",
            "自分で警察に行っていれば\x01",
            "すでに出会えていたはずだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F71")

    label("loc_7E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7EFF")

    #C0446
    ChrTalk(
        0x17,
        (
            "もう３週間も延長して\x01",
            "こっちに滞在しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x17,
        (
            "アントンといると\x01",
            "予想外のことが起きて\x01",
            "おもしろいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F71")

    label("loc_7EFF")


    #C0448
    ChrTalk(
        0x17,
        (
            "受けてくれるかは分からないけど、\x01",
            "とりあえず依頼は出したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x17,
        (
            "少しは落ち着いて待つのも\x01",
            "大事だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F71")

    Jump("loc_80C2")

    label("loc_7F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8000")

    #C0450
    ChrTalk(
        0xFE,
        (
            "アントンのサイフ探しを\x01",
            "手伝ってくれた女の子を探してるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "名前も聞かずに別れてしまうのも\x01",
            "実にアントンらしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80C2")

    label("loc_8000")


    #C0452
    ChrTalk(
        0xFE,
        (
            "サイフを落としたアントンを\x01",
            "通りがかった女の子が\x01",
            "親切にも手伝ってくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xFE,
        (
            "アントンは彼女に\x01",
            "運命的なものを感じたらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "帰国予定を伸ばして\x01",
            "彼女を探している最中なのさ。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)

    label("loc_80C2")

    TalkEnd(0xFE)
    Return()

    # Function_24_7C89 end

    def Function_25_80C6(): pass

    label("Function_25_80C6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_815A")
    Jump("loc_81A4")

    label("loc_815A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_817A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81A4")

    label("loc_817A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_819A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81A4")

    label("loc_819A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81A4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_83D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_8249")

    #C0455
    ChrTalk(
        0x18,
        (
            "#1602F伝説の殺し屋か……面白ぇ。\x02\x03",

            "俺らの縄張りに乗り込んで来たら\x01",
            "是非ともやり合ってみたいモンだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83D0")

    label("loc_8249")


    #C0456
    ChrTalk(
        0x18,
        (
            "#1603Fそういや、\x01",
            "《黒月#4Rヘイユエ#》といったか……\x02\x03",

            "#1600F最近、あの東方人どもが\x01",
            "調子に乗ってるみたいじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        "#0005Fどこでそれを……\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#0301Fもう結構、あちこちで\x01",
            "噂は広まってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x18,
        (
            "#1602Fフン、旧市街にも色々と\x01",
            "噂は集まってくるからな。\x02\x03",

            "#1604F何でも凄腕の殺し屋とやらを\x01",
            "雇ってるらしいが……クク。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#0006F……くれぐれも喧嘩を\x01",
            "吹っかけたりしないでくれよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_83D0")

    Jump("loc_85D1")

    label("loc_83D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_8459")

    #C0461
    ChrTalk(
        0x18,
        (
            "#1603Fフン……ウチの連中に\x01",
            "朝稽古を付けてやったから\x01",
            "腹が減って仕方ねぇぜ。\x02\x03",

            "#1600Fチッ、とっとと持って来やがれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85D1")

    label("loc_8459")


    #C0462
    ChrTalk(
        0x18,
        "#1600Fア、なんだテメエらか。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#0000Fあんたか……\x01",
            "この店はよく使うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x18,
        (
            "#1603Fフン、まあな。\x01",
            "店主はうるせぇオヤジだが\x01",
            "味は悪くねぇ。\x02\x03",

            "#1602Fクク、ウェイトレスも\x01",
            "けっこう色っぽいしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        "#0309Fおお、それは同感だぜ。\x02",
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
        "#0106Fまったく……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#0211Fランディさん、\x01",
            "節操なさすぎです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_85D1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_80C6 end

    def Function_26_85D9(): pass

    label("Function_26_85D9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_866D")
    Jump("loc_86B7")

    label("loc_866D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_868D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_86B7")

    label("loc_868D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_86B7")

    label("loc_86AD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86B7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8835")

    #C0468
    ChrTalk(
        0x19,
        (
            "オゥ釘バットでボコボコォ！\x01",
            "テスタメンツは血祭りィィ～ッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x19,
        "……むしゃむしゃ、ごっくん。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x19,
        (
            "ン～、デザートは\x01",
            "プリンにすっかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8825")
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
            "#0006F（歌うか食べるか注文するか、\x01",
            "  どれかにすればいいのに……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8825")

    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x19, 0x1)
    TalkEnd(0xFE)
    Return()

    label("loc_8835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_88A8")

    #C0472
    ChrTalk(
        0x19,
        "にしても腹減っちまったな～。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x19,
        (
            "オゥ、ヤァ、腹減ったァ～！\x01",
            "早くぅ、メシ、持って来い～……っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88F8")

    label("loc_88A8")


    #C0474
    ChrTalk(
        0x19,
        "なンだ～、サツの連中じゃん？\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x19,
        (
            "ひゃは、俺らの\x01",
            "邪魔すンじゃねえぞ～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_88F8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_85D9 end

    def Function_27_8900(): pass

    label("Function_27_8900")

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
        "#12P女神様、お願いします……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x16,
        (
            "#12P可憐なあの子に\x01",
            "今一度会えますように……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#5P#0000Fえっと……\x01",
            "アントンさん、ですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)

    #C0479
    ChrTalk(
        0x16,
        (
            "#12Pん、そうだけど……\x01",
            "そういう君たちは？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        (
            "#5P#0000Fクロスベル警察・特務支援課の者です。\x01",
            "支援要請を見て伺ったのですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0481
    ChrTalk(
        0x16,
        (
            "#12Pおお……！\x01",
            "待ってたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x16,
        (
            "#12Pすぐにでも\x01",
            "お願いしたいことがあるんだ。\x01",
            "話を聞いてくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        "#5P#0000Fええ、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        (
            "#5P#0100F依頼では、ある女性を\x01",
            "探し出して欲しいという\x01",
            "話でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x16,
        (
            "#12Pああ、あの子を探し出して……\x01",
            "一言お礼を言いたいのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x16,
        (
            "#12Pこの僕を闇の中から\x01",
            "救ってくれた彼女にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#5P#0001F……なにか事情があるんですね？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x16,
        (
            "#12P僕はリベール王国出身でね。\x01",
            "友達のリックスと一緒に\x01",
            "このクロスベルに旅行に来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        (
            "#12P何もいい事のない人生……\x01",
            "華やかな場所に来れば\x01",
            "何かが変わると思ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        "#5P#0003Fは、はぁ……\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x16,
        (
            "#12Pだが結局……\x01",
            "ここでも冷たい現実が\x01",
            "突きつけられてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x16,
        (
            "#12Pあろうことか……\x01",
            "旅費の入ったサイフを\x01",
            "丸々落としてしまったのさ。\x02",
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
        "#5P#0006Fそれはその、お気の毒に……\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x16,
        (
            "#12P……ああ、そうさ。\x01",
            "僕は果てしなく鈍くさい\x01",
            "ダメダメ野郎なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "#12Pリックスにも\x01",
            "手伝ってもらったけど、\x01",
            "結局サイフは見つからなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x16,
        (
            "#12P途方に暮れた僕は、\x01",
            "全てを諦めてリックスにミラを借り、\x01",
            "リベールへ戻ろうと思った。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x16,
        (
            "#12Pそのときだった……\x01",
            "僕に優しく手を差し伸べる\x01",
            "あの娘さんが現れたのは。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x104,
        (
            "#5P#0300Fへぇ……そりゃ羨ましいねぇ。\x01",
            "なかなかいないぜ、そんないい娘。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x16,
        (
            "#12Pああ、そして……\x01",
            "彼女のおかげで失ったサイフは\x01",
            "無事、手元に戻ってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x16,
        (
            "#12Pその時、僕は確信した。\x01",
            "これは運命の出会いなんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x16,
        (
            "#12P暗黒に包まれた僕の心に\x01",
            "優しく手を差し伸べた彼女は\x01",
            "まるで天使のようだった……\x02",
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
            "#5P#0006Fえ、え～っと……\x01",
            "要するに、その娘さんを\x01",
            "捜索して欲しい、と？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x16,
        "#12Pああ、そういうことだ。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "#12P予定より３週間も長く\x01",
            "こっちに滞在してるんだけど、\x01",
            "手がかりが全くなしでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x16,
        (
            "#12P一応遊撃士協会にも\x01",
            "頼んだんだけど、\x01",
            "断られてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x16,
        (
            "#12Pその子が行方不明とかならまだしも、\x01",
            "緊急性も薄いなら他の依頼を\x01",
            "優先したいんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "#12P全く、リベールだったら\x01",
            "お酒の飲み比べの手助けまで\x01",
            "してくれたっての……に……\x02",
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
            "どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x16,
        (
            "#12P……いや、ちょっと古傷がね。\x01",
            "ま、まぁ、それはともかく……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x16,
        (
            "#12P街で噂を聞いたリックスが、\x01",
            "僕の代わりに君たちに\x01",
            "依頼を出してくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x16,
        (
            "#12P君たち警察も、遊撃士みたいな\x01",
            "サービスをしてるんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x16,
        "#12P僕の依頼、受けてくれるよな？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#5P#0006Fえ、えっと、そうですね……\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x109,
        (
            "#5P#0505F……特務支援課って\x01",
            " こんな事までするんですか？\x02\x03",

            "#0500Fその……随分仕事の幅が\x01",
            "広いんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x102,
        (
            "#5P#0106F依頼としては\x01",
            "珍しい類だと思うけど……\x02\x03",

            "#0100Fどうする？　ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x103,
        (
            "#11P#0203F……正直、色恋沙汰に\x01",
            "警察が首を突っ込むのはどうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x101,
        "#5P#0003F（ううん、そうなんだよな……）\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x104,
        (
            "#5P#0304F相手の子の顔だけでも\x01",
            "拝んでみたい気はするけどな。\x02\x03",

            "#0300F……ちなみに、その子は\x01",
            "どういう感じなんだ？\x02\x03",

            "#0309Fさぞ、カワイコちゃん\x01",
            "なんだろうなぁ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x16,
        (
            "#12Pああ、あの姿は今でも\x01",
            "目に焼きついているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x16,
        (
            "#12P人の荒んだ心を落ち着かせる\x01",
            "あのフンワリした雰囲気。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x16,
        (
            "#12P彼女の優しさが滲み出るような\x01",
            "間延びした喋り方。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x16,
        (
            "#12Pそして、可愛さ溢れる\x01",
            "左右で結んだピンクブラウンの髪……\x02",
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
            "#5P#0005Fあれ、どこかで会ったような\x01",
            "雰囲気の子だな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x102,
        "#5P#0103Fそうねぇ……\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x103,
        (
            "#11P#0200Fそういう方と何度も\x01",
            "顔をあわせている気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x104,
        (
            "#5P#0306Fつーか……どう考えても、\x01",
            "フランちゃんじゃねえのか？\x02",
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
        "#5P#0505Fあっ……そうかもしれません！\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x16,
        (
            "#12P……き、君たち……！\x01",
            "彼女を知っているのかい！？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x109,
        (
            "#5P#0503Fえっと、多分ですけど……\x02\x03",

            "#0500Fさっき言ってた\x01",
            "ピンクブラウンの髪って……\x01",
            "もしかして、私と同じ髪の色ですか？\x02",
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
        "#12Pああ、ああああああ！！！\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x16,
        (
            "#12P確かに同じだ！\x01",
            "同じ髪の色だよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x16,
        (
            "#12Pハッ！！\x01",
            "あなたは、もしかして……！？\x02",
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
            "#5P#0503Fえ、ええっと、\x01",
            "間違いじゃなければ……\x01",
            "多分、その子の姉です。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x16,
        "#12Pなんてこった……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x17, 500)

    #C0535
    ChrTalk(
        0x16,
        (
            "#12Pはは、聞いたかい、リックス。\x01",
            "これは間違いなく運命だよっ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)

    #C0536
    ChrTalk(
        0x17,
        (
            "#5Pアントンがそう思うなら\x01",
            "そうなのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x17,
        (
            "#5Pちがう可能性も\x01",
            "なきにしもあらずだけど。\x02",
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
            "#12Pそ、そそそそそのッ……\x01",
            "お姉さん！！\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x109,
        "#5P#0505Fは、はははははいっ！？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x16,
        (
            "#12P妹さんに、その……\x01",
            "恋人とか彼氏とかって\x01",
            "いるんですかっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x109,
        (
            "#5P#0505Fえ、ええぇっ！？\x02\x03",

            "#0503Fい、いえ、そんな話は\x01",
            "聞いてないです。\x02\x03",

            "#0508Fというか、\x01",
            "今は一緒に暮らしてないので\x01",
            "なんとも言えませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x16,
        (
            "#12Pと、とにかく……\x01",
            "リベールに帰る前に\x01",
            "一言お礼がしたいんですっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x16,
        (
            "#12P会えないか頼んでみて\x01",
            "くれませんかっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x109,
        "#5P#0503Fそ、そうですね……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0545
    ChrTalk(
        0x109,
        (
            "#5P#0500F……ロイドさん、私は\x01",
            "引き受けても構いませんが……？\x02",
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
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A012")

    #C0546
    ChrTalk(
        0x101,
        (
            "#5P#0000F分かりました、\x01",
            "お引き受けしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x16,
        "#12Pおおっ！　恩に着るよ！\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x16,
        (
            "#12Pそ、それじゃよろしくね。\x01",
            "何とかその子に会う約束を\x01",
            "取り付けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        (
            "#5P#0003Fそうと決まれば\x01",
            "さっそく警察本部に\x01",
            "行ってみるか。\x02\x03",

            "#0000Fたぶん、受付の方に\x01",
            "いるだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x109,
        (
            "#5P#0500Fええ、そうですね。\x01",
            "お供します。\x02",
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
            "クエスト【真心の恩返し】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2A, 0x1, 0x1)
    Jump("loc_A1FA")

    label("loc_A012")


    #C0552
    ChrTalk(
        0x101,
        (
            "#5P#0006Fえっと、すみませんけど\x01",
            "今はちょっと別件の用事が\x01",
            "入っていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x16,
        (
            "#12P……そうかい。\x01",
            "結局そうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x16,
        (
            "#12Pいつもこれなんだ。\x01",
            "誰も僕の話なんか聞いてくれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x16,
        (
            "#12Pいや、聞いてくれたとしても\x01",
            "良い結果なんてついてくる\x01",
            "わけがないんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        (
            "#5P#0012Fあ、あの……\x01",
            "そこまで落ち込まなくても。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x109,
        (
            "#5P#0505Fそ、そうですよ。\x01",
            "別に断るっていうわけじゃ\x01",
            "ないんですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x16,
        (
            "#12P……いいんだよ、\x01",
            "気を遣わなくても。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x16,
        (
            "#12Pでもそうだね、\x01",
            "期待はせずに待っているよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1FA")

    SetChrPos(0x0, -100000, 20, -53500, 180)
    OP_93(0x16, 0x10E, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_27_8900 end

    def Function_28_A22A(): pass

    label("Function_28_A22A")

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
        "#12P……警察の人達かい。\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x16,
        (
            "#12Pそうか……\x01",
            "本当に戻ってきてくれたんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x101,
        "#5P#0005Fえ、ええまあ。\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x16,
        (
            "#12Pそれで、あの子……\x01",
            "フランさんって言うんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x16,
        (
            "#12P会う約束……\x01",
            "取り付けてくれるかい？\x02",
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
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5AD")

    #C0565
    ChrTalk(
        0x101,
        (
            "#5P#0000F分かりました、\x01",
            "お引き受けしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x16,
        "#12P……おおっ、本当かい！\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x16,
        "#12P本当に本当の本当なんだね！？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#5P#0005Fえ、ええ、モチロンです。\x02\x03",

            "#0003F（この世の終わりみたいな\x01",
            "  顔をしてたのに……）\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x16,
        (
            "#12Pそ、それじゃよろしくね。\x01",
            "何とかその子に会う約束を\x01",
            "取り付けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそうと決まれば\x01",
            "さっそく警察本部に\x01",
            "行ってみるか。\x02\x03",

            "たぶん、受付の方に\x01",
            "いるだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x109,
        (
            "#5P#0500Fええ、そうですね。\x01",
            "お供します。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2A, 0x1, 0x1)
    Jump("loc_A6E8")

    label("loc_A5AD")


    #C0572
    ChrTalk(
        0x101,
        (
            "#5P#0006Fえ、えっと、すみません。\x01",
            "今は用事が……\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x16,
        (
            "#12P……いや、いいんだ。\x01",
            "こんなのは慣れっこさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x16,
        (
            "#12Pいつもこうなんだ。\x01",
            "なにかやろうとして\x01",
            "上手くいったためしがない。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        (
            "#5P#0006F（め、面倒な人だな……）\x02\x03",

            "#0000Fす、すみません、\x01",
            "手が空いたら戻ってきますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x16,
        "#12P……期待はせずに待っているよ。\x02",
    )

    CloseMessageWindow()

    label("loc_A6E8")

    SetChrPos(0x0, -100000, 20, -53500, 180)
    OP_93(0x16, 0x10E, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_A22A end

    def Function_29_A718(): pass

    label("Function_29_A718")

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
        "#5P#0000Fえーっと、アントンさん。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x16,
        "#12Pあっ、君たち……\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x16,
        (
            "#12Pど、どうだった？\x01",
            "フランさんは会ってくれるって？\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x101,
        (
            "#5P#0003Fその件なんですが……\x01",
            "どうやら大丈夫そうです。\x02\x03",

            "#0000Fもう少ししたら休憩なので、\x01",
            "中央広場のレストランで\x01",
            "待ち合わせしたいそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x16,
        "#12Pお、おお……\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x16,
        (
            "#12Pあ、ありがとう。\x01",
            "何てお礼を言ったらいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x16,
        (
            "#12Pああ、僕にもこんなにいい日が\x01",
            "来るなんてっ……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        "#5P#0200F……すっかり有頂天ですね。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x102,
        "#5P#0100Fふふ、よかったですね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0586
    ChrTalk(
        0x16,
        (
            "#12Pそうだ、フランさんに\x01",
            "なにかお礼の品を見繕わないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x16,
        "#12Pまだ何も用意していないんだよ。\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x104,
        (
            "#5P#0306Fおいおい、レディとデートするのに\x01",
            "そんなんじゃ、先が思いやられるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x16,
        (
            "#12Pまさかこんなに早く\x01",
            "会えると思ってなかったからさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x16,
        "#12P……そうだ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x109, 500)

    #C0591
    ChrTalk(
        0x16,
        (
            "#12Pえ、えーっとお姉さん。\x01",
            "ちょっとデパートのほうに\x01",
            "ついてきてくれませんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x109,
        "#5P#0505Fデパート……ですか？\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x16,
        (
            "#12Pフランさんの\x01",
            "気に入りそうなプレゼントを\x01",
            "選びたいんです！\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x16,
        (
            "#12Pお姉さんに彼女の\x01",
            "好みとか趣味を教えてもらえば、\x01",
            "きっとばっちりです！\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x109,
        (
            "#5P#0508F……そ、そうですね。\x02\x03",

            "#0506Fっていうか、\x01",
            "その『お姉さん』って\x01",
            "やめません……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)

    #C0596
    ChrTalk(
        0x16,
        (
            "#12P君たちも……\x01",
            "プレゼント選び、\x01",
            "手伝ってくれるよね。\x02",
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
            "#5P#0006Fうっ……\x01",
            "（捨て犬のような目で\x01",
            "  見ないでくれ……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x103,
        (
            "#5P#0203F……なんだか面倒な事に\x01",
            "なってきましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x101,
        (
            "#5P#0006F（……はぁ、仕方ないな……\x01",
            "  こうなったら気の済むまで\x01",
            "  付き合ってみるか。）\x02\x03",

            "#0000Fそれじゃあ……\x01",
            "一旦、百貨店のほうに\x01",
            "行ってみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x16,
        (
            "#12Pうん、\x01",
            "よろしく頼むよ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5E, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_A718 end

    def Function_30_AE3B(): pass

    label("Function_30_AE3B")

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
            "うふふん♪\x01",
            "やっぱり来てくれたわね。\x02\x03",

            "ほら、座って座って。\x01",
            "お姉さんがご馳走したげるから♪\x02",
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
            "#12P#0006Fそれなんですけど……\x01",
            "食事は遠慮しておきますよ。\x02\x03",

            "#0001F代わりに話を聞かせてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x12,
        (
            "#2101F#5Pなによ～、いいじゃない。\x02\x03",

            "#2102Fそれともなに？\x01",
            "『ボクたちは警察の偉い人みたいに\x01",
            "  ワイロは受け取らないぞ！』ってこと？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0604
    ChrTalk(
        0x101,
        "#12P#0005Fなっ……\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x104,
        (
            "#0303Fうーん、俺は別に。\x02\x03",

            "#0302Fオゴってくれるなら喜んで。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x103,
        (
            "#2P#0204Fわたしも別に……\x01",
            "貸しを作るのでなければ。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x102,
        (
            "#0103Fまあ、そうね……\x02\x03",

            "#0100F常識の範囲内なら\x01",
            "問題はないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x101,
        "#12P#0011Fうっ……\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x12,
        (
            "#2102F#5Pふふん、潔癖症なのは\x01",
            "ロイド君だけみたいね～。\x02\x03",

            "#2109Fお堅いばっかりだと\x01",
            "捜査官として大成しないゾ？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#12P#0013Fっ……分かりましたよ！\x02\x03",

            "#0003Fただし酒はナシ！\x01",
            "それならご馳走になります！\x02",
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
            "#6P#0109F美味しい……\x02\x03",

            "#0102Fかなり腕の立つ\x01",
            "コックがいるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x103,
        (
            "#12P#0204Fもぐもぐ……\x01",
            "……なかなか美味です……\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x104,
        (
            "#5P#0306Fしかし、こんな美味い料理に\x01",
            "酒がないなんてありえねぇぜ。\x02",
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
            "#5P#0302Fなあロイド、せっかくの奢りだし、\x01",
            "ちょっとくらい良いだろ～？\x02",
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
            "#6P#0003F……駄目だって。\x01",
            "こっちは仕事中なんだから。\x02\x03",

            "#0001Fどこかでケジメは付けないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x104,
        (
            "#5P#0306Fはいはい、ったく、\x01",
            "ウチのリーダーは固いねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x103,
        (
            "#12P#0211Fランディさんが\x01",
            "柔らかすぎるのではないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそうね、さすがに仕事中に\x01",
            "お酒はどうかと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x12,
        "#11P#2104Fふふっ……\x02",
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
            "#11P#2109F面白いわね～、あなたたち。\x02\x03",

            "#2100Fてんでバラバラな顔触れなのに\x01",
            "どこかまとまってるっていうか……\x02\x03",

            "なかなか良いチームみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x101,
        (
            "#6P#0006F……誉めても何も出ませんよ。\x02\x03",

            "#0001Fそれより──\x01",
            "旧市街での事件に関しては\x01",
            "さっき一通り話した通りです。\x02\x03",

            "あなたが持っている\x01",
            "『欠けたパズルのピース』……\x02\x03",

            "そろそろ話してくれませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x12,
        (
            "#11P#2102Fうふふん……\x01",
            "もし、イヤだって言ったら？\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#6P#0003F……グレイスさんの事を\x01",
            "今後一切信用しないだけです。\x02\x03",

            "#0001Fお話をする機会も\x01",
            "今日で最後になるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x12,
        (
            "#11P#2105Fウソウソ、本気にしちゃやーよ。\x02\x03",

            "#2109Fでも、その毅然としたところは\x01",
            "結構いいわね～。\x02\x03",

            "#2102F優しげなマスクとのギャップが\x01",
            "なかなかそそるっていうか～。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x101,
        (
            "#6P#0004F──さて、みんな。\x01",
            "そろそろ捜査に戻ろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        "#6P#0102Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x103,
        "#12P#0204F……ご馳走さまです。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x12,
        (
            "#11P#2106Fああん、冗談だってば～。\x02\x03",

            "#2101Fパズルのピースでしょ？\x01",
            "ちゃんと話してあげるから～。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x101,
        "#6P#0006Fはあ……\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x12,
        (
            "#11P#2103F──まず前提として。\x02\x03",

            "#2100Fあなたたち、\x01",
            "『ルバーチェ』って知ってる？\x02",
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
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x102,
        "#6P#0101Fその名前は……\x02",
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
            "#5P#0305Fなんだ２人とも……\x01",
            "豆鉄砲くらったような顔をして。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x103,
        (
            "#12P#0205F『ルバーチェ商会』……\x02\x03",

            "#0203Fクロスベル市で認可された法人に\x01",
            "そんな名前があったような。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x12,
        (
            "#11P#2104Fふふ、表向きは\x01",
            "認可された法人を名乗ってるわ。\x02\x03",

            "#2101Fだけどその実態は──\x01",
            "昔からクロスベルの裏社会を\x01",
            "支配している『マフィア』よ。\x02",
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
            "#12P#0201Fマフィア……\x01",
            "犯罪組織というわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x104,
        (
            "#5P#0301Fなるほど……\x01",
            "そういうのがいるって噂は\x01",
            "聞いたことはあるが。\x02",
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
            "#5P#0301Fロイドとお嬢は\x01",
            "知ってたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0639
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……\x02\x03",

            "#0001Fクロスベルに住んでいたら\x01",
            "嫌でも耳にする名前だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x102,
        (
            "#6P#0108F色々なコネクションを\x01",
            "持っている組織みたいね……\x02\x03",

            "#0101F有力者とのつながりもあるから\x01",
            "警察も簡単に手が出せないって\x01",
            "聞いたことがあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x104,
        (
            "#5P#0303Fなるほど……\x01",
            "裏社会はどこの国も同じか。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x103,
        (
            "#12P#0200Fその『ルバーチェ』が\x01",
            "どうかしたんですか……？\x02",
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
            "#11P#2103Fうん、それなんだけどね。\x02\x03",

            "#2101F最近『ルバーチェ』の構成員が\x01",
            "妙な動きを見せてるらしいのよ。\x02\x03",

            "どこか忙しそうっていうか\x01",
            "積極的に動いているっていうか……\x02\x03",

            "それであたしも暇を見て\x01",
            "色々調べているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x101,
        (
            "#6P#0005Fマフィアが\x01",
            "忙しそうに動いている……？\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x102,
        (
            "#6P#0103F……どう考えても\x01",
            "良い予兆ではなさそうですね。\x02\x03",

            "#0101F貴女が旧市街に来ていたのも\x01",
            "もしかしてそれと関係が……？\x02",
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
        "#6P#0013Fえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x12,
        (
            "#11P#2100Fふふっ、そういうこと。\x02\x03",

            "#2103Fある筋から聞いたんだけど\x01",
            "半月ほど前、マフィアの構成員が\x01",
            "旧市街をうろついていたらしくてね。\x02\x03",

            "しかも、人目を避けるように\x01",
            "質素な格好をしていたらしいのよ。\x02\x03",

            "#2102F何かあると思わないかしら？\x02",
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
        "#5P#0301F……匂うな。\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#6P#0003Fああ、プンプンする。\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x102,
        (
            "#6P#0103F２つの不良グループが\x01",
            "同時に起こすのは難しいと\x01",
            "思われていた２件の闇討ち……\x02\x03",

            "#0101Fそこに新たな\x01",
            "第３の容疑者が現れたわけね。\x02",
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
            "#12P#0201F……でも、おかしいです。\x02\x03",

            "何故、マフィア組織が\x01",
            "不良グループのメンバーを\x01",
            "わざわざ闇討ちに……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0652
    ChrTalk(
        0x101,
        (
            "#6P#0001Fああ、問題はそこだ。\x02\x03",

            "何らかの敵対関係があるなら\x01",
            "話は単純なんだけど……\x02",
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
            "#11P#2106Fうーん、あたしの知る限り、\x01",
            "そういったイザコザは\x01",
            "今まで無かったんだけどね～。\x02\x03",

            "#2101F同じ暴力的なところはあっても\x01",
            "マフィアはプロだし、\x01",
            "不良たちは所詮アマチュア……\x02\x03",

            "利害が絡むわけでもないから\x01",
            "対立する接点がないのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x104,
        (
            "#5P#0300Fじゃあ、どちらかのグループが\x01",
            "相手を潰すためにマフィアと\x01",
            "手を組んだってのはどうだ？\x02\x03",

            "その場合、自分とこの闇討ちは\x01",
            "偽装ってことになるだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x102,
        (
            "#6P#0106Fうーん……\x01",
            "そこまでやるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        (
            "#6P#0001Fああ、少なくとも\x01",
            "あのワジとヴァルドの２人に\x01",
            "そこまでの険悪さは無かったな。\x02\x03",

            "どちらかと言うと、何となく\x01",
            "お互いを認め合ってるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x12,
        (
            "#11P#2105Fあら、鋭いじゃない。\x02\x03",

            "#2104Fあたしの知る限り、\x01",
            "あのヴァルド君とワジ君は\x01",
            "いい喧嘩相手って感じなのよね。\x02\x03",

            "#2100F元々、あの旧市街にいたのは\x01",
            "ヴァルド君の『サーベルバイパー』\x01",
            "だけだったんだけど……\x02\x03",

            "そこに２年くらい前、\x01",
            "あのワジ君がふらりと現れて\x01",
            "『テスタメンツ』を結成したのよ。\x02\x03",

            "#2106F当然、ヴァルド君たちに絡まれて\x01",
            "締め上げられそうになったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        "#6P#0005F……ひょっとして返り討ち？\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x12,
        (
            "#11P#2109Fそうそう、そうなのよ！\x02\x03",

            "#2110Fワジ君、ああ見えて\x01",
            "格闘術をやってるみたいでね。\x02\x03",

            "目にも止まらぬパンチとキックで\x01",
            "油断してたヴァルド君を\x01",
            "叩きのめしちゃったらしいの！\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x102,
        "#6P#0105Fあら……\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x103,
        "#12P#0205F……意外です。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x104,
        (
            "#5P#0305Fは～、あんな可愛い顔して\x01",
            "そんなに強かったのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#6P#0006Fうーん、あのヴァルドも\x01",
            "相当なものだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x12,
        (
            "#11P#2104Fまあ、最初は油断しただけで\x01",
            "その後は何度かやり合って\x01",
            "ほぼ互角の勝負みたいだけどね。\x02\x03",

            "#2100Fでも、そういう経緯があるから\x01",
            "お互い認め合っているみたいよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x102,
        (
            "#6P#0100Fなるほど……\x01",
            "ライバルというわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x104,
        (
            "#5P#0301Fとなると、マフィアを利用して\x01",
            "相手を潰そうって線はナシか。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#6P#0008Fそうだな……\x02\x03",

            "２人とも人望は厚そうだから\x01",
            "手下の暴走じゃなさそうだし……\x02\x03",

            "#0006Fうーん、そうなると……\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x12,
        (
            "#11P#2104Fふふっ……\x02\x03",

            "#2102F──あたしとしたことが\x01",
            "サービスしすぎちゃったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x101,
        "#6P#0005Fえっ……\x02",
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
            "#11P#2110F他の取材があるから\x01",
            "これで失礼させてもらうわ。\x02\x03",

            "まあ、せいぜい頑張って\x01",
            "良い記事を書かせてちょうだい。\x02\x03",

            "#2109Fそれじゃあ、まったね～♪\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1500, 1000, 0, 3000)
    OP_92(0x12, 0x5DC, 0x0, 0x1F4)

    def lambda_CDF6():
        OP_95(0xFE, 1500, 0, 0, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CDF6)
    Sleep(300)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetChrSubChip(0x102, 0x2)
    Sleep(300)
    SetChrSubChip(0x101, 0x2)
    Sleep(1500)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x12, 1)

    def lambda_CE30():
        OP_95(0xFE, -2000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CE30)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_CE56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_CE56)
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
        "#6P#0006Fふう……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    #C0672
    ChrTalk(
        0x102,
        (
            "#3P#0102Fふふっ……\x01",
            "我が道を行くって感じの人ね。\x02\x03",

            "#0100Fでも、彼女のおかげで\x01",
            "かなり情報が揃ってきたわ。\x02",
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
            "#6P#0000Fああ……\x01",
            "マフィアの話が聞けたのは\x01",
            "かなり大きな収穫だった。\x02\x03",

            "#0003F問題は、どうしてマフィアが\x01",
            "旧市街に介入してるのかだけど……\x02\x03",

            "#0008F……これは難しいな。\x01",
            "判断できる情報が少なすぎる。\x02",
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
            "#11P#0203F警察のデータベースでも\x01",
            "見た覚えはありません……\x02\x03",

            "#0201Fセキュリティの高い場所に\x01",
            "隠されてるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x104,
        "#5P#0306F所謂#4Rいわゆる#、機密情報ってやつか。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x102,
        (
            "#3P#0108F彼らをとりまく関係を考えると\x01",
            "その可能性は高そうね……\x02",
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
            "#0001F#12P……一度、支援課に戻って\x01",
            "セルゲイ課長の判断を仰ごう。\x02\x03",

            "何とか自力で解決したかったけど\x01",
            "そうも言ってられないみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x102,
        "#3P#0100Fそうね。\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x104,
        (
            "#1P#0300Fそんじゃ、とっとと戻って\x01",
            "オッサンを捕まえるとすっか。\x02",
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

    # Function_30_AE3B end

    def Function_31_D413(): pass

    label("Function_31_D413")

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
            "#12P困ったなぁ……\x01",
            "まさか売り切れだなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x1A, 0x0, 0x1F4)
    Sleep(500)

    #C0682
    ChrTalk(
        0x1A,
        "#12Pあっ、貴方がた……\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x1A,
        (
            "#12Pもしや今月発売された\x01",
            "《みっしぃ》のぬいぐるみを\x01",
            "お持ちじゃありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x1A,
        (
            "#12Pよろしかったら\x01",
            "譲っていただきたいんですが！\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#5P#0005Fえっと、《みっしぃ》の\x01",
            "ぬいぐるみ、ですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        (
            "#5P#0100F《みっしぃ》といえば\x01",
            "保養地《ミシュラム》の\x01",
            "マスコットキャラクターね。\x02\x03",

            "たしかティオちゃんが\x01",
            "グッズを集めてる……\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x103,
        (
            "#0200Fええ、まあ……\x01",
            "そのぬいぐるみは\x01",
            "まだ未購入ですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x2D, 0x1F4)
    Sleep(200)

    #C0688
    ChrTalk(
        0x1A,
        "#12Pおや、貴方もファンでしたか。\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x1A,
        (
            "#12Pははは、実は\x01",
            "息子も大ファンなんですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1A,
        (
            "#12Pそれでぬいぐるみを買いに\x01",
            "はるばるクロスベルを\x01",
            "訪れたのですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x0, 0x1F4)

    #C0691
    ChrTalk(
        0x1A,
        (
            "#12Pなんと、中央広場の百貨店では\x01",
            "売り切れになっていたんです……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあの百貨店で売り切れ……\x01",
            "そ、そんなに人気がある物なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x103,
        (
            "#0203Fええ、まあ。\x02\x03",

            "#0200F最近はさまざまなグッズが\x01",
            "月替わりで発売されていますから。\x01",
            "一部では大人気といっていいかと。\x02\x03",

            "#0202F……今月発売されたぬいぐるみは\x01",
            "『みっしぃぐるみ』ですね。\x01",
            "お手ごろな携帯感が魅力です。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x104,
        (
            "#0305Fはー、ティオすけの\x01",
            "データベースはさすがだなぁ……\x02\x03",

            "……………………………\x02\x03",

            "#0303Fそういや、そのぬいぐるみ……\x01",
            "カジノの景品に\x01",
            "入ってた気がするな。\x02",
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

    def lambda_D9A0():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9A0)

    def lambda_D9AD():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D9AD)

    def lambda_D9BA():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D9BA)

    def lambda_D9C7():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_D9C7)
    Sleep(600)
    OP_93(0x104, 0xE1, 0x12C)

    #C0695
    ChrTalk(
        0x104,
        (
            "#0303F俺は興味ねえし\x01",
            "完全スルーだったんだが……\x02\x03",

            "#0300F定番って感じで\x01",
            "並んでた気がするぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x1A,
        "#12P本当ですか！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x13B, 0x12C)
    Sleep(300)

    #C0697
    ChrTalk(
        0x1A,
        (
            "#12Pいや、でもカジノはちょっと……\x01",
            "私は賭け事はやらないタチでして。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DAA9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DAA9)

    def lambda_DAB6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DAB6)

    def lambda_DAC3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DAC3)

    def lambda_DAD0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_DAD0)
    OP_63(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A)
    Sleep(300)
    OP_93(0x1A, 0x0, 0x12C)

    #C0698
    ChrTalk(
        0x1A,
        (
            "#12Pあの、よろしかったら\x01",
            "皆さんで取って来て\x01",
            "いただけませんか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x1A,
        (
            "#12Pお礼はいたしますから！\x01",
            "どうか！\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x101,
        (
            "#5P#0006F（カジノか……どうしよう。\x01",
            "  微妙に警察の本分からは\x01",
            "  外れる気が……）\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x102,
        (
            "#5P#0100F（正式な要請ではないのだし、\x01",
            "  好意で持ってきてあげるくらいで\x01",
            "  いいんじゃないかしら。）\x02\x03",

            "#0106F（でないと……）\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x104,
        (
            "#5P#0309Fうっし、今から\x01",
            "カジノに直行しようぜッ！！\x02",
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

    def lambda_DCC7():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DCC7)

    def lambda_DCD4():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCD4)

    def lambda_DCE1():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DCE1)
    Sleep(300)

    #C0703
    ChrTalk(
        0x103,
        (
            "#0200F……大ハッスルですね。\x02\x03",

            "#0211Fまさかカジノで遊びたいがために\x01",
            "嘘を言ったりしてませんよね……？\x02",
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
            "クエスト【憧れのみっしぃ】\x07\x00",
            "を開始した！\x02",
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

    # Function_31_D413 end

    def Function_32_DDE3(): pass

    label("Function_32_DDE3")

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
            "#12P……おお！？\x01",
            "それは《みっしぃ》のぬいぐるみ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x1A,
        (
            "#12P１つでいいのです。\x01",
            "ぜひ私たちに\x01",
            "譲ってはくれませんか！？\x02",
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
            "【譲る】\x01",          # 0
            "【譲らない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DF39"),
        (1, "loc_DF3D"),
        (SWITCH_DEFAULT, "loc_DFCE"),
    )


    label("loc_DF39")

    Call(0, 33)
    Return()

    label("loc_DF3D")


    #C0707
    ChrTalk(
        0x1A,
        "#12Pそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x1A,
        (
            "#12Pまた気が向いたら\x01",
            "声を掛けていだらけませんか。\x01",
            "どうも諦めきれないもので……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -50510, 30, -53790, 180)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    EventEnd(0x5)
    Jump("loc_DFCE")

    label("loc_DFCE")

    Return()

    # Function_32_DDE3 end

    def Function_33_DFCF(): pass

    label("Function_33_DFCF")

    ClearChrFlags(0x1B, 0x4)

    #C0709
    ChrTalk(
        0x101,
        (
            "#5P#0000Fええ、どうぞ。\x01",
            "大した物でもありませんし……\x02",
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
            "ラルスに『みっしぃぐるみ』を渡した。\x02",
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
        "#12Pこれがみっしぃの……\x02",
    )

    CloseMessageWindow()
    OP_68(-53210, 1400, -55140, 2000)

    def lambda_E091():

        label("loc_E091")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_E091")

    QueueWorkItem2(0x0, 1, lambda_E091)

    def lambda_E0A3():

        label("loc_E0A3")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_E0A3")

    QueueWorkItem2(0x1, 1, lambda_E0A3)

    def lambda_E0B5():

        label("loc_E0B5")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_E0B5")

    QueueWorkItem2(0x2, 1, lambda_E0B5)

    def lambda_E0C7():

        label("loc_E0C7")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_E0C7")

    QueueWorkItem2(0x3, 1, lambda_E0C7)
    OP_95(0x1A, -52950, 0, -54800, 4000, 0x0)
    OP_93(0x1A, 0xE1, 0x1F4)
    OP_6F(0x1)

    #C0712
    ChrTalk(
        0x1A,
        (
            "#11Pほらクルト、\x01",
            "ついに手に入れたぞ！\x02",
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
        "#6Pあっ、みっしぃだっ……！\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x1B,
        "#6Pわーい、ほんもの～！\x02",
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
            "#12Pああ、皆さん\x01",
            "ありがとうございました。\x01",
            "なんと礼を言えばよいのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1A,
        (
            "#12Pそうだ、少ないですが\x01",
            "これを受け取ってください。\x02",
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
            "１２０ミラ\x07\x00",
            "を受け取った。\x02",
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
            "#5P#0000Fハハ、どうも……\x01",
            "本当に大した事じゃないんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x104,
        (
            "#5P#0304Fおう、あの程度の稼ぎなら\x01",
            "ちょちょいのちょいだぜ。\x02\x03",

            "もう少し時間があれば\x01",
            "ギャラリーができるほど\x01",
            "稼いでやるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x102,
        (
            "#5P#0103Fコホン、そろそろ\x01",
            "仕事に戻りましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x103,
        (
            "#0200Fそうですね。\x01",
            "ランディさんには次の機会に\x01",
            "頑張ってもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x104,
        "#5P#0306Fとほほ……そうすっか。\x02",
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
            "クエスト【憧れのみっしぃ】\x07\x00",
            "を達成した！\x02",
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

    # Function_33_DFCF end

    def Function_34_E504(): pass

    label("Function_34_E504")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_E908")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E677")

    #C0724
    ChrTalk(
        0xFE,
        (
            "皆さんありがとうございました。\x01",
            "息子も喜んでいるようで……\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0xFE,
        (
            "クロスベルに来てよかった……\x01",
            "息子に笑顔をありがとう、《みっしぃ》！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E66F")

    #C0726
    ChrTalk(
        0x104,
        (
            "#0300F（いろんな観光客が\x01",
            "  いるもんだなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x103,
        (
            "#0200F（《みっしぃ》のためなら、\x01",
            "  分からなくもないです。）\x02",
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

    label("loc_E66F")

    SetScenarioFlags(0x2, 1)
    Jump("loc_E903")

    label("loc_E677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x5D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6A9")
    Call(0, 32)
    Jump("loc_E844")

    label("loc_E6A9")


    #C0728
    ChrTalk(
        0x1A,
        (
            "《みっしぃ》のぬいぐるみ……\x01",
            "ぜひ私たちに\x01",
            "譲ってはくれませんか！？\x02",
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
            "【譲る】\x01",          # 0
            "【譲らない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E739"),
        (1, "loc_E7D7"),
        (SWITCH_DEFAULT, "loc_E844"),
    )


    label("loc_E739")

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

    label("loc_E7D7")


    #C0729
    ChrTalk(
        0x1A,
        "そ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x1A,
        (
            "また気が向いたら\x01",
            "声を掛けていだらけませんか。\x01",
            "どうも諦めきれないもので……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E844")

    label("loc_E844")

    Jump("loc_E903")

    label("loc_E849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_E900")

    #C0731
    ChrTalk(
        0xFE,
        (
            "まさかカジノの\x01",
            "景品にあったとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xFE,
        (
            "いや、ですが私は\x01",
            "賭け事はやらないタチでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xFE,
        (
            "できれば皆さんに\x01",
            "取って来て頂きたんですが……\x01",
            "虫のいい話でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E903")

    label("loc_E900")

    Call(0, 31)

    label("loc_E903")

    Jump("loc_EA44")

    label("loc_E908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_E9B8")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)

    #C0734
    ChrTalk(
        0x1A,
        "よし、腹ごしらえもしたし。\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x1A,
        (
            "父さんと例の物を\x01",
            "買いに行こうか！\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x1B,
        "わーい、やったぁ！\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x1A,
        (
            "あはは、お前は本当に\x01",
            "《みっしぃ》好きだなぁ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Jump("loc_EA44")

    label("loc_E9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_EA44")

    #C0738
    ChrTalk(
        0xFE,
        (
            "今日は息子のために\x01",
            "はるばるクロスベルまで来たんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xFE,
        (
            "はっはっは、\x01",
            "息子のためならなんのその。\x01",
            "仕事の残業など怖くないさ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA44")

    TalkEnd(0xFE)
    Return()

    # Function_34_E504 end

    def Function_35_EA48(): pass

    label("Function_35_EA48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_EB5F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EABD")

    #C0740
    ChrTalk(
        0xFE,
        (
            "わーい、みっしぃだー！\x01",
            "すっごくかわいいっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xFE,
        (
            "お兄ちゃんたち、\x01",
            "ありがとねー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB5A")

    label("loc_EABD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_EB23")

    #C0742
    ChrTalk(
        0xFE,
        (
            "お兄ちゃんたちが\x01",
            "《みっしぃ》をもってきてくれるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xFE,
        "わーい、まってるねー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB5A")

    label("loc_EB23")


    #C0744
    ChrTalk(
        0xFE,
        (
            "しくしく……《みっしぃ》に\x01",
            "会えると思ったのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB5A")

    Jump("loc_EC02")

    label("loc_EB5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_EB70")
    Call(0, 34)
    Jump("loc_EC02")

    label("loc_EB70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_EC02")

    #C0745
    ChrTalk(
        0xFE,
        (
            "わーい、ベッドも\x01",
            "ふかふかだぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0xFE,
        (
            "それにね、パパが\x01",
            "僕の好きなもの、１つだけ\x01",
            "買ってくれる約束なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0xFE,
        "わーい、楽しみだなっ！\x02",
    )

    CloseMessageWindow()

    label("loc_EC02")

    TalkEnd(0xFE)
    Return()

    # Function_35_EA48 end

    def Function_36_EC06(): pass

    label("Function_36_EC06")

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
        "#11Pはい～、いらっしゃい～。\x02",
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#5P#0000F君がサンサンさんかな。\x01",
            "支援要請を見て来たんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0750
    ChrTalk(
        0xA,
        "#11Pわ、もう来てくれたの！？\x02",
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xA,
        "#11Pわーい、よかったよ～！\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0752
    ChrTalk(
        0x104,
        (
            "#6P#0309F（ハハ、随分と可愛いコだな。）\x02\x03",

            "#0300F確か用件は『魚料理の食材求む』\x01",
            "……だったか。\x02\x03",

            "#0306Fなんつーか支援課としちゃあ\x01",
            "随分とアレな依頼なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x102,
        (
            "#6P#0106Fそうねえ、事情にも\x01",
            "よるとは思うけれど……\x02",
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
            "#11Pよく分からないけど……\x01",
            "お急ぎで頼みたいのは本当よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0xA,
        (
            "#11P実は今朝、急な予約客が入ってね。\x01",
            "それでお魚料理の材料が足りないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xA,
        (
            "#11P市場のお魚屋さんに行っても\x01",
            "いいお魚がフソク中らしくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xA,
        (
            "#11Pお願いよ、便利屋のヒトたちで\x01",
            "何とかとってきて欲しいよ～！\x02",
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
            "#5P#0003Fあの、ゴメン。\x01",
            "今なんと？\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x103,
        (
            "#5P#0200Fわたしたちは便利屋では\x01",
            "ないのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0xA,
        "#11Pほえ？\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0xA,
        (
            "#11Pギルドの受付さんに相談したら、\x01",
            "手を回しておくから\x01",
            "大丈夫って言ってたよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0xA,
        (
            "#11P手の空いてる遊撃士さんはいないけど\x01",
            "シリアイに便利屋がいるって……\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0xA,
        "#11Pみんながそのヒトたちじゃないの？\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x104,
        "#6P#0306F（……あの受付の仕業か。）\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x101,
        (
            "#5P#0003F（微妙に間違ってない所が\x01",
            "  否定しづらい……）\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x102,
        "#6P#0106F（悲しいわね……）\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x103,
        (
            "#5P#0200Fまあロイドさんは\x01",
            "釣りが出来るわけですし、\x01",
            "協力してあげていいのでは？\x02\x03",

            "一応お困りのようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそうだな……\x01",
            "引き受けてみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0xA,
        "#11Pほんと？　よかったよ～！\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0xA,
        (
            "#11Pお料理に使うのは\x01",
            "『とっても細長い魚』なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0xA,
        (
            "#11P予約のお客さまは５名だから、\x01",
            "同じ種類の魚を５匹でお願いね？\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0xA,
        (
            "#11Pん～……もし釣れなかったら\x01",
            "他のお魚でもいいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0xA,
        (
            "#11Pとにかく同じ魚を５匹ね。\x01",
            "それだけは絶対よ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x101,
        (
            "#5P#0003F『とっても細長い魚』を５匹……\x01",
            "無理だった場合でも\x01",
            "同じ種類の魚を５匹だね。\x02\x03",

            "#0000F分かった、\x01",
            "釣れたら持ってくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xA,
        (
            "#11Pうん、多謝多謝。\x01",
            "よろしくお願いね～！\x02",
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
            "クエスト【魚料理の食材求む！】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 9670, 30, -2060, 90)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_F4A1")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)

    label("loc_F4A1")

    OP_29(0x11, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_EC06 end

    def Function_37_F4AA(): pass

    label("Function_37_F4AA")

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
            "#11Pありがと、これで\x01",
            "何とか乗り切れそうよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5CF")
    OP_2C(0x11, 0x5)
    OP_29(0x11, 0x1, 0x2)

    #C0778
    ChrTalk(
        0xA,
        (
            "#11Pいつもの魚が手に入ったし、\x01",
            "これでお客さんも大満足よ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6D8")

    label("loc_F5CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F67A")
    OP_2C(0x11, 0x5)
    OP_29(0x11, 0x1, 0x3)

    #C0779
    ChrTalk(
        0xA,
        (
            "#11Pいつもの魚じゃなかったけど……\x01",
            "チョット珍しい種類だし、\x01",
            "きっとパパなら上手にお料理するね。\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0xA,
        "#11Pこれでお客さんも大大満足よ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_F6D8")

    label("loc_F67A")

    OP_2C(0x11, 0x2)
    OP_29(0x11, 0x1, 0x4)

    #C0781
    ChrTalk(
        0xA,
        (
            "#11P『とっても細長い魚』じゃなかったけど、\x01",
            "パパに頼んでお造りにしてもらうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6D8")


    #C0782
    ChrTalk(
        0xA,
        (
            "#11Pそうだ、みんなには\x01",
            "お礼にこれをあげちゃうね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F775")
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
            "×２を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 2)
    Jump("loc_F82D")

    label("loc_F775")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7DB")
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
            "×３を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 3)
    Jump("loc_F82D")

    label("loc_F7DB")

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
            "×２を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F4, 2)

    label("loc_F82D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9AB")

    #C0786
    ChrTalk(
        0xA,
        (
            "#11Pあと……そうだ。\x01",
            "みんなはこんなの、興味ある？\x02",
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
            "のレシピを受け取った。\x02",
        )
    )

    CloseMessageWindow()

    #A0788
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x197),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
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
            "#11Pうちの秘伝の炒飯レシピよ。\x01",
            "お魚と合わせて今晩のお客さんにも\x01",
            "振舞うつもりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0xA,
        "#11Pよかったら使ってよ～。\x02",
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそうか、ありがたく\x01",
            "受け取っておくよ。\x02\x03",

            "君も仕事、がんばってな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAE0")

    label("loc_F9AB")


    #C0792
    ChrTalk(
        0xA,
        (
            "#11Pあと……そうだ。\x01",
            "これもあげちゃうよ～。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x197, 1)

    #C0794
    ChrTalk(
        0xA,
        (
            "#11Pさっき間違えて\x01",
            "オーダーを取ってしまったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0xA,
        (
            "#11P作りたてだから、\x01",
            "よかったら食べてよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        (
            "#5P#0000Fはは……ありがとう。\x01",
            "受け取っておくよ。\x02\x03",

            "君も仕事、がんばってな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAE0")


    #C0797
    ChrTalk(
        0xA,
        (
            "#11Pうん、ホントにありがとね。\x01",
            "便利屋のヒト～。\x02",
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
        "#5P#0012Fは、ははは……\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x102,
        (
            "#6P#0106F（最後まで誤解は\x01",
            "  解けなかったわね……）\x02",
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
            "クエスト【魚料理の食材求む！】\x07\x00",
            "を達成した！\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_FC7D")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)

    label("loc_FC7D")

    OP_29(0x11, 0x4, 0x10)
    SetScenarioFlags(0x2, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_37_F4AA end

    def Function_38_FC8B(): pass

    label("Function_38_FC8B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCB6")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x175), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FCB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCD7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x174), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FCD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCF8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x173), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FCF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD19")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FD19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD3A")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x171), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FD3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD5B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FD5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD7C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FD7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD9D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FD9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FDBE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FDBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FDDF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FDDF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE00")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FE00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE21")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FE21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE42")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FE42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE63")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FE63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE84")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FE84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEA5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x166), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FEA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEC6")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FEC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEE7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FEE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF08")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x163), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FF08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF29")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FF29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF4A")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FF4A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF6B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FF6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF8C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FF8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FFA8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_FFA8")

    Return()

    # Function_38_FC8B end

    def Function_39_FFA9(): pass

    label("Function_39_FFA9")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10015")
    MenuCmd(1, 1, "スノーシュラブ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1000B")
    Call(0, 40)

    label("loc_1000B")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10015")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10074")
    MenuCmd(1, 1, "アルモリカブナ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1006A")
    Call(0, 40)

    label("loc_1006A")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10074")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100CD")
    MenuCmd(1, 1, "オロショ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100C3")
    Call(0, 40)

    label("loc_100C3")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_100CD")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10124")
    MenuCmd(1, 1, "ロック")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1011A")
    Call(0, 40)

    label("loc_1011A")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10124")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1017B")
    MenuCmd(1, 1, "カルプ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10171")
    Call(0, 40)

    label("loc_10171")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1017B")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_101D4")
    MenuCmd(1, 1, "レイニー")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_101CA")
    Call(0, 40)

    label("loc_101CA")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_101D4")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1022D")
    MenuCmd(1, 1, "エーゼル")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10223")
    Call(0, 40)

    label("loc_10223")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1022D")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10286")
    MenuCmd(1, 1, "カサギン")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1027C")
    Call(0, 40)

    label("loc_1027C")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10286")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_102E1")
    MenuCmd(1, 1, "レインボウ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_102D7")
    Call(0, 40)

    label("loc_102D7")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_102E1")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1033A")
    MenuCmd(1, 1, "トラード")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10330")
    Call(0, 40)

    label("loc_10330")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1033A")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10393")
    MenuCmd(1, 1, "サモーナ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10389")
    Call(0, 40)

    label("loc_10389")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10393")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_103EA")
    MenuCmd(1, 1, "イール")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_103E0")
    Call(0, 40)

    label("loc_103E0")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_103EA")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10447")
    MenuCmd(1, 1, "パールグラス")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1043D")
    Call(0, 40)

    label("loc_1043D")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10447")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_104A4")
    MenuCmd(1, 1, "グラトンバス")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1049A")
    Call(0, 40)

    label("loc_1049A")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_104A4")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10503")
    MenuCmd(1, 1, "バイパーヘッド")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_104F9")
    Call(0, 40)

    label("loc_104F9")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10503")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10562")
    MenuCmd(1, 1, "パイソンヘッド")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10558")
    Call(0, 40)

    label("loc_10558")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10562")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_105BB")
    MenuCmd(1, 1, "タイタン")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_105B1")
    Call(0, 40)

    label("loc_105B1")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_105BB")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10618")
    MenuCmd(1, 1, "クインシザー")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1060E")
    Call(0, 40)

    label("loc_1060E")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10618")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10675")
    MenuCmd(1, 1, "エレキイール")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1066B")
    Call(0, 40)

    label("loc_1066B")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10675")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106D4")
    MenuCmd(1, 1, "デモンタイタン")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_106CA")
    Call(0, 40)

    label("loc_106CA")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_106D4")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10733")
    MenuCmd(1, 1, "アークシュラブ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10729")
    Call(0, 40)

    label("loc_10729")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10733")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10792")
    MenuCmd(1, 1, "ゴルドサモーナ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10788")
    Call(0, 40)

    label("loc_10788")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10792")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_107F1")
    MenuCmd(1, 1, "ノーブルカルプ")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_107E7")
    Call(0, 40)

    label("loc_107E7")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_107F1")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10852")
    MenuCmd(1, 1, "サーペントヘッド")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10848")
    Call(0, 40)

    label("loc_10848")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10852")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x1)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1089E")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1089E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_108E6")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_108E6")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1092E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1092E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10976")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10976")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109BE")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_109BE")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A06")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A06")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A4E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A4E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A96")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A96")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10ADE")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10ADE")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B26")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B26")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B6E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B6E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BB6")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10BB6")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BFE")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C46")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10C46")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C8E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10C8E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10CD6")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D1E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D66")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10D66")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DAE")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10DAE")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DF6")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10DF6")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E3E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E86")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E86")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10ECE")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10ECE")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F16")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10F16")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F5E")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10F5E")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_FFA9 end

    def Function_40_10F6E(): pass

    label("Function_40_10F6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F86")
    MenuCmd(3, 1, 0x0)
    Jump("loc_111A9")

    label("loc_10F86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F9E")
    MenuCmd(3, 1, 0x1)
    Jump("loc_111A9")

    label("loc_10F9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FB6")
    MenuCmd(3, 1, 0x2)
    Jump("loc_111A9")

    label("loc_10FB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FCE")
    MenuCmd(3, 1, 0x3)
    Jump("loc_111A9")

    label("loc_10FCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FE6")
    MenuCmd(3, 1, 0x4)
    Jump("loc_111A9")

    label("loc_10FE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FFE")
    MenuCmd(3, 1, 0x5)
    Jump("loc_111A9")

    label("loc_10FFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11016")
    MenuCmd(3, 1, 0x6)
    Jump("loc_111A9")

    label("loc_11016")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102E")
    MenuCmd(3, 1, 0x7)
    Jump("loc_111A9")

    label("loc_1102E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11046")
    MenuCmd(3, 1, 0x8)
    Jump("loc_111A9")

    label("loc_11046")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1105E")
    MenuCmd(3, 1, 0x9)
    Jump("loc_111A9")

    label("loc_1105E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11076")
    MenuCmd(3, 1, 0xA)
    Jump("loc_111A9")

    label("loc_11076")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1108E")
    MenuCmd(3, 1, 0xB)
    Jump("loc_111A9")

    label("loc_1108E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110A6")
    MenuCmd(3, 1, 0xC)
    Jump("loc_111A9")

    label("loc_110A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110BE")
    MenuCmd(3, 1, 0xD)
    Jump("loc_111A9")

    label("loc_110BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110D6")
    MenuCmd(3, 1, 0xE)
    Jump("loc_111A9")

    label("loc_110D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110EE")
    MenuCmd(3, 1, 0xF)
    Jump("loc_111A9")

    label("loc_110EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11106")
    MenuCmd(3, 1, 0x10)
    Jump("loc_111A9")

    label("loc_11106")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1111E")
    MenuCmd(3, 1, 0x11)
    Jump("loc_111A9")

    label("loc_1111E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11136")
    MenuCmd(3, 1, 0x12)
    Jump("loc_111A9")

    label("loc_11136")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1114E")
    MenuCmd(3, 1, 0x13)
    Jump("loc_111A9")

    label("loc_1114E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11166")
    MenuCmd(3, 1, 0x14)
    Jump("loc_111A9")

    label("loc_11166")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1117E")
    MenuCmd(3, 1, 0x15)
    Jump("loc_111A9")

    label("loc_1117E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11196")
    MenuCmd(3, 1, 0x16)
    Jump("loc_111A9")

    label("loc_11196")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111A9")
    MenuCmd(3, 1, 0x17)

    label("loc_111A9")

    Return()

    # Function_40_10F6E end

    def Function_41_111AA(): pass

    label("Function_41_111AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x175), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C3")
    SubItemNumber(0x175, 5)
    Jump("loc_113FD")

    label("loc_111C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x174), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111DC")
    SubItemNumber(0x174, 5)
    Jump("loc_113FD")

    label("loc_111DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x173), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111F5")
    SubItemNumber(0x173, 5)
    Jump("loc_113FD")

    label("loc_111F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120E")
    SubItemNumber(0x172, 5)
    Jump("loc_113FD")

    label("loc_1120E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x171), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11227")
    SubItemNumber(0x171, 5)
    Jump("loc_113FD")

    label("loc_11227")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11240")
    SubItemNumber(0x170, 5)
    Jump("loc_113FD")

    label("loc_11240")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11259")
    SubItemNumber(0x16F, 5)
    Jump("loc_113FD")

    label("loc_11259")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11272")
    SubItemNumber(0x16E, 5)
    Jump("loc_113FD")

    label("loc_11272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1128B")
    SubItemNumber(0x16D, 5)
    Jump("loc_113FD")

    label("loc_1128B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112A4")
    SubItemNumber(0x16C, 5)
    Jump("loc_113FD")

    label("loc_112A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112BD")
    SubItemNumber(0x16B, 5)
    Jump("loc_113FD")

    label("loc_112BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112D6")
    SubItemNumber(0x16A, 5)
    Jump("loc_113FD")

    label("loc_112D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112EF")
    SubItemNumber(0x169, 5)
    Jump("loc_113FD")

    label("loc_112EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11308")
    SubItemNumber(0x168, 5)
    Jump("loc_113FD")

    label("loc_11308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11321")
    SubItemNumber(0x167, 5)
    Jump("loc_113FD")

    label("loc_11321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x166), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1133A")
    SubItemNumber(0x166, 5)
    Jump("loc_113FD")

    label("loc_1133A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11353")
    SubItemNumber(0x165, 5)
    Jump("loc_113FD")

    label("loc_11353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1136C")
    SubItemNumber(0x164, 5)
    Jump("loc_113FD")

    label("loc_1136C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x163), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11385")
    SubItemNumber(0x163, 5)
    Jump("loc_113FD")

    label("loc_11385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1139E")
    SubItemNumber(0x162, 5)
    Jump("loc_113FD")

    label("loc_1139E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113B7")
    SubItemNumber(0x161, 5)
    Jump("loc_113FD")

    label("loc_113B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113D0")
    SubItemNumber(0x160, 5)
    Jump("loc_113FD")

    label("loc_113D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113E9")
    SubItemNumber(0x15F, 5)
    Jump("loc_113FD")

    label("loc_113E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113FD")
    SubItemNumber(0x15E, 5)

    label("loc_113FD")

    Return()

    # Function_41_111AA end

    def Function_42_113FE(): pass

    label("Function_42_113FE")

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

    # Function_42_113FE end

    def Function_43_11449(): pass

    label("Function_43_11449")

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

    # Function_43_11449 end

    SaveToFile()

Try(main)
