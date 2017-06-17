from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c015b.bin",                # FileName
        "c015b",                    # MapName
        "c015b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c015b",                  # 0
        "霍伊斯托夫",             # 1
        "布拉温",                 # 2
        "赛尔缇欧",               # 3
        "侬诺",                   # 4
        "弗罗缇",                 # 5
        "市民",                   # 6
        "市民",                   # 7
        "女公关",                 # 8
        "商务人士",               # 9
        "基隆德",                 # 10
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch20302.itc",                   # 07
        "chr/ch43402.itc",                   # 08
        "chr/ch27802.itc",                   # 09
    ))

    DeclNpc(-509,    0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-52029,  0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-8880,   0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  325,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4460,    150,     5829,    180,  453,  0x0, 0,   6,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6679,    150,     3630,    270,  453,  0x0, 0,   7,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-1649,   5150,    17649,   180,  453,  0x0, 0,   8,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-1649,   5150,    13439,   0,    453,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  4,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  6,  0x0000)

    ChipFrameInfo(604, 0)                                        # 0

    ScpFunction((
        "Function_0_25C",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_3B1",          # 02, 2
        "Function_3_453",          # 03, 3
        "Function_4_454",          # 04, 4
        "Function_5_458",          # 05, 5
        "Function_6_6A9",          # 06, 6
        "Function_7_6AD",          # 07, 7
        "Function_8_84E",          # 08, 8
        "Function_9_88B",          # 09, 9
        "Function_10_90F",         # 0A, 10
        "Function_11_96C",         # 0B, 11
        "Function_12_9F9",         # 0C, 12
        "Function_13_A74",         # 0D, 13
        "Function_14_AEA",         # 0E, 14
        "Function_15_B3E",         # 0F, 15
    ))


    def Function_0_25C(): pass

    label("Function_0_25C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_29C"),
        (1, "loc_2A8"),
        (2, "loc_2B4"),
        (3, "loc_2C0"),
        (4, "loc_2CC"),
        (5, "loc_2D8"),
        (6, "loc_2E4"),
        (SWITCH_DEFAULT, "loc_2F0"),
    )


    label("loc_29C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2A8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2B4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2C0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2CC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2D8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_313")

    Return()

    # Function_0_25C end

    def Function_1_314(): pass

    label("Function_1_314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B0")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_314")

    label("loc_3B0")

    Return()

    # Function_1_314 end

    def Function_2_3B1(): pass

    label("Function_2_3B1")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    Return()

    # Function_2_3B1 end

    def Function_3_453(): pass

    label("Function_3_453")

    Return()

    # Function_3_453 end

    def Function_4_454(): pass

    label("Function_4_454")

    Call(0, 5)
    Return()

    # Function_4_454 end

    def Function_5_458(): pass

    label("Function_5_458")

    TalkBegin(0x11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D4")
    OP_AF(0x4)
    Jump("loc_506")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E4")
    OP_AF(0x3)
    Jump("loc_506")

    label("loc_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F4")
    OP_AF(0x2)
    Jump("loc_506")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_504")
    OP_AF(0x1)
    Jump("loc_506")

    label("loc_504")

    OP_AF(0x0)

    label("loc_506")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A0")

    label("loc_515")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_529")
    Jump("loc_6A0")

    label("loc_529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649")

    #C0001
    ChrTalk(
        0x11,
        (
            "哟，这不是达德利嘛。在和支援科\x01",
            "的人一起散步？关系真好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        (
            "#00603F不，只是有些让人比较在意的事情。\x02\x03",

            "#00600F光靠这几个家伙实在是不放心，\x01",
            "所以我要与他们同行。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x11,
        "嘿，你还是老样子啊。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x11,
        (
            "好啦，我马上就要关店了，\x01",
            "如果想买东西就赶快吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6A0")

    label("loc_649")


    #C0005
    ChrTalk(
        0x11,
        (
            "我差不多也该关店了，\x01",
            "如果想买东西就赶快吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x11,
        "我还想早点收工，好好喝上一杯呢。\x02",
    )

    CloseMessageWindow()

    label("loc_6A0")

    Jump("loc_465")

    label("loc_6A5")

    TalkEnd(0x11)
    Return()

    # Function_5_458 end

    def Function_6_6A9(): pass

    label("Function_6_6A9")

    Call(0, 7)
    Return()

    # Function_6_6A9 end

    def Function_7_6AD(): pass

    label("Function_7_6AD")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_70A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_729")
    OP_AF(0x9)
    Jump("loc_72B")

    label("loc_729")

    OP_AF(0x8)

    label("loc_72B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_845")

    label("loc_73A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_845")

    label("loc_74E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_845")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F7")

    #C0007
    ChrTalk(
        0x8,
        (
            "我听布拉温说了，\x01",
            "侬诺似乎很有\x01",
            "烹饪的天赋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "当初只是想让她\x01",
            "帮忙做点简单的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "嗯，这可真是\x01",
            "预料之外的收获。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_845")

    label("loc_7F7")


    #C0010
    ChrTalk(
        0x8,
        (
            "当初只是想让侬诺\x01",
            "帮忙做点简单的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "嗯，这可真是\x01",
            "预料之外的收获。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_845")

    Jump("loc_6BA")

    label("loc_84A")

    TalkEnd(0x8)
    Return()

    # Function_7_6AD end

    def Function_8_84E(): pass

    label("Function_8_84E")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        (
            "好，索性就下定决心，\x01",
            "明天把料理工作\x01",
            "交给侬诺吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_84E end

    def Function_9_88B(): pass

    label("Function_9_88B")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        (
            "虽然我一点都不在乎……\x01",
            "但侬诺那家伙不知从何时开始，\x01",
            "兼任起料理的准备工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "难道说，她会就此转职为\x01",
            "正式厨师吗……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_88B end

    def Function_10_90F(): pass

    label("Function_10_90F")

    TalkBegin(0xFE)

    #C0015
    ChrTalk(
        0xFE,
        (
            "准备工作结束之后，\x01",
            "就该去洗盘子了，然后还有……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "呼……晚餐时间\x01",
            "果然很忙啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_90F end

    def Function_11_96C(): pass

    label("Function_11_96C")

    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "呼，今天看书看得太投入，不知不觉\x01",
            "就待到天都黑了，已经好久没有这样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "真是有点对不起店里的人，\x01",
            "不然就在这里把晚饭也吃了吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_96C end

    def Function_12_9F9(): pass

    label("Function_12_9F9")

    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0xFE,
        (
            "我们两个女人今天都把家人\x01",
            "丢在一旁，相约来这里用餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "偶尔也要享受一下这样的生活。\x01",
            "主妇的工作也是很辛苦的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_9F9 end

    def Function_13_A74(): pass

    label("Function_13_A74")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "尽情享用喜欢的美食，并痛痛快快地聊天畅谈……\x01",
            "这就是我们缓解压力的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "好，今天一定要尽情享受哦～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_A74 end

    def Function_14_AEA(): pass

    label("Function_14_AEA")

    TalkBegin(0xFE)

    #C0023
    ChrTalk(
        0xFE,
        (
            "呵呵，真是老土的台词，\x01",
            "但我并不讨厌哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "我好像……已经有些醉了呢⊥\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_AEA end

    def Function_15_B3E(): pass

    label("Function_15_B3E")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        (
            "为你美丽的眼眸干杯，\x01",
            "今晚一定会是个很特别的夜晚呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_B3E end

    SaveToFile()

Try(main)
