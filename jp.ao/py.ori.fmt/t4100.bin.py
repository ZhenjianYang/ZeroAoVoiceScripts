from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4100.bin",                # FileName
        "t4100",                    # MapName
        "t4100",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4100",                  # 0
        "ミュシャ夫人",           # 1
        "クイント老人",           # 2
        "シスター・リース",       # 3
        "親衛隊隊士",             # 4
        "親衛隊隊士",             # 5
        "クラリス",               # 6
        "ニールセン",             # 7
        "アリオス",               # 8
        "ガイ墓前の花",           # 9
        "アリオス家墓前の花",     # 10
        "クローディア姫",         # 11
        "ユリア准佐",             # 12
    ))

    AddCharChip((
        "chr/ch20100.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "chr/ch14000.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "chr/ch41600.itc",                   # 04
        "apl/ch50423.itc",                   # 05
        "chr/ch02400.itc",                   # 06
        "chr/ch11000.itc",                   # 07
        "chr/ch11200.itc",                   # 08
        "chr/ch45100.itc",                   # 09
        "chr/ch11500.itc",                   # 0A
    ))

    DeclNpc(8579,    2000,    25379,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-8869,   0,       11800,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-1690,   0,       10510,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1720,    0,       10880,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-7599,   2000,    25329,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6469,   0,       12180,   135,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(20829,   0,       32299,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-23000,  0,       25500,   0,    502,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20600,   0,       34000,   0,    502,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(349,     4000,    42569,   0,    449,  0x0, 0,   7,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2230,    4000,    42750,   180,  449,  0x0, 0,   8,   0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0000, 0, 22,  -1.0,                  24.0,                  0.0,                   1764.0,                [0.0357142873108387,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.0357142873108387,    -8.0,                  -0.0,                  1.0])

    DeclActor(190,     4200,    45040,   1200,    190,     5700,    45040,   0x007C, 0,  13, 0x0000)
    DeclActor(-23050,  0,       25770,   1200,    -22620,  1500,    25860,   0x007C, 0,  15, 0x0000)
    DeclActor(20570,   0,       34830,   1500,    20570,   1500,    34830,   0x007C, 0,  18, 0x0000)
    DeclActor(12080,   4000,    37650,   1500,    12080,   5500,    37650,   0x007C, 0,  20, 0x0000)
    DeclActor(-8020,   2000,    26550,   1500,    -8020,   3500,    26550,   0x007C, 0,  14, 0x0000)

    ChipFrameInfo(924, 0)                                        # 0

    ScpFunction((
        "Function_0_39C",          # 00, 0
        "Function_1_44C",          # 01, 1
        "Function_2_8A9",          # 02, 2
        "Function_3_B2E",          # 03, 3
        "Function_4_CA7",          # 04, 4
        "Function_5_1B8C",         # 05, 5
        "Function_6_1F20",         # 06, 6
        "Function_7_2E69",         # 07, 7
        "Function_8_38BE",         # 08, 8
        "Function_9_3E6E",         # 09, 9
        "Function_10_3FA2",        # 0A, 10
        "Function_11_407F",        # 0B, 11
        "Function_12_4565",        # 0C, 12
        "Function_13_45C7",        # 0D, 13
        "Function_14_469C",        # 0E, 14
        "Function_15_490D",        # 0F, 15
        "Function_16_5057",        # 10, 16
        "Function_17_5504",        # 11, 17
        "Function_18_5C6C",        # 12, 18
        "Function_19_5DA3",        # 13, 19
        "Function_20_60E1",        # 14, 20
        "Function_21_640A",        # 15, 21
        "Function_22_6B0C",        # 16, 22
        "Function_23_7E84",        # 17, 23
        "Function_24_7EAD",        # 18, 24
        "Function_25_7EB1",        # 19, 25
        "Function_26_8A8D",        # 1A, 26
        "Function_27_8E86",        # 1B, 27
        "Function_28_93A2",        # 1C, 28
        "Function_29_960D",        # 1D, 29
    ))


    def Function_0_39C(): pass

    label("Function_0_39C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3D4"),
        (1, "loc_3E0"),
        (2, "loc_3EC"),
        (3, "loc_3F8"),
        (4, "loc_404"),
        (5, "loc_410"),
        (6, "loc_41C"),
        (SWITCH_DEFAULT, "loc_434"),
    )


    label("loc_3D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_3E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_3EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_3F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_404")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_410")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_434")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_44B")

    Return()

    # Function_0_39C end

    def Function_1_44C(): pass

    label("Function_1_44C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A8")
    OP_95(0xFE, -8870, 0, 11800, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -16950, 0, 11340, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -19140, 0, 11340, 2000, 0x0)
    OP_95(0xFE, -19140, 0, 16070, 2000, 0x0)
    OP_95(0xFE, -21040, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -16960, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 0, 16090, 2000, 0x0)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -10990, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -4930, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -1200, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -8460, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -50, 4200, 43970, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 12000, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 4970, 4000, 36140, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 1310, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 1310, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 15920, 0, 8039, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 22720, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 22720, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 20500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 11500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 9240, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 16390, 2000, 0x0)
    OP_95(0xFE, 15980, 0, 19640, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 21270, 0, 25620, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 20470, 0, 33170, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x6A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 6410, 2000, 0x0)
    OP_95(0xFE, 30, 0, 6690, 2000, 0x0)
    Jump("Function_1_44C")

    label("loc_8A8")

    Return()

    # Function_1_44C end

    def Function_2_8A9(): pass

    label("Function_2_8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DC")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -22960, 0, 24620, 0)

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8F5")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_8F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_924")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 12160, 4000, 36150, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_B2D")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95E")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -22960, 0, 24620, 0)

    label("loc_95E")

    Jump("loc_B2D")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_980")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_985")

    label("loc_980")

    ClearChrFlags(0x11, 0x80)

    label("loc_985")

    ClearChrFlags(0x10, 0x80)
    SetScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_99B")
    SetChrFlags(0x8, 0x10)

    label("loc_99B")

    Jump("loc_B2D")

    label("loc_9A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9C4")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    Jump("loc_B2D")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9D7")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B2D")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A00")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_B2D")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A24")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    Jump("loc_B2D")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_A32")
    Jump("loc_B2D")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_A4B")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A64")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8B")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_A8B")

    Jump("loc_B2D")

    label("loc_A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AA3")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_B2D")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ABC")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_ACF")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B2D")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_AFB")
    SetChrChipByIndex(0xA, 0xA)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    Jump("loc_B2D")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_B14")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B2D")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrFlags(0x8, 0x10)

    label("loc_B2D")

    Return()

    # Function_2_8A9 end

    def Function_3_B2E(): pass

    label("Function_3_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BB2")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0x168, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_BC9")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_BC9")

    label("loc_BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF5")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x14, 0x190, 0x0)
    Jump("loc_C1C")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C1C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x14, 0x190, 0x0)

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2E")
    OP_65(0x4, 0x1)

    label("loc_C2E")

    SoundDistance(0x84, 0xFFFFD878, 0xFA0, 0xDEA8, 0x2710, 0x186A0, 0x64, 0x0)
    OP_E3(0x6C2, 0xFA0, 0xDEA8)
    OP_E3(0x4F60, 0xFA0, 0xDEA8)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C81")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C81")

    OP_66(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA6")
    OP_65(0x1, 0x1)

    label("loc_CA6")

    Return()

    # Function_3_B2E end

    def Function_4_CA7(): pass

    label("Function_4_CA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")

    #C0001
    ChrTalk(
        0xFE,
        "先ほど、警察の者が事情聴取に来てな。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "まさか、イアン殿がこんな大それた事を……\x01",
            "とてもじゃないが信じられんわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00001F……ええ、俺たちも同じ気持ちです。\x02\x03",

            "#00003F（……だけど、事実には違いない。\x01",
            "  真意は先生自身に問い詰めて\x01",
            "  みるしかないだろうな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E4D")

    label("loc_DD0")


    #C0004
    ChrTalk(
        0xFE,
        (
            "イアン殿がよもや、\x01",
            "こんな大それた事を……\x01",
            "とてもじゃないが信じられん。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "一体、何が彼を\x01",
            "そうさせたというのじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4D")

    Jump("loc_1B88")

    label("loc_E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1423")

    #C0006
    ChrTalk(
        0xFE,
        (
            "あの障壁が消えたと思うたら、\x01",
            "とんでもない事が\x01",
            "起こってしもうたのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "あの独立宣言以来、\x01",
            "墓参りに来る者も減ってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "こんな状況ではわしに出来るのは、\x01",
            "墓の掃除をしてやることくらいじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141E")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0009
    ChrTalk(
        0x101,
        (
            "#00003F……あの。\x02\x03",

            "#00008Fこちらの墓は一体、\x01",
            "どなたのものなんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0010
    ChrTalk(
        0xFE,
        "なんじゃ、知らなかったのか？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "……ふむ、まあおぬしらなら\x01",
            "特に問題もあるまい。\x01",
            "“彼”とも親しいようだしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#00105Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        "#00305F俺たちの知り合いなのかよ？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "……うむ。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "ここに眠っている者たちの姓は\x01",
            "『グリムウッド』……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "つまり、イアン・グリムウッド殿の\x01",
            "ご家族なのだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x103,
        "#00205Fイアン先生の……！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#00108Fそ、そうなんですか……！？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "……まごうことなき事実じゃ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "１５年ほど前に、ある不幸な事故で\x01",
            "奥さんとお子さん２人の命が\x01",
            "失われてしまってな……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "いつも週末のたびに墓参りに来ては\x01",
            "ご家族のことを偲んでおったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "墓石は風雨で痛んでしまったが……\x01",
            "何やら願掛けをしておるらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "それが成るまではあえて修繕せずに\x01",
            "手入れするよう頼まれておるのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00106Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        "#00308Fあの先生も色々あるらしいな……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "あの独立宣言以来、彼も忙しいのか\x01",
            "なかなか訪れていないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "よかったら、これからは\x01",
            "お前さんたちも参ってやるといい。\x01",
            "……彼女たちも寂しかろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00003F………………………………\x02\x03",

            "#00000F……はい、わかりました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 4)

    label("loc_141E")

    Jump("loc_1494")

    label("loc_1423")


    #C0029
    ChrTalk(
        0xFE,
        (
            "こんな状況ではわしに出来るのは、\x01",
            "墓の掃除をしてやることくらいじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "……おぬしらも気をつけるんじゃぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_1494")

    Jump("loc_1B88")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_14A7")
    Jump("loc_1B88")

    label("loc_14A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DC")

    #C0031
    ChrTalk(
        0xFE,
        "先ほど、イアン殿が教会に来ていてな。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ガイやアリオスの妻の墓を\x01",
            "お参りしていったようじゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0033
    ChrTalk(
        0x101,
        "#00005Fえっと……どうしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "……いや、なに。\x01",
            "大したことじゃないわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "最近忙しくしておるようだし、\x01",
            "いい気分転換になったならよいがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_166F")

    label("loc_15DC")


    #C0036
    ChrTalk(
        0xFE,
        (
            "先ほど、イアン殿が\x01",
            "ガイやアリオスの妻の墓を\x01",
            "お参りしていったようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "最近忙しくしておるようだし、\x01",
            "いい気分転換になったならよいがのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166F")

    Jump("loc_1B88")

    label("loc_1674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1753")

    #C0038
    ChrTalk(
        0xFE,
        (
            "市長の言うとおり、\x01",
            "クロスベルには国家独立が\x01",
            "必要なのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "当然、帝国と共和国は\x01",
            "圧力をかけてくるだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "これからの若い世代のためにも、\x01",
            "なんとしても成してほしいものじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17CD")

    label("loc_1753")


    #C0041
    ChrTalk(
        0xFE,
        (
            "クロスベルには国家独立が\x01",
            "必要なのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "これからの若い世代のためにも、\x01",
            "なんとしても成してほしいものじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CD")

    Jump("loc_1B88")

    label("loc_17D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17E0")
    Jump("loc_1B88")

    label("loc_17E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17EE")
    Jump("loc_1B88")

    label("loc_17EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D5")

    #C0043
    ChrTalk(
        0xFE,
        (
            "いつも墓参りに来ている\x01",
            "あのご夫人は、紛争で旦那を\x01",
            "亡くしてしまったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "……時代はもう少し前だが、\x01",
            "わしもまた紛争で家族を失っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "似た境遇だからか、\x01",
            "どうも気にかけてしまうのじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_195E")

    label("loc_18D5")


    #C0046
    ChrTalk(
        0xFE,
        (
            "あのご夫人は、紛争で旦那を\x01",
            "亡くしてしまったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "ただ、彼女の家族は外国で\x01",
            "元気に暮らしておるらしい。\x01",
            "……そこが救いじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195E")

    Jump("loc_1B88")

    label("loc_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1971")
    Jump("loc_1B88")

    label("loc_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_197F")
    Jump("loc_1B88")

    label("loc_197F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199A")
    Call(0, 5)
    Jump("loc_1ADB")

    label("loc_199A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5B")

    #C0048
    ChrTalk(
        0xFE,
        (
            "ガイはよくそこの小屋に\x01",
            "酒を飲みにきていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "よく、夜が明けるまで\x01",
            "酒を酌み交わしたもんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "ふふ、奴はなかなかの酒豪でな。\x01",
            "何度酔い潰されたか分からんわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ADB")

    label("loc_1A5B")


    #C0051
    ChrTalk(
        0xFE,
        (
            "ガイの奴はなかなかの酒豪でな。\x01",
            "何度酔い潰されたか分からんわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……奴を飲み負かせなかったのは、\x01",
            "一つの心残りじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADB")

    Jump("loc_1B88")

    label("loc_1AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFB")
    Call(0, 5)
    Jump("loc_1B88")

    label("loc_1AFB")


    #C0053
    ChrTalk(
        0xFE,
        (
            "普段、わしは\x01",
            "この墓地の管理をしておる。\x01",
            "気が向いたらいつでも来るがええ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "そうだな、その時に覚えていたら\x01",
            "ガイの昔話でもしてやろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B88")

    TalkEnd(0xFE)
    Return()

    # Function_4_CA7 end

    def Function_5_1B8C(): pass

    label("Function_5_1B8C")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x9,
        (
            "おお、お前さんはロイド……\x01",
            "久しぶりじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "いつ戻ってきたんじゃ？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000Fええ、ついこの間です。\x01",
            "ご無沙汰していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        "#10105Fロイドさん、この方は……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C9A")

    #C0059
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、以前ある依頼で\x01",
            "知り合ったのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9A")


    #C0060
    ChrTalk(
        0x101,
        (
            "#00000Fああ……\x01",
            "俺の兄貴と飲み仲間だった\x01",
            "クイントさんだよ。\x02\x03",

            "#00004F弟の俺にもよくしてくれててさ。\x01",
            "教団事件のあと一緒に飲んだときも\x01",
            "色々と昔話を聞かせてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        "あの時は楽しませてもらったぞい。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "まあ、ロイドはガイほど飲まんから\x01",
            "少々つまらんかったがのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00012Fはは……すいません。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、その時は私たちも\x01",
            "同席させてもらったの。\x02\x03",

            "#00109F未成年のティオちゃんは\x01",
            "ジュースだけで不満そうだったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、なるほどね。\x02\x03",

            "#10304Fまあ、これからは僕たちとも\x01",
            "よろしく頼むよ、ご老人。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "うむ、ロイドの同僚なら大歓迎じゃ。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "普段、わしはこの墓地の管理をしておる。\x01",
            "気が向いたらいつでも来るがええ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_5_1B8C end

    def Function_6_1F20(): pass

    label("Function_6_1F20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202F")

    #C0068
    ChrTalk(
        0xFE,
        (
            "街に化け物が出るなんていう\x01",
            "あの怖い出来事を超えて、\x01",
            "ようやく墓参りに来る事ができたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "どうしようもなく不安だったけど、\x01",
            "死んだこの人のことを考えると\x01",
            "勇気がわいてきた……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "きっと私を護ってくれていたのね。\x01",
            "ありがとう、あなた……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20A5")

    label("loc_202F")


    #C0071
    ChrTalk(
        0xFE,
        (
            "死んだこの人のことを考えると\x01",
            "勇気がわいてくる……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "きっと何が起こっても大丈夫。\x01",
            "負けたりなんかしないから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A5")

    Jump("loc_2E65")

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20B8")
    Jump("loc_2E65")

    label("loc_20B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_221C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218F")

    #C0073
    ChrTalk(
        0xFE,
        (
            "今日の朝、レミフェリアにいた\x01",
            "息子夫婦が心配して来てくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "私なんか放っておいて、\x01",
            "安全なところにいた方が\x01",
            "いいでしょうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "ふふ、でも……\x01",
            "とても嬉しいのはなぜかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2217")

    label("loc_218F")


    #C0076
    ChrTalk(
        0xFE,
        (
            "今日の朝、レミフェリアにいた\x01",
            "息子夫婦が心配して来てくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "安全なところにいてほしいけど……\x01",
            "とても嬉しいのはなぜかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2217")

    Jump("loc_2E65")

    label("loc_221C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_237C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EE")

    #C0078
    ChrTalk(
        0xFE,
        (
            "先日の襲撃事件、\x01",
            "とても恐ろしかったわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "主人を失くした３０年前の紛争を\x01",
            "思い出してしまったくらいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "もう二度と、あんな思いは\x01",
            "したくなかったのだけれど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2377")

    label("loc_22EE")


    #C0081
    ChrTalk(
        0xFE,
        (
            "先日の襲撃事件で、\x01",
            "主人を失くした３０年前の紛争を\x01",
            "思い出してしまったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "もう二度と、あんな思いは\x01",
            "したくなかったのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2377")

    Jump("loc_2E65")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_23E8")

    #C0083
    ChrTalk(
        0xFE,
        (
            "まさか、こんな事件が\x01",
            "起きてしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "まるで紛争の時代みたい。\x01",
            "恐ろしいわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_23E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_23F6")
    Jump("loc_2E65")

    label("loc_23F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2494")

    #C0085
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00005F（熱心にお祈りしてるみたいだ……）\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x105,
        (
            "#10300F（邪魔しちゃ悪いし、\x01",
            "  行くとしようか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24B2")

    label("loc_2494")


    #C0088
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_24B2")

    Jump("loc_2E65")

    label("loc_24B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2582")

    #C0089
    ChrTalk(
        0xFE,
        (
            "最近、各地で妙な化物が\x01",
            "目撃されているらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "街のほうでも、\x01",
            "無闇に街道に出ないようにって\x01",
            "呼びかけがあったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "墓地が街の近くにあって\x01",
            "本当に良かったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25F2")

    label("loc_2582")


    #C0092
    ChrTalk(
        0xFE,
        (
            "街の外でも、大聖堂までなら\x01",
            "そんなに危険じゃないだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "墓地が街の近くにあって\x01",
            "本当に良かったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F2")

    Jump("loc_2E65")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2658")

    #C0094
    ChrTalk(
        0xFE,
        "綺麗な夕焼けね……\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    #C0095
    ChrTalk(
        0xFE,
        (
            "ふふ、あなた。\x01",
            "また明日来るわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2689")

    label("loc_2658")


    #C0096
    ChrTalk(
        0xFE,
        (
            "もう夕方だし……\x01",
            "私もそろそろ帰らないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2689")

    Jump("loc_2E65")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_282B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BA")

    #C0097
    ChrTalk(
        0xFE,
        (
            "最近、ささやかな趣味として\x01",
            "寝る前に読書をするように\x01",
            "なったのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "この間、新しい本を買うときに\x01",
            "同じ本を２冊選んでしまったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "あなたたち、よかったら\x01",
            "１冊もらってくださらない？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0100
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 6)
    Jump("loc_2826")

    label("loc_27BA")


    #C0101
    ChrTalk(
        0xFE,
        (
            "最近、息子夫婦に勧められて\x01",
            "趣味を持つことにしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ふふ、やっぱり人生には\x01",
            "楽しみがなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2826")

    Jump("loc_2E65")

    label("loc_282B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2943")

    #C0103
    ChrTalk(
        0xFE,
        (
            "この間、レミフェリアにいる\x01",
            "息子夫婦から手紙が届いてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "クロスベルに１人でいる私に\x01",
            "レミフェリアに来ないかって\x01",
            "誘ってくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "でも、やっぱりクロスベルは\x01",
            "離れられないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "ここは、私と死んだ主人との\x01",
            "大切な思い出が詰まった場所だから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29CC")

    label("loc_2943")


    #C0107
    ChrTalk(
        0xFE,
        (
            "誘いは嬉しかったけど……\x01",
            "私はクロスベルを\x01",
            "離れるつもりはないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "ここは、私と死んだ主人との\x01",
            "大切な思い出が詰まった場所だから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CC")

    Jump("loc_2E65")

    label("loc_29D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A6C")

    #C0109
    ChrTalk(
        0xFE,
        (
            "クローディア姫って、\x01",
            "とてもお優しそうな方ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "リベールのアリシア女王も\x01",
            "写真でみたことあるけど……\x01",
            "やはり雰囲気が似てらっしゃるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_2A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AF8")

    #C0111
    ChrTalk(
        0xFE,
        (
            "クロスベルの新しい時代を\x01",
            "象徴する建造物、オルキスタワー……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "ふふ、できたら夫と一緒に\x01",
            "除幕式を見に行きたかったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_2AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD4")

    #C0113
    ChrTalk(
        0xFE,
        (
            "通商会議には、帝国と共和国の\x01",
            "首脳も来るみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "紛争ばかりしていたときと比べると、\x01",
            "時代が変わったのを感じるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "これからは武力ではなく話し合いで、\x01",
            "いい時代を作ってほしいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C19")

    label("loc_2BD4")


    #C0116
    ChrTalk(
        0xFE,
        (
            "これからは武力ではなく話し合いで、\x01",
            "いい時代を作ってほしいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C19")

    Jump("loc_2E65")

    label("loc_2C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C2C")
    Jump("loc_2E65")

    label("loc_2C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CAD")

    #C0117
    ChrTalk(
        0xFE,
        (
            "あちらの方……\x01",
            "新しいシスターさんかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "ふふ……レミフェリアにいる\x01",
            "孫娘くらいの歳みたい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CF4")

    label("loc_2CAD")


    #C0119
    ChrTalk(
        0xFE,
        (
            "レミフェリアに孫娘がいるの。\x01",
            "歳はあのシスターさんくらいかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF4")

    Jump("loc_2E65")

    label("loc_2CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2D59")

    #C0120
    ChrTalk(
        0xFE,
        (
            "あら……\x01",
            "日が沈んできたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "私もそろそろ、\x01",
            "お家に帰るとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_2D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E11")

    #C0122
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0123
    ChrTalk(
        0xFE,
        (
            "あ、あらごめんなさい。\x01",
            "気づかなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "主人の墓にお祈りを\x01",
            "捧げていたものだから……\x01",
            "どうか許して頂戴ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E65")

    label("loc_2E11")


    #C0125
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#00103F（……邪魔をしては悪いわ。\x01",
            "  行きましょう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E65")

    TalkEnd(0xFE)
    Return()

    # Function_6_1F20 end

    def Function_7_2E69(): pass

    label("Function_7_2E69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E7A")
    Jump("loc_38BA")

    label("loc_2E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E88")
    Jump("loc_38BA")

    label("loc_2E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_31A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310C")

    #C0127
    ChrTalk(
        0xA,
        (
            "#04401F山道方面には猟兵たちが\x01",
            "展開しているようですね。\x02\x03",

            "#04403F……《星杯騎士》として、\x01",
            "私は表立った行動を\x01",
            "とることができません。\x02\x03",

            "#04408Fこの大変な時に\x01",
            "お力添えをできないのは、\x01",
            "大変心苦しいですが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FB3")

    #C0128
    ChrTalk(
        0x103,
        (
            "#00200Fそういえば、リースさんは\x01",
            "随分腕が立つんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB3")


    #C0129
    ChrTalk(
        0x102,
        (
            "#00108F確かに《星杯騎士》の力を\x01",
            "借りられるなら心強いですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x105,
        (
            "#10301Fまあ、山道にいるのは\x01",
            "かなり厄介な相手だろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#00003Fリースさんは、\x01",
            "もしもの時のためにも\x01",
            "ここで待っていてください。\x02\x03",

            "#00001Fマインツのことは俺たちや\x01",
            "警備隊でなんとかしてみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "#04401F……分かりました。\x01",
            "皆さんも充分にお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_319F")

    label("loc_310C")


    #C0133
    ChrTalk(
        0xA,
        (
            "#04401F山道方面には猟兵たちが\x01",
            "展開しているようです。\x02\x03",

            "#04403F私は《星杯騎士》の立場上、\x01",
            "力添えはできませんが……\x01",
            "どうかお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319F")

    Jump("loc_38BA")

    label("loc_31A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31B2")
    Jump("loc_38BA")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3278")

    #C0134
    ChrTalk(
        0xA,
        (
            "#04400F『プレロマ草』については、\x01",
            "騎士団と連絡を取り次第\x01",
            "こちらでも調査を始めるつもりです。\x02\x03",

            "#04403F私１人でどこまで\x01",
            "調べきれるか分かりませんが……\x01",
            "何か分かり次第、ご報告します。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BA")

    label("loc_3278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_35B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3548")

    #C0135
    ChrTalk(
        0xA,
        "#04400Fみなさん……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00000Fリースさん……\x01",
            "こちらにいたんですね。\x02\x03",

            "#00004F昨日は、貴重な情報を\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#04404Fいえ、お役に立てたなら幸いです。\x02\x03",

            "#04400Fみなさんは、これからどちらへ？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#00100Fええ、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィは人形工房に行く事を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0140
    ChrTalk(
        0xA,
        (
            "#04405Fローゼンベルク工房……\x02\x03",

            "#04403F確か《結社》に関係があると\x01",
            "目されている場所ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、さすがは\x01",
            "星杯騎士といった所かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "#04403F……ヨルグ・ローゼンベルクは\x01",
            "弁えた人物とは聞いていますが……\x02\x03",

            "#04401Fそれでも《結社》と繋がりが\x01",
            "あることには変わりません。\x02\x03",

            "会うつもりなら、\x01",
            "充分に注意されるべきでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00004Fええ……そのつもりです。\x01",
            "ご忠告ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 2)
    Jump("loc_35B1")

    label("loc_3548")


    #C0144
    ChrTalk(
        0xA,
        (
            "#04400F人形工房に行くのなら、\x01",
            "万全な準備をして行くべきでしょう。\x02\x03",

            "#04403F……どうか、お気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B1")

    Jump("loc_38BA")

    label("loc_35B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_35C4")
    Jump("loc_38BA")

    label("loc_35C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_35D2")
    Jump("loc_38BA")

    label("loc_35D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35E0")
    Jump("loc_38BA")

    label("loc_35E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35EE")
    Jump("loc_38BA")

    label("loc_35EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35FC")
    Jump("loc_38BA")

    label("loc_35FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_360A")
    Jump("loc_38BA")

    label("loc_360A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3618")
    Jump("loc_38BA")

    label("loc_3618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_38A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3637")
    TalkEnd(0xFE)
    Call(0, 8)
    Return()

    label("loc_3637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3820")

    #C0145
    ChrTalk(
        0xA,
        (
            "#13800F慰霊碑の参拝を済ませたら、\x01",
            "あとで先輩方に仕事の内容を\x01",
            "聞きに行かなくては。\x02\x03",

            "#13804F着任にあたって色々と\x01",
            "やることが多いみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#00105Fあ……なんだか\x01",
            "邪魔してしまったでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "#13800Fいえ、そんなことは……\x01",
            "キーアさんにも会えましたし。\x02\x03",

            "#13803F……それよりも、\x01",
            "なんだかおなかが\x01",
            "すいてきてしまいました。\x02\x03",

            "#13802F早く寄宿舎にもどって、\x01",
            "ベーカリーで買ったパンを\x01",
            "食べたいところですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#00109F（ふふ、食いしん坊なのは\x01",
            "  相変わらずみたいね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_389E")

    label("loc_3820")


    #C0149
    ChrTalk(
        0xA,
        (
            "#13800F私はしばらく、\x01",
            "このクロスベル大聖堂で\x01",
            "お世話になると思います。\x02\x03",

            "何かありましたら、\x01",
            "いつでもいらっしゃって下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389E")

    Jump("loc_38BA")

    label("loc_38A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_38B1")
    Jump("loc_38BA")

    label("loc_38B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_38BA")

    label("loc_38BA")

    TalkEnd(0xFE)
    Return()

    # Function_7_2E69 end

    def Function_8_38BE(): pass

    label("Function_8_38BE")

    EventBegin(0x0)
    Fade(500)
    OP_68(540, 5500, 39970, 0)
    MoveCamera(316, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14580, 0)
    SetChrPos(0x101, 0, 4000, 40000, 0)
    SetChrPos(0x102, -1600, 4000, 40700, 0)
    SetChrPos(0x109, -800, 4000, 39100, 0)
    SetChrPos(0x105, 1300, 4000, 39000, 0)
    SetChrPos(0x153, 1450, 4000, 40510, 0)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    TurnDirection(0x109, 0xA, 0)
    TurnDirection(0x105, 0xA, 0)
    TurnDirection(0x153, 0xA, 0)
    OP_0D()
    Sleep(100)
    TurnDirection(0xA, 0x101, 500)

    #C0150
    ChrTalk(
        0xA,
        (
            "#11P#13800Fああ、みなさん……\x01",
            "先ほどはどうも。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#6P#00000Fリースさん、着任の挨拶は\x01",
            "終わったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        "#11P#13804Fええ、つつがなく終わりました。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 500)

    #C0153
    ChrTalk(
        0xA,
        (
            "#11P#13800F……その子がさっき言っていた、\x01",
            "知り合いの子……ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#00100Fええ、キーアちゃんです。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x153,
        (
            "#12P#01105Fお姉ちゃん、\x01",
            "もしかして新しいシスタ～？\x02\x03",

            "#01109Fえへへ、こんにちはっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0156
    ChrTalk(
        0xA,
        "#11P#13802F……可愛い……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、そうでしょう？\x01",
            "それに、とっても\x01",
            "いい子なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#6P#00009Fよく食事の手伝いを\x01",
            "してくれたりするし……\x01",
            "すごく助かっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#12P#10306Fやれやれ、こんなとこでも\x01",
            "親バカ発揮かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        (
            "#6P#10109Fあはは……\x01",
            "気持ちは分かりますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x153,
        "#12P#01111Fほえ～？\x02",
    )

    CloseMessageWindow()

    def lambda_3C53():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C53)
    Sleep(50)

    def lambda_3C63():
        TurnDirection(0x105, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C63)
    Sleep(50)

    def lambda_3C73():
        TurnDirection(0x102, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C73)
    Sleep(50)

    def lambda_3C83():
        TurnDirection(0x109, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C83)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    #C0162
    ChrTalk(
        0xA,
        (
            "#11P#13803F（……なるほど、この子が\x01",
            "　例の教団の……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D3F():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D3F)
    Sleep(50)

    def lambda_3D4F():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D4F)
    Sleep(50)

    def lambda_3D5F():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D5F)
    Sleep(50)

    def lambda_3D6F():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D6F)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0163
    ChrTalk(
        0x102,
        (
            "#00105Fえっと、リースさん。\x01",
            "どうかしました？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "#11P#13803F……いいえ、なんでもありません。\x02\x03",

            "#13802Fキーアさん、\x01",
            "これからよろしくおねがいしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x153,
        "#12P#01109Fうんっ、よろしくねー！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x135, 5)
    SetChrPos(0x0, 0, 4000, 40000, 180)
    EventEnd(0x5)
    Return()

    # Function_8_38BE end

    def Function_9_3E6E(): pass

    label("Function_9_3E6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3F")

    #C0166
    ChrTalk(
        0xFE,
        (
            "おや、あなたがたは……\x01",
            "昨夜アルセイユに訪れていた\x01",
            "特務支援課の皆様ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "クローディア姫殿下とユリア准佐が\x01",
            "この先にいらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "よろしければどうぞ、\x01",
            "お通りください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F9E")

    label("loc_3F3F")


    #C0169
    ChrTalk(
        0xFE,
        (
            "クローディア姫殿下とユリア准佐が\x01",
            "この先にいらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        "どうぞ、お通りください。\x02",
    )

    CloseMessageWindow()

    label("loc_3F9E")

    TalkEnd(0xFE)
    Return()

    # Function_9_3E6E end

    def Function_10_3FA2(): pass

    label("Function_10_3FA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4032")

    #C0171
    ChrTalk(
        0xFE,
        (
            "さすがに、墓地で\x01",
            "騒ぎを起こそうなんて奴は\x01",
            "いないとは思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "万が一ということもある。\x01",
            "しっかり警戒しないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_407B")

    label("loc_4032")


    #C0173
    ChrTalk(
        0xFE,
        (
            "必要最低限での警備……\x01",
            "責任は重大だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "しっかり警戒しないとな。\x02",
    )

    CloseMessageWindow()

    label("loc_407B")

    TalkEnd(0xFE)
    Return()

    # Function_10_3FA2 end

    def Function_11_407F(): pass

    label("Function_11_407F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F5")

    #C0175
    ChrTalk(
        0xFE,
        (
            "……あら、あなたたち。\x01",
            "こんなところで奇遇ね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FD")

    #C0176
    ChrTalk(
        0x101,
        (
            "#00003Fお参りしていたみたいですね。\x01",
            "……失礼しました。\x02\x03",

            "#00000F……もしかして、\x01",
            "こちらに眠ってらっしゃるのは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x109,
        (
            "#10108Fオズマ・シーカー二尉……\x01",
            "１０年ほど前に亡くなった、\x01",
            "あたしとフランの父です。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41BD")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_41BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E0")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_41E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4203")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_4203")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4223")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_4223")

    Sleep(1000)

    #C0178
    ChrTalk(
        0x102,
        "#00105Fノエルさんのお父様……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        (
            "#00303F話だけは聞いたことあるな……\x01",
            "かなり優秀な士官だったそうだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x105,
        "#10305Fへえ、そうなのかい？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "ええ、正義感が強くて\x01",
            "厳格な人だったけど……\x01",
            "任務中の事故でね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B8")

    label("loc_42FD")


    #C0182
    ChrTalk(
        0x101,
        (
            "#00003Fお参りしていたみたいですね。\x01",
            "……失礼しました。\x02\x03",

            "#00008F……たしか、\x01",
            "こちらに眠ってらっしゃるのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x109,
        (
            "#10108F……ええ、\x01",
            "１０年ほど前に亡くなった\x01",
            "あたしとフランの父です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B8")


    #C0184
    ChrTalk(
        0xFE,
        (
            "……警備隊員という仕事だから、\x01",
            "覚悟だけはしていたけど……\x01",
            "やっぱり当時は堪えたわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "ふふ、昔の話なんだから\x01",
            "そんなしんみり\x01",
            "しないでちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "……でも、あなたたちも\x01",
            "命を大事にしなきゃだめよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "あなたたちがいなくなったら、\x01",
            "悲しむ人は大勢いるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x109,
        "#10104F……うん、分かってる。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 3)
    Jump("loc_4561")

    label("loc_44F5")


    #C0189
    ChrTalk(
        0xFE,
        (
            "あなたたちも\x01",
            "命を大事にしなきゃだめよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "あなたたちがいなくなったら、\x01",
            "悲しむ人は大勢いるんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4561")

    TalkEnd(0xFE)
    Return()

    # Function_11_407F end

    def Function_12_4565(): pass

    label("Function_12_4565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458E")
    Call(0, 26)
    Return()

    label("loc_458E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45A5")
    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Jump("loc_45BB")

    label("loc_45A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_45B7")
    Call(0, 29)
    Return()

    label("loc_45B7")

    Call(0, 27)
    Return()

    label("loc_45BB")

    Jump("loc_45C6")

    label("loc_45C0")

    TalkBegin(0xFE)
    TalkEnd(0xFE)

    label("loc_45C6")

    Return()

    # Function_12_4565 end

    def Function_13_45C7(): pass

    label("Function_13_45C7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "鐘の下より生まれし子羊たちよ\x01",
            "  どうか安らかに眠りたまえ\x02",
        )
    )

    CloseMessageWindow()

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 純白の雲間から差す黄金の陽光が\x01",
            "蒼き大空へと続く一筋の道となりて\x01",
            "    魂を女神の元へと導かん\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_45C7 end

    def Function_14_469C(): pass

    label("Function_14_469C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 オズマ・シーカー\x01",
            "  　　　　ここに眠る\x01",
            "───────────────\x01",
            "  Ｓ１１５７　～　Ｓ１１９４　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4909")

    #C0194
    ChrTalk(
        0x101,
        (
            "#00005F『シーカー』って……\x01",
            "もしかして？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x109,
        (
            "#10108Fオズマ・シーカー二尉……\x01",
            "１０年ほど前に亡くなった、\x01",
            "あたしとフランの父です。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        "#00105Fノエルさんのお父様……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x105,
        "#10305Fふうん、初めて聞くけど……\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x109,
        (
            "#10109Fあはは、あたしもあまり\x01",
            "自分からこういうことは\x01",
            "話さないタイプだから。\x02\x03",

            "#10104F……皆さん、行きましょう。\x01",
            "こんな所で立ち止まってると\x01",
            "父さんに叱られてしまいそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#00000F……はは、そうか。\x01",
            "それじゃあ行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 2)

    label("loc_4909")

    TalkEnd(0xFF)
    Return()

    # Function_14_469C end

    def Function_15_490D(): pass

    label("Function_15_490D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 　　　ガイ・バニングス\x01",
            "　　　　　ここに眠る\x01",
            "───────────────\x01",
            "　Ｓ１１７６　～　Ｓ１２０１　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A83")

    #C0201
    ChrTalk(
        0x153,
        (
            "#01105F（……このお墓のヒトって……）\x02\x03",

            "#01103F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "キーアは静かに手を合わせた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x0, 6)

    #C0203
    ChrTalk(
        0x101,
        "#00002Fはは……ありがとな。\x02",
    )

    CloseMessageWindow()

    label("loc_4A83")

    TalkEnd(0xFF)
    Return()

    label("loc_4A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_4AEE")

    #C0204
    ChrTalk(
        0x101,
        (
            "#00000Fこの花束……\x01",
            "多分、アリオスさんが\x01",
            "供えてくれたんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B37")

    label("loc_4AEE")


    #C0205
    ChrTalk(
        0x101,
        (
            "#00005Fあれ……\x01",
            "花束が供えられてるみたいだ。\x02\x03",

            "#00003F一体誰が……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B37")

    SetScenarioFlags(0x0, 6)
    Jump("loc_4B74")

    label("loc_4B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B5E")
    TalkEnd(0xFF)
    Call(0, 17)
    Return()

    label("loc_4B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B74")
    TalkEnd(0xFF)
    Call(0, 16)
    Return()

    label("loc_4B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4F89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F21")

    #C0206
    ChrTalk(
        0x101,
        "#00008F…………………………\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        "#00105Fロイド……？\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00000Fはは、いや……\x01",
            "アリオスさんに兄貴の最期を\x01",
            "聞かせてもらったけどさ……\x02\x03",

            "#00004F本当に、最後の最後まで\x01",
            "俺やセシル姉のことばかり\x01",
            "心配しててさ……\x02\x03",

            "しかも、アリオスさんや\x01",
            "イアン先生のことも\x01",
            "少しも恨んじゃいなくて……\x02\x03",

            "#00000Fまったく、どれだけ\x01",
            "お人好しだったんだと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        "#00200Fロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00304F……ハハ、安心しろ。\x02\x03",

            "#00302Fそういうとこはお前も\x01",
            "十分に受け継いでるからよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D83")

    #C0211
    ChrTalk(
        0x10A,
        "#00604Fフッ……確かにな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DE2")

    label("loc_4D83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DB5")

    #C0212
    ChrTalk(
        0x109,
        "#10102Fふふっ、確かに。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DE2")

    label("loc_4DB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DE2")

    #C0213
    ChrTalk(
        0x105,
        "#10402Fアハハ、確かに。\x02",
    )

    CloseMessageWindow()

    label("loc_4DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E1C")

    #C0214
    ChrTalk(
        0x106,
        "#10702Fクスクス……言えてます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7F")

    label("loc_4E1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E4C")

    #C0215
    ChrTalk(
        0x105,
        "#10404F言えてるねえ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7F")

    label("loc_4E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E7F")

    #C0216
    ChrTalk(
        0x109,
        "#10102Fふふっ、言えてますね。\x02",
    )

    CloseMessageWindow()

    label("loc_4E7F")


    #C0217
    ChrTalk(
        0x101,
        (
            "#00012Fあ、あのなぁ。\x01",
            "……はは、まあいいや。\x02\x03",

            "#00000Fとにかく……\x01",
            "後はキーアを助け出すだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00100Fええ、最後まで\x01",
            "気を抜かずに行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 5)
    Jump("loc_4F84")

    label("loc_4F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F84")

    #C0219
    ChrTalk(
        0x101,
        (
            "#00000F……後はキーアを助け出すだけだ。\x02\x03",

            "#00004F兄貴……どうか見守っていてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4F84")

    Jump("loc_5053")

    label("loc_4F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA3")
    TalkEnd(0xFF)
    Call(0, 21)
    Return()

    label("loc_4FA3")

    Jump("loc_5053")

    label("loc_4FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5053")

    #C0220
    ChrTalk(
        0x101,
        (
            "#00000F（兄貴……\x01",
            "  クロスベル市に戻ってきたよ。）\x02\x03",

            "#00004F（これからなんとしても\x01",
            "  キーアを取り戻してみせる。\x01",
            "  どうか見守っていてくれ……！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5053")

    TalkEnd(0xFF)
    Return()

    # Function_15_490D end

    def Function_16_5057(): pass

    label("Function_16_5057")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-22240, 1300, 23760, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(13720, 0)
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -22700, 0, 21640, 0)
    SetChrPos(0x109, -21150, 0, 22390, 315)
    SetChrPos(0x105, -23900, 0, 22740, 0)
    SetCameraDistance(13720, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0221
    ChrTalk(
        0x102,
        "#6P#00108Fこのお墓は……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00003Fガイ・バニングス……\x01",
            "３年前に殉職した、俺の兄貴だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x109,
        (
            "#12P#10100Fなんでも、警察でも\x01",
            "１、２を争うくらいの\x01",
            "凄腕捜査官だったそうですね。\x02\x03",

            "#10104F警備隊のほうでも、その名前を\x01",
            "知っている人は少なくないです。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x105,
        "#6P#10305Fへえ、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00000F元はセルゲイ課長の部下で、\x01",
            "あのアリオスさんと\x01",
            "コンビを組んでいたみたいだし……\x02\x03",

            "#00003F色々あって班が解散したあとも、\x01",
            "捜査一課でダドリーさんと\x01",
            "互角に渡り合ってたそうだ。\x02\x03",

            "#00009Fまあ、色々な方面に\x01",
            "首を突っ込んでたらしいから\x01",
            "とんでもなく顔が広かったのは確かだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        "#6P#00104F話を聞けば聞くほど凄い人よね……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00003F尋常じゃない行動力で\x01",
            "クロスベルの様々な《壁》に\x01",
            "立ち向かっていた捜査官……\x02\x03",

            "#00008F……殉職だなんて、\x01",
            "本当に信じられなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        (
            "#12P#10101F結局、例の教団も\x01",
            "お兄さんを殺害した犯人じゃ\x01",
            "なかったんですよね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#00008Fああ……\x01",
            "いまだに真相は謎のままだ。\x02\x03",

            "#00003F（でも……いつか必ず、\x01",
            "  この手で真実を掴んでみせる。）\x02\x03",

            "#00000F（少し先のことに\x01",
            "  なるかもしれないけど……\x01",
            "  待っていてくれ、兄貴。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x136, 0)
    EventEnd(0x5)
    Return()

    # Function_16_5057 end

    def Function_17_5504(): pass

    label("Function_17_5504")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-22240, 1300, 23760, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(13720, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -22700, 0, 21640, 0)
    SetChrPos(0x103, -21150, 0, 22390, 315)
    SetChrPos(0x104, -23900, 0, 22740, 0)
    SetChrPos(0x105, -20180, 0, 23320, 270)
    SetChrPos(0x109, -24250, 0, 21630, 0)
    SetCameraDistance(13720, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0230
    ChrTalk(
        0x101,
        "#00003F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x103,
        "#00203F#12P#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x105,
        (
            "#10305F#12P……そういえば……\x02\x03",

            "#10303Fロイドのお兄さんの墓は\x01",
            "ここだと聞いているけど……\x02\x03",

            "#10300Fご両親の方はどうなんだい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0233
    ChrTalk(
        0x104,
        "#00305F#6Pそう言やあ……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#00108F#6P……たしかお２人とも\x01",
            "亡くなってらっしゃるのよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    #C0235
    ChrTalk(
        0x101,
        (
            "#00004F#11Pああ、１５年前にね。\x02\x03",

            "#00008F……正直、小さかったから\x01",
            "あんまり良く覚えてないんだ。\x02\x03",

            "#00000F当時就航したばかりの導力飛行船の\x01",
            "事故だったとは聞いてるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        "#00106F#6P飛行船事故で……そうだったの。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x109,
        (
            "#10108F#6Pまだ飛行船が実用化したばかりで\x01",
            "不安定だった頃ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#00006F#11Pああ、結局山間部に落ちて\x01",
            "遺体も見付からなかったらしくて……\x02\x03",

            "#00008F兄貴も色々と大変だったみたいだ。\x02\x03",

            "#00002Fおまけに、まだまだ手のかかる\x01",
            "幼い弟も養わなくちゃならなくて……\x02\x03",

            "#00012F……はは……\x01",
            "本当、一生頭が上がらないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        "#00108F#6Pロイド……\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#00304F#6Pま、たぶんお前の兄貴はそれを\x01",
            "重荷になんて思いもしなかっただろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        (
            "#00204F#12Pそうですね……\x02\x03",

            "#00214F話していて、ロイドさんのことが\x01",
            "可愛くて仕方ないオーラでしたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x105,
        (
            "#10302F#12Pあはは、気持ちは判るけどね。\x02\x03",

            "#10309F３歳のロイドか……\x01",
            "さぞ可愛かったんだろうな㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        "#00102F#6Pた、確かに想像すると……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x109,
        (
            "#10112F#6P……抱きしめちゃいたいくらい\x01",
            "可愛らしい感じかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        "#00309F#6Pおお、容易に想像できるかもな！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_5BD7")

    #C0246
    ChrTalk(
        0x101,
        (
            "#00011F#11Pか、からかうなって。\x02\x03",

            "#00004F──ゴメン、時間を取らせた。\x01",
            "リースさんの所に行かなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5C3D")

    label("loc_5BD7")


    #C0247
    ChrTalk(
        0x101,
        (
            "#00011F#11Pか、からかうなって。\x02\x03",

            "#00004F──ゴメン、時間を取らせた。\x01",
            "とにかく大聖堂に行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5C3D")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x17C, 6)
    EventEnd(0x5)
    Return()

    # Function_17_5504 end

    def Function_18_5C6C(): pass

    label("Function_18_5C6C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0248
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 サヤ・マクレイン\x01",
            "　　　　　ここに眠る\x01",
            "───────────────\x01",
            "　Ｓ１１７５　～　Ｓ１１９９　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D88")

    #C0249
    ChrTalk(
        0x153,
        (
            "#01108Fこのお墓は……\x02\x03",

            "#01100Fロイド、お参りしていこっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#00000F……ああ、そうだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_5D88")

    Jump("loc_5D9F")

    label("loc_5D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D9F")
    Call(0, 19)

    label("loc_5D9F")

    TalkEnd(0xFF)
    Return()

    # Function_18_5C6C end

    def Function_19_5DA3(): pass

    label("Function_19_5DA3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(21300, 1500, 31700, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14830, 0)
    SetChrPos(0x101, 21140, 0, 32049, 0)
    SetChrPos(0x102, 19720, 0, 31850, 45)
    SetChrPos(0x109, 22920, 0, 31580, 315)
    SetChrPos(0x105, 21620, 0, 30560, 0)
    SetCameraDistance(12830, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0251
    ChrTalk(
        0x109,
        (
            "#12P#10105Fこのお墓の名前……\x01",
            "どこか聞き覚えが……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00008F《風の剣聖》、\x01",
            "アリオス・マクレイン。\x02\x03",

            "#00003F直接聞いた事はないけど、\x01",
            "多分彼の奥さんだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#00108F確か、事故に巻き込まれて、\x01",
            "亡くなってしまったのよね……\x02\x03",

            "#00103F一緒にいたシズクちゃんは\x01",
            "一命は取り留めたけど、\x01",
            "光を失ってしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00003Fああ、そしてアリオスさんは\x01",
            "警察を辞めて遊撃士になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x105,
        "#6P#10300Fふうん、なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x109,
        (
            "#12P#10108Fなんだか、やりきれない\x01",
            "話ですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        (
            "#00000F……希望がないわけじゃない。\x02\x03",

            "#00004Fシズクちゃんの目は\x01",
            "まだ光を取り戻せる可能性が\x01",
            "あるみたいだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#00100Fそうね……\x01",
            "近いうちに見舞いに行けると\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 20740, 0, 31990, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x135, 7)
    EventEnd(0x5)
    Return()

    # Function_19_5DA3 end

    def Function_20_60E1(): pass

    label("Function_20_60E1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0259
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 　………………　……　　　　　\x01",
            " 　……　……………………\x01",
            "　　　　　こ……眠……\x01",
            "───────────────……\x01",
            "　Ｓ１………　～　Ｓ１…８…　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62DC")

    #C0260
    ChrTalk(
        0x101,
        (
            "#00001Fボロボロの墓だ。\x01",
            "文字も風化して潰れてしまってる……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x105,
        (
            "#10300Fちょっとこれじゃあ、\x01",
            "解読する事はできなそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x109,
        (
            "#10106F解読って……\x01",
            "暗号遊びじゃないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#00100Fどなたのお墓か分からないけど……\x01",
            "手入れはされてるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#00000F一応、お参りしていくか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 6)

    label("loc_62DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_END)), "loc_6406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_635E")

    #C0265
    ChrTalk(
        0x101,
        (
            "#00001F（このお墓は、イアン先生の\x01",
            "  妻子のものだった……）\x02\x03",

            "#00003F（……今は行くとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_635E")

    Jump("loc_6406")

    label("loc_6363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6406")

    #C0266
    ChrTalk(
        0x101,
        (
            "#00001F（このお墓は、イアン先生の\x01",
            "  妻子のものだった……）\x02\x03",

            "#00008F（イアン先生……\x01",
            "  そんな素振りは一度だって\x01",
            "  見せなかったけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6406")

    TalkEnd(0xFF)
    Return()

    # Function_20_60E1 end

    def Function_21_640A(): pass

    label("Function_21_640A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    OP_68(-22240, 1300, 23760, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(15090, 0)
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -21100, 0, 24440, 270)
    SetChrPos(0x103, -22800, 0, 22460, 0)
    SetChrPos(0x104, -19980, 0, 23580, 270)
    SetChrPos(0xF4, -24290, 0, 23980, 45)
    SetChrPos(0xF5, -20900, 0, 22210, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(13720, 2000)
    StopBGM(0xFA0)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0267
    ChrTalk(
        0x101,
        "#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    Fade(500)
    Sound(805, 0, 70, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6545")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6545")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6565")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6565")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6585")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6585")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65A5")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_65A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65C5")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_65C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65E5")
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_65E5")

    Sleep(1000)

    #C0268
    ChrTalk(
        0x102,
        (
            "#12P#00108Fお兄さんのトンファー……\x01",
            "傷だらけで、何だか痛々しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#12P#00303F多分、あのアリオスのオッサンと\x01",
            "争ったときのものなんだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#00006Fああ……\x02\x03",

            "#00000F……だけど、よく見るとそれ以外にも\x01",
            "沢山の細かい傷なんかもついててさ。\x02\x03",

            "何度も修繕を繰り返した跡なんかも\x01",
            "あるみたいなんだ。\x02\x03",

            "#00004Fどんな《壁》に向かっても諦めずに、\x01",
            "真実を追い求めてきた兄貴……\x02\x03",

            "このトンファーの姿は、\x01",
            "きっと、兄貴の生き方そのものなんだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67DE")

    #C0271
    ChrTalk(
        0x10A,
        "#6P#00604F……そうかもしれんな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6855")

    label("loc_67DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_681D")

    #C0272
    ChrTalk(
        0x109,
        "#6P#10100F……そうかもしれませんね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6855")

    label("loc_681D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6855")

    #C0273
    ChrTalk(
        0x105,
        "#6P#10400F……そうかもしれないね。\x02",
    )

    CloseMessageWindow()

    label("loc_6855")

    OP_5A()
    Fade(500)
    Sound(805, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0274
    ChrTalk(
        0x101,
        (
            "#00008F今回の事件、そして兄貴の事件……\x02\x03",

            "#00001Fその真実に辿り着くためには、\x01",
            "アリオスさんを……そしてイアン先生を\x01",
            "乗り越えなきゃいけないだろう。\x02\x03",

            "#00004Fこのトンファーはしばらく借りていく。\x01",
            "……兄貴、どうか俺たちに力を貸してくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69A7")

    #C0275
    ChrTalk(
        0x106,
        "#6P#10710Fロイドさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A04")

    label("loc_69A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69D6")

    #C0276
    ChrTalk(
        0x105,
        "#6P#10400Fロイド……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A04")

    label("loc_69D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A04")

    #C0277
    ChrTalk(
        0x109,
        "#6P#10100Fロイドさん……\x02",
    )

    CloseMessageWindow()

    label("loc_6A04")


    #C0278
    ChrTalk(
        0x103,
        "#6P#00204F勿論、わたしたちも手伝います。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#12P#00309Fはは、だな。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#12P#00102Fキーアちゃんを取り戻す為に……\x01",
            "みんなで力を合わせましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(150)

    #C0281
    ChrTalk(
        0x101,
        (
            "#5P#00000Fああ……\x01",
            "みんな、改めてよろしく頼む！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -22300, 0, 23050, 180)
    OP_69(0xFF, 0x0)
    OP_D7(0x1F)
    SetScenarioFlags(0x1CD, 6)
    EventEnd(0x5)
    Return()

    # Function_21_640A end

    def Function_22_6B0C(): pass

    label("Function_22_6B0C")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, 380, 4000, 33790, 0)
    SetChrPos(0x102, 2620, 4000, 33580, 0)
    SetChrPos(0x103, -820, 4000, 32680, 0)
    SetChrPos(0x104, 2009, 4000, 31940, 0)
    SetChrPos(0x109, 560, 4000, 31330, 0)
    SetChrPos(0x105, -1060, 4000, 31090, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(2040, 5500, 41860, 0)
    MoveCamera(317, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14260, 0)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    FadeToBright(250, 0)
    OP_0D()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)
    TurnDirection(0x12, 0x13, 500)

    #C0282
    ChrTalk(
        0x12,
        (
            "#5P#07000Fそういえばユリアさん……\x02\x03",

            "こちらの大聖堂には、少し前から\x01",
            "“彼女”が赴任してきているそうですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    #C0283
    ChrTalk(
        0x13,
        (
            "#12P#07100Fええ、他のシスターによると\x01",
            "今日は出張しているとの事ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x12,
        (
            "#5P#07003Fそうでしたか……\x02\x03",

            "#07008Fあの時のご恩もありますし、\x01",
            "できればご挨拶したかったんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#12P#N#00005Fクローディア殿下……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0286
    ChrTalk(
        0x109,
        "#12P#N#10105Fそれにユリア准佐っ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6DB5():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6DB5)
    Sleep(50)

    def lambda_6DC5():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6DC5)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)

    #C0287
    ChrTalk(
        0x12,
        "#11P#07002Fあっ……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x13,
        "#12P#07102F彼らみたいですね。\x02",
    )

    CloseMessageWindow()
    OP_68(860, 5100, 39660, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14870, 3000)

    def lambda_6E47():
        OP_95(0xFE, 380, 4000, 38790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E47)

    def lambda_6E61():
        OP_95(0xFE, 2620, 4000, 38580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E61)

    def lambda_6E7B():
        OP_95(0xFE, -820, 4000, 37680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E7B)

    def lambda_6E95():
        OP_95(0xFE, 2009, 4000, 36940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E95)

    def lambda_6EAF():
        OP_95(0xFE, 560, 4000, 36330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6EAF)

    def lambda_6EC9():
        OP_95(0xFE, -1060, 4000, 36090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6EC9)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x12, 0)
    TurnDirection(0x102, 0x12, 0)
    TurnDirection(0x109, 0x12, 0)
    TurnDirection(0x105, 0x12, 0)
    TurnDirection(0x103, 0x12, 0)
    TurnDirection(0x104, 0x12, 0)

    #C0289
    ChrTalk(
        0x12,
        (
            "#11P#07002Fみなさん……\x01",
            "ふふっ、またお会いしましたね。\x02\x03",

            "#07009Fそろそろ来る頃だと思っていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x102,
        (
            "#12P#00105Fえっ、私たちが来るのに\x01",
            "気づいていたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x13,
        (
            "#11P#07102F今、ジークが上空を旋回して\x01",
            "周囲を見張ってくれていてね。\x02\x03",

            "それでさっき、君たちが来たのを\x01",
            "教えてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#6P#00000F昨日の白ハヤブサの……\x01",
            "はは、さすがに優秀ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x12,
        (
            "#11P#07004Fふふ、ジークは王室親衛隊の\x01",
            "情報伝達役ですから。\x02\x03",

            "#07000Fえっと、それで……\x01",
            "みなさんはこちらへは何をしに？\x02\x03",

            "#07005Fあら、それに今日は新しい方まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        (
            "#6P#00200Fどうも……昨夜付けで\x01",
            "特務支援課に復帰した、\x01",
            "ティオ・プラトーといいます。\x02\x03",

            "#00204Fこうしてお会いできて光栄です。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x12,
        "#11P#07009Fええ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        (
            "#6P#00300Fまあ、俺たちはなんとなく\x01",
            "ブラリと立ち寄ってみたって\x01",
            "ところなんッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、まさか姫様と准佐に\x01",
            "こうも早く再会できるとは\x01",
            "思ってなかったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#6P#00000F殿下たちは、こちらへ参拝に？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x12,
        (
            "#11P#07000Fええ……\x02\x03",

            "#07003Fこの墓地には、今までクロスベルで\x01",
            "亡くなった方々が数多く眠っています。\x02\x03",

            "ですから、\x01",
            "どうしても今日の本会議前に\x01",
            "立ち寄っておきたかったんです。\x02\x03",

            "#07008F《クロスベル問題》を本当の意味で\x01",
            "受け止めていくためにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#6P#00200Fクロスベル問題……\x02\x03",

            "#00204F帝国と共和国が、クロスベルの\x01",
            "帰属を争って対立している\x01",
            "問題の総称……でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#12P#00100Fええ、クロスベルに住んでいる人は\x01",
            "あまり使わない言葉だけどね。\x02\x03",

            "#00103Fこの問題のせいで、\x01",
            "まさに戦争が勃発する直前まで\x01",
            "緊張が高まっていたの。\x02\x03",

            "#00108F２年前にリベールで\x01",
            "《不戦条約》が締結された事で、\x01",
            "表面上#6R㈲　㈲　㈲#は落ち着いたのだけれど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_64(0x12)

    #C0302
    ChrTalk(
        0x102,
        (
            "#12P#00106Fす、すみませんっ！\x01",
            "私としたことが、失礼なことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x12,
        (
            "#11P#07003Fいえ……\x01",
            "エリィさんの言うことは\x01",
            "実際、正しいのです。\x02\x03",

            "#07000Fお祖母様……アリシア女王が提案した\x01",
            "不戦条約は、２大国に武力行使を\x01",
            "させないためのものでした。\x02\x03",

            "それによって当時のクロスベルは\x01",
            "極限の緊張状態から解放されましたが……\x02\x03",

            "#07003Fその一方で、両国からの\x01",
            "目に見えぬ圧力が高まっていき、\x01",
            "クロスベルの立場はいまだ危ういまま……\x02\x03",

            "#07001Fそういう意味では、不戦条約が\x01",
            "クロスベル問題を根本的に\x01",
            "解決したとは言えませんから。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    #C0304
    ChrTalk(
        0x13,
        "#12P#07108F殿下……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x109,
        (
            "#6P#10101Fで、でも……\x01",
            "自分は不戦条約が\x01",
            "無意味だったとは思えません。\x02\x03",

            "#10103F警備隊に入ったばかりでしたが、\x01",
            "当時の帝国と共和国が国境で行った\x01",
            "大規模な軍事演習の威圧感……\x02\x03",

            "#10108Fそして、帝国の《列車砲》が\x01",
            "クロスベル市に向けられた恐怖は\x01",
            "未だに忘れることができません。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#12P#00303F確かに……\x01",
            "戦争が始まっていれば、住民に\x01",
            "甚大な被害が出ていただろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x105,
        (
            "#6P#10303Fそれを取り除いただけでも\x01",
            "充分に価値ある\x01",
            "条約だったってことか。\x02\x03",

            "#10300Fまあ、殿下が気に病む必要は\x01",
            "ないんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#11P#00006Fワジ、おまえな……\x01",
            "さすがにフランクすぎるっていうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x12,
        (
            "#11P#07009Fふふっ……もちろん、\x01",
            "私も後ろ向きではいられません。\x02\x03",

            "#07004Fこの通商会議という場で、\x01",
            "クロスベルの未来を話し合う機会を\x01",
            "なんとしても作りたいと思っています。\x02\x03",

            "#07002Fこの墓地へは、その決意を\x01",
            "確かにするために訪れたんです。\x02\x03",

            "#07003Fユリアさんや親衛隊の方々には\x01",
            "余計な仕事を増やしてしまいましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x13,
        "#12P#07104F殿下……滅相もありません。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#00000Fなんというか……\x01",
            "その芯の強さは、さすがですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        (
            "#12P#00100Fええ……リベールという国が\x01",
            "本当にうらやましくなってきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x12,
        "#11P#07002Fふふっ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x13,
        "#12P#07100F……殿下、そろそろ予定の時刻です。\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x13, 500)

    #C0315
    ChrTalk(
        0x12,
        (
            "#5P#07005Fあっ、そうですね。\x01",
            "そろそろオルキスタワーに\x01",
            "向かわないと……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C45():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7C45)
    TurnDirection(0x13, 0x101, 500)

    #C0316
    ChrTalk(
        0x12,
        (
            "#11P#07004Fそれでは特務支援課の皆さん。\x01",
            "私たちはこれで失礼します。\x02\x03",

            "#07000F今日、みなさんは本会議の\x01",
            "警備にあたられると聞いていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#6P#00000Fええ、力の限り\x01",
            "勤めさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x12,
        (
            "#11P#07009Fふふっ、それではどうか\x01",
            "よろしくおねがいしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x13,
        (
            "#11P#07102Fではな、諸君。\x01",
            "次はオルキスタワーで会おう。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    def lambda_7DA4():

        label("loc_7DA4")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_7DA4")

    QueueWorkItem2(0x101, 2, lambda_7DA4)

    def lambda_7DB6():

        label("loc_7DB6")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_7DB6")

    QueueWorkItem2(0x102, 2, lambda_7DB6)

    def lambda_7DC8():

        label("loc_7DC8")

        TurnDirection(0x109, 0x12, 500)
        Yield()
        Jump("loc_7DC8")

    QueueWorkItem2(0x109, 2, lambda_7DC8)

    def lambda_7DDA():

        label("loc_7DDA")

        TurnDirection(0x105, 0x12, 500)
        Yield()
        Jump("loc_7DDA")

    QueueWorkItem2(0x105, 2, lambda_7DDA)

    def lambda_7DEC():

        label("loc_7DEC")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_7DEC")

    QueueWorkItem2(0x103, 2, lambda_7DEC)

    def lambda_7DFE():

        label("loc_7DFE")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_7DFE")

    QueueWorkItem2(0x104, 2, lambda_7DFE)
    BeginChrThread(0x12, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x13, 3, 0, 23)
    Sleep(3000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 590, 4000, 39380, 180)
    SetScenarioFlags(0x14B, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_22_6B0C end

    def Function_23_7E84(): pass

    label("Function_23_7E84")

    OP_95(0xFE, -2330, 4000, 42280, 2000, 0x0)
    OP_95(0xFE, -3140, 4000, 36010, 2000, 0x0)
    Return()

    # Function_23_7E84 end

    def Function_24_7EAD(): pass

    label("Function_24_7EAD")

    Call(0, 25)
    Return()

    # Function_24_7EAD end

    def Function_25_7EB1(): pass

    label("Function_25_7EB1")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xF, 0xFF)
    OP_68(20680, 1100, 30630, 0)
    MoveCamera(304, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16850, 0)
    SetChrPos(0x101, 21500, 0, 30200, 0)
    SetChrPos(0x102, 20300, 0, 30200, 0)
    SetChrPos(0x103, 21800, 0, 29000, 0)
    SetChrPos(0x104, 19800, 0, 29500, 0)
    SetChrPos(0x109, 20300, 0, 28700, 0)
    SetChrPos(0x105, 19100, 0, 28700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(14850, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_0D()
    Sleep(1000)

    #C0320
    ChrTalk(
        0x101,
        "#6P#00005Fアリオスさん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0xB4, 0x1F4)

    #C0321
    ChrTalk(
        0xF,
        (
            "#11P#01400F……お前たちか。\x02\x03",

            "#01404Fフ……こんなところで会うとはな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_834C")

    #C0322
    ChrTalk(
        0x101,
        (
            "#6P#00000Fさっき、ミシェルさんが\x01",
            "アリオスさんを探してた\x01",
            "みたいですよ？\x02\x03",

            "#00003F確かアリオスさんは、\x01",
            "市長に呼ばれたって\x01",
            "聞いていましたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "#11P#01403F……まあな。\x02\x03",

            "#01400Fあの市長も律儀なものだ。\x01",
            "礼などいらんと言ったのだが、\x01",
            "どうしてもと言うのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#6P#00200Fでも、オルキスタワーを\x01",
            "猟兵団から守りきったのは\x01",
            "すごいと思いますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#6P#00302Fああ、クロスベルタイムズでも\x01",
            "取り上げられてたみてえだし、\x01",
            "実際大したモンだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xF,
        (
            "#11P#01404Fフフ、あの時はダドリーの援護も\x01",
            "あったからな……\x02\x03",

            "#01400F……まあ、その件も思ったより\x01",
            "早く終わってしまってな。\x02\x03",

            "ギルドに帰るついでに\x01",
            "こちらに寄っていたというわけだ。\x02\x03",

            "#01400F帰りが遅くなったことは\x01",
            "あとでミシェルに謝罪しておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x102,
        (
            "#6P#00100Fふふ、それがいいと思います。\x02\x03",

            "#00105F……えっと、今日はお墓参りに\x01",
            "来ていたみたいですけど……\x02\x03",

            "そのお墓は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84D3")

    label("loc_834C")


    #C0328
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそういえば……\x01",
            "オルキスタワー前での活躍、\x01",
            "クロスベルタイムズで読みましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#6P#00200F猟兵団を相手どって、\x01",
            "獅子奮迅の戦いぶりだったとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x104,
        "#6P#00302Fああ、大したモンだぜ。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xF,
        (
            "#11P#01404Fフフ、あの時はダドリーの援護も\x01",
            "あったからな……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        (
            "#6P#00100Fふふ、謙遜なさらないでください。\x02\x03",

            "#00105F……えっと、今日はお墓参りに\x01",
            "来ていたみたいですけど……\x02\x03",

            "そのお墓は……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84D3")

    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(1000)
    OP_64(0xF)

    #C0333
    ChrTalk(
        0xF,
        (
            "#11P#01403F……サヤ・マクレイン。\x02\x03",

            "#01408F５年前に事故で亡くなった……\x01",
            "シズクの母親だ。\x02",
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

    #C0334
    ChrTalk(
        0x103,
        "#6P#00200Fシズクちゃんのお母さん……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        (
            "#6P#00308F確か、その事故でシズクちゃんは\x01",
            "光を失っちまったんだったな……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)
    Sleep(1000)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0336
    ChrTalk(
        0x109,
        "#6P#10105F……アリオスさん？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x105,
        "#6P#10305Fどうしたんだい？\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xF,
        (
            "#11P#01404F……いや、何でもない。\x02\x03",

            "#01400F──用は済んだ。\x01",
            "俺はそろそろ立ち去らせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        "#6P#00000Fあ……お疲れ様です。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_873D():

        label("loc_873D")

        TurnDirection(0x101, 0xF, 500)
        Yield()
        Jump("loc_873D")

    QueueWorkItem2(0x101, 2, lambda_873D)

    def lambda_874F():

        label("loc_874F")

        TurnDirection(0x102, 0xF, 500)
        Yield()
        Jump("loc_874F")

    QueueWorkItem2(0x102, 2, lambda_874F)

    def lambda_8761():

        label("loc_8761")

        TurnDirection(0x109, 0xF, 500)
        Yield()
        Jump("loc_8761")

    QueueWorkItem2(0x109, 2, lambda_8761)

    def lambda_8773():

        label("loc_8773")

        TurnDirection(0x105, 0xF, 500)
        Yield()
        Jump("loc_8773")

    QueueWorkItem2(0x105, 2, lambda_8773)

    def lambda_8785():

        label("loc_8785")

        TurnDirection(0x103, 0xF, 500)
        Yield()
        Jump("loc_8785")

    QueueWorkItem2(0x103, 2, lambda_8785)

    def lambda_8797():

        label("loc_8797")

        TurnDirection(0x104, 0xF, 500)
        Yield()
        Jump("loc_8797")

    QueueWorkItem2(0x104, 2, lambda_8797)
    OP_68(20680, 700, 30630, 1000)

    def lambda_87BA():
        OP_95(0xFE, 23250, 0, 30200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_87BA)
    WaitChrThread(0xF, 1)
    OP_4B(0xF, 0xFF)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0340
    ChrTalk(
        0xF,
        (
            "#12P#01401F──これからクロスベルは、\x01",
            "かつてない事態に見舞われるだろう。\x02\x03",

            "#01403Fだが、どんな状況になっても、\x01",
            "どんな試練が訪れようとも……\x02\x03",

            "#01400F大切なものは決して見失わない事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#5P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x105,
        "#5P#10305F……？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_88DF():
        OP_95(0xFE, 23250, 0, 16970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_88DF)
    WaitChrThread(0xF, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    SetChrFlags(0xF, 0x80)

    #C0343
    ChrTalk(
        0x102,
        "#11P#00103F……行ってしまったわね。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x104,
        "#5P#00305F今のは、どういう意味だ？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        "#6P#10105Fさ、さあ……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x103,
        (
            "#6P#00203Fよく分かりませんが……\x01",
            "何かの忠告、でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#11P#00001F（……アリオスさん……？）\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Sleep(50)
    SetScenarioFlags(0x18C, 6)
    EventEnd(0x5)
    Return()

    # Function_25_7EB1 end

    def Function_26_8A8D(): pass

    label("Function_26_8A8D")

    EventBegin(0x0)
    OP_4B(0xE, 0xFF)
    Fade(500)
    OP_68(-22550, 1500, 23420, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -23390, 0, 22950, 0)
    SetChrPos(0x102, -21870, 0, 22900, 0)
    SetChrPos(0x103, -21870, 0, 21360, 0)
    SetChrPos(0x104, -23390, 0, 21360, 0)
    OP_0D()

    #C0348
    ChrTalk(
        0xE,
        "………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_8B6C")

    #C0349
    ChrTalk(
        0x101,
        (
            "#00000F（この人は……\x01",
            "  確かニールセンだったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B89")

    label("loc_8B6C")


    #C0350
    ChrTalk(
        0x101,
        "#00000F（この人は……）\x02",
    )

    CloseMessageWindow()

    label("loc_8B89")

    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0351
    ChrTalk(
        0xE,
        (
            "さてと……\x01",
            "そろそろ帰るとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0352
    ChrTalk(
        0xE,
        (
            "ふむ、あなたがたも\x01",
            "お墓参りですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "こんにちは。\x01",
            "私はこれで失礼しますね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C2E():
        OP_95(0xFE, -20540, 0, 24610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8C2E)
    Sleep(500)

    def lambda_8C4B():

        label("loc_8C4B")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C4B")

    QueueWorkItem2(0x101, 1, lambda_8C4B)
    Sleep(50)

    def lambda_8C60():

        label("loc_8C60")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C60")

    QueueWorkItem2(0x102, 1, lambda_8C60)
    Sleep(50)

    def lambda_8C75():

        label("loc_8C75")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C75")

    QueueWorkItem2(0x103, 1, lambda_8C75)
    Sleep(50)

    def lambda_8C8A():

        label("loc_8C8A")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C8A")

    QueueWorkItem2(0x104, 1, lambda_8C8A)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -15310, 0, 19380, 2000, 0x0)
    SetChrFlags(0xE, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_8CC9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CC9)
    Sleep(100)

    def lambda_8CD9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CD9)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_8DA8")

    #C0354
    ChrTalk(
        0x101,
        (
            "#00000Fニールセンさん……\x01",
            "兄貴の墓参りに来てくれたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        (
            "#00100F熱心に拝んでいたみたいだけど……\x01",
            "何か報告でもしていたのかしらね？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#00000Fああ、どうなんだろうな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E60")

    label("loc_8DA8")

    TurnDirection(0x102, 0x101, 500)

    #C0357
    ChrTalk(
        0x102,
        "#00100Fロイド、あの人は知り合いなの？\x02",
    )

    CloseMessageWindow()

    def lambda_8DDF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DDF)
    Sleep(50)

    def lambda_8DEF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DEF)
    Sleep(300)

    #C0358
    ChrTalk(
        0x101,
        (
            "#00000Fいや……心当たりはないな。\x02\x03",

            "（墓を参ってくれてるってことは\x01",
            "  兄貴の知り合いなのかな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E60")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -21160, 0, 21930, 135)
    SetScenarioFlags(0x19D, 4)
    EventEnd(0x5)
    Return()

    # Function_26_8A8D end

    def Function_27_8E86(): pass

    label("Function_27_8E86")

    EventBegin(0x0)
    OP_4B(0xE, 0xFF)
    Fade(500)
    OP_68(-22550, 1500, 23420, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19360, 0)
    SetChrPos(0x101, -23390, 0, 22950, 0)
    SetChrPos(0x102, -21870, 0, 22900, 0)
    SetChrPos(0x103, -21870, 0, 21360, 0)
    SetChrPos(0x104, -23390, 0, 21360, 0)
    OP_0D()

    #C0359
    ChrTalk(
        0xE,
        "#5P………………………\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x101,
        "#00005Fニールセンさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0361
    ChrTalk(
        0xE,
        "#5P……ふむ、ロイドさんですね。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0362
    ChrTalk(
        0x102,
        (
            "#00108F#6Pここは……\x01",
            "ロイドのお兄さんのお墓……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#00000F兄貴のために墓参りを\x01",
            "なさってくれていたんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xE,
        "#11Pええ……\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        (
            "#11Pそれに少々、ガイさんと\x01",
            "お話したいことがあったので。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0366
    ChrTalk(
        0x101,
        "#00005F兄貴と話、ですか……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(300)

    #C0367
    ChrTalk(
        0xE,
        (
            "#5P襲撃事件に国家独立宣言、\x01",
            "そして今朝の大統領演説……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xE,
        (
            "#5Pその感情は様々ですが――\x01",
            "人々は今、等しく\x01",
            "１つの方向を向いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xE,
        (
            "#5Pですがだからこそ……\x01",
            "私は逆に、ある『過去の闇』に\x01",
            "思いを巡らせることにしたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        (
            "#00008F『過去の闇』……\x01",
            "……それはもしかして……？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "#5Pええ、あなたの兄――\x01",
            "ガイ・バニングス捜査官の\x01",
            "殺害事件についてです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0372
    ChrTalk(
        0x102,
        "#00105F#6Pえ……？\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x103,
        "#00208F#6Pガイさんの……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        "#00301F#6Pそいつはまた……\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#00006Fあえて今……\x01",
            "いや逆に今だからこそ、ですか？\x02\x03",

            "#00001Fニールセンさんには、\x01",
            "何かが見えたんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xE,
        "#5Pふむ……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0377
    ChrTalk(
        0xE,
        "#11Pロイドさん、皆さんも。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "#11Pもしよければ、場所を変えて\x01",
            "私と事件の検証をしてみませんか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 28)
    Return()

    # Function_27_8E86 end

    def Function_28_93A2(): pass

    label("Function_28_93A2")

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
            "ニールセンの検証に付き合う\x01",      # 0
            "いったん考える\x01",                  # 1
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
        (0, "loc_941C"),
        (1, "loc_9562"),
        (SWITCH_DEFAULT, "loc_960C"),
    )


    label("loc_941C")


    #C0379
    ChrTalk(
        0x101,
        (
            "#00003F……………………………\x02\x03",

            "#00001F分かりました。\x01",
            "ぜひ付き合わせて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xE,
        "ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xE,
        (
            "ここでは何ですから\x01",
            "いったん街に戻るとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0382
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【ガイ・バニングス殺害事件の検証】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x95, 0x4, 0x2)
    StopSound(132, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("c0570", 0, 0, 0)
    IdleLoop()
    Jump("loc_960C")

    label("loc_9562")


    #C0383
    ChrTalk(
        0x101,
        (
            "#00003F……すみません。\x01",
            "少し考えてもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xE,
        "ええ、構いません。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xE,
        (
            "私はしばらくここにいるので、\x01",
            "よければ声を掛けて下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9604")
    OP_93(0xE, 0x0, 0x1F4)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)

    label("loc_9604")

    SetScenarioFlags(0x19B, 6)
    Jump("loc_960C")

    label("loc_960C")

    Return()

    # Function_28_93A2 end

    def Function_29_960D(): pass

    label("Function_29_960D")

    TalkBegin(0xE)

    #C0386
    ChrTalk(
        0xE,
        "……ロイドさんですね。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xE,
        (
            "もしよければ、場所を変えて\x01",
            "私と事件の検証をしてみませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Call(0, 28)
    TalkEnd(0xE)
    Return()

    # Function_29_960D end

    SaveToFile()

Try(main)
