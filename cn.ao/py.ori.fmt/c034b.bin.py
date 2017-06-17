from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c034b.bin",                # FileName
        "c034b",                    # MapName
        "c034b",                    # Location
        0x002D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c034b",                  # 0
        "伊兹丽夫人",             # 1
        "菲利克",                 # 2
        "辛迪",                   # 3
        "亨利",                   # 4
        "约库斯",                 # 5
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

    DeclNpc(40669,   0,       9600,    360,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(32659,   0,       5679,    180,  261,  0x0, 0,   2,   0,   0,   2,   0,   7,   255,  0)
    DeclNpc(4980,    0,       8989,    89,   261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(5329,    0,       3990,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(689,     0,       990,     225,  389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)

    ChipFrameInfo(372, 0)                                        # 0

    ScpFunction((
        "Function_0_174",          # 00, 0
        "Function_1_224",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_277",          # 03, 3
        "Function_4_33E",          # 04, 4
        "Function_5_33F",          # 05, 5
        "Function_6_3AC",          # 06, 6
        "Function_7_45F",          # 07, 7
        "Function_8_526",          # 08, 8
        "Function_9_61A",          # 09, 9
        "Function_10_6F4",         # 0A, 10
    ))


    def Function_0_174(): pass

    label("Function_0_174")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1AC"),
        (1, "loc_1B8"),
        (2, "loc_1C4"),
        (3, "loc_1D0"),
        (4, "loc_1DC"),
        (5, "loc_1E8"),
        (6, "loc_1F4"),
        (SWITCH_DEFAULT, "loc_200"),
    )


    label("loc_1AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_20C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_223")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_223")

    Return()

    # Function_0_174 end

    def Function_1_224(): pass

    label("Function_1_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_94(0xFE, 0x14D2, 0xFFFFFCAE, 0xFFFFF6B4, 0x94C, 0x3E8)
    Jump("Function_1_224")

    label("loc_24B")

    Return()

    # Function_1_224 end

    def Function_2_24C(): pass

    label("Function_2_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_276")
    OP_94(0xFE, 0x7738, 0x1126, 0x852A, 0x1D38, 0x3E8)
    Sleep(300)
    Jump("Function_2_24C")

    label("loc_276")

    Return()

    # Function_2_24C end

    def Function_3_277(): pass

    label("Function_3_277")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_2D4")

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
    BeginChrThread(0x9, 0, 0, 1)
    Return()

    # Function_3_277 end

    def Function_4_33E(): pass

    label("Function_4_33E")

    Return()

    # Function_4_33E end

    def Function_5_33F(): pass

    label("Function_5_33F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    Call(0, 6)
    Jump("loc_3A8")

    label("loc_354")


    #C0001
    ChrTalk(
        0xFE,
        (
            "玛丽埃塔\x01",
            "似乎也很忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "看样子，要想全家一起吃顿饭，\x01",
            "还要再等一段时间呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A8")

    TalkEnd(0xFE)
    Return()

    # Function_5_33F end

    def Function_6_3AC(): pass

    label("Function_6_3AC")


    #C0003
    ChrTalk(
        0x8,
        (
            "对了，约库斯，\x01",
            "玛丽埃塔回国的事\x01",
            "现在有眉目了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xC,
        (
            "唔，短期内恐怕很难呢。\x01",
            "她现在好像很忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "是吗……\x01",
            "看样子，要想全家一起吃顿饭，\x01",
            "还要再等一段时间呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_3AC end

    def Function_7_45F(): pass

    label("Function_7_45F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E4")

    #C0006
    ChrTalk(
        0xFE,
        (
            "工作一向很忙碌的老爸\x01",
            "难得在晚饭时间\x01",
            "回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
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
    Jump("loc_522")

    label("loc_4E4")


    #C0008
    ChrTalk(
        0xFE,
        (
            "哎呀，说起来，\x01",
            "椅子好像不够呢。\x01",
            "得去储物间搬一把出来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_522")

    TalkEnd(0xFE)
    Return()

    # Function_7_45F end

    def Function_8_526(): pass

    label("Function_8_526")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7")

    #C0009
    ChrTalk(
        0xFE,
        (
            "亨利，你在近距离看到了\x01",
            "兰花塔吧？\x01",
            "感觉如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "是不是很大啊？\x01",
            "看起来花了很多钱吧？\x01",
            "人肯定非常多吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
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
    Jump("loc_616")

    label("loc_5E7")


    #C0012
    ChrTalk(
        0xFE,
        (
            "好啦好啦，不要计较这么多，\x01",
            "赶快告诉我嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_616")

    TalkEnd(0xFE)
    Return()

    # Function_8_526 end

    def Function_9_61A(): pass

    label("Function_9_61A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_695")

    #C0013
    ChrTalk(
        0xFE,
        "（吃东西）……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "啊，支援科的各位，\x01",
            "来我家有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "如果方便，\x01",
            "就和我们一起吃晚饭吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6F0")

    label("loc_695")


    #C0016
    ChrTalk(
        0xFE,
        (
            "话说回来，白天的揭幕式\x01",
            "真是很壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "看来各位警察\x01",
            "都很繁忙，\x01",
            "请大家继续加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F0")

    TalkEnd(0xFE)
    Return()

    # Function_9_61A end

    def Function_10_6F4(): pass

    label("Function_10_6F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_709")
    Call(0, 6)
    Jump("loc_76F")

    label("loc_709")


    #C0018
    ChrTalk(
        0xFE,
        (
            "我妻子玛丽埃塔\x01",
            "在外国的ＩＢＣ分公司工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "她的工作非常忙，\x01",
            "大概还要再过一段时间才能回来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76F")

    TalkEnd(0xFE)
    Return()

    # Function_10_6F4 end

    SaveToFile()

Try(main)
