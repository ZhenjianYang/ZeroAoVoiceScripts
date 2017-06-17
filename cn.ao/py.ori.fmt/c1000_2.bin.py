from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1000_2.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [152, 4017, 7488, 10676, 19610, 22568, 23003, 23593, 25608, 0, 28405, 0, 31631, 34204, 34590, 36328, 0, 37945, 0, 238, 155, 0, 0],
    )

    BuildStringList((
        "c1000_2",                # 0
    ))

    ChipFrameInfo(152, 0)                                        # 0

    ScpFunction((
        "Function_0_98",           # 00, 0
        "Function_1_FB1",          # 01, 1
        "Function_2_1D40",         # 02, 2
        "Function_3_29B4",         # 03, 3
        "Function_4_4C9A",         # 04, 4
        "Function_5_5828",         # 05, 5
        "Function_6_59DB",         # 06, 6
        "Function_7_5C29",         # 07, 7
        "Function_8_6408",         # 08, 8
        "Function_9_6EF5",         # 09, 9
        "Function_10_7B8F",        # 0A, 10
        "Function_11_859C",        # 0B, 11
        "Function_12_871E",        # 0C, 12
        "Function_13_8DE8",        # 0D, 13
        "Function_14_9439",        # 0E, 14
        "Function_15_9BEE",        # 0F, 15
        "Function_16_9CD5",        # 10, 16
    ))


    def Function_0_98(): pass

    label("Function_0_98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)

    #C0001
    ChrTalk(
        0x8,
        "哎呀，真是个可爱的小朋友呢～\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "要不要买个风车呢？\x01",
            "吹起来就会呼呼地转，很有趣哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x1A2,
        "……你是在和我说话吗？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x1A2,
        (
            "哼，这种东西在东方\x01",
            "根本就是烂大街的货，\x01",
            "你少糊弄小孩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "（打击）……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1FF")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2AC")

    label("loc_1FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_258")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2AC")

    label("loc_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2AC")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2AC")

    TalkEnd(0x8)
    SetScenarioFlags(0x1DC, 3)
    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_2FA")

    label("loc_2C3")


    #C0006
    ChrTalk(
        0x8,
        (
            "唔唔……\x01",
            "我还是头一次碰到\x01",
            "这么难对付的小朋友。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_2FA")

    Return()

    label("loc_2FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_355")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_355")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_374")
    OP_AF(0x38)
    Jump("loc_376")

    label("loc_374")

    OP_AF(0x39)

    label("loc_376")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FA8")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_399")
    Jump("loc_FA8")

    label("loc_399")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469")

    #C0007
    ChrTalk(
        0xFE,
        (
            "不管怎么说，克洛斯贝尔市\x01",
            "能恢复正常，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "虽然又冒出一棵\x01",
            "莫名其妙的大树……\x01",
            "不过，船到桥头自然直嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "干脆做点新的工艺品\x01",
            "来解解闷吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4D8")

    label("loc_469")


    #C0010
    ChrTalk(
        0xFE,
        (
            "从明天开始，我打算\x01",
            "让洛依也回来继续工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "虽然又冒出一棵\x01",
            "莫名其妙的大树……\x01",
            "不过，船到桥头自然直嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8")

    Jump("loc_FA8")

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4EB")
    Jump("loc_FA8")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_54D")

    #C0012
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市终于\x01",
            "成为独立国家了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "总觉得我见证到了\x01",
            "历史变迁的瞬间呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D9")

    #C0014
    ChrTalk(
        0xFE,
        (
            "为了支援旧城区那边的\x01",
            "赈济餐分发，\x01",
            "我给他们做了很多木质的餐具。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "虽然只是微不足道的小事，\x01",
            "但我能做的\x01",
            "也只有这么多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_64E")

    #C0016
    ChrTalk(
        0xFE,
        (
            "听说玛因兹被\x01",
            "占领了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "那里的人一直很关照我，\x01",
            "给我提供了不少工艺品的材料，\x01",
            "真担心他们啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C5")

    #C0018
    ChrTalk(
        0xFE,
        (
            "看样子，今天也不会\x01",
            "有什么顾客来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "已经让洛依去休息了，\x01",
            "我就一个人悠闲自在地\x01",
            "做些工艺品吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_6C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_721")

    #C0020
    ChrTalk(
        0xFE,
        (
            "洛依做的风车在不知不觉间\x01",
            "就卖出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "哎呀～连我都为他\x01",
            "感到高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_832")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5")

    #C0022
    ChrTalk(
        0xFE,
        (
            "摆在店面的那些风车，\x01",
            "每一个的旋转方式都有\x01",
            "细小区别哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "这正是手工制品\x01",
            "独具的特色。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "不过，外行人\x01",
            "一般都看不出\x01",
            "其中的不同。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_82D")

    label("loc_7C5")


    #C0025
    ChrTalk(
        0xFE,
        (
            "话说回来，洛依已经\x01",
            "能做出一个可以当作商品\x01",
            "出售的风车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "他的手其实\x01",
            "挺巧的，\x01",
            "将来很有前途呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82D")

    Jump("loc_FA8")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_93C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DC")

    #C0027
    ChrTalk(
        0xFE,
        (
            "我努力制作的\x01",
            "兰花塔模型\x01",
            "总算在昨晚完工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "我把它摆在店面，\x01",
            "结果好多游客\x01",
            "都很想买下它。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "但它是非卖品呢～\x01",
            "总觉得有点对不起大家。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_937")

    label("loc_8DC")


    #C0030
    ChrTalk(
        0xFE,
        (
            "话说回来，洛依\x01",
            "干活总是那么踏实，\x01",
            "真是帮了我的大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "这也是继承自\x01",
            "会长的优点吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_937")

    Jump("loc_FA8")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C2")

    #C0032
    ChrTalk(
        0xFE,
        (
            "洛依开始\x01",
            "在我这里工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "他不愧是工商协会会长的\x01",
            "孙子，做事非常认真。\x01",
            "看来是个可以期待的人才呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A18")

    label("loc_9C2")


    #C0034
    ChrTalk(
        0xFE,
        (
            "我打算趁此机会，\x01",
            "多教他一些东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "呵呵，感觉就像收了个徒弟一样，\x01",
            "真高兴啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A18")

    Jump("loc_FA8")

    label("loc_A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC4")

    #C0036
    ChrTalk(
        0xFE,
        (
            "刚才那个东方打扮的美女吗？\x01",
            "她在小摊上买了不少东西，\x01",
            "然后就往中央广场那边走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "那带着冷意的细长眉眼\x01",
            "实在是让人印象深刻啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D00")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFF")

    #C0038
    ChrTalk(
        0xFE,
        (
            "刚才有个东方打扮的美女\x01",
            "来这里买东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "她那带着冷意的细长眉眼\x01",
            "实在是让人印象深刻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00001F……请问那个人往哪里走了？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "她在小摊上买了不少东西，\x01",
            "然后就往中央广场那边走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00305F（喂，罗伊德，\x01",
            "  该不会是她吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00001F（……总之，我们去找找看吧。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1C6, 7)
    Jump("loc_D00")

    label("loc_BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAA")

    #C0044
    ChrTalk(
        0xFE,
        (
            "哎呀～兰花塔的气势\x01",
            "真是不同凡响～\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "嗯～我的创作欲也被它激发起来了。\x01",
            "干脆试着做个模型吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "以前举办纪念庆典的时候，\x01",
            "我也做过市政厅的模型呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D00")

    label("loc_CAA")


    #C0047
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "工商协会的摩尔斯会长的\x01",
            "孙子正在我这里参观呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "唔～这还真是稀奇。\x02",
    )

    CloseMessageWindow()

    label("loc_D00")

    Jump("loc_FA8")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D74")

    #C0049
    ChrTalk(
        0xFE,
        (
            "我这家店里的工艺品\x01",
            "全都是手工制作。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "手工制作的东西\x01",
            "让人有种温馨的感觉呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DC0")

    label("loc_D74")


    #C0051
    ChrTalk(
        0xFE,
        (
            "虽然手工制作很花工夫，\x01",
            "有时还会受伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "可是却会让人\x01",
            "感到很温馨～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC0")

    Jump("loc_FA8")

    label("loc_DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E70")

    #C0053
    ChrTalk(
        0xFE,
        (
            "好不容易才做好的\x01",
            "工艺品都被雨打湿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "……不过，\x01",
            "我店里的工艺品\x01",
            "全都做过防水加工。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "虽然这很花工夫，但正因如此，\x01",
            "它们十分结实哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ECA")

    label("loc_E70")


    #C0056
    ChrTalk(
        0xFE,
        (
            "我店里的工艺品\x01",
            "全都做过防水加工。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "虽然这很花工夫，但正因如此，\x01",
            "它们十分结实哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECA")

    Jump("loc_FA8")

    label("loc_ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F54")

    #C0058
    ChrTalk(
        0xFE,
        "嘿，欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "本店出售\x01",
            "各式手工制作的工艺品。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "如果您看中了哪件作品，\x01",
            "请一定要赏光购买哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FA8")

    label("loc_F54")


    #C0061
    ChrTalk(
        0xFE,
        (
            "在本店的商品中，\x01",
            "这款『风车』很受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "据说这种玩具在东方\x01",
            "还用于辟邪呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA8")

    Jump("loc_305")

    label("loc_FAD")

    TalkEnd(0xFE)
    Return()

    # Function_0_98 end

    def Function_1_FB1(): pass

    label("Function_1_FB1")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_100E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_100E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102E")
    OP_AF(0x35)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D37")

    label("loc_102E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1042")
    Jump("loc_1D37")

    label("loc_1042")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D37")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_113C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E7")

    #C0063
    ChrTalk(
        0xFE,
        "欢迎光临，欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "迪因兹食材店\x01",
            "正在营业！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "多吃点新鲜的蔬菜，\x01",
            "健健康康地渡过\x01",
            "这场异常事态吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1137")

    label("loc_10E7")


    #C0066
    ChrTalk(
        0xFE,
        (
            "……莉莉从刚才开始，\x01",
            "就频繁用眼角余光\x01",
            "瞄我。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "我的脸上沾了什么东西吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1137")

    Jump("loc_1D37")

    label("loc_113C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_114A")
    Jump("loc_1D37")

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D8")

    #C0068
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立国啊……\x01",
            "哎呀～真是件大喜事。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "但莉莉那家伙\x01",
            "却一副\x01",
            "相当烦恼的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "她有什么烦心事吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_121A")

    label("loc_11D8")


    #C0071
    ChrTalk(
        0xFE,
        (
            "莉莉那家伙\x01",
            "露出一副\x01",
            "相当烦恼的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "她有什么烦心事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_121A")

    Jump("loc_1D37")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1332")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C6")

    #C0073
    ChrTalk(
        0xFE,
        (
            "我们为今天在市民会馆\x01",
            "举办的慈善活动\x01",
            "捐了一些蔬菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "因为主办方工商协会\x01",
            "一直都很关照我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "而且我也希望\x01",
            "市民们能打起精神来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_132D")

    label("loc_12C6")


    #C0076
    ChrTalk(
        0xFE,
        (
            "工商协会的老爷子\x01",
            "还曾邀请我去做干部，\x01",
            "平时一直都很照顾我。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "而且我也想向市民们\x01",
            "献上一己之力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132D")

    Jump("loc_1D37")

    label("loc_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_13FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BE")

    #C0078
    ChrTalk(
        0xFE,
        (
            "听说玛因兹被占领了……\x01",
            "对方好像到现在都没有提出\x01",
            "索求赎金之类的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "那个武装集团到底\x01",
            "想干什么啊……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13F6")

    label("loc_13BE")


    #C0080
    ChrTalk(
        0xFE,
        (
            "那个武装集团到底\x01",
            "是为了什么\x01",
            "才会占领玛因兹啊……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F6")

    Jump("loc_1D37")

    label("loc_13FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A3")

    #C0081
    ChrTalk(
        0xFE,
        (
            "那个来送蔬菜的小兄弟\x01",
            "相当兴奋地和我说……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村昨天\x01",
            "出了件大事……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "他说事情已经圆满解决了……\x01",
            "嗯～到底发生了什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_151C")

    label("loc_14A3")


    #C0084
    ChrTalk(
        0xFE,
        (
            "听说阿尔摩利卡村昨天\x01",
            "出了件大事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "但那个开卡车的小兄弟实在是\x01",
            "太兴奋了，说话还带着口音，\x01",
            "我听得不是很明白。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151C")

    Jump("loc_1D37")

    label("loc_1521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_161E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B2")

    #C0086
    ChrTalk(
        0xFE,
        (
            "其实我小时候\x01",
            "最讨厌吃蔬菜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "不过长大之后，\x01",
            "渐渐就开始觉得\x01",
            "蔬菜很好吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "挑食其实也就是\x01",
            "这么一回事吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1619")

    label("loc_15B2")


    #C0089
    ChrTalk(
        0xFE,
        (
            "我以前最讨厌的就是蔬菜，\x01",
            "可是在不知不觉间\x01",
            "就开始喜欢吃蔬菜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "挑食其实也就是\x01",
            "这么一回事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1619")

    Jump("loc_1D37")

    label("loc_161E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16AD")

    #C0091
    ChrTalk(
        0xFE,
        (
            "其实，这家店的店名是\x01",
            "莉莉取的。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "自从我跟她说起想做生意之后，\x01",
            "她就一直在各方面支持着我……\x01",
            "嘿嘿，真是个很好的童年好友。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D37")

    label("loc_16AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174A")

    #C0093
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村的人一向是\x01",
            "开着导力卡车把蔬菜\x01",
            "运送过来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "唔～这样说可能有些不礼貌，\x01",
            "但我记得他们并没有\x01",
            "那么漂亮的卡车。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17A9")

    label("loc_174A")


    #C0095
    ChrTalk(
        0xFE,
        (
            "难道阿尔摩利卡村\x01",
            "买了一辆新的\x01",
            "导力卡车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "嘿嘿，看来他们的生意不错，\x01",
            "真让人羡慕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A9")

    Jump("loc_1D37")

    label("loc_17AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_18B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1834")

    #C0097
    ChrTalk(
        0xFE,
        (
            "听说通商会议主要会\x01",
            "围绕经济问题展开讨论……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "……不过，\x01",
            "我也搞不懂那些深奥的事。\x01",
            "还是顺其自然吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18AF")

    label("loc_1834")


    #C0099
    ChrTalk(
        0xFE,
        (
            "管他什么经济不经济的，\x01",
            "我只需要坚持顾客第一的原则，\x01",
            "好好做自己的生意就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "反正我也完全搞不懂那些\x01",
            "深奥的问题！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AF")

    Jump("loc_1D37")

    label("loc_18B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BF")

    #C0101
    ChrTalk(
        0xFE,
        (
            "听说利贝尔王国的\x01",
            "公主殿下今天来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "说起利贝尔王国，\x01",
            "他们那里出口的『苦西红柿』非常有名。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "据说是利贝尔的一家\x01",
            "名为蔡斯中央工房的\x01",
            "导力器制造商出产的蔬菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "明明是导力器制造商，\x01",
            "竟然还能出产蔬菜，\x01",
            "他们的技术水平果真高超啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A47")

    label("loc_19BF")


    #C0105
    ChrTalk(
        0xFE,
        (
            "苦西红柿是蔡斯中央工房\x01",
            "在前一段时间培育出来的\x01",
            "新品种蔬菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "明明是导力器制造商，\x01",
            "竟然还能生产蔬菜，\x01",
            "他们的技术水平果真高超啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A47")

    Jump("loc_1D37")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B66")

    #C0107
    ChrTalk(
        0xFE,
        (
            "听乌尔斯拉医院的\x01",
            "医生说……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "吃蔬菜有利于\x01",
            "吸收油脂。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "只要在吃肉的同时\x01",
            "吃一些蔬菜，\x01",
            "就不容易发胖。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF4")
    Jump("loc_1B5E")

    label("loc_1AF4")


    #C0110
    ChrTalk(
        0x109,
        "#10105F原、原来如此……！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#00102F真是受教了。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00012F（女性真是特别关心\x01",
            "  这种话题啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5E")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1BD1")

    label("loc_1B66")


    #C0113
    ChrTalk(
        0xFE,
        (
            "你们平时爱吃蔬菜吗？\x01",
            "如果光吃高热量食品，\x01",
            "对身体可是很不好的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "要想身体健康，\x01",
            "就得多吃些蔬菜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD1")

    Jump("loc_1D37")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C51")

    #C0115
    ChrTalk(
        0xFE,
        (
            "……嗯～顶棚\x01",
            "漏雨了呢，\x01",
            "得尽早修补才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "……话说回来，莉莉那家伙怎么\x01",
            "从刚才开始就一直扭扭捏捏的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D37")

    label("loc_1C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF2")

    #C0117
    ChrTalk(
        0xFE,
        "欢迎光临，欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "今天也有大量阿尔摩利卡出产的\x01",
            "蔬菜在等着大家购买哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔本土出产的蔬菜\x01",
            "果然是最好吃的啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D37")

    label("loc_1CF2")


    #C0120
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡出产的美味蔬菜\x01",
            "最值得推荐！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "各位多买一些回去吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1D37")

    Jump("loc_FBE")

    label("loc_1D3C")

    TalkEnd(0xFE)
    Return()

    # Function_1_FB1 end

    def Function_2_1D40(): pass

    label("Function_2_1D40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E12")

    #C0122
    ChrTalk(
        0xFE,
        (
            "迪因兹可真是的……\x01",
            "说什么多吃蔬菜就能渡过难关，\x01",
            "没脑子也得有个限度吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "不过，正因为迪因兹这个样子，\x01",
            "才让大家打起了精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "作为一个露天摊贩，\x01",
            "这一点也许才是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E97")

    label("loc_1E12")


    #C0125
    ChrTalk(
        0xFE,
        (
            "正因为迪因兹傻乎乎的，\x01",
            "才让大家打起了精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "市内出现怪物的时候，\x01",
            "我也曾在迪因兹的感染下产生了勇气。\x01",
            "呵呵，得好好感谢他呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E97")

    Jump("loc_29B0")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1EAA")
    Jump("loc_29B0")

    label("loc_1EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA7")

    #C0127
    ChrTalk(
        0xFE,
        (
            "与两大国的货物流通\x01",
            "已经完全中断了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "据说迪塔总统\x01",
            "准备了足够使用\x01",
            "五年的储备物资……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "可我们店的卖点就是新鲜蔬菜啊，\x01",
            "得考虑一下今后该怎么办了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "……可是，迪因兹好像\x01",
            "完全没想到这一点。\x01",
            "唉，真希望他能可靠些啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2022")

    label("loc_1FA7")


    #C0131
    ChrTalk(
        0xFE,
        (
            "据说迪塔总统准备了足够使用\x01",
            "五年的储备物资……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "可货物流通的中断\x01",
            "关系到我们今后的生意，\x01",
            "真希望迪因兹多想想这些啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2022")

    Jump("loc_29B0")

    label("loc_2027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206F")

    #C0133
    ChrTalk(
        0xFE,
        (
            "东街这边\x01",
            "几乎没有受损，\x01",
            "真是不幸中的万幸……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_206F")


    #C0134
    ChrTalk(
        0xFE,
        (
            "遭受那个巨大恶鬼的一番肆虐之后，\x01",
            "旧城区已经是满目狼藉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "听说那边已经开始重建了……\x01",
            "可真不知道何时才能建好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_20EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2148")

    #C0136
    ChrTalk(
        0xFE,
        "玛因兹那件事真是吓人啊……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "但愿警备队的人\x01",
            "能想个法子，\x01",
            "解决这件事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_2148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21D3")

    #C0138
    ChrTalk(
        0xFE,
        (
            "哎呀，真是的，\x01",
            "前段时间刚补好顶棚上的洞，\x01",
            "现在又有别的地方漏雨了。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "迪因兹可真是的，\x01",
            "别想东想西的了，赶紧来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_21D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_231B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B3")

    #C0140
    ChrTalk(
        0xFE,
        (
            "大葱和韭菜这类蔬菜的\x01",
            "气味很大，\x01",
            "所以有不少人感到厌恶……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "但很多人其实根本没吃过，\x01",
            "直接就产生了先入为主的偏见。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "如果他们能鼓起勇气尝一口，\x01",
            "没准会觉得很好吃呢，\x01",
            "真希望他们能尝试一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2316")

    label("loc_22B3")


    #C0143
    ChrTalk(
        0xFE,
        (
            "没尝过就产生偏见，\x01",
            "这实在是有些遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "某些食物闻起来不怎么样，\x01",
            "但吃起来却\x01",
            "相当美味呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2316")

    Jump("loc_29B0")

    label("loc_231B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2444")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D1")

    #C0145
    ChrTalk(
        0xFE,
        (
            "迪因兹什么\x01",
            "都还没搞清楚，\x01",
            "就想开始做生意了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "像营业许可证啊，\x01",
            "营业场地之类的，\x01",
            "都是我帮他准备好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "从小到大，他一直是个\x01",
            "让人放心不下的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_243F")

    label("loc_23D1")


    #C0148
    ChrTalk(
        0xFE,
        (
            "迪因兹什么\x01",
            "都还没搞清楚，\x01",
            "就想开始做生意了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "做生意之前的各项\x01",
            "准备工作都是我做的。\x01",
            "真叫人没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243F")

    Jump("loc_29B0")

    label("loc_2444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EB")

    #C0150
    ChrTalk(
        0xFE,
        (
            "不久前，工商协会的老爷子\x01",
            "悄悄来向我问过\x01",
            "迪因兹的现状。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "他以前曾经邀请迪因兹去做干部，\x01",
            "结果却被拒绝了，\x01",
            "看来他仍然为此感到遗憾呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_255F")

    label("loc_24EB")


    #C0152
    ChrTalk(
        0xFE,
        (
            "唔～当时我也觉得\x01",
            "拒绝那个邀请实在\x01",
            "是有点可惜……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "但迪因兹\x01",
            "确实不适合当领导，\x01",
            "所以我觉得现在这样也挺好的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255F")

    Jump("loc_29B0")

    label("loc_2564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25C8")

    #C0154
    ChrTalk(
        0xFE,
        (
            "迪因兹可真是的，\x01",
            "什么正事都不去想。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "作为他的童年好友，\x01",
            "我得好好协助他才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_26ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267A")

    #C0156
    ChrTalk(
        0xFE,
        (
            "如果用苦西红柿来做菜，\x01",
            "味道会很浓郁。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "不过，我不推荐大家\x01",
            "用它来做沙拉之类的\x01",
            "冷菜哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "……因为直接吃的话，\x01",
            "实在是太苦了。\x01",
            "我不太喜欢呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26E8")

    label("loc_267A")


    #C0159
    ChrTalk(
        0xFE,
        (
            "如果用苦西红柿来做菜，\x01",
            "味道会很浓郁。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "但直接吃的话，味道会很苦。\x01",
            "总之，它是一种面向烹饪高手的食材。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E8")

    Jump("loc_29B0")

    label("loc_26ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AD")

    #C0161
    ChrTalk(
        0xFE,
        (
            "为了成功当个露天摊贩，\x01",
            "迪因兹拼命学习了很多蔬菜的知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "可是他根本没有经济头脑，\x01",
            "做生意几乎全靠自己的人缘。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "不过，这也算是一种\x01",
            "只属于迪因兹的特色吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_280F")

    label("loc_27AD")


    #C0164
    ChrTalk(
        0xFE,
        (
            "迪因兹做生意十分诚信，\x01",
            "可是完全没有经济头脑。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "不过，这也算是一种\x01",
            "只属于迪因兹的特色吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280F")

    Jump("loc_29B0")

    label("loc_2814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C8")

    #C0166
    ChrTalk(
        0xFE,
        (
            "刚才来买东西的顾客对我说，\x01",
            "『你们看上去就像一对夫妻』……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "我一直觉得我们只是童年玩伴，\x01",
            "从没想过那方面的事……\x01",
            "现、现在却不由得开始胡思乱想了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_293E")

    label("loc_28C8")


    #C0168
    ChrTalk(
        0xFE,
        (
            "顾客刚刚对我说，\x01",
            "『你们看上去\x01",
            "  就像一对夫妻』。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "……可是迪因兹对这句话\x01",
            "却完全没反应。\x01",
            "真是的，太失礼了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293E")

    Jump("loc_29B0")

    label("loc_2943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29B0")

    #C0170
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的\x01",
            "食材大半都是靠进口的。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "铁路的运输速度非常快，\x01",
            "所以进口货物远比想象中新鲜哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B0")

    TalkEnd(0xFE)
    Return()

    # Function_2_1D40 end

    def Function_3_29B4(): pass

    label("Function_3_29B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29DD")
    Call(0, 29)
    Return()

    label("loc_29DD")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_4C93")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C8E")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "对话")
    MenuCmd(1, 1, "将鱼售出")
    MenuCmd(1, 1, "放弃")
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A45")
    MenuCmd(3, 1, 0x1)

    label("loc_2A45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A77")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2A77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C59")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C4A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B02")
    MenuCmd(1, 1, "斗鱼　　　　　　　时    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AF8")
    Call(2, 6)

    label("loc_2AF8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B58")
    MenuCmd(1, 1, "雪花蟹　　　　　　幻    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4E")
    Call(2, 6)

    label("loc_2B4E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BAE")
    MenuCmd(1, 1, "蓝带神仙鱼　　　　液状物×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA4")
    Call(2, 6)

    label("loc_2BA4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2BAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C04")
    MenuCmd(1, 1, "银伞鱼　　　　　　空    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BFA")
    Call(2, 6)

    label("loc_2BFA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C5A")
    MenuCmd(1, 1, "阿尔摩利卡鲫鱼　　青葱  ×  2")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C50")
    Call(2, 6)

    label("loc_2C50")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CB0")
    MenuCmd(1, 1, "乌龟　　　　　　　粉状物×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA6")
    Call(2, 6)

    label("loc_2CA6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D06")
    MenuCmd(1, 1, "橙河鱼　　　　　　胡萝卜×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CFC")
    Call(2, 6)

    label("loc_2CFC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D5C")
    MenuCmd(1, 1, "岩穴鱼　　　　　　液状物×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D52")
    Call(2, 6)

    label("loc_2D52")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DB2")
    MenuCmd(1, 1, "虹鳟鱼　　　　　　全    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DA8")
    Call(2, 6)

    label("loc_2DA8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E08")
    MenuCmd(1, 1, "食人鱼　　　　　　香草　×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DFE")
    Call(2, 6)

    label("loc_2DFE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E5E")
    MenuCmd(1, 1, "鲤鱼　　　　　　　香叶　×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E54")
    Call(2, 6)

    label("loc_2E54")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EB4")
    MenuCmd(1, 1, "大口鲈鱼　　　　　地    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EAA")
    Call(2, 6)

    label("loc_2EAA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F0A")
    MenuCmd(1, 1, "黑鲑　　　　　　　马铃薯×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F00")
    Call(2, 6)

    label("loc_2F00")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F60")
    MenuCmd(1, 1, "角斗鱼　　　　　　全    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F56")
    Call(2, 6)

    label("loc_2F56")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2FB6")
    MenuCmd(1, 1, "冷水鱼　　　　　　水    × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FAC")
    Call(2, 6)

    label("loc_2FAC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_300C")
    MenuCmd(1, 1, "小鲵　　　　　　　风    × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3002")
    Call(2, 6)

    label("loc_3002")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_300C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3062")
    MenuCmd(1, 1, "鲑鱼　　　　　　　草莓　×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3058")
    Call(2, 6)

    label("loc_3058")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3062")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30B8")
    MenuCmd(1, 1, "金龙鱼　　　　　　火    × 15")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30AE")
    Call(2, 6)

    label("loc_30AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_310E")
    MenuCmd(1, 1, "鳗鲡　　　　　　　珍奇蔬菜×3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3104")
    Call(2, 6)

    label("loc_3104")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_310E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3164")
    MenuCmd(1, 1, "钢壳龟　　　　　　糙米  ×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315A")
    Call(2, 6)

    label("loc_315A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31BA")
    MenuCmd(1, 1, "巨血蟹　　　　　　珍奇蔬菜×3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B0")
    Call(2, 6)

    label("loc_31B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3210")
    MenuCmd(1, 1, "珍珠龙鱼　　　　　味噌  ×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3206")
    Call(2, 6)

    label("loc_3206")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3210")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3266")
    MenuCmd(1, 1, "巨鲶　　　　　　　乳酪制品×4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325C")
    Call(2, 6)

    label("loc_325C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3266")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32BC")
    MenuCmd(1, 1, "金鲑　　　　　　　空    × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B2")
    Call(2, 6)

    label("loc_32B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3312")
    MenuCmd(1, 1, "大鲵　　　　　　　幻    × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3308")
    Call(2, 6)

    label("loc_3308")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3312")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3368")
    MenuCmd(1, 1, "锦鲤　　　　　　　全    × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335E")
    Call(2, 6)

    label("loc_335E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33BE")
    MenuCmd(1, 1, "翠耀神仙鱼　　　　风    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B4")
    Call(2, 6)

    label("loc_33B4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3414")
    MenuCmd(1, 1, "琥耀岩穴鱼　　　　地    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340A")
    Call(2, 6)

    label("loc_340A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3414")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_346A")
    MenuCmd(1, 1, "红耀食人鱼　　　　火    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3460")
    Call(2, 6)

    label("loc_3460")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_346A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34C0")
    MenuCmd(1, 1, "苍耀巨龙鱼　　　　水    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B6")
    Call(2, 6)

    label("loc_34B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_34C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3516")
    MenuCmd(1, 1, "巨骨龙皇鱼　　　　时空幻×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350C")
    Call(2, 6)

    label("loc_350C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3516")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3555")
    Jump("loc_4C45")

    label("loc_3555")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35DC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0172
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I５个时之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_35D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_35DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3646")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0173
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I５个幻之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_363C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3646")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36B0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0174
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个液状物食材\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_36A6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_36B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_371A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3710")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0175
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I５个空之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3710")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_371A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_377E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3774")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0176
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I２个青葱\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3774")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_377E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37E8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37DE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0177
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I４个粉状物食材\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_37DE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_384E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3844")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0178
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I４个胡萝卜\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3844")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_384E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38B8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0179
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个液状物食材\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_38AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_38B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3926")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_391C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0180
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "全部属性的耀晶片各５个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_391C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_398A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3980")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0181
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I４个香草\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3980")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_398A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39EE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0182
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个香叶\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_39E4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_39EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A58")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0183
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I５个地之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3A4E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ABE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0184
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I４个马铃薯\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3AB4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3ABE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B2C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B22")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0185
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "全部属性的耀晶片各５个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3B22")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B96")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B8C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0186
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I10个水之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3B8C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C00")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0187
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I10个风之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3BF6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C64")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0188
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个草莓\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3C5A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CCE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0189
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I15个火之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3CC4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3CCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D36")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0190
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个珍奇蔬菜\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3D2C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D9A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D90")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0191
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个糙米\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3D90")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E02")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0192
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个珍奇蔬菜\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3DF8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E66")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0193
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I３个味噌\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3E5C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ECE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0194
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#20I４个乳酪制品\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3EC4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3ECE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F38")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0195
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I50个空之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3F2E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FA2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F98")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0196
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I20个幻之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_3F98")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3FA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4010")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4006")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0197
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "全部属性的耀晶片各10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4006")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_407B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4071")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0198
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I500个风之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4071")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_407B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40E6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0199
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I500个地之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_40DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4151")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4147")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0200
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I500个火之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4147")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4151")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0201
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I500个水之耀晶片\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_41B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_422B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4221")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0202
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "时、空、幻耀晶片各500个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4221")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_422B")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "交换\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C45")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4333")

    #C0203
    ChrTalk(
        0xFE,
        (
            "这可是条好鱼啊，\x01",
            "而且没准再也钓不上这种鱼了哦……\x01",
            "真的可以卖给我吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4333")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C3B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4424"),
        (1, "loc_4455"),
        (2, "loc_4486"),
        (3, "loc_44BC"),
        (4, "loc_44ED"),
        (5, "loc_4514"),
        (6, "loc_4553"),
        (7, "loc_457A"),
        (8, "loc_45B0"),
        (9, "loc_4678"),
        (10, "loc_469F"),
        (11, "loc_46C6"),
        (12, "loc_46F7"),
        (13, "loc_471E"),
        (14, "loc_47E6"),
        (15, "loc_4819"),
        (16, "loc_484C"),
        (17, "loc_4873"),
        (18, "loc_48A6"),
        (19, "loc_48DC"),
        (20, "loc_4903"),
        (21, "loc_4939"),
        (22, "loc_4960"),
        (23, "loc_499F"),
        (24, "loc_49D2"),
        (25, "loc_4A05"),
        (26, "loc_4ADB"),
        (27, "loc_4B10"),
        (28, "loc_4B45"),
        (29, "loc_4B7A"),
        (30, "loc_4BAF"),
        (SWITCH_DEFAULT, "loc_4C1F"),
    )


    label("loc_4424")


    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×５\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x4, 5)
    SubItemNumber('斗鱼', 1)
    Jump("loc_4C1F")

    label("loc_4455")


    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻之耀晶片×５\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x6, 5)
    SubItemNumber('雪花蟹', 1)
    Jump("loc_4C1F")

    label("loc_4486")


    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '香油'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '蜂蜜糖浆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '百药精酒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber('香油', 1)
    AddItemNumber('蜂蜜糖浆', 1)
    AddItemNumber('百药精酒', 1)
    SubItemNumber('蓝带神仙鱼', 1)
    Jump("loc_4C1F")

    label("loc_44BC")


    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空之耀晶片×５\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x5, 5)
    SubItemNumber('银伞鱼', 1)
    Jump("loc_4C1F")

    label("loc_44ED")


    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '万能青葱'),
            "×２\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('万能青葱', 2)
    SubItemNumber('阿尔摩利卡鲫鱼', 1)
    Jump("loc_4C1F")

    label("loc_4514")


    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '胡椒粒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '热辣椒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '粗碎岩盐'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '新磨小麦粉'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber('胡椒粒', 1)
    AddItemNumber('热辣椒', 1)
    AddItemNumber('粗碎岩盐', 1)
    AddItemNumber('新磨小麦粉', 1)
    SubItemNumber('乌龟', 1)
    Jump("loc_4C1F")

    label("loc_4553")


    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '迷你胡萝卜'),
            "×４\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('迷你胡萝卜', 4)
    SubItemNumber('橙河鱼', 1)
    Jump("loc_4C1F")

    label("loc_457A")


    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '香油'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '蜂蜜糖浆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '百药精酒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber('香油', 1)
    AddItemNumber('蜂蜜糖浆', 1)
    AddItemNumber('百药精酒', 1)
    SubItemNumber('岩穴鱼', 1)
    Jump("loc_4C1F")

    label("loc_45B0")


    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×５\x01\x07\x02",

            "#57I水之耀晶片×５\x01\x07\x02",

            "#58I火之耀晶片×５\x01\x07\x02",

            "#59I风之耀晶片×５\x01\x07\x02",

            "#60I时之耀晶片×５\x01\x07\x02",

            "#61I空之耀晶片×５\x01\x07\x02",

            "#62I幻之耀晶片×５\x01\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber('虹鳟鱼', 1)
    Jump("loc_4C1F")

    label("loc_4678")


    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '清绿香草'),
            "×４\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('清绿香草', 4)
    SubItemNumber('食人鱼', 1)
    Jump("loc_4C1F")

    label("loc_469F")


    #A0214
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '朝摘香叶'),
            "×３\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('朝摘香叶', 3)
    SubItemNumber('鲤鱼', 1)
    Jump("loc_4C1F")

    label("loc_46C6")


    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×５\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 5)
    SubItemNumber('大口鲈鱼', 1)
    Jump("loc_4C1F")

    label("loc_46F7")


    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '国王马铃薯'),
            "×４\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('国王马铃薯', 4)
    SubItemNumber('黑鲑', 1)
    Jump("loc_4C1F")

    label("loc_471E")


    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×５\x01\x07\x02",

            "#57I水之耀晶片×５\x01\x07\x02",

            "#58I火之耀晶片×５\x01\x07\x02",

            "#59I风之耀晶片×５\x01\x07\x02",

            "#60I时之耀晶片×５\x01\x07\x02",

            "#61I空之耀晶片×５\x01\x07\x02",

            "#62I幻之耀晶片×５\x01\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber('角斗鱼', 1)
    Jump("loc_4C1F")

    label("loc_47E6")


    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber('冷水鱼', 1)
    Jump("loc_4C1F")

    label("loc_4819")


    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I风之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber('小鲵', 1)
    Jump("loc_4C1F")

    label("loc_484C")


    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '铃铛草莓'),
            "×３\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('铃铛草莓', 3)
    SubItemNumber('鲑鱼', 1)
    Jump("loc_4C1F")

    label("loc_4873")


    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火之耀晶片×１５\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x2, 15)
    SubItemNumber('金龙鱼', 1)
    Jump("loc_4C1F")

    label("loc_48A6")


    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '黑暗菇'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '七彩豆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber('黑暗菇', 1)
    AddItemNumber('七彩豆', 1)
    AddItemNumber('苦西红柿', 1)
    SubItemNumber('鳗鲡', 1)
    Jump("loc_4C1F")

    label("loc_48DC")


    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '发芽糙米'),
            "×３\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('发芽糙米', 3)
    SubItemNumber('钢壳龟', 1)
    Jump("loc_4C1F")

    label("loc_4903")


    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '黑暗菇'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '七彩豆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber('黑暗菇', 1)
    AddItemNumber('七彩豆', 1)
    AddItemNumber('苦西红柿', 1)
    SubItemNumber('巨血蟹', 1)
    Jump("loc_4C1F")

    label("loc_4939")


    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '五谷味噌'),
            "×３\x07\x00",
            "获得了。\x02",
        )
    )

    AddItemNumber('五谷味噌', 3)
    SubItemNumber('珍珠龙鱼', 1)
    Jump("loc_4C1F")

    label("loc_4960")


    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '新鲜牛奶'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '新鲜奶酪'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '新鲜鸡蛋'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '雪花里脊肉'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    AddItemNumber('新鲜牛奶', 1)
    AddItemNumber('新鲜奶酪', 1)
    AddItemNumber('新鲜鸡蛋', 1)
    AddItemNumber('雪花里脊肉', 1)
    SubItemNumber('巨鲶', 1)
    Jump("loc_4C1F")

    label("loc_499F")


    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空之耀晶片×５０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber('金鲑', 1)
    Jump("loc_4C1F")

    label("loc_49D2")


    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber('大鲵', 1)
    Jump("loc_4C1F")

    label("loc_4A05")


    #A0229
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×１０\x01\x07\x02",

            "#57I水之耀晶片×１０\x01\x07\x02",

            "#58I火之耀晶片×１０\x01\x07\x02",

            "#59I风之耀晶片×１０\x01\x07\x02",

            "#60I时之耀晶片×１０\x01\x07\x02",

            "#61I空之耀晶片×１０\x01\x07\x02",

            "#62I幻之耀晶片×１０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 10)
    AddSepith(0x1, 10)
    AddSepith(0x2, 10)
    AddSepith(0x3, 10)
    AddSepith(0x4, 10)
    AddSepith(0x5, 10)
    AddSepith(0x6, 10)
    SubItemNumber('锦鲤', 1)
    Jump("loc_4C1F")

    label("loc_4ADB")


    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I风之耀晶片×５００\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x3, 500)
    SubItemNumber('翠耀神仙鱼', 1)
    Jump("loc_4C1F")

    label("loc_4B10")


    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×５００\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 500)
    SubItemNumber('琥耀岩穴鱼', 1)
    Jump("loc_4C1F")

    label("loc_4B45")


    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火之耀晶片×５００\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x2, 500)
    SubItemNumber('红耀食人鱼', 1)
    Jump("loc_4C1F")

    label("loc_4B7A")


    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水之耀晶片×５００\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x1, 500)
    SubItemNumber('苍耀巨龙鱼', 1)
    Jump("loc_4C1F")

    label("loc_4BAF")


    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×５００\x01\x07\x02",

            "#61I空之耀晶片×５００\x01\x07\x02",

            "#62I幻之耀晶片×５００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x4, 500)
    AddSepith(0x5, 500)
    AddSepith(0x6, 500)
    SubItemNumber('巨骨龙皇鱼', 1)
    Jump("loc_4C1F")

    label("loc_4C1F")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C45")

    label("loc_4C3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C45")

    Jump("loc_2A90")

    label("loc_4C4A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C89")

    label("loc_4C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C6D")
    Jump("loc_4C89")

    label("loc_4C6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C89")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(2, 4)

    label("loc_4C89")

    Jump("loc_29F9")

    label("loc_4C8E")

    Jump("loc_4C96")

    label("loc_4C93")

    Call(2, 4)

    label("loc_4C96")

    TalkEnd(0xB)
    Return()

    # Function_3_29B4 end

    def Function_4_4C9A(): pass

    label("Function_4_4C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D57")

    #C0235
    ChrTalk(
        0xFE,
        (
            "突然出现了一棵莫名其妙的大树，\x01",
            "老公会担心也是当然的……\x01",
            "可真没想到他会陪我一起出摊。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "呵呵，这确实让我安心多了。\x01",
            "干脆我们夫妻以后就\x01",
            "一起经营这个摊子吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DC3")

    label("loc_4D57")


    #C0237
    ChrTalk(
        0xFE,
        (
            "我老公的工作原本是从国外采购鱼类，\x01",
            "但他现在已经失业了……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "干脆我们夫妻以后就\x01",
            "一起经营这个摊子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DC3")

    Jump("loc_5827")

    label("loc_4DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4DD6")
    Jump("loc_5827")

    label("loc_4DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E7D")

    #C0239
    ChrTalk(
        0xFE,
        (
            "我联络了正在国外工作的老公，\x01",
            "让他快点回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "因为我听说过了今天，\x01",
            "铁路列车就会\x01",
            "暂时停止运营。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "唉，也不知道他能否\x01",
            "顺利回来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EA4")

    label("loc_4E7D")


    #C0242
    ChrTalk(
        0xFE,
        (
            "哎呀，真希望我老公\x01",
            "能赶快回来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA4")

    Jump("loc_5827")

    label("loc_4EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4F2E")

    #C0243
    ChrTalk(
        0xFE,
        (
            "听说以前在这附近\x01",
            "胡闹的红衣孩子们\x01",
            "在之前那起袭击事件中受伤了。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "唉～真担心他们啊……\x01",
            "希望他们能早日恢复健康。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_4F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4F6E")

    #C0245
    ChrTalk(
        0xFE,
        "竟然会发生这种事……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "唉～真让人不安……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_4F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5006")

    #C0247
    ChrTalk(
        0xFE,
        (
            "今天早上，有游击士\x01",
            "来打听消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "据说有两位女游击士\x01",
            "不知跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "今天的天气这么差，\x01",
            "她们到底去哪里了呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_505E")

    label("loc_5006")


    #C0250
    ChrTalk(
        0xFE,
        (
            "听说有两位女游击士\x01",
            "不知跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "今天的天气这么差，\x01",
            "她们到底去哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_505E")

    Jump("loc_5827")

    label("loc_5063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_50B2")

    #C0252
    ChrTalk(
        0xFE,
        (
            "我老公去共和国\x01",
            "采购海鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "不知他有没有进到不错的货。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_50B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_51C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5169")

    #C0254
    ChrTalk(
        0xFE,
        (
            "很多淡水鱼\x01",
            "如果直接食用，\x01",
            "会有一股土腥味。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "所以最好\x01",
            "先用牛奶浸泡一下，\x01",
            "除掉那股腥味。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "和能直接烹饪的\x01",
            "海水鱼相比，\x01",
            "淡水鱼的烹调过程比较麻烦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_51BF")

    label("loc_5169")


    #C0257
    ChrTalk(
        0xFE,
        (
            "淡水鱼最好先用牛奶\x01",
            "浸泡一下，除掉腥味。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "在家里做菜时，\x01",
            "可以试试这个方法哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51BF")

    Jump("loc_5827")

    label("loc_51C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B7")

    #C0259
    ChrTalk(
        0xFE,
        (
            "按规定，克洛斯贝尔\x01",
            "需向帝国和共和国\x01",
            "缴纳约１０％的税收。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "如果克洛斯贝尔能独立，\x01",
            "那项规定就会失去效力，\x01",
            "我们的生活也会变得更好。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "当然了，这样一来，\x01",
            "安全保障方面可能会出问题……\x01",
            "但我还是希望能成功独立。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_531C")

    label("loc_52B7")


    #C0262
    ChrTalk(
        0xFE,
        (
            "我也赞成\x01",
            "克洛斯贝尔独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "如果能摆脱那毫无公平可言的\x01",
            "税收规定，我们的生活一定能\x01",
            "变得更好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_531C")

    Jump("loc_5827")

    label("loc_5321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_548B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5443")

    #C0264
    ChrTalk(
        0xFE,
        (
            "据说帝国的宰相是个\x01",
            "相当精明的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "都说吃鱼\x01",
            "会变聪明……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "他肯定是从小吃鱼\x01",
            "长大的吧。\x02",
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

    #C0267
    ChrTalk(
        0x101,
        (
            "#00000F……脑海中不由得\x01",
            "浮现出了一幅十分\x01",
            "平民化的画面呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5486")

    label("loc_5443")


    #C0268
    ChrTalk(
        0xFE,
        (
            "都说吃鱼\x01",
            "会变聪明。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "帝国的宰相\x01",
            "肯定是从小吃鱼\x01",
            "长大的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5486")

    Jump("loc_5827")

    label("loc_548B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_55BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5540")

    #C0270
    ChrTalk(
        0xFE,
        (
            "听说边境大门的警备力度\x01",
            "有了明显加强。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "那些从共和国而来的采购商\x01",
            "都在抱怨，说办理入境手续\x01",
            "实在是太浪费时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "各国首脑来访的影响\x01",
            "还真大呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_55B7")

    label("loc_5540")


    #C0273
    ChrTalk(
        0xFE,
        (
            "那些从共和国而来的采购商\x01",
            "都在抱怨，说办理入境手续\x01",
            "实在是太浪费时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "看来边境大门的警备力度\x01",
            "有了明显加强。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55B7")

    Jump("loc_5827")

    label("loc_55BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_56EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5681")

    #C0275
    ChrTalk(
        0xFE,
        (
            "搬进钓公师团那栋房子里的，\x01",
            "是叫……『钓皇俱乐部』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "我本来还以为他们\x01",
            "跟之前那个『钓公师团』\x01",
            "没什么差别……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "可是他们几乎不跟邻里来往，\x01",
            "总觉得有点可疑呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_56EA")

    label("loc_5681")


    #C0278
    ChrTalk(
        0xFE,
        (
            "『钓皇俱乐部』……\x01",
            "总觉得有点可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "不过他们好像只是个\x01",
            "钓鱼爱好者团体，\x01",
            "应该不会是些坏人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56EA")

    Jump("loc_5827")

    label("loc_56EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5752")

    #C0280
    ChrTalk(
        0xFE,
        (
            "嗯～今天天气\x01",
            "还真有点糟。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "不过，还不到\x01",
            "需要收摊的程度。\x01",
            "你们就随便看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_5752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D3")

    #C0282
    ChrTalk(
        0xFE,
        "需要新鲜的鱼吗～？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "最近都没看到\x01",
            "钓公师团的那些人。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        "……他们到哪里去了呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5827")

    label("loc_57D3")


    #C0285
    ChrTalk(
        0xFE,
        (
            "钓公师团的那帮人\x01",
            "到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "见不到那些有趣的人，\x01",
            "还真让人有点寂寞啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5827")

    Return()

    # Function_4_4C9A end

    def Function_5_5828(): pass

    label("Function_5_5828")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5836")
    SetScenarioFlags(0x2, 3)

    label("loc_5836")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_5844")
    SetScenarioFlags(0x2, 3)

    label("loc_5844")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5852")
    SetScenarioFlags(0x2, 3)

    label("loc_5852")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5860")
    SetScenarioFlags(0x2, 3)

    label("loc_5860")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_586E")
    SetScenarioFlags(0x2, 3)

    label("loc_586E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_587C")
    SetScenarioFlags(0x2, 3)

    label("loc_587C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_588A")
    SetScenarioFlags(0x2, 3)

    label("loc_588A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5898")
    SetScenarioFlags(0x2, 3)

    label("loc_5898")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_58A6")
    SetScenarioFlags(0x2, 3)

    label("loc_58A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_58B4")
    SetScenarioFlags(0x2, 3)

    label("loc_58B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_58C2")
    SetScenarioFlags(0x2, 3)

    label("loc_58C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_58D0")
    SetScenarioFlags(0x2, 3)

    label("loc_58D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_58DE")
    SetScenarioFlags(0x2, 3)

    label("loc_58DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_58EC")
    SetScenarioFlags(0x2, 3)

    label("loc_58EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_58FA")
    SetScenarioFlags(0x2, 3)

    label("loc_58FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_5908")
    SetScenarioFlags(0x2, 3)

    label("loc_5908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5916")
    SetScenarioFlags(0x2, 3)

    label("loc_5916")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5924")
    SetScenarioFlags(0x2, 3)

    label("loc_5924")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_5932")
    SetScenarioFlags(0x2, 3)

    label("loc_5932")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_5940")
    SetScenarioFlags(0x2, 3)

    label("loc_5940")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_594E")
    SetScenarioFlags(0x2, 3)

    label("loc_594E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_595C")
    SetScenarioFlags(0x2, 3)

    label("loc_595C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_596A")
    SetScenarioFlags(0x2, 3)

    label("loc_596A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_5978")
    SetScenarioFlags(0x2, 3)

    label("loc_5978")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_5986")
    SetScenarioFlags(0x2, 3)

    label("loc_5986")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_5994")
    SetScenarioFlags(0x2, 3)

    label("loc_5994")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_59A2")
    SetScenarioFlags(0x2, 3)

    label("loc_59A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_59B0")
    SetScenarioFlags(0x2, 3)

    label("loc_59B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_59BE")
    SetScenarioFlags(0x2, 3)

    label("loc_59BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_59CC")
    SetScenarioFlags(0x2, 3)

    label("loc_59CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_59DA")
    SetScenarioFlags(0x2, 3)

    label("loc_59DA")

    Return()

    # Function_5_5828 end

    def Function_6_59DB(): pass

    label("Function_6_59DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59EE")
    MenuCmd(3, 1, 0x0)

    label("loc_59EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A01")
    MenuCmd(3, 1, 0x1)

    label("loc_5A01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A14")
    MenuCmd(3, 1, 0x2)

    label("loc_5A14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A27")
    MenuCmd(3, 1, 0x3)

    label("loc_5A27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A3A")
    MenuCmd(3, 1, 0x4)

    label("loc_5A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4D")
    MenuCmd(3, 1, 0x5)

    label("loc_5A4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A60")
    MenuCmd(3, 1, 0x6)

    label("loc_5A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A73")
    MenuCmd(3, 1, 0x7)

    label("loc_5A73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A86")
    MenuCmd(3, 1, 0x8)

    label("loc_5A86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A99")
    MenuCmd(3, 1, 0x9)

    label("loc_5A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AAC")
    MenuCmd(3, 1, 0xA)

    label("loc_5AAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ABF")
    MenuCmd(3, 1, 0xB)

    label("loc_5ABF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD2")
    MenuCmd(3, 1, 0xC)

    label("loc_5AD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AE5")
    MenuCmd(3, 1, 0xD)

    label("loc_5AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF8")
    MenuCmd(3, 1, 0xE)

    label("loc_5AF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B0B")
    MenuCmd(3, 1, 0xF)

    label("loc_5B0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B1E")
    MenuCmd(3, 1, 0x10)

    label("loc_5B1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B31")
    MenuCmd(3, 1, 0x11)

    label("loc_5B31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B44")
    MenuCmd(3, 1, 0x12)

    label("loc_5B44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B57")
    MenuCmd(3, 1, 0x13)

    label("loc_5B57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B6A")
    MenuCmd(3, 1, 0x14)

    label("loc_5B6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7D")
    MenuCmd(3, 1, 0x15)

    label("loc_5B7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B90")
    MenuCmd(3, 1, 0x16)

    label("loc_5B90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA3")
    MenuCmd(3, 1, 0x17)

    label("loc_5BA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB6")
    MenuCmd(3, 1, 0x18)

    label("loc_5BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BC9")
    MenuCmd(3, 1, 0x19)

    label("loc_5BC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BDC")
    MenuCmd(3, 1, 0x1A)

    label("loc_5BDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BEF")
    MenuCmd(3, 1, 0x1B)

    label("loc_5BEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C02")
    MenuCmd(3, 1, 0x1C)

    label("loc_5C02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C15")
    MenuCmd(3, 1, 0x1D)

    label("loc_5C15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C28")
    MenuCmd(3, 1, 0x1E)

    label("loc_5C28")

    Return()

    # Function_6_59DB end

    def Function_7_5C29(): pass

    label("Function_7_5C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC0")

    #C0287
    ChrTalk(
        0xFE,
        (
            "听说迪塔总统\x01",
            "被捕了！\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "一国元首竟然被捕，\x01",
            "这可是前所未闻的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州今后\x01",
            "究竟会变成什么样呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D1E")

    label("loc_5CC0")


    #C0290
    ChrTalk(
        0xFE,
        (
            "一国元首竟然被捕，\x01",
            "这可是前所未闻的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州今后\x01",
            "究竟会变成什么样呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D1E")

    Jump("loc_6404")

    label("loc_5D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5D31")
    Jump("loc_6404")

    label("loc_5D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5DB2")

    #C0292
    ChrTalk(
        0xFE,
        (
            "大婶我也观看了迪塔市长……\x01",
            "不对，是迪塔总统的演讲。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "既然迈出了这一步，\x01",
            "希望他能为独立\x01",
            "努力拼搏到最后啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_5DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5E3F")

    #C0294
    ChrTalk(
        0xFE,
        (
            "中央广场的大钟\x01",
            "好像被人偷走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "到底为什么会去\x01",
            "偷那种东西呢，\x01",
            "至今都还没有可信的说法。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "唉，总觉得这件事怪怪的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_5E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5EAF")

    #C0297
    ChrTalk(
        0xFE,
        "真担心矿山镇的情况啊……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "听说警备队已经开始\x01",
            "着手解决这次的事件了，\x01",
            "镇上的人不要紧吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_5EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F19")

    #C0299
    ChrTalk(
        0xFE,
        (
            "昨天的列车事故\x01",
            "真是吓了我一大跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "不管怎么说，能这么快就\x01",
            "完成修复，实在是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_5F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5F92")

    #C0301
    ChrTalk(
        0xFE,
        (
            "刚刚有一辆共和国的\x01",
            "旅客巴士从这里经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "真奇怪啊……\x01",
            "我记得那辆巴士只开到\x01",
            "东出口的巴士停靠站啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_5F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601E")

    #C0303
    ChrTalk(
        0xFE,
        (
            "独立提案似乎是市长\x01",
            "酝酿已久的计划……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "不知麦克道尔议长\x01",
            "对这件事有什么看法。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "真想听听\x01",
            "他的意见啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_607F")

    label("loc_601E")


    #C0306
    ChrTalk(
        0xFE,
        (
            "大婶我还在犹豫，\x01",
            "不知该投赞成票\x01",
            "还是反对票。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "这种时候，真想听听麦克道尔\x01",
            "议长的意见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_607F")

    Jump("loc_6404")

    label("loc_6084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6128")

    #C0308
    ChrTalk(
        0xFE,
        (
            "连大婶我都被市长的\x01",
            "独立提案吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "不过，我也觉得克洛斯贝尔\x01",
            "应该更有国际地位。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "毕竟这里是大陆首屈一指的\x01",
            "贸易都市啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_617C")

    label("loc_6128")


    #C0311
    ChrTalk(
        0xFE,
        (
            "我觉得克洛斯贝尔应该\x01",
            "更有国际地位。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "毕竟这里是大陆首屈一指的\x01",
            "贸易都市啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617C")

    Jump("loc_6404")

    label("loc_6181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61E3")

    #C0313
    ChrTalk(
        0xFE,
        "正式会议终于要在今天召开了。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "希望迪塔市长他们\x01",
            "能为克洛斯贝尔市\x01",
            "努力加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_61E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6235")

    #C0315
    ChrTalk(
        0xFE,
        (
            "兰花塔的揭幕式\x01",
            "实在是太壮观了。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "大婶我被震撼得\x01",
            "腿都软了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_6235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_628D")

    #C0317
    ChrTalk(
        0xFE,
        (
            "今天总能看见那些\x01",
            "执勤中的警察呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "大街上也飘着\x01",
            "一股浮躁的气息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_628D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_62E7")

    #C0319
    ChrTalk(
        0xFE,
        (
            "呵呵呵呵呵～¤\x01",
            "大婶我从小就\x01",
            "喜欢下雨天呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "……是不是有些孩子气？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6404")

    label("loc_62E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A6")

    #C0321
    ChrTalk(
        0xFE,
        (
            "据说这个月底要召开什么\x01",
            "『通商会议』。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "不仅是帝国和共和国，\x01",
            "连利贝尔和雷米菲利亚的大人物们\x01",
            "也都会到克洛斯贝尔来。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "……看来那会是个\x01",
            "相当大型的活动呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6404")

    label("loc_63A6")


    #C0324
    ChrTalk(
        0xFE,
        (
            "据说这个月底要召开什么\x01",
            "『通商会议』。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "有好多大人物都要来，\x01",
            "看来会是一场大型活动呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6404")

    TalkEnd(0xFE)
    Return()

    # Function_7_5C29 end

    def Function_8_6408(): pass

    label("Function_8_6408")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_64AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_647C")

    #C0326
    ChrTalk(
        0xFE,
        (
            "就算没有迪塔总统，\x01",
            "我们也还有麦克道尔议长。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "议长一定能带我们\x01",
            "走出这种困境。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64A9")

    label("loc_647C")


    #C0328
    ChrTalk(
        0xFE,
        (
            "麦克道尔议长一定能\x01",
            "带我们走出这种困境。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64A9")

    Jump("loc_6EF1")

    label("loc_64AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_64BC")
    Jump("loc_6EF1")

    label("loc_64BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_65D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6562")

    #C0329
    ChrTalk(
        0xFE,
        (
            "真没想到，竟会任命游击士\x01",
            "亚里欧斯阁下出任国防长官。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "不过，考虑到他的功绩，\x01",
            "也许还真是个适当的人选呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "真不愧是\x01",
            "迪塔阁下啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_65CC")

    label("loc_6562")


    #C0332
    ChrTalk(
        0xFE,
        (
            "考虑到亚里欧斯阁下的功绩，\x01",
            "他的确适合担任国防长官一职。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "毕竟他是人称克洛斯贝尔\x01",
            "守护神的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65CC")

    Jump("loc_6EF1")

    label("loc_65D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_66FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6686")

    #C0334
    ChrTalk(
        0xFE,
        (
            "没想到克洛斯贝尔\x01",
            "竟然会发生\x01",
            "那种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "从旧城区传来的那个巨鬼般\x01",
            "怪物的吼叫声，至今仍然\x01",
            "回荡在我耳边，挥之不去。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        "唉……看来今晚也睡不着了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66F6")

    label("loc_6686")


    #C0337
    ChrTalk(
        0xFE,
        (
            "袭击事件时传来的那个巨鬼般\x01",
            "怪物的吼叫声，至今仍然\x01",
            "回荡在我耳边，挥之不去。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        "唉……看来今晚也睡不着了。\x02",
    )

    CloseMessageWindow()

    label("loc_66F6")

    Jump("loc_6EF1")

    label("loc_66FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_682D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67B7")

    #C0339
    ChrTalk(
        0xFE,
        (
            "玛因兹被占领了吗……\x01",
            "这可真是\x01",
            "出了大事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "市长刚刚发表了独立提案，\x01",
            "帝国和共和国现在也\x01",
            "不可能对我们伸出援手了……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "唔唔，玛因兹究竟会\x01",
            "怎么样呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6828")

    label("loc_67B7")


    #C0342
    ChrTalk(
        0xFE,
        (
            "市长刚刚发表了独立提案，\x01",
            "帝国和共和国现在也\x01",
            "不可能对我们伸出援手了……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "唔唔，玛因兹究竟会\x01",
            "怎么样呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6828")

    Jump("loc_6EF1")

    label("loc_682D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_683B")
    Jump("loc_6EF1")

    label("loc_683B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6897")

    #C0344
    ChrTalk(
        0xFE,
        (
            "刚才好像有急救车\x01",
            "从中央广场开过。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "怎么回事……\x01",
            "是不是出了什么事故？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EF1")

    label("loc_6897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_69E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694D")

    #C0346
    ChrTalk(
        0xFE,
        (
            "关于这次的居民投票……\x01",
            "我的朋友们也都在\x01",
            "热烈谈论。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "但是，一定不能被\x01",
            "他人的意见影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "毕竟这是关系到\x01",
            "我们每个人的大事，\x01",
            "一定要好好考虑清楚。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69DF")

    label("loc_694D")


    #C0349
    ChrTalk(
        0xFE,
        (
            "每个人都要在深思熟虑之后，\x01",
            "遵循自己的想法做出选择，\x01",
            "否则的话，投票就毫无意义了。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "毕竟这是关系到\x01",
            "我们每个人的大事，\x01",
            "一定要好好考虑清楚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69DF")

    Jump("loc_6EF1")

    label("loc_69E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AA4")

    #C0351
    ChrTalk(
        0xFE,
        (
            "作为熟知此地历史的人，\x01",
            "我无论如何都希望\x01",
            "能够成功独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "但事实上，我们正是因为\x01",
            "在帝国和共和国的支配之下，\x01",
            "才能保持和平……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "有必要仔细思考啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6B02")

    label("loc_6AA4")


    #C0354
    ChrTalk(
        0xFE,
        (
            "是甘当从属州，享受和平，\x01",
            "还是放弃和平，成为独立国家……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "有必要仔细思考啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B02")

    Jump("loc_6EF1")

    label("loc_6B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB2")

    #C0356
    ChrTalk(
        0xFE,
        (
            "听说从今早开始，\x01",
            "兰花塔一带\x01",
            "就被封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "我本来还想亲眼看看\x01",
            "来自各国的首脑人物呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "但考虑到他们的安全问题，\x01",
            "这也是无可奈何的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6C0E")

    label("loc_6BB2")


    #C0359
    ChrTalk(
        0xFE,
        (
            "听说从今早开始，\x01",
            "兰花塔周围就被封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "我本来还想亲眼看看\x01",
            "来自各国的首脑人物呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C0E")

    Jump("loc_6EF1")

    label("loc_6C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE3")

    #C0361
    ChrTalk(
        0xFE,
        (
            "洛克史密斯总统的轿车\x01",
            "刚刚从这条路经过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "真不愧是总统的座驾啊，\x01",
            "以白色和金色为主色调，\x01",
            "看上去真是豪华得惊人。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "哪怕找遍整个大陆，\x01",
            "恐怕也找不到几辆那么\x01",
            "豪华的轿车吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D50")

    label("loc_6CE3")


    #C0364
    ChrTalk(
        0xFE,
        (
            "洛克史密斯总统的轿车\x01",
            "实在是豪华得不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "哪怕找遍整个大陆，\x01",
            "恐怕也找不到几辆那么\x01",
            "豪华的轿车吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D50")

    Jump("loc_6EF1")

    label("loc_6D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6DC9")

    #C0366
    ChrTalk(
        0xFE,
        (
            "听说各国的首脑\x01",
            "明天就要来到\x01",
            "克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "这可是难得的机会，\x01",
            "如果能亲眼看看\x01",
            "他们就太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EF1")

    label("loc_6DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6DD7")
    Jump("loc_6EF1")

    label("loc_6DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6EF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E82")

    #C0368
    ChrTalk(
        0xFE,
        (
            "听说迪塔新市长和\x01",
            "麦克道尔议长正在\x01",
            "齐心协力地处理政务。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "市长和议长竟能齐心协力，\x01",
            "这种事情在以前真是连想都不敢想。\x01",
            "呵呵，真是件好事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6EF1")

    label("loc_6E82")


    #C0370
    ChrTalk(
        0xFE,
        (
            "迪塔新市长坐在\x01",
            "ＩＢＣ总裁这个位子上时，\x01",
            "就展示了非常高明的手腕。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "呵呵，他今后的表现\x01",
            "真是令人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF1")

    TalkEnd(0xFE)
    Return()

    # Function_8_6408 end

    def Function_9_6EF5(): pass

    label("Function_9_6EF5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FD7")
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0372
    ChrTalk(
        0xFE,
        (
            "总统遭到拘捕，\x01",
            "随后又出现了奇怪的蓝色大树……\x01",
            "接连不断地发生了很多事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "我们还能恢复\x01",
            "过去的生活吗……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0374
    ChrTalk(
        0x10,
        "哥哥，你怎么了～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    #C0375
    ChrTalk(
        0xFE,
        "哈哈，没什么。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0xF, 0x10E, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_703B")

    label("loc_6FD7")


    #C0376
    ChrTalk(
        0xFE,
        "……算了，还是顺其自然吧。\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "对我来说，最重要的事情\x01",
            "是保护好梅琳……\x01",
            "只要谨记这一点就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_703B")

    Jump("loc_7B8B")

    label("loc_7040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_704E")
    Jump("loc_7B8B")

    label("loc_704E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_719D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_710A")

    #C0378
    ChrTalk(
        0xFE,
        (
            "要是被帝国和共和国\x01",
            "给盯上，\x01",
            "确实十分可怕……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "可是……为了克洛斯贝尔，\x01",
            "我们市民也必须要下定决心。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "而且，无论发生什么事，\x01",
            "我都一定会保护好\x01",
            "梅琳的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7198")

    label("loc_710A")


    #C0381
    ChrTalk(
        0xFE,
        (
            "我拜托库隆克先生允许我\x01",
            "在工作时把梅琳带在身边，\x01",
            "他很爽快地就答应了。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "真是个通情达理的人啊。\x01",
            "能把梅琳带在身边，\x01",
            "我也就可以安下心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7198")

    Jump("loc_7B8B")

    label("loc_719D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_71AB")
    Jump("loc_7B8B")

    label("loc_71AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_72CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7253")

    #C0383
    ChrTalk(
        0xFE,
        (
            "听说玛因兹那边\x01",
            "出现了武装集团。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "镇上竟然会出现那种危险人物，\x01",
            "那里的人肯定十分惊慌吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "真希望警备队能尽快\x01",
            "把那些家伙赶走啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_72C5")

    label("loc_7253")


    #C0386
    ChrTalk(
        0xFE,
        (
            "梅琳现在在做什么呢……\x01",
            "最近这么乱，真担心她啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "拜托库隆克先生让我今天早点收工，\x01",
            "然后和她一起回家吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72C5")

    Jump("loc_7B8B")

    label("loc_72CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_739B")

    #C0388
    ChrTalk(
        0xFE,
        (
            "我把打工时\x01",
            "做的风车失败品\x01",
            "送给了梅琳。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "结果她今天就吵着\x01",
            "要把那东西拿出来玩，\x01",
            "完全不听人劝。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "说实话，我实在\x01",
            "不想在下雨天出门……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "……算了，只要梅琳\x01",
            "觉得高兴就好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7401")

    label("loc_739B")


    #C0392
    ChrTalk(
        0xFE,
        (
            "话说回来，她竟然会\x01",
            "因那种和废品一样的\x01",
            "失败品而感到高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "……下次一定\x01",
            "要做个更好的\x01",
            "送给她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7401")

    Jump("loc_7B8B")

    label("loc_7406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7472")

    #C0394
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "我做的风车\x01",
            "完全卖不出去啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "哎，等等！？\x01",
            "什么时候卖出去了！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7484")

    label("loc_7472")


    #C0396
    ChrTalk(
        0xFE,
        "（呆住）……\x02",
    )

    CloseMessageWindow()

    label("loc_7484")

    Jump("loc_7B8B")

    label("loc_7489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7507")

    #C0397
    ChrTalk(
        0xFE,
        (
            "在我的努力之下，\x01",
            "终于有一个风车\x01",
            "能摆在店面出售了。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "看到自己做出来的东西\x01",
            "被摆在店面……\x01",
            "真让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B8B")

    label("loc_7507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B7")

    #C0399
    ChrTalk(
        0xFE,
        (
            "库隆克先生好厉害，\x01",
            "竟然能做出\x01",
            "那么棒的模型……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "我原本也对自己的动手能力\x01",
            "挺有自信，但现在却\x01",
            "连个风车都做不好……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "唉，都快没有\x01",
            "信心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_75FF")

    label("loc_75B7")


    #C0402
    ChrTalk(
        0xFE,
        (
            "总之，今天还是\x01",
            "先把杂事做好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "自己赚钱可真不容易呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75FF")

    Jump("loc_7B8B")

    label("loc_7604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_76FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_769F")

    #C0404
    ChrTalk(
        0xFE,
        (
            "我向库隆克先生提出请求后，\x01",
            "他居然很爽快地\x01",
            "同意让我在这里工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "唔～唔……\x01",
            "早知如此，我一开始就该去\x01",
            "露天摊找工作了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_76F6")

    label("loc_769F")


    #C0406
    ChrTalk(
        0xFE,
        (
            "简单工艺品的制作方法\x01",
            "以及资金的管理……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "我得一点一点地记住这些工作内容才行。\x02",
    )

    CloseMessageWindow()

    label("loc_76F6")

    Jump("loc_7B8B")

    label("loc_76FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_77FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77AA")

    #C0408
    ChrTalk(
        0xFE,
        "唔……制作工艺品吗……\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "我这双手还蛮巧的，\x01",
            "说不定这种靠手艺吃饭的工作\x01",
            "还挺适合我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "……不过，店主会同意\x01",
            "让我在这里工作吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_77FA")

    label("loc_77AA")


    #C0411
    ChrTalk(
        0xFE,
        (
            "如果我能做出这样的风车来，\x01",
            "梅琳一定会很高兴……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "唔，好！\x01",
            "去问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77FA")

    Jump("loc_7B8B")

    label("loc_77FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_794B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D9")
    OP_4B(0x10, 0xFF)

    #C0413
    ChrTalk(
        0xFE,
        (
            "唉，工作可\x01",
            "真不好找啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x10,
        (
            "哥哥，那边有\x01",
            "好多店哦，\x01",
            "你不去问问看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "笨、笨蛋，\x01",
            "在街边小摊工作就要抛头露面，\x01",
            "那也太丢脸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "我想找份能在室内上班的\x01",
            "轻松工作啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_7946")

    label("loc_78D9")


    #C0417
    ChrTalk(
        0xFE,
        (
            "嗯～露天摊吗……\x01",
            "真不是什么好工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "可是除了露天摊之外，\x01",
            "我已经把能想到的工作\x01",
            "全都找了个遍了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7946")

    Jump("loc_7B8B")

    label("loc_794B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_79BD")

    #C0419
    ChrTalk(
        0xFE,
        (
            "今天我和梅琳一起出门\x01",
            "买东西，顺便散了散步。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "真是的……就算在下雨天，\x01",
            "小孩也还是很活泼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B8B")

    label("loc_79BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7B8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A81")

    #C0421
    ChrTalk(
        0xFE,
        (
            "刚才有个红头发的\x01",
            "男人突然跑来烦我。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "还说什么『尽情烦恼吧！这就是青春～！』，\x01",
            "之后就走向中央广场了……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "……总、总觉得那家伙\x01",
            "比我还要散漫啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7AE3")

    label("loc_7A81")


    #C0424
    ChrTalk(
        0xFE,
        (
            "刚刚那个红头发的男人吗？\x01",
            "他往中央广场走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "……总、总觉得是个\x01",
            "比我还要散漫的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE3")

    Jump("loc_7B8B")

    label("loc_7AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B67")

    #C0426
    ChrTalk(
        0xFE,
        (
            "不久前，\x01",
            "我开始找工作了……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "唉，但是都找不到\x01",
            "肯雇用我的\x01",
            "地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        "才刚开始找，就陷入瓶颈了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7B8B")

    label("loc_7B67")


    #C0429
    ChrTalk(
        0xFE,
        (
            "都找不到\x01",
            "肯雇用我的\x01",
            "地方啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B8B")

    TalkEnd(0xFE)
    Return()

    # Function_9_6EF5 end

    def Function_10_7B8F(): pass

    label("Function_10_7B8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7BEC")

    #C0430
    ChrTalk(
        0xFE,
        (
            "哥哥好像在\x01",
            "想心事呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "别想那些复杂的事情了，\x01",
            "来跟梅琳一起玩吧～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8598")

    label("loc_7BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7BFA")
    Jump("loc_8598")

    label("loc_7BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C6E")

    #C0432
    ChrTalk(
        0xFE,
        (
            "哥哥今天让我\x01",
            "在这里给他帮忙～\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "嘿嘿，哥哥做了\x01",
            "三个『转转』呢。\x01",
            "希望能卖出去～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7CB6")

    label("loc_7C6E")


    #C0434
    ChrTalk(
        0xFE,
        (
            "哥哥说，只要梅琳来帮忙，\x01",
            "就能得到\x01",
            "『转转』呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        "嘿嘿，真期待¤\x02",
    )

    CloseMessageWindow()

    label("loc_7CB6")

    Jump("loc_8598")

    label("loc_7CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D20")

    #C0436
    ChrTalk(
        0xFE,
        (
            "爷爷和哥哥都\x01",
            "不知跑到哪里去了～\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "梅琳今天干脆就和\x01",
            "奶奶在家玩吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7D76")

    label("loc_7D20")


    #C0438
    ChrTalk(
        0xFE,
        (
            "爷爷和哥哥一起去做\x01",
            "吃善……纸扇……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "……好像是慈善吧？\x01",
            "他们去做慈善活动了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D76")

    Jump("loc_8598")

    label("loc_7D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0A")

    #C0440
    ChrTalk(
        0xFE,
        (
            "梅琳长大了，明年就要\x01",
            "开始去『主日学校』上学了。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xFE,
        (
            "所以，虽然有点寂寞，\x01",
            "但我还是会给哥哥打气的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_7E22")

    label("loc_7E0A")


    #C0442
    ChrTalk(
        0xFE,
        "哥哥，要加油哦～！\x02",
    )

    CloseMessageWindow()

    label("loc_7E22")

    Jump("loc_8598")

    label("loc_7E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E77")

    #C0443
    ChrTalk(
        0xFE,
        (
            "这个是哥哥做的\x01",
            "『转转』哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        "转呀转呀～¤\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7EAB")

    label("loc_7E77")


    #C0445
    ChrTalk(
        0xFE,
        (
            "这个『转转』是\x01",
            "哥哥做的哦～！\x01",
            "是不是很厉害～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EAB")

    Jump("loc_8598")

    label("loc_7EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7EEB")

    #C0446
    ChrTalk(
        0xFE,
        (
            "爷爷好像\x01",
            "很烦恼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        "……好无聊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8598")

    label("loc_7EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7FB5")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F64")

    #C0448
    ChrTalk(
        0xFE,
        (
            "爷爷～\x01",
            "拉胡子拉胡子～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        "我拉，我拉拉¤\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x14,
        (
            "好痛好痛……\x01",
            "哎呀呀，别拉我的胡子。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7FAC")

    label("loc_7F64")


    #C0451
    ChrTalk(
        0xFE,
        "我拉，我拉拉¤\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x14,
        (
            "没、没想到，\x01",
            "梅琳还挺有力气的……\x01",
            "好痛好痛……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FAC")

    OP_4C(0x14, 0xFF)
    Jump("loc_8598")

    label("loc_7FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_801E")

    #C0453
    ChrTalk(
        0xFE,
        (
            "哥哥正在努力\x01",
            "工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "可是好希望他能\x01",
            "陪梅琳一起玩呀……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_804C")

    label("loc_801E")


    #C0455
    ChrTalk(
        0xFE,
        (
            "哥哥，梅琳想\x01",
            "和你在一起～！\x01",
            "……（抽泣）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_804C")

    Jump("loc_8598")

    label("loc_8051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_80F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80BC")

    #C0456
    ChrTalk(
        0xFE,
        (
            "哥哥现在就在那个\x01",
            "卖『转转』的店里工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "他能找到工作，\x01",
            "真是太好啦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_80F4")

    label("loc_80BC")


    #C0458
    ChrTalk(
        0xFE,
        (
            "虽然很为他高兴……\x01",
            "但又感到有点寂寞。\x01",
            "……（抽泣）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80F4")

    Jump("loc_8598")

    label("loc_80F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8265")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81DF")
    OP_4B(0xF, 0xFF)

    #C0459
    ChrTalk(
        0xFE,
        (
            "一直转个不停，\x01",
            "好有趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        "转呀转呀，转呀转呀……¤\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x10)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0x10, 0)

    #C0461
    ChrTalk(
        0xF,
        (
            "哇啊，梅琳！？\x01",
            "你看这个把自己给看晕了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        "转呀转呀，晕呀晕呀……\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Jump("loc_8260")

    label("loc_81DF")

    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x10, 0)
    TurnDirection(0x10, 0xF, 0)

    #C0463
    ChrTalk(
        0xF,
        "你、你没事吧？梅琳！\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "（摇摇晃晃……）\x01",
            "没、没关系的～\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xF,
        "但看起来可不像没事啊……\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_8260")

    Jump("loc_8598")

    label("loc_8265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_830F")
    OP_4B(0xF, 0xFF)

    #C0466
    ChrTalk(
        0xFE,
        (
            "哥哥最近都没怎么\x01",
            "陪我玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "快点找到工作，\x01",
            "然后陪梅琳玩吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0468
    ChrTalk(
        0xF,
        (
            "唉，要是那么简单\x01",
            "就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_8353")

    label("loc_830F")


    #C0469
    ChrTalk(
        0xFE,
        (
            "梅琳也会帮哥哥\x01",
            "一起找工作的！\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "找到工作后，\x01",
            "就能一起玩了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8353")

    Jump("loc_8598")

    label("loc_8358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_844E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8401")
    OP_4B(0xF, 0xFF)

    #C0471
    ChrTalk(
        0xFE,
        (
            "我看看～我看看……¤\x01",
            "嗯～好香哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xF,
        (
            "喂，梅琳，\x01",
            "现在还不能打开袋子。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xF,
        (
            "这些刚烤好的面包\x01",
            "会被雨打湿的。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        "知道啦～☆\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_8449")

    label("loc_8401")


    #C0475
    ChrTalk(
        0xFE,
        (
            "我刚刚跟哥哥\x01",
            "一起去面包店\x01",
            "买东西了～\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        "嗯～软绵绵，香喷喷的～☆\x02",
    )

    CloseMessageWindow()

    label("loc_8449")

    Jump("loc_8598")

    label("loc_844E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84BB")

    #C0477
    ChrTalk(
        0xFE,
        (
            "刚才有个红头发的人\x01",
            "过来捏了捏哥哥的肩膀。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        "梅琳也要捏一捏哥哥的肩膀～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8598")

    label("loc_84BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8550")
    OP_4B(0xF, 0xFF)

    #C0479
    ChrTalk(
        0xFE,
        "哥哥！打起精神来！\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        (
            "就算哥哥找不到工作，\x01",
            "梅琳也会待在哥哥身边的！\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xF,
        (
            "梅、梅琳……\x01",
            "只有你是站在我这边的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xF, 0xFF)
    Jump("loc_8598")

    label("loc_8550")


    #C0482
    ChrTalk(
        0xFE,
        (
            "哥哥因为找不到工作，\x01",
            "现在很沮丧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "梅琳要好好安慰\x01",
            "哥哥才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8598")

    TalkEnd(0xFE)
    Return()

    # Function_10_7B8F end

    def Function_11_859C(): pass

    label("Function_11_859C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8601")

    #C0484
    ChrTalk(
        0xFE,
        (
            "从刚才开始，就有\x01",
            "好几辆急救车不停地\x01",
            "在市内穿梭。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        "唔唔，有种不好的预感……\x02",
    )

    CloseMessageWindow()
    Jump("loc_871A")

    label("loc_8601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_871A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86BE")

    #C0486
    ChrTalk(
        0xFE,
        (
            "我孙子洛依\x01",
            "终于开始工作了，\x01",
            "而且还是在露天摊……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        (
            "我年轻的时候\x01",
            "也曾在露天摊干过活呢，\x01",
            "真让人感慨万分啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xFE,
        (
            "希望他能\x01",
            "好好努力。\x01",
            "我也会在一旁守护他的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_871A")

    label("loc_86BE")


    #C0489
    ChrTalk(
        0xFE,
        (
            "今天我休假，\x01",
            "所以就由我来\x01",
            "照顾梅琳。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "好吧，机会难得，\x01",
            "我就尽全力来\x01",
            "陪她一起玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_871A")

    TalkEnd(0xFE)
    Return()

    # Function_11_859C end

    def Function_12_871E(): pass

    label("Function_12_871E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87CB")

    #C0491
    ChrTalk(
        0xFE,
        (
            "我家那些男人最近\x01",
            "对我体贴了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "呵呵，都不知多少年\x01",
            "没和基雷一起出来买过东西了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xFE,
        (
            "虽然现在的情况不太妙，\x01",
            "但还是觉得有点高兴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8833")

    label("loc_87CB")


    #C0494
    ChrTalk(
        0xFE,
        (
            "呵呵，都不知多少年\x01",
            "没和基雷一起出来买过东西了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xFE,
        (
            "虽然现在的情况不太妙，\x01",
            "但还是觉得有点高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8833")

    Jump("loc_8DE4")

    label("loc_8838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8846")
    Jump("loc_8DE4")

    label("loc_8846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8854")
    Jump("loc_8DE4")

    label("loc_8854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_897D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8920")

    #C0496
    ChrTalk(
        0xFE,
        (
            "因为前段时间的事件，\x01",
            "我家那些男人工作的地方\x01",
            "全都放假了。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xFE,
        (
            "大家都待在家里，\x01",
            "要做的家务也多了一倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        (
            "不过，跟以前不同的是，\x01",
            "他们现在会帮我做家务了，\x01",
            "真是帮了我大忙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8978")

    label("loc_8920")


    #C0499
    ChrTalk(
        0xFE,
        (
            "大家都待在家里，\x01",
            "要做的家务也多了一倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        (
            "真希望他们工作的地方\x01",
            "都能早日复工啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8978")

    Jump("loc_8DE4")

    label("loc_897D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_898B")
    Jump("loc_8DE4")

    label("loc_898B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8999")
    Jump("loc_8DE4")

    label("loc_8999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8A51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A27")

    #C0501
    ChrTalk(
        0xFE,
        (
            "哎～不用做家务\x01",
            "真是轻松呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        (
            "……这……啊！？\x01",
            "肚子上有赘……肉……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        (
            "……我最近果然\x01",
            "太游手好闲了啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8A4C")

    label("loc_8A27")


    #C0504
    ChrTalk(
        0xFE,
        (
            "差不多也该\x01",
            "重新动手做家务了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A4C")

    Jump("loc_8DE4")

    label("loc_8A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AEB")

    #C0505
    ChrTalk(
        0xFE,
        (
            "我家那群男人最近终于\x01",
            "明白做家务有多辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "他们甚至开口\x01",
            "求我帮他们做家务呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "我的家务罢工运动大获成功。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8B4A")

    label("loc_8AEB")


    #C0508
    ChrTalk(
        0xFE,
        (
            "我家那群男人终于\x01",
            "明白做家务有多辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        (
            "唔～该怎么办呢？\x01",
            "我还想再\x01",
            "轻松一段时间……¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B4A")

    Jump("loc_8DE4")

    label("loc_8B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8B5D")
    Jump("loc_8DE4")

    label("loc_8B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8C92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C27")

    #C0510
    ChrTalk(
        0xFE,
        (
            "自从我不做家务之后，\x01",
            "家里的饭菜还真是\x01",
            "够简单的。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "他们有时还会自作主张地叫外卖，\x01",
            "胡乱花钱……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        (
            "我们家可是个大家庭，\x01",
            "得尽力节省开销……\x01",
            "真是的，男人实在是靠不住。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8C8D")

    label("loc_8C27")


    #C0513
    ChrTalk(
        0xFE,
        (
            "……啊！\x01",
            "我怎么又跑到露天摊了……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        (
            "我已经下定决心，不再做家务了啊，\x01",
            "以后可不能再到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C8D")

    Jump("loc_8DE4")

    label("loc_8C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8CA0")
    Jump("loc_8DE4")

    label("loc_8CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D34")

    #C0515
    ChrTalk(
        0xFE,
        (
            "最近我完全\x01",
            "不做家务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        (
            "日子过得真是超舒服☆\x01",
            "即使待在家里，也什么都不做。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xFE,
        (
            "呵呵，我才不管\x01",
            "什么老公儿子呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8DC8")

    label("loc_8D34")


    #C0518
    ChrTalk(
        0xFE,
        (
            "自从我不做家务之后，\x01",
            "我家那些男人每天都很慌乱。\x01",
            "呵呵，真是活该！\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "……不过，我一出来散步，\x01",
            "就会下意识地来到露天摊。\x01",
            "讨厌，这都成职业病了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DC8")

    Jump("loc_8DE4")

    label("loc_8DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8DDB")
    Jump("loc_8DE4")

    label("loc_8DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8DE4")

    label("loc_8DE4")

    TalkEnd(0xFE)
    Return()

    # Function_12_871E end

    def Function_13_8DE8(): pass

    label("Function_13_8DE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8F03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8ED5")

    #C0520
    ChrTalk(
        0xFE,
        (
            "让妈妈一个人出门，实在是不放心。\x01",
            "所以老爸和我们兄弟几个\x01",
            "决定轮班陪她一起出来买东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        (
            "虽然很麻烦，但我们必须这么做。\x01",
            "要是妈妈受伤了，\x01",
            "我们可就没法活下去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "最近已经彻底认识到\x01",
            "妈妈的重要性了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8EFE")

    label("loc_8ED5")


    #C0523
    ChrTalk(
        0xFE,
        (
            "我们已经彻底认识到\x01",
            "妈妈的重要性了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EFE")

    Jump("loc_9435")

    label("loc_8F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8F11")
    Jump("loc_9435")

    label("loc_8F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8F9B")

    #C0524
    ChrTalk(
        0xFE,
        (
            "哎呀～真是激动人心啊。\x01",
            "没想到克洛斯贝尔竟能\x01",
            "成为独立国家。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "不过，高兴是高兴，\x01",
            "但还不知道今后的\x01",
            "局势会如何发展呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9435")

    label("loc_8F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8FA9")
    Jump("loc_9435")

    label("loc_8FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_90AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9058")

    #C0526
    ChrTalk(
        0xFE,
        (
            "妈妈终于重新开始\x01",
            "做家务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "当、当然了，我们兄弟几个\x01",
            "和爸爸今后也会尽量\x01",
            "帮她分担一些的。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        (
            "我们家可是个大家庭，\x01",
            "大家必须得齐心协力……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_90A5")

    label("loc_9058")


    #C0529
    ChrTalk(
        0xFE,
        (
            "妈妈不做家务的那段日子，\x01",
            "实在过得太艰难了……\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xFE,
        "妈妈果然很伟大啊……\x02",
    )

    CloseMessageWindow()

    label("loc_90A5")

    Jump("loc_9435")

    label("loc_90AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_90B8")
    Jump("loc_9435")

    label("loc_90B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_90C6")
    Jump("loc_9435")

    label("loc_90C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_90D4")
    Jump("loc_9435")

    label("loc_90D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91AE")

    #C0531
    ChrTalk(
        0xFE,
        (
            "自从妈妈不做家务之后，\x01",
            "我们终于切身体会到她从前有多辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        (
            "我们每天都在向妈妈道歉，\x01",
            "可是她怎么都不肯原谅我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "整个城市的人都在讨论独立问题，\x01",
            "我家却有别的大问题等着处理呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9221")

    label("loc_91AE")


    #C0534
    ChrTalk(
        0xFE,
        (
            "我们以前从没帮妈妈做过家务，\x01",
            "这确实是不对。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xFE,
        (
            "总之，现在也只能\x01",
            "老老实实地向妈妈道歉，\x01",
            "直到她原谅我们了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9221")

    Jump("loc_9435")

    label("loc_9226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9234")
    Jump("loc_9435")

    label("loc_9234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C8")

    #C0536
    ChrTalk(
        0xFE,
        (
            "妈妈现在不肯做家务了，\x01",
            "所以老爸和我们兄弟几个\x01",
            "只好分摊负责那堆家务。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xFE,
        (
            "我是负责做饭的。\x01",
            "嗯～该买点什么才好呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_932F")

    label("loc_92C8")


    #C0538
    ChrTalk(
        0xFE,
        (
            "真没想到，考虑每天做什么\x01",
            "饭菜居然如此困难……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        (
            "妈妈每天都在做\x01",
            "这么困难的事啊。\x01",
            "真让人佩服……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_932F")

    Jump("loc_9435")

    label("loc_9334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9342")
    Jump("loc_9435")

    label("loc_9342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9350")
    Jump("loc_9435")

    label("loc_9350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9435")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93EE")

    #C0540
    ChrTalk(
        0xFE,
        (
            "妈妈最近\x01",
            "完全不肯做\x01",
            "家务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xFE,
        (
            "因为爸爸和我们兄弟几个\x01",
            "都不怎么帮她做家务，\x01",
            "结果她就彻底发怒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "这下可麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9435")

    label("loc_93EE")


    #C0543
    ChrTalk(
        0xFE,
        (
            "妈妈彻底发怒了，\x01",
            "现在完全不肯\x01",
            "做家务。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "这下可麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9435")

    TalkEnd(0xFE)
    Return()

    # Function_13_8DE8 end

    def Function_14_9439(): pass

    label("Function_14_9439")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_953B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94DA")

    #C0545
    ChrTalk(
        0xFE,
        (
            "总觉得市内已经\x01",
            "恢复一些活力了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        (
            "我也要多多购物，\x01",
            "为恢复经济做些贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        (
            "好～再逛一遍便宜购物路线，\x01",
            "大采购一番吧～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9536")

    label("loc_94DA")


    #C0548
    ChrTalk(
        0xFE,
        (
            "我也要多多购物，\x01",
            "为恢复经济做些贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        (
            "好～再逛一遍便宜购物路线，\x01",
            "大采购一番吧～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9536")

    Jump("loc_9BEA")

    label("loc_953B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9549")
    Jump("loc_9BEA")

    label("loc_9549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_95AD")

    #C0550
    ChrTalk(
        0xFE,
        (
            "我虽然搞不懂\x01",
            "那些深奥的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xFE,
        (
            "但既然是大家选择的结果，\x01",
            "应该就是正确的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_95AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9619")

    #C0552
    ChrTalk(
        0xFE,
        (
            "前不久，我去参加了教会的弥撒，\x01",
            "向女神做了祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "希望克洛斯贝尔市\x01",
            "能早日平稳下来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_9619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_967D")

    #C0554
    ChrTalk(
        0xFE,
        "最近经常发生大事件啊。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xFE,
        (
            "总觉得有点可怕，\x01",
            "今天就赶快买好东西，\x01",
            "早点回家吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_967D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_96F4")

    #C0556
    ChrTalk(
        0xFE,
        (
            "嘿嘿，我今天\x01",
            "成功省下了\x01",
            "十米拉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xFE,
        (
            "干脆吃个冰激凌再回家吧～¤\x01",
            "但在下雨天吃那个，好像有点冷……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_96F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_975D")

    #C0558
    ChrTalk(
        0xFE,
        (
            "唔，今天的购物\x01",
            "就到此结束吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "呵呵，因为我走的是\x01",
            "便宜购物路线，\x01",
            "节省了不少钱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_975D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_97BE")

    #C0560
    ChrTalk(
        0xFE,
        (
            "我已经慢慢摸索出了\x01",
            "一条全新的\x01",
            "购物路线。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        (
            "节约其实是\x01",
            "一件很困难的事呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_97BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_97CC")
    Jump("loc_9BEA")

    label("loc_97CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9877")

    #C0562
    ChrTalk(
        0xFE,
        (
            "和别人竞争，\x01",
            "买下那些便宜的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "这就是大减价和大甩卖的\x01",
            "乐趣所在。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "以便宜的价格\x01",
            "买到想要的东西时，\x01",
            "那种喜悦的感觉真是太棒了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9901")

    label("loc_9877")


    #C0565
    ChrTalk(
        0xFE,
        (
            "在大减价或大甩卖时\x01",
            "以低价买到自己想要的东西时，\x01",
            "那种喜悦的感觉真是太棒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "而且省下来的钱\x01",
            "还会成为我的零花钱，\x01",
            "喜悦感更是倍增。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9901")

    Jump("loc_9BEA")

    label("loc_9906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_999B")

    #C0567
    ChrTalk(
        0xFE,
        (
            "受兰花塔揭幕式的影响，\x01",
            "今天的气氛真是相当热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xFE,
        (
            "……我好像嗅到了大减价的味道。\x01",
            "今天就到我平时很少去的\x01",
            "百货店等地方逛逛吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_999B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9A9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A42")

    #C0569
    ChrTalk(
        0xFE,
        (
            "节约的窍门就是收集情报。\x01",
            "绝对不可以错过任何\x01",
            "限时抢购和大甩卖。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        (
            "嗯～在现在这个时间段，\x01",
            "如果去露天货摊买东西，\x01",
            "应该可以节省不少钱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9A98")

    label("loc_9A42")


    #C0571
    ChrTalk(
        0xFE,
        (
            "为了我的零花钱，\x01",
            "必须得节约再节约……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "绝对不可以错过任何\x01",
            "限时抢购和大甩卖。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A98")

    Jump("loc_9BEA")

    label("loc_9A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9B09")

    #C0573
    ChrTalk(
        0xFE,
        (
            "下雨天买东西的人很少，\x01",
            "因此可以慢慢挑选商品。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "呵呵，看来今天也能\x01",
            "买到不少好东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_9B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B89")

    #C0575
    ChrTalk(
        0xFE,
        (
            "妈妈叫我帮她买东西时，\x01",
            "一般会多给我一些米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        (
            "买完东西之后，\x01",
            "剩下的米拉就成了\x01",
            "我的零花钱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9BEA")

    label("loc_9B89")


    #C0577
    ChrTalk(
        0xFE,
        (
            "……可是，妈妈最近\x01",
            "只肯给我刚够\x01",
            "买东西的米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "这、这样一来……\x01",
            "我的零花钱计划也就……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BEA")

    TalkEnd(0xFE)
    Return()

    # Function_14_9439 end

    def Function_15_9BEE(): pass

    label("Function_15_9BEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C64")

    #C0579
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "关店停业不就好了吗，\x01",
            "玛尔缇还真是大胆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xFE,
        (
            "不过，这就是我老婆的\x01",
            "过人之处。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_9CD1")

    label("loc_9C64")


    #C0581
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "关店停业不就好了吗，\x01",
            "玛尔缇还真是大胆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "算了，我难得来一趟，\x01",
            "今天就在店里帮帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CD1")

    TalkEnd(0xFE)
    Return()

    # Function_15_9BEE end

    def Function_16_9CD5(): pass

    label("Function_16_9CD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9D66")

    #C0583
    ChrTalk(
        0xFE,
        (
            "兰花塔的设计图\x01",
            "很可能已经落到了\x01",
            "恐怖分子的手中。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "可是，他们到底\x01",
            "打算从哪里攻进来呢？\x01",
            "我认为我们的警备措施毫无漏洞……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB4")

    label("loc_9D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9DC7")

    #C0585
    ChrTalk(
        0xFE,
        (
            "『赤色星座』和『黑月』\x01",
            "如今都还没有展开行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        "呼，警备工作真是不轻松啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EB4")

    label("loc_9DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E58")

    #C0587
    ChrTalk(
        0xFE,
        "哦，是特别任务支援科啊。\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xFE,
        (
            "如你们所见，我正在负责\x01",
            "这条露天店街的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "你们就专心处理\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_9EB4")

    label("loc_9E58")


    #C0590
    ChrTalk(
        0xFE,
        (
            "如你们所见，我现在正在负责\x01",
            "这条露天店街的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        (
            "你们就专心处理\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB4")

    TalkEnd(0xFE)
    Return()

    # Function_16_9CD5 end

    SaveToFile()

Try(main)
