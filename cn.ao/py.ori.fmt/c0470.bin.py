from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0470.bin",                # FileName
        "c0470",                    # MapName
        "c0470",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0470",                  # 0
        "多雷克老板",             # 1
        "切莉",                   # 2
        "加雷提",                 # 3
        "艾琳迪",                 # 4
        "雷特罗莎",               # 5
        "利凯爷爷",               # 6
        "霍莉婆婆",               # 7
        "游客",                   # 8
        "矿工玛尔罗",             # 9
        "矿工冈兹",               # 10
        "尤利",                   # 11
        "塞克斯",                 # 12
        "瑞吉",                   # 13
        "雷克特",                 # 14
        "红发少女",               # 15
        "红发少女",               # 16
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch07402.itc",                   # 01
        "chr/ch33302.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch20002.itc",                   # 06
        "chr/ch33000.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch30702.itc",                   # 09
        "chr/ch44102.itc",                   # 0A
        "chr/ch47500.itc",                   # 0B
        "chr/ch23600.itc",                   # 0C
        "chr/ch20100.itc",                   # 0D
        "chr/ch20000.itc",                   # 0E
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1350,    -899,    11500,   0,    325,  0x0, 0,   2,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   14,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4239,    -1000,   13649,   225,  389,  0x0, 0,   13,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-3319,   -1000,   5599,    270,  389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(6690,    4000,    11539,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6690,    4269,    10460,   90,   453,  0x0, 0,   9,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(2480,    -1000,   11720,   225,  389,  0x0, 0,   10,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(4389,    -1000,   12359,   225,  389,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4239,    -1000,   13649,   225,  389,  0x0, 0,   12,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  4.0,                   3.5,                   4.5,                   225.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.6666666865348816,   -0.699999988079071,    -0.9000000357627869,   1.0])

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  6,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  12, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  27, 0x0000)

    ChipFrameInfo(1224, 0)                                       # 0

    ScpFunction((
        "Function_0_4C8",          # 00, 0
        "Function_1_578",          # 01, 1
        "Function_2_806",          # 02, 2
        "Function_3_906",          # 03, 3
        "Function_4_90A",          # 04, 4
        "Function_5_1DF9",         # 05, 5
        "Function_6_22B7",         # 06, 6
        "Function_7_22BB",         # 07, 7
        "Function_8_2F1B",         # 08, 8
        "Function_9_2F50",         # 09, 9
        "Function_10_2F54",        # 0A, 10
        "Function_11_3A67",        # 0B, 11
        "Function_12_3AF6",        # 0C, 12
        "Function_13_3AFA",        # 0D, 13
        "Function_14_4540",        # 0E, 14
        "Function_15_51D4",        # 0F, 15
        "Function_16_5E11",        # 10, 16
        "Function_17_5EDF",        # 11, 17
        "Function_18_612B",        # 12, 18
        "Function_19_6190",        # 13, 19
        "Function_20_61F7",        # 14, 20
        "Function_21_62C6",        # 15, 21
        "Function_22_637E",        # 16, 22
        "Function_23_64AF",        # 17, 23
        "Function_24_6509",        # 18, 24
        "Function_25_6564",        # 19, 25
        "Function_26_667C",        # 1A, 26
        "Function_27_7293",        # 1B, 27
        "Function_28_7322",        # 1C, 28
        "Function_29_7843",        # 1D, 29
        "Function_30_941D",        # 1E, 30
        "Function_31_9467",        # 1F, 31
        "Function_32_94B1",        # 20, 32
        "Function_33_94FB",        # 21, 33
        "Function_34_9545",        # 22, 34
        "Function_35_9594",        # 23, 35
        "Function_36_95B5",        # 24, 36
    ))


    def Function_0_4C8(): pass

    label("Function_0_4C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_500"),
        (1, "loc_50C"),
        (2, "loc_518"),
        (3, "loc_524"),
        (4, "loc_530"),
        (5, "loc_53C"),
        (6, "loc_548"),
        (SWITCH_DEFAULT, "loc_554"),
    )


    label("loc_500")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_50C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_518")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_524")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_530")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_53C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_548")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_554")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_560")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_577")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_577")

    Return()

    # Function_0_4C8 end

    def Function_1_578(): pass

    label("Function_1_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D0")
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrPos(0x15, 6540, 4270, 13420, 90)
    SetChrChipByIndex(0x15, 0x1)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetScenarioFlags(0x1, 2)

    label("loc_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EB")
    SetChrChipByIndex(0xC, 0x2)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_606")
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_680")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -800, -1000, 7000, 90)
    SetChrPos(0xD, 800, -1000, 7000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_64F")

    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrPos(0x15, 6700, 4270, 15750, 90)
    SetChrChipByIndex(0x15, 0x1)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jump("loc_805")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_69D")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_805")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6CB")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_805")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6D9")
    Jump("loc_805")

    label("loc_6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6E7")
    Jump("loc_805")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6F5")
    Jump("loc_805")

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_708")
    SetChrFlags(0xD, 0x10)
    Jump("loc_805")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_716")
    Jump("loc_805")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_77C")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrPos(0x12, -3460, -850, 12370, 45)
    SetChrPos(0x14, -3120, -1000, 10900, 90)
    SetChrPos(0x13, -4310, -1000, 12730, 90)
    Jump("loc_805")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78A")
    Jump("loc_805")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7BD")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    Jump("loc_805")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D5")
    SetChrFlags(0xD, 0x10)

    label("loc_7D5")

    Jump("loc_805")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7FC")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xF, 0x10)
    Jump("loc_805")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_805")

    label("loc_805")

    Return()

    # Function_1_578 end

    def Function_2_806(): pass

    label("Function_2_806")

    SetMapObjFrame(0xFF, "white00", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84E")
    ModifyEventFlags(1, 0, 0x80)
    SetMapObjFrame(0xFF, "white00", 0x0, 0x2)

    label("loc_84E")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_864")
    OP_65(0x7, 0x1)

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_876")
    OP_65(0x7, 0x1)

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88C")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A8")
    OP_10(0x0, 0x0)
    OP_10(0x4, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_8CD")

    label("loc_8A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8C4")
    OP_10(0x0, 0x0)
    OP_10(0x4, 0x1)
    OP_10(0x3, 0x0)
    Jump("loc_8CD")

    label("loc_8C4")

    OP_10(0x0, 0x1)
    OP_10(0x4, 0x0)
    OP_10(0x3, 0x0)

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EE")
    Sound(128, 1, 30, 0)

    label("loc_8EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_905")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_905")

    Return()

    # Function_2_806 end

    def Function_3_906(): pass

    label("Function_3_906")

    Call(0, 4)
    Return()

    # Function_3_906 end

    def Function_4_90A(): pass

    label("Function_4_90A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91C")
    Call(0, 28)
    Return()

    label("loc_91C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA7")
    TurnDirection(0x8, 0x104, 0)

    #C0001
    ChrTalk(
        0x8,
        (
            "……兰迪，你要前往\x01",
            "那棵大树了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#00300F哈哈，你连这都知道了啊，\x01",
            "不愧是多雷克老板。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "哼，因为和你来往的时间\x01",
            "已经不算短了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……兰迪，\x01",
            "你以前赊帐喝酒\x01",
            "欠下的钱还没还清呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "你可得向我保证，\x01",
            "一定要平安回来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00304F……嗯，我知道。\x02\x03",

            "#00309F到时一定会全部还上的，\x01",
            "你就放心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈……他们两人\x01",
            "  还真是心照不宣呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 0)
    Jump("loc_BD8")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B86")

    #C0008
    ChrTalk(
        0x8,
        (
            "现在正是克洛斯贝尔\x01",
            "需要接受试炼的时刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "……各位，兰迪\x01",
            "就托付给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "那小子以前\x01",
            "赊帐喝酒欠下的钱\x01",
            "还没还清呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#00003F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#00309F到时一定会全部还上的，\x01",
            "你就放心吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BD8")

    label("loc_B86")


    #C0013
    ChrTalk(
        0x8,
        (
            "现在正是克洛斯贝尔\x01",
            "需要接受试炼的时刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "……各位，兰迪\x01",
            "就托付给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD8")

    Jump("loc_1DF5")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D44")

    #C0015
    ChrTalk(
        0x8,
        "哦哦，是你们……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00300F好久不见啦，老板。\x01",
            "看样子，你好像还挺有精神嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)

    #C0017
    ChrTalk(
        0x8,
        "你也一样啊，兰迪。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "听说你之前投身于\x01",
            "玛因兹的反抗活动了，\x01",
            "如今能和同伴会合，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00000F这里还没有出现\x01",
            "什么问题吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0020
    ChrTalk(
        0x8,
        "嗯，暂时还没。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "各位，如果你们要在市内行动，\x01",
            "一定要十分小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        "#00300F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 7)
    Jump("loc_EB1")

    label("loc_D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")

    #C0023
    ChrTalk(
        0x8,
        (
            "话说回来，自从戒严令下达之后，\x01",
            "我们缩小了营业规模，看来确实是正确选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "现在的客人和工作人员都比较少，凭借店里目前的储备，\x01",
            "应该可以再支撑一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "请不用担心我们，\x01",
            "大家专心做好\x01",
            "自己的工作就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB1")

    label("loc_E2A")


    #C0026
    ChrTalk(
        0x8,
        (
            "现在的客人和工作人员都比较少，凭借店里目前的储备，\x01",
            "应该可以再支撑一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "请不用担心我们，\x01",
            "大家专心做好\x01",
            "自己的工作就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB1")

    Jump("loc_1DF5")

    label("loc_EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F78")

    #C0028
    ChrTalk(
        0x8,
        (
            "唔……从早上开始，就有一群\x01",
            "穿着陌生制服的家伙到处巡逻，\x01",
            "那就是国防军的士兵吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "准备还真是\x01",
            "充分啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "库罗伊斯究竟\x01",
            "从何时开始就已经\x01",
            "在策划如今的剧本了？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FE3")

    label("loc_F78")


    #C0031
    ChrTalk(
        0x8,
        (
            "仔细想想，居民投票活动\x01",
            "才刚刚过去一周而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "库罗伊斯究竟\x01",
            "从何时开始就已经\x01",
            "在策划如今的剧本了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE3")

    Jump("loc_1DF5")

    label("loc_FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120C")

    #C0033
    ChrTalk(
        0x8,
        (
            "哦，兰迪。\x01",
            "虽然不知道发生了什么事，\x01",
            "但看你的表情，似乎下定了什么决心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "因为这种状况，\x01",
            "店里现在冷冷清清的，\x01",
            "你到底来干什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00305F嗯？我觉得\x01",
            "和平时没什么不同啊。\x02\x03",

            "#00309F对了，老板，\x01",
            "我短时间内大概不会露面了，\x01",
            "到时你可不要寂寞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "哼，说什么蠢话。\x01",
            "你这烦人的小子不来了，\x01",
            "我只会感到愉快而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "总之，你以前还\x01",
            "赊了不少帐没还呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "在全部还清之前，\x01",
            "可别丢了小命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00300F哈，不用你说我也知道啦。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000F（这两个人的关系\x01",
            "  似乎很好呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00100F（嗯，简直就像小孩子斗嘴一样。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 1)
    Jump("loc_126B")

    label("loc_120C")


    #C0042
    ChrTalk(
        0x8,
        (
            "总之，兰迪你以前还\x01",
            "欠了不少帐没还呢，\x01",
            "可别忘了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "虽然没有严格期限，\x01",
            "但你一定要还清。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126B")

    Jump("loc_1DF5")

    label("loc_1270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_137E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131E")

    #C0044
    ChrTalk(
        0x8,
        (
            "我能为他做的，\x01",
            "也只是提供一个\x01",
            "喝酒的地方而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "而你们却能真正意义上的\x01",
            "为他提供帮助，\x01",
            "我有这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "各位……\x01",
            "兰迪就托付给你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1379")

    label("loc_131E")


    #C0047
    ChrTalk(
        0x8,
        (
            "你们可以真正意义上的\x01",
            "为他提供帮助，\x01",
            "我有这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "各位……\x01",
            "兰迪就托付给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1379")

    Jump("loc_1DF5")

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143F")

    #C0049
    ChrTalk(
        0x8,
        (
            "新版舞剧终于\x01",
            "要在明天公演了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "据说，继莉夏·毛之后，\x01",
            "又有一位超级新人要在\x01",
            "这次的表演中首度登台亮相了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "呵呵，彩虹剧团总能为我们\x01",
            "带来很有趣的话题啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C0")

    label("loc_143F")


    #C0052
    ChrTalk(
        0x8,
        (
            "据说，继莉夏·毛之后，\x01",
            "又有一位超级新人要在\x01",
            "这次的表演中首度登台亮相了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "呵呵，彩虹剧团总能为我们\x01",
            "带来很有趣的话题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C0")

    Jump("loc_1DF5")

    label("loc_14C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155F")

    #C0054
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎光临『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "如果想放松一下心情，\x01",
            "可以来吧台喝上一杯。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "各种酒自不必说，\x01",
            "咖啡等饮料也可以提供哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15BD")

    label("loc_155F")


    #C0057
    ChrTalk(
        0x8,
        (
            "如果想放松一下心情，\x01",
            "可以来吧台喝上一杯。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "各种酒自不必说，\x01",
            "咖啡等饮料也可以提供哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BD")

    Jump("loc_1DF5")

    label("loc_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B4")

    #C0059
    ChrTalk(
        0x8,
        (
            "独立的利弊吗……\x01",
            "地下世界的状况如今仍然不平稳，\x01",
            "而这个问题也同样麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "居民投票的结果应该不会\x01",
            "立刻导致什么情况……\x01",
            "主要问题还是两大国的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "如果处理不善，克洛斯贝尔的状况\x01",
            "很可能会比以往更加恶劣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_173D")

    label("loc_16B4")


    #C0062
    ChrTalk(
        0x8,
        (
            "居民投票的结果应该不会\x01",
            "立刻导致什么情况……\x01",
            "主要问题还是两大国的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "如果处理不善，克洛斯贝尔的状况\x01",
            "很可能会比以往更加恶劣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173D")

    Jump("loc_1DF5")

    label("loc_1742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17AE")

    #C0064
    ChrTalk(
        0x8,
        (
            "嗯？一层好像\x01",
            "有点吵闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "如果再这么吵闹下去，\x01",
            "就要将那些喧哗的客人婉言请出去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF5")

    label("loc_17AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1816")

    #C0066
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎光临『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "要不要来杯甜美的鸡尾酒？\x01",
            "它会使你的身心全部溶化哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF5")

    label("loc_1816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1875")

    #C0068
    ChrTalk(
        0x8,
        (
            "兰花塔的揭幕式\x01",
            "似乎已经在盛况中结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "呵呵，我以后有空时也要去看看。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DF5")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A31")
    TurnDirection(0x8, 0x104, 0)

    #C0070
    ChrTalk(
        0x8,
        (
            "哦，兰迪，\x01",
            "昨天的酒已经醒了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#00302F哈，那还用说。\x01",
            "只喝了那么一点点而已，\x01",
            "你难道以为我会醉到第二天吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "哼，你还是老样子，\x01",
            "油腔滑调的。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "虽说是庆祝你复归，\x01",
            "但竟然让我请客。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00304F哈哈，真不好意思，\x01",
            "但我很感谢你哦。\x02\x03",

            "#00300F好啦，老板，\x01",
            "以后要是有机会，就请你继续请客吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "哼，胡说八道。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#00100F（兰迪还真是见缝插针，\x01",
            "  一有空就来这里呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00000F（嗯，是啊。）\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x14C, 2)
    Jump("loc_1B47")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD7")
    TurnDirection(0x8, 0x104, 0)

    #C0078
    ChrTalk(
        0x8,
        (
            "算啦，如果还想让我请客，\x01",
            "你就改改那油腔滑调的坏毛病。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "如果你做得到，\x01",
            "我也不是不能考虑。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00304F遵命遵命，\x01",
            "我会努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B47")

    label("loc_1AD7")

    TurnDirection(0x8, 0x104, 0)

    #C0081
    ChrTalk(
        0x8,
        (
            "算啦，如果还想让我请客，\x01",
            "你就改改那油腔滑调的坏毛病。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "如果你做得到，\x01",
            "我也不是不能考虑。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_1B47")

    Jump("loc_1DF5")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B67")
    Call(0, 5)
    Jump("loc_1D69")

    label("loc_1B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD5")

    #C0083
    ChrTalk(
        0x8,
        (
            "最近这段时间，\x01",
            "由于鲁巴彻已经覆灭，所以开始有\x01",
            "小杂鱼来征收保护费了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "现在倒是还无所谓，\x01",
            "但如果这种状况一直持续下去，\x01",
            "大概会出现很多麻烦事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "哎呀呀，随便是谁都好，\x01",
            "真希望有人能尽快\x01",
            "继承鲁巴彻的霸权啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#10103F（鲁巴彻的覆灭，\x01",
            "  对这种地方也造成了影响……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#00000F（鲁巴彻也在某种程度上维持着秩序，\x01",
            "  这就是体现之一吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D69")

    label("loc_1CD5")


    #C0088
    ChrTalk(
        0x8,
        (
            "那些家伙现在\x01",
            "还不算太过嚣张……\x01",
            "但如果这种状况一直持续下去，终究是有些麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "哎呀呀，随便是谁都好，\x01",
            "真希望有人能尽快\x01",
            "继承鲁巴彻的霸权啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D69")

    Jump("loc_1DF5")

    label("loc_1D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D89")
    Call(0, 5)
    Jump("loc_1DF5")

    label("loc_1D89")


    #C0090
    ChrTalk(
        0x8,
        (
            "兰迪那家伙，好像和警备队的人在一起，\x01",
            "做得很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "呵呵，希望他别再像以前那样，\x01",
            "说些丢脸的话了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF5")

    TalkEnd(0x8)
    Return()

    # Function_4_90A end

    def Function_5_1DF9(): pass

    label("Function_5_1DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2185")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0092
    ChrTalk(
        0x8,
        (
            "特别任务支援科的各位……\x01",
            "还有瓦吉先生也在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "真是奇妙的组合。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#10300F哦，老板，\x01",
            "其实我已经被配属到\x01",
            "特别任务支援科了。\x02\x03",

            "详细经过就略去不谈了，\x01",
            "总之，今后还请多关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "原来如此，是这样啊……\x01",
            "呵呵，明白了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#00105F好、好像完全不吃惊呢。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00000F是啊……\x01",
            "瓦吉想必和老板\x01",
            "很熟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        (
            "#10304F嗯，对男公关来说，\x01",
            "这一带都算是\x01",
            "工作场所。\x02\x03",

            "#10300F而且，身为一名男公关，\x01",
            "如果连多雷克老板都不认识，\x01",
            "那也只能算是三流了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x109,
        (
            "#10106F说得真坦然啊……\x02\x03",

            "#10101F你这个年纪就\x01",
            "长期混迹在这类场所，\x01",
            "再怎么说也不太好吧。\x02\x03",

            "#10103F趁着这次的机会，你多少也该……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，还是和以前一样死板啊。\x02\x03",

            "算啦，这也正是\x01",
            "你的魅力之一⊥\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C3")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_20C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E9")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_20E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210F")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_210F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2135")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2135")

    Sleep(1000)

    #C0101
    ChrTalk(
        0x109,
        (
            "#10106F呼，我已经\x01",
            "什么都不想管了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        "#00106F我理解你的心情。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 7)
    Jump("loc_22B6")

    label("loc_2185")


    #C0103
    ChrTalk(
        0x8,
        (
            "对了，\x01",
            "兰迪那小子\x01",
            "还没回来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "之前听他本人说，要回\x01",
            "以前所在的警备队露个面。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00000F是的，再过不久，\x01",
            "他就会回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "原来如此，那能不能\x01",
            "帮我转告他，让他回来以后\x01",
            "顺便来店里看看？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "为了庆祝他的复归，\x01",
            "我会准备一瓶葡萄酒的。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00000F好，知道了。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#00100F我们一定会转告他的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 6)

    label("loc_22B6")

    Return()

    # Function_5_1DF9 end

    def Function_6_22B7(): pass

    label("Function_6_22B7")

    Call(0, 7)
    Return()

    # Function_6_22B7 end

    def Function_7_22BB(): pass

    label("Function_7_22BB")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F17")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "交换\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2318")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2318")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2337")
    OP_AF(0x41)
    Jump("loc_2379")

    label("loc_2337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2347")
    OP_AF(0x40)
    Jump("loc_2379")

    label("loc_2347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2357")
    OP_AF(0x3F)
    Jump("loc_2379")

    label("loc_2357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2367")
    OP_AF(0x3E)
    Jump("loc_2379")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2377")
    OP_AF(0x3D)
    Jump("loc_2379")

    label("loc_2377")

    OP_AF(0x3C)

    label("loc_2379")

    Call(0, 8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F12")

    label("loc_238B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239F")
    Jump("loc_2F12")

    label("loc_239F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F12")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2429")

    #C0110
    ChrTalk(
        0x9,
        (
            "欢迎，\x01",
            "欢迎光临『巴鲁卡』～！\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "在这里玩个痛快，\x01",
            "让不安的心情飞到九霄云外吧☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_248F")

    label("loc_2429")


    #C0112
    ChrTalk(
        0x9,
        (
            "虽然现在的状况比较特殊，\x01",
            "但我们还是照常营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "在这里玩个痛快，\x01",
            "让不安的心情飞到九霄云外吧☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_248F")

    Jump("loc_2F12")

    label("loc_2494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_25B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2524")

    #C0114
    ChrTalk(
        0x9,
        (
            "呜呜，真是害怕……\x01",
            "但能让加雷提先生和艾琳迪小姐\x01",
            "回家去休息真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "老板非常努力，\x01",
            "我也要振作起来才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25AF")

    label("loc_2524")


    #C0116
    ChrTalk(
        0x9,
        (
            "加雷提先生和艾琳迪小姐回去休息了，\x01",
            "所以现在不能在一层玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "但我这里的奖品中\x01",
            "说不定有一些有用的东西，\x01",
            "大家可以像平时一样兑换哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AF")

    Jump("loc_2F12")

    label("loc_25B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_261A")

    #C0118
    ChrTalk(
        0x9,
        (
            "唔～不会突然间\x01",
            "就发生战争吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "面对这种状况，两大国\x01",
            "究竟会发表怎样的声明呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_261A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2683")

    #C0120
    ChrTalk(
        0x9,
        "唔～居民投票吗～？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "虽然设立了很多个投票点，\x01",
            "但要投的话，显然还是要去兰花塔啊～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_2683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_26EB")

    #C0122
    ChrTalk(
        0x9,
        (
            "唔～虽说发生在市外，\x01",
            "但玛因兹的事情\x01",
            "终究不是事不关己啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        "真希望能早点顺利解决。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_26EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2770")

    #C0124
    ChrTalk(
        0x9,
        (
            "彩虹剧团的演出\x01",
            "终于要在明天开始了～\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "到时肯定又会有很多客人\x01",
            "来我们这里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        "呵呵，好期待～⊥\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27C1")

    label("loc_2770")


    #C0127
    ChrTalk(
        0x9,
        (
            "在观赏过彩虹剧团的表演之后，\x01",
            "很多人都会来我们这里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        "呵呵，好期待～⊥\x02",
    )

    CloseMessageWindow()

    label("loc_27C1")

    Jump("loc_2F12")

    label("loc_27C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_282A")

    #C0129
    ChrTalk(
        0x9,
        (
            "如果把代币用完了，\x01",
            "随时可以和我说哦～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "如果把米拉用光了，\x01",
            "就去ＩＢＣ取吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_282A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2879")

    #C0131
    ChrTalk(
        0x9,
        "欢迎光临『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "呵呵呵，今天也要\x01",
            "玩个痛快啊～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_2879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28F6")

    #C0133
    ChrTalk(
        0x9,
        (
            "那个三人组\x01",
            "好像很有钱，\x01",
            "但感觉真是很讨厌呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "他们一副很高傲的样子邀请我，\x01",
            "我当然是客气地回绝了他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_28F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2960")

    #C0135
    ChrTalk(
        0x9,
        (
            "通商会议终于要在今天\x01",
            "进入重头部分了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "我虽然不是很了解，\x01",
            "但还是希望能进展顺利啊⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_2960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2F")

    #C0137
    ChrTalk(
        0x9,
        (
            "冈兹先生还是不接受教训，\x01",
            "今天又去老虎机前\x01",
            "奋力拼搏了～\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "他几个月之前的那种\x01",
            "惊人好运气似乎已经\x01",
            "彻底消失了……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "莫非冈兹先生\x01",
            "在那个时候已经把\x01",
            "一辈子的好运气都用光了～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AA7")

    label("loc_2A2F")


    #C0140
    ChrTalk(
        0x9,
        (
            "莫非冈兹先生\x01",
            "在那个时候已经把\x01",
            "一辈子的好运气都用光了～？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "哈～不过他偶尔\x01",
            "也能赢上两局，\x01",
            "好像还不至于那么严重。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA7")

    Jump("loc_2F12")

    label("loc_2AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C81")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 0)

    #C0142
    ChrTalk(
        0x9,
        "啊，兰迪先生～\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "真是的，你最近到底去哪里了～\x01",
            "真过分，要多来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#00304F真是抱歉啊，小切莉。\x02\x03",

            "#00309F好，那就先把工作扔到一边……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF1")

    #C0145
    ChrTalk(
        0x101,
        "#00009F喂，兰迪……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#00109F呵呵，只是开个玩笑吧？\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        (
            "#00306F啊……嗯嗯……\x01",
            "真是的，你们两个的笑容好可怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C79")

    label("loc_2BF1")


    #C0148
    ChrTalk(
        0x102,
        (
            "#00109F喂，兰迪，\x01",
            "你刚才说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#00306F啊……嗯嗯……\x01",
            "都说了只是玩笑而已啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        (
            "#10106F（兰迪前辈……\x01",
            "  真是不知悔改呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C79")

    SetScenarioFlags(0x14C, 3)
    Jump("loc_2CC9")

    label("loc_2C81")


    #C0151
    ChrTalk(
        0x9,
        (
            "兰迪先生，\x01",
            "以后一定要多来玩啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "要是你不来，\x01",
            "切莉会很无聊的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC9")

    Jump("loc_2F12")

    label("loc_2CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D33")

    #C0153
    ChrTalk(
        0x9,
        (
            "湿漉漉的雨水让人心烦意乱，\x01",
            "在巴鲁卡转换一下心情吧～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        "今天也要玩个痛快哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_2D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF2")

    #C0155
    ChrTalk(
        0x9,
        (
            "雷克特先生刚才\x01",
            "突然来了，\x01",
            "直接上了二层。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "呵呵，几个月不见，\x01",
            "他还是一样奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        "#00101F罗伊德……！\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#00001F嗯，这次一定不能再让他逃走。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E4B")

    label("loc_2DF2")


    #C0159
    ChrTalk(
        0x9,
        (
            "雷克特先生刚才\x01",
            "突然来了，\x01",
            "直接上了二层。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "呵呵，几个月不见，\x01",
            "他还是一样奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4B")

    Jump("loc_2F12")

    label("loc_2E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC8")

    #C0161
    ChrTalk(
        0x9,
        "欢迎光临『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "这里是交换代币和\x01",
            "兑换奖品的柜台哦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        (
            "多玩一玩，\x01",
            "换些好奖品吧～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F12")

    label("loc_2EC8")


    #C0164
    ChrTalk(
        0x9,
        (
            "这里是交换代币和\x01",
            "兑换奖品的柜台哦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "多玩一玩，\x01",
            "换些好奖品吧～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F12")

    Jump("loc_22C8")

    label("loc_2F17")

    TalkEnd(0x9)
    Return()

    # Function_7_22BB end

    def Function_8_2F1B(): pass

    label("Function_8_2F1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F4F")
    SubItemNumber(0x18C, 1)
    AddItemNumber(0x186, 1)
    AddItemNumber(0x187, 1)
    AddItemNumber(0x188, 1)
    AddItemNumber(0x189, 1)
    AddItemNumber(0x18A, 1)
    Jump("Function_8_2F1B")

    label("loc_2F4F")

    Return()

    # Function_8_2F1B end

    def Function_9_2F50(): pass

    label("Function_9_2F50")

    Call(0, 10)
    Return()

    # Function_9_2F50 end

    def Function_10_2F54(): pass

    label("Function_10_2F54")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A63")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "玩扑克\x01",          # 1
            "玩二十一点\x01",      # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FBE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2FBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3013")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3013")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3068")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3068")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307C")
    Jump("loc_3A5E")

    label("loc_307C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_31C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3140")

    #C0166
    ChrTalk(
        0xA,
        (
            "老顾客雷特罗莎小姐\x01",
            "回国了，\x01",
            "真是寂寞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "和她比赛始终刺激不断，\x01",
            "每天都过得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "等克洛斯贝尔恢复和平以后，\x01",
            "希望她再来这里玩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_31BD")

    label("loc_3140")


    #C0169
    ChrTalk(
        0xA,
        (
            "等克洛斯贝尔恢复和平以后，\x01",
            "希望老顾客雷特罗莎小姐\x01",
            "再来这里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "在那棵来历不明的大树\x01",
            "消失之前，大概是很困难了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BD")

    Jump("loc_3A5E")

    label("loc_31C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_31D0")
    Jump("loc_3A5E")

    label("loc_31D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_330F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3296")

    #C0171
    ChrTalk(
        0xA,
        (
            "听说从今天早上开始，\x01",
            "导力铁路的运行就受到限制了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "身在克洛斯贝尔的\x01",
            "帝国人和共和国人都接到了\x01",
            "来自本国的归国劝告……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "事态的发展速度\x01",
            "似乎比想象中的\x01",
            "还要快呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_330A")

    label("loc_3296")


    #C0174
    ChrTalk(
        0xA,
        (
            "身在克洛斯贝尔的\x01",
            "帝国人和共和国人都接到了\x01",
            "来自本国的归国劝告……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "事态的发展速度\x01",
            "似乎比想象中的\x01",
            "还要快呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330A")

    Jump("loc_3A5E")

    label("loc_330F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F1")

    #C0176
    ChrTalk(
        0xA,
        (
            "现在再看看残留在地面上的焦痕……\x01",
            "我还是会回想起遭受袭击时的场面。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "万幸武装集团\x01",
            "当时并没有闯进\x01",
            "本店……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "如果他们当时进来袭击，\x01",
            "我们还不知会遭遇到什么下场呢……\x01",
            "光是想想就觉得很可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3471")

    label("loc_33F1")


    #C0179
    ChrTalk(
        0xA,
        (
            "万幸武装集团\x01",
            "当时并没有闯进\x01",
            "本店……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "如果他们当时进来袭击，\x01",
            "我们还不知会遭遇到什么下场呢……\x01",
            "光是想想就觉得很可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3471")

    Jump("loc_3A5E")

    label("loc_3476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3505")

    #C0181
    ChrTalk(
        0xA,
        (
            "如今已有传闻说，袭击事件是由\x01",
            "帝国政府一手策划的。\x01",
            "这样考虑应该是很合理的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "总之，帝国下一步的行动\x01",
            "真是很让人在意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5E")

    label("loc_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3585")

    #C0183
    ChrTalk(
        0xA,
        (
            "独立的利弊……\x01",
            "居民投票日好像\x01",
            "已经临近了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "唔，哪个选择才能\x01",
            "带来更好的结果呢……\x01",
            "我还要再考虑一阵子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5E")

    label("loc_3585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_35F6")

    #C0185
    ChrTalk(
        0xA,
        (
            "平淡无奇的人生和丰富刺激的人生，\x01",
            "究竟哪个才是真正的幸福呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        "呵呵，客人您又是怎么想的？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A5E")

    label("loc_35F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3667")

    #C0187
    ChrTalk(
        0xA,
        (
            "输了就垂头丧气或大发脾气，\x01",
            "那只能算是二流人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "希望各位客人能\x01",
            "心怀诚意地\x01",
            "享受游戏过程。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5E")

    label("loc_3667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_379F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3721")

    #C0189
    ChrTalk(
        0xA,
        (
            "（他们从刚才开始就一直在大声喧哗，\x01",
            "  打扰其他客人……）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "（那些客人好像\x01",
            "  没什么修养啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        (
            "（如果他们的行为太过分，\x01",
            "  就必须要给予严重警告了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_379A")

    label("loc_3721")


    #C0192
    ChrTalk(
        0xA,
        (
            "（虽说这里是娱乐场所，\x01",
            "  但娱乐场所也有\x01",
            "  自己的规矩。）\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "（如果他们的行为太过分，\x01",
            "  就必须要给予严重警告了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_379A")

    Jump("loc_3A5E")

    label("loc_379F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_380E")

    #C0194
    ChrTalk(
        0xA,
        (
            "迪塔市长赌博\x01",
            "时的样子吗……\x01",
            "哎呀呀，该怎么说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "他在赌博的时候，\x01",
            "也让人觉得很精明呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5E")

    label("loc_380E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_38FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A0")

    #C0196
    ChrTalk(
        0xA,
        (
            "今天又看到冈兹先生\x01",
            "来玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "之前有一段时间，\x01",
            "他的超强好运简直让人震惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        (
            "但现在已经完全\x01",
            "恢复原状了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38F9")

    label("loc_38A0")


    #C0199
    ChrTalk(
        0xA,
        (
            "冈兹先生以前\x01",
            "有段时间的超强好运\x01",
            "简直让人震惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "但现在已经完全\x01",
            "恢复原状了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F9")

    Jump("loc_3A5E")

    label("loc_38FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3992")

    #C0201
    ChrTalk(
        0xA,
        (
            "听说那个高级俱乐部\x01",
            "『诺艾·布朗』\x01",
            "已经装修完毕，重新开始营业了。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        (
            "像我这样的人，\x01",
            "与那种地方恐怕永远无缘……\x01",
            "但真想去一次啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5E")

    label("loc_3992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39AD")
    Call(0, 11)
    Jump("loc_3A11")

    label("loc_39AD")


    #C0203
    ChrTalk(
        0xA,
        (
            "哎呀呀，雷特罗莎小姐\x01",
            "真是胆大心细。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "结果比过程更重要……\x01",
            "笑到最后的人才是真正的胜利者啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A11")

    Jump("loc_3A5E")

    label("loc_3A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A5E")

    #C0205
    ChrTalk(
        0xA,
        (
            "欢迎，\x01",
            "这里是扑克台。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        "如果有兴趣，来和我比一场如何？\x02",
    )

    CloseMessageWindow()

    label("loc_3A5E")

    Jump("loc_2F61")

    label("loc_3A63")

    TalkEnd(0xA)
    Return()

    # Function_10_2F54 end

    def Function_11_3A67(): pass

    label("Function_11_3A67")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0207
    ChrTalk(
        0xA,
        (
            "……真遗憾，这场比赛\x01",
            "是我赢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xC,
        (
            "呵呵，很有一套嘛，\x01",
            "但下局可就没这么简单啦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        "呵呵，请手下留情。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_3A67 end

    def Function_12_3AF6(): pass

    label("Function_12_3AF6")

    Call(0, 13)
    Return()

    # Function_12_3AF6 end

    def Function_13_3AFA(): pass

    label("Function_13_3AFA")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_453C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",        # 0
            "玩轮盘\x01",      # 1
            "放弃\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B59")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3B59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BAE")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_3BAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC2")
    Jump("loc_4537")

    label("loc_3BC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4537")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C99")

    #C0210
    ChrTalk(
        0xB,
        (
            "在这种时期来娱乐场所……\x01",
            "并不是什么\x01",
            "错事哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xB,
        (
            "娱乐活动正是为了\x01",
            "让人忘却不安的心情，\x01",
            "变得轻松愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "所以，在不安的时候，\x01",
            "希望各位能多多享受娱乐活动。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D0A")

    label("loc_3C99")


    #C0213
    ChrTalk(
        0xB,
        (
            "娱乐活动正是为了\x01",
            "让人忘却不安的心情，\x01",
            "变得轻松愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xB,
        (
            "所以，在不安的时候，\x01",
            "希望各位能多多享受娱乐活动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0A")

    Jump("loc_4537")

    label("loc_3D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3D1D")
    Jump("loc_4537")

    label("loc_3D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE1")

    #C0215
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔独立的问题\x01",
            "终于还是发展到了\x01",
            "无法回头的地步啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        (
            "我并不认为迪塔总统\x01",
            "会在毫无胜算的情况下，\x01",
            "将事态引发到如今的状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        (
            "他究竟藏着\x01",
            "什么样的底牌呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E4C")

    label("loc_3DE1")


    #C0218
    ChrTalk(
        0xB,
        (
            "我并不认为迪塔总统\x01",
            "会在毫无胜算的情况下，\x01",
            "将事态引发到如今的状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "他究竟藏着\x01",
            "什么样的底牌呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E4C")

    Jump("loc_4537")

    label("loc_3E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F08")

    #C0220
    ChrTalk(
        0xB,
        (
            "居民投票活动终于要在\x01",
            "三天之后开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xB,
        (
            "虽然结果已经显而易见了，\x01",
            "但我还是准备在活动当天\x01",
            "前去参加投票。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        (
            "至于究竟投什么票……\x01",
            "请容我暂时保密吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F79")

    label("loc_3F08")


    #C0223
    ChrTalk(
        0xB,
        (
            "虽然结果已经显而易见了，\x01",
            "但我还是准备在活动当天\x01",
            "前去参加投票。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xB,
        (
            "至于究竟投什么票……\x01",
            "请容我暂时保密吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F79")

    Jump("loc_4537")

    label("loc_3F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3FD8")

    #C0225
    ChrTalk(
        0xB,
        (
            "多雷克老板今天\x01",
            "好像有点昏昏欲睡呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "他昨天是不是又喝酒\x01",
            "到很晚呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_3FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_403C")

    #C0227
    ChrTalk(
        0xB,
        (
            "遇到这种下雨天，\x01",
            "就请在本店愉快度过吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        (
            "呵呵呵，说不定能得到些\x01",
            "特别服务哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_403C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_40CA")

    #C0229
    ChrTalk(
        0xB,
        (
            "玩游戏也好，做其它事情也好……\x01",
            "最重要的就是要学会适时收手。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xB,
        (
            "有句话叫『见好就收』，\x01",
            "如果太过贪婪，多半会以失败告终哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_40CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4149")

    #C0231
    ChrTalk(
        0xB,
        (
            "我认为人类就是一种\x01",
            "追求刺激的生物。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xB,
        (
            "客人，您也来比试一场如何？\x01",
            "我会把最强烈的刺激感\x01",
            "当作礼物送给您哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_4149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41AB")

    #C0233
    ChrTalk(
        0xB,
        "克洛斯贝尔的独立吗……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xB,
        (
            "真是的，迪塔市长\x01",
            "给我们出了一道\x01",
            "十分棘手的难题啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_41AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4213")

    #C0235
    ChrTalk(
        0xB,
        (
            "呵呵呵，终于迎来\x01",
            "正式会议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        (
            "我从现在就开始期待\x01",
            "下一期的克洛斯贝尔时代周刊了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_4213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4290")

    #C0237
    ChrTalk(
        0xB,
        (
            "我虽然还没有亲眼见到，\x01",
            "但听说兰花塔是一座\x01",
            "非常雄伟的大楼。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xB,
        (
            "高达四十层的摩天大楼……\x01",
            "真想亲眼看看啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_4290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4360")

    #C0239
    ChrTalk(
        0xB,
        (
            "迪塔市长发起的国际会议\x01",
            "终于要开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "互相揣摩对方的想法，\x01",
            "留存各种各样的王牌，\x01",
            "在最关键的时刻打出……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xB,
        (
            "虽然这样说可能有些不妥，\x01",
            "但我觉得外交的本质\x01",
            "与赌博是相同的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_43C2")

    label("loc_4360")


    #C0242
    ChrTalk(
        0xB,
        (
            "亲自设置了这次赌局的迪塔市长\x01",
            "手中究竟藏有\x01",
            "什么样的王牌呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        "呵呵，真是让人兴趣十足啊。\x02",
    )

    CloseMessageWindow()

    label("loc_43C2")

    Jump("loc_4537")

    label("loc_43C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_441B")

    #C0244
    ChrTalk(
        0xB,
        "呵呵，客人，您也来比试一场如何？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xB,
        "我会带领您进入思考的迷宫。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4537")

    label("loc_441B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D6")

    #C0246
    ChrTalk(
        0xB,
        (
            "欢迎光临『巴鲁卡』，\x01",
            "在这里可以享受轮盘游戏哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xB,
        (
            "话说在先，\x01",
            "在这轮盘上，绝对没有\x01",
            "安置任何作弊类的小装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "如何？要不要试着\x01",
            "将一切都交给命运呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4537")

    label("loc_44D6")


    #C0249
    ChrTalk(
        0xB,
        (
            "把代币压在高概率的小奖也好……\x01",
            "压在低概率的大奖也罢……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xB,
        "一切结果都只有女神才能知道哦。\x02",
    )

    CloseMessageWindow()

    label("loc_4537")

    Jump("loc_3B07")

    label("loc_453C")

    TalkEnd(0xB)
    Return()

    # Function_13_3AFA end

    def Function_14_4540(): pass

    label("Function_14_4540")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4551")
    Jump("loc_51D0")

    label("loc_4551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_465F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4602")

    #C0251
    ChrTalk(
        0xFE,
        (
            "那段时间我正好不在，\x01",
            "听说在一周前发生了\x01",
            "很严重的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "今后也未必不会再度发生\x01",
            "同样的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "看来以后还是尽量不要\x01",
            "来克洛斯贝尔玩了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_465A")

    label("loc_4602")


    #C0254
    ChrTalk(
        0xFE,
        (
            "今后也未必不会再度发生\x01",
            "同样的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "看来以后还是尽量不要\x01",
            "来克洛斯贝尔玩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_465A")

    Jump("loc_51D0")

    label("loc_465F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46D8")

    #C0256
    ChrTalk(
        0xFE,
        (
            "神秘武装集团的目的\x01",
            "到底是什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "如果今后有哪个势力\x01",
            "提出了某些要求，\x01",
            "答案也就不言自明了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D0")

    label("loc_46D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4747")

    #C0258
    ChrTalk(
        0xFE,
        (
            "对了，今天好像\x01",
            "要在市民会馆召开\x01",
            "市民座谈会啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "为了学习社会知识，\x01",
            "稍后我也去看看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D0")

    label("loc_4747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_479C")

    #C0260
    ChrTalk(
        0xFE,
        (
            "呼，在克洛斯贝尔\x01",
            "也已经玩腻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "难道就没有什么有趣的事情吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_51D0")

    label("loc_479C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_48E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4882")

    #C0262
    ChrTalk(
        0xFE,
        (
            "昨天那几个有钱人家的浪荡公子，\x01",
            "一开始的运气还算不错，\x01",
            "但最后却大败而归。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "他们似乎是非常不甘心，\x01",
            "嘴里骂着污言秽语，\x01",
            "急急忙忙地离开了……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "呵呵呵，像那种无可救药的人，\x01",
            "连女神都会放弃他们的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_48E0")

    label("loc_4882")


    #C0265
    ChrTalk(
        0xFE,
        (
            "昨天那几个有钱人家的\x01",
            "浪荡公子今天没来巴鲁卡。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "呵呵，看来今天可以\x01",
            "集中精神玩游戏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E0")

    Jump("loc_51D0")

    label("loc_48E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_49F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4977")

    #C0267
    ChrTalk(
        0xFE,
        (
            "我对那些只会倚仗父母钱财权力\x01",
            "的浅薄男人没有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "呵呵，还是多雷克老板\x01",
            "那种既深沉又有品位\x01",
            "的男人最有魅力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_49F2")

    label("loc_4977")


    #C0269
    ChrTalk(
        0xFE,
        (
            "不管对方有多少钱，我也不会\x01",
            "和有钱人家的浪荡公子交往。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "呵呵，还是多雷克老板\x01",
            "那种既深沉又有品位\x01",
            "的男人最有魅力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F2")

    Jump("loc_51D0")

    label("loc_49F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A68")

    #C0271
    ChrTalk(
        0xFE,
        (
            "通商会议吗……\x01",
            "呵呵，迪塔市长\x01",
            "还真是有一套啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "政治手腕如此优秀……\x01",
            "赌技想必也很厉害吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D0")

    label("loc_4A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4ADB")

    #C0273
    ChrTalk(
        0xFE,
        (
            "加雷提先生仍然对\x01",
            "以前败给冈兹先生一事\x01",
            "耿耿于怀。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "呵呵，以牌技师为职业的人\x01",
            "都很讨厌失败呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D0")

    label("loc_4ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E05")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B94")
    Jump("loc_4BDE")

    label("loc_4B94")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4BB4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BDE")

    label("loc_4BB4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BD4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BDE")

    label("loc_4BD4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BDE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0275
    ChrTalk(
        0xFE,
        (
            "啊，你不是兰迪吗，\x01",
            "好久不见哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#00305F哦哦，是雷特罗莎\x01",
            "姐姐啊。\x02\x03",

            "#00302F为了庆祝这难得的重逢，\x01",
            "和我约个会如何……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "呵呵，这个嘛。\x01",
            "如果你能战胜我，\x01",
            "考虑一下也无妨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        (
            "#00309F哦哦，这可是你说的啊，\x01",
            "那我们现在就……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D71")

    #C0279
    ChrTalk(
        0x101,
        "#00009F喂，兰迪……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        "#00109F呵呵，只是开个玩笑吧？\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x104,
        (
            "#00306F啊……嗯嗯……\x01",
            "真是的，你们两个的笑容好可怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF9")

    label("loc_4D71")


    #C0282
    ChrTalk(
        0x102,
        (
            "#00109F喂，兰迪，\x01",
            "你刚才说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#00306F啊……嗯嗯……\x01",
            "都说了只是玩笑而已啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x109,
        (
            "#10106F（兰迪前辈……\x01",
            "  真是不知悔改呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF9")

    SetScenarioFlags(0x14C, 4)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_50F2")

    label("loc_4E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F93")
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4EA0")
    Jump("loc_4EEA")

    label("loc_4EA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EC0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4EEA")

    label("loc_4EC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EE0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4EEA")

    label("loc_4EE0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EEA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0285
    ChrTalk(
        0xFE,
        (
            "呵呵，看样子，我们的\x01",
            "对决要延后到下次了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "也不知道\x01",
            "还有没有下次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x104,
        "#00306F呜～不要这样啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_50F2")

    label("loc_4F93")

    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5024")
    Jump("loc_506E")

    label("loc_5024")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5044")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_506E")

    label("loc_5044")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5064")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_506E")

    label("loc_5064")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_506E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0288
    ChrTalk(
        0xFE,
        (
            "呵呵，看样子，我们的\x01",
            "对决要延后到下次了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "也不知道\x01",
            "还有没有下次了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_50F2")

    Jump("loc_51D0")

    label("loc_50F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_514E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5112")
    Call(0, 11)
    Jump("loc_5149")

    label("loc_5112")


    #C0290
    ChrTalk(
        0xFE,
        "啊啊～又输了。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "呵呵，但我是不会\x01",
            "就此放弃的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5149")

    Jump("loc_51D0")

    label("loc_514E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_51D0")

    #C0292
    ChrTalk(
        0xFE,
        (
            "本已决定要尽量不来\x01",
            "克洛斯贝尔了……\x01",
            "最后却还是来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "虽然我的故乡卡尔瓦德也不坏，\x01",
            "但还是克洛斯贝尔的气氛更好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D0")

    TalkEnd(0xFE)
    Return()

    # Function_14_4540 end

    def Function_15_51D4(): pass

    label("Function_15_51D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F2")
    Call(0, 16)
    Jump("loc_525E")

    label("loc_51F2")


    #C0294
    ChrTalk(
        0xFE,
        (
            "呼，异变平息下来之后，\x01",
            "我继续在这里玩老虎机，\x01",
            "结果老伴却跑来找我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        "……这次确实是太让她担心了。\x02",
    )

    CloseMessageWindow()

    label("loc_525E")

    Jump("loc_5E0D")

    label("loc_5263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_537D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5319")

    #C0296
    ChrTalk(
        0xFE,
        (
            "我本以为戒严令\x01",
            "没什么大不了的，\x01",
            "所以就过来玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "没、没想到会被\x01",
            "卷进这种事……\x01",
            "这可真是人生中最大的失败啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "我老伴现在肯定\x01",
            "担心得要死吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5378")

    label("loc_5319")


    #C0299
    ChrTalk(
        0xFE,
        (
            "竟然会被\x01",
            "卷进这种事……\x01",
            "这可真是人生中最大的失败啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "我老伴现在肯定\x01",
            "担心得要死吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5378")

    Jump("loc_5E0D")

    label("loc_537D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_53D9")

    #C0301
    ChrTalk(
        0xFE,
        (
            "我听了刚才的演说……\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "老实说，我也不知道\x01",
            "谁才是正确的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E0D")

    label("loc_53D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5453")

    #C0303
    ChrTalk(
        0xFE,
        (
            "一周前的那起袭击事件\x01",
            "让我体会到了真正意义上的恐怖。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "但我觉得，越是在这种时候，\x01",
            "就越需要打起精神。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E0D")

    label("loc_5453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_559C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5516")

    #C0305
    ChrTalk(
        0xFE,
        (
            "玛因兹似乎\x01",
            "发生了很严重的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "在家里待着也没办法镇定下来，\x01",
            "所以还是跑出来玩了……\x01",
            "但今天实在是没有兴致啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "而且又很对不住老伴，\x01",
            "不然还是早点回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5597")

    label("loc_5516")


    #C0308
    ChrTalk(
        0xFE,
        (
            "在家里待着也没办法镇定下来，\x01",
            "所以还是跑出来玩了……\x01",
            "但今天实在是没有兴致啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "而且又很对不住老伴，\x01",
            "不然还是早点回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5597")

    Jump("loc_5E0D")

    label("loc_559C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_55F7")

    #C0310
    ChrTalk(
        0xFE,
        (
            "昨天一直输个没完……\x01",
            "今天一定要全部赢回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "看着吧，我这就要赢了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E0D")

    label("loc_55F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_56FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56AA")

    #C0312
    ChrTalk(
        0xFE,
        (
            "噢噢！？莫非要凑中一排了……\x01",
            "……什么嘛，又是空欢喜一场。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "可恶……\x01",
            "为什么！为什么总是失败呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#00304F（哎呀呀，老爷爷\x01",
            "  又开始激动了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_56F5")

    label("loc_56AA")


    #C0315
    ChrTalk(
        0xFE,
        (
            "可恶……\x01",
            "为什么！为什么总是失败呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        "我可是经过千锤百炼的高手啊！\x02",
    )

    CloseMessageWindow()

    label("loc_56F5")

    Jump("loc_5E0D")

    label("loc_56FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5796")

    #C0317
    ChrTalk(
        0xFE,
        (
            "唔唔唔，今天的手气\x01",
            "比较一般啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "如果就这么灰溜溜地回去，\x01",
            "还不知会被老伴怎么唠叨呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "可恶，我要赢！\x01",
            "赶快让我赢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_57FD")

    label("loc_5796")


    #C0320
    ChrTalk(
        0xFE,
        (
            "唔唔唔……\x01",
            "如果就这么灰溜溜地回去，\x01",
            "还不知会被老伴怎么唠叨呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "可恶，我要赢！\x01",
            "快让我赢啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57FD")

    Jump("loc_5E0D")

    label("loc_5802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_58FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589C")

    #C0322
    ChrTalk(
        0xFE,
        (
            "我完全赞成\x01",
            "克洛斯贝尔独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "我们一直要将税收的一部分\x01",
            "交纳给两大国，\x01",
            "这简直就是荒谬绝伦。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "独立是我们应有的权利。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_58FA")

    label("loc_589C")


    #C0325
    ChrTalk(
        0xFE,
        (
            "我们一直要将税收的一部分\x01",
            "交纳给两大国，\x01",
            "这简直就是荒谬绝伦。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "独立是我们应有的权利。\x02",
    )

    CloseMessageWindow()

    label("loc_58FA")

    Jump("loc_5E0D")

    label("loc_58FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ACC")

    #C0327
    ChrTalk(
        0xFE,
        (
            "今天早上，我老伴\x01",
            "笑得十分神秘。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "我问她因何发笑，\x01",
            "她却回答说『你很快就会知道』……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "到了这里以后我才发现，\x01",
            "原来她神不知鬼不觉地\x01",
            "取走了我钱包里的钱。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0330
    ChrTalk(
        0x104,
        (
            "#00305F嗯？利凯爷爷，既然您都\x01",
            "没钱了，还在这里做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        "……我愿意干坐着，你有意见吗？\x02",
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

    #C0332
    ChrTalk(
        0x104,
        (
            "#00306F不不……我只是\x01",
            "随便问问，请别介意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5B89")

    label("loc_5ACC")


    #C0333
    ChrTalk(
        0xFE,
        (
            "没钱就没法玩了……\x01",
            "但我绝对不会回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "如果就此屈服，\x01",
            "可就让我老伴的奸计得逞了。\x02",
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

    label("loc_5B89")

    Jump("loc_5E0D")

    label("loc_5B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5C13")

    #C0335
    ChrTalk(
        0xFE,
        (
            "大家都在关注什么揭幕式，\x01",
            "但我只想在这里\x01",
            "专心玩老虎机。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "至于老伴，她也不关心揭幕式，\x01",
            "正和朋友一起喝茶聊天呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E0D")

    label("loc_5C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFE")

    #C0337
    ChrTalk(
        0x104,
        (
            "#00300F哟，利凯爷爷，\x01",
            "您好像很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "呵呵，听这声音，是兰迪吧？\x01",
            "好久不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "如你所见，我精神得很，\x01",
            "而且正玩到关键时刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        "如果明白了，就别来给我捣乱。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        "#00300F哈哈，真是打扰了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_5D36")

    label("loc_5CFE")


    #C0342
    ChrTalk(
        0xFE,
        "我现在手正热呢，别来捣乱。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "……哦哦！又赢了！\x02",
    )

    CloseMessageWindow()

    label("loc_5D36")

    Jump("loc_5E0D")

    label("loc_5D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5DA6")

    #C0344
    ChrTalk(
        0xFE,
        (
            "不管老伴怎么说，\x01",
            "我也不打算\x01",
            "放弃赌博。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "这可是赌徒生来就\x01",
            "注定要做的事情啊，呵呵呵～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E0D")

    label("loc_5DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5E0D")

    #C0346
    ChrTalk(
        0xFE,
        (
            "呵呵，今天老虎机也\x01",
            "吐出了好多代币。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "吐出代币时那哗啦啦的声音，\x01",
            "真是让人心情愉快啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E0D")

    TalkEnd(0xFE)
    Return()

    # Function_15_51D4 end

    def Function_16_5E11(): pass

    label("Function_16_5E11")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0348
    ChrTalk(
        0xE,
        (
            "老头子，你可真是的……\x01",
            "为什么不回家啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xE,
        "好了，赶快回家！\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xD,
        (
            "等、等一下啊，老婆子。\x01",
            "至少等我把代币换了奖品……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        "闭嘴！！赶快走！！\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xD,
        "不要啊，你行行好吧～！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_5E11 end

    def Function_17_5EDF(): pass

    label("Function_17_5EDF")


    #C0353
    ChrTalk(
        0x104,
        (
            "#00300F哟，利凯爷爷，\x01",
            "今天的手气如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xD,
        "嗯？听这声音，是兰迪吧？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xD,
        "最近好像一直都看不到你啊。\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x104,
        "#00306F嗯，工作稍微有点忙。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "正是因为忙碌，才更要抽空来玩，\x01",
            "你可要明白这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x104,
        "#00300F哈哈，确实没错。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        (
            "那个臭老婆子，今天早上\x01",
            "竟然埋伏在这里的门口阻拦我。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xD,
        "她扬眉瞪眼，对我大呼小叫，\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "差点就被她给揪回家。\x01",
            "呼，真是千钧一发啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xD,
        (
            "无论克洛斯贝尔怎么变化，\x01",
            "唯独这欢乐街是永远不变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xD,
        (
            "酒吧、娱乐场所、大量的游客，\x01",
            "还有成群的年轻姑娘⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "就算街景店面有所变化，\x01",
            "这些也都是从来不变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xD,
        (
            "……不过，这里的治安\x01",
            "稍微有点差。\x01",
            "一般人可得多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_17_5EDF end

    def Function_18_612B(): pass

    label("Function_18_612B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6140")
    Call(0, 16)
    Jump("loc_618C")

    label("loc_6140")


    #C0366
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "他知道我究竟有\x01",
            "多担心吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        "……我决定暂时扣除他零用钱。\x02",
    )

    CloseMessageWindow()

    label("loc_618C")

    TalkEnd(0xFE)
    Return()

    # Function_18_612B end

    def Function_19_6190(): pass

    label("Function_19_6190")

    TalkBegin(0xFE)

    #C0368
    ChrTalk(
        0xFE,
        (
            "唔～本以为连续两个红之后，\x01",
            "下一次就该是黑了……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "呼，轮盘这种游戏\x01",
            "果然不是那么简单啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_6190 end

    def Function_20_61F7(): pass

    label("Function_20_61F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6272")

    #C0370
    ChrTalk(
        0xFE,
        (
            "我为了散散心，\x01",
            "就陪冈兹一起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "但现在来看，还是早点回去，\x01",
            "和镇长他们商讨今后的对策为好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C2")

    label("loc_6272")


    #C0372
    ChrTalk(
        0xFE,
        (
            "哈哈，所以说，\x01",
            "你要是在那个时候收手就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "冈兹，你实在是\x01",
            "太贪心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C2")

    TalkEnd(0xFE)
    Return()

    # Function_20_61F7 end

    def Function_21_62C6(): pass

    label("Function_21_62C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6344")

    #C0374
    ChrTalk(
        0xFE,
        (
            "到了克洛斯贝尔之后，\x01",
            "竟然发生了\x01",
            "如此重大的事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "……呼，难得来这里玩，\x01",
            "现在已经完全没有心情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_637A")

    label("loc_6344")


    #C0376
    ChrTalk(
        0xFE,
        (
            "啊啊，可恶……！\x01",
            "难得赢了几次，\x01",
            "最后竟然又输了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_637A")

    TalkEnd(0xFE)
    Return()

    # Function_21_62C6 end

    def Function_22_637E(): pass

    label("Function_22_637E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6447")

    #C0377
    ChrTalk(
        0xFE,
        (
            "是否赞成独立的问题似乎\x01",
            "让他们乱成一团……\x01",
            "真是些愚蠢的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔只要和以往一样，\x01",
            "继续向共和国低头献媚\x01",
            "就好了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "只要如此，就可以\x01",
            "维持和平局面了。\x01",
            "哼哼哼……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_64AB")

    label("loc_6447")


    #C0380
    ChrTalk(
        0xFE,
        (
            "算啦，独立也好，不独立也好，\x01",
            "和我们完全无关。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "嘿嘿，反正我们只想在\x01",
            "这个城市尽情玩乐一番。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64AB")

    TalkEnd(0xFE)
    Return()

    # Function_22_637E end

    def Function_23_64AF(): pass

    label("Function_23_64AF")

    TalkBegin(0xFE)

    #C0382
    ChrTalk(
        0xFE,
        "嘿嘿，要手下留情啊，尤利～\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "要是赢得太狠，\x01",
            "老板说不定就会禁止我们入内了～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_64AF end

    def Function_24_6509(): pass

    label("Function_24_6509")

    TalkBegin(0xFE)

    #C0384
    ChrTalk(
        0xFE,
        (
            "坐在那边的那个女人\x01",
            "真是个美人啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "但竟然拒绝了我们的邀请，\x01",
            "实在是没眼光。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_6509 end

    def Function_25_6564(): pass

    label("Function_25_6564")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6678")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6586")
    TalkEnd(0xFE)
    Call(0, 26)
    Return()

    label("loc_6586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6619")

    #C0386
    ChrTalk(
        0x15,
        (
            "#03500F再稍微晃悠一下，\x01",
            "我差不多也该回帝国了。\x02\x03",

            "#03504F必须得回去帮帮那个\x01",
            "小胡子不良大叔啊……\x01",
            "哎呀呀，可靠的男人就是辛苦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6678")

    label("loc_6619")


    #C0387
    ChrTalk(
        0x15,
        (
            "#03500F好了，再稍微晃悠一下，\x01",
            "我差不多也该回帝国了。\x02\x03",

            "#03504F哎呀呀，可靠的男人就是辛苦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6678")

    TalkEnd(0xFE)
    Return()

    # Function_25_6564 end

    def Function_26_667C(): pass

    label("Function_26_667C")

    EventBegin(0x0)
    Fade(500)
    OP_68(5540, 5300, 15900, 0)
    MoveCamera(43, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21700, 0)
    SetChrPos(0x15, 6390, 4270, 15790, 270)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x0, 5210, 4000, 16780, 135)
    SetChrPos(0x1, 5670, 4000, 17920, 135)
    SetChrPos(0x2, 4550, 4000, 15300, 90)
    SetChrPos(0x3, 4750, 4000, 13990, 45)
    SetChrPos(0x4, 4330, 4000, 17810, 135)
    SetChrPos(0x5, 5730, 4000, 13110, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0388
    ChrTalk(
        0x15,
        "#11P#03502F哟，大家辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#6P#00006F雷、雷克特先生……\x01",
            "你又穿成这样在巴鲁卡玩……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67DD")

    #C0390
    ChrTalk(
        0x105,
        "#10402F呵呵，看起来好像非常轻松啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6849")

    label("loc_67DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6815")

    #C0391
    ChrTalk(
        0x109,
        "#10106F你还真是轻松自在啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6849")

    label("loc_6815")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6849")

    #C0392
    ChrTalk(
        0x106,
        (
            "#10702F似乎非常\x01",
            "轻松愉快呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6849")


    #C0393
    ChrTalk(
        0x103,
        (
            "#6P#00205F怎么不穿\x01",
            "书记官的制服了？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x15,
        (
            "#11P#03506F哦，在和『魔导兵』战斗\x01",
            "的时候已经破烂不堪了。\x02\x03",

            "#03509F好啦，不用在意这种小事，轻松点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#6P#00006F哦……\x02\x03",

            "#00000F咳咳，那个……\x01",
            "非常感谢你协助参与\x01",
            "解放作战。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#00104F在突入兰花塔的时候，\x01",
            "真是多亏了你的帮忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x15,
        (
            "#11P#03504F哈哈，哪里，\x01",
            "我也玩得很开心。\x02\x03",

            "#03502F身为书记官，\x01",
            "一天到晚都在做文案工作，\x01",
            "难得好好运动了一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        (
            "#12P#00306F你的工作是间谍……\x01",
            "明明一直都在东奔西走吧。\x02\x03",

            "#00301F话说回来，雾香小姐也就罢了，\x01",
            "没想到连你也隐藏着\x01",
            "如此强的战斗力啊。\x02\x03",

            "那种剑术和高等魔法……\x01",
            "一般人是绝不可能在\x01",
            "一朝一夕间掌握的。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x15,
        (
            "#11P#03510F嗯，既然你如此有兴趣，\x01",
            "那我就告诉你好了。\x02\x03",

            "#03504F那是大约三十年前……\x01",
            "住在帝国某座深山中的\x01",
            "一位仙人教给我的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0400
    ChrTalk(
        0x101,
        (
            "#6P#00006F……第一句就是这种\x01",
            "荒唐无稽的谎话啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C30")

    #C0401
    ChrTalk(
        0x10A,
        "#00603F（哎呀呀……真是个难以沟通的男人。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C9F")

    label("loc_6C30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C66")

    #C0402
    ChrTalk(
        0x109,
        "#10106F编得也太随便了吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C9F")

    label("loc_6C66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C9F")

    #C0403
    ChrTalk(
        0x105,
        "#10409F哈哈哈，编得未免太随便了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6C9F")


    #C0404
    ChrTalk(
        0x15,
        (
            "#11P#03504F算啦，\x01",
            "就随你们去想象吧。\x02\x03",

            "#03510F我差不多也该\x01",
            "回帝国了。\x02\x03",

            "#03506F必须得回去帮帮那个\x01",
            "小胡子不良大叔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x103,
        (
            "#6P#00205F『铁血宰相』……\x01",
            "据说他遭到枪击之后，\x01",
            "暂时下落不明呢。\x02\x03",

            "#00203F遭到『神机』的攻击后，\x01",
            "正规军受到了严重打击，\x01",
            "而贵族势力就趁机起势……\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x15,
        (
            "#11P#03510F嗯，好像连帝都\x01",
            "都被贵族们完全占领了。\x02\x03",

            "#03506F唉，话说回来，\x01",
            "那个大叔也不为我们这些守卫人员着想一下，\x01",
            "总是招惹别人的怨恨。\x02\x03",

            "#03500F不过，他肯定没那么\x01",
            "容易就死掉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        "#12P#00302F你好像很轻松啊……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x15,
        (
            "#11P#03509F哈哈，你们又如何呢？\x02\x03",

            "#03504F吉利亚斯大叔和贵族势力……\x01",
            "无论最终是哪一方取胜……\x02\x03",

            "#03502F克洛斯贝尔未来的命运\x01",
            "恐怕也不会有什么改变吧。\x02",
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
    Sleep(30)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)

    #C0409
    ChrTalk(
        0x102,
        "#00108F……这……\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#6P#00003F……我们并不知道\x01",
            "未来将会发展成什么状况。\x02\x03",

            "#00001F但无论如何……\x01",
            "为了夺回琪雅，我们首先要做的\x01",
            "就是前往那棵『大树』。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x15,
        (
            "#11P#03504F……哈哈，这就好。\x02\x03",

            "展望未来自然很重要，\x01",
            "但如果一直望向远处，\x01",
            "反而有可能忽视脚下，不慎滑倒。\x02\x03",

            "#03500F所以说，最最重要的，\x01",
            "还是我们眼前的『现在』。\x02",
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
    Sleep(1000)

    #C0412
    ChrTalk(
        0x101,
        (
            "#6P#00006F你、你突然说得这么正经，\x01",
            "倒让人有点无所适从……\x02\x03",

            "#00000F……不过，谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x15,
        (
            "#11P#03502F哈哈，总之，你们就\x01",
            "尽量努力吧。\x02\x03",

            "#03509F否则的话，\x01",
            "我特意留在这里\x01",
            "也就没有价值了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x15, 6700, 4270, 15750, 90)
    SetChrPos(0x0, 5480, 4000, 13730, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1CC, 1)
    EventEnd(0x5)
    Return()

    # Function_26_667C end

    def Function_27_7293(): pass

    label("Function_27_7293")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "玩老虎机\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731E")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_731E")

    TalkEnd(0xFF)
    Return()

    # Function_27_7293 end

    def Function_28_7322(): pass

    label("Function_28_7322")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-900, 5000, 20000, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -900, 4000, 18700, 0)
    SetChrPos(0x102, 200, 4000, 17800, 0)
    SetChrPos(0x103, -2000, 4000, 17800, 0)
    SetChrPos(0x109, -1100, 4000, 17400, 0)
    SetChrPos(0x105, -100, 4000, 16900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0414
    ChrTalk(
        0x8,
        "#5P各位。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "#5P……莫非你们是为了\x01",
            "兰迪的事情而来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#12P#00001F是的……\x01",
            "他果然来过这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x8,
        (
            "#5P嗯，凌晨三点左右，\x01",
            "他突然来到店里……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x8,
        (
            "#5P稍微喝了一些之后，\x01",
            "就离开了……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x103,
        (
            "#12P#00206F……看样子，他不辞而别之后，\x01",
            "首先来到了这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x105,
        (
            "#10301F#12P他没告诉您，他之后\x01",
            "要去什么地方吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "#5P……看来他果然没有\x01",
            "回支援科啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x8,
        (
            "#5P他并没有告诉我\x01",
            "要去什么地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "#5P不过，在喝酒的过程中，\x01",
            "他的话明显比平时要多……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#5P另外，他离开的时候，\x01",
            "还从我这里拿走了一件东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        "#12P#00005F一件东西……？\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#5P嗯……是个非常重的箱子，\x01",
            "我也不知道里面有什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x8,
        (
            "#5P两年前，兰迪刚刚来到这座城市的时候，\x01",
            "把它交给了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x8,
        (
            "#5P他当时说『如果我什么时候死了，\x01",
            "就把它卖到废品回收站之类的地方吧』。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x102,
        "#00106F怎么会……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x109,
        "#12P#10108F……兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x103,
        "#6P#00206F……这太不像他的作风了。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        "#5P#00008F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x8,
        (
            "#5P……关于他的经历，\x01",
            "我也有一定程度的了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "#5P不过，我并不知道\x01",
            "过去具体发生过什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x8,
        (
            "#5P能了解他的过去，并支撑他的人，\x01",
            "恐怕也只有你们了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x102,
        "#00100F老板……\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#12P#00004F……是的，\x01",
            "我们一定会做到的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -900, 4000, 17500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 0)
    OP_29(0xAA, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_28_7322 end

    def Function_29_7843(): pass

    label("Function_29_7843")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch07400.itc", 0x1F)
    LoadChrToIndex("apl/ch51101.itc", 0x20)
    LoadChrToIndex("apl/ch51102.itc", 0x21)
    SoundLoad(3391)
    SoundLoad(3392)
    SoundLoad(3393)
    SoundLoad(3936)
    SoundLoad(3937)
    SoundLoad(3938)
    SoundLoad(3939)
    SoundLoad(3940)
    SoundLoad(3970)
    SoundLoad(3971)
    SoundLoad(3972)
    SoundLoad(2176)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    SetChrFlags(0xD, 0x80)
    SetMapObjFrame(0xFF, "c0470:Layer10", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_03", 0x0, 0x1)
    OP_68(5500, 5500, 4750, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 5200, 4000, 5850, 0)
    SetChrPos(0x102, 6000, 4000, 5300, 0)
    SetChrPos(0x109, 4800, 4000, 4500, 0)
    SetChrPos(0x105, 6200, 4000, 4250, 0)
    OP_0D()
    FadeToBright(1000, 0)
    Sleep(500)
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
    OP_68(6540, 5500, 13420, 3000)
    SetCameraDistance(21860, 3000)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    #C0438
    ChrTalk(
        0x15,
        (
            "#03506F怎么搞的～又是多奇啊。\x02\x03",

            "#03501F好无聊啊，就不能\x01",
            "偶尔出现一次菲娜吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(5480, 5500, 12360, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(21860, 3000)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 32)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 31)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 33)
    OP_6F(0x79)
    WaitChrThread(0x109, 1)
    OP_0D()
    Sleep(100)
    Fade(500)
    OP_68(5600, 5500, 12250, 0)
    MoveCamera(48, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19630, 0)
    SetChrPos(0x15, 6540, 4270, 13420, 180)
    OP_0D()

    #C0439
    ChrTalk(
        0x101,
        (
            "#00013F#12P雷克特先生，\x01",
            "你已经逃不掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x102,
        (
            "#00101F#6P请你老老实实地\x01",
            "坦白自己的真实身份吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x15,
        (
            "#03503F#5P真实身份啊～\x02\x03",

            "#03510F身份、身份……\x01",
            "到底选哪种身份才好呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        (
            "#00006F#12P……请不要再这么\x01",
            "明目张胆地敷衍别人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x15,
        (
            "#03504F这样好了……\x02\x03",

            "#03500F你们有什么问题就尽管问，\x01",
            "我只用『ＹＥＳ』和『ＮＯ』来回答。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        (
            "#00003F#12P……明白了，\x01",
            "那我就开始问了。\x02\x03",

            "#00001F你是帝国政府的二等书记官，\x01",
            "雷克特·亚兰德尔先生，\x01",
            "没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x15,
        "#03504FＹＥＳ。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        (
            "#00013F#12P同时也隶属于帝国军情报局，\x01",
            "担任特务大尉一职。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x15,
        "#03504FＹＥＳ。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x101,
        "#00008F#12P（这么爽快就承认了啊……）\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#00103F#6P……那么，接下来换我来问。\x02\x03",

            "#00101F你这次的访问行动，\x01",
            "是帝国政府授意的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)
    Sleep(300)

    #C0450
    ChrTalk(
        0x15,
        "#03501F可以说是ＮＯ，也可以说是ＹＥＳ。\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        (
            "#00101F#6P你准备在克洛斯贝尔\x01",
            "滞留一个月以上吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x15,
        (
            "#03504F呵呵……\x02\x03",

            "#03502F答案是ＮＯ。\x01",
            "只待一周左右，我就要回去了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E98():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E98)
    Sleep(100)

    def lambda_7EA8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7EA8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(150)

    #C0453
    ChrTalk(
        0x101,
        "#00013F（只能问到这里了吧……）\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x102,
        (
            "#00108F（嗯……\x01",
            "  已经问不出更多东西了。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F15():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F15)
    Sleep(50)

    def lambda_7F25():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F25)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(200)

    #C0455
    ChrTalk(
        0x101,
        (
            "#00003F#12P真是打扰了，\x01",
            "亚兰德尔大尉。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x102,
        "#00100F#6P感谢你的合作。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(200)

    #C0457
    ChrTalk(
        0x15,
        (
            "#03506F哦，没什么。\x02\x03",

            "#03505F对了，那个小家伙还好吗？\x01",
            "你们已经收养了她吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0458
    ChrTalk(
        0x101,
        (
            "#00005F#12P啊，是说琪雅吧？\x02\x03",

            "#00012F嗯，托你的福，\x01",
            "她一直都在健康成长。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x102,
        (
            "#00104F#6P……当时真是\x01",
            "非常感谢你的帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x105,
        (
            "#10302F#6P呵呵，在我们逃离的时候，\x01",
            "多亏有你相助啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x15,
        (
            "#03504F嗯～？你在说什么？\x01",
            "我当时只是在和小黑玩耍而已。\x02\x03",

            "#03502F对了，那个叫哈尔特曼的大叔\x01",
            "已经被逮捕了吧？\x02\x03",

            "哈，被那个危险分子拉着东躲西藏，\x01",
            "最后能平安无事地被捕，也算幸运了。\x02",
        )
    )

    CloseMessageWindow()
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

    #C0462
    ChrTalk(
        0x101,
        "#00001F#12P……你为何连这些都知道……\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x109,
        (
            "#10108F#6P从逮捕他们两人的那天算起，\x01",
            "才刚过去三天而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x15,
        (
            "#03503F因为确认这件事情\x01",
            "正是我来此的目的之一。\x02\x03",

            "#03501F顺便一说，其它的目的就是──\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 5790, 250, -2980, 0)
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    #N0465
    NpcTalk(
        0x16,
        "少女的声音",
        "#3936V#1P#30W啊～找到了！\x02",
    )

    CloseMessageWindow()

    #N0466
    NpcTalk(
        0x16,
        "少女的声音",
        "#3937V#1P#30W你在这种地方做什么啊？\x02",
    )

    CloseMessageWindow()
    OP_24(0xF61)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    Fade(500)
    SetMapObjFrame(0xFF, "heri_04a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "poul_02a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "nuki_04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white00", 0x0, 0x2)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_68(3310, 5500, 3920, 0)
    MoveCamera(113, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21270, 0)

    def lambda_843D():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_843D)

    def lambda_844A():
        OP_93(0x102, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_844A)

    def lambda_8457():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8457)

    def lambda_8464():
        OP_93(0x105, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8464)
    SetChrPos(0x15, 6540, 4270, 13420, 180)
    OP_68(5340, 5500, 12170, 6000)
    MoveCamera(130, 18, 0, 6000)
    OP_6E(400, 6000)
    SetCameraDistance(22330, 6000)

    def lambda_84B0():
        OP_9B(0x0, 0x16, 0x0, 0x36B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_84B0)
    Sleep(2000)

    def lambda_84C8():

        label("loc_84C8")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_84C8")

    QueueWorkItem2(0x101, 1, lambda_84C8)
    Sleep(50)

    def lambda_84DD():

        label("loc_84DD")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_84DD")

    QueueWorkItem2(0x105, 1, lambda_84DD)
    OP_6F(0x1)
    WaitChrThread(0x16, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    OP_C9(0x0, 0x80000000)

    #C0467
    ChrTalk(
        0x16,
        (
            "#04601F#3970V#11P#30W不是让你去\x01",
            "安排彩虹剧团的票嘛？\x02\x03",

            "#3971V怎样？到手了吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF83)
    OP_C9(0x1, 0x80000000)

    #C0468
    ChrTalk(
        0x15,
        (
            "#03509F#6P哦，已经拿到了今日\x01",
            "晚间公演的贵宾席门票哦。\x02\x03",

            "好好感谢我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x16,
        (
            "#04602F#11P真的吗！？\x02\x03",

            "#04612F嘿嘿嘿，谢啦！\x01",
            "我早就想去看了！\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#00005F#5P（……她是谁啊……？）\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x102,
        "#00105F#6P（看起来很年轻……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x101, 500)

    #C0472
    ChrTalk(
        0x16,
        (
            "#04605F#11P哎……？\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        "#00012F#5P那个……怎么了？\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0474
    AnonymousTalk(
        0x16,
        (
            "（嗅来嗅去）……\x01",
            "小哥，你身上的味道不错啊。\x02\x03",

            "是很让我怀念的味道。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0475
    ChrTalk(
        0x101,
        "#00005F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_96(0x16, 0x17AC, 0xFA0, 0x2E2C, 0x7D0, 0x0)
    TurnDirection(0x105, 0x16, 500)
    Sleep(100)
    OP_93(0x16, 0x5A, 0x1F4)
    OP_9B(0x1, 0x16, 0x0, 0x64, 0x3E8, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(50)
    OP_C9(0x0, 0x80000000)

    #C0476
    ChrTalk(
        0x16,
        "#04609F#3972V#11P嗷呜。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(150)
    SetChrName("")

    #A0477
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "少女轻轻地咬了咬罗伊德的耳垂。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    OP_9C(0x101, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    #Sound(3318, 255, 100, 0)    #voice#Lloyd
    Sleep(100)
    TurnDirection(0x101, 0x16, 0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x101, 0x40)
    OP_96(0x101, 0x1B4E, 0xFA0, 0x2E2C, 0xFA0, 0x0)
    ClearChrFlags(0x101, 0x40)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0478
    ChrTalk(
        0x101,
        "#00011F#5P！！！？？？？\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        "#00111F#6P等、等一下！？\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x109,
        "#10111F#6P咦、咦咦咦咦～！？\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x105,
        "#10302F#12P哟¤\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_9B(0x1, 0x16, 0xB4, 0x1F4, 0x3E8, 0x0)

    #C0482
    ChrTalk(
        0x101,
        "#00007F#5P你、你这是干什么……！？\x02",
    )

    CloseMessageWindow()
    SetChrName("红发少女")

    #C0483
    ChrTalk(
        0x16,
        (
            "#04612F#11P嘿嘿嘿，真好吃⊥\x02\x03",

            "#04602F嗯，果然能依稀\x01",
            "感觉到那种味道呢。\x02\x03",

            "那两个人的身上\x01",
            "就几乎没有那种味道……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x16, 0x0, 0x1F4)

    #C0484
    ChrTalk(
        0x16,
        (
            "#04605F#11P啊！\x01",
            "不过这个姐姐的身上倒是稍微有一些哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        "#00105F#6P哎……\x02",
    )

    CloseMessageWindow()
    Sound(809, 0, 100, 0)
    BeginChrThread(0x16, 3, 0, 34)
    WaitChrThread(0x16, 3)
    Sleep(50)
    Fade(500)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5520, 4000, 13000, 180)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 35)
    OP_68(4930, 5600, 11710, 0)
    MoveCamera(39, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x15, 6400, 4270, 13350, 225)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    TurnDirection(0x105, 0x102, 500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x17, 0x3)
    BeginChrThread(0x17, 3, 0, 36)
    SetChrPos(0x16, 5500, 4000, 13060, 180)
    SetChrPos(0x102, 5590, 4000, 12570, 180)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0486
    ChrTalk(
        0x102,
        "#00115F#3391V#4S#5P呀啊啊啊啊啊啊！？\x02",
    )

    CloseMessageWindow()
    OP_24(0xD3F)
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    #C0487
    ChrTalk(
        0x101,
        "#00011F#11P艾、艾莉！？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x109,
        "#10111F#5P什、什么时候绕到后边的？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0489
    ChrTalk(
        0x16,
        (
            "#04611F#3938V#5P#30W姐姐，你的胸部好大呀。\x02\x03",

            "#04609F#3939V谢莉是平胸，\x01",
            "好羡慕你呢⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF63)
    OP_57(0x0)
    OP_5A()

    #C0490
    ChrTalk(
        0x102,
        (
            "#00112F#3392V#5P#40W等、等一下，\x01",
            "快住手……！\x02\x03",

            "#00113F#3393V啊啊……！\x01",
            "为、为什么会……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD41)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0491
    ChrTalk(
        0x109,
        "#10114F#5P这、这、这……\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x105,
        "#10309F#6P啊哈哈，好精彩的场面。\x02",
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x101,
        (
            "#00012F#11P确、确实……不对！\x02\x03",

            "#00007F喂！你干什么！\x01",
            "为何突然做这种事情！？\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x15,
        (
            "#11P#03509F哈哈，真是随心所欲啊。\x02\x03",

            "#03502F要是再稍微过火些的话，\x01",
            "恐怕就要构成性骚扰了吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "#04605F#5P才不是性骚扰呢，\x01",
            "这只是肌肤相接培养感情。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0496
    ChrTalk(
        0x102,
        "#00107F#5P#4S这、这完全就是性骚扰！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    EndChrThread(0x17, 0x3)
    SetChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x102, 0x2)
    SetChrPos(0x16, 5300, 4000, 13370, 180)
    SetChrPos(0x102, 5520, 4000, 13000, 180)
    SetCameraDistance(19230, 1000)

    def lambda_8ED4():
        OP_9B(0x1, 0x16, 0x87, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8ED4)
    Sound(802, 0, 100, 0)
    OP_A1(0x102, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)

    def lambda_8EFB():
        OP_99(0x101, 0x102, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EFB)
    Sleep(50)

    def lambda_8F12():
        OP_99(0x109, 0x102, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8F12)
    Sleep(500)

    #C0497
    ChrTalk(
        0x102,
        "#5P#00113F呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x109,
        "#10111F#5P艾、艾莉小姐……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        "#00011F#11P不、不要紧吧？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 6730, 4000, 12500, 180)
    OP_0D()
    Sleep(300)

    #C0500
    ChrTalk(
        0x15,
        (
            "#03510F#5P嗯，那么，\x01",
            "我们就先告辞吧。\x02\x03",

            "#03509F还要去米修拉姆的主题公园\x01",
            "玩到晚上呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #N0501
    NpcTalk(
        0x16,
        "谢莉",
        "#04612F#3940V#5P#30W那就再见了～！\x02",
    )

    CloseMessageWindow()
    OP_24(0xF64)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_68(4780, 5500, 11560, 3000)
    OP_93(0x15, 0xE1, 0x0)

    def lambda_9063():
        OP_96(0x15, 0x1662, 0xFA0, 0x29FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9063)
    OP_95(0x16, 4740, 4000, 12780, 2000, 0x0)

    def lambda_9091():
        OP_95(0x15, 4740, 4000, 4480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9091)
    OP_95(0x16, 5730, 4000, 11500, 2000, 0x0)

    def lambda_90BF():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_90BF)

    def lambda_90CC():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_90CC)
    OP_95(0x16, 4740, 4000, 4480, 2000, 0x0)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    StopBGM(0xFA0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x109)
    OP_64(0x105)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)

    #C0502
    ChrTalk(
        0x101,
        "#00013F#5P那女孩到底是怎么回事……？\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x109,
        (
            "#10106F#5P让、让他们两个\x01",
            "都跑掉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，真是个很有个性的孩子啊。\x02\x03",

            "#10309F大概也就十五、六岁吧？\x01",
            "干得还真是漂亮。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0505
    ChrTalk(
        0x102,
        "#00107F#5P#4S哪里漂亮啊！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x8, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x8, 0x7)

    #C0506
    ChrTalk(
        0x102,
        (
            "#00106F#5P#30W呜呜……\x01",
            "为什么我会遇到这种事……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0507
    ChrTalk(
        0x101,
        "#00012F#11P那个……真是个灾难啊。\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x109,
        (
            "#10112F#5P算、算啦，反正是个女孩子，\x01",
            "也不用那么在意……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    #C0509
    ChrTalk(
        0x105,
        (
            "#10305F#12P而且你不是应该早就被\x01",
            "玛丽亚贝尔小姐揉习惯了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x4, 0x7, 0xA, 0xB, 0xC)
    Sleep(100)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0510
    ChrTalk(
        0x102,
        "#00115F#5P#5S才、才没有被揉习惯！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19530, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0511
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人返回警察总部，\x01",
            "呼叫了搜查一科……\x02\x03",

            "将有关雷克特的情报\x01",
            "连同黑月的动向一起做了报告。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    SetMapObjFrame(0xFF, "white00", 0x0, 0x1)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 1)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_7843 end

    def Function_30_941D(): pass

    label("Function_30_941D")


    def lambda_9422():
        OP_95(0x101, 5030, 4000, 10490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9422)
    WaitChrThread(0x101, 1)

    def lambda_9440():
        OP_95(0x101, 6540, 4000, 11860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9440)
    WaitChrThread(0x101, 1)

    def lambda_945E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_945E)
    Return()

    # Function_30_941D end

    def Function_31_9467(): pass

    label("Function_31_9467")


    def lambda_946C():
        OP_95(0x102, 5500, 4000, 9870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_946C)
    WaitChrThread(0x102, 1)

    def lambda_948A():
        OP_95(0x102, 5520, 4000, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_948A)
    WaitChrThread(0x102, 1)

    def lambda_94A8():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94A8)
    Return()

    # Function_31_9467 end

    def Function_32_94B1(): pass

    label("Function_32_94B1")


    def lambda_94B6():
        OP_95(0x109, 4810, 4000, 13910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_94B6)
    WaitChrThread(0x109, 1)

    def lambda_94D4():
        OP_95(0x109, 5530, 4000, 14790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_94D4)
    WaitChrThread(0x109, 1)

    def lambda_94F2():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_94F2)
    Return()

    # Function_32_94B1 end

    def Function_33_94FB(): pass

    label("Function_33_94FB")


    def lambda_9500():
        OP_95(0x105, 4800, 4000, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9500)
    WaitChrThread(0x105, 1)

    def lambda_951E():
        OP_95(0x105, 4740, 4000, 10780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_951E)
    WaitChrThread(0x105, 1)

    def lambda_953C():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_953C)
    Return()

    # Function_33_94FB end

    def Function_34_9545(): pass

    label("Function_34_9545")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9F(0x0, 0x16)
    OP_9F(0x1, 4740, 4000, 12360)
    OP_9F(0x1, 4740, 4000, 13900)
    OP_9F(0x1, 5520, 4000, 13900)
    OP_9F(0x2, 0x16, 8000, 0x6)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x16, 0xB4, 0x0)
    Return()

    # Function_34_9545 end

    def Function_35_9594(): pass

    label("Function_35_9594")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95B4")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_35_9594")

    label("loc_95B4")

    Return()

    # Function_35_9594 end

    def Function_36_95B5(): pass

    label("Function_36_95B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95D5")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x3, 0x4, 0x5, 0x4)
    Jump("Function_36_95B5")

    label("loc_95D5")

    Return()

    # Function_36_95B5 end

    SaveToFile()

Try(main)
