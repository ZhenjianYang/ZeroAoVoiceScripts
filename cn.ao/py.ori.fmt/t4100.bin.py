from ScenarioHelper import *

def main():
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
        "缪夏夫人",               # 1
        "昆特老人",               # 2
        "莉丝修女",               # 3
        "亲卫队队员",             # 4
        "亲卫队队员",             # 5
        "克拉莉丝",               # 6
        "尼尔森",                 # 7
        "亚里欧斯",               # 8
        "盖伊墓前的花",           # 9
        "亚里欧斯家人墓前的花",   # 10
        "科洛蒂娅公主",           # 11
        "尤莉亚准校",             # 12
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
        "Function_5_18E2",         # 05, 5
        "Function_6_1BF8",         # 06, 6
        "Function_7_28C5",         # 07, 7
        "Function_8_3102",         # 08, 8
        "Function_9_35F0",         # 09, 9
        "Function_10_36E0",        # 0A, 10
        "Function_11_37AB",        # 0B, 11
        "Function_12_3BB9",        # 0C, 12
        "Function_13_3C1B",        # 0D, 13
        "Function_14_3CBE",        # 0E, 14
        "Function_15_3EC8",        # 0F, 15
        "Function_16_4549",        # 10, 16
        "Function_17_4944",        # 11, 17
        "Function_18_4FA4",        # 12, 18
        "Function_19_50D3",        # 13, 19
        "Function_20_53AB",        # 14, 20
        "Function_21_5676",        # 15, 21
        "Function_22_5CB0",        # 16, 22
        "Function_23_6D12",        # 17, 23
        "Function_24_6D3B",        # 18, 24
        "Function_25_6D3F",        # 19, 25
        "Function_26_7791",        # 1A, 26
        "Function_27_7B0E",        # 1B, 27
        "Function_28_7F80",        # 1C, 28
        "Function_29_8187",        # 1D, 29
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9C")

    #C0001
    ChrTalk(
        0xFE,
        "刚才有警察过来调查情况。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "没想到伊安律师惹出了那么大的事……\x01",
            "真让人难以置信啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00001F……嗯，我们也这么觉得。\x02\x03",

            "#00003F（……但这的确是事实。\x01",
            "  其中真意，恐怕只有亲自去问\x01",
            "  律师本人才能知道了吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DFD")

    label("loc_D9C")


    #C0004
    ChrTalk(
        0xFE,
        (
            "没想到伊安律师\x01",
            "会惹下那么大的事……\x01",
            "真是难以置信。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "到底是什么原因\x01",
            "促使他那样做呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFD")

    Jump("loc_18DE")

    label("loc_E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F1")

    #C0006
    ChrTalk(
        0xFE,
        (
            "那道壁障刚刚消失，\x01",
            "就发生了这么\x01",
            "惊人的大事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "自从独立宣言发表以来，\x01",
            "来扫墓的人也减少了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "在这种情况下，我能做的\x01",
            "也只有打扫墓场而已。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12EC")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0009
    ChrTalk(
        0x101,
        (
            "#00003F请问……\x02\x03",

            "#00008F这座墓碑到底\x01",
            "是谁的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0010
    ChrTalk(
        0xFE,
        "怎么，你不知道吗？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "……唔，告诉你们\x01",
            "应该没什么问题吧。\x01",
            "毕竟你们和『他』挺熟的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#00105F哎……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        "#00305F是我们的熟人吗？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "……嗯。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "长眠在这里的二人，\x01",
            "姓氏为『格里姆伍德』……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "也就是伊安·格里姆伍德\x01",
            "律师的家属。\x02",
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
        "#00205F伊安律师的……！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#00108F是、是真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "……千真万确。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "十五年前，他的夫人和孩子\x01",
            "都在一起不幸的事故中\x01",
            "失去了生命……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "每逢周末，他都会来这里扫墓，\x01",
            "缅怀自己的亲人。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "虽然墓碑久经风吹雨打，连上面的字迹都已模糊了……\x01",
            "但伊安律师似乎祈过什么愿。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "他以前曾拜托过我，要我在他实现愿望\x01",
            "之前不要修理墓碑，只要打扫打扫就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00106F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        "#00308F看来那位律师也有不少隐情啊……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "独立宣言发表之后，他似乎也很忙，\x01",
            "最近很少来这里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "不介意的话，你们以后\x01",
            "也可以来这里扫扫墓。\x01",
            "……夫人他们应该很寂寞吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00003F………………………………\x02\x03",

            "#00000F……好的，我明白了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 4)

    label("loc_12EC")

    Jump("loc_133E")

    label("loc_12F1")


    #C0029
    ChrTalk(
        0xFE,
        (
            "在这种情况下，我能做的\x01",
            "也只有打扫墓场而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "……你们要多加小心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_133E")

    Jump("loc_18DE")

    label("loc_1343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1351")
    Jump("loc_18DE")

    label("loc_1351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_14BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1444")

    #C0031
    ChrTalk(
        0xFE,
        "伊安律师刚才来教会了。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "他还给盖伊和\x01",
            "亚里欧斯的夫人扫了墓。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0033
    ChrTalk(
        0x101,
        "#00005F那个……发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "……不，\x01",
            "没什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "他最近好像相当忙碌，\x01",
            "要是扫扫墓能让他转换一下心情就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14B5")

    label("loc_1444")


    #C0036
    ChrTalk(
        0xFE,
        (
            "伊安律师刚才\x01",
            "给盖伊和\x01",
            "亚里欧斯的夫人扫了墓。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "他最近好像相当忙碌，\x01",
            "要是扫扫墓能让他转换一下心情就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B5")

    Jump("loc_18DE")

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_15BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1561")

    #C0038
    ChrTalk(
        0xFE,
        (
            "如市长所说，\x01",
            "克洛斯贝尔或许\x01",
            "正需要独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "当然，帝国和共和国\x01",
            "都会施加压力……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "但为了这代年轻人的未来，\x01",
            "我希望独立能取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15B5")

    label("loc_1561")


    #C0041
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔或许\x01",
            "正需要独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "为了这代年轻人的未来，\x01",
            "我希望独立能取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B5")

    Jump("loc_18DE")

    label("loc_15BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15C8")
    Jump("loc_18DE")

    label("loc_15C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15D6")
    Jump("loc_18DE")

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1689")

    #C0043
    ChrTalk(
        0xFE,
        (
            "经常来扫墓的那位夫人，\x01",
            "似乎在战争中\x01",
            "失去了丈夫。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "……在更早一些的年代，\x01",
            "我也在战争中失去了家人。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "或许是因为境遇相似吧，\x01",
            "所以挺担心她的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16F4")

    label("loc_1689")


    #C0046
    ChrTalk(
        0xFE,
        (
            "那位夫人，似乎在战争中\x01",
            "失去了丈夫。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "不过她的家人们\x01",
            "好像在外国过得很好。\x01",
            "……这也算是一些安慰吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F4")

    Jump("loc_18DE")

    label("loc_16F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1707")
    Jump("loc_18DE")

    label("loc_1707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1715")
    Jump("loc_18DE")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1730")
    Call(0, 5)
    Jump("loc_183B")

    label("loc_1730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CD")

    #C0048
    ChrTalk(
        0xFE,
        (
            "盖伊当年经常到那边的\x01",
            "小屋找我喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "我总是和他\x01",
            "举杯畅饮到天亮。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "呵呵，那家伙的酒量可不小啊，\x01",
            "我都数不清被他灌醉过多少次了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_183B")

    label("loc_17CD")


    #C0051
    ChrTalk(
        0xFE,
        (
            "盖伊那家伙的酒量可不小啊，\x01",
            "我都数不清被他灌醉过多少次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……从没喝赢过他一次，\x01",
            "是我心头一大憾事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183B")

    Jump("loc_18DE")

    label("loc_1840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_18DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185B")
    Call(0, 5)
    Jump("loc_18DE")

    label("loc_185B")


    #C0053
    ChrTalk(
        0xFE,
        (
            "我平时就在这里管理这片墓地。\x01",
            "只要你们方便，\x01",
            "什么时候过来都可以。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "到时候，我要是想起了什么，\x01",
            "可以给你们讲一些盖伊的往事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DE")

    TalkEnd(0xFE)
    Return()

    # Function_4_CA7 end

    def Function_5_18E2(): pass

    label("Function_5_18E2")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x9,
        (
            "哦，是罗伊德……\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "什么时候回来的？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000F嗯，最近才回来，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        "#10105F罗伊德警官，这位是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19CE")

    #C0059
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，是在以前的某次委托中\x01",
            "认识的老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CE")


    #C0060
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "是当年经常和我大哥\x01",
            "一起喝酒的昆特先生。\x02\x03",

            "#00004F昆特先生对我也很好。\x01",
            "在教团事件结束后，我们一起喝酒时，\x01",
            "他讲了很多过去的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        "当时确实聊得挺开心。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "不过你的酒量比盖伊差远了，\x01",
            "稍微有点无趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00012F哈哈……真抱歉。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，我们当时\x01",
            "也应邀而来了。\x02\x03",

            "#00109F缇欧还没有成年，所以当时\x01",
            "只能喝果汁，她好像还有些不满呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，原来如此。\x02\x03",

            "#10304F老人家，今后也请\x01",
            "多多关照我们哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "嗯，既然是罗伊德的同事，我自然非常欢迎。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "我平时就在这里管理这片墓地。\x01",
            "只要你们方便，什么时候过来都可以。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_5_18E2 end

    def Function_6_1BF8(): pass

    label("Function_6_1BF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC3")

    #C0068
    ChrTalk(
        0xFE,
        (
            "总算熬过了市区里有怪物的\x01",
            "那段恐怖时期，\x01",
            "终于又能来这里扫墓了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "虽然还是非常不安，\x01",
            "但一想到过世的老伴，\x01",
            "我就有了勇气……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "他一定在守护着我。\x01",
            "谢谢你，亲爱的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D21")

    label("loc_1CC3")


    #C0071
    ChrTalk(
        0xFE,
        (
            "一想到死去的老伴，\x01",
            "我就有了勇气……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "无论发生什么事，都没有问题的。\x01",
            "我绝不会认输……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D21")

    Jump("loc_28C1")

    label("loc_1D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D34")
    Jump("loc_28C1")

    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE1")

    #C0073
    ChrTalk(
        0xFE,
        (
            "今天早上，住在雷米菲利亚的\x01",
            "儿子和儿媳过来看望我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "其实他们不用管我，\x01",
            "待在安全的地方\x01",
            "就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "呵呵，不过……\x01",
            "我心里却很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E5F")

    label("loc_1DE1")


    #C0076
    ChrTalk(
        0xFE,
        (
            "今天早上，住在雷米菲利亚的\x01",
            "儿子和儿媳过来看望我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "虽然希望他们待在安全的地方……\x01",
            "但不知为什么，我心里却很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5F")

    Jump("loc_28C1")

    label("loc_1E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0E")

    #C0078
    ChrTalk(
        0xFE,
        (
            "前几天的袭击事件\x01",
            "真是太可怕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "让我回想起了三十年前，\x01",
            "夺去老伴性命的那场战争。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我原本再也不想\x01",
            "体会那种心情了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F7D")

    label("loc_1F0E")


    #C0081
    ChrTalk(
        0xFE,
        (
            "前几天的袭击事件，\x01",
            "让我回想起了三十年前，\x01",
            "夺去老伴性命的那场战争。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "我原本再也不想\x01",
            "体会那种心情了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7D")

    Jump("loc_28C1")

    label("loc_1F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1FD8")

    #C0083
    ChrTalk(
        0xFE,
        (
            "没想到会\x01",
            "发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "简直就像回到了战争年代。\x01",
            "太可怕了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C1")

    label("loc_1FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FE6")
    Jump("loc_28C1")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_209D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207A")

    #C0085
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00005F（这位夫人似乎正在诚心祈祷……）\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x105,
        (
            "#10300F（打扰人家可不好，\x01",
            "  还是走吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2098")

    label("loc_207A")


    #C0088
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2098")

    Jump("loc_28C1")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_219F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2142")

    #C0089
    ChrTalk(
        0xFE,
        (
            "听说在最近这段时间，\x01",
            "各地都出现了诡异的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "政府发言人也在呼吁，\x01",
            "建议市里的市民\x01",
            "不要轻易前往郊外。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "还好墓地\x01",
            "离市区很近。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_219A")

    label("loc_2142")


    #C0092
    ChrTalk(
        0xFE,
        (
            "虽然要离开市区，但来大圣堂\x01",
            "这一小段路应该没什么危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "还好墓地\x01",
            "离市区很近。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219A")

    Jump("loc_28C1")

    label("loc_219F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_222A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FC")

    #C0094
    ChrTalk(
        0xFE,
        "好美的晚霞啊……\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    #C0095
    ChrTalk(
        0xFE,
        (
            "呵呵，亲爱的，\x01",
            "我明天还会来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2225")

    label("loc_21FC")


    #C0096
    ChrTalk(
        0xFE,
        (
            "已经傍晚了……\x01",
            "我差不多也该回去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2225")

    Jump("loc_28C1")

    label("loc_222A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2312")

    #C0097
    ChrTalk(
        0xFE,
        (
            "最近我有个小小的兴趣，\x01",
            "就是在睡前\x01",
            "看书……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "前一阵子买新书的时候，\x01",
            "误买了两本一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "不介意的话，\x01",
            "你们要不要拿去一本？\x02",
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝７卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 6)
    Jump("loc_236C")

    label("loc_2312")


    #C0101
    ChrTalk(
        0xFE,
        (
            "最近在儿子和儿媳的劝说下，\x01",
            "我找到了自己的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "呵呵，人生果然\x01",
            "还是需要乐趣啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_236C")

    Jump("loc_28C1")

    label("loc_2371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_24BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244D")

    #C0103
    ChrTalk(
        0xFE,
        (
            "不久前，身在雷米菲利亚的\x01",
            "儿子和儿媳给我寄了信。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "邀请独自一人生活在\x01",
            "克洛斯贝尔的我\x01",
            "去雷米菲利亚定居。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "可是，我还是离不开\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "因为这里充满了\x01",
            "我和过世老伴的珍贵回忆。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24B6")

    label("loc_244D")


    #C0107
    ChrTalk(
        0xFE,
        (
            "虽然很高兴他们邀请我……\x01",
            "但我并不打算\x01",
            "离开克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "因为这里充满了\x01",
            "我和过世老伴的珍贵回忆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B6")

    Jump("loc_28C1")

    label("loc_24BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2538")

    #C0109
    ChrTalk(
        0xFE,
        (
            "科洛蒂娅公主……\x01",
            "看上去是个很温柔的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "我看过利贝尔的艾莉茜雅\x01",
            "女王的照片……\x01",
            "她们的气质确实很像呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C1")

    label("loc_2538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25AC")

    #C0111
    ChrTalk(
        0xFE,
        (
            "象征着克洛斯贝尔新时代的\x01",
            "建筑物——兰花塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "呵呵，如果可能，\x01",
            "真想和老伴一起观看揭幕式啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C1")

    label("loc_25AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_26CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267E")

    #C0113
    ChrTalk(
        0xFE,
        (
            "通商会议时，帝国和共和国的\x01",
            "首脑似乎也会前来。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "与战火不断的年代相比，\x01",
            "真让人切身感觉到时代的变迁。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "希望今后不要再使用武力，\x01",
            "而是通过交涉来解决问题，创造一个美好的时代。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26C9")

    label("loc_267E")


    #C0116
    ChrTalk(
        0xFE,
        (
            "希望今后不要再使用武力，\x01",
            "而是通过交涉来解决问题，创造一个美好的时代。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C9")

    Jump("loc_28C1")

    label("loc_26CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26DC")
    Jump("loc_28C1")

    label("loc_26DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_278F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274F")

    #C0117
    ChrTalk(
        0xFE,
        (
            "那位小姐……\x01",
            "是新来的修女吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "呵呵……和我在雷米菲利亚生活的\x01",
            "孙女年纪相仿呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_278A")

    label("loc_274F")


    #C0119
    ChrTalk(
        0xFE,
        (
            "我在雷米菲利亚有个孙女，\x01",
            "年纪大概和那位修女差不多……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278A")

    Jump("loc_28C1")

    label("loc_278F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_27D7")

    #C0120
    ChrTalk(
        0xFE,
        (
            "哎呀……\x01",
            "太阳已经下山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "我差不多\x01",
            "也该回家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C1")

    label("loc_27D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2875")

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
            "哎、哎呀，真是抱歉，\x01",
            "没注意到你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "我刚才正在向\x01",
            "老伴的墓碑祷告……\x01",
            "还请谅解哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_28C1")

    label("loc_2875")


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
            "#00103F（……打扰人家可不好，\x01",
            "  我们走吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C1")

    TalkEnd(0xFE)
    Return()

    # Function_6_1BF8 end

    def Function_7_28C5(): pass

    label("Function_7_28C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28D6")
    Jump("loc_30FE")

    label("loc_28D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28E4")
    Jump("loc_30FE")

    label("loc_28E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEE")

    #C0127
    ChrTalk(
        0xA,
        (
            "#04401F那些猎兵似乎\x01",
            "驻扎在了山道一带。\x02\x03",

            "#04403F……身为『星杯骑士』，\x01",
            "我不能过于张扬地\x01",
            "行动。\x02\x03",

            "#04408F在如此重要的时刻，\x01",
            "我却不能帮上忙，\x01",
            "实在是于心不安……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_29CF")

    #C0128
    ChrTalk(
        0x103,
        (
            "#00200F说起来，莉丝小姐\x01",
            "相当厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CF")


    #C0129
    ChrTalk(
        0x102,
        (
            "#00108F的确，要是能借助『星杯骑士』\x01",
            "的力量，我们的把握就大多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x105,
        (
            "#10301F毕竟山道上的\x01",
            "对手恐怕相当难缠。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#00003F为了在紧急时刻能够\x01",
            "及时出动，莉丝小姐还是\x01",
            "在这里等待吧。\x02\x03",

            "#00001F至于玛因兹的事情，\x01",
            "我们和警备队会想办法的。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "#04401F……明白了，\x01",
            "请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B61")

    label("loc_2AEE")


    #C0133
    ChrTalk(
        0xA,
        (
            "#04401F那些猎兵似乎\x01",
            "驻扎在了山道一带。\x02\x03",

            "#04403F由于『星杯骑士』的立场特殊，\x01",
            "我无法帮上忙……\x01",
            "请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B61")

    Jump("loc_30FE")

    label("loc_2B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B74")
    Jump("loc_30FE")

    label("loc_2B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2C20")

    #C0134
    ChrTalk(
        0xA,
        (
            "#04400F关于『灵智之草』，\x01",
            "和骑士团取得联络之后，\x01",
            "我也会开始调查。\x02\x03",

            "#04403F虽然不知凭我一人之力\x01",
            "能调查到什么程度……\x01",
            "不过，一有发现，我就会报告给各位的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30FE")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E56")

    #C0135
    ChrTalk(
        0xA,
        "#04400F各位……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00000F莉丝小姐……\x01",
            "你在这里啊。\x02\x03",

            "#00004F感谢你昨天给我们\x01",
            "提供了贵重的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#04404F哪里，能帮上忙就好。\x02\x03",

            "#04400F各位接下来要去哪里？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#00100F嗯，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉说明了要去人偶工房的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0140
    ChrTalk(
        0xA,
        (
            "#04405F罗赞贝尔克工房……\x02\x03",

            "#04403F我记得那里\x01",
            "与『结社』有关呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，不愧是\x01",
            "星杯骑士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xA,
        (
            "#04403F……据说约鲁古·罗赞贝尔克\x01",
            "是个明事理的人物……\x02\x03",

            "#04401F但罗赞贝尔克工房与『结社』\x01",
            "存在关联也是事实。\x02\x03",

            "各位如果打算去见他，\x01",
            "还需多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00004F嗯……我们会的，\x01",
            "谢谢你的忠告。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 2)
    Jump("loc_2EA9")

    label("loc_2E56")


    #C0144
    ChrTalk(
        0xA,
        (
            "#04400F要去人偶工房的话，\x01",
            "应该事先做好万全准备。\x02\x03",

            "#04403F……请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA9")

    Jump("loc_30FE")

    label("loc_2EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_2EBC")
    Jump("loc_30FE")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2ECA")
    Jump("loc_30FE")

    label("loc_2ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ED8")
    Jump("loc_30FE")

    label("loc_2ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EE6")
    Jump("loc_30FE")

    label("loc_2EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EF4")
    Jump("loc_30FE")

    label("loc_2EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F02")
    Jump("loc_30FE")

    label("loc_2F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F10")
    Jump("loc_30FE")

    label("loc_2F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_30E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2F")
    TalkEnd(0xFE)
    Call(0, 8)
    Return()

    label("loc_2F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3090")

    #C0145
    ChrTalk(
        0xA,
        (
            "#13800F祭拜完慰灵碑之后，\x01",
            "就要去向前辈们\x01",
            "请教工作内容了。\x02\x03",

            "#13804F刚刚到任，\x01",
            "大概会有许多事情要做。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#00105F啊……是不是\x01",
            "打扰你了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "#13800F不，没有的事……\x01",
            "很高兴能见到琪雅。\x02\x03",

            "#13803F……话说回来，\x01",
            "我的肚子\x01",
            "有点饿了。\x02\x03",

            "#13802F真想早点回宿舍，\x01",
            "吃些从面包店\x01",
            "买来的面包呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#00109F（呵呵，还是和以前\x01",
            "  一样贪吃呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30E2")

    label("loc_3090")


    #C0149
    ChrTalk(
        0xA,
        (
            "#13800F我会暂时寄宿在\x01",
            "克洛斯贝尔\x01",
            "大圣堂。\x02\x03",

            "如果有什么事，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E2")

    Jump("loc_30FE")

    label("loc_30E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_30F5")
    Jump("loc_30FE")

    label("loc_30F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_30FE")

    label("loc_30FE")

    TalkEnd(0xFE)
    Return()

    # Function_7_28C5 end

    def Function_8_3102(): pass

    label("Function_8_3102")

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
            "#11P#13800F啊，各位……\x01",
            "刚才多谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#6P#00000F莉丝小姐，已经办好\x01",
            "就任手续了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        "#11P#13804F嗯，顺利办好了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 500)

    #C0153
    ChrTalk(
        0xA,
        (
            "#11P#13800F……这孩子就是你们\x01",
            "之前所说的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#00100F嗯，她是小琪雅。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x153,
        (
            "#12P#01105F大姐姐，\x01",
            "你是新来的修女吗～？\x02\x03",

            "#01109F嘿嘿，你好！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0156
    ChrTalk(
        0xA,
        "#11P#13802F……真可爱……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，是吧？\x01",
            "而且是个\x01",
            "很乖的孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#6P#00009F她经常\x01",
            "帮忙做饭……\x01",
            "帮了我们很多忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#12P#10306F哎呀呀，在这种场合\x01",
            "都不忘显露爱子如命的本性啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        (
            "#6P#10109F啊哈哈……\x01",
            "心情倒是可以理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x153,
        "#12P#01111F哎～？\x02",
    )

    CloseMessageWindow()

    def lambda_340F():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_340F)
    Sleep(50)

    def lambda_341F():
        TurnDirection(0x105, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_341F)
    Sleep(50)

    def lambda_342F():
        TurnDirection(0x102, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_342F)
    Sleep(50)

    def lambda_343F():
        TurnDirection(0x109, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_343F)
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
            "#11P#13803F（……原来如此，这孩子\x01",
            "　就是那教团的……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34FB():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_34FB)
    Sleep(50)

    def lambda_350B():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_350B)
    Sleep(50)

    def lambda_351B():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_351B)
    Sleep(50)

    def lambda_352B():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_352B)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0163
    ChrTalk(
        0x102,
        (
            "#00105F嗯？莉丝小姐，\x01",
            "你怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "#11P#13803F……不，没什么。\x02\x03",

            "#13802F琪雅，\x01",
            "今后请多多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x153,
        "#12P#01109F嗯，请多关照！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x135, 5)
    SetChrPos(0x0, 0, 4000, 40000, 180)
    EventEnd(0x5)
    Return()

    # Function_8_3102 end

    def Function_9_35F0(): pass

    label("Function_9_35F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369B")

    #C0166
    ChrTalk(
        0xFE,
        (
            "哦，你们是……\x01",
            "昨晚到访埃尔赛尤的\x01",
            "特别任务支援科的各位吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "科洛蒂娅公主殿下和尤莉亚准校\x01",
            "就在这前面。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "如果想过去看看的话，\x01",
            "请随意通行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36DC")

    label("loc_369B")


    #C0169
    ChrTalk(
        0xFE,
        (
            "科洛蒂娅公主殿下和尤莉亚准校\x01",
            "就在这前面。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        "请随意通行。\x02",
    )

    CloseMessageWindow()

    label("loc_36DC")

    TalkEnd(0xFE)
    Return()

    # Function_9_35F0 end

    def Function_10_36E0(): pass

    label("Function_10_36E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3752")

    #C0171
    ChrTalk(
        0xFE,
        (
            "按理说，应该\x01",
            "不会有人在墓地\x01",
            "引起骚动……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "但凡事就怕万一，\x01",
            "还是要认真做好警戒工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37A7")

    label("loc_3752")


    #C0173
    ChrTalk(
        0xFE,
        (
            "殿下只带了最低限度的警备人员……\x01",
            "我们真是责任重大啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "必须要认真警戒才行。\x02",
    )

    CloseMessageWindow()

    label("loc_37A7")

    TalkEnd(0xFE)
    Return()

    # Function_10_36E0 end

    def Function_11_37AB(): pass

    label("Function_11_37AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B69")

    #C0175
    ChrTalk(
        0xFE,
        (
            "……哎呀，是你们。\x01",
            "在这种地方碰面，真是巧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DD")

    #C0176
    ChrTalk(
        0x101,
        (
            "#00003F您好像在扫墓。\x01",
            "……真是失礼了。\x02\x03",

            "#00000F……莫非……\x01",
            "长眠在这里的人是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x109,
        (
            "#10108F奥兹玛·希卡二尉……\x01",
            "是我和芙兰\x01",
            "在十年前去世的父亲。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B1")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_38B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38D4")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_38D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F7")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_38F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3917")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_3917")

    Sleep(1000)

    #C0178
    ChrTalk(
        0x102,
        "#00105F诺艾尔的父亲……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        (
            "#00303F我听说过传闻……\x01",
            "据说他是位非常优秀的士官。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x105,
        "#10305F哦，是这样啊？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "嗯，他是个正义感很强，\x01",
            "做事非常严格的人……\x01",
            "在执行任务的一起事故中殉职。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A66")

    label("loc_39DD")


    #C0182
    ChrTalk(
        0x101,
        (
            "#00003F您好像在扫墓啊。\x01",
            "……真是失礼了。\x02\x03",

            "#00008F……我记得\x01",
            "长眠在这里的是……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x109,
        (
            "#10108F……嗯，\x01",
            "是我和芙兰\x01",
            "在十年前去世的父亲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A66")


    #C0184
    ChrTalk(
        0xFE,
        (
            "……既然他选择了警备队员这份工作，\x01",
            "我便早有心理准备……\x01",
            "但当时真是很难承受呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "呵呵，不要露出\x01",
            "这种表情嘛，\x01",
            "都已经是过去的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "……总之，你们一定要\x01",
            "珍惜生命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "假如你们遭遇不测，\x01",
            "会让许多人伤心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x109,
        "#10104F……嗯，我知道。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 3)
    Jump("loc_3BB5")

    label("loc_3B69")


    #C0189
    ChrTalk(
        0xFE,
        (
            "……你们一定要\x01",
            "珍惜生命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "假如你们遭遇不测，\x01",
            "会让许多人伤心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB5")

    TalkEnd(0xFE)
    Return()

    # Function_11_37AB end

    def Function_12_3BB9(): pass

    label("Function_12_3BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C14")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BE2")
    Call(0, 26)
    Return()

    label("loc_3BE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3BF9")
    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Jump("loc_3C0F")

    label("loc_3BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_3C0B")
    Call(0, 29)
    Return()

    label("loc_3C0B")

    Call(0, 27)
    Return()

    label("loc_3C0F")

    Jump("loc_3C1A")

    label("loc_3C14")

    TalkBegin(0xFE)
    TalkEnd(0xFE)

    label("loc_3C1A")

    Return()

    # Function_12_3BB9 end

    def Function_13_3C1B(): pass

    label("Function_13_3C1B")

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
            "生于钟下的羔羊们\x01",
            "　　请安息吧\x02",
        )
    )

    CloseMessageWindow()

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "纯白云间洒下的金色阳光\x01",
            " 将成为连接苍穹的大道\x01",
            "引导汝之灵魂至女神座前\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_3C1B end

    def Function_14_3CBE(): pass

    label("Function_14_3CBE")

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
            " 　　　 　奥兹玛·希卡\x01",
            "　　　　　　长眠于此\x01",
            "———————————————\x01",
            "  Ｓ１１５７　～　Ｓ１１９４　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC4")

    #C0194
    ChrTalk(
        0x101,
        (
            "#00005F『希卡』……\x01",
            "莫非是？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x109,
        (
            "#10108F奥兹玛·希卡二尉……\x01",
            "是我和芙兰\x01",
            "在十年前去世的父亲。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        "#00105F诺艾尔的父亲……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x105,
        "#10305F唔，这还是头一次听说……\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x109,
        (
            "#10109F啊哈哈，因为\x01",
            "我一般不会主动\x01",
            "提起这些事情啦。\x02\x03",

            "#10104F……各位，我们走吧。\x01",
            "如果一直在这里驻足不前，\x01",
            "一定会被父亲训斥的。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#00000F……哈哈，是吗，\x01",
            "那我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 2)

    label("loc_3EC4")

    TalkEnd(0xFF)
    Return()

    # Function_14_3CBE end

    def Function_15_3EC8(): pass

    label("Function_15_3EC8")

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
            " 　　　 　盖伊·班宁斯\x01",
            "　　　　　　长眠于此\x01",
            "———————————————\x01",
            "　Ｓ１１７６　～　Ｓ１２０１　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_402D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4029")

    #C0201
    ChrTalk(
        0x153,
        (
            "#01105F（……这座墓是……）\x02\x03",

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
            "琪雅静静地合上双手。\x07\x00\x02",
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
        "#00002F哈哈……谢谢你啦。\x02",
    )

    CloseMessageWindow()

    label("loc_4029")

    TalkEnd(0xFF)
    Return()

    label("loc_402D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_4082")

    #C0204
    ChrTalk(
        0x101,
        (
            "#00000F这花束……\x01",
            "大概是亚里欧斯先生\x01",
            "供奉的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40BD")

    label("loc_4082")


    #C0205
    ChrTalk(
        0x101,
        (
            "#00005F咦……\x01",
            "有人供奉了花束。\x02\x03",

            "#00003F到底是谁……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40BD")

    SetScenarioFlags(0x0, 6)
    Jump("loc_40FA")

    label("loc_40C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40E4")
    TalkEnd(0xFF)
    Call(0, 17)
    Return()

    label("loc_40E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40FA")
    TalkEnd(0xFF)
    Call(0, 16)
    Return()

    label("loc_40FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_449B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4439")

    #C0206
    ChrTalk(
        0x101,
        "#00008F…………………………\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        "#00105F罗伊德……？\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，没什么……\x01",
            "听亚里欧斯先生讲述了\x01",
            "大哥临终前的事……\x02\x03",

            "#00004F他直到最后的最后，\x01",
            "都还在担心着\x01",
            "我和塞茜尔姐姐……\x02\x03",

            "而且对亚里欧斯先生\x01",
            "和伊安律师\x01",
            "没有一丝怨恨……\x02\x03",

            "#00000F真是的，他到底要\x01",
            "滥好人到什么程度啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        "#00200F罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00304F……哈哈，说起滥好人的性格……\x02\x03",

            "#00302F你不是已经\x01",
            "完全继承了下来嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42C1")

    #C0211
    ChrTalk(
        0x10A,
        "#00604F呵……的确呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4318")

    label("loc_42C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42EF")

    #C0212
    ChrTalk(
        0x109,
        "#10102F呵呵，的确。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4318")

    label("loc_42EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4318")

    #C0213
    ChrTalk(
        0x105,
        "#10402F哈哈，的确。\x02",
    )

    CloseMessageWindow()

    label("loc_4318")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_434A")

    #C0214
    ChrTalk(
        0x106,
        "#10702F嘻嘻……说的对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43A3")

    label("loc_434A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4376")

    #C0215
    ChrTalk(
        0x105,
        "#10404F说的对啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43A3")

    label("loc_4376")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43A3")

    #C0216
    ChrTalk(
        0x109,
        "#10102F呵呵，说的对呢。\x02",
    )

    CloseMessageWindow()

    label("loc_43A3")


    #C0217
    ChrTalk(
        0x101,
        (
            "#00012F你、你们……\x01",
            "……哈哈，也罢。\x02\x03",

            "#00000F总而言之……\x01",
            "接下来的目标，就只有救出琪雅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00100F嗯，直到最后一刻，\x01",
            "都不能松懈啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 5)
    Jump("loc_4496")

    label("loc_4439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4496")

    #C0219
    ChrTalk(
        0x101,
        (
            "#00000F……接下来的目标，就只有救出琪雅了。\x02\x03",

            "#00004F大哥……请守护我们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4496")

    Jump("loc_4545")

    label("loc_449B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B5")
    TalkEnd(0xFF)
    Call(0, 21)
    Return()

    label("loc_44B5")

    Jump("loc_4545")

    label("loc_44BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4545")

    #C0220
    ChrTalk(
        0x101,
        (
            "#00000F（大哥……\x01",
            "  我回到克洛斯贝尔市了。）\x02\x03",

            "#00004F（接下来，无论如何\x01",
            "  都要夺回琪雅。\x01",
            "  请守护我们吧……！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4545")

    TalkEnd(0xFF)
    Return()

    # Function_15_3EC8 end

    def Function_16_4549(): pass

    label("Function_16_4549")

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
        "#6P#00108F这座墓是……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00003F盖伊·班宁斯……\x01",
            "是我三年前殉职的大哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x109,
        (
            "#12P#10100F听说他是警察局中\x01",
            "数一数二的\x01",
            "优秀搜查官呢。\x02\x03",

            "#10104F即使在警备队，知道这个\x01",
            "名字的人也不在少数。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x105,
        "#6P#10305F哦？是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00000F他原本是赛尔盖科长的部下，\x01",
            "还和亚里欧斯先生\x01",
            "做过搭档……\x02\x03",

            "#00003F赛尔盖班由于各种原因而解散之后，\x01",
            "大哥便被调至搜查一科。据说他和\x01",
            "达德利警官互相争锋，势均力敌。\x02\x03",

            "#00009F无论什么事情，\x01",
            "他都喜欢插手介入，\x01",
            "所以人脉相当广。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        "#6P#00104F传闻听得越多，越感觉他是个厉害人物啊……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00003F凭借非同寻常的行动力\x01",
            "来对抗克洛斯贝尔各种\x01",
            "『壁障』的搜查官……\x02\x03",

            "#00008F……他竟然会殉职，\x01",
            "真是令人无法相信。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        (
            "#12P#10101F结果，那个教团\x01",
            "也不是杀害你哥哥的\x01",
            "真凶吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#00008F嗯……\x01",
            "真相至今还是个谜。\x02\x03",

            "#00003F（不过……总有一天，\x01",
            "  我会亲手找出真相。）\x02\x03",

            "#00000F（也许还需要\x01",
            "  再花一些时间……\x01",
            "  等着我吧，大哥。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x136, 0)
    EventEnd(0x5)
    Return()

    # Function_16_4549 end

    def Function_17_4944(): pass

    label("Function_17_4944")

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
            "#10305F#12P……说起来……\x02\x03",

            "#10303F虽然知道你的哥哥\x01",
            "长眠于此……\x02\x03",

            "#10300F但你父母呢？\x02",
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
        "#00305F#6P说起来……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#00108F#6P……记得令尊和令堂\x01",
            "也已经去世了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    #C0235
    ChrTalk(
        0x101,
        (
            "#00004F#11P嗯，十五年前去世的。\x02\x03",

            "#00008F……说实话，那时我还小，\x01",
            "所以几乎不记得了。\x02\x03",

            "#00000F他们搭乘了当时刚刚投入运行的\x01",
            "导力飞船，不幸遭遇事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        "#00106F#6P飞船事故……是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x109,
        (
            "#10108F#6P飞船在当时刚刚投入实用，\x01",
            "还不稳定吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#00006F#11P嗯，结果坠落到山里，\x01",
            "连遗体都没能找到……\x02\x03",

            "#00008F大哥当时真是吃了不少苦。\x02\x03",

            "#00002F而且还要抚养\x01",
            "年幼无知的弟弟……\x02\x03",

            "#00012F……哈哈……\x01",
            "真是亏欠大哥一辈子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        "#00108F#6P罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#00304F#6P不过，我认为你大哥\x01",
            "并没有把你视为负担。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        (
            "#00204F#12P是呀……\x02\x03",

            "#00214F每当说起罗伊德前辈的时候，\x01",
            "他都会流露出怜爱万分的口吻。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x105,
        (
            "#10302F#12P哈哈，可以理解他的心情。\x02\x03",

            "#10309F三岁的罗伊德吗……\x01",
            "一定很可爱吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        "#00102F#6P的、的确，想象一下的话……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x109,
        (
            "#10112F#6P……一定可爱得\x01",
            "让人忍不住想抱抱吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        "#00309F#6P哦哦，好像很容易想象嘛！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_4F1D")

    #C0246
    ChrTalk(
        0x101,
        (
            "#00011F#11P别、别取笑我啦。\x02\x03",

            "#00004F抱歉，延误了一些时间，\x01",
            "我们得赶快去找莉丝小姐了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4F75")

    label("loc_4F1D")


    #C0247
    ChrTalk(
        0x101,
        (
            "#00011F#11P别、别取笑我啦。\x02\x03",

            "#00004F抱歉，延误了一些时间，\x01",
            "我们赶快去大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F75")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x17C, 6)
    EventEnd(0x5)
    Return()

    # Function_17_4944 end

    def Function_18_4FA4(): pass

    label("Function_18_4FA4")

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
            "　　　 　纱绫·马克莱因\x01",
            "　　　　　　长眠于此\x01",
            "———————————————\x01",
            "　Ｓ１１７５　～　Ｓ１１９９　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50B8")

    #C0249
    ChrTalk(
        0x153,
        (
            "#01108F这座墓是……\x02\x03",

            "#01100F罗伊德，我们祭拜一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#00000F……嗯，说的对。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_50B8")

    Jump("loc_50CF")

    label("loc_50BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50CF")
    Call(0, 19)

    label("loc_50CF")

    TalkEnd(0xFF)
    Return()

    # Function_18_4FA4 end

    def Function_19_50D3(): pass

    label("Function_19_50D3")

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
            "#12P#10105F这座墓碑上刻的名字……\x01",
            "好像曾在哪里听过……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00008F虽然没有问过\x01",
            "他本人……\x02\x03",

            "#00003F但多半是『风之剑圣』\x01",
            "亚里欧斯·马克莱因的妻子。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#00108F记得她是被卷入一场事故\x01",
            "而去世的……\x02\x03",

            "#00103F当时在一起的小滴\x01",
            "虽然保住一命，\x01",
            "却因此而失去了光明……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00003F嗯，自那之后，亚里欧斯先生\x01",
            "就辞去了警察的工作，转职当了游击士。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x105,
        "#6P#10300F嗯，原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x109,
        (
            "#12P#10108F真是让人\x01",
            "心痛啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        (
            "#00000F……但也不是完全没有希望。\x02\x03",

            "#00004F小滴的眼睛\x01",
            "似乎还有\x01",
            "重见光明的可能性。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#00100F是啊……\x01",
            "最近要是有时间，\x01",
            "最好去探望她一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 20740, 0, 31990, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x135, 7)
    EventEnd(0x5)
    Return()

    # Function_19_50D3 end

    def Function_20_53AB(): pass

    label("Function_20_53AB")

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
            "　　　　　……眠……此\x01",
            "———————————————……\x01",
            "　　Ｓ１………　～　Ｓ１…８…　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556C")

    #C0260
    ChrTalk(
        0x101,
        (
            "#00001F好破旧的墓碑啊，\x01",
            "上面的字迹已经风化得模糊不清了……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x105,
        (
            "#10300F如此看来，\x01",
            "恐怕无法解读了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x109,
        (
            "#10106F解读……\x01",
            "这又不是暗号游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#00100F虽然不知是哪位的墓……\x01",
            "但似乎有人照料。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#00000F姑且祭拜一下吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 6)

    label("loc_556C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_END)), "loc_5672")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_55E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E4")

    #C0265
    ChrTalk(
        0x101,
        (
            "#00001F（这座墓原来是伊安律师的\x01",
            "  妻子和孩子的……）\x02\x03",

            "#00003F（……我们还是走吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_55E4")

    Jump("loc_5672")

    label("loc_55E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5672")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5672")

    #C0266
    ChrTalk(
        0x101,
        (
            "#00001F（这座墓原来是伊安律师的\x01",
            "  妻子和孩子的……）\x02\x03",

            "#00008F（伊安律师……\x01",
            "  从来都没有透露过\x01",
            "  这件事……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_5672")

    TalkEnd(0xFF)
    Return()

    # Function_20_53AB end

    def Function_21_5676(): pass

    label("Function_21_5676")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57B1")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_57B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D1")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_57D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57F1")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_57F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5811")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_5811")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5831")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_5831")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5851")
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_5851")

    Sleep(1000)

    #C0268
    ChrTalk(
        0x102,
        (
            "#12P#00108F你哥哥的旋棍……\x01",
            "伤痕累累，看着就令人痛心。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#12P#00303F大概是和亚里欧斯那大叔\x01",
            "对决时留下的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#00006F嗯……\x02\x03",

            "#00000F……不过，仔细观察就能发现，\x01",
            "除此之外还有许多细小伤痕。\x02\x03",

            "而且还能看出经过多次\x01",
            "修理的痕迹。\x02\x03",

            "#00004F大哥无论面对任何『壁障』都不会放弃，\x01",
            "始终都在勇往直前地探求真相……\x02\x03",

            "这旋棍的形态，\x01",
            "就是大哥生存方式的体现吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59F0")

    #C0271
    ChrTalk(
        0x10A,
        "#6P#00604F……或许正如你所说。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A5D")

    label("loc_59F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A29")

    #C0272
    ChrTalk(
        0x109,
        "#6P#10100F……或许正是如此呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A5D")

    label("loc_5A29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A5D")

    #C0273
    ChrTalk(
        0x105,
        "#6P#10400F……或许正是这样呢。\x02",
    )

    CloseMessageWindow()

    label("loc_5A5D")

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
            "#00008F这次的事件，还有大哥的事件……\x02\x03",

            "#00001F为了解明其中的真相，\x01",
            "我们必须要跨越亚里欧斯先生……\x01",
            "以及伊安律师这两道障碍。\x02\x03",

            "#00004F这对旋棍，我就暂时借用了。\x01",
            "……大哥，请借给我们力量吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B83")

    #C0275
    ChrTalk(
        0x106,
        "#6P#10710F罗伊德警官……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BE0")

    label("loc_5B83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BB2")

    #C0276
    ChrTalk(
        0x105,
        "#6P#10400F罗伊德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BE0")

    label("loc_5BB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BE0")

    #C0277
    ChrTalk(
        0x109,
        "#6P#10100F罗伊德警官……\x02",
    )

    CloseMessageWindow()

    label("loc_5BE0")


    #C0278
    ChrTalk(
        0x103,
        "#6P#00204F我们自然也会帮忙。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#12P#00309F哈哈，是啊。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#12P#00102F为了夺回琪雅……\x01",
            "大家齐心协力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(150)

    #C0281
    ChrTalk(
        0x101,
        (
            "#5P#00000F嗯……\x01",
            "拜托大家了！\x02",
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

    # Function_21_5676 end

    def Function_22_5CB0(): pass

    label("Function_22_5CB0")

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
            "#5P#07000F对了，尤莉亚……\x02\x03",

            "听说『她』在不久前\x01",
            "来这里的大圣堂赴任了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    #C0283
    ChrTalk(
        0x13,
        (
            "#12P#07100F嗯，但据其他修女说，\x01",
            "她今天出去工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x12,
        (
            "#5P#07003F这样啊……\x02\x03",

            "#07008F她在那时有恩于我们，\x01",
            "如果有机会，本想去打个招呼的。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#12P#N#00005F科洛蒂娅殿下……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0286
    ChrTalk(
        0x109,
        "#12P#N#10105F还有尤莉亚准校！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5F0B():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_5F0B)
    Sleep(50)

    def lambda_5F1B():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_5F1B)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)

    #C0287
    ChrTalk(
        0x12,
        "#11P#07002F啊……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x13,
        "#12P#07102F是他们。\x02",
    )

    CloseMessageWindow()
    OP_68(860, 5100, 39660, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14870, 3000)

    def lambda_5F91():
        OP_95(0xFE, 380, 4000, 38790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F91)

    def lambda_5FAB():
        OP_95(0xFE, 2620, 4000, 38580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FAB)

    def lambda_5FC5():
        OP_95(0xFE, -820, 4000, 37680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FC5)

    def lambda_5FDF():
        OP_95(0xFE, 2009, 4000, 36940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FDF)

    def lambda_5FF9():
        OP_95(0xFE, 560, 4000, 36330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FF9)

    def lambda_6013():
        OP_95(0xFE, -1060, 4000, 36090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6013)
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
            "#11P#07002F各位……\x01",
            "呵呵，我们又见面了。\x02\x03",

            "#07009F我想你们也该来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x102,
        (
            "#12P#00105F哎，您知道\x01",
            "我们要来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x13,
        (
            "#11P#07102F基库一直在上空盘旋，\x01",
            "帮忙监视周围呢。\x02\x03",

            "它刚才告诉我们，\x01",
            "说你们来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#6P#00000F是昨天的白隼……\x01",
            "哈哈，真是优秀啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x12,
        (
            "#11P#07004F呵呵，基库在王室亲卫队\x01",
            "负责传送情报的任务。\x02\x03",

            "#07000F嗯，请问……\x01",
            "各位来这里，有何要事吗？\x02\x03",

            "#07005F啊，今天还有新人……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        (
            "#6P#00200F您好……我是昨晚\x01",
            "回归特别任务支援科的\x01",
            "缇欧·普拉托。\x02\x03",

            "#00204F能与您会面，真是不胜荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x12,
        "#11P#07009F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        (
            "#6P#00300F我们只是\x01",
            "顺便来这里\x01",
            "转转而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，没想到\x01",
            "这么快就与公主殿下\x01",
            "和准校重逢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#6P#00000F殿下，你们是来这里祭拜的？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x12,
        (
            "#11P#07000F嗯……\x02\x03",

            "#07003F迄今为止，无数丧生于\x01",
            "克洛斯贝尔的人都长眠于此。\x02\x03",

            "所以，我无论如何\x01",
            "也想在今天的正式会议\x01",
            "之前来看一下。\x02\x03",

            "#07008F这也为了从真正意义上理解\x01",
            "『克洛斯贝尔问题』……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#6P#00200F克洛斯贝尔问题……\x02\x03",

            "#00204F就是帝国与共和国为了争夺\x01",
            "克洛斯贝尔的归属权而产生的一系列\x01",
            "问题的总称吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#12P#00100F嗯，但克洛斯贝尔的居民\x01",
            "很少会用到这个词。\x02\x03",

            "#00103F由于这个问题的存在，\x01",
            "国际形势曾紧张到\x01",
            "战争一触即发的程度。\x02\x03",

            "#00108F两年前，三个国家在利贝尔\x01",
            "签署了《互不侵犯条约》，但形势\x01",
            "只是在表面上稳定了下来，实际上……\x02",
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
            "#12P#00106F对、对不起！\x01",
            "我真是太失礼了……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x12,
        (
            "#11P#07003F哪里……\x01",
            "艾莉小姐\x01",
            "所言极是。\x02\x03",

            "#07000F我的祖母……艾莉茜雅女王当初\x01",
            "提议签署《互不侵犯条约》，本意是为了\x01",
            "阻止两大国动用武力。\x02\x03",

            "通过这项条约，当时的克洛斯贝尔\x01",
            "从极度的紧张状态中得到了解放……\x02\x03",

            "#07003F但另一方面，两国所施加的\x01",
            "无形压力越来越大，\x01",
            "克洛斯贝尔的立场如今依然岌岌可危……\x02\x03",

            "#07001F从这个意义上来说，《互不侵犯条约》\x01",
            "的确没有从根本上解决\x01",
            "克洛斯贝尔问题。\x02",
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
            "#6P#10101F但、但是……\x01",
            "我并不认为《互不侵犯条约》\x01",
            "是毫无意义的。\x02\x03",

            "#10103F在我刚刚加入警备队的时候，\x01",
            "帝国与共和国在边境线附近举行\x01",
            "大规模军事演习的那种压迫感……\x02\x03",

            "#10108F还有帝国的『列车炮』\x01",
            "对准克洛斯贝尔市时的恐怖感……\x01",
            "我至今依然难以忘却。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#12P#00303F的确……\x01",
            "如果发生战争，将会对居民们\x01",
            "造成巨大的伤害。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x105,
        (
            "#6P#10303F光是让当时的局势缓和下来，\x01",
            "这项条约就已经\x01",
            "相当有价值了。\x02\x03",

            "#10300F所以，殿下您无需\x01",
            "对此感到自责吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#11P#00006F瓦吉，你可真是的……\x01",
            "说话未免也太直接了。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x12,
        (
            "#11P#07009F呵呵……当然，\x01",
            "我也不能太过消极悲观。\x02\x03",

            "#07004F在本次通商会议上，\x01",
            "我一定要努力创造探讨\x01",
            "克洛斯贝尔未来的机会。\x02\x03",

            "#07002F来到这片墓地，就是为了\x01",
            "坚定这份决心。\x02\x03",

            "#07003F不过，却给尤莉亚和亲卫队的各位\x01",
            "增添了额外的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x13,
        "#12P#07104F殿下……您这是哪里的话。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#00000F该怎么说呢……\x01",
            "您果然是个内心很坚强的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        (
            "#12P#00100F嗯……让人真心羡慕\x01",
            "利贝尔这个国家。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x12,
        "#11P#07002F呵呵，感谢夸奖。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x13,
        "#12P#07100F……殿下，快要到预定时间了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x13, 500)

    #C0315
    ChrTalk(
        0x12,
        (
            "#5P#07005F啊，是呀。\x01",
            "差不多也该去\x01",
            "兰花塔了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B19():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6B19)
    TurnDirection(0x13, 0x101, 500)

    #C0316
    ChrTalk(
        0x12,
        (
            "#11P#07004F那么，特别任务支援科的各位，\x01",
            "我们就此失陪了。\x02\x03",

            "#07000F听说各位要在今日的\x01",
            "正式会议中负责警备工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，我们会\x01",
            "竭尽全力完成任务的。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x12,
        (
            "#11P#07009F呵呵，那就\x01",
            "拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x13,
        (
            "#11P#07102F那么，诸位，\x01",
            "我们在兰花塔再见吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    def lambda_6C32():

        label("loc_6C32")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_6C32")

    QueueWorkItem2(0x101, 2, lambda_6C32)

    def lambda_6C44():

        label("loc_6C44")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_6C44")

    QueueWorkItem2(0x102, 2, lambda_6C44)

    def lambda_6C56():

        label("loc_6C56")

        TurnDirection(0x109, 0x12, 500)
        Yield()
        Jump("loc_6C56")

    QueueWorkItem2(0x109, 2, lambda_6C56)

    def lambda_6C68():

        label("loc_6C68")

        TurnDirection(0x105, 0x12, 500)
        Yield()
        Jump("loc_6C68")

    QueueWorkItem2(0x105, 2, lambda_6C68)

    def lambda_6C7A():

        label("loc_6C7A")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_6C7A")

    QueueWorkItem2(0x103, 2, lambda_6C7A)

    def lambda_6C8C():

        label("loc_6C8C")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_6C8C")

    QueueWorkItem2(0x104, 2, lambda_6C8C)
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

    # Function_22_5CB0 end

    def Function_23_6D12(): pass

    label("Function_23_6D12")

    OP_95(0xFE, -2330, 4000, 42280, 2000, 0x0)
    OP_95(0xFE, -3140, 4000, 36010, 2000, 0x0)
    Return()

    # Function_23_6D12 end

    def Function_24_6D3B(): pass

    label("Function_24_6D3B")

    Call(0, 25)
    Return()

    # Function_24_6D3B end

    def Function_25_6D3F(): pass

    label("Function_25_6D3F")

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
        "#6P#00005F亚里欧斯先生……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0xB4, 0x1F4)

    #C0321
    ChrTalk(
        0xF,
        (
            "#11P#01400F……是你们啊。\x02\x03",

            "#01404F呵……没想到会在这里见面。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_7114")

    #C0322
    ChrTalk(
        0x101,
        (
            "#6P#00000F米歇尔先生\x01",
            "一直在找您哦。\x01",
            "　　　\x02\x03",

            "#00003F听说您被市长\x01",
            "叫去了。\x01",
            "　　　\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "#11P#01403F……是啊。\x02\x03",

            "#01400F市长也真是多礼，\x01",
            "我已经说过不必客气了，\x01",
            "他却还是坚持要当面道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#6P#00200F不过，抵御猎兵团的侵攻，\x01",
            "成功保卫兰花塔，\x01",
            "这的确是很了不起的功绩……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#6P#00302F嗯，克洛斯贝尔时代周刊\x01",
            "好像也对此大加报导，\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xF,
        (
            "#11P#01404F呵呵，当时毕竟\x01",
            "还有达德利的援护……\x02\x03",

            "#01400F……市长那边的事情\x01",
            "比预想中结束得早了一些。\x02\x03",

            "所以我就在回协会之前，\x01",
            "顺便来这里一趟。\x02\x03",

            "#01400F回去之后，得为迟归一事\x01",
            "向米歇尔道个歉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x102,
        (
            "#6P#00100F呵呵，说的也是。\x02\x03",

            "#00105F……您今天似乎\x01",
            "是来扫墓的……\x02\x03",

            "这座墓是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_725F")

    label("loc_7114")


    #C0328
    ChrTalk(
        0x101,
        (
            "#6P#00000F说起来……\x01",
            "我们已经在克洛斯贝尔时代周刊上了解到\x01",
            "您当时在兰花塔前的活跃表现了。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#6P#00200F面对着凶悍的猎兵团，\x01",
            "您也毫无畏惧地奋勇作战……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x104,
        "#6P#00302F嗯，真是了不起啊。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xF,
        (
            "#11P#01404F呵呵，当时毕竟\x01",
            "还有达德利的援护……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        (
            "#6P#00100F呵呵，您就别谦虚了。\x02\x03",

            "#00105F……您今天似乎\x01",
            "是来扫墓的……\x02\x03",

            "这座墓是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_725F")

    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(1000)
    OP_64(0xF)

    #C0333
    ChrTalk(
        0xF,
        (
            "#11P#01403F……纱绫·马克莱因。\x02\x03",

            "#01408F是五年前因事故身亡的……\x01",
            "小滴的母亲。\x02",
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
        "#6P#00200F小滴的母亲……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        (
            "#6P#00308F记得小滴也是在那起事故中\x01",
            "失去了光明吧……\x02",
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
        "#6P#10105F……亚里欧斯先生？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x105,
        "#6P#10305F您怎么了？\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xF,
        (
            "#11P#01404F……不，没什么。\x02\x03",

            "#01400F事情已经办完了，\x01",
            "我也该走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        "#6P#00000F啊……您辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_7479():

        label("loc_7479")

        TurnDirection(0x101, 0xF, 500)
        Yield()
        Jump("loc_7479")

    QueueWorkItem2(0x101, 2, lambda_7479)

    def lambda_748B():

        label("loc_748B")

        TurnDirection(0x102, 0xF, 500)
        Yield()
        Jump("loc_748B")

    QueueWorkItem2(0x102, 2, lambda_748B)

    def lambda_749D():

        label("loc_749D")

        TurnDirection(0x109, 0xF, 500)
        Yield()
        Jump("loc_749D")

    QueueWorkItem2(0x109, 2, lambda_749D)

    def lambda_74AF():

        label("loc_74AF")

        TurnDirection(0x105, 0xF, 500)
        Yield()
        Jump("loc_74AF")

    QueueWorkItem2(0x105, 2, lambda_74AF)

    def lambda_74C1():

        label("loc_74C1")

        TurnDirection(0x103, 0xF, 500)
        Yield()
        Jump("loc_74C1")

    QueueWorkItem2(0x103, 2, lambda_74C1)

    def lambda_74D3():

        label("loc_74D3")

        TurnDirection(0x104, 0xF, 500)
        Yield()
        Jump("loc_74D3")

    QueueWorkItem2(0x104, 2, lambda_74D3)
    OP_68(20680, 700, 30630, 1000)

    def lambda_74F6():
        OP_95(0xFE, 23250, 0, 30200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_74F6)
    WaitChrThread(0xF, 1)
    OP_4B(0xF, 0xFF)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0340
    ChrTalk(
        0xF,
        (
            "#12P#01401F接下来，克洛斯贝尔\x01",
            "恐怕将会遭遇前所未有的事态。\x02\x03",

            "#01403F然而，无论遇到怎样的状况，\x01",
            "无论面对怎样的试炼……\x02\x03",

            "#01400F你们也绝不能迷失最重要的信念。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#5P#00005F哎……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x105,
        "#5P#10305F……？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_7601():
        OP_95(0xFE, 23250, 0, 16970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7601)
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
        "#11P#00103F……他走了。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x104,
        "#5P#00305F刚才的话是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        "#6P#10105F不、不知道……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x103,
        (
            "#6P#00203F不太清楚……\x01",
            "应该是某种忠告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#11P#00001F（……亚里欧斯先生……？）\x02",
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

    # Function_25_6D3F end

    def Function_26_7791(): pass

    label("Function_26_7791")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7868")

    #C0349
    ChrTalk(
        0x101,
        (
            "#00000F（这个人……\x01",
            "  记得是叫尼尔森吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7883")

    label("loc_7868")


    #C0350
    ChrTalk(
        0x101,
        "#00000F（这个人……）\x02",
    )

    CloseMessageWindow()

    label("loc_7883")

    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0351
    ChrTalk(
        0xE,
        (
            "好了……\x01",
            "差不多该回去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0352
    ChrTalk(
        0xE,
        (
            "唔，你们也是\x01",
            "来扫墓的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "大家好，\x01",
            "我先失陪了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7900():
        OP_95(0xFE, -20540, 0, 24610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7900)
    Sleep(500)

    def lambda_791D():

        label("loc_791D")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_791D")

    QueueWorkItem2(0x101, 1, lambda_791D)
    Sleep(50)

    def lambda_7932():

        label("loc_7932")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_7932")

    QueueWorkItem2(0x102, 1, lambda_7932)
    Sleep(50)

    def lambda_7947():

        label("loc_7947")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_7947")

    QueueWorkItem2(0x103, 1, lambda_7947)
    Sleep(50)

    def lambda_795C():

        label("loc_795C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_795C")

    QueueWorkItem2(0x104, 1, lambda_795C)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -15310, 0, 19380, 2000, 0x0)
    SetChrFlags(0xE, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_799B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_799B)
    Sleep(100)

    def lambda_79AB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_79AB)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7A52")

    #C0354
    ChrTalk(
        0x101,
        (
            "#00000F尼尔森先生……\x01",
            "来为我大哥扫墓了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        (
            "#00100F他在祭拜时似乎很热诚……\x01",
            "是不是在报告什么事情？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#00000F嗯，怎么回事呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AE8")

    label("loc_7A52")

    TurnDirection(0x102, 0x101, 500)

    #C0357
    ChrTalk(
        0x102,
        "#00100F罗伊德，你认识那个人？\x02",
    )

    CloseMessageWindow()

    def lambda_7A81():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A81)
    Sleep(50)

    def lambda_7A91():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7A91)
    Sleep(300)

    #C0358
    ChrTalk(
        0x101,
        (
            "#00000F不……没有印象啊。\x02\x03",

            "（既然来扫墓，\x01",
            "  大概是认识大哥的人吧……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -21160, 0, 21930, 135)
    SetScenarioFlags(0x19D, 4)
    EventEnd(0x5)
    Return()

    # Function_26_7791 end

    def Function_27_7B0E(): pass

    label("Function_27_7B0E")

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
        "#00005F尼尔森先生……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0361
    ChrTalk(
        0xE,
        "#5P……唔，是罗伊德警官啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0362
    ChrTalk(
        0x102,
        (
            "#00108F#6P这里是……\x01",
            "罗伊德的哥哥的墓……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#00000F您是来给我大哥\x01",
            "扫墓的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xE,
        "#11P嗯……\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        (
            "#11P而且还有些话\x01",
            "想告诉盖伊先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0366
    ChrTalk(
        0x101,
        "#00005F有话要告诉大哥……？\x02",
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
            "#5P袭击事件和独立宣言，\x01",
            "还有今早的总统演讲……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xE,
        (
            "#5P如今，虽然大家的具体情绪\x01",
            "各不相同，但却都在朝着\x01",
            "同一个方向前进。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xE,
        (
            "#5P正因如此……\x01",
            "使我回想起了\x01",
            "『过去的黑暗』。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        (
            "#00008F『过去的黑暗』……\x01",
            "……莫非是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "#5P嗯，就是你的兄长——\x01",
            "盖伊·班宁斯搜查官\x01",
            "遇害事件。\x02",
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
        "#00105F#6P哎……？\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x103,
        "#00208F#6P盖伊先生……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        "#00301F#6P这可真是……\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#00006F偏偏在这种时期……\x01",
            "不，也许正是因为在这种时期……\x02\x03",

            "#00001F尼尔森先生，\x01",
            "您有什么发现吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xE,
        "#5P唔……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0377
    ChrTalk(
        0xE,
        "#11P罗伊德警官，还有各位。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "#11P如果不介意，能否换个地方，\x01",
            "与我一起探讨此事件？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 28)
    Return()

    # Function_27_7B0E end

    def Function_28_7F80(): pass

    label("Function_28_7F80")

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
            "陪尼尔森一起探讨\x01",      # 0
            "再考虑一下\x01",            # 1
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
        (0, "loc_7FEC"),
        (1, "loc_80F8"),
        (SWITCH_DEFAULT, "loc_8186"),
    )


    label("loc_7FEC")


    #C0379
    ChrTalk(
        0x101,
        (
            "#00003F……………………………\x02\x03",

            "#00001F我明白了，\x01",
            "请务必指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xE,
        "非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xE,
        (
            "在这里说话不方便，\x01",
            "我们先回市里吧。\x02",
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
            "任务【盖伊·班宁斯遇害事件的分析】\x07\x00",
            "开始！\x02",
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
    Jump("loc_8186")

    label("loc_80F8")


    #C0383
    ChrTalk(
        0x101,
        (
            "#00003F……不好意思，\x01",
            "我可以再考虑一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xE,
        "嗯，无妨。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xE,
        (
            "我会暂时留在这里，\x01",
            "等你方便时再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_817E")
    OP_93(0xE, 0x0, 0x1F4)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)

    label("loc_817E")

    SetScenarioFlags(0x19B, 6)
    Jump("loc_8186")

    label("loc_8186")

    Return()

    # Function_28_7F80 end

    def Function_29_8187(): pass

    label("Function_29_8187")

    TalkBegin(0xE)

    #C0386
    ChrTalk(
        0xE,
        "……是罗伊德警官啊。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xE,
        (
            "如果不介意，能否换个地方，\x01",
            "与我一起探讨此事件？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Call(0, 28)
    TalkEnd(0xE)
    Return()

    # Function_29_8187 end

    SaveToFile()

Try(main)
