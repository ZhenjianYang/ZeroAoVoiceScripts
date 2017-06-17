from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0320.bin",                # FileName
        "c0320",                    # MapName
        "c0320",                    # Location
        0x002D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0320",                  # 0
        "坎贝尔议员",             # 1
        "共和国派议员",           # 2
        "共和国派议员",           # 3
        "卡拉",                   # 4
        "玛夏",                   # 5
    ))

    AddCharChip((
        "chr/ch27702.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch27802.itc",                   # 02
        "chr/ch33200.itc",                   # 03
        "chr/ch34500.itc",                   # 04
    ))

    DeclNpc(0,       250,     46110,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-2490,   0,       48869,   45,   389,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(2299,    250,     43630,   270,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(43490,   59,      3440,    135,  389,  0x0, 0,   3,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(-44409,  0,       10199,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(45950,   60,      1790,    1500,    46410,   1000,    1270,    0x007C, 0,  13, 0x0000)

    ScpFunction((
        "Function_0_190",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_273",          # 02, 2
        "Function_3_29E",          # 03, 3
        "Function_4_311",          # 04, 4
        "Function_5_383",          # 05, 5
        "Function_6_835",          # 06, 6
        "Function_7_964",          # 07, 7
        "Function_8_11FB",         # 08, 8
        "Function_9_151D",         # 09, 9
        "Function_10_17A5",        # 0A, 10
        "Function_11_2623",        # 0B, 11
        "Function_12_2D6D",        # 0C, 12
        "Function_13_35EA",        # 0D, 13
    ))


    def Function_0_190(): pass

    label("Function_0_190")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1D0"),
        (1, "loc_1DC"),
        (2, "loc_1E8"),
        (3, "loc_1F4"),
        (4, "loc_200"),
        (5, "loc_20C"),
        (6, "loc_218"),
        (SWITCH_DEFAULT, "loc_224"),
    )


    label("loc_1D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_200")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_20C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_218")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_224")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_230")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_247")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_247")

    Return()

    # Function_0_190 end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_272")
    OP_94(0xFE, 0xFFFFF57E, 0xC1DE, 0xFFFFEFFC, 0xB4AA, 0x3E8)
    Sleep(300)
    Jump("Function_1_248")

    label("loc_272")

    Return()

    # Function_1_248 end

    def Function_2_273(): pass

    label("Function_2_273")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29D")
    OP_94(0xFE, 0xAE56, 0xD70, 0xA320, 0x67C, 0x3E8)
    Sleep(300)
    Jump("Function_2_273")

    label("loc_29D")

    Return()

    # Function_2_273 end

    def Function_3_29E(): pass

    label("Function_3_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_2B9")
    ClearChrFlags(0xC, 0x80)

    label("loc_2B9")

    Jump("loc_2FE")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DB")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_2FE")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0xA, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0xC, 0x80)

    label("loc_2FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_310")
    ClearChrFlags(0xB, 0x80)

    label("loc_310")

    Return()

    # Function_3_29E end

    def Function_4_311(): pass

    label("Function_4_311")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C")
    OP_66(0x0, 0x1)

    label("loc_34C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x1)
    Jump("loc_36B")

    label("loc_365")

    OP_10(0x0, 0x1)
    OP_10(0x7, 0x0)

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_382")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_382")

    label("loc_382")

    Return()

    # Function_4_311 end

    def Function_5_383(): pass

    label("Function_5_383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD")
    Call(0, 10)
    Return()

    label("loc_3AD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_441")
    Jump("loc_48B")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_461")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_481")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B")

    label("loc_481")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_592")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_522")

    #C0001
    ChrTalk(
        0xFE,
        (
            "……对于将小女带回一事，\x01",
            "我姑且表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "哼，仅此而已，\x01",
            "你们可以回去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58D")

    label("loc_522")


    #C0003
    ChrTalk(
        0xFE,
        (
            "哼……警察果然\x01",
            "不值得依靠。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "算了，只要知道她在哪里，\x01",
            "再强行带回即可。\x01",
            "怎样都有办法将她带回来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58D")

    Jump("loc_82D")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76B")

    #C0005
    ChrTalk(
        0xFE,
        (
            "今天由于议会政务和黑月事件，\x01",
            "从早晨开始就忙碌不堪……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "但刚过中午时因为有事\x01",
            "而回来了一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "然而无论我怎么叫，\x01",
            "女儿和女仆也没有出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "在我觉得奇怪时，\x01",
            "就发现了女儿留下的字条。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_763")

    #C0009
    ChrTalk(
        0x104,
        "#0301F（这个议员似乎平时就很目中无人啊。）\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0006F（看样子，\x01",
            "  他好像连女儿的去处\x01",
            "  也毫无头绪。）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2D, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_763")

    #C0011
    ChrTalk(
        0x103,
        (
            "#0200F（情报都搜集完了……\x01",
            "　先回到卡拉小姐的房间，\x01",
            "　再重新开始推理吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0000F（嗯，就这么办吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_763")

    SetScenarioFlags(0x0, 0)
    Jump("loc_82D")

    label("loc_76B")


    #C0013
    ChrTalk(
        0xFE,
        (
            "刚过中午时，我因为有事而回来之后，\x01",
            "就发现女儿和女仆都不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……小女的事就拜托各位了。\x01",
            "若这样下去，这件事可能会被\x01",
            "帝国派当成攻击材料。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#0108F（他难道都\x01",
            "  不担心卡拉小姐吗……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_383 end

    def Function_6_835(): pass

    label("Function_6_835")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_906")

    #C0016
    ChrTalk(
        0xFE,
        (
            "议员秘书的受贿嫌疑，\x01",
            "以及在那座议长宅邸所发生的神秘事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "唔，要用哪件事对帝国派进行攻击\x01",
            "才是最有效的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "预算会议也渐入佳境，\x01",
            "必须快点做出了结，然后\x01",
            "去协助坎贝尔议员呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_960")

    label("loc_906")


    #C0019
    ChrTalk(
        0xFE,
        (
            "在坎贝尔议员\x01",
            "参加议会时，\x01",
            "我就在为了战斗而收集情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "因为议会打的就是情报战啊。\x02",
    )

    CloseMessageWindow()

    label("loc_960")

    TalkEnd(0xFE)
    Return()

    # Function_6_835 end

    def Function_7_964(): pass

    label("Function_7_964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98E")
    Call(0, 10)
    Return()

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C20")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2B")
    Jump("loc_A75")

    label("loc_A2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A4B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A75")

    label("loc_A4B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A75")

    label("loc_A6B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A75")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B38")

    #C0021
    ChrTalk(
        0xFE,
        (
            "就在不久之前，\x01",
            "自治州议会终于结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……嗯，\x01",
            "今年会期真是延长了很久啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "哈哈……\x01",
            "因为我们共和国派\x01",
            "就是坚持到底，不肯妥协。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C14")

    label("loc_B38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_BB3")

    #C0024
    ChrTalk(
        0xFE,
        (
            "咳咳……话说回来，\x01",
            "小姐能回来，\x01",
            "真是太好了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "因为，如果女仆不在的话，\x01",
            "就连茶都没人给泡了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_BB3")


    #C0026
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "茶还没泡好吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "这里的女仆从刚才开始\x01",
            "就不见人影，\x01",
            "到底是在干些什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C14")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_11FA")

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11FA")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC0")
    Jump("loc_D0A")

    label("loc_CC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D0A")

    label("loc_CE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D00")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D0A")

    label("loc_D00")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D0A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F38")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD1")

    #C0028
    ChrTalk(
        0xFE,
        (
            "哎呀，真是太好了。\x01",
            "这样一来，这件事就不会\x01",
            "被帝国派发现了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "呵呵……这下可以安心\x01",
            "专注于制定议会上的对策了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E3D")

    label("loc_DD1")


    #C0030
    ChrTalk(
        0xFE,
        (
            "话说回来，议员竟会方寸大乱，\x01",
            "这还真是少见啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "莫非真的是在担心小姐吗？\x01",
            "……才不可能吧，哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3D")

    Jump("loc_F33")

    label("loc_E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF7")

    #C0032
    ChrTalk(
        0xFE,
        (
            "哎？没能将\x01",
            "小姐带回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀……\x01",
            "算了，只要不被帝国派发现，\x01",
            "怎样都无所谓。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "我们可是在忙着应对黑月和\x01",
            "制定议会上的对策呢，\x01",
            "可以请你们回去了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F33")

    label("loc_EF7")


    #C0035
    ChrTalk(
        0xFE,
        (
            "我们正忙着应对黑月和\x01",
            "制定议会上的对策，\x01",
            "请你们回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F33")

    Jump("loc_11F3")

    label("loc_F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116E")

    #C0036
    ChrTalk(
        0xFE,
        (
            "议员是一个\x01",
            "很有讲究的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "例如，早饭一定要\x01",
            "与家人一起吃，就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "虽然也跟大小姐说过\x01",
            "要遵守这个规矩了，\x01",
            "但她似乎很不情愿呢。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1166")

    #C0039
    ChrTalk(
        0x103,
        "#0203F……是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "两人不和的原因\x01",
            "也许就出在那里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "……总之，小姐今天早上\x01",
            "至少是来吃了早餐的。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "因为我也\x01",
            "一起叨扰了，\x01",
            "肯定不会有错。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1160")

    #C0043
    ChrTalk(
        0x103,
        (
            "#0200F（情报搜集完了……\x01",
            "　先回到卡拉小姐的房间，\x01",
            "　再重新开始推理吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0000F（嗯，就这么办吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_1160")

    OP_29(0x2D, 0x1, 0x3)

    label("loc_1166")

    SetScenarioFlags(0x0, 1)
    Jump("loc_11F3")

    label("loc_116E")


    #C0045
    ChrTalk(
        0xFE,
        (
            "总之我们这边已经因为议会对策\x01",
            "和黑月事件而忙得不可开交了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "你们在进行调查时，\x01",
            "一定要尽量隐秘，\x01",
            "给我注意不要让帝国派发现了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F3")

    SetChrSubChip(0xFE, 0x2)
    TalkEnd(0xFE)

    label("loc_11FA")

    Return()

    # Function_7_964 end

    def Function_8_11FB(): pass

    label("Function_8_11FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128D")

    #C0047
    ChrTalk(
        0xFE,
        (
            "听说预算会议已经结束了呢，\x01",
            "这样的话，父亲也能提早回来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "……真没办法……\x01",
            "我就勉为其难地陪他共进晚餐吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12F4")

    label("loc_128D")


    #C0049
    ChrTalk(
        0xFE,
        (
            "……这次可不是因为\x01",
            "他要求我这么做，\x01",
            "只是我正好有心情而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "因为，我心里也不是真的\x01",
            "讨厌父亲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F4")

    Jump("loc_1519")

    label("loc_12F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1389")

    #C0051
    ChrTalk(
        0xFE,
        (
            "今天我准备和玛夏\x01",
            "一起去购物。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "呵呵……父亲他也\x01",
            "不再啰啰嗦嗦了，\x01",
            "感觉变得好自由呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "这都是多亏了各位。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_13E6")

    label("loc_1389")


    #C0054
    ChrTalk(
        0xFE,
        (
            "今天我准备和玛夏\x01",
            "一起去购物。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "呵呵……父亲他也\x01",
            "不再啰啰嗦嗦了，\x01",
            "感觉变得好自由呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E6")

    Jump("loc_1519")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")

    #C0056
    ChrTalk(
        0xFE,
        "果然还是自己家最好了。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……艾莉小姐，还有各位，\x01",
            "今天真是受你们多方照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0100F请不必在意。\x01",
            "比起那个……请你平时\x01",
            "多和令尊沟通沟通吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "嗯，放心吧，没问题了，\x01",
            "因为我已经有了自信。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1519")

    label("loc_14CE")


    #C0060
    ChrTalk(
        0xFE,
        (
            "……艾莉小姐，还有各位，\x01",
            "今天真是受你们多方照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "请再来玩哦。\x02",
    )

    CloseMessageWindow()

    label("loc_1519")

    TalkEnd(0xFE)
    Return()

    # Function_8_11FB end

    def Function_9_151D(): pass

    label("Function_9_151D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1576")

    #C0062
    ChrTalk(
        0xFE,
        (
            "今晚准备了\x01",
            "豪华的晚餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "呵呵……如果小姐和老爷\x01",
            "能高兴就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A1")

    label("loc_1576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_162B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_15E3")

    #C0064
    ChrTalk(
        0xFE,
        (
            "小姐她，露出了\x01",
            "很灿烂的笑容呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "呵呵……我很期待今天\x01",
            "和小姐一起去购物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1626")

    label("loc_15E3")


    #C0066
    ChrTalk(
        0xFE,
        "……小姐她…………\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "离家出走后就孤身一人……\x01",
            "不要紧吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1626")

    Jump("loc_17A1")

    label("loc_162B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_17A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_1757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171F")

    #C0068
    ChrTalk(
        0xFE,
        (
            "各位，我真的不知道\x01",
            "该如何感谢你们才好……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "果然还是应该找各位商量呀，\x01",
            "幸好当时没有盲目服从小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0000F如果发生什么的话，欢迎再来\x01",
            "找我们『特别任务支援科』商谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "好、好的。\x01",
            "一定会的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1752")

    label("loc_171F")


    #C0072
    ChrTalk(
        0xFE,
        (
            "各位，真的非常感谢。\x01",
            "我真庆幸自己拿出了勇气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1752")

    Jump("loc_17A1")

    label("loc_1757")


    #C0073
    ChrTalk(
        0xFE,
        (
            "今天将工作都\x01",
            "搁下了……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "……如果不快点准备，\x01",
            "就来不及做饭了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A1")

    TalkEnd(0xFE)
    Return()

    # Function_9_151D end

    def Function_10_17A5(): pass

    label("Function_10_17A5")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(440, 1000, 42830, 0)
    MoveCamera(54, 20, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(22640, 0)
    SetChrPos(0x101, 500, 0, 40660, 0)
    SetChrPos(0x102, -500, 0, 40660, 0)
    SetChrPos(0x103, -500, 60, 39200, 0)
    SetChrPos(0x104, 500, 60, 39200, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0075
    ChrTalk(
        0x8,
        "#5P可恶，竟然给我惹出这种麻烦……！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "#11P但是议员，我们必须\x01",
            "快点制定对策……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个，抱歉打扰了，\x01",
            "我们是因为支援请求前来拜访的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    SetChrSubChip(0xA, 0x1)
    Fade(300)
    SetChrPos(0xA, 1900, 60, 43630, 270)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_95(0xA, 2029, 60, 42410, 1000, 0x0)
    OP_93(0xA, 0xE1, 0x190)

    #C0078
    ChrTalk(
        0xA,
        "#5P是警察局的那个什么什么科吧？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "#5P太好了，现在我们可是\x01",
            "束手无策了！\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "#5P哎呀，等一下……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5P那边那位不是麦克道尔\x01",
            "市长家的艾莉吗，\x01",
            "为什么你也会与他们同行呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        (
            "#12P#0103F久疏问候，议员。\x02\x03",

            "#0100F那个……我现在\x01",
            "正在警察系统工作，\x01",
            "今天是作为一名警官前来拜访的。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "#5P是、是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#5P唔唔，算了，市长是中立派，\x01",
            "应该没什么大问题吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)
    Sleep(300)

    #C0085
    ChrTalk(
        0xA,
        (
            "#11P但是议员，帝国派的家伙\x01",
            "都很卑鄙狡猾，\x01",
            "如果不小心被他们知道了……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#12P#0300F（……以大小姐的立场来说，\x01",
            "  很容易演变为政治问题呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#12P#0106F（跟议员先生们说话\x01",
            "  还真累……）\x02\x03",

            "#0101F那个，议员先生，能请您\x01",
            "将可以透露的部分告诉我们吗？\x02\x03",

            "而且您看上去似乎\x01",
            "也很困扰……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#12P#0200F支援请求的内容\x01",
            "好像是『重要人士的搜索委托』吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    #C0089
    ChrTalk(
        0x8,
        (
            "#5P是、是啊，\x01",
            "其实发生了一件棘手的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "#5P……事到如今也没办法了，\x01",
            "我就将情况全部说明一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "#5P但是有件事我先说在前面，\x01",
            "这是涉及到政治决定的重要案件。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#5P我们共和国派也\x01",
            "陷入了困难的局面……\x01",
            "所以绝对不可以将这件事泄露出去！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0001F知道了，\x01",
            "我们保证不会泄露。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#12P#0100F我们发誓绝不会做\x01",
            "对您不利的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        "#5P好，那么我就告诉你们吧。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#5P……实际上，我们共和派的\x01",
            "某个人物突然失踪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x103,
        "#12P#0205F失踪了……？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#5P是我的女儿。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#5P她好像带着女仆\x01",
            "离家出走了。\x02",
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
    Sleep(1200)

    #C0100
    ChrTalk(
        0x104,
        (
            "#12P#0306F（卖了这么大的关子，\x01",
            "  结果只是女儿离家出走啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        (
            "#12P#0101F令千金……就是卡拉小姐吧？\x01",
            "我曾经与她一起\x01",
            "在主日学校上过课。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "#5P哎呀，是吗。\x01",
            "……议员他与小姐的关系\x01",
            "并不是很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#5P一直以来，\x01",
            "就争执不断呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        "#5P但是现在时机实在不好……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#5P我们的后盾黑月\x01",
            "似乎在今日凌晨遭到了袭击。\x01",
            "我们这边为了应付这件事，已经是精疲力尽了……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "#5P哼，这个蠢女儿。\x01",
            "现在这么忙，我根本就\x01",
            "没空管她。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "#5P而且最近黑手党之间的斗争\x01",
            "似乎也激烈化了……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#5P跟女仆两人四处游荡，\x01",
            "该有多大危险啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#12P#0003F原来如此，您果然\x01",
            "是在担心令千金的安危。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "#5P……而且，这件事要是泄露出去的话，\x01",
            "帝国派的家伙们就会\x01",
            "把它当成攻击材料吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#5P议会还是混战一片的局面，\x01",
            "这种时候更要避免这种丑闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "#5P你们几个，无论如何都要\x01",
            "将她秘密带回。\x02",
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
    Sleep(1200)

    #C0113
    ChrTalk(
        0x103,
        "#12P#0203F（结果在意的还是公众影响啊……）\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#12P#0306F（思考方式还真是有大人物的风格。）\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x102,
        "#12P#0103F（虽然已经预料到了……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_22B8():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22B8)
    Sleep(50)

    def lambda_22C8():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C8)

    def lambda_22D5():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22D5)

    def lambda_22E2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22E2)
    Sleep(400)

    #C0116
    ChrTalk(
        0x102,
        (
            "#6P#0101F这种情况确实很令人担心……\x01",
            "而且我觉得卡拉小姐被\x01",
            "卷入什么事件的可能性也不低。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#12P#0003F是啊……\x02",
    )

    CloseMessageWindow()

    def lambda_2365():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2365)

    def lambda_2372():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2372)

    def lambda_237F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_237F)

    def lambda_238C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_238C)
    Sleep(400)

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#0001F知道了，\x01",
            "就由我们来寻找令千金吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        "#5P哦哦，太好了！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        "#5P尽快把她给我带回来。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#12P#0003F虽然我们没法确保一定能做到那点……\x02\x03",

            "#0001F但我们会尽力查明\x01",
            "令千金的行踪，\x01",
            "并保障她的安全的。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#5P哎，没办法。\x01",
            "只要找到她在哪，之后也就好办了……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        "#5P就给我按照那个方针去办吧。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "#5P小姐似乎在自己的房间里\x01",
            "留了字条。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "#5P如果要进行调查，\x01",
            "可以将那个当成线索。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2520():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2520)

    def lambda_252D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_252D)

    def lambda_253A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_253A)

    def lambda_2547():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2547)
    Sleep(300)

    #C0126
    ChrTalk(
        0x102,
        (
            "#12P#0101F知道了，\x01",
            "那就请允许我们前去查看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【重要人士的搜索委托】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 30, 0, 40130, 180)
    SetChrPos(0xA, 2300, 250, 43630, 270)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x2)
    OP_29(0x2D, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_17A5 end

    def Function_11_2623(): pass

    label("Function_11_2623")

    EventBegin(0x0)
    Fade(800)
    OP_68(44280, 1560, 2580, 0)
    MoveCamera(56, 25, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(21530, 0)
    SetChrPos(0x101, 44280, 60, 2500, 135)
    SetChrPos(0x102, 45340, 60, 3250, 135)
    SetChrPos(0x103, 43820, 60, 3620, 135)
    SetChrPos(0x104, 44820, 60, 4220, 135)
    OP_0D()

    #C0128
    ChrTalk(
        0x101,
        (
            "#12P#0005F似乎在笔记本上\x01",
            "写了留言呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x102, 45710, 60, 2120, 1000, 0x0)
    OP_93(0x102, 0x5A, 0x190)

    #C0129
    ChrTalk(
        0x102,
        (
            "#11P#0103F我看看……\x02\x03",

            "『我已经受够了，\x01",
            "  父亲您爱怎么样就怎么样吧。』\x02\x03",

            "『我也要按自己的想法行事！\x01",
            "  　卡拉』。\x02\x03",

            "『ＰＳ：女仆我也带走了，\x01",
            "  您就为了没法准备食物\x01",
            "  而苦恼吧！』\x02",
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
    Sleep(1200)

    #C0130
    ChrTalk(
        0x101,
        "#12P#0006F该怎么说呢……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#5P#0306F虽然父亲是那样，\x01",
            "但这个女儿也相当任性呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x190)
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    #C0132
    ChrTalk(
        0x102,
        (
            "#11P#0108F坎贝尔议员是那种\x01",
            "为了工作不顾家庭的类型呢。\x02\x03",

            "说起来，卡拉小姐从以前开始\x01",
            "就一直在抱怨自己的父亲……\x02\x03",

            "#0103F我想只要有一条导火索，\x01",
            "她离家出走也不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#6P#0203F但是她似乎并没有\x01",
            "写明那条导火索呢。\x02\x03",

            "#0200F从留言上只能看出，\x01",
            "她是以自己的意志离家出走的。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#12P#0000F是啊……\x01",
            "从内容上来看，可以知道这是……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【突发性的离家出走】\x01",      # 0
            "【有计划的离家出走】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B10")
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    #C0135
    ChrTalk(
        0x101,
        (
            "#12P#0003F应该是比较突然的离家出走吧。\x02\x03",

            "就像艾莉所说的那样，\x01",
            "应该有条导火索的……\x02\x03",

            "#0001F然后她一生气，\x01",
            "就奔出家门了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        "#6P#0200F原来如此，就是那种感觉。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#5P#0300F如果早有计划，\x01",
            "留言中应该会涉及更多\x01",
            "各种各样的怨言吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 1)
    Jump("loc_2C38")

    label("loc_2B10")


    #C0138
    ChrTalk(
        0x101,
        "#12P#0003F是早有计划的吧……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    #C0139
    ChrTalk(
        0x104,
        (
            "#5P#0305F如果早有计划，留言中应该会\x01",
            "写有更多各种各样的抱怨吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#6P#0200F如果是那样，为了传达自己\x01",
            "想要反抗的意志，内容应该会\x01",
            "更加条理分明，字迹工整呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Sleep(300)

    #C0141
    ChrTalk(
        0x101,
        (
            "#12P#0006F是、是吗……\x02\x03",

            "看这种潦草的字迹，也许\x01",
            "应该是突发性的离家出走吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C38")


    #C0142
    ChrTalk(
        0x102,
        (
            "#11P#0101F她是什么时候\x01",
            "离家出走的呢？\x02\x03",

            "#0108F希望她\x01",
            "还没走远……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D5E")
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    #C0143
    ChrTalk(
        0x101,
        (
            "#12P#0003F从字条的内容上\x01",
            "是看不出来的呢。\x02\x03",

            "#0001F先问一下议员\x01",
            "他们两人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        "#5P#0300F好，去确认一下吧。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x103,
        (
            "#6P#0200F是啊，确认完毕之后\x01",
            "再回到这里吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 45270, 60, 2680, 152)
    OP_29(0x2D, 0x1, 0x4)
    EventEnd(0x5)
    Jump("loc_2D6C")

    label("loc_2D5E")

    TurnDirection(0x101, 0x102, 400)
    Sleep(300)
    Call(0, 12)
    Return()

    label("loc_2D6C")

    Return()

    # Function_11_2623 end

    def Function_12_2D6D(): pass

    label("Function_12_2D6D")


    #C0146
    ChrTalk(
        0x101,
        (
            "#12P#0003F……我想想。\x01",
            "从刚才议员他们\x01",
            "所说的内容来看，时间应该是……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【昨天】\x01",              # 0
            "【今天中午之前】\x01",      # 1
            "【就在刚才】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0147
    ChrTalk(
        0x102,
        (
            "#11P#0103F早餐时还在，\x01",
            "但过了中午之后就不在了……\x02\x03",

            "#0101F出走时间无疑就是\x01",
            "今天上午了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCE")

    label("loc_2E8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F37")

    #C0148
    ChrTalk(
        0x102,
        (
            "#11P#0105F咦，但据说她今天早上\x01",
            "还出来吃了早餐……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#12P#0006F弄错了……\x01",
            "似乎是过了中午才注意到她不见了的，\x01",
            "那么出走时间就应该是今天上午了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCE")

    label("loc_2F37")


    #C0150
    ChrTalk(
        0x102,
        (
            "#11P#0105F咦，但议员他们好像在中午\x01",
            "就已经发现卡拉小姐不见了……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0006F弄错了……\x01",
            "今天早餐时她似乎还在，\x01",
            "那么出走时间就应该是今天上午了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCE")


    #C0152
    ChrTalk(
        0x103,
        "#6P#0200F似乎还追得上。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#5P#0301F问题是她去了哪里。\x02\x03",

            "#0303F要从这位离家出走的小姐\x01",
            "的交友关系上推测一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    #C0154
    ChrTalk(
        0x101,
        (
            "#12P#0003F不，那就太浪费时间了。\x02\x03",

            "#0001F而且，从目前的状况来看，\x01",
            "应该能够十拿九稳地推测出\x01",
            "她最有可能会去的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0155
    ChrTalk(
        0x101,
        (
            "#12P#0000F突发性的决定，\x01",
            "加上今天上午刚刚离开。\x02\x03",

            "她可能会去的地方是……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【大圣堂】\x01",      # 0
            "【市政厅】\x01",      # 1
            "【ＩＢＣ】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3308")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0156
    ChrTalk(
        0x101,
        "#12P#0000F应该是ＩＢＣ吧。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#5P#0300F原来如此……是去\x01",
            "确保眼下离家出走的资金了啊。\x02\x03",

            "从某种意义上来说，\x01",
            "是离家出走的常见套路呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#11P#0100F而且如果是突发性的离家出走，\x01",
            "身上应该也不会有多少现金吧。\x01",
            "很有可能是去ＩＢＣ呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#6P#0200F那我们就去ＩＢＣ吧，\x01",
            "她也许还在那里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#12P#0000F是啊，尽量加快脚步吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_35AA")

    label("loc_3308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339E")

    #C0161
    ChrTalk(
        0x101,
        (
            "#12P#0000F是大圣堂吗？\x02\x03",

            "信仰坚定的人\x01",
            "是有可能会去那里的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#11P#0108F是啊……但我想卡拉小姐\x01",
            "对教会的信仰并不是很坚定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342C")

    label("loc_339E")


    #C0163
    ChrTalk(
        0x101,
        (
            "#12P#0000F是市政厅吗？\x02\x03",

            "比如说，果断去提交了\x01",
            "迁居申请之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        (
            "#11P#0108F是啊……但我怀疑突然奔出家门\x01",
            "的卡拉小姐会不会有那么冷静……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342C")

    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x103,
        (
            "#6P#0203F因为是突发性的离家出走，\x02\x03",

            "#0200F所以身上现金不多的\x01",
            "可能性也很高吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_34D1():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D1)

    def lambda_34DE():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34DE)

    def lambda_34EB():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34EB)
    Sleep(300)

    #C0166
    ChrTalk(
        0x101,
        (
            "#12P#0005F是吗，是去ＩＢＣ\x01",
            "取离家出走的资金了吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#5P#0303F这么一想，\x01",
            "的确是离家出走的常见套路呢。\x02\x03",

            "#0300F好，就去一趟ＩＢＣ吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        (
            "#11P#0100F嗯，尽量\x01",
            "加快脚步吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C2")
    OP_2C(0x2D, 0x2)

    label("loc_35C2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 45270, 60, 2680, 152)
    OP_29(0x2D, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_2D6D end

    def Function_13_35EA(): pass

    label("Function_13_35EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_370F")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『我已经受够了，\x01",
            "  父亲您爱怎么样就怎么样吧。\x01",
            "　我也要按自己的想法行事！\x01",
            "  　　　　　　　　  卡拉　』\x02",
        )
    )

    CloseMessageWindow()

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『ＰＳ：女仆我也带走了，\x01",
            "  您就为了没法准备食物\x01",
            "  而苦恼吧！』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_37F6")

    label("loc_370F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_37F3")
    EventBegin(0x0)
    Fade(800)
    OP_68(44280, 1560, 2580, 0)
    MoveCamera(56, 25, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(21530, 0)
    SetChrPos(0x101, 44280, 60, 2500, 0)
    SetChrPos(0x102, 45340, 60, 3250, 270)
    SetChrPos(0x103, 43820, 60, 3620, 90)
    SetChrPos(0x104, 44820, 60, 4220, 180)
    OP_0D()

    #C0171
    ChrTalk(
        0x102,
        (
            "#11P#0108F卡拉小姐，\x01",
            "到底是什么时候\x01",
            "离家出走的呢？\x02\x03",

            "#0103F希望她还\x01",
            "没有走远……\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_37F6")

    label("loc_37F3")

    Call(0, 11)

    label("loc_37F6")

    Return()

    label("loc_37F7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『我已经受够了，\x01",
            "  父亲您爱怎么样就怎么样吧。\x01",
            "　我也要按自己的想法行事！\x01",
            "  　　　　　　　　　卡拉　』\x02",
        )
    )

    CloseMessageWindow()

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『ＰＳ：女仆我也带走了，\x01",
            "  您就为了没法准备食物\x01",
            "  而苦恼吧！』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_13_35EA end

    SaveToFile()

Try(main)
