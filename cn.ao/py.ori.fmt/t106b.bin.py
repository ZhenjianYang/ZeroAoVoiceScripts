from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t106b.bin",                # FileName
        "t106b",                    # MapName
        "t106b",                    # Location
        0x0042,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 1, 0, 2],
    )

    BuildStringList((
        "t106b",                  # 0
        "游客",                   # 1
        "游客",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "男孩",                   # 5
    ))

    AddCharChip((
        "chr/ch27600.itc",                   # 00
        "chr/ch33300.itc",                   # 01
        "chr/ch23402.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch23800.itc",                   # 04
    ))

    DeclNpc(-101040, 0,       1070,    180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-95849,  0,       3210,    0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(101919,  400,     -2849,   0,    453,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(101940,  0,       -1720,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(99339,   0,       -209,    135,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)

    ChipFrameInfo(340, 0)                                        # 0

    ScpFunction((
        "Function_0_154",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_270",          # 03, 3
        "Function_4_2F1",          # 04, 4
        "Function_5_375",          # 05, 5
        "Function_6_408",          # 06, 6
        "Function_7_463",          # 07, 7
    ))


    def Function_0_154(): pass

    label("Function_0_154")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_194"),
        (1, "loc_1A0"),
        (2, "loc_1AC"),
        (3, "loc_1B8"),
        (4, "loc_1C4"),
        (5, "loc_1D0"),
        (6, "loc_1DC"),
        (SWITCH_DEFAULT, "loc_1E8"),
    )


    label("loc_194")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_20B")

    Return()

    # Function_0_154 end

    def Function_1_20C(): pass

    label("Function_1_20C")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_22B")
    Jump("loc_26E")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_257")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_26E")

    label("loc_257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_265")
    Jump("loc_26E")

    label("loc_265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_26E")

    label("loc_26E")

    Return()

    # Function_1_20C end

    def Function_2_26F(): pass

    label("Function_2_26F")

    Return()

    # Function_2_26F end

    def Function_3_270(): pass

    label("Function_3_270")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2D6")

    #C0001
    ChrTalk(
        0xFE,
        (
            "我们是来米修拉姆\x01",
            "新婚旅行的。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "今天真是美好\x01",
            "的一天啊。\x01",
            "必须要感谢她和女神。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED")

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2E4")
    Jump("loc_2ED")

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2ED")

    label("loc_2ED")

    TalkEnd(0xFE)
    Return()

    # Function_3_270 end

    def Function_4_2F1(): pass

    label("Function_4_2F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_35A")

    #C0003
    ChrTalk(
        0xFE,
        (
            "如此有趣又美丽的地方，\x01",
            "实在是很少有。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "呵呵，搬家到克洛斯贝尔\x01",
            "说不定也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371")

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_368")
    Jump("loc_371")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_371")

    label("loc_371")

    TalkEnd(0xFE)
    Return()

    # Function_4_2F1 end

    def Function_5_375(): pass

    label("Function_5_375")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3ED")

    #C0005
    ChrTalk(
        0xFE,
        (
            "我们正准备去看主题公园的\x01",
            "晚间巡游活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "其实我更想\x01",
            "在房间里休息……\x01",
            "哈哈，当爸爸也不容易啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404")

    label("loc_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3FB")
    Jump("loc_404")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_404")

    label("loc_404")

    TalkEnd(0xFE)
    Return()

    # Function_5_375 end

    def Function_6_408(): pass

    label("Function_6_408")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_448")

    #C0007
    ChrTalk(
        0xFE,
        (
            "呵呵，孩子还在等着我，\x01",
            "必须得赶快准备好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_456")
    Jump("loc_45F")

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_45F")

    label("loc_45F")

    TalkEnd(0xFE)
    Return()

    # Function_6_408 end

    def Function_7_463(): pass

    label("Function_7_463")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B7")

    #C0008
    ChrTalk(
        0xFE,
        "爸爸、妈妈，还没好吗！？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "再不快一点，\x01",
            "巡游就要结束了哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4C5")
    Jump("loc_4CE")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4CE")

    label("loc_4CE")

    TalkEnd(0xFE)
    Return()

    # Function_7_463 end

    SaveToFile()

Try(main)
