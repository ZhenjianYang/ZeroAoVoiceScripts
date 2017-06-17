from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0580.bin",                # FileName
        "c0580",                    # MapName
        "c0580",                    # Location
        0x0028,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 40, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0580",                  # 0
        "伊梅尔达夫人",           # 1
        "SE控制",                 # 2
    ))

    AddCharChip((
        "chr/ch09002.itc",                   # 00
    ))

    DeclNpc(-750,    100,     4800,    180,  261,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-750,    0,       3500,    1500,    -750,    1500,    4800,    0x007E, 0,  2,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_126",          # 01, 1
        "Function_2_19B",          # 02, 2
        "Function_3_19F",          # 03, 3
        "Function_4_1B6E",         # 04, 4
        "Function_5_22D0",         # 05, 5
        "Function_6_2DA1",         # 06, 6
        "Function_7_2DB7",         # 07, 7
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Return()

    # Function_0_114 end

    def Function_1_126(): pass

    label("Function_1_126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_159")

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A")
    Sound(128, 1, 50, 0)

    label("loc_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_191")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Return()

    # Function_1_126 end

    def Function_2_19B(): pass

    label("Function_2_19B")

    Call(0, 3)
    Return()

    # Function_2_19B end

    def Function_3_19F(): pass

    label("Function_3_19F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1")
    TalkEnd(0x8)
    Call(0, 5)
    Return()

    label("loc_1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4")
    TalkEnd(0x8)
    Call(0, 4)
    Return()

    label("loc_1E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_23E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_AF(0x43)
    Jump("loc_26F")

    label("loc_25D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26D")
    OP_AF(0x44)
    Jump("loc_26F")

    label("loc_26D")

    OP_AF(0x43)

    label("loc_26F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B65")

    label("loc_27E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_292")
    Jump("loc_1B65")

    label("loc_292")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B65")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_45F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8")

    #C0001
    ChrTalk(
        0x8,
        (
            "（敲击键盘……）\x01",
            "总统被捕，\x01",
            "湿地出现了巨大的树……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "特别是那棵大树，\x01",
            "在导力网络上引起了\x01",
            "各种各样的猜测。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "难得出现了那种惊人之物，\x01",
            "不如趁此机会，\x01",
            "把它变成新的观光景点如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "这样一来，等到恢复正常外交之后，\x01",
            "我就能大赚一笔了。\x01",
            "嘻嘻嘻嘻……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_45A")

    label("loc_3C8")


    #C0005
    ChrTalk(
        0x8,
        (
            "虽然世人都为之震惊慌乱，\x01",
            "但在我眼里，那棵大树\x01",
            "越看越像一棵摇钱树。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "为了在恢复正常外交之后大赚一笔，\x01",
            "现在就要将那片地购下。\x01",
            "嘻嘻嘻嘻……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A")

    Jump("loc_1B65")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_601")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_593")

    #C0007
    ChrTalk(
        0x8,
        "哎呀，这不是支援科的小鬼们吗？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "既然你们开始行动了，\x01",
            "事态应该会越来越有趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00006F有趣吗……我们可是头疼得很呢……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#00200F总之，请您千万注意，\x01",
            "一定不要到外面去。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "知道啦知道啦，\x01",
            "我会在这里专心观战的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "你们就继续努力，\x01",
            "去搅乱总统他们吧。\x01",
            "嘻嘻嘻嘻……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5FC")

    label("loc_593")


    #C0013
    ChrTalk(
        0x8,
        (
            "既然你们开始行动了，\x01",
            "事态应该会越来越有趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "你们就继续努力，\x01",
            "去搅乱总统他们吧。\x01",
            "嘻嘻嘻嘻……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC")

    Jump("loc_1B65")

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_723")

    #C0015
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻嘻……！\x01",
            "那场演讲实在是很有意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "竟然会用那么激烈的言辞\x01",
            "痛斥帝国和共和国。\x01",
            "呵呵，连我都没想到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……不知迪塔那小鬼\x01",
            "接下来有什么打算，\x01",
            "反正帝国和共和国肯定不会善罢甘休的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，要不要趁现在\x01",
            "把仓库里那一大堆古董\x01",
            "转移到安全的地方呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7B3")

    label("loc_723")


    #C0019
    ChrTalk(
        0x8,
        (
            "不知迪塔那小鬼\x01",
            "接下来有什么打算，\x01",
            "反正帝国和共和国肯定不会善罢甘休的。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，要不要趁现在\x01",
            "把仓库里那一大堆古董\x01",
            "转移到安全的地方呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3")

    Jump("loc_1B65")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_901")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87F")

    #C0021
    ChrTalk(
        0x8,
        (
            "在之前那起袭击事件中，\x01",
            "出现在旧城区的巨大怪物\x01",
            "把我名下的公寓彻底毁坏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，看到那种惨状，\x01",
            "也只能干笑了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "……呼，真是的，\x01",
            "到底该怎么处理那片土地呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8FC")

    label("loc_87F")


    #C0024
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，看到被毁坏的那栋公寓的惨状，\x01",
            "也只能干笑了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "重建新公寓\x01",
            "又麻烦又费钱……\x01",
            "要不要干脆把那块土地直接卖掉呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FC")

    Jump("loc_1B65")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F7")

    #C0026
    ChrTalk(
        0x8,
        (
            "那些猎兵真是\x01",
            "无法无天，\x01",
            "居然占领了一个镇子。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "我试着联系了\x01",
            "山道上的人偶工房，\x01",
            "结果却没有接通。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，\x01",
            "算了，约鲁古那个老头子\x01",
            "倒也不需要担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "即使在这种状况下，他说不定\x01",
            "也还在专心致志地制作人偶呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A93")

    label("loc_9F7")


    #C0030
    ChrTalk(
        0x8,
        (
            "我试着联系了\x01",
            "山道上的人偶工房，\x01",
            "结果却没有接通。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "呵呵，算了，以约鲁古那个老头子的性格来说，\x01",
            "即使在这种状况下，说不定\x01",
            "也还在专心致志地制作人偶呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A93")

    Jump("loc_1B65")

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C00")

    #C0032
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，因为这场雨，\x01",
            "本来就很少的顾客\x01",
            "恐怕会变得更少。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "你们难得来一次，\x01",
            "不如趁此机会帮我打扫一下\x01",
            "店里的货架吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#00006F请、请容我拒绝。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，开个玩笑啦。\x01",
            "上面有不少价值不菲的货品，\x01",
            "才不会让你们碰货架。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Jump("loc_C62")

    label("loc_C00")


    #C0036
    ChrTalk(
        0x8,
        (
            "我看了导力网络上的消息，\x01",
            "下午应该就会放晴了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，尽管如此，\x01",
            "顾客应该也不会增多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C62")

    Jump("loc_1B65")

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0D")

    #C0038
    ChrTalk(
        0x8,
        (
            "我刚刚查看了导力网络，\x01",
            "发现一条速报。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "据说西克洛斯贝尔\x01",
            "街道上发生了\x01",
            "列车脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，\x01",
            "难道只有我嗅到了\x01",
            "可疑的味道吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D77")

    label("loc_D0D")


    #C0041
    ChrTalk(
        0x8,
        (
            "导力网络上说，\x01",
            "西克洛斯贝尔街道上\x01",
            "发生了列车脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，\x01",
            "难道只有我嗅到了\x01",
            "可疑的味道吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D77")

    Jump("loc_1B65")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E59")

    #C0043
    ChrTalk(
        0x8,
        (
            "我也不太了解\x01",
            "那个老头子的\x01",
            "底细呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "毕竟他平时就不爱露脸，\x01",
            "只知道默默制作人偶，\x01",
            "是个极其孤僻的老头子。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "反正对我来说，只要那间工房制作的\x01",
            "人偶能让我赚上大把的钱就好了。\x01",
            "嘻嘻嘻嘻……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ED3")

    label("loc_E59")


    #C0046
    ChrTalk(
        0x8,
        (
            "我也不太了解\x01",
            "那个老头子的\x01",
            "底细呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "反正对我来说，只要那间工房制作的\x01",
            "人偶能让我赚上大把的钱就好了。\x01",
            "嘻嘻嘻嘻……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED3")

    Jump("loc_1B65")

    label("loc_ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1037")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBD")

    #C0048
    ChrTalk(
        0x8,
        (
            "（敲击键盘……）\x01",
            "嗯嗯，原来如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "对于独立这个问题，\x01",
            "导力网络上的意见\x01",
            "也是赞同和反对皆有。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "不过，到目前为止，\x01",
            "还是赞成派\x01",
            "占了多数。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，讨论肯定会一直继续，\x01",
            "我可得经常关心一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1032")

    label("loc_FBD")


    #C0052
    ChrTalk(
        0x8,
        (
            "对于独立这个问题，\x01",
            "导力网络上的意见\x01",
            "也是赞同和反对皆有。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，讨论肯定会一直继续，\x01",
            "我可得经常关心一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1032")

    Jump("loc_1B65")

    label("loc_1037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1296")

    #C0054
    ChrTalk(
        0x8,
        (
            "哦，你是……\x01",
            "爱普斯泰恩的……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#00200F好久不见了，老婆婆。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，你们特别任务支援科的\x01",
            "人员总算聚齐了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "听说你们还要参加通商会议的警备工作，\x01",
            "能以完美的阵容处理任务，真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00006F您还是老样子，\x01",
            "知道各种各样的情报啊……\x02\x03",

            "#00000F您获取情报\x01",
            "只是为了自娱自乐，\x01",
            "倒真是让我们松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，关于这个问题，\x01",
            "你们尽管放心好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "我的人生信条就是，\x01",
            "绝对不留下任何会使\x01",
            "自己被警方逮捕的把柄。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#00206F……这种话不应该\x01",
            "对我们说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 4)
    Jump("loc_12FF")

    label("loc_1296")


    #C0062
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，你们特别任务支援科的\x01",
            "人员总算聚齐了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "我今后也会继续\x01",
            "观察你们的行动，\x01",
            "并以此为乐的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FF")

    Jump("loc_1B65")

    label("loc_1304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140E")

    #C0064
    ChrTalk(
        0x8,
        (
            "（敲击键盘……）\x01",
            "哦哦，原来如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "兰花塔的话题\x01",
            "在导力网络上\x01",
            "也掀起了热议呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "毕竟是一座直耸云霄的超高层大楼，\x01",
            "作为观光景点，应该也能\x01",
            "带来相当可观的经济效益。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，我得趁现在\x01",
            "大量收购那些可以清晰\x01",
            "眺望到兰花塔的地产。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1494")

    label("loc_140E")


    #C0068
    ChrTalk(
        0x8,
        (
            "那座兰花塔……\x01",
            "作为观光景点，应该也能\x01",
            "带来相当可观的经济效益。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，我得趁现在\x01",
            "大量收购那些可以清晰\x01",
            "眺望到兰花塔的地产。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    Jump("loc_1B65")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157A")

    #C0070
    ChrTalk(
        0x8,
        (
            "对了，我最近在看\x01",
            "一部连载小说……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "故事虽然挺有趣，\x01",
            "但却不太合我的口味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，机会难得，\x01",
            "干脆塞给你们好了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝３卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝３卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 2)
    Jump("loc_171D")

    label("loc_157A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166B")

    #C0074
    ChrTalk(
        0x8,
        (
            "在明天的通商会议上，\x01",
            "各国首脑将齐聚一堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "其他首脑倒无所谓，\x01",
            "但我真想亲眼目睹『铁血宰相』\x01",
            "与共和国总统的会面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "这两个国家长久以来一直都互不相让，\x01",
            "这次直接会面，又会有如何表现呢……\x01",
            "嘻嘻嘻，真是值得一看啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_171D")

    label("loc_166B")


    #C0077
    ChrTalk(
        0x8,
        (
            "说起明天那场通商会议，\x01",
            "我真想亲眼目睹『铁血宰相』\x01",
            "与共和国总统的会面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "这两个国家长久以来一直都互不相让，\x01",
            "这次直接会面，又会有如何表现呢……\x01",
            "嘻嘻嘻，真是值得一看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171D")

    Jump("loc_1B65")

    label("loc_1722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_181C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C1")

    #C0079
    ChrTalk(
        0x8,
        (
            "刚才有些引人注目的家伙\x01",
            "往鲁巴彻旧址\x01",
            "那边去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "本以为那个地方会被\x01",
            "黑月的人弄到手呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，事情好像\x01",
            "变得有趣了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1817")

    label("loc_17C1")


    #C0082
    ChrTalk(
        0x8,
        (
            "本以为鲁巴彻旧址肯定\x01",
            "会被黑月的人弄到手呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，事情好像\x01",
            "变得有趣了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1817")

    Jump("loc_1B65")

    label("loc_181C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1983")

    #C0084
    ChrTalk(
        0x8,
        (
            "说起来，从目前的\x01",
            "发展来看……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "后巷的那片鲁巴彻旧址\x01",
            "早晚会成为黑月的囊中物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，早知如此，\x01",
            "我真应该提前收购下来，\x01",
            "然后再以高价转卖给他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00006F（说起来，这位老婆婆\x01",
            "  就是靠买卖土地而暴富的……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A0B")

    label("loc_1983")


    #C0088
    ChrTalk(
        0x8,
        (
            "说起来，后巷的那片\x01",
            "鲁巴彻旧址……\x01",
            "似乎就要被黑月弄到手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，早知如此，\x01",
            "我真应该提前收购下来，\x01",
            "然后再以高价转卖给他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0B")

    Jump("loc_1B65")

    label("loc_1A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B01")

    #C0090
    ChrTalk(
        0x8,
        (
            "支援科总算再次开工了，\x01",
            "我今后也会继续关注你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻……\x01",
            "多给我提供一些热门的新消息，\x01",
            "让我好好乐一乐吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00012F我、我们可不是为了\x01",
            "取悦您才工作的……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        "#10309F呵呵，真是位有趣的老婆婆。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B65")

    label("loc_1B01")


    #C0094
    ChrTalk(
        0x8,
        (
            "支援科总算再次开工了，\x01",
            "我今后也会继续关注你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，你们就\x01",
            "多给我找点乐子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B65")

    Jump("loc_1EE")

    label("loc_1B6A")

    TalkEnd(0x8)
    Return()

    # Function_3_19F end

    def Function_4_1B6E(): pass

    label("Function_4_1B6E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -1540, 0, 1900, 45)
    SetChrPos(0x102, 390, 0, 2110, 0)
    SetChrPos(0x109, -1050, 0, 800, 0)
    SetChrPos(0x105, 150, 0, 830, 0)
    OP_0D()

    #C0096
    ChrTalk(
        0x8,
        "#11P嘻嘻嘻，欢迎光临。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x8,
        (
            "#11P哎呀，这不是特别任务支援科的\x01",
            "小朋友们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#11P嘻嘻嘻，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#6P#00000F好久不见了，伊梅尔达夫人。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#6P#00100F您还是这么有精神啊。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "#11P哼，有什么精神，\x01",
            "最近每天都无聊得很，\x01",
            "快烦死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#11P鲁巴彻已经被摧毁了，\x01",
            "你们也暂时停止了工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#11P就连导力网络上那个\x01",
            "经常和我交易的情报商\x01",
            "都停止了营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#6P#00105F（导力网络上的情报商……）\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#6P#00003F（应该就是约纳，\x01",
            "  他已经被调回财团工作了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0106
    ChrTalk(
        0x8,
        (
            "#11P哦？仔细一看，\x01",
            "有两个生面孔呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "#11P你们就是支援科的\x01",
            "新人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#11P警备队员和不良团伙的头领……\x01",
            "嘻嘻嘻，恢复工作的同时，\x01",
            "还聚集到了很有趣的成员嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x109,
        "#6P#10105F为、为何连这种事都知道……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#6P#00006F情报商不是已经\x01",
            "停止营业了吗？\x01",
            "您怎么还了解这么多？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻嘻嘻……\x01",
            "我的情报来源\x01",
            "又不是只有那一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        "#6P#10309F哈哈，真是个有趣的老婆婆。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x8,
        (
            "#11P哦，对了，\x01",
            "为了答谢你们特地来看我，\x01",
            "送你们一个好东西吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        "#11P来，拿着吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0115
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '伊梅尔达馆的钥匙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('伊梅尔达馆的钥匙', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0116
    ChrTalk(
        0x102,
        "#6P#00105F这是……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻嘻，\x01",
            "这是我在旧城区的那座公寓——\x01",
            "『伊梅尔达馆』的钥匙。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x105,
        (
            "#6P#10302F哦，说起来，\x01",
            "那里确实有一座很\x01",
            "破烂的公寓叫这名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "#11P喂！不许说它破烂！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#11P哼，算了。\x01",
            "那座公寓里最近又出现了魔兽，\x01",
            "如果你们愿意，就去清扫一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x101,
        (
            "#6P#00006F某、某件委托中的\x01",
            "通缉魔兽确实在\x01",
            "那个地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        "#6P#10106F如此一来，我们想不去都不行了呢。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻嘻……\x01",
            "没关系，愿意去的时候再去就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        "#11P拜托你们啦，小家伙。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x139, 4)
    OP_29(0x67, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_1B6E end

    def Function_5_22D0(): pass

    label("Function_5_22D0")

    EventBegin(0x0)
    Fade(500)
    SoundLoad(841)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    SetChrPos(0x109, -2840, 0, 390, 44)
    SetChrPos(0x105, -1360, 0, -710, 44)
    OP_0D()
    BeginChrThread(0x9, 1, 0, 6)
    SetChrName("")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊梅尔达夫人正用柜台下的\x01",
            "通讯器进行通话。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 1)

    #C0126
    ChrTalk(
        0x8,
        (
            "#11P……啧，那个臭老头，\x01",
            "竟然不接！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#00005F伊梅尔达夫人，\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25C9")

    #C0128
    ChrTalk(
        0x8,
        "#11P啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#11P没什么，我本想联络\x01",
            "约鲁古那老头子，问问他有关\x01",
            "下一款新品人偶的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        "#00105F联络约鲁古大师……？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "#11P嗯，但一直都\x01",
            "联络不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#11P他现在应该在工房的……\x01",
            "啧，如果正在集中精神工作，\x01",
            "短时间内恐怕是联系不上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0133
    ChrTalk(
        0x101,
        (
            "#6P#00003F（……在以前的委托中听说过，\x01",
            "  伊梅尔达夫人和约鲁古大师\x01",
            "  是老相识。）\x02\x03",

            "（趁此机会……\x01",
            "  询问一下人偶工房的事情吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2964")

    label("loc_25C9")


    #C0134
    ChrTalk(
        0x8,
        "#11P啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#11P没什么，我本想联络\x01",
            "约鲁古那老头子，问问他有关\x01",
            "下一款新品人偶的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "#11P但一直都\x01",
            "联络不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "#11P他现在应该在工房的……\x01",
            "啧，如果正在集中精神工作，\x01",
            "短时间内恐怕是联系不上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x109)
    Sleep(50)
    OP_64(0x105)

    #C0138
    ChrTalk(
        0x101,
        (
            "#6P#00005F约鲁古……？\x01",
            "新品人偶……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#00005F您、您指的难道是……\x01",
            "约鲁古·罗赞贝尔克大师！？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#00105F伊梅尔达夫人，\x01",
            "您和他认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#11P是啊，我可是他\x01",
            "制造的人偶的\x01",
            "销售代理。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#11P但那个老头子极其孤僻，\x01",
            "完全不懂变通为何物，\x01",
            "总是给我找各种麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0143
    ChrTalk(
        0x101,
        (
            "#6P#00006F（……居然在这种地方\x01",
            "  遇到了认识他的人。）\x02\x03",

            "（趁此机会……\x01",
            "  询问一下人偶工房的事情吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2964")


    #C0144
    ChrTalk(
        0x8,
        (
            "#11P……话说回来，\x01",
            "你们找我有事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻嘻，\x01",
            "如果想买卖古董，\x01",
            "我随时都可以为你们服务哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#6P#00000F不、不是的，\x01",
            "只是想向您请教一些事情……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向对方询问了有关罗赞贝尔克\x01",
            "工房与约鲁古老人的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0148
    ChrTalk(
        0x8,
        (
            "#11P……你们为什么要\x01",
            "调查那种事？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#00012F没、没什么啊……\x01",
            "只是有点兴趣而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x8,
        (
            "#11P算啦，和你们说说也无妨……\x01",
            "其实我也不太了解\x01",
            "那个老头子的底细。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#11P毕竟他平时就不爱露脸，\x01",
            "只知道默默制作人偶，\x01",
            "是个极其孤僻的老头子。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BA1")

    #C0152
    ChrTalk(
        0x8,
        (
            "#11P以前和你们说过，彩虹剧团的\x01",
            "舞台装置也是由他制造的，\x01",
            "除此之外，我就一无所知了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD8")

    label("loc_2BA1")


    #C0153
    ChrTalk(
        0x8,
        (
            "#11P我虽然是他的销售代理，\x01",
            "但并不了解更多的内情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD8")


    #C0154
    ChrTalk(
        0x109,
        "#10106F这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#11P反正对我来说，只要那间工房制作的\x01",
            "人偶能让我赚上大把的钱就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "#11P谁有兴趣打听那个\x01",
            "老头子的私人秘密啊。\x01",
            "嘻嘻嘻嘻……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#6P#00303F（原、原来如此……\x01",
            "  没想到居然是这么浅显的关系。）\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        (
            "#6P#00200F（也许正是\x01",
            "  因为这样，\x01",
            "  他们才能保持来往呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#6P#10300F（既然如此，\x01",
            "  我们只能直接去\x01",
            "  拜访那位老人了吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#6P#00000F（是啊……\x01",
            "  各位，我们出发吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x16F, 5)
    OP_24(0x349)
    EventEnd(0x5)
    Return()

    # Function_5_22D0 end

    def Function_6_2DA1(): pass

    label("Function_6_2DA1")

    Sound(841, 2, 50, 0)
    Sleep(1800)
    OP_24(0x349)
    Sound(813, 0, 20, 0)
    Sleep(500)
    Return()

    # Function_6_2DA1 end

    def Function_7_2DB7(): pass

    label("Function_7_2DB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_2DB7 end

    SaveToFile()

Try(main)
