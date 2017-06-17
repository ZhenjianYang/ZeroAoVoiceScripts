from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "イズリ夫人",             # 1
        "フェリック",             # 2
        "シンディ",               # 3
        "アンリ",                 # 4
        "ユンクス",               # 5
        "マリエッタ",             # 6
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
        "Function_9_193B",         # 09, 9
        "Function_10_1A30",        # 0A, 10
        "Function_11_1B2D",        # 0B, 11
        "Function_12_1C10",        # 0C, 12
        "Function_13_1D29",        # 0D, 13
        "Function_14_289B",        # 0E, 14
        "Function_15_34C1",        # 0F, 15
        "Function_16_36E5",        # 10, 16
        "Function_17_38CB",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_953")

    #C0001
    ChrTalk(
        0xFE,
        (
            "やはり、こういうときこそ\x01",
            "家族で一緒にいなくてはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "ともあれ、息子夫婦が\x01",
            "無事でよかったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9C1")

    label("loc_953")


    #C0003
    ChrTalk(
        0xFE,
        (
            "一家の大黒柱である\x01",
            "息子夫婦が無事でよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "やはり、こういうときこそ\x01",
            "家族で一緒にいなくてはね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C1")

    Jump("loc_1937")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC6")

    #C0005
    ChrTalk(
        0xFE,
        (
            "大切なのは、どんな時でも\x01",
            "堂々と構えていることです。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "堂々とさえしていれば、\x01",
            "他者に伝染しがちな怯えや不安も\x01",
            "きっと吹き飛んでいくでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "子供たちも、息子夫婦の事は\x01",
            "不安でしょうが……\x01",
            "私がしっかりしていなければね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B72")

    label("loc_AC6")


    #C0008
    ChrTalk(
        0xFE,
        (
            "堂々とさえしていれば、\x01",
            "他者に伝染しがちな怯えや不安も\x01",
            "きっと吹き飛んでいくでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "子供たちも、息子夫婦の事は\x01",
            "不安でしょうが……\x01",
            "私がしっかりしていなければね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B72")

    Jump("loc_1937")

    label("loc_B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C48")

    #C0010
    ChrTalk(
        0xFE,
        (
            "この先、クロスベルは\x01",
            "大変な事になっていくでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "でも、私たち家族が一丸になれば\x01",
            "きっと大丈夫……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "どんなことがあっても\x01",
            "皆で力をあわせて、\x01",
            "乗り切っていかなければね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CCB")

    label("loc_C48")


    #C0013
    ChrTalk(
        0xFE,
        (
            "この先、クロスベルは\x01",
            "大変な事になっていくでしょう……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "どんなことがあっても\x01",
            "皆で力をあわせて、\x01",
            "乗り切っていかなければね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCB")

    Jump("loc_1937")

    label("loc_CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEB")
    Call(0, 9)
    Jump("loc_D7E")

    label("loc_CEB")


    #C0015
    ChrTalk(
        0xFE,
        (
            "息子もマリエッタさんも、\x01",
            "破壊されたＩＢＣに勤務していたから\x01",
            "かなり忙しくしてるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "ふう、体を壊さないよう\x01",
            "気をつけて欲しいものだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7E")

    Jump("loc_1937")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E57")

    #C0017
    ChrTalk(
        0xFE,
        (
            "武装集団だなんて\x01",
            "どこから沸いて出たか\x01",
            "分からないけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "罪のない人々を巻き込むなんて\x01",
            "とても許せないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "警備隊には、一刻も早く\x01",
            "マインツの人々を\x01",
            "助け出してほしいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EDC")

    label("loc_E57")


    #C0020
    ChrTalk(
        0xFE,
        (
            "罪のない人々を巻き込むなんて\x01",
            "とても許せないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "警備隊には、一刻も早く\x01",
            "武装集団からマインツの人々を\x01",
            "助け出してほしいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDC")

    Jump("loc_1937")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_100C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F97")

    #C0022
    ChrTalk(
        0xFE,
        (
            "今日はアンリも\x01",
            "出かけているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "雨の日くらい家にいろ、\x01",
            "とまでは言わないけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "濡れて風邪をひかないように\x01",
            "注意していてほしいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1007")

    label("loc_F97")


    #C0025
    ChrTalk(
        0xFE,
        (
            "雨の日くらい家にいろ、\x01",
            "とまでは言わないけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "濡れて風邪をひかないように\x01",
            "注意していてほしいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1007")

    Jump("loc_1937")

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_108B")

    #C0027
    ChrTalk(
        0xFE,
        (
            "さっきまでシンディに\x01",
            "ちょっとした料理のコツを\x01",
            "教えていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "ふぅ……\x01",
            "一仕事終えた後のお茶は格別ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1937")

    label("loc_108B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A6")
    Call(0, 10)
    Jump("loc_10ED")

    label("loc_10A6")


    #C0029
    ChrTalk(
        0xFE,
        (
            "さ、あとは焼きあがるのを待つだけ。\x01",
            "自分だけでやってごらんなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10ED")

    Jump("loc_1937")

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_127C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EC")

    #C0030
    ChrTalk(
        0xFE,
        (
            "クロスベルが国家独立する……\x01",
            "実現すればこの上ない事だと\x01",
            "あたしも思うけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "当然、帝国と共和国は\x01",
            "圧力をかけてくるでしょうし\x01",
            "かなり難しいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "それともディーター市長には、\x01",
            "何かいい策でもあるのかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1277")

    label("loc_11EC")


    #C0033
    ChrTalk(
        0xFE,
        (
            "クロスベルが国家独立する……\x01",
            "実現すればこの上ない事だと\x01",
            "あたしも思うけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ディーター市長には、\x01",
            "何かいい策でもあるのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1277")

    Jump("loc_1937")

    label("loc_127C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")

    #C0035
    ChrTalk(
        0xFE,
        (
            "シンディは今日はおとなりに\x01",
            "遊びに行っているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "ヘイワースさんの奥さんには\x01",
            "よく、お料理教室などで\x01",
            "お世話になっているようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "今度お礼をしなくてはいけませんね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13BB")

    label("loc_134E")


    #C0038
    ChrTalk(
        0xFE,
        (
            "ヘイワースさんの奥さんには\x01",
            "シンディがよくお世話になっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "今度お礼をしなくてはいけませんね。\x02",
    )

    CloseMessageWindow()

    label("loc_13BB")

    Jump("loc_1937")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DB")
    Call(0, 11)
    Jump("loc_1443")

    label("loc_13DB")


    #C0040
    ChrTalk(
        0xFE,
        (
            "マリエッタさんも\x01",
            "忙しいみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "家族全員で食事をするのは\x01",
            "しばらく先のことになりそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1443")

    Jump("loc_1937")

    label("loc_1448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1601")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1571")

    #C0042
    ChrTalk(
        0xFE,
        (
            "除幕式の様子は\x01",
            "この住宅街からも見えたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "あれほど高い建造物が建つなど、\x01",
            "昔では考えられませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "内部の設備も、旧市庁舎とは\x01",
            "比べ物にならないほど\x01",
            "整っているといいますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "まさに、あの除幕式は\x01",
            "歴史の移り変わりを\x01",
            "表しているようでしたね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15FC")

    label("loc_1571")


    #C0046
    ChrTalk(
        0xFE,
        (
            "オルキスタワー……\x01",
            "あれほど高い建造物が建つなど、\x01",
            "昔では考えられませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "技術の進歩というものは、\x01",
            "本当にすごいものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FC")

    Jump("loc_1937")

    label("loc_1601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C9")

    #C0048
    ChrTalk(
        0xFE,
        (
            "この間引っ越してきた、\x01",
            "共和国出身の子たち……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "どうやら人に迷惑をかけるのを\x01",
            "楽しんでいるフシがありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "ふう、嘆かわしい……\x01",
            "どういう教育をされたのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_174B")

    label("loc_16C9")


    #C0051
    ChrTalk(
        0xFE,
        (
            "子供がどう成長するかは\x01",
            "親の育て方一つにかかっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "子供が間違った道に行かないよう\x01",
            "導くのも親の務めだと思うのです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174B")

    Jump("loc_1937")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_17F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176B")
    Call(0, 12)
    Jump("loc_17F2")

    label("loc_176B")


    #C0053
    ChrTalk(
        0xFE,
        (
            "フェリックは言葉が荒いし\x01",
            "礼儀正しいとは言えないけれど、\x01",
            "思いやりがある優しい子です。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "ふふ、いい子に育ってくれて\x01",
            "うれしいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F2")

    Jump("loc_1937")

    label("loc_17F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A5")

    #C0055
    ChrTalk(
        0xFE,
        (
            "アンリは最近、遊ぶだけでなく\x01",
            "勉強に対してもかなりのやる気を\x01",
            "見せるようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "ふふ、日曜学校でいい競争相手でも\x01",
            "できたのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1937")

    label("loc_18A5")


    #C0057
    ChrTalk(
        0xFE,
        (
            "よく遊び、よく学ぶ……\x01",
            "それこそが子供のあるべき姿だと\x01",
            "あたしは思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "アンリには、\x01",
            "遊びにも勉強にも一所懸命に\x01",
            "取り組んで欲しいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1937")

    TalkEnd(0xFE)
    Return()

    # Function_8_8CF end

    def Function_9_193B(): pass

    label("Function_9_193B")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0059
    ChrTalk(
        0x8,
        "マリエッタさん、よく戻ってきたわね。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "ええ、ＩＢＣ本社が\x01",
            "あんな事になっちゃいましたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        (
            "今日はこのままオルキスタワーに\x01",
            "手伝いに向かう予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "そう……忙しいようだけど\x01",
            "体を壊さないようにね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_9_193B end

    def Function_10_1A30(): pass

    label("Function_10_1A30")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0063
    ChrTalk(
        0xA,
        (
            "へえ、すご～い！\x01",
            "クッキーってフライパンでも\x01",
            "焼けちゃうのね！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "生地が張り付かないように\x01",
            "気をつけてさえいれば、\x01",
            "基本は同じですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "道具なんか\x01",
            "いくらでも代用がきくの。\x01",
            "覚えておくといいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        "さっすがお婆ちゃん！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_10_1A30 end

    def Function_11_1B2D(): pass

    label("Function_11_1B2D")


    #C0067
    ChrTalk(
        0x8,
        (
            "そういえばユンクス、\x01",
            "マリエッタさんは帰国の目処は\x01",
            "ついているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "うーん、しばらく難しいかもな。\x01",
            "結構忙しくしてるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "そう……\x01",
            "家族全員で食事をするのは\x01",
            "しばらく先のことになりそうね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_11_1B2D end

    def Function_12_1C10(): pass

    label("Function_12_1C10")

    OP_4B(0x9, 0xFF)

    #C0070
    ChrTalk(
        0x8,
        (
            "……あいたた。\x01",
            "雨の日は節々が痛むわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "ウルスラ病院に\x01",
            "薬をもらいにいかなくては\x01",
            "ならないのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        "婆ちゃん、大丈夫かい？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "なんなら俺が病院まで\x01",
            "付き添おうか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    #C0074
    ChrTalk(
        0x8,
        "ふふ、ありがとうフェリック。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "でも結構よ、１人で行けますから。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_12_1C10 end

    def Function_13_1D29(): pass

    label("Function_13_1D29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D3A")
    Jump("loc_2897")

    label("loc_1D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D9E")

    #C0076
    ChrTalk(
        0xFE,
        (
            "外じゃあんな化物が\x01",
            "うろついてるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "親父たちなら\x01",
            "きっと大丈夫だよな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E2F")

    #C0078
    ChrTalk(
        0xFE,
        (
            "なんだかクロスベルが\x01",
            "妙なことになっちまってる\x01",
            "みたいだなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "ま、ウチには婆ちゃんがいるし……\x01",
            "何があっても平気だよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E8D")

    #C0080
    ChrTalk(
        0xFE,
        (
            "母ちゃん、この間の\x01",
            "記念祭以来だなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "へへ、元気そうで\x01",
            "なによりだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1F03")

    #C0082
    ChrTalk(
        0xFE,
        (
            "とんでもない事件が\x01",
            "起こっちまったなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "こりゃ、パーティなんかに\x01",
            "参加してる場合じゃないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F87")

    #C0084
    ChrTalk(
        0xFE,
        (
            "湿気はスーツの天敵なんだよな。\x01",
            "雨の日は特に気を遣うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "パーティに着ていくスーツなんだ、\x01",
            "大事にしないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_1F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207E")

    #C0086
    ChrTalk(
        0xFE,
        (
            "シンディが作ったクッキーを\x01",
            "つまみ食いしたら、行儀が悪いって\x01",
            "婆ちゃんに叱られちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "うーん、曲がりなりにも社交界に\x01",
            "出入りしてるのに、行儀が悪いのは\x01",
            "ちょっと致命的だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "今度からは気をつけようっと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20FE")

    label("loc_207E")


    #C0089
    ChrTalk(
        0xFE,
        (
            "シンディが作ったクッキーを\x01",
            "つまみ食いしたら、行儀が悪いって\x01",
            "婆ちゃんに叱られちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "今度からは気をつけようっと。\x02",
    )

    CloseMessageWindow()

    label("loc_20FE")

    Jump("loc_2897")

    label("loc_2103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2187")

    #C0091
    ChrTalk(
        0xFE,
        (
            "おお、なんだか下から\x01",
            "甘くていい匂いがしてきたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "お菓子でも作ってんのかな。\x01",
            "ひとつまみもらいにいこうっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_22DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2261")

    #C0093
    ChrTalk(
        0xFE,
        (
            "昨夜行った財界人のパーティでも、\x01",
            "独立の話題が飛び交ってたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "けど俺、よく分かってなくて\x01",
            "いまいち話についていけなくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "婆ちゃんに聞いて、\x01",
            "どういうことか勉強しとこうかなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22D7")

    label("loc_2261")


    #C0096
    ChrTalk(
        0xFE,
        (
            "今時の話題についていけないんじゃ、\x01",
            "社交界では取り残されちまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "独立のことは\x01",
            "婆ちゃんに教えてもらおうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D7")

    Jump("loc_2897")

    label("loc_22DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2367")

    #C0098
    ChrTalk(
        0xFE,
        (
            "ちぇっ、シンディのやつに\x01",
            "家事を押し付けられちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "まあ、仕方ねえか。\x01",
            "俺もたまにはちゃんと\x01",
            "家事をやんないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240A")

    #C0100
    ChrTalk(
        0xFE,
        (
            "仕事で忙しい親父が、\x01",
            "久しぶりに夕飯の時間に\x01",
            "帰ってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "ありゃ、そういえば\x01",
            "イスが足りないな。\x01",
            "物置から出してこないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2450")

    label("loc_240A")


    #C0102
    ChrTalk(
        0xFE,
        (
            "ありゃ、そういえば\x01",
            "イスが足りないな。\x01",
            "物置から出してこないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2450")

    Jump("loc_2897")

    label("loc_2455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252E")

    #C0103
    ChrTalk(
        0xFE,
        (
            "今夜は各国の首脳たちが\x01",
            "アルカンシェルを観劇するらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "そのあとミシュラムの迎賓館で\x01",
            "ちょっとした会食があるそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "いいよなあ。\x01",
            "俺もいつかそんなパーティに\x01",
            "参加してみたいぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25B6")

    label("loc_252E")


    #C0106
    ChrTalk(
        0xFE,
        (
            "各国の首脳たちは、\x01",
            "アルカンシェルを見た後\x01",
            "迎賓館で会食するらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "いいよなあ。\x01",
            "俺もいつかそんなパーティに\x01",
            "参加してみたいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B6")

    Jump("loc_2897")

    label("loc_25BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2646")

    #C0108
    ChrTalk(
        0xFE,
        (
            "フフ、シンディ。\x01",
            "なんだったらお前も\x01",
            "パーティに参加してみるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "きっと新しい価値観に\x01",
            "目覚めること請け合いだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_2646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2661")
    Call(0, 12)
    Jump("loc_26D2")

    label("loc_2661")


    #C0110
    ChrTalk(
        0xFE,
        (
            "ちぇ、婆ちゃんってば\x01",
            "せっかくおぶってやるって\x01",
            "言ってるのにさー。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "ま、婆ちゃんらしくて\x01",
            "いいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D2")

    Jump("loc_2897")

    label("loc_26D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2810")

    #C0112
    ChrTalk(
        0xFE,
        (
            "俺んちの親父、\x01",
            "ＩＢＣの事業部の主任でさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "社交界にもコネがあって、\x01",
            "よくパーティの招待状とかが届くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "ただ、親父はなかなか忙しくてね。\x01",
            "せっかくだから俺が代理として\x01",
            "出席させてもらってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "いや～、おかげさまで\x01",
            "社交界のことを色々勉強できるし\x01",
            "毎日が充実してるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2897")

    label("loc_2810")


    #C0116
    ChrTalk(
        0xFE,
        (
            "パーティに参加するのって、\x01",
            "社交界のことが色々わかって\x01",
            "楽しいんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "これも親父のコネのおかげ。\x01",
            "へへ、役得ってやつかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2897")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D29 end

    def Function_14_289B(): pass

    label("Function_14_289B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2928")

    #C0118
    ChrTalk(
        0xFE,
        (
            "ソフィアさんのご家族も\x01",
            "アルモリカ村から\x01",
            "戻ってきてたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "ふふ、よかった。\x01",
            "またお料理を教えて\x01",
            "もらわなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_2928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F0")

    #C0120
    ChrTalk(
        0xFE,
        (
            "父さんと母さんも、\x01",
            "オルキスタワーのＩＢＣ事業部に\x01",
            "勤めてたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "仕事に行ったままこんな事が起きて、\x01",
            "まだ帰ってきていないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        "どうしよう、大丈夫かな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A5C")

    label("loc_29F0")


    #C0123
    ChrTalk(
        0xFE,
        (
            "父さんと母さん、\x01",
            "オルキスタワーに仕事に行ったまま\x01",
            "帰ってきていないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "どうしよう、大丈夫かな……\x02",
    )

    CloseMessageWindow()

    label("loc_2A5C")

    Jump("loc_34BD")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2BF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5E")

    #C0125
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ事業部に勤めてる\x01",
            "お父さんとお母さんも、\x01",
            "今は相当忙しいみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "資産凍結とかの話が出たから\x01",
            "色んな方面に影響が\x01",
            "出ちゃってるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "こんな時だから\x01",
            "みんな一緒にいたかったけど……\x01",
            "仕方ないでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BF4")

    label("loc_2B5E")


    #C0128
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ事業部に勤めてる\x01",
            "お父さんとお母さんも、\x01",
            "今は相当忙しいみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "こんな時だから\x01",
            "みんな一緒にいたかったけど……\x01",
            "仕方ないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF4")

    Jump("loc_34BD")

    label("loc_2BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C8B")

    #C0130
    ChrTalk(
        0xFE,
        (
            "お母さんが外国から戻ってきたの。\x01",
            "……なんだか安心しちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "あんな事件があったんだし、\x01",
            "家族が離れ離れだと不安だもんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_2C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D18")

    #C0132
    ChrTalk(
        0xFE,
        (
            "事件のニュースを聞いて\x01",
            "びっくりしちゃったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "警備隊の装甲車も\x01",
            "何台も通ってるみたいだし……\x01",
            "うう、やっぱり怖いわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_2D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD0")

    #C0134
    ChrTalk(
        0xFE,
        (
            "今日はお料理教室もないし……\x01",
            "おうちでゆっくりとしてようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "そうだ、昨日作ったみたいな\x01",
            "クッキーのアレンジを研究するのも\x01",
            "楽しいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E50")

    label("loc_2DD0")


    #C0136
    ChrTalk(
        0xFE,
        (
            "クッキーの生地に\x01",
            "チョコレートチップを\x01",
            "混ぜてみようかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "ふふ、完成したら\x01",
            "お婆ちゃんも呼んで\x01",
            "優雅なティータイムね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E50")

    Jump("loc_34BD")

    label("loc_2E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F28")

    #C0138
    ChrTalk(
        0xFE,
        (
            "ソフィアさんちに\x01",
            "クッキーを届けに行く途中で、\x01",
            "救急車のサイレンが聞こえたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "急いで見にいったら、\x01",
            "結構な台数が通っていって……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "やだなあ、大きな事故でも\x01",
            "あったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FA3")

    label("loc_2F28")


    #C0141
    ChrTalk(
        0xFE,
        (
            "……まあいっか。\x01",
            "深く考えないようにしよっと。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "とにかく、コリン君が\x01",
            "私の作ったクッキーを\x01",
            "喜んでくれて良かったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA3")

    Jump("loc_34BD")

    label("loc_2FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC3")
    Call(0, 10)
    Jump("loc_3050")

    label("loc_2FC3")


    #C0143
    ChrTalk(
        0xFE,
        (
            "さっすがお婆ちゃんね。\x01",
            "オーブンを使わなくても\x01",
            "クッキーができちゃうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "ふふ、あとでソフィアさんに\x01",
            "出来栄えを見てもらおうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3050")

    Jump("loc_34BD")

    label("loc_3055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_316F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EC")

    #C0145
    ChrTalk(
        0xFE,
        "あれー、オーブンが壊れてる……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "せっかくソフィアさんに\x01",
            "クッキーの焼き方を教わったのに、\x01",
            "これじゃあ焼けないよ～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_316A")

    label("loc_30EC")


    #C0147
    ChrTalk(
        0xFE,
        (
            "はあ、せっかくソフィアさんに\x01",
            "クッキーの焼き方を教わったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "オーブンが壊れてるんじゃ、\x01",
            "当分は実践できないよ～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_316A")

    Jump("loc_34BD")

    label("loc_316F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_317D")
    Jump("loc_34BD")

    label("loc_317D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_32AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3278")

    #C0149
    ChrTalk(
        0xFE,
        (
            "アンリ、オルキスタワーを\x01",
            "近くで見てきたんでしょ。\x01",
            "どんな感じだった？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "やっぱり大っきかった？\x01",
            "ミラがかかってそうだった？\x01",
            "いっぱい人いた？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "ちょ、ちょっと姉さん。\x01",
            "一度にそんなに質問されても\x01",
            "答えられないってば～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32A7")

    label("loc_3278")


    #C0152
    ChrTalk(
        0xFE,
        (
            "いいじゃない、\x01",
            "ケチケチしないで教えてよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A7")

    Jump("loc_34BD")

    label("loc_32AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3340")

    #C0153
    ChrTalk(
        0xFE,
        (
            "アンリは友達と一緒に\x01",
            "オルキスタワーを\x01",
            "見に行ったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "やー、わざわざ\x01",
            "混んでるときに行くなんて、\x01",
            "子供ってパワフルよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_3340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3395")

    #C0155
    ChrTalk(
        0xFE,
        (
            "お兄ちゃん、\x01",
            "今夜もパーティなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "もう、よく飽きないわねえ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34BD")

    label("loc_3395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33A3")
    Jump("loc_34BD")

    label("loc_33A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3440")

    #C0157
    ChrTalk(
        0xFE,
        "うん、いい味付け☆\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "私ったら、どんどん料理が\x01",
            "上手になっていくわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "ふふ、これもソフィアさんの\x01",
            "教えのおかげかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34BD")

    label("loc_3440")


    #C0160
    ChrTalk(
        0xFE,
        (
            "私、お隣のソフィアさんが\x01",
            "定期的に開いてる\x01",
            "お料理教室に通ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "ふふ、おかげさまで\x01",
            "料理の腕がかなり上達したわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BD")

    TalkEnd(0xFE)
    Return()

    # Function_14_289B end

    def Function_15_34C1(): pass

    label("Function_15_34C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_356A")

    #C0162
    ChrTalk(
        0xFE,
        (
            "私たちは、職員たちと一緒に\x01",
            "オルキスタワーに\x01",
            "閉じ込められていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "子供達やお袋には\x01",
            "心配をかけてしまったが、\x01",
            "何とか帰ってこれてよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_356A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3578")
    Jump("loc_36E1")

    label("loc_3578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_364F")

    #C0164
    ChrTalk(
        0xFE,
        (
            "この間の襲撃事件みたいなことが\x01",
            "またいつ起きるとも分からない。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "いや、むしろ何が起きても\x01",
            "不思議じゃない状況なのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "私も一家の大黒柱として、\x01",
            "しっかりと家族を守っていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_364F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3661")
    Call(0, 11)
    Jump("loc_36E1")

    label("loc_3661")


    #C0167
    ChrTalk(
        0xFE,
        (
            "妻のマリエッタは\x01",
            "外国のＩＢＣ支社で働いてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "あっちはあっちで忙しそうだし、\x01",
            "帰ってくるのはまだまだ先だろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E1")

    TalkEnd(0xFE)
    Return()

    # Function_15_34C1 end

    def Function_16_36E5(): pass

    label("Function_16_36E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3775")

    #C0169
    ChrTalk(
        0xFE,
        (
            "私たちがいない間、\x01",
            "お義母さんが子供達を\x01",
            "勇気付けてくれていたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "ふふ、お義母さんには\x01",
            "本当に頭が上がらないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C7")

    label("loc_3775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3783")
    Jump("loc_38C7")

    label("loc_3783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3820")

    #C0171
    ChrTalk(
        0xFE,
        (
            "あんな演説があったからね、\x01",
            "夫と２人で特別に許可をとって、\x01",
            "家の様子を見に来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "ふふ、頼りになるお義母さんで\x01",
            "本当に助かっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C7")

    label("loc_3820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383B")
    Call(0, 9)
    Jump("loc_38C7")

    label("loc_383B")


    #C0173
    ChrTalk(
        0xFE,
        (
            "ふふ、息子たちも義母さんも、\x01",
            "襲撃で怪我なんてしてなくて\x01",
            "本当に良かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "さてと……はやく\x01",
            "ＩＢＣ事業部の手伝いに\x01",
            "行かないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C7")

    TalkEnd(0xFE)
    Return()

    # Function_16_36E5 end

    def Function_17_38CB(): pass

    label("Function_17_38CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38DC")
    Jump("loc_3B7F")

    label("loc_38DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_394D")

    #C0175
    ChrTalk(
        0xFE,
        (
            "政府支給の食品も、\x01",
            "戒厳令から入ってきてないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "この状況が続いたら厳しいですよね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B7F")

    label("loc_394D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_395B")
    Jump("loc_3B7F")

    label("loc_395B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E6")

    #C0177
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "あ、支援課の皆さん。\x01",
            "ウチになにか用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "よかったら一緒に\x01",
            "夕飯を食べていきます？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A5B")

    label("loc_39E6")


    #C0180
    ChrTalk(
        0xFE,
        (
            "それにしても昼の除幕式は\x01",
            "すごかったですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "警察のみなさんは\x01",
            "忙しいでしょうけど、\x01",
            "がんばってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5B")

    Jump("loc_3B7F")

    label("loc_3A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AFC")

    #C0182
    ChrTalk(
        0xFE,
        (
            "昨日は日曜学校で\x01",
            "たくさん宿題が出たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "最近はテストの点でも\x01",
            "キーアちゃんに負けてますし、\x01",
            "きちんと自習もしないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B7F")

    label("loc_3AFC")


    #C0184
    ChrTalk(
        0xFE,
        (
            "『大切なのは自習だ』って、\x01",
            "おばあちゃんも言ってました。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "次はテストで\x01",
            "キーアちゃんに勝てるように、\x01",
            "しっかり勉強しないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B7F")

    TalkEnd(0xFE)
    Return()

    # Function_17_38CB end

    SaveToFile()

Try(main)
