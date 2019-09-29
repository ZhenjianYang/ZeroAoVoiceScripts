from ScenarioHelper import *

def main():
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
        "雷欧鲁老人",             # 1
        "杰克",                   # 2
        "格方",                   # 3
        "席莉",                   # 4
        "奇斯",                   # 5
        "阿尔弗雷德",             # 6
        "阿蕾莎",                 # 7
        "卡米尤",                 # 8
        "普莉",                   # 9
        "史蒂芬",                 # 10
        "迪利克",                 # 11
        "安洁",                   # 12
        "哈缇娜修女",             # 13
        "哈罗德",                 # 14
        "索菲亚",                 # 15
        "柯林",                   # 16
        "凯文神父",               # 17
        "莉丝修女",               # 18
        "游击士林",               # 19
        "游击士艾欧莉娅",         # 20
        "游击士斯克特",           # 21
        "琪露露",                 # 22
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
        "Function_8_D32",          # 08, 8
        "Function_9_1AD1",         # 09, 9
        "Function_10_1AD5",        # 0A, 10
        "Function_11_26F0",        # 0B, 11
        "Function_12_26F4",        # 0C, 12
        "Function_13_3696",        # 0D, 13
        "Function_14_417C",        # 0E, 14
        "Function_15_428A",        # 0F, 15
        "Function_16_4D38",        # 10, 16
        "Function_17_5C8B",        # 11, 17
        "Function_18_651F",        # 12, 18
        "Function_19_659B",        # 13, 19
        "Function_20_65E5",        # 14, 20
        "Function_21_67DA",        # 15, 21
        "Function_22_6C6E",        # 16, 22
        "Function_23_6CF1",        # 17, 23
        "Function_24_6DCD",        # 18, 24
        "Function_25_6EBF",        # 19, 25
        "Function_26_798C",        # 1A, 26
        "Function_27_7AEB",        # 1B, 27
        "Function_28_7B25",        # 1C, 28
        "Function_29_7B5F",        # 1D, 29
        "Function_30_7D39",        # 1E, 30
        "Function_31_80CD",        # 1F, 31
        "Function_32_8540",        # 20, 32
        "Function_33_86A4",        # 21, 33
        "Function_34_882F",        # 22, 34
        "Function_35_88D8",        # 23, 35
        "Function_36_9646",        # 24, 36
        "Function_37_9752",        # 25, 37
        "Function_38_98FA",        # 26, 38
        "Function_39_A5E2",        # 27, 39
        "Function_40_A920",        # 28, 40
        "Function_41_B404",        # 29, 41
        "Function_42_B83C",        # 2A, 42
        "Function_43_BBC3",        # 2B, 43
        "Function_44_C053",        # 2C, 44
        "Function_45_C9AE",        # 2D, 45
        "Function_46_D85E",        # 2E, 46
        "Function_47_D8A7",        # 2F, 47
        "Function_48_D8F0",        # 30, 48
        "Function_49_D939",        # 31, 49
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
            "放置着车杂志《导力车狂热爱好者vol.2》。\x07\x00\x02",
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
            "导力车喷漆式样\x01\x07\x02",

            "『轻快色彩』\x07\x00",
            "已经记下来了。\x02",
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
            "★白蜡亭·推荐料理★\x01",
            "　 ～　大师蛋包饭　～\x02",
        )
    )

    CloseMessageWindow()

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "记载着大师蛋包饭的食谱。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_D2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『大师蛋包饭』\x07\x00",
            "的食谱已经记录下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D2E")

    TalkEnd(0xFF)
    Return()

    # Function_7_C50 end

    def Function_8_D32(): pass

    label("Function_8_D32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D61")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E63")

    #C0006
    ChrTalk(
        0x8,
        (
            "那棵来历不明的大树出现之后，\x01",
            "我本来还很担心杰克会不会\x01",
            "被吓得萎靡不振……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "但哈罗德先生只用了一句话，\x01",
            "就让他涌起了无穷干劲。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "对商人而言，最重要的品格就是坚毅……\x01",
            "这种品格已经在杰克的心中发芽了，\x01",
            "他今后也一定没问题的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF9")

    label("loc_E63")


    #C0009
    ChrTalk(
        0x8,
        (
            "对商人而言，最重要的品格就是坚毅……\x01",
            "这种品格已经在杰克的心中发芽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "无论克洛斯贝尔这次发展成什么状况，\x01",
            "我的心中也都没有需要挂怀的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF9")

    Jump("loc_1ACD")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB0")

    #C0011
    ChrTalk(
        0x8,
        (
            "哈罗德有索菲亚夫人\x01",
            "和柯林这两位家人\x01",
            "在背后支撑。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "嗯，要是杰克能找到个妻子，\x01",
            "说不定也会……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "等我退休之后，\x01",
            "或许应该专心帮\x01",
            "孙子找个老婆。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_101F")

    label("loc_FB0")


    #C0014
    ChrTalk(
        0x8,
        (
            "嗯……要是杰克也能有个\x01",
            "在生活和事业上支撑他的妻子，\x01",
            "说不定也会……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "或许我应该专心帮\x01",
            "孙子找个老婆呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101F")

    Jump("loc_1ACD")

    label("loc_1024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FC")

    #C0016
    ChrTalk(
        0x8,
        (
            "为了协商物资配发问题，\x01",
            "哈罗德先生与国防军\x01",
            "进行了多次交涉。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "虽说我们这个村子\x01",
            "基本可以做到自给自足，\x01",
            "但也同样需要常用药等必备品。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "要是杰克那小子也能像\x01",
            "哈罗德一样能干就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_117E")

    label("loc_10FC")


    #C0019
    ChrTalk(
        0x8,
        (
            "要是杰克那小子\x01",
            "能变成像哈罗德\x01",
            "一样出色的商人就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "……不好不好，那孩子\x01",
            "最近总算有了干劲，\x01",
            "我可不能动不动就发牢骚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117E")

    Jump("loc_1ACD")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125A")

    #C0021
    ChrTalk(
        0x8,
        (
            "杰克从前一段时间开始\x01",
            "突然充满干劲，\x01",
            "简直就像变了个人一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "虽然他还是不太成熟，\x01",
            "但我总算可以\x01",
            "放下心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "我还要继续教导他，\x01",
            "争取让他早日将杂货店的\x01",
            "招牌更换成『杰克杂货店』。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D2")

    label("loc_125A")


    #C0024
    ChrTalk(
        0x8,
        (
            "杰克总算拿出\x01",
            "干劲了，\x01",
            "我也可以放下心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "我还要继续教导他，\x01",
            "争取让他早日将杂货店的\x01",
            "招牌更换成『杰克杂货店』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D2")

    Jump("loc_1ACD")

    label("loc_12D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1387")

    #C0026
    ChrTalk(
        0x8,
        (
            "我的腰从昨天疼到现在了，\x01",
            "还是不见好。\x01",
            "看来是上了年纪啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "话说回来，\x01",
            "杰克那小子……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "今天的样子好像\x01",
            "和平常不太一样，\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13D1")

    label("loc_1387")


    #C0029
    ChrTalk(
        0x8,
        (
            "杰克那小子……\x01",
            "今天的样子好像\x01",
            "和平常不太一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_13D1")

    Jump("loc_1ACD")

    label("loc_13D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_156F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145D")

    #C0031
    ChrTalk(
        0x8,
        (
            "听说敏涅斯先生\x01",
            "今天要过来\x01",
            "进行最后的商谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "迪利克和他的计划\x01",
            "终于要开始实施了啊。\x01",
            "呵呵，真期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156A")

    label("loc_145D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FE")

    #C0033
    ChrTalk(
        0x8,
        (
            "我无意中打开窗户一看，\x01",
            "发现广场上竟然有魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "而且好像是\x01",
            "敏涅斯先生\x01",
            "驯养的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "我当时大吃一惊，\x01",
            "结果把腰给扭伤了。\x01",
            "疼死了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_156A")

    label("loc_14FE")


    #C0036
    ChrTalk(
        0x8,
        (
            "出现在广场的那些魔兽\x01",
            "好像是敏涅斯先生\x01",
            "驯养的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "我当时大吃一惊，\x01",
            "结果把腰给扭伤了。\x01",
            "疼死了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156A")

    Jump("loc_1ACD")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E1")

    #C0038
    ChrTalk(
        0x8,
        (
            "继哈罗德先生之后，最近我又\x01",
            "结识了一位精干的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "呵呵，真是受到他\x01",
            "不少关照呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1642")

    label("loc_15E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F0")
    Jump("loc_1642")

    label("loc_15F0")


    #C0040
    ChrTalk(
        0x8,
        (
            "那个男人\x01",
            "非常中意\x01",
            "村里出产的蜂蜜。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "嗯嗯，他一定\x01",
            "是个很有名望\x01",
            "的商人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1642")

    Jump("loc_1ACD")

    label("loc_1647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1704")

    #C0042
    ChrTalk(
        0x8,
        (
            "我差不多也该退休了，\x01",
            "想把这家店交给杰克来经营……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "但那小子好像\x01",
            "不是很有干劲呢，\x01",
            "总是在工作时偷懒发呆。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "唔，要是有什么契机\x01",
            "能让他发生改变就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1762")

    label("loc_1704")


    #C0045
    ChrTalk(
        0x8,
        (
            "杰克那小子\x01",
            "到底有没有继承\x01",
            "商店的打算呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "要是有什么\x01",
            "能让他拿出干劲\x01",
            "的契机就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1762")

    Jump("loc_1ACD")

    label("loc_1767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1876")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")

    #C0047
    ChrTalk(
        0x8,
        (
            "我的腰最近一直不太好，\x01",
            "看来真是上了年纪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "真想尽早退休，\x01",
            "把店交给杰克\x01",
            "来管理……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "怎么才能让我这孙子\x01",
            "拿出干劲呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1871")

    label("loc_1804")


    #C0050
    ChrTalk(
        0x8,
        (
            "我已经上了年纪，\x01",
            "想退休回家，把这家店\x01",
            "交给杰克来经营……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "但他本人却没什么干劲。\x01",
            "这真是前途多难啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1871")

    Jump("loc_1ACD")

    label("loc_1876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_19FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196B")

    #C0052
    ChrTalk(
        0x8,
        (
            "相貌威严的红发男人……\x01",
            "哦哦！最近确实有个那样\x01",
            "的男人和同伴一起来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "看起来似乎是一些危险的家伙，\x01",
            "不过在我们这里买了很多东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "杰克那小子当时很害怕，\x01",
            "但那些人真是难得一见的好客人。\x01",
            "呵呵呵……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F7")

    label("loc_196B")


    #C0055
    ChrTalk(
        0x8,
        (
            "那个相貌威严的红发男人\x01",
            "真是个好客人啊。\x01",
            "呵呵呵……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "杰克那小子当时很害怕，\x01",
            "但从外表来判断客人是不对的。\x01",
            "那小子该学的东西还多着呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F7")

    Jump("loc_1ACD")

    label("loc_19FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A85")

    #C0057
    ChrTalk(
        0x8,
        (
            "刚才哈罗德来我们这里\x01",
            "做了交易。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "哎呀呀，他真是一位\x01",
            "很有前途的商人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "真希望杰克那小子\x01",
            "能好好学学人家。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ACD")

    label("loc_1A85")


    #C0060
    ChrTalk(
        0x8,
        (
            "哈罗德是个\x01",
            "很有前途的商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "真希望杰克那小子\x01",
            "能好好学学人家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACD")

    TalkEnd(0xFE)
    Return()

    # Function_8_D32 end

    def Function_9_1AD1(): pass

    label("Function_9_1AD1")

    Call(0, 10)
    Return()

    # Function_9_1AD1 end

    def Function_10_1AD5(): pass

    label("Function_10_1AD5")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26EC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B32")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1B32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1B51")
    OP_AF(0x4F)
    Jump("loc_1B83")

    label("loc_1B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B61")
    OP_AF(0x4E)
    Jump("loc_1B83")

    label("loc_1B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B71")
    OP_AF(0x4D)
    Jump("loc_1B83")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B81")
    OP_AF(0x4C)
    Jump("loc_1B83")

    label("loc_1B81")

    OP_AF(0x4B)

    label("loc_1B83")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26E7")

    label("loc_1B92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA6")
    Jump("loc_26E7")

    label("loc_1BA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBE")
    TalkEnd(0x9)
    Return()

    label("loc_1BBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA5")

    #C0062
    ChrTalk(
        0x9,
        (
            "哈罗德先生在回去之前，\x01",
            "给了我这样一句忠告——\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "『越是在这种时候，\x01",
            "  才更要为了大家而努力经商，\x01",
            "  这是我们的使命』。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "既然我的工作可以\x01",
            "帮助他人，\x01",
            "那就必须要拼命努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CF1")

    label("loc_1CA5")


    #C0065
    ChrTalk(
        0x9,
        (
            "既然我的工作可以\x01",
            "帮助他人，\x01",
            "那就必须要拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "好……加油吧！！\x02",
    )

    CloseMessageWindow()

    label("loc_1CF1")

    Jump("loc_26E7")

    label("loc_1CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D70")

    #C0067
    ChrTalk(
        0x9,
        (
            "爷、爷爷好像在思考一些\x01",
            "很令人不安的事情呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "在这种时期，还是多担心担心\x01",
            "农作物收成降低的问题吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E7")

    label("loc_1D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E52")

    #C0069
    ChrTalk(
        0x9,
        (
            "不久前，我看到了\x01",
            "哈罗德先生与国防军交涉，\x01",
            "发现自己该学的东西还有很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "如果以后想继承商店，\x01",
            "就必须继续提高，让自己\x01",
            "也能顺利处理那样的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "机会难得，不如去听听\x01",
            "哈罗德先生的建议吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EBA")

    label("loc_1E52")


    #C0072
    ChrTalk(
        0x9,
        (
            "我只要看到爷爷的脸，\x01",
            "就基本明白他想说什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "我必须要成为一名\x01",
            "像哈罗德先生那样出色的商人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBA")

    Jump("loc_26E7")

    label("loc_1EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F30")

    #C0074
    ChrTalk(
        0x9,
        (
            "欢迎，欢迎光临\x01",
            "『雷欧鲁杂货店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "向您推荐我们的特产蜂蜜哦，\x01",
            "请一定要看看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F86")

    label("loc_1F30")


    #C0076
    ChrTalk(
        0x9,
        (
            "……怎么样？招呼得\x01",
            "像模像样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "嘿嘿，不然就好好考虑一下\x01",
            "继承商店的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F86")

    Jump("loc_26E7")

    label("loc_1F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2046")

    #C0078
    ChrTalk(
        0x9,
        (
            "爷爷昨天\x01",
            "把腰扭了。\x01",
            "今天何不休息一下呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "多半还是因为我太靠不住，\x01",
            "爷爷才不敢让我一人看店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "……唉，我到底在做什么啊。\x01",
            "必须要更加努力才行……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20B5")

    label("loc_2046")


    #C0081
    ChrTalk(
        0x9,
        (
            "我并不是很想继承\x01",
            "这家杂货店，\x01",
            "所以没什么干劲……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "但为了不让爷爷担心，\x01",
            "我是不是应该试着多努力一下呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B5")

    Jump("loc_26E7")

    label("loc_20BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2155")

    #C0083
    ChrTalk(
        0x9,
        (
            "听说阿尔摩利卡村\x01",
            "好像要改革……\x01",
            "到底要怎么改呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "就算一直维持现状，\x01",
            "我也不觉得有什么不好。\x01",
            "只要能过得轻松自在就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AE")

    label("loc_2155")


    #C0085
    ChrTalk(
        0x9,
        (
            "爷爷刚才\x01",
            "把腰扭了，\x01",
            "不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "啊，对了，我得去里面\x01",
            "找条热毛巾给爷爷敷上……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AE")

    Jump("loc_26E7")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_22CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2272")

    #C0087
    ChrTalk(
        0x9,
        (
            "最近总能在村里看到\x01",
            "一位打扮得很讲究的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "那个人对爷爷说\x01",
            "『您有个很能干的好孙子』，\x01",
            "爷爷听了之后好像很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……但我认为那只是\x01",
            "普通的客套话而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22C9")

    label("loc_2272")


    #C0090
    ChrTalk(
        0x9,
        (
            "爷爷听到别人\x01",
            "夸赞我的时候\x01",
            "好像很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "……但我认为那只是\x01",
            "普通的客套话而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C9")

    Jump("loc_26E7")

    label("loc_22CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_237D")

    #C0092
    ChrTalk(
        0x9,
        (
            "看来我必须得早点\x01",
            "和爷爷说清楚，\x01",
            "让他明白我并不想继承店铺。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "不过，如果那样说的话，\x01",
            "爷爷肯定会很失望吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "……算了，\x01",
            "暂时就先这样吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23E4")

    label("loc_237D")


    #C0095
    ChrTalk(
        0x9,
        (
            "又有薪水，又不太忙……\x01",
            "如果把这当作打工，\x01",
            "倒也是一份不错的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "……算了，\x01",
            "暂时就先这样吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E4")

    Jump("loc_26E7")

    label("loc_23E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_249D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245D")

    #C0097
    ChrTalk(
        0x9,
        (
            "爷爷想让我\x01",
            "继承杂货店……\x01",
            "但老实说，这实在太麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "我将来想去市里\x01",
            "大赚一笔。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2498")

    label("loc_245D")


    #C0099
    ChrTalk(
        0x9,
        "实在是没兴趣继承店铺。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "我将来想去市里\x01",
            "大赚一笔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2498")

    Jump("loc_26E7")

    label("loc_249D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_26E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_25DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2568")

    #C0101
    ChrTalk(
        0x9,
        (
            "红发壮汉……？\x01",
            "说起来，不久前确实有个\x01",
            "那样的男人来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "他买了很多东西，\x01",
            "爷爷很高兴……\x01",
            "但我当时真是怕得要死。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "那些家伙绝不是普通人，\x01",
            "肯定有什么企图……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25D9")

    label("loc_2568")


    #C0104
    ChrTalk(
        0x9,
        (
            "那个红发壮汉……\x01",
            "绝对不是普通人，\x01",
            "当时真是吓死我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "……不过，和他一起来的那个\x01",
            "红发女孩倒是挺可爱的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D9")

    Jump("loc_26E7")

    label("loc_25DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2685")

    #C0106
    ChrTalk(
        0x9,
        (
            "欢迎光临，\x01",
            "随……请您随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "我们这里出售村中的特产蜂蜜，\x01",
            "你就……建议您选购。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "……呼，必须要使用这种正式敬语，\x01",
            "实在是很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26E7")

    label("loc_2685")


    #C0109
    ChrTalk(
        0x9,
        (
            "爷爷非要让我\x01",
            "向哈罗德先生学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "竟然要我和那种经验老道的商人\x01",
            "比拼，这担子未免也太重了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E7")

    Jump("loc_1AE2")

    label("loc_26EC")

    TalkEnd(0x9)
    Return()

    # Function_10_1AD5 end

    def Function_11_26F0(): pass

    label("Function_11_26F0")

    Call(0, 12)
    Return()

    # Function_11_26F0 end

    def Function_12_26F4(): pass

    label("Function_12_26F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_273D")
    Call(0, 40)
    Return()

    label("loc_273D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_276B")
    Call(0, 41)
    Return()

    label("loc_276B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2799")
    Call(0, 43)
    Return()

    label("loc_2799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27B0")
    Call(0, 44)
    Return()

    label("loc_27B0")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3692")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_281C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_281C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283C")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_368D")

    label("loc_283C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285C")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_368D")

    label("loc_285C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2870")
    Jump("loc_368D")

    label("loc_2870")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2888")
    TalkEnd(0xA)
    Return()

    label("loc_2888")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_291A")

    #C0111
    ChrTalk(
        0xA,
        (
            "受到如此夸奖，\x01",
            "还真有点不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "哈哈，请一定要写出\x01",
            "一篇精彩的报道，\x01",
            "让我们的生意更加兴隆哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368D")

    label("loc_291A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F9")

    #C0113
    ChrTalk(
        0xA,
        (
            "那棵蓝白色巨树的出现\x01",
            "真是让我大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "如今的状况非常严峻……\x01",
            "但正是在这种时期，\x01",
            "才更要注意休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "刚才有位筋疲力竭的神父\x01",
            "在修女的陪同下\x01",
            "上楼休息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "稍后给他们送杯\x01",
            "咖啡好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A50")

    label("loc_29F9")


    #C0117
    ChrTalk(
        0xA,
        (
            "刚才有位筋疲力竭的神父\x01",
            "在修女的陪同下\x01",
            "上楼休息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "稍后给他们送杯\x01",
            "咖啡好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A50")

    Jump("loc_368D")

    label("loc_2A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B36")

    #C0119
    ChrTalk(
        0xA,
        (
            "有关无效宣言的传闻\x01",
            "已经传到这个村子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "这个村子的人原本就对\x01",
            "总统没什么好印象……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "如今说不定连市里的居民\x01",
            "也开始对他抱有怀疑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "今后的情况将会如何发展呢……\x01",
            "我个人是十分关注啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BA2")

    label("loc_2B36")


    #C0123
    ChrTalk(
        0xA,
        (
            "如今说不定连市里的居民\x01",
            "也开始对总统抱有怀疑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "今后的情况将会如何发展呢……\x01",
            "我个人是十分关注啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA2")

    Jump("loc_368D")

    label("loc_2BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C97")

    #C0125
    ChrTalk(
        0xA,
        (
            "哈罗德先生和他的家人\x01",
            "暂住在二层的大房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔已经陷入如此状况，\x01",
            "大概也不会有新客人来了。\x01",
            "在困难时期，就要互相帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "哈罗德先生给我们村子帮了很多忙，\x01",
            "借房间给他们住是应该的，\x01",
            "算不上什么大事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D3B")

    label("loc_2C97")


    #C0128
    ChrTalk(
        0xA,
        (
            "话说回来，哈罗德先生难得\x01",
            "有个假期，结果却遇到这种事，\x01",
            "运气还真是差啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "对村子来说，哈罗德先生的到来自然是大有帮助……\x01",
            "但现在无法回市里，\x01",
            "他肯定很不安吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3B")

    Jump("loc_368D")

    label("loc_2D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2ED9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DDE")

    #C0130
    ChrTalk(
        0xA,
        (
            "我本来以为盖巴尔先生是因为\x01",
            "喜欢本店的料理，\x01",
            "所以才会特意从市内跑到村子……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        "……他现在住在什么地方呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED4")

    label("loc_2DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E84")

    #C0132
    ChrTalk(
        0xA,
        (
            "之前那起袭击事件\x01",
            "可是足以动摇整个自治州的\x01",
            "和平局势的严重问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "据说边境地区的状态\x01",
            "比以往更加紧张了……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔今后\x01",
            "究竟会如何呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2ED4")

    label("loc_2E84")


    #C0135
    ChrTalk(
        0xA,
        (
            "据说边境地区的状态\x01",
            "比以往更加紧张了……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔今后\x01",
            "究竟会如何呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED4")

    Jump("loc_368D")

    label("loc_2ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F72")

    #C0137
    ChrTalk(
        0xA,
        (
            "为了今天的主日学校课程，\x01",
            "我们借出了二层的大房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "好，做些布丁\x01",
            "给孩子们\x01",
            "吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "哦，当然也会准备\x01",
            "修女的那一份。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FBD")

    label("loc_2F72")


    #C0140
    ChrTalk(
        0xA,
        (
            "二层的大房间今天借给\x01",
            "主日学校当课堂了。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "给大家\x01",
            "做些布丁\x01",
            "吃好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBD")

    Jump("loc_368D")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_318A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3060")

    #C0142
    ChrTalk(
        0xA,
        (
            "我向迪利克打听了一下\x01",
            "他离开家的缘由，\x01",
            "还有他最近正在做的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "话说回来，这样做真的没问题吗？\x01",
            "突然说要开拓什么新事业……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3185")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3116")

    #C0144
    ChrTalk(
        0xA,
        (
            "没想到敏涅斯先生\x01",
            "竟然是诈骗犯……\x01",
            "我完全没有察觉到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "看来他是个\x01",
            "专业的大骗子啊。\x01",
            "真是个可怕的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "听说已经指名通缉他了，\x01",
            "希望能尽早\x01",
            "抓到人啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3185")

    label("loc_3116")


    #C0147
    ChrTalk(
        0xA,
        (
            "不管怎么说，迪利克能与\x01",
            "村长和解，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "从某种意义上说，\x01",
            "这起事件到也算是\x01",
            "让他们和好的契机呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3185")

    Jump("loc_368D")

    label("loc_318A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31EB")

    #C0149
    ChrTalk(
        0xA,
        (
            "呼，迪利克\x01",
            "什么时候才\x01",
            "愿意回家呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "希望他和村长\x01",
            "能尽早和好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3259")

    label("loc_31EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FA")
    Jump("loc_3259")

    label("loc_31FA")


    #C0151
    ChrTalk(
        0xA,
        (
            "我和敏涅斯先生\x01",
            "并没有什么接触。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "迪利克最近倒是经常和他\x01",
            "凑在一起……\x01",
            "究竟在谈什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3321")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3321")

    #C0153
    ChrTalk(
        0x101,
        (
            "#00003F（说起来，\x01",
            "  在这里似乎可以进行\x01",
            "  美食向导的取材……）\x02\x03",

            "#00001F（但现在不是做这种事的时候，\x01",
            "  以后别忘了再过来一趟。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3321")

    Jump("loc_368D")

    label("loc_3326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3441")
    SetChrSubChip(0x12, 0x1)
    TurnDirection(0xA, 0x12, 0)

    #C0154
    ChrTalk(
        0xA,
        (
            "迪利克……\x01",
            "村长他并不是\x01",
            "不问情由地否定你……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x12,
        (
            "不，父亲他一定是……\x01",
            "根本就不赞同\x01",
            "改革这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x12,
        (
            "否则的话，\x01",
            "面对村子如今的状况，\x01",
            "他没理由漠不关心……！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        (
            "……我知道你有很多难处。\x01",
            "不过偶尔也应该喝杯咖啡，\x01",
            "冷静一下头脑哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    TurnDirection(0xA, 0x0, 0)
    SetChrSubChip(0x12, 0x0)
    Jump("loc_34B5")

    label("loc_3441")


    #C0158
    ChrTalk(
        0xA,
        (
            "迪利克和村长很像，\x01",
            "责任感太强了。\x01",
            "总会考虑各种烦心的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "他难得来这里坐坐，\x01",
            "不然就赠送他\x01",
            "一杯咖啡好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B5")

    Jump("loc_368D")

    label("loc_34BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3601")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3592")

    #C0160
    ChrTalk(
        0xA,
        (
            "各国首脑齐聚\x01",
            "克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "对克洛斯贝尔来说，\x01",
            "这可是史无前例的重大活动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "听说发起提议的人\x01",
            "是克洛斯贝尔市的新市长……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "哎呀呀，真不愧是\x01",
            "ＩＢＣ的首脑，\x01",
            "想法果然大胆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35FC")

    label("loc_3592")


    #C0164
    ChrTalk(
        0xA,
        (
            "西塞姆里亚通商会议……\x01",
            "终于要开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "据说周边诸国都很关心此次会议，\x01",
            "我也非常关注会议的动向。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FC")

    Jump("loc_368D")

    label("loc_3601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_368D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3619")
    Jump("loc_368D")

    label("loc_3619")


    #C0166
    ChrTalk(
        0xA,
        (
            "红发壮汉和他的同伴\x01",
            "并没在村里做什么\x01",
            "奇怪的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "看起来，好像是一群\x01",
            "很强悍的人……\x01",
            "他们究竟是什么身份呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368D")

    Jump("loc_27BD")

    label("loc_3692")

    TalkEnd(0xA)
    Return()

    # Function_12_26F4 end

    def Function_13_3696(): pass

    label("Function_13_3696")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3740")

    #C0168
    ChrTalk(
        0xB,
        (
            "我以前没怎么关注过\x01",
            "奇斯……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "呵呵，没想到他\x01",
            "很有男子气概嘛，\x01",
            "真要刮目相看了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "刚才没忍住，还是笑了出来，\x01",
            "稍后可要去向他道歉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37A5")

    label("loc_3740")


    #C0171
    ChrTalk(
        0xB,
        (
            "奇斯很有\x01",
            "男子气概嘛，\x01",
            "真要对他刮目相看了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        (
            "刚才没忍住，还是笑了出来，\x01",
            "稍后可要去向他道歉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A5")

    Jump("loc_4178")

    label("loc_37AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_38BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384B")

    #C0173
    ChrTalk(
        0xB,
        (
            "索菲亚夫人\x01",
            "非常擅长烹饪呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "趁着她暂住在这里，\x01",
            "我去向她学习学习好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "呵呵，以后说不定能\x01",
            "做出超越爸爸的\x01",
            "美味蛋包饭呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38B8")

    label("loc_384B")


    #C0176
    ChrTalk(
        0xB,
        (
            "趁着索菲亚夫人暂住在这里，\x01",
            "我去向她学习烹饪好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "呵呵，以后说不定能\x01",
            "做出超越爸爸的\x01",
            "美味蛋包饭呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B8")

    Jump("loc_4178")

    label("loc_38BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_39C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3960")

    #C0178
    ChrTalk(
        0xB,
        (
            "啊～柯林真是\x01",
            "很可爱呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "一双大眼睛闪闪发亮，\x01",
            "而且完全不认生……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "不愧是我崇敬的\x01",
            "哈罗德先生的孩子，\x01",
            "真期待他将来的表现！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39BB")

    label("loc_3960")


    #C0181
    ChrTalk(
        0xB,
        (
            "啊～柯林真是\x01",
            "很可爱呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "不愧是我崇敬的\x01",
            "哈罗德先生的孩子，\x01",
            "真期待他将来的表现！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BB")

    Jump("loc_4178")

    label("loc_39C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3B05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A83")

    #C0183
    ChrTalk(
        0xB,
        (
            "在纪念庆典的时候，\x01",
            "我曾去过克洛斯贝尔市……\x01",
            "那真是一座美丽的城市啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xB,
        (
            "竟然袭击那样的地方，\x01",
            "武装集团实在是让人无法原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "希望警察和警备队员\x01",
            "把他们都逮捕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B00")

    label("loc_3A83")


    #C0186
    ChrTalk(
        0xB,
        (
            "竟然袭击克洛斯贝尔市，\x01",
            "武装集团实在是让人无法原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        (
            "之前那个叫敏涅斯的人也是一样，\x01",
            "世上为什么会有\x01",
            "这么多坏人呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B00")

    Jump("loc_4178")

    label("loc_3B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B97")

    #C0188
    ChrTalk(
        0xB,
        (
            "唉，在下雨天，到处都\x01",
            "湿漉漉的，真是讨厌。\x01",
            "清扫地板也很麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xB,
        (
            "真希望客人先在门口的\x01",
            "垫子上把鞋底的泥\x01",
            "擦一擦，然后再进店。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4178")

    label("loc_3B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C19")

    #C0190
    ChrTalk(
        0xB,
        (
            "敏涅斯先生今天好像\x01",
            "要来和迪利克先生\x01",
            "商讨一件重要的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "他们的计划终于要\x01",
            "进入最终阶段了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D13")

    label("loc_3C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB4")

    #C0192
    ChrTalk(
        0xB,
        (
            "那个叫敏涅斯的家伙……\x01",
            "真是个彻头彻尾的大骗子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "哼，我从一开始\x01",
            "就觉得他很可疑。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "要是他敢再来，\x01",
            "我一定会狠狠修理他一顿。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D13")

    label("loc_3CB4")


    #C0195
    ChrTalk(
        0xB,
        (
            "我从一开始就觉得\x01",
            "那个叫敏涅斯的家伙\x01",
            "很可疑。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "要是他敢再来，\x01",
            "我一定会狠狠修理他一顿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D13")

    Jump("loc_4178")

    label("loc_3D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC9")

    #C0197
    ChrTalk(
        0xB,
        (
            "最近，有一位\x01",
            "非常温和的叔叔时常过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "听说他在外国一家\x01",
            "很有名的公司任职，\x01",
            "但他却完全没有架子。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "嗯，看来世上的确存在着\x01",
            "不少优秀的人呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E40")

    label("loc_3DC9")


    #C0200
    ChrTalk(
        0xB,
        (
            "最近，有一位\x01",
            "非常温和的叔叔时常过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "他在外国一家很有名的公司任职，\x01",
            "但却完全没有架子……\x01",
            "真是位优秀的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E40")

    Jump("loc_4178")

    label("loc_3E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E60")
    Call(0, 14)
    Jump("loc_3EE5")

    label("loc_3E60")


    #C0202
    ChrTalk(
        0xB,
        (
            "其实我很想去看看那个兰花塔，\x01",
            "不过店里还有工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "如果他能在一小时之内把\x01",
            "我们店里的十盘蛋包饭全部吃光，\x01",
            "我就答应和他约会☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE5")

    Jump("loc_4178")

    label("loc_3EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_407C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FAB")

    #C0204
    ChrTalk(
        0xB,
        (
            "游击士果然\x01",
            "很强啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "虽然最出名的只有\x01",
            "亚里欧斯先生，\x01",
            "但那两位女游击士也相当厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        (
            "呵呵，当然，你们也很不错哦。\x01",
            "多亏你们，让我看得很开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_402C")

    label("loc_3FAB")


    #C0207
    ChrTalk(
        0xB,
        (
            "虽然最出名的只有\x01",
            "亚里欧斯先生，\x01",
            "但那两位女游击士也相当厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "呵呵，当然，你们也很不错哦。\x01",
            "多亏你们，让我看得很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402C")

    Jump("loc_4077")

    label("loc_4031")


    #C0209
    ChrTalk(
        0xB,
        (
            "游击士来帮我们\x01",
            "驱赶魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "呵呵，一定要好好\x01",
            "招待她们一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4077")

    Jump("loc_4178")

    label("loc_407C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4123")

    #C0211
    ChrTalk(
        0xB,
        (
            "欢迎光临～\x01",
            "请随意就坐～\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "说到我们店的推荐料理，\x01",
            "自然还是蛋包饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "经过最近的改良，\x01",
            "比以前更加美味了。\x01",
            "如果愿意，还请尝尝看哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4178")

    label("loc_4123")


    #C0214
    ChrTalk(
        0xB,
        (
            "哈罗德先生\x01",
            "今天住在二层的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        (
            "商谈好像已经结束了，\x01",
            "我去给他送杯\x01",
            "咖啡吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4178")

    TalkEnd(0xFE)
    Return()

    # Function_13_3696 end

    def Function_14_417C(): pass

    label("Function_14_417C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0216
    ChrTalk(
        0xC,
        (
            "席莉小姐，\x01",
            "下次和我一起去市里逛逛如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xC,
        (
            "去看看那座传闻中的\x01",
            "兰花塔吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "唔……\x01",
            "可是店里还有工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "……对了☆\x01",
            "如果你能在一小时之内把我们店里的十盘\x01",
            "蛋包饭全部吃光，我就和你一起去。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "这、这个……\x01",
            "实在太强人所难了吧……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_417C end

    def Function_15_428A(): pass

    label("Function_15_428A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_438D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433F")

    #C0221
    ChrTalk(
        0xC,
        (
            "老实说，我并不了解\x01",
            "如今的状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        (
            "但无论发生什么，\x01",
            "我也一定会保护好席莉小姐的。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xC,
        (
            "……我当面对她说了这样的话，\x01",
            "结果却遭到嘲笑了……哈哈。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4388")

    label("loc_433F")


    #C0224
    ChrTalk(
        0xC,
        (
            "虽然被席莉\x01",
            "嘲笑了……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "但无论发生什么，\x01",
            "我也一定会\x01",
            "保护好她的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4388")

    Jump("loc_4D34")

    label("loc_438D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_44BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444B")

    #C0226
    ChrTalk(
        0xC,
        (
            "一定不要说出去哦，其实席莉小姐\x01",
            "的烹饪水平……相当那个。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "当她把烧成黑炭般的\x01",
            "蛋包饭端到我面前时，\x01",
            "真是连我都吓得发抖。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        "……呼，但最后还是拼命吃光了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_44B9")

    label("loc_444B")


    #C0229
    ChrTalk(
        0xC,
        (
            "一定不要说出去哦，其实席莉小姐\x01",
            "的烹饪水平……相当那个。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        (
            "……但无论她端出什么来，\x01",
            "我都会拼命吃光的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B9")

    Jump("loc_4D34")

    label("loc_44BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_45D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_456D")

    #C0231
    ChrTalk(
        0xC,
        (
            "国防军的那些家伙\x01",
            "真让人厌恶。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "只不过是顺路来趟村子而已，\x01",
            "却偏要摆出一副保卫\x01",
            "我们的嘴脸。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        (
            "从警备队变成了国防军，\x01",
            "就开始得意忘形了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45CB")

    label("loc_456D")


    #C0234
    ChrTalk(
        0xC,
        (
            "不知为何，看到国防军\x01",
            "的那些家伙就生气。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        (
            "从警备队变成了国防军，\x01",
            "就开始得意忘形了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CB")

    Jump("loc_4D34")

    label("loc_45D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469C")

    #C0236
    ChrTalk(
        0xC,
        (
            "据说之前那起袭击事件的主犯\x01",
            "很可能还潜伏在\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        (
            "警备队最近巡逻得更加频繁了，\x01",
            "或许就是因为这个理由吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "总觉得克洛斯贝尔\x01",
            "渐渐变成了一个\x01",
            "很危险的地方呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_470F")

    label("loc_469C")


    #C0239
    ChrTalk(
        0xC,
        (
            "据说之前那起袭击事件的主犯\x01",
            "很可能还潜伏在\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        (
            "总觉得克洛斯贝尔\x01",
            "渐渐变成了一个很危险的地方呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_470F")

    Jump("loc_4D34")

    label("loc_4714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C8")

    #C0241
    ChrTalk(
        0xC,
        (
            "啊，说起来，\x01",
            "那个居民投票活动\x01",
            "好像渐渐临近了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        (
            "去市里投票\x01",
            "实在是有点麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "但投票结果也关系到\x01",
            "我们这些村民的未来，\x01",
            "所以还是应该去的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_482C")

    label("loc_47C8")


    #C0244
    ChrTalk(
        0xC,
        (
            "调查是否赞成独立的\x01",
            "居民投票活动已经临近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "去市里投票实在是有点麻烦……\x01",
            "但还是应该去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_482C")

    Jump("loc_4D34")

    label("loc_4831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_49DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4906")

    #C0246
    ChrTalk(
        0xC,
        (
            "听说敏涅斯先生和迪利克\x01",
            "会在今天商讨出最后结果。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "为了庆祝阿尔摩利卡村的新生，\x01",
            "一定要痛痛快快地聚个餐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "嘿嘿，热热闹闹地摆上一大桌，\x01",
            "席莉小姐一定会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4983")

    label("loc_4906")


    #C0249
    ChrTalk(
        0xC,
        (
            "听说敏涅斯先生和迪利克\x01",
            "会在今天商讨出最后结果。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        (
            "我们一定要痛痛快快地聚个餐，\x01",
            "庆祝阿尔摩利卡村从此\x01",
            "走上了新的道路。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4983")

    Jump("loc_49DA")

    label("loc_4988")


    #C0251
    ChrTalk(
        0xC,
        (
            "敏涅斯先生的话……\x01",
            "难道全都是谎言吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "哎，迪利克那家伙\x01",
            "肯定很沮丧吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49DA")

    Jump("loc_4D34")

    label("loc_49DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6F")

    #C0253
    ChrTalk(
        0xC,
        (
            "那个外国大叔的\x01",
            "人生阅历好像很丰富。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xC,
        (
            "他看出我暗恋\x01",
            "席莉小姐，\x01",
            "还特意鼓励了我一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        "哎，真是个好人啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4AC5")

    label("loc_4A6F")


    #C0256
    ChrTalk(
        0xC,
        (
            "那个外国大叔\x01",
            "看出我暗恋席莉小姐，\x01",
            "还特意鼓励了我一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        "哎，真是个好人啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4AC5")

    Jump("loc_4D34")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AE5")
    Call(0, 14)
    Jump("loc_4B32")

    label("loc_4AE5")


    #C0258
    ChrTalk(
        0xC,
        (
            "呵呵呵……我好不容易\x01",
            "鼓起勇气邀请她，结果却……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xC,
        "席莉小姐真苛刻啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4B32")

    Jump("loc_4D34")

    label("loc_4B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD0")

    #C0260
    ChrTalk(
        0xC,
        (
            "我准备在近期\x01",
            "向席莉小姐提出\x01",
            "约会的请求。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "至今为止，我每天\x01",
            "都来店里用餐，\x01",
            "已经和她很亲近了……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        "她一定会答应的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C30")

    label("loc_4BD0")


    #C0263
    ChrTalk(
        0xC,
        (
            "我准备在近期向席莉小姐\x01",
            "提出约会的请求。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "好，今天做好心理准备……\x01",
            "明天一定要实行计划。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C30")

    Jump("loc_4D34")

    label("loc_4C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CC5")

    #C0265
    ChrTalk(
        0xC,
        (
            "我很喜欢这家店的\x01",
            "招牌女店员席莉小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "她那可爱的笑脸\x01",
            "真是让人无法抗拒啊！\x01",
            "我总是不知不觉地在这里坐上很久。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D34")

    label("loc_4CC5")


    #C0267
    ChrTalk(
        0xC,
        (
            "为了欣赏席莉小姐的笑脸，\x01",
            "无论添多少次咖啡，\x01",
            "我也会一直坐在这里不走。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "……呼，不过加咖啡\x01",
            "也不便宜呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D34")

    TalkEnd(0xFE)
    Return()

    # Function_15_428A end

    def Function_16_4D38(): pass

    label("Function_16_4D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D4F")
    Call(0, 44)
    Return()

    label("loc_4D4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E26")

    #C0269
    ChrTalk(
        0xD,
        (
            "『幻兽』还没有消失，\x01",
            "又出现了那棵来历不明的大树，\x01",
            "所以现在仍然不能出村……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "不过，已经回到市里的哈罗德\x01",
            "说要给我带些\x01",
            "我喜欢的书来。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        (
            "嗯，真不愧是哈罗德，\x01",
            "太期待他的归来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4EA6")

    label("loc_4E26")


    #C0272
    ChrTalk(
        0xD,
        (
            "哈罗德真是善解人意，\x01",
            "他一定会给我带来\x01",
            "我喜欢的书。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xD,
        (
            "……话说回来，现在的状况很严峻。\x01",
            "如果要前往郊外，\x01",
            "一定要万分小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA6")

    Jump("loc_5C87")

    label("loc_4EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4FD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F67")

    #C0274
    ChrTalk(
        0xD,
        (
            "由于现在禁止前往郊外，\x01",
            "连图书馆都不能去了，\x01",
            "真是头疼……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "不过麦克道尔议长\x01",
            "总算开始反击了。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "不知能否使情况有所好转，\x01",
            "让笼罩着城市的结界\x01",
            "尽快消失。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4FCE")

    label("loc_4F67")


    #C0277
    ChrTalk(
        0xD,
        (
            "不知能否让笼罩着城市的\x01",
            "结界尽快消失。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xD,
        (
            "要是能恢复以往的状况，\x01",
            "让我可以自由前往\x01",
            "图书馆就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FCE")

    Jump("loc_5C87")

    label("loc_4FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_512A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50AE")

    #C0279
    ChrTalk(
        0xD,
        (
            "受『幻兽』的影响，再加上禁止前往\x01",
            "郊外的限制，农业收成相当不如意。\x01",
            "本想找些新书看，从而转换心情……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xD,
        (
            "但现在也没办法去\x01",
            "克洛斯贝尔市的图书馆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xD,
        (
            "读书可以滋润生活，\x01",
            "你们也这么想吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5125")

    label("loc_50AE")


    #C0282
    ChrTalk(
        0xD,
        (
            "现在都没办法去\x01",
            "克洛斯贝尔市的图书馆了……\x01",
            "连新书都看不到。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xD,
        (
            "如果这样的生活要持续多年，\x01",
            "便只能称之为地狱了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5125")

    Jump("loc_5C87")

    label("loc_512A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5218")

    #C0284
    ChrTalk(
        0xD,
        (
            "不久前上市的那本\x01",
            "克洛斯贝尔时代周刊特别号，\x01",
            "我反复看了好多次。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xD,
        (
            "袭击事件自然令人在意，\x01",
            "但最让人震惊的还是\x01",
            "伊莉娅身负重伤的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "……身为克洛斯贝尔的居民，\x01",
            "现在要做的就是多多祈祷，希望她尽快康复。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_527C")

    label("loc_5218")


    #C0287
    ChrTalk(
        0xD,
        (
            "一直为克洛斯贝尔\x01",
            "带来活力的伊莉娅\x01",
            "竟然会有如此遭遇……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        "……我会多多祈祷，希望她尽快康复。\x02",
    )

    CloseMessageWindow()

    label("loc_527C")

    Jump("loc_5C87")

    label("loc_5281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533C")

    #C0289
    ChrTalk(
        0xD,
        (
            "击打在窗户上的雨滴声如此动听，\x01",
            "手边还摆放着热腾腾的咖啡……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xD,
        (
            "对我来说，下雨天\x01",
            "就是最好的读书日。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "难得的好日子，\x01",
            "把以前来不及看的书\x01",
            "一口气看完吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_53A6")

    label("loc_533C")


    #C0292
    ChrTalk(
        0xD,
        (
            "击打在窗户上的雨滴声如此动听，\x01",
            "手边还摆放着热腾腾的咖啡……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "对我来说，下雨天\x01",
            "就是最好的读书日。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A6")

    Jump("loc_5C87")

    label("loc_53AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5611")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5453")

    #C0294
    ChrTalk(
        0xD,
        (
            "随着时代的变迁，\x01",
            "这个村子需要面对的问题\x01",
            "不断增多。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        (
            "虽然村长坚持要\x01",
            "保留传统……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xD,
        (
            "但我很理解迪利克\x01",
            "盼望改革的想法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54B0")

    label("loc_5453")


    #C0297
    ChrTalk(
        0xD,
        (
            "随着时代的变迁，\x01",
            "这个村子需要面对的问题\x01",
            "不断增多。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xD,
        (
            "我很理解迪利克\x01",
            "盼望改革的想法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B0")

    Jump("loc_560C")

    label("loc_54B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5578")

    #C0299
    ChrTalk(
        0xD,
        (
            "那个叫敏涅斯的男人\x01",
            "博得了不少村民的信任呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "他似乎可以看穿他人心中的渴望……\x01",
            "那种洞察力\x01",
            "确实是真本事。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xD,
        (
            "难得的才能，却被他\x01",
            "利用在欺诈行为上，\x01",
            "真是个无可救药的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_560C")

    label("loc_5578")


    #C0302
    ChrTalk(
        0xD,
        (
            "那个叫敏涅斯的男人……\x01",
            "如果一开始没有染指什么欺诈行为的话，\x01",
            "说不定能取得很大成就呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        (
            "……呼，但听说他\x01",
            "还有很多前科，\x01",
            "并没有同情的余地呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_560C")

    Jump("loc_5C87")

    label("loc_5611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5758")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    #C0304
    ChrTalk(
        0xD,
        (
            "我从图书馆借了一本名为\x01",
            "《真实存在的克洛斯贝尔怪谈》的书。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xD,
        (
            "『寻找自己头颅的男子』这个故事……\x01",
            "唔唔，真是让人后背发冷啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        "嗯，确实很恐怖……\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xA,
        (
            "连头都不见了，\x01",
            "究竟是从哪里发出『快把我的头找回来』\x01",
            "这种呻吟声的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xD,
        (
            "……恐怖之处好像\x01",
            "并不在这里。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_57D9")

    label("loc_5758")


    #C0309
    ChrTalk(
        0xD,
        (
            "唉，好不容易沉浸到了\x01",
            "恐怖的感觉中，\x01",
            "被格方这么一说，气氛全没了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "必须要好好教教这家伙，\x01",
            "让他明白应该如何享受怪谈故事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57D9")

    Jump("loc_5C87")

    label("loc_57DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5AAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5900")

    #C0311
    ChrTalk(
        0xD,
        (
            "我之前去图书馆的时候，\x01",
            "顺便买了一本最近\x01",
            "很喜欢看的连载小说……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xD,
        (
            "不过好像买错了卷数，\x01",
            "中间漏掉了一本。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "我怕自己忍不住去看，\x01",
            "导致提前剧透……\x01",
            "不好意思，你们能把它拿去吗？\x02",
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
            "获得了。\x02",
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

    label("loc_5900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A52")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    #C0315
    ChrTalk(
        0xD,
        (
            "我今天从图书馆借来了\x01",
            "《改变大陆的美人们》……\x01",
            "这本书真是很有意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xA,
        (
            "以『女战士莉安娜』为代表，\x01",
            "书中介绍了数名在各国历史中\x01",
            "留下丰功伟业的女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xA,
        (
            "嗯……看来女性自古就是\x01",
            "很强大的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xA,
        (
            "我这家店也是一样，\x01",
            "主要都由我女儿来拿主意。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xD,
        (
            "（那只是因为你\x01",
            "  太靠不住而已……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_5AA6")

    label("loc_5A52")


    #C0320
    ChrTalk(
        0xD,
        (
            "《改变大陆的美人们》……\x01",
            "这本书真是很有意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xD,
        (
            "你们也去图书馆\x01",
            "看看如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AA6")

    Jump("loc_5C87")

    label("loc_5AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9C")

    #C0322
    ChrTalk(
        0xD,
        (
            "我很喜欢读书。\x01",
            "今早本打算\x01",
            "去市里的图书馆……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xD,
        (
            "但由于各国首脑要进入克洛斯贝尔，\x01",
            "之前已经下达了交通管制命令。\x01",
            "我竟然把这件事给忘了。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xD,
        (
            "拜其所赐，我就一直这么\x01",
            "无所事事地闲待到了中午。\x01",
            "哎呀呀，真是郁闷啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BF3")

    label("loc_5B9C")


    #C0325
    ChrTalk(
        0xD,
        (
            "郊外的交通管制\x01",
            "好像已经解除了……\x01",
            "稍后去一趟市里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xD,
        (
            "我要去图书馆\x01",
            "找些书看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BF3")

    Jump("loc_5C87")

    label("loc_5BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C10")
    Jump("loc_5C87")

    label("loc_5C10")


    #C0327
    ChrTalk(
        0xD,
        (
            "那些人好像在雷欧鲁先生\x01",
            "的杂货店买了很多保质期\x01",
            "很长的食品。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xD,
        (
            "唔，难道是要去登山吗？\x01",
            "但看上去又不像那样的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C87")

    TalkEnd(0xFE)
    Return()

    # Function_16_4D38 end

    def Function_17_5C8B(): pass

    label("Function_17_5C8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5DA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2E")

    #C0329
    ChrTalk(
        0xE,
        (
            "哈罗德先生一家\x01",
            "已经回市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xE,
        (
            "好不容易和他们交上了朋友，\x01",
            "他们一走，还真是有点寂寞呢……\x01",
            "但在这种状况下，也是没办法的事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5DA1")

    label("loc_5D2E")


    #C0331
    ChrTalk(
        0xE,
        (
            "哈罗德先生一家\x01",
            "很担心市里的邻居们，\x01",
            "确实是回去比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xE,
        (
            "我和史蒂芬以后回市里时，\x01",
            "一定要去他们家打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DA1")

    Jump("loc_651B")

    label("loc_5DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5DB4")
    Jump("loc_651B")

    label("loc_5DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5F01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7B")

    #C0333
    ChrTalk(
        0xE,
        (
            "在这种状况下，\x01",
            "真是很担心克洛斯贝尔市\x01",
            "的那些老街坊啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xE,
        (
            "哈罗德先生一家虽然\x01",
            "也很担心市里的情况，\x01",
            "但一直都在努力为村子做实事。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xE,
        "我也必须要做些力所能及的事情。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5EFC")

    label("loc_5E7B")


    #C0336
    ChrTalk(
        0xE,
        (
            "哈罗德先生一家虽然\x01",
            "也很担心市里的情况，\x01",
            "但一直都在努力为村子做实事。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xE,
        (
            "我也不能在这里干着急，\x01",
            "必须要做点力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EFC")

    Jump("loc_651B")

    label("loc_5F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6019")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FB7")

    #C0338
    ChrTalk(
        0xE,
        (
            "呼……\x01",
            "城市竟然会遭受袭击，\x01",
            "这真是让人意想不到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xE,
        (
            "幸好我的熟人朋友\x01",
            "全都平安无事……\x01",
            "但听说有不少人负伤呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xE,
        (
            "希望以后别再发生\x01",
            "这样的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6014")

    label("loc_5FB7")


    #C0341
    ChrTalk(
        0xE,
        (
            "呼……\x01",
            "城市竟然会遭受袭击，\x01",
            "这真是让人意想不到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xE,
        (
            "希望以后别再发生\x01",
            "这样的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6014")

    Jump("loc_651B")

    label("loc_6019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CA")

    #C0343
    ChrTalk(
        0xE,
        (
            "在我搬到村子之前，\x01",
            "完全不知道主日学校\x01",
            "还会外出授课呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        (
            "从村子赶到大圣堂上课，\x01",
            "对孩子来说确实很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xE,
        (
            "真该好好感谢\x01",
            "远道而来的修女啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6122")

    label("loc_60CA")


    #C0346
    ChrTalk(
        0xE,
        (
            "从这里赶到大圣堂上课，\x01",
            "对孩子来说确实很辛苦。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xE,
        (
            "真该好好感谢\x01",
            "远道而来的修女啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6122")

    Jump("loc_651B")

    label("loc_6127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6225")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61BA")

    #C0348
    ChrTalk(
        0xE,
        (
            "村长的儿子……\x01",
            "昨天回来之后，\x01",
            "神情好像相当紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xE,
        (
            "听说今天的商谈\x01",
            "将会关系到村子的未来……\x01",
            "紧张也是难免的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6220")

    label("loc_61BA")


    #C0350
    ChrTalk(
        0xE,
        (
            "史蒂芬和村里的孩子们\x01",
            "没有遭到魔兽的袭击，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        (
            "真是的，那个诈骗犯……\x01",
            "真是不可原谅。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6220")

    Jump("loc_651B")

    label("loc_6225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_631B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62B3")

    #C0352
    ChrTalk(
        0xE,
        (
            "啦啦啦……\x01",
            "床单铺好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "我生下史蒂芬之前，\x01",
            "一直很想当酒店的服务员。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xE,
        (
            "呵呵，在酒馆里帮忙\x01",
            "也很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6316")

    label("loc_62B3")


    #C0355
    ChrTalk(
        0xE,
        (
            "呵呵，在酒馆里帮忙\x01",
            "很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "史蒂芬好像也和朋友们\x01",
            "相处得很好，\x01",
            "我现在每天都过得很充实。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6316")

    Jump("loc_651B")

    label("loc_631B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6378")

    #C0357
    ChrTalk(
        0xE,
        (
            "我正在帮\x01",
            "店里做扫除。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xE,
        (
            "我和史蒂芬都蒙受\x01",
            "大家的照顾，\x01",
            "理应做出些回报。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_651B")

    label("loc_6378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6393")
    Call(0, 23)
    Jump("loc_63FE")

    label("loc_6393")


    #C0359
    ChrTalk(
        0xE,
        (
            "真的可以吗？\x01",
            "那我可就不客气啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xE,
        (
            "呵呵，听史蒂芬说你\x01",
            "之前请他吃过这个之后，\x01",
            "我就一直很想尝尝看呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63FE")

    Jump("loc_651B")

    label("loc_6403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_651B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B0")

    #C0361
    ChrTalk(
        0xE,
        (
            "我和儿子史蒂芬\x01",
            "是在不久之前从\x01",
            "克洛斯贝尔市搬来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xE,
        (
            "一开始，那孩子很讨厌这里，但他现在\x01",
            "好像已经完全习惯了村里的生活。\x01",
            "呵呵，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_651B")

    label("loc_64B0")


    #C0363
    ChrTalk(
        0xE,
        (
            "顺便一说，这个房间\x01",
            "是好心的格方先生以低廉\x01",
            "的价格租借给我们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xE,
        (
            "呵呵，这个村子的人们\x01",
            "都很友善呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651B")

    TalkEnd(0xFE)
    Return()

    # Function_17_5C8B end

    def Function_18_651F(): pass

    label("Function_18_651F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6597")

    #C0365
    ChrTalk(
        0xF,
        (
            "在主日学校的上课日，\x01",
            "只要到了休息时间，\x01",
            "酒馆的叔叔就会拿点心给我们吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xF,
        "啊～怎么还不快到休息时间～\x02",
    )

    CloseMessageWindow()

    label("loc_6597")

    TalkEnd(0xFE)
    Return()

    # Function_18_651F end

    def Function_19_659B(): pass

    label("Function_19_659B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_65E1")

    #C0367
    ChrTalk(
        0x10,
        (
            "普莉今天\x01",
            "要和哥哥\x01",
            "一起学习～\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x10,
        "不过什么都听不懂。\x02",
    )

    CloseMessageWindow()

    label("loc_65E1")

    TalkEnd(0xFE)
    Return()

    # Function_19_659B end

    def Function_20_65E5(): pass

    label("Function_20_65E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_66F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668A")

    #C0369
    ChrTalk(
        0x11,
        (
            "不久前，我和妈妈一起去\x01",
            "市里看了看。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x11,
        (
            "以前的朋友\x01",
            "和邻居们\x01",
            "都没出什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x11,
        (
            "妈妈之前一直\x01",
            "很担心……\x01",
            "大家都没事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_66EB")

    label("loc_668A")


    #C0372
    ChrTalk(
        0x11,
        (
            "我和妈妈一起去市里看了看，\x01",
            "昨天才回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x11,
        (
            "以前的朋友和邻居们\x01",
            "都没出什么事，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66EB")

    Jump("loc_67D6")

    label("loc_66F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_67D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6782")

    #C0374
    ChrTalk(
        0x11,
        (
            "住在市里的时候，\x01",
            "要自己去大圣堂听课……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x11,
        (
            "但搬到村里之后，\x01",
            "修女会到这里\x01",
            "给我们讲课。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x11,
        "……真是轻松了不少。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_67D6")

    label("loc_6782")


    #C0377
    ChrTalk(
        0x11,
        (
            "住在市里的时候，\x01",
            "要自己去大圣堂\x01",
            "的主日学校听课。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x11,
        "……现在真是轻松了不少。\x02",
    )

    CloseMessageWindow()

    label("loc_67D6")

    TalkEnd(0xFE)
    Return()

    # Function_20_65E5 end

    def Function_21_67DA(): pass

    label("Function_21_67DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6824")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681F")

    #C0379
    ChrTalk(
        0x12,
        (
            "……今天有位\x01",
            "重要的客人要来。\x01",
            "请出去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_681F")

    Jump("loc_6C6A")

    label("loc_6824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6AE0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6ADB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A3F")

    #C0380
    ChrTalk(
        0x12,
        "……是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#00003F迪利克先生……\x01",
            "那个……如果可以，\x01",
            "希望您再和村长谈谈……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x12,
        (
            "……哼，都已经谈过\x01",
            "无数次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x12,
        (
            "但村长实在是太过保守，\x01",
            "我提出了那么多种改革方案，\x01",
            "他却一条都不赞成。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x12,
        (
            "我原本都准备放弃改革了，\x01",
            "就在这种时候，\x01",
            "敏涅斯先生给我带来了新的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x12,
        (
            "我不再指望父亲了……\x01",
            "我会与敏涅斯先生齐心协力，\x01",
            "带领阿尔摩利卡村展开改革。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#00003F（……敏涅斯的身上存在一些可疑之处，\x01",
            "  真希望他能再考虑一下……）\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#00108F（但我们现在并没有足够的证据，\x01",
            "  想说服他恐怕很难……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6ADB")

    label("loc_6A3F")


    #C0388
    ChrTalk(
        0x12,
        (
            "我原本都准备放弃改革了，\x01",
            "就在这种时候，\x01",
            "敏涅斯先生给我带来了新的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x12,
        (
            "我不再指望父亲了……\x01",
            "我会与敏涅斯先生齐心协力，\x01",
            "带领阿尔摩利卡村展开改革。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ADB")

    Jump("loc_6C6A")

    label("loc_6AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C03")

    #C0390
    ChrTalk(
        0x12,
        (
            "无论我提出什么样的改革方案，\x01",
            "父亲……村长都会顽固不化地\x01",
            "否决掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x12,
        (
            "他的嘴里永远都只有『村子应有的姿态』、\x01",
            "『不能迷失本质』这些老掉牙的套话……\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x12,
        (
            "可是，如果总是抱着那种\x01",
            "虚无缥缈的过时理念不放，\x01",
            "就只会使村子默默走向灭亡……\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x12,
        (
            "……呼，我真是\x01",
            "有些累了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6C6A")

    label("loc_6C03")


    #C0394
    ChrTalk(
        0x12,
        (
            "既然村长不认同我的观念，\x01",
            "那就别想改革了。\x01",
            "接下来只需慢慢等待灭亡就是了……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x12,
        (
            "……我真是\x01",
            "累了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C6A")

    TalkEnd(0xFE)
    Return()

    # Function_21_67DA end

    def Function_22_6C6E(): pass

    label("Function_22_6C6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6CED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C8C")
    Call(0, 23)
    Jump("loc_6CED")

    label("loc_6C8C")


    #C0396
    ChrTalk(
        0x13,
        (
            "对了，我今天是来\x01",
            "给你送东西的。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x13,
        (
            "看啊，这是我最拿手的\x01",
            "自家制酱料，\x01",
            "和面条拌在一起吃吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CED")

    TalkEnd(0xFE)
    Return()

    # Function_22_6C6E end

    def Function_23_6CF1(): pass

    label("Function_23_6CF1")

    OP_4B(0xE, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0398
    ChrTalk(
        0x13,
        (
            "也就是说，你们暂时就\x01",
            "住在这个房间了？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xE,
        (
            "嗯，老板盛情难却，\x01",
            "我就恭敬不如从命了。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "作为回报，\x01",
            "我想为店里\x01",
            "做些事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x13,
        (
            "那很好啊。\x01",
            "他们一直都是父女两人操劳，\x01",
            "要是人手能增加，自然再好不过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0xE, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_23_6CF1 end

    def Function_24_6DCD(): pass

    label("Function_24_6DCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E58")

    #C0402
    ChrTalk(
        0x14,
        (
            "今天我无意中发现，\x01",
            "村中各处都留有脚印，\x01",
            "看起来像是大型猫科动物的。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x14,
        (
            "这个村子昨天\x01",
            "发生过什么事情吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_6EBB")

    label("loc_6E58")


    #C0404
    ChrTalk(
        0x14,
        (
            "村中各处都留有\x01",
            "奇怪的脚印，\x01",
            "看起来好像是大型猫科动物的。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x14,
        (
            "这个村子昨天\x01",
            "发生过什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EBB")

    TalkEnd(0xFE)
    Return()

    # Function_24_6DCD end

    def Function_25_6EBF(): pass

    label("Function_25_6EBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6ED0")
    Jump("loc_7988")

    label("loc_6ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_723E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71BE")

    #C0406
    ChrTalk(
        0x15,
        (
            "#03600F啊，各位……！\x01",
            "你们平安无事，真是太好了。\x02\x03",

            "#03603F我已经听到传闻了，\x01",
            "据说麦克道尔议长\x01",
            "发表了独立无效宣言。\x02\x03",

            "#03605F莫非是各位……？\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x103,
        "#00200F嗯，虽然其间大费周折……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#00000F阿尔摩利卡村的状况\x01",
            "有什么变化吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x15,
        (
            "#03603F不，暂时还没……\x02\x03",

            "#03600F要说最近比较特别的事情，就只有\x01",
            "在我和国防军交涉到一半时，他们突然接到了联络，\x01",
            "看起来似乎相当慌乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#00103F看样子，无效宣言对村子的影响\x01",
            "实在是微乎其微呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        (
            "#00306F嗯，不过对市内的影响\x01",
            "应该会很大。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x15,
        (
            "#03603F嗯，我很担心市里的邻居们，\x01",
            "也很挂念玛因兹和\x01",
            "乌尔斯拉医院的情况。\x02\x03",

            "#03608F如果可以自由行动，\x01",
            "真想去那些地方探访……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#00003F……总之，目前的状况\x01",
            "还没有彻底好转。\x02\x03",

            "#00000F哈罗德先生，\x01",
            "请您还是要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x15,
        "#03600F嗯，大家也要多加小心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 5)
    Jump("loc_7239")

    label("loc_71BE")


    #C0415
    ChrTalk(
        0x15,
        (
            "#03603F我很担心市里的邻居们，\x01",
            "也很挂念玛因兹和\x01",
            "乌尔斯拉医院的情况。\x02\x03",

            "#03608F如果可以自由行动，\x01",
            "真想去那些地方探访……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7239")

    Jump("loc_7988")

    label("loc_723E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_72DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7259")
    Call(0, 26)
    Jump("loc_72D8")

    label("loc_7259")


    #C0416
    ChrTalk(
        0x15,
        (
            "#03600F我正在了解各位村民\x01",
            "所需要的物资，以便与\x01",
            "国防军进行下一次交涉。\x02\x03",

            "#03603F各位，一定要多加小心。\x01",
            "……愿女神保佑你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72D8")

    Jump("loc_7988")

    label("loc_72DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73BA")
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
            "#1K◆「欺诈事件第二天」？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【已完成】\x01",        # 1
            "【未完成】\x01",        # 2
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
        (0, "loc_73A1"),
        (1, "loc_73A6"),
        (2, "loc_73B0"),
        (SWITCH_DEFAULT, "loc_73BA"),
    )


    label("loc_73A1")

    Jump("loc_73BA")

    label("loc_73A6")

    OP_29(0x87, 0x4, 0x10)
    Jump("loc_73BA")

    label("loc_73B0")

    OP_29(0x87, 0x3, 0x10)
    Jump("loc_73BA")

    label("loc_73BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_74AE")

    #C0418
    ChrTalk(
        0x15,
        (
            "#03600F是村长招待我\x01",
            "前来阿尔摩利卡村的。\x02\x03",

            "#03603F作为帮忙解决那起欺诈事件的回礼，\x01",
            "村长邀请我和皮特前来做客，\x01",
            "不过皮特婉言谢绝了……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        (
            "#00005F敏涅斯的那起事件吗……\x01",
            "原来如此。\x02\x03",

            "#00003F皮特没有被卷进来，\x01",
            "该说是万幸吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_757A")

    label("loc_74AE")


    #C0420
    ChrTalk(
        0x15,
        (
            "#03600F是村长招待我\x01",
            "前来阿尔摩利卡村的。\x02\x03",

            "#03603F作为之前帮忙解决某起事件的回礼，\x01",
            "村长邀请我和皮特前来做客，\x01",
            "不过皮特婉言谢绝了……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#00000F是这样啊。\x02\x03",

            "#00003F皮特没有被卷进来，\x01",
            "该说是万幸吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_757A")


    #C0422
    ChrTalk(
        0x15,
        "#03600F嗯，确实可以这么说。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_760F")

    label("loc_75A3")


    #C0423
    ChrTalk(
        0x15,
        (
            "#03600F好像有人在位于古道途中的\x01",
            "阿尔摩利卡古战场一带\x01",
            "看到过反抗势力的成员。\x02\x03",

            "#03603F各位，请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_760F")

    Jump("loc_7988")

    label("loc_7614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7869")

    #C0424
    ChrTalk(
        0x101,
        (
            "#00000F啊……哈罗德先生，\x01",
            "您今天来这里了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x15,
        (
            "#03605F哦，支援科的各位，\x01",
            "竟然在这里见到你们，真巧啊。\x02\x03",

            "#03600F嗯，我今天是来\x01",
            "做生意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，您似乎还是\x01",
            "和从前一样，\x01",
            "坚持诚信经商呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x15,
        (
            "#03609F哈哈，托各位的福，\x01",
            "我今天也做了一笔\x01",
            "很不错的买卖。\x02\x03",

            "#03600F对了……\x01",
            "如果可以，请各位\x01",
            "收下这个吧。\x02",
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
            "收下了１０个。\x02",
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
        "#00305F哦，可以收下吗？\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x15,
        (
            "#03600F嗯，这是对方在交易时\x01",
            "附送给我的礼品。\x02\x03",

            "#03609F我们也吃不了这么多，\x01",
            "就请各位拿去\x01",
            "一些好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#00002F嗯，既然如此……\x01",
            "那我们就不客气啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 6)
    Jump("loc_7988")

    label("loc_7869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7925")

    #C0432
    ChrTalk(
        0x15,
        (
            "#03604F托各位的福，\x01",
            "我今天也做了一笔\x01",
            "很不错的买卖。\x02\x03",

            "#03608F最近这段时间，\x01",
            "村长一直和迪利克争吵不休，\x01",
            "好像很烦恼的样子。\x02\x03",

            "#03603F……父子之间的矛盾\x01",
            "实在是很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_7988")

    label("loc_7925")


    #C0433
    ChrTalk(
        0x15,
        (
            "#03603F村长和迪利克……\x01",
            "其实都是在为\x01",
            "村子着想……\x02\x03",

            "#03608F……父子之间的矛盾\x01",
            "实在是很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7988")

    TalkEnd(0xFE)
    Return()

    # Function_25_6EBF end

    def Function_26_798C(): pass

    label("Function_26_798C")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0434
    ChrTalk(
        0x15,
        (
            "#03608F雷欧鲁先生需要治疗腰疼的药……\x01",
            "另外，安洁夫人家里的\x01",
            "创可贴已经不够了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x16,
        (
            "#03700F这家店的老板\x01",
            "也正因部分调料用完\x01",
            "而苦恼呢。\x02\x03",

            "#03708F但那些香料好像只能在\x01",
            "百货店里买到。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x15,
        (
            "#03603F嗯……创可贴\x01",
            "总有办法弄到，\x01",
            "至于其它东西，就需要去交涉了。\x02\x03",

            "#03600F谢谢啦，索菲娅。\x01",
            "后面的事情就交给我，你好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x10)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_26_798C end

    def Function_27_7AEB(): pass

    label("Function_27_7AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B1A")
    Call(0, 38)
    Return()

    label("loc_7B1A")

    Call(0, 39)
    Return()

    label("loc_7B1E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_27_7AEB end

    def Function_28_7B25(): pass

    label("Function_28_7B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B54")
    Call(0, 38)
    Return()

    label("loc_7B54")

    Call(0, 39)
    Return()

    label("loc_7B58")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_28_7B25 end

    def Function_29_7B5F(): pass

    label("Function_29_7B5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B70")
    Jump("loc_7D35")

    label("loc_7B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7B7E")
    Jump("loc_7D35")

    label("loc_7B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_7BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B99")
    Call(0, 26)
    Jump("loc_7BFA")

    label("loc_7B99")


    #C0437
    ChrTalk(
        0x16,
        (
            "#03700F我身为老公的内助，也要拿出\x01",
            "自己的微薄之力，为大家做些事情。\x02\x03",

            "希望多少能帮上\x01",
            "村民们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BFA")

    Jump("loc_7D35")

    label("loc_7BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD1")

    #C0438
    ChrTalk(
        0x16,
        (
            "#03708F支援科的其他成员……\x01",
            "真是让人担心啊。\x02\x03",

            "#03700F我会在此为大家祈祷，\x01",
            "希望你们能平安会合。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x105,
        "#10402F呵呵，谢谢啦，夫人。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x103,
        (
            "#00200F既然如此，我们无论如何\x01",
            "也要平安会面。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7D35")

    label("loc_7CD1")


    #C0441
    ChrTalk(
        0x16,
        (
            "#03708F支援科的其他成员……\x01",
            "真是让人担心啊。\x02\x03",

            "#03700F我会在此为大家祈祷，\x01",
            "希望你们能平安会合。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D35")

    TalkEnd(0xFE)
    Return()

    # Function_29_7B5F end

    def Function_30_7D39(): pass

    label("Function_30_7D39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7D4A")
    Jump("loc_80C9")

    label("loc_7D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7D58")
    Jump("loc_80C9")

    label("loc_7D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_7DB6")

    #C0442
    ChrTalk(
        0x17,
        (
            "#03805F唔～爸爸和妈妈\x01",
            "好像正在工作……\x02\x03",

            "#03800F不然就去找卡米尤\x01",
            "他们玩吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80C9")

    label("loc_7DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_80C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F92")
    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E5A")
    Jump("loc_7EA4")

    label("loc_7E5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E7A")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EA4")

    label("loc_7E7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E9A")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EA4")

    label("loc_7E9A")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EA4")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    #C0443
    ChrTalk(
        0x17,
        (
            "#03809F嘿嘿嘿，大狗狗，\x01",
            "以后还要来找我玩哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x107,
        (
            "#01200F#3C嗯，如果时间允许。\x02\x03",

            "#01203F……说起来，自从加入\x01",
            "支援科之后，\x01",
            "就经常有小孩子找我玩闹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x103,
        (
            "#00202F呵呵，这正是\x01",
            "蔡特的优点啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_80C4")

    label("loc_7F92")

    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8023")
    Jump("loc_806D")

    label("loc_8023")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8043")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_806D")

    label("loc_8043")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8063")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_806D")

    label("loc_8063")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_806D")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    #C0446
    ChrTalk(
        0x17,
        (
            "#03809F嘿嘿嘿，大狗狗，\x01",
            "以后还要来找我玩哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80C4")

    ClearChrFlags(0x17, 0x10)

    label("loc_80C9")

    TalkEnd(0xFE)
    Return()

    # Function_30_7D39 end

    def Function_31_80CD(): pass

    label("Function_31_80CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80E3")
    SetScenarioFlags(0x2, 2)

    label("loc_80E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84AF")

    #C0447
    ChrTalk(
        0x18,
        (
            "#04303F#30W我们的梅尔卡瓦\x01",
            "暂时无法使用了……\x02\x03",

            "#04300F不过，修复完毕之后，\x01",
            "我们会尽力为你们提供支援的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_826D")
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x10)
    TurnDirection(0x18, 0x105, 0)
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81F9")
    Jump("loc_8243")

    label("loc_81F9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8219")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8243")

    label("loc_8219")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8239")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8243")

    label("loc_8239")

    OP_52(0x18, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8243")

    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x10)

    label("loc_826D")


    #C0448
    ChrTalk(
        0x18,
        (
            "#04308F#30W瓦吉，\x01",
            "一定不要太乱来哦。\x02\x03",

            "#04301F如果像我这样，耗尽全部力量，\x01",
            "在危机时刻恐怕就要丢掉小命了。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x105,
        (
            "#10403F嗯……\x01",
            "我一定会铭记在心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84AA")
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x18,
        (
            "#04300F#30W哦……差点忘了。\x01",
            "罗伊德，把手伸出来。\x02",
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
            "获得了。\x02",
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
        "#00305F这是……\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#00005F好像是什么东西的碎片吧……？\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x18,
        (
            "#04303F#30W这是在神机的坠毁地点\x01",
            "发现的东西……\x01",
            "多半是机体中的某些部件吧。\x02\x03",

            "#04300F我觉得你们\x01",
            "也许能用得上，\x01",
            "就把它捡走了。\x02\x03",

            "#04311F总之这东西很少见，你们就带走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#00000F那就……\x01",
            "不客气啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84AA")

    Jump("loc_853C")

    label("loc_84AF")


    #C0456
    ChrTalk(
        0x18,
        (
            "#04303F#30W我们的梅尔卡瓦\x01",
            "暂时无法使用了……\x02\x03",

            "#04300F不过，修复完毕之后，\x01",
            "我们会尽力为你们提供支援的。\x02\x03",

            "#04302F总之，你们就多多加油吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_853C")

    TalkEnd(0xFE)
    Return()

    # Function_31_80CD end

    def Function_32_8540(): pass

    label("Function_32_8540")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8631")

    #C0457
    ChrTalk(
        0x19,
        (
            "#13808F来主日学校上课的小琪雅\x01",
            "总是一脸兴奋地\x01",
            "谈论你们。\x02\x03",

            "#13804F……身为一名星杯骑士，\x01",
            "这样的发言也许不太合适……\x02\x03",

            "#13802F但我认为，让那孩子恢复笑脸\x01",
            "才是最重要的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        "#00102F莉丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        "#00204F……明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_86A0")

    label("loc_8631")


    #C0460
    ChrTalk(
        0x19,
        (
            "#13808F来主日学校上课的小琪雅\x01",
            "总是一脸兴奋地\x01",
            "谈论你们。\x02\x03",

            "#13804F……请一定要让她\x01",
            "重新显露出当时那种笑容。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A0")

    TalkEnd(0xFE)
    Return()

    # Function_32_8540 end

    def Function_33_86A4(): pass

    label("Function_33_86A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_879D")

    #C0461
    ChrTalk(
        0xFE,
        (
            "作为正式会议的前期准备，\x01",
            "我一边处理委托，一边巡视各地。\x01",
            "这一带真是很安宁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "不过村长先生和迪利克之间的关系\x01",
            "似乎变得有些恶劣啊，让人有点担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        (
            "呼，但那些事情也轮不到我去干预。\x01",
            "身为游击士，必须要站在中立的立场。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_882B")

    label("loc_879D")


    #C0464
    ChrTalk(
        0xFE,
        (
            "村长先生和迪利克之间的关系\x01",
            "似乎变得有些恶劣啊，让人有点担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "呼，但那些事情也轮不到我去干预。\x01",
            "身为游击士，必须要站在中立的立场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_882B")

    TalkEnd(0xFE)
    Return()

    # Function_33_86A4 end

    def Function_34_882F(): pass

    label("Function_34_882F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_889F")

    #C0466
    ChrTalk(
        0xFE,
        (
            "小桥那里站着一位\x01",
            "打扮得非常考究的\x01",
            "叔叔……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "……呼，不管他了，\x01",
            "我对人类没有兴趣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_88D4")

    label("loc_889F")


    #C0468
    ChrTalk(
        0xFE,
        "（大吃大嚼）……\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xFE,
        (
            "我好喜欢这里的\x01",
            "蛋包饭……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88D4")

    TalkEnd(0xFE)
    Return()

    # Function_34_882F end

    def Function_35_88D8(): pass

    label("Function_35_88D8")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8977")
    BeginChrThread(0x109, 1, 0, 36)
    WaitChrThread(0x109, 1)

    label("loc_8977")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8991")
    BeginChrThread(0x105, 1, 0, 36)
    WaitChrThread(0x105, 1)

    label("loc_8991")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89AB")
    BeginChrThread(0x106, 1, 0, 36)
    WaitChrThread(0x106, 1)

    label("loc_89AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89C5")
    BeginChrThread(0x10A, 1, 0, 36)
    WaitChrThread(0x10A, 1)

    label("loc_89C5")

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

    def lambda_8AA9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8AA9)
    Sleep(50)

    def lambda_8AB9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8AB9)
    Sleep(50)

    def lambda_8AC9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8AC9)
    Sleep(50)

    def lambda_8AD9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8AD9)
    Sleep(50)

    def lambda_8AE9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_8AE9)
    Sleep(50)

    def lambda_8AF9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_8AF9)
    OP_6F(0x79)

    #C0470
    ChrTalk(
        0x101,
        "#00005F啊……\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x102,
        "#00105F莉丝小姐……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B68")

    #C0472
    ChrTalk(
        0x105,
        "#10402F怎么，原来你们在这里啊。\x02",
    )

    CloseMessageWindow()

    label("loc_8B68")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetChrSubChip(0x18, 0x1)
    OP_93(0x19, 0x5A, 0x1F4)

    #C0473
    ChrTalk(
        0x19,
        "#13805F各位……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BD3")

    #C0474
    ChrTalk(
        0x18,
        (
            "#11P#04300F#30W啊……\x01",
            "是瓦吉和罗伊德啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF8")

    label("loc_8BD3")


    #C0475
    ChrTalk(
        0x18,
        "#11P#04300F#30W啊……是你们啊。\x02",
    )

    CloseMessageWindow()

    label("loc_8BF8")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CD8")
    BeginChrThread(0x109, 1, 0, 37)
    WaitChrThread(0x109, 1)

    label("loc_8CD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CF2")
    BeginChrThread(0x105, 1, 0, 37)
    WaitChrThread(0x105, 1)

    label("loc_8CF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D0C")
    BeginChrThread(0x106, 1, 0, 37)
    WaitChrThread(0x106, 1)

    label("loc_8D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D26")
    BeginChrThread(0x10A, 1, 0, 37)
    WaitChrThread(0x10A, 1)

    label("loc_8D26")

    WaitChrThread(0x104, 2)
    Sleep(1000)

    #C0476
    ChrTalk(
        0x101,
        "#6P#00000F二位……我们已经收到消息了。\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x104,
        (
            "#12P#00309F听说你们漂亮地击坠了\x01",
            "那架惊人的神机。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x102,
        "#12P#00104F真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x18,
        (
            "#11P#04302F#30W哈哈……\x01",
            "但我们的损失也很惨重啊。\x02\x03",

            "#04306F我用尽了全部力量，不得不在\x01",
            "这里休养，真是丢脸呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F0D")

    #C0480
    ChrTalk(
        0x103,
        (
            "#6P#00205F据阿巴斯先生说，\x01",
            "你使用了某种相当危险的力量，\x01",
            "因此陷入危险状态了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x105,
        (
            "#12P#10404F嗯，你是将『圣痕』的力量\x01",
            "与梅尔卡瓦相结合，一口气释放而出吧？\x02\x03",

            "#10402F真是太乱来了。\x01",
            "稍有疏忽，恐怕就要去见女神了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F63")

    label("loc_8F0D")


    #C0482
    ChrTalk(
        0x103,
        (
            "#6P#00205F据阿巴斯先生说，\x01",
            "你使用了某种相当危险的力量，\x01",
            "因此陷入危险状态了……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F63")


    #C0483
    ChrTalk(
        0x101,
        "#6P#00005F是、是这样吗……？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x19,
        (
            "#5P#13800F嗯，『圣痕』是禁忌之力的源泉，\x01",
            "人类的身体是无法承受的。\x02\x03",

            "#13808F无限制地释放那种力量，\x01",
            "未免也太过鲁莽了。\x02\x03",

            "#13803F身为担负着重大责任的『守护骑士』，\x01",
            "不得不说，这种行为实在是轻率妄为。\x02",
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
            "#11P#04306F#30W……呼，莉丝，\x01",
            "你就饶了我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_917C")

    #C0486
    ChrTalk(
        0x105,
        (
            "#12P#10409F哈哈，感觉真不错，\x01",
            "就像是被妻子管教的丈夫呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_920F")

    label("loc_917C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91C5")

    #C0487
    ChrTalk(
        0x109,
        (
            "#12P#10109F（怎、怎么像\x01",
            "  妻子管教丈夫一样…）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_920F")

    label("loc_91C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_920F")

    #C0488
    ChrTalk(
        0x106,
        (
            "#12P#10702F（呵呵，被教训得\x01",
            "  连头都抬不起来呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_920F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9272")

    #C0489
    ChrTalk(
        0x10A,
        (
            "#12P#00603F（星杯骑士团的守护骑士……\x01",
            "  与我了解到的情报有很大不同啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9323")

    label("loc_9272")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92D3")

    #C0490
    ChrTalk(
        0x106,
        (
            "#12P#10704F（星杯骑士团的守护骑士……\x01",
            "  与我所知的情报有很大不同呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9323")

    label("loc_92D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9323")

    #C0491
    ChrTalk(
        0x109,
        (
            "#12P#10106F呼，我认为你也应该\x01",
            "牢牢记住阿巴斯先生说过的话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9323")


    #C0492
    ChrTalk(
        0x18,
        (
            "#11P#04303F#30W说的没错……\x02\x03",

            "#04308F话说回来，出现了\x01",
            "相当惊人的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x19,
        (
            "#5P#13801F『碧之大树』……\x01",
            "凭借人类的执念而生成的奇迹。\x02\x03",

            "#13803F除了女神之力外，竟然还有\x01",
            "其它方式能创造出那样的东西……\x02\x03",

            "#13808F而且还是利用小琪雅的力量……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x102,
        "#12P#00108F……嗯……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x103,
        (
            "#6P#00203F嗯，老实说，我们直到\x01",
            "现在都感觉像在做梦……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        (
            "#6P#00003F但我们无论如何也要\x01",
            "亲自将此次事件解决。\x02\x03",

            "#00001F我们是『特别任务支援科』的成员……\x01",
            "更是那个孩子的监护人。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x18,
        (
            "#11P#04304F#30W是吗……\x01",
            "看来你们已经有所觉悟了呢。\x02\x03",

            "#04300F我们的梅尔卡瓦\x01",
            "暂时无法使用了……\x02\x03",

            "不过，修复完毕之后，\x01",
            "我们会尽力为你们提供支援的。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x19,
        (
            "#5P#13802F……愿女神保佑各位，\x01",
            "请一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x104,
        "#12P#00302F谢啦，莉丝小姐。\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#12P#00100F那我们就先走了。\x02",
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

    # Function_35_88D8 end

    def Function_36_9646(): pass

    label("Function_36_9646")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9675")
    SetChrPos(0xFE, 77230, 0, -2080, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9751")

    label("loc_9675")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96A4")
    SetChrPos(0xFE, 78370, 0, -1940, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9751")

    label("loc_96A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96D3")
    SetChrPos(0xFE, 79550, 0, -2100, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9751")

    label("loc_96D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9702")
    SetChrPos(0xFE, 77200, 0, -3170, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9751")

    label("loc_9702")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9731")
    SetChrPos(0xFE, 78370, 0, -3110, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9751")

    label("loc_9731")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9751")
    SetChrPos(0xFE, 79550, 0, -3200, 0)

    label("loc_9751")

    Return()

    # Function_36_9646 end

    def Function_37_9752(): pass

    label("Function_37_9752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_979B")
    SetChrPos(0xFE, 78700, 0, -1050, 270)

    def lambda_9777():
        OP_95(0xFE, 71150, 0, -1050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9777)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98F9")

    label("loc_979B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E4")
    SetChrPos(0xFE, 78650, 0, 0, 270)

    def lambda_97C0():
        OP_95(0xFE, 71150, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_97C0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98F9")

    label("loc_97E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982D")
    SetChrPos(0xFE, 79740, 0, -1220, 270)

    def lambda_9809():
        OP_95(0xFE, 72240, 0, -1220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9809)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98F9")

    label("loc_982D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9876")
    SetChrPos(0xFE, 79740, 0, -40, 270)

    def lambda_9852():
        OP_95(0xFE, 72240, 0, -40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9852)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98F9")

    label("loc_9876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98BF")
    SetChrPos(0xFE, 80780, 0, -1100, 270)

    def lambda_989B():
        OP_95(0xFE, 73280, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_989B)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98F9")

    label("loc_98BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98F9")
    SetChrPos(0xFE, 80780, 0, 20, 270)

    def lambda_98E4():
        OP_95(0xFE, 73280, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_98E4)

    label("loc_98F9")

    Return()

    # Function_37_9752 end

    def Function_38_98FA(): pass

    label("Function_38_98FA")

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
        "#5P呀，你们来了啊。\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x1B,
        (
            "#5P缇欧！\x01",
            "……还是不在啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x1B,
        "#5P唉，心情好低落。\x02",
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
        "#12P#00006F真、真抱歉啊。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x1A,
        (
            "#5P哪里……\x01",
            "该道歉的是我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        (
            "#12P#00309F话说回来，艾欧莉娅小姐……\x01",
            "还是一样美丽动人啊。\x02\x03",

            "#00304F不如就放弃阿缇，\x01",
            "让我来抚慰你如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1B,
        "#5P不必了，我拒绝⊥\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x104,
        "#12P#00306F呜……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x109,
        "#12P#10106F兰、兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x105,
        "#12P#10302F呵呵，拒绝得真干脆啊。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x102,
        (
            "#12P#00106F真是的，兰迪你就\x01",
            "长点教训吧。\x02\x03",

            "#00100F抱歉哦，林小姐。\x01",
            "请赶快说说\x01",
            "委托的内容吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x1A,
        (
            "#5P嗯，我现在就开始说明。\x01",
            "委托内容非常简单。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x1A,
        (
            "#5P想拜托你们做的并非他事，\x01",
            "就是陪我们两人进行训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x1A,
        (
            "#5P也就是希望各位\x01",
            "与我们交手比试。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        (
            "#12P#00000F所谓的比试……\x01",
            "是实战形式的战斗吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#12P#00100F不过，为何要等到现在\x01",
            "才提出这样的委托呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x1B,
        (
            "#5P这个嘛，因为你们不久之前\x01",
            "还是一群稚气未脱的弱小之辈呢。\x02",
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
        "#12P#00012F确实无法反驳啊……\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        "#12P#00106F嗯，戳到痛处了呢。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x1A,
        (
            "#5P哈哈，不要沮丧嘛，\x01",
            "如今找上你们，就表示我们\x01",
            "已经认同了你们的实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x1A,
        (
            "#5P而且强烈希望\x01",
            "亲身感受你们的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x1B,
        (
            "#5P我和林的空闲时间\x01",
            "正好赶在了一起，\x01",
            "所以就想充分利用这次机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x1B,
        (
            "#5P不过，把斯克特和温蔡尔排除在外，\x01",
            "还真是有点对不起他们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        (
            "#12P#00009F啊哈哈，\x01",
            "要是他们二位也在，\x01",
            "我们就真是应付不来了。\x02\x03",

            "#00000F不过……的确有道理，\x01",
            "这种机会实在是不多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x104,
        (
            "#12P#00300F是啊！\x01",
            "就让我们接受指导吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x105,
        (
            "#12P#10300F接受指导吗……\x02\x03",

            "#10304F这种话从兰迪的嘴里说出来，\x01",
            "似乎另有其它含义呢。\x02",
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
            "#12P#10100F哎？那是什么意思……\x02\x03",

            "#10114F啊。\x02",
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
            "#6P#00111F瓦吉……不要再\x01",
            "继续胡说八道了哟～\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x1A,
        (
            "#5P哈哈，两位新成员似乎\x01",
            "也能给我们带来很多乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x1B,
        (
            "#5P嗯嗯，看上去，他们两个\x01",
            "也都相当有实力呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x12C, 0x1F4)
    Sleep(300)

    #C0531
    ChrTalk(
        0x109,
        (
            "#12P#10102F相、相当有实力可真是过奖了，\x01",
            "我有点没自信呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x105,
        "#12P#10300F呵呵，承蒙夸奖，深感荣幸。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x1A,
        (
            "#5P那么，意下如何？\x01",
            "你们可以接受吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        (
            "#12P#00004F嗯……\x01",
            "如果二位不嫌弃，我们很愿意接受这个任务。\x02\x03",

            "#00000F地点要选在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x1A,
        (
            "#5P哦，既要选择比较广阔的场所，\x01",
            "又不能影响大家的日常生活，\x01",
            "所以我们认为村口比较合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x1A,
        (
            "#5P之前已经得到了村长的许可，\x01",
            "我们随时都可以过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x1A,
        (
            "#5P如果你们已经准备好了，\x01",
            "最好立刻开始……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x1B,
        (
            "#5P还需要购买道具或整理装备吗？\x01",
            "如果需要准备，我们也可以再等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        "#12P#00000F这个嘛……\x02",
    )

    CloseMessageWindow()
    OP_29(0x75, 0x1, 0x0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【准备完毕，开始比试】\x01",      # 0
            "【还要继续准备】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A48E")

    #C0540
    ChrTalk(
        0x101,
        (
            "#12P#00000F已经准备好了，\x01",
            "现在就一起过去如何？\x02\x03",

            "#00004F我们正式接受\x01",
            "二位的任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x1A,
        "#5P呵呵，就该这样。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x1B,
        "#5P好，那我们就立刻开始训练吧！\x02",
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
            "任务【参加游击士的训练】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_A58A")

    label("loc_A48E")


    #C0544
    ChrTalk(
        0x101,
        (
            "#12P#00000F我们需要准备一下，\x01",
            "可以请二位等等吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x1A,
        "#5P嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x1A,
        (
            "#5P另外，\x01",
            "你们要是还有其它事情，\x01",
            "也可以优先处理哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x1B,
        (
            "#5P反正我们只是利用\x01",
            "空闲时间而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x1B,
        (
            "#5P要是各位有事，\x01",
            "我们就先在这里休息一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        "#12P#00000F好的，明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A58A")

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

    # Function_38_98FA end

    def Function_39_A5E2(): pass

    label("Function_39_A5E2")

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
        "#5P哦，已经准备好了？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x1B,
        (
            "#5P可以和我们\x01",
            "交手比试了吗？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【准备完毕，开始比试】\x01",      # 0
            "【还要继续准备】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A816")

    #C0552
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，准备好了。\x01",
            "现在就一起过去吧？\x02\x03",

            "我们正式接受\x01",
            "二位的任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x1A,
        "#5P呵呵，就该这样。\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x1B,
        "#5P好，那我们就立刻开始训练吧！\x02",
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
            "任务【参加游击士的训练】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_A8CB")

    label("loc_A816")


    #C0556
    ChrTalk(
        0x101,
        (
            "#12P#00006F抱歉……\x01",
            "还要请二位再等一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x1A,
        "#5P哦，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x1A,
        (
            "#5P没关系，如果你们还有其它事情，\x01",
            "就优先处理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x1B,
        (
            "#5P不用在意\x01",
            "我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x101,
        "#12P#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A8CB")

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

    # Function_39_A5E2 end

    def Function_40_A920(): pass

    label("Function_40_A920")

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
            "呀，支援科的诸位，\x01",
            "欢迎光临『白蜡亭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xA,
        (
            "今天要吃点什么吗？\x01",
            "还是想住宿？\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x101,
        (
            "#00000F那个……我们今天\x01",
            "是为工作而来的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0564
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

    #C0565
    ChrTalk(
        0xA,
        (
            "哦，是那个啊。\x01",
            "我听克洛斯贝尔通讯社\x01",
            "的人说过。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "那就请你们\x01",
            "赶快尝尝我做的\x01",
            "『大师蛋包饭』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x105,
        "#10300F呵呵，麻烦您啦，老板。\x02",
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
            "罗伊德等人品尝了大师蛋包饭。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0569
    ChrTalk(
        0x102,
        (
            "#00104F（品尝）……\x01",
            "嗯～这里的蛋包饭\x01",
            "果然很美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x103,
        "#00200F嗯，确实是顶级的。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x101,
        (
            "#00000F饭粒被柔软的鸡蛋所包裹，\x01",
            "充满番茄的味道，\x01",
            "这种质朴的风味真是很不错啊。\x02\x03",

            "#00004F这座被自然地带所环绕\x01",
            "的阿尔摩利卡村\x01",
            "也是个很不错的地方……\x02\x03",

            "#00009F如果来到阿尔摩利卡村，\x01",
            "在吃到这里的蛋包饭之前绝不能回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "哈哈，听你们如此夸奖，\x01",
            "还真是有点不好意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x109,
        (
            "#10102F呵呵，看来罗伊德警官\x01",
            "很喜欢这里的蛋包饭……\x02\x03",

            "那报道文章就交给你来写吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    #C0574
    ChrTalk(
        0x104,
        (
            "#00306F嗯，连同老板的品格，到时候一定\x01",
            "要在报道中好好夸赞一下这家店。\x02\x03",

            "#00300F老板以前也请我们白吃过一顿呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        (
            "#00000F嗯，交给我\x01",
            "来写吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        (
            "哈哈，请一定要写出\x01",
            "一篇精彩的报道，\x01",
            "让我们的生意更加兴隆哦。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B142")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B15F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B15F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B172")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_B185")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B1A2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B1B5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_B1D2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_B1E5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_B202")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_B215")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_B232")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B232")

    OP_29(0x80, 0x1, 0x7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B307")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0577
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B2FE")

    #A0578
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

    label("loc_B2FE")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_B307")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3CA")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0579
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

    #A0580
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

    label("loc_B3CA")

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

    # Function_40_A920 end

    def Function_41_B404(): pass

    label("Function_41_B404")

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
            "#00000F那个……有点事情\x01",
            "想问问您……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0582
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "询问了最近来访村里的\x01",
            "外国人的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0583
    ChrTalk(
        0xA,
        (
            "哦，是最近这段时间偶尔\x01",
            "住在我们这里的那个人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xA,
        (
            "嗯，那是个很讲究礼仪的人，\x01",
            "我对他很有好感。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x104,
        "#00303F很讲究礼仪啊。\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x102,
        (
            "#00105F对了……\x01",
            "您知道那个人\x01",
            "的名字吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xA,
        (
            "唔，我记得是……\x01",
            "『敏涅斯』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xA,
        (
            "他在住宿登记本上签的名字\x01",
            "好像是这个。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x105,
        (
            "#10300F『敏涅斯』吗……\x01",
            "呵呵，至少知道\x01",
            "名字了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x103,
        (
            "#00201F关于那位敏涅斯先生，\x01",
            "您还有什么了解吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xA,
        (
            "唔……我和他没说过几句话，\x01",
            "谈不上什么了解呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xA,
        (
            "不过他曾多次把迪利克叫到房间里，\x01",
            "两人好像聊了些什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xA,
        "我知道的也只有这些了。\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x109,
        (
            "#10105F（和村长的儿子\x01",
            "  秘密会谈啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        (
            "#00003F（嗯……总之，\x01",
            "  我们已经了解到\x01",
            "  不少情报了。）\x02\x03",

            "#00000F多谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xA,
        "哪里哪里，不客气。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xA,
        (
            "要是能顺便点些东西\x01",
            "就更好了。\x02",
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

    # Function_41_B404 end

    def Function_42_B83C(): pass

    label("Function_42_B83C")

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
            "#00000F那个……有点事情\x01",
            "想问问您……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0599
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "询问了最近来访村里的\x01",
            "外国人的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0600
    ChrTalk(
        0x8,
        (
            "哦，那个男人啊。\x01",
            "那可是个很有眼光的男人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        "#00105F……怎么说？\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x8,
        (
            "他非常中意我们村子\x01",
            "出产的蜂蜜。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x8,
        (
            "『这么好的蜂蜜，\x01",
            "  在整个大陆都会大受欢迎的！』\x01",
            "……他是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x103,
        "#00203F受欢迎吗……\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x105,
        (
            "#10300F从他的言行举止来看，\x01",
            "是个生意人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x8,
        (
            "唔，我并没有问得很详细，\x01",
            "不过应该没错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x8,
        (
            "他独具慧眼，\x01",
            "一定是个很有名的商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x8,
        (
            "真是的，要是我孙子\x01",
            "能多学学人家就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x109,
        "#10112F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x104,
        (
            "#00303F总之就是个看似\x01",
            "很老练的生意人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        (
            "#00000F原来如此……\x01",
            "我明白了。\x02\x03",

            "#00004F感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x8,
        "嗯，以后有空再来哦。\x02",
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

    # Function_42_B83C end

    def Function_43_BBC3(): pass

    label("Function_43_BBC3")

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
            "哦……\x01",
            "莫非各位想住宿吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xA,
        "现在还有空房间哦。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        (
            "#00005F（对了，如果盖巴尔\x01",
            "  先生来到了\x01",
            "  阿尔摩利卡村……）\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x103,
        (
            "#00203F（来酒馆住宿的可能性\x01",
            "  应该很高吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x101,
        (
            "#00000F那个……有件事情\x01",
            "想问问您……\x02\x03",

            "请问有没有一位名叫盖巴尔\x01",
            "的先生来这里住宿？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xA,
        "哦，盖巴尔先生啊。\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xA,
        (
            "他最近偶尔会来\x01",
            "我这里吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x102,
        (
            "#00105F偶尔来吃饭……？\x02\x03",

            "也就是说，并没有\x01",
            "住在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xA,
        (
            "嗯，并没有。\x01",
            "我不记得他登记过房间……\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xA,
        (
            "我想盖巴尔先生是因为\x01",
            "喜欢本店的料理，\x01",
            "所以才会特意从市内跑到村子……\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x104,
        (
            "#00303F嗯……\x01",
            "总觉得那终究不太\x01",
            "现实呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x109,
        (
            "#10100F说不定……\x01",
            "他在阿尔摩利卡村\x01",
            "有亲戚？\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x105,
        (
            "#10300F若是如此，\x01",
            "阿鲁姆先生之前\x01",
            "就应该调查到了……\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_END)), "loc_BF98")

    #C0626
    ChrTalk(
        0x101,
        "#00003F莫非是……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    #C0627
    ChrTalk(
        0x101,
        (
            "#00001F……我们还是去找村长谈谈吧，\x01",
            "说不定他知道些什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_BFF9")

    label("loc_BF98")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    #C0628
    ChrTalk(
        0x101,
        (
            "#00003F我们先四处调查一番吧。\x02\x03",

            "#00000F说不定能发现\x01",
            "某些可以藏身\x01",
            "的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFF9")

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

    # Function_43_BBC3 end

    def Function_44_C053(): pass

    label("Function_44_C053")

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
            "#11P哦……\x01",
            "你们好像是警察局\x01",
            "特别任务支援科的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xA,
        "#11P当时真是多谢你们的帮忙啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_C24B")

    #C0631
    ChrTalk(
        0xD,
        (
            "#5P是啊，多亏你们帮忙救回了\x01",
            "迷失在古战场的游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xD,
        (
            "#5P说起来，\x01",
            "我以前忘了归还图书馆的书，\x01",
            "也给你们添了不少麻烦呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x101,
        (
            "#00012F哈哈……\x01",
            "哪里哪里，请不必在意。\x02\x03",

            "#00000F最近有什么\x01",
            "异常情况吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2B7")

    label("loc_C24B")


    #C0634
    ChrTalk(
        0xD,
        (
            "#5P是啊，多亏你们帮忙救回了\x01",
            "迷失在古战场的游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        (
            "#00000F嗯，好久不见啦。\x02\x03",

            "最近有什么\x01",
            "异常情况吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2B7")


    #C0636
    ChrTalk(
        0xA,
        (
            "#11P这个嘛，\x01",
            "这个村子一直\x01",
            "都很平静……\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xA,
        (
            "#11P硬要说的话，\x01",
            "也就是不久之前，\x01",
            "有几个生面孔来过村子。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xD,
        "#5P哦，你是说那个红发壮汉和他的同伴吧……\x02",
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
        "#00105F红发壮汉……\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x104,
        (
            "#6P#00301F……那红发的颜色\x01",
            "是不是和我的\x01",
            "发色一样？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xA,
        (
            "#11P啊，你这么一说，\x01",
            "好像还真是很像呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xA,
        (
            "#11P和红发壮汉在一起的\x01",
            "那个活泼小姑娘\x01",
            "好像也是这种发色。\x02",
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
            "#00001F……那个，希望您能\x01",
            "说得再详细些……\x01",
            "那些人在村子里做了什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xA,
        (
            "#11P这个嘛～我也不可能\x01",
            "一直盯着他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xA,
        "#11P你知道什么吗？阿尔弗雷德。\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xD,
        (
            "……说起来，我倒是看见\x01",
            "他们在杂货店买东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xD,
        (
            "好像买了很多干酪、\x01",
            "腌肉和黑麦面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xD,
        (
            "因为那天赚到了不少钱，\x01",
            "雷欧鲁爷爷很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        "#00103F是吗……\x02",
    )

    CloseMessageWindow()

    def lambda_C620():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C620)
    Sleep(50)

    def lambda_C630():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C630)
    Sleep(50)

    def lambda_C640():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C640)
    Sleep(50)
    OP_93(0x109, 0x13B, 0x1F4)

    #C0650
    ChrTalk(
        0x101,
        (
            "#11P#00001F……『赤色星座』的人\x01",
            "竟然会来阿尔摩利卡村。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x109,
        (
            "#6P#10101F听起来，\x01",
            "他们似乎是来采购食物的。\x02\x03",

            "#10103F买的好像都是一些\x01",
            "保质期很长的食品。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x104,
        (
            "#12P#00303F……对猎兵团而言，\x01",
            "保存充足的食物是基本中的基本。\x02\x03",

            "为了确保可以随时迎接战斗，\x01",
            "必须要一直保持万全状态……\x02\x03",

            "#00301F他们身为经受过千锤百炼的猎兵团，\x01",
            "在这方面自然不会敷衍。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x105,
        "#6P#10300F呵呵，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        (
            "#00103F不过，他们的目的\x01",
            "真的只是采购食物吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        (
            "#11P#00001F……我们还是\x01",
            "继续保持警觉\x01",
            "为好。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C82E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C82E)
    Sleep(50)

    def lambda_C83E():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C83E)
    Sleep(50)

    def lambda_C84E():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C84E)
    Sleep(50)

    def lambda_C85E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C85E)
    Sleep(50)

    def lambda_C86E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C86E)
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
            "#00004F……感谢您的协助，\x01",
            "这些情报非常重要。\x02\x03",

            "#00000F如果以后有什么事情，\x01",
            "请随时联系我们支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xA,
        (
            "#11P嗯，虽然不太明白，\x01",
            "但你们似乎也很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0xA,
        (
            "#11P好啦，以后还要再来哦。\x01",
            "我会给你们准备\x01",
            "美味的蛋包饭的。\x02",
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

    # Function_44_C053 end

    def Function_45_C9AE(): pass

    label("Function_45_C9AE")

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
        "啊，好大的狗狗～！\x02",
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

    def lambda_CC77():
        OP_93(0x15, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_CC77)
    Sleep(50)

    def lambda_CC87():
        OP_93(0x16, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_CC87)
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
        "你们是……！\x02",
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
            "哦哦……罗伊德警官！\x02\x03",

            "太好了……\x01",
            "你平安无事啊！\x02",
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
            "#00002F#12P……哈罗德先生，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x107,
        (
            "#01200F#12P#3C……『好大的狗狗』\x01",
            "是指我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x103,
        "#00204F#6P呵呵，这称呼真不错。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x105,
        "#10409F#12P啊哈哈，神狼也无可奈何呢。\x02",
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
            "#03610F#11P我当时听到有关\x01",
            "你们的传闻之后，\x01",
            "实在是很担心。\x02\x03",

            "#03600F听说你还强行越狱，\x01",
            "遭到指名通缉……看你现在的样子，\x01",
            "似乎平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x16,
        (
            "#03708F#11P那个……支援科的其他成员\x01",
            "现在怎样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x103,
        (
            "#00206F#6P……很遗憾，\x01",
            "仍然分散在各地。\x02\x03",

            "#00208F而且我们并不了解\x01",
            "大家的详细所在地……\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x16,
        "#03710F#11P是吗……真让人担心呢。\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x101,
        (
            "#00001F#6P……哈罗德先生，\x01",
            "发生异变时，你们正好\x01",
            "来这个村子了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x15,
        (
            "#03610F#11P嗯……\x01",
            "一开始并不知道发生了什么，\x01",
            "完全不知所措。\x02\x03",

            "#03608F然后就在还没搞清状况的情况下，\x01",
            "总统又颁布了禁行令，\x01",
            "结果一家人都无法回市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x16,
        (
            "#03700F#11P不过，村民们实在是\x01",
            "很关照我们。\x02\x03",

            "酒馆的老板为我们提供了房间，\x01",
            "让我们住到事态平息下来为止……\x02\x03",

            "#03709F柯林也和村里的孩子们\x01",
            "交上了朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x17,
        (
            "#03809F#5P卡米尤和普莉\x01",
            "总是陪我一起玩～\x02\x03",

            "狗狗下次也来和我们一起玩吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x107,
        "#01200F#6P#3C呵呵，我考虑一下吧。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x15,
        (
            "#03609F#11P哈哈……谢谢。\x02\x03",

            "#03600F总之，事情就是这样。\x01",
            "我们为了回报村中的各位，\x01",
            "决定为大家做一些事情。\x02\x03",

            "#03604F话虽如此，但也只不过\x01",
            "是在国防军到来的时候，\x01",
            "负责与他们交涉而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x103,
        (
            "#00204F#6P在这种状况下，\x01",
            "交涉是非常重要的任务。\x02\x03",

            "#00202F像哈罗德先生这样\x01",
            "老练的商人，肯定很善于\x01",
            "与人交涉吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x15,
        (
            "#03600F#11P哈哈，这真的\x01",
            "不算什么啦。\x02",
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
            "#03605F#11P对了，在与国防军交涉的时候，\x01",
            "我听到了一件很令人在意的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        "#00005F#6P很令人在意的事情……？\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x15,
        (
            "#03610F#11P嗯，据说有一股\x01",
            "来历不明的反抗势力\x01",
            "潜伏在这附近。\x02\x03",

            "#03601F好像已经向国防军的部队\x01",
            "发动过多次袭击了。\x02",
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
        "#00011F#6P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x105,
        (
            "#10402F#6P嘿……在如此状况下，\x01",
            "竟然还有人做那种事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x103,
        (
            "#00201F#6P虽然不知是什么人……\x01",
            "但似乎是非常有价值的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯，我们有确认一番的必要。\x02\x03",

            "#00001F哈罗德先生，国防军是在什么地方\x01",
            "目击到那股反抗势力的？\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x15,
        (
            "#03610F#11P好像是在位于古道途中的\x01",
            "阿尔摩利卡古战场一带\x01",
            "目击到的。\x02\x03",

            "#03601F国防军会定期\x01",
            "去那里巡逻……\x01",
            "但似乎没有取得任何成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3C阿尔摩利卡古战场……\x01",
            "教团当年的根据地，\x01",
            "曾经数次血流成河的宿命之地吗……\x02\x03",

            "#01201F那座遗迹中有很多隐藏通路，\x01",
            "对反抗势力来说，\x01",
            "正是最合适的藏身之地。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        (
            "#00013F#6P虽然还不知他们究竟是什么人……\x01",
            "但我们准备完毕之后，就过去看看吧。\x02",
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

    # Function_45_C9AE end

    def Function_46_D85E(): pass

    label("Function_46_D85E")


    def lambda_D863():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D863)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 73000, 0, -500, 2000, 0x0)
    Return()

    # Function_46_D85E end

    def Function_47_D8A7(): pass

    label("Function_47_D8A7")


    def lambda_D8AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D8AC)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -1000, 2000, 0x0)
    OP_95(0xFE, 73750, 0, -1000, 2000, 0x0)
    Return()

    # Function_47_D8A7 end

    def Function_48_D8F0(): pass

    label("Function_48_D8F0")


    def lambda_D8F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D8F5)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 75000, 0, -500, 2000, 0x0)
    Return()

    # Function_48_D8F0 end

    def Function_49_D939(): pass

    label("Function_49_D939")


    def lambda_D93E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D93E)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
    OP_95(0xFE, 74250, 0, 0, 2000, 0x0)
    Return()

    # Function_49_D939 end

    SaveToFile()

Try(main)
