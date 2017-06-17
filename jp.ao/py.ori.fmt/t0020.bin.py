from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0020.bin",                # FileName
        "t0020",                    # MapName
        "t0020",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 4, 0, 5],
    )

    BuildStringList((
        "t0020",                  # 0
        "レオール老人",           # 1
        "ジェイク",               # 2
        "ゴーファン",             # 3
        "シーリィ",               # 4
        "キース",                 # 5
        "アルフレッド",           # 6
        "アレサ",                 # 7
        "カミーユ",               # 8
        "プーリー",               # 9
        "ステファン",             # 10
        "デリック",               # 11
        "アンジェ",               # 12
        "シスター・ハティナ",     # 13
        "ハロルド",               # 14
        "ソフィア",               # 15
        "コリン",                 # 16
        "ケビン神父",             # 17
        "シスター・リース",       # 18
        "遊撃士リン",             # 19
        "遊撃士エオリア",         # 20
        "遊撃士スコット",         # 21
        "チルル",                 # 22
        "料理",                   # 23
        "料理",                   # 24
        "料理",                   # 25
        "料理",                   # 26
        "料理",                   # 27
        "料理",                   # 28
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch25200.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch24402.itc",                   # 04
        "chr/ch21002.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch22702.itc",                   # 07
        "chr/ch24600.itc",                   # 08
        "chr/ch24700.itc",                   # 09
        "chr/ch20600.itc",                   # 0A
        "chr/ch32300.itc",                   # 0B
        "chr/ch32302.itc",                   # 0C
        "chr/ch24300.itc",                   # 0D
        "chr/ch25500.itc",                   # 0E
        "chr/ch09300.itc",                   # 0F
        "chr/ch32002.itc",                   # 10
        "chr/ch32102.itc",                   # 11
        "chr/ch09400.itc",                   # 12
        "chr/ch09402.itc",                   # 13
        "chr/ch07202.itc",                   # 14
        "chr/ch09302.itc",                   # 15
        "chr/ch11402.itc",                   # 16
        "chr/ch11500.itc",                   # 17
        "chr/ch27202.itc",                   # 18
        "chr/ch20502.itc",                   # 19
    ))

    DeclNpc(-40529,  0,       3470,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-48360,  0,       769,     90,   261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-39,     0,       6039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(699,     0,       2049,    90,   261,  0x0, 0,   3,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(7849,    180,     2460,    0,    261,  0x0, 0,   4,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-2059,   180,     4000,    0,    261,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(139320,  500,     360,     180,  261,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(78019,   0,       -370,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(79169,   0,       -129,    315,  389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(76849,   0,       -170,    90,   389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(112559,  0,       -509,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(141600,  0,       -1000,   180,  389,  0x0, 0,   13,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(78000,   189,     1500,    180,  389,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(112559,  0,       -509,    270,  389,  0x0, 0,   15,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(71449,   0,       -1600,   0,    389,  0x0, 0,   18,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(74000,   100,     -1750,   0,    388,  0x0, 0,   20,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(69290,   500,     790,     180,  452,  0x0, 0,   22,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(69379,   0,       -1190,   0,    453,  0x0, 0,   23,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-2509,   180,     1179,    270,  389,  0x0, 0,   16,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(-3380,   189,     -810,    0,    389,  0x0, 0,   17,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(-2509,   180,     1179,    270,  452,  0x0, 0,   24,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(3549,    180,     -2000,   70,   452,  0x0, 0,   25,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(-3500,   800,     -349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-4719,   800,     289,     0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-4190,   800,     1519,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-3150,   800,     699,     0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-4380,   800,     -349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-4739,   800,     1000,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(270,     0,       4460,    1000,    -40,     1500,    6040,    0x007E, 0,  11, 0x0000)
    DeclActor(-46360,  0,       30,      1000,    -48360,  1500,    770,     0x007E, 0,  9,  0x0000)
    DeclActor(86250,   0,       2050,    1200,    86250,   2500,    2050,    0x007C, 0,  6,  0x0000)
    DeclActor(6400,    0,       8900,    1200,    6400,    1700,    8900,    0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1380, 0)                                       # 0

    ScpFunction((
        "Function_0_564",          # 00, 0
        "Function_1_61C",          # 01, 1
        "Function_2_6CD",          # 02, 2
        "Function_3_6F8",          # 03, 3
        "Function_4_723",          # 04, 4
        "Function_5_B30",          # 05, 5
        "Function_6_BA8",          # 06, 6
        "Function_7_C50",          # 07, 7
        "Function_8_D4C",          # 08, 8
        "Function_9_1DBD",         # 09, 9
        "Function_10_1DC1",        # 0A, 10
        "Function_11_2C66",        # 0B, 11
        "Function_12_2C6A",        # 0C, 12
        "Function_13_3F1E",        # 0D, 13
        "Function_14_4C68",        # 0E, 14
        "Function_15_4D9A",        # 0F, 15
        "Function_16_5A78",        # 10, 16
        "Function_17_6C7D",        # 11, 17
        "Function_18_76BD",        # 12, 18
        "Function_19_7749",        # 13, 19
        "Function_20_77BF",        # 14, 20
        "Function_21_7A36",        # 15, 21
        "Function_22_7F2A",        # 16, 22
        "Function_23_7FC9",        # 17, 23
        "Function_24_80E7",        # 18, 24
        "Function_25_8207",        # 19, 25
        "Function_26_8F28",        # 1A, 26
        "Function_27_90D5",        # 1B, 27
        "Function_28_910F",        # 1C, 28
        "Function_29_9149",        # 1D, 29
        "Function_30_9369",        # 1E, 30
        "Function_31_973D",        # 1F, 31
        "Function_32_9C6A",        # 20, 32
        "Function_33_9E2A",        # 21, 33
        "Function_34_9FD1",        # 22, 34
        "Function_35_A096",        # 23, 35
        "Function_36_AF10",        # 24, 36
        "Function_37_B01C",        # 25, 37
        "Function_38_B1C4",        # 26, 38
        "Function_39_C036",        # 27, 39
        "Function_40_C406",        # 28, 40
        "Function_41_D002",        # 29, 41
        "Function_42_D514",        # 2A, 42
        "Function_43_D941",        # 2B, 43
        "Function_44_DE9F",        # 2C, 44
        "Function_45_E9A2",        # 2D, 45
        "Function_46_FA0E",        # 2E, 46
        "Function_47_FA57",        # 2F, 47
        "Function_48_FAA0",        # 30, 48
        "Function_49_FAE9",        # 31, 49
    ))


    def Function_0_564(): pass

    label("Function_0_564")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5A4"),
        (1, "loc_5B0"),
        (2, "loc_5BC"),
        (3, "loc_5C8"),
        (4, "loc_5D4"),
        (5, "loc_5E0"),
        (6, "loc_5EC"),
        (SWITCH_DEFAULT, "loc_5F8"),
    )


    label("loc_5A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_61B")

    Return()

    # Function_0_564 end

    def Function_1_61C(): pass

    label("Function_1_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CC")
    OP_95(0xFE, 700, 0, 2050, 2000, 0x0)
    OP_95(0xFE, 6210, 0, 2640, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 2810, 0, 1030, 2000, 0x0)
    OP_95(0xFE, 3120, 0, -560, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -2050, 0, -820, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    Jump("Function_1_61C")

    label("loc_6CC")

    Return()

    # Function_1_61C end

    def Function_2_6CD(): pass

    label("Function_2_6CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F7")
    OP_94(0xFE, 0x229CA, 0xFFFFF754, 0x23212, 0xFFFFFF9C, 0x3E8)
    Sleep(250)
    Jump("Function_2_6CD")

    label("loc_6F7")

    Return()

    # Function_2_6CD end

    def Function_3_6F8(): pass

    label("Function_3_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_722")
    OP_94(0xFE, 0x8AAC, 0x3E8, 0xB5A4, 0xFFFFFC7C, 0x7D0)
    Sleep(250)
    Jump("Function_3_6F8")

    label("loc_722")

    Return()

    # Function_3_6F8 end

    def Function_4_723(): pass

    label("Function_4_723")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76B")
    SetChrChipByIndex(0x1A, 0x10)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1B, 0x11)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_76B")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0x17, 0x14)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7D8")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x16)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_B15")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_801")
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 78010, 0, 2060, 0)
    Jump("loc_B15")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_887")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x15, 0x15)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 82040, 180, -1400, 45)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 81720, 0, 220, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C")
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)

    label("loc_86C")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 73950, 400, 800, 180)
    Jump("loc_B15")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8E8")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 71500, 0, 0, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 71500, 0, -1000, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 73950, 400, 800, 180)
    Jump("loc_B15")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_923")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 142940, 0, -770, 180)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_B15")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_931")
    Jump("loc_B15")

    label("loc_931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_964")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_B15")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_972")
    Jump("loc_B15")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9A9")
    SetChrPos(0xE, 41000, 0, 0, 180)
    BeginChrThread(0xE, 0, 0, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A4")
    ClearChrFlags(0x12, 0x80)

    label("loc_9A4")

    Jump("loc_B15")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9E8")
    SetChrPos(0xE, 73600, 0, -960, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D2")
    SetChrFlags(0xD, 0x10)

    label("loc_9D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9E3")
    ClearChrFlags(0x12, 0x80)

    label("loc_9E3")

    Jump("loc_B15")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A9E")
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x18)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x19)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    SetChrPos(0xE, 41000, 0, 0, 180)
    BeginChrThread(0xE, 0, 0, 3)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 7850, 0, 5660, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5F")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A72")
    SetChrFlags(0xD, 0x10)

    label("loc_A72")

    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1920, 180, 4000, 0)
    SetChrChipByIndex(0x12, 0xC)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_B15")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_AAC")
    Jump("loc_B15")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_ADA")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0xE, 141600, 0, -2000, 0)
    SetChrFlags(0xE, 0x10)
    Jump("loc_B15")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AFE")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_B15")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B0C")
    Jump("loc_B15")

    label("loc_B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B15")

    label("loc_B15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2F")
    Event(0, 45)

    label("loc_B2F")

    Return()

    # Function_4_723 end

    def Function_5_B30(): pass

    label("Function_5_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_B42")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B68")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_B68")

    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B94")
    SetMapObjFrame(0xFF, "tuika00", 0x1, 0x1)

    label("loc_B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA7")
    OP_1B(0x3, 0x0, 0x23)

    label("loc_BA7")

    Return()

    # Function_5_B30 end

    def Function_6_BA8(): pass

    label("Function_6_BA8")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『導力車フリークvol.2』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x372, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『ポップカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x372, 1)

    label("loc_C4C")

    TalkEnd(0xFF)
    Return()

    # Function_6_BA8 end

    def Function_7_C50(): pass

    label("Function_7_C50")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★トネリコ亭・おすすめ料理★\x01",
            "　 ～　匠風オムライス　～\x02",
        )
    )

    CloseMessageWindow()

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "匠風オムライスのレシピが書かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_D48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『匠風オムライス』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D48")

    TalkEnd(0xFF)
    Return()

    # Function_7_C50 end

    def Function_8_D4C(): pass

    label("Function_8_D4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7B")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E83")

    #C0006
    ChrTalk(
        0x8,
        (
            "得体のしれん大樹が現れて、\x01",
            "ジェイクが萎縮してしまわんか\x01",
            "心配だったのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "ハロルドくんの一言で\x01",
            "逆にやる気を発揮したようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "商人にとって最も大切な商魂……\x01",
            "それが芽生えたジェイクは\x01",
            "これからもきっと大丈夫じゃろうて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F15")

    label("loc_E83")


    #C0009
    ChrTalk(
        0x8,
        (
            "商人にとって最も大切な商魂……\x01",
            "ジェイクにもそれが芽生えおった。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "クロスベルが今度どうなってしまおうと、\x01",
            "もうわしに思い残す事はないわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F15")

    Jump("loc_1DB9")

    label("loc_F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101A")

    #C0011
    ChrTalk(
        0x8,
        (
            "ハロルドくんは、ソフィア殿や\x01",
            "コリンくんという家族の存在に\x01",
            "しっかりと支えられておるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ふむ、ジェイクにもそのような\x01",
            "存在がいればあるいは……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "隠居したら、本格的に\x01",
            "孫の嫁探しをするのも\x01",
            "悪くないかもしれんのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_108D")

    label("loc_101A")


    #C0014
    ChrTalk(
        0x8,
        (
            "ふむ、ジェイクにも\x01",
            "公私共に支えてくれる\x01",
            "嫁が見つかれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "孫の嫁探しをするのも\x01",
            "悪くないかもしれんのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108D")

    Jump("loc_1DB9")

    label("loc_1092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A6")

    #C0016
    ChrTalk(
        0x8,
        (
            "ハロルドくんは、\x01",
            "国防軍からの物資の支給に関して\x01",
            "色々と交渉してくれているのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "いくら自給自足の成り立っている\x01",
            "この村とて、常備薬などは\x01",
            "かなり必要になってくるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "ジェイクのやつも、あれくらい\x01",
            "出来るようになってくれればのう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1252")

    label("loc_11A6")


    #C0019
    ChrTalk(
        0x8,
        (
            "ジェイクのやつも、\x01",
            "ハロルドくん位の商人に\x01",
            "なってくれればのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "……いかんいかん、最近せっかく\x01",
            "やる気をだしてきておるんじゃ。\x01",
            "あまり小言は言わんようにせんとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1252")

    Jump("loc_1DB9")

    label("loc_1257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1354")

    #C0021
    ChrTalk(
        0x8,
        (
            "少し前から、ジェイクが\x01",
            "人が変わったように\x01",
            "やる気を出しはじめてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "まだまだ未熟だが、\x01",
            "わしもようやく安心できる\x01",
            "というもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "いつか《ジェイク雑貨店》の\x01",
            "看板を掲げられるよう、\x01",
            "改めて教え込んでやらねばのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FA")

    label("loc_1354")


    #C0024
    ChrTalk(
        0x8,
        (
            "ジェイクがようやく\x01",
            "やる気を出してくれた。\x01",
            "わしも安心できるというもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "いつか《ジェイク雑貨店》の\x01",
            "看板を掲げられるよう、\x01",
            "改めて教え込んでやらねばのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_1DB9")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_152A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C9")

    #C0026
    ChrTalk(
        0x8,
        (
            "昨日痛めたコシが\x01",
            "まだよくならんわい。\x01",
            "わしも歳じゃのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "はて、それにしても\x01",
            "ジェイクの奴……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "今日はなんだかいつもと\x01",
            "様子が違うようじゃ。\x01",
            "何かあったのかのう？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1525")

    label("loc_14C9")


    #C0029
    ChrTalk(
        0x8,
        (
            "ジェイクの奴……\x01",
            "今日はなんだかいつもと\x01",
            "様子が違うようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "何かあったのかのう？\x02",
    )

    CloseMessageWindow()

    label("loc_1525")

    Jump("loc_1DB9")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1739")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D3")

    #C0031
    ChrTalk(
        0x8,
        (
            "どうやら今日は、\x01",
            "ミンネス殿が最後の商談を\x01",
            "しにくるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "いよいよデリックとの計画が\x01",
            "始動するのかのう。\x01",
            "いやはや、楽しみじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1734")

    label("loc_15D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A8")

    #C0033
    ChrTalk(
        0x8,
        (
            "ふと窓の外をみたら、\x01",
            "広場に魔獣どもがおってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "しかも様子を見る限り、\x01",
            "あのミンネス殿が操って\x01",
            "おったようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "あんまり驚いた拍子に、\x01",
            "コシを痛めてしもうたわい。\x01",
            "あたたた……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1734")

    label("loc_16A8")


    #C0036
    ChrTalk(
        0x8,
        (
            "広場に現れた魔獣は、\x01",
            "あのミンネス殿が操って\x01",
            "おったようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "あんまり驚いた拍子に、\x01",
            "コシを痛めてしもうたわい。\x01",
            "あたたた……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1734")

    Jump("loc_1DB9")

    label("loc_1739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B9")

    #C0038
    ChrTalk(
        0x8,
        (
            "最近、ハロルドくんに次いで\x01",
            "見込みのある男に出会ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "ほほ、色々とよくして\x01",
            "もらっておるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183C")

    label("loc_17B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C8")
    Jump("loc_183C")

    label("loc_17C8")


    #C0040
    ChrTalk(
        0x8,
        (
            "あの男は、\x01",
            "村のハチミツをとても\x01",
            "気に入ってくれてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "うむうむ、さぞかし\x01",
            "名のある商売人に\x01",
            "違いなかろうて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183C")

    Jump("loc_1DB9")

    label("loc_1841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_199D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1916")

    #C0042
    ChrTalk(
        0x8,
        (
            "わしもそろそろ隠居して、\x01",
            "店をジェイクに任せたいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "あやつはなかなか\x01",
            "やる気になってくれんでな。\x01",
            "いつもぼーっとしておるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "ふむ、何かきっかけでも\x01",
            "あればいいんじゃが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1998")

    label("loc_1916")


    #C0045
    ChrTalk(
        0x8,
        (
            "ジェイクの奴は、\x01",
            "本当に店を継いでくれる気が\x01",
            "あるのかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "なにか、やる気が出る\x01",
            "きっかけでもあれば\x01",
            "いいんじゃがのう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1998")

    Jump("loc_1DB9")

    label("loc_199D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A70")

    #C0047
    ChrTalk(
        0x8,
        (
            "最近はどうもコシの調子が悪い。\x01",
            "わしもそろそろ歳じゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "やはり、近いうちに\x01",
            "ジェイクに店を任せて\x01",
            "隠居したいものだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "どうやったらこの孫が\x01",
            "やる気を出してくれるかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AEF")

    label("loc_1A70")


    #C0050
    ChrTalk(
        0x8,
        (
            "わしも歳じゃ、近いうちに\x01",
            "ジェイクに店を任せて\x01",
            "隠居したいものだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "本人にやる気がないからのう。\x01",
            "前途多難じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEF")

    Jump("loc_1DB9")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_1CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C01")

    #C0052
    ChrTalk(
        0x8,
        (
            "赤毛の厳つい男……\x01",
            "おーおー、確かに最近\x01",
            "そんな男が仲間と来たぞい。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "何やら物々しい連中じゃったが、\x01",
            "うちの商品をたくさん買い込んでくれてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "ジェイクのやつは怯えておったが、\x01",
            "ひさびさの上客じゃったわい。\x01",
            "ほっほっほ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CA5")

    label("loc_1C01")


    #C0055
    ChrTalk(
        0x8,
        (
            "赤毛の厳つい男は、\x01",
            "ひさびさの上客じゃったわい。\x01",
            "ほっほっほ……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "ジェイクのやつは怯えておったが、\x01",
            "客を見かけで判断してはいかん。\x01",
            "あやつもまだまだじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA5")

    Jump("loc_1DB9")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D59")

    #C0057
    ChrTalk(
        0x8,
        (
            "先ほど、ハロルドくんが\x01",
            "取引きにやってきおったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "いや、やはり彼は\x01",
            "見込みのある商人じゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "ジェイクのやつに\x01",
            "爪の垢を煎じて飲ませたいわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB9")

    label("loc_1D59")


    #C0060
    ChrTalk(
        0x8,
        (
            "ハロルドくんは\x01",
            "見込みのある商人じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "ジェイクのやつに\x01",
            "爪の垢を煎じて飲ませたいわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB9")

    TalkEnd(0xFE)
    Return()

    # Function_8_D4C end

    def Function_9_1DBD(): pass

    label("Function_9_1DBD")

    Call(0, 10)
    Return()

    # Function_9_1DBD end

    def Function_10_1DC1(): pass

    label("Function_10_1DC1")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C62")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1E4B")
    OP_AF(0x4F)
    Jump("loc_1E7D")

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E5B")
    OP_AF(0x4E)
    Jump("loc_1E7D")

    label("loc_1E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E6B")
    OP_AF(0x4D)
    Jump("loc_1E7D")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E7B")
    OP_AF(0x4C)
    Jump("loc_1E7D")

    label("loc_1E7B")

    OP_AF(0x4B)

    label("loc_1E7D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C5D")

    label("loc_1E8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA0")
    Jump("loc_2C5D")

    label("loc_1EA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB8")
    TalkEnd(0x9)
    Return()

    label("loc_1EB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2036")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC9")

    #C0062
    ChrTalk(
        0x9,
        (
            "ハロルドさんが帰り際に、\x01",
            "俺にアドバイスをくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "『こういう時こそ、みんなのために\x01",
            "  商売を頑張るのが僕達の使命だよ』\x01",
            "……ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "俺が商売をすることで\x01",
            "誰かの助けになるなら、\x01",
            "死ぬ気でやってみないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2031")

    label("loc_1FC9")


    #C0065
    ChrTalk(
        0x9,
        (
            "俺が商売をすることで\x01",
            "誰かの助けになるなら、\x01",
            "死ぬ気でやってみないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "よーし……やるぞっ！！\x02",
    )

    CloseMessageWindow()

    label("loc_2031")

    Jump("loc_2C5D")

    label("loc_2036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_20C8")

    #C0067
    ChrTalk(
        0x9,
        (
            "な、なんかじいちゃんが\x01",
            "不穏な事を企んでる気がするな……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "こんな時なんだし、農作物の収穫が\x01",
            "落ち込んでる事を心配しろっての。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5D")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_223D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C6")

    #C0069
    ChrTalk(
        0x9,
        (
            "この間、ハロルドさんが\x01",
            "国防軍と交渉してるのを見て、\x01",
            "俺もまだまだだと思ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "店を継ぐつもりだったら、\x01",
            "ああいうことが本格的に\x01",
            "出来るようにならないとなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "折角だし、ハロルドさんに\x01",
            "アドバイスをもらおうかなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2238")

    label("loc_21C6")


    #C0072
    ChrTalk(
        0x9,
        (
            "じいちゃんの言いたい事は\x01",
            "顔を見てれば大体わかるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "俺もハロルドさんみたいな\x01",
            "立派な商人にならないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2238")

    Jump("loc_2C5D")

    label("loc_223D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CC")

    #C0074
    ChrTalk(
        0x9,
        (
            "どうもいらっしゃい、\x01",
            "《レオール雑貨店》にようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "オススメは特産品のハチミツさ。\x01",
            "ぜひ見てってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2330")

    label("loc_22CC")


    #C0076
    ChrTalk(
        0x9,
        (
            "……どうだ、なかなか\x01",
            "サマになってるだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "へへ、店を継ぐのを本格的に\x01",
            "考えてみようかなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2330")

    Jump("loc_2C5D")

    label("loc_2335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2416")

    #C0078
    ChrTalk(
        0x9,
        (
            "昨日じいちゃんが\x01",
            "腰を痛めちゃってさ。\x01",
            "今日は休んでりゃいいのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "でも、多分俺が頼りないから\x01",
            "店に出てないと心配なんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "……はあ、何やってんだろ俺。\x01",
            "もっとがんばんなきゃな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24AB")

    label("loc_2416")


    #C0081
    ChrTalk(
        0x9,
        (
            "雑貨屋を継ぐなんて、\x01",
            "あんまり乗り気じゃないし、\x01",
            "やる気もでなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "じいちゃんに心配かけないためにも、\x01",
            "もっとがんばってみようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AB")

    Jump("loc_2C5D")

    label("loc_24B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255D")

    #C0083
    ChrTalk(
        0x9,
        (
            "アルモリカの改革なんていう\x01",
            "話が出てるみたいだけど……\x01",
            "どうなんのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "俺は別に、今まで通りでも\x01",
            "構わないんだけどなー。\x01",
            "気楽でいいし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D0")

    label("loc_255D")


    #C0085
    ChrTalk(
        0x9,
        (
            "じいちゃん、\x01",
            "さっき腰が痛そうだったけど\x01",
            "大丈夫かな……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "あ、そうだ、奥から湿布を\x01",
            "もってきてやんねーと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D0")

    Jump("loc_2C5D")

    label("loc_25D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C0")

    #C0087
    ChrTalk(
        0x9,
        (
            "最近よく村で見かける\x01",
            "身なりのいい人がいるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "どうやらじいちゃん、その人に\x01",
            "『出来のいいお孫さんをお持ちで』とか\x01",
            "言われて喜んでるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……さすがにお世辞だと\x01",
            "思うんだけどなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272B")

    label("loc_26C0")


    #C0090
    ChrTalk(
        0x9,
        (
            "じいちゃん、\x01",
            "俺のことを褒められて\x01",
            "喜んでるらしくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "……さすがにお世辞だと\x01",
            "思うんだけどなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272B")

    Jump("loc_2C5D")

    label("loc_2730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_288B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2805")

    #C0092
    ChrTalk(
        0x9,
        (
            "そろそろじいちゃんに\x01",
            "『店を継ぐつもりはない』って\x01",
            "ハッキリ言わないとだめかなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "でも、言うとじいちゃん、\x01",
            "がっかりするだろうなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "……まあいいか、\x01",
            "しばらくこのままで。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2886")

    label("loc_2805")


    #C0095
    ChrTalk(
        0x9,
        (
            "給料は出るし、忙しくないし……\x01",
            "アルバイトだと思えば\x01",
            "雑貨屋も割がいいんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "……まあいいか、\x01",
            "しばらくこのままで。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2886")

    Jump("loc_2C5D")

    label("loc_288B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2927")

    #C0097
    ChrTalk(
        0x9,
        (
            "じいちゃんは俺に\x01",
            "店を継がせるつもりらしいけど……\x01",
            "正直、めんどいんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "将来は街に出て、\x01",
            "一山当てたいんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_297C")

    label("loc_2927")


    #C0099
    ChrTalk(
        0x9,
        "店を継ぐのは、正直ゴメンだなー。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "将来は街に出て、\x01",
            "一山当てたいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_297C")

    Jump("loc_2C5D")

    label("loc_2981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_2B04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A78")

    #C0101
    ChrTalk(
        0x9,
        (
            "赤毛の大男……？\x01",
            "そういや、ちょっと前に\x01",
            "そんな男が仲間と来たっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "じいちゃんは儲かったって\x01",
            "喜んでたけど……\x01",
            "俺はなんだか怖かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "あいつら絶対カタギじゃないもの。\x01",
            "何か企んでるに違いねえぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AFF")

    label("loc_2A78")


    #C0104
    ChrTalk(
        0x9,
        (
            "赤毛の大男……\x01",
            "絶対カタギじゃないし、\x01",
            "俺はなんだか怖かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "……でも、一緒にいた赤毛の女の子は\x01",
            "ちょっとかわいかったなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFF")

    Jump("loc_2C5D")

    label("loc_2B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD5")

    #C0106
    ChrTalk(
        0x9,
        (
            "どーも、いらっしゃいませ。\x01",
            "お好きに見てってくれ……クダサイ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "村の特産品であるハチミツも\x01",
            "ここでとりあつかってるぜ……マスヨ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "……ふう、丁寧な言葉遣いって\x01",
            "やっぱりニガテだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C5D")

    label("loc_2BD5")


    #C0109
    ChrTalk(
        0x9,
        (
            "うちのじいちゃん、なにかにつけて\x01",
            "ハロルドさんを見習えって言うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "あんなベテランの商人さんと\x01",
            "比べられても、正直荷が重いよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5D")

    Jump("loc_1DCE")

    label("loc_2C62")

    TalkEnd(0x9)
    Return()

    # Function_10_1DC1 end

    def Function_11_2C66(): pass

    label("Function_11_2C66")

    Call(0, 12)
    Return()

    # Function_11_2C66 end

    def Function_12_2C6A(): pass

    label("Function_12_2C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB3")
    Call(0, 40)
    Return()

    label("loc_2CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CE1")
    Call(0, 41)
    Return()

    label("loc_2CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D0F")
    Call(0, 43)
    Return()

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D26")
    Call(0, 44)
    Return()

    label("loc_2D26")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DA6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2DA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC6")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F15")

    label("loc_2DC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE6")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F15")

    label("loc_2DE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DFA")
    Jump("loc_3F15")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E12")
    TalkEnd(0xA)
    Return()

    label("loc_2E12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F15")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_2EB8")

    #C0111
    ChrTalk(
        0xA,
        (
            "あそこまで絶賛されると\x01",
            "なんだか照れてしまうなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "はは、是非ともうちが\x01",
            "繁盛してくれるような記事を\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F15")

    label("loc_2EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_306B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE1")

    #C0113
    ChrTalk(
        0xA,
        (
            "あの青白い巨大な樹の出現には\x01",
            "かなり驚かされたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "とんでもない状況だけど……\x01",
            "こういうときこそ、\x01",
            "一度手を休めるのも大事だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "ついさっきも、疲れ果てた\x01",
            "神父様とシスターさんが\x01",
            "やってきたところでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "彼らにも後で、コーヒーでも\x01",
            "持って行ってやらないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3066")

    label("loc_2FE1")


    #C0117
    ChrTalk(
        0xA,
        (
            "ついさっき、疲れ果てた\x01",
            "神父様とシスターさんが\x01",
            "やってきたところでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "彼らにも後で、コーヒーでも\x01",
            "持って行ってやらないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3066")

    Jump("loc_3F15")

    label("loc_306B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_31F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3172")

    #C0119
    ChrTalk(
        0xA,
        (
            "例の無効宣言の噂は、\x01",
            "この村にも届いてきてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "もともと村では大統領に\x01",
            "あまりいい印象はなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "今回は流石に街の人も、\x01",
            "疑問に感じたんじゃないかなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "これからどんな展開になるか……\x01",
            "個人的には目が離せないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31F2")

    label("loc_3172")


    #C0123
    ChrTalk(
        0xA,
        (
            "今回は流石に街の人も、大統領を\x01",
            "疑問に感じたんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "これからどんな展開になるか……\x01",
            "個人的には目が離せないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F2")

    Jump("loc_3F15")

    label("loc_31F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_33B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3307")

    #C0125
    ChrTalk(
        0xA,
        (
            "ハロルド君とご家族は、\x01",
            "２階の大部屋に滞在しているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "まあ、クロスベルがこんな状況で\x01",
            "新規のお客も来ないだろうしね。\x01",
            "困ったときはお互い様だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "村の事も色々手伝ってくれてるし、\x01",
            "部屋を貸したくらいじゃ\x01",
            "申し訳ないくらいなんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33AD")

    label("loc_3307")


    #C0128
    ChrTalk(
        0xA,
        (
            "それにしても、ハロルド君も\x01",
            "せっかくの休暇だというのに、\x01",
            "運が悪かったよなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "村としては大助かりだけど……\x01",
            "街に帰れないというのも\x01",
            "なかなか不安じゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33AD")

    Jump("loc_3F15")

    label("loc_33B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3599")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3468")

    #C0130
    ChrTalk(
        0xA,
        (
            "ゲバルさんは、うちの味を気に入って\x01",
            "市内から通ってくれてるんだと\x01",
            "思ってたんだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        "……今は、どこに滞在してるんだろうね？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3594")

    label("loc_3468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352C")

    #C0132
    ChrTalk(
        0xA,
        (
            "この間の襲撃事件は、\x01",
            "クロスベル自治州全体の\x01",
            "平和を揺るがす問題だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "国境の緊張状態も\x01",
            "より強まっているというし……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "クロスベルは一体、\x01",
            "どうなってしまうんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3594")

    label("loc_352C")


    #C0135
    ChrTalk(
        0xA,
        (
            "国境の緊張状態も\x01",
            "より強まっているというし……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "クロスベルは一体、\x01",
            "どうなってしまうんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3594")

    Jump("loc_3F15")

    label("loc_3599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365E")

    #C0137
    ChrTalk(
        0xA,
        (
            "今日は日曜学校のために、\x01",
            "２階の大部屋を貸し出してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "さて、子供たちに\x01",
            "おやつのプリンでも\x01",
            "作ってあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "おっと、もちろん\x01",
            "シスターさんの分もね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36D1")

    label("loc_365E")


    #C0140
    ChrTalk(
        0xA,
        (
            "今日は２階の大部屋で\x01",
            "日曜学校をやってるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "みんなのために、\x01",
            "おやつのプリンでも\x01",
            "作ってあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D1")

    Jump("loc_3F15")

    label("loc_36D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_38EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377A")

    #C0142
    ChrTalk(
        0xA,
        (
            "デリック君に、ここ最近\x01",
            "村長と離れて何をやっていたのか\x01",
            "一通り聞く事ができたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "しかし、大丈夫なのかな。\x01",
            "新しい事業だなんて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E7")

    label("loc_377A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3860")

    #C0144
    ChrTalk(
        0xA,
        (
            "まさか、ミンネスさんが\x01",
            "詐欺師だったとはね……\x01",
            "まったく気づかなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "さしずめ、人を騙す\x01",
            "プロとでもいうべきか。\x01",
            "恐ろしい男だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "指名手配されるらしいし、\x01",
            "早いところ、逮捕されれば\x01",
            "いいんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38E7")

    label("loc_3860")


    #C0147
    ChrTalk(
        0xA,
        (
            "ともあれ、デリック君が\x01",
            "村長と和解できたのは良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "そういう意味では、\x01",
            "この事件はいいきっかけに\x01",
            "なったのかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E7")

    Jump("loc_3F15")

    label("loc_38EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3971")

    #C0149
    ChrTalk(
        0xA,
        (
            "ふう、デリック君は\x01",
            "いつになったら\x01",
            "家に戻る気なのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "早いところ村長と\x01",
            "仲直りしてほしいんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A09")

    label("loc_3971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3980")
    Jump("loc_3A09")

    label("loc_3980")


    #C0151
    ChrTalk(
        0xA,
        (
            "僕はミンネスさんとは、\x01",
            "あまり接したことはないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "なにやら最近デリック君と\x01",
            "よく会ってるようだが……\x01",
            "どんな話をしてるのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADF")

    #C0153
    ChrTalk(
        0x101,
        (
            "#00003F（そういえば、\x01",
            "  ここでグルメガイドの取材が\x01",
            "  出来そうだけど……）\x02\x03",

            "#00001F（今はそれどころじゃない。\x01",
            "  後で忘れずに来るとしよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADF")

    Jump("loc_3F15")

    label("loc_3AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3F")
    SetChrSubChip(0x12, 0x1)
    TurnDirection(0xA, 0x12, 0)

    #C0154
    ChrTalk(
        0xA,
        (
            "デリック君……\x01",
            "村長だって、頭ごなしに\x01",
            "君を否定しているわけじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x12,
        (
            "いや、親父はきっと……\x01",
            "俺の考えそのものが\x01",
            "気に入らないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "そうでなければ、\x01",
            "現在の村の状況を\x01",
            "黙ってみているわけがない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        (
            "……色々と難しいのは分かる。\x01",
            "でも時にはコーヒーでも飲んで、\x01",
            "落ち着くのも大事だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    TurnDirection(0xA, 0x0, 0)
    SetChrSubChip(0x12, 0x0)
    Jump("loc_3CE1")

    label("loc_3C3F")


    #C0158
    ChrTalk(
        0xA,
        (
            "デリック君も、\x01",
            "村長に似て責任感が強いからね。\x01",
            "色々と思い悩む事も多いみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "せっかく来てくれたんだし、\x01",
            "ブレンドの一杯でも\x01",
            "サービスしてあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE1")

    Jump("loc_3F15")

    label("loc_3CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE8")

    #C0160
    ChrTalk(
        0xA,
        (
            "各国の首脳が\x01",
            "クロスベルに集まる……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "これはクロスベルの歴史にも\x01",
            "類を見ない、大変な事だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "提唱したのはクロスベル市の\x01",
            "新市長さんということだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "いや、さすが\x01",
            "ＩＢＣのトップなだけあって、\x01",
            "大胆な発想をするよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E60")

    label("loc_3DE8")


    #C0164
    ChrTalk(
        0xA,
        (
            "西ゼムリア通商会議……\x01",
            "いよいよ始まったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "周辺諸国の関心も高いようだし、\x01",
            "僕も動向が気になるところだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E60")

    Jump("loc_3F15")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7D")
    Jump("loc_3F15")

    label("loc_3E7D")


    #C0166
    ChrTalk(
        0xA,
        (
            "赤毛の大男たちは、\x01",
            "村では特に怪しいことを\x01",
            "してなかったみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "腕が立ちそうな人が\x01",
            "揃っていたみたいだけど……\x01",
            "どういう人たちなんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F15")

    Jump("loc_2D33")

    label("loc_3F1A")

    TalkEnd(0xA)
    Return()

    # Function_12_2C6A end

    def Function_13_3F1E(): pass

    label("Function_13_3F1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFC")

    #C0168
    ChrTalk(
        0xB,
        (
            "あたし、キース君のことは\x01",
            "気にも留めてなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "ふふ、あれでなかなか\x01",
            "男気があるじゃない。\x01",
            "なんだか見直しちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "さっきはつい笑っちゃったけど、\x01",
            "後で謝っとかないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4081")

    label("loc_3FFC")


    #C0171
    ChrTalk(
        0xB,
        (
            "キースくんもなかなか\x01",
            "男気があるじゃない。\x01",
            "なんだか見直しちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        (
            "さっきはつい笑っちゃったけど、\x01",
            "後で謝っとかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4081")

    Jump("loc_4C64")

    label("loc_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_41F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415D")

    #C0173
    ChrTalk(
        0xB,
        (
            "ソフィアさん、とっても\x01",
            "料理が上手なのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "滞在しているうちに、\x01",
            "私もお料理を習っとこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "ふふ、お父さんより美味しく\x01",
            "オムライスを作れるように\x01",
            "なっちゃったりしてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41F0")

    label("loc_415D")


    #C0176
    ChrTalk(
        0xB,
        (
            "ソフィアさんが滞在しているうちに、\x01",
            "お料理を習っとこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "ふふ、お父さんより美味しく\x01",
            "オムライスを作れるように\x01",
            "なっちゃったりしてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F0")

    Jump("loc_4C64")

    label("loc_41F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BC")

    #C0178
    ChrTalk(
        0xB,
        (
            "あ～、コリンくんは\x01",
            "ホントに可愛いなあ～㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "お目目なんかクリっとして、\x01",
            "とっても人懐っこくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "さすが私の憧れてる\x01",
            "ハロルドさんの子供だわ。\x01",
            "将来が楽しみね！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_432F")

    label("loc_42BC")


    #C0181
    ChrTalk(
        0xB,
        (
            "あ～、コリンくんは\x01",
            "ホントに可愛いなあ～㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "さすが私の憧れてる\x01",
            "ハロルドさんの子供だわ。\x01",
            "将来が楽しみね！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432F")

    Jump("loc_4C64")

    label("loc_4334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4409")

    #C0183
    ChrTalk(
        0xB,
        (
            "クロスベル市へは\x01",
            "記念祭のとき行ったけど……\x01",
            "とっても綺麗で素敵な街よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xB,
        (
            "そんな場所を襲撃するなんて、\x01",
            "武装集団、許すまじね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "警察や警備隊には、\x01",
            "なんとか捕まえてほしいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_448C")

    label("loc_4409")


    #C0186
    ChrTalk(
        0xB,
        (
            "クロスベル市を襲撃するなんて、\x01",
            "武装集団許すまじね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        (
            "この間のミンネスといい、\x01",
            "悪い人ってどうして\x01",
            "こんなにいるのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448C")

    Jump("loc_4C64")

    label("loc_4491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_452F")

    #C0188
    ChrTalk(
        0xB,
        (
            "はー、雨の日は\x01",
            "湿っぽくてキライなのよねー。\x01",
            "床のお掃除も大変だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xB,
        (
            "せめてお客さんには\x01",
            "店先でドロをおとしてから\x01",
            "入ってきてほしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C64")

    label("loc_452F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_470A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C1")

    #C0190
    ChrTalk(
        0xB,
        (
            "今日は、ミンネスさんが\x01",
            "デリックさんに大事な話を\x01",
            "しに来るらしいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "いよいよ計画も\x01",
            "大詰めってところかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4705")

    label("loc_45C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4682")

    #C0192
    ChrTalk(
        0xB,
        (
            "あのミンネスってヤツ……\x01",
            "とんでもない食わせ物だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "フフン、あたしは最初っから\x01",
            "怪しいと思ってたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "今度現れたら、このあたしが\x01",
            "とっちめてやるんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4705")

    label("loc_4682")


    #C0195
    ChrTalk(
        0xB,
        (
            "あのミンネスってヤツ……\x01",
            "あたしは最初っから\x01",
            "怪しいと思ってたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "今度現れたら、このあたしが\x01",
            "とっちめてやるんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4705")

    Jump("loc_4C64")

    label("loc_470A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E1")

    #C0197
    ChrTalk(
        0xB,
        (
            "最近、とっても優しそうな\x01",
            "おじさんがよく来るのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "外国の有名な会社に\x01",
            "勤めてるって聞いたけど、\x01",
            "そのことを全然偉ぶらないしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "うーん、世の中には\x01",
            "できた人っているものよねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_486E")

    label("loc_47E1")


    #C0200
    ChrTalk(
        0xB,
        (
            "最近、とっても優しそうな\x01",
            "おじさんがよく来るのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "外国の有名な会社に勤めてるのに\x01",
            "全然偉ぶらないし……\x01",
            "できた人っているものよねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486E")

    Jump("loc_4C64")

    label("loc_4873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488E")
    Call(0, 14)
    Jump("loc_491D")

    label("loc_488E")


    #C0202
    ChrTalk(
        0xB,
        (
            "オルキスタワーってのは\x01",
            "見てみたいけど、お店があるしねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "うちのオムライスを\x01",
            "１時間で１０皿完食できたら、\x01",
            "デートしたげてもいいけど☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491D")

    Jump("loc_4C64")

    label("loc_4922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B1C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A15")

    #C0204
    ChrTalk(
        0xB,
        (
            "遊撃士の人たちってのは\x01",
            "ホント強いわよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "アリオスさんばかりが\x01",
            "注目されがちだけど、\x01",
            "あの女性遊撃士さんたちも相当だわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        (
            "ふふっ、もちろんあなたたちもね。\x01",
            "おかげで楽しい時間を過ごせたわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AB0")

    label("loc_4A15")


    #C0207
    ChrTalk(
        0xB,
        (
            "アリオスさんばかりが\x01",
            "注目されがちだけど、\x01",
            "あの女性遊撃士さんたちも相当だわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "ふふっ、もちろんあなたたちもね。\x01",
            "おかげで楽しい時間を過ごせたわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB0")

    Jump("loc_4B17")

    label("loc_4AB5")


    #C0209
    ChrTalk(
        0xB,
        (
            "遊撃士さんたちが、\x01",
            "魔獣退治に来てくれてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "ふふ、うんとサービスして\x01",
            "あげなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B17")

    Jump("loc_4C64")

    label("loc_4B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE7")

    #C0211
    ChrTalk(
        0xB,
        (
            "いらっしゃ～い。\x01",
            "お好きな席にどうぞ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "うちのオススメ料理は、\x01",
            "なんといってもオムライスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "最近改良を加えて\x01",
            "更に美味しくなったから、\x01",
            "よかったら召し上がってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C64")

    label("loc_4BE7")


    #C0214
    ChrTalk(
        0xB,
        (
            "今日はハロルドさんが\x01",
            "２階で部屋をとってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        (
            "商談も終わったみたいだし、\x01",
            "コーヒーでも持っていって\x01",
            "あげようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C64")

    TalkEnd(0xFE)
    Return()

    # Function_13_3F1E end

    def Function_14_4C68(): pass

    label("Function_14_4C68")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0216
    ChrTalk(
        0xC,
        (
            "シーリィちゃん、\x01",
            "今度俺と一緒に街に行かない？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xC,
        (
            "噂のオルキスタワーとやらを\x01",
            "見に行ってみようぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "うーん、\x01",
            "でも店の手伝いもあるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "……そうだ☆\x01",
            "うちのオムライスを１時間で１０皿\x01",
            "完食できたら、行ってもいいわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "い、いやいや……\x01",
            "そりゃさすがにムリだよ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_4C68 end

    def Function_15_4D9A(): pass

    label("Function_15_4D9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E75")

    #C0221
    ChrTalk(
        0xC,
        (
            "正直言って、俺なんかには\x01",
            "訳の分かんない状況だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        (
            "絶対、何が起こっても\x01",
            "俺がシーリィちゃんを守ってやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xC,
        (
            "……面と向かって本人に言ったら\x01",
            "笑われちゃったけどね……とほほ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EE2")

    label("loc_4E75")


    #C0224
    ChrTalk(
        0xC,
        (
            "シーリィちゃんには\x01",
            "笑われちゃったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "絶対、何が起こっても\x01",
            "俺がシーリィちゃんを\x01",
            "守ってやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE2")

    Jump("loc_5A74")

    label("loc_4EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_504A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC1")

    #C0226
    ChrTalk(
        0xC,
        (
            "ここだけの話、シーリィちゃんの\x01",
            "料理の腕って……アレなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "前に消し炭みたいな\x01",
            "オムライスを出されたときは、\x01",
            "さすがの俺もビビっちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        "……まあ、無理やり完食したけど！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5045")

    label("loc_4FC1")


    #C0229
    ChrTalk(
        0xC,
        (
            "ここだけの話、シーリィちゃんの\x01",
            "料理の腕って……アレなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        (
            "……まあ、何が出てこようと\x01",
            "無理やり完食するだけだけどな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5045")

    Jump("loc_5A74")

    label("loc_504A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5123")

    #C0231
    ChrTalk(
        0xC,
        (
            "国防軍の連中、\x01",
            "いけ好かないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "村には立ち寄るくらいの癖に、\x01",
            "『守ってやってる』みたいな\x01",
            "雰囲気をだしやがんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        (
            "警備隊から国防軍になって、\x01",
            "舞い上がってるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_518B")

    label("loc_5123")


    #C0234
    ChrTalk(
        0xC,
        (
            "国防軍の連中には\x01",
            "なんだか腹が立つな。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        (
            "警備隊から国防軍になって、\x01",
            "舞い上がってるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518B")

    Jump("loc_5A74")

    label("loc_5190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5286")

    #C0236
    ChrTalk(
        0xC,
        (
            "こないだの襲撃事件の主犯、\x01",
            "まだクロスベルに潜伏してる\x01",
            "可能性が高いんだってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        (
            "最近、警備隊の見回りが増えたのも\x01",
            "そういうことなんだろうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "なんだかクロスベルも、\x01",
            "物騒な場所になっちまった\x01",
            "もんだよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5311")

    label("loc_5286")


    #C0239
    ChrTalk(
        0xC,
        (
            "こないだの襲撃事件の主犯、\x01",
            "まだクロスベルに潜伏してる\x01",
            "可能性が高いんだってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        (
            "なんだかクロスベルも、\x01",
            "物騒な場所になったよな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5311")

    Jump("loc_5A74")

    label("loc_5316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E8")

    #C0241
    ChrTalk(
        0xC,
        (
            "あー、そういや\x01",
            "例の住民投票ってヤツが\x01",
            "近づいてるんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        (
            "街まで投票に行くのは\x01",
            "ちょっと面倒だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "俺たち村人にも\x01",
            "関係あることだし、\x01",
            "ちゃんと行った方がいいよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5464")

    label("loc_53E8")


    #C0244
    ChrTalk(
        0xC,
        (
            "独立の是非を問うっていう\x01",
            "住民投票が近づいてるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "街まで投票に行くのは面倒だけど……\x01",
            "ちゃんと行った方がいいよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5464")

    Jump("loc_5A74")

    label("loc_5469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5667")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5558")

    #C0246
    ChrTalk(
        0xC,
        (
            "今日で、ミンネスさんと\x01",
            "デリックの商談が終わるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "アルモリカ村の生まれ変わりを祝って、\x01",
            "パーッと打ち上げでもやりたいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "へへ、シーリィちゃんも派手好きだし、\x01",
            "きっと喜んでくれるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55E7")

    label("loc_5558")


    #C0249
    ChrTalk(
        0xC,
        (
            "今日で、ミンネスさんと\x01",
            "デリックの商談が終わるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        (
            "パーッと打ち上げでもやって、\x01",
            "アルモリカ村の新たな門出を\x01",
            "みんなで祝わないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E7")

    Jump("loc_5662")

    label("loc_55EC")


    #C0251
    ChrTalk(
        0xC,
        (
            "ミンネスさんの話って……\x01",
            "もしかして、全部ウソだったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "あー、デリックの奴も\x01",
            "相当ヘコんでるだろうなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5662")

    Jump("loc_5A74")

    label("loc_5667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_579C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5725")

    #C0253
    ChrTalk(
        0xC,
        (
            "あの外国人のオッサンは、\x01",
            "人生経験が豊富みたいでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xC,
        (
            "俺がシーリィちゃんに\x01",
            "憧れているのを見抜いて、\x01",
            "色々と励ましてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        "ああ、いい人だよな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5797")

    label("loc_5725")


    #C0256
    ChrTalk(
        0xC,
        (
            "あの外国人のオッサン、\x01",
            "シーリィちゃんに憧れている俺を\x01",
            "色々と励ましてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        "ああ、いい人だよな……\x02",
    )

    CloseMessageWindow()

    label("loc_5797")

    Jump("loc_5A74")

    label("loc_579C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_580D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B7")
    Call(0, 14)
    Jump("loc_5808")

    label("loc_57B7")


    #C0258
    ChrTalk(
        0xC,
        (
            "とほほ……\x01",
            "せっかく勇気だして誘ったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xC,
        "シーリィちゃんは手厳しいぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_5808")

    Jump("loc_5A74")

    label("loc_580D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58E0")

    #C0260
    ChrTalk(
        0xC,
        (
            "実は、近いうちに\x01",
            "シーリィちゃんをデートに\x01",
            "誘おうと思っていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "今まで毎日と言っていいほど\x01",
            "店に通ってきて、彼女とも\x01",
            "随分親しくなった……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        "きっとＯＫしてくれるはずさ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5950")

    label("loc_58E0")


    #C0263
    ChrTalk(
        0xC,
        (
            "近いうちにシーリィちゃんを\x01",
            "デートに誘うつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "よし、今日は心の準備をして……\x01",
            "決行は明日だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5950")

    Jump("loc_5A74")

    label("loc_5955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EF")

    #C0265
    ChrTalk(
        0xC,
        (
            "この店の看板娘、\x01",
            "シーリィちゃんは俺の憧れなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "なんと言っても、\x01",
            "あの笑顔がたまんないね！\x01",
            "ついつい居座っちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A74")

    label("loc_59EF")


    #C0267
    ChrTalk(
        0xC,
        (
            "シーリィちゃんの笑顔の為なら、\x01",
            "何度コーヒーをおかわりしてでも\x01",
            "居座ってたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "……ま、おかわりは\x01",
            "タダじゃないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A74")

    TalkEnd(0xFE)
    Return()

    # Function_15_4D9A end

    def Function_16_5A78(): pass

    label("Function_16_5A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8F")
    Call(0, 44)
    Return()

    label("loc_5A8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9C")

    #C0269
    ChrTalk(
        0xD,
        (
            "《幻獣》がまだいるし、\x01",
            "得体の知れない大樹の出現で\x01",
            "街道の移動は制限されたままだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "街に戻ったハロルド君が、\x01",
            "なにか私が気に入りそうな本を\x01",
            "持ってきてくれるそうでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        (
            "ああ、流石はハロルド君だ。\x01",
            "彼の帰りが楽しみでならないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C3C")

    label("loc_5B9C")


    #C0272
    ChrTalk(
        0xD,
        (
            "聡明なハロルド君のことだ、\x01",
            "きっと私好みの本を\x01",
            "持ってきてくれるに違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xD,
        (
            "……とはいえこんな状況だ。\x01",
            "街道の移動にも十分に\x01",
            "気をつけて欲しいものだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C3C")

    Jump("loc_6C79")

    label("loc_5C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D29")

    #C0274
    ChrTalk(
        0xD,
        (
            "街道の移動制限のせいで、\x01",
            "図書館に自由に行けなくて\x01",
            "参っていたのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "マクダエル議長が\x01",
            "ついにやってくれたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "このまま状況が好転して、\x01",
            "街を包む結界なんかも\x01",
            "消えてなくなってくれないものか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5DBC")

    label("loc_5D29")


    #C0277
    ChrTalk(
        0xD,
        (
            "このまま街を包む結界なんかも\x01",
            "消えてなくなってくれないものか。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xD,
        (
            "何もかも元通りになって、\x01",
            "自由に図書館に行く事が\x01",
            "出来るようになればいいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DBC")

    Jump("loc_6C79")

    label("loc_5DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EB8")

    #C0279
    ChrTalk(
        0xD,
        (
            "《幻獣》や街道の移動制限で\x01",
            "農業もままならないし、気分転換に\x01",
            "新しい本でも読みたいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xD,
        (
            "クロスベル市にある図書館にも\x01",
            "当然行く事ができなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xD,
        (
            "読書は生活の潤いだというのに、\x01",
            "あんまりだとは思わないか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F4D")

    label("loc_5EB8")


    #C0282
    ChrTalk(
        0xD,
        (
            "クロスベル市にある図書館に\x01",
            "行く事ができなくてね……\x01",
            "新しい本が読めないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xD,
        (
            "こんな生活、何年も続くとしたら\x01",
            "地獄としか言いようがないな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4D")

    Jump("loc_6C79")

    label("loc_5F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_60C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604C")

    #C0284
    ChrTalk(
        0xD,
        (
            "少し前に出た\x01",
            "クロスベルタイムズの特別号、\x01",
            "何度も読み返してしまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xD,
        (
            "襲撃の事も気になるが、\x01",
            "イリアが重傷を負った記事が\x01",
            "何よりもショッキングでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "……クロスベルの住民として、\x01",
            "彼女の回復をただ祈るばかりだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60BE")

    label("loc_604C")


    #C0287
    ChrTalk(
        0xD,
        (
            "常にクロスベルに\x01",
            "活気を与え続けてくれたイリアが、\x01",
            "こんな目にあうとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        "……回復をただ祈るばかりだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_60BE")

    Jump("loc_6C79")

    label("loc_60C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_618E")

    #C0289
    ChrTalk(
        0xD,
        (
            "窓を叩く心地よい雨の音、\x01",
            "傍らには暖かいコーヒー……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xD,
        (
            "雨の日は私にとって、\x01",
            "最高の読書日和といえるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "せっかくだから\x01",
            "溜まっていた本を一気に\x01",
            "読み進めるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_61FC")

    label("loc_618E")


    #C0292
    ChrTalk(
        0xD,
        (
            "窓を叩く心地よい雨の音、\x01",
            "傍らには暖かいコーヒー……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "雨の日は私にとって、\x01",
            "最高の読書日和といえるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61FC")

    Jump("loc_6C79")

    label("loc_6201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_650D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6359")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D9")

    #C0294
    ChrTalk(
        0xD,
        (
            "時代が移り変わり、\x01",
            "この村が抱える問題は\x01",
            "より増えてきたように思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        (
            "村長は伝統を捨てるべきでは\x01",
            "ないというけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xD,
        (
            "デリック君が改革を望むのも\x01",
            "分かる気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6354")

    label("loc_62D9")


    #C0297
    ChrTalk(
        0xD,
        (
            "時代が移り変わり、\x01",
            "この村が抱える問題は\x01",
            "より増えてきたように思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xD,
        (
            "デリック君が改革を望むのも\x01",
            "分かる気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6354")

    Jump("loc_6508")

    label("loc_6359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6458")

    #C0299
    ChrTalk(
        0xD,
        (
            "あのミンネスという男は、\x01",
            "村人を上手く懐柔していたようでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "他人が何を欲しているか……\x01",
            "それを見極める洞察力は、\x01",
            "間違いなく本物だったろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xD,
        (
            "せっかくの才能を、詐欺などに\x01",
            "利用してしまったというのは\x01",
            "救いようがない話だがね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6508")

    label("loc_6458")


    #C0302
    ChrTalk(
        0xD,
        (
            "あのミンネスという男……\x01",
            "詐欺になど手を染めなければ、\x01",
            "大成していたかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        (
            "……まあ、話を聞く限りでは\x01",
            "前科もかなりありそうだし、\x01",
            "同情する余地もないんだがね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6508")

    Jump("loc_6C79")

    label("loc_650D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_66FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6672")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    #C0304
    ChrTalk(
        0xD,
        (
            "《本当にあったクロスベルの怪》\x01",
            "という本を図書館から借りてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xD,
        (
            "この“自分の頭を探す男”の話……\x01",
            "ううむ、背筋が凍るな。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        "ああ、確かに恐ろしいな……\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xA,
        (
            "自分の頭がないはずなのに、\x01",
            "どこから『探してくれ』だなんて\x01",
            "呻き声を上げたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xD,
        (
            "……そこはあまり\x01",
            "怖い部分じゃないんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_66F5")

    label("loc_6672")


    #C0309
    ChrTalk(
        0xD,
        (
            "ふう、せっかく\x01",
            "恐怖に浸っていたのに\x01",
            "ゴーファンのせいで台無しだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "こいつには怪談の楽しみ方を\x01",
            "ちゃんと教えてやらないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F5")

    Jump("loc_6C79")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_685A")

    #C0311
    ChrTalk(
        0xD,
        (
            "図書館に行ったついでに、\x01",
            "最近楽しんで読んでいる\x01",
            "続き物の小説を買ってきたのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xD,
        (
            "どうやら、巻数を飛ばして\x01",
            "買ってしまったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "うっかり読んでしまって\x01",
            "ネタバレになってしまうのは避けたい……\x01",
            "悪いが、もらってくれないかな。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0314
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F2, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 4)
    TalkEnd(0xFE)
    SetChrFlags(0xD, 0x10)
    Return()

    label("loc_685A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D8")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    #C0315
    ChrTalk(
        0xD,
        (
            "今日、図書館で借りた\x01",
            "《大陸を動かした美人たち》……\x01",
            "なかなか興味深いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xA,
        (
            "《戦乙女リアンヌ》を筆頭に、\x01",
            "各国の歴史的偉業を成した女性を\x01",
            "紹介している本だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xA,
        (
            "うーん、やはり女性というのは\x01",
            "元来、強い存在なのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xA,
        (
            "僕も娘には\x01",
            "尻にしかれっぱなしだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xD,
        (
            "（それはお前が\x01",
            "  頼りないだけだと思うが……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_6A3E")

    label("loc_69D8")


    #C0320
    ChrTalk(
        0xD,
        (
            "《大陸を動かした美人たち》……\x01",
            "なかなか興味深いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xD,
        (
            "君たちも図書館で\x01",
            "読んでみてはどうかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A3E")

    Jump("loc_6C79")

    label("loc_6A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4C")

    #C0322
    ChrTalk(
        0xD,
        (
            "私は読書が好きでね。\x01",
            "今朝は街の図書館へ\x01",
            "行くつもりだったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xD,
        (
            "大統領のクロスベル入りで\x01",
            "街道が交通規制になるのを、\x01",
            "すっかり忘れてしまっていたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xD,
        (
            "おかげさまで無意義に\x01",
            "午前中を過ごしてしまった。\x01",
            "やれやれ、やるせないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BC7")

    label("loc_6B4C")


    #C0325
    ChrTalk(
        0xD,
        (
            "今は街道の交通規制も\x01",
            "解除されているようだし……\x01",
            "また後で街に行くかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xD,
        (
            "図書館に行って、\x01",
            "何か本を探してこないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BC7")

    Jump("loc_6C79")

    label("loc_6BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE4")
    Jump("loc_6C79")

    label("loc_6BE4")


    #C0327
    ChrTalk(
        0xD,
        (
            "彼ら、レオールさんの雑貨店で\x01",
            "保存がきく食料を\x01",
            "買いこんでいったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xD,
        (
            "うーむ、登山にでもいくのかな。\x01",
            "そんな集まりには見えなかったが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C79")

    TalkEnd(0xFE)
    Return()

    # Function_16_5A78 end

    def Function_17_6C7D(): pass

    label("Function_17_6C7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D20")

    #C0329
    ChrTalk(
        0xE,
        (
            "ハロルドさん一家は、\x01",
            "街の方に帰ってしまったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xE,
        (
            "折角仲良くなれたから\x01",
            "ちょっと寂しいけど……\x01",
            "こんな状況だし仕方ないわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6DBF")

    label("loc_6D20")


    #C0331
    ChrTalk(
        0xE,
        (
            "ハロルドさん一家は、\x01",
            "ご近所のことを心配してらしたし、\x01",
            "街に戻ったほうがいいわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xE,
        (
            "私とステファンも里帰りする時には、\x01",
            "是非とも挨拶にいかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DBF")

    Jump("loc_76B9")

    label("loc_6DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6DD2")
    Jump("loc_76B9")

    label("loc_6DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EBF")

    #C0333
    ChrTalk(
        0xE,
        (
            "こんなことになってしまって、\x01",
            "クロスベル市の方にいる\x01",
            "昔のご近所さんが心配だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xE,
        (
            "ハロルドさんたちは、\x01",
            "街を心配しながらもちゃんと\x01",
            "やるべきことをやってるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xE,
        "私も何か、出来ることをしないと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6F50")

    label("loc_6EBF")


    #C0336
    ChrTalk(
        0xE,
        (
            "ハロルドさんたちは、\x01",
            "街を心配しながらもちゃんと\x01",
            "やるべきことをやってるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xE,
        (
            "私も心配するばかりじゃなくて、\x01",
            "出来ることをしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F50")

    Jump("loc_76B9")

    label("loc_6F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7025")

    #C0338
    ChrTalk(
        0xE,
        (
            "はあ……\x01",
            "街が襲撃を受けるなんて\x01",
            "思いも寄らなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xE,
        (
            "幸い、知り合いは\x01",
            "無事だったみたいだけど……\x01",
            "犠牲者も多かったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xE,
        (
            "もうこんな事が\x01",
            "起こらないといいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7090")

    label("loc_7025")


    #C0341
    ChrTalk(
        0xE,
        (
            "はあ……\x01",
            "街が襲撃を受けるなんて\x01",
            "思いも寄らなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xE,
        (
            "もうこんな事が\x01",
            "起こらないといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7090")

    Jump("loc_76B9")

    label("loc_7095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7180")

    #C0343
    ChrTalk(
        0xE,
        (
            "村に引っ越してくるまで、\x01",
            "日曜学校の出張なんてものの\x01",
            "存在すら知らなかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        (
            "村から大聖堂に通わせるのは\x01",
            "大変だと思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xE,
        (
            "遠い所から来ていただいてる\x01",
            "シスターさんには感謝しないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_71F0")

    label("loc_7180")


    #C0346
    ChrTalk(
        0xE,
        (
            "ここから大聖堂に\x01",
            "通わせるのは大変だもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xE,
        (
            "遠い所から来ていただいてる\x01",
            "シスターさんには感謝しないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71F0")

    Jump("loc_76B9")

    label("loc_71F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_731B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7298")

    #C0348
    ChrTalk(
        0xE,
        (
            "村長の息子さん……\x01",
            "昨日帰ってきてからすごく\x01",
            "ピリピリしてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xE,
        (
            "今日の商談に村の今後が\x01",
            "かかっているんだもの……\x01",
            "当然よね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7316")

    label("loc_7298")


    #C0350
    ChrTalk(
        0xE,
        (
            "ステファンや村の子供たちが\x01",
            "魔獣に襲われなくてよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        (
            "まったく、あの詐欺師ときたら……\x01",
            "絶対に許さないんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7316")

    Jump("loc_76B9")

    label("loc_731B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D3")

    #C0352
    ChrTalk(
        0xE,
        (
            "ふんふふ～ん……\x01",
            "シーツはこれでよし、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "私、ステファンを産む前は\x01",
            "ホテルのメイドに憧れてたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xE,
        (
            "ふふ、宿酒場の手伝いも\x01",
            "なかなか楽しいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_744C")

    label("loc_73D3")


    #C0355
    ChrTalk(
        0xE,
        (
            "ふふ、宿酒場の手伝いも\x01",
            "なかなか楽しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "ステファンも友達と\x01",
            "仲良くやってるみたいだし、\x01",
            "毎日が充実してるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_744C")

    Jump("loc_76B9")

    label("loc_7451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_74D6")

    #C0357
    ChrTalk(
        0xE,
        (
            "今日はお店の手伝いで\x01",
            "掃除をしているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xE,
        (
            "私もステファンも\x01",
            "お世話になってるし、\x01",
            "少しでもお役に立たなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76B9")

    label("loc_74D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_757D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74F1")
    Call(0, 23)
    Jump("loc_7578")

    label("loc_74F1")


    #C0359
    ChrTalk(
        0xE,
        (
            "まあ、いいのかしら？\x01",
            "ありがたくいただくわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xE,
        (
            "ふふ、ステファンが前に\x01",
            "ご馳走になったって聞いて、\x01",
            "私も食べてみたかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7578")

    Jump("loc_76B9")

    label("loc_757D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_76B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7632")

    #C0361
    ChrTalk(
        0xE,
        (
            "私と息子のステファンは、\x01",
            "少し前にクロスベルから\x01",
            "移住してきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xE,
        (
            "最初はあの子も嫌がってたけど、\x01",
            "村にも大分慣れてきたみたい。\x01",
            "ふふ、よかったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_76B9")

    label("loc_7632")


    #C0363
    ChrTalk(
        0xE,
        (
            "ちなみにこのお部屋は、\x01",
            "ゴーファンさんのご好意で\x01",
            "格安で間借りさせてもらったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xE,
        (
            "ふふ、この村の人たちは\x01",
            "暖かくて優しいのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76B9")

    TalkEnd(0xFE)
    Return()

    # Function_17_6C7D end

    def Function_18_76BD(): pass

    label("Function_18_76BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7745")

    #C0365
    ChrTalk(
        0xF,
        (
            "日曜学校の日は、\x01",
            "休み時間に宿屋のおっちゃんが\x01",
            "おやつを持ってきてくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xF,
        "あ～、早く休み時間にならないかな～。\x02",
    )

    CloseMessageWindow()

    label("loc_7745")

    TalkEnd(0xFE)
    Return()

    # Function_18_76BD end

    def Function_19_7749(): pass

    label("Function_19_7749")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_77BB")

    #C0367
    ChrTalk(
        0x10,
        (
            "プーリーね、\x01",
            "今日はおにいちゃんたちと\x01",
            "おべんきょうなんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x10,
        "ひとつもわかんないけどねー。\x02",
    )

    CloseMessageWindow()

    label("loc_77BB")

    TalkEnd(0xFE)
    Return()

    # Function_19_7749 end

    def Function_20_77BF(): pass

    label("Function_20_77BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_792A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_789C")

    #C0369
    ChrTalk(
        0x11,
        (
            "お母さんと一緒に\x01",
            "街の様子を見に行ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x11,
        (
            "前に住んでた辺りの\x01",
            "友達やご近所さんは。\x01",
            "みんな無事だったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x11,
        (
            "お母さん、ずっと心配してた\x01",
            "みたいだから……\x01",
            "ほんと、よかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7925")

    label("loc_789C")


    #C0372
    ChrTalk(
        0x11,
        (
            "昨日まで、お母さんと一緒に\x01",
            "街の様子を見に行ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x11,
        (
            "前の友達やご近所さんは、\x01",
            "みんな無事だったみたい。\x01",
            "ほんと、よかったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7925")

    Jump("loc_7A32")

    label("loc_792A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D4")

    #C0374
    ChrTalk(
        0x11,
        (
            "街にいた頃は大聖堂まで\x01",
            "通っていたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x11,
        (
            "村に住んでると\x01",
            "シスターのほうから\x01",
            "来てくれるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x11,
        "……ちょっとラクちんかも。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7A32")

    label("loc_79D4")


    #C0377
    ChrTalk(
        0x11,
        (
            "街にいた頃は、\x01",
            "日曜学校へは大聖堂まで\x01",
            "通ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x11,
        "……今はちょっとラクちんかも。\x02",
    )

    CloseMessageWindow()

    label("loc_7A32")

    TalkEnd(0xFE)
    Return()

    # Function_20_77BF end

    def Function_21_7A36(): pass

    label("Function_21_7A36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7A8E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A89")

    #C0379
    ChrTalk(
        0x12,
        (
            "……今日は、\x01",
            "大事な来客があるんだ。\x01",
            "出て行ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A89")

    Jump("loc_7F26")

    label("loc_7A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7D82")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CE1")

    #C0380
    ChrTalk(
        0x12,
        "……あんたたちか。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#00003Fデリックさん……\x01",
            "あの、できればもう一度\x01",
            "村長と話をしてみては……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x12,
        (
            "……フン。\x01",
            "話など今まで何度もした。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x12,
        (
            "だが、村長は保守に拘るばかりで、\x01",
            "俺の改革案は何一つ\x01",
            "認めようとはしなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x12,
        (
            "そんな中、ミンネスさんは\x01",
            "村の改革を諦めかけていた俺に\x01",
            "チャンスを与えてくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x12,
        (
            "もう親父には頼らん……\x01",
            "俺たち２人で、アルモリカ村を\x01",
            "立派に改革してやるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#00003F（……ミンネスには怪しい点がある。\x01",
            "  できれば考えなおしてほしいけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#00108F（今の時点では証拠が足りないわ。\x01",
            "  説得は難しいでしょうね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7D7D")

    label("loc_7CE1")


    #C0388
    ChrTalk(
        0x12,
        (
            "ミンネスさんは\x01",
            "村の改革を諦めかけていた俺に\x01",
            "チャンスを与えてくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x12,
        (
            "もう親父には頼らん……\x01",
            "俺たち２人で、アルモリカ村を\x01",
            "立派に改革してやるんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D7D")

    Jump("loc_7F26")

    label("loc_7D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7F26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EAB")

    #C0390
    ChrTalk(
        0x12,
        (
            "親父……村長は、\x01",
            "どんな改革案を出しても\x01",
            "頑として認めようとしないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x12,
        (
            "二言めには『村のあるべき姿』だの\x01",
            "『本質を見失うな』だの……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x12,
        (
            "だが、そんな形のないものに\x01",
            "しがみついていても、村は\x01",
            "静かに滅んでいくだけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x12,
        (
            "……ふう、俺はなんだか\x01",
            "疲れてしまったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7F26")

    label("loc_7EAB")


    #C0394
    ChrTalk(
        0x12,
        (
            "村長が認めない以上、\x01",
            "村の改革は行われないだろう。\x01",
            "後は滅びるのを待つのみ……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x12,
        (
            "……俺はなんだか\x01",
            "疲れてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F26")

    TalkEnd(0xFE)
    Return()

    # Function_21_7A36 end

    def Function_22_7F2A(): pass

    label("Function_22_7F2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F48")
    Call(0, 23)
    Jump("loc_7FC5")

    label("loc_7F48")


    #C0396
    ChrTalk(
        0x13,
        (
            "そうそう、今日は\x01",
            "お裾分けに来たんだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x13,
        (
            "ほら、あたしの得意な\x01",
            "自家製カルボナーラソースさ。\x01",
            "パスタに絡めてお食べ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC5")

    TalkEnd(0xFE)
    Return()

    # Function_22_7F2A end

    def Function_23_7FC9(): pass

    label("Function_23_7FC9")

    OP_4B(0xE, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0398
    ChrTalk(
        0x13,
        (
            "それじゃ、しばらくは\x01",
            "この部屋に滞在するのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xE,
        (
            "ええ、せっかくのご好意だから\x01",
            "甘えさせてもらおうと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "その代わり、少しは\x01",
            "お店を手伝わせてもらおうと\x01",
            "思っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x13,
        (
            "そりゃあいい。\x01",
            "今まで２人で切り盛りしてたし、\x01",
            "人手が増えたら喜んでくれるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0xE, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_23_7FC9 end

    def Function_24_80E7(): pass

    label("Function_24_80E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_818E")

    #C0402
    ChrTalk(
        0x14,
        (
            "今日、行きがけに気づいたのですが\x01",
            "村のところどころに\x01",
            "大きな猫のような足跡がありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x14,
        (
            "昨日、この村で\x01",
            "何かあったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8203")

    label("loc_818E")


    #C0404
    ChrTalk(
        0x14,
        (
            "村のところどころに\x01",
            "大きな猫のような足跡が\x01",
            "ついているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x14,
        (
            "昨日、この村で\x01",
            "何かあったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8203")

    TalkEnd(0xFE)
    Return()

    # Function_24_80E7 end

    def Function_25_8207(): pass

    label("Function_25_8207")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8218")
    Jump("loc_8F24")

    label("loc_8218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_863E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8590")

    #C0406
    ChrTalk(
        0x15,
        (
            "#03600Fああ、皆さん……！\x01",
            "ご無事で何よりです。\x02\x03",

            "#03603Fマクダエル議長によって\x01",
            "独立国の無効宣言がされたと\x01",
            "噂を聞きました。\x02\x03",

            "#03605Fもしかして、皆さんが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x103,
        "#00200Fええ、色々と大変でしたが……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#00000Fアルモリカ村では何か、\x01",
            "状況に変化はありましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x15,
        (
            "#03603Fいえ、今のところは……\x02\x03",

            "#03600Fただ、ちょうど国防軍と交渉中に\x01",
            "連絡を受けたもので、\x01",
            "彼らも随分慌てている様子でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#00103Fやっぱり村への影響は\x01",
            "微々たるものみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        (
            "#00306Fまあ、どちらかというと\x01",
            "市内への影響が大きいだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x15,
        (
            "#03603Fええ、ご近所の皆さんも心配ですし\x01",
            "マインツやウルスラ病院方面も\x01",
            "気になっているところです。\x02\x03",

            "#03608Fなんとか自由に動けるようになったら\x01",
            "各方面を訪ねたいところですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#00003F……とにかく、まだ状況が\x01",
            "完全に好転したとはいえません。\x02\x03",

            "#00000Fハロルドさんの方も\x01",
            "お気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x15,
        "#03600Fええ、皆さんもどうかお気をつけて。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 5)
    Jump("loc_8639")

    label("loc_8590")


    #C0415
    ChrTalk(
        0x15,
        (
            "#03603F市内のご近所も心配ですし\x01",
            "マインツやウルスラ病院方面も\x01",
            "気になっているところです。\x02\x03",

            "#03608Fなんとか自由に動けるようになったら\x01",
            "各方面を訪ねたいところですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8639")

    Jump("loc_8F24")

    label("loc_863E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_86F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8659")
    Call(0, 26)
    Jump("loc_86F4")

    label("loc_8659")


    #C0416
    ChrTalk(
        0x15,
        (
            "#03600F次の国防軍との交渉のために、\x01",
            "村の皆さんが必要としている物資を\x01",
            "まとめている所なんです。\x02\x03",

            "#03603F皆さん、どうかお気をつけて。\x01",
            "……女神の加護を。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86F4")

    Jump("loc_8F24")

    label("loc_86F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87EE")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0417
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆「詐欺事件２日目」を？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",            # 0
            "【クリアしている】\x01",        # 1
            "【クリアしていない】\x01",      # 2
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
        (0, "loc_87D5"),
        (1, "loc_87DA"),
        (2, "loc_87E4"),
        (SWITCH_DEFAULT, "loc_87EE"),
    )


    label("loc_87D5")

    Jump("loc_87EE")

    label("loc_87DA")

    OP_29(0x87, 0x4, 0x10)
    Jump("loc_87EE")

    label("loc_87E4")

    OP_29(0x87, 0x3, 0x10)
    Jump("loc_87EE")

    label("loc_87EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8910")

    #C0418
    ChrTalk(
        0x15,
        (
            "#03600Fアルモリカへは、村長から\x01",
            "招待を受けて来たんです。\x02\x03",

            "#03603F例の詐欺事件の件の礼にと\x01",
            "一緒に誘いを受けていたピート君は\x01",
            "遠慮したみたいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        (
            "#00005Fあのミンネスの事件で……\x01",
            "そうだったんですか。\x02\x03",

            "#00003Fピート君まで巻き込まれなくて\x01",
            "よかったというべきか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A08")

    label("loc_8910")


    #C0420
    ChrTalk(
        0x15,
        (
            "#03600Fアルモリカへは、村長から\x01",
            "招待を受けて来たんです。\x02\x03",

            "#03603Fある事件を手伝った礼にと\x01",
            "一緒に誘いを受けていたピート君は\x01",
            "遠慮したみたいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#00000Fそうだったんですか。\x02\x03",

            "#00003Fピート君まで巻き込まれなくて\x01",
            "よかったというべきか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A08")


    #C0422
    ChrTalk(
        0x15,
        "#03600Fええ、本当にそう思います。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8AB9")

    label("loc_8A37")


    #C0423
    ChrTalk(
        0x15,
        (
            "#03600F抵抗勢力は、古道の途中にある\x01",
            "アルモリカ古戦場のあたりで\x01",
            "目撃されているようです。\x02\x03",

            "#03603F皆さん、どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AB9")

    Jump("loc_8F24")

    label("loc_8ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D9D")

    #C0424
    ChrTalk(
        0x101,
        (
            "#00000Fあ……ハロルドさん。\x01",
            "今日はこちらに来ていたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x15,
        (
            "#03605Fおや、支援課の皆さん。\x01",
            "こんな所で会うとは奇遇ですね。\x02\x03",

            "#03600Fええ、今日は商談に\x01",
            "来ていたところでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、相変わらず\x01",
            "誠実な商売をされてらっしゃる\x01",
            "ようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x15,
        (
            "#03609Fはは、おかげさまで\x01",
            "今日はいい取引きを\x01",
            "させていただきました。\x02\x03",

            "#03600Fそうだ皆さん……\x01",
            "よければこれを受け取って\x01",
            "もらえますか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0428
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を１０個受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13C, 10)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0429
    ChrTalk(
        0x104,
        "#00305Fお、いいんスか？\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x15,
        (
            "#03600Fええ、実は取引きの際に\x01",
            "おまけしていただいたんです。\x02\x03",

            "#03609Fウチでは食べきれませんし、\x01",
            "よろしければ皆さんの\x01",
            "お役に立ててください。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#00002Fえっと、それじゃあ……\x01",
            "ありがたくいただきますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 6)
    Jump("loc_8F24")

    label("loc_8D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E91")

    #C0432
    ChrTalk(
        0x15,
        (
            "#03604Fおかげさまで\x01",
            "今日はいい取引きを\x01",
            "させていただきました。\x02\x03",

            "#03608Fただ最近、村長はデリックくんと\x01",
            "諍#2Rいさか#いが絶えないようで、\x01",
            "とても悩んでいるご様子でした。\x02\x03",

            "#03603F……親子というものは\x01",
            "やはり、難しいものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8F24")

    label("loc_8E91")


    #C0433
    ChrTalk(
        0x15,
        (
            "#03603F村長とデリックくん……\x01",
            "村を守りたいという気持ちは\x01",
            "互いにあるはずなのですが……\x02\x03",

            "#03608F……親子というものは\x01",
            "やはり、難しいものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F24")

    TalkEnd(0xFE)
    Return()

    # Function_25_8207 end

    def Function_26_8F28(): pass

    label("Function_26_8F28")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0434
    ChrTalk(
        0x15,
        (
            "#03608Fレオールさんの腰痛の薬……\x01",
            "それにアンジェさんの家では\x01",
            "絆創膏が不足しているか。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x16,
        (
            "#03700Fこの宿のご主人も、\x01",
            "一部の調味料が切れかかっていて\x01",
            "困っている様子だったわ。\x02\x03",

            "#03708Fあの香辛料は百貨店のデパートにしか\x01",
            "置いてないものだったと思うけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x15,
        (
            "#03603Fふむ……絆創膏は\x01",
            "何とかなりそうだけど、\x01",
            "他は交渉の必要がありそうだね。\x02\x03",

            "#03600Fありがとう、ソフィア。\x01",
            "後は僕に任せて休んでてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x10)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_26_8F28 end

    def Function_27_90D5(): pass

    label("Function_27_90D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9104")
    Call(0, 38)
    Return()

    label("loc_9104")

    Call(0, 39)
    Return()

    label("loc_9108")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_27_90D5 end

    def Function_28_910F(): pass

    label("Function_28_910F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913E")
    Call(0, 38)
    Return()

    label("loc_913E")

    Call(0, 39)
    Return()

    label("loc_9142")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_28_910F end

    def Function_29_9149(): pass

    label("Function_29_9149")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_915A")
    Jump("loc_9365")

    label("loc_915A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9168")
    Jump("loc_9365")

    label("loc_9168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9183")
    Call(0, 26)
    Jump("loc_9200")

    label("loc_9183")


    #C0437
    ChrTalk(
        0x16,
        (
            "#03700F私も主人のパートナーとして、\x01",
            "微力ながらお手伝いしています。\x02\x03",

            "少しでも、村の皆さんの\x01",
            "役に立てればいいのですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9200")

    Jump("loc_9365")

    label("loc_9205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F5")

    #C0438
    ChrTalk(
        0x16,
        (
            "#03708F支援課の他の皆さん……\x01",
            "心配ですね。\x02\x03",

            "#03700Fどうか無事に合流できる事を\x01",
            "お祈りさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x105,
        "#10402Fフフ、ありがとうマダム。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x103,
        (
            "#00200Fこうなったらなんとしても、\x01",
            "合流しないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_9365")

    label("loc_92F5")


    #C0441
    ChrTalk(
        0x16,
        (
            "#03708F支援課の他の皆さん……\x01",
            "心配ですね。\x02\x03",

            "#03700F皆さんが無事に合流できる事を\x01",
            "お祈りさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9365")

    TalkEnd(0xFE)
    Return()

    # Function_29_9149 end

    def Function_30_9369(): pass

    label("Function_30_9369")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_937A")
    Jump("loc_9739")

    label("loc_937A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9388")
    Jump("loc_9739")

    label("loc_9388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_940C")

    #C0442
    ChrTalk(
        0x17,
        (
            "#03805Fう～ん、パパたちは\x01",
            "おしごとしてるみたいだし……\x02\x03",

            "#03800Fカミーユくんたちのところに\x01",
            "あそびにいこうかな～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9739")

    label("loc_940C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9602")
    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94B0")
    Jump("loc_94FA")

    label("loc_94B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_94D0")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94FA")

    label("loc_94D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94F0")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94FA")

    label("loc_94F0")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_94FA")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    #C0443
    ChrTalk(
        0x17,
        (
            "#03809Fえへへ、ワンちゃん。\x01",
            "また遊んでね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x107,
        (
            "#01200F#3Cうむ、時が許せばな。\x02\x03",

            "#01203F……しかし、支援課に\x01",
            "入ってからというもの、\x01",
            "やたらと幼子に懐かれるものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x103,
        (
            "#00202Fふふっ、\x01",
            "それがツァイトのいい所かと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_9734")

    label("loc_9602")

    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9693")
    Jump("loc_96DD")

    label("loc_9693")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96B3")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96DD")

    label("loc_96B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96D3")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96DD")

    label("loc_96D3")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96DD")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    #C0446
    ChrTalk(
        0x17,
        (
            "#03809Fえへへ、ワンちゃん。\x01",
            "また遊んでね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9734")

    ClearChrFlags(0x17, 0x10)

    label("loc_9739")

    TalkEnd(0xFE)
    Return()

    # Function_30_9369 end

    def Function_31_973D(): pass

    label("Function_31_973D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9753")
    SetScenarioFlags(0x2, 2)

    label("loc_9753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA9")

    #C0447
    ChrTalk(
        0x18,
        (
            "#04303F#30Wこっちのメルカバは\x01",
            "しばらく使い物にならへんけど……\x02\x03",

            "#04300F回復しだい、オレたちも出来る限りの\x01",
            "バックアップをさせてもらうつもりや。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_9905")
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x10)
    TurnDirection(0x18, 0x105, 0)
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9891")
    Jump("loc_98DB")

    label("loc_9891")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_98B1")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98DB")

    label("loc_98B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98D1")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98DB")

    label("loc_98D1")

    OP_52(0x18, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_98DB")

    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x10)

    label("loc_9905")


    #C0448
    ChrTalk(
        0x18,
        (
            "#04308F#30W──ワジ。\x01",
            "あんまり無茶すんなや？\x02\x03",

            "#04301Fオレみたいに力を使い果たしたら\x01",
            "ここぞの時に命取りになりかねへんで。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x105,
        (
            "#10403Fああ……\x01",
            "せいぜい肝に銘じておくよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA4")
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x18,
        (
            "#04300F#30Wそや……忘れる所やった。\x01",
            "ロイド君、手ぇ出し。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0451
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 2)

    #C0452
    ChrTalk(
        0x104,
        "#00305Fこいつは……\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#00005F何かの欠片……ですか？\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x18,
        (
            "#04303F#30Wアイオーンが\x01",
            "墜落した場所に落ちとった……\x01",
            "多分、ヤツのどっかの部品や。\x02\x03",

            "#04300Fロイド君たちやったら\x01",
            "何か使い道があるかもしれん思て、\x01",
            "拾っといたモンでな。\x02\x03",

            "#04311Fま、せっかくやからとっとき。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ……\x01",
            "ありがたく頂いておきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BA4")

    Jump("loc_9C66")

    label("loc_9BA9")


    #C0456
    ChrTalk(
        0x18,
        (
            "#04303F#30Wこっちのメルカバは\x01",
            "しばらく使い物にならへんけど……\x02\x03",

            "#04300F回復しだい、オレたちも出来る限りの\x01",
            "バックアップをさせてもらうつもりや。\x02\x03",

            "#04302Fとにかく気張れや、ロイド君たち！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C66")

    TalkEnd(0xFE)
    Return()

    # Function_31_973D end

    def Function_32_9C6A(): pass

    label("Function_32_9C6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D95")

    #C0457
    ChrTalk(
        0x19,
        (
            "#13808F日曜学校に来ていたキーアさんは\x01",
            "いつも皆さんの事を\x01",
            "楽しそうに話していました。\x02\x03",

            "#13804F……星杯の騎士としては\x01",
            "相応しくない発言かもしれませんが……\x02\x03",

            "#13802Fあの笑顔を取り戻すことは\x01",
            "何より価値がある事だと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        "#00102Fリースさん……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        "#00204F……合点承知です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E26")

    label("loc_9D95")


    #C0460
    ChrTalk(
        0x19,
        (
            "#13808F日曜学校に来ていたキーアさんは\x01",
            "いつも皆さんの事を\x01",
            "楽しそうに話していました。\x02\x03",

            "#13804F……どうかあの笑顔を\x01",
            "取り戻してあげてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E26")

    TalkEnd(0xFE)
    Return()

    # Function_32_9C6A end

    def Function_33_9E2A(): pass

    label("Function_33_9E2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F35")

    #C0461
    ChrTalk(
        0xFE,
        (
            "本会議に向けて、依頼がてら\x01",
            "各地を見回っているところだけど、\x01",
            "この辺りは平和そのものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "村長さんとデリック君の関係が\x01",
            "若干険悪になってるのが気になるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        (
            "まあ、それは俺が口出しすることじゃない。\x01",
            "遊撃士はあくまで中立でいないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_9FCD")

    label("loc_9F35")


    #C0464
    ChrTalk(
        0xFE,
        (
            "村長さんとデリック君の関係が\x01",
            "若干険悪になってるのが気になるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "まあ、それは俺が口出しすることじゃない。\x01",
            "遊撃士はあくまで中立でいないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FCD")

    TalkEnd(0xFE)
    Return()

    # Function_33_9E2A end

    def Function_34_9FD1(): pass

    label("Function_34_9FD1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A057")

    #C0466
    ChrTalk(
        0xFE,
        (
            "渡り橋のところに、\x01",
            "身なりのいいおじさんが\x01",
            "いたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "……まあ、いいか。\x01",
            "人間には興味ないし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_A092")

    label("loc_A057")


    #C0468
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xFE,
        (
            "ここのオムライスは、\x01",
            "お気に入り……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A092")

    TalkEnd(0xFE)
    Return()

    # Function_34_9FD1 end

    def Function_35_A096(): pass

    label("Function_35_A096")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(78100, 1500, -3470, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x19, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 36)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x102, 1, 0, 36)
    WaitChrThread(0x102, 1)
    BeginChrThread(0x103, 1, 0, 36)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x104, 1, 0, 36)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A135")
    BeginChrThread(0x109, 1, 0, 36)
    WaitChrThread(0x109, 1)

    label("loc_A135")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A14F")
    BeginChrThread(0x105, 1, 0, 36)
    WaitChrThread(0x105, 1)

    label("loc_A14F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A169")
    BeginChrThread(0x106, 1, 0, 36)
    WaitChrThread(0x106, 1)

    label("loc_A169")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A183")
    BeginChrThread(0x10A, 1, 0, 36)
    WaitChrThread(0x10A, 1)

    label("loc_A183")

    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0xFA0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(70310, 1500, -240, 3000)
    MoveCamera(313, 27, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_A267():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A267)
    Sleep(50)

    def lambda_A277():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A277)
    Sleep(50)

    def lambda_A287():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A287)
    Sleep(50)

    def lambda_A297():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A297)
    Sleep(50)

    def lambda_A2A7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_A2A7)
    Sleep(50)

    def lambda_A2B7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_A2B7)
    OP_6F(0x79)

    #C0470
    ChrTalk(
        0x101,
        "#00005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x102,
        "#00105Fリースさん……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A328")

    #C0472
    ChrTalk(
        0x105,
        "#10402Fなんだ、ここにいたのか。\x02",
    )

    CloseMessageWindow()

    label("loc_A328")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetChrSubChip(0x18, 0x1)
    OP_93(0x19, 0x5A, 0x1F4)

    #C0473
    ChrTalk(
        0x19,
        "#13805F皆さん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A39B")

    #C0474
    ChrTalk(
        0x18,
        (
            "#11P#04300F#30Wああ……\x01",
            "ワジにロイド君たちか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C0")

    label("loc_A39B")


    #C0475
    ChrTalk(
        0x18,
        "#11P#04300F#30Wああ……君らか。\x02",
    )

    CloseMessageWindow()

    label("loc_A3C0")

    SetChrPos(0x0, 85600, 0, -1570, 0)
    SetChrPos(0x1, 85600, 0, -1570, 0)
    SetChrPos(0x2, 85600, 0, -1570, 0)
    SetChrPos(0x3, 85600, 0, -1570, 0)
    SetChrPos(0x4, 85600, 0, -1570, 0)
    SetChrPos(0x5, 85600, 0, -1570, 0)
    OP_68(70310, 1200, -240, 3000)
    MoveCamera(310, 19, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(24880, 3000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 37)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x102, 1, 0, 37)
    WaitChrThread(0x102, 1)
    BeginChrThread(0x103, 1, 0, 37)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x104, 1, 0, 37)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4A0")
    BeginChrThread(0x109, 1, 0, 37)
    WaitChrThread(0x109, 1)

    label("loc_A4A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4BA")
    BeginChrThread(0x105, 1, 0, 37)
    WaitChrThread(0x105, 1)

    label("loc_A4BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4D4")
    BeginChrThread(0x106, 1, 0, 37)
    WaitChrThread(0x106, 1)

    label("loc_A4D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4EE")
    BeginChrThread(0x10A, 1, 0, 37)
    WaitChrThread(0x10A, 1)

    label("loc_A4EE")

    WaitChrThread(0x104, 2)
    Sleep(1000)

    #C0476
    ChrTalk(
        0x101,
        "#6P#00000Fお２人とも、話は聞きました。\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x104,
        (
            "#12P#00309Fあのとんでもない飛行人形を\x01",
            "見事、撃墜したそうじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x102,
        "#12P#00104F本当にお疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x18,
        (
            "#11P#04302F#30Wハハ……\x01",
            "コッチの被害も甚大やけどなぁ。\x02\x03",

            "#04306F情けないことに力を使い果たして\x01",
            "休ませてもらってる所やけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A721")

    #C0480
    ChrTalk(
        0x103,
        (
            "#6P#00205Fアッバスさんによると\x01",
            "かなり危険な“力”を使って\x01",
            "危ない状態だったとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x105,
        (
            "#12P#10404Fああ、《聖痕》の力とメルカバを\x01",
            "連動させて一気に解放したんだって？\x02\x03",

            "#10402Fまったく無茶するなぁ。\x01",
            "下手したら女神#4Rエイドス#行きだと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A77B")

    label("loc_A721")


    #C0482
    ChrTalk(
        0x103,
        (
            "#6P#00205Fアッバスさんによると\x01",
            "かなり危険な“力”を使って\x01",
            "危ない状態だったとか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A77B")


    #C0483
    ChrTalk(
        0x101,
        "#6P#00005Fそ、そうなのか……？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x19,
        (
            "#5P#13800Fええ、《聖痕》は本来、\x01",
            "人の身には余る禁断の力の源泉……\x02\x03",

            "#13808Fそれを無制限に解放するなど\x01",
            "無謀にもほどがあります。\x02\x03",

            "#13803F責任ある《守護騎士》の立場としては\x01",
            "あまりに軽卒と言わざるを得ませんね。\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0485
    ChrTalk(
        0x18,
        (
            "#11P#04306F#30W……はあ、リース。\x01",
            "そろそろ勘弁してくれや。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9AE")

    #C0486
    ChrTalk(
        0x105,
        (
            "#12P#10409Fハハ、いい感じで\x01",
            "尻に敷かれてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA5B")

    label("loc_A9AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA05")

    #C0487
    ChrTalk(
        0x109,
        (
            "#12P#10109F（な、何だかお尻に\x01",
            "  敷かれてるみたいですね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA5B")

    label("loc_AA05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA5B")

    #C0488
    ChrTalk(
        0x106,
        (
            "#12P#10702F（ふふっ、どうやら頭が\x01",
            "  上がらないみたいですね……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAB6")

    #C0489
    ChrTalk(
        0x10A,
        (
            "#12P#00603F（星杯の守護騎士……\x01",
            "  聞いていた情報と随分違うな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB79")

    label("loc_AAB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB13")

    #C0490
    ChrTalk(
        0x106,
        (
            "#12P#10704F（星杯の守護騎士……\x01",
            "  聞いていたのと随分違いますね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB79")

    label("loc_AB13")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB79")

    #C0491
    ChrTalk(
        0x109,
        (
            "#12P#10106Fふう、君もアッバスさんの言う事を\x01",
            "もっとちゃんと聞くべきだと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB79")


    #C0492
    ChrTalk(
        0x18,
        (
            "#11P#04303F#30Wそれはそうと……\x02\x03",

            "#04308Fしかしまあ、とんでもないモンが\x01",
            "現れてしまったもんやな。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x19,
        (
            "#5P#13801F《碧の大樹》……\x01",
            "人の執念が生み出した奇蹟ですか。\x02\x03",

            "#13803Fまさか女神以外の手で\x01",
            "あのようなものが顕れるなんて……\x02\x03",

            "#13808Fしかも、キーアさんの力で……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x102,
        "#12P#00108F……ええ……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x103,
        (
            "#6P#00203F正直、わたしたちも\x01",
            "まだ実感がありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        (
            "#6P#00003F──ですが、この事件だけは\x01",
            "必ず俺たちで解決するつもりです。\x02\x03",

            "#00001F《特務支援課》として……\x01",
            "何よりもあの子の保護者として。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x18,
        (
            "#11P#04304F#30Wそっか……\x01",
            "とっくに覚悟完了みたいやね。\x02\x03",

            "#04300Fこっちのメルカバは\x01",
            "しばらく使い物にならへんけど……\x02\x03",

            "回復しだい、オレたちも出来る限りの\x01",
            "バックアップをさせてもらうつもりや。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x19,
        (
            "#5P#13802F……女神の加護を。\x01",
            "くれぐれも気を付けてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x104,
        "#12P#00302Fサンクス、リースちゃん。\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#12P#00100Fそれでは行って来ます。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x18, 0x0)
    OP_93(0x19, 0x0, 0x0)
    OP_4C(0x19, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7563", 0)
    SetChrPos(0x0, 71500, 0, -610, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_1B(0x3, 0xFF, 0xFFFF)
    SetScenarioFlags(0x1CE, 0)
    EventEnd(0x5)
    Return()

    # Function_35_A096 end

    def Function_36_AF10(): pass

    label("Function_36_AF10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF3F")
    SetChrPos(0xFE, 77230, 0, -2080, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AF3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF6E")
    SetChrPos(0xFE, 78370, 0, -1940, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AF6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9D")
    SetChrPos(0xFE, 79550, 0, -2100, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AF9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFCC")
    SetChrPos(0xFE, 77200, 0, -3170, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AFCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFFB")
    SetChrPos(0xFE, 78370, 0, -3110, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AFFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01B")
    SetChrPos(0xFE, 79550, 0, -3200, 0)

    label("loc_B01B")

    Return()

    # Function_36_AF10 end

    def Function_37_B01C(): pass

    label("Function_37_B01C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B065")
    SetChrPos(0xFE, 78700, 0, -1050, 270)

    def lambda_B041():
        OP_95(0xFE, 71150, 0, -1050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B041)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B065")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0AE")
    SetChrPos(0xFE, 78650, 0, 0, 270)

    def lambda_B08A():
        OP_95(0xFE, 71150, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B08A)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B0AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F7")
    SetChrPos(0xFE, 79740, 0, -1220, 270)

    def lambda_B0D3():
        OP_95(0xFE, 72240, 0, -1220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B0D3)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B0F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B140")
    SetChrPos(0xFE, 79740, 0, -40, 270)

    def lambda_B11C():
        OP_95(0xFE, 72240, 0, -40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B11C)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B140")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B189")
    SetChrPos(0xFE, 80780, 0, -1100, 270)

    def lambda_B165():
        OP_95(0xFE, 73280, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B165)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B189")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C3")
    SetChrPos(0xFE, 80780, 0, 20, 270)

    def lambda_B1AE():
        OP_95(0xFE, 73280, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B1AE)

    label("loc_B1C3")

    Return()

    # Function_37_B01C end

    def Function_38_B1C4(): pass

    label("Function_38_B1C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1240, 1700, -2210, 0)
    MoveCamera(340, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23160, 0)
    SetChrPos(0x101, -700, 0, -550, 300)
    SetChrPos(0x102, -1350, 0, -1680, 300)
    SetChrPos(0x104, -670, 0, -2990, 300)
    SetChrPos(0x109, 860, 0, -380, 270)
    SetChrPos(0x105, 350, 0, -1860, 300)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1A, -2340, 180, 910, 135)
    SetChrPos(0x1B, -3100, 190, -1070, 135)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0501
    ChrTalk(
        0x1A,
        "#5Pやあ、来たね。\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x1B,
        (
            "#5Pティオちゃん！\x01",
            "……はまだいないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x1B,
        "#5Pはあ、テンション下がるなあ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0504
    ChrTalk(
        0x101,
        "#12P#00006Fな、何かすみません。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x1A,
        (
            "#5Pいや……\x01",
            "こちらこそすまない。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        (
            "#12P#00309Fでも、エオリアさん……\x01",
            "相変わらず素敵ッス。\x02\x03",

            "#00304Fこの際、ティオすけは諦めて\x01",
            "俺に乗り換えません？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1B,
        "#5Pううん、遠慮するわ㈱\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x104,
        "#12P#00306Fぐさっ……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x109,
        "#12P#10106Fラ、ランディ先輩……\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x105,
        "#12P#10302Fフフ、見事な玉砕ぶりだね。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x102,
        (
            "#12P#00106Fもう、ランディも\x01",
            "いい加減学習しなさいよ。\x02\x03",

            "#00100Fすみません、リンさん。\x01",
            "さっそく依頼の話を\x01",
            "聞きたいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x1A,
        (
            "#5Pああ、説明させてもらう。\x01",
            "といっても単純な話さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x1A,
        (
            "#5P付き合ってもらいたいのは\x01",
            "他ならぬ私たち自身の訓練――\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x1A,
        (
            "#5Pつまりは、私たちとアンタたちとで\x01",
            "手合わせをしたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        (
            "#12P#00000F手合わせということは……\x01",
            "実戦形式で戦うわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#12P#00100Fでも、どうしてまた\x01",
            "今になってそんな依頼を？\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x1B,
        (
            "#5Pそりゃあ、ちょっと前だと\x01",
            "ヒヨッコ過ぎたからじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0518
    ChrTalk(
        0x101,
        "#12P#00012F確かに返す言葉もありませんが……\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        "#12P#00106Fええ、胸に突き刺さるわね。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x1A,
        (
            "#5Pはは、まあいいじゃないか。\x01",
            "その代わり今はもう\x01",
            "アンタたちの実力を認めてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x1A,
        (
            "#5Pそれこそ、私たちが\x01",
            "肌で感じておきたいと思う程にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x1B,
        (
            "#5Pちょうど私とリンの空き時間が\x01",
            "重なることも分かって\x01",
            "今しかないって思ったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x1B,
        (
            "#5Pスコットとヴェンツェルには\x01",
            "悪いんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        (
            "#12P#00009Fあはは、あの２人までいたら\x01",
            "さらにとんでもないことに\x01",
            "なっていそうですけど。\x02\x03",

            "#00000Fでも確かに。\x01",
            "こんな機会滅多にないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x104,
        (
            "#12P#00300Fおうよ！\x01",
            "ぜひ胸をお借りしたいッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x105,
        (
            "#12P#10300F胸を借りる、か……\x02\x03",

            "#10304Fランディが言うと\x01",
            "別の意味にも取れそうだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0527
    ChrTalk(
        0x109,
        (
            "#12P#10100Fそれってどういう……\x02\x03",

            "#10114Fあ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)
    TurnDirection(0x102, 0x105, 500)
    Sleep(300)

    #C0528
    ChrTalk(
        0x102,
        (
            "#6P#00111Fワジ君……これ以上\x01",
            "引っ掻き回さないでくれる？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x1A,
        (
            "#5Pはは、どうやら新しい面子も\x01",
            "楽しませてくれそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x1B,
        (
            "#5Pうんうん、見たところ\x01",
            "２人とも相当できるみたいだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x12C, 0x1F4)
    Sleep(300)

    #C0531
    ChrTalk(
        0x109,
        (
            "#12P#10102Fそ、相当かどうかは\x01",
            "さすがに自信ないですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x105,
        "#12P#10300Fフフ、まあ光栄な話だね。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x1A,
        (
            "#5Pで、どうする。\x01",
            "受けてくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        (
            "#12P#00004Fええ……\x01",
            "できればそのつもりですけど。\x02\x03",

            "#00000F場所はどうするんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x1A,
        (
            "#5Pああ、それなりに広くて\x01",
            "生活の邪魔にならないってことで\x01",
            "村の入口を考えている。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x1A,
        (
            "#5P村長の許可も取ってあるから\x01",
            "いつでも使っていいとのことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x1A,
        (
            "#5P既に準備ができてるんなら\x01",
            "すぐにでも始めたいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x1B,
        (
            "#5P装備や買い物は大丈夫？\x01",
            "準備が必要だったら待つけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        "#12P#00000Fそうですね……\x02",
    )

    CloseMessageWindow()
    OP_29(0x75, 0x1, 0x0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【準備万端、手合わせを行う】\x01",      # 0
            "【やめておく】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE9A")

    #C0540
    ChrTalk(
        0x101,
        (
            "#12P#00000F準備は出来ているので\x01",
            "さっそく移動してもいいですか？\x02\x03",

            "#00004Fお２人との手合わせ、\x01",
            "正式に受けさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x1A,
        "#5Pふふ、そうこなくっちゃ。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x1B,
        "#5Pそれじゃ、さっそく訓練開始ね！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CloseMessageWindow()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0543
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【遊撃士訓練への参加要請】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_BFDE")

    label("loc_BE9A")


    #C0544
    ChrTalk(
        0x101,
        (
            "#12P#00000F準備したいことがあるので、\x01",
            "待ってもらっていいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x1A,
        "#5Pああ、もちろん。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x1A,
        (
            "#5Pそれと、他に用事があったら\x01",
            "別にそちらを優先してくれても\x01",
            "構わないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x1B,
        (
            "#5P元々私たちも空き時間を\x01",
            "利用してるだけだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x1B,
        (
            "#5Pその時は、気にせずここで\x01",
            "ゆっくりさせてもらうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        "#12P#00000Fはい、了解です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BFDE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0x0, -70, 0, -3430, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x155, 7)
    SetChrPos(0x1A, -2510, 180, 1180, 270)
    SetChrPos(0x1B, -3380, 190, -810, 0)
    EventEnd(0x5)
    Return()

    # Function_38_B1C4 end

    def Function_39_C036(): pass

    label("Function_39_C036")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1240, 1700, -2210, 0)
    MoveCamera(340, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23160, 0)
    SetChrPos(0x101, -700, 0, -550, 300)
    SetChrPos(0x102, -1350, 0, -1680, 300)
    SetChrPos(0x104, -670, 0, -2990, 300)
    SetChrPos(0x109, 860, 0, -380, 270)
    SetChrPos(0x105, 350, 0, -1860, 300)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1A, -2340, 180, 910, 135)
    SetChrPos(0x1B, -3100, 190, -1070, 135)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0550
    ChrTalk(
        0x1A,
        "#5Pやあ、準備はできたかい？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x1B,
        (
            "#5P私たちとの手合わせ、\x01",
            "受けてくれる？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【準備万端、手合わせを行う】\x01",      # 0
            "【やめておく】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C2")

    #C0552
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、バッチリです。\x01",
            "さっそく移動してもいいですか？\x02\x03",

            "お２人との手合わせ、\x01",
            "正式に受けさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x1A,
        "#5Pふふ、そうこなくっちゃ。\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x1B,
        "#5Pそれじゃ、さっそく訓練開始ね！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CloseMessageWindow()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0555
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【遊撃士訓練への参加要請】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_C3B1")

    label("loc_C2C2")


    #C0556
    ChrTalk(
        0x101,
        (
            "#12P#00006Fすみません……\x01",
            "まだちょっと、かかりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x1A,
        "#5Pああ、そうかい。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x1A,
        (
            "#5Pま、もし他にも用事があるんなら\x01",
            "そちらを優先しなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x1B,
        (
            "#5P別に私たちのことは\x01",
            "気にしなくていいからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x101,
        "#12P#00000Fええ、分かりました。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C3B1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0x0, -70, 0, -3430, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1A, -2510, 180, 1180, 270)
    SetChrPos(0x1B, -3380, 190, -810, 0)
    EventEnd(0x5)
    Return()

    # Function_39_C036 end

    def Function_40_C406(): pass

    label("Function_40_C406")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xA, 0xB4, 0x0)
    OP_68(410, 1500, 3290, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -510, 0, 3060, 0)
    SetChrPos(0x102, 940, 0, 2410, 0)
    SetChrPos(0x103, -1310, 0, 2160, 0)
    SetChrPos(0x104, 120, 0, 1520, 0)
    SetChrPos(0x109, -980, 0, 540, 0)
    SetChrPos(0x105, 920, 0, 440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0561
    ChrTalk(
        0xA,
        (
            "やあ、支援課の諸君。\x01",
            "《トネリコ亭》にようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xA,
        (
            "今日は何か食べていくかい？\x01",
            "それとも、宿泊かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x101,
        (
            "#00000Fええと、今日は仕事で\x01",
            "来たんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0564
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

    #C0565
    ChrTalk(
        0xA,
        (
            "ああ、そのことか。\x01",
            "クロスベル通信社から\x01",
            "話は聞いているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "それじゃあ、早速君たちに\x01",
            "僕の『匠風オムライス』を\x01",
            "ご馳走させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x105,
        "#10300Fフフ、よろしく頼むよマスター。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    SetChrPos(0x103, -2490, 200, 950, 245)
    SetChrPos(0x101, -4490, 200, 2190, 175)
    SetChrPos(0x104, -5400, 200, 1100, 126)
    SetChrPos(0x102, -5210, 200, -110, 65)
    SetChrPos(0x109, -4380, 200, -1100, 30)
    SetChrPos(0x105, -3410, 200, -1000, 0)
    SetChrPos(0xA, -3130, 200, 3130, 180)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x24)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x24)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_68(-4100, 1600, 580, 0)
    MoveCamera(310, 33, 0, 0)
    OP_6E(330, 0)
    SetCameraDistance(25000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0568
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは匠風オムライスを食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0569
    ChrTalk(
        0x102,
        (
            "#00104Fぱくぱく……\x01",
            "う～ん、やっぱりここの\x01",
            "オムライスは美味しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x103,
        "#00200Fええ、本当に絶品だと思います。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x101,
        (
            "#00000Fふんわりとした卵に包まれた\x01",
            "チキンライスのケチャップ味が、\x01",
            "何とも素朴でいいんだよな。\x02\x03",

            "#00004Fこの大自然に囲まれた\x01",
            "アルモリカ村でっていうのも\x01",
            "いいロケーションだと思うし……\x02\x03",

            "#00009Fアルモリカ村に来たら\x01",
            "これを食べずには帰れないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "はは、そこまで言われると\x01",
            "なんだか照れてしまうなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x109,
        (
            "#10102Fふふ、ここのオムライスは\x01",
            "ロイドさんのお気に入りみたいですし……\x02\x03",

            "ガイドの記事は任せてよさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    #C0574
    ChrTalk(
        0x104,
        (
            "#00306Fま、ここはマスターの人柄も含めて\x01",
            "しっかり一押しにしとかないとな。\x02\x03",

            "#00300F前にもごちそうしてもらったりしたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        (
            "#00000Fああ、俺が責任を持って\x01",
            "書かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        (
            "はは、是非ともうちが\x01",
            "繁盛してくれるような記事を\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -600, 0, 3900, 0)
    SetChrPos(0x102, 600, 0, 3900, 0)
    SetChrPos(0x103, -600, 0, 2700, 0)
    SetChrPos(0x109, 600, 0, 2700, 0)
    SetChrPos(0x104, -600, 0, 1500, 0)
    SetChrPos(0x105, 600, 0, 1500, 0)
    SetChrPos(0xA, -40, 0, 6040, 180)
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
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_68(590, 2000, 2950, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(330, 0)
    SetCameraDistance(25000, 0)
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
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x172, 7)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_CD04")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_CD21")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_CD34")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_CD47")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_CD64")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_CD77")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_CD94")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_CDA7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_CDC4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_CDD7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_CDF4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDF4")

    OP_29(0x80, 0x1, 0x7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEF7")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0577
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEEE")

    #A0578
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

    label("loc_CEEE")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_CEF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFC8")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0579
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

    #A0580
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

    label("loc_CFC8")

    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -250, 0, -920, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_40_C406 end

    def Function_41_D002(): pass

    label("Function_41_D002")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    OP_68(730, 1500, 2190, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -510, 0, 3060, 0)
    SetChrPos(0x102, 940, 0, 2410, 0)
    SetChrPos(0x103, -1310, 0, 2160, 0)
    SetChrPos(0x104, 120, 0, 1520, 0)
    SetChrPos(0x109, -980, 0, 540, 0)
    SetChrPos(0x105, 920, 0, 440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0581
    ChrTalk(
        0x101,
        (
            "#00000Fあの、少々お尋ね\x01",
            "したいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0582
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最近村を訪れているという\x01",
            "外国人について尋ねた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0583
    ChrTalk(
        0xA,
        (
            "ああ、最近たまに\x01",
            "ウチに泊まりにくるあの人か。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xA,
        (
            "うん、とても礼儀正しくて\x01",
            "好感が持てる人だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x104,
        "#00303F礼儀正しい、ねえ。\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x102,
        (
            "#00105Fそういえば……\x01",
            "その方の名前などは\x01",
            "ご存知でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xA,
        (
            "えーっと、確か……\x01",
            "『ミンネス』さんだったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xA,
        (
            "宿泊客名簿には\x01",
            "そうサインしてたようだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x105,
        (
            "#10300F『ミンネス』か……\x01",
            "フフ、とりあえず名前は\x01",
            "明らかになったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x103,
        (
            "#00201Fそれで、そのミンネスさんについて\x01",
            "何か知ってる事はありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xA,
        (
            "うーん、あまり話した事が\x01",
            "ないから、なんとも言えないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xA,
        (
            "ただ、部屋にデリックくんを呼んで\x01",
            "何度か話し合っているみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xA,
        "私に分かるのはそれくらいかなあ。\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x109,
        (
            "#10105F（例の村長の息子さんとの\x01",
            "  密談のことみたいですね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        (
            "#00003F（ああ……とにかく、\x01",
            "  そこそこの情報は\x01",
            "  得られたみたいだな。）\x02\x03",

            "#00000Fご協力、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xA,
        "いえいえ、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xA,
        (
            "ついでになにか\x01",
            "注文してってくれるとうれしいよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 700, 0, 2050, 90)
    BeginChrThread(0xB, 0, 0, 1)
    OP_4C(0xA, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x174, 1)
    OP_29(0x82, 0x1, 0x1)
    SetChrPos(0x0, 120, 0, 1520, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_41_D002 end

    def Function_42_D514(): pass

    label("Function_42_D514")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-40910, 1500, 2430, 0)
    MoveCamera(345, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -41240, 0, 2080, 45)
    SetChrPos(0x102, -42090, 0, 3420, 90)
    SetChrPos(0x103, -40430, 0, 960, 0)
    SetChrPos(0x104, -41790, 0, 470, 45)
    SetChrPos(0x109, -42790, 0, 1440, 450)
    SetChrPos(0x105, -43210, 0, 2600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0598
    ChrTalk(
        0x101,
        (
            "#00000Fあの、少々お尋ね\x01",
            "したいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0599
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最近村を訪れているという\x01",
            "外国人について尋ねた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0600
    ChrTalk(
        0x8,
        (
            "ああ、あの男か。\x01",
            "なかなか見る目のある男じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        "#00105F……というと？\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x8,
        (
            "なんでも、村の蜂蜜を\x01",
            "とても気に入ってくれたらしくてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x8,
        (
            "『これならきっと、\x01",
            "  大陸中に通用します！』\x01",
            "……などと言ってくれたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x103,
        "#00203F通用……ですか。\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x105,
        (
            "#10300F話しぶりから察するに、\x01",
            "商売人か何かなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x8,
        (
            "うむ、詳しくは聞かなかったが\x01",
            "おそらくそうじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x8,
        (
            "あの慧眼の持ち主ならば\x01",
            "さぞかし名のある男なのじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x8,
        (
            "まったく、ウチの孫にも\x01",
            "見習わせたいくらいじゃわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x109,
        "#10112Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x104,
        (
            "#00303Fとにかく腕を感じさせる\x01",
            "商売人って感じなわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        (
            "#00000Fなるほど……\x01",
            "色々と分かりました。\x02\x03",

            "#00004Fご協力、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x8,
        "うむ、またいつでも来るとええ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x174, 2)
    OP_29(0x82, 0x1, 0x2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -41240, 0, 2080, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_42_D514 end

    def Function_43_D941(): pass

    label("Function_43_D941")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xA, 0xB4, 0x0)
    OP_68(410, 1500, 3290, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -510, 0, 3060, 0)
    SetChrPos(0x102, 940, 0, 2410, 0)
    SetChrPos(0x103, -1310, 0, 2160, 0)
    SetChrPos(0x104, 120, 0, 1520, 0)
    SetChrPos(0x109, -980, 0, 540, 0)
    SetChrPos(0x105, 920, 0, 440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0613
    ChrTalk(
        0xA,
        (
            "おや……\x01",
            "もしかして、宿泊かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xA,
        "今なら部屋が空いてるよ。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        (
            "#00005F（そうだ、もしゲバルさんが\x01",
            "  アルモリカ村に\x01",
            "  来ているとしたら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x103,
        (
            "#00203F（宿酒場に来ている可能性は\x01",
            "  高いかもしれませんね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x101,
        (
            "#00000Fあの、ちょっと\x01",
            "お聞きしたいんですが……\x02\x03",

            "こちらに、ゲバルという方が\x01",
            "宿泊されてませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xA,
        "ああ、ゲバルさんか。\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xA,
        (
            "最近、たまに食事に\x01",
            "来てくれてるお客さんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x102,
        (
            "#00105Fたまに食事に……？\x02\x03",

            "こちらに宿泊されている\x01",
            "わけではないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xA,
        (
            "いや、そんなはずは無いよ。\x01",
            "受付した覚えはないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xA,
        (
            "うちの味を気に入って、\x01",
            "市内から通ってくれてるんだと\x01",
            "思ってたんだけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x104,
        (
            "#00303Fんー……\x01",
            "流石にそりゃ現実的じゃ\x01",
            "なさそうな気もするが。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x109,
        (
            "#10100Fあるいは……\x01",
            "アルモリカ村に親戚でも\x01",
            "いるんですかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x105,
        (
            "#10300Fそうだとしたら、\x01",
            "アルムさんたちがすでに\x01",
            "調べてそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_END)), "loc_DDCE")

    #C0626
    ChrTalk(
        0x101,
        "#00003Fもしかすると……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    #C0627
    ChrTalk(
        0x101,
        (
            "#00001F……一度、村長に相談してみよう。\x01",
            "何か知ってるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_DE45")

    label("loc_DDCE")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    #C0628
    ChrTalk(
        0x101,
        (
            "#00003F一応、調査をしてみようか。\x02\x03",

            "#00000Fもしかしたら\x01",
            "身を隠せそうな場所が\x01",
            "あるのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE45")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 700, 0, 2050, 90)
    BeginChrThread(0xB, 0, 0, 1)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x19B, 2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 120, 0, 1520, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_43_D941 end

    def Function_44_DE9F(): pass

    label("Function_44_DE9F")

    EventBegin(0x0)
    Fade(500)
    OP_68(-580, 1200, 2920, 0)
    MoveCamera(308, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0xD, -1420, 180, 3810, 90)
    SetChrSubChip(0xD, 0x2)
    SetChrPos(0x101, -470, 0, 2360, 0)
    SetChrPos(0x102, -1200, 0, 1520, 0)
    SetChrPos(0x104, 880, 0, 1830, 0)
    SetChrPos(0x109, 80, 0, 1070, 0)
    SetChrPos(0x105, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_93(0xA, 0xB4, 0x0)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0629
    ChrTalk(
        0xA,
        (
            "#11Pおや……\x01",
            "君たちはたしか、警察の\x01",
            "特務支援課だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xA,
        "#11P以前は依頼でお世話になったね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_E0CB")

    #C0631
    ChrTalk(
        0xD,
        (
            "#5Pああ、確か古戦場に迷い込んだ\x01",
            "観光客を探してくれたんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xD,
        (
            "#5Pそういえば、私のほうは\x01",
            "図書館の本の件でも\x01",
            "迷惑をかけてしまったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x101,
        (
            "#00012Fはは……\x01",
            "いえいえ、お気になさらず。\x02\x03",

            "#00000F最近、変わったことは\x01",
            "ありませんでしたか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E163")

    label("loc_E0CB")


    #C0634
    ChrTalk(
        0xD,
        (
            "#5Pああ、確か古戦場に迷い込んだ\x01",
            "観光客を探してくれたんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        (
            "#00000Fええ、ご無沙汰しています。\x02\x03",

            "最近、変わったことは\x01",
            "ありませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E163")


    #C0636
    ChrTalk(
        0xA,
        (
            "#11Pそうだねえ、\x01",
            "この村はいたって\x01",
            "平和なものだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xA,
        (
            "#11P強いて言うならこの間、\x01",
            "見慣れない人たちが\x01",
            "村を訪れたってことくらいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xD,
        "#5Pああ、あの赤毛の大男たちか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0639
    ChrTalk(
        0x102,
        "#00105F赤毛の大男って……\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x104,
        (
            "#6P#00301F……もしかして、\x01",
            "その赤毛っつうのは\x01",
            "俺の髪と同じ色じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xA,
        (
            "#11Pおや、そういえば\x01",
            "確かに似てる気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xA,
        (
            "#11Pその赤毛の大男と、\x01",
            "一緒にいた活発そうなお嬢ちゃんが\x01",
            "そんな髪の色だったと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0643
    ChrTalk(
        0x101,
        (
            "#00001F……あの、詳しく聞かせて\x01",
            "いただきたいんですが……\x01",
            "その人たちは、この村で何を？\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xA,
        (
            "#11Pいや～、ずっと見てたって\x01",
            "わけじゃないからなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xA,
        "#11P君はどうだい、アルフ？\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xD,
        (
            "……そういえば、雑貨店のほうで\x01",
            "買い物をしていたのを見たな。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xD,
        (
            "何やら、チーズやベーコン、黒パンなんかを\x01",
            "大量に買い込んでいたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xD,
        (
            "その日は大儲けだったって\x01",
            "レオール爺さんが大喜びしてたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        "#00103Fそうですか……\x02",
    )

    CloseMessageWindow()

    def lambda_E58A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E58A)
    Sleep(50)

    def lambda_E59A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E59A)
    Sleep(50)

    def lambda_E5AA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E5AA)
    Sleep(50)
    OP_93(0x109, 0x13B, 0x1F4)

    #C0650
    ChrTalk(
        0x101,
        (
            "#11P#00001F……《赤い星座》が\x01",
            "アルモリカ村を訪れていたとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x109,
        (
            "#6P#10101F話を聞く限りでは\x01",
            "食料の調達に来てたみたいですね。\x02\x03",

            "#10103F保存の効きそうなものばかり\x01",
            "買い込んでいたみたいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x104,
        (
            "#12P#00303F……猟兵団にとって、\x01",
            "食糧の確保は基本中の基本だからな。\x02\x03",

            "いつ戦闘が起こってもいいよう、\x01",
            "常に万全の体制を整えておく……\x02\x03",

            "#00301F百戦錬磨の猟兵団であるヤツらは、\x01",
            "その辺を徹底してるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x105,
        "#6P#10300Fフフ、なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        (
            "#00103Fでも、目的は本当に\x01",
            "それだけなのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        (
            "#11P#00001F……ひとまず、\x01",
            "心に留めておいたほうが\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E7F6():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E7F6)
    Sleep(50)

    def lambda_E806():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E806)
    Sleep(50)

    def lambda_E816():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E816)
    Sleep(50)

    def lambda_E826():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E826)
    Sleep(50)

    def lambda_E836():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E836)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0656
    ChrTalk(
        0x101,
        (
            "#00004F……貴重なお話を\x01",
            "ありがとうございます。\x02\x03",

            "#00000Fまた何かありましたら\x01",
            "支援課までご連絡ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xA,
        (
            "#11Pふむ、なんだかよく分からないが\x01",
            "君たちも忙しそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0xA,
        (
            "#11Pまあ、またいつでも来てくれ。\x01",
            "美味しいオムライスを用意して\x01",
            "お待ちしてるからね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xD, -2060, 180, 4000, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0x14F, 0)
    OP_29(0xA3, 0x1, 0x1)
    SetChrPos(0x0, -470, 0, 2360, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_44_DE9F end

    def Function_45_E9A2(): pass

    label("Function_45_E9A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07200.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03700.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03600.itp")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x101, 77920, 0, -5350, 0)
    SetChrPos(0x103, 77920, 0, -5350, 0)
    SetChrPos(0x105, 77920, 0, -5350, 0)
    SetChrPos(0x107, 77920, 0, -5350, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 71500, 0, -1000, 0)
    SetChrPos(0x15, 71500, 0, 0, 180)
    SetChrPos(0x17, 73950, 400, 800, 180)
    OP_68(77910, 700, -5350, 0)
    MoveCamera(320, 30, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    OP_68(72500, 1000, -500, 5000)
    MoveCamera(315, 25, 0, 5000)
    SetCameraDistance(25000, 5000)
    BeginChrThread(0x101, 1, 0, 46)
    Sleep(750)
    BeginChrThread(0x107, 1, 0, 49)
    Sleep(750)
    BeginChrThread(0x103, 1, 0, 47)
    Sleep(750)
    BeginChrThread(0x105, 1, 0, 48)
    OP_0D()
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x17, 0x0, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0659
    AnonymousTalk(
        0x17,
        "あー、おっきなワンちゃんだ～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_EC77():
        OP_93(0x15, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_EC77)
    Sleep(50)

    def lambda_EC87():
        OP_93(0x16, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_EC87)
    Sleep(50)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x16, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0660
    AnonymousTalk(
        0x16,
        "皆さんは……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0661
    AnonymousTalk(
        0x15,
        (
            "おお……ロイドさん！\x02\x03",

            "よかった……\x01",
            "ご無事だったんですね！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0662
    ChrTalk(
        0x101,
        (
            "#00002F#12P……ハロルドさん、\x01",
            "どうもお久しぶりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x107,
        (
            "#01200F#12P#3C……『おっきなワンちゃん』とは\x01",
            "私のことだろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x103,
        "#00204F#6Pふふ、ナイスな呼称かと。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x105,
        "#10409F#12Pアハハ、神狼も形無しだね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x1)
    SetChrPos(0x15, 78650, 0, 1000, 180)
    SetChrPos(0x16, 77650, 0, 1000, 180)
    SetChrPos(0x17, 74900, 0, -150, 135)
    SetChrPos(0x101, 78650, 0, -1000, 0)
    SetChrPos(0x103, 77650, 0, -1000, 0)
    SetChrPos(0x105, 78650, 0, -2250, 0)
    SetChrPos(0x107, 77650, 0, -2750, 0)
    OP_68(77650, 1200, -110, 0)
    MoveCamera(324, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24250, 0)
    SetCameraDistance(23750, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    #C0666
    ChrTalk(
        0x15,
        (
            "#03610F#11Pロイドさんたちが\x01",
            "逮捕されたという噂を聞いて\x01",
            "本当に心配していました。\x02\x03",

            "#03600F何でも脱走犯として\x01",
            "指名手配されたそうですが……\x01",
            "ご無事そうで本当に良かった。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x16,
        (
            "#03708F#11Pあの、他の支援課の皆さんは\x01",
            "どうなさったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x103,
        (
            "#00206F#6P……残念ですが、\x01",
            "離れ離れになっています。\x02\x03",

            "#00208F詳しい居場所も\x01",
            "分からない状態で……\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x16,
        "#03710F#11Pそうでしたか……心配ですね。\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x101,
        (
            "#00001F#6P……ハロルドさんたちは\x01",
            "異変の時、ちょうど村を\x01",
            "訪れていたみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x15,
        (
            "#03610F#11Pええ……\x01",
            "最初は何が起こったのやら、\x01",
            "皆目見当がつきませんでした。\x02\x03",

            "#03608F訳も分からないまま\x01",
            "街道の移動制限が出されて、\x01",
            "街にも戻れなくなってしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x16,
        (
            "#03700F#11Pでも、村の方々には本当に\x01",
            "お世話になっています。\x02\x03",

            "宿のご主人は、ほとぼりが冷めるまで\x01",
            "滞在していくよう言って下さって……\x02\x03",

            "#03709Fコリンも、村の子供達と\x01",
            "すっかり仲良くなったみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x17,
        (
            "#03809F#5Pカミーユくんやプーリーちゃんが\x01",
            "いっぱいあそんでくれるんだよ～。\x02\x03",

            "ワンちゃんも今度一緒に遊ぼうね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x107,
        "#01200F#6P#3Cフフ、考えておこう。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x15,
        (
            "#03609F#11Pはは……ありがとうございます。\x02\x03",

            "#03600Fまあ、そういうわけで\x01",
            "私も恩返しに村のお手伝いを\x01",
            "させて頂いてるんです。\x02\x03",

            "#03604Fとは言っても、時々訪れる\x01",
            "国防軍との交渉を\x01",
            "引き受けるくらいなのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x103,
        (
            "#00204F#6Pいえ、この状況下だと\x01",
            "とても大切な役割かと。\x02\x03",

            "#00202Fハロルドさんのような\x01",
            "ベテランの商人なら、交渉も\x01",
            "かなり慣れているでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x15,
        (
            "#03600F#11Pはは、本当に大したことは\x01",
            "ないんですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x15)

    #C0679
    ChrTalk(
        0x15,
        (
            "#03605F#11Pそうだ、国防軍と交渉している時に\x01",
            "気になる話を聞いたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        "#00005F#6P気になる話……？\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x15,
        (
            "#03610F#11Pええ、なんでもこの辺りに\x01",
            "正体不明の抵抗勢力が\x01",
            "潜んでいるそうなんです。\x02\x03",

            "#03601F何度か国防軍の部隊が\x01",
            "襲撃にあっているらしくて。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0682
    ChrTalk(
        0x101,
        "#00011F#6Pほ、本当ですか！？\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x105,
        (
            "#10402F#6Pへえ……この状況下で\x01",
            "そんな事をする人間がいるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x103,
        (
            "#00201F#6P何者かは分かりませんが……\x01",
            "非常に有益な情報ではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#00003F#6Pああ、確かめる必要がありそうだ。\x02\x03",

            "#00001Fハロルドさん、抵抗勢力というのは\x01",
            "どの辺りで目撃されてるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x15,
        (
            "#03610F#11Pどうやら、古道の途中にある\x01",
            "アルモリカ古戦場のあたりで\x01",
            "目撃されているようです。\x02\x03",

            "#03601F国防軍も定期的に\x01",
            "巡回しているようですが……\x01",
            "成果は上がっていないようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3Cアルモリカ古戦場……\x01",
            "かつて幾度となく血が流され、\x01",
            "教団が本拠地と定めた宿業の地か。\x02\x03",

            "#01201Fあの遺跡には隠れた通路なども多い。\x01",
            "抵抗勢力とやらが身を潜めるのには\x01",
            "適しているだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        (
            "#00013F#6P何が待ってるか分からないけど……\x01",
            "準備を整えて行ってみるか。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x17, 0x14)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x1)
    OP_49()
    OP_D7(0x1E)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    SetChrPos(0x16, 71500, 0, -1000, 0)
    SetChrPos(0x15, 71500, 0, 0, 180)
    SetChrPos(0x17, 73950, 400, 800, 180)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    BeginChrThread(0x15, 0, 0, 0)
    BeginChrThread(0x16, 0, 0, 0)
    SetChrPos(0x0, 76660, 0, -1410, 135)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A1, 4)
    OP_29(0xAF, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_45_E9A2 end

    def Function_46_FA0E(): pass

    label("Function_46_FA0E")


    def lambda_FA13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FA13)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 73000, 0, -500, 2000, 0x0)
    Return()

    # Function_46_FA0E end

    def Function_47_FA57(): pass

    label("Function_47_FA57")


    def lambda_FA5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FA5C)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -1000, 2000, 0x0)
    OP_95(0xFE, 73750, 0, -1000, 2000, 0x0)
    Return()

    # Function_47_FA57 end

    def Function_48_FAA0(): pass

    label("Function_48_FAA0")


    def lambda_FAA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FAA5)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 75000, 0, -500, 2000, 0x0)
    Return()

    # Function_48_FAA0 end

    def Function_49_FAE9(): pass

    label("Function_49_FAE9")


    def lambda_FAEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FAEE)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
    OP_95(0xFE, 74250, 0, 0, 2000, 0x0)
    Return()

    # Function_49_FAE9 end

    SaveToFile()

Try(main)
