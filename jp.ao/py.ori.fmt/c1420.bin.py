from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1420.bin",                # FileName
        "c1420",                    # MapName
        "c1420",                    # Location
        0x002F,                     # MapIndex
        "ed7116",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 47, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1420",                  # 0
        "ルガノフ",               # 1
        "ジェド",                 # 2
        "ヒューイ",               # 3
        "スラッシュ",             # 4
        "コウキ",                 # 5
        "ディーノ",               # 6
    ))

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch30800.itc",                   # 01
        "chr/ch31700.itc",                   # 02
        "chr/ch30802.itc",                   # 03
        "chr/ch31702.itc",                   # 04
    ))

    DeclNpc(17079,   1000,    -2579,   225,  261,  0x0, 0,   1,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(12189,   0,       -5269,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(18700,   4000,    -8210,   315,  261,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1779,    0,       -5260,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(11420,   0,       7809,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(2920,    0,       6769,    89,   389,  0x0, 0,   0,   0,   0,   0,   0,   24,  255,  0)

    DeclEvent(0x0040, 0, 15,  6.260000228881836,     -1.0800000429153442,   -1.0,                  9.0,                   [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.0433334112167358,   0.18000000715255737,   0.20000000298023224,   1.0])

    ChipFrameInfo(540, 0)                                        # 0

    ScpFunction((
        "Function_0_21C",          # 00, 0
        "Function_1_2CC",          # 01, 1
        "Function_2_2F7",          # 02, 2
        "Function_3_992",          # 03, 3
        "Function_4_A07",          # 04, 4
        "Function_5_1074",         # 05, 5
        "Function_6_164E",         # 06, 6
        "Function_7_17F1",         # 07, 7
        "Function_8_196F",         # 08, 8
        "Function_9_1C0A",         # 09, 9
        "Function_10_2170",        # 0A, 10
        "Function_11_2712",        # 0B, 11
        "Function_12_28C0",        # 0C, 12
        "Function_13_2A34",        # 0D, 13
        "Function_14_2D22",        # 0E, 14
        "Function_15_2E6A",        # 0F, 15
        "Function_16_31FE",        # 10, 16
        "Function_17_326C",        # 11, 17
        "Function_18_3412",        # 12, 18
        "Function_19_37BF",        # 13, 19
        "Function_20_397E",        # 14, 20
        "Function_21_3BDD",        # 15, 21
        "Function_22_3F64",        # 16, 22
        "Function_23_4245",        # 17, 23
        "Function_24_4301",        # 18, 24
        "Function_25_4823",        # 19, 25
        "Function_26_5968",        # 1A, 26
    ))


    def Function_0_21C(): pass

    label("Function_0_21C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_254"),
        (1, "loc_260"),
        (2, "loc_26C"),
        (3, "loc_278"),
        (4, "loc_284"),
        (5, "loc_290"),
        (6, "loc_29C"),
        (SWITCH_DEFAULT, "loc_2A8"),
    )


    label("loc_254")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_260")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_26C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_278")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_284")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_290")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_29C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_2B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B4")

    label("loc_2CB")

    Return()

    # Function_0_21C end

    def Function_1_2CC(): pass

    label("Function_1_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F6")
    OP_94(0xFE, 0x38C2, 0xFFFFF1B4, 0x4902, 0xFFFFF984, 0x3E8)
    Sleep(300)
    Jump("Function_1_2CC")

    label("loc_2F6")

    Return()

    # Function_1_2CC end

    def Function_2_2F7(): pass

    label("Function_2_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30F")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_991")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_384")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x9, 8410, 150, 2820, 180)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0xA, 8610, 0, 620, 0)
    SetChrPos(0xB, 9810, 0, 1720, 315)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_37F")

    Jump("loc_991")

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3AB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_991")

    label("loc_3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3ED")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5200, 0, -850, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_991")

    label("loc_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_48C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 11110, 0, -5220, 315)
    SetChrPos(0xD, 9940, 0, -4200, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C")
    SetChrFlags(0xD, 0x10)

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B")
    SetChrFlags(0xC, 0x10)

    label("loc_43B")

    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xB, 5200, 0, -850, 90)
    SetChrPos(0xA, 7320, 0, -1690, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_487")

    Jump("loc_991")

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_583")
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_518")
    SetChrPos(0x8, 11740, 0, 3420, 270)
    SetChrPos(0xB, 10710, 0, 3950, 180)
    SetChrPos(0xA, 11310, 0, 2070, 0)
    SetChrPos(0x9, 11990, 0, -2650, 270)
    SetChrPos(0xC, 10020, 0, -3240, 0)
    SetChrPos(0xD, 10920, 0, -1430, 180)
    Event(0, 25)
    Jump("loc_57E")

    label("loc_518")

    SetChrPos(0x8, 16290, 1000, -1650, 315)
    SetChrPos(0x9, 15290, 1000, -650, 135)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrPos(0xC, 7030, 0, -50, 180)
    SetChrPos(0xD, 7320, 0, -1690, 0)

    label("loc_57E")

    Jump("loc_991")

    label("loc_583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_620")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 8420, 0, -590, 90)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xB, 9260, 0, -2100, 90)
    SetChrPos(0xA, 9360, 0, 930, 90)
    SetChrPos(0xD, 11270, 0, -2110, 270)
    SetChrPos(0x9, 11840, 0, -590, 270)
    SetChrPos(0xC, 11330, 0, 1080, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_991")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_69B")
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x8, 8420, 0, -590, 90)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 10910, 0, -710, 270)
    SetChrPos(0xB, 9740, 0, -1840, 0)
    SetChrPos(0xA, 9850, 0, 700, 180)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")
    SetChrFlags(0x9, 0x10)

    label("loc_68C")

    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_991")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_738")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 11500, 0, -3660, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_991")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7D5")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 11500, 0, -3660, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xA, 11110, 0, -5220, 0)
    SetChrPos(0xB, 9940, 0, -4200, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_991")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_865")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83E")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_860")

    label("loc_83E")

    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)

    label("loc_860")

    Jump("loc_991")

    label("loc_865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8E5")
    SetChrPos(0x8, 7030, 0, -50, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0x9, 7320, 0, -1690, 315)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")
    Event(0, 9)

    label("loc_8E0")

    Jump("loc_991")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_96F")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 7030, 0, -50, 225)
    SetChrPos(0xC, 5200, 0, -850, 90)
    SetChrPos(0xD, 7320, 0, -1690, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_END)), "loc_939")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_939")

    SetChrFlags(0xC, 0x10)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_991")

    label("loc_96F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_991")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_991")

    Return()

    # Function_2_2F7 end

    def Function_3_992(): pass

    label("Function_3_992")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_9AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C8")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_9CE")

    label("loc_9C8")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_9CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EF")
    Sound(128, 1, 50, 0)

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A06")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_A06")

    Return()

    # Function_3_992 end

    def Function_4_A07(): pass

    label("Function_4_A07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD2")

    #C0001
    ChrTalk(
        0xFE,
        "イェ、イェ～～～ッ！！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "不安なんか知らねェ～～！！\x01",
            "ワケわかんねえ事に\x01",
            "かまってるヒマねェ～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "ヤァ、歌でも歌って吹き飛ばせ、\x01",
            "イィ～～～～～ヤッホォウ～～！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B5A")

    label("loc_AD2")


    #C0004
    ChrTalk(
        0xFE,
        (
            "あんなデカい木なんざ屁でもねェ～！\x01",
            "不安なんか知らねェ～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ヤァ、歌でも歌って吹き飛ばせ、\x01",
            "イィ～～～～～ヤッホォウ～～！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A")

    Jump("loc_1070")

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B6D")
    Jump("loc_1070")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B7B")
    Jump("loc_1070")

    label("loc_B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B89")
    Jump("loc_1070")

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C28")

    #C0006
    ChrTalk(
        0xFE,
        (
            "ヴオ゛オ゛ォォォ……\x01",
            "がぁくそッ、何かイライラすんぜェ～ッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "マインツで襲撃事件だぁ！？\x01",
            "んなことより、\x01",
            "ヴァルドさんはどこだァア～ッ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C6D")

    #C0008
    ChrTalk(
        0xFE,
        (
            "ハンッ、言っておくが、\x01",
            "ゲンコは貸しだからなァッ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C88")
    Call(0, 5)
    Jump("loc_CF2")

    label("loc_C88")


    #C0009
    ChrTalk(
        0xFE,
        (
            "ヴァルドさん……\x01",
            "カジノで大当たりでもしたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "でも、だったら何で\x01",
            "教えてくれねえんだよォオ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF2")

    Jump("loc_1070")

    label("loc_CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D12")
    Call(0, 6)
    Jump("loc_D53")

    label("loc_D12")


    #C0011
    ChrTalk(
        0xFE,
        (
            "ハァ～、にしてもヴァルドさんが\x01",
            "いねえとマジつまンねえぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D53")

    Jump("loc_1070")

    label("loc_D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D69")
    Call(0, 7)
    Jump("loc_1070")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D7A")
    Call(0, 8)
    Jump("loc_1070")

    label("loc_D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4C")

    #C0012
    ChrTalk(
        0xFE,
        (
            "ヴァルドさ～～んッ！\x01",
            "マジお願いだから顔出してくれよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "酒ならオレらが買うから\x01",
            "ここで飲みましょうよォオ～～ッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "アンタがいねえと、\x01",
            "何も始まらねえンだよォオオ～～ッ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EC6")

    label("loc_E4C")


    #C0015
    ChrTalk(
        0xFE,
        (
            "酒ならオレらが買うから\x01",
            "ここで飲みましょうよォオ～～ッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "アンタがいねえと、\x01",
            "何も始まらねえンだよォオオ～～ッ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC6")

    Jump("loc_1070")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE6")
    Call(0, 9)
    Jump("loc_F46")

    label("loc_EE6")


    #C0017
    ChrTalk(
        0xFE,
        (
            "信じねえ……\x01",
            "オレはぜってェ信じねえぞッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "そんなフザケた話が\x01",
            "あってたまるかァア……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F46")

    Jump("loc_1070")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF3")

    #C0019
    ChrTalk(
        0xFE,
        "イェ～、イャアア～～ッ！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "テスタメンツのヤロウどもォオ！\x01",
            "スカしてられるのも今の内ィイッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "#4S……イィィ～～ヤッホウッッ！！#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1062")

    label("loc_FF3")


    #C0022
    ChrTalk(
        0xFE,
        (
            "テスタメンツのヤロウどもォオ！\x01",
            "スカしてられるのも今の内ィイッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "#4S……イィィ～～ヤッホウッッ！！#3S\x02",
    )

    CloseMessageWindow()

    label("loc_1062")

    Jump("loc_1070")

    label("loc_1067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1070")

    label("loc_1070")

    TalkEnd(0xFE)
    Return()

    # Function_4_A07 end

    def Function_5_1074(): pass

    label("Function_5_1074")

    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0024
    ChrTalk(
        0x9,
        (
            "で、オマエら。\x01",
            "調査の結果はどうだったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xD,
        "オ、オッス……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xD,
        (
            "１週間前になるんスけど、\x01",
            "カノンってガキがヴァルドさんを\x01",
            "見かけたらしくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "それで、その時にどうやら\x01",
            "エニグマっつう小型の通信端末を\x01",
            "使っていたみたいッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        (
            "交換屋の女主人が言うには\x01",
            "１０万ミラはする高価な\x01",
            "シロモンらしいんスけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0xB,
        "じゅ、１０万ミラァ～！？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "うおぅ、マジか……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "ヴァ、ヴァルドさん、\x01",
            "一体どこにそんなミラが……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "確かにそれも気になるが……\x01",
            "コウキ、オマエ通信端末っつったな？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "それはつまり……\x01",
            "ヴァルドさんが誰かと\x01",
            "連絡を取ってたってことかよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0034
    ChrTalk(
        0xC,
        (
            "ハイ、流石にそのガキんちょも\x01",
            "内容までは聞き取れなかった\x01",
            "そうなんスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xD,
        (
            "ええ、でもヴァルドさん、\x01",
            "何だか楽しそうに笑ってたって……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "……わ、笑ってた？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "何か良いことあったんすかね……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "ってか、まさかオレたち\x01",
            "ヴァルドさんに見捨てられた……\x01",
            "なぁんてことはないッスよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "てめえ、スラッシュ。\x01",
            "ふざけたクチ利いてんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "ブチ殺されたいなら別だけどよォ？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)
    TurnDirection(0xB, 0x8, 0)

    #C0042
    ChrTalk(
        0xB,
        "す、すんません……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00001F（ヴァルドがエニグマを、か……\x01",
            "  確かに少し気になるな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#00203F（ええ、言ってもまだエニグマは\x01",
            "  一般的にそれほど数が\x01",
            "  出回ってるワケでもないですし……）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        "#10303F（……ヴァルド………………）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_93(0x8, 0x5A, 0x0)
    OP_93(0xD, 0x10E, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xB, 0x5A, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    SetScenarioFlags(0x16E, 4)
    Return()

    # Function_5_1074 end

    def Function_6_164E(): pass

    label("Function_6_164E")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0046
    ChrTalk(
        0x8,
        (
            "おう、ジェド。\x01",
            "コウキとディーノのヤロウは\x01",
            "まだ来ねえのかァ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "まあ、待ってやれよ。\x01",
            "追加調査が必要なんだとさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "ところで、お前らの方は\x01",
            "全然だったそうじぇねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "まあよォ……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        "す、すんません。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "一通り心当たりは\x01",
            "回ったんスけど、ここ最近は\x01",
            "モノの見事に誰も見てないって……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        "……そうか。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "ヴァルドさん……\x01",
            "マジでどこへ行ったんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x9, 0x10)
    Return()

    # Function_6_164E end

    def Function_7_17F1(): pass

    label("Function_7_17F1")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B8")

    #C0054
    ChrTalk(
        0x8,
        (
            "あ～っと、オレたちは\x01",
            "とにかくヴァルドさんの\x01",
            "行きそうな場所を探すかンな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "範囲は街ゼンブだ。\x01",
            "片っ端から調べて回りやがれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        "オッス！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        "かしこまりッス！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1962")

    label("loc_18B8")


    #C0058
    ChrTalk(
        0x8,
        (
            "あ～、ヴァルドさんを見かけたら\x01",
            "ソッコーでここに戻って報告しろよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "テメエらが声掛けても\x01",
            "またシカトされンのがオチだかンなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "オッス！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        "かしこまりッス！\x02",
    )

    CloseMessageWindow()

    label("loc_1962")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_17F1 end

    def Function_8_196F(): pass

    label("Function_8_196F")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B95")

    #C0062
    ChrTalk(
        0x8,
        "んで、ヤツら何つったんだァ？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "ハ、ハイ。\x01",
            "それが素直に謝って来たんスよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "そういう態度に出られると\x01",
            "それ以上ケチ付けられねえっつうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "ったく、どーしようもねェなァッ！\x01",
            "青坊主のヤツらもヤツらだが、\x01",
            "てめえらも気合い足りねえンだよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "いーか、そういう時は挑発だァア。\x01",
            "今からオレがとっておきの脅し文句を\x01",
            "教えてやるから、よォ～く覚えとけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "『オマエのかーちゃん、デーベーソー！』\x01",
            "……そらッ、言ってみろ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0xA,
        "え、え～っと……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        "オ、オスッ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BFD")

    label("loc_1B95")


    #C0070
    ChrTalk(
        0xA,
        "オ、オマエのかーちゃん……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        "デ、デーベーソー……っと。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "オラオラァ、声が小せえぞォォオ～！\x02",
    )

    CloseMessageWindow()

    label("loc_1BFD")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_196F end

    def Function_9_1C0A(): pass

    label("Function_9_1C0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1400, 1000, 0, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 2400, 0, -700, 90)
    SetChrPos(0x105, 2400, 0, 700, 90)
    SetChrPos(0x102, 1100, 0, -700, 90)
    SetChrPos(0x109, 1100, 0, 700, 90)
    SetChrPos(0x104, 100, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(3400, 1000, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0073
    ChrTalk(
        0x9,
        (
            "コウキ……\x01",
            "その話は本当なんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "ええ、ガキんちょどもの\x01",
            "言ってることッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "オレァ信じらんねえ、\x01",
            "ってか信じてたまるかァッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "あのヴァルドさんが\x01",
            "一方的にやられるなんざァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00105F（これって……\x01",
            "  雨の日の対決のことを\x01",
            "  言っているのかしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00001F（ああ……だろうな。）\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x105,
        "#10303F（………………）\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x105, 500)

    #C0080
    ChrTalk(
        0x9,
        (
            "て、てめえ……\x01",
            "どのツラ下げてここに来た！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1EAC():
        TurnDirection(0x8, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EAC)
    TurnDirection(0xC, 0x105, 500)

    #C0081
    ChrTalk(
        0xC,
        "ワ、ワジ……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "ヒャハ、今度は俺たちってかァ？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "いいぜ、オモテ出ろやァ！\x01",
            "返り討ちにしてやらァアア～ッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00005Fお、おい……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0085
    ChrTalk(
        0x9,
        "――止めろ、ルガノフ！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "ガキどもの話が本当だとしても、\x01",
            "ここで手を出したらヴァルドさんの\x01",
            "顔を潰すことになる……！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "それに、そんなことをしても\x01",
            "ヴァルドさんは喜ばねえぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "ちいッ、クソがァ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 500)

    #C0089
    ChrTalk(
        0xC,
        (
            "……どういうつもりで\x01",
            "ここへ来たかは知らねえが。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        (
            "争う気がないってんなら、\x01",
            "さっさと出てってくれねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "もっとも、喧嘩売りに\x01",
            "来たってんなら話は別だけどよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        (
            "#10303Fいや、そんなつもりはないさ。\x02\x03",

            "#10300F邪魔したね。\x01",
            "……行こうか、みんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00005Fあ、ああ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x0)
    OP_93(0x9, 0x13B, 0x0)
    OP_93(0xC, 0x87, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x14D, 0)
    EventEnd(0x5)
    Return()

    # Function_9_1C0A end

    def Function_10_2170(): pass

    label("Function_10_2170")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2264")

    #C0094
    ChrTalk(
        0xFE,
        (
            "俺はまだ、ヴァルドさんを\x01",
            "許したわけじゃねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……わけじゃねえが……\x01",
            "サーベルバイパーってとこが\x01",
            "すげえ楽しい場所だったのは確かだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "だったらバイパーの幹部として……\x01",
            "守っていくのがスジってもんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22EB")

    label("loc_2264")


    #C0097
    ChrTalk(
        0xFE,
        (
            "俺はまだ、ヴァルドさんを\x01",
            "許したわけじゃねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "バイパーの幹部として、\x01",
            "この大切な場所を守っていくのが\x01",
            "スジってもんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EB")

    Jump("loc_270E")

    label("loc_22F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_238B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230B")
    Call(0, 11)
    Jump("loc_2386")

    label("loc_230B")


    #C0099
    ChrTalk(
        0xFE,
        (
            "……くそっ。\x01",
            "よりによって青坊主と\x01",
            "協力するなんざ……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ルガノフ、コウキ、ディーノ……\x01",
            "アイツらなに考えてやがる……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2386")

    Jump("loc_270E")

    label("loc_238B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2399")
    Jump("loc_270E")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23A7")
    Jump("loc_270E")

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_244C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C2")
    Call(0, 12)
    Jump("loc_2447")

    label("loc_23C2")


    #C0101
    ChrTalk(
        0xFE,
        (
            "ん？　支援課か……\x01",
            "どうやらお互い進展はなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "いいか、今度\x01",
            "ヴァルドさんを見かけたら\x01",
            "すぐにオレたちに声を掛けろよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2447")

    Jump("loc_270E")

    label("loc_244C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FE")

    #C0103
    ChrTalk(
        0xFE,
        (
            "……俺たちが言いたいことは、\x01",
            "ルガノフが大体言ってくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "他に話すことはねえ。\x01",
            "……今日の所は失せるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x105,
        "#10303F…………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_253D")

    label("loc_24FE")


    #C0106
    ChrTalk(
        0xFE,
        (
            "俺たちが話すことはもうねえ。\x01",
            "……今日の所は失せるんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253D")

    Jump("loc_270E")

    label("loc_2542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255D")
    Call(0, 5)
    Jump("loc_2590")

    label("loc_255D")


    #C0107
    ChrTalk(
        0xFE,
        (
            "ヴァルドさん……\x01",
            "一体アンタに何があったんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2590")

    Jump("loc_270E")

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B0")
    Call(0, 6)
    Jump("loc_25E5")

    label("loc_25B0")


    #C0108
    ChrTalk(
        0xFE,
        (
            "ヴァルドさん……\x01",
            "マジでどこへ行ったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E5")

    Jump("loc_270E")

    label("loc_25EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_25FB")
    Call(0, 13)
    Jump("loc_270E")

    label("loc_25FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_260C")
    Call(0, 14)
    Jump("loc_270E")

    label("loc_260C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_261D")
    Call(0, 16)
    Jump("loc_270E")

    label("loc_261D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2638")
    Call(0, 9)
    Jump("loc_26A6")

    label("loc_2638")


    #C0109
    ChrTalk(
        0xFE,
        (
            "争う気がないなら、\x01",
            "さっさと出て行きやがれ……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "これ以上いられると、\x01",
            "正直オレもどうなるか分からねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A6")

    Jump("loc_270E")

    label("loc_26AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C6")
    Call(0, 17)
    Jump("loc_2700")

    label("loc_26C6")


    #C0111
    ChrTalk(
        0xFE,
        (
            "いいか、ワジ……\x01",
            "このまま無事でいられると\x01",
            "思うなよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2700")

    Jump("loc_270E")

    label("loc_2705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_270E")

    label("loc_270E")

    TalkEnd(0xFE)
    Return()

    # Function_10_2170 end

    def Function_11_2712(): pass

    label("Function_11_2712")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0112
    ChrTalk(
        0x9,
        (
            "あいつら……\x01",
            "よりによって青坊主どもに\x01",
            "協力なんてしやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "……ジェドさん。\x01",
            "やっぱり俺たちも協力したほうが\x01",
            "よくないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "ヒャハ、何言ってんだヒューイ！\x01",
            "バイパーとしちゃ、裏切りモンは\x01",
            "きちんとシメてやって……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "……バイパーは解散したって\x01",
            "言ってるだろうが、バカ野郎！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0116
    ChrTalk(
        0xB,
        "ス、スンマセン。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "……とにかく、今は考え中だ。\x01",
            "お前らも勝手なことはするなよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_2712 end

    def Function_12_28C0(): pass

    label("Function_12_28C0")

    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0118
    ChrTalk(
        0x9,
        (
            "ちっ、よく分かんねえが\x01",
            "騒がしいことになってんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "はい、街の方もマインツ占領の\x01",
            "話題一色って感じッスからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "まさか、ヴァルドさん……\x01",
            "事件に巻き込まれてたり\x01",
            "していないッスよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "まあ流石にそれはないと思うが……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "とにかくテメエら、\x01",
            "今日も気合い入れて情報を集めんぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        "#2Pオッス！\x02",
    )


    #C0124
    ChrTalk(
        0xB,
        "#3Pオッス！\x02",
    )

    OP_57(0x1)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_28C0 end

    def Function_13_2A34(): pass

    label("Function_13_2A34")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C96")

    #C0125
    ChrTalk(
        0xC,
        (
            "ヴァルドさん……\x01",
            "今頃どうしてるんスかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "さあな……\x01",
            "しばらく寝ぐらの方にも\x01",
            "帰っていないようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "ちらっとも見かけなくなって、\x01",
            "もう３日になるんスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "港湾区の方でヒューイさんたちが\x01",
            "見かけたのを最後に……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "ああ、それも声を掛けたのに\x01",
            "無視されたっつう話だったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "……ともかく、ヴァルドさんに\x01",
            "何かあったってんならコトだ。\x01",
            "手分けして心当たりを探すぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "お前ら２人はこの旧市街だ。\x01",
            "色んなヤツに片っ端から聞いて回れ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        "オッス！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        "了解ッス！\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#00005F（ヴァルド……\x01",
            "  所在が分からないのか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x105,
        "#10303F（何だろう……気になるね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D15")

    label("loc_2C96")


    #C0136
    ChrTalk(
        0x9,
        (
            "イグニスには、俺とルガノフが\x01",
            "交代で詰めておくからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        "何かあったらすぐに報告に来いよ。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        "オッス！\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xD,
        "了解ッス！\x02",
    )

    CloseMessageWindow()

    label("loc_2D15")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_2A34 end

    def Function_14_2D22(): pass

    label("Function_14_2D22")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE8")

    #C0140
    ChrTalk(
        0x9,
        (
            "どうだ、昨日はあれから\x01",
            "ヴァルドさんの姿を見たか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        "いえ、俺の方は全然……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xD,
        "お、俺もッス。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "そうか、昨日の様子からすりゃ\x01",
            "二日酔いって所だとは思うが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E5D")

    label("loc_2DE8")


    #C0144
    ChrTalk(
        0x9,
        (
            "そうだな……後でまた\x01",
            "寝ぐらの様子でも見に行くか。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "お前らも付いて来いよ。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        "オッス！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xD,
        "もちろんッス！\x02",
    )

    CloseMessageWindow()

    label("loc_2E5D")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_2D22 end

    def Function_15_2E6A(): pass

    label("Function_15_2E6A")

    EventBegin(0x0)
    Fade(500)
    OP_68(5960, 1000, -720, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 1660, 0, -200, 90)
    SetChrPos(0x102, 1860, 0, 1200, 90)
    SetChrPos(0x104, 1660, 0, -1610, 90)
    SetChrPos(0x109, 730, 0, 610, 90)
    SetChrPos(0x105, 330, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_0D()

    #C0148
    ChrTalk(
        0x9,
        "そうか……ヴァルドさんが……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "ええ、人目もはばからず、\x01",
            "フラフラしながら店の方に……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        (
            "相当な量を買い込んでいたから\x01",
            "今頃また寝ぐらの方で\x01",
            "呑んでいるんじゃないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xC,
        (
            "正直……\x01",
            "あんなヴァルドさんの姿、\x01",
            "見たくなかったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "まさか、あの人が……\x01",
            "酒に呑まれてしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "……ああ、俺も同じ気持ちだ。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "ともかく……\x01",
            "路上で酔い潰れたりされると\x01",
            "色々マズイことになりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "引き続き、\x01",
            "全員で気に掛けていくぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xC,
        "オッス！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xD,
        "了解です！\x02",
    )

    CloseMessageWindow()
    OP_68(1930, 1000, -40, 1500)
    OP_6F(0x1)

    #C0158
    ChrTalk(
        0x101,
        "#00005Fヴァルドがそんなことに……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#12P#00301Fいわゆる自棄#4Rヤ　ケ#酒っつうヤツか。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#00103Fあまり大量だと\x01",
            "身体の方が心配だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x105,
        "#6P#10308F………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x14D, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 500, 0, 0, 90)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_15_2E6A end

    def Function_16_31FE(): pass

    label("Function_16_31FE")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0162
    ChrTalk(
        0x9,
        (
            "いいか、何かあったら\x01",
            "すぐに俺かルガノフを呼べよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        "オッス！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xD,
        "了解です！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_31FE end

    def Function_17_326C(): pass

    label("Function_17_326C")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xC, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0165
    ChrTalk(
        0xD,
        "お、お前ら……！\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        "特務支援課……それにワジ！\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "……どうやら、ヴァルドさんには\x01",
            "まだ会っていないようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0168
    ChrTalk(
        0x105,
        "#10305Fヴァルドがどうかしたのかい？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xD,
        "そ、それは……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "黙ってろ、ディーノ。\x01",
            "サツに尻尾を振る腰抜け野郎に\x01",
            "話すことなんて何もねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        "分かったらとっとと失せやがれ。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        "#10303F……やれやれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 4)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xC, 0x87, 0x0)
    OP_93(0xD, 0x13B, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_326C end

    def Function_18_3412(): pass

    label("Function_18_3412")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3423")
    Jump("loc_37BB")

    label("loc_3423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343E")
    Call(0, 11)
    Jump("loc_3481")

    label("loc_343E")


    #C0173
    ChrTalk(
        0xFE,
        (
            "（なんだかんだ言って、\x01",
            "  ジェドさんも迷ってるみたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3481")

    Jump("loc_37BB")

    label("loc_3486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3494")
    Jump("loc_37BB")

    label("loc_3494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34A2")
    Jump("loc_37BB")

    label("loc_34A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_351E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BD")
    Call(0, 12)
    Jump("loc_3519")

    label("loc_34BD")


    #C0174
    ChrTalk(
        0xFE,
        (
            "正体不明の武装集団か……\x01",
            "もし襲われたとしても流石に\x01",
            "返り討ちってワケにはいかねえよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3519")

    Jump("loc_37BB")

    label("loc_351E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_355B")

    #C0175
    ChrTalk(
        0xFE,
        (
            "ルガノフさん……\x01",
            "マジでかっこよかったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BB")

    label("loc_355B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_35AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3576")
    Call(0, 5)
    Jump("loc_35A7")

    label("loc_3576")


    #C0176
    ChrTalk(
        0xFE,
        (
            "１０万ミラって、\x01",
            "そんな大金どうやったら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A7")

    Jump("loc_37BB")

    label("loc_35AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C7")
    Call(0, 6)
    Jump("loc_364C")

    label("loc_35C7")


    #C0177
    ChrTalk(
        0xFE,
        (
            "色々聞いて回ったんスけど……\x01",
            "ここ最近は、マジで誰も\x01",
            "見てないって言うんスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "流石に街を出たとは\x01",
            "思いたくないッスけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364C")

    Jump("loc_37BB")

    label("loc_3651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3662")
    Call(0, 7)
    Jump("loc_37BB")

    label("loc_3662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3673")
    Call(0, 8)
    Jump("loc_37BB")

    label("loc_3673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371E")

    #C0179
    ChrTalk(
        0xFE,
        (
            "ハッ……\x01",
            "さっきはおかしなヤツに\x01",
            "気を削がれちまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……次はねえからな。\x01",
            "覚えてろよ、ワジ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x105,
        "#10303F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_374B")

    label("loc_371E")


    #C0182
    ChrTalk(
        0xFE,
        (
            "……次はねえからな。\x01",
            "覚えてろよ、ワジ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374B")

    Jump("loc_37BB")

    label("loc_3750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376B")
    Call(0, 19)
    Jump("loc_379C")

    label("loc_376B")


    #C0183
    ChrTalk(
        0xFE,
        (
            "て、てめえ……\x01",
            "もっとマシなことを考えろや！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_379C")

    Jump("loc_37BB")

    label("loc_37A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_37B2")
    Call(0, 20)
    Jump("loc_37BB")

    label("loc_37B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37BB")

    label("loc_37BB")

    TalkEnd(0xFE)
    Return()

    # Function_18_3412 end

    def Function_19_37BF(): pass

    label("Function_19_37BF")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0184
    ChrTalk(
        0xA,
        "で、いい案は思いついたかよ？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "おうよ！　実は今朝ここへ来る前に\x01",
            "パンを山ほど抱えたシスターを\x01",
            "見かけたんだけどよォ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xB,
        "それがもう、可愛いの何のってよォ！\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "……アア？　その話がどう\x01",
            "ヴァルドさんの機嫌取りに\x01",
            "つながるってんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "ああ、だから\x01",
            "今度そのシスターをナンパしに\x01",
            "教会に行ってだなァ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0189
    ChrTalk(
        0xA,
        "てめえ、頭おかしいだろ！？\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "何で俺たちが教会になんか\x01",
            "行かなきゃならねえンだよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_19_37BF end

    def Function_20_397E(): pass

    label("Function_20_397E")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B57")

    #C0191
    ChrTalk(
        0xB,
        (
            "ハァ、今朝のヴァルドさん、\x01",
            "マジでおっかなかったよなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "っつうかさ……\x01",
            "ヴァルドさんは何であそこまで\x01",
            "ワジの野郎にこだわるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "とにかく一番厄介なヤツが\x01",
            "いなくなったんだ。\x01",
            "むしろ喜ぶべきっつうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "おいコラ、スラッシュ！\x01",
            "滅多なこと口にしてンじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "オレたちがヴァルドさんに\x01",
            "意見しようなんざ百万年早ェんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        (
            "んなことより、どうすりゃ\x01",
            "キゲン直してもらえるか考えろや！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "あ、ああ。\x01",
            "んなこたァ分かってるがよォ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BD4")

    label("loc_3B57")


    #C0198
    ChrTalk(
        0xA,
        (
            "ったく、今みたいな話を\x01",
            "ヴァルドさんに聞かれてみろ。\x01",
            "半殺しじゃすまねえぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "わ、悪かったよ。\x01",
            "もう言わねえって……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD4")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_20_397E end

    def Function_21_3BDD(): pass

    label("Function_21_3BDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3BEE")
    Jump("loc_3F60")

    label("loc_3BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C09")
    Call(0, 11)
    Jump("loc_3C29")

    label("loc_3C09")


    #C0200
    ChrTalk(
        0xFE,
        "ヒャハ、怒られちまった……\x02",
    )

    CloseMessageWindow()

    label("loc_3C29")

    Jump("loc_3F60")

    label("loc_3C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C3C")
    Jump("loc_3F60")

    label("loc_3C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C4A")
    Jump("loc_3F60")

    label("loc_3C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C65")
    Call(0, 12)
    Jump("loc_3CC5")

    label("loc_3C65")


    #C0201
    ChrTalk(
        0xFE,
        (
            "えっと……\x01",
            "トンカチと釘はどこにやったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "念のため、\x01",
            "棍棒を増強しとかねえとなァ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC5")

    Jump("loc_3F60")

    label("loc_3CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D05")

    #C0203
    ChrTalk(
        0xFE,
        (
            "くう～、やっぱ\x01",
            "先輩方はサイコーだよな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F60")

    label("loc_3D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D20")
    Call(0, 5)
    Jump("loc_3D5D")

    label("loc_3D20")


    #C0204
    ChrTalk(
        0xFE,
        (
            "だァもー、ワケ分かんなって来た。\x01",
            "誰か説明してくれよォ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5D")

    Jump("loc_3F60")

    label("loc_3D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7D")
    Call(0, 6)
    Jump("loc_3DD7")

    label("loc_3D7D")


    #C0205
    ChrTalk(
        0xFE,
        (
            "相変わらず、寝ぐらの方にも\x01",
            "帰っていないみたいッスけど……\x01",
            "どこで寝泊りしてんスかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD7")

    Jump("loc_3F60")

    label("loc_3DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DED")
    Call(0, 7)
    Jump("loc_3F60")

    label("loc_3DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DFE")
    Call(0, 8)
    Jump("loc_3F60")

    label("loc_3DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E93")

    #C0206
    ChrTalk(
        0xFE,
        (
            "ヒャハ、世の中には\x01",
            "ヘンな野郎がいるもんだなァ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "……あれ、そういえば俺とヒューイ、\x01",
            "ケンカしてなかったっけか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EE8")

    label("loc_3E93")


    #C0208
    ChrTalk(
        0xFE,
        "……まあ、小せえことはいいかァ。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "今はヴァルドさんのことを\x01",
            "考えねえとなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE8")

    Jump("loc_3F60")

    label("loc_3EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F08")
    Call(0, 19)
    Jump("loc_3F41")

    label("loc_3F08")


    #C0210
    ChrTalk(
        0xFE,
        (
            "そ、そういうてめえこそ\x01",
            "ロクな案ださねえくせによォ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F41")

    Jump("loc_3F60")

    label("loc_3F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F57")
    Call(0, 20)
    Jump("loc_3F60")

    label("loc_3F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3F60")

    label("loc_3F60")

    TalkEnd(0xFE)
    Return()

    # Function_21_3BDD end

    def Function_22_3F64(): pass

    label("Function_22_3F64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_401E")

    #C0211
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんが戻ってくるまでは、\x01",
            "幹部のジェドさんとルガノフさんが\x01",
            "サーベルバイパーを引っ張ることになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "皆で協力して、バイパーを\x01",
            "守っていかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4241")

    label("loc_401E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_402C")
    Jump("loc_4241")

    label("loc_402C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_403A")
    Jump("loc_4241")

    label("loc_403A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4048")
    Jump("loc_4241")

    label("loc_4048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4063")
    Call(0, 23)
    Jump("loc_4090")

    label("loc_4063")


    #C0213
    ChrTalk(
        0xFE,
        (
            "ヴァルドさん、\x01",
            "今頃何してんだろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4090")

    Jump("loc_4241")

    label("loc_4095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4132")

    #C0214
    ChrTalk(
        0xFE,
        (
            "よく考えりゃ、幹部のお２人は\x01",
            "サーベルバイパー結成当時からの\x01",
            "メンバーなんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "俺たちなんかよりも\x01",
            "ずっとヴァルドさんのことを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4241")

    label("loc_4132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414D")
    Call(0, 5)
    Jump("loc_4180")

    label("loc_414D")


    #C0216
    ChrTalk(
        0xFE,
        (
            "ヴァルドさん……\x01",
            "オレら以外にいったい誰と……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4180")

    Jump("loc_4241")

    label("loc_4185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4193")
    Jump("loc_4241")

    label("loc_4193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41A4")
    Call(0, 13)
    Jump("loc_4241")

    label("loc_41A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_41B5")
    Call(0, 14)
    Jump("loc_4241")

    label("loc_41B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41C6")
    Call(0, 16)
    Jump("loc_4241")

    label("loc_41C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4202")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E1")
    Call(0, 9)
    Jump("loc_41FD")

    label("loc_41E1")


    #C0217
    ChrTalk(
        0xFE,
        "は、早くどっか行けよ！\x02",
    )

    CloseMessageWindow()

    label("loc_41FD")

    Jump("loc_4241")

    label("loc_4202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_421D")
    Call(0, 17)
    Jump("loc_4233")

    label("loc_421D")


    #C0218
    ChrTalk(
        0xFE,
        "ヴァルドさん……\x02",
    )

    CloseMessageWindow()

    label("loc_4233")

    Jump("loc_4241")

    label("loc_4238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4241")

    label("loc_4241")

    TalkEnd(0xFE)
    Return()

    # Function_22_3F64 end

    def Function_23_4245(): pass

    label("Function_23_4245")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0219
    ChrTalk(
        0xD,
        (
            "ヴァルドさん……\x01",
            "やっぱり今日も見かけないッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "そうだな……\x01",
            "何かスゲエ騒ぎにもなってんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "……とにかく、\x01",
            "無事でいてくれりゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_23_4245 end

    def Function_24_4301(): pass

    label("Function_24_4301")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4312")
    Jump("loc_481F")

    label("loc_4312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4320")
    Jump("loc_481F")

    label("loc_4320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_432E")
    Jump("loc_481F")

    label("loc_432E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_463A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45EF")
    OP_4B(0xFE, 0xFF)

    #C0222
    ChrTalk(
        0xFE,
        "ヴァルドさん……みんな……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        "#00108F……ディーノ君…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0224
    ChrTalk(
        0xFE,
        "……なんだ、特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00003F他のメンバーは……\x01",
            "まだ入院中なんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "ああ、オレ以外のメンバーはみんな……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "特にコウキさんが酷くて……\x01",
            "……今もみんなとは別の病室で……\x01",
            "うぅ、ひぐっ……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#00008Fすまない……少し無神経だったな。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "ひぐっ……べ、別に……\x01",
            "俺なんかを気遣う必要なんてねえよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "先輩たちはツライ思いを\x01",
            "してるってのに俺だけ無事で……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "うぅ……くそっ！\x01",
            "なんで……なんでこんなことに……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#00208F（ロイドさん……\x01",
            "  今は１人にしてあげましょう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        "#00003F（ああ……そうだな。）\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x105,
        "#10308F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x87, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 3)
    Jump("loc_4635")

    label("loc_45EF")


    #C0235
    ChrTalk(
        0xFE,
        "ヴァルドさん……みんな……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "なんで……なんでこんなことに……\x02",
    )

    CloseMessageWindow()

    label("loc_4635")

    Jump("loc_481F")

    label("loc_463A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4655")
    Call(0, 23)
    Jump("loc_46B5")

    label("loc_4655")


    #C0237
    ChrTalk(
        0xFE,
        "グノーシス、か……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "ヴァルドさん、\x01",
            "ルバーチェもいないってのに\x01",
            "あんなのを一体どこで……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B5")

    Jump("loc_481F")

    label("loc_46BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_472F")

    #C0239
    ChrTalk(
        0xFE,
        "へへっ、やっぱり先輩方は偉大だな。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "こんな時になんだけど……\x01",
            "俺、何だかちょっとだけ嬉しいや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481F")

    label("loc_472F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4790")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474A")
    Call(0, 5)
    Jump("loc_478B")

    label("loc_474A")


    #C0241
    ChrTalk(
        0xFE,
        (
            "うぅ……ヴァルドさん。\x01",
            "まさか危険な仕事でもしてるんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478B")

    Jump("loc_481F")

    label("loc_4790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47A1")
    Call(0, 13)
    Jump("loc_481F")

    label("loc_47A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47B2")
    Call(0, 14)
    Jump("loc_481F")

    label("loc_47B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47C3")
    Call(0, 16)
    Jump("loc_481F")

    label("loc_47C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_481F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47DE")
    Call(0, 17)
    Jump("loc_481F")

    label("loc_47DE")


    #C0242
    ChrTalk(
        0xFE,
        (
            "ジェ、ジェドさんの言う通り\x01",
            "話すことなんて何もないからなっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481F")

    TalkEnd(0xFE)
    Return()

    # Function_24_4301 end

    def Function_25_4823(): pass

    label("Function_25_4823")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(8510, 900, 300, 0)
    MoveCamera(48, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 1000, 0, -700, 90)
    SetChrPos(0x105, 1000, 0, 700, 90)
    SetChrPos(0x102, 500, 0, -700, 90)
    SetChrPos(0x103, 500, 0, 700, 90)
    SetChrPos(0x109, 0, 0, -700, 90)
    SetChrPos(0x104, 0, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)

    def lambda_48E9():
        OP_96(0xFE, 0x1C20, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48E9)
    Sleep(400)

    def lambda_4906():
        OP_96(0xFE, 0x1CE8, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4906)
    Sleep(400)

    def lambda_4923():
        OP_96(0xFE, 0x170C, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4923)
    Sleep(400)

    def lambda_4940():
        OP_96(0xFE, 0x1900, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4940)
    Sleep(400)

    def lambda_495D():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_495D)
    Sleep(400)

    def lambda_497A():
        OP_96(0xFE, 0x13EC, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_497A)
    Sleep(400)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x104, 1)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4A00():

        label("loc_4A00")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A00")

    QueueWorkItem2(0x9, 2, lambda_4A00)

    def lambda_4A12():

        label("loc_4A12")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A12")

    QueueWorkItem2(0xC, 2, lambda_4A12)

    def lambda_4A24():

        label("loc_4A24")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A24")

    QueueWorkItem2(0xD, 2, lambda_4A24)

    #C0243
    ChrTalk(
        0x9,
        "#11Pサツが……また来たのかよ。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xC,
        "#11Pもしかして、新しい情報でも……\x02",
    )

    CloseMessageWindow()

    def lambda_4A82():

        label("loc_4A82")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A82")

    QueueWorkItem2(0x8, 2, lambda_4A82)

    def lambda_4A94():

        label("loc_4A94")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4A94")

    QueueWorkItem2(0xB, 2, lambda_4A94)

    def lambda_4AA6():

        label("loc_4AA6")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4AA6")

    QueueWorkItem2(0xA, 2, lambda_4AA6)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4AD3():

        label("loc_4AD3")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4AD3")

    QueueWorkItem2(0xD, 2, lambda_4AD3)

    #C0245
    ChrTalk(
        0xD,
        "#11P……って、お前はワジ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0246
    ChrTalk(
        0x105,
        "#6P#10308F…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_4BB0():

        label("loc_4BB0")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BB0")

    QueueWorkItem2(0x8, 2, lambda_4BB0)

    def lambda_4BC2():

        label("loc_4BC2")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BC2")

    QueueWorkItem2(0xB, 2, lambda_4BC2)

    def lambda_4BD4():

        label("loc_4BD4")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BD4")

    QueueWorkItem2(0xA, 2, lambda_4BD4)

    def lambda_4BE6():

        label("loc_4BE6")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BE6")

    QueueWorkItem2(0x9, 2, lambda_4BE6)

    def lambda_4BF8():

        label("loc_4BF8")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4BF8")

    QueueWorkItem2(0xC, 2, lambda_4BF8)

    #C0247
    ChrTalk(
        0xA,
        "#5Pて、てめえ……！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "#5Pよくも、ぬけぬけと……\x01",
            "てめえのせいでヴァルドさんは！\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#12P#00001F（くっ……さすがに険悪なムードだな。）\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        "#6P#00208F（来たのはまずかったでしょうか……）\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        "#5P…………………\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x40)

    def lambda_4CEC():
        OP_96(0xFE, 0x215C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CEC)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x105, 500)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0252
    ChrTalk(
        0x9,
        "#11Pおい、ルガノフ……？\x02",
    )

    CloseMessageWindow()

    def lambda_4DEC():

        label("loc_4DEC")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4DEC")

    QueueWorkItem2(0x101, 2, lambda_4DEC)

    def lambda_4DFE():

        label("loc_4DFE")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4DFE")

    QueueWorkItem2(0x102, 2, lambda_4DFE)

    def lambda_4E10():

        label("loc_4E10")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4E10")

    QueueWorkItem2(0x103, 2, lambda_4E10)

    def lambda_4E22():

        label("loc_4E22")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4E22")

    QueueWorkItem2(0x109, 2, lambda_4E22)

    def lambda_4E34():

        label("loc_4E34")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4E34")

    QueueWorkItem2(0x104, 2, lambda_4E34)

    def lambda_4E46():

        label("loc_4E46")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4E46")

    QueueWorkItem2(0x105, 2, lambda_4E46)

    def lambda_4E58():
        OP_95(0xFE, 8039, 0, 570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E58)
    Sleep(50)
    WaitChrThread(0x8, 1)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x4)
    Sound(802, 0, 100, 0)

    def lambda_4E8D():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4E8D)

    def lambda_4EA6():
        OP_96(0xFE, 0x1CE8, 0xC8, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4EA6)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x105, 2)
    ClearChrFlags(0x105, 0x20)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 26)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x104, 3)
    Sleep(1000)

    #C0253
    ChrTalk(
        0x105,
        "#6P#10310F…………っ………………\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#12P#00011Fお、おい……！\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#6P#10111Fワジ君……！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0256
    ChrTalk(
        0x8,
        (
            "#4S#11Pよぉ、ワジィ！\x01",
            "分かってンよなァ～ッ！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0257
    ChrTalk(
        0x8,
        (
            "#4S#11Pよりにもよって、ヴァルドさんが\x01",
            "クスリに手を出しただァ～ッ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0258
    ChrTalk(
        0x8,
        (
            "#4S#11Pこれもゼンブ……\x01",
            "ゼンブ、テメエのせいだろォオ！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        (
            "#6P#00101F（ロ、ロイド……\x01",
            "  彼らにはどこまで教えたの？）\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#12P#00003F（ああ、さすがに魔人化の\x01",
            "  ことまでは言っていないけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        (
            "#6P#N#10108F（……でも、グノーシスを服用した\x01",
            "  可能性については伝えました。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0262
    ChrTalk(
        0x8,
        (
            "#11P……２年前、テメエが来なけりゃ\x01",
            "オレたちはずっと……\x01",
            "ずっと楽しくやってたんだ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "#11Pそこへテメェが突然やって来て……\x01",
            "オマケに今度はサツ入りなんつう\x01",
            "ワケの分からねえ気紛れのせいで……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0264
    ChrTalk(
        0x8,
        "#11P#4S……分かってんのかコラァ！！#3S\x02",
    )

    CloseMessageWindow()

    def lambda_532B():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_532B)
    WaitChrThread(0x105, 2)

    #C0265
    ChrTalk(
        0x105,
        (
            "#6P#10303F……気紛れのつもりはない。\x01",
            "僕にとって必要な事だったから、\x01",
            "この道を選んだというだけの事さ。\x02\x03",

            "#10308Fその結果、ヴァルドが\x01",
            "あんな事になったのは……\x01",
            "流石に予想外だったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#6P#00303F……ワジ……\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        "#11P……だから抵抗はしませんってかァ？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0268
    ChrTalk(
        0x8,
        "#11P#4S……上等だァ、ぶっ殺してやらァアッ！#3S\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x103,
        "#6P#00210F！！\x02",
    )

    CloseMessageWindow()

    def lambda_54A4():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_54A4)
    WaitChrThread(0x105, 2)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Sound(811, 0, 100, 0)

    def lambda_54E2():
        OP_9D(0xFE, 0x1A2C, 0x0, 0x2BC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_54E2)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x8, 0x40)
    WaitChrThread(0x105, 1)
    Sleep(500)

    #C0270
    ChrTalk(
        0x102,
        "#N#6P#00105Fあ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_5529():

        label("loc_5529")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5529")

    QueueWorkItem2(0x101, 2, lambda_5529)

    def lambda_553B():

        label("loc_553B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_553B")

    QueueWorkItem2(0x102, 2, lambda_553B)

    def lambda_554D():

        label("loc_554D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_554D")

    QueueWorkItem2(0x103, 2, lambda_554D)

    def lambda_555F():

        label("loc_555F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_555F")

    QueueWorkItem2(0x109, 2, lambda_555F)

    def lambda_5571():

        label("loc_5571")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5571")

    QueueWorkItem2(0x104, 2, lambda_5571)

    #C0271
    ChrTalk(
        0xC,
        "#11Pえ……？\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x105,
        "#6P#10305F…………何のつもりだい？\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x8,
        (
            "#11P……ぶっちゃけ\x01",
            "今のあの人にオレらの声は届かねえ。\x01",
            "届くとしたら……テメエの声だけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#11P……いいか、コイツは貸しだ。\x01",
            "ゲンコ一発の代わりに……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0275
    ChrTalk(
        0x8,
        (
            "#4S#11Pテメエが責任持って、\x01",
            "ヴァルドさんの目を覚まさせてこいやァア！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        "#11Pルガノフ……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xD,
        "#11Pせ、先輩……\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)

    #C0278
    ChrTalk(
        0x105,
        (
            "#6P#10308F……フフ、そういうことか。\x02\x03",

            "#10303F………………………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5744():

        label("loc_5744")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5744")

    QueueWorkItem2(0x101, 2, lambda_5744)

    def lambda_5756():

        label("loc_5756")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5756")

    QueueWorkItem2(0x102, 2, lambda_5756)

    def lambda_5768():

        label("loc_5768")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5768")

    QueueWorkItem2(0x103, 2, lambda_5768)

    def lambda_577A():

        label("loc_577A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_577A")

    QueueWorkItem2(0x109, 2, lambda_577A)

    def lambda_578C():

        label("loc_578C")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_578C")

    QueueWorkItem2(0x104, 2, lambda_578C)

    #C0279
    ChrTalk(
        0x101,
        "#12P#00005Fワジ……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x105,
        (
            "#6P#10303F……約束はできないけど……\x01",
            "出来る限りの手は尽くさせてもらうよ。\x02\x03",

            "#10301Fテスタメンツのヘッドとして……\x01",
            "彼につけ損ねたケジメを\x01",
            "改めてつける意味でもね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    SetChrPos(0x8, 16290, 1000, -1650, 315)
    SetChrPos(0x9, 15290, 1000, -650, 135)
    SetChrPos(0xA, 11110, 0, -5220, 315)
    SetChrPos(0xB, 9940, 0, -4200, 135)
    SetChrPos(0xC, 7030, 0, -50, 180)
    SetChrPos(0xD, 7320, 0, -1690, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrPos(0x0, 2500, 0, -590, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x16F, 1)
    EventEnd(0x5)
    Return()

    # Function_25_4823 end

    def Function_26_5968(): pass

    label("Function_26_5968")


    def lambda_596D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_596D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_5968 end

    SaveToFile()

Try(main)
