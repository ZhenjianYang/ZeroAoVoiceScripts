from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t2020.bin",                # FileName
        "t2020",                    # MapName
        "t2020",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2020",                  # 0
        "米蕾优准尉",             # 1
        "布鲁德队员",             # 2
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch23000.itc",                   # 02
    ))

    DeclNpc(-1309,   0,       42250,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(40889,   0,       -30579,  315,  261,  0x0, 0,   1,   0,   0,   2,   0,   8,   255,  0)

    ScpFunction((
        "Function_0_10C",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_24D",          # 02, 2
        "Function_3_278",          # 03, 3
        "Function_4_351",          # 04, 4
        "Function_5_352",          # 05, 5
        "Function_6_4E8",          # 06, 6
        "Function_7_1AFD",         # 07, 7
        "Function_8_1CAC",         # 08, 8
        "Function_9_1FA9",         # 09, 9
        "Function_10_20AC",        # 0A, 10
        "Function_11_3116",        # 0B, 11
        "Function_12_382C",        # 0C, 12
    ))


    def Function_0_10C(): pass

    label("Function_0_10C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_14C"),
        (1, "loc_158"),
        (2, "loc_164"),
        (3, "loc_170"),
        (4, "loc_17C"),
        (5, "loc_188"),
        (6, "loc_194"),
        (SWITCH_DEFAULT, "loc_1A0"),
    )


    label("loc_14C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_158")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_164")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_170")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_17C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_188")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_194")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1C3")

    Return()

    # Function_0_10C end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24C")
    OP_95(0xFE, -890, 0, 5100, 2000, 0x0)
    OP_95(0xFE, 12780, 0, 5100, 2000, 0x0)
    OP_95(0xFE, 12780, 0, 3300, 2000, 0x0)
    OP_95(0xFE, 860, 0, 3300, 2000, 0x0)
    OP_95(0xFE, 860, 0, -10930, 2000, 0x0)
    OP_95(0xFE, -890, 0, -10930, 2000, 0x0)
    Jump("Function_1_1C4")

    label("loc_24C")

    Return()

    # Function_1_1C4 end

    def Function_2_24D(): pass

    label("Function_2_24D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_94(0xFE, 0x99A2, 0xFFFF838C, 0xA4BA, 0xFFFF8E40, 0x3E8)
    Sleep(300)
    Jump("Function_2_24D")

    label("loc_277")

    Return()

    # Function_2_24D end

    def Function_3_278(): pass

    label("Function_3_278")

    SetMapObjFrame(0xFF, "main03", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29D")
    SetMapObjFrame(0xFF, "main03", 0x1, 0x1)

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1")
    SetChrPos(0x8, -40640, 0, 1570, 135)
    Jump("loc_322")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31D")

    label("loc_2E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_30C")
    SetChrPos(0x8, -35130, 0, 4170, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_31D")

    label("loc_30C")

    SetChrPos(0x8, -40640, 0, 1570, 135)

    label("loc_31D")

    Jump("loc_322")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    SetChrFlags(0x9, 0x80)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350")
    Event(0, 12)

    label("loc_350")

    Return()

    # Function_3_278 end

    def Function_4_351(): pass

    label("Function_4_351")

    Return()

    # Function_4_351 end

    def Function_5_352(): pass

    label("Function_5_352")

    TurnDirection(0xFE, 0x104, 0)

    #C0001
    ChrTalk(
        0xFE,
        "啊，你……你不是兰迪吗！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#0300F哦哦，这不是米蕾优上士吗，\x01",
            "你最近还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "还、还是和以前一样不懂礼节啊……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "而且，我现在已经晋升为准尉了！\x01",
            "叫我的时候，能不能不要这么随便啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，是吗？\x01",
            "抱歉抱歉。\x02\x03",

            "#0304F不过呢……\x01",
            "反正我已经脱离了警备队，\x01",
            "头衔对我来说已经没有什么意义了。\x02\x03",

            "#0309F今后也允许我轻松自然地称呼你吧，\x01",
            "米蕾优准尉大人。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……真是的！！\x01",
            "随便你好了！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 1)
    Return()

    # Function_5_352 end

    def Function_6_4E8(): pass

    label("Function_6_4E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506")
    Call(0, 5)
    Jump("loc_701")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_674")

    #C0007
    ChrTalk(
        0xFE,
        (
            "由乌尔斯拉医科大学\x01",
            "所研究开发的\x01",
            "营养剂已经运到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "与原来的营养剂相比，\x01",
            "是可以大幅度延长效果持续时间\x01",
            "的划时代产品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0005F不愧是乌尔斯拉医科大学……\x01",
            "经营领域真广呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#0309F喂，米蕾优。\x01",
            "机会难得，把那东西\x01",
            "也分给我们一点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "哈，可惜。\x01",
            "因为跟人数刚好相符，\x01",
            "所以完全没有多余的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0306F呜……有种莫名的\x01",
            "沮丧感呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_701")

    label("loc_674")


    #C0013
    ChrTalk(
        0xFE,
        (
            "由乌尔斯拉医科大学所开发的\x01",
            "营养剂的样品已经送到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "因为今晚的演习地点是在诺克斯森林。\x01",
            "肯定会非常疲劳吧，\x01",
            "希望这营养剂能发挥效果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_701")

    Jump("loc_1AF9")

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721")
    Call(0, 5)
    Jump("loc_96B")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7")

    #C0015
    ChrTalk(
        0xFE,
        (
            "明天预定要在诺克斯森林\x01",
            "使用标准装备来进行\x01",
            "夜战演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "警备队的标准装备是\x01",
            "冲击斧枪和来复枪，\x01",
            "参加这两种武器的训练是警备队员的义务。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "……但某个人\x01",
            "却违反了规定，\x01",
            "只使用冲击斧枪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0309F……哈哈哈，因为只有近身战\x01",
            "才符合我的性格，这也是没办法的事吧。\x02\x03",

            "#0300F不然，我就再让你见识一下？\x01",
            "兰迪大人比来复枪的子弹\x01",
            "还要快的斧枪绝技……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "呼，真是的……\x01",
            "还是这么得意忘形啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_96B")

    label("loc_8B7")


    #C0020
    ChrTalk(
        0xFE,
        (
            "警备队的标准装备是\x01",
            "冲击斧枪和来复枪，\x01",
            "参加这两种武器的训练是警备队员的义务。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……要是兰迪能老老实实\x01",
            "参加来复枪训练的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……算啦，还是不提了。\x01",
            "反正都已经过去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96B")

    Jump("loc_1AF9")

    label("loc_970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")
    Call(0, 5)
    Jump("loc_CB7")

    label("loc_98B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C02")
    TurnDirection(0xFE, 0x109, 0)

    #C0023
    ChrTalk(
        0xFE,
        "你是……诺艾尔上士吧。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "我听说过你的传闻呢，\x01",
            "唐古拉姆门的一位\x01",
            "诚实又能干的队员。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#0503F哪里，我还需要多加磨练呢。\x02\x03",

            "#0500F米蕾优准尉才令人佩服，\x01",
            "在那种司令的手下工作，\x01",
            "还能百折不挠地尽忠职守……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，米蕾优一直就是这样，\x01",
            "只有正义感这一点，绝对要胜过常人一倍呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0027
    ChrTalk(
        0xFE,
        "只、『只有』是什么意思啊？为什么要说『只有』？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006F喂，兰迪，\x01",
            "开玩笑也要有个限度啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        "#0304F好吧好吧。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "……真是的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    #C0031
    ChrTalk(
        0xFE,
        (
            "总之，能有诺艾尔上士这样\x01",
            "优秀的队员在，\x01",
            "作为长官，也是件高兴的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "为了让这支警备队有朝一日\x01",
            "转变为应有的正常状态，\x01",
            "我们就一起努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        "#0501F是、是的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 0)
    Jump("loc_CB7")

    label("loc_C02")


    #C0034
    ChrTalk(
        0xFE,
        (
            "其实，那个遗迹的调查工作\x01",
            "本来应该由我们来做，\x01",
            "但既然司令下达了命令，也就没办法了……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……诺艾尔上士，特别任务支援科的诸位。\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#0304F哈，你只管放心就好。\x02",
    )

    CloseMessageWindow()

    label("loc_CB7")

    Jump("loc_1AF9")

    label("loc_CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE6")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF8")
    Call(0, 5)
    Jump("loc_EC2")

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E27")

    #C0037
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，由我负责国境门的任务指挥，\x01",
            "到今天总算是告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "幸好，直到庆典结束，\x01",
            "也没有出现什么大麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0303F……不过，以那个司令的作风来说，\x01",
            "他今后肯定也会经常擅离职守，\x01",
            "把国境门丢下不管吧。\x02\x03",

            "#0300F米蕾优，你可得好好地\x01",
            "领导队员们才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "……嗯，我知道。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EC2")

    label("loc_E27")


    #C0041
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间的盘查工作一直\x01",
            "没出什么大问题，顺利撑到了庆典结束。\x01",
            "我总算是松了一口气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "从今以后，我也要继续努力，\x01",
            "引导队员们，以免他们迷失方向。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC2")

    Jump("loc_1AF9")

    label("loc_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1118")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF1")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F03")
    Call(0, 5)
    Jump("loc_1113")

    label("loc_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104C")

    #C0043
    ChrTalk(
        0xFE,
        (
            "我作为司令的代理，\x01",
            "正在整理出入境者\x01",
            "的通行许可申请书呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "……说起来，\x01",
            "我现在做的这种事务性工作，\x01",
            "兰迪好像几乎都没有做过吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#0306F嗯，因为太麻烦了嘛。\x02\x03",

            "基本都推给卡塔和柯纳斯\x01",
            "那些家伙了。\x02\x03",

            "#0309F作为回报，把在欢乐街\x01",
            "认识的女孩子介绍给了他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "（……以后有必要\x01",
            "  好好审问一下那两个人呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1113")

    label("loc_104C")


    #C0047
    ChrTalk(
        0xFE,
        (
            "兰迪……\x01",
            "难道你在特别任务支援科\x01",
            "也如此行事吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0309F哈哈，怎么会啊。\x01",
            "我怎么可能会把工作都推给罗伊德，\x01",
            "然后再给他介绍女孩子作为补偿……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0011F你、你这么说，\x01",
            "不就像不打自招一样吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1113")

    Jump("loc_1AF9")

    label("loc_1118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1327")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1142")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_1142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1154")
    Call(0, 5)
    Jump("loc_1322")

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E5")

    #C0050
    ChrTalk(
        0xFE,
        (
            "呼……我虽然不讨厌事务性工作。\x01",
            "不过还真是辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0304F嗯，因为米蕾优准尉\x01",
            "是武斗派呢。\x02\x03",

            "#0300F总之，要论武术造诣的话，\x01",
            "她可是技压贝尔加德门的男人们，\x01",
            "拥有着数一数二的实力呢。\x02\x03",

            "若是让她负责文案工作，\x01",
            "觉得无聊也是可以理解的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "你……！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "你岂不就是在说，\x01",
            "我连大脑都是\x01",
            "肌肉做的吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#0309F哎呀，失礼了。\x01",
            "不过我可没说谎啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "……哼。\x01",
            "够了，你别再来打扰我了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1322")

    label("loc_12E5")


    #C0056
    ChrTalk(
        0xFE,
        (
            "……哼，\x01",
            "我也是很忙的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "够了，你别再来打扰我了。\x02",
    )

    CloseMessageWindow()

    label("loc_1322")

    Jump("loc_1AF9")

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1639")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_140A")
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")

    #C0058
    ChrTalk(
        0xFE,
        (
            "我打算把司令室\x01",
            "彻底地查找一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "虽说是硬推给我的，\x01",
            "但这项工作非常重要。\x01",
            "就算是硬着头皮，也要做好……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FE")

    label("loc_13C7")


    #C0060
    ChrTalk(
        0xFE,
        (
            "那边的调查就交给你们了。\x01",
            "……总之，就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FE")

    OP_93(0x8, 0x0, 0x0)
    Jump("loc_1634")

    label("loc_140A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_141E")
    Call(0, 10)
    Jump("loc_1634")

    label("loc_141E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1430")
    Call(0, 5)
    Jump("loc_1634")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BF")

    #C0061
    ChrTalk(
        0xFE,
        (
            "纪念庆典从昨天就开始了……\x01",
            "在纪念庆典期间，\x01",
            "司令似乎出差了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "作为司令代理，\x01",
            "我一定要努力领导好\x01",
            "国境门的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#0300F警备队的队员全都是精英，\x01",
            "即使上司是那个偷懒大王司令，\x01",
            "也能努力做好工作。\x02\x03",

            "#0304F……不过，要是太拼命的话，\x01",
            "也许又会像以前一样，\x01",
            "犯下不必要的错误吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "（你……\x01",
            "  总、总是提一些不该说的事情……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0006F（以、以前究竟犯过什么错误呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1634")

    label("loc_15BF")


    #C0066
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间的交通量剧增，\x01",
            "发生事故也是在预料之内的。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "作为司令代理，\x01",
            "我一定要努力领导好\x01",
            "国境门的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1634")

    Jump("loc_1AF9")

    label("loc_1639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1654")
    Call(0, 5)
    Jump("loc_1A3C")

    label("loc_1654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1953")
    TurnDirection(0xFE, 0x104, 0)

    #C0068
    ChrTalk(
        0xFE,
        (
            "……兰迪，你……\x01",
            "还是别在贝尔加德门\x01",
            "附近晃来晃去为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0304F哈哈，怎么啦，米蕾优。\x01",
            "你会担心我，还真是少见呢。\x02\x03",

            "#0300F这么说来，在我被开除出\x01",
            "贝尔加德门警备队的时候，\x01",
            "你好像也曾激动地表示反对呢。\x02\x03",

            "#0305F……难道说，你对我……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "少、少说梦话了！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "我只是……不想因为那种小事\x01",
            "就失去宝贵的队员……！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#0005F那种小事是指……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#0200F……啊，就是之前说过的，\x01",
            "关于女性关系方面的纠纷吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0106F对与异性交往的热情竟然能\x01",
            "高到被警备队开除的程度，\x01",
            "这种事也就只有兰迪能做到了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0075
    ChrTalk(
        0xFE,
        "……女性关系方面的纠纷……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0309F──怎么了，米蕾优！\x01",
            "用不着那么害羞啦～\x02\x03",

            "#0304F你一直都对兰迪大人\x01",
            "怀有淡淡的恋情。\x01",
            "把心里话说出来就会轻松多了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "……唉，算了。\x01",
            "想和你认真说话也只是对牛弹琴……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A3C")

    label("loc_1953")


    #C0078
    ChrTalk(
        0xFE,
        (
            "我当时确实\x01",
            "对兰迪被解雇一事\x01",
            "表示了强烈反对。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "但、但那并……并不是\x01",
            "出于什么恋情不恋情，\x01",
            "只不过是经过理性考虑之后的……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#0306F哈，简单来说就是，\x01",
            "我离开的话，\x01",
            "你会感到寂寞难耐吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0081
    ChrTalk(
        0xFE,
        "……真是的，随便你怎么想吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1A3C")

    Jump("loc_1AF9")

    label("loc_1A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5C")
    Call(0, 5)
    Jump("loc_1AF9")

    label("loc_1A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC2")

    #C0082
    ChrTalk(
        0xFE,
        (
            "唉，离开警备队之后，\x01",
            "他还是一点都没变呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "你们平时看管兰迪\x01",
            "也很不容易吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AF9")

    label("loc_1AC2")


    #C0084
    ChrTalk(
        0xFE,
        (
            "你们也要注意呢。\x01",
            "要想管住这个男人，可是很麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF9")

    TalkEnd(0xFE)
    Return()

    # Function_6_4E8 end

    def Function_7_1AFD(): pass

    label("Function_7_1AFD")


    #C0085
    ChrTalk(
        0xFE,
        "啊……特别任务支援科的诸位。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0005F米蕾优准尉……\x01",
            "那、那个……\x02\x03",

            "#0003F前些天那个启动钥匙的事情……\x01",
            "在进行到一半时放弃，真是很抱歉。\x01",
            "因为当时还有些无论如何也推托不开的工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "哪里，请不必放在心上。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "在那之后，我们又彻夜进行了寻找，\x01",
            "最后总算是把启动钥匙找到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#0303F……对不起，真是很抱歉。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0090
    ChrTalk(
        0xFE,
        "呵呵，说这种话可不像你的性格啊。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "算了，你们也很忙的，\x01",
            "那也是没办法的事啊。\x01",
            "真的不用放在心上。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 3)
    Return()

    # Function_7_1AFD end

    def Function_8_1CAC(): pass

    label("Function_8_1CAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2C")

    #C0092
    ChrTalk(
        0xFE,
        (
            "虽然今天要在森林\x01",
            "进行夜战演习……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "但还是和往常一样，只能小打小闹一场，\x01",
            "真是很难为情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D63")

    label("loc_1D2C")


    #C0094
    ChrTalk(
        0xFE,
        (
            "……算啦，但终究还是要参加的。\x01",
            "唉，真是难为情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D63")

    Jump("loc_1FA5")

    label("loc_1D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1E14")

    #C0095
    ChrTalk(
        0xFE,
        (
            "在唐古拉姆门工作的巴雷尔因为\x01",
            "遗迹调查工作顺利结束而非常高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "听说是特别任务支援科的诸位\x01",
            "协助了诺艾尔上士吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        "我在此也要表示感谢，谢谢你们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1EAD")

    #C0098
    ChrTalk(
        0xFE,
        (
            "前些天，我从唐古拉姆门的巴雷尔\x01",
            "那里得到了彩虹剧团的新人\x01",
            "莉夏·毛的海报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "因为很难得，我就把它贴在那边了……\x01",
            "嗯，真是好东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC8")
    Call(0, 9)
    Jump("loc_1F17")

    label("loc_1EC8")


    #C0100
    ChrTalk(
        0xFE,
        (
            "在贝尔加德门司令\x01",
            "手下工作的我最能体会……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "上司无能，是不幸中的不幸。\x02",
    )

    CloseMessageWindow()

    label("loc_1F17")

    Jump("loc_1FA5")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1FA5")

    #C0102
    ChrTalk(
        0xFE,
        (
            "因为司令总是不在司令部，\x01",
            "所以这里其实是由米蕾优准尉来指挥的。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "准尉虽然还有点不够可靠，\x01",
            "但仍算是一位拼命努力的好长官。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA5")

    TalkEnd(0xFE)
    Return()

    # Function_8_1CAC end

    def Function_9_1FA9(): pass

    label("Function_9_1FA9")


    #C0104
    ChrTalk(
        0xFE,
        (
            "好，休息也该结束了，\x01",
            "今天必须要努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "并不是为了司令，\x01",
            "而是为了米蕾优准尉。\x01",
            "只要这么想，工作也就没那么辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "对了，这本书……\x01",
            "我已经在休息时看完了，\x01",
            "就送给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CA, 1)
    SetScenarioFlags(0x9C, 4)
    Return()

    # Function_9_1FA9 end

    def Function_10_20AC(): pass

    label("Function_10_20AC")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-35280, 900, 2640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24100, 0)
    SetChrPos(0x101, -34000, 0, 1500, 0)
    SetChrPos(0x102, -35300, 0, 1000, 0)
    SetChrPos(0x103, -34000, 0, 500, 0)
    SetChrPos(0x104, -35300, 0, 2000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A5")

    #C0108
    ChrTalk(
        0x8,
        (
            "#11P哎呀，真是的……\x01",
            "到底在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        "#11P再不赶快找出来的话……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_END)), "loc_22AD")

    #C0110
    ChrTalk(
        0x104,
        (
            "#6P#0300F哟，米蕾优，\x01",
            "你还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#0000F准尉，您辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x12C)

    #C0112
    ChrTalk(
        0x8,
        (
            "#11P……兰迪？\x01",
            "还有特别任务支援科的诸位……\x01",
            "你们怎么会在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0113
    ChrTalk(
        0x8,
        (
            "#11P啊，对了，是我发出了\x01",
            "支援请求呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#11P对不起，我可真是的，\x01",
            "都忘得一干二净了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_22AD")


    #C0115
    ChrTalk(
        0x104,
        (
            "#6P#0300F哟，米蕾优，\x01",
            "你还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x12C)

    #C0116
    ChrTalk(
        0x8,
        "#11P……兰迪？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#11P啊……你不是兰迪吗！\x01",
            "怎么会在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "#11P还有，这几位是……？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊，那个……\x01",
            "我是警察局·特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02\x03",

            "#0000F这次是接到了支援请求，\x01",
            "特意前来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x8,
        (
            "#11P……啊……\x01",
            "这样啊，是兰迪如今\x01",
            "所在的那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#11P说起来，我已经把发出支援请求的\x01",
            "事情忘得一干二净了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2456")

    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x102,
        (
            "#6P#0109F那个……\x01",
            "您一定很忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#6P#0304F哈哈，你还是老样子，\x01",
            "表面上看起来一丝不苟，\x01",
            "其实有些傻里傻气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        "#11P你、你说什么？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#11P你这家伙\x01",
            "有什么资格说我……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0006F那、那个，总之，\x01",
            "请先冷静一下。\x02\x03",

            "#0001F能否请您先说明一下……\x01",
            "把我们支援科\x01",
            "叫到此处的理由呢？\x02\x03",

            "优秀的警备队竟然\x01",
            "需要请求我们来协助，\x01",
            "莫非是出了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#11P……咳咳，是啊。\x01",
            "不好意思，我刚才有些失态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#11P……现在整个贝尔加德门上下\x01",
            "都在寻找一件重要的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#11P这本来应该算是优先级最高的事件，\x01",
            "但正如你们所见，在纪念庆典这个特殊时期，\x01",
            "我们这边正处于人手严重不足的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#11P所以我这次就擅作主张，\x01",
            "请了诸位前来。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#6P#0103F原来如此……情况已经了解了。\x02\x03",

            "#0105F那么，重要的东西是指？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#11P这个……\x01",
            "是最近警备队刚刚配备的\x01",
            "新型装甲车的启动钥匙。\x02",
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

    #C0133
    ChrTalk(
        0x101,
        "#12P#0005F新型装甲车……！？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        (
            "#6P#0200F我听说过关于那个的情报……\x01",
            "原来都已经正式配备了吗？\x02\x03",

            "但是，那么重要的东西，\x01",
            "为什么会……？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        "#6P#0301F……因为司令，对吧？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2902():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2902)

    def lambda_290F():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_290F)

    def lambda_291C():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_291C)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x8,
        "#11P……果然被你猜到了呢。\x02",
    )

    CloseMessageWindow()

    def lambda_294C():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_294C)

    def lambda_2959():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2959)

    def lambda_2966():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2966)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)

    #C0137
    ChrTalk(
        0x101,
        "#12P#0005F到、到底是怎么回事呢？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#11P就在昨天……司令在平时接待客人的地方\x01",
            "召开了一场纪念庆典的庆祝会。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#11P酒酣耳热之后，\x01",
            "喝到酩酊大醉的司令……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#11P让部下把刚刚配备的\x01",
            "新型装甲车开到了\x01",
            "庆祝会会场那边。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#6P#0303F大概是想展示给那些大人物，\x01",
            "讨他们的欢心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        "#6P#0200F……真是鄙俗呢。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "#11P……然后，司令回来以后，\x01",
            "就把新型装甲车停在了国境门内部，\x01",
            "又从部下那里要回了启动钥匙……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#11P最后，就不知\x01",
            "丢在了什么地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#11P因为没有钥匙就无法将车子启动后转移，\x01",
            "所以才出此下策，\x01",
            "就那样用罩子暂时遮住……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊……原来那个就是新型装甲车啊。\x02\x03",

            "#0001F不过，那个罩子不是起到了反效果吗？\x01",
            "我怎么感觉它更加显眼了……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        (
            "#6P#0101F但是，如果就那么放着不管的话，\x01",
            "也会引起各种麻烦的问题呢。\x02\x03",

            "#0103F把警备队新武装的装甲车\x01",
            "停放在国境门的内部……\x02\x03",

            "#0101F就算被人指责成是\x01",
            "向埃雷波尼亚帝国发起的敌对行为，\x01",
            "也无可辩驳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#12P#0005F竟、竟然有那么严重吗……？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "#11P……多少也会产生一点\x01",
            "负面的刺激吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            "#6P#0303F嗯……不过，所谓的新型号，\x01",
            "是那么不得了的东西吗？\x02\x03",

            "#0300F现在配备的这种型号，\x01",
            "如果只看装甲强度与机动性的话，\x01",
            "我觉得就已经相当不错了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#11P相比以前那些旧型号的装甲车，\x01",
            "新型战车改良成了更加适合战斗的设计。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "#11P装设了机关炮与小型导弹炮座，\x01",
            "所以火力性能得到了大幅提高。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#11P按照警备队目前的武装水平来说，\x01",
            "应该算得上是最强的一类了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#6P#0301F……原来如此。\x01",
            "看样子，果然不是可以随便放在\x01",
            "国境门内部的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0155
    ChrTalk(
        0x104,
        (
            "#6P#0303F……所以呢？\x01",
            "那个传说中的司令大人\x01",
            "到底干了什么好事？\x02\x03",

            "#0301F这里好像就是那家伙的房间吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "#11P司令在今天早晨\x01",
            "把寻找钥匙的事情交给了我，\x01",
            "自己就出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x8,
        (
            "#11P他说，纪念庆典的接待工作\x01",
            "可不能交给别人随便应付……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        "#6P#0303F……嘁，还是老样子呢。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#6P#0200F越听越觉得是个\x01",
            "无药可救的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#11P总之……\x01",
            "我希望能尽早\x01",
            "把新型装甲车移动到其它地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#11P寻找启动钥匙的工作……\x01",
            "你们能提供帮助吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x1)
    SetScenarioFlags(0x8C, 1)
    Jump("loc_3112")

    label("loc_30A5")

    OP_93(0x8, 0xB4, 0x1F4)

    #C0162
    ChrTalk(
        0x8,
        (
            "#11P我希望能尽早\x01",
            "把新型装甲车移动到其它地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#11P寻找启动钥匙的工作……\x01",
            "你们能提供帮助吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3112")

    Call(0, 11)
    Return()

    # Function_10_20AC end

    def Function_11_3116(): pass

    label("Function_11_3116")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3167"),
        (1, "loc_3736"),
        (SWITCH_DEFAULT, "loc_37EA"),
    )


    label("loc_3167")

    OP_60(0x0)

    #C0164
    ChrTalk(
        0x101,
        "#12P#0001F明白了，我们接受您的委托。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#11P……谢谢，\x01",
            "真是帮了大忙……！\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#6P#0101F那么……\x01",
            "为了寻找钥匙，请您告诉我们\x01",
            "司令当天的行动路线。\x02\x03",

            "您应该也向司令\x01",
            "了解过这些了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "#11P是的……不过都是今天早上\x01",
            "才从司令口中得知的信息。\x01",
            "要听吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        "#6P#0203F……嗯，请说吧。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "#11P……首先，司令回来之后，\x01",
            "让部下把装甲车停在了国境门的内部，\x01",
            "然后要走了钥匙。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "#11P恐怕是……因为在庆祝会上喝多了，\x01",
            "为了醒酒，想要吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "#11P于是就直奔食堂，\x01",
            "要求厨师给他做点小菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "#11P然后，他趁着兴致大发，\x01",
            "就跑到屋顶上唱歌……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "#11P之后就突然注意到\x01",
            "启动钥匙不见了。\x02",
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

    #C0174
    ChrTalk(
        0x103,
        (
            "#6P#0203F真是的……\x01",
            "好像是醉得不轻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#12P#0006F该、该怎么说呢……\x01",
            "能醉到那种程度，也真不是一般人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        "#6P#0301F真没办法啊。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#6P#0101F那么……看样子，钥匙应该是在\x01",
            "刚才提到过的那些地点中丢失的吧。\x02\x03",

            "#0103F既然如此，我想钥匙\x01",
            "应该还在贝尔加德门之内。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯，确实是这样。\x02\x03",

            "#0000F好，那么……\x01",
            "我们就去那些地方调查一下吧。\x02\x03",

            "说不定能发现什么\x01",
            "新线索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#6P#0200F米蕾优准尉\x01",
            "要和我们一起搜寻吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "#11P不……既然已经决定了搜寻方针，\x01",
            "我跟你们去也只是添乱罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "#11P我要把这间司令室\x01",
            "彻底检查一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#6P#0304F嗯，剩下的就交给我们吧，\x01",
            "大家破釜沉舟，\x01",
            "一心向敌吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        "#11P真是的……拜托你认真一点啊。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#12P#0000F总之，搜寻任务开始。\x02\x03",

            "先去调查一下那辆\x01",
            "新型装甲车吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【搜寻重要遗失物】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x19, 0x1, 0x2)
    Jump("loc_37F9")

    label("loc_3736")

    OP_60(0x0)

    #C0186
    ChrTalk(
        0x101,
        (
            "#12P#0006F十分抱歉……\x01",
            "我们还有些重要的工作在身……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#11P这样啊……\x01",
            "那也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "#11P那就等你们把\x01",
            "其它事情解决之后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        "#11P总之，拜托各位了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F9")

    label("loc_37EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F9")

    label("loc_37F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -34470, 0, 200, 90)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_3116 end

    def Function_12_382C(): pass

    label("Function_12_382C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-42850, 900, 590, 0)
    MoveCamera(294, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(29780, 0)
    SetChrPos(0x101, -33410, 0, -910, 225)
    SetChrPos(0x102, -32170, 0, 1270, 315)
    SetChrPos(0x103, -33510, 0, 870, 315)
    SetChrPos(0x104, -32220, 0, -420, 270)
    Sleep(500)
    OP_68(-36150, 900, 890, 5000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0190
    ChrTalk(
        0x101,
        "#0005F这里是……？\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#0301F……警备队司令大人的房间啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0192
    ChrTalk(
        0x101,
        (
            "#0005F那个司令似乎不在……\x02\x03",

            "是去了什么地方了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#0306F嗯，无非就是应酬之类的吧。\x02\x03",

            "他的工作基本都会推给部下。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#0000F嗯……这么说的话，\x01",
            "还是放弃和司令见面这个念头吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        (
            "#0305F啊？难道你之前还打算和他见面吗？\x02\x03",

            "#0306F我说你啊……那可是我的前上司哦。\x01",
            "要是见了面，可不是一般的尴尬啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#0000F说、说得也是。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        (
            "#0106F……话说回来，\x01",
            "这可真是个恶趣味的房间啊。\x02\x03",

            "#0101F架子上摆的古董之类，\x01",
            "似乎价值几万米拉……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x103,
        (
            "#0200F……该怎么说呢，很难想象\x01",
            "这里会是警备队司令的房间啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0199
    ChrTalk(
        0x104,
        (
            "#0300F收集这些东西所花费的金钱，\x01",
            "大概都是通过常年受贿所积攒下的吧。\x02\x03",

            "#0306F不过，还真是浪费啊。\x01",
            "我要是有这么多米拉的话，\x01",
            "肯定会去欢乐街好好开心一下。\x02\x03",

            "比如让漂亮的姐姐陪着我，\x01",
            "在『巴鲁卡』玩个通宵。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    #C0200
    ChrTalk(
        0x103,
        "#0211F……你们根本就是一丘之貉。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -32220, 0, -420, 270)
    SetScenarioFlags(0x6F, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_382C end

    SaveToFile()

Try(main)
