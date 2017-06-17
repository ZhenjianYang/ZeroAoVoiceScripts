from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1540.bin",                # FileName
        "t1540",                    # MapName
        "t1540",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1540",                  # 0
        "塞茜尔",                 # 1
        "菲莉亚护士",             # 2
        "玛萨护士长",             # 3
        "希伦护士",               # 4
        "梅菲尔护士",             # 5
        "诊断医生贝尔达因",       # 6
        "赛兰德教授",             # 7
        "住院患者",               # 8
        "住院患者",               # 9
        "住院患者",               # 10
        "住院患者",               # 11
        "住院患者",               # 12
        "住院患者",               # 13
        "住院患者",               # 14
        "住院患者",               # 15
        "住院患者",               # 16
        "住院患者",               # 17
        "住院患者",               # 18
        "住院患者",               # 19
        "警官",                   # 20
        "女警",                   # 21
        "警官",                   # 22
        "警官",                   # 23
        "诺加诺夫",               # 24
        "杰德",                   # 25
        "修伊",                   # 26
        "斯拉修",                 # 27
        "勤杂工戴森",             # 28
        "实习医生利顿",           # 29
        "实习医生古恩",           # 30
        "住院患者",               # 31
        "住院患者",               # 32
        "住院患者",               # 33
        "住院患者",               # 34
        "住院患者",               # 35
        "住院患者",               # 36
        "住院患者",               # 37
        "住院患者",               # 38
    ))

    AddCharChip((
        "chr/ch05300.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "chr/ch29600.itc",                   # 02
        "chr/ch29800.itc",                   # 03
        "chr/ch29300.itc",                   # 04
        "chr/ch44800.itc",                   # 05
        "apl/ch50133.itc",                   # 06
        "apl/ch50141.itc",                   # 07
        "apl/ch50135.itc",                   # 08
        "apl/ch50137.itc",                   # 09
        "apl/ch50139.itc",                   # 0A
        "apl/ch50143.itc",                   # 0B
        "apl/ch50132.itc",                   # 0C
        "apl/ch50141.itc",                   # 0D
        "apl/ch51538.itc",                   # 0E
        "apl/ch51540.itc",                   # 0F
        "chr/ch20200.itc",                   # 10
        "chr/ch29400.itc",                   # 11
        "chr/ch29500.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(110709,  0,       -4320,   90,   389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(24610,   0,       680,     225,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(108930,  0,       1450,    45,   261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(110709,  0,       -5639,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(110709,  0,       -4320,   90,   261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(110720,  0,       -4239,   180,  261,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(4849,    699,     -56970,  270,  453,  0x0, 0,   8,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  453,  0x0, 0,   9,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   10,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  453,  0x0, 0,   8,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  453,  0x0, 0,   11,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-4000,   699,     57029,   270,  453,  0x0, 0,   9,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-4110,   400,     -56970,  0,    469,  0x0, 0,   12,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(4849,    699,     -56970,  270,  453,  0x0, 0,   10,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-4000,   699,     57029,   270,  453,  0x0, 0,   11,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  453,  0x0, 0,   9,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  453,  0x0, 0,   13,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(4809,    400,     -51959,  0,    469,  0x0, 0,   14,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(4809,    400,     -56970,  0,    469,  0x0, 0,   15,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(-4110,   400,     -52060,  0,    469,  0x0, 0,   15,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(-4110,   400,     -56970,  0,    469,  0x0, 0,   14,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(103349,  0,       0,       90,   389,  0x0, 0,   16,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   43,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  453,  0x0, 0,   9,   0,   255, 255, 0,   44,  255,  0)
    DeclNpc(4849,    699,     -56970,  270,  453,  0x0, 0,   8,   0,   255, 255, 0,   45,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  453,  0x0, 0,   7,   0,   255, 255, 0,   46,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   47,  255,  0)
    DeclNpc(-4000,   699,     57029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   48,  255,  0)
    DeclNpc(4849,    699,     -56970,  270,  453,  0x0, 0,   10,  0,   255, 255, 0,   49,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  453,  0x0, 0,   9,   0,   255, 255, 0,   50,  255,  0)

    DeclEvent(0x0000, 0, 53,  8.779999732971191,     5.800000190734863,     -1.0,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -2.926666736602783,    -2.9000000953674316,   0.20000001788139343,   1.0])

    DeclActor(23500,   0,       -830,    1500,    24610,   1500,    680,     0x007E, 0,  5,  0x0000)

    ChipFrameInfo(1684, 0)                                       # 0

    ScpFunction((
        "Function_0_694",          # 00, 0
        "Function_1_744",          # 01, 1
        "Function_2_DF4",          # 02, 2
        "Function_3_133B",         # 03, 3
        "Function_4_16EF",         # 04, 4
        "Function_5_1B4C",         # 05, 5
        "Function_6_1B50",         # 06, 6
        "Function_7_2780",         # 07, 7
        "Function_8_3572",         # 08, 8
        "Function_9_3643",         # 09, 9
        "Function_10_36EA",        # 0A, 10
        "Function_11_3AD6",        # 0B, 11
        "Function_12_3C1A",        # 0C, 12
        "Function_13_3D8E",        # 0D, 13
        "Function_14_40C9",        # 0E, 14
        "Function_15_498F",        # 0F, 15
        "Function_16_4A33",        # 10, 16
        "Function_17_4CFB",        # 11, 17
        "Function_18_4E22",        # 12, 18
        "Function_19_4EF0",        # 13, 19
        "Function_20_50AF",        # 14, 20
        "Function_21_523D",        # 15, 21
        "Function_22_5419",        # 16, 22
        "Function_23_5651",        # 17, 23
        "Function_24_57B4",        # 18, 24
        "Function_25_5A78",        # 19, 25
        "Function_26_5AF1",        # 1A, 26
        "Function_27_5B59",        # 1B, 27
        "Function_28_5BA4",        # 1C, 28
        "Function_29_5C27",        # 1D, 29
        "Function_30_5D36",        # 1E, 30
        "Function_31_5E1B",        # 1F, 31
        "Function_32_5F0C",        # 20, 32
        "Function_33_5F78",        # 21, 33
        "Function_34_5FDC",        # 22, 34
        "Function_35_60BD",        # 23, 35
        "Function_36_61F9",        # 24, 36
        "Function_37_6234",        # 25, 37
        "Function_38_629D",        # 26, 38
        "Function_39_6542",        # 27, 39
        "Function_40_65F9",        # 28, 40
        "Function_41_66B2",        # 29, 41
        "Function_42_686D",        # 2A, 42
        "Function_43_6AE4",        # 2B, 43
        "Function_44_6B53",        # 2C, 44
        "Function_45_6C49",        # 2D, 45
        "Function_46_6D13",        # 2E, 46
        "Function_47_6EAB",        # 2F, 47
        "Function_48_6F82",        # 30, 48
        "Function_49_706C",        # 31, 49
        "Function_50_7135",        # 32, 50
        "Function_51_721C",        # 33, 51
        "Function_52_7223",        # 34, 52
        "Function_53_7F39",        # 35, 53
        "Function_54_7F88",        # 36, 54
    ))


    def Function_0_694(): pass

    label("Function_0_694")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6CC"),
        (1, "loc_6D8"),
        (2, "loc_6E4"),
        (3, "loc_6F0"),
        (4, "loc_6FC"),
        (5, "loc_708"),
        (6, "loc_714"),
        (SWITCH_DEFAULT, "loc_720"),
    )


    label("loc_6CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_708")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_714")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_720")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_743")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_743")

    Return()

    # Function_0_694 end

    def Function_1_744(): pass

    label("Function_1_744")

    SetChrChipByIndex(0xF, 0x6)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrChipByIndex(0x14, 0x6)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0x8)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrChipByIndex(0x16, 0xB)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x9)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrChipByIndex(0x18, 0x7)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrChipByIndex(0x19, 0xC)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0xA)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1B, 0x7)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    SetChrChipByIndex(0x1C, 0xB)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1D, 0x9)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    SetChrChipByIndex(0x1E, 0xD)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x26, 0x6)
    SetChrSubChip(0x26, 0x0)
    EndChrThread(0x26, 0x0)
    SetChrBattleFlags(0x26, 0x4)
    SetChrChipByIndex(0x27, 0x9)
    SetChrSubChip(0x27, 0x0)
    EndChrThread(0x27, 0x0)
    SetChrBattleFlags(0x27, 0x4)
    SetChrChipByIndex(0x28, 0x8)
    SetChrSubChip(0x28, 0x0)
    EndChrThread(0x28, 0x0)
    SetChrBattleFlags(0x28, 0x4)
    SetChrChipByIndex(0x29, 0x7)
    SetChrSubChip(0x29, 0x0)
    EndChrThread(0x29, 0x0)
    SetChrBattleFlags(0x29, 0x4)
    SetChrChipByIndex(0x2A, 0x7)
    SetChrSubChip(0x2A, 0x0)
    EndChrThread(0x2A, 0x0)
    SetChrBattleFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2B, 0x6)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    SetChrChipByIndex(0x2C, 0xA)
    SetChrSubChip(0x2C, 0x0)
    EndChrThread(0x2C, 0x0)
    SetChrBattleFlags(0x2C, 0x4)
    SetChrChipByIndex(0x2D, 0x9)
    SetChrSubChip(0x2D, 0x0)
    EndChrThread(0x2D, 0x0)
    SetChrBattleFlags(0x2D, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_92A")
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xD, 26640, 0, -19370, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    Jump("loc_DDB")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9D3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 102790, 0, 3080, 0)
    SetChrPos(0xA, 23790, 0, 1610, 135)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x9, 24610, 0, 680, 315)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_995")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_995")

    SetChrPos(0xD, 3970, 0, -55460, 135)
    ClearChrFlags(0x2C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BF")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x2C, 0x10)

    label("loc_9BF")

    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2D, 0x80)
    Jump("loc_DDB")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A30")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 24840, 0, -17230, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 24830, 0, -18620, 0)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    Jump("loc_DDB")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A97")
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 3490, 0, 55460, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")
    SetChrFlags(0x24, 0x10)
    SetChrFlags(0x26, 0x10)

    label("loc_A63")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 26640, 0, -19370, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    Jump("loc_DDB")

    label("loc_A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC7")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 110700, 0, -3400, 90)

    label("loc_AC7")

    SetChrPos(0xD, -3950, 0, -55500, 180)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -10, 0, 53970, 0)
    Jump("loc_DDB")

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BA5")
    SetChrPos(0xA, -4100, 0, 55470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B44")
    SetChrFlags(0xA, 0x10)

    label("loc_B44")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, -3950, 0, -55500, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")
    SetChrFlags(0x17, 0x10)

    label("loc_B8C")

    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_DDB")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C66")
    SetChrPos(0xA, 110710, 0, -4320, 180)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xB, 110710, 0, -5640, 0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 1390, 0, 52480, 315)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C24")
    ClearChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24")
    ClearChrFlags(0xB, 0x10)

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    SetChrFlags(0x15, 0x10)
    SetChrSubChip(0x15, 0x1)

    label("loc_C37")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 3490, 0, -53570, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C61")
    SetChrFlags(0x24, 0x10)

    label("loc_C61")

    Jump("loc_DDB")

    label("loc_C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CCF")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 110650, 0, -5010, 90)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 26640, 0, -19370, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 6700, 0, 4970, 180)
    Jump("loc_DDB")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D3A")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -540, 0, 53560, 315)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x10)
    SetChrPos(0x24, -3940, 0, -55480, 180)
    Jump("loc_DDB")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D95")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, 24930, 0, -26050, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D90")
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 30220, 0, -21990, 315)

    label("loc_D90")

    Jump("loc_DDB")

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrPos(0xB, -3950, 0, 53530, 180)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0x2)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_DDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF3")
    ClearScenarioFlags(0x25, 1)
    Call(0, 51)

    label("loc_DF3")

    Return()

    # Function_1_744 end

    def Function_2_DF4(): pass

    label("Function_2_DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E06")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E06")

    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FE4")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1026")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1068")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_10AA")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_10AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1120")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1196")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11D8")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_11D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_121A")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_125C")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_125C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_129E")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_129E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12DB")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)

    label("loc_12DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1317")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_1317")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133A")
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x4, 0x0, 0x36)

    label("loc_133A")

    Return()

    # Function_2_DF4 end

    def Function_3_133B(): pass

    label("Function_3_133B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_144F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1359")
    Call(0, 4)
    Jump("loc_144A")

    label("loc_1359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E2")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01304F特别任务支援科全员\x01",
            "已经聚齐，一定可以\x01",
            "解决这一连串的事件。\x02\x03",

            "#01300F我会在这里给你们加油的，\x01",
            "大家要努力哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_144A")

    label("loc_13E2")


    #C0002
    ChrTalk(
        0x8,
        (
            "#01304F呵呵，既然如此，\x01",
            "我也要努力做好医院的工作。\x02\x03",

            "#01300F女神一定会保佑我们的，\x01",
            "你们也要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144A")

    Jump("loc_16EB")

    label("loc_144F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B9")

    #C0003
    ChrTalk(
        0x8,
        (
            "#01300F帮我向科长和\x01",
            "小琪雅问声好。\x02\x03",

            "虽然形势严峻……\x01",
            "但我们都要努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B9")

    label("loc_14B9")

    Jump("loc_16EB")

    label("loc_14BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14CC")
    Jump("loc_16EB")

    label("loc_14CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_14DA")
    Jump("loc_16EB")

    label("loc_14DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166A")

    #C0004
    ChrTalk(
        0x8,
        (
            "#01308F因为小滴手术的事，\x01",
            "医院里的气氛\x01",
            "变得十分阴沉。\x02\x03",

            "#01300F但是，正是在这种时候，\x01",
            "我们护士才更加\x01",
            "需要露出笑容。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00000F确实如此。\x01",
            "在看到琪雅的笑容时，\x01",
            "我们就会有种被治愈的感觉……\x02\x03",

            "#00009F塞茜尔姐姐的笑容\x01",
            "也一定可以让患者们\x01",
            "立刻就恢复精神的。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#00100F嗯，肯定能让\x01",
            "不安的心情烟消云散。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#01309F呵呵，谢谢。\x02\x03",

            "#01300F连小滴都很乐观，\x01",
            "我们更应该振作起来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16C1")

    label("loc_166A")


    #C0008
    ChrTalk(
        0x8,
        (
            "#01300F感到消沉的时候，\x01",
            "就更要露出笑容。\x02\x03",

            "打消患者们的不安，\x01",
            "也是我们护士的职责。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C1")

    Jump("loc_16EB")

    label("loc_16C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16D4")
    Jump("loc_16EB")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16E2")
    Jump("loc_16EB")

    label("loc_16E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16EB")

    label("loc_16EB")

    TalkEnd(0xFE)
    Return()

    # Function_3_133B end

    def Function_4_16EF(): pass

    label("Function_4_16EF")

    EventBegin(0x0)
    Fade(500)
    OP_68(102280, 1100, 1850, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18970, 0)
    SetChrPos(0x101, 102320, 0, 1060, 356)
    SetChrPos(0x102, 103040, 0, 420, 356)
    SetChrPos(0x103, 101120, 0, 850, 41)
    SetChrPos(0x104, 104270, 0, 1230, 311)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D1")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A6")
    SetChrPos(0x109, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_17D1")

    label("loc_17A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17D1")
    SetChrPos(0x105, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_17D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_183A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_180F")
    SetChrPos(0x105, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_183A")

    label("loc_180F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_183A")
    SetChrPos(0x109, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_183A")

    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#01305F啊，罗伊德，是你们……！\x02\x03",

            "#01309F呵呵，特别任务支援科的成员\x01",
            "终于聚齐了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#12P#00000F嗯，总算都回来了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18FF")

    #C0011
    ChrTalk(
        0x105,
        (
            "#12P#10402F呵呵，多亏有\x01",
            "姐姐你的支持。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FF")


    #C0012
    ChrTalk(
        0x102,
        (
            "#12P#00100F让你担心了，\x01",
            "塞茜尔小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#5P#01300F艾莉小姐……还有大家\x01",
            "好像都吃了不少苦。\x02\x03",

            "#01304F呵呵，但不知道为什么……\x02\x03",

            "#01302F感觉你们之间的羁绊\x01",
            "比以前更加深厚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#12P#00302F哈哈，努力走到现在这一步，\x01",
            "确实吃过不少苦头。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#00202F但成就感也格外强呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A5C")

    #C0016
    ChrTalk(
        0x109,
        (
            "#12P#10112F啊哈哈……\x01",
            "但接下来要做的事情还堆积如山。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5C")


    #C0017
    ChrTalk(
        0x8,
        (
            "#5P#01304F困难时期恐怕还会持续一阵子……\x02\x03",

            "#01300F但你们一定可以\x01",
            "解决这一连串的事件。\x02\x03",

            "#01309F呵呵，大家加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00000F嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1AC, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 102700, 0, 940, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B26")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1B26")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3E")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1B3E")

    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_4_16EF end

    def Function_5_1B4C(): pass

    label("Function_5_1B4C")

    Call(0, 6)
    Return()

    # Function_5_1B4C end

    def Function_6_1B50(): pass

    label("Function_6_1B50")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C15")

    #C0019
    ChrTalk(
        0x9,
        (
            "竟然出现了那样的大树，\x01",
            "事、事情真是\x01",
            "不得了了……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "护士长要我们\x01",
            "保持冷静，不要让\x01",
            "患者们感到不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "唉……虽然也不是完全无法做到，\x01",
            "但真是很难镇静下来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C80")

    label("loc_1C15")


    #C0022
    ChrTalk(
        0x9,
        (
            "啊，你们要找塞茜尔前辈吗？\x01",
            "她去院内的休息处\x01",
            "看那棵大树了～\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "唉，前辈竟然那么冷静，\x01",
            "真是了不起……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C80")

    Jump("loc_277C")

    label("loc_1C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D0C")

    #C0024
    ChrTalk(
        0x9,
        (
            "我这就要去接待那些\x01",
            "无法回市里的住院患者\x01",
            "和外来的门诊患者～\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "市里出了那么大的事，\x01",
            "这种情况恐怕还会持续一阵子吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_277C")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCA")

    #C0026
    ChrTalk(
        0x9,
        (
            "多诺邦警督恢复得\x01",
            "很顺利，短期之内\x01",
            "应该就能出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "但是，听说伊莉娅小姐\x01",
            "就算耐心接受复健训练，\x01",
            "也不一定能痊愈……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "希望她努力坚持，\x01",
            "日后能重返舞台。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E60")

    label("loc_1DCA")


    #C0029
    ChrTalk(
        0x9,
        (
            "听说伊莉娅小姐\x01",
            "就算耐心接受复健训练，\x01",
            "也不一定能痊愈……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "话虽如此，但她依然能让人\x01",
            "感受到一种难以名状的希望，\x01",
            "这正是伊莉娅小姐的过人之处啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E60")

    Jump("loc_277C")

    label("loc_1E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0B")

    #C0031
    ChrTalk(
        0x9,
        (
            "伊莉娅小姐和多诺邦警督\x01",
            "都恢复意识了～\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "最近总是听到不太平的消息，\x01",
            "说实话，真是令人郁闷……\x01",
            "能出现这种振奋人心的事情，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F43")

    label("loc_1F0B")


    #C0033
    ChrTalk(
        0x9,
        (
            "伊莉娅小姐和多诺邦警督\x01",
            "都恢复了意识，\x01",
            "真是太好了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F43")

    Jump("loc_277C")

    label("loc_1F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2026")

    #C0034
    ChrTalk(
        0x9,
        (
            "研究楼的集中治疗室\x01",
            "收容了警备队的\x01",
            "成员……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "大家都被猎兵打成了重伤，\x01",
            "要想出院，恐怕得花不少时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "虽然我以前也曾见过各种各样的\x01",
            "住院患者，但那些警备队员的伤势\x01",
            "实在是让我不忍目睹……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2091")

    label("loc_2026")


    #C0037
    ChrTalk(
        0x9,
        (
            "虽然我以前也曾见过\x01",
            "各种各样的住院患者……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "但集中治疗室那些\x01",
            "警备队员的伤势实在是\x01",
            "让我不忍目睹……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2091")

    Jump("loc_277C")

    label("loc_2096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_217C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2131")

    #C0039
    ChrTalk(
        0x9,
        (
            "昨天那起列车事故\x01",
            "所带来的忙乱，基本\x01",
            "已经平稳下来了～\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        "（咕噜噜……）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "……说起来，\x01",
            "我都没有好好吃饭。\x01",
            "肚子饿了呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2177")

    label("loc_2131")


    #C0042
    ChrTalk(
        0x9,
        (
            "工作太忙，\x01",
            "都没有好好吃饭。\x01",
            "肚子饿了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "待会去吃个午饭吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2177")

    Jump("loc_277C")

    label("loc_217C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_22F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226D")

    #C0044
    ChrTalk(
        0x9,
        (
            "赛兰德教授好像在\x01",
            "为小滴设计新的\x01",
            "复明手术方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "上次的手术失败后，我本以为\x01",
            "她会很消沉，都不敢跟她搭话……\x01",
            "原来她早就从阴影中走出来了～\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "在任何时候都能保持冷静，\x01",
            "并采取最合理的行动……\x01",
            "真不愧是教授啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22ED")

    label("loc_226D")


    #C0047
    ChrTalk(
        0x9,
        (
            "在事情不顺的时候，\x01",
            "想迅速调整心情\x01",
            "是很困难的～\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "在任何时候都能保持冷静，\x01",
            "并采取最合理的行动……\x01",
            "真不愧是赛兰德教授啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22ED")

    Jump("loc_277C")

    label("loc_22F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C8")

    #C0049
    ChrTalk(
        0x9,
        (
            "我正为小滴手术的事情\x01",
            "而消沉的时候，护士长\x01",
            "突然拍了一下我的屁股。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "呼～吓我一跳……\x01",
            "现在还火辣辣地疼呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "不过，多亏她那一下，\x01",
            "消沉的情绪好像已经被驱散了。\x01",
            "今天也要继续加油～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2450")

    label("loc_23C8")


    #C0052
    ChrTalk(
        0x9,
        (
            "多亏护士长那一下，\x01",
            "消沉的情绪好像已经被驱散了。\x01",
            "不愧是护士长啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "……不过，她下手\x01",
            "没必要那么重吧。\x01",
            "屁股到现在还火辣辣地疼呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2450")

    Jump("loc_277C")

    label("loc_2455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24DC")

    #C0054
    ChrTalk(
        0x9,
        (
            "米海尔能顺利出院，我自然很开心，\x01",
            "但同时也有些失落～\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "小滴和他年纪接近，\x01",
            "关系也非常好，\x01",
            "肯定会比别人更加寂寞吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_277C")

    label("loc_24DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2570")

    #C0056
    ChrTalk(
        0x9,
        (
            "我也好想去看今天的\x01",
            "兰花塔揭幕式啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "但最近实在是\x01",
            "请不到假……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "虽说工作忙是没办法的事，\x01",
            "但也该出去玩玩了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25DD")

    label("loc_2570")


    #C0059
    ChrTalk(
        0x9,
        (
            "这次的彩虹剧团公演，\x01",
            "我都不确定能不能\x01",
            "抽空去排队买票。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "虽说工作忙是没办法的事，\x01",
            "但也该出去玩玩了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DD")

    Jump("loc_277C")

    label("loc_25E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_277C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2738")

    #C0061
    ChrTalk(
        0x9,
        (
            "您好～这里是\x01",
            "护士中心……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "……啊！\x01",
            "是警察弟弟和兰迪先生～！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        "#00302F哟，菲莉亚。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00000F好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "是啊～！\x01",
            "呵呵，你们好像很有精神呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "……兰迪先生，我最近一定\x01",
            "会把行程空出来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#00309F好啊，\x01",
            "有时间再联谊哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#10106F前辈，你又随便\x01",
            "约人家……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00106F唉，真拿他没办法。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 5)
    Jump("loc_277C")

    label("loc_2738")


    #C0070
    ChrTalk(
        0x9,
        (
            "真想和大家\x01",
            "一起联谊啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "到时候，警察弟弟\x01",
            "也一定要来啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_277C")

    TalkEnd(0x9)
    Return()

    # Function_6_1B50 end

    def Function_7_2780(): pass

    label("Function_7_2780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27A9")
    Call(0, 52)
    Return()

    label("loc_27A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285A")

    #C0072
    ChrTalk(
        0xFE,
        (
            "门诊又开放了，\x01",
            "好久没有这么忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "前一段时间一直无法前来的患者\x01",
            "一下子涌了过来，所以现在门诊患者特别多。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "好，打起精神，\x01",
            "努力工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28C4")

    label("loc_285A")


    #C0075
    ChrTalk(
        0xFE,
        (
            "不足的物资已经拜托\x01",
            "哈罗德先生送过来了，\x01",
            "接收患者的准备工作已经万无一失。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "打起精神，努力工作吧。\x02",
    )

    CloseMessageWindow()

    label("loc_28C4")

    Jump("loc_356E")

    label("loc_28C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2954")

    #C0077
    ChrTalk(
        0xFE,
        (
            "我去住宿设施那边\x01",
            "看看外来客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "那么，菲莉亚，\x01",
            "向住院患者说明情况的\x01",
            "工作就交给你了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)

    #C0079
    ChrTalk(
        0x9,
        "好，我明白了～\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_356E")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A40")

    #C0080
    ChrTalk(
        0xFE,
        (
            "话说回来，竟然只允许重病、\x01",
            "重伤患者入院接受治疗，\x01",
            "这种规定真是不像话。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "有些疾病和伤势比较隐蔽，\x01",
            "光看外表根本就看不出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "如果使那些及时接受治疗就能\x01",
            "得救的患者错过最佳救治时期，\x01",
            "未免也太残酷了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2AAD")

    label("loc_2A40")


    #C0083
    ChrTalk(
        0xFE,
        (
            "竟然只允许重病、\x01",
            "重伤患者入院接受治疗，\x01",
            "这种规定真是不像话。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "迪塔总统到底有没有\x01",
            "意识到这一点啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAD")

    Jump("loc_356E")

    label("loc_2AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEB")
    TurnDirection(0xFE, 0x103, 0)

    #C0085
    ChrTalk(
        0xFE,
        (
            "小缇欧……\x01",
            "你要离开医院了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        (
            "#00200F嗯……玛萨护士长，\x01",
            "承蒙您照顾了。\x02\x03",

            "#00204F以前住院时的恩情，\x01",
            "总算稍微还上了一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "哎呀，真是的，都是陈年旧事了，\x01",
            "你完全不必放在心上。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "以后随时都可以过来玩……\x01",
            "一定要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#00202F呵呵，好的，\x01",
            "我一定会再来玩的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C66")

    label("loc_2BEB")


    #C0090
    ChrTalk(
        0xFE,
        (
            "小缇欧在维护医院的器材\x01",
            "方面帮了许多忙，\x01",
            "我也有了聊天对象，非常开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "以后随时都可以过来玩……\x01",
            "一定要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C66")

    Jump("loc_356E")

    label("loc_2C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9F")

    #C0092
    ChrTalk(
        0xFE,
        (
            "我们这些医学界人士，\x01",
            "自然会经常面对\x01",
            "人的死亡。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "像我和教授们这种从业\x01",
            "多年的人，已经不会因为\x01",
            "个人的死亡而轻易落泪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "但这次的袭击事件实在是太过分了……\x01",
            "一想到那么多无辜的人不幸牺牲，\x01",
            "就有一股怒火涌上心头。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "竟然如此随便地夺去他人的生命……\x01",
            "这种行为绝对不能饶恕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E02")

    label("loc_2D9F")


    #C0096
    ChrTalk(
        0xFE,
        (
            "医生会拯救众多生命，\x01",
            "而那些猎兵却\x01",
            "随便夺去别人的性命。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "……人这种生物，\x01",
            "真是罪孽深重啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E02")

    Jump("loc_356E")

    label("loc_2E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E22")
    Call(0, 8)
    Jump("loc_2E90")

    label("loc_2E22")


    #C0098
    ChrTalk(
        0xFE,
        (
            "好啦，只要保住了性命，\x01",
            "以后总有机会去看彩虹剧团的公演嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "如今应该感谢女神让自己得救，\x01",
            "并安心疗养。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E90")

    Jump("loc_356E")

    label("loc_2E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBA")
    Call(0, 9)
    Jump("loc_2F01")

    label("loc_2EBA")


    #C0100
    ChrTalk(
        0xFE,
        "说得倒是好听……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "想到你以前的种种失误，\x01",
            "实在是没有说服力呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F01")

    Jump("loc_2F8F")

    label("loc_2F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F67")

    #C0102
    ChrTalk(
        0xFE,
        (
            "你们特地赶来，\x01",
            "真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "我必须要\x01",
            "教训一下这孩子，\x01",
            "下次再聊哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F8F")

    label("loc_2F67")


    #C0104
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "照顾希伦\x01",
            "真是够累人的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8F")

    Jump("loc_356E")

    label("loc_2F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_310E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3099")

    #C0105
    ChrTalk(
        0xFE,
        (
            "真是受不了，所有人都像\x01",
            "泄了气的皮球一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "小滴的手术不幸失败，\x01",
            "我非常理解大家现在的心情。\x01",
            "遇到这种事，谁都会消沉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "但是，如果连我们\x01",
            "都一脸沮丧的表情，\x01",
            "会让患者们感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "我觉得，在这种时候\x01",
            "就更应该打起精神来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3109")

    label("loc_3099")


    #C0109
    ChrTalk(
        0xFE,
        (
            "真是受不了，所有人都像\x01",
            "泄了气的皮球一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "就算是强打精神，也比垂头丧气好啊。\x01",
            "喂，你们也要打起精神哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3109")

    Jump("loc_356E")

    label("loc_310E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326E")
    TurnDirection(0xFE, 0x103, 0)

    #C0111
    ChrTalk(
        0xFE,
        (
            "呀……！\x01",
            "这不是\x01",
            "小缇欧吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "哎呀，好久不见呢！\x01",
            "你还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#00202F托您的福，我很好。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x109,
        (
            "#10100F原来缇欧\x01",
            "认识护士长啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#00200F嗯，以前住院的时候，\x01",
            "一直承蒙护士长的照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "哈哈，我只是尽到了\x01",
            "护士的本分而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "警察的工作应该也很辛苦吧，\x01",
            "你要注意身体，\x01",
            "好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x103,
        "#00204F是……谢谢您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 4)
    Jump("loc_32D8")

    label("loc_326E")


    #C0119
    ChrTalk(
        0xFE,
        (
            "以前我就说过，\x01",
            "小缇欧真是\x01",
            "越大越漂亮了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "警察的工作应该也很辛苦吧，\x01",
            "你要注意身体，\x01",
            "好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D8")

    Jump("loc_356E")

    label("loc_32DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3443")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33BC")

    #C0121
    ChrTalk(
        0xFE,
        (
            "塞茜尔对所有人\x01",
            "都一视同仁，\x01",
            "体谅关心着对方。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "看上去似乎没什么大不了，\x01",
            "但其实很少有人能做到。\x01",
            "我觉得这是一种出色的才能。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "呵呵，那孩子会走上\x01",
            "护士这条道路，\x01",
            "或许也是因为女神的指引呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_343E")

    label("loc_33BC")


    #C0124
    ChrTalk(
        0xFE,
        (
            "关心和体谅能给\x01",
            "患者们带来安心感。\x01",
            "这正是塞茜尔的出色才能。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "呵呵，那孩子会走上\x01",
            "护士这条道路，\x01",
            "或许也是因为女神的指引呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_343E")

    Jump("loc_356E")

    label("loc_3443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_356E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3526")

    #C0126
    ChrTalk(
        0xFE,
        (
            "赛兰德教授\x01",
            "在雷米菲利亚\x01",
            "相当有名。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "她在医学领域拥有博士称号，\x01",
            "据说和大公家族的关系也很深厚。\x01",
            "身份方面可以说是有保证的。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "更重要的是，我很欣赏\x01",
            "她那种沉着冷静的态度，\x01",
            "现代女性就应该那样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_356E")

    label("loc_3526")


    #C0129
    ChrTalk(
        0xFE,
        (
            "我很欣赏\x01",
            "赛兰德教授那种\x01",
            "沉着冷静的态度。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "现代女性就应该那样。\x02",
    )

    CloseMessageWindow()

    label("loc_356E")

    TalkEnd(0xFE)
    Return()

    # Function_7_2780 end

    def Function_8_3572(): pass

    label("Function_8_3572")

    OP_4B(0xA, 0xFF)
    OP_4B(0x17, 0xFF)

    #C0131
    ChrTalk(
        0x17,
        (
            "难得有机会去看\x01",
            "彩虹剧团的表演，\x01",
            "竟然遇到了列车事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x17,
        "呜呜，好可惜……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "啊，说起来，\x01",
            "明天有新版舞剧的公演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "至少得活着才有的看。\x01",
            "应该感谢女神\x01",
            "让你得救才对。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x17, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x17, 0xFF)
    Return()

    # Function_8_3572 end

    def Function_9_3643(): pass

    label("Function_9_3643")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0135
    ChrTalk(
        0xA,
        (
            "你这孩子真是的……\x01",
            "同样的错误，到底要犯几次啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "呜～我都说过了，\x01",
            "这次真的没出差错嘛～！\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "肯定是因为哪里搞错了，\x01",
            "才会出现这种问题～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_3643 end

    def Function_10_36EA(): pass

    label("Function_10_36EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3713")
    Call(0, 52)
    Return()

    label("loc_3713")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3773")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3731")
    Call(0, 12)
    Jump("loc_376E")

    label("loc_3731")


    #C0138
    ChrTalk(
        0xFE,
        (
            "嘿嘿，因为很像，所以搞错了。\x01",
            "仔细看看，原来大小不同呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376E")

    Jump("loc_3AD2")

    label("loc_3773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_37B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378E")
    Call(0, 12)
    Jump("loc_37B2")

    label("loc_378E")


    #C0139
    ChrTalk(
        0xFE,
        (
            "市里的巴乔\x01",
            "和父母\x01",
            "都没事吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B2")

    Jump("loc_3AD2")

    label("loc_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_37C5")
    Jump("loc_3AD2")

    label("loc_37C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_37D3")
    Jump("loc_3AD2")

    label("loc_37D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3884")

    #C0140
    ChrTalk(
        0xFE,
        (
            "……我还是第一次看到\x01",
            "那么多伤员被送进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "大家好像都很痛苦……\x01",
            "最近这段时间，我都不敢\x01",
            "一个人待着了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "今天晚上也拜托\x01",
            "梅菲尔来陪我吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38E9")

    label("loc_3884")


    #C0143
    ChrTalk(
        0xFE,
        (
            "……我还是第一次看到\x01",
            "那么多伤员被送进来，\x01",
            "总觉得好可怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "今天晚上也拜托\x01",
            "梅菲尔来陪我吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E9")

    Jump("loc_3AD2")

    label("loc_38EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38FC")
    Jump("loc_3AD2")

    label("loc_38FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3921")
    Call(0, 9)
    Jump("loc_3960")

    label("loc_3921")


    #C0145
    ChrTalk(
        0xFE,
        (
            "我都说过了，这一定是\x01",
            "哪里搞错了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "呜～相信我啊～！\x02",
    )

    CloseMessageWindow()

    label("loc_3960")

    Jump("loc_3A97")

    label("loc_3965")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A39")

    #C0147
    ChrTalk(
        0xFE,
        (
            "嘿嘿，影丸的挂饰……\x01",
            "终于送来了～\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        (
            "#00202F影丸很可爱呢……\x01",
            "我也很喜欢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0149
    ChrTalk(
        0xFE,
        (
            "没错～☆\x01",
            "看～很可爱吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        "……喂，你有没有在听我说话啊！？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TurnDirection(0xFE, 0xA, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_3A93")

    label("loc_3A39")


    #C0151
    ChrTalk(
        0xFE,
        (
            "呜呜，玛萨护士长，\x01",
            "你也看看嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "影丸的挂饰\x01",
            "超可爱的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        "谁要看什么挂饰啊！\x02",
    )

    CloseMessageWindow()

    label("loc_3A93")

    OP_4C(0xA, 0xFF)

    label("loc_3A97")

    Jump("loc_3AD2")

    label("loc_3A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AAA")
    Jump("loc_3AD2")

    label("loc_3AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3AB8")
    Jump("loc_3AD2")

    label("loc_3AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AC6")
    Jump("loc_3AD2")

    label("loc_3AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3AD2")
    Call(0, 11)

    label("loc_3AD2")

    TalkEnd(0xFE)
    Return()

    # Function_10_36EA end

    def Function_11_3AD6(): pass

    label("Function_11_3AD6")

    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x10, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC8")

    #C0154
    ChrTalk(
        0xB,
        "来，打点滴了哦～\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x10,
        (
            "呜……护士小姐，\x01",
            "今天没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10,
        (
            "要是你再扎错地方，\x01",
            "让血一下子喷出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "讨厌啦，我上次只是\x01",
            "手抖了一下而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "呵呵，请放心吧，\x01",
            "这次多半没问题！\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x10,
        "（太、太不放心了……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_3C11")

    label("loc_3BC8")


    #C0160
    ChrTalk(
        0xB,
        (
            "……咦？\x01",
            "我好像忘带注射器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x10,
        "拜、拜托你靠谱点啊，护士小姐……\x02",
    )

    CloseMessageWindow()

    label("loc_3C11")

    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_11_3AD6 end

    def Function_12_3C1A(): pass

    label("Function_12_3C1A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CD4")

    #C0162
    ChrTalk(
        0xC,
        (
            "好，希伦，我们分头去给\x01",
            "住院患者们量体温吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        "好的，梅菲尔！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xC,
        "体温计带了吧！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        "带了¤在这里哦。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "……你拿的那个\x01",
            "不是温度计吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xB,
        "……咦咦？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D82")

    label("loc_3CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3D82")

    #C0168
    ChrTalk(
        0xB,
        (
            "梅菲尔，\x01",
            "发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        "我有点害怕……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        "市里好像出大事了。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "不过，不必担心。\x01",
            "我们现在只要做好自己\x01",
            "力所能及的事就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        "嗯、嗯……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_3D82")

    SetScenarioFlags(0x3, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_3C1A end

    def Function_13_3D8E(): pass

    label("Function_13_3D8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAC")
    Call(0, 12)
    Jump("loc_3DDF")

    label("loc_3DAC")


    #C0173
    ChrTalk(
        0xFE,
        (
            "完全就是两种东西啊！\x01",
            "……唉，真是服了这孩子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DDF")

    Jump("loc_40C5")

    label("loc_3DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3E52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFF")
    Call(0, 12)
    Jump("loc_3E4D")

    label("loc_3DFF")


    #C0174
    ChrTalk(
        0xFE,
        (
            "虽然的确\x01",
            "发生了大事……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "但现在最重要的，\x01",
            "还是做好自己力所能及的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E4D")

    Jump("loc_40C5")

    label("loc_3E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3E60")
    Jump("loc_40C5")

    label("loc_3E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3E6E")
    Jump("loc_40C5")

    label("loc_3E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F10")

    #C0176
    ChrTalk(
        0xFE,
        (
            "住进２０２号室的那几个孩子，\x01",
            "一开始耀武扬威的，\x01",
            "但没过多久就消沉起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "好像不光是受伤的缘故，\x01",
            "市里到底发生了什么事呢……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F56")

    label("loc_3F10")


    #C0178
    ChrTalk(
        0xFE,
        (
            "说起来，希伦最近\x01",
            "总是胆怯不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "唉，我们今后\x01",
            "将会怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F56")

    Jump("loc_40C5")

    label("loc_3F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F69")
    Jump("loc_40C5")

    label("loc_3F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3F77")
    Jump("loc_40C5")

    label("loc_3F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F85")
    Jump("loc_40C5")

    label("loc_3F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F93")
    Jump("loc_40C5")

    label("loc_3F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_40BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4052")

    #C0180
    ChrTalk(
        0xFE,
        (
            "希伦那家伙，之前\x01",
            "跑到楼顶上晒太阳。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "而且还把晒干的床单包在身上，\x01",
            "一脸幸福的样子……\x01",
            "真是受不了她。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "……啊，我有不好的预感。\x01",
            "她也许又会做出那种事……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40B7")

    label("loc_4052")


    #C0183
    ChrTalk(
        0xFE,
        (
            "希伦那家伙，之前\x01",
            "跑到楼顶上晒太阳。\x01",
            "而且还弄脏了床单……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "……保险起见，待会\x01",
            "去看看情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B7")

    Jump("loc_40C5")

    label("loc_40BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40C5")

    label("loc_40C5")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D8E end

    def Function_14_40C9(): pass

    label("Function_14_40C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_41F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418D")

    #C0185
    ChrTalk(
        0xFE,
        (
            "查完病房以后，\x01",
            "还有手术要做。\x01",
            "……哎呀呀，真是忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "不过，无论其它地方发生了什么情况，\x01",
            "我们该做的事情都不会改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "救助眼前的患者……\x01",
            "就是医生的职责。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_41EF")

    label("loc_418D")


    #C0188
    ChrTalk(
        0xFE,
        (
            "无论在哪里发生什么情况，\x01",
            "我们该做的事情都不会改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "救助眼前的患者……\x01",
            "就是医生的职责。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41EF")

    Jump("loc_498B")

    label("loc_41F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420F")
    Call(0, 15)
    Jump("loc_423E")

    label("loc_420F")


    #C0190
    ChrTalk(
        0xFE,
        (
            "我们医院的工作人员都很优秀。\x01",
            "请不必担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_423E")

    Jump("loc_498B")

    label("loc_4243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4254")
    Call(0, 41)
    Jump("loc_498B")

    label("loc_4254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_43FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_434F")

    #C0191
    ChrTalk(
        0xFE,
        (
            "之前住院的警察\x01",
            "和不良团伙的年轻人们\x01",
            "已经出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "出院之后，本应定期\x01",
            "再来医院复查几次……\x01",
            "但由于禁行令的限制，也只能作罢。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "身为医生，却要被迫采取这种\x01",
            "不负责任的处理方式……\x01",
            "如今这种情况，真是让人不得不质疑啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_43F7")

    label("loc_434F")


    #C0194
    ChrTalk(
        0xFE,
        (
            "出院的患者本应定期\x01",
            "再来医院复查几次，\x01",
            "但由于禁行令的限制，也只能作罢。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "身为医生，却要被迫采取这种\x01",
            "不负责任的处理方式……\x01",
            "如今这种情况，真是让人不得不质疑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F7")

    Jump("loc_498B")

    label("loc_43FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_451A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44BB")

    #C0196
    ChrTalk(
        0xFE,
        (
            "相比身体所受的伤，他们所负的\x01",
            "心灵创伤似乎更加严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "疾病和伤势都需要患者用心来治愈，\x01",
            "自暴自弃的心情\x01",
            "将会影响身体的痊愈。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "希望他们能\x01",
            "努力振作起来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4515")

    label("loc_44BB")


    #C0199
    ChrTalk(
        0xFE,
        (
            "相比身体所受的伤，他们所负的\x01",
            "心灵创伤似乎更加严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "希望他们能\x01",
            "努力振作起来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4515")

    Jump("loc_498B")

    label("loc_451A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4572")

    #C0201
    ChrTalk(
        0xFE,
        (
            "……骨折的腿\x01",
            "已经处理好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "这种伤势不会危及生命，\x01",
            "请保持冷静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_498B")

    label("loc_4572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464C")

    #C0203
    ChrTalk(
        0xFE,
        (
            "外科医学在诞生之初，\x01",
            "曾被无数人大加指责，\x01",
            "说什么『切割人体，简直荒唐无稽』……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "不过，大家最近好像\x01",
            "越来越接受它了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "多亏伟大的前辈们用成功\x01",
            "揭示了它的实用性，\x01",
            "必须要感谢他们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_46B9")

    label("loc_464C")


    #C0206
    ChrTalk(
        0xFE,
        (
            "大家最近好像越来越能\x01",
            "接受外科手术了。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "多亏伟大的前辈们用成功\x01",
            "揭示了它的实用性，\x01",
            "必须要感谢他们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B9")

    Jump("loc_498B")

    label("loc_46BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_485F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E4")

    #C0208
    ChrTalk(
        0xFE,
        (
            "小滴的症状涉及外科、\x01",
            "内科，以及神经科的各种问题，\x01",
            "非常复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "虽说很难完全治愈，\x01",
            "但她并没有彻底失明，\x01",
            "因此可以说，仍然留有一线希望。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……从某种意义上来说，\x01",
            "追求微小的希望\x01",
            "比放弃要更辛苦、更艰难。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "但即使如此，那对父女也始终没有放弃，\x01",
            "令我深感敬佩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_485A")

    label("loc_47E4")


    #C0212
    ChrTalk(
        0xFE,
        (
            "……从某种意义上来说，追求微小的\x01",
            "希望是非常辛苦艰难的。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "但即使如此，那对父女也始终没有放弃，\x01",
            "令我深感敬佩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_485A")

    Jump("loc_498B")

    label("loc_485F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_486D")
    Jump("loc_498B")

    label("loc_486D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4982")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_491D")

    #C0214
    ChrTalk(
        0xFE,
        (
            "约亚西姆的事情令患者\x01",
            "对医院的信任一度下降……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "但我们医生的职责就是\x01",
            "以真挚的态度救助患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "只要保持这种姿态，\x01",
            "就一定能恢复患者的信赖。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_497D")

    label("loc_491D")


    #C0217
    ChrTalk(
        0xFE,
        (
            "我们医生的职责就是\x01",
            "以真挚的态度救助患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "只要保持这种姿态，\x01",
            "就一定能恢复患者的信赖。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_497D")

    Jump("loc_498B")

    label("loc_4982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_498B")

    label("loc_498B")

    TalkEnd(0xFE)
    Return()

    # Function_14_40C9 end

    def Function_15_498F(): pass

    label("Function_15_498F")

    OP_4B(0xD, 0xFF)
    OP_4B(0x2C, 0xFF)

    #C0219
    ChrTalk(
        0x2C,
        (
            "医生……听说药的\x01",
            "种类不够，\x01",
            "没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xD,
        (
            "……医院的全体职员现在\x01",
            "都在尽力思索对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xD,
        (
            "本院的工作人员都很优秀，\x01",
            "请不必担心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 5)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x2C, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0x2C, 0xFF)
    Return()

    # Function_15_498F end

    def Function_16_4A33(): pass

    label("Function_16_4A33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A44")
    Jump("loc_4CF7")

    label("loc_4A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A52")
    Jump("loc_4CF7")

    label("loc_4A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A60")
    Jump("loc_4CF7")

    label("loc_4A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A6E")
    Jump("loc_4CF7")

    label("loc_4A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C5D")

    #C0222
    ChrTalk(
        0xFE,
        (
            "我让利顿去２０２号病房查房，\x01",
            "现在已经超过预定时间１分１４秒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "我这边都已经查完了，\x01",
            "他还真是靠不住啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00006F我、我之前就想说……\x01",
            "教授，您对时间的要求\x01",
            "真是出奇的严格啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "医疗现场就是这样的世界，\x01",
            "一分一秒都会左右患者的生死。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "为了拯救更多的生命，\x01",
            "严守时间、按计划行动\x01",
            "是理所当然的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x103,
        (
            "#00200F的确……\x01",
            "这些话或许也适用于\x01",
            "其它所有职业呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "当然，为此必须要\x01",
            "掌握高度的技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "……希望那些\x01",
            "年轻医生们将来也能\x01",
            "迅速、完美地完成工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4CDB")

    label("loc_4C5D")


    #C0230
    ChrTalk(
        0xFE,
        (
            "为了拯救更多的生命，\x01",
            "严守时间、按计划行动\x01",
            "是理所当然的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "……希望那些\x01",
            "年轻医生们将来也能\x01",
            "迅速、完美地完成工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDB")

    Jump("loc_4CF7")

    label("loc_4CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4CEE")
    Jump("loc_4CF7")

    label("loc_4CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4CF7")

    label("loc_4CF7")

    TalkEnd(0xFE)
    Return()

    # Function_16_4A33 end

    def Function_17_4CFB(): pass

    label("Function_17_4CFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D5D")

    #C0232
    ChrTalk(
        0xFE,
        (
            "赛兰德医生\x01",
            "真是了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "虽然言辞严厉，\x01",
            "但在为患者诊断时\x01",
            "却体贴入微。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E1E")

    label("loc_4D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4DC2")

    #C0234
    ChrTalk(
        0xFE,
        (
            "这里的病号餐很不错，\x01",
            "非常讲究\x01",
            "营养均衡。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "多亏如此，我在手术\x01",
            "之后恢复得很好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E1E")

    label("loc_4DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E1E")

    #C0236
    ChrTalk(
        0xFE,
        (
            "这家医院的\x01",
            "护士小姐和医生们\x01",
            "都非常亲切。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "我对这里的住院生活\x01",
            "十分满意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E1E")

    TalkEnd(0xFE)
    Return()

    # Function_17_4CFB end

    def Function_18_4E22(): pass

    label("Function_18_4E22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E8B")

    #C0238
    ChrTalk(
        0xFE,
        (
            "那位女医生，感觉\x01",
            "好像很凶啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "抱怨一下就被她瞪，\x01",
            "在出院之前，还是老实点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EEC")

    label("loc_4E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4EE0")

    #C0240
    ChrTalk(
        0xFE,
        "啊～好想早点出院啊。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "我已经受够朴素的餐点了。\x01",
            "好想吃牛排啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EEC")

    label("loc_4EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4EEC")
    Call(0, 11)

    label("loc_4EEC")

    TalkEnd(0xFE)
    Return()

    # Function_18_4E22 end

    def Function_19_4EF0(): pass

    label("Function_19_4EF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F58")

    #C0242
    ChrTalk(
        0xFE,
        (
            "（削皮）……\x01",
            "我正在削\x01",
            "孙子送来的苹果。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "呵呵，不介意的话，\x01",
            "你们要不要一起吃？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50AB")

    label("loc_4F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_502F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE0")

    #C0244
    ChrTalk(
        0xFE,
        (
            "我记得市里今天\x01",
            "要举行揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "好想看看\x01",
            "传说中的兰花塔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "算啦，就把它当作\x01",
            "出院之后的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_502A")

    label("loc_4FE0")


    #C0247
    ChrTalk(
        0xFE,
        (
            "好想看看\x01",
            "传说中的兰花塔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "算啦，就把它当作\x01",
            "出院之后的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_502A")

    Jump("loc_50AB")

    label("loc_502F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50AB")

    #C0249
    ChrTalk(
        0xFE,
        (
            "听说这家医院的某位医生\x01",
            "引发了一起重大事件，\x01",
            "一时间闹得沸沸扬扬……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "不过，这家医院很好嘛，\x01",
            "害我白担心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50AB")

    TalkEnd(0xFE)
    Return()

    # Function_19_4EF0 end

    def Function_20_50AF(): pass

    label("Function_20_50AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_510A")

    #C0251
    ChrTalk(
        0xFE,
        "哦哦，真的吗？\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "呼，总算放心了。\x01",
            "我得早点治好，\x01",
            "回去工作才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5239")

    label("loc_510A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_51DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519C")

    #C0253
    ChrTalk(
        0xFE,
        (
            "同事们在百忙之中\x01",
            "还来看望我。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "叫我不要在意工作的事，\x01",
            "专心治疗伤势。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "说的也有道理，现在把\x01",
            "工作先忘掉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_51DA")

    label("loc_519C")


    #C0256
    ChrTalk(
        0xFE,
        (
            "暂时忘掉\x01",
            "工作方面的事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "现在必须要\x01",
            "专心治疗伤势。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DA")

    Jump("loc_5239")

    label("loc_51DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5239")

    #C0258
    ChrTalk(
        0xFE,
        (
            "我的腿在交通\x01",
            "事故中骨折了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "还有重要的工作呢，\x01",
            "真是伤脑筋啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5239")

    TalkEnd(0xFE)
    Return()

    # Function_20_50AF end

    def Function_21_523D(): pass

    label("Function_21_523D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_52A9")

    #C0260
    ChrTalk(
        0xFE,
        (
            "医院的病床\x01",
            "一下就满员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "听说发生了很严重的事故，\x01",
            "没有出现死难者，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5415")

    label("loc_52A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5329")

    #C0262
    ChrTalk(
        0xFE,
        (
            "不知留在家里的老公\x01",
            "有没有让孩子们吃好，\x01",
            "真是不放心啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "不过他最近一直在\x01",
            "努力学习做饭，\x01",
            "应该不用担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5415")

    label("loc_5329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C9")

    #C0264
    ChrTalk(
        0xFE,
        (
            "我的手术并不大，\x01",
            "所以住院时间应该也不会太长。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "不过，离开了家，\x01",
            "终究还是很担心家人……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "老公和孩子们\x01",
            "有没有好好吃饭呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5415")

    label("loc_53C9")


    #C0267
    ChrTalk(
        0xFE,
        (
            "离开了家，\x01",
            "终究还是很担心家人……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "老公和孩子们\x01",
            "有没有好好吃饭呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5415")

    TalkEnd(0xFE)
    Return()

    # Function_21_523D end

    def Function_22_5419(): pass

    label("Function_22_5419")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_547F")

    #C0269
    ChrTalk(
        0xFE,
        (
            "没想到竟然会发生\x01",
            "列车脱轨事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "最近的负面事件\x01",
            "接连不断啊，\x01",
            "真是不太平。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564D")

    label("loc_547F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_55FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5574")

    #C0271
    ChrTalk(
        0xFE,
        (
            "住院时，我为了换换心情，\x01",
            "把今年出版的克洛斯贝尔时代周刊\x01",
            "从第一期开始，全部重看了一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "暗杀麦克道尔前市长未遂事件、\x01",
            "创立纪念庆典，以及那起教团事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "仔细想想，在这半年多的时间里，\x01",
            "真是发生了很多事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_55F5")

    label("loc_5574")


    #C0274
    ChrTalk(
        0xFE,
        (
            "暗杀麦克道尔前市长未遂事件、\x01",
            "教团事件、恐怖分子\x01",
            "袭击兰花塔事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "仔细想想，在这半年多的时间里，\x01",
            "真是发生了很多事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55F5")

    Jump("loc_564D")

    label("loc_55FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_564D")

    #C0276
    ChrTalk(
        0xFE,
        (
            "在住院期间，\x01",
            "总会闲得无聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "不然就把存了很久的书\x01",
            "一口气看完吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_564D")

    TalkEnd(0xFE)
    Return()

    # Function_22_5419 end

    def Function_23_5651(): pass

    label("Function_23_5651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_56D3")

    #C0278
    ChrTalk(
        0xFE,
        (
            "能够把这么多患者\x01",
            "顺利治好，\x01",
            "医生们真是了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "只要有乌尔斯拉医院在，\x01",
            "克洛斯贝尔的居民就可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57B0")

    label("loc_56D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56EE")
    Call(0, 39)
    Jump("loc_5740")

    label("loc_56EE")


    #C0280
    ChrTalk(
        0xFE,
        (
            "利顿医生很年轻，\x01",
            "我一开始还有点担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "不过，他真是一位\x01",
            "很可靠的医生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5740")

    Jump("loc_57B0")

    label("loc_5745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57B0")

    #C0282
    ChrTalk(
        0xFE,
        (
            "贝尔达因医生的诊断\x01",
            "非常仔细，真是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "能让那么高明的医生给自己\x01",
            "治疗，我可真是幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B0")

    TalkEnd(0xFE)
    Return()

    # Function_23_5651 end

    def Function_24_57B4(): pass

    label("Function_24_57B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5855")

    #C0284
    ChrTalk(
        0xFE,
        (
            "竟然因为列车事故而住院，\x01",
            "真是可怜……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "和因为闪到腰而住院的我\x01",
            "一样可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "……怎么？看你那表情，\x01",
            "好像有什么话要说？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_58C6")

    label("loc_5855")


    #C0287
    ChrTalk(
        0xFE,
        (
            "竟然因为列车事故而住院，\x01",
            "和因为闪到腰而住院的我\x01",
            "一样可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "……怎么？看你那表情，\x01",
            "好像有什么话要说？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C6")

    Jump("loc_5A74")

    label("loc_58CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597F")

    #C0289
    ChrTalk(
        0xFE,
        "……昨天，我的朋友来看望我了。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "因为闪到腰而住院，\x01",
            "实在是太丢人了，\x01",
            "所以我并没有告诉任何人……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "一定是妈妈说出去的。\x01",
            "真过分……太过分了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5A04")

    label("loc_597F")


    #C0292
    ChrTalk(
        0xFE,
        (
            "因为闪到腰而住院，\x01",
            "实在是太丢人了，\x01",
            "所以我并没有告诉任何人……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "不过，有人来看望自己，感觉还是\x01",
            "挺开心的，就不计较那么多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A04")

    Jump("loc_5A74")

    label("loc_5A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5A74")

    #C0294
    ChrTalk(
        0xFE,
        (
            "啊啊，我这年轻娇嫩的少女\x01",
            "竟然会受伤住院。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "而且还是因为闪到腰……\x01",
            "真丢人……太丢人了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A74")

    TalkEnd(0xFE)
    Return()

    # Function_24_57B4 end

    def Function_25_5A78(): pass

    label("Function_25_5A78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5AED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A96")
    Call(0, 8)
    Jump("loc_5AED")

    label("loc_5A96")


    #C0296
    ChrTalk(
        0xFE,
        (
            "虽然得救了，但观看彩虹剧团\x01",
            "演出的难得机会却白白浪费掉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "呜呜，好可惜……\x02",
    )

    CloseMessageWindow()

    label("loc_5AED")

    TalkEnd(0xFE)
    Return()

    # Function_25_5A78 end

    def Function_26_5AF1(): pass

    label("Function_26_5AF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B55")

    #C0298
    ChrTalk(
        0xFE,
        (
            "列车翻车的时候，\x01",
            "我还以为彻底完蛋了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "短时间内，我恐怕是\x01",
            "不敢再坐列车了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B55")

    TalkEnd(0xFE)
    Return()

    # Function_26_5AF1 end

    def Function_27_5B59(): pass

    label("Function_27_5B59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5BA0")

    #C0300
    ChrTalk(
        0xFE,
        (
            "好痛好痛好痛……！\x01",
            "要、要死了！我要死了！啊啊啊……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BA0")

    TalkEnd(0xFE)
    Return()

    # Function_27_5B59 end

    def Function_28_5BA4(): pass

    label("Function_28_5BA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C23")

    #C0301
    ChrTalk(
        0xFE,
        (
            "……对面那个人，身为男子汉，\x01",
            "却大呼小叫的，真是吵啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "好不容易才从事故中\x01",
            "生还，这点小小的痛楚\x01",
            "还不忍忍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C23")

    TalkEnd(0xFE)
    Return()

    # Function_28_5BA4 end

    def Function_29_5C27(): pass

    label("Function_29_5C27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD5")

    #C0303
    ChrTalk(
        0xFE,
        (
            "面对『赤色星座』的战斗力，\x01",
            "我们真是毫无\x01",
            "还手之力。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "这恐怕会给市民们带来\x01",
            "强烈的不安吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "我们警察竟然如此无能……\x01",
            "实在是羞愧啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5D32")

    label("loc_5CD5")


    #C0306
    ChrTalk(
        0xFE,
        (
            "面对『赤色星座』的战斗力，\x01",
            "我们真是毫无\x01",
            "还手之力。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "希望多诺邦警督\x01",
            "也能恢复健康……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D32")

    TalkEnd(0xFE)
    Return()

    # Function_29_5C27 end

    def Function_30_5D36(): pass

    label("Function_30_5D36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD0")

    #C0308
    ChrTalk(
        0xFE,
        (
            "芙兰小姐在接待员的\x01",
            "工作中给了我们这些\x01",
            "警官很多鼓励。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "她能够恢复意识，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        "#10100F……谢谢你的关心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_5E17")

    label("loc_5DD0")


    #C0311
    ChrTalk(
        0xFE,
        (
            "芙兰小姐\x01",
            "能够恢复意识，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "希望她能早日\x01",
            "恢复健康。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E17")

    TalkEnd(0xFE)
    Return()

    # Function_30_5D36 end

    def Function_31_5E1B(): pass

    label("Function_31_5E1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9A")

    #C0313
    ChrTalk(
        0xFE,
        (
            "连接待员芙兰小姐\x01",
            "都受了重伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "可恶……！\x01",
            "我们在警察学校刻苦训练，\x01",
            "到底是为了什么……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_5F08")

    label("loc_5E9A")


    #C0315
    ChrTalk(
        0xFE,
        (
            "可恶……！\x01",
            "我们在警察学校刻苦训练，\x01",
            "到底是为了什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "连芙兰小姐\x01",
            "都受了重伤，\x01",
            "我们真是太没用了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F08")

    TalkEnd(0xFE)
    Return()

    # Function_31_5E1B end

    def Function_32_5F0C(): pass

    label("Function_32_5F0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5F74")

    #C0317
    ChrTalk(
        0xFE,
        (
            "那些猎兵驯养的魔兽\x01",
            "饱经训练，十分凶悍……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "要是再被那种魔兽袭击，\x01",
            "一定会没命的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F74")

    TalkEnd(0xFE)
    Return()

    # Function_32_5F0C end

    def Function_33_5F78(): pass

    label("Function_33_5F78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5FD8")

    #C0319
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥……\x01",
            "你不惜变成那种样子，\x01",
            "也要变强吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "可恶，真是搞不懂啊……\x02",
    )

    CloseMessageWindow()

    label("loc_5FD8")

    TalkEnd(0xFE)
    Return()

    # Function_33_5F78 end

    def Function_34_5FDC(): pass

    label("Function_34_5FDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_60B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6069")

    #C0321
    ChrTalk(
        0xFE,
        (
            "无论他有什么难处，也不该……\x01",
            "总之，那种人\x01",
            "已经不是我们的首领了。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "或者说，剑蛇帮……\x01",
            "也已经完蛋了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_60B9")

    label("loc_6069")


    #C0323
    ChrTalk(
        0xFE,
        (
            "那种人……\x01",
            "已经不是我们的首领了。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "或者说，剑蛇帮……\x01",
            "也已经完蛋了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B9")

    TalkEnd(0xFE)
    Return()

    # Function_34_5FDC end

    def Function_35_60BD(): pass

    label("Function_35_60BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_61F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A0")

    #C0325
    ChrTalk(
        0xFE,
        (
            "我们还好，只是骨折而已……\x01",
            "但寇奇那家伙却身受重伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "刚到医院，就被送进了\x01",
            "集中治疗室……\x01",
            "现在正在研究楼里接受治疗。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "听说他直到现在\x01",
            "都没有恢复意识……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "可恶，为什么\x01",
            "会这样啊……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_61F5")

    label("loc_61A0")


    #C0329
    ChrTalk(
        0xFE,
        (
            "斯拉修那家伙\x01",
            "也被吓坏了，\x01",
            "已经不能好好说话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "可恶，为什么\x01",
            "会这样啊……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61F5")

    TalkEnd(0xFE)
    Return()

    # Function_35_60BD end

    def Function_36_61F9(): pass

    label("Function_36_61F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6230")

    #C0331
    ChrTalk(
        0xFE,
        (
            "（颤抖）……\x01",
            "怪、怪物……怪物来了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6230")

    TalkEnd(0xFE)
    Return()

    # Function_36_61F9 end

    def Function_37_6234(): pass

    label("Function_37_6234")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6299")

    #C0332
    ChrTalk(
        0xFE,
        (
            "好了，接下来\x01",
            "要打扫\x01",
            "护士中心……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "……这里是女性专用的地方，\x01",
            "我总觉得有点紧张。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6299")

    TalkEnd(0xFE)
    Return()

    # Function_37_6234 end

    def Function_38_629D(): pass

    label("Function_38_629D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_62AE")
    Jump("loc_653E")

    label("loc_62AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_62BC")
    Jump("loc_653E")

    label("loc_62BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_62CD")
    Call(0, 41)
    Jump("loc_653E")

    label("loc_62CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E8")
    Call(0, 40)
    Jump("loc_634E")

    label("loc_62E8")


    #C0334
    ChrTalk(
        0xFE,
        (
            "可以出院的患者们\x01",
            "也无法自由\x01",
            "回到市里。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "虽说是为了防备\x01",
            "郊外的『幻兽』，\x01",
            "但这未免也太严格了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_634E")

    Jump("loc_653E")

    label("loc_6353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_646C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63DD")

    #C0336
    ChrTalk(
        0xFE,
        (
            "受伤的警察就住在\x01",
            "这间病房。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "除了那位二科的警督，\x01",
            "其他人伤得并不重。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "住院期间应该\x01",
            "也不会太长的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_6467")

    label("loc_63DD")


    #C0339
    ChrTalk(
        0xFE,
        (
            "那位二科的警督……\x01",
            "虽然还没恢复意识，\x01",
            "但应该已经过了危险期。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "他好像住在三楼的３０２号\x01",
            "病房。如果想要探望他，\x01",
            "你们可以直接过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6467")

    Jump("loc_653E")

    label("loc_646C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_647A")
    Jump("loc_653E")

    label("loc_647A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_64C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6495")
    Call(0, 39)
    Jump("loc_64C0")

    label("loc_6495")


    #C0341
    ChrTalk(
        0xFE,
        (
            "利顿『医生』吗……\x01",
            "嗯……真好听啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C0")

    Jump("loc_653E")

    label("loc_64C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_64D3")
    Jump("loc_653E")

    label("loc_64D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6527")

    #C0342
    ChrTalk(
        0xFE,
        (
            "哦，骨头已经\x01",
            "基本接好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "再稍微忍耐一下，\x01",
            "就可以走路了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_653E")

    label("loc_6527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6535")
    Jump("loc_653E")

    label("loc_6535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_653E")

    label("loc_653E")

    TalkEnd(0xFE)
    Return()

    # Function_38_629D end

    def Function_39_6542(): pass

    label("Function_39_6542")

    OP_4B(0x24, 0xFF)

    #C0344
    ChrTalk(
        0x24,
        (
            "嗯，恢复得很顺利。\x01",
            "这样看来，\x01",
            "马上出院都没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x15,
        (
            "是吗？\x01",
            "那真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x15,
        (
            "呵呵，利顿医生\x01",
            "也很可靠呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x24,
        (
            "哎，是、是吗？\x01",
            "哈哈……真难为情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 0)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x24, 0xFF)
    Return()

    # Function_39_6542 end

    def Function_40_65F9(): pass

    label("Function_40_65F9")

    OP_4B(0x24, 0xFF)
    OP_4B(0x26, 0xFF)

    #C0348
    ChrTalk(
        0x24,
        "嗯，手术之后，恢复得很顺利呢。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x24,
        (
            "本可以让您立刻出院，\x01",
            "但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x26,
        (
            "哦，我听说了，\x01",
            "好像正在实施禁行令吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x26,
        (
            "哎呀呀，看来也只能\x01",
            "再住一阵子院了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 3)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x26, 0x10)
    OP_4C(0x24, 0xFF)
    OP_4C(0x26, 0xFF)
    Return()

    # Function_40_65F9 end

    def Function_41_66B2(): pass

    label("Function_41_66B2")

    OP_4B(0x24, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67EE")

    #C0352
    ChrTalk(
        0xD,
        (
            "虽然医院得到了\x01",
            "总统的援助……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xD,
        (
            "但患者们的不安情绪\x01",
            "还是相当严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x24,
        (
            "嗯，急救车的往来\x01",
            "也受到了严格的限制……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x24,
        (
            "说不定，正是我这种\x01",
            "实习医生把不安情绪\x01",
            "传染给了患者们。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xD,
        (
            "在这种情况下，就算不是实习医生，\x01",
            "也还是会感到不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "……不管怎么说，\x01",
            "我们要想办法\x01",
            "把患者们安抚好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 2)
    Jump("loc_6864")

    label("loc_67EE")


    #C0358
    ChrTalk(
        0x24,
        (
            "贝尔达因医生\x01",
            "竟然也会\x01",
            "感到不安啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        "谁都会感到不安的。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xD,
        (
            "……不管怎么说，\x01",
            "我们要想办法\x01",
            "把患者们安抚好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6864")

    OP_4C(0x24, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_41_66B2 end

    def Function_42_686D(): pass

    label("Function_42_686D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_687E")
    Jump("loc_6AE0")

    label("loc_687E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_688C")
    Jump("loc_6AE0")

    label("loc_688C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_689A")
    Jump("loc_6AE0")

    label("loc_689A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_69DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697C")

    #C0361
    ChrTalk(
        0xFE,
        (
            "对于小滴的手术结果，\x01",
            "大家抱持着不同的看法……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "之前完全没有恢复迹象的\x01",
            "眼部功能能够有点改善，\x01",
            "这就已经很好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "不管怎么说，总算踏出了\x01",
            "治疗的第一步嘛。\x01",
            "接下来，还需要医院的各位一起努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_69D9")

    label("loc_697C")


    #C0364
    ChrTalk(
        0xFE,
        (
            "小滴总算踏出了\x01",
            "治疗的第一步，\x01",
            "这就已经很好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "……不过，患者应该\x01",
            "还是很不安吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69D9")

    Jump("loc_6AE0")

    label("loc_69DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_69EC")
    Jump("loc_6AE0")

    label("loc_69EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6AD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A83")

    #C0366
    ChrTalk(
        0xFE,
        (
            "赛兰德教授\x01",
            "年纪轻轻，\x01",
            "却相当有风度。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "我理想中的『优秀女医生』，\x01",
            "正是像她这样的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "我必须要向她\x01",
            "好好学习。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_6AD2")

    label("loc_6A83")


    #C0369
    ChrTalk(
        0xFE,
        (
            "赛兰德教授\x01",
            "正是我理想中的\x01",
            "『优秀女医生』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "我必须要向她\x01",
            "好好学习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AD2")

    Jump("loc_6AE0")

    label("loc_6AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6AE0")

    label("loc_6AE0")

    TalkEnd(0xFE)
    Return()

    # Function_42_686D end

    def Function_43_6AE4(): pass

    label("Function_43_6AE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6B0D")

    #C0371
    ChrTalk(
        0xFE,
        "唉，好想出院啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B4F")

    label("loc_6B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B28")
    Call(0, 40)
    Jump("loc_6B4F")

    label("loc_6B28")


    #C0372
    ChrTalk(
        0xFE,
        (
            "哎呀呀，看来只好\x01",
            "再住院一阵子了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B4F")

    TalkEnd(0xFE)
    Return()

    # Function_43_6AE4 end

    def Function_44_6B53(): pass

    label("Function_44_6B53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6BD7")

    #C0373
    ChrTalk(
        0xFE,
        (
            "虽然我的申请获得了批准，\x01",
            "总算可以回去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "但国防军好像要\x01",
            "过一阵子才会再来。\x01",
            "哎呀呀，只好耐心等待了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C45")

    label("loc_6BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6C45")

    #C0375
    ChrTalk(
        0xFE,
        (
            "出院回市里需要\x01",
            "经过繁琐的申请。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "而且只有等到国防军来巡查的\x01",
            "时候才能回去……\x01",
            "真是让人郁闷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C45")

    TalkEnd(0xFE)
    Return()

    # Function_44_6B53 end

    def Function_45_6C49(): pass

    label("Function_45_6C49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6CA1")

    #C0377
    ChrTalk(
        0xFE,
        (
            "就算表达出对总统的不满，\x01",
            "也没有任何用处。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        "现在也只能忍耐了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D0F")

    label("loc_6CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6D0F")

    #C0379
    ChrTalk(
        0xFE,
        (
            "我对总统有\x01",
            "很多不满。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "但克洛斯贝尔已经独立了，\x01",
            "从某种程度上说，就算满腹牢骚\x01",
            "也是无济于事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D0F")

    TalkEnd(0xFE)
    Return()

    # Function_45_6C49 end

    def Function_46_6D13(): pass

    label("Function_46_6D13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6DB0")

    #C0381
    ChrTalk(
        0xFE,
        (
            "虽然没有和伊莉娅直接说过话，\x01",
            "但她努力接受复健训练的身姿\x01",
            "真是鼓舞人心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "过一阵子回市里之后，\x01",
            "我要把伊莉娅努力的样子\x01",
            "形容给大家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA7")

    label("loc_6DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E85")

    #C0383
    ChrTalk(
        0xFE,
        (
            "伊莉娅也在这家医院住院，\x01",
            "我本来还抱有淡淡的期待，\x01",
            "心想说不定能见到她……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "可是，看到她那一脸专注地\x01",
            "接受复健训练的样子，\x01",
            "无聊的追星想法就立刻消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "……希望她继续加油啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 1)
    Jump("loc_6EA7")

    label("loc_6E85")


    #C0386
    ChrTalk(
        0xFE,
        "伊莉娅……一定要继续加油啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6EA7")

    TalkEnd(0xFE)
    Return()

    # Function_46_6D13 end

    def Function_47_6EAB(): pass

    label("Function_47_6EAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6F10")

    #C0387
    ChrTalk(
        0xFE,
        (
            "唉，好无聊啊。\x01",
            "在医院里又不能\x01",
            "看《热辣宝贝》……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        "就没人能来看望我一下吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F7E")

    label("loc_6F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6F7E")

    #C0389
    ChrTalk(
        0xFE,
        (
            "我因为复杂性骨折\x01",
            "而住进了医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "虽然已经基本好了，\x01",
            "但要回市里似乎也很麻烦，\x01",
            "真让人郁闷啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F7E")

    TalkEnd(0xFE)
    Return()

    # Function_47_6EAB end

    def Function_48_6F82(): pass

    label("Function_48_6F82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6FEB")

    #C0391
    ChrTalk(
        0xFE,
        (
            "出现在东方天空的\x01",
            "那棵蓝白色大树到底是……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "噢，女神啊，\x01",
            "请拯救我们吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7068")

    label("loc_6FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7068")

    #C0393
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔将会变成怎样……\x01",
            "只有女神才会知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "如今惟有向女神祈祷，期盼她\x01",
            "为我们指引能够获得救赎的道路……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7068")

    TalkEnd(0xFE)
    Return()

    # Function_48_6F82 end

    def Function_49_706C(): pass

    label("Function_49_706C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_70E7")

    #C0395
    ChrTalk(
        0xFE,
        (
            "今天就可以出院了，\x01",
            "真是松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "虽然外面的情况比较混乱……\x01",
            "但还是想赶快回家，让家人们放心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7131")

    label("loc_70E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7102")
    Call(0, 15)
    Jump("loc_7131")

    label("loc_7102")


    #C0397
    ChrTalk(
        0xFE,
        (
            "呼，既然医生都那么说了，\x01",
            "应该没问题吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7131")

    TalkEnd(0xFE)
    Return()

    # Function_49_706C end

    def Function_50_7135(): pass

    label("Function_50_7135")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_71A1")

    #C0398
    ChrTalk(
        0xFE,
        "听说送来了大量的门诊患者……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "巡诊的医生们全都忙得不可开交，\x01",
            "希望医生们多加努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7218")

    label("loc_71A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7218")

    #C0400
    ChrTalk(
        0xFE,
        (
            "虽然医院也存在各种各样的问题，\x01",
            "但医生们好像都很努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "不愧是乌尔斯拉医院啊……\x01",
            "我们可以放心住院了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7218")

    TalkEnd(0xFE)
    Return()

    # Function_50_7135 end

    def Function_51_721C(): pass

    label("Function_51_721C")

    Sound(160, 0, 100, 0)
    Return()

    # Function_51_721C end

    def Function_52_7223(): pass

    label("Function_52_7223")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110440, 1000, -3360, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 109780, 0, -3000, 135)
    SetChrPos(0x102, 110740, 0, -3020, 180)
    SetChrPos(0x103, 109190, 0, -4120, 135)
    SetChrPos(0x109, 109950, 0, -1880, 180)
    SetChrPos(0x104, 110150, 0, -580, 180)
    SetChrPos(0x105, 108940, 0, -1070, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0402
    ChrTalk(
        0xA,
        "真是的，你这孩子……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xA,
        (
            "以后能不能不要再犯\x01",
            "下错订单这种低级错误。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xB,
        "唔……这一定是哪里搞错了。\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xB,
        (
            "我写订单的时候，\x01",
            "梅菲尔一直在旁边\x01",
            "仔细盯着我呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xB,
        (
            "但我当时还是把位数\x01",
            "写错了二十多次……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "……唉，可以想象\x01",
            "梅菲尔有多辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#00005F请问……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0409
    ChrTalk(
        0xA,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xA,
        (
            "我让这孩子\x01",
            "下单订购\x01",
            "医疗用品……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xA,
        (
            "但货物送来之后，\x01",
            "里面放的却是个\x01",
            "破旧的人偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xA,
        (
            "这孩子以前也\x01",
            "下错过订单，\x01",
            "买来了一堆莫名其妙的杂货……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xB,
        (
            "呜，相信我嘛，\x01",
            "我这次真的没写错呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x103,
        "#00200F罗伊德前辈，果然……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        "#00003F嗯，确实是发错了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0416
    ChrTalk(
        0xA,
        "怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        "#00012F其实是这样的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0418
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德说明了\x01",
            "送错货物的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0419
    ChrTalk(
        0xA,
        (
            "送错货物……\x01",
            "原来是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x109,
        (
            "#10100F我们现在正在\x01",
            "重新配送货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#00000F寄到医院的货物\x01",
            "应该是这个吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0422
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '沉重货物'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('沉重货物', 1)

    #C0423
    ChrTalk(
        0xA,
        (
            "嗯……这的确是\x01",
            "我让她订购的医疗用具。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xA,
        (
            "谢谢你们\x01",
            "特地送过来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0425
    ChrTalk(
        0xA,
        (
            "还有……\x01",
            "对不起啊，希伦。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xA,
        (
            "看来我这次真的\x01",
            "是错怪你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xB,
        (
            "呵呵，没关系啦，\x01",
            "我根本就不介意。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xB,
        (
            "啊，对了，\x01",
            "那个是不是也在呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0429
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "希伦将手伸进\x01",
            "货物箱里面摸索着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0430
    ChrTalk(
        0xB,
        (
            "啊，有了！\x01",
            "『影丸』的挂饰⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xB,
        (
            "我在下订单时\x01",
            "顺便一起订的。\x01",
            "呵呵，好可爱啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xA,
        (
            "……希伦，我稍后还是要\x01",
            "好好训你一顿。\x02",
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

    #C0433
    ChrTalk(
        0x101,
        (
            "#00006F那、那个……\x02\x03",

            "#00000F不好意思，请问能否把\x01",
            "误送到这里的\x01",
            "货物交给我们？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0434
    ChrTalk(
        0xA,
        (
            "哦，差点忘了，\x01",
            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 500)

    #C0435
    ChrTalk(
        0xA,
        (
            "给，就是这个，\x01",
            "麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0436
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '小箱子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('小箱子', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0437
    ChrTalk(
        0x101,
        (
            "#00000F谢谢。\x02\x03",

            "#00003F嗯，从阿伦先生\x01",
            "给我们的送货单来看……\x02\x03",

            "#00000F这件货物的送货地址是住宅街的民宅。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A85():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A85)
    Sleep(50)

    def lambda_7A95():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A95)
    Sleep(300)

    #C0438
    ChrTalk(
        0x103,
        (
            "#00200F只要把这个送过去，\x01",
            "就算是完成委托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x105,
        (
            "#10305F说起住宅街，\x01",
            "麦克道尔议长的宅邸好像也\x01",
            "坐落在住宅街的一角。\x02\x03",

            "#10300F艾莉，这个地址\x01",
            "是在哪一带呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B44():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B44)
    Sleep(50)

    def lambda_7B54():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7B54)
    Sleep(300)

    #C0440
    ChrTalk(
        0x102,
        "#00103F嗯，我看看……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0441
    ChrTalk(
        0x102,
        (
            "#00105F咦，这个地址……\x02\x03",

            "不是坎贝尔议员家\x01",
            "隔壁的空屋吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D50")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0442
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "住宅街的空屋？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不变更】\x01",                                    # 0
            "【在怪盗Ｂ的任务中进去过】\x01",                    # 1
            "【在前作『无人住所的确认』任务中调查过】\x01",      # 2
            "【没调查过】\x01",                                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D36")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x1, 0x2)
    Jump("loc_7D50")

    label("loc_7D36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D50")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x2, 0x2)

    label("loc_7D50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7DBC")

    #C0443
    ChrTalk(
        0x101,
        (
            "#00005F就是十年前\x01",
            "曾经引起过鬼屋\x01",
            "传闻的那栋吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        "#00101F嗯、嗯……不会错的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E4E")

    label("loc_7DBC")


    #C0445
    ChrTalk(
        0x101,
        (
            "#00005F坎贝尔？那是一个共和国派\x01",
            "议员的名字吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x102,
        (
            "#00103F嗯……\x01",
            "他在住宅街的北侧有座房屋。\x02\x03",

            "#00101F而隔壁那座空屋，\x01",
            "已经废弃十年以上了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E4E")


    #C0447
    ChrTalk(
        0x104,
        (
            "#00305F……这是怎么回事？\x02\x03",

            "#00300F莫非最近\x01",
            "有人住进去了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        "#00106F唔，这我就不清楚了。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#00000F……总之，\x01",
            "我们先把货物送去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    SetScenarioFlags(0x176, 0)
    OP_29(0x85, 0x1, 0x3)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 109780, 0, -3000, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_7223 end

    def Function_53_7F39(): pass

    label("Function_53_7F39")

    EventBegin(0x1)

    #C0450
    ChrTalk(
        0x101,
        (
            "#00000F芙兰的病房是３０１号室，\x01",
            "赶快过去看看她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 8600, 0, 3680, 180)
    EventEnd(0x4)
    Return()

    # Function_53_7F39 end

    def Function_54_7F88(): pass

    label("Function_54_7F88")

    EventBegin(0x1)

    #C0451
    ChrTalk(
        0x101,
        (
            "#00000F芙兰的病房是３０１号室，\x01",
            "赶快过去看看她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 26800, 0, -25170, 0)
    EventEnd(0x4)
    Return()

    # Function_54_7F88 end

    SaveToFile()

Try(main)
