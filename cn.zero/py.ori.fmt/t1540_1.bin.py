from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1540_1.bin",                # FileName
        "t1540",                    # MapName
        "t1540",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 1, 0, 3],
    )

    BuildStringList((
        "t1540_1",                # 0
    ))

    ScpFunction((
        "Function_0_15C",          # 00, 0
        "Function_1_6B1",          # 01, 1
        "Function_2_942",          # 02, 2
        "Function_3_DB3",          # 03, 3
        "Function_4_FAC",          # 04, 4
        "Function_5_FB0",          # 05, 5
        "Function_6_1C75",         # 06, 6
        "Function_7_2AE2",         # 07, 7
        "Function_8_3608",         # 08, 8
        "Function_9_3D9E",         # 09, 9
        "Function_10_4519",        # 0A, 10
        "Function_11_45DA",        # 0B, 11
        "Function_12_467C",        # 0C, 12
        "Function_13_4891",        # 0D, 13
        "Function_14_4A63",        # 0E, 14
        "Function_15_4A9F",        # 0F, 15
        "Function_16_4D8A",        # 10, 16
        "Function_17_4FD6",        # 11, 17
        "Function_18_52B6",        # 12, 18
        "Function_19_544F",        # 13, 19
        "Function_20_5530",        # 14, 20
        "Function_21_5574",        # 15, 21
        "Function_22_56D2",        # 16, 22
        "Function_23_58A1",        # 17, 23
        "Function_24_5919",        # 18, 24
        "Function_25_5B16",        # 19, 25
        "Function_26_5CF8",        # 1A, 26
        "Function_27_5F9E",        # 1B, 27
        "Function_28_62BD",        # 1C, 28
        "Function_29_654F",        # 1D, 29
        "Function_30_67BB",        # 1E, 30
        "Function_31_6A02",        # 1F, 31
        "Function_32_6C45",        # 20, 32
        "Function_33_6E23",        # 21, 33
        "Function_34_703E",        # 22, 34
        "Function_35_725E",        # 23, 35
        "Function_36_73B8",        # 24, 36
        "Function_37_74BA",        # 25, 37
        "Function_38_76E9",        # 26, 38
        "Function_39_7749",        # 27, 39
        "Function_40_79B1",        # 28, 40
        "Function_41_7B3D",        # 29, 41
        "Function_42_7DAF",        # 2A, 42
        "Function_43_804B",        # 2B, 43
        "Function_44_81FC",        # 2C, 44
        "Function_45_832D",        # 2D, 45
        "Function_46_8606",        # 2E, 46
        "Function_47_89A1",        # 2F, 47
        "Function_48_8AF1",        # 30, 48
        "Function_49_8BCE",        # 31, 49
    ))


    def Function_0_15C(): pass

    label("Function_0_15C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F0")
    Jump("loc_23A")

    label("loc_1F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_210")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A")

    label("loc_210")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_230")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A")

    label("loc_230")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26D")
    Jump("loc_6A9")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_27B")
    Jump("loc_6A9")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_289")
    Jump("loc_6A9")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_297")
    Jump("loc_6A9")

    label("loc_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2A5")
    Jump("loc_6A9")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2B3")
    Jump("loc_6A9")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C1")
    Jump("loc_6A9")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CF")
    Jump("loc_6A9")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DD")
    Jump("loc_6A9")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_6A9")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F9")
    Jump("loc_6A9")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_6A9")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B")

    #C0001
    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "约亚西姆医生说\x01",
            "我明天应该就可以出院了……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "呜啊～工作一定堆积如山了。\x01",
            "还想再睡一下啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3C4")

    label("loc_38B")


    #C0003
    ChrTalk(
        0xFE,
        (
            "唉，难得明天可以出院了，\x01",
            "但一想到工作还真郁闷啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4")

    Jump("loc_6A9")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")

    #C0004
    ChrTalk(
        0xFE,
        (
            "啊，我说你们几个。\x01",
            "楼顶调查得怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0001F嗯，虽然还残留着一些谜团……\x01",
            "不过已经发现了魔兽去过的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "嗯～那果然\x01",
            "不是我在做梦啊………………\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "……嗯，谢谢你们了。\x01",
            "光是确定了这一点，\x01",
            "对我来说，就算是有收获了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#0100F不用客气。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0200F那么……\x01",
            "去向塞茜尔小姐\x01",
            "报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_565")

    #C0011
    ChrTalk(
        0x104,
        (
            "#0300F她好像去了病房楼\x01",
            "三层的单人间吧。\x01",
            "赶快过去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B1")

    label("loc_565")


    #C0012
    ChrTalk(
        0x104,
        (
            "#0300F去护士中心那里问问，\x01",
            "应该就能知道她在哪里了吧。\x01",
            "赶快过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B1")

    SetScenarioFlags(0x0, 0)
    Jump("loc_5D7")

    label("loc_5B9")


    #C0013
    ChrTalk(
        0xFE,
        "那果然不是我在做梦啊……\x02",
    )

    CloseMessageWindow()

    label("loc_5D7")

    Jump("loc_6A9")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_6A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D")

    #C0014
    ChrTalk(
        0xFE,
        (
            "嗯～……那果然\x01",
            "是我的幻觉吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "如果真的只是梦就好了，\x01",
            "可我全身都受了伤……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_69B")

    label("loc_64D")


    #C0016
    ChrTalk(
        0xFE,
        (
            "……总之，调查就拜托你们了。\x01",
            "无论是梦还是现实，\x01",
            "我都想知道受伤的原因呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69B")

    Jump("loc_6A9")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6A9")

    label("loc_6A9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_0_15C end

    def Function_1_6B1(): pass

    label("Function_1_6B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF")
    Call(1, 2)
    Jump("loc_740")

    label("loc_6CF")

    TurnDirection(0xC, 0x9, 0)
    OP_4B(0xC, 0xFF)

    #C0017
    ChrTalk(
        0xFE,
        "嘿嘿，又失败了。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "不要介意，不要介意。\x01",
            "人生在世，\x01",
            "孰能无过嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        "但你的过失也太多了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_740")

    Jump("loc_93E")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_753")
    Jump("loc_93E")

    label("loc_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_761")
    Jump("loc_93E")

    label("loc_761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_76F")
    Jump("loc_93E")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_77D")
    Jump("loc_93E")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_78B")
    Jump("loc_93E")

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_799")
    Jump("loc_93E")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B4")
    Call(1, 2)
    Jump("loc_7E7")

    label("loc_7B4")


    #C0020
    ChrTalk(
        0xFE,
        (
            "米海尔和艾达\x01",
            "出去散步了～\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "大概在水边吧？\x02",
    )

    CloseMessageWindow()

    label("loc_7E7")

    Jump("loc_93E")

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7FA")
    Jump("loc_93E")

    label("loc_7FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_808")
    Jump("loc_93E")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_860")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823")
    Call(1, 3)
    Jump("loc_85B")

    label("loc_823")


    #C0022
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "有这么多体温计的话，\x01",
            "再怎么失败也不怕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85B")

    Jump("loc_93E")

    label("loc_860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B")
    Call(1, 3)
    Jump("loc_8B1")

    label("loc_87B")


    #C0023
    ChrTalk(
        0xFE,
        (
            "呵呵，失败失败。\x01",
            "原来体温计放在\x01",
            "这边的口袋里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B1")

    Jump("loc_93E")

    label("loc_8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_8C4")
    Jump("loc_93E")

    label("loc_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_8D2")
    Jump("loc_93E")

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_935")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8ED")
    Call(1, 2)
    Jump("loc_930")

    label("loc_8ED")


    #C0024
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "梅菲尔真是\x01",
            "爱生气。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "待会还要去\x01",
            "盖巴尔先生那里啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_930")

    Jump("loc_93E")

    label("loc_935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_93E")

    label("loc_93E")

    TalkEnd(0xFE)
    Return()

    # Function_1_6B1 end

    def Function_2_942(): pass

    label("Function_2_942")

    TurnDirection(0x9, 0xC, 0)
    TurnDirection(0xC, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A3D")

    #C0026
    ChrTalk(
        0xC,
        (
            "希伦，你啊……\x01",
            "连杯咖啡也泡不好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "为什么咖啡里\x01",
            "会有红茶的香味啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "嗯～大概是因为……\x01",
            "我可能把咖啡\x01",
            "和红茶放在一起泡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "这我知道！\x01",
            "所以我才想问你为什么总是这样……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xC,
        "……唉，真是累死人了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DA4")

    label("loc_A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_A4B")
    Jump("loc_DA4")

    label("loc_A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A59")
    Jump("loc_DA4")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A67")
    Jump("loc_DA4")

    label("loc_A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_A75")
    Jump("loc_DA4")

    label("loc_A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_A83")
    Jump("loc_DA4")

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A91")
    Jump("loc_DA4")

    label("loc_A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C02")

    #C0031
    ChrTalk(
        0x9,
        (
            "那个～梅菲尔，\x01",
            "米海尔得的到底是什么病？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "嗯～……是很难治的病，\x01",
            "想痊愈的话，似乎必须要动手术。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xC,
        (
            "但是，外科手术给人感觉很恐怖吧？\x01",
            "米海尔似乎也不例外，\x01",
            "总是无法下定决心，接受手术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "呼，是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "只要有接受手术的勇气，\x01",
            "米海尔的病也是能治好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "要是能有什么让他产生勇气的\x01",
            "契机就好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "你啊……偶尔也会\x01",
            "说两句正经话呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA4")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C10")
    Jump("loc_DA4")

    label("loc_C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C1E")
    Jump("loc_DA4")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C2C")
    Jump("loc_DA4")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C3A")
    Jump("loc_DA4")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_C48")
    Jump("loc_DA4")

    label("loc_C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_C56")
    Jump("loc_DA4")

    label("loc_C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_D9B")

    #C0038
    ChrTalk(
        0xC,
        (
            "听说你昨天……把番茄酱\x01",
            "洒到盖巴尔先生的床单上了？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "是呀～\x01",
            "真是吓我一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "偶然来查房的医生\x01",
            "误以为是大出血而吓得昏倒……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        "你、你这人啊……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "总之，床单算是\x01",
            "洗干净了……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "你可要把干净的\x01",
            "新床单拿过去，\x01",
            "并向盖巴尔先生好好道歉哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "哎～……可是我不太喜欢\x01",
            "那个大叔哎……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        "不准发牢骚！\x02",
    )

    CloseMessageWindow()
    Jump("loc_DA4")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_DA4")

    label("loc_DA4")

    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_2_942 end

    def Function_3_DB3(): pass

    label("Function_3_DB3")

    TurnDirection(0x9, 0x1B, 0)
    SetChrSubChip(0x1B, 0x2)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_DD0")
    Jump("loc_FA0")

    label("loc_DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_EC2")

    #C0046
    ChrTalk(
        0x9,
        (
            "来～到了今天量体温的时间了哦。\x01",
            "要夹体温计了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x1B,
        (
            "……护、护士小姐。\x01",
            "量体温虽然可以……\x01",
            "但你为什么拿着十支体温计？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "因为，有这么多的话，就算量的时候\x01",
            "断掉几根，至少应该也有一根能正常量出来嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x1B,
        "（好、好不安……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_FA0")

    label("loc_EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FA0")

    #C0050
    ChrTalk(
        0x9,
        (
            "来～到了量体温的时间了哦。\x01",
            "要夹体温计了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1B,
        (
            "……护、护士小姐。\x01",
            "你没有像昨天一样，\x01",
            "错把注射针拿来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "讨厌，没有啦。\x01",
            "就算是我，也不会重复\x01",
            "同样的错误啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        "…………啊。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x1B,
        "…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_FA0")

    SetScenarioFlags(0x0, 1)
    SetChrSubChip(0x1B, 0x0)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_3_DB3 end

    def Function_4_FAC(): pass

    label("Function_4_FAC")

    Call(1, 5)
    Return()

    # Function_4_FAC end

    def Function_5_FB0(): pass

    label("Function_5_FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC6")
    Call(0, 11)
    Jump("loc_1C74")

    label("loc_FC6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1157")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FA")

    #C0055
    ChrTalk(
        0xA,
        "再过几天，就是久违的假日了。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "呵呵，兰迪先生……\x01",
            "下次大家再一起去玩吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#0300F好，等你们哦！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F2")

    #C0058
    ChrTalk(
        0x10A,
        (
            "#0603F……执行任务时，竟敢当着我的面\x01",
            "约定出游，真是好大的胆子啊。\x02\x03",

            "#0600F如果你是一科的成员，\x01",
            "回去以后就得给我\x01",
            "拼死写检讨书了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        "#0305F呃……！？\x02",
    )

    CloseMessageWindow()

    label("loc_10F2")

    SetScenarioFlags(0x0, 3)
    Jump("loc_1152")

    label("loc_10FA")


    #C0060
    ChrTalk(
        0xA,
        (
            "自纪念庆典以来，终于\x01",
            "可以请到假了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "我会把兰和艾达也约上，\x01",
            "下次再一起去玩吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1152")

    Jump("loc_1C71")

    label("loc_1157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_11B4")

    #C0062
    ChrTalk(
        0xA,
        "差不多快到晚饭的时间了呢～\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "要去琪尔修宿舍长那里\x01",
            "给病人们取餐点才行～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11FA")

    #C0064
    ChrTalk(
        0xA,
        (
            "今天送来的那些伤员，\x01",
            "轻伤的那位躺在\x01",
            "２０１号室哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EE")

    #C0065
    ChrTalk(
        0xA,
        (
            "那个叫盖巴尔的议员大叔\x01",
            "住在三楼的单人病房……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        (
            "有一次，他喝得大醉，\x01",
            "然后闯进了护士站，\x01",
            "还说什么来人给他倒酒呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "之后护士长很快就赶了回来，\x01",
            "把他轰走了……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "真是的，该不会是把护士\x01",
            "当成女公关之类了吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_138C")

    label("loc_12EE")


    #C0069
    ChrTalk(
        0xA,
        (
            "偶尔也会有盖巴尔议员\x01",
            "那种给人添麻烦的患者呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "要么就是在医院里住得很舒服，所以赖着不出院，\x01",
            "要么就是对护士们进行骚扰……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        "真是的，感觉好讨厌啊～\x02",
    )

    CloseMessageWindow()

    label("loc_138C")

    Jump("loc_1C71")

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1401")

    #C0072
    ChrTalk(
        0xA,
        (
            "有个脸蛋涨得通红的小女孩\x01",
            "往楼下跑去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "好像在生气闹别扭的样子……\x01",
            "不过还真是可爱啊～⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_144E")

    #C0074
    ChrTalk(
        0xA,
        "啊，这不是警察弟弟嘛。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "塞茜尔前辈\x01",
            "去３０１号室了哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_14C0")

    #C0076
    ChrTalk(
        0xA,
        (
            "医生不在的话，\x01",
            "总是会觉得不安呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "虽然听说各位实习医生也是很优秀的，\x01",
            "但还是比不上教授呀～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_14C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1560")

    #C0078
    ChrTalk(
        0xA,
        "肚子饿了～……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "护士的午休是轮流制，\x01",
            "所以经常会错过\x01",
            "午饭时间呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "给病人量体温的时候，肚子突然叫起来，\x01",
            "会很难为情的啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_158E")

    label("loc_1560")


    #C0081
    ChrTalk(
        0xA,
        "（咕～……）\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        "唉……好想早点午休啊。\x02",
    )

    CloseMessageWindow()

    label("loc_158E")

    Jump("loc_1C71")

    label("loc_1593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168C")

    #C0083
    ChrTalk(
        0xA,
        (
            "明天真想再多休息一天呀，\x01",
            "哪怕只多一天也好～\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "因为明天会有游行哦。\x01",
            "不观赏那个的话，\x01",
            "就不能算是参加了纪念庆典呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "好羡慕当警察的各位呀。\x01",
            "可以以工作为借口，\x01",
            "去看游行吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006F我、我们才不会\x01",
            "做那样的事……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16C9")

    label("loc_168C")


    #C0087
    ChrTalk(
        0xA,
        (
            "虽然很想看明天的游行……\x01",
            "唉，但毕竟要工作，也没办法呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C9")

    Jump("loc_1C71")

    label("loc_16CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_173E")

    #C0088
    ChrTalk(
        0xA,
        (
            "昨天值班的梅菲尔\x01",
            "和希伦今天休息～\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "我们昨天玩得很开心呢，\x01",
            "所以今天一天可得努力工作才行～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_173E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1863")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1807")

    #C0090
    ChrTalk(
        0xA,
        (
            "那个伊莉娅·普拉提耶的朋友\x01",
            "竟然就在我的身边，真是令人吃惊呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "……能不能拜托\x01",
            "塞茜尔前辈\x01",
            "向伊莉娅小姐要个签名呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0000F（伊莉娅小姐的崇拜者……\x01",
            "  还真多啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_185E")

    label("loc_1807")


    #C0093
    ChrTalk(
        0xA,
        (
            "……能不能拜托\x01",
            "塞茜尔前辈\x01",
            "向伊莉娅小姐要个签名呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "下次找个机会\x01",
            "问问看吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185E")

    Jump("loc_1C71")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_18EE")

    #C0095
    ChrTalk(
        0xA,
        (
            "唉～唉，结果还是没有\x01",
            "弄到彩虹剧团的票啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "护士长虽然很得意地说她以前看过，\x01",
            "但现在的彩虹剧团\x01",
            "肯定已经更加厉害了呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_18EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1934")

    #C0097
    ChrTalk(
        0xA,
        "３６度６……很正常呢～\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        "接下来是利顿医生了吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_1934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_19AA")

    #C0099
    ChrTalk(
        0xA,
        (
            "……玛萨护士长是顺风耳，\x01",
            "真有点怕她呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "不知道她会不会躲在某处听到\x01",
            "我们谈话，可要小心才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_19AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C22")

    #C0101
    ChrTalk(
        0xA,
        (
            "啊，塞茜尔前辈。\x01",
            "辛苦了～\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "休息时间很快\x01",
            "就要结束了……\x01",
            "你在干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x136,
        (
            "#1300F我在帮他们做点事情。\x01",
            "抱歉哦，我马上就回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "啊，没事没事～\x01",
            "稍微迟到一会应该没关系的。\x01",
            "……嗯，这几位是？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#0304F我叫兰迪，唐突造访，\x01",
            "真是十分抱歉。\x02\x03",

            "#0300F……请问小姐芳名？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        "那个，我叫菲莉亚～……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#0006F唉，好了啦，兰迪，\x01",
            "你就先安分一下吧……\x02\x03",

            "#0000F……咳咳，抱歉，还没有自我介绍。\x01",
            "我是警察局·特别任务支援科的罗伊德。\x02\x03",

            "我们是来调查实习医生利顿\x01",
            "遇袭事件的……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        "哦，那件事啊～\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "（莫非这个人就是\x01",
            "  塞茜尔前辈说的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        "……呵呵，请加油哦～\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#0003F（刚、刚才的停顿是什么意思……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 1)
    Jump("loc_1C63")

    label("loc_1C22")


    #C0112
    ChrTalk(
        0xA,
        "调查要加油哦～\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0003F（怎么一直\x01",
            "  露出诡异的笑容……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C63")

    Jump("loc_1C71")

    label("loc_1C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1C71")

    label("loc_1C71")

    TalkEnd(0xA)

    label("loc_1C74")

    Return()

    # Function_5_FB0 end

    def Function_6_1C75(): pass

    label("Function_6_1C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C9C")
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1C97")
    SetScenarioFlags(0x0, 5)

    label("loc_1C97")

    Jump("loc_2AE1")

    label("loc_1C9C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1CF8")

    #C0114
    ChrTalk(
        0xB,
        "好，今天一天也要努力工作啊。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "我们护士必须要为病人\x01",
            "尽心尽力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_1CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1DCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D88")
    TurnDirection(0xB, 0x103, 0)

    #C0116
    ChrTalk(
        0xB,
        (
            "……哎呀，缇欧，\x01",
            "你的脸色好像不太好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#0203F……没那回事，\x01",
            "请不必介意……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        "嗯嗯……是错觉吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1DC9")

    label("loc_1D88")


    #C0119
    ChrTalk(
        0xB,
        "是错觉吧……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "……算啦，天也快黑了，\x01",
            "回去时可要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC9")

    Jump("loc_2ADE")

    label("loc_1DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1E42")

    #C0121
    ChrTalk(
        0xB,
        (
            "虽然从早上开始就手忙脚乱的，\x01",
            "但刚刚总算是稳定下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "不管怎么说，\x01",
            "病人能够保住性命就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_1E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDE")

    #C0123
    ChrTalk(
        0xB,
        (
            "小滴最近这段时间\x01",
            "似乎变得开朗多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        (
            "她很开心地告诉我说，\x01",
            "自己交到了新的朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "呵呵，太好啦。\x01",
            "朋友就是人生之宝嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1F3E")

    label("loc_1EDE")


    #C0126
    ChrTalk(
        0xB,
        (
            "小滴最近这段时间\x01",
            "似乎变得开朗多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "这都是因为她交到了新朋友吧，\x01",
            "我们也很替她开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3E")

    Jump("loc_2ADE")

    label("loc_1F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_209B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2033")

    #C0128
    ChrTalk(
        0xB,
        "塞茜尔真是个工作勤奋的女孩啊。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "而且其他护士和医生，\x01",
            "还有病人们都很信任她。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "真想让塞茜尔来继承\x01",
            "护士长的位置啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0006F好、好像突然\x01",
            "听到了很重大的消息啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xB,
        "哈哈，但现在说这些还为时尚早啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2096")

    label("loc_2033")


    #C0133
    ChrTalk(
        0xB,
        (
            "真想让塞茜尔来继承\x01",
            "护士长的位置啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "不过，我还打算\x01",
            "再干二十年呢，\x01",
            "现在说这些还为时尚早。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2096")

    Jump("loc_2ADE")

    label("loc_209B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_218F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212F")

    #C0135
    ChrTalk(
        0xB,
        (
            "真希望在３０２号室住院的\x01",
            "盖巴尔先生能早点出院啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "护士们都有各自的工作在身，\x01",
            "可没有闲工夫去应付\x01",
            "装病的人啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_218A")

    label("loc_212F")


    #C0137
    ChrTalk(
        0xB,
        (
            "……唉，但既然名义上算是病人，\x01",
            "也总不能硬赶他出去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        "只能等他待到腻烦为止吗……\x02",
    )

    CloseMessageWindow()

    label("loc_218A")

    Jump("loc_2ADE")

    label("loc_218F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_224A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2201")

    #C0139
    ChrTalk(
        0xB,
        (
            "……呼。\x01",
            "管理护士们\x01",
            "其实也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "不过，塞茜尔来了之后，\x01",
            "多少就轻松了点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2245")

    label("loc_2201")


    #C0141
    ChrTalk(
        0xB,
        (
            "我让塞茜尔\x01",
            "负责相当于\x01",
            "护士主任的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        "她可帮了我大忙呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2245")

    Jump("loc_2ADE")

    label("loc_224A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2308")

    #C0143
    ChrTalk(
        0xB,
        "菲莉亚还差得远呢。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "虽然工作时间是不能吃东西，\x01",
            "但也不用那么认真地\x01",
            "等待午休吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "完全可以在走路时，或者趁我不注意时，\x01",
            "三口两口把东西吃掉啊！\x01",
            "这点胆量还是该有的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_2308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BF")

    #C0146
    ChrTalk(
        0xB,
        (
            "塞茜尔去小滴的\x01",
            "病房了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "……小滴这孩子的情况也很难办呢。\x01",
            "大概因为母亲去世得早，\x01",
            "所以态度总是很老成。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "我倒是觉得，她可以\x01",
            "再多一点孩子气的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2424")

    label("loc_23BF")


    #C0149
    ChrTalk(
        0xB,
        (
            "小滴她\x01",
            "大概是因为母亲去世得早，\x01",
            "所以态度总是很老成。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "我倒是觉得，她可以\x01",
            "再多一点孩子气的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2424")

    Jump("loc_2ADE")

    label("loc_2429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2498")

    #C0151
    ChrTalk(
        0xB,
        (
            "你问我？\x01",
            "昨天当然也出勤了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "病人可是等不得的嘛。\x01",
            "我们基本上是没有休假的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2500")

    label("loc_2498")


    #C0153
    ChrTalk(
        0xB,
        (
            "为了预防突然有患者被送来，\x01",
            "医院是不能休息的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "约亚西姆医生有偷懒的习惯，\x01",
            "真是令人伤脑筋呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2500")

    Jump("loc_2ADE")

    label("loc_2505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2594")

    #C0155
    ChrTalk(
        0xB,
        (
            "在听说塞茜尔是那个伊莉娅·普拉提耶\x01",
            "的朋友之后，女孩子们好像\x01",
            "都兴奋不已呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "真是的，多少也学学\x01",
            "塞茜尔努力工作的样子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_26D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2688")

    #C0157
    ChrTalk(
        0xB,
        (
            "彩虹剧团的公演传单\x01",
            "也发到医院来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "我年轻的时候，\x01",
            "伊莉娅·普拉提耶还没有加入彩虹剧团，\x01",
            "剧团也没有现在这么有名。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "现在彩虹已经成为名震克洛斯贝尔的\x01",
            "实力派剧团……\x01",
            "感觉他们在成功之路上真是越走越远了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_26CC")

    label("loc_2688")


    #C0160
    ChrTalk(
        0xB,
        (
            "彩虹剧团的表演……\x01",
            "我年轻的时候也经常去看呢。\x01",
            "啊，好怀念呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26CC")

    Jump("loc_2ADE")

    label("loc_26D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_27A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_2745")

    #C0161
    ChrTalk(
        0xB,
        (
            "话说回来……\x01",
            "那个小缇欧\x01",
            "竟然都长得这么大了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "今天已经要回去了吧？\x01",
            "有时间再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27A2")

    label("loc_2745")


    #C0163
    ChrTalk(
        0xB,
        (
            "多亏你们，\x01",
            "应该不会再发生\x01",
            "魔兽侵害了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "请让我代替工作人员和病人们\x01",
            "向你们道声谢吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A2")

    Jump("loc_2ADE")

    label("loc_27A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_294F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_28E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2857")

    #C0165
    ChrTalk(
        0xB,
        (
            "只要是见过一次的病人，\x01",
            "我就一定不会忘记……\x01",
            "哎呀，但这次真是差点没认出来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xB,
        (
            "缇欧，下次再来哦。\x01",
            "要是有机会的话，\x01",
            "再一起慢慢聊吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_28DE")

    label("loc_2857")


    #C0167
    ChrTalk(
        0xB,
        (
            "对了对了，塞茜尔\x01",
            "就在三楼最里面的病房哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "那里住的是个情况特殊，\x01",
            "但是非常乖的好孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "方便的话，希望\x01",
            "你们也能去看看她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DE")

    Jump("loc_294A")

    label("loc_28E3")


    #C0170
    ChrTalk(
        0xB,
        (
            "啊，抱歉哦。\x01",
            "我现在正在记账，\x01",
            "腾不出手来。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "不好意思，要是有事的话，\x01",
            "能不能去问外面的菲莉亚？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294A")

    Jump("loc_2ADE")

    label("loc_294F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A84")

    #C0172
    ChrTalk(
        0xB,
        (
            "哎呀，塞茜尔。\x01",
            "是在给客人带路吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x136,
        "#1300F是的，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "塞茜尔向护士长说明了事由。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "原来如此，既然是这样，\x01",
            "你就给他们带路吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        (
            "你们是那个什么支援科的吧？\x01",
            "调查就拜托你们了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0005F是、是的。\x01",
            "（好有魄力的人啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x103,
        "#0208F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AD0")

    label("loc_2A84")


    #C0179
    ChrTalk(
        0xB,
        (
            "要是真的有魔兽出没，\x01",
            "情况可就严重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "你们几位，\x01",
            "可要努力调查哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD0")

    Jump("loc_2ADE")

    label("loc_2AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2ADE")

    label("loc_2ADE")

    TalkEnd(0xB)

    label("loc_2AE1")

    Return()

    # Function_6_1C75 end

    def Function_7_2AE2(): pass

    label("Function_7_2AE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B00")
    Call(1, 2)
    Jump("loc_2B58")

    label("loc_2B00")


    #C0181
    ChrTalk(
        0xFE,
        (
            "唉～这孩子\x01",
            "真是让人难以理解啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "我发现，拜托希伦办事\x01",
            "从根本上就是个错误……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B58")

    Jump("loc_3604")

    label("loc_2B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2B6B")
    Jump("loc_3604")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6B")

    #C0183
    ChrTalk(
        0xFE,
        (
            "我们医院使用的床单\x01",
            "是从贸易商哈罗德先生那里购买的。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "之前拜托希伦写了订单……\x01",
            "明明说要订五十张的，\x01",
            "但她竟然订了五百张。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "五百张啊，五百张！\x01",
            "幸好哈罗德先生发现\x01",
            "情况不对，马上告诉了我……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "但希伦她真是让人头疼啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CE0")

    label("loc_2C6B")


    #C0187
    ChrTalk(
        0xFE,
        (
            "如果贸易商不是哈罗德先生，\x01",
            "肯定就会强迫我们买下\x01",
            "五百张床单吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "真是的，希伦虽然爱犯迷糊，\x01",
            "运气倒是很强……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE0")

    Jump("loc_3604")

    label("loc_2CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2F52")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D57")

    #C0189
    ChrTalk(
        0xFE,
        (
            "其实，那条丝带\x01",
            "是希伦怂恿我\x01",
            "买的。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "希伦真是的，\x01",
            "到底要怎样捉弄我\x01",
            "才会甘心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F4D")

    label("loc_2D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_2DD5")

    #C0191
    ChrTalk(
        0xFE,
        (
            "不用将丝带白白扔掉，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "这种长度的话，\x01",
            "应该可以用来包装哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "请加油继续收集材料吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F4D")

    label("loc_2DD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2DE9")
    Call(1, 49)
    Jump("loc_2F4D")

    label("loc_2DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB3")

    #C0194
    ChrTalk(
        0xFE,
        (
            "……希伦那家伙，最近才刚安分了没多久，\x01",
            "结果就又闯祸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "她竟然把刚从雷米菲利亚\x01",
            "送来的输血用血液包\x01",
            "放进了家庭用的冷柜！\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "我毫不知情地打开时，\x01",
            "真是吓得连心脏都要跳出来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F4D")

    label("loc_2EB3")


    #C0197
    ChrTalk(
        0xFE,
        (
            "希伦的那些失误，\x01",
            "可不是一般形容为『天生迷糊』\x01",
            "的那种可爱小错误。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "竟然把输血用的血液包\x01",
            "放进家庭用的冷柜保存……\x01",
            "这根本就是恐怖分子啊，恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4D")

    Jump("loc_3604")

    label("loc_2F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2F60")
    Jump("loc_3604")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2F6E")
    Jump("loc_3604")

    label("loc_2F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3015")

    #C0199
    ChrTalk(
        0xFE,
        (
            "希伦那家伙……\x01",
            "竟然擅自把我的\x01",
            "居家服拿到别处去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "没了那个，我在房间里\x01",
            "也只能穿着护士服……\x01",
            "我得赶快抓住希伦，好好盘问一番才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_304C")

    label("loc_3015")


    #C0201
    ChrTalk(
        0xFE,
        (
            "希伦那家伙……跑到哪里去了？\x01",
            "快把我的衣服还回来～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304C")

    Jump("loc_3604")

    label("loc_3051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_30B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306C")
    Call(1, 2)
    Jump("loc_30AE")

    label("loc_306C")


    #C0202
    ChrTalk(
        0xFE,
        (
            "小滴也是，\x01",
            "米海尔也是……\x01",
            "虽然只是小孩子，但还真是坚强呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AE")

    Jump("loc_3604")

    label("loc_30B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_30C1")
    Jump("loc_3604")

    label("loc_30C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_30CF")
    Jump("loc_3604")

    label("loc_30CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_31D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316C")

    #C0203
    ChrTalk(
        0xFE,
        (
            "……唔唔……\x01",
            "我总感觉，希伦那家伙\x01",
            "好像又在哪里做什么奇怪的事了……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "……真讨厌啊。\x01",
            "相处的时间一长，\x01",
            "就会有种奇怪的直觉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31CB")

    label("loc_316C")


    #C0205
    ChrTalk(
        0xFE,
        (
            "唉……就算是希伦，\x01",
            "量体温这种小事总该做得来吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "保险起见，待会还是去看看情况吧……\x02",
    )

    CloseMessageWindow()

    label("loc_31CB")

    Jump("loc_3604")

    label("loc_31D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_339E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3308")

    #C0207
    ChrTalk(
        0xFE,
        (
            "我的同事希伦是个冒失鬼，\x01",
            "而且是非同寻常的冒失。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "像使用医疗器具时出现失误，险些引发医疗事故啦，\x01",
            "还有把危险的药品洒在地上之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "只是，在酿成大错之前，\x01",
            "她周围的人都会努力补救，\x01",
            "所以才能一直将受害人数保持为零。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "唉，她要是能有塞茜尔前辈\x01",
            "的一个小指头尖可靠就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3399")

    label("loc_3308")


    #C0211
    ChrTalk(
        0xFE,
        (
            "希伦的冒失程度可是非同寻常的。\x01",
            "至今为止居然都没有受害者出现，\x01",
            "真是太不可思议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "唉，她要是能有塞茜尔前辈\x01",
            "的一个小指头尖可靠就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3399")

    Jump("loc_3604")

    label("loc_339E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_348D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3455")

    #C0213
    ChrTalk(
        0xFE,
        "呃啊～太慢了！\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "希伦那家伙，\x01",
            "不过就是晒个床单而已，\x01",
            "到底要花多长时间啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "啊啊，我总有种不祥的预感……\x01",
            "感觉好不容易洗干净的\x01",
            "床单又要被弄脏了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3488")

    label("loc_3455")


    #C0216
    ChrTalk(
        0xFE,
        (
            "希伦那家伙……\x01",
            "不会把洗好的床单又弄脏了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3488")

    Jump("loc_3604")

    label("loc_348D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_3506")

    #C0217
    ChrTalk(
        0xFE,
        (
            "希伦那家伙，\x01",
            "有没有向盖巴尔议员\x01",
            "好好道歉啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "那孩子实在是太冒失了，\x01",
            "出了什么问题都不稀奇呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3604")

    label("loc_3506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3574")

    #C0219
    ChrTalk(
        0xFE,
        "哎，塞茜尔前辈？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "嗯～我想她应该还没回\x01",
            "护士中心……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "是不是直接\x01",
            "去做其它工作了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3604")

    label("loc_3574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_35FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358F")
    Call(1, 2)
    Jump("loc_35F6")

    label("loc_358F")


    #C0222
    ChrTalk(
        0xFE,
        (
            "希伦真是的，\x01",
            "总是会犯些\x01",
            "不小的失误。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "可不知为何，在病人之中反倒很受欢迎……\x01",
            "真是莫名其妙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F6")

    Jump("loc_3604")

    label("loc_35FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3604")

    label("loc_3604")

    TalkEnd(0xFE)
    Return()

    # Function_7_2AE2 end

    def Function_8_3608(): pass

    label("Function_8_3608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3619")
    Jump("loc_3D9A")

    label("loc_3619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3627")
    Jump("loc_3D9A")

    label("loc_3627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3635")
    Jump("loc_3D9A")

    label("loc_3635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3643")
    Jump("loc_3D9A")

    label("loc_3643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3651")
    Jump("loc_3D9A")

    label("loc_3651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_365F")
    Jump("loc_3D9A")

    label("loc_365F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_366D")
    Jump("loc_3D9A")

    label("loc_366D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_367B")
    Jump("loc_3D9A")

    label("loc_367B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3689")
    Jump("loc_3D9A")

    label("loc_3689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3804")

    #C0224
    ChrTalk(
        0xD,
        (
            "#1302F哎呀，罗伊德。\x01",
            "这么快就开始工作了呀。\x02\x03",

            "#1309F呵呵……\x01",
            "大家都过了个有意义的假日吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#0102F是呀……\x01",
            "好久都没有回过家了，总算回去待了一天。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x103,
        "#0202F……嗯，算是稍微清闲了一下呢。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        (
            "#0306F唉，不过只有一天，\x01",
            "这假期也太短了啊。\x02\x03",

            "#0300F其实还想和塞茜尔小姐\x01",
            "一起去玩呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#0004F（嗯～虽然发生了不少事，\x01",
            "  但那天还算是充实吧……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 5)
    Jump("loc_38FB")

    label("loc_3804")


    #C0229
    ChrTalk(
        0xD,
        (
            "#1304F我昨天度过了一个很有意义\x01",
            "的假日呢，伊莉娅还把\x01",
            "莉夏小姐介绍给我了……\x02\x03",

            "#1302F对了对了，伊莉娅还说，\x01",
            "原本应该也邀请罗伊德来的，\x01",
            "你没来，她觉得很遗憾呢。\x02\x03",

            "#1309F呵呵，罗伊德还真受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#0012F我怎么觉得自己只是\x01",
            "被她当成了玩具呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38FB")

    Jump("loc_3D9A")

    label("loc_3900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B59")

    #C0231
    ChrTalk(
        0xD,
        (
            "#1300F啊，罗伊德。\x01",
            "来得正好。\x02\x03",

            "其实呢，伊莉娅\x01",
            "给了我两张下个月的\x01",
            "彩虹剧团公演门票。\x02\x03",

            "#1309F要是行程有空的话，\x01",
            "要不要一起去呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#0009F好啊，太感谢了！\x01",
            "真是求之不得呢。\x02\x03",

            "#0004F虽然工作很忙，\x01",
            "不知道能否抽出时间……\x01",
            "但真想去看看啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xD,
        (
            "#1309F呵呵，明白了。\x01",
            "那我就帮你把票留着了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#0004F（从那排练的情景来看……\x01",
            "  正式演出时一定会更加精彩吧。\x01",
            "  ……………………嗯？）\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x103,
        "#0211F（瞪～…………）\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#0111F（竟然在工作中敲定了约会呢，\x01",
            "  ……真是好大的派头。）\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x104,
        (
            "#0301F（这个混蛋弟弟……\x01",
            "  为什么只有你……！！）\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        "#0006F（呜……大家的视线好锐利……！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 4)
    Jump("loc_3BDC")

    label("loc_3B59")


    #C0239
    ChrTalk(
        0xD,
        (
            "#1300F彩虹剧团的公演……\x01",
            "真希望能一起去看啊。\x02\x03",

            "#1309F呵呵，期待你能请到假哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#0011F是、是啊……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        "#0211F（瞪～……）\x02",
    )

    CloseMessageWindow()

    label("loc_3BDC")

    Jump("loc_3D9A")

    label("loc_3BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3BEF")
    Jump("loc_3D9A")

    label("loc_3BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE4")

    #C0242
    ChrTalk(
        0xD,
        "#1305F哎呀，罗伊德，忘了什么东西吗？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#0000F不，倒不是\x01",
            "因为这个……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xD,
        (
            "#1305F啊，难不成……\x01",
            "你是来向我汇报的吗！？\x02\x03",

            "#1309F艾莉、缇欧\x01",
            "和兰迪……\x02\x03",

            "最后，你决定\x01",
            "要和谁交往了？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#0006F……也不是为了这个啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3D70")

    label("loc_3CE4")


    #C0246
    ChrTalk(
        0xD,
        (
            "#1300F呵呵，开个玩笑啦。\x02\x03",

            "要是再有什么事的话……\x01",
            "不，就算没什么事，\x01",
            "也可以再来找我哦。\x02\x03",

            "#1304F……那么，\x01",
            "我还要去给小滴\x01",
            "送晚餐才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D70")

    Jump("loc_3D9A")

    label("loc_3D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3D83")
    Jump("loc_3D9A")

    label("loc_3D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3D91")
    Jump("loc_3D9A")

    label("loc_3D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3D9A")

    label("loc_3D9A")

    TalkEnd(0xFE)
    Return()

    # Function_8_3608 end

    def Function_9_3D9E(): pass

    label("Function_9_3D9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3E02")
    OP_93(0xFE, 0x0, 0x0)

    #C0247
    ChrTalk(
        0xFE,
        (
            "虽然只是个小手术，\x01",
            "但也不可轻视哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "……要安心静养哦，\x01",
            "知道了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4515")

    label("loc_3E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3E65")

    #C0249
    ChrTalk(
        0xFE,
        (
            "那位病人……\x01",
            "似乎也没有\x01",
            "乱发脾气的表现。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "……总之，看起来像是\x01",
            "讲道理的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4515")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5B")

    #C0251
    ChrTalk(
        0xFE,
        (
            "今天早上，有几名伤员被送到了医院。\x01",
            "据说他们都隶属于一个名为『黑月』的组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "然后，有一个人恢复到可以\x01",
            "开口说话了，就被转移到这边来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "可是，那种伤势……\x01",
            "明显不是普通人会受的伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        "真是些可疑的人啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3FF4")

    label("loc_3F5B")


    #C0255
    ChrTalk(
        0xFE,
        (
            "今早入院的那些\x01",
            "黑月公司的职员……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "除了转移到这个病房的人以外，\x01",
            "都还需要继续静养。\x01",
            "他们应该睡在ＩＣＵ病房吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "不过……还真是些可疑的人啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3FF4")

    Jump("loc_4515")

    label("loc_3FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4007")
    Jump("loc_4515")

    label("loc_4007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_41DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4177")

    #C0258
    ChrTalk(
        0xFE,
        (
            "刚才我给小滴\x01",
            "诊察过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "……以她的病情来说，\x01",
            "凭现在的医疗技术，很难完全治愈。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "外科、内科、神经科……\x01",
            "各个领域的问题错综复杂，相互干涉，\x01",
            "阻碍了治疗的进行。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "因为还没有完全失明，\x01",
            "所以还有极小的治愈可能……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    #C0262
    ChrTalk(
        0xFE,
        (
            "……我真是的，\x01",
            "竟然将病人的情况说了出来，\x01",
            "真是太轻率了。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        "……刚才的话请你们忘了吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_41D7")

    label("loc_4177")


    #C0264
    ChrTalk(
        0xFE,
        (
            "……我真是的，\x01",
            "竟然将病人的情况说了出来，\x01",
            "真是太轻率了。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "……刚才的话，请你们忘掉吧。\x02",
    )

    CloseMessageWindow()

    label("loc_41D7")

    Jump("loc_4515")

    label("loc_41DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_41EA")
    Jump("loc_4515")

    label("loc_41EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_41F8")
    Jump("loc_4515")

    label("loc_41F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4268")

    #C0266
    ChrTalk(
        0xFE,
        "……我可没兴趣给健康的人看病哦。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "我现在要去查房。\x01",
            "趁着还没打扰到其他病人，\x01",
            "快点回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4515")

    label("loc_4268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4276")
    Jump("loc_4515")

    label("loc_4276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_436F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4324")

    #C0268
    ChrTalk(
        0xFE,
        "今天是纪念庆典第二天了吧……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "太过兴奋，注意不到周围的时候\x01",
            "便有受伤的危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "希望明天不要\x01",
            "再有克洛斯贝尔市的\x01",
            "不良团伙成员被送到这里。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_436A")

    label("loc_4324")


    #C0271
    ChrTalk(
        0xFE,
        (
            "太过兴奋，注意不到周围的时候\x01",
            "便有受伤的危险，\x01",
            "你们也多加小心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_436A")

    Jump("loc_4515")

    label("loc_436F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_43EA")

    #C0272
    ChrTalk(
        0xFE,
        (
            "这次虽然只是个小手术……\x01",
            "但我绝对不会松懈大意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "身为外科医生，\x01",
            "这是在面对手术时\x01",
            "最低限度的原则。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4515")

    label("loc_43EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4491")
    OP_93(0xFE, 0xB4, 0x0)

    #C0274
    ChrTalk(
        0xFE,
        (
            "会觉得外科手术\x01",
            "很可怕也是难免的。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "不过，这次手术的危险度\x01",
            "可以说是相当低。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "太过担心的话对身体也不好。\x01",
            "今天就请放宽心，\x01",
            "早点休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4515")

    label("loc_4491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_44F0")

    #C0277
    ChrTalk(
        0xFE,
        "接下来要去２０２号室查房。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "你不是住院患者吧？\x01",
            "趁天还没黑，赶快回家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4515")

    label("loc_44F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_44FE")
    Jump("loc_4515")

    label("loc_44FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_450C")
    Jump("loc_4515")

    label("loc_450C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4515")

    label("loc_4515")

    TalkEnd(0xFE)
    Return()

    # Function_9_3D9E end

    def Function_10_4519(): pass

    label("Function_10_4519")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452E")
    Call(1, 12)
    Jump("loc_45D6")

    label("loc_452E")


    #C0279
    ChrTalk(
        0xFE,
        (
            "从早上一直坚持到现在……\x01",
            "差不多也该撤退了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "……话说回来，黑月似乎是\x01",
            "相当难缠的对手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "我是第一次跟他们交涉，\x01",
            "感觉就连底层的成员\x01",
            "也都很有组织纪律性。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45D6")

    TalkEnd(0xFE)
    Return()

    # Function_10_4519 end

    def Function_11_45DA(): pass

    label("Function_11_45DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45EF")
    Call(1, 12)
    Jump("loc_4678")

    label("loc_45EF")


    #C0282
    ChrTalk(
        0xFE,
        (
            "可恶，搜查一科的那些家伙，\x01",
            "我早就看他们不顺眼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "平时总是理直气壮地\x01",
            "强行接管我们处理的事件，\x01",
            "到这种时候却又把人呼来唤去……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4678")

    TalkEnd(0xFE)
    Return()

    # Function_11_45DA end

    def Function_12_467C(): pass

    label("Function_12_467C")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    TurnDirection(0xF, 0x0, 0)
    TurnDirection(0x10, 0x0, 0)

    #C0284
    ChrTalk(
        0xF,
        "嘁，那就是黑月吗？\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xF,
        (
            "说话都统一口径，\x01",
            "真是不讨人喜欢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x102,
        (
            "#0105F警督，你们是来找黑月成员们\x01",
            "询问案情的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x10,
        (
            "是受搜查一科的请求才来的～\x01",
            "他们要我们去找住院的成员们做笔录。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x10,
        (
            "但那些人的口风实在太紧，\x01",
            "根本不可能露出破绽的～\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x10,
        (
            "可恶，搜查一科的混蛋们。\x01",
            "肯定是明知如此，才把工作推给我们的～！\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0011F哈哈……\x01",
            "（大概只是被派来做个\x01",
            "  形式上的笔录吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        "#0306F（搜查二科也够辛苦啊。）\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x0)
    OP_93(0x10, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_12_467C end

    def Function_13_4891(): pass

    label("Function_13_4891")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4925")
    Jump("loc_496F")

    label("loc_4925")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4945")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_496F")

    label("loc_4945")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4965")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_496F")

    label("loc_4965")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_496F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_49A2")
    Jump("loc_4A5B")

    label("loc_49A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_49E3")

    #C0292
    ChrTalk(
        0xFE,
        (
            "都傍晚了吗……\x01",
            "一直睡着，就感觉一天过得很快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5B")

    label("loc_49E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_49F1")
    Jump("loc_4A5B")

    label("loc_49F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4A52")

    #C0293
    ChrTalk(
        0xFE,
        (
            "虽说还在实习，\x01",
            "但医生竟然会受伤住院。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        "这就是所谓的勤于谋人、疏于谋己吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A5B")

    label("loc_4A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4A5B")

    label("loc_4A5B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_4891 end

    def Function_14_4A63(): pass

    label("Function_14_4A63")

    TalkBegin(0xFE)

    #C0295
    ChrTalk(
        0xFE,
        (
            "从刚才起就一直吵吵嚷嚷的。\x01",
            "难道就不能安静点吗。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_4A63 end

    def Function_15_4A9F(): pass

    label("Function_15_4A9F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B33")
    Jump("loc_4B7D")

    label("loc_4B33")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B53")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B7D")

    label("loc_4B53")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B73")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B7D")

    label("loc_4B73")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B7D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4BB0")
    Jump("loc_4D82")

    label("loc_4BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4BD8")

    #C0296
    ChrTalk(
        0xFE,
        "住院生活真是闲啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D82")

    label("loc_4BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4C07")

    #C0297
    ChrTalk(
        0xFE,
        (
            "那位美女护士\x01",
            "可没来这里哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D82")

    label("loc_4C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CFA")

    #C0298
    ChrTalk(
        0xFE,
        (
            "什、什么啊……\x01",
            "刚才那个戴眼镜的医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "本以为他要谈谈治疗的事情，\x01",
            "没想到一开口就是Ｓ啊Ｍ啊什么的……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x136,
        (
            "#1306F对不起，\x01",
            "请不要太放在心上。\x01",
            "约亚西姆医生就是那种人……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x103,
        "#0200F……就这么纵容他也不太好吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4D74")

    label("loc_4CFA")


    #C0302
    ChrTalk(
        0xFE,
        (
            "刚才那位戴眼镜的医生……\x01",
            "怎么看都不像是个医生啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "但说到副教授，那就是地位仅次于\x01",
            "教授的人了，应该很了不起吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D74")

    Jump("loc_4D82")

    label("loc_4D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4D82")

    label("loc_4D82")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_4A9F end

    def Function_16_4D8A(): pass

    label("Function_16_4D8A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E1E")
    Jump("loc_4E68")

    label("loc_4E1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E3E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E68")

    label("loc_4E3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E68")

    label("loc_4E5E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E68")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4E9B")
    Jump("loc_4FCE")

    label("loc_4E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4EF2")

    #C0304
    ChrTalk(
        0xFE,
        "那位老婆婆，好像很幸福呢。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "嗯～我也要好好加油，\x01",
            "直到痊愈出院。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FCE")

    label("loc_4EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4F60")

    #C0306
    ChrTalk(
        0xFE,
        (
            "那位老婆婆……\x01",
            "好像有孙女来看她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "她总是在抱怨，说没人来看她，\x01",
            "但现在不是挺好的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FCE")

    label("loc_4F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4FC5")

    #C0308
    ChrTalk(
        0xFE,
        (
            "唉，那位老婆婆……\x01",
            "总是在抱怨\x01",
            "没人来看她。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "连我都觉得郁闷起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FCE")

    label("loc_4FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4FCE")

    label("loc_4FCE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_4D8A end

    def Function_17_4FD6(): pass

    label("Function_17_4FD6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_506A")
    Jump("loc_50B4")

    label("loc_506A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_508A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B4")

    label("loc_508A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50AA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B4")

    label("loc_50AA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50B4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_50E7")
    Jump("loc_52AE")

    label("loc_50E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_515F")

    #C0310
    ChrTalk(
        0xFE,
        (
            "孙女来看我了，\x01",
            "不过我让她趁着天还没黑，快点回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "唔……多亏了她，总算是精神点了。\x01",
            "我得加油啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52AE")

    label("loc_515F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517A")
    Call(1, 19)
    Jump("loc_520C")

    label("loc_517A")


    #C0312
    ChrTalk(
        0xFE,
        (
            "孙女自己一个人\x01",
            "特意过来看我……\x01",
            "没有比这更令人开心的事啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "她说我的儿子和儿媳\x01",
            "都相当忙碌……\x01",
            "真为自己之前那迁怒于他们的想法感到羞愧啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_520C")

    Jump("loc_52AE")

    label("loc_5211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_52A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_END)), "loc_5235")
    Call(1, 18)
    Jump("loc_527F")

    label("loc_5235")


    #C0314
    ChrTalk(
        0xFE,
        (
            "住院之后到现在，\x01",
            "没有一个家人来看我……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "唉，好想念孙女啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_527F")

    Jump("loc_52A0")

    label("loc_5284")


    #C0316
    ChrTalk(
        0xFE,
        "唉……好想念孙女啊……\x02",
    )

    CloseMessageWindow()

    label("loc_52A0")

    Jump("loc_52AE")

    label("loc_52A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_52AE")

    label("loc_52AE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_4FD6 end

    def Function_18_52B6(): pass

    label("Function_18_52B6")

    OP_93(0x30, 0xB4, 0x0)
    SetChrSubChip(0x15, 0x2)
    OP_4B(0x30, 0xFF)

    #C0317
    ChrTalk(
        0x15,
        (
            "住院之后到现在，\x01",
            "没有一个家人来看我……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x15,
        "唉，好想念孙女啊……\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x15,
        (
            "我可不管儿子儿媳忙不忙，\x01",
            "他们也太不关心人了！\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x30,
        (
            "#2406F是啊……\x01",
            "嗯，真是可悲可叹啊。\x02\x03",

            "#2400F不过，既然您这么精神，\x01",
            "大概用不了多久就能出院吧。\x01",
            "很快就能见到孙女啦。\x02\x03",

            "#2409F对了，吃不吃点心啊？\x01",
            "可以让人镇定下来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x15,
        (
            "唉，会对我这么体贴的人，\x01",
            "也只有医生啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        "#0005F（真、真是位奇怪的医生啊……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x30, 0xFF)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_18_52B6 end

    def Function_19_544F(): pass

    label("Function_19_544F")

    TurnDirection(0x16, 0x15, 0)
    SetChrSubChip(0x15, 0x2)
    OP_4B(0x16, 0xFF)

    #C0323
    ChrTalk(
        0x16,
        (
            "奶奶，听我说！\x01",
            "我还是第一次\x01",
            "一个人坐定期巴士哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x16,
        (
            "比和爸爸妈妈一起乘坐\x01",
            "还要让人兴奋，好开心啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x15,
        "是吗是吗，真了不起呀。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x15,
        (
            "来，把约亚西姆医生刚才\x01",
            "送我的糖球给你吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x16,
        "哇～谢谢！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_19_544F end

    def Function_20_5530(): pass

    label("Function_20_5530")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5545")
    Call(1, 19)
    Jump("loc_5570")

    label("loc_5545")


    #C0328
    ChrTalk(
        0xFE,
        (
            "奶奶比我想象的还有精神，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5570")

    TalkEnd(0xFE)
    Return()

    # Function_20_5530 end

    def Function_21_5574(): pass

    label("Function_21_5574")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5608")
    Jump("loc_5652")

    label("loc_5608")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5628")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5652")

    label("loc_5628")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5648")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5652")

    label("loc_5648")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5652")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0329
    ChrTalk(
        0xFE,
        (
            "虽然膝盖还有些痛，\x01",
            "但看今天的情况，离出院也不远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "呵呵，真令人期待啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_5574 end

    def Function_22_56D2(): pass

    label("Function_22_56D2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5766")
    Jump("loc_57B0")

    label("loc_5766")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5786")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B0")

    label("loc_5786")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57A6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B0")

    label("loc_57A6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57B0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_57E3")
    Jump("loc_5899")

    label("loc_57E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_584D")

    #C0331
    ChrTalk(
        0xFE,
        (
            "今、今天终于要动手术了，\x01",
            "主刀医生似乎是\x01",
            "这位贝尔达因医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "……唉，真是好紧张啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5899")

    label("loc_584D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5899")

    #C0333
    ChrTalk(
        0xFE,
        "唉……好郁闷啊。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "虽然医生说是个小手术，\x01",
            "叫我不要担心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5899")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_56D2 end

    def Function_23_58A1(): pass

    label("Function_23_58A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_58B2")
    Jump("loc_5915")

    label("loc_58B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_58F2")

    #C0335
    ChrTalk(
        0xFE,
        "嗯咕～……嗯咕～……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        "呼啊啊，嗯咕～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5915")

    label("loc_58F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5915")

    #C0337
    ChrTalk(
        0xFE,
        "嗯咕～……嗯咕～……\x02",
    )

    CloseMessageWindow()

    label("loc_5915")

    TalkEnd(0xFE)
    Return()

    # Function_23_58A1 end

    def Function_24_5919(): pass

    label("Function_24_5919")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_59AD")
    Jump("loc_59F7")

    label("loc_59AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_59CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59F7")

    label("loc_59CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59F7")

    label("loc_59ED")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59F7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5A2A")
    Jump("loc_5B0E")

    label("loc_5A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5AA9")

    #C0338
    ChrTalk(
        0xFE,
        (
            "这家医院待着很舒服，\x01",
            "住下就不想走了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "医生和护士们都很温柔……\x01",
            "呵呵，要是不想出院了，\x01",
            "可该怎么办呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B0E")

    label("loc_5AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B0E")

    #C0340
    ChrTalk(
        0xFE,
        (
            "医院的床睡着很舒服呢。\x01",
            "即使一声不吭，也会有饭菜端过来，\x01",
            "有多少年没享受过这种生活了啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B0E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_5919 end

    def Function_25_5B16(): pass

    label("Function_25_5B16")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BAA")
    Jump("loc_5BF4")

    label("loc_5BAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BCA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BF4")

    label("loc_5BCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BEA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BF4")

    label("loc_5BEA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BF4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C27")
    Jump("loc_5CF0")

    label("loc_5C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5C70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C42")
    Call(1, 3)
    Jump("loc_5C6B")

    label("loc_5C42")


    #C0341
    ChrTalk(
        0xFE,
        (
            "到底要怎么做\x01",
            "才能折断体温计啊……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C6B")

    Jump("loc_5CF0")

    label("loc_5C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C8B")
    Call(1, 3)
    Jump("loc_5CF0")

    label("loc_5C8B")


    #C0342
    ChrTalk(
        0xFE,
        (
            "……面对这位冒失的护士小姐，\x01",
            "真是有几条命都不够赔的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "不过……看她那么可爱，也就算了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5CF0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_5B16 end

    def Function_26_5CF8(): pass

    label("Function_26_5CF8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1C)
    ClearChrFlags(0x1C, 0x10)
    TurnDirection(0x1C, 0x0, 0)
    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D8C")
    Jump("loc_5DD6")

    label("loc_5D8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5DAC")
    OP_52(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DD6")

    label("loc_5DAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DCC")
    OP_52(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DD6")

    label("loc_5DCC")

    OP_52(0x1C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DD6")

    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1C, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5E09")
    Jump("loc_5F96")

    label("loc_5E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5E9A")

    #C0344
    ChrTalk(
        0x1C,
        (
            "自从我藏起来的写真杂志被发现以后，\x01",
            "就感觉护士们的眼神\x01",
            "都变得冷淡起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x1C,
        (
            "都怪对面那个大叔，\x01",
            "硬把那种杂志塞给我啦……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F96")

    label("loc_5E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5F0E")

    #C0346
    ChrTalk(
        0x1C,
        (
            "对面那个大叔昨天\x01",
            "给我的写真杂志……\x01",
            "在量体温的时候被发现了。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x1C,
        "我真是从来都没有那么丢人过……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F96")

    label("loc_5F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5F4F")

    #C0348
    ChrTalk(
        0x1C,
        (
            "（……这个人，真的是\x01",
            "  很厉害的医生吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F96")

    label("loc_5F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5F96")

    #C0349
    ChrTalk(
        0x1C,
        (
            "唉～唉……\x01",
            "要是没受这种伤的话，\x01",
            "现在应该正在享受庆典了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F96")

    SetChrSubChip(0x1C, 0x0)
    TalkEnd(0x1C)
    Return()

    # Function_26_5CF8 end

    def Function_27_5F9E(): pass

    label("Function_27_5F9E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6032")
    Jump("loc_607C")

    label("loc_6032")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6052")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_607C")

    label("loc_6052")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6072")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_607C")

    label("loc_6072")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_607C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_60AF")
    Jump("loc_62B5")

    label("loc_60AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6146")

    #C0350
    ChrTalk(
        0xFE,
        (
            "自从把写真杂志送给对面的孩子\x01",
            "之后，他就经常瞪着我。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "嗯～莫非是还想要吗？\x01",
            "没办法，作为友好的证明，\x01",
            "再送他一本我珍藏的好杂志吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B5")

    label("loc_6146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_61B5")

    #C0352
    ChrTalk(
        0xFE,
        (
            "我昨天送了本写真杂志\x01",
            "给对面的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "看他量体温时\x01",
            "那慌张的样子，\x01",
            "似乎已经精神起来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B5")

    label("loc_61B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_624F")

    #C0354
    ChrTalk(
        0xFE,
        (
            "大叔我在跟人交往的时候，\x01",
            "都会赠送自己收藏的写真杂志，\x01",
            "当做见面礼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生\x01",
            "很爽快地就收下了哦。\x01",
            "哎呀，真是个容易亲近的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B5")

    label("loc_624F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_62B5")

    #C0356
    ChrTalk(
        0xFE,
        (
            "对面床位的孩子，\x01",
            "怎么无精打采的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "没办法，偷偷送他一本\x01",
            "大叔我秘藏的\x01",
            "写真杂志吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62B5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_5F9E end

    def Function_28_62BD(): pass

    label("Function_28_62BD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6351")
    Jump("loc_639B")

    label("loc_6351")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6371")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_639B")

    label("loc_6371")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6391")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_639B")

    label("loc_6391")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_639B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_63CE")
    Jump("loc_6547")

    label("loc_63CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_643B")

    #C0358
    ChrTalk(
        0xFE,
        (
            "我调查了一下今天来\x01",
            "查房的医生……\x01",
            "盖里教授是谁啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "我想让约亚西姆医生\x01",
            "来帮我诊察呀！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6547")

    label("loc_643B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6456")
    Call(1, 47)
    Jump("loc_647D")

    label("loc_6456")


    #C0360
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生\x01",
            "就是爱害羞，真是的⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_647D")

    Jump("loc_6547")

    label("loc_6482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_64DC")

    #C0361
    ChrTalk(
        0xFE,
        "约亚西姆医生好像还是单身呢～\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "呵呵，让我来\x01",
            "填补医生\x01",
            "心中的空虚吧⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6547")

    label("loc_64DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6547")

    #C0363
    ChrTalk(
        0xFE,
        (
            "啊啊，约亚西姆医生\x01",
            "怎么还不来查房呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "那种超然于世的感觉……\x01",
            "是阿姨我最喜欢的类型呀～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6547")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_62BD end

    def Function_29_654F(): pass

    label("Function_29_654F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_65E3")
    Jump("loc_662D")

    label("loc_65E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6603")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_662D")

    label("loc_6603")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6623")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_662D")

    label("loc_6623")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_662D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6660")
    Jump("loc_67B3")

    label("loc_6660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_66AD")

    #C0365
    ChrTalk(
        0xFE,
        (
            "今天预定有外科的医生\x01",
            "来查房的。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        "希望我的腰腿好些了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67B3")

    label("loc_66AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_66E8")

    #C0367
    ChrTalk(
        0xFE,
        (
            "哎呀呀，好可爱的医生。\x01",
            "一定很受欢迎吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67B3")

    label("loc_66E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6754")

    #C0368
    ChrTalk(
        0xFE,
        (
            "护士们对我\x01",
            "真的很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然也有几个奇怪的孩子……\x01",
            "但大家都是很体贴人的好孩子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67B3")

    label("loc_6754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_67B3")

    #C0370
    ChrTalk(
        0xFE,
        (
            "这家医院真是个\x01",
            "舒服的好地方呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "在腰腿感觉好些之前，\x01",
            "就在这里享受一阵子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67B3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_654F end

    def Function_30_67BB(): pass

    label("Function_30_67BB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_684F")
    Jump("loc_6899")

    label("loc_684F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_686F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6899")

    label("loc_686F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_688F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6899")

    label("loc_688F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6899")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_68CC")
    Jump("loc_69FA")

    label("loc_68CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6956")

    #C0372
    ChrTalk(
        0xFE,
        (
            "刚才量体温的时候，\x01",
            "护士小姐发现了我的\x01",
            "写真杂志。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "虽然她只是对我微笑了一下，\x01",
            "但这反而更加让人难堪……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_698C")

    label("loc_6956")


    #C0374
    ChrTalk(
        0xFE,
        (
            "唉，果然不该收下\x01",
            "旁边那个大叔给的\x01",
            "写真杂志啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698C")

    Jump("loc_69FA")

    label("loc_6991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_69FA")

    #C0375
    ChrTalk(
        0xFE,
        (
            "嘿嘿……\x01",
            "这家医院的护士小姐真漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "比起写真杂志里的美女，\x01",
            "还是现实中的美女更好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69FA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_67BB end

    def Function_31_6A02(): pass

    label("Function_31_6A02")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A96")
    Jump("loc_6AE0")

    label("loc_6A96")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6AB6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AE0")

    label("loc_6AB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AD6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AE0")

    label("loc_6AD6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AE0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6B13")
    Jump("loc_6C3D")

    label("loc_6B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6BC5")

    #C0377
    ChrTalk(
        0xFE,
        "其实我已经快出院了。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "要和同病房中意气相投的朋友分别，真是很失落……\x01",
            "但这也是没办法的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "好……作为饯别礼，就把我\x01",
            "秘藏的写真杂志送给旁边的孩子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C3D")

    label("loc_6BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6C3D")

    #C0380
    ChrTalk(
        0xFE,
        (
            "作为友好的证明，\x01",
            "我送给邻床的孩子\x01",
            "好几本写真杂志。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "虽然查房的时候差点被发现……\x01",
            "啊哈哈，真是刺激啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C3D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_6A02 end

    def Function_32_6C45(): pass

    label("Function_32_6C45")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CD9")
    Jump("loc_6D23")

    label("loc_6CD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6CF9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D23")

    label("loc_6CF9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D19")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D23")

    label("loc_6D19")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D23")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6D56")
    Jump("loc_6E1B")

    label("loc_6D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6DA8")

    #C0382
    ChrTalk(
        0xFE,
        "刚才有个孩子从走廊跑过去了。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        "真是的，父母是怎么教育的啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E1B")

    label("loc_6DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6E1B")

    #C0384
    ChrTalk(
        0xFE,
        (
            "拉格教授上周给我看过病了，\x01",
            "似乎在本周之内就可以出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "乱吃东西果然很恐怖啊，\x01",
            "你们也小心点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E1B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_6C45 end

    def Function_33_6E23(): pass

    label("Function_33_6E23")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EB7")
    Jump("loc_6F01")

    label("loc_6EB7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6ED7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F01")

    label("loc_6ED7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EF7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F01")

    label("loc_6EF7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F01")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6F34")
    Jump("loc_7036")

    label("loc_6F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6FA6")

    #C0386
    ChrTalk(
        0xFE,
        "哎……你们去见过约亚西姆医生了？\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "太让人生气了～！\x01",
            "有空见这些孩子的话，\x01",
            "为什么不来查房啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7036")

    label("loc_6FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7036")

    #C0388
    ChrTalk(
        0xFE,
        (
            "我还在奇怪为什么约亚西姆医生\x01",
            "最近不来查房了呢……\x01",
            "原来不知不觉间，主治医师竟然被换了！\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "太让人生气了～！\x01",
            "约亚西姆医生太坏了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7036")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_6E23 end

    def Function_34_703E(): pass

    label("Function_34_703E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_70D2")
    Jump("loc_711C")

    label("loc_70D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70F2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_711C")

    label("loc_70F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7112")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_711C")

    label("loc_7112")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_711C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_714F")
    Jump("loc_7256")

    label("loc_714F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_71A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_716A")
    Call(1, 36)
    Jump("loc_719B")

    label("loc_716A")


    #C0390
    ChrTalk(
        0xFE,
        (
            "算、算啦，总而言之，\x01",
            "你能来看我，我很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_719B")

    Jump("loc_7256")

    label("loc_71A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7256")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722F")

    #C0391
    ChrTalk(
        0xFE,
        (
            "昨天我的朋友联络过我，\x01",
            "说是要来探望，\x01",
            "结果又没来。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "……真令人担心啊。\x01",
            "那家伙是个令人\x01",
            "难以置信的路痴呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_7256")

    label("loc_722F")


    #C0393
    ChrTalk(
        0xFE,
        (
            "那家伙真的能顺利\x01",
            "找到病房吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7256")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_703E end

    def Function_35_725E(): pass

    label("Function_35_725E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72F2")
    Jump("loc_733C")

    label("loc_72F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7312")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_733C")

    label("loc_7312")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7332")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_733C")

    label("loc_7332")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_733C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7373")
    Call(1, 36)
    Jump("loc_73B0")

    label("loc_7373")


    #C0394
    ChrTalk(
        0xFE,
        (
            "哎呀，真是累死人了。\x01",
            "不知道病房在哪里，让我找得好辛苦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73B0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_725E end

    def Function_36_73B8(): pass

    label("Function_36_73B8")

    TurnDirection(0x2D, 0x24, 0)
    SetChrSubChip(0x24, 0x1)
    OP_4B(0x2D, 0xFF)

    #C0395
    ChrTalk(
        0x2D,
        (
            "哟，\x01",
            "住院生活还算充实吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x24,
        "哈哈，你竟然找到路了啊。\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x24,
        (
            "话说，\x01",
            "进行导力通讯的时候，\x01",
            "你不是说准备昨天来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x2D,
        (
            "我是来医院了，\x01",
            "但是一直找不到病房啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x2D,
        (
            "无奈之下，只好在\x01",
            "住宿设施里住了一晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x24,
        "你果然还是个路痴啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x24, 0x0)
    OP_4C(0x2D, 0xFF)
    Return()

    # Function_36_73B8 end

    def Function_37_74BA(): pass

    label("Function_37_74BA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_754E")
    Jump("loc_7598")

    label("loc_754E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_756E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7598")

    label("loc_756E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_758E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7598")

    label("loc_758E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7598")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_761D")

    #C0401
    ChrTalk(
        0xFE,
        (
            "昨天住院的人，\x01",
            "今天早上不知何时出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "那家伙肯定是做了什么\x01",
            "亏心事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E1")

    label("loc_761D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_762B")
    Jump("loc_76E1")

    label("loc_762B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7688")

    #C0403
    ChrTalk(
        0xFE,
        (
            "那个新来的……\x01",
            "好像在斗殴中受了重伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "跟那种人同病房，不要紧吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_76E1")

    label("loc_7688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_76E1")

    #C0405
    ChrTalk(
        0xFE,
        (
            "拉格教授之前\x01",
            "来查过房了。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "能让那么厉害的医生给我看病，\x01",
            "真是太幸运了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76E1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_74BA end

    def Function_38_76E9(): pass

    label("Function_38_76E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_76FA")
    Jump("loc_7745")

    label("loc_76FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_772E")

    #C0407
    ChrTalk(
        0xFE,
        "唔……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        "呼…………呼…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_7745")

    label("loc_772E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_773C")
    Jump("loc_7745")

    label("loc_773C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7745")

    label("loc_7745")

    TalkEnd(0xFE)
    Return()

    # Function_38_76E9 end

    def Function_39_7749(): pass

    label("Function_39_7749")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_77DD")
    Jump("loc_7827")

    label("loc_77DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77FD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7827")

    label("loc_77FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_781D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7827")

    label("loc_781D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7827")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_78A6")

    #C0409
    ChrTalk(
        0xFE,
        (
            "昨天我女朋友来探病，\x01",
            "真是丢脸丢大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "多难为情啊～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79A9")

    label("loc_78A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_7908")

    #C0411
    ChrTalk(
        0xFE,
        (
            "笨……不要为了专门\x01",
            "说这种话来探病呀～！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "才没给别人添麻烦呢～\x01",
            "……真的啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79A9")

    label("loc_7908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_795B")

    #C0413
    ChrTalk(
        0xFE,
        "我女朋友今天要来探病。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "我都跟她说不用来了……\x01",
            "多难为情啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79A9")

    label("loc_795B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_79A9")

    #C0415
    ChrTalk(
        0xFE,
        (
            "嘁，医院这种地方\x01",
            "真是无聊到让人不耐烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        "赶快让我出院吧～\x02",
    )

    CloseMessageWindow()

    label("loc_79A9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_7749 end

    def Function_40_79B1(): pass

    label("Function_40_79B1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A45")
    Jump("loc_7A8F")

    label("loc_7A45")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A65")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A8F")

    label("loc_7A65")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A85")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A8F")

    label("loc_7A85")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A8F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7AC2")
    Jump("loc_7B35")

    label("loc_7AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_7B1E")
    TurnDirection(0xFE, 0x27, 0)

    #C0417
    ChrTalk(
        0xFE,
        (
            "呵呵，我放心了。\x01",
            "你看起来似乎很有精神嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "没给大家添麻烦吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B35")

    label("loc_7B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B2C")
    Jump("loc_7B35")

    label("loc_7B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7B35")

    label("loc_7B35")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_79B1 end

    def Function_41_7B3D(): pass

    label("Function_41_7B3D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7BD1")
    Jump("loc_7C1B")

    label("loc_7BD1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7BF1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C1B")

    label("loc_7BF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C11")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C1B")

    label("loc_7C11")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C1B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7CAF")

    #C0419
    ChrTalk(
        0xFE,
        (
            "同室的老爷爷\x01",
            "跟护士小姐出去散步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "嗯，真好呢。\x01",
            "我要不要也拜托\x01",
            "护士小姐带我去散步呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DA7")

    label("loc_7CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_7CEC")

    #C0421
    ChrTalk(
        0xFE,
        (
            "呵呵，病房里的人\x01",
            "都很有个性，挺有趣的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DA7")

    label("loc_7CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7D34")

    #C0422
    ChrTalk(
        0xFE,
        "哎呀哎呀，这么多人来病房……\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        "是来探望什么人吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DA7")

    label("loc_7D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7DA7")

    #C0424
    ChrTalk(
        0xFE,
        (
            "我在家都是一个人住，\x01",
            "所以觉得这种集体生活很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "大家看上去都很不错，\x01",
            "可要和他们友好相处啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DA7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_41_7B3D end

    def Function_42_7DAF(): pass

    label("Function_42_7DAF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E43")
    Jump("loc_7E8D")

    label("loc_7E43")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E63")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E8D")

    label("loc_7E63")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E83")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E8D")

    label("loc_7E83")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E8D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7F11")

    #C0426
    ChrTalk(
        0xFE,
        (
            "明天我儿子和婆婆\x01",
            "会来看我。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "婆婆这次\x01",
            "为我做了很多，\x01",
            "我得好好道谢才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8043")

    label("loc_7F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_7F5C")

    #C0428
    ChrTalk(
        0xFE,
        (
            "听说这家医院的\x01",
            "餐点水平也很高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        "呵呵，好期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8043")

    label("loc_7F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7FC6")

    #C0430
    ChrTalk(
        0xFE,
        (
            "我婆婆发来联络说，\x01",
            "下次会带我儿子来看我。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "哇哇～怎么办？\x01",
            "总觉得很过意不去啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8043")

    label("loc_7FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8043")

    #C0432
    ChrTalk(
        0xFE,
        (
            "我来住院时，\x01",
            "把儿子交给婆婆带了。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "我们之间的婆媳关系本来并不算好，\x01",
            "但没想到在关键时刻也能得到她的帮助呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8043")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_42_7DAF end

    def Function_43_804B(): pass

    label("Function_43_804B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80DF")
    Jump("loc_8129")

    label("loc_80DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80FF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8129")

    label("loc_80FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_811F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8129")

    label("loc_811F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8129")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_815C")
    Jump("loc_81F4")

    label("loc_815C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_816A")
    Jump("loc_81F4")

    label("loc_816A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8178")
    Jump("loc_81F4")

    label("loc_8178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_81F4")

    #C0434
    ChrTalk(
        0xFE,
        (
            "我觉得肚子莫名地痛了起来，\x01",
            "结果医生说是盲肠炎……什么的，\x01",
            "突然就让我住院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "啊～讨厌！\x01",
            "好想早点回家～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_804B end

    def Function_44_81FC(): pass

    label("Function_44_81FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_826D")

    #C0436
    ChrTalk(
        0xFE,
        (
            "呜～感觉肚子\x01",
            "又在一阵一阵地刺痛……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "虽然手术已经做完了，\x01",
            "但还是要再休养一阵才行吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8329")

    label("loc_826D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_82B4")

    #C0438
    ChrTalk(
        0xFE,
        (
            "……我早上刚做了手术，所以要睡觉。\x01",
            "能不能不要吵我？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8329")

    label("loc_82B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8320")

    #C0439
    ChrTalk(
        0xFE,
        (
            "呜～……我早上\x01",
            "做了治疗盲肠炎的手术。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "好痛……什么也不想干……\x01",
            "好困……肚子饿了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8329")

    label("loc_8320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8329")

    label("loc_8329")

    TalkEnd(0xFE)
    Return()

    # Function_44_81FC end

    def Function_45_832D(): pass

    label("Function_45_832D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83C1")
    Jump("loc_840B")

    label("loc_83C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_83E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_840B")

    label("loc_83E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8401")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_840B")

    label("loc_8401")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_840B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_843E")
    Jump("loc_85FE")

    label("loc_843E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_84D1")
    SetChrSubChip(0xFE, 0x0)

    #C0441
    ChrTalk(
        0xFE,
        (
            "（……待太久的话，\x01",
            "  会给周围的人带来不安，\x01",
            "  进而对公司不利呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "（等同伴们明天醒了以后，\x01",
            "  就带着大家立刻出院吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85FE")

    label("loc_84D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_85F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8587")

    #C0443
    ChrTalk(
        0xFE,
        "哎呀呀，警察也真是令人伤脑筋啊。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "就算再怎么刨根问底，\x01",
            "我也没有什么\x01",
            "可以回答的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        (
            "而且，再怎么说，我也算是住院的人，\x01",
            "就不能稍微体谅一点吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_85F0")

    label("loc_8587")


    #C0446
    ChrTalk(
        0xFE,
        (
            "一起被送来的同伴们\x01",
            "似乎还在ＩＣＵ室……\x01",
            "听说明天就会醒来。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "呵呵，不愧是著名的\x01",
            "乌尔斯拉医院呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85F0")

    Jump("loc_85FE")

    label("loc_85F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_85FE")

    label("loc_85FE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_832D end

    def Function_46_8606(): pass

    label("Function_46_8606")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8617")
    Jump("loc_899D")

    label("loc_8617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_8625")
    Jump("loc_899D")

    label("loc_8625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8633")
    Jump("loc_899D")

    label("loc_8633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8641")
    Jump("loc_899D")

    label("loc_8641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_864F")
    Jump("loc_899D")

    label("loc_864F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_865D")
    Jump("loc_899D")

    label("loc_865D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_866B")
    Jump("loc_899D")

    label("loc_866B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_86DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8686")
    Call(1, 47)
    Jump("loc_86D8")

    label("loc_8686")


    #C0448
    ChrTalk(
        0x30,
        (
            "#2406F呼……难得受欢迎一次，却这么累人啊。\x01",
            "我还想尽快查完房，\x01",
            "早点回去呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86D8")

    Jump("loc_899D")

    label("loc_86DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_88BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8808")

    #C0449
    ChrTalk(
        0x30,
        (
            "#2400F纪念庆典玩得开心吗？\x02\x03",

            "#2409F我昨天也找到了新的钓鱼点，\x01",
            "稍后正打算去看看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        "#0005F那个……您的工作呢？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x30,
        (
            "#2409F哈哈哈……\x01",
            "请不要告诉其他医生哦。\x02",
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
    SetScenarioFlags(0x1, 5)
    Jump("loc_88B5")

    label("loc_8808")


    #C0452
    ChrTalk(
        0x30,
        (
            "#2405F啊，话说在先，\x01",
            "我已经把今天该做的事情\x01",
            "全部认真完成了哦。\x02\x03",

            "#2400F这可是我自己挤出来的休息时间，\x01",
            "没理由被人教训吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#0006F（既然如此，那就堂堂正正地走嘛……）\x02",
    )

    CloseMessageWindow()

    label("loc_88B5")

    Jump("loc_899D")

    label("loc_88BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_88C8")
    Jump("loc_899D")

    label("loc_88C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_88D6")
    Jump("loc_899D")

    label("loc_88D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_88E4")
    Jump("loc_899D")

    label("loc_88E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_88F2")
    Jump("loc_899D")

    label("loc_88F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_8900")
    Jump("loc_899D")

    label("loc_8900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8994")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_891B")
    Call(1, 18)
    Jump("loc_898F")

    label("loc_891B")


    #C0454
    ChrTalk(
        0x30,
        (
            "#2403F俗话说，病由心生啊。\x01",
            "既然这么有精神，应该很快就能出院了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x136,
        (
            "#1306F……请您说点像是医生\x01",
            "该说的话吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_898F")

    Jump("loc_899D")

    label("loc_8994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_899D")

    label("loc_899D")

    TalkEnd(0xFE)
    Return()

    # Function_46_8606 end

    def Function_47_89A1(): pass

    label("Function_47_89A1")

    TurnDirection(0x30, 0x1E, 0)
    SetChrSubChip(0x1E, 0x2)
    OP_4B(0x30, 0xFF)

    #C0456
    ChrTalk(
        0x1E,
        (
            "约亚西姆医生\x01",
            "有没有女朋友呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x30,
        (
            "#2409F哈哈哈，不管怎么说，\x01",
            "我也是以单身贵族自居的。\x01",
            "女性大多都觉得我难以接近，所以不怎么受欢迎呢。\x02\x03",

            "#2400F这个暂且不提，\x01",
            "还是先来诊察吧──\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x1E,
        (
            "哎呀，是这样吗？\x01",
            "好可惜呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x1E,
        (
            "呵呵，既·然·如·此……\x01",
            "那我就来当候补吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x30,
        (
            "#2406F呃，这个～……\x01",
            "哈哈哈，伤脑筋啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0x1E, 0x0)
    OP_4C(0x30, 0xFF)
    Return()

    # Function_47_89A1 end

    def Function_48_8AF1(): pass

    label("Function_48_8AF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B6E")

    #C0461
    ChrTalk(
        0xFE,
        (
            "作为将来的参考，我正在参观\x01",
            "医生们的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "看到他们办事干脆利落的样子，\x01",
            "就知道他们有多优秀呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_8BCA")

    label("loc_8B6E")


    #C0463
    ChrTalk(
        0xFE,
        (
            "作为将来的参考，我正在参观\x01",
            "医生们的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "……待太久的话，\x01",
            "还是会妨碍到他们吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BCA")

    TalkEnd(0xFE)
    Return()

    # Function_48_8AF1 end

    def Function_49_8BCE(): pass

    label("Function_49_8BCE")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110090, 1000, -5610, 0)
    MoveCamera(68, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20480, 0)
    SetChrPos(0x101, 110500, 0, -6000, 0)
    SetChrPos(0x102, 109200, 0, -6000, 45)
    SetChrPos(0x103, 110500, 0, -7300, 0)
    SetChrPos(0x104, 109200, 0, -7300, 45)
    SetChrPos(0x109, 109200, 0, -4700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0xC, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    #C0465
    ChrTalk(
        0xC,
        (
            "#5P嗯～……那个东西，\x01",
            "不然还是退给店里算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        (
            "#12P#0005F请问……\x01",
            "您有什么麻烦吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xC,
        (
            "#5P嗯？不，\x01",
            "倒不算是\x01",
            "麻烦啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "#5P之前纪念庆典的时候，\x01",
            "我去了克洛斯贝尔市，\x01",
            "在那里买了一条丝带。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xC,
        (
            "#5P买的时候觉得\x01",
            "很可爱……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xC,
        (
            "#5P但仔细想想的话，\x01",
            "这未免可爱过头了，\x01",
            "不太适合我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#12P#0003F（丝带吗……）\x02\x03",

            "（用来包装礼物的话，\x01",
            "  似乎不错呢。）\x02\x03",

            "#0000F那个，有件事想和您商量一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        "#5P哎，什么？\x02",
    )

    CloseMessageWindow()

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德说明了正在收集\x01",
            "礼物材料的事由。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0474
    ChrTalk(
        0x101,
        (
            "#12P#0000F因此……\x01",
            "如果您愿意的话，\x01",
            "能不能将那条丝带让给我们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xC,
        "#5P哦，小滴她……\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x104,
        (
            "#12P#0304F我们绝对不会用来做\x01",
            "一些不正经的事情，请不必担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x109,
        "#6P#0506F兰、兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#12P#0200F……你说这种话，\x01",
            "反而更容易被怀疑。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xC,
        "#5P哈哈……嗯，好吧。\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        (
            "#5P既然如此，\x01",
            "就请有效地利用它吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0481
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x344),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x344, 1)

    #C0482
    ChrTalk(
        0x102,
        (
            "#12P#0100F不好意思，\x01",
            "是我们强人所难了。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xC,
        (
            "#5P不会不会，没关系啦。物尽其用最好，\x01",
            "给你们的话，也就不用白白扔掉这条丝带了。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xC,
        "#5P请继续加油收集材料吧。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#12P#0000F嗯，非常感谢。\x02",
    )

    CloseMessageWindow()
    OP_29(0x2C, 0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_912D")
    OP_29(0x2C, 0x1, 0x5)

    #C0486
    ChrTalk(
        0x101,
        (
            "#12P#0000F（适合制作礼物的材料已经集齐了，\x01",
            "  包装用的盒子和丝带也拿到了……）\x02\x03",

            "（好，差不多该拿去\x01",
            "  给小滴了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_912D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110500, 1000, -6000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xC, 0x5A, 0x0)
    SetChrPos(0x0, 110500, 0, -6000, 0)
    SetChrPos(0x1, 110500, 0, -6000, 0)
    SetChrPos(0x2, 110500, 0, -6000, 0)
    SetChrPos(0x3, 110500, 0, -6000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_49_8BCE end

    SaveToFile()

Try(main)
