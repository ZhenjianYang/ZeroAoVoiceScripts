from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ドレイク・オーナー",     # 1
        "チェリー",               # 2
        "ガレッティ",             # 3
        "エリンデ",               # 4
        "レイタロッサ",           # 5
        "リッケ爺さん",           # 6
        "ホリィ婆さん",           # 7
        "観光客",                 # 8
        "鉱員マルロ",             # 9
        "鉱員ガンツ",             # 10
        "ユーリ",                 # 11
        "サイクス",               # 12
        "レジー",                 # 13
        "レクター",               # 14
        "赤毛の少女",             # 15
        "赤毛の少女",             # 16
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
        "Function_5_228F",         # 05, 5
        "Function_6_288F",         # 06, 6
        "Function_7_2893",         # 07, 7
        "Function_8_3727",         # 08, 8
        "Function_9_375C",         # 09, 9
        "Function_10_3760",        # 0A, 10
        "Function_11_454B",        # 0B, 11
        "Function_12_45EE",        # 0C, 12
        "Function_13_45F2",        # 0D, 13
        "Function_14_52A2",        # 0E, 14
        "Function_15_60EE",        # 0F, 15
        "Function_16_6F29",        # 10, 16
        "Function_17_701B",        # 11, 17
        "Function_18_72B5",        # 12, 18
        "Function_19_733A",        # 13, 19
        "Function_20_73B7",        # 14, 20
        "Function_21_74AE",        # 15, 21
        "Function_22_7588",        # 16, 22
        "Function_23_76F5",        # 17, 23
        "Function_24_7765",        # 18, 24
        "Function_25_77DA",        # 19, 25
        "Function_26_7918",        # 1A, 26
        "Function_27_86EB",        # 1B, 27
        "Function_28_8782",        # 1C, 28
        "Function_29_8D63",        # 1D, 29
        "Function_30_AAFD",        # 1E, 30
        "Function_31_AB47",        # 1F, 31
        "Function_32_AB91",        # 20, 32
        "Function_33_ABDB",        # 21, 33
        "Function_34_AC25",        # 22, 34
        "Function_35_AC74",        # 23, 35
        "Function_36_AC95",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B07")
    TurnDirection(0x8, 0x104, 0)

    #C0001
    ChrTalk(
        0x8,
        (
            "……ランディ、お前は\x01",
            "あの《大樹》に向かうんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#00300Fはは、よく分かるなぁ。\x01",
            "さすがドレイク・オーナーだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "フン、お前との付き合いも\x01",
            "短くはないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……ランディ、お前には\x01",
            "今までツケで飲んだ分の代金が\x01",
            "まだ残ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "絶対に無事に帰ってこねえと、\x01",
            "承知しねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00304F……ああ、分かった。\x02\x03",

            "#00309Fそのうちキッチリ返すから\x01",
            "安心しとけっつの。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00002F（はは……この２人って\x01",
            "  通じ合うものがあるんだろうな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 0)
    Jump("loc_CB8")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C38")

    #C0008
    ChrTalk(
        0x8,
        (
            "今まさに、クロスベルに試練の時が\x01",
            "訪れているのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "……皆さん、どうかランディを\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "そいつが今まで\x01",
            "ツケで飲んだ分の代金が、\x01",
            "まだ残っていますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#00003Fええ、お任せください。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#00309Fそのうちキッチリ返すから\x01",
            "安心しとけっつの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CB8")

    label("loc_C38")


    #C0013
    ChrTalk(
        0x8,
        (
            "今まさに、クロスベルに試練の時が\x01",
            "訪れているのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "……皆さん、どうかランディを\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB8")

    Jump("loc_228B")

    label("loc_CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E72")

    #C0015
    ChrTalk(
        0x8,
        "おお、これは皆さん……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00300F久しぶりだな、オーナー。\x01",
            "元気にしてたみてえじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)

    #C0017
    ChrTalk(
        0x8,
        "お前もな、ランディ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "マインツでのレジスタンス活動に\x01",
            "身を投じていると聞いたが、\x01",
            "お仲間と合流できたようでなによりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00000Fこちらには\x01",
            "被害などは出ていませんか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0020
    ChrTalk(
        0x8,
        "ええ、今のところは。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "皆さんも、市内を回られているなら\x01",
            "十分にお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        "#00300Fああ、そっちもな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 7)
    Jump("loc_FD5")

    label("loc_E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F48")

    #C0023
    ChrTalk(
        0x8,
        (
            "しかし、戒厳令から\x01",
            "営業を縮小していて正解でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "この少人数なら店の備蓄でも\x01",
            "しばらくは持ちこたえるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "どうかこちらはご心配なく。\x01",
            "皆さんは皆さんの仕事に\x01",
            "あたられてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD5")

    label("loc_F48")


    #C0026
    ChrTalk(
        0x8,
        (
            "この少人数なら店の備蓄でも\x01",
            "しばらくは持ちこたえるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "どうかこちらはご心配なく。\x01",
            "皆さんは皆さんの仕事に\x01",
            "あたられてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD5")

    Jump("loc_228B")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C2")

    #C0028
    ChrTalk(
        0x8,
        (
            "ふむ……朝から見慣れない\x01",
            "制服を着た連中がいると思ったら、\x01",
            "あれが国防軍の兵士ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "いかにも\x01",
            "準備万端という感じですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "クロイス氏は一体いつ頃から\x01",
            "このシナリオを\x01",
            "思い描いてたんですかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_114B")

    label("loc_10C2")


    #C0031
    ChrTalk(
        0x8,
        (
            "思えばまだ、あの住民投票から\x01",
            "１週間しか経っていませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "クロイス氏は一体いつ頃から\x01",
            "このシナリオを\x01",
            "思い描いてたんですかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114B")

    Jump("loc_228B")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EE")

    #C0033
    ChrTalk(
        0x8,
        (
            "おう、ランディ。\x01",
            "よく分かんねえが、何か\x01",
            "吹っ切れた顔してやがんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "店の方はこの状況で\x01",
            "閑古鳥が鳴いてるっつうのに、\x01",
            "一体どういうつもりだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00305Fん、別にどこも\x01",
            "変わっちゃいねえと思うが？\x02\x03",

            "#00309Fさてはオーナー、俺がちょっと\x01",
            "店に顔を出さなかったからって\x01",
            "早くも寂しがってんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "フン、バカ言え。\x01",
            "口うるさいのがいなくて、\x01",
            "逆にせいせいしてたくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "とにかく、お前にはこれまで\x01",
            "色んなモンを貸して来てんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "そいつらを全部返し終えるまで、\x01",
            "勝手にバックレんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00300Fハ、言われなくても分かってら。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000F（この２人、何だかんだで\x01",
            "  仲が良いんだよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00100F（ええ、まるで子供みたいにね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 1)
    Jump("loc_147D")

    label("loc_13EE")


    #C0042
    ChrTalk(
        0x8,
        (
            "とにかくランディ、\x01",
            "俺がお前にこれまで色んなモンを\x01",
            "貸して来たことを忘れんなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "期限は特に設けねえが、\x01",
            "いつか必ず返してもらうからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147D")

    Jump("loc_228B")

    label("loc_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_15FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1572")

    #C0044
    ChrTalk(
        0x8,
        (
            "私がヤツにしてやれるのは\x01",
            "せいぜい飲む場所を\x01",
            "与えてやる程度のこと……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "ですが皆さんならば\x01",
            "本当の意味でヤツの力になれる、\x01",
            "そんな気がするのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "皆さん、ランディのこと……\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F7")

    label("loc_1572")


    #C0047
    ChrTalk(
        0x8,
        (
            "皆さんならば\x01",
            "本当の意味でヤツの力になれる、\x01",
            "そんな気がするのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "皆さん、ランディのこと……\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F7")

    Jump("loc_228B")

    label("loc_15FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_177B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E1")

    #C0049
    ChrTalk(
        0x8,
        (
            "明日はいよいよ\x01",
            "リニューアル舞台の公開日ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "何でも今度の舞台では\x01",
            "あのリーシャ・マオに次ぐ\x01",
            "大型新人がデビューするとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "フフ、アルカンシェルの話題は\x01",
            "いつも我々を楽しませてくれますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1776")

    label("loc_16E1")


    #C0052
    ChrTalk(
        0x8,
        (
            "何でも今度の舞台では\x01",
            "あのリーシャ・マオに次ぐ\x01",
            "大型新人がデビューするとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "フフ、アルカンシェルの話題は\x01",
            "いつも我々を楽しませてくれますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1776")

    Jump("loc_228B")

    label("loc_177B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1859")

    #C0054
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "頭を休めたい時は、どうぞこちらの\x01",
            "バーカウンターをご利用下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "アルコール類はもちろん、\x01",
            "コーヒーなどもお出しできますよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18E1")

    label("loc_1859")


    #C0057
    ChrTalk(
        0x8,
        (
            "頭を休めたい時は、どうぞこちらの\x01",
            "バーカウンターをご利用下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "アルコール類はもちろん、\x01",
            "コーヒーなどもお出しできますよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E1")

    Jump("loc_228B")

    label("loc_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A12")

    #C0059
    ChrTalk(
        0x8,
        (
            "国家独立の是非、ですか……\x01",
            "裏社会の勢力図が今も蠢く中にあって、\x01",
            "この問題はまたとんでもないですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "住民投票の結果が即何かの動きに\x01",
            "つながるとは到底思えませんが……\x01",
            "問題は２大国の動向ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "下手をすれば、クロスベルの立場は\x01",
            "今以上に悪くなりなねませんからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ABB")

    label("loc_1A12")


    #C0062
    ChrTalk(
        0x8,
        (
            "住民投票の結果が即何かの動きに\x01",
            "つながるとは到底思えませんが……\x01",
            "問題は２大国の動向ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "下手をすれば、クロスベルの立場は\x01",
            "今以上に悪くなりかねませんからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABB")

    Jump("loc_228B")

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B4A")

    #C0064
    ChrTalk(
        0x8,
        (
            "ふむ、何だか少々\x01",
            "１階の方が騒がしいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "これ以上うるさくするようでしたら、\x01",
            "お引取り願いたい所ですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228B")

    label("loc_1B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1BD2")

    #C0066
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "身も心も溶かしてしまう……\x01",
            "甘いカクテルはいかがですかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228B")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C47")

    #C0068
    ChrTalk(
        0x8,
        (
            "オルキスタワーの除幕式は\x01",
            "盛況の内に終わったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "フフ、私も後で見るのが楽しみですよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_228B")

    label("loc_1C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E43")
    TurnDirection(0x8, 0x104, 0)

    #C0070
    ChrTalk(
        0x8,
        (
            "おう、ランディ。\x01",
            "昨日の酒はもう抜けたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#00302Fハ、当たり前だろ。\x01",
            "この俺があんなケチな量の酒を\x01",
            "次の日に残すと思ったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "フン、お前は相変わらず\x01",
            "口の減らんヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "復帰祝いとはいえ、\x01",
            "奢るんじゃなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00304Fはは、すまねえな。\x01",
            "だが感謝はしてんだぜ？\x02\x03",

            "#00300Fってわけでオーナー、\x01",
            "また機会があったら頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "フン、勝手言いやがって。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#00100F（ランディ、ちゃっかり\x01",
            "  顔を出していたみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00000F（ああ、そうだな。）\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x14C, 2)
    Jump("loc_1F69")

    label("loc_1E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")
    TurnDirection(0x8, 0x104, 0)

    #C0078
    ChrTalk(
        0x8,
        (
            "ま、また奢ってもらいたきゃ\x01",
            "その減らず口を治すんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "そうすりゃ\x01",
            "考えてやらんこともない。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00304Fへいへい、\x01",
            "まあゼンショしておくぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F69")

    label("loc_1EF7")

    TurnDirection(0x8, 0x104, 0)

    #C0081
    ChrTalk(
        0x8,
        (
            "ま、また奢ってもらいたきゃ\x01",
            "その減らず口を治すんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "そうすりゃ\x01",
            "考えてやらんこともない。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_1F69")

    Jump("loc_228B")

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F89")
    Call(0, 5)
    Jump("loc_21E5")

    label("loc_1F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212B")

    #C0083
    ChrTalk(
        0x8,
        (
            "最近、ルバーチェの代わりに\x01",
            "みかじめ料を寄こせという小物が\x01",
            "現れるようになりましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "今は相手にしていないのですが、\x01",
            "この状況が続けば色々と\x01",
            "面倒な事になって来るでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "やれやれ、早くどこでもいいから\x01",
            "ルバーチェ跡の一帯を\x01",
            "引き継いで欲しいものですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#10103F（ルバーチェが消えた影響が\x01",
            "  こういう所にも……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#00000F（これも紛いなりに保っていた\x01",
            "  秩序の１つって所だろうな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21E5")

    label("loc_212B")


    #C0088
    ChrTalk(
        0x8,
        (
            "今はまだ、どこの連中も比較的\x01",
            "大人しくはしているようですが……\x01",
            "流石にこの状況が続くと面倒です。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "やれやれ、早くどこでもいいから\x01",
            "ルバーチェ跡の一帯を\x01",
            "引き継いで欲しいものですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E5")

    Jump("loc_228B")

    label("loc_21EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_228B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2205")
    Call(0, 5)
    Jump("loc_228B")

    label("loc_2205")


    #C0090
    ChrTalk(
        0x8,
        (
            "ランディのヤツは警備隊に混じって\x01",
            "うまくやれているんですかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "フフ、昔みたいに情けないことを\x01",
            "言っていなければ良いのですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228B")

    TalkEnd(0x8)
    Return()

    # Function_4_90A end

    def Function_5_228F(): pass

    label("Function_5_228F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0092
    ChrTalk(
        0x8,
        (
            "特務支援課の皆さん……\x01",
            "それにワジさんじゃありませんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "何とも、珍しい組み合わせですね。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#10300Fああ、オーナー。\x01",
            "実はこの度、特務支援課に\x01",
            "配属されることが決まってね。\x02\x03",

            "詳細は省くけど、今後はひとつ\x01",
            "そういうことでヨロシク頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "なるほど、そうでしたか……\x01",
            "フフ、かしこまりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#00105Fあ、あっさり受け入れるんですね。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00000Fそれもそうだけど……\x01",
            "ワジ、当然のように\x01",
            "オーナーと知り合いなんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        (
            "#10304Fまあ、ホストにとっては\x01",
            "カジノを含めてここいら一帯は\x01",
            "仕事場みたいなものだからね。\x02\x03",

            "#10300F逆にドレイク・オーナーと\x01",
            "知り合いじゃないホストなんて\x01",
            "モグリか三流なんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x109,
        (
            "#10106Fしれっと言うなあ……\x02\x03",

            "#10101F大体、その歳で\x01",
            "この界隈を遊び回るなんて\x01",
            "よくないことなんだからね。\x02\x03",

            "#10103Fこの機会に少しは……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、相変わらず堅いね。\x02\x03",

            "まあ、そういう所も\x01",
            "君の魅力の内のひとつだと思うけど㈱\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2619")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2619")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_263F")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_263F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2665")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2665")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_268B")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_268B")

    Sleep(1000)

    #C0101
    ChrTalk(
        0x109,
        (
            "#10106Fはあ、何だかもう\x01",
            "どうでもよくなってきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        "#00106F分かるわ、その気持ち。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 7)
    Jump("loc_288E")

    label("loc_26EF")


    #C0103
    ChrTalk(
        0x8,
        (
            "そういえば皆さん、\x01",
            "ランディのヤツはまだ\x01",
            "復帰していないのですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "前に本人から古巣の警備隊に\x01",
            "顔を出して来ると聞きましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00000Fええ、もうしばらくすれば\x01",
            "合流できると思うんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "なるほど、ではまあヤツが\x01",
            "復帰した折には店に顔を出すよう\x01",
            "お伝え頂けますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "復帰祝いにワインの一本でも\x01",
            "用意してやる、と言っていたと。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00000Fはい、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#00100Fちゃんと伝えておきますね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 6)

    label("loc_288E")

    Return()

    # Function_5_228F end

    def Function_6_288F(): pass

    label("Function_6_288F")

    Call(0, 7)
    Return()

    # Function_6_288F end

    def Function_7_2893(): pass

    label("Function_7_2893")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3723")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "交換をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28FC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_28FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_291B")
    OP_AF(0x41)
    Jump("loc_295D")

    label("loc_291B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_292B")
    OP_AF(0x40)
    Jump("loc_295D")

    label("loc_292B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_293B")
    OP_AF(0x3F)
    Jump("loc_295D")

    label("loc_293B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_294B")
    OP_AF(0x3E)
    Jump("loc_295D")

    label("loc_294B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_295B")
    OP_AF(0x3D)
    Jump("loc_295D")

    label("loc_295B")

    OP_AF(0x3C)

    label("loc_295D")

    Call(0, 8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_371E")

    label("loc_296F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2983")
    Jump("loc_371E")

    label("loc_2983")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A21")

    #C0110
    ChrTalk(
        0x9,
        (
            "ようこそ、\x01",
            "カジノハウス《バルカ》へ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "たっくさん遊んでいって、\x01",
            "不安を吹き飛ばしてちょうだい☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A8D")

    label("loc_2A21")


    #C0112
    ChrTalk(
        0x9,
        (
            "こんな時だけど、\x01",
            "ウチも通常通り営業よん。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "たっくさん遊んでいって、\x01",
            "不安を吹き飛ばしてちょうだい☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8D")

    Jump("loc_371E")

    label("loc_2A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3C")

    #C0114
    ChrTalk(
        0x9,
        (
            "ううっ、正直怖いけど……\x01",
            "ガレッティさんとエリンデさんが\x01",
            "お休みでよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "オーナーが頑張ってるし、\x01",
            "あたしもしっかりしなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BD9")

    label("loc_2B3C")


    #C0116
    ChrTalk(
        0x9,
        (
            "ガレッティさんとエリンデさんが\x01",
            "お休みだから、１Ｆでは遊べないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "うちの景品にも役立つものが\x01",
            "あるかもしれないから、\x01",
            "いつも通り利用してってね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD9")

    Jump("loc_371E")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C5C")

    #C0118
    ChrTalk(
        0x9,
        (
            "う～ん、まさか突然戦争に\x01",
            "なったりはしないわよね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "これを受けて、２大国は\x01",
            "どんな声明を出すのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CD1")

    #C0120
    ChrTalk(
        0x9,
        "う～ん、住民投票か～。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "投票所は何箇所かあるらしいけど、\x01",
            "やっぱ行くならオルキスタワーよね～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D57")

    #C0122
    ChrTalk(
        0x9,
        (
            "う～ん、クロスベル市外の\x01",
            "出来事とは言え、マインツの事は\x01",
            "他人事じゃないよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        "早く無事に解決して欲しいわぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF4")

    #C0124
    ChrTalk(
        0x9,
        (
            "アルカンシェルの公演、\x01",
            "ついに明日の公開ね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "きっとまた、ウチにも\x01",
            "お客さんが流れてくるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        "うふ、楽しみね～㈱\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E4B")

    label("loc_2DF4")


    #C0127
    ChrTalk(
        0x9,
        (
            "アルカンシェルを観終わって\x01",
            "ウチに来る人って結構多いのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        "うふ、楽しみね～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_2E4B")

    Jump("loc_371E")

    label("loc_2E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EBC")

    #C0129
    ChrTalk(
        0x9,
        (
            "メダルがなくなったら\x01",
            "いつでも言ってね～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "ミラがなくなったら、\x01",
            "ＩＢＣへレッツゴー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F17")

    #C0131
    ChrTalk(
        0x9,
        "ようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "うふふ、今日もたっぷり\x01",
            "遊んで行ってね～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FA0")

    #C0133
    ChrTalk(
        0x9,
        (
            "あの３人組、\x01",
            "お金持ちらしいけど\x01",
            "随分感じが悪いのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "上から目線で誘われたけど、\x01",
            "こっちから願い下げって感じ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3024")

    #C0135
    ChrTalk(
        0x9,
        (
            "通商会議も今日が\x01",
            "いよいよ本番なんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "チェリーにはよく分かんないけど、\x01",
            "とにかくうまく行って欲しいわ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_3024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3129")

    #C0137
    ChrTalk(
        0x9,
        (
            "ガンツさん、\x01",
            "今日もまた懲りずにスロットに\x01",
            "精を出しているみたいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "数ヶ月前に見せたツキは\x01",
            "一体何だったんだろうってくらい\x01",
            "ヘボヘボだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "ガンツさん、もしかしたら\x01",
            "あの時に一生分のツキを\x01",
            "使い果たしちゃったのかも～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31CD")

    label("loc_3129")


    #C0140
    ChrTalk(
        0x9,
        (
            "ガンツさん、もしかしたら\x01",
            "あの時に一生分のツキを\x01",
            "使い果たしちゃったのかも～？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "ま、それでもたま～に\x01",
            "当ててはいるみたいだから\x01",
            "そこまでじゃないんだろうけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CD")

    Jump("loc_371E")

    label("loc_31D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3456")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33EB")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 0)

    #C0142
    ChrTalk(
        0x9,
        "あ、ランディさんだ～。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "もー、最近どこへ行ってたのよ～。\x01",
            "ダメじゃない、もっと遊ばなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#00304F全くだ、悪ぃなチェリーちゃん。\x02\x03",

            "#00309Fそんじゃ早速、仕事を切り上げて――\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3343")

    #C0145
    ChrTalk(
        0x101,
        "#00009Fなあ、ランディ。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#00109Fふふ、もちろん冗談よね？\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        (
            "#00306Fあ、ああ……\x01",
            "ってか笑顔が怖ぇぞ、２人とも。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E3")

    label("loc_3343")


    #C0148
    ChrTalk(
        0x102,
        (
            "#00109Fねえ、ランディ。\x01",
            "さっきも言ったと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#00306Fあ、ああ……\x01",
            "だから冗談だって。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        (
            "#10106F（ランディ先輩……\x01",
            "  本当に懲りないですね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E3")

    SetScenarioFlags(0x14C, 3)
    Jump("loc_3451")

    label("loc_33EB")


    #C0151
    ChrTalk(
        0x9,
        (
            "ランディさん、\x01",
            "またバンバン顔を見せてよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "そうでないと、\x01",
            "チェリーつまんないんだからぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3451")

    Jump("loc_371E")

    label("loc_3456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34B9")

    #C0153
    ChrTalk(
        0x9,
        (
            "ジメジメうっとうしい雨は\x01",
            "カジノで吹き飛ばそ～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        "今日もバンバン遊んでね～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_371E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3636")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A8")

    #C0155
    ChrTalk(
        0x9,
        (
            "さっき突然、ふらっと\x01",
            "レクターさんがやって来て\x01",
            "２階に上がっていったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "ふふ、数ヶ月ぶりに見たけど、\x01",
            "相変わらず変わった人よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        "#00101Fロイド……！\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#00001Fああ、今度こそ逃がさないぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3631")

    label("loc_35A8")


    #C0159
    ChrTalk(
        0x9,
        (
            "さっき突然、ふらっと\x01",
            "レクターさんがやって来て\x01",
            "２階に上がっていったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "ふふ、数ヶ月ぶりに見たけど、\x01",
            "相変わらず変わった人よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3631")

    Jump("loc_371E")

    label("loc_3636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C2")

    #C0161
    ChrTalk(
        0x9,
        "ようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "ここはメダルや\x01",
            "景品の交換カウンターよ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        (
            "バンバン遊んで\x01",
            "いい景品をゲットしてね～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_371E")

    label("loc_36C2")


    #C0164
    ChrTalk(
        0x9,
        (
            "ここはメダルや\x01",
            "景品の交換カウンターよ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "バンバン遊んで\x01",
            "いい景品をゲットしてね～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371E")

    Jump("loc_28A0")

    label("loc_3723")

    TalkEnd(0x9)
    Return()

    # Function_7_2893 end

    def Function_8_3727(): pass

    label("Function_8_3727")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_375B")
    SubItemNumber(0x18C, 1)
    AddItemNumber(0x186, 1)
    AddItemNumber(0x187, 1)
    AddItemNumber(0x188, 1)
    AddItemNumber(0x189, 1)
    AddItemNumber(0x18A, 1)
    Jump("Function_8_3727")

    label("loc_375B")

    Return()

    # Function_8_3727 end

    def Function_9_375C(): pass

    label("Function_9_375C")

    Call(0, 10)
    Return()

    # Function_9_375C end

    def Function_10_3760(): pass

    label("Function_10_3760")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_376D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4547")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                    # 0
            "ポーカーで遊ぶ\x01",              # 1
            "ブラックジャックで遊ぶ\x01",      # 2
            "やめる\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_37E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3839")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3839")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388E")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_388E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38A2")
    Jump("loc_4542")

    label("loc_38A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4542")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_399C")

    #C0166
    ChrTalk(
        0xA,
        (
            "常連のレイタロッサさんが\x01",
            "帰国されてしまって、\x01",
            "私も寂しい限りです。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "彼女とのスリル溢れる勝負は\x01",
            "毎日の楽しみでしたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "クロスベルが平和を取り戻したら、\x01",
            "また遊びに来てほしいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A47")

    label("loc_399C")


    #C0169
    ChrTalk(
        0xA,
        (
            "常連のレイタロッサさん……\x01",
            "クロスベルが平和を取り戻したら、\x01",
            "また遊びに来てほしいものですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "あのような得体のしれない大樹が\x01",
            "現れている間は、難しいでしょうが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A47")

    Jump("loc_4542")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3A5A")
    Jump("loc_4542")

    label("loc_3A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B58")

    #C0171
    ChrTalk(
        0xA,
        (
            "今日は朝から導力鉄道の運行が\x01",
            "制限されているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "クロスベルにいる帝国・\x01",
            "共和国人には本国への帰国勧告も\x01",
            "発令されたとのことですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "事態は我々が\x01",
            "思っている以上のスピードで\x01",
            "動いているのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BFC")

    label("loc_3B58")


    #C0174
    ChrTalk(
        0xA,
        (
            "クロスベルにいる帝国・\x01",
            "共和国人には本国への帰国勧告も\x01",
            "発令されたとのことですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "事態は我々が\x01",
            "思っている以上のスピードで\x01",
            "動いているのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFC")

    Jump("loc_4542")

    label("loc_3C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0D")

    #C0176
    ChrTalk(
        0xA,
        (
            "今も地面などに残る焦げ跡を見ると……\x01",
            "襲撃時のことが思い起こされます。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "幸いにも武装集団が\x01",
            "当店に乗り込んで来ることは\x01",
            "ありませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "もしここが襲われていたら\x01",
            "私たちもどうなっていたことか……\x01",
            "考えただけで恐ろしいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DB3")

    label("loc_3D0D")


    #C0179
    ChrTalk(
        0xA,
        (
            "幸いにも武装集団が\x01",
            "当店に乗り込んで来ることは\x01",
            "ありませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "もしここが襲われていたら\x01",
            "私たちもどうなっていたことか……\x01",
            "考えただけで恐ろしいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB3")

    Jump("loc_4542")

    label("loc_3DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E5F")

    #C0181
    ChrTalk(
        0xA,
        (
            "既に噂もあるようですが……\x01",
            "背後に帝国政府がいると考えるのが\x01",
            "自然といった所でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "とにかく、次に帝国が\x01",
            "どう出てくるかが気になる所ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_3E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F0B")

    #C0183
    ChrTalk(
        0xA,
        (
            "国家独立の是非……\x01",
            "確か住民投票の期日も\x01",
            "近づいて来ていましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "ふむ、どちらの選択が\x01",
            "よりベターな結果を生みそうか……\x01",
            "もう少し見極めたい所ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_3F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F86")

    #C0185
    ChrTalk(
        0xA,
        (
            "退屈な人生と刺激に満ちた人生は、\x01",
            "一体どちらが幸せなのでしょう……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        "ふふ、お客様はどうお考えですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_3F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4029")

    #C0187
    ChrTalk(
        0xA,
        (
            "負けが込んだとふてくされるのは\x01",
            "二流のやることでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "お客様がたには、是非とも\x01",
            "誠意を持って賭け事に望んで\x01",
            "欲しいものでございますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_4029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4103")

    #C0189
    ChrTalk(
        0xA,
        (
            "（さっきから大声で騒いだり、\x01",
            "  他のお客様に迷惑をかけたり……）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "（あちらのお客様は、\x01",
            "  少々マナーがなっていませんね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        (
            "（行為が過ぎるようなら\x01",
            "  厳重に注意しておかなければ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_419C")

    label("loc_4103")


    #C0192
    ChrTalk(
        0xA,
        (
            "（いくらカジノとはいえ、\x01",
            "  この場所にはこの場所なりの\x01",
            "  ルールとマナーがございます。）\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "（行為が過ぎるようなら\x01",
            "  厳重に注意しておかなければ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_419C")

    Jump("loc_4542")

    label("loc_41A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_423C")

    #C0194
    ChrTalk(
        0xA,
        (
            "ディーター市長の\x01",
            "ギャンブルセンスですか……\x01",
            "はてさて、どうなんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "こうした遊びもスマートに\x01",
            "こなしそうな印象ではありますが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_423C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4308")

    #C0196
    ChrTalk(
        0xA,
        (
            "今日はガンツさんが\x01",
            "お見えになっているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "いつぞやの強運ぶりには\x01",
            "本当に驚かされましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        (
            "今ではすっかり、元の冴えない\x01",
            "週末ギャンブラーに逆戻りですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_438F")

    label("loc_4308")


    #C0199
    ChrTalk(
        0xA,
        (
            "ガンツさんのいつぞやの\x01",
            "強運ぶりには本当に\x01",
            "驚かされましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "今ではすっかり、元の冴えない\x01",
            "週末ギャンブラーに逆戻りですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_438F")

    Jump("loc_4542")

    label("loc_4394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_443E")

    #C0201
    ChrTalk(
        0xA,
        (
            "かの高級クラブ\x01",
            "《ノイエ＝ブラン》がこの度\x01",
            "新装開店したそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        (
            "私のような者にはとても\x01",
            "手の届かない場所ですが……\x01",
            "一度は行ってみたいものです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_443E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4459")
    Call(0, 11)
    Jump("loc_44D7")

    label("loc_4459")


    #C0203
    ChrTalk(
        0xA,
        (
            "いやはや、レイタロッサ様は\x01",
            "本当に不敵でいらっしゃる。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "ギャンブルは過程より結果……\x01",
            "最後に笑った者の勝ちですからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D7")

    Jump("loc_4542")

    label("loc_44DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4542")

    #C0205
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "こちらはカード台でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        "宜しければ、一勝負いかがですか？\x02",
    )

    CloseMessageWindow()

    label("loc_4542")

    Jump("loc_376D")

    label("loc_4547")

    TalkEnd(0xA)
    Return()

    # Function_10_3760 end

    def Function_11_454B(): pass

    label("Function_11_454B")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0207
    ChrTalk(
        0xA,
        (
            "……残念、この勝負、\x01",
            "私の勝ちでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xC,
        (
            "ふふ、やるじゃない。\x01",
            "でも次はそうは行かないわよ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        "フフ、お手柔らかに。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_454B end

    def Function_12_45EE(): pass

    label("Function_12_45EE")

    Call(0, 13)
    Return()

    # Function_12_45EE end

    def Function_13_45F2(): pass

    label("Function_13_45F2")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "ルーレットで遊ぶ\x01",      # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4661")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4661")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B6")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_46B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46CA")
    Jump("loc_5299")

    label("loc_46CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5299")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_486B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47DB")

    #C0210
    ChrTalk(
        0xB,
        (
            "こんな時にでも賭け事に来る……\x01",
            "それは悪い事でも\x01",
            "なんでもありませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xB,
        (
            "本来、不安な気持ちを紛らわせ、\x01",
            "心を楽にしてくれるのが\x01",
            "娯楽というものなのですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "どうか、不安な時こそ\x01",
            "娯楽を楽しんでほしいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4866")

    label("loc_47DB")


    #C0213
    ChrTalk(
        0xB,
        (
            "本来、不安な気持ちを紛らわせ、\x01",
            "心を楽にしてくれるのが\x01",
            "娯楽というものですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xB,
        (
            "どうか、不安な時こそ\x01",
            "娯楽を楽しんでほしいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4866")

    Jump("loc_5299")

    label("loc_486B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4879")
    Jump("loc_5299")

    label("loc_4879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_49EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4963")

    #C0215
    ChrTalk(
        0xB,
        (
            "クロスベルの独立問題も\x01",
            "とうとう引き返せない所まで\x01",
            "来てしまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        (
            "ディーター大統領も\x01",
            "何の勝算なしにここまでの事を\x01",
            "するとは思えませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        (
            "一体、どんなカードを\x01",
            "用意しているのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49E6")

    label("loc_4963")


    #C0218
    ChrTalk(
        0xB,
        (
            "ディーター大統領も\x01",
            "何の勝算なしにここまでの事を\x01",
            "するとは思えませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "一体、どんなカードを\x01",
            "用意しているのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E6")

    Jump("loc_5299")

    label("loc_49EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC4")

    #C0220
    ChrTalk(
        0xB,
        (
            "住民投票の日がいよいよ\x01",
            "３日後に迫りましたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xB,
        (
            "結果は目に見えていますが、\x01",
            "当日はわたくしも\x01",
            "投票に行く予定でいますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        (
            "どちらかに投票するかは……\x01",
            "一応秘密にさせてくださいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B4D")

    label("loc_4AC4")


    #C0223
    ChrTalk(
        0xB,
        (
            "結果は目に見えていますが、\x01",
            "当日はわたくしも\x01",
            "投票に行く予定でいますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xB,
        (
            "どちらかに投票するかは……\x01",
            "一応秘密にさせてくださいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B4D")

    Jump("loc_5299")

    label("loc_4B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4BCC")

    #C0225
    ChrTalk(
        0xB,
        (
            "ドレイク・オーナー、\x01",
            "今日は何だか少し眠たそうですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "また遅くまで\x01",
            "飲んでいらしたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C4E")

    #C0227
    ChrTalk(
        0xB,
        (
            "こんな雨の日はどうぞ当店で\x01",
            "愉しんで行って下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        (
            "うふふ、もしかしたら\x01",
            "サービスするかもしれませんよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4CD8")

    #C0229
    ChrTalk(
        0xB,
        (
            "ギャンブルでも何でも……\x01",
            "重要なのは引き際ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xB,
        (
            "分相応という言葉もありますし、\x01",
            "多くを望むと大概失敗しますわよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D6B")

    #C0231
    ChrTalk(
        0xB,
        (
            "わたくし、人間はスリルを\x01",
            "求める生き物だと思いますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xB,
        (
            "お客様も一勝負どうかしら。\x01",
            "極上のスリルを\x01",
            "プレゼントいたしますわよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4DFF")

    #C0233
    ChrTalk(
        0xB,
        "クロスベルが独立すべきか否か……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xB,
        (
            "まったく、ディーター市長は\x01",
            "とんでもない難題をわたくしたちに\x01",
            "突きつけてくれたものですわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E85")

    #C0235
    ChrTalk(
        0xB,
        (
            "うふふ、いよいよ本会議の\x01",
            "当日がやって来ましたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        (
            "今から次のクロスベルタイムズが\x01",
            "愉しみで仕方ありませんわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F3A")

    #C0237
    ChrTalk(
        0xB,
        (
            "わたくしまだ見ていないのですが、\x01",
            "オルキスタワーは、それはそれは\x01",
            "立派なビルだそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xB,
        (
            "地上４０階の超高層ビルディング……\x01",
            "目に焼き付けるのが楽しみですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5050")

    #C0239
    ChrTalk(
        0xB,
        (
            "ディーター市長の呼びかけた\x01",
            "国際会議がいよいよ始まりますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "互いの真理を読み合い、\x01",
            "それぞれが持つ様々な切り札#6Rカード#を\x01",
            "ここぞというタイミングで切る……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xB,
        (
            "こう言っては何ですけど、\x01",
            "わたくし外交もギャンブルも\x01",
            "本質は同じだと思いますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50D0")

    label("loc_5050")


    #C0242
    ChrTalk(
        0xB,
        (
            "今回の場を設けるにあたり、\x01",
            "ディーター市長は\x01",
            "いかなる切り札#6Rカード#を用意したのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        "うふふ、興味が尽きませんわね。\x02",
    )

    CloseMessageWindow()

    label("loc_50D0")

    Jump("loc_5299")

    label("loc_50D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5133")

    #C0244
    ChrTalk(
        0xB,
        "ふふ、お客様も一勝負いかがですか？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xB,
        "思考の迷宮に、ご招待致しますわよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_5133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5230")

    #C0246
    ChrTalk(
        0xB,
        (
            "カジノハウス《バルカ》へようこそ。\x01",
            "こちらではルーレットが楽しめますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xB,
        (
            "はじめにお断りしておきますが、\x01",
            "この台にイカサマの類を\x01",
            "仕掛けることは一切不可能……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "どうです、一度小細工なしに\x01",
            "運命に身を委ねてみませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5299")

    label("loc_5230")


    #C0249
    ChrTalk(
        0xB,
        (
            "広く薄く堅実に張るも良し……\x01",
            "狭く厚く勝負に出るも良し……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xB,
        "全ての結果は女神のみぞ知る、ですわ。\x02",
    )

    CloseMessageWindow()

    label("loc_5299")

    Jump("loc_45FF")

    label("loc_529E")

    TalkEnd(0xB)
    Return()

    # Function_13_45F2 end

    def Function_14_52A2(): pass

    label("Function_14_52A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_52B3")
    Jump("loc_60EA")

    label("loc_52B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_541B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539A")

    #C0251
    ChrTalk(
        0xFE,
        (
            "私は丁度いなかったんだけど、\x01",
            "１週間前にとんでもない事件が\x01",
            "起こったそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "今後も同じような事がないとは\x01",
            "言い切れないみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "クロスベルに遊びに来るのも\x01",
            "そろそろ控えた方がいいかもね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5416")

    label("loc_539A")


    #C0254
    ChrTalk(
        0xFE,
        (
            "今後も同じような事がないとは\x01",
            "言い切れないみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "クロスベルに遊びに来るのも\x01",
            "そろそろ控えた方がいいかもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5416")

    Jump("loc_60EA")

    label("loc_541B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_54AC")

    #C0256
    ChrTalk(
        0xFE,
        (
            "謎の武装集団の目的って\x01",
            "一体何なのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "今後どんな要求が\x01",
            "どこから出てくるかで自ずと\x01",
            "分かって来るんでしょうけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_553D")

    #C0258
    ChrTalk(
        0xFE,
        (
            "そういえば今日は、\x01",
            "市民会館の方で市民フォーラムを\x01",
            "やってるって話ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "社会見学のつもりで、\x01",
            "後でちょっと見てこようかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_553D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_55A8")

    #C0260
    ChrTalk(
        0xFE,
        (
            "ふう、クロスベルで遊ぶのにも\x01",
            "また飽きてきちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "何か面白い事はないかしら？\x02",
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_55A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_570B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A0")

    #C0262
    ChrTalk(
        0xFE,
        (
            "昨日のドラ息子たち、\x01",
            "最初は調子よかったんだけど\x01",
            "結局最後には大負けしてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "よっぽど悔しかったのか、\x01",
            "汚い捨てゼリフを吐いて\x01",
            "さっさと帰っていったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "うふふ、あんな人たちには\x01",
            "女神も愛想を尽かすわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5706")

    label("loc_56A0")


    #C0265
    ChrTalk(
        0xFE,
        (
            "昨日のドラ息子たち、\x01",
            "今日はカジノに来てないみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "うふふ、今日はゲームに\x01",
            "集中できそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5706")

    Jump("loc_60EA")

    label("loc_570B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5847")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B9")

    #C0267
    ChrTalk(
        0xFE,
        (
            "私、親のミラと権力にべったりの\x01",
            "底の浅い男なんかに興味は無いわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "うふふ、やっぱり\x01",
            "ドレイク・オーナーみたいに\x01",
            "渋くてダンディじゃないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5842")

    label("loc_57B9")


    #C0269
    ChrTalk(
        0xFE,
        (
            "いくらミラをもってようが、\x01",
            "ドラ息子なんかお断りだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "うふふ、やっぱり\x01",
            "ドレイク・オーナーみたいに\x01",
            "渋くてダンディじゃないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5842")

    Jump("loc_60EA")

    label("loc_5847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58D2")

    #C0271
    ChrTalk(
        0xFE,
        (
            "通商会議か……\x01",
            "ふふ、ディーター市長って\x01",
            "本当にやり手よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "これだけの政治手腕……\x01",
            "ギャンブルの方もお強いのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_58D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5967")

    #C0273
    ChrTalk(
        0xFE,
        (
            "ガレッティさん、\x01",
            "以前ガンツさんに負けたのを\x01",
            "まだ根に持っているみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "ふふ、勝負師ってのは\x01",
            "本当に負けず嫌いばかりよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_5967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD7")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A20")
    Jump("loc_5A6A")

    label("loc_5A20")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A40")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A6A")

    label("loc_5A40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A60")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A6A")

    label("loc_5A60")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A6A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0275
    ChrTalk(
        0xFE,
        (
            "あら、貴方ランディじゃない。\x01",
            "お久しぶりね。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#00305Fおお、そういうアンタは\x01",
            "レイタロッサのお姉さん。\x02\x03",

            "#00302Fどうだい、再会を祝して\x01",
            "今度俺とデートでも……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "ふふ、そうね。\x01",
            "私との勝負に勝てたら\x01",
            "考えてあげてもいいわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        (
            "#00309Fおお、言ったな？\x01",
            "ならさっそく――\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C2B")

    #C0279
    ChrTalk(
        0x101,
        "#00009Fなあ、ランディ。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        "#00109Fふふ、もちろん冗談よね？\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x104,
        (
            "#00306Fあ、ああ……\x01",
            "ってか笑顔が怖ぇぞ、２人とも。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CCB")

    label("loc_5C2B")


    #C0282
    ChrTalk(
        0x102,
        (
            "#00109Fねえ、ランディ。\x01",
            "さっきも言ったと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#00306Fあ、ああ……\x01",
            "だから冗談だって。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x109,
        (
            "#10106F（ランディ先輩……\x01",
            "  本当に懲りないですね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CCB")

    SetScenarioFlags(0x14C, 4)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_5FD6")

    label("loc_5CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E71")
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D72")
    Jump("loc_5DBC")

    label("loc_5D72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D92")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DBC")

    label("loc_5D92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DB2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DBC")

    label("loc_5DB2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DBC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0285
    ChrTalk(
        0xFE,
        (
            "ふふ、どうやら\x01",
            "勝負はお預けみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "といっても、\x01",
            "次があるかどうかは\x01",
            "分からないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x104,
        "#00306Fくぅ～、そりゃねえぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_5FD6")

    label("loc_5E71")

    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F02")
    Jump("loc_5F4C")

    label("loc_5F02")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F22")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F4C")

    label("loc_5F22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F42")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F4C")

    label("loc_5F42")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F4C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0288
    ChrTalk(
        0xFE,
        (
            "ふふ、どうやら\x01",
            "勝負はお預けみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "といっても、\x01",
            "次があるかどうかは\x01",
            "分からないけど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_5FD6")

    Jump("loc_60EA")

    label("loc_5FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_604A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF6")
    Call(0, 11)
    Jump("loc_6045")

    label("loc_5FF6")


    #C0290
    ChrTalk(
        0xFE,
        "あ～あ、また負けちゃったわ。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "ふふ、でも\x01",
            "これで終わる私じゃないわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6045")

    Jump("loc_60EA")

    label("loc_604A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_60EA")

    #C0292
    ChrTalk(
        0xFE,
        (
            "しばらくクロスベルに\x01",
            "来るのは控えてたんだけど……\x01",
            "結局また来ちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "故郷カルバードも悪くないけど、\x01",
            "やっぱりクロスベルの空気は格別よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EA")

    TalkEnd(0xFE)
    Return()

    # Function_14_52A2 end

    def Function_15_60EE(): pass

    label("Function_15_60EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_610C")
    Call(0, 16)
    Jump("loc_618C")

    label("loc_610C")


    #C0294
    ChrTalk(
        0xFE,
        (
            "くう、異変が収まってそのまま\x01",
            "スロットで遊んでおったら、\x01",
            "婆さんが乗り込んできおった。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        "……さすがに心配をかけたかのう。\x02",
    )

    CloseMessageWindow()

    label("loc_618C")

    Jump("loc_6F25")

    label("loc_6191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_62E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626F")

    #C0296
    ChrTalk(
        0xFE,
        (
            "戒厳令など大したことないと\x01",
            "タカをくくって、\x01",
            "遊びにきていたんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "ま、まさかこんな事に\x01",
            "巻き込まれてしまうとは……\x01",
            "一生の不覚じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "今頃、婆さんも\x01",
            "心配しとるじゃろうな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_62DC")

    label("loc_626F")


    #C0299
    ChrTalk(
        0xFE,
        (
            "こんな事に\x01",
            "巻き込まれてしまうとは……\x01",
            "一生の不覚じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "今頃、婆さんも\x01",
            "心配しとるじゃろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62DC")

    Jump("loc_6F25")

    label("loc_62E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_635D")

    #C0301
    ChrTalk(
        0xFE,
        (
            "さっき演説を聞いてきたが……\x01",
            "凄い話になったものじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "正直、わしには\x01",
            "何が正しいのか分からんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_635D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_63ED")

    #C0303
    ChrTalk(
        0xFE,
        (
            "１週間前の襲撃事件には、\x01",
            "本当に恐怖を味わわされたのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "じゃが、わしはこういう時こそ\x01",
            "元気を出さねばいかんと思うのじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_63ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_655A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64CC")

    #C0305
    ChrTalk(
        0xFE,
        (
            "どうやら、マインツで\x01",
            "大変な事が起こっとるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "家におっても何となく\x01",
            "落ち着かんから出てきたが……\x01",
            "今日は流石に気乗りがせんわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "婆さんにも悪いし、\x01",
            "さっさと帰るとするかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6555")

    label("loc_64CC")


    #C0308
    ChrTalk(
        0xFE,
        (
            "家におっても何となく\x01",
            "落ち着かんから出てきたが……\x01",
            "今日は流石に気乗りがせんわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "婆さんにも悪いし、\x01",
            "さっさと帰るとするかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6555")

    Jump("loc_6F25")

    label("loc_655A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_65D7")

    #C0310
    ChrTalk(
        0xFE,
        (
            "昨日は負けに負けてしもうての……\x01",
            "今日は必ず取り返すつもりじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "今に見ておれぇ、わしはやるぞぉお！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_65D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_66FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A0")

    #C0312
    ChrTalk(
        0xFE,
        (
            "おおっ！？　今のは当たりでは……\x01",
            "……ってなんじゃ、肩透かしか。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "くぬうううぅ……\x01",
            "なぜ来ん、なぜ来んのじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#00304F（やれやれ、爺さん\x01",
            "  また熱くなってんな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_66F5")

    label("loc_66A0")


    #C0315
    ChrTalk(
        0xFE,
        (
            "くぬうううぅ……\x01",
            "なぜ来ん、なぜ来んのじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        "わしは百戦錬磨の勝負師じゃぞ！\x02",
    )

    CloseMessageWindow()

    label("loc_66F5")

    Jump("loc_6F25")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67AC")

    #C0317
    ChrTalk(
        0xFE,
        (
            "ふむむ、今日は\x01",
            "いまいち当たりが来んのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "こんな体たらくで帰っては\x01",
            "婆さんに何と言われるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "ええい、出ろッ！\x01",
            "出んかッ、出てこいやッ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6823")

    label("loc_67AC")


    #C0320
    ChrTalk(
        0xFE,
        (
            "ふむむ……\x01",
            "こんな体たらくで帰っては\x01",
            "婆さんに何と言われるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "ええい、出ろッ！\x01",
            "出なさいッ、出てきてちょッ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6823")

    Jump("loc_6F25")

    label("loc_6828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68E2")

    #C0322
    ChrTalk(
        0xFE,
        (
            "クロスベルの独立には、\x01",
            "わしは全面的に賛成じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "そもそも税収の一部を\x01",
            "２大国に納めるという話が\x01",
            "ナンセンスじゃからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "独立は当然の権利じゃよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_694E")

    label("loc_68E2")


    #C0325
    ChrTalk(
        0xFE,
        (
            "そもそも、税収の一部を\x01",
            "２大国に納めるという話が\x01",
            "ナンセンスじゃからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "独立は当然の権利じゃよ。\x02",
    )

    CloseMessageWindow()

    label("loc_694E")

    Jump("loc_6F25")

    label("loc_6953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B50")

    #C0327
    ChrTalk(
        0xFE,
        (
            "今朝は婆さんが\x01",
            "不敵に笑っておってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "なぜ笑うのかと問うたら、\x01",
            "じきに分かると言っておったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "どうやら、婆さんに\x01",
            "いつの間にか財布の中身を\x01",
            "抜かれておったみたいなんじゃ。\x02",
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
            "#00305Fん？　じゃあリッケ爺さん、\x01",
            "ミラもなしに何してんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        "……ただ座っとるだけじゃ、悪いか？\x02",
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
            "#00306Fいや……まあ混んでる\x01",
            "ワケでもねえし、悪くはねえがよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6C2D")

    label("loc_6B50")


    #C0333
    ChrTalk(
        0xFE,
        (
            "ミラがない以上、遊べんが……\x01",
            "わしは絶対に家へは帰らんぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "ここで屈してしまっては、\x01",
            "婆さんの思うツボじゃからな。\x02",
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

    label("loc_6C2D")

    Jump("loc_6F25")

    label("loc_6C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6CCD")

    #C0335
    ChrTalk(
        0xFE,
        (
            "世間が除幕式で騒ごうが、\x01",
            "わしはとにかくここで\x01",
            "スロットを打つだけじゃい。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "婆さんは婆さんで、茶飲み仲間と\x01",
            "ヨロシクやっとるからのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_6CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DCA")

    #C0337
    ChrTalk(
        0x104,
        (
            "#00300Fよう、リッケ爺さん。\x01",
            "元気にしてたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "ほほ、その声はランディか。\x01",
            "久しぶりじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "見ての通り元気も元気、\x01",
            "大フィーバーじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        "分かったら邪魔せんでくれ！\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        "#00300Fはは、そいつはすまねえな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_6E14")

    label("loc_6DCA")


    #C0342
    ChrTalk(
        0xFE,
        "今いい所なんじゃ、邪魔せんでくれ！\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "……おおっ、また来よったぞ！\x02",
    )

    CloseMessageWindow()

    label("loc_6E14")

    Jump("loc_6F25")

    label("loc_6E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6EB2")

    #C0344
    ChrTalk(
        0xFE,
        (
            "婆さんが何と言おうと、\x01",
            "わしはギャンブルを\x01",
            "止めるつもりは一切ないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "これも勝負師に生まれついた\x01",
            "定めというヤツじゃ、ほっほっほ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_6EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6F25")

    #C0346
    ChrTalk(
        0xFE,
        (
            "ほっほっ、今日も\x01",
            "スロットがよう出よるのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "メダルのじゃらじゃらする\x01",
            "音がたまらん心地じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F25")

    TalkEnd(0xFE)
    Return()

    # Function_15_60EE end

    def Function_16_6F29(): pass

    label("Function_16_6F29")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0348
    ChrTalk(
        0xE,
        (
            "ほんと、あなたって人は……\x01",
            "どうして家に帰ってこないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xE,
        "さあ、早く帰りますよ！\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xD,
        (
            "ま、待ってくれ婆さん。\x01",
            "せめてこのコインを交換してから……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        "ええい、お黙りなさいっ！！\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xD,
        "そんな、後生じゃ～！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_6F29 end

    def Function_17_701B(): pass

    label("Function_17_701B")


    #C0353
    ChrTalk(
        0x104,
        (
            "#00300Fよう、リッケ爺さん。\x01",
            "調子はどうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xD,
        "あん？　その声はランディ？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xD,
        "最近、顔を出さないじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x104,
        "#00306Fま、ちょっと仕事が忙しくてな。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "忙しいからこそ遊ぶのじゃ。\x01",
            "分かっておらんのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x104,
        "#00300Fはは、確かにそうかもな。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        (
            "婆さんめ、今朝は\x01",
            "玄関先で待ち伏せしておったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xD,
        "眉を吊り上げて一喝しおってな。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "危なく連れ戻される所じゃった。\x01",
            "ふう、まさに間一髪じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xD,
        (
            "クロスベルがいかに変わろうとも\x01",
            "歓楽街だけは無くならんじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xD,
        (
            "バーに賭博場、溢れる観光客に\x01",
            "群がるギャルたち㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "姿かたちは変化しようとも\x01",
            "昔から何一つ変わっておらんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xD,
        (
            "……ついでにちーっとばかり\x01",
            "治安が悪い所もな。\x01",
            "素人は気を付けることじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_17_701B end

    def Function_18_72B5(): pass

    label("Function_18_72B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72CA")
    Call(0, 16)
    Jump("loc_7336")

    label("loc_72CA")


    #C0366
    ChrTalk(
        0xFE,
        (
            "まったく、この人ったら……\x01",
            "私がどれだけ心配したと\x01",
            "思っているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        "……当分はお小遣いゼロね。\x02",
    )

    CloseMessageWindow()

    label("loc_7336")

    TalkEnd(0xFE)
    Return()

    # Function_18_72B5 end

    def Function_19_733A(): pass

    label("Function_19_733A")

    TalkBegin(0xFE)

    #C0368
    ChrTalk(
        0xFE,
        (
            "う～ん、赤・赤とくれば\x01",
            "次は黒だと思ったんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "ふう、ギャンブルってのは\x01",
            "一筋縄ではいかないものだね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_733A end

    def Function_20_73B7(): pass

    label("Function_20_73B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7450")

    #C0370
    ChrTalk(
        0xFE,
        (
            "気晴らしにいいと思って、\x01",
            "ガンツの付き合いで来てたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "早めに帰って、今後について\x01",
            "町長たちと相談したほうが良さそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74AA")

    label("loc_7450")


    #C0372
    ChrTalk(
        0xFE,
        (
            "はは、だからあの時\x01",
            "やめときゃ良かったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "ガンツ、お前は\x01",
            "欲張りすぎなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74AA")

    TalkEnd(0xFE)
    Return()

    # Function_20_73B7 end

    def Function_21_74AE(): pass

    label("Function_21_74AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7542")

    #C0374
    ChrTalk(
        0xFE,
        (
            "クロスベル市に来てみたら\x01",
            "こんな大変なことに\x01",
            "なっちまってるとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "……はあ、せっかくのカジノなのに\x01",
            "気分が乗らねえよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7584")

    label("loc_7542")


    #C0376
    ChrTalk(
        0xFE,
        (
            "ああ、くそ……！\x01",
            "せっかく勝ってたのに\x01",
            "もうパーじゃねえかっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7584")

    TalkEnd(0xFE)
    Return()

    # Function_21_74AE end

    def Function_22_7588(): pass

    label("Function_22_7588")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_767F")

    #C0377
    ChrTalk(
        0xFE,
        (
            "独立の是非がどうとか\x01",
            "世間では騒がれているようだが……\x01",
            "まったく愚かな奴ばかりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "クロスベルは今までどおり\x01",
            "共和国に媚びへつらい、\x01",
            "従っていればいいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "そうしている間は\x01",
            "平和が約束されるだろうしな。\x01",
            "ククク……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_76F1")

    label("loc_767F")


    #C0380
    ChrTalk(
        0xFE,
        (
            "まあ、独立しようがしまいが\x01",
            "俺たちには関係ないがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "クク、せいぜいこの街で\x01",
            "遊び尽くさせてもらうだけさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76F1")

    TalkEnd(0xFE)
    Return()

    # Function_22_7588 end

    def Function_23_76F5(): pass

    label("Function_23_76F5")

    TalkBegin(0xFE)

    #C0382
    ChrTalk(
        0xFE,
        "ククッ、ほどほどにしとけよユーリ～。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "あんまり勝ちすぎると、\x01",
            "出禁食らっちまうかもしれねえぜ～？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_76F5 end

    def Function_24_7765(): pass

    label("Function_24_7765")

    TalkBegin(0xFE)

    #C0384
    ChrTalk(
        0xFE,
        (
            "あっちに座ってる女、\x01",
            "なかなかの美人なんだけどな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "俺たちの誘いを断るなんて\x01",
            "見る目がないっつーの。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_7765 end

    def Function_25_77DA(): pass

    label("Function_25_77DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77FC")
    TalkEnd(0xFE)
    Call(0, 26)
    Return()

    label("loc_77FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78AD")

    #C0386
    ChrTalk(
        0x15,
        (
            "#03500Fさて、俺ももうちょいしたら\x01",
            "帝国に帰るとするかね。\x02\x03",

            "#03504Fあのチョイ悪ヒゲオヤジも\x01",
            "助けてやんねえといけねえし……\x01",
            "やれやれ、頼れる男はツラいぜェ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7914")

    label("loc_78AD")


    #C0387
    ChrTalk(
        0x15,
        (
            "#03500Fさて、俺ももうちょいしたら\x01",
            "帝国に帰るとするかね。\x02\x03",

            "#03504Fやれやれ、頼れる男はツラいぜェ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7914")

    TalkEnd(0xFE)
    Return()

    # Function_25_77DA end

    def Function_26_7918(): pass

    label("Function_26_7918")

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
        "#11P#03502Fよぉ、お疲れさん。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#6P#00006Fレ、レクターさん……\x01",
            "またそんな格好でカジノに……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A7F")

    #C0390
    ChrTalk(
        0x105,
        "#10402Fフフ、ものすごく寛いでるね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AFB")

    label("loc_7A7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7ABB")

    #C0391
    ChrTalk(
        0x109,
        "#10106Fものすごく寛いでますね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AFB")

    label("loc_7ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AFB")

    #C0392
    ChrTalk(
        0x106,
        (
            "#10702Fものすごく寛いでる\x01",
            "みたいですね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AFB")


    #C0393
    ChrTalk(
        0x103,
        (
            "#6P#00205F書記官の服は\x01",
            "どうされたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x15,
        (
            "#11P#03506Fああ、《魔導兵》との戦闘中に\x01",
            "ビリっと破けちまってなァ。\x02\x03",

            "#03509Fまあ、気にせず楽にしてくれたまへ。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#6P#00006Fは、はあ……\x02\x03",

            "#00000Fコホン、えっと……\x01",
            "解放作戦へのご協力、\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#00104Fオルキスタワーの突入では\x01",
            "本当にお世話になってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x15,
        (
            "#11P#03504Fハハ、いいってことよ。\x01",
            "こっちも好きでやったことだしな。\x02\x03",

            "#03502F書記官としての\x01",
            "デスクワークばっかだったから、\x01",
            "正直いい運動になったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        (
            "#12P#00306Fアンタの仕事は諜報員だろうが……\x01",
            "あんだけ動き回っといてよく言うぜ。\x02\x03",

            "#00301Fしかし、キリカさんはともかく\x01",
            "あんたがあそこまでの\x01",
            "戦闘力を隠し持ってたとはな。\x02\x03",

            "あの剣術と高位アーツ……\x01",
            "素人が一朝一夕で\x01",
            "扱えるもんじゃねえはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x15,
        (
            "#11P#03510Fふむ、そんなに\x01",
            "知りたいなら教えてしんぜよう。\x02\x03",

            "#03504Fそう、あれは約３０年前……\x01",
            "帝国のとある山奥に住む\x01",
            "仙人に教わったものでな。\x02",
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
            "#6P#00006F……出だしからあからさまに\x01",
            "ウソ臭いんですが。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F80")

    #C0401
    ChrTalk(
        0x10A,
        "#00603F（やれやれ……食えん男だ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FF3")

    label("loc_7F80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FBC")

    #C0402
    ChrTalk(
        0x109,
        "#10106Fさすがに適当すぎますね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FF3")

    label("loc_7FBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FF3")

    #C0403
    ChrTalk(
        0x105,
        "#10409Fアハハ、適当極まりないね。\x02",
    )

    CloseMessageWindow()

    label("loc_7FF3")


    #C0404
    ChrTalk(
        0x15,
        (
            "#11P#03504Fま、その辺は\x01",
            "お好きに想像してくれってな。\x02\x03",

            "#03510F……さて、俺もそろそろ\x01",
            "帝国に帰んないといけねえなあ。\x02\x03",

            "#03506Fあのチョイ悪ヒゲオヤジも\x01",
            "助けてやんねえといけねえし。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x103,
        (
            "#6P#00205F《鉄血宰相》……\x01",
            "確か、撃たれて行方不明に\x01",
            "なっているんでしたよね。\x02\x03",

            "#00203F《神機》によって\x01",
            "正規軍が大打撃を受けたスキを\x01",
            "貴族勢力に突かれたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x15,
        (
            "#11P#03510Fああ、帝都もすっかり\x01",
            "貴族どもに占領されちまったそうだ。\x02\x03",

            "#03506Fやれやれ、それにしても\x01",
            "逆恨みされやすいオッサンだよなァ。\x01",
            "お守りする俺らの身にもなれっての。\x02\x03",

            "#03500Fま、あのオッサンのことだから\x01",
            "簡単にくたばりゃしねえだろうがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        "#12P#00302Fなんだか気楽だなあ……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x15,
        (
            "#11P#03509Fハハ、あんたらこそどうなのよ？\x02\x03",

            "#03504Fギリアスのオッサンと貴族勢力、\x01",
            "どちらが勝ったとしても……\x02\x03",

            "#03502Fこの先、クロスベルの運命は\x01",
            "変わらないと思うけどなァ。\x02",
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
        "#00108F……それは……\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#6P#00003F……この先、どうしていくかは\x01",
            "まだ分かりません。\x02\x03",

            "#00001Fですが、何はなくとも……\x01",
            "まずはキーアを取り戻すため、\x01",
            "あの《大樹》に向かうつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x15,
        (
            "#11P#03504F……ハハ、それでいい。\x02\x03",

            "先を見据えるのは大事だが、\x01",
            "そればっかりに捉われちゃ\x01",
            "足元をすくわれる。\x02\x03",

            "#03500F何より大事なのは\x01",
            "目の前にある“今”だからな。\x02",
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
            "#6P#00006Fきゅ、急にまともな事を言われても\x01",
            "それはそれで戸惑うんですが……\x02\x03",

            "#00000F……ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x15,
        (
            "#11P#03502Fハハ、まあせいぜい\x01",
            "足掻いてみろってこった。\x02\x03",

            "#03509Fそうでなくちゃあ、\x01",
            "俺もわざわざ居残りまでした\x01",
            "甲斐がねえからなァ。\x02",
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

    # Function_26_7918 end

    def Function_27_86EB(): pass

    label("Function_27_86EB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "スロットで遊ぶ\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_877E")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_877E")

    TalkEnd(0xFF)
    Return()

    # Function_27_86EB end

    def Function_28_8782(): pass

    label("Function_28_8782")

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
        "#5Pこれは皆さん。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "#5P……もしやランディの件で\x01",
            "いらっしゃったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#12P#00001Fはい……\x01",
            "やはり彼はこちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x8,
        (
            "#5Pええ、夜中の３時くらいに\x01",
            "店にフラリと現れまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x8,
        (
            "#5Pしばらくここで飲んでから\x01",
            "帰って行きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x103,
        (
            "#12P#00206F……どうやら真っ先に\x01",
            "こちらを訪れたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x105,
        (
            "#10301F#12Pそれで、その後どこかに\x01",
            "行くとか言ってなかったかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "#5P……やはり支援課には\x01",
            "戻らなかったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x8,
        (
            "#5Pいえ、どこに行くとは\x01",
            "特に言っていませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "#5Pただ、どうも飲んでいる最中、\x01",
            "いつも以上に減らず口が多くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#5Pおまけに帰り際、ある物を\x01",
            "私から引き取って行ったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        "#12P#00005Fある物……ですか？\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#5Pええ……随分重いトランクで\x01",
            "中身は私も存じません。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x8,
        (
            "#5P２年前、ランディがこの街に\x01",
            "来たばかりの時に預かったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x8,
        (
            "#5P『俺が死んだらジャンク屋あたりに\x01",
            "  バラして売り払ってくれ』と言って。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x102,
        "#00106Fそんな……\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x109,
        "#12P#10108F……ランディ先輩……\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x103,
        "#6P#00206F……らしく無さすぎです。\x02",
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
            "#5P……ヤツの経歴については\x01",
            "私もある程度は存じています。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "#5Pですが、過去にどんな事が\x01",
            "あったのかまでは知りません。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x8,
        (
            "#5Pそれを知ってヤツの力になれるのは\x01",
            "恐らく、皆さんだけでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x102,
        "#00100Fオーナー……\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#12P#00004F……はい。\x01",
            "そうありたいと思います。\x02",
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

    # Function_28_8782 end

    def Function_29_8D63(): pass

    label("Function_29_8D63")

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
            "#03506Fなんだなんだ～、またドギかよ。\x02\x03",

            "#03501Fたまにはフィーナも\x01",
            "出てくれないとつまんねぇぜ。\x02",
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
            "#00013F#12P──レクターさん。\x01",
            "もう逃げられませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x102,
        (
            "#00101F#6Pいいかげん、観念して\x01",
            "身元を明らかにしてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x15,
        (
            "#03503F#5P身元ねェ～。\x02\x03",

            "#03510Fミモト、ミモト……\x01",
            "どれがいいかなぁっと。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        (
            "#00006F#12P……あからさまに\x01",
            "誤魔化そうとしないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x15,
        (
            "#03504Fそうだな……\x02\x03",

            "#03500Fイエス・オア・ノーで答えるから\x01",
            "何でも質問してくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        (
            "#00003F#12P……分かりました。\x01",
            "それでは質問させて頂きます。\x02\x03",

            "#00001F──帝国政府二等書記官、\x01",
            "レクター・アランドール殿で\x01",
            "間違いありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x15,
        "#03504Fイエス。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        (
            "#00013F#12P帝国軍情報局に所属する\x01",
            "特務大尉でもいらっしゃる？\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x15,
        "#03504Fイエスだ。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x101,
        "#00008F#12P（あっさり認めるのか……）\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#00103F#6P……では、私の方からも。\x02\x03",

            "#00101F今回の訪問は、帝国政府の\x01",
            "意向を受けてのものですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)
    Sleep(300)

    #C0450
    ChrTalk(
        0x15,
        "#03501Fノーであり、イエスでもある。\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        (
            "#00101F#6P１ヶ月以上の滞在を\x01",
            "予定されていますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x15,
        (
            "#03504Fフフ……\x02\x03",

            "#03502F答えはノーだ。\x01",
            "一週間くらいで帰るぜ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9410():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9410)
    Sleep(100)

    def lambda_9420():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9420)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(150)

    #C0453
    ChrTalk(
        0x101,
        "#00013F（ここまでか……）\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x102,
        (
            "#00108F（ええ……\x01",
            "  これ以上は無理ね。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9485():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9485)
    Sleep(50)

    def lambda_9495():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9495)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(200)

    #C0455
    ChrTalk(
        0x101,
        (
            "#00003F#12P──お手数をかけました。\x01",
            "アランドール大尉。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x102,
        "#00100F#6Pご協力、感謝いたします。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(200)

    #C0457
    ChrTalk(
        0x15,
        (
            "#03506Fああ、別にいいけどよー。\x02\x03",

            "#03505Fそういや、あのチビッ子は元気か？\x01",
            "アンタらが引き取ったんだよな？\x02",
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
            "#00005F#12Pえっと、キーアの事ですよね？\x02\x03",

            "#00012Fええ、おかげさまで\x01",
            "元気一杯に暮らしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x102,
        (
            "#00104F#6P……その節は\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x105,
        (
            "#10302F#6Pフフ、僕たちを逃がすのに\x01",
            "協力してくれたもんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x15,
        (
            "#03504Fん～、何のことだ？\x01",
            "オレはクロと遊んでただけだぜ。\x02\x03",

            "#03502Fそういや、ハルトマンのオッサン、\x01",
            "結局捕まっちまったんだってな？\x02\x03",

            "まあ、妙なのに連れ回されてたし、\x01",
            "無事に保護されてよかったぜ。\x02",
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
        "#00001F#12P……何でそんなことまで。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x109,
        (
            "#10108F#6Pあの２人を逮捕してから\x01",
            "３日も経っていないのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x15,
        (
            "#03503Fま、そのあたりの確認も\x01",
            "オレが来た目的の一つだからな。\x02\x03",

            "#03501Fちなみに他の目的は──\x02",
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
        "少女の声",
        "#3936V#1P#30Wあ～、いたいた！\x02",
    )

    CloseMessageWindow()

    #N0466
    NpcTalk(
        0x16,
        "少女の声",
        "#3937V#1P#30Wこんな所で何やってんのさー。\x02",
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

    def lambda_9A25():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A25)

    def lambda_9A32():
        OP_93(0x102, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A32)

    def lambda_9A3F():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A3F)

    def lambda_9A4C():
        OP_93(0x105, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A4C)
    SetChrPos(0x15, 6540, 4270, 13420, 180)
    OP_68(5340, 5500, 12170, 6000)
    MoveCamera(130, 18, 0, 6000)
    OP_6E(400, 6000)
    SetCameraDistance(22330, 6000)

    def lambda_9A98():
        OP_9B(0x0, 0x16, 0x0, 0x36B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9A98)
    Sleep(2000)

    def lambda_9AB0():

        label("loc_9AB0")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_9AB0")

    QueueWorkItem2(0x101, 1, lambda_9AB0)
    Sleep(50)

    def lambda_9AC5():

        label("loc_9AC5")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_9AC5")

    QueueWorkItem2(0x105, 1, lambda_9AC5)
    OP_6F(0x1)
    WaitChrThread(0x16, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    OP_C9(0x0, 0x80000000)

    #C0467
    ChrTalk(
        0x16,
        (
            "#04601F#3970V#11P#30Wアルカンシェルのチケットを\x01",
            "手配してくれるんだろー？\x02\x03",

            "#3971Vそれで、どうなったのさ～！\x02",
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
            "#03509F#6Pうむ、今日の夜公演の\x01",
            "貴賓席を確保してやったぞ。\x02\x03",

            "せいぜい感謝するがよい。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x16,
        (
            "#04602F#11Pホント！？\x02\x03",

            "#04612Fえへへ、サンキュ！\x01",
            "前から見たかったんだよねっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#00005F#5P（……誰だ……？）\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x102,
        "#00105F#6P（まだ若いみたいだけど……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x101, 500)

    #C0472
    ChrTalk(
        0x16,
        (
            "#04605F#11Pあれ……？\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        "#00012F#5Pえっと……何かな？\x02",
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
            "フーン……\x01",
            "お兄さん、匂いがするね。\x02\x03",

            "懐かしい匂いだ。\x02",
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
        "#00005F#5Pえ……\x02",
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
        "#04609F#3972V#11Pあーむっ。\x02",
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
            "少女はロイドの耳たぶに軽く噛#2Rかじ#り付いた。\x07\x00\x02",
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
        "#00111F#6Pちょ、ちょっと！？\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x109,
        "#10111F#6Pえ、ええええ～っ！？\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x105,
        "#10302F#12Pヒュウ♪\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_9B(0x1, 0x16, 0xB4, 0x1F4, 0x3E8, 0x0)

    #C0482
    ChrTalk(
        0x101,
        "#00007F#5Pい、いきなり何を……！？\x02",
    )

    CloseMessageWindow()
    SetChrName("赤毛の少女")

    #C0483
    ChrTalk(
        0x16,
        (
            "#04612F#11Pえへへ、ご馳走さま㈱\x02\x03",

            "#04602Fうん、やっぱり\x01",
            "かすかに匂いがするなぁ。\x02\x03",

            "そっちの２人からは\x01",
            "ほとんど匂わないけど……\x02",
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
            "#04605F#11P──あ！\x01",
            "お姉さんはちょっとするね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        "#00105F#6Pえ……\x02",
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
        "#00115F#3391V#4S#5Pきゃあああああっ！？\x02",
    )

    CloseMessageWindow()
    OP_24(0xD3F)
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    #C0487
    ChrTalk(
        0x101,
        "#00011F#11Pエ、エリィ！？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x109,
        "#10111F#5Pい、いつの間に後ろに？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0489
    ChrTalk(
        0x16,
        (
            "#04611F#3938V#5P#30Wお姉さん、おっきいねー。\x02\x03",

            "#04609F#3939Vシャーリィはペタンだから\x01",
            "うらやましいよ㈱\x02",
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
            "#00112F#3392V#5P#40Wちょ、ちょっと\x01",
            "やめてちょうだい……！\x02\x03",

            "#00113F#3393Vあうんっ……！\x01",
            "ど、どうしてこんな……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD41)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0491
    ChrTalk(
        0x109,
        "#10114F#5Pな、な、な……\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x105,
        "#10309F#6Pアハハ、いい光景だなぁ。\x02",
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x101,
        (
            "#00012F#11Pた、確かに……じゃなくて！\x02\x03",

            "#00007Fちょっと君！\x01",
            "いきなり何してるんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x15,
        (
            "#11P#03509Fハハッ、やりたい放題だな。\x02\x03",

            "#03502Fそれ以上やると\x01",
            "セクハラになっちまうぞ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "#04605F#5Pセクハラじゃないよー。\x01",
            "スキンシップだってば。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0496
    ChrTalk(
        0x102,
        "#00107F#5P#4Sじゅ、十分セクハラですっ！\x02",
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

    def lambda_A556():
        OP_9B(0x1, 0x16, 0x87, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A556)
    Sound(802, 0, 100, 0)
    OP_A1(0x102, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)

    def lambda_A57D():
        OP_99(0x101, 0x102, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A57D)
    Sleep(50)

    def lambda_A594():
        OP_99(0x109, 0x102, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A594)
    Sleep(500)

    #C0497
    ChrTalk(
        0x102,
        "#5P#00113Fはあはあはあ……\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x109,
        "#10111F#5Pエ、エリィさん。\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        "#00011F#11Pだ、大丈夫か？\x02",
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
            "#03510F#5Pうむ、それでは\x01",
            "オレたちは失礼しよう。\x02\x03",

            "#03509Fミシュラムのテーマパークで\x01",
            "夜まで遊び倒すんでな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #N0501
    NpcTalk(
        0x16,
        "シャーリィ",
        "#04612F#3940V#5P#30Wそれじゃ、またね～！\x02",
    )

    CloseMessageWindow()
    OP_24(0xF64)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_68(4780, 5500, 11560, 3000)
    OP_93(0x15, 0xE1, 0x0)

    def lambda_A709():
        OP_96(0x15, 0x1662, 0xFA0, 0x29FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A709)
    OP_95(0x16, 4740, 4000, 12780, 2000, 0x0)

    def lambda_A737():
        OP_95(0x15, 4740, 4000, 4480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A737)
    OP_95(0x16, 5730, 4000, 11500, 2000, 0x0)

    def lambda_A765():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A765)

    def lambda_A772():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A772)
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
        "#00013F#5Pな、何だったんだ……？\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x109,
        (
            "#10106F#5Pつ、つい\x01",
            "見逃しちゃいましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、強烈な子だったね。\x02\x03",

            "#10309F１５、６歳くらいかな？\x01",
            "なかなか良い仕事するじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0505
    ChrTalk(
        0x102,
        "#00107F#5P#4S良い仕事じゃありません！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x8, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x8, 0x7)

    #C0506
    ChrTalk(
        0x102,
        (
            "#00106F#5P#30Wううっ……\x01",
            "どうして私がこんな目に……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0507
    ChrTalk(
        0x101,
        "#00012F#11Pえっと……災難だったな。\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x109,
        (
            "#10112F#5Pま、まあ女の子同士だし\x01",
            "そこまで深刻にならなくても……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    #C0509
    ChrTalk(
        0x105,
        (
            "#10305F#12Pそれに君、マリアベル嬢に\x01",
            "揉まれ慣れてるんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x4, 0x7, 0xA, 0xB, 0xC)
    Sleep(100)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0510
    ChrTalk(
        0x102,
        "#00115F#5P#5Sも、揉まれ慣れてません！\x02",
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
            "その後、ロイドたちは\x01",
            "警察本部に戻って一課を呼び出し……\x02\x03",

            "黒月の動向と合わせて\x01",
            "レクターに関する報告を行った。\x07\x00\x02",
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

    # Function_29_8D63 end

    def Function_30_AAFD(): pass

    label("Function_30_AAFD")


    def lambda_AB02():
        OP_95(0x101, 5030, 4000, 10490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB02)
    WaitChrThread(0x101, 1)

    def lambda_AB20():
        OP_95(0x101, 6540, 4000, 11860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB20)
    WaitChrThread(0x101, 1)

    def lambda_AB3E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB3E)
    Return()

    # Function_30_AAFD end

    def Function_31_AB47(): pass

    label("Function_31_AB47")


    def lambda_AB4C():
        OP_95(0x102, 5500, 4000, 9870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB4C)
    WaitChrThread(0x102, 1)

    def lambda_AB6A():
        OP_95(0x102, 5520, 4000, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB6A)
    WaitChrThread(0x102, 1)

    def lambda_AB88():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB88)
    Return()

    # Function_31_AB47 end

    def Function_32_AB91(): pass

    label("Function_32_AB91")


    def lambda_AB96():
        OP_95(0x109, 4810, 4000, 13910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB96)
    WaitChrThread(0x109, 1)

    def lambda_ABB4():
        OP_95(0x109, 5530, 4000, 14790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABB4)
    WaitChrThread(0x109, 1)

    def lambda_ABD2():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABD2)
    Return()

    # Function_32_AB91 end

    def Function_33_ABDB(): pass

    label("Function_33_ABDB")


    def lambda_ABE0():
        OP_95(0x105, 4800, 4000, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ABE0)
    WaitChrThread(0x105, 1)

    def lambda_ABFE():
        OP_95(0x105, 4740, 4000, 10780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ABFE)
    WaitChrThread(0x105, 1)

    def lambda_AC1C():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC1C)
    Return()

    # Function_33_ABDB end

    def Function_34_AC25(): pass

    label("Function_34_AC25")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9F(0x0, 0x16)
    OP_9F(0x1, 4740, 4000, 12360)
    OP_9F(0x1, 4740, 4000, 13900)
    OP_9F(0x1, 5520, 4000, 13900)
    OP_9F(0x2, 0x16, 8000, 0x6)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x16, 0xB4, 0x0)
    Return()

    # Function_34_AC25 end

    def Function_35_AC74(): pass

    label("Function_35_AC74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC94")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_35_AC74")

    label("loc_AC94")

    Return()

    # Function_35_AC74 end

    def Function_36_AC95(): pass

    label("Function_36_AC95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ACB5")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x3, 0x4, 0x5, 0x4)
    Jump("Function_36_AC95")

    label("loc_ACB5")

    Return()

    # Function_36_AC95 end

    SaveToFile()

Try(main)
