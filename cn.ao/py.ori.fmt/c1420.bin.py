from ScenarioHelper import *

def main():
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
        "诺加诺夫",               # 1
        "杰德",                   # 2
        "修伊",                   # 3
        "斯拉修",                 # 4
        "寇奇",                   # 5
        "迪诺",                   # 6
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
        "Function_5_F7A",          # 05, 5
        "Function_6_1456",         # 06, 6
        "Function_7_15C7",         # 07, 7
        "Function_8_16F9",         # 08, 8
        "Function_9_1916",         # 09, 9
        "Function_10_1DE6",        # 0A, 10
        "Function_11_22B0",        # 0B, 11
        "Function_12_23FE",        # 0C, 12
        "Function_13_252C",        # 0D, 13
        "Function_14_27A0",        # 0E, 14
        "Function_15_28C2",        # 0F, 15
        "Function_16_2BDE",        # 10, 16
        "Function_17_2C48",        # 11, 17
        "Function_18_2DBA",        # 12, 18
        "Function_19_311F",        # 13, 19
        "Function_20_328C",        # 14, 20
        "Function_21_347F",        # 15, 21
        "Function_22_3775",        # 16, 22
        "Function_23_39F4",        # 17, 23
        "Function_24_3A8C",        # 18, 24
        "Function_25_3F52",        # 19, 25
        "Function_26_4F5B",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC6")

    #C0001
    ChrTalk(
        0xFE,
        "ＹＥＡＨ、ＹＥＡＨ～～～！！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "我才不会害怕呢～～！！\x01",
            "现在可没空理会\x01",
            "那些莫名其妙的事情～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "一起尽情高歌，吹散不安吧，\x01",
            "咿咿～～～～～呀哈～～！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B34")

    label("loc_AC6")


    #C0004
    ChrTalk(
        0xFE,
        (
            "那大树连个屁都不算～！\x01",
            "我才不会害怕呢～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "一起尽情高歌，吹散不安吧，\x01",
            "咿咿～～～～～呀哈～～！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B34")

    Jump("loc_F76")

    label("loc_B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B47")
    Jump("loc_F76")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B55")
    Jump("loc_F76")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B63")
    Jump("loc_F76")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BEA")

    #C0006
    ChrTalk(
        0xFE,
        (
            "唔唔唔……\x01",
            "哼，可恶！总是觉得焦躁不安！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "玛因兹发生了袭击事件！？\x01",
            "比起那种事，\x01",
            "我更想知道瓦鲁多大哥在哪里～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F76")

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C41")

    #C0008
    ChrTalk(
        0xFE,
        (
            "哼，话说在先，你欠我一拳，\x01",
            "作为回报，你必须要让瓦鲁多大哥清醒过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F76")

    label("loc_C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5C")
    Call(0, 5)
    Jump("loc_CAA")

    label("loc_C5C")


    #C0009
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥……\x01",
            "在巴鲁卡大赚了一票吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "可是，为什么\x01",
            "不告诉我呢～！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA")

    Jump("loc_F76")

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCA")
    Call(0, 6)
    Jump("loc_D05")

    label("loc_CCA")


    #C0011
    ChrTalk(
        0xFE,
        (
            "呼～话说回来，瓦鲁多大哥不在了以后，\x01",
            "还真是无聊啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D05")

    Jump("loc_F76")

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D1B")
    Call(0, 7)
    Jump("loc_F76")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D2C")
    Call(0, 8)
    Jump("loc_F76")

    label("loc_D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC")

    #C0012
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥～～！\x01",
            "算我求你了，你快出现吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "我们会帮你买酒的，\x01",
            "在这里喝吧～～！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "你不在这里，\x01",
            "我们什么都做不了啊～～！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E22")

    label("loc_DCC")


    #C0015
    ChrTalk(
        0xFE,
        (
            "我们会帮你买酒的，\x01",
            "在这里喝吧～～！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "你不在这里，\x01",
            "我们什么都做不了啊～～！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E22")

    Jump("loc_F76")

    label("loc_E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E42")
    Call(0, 9)
    Jump("loc_E8C")

    label("loc_E42")


    #C0017
    ChrTalk(
        0xFE,
        (
            "无法相信……\x01",
            "我无法相信啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "那么荒唐的事情\x01",
            "怎么可能会发生……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8C")

    Jump("loc_F76")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")

    #C0019
    ChrTalk(
        0xFE,
        "ＹＥＡＨ～ＹＥＡＨ～～！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "圣书会的那些混蛋！\x01",
            "想逞威风就趁现在吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "#4S……咿咿咿～～呀哈！！#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F68")

    label("loc_F19")


    #C0022
    ChrTalk(
        0xFE,
        (
            "圣书会的那些混蛋！\x01",
            "想逞威风就趁现在吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "#4S……咿咿咿～～呀哈！！#3S\x02",
    )

    CloseMessageWindow()

    label("loc_F68")

    Jump("loc_F76")

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F76")

    label("loc_F76")

    TalkEnd(0xFE)
    Return()

    # Function_4_A07 end

    def Function_5_F7A(): pass

    label("Function_5_F7A")

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
            "嗯？你们几个，\x01",
            "调查结果如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xD,
        "嗯，这个……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xD,
        (
            "大概在一周前左右，\x01",
            "有个叫卡农的小鬼\x01",
            "曾见到过瓦鲁多大哥……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "听说瓦鲁多大哥当时\x01",
            "正在使用一个叫做\x01",
            "艾尼格玛的小型通讯终端。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        (
            "据交换店的女老板说，\x01",
            "那是个价值十万米拉\x01",
            "的高价货……\x02",
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
        "十、十万米拉～！？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "哇，真的假的……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "瓦、瓦鲁多大哥\x01",
            "究竟是从哪里搞到那么多钱的……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "这确实很令人在意……\x01",
            "寇奇，你刚才是说通讯终端吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "也就是说……\x01",
            "瓦鲁多大哥当时正在\x01",
            "和什么人联络吧？\x02",
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
            "是的，不过那小鬼\x01",
            "终究不可能连\x01",
            "对话内容都听到……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xD,
        (
            "嗯，但听说瓦鲁多大哥\x01",
            "当时笑得很开心……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "……笑、笑吗？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "是发生什么好事了吗……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "也就是说，我们竟然被\x01",
            "瓦鲁多大哥抛弃了吗……\x01",
            "应该不会有这种事吧？\x02",
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
            "斯拉修，你这小子……\x01",
            "还真敢胡说八道啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "如果想让我宰了你，不妨直说啊！\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)
    TurnDirection(0xB, 0x8, 0)

    #C0042
    ChrTalk(
        0xB,
        "对、对不起……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00001F（瓦鲁多使用艾尼格玛……\x01",
            "  的确有点令人在意呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#00203F（嗯，艾尼格玛还\x01",
            "  没有全面普及，\x01",
            "  一般人很难得到……）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        "#10303F（……瓦鲁多………………）\x02",
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

    # Function_5_F7A end

    def Function_6_1456(): pass

    label("Function_6_1456")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0046
    ChrTalk(
        0x8,
        (
            "哦，杰德，\x01",
            "寇奇和迪诺那两个小子\x01",
            "还没来吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "嗯，再等等吧，\x01",
            "他们还需要调查一些其它的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "话说回来，你们好像\x01",
            "什么消息都没有打听到吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "算是吧……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        "对、对不起。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "我们已经去所有能想到的地方\x01",
            "调查过了，但最近没有任何人\x01",
            "见过瓦鲁多大哥……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        "……是吗。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "瓦鲁多大哥……\x01",
            "究竟去了什么地方呢？\x02",
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

    # Function_6_1456 end

    def Function_7_15C7(): pass

    label("Function_7_15C7")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1668")

    #C0054
    ChrTalk(
        0x8,
        (
            "呼～总之，\x01",
            "我们就去瓦鲁多大哥\x01",
            "可能会去的地方找找看吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "搜索范围是整个城市。\x01",
            "把所有地方都搜个遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        "明白了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16EC")

    label("loc_1668")


    #C0058
    ChrTalk(
        0x8,
        (
            "哦～要是发现了瓦鲁多大哥，\x01",
            "就立刻回这里报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "如果你们直接出声搭话，\x01",
            "瓦鲁多大哥很可能会再次跑掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        "明白了！\x02",
    )

    CloseMessageWindow()

    label("loc_16EC")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_15C7 end

    def Function_8_16F9(): pass

    label("Function_8_16F9")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C3")

    #C0062
    ChrTalk(
        0x8,
        "嗯？他们说了些什么？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "那、那个……\x01",
            "他们很诚恳地道了歉……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "对方表现出那样的态度，\x01",
            "我们也没法继续挑事了……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "哼，你们真是没用啊！\x01",
            "虽然蓝衣服的小子们十分废物，\x01",
            "但你们也很缺乏气势！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "听好，在这种时候必须要向对方挑衅。\x01",
            "现在就把我压箱底的最强\x01",
            "挑衅台词教给你们，给我好好记住～\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "『你妈是个凸肚脐！』\x01",
            "……好，给我重复一遍！\x02",
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
        "哎～那、那个……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        "是、是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1909")

    label("loc_18C3")


    #C0070
    ChrTalk(
        0xA,
        "你、你妈是个……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        "凸、凸……凸肚脐。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "喂！声音太小了～！\x02",
    )

    CloseMessageWindow()

    label("loc_1909")

    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_16F9 end

    def Function_9_1916(): pass

    label("Function_9_1916")

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
            "寇奇……\x01",
            "刚才说的那些是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "嗯，虽然是听两个小鬼说的，\x01",
            "但好像是真的……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "我不相信啊！\x01",
            "我绝对不能相信！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "瓦鲁多大哥那么强的人怎么可能\x01",
            "会败的毫无还手之力……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00105F（这……\x01",
            "  是在说之前那场\x01",
            "  雨中的对决吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00001F（嗯……应该是。）\x02",
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
            "你、你这混蛋……\x01",
            "还敢来这里啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1B80():
        TurnDirection(0x8, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B80)
    TurnDirection(0xC, 0x105, 500)

    #C0081
    ChrTalk(
        0xC,
        "瓦、瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "哈，这次要找我们打架了吗？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "好啊，来吧！\x01",
            "我要给瓦鲁多大哥报仇～！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00005F喂、喂……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0085
    ChrTalk(
        0x9,
        "住手，诺加诺夫！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "即使那两个小鬼说的话是真的，\x01",
            "我们在这里对他出手，\x01",
            "也会有损瓦鲁多大哥的声誉……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "而且，我们这么多人围攻他，\x01",
            "瓦鲁多大哥知道后一定会不高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "啧，可恶……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 500)

    #C0089
    ChrTalk(
        0xC,
        (
            "……我不知道你来这里\x01",
            "有何目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        (
            "如果不想打架，\x01",
            "那就赶快出去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "不过，如果你原本就是想来打架的，\x01",
            "那就另当别论了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        (
            "#10303F不，我并没有那种想法。\x02\x03",

            "#10300F打扰了。\x01",
            "……我们走吧，各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00005F啊……嗯……\x02",
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

    # Function_9_1916 end

    def Function_10_1DE6(): pass

    label("Function_10_1DE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA8")

    #C0094
    ChrTalk(
        0xFE,
        (
            "我还不能原谅\x01",
            "瓦鲁多大哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……虽然不能原谅……\x01",
            "但对我来说，剑蛇帮的据点\x01",
            "确实是个非常开心愉快的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "所以，身为剑蛇帮的干部……\x01",
            "我理应守护这个地方。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EFF")

    label("loc_1EA8")


    #C0097
    ChrTalk(
        0xFE,
        (
            "我还不能原谅\x01",
            "瓦鲁多大哥……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "但身为剑蛇帮的干部，\x01",
            "我理应守护这个\x01",
            "重要的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFF")

    Jump("loc_22AC")

    label("loc_1F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1F")
    Call(0, 11)
    Jump("loc_1F88")

    label("loc_1F1F")


    #C0099
    ChrTalk(
        0xFE,
        (
            "……可恶，\x01",
            "他们竟然去和那些\x01",
            "蓝衣小子合作……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "诺加诺夫、寇奇、迪诺……\x01",
            "那些家伙到底在想什么……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F88")

    Jump("loc_22AC")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F9B")
    Jump("loc_22AC")

    label("loc_1F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1FA9")
    Jump("loc_22AC")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2038")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC4")
    Call(0, 12)
    Jump("loc_2033")

    label("loc_1FC4")


    #C0101
    ChrTalk(
        0xFE,
        (
            "嗯？支援科吗……\x01",
            "看来我们的调查都没什么进展啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "听好，如果以后\x01",
            "发现了瓦鲁多大哥，\x01",
            "要立刻通知我们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2033")

    Jump("loc_22AC")

    label("loc_2038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DA")

    #C0103
    ChrTalk(
        0xFE,
        (
            "……诺加诺夫已经把\x01",
            "我们想说的话基本说完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "已经没有其它事情了。\x01",
            "……你们赶快从这里消失吧。\x02",
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
    Jump("loc_2113")

    label("loc_20DA")


    #C0106
    ChrTalk(
        0xFE,
        (
            "我们已经没什么话要说了。\x01",
            "……你们赶快从这里消失吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2113")

    Jump("loc_22AC")

    label("loc_2118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_215B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2133")
    Call(0, 5)
    Jump("loc_2156")

    label("loc_2133")


    #C0107
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥……\x01",
            "你到底怎么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2156")

    Jump("loc_22AC")

    label("loc_215B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2176")
    Call(0, 6)
    Jump("loc_21A1")

    label("loc_2176")


    #C0108
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥……\x01",
            "你到底去什么地方了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A1")

    Jump("loc_22AC")

    label("loc_21A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_21B7")
    Call(0, 13)
    Jump("loc_22AC")

    label("loc_21B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21C8")
    Call(0, 14)
    Jump("loc_22AC")

    label("loc_21C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21D9")
    Call(0, 16)
    Jump("loc_22AC")

    label("loc_21D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F4")
    Call(0, 9)
    Jump("loc_2252")

    label("loc_21F4")


    #C0109
    ChrTalk(
        0xFE,
        (
            "如果不想打架，\x01",
            "就赶快出去吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "如果你们继续待下去，\x01",
            "连我都猜不到自己会做出什么事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2252")

    Jump("loc_22AC")

    label("loc_2257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_22A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2272")
    Call(0, 17)
    Jump("loc_229E")

    label("loc_2272")


    #C0111
    ChrTalk(
        0xFE,
        (
            "听好，瓦吉……\x01",
            "别以为这样\x01",
            "就算没事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229E")

    Jump("loc_22AC")

    label("loc_22A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_22AC")

    label("loc_22AC")

    TalkEnd(0xFE)
    Return()

    # Function_10_1DE6 end

    def Function_11_22B0(): pass

    label("Function_11_22B0")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0112
    ChrTalk(
        0x9,
        (
            "那几个家伙……\x01",
            "竟然去和那些\x01",
            "蓝衣小子合作……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "……杰德前辈，\x01",
            "我们是不是\x01",
            "也应该去帮忙呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "啊！？你说什么呢！？修伊！\x01",
            "我们剑蛇帮对叛徒\x01",
            "可是绝不轻饶的……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "……不是和你说过剑蛇帮\x01",
            "已经解散了吗！蠢货！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0116
    ChrTalk(
        0xB,
        "对、对不起。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "……总之，我正在考虑。\x01",
            "你们不要擅自行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_22B0 end

    def Function_12_23FE(): pass

    label("Function_12_23FE")

    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0118
    ChrTalk(
        0x9,
        (
            "啧，虽然不知道是怎么回事，\x01",
            "但好像发生了很严重的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "是的，市里的人全都在\x01",
            "讨论玛因兹被占领的话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "瓦鲁多大哥……\x01",
            "该不会被卷入到\x01",
            "事件中了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "呼，我想应该不会吧……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "总之，你们今天\x01",
            "也要拼命搜集情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        "#2P是！\x02",
    )


    #C0124
    ChrTalk(
        0xB,
        "#3P是！\x02",
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

    # Function_12_23FE end

    def Function_13_252C(): pass

    label("Function_13_252C")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2734")

    #C0125
    ChrTalk(
        0xC,
        (
            "瓦鲁多大哥……\x01",
            "现在到底在什么地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "呼……\x01",
            "瓦鲁多大哥这段时间\x01",
            "好像也没有回过自己的家……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "至今都已经三天\x01",
            "没有见过他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "最后一次见到瓦鲁多大哥，\x01",
            "是修伊前辈他们在港湾区……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "嗯，虽然出声打了招呼，\x01",
            "但却被完全无视了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "……总之，瓦鲁多大哥\x01",
            "似乎遇到了什么事情。\x01",
            "我们分头寻找线索吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "你们两个负责这片旧城区。\x01",
            "要找遍每一个角落，多向路人打听。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        "明白！\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#00005F（瓦鲁多……\x01",
            "  下落不明了吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x105,
        "#10303F（怎么回事……很让人在意呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2793")

    label("loc_2734")


    #C0136
    ChrTalk(
        0x9,
        (
            "鬼火由我和诺加诺夫\x01",
            "轮班看守。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        "如果有什么情况，要立刻回来报告。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xD,
        "明白！\x02",
    )

    CloseMessageWindow()

    label("loc_2793")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_252C end

    def Function_14_27A0(): pass

    label("Function_14_27A0")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2862")

    #C0140
    ChrTalk(
        0x9,
        (
            "怎么，自昨天那次之后，\x01",
            "就没人再见过瓦鲁多大哥吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        "嗯，我再也没看见过……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xD,
        "我、我也是。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "是吗……从昨天见到他的样子来看，\x01",
            "现在应该还在宿醉中吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B5")

    label("loc_2862")


    #C0144
    ChrTalk(
        0x9,
        (
            "对了……稍后去他家里\x01",
            "看看好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "你们也和我一起去。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xD,
        "当然！\x02",
    )

    CloseMessageWindow()

    label("loc_28B5")

    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_27A0 end

    def Function_15_28C2(): pass

    label("Function_15_28C2")

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
        "是吗……瓦鲁多大哥他……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "他完全不在意别人的目光，\x01",
            "遥遥晃晃地进了店……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        (
            "之后买了相当多的酒，\x01",
            "现在应该正在家里\x01",
            "继续狂饮吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xC,
        (
            "老实说……\x01",
            "我真不愿意看到\x01",
            "那个样子的瓦鲁多大哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "瓦鲁多大哥竟然会……\x01",
            "喝得烂醉如泥……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "……嗯，我的心情也一样。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "而且……\x01",
            "万一在路上醉倒，\x01",
            "实在是非常危险呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "大家继续留意\x01",
            "瓦鲁多大哥的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xC,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xD,
        "明白！\x02",
    )

    CloseMessageWindow()
    OP_68(1930, 1000, -40, 1500)
    OP_6F(0x1)

    #C0158
    ChrTalk(
        0x101,
        "#00005F瓦鲁多竟然会……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#12P#00301F这就是所谓的借酒消愁吧……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#00103F喝得那么多，\x01",
            "实在是担心他的身体……\x02",
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

    # Function_15_28C2 end

    def Function_16_2BDE(): pass

    label("Function_16_2BDE")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0162
    ChrTalk(
        0x9,
        (
            "听好，如果发现了什么情况，\x01",
            "就立刻来通知我或诺加诺夫。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        "是！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xD,
        "明白！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_2BDE end

    def Function_17_2C48(): pass

    label("Function_17_2C48")

    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xC, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0165
    ChrTalk(
        0xD,
        "你、你们是……！\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        "特别任务支援科……还有瓦吉！\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "……看来你还没有见到\x01",
            "瓦鲁多大哥啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0168
    ChrTalk(
        0x105,
        "#10305F瓦鲁多怎么了？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xD,
        "其、其实……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "住口，迪诺。\x01",
            "我们和这种向警察摇尾示好\x01",
            "的懦夫没什么话好说。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        "如果听明白了，你们就赶快消失吧。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        "#10303F……哎呀呀。\x02",
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

    # Function_17_2C48 end

    def Function_18_2DBA(): pass

    label("Function_18_2DBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DCB")
    Jump("loc_311B")

    label("loc_2DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE6")
    Call(0, 11)
    Jump("loc_2E1B")

    label("loc_2DE6")


    #C0173
    ChrTalk(
        0xFE,
        (
            "（话是这么说，\x01",
            "  但杰德前辈似乎也很犹豫呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1B")

    Jump("loc_311B")

    label("loc_2E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E2E")
    Jump("loc_311B")

    label("loc_2E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E3C")
    Jump("loc_311B")

    label("loc_2E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E57")
    Call(0, 12)
    Jump("loc_2EA5")

    label("loc_2E57")


    #C0174
    ChrTalk(
        0xFE,
        (
            "不明身份的武装集团吗……\x01",
            "如果遭到那种家伙的袭击，\x01",
            "我们恐怕完全无力抵抗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA5")

    Jump("loc_311B")

    label("loc_2EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EDB")

    #C0175
    ChrTalk(
        0xFE,
        (
            "诺加诺夫前辈……\x01",
            "真是好帅啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311B")

    label("loc_2EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF6")
    Call(0, 5)
    Jump("loc_2F25")

    label("loc_2EF6")


    #C0176
    ChrTalk(
        0xFE,
        (
            "十万米拉……\x01",
            "到底是怎么搞到那么多钱的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F25")

    Jump("loc_311B")

    label("loc_2F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F45")
    Call(0, 6)
    Jump("loc_2FA8")

    label("loc_2F45")


    #C0177
    ChrTalk(
        0xFE,
        (
            "我已经到处打听过了……\x01",
            "但所有人都说最近\x01",
            "一直没看见过瓦鲁多大哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "但愿他没有\x01",
            "离开城市……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA8")

    Jump("loc_311B")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FBE")
    Call(0, 7)
    Jump("loc_311B")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FCF")
    Call(0, 8)
    Jump("loc_311B")

    label("loc_2FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_30BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3082")

    #C0179
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "被刚才那个奇怪的家伙一闹，\x01",
            "我已经没心情打架了……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……下次可不会有这种好运了。\x01",
            "给我记清楚，瓦吉。\x02",
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
    Jump("loc_30B7")

    label("loc_3082")


    #C0182
    ChrTalk(
        0xFE,
        (
            "……下次可不会有这种好运了。\x01",
            "给我记清楚，瓦吉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B7")

    Jump("loc_311B")

    label("loc_30BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D7")
    Call(0, 19)
    Jump("loc_30FC")

    label("loc_30D7")


    #C0183
    ChrTalk(
        0xFE,
        (
            "你、你这家伙……\x01",
            "多想点正事啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30FC")

    Jump("loc_311B")

    label("loc_3101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3112")
    Call(0, 20)
    Jump("loc_311B")

    label("loc_3112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_311B")

    label("loc_311B")

    TalkEnd(0xFE)
    Return()

    # Function_18_2DBA end

    def Function_19_311F(): pass

    label("Function_19_311F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0184
    ChrTalk(
        0xA,
        "喂，你有没有什么好点子？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "有！我今天早上过来之前，\x01",
            "看到一位修女抱着\x01",
            "堆积如山的面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xB,
        "她真是太可爱了！\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "……嗯？\x01",
            "这和瓦鲁多大哥的事情\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "哦，我只是想说，\x01",
            "下次不妨和瓦鲁多大哥一起到教会看看，\x01",
            "和那位修女搭个讪……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0189
    ChrTalk(
        0xA,
        "你这家伙脑袋有问题吗！？\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "我们为什么要去\x01",
            "教会那种地方啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_19_311F end

    def Function_20_328C(): pass

    label("Function_20_328C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3405")

    #C0191
    ChrTalk(
        0xB,
        (
            "呼，瓦鲁多大哥今天早上\x01",
            "真是好可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "话说回来……\x01",
            "瓦鲁多大哥为何如此在意\x01",
            "瓦吉那混账呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "不管怎么说，\x01",
            "最棘手的家伙不在了，\x01",
            "不是应该高兴才对吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "喂！斯拉修！\x01",
            "你小子在胡说些什么！？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "我们再过一百万年也没资格\x01",
            "对瓦鲁多大哥说三道四。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        (
            "与其说那种没用的话，\x01",
            "不如想想怎么才能让他心情好起来！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "啊……嗯嗯，\x01",
            "我也明白这些的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3476")

    label("loc_3405")


    #C0198
    ChrTalk(
        0xA,
        (
            "真是的，你把刚才那些话\x01",
            "当面说给瓦鲁多大哥试试。\x01",
            "他非把你打个半死不可！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "是、是我不好，\x01",
            "我不会再说啦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3476")

    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_20_328C end

    def Function_21_347F(): pass

    label("Function_21_347F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3490")
    Jump("loc_3771")

    label("loc_3490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_34C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AB")
    Call(0, 11)
    Jump("loc_34C3")

    label("loc_34AB")


    #C0200
    ChrTalk(
        0xFE,
        "呼，被教训了呢……\x02",
    )

    CloseMessageWindow()

    label("loc_34C3")

    Jump("loc_3771")

    label("loc_34C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_34D6")
    Jump("loc_3771")

    label("loc_34D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34E4")
    Jump("loc_3771")

    label("loc_34E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_354C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FF")
    Call(0, 12)
    Jump("loc_3547")

    label("loc_34FF")


    #C0201
    ChrTalk(
        0xFE,
        (
            "那个……\x01",
            "锤子和钉子放在哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "谨慎起见，\x01",
            "必须要强化棍棒啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3547")

    Jump("loc_3771")

    label("loc_354C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3577")

    #C0203
    ChrTalk(
        0xFE,
        (
            "哇～前辈们\x01",
            "果然了不起！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3771")

    label("loc_3577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_35C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3592")
    Call(0, 5)
    Jump("loc_35C3")

    label("loc_3592")


    #C0204
    ChrTalk(
        0xFE,
        (
            "真是的，我完全不明白，\x01",
            "谁来给我说明一下啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C3")

    Jump("loc_3771")

    label("loc_35C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E3")
    Call(0, 6)
    Jump("loc_3620")

    label("loc_35E3")


    #C0205
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥好像还是\x01",
            "没有回家……\x01",
            "他究竟在什么地方过夜呢?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3620")

    Jump("loc_3771")

    label("loc_3625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3636")
    Call(0, 7)
    Jump("loc_3771")

    label("loc_3636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3647")
    Call(0, 8)
    Jump("loc_3771")

    label("loc_3647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_370A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36BC")

    #C0206
    ChrTalk(
        0xFE,
        (
            "哈，世上竟然还有\x01",
            "那种奇怪的混账家伙～\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "……哎，说起来，\x01",
            "我和修伊都没有打成架呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3705")

    label("loc_36BC")


    #C0208
    ChrTalk(
        0xFE,
        "……算了，不管那种小事了。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "现在还是多想想\x01",
            "瓦鲁多大哥的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3705")

    Jump("loc_3771")

    label("loc_370A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3725")
    Call(0, 19)
    Jump("loc_3752")

    label("loc_3725")


    #C0210
    ChrTalk(
        0xFE,
        (
            "你、你不是也没有\x01",
            "想出任何像样的主意吗！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3752")

    Jump("loc_3771")

    label("loc_3757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3768")
    Call(0, 20)
    Jump("loc_3771")

    label("loc_3768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3771")

    label("loc_3771")

    TalkEnd(0xFE)
    Return()

    # Function_21_347F end

    def Function_22_3775(): pass

    label("Function_22_3775")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37FB")

    #C0211
    ChrTalk(
        0xFE,
        (
            "在瓦鲁多大哥回来之前，\x01",
            "由组织的干部杰德前辈和诺加诺夫前辈\x01",
            "来领导剑蛇帮。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "大家一定要齐心协力，\x01",
            "守卫剑蛇帮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F0")

    label("loc_37FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3809")
    Jump("loc_39F0")

    label("loc_3809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3817")
    Jump("loc_39F0")

    label("loc_3817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3825")
    Jump("loc_39F0")

    label("loc_3825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_386A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3840")
    Call(0, 23)
    Jump("loc_3865")

    label("loc_3840")


    #C0213
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥现在\x01",
            "正在做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3865")

    Jump("loc_39F0")

    label("loc_386A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38E3")

    #C0214
    ChrTalk(
        0xFE,
        (
            "仔细想想，两位干部\x01",
            "是在剑蛇帮成立之初\x01",
            "就加入组织的老成员……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "他们远比我们\x01",
            "更加担心瓦鲁多大哥……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F0")

    label("loc_38E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FE")
    Call(0, 5)
    Jump("loc_3933")

    label("loc_38FE")


    #C0216
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥……\x01",
            "把我们抛下不管，到底和什么人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3933")

    Jump("loc_39F0")

    label("loc_3938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3946")
    Jump("loc_39F0")

    label("loc_3946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3957")
    Call(0, 13)
    Jump("loc_39F0")

    label("loc_3957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3968")
    Call(0, 14)
    Jump("loc_39F0")

    label("loc_3968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3979")
    Call(0, 16)
    Jump("loc_39F0")

    label("loc_3979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_39B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3994")
    Call(0, 9)
    Jump("loc_39AE")

    label("loc_3994")


    #C0217
    ChrTalk(
        0xFE,
        "你、你们赶快滚出去！\x02",
    )

    CloseMessageWindow()

    label("loc_39AE")

    Jump("loc_39F0")

    label("loc_39B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_39E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CE")
    Call(0, 17)
    Jump("loc_39E2")

    label("loc_39CE")


    #C0218
    ChrTalk(
        0xFE,
        "瓦鲁多大哥……\x02",
    )

    CloseMessageWindow()

    label("loc_39E2")

    Jump("loc_39F0")

    label("loc_39E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39F0")

    label("loc_39F0")

    TalkEnd(0xFE)
    Return()

    # Function_22_3775 end

    def Function_23_39F4(): pass

    label("Function_23_39F4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0219
    ChrTalk(
        0xD,
        (
            "瓦鲁多大哥……\x01",
            "今天果然也不见踪影啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "是啊……\x01",
            "好像发生了什么严重的骚乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "……总之，\x01",
            "希望他能平安无事。\x02",
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

    # Function_23_39F4 end

    def Function_24_3A8C(): pass

    label("Function_24_3A8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A9D")
    Jump("loc_3F4E")

    label("loc_3A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3AAB")
    Jump("loc_3F4E")

    label("loc_3AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3AB9")
    Jump("loc_3F4E")

    label("loc_3AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D50")
    OP_4B(0xFE, 0xFF)

    #C0222
    ChrTalk(
        0xFE,
        "瓦鲁多大哥……各位前辈……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        "#00108F……迪诺…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0224
    ChrTalk(
        0xFE,
        "……怎么，是特别任务支援科啊。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00003F其他成员……\x01",
            "还在医院里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "嗯，除我之外的所有成员都……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "尤其是寇奇前辈，伤得非常重……\x01",
            "……如今仍然躺在单独病房里……\x01",
            "呜、呜呜……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#00008F抱歉……我好像没有考虑到你的感受呢。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "呜……没、没……\x01",
            "没必要考虑我这种人的感受啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "前辈们都承受了那么大的痛苦，\x01",
            "却只有我一个人平安无事……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "呜呜……可恶！\x01",
            "为什么……为什么会发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#00208F（罗伊德前辈……\x01",
            "  现在还是让他一个人静一静吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        "#00003F（嗯……是啊。）\x02",
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
    Jump("loc_3D96")

    label("loc_3D50")


    #C0235
    ChrTalk(
        0xFE,
        "瓦鲁多大哥……各位前辈……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "为什么……为什么会发生这种事……\x02",
    )

    CloseMessageWindow()

    label("loc_3D96")

    Jump("loc_3F4E")

    label("loc_3D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB6")
    Call(0, 23)
    Jump("loc_3E0E")

    label("loc_3DB6")


    #C0237
    ChrTalk(
        0xFE,
        "『真知』吗……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "鲁巴彻都已经灭亡了，\x01",
            "瓦鲁多大哥究竟是\x01",
            "从哪里弄到那种东西的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0E")

    Jump("loc_3F4E")

    label("loc_3E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3E7E")

    #C0239
    ChrTalk(
        0xFE,
        "嘿嘿嘿，前辈们果然伟大啊。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "虽然现在的情况不容乐观……\x01",
            "但不知为何，我却有点开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4E")

    label("loc_3E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3ED1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E99")
    Call(0, 5)
    Jump("loc_3ECC")

    label("loc_3E99")


    #C0241
    ChrTalk(
        0xFE,
        (
            "呜呜……瓦鲁多大哥\x01",
            "难道去做很危险的工作了吗…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECC")

    Jump("loc_3F4E")

    label("loc_3ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3EE2")
    Call(0, 13)
    Jump("loc_3F4E")

    label("loc_3EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EF3")
    Call(0, 14)
    Jump("loc_3F4E")

    label("loc_3EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F04")
    Call(0, 16)
    Jump("loc_3F4E")

    label("loc_3F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F1F")
    Call(0, 17)
    Jump("loc_3F4E")

    label("loc_3F1F")


    #C0242
    ChrTalk(
        0xFE,
        (
            "杰、杰德前辈说的没错，\x01",
            "我和你们没话可说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F4E")

    TalkEnd(0xFE)
    Return()

    # Function_24_3A8C end

    def Function_25_3F52(): pass

    label("Function_25_3F52")

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

    def lambda_4018():
        OP_96(0xFE, 0x1C20, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4018)
    Sleep(400)

    def lambda_4035():
        OP_96(0xFE, 0x1CE8, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4035)
    Sleep(400)

    def lambda_4052():
        OP_96(0xFE, 0x170C, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4052)
    Sleep(400)

    def lambda_406F():
        OP_96(0xFE, 0x1900, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_406F)
    Sleep(400)

    def lambda_408C():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_408C)
    Sleep(400)

    def lambda_40A9():
        OP_96(0xFE, 0x13EC, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40A9)
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

    def lambda_412F():

        label("loc_412F")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_412F")

    QueueWorkItem2(0x9, 2, lambda_412F)

    def lambda_4141():

        label("loc_4141")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4141")

    QueueWorkItem2(0xC, 2, lambda_4141)

    def lambda_4153():

        label("loc_4153")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_4153")

    QueueWorkItem2(0xD, 2, lambda_4153)

    #C0243
    ChrTalk(
        0x9,
        "#11P警察……又来了啊。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xC,
        "#11P莫非有什么新情报……\x02",
    )

    CloseMessageWindow()

    def lambda_419F():

        label("loc_419F")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_419F")

    QueueWorkItem2(0x8, 2, lambda_419F)

    def lambda_41B1():

        label("loc_41B1")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_41B1")

    QueueWorkItem2(0xB, 2, lambda_41B1)

    def lambda_41C3():

        label("loc_41C3")

        TurnDirection(0xFE, 0x0, 500)
        Yield()
        Jump("loc_41C3")

    QueueWorkItem2(0xA, 2, lambda_41C3)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_41F0():

        label("loc_41F0")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_41F0")

    QueueWorkItem2(0xD, 2, lambda_41F0)

    #C0245
    ChrTalk(
        0xD,
        "#11P……瓦、瓦吉！\x02",
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

    def lambda_42C5():

        label("loc_42C5")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_42C5")

    QueueWorkItem2(0x8, 2, lambda_42C5)

    def lambda_42D7():

        label("loc_42D7")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_42D7")

    QueueWorkItem2(0xB, 2, lambda_42D7)

    def lambda_42E9():

        label("loc_42E9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_42E9")

    QueueWorkItem2(0xA, 2, lambda_42E9)

    def lambda_42FB():

        label("loc_42FB")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_42FB")

    QueueWorkItem2(0x9, 2, lambda_42FB)

    def lambda_430D():

        label("loc_430D")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_430D")

    QueueWorkItem2(0xC, 2, lambda_430D)

    #C0247
    ChrTalk(
        0xA,
        "#5P你、你这混蛋……！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "#5P竟然还敢厚颜无耻地来这里……\x01",
            "都是因为你！瓦鲁多大哥才会……！\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#12P#00001F（呜……气氛相当险恶啊。）\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        "#6P#00208F（似乎不应该来这里啊……）\x02",
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

    def lambda_43F5():
        OP_96(0xFE, 0x215C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_43F5)
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
        "#11P喂，诺加诺夫……？\x02",
    )

    CloseMessageWindow()

    def lambda_44F3():

        label("loc_44F3")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_44F3")

    QueueWorkItem2(0x101, 2, lambda_44F3)

    def lambda_4505():

        label("loc_4505")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4505")

    QueueWorkItem2(0x102, 2, lambda_4505)

    def lambda_4517():

        label("loc_4517")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4517")

    QueueWorkItem2(0x103, 2, lambda_4517)

    def lambda_4529():

        label("loc_4529")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4529")

    QueueWorkItem2(0x109, 2, lambda_4529)

    def lambda_453B():

        label("loc_453B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_453B")

    QueueWorkItem2(0x104, 2, lambda_453B)

    def lambda_454D():

        label("loc_454D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_454D")

    QueueWorkItem2(0x105, 2, lambda_454D)

    def lambda_455F():
        OP_95(0xFE, 8039, 0, 570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_455F)
    Sleep(50)
    WaitChrThread(0x8, 1)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x4)
    Sound(802, 0, 100, 0)

    def lambda_4594():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4594)

    def lambda_45AD():
        OP_96(0xFE, 0x1CE8, 0xC8, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_45AD)
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
        "#6P#10310F…………唔………………\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#12P#00011F喂、喂……！\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#6P#10111F瓦吉……！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0256
    ChrTalk(
        0x8,
        (
            "#4S#11P哟，瓦吉！\x01",
            "你也知道了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0257
    ChrTalk(
        0x8,
        (
            "#4S#11P瓦鲁多大哥竟然\x01",
            "服下了那种药！！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0258
    ChrTalk(
        0x8,
        (
            "#4S#11P这全都……\x01",
            "这全都是因为你啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        (
            "#6P#00101F（罗、罗伊德……\x01",
            "  你和他们说了多少？）\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#12P#00003F（哦，倒是没有连\x01",
            "  魔人化的事情都透露……）\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        (
            "#6P#N#10108F（……不过，告诉了他们\x01",
            "  瓦鲁多有可能已经服用『真知』。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0262
    ChrTalk(
        0x8,
        (
            "#11P……两年前，你要是没来的话，\x01",
            "我们会一直……\x01",
            "一直过得开开心心……！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "#11P你当时突然出现，这次又\x01",
            "突然当起警察……都是因为你\x01",
            "总这么由着性子胡来，他才会……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0264
    ChrTalk(
        0x8,
        "#11P#4S……你明白吗！？#3S\x02",
    )

    CloseMessageWindow()

    def lambda_49A6():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_49A6)
    WaitChrThread(0x105, 2)

    #C0265
    ChrTalk(
        0x105,
        (
            "#6P#10303F……我并不是由着性子胡来。\x01",
            "我有必须要做的事情，所以才会\x01",
            "选择现在这条路，仅此而已。\x02\x03",

            "#10308F但我的选择竟然会使\x01",
            "瓦鲁多变成这样……\x01",
            "确实是在预料之外。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#6P#00303F……瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        "#11P……所以你不准备抵抗吗？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0268
    ChrTalk(
        0x8,
        "#11P#4S……有种！那我就宰了你！#3S\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x103,
        "#6P#00210F！！\x02",
    )

    CloseMessageWindow()

    def lambda_4AF1():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4AF1)
    WaitChrThread(0x105, 2)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Sound(811, 0, 100, 0)

    def lambda_4B2F():
        OP_9D(0xFE, 0x1A2C, 0x0, 0x2BC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4B2F)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x8, 0x40)
    WaitChrThread(0x105, 1)
    Sleep(500)

    #C0270
    ChrTalk(
        0x102,
        "#N#6P#00105F啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_4B76():

        label("loc_4B76")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4B76")

    QueueWorkItem2(0x101, 2, lambda_4B76)

    def lambda_4B88():

        label("loc_4B88")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4B88")

    QueueWorkItem2(0x102, 2, lambda_4B88)

    def lambda_4B9A():

        label("loc_4B9A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4B9A")

    QueueWorkItem2(0x103, 2, lambda_4B9A)

    def lambda_4BAC():

        label("loc_4BAC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4BAC")

    QueueWorkItem2(0x109, 2, lambda_4BAC)

    def lambda_4BBE():

        label("loc_4BBE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4BBE")

    QueueWorkItem2(0x104, 2, lambda_4BBE)

    #C0271
    ChrTalk(
        0xC,
        "#11P哎……？\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x105,
        "#6P#10305F…………你想怎样？\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x8,
        (
            "#11P……说到底，\x01",
            "我们全都没有唤醒他的能力。\x01",
            "能够唤醒他的……只有你一个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#11P……记住，这一拳是你欠我的。\x01",
            "作为回报……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0275
    ChrTalk(
        0x8,
        (
            "#4S#11P你必须要担负起责任，\x01",
            "让瓦鲁多大哥清醒过来！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        "#11P诺加诺夫……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xD,
        "#11P前、前辈……\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)

    #C0278
    ChrTalk(
        0x105,
        (
            "#6P#10308F……呵呵，原来如此。\x02\x03",

            "#10303F………………………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D59():

        label("loc_4D59")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4D59")

    QueueWorkItem2(0x101, 2, lambda_4D59)

    def lambda_4D6B():

        label("loc_4D6B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4D6B")

    QueueWorkItem2(0x102, 2, lambda_4D6B)

    def lambda_4D7D():

        label("loc_4D7D")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4D7D")

    QueueWorkItem2(0x103, 2, lambda_4D7D)

    def lambda_4D8F():

        label("loc_4D8F")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4D8F")

    QueueWorkItem2(0x109, 2, lambda_4D8F)

    def lambda_4DA1():

        label("loc_4DA1")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4DA1")

    QueueWorkItem2(0x104, 2, lambda_4DA1)

    #C0279
    ChrTalk(
        0x101,
        "#12P#00005F瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x105,
        (
            "#6P#10303F……虽然无法向你保证……\x01",
            "但我一定会竭尽全力的。\x02\x03",

            "#10301F身为圣书会的首领……\x01",
            "我也一定会和他完成\x01",
            "之前未能完成的了断。\x02",
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

    # Function_25_3F52 end

    def Function_26_4F5B(): pass

    label("Function_26_4F5B")


    def lambda_4F60():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F60)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_4F5B end

    SaveToFile()

Try(main)
