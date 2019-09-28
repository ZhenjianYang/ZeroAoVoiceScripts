from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t210d.bin",                # FileName
        "t210d",                    # MapName
        "t210d",                    # Location
        0x0059,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t210d",                  # 0
        "索妮亚司令",             # 1
        "士兵布鲁德",             # 2
        "士兵达利亚",             # 3
        "游客",                   # 4
    ))

    AddCharChip((
        "chr/ch12200.itc",                   # 00
        "chr/ch41400.itc",                   # 01
        "chr/ch41800.itc",                   # 02
        "chr/ch33000.itc",                   # 03
    ))

    DeclNpc(-10000,  10000,   0,       270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-13829,  10000,   -2960,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-14060,  10000,   2900,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-18600,  5000,    -17170,  270,  389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(348, 0)                                        # 0

    ScpFunction((
        "Function_0_15C",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_25C",          # 03, 3
        "Function_4_397",          # 04, 4
        "Function_5_539",          # 05, 5
        "Function_6_6A8",          # 06, 6
        "Function_7_798",          # 07, 7
        "Function_8_8C1",          # 08, 8
    ))


    def Function_0_15C(): pass

    label("Function_0_15C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
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

    # Function_0_15C end

    def Function_1_20C(): pass

    label("Function_1_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)

    label("loc_21A")

    Return()

    # Function_1_20C end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_22D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_244")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257")
    OP_70(0x2, 0x0)
    Jump("loc_25B")

    label("loc_257")

    OP_70(0x2, 0x1E)

    label("loc_25B")

    Return()

    # Function_2_21B end

    def Function_3_25C(): pass

    label("Function_3_25C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('回复药', 1)"), scpexpr(EXPR_END)), "loc_2DF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_349")

    label("loc_2DF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_349")

    Jump("loc_38B")

    label("loc_34E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_38B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_25C end

    def Function_4_397(): pass

    label("Function_4_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5")
    Call(0, 8)
    Return()

    label("loc_3A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C1")

    #C0004
    ChrTalk(
        0x8,
        (
            "#10600F道格拉斯副司令去找\x01",
            "麦克道尔议长商量\x01",
            "今后的应对措施了。\x02\x03",

            "我身为正规军的司令官，\x01",
            "必须要确保万全的警备体制，\x01",
            "随时警戒来自帝国和共和国的威胁。\x02\x03",

            "#10603F其实等到一切都结束之后，\x01",
            "我也不知该如何抉择……\x02\x03",

            "#10600F但现在，我至少要尽\x01",
            "最大努力，履行司令官的职责。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_535")

    label("loc_4C1")


    #C0005
    ChrTalk(
        0x8,
        (
            "#10603F其实等到一切都结束之后，\x01",
            "我也不知该如何抉择……\x02\x03",

            "#10600F但现在，我至少要尽\x01",
            "最大努力，履行司令官的职责。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_535")

    TalkEnd(0xFE)
    Return()

    # Function_4_397 end

    def Function_5_539(): pass

    label("Function_5_539")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A")

    #C0006
    ChrTalk(
        0x9,
        (
            "据说帝国在内战过程中\x01",
            "仍在开发一种叫做\x01",
            "『飞行军舰』的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "帝国军的机甲师团如果\x01",
            "再加上那种东西，\x01",
            "老实说，我们实在是无力抵御……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "如果『神机』还在就好了……\x01",
            "会这样想的人\x01",
            "难道只有我一个吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6A4")

    label("loc_61A")


    #C0009
    ChrTalk(
        0x9,
        (
            "机甲师团如果再加上\x01",
            "『飞行军舰』……\x01",
            "帝国军完全不是我们可以抵御的。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "如果『神机』还在就好了……\x01",
            "会这样想的人\x01",
            "难道只有我一个吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A4")

    TalkEnd(0xFE)
    Return()

    # Function_5_539 end

    def Function_6_6A8(): pass

    label("Function_6_6A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71E")

    #C0011
    ChrTalk(
        0xA,
        (
            "我认为失去『神机』\x01",
            "是一件好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "那种兵器具有如此惊人的威力，\x01",
            "完全不是我们\x01",
            "可以掌控的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_794")

    label("loc_71E")


    #C0013
    ChrTalk(
        0xA,
        (
            "『神机』……那种东西\x01",
            "无论如何也不是我们可以掌控的。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        (
            "……看到卡雷利亚要塞的惨状之后，\x01",
            "我直到现在都后背发冷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_794")

    TalkEnd(0xFE)
    Return()

    # Function_6_6A8 end

    def Function_7_798(): pass

    label("Function_7_798")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_853")

    #C0015
    ChrTalk(
        0xB,
        (
            "我本想尝试返回帝国，\x01",
            "因此来到了贝尔加德门……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "没、没想到『卡雷利亚要塞』\x01",
            "竟然变成那种样子了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "如、如此说来，\x01",
            "我无论如何也不可能回去了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8BD")

    label("loc_853")


    #C0018
    ChrTalk(
        0xB,
        (
            "没、没想到『卡雷利亚要塞』\x01",
            "竟然变成那种样子了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "如、如此说来，\x01",
            "我无论如何也不可能回去了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD")

    TalkEnd(0xFE)
    Return()

    # Function_7_798 end

    def Function_8_8C1(): pass

    label("Function_8_8C1")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    SetChrPos(0x101, -8000, 10000, 500, 270)
    SetChrPos(0x102, -7900, 10000, -500, 270)
    SetChrPos(0x103, -7000, 10000, 1400, 270)
    SetChrPos(0x104, -6800, 10000, -1500, 270)
    SetChrPos(0xF4, -6000, 10000, 500, 270)
    SetChrPos(0xF5, -5800, 10000, -500, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0020
    ChrTalk(
        0x101,
        (
            "#12P#00002F索妮亚司令……\x01",
            "您在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    #C0021
    ChrTalk(
        0x8,
        "#10605F#5P是你们……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-68290, 12670, -3030, 0)
    MoveCamera(239, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(127990, 0)
    OP_0D()
    MoveCamera(303, 17, 0, 40000)
    Sleep(1000)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0022
    AnonymousTalk(
        0x104,
        (
            "#00301F……真是惊人的景象啊。\x02\x03",

            "#00303F我们当时也从影像中\x01",
            "看到那白色智能兵器使列车炮\x01",
            "瞬间消失的场面了……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0023
    AnonymousTalk(
        0x101,
        (
            "#00008F……虽说是间接的，\x01",
            "但琪雅的力量竟然\x01",
            "造成了这种状况……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0024
    AnonymousTalk(
        0x8,
        (
            "#10603F……我从帝国方面\x01",
            "得到了一条\x01",
            "未经确认的情报……\x02\x03",

            "#10600F据说『神机』的攻击\x01",
            "几乎没有对帝国军\x01",
            "造成人员伤亡。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0025
    AnonymousTalk(
        0x101,
        "#12P#00005F真、真的吗！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #A0026
    AnonymousTalk(
        0x102,
        (
            "#12P#00105F在、在那种状况下竟能有如此结果，\x01",
            "这也只能称之为奇迹了……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0027
    AnonymousTalk(
        0x8,
        (
            "#10600F如今无法确认事态，\x01",
            "因此并不清楚实际情况是怎样的……\x02\x03",

            "#10604F据我推测，那也许是一种\x01",
            "只会使无机物消失，却不会将\x01",
            "人类卷入的力量呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0028
    AnonymousTalk(
        0x103,
        (
            "#12P#00202F如果真是如此，\x01",
            "那或许是琪雅无意识的干涉\x01",
            "造成了奇迹呢。\x02\x03",

            "#00204F虽然帝国肯定遭受到了\x01",
            "巨大的损失……\x01",
            "但我们至少可以稍微松一口气了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    OP_0D()

    #C0029
    ChrTalk(
        0x8,
        (
            "#10604F#5P……我已经听说了。\x02\x03",

            "#10602F解放克洛斯贝尔市的作战\x01",
            "似乎相当成功啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        "#12P#00309F哈哈，老实说，成功得都有些过头了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2A")

    #C0031
    ChrTalk(
        0x109,
        (
            "#12P#10104F这多亏有索妮亚司令相助！\x02\x03",

            "#10102F正是因为受您那番话的启发，\x01",
            "我们才能想到发表\x01",
            "独立无效宣言这条道路！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F31")

    label("loc_E2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EB5")

    #C0032
    ChrTalk(
        0x105,
        (
            "#12P#10400F呵呵，这多亏有司令相助啊。\x02\x03",

            "#10404F正是由于受您那番话的启发，\x01",
            "我们才能想到发表\x01",
            "独立无效宣言这条道路。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F31")

    label("loc_EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F31")

    #C0033
    ChrTalk(
        0x106,
        (
            "#12P#10704F这多亏有您相助。\x02\x03",

            "#10702F正是由于受您那番话的启发，\x01",
            "我们才能想到发表\x01",
            "独立无效宣言这条道路。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F31")


    #C0034
    ChrTalk(
        0x8,
        (
            "#10602F#5P呵呵，我什么都没有做呀。\x01",
            "这一切都是你们努力的成果……\x02\x03",

            "#10603F……我所做的，\x01",
            "只是遵照总统的方针\x01",
            "来指挥国防军而已。\x02\x03",

            "#10608F现如今，独立国已经失去了正当性，\x01",
            "我这种人恐怕也没资格\x01",
            "继续当司令了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        "#12P#00011F这、这……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10DC")

    #C0036
    ChrTalk(
        0x10A,
        (
            "#12P#00606F……我认为你没必要\x01",
            "自责到这种地步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_10DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_111F")

    #C0037
    ChrTalk(
        0x105,
        (
            "#12P#10406F……没必要自责\x01",
            "到这种程度吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_111F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_116B")

    #C0038
    ChrTalk(
        0x109,
        (
            "#12P#10113F您、您并没有自责\x01",
            "到这种地步的必要吧……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116B")


    #C0039
    ChrTalk(
        0x8,
        (
            "#10602F#5P呵呵，我很清楚\x01",
            "自己现在应该做什么。\x02\x03",

            "#10604F等到一切都结束之后，\x01",
            "我也不知该如何抉择……\x02\x03",

            "#10600F但现在，我至少要尽\x01",
            "最大努力，履行司令官的职责。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1AC, 0)
    EventEnd(0x5)
    Return()

    # Function_8_8C1 end

    SaveToFile()

Try(main)
