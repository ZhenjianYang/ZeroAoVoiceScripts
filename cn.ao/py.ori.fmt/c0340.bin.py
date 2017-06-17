from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0340.bin",                # FileName
        "c0340",                    # MapName
        "c0340",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0340",                  # 0
        "伊兹丽夫人",             # 1
        "菲利克",                 # 2
        "辛迪",                   # 3
        "亨利",                   # 4
        "约库斯",                 # 5
        "玛丽埃塔",               # 6
    ))

    AddCharChip((
        "chr/ch21700.itc",                   # 00
        "chr/ch21702.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch22200.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch21900.itc",                   # 06
        "chr/ch22102.itc",                   # 07
        "chr/ch22202.itc",                   # 08
        "chr/ch27602.itc",                   # 09
    ))

    DeclNpc(40669,   0,       9600,    360,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(32659,   0,       5679,    180,  261,  0x0, 0,   2,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(4980,    0,       8989,    89,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(5329,    0,       3990,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(689,     0,       990,     225,  389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-3710,   0,       5789,    225,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)

    ChipFrameInfo(428, 0)                                        # 0

    ScpFunction((
        "Function_0_1AC",          # 00, 0
        "Function_1_264",          # 01, 1
        "Function_2_28F",          # 02, 2
        "Function_3_2B7",          # 03, 3
        "Function_4_2E2",          # 04, 4
        "Function_5_32F",          # 05, 5
        "Function_6_35A",          # 06, 6
        "Function_7_84E",          # 07, 7
        "Function_8_8CF",          # 08, 8
        "Function_9_15C1",         # 09, 9
        "Function_10_167C",        # 0A, 10
        "Function_11_1743",        # 0B, 11
        "Function_12_17F2",        # 0C, 12
        "Function_13_18DD",        # 0D, 13
        "Function_14_21E7",        # 0E, 14
        "Function_15_2BA5",        # 0F, 15
        "Function_16_2D61",        # 10, 16
        "Function_17_2EED",        # 11, 17
    ))


    def Function_0_1AC(): pass

    label("Function_0_1AC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1EC"),
        (1, "loc_1F8"),
        (2, "loc_204"),
        (3, "loc_210"),
        (4, "loc_21C"),
        (5, "loc_228"),
        (6, "loc_234"),
        (SWITCH_DEFAULT, "loc_240"),
    )


    label("loc_1EC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_1F8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_204")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_210")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_21C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_228")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_234")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_240")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_263")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_24C")

    label("loc_263")

    Return()

    # Function_0_1AC end

    def Function_1_264(): pass

    label("Function_1_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28E")
    OP_94(0xFE, 0xFFFFF510, 0xFFFFFF56, 0x11D0, 0x94C, 0x3E8)
    Sleep(300)
    Jump("Function_1_264")

    label("loc_28E")

    Return()

    # Function_1_264 end

    def Function_2_28F(): pass

    label("Function_2_28F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B6")
    OP_94(0xFE, 0x14D2, 0xFFFFFCAE, 0xFFFFF6B4, 0x94C, 0x3E8)
    Jump("Function_2_28F")

    label("loc_2B6")

    Return()

    # Function_2_28F end

    def Function_3_2B7(): pass

    label("Function_3_2B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_94(0xFE, 0x7738, 0x1126, 0x852A, 0x1D38, 0x3E8)
    Sleep(300)
    Jump("Function_3_2B7")

    label("loc_2E1")

    Return()

    # Function_3_2B7 end

    def Function_4_2E2(): pass

    label("Function_4_2E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32E")
    OP_95(0xFE, 1790, 0, 500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 1790, 0, 1500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_4_2E2")

    label("loc_32E")

    Return()

    # Function_4_2E2 end

    def Function_5_32F(): pass

    label("Function_5_32F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_359")
    OP_94(0xFE, 0xF32, 0x2C6, 0x139C, 0x2634, 0x3E8)
    Sleep(300)
    Jump("Function_5_32F")

    label("loc_359")

    Return()

    # Function_5_32F end

    def Function_6_35A(): pass

    label("Function_6_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3BB")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34130, 0, 4390, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 32200, 0, 4080, 135)
    Jump("loc_84D")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F0")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2500, 200, 3760, 315)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jump("loc_84D")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45D")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34130, 0, 4390, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 32200, 0, 4080, 135)
    SetChrPos(0xA, 32200, 0, 1340, 45)
    Jump("loc_84D")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4BD")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 40600, 0, 8220, 270)
    SetChrPos(0x8, 38120, 0, 8230, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_4A1")

    SetChrPos(0x9, 36730, 0, 7190, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_84D")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4ED")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_84D")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_534")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40670, 0, 9600, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_84D")

    label("loc_534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_58C")
    SetChrPos(0x8, 2560, 350, 6660, 225)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 3620, 0, 9800, 0)
    SetChrPos(0x9, 2370, 0, 9290, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_84D")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D0")
    SetChrPos(0x8, 2370, 0, 9290, 45)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, 3620, 0, 9800, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB")
    SetChrFlags(0xA, 0x10)

    label("loc_5CB")

    Jump("loc_84D")

    label("loc_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_611")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 3620, 0, 9800, 0)
    Jump("loc_84D")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_646")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x80)
    Jump("loc_84D")

    label("loc_646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_71A")
    SetChrPos(0x8, 2560, 350, 6660, 225)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -630, 200, 6750, 135)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AC")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_6AC")

    SetChrPos(0xA, 2380, 200, 3690, 315)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrSubChip(0xA, 0x1)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -380, 200, 3780, 45)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0x9, 700, 0, 0, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_84D")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_74A")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_84D")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7AC")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 4590, 0, 7300, 0)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, 4590, 0, 9050, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_84D")

    label("loc_7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_822")
    SetChrPos(0x8, 2560, 350, 6660, 225)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 1000, 0, 7830, 135)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_802")

    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 34000, 0, 6920, 90)
    Jump("loc_84D")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_84D")
    SetChrPos(0x8, 36820, 200, 2990, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_84D")

    Return()

    # Function_6_35A end

    def Function_7_84E(): pass

    label("Function_7_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_893")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_8CE")

    Return()

    # Function_7_84E end

    def Function_8_8CF(): pass

    label("Function_8_8CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94B")

    #C0001
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "一家人就更要聚在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "不管怎么说，我儿子和儿媳\x01",
            "平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9B1")

    label("loc_94B")


    #C0003
    ChrTalk(
        0xFE,
        (
            "我儿子和儿媳是家里的顶梁柱，\x01",
            "他们平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "一家人就更要聚在一起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B1")

    Jump("loc_15BD")

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A86")

    #C0005
    ChrTalk(
        0xFE,
        (
            "无论在任何时候，\x01",
            "从容冷静都是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "只要能保持冷静，\x01",
            "就能使易于传染的恐惧和不安\x01",
            "全部消失。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "孩子们肯定也都在为我儿子和儿媳\x01",
            "而感到担心吧……\x01",
            "我必须要保持镇静才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B0E")

    label("loc_A86")


    #C0008
    ChrTalk(
        0xFE,
        (
            "只要能保持冷静，\x01",
            "就能使易于传染的恐惧和不安\x01",
            "全部消失。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "孩子们肯定也都在为我儿子和儿媳\x01",
            "而感到担心吧……\x01",
            "我必须要保持镇静才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0E")

    Jump("loc_15BD")

    label("loc_B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC")

    #C0010
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔今后的局势\x01",
            "一定会非常混乱吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "但是，只要我们一家人齐心协力，\x01",
            "就一定能渡过难关……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "无论发生什么事，\x01",
            "大家都要齐心协力，\x01",
            "一起渡过困境。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C31")

    label("loc_BCC")


    #C0013
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔今后的局势\x01",
            "一定会非常混乱吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "无论发生什么事，\x01",
            "大家都要齐心协力，\x01",
            "一起渡过困境。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C31")

    Jump("loc_15BD")

    label("loc_C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C51")
    Call(0, 9)
    Jump("loc_CC0")

    label("loc_C51")


    #C0015
    ChrTalk(
        0xFE,
        (
            "我儿子和玛丽埃塔都在\x01",
            "大楼已被炸毁的ＩＢＣ工作，\x01",
            "现在十分忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "唉，希望他们注意身体，\x01",
            "别把自己累坏。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC0")

    Jump("loc_15BD")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6B")

    #C0017
    ChrTalk(
        0xFE,
        (
            "不知那武装集团\x01",
            "到底是从哪里\x01",
            "冒出来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "他们竟把无辜的市民牵连进来，\x01",
            "真是不可饶恕。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "希望警备队\x01",
            "尽快解救出\x01",
            "玛因兹的居民们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DCC")

    label("loc_D6B")


    #C0020
    ChrTalk(
        0xFE,
        (
            "武装集团竟把无辜的市民牵连进来，\x01",
            "真是不可饶恕。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "希望警备队\x01",
            "尽快解救出\x01",
            "玛因兹的居民们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCC")

    Jump("loc_15BD")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E63")

    #C0022
    ChrTalk(
        0xFE,
        (
            "亨利今天\x01",
            "也出去玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "我并不要求他在下雨天\x01",
            "待在家里不出门……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "但希望他能注意些，\x01",
            "不要淋湿之后患上感冒。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EBF")

    label("loc_E63")


    #C0025
    ChrTalk(
        0xFE,
        (
            "我并不要求他在下雨天\x01",
            "待在家里不出门……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "但希望他能注意些，\x01",
            "不要淋湿之后患上感冒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EBF")

    Jump("loc_15BD")

    label("loc_EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F23")

    #C0027
    ChrTalk(
        0xFE,
        (
            "我刚才教给辛迪\x01",
            "一些做甜点的\x01",
            "技巧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "工作结束后喝杯茶的感觉真好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BD")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3E")
    Call(0, 10)
    Jump("loc_F75")

    label("loc_F3E")


    #C0029
    ChrTalk(
        0xFE,
        (
            "好，接下来，只要等着烤好就行了。\x01",
            "你自己试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F75")

    Jump("loc_15BD")

    label("loc_F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1038")

    #C0030
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立吗……\x01",
            "如果能顺利实现，\x01",
            "自然再好不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "但帝国和共和国\x01",
            "肯定会施加很大压力，\x01",
            "显然没那么容易实现。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "难道迪塔市长手中\x01",
            "还握有什么妙计……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_109D")

    label("loc_1038")


    #C0033
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立吗……\x01",
            "如果能顺利实现，\x01",
            "自然再好不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "迪塔市长是不是\x01",
            "暗藏着什么妙计呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109D")

    Jump("loc_15BD")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_116E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1126")

    #C0035
    ChrTalk(
        0xFE,
        (
            "辛迪今天去邻居家\x01",
            "玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "她在烹饪教室\x01",
            "常受海瓦斯\x01",
            "夫人的关照……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "下次得向人家好好道谢才行。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1169")

    label("loc_1126")


    #C0038
    ChrTalk(
        0xFE,
        (
            "辛迪一直受\x01",
            "海瓦斯夫人的关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "下次得向人家好好道谢才行。\x02",
    )

    CloseMessageWindow()

    label("loc_1169")

    Jump("loc_15BD")

    label("loc_116E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_11DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1189")
    Call(0, 11)
    Jump("loc_11D9")

    label("loc_1189")


    #C0040
    ChrTalk(
        0xFE,
        (
            "玛丽埃塔似乎\x01",
            "也很忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "看来还要等一段时间，\x01",
            "才能全家一起吃团圆饭啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D9")

    Jump("loc_15BD")

    label("loc_11DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_132B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C3")

    #C0042
    ChrTalk(
        0xFE,
        (
            "在住宅街也能\x01",
            "观看到兰花塔的揭幕式……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "竟能建起那种高耸入云的建筑物，\x01",
            "在过去根本就无法想象。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "听说里面的设备也很齐全，\x01",
            "旧市政厅完全\x01",
            "没法和它比……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "那场揭幕式\x01",
            "真是体现了\x01",
            "时代的变迁啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1326")

    label("loc_12C3")


    #C0046
    ChrTalk(
        0xFE,
        (
            "兰花塔……\x01",
            "竟能建起那种高耸入云的建筑物，\x01",
            "在过去根本就无法想象。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "技术的进步真是\x01",
            "厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1326")

    Jump("loc_15BD")

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1430")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C1")

    #C0048
    ChrTalk(
        0xFE,
        (
            "不久前搬到附近的\x01",
            "那几个共和国小孩……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "似乎以恶作剧\x01",
            "为乐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "唉，真是可叹……\x01",
            "他们到底接受了什么样的教育啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_142B")

    label("loc_13C1")


    #C0051
    ChrTalk(
        0xFE,
        (
            "小孩会长成什么样，\x01",
            "主要取决于家长的教育方式。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "用心教导孩子，不让他们走错路，\x01",
            "这都是家长的职责。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142B")

    Jump("loc_15BD")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144B")
    Call(0, 12)
    Jump("loc_14C8")

    label("loc_144B")


    #C0053
    ChrTalk(
        0xFE,
        (
            "菲利克言辞不太懂礼貌，\x01",
            "举止也不够端庄，\x01",
            "但却是个为他人着想的好孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "呵呵，能培养出这么好的孩子，\x01",
            "我真是很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C8")

    Jump("loc_15BD")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_15BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1553")

    #C0055
    ChrTalk(
        0xFE,
        (
            "亨利最近不再一味地玩了，\x01",
            "对学习也开始\x01",
            "有了浓厚的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "呵呵，大概是在主日学校\x01",
            "找到了竞争对手吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15BD")

    label("loc_1553")


    #C0057
    ChrTalk(
        0xFE,
        (
            "好好玩耍，好好学习……\x01",
            "我觉得小孩子\x01",
            "就该这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "我希望亨利\x01",
            "在玩耍时玩得尽兴，\x01",
            "在学习时专心用功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BD")

    TalkEnd(0xFE)
    Return()

    # Function_8_8CF end

    def Function_9_15C1(): pass

    label("Function_9_15C1")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0059
    ChrTalk(
        0x8,
        "玛丽埃塔，你可回来了。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "嗯，因为ＩＢＣ总部大楼\x01",
            "已经变成那副模样了……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        (
            "我今天打算去\x01",
            "兰花塔帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "是吗……看来会很忙吧，\x01",
            "你可要注意身体哦。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_9_15C1 end

    def Function_10_167C(): pass

    label("Function_10_167C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0063
    ChrTalk(
        0xA,
        (
            "哇，好棒！\x01",
            "原来用平底锅也能\x01",
            "烤曲奇啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "只要注意别让面团\x01",
            "粘上平底锅，\x01",
            "其它步骤是完全一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "任何工具都可以用\x01",
            "别的东西替代，\x01",
            "你可要用心记住。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        "奶奶真厉害！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_10_167C end

    def Function_11_1743(): pass

    label("Function_11_1743")


    #C0067
    ChrTalk(
        0x8,
        (
            "对了，约库斯，\x01",
            "玛丽埃塔回国的事\x01",
            "现在有眉目了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "唔，短期内恐怕很难呢。\x01",
            "她现在好像很忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "是吗……\x01",
            "看来还要等一段时间，\x01",
            "才能全家一起吃团圆饭啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_11_1743 end

    def Function_12_17F2(): pass

    label("Function_12_17F2")

    OP_4B(0x9, 0xFF)

    #C0070
    ChrTalk(
        0x8,
        (
            "……啊，好痛。\x01",
            "一到雨天，好多关节就都会痛。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "得去乌尔斯拉医院\x01",
            "拿点药\x01",
            "才行啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        "奶奶，您没事吧？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "不然我陪您\x01",
            "去医院吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    #C0074
    ChrTalk(
        0x8,
        "呵呵，谢谢你了，菲利克。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "但不用麻烦了，我一个人去就可以。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_12_17F2 end

    def Function_13_18DD(): pass

    label("Function_13_18DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_18EE")
    Jump("loc_21E3")

    label("loc_18EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_193C")

    #C0076
    ChrTalk(
        0xFE,
        (
            "虽然外面有那种怪物\x01",
            "出没……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "但老爸他们\x01",
            "不会有事的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_193C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19AB")

    #C0078
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的\x01",
            "情况似乎变得很\x01",
            "奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "不过，我家有奶奶在……\x01",
            "不管发生什么事都没问题吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_19AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A0D")

    #C0080
    ChrTalk(
        0xFE,
        (
            "上次见到妈妈，\x01",
            "还是在纪念庆典的时候呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "哈哈，看到她这么精神，\x01",
            "我真高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A5F")

    #C0082
    ChrTalk(
        0xFE,
        (
            "发生了很严重的\x01",
            "事件啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "现在可不是\x01",
            "参加什么宴会的时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1ACD")

    #C0084
    ChrTalk(
        0xFE,
        (
            "湿气是西服的天敌，\x01",
            "所以下雨天就会特别担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "这可是要在宴会上穿的西装，\x01",
            "必须用心爱惜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1BD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7C")

    #C0086
    ChrTalk(
        0xFE,
        (
            "我偷吃了辛迪做的曲奇，\x01",
            "结果被奶奶骂了，\x01",
            "说我没规矩。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "嗯，再怎么说，我也是\x01",
            "出入社交界的人，\x01",
            "不懂规矩可是致命伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "以后还是注意一下吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BD0")

    label("loc_1B7C")


    #C0089
    ChrTalk(
        0xFE,
        (
            "我偷吃了辛迪做的曲奇，\x01",
            "结果被奶奶骂了，\x01",
            "说我没规矩。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "以后还是注意一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1BD0")

    Jump("loc_21E3")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C2F")

    #C0091
    ChrTalk(
        0xFE,
        (
            "哦哦，从下面传来了\x01",
            "甜甜的味道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "是在做点心吗？\x01",
            "去稍微偷吃点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCD")

    #C0093
    ChrTalk(
        0xFE,
        (
            "在昨晚举办的财经界宴会上，\x01",
            "一直都在讨论独立的话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "但我不太懂这些，\x01",
            "基本插不上嘴。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "稍后还是去向奶奶\x01",
            "请教一下好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D29")

    label("loc_1CCD")


    #C0096
    ChrTalk(
        0xFE,
        (
            "如果不了解社会的时事话题，\x01",
            "在社交界就会陷入孤立。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "稍后还是去向奶奶\x01",
            "请教一下好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D29")

    Jump("loc_21E3")

    label("loc_1D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D95")

    #C0098
    ChrTalk(
        0xFE,
        (
            "哼，辛迪那家伙\x01",
            "把家务事都推给我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "算了，没办法。\x01",
            "我偶尔也得认真\x01",
            "做些家务事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1E63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E20")

    #C0100
    ChrTalk(
        0xFE,
        (
            "工作一向很忙碌的老爸\x01",
            "难得在晚饭时间\x01",
            "回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "哎呀，说起来，\x01",
            "椅子好像不够呢。\x01",
            "得去储物间搬一把出来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E5E")

    label("loc_1E20")


    #C0102
    ChrTalk(
        0xFE,
        (
            "哎呀，说起来，\x01",
            "椅子好像不够呢。\x01",
            "得去储物间搬一把出来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5E")

    Jump("loc_21E3")

    label("loc_1E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F14")

    #C0103
    ChrTalk(
        0xFE,
        (
            "各国首脑今晚要去观看\x01",
            "彩虹剧团的演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "之后会在米修拉姆的迎宾馆\x01",
            "参加一场小型聚餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "好棒啊。\x01",
            "真希望自己有朝一日也能参加\x01",
            "那种级别的宴会。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F8E")

    label("loc_1F14")


    #C0106
    ChrTalk(
        0xFE,
        (
            "各国首脑观看完\x01",
            "彩虹剧团的演出之后，\x01",
            "还会在迎宾馆参加聚餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "好棒啊。\x01",
            "真希望自己有朝一日也能参加\x01",
            "那种级别的宴会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8E")

    Jump("loc_21E3")

    label("loc_1F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FF6")

    #C0108
    ChrTalk(
        0xFE,
        (
            "呵呵，辛迪，\x01",
            "你不如也去参加\x01",
            "一些宴会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "到时候，一定会萌生\x01",
            "全新的价值观。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_207D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2011")
    Call(0, 12)
    Jump("loc_2078")

    label("loc_2011")


    #C0110
    ChrTalk(
        0xFE,
        (
            "啧，奶奶可真是的，\x01",
            "我主动提出背她去医院，\x01",
            "她却拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "不过，奶奶就是这样的人，\x01",
            "也挺不错的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2078")

    Jump("loc_21E3")

    label("loc_207D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216E")

    #C0112
    ChrTalk(
        0xFE,
        (
            "我老爸是\x01",
            "ＩＢＣ事业部的主任。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "他在社交界也有很多人脉，\x01",
            "因此时常收到宴会邀请函。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "但老爸总是很忙，\x01",
            "所以一般都由我\x01",
            "代替他出席宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "哎呀，多亏如此，\x01",
            "让我学到了不少社交界的知识，\x01",
            "每天都过得很充实。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E3")

    label("loc_216E")


    #C0116
    ChrTalk(
        0xFE,
        (
            "参加宴会，\x01",
            "了解社交界的方方面面，\x01",
            "真是让人开心啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "这也多亏了老爹的人脉。\x01",
            "呵呵，这就是工作上的额外好处吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E3")

    TalkEnd(0xFE)
    Return()

    # Function_13_18DD end

    def Function_14_21E7(): pass

    label("Function_14_21E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2262")

    #C0118
    ChrTalk(
        0xFE,
        (
            "索菲亚夫人一家\x01",
            "已经从阿尔摩利卡村\x01",
            "回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "呵呵，太好了，\x01",
            "又可以向索菲亚夫人\x01",
            "请教做菜的方法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA1")

    label("loc_2262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_235B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2304")

    #C0120
    ChrTalk(
        0xFE,
        (
            "我的父母都在兰花塔的\x01",
            "ＩＢＣ事业部\x01",
            "上班……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "他们去上班后，就发生了这种事，\x01",
            "直到现在都没回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        "怎么办……他们没出事吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2356")

    label("loc_2304")


    #C0123
    ChrTalk(
        0xFE,
        (
            "我的父母\x01",
            "去兰花塔上班了，\x01",
            "直到现在都没回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "怎么办……他们没出事吧……\x02",
    )

    CloseMessageWindow()

    label("loc_2356")

    Jump("loc_2BA1")

    label("loc_235B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2430")

    #C0125
    ChrTalk(
        0xFE,
        (
            "在ＩＢＣ事业部工作的\x01",
            "爸爸和妈妈\x01",
            "现在似乎都很忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "听说是因为冻结资产宣言的\x01",
            "发表对各方面都\x01",
            "造成了很大影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "很希望全家人能一直聚在一起……\x01",
            "但到底还是没办法吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24AC")

    label("loc_2430")


    #C0128
    ChrTalk(
        0xFE,
        (
            "在ＩＢＣ事业部工作的\x01",
            "爸爸和妈妈\x01",
            "现在似乎都很忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "很希望全家人能一直聚在一起……\x01",
            "但到底还是没办法吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AC")

    Jump("loc_2BA1")

    label("loc_24B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2527")

    #C0130
    ChrTalk(
        0xFE,
        (
            "妈妈从外国回来了，\x01",
            "总算可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "毕竟发生了那种事件，\x01",
            "如果一家人不在一起，就会觉得很不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA1")

    label("loc_2527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_25A4")

    #C0132
    ChrTalk(
        0xFE,
        (
            "听到那起事件的消息时，\x01",
            "我真是吓了一大跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "之前有好几辆警备队的\x01",
            "装甲车从这里驶过……\x01",
            "呜呜，真可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA1")

    label("loc_25A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261E")

    #C0134
    ChrTalk(
        0xFE,
        (
            "烹饪教室今天没课……\x01",
            "在家里休息一下好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "可以试着改良一下\x01",
            "昨天做的那种曲奇。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2680")

    label("loc_261E")


    #C0136
    ChrTalk(
        0xFE,
        (
            "这次就把\x01",
            "巧克力豆混进\x01",
            "面团里好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "呵呵，做好以后\x01",
            "把奶奶叫来，\x01",
            "一起享受优雅的下午茶吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2680")

    Jump("loc_2BA1")

    label("loc_2685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272E")

    #C0138
    ChrTalk(
        0xFE,
        (
            "我在去索菲亚夫人家\x01",
            "送曲奇的路上，\x01",
            "听到了急救车的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "匆忙抬头一看，\x01",
            "竟然有好几辆开过……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "好可怕，是不是发生\x01",
            "什么重大事故了？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2783")

    label("loc_272E")


    #C0141
    ChrTalk(
        0xFE,
        (
            "……算了，\x01",
            "还是别多想了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "柯林很喜欢我做的曲奇，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2783")

    Jump("loc_2BA1")

    label("loc_2788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2811")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A3")
    Call(0, 10)
    Jump("loc_280C")

    label("loc_27A3")


    #C0143
    ChrTalk(
        0xFE,
        (
            "奶奶真厉害啊，\x01",
            "不用烤箱竟然\x01",
            "也能做曲奇。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "呵呵，稍后给索菲亚夫人送去一些，\x01",
            "让她看看我做的多棒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280C")

    Jump("loc_2BA1")

    label("loc_2811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288C")

    #C0145
    ChrTalk(
        0xFE,
        "哎呀，烤箱坏了……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "我好不容易在索菲亚夫人那里\x01",
            "学会了烤曲奇的方法，\x01",
            "这下却没法烤了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28F0")

    label("loc_288C")


    #C0147
    ChrTalk(
        0xFE,
        (
            "唉，我好不容易在索菲亚夫人那里\x01",
            "学会了烤曲奇的方法……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "但烤箱却坏了，\x01",
            "这下就没法实践了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F0")

    Jump("loc_2BA1")

    label("loc_28F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2903")
    Jump("loc_2BA1")

    label("loc_2903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_29FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29CA")

    #C0149
    ChrTalk(
        0xFE,
        (
            "亨利，你在近距离看到了\x01",
            "兰花塔吧？\x01",
            "感觉如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "是不是很大啊？\x01",
            "看起来花了很多钱吧？\x01",
            "人肯定非常多吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "等、等一下啦，姐姐。\x01",
            "你一下提这么多问题，\x01",
            "我怎么回答得了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29F9")

    label("loc_29CA")


    #C0152
    ChrTalk(
        0xFE,
        (
            "好啦好啦，不要计较这么多，\x01",
            "赶快告诉我嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F9")

    Jump("loc_2BA1")

    label("loc_29FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A70")

    #C0153
    ChrTalk(
        0xFE,
        (
            "亨利好像和朋友\x01",
            "一起去参观\x01",
            "兰花塔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "哎，故意挑人多的时候\x01",
            "去凑热闹，\x01",
            "小孩子可真有精神啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA1")

    label("loc_2A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AB9")

    #C0155
    ChrTalk(
        0xFE,
        (
            "哥哥今晚\x01",
            "也要去参加宴会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "真是永远都不厌倦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BA1")

    label("loc_2AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2AC7")
    Jump("loc_2BA1")

    label("loc_2AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B42")

    #C0157
    ChrTalk(
        0xFE,
        "嗯，味道很好☆\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "我做菜的水平越来\x01",
            "越好了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "呵呵，这都要归功于\x01",
            "索菲亚夫人的教导。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BA1")

    label("loc_2B42")


    #C0160
    ChrTalk(
        0xFE,
        (
            "我正在索菲亚夫人\x01",
            "定期开课的烹饪教室\x01",
            "学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "呵呵，多亏如此，\x01",
            "做菜的水平有不少长进呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA1")

    TalkEnd(0xFE)
    Return()

    # Function_14_21E7 end

    def Function_15_2BA5(): pass

    label("Function_15_2BA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C1C")

    #C0162
    ChrTalk(
        0xFE,
        (
            "我们和众多塔内职员\x01",
            "都被关在了\x01",
            "兰花塔里。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "让孩子们和老妈\x01",
            "担惊受怕了一场，\x01",
            "如今总算回到家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5D")

    label("loc_2C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C2A")
    Jump("loc_2D5D")

    label("loc_2C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2CE3")

    #C0164
    ChrTalk(
        0xFE,
        (
            "像上次那样的袭击事件，\x01",
            "今后说不定还会发生。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "唔，不如说……在现在这种局势下，\x01",
            "无论再发生什么事情都不奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "我身为家里的顶梁柱，\x01",
            "必须要保护好自己的家人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5D")

    label("loc_2CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF5")
    Call(0, 11)
    Jump("loc_2D5D")

    label("loc_2CF5")


    #C0167
    ChrTalk(
        0xFE,
        (
            "我妻子玛丽埃塔\x01",
            "在外国的ＩＢＣ分公司工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "那边的工作非常忙，\x01",
            "大概还要再过一段时间才能回来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5D")

    TalkEnd(0xFE)
    Return()

    # Function_15_2BA5 end

    def Function_16_2D61(): pass

    label("Function_16_2D61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DCB")

    #C0169
    ChrTalk(
        0xFE,
        (
            "我们不在家时，\x01",
            "一直都靠婆婆来\x01",
            "安慰两个孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "呵呵，真是欠了婆婆\x01",
            "很大的人情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EE9")

    label("loc_2DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2DD9")
    Jump("loc_2EE9")

    label("loc_2DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E68")

    #C0171
    ChrTalk(
        0xFE,
        (
            "由于总统发表了那样的演讲，\x01",
            "所以我和丈夫得到了特别许可，\x01",
            "可以回家来看看情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "呵呵，有个这么可靠的婆婆，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EE9")

    label("loc_2E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2EE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E83")
    Call(0, 9)
    Jump("loc_2EE9")

    label("loc_2E83")


    #C0173
    ChrTalk(
        0xFE,
        (
            "呵呵，两个孩子和婆婆\x01",
            "都没在袭击中受伤，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "好了……得赶快\x01",
            "去ＩＢＣ事业部\x01",
            "帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE9")

    TalkEnd(0xFE)
    Return()

    # Function_16_2D61 end

    def Function_17_2EED(): pass

    label("Function_17_2EED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EFE")
    Jump("loc_313F")

    label("loc_2EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F77")

    #C0175
    ChrTalk(
        0xFE,
        (
            "戒严令正式下达之后，\x01",
            "政府提供的食品也不再继续发放了。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "这种状况要是一直持续下去，可就麻烦了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_313F")

    label("loc_2F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F85")
    Jump("loc_313F")

    label("loc_2F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3002")

    #C0177
    ChrTalk(
        0xFE,
        "（嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "啊，支援科的各位\x01",
            "来我家有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "如果方便，\x01",
            "就和我们一起吃晚饭吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_305B")

    label("loc_3002")


    #C0180
    ChrTalk(
        0xFE,
        (
            "话说回来，白天的揭幕式\x01",
            "真是很壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "各位警察肯定\x01",
            "都很繁忙吧，\x01",
            "请大家加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305B")

    Jump("loc_313F")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_313F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EA")

    #C0182
    ChrTalk(
        0xFE,
        (
            "我最近的考试分数\x01",
            "一直比琪雅低。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "虽然主日学校昨天\x01",
            "布置了很多作业，\x01",
            "但我必须认真完成，再好好自习一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_313F")

    label("loc_30EA")


    #C0184
    ChrTalk(
        0xFE,
        (
            "奶奶说过，\x01",
            "『自习最重要』。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "为了在下次考试时\x01",
            "超过琪雅，\x01",
            "我一定要好好学习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313F")

    TalkEnd(0xFE)
    Return()

    # Function_17_2EED end

    SaveToFile()

Try(main)
