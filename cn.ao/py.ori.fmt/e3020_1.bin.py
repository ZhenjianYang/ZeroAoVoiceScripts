from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3020_1.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [312, 1859, 2560, 6438, 6946, 7864, 8415, 11213, 12191, 0, 12657, 0, 13433, 14061, 14738, 17341, 0, 18113, 0, 234, 72, 0, 0],
    )

    BuildStringList((
        "e3020_1",                # 0
    ))

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_743",          # 01, 1
        "Function_2_A00",          # 02, 2
        "Function_3_1926",         # 03, 3
        "Function_4_1B22",         # 04, 4
        "Function_5_1EB8",         # 05, 5
        "Function_6_20DF",         # 06, 6
        "Function_7_2BCD",         # 07, 7
        "Function_8_2F9F",         # 08, 8
        "Function_9_3171",         # 09, 9
        "Function_10_3479",        # 0A, 10
        "Function_11_36ED",        # 0B, 11
        "Function_12_3992",        # 0C, 12
        "Function_13_43BD",        # 0D, 13
        "Function_14_46C1",        # 0E, 14
        "Function_15_48EA",        # 0F, 15
        "Function_16_5E52",        # 10, 16
        "Function_17_5FC8",        # 11, 17
        "Function_18_638B",        # 12, 18
        "Function_19_66EA",        # 13, 19
        "Function_20_7378",        # 14, 20
        "Function_21_76A5",        # 15, 21
        "Function_22_79A8",        # 16, 22
        "Function_23_862B",        # 17, 23
        "Function_24_8871",        # 18, 24
        "Function_25_8EBE",        # 19, 25
        "Function_26_919C",        # 1A, 26
        "Function_27_AB0A",        # 1B, 27
        "Function_28_AD61",        # 1C, 28
        "Function_29_AE3C",        # 1D, 29
        "Function_30_B0A9",        # 1E, 30
        "Function_31_B371",        # 1F, 31
        "Function_32_C85B",        # 20, 32
        "Function_33_CC05",        # 21, 33
        "Function_34_CE14",        # 22, 34
        "Function_35_D5FA",        # 23, 35
        "Function_36_D7F2",        # 24, 36
        "Function_37_D9CA",        # 25, 37
        "Function_38_DE32",        # 26, 38
        "Function_39_E3C1",        # 27, 39
        "Function_40_E78C",        # 28, 40
        "Function_41_E9AB",        # 29, 41
        "Function_42_ECEB",        # 2A, 42
        "Function_43_ECEF",        # 2B, 43
        "Function_44_FB15",        # 2C, 44
        "Function_45_FDFA",        # 2D, 45
        "Function_46_FDFE",        # 2E, 46
        "Function_47_10AA0",       # 2F, 47
        "Function_48_10C44",       # 30, 48
        "Function_49_10D90",       # 31, 49
        "Function_50_112A6",       # 32, 50
        "Function_51_113E1",       # 33, 51
        "Function_52_118DF",       # 34, 52
        "Function_53_1215F",       # 35, 53
        "Function_54_1299C",       # 36, 54
        "Function_55_12C97",       # 37, 55
        "Function_56_12E51",       # 38, 56
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156")
    Call(1, 1)
    Jump("loc_303")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C")

    #C0001
    ChrTalk(
        0x11,
        (
            "#00101F贝尔恐怕完全是为了自己\x01",
            "而参加此次计划的。\x02\x03",

            "#00108F她的那种性格曾给我\x01",
            "带来过不少麻烦，\x01",
            "但我一直都认为那也是她的魅力之一……\x02\x03",

            "#00103F……不过，无论有什么理由，\x01",
            "我也绝对不能原谅\x01",
            "她那种牺牲他人的做法。\x02\x03",

            "#00100F身为自幼和贝尔一起玩耍的好友……\x01",
            "我一定会将她的错误纠正。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_303")

    label("loc_27C")


    #C0002
    ChrTalk(
        0x11,
        (
            "#00103F无论有什么理由，\x01",
            "我也绝对不能原谅\x01",
            "她那种牺牲他人的做法。\x02\x03",

            "#00100F身为自幼和贝尔一起玩耍的好友……\x01",
            "我一定会将她的错误纠正。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_303")

    Jump("loc_73F")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_45D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2")

    #C0003
    ChrTalk(
        0x11,
        (
            "#00103F贝尔身为库罗伊斯家族后裔，\x01",
            "肯定与此次计划存在着\x01",
            "相当深刻的牵连。\x02\x03",

            "#00108F我们所追寻的真相，\x01",
            "一定掌握在她与伊安律师的手中……\x02\x03",

            "#00101F……我们走吧，罗伊德。\x01",
            "去把小琪雅带回来……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_458")

    label("loc_3E2")


    #C0004
    ChrTalk(
        0x11,
        (
            "#00108F我们所追寻的真相，\x01",
            "一定掌握在她与伊安律师的手中……\x02\x03",

            "#00101F……我们走吧，罗伊德。\x01",
            "去把小琪雅带回来……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458")

    Jump("loc_73F")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564")

    #C0005
    ChrTalk(
        0x11,
        (
            "#00108F贝尔……难道从一开始\x01",
            "就决定将迪塔叔叔当作弃子了吗……\x02\x03",

            "而且，没想到真正的幕后黑手\x01",
            "竟然是伊安律师……\x02\x03",

            "#00106F……不行了，\x01",
            "脑子里一片混乱……\x01",
            "已经无法冷静思考了。\x02\x03",

            "#00100F总之，我们也只能继续前进了，\x01",
            "向着那棵『碧之大树』……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5DA")

    label("loc_564")


    #C0006
    ChrTalk(
        0x11,
        (
            "#00108F……发生了太多事情，\x01",
            "我的脑子里一片混乱……\x02\x03",

            "#00100F但我们现在也只能继续前进了，\x01",
            "向着那棵『碧之大树』……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DA")

    Jump("loc_73F")

    label("loc_5DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_73F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C0")

    #C0007
    ChrTalk(
        0x11,
        (
            "#00103F外公发表的独立无效宣言\x01",
            "似乎对各地都产生了\x01",
            "很大的影响。\x02\x03",

            "#00108F再加上国防军已经暂时撤离，\x01",
            "或许会引起各种各样的混乱……\x02\x03",

            "#00100F趁着去停止『大钟』共鸣的机会，\x01",
            "我们可以再去各地\x01",
            "探查一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_73F")

    label("loc_6C0")


    #C0008
    ChrTalk(
        0x11,
        (
            "#00103F独立无效宣言的发表\x01",
            "或许会引起各种各样的混乱……\x02\x03",

            "#00100F趁着去停止『大钟』共鸣的机会，\x01",
            "我们可以再去各地\x01",
            "探查一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73F")

    TalkEnd(0xFE)
    Return()

    # Function_0_138 end

    def Function_1_743(): pass

    label("Function_1_743")


    #C0009
    ChrTalk(
        0x11,
        (
            "#00100F终于迎来了此刻……\x01",
            "通往小琪雅所在之地的道路\x01",
            "总算呈现在了我们的眼前。\x02\x03",

            "#00108F真正的幕后黑手伊安律师，\x01",
            "还有贝尔都在那里………………\x02\x03",

            "#00103F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00001F艾莉…………\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x11,
        (
            "#00103F贝尔恐怕完全是为了自己\x01",
            "而参加此次计划的。\x02\x03",

            "#00108F她的那种性格曾给我\x01",
            "带来过不少麻烦，\x01",
            "但我一直都认为那也是她的魅力之一……\x02\x03",

            "#00101F……不过，无论有什么理由，\x01",
            "我也绝对不能原谅\x01",
            "她那种随意牺牲他人的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00003F……嗯，说的对。\x02\x03",

            "#00001F无论玛丽亚贝尔小姐和伊安律师\x01",
            "有着怎样的计划，\x01",
            "也绝不允许他们利用琪雅。\x02\x03",

            "#00003F艾莉，与她展开争斗，\x01",
            "可能令你很痛苦……\x01",
            "但还是需要你的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x11,
        (
            "#00103F……嗯，我早有觉悟了。\x02\x03",

            "#00101F身为自幼和贝尔一起玩耍的好友……\x01",
            "我一定会将她的错误纠正。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 1)
    Return()

    # Function_1_743 end

    def Function_2_A00(): pass

    label("Function_2_A00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A24")
    Call(1, 56)
    Jump("loc_BC0")

    label("loc_A24")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A44")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    label("loc_A44")


    #C0014
    ChrTalk(
        0xB,
        (
            "#00200F罗伊德前辈，\x01",
            "不介意的话，\x01",
            "请收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『缇欧的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 1)
    OP_E4(0x3)

    #C0016
    ChrTalk(
        0x101,
        "#00005F是『波波碰！』的账号……？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "#00204F在这种紧张的状况下，\x01",
            "就更要注意休息娱乐。\x02\x03",

            "#00202F如果想挑战，我随时都奉陪，\x01",
            "请放松心情来比赛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，知道啦。\x02\x03",

            "#00004F（缇欧自然是相当\x01",
            "　厉害的强敌……\x01",
            "　但我一定要努力挑战试试。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC0")
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC0")

    Jump("loc_1922")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE0")
    Call(1, 5)
    Jump("loc_D19")

    label("loc_BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB1")

    #C0019
    ChrTalk(
        0xB,
        (
            "#00208F伊安律师是连盖伊先生\x01",
            "都未能战胜的对手……\x01",
            "我们无法估量他的觉悟究竟有多强。\x02\x03",

            "#00203F既然如此，\x01",
            "我们就要展现出最大限度，\x01",
            "比对方更强一筹的觉悟才行……\x02\x03",

            "#00202F……加油，罗伊德前辈。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_D19")

    label("loc_CB1")


    #C0020
    ChrTalk(
        0xB,
        (
            "#00203F我们必须要展现出\x01",
            "最大限度，比伊安律师\x01",
            "更强一筹的觉悟才行……\x02\x03",

            "#00202F……加油，罗伊德前辈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D19")

    Jump("loc_1922")

    label("loc_D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1B")

    #C0021
    ChrTalk(
        0xB,
        (
            "#00200F『碧之大树』中形成了\x01",
            "不可思议的空间。\x02\x03",

            "#00203F那远远超越了『僧院』和『塔』\x01",
            "凭借大钟的共鸣而产生的『力场』，\x01",
            "是完全无视物理法则的世界……\x02\x03",

            "#00201F在大树的空间内，\x01",
            "我们掌握的一切常识恐怕都是无用的……\x01",
            "最好慎重前进。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_EA7")

    label("loc_E1B")


    #C0022
    ChrTalk(
        0xB,
        (
            "#00203F『碧之大树』中形成了\x01",
            "完全无视物理法则\x01",
            "的奇异空间。\x02\x03",

            "#00201F在大树的空间内，\x01",
            "我们掌握的一切常识恐怕都是无用的……\x01",
            "最好慎重前进。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA7")

    Jump("loc_1922")

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F88")

    #C0023
    ChrTalk(
        0xB,
        (
            "#00200F从那棵『大树』的方位，\x01",
            "的确能感觉到与琪雅相似的波动。\x02\x03",

            "玛丽亚贝尔小姐曾说过，\x01",
            "那棵『大树』本身\x01",
            "就是琪雅……\x02\x03",

            "#00206F……真是无法理解。\x01",
            "让那样的东西显现于世，\x01",
            "她究竟有什么企图呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1012")

    label("loc_F88")


    #C0024
    ChrTalk(
        0xB,
        (
            "#00200F玛丽亚贝尔小姐曾说过，\x01",
            "那棵『大树』本身\x01",
            "就是琪雅……\x02\x03",

            "#00206F……真是无法理解。\x01",
            "让那样的东西显现于世，\x01",
            "她究竟有什么企图呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1012")

    Jump("loc_1922")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111F")

    #C0025
    ChrTalk(
        0xB,
        (
            "#00200F如今已经不需要探查\x01",
            "新的『狭间』，所以把\x01",
            "飞艇的工作全部交给约纳了。\x02\x03",

            "#00203F这次的对手可是那个『结社』 ……\x01",
            "完全无法预料对方\x01",
            "将会采取怎样的手段。\x02\x03",

            "#00200F连同魔导杖的调整在内，一定要将各种\x01",
            "准备工作做好，确保随时处于万全状态。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_11C1")

    label("loc_111F")


    #C0026
    ChrTalk(
        0xB,
        (
            "#00203F这次的对手可是那个『结社』 ……\x01",
            "完全无法预料对方\x01",
            "将会采取怎样的手段。\x02\x03",

            "#00200F连同魔导杖的调整在内，一定要将各种\x01",
            "准备工作做好，确保随时处于万全状态。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C1")

    Jump("loc_1922")

    label("loc_11C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E1")
    Call(1, 4)
    Jump("loc_130E")

    label("loc_11E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1285")

    #C0027
    ChrTalk(
        0xB,
        (
            "#00204F虽然只有很短的时间……\x01",
            "但能和蔡特并肩奔波于各处，\x01",
            "真是很开心。\x02\x03",

            "#00202F就算是为了回报它一直\x01",
            "以来的庇护，我们今后\x01",
            "也要更加努力才行呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_130E")

    label("loc_1285")


    #C0028
    ChrTalk(
        0xB,
        (
            "#00204F好了，我稍后也要去\x01",
            "帮忙做一些入侵导力网络\x01",
            "方面的最终准备。\x02\x03",

            "#00211F虽然我信任约纳的能力，\x01",
            "但也不能否认，他有些容易掉以轻心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130E")

    Jump("loc_1922")

    label("loc_1313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_147E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EF")

    #C0029
    ChrTalk(
        0xB,
        (
            "#00200F只要艾莉前辈归队，\x01",
            "我们支援科的成员\x01",
            "就全部到齐了。\x02\x03",

            "#00203F既然连麦克道尔议长\x01",
            "也被监禁在那里，\x01",
            "警备想必会相当森严……\x02\x03",

            "#00202F蔡特主动替我们\x01",
            "承担了危险的任务，\x01",
            "我们一定要取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1479")

    label("loc_13EF")


    #C0030
    ChrTalk(
        0xB,
        (
            "#00203F艾莉前辈和麦克道尔议长\x01",
            "都被监禁在那里，\x01",
            "警备想必会相当森严……\x02\x03",

            "#00200F蔡特主动替我们\x01",
            "承担了危险的任务，\x01",
            "我们一定要取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1479")

    Jump("loc_1922")

    label("loc_147E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_15D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153F")

    #C0031
    ChrTalk(
        0xB,
        (
            "#00200F从西克洛斯贝尔街道可以前往\x01",
            "贝尔加德门、警察学校……\x02\x03",

            "#00206F呼，在很麻烦的地方\x01",
            "发现了『狭间』呢。\x02\x03",

            "#00200F……不过，我们现在也只能\x01",
            "先去能去的地方看看了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_15CC")

    label("loc_153F")


    #C0032
    ChrTalk(
        0xB,
        (
            "#00206F从西克洛斯贝尔街道可以前往\x01",
            "贝尔加德门、警察学校……\x02\x03",

            "#00200F这是个很麻烦的地方呢……\x01",
            "不过，我们现在也只能\x01",
            "先去能去的地方看看了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    Jump("loc_1922")

    label("loc_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_165F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EC")
    Call(1, 3)
    Jump("loc_165A")

    label("loc_15EC")


    #C0033
    ChrTalk(
        0xB,
        (
            "#00208F蔡特手下的那些狼……\x01",
            "现在正在做些什么呢……\x02\x03",

            "#00203F如果能得到它们的帮助，\x01",
            "心里就会踏实很多了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165A")

    Jump("loc_1922")

    label("loc_165F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167A")
    Call(1, 56)
    Jump("loc_1922")

    label("loc_167A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AD")
    EndChrThread(0x8, 0x0)

    #C0034
    ChrTalk(
        0xB,
        (
            "#00203F财团与教会之间存在协力关系……\x01",
            "以前就听说过这方面的传闻，\x01",
            "如今终于有了确凿证据。\x02\x03",

            "#00202F总之，这样应该就可以\x01",
            "顺利操作终端了。\x02\x03",

            "只要与永世系统搭配使用，\x01",
            "探测『狭间』的范围也会大幅度增加。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17E1")
    Jump("loc_182B")

    label("loc_17E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1801")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_182B")

    label("loc_1801")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1821")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_182B")

    label("loc_1821")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_182B")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0035
    ChrTalk(
        0xB,
        (
            "#00200F阿巴斯先生，请您指导\x01",
            "接下来的使用方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#12100F嗯，好的。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1922")

    label("loc_18AD")


    #C0037
    ChrTalk(
        0xB,
        (
            "#00203F只要与永世系统搭配使用，\x01",
            "探测『狭间』的范围\x01",
            "应该可以大幅度增加。\x02\x03",

            "#00200F这里就交给我和\x01",
            "芙兰小姐负责吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1922")

    TalkEnd(0xFE)
    Return()

    # Function_2_A00 end

    def Function_3_1926(): pass

    label("Function_3_1926")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0038
    ChrTalk(
        0xB,
        (
            "#00205F说起来……\x01",
            "你的那些部下\x01",
            "现在栖息在山道中吧？\x02\x03",

            "#00200F它们和你一样，\x01",
            "也是『神狼』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x13,
        (
            "#01203F#3C不，它们只是普通的狼。\x02\x03",

            "#01200F不过，从乌尔斯拉还活着的时代开始，\x01",
            "它们就世世代代地伴随在我的身边，\x01",
            "可以称得上是我的眷属。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "#00203F神狼的眷属吗……\x01",
            "怪不得它们当时能在鲁巴彻事件中\x01",
            "靠气势轻松压制住那些军犬啊。\x02\x03",

            "#00208F希望它们都平安无事……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x13,
        (
            "#01203F#3C在我离开狼群之前，\x01",
            "已经仔细叮嘱过大家了，\x01",
            "所以不必担心。\x02\x03",

            "#01200F它们如今一定正在什么地方\x01",
            "观望着现在的状况吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_3_1926 end

    def Function_4_1B22(): pass

    label("Function_4_1B22")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0042
    ChrTalk(
        0xB,
        (
            "#00203F……好了，\x01",
            "已经治疗完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x13,
        "#01200F#3C嗯，谢谢你，缇欧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)

    #C0044
    ChrTalk(
        0x101,
        (
            "#00005F蔡特……\x01",
            "在之前的战斗中负伤了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x13,
        (
            "#01203F#3C嗯，被『赤色星座』的那些人击伤了。\x02\x03",

            "#01200F这点伤势很快就可以彻底痊愈……\x01",
            "不过，那些家伙的战斗力的确是\x01",
            "国防军完全无法相比的。\x02\x03",

            "这次因为是突然袭击，\x01",
            "佯攻顺利吸引到了火力，\x01",
            "但同样的方法再用第二次可就行不通了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x02\x03",

            "#00002F不过，你真是帮了大忙呢，\x01",
            "谢谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x13,
        (
            "#01203F#3C呵呵，不必客气。\x02\x03",

            "#01200F……如今，你们的战力\x01",
            "已经很充足了，应该不需要\x01",
            "我继续跟随了吧。\x02\x03",

            "我会和以前一样，留在你们的后方，\x01",
            "到了需要帮助的时候再叫我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "#00200F就是像以前一样，用魔导杖\x01",
            "发送导力波来呼唤你吧？\x01",
            "……明白了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x13,
        (
            "#01200F#3C另外，今后\x01",
            "我会以原本的形态\x01",
            "奔赴至战线。\x02\x03",

            "#01203F如果对手只是一般程度的魔兽，\x01",
            "大概一瞬间就可以轻松解决了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，要是你能以那种形态\x01",
            "赶到战场帮助我们，\x01",
            "我们可就更有底气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "#00202F那么……蔡特，\x01",
            "今后请继续关照了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1D7, 0)
    Return()

    # Function_4_1B22 end

    def Function_5_1EB8(): pass

    label("Function_5_1EB8")


    #C0052
    ChrTalk(
        0xB,
        (
            "#00203F……听说伊安律师亲手杀害了\x01",
            "原本关系亲近的盖伊先生之后……\x01",
            "我稍微有些不安的感觉。\x02\x03",

            "#00208F他宁愿做出这样的事情也坚持要\x01",
            "达成的『碧零计划』，究竟会是……\x02\x03",

            "#00206F更重要的是，\x01",
            "连盖伊先生都未能战胜的对手，\x01",
            "我们又能否应付……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F……是啊，\x01",
            "的确有些让人不安。\x02\x03",

            "#00008F伊安律师的觉悟之强，\x01",
            "恐怕更在亚里欧斯先生之上吧。\x02\x03",

            "#00001F但是……正因如此，\x01",
            "我们才更要展现出超越\x01",
            "伊安律师的最强觉悟才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "#00208F超越伊安律师的觉悟……\x01",
            "……说的对。\x02\x03",

            "#00201F加油，罗伊德前辈。\x01",
            "我想，现在正是我们超越\x01",
            "盖伊先生的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000F嗯……那当然！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 2)
    Return()

    # Function_5_1EB8 end

    def Function_6_20DF(): pass

    label("Function_6_20DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_2298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20FD")
    Call(1, 11)
    Jump("loc_2293")

    label("loc_20FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2216")

    #C0056
    ChrTalk(
        0xE,
        (
            "#00300F最后的对手是\x01",
            "深不可测的玛丽亚贝尔大小姐\x01",
            "和整个事件的幕后黑手伊安律师。\x02\x03",

            "#00303F既然他们利用了身为\x01",
            "『零之至宝』的阿琪，\x01",
            "自然会是相当危险的对手。\x02\x03",

            "#00302F但是，我们也绝对不会\x01",
            "退让半步的。\x02\x03",

            "#00309F我们的可爱女儿\x01",
            "还在等着爸爸和妈妈呢，\x01",
            "赶快去接她回家吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2293")

    label("loc_2216")


    #C0057
    ChrTalk(
        0xE,
        (
            "#00302F不管对手是什么样的家伙，\x01",
            "我们也绝不会退让半步。\x02\x03",

            "#00309F我们的可爱女儿\x01",
            "还在等着爸爸和妈妈呢，\x01",
            "赶快去接她回家吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2293")

    Jump("loc_2BC9")

    label("loc_2298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_2343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B3")
    Call(1, 10)
    Jump("loc_233E")

    label("loc_22B3")


    #C0058
    ChrTalk(
        0xE,
        (
            "#00303F从今以后，我一定会继续\x01",
            "证明自己所选择的道路没有错。\x02\x03",

            "#00302F叔叔和已故的父亲好歹\x01",
            "也算照顾过我，\x01",
            "这也是我所能尽到的最大情分了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233E")

    Jump("loc_2BC9")

    label("loc_2343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_23C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_235E")
    Call(1, 9)
    Jump("loc_23BF")

    label("loc_235E")


    #C0059
    ChrTalk(
        0xE,
        (
            "#00303F接下来，\x01",
            "我必须要和那个怪物一样的\x01",
            "叔叔做个了结。\x02\x03",

            "#00301F一定要趁现在\x01",
            "做好各种准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23BF")

    Jump("loc_2BC9")

    label("loc_23C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_252B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AD")

    #C0060
    ChrTalk(
        0xE,
        (
            "#00301F虽然『赤色星座』的飞艇没有追击，\x01",
            "但对他们来说，\x01",
            "刚才那只是试探性的攻击而已。\x02\x03",

            "#00303F叔叔和谢莉必定在\x01",
            "前方摩拳擦掌地等着我们……\x02\x03",

            "#00301F还不知道他们\x01",
            "准备了怎样的陷阱，\x01",
            "我们绝对不能有丝毫大意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2526")

    label("loc_24AD")


    #C0061
    ChrTalk(
        0xE,
        (
            "#00303F叔叔和谢莉必定在\x01",
            "前方摩拳擦掌地等着我们……\x02\x03",

            "#00301F还不知道他们\x01",
            "准备了怎样的陷阱，\x01",
            "我们绝对不能有丝毫大意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2526")

    Jump("loc_2BC9")

    label("loc_252B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260F")

    #C0062
    ChrTalk(
        0xE,
        (
            "#00300F那棵『大树』的来历\x01",
            "对我们来说只是无关紧要的小事。\x01",
            "……没错吧？罗伊德。\x02\x03",

            "#00304F我们的目标只是让阿琪回到身边，\x01",
            "只要别忘记这一点，就万事ＯＫ。\x02\x03",

            "#00300F与其浪费时间慢慢思考，\x01",
            "倒不如马上突击。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2663")

    label("loc_260F")


    #C0063
    ChrTalk(
        0xE,
        (
            "#00304F我的斧枪和『狂战士』\x01",
            "都已经准备完毕了。\x02\x03",

            "#00300F赶快去把阿琪\x01",
            "接回来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2663")

    Jump("loc_2BC9")

    label("loc_2668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277D")

    #C0064
    ChrTalk(
        0xE,
        (
            "#00303F如果单看整体战斗力，\x01",
            "大概还是『赤色星座』更胜一筹……\x02\x03",

            "#00301F但『结社』拥有先进的智能兵器，\x01",
            "而且还有那位强得夸张的枪技达人存在。\x02\x03",

            "如果正面硬拼，\x01",
            "我们恐怕无法轻松取胜。\x02\x03",

            "#00303F……总之，\x01",
            "绝对不能小看那些家伙。\x01",
            "你也要牢记这一点，罗伊德。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2803")

    label("loc_277D")


    #C0065
    ChrTalk(
        0xE,
        (
            "#00303F如果正面硬拼，\x01",
            "我们恐怕无法轻松战胜\x01",
            "『结社』的那些家伙。\x02\x03",

            "#00301F……总之，\x01",
            "绝对不能小看他们。\x01",
            "你也要牢记这一点，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2803")

    Jump("loc_2BC9")

    label("loc_2808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_29BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290F")

    #C0066
    ChrTalk(
        0xE,
        (
            "#00300F『独立无效宣言』发表之后，\x01",
            "国防军应该会\x01",
            "暂时采取观望态度……\x02\x03",

            "#00303F但总统私下雇佣的\x01",
            "『赤色星座』应该还会像\x01",
            "以往一样，继续对我们发动袭击。\x02\x03",

            "#00308F不……\x01",
            "他们说不定会比之前\x01",
            "更加不择手段。\x02\x03",

            "#00300F总之，绝对不能放松警惕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_29B5")

    label("loc_290F")


    #C0067
    ChrTalk(
        0xE,
        (
            "#00303F就算发表了无效宣言，\x01",
            "『赤色星座』的家伙们应该也会像\x01",
            "以往一样，继续对我们发动袭击。\x02\x03",

            "#00301F而且他们有可能会比\x01",
            "之前更加不择手段，\x01",
            "我们今后也不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B5")

    Jump("loc_2BC9")

    label("loc_29BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_2A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D5")
    Call(1, 8)
    Jump("loc_2A60")

    label("loc_29D5")


    #C0068
    ChrTalk(
        0xE,
        (
            "#00300F叔叔和谢莉似乎并不在\x01",
            "驻守于米修拉姆的部队中……\x02\x03",

            "#00303F应该是加雷斯之类的\x01",
            "干部级成员在负责指挥。\x01",
            "……我们一定要做好万全准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A60")

    Jump("loc_2BC9")

    label("loc_2A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_2BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A80")
    Call(1, 7)
    Jump("loc_2BC9")

    label("loc_2A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4D")

    #C0069
    ChrTalk(
        0xE,
        (
            "#00304F米蕾优那边还有\x01",
            "玛因兹的人提供协助，\x01",
            "暂时应该不用担心。\x02\x03",

            "#00300F虽然我们也有很多事要做，\x01",
            "但首先还是专心处理眼前的事情吧。\x02\x03",

            "#00309F以后就看我的吧，\x01",
            "大哥我一定会好好大闹一番的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2BC9")

    label("loc_2B4D")


    #C0070
    ChrTalk(
        0xE,
        (
            "#00303F虽然我们也有很多事要做，\x01",
            "但首先还是专心处理眼前的事情吧。\x02\x03",

            "#00300F以后就看我的吧，\x01",
            "大哥我一定会好好大闹一番的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC9")

    TalkEnd(0xFE)
    Return()

    # Function_6_20DF end

    def Function_7_2BCD(): pass

    label("Function_7_2BCD")


    #C0071
    ChrTalk(
        0xE,
        (
            "#00309F没想到这里连工房都有啊……\x01",
            "哎呀呀～梅尔卡瓦里的设施\x01",
            "真是应有尽有。\x02\x03",

            "#00300F看样子，\x01",
            "今后也可以定期\x01",
            "维护『狂战士』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00000F说起来，那把武器之前\x01",
            "好像是请基约姆师傅给修好了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        (
            "#00304F嗯，听从了他那时候的建议，\x01",
            "只有在真正需要的时候才会使用它。\x02\x03",

            "#00300F而且我也不想把\x01",
            "道格拉斯老兄用心教给我的\x01",
            "斧枪技术给荒废掉……\x02\x03",

            "#00300F今后就脚踩两条船，\x01",
            "让狂战士和斧枪轮番上阵好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，虽然说得有些……\x01",
            "但这才像是兰迪的风格啊。\x02\x03",

            "#00003F说起来……\x01",
            "道格拉斯副司令如今正在做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xE,
        (
            "#00303F那位老兄啊，\x01",
            "大概还是和平常一样，\x01",
            "一丝不苟地完成副司令的所有工作吧……\x02\x03",

            "#00301F司令也好，副司令也好，\x01",
            "不知道他们是否真的能接受如今这种状况。\x02\x03",

            "#00303F不过，就算无法接受，\x01",
            "大概也不可能像米蕾优那样\x01",
            "带头扬起反旗吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00001F是啊……\x01",
            "要是能想办法了解到\x01",
            "司令他们的真实想法就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xE,
        (
            "#00304F好啦，虽然我们有很多事要做，\x01",
            "但首先还是专心处理眼前的事情吧。\x02\x03",

            "#00300F以后就看我的吧，\x01",
            "大哥我一定会好好大闹一番的。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……明白啦。\x01",
            "今后就靠你了，兰迪。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 1)
    Return()

    # Function_7_2BCD end

    def Function_8_2F9F(): pass

    label("Function_8_2F9F")


    #C0079
    ChrTalk(
        0xD,
        (
            "#10703F驻守在米修拉姆\x01",
            "的『赤色星座』部队……\x02\x03",

            "#10708F……『血腥谢莉』大概\x01",
            "也在其中吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xE,
        (
            "#00303F……不，以她的性格来说，\x01",
            "应该没兴趣在监禁\x01",
            "重要人物的场所负责警戒。\x02\x03",

            "#00300F就算有干部级的成员在驻守，\x01",
            "恐怕也是其他人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xD,
        "#10703F……是吗。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xE,
        (
            "#00303F莉夏……\x01",
            "我们现在还是集中精神，\x01",
            "救出大小姐他们吧。\x02\x03",

            "#00300F就算不想，\x01",
            "以后也难免会与\x01",
            "叔叔和谢莉展开正面对决。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xD,
        (
            "#10708F……嗯，说的对。\x01",
            "抱歉，兰迪先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xE,
        "#00309F哈哈，用不着道歉啦。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_8_2F9F end

    def Function_9_3171(): pass

    label("Function_9_3171")


    #C0085
    ChrTalk(
        0xE,
        (
            "#00303F谢莉从刚刚懂事的时候开始，\x01",
            "就将战斗视为唯一的乐趣，\x01",
            "可以称得上是一头真正意义上的食人猛虎。\x02\x03",

            "只有不是你死就是我活的血腥战场\x01",
            "才能让她感到满足……\x02\x03",

            "#00302F那样的家伙，却在莉夏小姐的身上\x01",
            "尝到了『被杀』之外的败北方式……\x01",
            "她想必会感到无地自容吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x01",
            "直到失去意识之前，\x01",
            "她都是一副未能满足的表情。\x02\x03",

            "#00002F不过，如此收场，\x01",
            "你应该也松了口气吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xE,
        (
            "#00302F……哈哈，算是吧。\x01",
            "虽说她是那样的家伙，但终究也是我的堂妹。\x02\x03",

            "#00303F老实说，她毕竟做过那么多过分的事情，\x01",
            "就算血债血偿也没有什么不对……\x02\x03",

            "#00300F但莉夏小姐却没有那样做，\x01",
            "真得好好感谢她才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00002F哈哈……是吗……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xE,
        (
            "#00303F……接下来，\x01",
            "我必须要和那个怪物一样的\x01",
            "叔叔做个了结。\x02\x03",

            "#00300F到时就请大家助我一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00000F嗯，当然没问题。\x01",
            "只要大家齐心协力，\x01",
            "就一定能跨越任何障碍。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 2)
    Return()

    # Function_9_3171 end

    def Function_10_3479(): pass

    label("Function_10_3479")


    #C0091
    ChrTalk(
        0xE,
        "#00303F呼……………………\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00001F兰迪的叔叔……\x01",
            "果然强得\x01",
            "让人难以相信呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xE,
        (
            "#00302F嗯……\x01",
            "多亏有你们的帮忙，\x01",
            "总算是战胜了他啊。\x02\x03",

            "#00306F老实说，如果再战一次的话，\x01",
            "恐怕就未必可以再次取胜了。\x02\x03",

            "#00300F最强的猎兵『赤色战鬼』……\x01",
            "果然不是浪得虚名。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00004F……只要我们齐心协力，\x01",
            "无论多少次也都能取胜的。\x02\x03",

            "#00000F因为我们全都伴随在兰迪的身边。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xE,
        (
            "#00304F……哈哈，说的没错。\x01",
            "这才是我所拥有的最强力量。\x02\x03",

            "#00300F从今以后，我一定会继续\x01",
            "证明自己所选择的道路没有错。\x02\x03",

            "#00303F叔叔和已故的父亲好歹\x01",
            "也算照顾过我，\x01",
            "这也是我所能尽到的最大情分了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00002F嗯……我们也一定会\x01",
            "全力协助你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xE,
        "#00309F哈哈，谢谢啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 3)
    Return()

    # Function_10_3479 end

    def Function_11_36ED(): pass

    label("Function_11_36ED")


    #C0098
    ChrTalk(
        0xE,
        (
            "#00301F最后的对手是\x01",
            "深不可测的玛丽亚贝尔大小姐\x01",
            "和整个事件的幕后黑手伊安律师。\x02\x03",

            "#00303F单以战斗力而言，\x01",
            "也许还是叔叔和亚里欧斯大叔\x01",
            "更具威胁性……\x02\x03",

            "#00301F但他们毕竟利用了身为\x01",
            "『零之至宝』的阿琪，\x01",
            "自然也会是相当危险的对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00008F嗯……接下来的挑战，\x01",
            "也许会比与亚里欧斯先生的战斗更加严酷。\x02\x03",

            "#00001F但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        (
            "#00304F一切真相都在前方等着我们，\x01",
            "我们绝对没有退却的理由——对吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        "#00006F竟、竟然被你抢先说出来了。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        (
            "#00309F哈哈，毕竟相处了这么久，\x01",
            "已经基本能猜到\x01",
            "你会说些什么了。\x02\x03",

            "#00304F当然，我们是绝对不会\x01",
            "退让半步的。\x02\x03",

            "#00302F因为我们的可爱女儿\x01",
            "还在等着爸爸和妈妈来接她呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00000F嗯……是啊。\x01",
            "大家一起去把琪雅接回来吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 4)
    Return()

    # Function_11_36ED end

    def Function_12_3992(): pass

    label("Function_12_3992")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39B0")
    Call(1, 14)
    Jump("loc_3B2C")

    label("loc_39B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA1")

    #C0104
    ChrTalk(
        0x10,
        (
            "#10100F既然已经走到了这一步，\x01",
            "接下来，唯一能做的就是相信自己，\x01",
            "勇敢前进了。\x02\x03",

            "#10104F为了今后继续守护克洛斯贝尔……\x01",
            "我们一起加油吧，罗伊德警官。\x02\x03",

            "#10102F不仅是作为警察或警备队员，\x01",
            "更是以共同生活在此地的同伴的身份……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3B2C")

    label("loc_3AA1")


    #C0105
    ChrTalk(
        0x10,
        (
            "#10100F为了今后继续守护克洛斯贝尔……\x01",
            "我们一起加油吧，罗伊德警官。\x02\x03",

            "不仅是作为警察或警备队员，\x01",
            "更是以共同生活在此地的同伴的身份……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2C")

    Jump("loc_43B9")

    label("loc_3B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_3C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C00")

    #C0106
    ChrTalk(
        0x10,
        (
            "#10106F强袭战舰的出现\x01",
            "真是让我吃了一惊……\x02\x03",

            "#10100F但总算平安抵达『大树』，\x01",
            "真是太好了。\x02\x03",

            "#10103F但那战舰说不定\x01",
            "还会再次出现。\x02\x03",

            "#10101F留在原地待命的成员\x01",
            "一定要多加注意才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3C5A")

    label("loc_3C00")


    #C0107
    ChrTalk(
        0x10,
        (
            "#10103F强袭战舰说不定\x01",
            "还会再次出现。\x02\x03",

            "#10101F留在原地待命的成员\x01",
            "一定要多加注意才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5A")

    Jump("loc_43B9")

    label("loc_3C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D86")

    #C0108
    ChrTalk(
        0x10,
        (
            "#10103F亚里欧斯先生失踪后，\x01",
            "整个国防军的指挥权\x01",
            "已经转交给了索妮亚司令。\x02\x03",

            "#10100F由于『大树』的出现，\x01",
            "在短时间之内可能需要\x01",
            "全力平息各地的混乱事态。\x02\x03",

            "#10104F虽然相当棘手……\x01",
            "但我认为只要交给\x01",
            "索妮亚司令就一定没问题。\x02\x03",

            "#10100F我们还是\x01",
            "专注于眼前的目标，\x01",
            "继续前进吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3DFC")

    label("loc_3D86")


    #C0109
    ChrTalk(
        0x10,
        (
            "#10104F国防军那边的事情\x01",
            "有索妮亚司令在处理，\x01",
            "我想一定没问题的。\x02\x03",

            "#10100F我们还是\x01",
            "专注于眼前的目标，\x01",
            "继续前进吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DFC")

    Jump("loc_43B9")

    label("loc_3E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3F87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EED")

    #C0110
    ChrTalk(
        0x10,
        (
            "#10101F『月之僧院』和『星见之塔』\x01",
            "原本都是由警备队管理的遗迹。\x02\x03",

            "#10106F如果早点将钟的来历查明，\x01",
            "事态也许就不会\x01",
            "发展到现在这种地步了。\x02\x03",

            "#10103F……事到如今，后悔也无济于事了。\x01",
            "总之，我们现在还是要向前看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3F82")

    label("loc_3EED")


    #C0111
    ChrTalk(
        0x10,
        (
            "#10108F如果能在事前将钟的来历查明，\x01",
            "事态也许就不会\x01",
            "发展到现在这种地步了。\x02\x03",

            "#10103F……事到如今，后悔也无济于事了。\x01",
            "总之，我们现在还是要向前看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F82")

    Jump("loc_43B9")

    label("loc_3F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_415E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A4")

    #C0112
    ChrTalk(
        0x10,
        (
            "#10103F独立国的正当性遭到质疑……\x02\x03",

            "#10101F也就意味着国防军这个组织\x01",
            "的正当性存有疑问。\x02\x03",

            "#10108F虽然我相信索妮亚司令\x01",
            "一定可以妥善处理，\x01",
            "但恐怕还是无法避免相当程度的混乱吧。\x02\x03",

            "#10103F……两大国由于内战和经济危机而无法行动，\x01",
            "从某种意义上说，也算是救了我们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4159")

    label("loc_40A4")


    #C0113
    ChrTalk(
        0x10,
        (
            "#10101F无效宣言一旦正式发表，\x01",
            "贝尔加德门和唐古拉姆门\x01",
            "两边的部队恐怕都会陷入相当程度的混乱……\x02\x03",

            "#10103F……两大国由于内战和经济危机而无法行动，\x01",
            "从某种意义上说，也算是救了我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4159")

    Jump("loc_43B9")

    label("loc_415E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_43B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4179")
    Call(1, 13)
    Jump("loc_43B9")

    label("loc_4179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4338")

    #C0114
    ChrTalk(
        0x10,
        (
            "#10105F啊，罗、罗伊德警官……\x02\x03",

            "#10111F那个……\x01",
            "听你说出『你就是我的人了』的时候，\x01",
            "我的确是吃了一惊……\x02\x03",

            "#10106F但、但我完全明白\x01",
            "你当时说这句话\x01",
            "并不是那种意思啦！！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00005F那个……\x01",
            "『那种意思』到底是哪种意思呢……\x01",
            "我不是太明白……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x10,
        (
            "#10106F（他、他真的不是在开玩笑吗……）\x02\x03",

            "#10100F……咳咳，总之，\x01",
            "如今的首要目标还是\x01",
            "在米修拉姆的作战中取得成功！\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00000F嗯，那当然。\x01",
            "拜托你啦，诺艾尔。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_43B9")

    label("loc_4338")


    #C0118
    ChrTalk(
        0x10,
        (
            "#10100F……咳咳，总之，\x01",
            "如今的首要目标还是\x01",
            "在米修拉姆的作战中取得成功！\x02\x03",

            "为了艾莉小姐\x01",
            "和麦克道尔议长，\x01",
            "我一定会拿出全力的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B9")

    TalkEnd(0xFE)
    Return()

    # Function_12_3992 end

    def Function_13_43BD(): pass

    label("Function_13_43BD")

    OP_4B(0x10, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0119
    ChrTalk(
        0xC,
        (
            "#01912F呼……\x01",
            "能和姐姐重逢，\x01",
            "真是太好了～\x02\x03",

            "#01911F呜呜，\x01",
            "不小心又哭出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#10112F芙兰，你真是的……\x02\x03",

            "#10104F……呵呵，我听说\x01",
            "你的伤势已经痊愈时，\x01",
            "也真是松了一口气呢。\x02\x03",

            "#10109F而且，你好像一直在\x01",
            "努力协助罗伊德警官和瓦吉。\x01",
            "呵呵，真是很了不起哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xC,
        (
            "#01906F姐、姐姐你可真是的，\x01",
            "不要总是把我当作小孩子嘛～！\x02\x03",

            "#01905F……啊，对了。\x01",
            "听说姐姐现在已经是\x01",
            "罗伊德警官的人了～？\x02\x03",

            "#01906F嗯，毕竟都已经突破了那个阶段，\x01",
            "成为真正意义上的大人了，\x01",
            "把我当作小孩子倒也情有可原……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    #C0122
    ChrTalk(
        0x10,
        (
            "#10111F笨、笨蛋……！\x01",
            "你在说什么蠢话啊！芙兰！\x02\x03",

            "#10106F罗伊德警官的那句话\x01",
            "并不是那种意思……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "#01909F哇哇，姐姐想起当时\x01",
            "的事情，害羞起来了～\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00004F（……虽然听不懂她们在说些什么……\x01",
            "  但看如今的气氛，似乎不宜加入对话呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 5)
    OP_4C(0x10, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_13_43BD end

    def Function_14_46C1(): pass

    label("Function_14_46C1")


    #C0125
    ChrTalk(
        0x10,
        (
            "#10101F终于迎来最后的挑战了……\x02\x03",

            "#10103F既然已经走到了这一步，\x01",
            "接下来，唯一能做的就是相信自己，\x01",
            "勇敢前进了。\x02\x03",

            "#10108F就算此次事件能顺利平息，\x01",
            "克洛斯贝尔今后恐怕也\x01",
            "仍要继续承受无数苦难……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#00004F嗯……但我们现在也\x01",
            "只能把眼前的问题\x01",
            "一个一个地解决。\x02\x03",

            "#00000F我想……解决这次事件，\x01",
            "或许正是为了今后能继续守护\x01",
            "克洛斯贝尔而迈出的第一步。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10,
        (
            "#10109F呵呵，如果我爸爸还活着，\x01",
            "一定也会说出同样的话呢。\x02\x03",

            "#10103F为了今后能继续守护克洛斯贝尔……\x01",
            "我们一起加油吧，罗伊德警官。\x02\x03",

            "#10102F不仅是作为警察或警备队员，\x01",
            "更是以共同生长在此地的同伴的身份……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 6)
    Return()

    # Function_14_46C1 end

    def Function_15_48EA(): pass

    label("Function_15_48EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4908")
    Call(1, 18)
    Jump("loc_4A88")

    label("loc_4908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F6")

    #C0128
    ChrTalk(
        0xA,
        (
            "#10404F虽然相处的时间并不算久，\x01",
            "但你们与琪雅之间的『羁绊』是毋庸置疑的。\x02\x03",

            "#10402F无论发生了什么，\x01",
            "只要你们坚持追寻自己的目标，\x01",
            "希望就永远不会消失。\x02\x03",

            "#10409F呵呵，既然如此，\x01",
            "我就奉陪到底好了。\x01",
            "这也是为了可爱的琪雅。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4A88")

    label("loc_49F6")


    #C0129
    ChrTalk(
        0xA,
        (
            "#10404F无论发生了什么，\x01",
            "只要你们坚持追寻自己的目标，\x01",
            "希望就永远不会消失。\x02\x03",

            "#10409F呵呵，既然如此，\x01",
            "我就奉陪到底好了。\x01",
            "这也是为了可爱的琪雅。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A88")

    Jump("loc_5E4E")

    label("loc_4A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_4B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA8")
    Call(1, 17)
    Jump("loc_4B3E")

    label("loc_4AA8")


    #C0130
    ChrTalk(
        0xA,
        (
            "#10404F终于以我自己的身份\x01",
            "与他做了彻底的了断……\x01",
            "请容我向大家表示谢意。\x02\x03",

            "#10402F现在开始，我将以\x01",
            "星杯骑士与特别任务支援科成员\x01",
            "的身份来协助大家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3E")

    Jump("loc_5E4E")

    label("loc_4B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_END)), "loc_4C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B63")
    Call(1, 55)
    Jump("loc_4C56")

    label("loc_4B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BE2")

    #C0131
    ChrTalk(
        0xA,
        (
            "#10403F看起来，『他』似乎\x01",
            "很希望与我做个彻底的了断。\x02\x03",

            "#10400F如果已经准备完毕，\x01",
            "就尽快前往壁障处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C56")

    label("loc_4BE2")


    #C0132
    ChrTalk(
        0xA,
        (
            "#10403F看起来，『他』似乎\x01",
            "很希望与我做个彻底的了断。\x02\x03",

            "#10400F让我加入探索队伍吧，\x01",
            "我们一起前往壁障所在的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C56")

    Jump("loc_5E4E")

    label("loc_4C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_4D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D26")

    #C0133
    ChrTalk(
        0xA,
        (
            "#10404F嗯，终于要开始探索了啊。\x02\x03",

            "#10401F无法继续乘坐梅尔卡瓦前进，实在遗憾……\x01",
            "『他』应该也在前方等着我们。\x02\x03",

            "#10403F就算是为了完成\x01",
            "之前始终未能完成的了断，\x01",
            "也要谨慎前进。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4D91")

    label("loc_4D26")


    #C0134
    ChrTalk(
        0xA,
        (
            "#10401F『他』应该也在前方\x01",
            "等待着我们。\x02\x03",

            "#10403F就算是为了完成\x01",
            "之前始终未能完成的了断，\x01",
            "也要谨慎前进。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D91")

    Jump("loc_5E4E")

    label("loc_4D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F0E")

    #C0135
    ChrTalk(
        0xA,
        (
            "#10403F那棵『大树』的出现，\x01",
            "在亚尔特利亚法典国\x01",
            "似乎也引起了很大的骚动。\x02\x03",

            "#10400F毕竟那是教会的\x01",
            "任何圣典中都没有记载的\x01",
            "『预料外的奇迹』。\x02\x03",

            "#10408F再加上之前发生过『盐之桩』事件，\x01",
            "高层也不得不\x01",
            "慎重对待吧……\x02\x03",

            "#10400F不过，既然琪雅在那里，\x01",
            "我们便不能再慢慢等下去了。\x02\x03",

            "一切责任都由我来承担，\x01",
            "如果想前往『大树』，不必多虑，\x01",
            "对阿巴斯做出指示就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4FB2")

    label("loc_4F0E")


    #C0136
    ChrTalk(
        0xA,
        (
            "#10404F既然琪雅在那里，\x01",
            "我们便没时间慢慢等待\x01",
            "亚尔特利亚法典国的指示了。\x02\x03",

            "#10400F一切责任都由我来承担，\x01",
            "如果想前往『大树』，不必多虑，\x01",
            "对阿巴斯做出指示就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB2")

    Jump("loc_5E4E")

    label("loc_4FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_51D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511C")

    #C0137
    ChrTalk(
        0xA,
        (
            "#10400F『结社』和我们骑士团在历史中\x01",
            "曾经有过多次不为人知的对立，\x01",
            "可以称得上是宿命的对手呢。\x02\x03",

            "#10403F虽然骑士团也曾调查过他们，\x01",
            "但有关『小丑』和『钢之圣女』\x01",
            "的情报实在是少之又少。\x02\x03",

            "在没有掌握有效对抗手段的情况下，\x01",
            "我们就要面临与他们的战斗了……\x02\x03",

            "#10402F但正所谓『不入虎穴焉得虎子』，\x01",
            "只要拿出全力挑战，\x01",
            "总有机会寻找到胜机的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_51D2")

    label("loc_511C")


    #C0138
    ChrTalk(
        0xA,
        (
            "#10403F虽然骑士团也曾对『结社』展开过调查，\x01",
            "但有关『小丑』和『钢之圣女』\x01",
            "的情报实在是少之又少。\x02\x03",

            "#10402F但正所谓『不入虎穴焉得虎子』，\x01",
            "只要拿出全力挑战，\x01",
            "总有机会寻找到胜机的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D2")

    Jump("loc_5E4E")

    label("loc_51D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_537E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5304")

    #C0139
    ChrTalk(
        0xA,
        (
            "#10402F无线信号增幅器地点的周边地区\x01",
            "似乎并没有特别警备。\x02\x03",

            "#10404F那里处于国防军和猎兵们的警备范围之外，\x01",
            "就这样直接驾驶梅尔卡瓦前往，\x01",
            "应该也不会遭到阻碍的。\x02\x03",

            "#10408F这次的『独立无效宣言』究竟会将\x01",
            "今后的命运引向何种结果呢……\x02\x03",

            "#10409F呵呵，以后的事情就只有女神才知道了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5379")

    label("loc_5304")


    #C0140
    ChrTalk(
        0xA,
        (
            "#10404F这次的『独立无效宣言』究竟会将\x01",
            "今后的命运引向何种结果呢……\x02\x03",

            "#10409F呵呵，以后的事情就只有女神才知道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5379")

    Jump("loc_5E4E")

    label("loc_537E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_5584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54EA")

    #C0141
    ChrTalk(
        0xA,
        (
            "#10402F米修拉姆的湖水浴场吗……\x01",
            "没想到会以这样的形式去那里。\x02\x03",

            "#10406F下次再去的时候，\x01",
            "但愿是大家一起去度假啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#00004F等我们把琪雅带回……\x01",
            "并将一切事情都解决之后，\x01",
            "一定要一起去玩。\x02\x03",

            "#00000F下次要把科长、阿巴斯，\x01",
            "还有索妮亚司令他们\x01",
            "也都叫上。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#10409F啊哈哈，那可太好了！\x02\x03",

            "#10400F为了迎接那一天的到来，\x01",
            "我们也要拼命努力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_557F")

    label("loc_54EA")


    #C0144
    ChrTalk(
        0xA,
        (
            "#10404F米修拉姆的湖水浴场……\x01",
            "这次等待着我们的可不是美好的度假，\x01",
            "而是严酷的战斗呢。\x02\x03",

            "#10400F就算是为了恢复安稳和平的生活，\x01",
            "我们也要拼命努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_557F")

    Jump("loc_5E4E")

    label("loc_5584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_58BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E4")

    #C0145
    ChrTalk(
        0xA,
        (
            "#10404F哎呀呀，只要和格蕾丝小姐扯上关系，\x01",
            "无论如何也躲不过采访啊。\x02\x03",

            "过于重要的情报我不能透露，\x01",
            "不然阿巴斯会发怒的……\x02\x03",

            "#10409F但她要是继续这样紧紧相逼，\x01",
            "我恐怕也只好随便说一些真真假假的消息了。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0xA, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_56EF")
    Jump("loc_5739")

    label("loc_56EF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_570F")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5739")

    label("loc_570F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_572F")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5739")

    label("loc_572F")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5739")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0146
    ChrTalk(
        0xF,
        (
            "#02109F啊，这可不行哦，瓦吉～\x01",
            "我只要听『真消息』！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x101,
        "#00006F（阿巴斯也真是辛苦呢……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_58B7")

    label("loc_57E4")


    #C0148
    ChrTalk(
        0xA,
        (
            "#10404F圣书会这个组织的名字，\x01",
            "就是从我绰号中的『圣典』这个词\x01",
            "适当变换而来的。\x02\x03",

            "#10409F老实说，其实取什么名字我都无所谓，\x01",
            "但阿巴斯实在太麻烦了，\x01",
            "因为他是那种比较形式主义的类型呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_58B7")

    Jump("loc_5E4E")

    label("loc_58BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_5B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E8")

    #C0149
    ChrTalk(
        0xA,
        (
            "#10403F莉夏站在甲板上，\x01",
            "似乎正在想什么心事呢。\x02\x03",

            "彩虹剧团、黑月，\x01",
            "还有『银』的使命……\x01",
            "让她烦恼的事情大概有不少吧。\x02\x03",

            "#10402F呵呵，如果愿意，\x01",
            "你就去和她聊聊如何？\x02\x03",

            "#10409F说不定还能趁机使\x01",
            "彼此之间的关系更进一步呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00003F我、我才不会带着那种企图\x01",
            "去找她呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_59E8")


    #C0151
    ChrTalk(
        0xA,
        (
            "#10403F莉夏站在甲板上，\x01",
            "似乎正在想什么心事呢。\x02\x03",

            "彩虹剧团、黑月，\x01",
            "还有『银』的使命……\x01",
            "让她烦恼的事情大概有不少吧。\x02\x03",

            "#10402F呵呵……\x01",
            "看样子，你已经去和她谈过了啊，\x01",
            "彼此之间的关系有没有更进一步呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#00006F我、我才不是为了\x01",
            "那种目的而去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ADF")

    SetScenarioFlags(0x0, 7)
    Jump("loc_5B6C")

    label("loc_5AE7")


    #C0153
    ChrTalk(
        0xA,
        (
            "#10404F话说回来，如果莉夏\x01",
            "换掉现在这身装扮，\x01",
            "怎么看都不像是『银』呢。\x02\x03",

            "#10400F呵呵，那种单纯的性格，\x01",
            "可以算是天然的隐匿手段吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B6C")

    Jump("loc_5E4E")

    label("loc_5B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5CC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C51")

    #C0154
    ChrTalk(
        0xA,
        (
            "#10400F多亏缇欧和芙兰的加入，\x01",
            "舰艇的运用效率似乎大幅度提高了。\x02\x03",

            "#10404F如果光靠我们来寻找『狭间』，\x01",
            "毕竟是有极限的。\x01",
            "如今可以说是迈出了很大的一步。\x02\x03",

            "#10400F呵呵，说不定，\x01",
            "这也是女神的安排呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CBD")

    label("loc_5C51")


    #C0155
    ChrTalk(
        0xA,
        (
            "#10404F在最初的目的地乌尔斯拉医院\x01",
            "就能与缇欧和芙兰会合……\x02\x03",

            "#10400F呵呵，说不定，\x01",
            "这也是女神的安排呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CBD")

    Jump("loc_5E4E")

    label("loc_5CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CDD")
    Call(1, 16)
    Jump("loc_5E4E")

    label("loc_5CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DDC")

    #C0156
    ChrTalk(
        0xA,
        (
            "#10406F虽然前方还有重重困难……\x01",
            "但现在也只能踏实地努力了。\x02\x03",

            "#10400F……对了，梅尔卡瓦内的设施\x01",
            "全都可以自由使用。\x02\x03",

            "包括装备、消耗品、工房等机能，\x01",
            "另外上层还有休息室哦。\x02\x03",

            "#10409F不如去熟悉一下环境吧，\x01",
            "顺便还能和艇内的成员们打个招呼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5E4E")

    label("loc_5DDC")


    #C0157
    ChrTalk(
        0xA,
        (
            "#10400F梅尔卡瓦内的设施\x01",
            "全都可以自由使用哦。\x02\x03",

            "#10409F不如去熟悉一下环境吧，\x01",
            "顺便还能和艇内的成员们打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E4E")

    TalkEnd(0xFE)
    Return()

    # Function_15_48EA end

    def Function_16_5E52(): pass

    label("Function_16_5E52")


    #C0158
    ChrTalk(
        0xA,
        (
            "#10403F异变发生之前，\x01",
            "我们曾在乌尔斯拉间道的\x01",
            "河滩附近找到了『狭间』……\x02\x03",

            "#10400F今后也要继续寻找新的『狭间』，\x01",
            "以便让梅尔卡瓦着陆。\x02\x03",

            "#10406F梅尔卡瓦上人手不足，\x01",
            "今后的情况大概会很艰难。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#00003F……不过，现在也只能\x01",
            "一步一步往前走了。\x02\x03",

            "#00001F与同伴会合，夺回琪雅……\x01",
            "这当然不是\x01",
            "那么简单的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "#10402F呵呵，说的没错，\x01",
            "但我们能做的也只有踏实地努力下去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 7)
    Return()

    # Function_16_5E52 end

    def Function_17_5FC8(): pass

    label("Function_17_5FC8")


    #C0161
    ChrTalk(
        0xA,
        "#10402F哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#00005F你才是呢，瓦吉……\x01",
            "身体状况如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "#10404F嗯，不必担心。如你所见，\x01",
            "稍稍休息过一阵之后，已经没什么事了。\x02\x03",

            "#10408F由于副作用太强，\x01",
            "所以我平时一直都\x01",
            "尽量抑制力量……\x02\x03",

            "#10404F呵呵，真是好久\x01",
            "都没有这样亢奋过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#00000F拿出全部力量将瓦鲁多打倒，\x01",
            "让他彻底服气……\x02\x03",

            "这样做是很有必要的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "#10404F嗯，正是如此。\x02\x03",

            "#10408F……如果我从一开始就拿出全力，\x01",
            "他或许就不会钻牛角尖\x01",
            "到那种地步了。\x02\x03",

            "#10403F从这一点来看，\x01",
            "我其实应该承担所有责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#00005F哪里的话……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "#10402F呵呵，没关系。\x01",
            "我并不是在后悔，\x01",
            "只是今后必须要吸取教训了。\x02\x03",

            "#10404F如此一来……\x01",
            "我终于以自己的身份\x01",
            "与他做了彻底的了断。\x02\x03",

            "圣书会首领\x01",
            "瓦吉·赫米斯菲亚的使命，\x01",
            "至此就已经彻底结束了。\x02\x03",

            "#10402F请容我向见证了这一切\x01",
            "的各位表示谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……不用客气。\x02\x03",

            "#00000F接下来，恐怕还有不少\x01",
            "相当棘手的强敌在等着我们……\x01",
            "再次请你多加关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "#10402F呵呵，明白了，队长。\x02\x03",

            "#10404F现在开始，我将以\x01",
            "星杯骑士与特别任务支援科成员\x01",
            "的身份来协助大家。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 1)
    Return()

    # Function_17_5FC8 end

    def Function_18_638B(): pass

    label("Function_18_638B")


    #C0170
    ChrTalk(
        0xA,
        (
            "#10400F虽然从『风之剑圣』口中\x01",
            "了解到了很多情报，\x01",
            "但仍然存在着数个谜团。\x02\x03",

            "#10403F『碧零计划』的真相、\x01",
            "大胡子熊律师的计划全貌……\x02\x03",

            "#10408F『零之至宝』琪雅的潜在能力，\x01",
            "以及玛丽亚贝尔小姐他们\x01",
            "如何在计划中利用其能力……\x02\x03",

            "#10406F这些问题，恐怕只有当面询问\x01",
            "才能得到答案了。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00001F嗯……只要能抵达他们的面前，\x01",
            "就一定可以揭开真相。\x02\x03",

            "#00008F琪雅为什么甘愿协助他们，\x01",
            "这个问题也必须要……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "#10404F……嗯，我认为不必担心。\x02\x03",

            "#10402F虽然相处的时间并不算久，\x01",
            "但你们与琪雅之间的『羁绊』是毋庸置疑的。\x02\x03",

            "#10409F无论发生了什么，\x01",
            "只要你们坚持追寻自己的目标，\x01",
            "希望就永远不会消失。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000F……说的没错，\x01",
            "一定会一切顺利的。\x02\x03",

            "#00005F瓦吉，虽然你一副局外人的口气，\x01",
            "但你其实也身在这『羁绊』之中吧？\x02\x03",

            "#00004F琪雅一定也是这样想的……\x01",
            "我们一起去把她接回家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "#10404F……呵呵，这话说得\x01",
            "真是让人开心呢。\x02\x03",

            "#10402F既然如此，\x01",
            "我就奉陪到底好了。\x01",
            "这也是为了可爱的琪雅。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 2)
    Return()

    # Function_18_638B end

    def Function_19_66EA(): pass

    label("Function_19_66EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_68D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6708")
    Call(1, 21)
    Jump("loc_68CB")

    label("loc_6708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6823")

    #C0175
    ChrTalk(
        0xD,
        (
            "#10708F杀手『银』和剧团演员这两条道路……\x01",
            "今后究竟要走向哪一条，\x01",
            "我还没有做出最后决断……\x02\x03",

            "#10704F但是，现在的我……\x01",
            "只想守护克洛斯贝尔……守护伊莉娅小姐他们\x01",
            "所在的这片土地，这种心情是十分真切的。\x02\x03",

            "#10702F为了守护『最重要的人』……\x01",
            "我会和大家一起\x01",
            "竭尽全力的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_68CB")

    label("loc_6823")


    #C0176
    ChrTalk(
        0xD,
        (
            "#10704F现在的我……\x01",
            "只想守护克洛斯贝尔……守护伊莉娅小姐他们\x01",
            "所在的这片土地，这种心情是十分真切的。\x02\x03",

            "#10702F为了守护『最重要的人』……\x01",
            "我会和大家一起\x01",
            "竭尽全力的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68CB")

    Jump("loc_7374")

    label("loc_68D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_697A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68EB")
    Call(1, 20)
    Jump("loc_6975")

    label("loc_68EB")


    #C0177
    ChrTalk(
        0xD,
        (
            "#10703F多亏有大家的帮助，\x01",
            "总算和她做了个\x01",
            "正式的了断。\x02\x03",

            "#10702F为了回报此恩……\x01",
            "我一定会奉陪到最后，\x01",
            "和大家一起将这次的事件彻底解决。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6975")

    Jump("loc_7374")

    label("loc_697A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_END)), "loc_6AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_699A")
    Call(1, 54)
    Jump("loc_6AA1")

    label("loc_699A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A26")

    #C0178
    ChrTalk(
        0xD,
        (
            "#10703F……我已经准备好了，\x01",
            "这就去壁障那里吧。\x02\x03",

            "#10701F为了寻找到自己今后\x01",
            "要选择的道路……\x01",
            "我也必须要再次面对她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AA1")

    label("loc_6A26")


    #C0179
    ChrTalk(
        0xD,
        (
            "#10703F……我已经准备好了，\x01",
            "请让我加入探索队伍吧。\x02\x03",

            "#10701F为了寻找到自己今后\x01",
            "要选择的道路……\x01",
            "我也必须要再次面对她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AA1")

    Jump("loc_7374")

    label("loc_6AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_6BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B66")

    #C0180
    ChrTalk(
        0xD,
        (
            "#10703F……终于走到了这一步啊。\x02\x03",

            "包括『她』在内，前方必定有\x01",
            "大量强敌在等着我们……\x02\x03",

            "#10701F在前进的路上一定要保持警戒，\x01",
            "这也是为了亲手将我们的\x01",
            "重要存在取回……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6BF1")

    label("loc_6B66")


    #C0181
    ChrTalk(
        0xD,
        (
            "#10703F包括『她』在内，前方必定有\x01",
            "大量强敌在等着我们……\x02\x03",

            "#10701F在前进的路上一定要保持警戒，\x01",
            "这也是为了亲手将我们的\x01",
            "重要存在取回……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF1")

    Jump("loc_7374")

    label("loc_6BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D28")

    #C0182
    ChrTalk(
        0xD,
        (
            "#10703F就算是为了给自己一个交代……\x01",
            "我也必须要与等待在\x01",
            "『大树』的『她』做个了结。\x02\x03",

            "#10701F……我已经有所觉悟了。\x01",
            "如果已经准备完毕，就立刻出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00003F（彩虹剧团已经解放，\x01",
            "  如今是否应该……）\x02\x03",

            "（在前往大树之前，\x01",
            "  带莉夏去『那个人』\x01",
            "  所在的地方呢……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6DBF")

    label("loc_6D28")


    #C0184
    ChrTalk(
        0xD,
        (
            "#10703F就算是为了给自己一个交代……\x01",
            "我也必须要与等待在\x01",
            "『大树』的『她』做个了结。\x02\x03",

            "#10701F……我已经有所觉悟了。\x01",
            "如果已经准备完毕，就立刻出发吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DBF")

    Jump("loc_6F17")

    label("loc_6DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA7")

    #C0185
    ChrTalk(
        0xD,
        (
            "#10704F伊莉娅小姐给了我勇气，\x01",
            "如今的我已经再无畏惧。\x02\x03",

            "#10701F接下来，就算是为了给自己一个交代，\x01",
            "我也必须要与『她』决一高下……\x02\x03",

            "#10702F……我已经有所觉悟了。\x01",
            "如果已经准备完毕，\x01",
            "我们就立刻前往『大树』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6F17")

    label("loc_6EA7")


    #C0186
    ChrTalk(
        0xD,
        (
            "#10704F伊莉娅小姐给了我勇气，\x01",
            "如今的我已经再无畏惧。\x02\x03",

            "#10702F如果已经准备完毕，\x01",
            "我们就立刻前往『大树』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F17")

    Jump("loc_7374")

    label("loc_6F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_70B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_700C")

    #C0187
    ChrTalk(
        0xD,
        (
            "#10708F身为『银』的我竟然会\x01",
            "帮助大家拯救克洛斯贝尔……\x02\x03",

            "#10703F事到如今才说这种话可能有点奇怪，\x01",
            "但总觉得自己是在做和身份不相符的事。\x02\x03",

            "#10701F……不过，为了解放\x01",
            "克洛斯贝尔市和彩虹剧团……\x01",
            "我一定会拿出全力的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_70AE")

    label("loc_700C")


    #C0188
    ChrTalk(
        0xD,
        (
            "#10708F身为『银』的我竟然会\x01",
            "帮助大家拯救克洛斯贝尔……\x01",
            "总觉得自己是在做和身份不相符的事。\x02\x03",

            "#10701F但为了解放\x01",
            "克洛斯贝尔市和彩虹剧团……\x01",
            "我一定会拿出全力的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70AE")

    Jump("loc_7374")

    label("loc_70B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_7147")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70CE")
    Call(1, 8)
    Jump("loc_7142")

    label("loc_70CE")


    #C0189
    ChrTalk(
        0xD,
        (
            "#10708F『血腥谢莉』……\x01",
            "虽然很在意她的动向……\x02\x03",

            "#10703F……但如今还是把精神集中在\x01",
            "援救艾莉小姐他们的行动上吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7142")

    Jump("loc_7374")

    label("loc_7147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_7374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72DC")

    #C0190
    ChrTalk(
        0xD,
        (
            "#10705F你、你真的不会把有关『银』的\x01",
            "事情写在报道里吧……？\x02\x03",

            "#10706F总有些担心呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xF,
        (
            "#02103F大家关注的剧团秘闻！\x01",
            "传说中的『银』的历史、舞台幕后的秘密！\x01",
            "以及莉夏·毛的三围尺寸！\x02\x03",

            "#02109F难得有这样的好机会，\x01",
            "可要毫无保留地向我坦白哟～¤\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0192
    ChrTalk(
        0xD,
        "#10706F呜呜呜～罗伊德警官……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#00012F总、总之，\x01",
            "你就努力敷衍好了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x1, 0)
    Jump("loc_7374")

    label("loc_72DC")


    #C0194
    ChrTalk(
        0xD,
        (
            "#10706F在平时，剧团长肯定会在\x01",
            "适当的时候帮我打断……\x01",
            "从、从来没接受过这么纠缠不休的采访。\x02\x03",

            "#10709F真的不会把这些事\x01",
            "写进报道里吧……\x01",
            "总有些担心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7374")

    TalkEnd(0xFE)
    Return()

    # Function_19_66EA end

    def Function_20_7378(): pass

    label("Function_20_7378")


    #C0195
    ChrTalk(
        0xD,
        (
            "#10703F『血腥谢莉』……\x02\x03",

            "正如其绰号一样，\x01",
            "她所走过的道路上应该洒满了鲜血吧。\x02\x03",

            "将杀戮视为自己的生存价值，\x01",
            "在战场中寻找让自己畅快的乐趣，\x01",
            "最终造就了如今的她……\x02\x03",

            "#10708F对身为『银』的我来说，\x01",
            "就像是看到了从前的自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#00001F莉夏……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        (
            "#10704F不过……我能感觉到，\x01",
            "自己已经有了真正意义上的改变。\x02\x03",

            "#10702F与伊莉娅小姐、罗伊德警官……\x01",
            "还有大家的相遇，\x01",
            "使我改变了很多。\x02\x03",

            "#10703F成长经历与谢莉很相似的我，\x01",
            "在大家的影响下，却可以走向完全不同的道路……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#00004F人和人的相遇啊……\x02\x03",

            "#00000F仔细想想，\x01",
            "再没有比这更加奇妙的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xD,
        (
            "#10702F嗯……是啊。\x02\x03",

            "#10704F多亏有大家的帮助，\x01",
            "总算和她做了个\x01",
            "正式的了断。\x02\x03",

            "#10702F为了回报此恩……\x01",
            "我一定会奉陪到最后，\x01",
            "和大家一起将这次的事件彻底解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#00000F嗯，拜托了，莉夏。\x02\x03",

            "让我们一起把琪雅救出……\x01",
            "欢笑着回到伊莉娅小姐他们的身边吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xD,
        "#10709F呵呵，嗯！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 5)
    Return()

    # Function_20_7378 end

    def Function_21_76A5(): pass

    label("Function_21_76A5")


    #C0202
    ChrTalk(
        0xD,
        (
            "#10708F……漫长的旅途\x01",
            "终于接近尾声了啊。\x02\x03",

            "#10703F在那位玛丽亚贝尔小姐的面前，\x01",
            "不知道『银』的力量\x01",
            "究竟能起到多少作用……\x02\x03",

            "#10701F但无论如何，我也会竭尽全力，\x01",
            "与大家一起努力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#00000F嗯……拜托了。\x02\x03",

            "#00009F哈哈，现在再说这些也许有点奇怪……\x01",
            "但仔细想想，我们时而交战，时而联手，\x01",
            "还真是共同经历过不少事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xD,
        (
            "#10709F啊、啊哈哈……\x01",
            "之前的事情真是抱歉呢。\x02\x03",

            "#10703F杀手『银』和剧团演员这两条道路……\x01",
            "今后究竟要走向哪一条，\x01",
            "我还没有做出最后决断……\x02\x03",

            "#10702F但是，现在的我……\x01",
            "只想守护克洛斯贝尔……守护伊莉娅小姐他们\x01",
            "所在的这片土地，这种心情是十分真切的。\x02\x03",

            "#10704F如果以『银』的身份\x01",
            "而掌握的力量可以发挥作用……\x01",
            "我一定会毫不迷茫地展现力量的。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#00004F谢谢，莉夏……\x01",
            "那就拜托你了。\x02\x03",

            "#00000F为了守护『最重要的人』，\x01",
            "我们就一起努力吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xD,
        "#10702F是……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 6)
    Return()

    # Function_21_76A5 end

    def Function_22_79A8(): pass

    label("Function_22_79A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_7B00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79C6")
    Call(1, 23)
    Jump("loc_7AFB")

    label("loc_79C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A7F")

    #C0207
    ChrTalk(
        0x13,
        (
            "#01203F#3C从前的『幻之至宝』\x01",
            "最终选择了自我毁灭的道路……\x02\x03",

            "#01200F琪雅恐怕也并非\x01",
            "没有走向同一条\x01",
            "道路的可能性。\x02\x03",

            "人类之子啊，快去将琪雅夺回，\x01",
            "阻止悲剧再次发生吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7AFB")

    label("loc_7A7F")


    #C0208
    ChrTalk(
        0x13,
        (
            "#01203F#3C琪雅未必不会与\x01",
            "当年的『幻之至宝』\x01",
            "走向同样的道路。\x02\x03",

            "#01200F人类之子啊，快去将琪雅夺回，\x01",
            "阻止悲剧再次发生吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AFB")

    Jump("loc_8627")

    label("loc_7B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_7C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC6")

    #C0209
    ChrTalk(
        0x13,
        (
            "#01203F#3C琪雅如今一定在\x01",
            "『大树』中的某处。\x02\x03",

            "#01200F恐怕会是最深处……\x01",
            "与库罗伊斯家族的女孩，\x01",
            "还有那个身为幕后黑手的律师在一起。\x02\x03",

            "如果需要我的帮助，\x01",
            "随时可以呼叫我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7C23")

    label("loc_7BC6")


    #C0210
    ChrTalk(
        0x13,
        (
            "#01203F#3C琪雅如今一定在\x01",
            "『大树』中的某处。\x02\x03",

            "#01200F如果需要我的帮助，\x01",
            "随时可以呼叫我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C23")

    Jump("loc_8627")

    label("loc_7C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D00")

    #C0211
    ChrTalk(
        0x13,
        (
            "#01200F#3C那棵『大树』\x01",
            "究竟可以造成何种程度的影响，\x01",
            "连我都无法估量。\x02\x03",

            "它存在着可以与女神匹敌的力量……\x01",
            "即使这样说也并不为过。\x02\x03",

            "#01203F人类的妄执不断膨胀，\x01",
            "竟可使状况发展到如此地步……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7D86")

    label("loc_7D00")


    #C0212
    ChrTalk(
        0x13,
        (
            "#01200F#3C那棵『大树』存在着\x01",
            "可以与女神匹敌的力量……\x01",
            "即使这样说也并不为过。\x02\x03",

            "#01203F人类妄执的结果\x01",
            "竟可使状况发展到如此地步……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D86")

    Jump("loc_8627")

    label("loc_7D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EDD")

    #C0213
    ChrTalk(
        0x13,
        (
            "#01203F#3C分布在克洛斯贝尔各处的钟\x01",
            "可以生成使『至宝』的力量\x01",
            "产生增幅的『力场』……\x02\x03",

            "#01200F通过现状来分析，\x01",
            "约鲁古的调查结果应该是可以相信的。\x02\x03",

            "#01203F说起来，\x01",
            "还有那个教团的『摇篮』……\x01",
            "凭人类的力量，竟能创造出如此惊人的东西。\x02\x03",

            "#01200F从中似乎也能清楚地窥视到库罗伊斯\x01",
            "家族的炼金术师们那不可理喻的妄执了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7F87")

    label("loc_7EDD")


    #C0214
    ChrTalk(
        0x13,
        (
            "#01203F#3C说起来，\x01",
            "还有那个教团的『摇篮』……\x01",
            "凭人类的力量，竟能创造出如此惊人的东西。\x02\x03",

            "#01200F从中似乎也能清楚地窥视到库罗伊斯\x01",
            "家族的炼金术师们那不可理喻的妄执了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F87")

    Jump("loc_8627")

    label("loc_7F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_812E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA7")
    Call(1, 4)
    Jump("loc_8129")

    label("loc_7FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8099")

    #C0215
    ChrTalk(
        0x13,
        (
            "#01203F#3C如今的你们，\x01",
            "已经不再需要我来保护了。\x02\x03",

            "#01200F我会和以前一样，在后方待命，\x01",
            "在有需要的时候就呼叫我吧。\x02\x03",

            "今后我会以原本的形态\x01",
            "奔赴至战线。\x02\x03",

            "#01203F呵呵，如果对手只是一般程度的魔兽，\x01",
            "大概一瞬间就可以轻松解决了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8129")

    label("loc_8099")


    #C0216
    ChrTalk(
        0x13,
        (
            "#01200F#3C在情况需要时只要呼叫我，\x01",
            "我就会以原本的形态\x01",
            "奔赴至战线。\x02\x03",

            "#01203F呵呵，如果对手只是一般程度的魔兽，\x01",
            "大概一瞬间就可以轻松解决了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8129")

    Jump("loc_8627")

    label("loc_812E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82B4")

    #C0217
    ChrTalk(
        0x13,
        (
            "#01200F#3C对猎兵们的佯攻任务就交给我吧。\x01",
            "只要我恢复原本的形态，\x01",
            "应该可以牵制不少战力。\x02\x03",

            "你们就趁此机会击退零散的部队，\x01",
            "前往艾莉他们的所在之处吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#00003F对手是那些强悍的猎兵，\x01",
            "即使是蔡特，恐怕也会相当危险……\x02\x03",

            "#00001F请一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x13,
        (
            "#01203F#3C呵呵，不必担心，\x01",
            "我可没打算被敌人轻易干掉。\x02\x03",

            "#01200F赌上神狼的骄傲，\x01",
            "我一定会最大限度地打乱敌人的战线。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8343")

    label("loc_82B4")


    #C0220
    ChrTalk(
        0x13,
        (
            "#01203F#3C只要我恢复原本的形态，就算对手\x01",
            "是那些猎兵，也足以吸引住相当的数量。\x02\x03",

            "#01200F赌上神狼的骄傲，\x01",
            "我一定会最大限度地打乱敌人的战线。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8343")

    Jump("loc_8627")

    label("loc_8348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_8407")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8363")
    Call(1, 3)
    Jump("loc_8402")

    label("loc_8363")


    #C0221
    ChrTalk(
        0x13,
        (
            "#01200F#3C从乌尔斯拉还活着的时代开始，那些狼就是\x01",
            "伴随在我身边的眷属，世世代代地守望着克洛斯贝尔。\x02\x03",

            "它们如今一定正在什么地方\x01",
            "观望着现在的状况，\x01",
            "不必担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8402")

    Jump("loc_8627")

    label("loc_8407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85B9")

    #C0222
    ChrTalk(
        0x13,
        "#01200F#3C……那个护士女孩……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0223
    ChrTalk(
        0x101,
        (
            "#00005F哎……\x01",
            "塞茜尔姐姐怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x13,
        (
            "#01203F#3C……呵呵，没什么。\x01",
            "我只是在想，这可真是命运啊。\x02\x03",

            "没什么重要的事，\x01",
            "请不必在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        "#00000F哎……？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x13,
        (
            "#01200F#3C总之，\x01",
            "能与缇欧顺利再会，\x01",
            "可以算是意想不到的幸运。\x02\x03",

            "希望能继续保持这种势头，\x01",
            "与支援科的其他同伴重逢。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00000F嗯，虽然不太明白你刚才说的什么命运……\x01",
            "但我一定会继续努力的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8627")

    label("loc_85B9")


    #C0228
    ChrTalk(
        0x13,
        (
            "#01200F#3C总之，\x01",
            "能与缇欧再会，\x01",
            "可以算是意想不到的幸运。\x02\x03",

            "她现在似乎很忙……\x01",
            "呵呵，稍后再过去\x01",
            "看看她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8627")

    TalkEnd(0xFE)
    Return()

    # Function_22_79A8 end

    def Function_23_862B(): pass

    label("Function_23_862B")


    #C0229
    ChrTalk(
        0x13,
        (
            "#01200F#3C过去的『幻之至宝』\x01",
            "最终选择了自我毁灭的道路……\x02\x03",

            "罗伊德，我当时和你说过这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00001F嗯，那是为了防止自己\x01",
            "失去控制，伤害到本应守护\x01",
            "的人们……\x02\x03",

            "#00003F……身为『零之至宝』的琪雅\x01",
            "也会遭遇同样的下场吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x13,
        (
            "#01200F#3C……目前还无法断言。\x02\x03",

            "但琪雅已经化身为『零之至宝』，\x01",
            "并创造出了这棵可与女神之力\x01",
            "相匹敌的『大树』。\x02\x03",

            "如今谁也无法保证\x01",
            "这种巨大的力量\x01",
            "可以一直得到控制。\x02\x03",

            "#01203F也就是说，琪雅未必不会\x01",
            "与当年的『幻之至宝』\x01",
            "走上相同的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x02\x03",

            "#00001F不，只要还有我们在，\x01",
            "就绝对不会让那种情况发生……！\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x13,
        "#01200F#3C……呵呵，这才像你。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 0)
    Return()

    # Function_23_862B end

    def Function_24_8871(): pass

    label("Function_24_8871")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8898")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7F), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8898")
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1DE, 3)

    label("loc_8898")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6B), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88B3")
    Call(1, 53)
    Jump("loc_8EBA")

    label("loc_88B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8954")

    #C0234
    ChrTalk(
        0x14,
        (
            "#00603F你拥有自己独有的素质。\x01",
            "只要继续发挥那些优点，\x01",
            "就一定可以成为一名优秀的搜查官。\x02\x03",

            "#00602F以自己心中的完美搜查官为目标，\x01",
            "继续努力提高吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EBA")

    label("loc_8954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_8A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_896F")
    Call(1, 25)
    Jump("loc_8A95")

    label("loc_896F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A25")

    #C0235
    ChrTalk(
        0x14,
        (
            "#00603F盖伊·班宁斯的死亡……\x01",
            "时隔三年，\x01",
            "终于真相大白了。\x02\x03",

            "接下来要做的，就只有\x01",
            "从真正意义上解决此事件了。\x02\x03",

            "#00602F出发吧，班宁斯。\x01",
            "如今正是超越你哥哥的时候。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8A95")

    label("loc_8A25")


    #C0236
    ChrTalk(
        0x14,
        (
            "#00603F接下来要做的，就只有\x01",
            "从真正意义上解决此事件了。\x02\x03",

            "#00602F出发吧，班宁斯。\x01",
            "如今正是超越你哥哥的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A95")

    Jump("loc_8EBA")

    label("loc_8A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_8C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BCA")

    #C0237
    ChrTalk(
        0x14,
        (
            "#00600F不要停下脚步，班宁斯。\x01",
            "只有一步一步地努力前进，\x01",
            "才能不断接近真相。\x02\x03",

            "#00603F如今还不知道那棵『大树』\x01",
            "将会对克洛斯贝尔造成怎样的影响，\x01",
            "因此必须要尽早将此事件解决。\x02\x03",

            "#00608F伊安律师，马克莱因……\x01",
            "这些对手都不是用寻常手段就可以战胜的，\x01",
            "但我们无论如何也必须要完成任务。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8C94")

    label("loc_8BCA")


    #C0238
    ChrTalk(
        0x14,
        (
            "#00600F如今还不知道那棵『大树』\x01",
            "将会对克洛斯贝尔造成怎样的影响，\x01",
            "因此必须要尽早将此事件解决。\x02\x03",

            "#00608F伊安律师，马克莱因……\x01",
            "这些对手都不是用寻常手段就可以战胜的，\x01",
            "但我们无论如何也必须要完成任务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C94")

    Jump("loc_8EBA")

    label("loc_8C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E15")

    #C0239
    ChrTalk(
        0x14,
        (
            "#00608F真没想到，伊安律师\x01",
            "竟然是真正的幕后黑手……\x02\x03",

            "#00610F可恶，我平时频繁拜访律师事务所，\x01",
            "却始终没有丝毫察觉，这是何等的无能。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#00003F达德利警官……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x14,
        (
            "#00603F……总之，既然事情已经变成这样，\x01",
            "我们也只有当面质问律师和马克莱因，\x01",
            "才能了解他们的真实用意了。\x02\x03",

            "#00601F这已经不仅是支援科的问题了，\x01",
            "我们无论如何也要查明真相。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        "#00000F是……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8EBA")

    label("loc_8E15")


    #C0243
    ChrTalk(
        0x14,
        (
            "#00603F总之，既然事情已经变成这样，\x01",
            "我们也只有当面质问律师和马克莱因，\x01",
            "才能了解他们的真实用意了。\x02\x03",

            "#00600F这已经不是支援科的问题了，\x01",
            "我们无论如何也要查明真相。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EBA")

    TalkEnd(0xFE)
    Return()

    # Function_24_8871 end

    def Function_25_8EBE(): pass

    label("Function_25_8EBE")


    #C0244
    ChrTalk(
        0x14,
        (
            "#00600F盖伊·班宁斯的死亡……\x01",
            "时隔三年，\x01",
            "终于真相大白了。\x02\x03",

            "#00603F这些年来，马克莱因竟然\x01",
            "一直都背负着如此沉重的包袱啊。\x02\x03",

            "#00608F……真是个超级蠢才。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#00003F将一切都视为对自己的惩戒，\x01",
            "并切断全部退路，\x01",
            "一心向前，永不回头……\x02\x03",

            "#00008F或许正是因为如此，\x01",
            "亚里欧斯先生才会那样强大吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x14,
        (
            "#00603F……但那并不是正确的变强之道。\x02\x03",

            "#00608F相信那家伙自己也很清楚……\x01",
            "正因如此，他才会为你们开启道路。\x02\x03",

            "#00600F总之，班宁斯，\x01",
            "如此一来，你终于可以\x01",
            "从盖伊死亡的阴影中解脱了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00004F……是的。\x01",
            "虽然还需要一定时间将问题理清，\x01",
            "但已经不要紧了。\x02\x03",

            "#00001F如今……\x01",
            "我们必须要全力跨越最后的『壁障』——\x01",
            "伊安律师与玛丽亚贝尔小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x14,
        (
            "#00604F那就好。\x02\x03",

            "#00602F为了从真正意义上\x01",
            "将此次事件解决……\x01",
            "我们只有继续前进。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#00000F是……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 2)
    Return()

    # Function_25_8EBE end

    def Function_26_919C(): pass

    label("Function_26_919C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91AA")
    Call(0, 11)
    Return()

    label("loc_91AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91CC")
    Call(1, 56)
    TalkEnd(0xFE)
    Return()

    label("loc_91CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_931A")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91FA")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x8, 0x0, 0)

    label("loc_91FA")


    #C0250
    ChrTalk(
        0x8,
        (
            "#12100F……对了，机会难得，\x01",
            "就把这个给你吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『阿巴斯的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 0)
    OP_E4(0x3)

    #C0252
    ChrTalk(
        0x101,
        (
            "#00000F『波波碰！』的账号……？\x01",
            "阿巴斯，你也玩这个吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#12102F只在有空的时候玩玩而已。\x02\x03",

            "#12100F如有兴趣，我可以当你的对手，\x01",
            "尽管向我挑战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9315")
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9315")

    Jump("loc_9357")

    label("loc_931A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9330")
    Call(1, 28)
    Jump("loc_9357")

    label("loc_9330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9346")
    Call(1, 29)
    Jump("loc_9357")

    label("loc_9346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9357")
    Call(1, 30)

    label("loc_9357")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9368")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_93B5")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                  # 0
            "乘坐梅尔卡瓦移动\x01",      # 1
            "编组队伍\x01",              # 2
            "放弃\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_93F5")

    label("loc_93B5")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                  # 0
            "乘坐梅尔卡瓦移动\x01",      # 1
            "放弃\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93F5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93F5")

    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9414"),
        (1, "loc_A794"),
        (2, "loc_AAD8"),
        (SWITCH_DEFAULT, "loc_AAF4"),
    )


    label("loc_9414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_9513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94B1")

    #C0254
    ChrTalk(
        0x8,
        (
            "#12100F说不定今后还会与\x01",
            "『赤色星座』有所牵扯……\x02\x03",

            "但如今最重要的就是\x01",
            "解决此次事件。\x02\x03",

            "为了迎接最后的战斗，\x01",
            "做好万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_950E")

    label("loc_94B1")


    #C0255
    ChrTalk(
        0x8,
        (
            "#12100F我们也会以星杯骑士的身份\x01",
            "履行自己的使命，直至最后的。\x02\x03",

            "你们也做好\x01",
            "万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_950E")

    Jump("loc_A78F")

    label("loc_9513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_9589")

    #C0256
    ChrTalk(
        0x8,
        (
            "#12100F……剑蛇帮的\x01",
            "那些家伙想必\x01",
            "都很担心瓦鲁多。\x02\x03",

            "克洛斯贝尔的危机消除之后，\x01",
            "得把他也带回去才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A78F")

    label("loc_9589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_97BF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_964D")

    #C0257
    ChrTalk(
        0x8,
        (
            "#12100F机体的受损程度很轻微，\x01",
            "完全不影响飞行。\x02\x03",

            "我们会一直在舰内待命，\x01",
            "以确保可以随时带你们\x01",
            "离开『大树』。\x02\x03",

            "想离开『大树』的时候，\x01",
            "向我做出指示即可。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_96AA")

    label("loc_964D")


    #C0258
    ChrTalk(
        0x8,
        (
            "#12100F梅尔卡瓦似乎并没有\x01",
            "遭受到严重损伤。\x02\x03",

            "如果想离开『大树』，\x01",
            "只要向我做出指示即可。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96AA")

    Jump("loc_97BA")

    label("loc_96AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9759")

    #C0259
    ChrTalk(
        0x8,
        (
            "#12100F机体的受损程度很轻微，\x01",
            "完全不影响飞行。\x02\x03",

            "通向『碧之大树』内部\x01",
            "的安全飞行路线也已经掌握了。\x02\x03",

            "如果想再次前往『大树』，\x01",
            "只要向我做出指示即可。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_97BA")

    label("loc_9759")


    #C0260
    ChrTalk(
        0x8,
        (
            "#12100F梅尔卡瓦似乎并没有\x01",
            "遭受到严重损伤。\x02\x03",

            "如果想再次前往『大树』，\x01",
            "只要向我做出指示即可。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97BA")

    Jump("loc_A78F")

    label("loc_97BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_993D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98C0")

    #C0261
    ChrTalk(
        0x8,
        (
            "#12100F『碧之大树』的出现\x01",
            "究竟意味着什么，目前连\x01",
            "教会也无法掌握。\x02\x03",

            "我们前往那里之后，\x01",
            "无论遇到怎样的事态\x01",
            "也都不足为奇。\x02\x03",

            "如今已经可以降落至\x01",
            "克洛斯贝尔的各个地点了……\x02\x03",

            "如果有什么需要处理的事情，\x01",
            "不妨在前往大树之前\x01",
            "优先解决。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9938")

    label("loc_98C0")


    #C0262
    ChrTalk(
        0x8,
        (
            "#12100F『碧之大树』的出现\x01",
            "究竟意味着什么，目前连\x01",
            "教会也无法掌握。\x02\x03",

            "总之，在前往『大树』之前，\x01",
            "一定要做好充足准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9938")

    Jump("loc_A78F")

    label("loc_993D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_9B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AA1")

    #C0263
    ChrTalk(
        0x8,
        (
            "#12100F需要停止共鸣的另一口钟……\x01",
            "就在乌尔斯拉间道尽头处的『星见之塔』上。\x02\x03",

            "使徒之一柱——\x01",
            "『钢之圣女』阿瑞安赫德\x01",
            "与其手下的女战士们驻守在那里。\x02\x03",

            "想战胜她们，恐怕是极其困难的……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00001F……不管怎么说，我们也只能硬着头皮上了，\x01",
            "无论如何也要寻找到胜机。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "#12102F嗯，说的好。\x01",
            "如果已经有所觉悟，我们就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9B41")

    label("loc_9AA1")


    #C0266
    ChrTalk(
        0x8,
        (
            "#12100F身为使徒之一柱的『钢之圣女』\x01",
            "与其部下的女战士们都已在\x01",
            "『星见之塔』中严阵以待了。\x02\x03",

            "想战胜她们，恐怕是极其困难的……\x01",
            "如果已经有所觉悟，就前去挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B41")

    Jump("loc_9D32")

    label("loc_9B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C97")

    #C0267
    ChrTalk(
        0x8,
        (
            "#12100F最初的目的地是『月之僧院』……\x01",
            "那是位于玛因兹地区\x01",
            "的中世纪遗迹之一。\x02\x03",

            "据约鲁古老人所说，\x01",
            "守卫在那里的人是执行者\x01",
            "中的『小丑』肯帕雷拉……\x02\x03",

            "此人一般都在幕后行动，\x01",
            "是个相当诡异的人物……\x01",
            "因此我们几乎没有与其相关的情报。\x02\x03",

            "不知道对手设下了什么陷阱，\x01",
            "为了应对一切有可能出现的状况，\x01",
            "还是做足十二分的准备工作为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9D32")

    label("loc_9C97")


    #C0268
    ChrTalk(
        0x8,
        (
            "#12100F执行者中的\x01",
            "『小丑』肯帕雷拉\x01",
            "在『月之僧院』中看守……\x02\x03",

            "不知道对手设下了什么陷阱，\x01",
            "为了应对一切有可能出现的状况，\x01",
            "还是做足十二分的准备工作为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D32")

    Jump("loc_A78F")

    label("loc_9D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_9F35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E7D")

    #C0269
    ChrTalk(
        0x8,
        (
            "#12100F由于麦克道尔议长被救出，\x01",
            "国防军与猎兵加强了\x01",
            "地面警戒的力度。\x02\x03",

            "在这种状况下，梅尔卡瓦\x01",
            "暂时无法在各地着陆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#00001F是吗……既然如此，\x01",
            "我们就先集中精力，\x01",
            "前往无线信号增幅器地点，完成预定计划吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#12100F嗯，接下来的事情\x01",
            "就只剩下决定开始时间了。\x02\x03",

            "如果已经准备结束，就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9F30")

    label("loc_9E7D")


    #C0272
    ChrTalk(
        0x8,
        (
            "#12100F在这种戒严态势下，梅尔卡瓦\x01",
            "暂时无法在各地着陆。\x02\x03",

            "现在就先集中精力，\x01",
            "前往无线信号增幅器地点，\x01",
            "完成预定计划吧。\x02\x03",

            "我这边都已经安排好了，\x01",
            "如果已经准备结束，就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F30")

    Jump("loc_A78F")

    label("loc_9F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_A170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0A8")

    #C0273
    ChrTalk(
        0x8,
        (
            "#12100F我想，抵达米修拉姆之后，\x01",
            "恐怕立刻就会遭到\x01",
            "猎兵们的迎击。\x02\x03",

            "为了防止被对空兵器击坠，\x01",
            "梅尔卡瓦将会停留在上空，\x01",
            "暂时保持隐形状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        (
            "#00006F也就是说，一旦下去，在救出艾莉\x01",
            "他们之前，我们无法再上来了吗……\x01",
            "果然是场相当严峻的战斗呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x8,
        (
            "#12100F嗯，恐怕比你想象的还要严峻。\x02\x03",

            "装备、导力器、回复药……\x01",
            "各方面的准备工作都要做得万无一失。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A16B")

    label("loc_A0A8")


    #C0276
    ChrTalk(
        0x8,
        (
            "#12100F在米修拉姆的战斗开始之后，\x01",
            "为了防止被对空兵器击坠，舰艇将会\x01",
            "停留在上空，暂时保持隐形状态。\x02\x03",

            "在此期间，你们无法返回舰艇内。\x01",
            "装备、导力器、回复药……\x01",
            "各方面的准备工作都要做得万无一失。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A16B")

    Jump("loc_A78F")

    label("loc_A170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_A351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2DE")

    #C0277
    ChrTalk(
        0x8,
        (
            "#12100F那名记者似乎正在仔细调查\x01",
            "梅尔卡瓦和瓦吉。\x02\x03",

            "……哎呀呀，竟然把媒体界的人士\x01",
            "带上来，这可真是前所未闻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x101,
        (
            "#00012F算、算啦……\x01",
            "我想她只不过是想满足自己的\x01",
            "好奇心而已，不会有什么问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        (
            "#12100F……算了，\x01",
            "毕竟有瓦吉的许可。\x02\x03",

            "但万一要是发生了预料之外的事态，\x01",
            "班宁斯，你可要承担\x01",
            "一切责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#00006F（为、为什么是我……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A34C")

    label("loc_A2DE")


    #C0281
    ChrTalk(
        0x8,
        (
            "#12100F哎呀呀，竟然把\x01",
            "媒体界的人士带上来，\x01",
            "这可真是前所未闻啊……\x02\x03",

            "算了，毕竟有瓦吉的许可，\x01",
            "这也没办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A34C")

    Jump("loc_A78F")

    label("loc_A351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_A479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A40B")

    #C0282
    ChrTalk(
        0x8,
        (
            "#12100F警备队的人出于与『黑月』\x01",
            "大相径庭的信念，向政府发起了反抗吗……\x02\x03",

            "不管怎么说，既然公然竖起反旗，\x01",
            "总统那边自然不会坐视不理。\x02\x03",

            "我们还是尽快出发为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A474")

    label("loc_A40B")


    #C0283
    ChrTalk(
        0x8,
        (
            "#12100F就算是原警备队的成员，\x01",
            "如果与国防军和猎兵交战，\x01",
            "恐怕也很难坚持太久。\x02\x03",

            "我们还是尽快出发为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A474")

    Jump("loc_A78F")

    label("loc_A479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A59F")

    #C0284
    ChrTalk(
        0x8,
        (
            "#12100F梅尔卡瓦的机关区域所使用的\x01",
            "『天之车』原本是拥有飞翔机能\x01",
            "的古代遗物……\x02\x03",

            "导力革命之后，在财团的协助下，\x01",
            "改造成了如今的样子。\x02\x03",

            "除此之外，在战术导力器开发等方面，\x01",
            "我们也存在着一定的协力关系。\x02\x03",

            "……不过，这些都是没有向\x01",
            "社会公开的机密情报，\x01",
            "一定不要泄露出去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A623")

    label("loc_A59F")


    #C0285
    ChrTalk(
        0x8,
        (
            "#12100F梅尔卡瓦和战术导力器\x01",
            "都是在财团与教会的协力下\x01",
            "制造出来的……\x02\x03",

            "……这些都是没有向社会公开的机密情报，\x01",
            "一定不要泄露出去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A623")

    Jump("loc_A78F")

    label("loc_A628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A78F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A643")
    Call(1, 27)
    Jump("loc_A78F")

    label("loc_A643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A723")

    #C0286
    ChrTalk(
        0x8,
        (
            "#12100F在前往新场所时，需要有瓦吉的指挥，\x01",
            "并且还要对『神机』保持警戒，\x01",
            "但以目前的状况来看，完全可以应对。\x02\x03",

            "不必担心这些事情，\x01",
            "去做好装备和导力器方面\x01",
            "的准备工作吧。\x02\x03",

            "做好降落的准备之后，\x01",
            "就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A78F")

    label("loc_A723")


    #C0287
    ChrTalk(
        0x8,
        (
            "#12100F不必担心这边的事情，\x01",
            "去做好装备和导力器方面\x01",
            "的准备工作吧。\x02\x03",

            "做好降落的准备之后，\x01",
            "就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A78F")

    Jump("loc_AAFE")

    label("loc_A794")

    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_AAC9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8B7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A7ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8B2")
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8AD")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8AD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_A89E")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A88E")
    Call(0, 6)
    Jump("loc_A891")

    label("loc_A88E")

    Call(0, 5)

    label("loc_A891")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_A8AD")

    label("loc_A89E")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_A8AD")

    Jump("loc_A7ED")

    label("loc_A8B2")

    Jump("loc_AAC3")

    label("loc_A8B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A99E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A999")
    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A994")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A994")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_A985")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A975")
    Call(0, 6)
    Jump("loc_A978")

    label("loc_A975")

    Call(0, 5)

    label("loc_A978")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_A994")

    label("loc_A985")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_A994")

    Jump("loc_A8D4")

    label("loc_A999")

    Jump("loc_AAC3")

    label("loc_A99E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA85")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA80")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA7B")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA7B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_AA6C")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA5C")
    Call(0, 6)
    Jump("loc_AA5F")

    label("loc_AA5C")

    Call(0, 5)

    label("loc_AA5F")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_AA7B")

    label("loc_AA6C")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_AA7B")

    Jump("loc_A9BB")

    label("loc_AA80")

    Jump("loc_AAC3")

    label("loc_AA85")

    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAA1")
    Call(0, 12)

    label("loc_AAA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAB8")
    Call(0, 6)
    Jump("loc_AABB")

    label("loc_AAB8")

    Call(0, 5)

    label("loc_AABB")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)

    label("loc_AAC3")

    Return()

    label("loc_AAC9")

    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_AAFE")

    label("loc_AAD8")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AAFE")

    label("loc_AAF4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AAFE")

    Jump("loc_9368")

    label("loc_AB03")

    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_919C end

    def Function_27_AB0A(): pass

    label("Function_27_AB0A")


    #C0288
    ChrTalk(
        0x8,
        (
            "#12100F之前接到了联络。\x01",
            "梅尔卡瓦五号机\x01",
            "已经顺利甩开了『神机』。\x02\x03",

            "格拉汉姆大人与机内众人\x01",
            "全都平安无事。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#00004F是吗……这就放心了。\x02\x03",

            "#00005F……对了，阿巴斯，\x01",
            "你离开操作席没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#12100F不用担心……\x01",
            "『梅尔卡瓦』的大部分机能\x01",
            "都可以在这个席位上掌控。\x02\x03",

            "而且现在已经转换到自动操作模式，\x01",
            "让舰艇滞留在『狭间』的上空了，\x01",
            "因此没必要坐在操作席。\x02\x03",

            "在前往新场所时，需要有瓦吉的指挥，\x01",
            "并且还要对『神机』保持警戒。\x01",
            "但以目前的状况来看，完全可以应对。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00003F原来如此……\x01",
            "看来确实拥有很高的性能呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#12100F总之，尽量在舰内\x01",
            "做好充分的准备。\x02\x03",

            "做好降落的准备之后，\x01",
            "和我说一声就可以了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 3)
    Return()

    # Function_27_AB0A end

    def Function_28_AD61(): pass

    label("Function_28_AD61")


    #C0293
    ChrTalk(
        0x8,
        (
            "#12100F之前依靠机体的\x01",
            "镜面装甲和抗冲击磁场\x01",
            "完成了强行突破……\x02\x03",

            "不过机体的受损程度很轻微，\x01",
            "完全不影响飞行。\x02\x03",

            "我们会一直在舰内待命，\x01",
            "以确保可以随时带你们\x01",
            "离开『大树』。\x02\x03",

            "想离开『大树』的时候，\x01",
            "向我做出指示即可。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 5)
    Return()

    # Function_28_AD61 end

    def Function_29_AE3C(): pass

    label("Function_29_AE3C")


    #C0294
    ChrTalk(
        0x8,
        (
            "#12100F你们已经把瓦鲁多打败了啊。\x02\x03",

            "……从两年前与瓦吉\x01",
            "一起潜入克洛斯贝尔开始，\x01",
            "我们就与那家伙有所来往了……\x02\x03",

            "为了掩饰自己的身份\x01",
            "而组建了圣书会之后，\x01",
            "瓦吉似乎一直都很开心。\x02\x03",

            "虽然在鲁巴彻策划阴谋的\x01",
            "那段时期，他与瓦鲁多之间\x01",
            "的关系曾变得有些恶劣……\x02\x03",

            "但对瓦吉而言，\x01",
            "瓦鲁多不仅是打架的好对手，\x01",
            "而且一直都是个很好的朋友。\x02\x03",

            "#12102F当然，对瓦鲁多而言也是一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        "#00005F确、确实觉得他们两人很合得来……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "#12100F说不定，这也是\x01",
            "瓦吉一直不拿出真正实力\x01",
            "来对付瓦鲁多的原因之一吧。\x02\x03",

            "不过，毕竟瓦吉没有明言，\x01",
            "所以我也不能确定他的真实想法……\x02\x03",

            "……似乎说了些多余的话，\x01",
            "请不要对别人提及。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        "#00000F啊……嗯，我明白。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 6)
    Return()

    # Function_29_AE3C end

    def Function_30_B0A9(): pass

    label("Function_30_B0A9")


    #C0298
    ChrTalk(
        0x8,
        (
            "#12100F……就在之前，\x01",
            "你们与『剑圣』战斗的时候……\x02\x03",

            "我通过舰艇的雷达\x01",
            "感知到有飞行物体\x01",
            "入侵到了『神域』。\x02\x03",

            "看样子，似乎是赤色星座的\x01",
            "『贝奥武夫号』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0299
    ChrTalk(
        0x101,
        "#00005F哎……那岂不是很危险吗！？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "#12100F不，他们完全无视我们，\x01",
            "而是降落到了其它地点，\x01",
            "没过多久又驶向『大树』之外了。\x02\x03",

            "其目的恐怕是\x01",
            "接走『赤色战鬼』\x01",
            "和『血腥谢莉』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x01",
            "身为警察，本想将他们\x01",
            "带回去审讯呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x8,
        (
            "#12100F算啦，这也没办法。\x01",
            "只靠待命成员，\x01",
            "毕竟无力阻止他们啊。\x02\x03",

            "那种井然有序的撤退方式\x01",
            "也正是猎兵团的专长呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#00003F以后说不定还会\x01",
            "再次见到他们的……\x02\x03",

            "#00001F……至于现在，\x01",
            "我们还是集中精神，\x01",
            "专心解决这次的事件吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        (
            "#12100F嗯，正是如此。\x02\x03",

            "为了面对最后的战斗，\x01",
            "做好万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 7)
    Return()

    # Function_30_B0A9 end

    def Function_31_B371(): pass

    label("Function_31_B371")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B40F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6E), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B39C")
    Call(1, 52)
    TalkEnd(0xC)
    Return()

    label("loc_B39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_B40F")

    #C0305
    ChrTalk(
        0xC,
        (
            "#01909F请仔细保存好\x01",
            "那个护身符哦～\x02\x03",

            "那是我为了祈祷大家平安无事，\x01",
            "用心制作出来的，\x01",
            "一定效果拔群！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_B40F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62D")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B52E")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B4BA")
    Jump("loc_B504")

    label("loc_B4BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B4DA")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B504")

    label("loc_B4DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4FA")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B504")

    label("loc_B4FA")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B504")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jump("loc_B53E")

    label("loc_B52E")

    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xC, 0x0, 0)

    label("loc_B53E")


    #C0306
    ChrTalk(
        0xC,
        (
            "#01900F大家知道名叫『波波碰！』\x01",
            "的导力游戏吗～？\x02\x03",

            "#01909F呵呵，其实我也开始玩了。\x01",
            "不介意的话，我们就来交换账号吧～\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『芙兰的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B61F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B616")
    ClearChrFlags(0xC, 0x10)

    label("loc_B616")

    SetChrSubChip(0xC, 0x0)
    Jump("loc_B628")

    label("loc_B61F")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B628")

    Jump("loc_C857")

    label("loc_B62D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_B794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B648")
    Call(1, 33)
    Jump("loc_B78F")

    label("loc_B648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B731")

    #C0308
    ChrTalk(
        0xC,
        (
            "#01904F虽然我只是忍耐着不安的心情而等待，\x01",
            "但这也算是在和大家\x01",
            "一起战斗吧……\x02\x03",

            "#01902F既然如此，\x01",
            "我该做的事情就只有一件。\x02\x03",

            "#01909F芙兰·希卡……\x01",
            "在此祈祷姐姐和大家\x01",
            "平安归来！\x02\x03",

            "请各位一定一定要\x01",
            "平安无事地回来啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B78F")

    label("loc_B731")


    #C0309
    ChrTalk(
        0xC,
        (
            "#01909F芙兰·希卡……\x01",
            "在此祈祷姐姐和大家\x01",
            "平安归来！\x02\x03",

            "请各位一定一定要\x01",
            "平安无事地回来啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B78F")

    Jump("loc_C857")

    label("loc_B794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_B900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B883")

    #C0310
    ChrTalk(
        0xC,
        (
            "#01900F真是完全没想到\x01",
            "『大树』的内部会\x01",
            "如此美丽啊～\x02\x03",

            "#01904F如果不是这种情况，\x01",
            "就可以尽情欣赏\x01",
            "这美丽的景色了～\x02\x03",

            "#01905F……呃！不行不行，\x01",
            "绝不能大意啊。\x02\x03",

            "#01909F总之，请各位加油！\x01",
            "我会在这里给大家鼓劲的～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B8FB")

    label("loc_B883")


    #C0311
    ChrTalk(
        0xC,
        (
            "#01906F虽然『大树』的内部如此美丽，\x01",
            "但是绝对不能松懈大意呢。\x02\x03",

            "#01909F总之，请各位加油！\x01",
            "我会在这里给大家鼓劲的～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8FB")

    Jump("loc_C857")

    label("loc_B900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BA14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9AF")

    #C0312
    ChrTalk(
        0xC,
        (
            "#01905F要闯进那棵『大树』，\x01",
            "心里总觉得有点害怕……\x02\x03",

            "#01901F……但我也是个警察，\x01",
            "在这种时刻就更要\x01",
            "鼓起勇气才行！\x02\x03",

            "#01909F罗伊德警官，请加油吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BA0F")

    label("loc_B9AF")


    #C0313
    ChrTalk(
        0xC,
        (
            "#01901F……但我也是个警察，\x01",
            "在这种时刻就更要\x01",
            "鼓起勇气才行！\x02\x03",

            "#01909F罗伊德警官，请加油吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA0F")

    Jump("loc_C857")

    label("loc_BA14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_BB8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB09")

    #C0314
    ChrTalk(
        0xC,
        (
            "#01900F只要能想办法解决\x01",
            "结界和白色的『神机』，\x01",
            "侵入市内的成功率就会大增了～\x02\x03",

            "#01904F身在市内的赛尔盖科长他们\x01",
            "应该也能听到『独立无效宣言』，\x01",
            "说不定他们也开始行动了。\x02\x03",

            "#01909F总之，我们还要继续努力！\x01",
            "请各位加油吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BB8A")

    label("loc_BB09")


    #C0315
    ChrTalk(
        0xC,
        (
            "#01900F只要能想办法解决\x01",
            "结界和白色的『神机』，\x01",
            "侵入市内的成功率就会大增了～\x02\x03",

            "#01909F总之，我们还要继续努力！\x01",
            "请各位加油吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB8A")

    Jump("loc_C857")

    label("loc_BB8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BEC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE1B")

    #C0316
    ChrTalk(
        0xC,
        (
            "#01904F（敲打键盘……）\x02\x03",

            "嗯，继续测试……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#00005F芙兰，你在做什么？\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BC81")
    Jump("loc_BCCB")

    label("loc_BC81")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BCA1")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BCCB")

    label("loc_BCA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCC1")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BCCB")

    label("loc_BCC1")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BCCB")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0318
    ChrTalk(
        0xC,
        (
            "#01902F啊，罗伊德警官。\x01",
            "我正在测试麦克风\x01",
            "和摄影机哦～\x02\x03",

            "我们计划通过梅尔卡瓦的控制器，\x01",
            "经由导力网络，将影像与声音\x01",
            "传送到各地。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    #C0319
    ChrTalk(
        0xC,
        (
            "#01904F『我是芙兰·希卡，\x01",
            "  最喜欢姐姐了！』\x02\x03",

            "#01909F……嗯，声音效果良好呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00009F（哈哈，即使在这种状况下，\x01",
            "  芙兰也能将气氛缓和呢……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_BEBB")

    label("loc_BE1B")


    #C0321
    ChrTalk(
        0xC,
        (
            "#01902F我们计划通过梅尔卡瓦的控制器，\x01",
            "经由导力网络，将影像与声音\x01",
            "传送到各地。\x02\x03",

            "#01909F为了让各位市民都能听到\x01",
            "麦克道尔议长的声音，\x01",
            "必须要认真检查设备才行～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEBB")

    Jump("loc_C857")

    label("loc_BEC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BFE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEDB")
    Call(1, 13)
    Jump("loc_BFE4")

    label("loc_BEDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFA2")

    #C0322
    ChrTalk(
        0xC,
        (
            "#01912F呵呵，姐姐能回来，\x01",
            "我真是太高兴了。\x02\x03",

            "#01901F罗伊德警官……\x01",
            "姐姐以后就\x01",
            "拜托你了哦！\x02\x03",

            "#01909F我会默默\x01",
            "祝福你们的！\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00006F（唔、唔唔……\x01",
            "  她好像产生了什么误解吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BFE4")

    label("loc_BFA2")


    #C0324
    ChrTalk(
        0xC,
        (
            "#01901F姐姐以后就\x01",
            "拜托你了哦！\x02\x03",

            "#01909F我会默默\x01",
            "祝福你们的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFE4")

    Jump("loc_C857")

    label("loc_BFE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_C130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0DB")

    #C0325
    ChrTalk(
        0xC,
        (
            "#01908F西克洛斯贝尔街道……\x01",
            "是贝尔加德门的所在地呢。\x02\x03",

            "#01903F姐姐多半就在那里……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0326
    ChrTalk(
        0xC,
        (
            "#01906F呼，现在该想的可不是这些，\x01",
            "我要努力振作才行～\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#00003F（芙兰果然很担心\x01",
            "  诺艾尔呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C12B")

    label("loc_C0DB")


    #C0328
    ChrTalk(
        0xC,
        (
            "#01908F姐姐现在多半就在贝尔加德门吧……\x02\x03",

            "#01906F……她现在正在做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C12B")

    Jump("loc_C857")

    label("loc_C130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_C6D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C560")

    #C0329
    ChrTalk(
        0xC,
        (
            "#01908F……姐姐选择了\x01",
            "现在的道路，甚至不惜\x01",
            "与我们对立……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#00001F嗯……老实说，\x01",
            "我觉得她的觉悟相当坚定。\x02\x03",

            "#00003F诺艾尔为什么能下定\x01",
            "如此坚定的决心呢……\x02\x03",

            "#00008F我总觉得，这一连串的事件\x01",
            "并非全部原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        (
            "#01903F……这只是我的猜测……\x02\x03",

            "#01901F在我们很小的时候，\x01",
            "父亲不幸身亡的事情\x01",
            "也许才是根本原因。\x02\x03",

            "#01908F……在共和国军举行的演习中，\x01",
            "父亲遭到来复枪的『误射』而身亡。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        (
            "#00005F哎……！？\x02\x03",

            "你们的父亲不是\x01",
            "在大约十年前的一起\x01",
            "『事故』中去世的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "#01906F那时我还很小，\x01",
            "所以记得并不是太清楚……\x02\x03",

            "#01908F共和国军在演习过程中出现失误，\x01",
            "开枪后正好射中了正在执行警备任务的父亲……\x01",
            "事情的经过大概就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00003F……是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        (
            "#01903F但以克洛斯贝尔的立场而言，\x01",
            "自然无法将这种事情\x01",
            "处理得太过强硬……\x02\x03",

            "#01908F最终，这件事情就被当作\x01",
            "普通的『事故』而处理了。\x02\x03",

            "妈妈虽然很悲伤，\x01",
            "但考虑到爸爸的工作性质本来就很危险，\x01",
            "最终也只能选择接受现实……\x02\x03",

            "#01903F……但是，姐姐似乎一直都\x01",
            "无法释怀呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#00008F……也许就是这个缘故吧。\x02\x03",

            "#00003F（诺艾尔想要守护克洛斯贝尔\x01",
            "  的意志之所以会如此强烈……\x01",
            "  我总算是明白原因了呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 7)
    Jump("loc_C6CF")

    label("loc_C560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C66F")

    #C0337
    ChrTalk(
        0xC,
        (
            "#01908F……对不起，\x01",
            "好像让气氛变得很沉重了。\x02\x03",

            "#01903F原警备队的成员对国防军的\x01",
            "现状提出了异议……\x02\x03",

            "#01900F我们如今必须要将与他们会合\x01",
            "视为首要考虑的目标。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00003F嗯……没错。\x02\x03",

            "#00000F芙兰，后援工作就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xC,
        "#01909F是，我一定会尽力的～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C6CF")

    label("loc_C66F")


    #C0340
    ChrTalk(
        0xC,
        (
            "#01903F对国防军的现状提出异议的\x01",
            "原警备队成员……\x02\x03",

            "#01900F既然不是姐姐，\x01",
            "那究竟会是谁呢～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6CF")

    Jump("loc_C857")

    label("loc_C6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_C857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6EF")
    Call(1, 32)
    Jump("loc_C857")

    label("loc_C6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7CB")

    #C0341
    ChrTalk(
        0xC,
        (
            "#01900F在探查『狭间』的同时，\x01",
            "顺便也能探查到\x01",
            "危险魔兽的反应呢～\x02\x03",

            "今后我会负起责任，\x01",
            "以正式支援请求的形式，\x01",
            "将有关魔兽的情报发送到终端～\x02\x03",

            "#01909F将魔兽清除之后，\x01",
            "别忘了用休息舱的终端\x01",
            "提交报告哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C857")

    label("loc_C7CB")


    #C0342
    ChrTalk(
        0xC,
        (
            "#01900F虽然我还有很多不足之处，\x01",
            "但一定会竭尽全力\x01",
            "在梅尔卡瓦帮忙的。\x02\x03",

            "#01909F大家将通缉魔兽清除之后，\x01",
            "请使用休息舱的终端\x01",
            "提交报告哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C857")

    TalkEnd(0xC)
    Return()

    # Function_31_B371 end

    def Function_32_C85B(): pass

    label("Function_32_C85B")


    #C0343
    ChrTalk(
        0xC,
        (
            "#01900F梅尔卡瓦上也备有和支援科那台\x01",
            "很相似的报告用终端……\x02\x03",

            "#01909F今后我会负起责任，\x01",
            "将支援请求的情报\x01",
            "发送过去的～！\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00005F哎，是吗？\x01",
            "说起来，休息舱里好像\x01",
            "是有个那样的终端……\x02\x03",

            "#00003F不过，你要从何处获取\x01",
            "那些情报呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xC,
        (
            "#01905F因为我比较在意这个问题，\x01",
            "就去问了阿巴斯先生……\x02\x03",

            "#01904F据说在探查『狭间』的同时，\x01",
            "顺便也能探查到\x01",
            "危险魔兽的反应呢～\x02\x03",

            "#01902F这好像是为了让梅尔卡瓦\x01",
            "在作战行动中能及早发现障碍，\x01",
            "并采取应对手段而加设的机能～\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#00000F原来如此……\x01",
            "如果放任不管，的确会很危险。\x01",
            "我们可以利用空闲时间来清除那些魔兽。\x02\x03",

            "#00009F话说回来，向芙兰提交报告吗……\x01",
            "已经好久没这样做过了，还真是怀念啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xC,
        (
            "#01909F呵呵，确实如此～！\x01",
            "我也有很深的感慨呢～\x02\x03",

            "#01906F使用休息舱的终端机来提交报告，\x01",
            "也许稍微有点麻烦……\x02\x03",

            "#01900F但为了在返回警察局以后\x01",
            "获取应得的评价，现在还是请大家\x01",
            "严格遵照以往的步骤来处理吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#00004F……嗯，说的对。\x02\x03",

            "#00000F那就还像以往一样，后援工作\x01",
            "就全部拜托你了，芙兰。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        "#01909F是，请多指教～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_32_C85B end

    def Function_33_CC05(): pass

    label("Function_33_CC05")


    #C0350
    ChrTalk(
        0xC,
        (
            "#01903F这次真的是最后的\x01",
            "战斗了吧……\x02\x03",

            "#01908F在这种时候，我却只能\x01",
            "在安全的场所内等待，\x01",
            "实在是太没用了……\x02\x03",

            "#01906F其实我也曾无数次幻想过，\x01",
            "上前线与大家并肩战斗。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00003F……哪里的话，并不是非要与敌人\x01",
            "直接交锋才算『战斗』。\x02\x03",

            "#00000F正是因为有芙兰和大家\x01",
            "在等着我们，\x01",
            "我们才能充满斗志。\x02\x03",

            "无论遇到多么艰险的挑战，\x01",
            "也一定要回到大家的身边……\x01",
            "这是我发自内心的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xC,
        (
            "#01900F罗伊德警官……\x01",
            "……我明白了。\x02\x03",

            "#01909F芙兰·希卡……\x01",
            "在此祈祷姐姐和大家\x01",
            "平安归来！\x02\x03",

            "请各位一定一定要\x01",
            "平安无事地回来啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#00002F嗯……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_33_CC05 end

    def Function_34_CE14(): pass

    label("Function_34_CE14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF28")

    #C0354
    ChrTalk(
        0x9,
        (
            "#02305F对了……\x01",
            "你们应该有『波波碰！』\x01",
            "的账号吧？\x02\x03",

            "#02304F哼哼，机会难得，\x01",
            "就把我约纳大人的账号当作礼物告诉你们吧。\x02\x03",

            "#02309F我可是从研发阶段就开始玩这个游戏了，\x01",
            "要是自以为能战胜我，就尽管试试看吧～\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『约纳的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_D5F6")

    label("loc_CF28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_D054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF43")
    Call(1, 36)
    Jump("loc_D04F")

    label("loc_CF43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFEB")

    #C0356
    ChrTalk(
        0x9,
        (
            "#02306F啧，什么嘛，\x01",
            "难得人家\x01",
            "担心你们……\x02\x03",

            "#02300F哼，算了……\x01",
            "总之你们就尽量努力吧。\x02\x03",

            "#02309F赶快给我把\x01",
            "过去那种可以随便上网的\x01",
            "愉快生活夺回来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D04F")

    label("loc_CFEB")


    #C0357
    ChrTalk(
        0x9,
        (
            "#02300F好啦，总之你们就尽量努力吧。\x02\x03",

            "#02309F赶快给我把\x01",
            "过去那种可以随便上网的\x01",
            "愉快生活夺回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D04F")

    Jump("loc_D5F6")

    label("loc_D054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_D1E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D169")

    #C0358
    ChrTalk(
        0x9,
        (
            "#02301F那种无数光芒被吸入\x01",
            "树中的景象……\x01",
            "简直就像是导力网络的概念图呢。\x02\x03",

            "#02303F仔细想想，库罗伊斯家族的家伙\x01",
            "在这场阴谋中也利用到了导力网络。\x02\x03",

            "那棵『大树』的样子或许\x01",
            "与他们的『计划』存在着一定关联。\x02\x03",

            "#02302F……算了，这方面的分析\x01",
            "就交给你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D1DB")

    label("loc_D169")


    #C0359
    ChrTalk(
        0x9,
        (
            "#02303F那棵『大树』的样子\x01",
            "或许与他们的『计划』存在着一定关联。\x02\x03",

            "#02302F……算了，这方面的分析\x01",
            "就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1DB")

    Jump("loc_D5F6")

    label("loc_D1E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D2F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D28B")

    #C0360
    ChrTalk(
        0x9,
        (
            "#02303F虽然回到地下空间\x01",
            "的秘密基地也不错……\x02\x03",

            "#02302F但现在好像还是这边更有趣。\x01",
            "机会难得，我就陪你们\x01",
            "到最后好了。\x02\x03",

            "#02304F嘿嘿，感谢我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D2EB")

    label("loc_D28B")


    #C0361
    ChrTalk(
        0x9,
        (
            "#02302F现在好像还是这边更有趣。\x01",
            "机会难得，我就陪你们\x01",
            "到最后好了。\x02\x03",

            "#02304F嘿嘿，感谢我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2EB")

    Jump("loc_D5F6")

    label("loc_D2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D418")

    #C0362
    ChrTalk(
        0x9,
        (
            "#02302F对导力网络的入侵\x01",
            "比想象中还要顺利。\x02\x03",

            "#02306F但经由无线信号增幅器的线路\x01",
            "已经被彻底阻断了，\x01",
            "大概不可能再次使用了。\x02\x03",

            "#02309F……嘿嘿，算啦。\x01",
            "再怎么说，应该也都把兰花塔中的\x01",
            "那些家伙吓得惊慌失措了。\x02\x03",

            "#02302F接下来的目标就是\x01",
            "解放克洛斯贝尔市，\x01",
            "夺回我的秘密基地！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D490")

    label("loc_D418")


    #C0363
    ChrTalk(
        0x9,
        (
            "#02300F看样子，对手好像很强呢，\x01",
            "不过那些事情就全部交给你们了。\x02\x03",

            "#02309F赶快解放克洛斯贝尔市，\x01",
            "夺回我的秘密基地吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D490")

    Jump("loc_D5F6")

    label("loc_D495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_D5F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4B0")
    Call(1, 35)
    Jump("loc_D5F6")

    label("loc_D4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D57C")

    #C0364
    ChrTalk(
        0x9,
        (
            "#02306F那些家伙竟敢把我\x01",
            "关到连终端都没有的鬼地方，\x01",
            "我必须要彻底报仇。\x02\x03",

            "#02310F特别是那个什么玛丽亚贝尔！\x01",
            "一定得让那个恶魔知道我的厉害！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#00006F（似乎有很强烈的私人恩怨呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D5F6")

    label("loc_D57C")


    #C0366
    ChrTalk(
        0x9,
        (
            "#02302F我已经准备完毕了，\x01",
            "随时都可以开始网络入侵行动～！\x02\x03",

            "#02309F看着吧，克洛斯贝尔的所有终端\x01",
            "都会接收到无效宣言的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5F6")

    TalkEnd(0xFE)
    Return()

    # Function_34_CE14 end

    def Function_35_D5FA(): pass

    label("Function_35_D5FA")


    #C0367
    ChrTalk(
        0x9,
        (
            "#02305F嘿，作战还不开始吗？\x02\x03",

            "我都已经准备完毕了，\x01",
            "随时都可以开始网络入侵行动哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        "#00006F你好像非常开心得意啊……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x9,
        (
            "#02304F嘿嘿，那些可恶的家伙\x01",
            "竟敢把我关到连终端都没有的鬼地方，\x01",
            "这下终于可以报仇了。\x02\x03",

            "#02302F看着吧，我一定会把那个议长老伯\x01",
            "的影像和声音完美传送到\x01",
            "克洛斯贝尔的所有终端！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0370
    ChrTalk(
        0x101,
        (
            "#00003F是麦克道尔议长。\x02\x03",

            "#00001F约纳，\x01",
            "就算在特殊时期，\x01",
            "也必须要懂礼貌哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x9,
        (
            "#02306F啊啊，真是的，\x01",
            "你怎么还是和以前一样烦人。\x02\x03",

            "#02302F好了好了，\x01",
            "我们马上开始作战吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_35_D5FA end

    def Function_36_D7F2(): pass

    label("Function_36_D7F2")


    #C0372
    ChrTalk(
        0x9,
        (
            "#02300F不知为何，总有种\x01",
            "临近尾声的感觉呢。\x02\x03",

            "#02303F……那个……不要紧吧？\x01",
            "听说那个什么玛丽亚贝尔\x01",
            "在等着你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#00005F嘿，真是少见啊……\x01",
            "你是在为我们担心吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x9,
        (
            "#02305F这、这还用问吗！\x01",
            "在这么危险的状况下，\x01",
            "不管是谁都会担心吧！？\x02\x03",

            "#02306F啧，什么嘛，\x01",
            "难得人家担心你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，抱歉抱歉。\x02\x03",

            "#00000F……谢谢你了，约纳。\x01",
            "我们一定会平安归来的。\x02\x03",

            "拜托你认真做好准备工作，\x01",
            "保证我们随时可以飞向外面哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x9,
        (
            "#02303F哼，知道了。\x01",
            "总之你们就尽量努力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_36_D7F2 end

    def Function_37_D9CA(): pass

    label("Function_37_D9CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_D9DB")
    Jump("loc_DE2E")

    label("loc_D9DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_D9E9")
    Jump("loc_DE2E")

    label("loc_D9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D9F7")
    Jump("loc_DE2E")

    label("loc_D9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_DB43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DADD")

    #C0377
    ChrTalk(
        0xF,
        (
            "#02103F神秘结社『噬身之蛇』……\x01",
            "据说他们在利贝尔的\x01",
            "那场异变中也曾暗中活动。\x02\x03",

            "#02101F虽然在此次事件中，\x01",
            "他们没怎么出现在第一线，\x01",
            "不过还是负责驻守了重要的场所……\x02\x03",

            "#02106F……他们的目的究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_DB3E")

    label("loc_DADD")


    #C0378
    ChrTalk(
        0xF,
        (
            "#02103F神秘结社『噬身之蛇』……\x02\x03",

            "#02101F这个组织目前充满谜团，\x01",
            "他们的真实目的究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB3E")

    Jump("loc_DE2E")

    label("loc_DB43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_DCBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC22")

    #C0379
    ChrTalk(
        0xF,
        (
            "#02102F『独立无效宣言』的准备工作\x01",
            "总算是基本就绪了。\x02\x03",

            "麦克道尔议长已经\x01",
            "写好了演讲文稿，\x01",
            "接下来就只剩下正式发表了……\x02\x03",

            "#02106F……呜～不知为何，总觉得好紧张啊～！\x01",
            "不如去甲板上做做发声练习吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_DCB7")

    label("loc_DC22")


    #C0380
    ChrTalk(
        0xF,
        (
            "#02102F麦克道尔议长已经\x01",
            "写好了演讲文稿，\x01",
            "接下来就只剩下正式发表了……\x02\x03",

            "#02106F……呜～不知为何，总觉得好紧张啊～！\x01",
            "不如去甲板上做做发声练习吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCB7")

    Jump("loc_DE2E")

    label("loc_DCBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_DE2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCD7")
    Call(1, 38)
    Jump("loc_DE2E")

    label("loc_DCD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDE7")

    #C0381
    ChrTalk(
        0xF,
        (
            "#02109F那么～瓦吉，还有莉夏小姐，\x01",
            "就让我继续采访你们吧～！\x02\x03",

            "只是满足我个人的好奇心而已，\x01",
            "绝不会写成新闻报道，\x01",
            "请尽管放心，多透露一些秘密给我吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xD,
        "#10706F呼……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xA,
        (
            "#10409F哎呀呀，\x01",
            "格蕾丝小姐对八卦消息真热衷啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#00006F（不、不要紧吧……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_DE2E")

    label("loc_DDE7")


    #C0385
    ChrTalk(
        0xF,
        (
            "#02105F……嘿～这样吗～！\x02\x03",

            "#02109F嘿嘿～我就喜欢\x01",
            "这种内幕消息～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE2E")

    TalkEnd(0xFE)
    Return()

    # Function_37_D9CA end

    def Function_38_DE32(): pass

    label("Function_38_DE32")


    #C0386
    ChrTalk(
        0xF,
        (
            "#02104F竟然能在这么棒的\x01",
            "飞艇上进行如此\x01",
            "华丽的采访……\x02\x03",

            "#02109F啊啊，新闻工作者的热血\x01",
            "已经开始沸腾了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#00006F格、格蕾丝小姐……\x01",
            "您不会把这些都写进报道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xF,
        (
            "#02102F真是的，这还用问吗？\x01",
            "不必担心，只是满足我个人的好奇心而已。\x02\x03",

            "#02104F我还要继续整理和反抗军一起行动时\x01",
            "掌握到的消息，不会把这里的事情\x01",
            "写入报道的，你们尽管放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#00006F呼……\x02\x03",

            "#00005F……对了，格蕾丝小姐，\x01",
            "您是怎么与反抗军走到一起的……？\x02\x03",

            "#00003F您之前好像说起过，\x01",
            "在克洛斯贝尔市遇到了什么问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xF,
        (
            "#02106F嗯～该怎么说呢，\x01",
            "这说来就有些话长了……\x02\x03",

            "#02101F……其实，自从独立宣言正式发表的那一天开始，\x01",
            "我们写好的报道就都要\x01",
            "先交给政府来审阅了。\x02\x03",

            "包含批判总统等内容的\x01",
            "反对派采访报道\x01",
            "是绝对禁止撰写的……\x02\x03",

            "#02106F最后，甚至连\x01",
            "通讯器的使用和采访行为\x01",
            "都遭到了管制。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#00001F管制得真彻底啊……\x02\x03",

            "#00003F……唉，这种做法确实\x01",
            "很符合迪塔总统的作风呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xF,
        (
            "#02103F总之，那种现状已经完全偏离了\x01",
            "我所追求的新闻工作者之道，\x01",
            "实在让我无法接受。\x02\x03",

            "#02102F如果无视通告，继续我行我素地采访，\x01",
            "很快会被国防军盯上的。\x02\x03",

            "#02104F最后，我在克洛斯贝尔市实在是待不下去，\x01",
            "就跑到反抗军那边了。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#00000F原来是这样……\x01",
            "亏得你能平安无事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xF,
        (
            "#02109F这多亏雷因兹足智多谋，\x01",
            "帮我准备好了逃脱路线～\x01",
            "有个出色的后辈，真是幸运啊。\x02\x03",

            "#02100F……总之，\x01",
            "今后我会尽己所能，以我的方式\x01",
            "来协助大家解放克洛斯贝尔市！\x02\x03",

            "#02109F有句话是这样说的，『一支笔胜过百万兵』，\x01",
            "所以我绝对不会输给国防军或猎兵的！\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#00012F哈哈……说不定真的\x01",
            "需要您的协助呢，\x01",
            "到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 7)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_38_DE32 end

    def Function_39_E3C1(): pass

    label("Function_39_E3C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_E581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3DF")
    Call(1, 41)
    Jump("loc_E57C")

    label("loc_E3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4CC")

    #C0396
    ChrTalk(
        0x12,
        (
            "#02503F接下来，我恐怕就\x01",
            "帮不上你们什么忙了……\x02\x03",

            "#02500F但身为无效宣言的发表者，\x01",
            "我会继续思考宣言对克洛斯贝尔的未来\x01",
            "造成的影响，以及应对的策略。\x02\x03",

            "毕竟我不仅是自治州议会的议长……\x01",
            "更是居住在克洛斯贝尔\x01",
            "的一名市民啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_E57C")

    label("loc_E4CC")


    #C0397
    ChrTalk(
        0x12,
        (
            "#02503F身为无效宣言的发表者，\x01",
            "我会继续思考宣言对克洛斯贝尔的未来\x01",
            "造成的影响，以及应对的策略。\x02\x03",

            "#02500F毕竟我不仅是自治州议会的议长……\x01",
            "更是居住在克洛斯贝尔\x01",
            "的一名市民啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E57C")

    Jump("loc_E788")

    label("loc_E581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_E788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E59C")
    Call(1, 40)
    Jump("loc_E788")

    label("loc_E59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6E9")

    #C0398
    ChrTalk(
        0x12,
        (
            "#02500F我已经做好准备了，\x01",
            "随时都可以发表\x01",
            "『独立无效宣言』。\x02\x03",

            "#02503F接下来的问题就是……\x01",
            "如何才能把宣言传达到\x01",
            "克洛斯贝尔居民们的心中……\x02\x03",

            "#02500F虽然我并没有迪塔\x01",
            "那么出众的演说能力，\x01",
            "但一定会以自己的方式尽力将观点传达给大家的。\x02\x03",

            "为了让居住在克洛斯贝尔的每一个人\x01",
            "都能用心思考此地的未来，\x01",
            "我必须要顺利取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_E788")

    label("loc_E6E9")


    #C0399
    ChrTalk(
        0x12,
        (
            "#02503F『独立无效宣言』……\x01",
            "我一定会以自己的方式尽力完成演讲的。\x02\x03",

            "#02500F为了让居住在克洛斯贝尔的每一个人\x01",
            "都能用心思考此地的未来，\x01",
            "我必须要顺利取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E788")

    TalkEnd(0xFE)
    Return()

    # Function_39_E3C1 end

    def Function_40_E78C(): pass

    label("Function_40_E78C")


    #C0400
    ChrTalk(
        0x101,
        (
            "#00000F麦克道尔议长……\x01",
            "您已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x12,
        (
            "#02500F嗯，\x01",
            "我随时都可以发表\x01",
            "『独立无效宣言』。\x02\x03",

            "至于宣言内容，\x01",
            "我想也可以算是无懈可击。\x02\x03",

            "#02503F当然，其中也包括用迪塔\x01",
            "自己的言论来质问他这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#00003F……谢谢您。\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x12,
        (
            "#02503F哪里……不需要向我道谢。\x02\x03",

            "#02501F接下来的问题就是……\x01",
            "如何才能把宣言传达到\x01",
            "克洛斯贝尔居民们的心中……\x02\x03",

            "虽然我并没有迪塔\x01",
            "那么出众的演说能力，\x01",
            "但一定会努力将自己的每一句观点传达给大家。\x02\x03",

            "#02503F为了让居住在克洛斯贝尔的每一个人\x01",
            "都能用心思考此地的未来，\x01",
            "我必须要顺利取得成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        "#00000F嗯……拜托您了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 1)
    Return()

    # Function_40_E78C end

    def Function_41_E9AB(): pass

    label("Function_41_E9AB")


    #C0405
    ChrTalk(
        0x12,
        "#02503F………………………………\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        "#00005F麦克道尔议长……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x101, 0)
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EA95")
    Jump("loc_EADF")

    label("loc_EA95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EAB5")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EADF")

    label("loc_EAB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAD5")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EADF")

    label("loc_EAD5")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EADF")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    #C0407
    ChrTalk(
        0x12,
        (
            "#02505F……哦，抱歉，\x01",
            "我正在思考一些问题。\x02\x03",

            "#02503F克洛斯贝尔独立无效宣言……\x01",
            "虽说是为了打破现状，\x01",
            "但这样做真的正确吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#00008F…………………………\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x12,
        (
            "#02503F……这个问题，\x01",
            "恐怕并没有一个正确的答案。\x02\x03",

            "#02500F但我认为，努力追寻正确的答案\x01",
            "才是最重要的。\x02\x03",

            "毕竟我不仅是自治州议会的议长……\x01",
            "更是居住在克洛斯贝尔\x01",
            "的一名市民啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#00003F……谢谢您。\x02\x03",

            "#00000F等这次的事件告一段落之后，\x01",
            "我们也一定会去\x01",
            "给您帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x12,
        (
            "#02509F呵呵，那可太好了，\x01",
            "到时候就拜托你们啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1DA, 2)
    Return()

    # Function_41_E9AB end

    def Function_42_ECEB(): pass

    label("Function_42_ECEB")

    Call(1, 43)
    Return()

    # Function_42_ECEB end

    def Function_43_ECEF(): pass

    label("Function_43_ECEF")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ECFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB11")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "购买装备\x01",        # 1
            "购买消耗品\x01",      # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED5B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_ED5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ED7A")
    OP_AF(0xD8)
    Jump("loc_EDCC")

    label("loc_ED7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_ED8A")
    OP_AF(0xD7)
    Jump("loc_EDCC")

    label("loc_ED8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_ED9A")
    OP_AF(0xD6)
    Jump("loc_EDCC")

    label("loc_ED9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_EDAA")
    OP_AF(0xD5)
    Jump("loc_EDCC")

    label("loc_EDAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_EDBA")
    OP_AF(0xD4)
    Jump("loc_EDCC")

    label("loc_EDBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_EDCA")
    OP_AF(0xD3)
    Jump("loc_EDCC")

    label("loc_EDCA")

    OP_AF(0xD2)

    label("loc_EDCC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB0C")

    label("loc_EDDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDFB")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB0C")

    label("loc_EDFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE0F")
    Jump("loc_FB0C")

    label("loc_EE0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB0C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_EF96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF2F")

    #C0412
    ChrTalk(
        0x15,
        (
            "围绕着克洛斯贝尔的命运而展开的战斗\x01",
            "终于迎来了对决的时刻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x15,
        (
            "一开始，由于教会的人员没有汇集，\x01",
            "还不知道事情将会变成怎样……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x15,
        (
            "但最终总算是走到了这一步。\x01",
            "你们一定没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x15,
        (
            "好了，为了迎接最后的战斗，\x01",
            "请做好充足的准备吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_EF91")

    label("loc_EF2F")


    #C0416
    ChrTalk(
        0x15,
        (
            "都已经走到这一步了，\x01",
            "你们一定没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x15,
        (
            "好了，为了迎接最后的战斗，\x01",
            "请做好充足的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF91")

    Jump("loc_FB0C")

    label("loc_EF96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_F0AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F044")

    #C0418
    ChrTalk(
        0x15,
        (
            "『大树』的道路似乎\x01",
            "一直通到很深的场所……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x15,
        (
            "如果遇到危险，经常回来补给\x01",
            "也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x15,
        (
            "事件能否解决，全看你们的了。\x01",
            "一定要慎重前进啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F0A8")

    label("loc_F044")


    #C0421
    ChrTalk(
        0x15,
        (
            "如果遇到危险，经常回来补给\x01",
            "也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x15,
        (
            "事件能否解决，全看你们的了。\x01",
            "一定要慎重前进啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0A8")

    Jump("loc_FB0C")

    label("loc_F0AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F22B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19F")

    #C0423
    ChrTalk(
        0x15,
        (
            "本想在前往『大树』之前\x01",
            "做足各方面的准备，\x01",
            "但这里能收集到的东西也是有限的。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x15,
        (
            "先降落在克洛斯贝尔各地，\x01",
            "去各个设施拜访，与亲友们打个招呼\x01",
            "也是不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x15,
        (
            "还不知道将会发生什么事……\x01",
            "不要给自己留下遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F226")

    label("loc_F19F")


    #C0426
    ChrTalk(
        0x15,
        (
            "先降落在克洛斯贝尔各地，\x01",
            "去各个设施拜访，与亲友们打个招呼\x01",
            "也是不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x15,
        (
            "还不知道将会发生什么事……\x01",
            "不要给自己留下遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F226")

    Jump("loc_FB0C")

    label("loc_F22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_F37F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2FB")

    #C0428
    ChrTalk(
        0x15,
        (
            "约鲁古·罗赞贝尔克……\x01",
            "『结社』的人竟然向我们提供了\x01",
            "很有用的情报啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x15,
        (
            "身为星杯骑士，\x01",
            "不知是否应该轻易信之，\x01",
            "但那些情报似乎并不假。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x15,
        (
            "看来结社中也有着\x01",
            "各种不同的人呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F37A")

    label("loc_F2FB")


    #C0431
    ChrTalk(
        0x15,
        (
            "约鲁古·罗赞贝尔克……\x01",
            "不知是否应该轻易相信他提供的情报，\x01",
            "但那些情报似乎并不假。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x15,
        (
            "看来结社中也有着\x01",
            "各种不同的人呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F37A")

    Jump("loc_FB0C")

    label("loc_F37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_F4A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F433")

    #C0433
    ChrTalk(
        0x15,
        (
            "麦克道尔议长发表\x01",
            "独立无效宣言之后，\x01",
            "一定能对克洛斯贝尔各地造成影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x15,
        (
            "潜伏在各地的反抗军\x01",
            "大概也会更易于行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x15,
        "……感觉快要迎来高潮了呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F49D")

    label("loc_F433")


    #C0436
    ChrTalk(
        0x15,
        (
            "麦克道尔议长发表\x01",
            "独立无效宣言之后，\x01",
            "一定能对克洛斯贝尔各地造成影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x15,
        "……感觉快要迎来高潮了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_F49D")

    Jump("loc_FB0C")

    label("loc_F4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_F5E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F572")

    #C0438
    ChrTalk(
        0x15,
        (
            "救出麦克道尔议长的作战……\x01",
            "虽然我并不会出击，\x01",
            "但还是非常紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x15,
        (
            "对手是『赤色星座』的一个中队……\x01",
            "想必会有前所未有的严酷战斗\x01",
            "在等待着你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x15,
        (
            "请大家一定要\x01",
            "平安归来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F5E1")

    label("loc_F572")


    #C0441
    ChrTalk(
        0x15,
        (
            "对手是『赤色星座』的一个中队……\x01",
            "想必会有前所未有的严酷战斗\x01",
            "在等待着你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x15,
        (
            "请大家一定要\x01",
            "平安归来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5E1")

    Jump("loc_FB0C")

    label("loc_F5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_F73B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6B7")

    #C0443
    ChrTalk(
        0x15,
        (
            "梅尔卡瓦的内部\x01",
            "变得热闹多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x15,
        (
            "平时只有骑士团的人员才能进入，\x01",
            "普通民间人士进入这里，\x01",
            "本身就是件很稀奇的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x15,
        (
            "其实我觉得这样也不错呢……\x01",
            "当然，这种话只能在这里说说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F736")

    label("loc_F6B7")


    #C0446
    ChrTalk(
        0x15,
        (
            "普通民间人士进入\x01",
            "梅尔卡瓦的内部，\x01",
            "本身就是件很稀奇的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x15,
        (
            "其实我觉得这样也不错呢……\x01",
            "当然，这种话只能在这里说说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F736")

    Jump("loc_FB0C")

    label("loc_F73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_F87F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F81B")

    #C0448
    ChrTalk(
        0x15,
        (
            "传说中的杀手『银』……\x01",
            "我也听说过相关的传闻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x15,
        (
            "但真没想到，\x01",
            "竟然会是那样的少女……\x01",
            "世间事，真是很难理解呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x15,
        (
            "……不过，你们在得知\x01",
            "赫米斯菲亚大人是神职人员时，\x01",
            "应该也感到相当震惊吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F87A")

    label("loc_F81B")


    #C0451
    ChrTalk(
        0x15,
        (
            "传说中的杀手『银』……\x01",
            "没想到竟然会是那样的少女啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x15,
        "哈哈，世间事，真是很难理解呢。\x02",
    )

    CloseMessageWindow()

    label("loc_F87A")

    Jump("loc_FB0C")

    label("loc_F87F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_F99E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F907")

    #C0453
    ChrTalk(
        0x15,
        (
            "与同伴会合了吗……\x01",
            "开端似乎还算顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x15,
        (
            "但即使如此，也该\x01",
            "事先做好各种准备。\x01",
            "今后也要继续保持警惕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F999")

    label("loc_F907")


    #C0455
    ChrTalk(
        0x15,
        (
            "凭借赫米斯菲亚大人的法术，\x01",
            "短时间内应该可以自由出入医院，\x01",
            "不会遭遇到国防军。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x15,
        (
            "虽说开端还算顺利，\x01",
            "但仍然不能大意，\x01",
            "今后还要继续保持警惕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F999")

    Jump("loc_FB0C")

    label("loc_F99E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_FB0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9B9")
    Call(1, 44)
    Jump("loc_FB0C")

    label("loc_F9B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA95")

    #C0457
    ChrTalk(
        0x15,
        (
            "总之，这里储备了\x01",
            "大量的装备与物资，\x01",
            "有需要时就尽管来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x15,
        (
            "……呼，话说回来，\x01",
            "从以前开始就经常被\x01",
            "赫米斯菲亚大人折腾得手忙脚乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x15,
        (
            "我们不在的时候，\x01",
            "阿巴斯先生一直陪伴\x01",
            "在他身边，真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_FB0C")

    label("loc_FA95")


    #C0460
    ChrTalk(
        0x15,
        (
            "从以前开始就经常被\x01",
            "赫米斯菲亚大人折腾得手忙脚乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x15,
        (
            "我们不在的时候，\x01",
            "阿巴斯先生一直陪伴\x01",
            "在他身边，真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB0C")

    Jump("loc_ECFC")

    label("loc_FB11")

    TalkEnd(0x15)
    Return()

    # Function_43_ECEF end

    def Function_44_FB15(): pass

    label("Function_44_FB15")


    #C0462
    ChrTalk(
        0x15,
        (
            "我是随从骑士维恩图斯，\x01",
            "全权负责管理\x01",
            "舰内的设备。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x15,
        (
            "在作战开始前，已经准备了\x01",
            "大量的装备与物资，\x01",
            "有需要时就尽管来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#00005F全权负责……\x01",
            "在人手不足的情况下，\x01",
            "这肯定很辛苦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x15,
        (
            "嗯，因为赫米斯菲亚大人\x01",
            "突然以骑士身份展开行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x15,
        (
            "舰内仅凑够了\x01",
            "最低限度的人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x15, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FCBD")
    Jump("loc_FD07")

    label("loc_FCBD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FCDD")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD07")

    label("loc_FCDD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FCFD")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD07")

    label("loc_FCFD")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD07")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    #C0467
    ChrTalk(
        0xA,
        (
            "#10404F呵呵，没办法，\x01",
            "毕竟事态紧急嘛。\x02\x03",

            "#10409F与维恩图斯和大家已经两年不见了，\x01",
            "短时间内又得请你们多关照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x15,
        "……呼，总之，必须要努力了。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        (
            "#00006F（嗯，看来的确是\x01",
            "  十分操劳呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x1DA, 3)
    Return()

    # Function_44_FB15 end

    def Function_45_FDFA(): pass

    label("Function_45_FDFA")

    Call(1, 46)
    Return()

    # Function_45_FDFA end

    def Function_46_FDFE(): pass

    label("Function_46_FDFE")

    TalkBegin(0x16)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A9C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "改造·合成\x01",      # 1
            "放弃\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE61")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_FE61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE81")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A97")

    label("loc_FE81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE95")
    Jump("loc_10A97")

    label("loc_FE95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A97")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_FFF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF75")

    #C0470
    ChrTalk(
        0x16,
        (
            "既然都走到了这一步，\x01",
            "我便已经没什么可说的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x16,
        (
            "虽然挡在前方的敌人十分强大，\x01",
            "但空之女神一定会为\x01",
            "大家指引前进的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x16,
        (
            "请大家一定要多加小心，\x01",
            "愿女神保佑各位……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_FFEE")

    label("loc_FF75")


    #C0473
    ChrTalk(
        0x16,
        (
            "虽然挡在前方的敌人十分强大，\x01",
            "但空之女神一定会为\x01",
            "大家指引前进的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x16,
        (
            "请大家一定要多加小心，\x01",
            "愿女神保佑各位……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFEE")

    Jump("loc_10A97")

    label("loc_FFF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_1015B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100D6")

    #C0475
    ChrTalk(
        0x16,
        (
            "『零之至宝』……\x01",
            "竟能创造出那样的空间，\x01",
            "简直就是女神般的神力。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x16,
        (
            "……已经与各位同行到了这一步，\x01",
            "这艘舰艇的命运\x01",
            "就交给大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x16,
        (
            "我虽然帮不上什么大忙，\x01",
            "但如果要调整导力器，\x01",
            "随时可以来找我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_10156")

    label("loc_100D6")


    #C0478
    ChrTalk(
        0x16,
        (
            "已经与各位同行到了这一步，\x01",
            "这艘舰艇的命运\x01",
            "就交给大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x16,
        (
            "我虽然帮不上什么大忙，\x01",
            "但如果要调整导力器，\x01",
            "随时可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10156")

    Jump("loc_10A97")

    label("loc_1015B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101F1")

    #C0480
    ChrTalk(
        0x16,
        (
            "……舰内的紧张感\x01",
            "似乎比解放克洛斯贝尔市\x01",
            "作战时更加强烈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x16,
        (
            "最终阶段总算要到来了……\x01",
            "现在也只能祈祷女神的保佑了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_1022C")

    label("loc_101F1")


    #C0482
    ChrTalk(
        0x16,
        (
            "最终阶段总算要到来了……\x01",
            "现在也只能祈祷女神的保佑了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1022C")

    Jump("loc_10A97")

    label("loc_10231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_103BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10326")

    #C0483
    ChrTalk(
        0x16,
        (
            "受无效宣言的影响，\x01",
            "现在已经与位于克洛斯贝尔\x01",
            "外的五号机恢复联络了。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x16,
        (
            "为了解放克洛斯贝尔市，\x01",
            "格拉汉姆大人他们似乎\x01",
            "也在进行各种准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x16,
        (
            "为了能得到他们的协助，\x01",
            "无论如何也要想办法解决\x01",
            "白色『神机』与『结界』啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_103B8")

    label("loc_10326")


    #C0486
    ChrTalk(
        0x16,
        (
            "为了解放克洛斯贝尔市，\x01",
            "格拉汉姆大人他们似乎\x01",
            "也在进行各种准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x16,
        (
            "为了能得到他们的协助，\x01",
            "无论如何也要想办法解决\x01",
            "白色『神机』与『结界』啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103B8")

    Jump("loc_10A97")

    label("loc_103BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_10501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10483")

    #C0488
    ChrTalk(
        0x16,
        (
            "入侵导力网络时，\x01",
            "我也会通过那台终端\x01",
            "来帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        (
            "导力网络并非我的专长，\x01",
            "我只能负责操纵\x01",
            "梅尔卡瓦的系统……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x16,
        (
            "但为了履行骑士团成员的使命，\x01",
            "我一定会竭尽自己的全力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_104FC")

    label("loc_10483")


    #C0491
    ChrTalk(
        0x16,
        (
            "导力网络并非我的专长，\x01",
            "我只能负责操纵\x01",
            "梅尔卡瓦的系统……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x16,
        (
            "但为了履行骑士团成员的使命，\x01",
            "我一定会竭尽自己的全力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104FC")

    Jump("loc_10A97")

    label("loc_10501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1062B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105A5")

    #C0493
    ChrTalk(
        0x16,
        (
            "国防军的部队似乎\x01",
            "并没有驻守在米修拉姆……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x16,
        (
            "但就算只有那些猎兵，\x01",
            "也一样是非常危险的。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "导力器方面的准备工作\x01",
            "一定要仔细做好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_10626")

    label("loc_105A5")


    #C0496
    ChrTalk(
        0x16,
        (
            "虽然国防军的部队并没有\x01",
            "驻守在米修拉姆，但就算只有\x01",
            "那些猎兵，也一样是非常危险的。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x16,
        (
            "导力器方面的准备工作\x01",
            "一定要仔细做好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10626")

    Jump("loc_10A97")

    label("loc_1062B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1077E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10709")

    #C0498
    ChrTalk(
        0x16,
        (
            "兰迪先生那把名为\x01",
            "『狂战士』的来复枪……\x01",
            "似乎拥有相当强的火力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x16,
        (
            "与大陆最强的猎兵团之一\x01",
            "『赤色星座』为敌，\x01",
            "战斗想必会相当严酷……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x16,
        (
            "但兰迪先生拥有那种武器，\x01",
            "难怪可以和他们一较高下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_10779")

    label("loc_10709")


    #C0501
    ChrTalk(
        0x16,
        (
            "兰迪先生那把名为\x01",
            "『狂战士』的来复枪……\x01",
            "似乎拥有相当强的火力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x16,
        (
            "难怪他\x01",
            "可以和『赤色星座』\x01",
            "一较高下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10779")

    Jump("loc_10A97")

    label("loc_1077E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_108D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1085F")

    #C0503
    ChrTalk(
        0x16,
        (
            "与国防军这种巨大组织为敌，\x01",
            "展开抵抗活动，\x01",
            "需要相当强的信念。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "不但得不到充分的补给，\x01",
            "而且怎么说也是\x01",
            "背叛昔日同伴的行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x16,
        (
            "虽然不知道他们\x01",
            "的首领是谁，但显然是个\x01",
            "内心坚定，很有骨气的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_108D2")

    label("loc_1085F")


    #C0506
    ChrTalk(
        0x16,
        (
            "向国防军发起抵抗行动\x01",
            "需要相当强的信念。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "虽然不知道反抗军\x01",
            "的首领是谁，但显然是个\x01",
            "内心坚定，很有骨气的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108D2")

    Jump("loc_10A97")

    label("loc_108D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_10A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109DD")

    #C0508
    ChrTalk(
        0x16,
        (
            "无论发生什么事，\x01",
            "也请不要进入\x01",
            "那里的机关室。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x16,
        (
            "因为里面有一些不能被\x01",
            "普通民间人士看到的重要之物。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_END)), "loc_109B2")

    #C0510
    ChrTalk(
        0x101,
        (
            "#00005F（莫非是阿巴斯\x01",
            "  刚才提到的那个名为\x01",
            "  『天之车』的古代遗物吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109D5")

    label("loc_109B2")


    #C0511
    ChrTalk(
        0x101,
        "#00005F（究竟有什么呢……？）\x02",
    )

    CloseMessageWindow()

    label("loc_109D5")

    SetScenarioFlags(0x2, 2)
    Jump("loc_10A1D")

    label("loc_109DD")


    #C0512
    ChrTalk(
        0x16,
        (
            "差不多也该去\x01",
            "机关室内部\x01",
            "做维护了。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x16,
        "……请不要偷看哦。\x02",
    )

    CloseMessageWindow()

    label("loc_10A1D")

    Jump("loc_10A97")

    label("loc_10A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_10A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A3D")
    Call(1, 47)
    Jump("loc_10A97")

    label("loc_10A3D")


    #C0514
    ChrTalk(
        0x16,
        (
            "……既然结社已经出动，\x01",
            "骑士团自然也不能\x01",
            "对这次的事件坐视不理。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x16,
        "我们一起加油吧。\x02",
    )

    CloseMessageWindow()

    label("loc_10A97")

    Jump("loc_FE0B")

    label("loc_10A9C")

    TalkEnd(0x16)
    Return()

    # Function_46_FDFE end

    def Function_47_10AA0(): pass

    label("Function_47_10AA0")


    #C0516
    ChrTalk(
        0x16,
        (
            "你就是克洛斯贝尔警察局\x01",
            "特别任务支援科的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x16,
        (
            "我是负责管理\x01",
            "这个机关区域的\x01",
            "朱诺。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x16,
        (
            "结晶回路的合成，\x01",
            "以及战术导力器的改造工作\x01",
            "都可以交给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x101,
        (
            "#00005F哎……原来随从骑士\x01",
            "还掌握这些技术吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x16,
        (
            "呵呵，我只是特例而已。\x01",
            "对这种精巧的手工活，\x01",
            "我还是比较有自信的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0521
    ChrTalk(
        0x16,
        (
            "……既然结社已经出动，\x01",
            "骑士团自然也不能\x01",
            "对这次的事件坐视不理。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x16,
        "我们一起加油吧。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        "#00000F嗯……请多指教。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 4)
    Return()

    # Function_47_10AA0 end

    def Function_48_10C44(): pass

    label("Function_48_10C44")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K 休息室\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "休息\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D8C")
    EventBegin(0x2)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    OP_0D()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_10CF7():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10CF7)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFF, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    OP_70(0x3, 0x0)
    OP_68(1300, 1000, -92030, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 270)
    SetChrSubChip(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x3)

    label("loc_10D8C")

    TalkEnd(0xFF)
    Return()

    # Function_48_10C44 end

    def Function_49_10D90(): pass

    label("Function_49_10D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DA6")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_10DA6")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10DBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11259")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_10DF8"),
        (1, "loc_10E27"),
        (2, "loc_1123D"),
        (3, "loc_11245"),
        (SWITCH_DEFAULT, "loc_11254"),
    )


    label("loc_10DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10E17")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_10E22")

    label("loc_10E17")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_10E22")

    Jump("loc_11254")

    label("loc_10E27")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EDA")
    SetChrName("自动语音")

    #A0525
    AnonymousTalk(
        0xFF,
        "这里是克洛斯贝尔警察局，\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_10EBB")

    #A0526
    AnonymousTalk(
        0xFF,
        "已经接到您的报告。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自动语音")

    #A0527
    AnonymousTalk(
        0xFF,
        (
            "报告处理完毕，\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10ED5")

    label("loc_10EBB")


    #A0528
    AnonymousTalk(
        0xFF,
        "没有可以报告的委托。\x02",
    )

    CloseMessageWindow()

    label("loc_10ED5")

    Jump("loc_1122F")

    label("loc_10EDA")

    SetChrName("接待小姐芙兰")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10F2C")
    Sound(3062, 255, 100, 0)    #voice#Fran

    #A0529
    AnonymousTalk(
        0xFF,
        "#26A您好，这里是克洛斯贝尔警察局～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_10F44")

    label("loc_10F2C")

    Sound(3061, 255, 100, 0)    #voice#Fran

    #A0530
    AnonymousTalk(
        0xFF,
        "#29A各位辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_10F44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_11167")
    Sound(3067, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0531
    AnonymousTalk(
        0xFF,
        "#27A已经收到大家的报告～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110F4")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_10FAD"),
        (13, "loc_10FF5"),
        (12, "loc_11039"),
        (SWITCH_DEFAULT, "loc_1107F"),
    )


    label("loc_10FAD")

    Sound(3075, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0532
    AnonymousTalk(
        0xFF,
        (
            "#39A级别１ｓｔ——\x01",
            "罗伊德警官，实在太厉害了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1107F")

    label("loc_10FF5")

    Sound(3074, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0533
    AnonymousTalk(
        0xFF,
        (
            "#38A级别２ｎｄ──\x01",
            "罗伊德警官，好厉害呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1107F")

    label("loc_11039")

    Sound(3073, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0534
    AnonymousTalk(
        0xFF,
        (
            "#33A级别３ｒｄ──\x01",
            "罗伊德警官，做得很好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1107F")

    label("loc_1107F")

    Sound(3076, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0535
    AnonymousTalk(
        0xFF,
        (
            "#33A马上就会把奖励物品\x01",
            "给你们送去的～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)    #voice#Fran

    #A0536
    AnonymousTalk(
        0xFF,
        (
            "#33A大家辛苦了～！\x01",
            "以后也请随时来向我报告～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115F")

    label("loc_110F4")

    Sound(3078, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0537
    AnonymousTalk(
        0xFF,
        "#17A报告就是以上这些吧～\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)    #voice#Fran

    #A0538
    AnonymousTalk(
        0xFF,
        (
            "#38A那么，以后如果完成了新的委托，\x01",
            "请再来向我报告吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1115F")

    SetScenarioFlags(0x2, 4)
    Jump("loc_1122F")

    label("loc_11167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_111D6")
    Sound(3063, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0539
    AnonymousTalk(
        0xFF,
        (
            "#31A哎……\x01",
            "不是刚刚才报告过吗？\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)    #voice#Fran

    #A0540
    AnonymousTalk(
        0xFF,
        "#35A等完成了新的委托之后再来报告吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1122F")

    label("loc_111D6")

    Sound(3065, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            "#38A哎，好像并没有可以\x01",
            "报告的委托啊～\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)    #voice#Fran

    #A0542
    AnonymousTalk(
        0xFF,
        "#20A请下次再来报告吧～\x02",
    )

    CloseMessageWindow()

    label("loc_1122F")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_11254")

    label("loc_1123D")

    Call(1, 50)
    Jump("loc_11254")

    label("loc_11245")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11254")

    label("loc_11254")

    Jump("loc_10DBF")

    label("loc_11259")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11296")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(1, 51)
    Return()

    label("loc_11296")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_49_10D90 end

    def Function_50_112A6(): pass

    label("Function_50_112A6")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_112C8")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_112C8")
    ClearScenarioFlags(0x2A, 0)

    label("loc_112C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_112E5")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_112E5")
    ClearScenarioFlags(0x2A, 1)

    label("loc_112E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_11302")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11302")
    ClearScenarioFlags(0x2A, 2)

    label("loc_11302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_1131F")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1131F")
    ClearScenarioFlags(0x2A, 3)

    label("loc_1131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_1133C")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1133C")
    ClearScenarioFlags(0x2A, 4)

    label("loc_1133C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_11359")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11359")
    ClearScenarioFlags(0x2A, 5)

    label("loc_11359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_11365")
    SetScenarioFlags(0x2A, 6)

    label("loc_11365")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113AA")
    Sound(498, 1, 50, 0)
    Jump("loc_113B0")

    label("loc_113AA")

    Sound(498, 1, 100, 0)

    label("loc_113B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_113E0")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_113E0")

    Return()

    # Function_50_112A6 end

    def Function_51_113E1(): pass

    label("Function_51_113E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_1144A")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_1144A")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0543
    ChrTalk(
        0xB,
        (
            "#00205F啊……\x02\x03",

            "#00204F看样子，罗伊德前辈\x01",
            "已经在『波波碰！』游戏中\x01",
            "战胜过所有对手了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xC,
        (
            "#01905F哎哎，真的吗～！？\x02\x03",

            "#01909F真不愧是罗伊德警官……\x01",
            "实在太厉害了～！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_115A6")

    #C0545
    ChrTalk(
        0x9,
        (
            "#02302F嘿，的确，\x01",
            "你也挺有一套的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115A6")

    SetChrSubChip(0x101, 0x1)

    #C0546
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢，\x01",
            "其实只是运气好而已啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x8,
        (
            "#12100F不，在这种脑力游戏中，\x01",
            "光靠运气是无法取得胜利的。\x02\x03",

            "#12102F班宁斯，你才是真正的\x01",
            "『波波碰大师』。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        "#00012F……这、这真是过奖了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('贤者', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117E5")

    #C0549
    ChrTalk(
        0x8,
        (
            "#12100F哦，对了……\x02\x03",

            "如果不介意，就收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0550
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('贤者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0551
    ChrTalk(
        0x8,
        (
            "#12100F这是教会与爱普斯泰恩财团\x01",
            "以古代秘术为基础，\x01",
            "共同开发的禁忌核心回路。\x02\x03",

            "由于性能过强，很难操控，\x01",
            "所以一直没有正式投入运用……\x02\x03",

            "#12102F不过，你应该有能力控制它。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x101,
        (
            "#00000F嗯，明白了，\x01",
            "我一定会让它发挥作用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118AD")

    label("loc_117E5")


    #C0553
    ChrTalk(
        0x8,
        (
            "#12100F哦，对了……\x02\x03",

            "#12102F作为奖励，把这个给你吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0554
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('水耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    #C0555
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，谢谢，\x01",
            "我一定会让它派上用场的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_118AD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_113E1 end

    def Function_52_118DF(): pass

    label("Function_52_118DF")

    EventBegin(0x0)
    Fade(500)
    OP_68(4130, -1100, 7060, 0)
    MoveCamera(47, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14590, 0)
    SetChrPos(0x101, 4000, -1500, 5730, 315)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_119B6")
    Jump("loc_11A00")

    label("loc_119B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_119D6")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11A00")

    label("loc_119D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_119F6")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11A00")

    label("loc_119F6")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A00")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    OP_0D()

    #C0556
    ChrTalk(
        0xC,
        (
            "#6P#01905F罗伊德警官……\x01",
            "你好像很累了呢。\x02\x03",

            "没关系吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x101,
        (
            "#11P#00005F没关系的，不过听你这么一说……\x02\x03",

            "#00003F经历了这么多的事情，\x01",
            "似乎是有些累呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xC,
        (
            "#6P#01906F嗯，请一定不要\x01",
            "太勉强自己哦～\x02\x03",

            "#01908F每当想到罗伊德警官、姐姐\x01",
            "和大家倒下的情景……\x01",
            "我就会非常担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#11P#00000F哈哈，谢谢，\x01",
            "我一定会多加小心的……\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xC,
        (
            "#6P#01901F光是小心可不行哦～！\x01",
            "在这种时候，必须要好好休息！\x02\x03",

            "#01902F不然……就让我给你\x01",
            "按摩一下如何？\x02\x03",

            "#01909F只要对准穴位狠狠按下去，\x01",
            "一下就能恢复精力了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#11P#00006F（听、听起来好像会很疼……）\x02\x03",

            "#00002F那、那个……\x01",
            "你的好意我还是心领了。\x02\x03",

            "#00009F光是和你聊几句，\x01",
            "就感觉已经恢复精神了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xC,
        (
            "#6P#01905F哎……是、是吗～？\x02\x03",

            "#01909F嘿嘿嘿……\x01",
            "听你这么说，真是好开心～\x02\x03",

            "#01904F身为大家的联络员，\x01",
            "让大家振作精神\x01",
            "是我的使命。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x101,
        (
            "#11P#00009F哈哈，如此说来，\x01",
            "你真的很有这方面的天赋呢。\x02\x03",

            "#00004F每当在终端上看到你的笑脸时，\x01",
            "都会有种精神大振的感觉……\x02\x03",

            "#00000F在那些出入警察总部的人之中，\x01",
            "肯定也有不少人是专门为了看你而去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xC,
        (
            "#6P#01906F唔唔……你说得这么夸张，\x01",
            "我还真有点不好意思呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0565
    ChrTalk(
        0xC,
        (
            "#6P#01904F对了～\x01",
            "如果不介意，\x01",
            "可以收下这个吗？\x02\x03",

            "#01902F希望罗伊德警官\x01",
            "今后也继续加油～\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0566
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('芙兰的护符', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0567
    ChrTalk(
        0x101,
        "#11P#00005F这个……我可以收下吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_12080")

    #C0568
    ChrTalk(
        0xC,
        (
            "#6P#01909F嗯，请一定\x01",
            "要收下。\x02\x03",

            "#01904F毕竟罗伊德警官\x01",
            "将来有可能会\x01",
            "成为我的姐夫……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0569
    ChrTalk(
        0x101,
        "#11P#00011F哎……什么！？\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xC,
        (
            "#6P#01909F呵呵呵……\x01",
            "只要是和姐姐有关的事情，\x01",
            "我全都了解得一清二楚哟～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0571
    ChrTalk(
        0x101,
        (
            "#11P#00012F（哈、哈哈……真是服了她。\x01",
            "  到底还是被看穿了啊……）\x02\x03",

            "#00000F……嗯，既然如此，\x01",
            "那我就不客气地收下啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1210F")

    label("loc_12080")


    #C0572
    ChrTalk(
        0xC,
        (
            "#6P#01909F嗯，请一定\x01",
            "要收下。\x02\x03",

            "那是我为了祈祷大家平安无事，\x01",
            "用心制作出来的，\x01",
            "一定效果拔群！\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x101,
        (
            "#11P#00009F哈哈，那我一定会\x01",
            "好好使用的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1210F")


    #C0574
    ChrTalk(
        0xC,
        "#6P#01909F嘿嘿，请仔细保存好哦～\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D9, 4)
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1215C")
    OP_E0(0x34, 0x0)

    label("loc_1215C")

    EventEnd(0x5)
    Return()

    # Function_52_118DF end

    def Function_53_1215F(): pass

    label("Function_53_1215F")

    EventBegin(0x0)
    Fade(500)
    OP_68(97920, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15320, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12236")
    Jump("loc_12280")

    label("loc_12236")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12256")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12280")

    label("loc_12256")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12276")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12280")

    label("loc_12276")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12280")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)
    OP_0D()

    #C0575
    ChrTalk(
        0x14,
        (
            "#5P#00603F嗯……\x02\x03",

            "#00600F……班宁斯，\x01",
            "你似乎也有了一定的成长啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0576
    ChrTalk(
        0x101,
        "#12P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x14,
        (
            "#5P#00603F通过这段时间与你们的同行，\x01",
            "我颇有感触……\x02\x03",

            "调查与推理的能力自然不容置疑，\x01",
            "以前的那种天真和幼稚，\x01",
            "如今似乎也完全消失了。\x02\x03",

            "虽然与警察时代的盖伊或马克莱因相比，\x01",
            "仍然还有一定差距……\x02\x03",

            "#00602F不过……哼，看来你在搜查一科\x01",
            "的学习并没有白费呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0578
    ChrTalk(
        0x101,
        (
            "#12P#00012F那、那个……\x01",
            "突然说这些，到底是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x14,
        "#5P#00603F别插嘴，安静听我说。\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x101,
        "#12P#00006F是、是。\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x14,
        (
            "#5P#00600F……虽然我刚刚提到了\x01",
            "盖伊和马克莱因，但并不是希望你\x01",
            "成为他们那种类型的搜查官。\x02\x03",

            "你拥有自己独有的素质。\x01",
            "只要继续发挥那些优点，\x01",
            "就一定可以成为一名优秀的搜查官。\x02\x03",

            "#00604F以自己心中的完美搜查官为目标，\x01",
            "继续努力提高吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0582
    ChrTalk(
        0x14,
        "#5P#00605F……怎么，你有什么不满吗？\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#12P#00011F怎、怎么会……\x01",
            "只是有些吃惊而已。\x02\x03",

            "#00006F竟然会给我这样直接的好评，\x01",
            "完全不像达德利警官的一贯风格呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x14,
        (
            "#5P#00603F……国防军最终将会如何，\x01",
            "还要看今后的动向，\x01",
            "但警察组织肯定会继续存在。\x02\x03",

            "#00600F将这一连串的事件平息下来之后，\x01",
            "你自然要\x01",
            "回归警察局。\x02\x03",

            "为了那种状况，\x01",
            "我才会以一科主任搜查官的身份，\x01",
            "提前向你提出一些建议。\x02\x03",

            "#00603F仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#12P#00000F是吗……\x02\x03",

            "#00004F……谢谢。\x02\x03",

            "#00002F为了回应您的期待，\x01",
            "我今后一定会继续努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x14,
        (
            "#5P#00606F哼，不要搞错。\x02\x03",

            "我只不过是在一番分析之后\x01",
            "讲出了客观事实而已。\x02\x03",

            "#00600F总之，我们只有将\x01",
            "此次事件彻底解决，掌握一切真相，\x01",
            "才能取得更进一步的成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        (
            "#12P#00012F（哈哈，还是这么\x01",
            "  不坦率啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0588
    ChrTalk(
        0x14,
        "#5P#00601F……你在笑什么？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0589
    ChrTalk(
        0x101,
        "#12P#00011F没、没什么！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_128EF")
    Jump("loc_12989")

    label("loc_128EF")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "罗伊德与达德利\x01",
            "习得钢铁雄心Ⅱ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0591
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德与达德利的组合战技\x01",
            "『钢铁雄心』得到了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)

    label("loc_12989")

    OP_E0(0x24, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1D9, 1)
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x14, 0x0)
    EventEnd(0x5)
    Return()

    # Function_53_1215F end

    def Function_54_1299C(): pass

    label("Function_54_1299C")

    EventBegin(0x0)
    Fade(500)
    OP_68(96790, 1200, -101940, 0)
    MoveCamera(48, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 96960, 0, -100830, 180)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x101, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12A73")
    Jump("loc_12ABD")

    label("loc_12A73")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12A93")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12ABD")

    label("loc_12A93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12AB3")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12ABD")

    label("loc_12AB3")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12ABD")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_0D()
    SetChrName("")

    #A0592
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将有关壁障的情况向莉夏做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0593
    ChrTalk(
        0xD,
        (
            "#12P#10704F……看来必须要我\x01",
            "过去才行啊。\x02\x03",

            "#10701F身为与『她』存在着一定牵连的人，我……\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x101,
        (
            "#00003F……那个，莉夏。\x02\x03",

            "#00001F如果你不介意，\x01",
            "就把她交给我们来……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xD,
        (
            "#12P#10706F不。\x02\x03",

            "#10708F从某种意义上说，\x01",
            "我与她的境遇很相似。\x02\x03",

            "就算是为了让自己\x01",
            "寻找到今后的道路……\x02\x03",

            "#10701F我也必须要\x01",
            "再次面对她。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x101,
        (
            "#00006F………明白了。\x02\x03",

            "#00001F如果已经准备好了，我们就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 4)
    SetChrSubChip(0xD, 0x0)
    EventEnd(0x5)
    Return()

    # Function_54_1299C end

    def Function_55_12C97(): pass

    label("Function_55_12C97")

    EventBegin(0x0)
    Fade(500)
    OP_68(101090, 1000, -93870, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100220, 0, -93940, 90)
    SetChrPos(0xA, 101370, 150, -94090, 270)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    SetChrName("")

    #A0597
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将有关壁障的情况向瓦吉做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0598
    ChrTalk(
        0xA,
        (
            "#10404F呼……原来如此啊。\x02\x03",

            "#10408F……真是的，\x01",
            "为什么对我这种人\x01",
            "如此执著啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x101,
        "#6P#00008F瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xA,
        (
            "#10401F看起来，『他』似乎\x01",
            "很希望与我做个彻底的了断。\x02\x03",

            "#10403F罗伊德，让我加入\x01",
            "探索队伍如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，明白了。\x02\x03",

            "#00000F如果已经准备好了，我们就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 0)
    SetChrPos(0xA, 101790, 150, -93960, 90)
    EventEnd(0x5)
    Return()

    # Function_55_12C97 end

    def Function_56_12E51(): pass

    label("Function_56_12E51")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3010, -500, 6090, 0)
    MoveCamera(46, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, -3520, -1500, 5560, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12F28")
    Jump("loc_12F72")

    label("loc_12F28")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12F48")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12F72")

    label("loc_12F48")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12F68")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12F72")

    label("loc_12F68")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12F72")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_93(0x8, 0x104, 0x0)
    EndChrThread(0x8, 0x0)
    OP_0D()

    #C0602
    ChrTalk(
        0xB,
        (
            "#00200F我之前向阿巴斯先生\x01",
            "请教了终端的\x01",
            "使用方法……\x02\x03",

            "#00203F看起来，『梅尔卡瓦』的系统\x01",
            "是由爱普斯泰恩财团制造的。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x101,
        "#00005F哎……是吗！？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xB,
        (
            "#00200F嗯，应该没错。\x02\x03",

            "#00203F我以前也曾在财团总部\x01",
            "见到过教会的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13111")
    Jump("loc_1315B")

    label("loc_13111")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13131")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1315B")

    label("loc_13131")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13151")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1315B")

    label("loc_13151")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1315B")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0605
    ChrTalk(
        0xB,
        (
            "#00200F莫非财团与教会从以前开始\x01",
            "就一直存在协力关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x8,
        (
            "#12100F……这是没有向社会公开的机密情报。\x02\x03",

            "梅尔卡瓦的前身其实是\x01",
            "一种拥有飞翔机能，\x01",
            "名为『天之车』的古代遗物……\x02\x03",

            "导力革命之后，在财团的协助下，\x01",
            "将『天之车』用于舰艇的机关区域，\x01",
            "从而改造成了现在的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x101,
        (
            "#00005F『天之车』……\x01",
            "就是蔡特在看到梅尔卡瓦时\x01",
            "所说的那个名字呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x8,
        (
            "#12100F顺便一说，\x01",
            "在战术导力器的开发工作中，\x01",
            "教会也提供了一定程度的协助。\x02\x03",

            "你们所使用的『导力魔法』，\x01",
            "实际上是教会『法术』的\x01",
            "实用化成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0xB,
        "#00203F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x8,
        (
            "#12100F……我想就算不说你们也该明白，\x01",
            "这些都是未对外界公开的情报，\x01",
            "请一定不要随意泄露。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#00000F嗯，我当然知道。\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xB,
        "#00200F我也明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    OP_93(0x8, 0x13B, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    EventEnd(0x5)
    Return()

    # Function_56_12E51 end

    SaveToFile()

Try(main)
