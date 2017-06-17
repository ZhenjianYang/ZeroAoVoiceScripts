from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "セシル",                 # 1
        "看護師フィリア",         # 2
        "マーサ師長",             # 3
        "看護師シロン",           # 4
        "看護師メイファ",         # 5
        "診察医ベルダイン",       # 6
        "セイランド教授",         # 7
        "入院患者",               # 8
        "入院患者",               # 9
        "入院患者",               # 10
        "入院患者",               # 11
        "入院患者",               # 12
        "入院患者",               # 13
        "入院患者",               # 14
        "入院患者",               # 15
        "入院患者",               # 16
        "入院患者",               # 17
        "入院患者",               # 18
        "入院患者",               # 19
        "警官",                   # 20
        "婦警",                   # 21
        "警官",                   # 22
        "警官",                   # 23
        "ルガノフ",               # 24
        "ジェド",                 # 25
        "ヒューイ",               # 26
        "スラッシュ",             # 27
        "ダイソン用務員",         # 28
        "研修医リットン",         # 29
        "研修医グェン",           # 30
        "入院患者",               # 31
        "入院患者",               # 32
        "入院患者",               # 33
        "入院患者",               # 34
        "入院患者",               # 35
        "入院患者",               # 36
        "入院患者",               # 37
        "入院患者",               # 38
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
        "Function_4_1801",         # 04, 4
        "Function_5_1CCA",         # 05, 5
        "Function_6_1CCE",         # 06, 6
        "Function_7_2C3A",         # 07, 7
        "Function_8_3DC6",         # 08, 8
        "Function_9_3ECD",         # 09, 9
        "Function_10_3F82",        # 0A, 10
        "Function_11_4464",        # 0B, 11
        "Function_12_45F4",        # 0C, 12
        "Function_13_47EE",        # 0D, 13
        "Function_14_4BE9",        # 0E, 14
        "Function_15_5675",        # 0F, 15
        "Function_16_5759",        # 10, 16
        "Function_17_5ACB",        # 11, 17
        "Function_18_5C54",        # 12, 18
        "Function_19_5D5E",        # 13, 19
        "Function_20_5FAD",        # 14, 20
        "Function_21_6195",        # 15, 21
        "Function_22_63FB",        # 16, 22
        "Function_23_668B",        # 17, 23
        "Function_24_6816",        # 18, 24
        "Function_25_6B36",        # 19, 25
        "Function_26_6BA5",        # 1A, 26
        "Function_27_6C19",        # 1B, 27
        "Function_28_6C64",        # 1C, 28
        "Function_29_6D05",        # 1D, 29
        "Function_30_6E62",        # 1E, 30
        "Function_31_6FA1",        # 1F, 31
        "Function_32_70C8",        # 20, 32
        "Function_33_715A",        # 21, 33
        "Function_34_71D8",        # 22, 34
        "Function_35_72F7",        # 23, 35
        "Function_36_74A1",        # 24, 36
        "Function_37_74E4",        # 25, 37
        "Function_38_756B",        # 26, 38
        "Function_39_78C4",        # 27, 39
        "Function_40_79C1",        # 28, 40
        "Function_41_7AB8",        # 29, 41
        "Function_42_7D09",        # 2A, 42
        "Function_43_802E",        # 2B, 43
        "Function_44_80C3",        # 2C, 44
        "Function_45_81F5",        # 2D, 45
        "Function_46_8305",        # 2E, 46
        "Function_47_84CD",        # 2F, 47
        "Function_48_85DA",        # 30, 48
        "Function_49_86C4",        # 31, 49
        "Function_50_87A7",        # 32, 50
        "Function_51_88C4",        # 33, 51
        "Function_52_88CB",        # 34, 52
        "Function_53_9805",        # 35, 53
        "Function_54_9868",        # 36, 54
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1359")
    Call(0, 4)
    Jump("loc_1494")

    label("loc_1359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140A")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01304F特務支援課のメンバーが\x01",
            "全員揃った今なら、きっと\x01",
            "一連の事件を解決できるはずよ。\x02\x03",

            "#01300F私はここで応援させてもらうわ。\x01",
            "どうか頑張ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1494")

    label("loc_140A")


    #C0002
    ChrTalk(
        0x8,
        (
            "#01304Fふふ、そうと決まれば\x01",
            "私も病院の仕事を頑張らないと。\x02\x03",

            "#01300Fきっと女神様は見ていて下さるわ。\x01",
            "あなたたちも頑張ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    Jump("loc_17FD")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_153C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1537")

    #C0003
    ChrTalk(
        0x8,
        (
            "#01300F課長さんやキーアちゃんにも、\x01",
            "よろしく言っておいてちょうだいね。\x02\x03",

            "大変な状況だけど……\x01",
            "お互い頑張っていきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1537")

    label("loc_1537")

    Jump("loc_17FD")

    label("loc_153C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_154A")
    Jump("loc_17FD")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1558")
    Jump("loc_17FD")

    label("loc_1558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1756")

    #C0004
    ChrTalk(
        0x8,
        (
            "#01308Fシズクちゃんの手術の件で、\x01",
            "病院内の雰囲気はとても\x01",
            "暗くなってしまっているの。\x02\x03",

            "#01300Fでも、こんなときこそ\x01",
            "私たち看護師は笑顔を\x01",
            "見せていかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00000F確かに、そうだね。\x01",
            "俺たちもキーアの笑顔には\x01",
            "救われる気持ちになるし……\x02\x03",

            "#00009Fセシル姉の笑顔があったら\x01",
            "患者さんたちもたちまち\x01",
            "元気になると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#00100Fええ、不安なんかきっと\x01",
            "吹っ飛んじゃうでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#01309Fふふ、ありがとう。\x02\x03",

            "#01300Fシズクちゃんも前向きだもの。\x01",
            "私たちがしっかりしなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D3")

    label("loc_1756")


    #C0008
    ChrTalk(
        0x8,
        (
            "#01300F暗くなっているときこそ、\x01",
            "笑顔を見せていかなくちゃね。\x02\x03",

            "患者さんの不安を和らげるのも\x01",
            "私たち看護師の務めですもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D3")

    Jump("loc_17FD")

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17E6")
    Jump("loc_17FD")

    label("loc_17E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17F4")
    Jump("loc_17FD")

    label("loc_17F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_17FD")

    label("loc_17FD")

    TalkEnd(0xFE)
    Return()

    # Function_3_133B end

    def Function_4_1801(): pass

    label("Function_4_1801")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18B8")
    SetChrPos(0x109, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_18E3")

    label("loc_18B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18E3")
    SetChrPos(0x105, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_18E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_194C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1921")
    SetChrPos(0x105, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_194C")

    label("loc_1921")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_194C")
    SetChrPos(0x109, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_194C")

    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#01305Fまあ、ロイドたち……！\x02\x03",

            "#01309Fふふ、特務支援課のメンバーが\x01",
            "みんな揃ったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#12P#00000Fああ、ようやくね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A21")

    #C0011
    ChrTalk(
        0x105,
        (
            "#12P#10402Fフフ、お姉さんの\x01",
            "応援のおかげだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A21")


    #C0012
    ChrTalk(
        0x102,
        (
            "#12P#00100Fご心配をおかけしました、\x01",
            "セシルさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#5P#01300Fエリィさん……みんなも\x01",
            "随分と苦労したみたいね。\x02\x03",

            "#01304Fふふ、でもどうしてかしら。\x02\x03",

            "#01302Fあなたたちの絆が以前よりも\x01",
            "深まっているのを感じるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#12P#00302Fハハ、ここまでこぎつけるのに\x01",
            "随分と苦労したッスからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#00202F達成感もひとしおかと。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BB2")

    #C0016
    ChrTalk(
        0x109,
        (
            "#12P#10112Fあはは……\x01",
            "まだやることは山積みですけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")


    #C0017
    ChrTalk(
        0x8,
        (
            "#5P#01304Fまだまだ大変な時が続きそうだけど……\x02\x03",

            "#01300Fあなたたちならきっと、\x01",
            "この一連の事件を解決できるはずよ。\x02\x03",

            "#01309Fふふ、頑張ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00000Fああ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1AC, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 102700, 0, 940, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1CA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CBC")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1CBC")

    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_4_1801 end

    def Function_5_1CCA(): pass

    label("Function_5_1CCA")

    Call(0, 6)
    Return()

    # Function_5_1CCA end

    def Function_6_1CCE(): pass

    label("Function_6_1CCE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC9")

    #C0019
    ChrTalk(
        0x9,
        (
            "あんな樹が現れるなんて、\x01",
            "と、とんでもないことに\x01",
            "なってしまいましたね～……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "師長からは患者さんに\x01",
            "不安を与えないよう冷静にって\x01",
            "言われてるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "はあ、とてもじゃないけど\x01",
            "落ち着いてられませんよね～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E4E")

    label("loc_1DC9")


    #C0022
    ChrTalk(
        0x9,
        (
            "あ、セシル先輩なら\x01",
            "あの大きな樹を見るために\x01",
            "敷地内の休憩所にいきましたよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "はあ、先輩は落ち着いてて\x01",
            "スゴいですよね～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4E")

    Jump("loc_2C36")

    label("loc_1E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F00")

    #C0024
    ChrTalk(
        0x9,
        (
            "街に帰れなくなってる\x01",
            "入院患者さんや外来の方への\x01",
            "対応をしているところなんです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "街であんなことが起こった以上、\x01",
            "しばらくこの状況は続きそうですね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C36")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF2")

    #C0026
    ChrTalk(
        0x9,
        (
            "ドノバンさんの回復は\x01",
            "かなり順調ですし、近いうちに\x01",
            "退院も出来ると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "だけど、イリアさんは\x01",
            "根気強くリハビリをしても\x01",
            "完治するか分からないんだとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "なんとか頑張って\x01",
            "復活できるといいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2094")

    label("loc_1FF2")


    #C0029
    ChrTalk(
        0x9,
        (
            "イリアさんは\x01",
            "根気強くリハビリをしても\x01",
            "完治するか分からないなんだとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "それでも、いいしれない希望を\x01",
            "感じさせてくれるのが\x01",
            "イリアさんの凄い所ですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2094")

    Jump("loc_2C36")

    label("loc_2099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_219A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214F")

    #C0031
    ChrTalk(
        0x9,
        (
            "イリアさんやドノバンさんの\x01",
            "意識が戻ったんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "最近は何かと物騒な話ばかりで\x01",
            "正直、気が滅入ってましたけど……\x01",
            "明るい話題が出てよかったです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2195")

    label("loc_214F")


    #C0033
    ChrTalk(
        0x9,
        (
            "イリアさんやドノバンさんの\x01",
            "意識が戻って、\x01",
            "本当によかったです～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2195")

    Jump("loc_2C36")

    label("loc_219A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A6")

    #C0034
    ChrTalk(
        0x9,
        (
            "研究棟にある集中治療室の方は\x01",
            "警備隊の方たちが収容されて\x01",
            "いるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "みんな猟兵に酷いケガを負わされて、\x01",
            "退院には時間がかかりそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "今まで色んな患者さんが\x01",
            "入院してきましたけど、\x01",
            "さすがに目を覆いたくなりますよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2335")

    label("loc_22A6")


    #C0037
    ChrTalk(
        0x9,
        (
            "今まで色んな患者さんが\x01",
            "入院してきましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "集中治療室に入っている\x01",
            "警備隊の人たちのケガには、\x01",
            "さすがに目を覆いたくなりますよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_2C36")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_245E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F5")

    #C0039
    ChrTalk(
        0x9,
        (
            "昨日の列車事故の対応も\x01",
            "ようやく落ち着いてきた\x01",
            "感じですかね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        "（くぅぅう……）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "……そういえば、\x01",
            "ロクに食べてませんでした。\x01",
            "お腹空きましたね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2459")

    label("loc_23F5")


    #C0042
    ChrTalk(
        0x9,
        (
            "忙しくて、\x01",
            "ロクに食べてませんでした。\x01",
            "お腹空きましたね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "あとで昼食をとりにいこうっと。\x02",
    )

    CloseMessageWindow()

    label("loc_2459")

    Jump("loc_2C36")

    label("loc_245E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2591")

    #C0044
    ChrTalk(
        0x9,
        (
            "セイランド教授、\x01",
            "シズクちゃんの目を治すための術式を\x01",
            "新しく練りなおしているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "最初は落ち込んでるのかと思って\x01",
            "声をかけづらかったんですけど……\x01",
            "もう頭を切り替えてたんですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "どんな時でも冷静で\x01",
            "合理的に行動できる精神力……\x01",
            "さすがは教授って気がしますよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_263B")

    label("loc_2591")


    #C0047
    ChrTalk(
        0x9,
        (
            "上手くいかなかったとき、\x01",
            "すぐに頭を切り替えるのって\x01",
            "意外と難しいんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "どんな時でも冷静で\x01",
            "合理的に行動できる精神力……\x01",
            "さすがはセイランド教授ですよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263B")

    Jump("loc_2C36")

    label("loc_2640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2742")

    #C0049
    ChrTalk(
        0x9,
        (
            "シズクちゃんの手術のことで\x01",
            "落ち込んでたら、突然師長に\x01",
            "おしりを叩かれちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "はあ～びっくりした……\x01",
            "まだヒリヒリしますよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "でも、おかげでなんだか\x01",
            "暗い気持ちが吹っ飛びました。\x01",
            "今日もがんばらないと、ですね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27F0")

    label("loc_2742")


    #C0052
    ChrTalk(
        0x9,
        (
            "叩かれたおかげで、なんだか\x01",
            "暗い気持ちが吹っ飛びました。\x01",
            "さすがは師長ですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "……でも、もう少し\x01",
            "手加減してくれてもよかったのに。\x01",
            "まだおしりがヒリヒリしますよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F0")

    Jump("loc_2C36")

    label("loc_27F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_289A")

    #C0054
    ChrTalk(
        0x9,
        (
            "ミハイル君の退院はうれしいけど、\x01",
            "寂しくなっちゃいますね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "特にシズクちゃんは\x01",
            "歳も近くて大の仲良しでしたし、\x01",
            "人一倍寂しいんじゃないかなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C36")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2978")

    #C0056
    ChrTalk(
        0x9,
        (
            "今日のオルキスタワーの除幕式、\x01",
            "私も見に行きたかったですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "でも、最近はなかなか\x01",
            "休みがとれないんですよね～……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "忙しいのは仕方ないんですけど、\x01",
            "そろそろ遊びにも行きたいですよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A11")

    label("loc_2978")


    #C0059
    ChrTalk(
        0x9,
        (
            "今度のアルカンシェル公演も、\x01",
            "チケットを買いに並べるか\x01",
            "どうかすら怪しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "忙しいのは仕方ないんですけど、\x01",
            "そろそろ遊びにも行きたいですよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A11")

    Jump("loc_2C36")

    label("loc_2A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDA")

    #C0061
    ChrTalk(
        0x9,
        (
            "こんにちは～、こちらは\x01",
            "ナースステーションですよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "……ってああ！\x01",
            "弟君にランディさ～ん！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        "#00302Fいよッス、フィリアちゃん。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00000Fお久しぶりですね。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "ほんとだよ～！\x01",
            "ふふ、でも元気そうだね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "……ランディさん、近いうちに\x01",
            "スケジュール空けておきますから！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#00309Fオーケイオーケイ、\x01",
            "また合コンでもしようや。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#10106F先輩、またそんな\x01",
            "気楽に約束なんかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00106Fはあ、やれやれね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 5)
    Jump("loc_2C36")

    label("loc_2BDA")


    #C0070
    ChrTalk(
        0x9,
        (
            "いつかみんなで\x01",
            "合コンしたいものですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "そのときは弟君も、\x01",
            "ゼッタイ来てよね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C36")

    TalkEnd(0x9)
    Return()

    # Function_6_1CCE end

    def Function_7_2C3A(): pass

    label("Function_7_2C3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C63")
    Call(0, 52)
    Return()

    label("loc_2C63")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D28")

    #C0072
    ChrTalk(
        0xFE,
        (
            "外来が再開して、\x01",
            "久々に忙しくなってきたねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "今まで受け付けられなかった分、\x01",
            "外来も沢山来てるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "よっしゃ、気合を入れて\x01",
            "仕事に励むとするかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DAC")

    label("loc_2D28")


    #C0075
    ChrTalk(
        0xFE,
        (
            "ハロルドさんに足りない物資の\x01",
            "運び込みをお願いしたし、\x01",
            "患者の受け入れ体制は万全だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "気合を入れて仕事に励むとするかねえ。\x02",
    )

    CloseMessageWindow()

    label("loc_2DAC")

    Jump("loc_3DC2")

    label("loc_2DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2E68")

    #C0077
    ChrTalk(
        0xFE,
        (
            "あたしは宿泊施設の方にいる\x01",
            "外来客のところに行ってくるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "それじゃフィリア、\x01",
            "入院患者たちへの説明は\x01",
            "よろしくたのんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)

    #C0079
    ChrTalk(
        0x9,
        "はい、分かりました～。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_3DC2")

    label("loc_2E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F76")

    #C0080
    ChrTalk(
        0xFE,
        (
            "しかし、重病・重傷患者しか\x01",
            "病院に搬送できないなんて、\x01",
            "ロクでもない決まりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "見た目からは分からない病気や\x01",
            "怪我だって当然あるんだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "早期治療すれば助けられる患者まで\x01",
            "助けられなくなったりしたら、\x01",
            "本当に目も当てられないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FF9")

    label("loc_2F76")


    #C0083
    ChrTalk(
        0xFE,
        (
            "重病・重傷患者しか\x01",
            "病院に搬送できないなんて、\x01",
            "ロクでもない決まりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "ディーター大統領は\x01",
            "そこの所を分かってるのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF9")

    Jump("loc_3DC2")

    label("loc_2FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318F")
    TurnDirection(0xFE, 0x103, 0)

    #C0085
    ChrTalk(
        0xFE,
        (
            "ティオちゃん……\x01",
            "病院を離れるんだってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        (
            "#00200Fええ……マーサ師長、\x01",
            "色々とお世話になりました。\x02\x03",

            "#00204F昔、入院していたときのお返しが\x01",
            "出来たならよかったんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "ああもう、昔の話だしそんなことを\x01",
            "気にしなくたっていいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "またいつでも遊びに来ていいから……\x01",
            "どうか、気をつけていっといで。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#00202Fふふ、はい。\x01",
            "是非そうさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_323C")

    label("loc_318F")


    #C0090
    ChrTalk(
        0xFE,
        (
            "ティオちゃんには病院の機械のことで\x01",
            "色々と手伝ってもらったし、\x01",
            "あたしもお喋りできて楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "またいつでも遊びに来ていいから……\x01",
            "どうか、気をつけていっといで。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    Jump("loc_3DC2")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A9")

    #C0092
    ChrTalk(
        0xFE,
        (
            "あたしたち医療関係者は、\x01",
            "人の死に立ち会う機会が\x01",
            "当然のように多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "だから、あたしや教授たちみたいに\x01",
            "長い事やってると、一人一人の死には\x01",
            "涙すら出なくなっちまうもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "だが、今回の襲撃事件……\x01",
            "犠牲になった多くの人たちを思うと、\x01",
            "怒りってやつが湧いてくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "軽々しく人の命を奪うなんて……\x01",
            "絶対に許されない行為だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_342E")

    label("loc_33A9")


    #C0096
    ChrTalk(
        0xFE,
        (
            "医者が多くの命を助ける一方で、\x01",
            "軽々しく人の命を奪う\x01",
            "猟兵みたいな奴らがいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "……人ってヤツは、\x01",
            "本当に業の深い生き物だね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342E")

    Jump("loc_3DC2")

    label("loc_3433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_34D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344E")
    Call(0, 8)
    Jump("loc_34CE")

    label("loc_344E")


    #C0098
    ChrTalk(
        0xFE,
        (
            "ま、アルカンシェル公演を観るのも\x01",
            "命あっての物種さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "助かった事を女神様に感謝して、\x01",
            "今はしっかりとケガを治さなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CE")

    Jump("loc_3DC2")

    label("loc_34D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_361C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F8")
    Call(0, 9)
    Jump("loc_3553")

    label("loc_34F8")


    #C0100
    ChrTalk(
        0xFE,
        "そんなこと言ってもねえ……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "今までのあんたのミスを考えると\x01",
            "とても信じられないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3553")

    Jump("loc_3617")

    label("loc_3558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DD")

    #C0102
    ChrTalk(
        0xFE,
        (
            "あんたたち、わざわざ\x01",
            "来てもらって助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "あたしはこの子に\x01",
            "お説教しなきゃいけないから、\x01",
            "また今度ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3617")

    label("loc_35DD")


    #C0104
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "シロンの面倒を見るのは\x01",
            "本当に大変だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3617")

    Jump("loc_3DC2")

    label("loc_361C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3757")

    #C0105
    ChrTalk(
        0xFE,
        (
            "まったく、どいつもこいつも\x01",
            "気合が抜けちまってるねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "あのシズクちゃんの件だから\x01",
            "気持ちは充分に分かる。\x01",
            "誰だって落ち込みそうになるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "だけど、あたしたちまで\x01",
            "落ち込んだ顔してちゃ、\x01",
            "他の患者が不安になっちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "こういうときこそ元気を見せないと。\x01",
            "あたしはそう思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37D5")

    label("loc_3757")


    #C0109
    ChrTalk(
        0xFE,
        (
            "まったく、どいつもこいつも\x01",
            "落ち込んじまっていけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "空元気でも元気が一番ってね。\x01",
            "ほら、あんたたちも元気だしな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D5")

    Jump("loc_3DC2")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CA")
    TurnDirection(0xFE, 0x103, 0)

    #C0111
    ChrTalk(
        0xFE,
        (
            "まあまあまあ……！\x01",
            "そこにいるのは\x01",
            "ティオちゃんじゃないかい！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "いやあ、久しぶりだねえ！\x01",
            "元気にしてたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#00202Fはい、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x109,
        (
            "#10100Fティオちゃんは\x01",
            "師長さんと知り合いなんだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#00200Fええ、昔入院していたときに\x01",
            "何かとお世話になったことがありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "あはは、看護師として\x01",
            "大したことはしちゃいないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "警察の仕事も色々大変だろうが、\x01",
            "身体に気をつけて\x01",
            "しっかりがんばるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x103,
        "#00204Fはい……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 4)
    Jump("loc_3A5E")

    label("loc_39CA")


    #C0119
    ChrTalk(
        0xFE,
        (
            "前も言ったけど、\x01",
            "ティオちゃんは本当に\x01",
            "美人さんになったもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "警察の仕事も色々大変だろうが、\x01",
            "身体に気をつけて\x01",
            "しっかりがんばるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5E")

    Jump("loc_3DC2")

    label("loc_3A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7E")

    #C0121
    ChrTalk(
        0xFE,
        (
            "セシルはどんな相手に対しても\x01",
            "分け隔てなく、思いやりをもって\x01",
            "接する事ができる。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "当たり前のことに見えて、\x01",
            "それができる人間はそう多くない。\x01",
            "立派な才能だとあたしは思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "ふふ、あのコを\x01",
            "看護師の道へ進ませたのは\x01",
            "女神様の思し召しかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C1C")

    label("loc_3B7E")


    #C0124
    ChrTalk(
        0xFE,
        (
            "思いやりは、患者たちに\x01",
            "安心ってもんを与えられる。\x01",
            "セシルの立派な才能だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "ふふ、あのコを\x01",
            "看護師の道へ進ませたのは\x01",
            "女神様の思し召しかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1C")

    Jump("loc_3DC2")

    label("loc_3C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D54")

    #C0126
    ChrTalk(
        0xFE,
        (
            "セイランド教授ってのは、\x01",
            "レミフェリアではなかなか\x01",
            "名の知れたお人でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "医学の分野で博士号を持ってて、\x01",
            "大公家とも繋がりが深いんだとさ。\x01",
            "まあ、身元は確かだと言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "それよりなにより、あたしゃあの\x01",
            "肝っ玉の据わった態度が気に入ったよ。\x01",
            "今時の女はああでなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DC2")

    label("loc_3D54")


    #C0129
    ChrTalk(
        0xFE,
        (
            "あたしゃ、セイランド教授の\x01",
            "肝っ玉の据わった\x01",
            "態度が気に入っててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "今時の女はああでなきゃダメだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3DC2")

    TalkEnd(0xFE)
    Return()

    # Function_7_2C3A end

    def Function_8_3DC6(): pass

    label("Function_8_3DC6")

    OP_4B(0xA, 0xFF)
    OP_4B(0x17, 0xFF)

    #C0131
    ChrTalk(
        0x17,
        (
            "せっかくアルカンシェルを\x01",
            "観にきたというのに、\x01",
            "列車事故などにあってしまうとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x17,
        "うう、無念だ……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "ああ、そういえば明日は\x01",
            "リニューアル公演だったねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "ま、命あっての物種さ。\x01",
            "助かった事を女神様に\x01",
            "感謝しなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x17, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x17, 0xFF)
    Return()

    # Function_8_3DC6 end

    def Function_9_3ECD(): pass

    label("Function_9_3ECD")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0135
    ChrTalk(
        0xA,
        (
            "まったくあんたって子は……\x01",
            "何度同じ間違いをするんだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "ひ～ん、だからちゃんと\x01",
            "やったんですってば～！\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "間違いが起こってるのが\x01",
            "間違いなんですよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_3ECD end

    def Function_10_3F82(): pass

    label("Function_10_3F82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FAB")
    Call(0, 52)
    Return()

    label("loc_3FAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC9")
    Call(0, 12)
    Jump("loc_400E")

    label("loc_3FC9")


    #C0138
    ChrTalk(
        0xFE,
        (
            "てへへ、似てるから間違えちゃった。\x01",
            "よく見ると大きさが違うねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400E")

    Jump("loc_4460")

    label("loc_4013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4075")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402E")
    Call(0, 12)
    Jump("loc_4070")

    label("loc_402E")


    #C0139
    ChrTalk(
        0xFE,
        (
            "街にいるバッジョや\x01",
            "お父さん、お母さんたちは\x01",
            "大丈夫かなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4070")

    Jump("loc_4460")

    label("loc_4075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4083")
    Jump("loc_4460")

    label("loc_4083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4091")
    Jump("loc_4460")

    label("loc_4091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417C")

    #C0140
    ChrTalk(
        0xFE,
        (
            "……あんなに患者さんが\x01",
            "運び込まれたのを見たのは初めてです。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "みんなとっても痛そうにしてて……\x01",
            "あれ以来なんだか１人でいるのが\x01",
            "怖くなっちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "今日も夜はメイファちゃんに\x01",
            "一緒に居てもらおう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4211")

    label("loc_417C")


    #C0143
    ChrTalk(
        0xFE,
        (
            "……あんなに患者さんが\x01",
            "運び込まれたのを見たのは初めてで、\x01",
            "なんだか怖くなっちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "今日も夜はメイファちゃんに\x01",
            "一緒に居てもらおう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4211")

    Jump("loc_4460")

    label("loc_4216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4224")
    Jump("loc_4460")

    label("loc_4224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_442A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4249")
    Call(0, 9)
    Jump("loc_429C")

    label("loc_4249")


    #C0145
    ChrTalk(
        0xFE,
        (
            "だから、きっとなにかの\x01",
            "間違いなんですって～！\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "ひ～ん、信じてください～！\x02",
    )

    CloseMessageWindow()

    label("loc_429C")

    Jump("loc_4425")

    label("loc_42A1")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43AB")

    #C0147
    ChrTalk(
        0xFE,
        (
            "えへへ、カゲマルのストラップ……\x01",
            "届いてよかったです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        (
            "#00202Fカゲマルはいいですよね……\x01",
            "わたしもお気に入りです。\x02",
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
            "そうなんだ～☆\x01",
            "ね～、かわいいよね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        "……コラッ、聞いてるのかい！？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TurnDirection(0xFE, 0xA, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_4421")

    label("loc_43AB")


    #C0151
    ChrTalk(
        0xFE,
        (
            "うう、マーサ師長もホラ、\x01",
            "見てくださいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "カゲマルのストラップ、\x01",
            "ちょ～可愛いですよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        "知るかいっ！\x02",
    )

    CloseMessageWindow()

    label("loc_4421")

    OP_4C(0xA, 0xFF)

    label("loc_4425")

    Jump("loc_4460")

    label("loc_442A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4438")
    Jump("loc_4460")

    label("loc_4438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4446")
    Jump("loc_4460")

    label("loc_4446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4454")
    Jump("loc_4460")

    label("loc_4454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4460")
    Call(0, 11)

    label("loc_4460")

    TalkEnd(0xFE)
    Return()

    # Function_10_3F82 end

    def Function_11_4464(): pass

    label("Function_11_4464")

    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x10, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459C")

    #C0154
    ChrTalk(
        0xB,
        "はーい、点滴しましょうね～。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x10,
        (
            "う……看護師さん、\x01",
            "今日は大丈夫なんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10,
        (
            "また刺す所を間違えて、\x01",
            "ピューッと血が出たりしたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "やだなあ、こないだのは\x01",
            "手元が狂っただけですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "ふふ、安心してください。\x01",
            "多分絶対大丈夫ですから！\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x10,
        "（ふ、不安すぎる……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_45EB")

    label("loc_459C")


    #C0160
    ChrTalk(
        0xB,
        (
            "……あれ？\x01",
            "注射針、忘れちゃったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x10,
        "た、頼むよ看護師さん……\x02",
    )

    CloseMessageWindow()

    label("loc_45EB")

    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_11_4464 end

    def Function_12_45F4(): pass

    label("Function_12_45F4")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46EE")

    #C0162
    ChrTalk(
        0xC,
        (
            "それじゃシロン、手分けして\x01",
            "入院患者さんたちの検温に行くわよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        "うんっ、メイファちゃん！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xC,
        "体温計は持ったわね！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        "はーいっ♪　ここにあるよっ。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "……あんたが持ってるソレ、\x01",
            "温度計じゃないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xB,
        "……あれれ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E2")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_47E2")

    #C0168
    ChrTalk(
        0xB,
        (
            "メイファちゃん、\x01",
            "何が起こってるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        "あたし、ちょっと怖いかも……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        "街で大きな動きがあったみたいね。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "でも、心配しなくていいわ。\x01",
            "今は自分たちに出来ることを\x01",
            "キチンとやっていけばいいから。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        "う、うんっ……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_47E2")

    SetScenarioFlags(0x3, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_45F4 end

    def Function_13_47EE(): pass

    label("Function_13_47EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_484E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480C")
    Call(0, 12)
    Jump("loc_4849")

    label("loc_480C")


    #C0173
    ChrTalk(
        0xFE,
        (
            "なにもかも全然違うっつの！\x01",
            "……まったく、この子ったら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4849")

    Jump("loc_4BE5")

    label("loc_484E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_48DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4869")
    Call(0, 12)
    Jump("loc_48D5")

    label("loc_4869")


    #C0174
    ChrTalk(
        0xFE,
        (
            "大きな動きがあったのは\x01",
            "確かみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "今は自分たちに出来ることを\x01",
            "キチンとやるのが大事よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D5")

    Jump("loc_4BE5")

    label("loc_48DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_48E8")
    Jump("loc_4BE5")

    label("loc_48E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_48F6")
    Jump("loc_4BE5")

    label("loc_48F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C4")

    #C0176
    ChrTalk(
        0xFE,
        (
            "２０２号室に入れられた子たち、\x01",
            "最初はすごく威勢がよかったんだけど、\x01",
            "しばらくしたら落ち込んじゃってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "ケガのせいだけじゃないみたいだけど、\x01",
            "街で何かあったのかしら……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A38")

    label("loc_49C4")


    #C0178
    ChrTalk(
        0xFE,
        (
            "そういえば最近、シロンがなんだか\x01",
            "怯えちゃってるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "はあ、私達これから\x01",
            "どうなっちゃうのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A38")

    Jump("loc_4BE5")

    label("loc_4A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A4B")
    Jump("loc_4BE5")

    label("loc_4A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A59")
    Jump("loc_4BE5")

    label("loc_4A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A67")
    Jump("loc_4BE5")

    label("loc_4A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A75")
    Jump("loc_4BE5")

    label("loc_4A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B54")

    #C0180
    ChrTalk(
        0xFE,
        (
            "シロンのやつ、この間\x01",
            "屋上で日向ぼっこしてたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "しかも、干してたシーツに\x01",
            "包まって幸せそうな顔して……\x01",
            "ほんとあり得ないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "……ああ、イヤな予感。\x01",
            "また同じ事やってそう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BD7")

    label("loc_4B54")


    #C0183
    ChrTalk(
        0xFE,
        (
            "シロンのやつ、この間\x01",
            "屋上で日向ぼっこしてたのよね。\x01",
            "シーツも汚しちゃうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "……念のため、後で\x01",
            "様子を見に行ってみるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD7")

    Jump("loc_4BE5")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BE5")

    label("loc_4BE5")

    TalkEnd(0xFE)
    Return()

    # Function_13_47EE end

    def Function_14_4BE9(): pass

    label("Function_14_4BE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CDD")

    #C0185
    ChrTalk(
        0xFE,
        (
            "一通り回診に回ったあとは\x01",
            "手術も入っている。\x01",
            "……やれやれ、大忙しだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "だが、どこで何が起ころうとも、\x01",
            "我々のやるべき事は変わらない。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "目の前の患者を助けていくこと……\x01",
            "それこそが医者の仕事なのだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D63")

    label("loc_4CDD")


    #C0188
    ChrTalk(
        0xFE,
        (
            "どこで何が起ころうとも、\x01",
            "我々のやるべき事は変わらない。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "目の前の患者を助けていくこと……\x01",
            "それこそが医者の仕事なのだからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D63")

    Jump("loc_5671")

    label("loc_4D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D83")
    Call(0, 15)
    Jump("loc_4DBE")

    label("loc_4D83")


    #C0190
    ChrTalk(
        0xFE,
        (
            "うちの病院のスタッフは優秀です。\x01",
            "どうか心配なさらず。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DBE")

    Jump("loc_5671")

    label("loc_4DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4DD4")
    Call(0, 41)
    Jump("loc_5671")

    label("loc_4DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF7")

    #C0191
    ChrTalk(
        0xFE,
        (
            "入院していた警察関係者や\x01",
            "不良グループの若者たちは、\x01",
            "すでに退院していった。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "本来なら、退院後もしばらくは\x01",
            "通院してもらい様子を見るのだが……\x01",
            "街道の移動制限下ではそれもできない。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "医師として無責任な行いを\x01",
            "強いられるこの状況……\x01",
            "疑問を感じざるを得んよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4FAB")

    label("loc_4EF7")


    #C0194
    ChrTalk(
        0xFE,
        (
            "本来なら、退院した患者も\x01",
            "しばらくは経過を見る必要があるが、\x01",
            "街道の移動制限下ではそれもできない。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "医師として無責任な行いを\x01",
            "強いられるこの状況……\x01",
            "疑問を感じざるを得んよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAB")

    Jump("loc_5671")

    label("loc_4FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5104")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5091")

    #C0196
    ChrTalk(
        0xFE,
        (
            "彼らは、身体よりも心の方が\x01",
            "負ったダメージが大きいようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "病気や怪我は患者の心が治すもの。\x01",
            "捨て鉢な気持ちでは\x01",
            "治りも遅くなってしまうだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "何とか立ち直ってくれると\x01",
            "いいのだがな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_50FF")

    label("loc_5091")


    #C0199
    ChrTalk(
        0xFE,
        (
            "彼らは、身体よりも心の方が\x01",
            "負ったダメージが大きいようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "何とか立ち直ってくれると\x01",
            "いいのだがな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50FF")

    Jump("loc_5671")

    label("loc_5104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5172")

    #C0201
    ChrTalk(
        0xFE,
        (
            "……足の骨折は\x01",
            "既に処置をしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "死ぬようなケガではないから、\x01",
            "落ち着いてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5671")

    label("loc_5172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_527C")

    #C0203
    ChrTalk(
        0xFE,
        (
            "外科というものが生まれた当初は、\x01",
            "『人の身体を切るなど言語道断』と\x01",
            "散々言われてきたものだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "近頃は、その理解も\x01",
            "段々と深まってきたように感じる。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "偉大な先達が成功をもって\x01",
            "有用性を示してきたおかげだ。\x01",
            "感謝せねばなるまいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_530B")

    label("loc_527C")


    #C0206
    ChrTalk(
        0xFE,
        (
            "近頃は、外科への理解も\x01",
            "段々と深まってきたように感じる。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "偉大な先達が成功をもって\x01",
            "有用性を示してきたおかげだ。\x01",
            "感謝せねばなるまいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_530B")

    Jump("loc_5671")

    label("loc_5310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_550F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5486")

    #C0208
    ChrTalk(
        0xFE,
        (
            "シズクくんの症状は、\x01",
            "外科・内科・神経科の問題が\x01",
            "複雑に干渉しあったものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "完治は難しいと言われているが、\x01",
            "完全に失明しているわけではないから\x01",
            "わずかに希望はあると言われている。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……わずかな希望を求めることは\x01",
            "ある意味、諦めるよりも\x01",
            "辛く、苦しい事だとも言えるがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "それでも決して諦めようとしない\x01",
            "あの親子に、私は敬意を覚えるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_550A")

    label("loc_5486")


    #C0212
    ChrTalk(
        0xFE,
        (
            "わずかな希望を求めることは\x01",
            "ある意味、辛く、苦しいものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "それでも決して諦めようとしない\x01",
            "あの親子に、私は敬意を覚えるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550A")

    Jump("loc_5671")

    label("loc_550F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_551D")
    Jump("loc_5671")

    label("loc_551D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E9")

    #C0214
    ChrTalk(
        0xFE,
        (
            "ヨアヒム君の件で\x01",
            "病院の信用は一時落ち込んだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "我々医者の仕事は、\x01",
            "真摯に患者を助けることが全てだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "その姿勢を示し続ければ、\x01",
            "信用は必ず取り戻していけるだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5663")

    label("loc_55E9")


    #C0217
    ChrTalk(
        0xFE,
        (
            "我々医者の仕事は、\x01",
            "真摯に患者を助けることが全てだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "その姿勢を示し続ければ、\x01",
            "失った信用は必ず取り戻せるだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5663")

    Jump("loc_5671")

    label("loc_5668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5671")

    label("loc_5671")

    TalkEnd(0xFE)
    Return()

    # Function_14_4BE9 end

    def Function_15_5675(): pass

    label("Function_15_5675")

    OP_4B(0xD, 0xFF)
    OP_4B(0x2C, 0xFF)

    #C0219
    ChrTalk(
        0x2C,
        (
            "先生……薬の種類が\x01",
            "足りてないとか聞きましたけど、\x01",
            "大丈夫なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xD,
        (
            "……今、病院全体でなんとか\x01",
            "対策を練っているところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xD,
        (
            "うちの病院のスタッフは優秀です。\x01",
            "どうか心配なさらず。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 5)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x2C, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0x2C, 0xFF)
    Return()

    # Function_15_5675 end

    def Function_16_5759(): pass

    label("Function_16_5759")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_576A")
    Jump("loc_5AC7")

    label("loc_576A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5778")
    Jump("loc_5AC7")

    label("loc_5778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5786")
    Jump("loc_5AC7")

    label("loc_5786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5794")
    Jump("loc_5AC7")

    label("loc_5794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F9")

    #C0222
    ChrTalk(
        0xFE,
        (
            "リットンの２０２号の回診、\x01",
            "現在予定より１分１４秒オーバーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "既にこちらは終わったと言うのに、\x01",
            "……ヤツもまだまだだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00006Fま、前も思ったんですけど……\x01",
            "教授って異様に\x01",
            "時間に厳しいですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "たかが一分一秒が生死を左右する……\x01",
            "医療の現場とはそういう世界だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "より多くの人の命を助けるために、\x01",
            "時間を厳守し、計画通りに動くのは\x01",
            "ごく当たり前のことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x103,
        (
            "#00200F確かに……\x01",
            "どんなことにも言えること\x01",
            "かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "無論、そのために技術が\x01",
            "不完全であってはならないがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "素早く、完璧に仕事をこなす。\x01",
            "……将来は若い医師たちにも\x01",
            "そうなってほしいものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5AAB")

    label("loc_59F9")


    #C0230
    ChrTalk(
        0xFE,
        (
            "より多くの人の命を助けるために\x01",
            "時間を厳守し、計画通りに動くのは\x01",
            "ごく当たり前のことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "素早く、完璧に仕事をこなす。\x01",
            "……将来は若い医師たちにも\x01",
            "そうなってほしいものだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AAB")

    Jump("loc_5AC7")

    label("loc_5AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5ABE")
    Jump("loc_5AC7")

    label("loc_5ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5AC7")

    label("loc_5AC7")

    TalkEnd(0xFE)
    Return()

    # Function_16_5759 end

    def Function_17_5ACB(): pass

    label("Function_17_5ACB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B51")

    #C0232
    ChrTalk(
        0xFE,
        (
            "セイランド先生は、\x01",
            "とても立派な方じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "言葉遣いは厳しいが、\x01",
            "その診察は思いやりに\x01",
            "あふれているからのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C50")

    label("loc_5B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BD2")

    #C0234
    ChrTalk(
        0xFE,
        (
            "ここの病院食は、\x01",
            "栄養のバランスが\x01",
            "よく考えられていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "お陰でなんだか手術後の\x01",
            "治りもいい気がするわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C50")

    label("loc_5BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C50")

    #C0236
    ChrTalk(
        0xFE,
        (
            "この病院じゃ、\x01",
            "看護師さんや先生方が\x01",
            "とてもよくしてくれてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "わしゃ、なかなか\x01",
            "入院生活を気に入っておるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C50")

    TalkEnd(0xFE)
    Return()

    # Function_17_5ACB end

    def Function_18_5C54(): pass

    label("Function_18_5C54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5CE5")

    #C0238
    ChrTalk(
        0xFE,
        (
            "あの女医先生、なんだか\x01",
            "すげえおっかねえんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "文句言ってると睨まれちまうし、\x01",
            "退院まではおとなしくしてようっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D5A")

    label("loc_5CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D4E")

    #C0240
    ChrTalk(
        0xFE,
        "あ～、早く退院したいぜ。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "質素な食事も、もうこりごりだ。\x01",
            "ビフテキとか食いてえよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D5A")

    label("loc_5D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D5A")
    Call(0, 11)

    label("loc_5D5A")

    TalkEnd(0xFE)
    Return()

    # Function_18_5C54 end

    def Function_19_5D5E(): pass

    label("Function_19_5D5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5DEE")

    #C0242
    ChrTalk(
        0xFE,
        (
            "ショリショリショリ……\x01",
            "孫が差し入れてくれた\x01",
            "リンゴを剥いているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "ふふ、よかったら\x01",
            "あなたたちもいっしょにいかが？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA9")

    label("loc_5DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EAA")

    #C0244
    ChrTalk(
        0xFE,
        (
            "今日は確か、街のほうで\x01",
            "除幕式があったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "噂のオルキスタワーとやらを\x01",
            "見てみたかったわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "まあ、退院した後の\x01",
            "楽しみにしておきましょうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F18")

    label("loc_5EAA")


    #C0247
    ChrTalk(
        0xFE,
        (
            "噂のオルキスタワーとやらを\x01",
            "見てみたかったわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "まあ、退院した後の\x01",
            "楽しみにしておきましょうかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F18")

    Jump("loc_5FA9")

    label("loc_5F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FA9")

    #C0249
    ChrTalk(
        0xFE,
        (
            "以前は病院の先生が\x01",
            "大きな事件を起こしたとかで\x01",
            "騒ぎになっていたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "とってもいい病院じゃない。\x01",
            "心配してソンしたわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA9")

    TalkEnd(0xFE)
    Return()

    # Function_19_5D5E end

    def Function_20_5FAD(): pass

    label("Function_20_5FAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6010")

    #C0251
    ChrTalk(
        0xFE,
        "おお、本当かい？\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "いやあ、安心したよ。\x01",
            "早く治して仕事に\x01",
            "復帰しないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6191")

    label("loc_6010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6125")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CC")

    #C0253
    ChrTalk(
        0xFE,
        (
            "同僚が忙しい中、\x01",
            "お見舞いにきてくれてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "仕事のことは気にしないで、\x01",
            "怪我を治すのに専念しろだとさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "そうだな、この際\x01",
            "仕事のことは忘れてしまうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6120")

    label("loc_60CC")


    #C0256
    ChrTalk(
        0xFE,
        (
            "この際、仕事のことは\x01",
            "忘れてしまおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "今は怪我を治すのに\x01",
            "専念しないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6120")

    Jump("loc_6191")

    label("loc_6125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6191")

    #C0258
    ChrTalk(
        0xFE,
        (
            "交通事故で、足の骨を\x01",
            "折ってしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "やれやれ、\x01",
            "大事な仕事もあるのに\x01",
            "参ってしまうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6191")

    TalkEnd(0xFE)
    Return()

    # Function_20_5FAD end

    def Function_21_6195(): pass

    label("Function_21_6195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_621F")

    #C0260
    ChrTalk(
        0xFE,
        (
            "病室のベッドも、\x01",
            "一気に埋まっちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "大きな事故だったそうだけど、\x01",
            "死者とかが出なくて\x01",
            "本当に良かったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F7")

    label("loc_621F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_62CD")

    #C0262
    ChrTalk(
        0xFE,
        (
            "家に残してきた旦那が、\x01",
            "子供たちにちゃんと食べさせてるか\x01",
            "心配だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "あの人なりに、なんとか\x01",
            "料理に挑戦してるみたいでね。\x01",
            "とりあえず安心したわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F7")

    label("loc_62CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_63F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6391")

    #C0264
    ChrTalk(
        0xFE,
        (
            "私は、大した事ない手術だから\x01",
            "入院も短くて済むらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "でも、家を空けるとなると\x01",
            "やっぱり家族が心配よね……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "旦那や子供たちは\x01",
            "ちゃんとご飯食べてるかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_63F7")

    label("loc_6391")


    #C0267
    ChrTalk(
        0xFE,
        (
            "家を空けるとなると\x01",
            "やっぱり家族が心配よね……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "旦那や子供たちは\x01",
            "ちゃんとご飯食べてるかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F7")

    TalkEnd(0xFE)
    Return()

    # Function_21_6195 end

    def Function_22_63FB(): pass

    label("Function_22_63FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6473")

    #C0269
    ChrTalk(
        0xFE,
        (
            "まさか、列車の\x01",
            "脱線事故とは……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "最近は、立て続けに\x01",
            "事件が起こっておるのう。\x01",
            "物騒なもんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6687")

    label("loc_6473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_661A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6574")

    #C0271
    ChrTalk(
        0xFE,
        (
            "入院中の気晴らしに、\x01",
            "今年出たクロスベルタイムズを\x01",
            "１号から読み直しておったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "マクダエル元市長の暗殺未遂事件、\x01",
            "創立記念祭、そしてあの教団事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "こうしてみると、半年あまりの間に\x01",
            "本当に色々な事があったんじゃのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6615")

    label("loc_6574")


    #C0274
    ChrTalk(
        0xFE,
        (
            "元市長の暗殺未遂事件、\x01",
            "教団事件、テロリストによる\x01",
            "オルキスタワーでの襲撃事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "こうしてみると、半年あまりの間に\x01",
            "本当に色々な事件が起こっておるのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6615")

    Jump("loc_6687")

    label("loc_661A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6687")

    #C0276
    ChrTalk(
        0xFE,
        (
            "入院中はどうしても\x01",
            "暇を持て余してしまうのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "溜まっていた本でも\x01",
            "一気読みするとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6687")

    TalkEnd(0xFE)
    Return()

    # Function_22_63FB end

    def Function_23_668B(): pass

    label("Function_23_668B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_671F")

    #C0278
    ChrTalk(
        0xFE,
        (
            "これだけの患者さんを\x01",
            "無事に治してしまうなんて、\x01",
            "さすが先生方だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院がある限り、\x01",
            "クロスベルの住民は安心だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6812")

    label("loc_671F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_673A")
    Call(0, 39)
    Jump("loc_679C")

    label("loc_673A")


    #C0280
    ChrTalk(
        0xFE,
        (
            "お若いから、少し心配に\x01",
            "思っていたけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "リットン先生も\x01",
            "なかなか頼りがいがあるねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_679C")

    Jump("loc_6812")

    label("loc_67A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6812")

    #C0282
    ChrTalk(
        0xFE,
        (
            "ベルダイン先生の診察は\x01",
            "とても丁寧でいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "腕のいい先生方に看てもらえて、\x01",
            "あたしは幸せだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6812")

    TalkEnd(0xFE)
    Return()

    # Function_23_668B end

    def Function_24_6816(): pass

    label("Function_24_6816")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_694B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C7")

    #C0284
    ChrTalk(
        0xFE,
        (
            "列車事故で入院だなんて、\x01",
            "ほんと可哀想……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "私がギックリ腰で入院したのと\x01",
            "同じくらい可哀想よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "……なによ、その\x01",
            "何か言いたげな顔は。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6946")

    label("loc_68C7")


    #C0287
    ChrTalk(
        0xFE,
        (
            "列車事故で入院だなんて、\x01",
            "私がギックリ腰で入院したのと\x01",
            "同じくらい可哀想よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "……なによ、その\x01",
            "何か言いたそうな顔は。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6946")

    Jump("loc_6B32")

    label("loc_694B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A17")

    #C0289
    ChrTalk(
        0xFE,
        "……昨日、友達が見舞いに来たの。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "ギックリ腰で入院だなんて、\x01",
            "かっこ悪いから誰にも\x01",
            "言ってなかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "きっとお母さんがバラしたんだわ。\x01",
            "ひどい……ひどすぎる……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6A9A")

    label("loc_6A17")


    #C0292
    ChrTalk(
        0xFE,
        (
            "ギックリ腰で入院だなんて、\x01",
            "かっこ悪いから誰にも\x01",
            "言ってなかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "お見舞い自体はうれしかったから、\x01",
            "まあいいけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A9A")

    Jump("loc_6B32")

    label("loc_6A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6B32")

    #C0294
    ChrTalk(
        0xFE,
        (
            "ああ、うら若き乙女たるこの私が、\x01",
            "入院なんかしなくちゃならないなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "しかもギックリ腰だなんて、\x01",
            "かっこ悪い……かっこ悪いわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B32")

    TalkEnd(0xFE)
    Return()

    # Function_24_6816 end

    def Function_25_6B36(): pass

    label("Function_25_6B36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B54")
    Call(0, 8)
    Jump("loc_6BA1")

    label("loc_6B54")


    #C0296
    ChrTalk(
        0xFE,
        (
            "助かったとはいえ、\x01",
            "せっかくのアルカンシェルが……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "うう、無念だ……\x02",
    )

    CloseMessageWindow()

    label("loc_6BA1")

    TalkEnd(0xFE)
    Return()

    # Function_25_6B36 end

    def Function_26_6BA5(): pass

    label("Function_26_6BA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C15")

    #C0298
    ChrTalk(
        0xFE,
        (
            "列車が横転したときは、\x01",
            "もうダメかと思ったぜ……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "もう当分の間は、\x01",
            "鉄道は利用したくないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C15")

    TalkEnd(0xFE)
    Return()

    # Function_26_6BA5 end

    def Function_27_6C19(): pass

    label("Function_27_6C19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C60")

    #C0300
    ChrTalk(
        0xFE,
        (
            "痛たたたたた……！\x01",
            "し、死ぬ！　死んでしまううう……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C60")

    TalkEnd(0xFE)
    Return()

    # Function_27_6C19 end

    def Function_28_6C64(): pass

    label("Function_28_6C64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D01")

    #C0301
    ChrTalk(
        0xFE,
        (
            "……向かいの人、男のくせに\x01",
            "ギャーギャーうるさいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "せっかくこうして\x01",
            "事故から生還できたんだから、\x01",
            "ちょっと痛いくらい我慢しなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D01")

    TalkEnd(0xFE)
    Return()

    # Function_28_6C64 end

    def Function_29_6D05(): pass

    label("Function_29_6D05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6E5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD7")

    #C0303
    ChrTalk(
        0xFE,
        (
            "《赤い星座》の戦闘力に、\x01",
            "我々は全くと言っていいほど\x01",
            "太刀打ちできなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "市民たちにも大きな不安を\x01",
            "与えてしまったろうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "何のための警察だ……\x01",
            "情けない気分だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6E5E")

    label("loc_6DD7")


    #C0306
    ChrTalk(
        0xFE,
        (
            "《赤い星座》の戦闘力に、\x01",
            "我々は全くと言っていいほど\x01",
            "太刀打ちできなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "ドノバン警部も、なんとか\x01",
            "回復すればいいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E5E")

    TalkEnd(0xFE)
    Return()

    # Function_29_6D05 end

    def Function_30_6E62(): pass

    label("Function_30_6E62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F32")

    #C0308
    ChrTalk(
        0xFE,
        (
            "フランさんが受付にいることで、\x01",
            "私たち警官はこれまで\x01",
            "随分と励まされてました。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "彼女が意識を取り戻してくれて、\x01",
            "本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        "#10100F……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6F9D")

    label("loc_6F32")


    #C0311
    ChrTalk(
        0xFE,
        (
            "フランさんが\x01",
            "意識を取り戻してくれて、\x01",
            "本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "早く元気になってくれると\x01",
            "いいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9D")

    TalkEnd(0xFE)
    Return()

    # Function_30_6E62 end

    def Function_31_6FA1(): pass

    label("Function_31_6FA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_70C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7034")

    #C0313
    ChrTalk(
        0xFE,
        (
            "受付のフランさんまで\x01",
            "大怪我させちまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "くそっ……！\x01",
            "俺たちは何のために\x01",
            "警察学校で訓練を積んだんだ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_70C4")

    label("loc_7034")


    #C0315
    ChrTalk(
        0xFE,
        (
            "くそっ……！\x01",
            "俺たちは何のために\x01",
            "警察学校で訓練を積んだんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "フランさんにまで\x01",
            "大怪我をさせちまうなんて、\x01",
            "情けなくて仕方がないぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70C4")

    TalkEnd(0xFE)
    Return()

    # Function_31_6FA1 end

    def Function_32_70C8(): pass

    label("Function_32_70C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7156")

    #C0317
    ChrTalk(
        0xFE,
        (
            "あの猟兵の操っていた魔獣、\x01",
            "恐ろしく鍛え上げられていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "もう一度あんな奴らが襲ってきたら、\x01",
            "今度こそやられちまうよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7156")

    TalkEnd(0xFE)
    Return()

    # Function_32_70C8 end

    def Function_33_715A(): pass

    label("Function_33_715A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_71D4")

    #C0319
    ChrTalk(
        0xFE,
        (
            "ヴァルドさん……\x01",
            "アンタあんなになってまで\x01",
            "強くなりたかったのかよォ……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "クソッ、ワケわかンねえよ……\x02",
    )

    CloseMessageWindow()

    label("loc_71D4")

    TalkEnd(0xFE)
    Return()

    # Function_33_715A end

    def Function_34_71D8(): pass

    label("Function_34_71D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_72F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7287")

    #C0321
    ChrTalk(
        0xFE,
        (
            "どんな葛藤があったにせよ……\x01",
            "とにかく、あんなヤツは\x01",
            "もうヘッドでも何でもねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "つうか、サーベルバイパーも……\x01",
            "これで終わりなのかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_72F3")

    label("loc_7287")


    #C0323
    ChrTalk(
        0xFE,
        (
            "あんなヤツ……\x01",
            "もうヘッドでも何でもねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "つうか、サーベルバイパーも……\x01",
            "これで終わりなのかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72F3")

    TalkEnd(0xFE)
    Return()

    # Function_34_71D8 end

    def Function_35_72F7(): pass

    label("Function_35_72F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_749D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_741C")

    #C0325
    ChrTalk(
        0xFE,
        (
            "俺たちは骨折程度で済んだが……\x01",
            "コウキのヤツは飛び切り重傷でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "病院に着いてからすぐに\x01",
            "集中治療室に運ばれて……\x01",
            "今は研究棟の方で治療を受けてんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "何でもまだ、意識すら\x01",
            "回復しないって話だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "クソッ、何でこんなことに\x01",
            "なっちまったンだよ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_749D")

    label("loc_741C")


    #C0329
    ChrTalk(
        0xFE,
        (
            "スラッシュのヤツも\x01",
            "すっかり脅えちまってよ。\x01",
            "ロクに話もできねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "クソッ、何でこんなことに\x01",
            "なっちまったンだよ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_749D")

    TalkEnd(0xFE)
    Return()

    # Function_35_72F7 end

    def Function_36_74A1(): pass

    label("Function_36_74A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_74E0")

    #C0331
    ChrTalk(
        0xFE,
        (
            "ぶるぶるぶる……\x01",
            "ば、化物……化物が襲って……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74E0")

    TalkEnd(0xFE)
    Return()

    # Function_36_74A1 end

    def Function_37_74E4(): pass

    label("Function_37_74E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7567")

    #C0332
    ChrTalk(
        0xFE,
        (
            "さて、今から\x01",
            "ナースステーションの\x01",
            "掃除をするわけだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "……女性の園だからなあ。\x01",
            "どうにも緊張してしまうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7567")

    TalkEnd(0xFE)
    Return()

    # Function_37_74E4 end

    def Function_38_756B(): pass

    label("Function_38_756B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_757C")
    Jump("loc_78C0")

    label("loc_757C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_758A")
    Jump("loc_78C0")

    label("loc_758A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_759B")
    Call(0, 41)
    Jump("loc_78C0")

    label("loc_759B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_765D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B6")
    Call(0, 40)
    Jump("loc_7658")

    label("loc_75B6")


    #C0334
    ChrTalk(
        0xFE,
        (
            "退院できる患者さんを\x01",
            "市内に帰すのも、自由にという\x01",
            "わけにはいかないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "街道の《幻獣》への\x01",
            "警戒もあるんだろうけど、\x01",
            "さすがに厳しすぎる気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7658")

    Jump("loc_78C0")

    label("loc_765D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_77C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7711")

    #C0336
    ChrTalk(
        0xFE,
        (
            "こっちの病室は\x01",
            "警察関係者が入院しているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "あの二課の警部さん以外は\x01",
            "そこまでの怪我じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "そこまで入院期間も\x01",
            "長くならないとは思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_77BB")

    label("loc_7711")


    #C0339
    ChrTalk(
        0xFE,
        (
            "あの二課の警部さん……\x01",
            "意識はまだ戻っていないけど、\x01",
            "ひとまずヤマは越えたはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "３階の３０２号室に\x01",
            "入院していたと思うよ。\x01",
            "よかったらお見舞いしていくといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77BB")

    Jump("loc_78C0")

    label("loc_77C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_77CE")
    Jump("loc_78C0")

    label("loc_77CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7825")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77E9")
    Call(0, 39)
    Jump("loc_7820")

    label("loc_77E9")


    #C0341
    ChrTalk(
        0xFE,
        (
            "リットン“先生”か……\x01",
            "うーん、いい響きだなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7820")

    Jump("loc_78C0")

    label("loc_7825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7833")
    Jump("loc_78C0")

    label("loc_7833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78A9")

    #C0342
    ChrTalk(
        0xFE,
        (
            "ああ、骨もだいぶ\x01",
            "くっついてきたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "もうちょっと辛抱すれば\x01",
            "歩けるようになりますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78C0")

    label("loc_78A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78B7")
    Jump("loc_78C0")

    label("loc_78B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_78C0")

    label("loc_78C0")

    TalkEnd(0xFE)
    Return()

    # Function_38_756B end

    def Function_39_78C4(): pass

    label("Function_39_78C4")

    OP_4B(0x24, 0xFF)

    #C0344
    ChrTalk(
        0x24,
        (
            "うん、経過は順調ですね。\x01",
            "これならすぐにでも\x01",
            "退院できると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x15,
        (
            "そうかいそうかい、\x01",
            "そいつぁありがたいねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x15,
        (
            "ふふ、リットン先生も\x01",
            "なんだか頼りがいがあるねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x24,
        (
            "え、そ、そうですか？\x01",
            "いやはは……照れるなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 0)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x24, 0xFF)
    Return()

    # Function_39_78C4 end

    def Function_40_79C1(): pass

    label("Function_40_79C1")

    OP_4B(0x24, 0xFF)
    OP_4B(0x26, 0xFF)

    #C0348
    ChrTalk(
        0x24,
        "はい、術後の経過は順調ですね。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x24,
        (
            "本当ならすぐにでも\x01",
            "退院していただけるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x26,
        (
            "ああ、そういえば街道の行き来に\x01",
            "制限があるんじゃったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x26,
        (
            "やれやれ、もうしばらくは\x01",
            "入院しているしかなさそうじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 3)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x26, 0x10)
    OP_4C(0x24, 0xFF)
    OP_4C(0x26, 0xFF)
    Return()

    # Function_40_79C1 end

    def Function_41_7AB8(): pass

    label("Function_41_7AB8")

    OP_4B(0x24, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5A")

    #C0352
    ChrTalk(
        0xD,
        (
            "病院は大統領によって\x01",
            "援助を受けているものの……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xD,
        (
            "やはり、患者に広がる不安は\x01",
            "かなりのもののようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x24,
        (
            "ええ、救急車での行き来も\x01",
            "かなり制限されてますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x24,
        (
            "もしかしたら、僕みたいな\x01",
            "研修医が感じている不安が患者に\x01",
            "伝わっちゃってるのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xD,
        (
            "この場合、研修医でなくても\x01",
            "不安は感じているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "……どちらにせよ、\x01",
            "患者たちが安心できるような\x01",
            "配慮は必要だろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 2)
    Jump("loc_7D00")

    label("loc_7C5A")


    #C0358
    ChrTalk(
        0x24,
        (
            "ベルダイン先生でも\x01",
            "不安を感じる事なんて\x01",
            "あるんですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        "不安くらい誰でも感じるさ。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xD,
        (
            "……どちらにせよ、\x01",
            "患者たちが安心できるような\x01",
            "配慮は必要だろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D00")

    OP_4C(0x24, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_41_7AB8 end

    def Function_42_7D09(): pass

    label("Function_42_7D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D1A")
    Jump("loc_802A")

    label("loc_7D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7D28")
    Jump("loc_802A")

    label("loc_7D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7D36")
    Jump("loc_802A")

    label("loc_7D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E38")

    #C0361
    ChrTalk(
        0xFE,
        (
            "シズクちゃんの手術の結果には\x01",
            "賛否あるとおもうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "今までちっとも回復できなかった\x01",
            "眼の機能を少しでも改善できたのは\x01",
            "すごい事だと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "ようやく治療への\x01",
            "第一歩を踏み出したんだもの。\x01",
            "病院全体で頑張っていかなきゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_7ED3")

    label("loc_7E38")


    #C0364
    ChrTalk(
        0xFE,
        (
            "シズクちゃんがようやく治療への\x01",
            "第一歩を踏み出せたんだもの。\x01",
            "私はすごい事だと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "……でも、患者本人にしてみれば\x01",
            "やっぱり不安はあるわよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED3")

    Jump("loc_802A")

    label("loc_7ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7EE6")
    Jump("loc_802A")

    label("loc_7EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8021")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA5")

    #C0366
    ChrTalk(
        0xFE,
        (
            "セイランド教授って、\x01",
            "若いのになんだか\x01",
            "すごく風格があるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "私の求める“デキる女医”の\x01",
            "理想像はまさに彼女……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "しっかり勉強させて\x01",
            "もらわないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_801C")

    label("loc_7FA5")


    #C0369
    ChrTalk(
        0xFE,
        (
            "セイランド教授は、\x01",
            "私の求める“デキる女医”の\x01",
            "理想像にピッタリなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "しっかり勉強させて\x01",
            "もらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801C")

    Jump("loc_802A")

    label("loc_8021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_802A")

    label("loc_802A")

    TalkEnd(0xFE)
    Return()

    # Function_42_7D09 end

    def Function_43_802E(): pass

    label("Function_43_802E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8065")

    #C0371
    ChrTalk(
        0xFE,
        "はあ、いい加減退院したいわい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_80BF")

    label("loc_8065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_80BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8080")
    Call(0, 40)
    Jump("loc_80BF")

    label("loc_8080")


    #C0372
    ChrTalk(
        0xFE,
        (
            "やれやれ、もうしばらくは\x01",
            "入院しているしかなさそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80BF")

    TalkEnd(0xFE)
    Return()

    # Function_43_802E end

    def Function_44_80C3(): pass

    label("Function_44_80C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8159")

    #C0373
    ChrTalk(
        0xFE,
        (
            "一応申請が通ってね、\x01",
            "帰れることにはなったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "次に国防軍が来るのは\x01",
            "もう少し先みたいだね。\x01",
            "やれやれ、気長に待つか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F1")

    label("loc_8159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_81F1")

    #C0375
    ChrTalk(
        0xFE,
        (
            "退院して街に帰るのも\x01",
            "面倒な申請が要るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "国防軍が巡回に訪れている\x01",
            "タイミングしか帰れないし……\x01",
            "こんなことじゃあ気が滅入るよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F1")

    TalkEnd(0xFE)
    Return()

    # Function_44_80C3 end

    def Function_45_81F5(): pass

    label("Function_45_81F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8261")

    #C0377
    ChrTalk(
        0xFE,
        (
            "大統領への不満は、\x01",
            "もう言っても仕方ないですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        "今は耐える時なんじゃないかねえ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8301")

    label("loc_8261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8301")

    #C0379
    ChrTalk(
        0xFE,
        (
            "そりゃあ、大統領には\x01",
            "色々と文句はありますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "だけど、文句を言ったところで\x01",
            "独立はしてしまっているんだし、\x01",
            "ある程度仕方ないんじゃないかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8301")

    TalkEnd(0xFE)
    Return()

    # Function_45_81F5 end

    def Function_46_8305(): pass

    label("Function_46_8305")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_83C8")

    #C0381
    ChrTalk(
        0xFE,
        (
            "直接会って話したわけじゃないけど、\x01",
            "リハビリを頑張ってるイリアの姿には\x01",
            "本当に勇気付けられたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "しばらくして街に帰れたら、\x01",
            "みんなにもイリアの頑張りを\x01",
            "教えてあげたいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84C9")

    label("loc_83C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_84C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84A5")

    #C0383
    ChrTalk(
        0xFE,
        (
            "病院にはイリアが入院してるし\x01",
            "会えるかも、なんて\x01",
            "淡い期待もあったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "物凄い形相でリハビリを\x01",
            "頑張っているのを見たら、\x01",
            "ミーハー魂はぶっとんじゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "……頑張ってほしいよな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 1)
    Jump("loc_84C9")

    label("loc_84A5")


    #C0386
    ChrTalk(
        0xFE,
        "イリア……頑張ってほしいよな。\x02",
    )

    CloseMessageWindow()

    label("loc_84C9")

    TalkEnd(0xFE)
    Return()

    # Function_46_8305 end

    def Function_47_84CD(): pass

    label("Function_47_84CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8542")

    #C0387
    ChrTalk(
        0xFE,
        (
            "あーあ、ヒマだなあ。\x01",
            "病院じゃホットショットも\x01",
            "読めないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        "誰か会いにきてくれないかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_85D6")

    label("loc_8542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_85D6")

    #C0389
    ChrTalk(
        0xFE,
        (
            "複雑骨折なんかしたばっかりに\x01",
            "病院に運ばれちゃってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "かなりよくなったけど、\x01",
            "街に戻るのもかなり面倒そうだし\x01",
            "いやになっちゃうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85D6")

    TalkEnd(0xFE)
    Return()

    # Function_47_84CD end

    def Function_48_85DA(): pass

    label("Function_48_85DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8647")

    #C0391
    ChrTalk(
        0xFE,
        (
            "東の空に見える\x01",
            "あの青白い樹は一体……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "おお、女神よ。\x01",
            "わしらを救いたまえ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86C0")

    label("loc_8647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_86C0")

    #C0393
    ChrTalk(
        0xFE,
        (
            "クロスベルがどうなるか……\x01",
            "それは女神のみが知っておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "願わくば、わしらに救いの道が\x01",
            "示されん事を……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86C0")

    TalkEnd(0xFE)
    Return()

    # Function_48_85DA end

    def Function_49_86C4(): pass

    label("Function_49_86C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_874F")

    #C0395
    ChrTalk(
        0xFE,
        (
            "今日、退院できることになって\x01",
            "本当に安心しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "外はあんな状況ですけど……\x01",
            "家に帰って家族を安心させたいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87A3")

    label("loc_874F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_87A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_876A")
    Call(0, 15)
    Jump("loc_87A3")

    label("loc_876A")


    #C0397
    ChrTalk(
        0xFE,
        (
            "ふう、先生がそういうなら\x01",
            "大丈夫なんでしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87A3")

    TalkEnd(0xFE)
    Return()

    # Function_49_86C4 end

    def Function_50_87A7(): pass

    label("Function_50_87A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8825")

    #C0398
    ChrTalk(
        0xFE,
        "回診の先生方も大忙しのようだ。\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "外来が大挙して来ているそうだからな。\x01",
            "何とか頑張ってほしいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88C0")

    label("loc_8825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_88C0")

    #C0400
    ChrTalk(
        0xFE,
        (
            "病院でも色々と問題があるようだけど、\x01",
            "先生方が頑張っているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "さすがウルスラ病院というべきか……\x01",
            "私たちも安心して入院できるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88C0")

    TalkEnd(0xFE)
    Return()

    # Function_50_87A7 end

    def Function_51_88C4(): pass

    label("Function_51_88C4")

    Sound(160, 0, 100, 0)
    Return()

    # Function_51_88C4 end

    def Function_52_88CB(): pass

    label("Function_52_88CB")

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
        "まったく、あんたって子は……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xA,
        (
            "いいかげん発注のミスくらい\x01",
            "無くしてもらわないとねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xB,
        "ううん、何かの間違いですよ。\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xB,
        (
            "発注表を書くとき、\x01",
            "メイファちゃんがしっかり\x01",
            "見張ってくれてましたし㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xB,
        (
            "それでも２０回くらい\x01",
            "桁を間違えちゃいましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "……はあ、メイファの\x01",
            "苦労が知れるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#00005Fあの……\x01",
            "何かあったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0409
    ChrTalk(
        0xA,
        "ああ、あんたたちかい。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xA,
        (
            "いやね、この子に\x01",
            "医療用品の発注を\x01",
            "任せたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xA,
        (
            "荷物が届いてみたら、\x01",
            "中にボロっちい人形が\x01",
            "入っていたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xA,
        (
            "この子ったら、以前も\x01",
            "ワケの分からない雑貨を\x01",
            "間違って注文したのよねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xB,
        (
            "ひーん、信じてくださいよ。\x01",
            "今回はちゃんとできたんですってば。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x103,
        "#00200Fロイドさん、やっぱり……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        "#00003Fああ、裏がとれたな。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0416
    ChrTalk(
        0xA,
        "どういうことだい？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        "#00012Fえっとですね……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0418
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは荷物の誤配が\x01",
            "あったことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0419
    ChrTalk(
        0xA,
        (
            "誤配ねえ……\x01",
            "そういうことだったのかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x109,
        (
            "#10100F今、自分たちで\x01",
            "再配達をしている最中なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#00000F病院宛ての荷物って\x01",
            "これのことですよね？\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x330),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x330, 1)

    #C0423
    ChrTalk(
        0xA,
        (
            "ふむ……確かにこれは\x01",
            "発注を頼んどいた医療用具だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xA,
        (
            "わざわざ届けてくれて\x01",
            "ありがとうよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0425
    ChrTalk(
        0xA,
        (
            "それと……\x01",
            "すまなかったねえシロン。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xA,
        (
            "今回ばかりはあたしの\x01",
            "早とちりだったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xB,
        (
            "うふふ、いいですよ。\x01",
            "全然気にしてませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xB,
        (
            "あ、そうだ。\x01",
            "アレも入ってるかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0429
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "シロンは荷物の奥に\x01",
            "手を入れてまさぐりだした。\x07\x00\x02",
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
            "あ、あったあ！\x01",
            "“カゲマル”のストラップ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xB,
        (
            "発注のついでに、\x01",
            "一緒に頼んでおいたんですよ。\x01",
            "うふふ、かわいいな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xA,
        (
            "……シロン、あんたやっぱり\x01",
            "あとでお説教だね。\x02",
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
            "#00006Fえ、えーっと……\x02\x03",

            "#00000Fすみませんが、誤配された\x01",
            "荷物を預からせてもらっても\x01",
            "いいでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0434
    ChrTalk(
        0xA,
        (
            "ああ、それもそうだね。\x01",
            "ちょっと待っとくれ。\x02",
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
            "ほら、これさ。\x01",
            "よろしく頼んだよ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x33A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33A, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0437
    ChrTalk(
        0x101,
        (
            "#00000Fありがとうございます。\x02\x03",

            "#00003Fええと、アロンさんから\x01",
            "もらった伝票によると……\x02\x03",

            "#00000F届け先は住宅街の民家だったな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_92D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92D7)
    Sleep(50)

    def lambda_92E7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92E7)
    Sleep(300)

    #C0438
    ChrTalk(
        0x103,
        (
            "#00200Fそれを届ければ\x01",
            "晴れて依頼達成ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x105,
        (
            "#10305F住宅街っていえば、\x01",
            "マクダエル議長邸も\x01",
            "住宅街の一角にあるよね。\x02\x03",

            "#10300Fエリィ、この住所って\x01",
            "どのへんなんだい？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_93A4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_93A4)
    Sleep(50)

    def lambda_93B4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93B4)
    Sleep(300)

    #C0440
    ChrTalk(
        0x102,
        "#00103Fええと、そうね……\x02",
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
            "#00105Fあれ、この住所って……\x02\x03",

            "キャンベル議員宅の\x01",
            "隣の空き家じゃない。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95CC")
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
            "住宅街の空き家を？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",                        # 0
            "【怪盗Ｂクエストで入った】\x01",            # 1
            "【前編不在住戸クエストで調べた】\x01",      # 2
            "【調べたことがない】\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95B2")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x1, 0x2)
    Jump("loc_95CC")

    label("loc_95B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95CC")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x2, 0x2)

    label("loc_95CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9650")

    #C0443
    ChrTalk(
        0x101,
        (
            "#00005F確か、十年くらい前に\x01",
            "お化け屋敷だって\x01",
            "騒がれてたっていう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        "#00101Fえ、ええ……間違いないわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_96F4")

    label("loc_9650")


    #C0445
    ChrTalk(
        0x101,
        (
            "#00005Fそれって、確か\x01",
            "共和国派議員の名前だったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x102,
        (
            "#00103Fええ……\x01",
            "住宅街の北側に屋敷があるの。\x02\x03",

            "#00101Fお隣は、十年以上\x01",
            "空き家になってたはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96F4")


    #C0447
    ChrTalk(
        0x104,
        (
            "#00305F……どういうことなんだ？\x02\x03",

            "#00300F最近になって\x01",
            "入居者でもあったのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        "#00106Fううん、ちょっと分からないわ。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#00000F……とにかく、\x01",
            "一応荷物を届けに行ってみよう。\x02",
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

    # Function_52_88CB end

    def Function_53_9805(): pass

    label("Function_53_9805")

    EventBegin(0x1)

    #C0450
    ChrTalk(
        0x101,
        (
            "#00000Fフランの病室は３０１号室だったな。\x01",
            "早いところ様子を見に行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 8600, 0, 3680, 180)
    EventEnd(0x4)
    Return()

    # Function_53_9805 end

    def Function_54_9868(): pass

    label("Function_54_9868")

    EventBegin(0x1)

    #C0451
    ChrTalk(
        0x101,
        (
            "#00000Fフランの病室は３０１号室だったな。\x01",
            "早いところ様子を見に行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 26800, 0, -25170, 0)
    EventEnd(0x4)
    Return()

    # Function_54_9868 end

    SaveToFile()

Try(main)
